# the IT(212) (37,57,22) cell — exact generating data and coordinates

Type id `ceb70631e274e727` · status: **HELD (Engel/Koch ILL check)** · mined-group finalist; NOT to be named before the ILL check.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_ceb70631e274e727.json`.

## Generating data

- Space group: IT(212) = P4_332 (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (1/12, 1/12, 1/12) — special position (Wyckoff stratum dimension 1, site-symmetry order 3)
- Orbit: 8 points per conventional cell, T = 8 translation classes (primitive)
- Integer scaling: PERIOD = 12 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-12, 0, 0], [0, -12, 0], [0, 0, -12]] with |det| = 1728
- Exact cell volume: 216 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (37, 57, 22)
- p-vector: 3^6 4^6 5^6 10^3 12^1
- Combinatorial automorphism order: 3 (canonical code)
- Site symmetry order: 3; geometric stabilizer order: 3 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 24 (24 proper, 0 improper)
- Chirality status: CHIRAL honeycomb: all 24 honeycomb ops proper; site = stab_geo = aut = 3
- Non-simple vertices: 3 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 12)

```
(1, 1, 1)
(2, 2, 2)
(4, 10, 8)
(5, 11, 7)
(7, 5, 11)
(8, 4, 10)
(10, 8, 4)
(11, 7, 5)
```

## Exact vertex coordinates of one cell (site (1, 1, 1), same integer scaling)

37 vertices (exact Fractions), followed by the 22 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-69/16, 3/4, 39/16)
v1: (-405/94, 75/94, 237/94)
v2: (-357/94, -123/94, -45/94)
v3: (-15/4, -21/16, -9/16)
v4: (-15/4, 9/4, 15/4)
v5: (-51/14, -3/2, -9/14)
v6: (-327/94, -159/94, -75/94)
v7: (-237/94, 159/94, 489/94)
v8: (-39/16, 27/16, 21/4)
v9: (-33/14, 3/2, 75/14)
v10: (-9/4, -9/4, -9/4)
v11: (-9/4, 21/16, 87/16)
v12: (-159/94, -75/94, -327/94)
v13: (-3/2, -9/14, -51/14)
v14: (-3/2, 9/2, 3/2)
v15: (-21/16, -9/16, -15/4)
v16: (-123/94, -45/94, -357/94)
v17: (-75/94, -327/94, -159/94)
v18: (-9/14, -51/14, -3/2)
v19: (-9/16, -15/4, -21/16)
v20: (-45/94, -357/94, -123/94)
v21: (3/4, 39/16, -69/16)
v22: (75/94, 237/94, -405/94)
v23: (21/16, 87/16, -9/4)
v24: (3/2, -3/2, 9/2)
v25: (3/2, 75/14, -33/14)
v26: (27/16, 21/4, -39/16)
v27: (159/94, 489/94, -237/94)
v28: (9/4, 15/4, -15/4)
v29: (39/16, -69/16, 3/4)
v30: (237/94, -405/94, 75/94)
v31: (15/4, -15/4, 9/4)
v32: (9/2, 3/2, -3/2)
v33: (489/94, -237/94, 159/94)
v34: (21/4, -39/16, 27/16)
v35: (75/14, -33/14, 3/2)
v36: (87/16, -9/4, 21/16)

facet 12-gon [14, 8, 9, 11, 24, 34, 35, 36, 32, 26, 25, 23]  neighbor site (2, 2, 2)
facet 10-gon [3, 2, 0, 14, 23, 22, 21, 16, 13, 12]  neighbor site (-4, 4, -2)
facet 10-gon [2, 5, 6, 19, 20, 29, 24, 11, 1, 0]  neighbor site (-2, -4, 4)
facet 10-gon [20, 18, 17, 15, 16, 21, 32, 36, 30, 29]  neighbor site (4, -2, -4)
facet 4-gon [4, 14, 0, 1]  neighbor site (-5, 5, -1)
facet 4-gon [31, 24, 29, 30]  neighbor site (-1, -5, 5)
facet 4-gon [14, 4, 7, 8]  neighbor site (-1, 7, 5)
facet 4-gon [28, 32, 21, 22]  neighbor site (5, -1, -5)
facet 4-gon [24, 31, 33, 34]  neighbor site (5, -1, 7)
facet 4-gon [32, 28, 27, 26]  neighbor site (7, 5, -1)
facet 5-gon [6, 5, 3, 12, 10]  neighbor site (-7, -1, -5)
facet 5-gon [11, 9, 7, 4, 1]  neighbor site (-7, -1, 7)
facet 5-gon [10, 17, 18, 19, 6]  neighbor site (-5, -7, -1)
facet 5-gon [12, 13, 15, 17, 10]  neighbor site (-1, -5, -7)
facet 5-gon [27, 28, 22, 23, 25]  neighbor site (-1, 7, -7)
facet 5-gon [36, 35, 33, 31, 30]  neighbor site (7, -7, -1)
facet 3-gon [3, 5, 2]  neighbor site (-8, -2, -4)
facet 3-gon [20, 19, 18]  neighbor site (-4, -8, -2)
facet 3-gon [8, 7, 9]  neighbor site (-4, 4, 10)
facet 3-gon [15, 13, 16]  neighbor site (-2, -4, -8)
facet 3-gon [27, 25, 26]  neighbor site (4, 10, -4)
facet 3-gon [34, 33, 35]  neighbor site (10, -4, 4)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** full isometry group order 3 (= site, all proper), aut 3 with 0 reversing elements; type OPEN on the 8c line.
