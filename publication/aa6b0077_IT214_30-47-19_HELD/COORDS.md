# the IT(214) (30,47,19) cell — exact generating data and coordinates

Type id `aa6b0077c3234d24` · status: **HELD (Engel/Koch ILL check)** · mined-group finalist; NOT to be named before the ILL check.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_aa6b0077c3234d24.json`.

## Generating data

- Space group: IT(214) = I4_132 (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (0, 1/4, 1/12) — special position (Wyckoff stratum dimension 1, site-symmetry order 2)
- Orbit: 24 points per conventional cell, T = 12 translation classes (primitive)
- Integer scaling: PERIOD = 12 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-6, -6, -6], [-6, -6, 6], [-6, 6, -6]] with |det| = 864
- Exact cell volume: 72 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (30, 47, 19)
- p-vector: 3^4 4^5 5^6 6^2 10^2
- Combinatorial automorphism order: 2 (canonical code)
- Site symmetry order: 2; geometric stabilizer order: 2 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 24 (24 proper, 0 improper)
- Chirality status: CHIRAL honeycomb: all 24 honeycomb ops proper; site = stab_geo = aut = 2
- Non-simple vertices: 4 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 12)

```
(0, 3, 1)
(0, 3, 2)
(0, 9, 4)
(0, 9, 5)
(1, 0, 3)
(2, 0, 3)
(3, 1, 0)
(3, 2, 0)
(3, 10, 6)
(3, 11, 6)
(4, 0, 9)
(5, 0, 9)
(6, 3, 10)
(6, 3, 11)
(6, 9, 7)
(6, 9, 8)
(7, 6, 9)
(8, 6, 9)
(9, 4, 0)
(9, 5, 0)
(9, 7, 6)
(9, 8, 6)
(10, 6, 3)
(11, 6, 3)
```

## Exact vertex coordinates of one cell (site (0, 3, 1), same integer scaling)

30 vertices (exact Fractions), followed by the 19 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-3, 0, 3/2)
v1: (-111/40, -9/8, -3/10)
v2: (-21/8, -29/24, -1/2)
v3: (-9/4, -3/4, -3/2)
v4: (-43/24, -3/8, -5/2)
v5: (-3/2, -3/2, -3/2)
v6: (-3/2, 0, -3)
v7: (-3/2, 9/2, 3/2)
v8: (-29/24, -1/2, -21/8)
v9: (-29/24, 1/2, -27/8)
v10: (-9/8, -3/10, -111/40)
v11: (-9/8, 3/10, -129/40)
v12: (-3/4, 3/2, -15/4)
v13: (-9/40, 27/10, -33/8)
v14: (0, 3/2, -3)
v15: (0, 9/2, -3)
v16: (9/40, 33/10, -33/8)
v17: (3/4, 9/2, -15/4)
v18: (9/8, 57/10, -129/40)
v19: (9/8, 63/10, -111/40)
v20: (29/24, 11/2, -27/8)
v21: (29/24, 13/2, -21/8)
v22: (3/2, 3/2, 3/2)
v23: (3/2, 6, -3)
v24: (3/2, 15/2, -3/2)
v25: (43/24, 51/8, -5/2)
v26: (9/4, 27/4, -3/2)
v27: (21/8, 173/24, -1/2)
v28: (111/40, 57/8, -3/10)
v29: (3, 6, 3/2)

facet 4-gon [0, 22, 29, 7]  neighbor site (0, 3, 2)
facet 10-gon [15, 13, 12, 9, 6, 4, 3, 1, 0, 7]  neighbor site (-3, 4, 0)
facet 10-gon [26, 28, 29, 22, 14, 16, 17, 20, 23, 25]  neighbor site (3, 2, 0)
facet 5-gon [24, 21, 19, 15, 7]  neighbor site (-3, 5, 0)
facet 5-gon [7, 29, 28, 27, 24]  neighbor site (-1, 6, 3)
facet 5-gon [1, 2, 5, 22, 0]  neighbor site (1, 0, 3)
facet 5-gon [5, 8, 10, 14, 22]  neighbor site (3, 1, 0)
facet 6-gon [19, 18, 17, 16, 13, 15]  neighbor site (-4, 6, -3)
facet 6-gon [10, 11, 12, 13, 16, 14]  neighbor site (4, 0, -3)
facet 3-gon [3, 2, 1]  neighbor site (-7, 0, -3)
facet 3-gon [17, 18, 20]  neighbor site (-3, 7, -6)
facet 3-gon [12, 11, 9]  neighbor site (3, -1, -6)
facet 3-gon [26, 27, 28]  neighbor site (7, 6, -3)
facet 4-gon [2, 3, 4, 5]  neighbor site (-6, -3, -4)
facet 4-gon [27, 26, 25, 24]  neighbor site (6, 9, -4)
facet 5-gon [6, 9, 11, 10, 8]  neighbor site (0, -3, -7)
facet 5-gon [23, 20, 18, 19, 21]  neighbor site (0, 9, -7)
facet 4-gon [5, 4, 6, 8]  neighbor site (-3, -4, -6)
facet 4-gon [24, 25, 23, 21]  neighbor site (3, 10, -6)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** full isometry group order 2 (= site), aut 2 with 0 reversing elements; type OPEN on the 24f line but on a short interval (survives +-1/192, not +1/96 toward larger z).
