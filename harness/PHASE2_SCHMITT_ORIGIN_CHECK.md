# Phase 2 — Schmitt screen mismatch diligence (post-run, 2026-09-03)

Input: phase2_types.json (424 schmitt_fvec_mismatch quarantines over groups [85, 86, 88, 95, 96, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142]), schmitt_tetragonal_rows_harvested.json. Frozen setting: origin choice 1 (spacegroups.json setting_convention). Exact chain: sweep_phase2_tetragonal.evaluate (float proposal -> exact clip with certificate -> f-vector).

## (a) Two-origin-choice groups: origin shift search

| group | symbol | mismatched rows | rows total | shifts surviving row-1 screen | shifts reproducing ALL rows | residual rows under best shift |
|---|---|---|---|---|---|---|
| 85 | P4/n | 10 | 13 | 8 | ["('1/4', '3/4', '0')", "('1/4', '3/4', '1/2')", "('3/4', '1/4', '0')", "('3/4', '1/4', '1/2')"] | 0 |
| 86 | P4_2/n | 34 | 36 | 8 | ["('1/4', '1/4', '1/4')", "('1/4', '1/4', '3/4')", "('3/4', '3/4', '1/4')", "('3/4', '3/4', '3/4')"] | 0 |
| 88 | I4_1/a | 50 | 52 | 16 | ["('0', '1/4', '1/8')", "('0', '1/4', '5/8')", "('1/2', '3/4', '1/8')", "('1/2', '3/4', '5/8')"] | 0 |
| 125 | P4/nbm | 4 | 7 | 16 | ["('1/4', '1/4', '0')", "('1/4', '1/4', '1/2')", "('3/4', '3/4', '0')", "('3/4', '3/4', '1/2')"] | 0 |
| 126 | P4/nnc | 15 | 16 | 148 | ["('1/4', '1/4', '1/4')", "('1/4', '1/4', '3/4')", "('3/4', '3/4', '1/4')", "('3/4', '3/4', '3/4')"] | 0 |
| 129 | P4/nmm | 5 | 7 | 16 | ["('1/4', '3/4', '0')", "('1/4', '3/4', '1/2')", "('3/4', '1/4', '0')", "('3/4', '1/4', '1/2')"] | 0 |
| 130 | P4/ncc | 17 | 21 | 8 | ["('1/4', '3/4', '0')", "('1/4', '3/4', '1/2')", "('3/4', '1/4', '0')", "('3/4', '1/4', '1/2')"] | 0 |
| 133 | P4_2/nbc | 18 | 20 | 8 | ["('1/4', '3/4', '1/4')", "('1/4', '3/4', '3/4')", "('3/4', '1/4', '1/4')", "('3/4', '1/4', '3/4')"] | 0 |
| 134 | P4_2/nnm | 26 | 31 | 16 | ["('1/4', '3/4', '1/4')", "('1/4', '3/4', '3/4')", "('3/4', '1/4', '1/4')", "('3/4', '1/4', '3/4')"] | 0 |
| 137 | P4_2/nmc | 15 | 16 | 188 | ["('1/4', '3/4', '1/4')", "('1/4', '3/4', '3/4')", "('3/4', '1/4', '1/4')", "('3/4', '1/4', '3/4')"] | 0 |
| 138 | P4_2/ncm | 17 | 19 | 16 | ["('1/4', '3/4', '1/4')", "('1/4', '3/4', '3/4')", "('3/4', '1/4', '1/4')", "('3/4', '1/4', '3/4')"] | 0 |
| 141 | I4_1/amd | 60 | 65 | 16 | ["('0', '3/4', '1/8')", "('0', '3/4', '5/8')", "('1/2', '1/4', '1/8')", "('1/2', '1/4', '5/8')"] | 0 |
| 142 | I4_1/acd | 46 | 52 | 32 | ["('0', '3/4', '1/8')", "('0', '3/4', '5/8')", "('1/2', '1/4', '1/8')", "('1/2', '1/4', '5/8')"] | 0 |

## (b) Second members of enantiomorphic pairs: signed-axis transforms of the printed point (printed for the first member)

| group | symbol | mismatched rows | rows total | transforms reproducing ALL rows (sx,sy,sz,swap) | best residual |
|---|---|---|---|---|---|
| 95 | P4_322 | 62 | 84 | ['(1, 1, -1, False)', '(1, -1, 1, False)', '(-1, 1, 1, False)', '(-1, -1, -1, False)'] | 0 |
| 96 | P4_32_12 | 45 | 69 | ['(1, 1, 1, True)', '(1, 1, -1, False)', '(-1, -1, 1, True)', '(-1, -1, -1, False)'] | 0 |

## (c) Mismatches outside both classes


Wall 438 s, 12 workers. This check explains mismatches as coordinate-convention effects where a single shift/transform reproduces ALL printed rows of a group; anything else stays an open mismatch (recorded, not explained away).
