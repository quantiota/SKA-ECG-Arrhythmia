# SKA learning on arrhythmic ECG — results

**What the SKA learner does with the five waves of the cardiac cycle, in arrhythmic hearts.**

This folder holds the **results** of the SKA engine: the learner's output for every step.
The engine code is not published. The method, the input and the learner's 3D space are the
ones of [SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability/tree/main/ska-ecg-engine),
unchanged.

The records come from the PhysioNet
[MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/), lead MLII, 360 Hz
(no resampling), 30 minutes. Cosine input, scale 25. One run per record: 3,500 steps, five per
cycle. The time between steps is the real time between the peaks of successive waves. Four cubes
per record: the cube (P), the same with the steps into or out of a missing wave tagged (×), the
cube with Δt, the time since the previous wave, as the vertical axis, and the tagged cube with
the MIT-BIH labels.

## Entropic characteristic time of the heart τ_H

The characteristic time of SKA learning, T = η × K ([arXiv:2504.03214](https://arxiv.org/abs/2504.03214), §2.2),
is the time the learner needs to complete its learning. On the ECG stream the time step is Δt_k, the real time
between waves k−1 and k, so it changes from wave to wave. The total time is the integral up to step K, the wave
where the entropy is 90 % saturated (|H| back to 10 % of its minimum; the slowest of the five transitions):

$$
\tau_H = \sum_{k=1}^{K} \Delta t_k = \int_0^{t_K} dt
$$

One value per record: [`results/tau_H.csv`](results/tau_H.csv), computed by [`tau_h.py`](tau_h.py).
The entropy of each run is in `results/<record>/figures/`, to check the saturation.

## Records

| record | sex, age | labels (cycles) | scale | cube | missing waves tagged (×) | Δt | labels |
|---|---|---|---|---|---|---|---|
| mitdb100 | M, 69 | 694 N, 6 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb100_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb100_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb100_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb100_scale25_label_vr.html) |
| mitdb101 | F, 75 | 695 N, 2 ?, 2 A, 1 Q | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb101_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb101_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb101_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb101_scale25_label_vr.html) |
| mitdb103 | M, ? | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb103_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb103_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb103_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb103_scale25_label_vr.html) |
| mitdb105 | F, 73 | 680 N, 20 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb105_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb105_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb105_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb105_scale25_label_vr.html) |
| mitdb106 | F, 24 | 663 N, 37 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb106_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb106_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb106_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb106_scale25_label_vr.html) |
| mitdb107 | M, 63 | 696 /, 4 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb107_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb107_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb107_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb107_scale25_label_vr.html) |
| mitdb108 | F, 87 | 690 N, 8 V, 1 F, 1 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb108_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb108_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb108_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb108_scale25_label_vr.html) |
| mitdb109 | M, 64 | 691 L, 7 V, 2 F | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb109_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb109_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb109_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb109_scale25_label_vr.html) |
| mitdb111 | F, 47 | 699 L, 1 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb111_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb111_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb111_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb111_scale25_label_vr.html) |
| mitdb112 | M, 54 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb112_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb112_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb112_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb112_scale25_label_vr.html) |
| mitdb113 | F, 24 | 696 N, 4 a | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb113_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb113_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb113_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb113_scale25_label_vr.html) |
| mitdb114 | F, 72 | 653 N, 36 V, 5 A, 4 F, 2 J | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb114_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb114_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb114_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb114_scale25_label_vr.html) |
| mitdb115 | F, 39 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb115_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb115_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb115_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb115_scale25_label_vr.html) |
| mitdb116 | M, 68 | 671 N, 29 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb116_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb116_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb116_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb116_scale25_label_vr.html) |
| mitdb117 | M, 69 | 699 N, 1 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb117_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb117_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb117_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb117_scale25_label_vr.html) |
| mitdb118 | M, 69 | 668 R, 26 A, 6 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb118_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb118_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb118_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb118_scale25_label_vr.html) |
| mitdb119 | F, 51 | 553 N, 147 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb119_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb119_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb119_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb119_scale25_label_vr.html) |
| mitdb121 | F, 83 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb121_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb121_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb121_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb121_scale25_label_vr.html) |
| mitdb122 | M, 51 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb122_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb122_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb122_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb122_scale25_label_vr.html) |
| mitdb123 | F, 63 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb123_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb123_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb123_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb123_scale25_label_vr.html) |
| mitdb124 | M, 77 | 646 R, 29 J, 19 V, 3 F, 2 j, 1 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb124_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb124_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb124_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb124_scale25_label_vr.html) |
| mitdb200 | M, 64 | 493 N, 204 V, 3 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb200_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb200_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb200_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb200_scale25_label_vr.html) |
| mitdb201 | M, 68 | 684 N, 6 j, 5 V, 2 a, 2 A, 1 J | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb201_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb201_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb201_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb201_scale25_label_vr.html) |
| mitdb202 | M, 68 | 692 N, 8 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb202_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb202_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb202_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb202_scale25_label_vr.html) |
| mitdb203 | M, 43 | 594 N, 101 V, 2 a, 2 ?, 1 Q | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb203_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb203_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb203_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb203_scale25_label_vr.html) |
| mitdb205 | M, 59 | 683 N, 16 V, 1 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb205_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb205_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb205_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb205_scale25_label_vr.html) |
| mitdb207 | F, 89 | 548 L, 81 R, 41 !, 26 V, 4 ? | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb207_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb207_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb207_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb207_scale25_label_vr.html) |
| mitdb208 | F, 23 | 521 N, 148 F, 31 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb208_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb208_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb208_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb208_scale25_label_vr.html) |
| mitdb209 | M, 62 | 672 N, 28 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb209_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb209_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb209_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb209_scale25_label_vr.html) |
| mitdb210 | M, 89 | 692 N, 8 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb210_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb210_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb210_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb210_scale25_label_vr.html) |
| mitdb212 | F, 32 | 509 R, 191 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb212_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb212_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb212_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb212_scale25_label_vr.html) |
| mitdb213 | M, 61 | 565 N, 94 F, 35 V, 6 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb213_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb213_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb213_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb213_scale25_label_vr.html) |
| mitdb214 | M, 53 | 617 L, 82 V, 1 Q | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb214_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb214_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb214_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb214_scale25_label_vr.html) |
| mitdb215 | M, 81 | 659 N, 39 V, 2 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb215_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb215_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb215_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb215_scale25_label_vr.html) |
| mitdb217 | M, 65 | 569 /, 60 f, 50 V, 21 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb217_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb217_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb217_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb217_scale25_label_vr.html) |
| mitdb219 | M, ? | 693 N, 4 A, 2 V, 1 F | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb219_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb219_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb219_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb219_scale25_label_vr.html) |
| mitdb220 | F, 87 | 676 N, 24 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb220_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb220_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb220_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb220_scale25_label_vr.html) |
| mitdb221 | M, 83 | 688 N, 12 V | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb221_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb221_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb221_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb221_scale25_label_vr.html) |
| mitdb222 | F, 84 | 668 N, 17 A, 15 j | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb222_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb222_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb222_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb222_scale25_label_vr.html) |
| mitdb223 | M, 73 | 656 N, 21 A, 13 V, 6 F, 4 e | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb223_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb223_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb223_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb223_scale25_label_vr.html) |
| mitdb228 | F, 80 | 491 N, 208 V, 1 ? | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb228_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb228_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb228_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb228_scale25_label_vr.html) |
| mitdb230 | M, 32 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb230_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb230_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb230_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb230_scale25_label_vr.html) |
| mitdb231 | F, 72 | 577 R, 120 N, 2 V, 1 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb231_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb231_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb231_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb231_scale25_label_vr.html) |
| mitdb232 | F, 76 | 534 A, 166 R | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb232_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb232_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb232_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb232_scale25_label_vr.html) |
| mitdb233 | M, 57 | 506 N, 186 V, 5 F, 3 A | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb233_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb233_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb233_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb233_scale25_label_vr.html) |
| mitdb234 | F, 56 | 700 N | 25 | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb234_scale25_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb234_scale25_tagged_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb234_scale25_dt_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Arrhythmia/vr/ska_ecg_mitdb234_scale25_label_vr.html) |

