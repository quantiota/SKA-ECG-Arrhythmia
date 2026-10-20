# SKA ECG Arrhythmia

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)


**Structured Knowledge Accumulation (SKA) on arrhythmic ECG**

This project applies the SKA real-time learner to arrhythmic hearts, from the PhysioNet
[MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/).

The method is the one of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability):
the five waves of each cardiac cycle, the same input, the same learner, the same 3D cube.

A wave that is not found in a cycle is sent with c = 0, as in the first prototype of
[SKA-ECG-Pathology](https://github.com/quantiota/SKA-ECG-Pathology).

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

## Cases

Lead MLII, 360 Hz (no resampling), scale 25. Each record lasts 30 minutes; the run is its first
3,500 steps (700 cycles). Records 102 and 104 have no MLII lead and are not used: 46 records.
Labels counted over the 700 cycles of the run.

| record | sex, age | labels (cycles) |
|---|---|---|
| mitdb100 | M, 69 | 694 N, 6 A |
| mitdb101 | F, 75 | 695 N, 2 ?, 2 A, 1 Q |
| mitdb103 | M, ? | 700 N |
| mitdb105 | F, 73 | 680 N, 20 V |
| mitdb106 | F, 24 | 663 N, 37 V |
| mitdb107 | M, 63 | 696 /, 4 V |
| mitdb108 | F, 87 | 690 N, 8 V, 1 F, 1 A |
| mitdb109 | M, 64 | 691 L, 7 V, 2 F |
| mitdb111 | F, 47 | 699 L, 1 V |
| mitdb112 | M, 54 | 700 N |
| mitdb113 | F, 24 | 696 N, 4 a |
| mitdb114 | F, 72 | 653 N, 36 V, 5 A, 4 F, 2 J |
| mitdb115 | F, 39 | 700 N |
| mitdb116 | M, 68 | 671 N, 29 V |
| mitdb117 | M, 69 | 699 N, 1 A |
| mitdb118 | M, 69 | 668 R, 26 A, 6 V |
| mitdb119 | F, 51 | 553 N, 147 V |
| mitdb121 | F, 83 | 700 N |
| mitdb122 | M, 51 | 700 N |
| mitdb123 | F, 63 | 700 N |
| mitdb124 | M, 77 | 646 R, 29 J, 19 V, 3 F, 2 j, 1 A |
| mitdb200 | M, 64 | 493 N, 204 V, 3 A |
| mitdb201 | M, 68 | 684 N, 6 j, 5 V, 2 a, 2 A, 1 J |
| mitdb202 | M, 68 | 692 N, 8 A |
| mitdb203 | M, 43 | 594 N, 101 V, 2 a, 2 ?, 1 Q |
| mitdb205 | M, 59 | 683 N, 16 V, 1 A |
| mitdb207 | F, 89 | 548 L, 81 R, 41 !, 26 V, 4 ? |
| mitdb208 | F, 23 | 521 N, 148 F, 31 V |
| mitdb209 | M, 62 | 672 N, 28 A |
| mitdb210 | M, 89 | 692 N, 8 V |
| mitdb212 | F, 32 | 509 R, 191 N |
| mitdb213 | M, 61 | 565 N, 94 F, 35 V, 6 A |
| mitdb214 | M, 53 | 617 L, 82 V, 1 Q |
| mitdb215 | M, 81 | 659 N, 39 V, 2 A |
| mitdb217 | M, 65 | 569 /, 60 f, 50 V, 21 N |
| mitdb219 | M, ? | 693 N, 4 A, 2 V, 1 F |
| mitdb220 | F, 87 | 676 N, 24 A |
| mitdb221 | M, 83 | 688 N, 12 V |
| mitdb222 | F, 84 | 668 N, 17 A, 15 j |
| mitdb223 | M, 73 | 656 N, 21 A, 13 V, 6 F, 4 e |
| mitdb228 | F, 80 | 491 N, 208 V, 1 ? |
| mitdb230 | M, 32 | 700 N |
| mitdb231 | F, 72 | 577 R, 120 N, 2 V, 1 A |
| mitdb232 | F, 76 | 534 A, 166 R |
| mitdb233 | M, 57 | 506 N, 186 V, 5 F, 3 A |
| mitdb234 | F, 56 | 700 N |


## Repository

- [`ecg-data-validation/`](ecg-data-validation/): streams the MIT-BIH records into QuestDB (`ecg_arrhythmia_steps`)
- [`ska-ecg-engine/results/`](ska-ecg-engine/results/): the SKA output of each record (`ecg_arrhythmia_ska_results`)
- [`vr/`](vr/): the 3D cubes

The SKA real-time engine is proprietary and is not included in this repository.


## License

MIT. ECG data: from PhysioNet, under the license of the MIT-BIH Arrhythmia Database; cite the
database when you use it.
