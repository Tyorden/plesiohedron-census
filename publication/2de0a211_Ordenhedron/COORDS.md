# Ordenhedron — exact generating data and coordinates

Type id `2de0a21129cabe90` · status: **PUBLISHABLE-NOW** · the IT(201) Pn-3 fully asymmetric cell.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_2de0a21129cabe90.json`.

## Generating data

- Space group: IT(201) = Pn-3 (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (1/8, 1/6, 5/12) — general position (trivial site symmetry)
- Orbit: 24 points per conventional cell, T = 24 translation classes (primitive)
- Integer scaling: PERIOD = 24 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-24, 0, 0], [0, -24, 0], [0, 0, -24]] with |det| = 13824
- Exact cell volume: 576 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (20, 33, 15)
- p-vector: 3^6 4^3 5^2 6^2 7^2
- Combinatorial automorphism order: 1 (canonical code)
- Site symmetry order: 1; geometric stabilizer order: 1 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 24 (12 proper, 12 improper)
- Chirality status: fully asymmetric: site symmetry = geometric stabilizer = combinatorial aut = 1 (trivial); the cell has NO symmetry of its own yet tiles under |ops|=24
- Non-simple vertices: 5 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 24)

```
(2, 9, 8)
(2, 15, 16)
(3, 4, 10)
(3, 20, 14)
(4, 10, 3)
(4, 14, 21)
(8, 2, 9)
(8, 22, 15)
(9, 8, 2)
(9, 16, 22)
(10, 3, 4)
(10, 21, 20)
(14, 3, 20)
(14, 21, 4)
(15, 8, 22)
(15, 16, 2)
(16, 2, 15)
(16, 22, 9)
(20, 10, 21)
(20, 14, 3)
(21, 4, 14)
(21, 20, 10)
(22, 9, 16)
(22, 15, 8)
```

## Exact vertex coordinates of one cell (site (2, 9, 8), same integer scaling)

20 vertices (exact Fractions), followed by the 15 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-6, 6, 6)
v1: (-1008/173, 1404/173, 1368/173)
v2: (-9/2, 9, 39/4)
v3: (-708/173, 1068/173, 672/173)
v4: (-672/173, 708/173, 1068/173)
v5: (-3, 3, 3)
v6: (-9/4, 15/2, 3)
v7: (-216/125, 372/125, 288/125)
v8: (0, 36/5, 12)
v9: (0, 12, 24/5)
v10: (0, 12, 12)
v11: (9/2, 9, 57/4)
v12: (9/2, 15, 39/4)
v13: (1008/173, 2748/173, 1368/173)
v14: (6, 6, 6)
v15: (9, 15, 9)
v16: (1128/125, 1212/125, 1716/125)
v17: (1128/125, 1788/125, 1284/125)
v18: (1212/125, 1716/125, 1128/125)
v19: (12, 12, 12)

facet 7-gon [4, 5, 7, 14, 16, 11, 8]  neighbor site (3, 4, 10)
facet 7-gon [13, 15, 18, 14, 7, 6, 9]  neighbor site (4, 10, 3)
facet 6-gon [9, 1, 2, 10, 12, 13]  neighbor site (-2, 15, 8)
facet 4-gon [11, 10, 2, 8]  neighbor site (-2, 9, 16)
facet 5-gon [6, 3, 0, 1, 9]  neighbor site (-4, 14, 3)
facet 5-gon [8, 2, 1, 0, 4]  neighbor site (-3, 4, 14)
facet 3-gon [19, 16, 14]  neighbor site (8, 2, 9)
facet 3-gon [18, 19, 14]  neighbor site (9, 8, 2)
facet 6-gon [19, 17, 12, 10, 11, 16]  neighbor site (2, 15, 16)
facet 4-gon [6, 7, 5, 3]  neighbor site (-4, 10, -3)
facet 4-gon [13, 12, 17, 15]  neighbor site (3, 20, 14)
facet 3-gon [5, 0, 3]  neighbor site (-9, 8, -2)
facet 3-gon [0, 5, 4]  neighbor site (-8, -2, 9)
facet 3-gon [17, 19, 15]  neighbor site (8, 22, 15)
facet 3-gon [18, 15, 19]  neighbor site (15, 16, 2)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** isometry group trivial (centre-free check); type OPEN under +-1/96, +-1/48 in all three coordinates; the five non-simple vertices lie on symmetry elements of Pn-3.