## Files

```
build_ecg_vr.py                     fills a cube template with one run (record, scale)
ska_ecg_vr_template.html            the cube (Three.js), placeholders __DATA__ and __DESCRIPTION__
ska_ecg_vr_template_tagged.html     the same, steps into or out of a missing wave drawn as ×
ska_ecg_vr_template_dt.html         the same, vertical axis Δt (ms) instead of P
ska_ecg_vr_template_label.html      the tagged cube with the MIT-BIH labels, click a point to read it
plot_entropy.py                     the entropy figure of each run (H and P along the steps)
tau_h.py                            τ_H of each record, from the run CSVs
results/
├── tau_H.csv                       τ_H and τ of each transition, one row per record
└── <record>/
    ├── ska_<record>_runs.csv       one row per step
    └── figures/                    the entropy figure
```

The cubes are in [`../vr/`](../vr/). To rebuild one:

```bash
python build_ecg_vr.py ska_ecg_vr_template.html results/mitdb100/ska_mitdb100_runs.csv 25 "M, 69" ../vr/ska_ecg_mitdb100_scale25_vr.html
python build_ecg_vr.py ska_ecg_vr_template_tagged.html results/mitdb100/ska_mitdb100_runs.csv 25 "M, 69" ../vr/ska_ecg_mitdb100_scale25_tagged_vr.html tagged
python build_ecg_vr.py ska_ecg_vr_template_dt.html results/mitdb100/ska_mitdb100_runs.csv 25 "M, 69" ../vr/ska_ecg_mitdb100_scale25_dt_vr.html dt
python build_ecg_vr.py ska_ecg_vr_template_label.html results/mitdb100/ska_mitdb100_runs.csv 25 "M, 69" ../vr/ska_ecg_mitdb100_scale25_label_vr.html label ../ecg-data-validation/data/100.atr
```

