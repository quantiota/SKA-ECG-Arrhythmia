# SKA ECG Arrhythmia

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)


**Structured Knowledge Accumulation (SKA) on arrhythmic ECG**

This project applies the SKA real-time learner to the 48 records of the PhysioNet
[MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/).

The method is the one of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability):
the five waves of each cardiac cycle, the same input, the same learner, the same 3D cube.

## Data

Lead MLII, 360 Hz (no resampling), 30 minutes per record. Records 102 and 104 have no MLII
lead and are not used: 46 records. One step is one wave, and the time between steps is the
real time between the peaks of successive waves. One run per record: input cosine, scale 25,
3,500 steps (700 cycles).

A wave that is not found in a cycle is sent with c = 0 (the first prototype of
[SKA-ECG-Pathology](https://github.com/quantiota/SKA-ECG-Pathology)).

## Labels

Every cycle of MIT-BIH was annotated by cardiologists. Each cycle of the learner gets the label of
the annotation nearest its R peak (within 150 ms). The labels of a record are in the title of its
label cube; clicking a point (a transition) shows its transition, the label of its cycle, the
cycle number and the time in the recording.

| label | meaning |
|---|---|
| N | normal |
| L | left bundle branch block |
| R | right bundle branch block |
| A | atrial premature |
| a | aberrated atrial premature |
| J | nodal (junctional) premature |
| S | supraventricular premature |
| V | premature ventricular contraction |
| F | fusion of ventricular and normal |
| ! | ventricular flutter wave |
| e | atrial escape |
| j | nodal (junctional) escape |
| n | supraventricular escape |
| E | ventricular escape |
| / | paced |
| f | fusion of paced and normal |
| Q | unclassifiable |
| ? | no annotation within 150 ms |

N means a normal cycle, not a healthy heart: every MIT-BIH record is from a patient.

## Entropic characteristic time τ_H

τ_H is the total learning time until the entropy is 90 % saturated, the integral of the time
between waves up to step K (definition in
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability/tree/main/ska-ecg-engine),
[arXiv:2504.03214](https://arxiv.org/abs/2504.03214)):

$$
\tau_H = \sum_{k=1}^{K} \Delta t_k = \int_0^{t_K} dt
$$

## Cases

Labels counted over the 700 cycles of the run.

| record | sex, age | labels (cycles) | τ_H (min) | cube |
|---|---|---|---|---|
| 100 | M, 69 | 694 N, 6 A | 7.2 | [cube](vr/ska_ecg_mitdb100_scale25_label_vr.html) |
| 101 | F, 75 | 695 N, 2 ?, 2 A, 1 Q | 10.0 | [cube](vr/ska_ecg_mitdb101_scale25_label_vr.html) |
| 103 | M, ? | 700 N | 9.3 | [cube](vr/ska_ecg_mitdb103_scale25_label_vr.html) |
| 105 | F, 73 | 680 N, 20 V | 5.8 | [cube](vr/ska_ecg_mitdb105_scale25_label_vr.html) |
| 106 | F, 24 | 663 N, 37 V | 10.9 | [cube](vr/ska_ecg_mitdb106_scale25_label_vr.html) |
| 107 | M, 63 | 696 /, 4 V | 8.4 | [cube](vr/ska_ecg_mitdb107_scale25_label_vr.html) |
| 108 | F, 87 | 690 N, 8 V, 1 F, 1 A | 10.2 | [cube](vr/ska_ecg_mitdb108_scale25_label_vr.html) |
| 109 | M, 64 | 691 L, 7 V, 2 F | not saturated | [cube](vr/ska_ecg_mitdb109_scale25_label_vr.html) |
| 111 | F, 47 | 699 L, 1 V | 7.5 | [cube](vr/ska_ecg_mitdb111_scale25_label_vr.html) |
| 112 | M, 54 | 700 N | 5.9 | [cube](vr/ska_ecg_mitdb112_scale25_label_vr.html) |
| 113 | F, 24 | 696 N, 4 a | 11.0 | [cube](vr/ska_ecg_mitdb113_scale25_label_vr.html) |
| 114 | F, 72 | 653 N, 36 V, 5 A, 4 F, 2 J | 8.6 | [cube](vr/ska_ecg_mitdb114_scale25_label_vr.html) |
| 115 | F, 39 | 700 N | 10.3 | [cube](vr/ska_ecg_mitdb115_scale25_label_vr.html) |
| 116 | M, 68 | 671 N, 29 V | 6.9 | [cube](vr/ska_ecg_mitdb116_scale25_label_vr.html) |
| 117 | M, 69 | 699 N, 1 A | 13.3 | [cube](vr/ska_ecg_mitdb117_scale25_label_vr.html) |
| 118 | M, 69 | 668 R, 26 A, 6 V | 6.5 | [cube](vr/ska_ecg_mitdb118_scale25_label_vr.html) |
| 119 | F, 51 | 553 N, 147 V | 9.2 | [cube](vr/ska_ecg_mitdb119_scale25_label_vr.html) |
| 121 | F, 83 | 700 N | 10.2 | [cube](vr/ska_ecg_mitdb121_scale25_label_vr.html) |
| 122 | M, 51 | 700 N | 7.3 | [cube](vr/ska_ecg_mitdb122_scale25_label_vr.html) |
| 123 | F, 63 | 700 N | 13.0 | [cube](vr/ska_ecg_mitdb123_scale25_label_vr.html) |
| 124 | M, 77 | 646 R, 29 J, 19 V, 3 F, 2 j, 1 A | 12.3 | [cube](vr/ska_ecg_mitdb124_scale25_label_vr.html) |
| 200 | M, 64 | 493 N, 204 V, 3 A | 5.8 | [cube](vr/ska_ecg_mitdb200_scale25_label_vr.html) |
| 201 | M, 68 | 684 N, 6 j, 5 V, 2 a, 2 A, 1 J | 5.8 | [cube](vr/ska_ecg_mitdb201_scale25_label_vr.html) |
| 202 | M, 68 | 692 N, 8 A | 11.4 | [cube](vr/ska_ecg_mitdb202_scale25_label_vr.html) |
| 203 | M, 43 | 594 N, 101 V, 2 a, 2 ?, 1 Q | 6.6 | [cube](vr/ska_ecg_mitdb203_scale25_label_vr.html) |
| 205 | M, 59 | 683 N, 16 V, 1 A | 6.3 | [cube](vr/ska_ecg_mitdb205_scale25_label_vr.html) |
| 207 | F, 89 | 548 L, 81 R, 41 !, 26 V, 4 ? | 7.8 | [cube](vr/ska_ecg_mitdb207_scale25_label_vr.html) |
| 208 | F, 23 | 521 N, 148 F, 31 V | 6.1 | [cube](vr/ska_ecg_mitdb208_scale25_label_vr.html) |
| 209 | M, 62 | 672 N, 28 A | 5.2 | [cube](vr/ska_ecg_mitdb209_scale25_label_vr.html) |
| 210 | M, 89 | 692 N, 8 V | 6.8 | [cube](vr/ska_ecg_mitdb210_scale25_label_vr.html) |
| 212 | F, 32 | 509 R, 191 N | 6.0 | [cube](vr/ska_ecg_mitdb212_scale25_label_vr.html) |
| 213 | M, 61 | 565 N, 94 F, 35 V, 6 A | 4.3 | [cube](vr/ska_ecg_mitdb213_scale25_label_vr.html) |
| 214 | M, 53 | 617 L, 82 V, 1 Q | 7.2 | [cube](vr/ska_ecg_mitdb214_scale25_label_vr.html) |
| 215 | M, 81 | 659 N, 39 V, 2 A | 5.1 | [cube](vr/ska_ecg_mitdb215_scale25_label_vr.html) |
| 217 | M, 65 | 569 /, 60 f, 50 V, 21 N | 6.4 | [cube](vr/ska_ecg_mitdb217_scale25_label_vr.html) |
| 219 | M, ? | 693 N, 4 A, 2 V, 1 F | 6.6 | [cube](vr/ska_ecg_mitdb219_scale25_label_vr.html) |
| 220 | F, 87 | 676 N, 24 A | 8.7 | [cube](vr/ska_ecg_mitdb220_scale25_label_vr.html) |
| 221 | M, 83 | 688 N, 12 V | 7.8 | [cube](vr/ska_ecg_mitdb221_scale25_label_vr.html) |
| 222 | F, 84 | 668 N, 17 A, 15 j | 9.0 | [cube](vr/ska_ecg_mitdb222_scale25_label_vr.html) |
| 223 | M, 73 | 656 N, 21 A, 13 V, 6 F, 4 e | 5.8 | [cube](vr/ska_ecg_mitdb223_scale25_label_vr.html) |
| 228 | F, 80 | 491 N, 208 V, 1 ? | 11.6 | [cube](vr/ska_ecg_mitdb228_scale25_label_vr.html) |
| 230 | M, 32 | 700 N | 8.3 | [cube](vr/ska_ecg_mitdb230_scale25_label_vr.html) |
| 231 | F, 72 | 577 R, 120 N, 2 V, 1 A | 12.4 | [cube](vr/ska_ecg_mitdb231_scale25_label_vr.html) |
| 232 | F, 76 | 534 A, 166 R | 9.0 | [cube](vr/ska_ecg_mitdb232_scale25_label_vr.html) |
| 233 | M, 57 | 506 N, 186 V, 5 F, 3 A | 4.3 | [cube](vr/ska_ecg_mitdb233_scale25_label_vr.html) |
| 234 | F, 56 | 700 N | 5.7 | [cube](vr/ska_ecg_mitdb234_scale25_label_vr.html) |

Each record has four cubes in [`vr/`](vr/): `_vr` (the transitions), `_tagged_vr` (a step into or
out of a missing wave drawn as a cross), `_dt_vr` (vertical axis Δt) and `_label_vr` (tagged, with
the labels).

## Repository

- [`ecg-data-validation/`](ecg-data-validation/): downloads the MIT-BIH records (`fetch_data.sh`) and streams them into QuestDB (`ecg_arrhythmia_steps`)
- [`ska-ecg-engine/`](ska-ecg-engine/): the SKA output of each record (`ecg_arrhythmia_ska_results`), the entropy figures, τ_H and the cube builder
- [`vr/`](vr/): the 3D cubes

The SKA real-time engine is proprietary and is not included in this repository.

To rebuild a label cube:

```bash
cd ska-ecg-engine
python build_ecg_vr.py ska_ecg_vr_template_label.html results/mitdb100/ska_mitdb100_runs.csv 25 "M, 69" ../vr/ska_ecg_mitdb100_scale25_label_vr.html label ../ecg-data-validation/data/100.atr
```

To recompute τ_H and the entropy figures:

```bash
cd ska-ecg-engine
python tau_h.py results results/tau_H.csv
python plot_entropy.py results
```


## License

MIT. ECG data: from PhysioNet, under the license of the MIT-BIH Arrhythmia Database; cite the
database when you use it.
