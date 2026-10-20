"""
ECG VR cube for a MIT-BIH record: fills the Three.js template with one run of the SKA learner.

The template (ska_ecg_vr_template.html) holds two placeholders:
    __DATA__         the points: z, ż, P and the transition of each step
    __DESCRIPTION__  the line under the title (record, patient, cycles, input, scale)

Usage
    python build_ecg_vr.py ska_ecg_vr_template.html ska_<record>_runs.csv <scale> "<patient>" out.html
    python build_ecg_vr.py ska_ecg_vr_template_tagged.html ska_<record>_runs.csv <scale> "<patient>" out.html tagged
    python build_ecg_vr.py ska_ecg_vr_template_dt.html ska_<record>_runs.csv <scale> "<patient>" out.html dt
    python build_ecg_vr.py ska_ecg_vr_template_label.html ska_<record>_runs.csv <scale> "<patient>" out.html label <record>.atr

With "tagged", a step that goes into or out of a missing wave (value_cos = value_sin = 0) is
marked (D.m = 1); the tagged template draws it as a cross, in its transition colour.
With "label", each cycle also gets its MIT-BIH label (the .atr annotation nearest its R peak,
within 150 ms; "?" if none), shown on click.
    python build_ecg_vr.py ska_ecg_vr_template.html ska_mitdb100_runs.csv 25 "M, 69" ska_ecg_mitdb100_scale25_vr.html
Requires: numpy, pandas
"""
import json
import sys

import numpy as np
import pandas as pd

NAMES = ["P→Q", "Q→R", "R→S", "S→T", "T→P"]
COLORS = ["#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#3987e5"]
FS = 360.0
# MIT-BIH beat annotation codes -> (symbol, meaning)
BEATS = {1: ("N", "normal"), 2: ("L", "left bundle branch block"), 3: ("R", "right bundle branch block"),
         4: ("a", "aberrated atrial premature"), 5: ("V", "premature ventricular contraction"),
         6: ("F", "fusion of ventricular and normal"), 7: ("J", "nodal (junctional) premature"),
         8: ("A", "atrial premature"), 9: ("S", "supraventricular premature"), 10: ("E", "ventricular escape"),
         11: ("j", "nodal (junctional) escape"), 12: ("/", "paced"), 13: ("Q", "unclassifiable"),
         31: ("!", "ventricular flutter wave"), 34: ("e", "atrial escape"), 35: ("n", "supraventricular escape"), 38: ("f", "fusion of paced and normal")}


def read_atr(path):
    """MIT-BIH .atr -> (time in ms, symbol) of every beat annotation."""
    w = np.fromfile(path, dtype="<u2")
    i, s, out = 0, 0, []
    while i < len(w):
        t, v = int(w[i]) >> 10, int(w[i]) & 0x3FF
        i += 1
        if t == 0 and v == 0:
            break
        if t == 59:                                        # SKIP: 32-bit interval in the next two words
            s += (int(w[i]) << 16 | int(w[i + 1])); i += 2
            continue
        if t == 63:                                        # AUX: v bytes
            i += (v + 1) // 2
            continue
        if t in (60, 61, 62):                              # NUM, SUB, CHN
            continue
        s += v
        if t in BEATS:
            out.append((s * 1000.0 / FS, BEATS[t][0]))
    return np.array([o[0] for o in out]), np.array([o[1] for o in out])


def main():
    tpl, csv, scale, patient, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
    label = len(sys.argv) > 6 and sys.argv[6] == "label"              # tagged + a label on click
    tagged = len(sys.argv) > 6 and sys.argv[6] in ("tagged", "label")
    dt = len(sys.argv) > 6 and sys.argv[6] == "dt"                    # vertical axis = delta_t (ms), not P
    d = pd.read_csv(csv, dtype={"record_id": str})
    d = d[(d.input == "cdot_cos") & (d.scale == scale)].sort_values("event_index").reset_index(drop=True)
    missing = (d.value_cos == 0) & (d.value_sin == 0)                  # the wave of this step is missing
    d["m"] = (missing | missing.shift(fill_value=False)).astype(int)   # into it, or out of it
    R = d[d.event == "R"].groupby("k").peak.first()                     # R peak of each cycle (ms)
    d = d.dropna(subset=["P", "zdot"]).reset_index(drop=True)
    if d.empty:
        raise SystemExit(f"no rows for input=cdot_cos scale={scale:g}")
    rec = str(d.record_id.iloc[0])
    tr = d.transition.str.replace("-", "→")
    D = dict(z=d.knowledge.round(2).tolist(), zd=d.zdot.round(3).tolist(), p=d.P.round(4).tolist(),
             t=[NAMES.index(t) for t in tr], names=NAMES, colors=COLORS,
             zmax=float(d.knowledge.max()), zdmax=float(d.zdot.max()))
    if tagged:
        D["m"] = d.m.tolist()
    if label:
        at, sym = read_atr(sys.argv[7])
        j = np.clip(np.searchsorted(at, R.values), 1, len(at) - 1)
        j = np.where(np.abs(at[j - 1] - R.values) < np.abs(at[j] - R.values), j - 1, j)
        lab = dict(zip(R.index, np.where(np.abs(at[j] - R.values) <= 150, sym[j], "?")))
        D.update(lb=[lab.get(k, "?") for k in d.k], lbn={**{b[0]: b[1] for b in BEATS.values()}, "?": "no annotation"})
        cnt = pd.Series([lab[k] for k in d.k.unique() if k in lab]).value_counts()   # cycles with an R wave
        labels = "cycles: " + ", ".join(f"{n} {b} {D['lbn'][b]}" for b, n in cnt.items()) + ", "
        D.update(k=d.k.astype(int).tolist(), n=d.event_index.astype(int).tolist(),
                 tm=(d.peak / 1000).round(3).tolist(), x=d.x_input.round(4).tolist(),
                 dt=(1000 * d.delta_t).round(1).tolist())
    if dt:
        D["p"] = (1000 * d.delta_t).round(1).tolist()
        D["ymax"] = float(1000 * d.delta_t.max())
    desc = (f"Record {rec}, PhysioNet MIT-BIH Arrhythmia Database ({patient}, lead MLII, 360 Hz), "
            + (labels if label else "") +
            f"{d.k.nunique()} cycles = {len(d):,} steps of SKA real-time learning. "
            f"Input: Re ċ (cosine), scale {scale:g}. Horizontal axes: z = ‖Z‖ and ż = dz/dt (1/s); "
            + ("vertical axis: Δt, the time since the previous wave (ms). " if dt else "vertical axis: P = exp(−|ΔH/H|). ")
            + "5 colours = the five transitions of the cardiac cycle.")
    s = open(tpl, encoding="utf-8").read()
    if "__DATA__" not in s or "__DESCRIPTION__" not in s:
        raise SystemExit("template is missing __DATA__ or __DESCRIPTION__")
    s = s.replace("__DATA__", json.dumps(D, separators=(",", ":"), ensure_ascii=False))
    s = s.replace("__DESCRIPTION__", desc)
    open(out, "w", encoding="utf-8").write(s)
    print(f"saved {out}  (record {rec}, {len(d):,} steps)")


if __name__ == "__main__":
    main()
