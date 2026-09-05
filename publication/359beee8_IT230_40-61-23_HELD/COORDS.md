# the IT(230) (40,61,23) cell — exact generating data and coordinates

Type id `359beee832567a71` · status: **HELD (Engel/Koch ILL check)** · mined-group finalist; NOT to be named before the ILL check.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_359beee832567a71.json`.

## Generating data

- Space group: IT(230) = Ia-3d (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (1/12, 1/6, 1/8) — special position (Wyckoff stratum dimension 1, site-symmetry order 2)
- Orbit: 48 points per conventional cell, T = 24 translation classes (primitive)
- Integer scaling: PERIOD = 24 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-12, -12, -12], [-12, -12, 12], [-12, 12, -12]] with |det| = 6912
- Exact cell volume: 288 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (40, 61, 23)
- p-vector: 4^20 11^2 20^1
- Combinatorial automorphism order: 4 (canonical code)
- Site symmetry order: 2; geometric stabilizer order: 2 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 48 (24 proper, 24 improper)
- Chirality status: site = stab_geo = 2 < aut = 4 — combinatorial-vs-geometric symmetry gap (G4/V2); p-vector carries two 11-gons and a 20-gon
- Non-simple vertices: 2 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 24)

```
(2, 4, 3)
(2, 8, 15)
(2, 16, 21)
(2, 20, 9)
(3, 2, 4)
(3, 10, 16)
(3, 14, 20)
(3, 22, 8)
(4, 3, 2)
(4, 9, 14)
(4, 15, 22)
(4, 21, 10)
(8, 3, 22)
(8, 9, 10)
(8, 15, 2)
(8, 21, 14)
(9, 2, 20)
(9, 10, 8)
(9, 14, 4)
(9, 22, 16)
(10, 4, 21)
(10, 8, 9)
(10, 16, 3)
(10, 20, 15)
(14, 4, 9)
(14, 8, 21)
(14, 16, 15)
(14, 20, 3)
(15, 2, 8)
(15, 10, 20)
(15, 14, 16)
(15, 22, 4)
(16, 3, 10)
(16, 9, 22)
(16, 15, 14)
(16, 21, 2)
(20, 3, 14)
(20, 9, 2)
(20, 15, 10)
(20, 21, 22)
(21, 2, 16)
(21, 10, 4)
(21, 14, 8)
(21, 22, 20)
(22, 4, 15)
(22, 8, 3)
(22, 16, 9)
(22, 20, 21)
```

## Exact vertex coordinates of one cell (site (2, 4, 3), same integer scaling)

40 vertices (exact Fractions), followed by the 23 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-69/17, 33/17, 3)
v1: (-4, 2, 2)
v2: (-4, 2, 4)
v3: (-33/10, 9/10, 51/10)
v4: (-19/6, 1/2, 25/6)
v5: (-19/6, 17/6, -1/6)
v6: (-19/6, 17/6, 37/6)
v7: (-17/6, 1/6, 19/6)
v8: (-17/6, 11/6, 13/2)
v9: (-2, 4, -2)
v10: (-2, 4, 8)
v11: (-33/17, 3, 135/17)
v12: (-9/10, 51/10, -27/10)
v13: (-9/10, 51/10, 87/10)
v14: (-1/2, 25/6, 53/6)
v15: (0, 0, 0)
v16: (0, 6, -3)
v17: (0, 6, 9)
v18: (1/6, 19/6, -17/6)
v19: (1/2, 25/6, -19/6)
v20: (9/10, 51/10, -33/10)
v21: (9/10, 51/10, 93/10)
v22: (9/10, 69/10, -27/10)
v23: (9/10, 69/10, 87/10)
v24: (11/6, 11/2, 55/6)
v25: (11/6, 13/2, -17/6)
v26: (2, 8, -2)
v27: (2, 8, 8)
v28: (17/6, 35/6, 53/6)
v29: (3, 135/17, -33/17)
v30: (19/6, 55/6, -1/6)
v31: (19/6, 55/6, 37/6)
v32: (4, 10, 2)
v33: (4, 10, 4)
v34: (69/17, 171/17, 3)
v35: (25/6, 53/6, -1/2)
v36: (51/10, 93/10, 9/10)
v37: (11/2, 55/6, 11/6)
v38: (35/6, 53/6, 17/6)
v39: (6, 6, 6)

facet 11-gon [7, 15, 39, 28, 24, 21, 14, 11, 8, 3, 4]  neighbor site (3, 2, 4)
facet 11-gon [19, 20, 25, 29, 35, 36, 37, 38, 39, 15, 18]  neighbor site (4, 3, 2)
facet 20-gon [1, 0, 2, 6, 10, 13, 17, 23, 27, 31, 33, 34, 32, 30, 26, 22, 16, 12, 9, 5]  neighbor site (-2, 8, 3)
facet 4-gon [7, 1, 5, 15]  neighbor site (-4, -3, -2)
facet 4-gon [15, 5, 9, 18]  neighbor site (-3, -2, -4)
facet 4-gon [39, 31, 27, 28]  neighbor site (8, 9, 10)
facet 4-gon [38, 33, 31, 39]  neighbor site (9, 10, 8)
facet 4-gon [8, 6, 2, 3]  neighbor site (-9, 2, 8)
facet 4-gon [4, 0, 1, 7]  neighbor site (-8, -3, 2)
facet 4-gon [11, 10, 6, 8]  neighbor site (-8, 3, 10)
facet 4-gon [18, 9, 12, 19]  neighbor site (-3, 2, -8)
facet 4-gon [29, 26, 30, 35]  neighbor site (3, 14, -4)
facet 4-gon [28, 27, 23, 24]  neighbor site (4, 9, 14)
facet 4-gon [35, 30, 32, 36]  neighbor site (4, 15, -2)
facet 4-gon [37, 34, 33, 38]  neighbor site (9, 14, 4)
facet 4-gon [3, 2, 0, 4]  neighbor site (-9, -2, 4)
facet 4-gon [14, 13, 10, 11]  neighbor site (-4, 3, 14)
facet 4-gon [25, 22, 26, 29]  neighbor site (3, 10, -8)
facet 4-gon [36, 32, 34, 37]  neighbor site (8, 15, 2)
facet 4-gon [19, 12, 16, 20]  neighbor site (-2, 4, -9)
facet 4-gon [21, 17, 13, 14]  neighbor site (-2, 4, 15)
facet 4-gon [20, 16, 22, 25]  neighbor site (2, 8, -9)
facet 4-gon [24, 23, 17, 21]  neighbor site (2, 8, 15)
```



**Update 2026-09-03 (round-1 C2, harness/round1_computations/RESULTS.md):** the combinatorial automorphism group (order 4) contains 2 orientation-reversing elements; the full isometry group of the solid, computed centre-free (all pairwise vertex distances), has order 2 (one proper two-fold rotation, fixing the site), equal to the site symmetry. The cell is amphichiral as a map and chiral as a solid; the honeycomb's 24 improper operations carry it to its mirror image, 12 translation classes of each hand. Type is OPEN on the 48g line (unchanged under +-1/96, +-1/48 along the tangent direction (-1,1,0)).
