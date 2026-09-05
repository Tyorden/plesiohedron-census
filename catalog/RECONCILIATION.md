# RECONCILIATION - the catalog vs Schmitt 2016's printed tables, f-vector level

Built by `catalog/reconcile_schmitt.py` from `catalog/catalog.json` (snapshot 2026-09-04); deterministic. Cubic tables: `harness/triage_phase1.py` SCHMITT_FVECTORS (881 rows, Sec. 2.2.5, printed pp. 119-150; 386 rows independently re-keyed, `harness/rekey_tables.json`; the other 495 rows single-pass). Tetragonal tables: `harness/schmitt_tetragonal_tables.json` (1,476 rows, Sec. 2.2.2, printed pp. 27-81; single-pass visual read cross-checked against the text layer, NOT independently re-keyed). Every printed row passed Euler V-E+F=2 here.

**Wording rule, stated once and binding for every line below.** An f-vector match is NOT type identity (the Josehedron and Schmitt's IT(220) (12,22,12) cell share an f-vector and are different types; the accepted collision screens found the same for six more pairs). Absence of an f-vector from his table is evidence, not proof, of anything: his chapter 2 is a 351-CPU-year exact GRID SAMPLING that prints one representative per (group, f-vector), not an enumeration (ANCHORS.md G5 amendment). Conversely, his rows that our menu did not reach are a COVERAGE GAP OF OUR SWEEP, not a statement about his data. Everything is 'not matched against the records checked as of 2026-09-04'; the literature facet maximum is an observed 38, not a proven bound.

## Definitions

- **Our menu** = the program's own sample points: phase 1 (cubic) every stored orbit; phase 2 (tetragonal) passes P1 (grid x 13 coarse c/a), P3 (5 printed c/a x grid), P4 (1/24 line orbits), P5 (c/a bisection). Phase-2 pass **P2** evaluated his printed generating points themselves; a P2 sighting reproduces his row by construction and is therefore reported separately and never counted as coverage.
- **(a) ours-in-his**: distinct f-vectors of our menu-sighted types in g that his table for g prints (and how many of our types sit at those f-vectors).
- **(b) ours-not-his**: our menu f-vectors in g absent from his table for g.
- **(c) his-not-ours**: his printed f-vectors for g that our menu did not reach in g (coverage gap of our sweep), split into rows whose cell IS in the store because P2 reproduced it at his own point, and rows with no stored type at all (tetragonal: the 13 two-origin groups and IT(95)/(96) whose printed coordinates needed a setting conversion that the read-only origin check applied but the store did not absorb, plus the two order_cycle rows; cubic: there was no P2-style pass in phase 1).
- Shared printed tables (212/213; 76/78, 91/95, 92/96) give both groups the same printed set; our sightings are per group.

## Cubic (36 groups; his rows 881)

Headline (sums over groups; a (group, f-vector) pair counts once per group):

- his distinct (group, f) pairs: **986** (986 (group, row) pairs from 881 printed rows; a shared table is counted once per group it serves)
- (a) ours-in-his: **292** (group, f) pairs, carrying **309** of our (type, group) sightings-by-menu
- (b) ours-not-his: **33** (group, f) pairs, carrying **34** of our (type, group) menu sightings
- (c) his-not-ours: **694** (group, f) pairs = 694 printed rows our menu never reached in that group (coverage gap of our sweep); of these 0 have his cell stored via P2 and 694 have no stored type at all
- whole-system distinct f-vectors: his 194, our menu 63, shared 62; ours not printed in ANY cubic table: 1 ((16,25,11)); his f-vectors unreached by our menu anywhere in the system: 132

Per group (full (group, f)-level table in `reconciliation_cubic.csv`):

| IT | symbol | his rows | his f | our types (menu) | our f (menu) | (a) f matched | (a) our types | (b) our f absent | (b) our types | (c) his f unreached | (c) stored via P2 | (c) not stored | coverage a/his |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 195 | P23 | 9 | 9 | 6 | 6 | 6 | 6 | 0 | 0 | 3 | 0 | 3 | 6/9 |
| 196 | F23 | 5 | 5 | 4 | 4 | 4 | 4 | 0 | 0 | 1 | 0 | 1 | 4/5 |
| 197 | I23 | 27 | 27 | 8 | 8 | 8 | 8 | 0 | 0 | 19 | 0 | 19 | 8/27 |
| 198 | P2_13 | 18 | 18 | 4 | 4 | 4 | 4 | 0 | 0 | 14 | 0 | 14 | 4/18 |
| 199 | I2_13 | 44 | 44 | 8 | 7 | 6 | 6 | 1 | 2 | 38 | 0 | 38 | 6/44 |
| 200 | Pm-3 | 7 | 7 | 7 | 7 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 7/7 |
| 201 | Pn-3 | 16 | 16 | 9 | 9 | 5 | 5 | 4 | 4 | 11 | 0 | 11 | 5/16 |
| 202 | Fm-3 | 8 | 8 | 7 | 7 | 7 | 7 | 0 | 0 | 1 | 0 | 1 | 7/8 |
| 203 | Fd-3 | 12 | 12 | 8 | 7 | 6 | 7 | 1 | 1 | 6 | 0 | 6 | 6/12 |
| 204 | Im-3 | 21 | 21 | 17 | 15 | 15 | 17 | 0 | 0 | 6 | 0 | 6 | 15/21 |
| 205 | Pa-3 | 24 | 24 | 5 | 5 | 5 | 5 | 0 | 0 | 19 | 0 | 19 | 5/24 |
| 206 | Ia-3 | 72 | 72 | 7 | 6 | 4 | 5 | 2 | 2 | 68 | 0 | 68 | 4/72 |
| 207 | P432 | 6 | 6 | 6 | 6 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 6/6 |
| 208 | P4_232 | 27 | 27 | 10 | 10 | 10 | 10 | 0 | 0 | 17 | 0 | 17 | 10/27 |
| 209 | F432 | 7 | 7 | 6 | 6 | 6 | 6 | 0 | 0 | 1 | 0 | 1 | 6/7 |
| 210 | F4_132 | 18 | 18 | 9 | 9 | 8 | 8 | 1 | 1 | 10 | 0 | 10 | 8/18 |
| 211 | I432 | 27 | 27 | 15 | 15 | 15 | 15 | 0 | 0 | 12 | 0 | 12 | 15/27 |
| 212 | P4_332 | 105 | 105 | 11 | 10 | 10 | 11 | 0 | 0 | 95 | 0 | 95 | 10/105 |
| 213 | P4_132 | 105 | 105 | 11 | 10 | 10 | 11 | 0 | 0 | 95 | 0 | 95 | 10/105 |
| 214 | I4_132 | 102 | 102 | 13 | 11 | 9 | 11 | 2 | 2 | 93 | 0 | 93 | 9/102 |
| 215 | P-43m | 8 | 8 | 8 | 8 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 8/8 |
| 216 | F-43m | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 5/5 |
| 217 | I-43m | 20 | 20 | 14 | 14 | 14 | 14 | 0 | 0 | 6 | 0 | 6 | 14/20 |
| 218 | P-43n | 30 | 30 | 8 | 8 | 8 | 8 | 0 | 0 | 22 | 0 | 22 | 8/30 |
| 219 | F-43c | 8 | 8 | 5 | 4 | 4 | 5 | 0 | 0 | 4 | 0 | 4 | 4/8 |
| 220 | I-43d | 62 | 62 | 10 | 10 | 9 | 9 | 1 | 1 | 53 | 0 | 53 | 9/62 |
| 221 | Pm-3m | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 5/5 |
| 222 | Pn-3n | 11 | 11 | 13 | 13 | 7 | 7 | 6 | 6 | 4 | 0 | 4 | 7/11 |
| 223 | Pm-3n | 20 | 20 | 20 | 16 | 16 | 20 | 0 | 0 | 4 | 0 | 4 | 16/20 |
| 224 | Pn-3m | 8 | 8 | 18 | 18 | 8 | 8 | 10 | 10 | 0 | 0 | 0 | 8/8 |
| 225 | Fm-3m | 6 | 6 | 6 | 6 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 6/6 |
| 226 | Fm-3c | 7 | 7 | 7 | 7 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 7/7 |
| 227 | Fd-3m | 11 | 11 | 12 | 11 | 10 | 11 | 1 | 1 | 1 | 0 | 1 | 10/11 |
| 228 | Fd-3c | 16 | 16 | 8 | 7 | 5 | 6 | 2 | 2 | 11 | 0 | 11 | 5/16 |
| 229 | Im-3m | 16 | 16 | 17 | 16 | 16 | 17 | 0 | 0 | 0 | 0 | 0 | 16/16 |
| 230 | Ia-3d | 93 | 93 | 16 | 15 | 13 | 14 | 2 | 2 | 80 | 0 | 80 | 13/93 |

## Tetragonal (68 groups; his rows 1476)

Headline (sums over groups; a (group, f-vector) pair counts once per group):

- his distinct (group, f) pairs: **1639** (1641 (group, row) pairs from 1476 printed rows; a shared table is counted once per group it serves)
- (a) ours-in-his: **700** (group, f) pairs, carrying **988** of our (type, group) sightings-by-menu; of these 355 pairs match at a c/a value we also sampled
- (b) ours-not-his: **67** (group, f) pairs, carrying **68** of our (type, group) menu sightings
- (c) his-not-ours: **939** (group, f) pairs = 941 printed rows our menu never reached in that group (coverage gap of our sweep); of these 669 have his cell stored via P2 and 270 have no stored type at all
- whole-system distinct f-vectors: his 163, our menu 80, shared 80; ours not printed in ANY tetragonal table: 0 (none); his f-vectors unreached by our menu anywhere in the system: 83 (even counting P2: 4)

Per group (full (group, f)-level table in `reconciliation_tetragonal.csv`):

| IT | symbol | his rows | his f | our types (menu) | our f (menu) | (a) f matched | (a) our types | (a) same c/a | (b) our f absent | (b) our types | (c) his f unreached | (c) stored via P2 | (c) not stored | coverage a/his |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 75 | P4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 2/3 |
| 76 | P4_1 | 12 | 12 | 18 | 7 | 7 | 18 | 3 | 0 | 0 | 5 | 5 | 0 | 7/12 |
| 77 | P4_2 | 8 | 8 | 7 | 6 | 6 | 7 | 3 | 0 | 0 | 2 | 2 | 0 | 6/8 |
| 78 | P4_3 | 12 | 12 | 18 | 7 | 7 | 18 | 3 | 0 | 0 | 5 | 5 | 0 | 7/12 |
| 79 | I4 | 10 | 10 | 6 | 6 | 6 | 6 | 5 | 0 | 0 | 4 | 4 | 0 | 6/10 |
| 80 | I4_1 | 27 | 27 | 22 | 12 | 12 | 22 | 4 | 0 | 0 | 15 | 15 | 0 | 12/27 |
| 81 | P-4 | 16 | 16 | 8 | 7 | 7 | 8 | 3 | 0 | 0 | 9 | 9 | 0 | 7/16 |
| 82 | I-4 | 40 | 40 | 13 | 9 | 9 | 13 | 5 | 0 | 0 | 31 | 31 | 0 | 9/40 |
| 83 | P4/m | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 84 | P4_2/m | 25 | 25 | 20 | 17 | 17 | 20 | 9 | 0 | 0 | 8 | 8 | 0 | 17/25 |
| 85 | P4/n | 13 | 13 | 8 | 8 | 5 | 5 | 2 | 3 | 3 | 8 | 1 | 7 | 5/13 |
| 86 | P4_2/n | 36 | 36 | 23 | 12 | 11 | 22 | 4 | 1 | 1 | 25 | 0 | 25 | 11/36 |
| 87 | I4/m | 23 | 23 | 20 | 18 | 18 | 20 | 9 | 0 | 0 | 5 | 5 | 0 | 18/23 |
| 88 | I4_1/a | 52 | 52 | 37 | 17 | 13 | 33 | 4 | 4 | 4 | 39 | 0 | 39 | 13/52 |
| 89 | P422 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 0 | 0 | 1 | 1 | 0 | 4/5 |
| 90 | P42_12 | 14 | 14 | 8 | 8 | 7 | 7 | 4 | 1 | 1 | 7 | 7 | 0 | 7/14 |
| 91 | P4_122 | 84 | 83 | 26 | 24 | 24 | 26 | 6 | 0 | 0 | 59 | 59 | 0 | 24/83 |
| 92 | P4_12_12 | 69 | 69 | 36 | 13 | 12 | 35 | 5 | 1 | 1 | 57 | 57 | 0 | 12/69 |
| 93 | P4_222 | 32 | 32 | 19 | 15 | 15 | 19 | 6 | 0 | 0 | 17 | 17 | 0 | 15/32 |
| 94 | P4_22_12 | 42 | 42 | 21 | 15 | 14 | 20 | 5 | 1 | 1 | 28 | 28 | 0 | 14/42 |
| 95 | P4_322 | 84 | 83 | 25 | 18 | 18 | 25 | 5 | 0 | 0 | 65 | 18 | 47 | 18/83 |
| 96 | P4_32_12 | 69 | 69 | 35 | 13 | 12 | 34 | 5 | 1 | 1 | 57 | 21 | 36 | 12/69 |
| 97 | I422 | 35 | 35 | 18 | 18 | 18 | 18 | 9 | 0 | 0 | 17 | 17 | 0 | 18/35 |
| 98 | I4_122 | 130 | 130 | 54 | 26 | 25 | 53 | 11 | 1 | 1 | 105 | 105 | 0 | 25/130 |
| 99 | P4mm | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2/2 |
| 100 | P4bm | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 2/3 |
| 101 | P4_2cm | 6 | 6 | 6 | 6 | 5 | 5 | 3 | 1 | 1 | 1 | 1 | 0 | 5/6 |
| 102 | P4_2nm | 8 | 8 | 9 | 9 | 7 | 7 | 6 | 2 | 2 | 1 | 1 | 0 | 7/8 |
| 103 | P4cc | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 1 | 1 | 0 | 3/4 |
| 104 | P4nc | 10 | 10 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 5 | 5 | 0 | 5/10 |
| 105 | P4_2mc | 5 | 5 | 7 | 6 | 5 | 6 | 5 | 1 | 1 | 0 | 0 | 0 | 5/5 |
| 106 | P4_2bc | 7 | 7 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 4 | 4 | 0 | 3/7 |
| 107 | I4mm | 8 | 8 | 10 | 10 | 8 | 8 | 7 | 2 | 2 | 0 | 0 | 0 | 8/8 |
| 108 | I4cm | 6 | 6 | 5 | 5 | 5 | 5 | 4 | 0 | 0 | 1 | 1 | 0 | 5/6 |
| 109 | I4_1md | 15 | 15 | 19 | 16 | 15 | 18 | 8 | 1 | 1 | 0 | 0 | 0 | 15/15 |
| 110 | I4_1cd | 14 | 14 | 18 | 8 | 8 | 18 | 6 | 0 | 0 | 6 | 6 | 0 | 8/14 |
| 111 | P-42m | 8 | 8 | 7 | 7 | 7 | 7 | 4 | 0 | 0 | 1 | 1 | 0 | 7/8 |
| 112 | P-42c | 20 | 20 | 12 | 11 | 10 | 11 | 5 | 1 | 1 | 10 | 10 | 0 | 10/20 |
| 113 | P-42_1m | 15 | 15 | 10 | 10 | 10 | 10 | 4 | 0 | 0 | 5 | 5 | 0 | 10/15 |
| 114 | P-42_1c | 32 | 32 | 14 | 11 | 10 | 13 | 4 | 1 | 1 | 22 | 22 | 0 | 10/32 |
| 115 | P-4m2 | 8 | 8 | 9 | 8 | 7 | 8 | 4 | 1 | 1 | 1 | 1 | 0 | 7/8 |
| 116 | P-4c2 | 31 | 31 | 15 | 12 | 12 | 15 | 3 | 0 | 0 | 19 | 19 | 0 | 12/31 |
| 117 | P-4b2 | 8 | 8 | 4 | 4 | 4 | 4 | 3 | 0 | 0 | 4 | 4 | 0 | 4/8 |
| 118 | P-4n2 | 53 | 53 | 19 | 16 | 15 | 18 | 7 | 1 | 1 | 38 | 38 | 0 | 15/53 |
| 119 | I-4m2 | 22 | 22 | 19 | 16 | 16 | 19 | 9 | 0 | 0 | 6 | 6 | 0 | 16/22 |
| 120 | I-4c2 | 17 | 17 | 7 | 7 | 7 | 7 | 3 | 0 | 0 | 10 | 10 | 0 | 7/17 |
| 121 | I-42m | 24 | 24 | 20 | 18 | 17 | 19 | 8 | 1 | 1 | 7 | 7 | 0 | 17/24 |
| 122 | I-42d | 101 | 101 | 43 | 17 | 17 | 43 | 7 | 0 | 0 | 84 | 84 | 0 | 17/101 |
| 123 | P4/mmm | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2/2 |
| 124 | P4/mcc | 7 | 7 | 6 | 6 | 6 | 6 | 4 | 0 | 0 | 1 | 1 | 0 | 6/7 |
| 125 | P4/nbm | 7 | 7 | 6 | 6 | 6 | 6 | 4 | 0 | 0 | 1 | 0 | 1 | 6/7 |
| 126 | P4/nnc | 16 | 16 | 15 | 15 | 9 | 9 | 4 | 6 | 6 | 7 | 1 | 6 | 9/16 |
| 127 | P4/mbm | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 128 | P4/mnc | 21 | 21 | 19 | 18 | 17 | 18 | 10 | 1 | 1 | 4 | 4 | 0 | 17/21 |
| 129 | P4/nmm | 7 | 7 | 11 | 11 | 6 | 6 | 3 | 5 | 5 | 1 | 0 | 1 | 6/7 |
| 130 | P4/ncc | 21 | 21 | 12 | 12 | 9 | 9 | 3 | 3 | 3 | 12 | 2 | 10 | 9/21 |
| 131 | P4_2/mmc | 11 | 11 | 14 | 12 | 11 | 13 | 7 | 1 | 1 | 0 | 0 | 0 | 11/11 |
| 132 | P4_2/mcm | 12 | 12 | 11 | 10 | 10 | 11 | 7 | 0 | 0 | 2 | 2 | 0 | 10/12 |
| 133 | P4_2/nbc | 20 | 20 | 12 | 9 | 9 | 12 | 4 | 0 | 0 | 11 | 0 | 11 | 9/20 |
| 134 | P4_2/nnm | 31 | 31 | 27 | 22 | 20 | 25 | 9 | 2 | 2 | 11 | 0 | 11 | 20/31 |
| 135 | P4_2/mbc | 16 | 16 | 11 | 10 | 10 | 11 | 6 | 0 | 0 | 6 | 6 | 0 | 10/16 |
| 136 | P4_2/mnm | 19 | 19 | 19 | 15 | 14 | 18 | 8 | 1 | 1 | 5 | 5 | 0 | 14/19 |
| 137 | P4_2/nmc | 16 | 16 | 19 | 16 | 13 | 16 | 6 | 3 | 3 | 3 | 1 | 2 | 13/16 |
| 138 | P4_2/ncm | 19 | 19 | 22 | 19 | 9 | 12 | 5 | 10 | 10 | 10 | 0 | 10 | 9/19 |
| 139 | I4/mmm | 14 | 14 | 18 | 15 | 14 | 17 | 9 | 1 | 1 | 0 | 0 | 0 | 14/14 |
| 140 | I4/mcm | 11 | 11 | 12 | 11 | 10 | 11 | 6 | 1 | 1 | 1 | 1 | 0 | 10/11 |
| 141 | I4_1/amd | 65 | 65 | 65 | 44 | 37 | 57 | 17 | 7 | 8 | 28 | 0 | 28 | 37/65 |
| 142 | I4_1/acd | 52 | 52 | 33 | 14 | 13 | 32 | 5 | 1 | 1 | 39 | 3 | 36 | 13/52 |

## The seven cubic finalists and the two named cells: cross-system f-vector scan

Own-group absence is the paper's stated criterion (draft_v3, Sec. 1). Cross-group and cross-system appearances are listed so that no reader is surprised; a same-f-vector row in another group or system is exactly the situation the collision screens exist for, and it says nothing about type identity until the exact code is compared.

| type | name | IT | f | own-group table | other cubic groups printing f | tetragonal rows printing f (IT, c/a, point, PDF p.) | his tetragonal cell stored? | type-level status |
|---|---|---|---|---|---|---|---|---|
| `8cf50403cf88c455` | Satchelhedron | 220 | (16,25,11) | ABSENT | none | IT134 b=4/5 (43/125,-1/10,11/50) p.78; IT141 b=797/1000 (62/125,62/125,0) p.84 | IT134: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT141: NOT stored (origin-shift group; only the read-only origin check reproduced the row) | unchecked at type level |
| `2de0a21129cabe90` | Ordenhedron | 201 | (20,33,15) | ABSENT | 197, 206, 208, 210, 212, 214, 218, 220, 230 | IT91 b=14/25 (271/500,49/500,1/8) p.44; IT95 b=14/25 (271/500,49/500,1/8) p.44; IT98 b=2 (3/10,6/25,27/1000) p.52; IT122 b=2 (3/10,6/25,123/1000) p.70; IT142 b=2 (13/250,9/250,9/500) p.86 | IT91: 21e0b5a7ebe148d6; IT95: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT98: 802c7ba284e53e8d; IT122: 3282abd05218d9c6; IT142: NOT stored (origin-shift group; only the read-only origin check reproduced the row) | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `c4ea3f32fdd6dc51` | Pn3m_11facet | 224 | (14,23,11) | ABSENT | 197, 208, 212, 217, 218, 222, 230 | IT79 b=1/2 (2825/5652,-1/5652,0) p.34; IT82 b=3497/1000 (249/500,-1/500,0) p.36; IT85 b=3497/1000 (62/125,0,1/4) p.39; IT86 b=3497/1000 (62/125,0,1/4) p.39; IT87 b=3497/1000 (249/500,-1/500,0) p.41; IT89 b=3497/1000 (249/500,-1/500,1/4) p.43; IT94 b=3497/1000 (249/500,-1/500,1/4) p.49; IT97 b=3497/1000 (249/500,-1/500,1/4) p.50; IT98 b=38/25 (885/2518,885/2518,1/8) p.51; IT103 b=1/2 (2825/5652,-1/5652,0) p.56; IT106 b=1/2 (353/1413,-353/1413,0) p.58; IT108 b=1/2 (2825/5652,-1/5652,0) p.59; IT112 b=3497/1000 (249/500,-1/500,0) p.61; IT114 b=3497/1000 (31/125,-31/125,1/4) p.62; IT116 b=3497/1000 (249/500,-1/500,0) p.64; IT117 b=3497/1000 (31/125,-31/125,1/4) p.65; IT120 b=3497/1000 (249/500,-1/500,0) p.68; IT121 b=3497/1000 (31/125,-31/125,1/4) p.69; IT124 b=3497/1000 (249/500,-1/500,0) p.72; IT125 b=3497/1000 (249/500,-1/500,1/4) p.73; IT126 b=3497/1000 (62/125,0,31/125) p.73; IT130 b=3497/1000 (249/500,-1/500,1/4) p.76; IT133 b=3497/1000 (249/500,-1/500,31/125) p.78; IT135 b=3497/1000 (31/125,-31/125,0) p.79; IT140 b=3497/1000 (249/500,-1/500,0) p.83 | IT79: 7824c3404ec7c532; IT82: 7824c3404ec7c532; IT85: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT86: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT87: 7824c3404ec7c532; IT89: 7824c3404ec7c532; IT94: 7824c3404ec7c532; IT97: 7824c3404ec7c532; IT98: 9cdad5392bcaebf9; IT103: 7824c3404ec7c532; IT106: 7824c3404ec7c532; IT108: 7824c3404ec7c532; IT112: 7824c3404ec7c532; IT114: 7824c3404ec7c532; IT116: 7824c3404ec7c532; IT117: 7824c3404ec7c532; IT120: 7824c3404ec7c532; IT121: 7824c3404ec7c532; IT124: 7824c3404ec7c532; IT125: 7824c3404ec7c532; IT126: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT130: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT133: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT135: 7824c3404ec7c532; IT140: 7824c3404ec7c532 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `f98a3ee5675fc121` | Pn3m_7facet | 224 | (10,15,7) | ABSENT | 203, 204, 210, 211, 217, 222, 223, 227, 229 | IT75 b=1/2 (2825/5652,-1/5652,0) p.33; IT81 b=3497/1000 (249/500,-1/500,0) p.36; IT83 b=3497/1000 (249/500,-1/500,0) p.37; IT84 b=3497/1000 (107/250,0,107/500) p.38; IT85 b=3497/1000 (62/125,0,0) p.39; IT87 b=3497/1000 (247/500,-1/500,1/4) p.40; IT88 b=3497/1000 (1/2,0,21/250) p.41; IT90 b=3497/1000 (31/125,-31/125,0) p.43; IT91 b=3497/1000 (3/4,1/4,31/250) p.44; IT95 b=3497/1000 (3/4,1/4,31/250) p.44; IT93 b=3497/1000 (107/250,0,107/500) p.48; IT94 b=3497/1000 (31/125,-31/125,1/4) p.49; IT97 b=3497/1000 (59/125,0,31/125) p.50; IT98 b=38/25 (1/2,315/1259,1257/10072) p.51; IT100 b=1/2 (2825/5652,-1/5652,0) p.54; IT104 b=1/2 (2825/5652,-1/5652,0) p.56; IT106 b=1/2 (2825/5652,-1/5652,0) p.57; IT107 b=1/2 (2471/5652,-1/5652,0) p.58; IT112 b=3497/1000 (62/125,0,31/125) p.61; IT113 b=3497/1000 (249/500,-1/500,0) p.62; IT114 b=3497/1000 (249/500,-1/500,0) p.62; IT117 b=3497/1000 (249/500,-1/500,0) p.65; IT118 b=3497/1000 (249/500,-1/500,0) p.65; IT119 b=3497/1000 (249/500,-1/500,1/25) p.67; IT121 b=3497/1000 (59/125,0,31/125) p.68; IT122 b=3497/1000 (1/2,1/2,21/250) p.69; IT126 b=3497/1000 (1/4,-111/500,1/500) p.73; IT127 b=3497/1000 (249/500,-1/500,0) p.74; IT128 b=3497/1000 (249/500,-1/500,0) p.74; IT129 b=3497/1000 (56/125,0,1/500) p.75; IT131 b=3497/1000 (107/250,0,107/500) p.76; IT132 b=3497/1000 (249/500,-1/500,31/125) p.77; IT134 b=3497/1000 (1/4,-123/500,1/500) p.78; IT135 b=3497/1000 (249/500,-1/500,0) p.79; IT136 b=3497/1000 (249/500,-1/500,31/125) p.80; IT137 b=3497/1000 (71/250,-27/125,17/500) p.81; IT138 b=3497/1000 (12/25,-1/50,23/100) p.81; IT139 b=3497/1000 (59/125,0,31/125) p.82; IT141 b=3497/1000 (1/2,0,21/250) p.83 | IT75: 52392121966e66eb; IT81: 52392121966e66eb; IT83: 52392121966e66eb; IT84: 52392121966e66eb; IT85: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT87: 52392121966e66eb; IT88: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT90: 52392121966e66eb; IT91: 52392121966e66eb; IT95: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT93: 52392121966e66eb; IT94: 52392121966e66eb; IT97: e3b3aae804f2c179; IT98: 52392121966e66eb; IT100: 52392121966e66eb; IT104: 52392121966e66eb; IT106: 52392121966e66eb; IT107: ca9a19039647d676; IT112: 52392121966e66eb; IT113: 52392121966e66eb; IT114: 52392121966e66eb; IT117: 52392121966e66eb; IT118: 52392121966e66eb; IT119: ca9a19039647d676; IT121: e3b3aae804f2c179; IT122: 52392121966e66eb; IT126: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT127: 52392121966e66eb; IT128: 52392121966e66eb; IT129: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT131: 52392121966e66eb; IT132: 52392121966e66eb; IT134: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT135: 52392121966e66eb; IT136: 52392121966e66eb; IT137: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT138: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT139: e3b3aae804f2c179; IT141: NOT stored (origin-shift group; only the read-only origin check reproduced the row) | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `ceb70631e274e727` | IT212_37-57-22_HELD | 212 | (37,57,22) | present | 199, 212, 214, 230 | IT91 b=4/5 (47/111,-17/333,23/999) p.45; IT95 b=4/5 (47/111,-17/333,23/999) p.45; IT92 b=4/5 (107/250,-3/250,3/25) p.47; IT96 b=4/5 (107/250,-3/250,3/25) p.47; IT98 b=38/25 (508/1259,405/1259,317/5036) p.53; IT118 b=7/2 (38/125,-1/250,119/500) p.66; IT122 b=5/4 (1247/2518,1067/2518,209/10072) p.71 | IT91: 90bbc790e01da31f; IT95: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT92: febc43bf173bf396; IT96: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT98: f9003106afcdc4f7; IT118: 84bbeabc892ed227; IT122: da36eed0a2de2eee | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `359beee832567a71` | IT230_40-61-23_HELD | 230 | (40,61,23) | present | 206, 212, 214, 220, 230 | IT98 b=821/1000 (1/2,63/250,123/1000) p.53; IT122 b=821/1000 (1/2,63/250,123/1000) p.71; IT141 b=1/2 (1/2,629/1259,1/5036) p.85 | IT98: 33aa9b759d545f78; IT122: 33aa9b759d545f78; IT141: fe3a62d422ed4d82 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `aa6b0077c3234d24` | IT214_30-47-19_HELD | 214 | (30,47,19) | present | 199, 206, 212, 214, 230 | IT80 b=4/5 (79/628,59/628,0) p.35; IT91 b=44/25 (7/25,-4/25,1/20) p.45; IT95 b=44/25 (7/25,-4/25,1/20) p.45; IT92 b=1/2 (59/125,0,99/1000) p.47; IT96 b=1/2 (59/125,0,99/1000) p.47; IT98 b=7/2 (109/250,87/250,109/1000) p.52; IT122 b=1157/1000 (1/2,62/125,1/500) p.70; IT141 b=1157/1000 (1/2,62/125,1/500) p.84 | IT80: 2d64348ab19ff182; IT91: de323953135731ae; IT95: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT92: 0191a4793071cbb8; IT96: NOT stored (origin-shift group; only the read-only origin check reproduced the row); IT98: 5eec09cbb0769b16; IT122: b9d2f3e02e91b42b; IT141: b9d2f3e02e91b42b | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |

**Finding (new, from this reconciliation).** The Satchelhedron's f-vector (16,25,11) is absent from every printed CUBIC table (as banked in G5_DILIGENCE and CROSS_GROUP_RESULTS, which say 'cubic'), but it IS printed in two TETRAGONAL tables: IT(134) at c/a = 4/5, point (43/125,-1/10,11/50) (PDF p. 78); IT(141) at c/a = 797/1000, point (62/125,62/125,0) (PDF p. 84). Both are two-origin groups; their printed rows were reproduced at f-vector level only by the read-only origin check (PHASE2_SCHMITT_ORIGIN_CHECK) and their cells are NOT in the store, so the exact canonical code at those two points has never been compared with the Satchelhedron's. STATUS.md 2026-09-01 shortens this to 'absent from the whole printed survey'; that shorthand should read 'cubic survey'. The paper's criterion (own-group absence) is unaffected. A type-level check at these two points (origin-choice-2 shift, exact chain, canonical code) is cheap and is the obvious next diligence step before any public wording about the Satchelhedron.

**Follow-up run (`catalog/check_satchelhedron_tetragonal_rows.py`, accepted phase-2 chain, all documented shifts; main-session re-run required for acceptance):** **Verdict: both printed (16,25,11) cells reproduce their printed f-vector under every documented shift and are DIFFERENT combinatorial types from the Satchelhedron** (and, per the last column, whether either is any stored type). This is not a novelty claim: his tables print one representative per (group, f-vector) from a grid sampling; the Satchelhedron remains 'not matched against the records checked as of 2026-09-04'. New micro-fact of the Josehedron/Schmitt-220 class: f = (16,25,11) is realised by at least 3 distinct combinatorial types across the survey (the Satchelhedron plus one per printed row; codes pairwise distinct).

## Limits

- f-vector level only. Type-level facts live in the catalog's `schmitt_type_level_*` columns (accepted screens: 21 + 55 cubic pairs, 27 tetragonal pairs, and the P2 reproductions).
- The cubic digitization is single-pass for 30 of 36 groups (the six finalist-hosting tables are re-keyed); the tetragonal digitization is single-pass throughout (text-layer cross-checked).
- Our tetragonal menu sampled 13 coarse c/a values plus 5 of his 56 printed ones; 51 printed c/a values were never swept, so (c) on the tetragonal side is dominated by metric under-sampling, not point under-sampling.
- Frequencies (printed in the cubic tables only) are not used here.


## v2 (2026-09-04): hexagonal family (IT 143-194)

Appended by `catalog/reconcile_schmitt.py` v2 from `catalog/catalog.json` v2 (1,583 types; snapshot 2026-09-04); deterministic. Everything above this heading is the v1 text (cubic + tetragonal), preserved verbatim; v2 recomputed both from the v2 catalog and asserted the four headline numbers of each equal (his pairs / (a) / (b) / (c)). Trigonal + hexagonal tables: `harness/schmitt_hexagonal_tables.json` (958 rows in 45 printed blocks, Sec. 2.2.3-2.2.4, PDF pp. 86-123; text layer primary, 153 rows visually cross-read, NOT independently re-keyed - G5 duty owed, agent #147 in progress). Every printed row passed Euler V-E+F=2 here. The wording rule of the v1 preamble binds every line below: an f-vector match is NOT type identity; absence is evidence, not proof; his survey is a grid sampling; (c) is a coverage gap of OUR sweep.

### Definitions specific to this family

- **Shared tables**: seven enantiomorphic pairs print ONE table each (144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181); both members get the printed set here, our sightings are per group. For 180/181 Schmitt's normalizer remark ('only the normalizer for IT(181) but not for IT(180)') means the printed points belong to IT(181): pass P2 reproduced all 69 rows in IT(181) verbatim (conversion H1) and 23 of them in IT(180); the other 46 reproduce in IT(180) only under z -> -z then H1, established by the read-only re-run `harness/phase2_hex_schmitt_180_check.py` with every one of the 46 cells already in the store. Those 46 rows are reported as a third (c) sub-split, **'(c) read-only, cell stored'**, never as coverage.
- **Our menu** (batch 2) = passes P1 (grid x 13 coarse c/a), P3 (5 printed b-ratios x grid: 3497/1000, 797/1000, 4/5, 527/1000, 7/8), P4 (1/24 line orbits), P5 (c/a bisection); pass P2 = his printed points (converted from his B'' basis by x' = 2x'', y' = x''+y'', z' = z''; second enantiomorphs verbatim then z -> -z).
- **b-ratio** = ||b3'||/||b1'|| = c/a in the ITA hexagonal basis; '(a) same c/a' counts matched (group, f) pairs where at least one of his printed b-ratios for that f equals one our menu sampled.

### Hexagonal family (52 groups; his rows 958)

Headline (sums over groups; a (group, f-vector) pair counts once per group):

- his distinct (group, f) pairs: **1276** (1276 (group, row) pairs from 958 printed rows; a shared table is counted once per group it serves)
- (a) ours-in-his: **510** (group, f) pairs, carrying **728** of our (type, group) sightings-by-menu; of these 278 pairs match at a c/a value we also sampled
- (b) ours-not-his: **40** (group, f) pairs, carrying **42** of our (type, group) menu sightings
- (c) his-not-ours: **766** (group, f) pairs = 766 printed rows our menu never reached in that group (coverage gap of our sweep); of these 733 have his cell stored via P2 at his own point, 33 are IT(180) rows reproduced read-only with the cell already stored, and 0 have no stored type at all
- whole-family distinct f-vectors: his 177, our menu 95, shared 94; ours not printed in ANY trigonal/hexagonal table: 1 ((20,36,18)); his f-vectors unreached by our menu anywhere in the family: 83 (even counting P2 and the read-only 180 rows: 0)
- across families: of his 177 trigonal/hexagonal f-vectors, 137 are also printed in a cubic table and 152 in a tetragonal table; 3 appear in this family only. Our 167 hexagonal-first f-vectors (84 from our menu): menu f-vectors printed in no table of any family: 1 ((20,36,18)); printed in no trigonal/hexagonal table: 1 ((20,36,18)).

Per group (full (group, f)-level table in `reconciliation_hexagonal.csv`):

| IT | symbol | his rows | his f | our types (menu) | our f (menu) | (a) f matched | (a) our types | (a) same c/a | (b) our f absent | (b) our types | (c) his f unreached | (c) stored via P2 | (c) read-only, cell stored | (c) not stored | coverage a/his |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 143 | P3 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1/2 |
| 144 | P3_1 | 9 | 9 | 9 | 4 | 4 | 9 | 2 | 0 | 0 | 5 | 5 | 0 | 0 | 4/9 |
| 145 | P3_2 | 9 | 9 | 9 | 4 | 4 | 9 | 2 | 0 | 0 | 5 | 5 | 0 | 0 | 4/9 |
| 146 | R3 | 19 | 19 | 12 | 9 | 9 | 12 | 4 | 0 | 0 | 10 | 10 | 0 | 0 | 9/19 |
| 147 | P-3 | 13 | 13 | 6 | 6 | 6 | 6 | 4 | 0 | 0 | 7 | 7 | 0 | 0 | 6/13 |
| 148 | R-3 | 63 | 63 | 25 | 16 | 15 | 24 | 7 | 1 | 1 | 48 | 48 | 0 | 0 | 15/63 |
| 149 | P312 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 4/5 |
| 150 | P321 | 13 | 13 | 9 | 8 | 8 | 9 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 8/13 |
| 151 | P3_112 | 29 | 29 | 14 | 10 | 10 | 14 | 6 | 0 | 0 | 19 | 19 | 0 | 0 | 10/29 |
| 152 | P3_121 | 64 | 64 | 28 | 18 | 14 | 24 | 5 | 4 | 4 | 50 | 50 | 0 | 0 | 14/64 |
| 153 | P3_212 | 29 | 29 | 16 | 11 | 11 | 16 | 4 | 0 | 0 | 18 | 18 | 0 | 0 | 11/29 |
| 154 | P3_221 | 64 | 64 | 32 | 20 | 16 | 28 | 5 | 4 | 4 | 48 | 48 | 0 | 0 | 16/64 |
| 155 | R32 | 89 | 89 | 33 | 25 | 23 | 31 | 9 | 2 | 2 | 66 | 66 | 0 | 0 | 23/89 |
| 156 | P3m1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 157 | P31m | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 158 | P3c1 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 3/4 |
| 159 | P31c | 9 | 9 | 6 | 5 | 5 | 6 | 3 | 0 | 0 | 4 | 4 | 0 | 0 | 5/9 |
| 160 | R3m | 17 | 17 | 12 | 11 | 11 | 12 | 7 | 0 | 0 | 6 | 6 | 0 | 0 | 11/17 |
| 161 | R3c | 17 | 17 | 14 | 9 | 9 | 14 | 4 | 0 | 0 | 8 | 8 | 0 | 0 | 9/17 |
| 162 | P-31m | 8 | 8 | 7 | 7 | 7 | 7 | 5 | 0 | 0 | 1 | 1 | 0 | 0 | 7/8 |
| 163 | P-31c | 22 | 22 | 14 | 13 | 13 | 14 | 8 | 0 | 0 | 9 | 9 | 0 | 0 | 13/22 |
| 164 | P-3m1 | 11 | 11 | 11 | 10 | 10 | 11 | 5 | 0 | 0 | 1 | 1 | 0 | 0 | 10/11 |
| 165 | P-3c1 | 23 | 23 | 9 | 9 | 9 | 9 | 5 | 0 | 0 | 14 | 14 | 0 | 0 | 9/23 |
| 166 | R-3m | 60 | 60 | 57 | 43 | 41 | 55 | 18 | 2 | 2 | 19 | 19 | 0 | 0 | 41/60 |
| 167 | R-3c | 84 | 84 | 27 | 20 | 17 | 24 | 7 | 3 | 3 | 67 | 67 | 0 | 0 | 17/84 |
| 168 | P6 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 4/4 |
| 169 | P6_1 | 16 | 16 | 21 | 6 | 6 | 21 | 3 | 0 | 0 | 10 | 10 | 0 | 0 | 6/16 |
| 170 | P6_5 | 16 | 16 | 21 | 6 | 6 | 21 | 3 | 0 | 0 | 10 | 10 | 0 | 0 | 6/16 |
| 171 | P6_2 | 34 | 34 | 14 | 9 | 9 | 14 | 5 | 0 | 0 | 25 | 25 | 0 | 0 | 9/34 |
| 172 | P6_4 | 34 | 34 | 14 | 9 | 9 | 14 | 5 | 0 | 0 | 25 | 25 | 0 | 0 | 9/34 |
| 173 | P6_3 | 8 | 8 | 4 | 4 | 4 | 4 | 3 | 0 | 0 | 4 | 4 | 0 | 0 | 4/8 |
| 174 | P-6 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2/2 |
| 175 | P6/m | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 4/4 |
| 176 | P6_3/m | 23 | 23 | 17 | 16 | 16 | 17 | 10 | 0 | 0 | 7 | 7 | 0 | 0 | 16/23 |
| 177 | P622 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 1 | 1 | 0 | 0 | 4/5 |
| 178 | P6_122 | 97 | 97 | 45 | 20 | 18 | 43 | 6 | 2 | 2 | 79 | 79 | 0 | 0 | 18/97 |
| 179 | P6_522 | 97 | 97 | 46 | 24 | 22 | 44 | 6 | 2 | 2 | 75 | 75 | 0 | 0 | 22/97 |
| 180 | P6_222 | 69 | 69 | 49 | 32 | 24 | 40 | 8 | 8 | 9 | 45 | 12 | 33 | 0 | 24/69 |
| 181 | P6_422 | 69 | 69 | 44 | 28 | 20 | 35 | 9 | 8 | 9 | 49 | 49 | 0 | 0 | 20/69 |
| 182 | P6_322 | 30 | 30 | 18 | 17 | 17 | 18 | 9 | 0 | 0 | 13 | 13 | 0 | 0 | 17/30 |
| 183 | P6mm | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 184 | P6cc | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 4/4 |
| 185 | P6_3cm | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7/7 |
| 186 | P6_3mc | 8 | 8 | 11 | 10 | 8 | 9 | 7 | 2 | 2 | 0 | 0 | 0 | 0 | 8/8 |
| 187 | P-6m2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 188 | P-6c2 | 8 | 8 | 6 | 6 | 6 | 6 | 5 | 0 | 0 | 2 | 2 | 0 | 0 | 6/8 |
| 189 | P-62m | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 190 | P-62c | 23 | 23 | 22 | 19 | 18 | 21 | 11 | 1 | 1 | 5 | 5 | 0 | 0 | 18/23 |
| 191 | P6/mmm | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3/3 |
| 192 | P6/mcc | 7 | 7 | 6 | 6 | 6 | 6 | 5 | 0 | 0 | 1 | 1 | 0 | 0 | 6/7 |
| 193 | P6_3/mcm | 14 | 14 | 12 | 12 | 12 | 12 | 9 | 0 | 0 | 2 | 2 | 0 | 0 | 12/14 |
| 194 | P6_3/mmc | 16 | 16 | 19 | 17 | 16 | 18 | 9 | 1 | 1 | 0 | 0 | 0 | 0 | 16/16 |

### The seven cubic finalists and the two named cells: trigonal/hexagonal f-vector scan

Same purpose as the v1 cross-system table (own-group absence is the paper's criterion; a same-f-vector row elsewhere says nothing about type identity until the exact code is compared). The type-level column is the v2 catalog's, which now also carries the hexagonal dedupe inference.

| type | name | IT | f | own-group table | trigonal/hexagonal rows printing f (IT, c/a, point as printed in B'', PDF p.) | his cell stored (P2)? | type-level status (v2) |
|---|---|---|---|---|---|---|---|
| `8cf50403cf88c455` | Satchelhedron | 220 | (16,25,11) | ABSENT | IT148 b=3497/1000 (-63/250,-61/250,1/1500) p.90; IT155 b=3497/1000 (-63/250,-61/250,1/1500) p.96; IT166 b=3497/1000 (-63/250,-61/250,1/1500) p.104; IT167 b=3497/1000 (-31/375,0,47/750) p.106; IT180 b=3497/1000 (62/125,61/125,31/375) p.115; IT181 b=3497/1000 (62/125,61/125,31/375) p.115 | IT148: 3f5fce0d11d8899e; IT155: 3f5fce0d11d8899e; IT166: 3f5fce0d11d8899e; IT167: 3f5fce0d11d8899e; IT180: 28f754a17236ade8; IT181: 28f754a17236ade8 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `2de0a21129cabe90` | Ordenhedron | 201 | (20,33,15) | ABSENT | IT148 b=4/5 (-97/375,-27/125,1/20) p.91; IT155 b=527/1000 (-203/750,-47/250,0) p.96; IT165 b=3497/1000 (307/1500,-97/500,1/125) p.103; IT166 b=527/1000 (-203/750,-47/250,0) p.105; IT167 b=3497/1000 (-64/375,-1/125,1/25) p.106; IT171 b=1/2 (1/54,0,0) p.109; IT172 b=1/2 (1/54,0,0) p.109; IT180 b=3497/1000 (62/125,0,11/375) p.115; IT181 b=3497/1000 (62/125,0,11/375) p.115; IT182 b=3497/1000 (17/100,-73/500,1/500) p.117 | IT148: 2185d1de22e99f29; IT155: 1a804bb88ddff3e2; IT165: 001cbd004f823a98; IT166: 1a804bb88ddff3e2; IT167: 001cbd004f823a98; IT171: 5ecea070beaf2efa; IT172: 5ecea070beaf2efa; IT180: NOT stored; IT181: 6e1c279805390881; IT182: 001cbd004f823a98 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `c4ea3f32fdd6dc51` | Pn3m_11facet | 224 | (14,23,11) | ABSENT | IT148 b=3497/1000 (-83/250,-1/250,0) p.90; IT155 b=3497/1000 (-83/250,-1/250,0) p.96; IT163 b=3497/1000 (33/100,-1/500,0) p.102; IT165 b=3497/1000 (33/100,-1/500,0) p.103; IT166 b=3497/1000 (-83/250,-1/250,0) p.104; IT167 b=3497/1000 (-1/375,0,1/12) p.106; IT177 b=3497/1000 (33/100,-1/500,1/4) p.112; IT180 b=1/2 (123/250,119/250,17/750) p.115; IT181 b=1/2 (123/250,119/250,17/750) p.115; IT184 b=3497/1000 (5647/16956,-1/5652,0) p.118; IT190 b=4/5 (29/125,-13/125,1/5) p.121; IT192 b=3497/1000 (33/100,-1/500,0) p.122 | IT148: 7f99db4f8ceb12b6; IT155: 7f99db4f8ceb12b6; IT163: 7824c3404ec7c532; IT165: 7824c3404ec7c532; IT166: 7f99db4f8ceb12b6; IT167: 7f99db4f8ceb12b6; IT177: 7824c3404ec7c532; IT180: 45cb5c5233427d61; IT181: 45cb5c5233427d61; IT184: 7824c3404ec7c532; IT190: 40dce96307e59597; IT192: 7824c3404ec7c532 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `f98a3ee5675fc121` | Pn3m_7facet | 224 | (10,15,7) | ABSENT | IT147 b=3497/1000 (33/100,-1/500,0) p.89; IT148 b=797/1000 (-51/250,-51/250,0) p.90; IT160 b=797/1000 (250/2997,749/2997,0) p.100; IT163 b=3497/1000 (499/1500,-1/500,13/500) p.102; IT164 b=3497/1000 (33/100,-1/500,3/250) p.102; IT166 b=3497/1000 (-163/750,-1/250,43/1500) p.104; IT167 b=797/1000 (-22/125,-22/125,0) p.105; IT168 b=3497/1000 (5647/16956,-1/5652,0) p.108; IT175 b=3497/1000 (33/100,-1/500,1/4) p.111; IT176 b=3497/1000 (33/100,-1/500,0) p.111; IT182 b=3497/1000 (499/1500,-1/500,13/500) p.117; IT186 b=797/1000 (5647/16956,-1/5652,0) p.119; IT190 b=3497/1000 (499/1500,-1/500,13/500) p.121; IT194 b=3497/1000 (499/1500,-1/500,13/500) p.123 | IT147: 52392121966e66eb; IT148: 5aa8e199fd7ddb2f; IT160: 5aa8e199fd7ddb2f; IT163: ca9a19039647d676; IT164: ca9a19039647d676; IT166: 5aa8e199fd7ddb2f; IT167: 5aa8e199fd7ddb2f; IT168: 52392121966e66eb; IT175: 52392121966e66eb; IT176: 52392121966e66eb; IT182: ca9a19039647d676; IT186: ca9a19039647d676; IT190: ca9a19039647d676; IT194: ca9a19039647d676 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `ceb70631e274e727` | IT212_37-57-22_HELD | 212 | (37,57,22) | present | IT152 b=136/125 (7/50,101/250,1/12) p.95; IT154 b=136/125 (7/50,101/250,1/12) p.95; IT167 b=769/500 (-68/375,-52/125,1/15) p.107; IT178 b=797/1000 (57/250,-3/250,2/25) p.114; IT179 b=797/1000 (57/250,-3/250,2/25) p.114; IT180 b=797/1000 (52/125,49/125,1/12) p.116; IT181 b=797/1000 (52/125,49/125,1/12) p.116 | IT152: f2ca3002be16e624; IT154: f2ca3002be16e624; IT167: a447ff728729e3b8; IT178: 1b1ac6860317aea8; IT179: 1b1ac6860317aea8; IT180: NOT stored; IT181: 8bd6a83d55f18ed6 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `359beee832567a71` | IT230_40-61-23_HELD | 230 | (40,61,23) | present | IT155 b=797/1000 (-53/750,-43/250,1/12) p.97; IT167 b=797/1000 (-127/750,-111/250,109/1500) p.107; IT178 b=977/1000 (4/125,-3/125,1/60) p.114; IT179 b=977/1000 (4/125,-3/125,1/60) p.114 | IT155: aa98eb9bdc2a5fc1; IT167: 24ec08378bbbe887; IT178: e4ff2fde16abc8a8; IT179: e4ff2fde16abc8a8 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| `aa6b0077c3234d24` | IT214_30-47-19_HELD | 214 | (30,47,19) | present | IT152 b=797/1000 (57/250,119/250,0) p.95; IT154 b=797/1000 (57/250,119/250,0) p.95; IT155 b=3497/1000 (-39/125,-3/125,1/300) p.97; IT167 b=3497/1000 (-1/150,-1/250,61/750) p.107; IT178 b=4/5 (36/125,-16/125,3/500) p.113; IT179 b=4/5 (36/125,-16/125,3/500) p.113; IT182 b=3497/1000 (33/100,-1/500,13/500) p.117 | IT152: 71735d01128c3326; IT154: 71735d01128c3326; IT155: 1691bbed1350a06b; IT167: 7c11e29fe6def4a8; IT178: 0105f5c3d7eb0b30; IT179: 0105f5c3d7eb0b30; IT182: 5aed4eedad8d6cf6 | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |

### The top-10 hexagonal-family collision-screen survivors (all G4-certified 2026-09-04)

Rank = survivor rank among the 151 (triage_phase2_hex_shortlist.json survivors_ranked = the # column of G4_PHASE2_HEX_RESULTS.md); all ten were re-confirmed DIFFERENT by exact recomputation at every printed row of their (group, f) (COLLISION_PHASE2_HEX_RESULTS.md, 26 pairs). Own-group table = whether his table for the first-witness group prints the f-vector at all. No name is proposed for any of them.

| rank | type | IT | c/a | f | aut | own-group table | other trigonal/hexagonal groups printing f | cubic groups printing f | tetragonal groups printing f | G4 | solid chiral | type-level status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 P6_122 | 5/4 | (44,66,24) | 2 | present | 152, 154, 169, 170, 179, 180, 181 | none | 76, 78, 80, 91, 92, 95, 96, 98, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 2 | `59585d778cb3a7a4` | 178 P6_122 | 3/4 | (40,60,22) | 2 | present | 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | none | 76, 78, 80, 82, 88, 91, 92, 93, 94, 95, 96, 98, 110, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 3 | `095ce61d28388c98` | 178 P6_122 | 1 | (40,60,22) | 2 | present | 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | none | 76, 78, 80, 82, 88, 91, 92, 93, 94, 95, 96, 98, 110, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 4 | `9be0f2271a14b6a9` | 178 P6_122 | 1 | (36,54,20) | 4 | present | 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | 199, 230 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 5 | `2d654c836f3731c6` | 178 P6_122 | 1 | (36,54,20) | 2 | present | 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | 199, 230 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 6 | `b0f80776885f3ae1` | 178 P6_122 | 1/2 | (36,54,20) | 2 | present | 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | 199, 230 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 7 | `a348875c3f707895` | 178 P6_122 | 1/2 | (36,54,20) | 2 | present | 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | 199, 230 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 8 | `dcc38ea9177089b9` | 178 P6_122 | 1/2 | (36,54,20) | 2 | present | 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 179, 180, 181 | 199, 230 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 9 | `5b86a254c715306c` | 169 P6_1 | 797/1000 | (40,60,22) | 1 | present | 151, 152, 153, 154, 170, 171, 172, 178, 179, 180, 181 | none | 76, 78, 80, 82, 88, 91, 92, 93, 94, 95, 96, 98, 110, 118, 122, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |
| 10 | `f05f0b009e0929f6` | 169 P6_1 | 3/4 | (32,48,18) | 2 | present | 144, 145, 151, 152, 153, 154, 170, 171, 172, 178, 179, 180, 181 | 198, 212 | 76, 78, 80, 82, 86, 88, 91, 92, 93, 94, 95, 96, 98, 109, 110, 114, 116, 118, 120, 122, 133, 141, 142 | certified-hexagonal | True | DIFFERENT from every checked printed representative (not identity evidence; sampling caveat) |

### Limits (v2)

- f-vector level only; type-level facts live in the catalog's `schmitt_type_level_*` and `schmitt_match_hexagonal` columns (store-side screen of all 288 menu-sighted hexagonal-first types: 151 SURVIVOR / 124 COLLISION / 13 UNRESOLVED; the 13 are unresolved only at IT(180) rows, and the read-only re-run finds all 13 DIFFERENT there - recorded, store verdict stands).
- The trigonal/hexagonal digitization is single-pass (text layer + 153-row visual cross-read), not an independent re-key; every row was, however, run through the exact chain by pass P2 (1,230 verbatim + 46 read-only = 1,276/1,276 reproduce their printed f-vector).
- Our batch-2 menu sampled 13 coarse c/a values plus 5 of his 38 printed b-ratios (9 of 38 reached in total); (c) on this side is dominated by metric under-sampling, as in the tetragonal batch.
- The 43 prior (cubic-/tetragonal-first) types re-sighted in this family were NOT collision-screened here; their hexagonal status is f-vector level only.
- No frequency column is printed in these tables.


## v3 (2026-09-04): computed open/wall verdicts x type-level Schmitt status

Appended by `catalog/reconcile_schmitt.py` v3 from `catalog/catalog.json` v3 (1,583 types; snapshot 2026-09-04); deterministic. Everything above this heading is the v1 text + the v2 section, preserved byte for byte (asserted: the v1 and v2 sections regenerated from the v3 catalog equal the preserved text); v2 of this script = `git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py`. Sources of the two v3 columns cross-tabulated here: `harness/phase2/WALL_OPEN_PHASE2.json` (computed open/wall verdicts of the 165 G4-certified phase-2 cells at their stored first witness; scheme pre-registered in ANCHORS.md 'PERTURBATION CLASSIFICATION, PHASE 2' on 2026-09-04 BEFORE the run; agent #148; accepted by the main session's fresh re-run 2026-09-04 14:10, JSON md5 6b257c551f6fb275dfabb03e992f57c2), `harness/round1_computations/c1_wall_open.json` (the 7 cubic finalists, c1 round of 2026-09-03), `harness/COLLISION_PHASE2_RESULTS.md` (tetragonal top-15 shortlist, 27 printed pairs) and `harness/COLLISION_PHASE2_HEX_RESULTS.md` (store-side screen of the 288 menu-sighted hexagonal-first types; top-10 recomputed at the printed points). Wording, stated once: OPEN = the type holds on the tested neighbourhood of its first witness at finite steps (point 1/1536, metric 1/3072 relative), never an interval proof; WALL = the witness sits on a transition (both sides of some direction change); ONE-SIDED = some side changes but no direction on both sides (a short neighbourhood, not a wall); SURVIVOR = not matched at the printed representatives checked (records checked as of 2026-09-04), never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe); printed-only = an S-cell never reached by our menu; not-screened = outside both phase-2 screens (all cubic-first types by construction; 389 menu-sighted tetragonal-first types outside the top-15). A wall cell is excluded from the naming pool because its witness sits on a transition; nothing here proposes a name.

### Cross-tab per family: open_wall_verdict (rows) x schmitt_type_status (columns)

**cubic-first** (102 types; verdicts OPEN 6, WALL 1, ONE-SIDED 0, not-computed 95; statuses SURVIVOR 0, COLLISION 0, UNRESOLVED 0, printed-only 0, not-screened 102):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 0 | 0 | 0 | 0 | 6 | 6 |
| WALL | 0 | 0 | 0 | 0 | 1 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 0 | 0 | 0 | 0 | 95 | 95 |
| total | 0 | 0 | 0 | 0 | 102 | 102 |

**tetragonal-first** (789 types; verdicts OPEN 13, WALL 1, ONE-SIDED 0, not-computed 775; statuses SURVIVOR 14, COLLISION 1, UNRESOLVED 0, printed-only 385, not-screened 389):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 13 | 0 | 0 | 0 | 0 | 13 |
| WALL | 1 | 0 | 0 | 0 | 0 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 0 | 1 | 0 | 385 | 389 | 775 |
| total | 14 | 1 | 0 | 385 | 389 | 789 |

**hexagonal-first** (692 types; verdicts OPEN 102, WALL 40, ONE-SIDED 9, not-computed 541; statuses SURVIVOR 151, COLLISION 124, UNRESOLVED 13, printed-only 404, not-screened 0):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 102 | 0 | 0 | 0 | 0 | 102 |
| WALL | 40 | 0 | 0 | 0 | 0 | 40 |
| ONE-SIDED | 9 | 0 | 0 | 0 | 0 | 9 |
| not-computed | 0 | 124 | 13 | 404 | 0 | 541 |
| total | 151 | 124 | 13 | 404 | 0 | 692 |

### Naming pool = G4-certified AND open_wall_verdict OPEN AND unnamed, per family

- cubic: **0** of 12 accepted-cubic types: the 6 OPEN cells (c1) all carry a name or a marker already (`ceb70631e274e727` IT212_37-57-22_HELD [HELD]; `aa6b0077c3234d24` IT214_30-47-19_HELD [HELD]; `2de0a21129cabe90` Ordenhedron [named]; `c4ea3f32fdd6dc51` Pn3m_11facet [descriptive package name]; `f98a3ee5675fc121` Pn3m_7facet [descriptive package name]; `359beee832567a71` IT230_40-61-23_HELD [HELD]); the Satchelhedron is the cubic WALL cell; 5 accepted-cubic types have no perturbation run on record (`8c69db9e84095469`, `c314dedd38208a2e`, `f3d0f39a0b9676b9`, `d2d935e5499e6e11`, `9b69eefb8bd8437c`).
- tetragonal: **13** of 14 certified (13 OPEN, 1 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-T004 = `164d4bd63d82d0c3`, MINT-T005 = `6797ab70c6015039`, MINT-T076 = `1497877268495988`, MINT-T137 = `7575121042ade3b3`, MINT-T151 = `3ebbca7ed2eda199`, MINT-T152 = `4f6d3e68cbd9e729`, MINT-T264 = `f654982d74d740f6`, MINT-T716 = `086ac96faf390886`, MINT-T721 = `4e9c9b076cfec323`, MINT-T722 = `e0d18e5ea938d649`, MINT-T758 = `2e8e49eb28497267`, MINT-T766 = `5dc2479b9bc14edc`, MINT-T767 = `213c7a114d5a97a8`.
- hexagonal: **102** of 151 certified (102 OPEN, 49 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-H002 = `bff9b24ce78050f5`, MINT-H003 = `c0071756347c5a8a`, MINT-H007 = `7b9cfe26fe4a9c4b`, MINT-H021 = `f0b07b168368759b`, MINT-H024 = `f429e996b3f455a6`, MINT-H025 = `56918d2cff883e22`, MINT-H034 = `ce3b42c8a4ceff6f`, MINT-H035 = `36ec4ad2f530e145`, MINT-H041 = `e98412e7cb95aea2`, MINT-H045 = `847d2695a14ae424`, MINT-H047 = `5838282f46223111`, MINT-H050 = `72bcd959be4ab7dd`, MINT-H051 = `e198aac88f223892`, MINT-H052 = `23594bd7053503aa`, MINT-H055 = `b2430fc4bea4e06d`, MINT-H058 = `542cbe76934b484b`, MINT-H059 = `3d6b109f392fda19`, MINT-H063 = `2c121297dbaa80af`, MINT-H065 = `64203f15fcf6c09b`, MINT-H070 = `a46cbaad3c23e834`, MINT-H072 = `c3b4b14633c9d4d5`, MINT-H073 = `d9bf7fb7a80eaa38`, MINT-H095 = `9d4396ca0b08fc3c`, MINT-H105 = `ab801b11bead62ef`, MINT-H112 = `36c92427e3d084dc`, MINT-H120 = `057255f61286b052`, MINT-H121 = `6de3dac5f334cfed`, MINT-H126 = `85244add8d1f2d55`, MINT-H127 = `f05f0b009e0929f6`, MINT-H128 = `16025e0680843c36`, MINT-H129 = `a35623e347ef03b4`, MINT-H131 = `9c0b7e0c29dfebb2`, MINT-H133 = `2b9726574a0a8bed`, MINT-H135 = `3ddc41389e6d484f`, MINT-H136 = `29bbba1adec778da`, MINT-H137 = `cff2d5fb5e0d4149`, MINT-H141 = `a348875c3f707895`, MINT-H142 = `2d654c836f3731c6`, MINT-H145 = `b0f80776885f3ae1`, MINT-H146 = `59585d778cb3a7a4`, MINT-H147 = `095ce61d28388c98`, MINT-H148 = `c49077384aaebeb0`, MINT-H150 = `9be0f2271a14b6a9`, MINT-H153 = `dcc38ea9177089b9`, MINT-H157 = `34351050a4f29035`, MINT-H158 = `24a6b511067d37b2`, MINT-H159 = `042c19cbfdc869cb`, MINT-H160 = `7a448bed1119dfad`, MINT-H161 = `f6f8b3050a1eef42`, MINT-H162 = `d718e083bd23d2b1`, MINT-H163 = `8cc8c5ab3cf36d8f`, MINT-H165 = `d176b8d859dd651a`, MINT-H166 = `30f2a1e483babf55`, MINT-H167 = `437fbe758a6dd8e3`, MINT-H168 = `0948aa6184f13a8a`, MINT-H169 = `a182e87006c7a00d`, MINT-H176 = `e19babba732f5fd4`, MINT-H177 = `dd3fb07fe11d73d3`, MINT-H194 = `257b627a90b78038`, MINT-H201 = `e0bf1a48f096c10d`, MINT-H203 = `f14a8c4e7c5b3e3a`, MINT-H207 = `7715c7010e513b71`, MINT-H208 = `505a4911e298c933`, MINT-H635 = `cda1d1c03659b67d`, MINT-H636 = `2165f5c5260120de`, MINT-H637 = `d10bb4a25bbf4c80`, MINT-H638 = `c82ebc15c49c1413`, MINT-H639 = `4a560e459032166a`, MINT-H640 = `87c94384d7851cb2`, MINT-H641 = `466b12546dd936c3`, MINT-H642 = `c53bc05bc306c97d`, MINT-H643 = `74a69fba4266de3b`, MINT-H645 = `5b86a254c715306c`, MINT-H646 = `ac4489d658eb445e`, MINT-H648 = `af8b2135c913b13b`, MINT-H650 = `e598ffd8a1cac138`, MINT-H651 = `a93f8fe7ecdc5851`, MINT-H652 = `75bbbcb4a37e70e8`, MINT-H653 = `3a491fd6426d90b2`, MINT-H654 = `fac4317d5a65b959`, MINT-H655 = `5f812747976b224a`, MINT-H660 = `d0c5a15c25ab6413`, MINT-H661 = `07d543d89e2934f2`, MINT-H663 = `d770abfcee4deb90`, MINT-H664 = `cbead3df2d2f1d0e`, MINT-H665 = `fcffad0da2b5b62f`, MINT-H667 = `59b28b3a59c27092`, MINT-H668 = `37aa18e6e10583be`, MINT-H670 = `2081d7b9a734e4fe`, MINT-H671 = `27dbb77012555d28`, MINT-H672 = `e1a38303b2378f17`, MINT-H673 = `6f4101f83371033d`, MINT-H674 = `d9ac68100a276dfe`, MINT-H675 = `646b518ccf3bd724`, MINT-H676 = `322d5ff451e4101d`, MINT-H678 = `8d90c524c89922d9`, MINT-H679 = `d07f950b8309de82`, MINT-H680 = `27d463eac6cda5ea`, MINT-H681 = `aef8972953d53d20`, MINT-H683 = `7e05ce00d8a7cbf6`, MINT-H687 = `0b5d9beb0fc972f6`, MINT-H692 = `43e4e46001b4d8b9`.
- Pool check: 13 tetragonal + 102 hexagonal-family = 115, equal to PROGRAM_LEDGER 2026-09-04 14:10 ('13 tetragonal + 102 hexagonal'); asserted in build_catalog.py and recounted from the raw verdict / screen / certificate files by verify_counts_independent.py v3. Pool membership is catalog-relative; G5 diligence (print-only Engel / Koch exposure) still applies before any name.

### Certified phase-2 cells outside the pool (WALL / ONE-SIDED), with the naming-relevant facts

Wall directions, the neighbouring types on each side and their Schmitt status are in `WALL_OPEN_PHASE2.md` section 'Wall cells (41) and their neighbouring types'; flags are never verdict inputs (line_isolated = stratum dim 1 and the single point direction is WALL; nonsimple_vertex = non-simple vertices at the witness; degenerate_flag_any = a float degeneracy flag on some perturbed cell, exact superseding).

| catalog id | type | family | IT | c/a | f | aut | COMBINED | POINT | METRIC | flags |
|---|---|---|---|---|---|---|---|---|---|---|
| MINT-T755 | `49cedbdd58376fac` | tetragonal | 92 P4_12_12 | 19/16 | (44,66,24) | 2 | **WALL** | WALL | OPEN | line_isolated |
| MINT-H008 | `78e755ffdff3a2f5` | hexagonal | 146 R3 | 3/4 | (14,24,12) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H018 | `105e41c2798e6180` | hexagonal | 148 R-3 | 2 | (16,27,13) | 6 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H023 | `c18a9b1cb2a5d168` | hexagonal | 148 R-3 | 1/2 | (26,40,16) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H028 | `1ba26ab2c0999b93` | hexagonal | 148 R-3 | 1/2 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H029 | `6074c5fa5d2dffc5` | hexagonal | 148 R-3 | 3/4 | (16,26,12) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H033 | `4db369a636f4396b` | hexagonal | 151 P3_112 | 3/2 | (18,30,14) | 4 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H049 | `0417061f8f56488e` | hexagonal | 152 P3_121 | 1/2 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H056 | `7e023be581e7c50a` | hexagonal | 154 P3_221 | 3/4 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |
| MINT-H057 | `66563d07a1110a25` | hexagonal | 154 P3_221 | 1 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |
| MINT-H061 | `d1f1121757598de0` | hexagonal | 154 P3_221 | 9/4 | (15,25,12) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H071 | `d70e6901953070e7` | hexagonal | 155 R32 | 3/4 | (38,58,22) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H074 | `67b1ede4b021a4fc` | hexagonal | 155 R32 | 3/2 | (17,29,14) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H076 | `d0ed9179c6947b5f` | hexagonal | 155 R32 | 1/2 | (16,26,12) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H079 | `b27ba8dbcbc2891a` | hexagonal | 161 R3c | 1/2 | (22,34,14) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H096 | `c95a5fcf4d681568` | hexagonal | 166 R-3m | 3/2 | (12,21,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H099 | `34e5e7acce18b5cd` | hexagonal | 166 R-3m | 3/2 | (14,23,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H101 | `090dcafb7ce9cb08` | hexagonal | 166 R-3m | 1/2 | (20,32,14) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H102 | `9bc4922a7b574aa6` | hexagonal | 166 R-3m | 3/4 | (17,28,13) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H111 | `f7bd7cd9eae6436b` | hexagonal | 166 R-3m | 1 | (16,27,13) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H122 | `4ff9d77aa9f8194a` | hexagonal | 167 R-3c | 3/4 | (24,37,15) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H123 | `400cba5c78326d1d` | hexagonal | 167 R-3c | 1 | (17,28,13) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H124 | `5e68ffe7582a0657` | hexagonal | 167 R-3c | 1/2 | (20,31,13) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H132 | `d7c638d7fa23127e` | hexagonal | 169 P6_1 | 3/2 | (25,39,16) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H143 | `7e79f1c38b5516bf` | hexagonal | 178 P6_122 | 3/2 | (22,34,14) | 2 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H144 | `161b09808f4c1863` | hexagonal | 178 P6_122 | 2 | (18,30,14) | 4 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H152 | `f07d69523ef41b37` | hexagonal | 178 P6_122 | 3/2 | (20,36,18) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H155 | `5beb94b61eb66eb1` | hexagonal | 178 P6_122 | 1/2 | (27,41,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H156 | `bc59e5d778f60d1f` | hexagonal | 178 P6_122 | 3/4 | (29,44,17) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H170 | `8463196a30c6643f` | hexagonal | 179 P6_522 | 2 | (23,36,15) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H172 | `95934e84555dc2ea` | hexagonal | 179 P6_522 | 1/2 | (26,40,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H173 | `4885ce1e70fa9713` | hexagonal | 179 P6_522 | 3/4 | (27,41,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H174 | `f5fbebffa76808d5` | hexagonal | 179 P6_522 | 5/4 | (31,47,18) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H175 | `c92eef8763d02d8a` | hexagonal | 179 P6_522 | 3/2 | (25,39,16) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H181 | `457c20cf036ae496` | hexagonal | 180 P6_222 | 3/2 | (11,20,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H191 | `fa9c370d30741970` | hexagonal | 180 P6_222 | 3/2 | (9,16,9) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H209 | `6cc34ed38aa354e1` | hexagonal | 181 P6_422 | 1/2 | (22,34,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H644 | `9d0b36ad5caceb2e` | hexagonal | 167 R-3c | 7/8 | (22,35,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H656 | `487490cdf474e568` | hexagonal | 148 R-3 | 1277/2000 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H657 | `f0e2036d295195b4` | hexagonal | 152 P3_121 | 9/8 | (12,20,10) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H658 | `7472d8ba000c8056` | hexagonal | 152 P3_121 | 9/8 | (22,36,16) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H659 | `75c9be976d704515` | hexagonal | 152 P3_121 | 9/8 | (18,28,12) | 2 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H662 | `5b679d8b0a3147c3` | hexagonal | 152 P3_121 | 17/16 | (24,38,16) | 1 | **WALL** | WALL | ONE-SIDED | degenerate_flag_any, nonsimple_vertex |
| MINT-H666 | `919d30fd9021b5ee` | hexagonal | 154 P3_221 | 51/32 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H669 | `f43b45fd6383b36b` | hexagonal | 155 R32 | 19/16 | (26,41,17) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H677 | `71d2c9953ca110b8` | hexagonal | 169 P6_1 | 39/32 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | - |
| MINT-H682 | `4b6055c7aa3d341b` | hexagonal | 178 P6_122 | 17/8 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H684 | `11a9fe078850b5cd` | hexagonal | 179 P6_522 | 65/32 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H685 | `272aefcd5e48ba49` | hexagonal | 179 P6_522 | 9/8 | (29,44,17) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H686 | `60eb4282db04fca2` | hexagonal | 179 P6_522 | 11/8 | (30,45,17) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |

### Limits (v3)

- Every verdict is for the stored FIRST witness of the type only (one point, one c/a); a type OPEN here may have other sightings on a wall, and a WALL witness does not preclude an open region of the same type elsewhere.
- Finite steps: point 1/48, 1/96 halved to 1/1536; metric c/a(1 +- 1/96, 1/192) halved to 1/3072 (relative, so coarser than 1/96 absolute for the five cells with c/a > 2, stated in WALL_OPEN_PHASE2.md); OPEN is 'holds on the tested neighbourhood', ONE-SIDED is a short neighbourhood, neither is an interval proof.
- The heuristic open-likely / wall-suspect / indeterminate labels disagreed with the computed verdict on 35 of the 165 cells in both directions (WALL_OPEN_PHASE2.md); the catalog carries the computed verdict and keeps the label only inside open_wall_verdict_pointer.
- The tetragonal collision screen covered the top-15 shortlist only (15 of 404 menu-sighted types, 27 printed pairs); 176 of the 389 not-screened menu-sighted tetragonal-first types are S-cells (type-level SAME by pass P2, recorded in schmitt_type_level_status) and would be COLLISION under the hexagonal screen's store-side rule, which was not run on the tetragonal family - a main-session decision, not made here.
- Cubic-first types are not-screened by the two phase-2 screens by construction; their cubic-round verdicts (SCHMITT_COLLISION_RESULTS.md, CROSS_GROUP_RESULTS.md) stay in schmitt_type_level_*.
- No new digitization, perturbation or certificate was computed here; the section only cross-tabulates accepted records. Snapshot wording throughout.


## v4 (2026-09-04): tetragonal store-side status folded in (both phase-2 families under one rule)

Appended by `catalog/reconcile_schmitt.py` v4 from `catalog/catalog.json` v4 (1,583 types; snapshot 2026-09-04); deterministic. Everything above this heading is the v1 text + the v2 section + the v3 section, preserved byte for byte (asserted for v1 + v2 by regeneration from the v4 catalog; the v3 section is the pre-rule record and is kept verbatim: its tetragonal column 'not-screened 389' is superseded below); v3 of this script = `git show e01618b:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py`. Sources of the two v3 columns cross-tabulated here: `harness/phase2/WALL_OPEN_PHASE2.json` (computed open/wall verdicts of the 165 G4-certified phase-2 cells at their stored first witness; scheme pre-registered in ANCHORS.md 'PERTURBATION CLASSIFICATION, PHASE 2' on 2026-09-04 BEFORE the run; agent #148; accepted by the main session's fresh re-run 2026-09-04 14:10, JSON md5 6b257c551f6fb275dfabb03e992f57c2), `harness/round1_computations/c1_wall_open.json` (the 7 cubic finalists, c1 round of 2026-09-03), `harness/COLLISION_PHASE2_RESULTS.md` (tetragonal top-15 shortlist, 27 printed pairs; ADDENDUM 2026-09-04 = the hexagonal screen's store-side rule applied to all 404 menu-sighted tetragonal types, `harness/collision_phase2_tetragonal_storeside.json`, hexagonal equivalence asserted 151/124/13) and `harness/COLLISION_PHASE2_HEX_RESULTS.md` (store-side screen of the 288 menu-sighted hexagonal-first types; top-10 recomputed at the printed points). Wording, stated once: OPEN = the type holds on the tested neighbourhood of its first witness at finite steps (point 1/1536, metric 1/3072 relative), never an interval proof; WALL = the witness sits on a transition (both sides of some direction change); ONE-SIDED = some side changes but no direction on both sides (a short neighbourhood, not a wall); SURVIVOR = not matched at the printed representatives checked (records checked as of 2026-09-04), never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe); printed-only = an S-cell never reached by our menu; not-screened = outside both phase-2 screens (all cubic-first types by construction; since v4 no tetragonal-first type). A wall cell is excluded from the naming pool because its witness sits on a transition; nothing here proposes a name.

### Cross-tab per family: open_wall_verdict (rows) x schmitt_type_status (columns)

**cubic-first** (102 types; verdicts OPEN 6, WALL 1, ONE-SIDED 0, not-computed 95; statuses SURVIVOR 0, COLLISION 0, UNRESOLVED 0, printed-only 0, not-screened 102):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 0 | 0 | 0 | 0 | 6 | 6 |
| WALL | 0 | 0 | 0 | 0 | 1 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 0 | 0 | 0 | 0 | 95 | 95 |
| total | 0 | 0 | 0 | 0 | 102 | 102 |

**tetragonal-first** (789 types; verdicts OPEN 13, WALL 1, ONE-SIDED 0, not-computed 775; statuses SURVIVOR 121, COLLISION 177, UNRESOLVED 106, printed-only 385, not-screened 0):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 13 | 0 | 0 | 0 | 0 | 13 |
| WALL | 1 | 0 | 0 | 0 | 0 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 107 | 177 | 106 | 385 | 0 | 775 |
| total | 121 | 177 | 106 | 385 | 0 | 789 |

**hexagonal-first** (692 types; verdicts OPEN 102, WALL 40, ONE-SIDED 9, not-computed 541; statuses SURVIVOR 151, COLLISION 124, UNRESOLVED 13, printed-only 404, not-screened 0):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 102 | 0 | 0 | 0 | 0 | 102 |
| WALL | 40 | 0 | 0 | 0 | 0 | 40 |
| ONE-SIDED | 9 | 0 | 0 | 0 | 0 | 9 |
| not-computed | 0 | 124 | 13 | 404 | 0 | 541 |
| total | 151 | 124 | 13 | 404 | 0 | 692 |

### Tetragonal type-level status, v3 -> v4 (the store-side rule applied to all 404 menu-sighted tetragonal-first types)

Source: v4: harness/collision_phase2_tetragonal_storeside.json (subagent #152, 2026-09-04; rule = COLLISION_PHASE2_HEX_RESULTS.md section 1 store-side rule re-implemented, hexagonal equivalence asserted 151/124/13; dated addendum in harness/COLLISION_PHASE2_RESULTS.md); JSON md5 64cc7bb82e85164914d7ec441cfc1304. Rule (stated once, identical to the hexagonal screen's): SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed row with that (group, f) reproduced (P2) as a different stored type; COLLISION = the type reproduces one of his printed cells (S-cell / SAME); UNRESOLVED = a printed row with that (group, f) was not stored, so no type-level statement is possible for that pair. Overlay: the 27 shortlist pairs recomputed in COLLISION_PHASE2_RESULTS.md resolve their rows (SAME -> COLLISION; DIFFERENT on an unstored row -> row resolved).

| count | SURVIVOR | COLLISION | UNRESOLVED |
|---|---|---|---|
| catalog v3 (top-15 recomputation only; not-screened = 389) | 14 | 1 | 0 |
| pure store-side rule | 116 | 176 | 112 |
| v4 = rule + recomputed pairs overlaid | 121 | 177 | 106 |

Transitions v3 -> v4 over the 404 menu-sighted tetragonal-first types: COLLISION -> COLLISION: 1; SURVIVOR -> SURVIVOR: 14; not-screened -> COLLISION: 176; not-screened -> SURVIVOR: 107; not-screened -> UNRESOLVED: 106. S-cells 176 (all COLLISION). Shortlist disagreements: 0. The 385 Schmitt-printed-only tetragonal types stay printed-only; the 102 cubic-first types stay not-screened (scope fact).

### Naming pool = G4-certified AND open_wall_verdict OPEN AND unnamed, per family

- cubic: **0** of 12 accepted-cubic types: the 6 OPEN cells (c1) all carry a name or a marker already (`ceb70631e274e727` IT212_37-57-22_HELD [HELD]; `aa6b0077c3234d24` IT214_30-47-19_HELD [HELD]; `2de0a21129cabe90` Ordenhedron [named]; `c4ea3f32fdd6dc51` Pn3m_11facet [descriptive package name]; `f98a3ee5675fc121` Pn3m_7facet [descriptive package name]; `359beee832567a71` IT230_40-61-23_HELD [HELD]); the Satchelhedron is the cubic WALL cell; 5 accepted-cubic types have no perturbation run on record (`8c69db9e84095469`, `c314dedd38208a2e`, `f3d0f39a0b9676b9`, `d2d935e5499e6e11`, `9b69eefb8bd8437c`).
- tetragonal: **13** of 14 certified (13 OPEN, 1 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-T004 = `164d4bd63d82d0c3`, MINT-T005 = `6797ab70c6015039`, MINT-T076 = `1497877268495988`, MINT-T137 = `7575121042ade3b3`, MINT-T151 = `3ebbca7ed2eda199`, MINT-T152 = `4f6d3e68cbd9e729`, MINT-T264 = `f654982d74d740f6`, MINT-T716 = `086ac96faf390886`, MINT-T721 = `4e9c9b076cfec323`, MINT-T722 = `e0d18e5ea938d649`, MINT-T758 = `2e8e49eb28497267`, MINT-T766 = `5dc2479b9bc14edc`, MINT-T767 = `213c7a114d5a97a8`.
- hexagonal: **102** of 151 certified (102 OPEN, 49 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-H002 = `bff9b24ce78050f5`, MINT-H003 = `c0071756347c5a8a`, MINT-H007 = `7b9cfe26fe4a9c4b`, MINT-H021 = `f0b07b168368759b`, MINT-H024 = `f429e996b3f455a6`, MINT-H025 = `56918d2cff883e22`, MINT-H034 = `ce3b42c8a4ceff6f`, MINT-H035 = `36ec4ad2f530e145`, MINT-H041 = `e98412e7cb95aea2`, MINT-H045 = `847d2695a14ae424`, MINT-H047 = `5838282f46223111`, MINT-H050 = `72bcd959be4ab7dd`, MINT-H051 = `e198aac88f223892`, MINT-H052 = `23594bd7053503aa`, MINT-H055 = `b2430fc4bea4e06d`, MINT-H058 = `542cbe76934b484b`, MINT-H059 = `3d6b109f392fda19`, MINT-H063 = `2c121297dbaa80af`, MINT-H065 = `64203f15fcf6c09b`, MINT-H070 = `a46cbaad3c23e834`, MINT-H072 = `c3b4b14633c9d4d5`, MINT-H073 = `d9bf7fb7a80eaa38`, MINT-H095 = `9d4396ca0b08fc3c`, MINT-H105 = `ab801b11bead62ef`, MINT-H112 = `36c92427e3d084dc`, MINT-H120 = `057255f61286b052`, MINT-H121 = `6de3dac5f334cfed`, MINT-H126 = `85244add8d1f2d55`, MINT-H127 = `f05f0b009e0929f6`, MINT-H128 = `16025e0680843c36`, MINT-H129 = `a35623e347ef03b4`, MINT-H131 = `9c0b7e0c29dfebb2`, MINT-H133 = `2b9726574a0a8bed`, MINT-H135 = `3ddc41389e6d484f`, MINT-H136 = `29bbba1adec778da`, MINT-H137 = `cff2d5fb5e0d4149`, MINT-H141 = `a348875c3f707895`, MINT-H142 = `2d654c836f3731c6`, MINT-H145 = `b0f80776885f3ae1`, MINT-H146 = `59585d778cb3a7a4`, MINT-H147 = `095ce61d28388c98`, MINT-H148 = `c49077384aaebeb0`, MINT-H150 = `9be0f2271a14b6a9`, MINT-H153 = `dcc38ea9177089b9`, MINT-H157 = `34351050a4f29035`, MINT-H158 = `24a6b511067d37b2`, MINT-H159 = `042c19cbfdc869cb`, MINT-H160 = `7a448bed1119dfad`, MINT-H161 = `f6f8b3050a1eef42`, MINT-H162 = `d718e083bd23d2b1`, MINT-H163 = `8cc8c5ab3cf36d8f`, MINT-H165 = `d176b8d859dd651a`, MINT-H166 = `30f2a1e483babf55`, MINT-H167 = `437fbe758a6dd8e3`, MINT-H168 = `0948aa6184f13a8a`, MINT-H169 = `a182e87006c7a00d`, MINT-H176 = `e19babba732f5fd4`, MINT-H177 = `dd3fb07fe11d73d3`, MINT-H194 = `257b627a90b78038`, MINT-H201 = `e0bf1a48f096c10d`, MINT-H203 = `f14a8c4e7c5b3e3a`, MINT-H207 = `7715c7010e513b71`, MINT-H208 = `505a4911e298c933`, MINT-H635 = `cda1d1c03659b67d`, MINT-H636 = `2165f5c5260120de`, MINT-H637 = `d10bb4a25bbf4c80`, MINT-H638 = `c82ebc15c49c1413`, MINT-H639 = `4a560e459032166a`, MINT-H640 = `87c94384d7851cb2`, MINT-H641 = `466b12546dd936c3`, MINT-H642 = `c53bc05bc306c97d`, MINT-H643 = `74a69fba4266de3b`, MINT-H645 = `5b86a254c715306c`, MINT-H646 = `ac4489d658eb445e`, MINT-H648 = `af8b2135c913b13b`, MINT-H650 = `e598ffd8a1cac138`, MINT-H651 = `a93f8fe7ecdc5851`, MINT-H652 = `75bbbcb4a37e70e8`, MINT-H653 = `3a491fd6426d90b2`, MINT-H654 = `fac4317d5a65b959`, MINT-H655 = `5f812747976b224a`, MINT-H660 = `d0c5a15c25ab6413`, MINT-H661 = `07d543d89e2934f2`, MINT-H663 = `d770abfcee4deb90`, MINT-H664 = `cbead3df2d2f1d0e`, MINT-H665 = `fcffad0da2b5b62f`, MINT-H667 = `59b28b3a59c27092`, MINT-H668 = `37aa18e6e10583be`, MINT-H670 = `2081d7b9a734e4fe`, MINT-H671 = `27dbb77012555d28`, MINT-H672 = `e1a38303b2378f17`, MINT-H673 = `6f4101f83371033d`, MINT-H674 = `d9ac68100a276dfe`, MINT-H675 = `646b518ccf3bd724`, MINT-H676 = `322d5ff451e4101d`, MINT-H678 = `8d90c524c89922d9`, MINT-H679 = `d07f950b8309de82`, MINT-H680 = `27d463eac6cda5ea`, MINT-H681 = `aef8972953d53d20`, MINT-H683 = `7e05ce00d8a7cbf6`, MINT-H687 = `0b5d9beb0fc972f6`, MINT-H692 = `43e4e46001b4d8b9`.
- Pool check: 13 tetragonal + 102 hexagonal-family = 115, equal to PROGRAM_LEDGER 2026-09-04 14:10 ('13 tetragonal + 102 hexagonal'); asserted in build_catalog.py and recounted from the raw verdict / screen / certificate files by verify_counts_independent.py v3. Pool membership is catalog-relative; G5 diligence (print-only Engel / Koch exposure) still applies before any name.

### Certified phase-2 cells outside the pool (WALL / ONE-SIDED), with the naming-relevant facts

Wall directions, the neighbouring types on each side and their Schmitt status are in `WALL_OPEN_PHASE2.md` section 'Wall cells (41) and their neighbouring types'; flags are never verdict inputs (line_isolated = stratum dim 1 and the single point direction is WALL; nonsimple_vertex = non-simple vertices at the witness; degenerate_flag_any = a float degeneracy flag on some perturbed cell, exact superseding).

| catalog id | type | family | IT | c/a | f | aut | COMBINED | POINT | METRIC | flags |
|---|---|---|---|---|---|---|---|---|---|---|
| MINT-T755 | `49cedbdd58376fac` | tetragonal | 92 P4_12_12 | 19/16 | (44,66,24) | 2 | **WALL** | WALL | OPEN | line_isolated |
| MINT-H008 | `78e755ffdff3a2f5` | hexagonal | 146 R3 | 3/4 | (14,24,12) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H018 | `105e41c2798e6180` | hexagonal | 148 R-3 | 2 | (16,27,13) | 6 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H023 | `c18a9b1cb2a5d168` | hexagonal | 148 R-3 | 1/2 | (26,40,16) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H028 | `1ba26ab2c0999b93` | hexagonal | 148 R-3 | 1/2 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H029 | `6074c5fa5d2dffc5` | hexagonal | 148 R-3 | 3/4 | (16,26,12) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H033 | `4db369a636f4396b` | hexagonal | 151 P3_112 | 3/2 | (18,30,14) | 4 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H049 | `0417061f8f56488e` | hexagonal | 152 P3_121 | 1/2 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H056 | `7e023be581e7c50a` | hexagonal | 154 P3_221 | 3/4 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |
| MINT-H057 | `66563d07a1110a25` | hexagonal | 154 P3_221 | 1 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |
| MINT-H061 | `d1f1121757598de0` | hexagonal | 154 P3_221 | 9/4 | (15,25,12) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H071 | `d70e6901953070e7` | hexagonal | 155 R32 | 3/4 | (38,58,22) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H074 | `67b1ede4b021a4fc` | hexagonal | 155 R32 | 3/2 | (17,29,14) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H076 | `d0ed9179c6947b5f` | hexagonal | 155 R32 | 1/2 | (16,26,12) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H079 | `b27ba8dbcbc2891a` | hexagonal | 161 R3c | 1/2 | (22,34,14) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H096 | `c95a5fcf4d681568` | hexagonal | 166 R-3m | 3/2 | (12,21,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H099 | `34e5e7acce18b5cd` | hexagonal | 166 R-3m | 3/2 | (14,23,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H101 | `090dcafb7ce9cb08` | hexagonal | 166 R-3m | 1/2 | (20,32,14) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H102 | `9bc4922a7b574aa6` | hexagonal | 166 R-3m | 3/4 | (17,28,13) | 2 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H111 | `f7bd7cd9eae6436b` | hexagonal | 166 R-3m | 1 | (16,27,13) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H122 | `4ff9d77aa9f8194a` | hexagonal | 167 R-3c | 3/4 | (24,37,15) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H123 | `400cba5c78326d1d` | hexagonal | 167 R-3c | 1 | (17,28,13) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H124 | `5e68ffe7582a0657` | hexagonal | 167 R-3c | 1/2 | (20,31,13) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H132 | `d7c638d7fa23127e` | hexagonal | 169 P6_1 | 3/2 | (25,39,16) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H143 | `7e79f1c38b5516bf` | hexagonal | 178 P6_122 | 3/2 | (22,34,14) | 2 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H144 | `161b09808f4c1863` | hexagonal | 178 P6_122 | 2 | (18,30,14) | 4 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H152 | `f07d69523ef41b37` | hexagonal | 178 P6_122 | 3/2 | (20,36,18) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H155 | `5beb94b61eb66eb1` | hexagonal | 178 P6_122 | 1/2 | (27,41,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H156 | `bc59e5d778f60d1f` | hexagonal | 178 P6_122 | 3/4 | (29,44,17) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H170 | `8463196a30c6643f` | hexagonal | 179 P6_522 | 2 | (23,36,15) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H172 | `95934e84555dc2ea` | hexagonal | 179 P6_522 | 1/2 | (26,40,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H173 | `4885ce1e70fa9713` | hexagonal | 179 P6_522 | 3/4 | (27,41,16) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H174 | `f5fbebffa76808d5` | hexagonal | 179 P6_522 | 5/4 | (31,47,18) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H175 | `c92eef8763d02d8a` | hexagonal | 179 P6_522 | 3/2 | (25,39,16) | 1 | **WALL** | WALL | WALL | degenerate_flag_any, nonsimple_vertex |
| MINT-H181 | `457c20cf036ae496` | hexagonal | 180 P6_222 | 3/2 | (11,20,11) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H191 | `fa9c370d30741970` | hexagonal | 180 P6_222 | 3/2 | (9,16,9) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H209 | `6cc34ed38aa354e1` | hexagonal | 181 P6_422 | 1/2 | (22,34,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H644 | `9d0b36ad5caceb2e` | hexagonal | 167 R-3c | 7/8 | (22,35,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H656 | `487490cdf474e568` | hexagonal | 148 R-3 | 1277/2000 | (20,32,14) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H657 | `f0e2036d295195b4` | hexagonal | 152 P3_121 | 9/8 | (12,20,10) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H658 | `7472d8ba000c8056` | hexagonal | 152 P3_121 | 9/8 | (22,36,16) | 2 | **WALL** | WALL | WALL | degenerate_flag_any, line_isolated, nonsimple_vertex |
| MINT-H659 | `75c9be976d704515` | hexagonal | 152 P3_121 | 9/8 | (18,28,12) | 2 | **WALL** | WALL | WALL | line_isolated, nonsimple_vertex |
| MINT-H662 | `5b679d8b0a3147c3` | hexagonal | 152 P3_121 | 17/16 | (24,38,16) | 1 | **WALL** | WALL | ONE-SIDED | degenerate_flag_any, nonsimple_vertex |
| MINT-H666 | `919d30fd9021b5ee` | hexagonal | 154 P3_221 | 51/32 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H669 | `f43b45fd6383b36b` | hexagonal | 155 R32 | 19/16 | (26,41,17) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H677 | `71d2c9953ca110b8` | hexagonal | 169 P6_1 | 39/32 | (36,54,20) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | - |
| MINT-H682 | `4b6055c7aa3d341b` | hexagonal | 178 P6_122 | 17/8 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H684 | `11a9fe078850b5cd` | hexagonal | 179 P6_522 | 65/32 | (25,38,15) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H685 | `272aefcd5e48ba49` | hexagonal | 179 P6_522 | 9/8 | (29,44,17) | 1 | **WALL** | WALL | OPEN | degenerate_flag_any, nonsimple_vertex |
| MINT-H686 | `60eb4282db04fca2` | hexagonal | 179 P6_522 | 11/8 | (30,45,17) | 1 | **ONE-SIDED** | ONE-SIDED | OPEN | degenerate_flag_any |

### Limits (v4)

- Every verdict is for the stored FIRST witness of the type only (one point, one c/a); a type OPEN here may have other sightings on a wall, and a WALL witness does not preclude an open region of the same type elsewhere.
- Finite steps: point 1/48, 1/96 halved to 1/1536; metric c/a(1 +- 1/96, 1/192) halved to 1/3072 (relative, so coarser than 1/96 absolute for the five cells with c/a > 2, stated in WALL_OPEN_PHASE2.md); OPEN is 'holds on the tested neighbourhood', ONE-SIDED is a short neighbourhood, neither is an interval proof.
- The heuristic open-likely / wall-suspect / indeterminate labels disagreed with the computed verdict on 35 of the 165 cells in both directions (WALL_OPEN_PHASE2.md); the catalog carries the computed verdict and keeps the label only inside open_wall_verdict_pointer.
- Tetragonal type-level status (v4) is the store-side rule's: COLLISION 177 (the 176 S-cells + the shortlist's cd4fb52572edcb73) / SURVIVOR 121 / UNRESOLVED 106 of the 404 menu-sighted types. Each UNRESOLVED type has an unstored printed row (two-origin groups, second enantiomorphs 95/96, IT(80)) at its (group, f) that no recomputation has touched; only the 27 shortlist pairs were recomputed at the printed points, so UNRESOLVED is neither survivor nor collision. The tetragonal digitization is a single visual pass, text-layer cross-checked, not re-keyed.
- Cubic-first types are not-screened by the two phase-2 screens by construction; their cubic-round verdicts (SCHMITT_COLLISION_RESULTS.md, CROSS_GROUP_RESULTS.md) stay in schmitt_type_level_*.
- No new digitization, perturbation or certificate was computed here; the section only cross-tabulates accepted records. Snapshot wording throughout.


## v5 (2026-09-04): the 62 unstored tetragonal rows recomputed; the 106 UNRESOLVED settled (no tetragonal UNRESOLVED left)

Appended by `catalog/reconcile_schmitt.py` v5 from `catalog/catalog.json` v5 (1,583 types; snapshot 2026-09-04); deterministic. Everything above this heading is the v1 text + the v2, v3 and v4 sections, preserved byte for byte (asserted for v1 + v2 by regeneration from the v5 catalog; the v3 and v4 sections are the pre-recomputation record and are kept verbatim: the v4 tetragonal column 'UNRESOLVED 106' is superseded below); v4 of this script = `git show 27e0083:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py`. Sources of the two columns cross-tabulated here: `harness/phase2/WALL_OPEN_PHASE2.json` (computed open/wall verdicts of the 165 G4-certified phase-2 cells at their stored first witness; agent #148; accepted 2026-09-04 14:10, JSON md5 6b257c551f6fb275dfabb03e992f57c2), `harness/round1_computations/c1_wall_open.json` (the 7 cubic finalists), `harness/COLLISION_PHASE2_RESULTS.md` (tetragonal top-15 shortlist, 27 printed pairs; ADDENDUM 2026-09-04 #152 = the store-side rule over all 404 menu-sighted tetragonal types, `collision_phase2_tetragonal_storeside.json`; ADDENDUM 2026-09-04 #154 = the 62 unstored printed rows behind the 106 UNRESOLVED recomputed at the printed points with the documented setting conversions, `collision_phase2_tetragonal_rows_recomputed.json` md5 4d27ce41466509feab6a180249330af7 + `collision_phase2_tetragonal_unresolved_overlay.json` md5 a3716a2330c6dbe9c93414dfe8e832ee) and `harness/COLLISION_PHASE2_HEX_RESULTS.md` (store-side screen of the 288 menu-sighted hexagonal-first types; top-10 recomputed at the printed points). Wording, stated once: OPEN = the type holds on the tested neighbourhood of its first witness at finite steps (point 1/1536, metric 1/3072 relative), never an interval proof; WALL = the witness sits on a transition (both sides of some direction change); ONE-SIDED = some side changes but no direction on both sides (a short neighbourhood, not a wall); SURVIVOR = not matched at the printed representatives checked (records checked as of 2026-09-04), never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe); printed-only = an S-cell never reached by our menu; not-screened = outside both phase-2 screens (all cubic-first types by construction; no tetragonal-first type). A wall cell is excluded from the naming pool because its witness sits on a transition; nothing here proposes a name.

### Cross-tab per family: open_wall_verdict (rows) x schmitt_type_status (columns)

**cubic-first** (102 types; verdicts OPEN 6, WALL 1, ONE-SIDED 0, not-computed 95; statuses SURVIVOR 0, COLLISION 0, UNRESOLVED 0, printed-only 0, not-screened 102):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 0 | 0 | 0 | 0 | 6 | 6 |
| WALL | 0 | 0 | 0 | 0 | 1 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 0 | 0 | 0 | 0 | 95 | 95 |
| total | 0 | 0 | 0 | 0 | 102 | 102 |

**tetragonal-first** (789 types; verdicts OPEN 13, WALL 1, ONE-SIDED 0, not-computed 775; statuses SURVIVOR 203, COLLISION 201, UNRESOLVED 0, printed-only 385, not-screened 0):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 13 | 0 | 0 | 0 | 0 | 13 |
| WALL | 1 | 0 | 0 | 0 | 0 | 1 |
| ONE-SIDED | 0 | 0 | 0 | 0 | 0 | 0 |
| not-computed | 189 | 201 | 0 | 385 | 0 | 775 |
| total | 203 | 201 | 0 | 385 | 0 | 789 |

**hexagonal-first** (692 types; verdicts OPEN 102, WALL 40, ONE-SIDED 9, not-computed 541; statuses SURVIVOR 151, COLLISION 124, UNRESOLVED 13, printed-only 404, not-screened 0):

| verdict \ status | SURVIVOR | COLLISION | UNRESOLVED | printed-only | not-screened | total |
|---|---|---|---|---|---|---|
| OPEN | 102 | 0 | 0 | 0 | 0 | 102 |
| WALL | 40 | 0 | 0 | 0 | 0 | 40 |
| ONE-SIDED | 9 | 0 | 0 | 0 | 0 | 9 |
| not-computed | 0 | 124 | 13 | 404 | 0 | 541 |
| total | 151 | 124 | 13 | 404 | 0 | 692 |

### Tetragonal type-level status, v4 -> v5 (the 62 unstored printed rows behind the 106 UNRESOLVED recomputed)

Source: v5: harness/collision_phase2_tetragonal_unresolved_overlay.json + collision_phase2_tetragonal_rows_recomputed.json (subagent #154, 2026-09-04; script harness/collision_phase2_tetragonal_rows_recompute.py; dated addendum in harness/COLLISION_PHASE2_RESULTS.md): the 62 unstored printed rows behind the 106 v4-UNRESOLVED types recomputed at the printed points with the documented setting conversions of PHASE2_SCHMITT_ORIGIN_CHECK.md through the accepted phase-2 exact chain; overlay JSON md5 a3716a2330c6dbe9c93414dfe8e832ee, rows JSON md5 4d27ce41466509feab6a180249330af7. Rule (stated once): per UNRESOLVED type (collision_phase2_tetragonal_storeside.json status UNRESOLVED): compare its canonical code with the recomputed cell of every printed row it hangs on (unstored_rows): any SAME TYPE -> COLLISION (the type reproduces one of his printed cells; first-realization reframe); every row REPRODUCED and DIFFERENT TYPE -> SURVIVOR ('not matched against the records checked as of 2026-09-04', never novelty); any row not REPRODUCED and no SAME -> UNRESOLVED Rows: 62 recomputed (306 cells: every documented convention of the group plus the other origin / enantiomorph reading, recorded), status counts {'REPRODUCED': 62}; documented conventions agree on the code in 62/62 rows; the other reading reproduces the printed f in 0/62 (it is pass P2's quarantined run); 18 row cells are stored under no id (types our menu never sampled; read-only, not added); row cells that are stored types outside the 106: {'SURVIVOR_hits': 0, 'cubic_first_hits': 2, 'expected_S_cell_hits_COLLISION_or_printed_only': 15}.

| count | SURVIVOR | COLLISION | UNRESOLVED |
|---|---|---|---|
| catalog v3 (top-15 recomputation only; not-screened = 389) | 14 | 1 | 0 |
| pure store-side rule | 116 | 176 | 112 |
| v4 = rule + recomputed shortlist pairs overlaid | 121 | 177 | 106 |
| the 106 v4-UNRESOLVED after recomputation | 82 | 24 | 0 |
| v5 = v4 + the 106 settled | 203 | 201 | 0 |

Transitions v4 -> v5 over the 404 menu-sighted tetragonal-first types: COLLISION -> COLLISION: 177; SURVIVOR -> SURVIVOR: 121; UNRESOLVED -> COLLISION: 24; UNRESOLVED -> SURVIVOR: 82. Still UNRESOLVED: 0. Secondary hits (a type's code equal to the cell of a row it does not hang on; no status effect): 1. The 385 Schmitt-printed-only tetragonal types stay printed-only; the 102 cubic-first types stay not-screened (scope fact); the 15 shortlist statuses and the 14 certified survivors are untouched (none was UNRESOLVED).

Recorded facts from the recomputation (no status effect): (1) IT(137) b=3497/1000 pt=(1/4, -1/4, 1/4): row cell = cubic-first store type c1824c64dfbb3615 (f (18, 28, 12), p 4^8 6^4, aut 16): a cubic-store type IS Schmitt's printed representative at this tetragonal row (cross-system fact; cubic-first types are not-screened by the phase-2 screens by construction; recorded only) (2) IT(95) b=797/1000 pt=(309/500, 59/500, 1/8): row cell = cubic-first store type 8c69db9e84095469 (f (30, 45, 17), p 4^6 5^6 6^2 8^3, aut 12): a cubic-store type IS Schmitt's printed representative at this tetragonal row (cross-system fact; cubic-first types are not-screened by the phase-2 screens by construction; recorded only) (3) type 5c6382a9ef3bc209 (COLLISION by its hung-on rows) also equals the recomputed cell of a row it does not hang on (a printed cell of the type in a group where our menu never sighted it): [[142, '3497/1000', ['58/125', '58/125', '29/250']]]; no status effect

### Naming pool = G4-certified AND open_wall_verdict OPEN AND unnamed, per family

- cubic: **0** of 12 accepted-cubic types: the 6 OPEN cells (c1) all carry a name or a marker already (`ceb70631e274e727` IT212_37-57-22_HELD [HELD]; `aa6b0077c3234d24` IT214_30-47-19_HELD [HELD]; `2de0a21129cabe90` Ordenhedron [named]; `c4ea3f32fdd6dc51` Pn3m_11facet [descriptive package name]; `f98a3ee5675fc121` Pn3m_7facet [descriptive package name]; `359beee832567a71` IT230_40-61-23_HELD [HELD]); the Satchelhedron is the cubic WALL cell; 5 accepted-cubic types have no perturbation run on record (`8c69db9e84095469`, `c314dedd38208a2e`, `f3d0f39a0b9676b9`, `d2d935e5499e6e11`, `9b69eefb8bd8437c`).
- tetragonal: **13** of 14 certified (13 OPEN, 1 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-T004 = `164d4bd63d82d0c3`, MINT-T005 = `6797ab70c6015039`, MINT-T076 = `1497877268495988`, MINT-T137 = `7575121042ade3b3`, MINT-T151 = `3ebbca7ed2eda199`, MINT-T152 = `4f6d3e68cbd9e729`, MINT-T264 = `f654982d74d740f6`, MINT-T716 = `086ac96faf390886`, MINT-T721 = `4e9c9b076cfec323`, MINT-T722 = `e0d18e5ea938d649`, MINT-T758 = `2e8e49eb28497267`, MINT-T766 = `5dc2479b9bc14edc`, MINT-T767 = `213c7a114d5a97a8`.
- hexagonal: **102** of 151 certified (102 OPEN, 49 WALL / ONE-SIDED, 0 not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): MINT-H002 = `bff9b24ce78050f5`, MINT-H003 = `c0071756347c5a8a`, MINT-H007 = `7b9cfe26fe4a9c4b`, MINT-H021 = `f0b07b168368759b`, MINT-H024 = `f429e996b3f455a6`, MINT-H025 = `56918d2cff883e22`, MINT-H034 = `ce3b42c8a4ceff6f`, MINT-H035 = `36ec4ad2f530e145`, MINT-H041 = `e98412e7cb95aea2`, MINT-H045 = `847d2695a14ae424`, MINT-H047 = `5838282f46223111`, MINT-H050 = `72bcd959be4ab7dd`, MINT-H051 = `e198aac88f223892`, MINT-H052 = `23594bd7053503aa`, MINT-H055 = `b2430fc4bea4e06d`, MINT-H058 = `542cbe76934b484b`, MINT-H059 = `3d6b109f392fda19`, MINT-H063 = `2c121297dbaa80af`, MINT-H065 = `64203f15fcf6c09b`, MINT-H070 = `a46cbaad3c23e834`, MINT-H072 = `c3b4b14633c9d4d5`, MINT-H073 = `d9bf7fb7a80eaa38`, MINT-H095 = `9d4396ca0b08fc3c`, MINT-H105 = `ab801b11bead62ef`, MINT-H112 = `36c92427e3d084dc`, MINT-H120 = `057255f61286b052`, MINT-H121 = `6de3dac5f334cfed`, MINT-H126 = `85244add8d1f2d55`, MINT-H127 = `f05f0b009e0929f6`, MINT-H128 = `16025e0680843c36`, MINT-H129 = `a35623e347ef03b4`, MINT-H131 = `9c0b7e0c29dfebb2`, MINT-H133 = `2b9726574a0a8bed`, MINT-H135 = `3ddc41389e6d484f`, MINT-H136 = `29bbba1adec778da`, MINT-H137 = `cff2d5fb5e0d4149`, MINT-H141 = `a348875c3f707895`, MINT-H142 = `2d654c836f3731c6`, MINT-H145 = `b0f80776885f3ae1`, MINT-H146 = `59585d778cb3a7a4`, MINT-H147 = `095ce61d28388c98`, MINT-H148 = `c49077384aaebeb0`, MINT-H150 = `9be0f2271a14b6a9`, MINT-H153 = `dcc38ea9177089b9`, MINT-H157 = `34351050a4f29035`, MINT-H158 = `24a6b511067d37b2`, MINT-H159 = `042c19cbfdc869cb`, MINT-H160 = `7a448bed1119dfad`, MINT-H161 = `f6f8b3050a1eef42`, MINT-H162 = `d718e083bd23d2b1`, MINT-H163 = `8cc8c5ab3cf36d8f`, MINT-H165 = `d176b8d859dd651a`, MINT-H166 = `30f2a1e483babf55`, MINT-H167 = `437fbe758a6dd8e3`, MINT-H168 = `0948aa6184f13a8a`, MINT-H169 = `a182e87006c7a00d`, MINT-H176 = `e19babba732f5fd4`, MINT-H177 = `dd3fb07fe11d73d3`, MINT-H194 = `257b627a90b78038`, MINT-H201 = `e0bf1a48f096c10d`, MINT-H203 = `f14a8c4e7c5b3e3a`, MINT-H207 = `7715c7010e513b71`, MINT-H208 = `505a4911e298c933`, MINT-H635 = `cda1d1c03659b67d`, MINT-H636 = `2165f5c5260120de`, MINT-H637 = `d10bb4a25bbf4c80`, MINT-H638 = `c82ebc15c49c1413`, MINT-H639 = `4a560e459032166a`, MINT-H640 = `87c94384d7851cb2`, MINT-H641 = `466b12546dd936c3`, MINT-H642 = `c53bc05bc306c97d`, MINT-H643 = `74a69fba4266de3b`, MINT-H645 = `5b86a254c715306c`, MINT-H646 = `ac4489d658eb445e`, MINT-H648 = `af8b2135c913b13b`, MINT-H650 = `e598ffd8a1cac138`, MINT-H651 = `a93f8fe7ecdc5851`, MINT-H652 = `75bbbcb4a37e70e8`, MINT-H653 = `3a491fd6426d90b2`, MINT-H654 = `fac4317d5a65b959`, MINT-H655 = `5f812747976b224a`, MINT-H660 = `d0c5a15c25ab6413`, MINT-H661 = `07d543d89e2934f2`, MINT-H663 = `d770abfcee4deb90`, MINT-H664 = `cbead3df2d2f1d0e`, MINT-H665 = `fcffad0da2b5b62f`, MINT-H667 = `59b28b3a59c27092`, MINT-H668 = `37aa18e6e10583be`, MINT-H670 = `2081d7b9a734e4fe`, MINT-H671 = `27dbb77012555d28`, MINT-H672 = `e1a38303b2378f17`, MINT-H673 = `6f4101f83371033d`, MINT-H674 = `d9ac68100a276dfe`, MINT-H675 = `646b518ccf3bd724`, MINT-H676 = `322d5ff451e4101d`, MINT-H678 = `8d90c524c89922d9`, MINT-H679 = `d07f950b8309de82`, MINT-H680 = `27d463eac6cda5ea`, MINT-H681 = `aef8972953d53d20`, MINT-H683 = `7e05ce00d8a7cbf6`, MINT-H687 = `0b5d9beb0fc972f6`, MINT-H692 = `43e4e46001b4d8b9`.
- Pool check: 13 tetragonal + 102 hexagonal-family = 115, equal to PROGRAM_LEDGER 2026-09-04 14:10 ('13 tetragonal + 102 hexagonal'); asserted in build_catalog.py and recounted from the raw verdict / screen / certificate files by verify_counts_independent.py. Pool membership is catalog-relative; G5 diligence (print-only Engel / Koch exposure) still applies before any name. The certified phase-2 cells outside the pool (WALL / ONE-SIDED) are tabulated in the v4 section above; nothing about them changed in v5.

### Limits (v5)

- Every verdict is for the stored FIRST witness of the type only (one point, one c/a); a type OPEN here may have other sightings on a wall, and a WALL witness does not preclude an open region of the same type elsewhere.
- Finite steps: point 1/48, 1/96 halved to 1/1536; metric c/a(1 +- 1/96, 1/192) halved to 1/3072 (relative, so coarser than 1/96 absolute for the five cells with c/a > 2, stated in WALL_OPEN_PHASE2.md); OPEN is 'holds on the tested neighbourhood', ONE-SIDED is a short neighbourhood, neither is an interval proof.
- Tetragonal type-level status (v5): COLLISION 201 (the 176 S-cells + the shortlist's cd4fb52572edcb73 + the 24 v4-UNRESOLVED types whose recomputed hung-on row IS the type) / SURVIVOR 203 / UNRESOLVED 0 of the 404 menu-sighted types. Every printed row at a menu-sighted type's (group, f) has now been reproduced by the exact chain (stored by pass P2, recomputed for the 27 shortlist pairs, or recomputed here for the 62 unstored rows), so SURVIVOR is type-level at every printed representative of the type's (group, f) pairs; it remains catalog-relative: his tables print ONE point per (group, f) from a grid sampling. The tetragonal digitization is a single visual pass, text-layer cross-checked, not re-keyed; the setting conversions are the machine-verified ones of PHASE2_SCHMITT_ORIGIN_CHECK.md (every printed row of each group reproduces under them; here 62/62 again).
- Cubic-first types are not-screened by the two phase-2 screens by construction; their cubic-round verdicts (SCHMITT_COLLISION_RESULTS.md, CROSS_GROUP_RESULTS.md) stay in schmitt_type_level_*. Two of the 62 recomputed rows are cubic-store types (recorded above), a cross-system fact and not a status change.
- No new digitization, perturbation or certificate was computed here; the section only cross-tabulates accepted and staged records (the #154 recomputation is provisional until the main-session re-run). Snapshot wording throughout.