The label cube reads the MIT-BIH annotation file (`.atr`, from `ecg-data-validation/fetch_data.sh`).

To recompute τ_H and the entropy figures:

```bash
python tau_h.py results results/tau_H.csv
python plot_entropy.py results
```

## Data — `results/<record>/ska_<record>_runs.csv`

The same columns as in SKA-ECG-Heart-Rate-Variability, stored in QuestDB in `ecg_arrhythmia_ska_results`.

| column | meaning |
|---|---|
| `record_id`, `input`, `scale` | the run |
| `event`, `transition` | the wave (P, Q, R, S, T) and the transition into it |
| `event_index`, `k`, `peak` | step n = 5k + j, cycle k, time of the wave's peak in the recording (ms) |
| `value_cos`, `value_sin` | Re c_n, Im c_n (mV); 0 when the wave is absent |
| `value_return` | u_n = Re ċ_n (mV) |
| `x_input` | x_n, what the learner reads |
| `rr` | time from the cycle's P peak to the next cycle's P peak (ms) |
| `knowledge` | z = ‖Z‖ |
| `decision`, `decision_norm` | the learner's last decision D and ‖D‖ |
| `entropy` | H |
| `delta_t` | time since the previous wave (s) |
| `cosine_similarity`, `delta_h_over_delta_d`, `frobenius_norm`, `matrix_size` | learner diagnostics |
| `P`, `zdot`, `zdot_back` | **computed at export**: P = exp(−\|ΔH/H\|) from `entropy`; ż from `knowledge` and `delta_t`, central (`zdot`) and backward (`zdot_back`) difference |
| `timestamp` | the wave's time in the stream |
