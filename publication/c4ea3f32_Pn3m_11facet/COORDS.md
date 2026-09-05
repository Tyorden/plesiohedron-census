# the Pn-3m 11-facet cell — exact generating data and coordinates

Type id `c4ea3f32fdd6dc51` · status: **PUBLISHABLE-NOW (name pending Tyler)** · descriptive name pending Tyler's choice.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_c4ea3f32fdd6dc51.json`.

## Generating data

- Space group: IT(224) = Pn-3m (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (1/12, 3/8, 3/8) — special position (Wyckoff stratum dimension 2, site-symmetry order 2)
- Orbit: 24 points per conventional cell, T = 24 translation classes (primitive)
- Integer scaling: PERIOD = 24 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-24, 0, 0], [0, -24, 0], [0, 0, -24]] with |det| = 13824
- Exact cell volume: 576 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (14, 23, 11)
- p-vector: 3^4 4^4 6^3
- Combinatorial automorphism order: 2 (canonical code)
- Site symmetry order: 2; geometric stabilizer order: 2 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 48 (24 proper, 24 improper)
- Chirality status: site = stab_geo = aut = 2; achiral honeycomb (24 improper ops)
- Non-simple vertices: 4 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 24)

```
(2, 9, 9)
(2, 15, 15)
(3, 3, 10)
(3, 10, 3)
(3, 14, 21)
(3, 21, 14)
(9, 2, 9)
(9, 9, 2)
(9, 15, 22)
(9, 22, 15)
(10, 3, 3)
(10, 21, 21)
(14, 3, 21)
(14, 21, 3)
(15, 2, 15)
(15, 9, 22)
(15, 15, 2)
(15, 22, 9)
(21, 3, 14)
(21, 10, 21)
(21, 14, 3)
(21, 21, 10)
(22, 9, 15)
(22, 15, 9)
```

## Exact vertex coordinates of one cell (site (2, 9, 9), same integer scaling)

14 vertices (exact Fractions), followed by the 11 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-108/17, 132/17, 132/17)
v1: (-6, 6, 6)
v2: (-72/17, 72/17, 96/17)
v3: (-72/17, 96/17, 72/17)
v4: (-4, 4, 4)
v5: (0, 6, 12)
v6: (0, 12, 6)
v7: (0, 12, 12)
v8: (6, 6, 6)
v9: (108/17, 132/17, 276/17)
v10: (108/17, 276/17, 132/17)
v11: (8, 8, 16)
v12: (8, 16, 8)
v13: (12, 12, 12)

facet 6-gon [11, 9, 5, 2, 4, 8]  neighbor site (3, 3, 10)
facet 6-gon [8, 4, 3, 6, 10, 12]  neighbor site (3, 10, 3)
facet 4-gon [9, 7, 0, 5]  neighbor site (-2, 9, 15)
facet 4-gon [6, 0, 7, 10]  neighbor site (-2, 15, 9)
facet 6-gon [11, 13, 12, 10, 7, 9]  neighbor site (2, 15, 15)
facet 4-gon [5, 0, 1, 2]  neighbor site (-3, 3, 14)
facet 4-gon [0, 6, 3, 1]  neighbor site (-3, 14, 3)
facet 3-gon [11, 8, 13]  neighbor site (9, 2, 9)
facet 3-gon [8, 12, 13]  neighbor site (9, 9, 2)
facet 3-gon [1, 4, 2]  neighbor site (-9, -2, 9)
facet 3-gon [3, 4, 1]  neighbor site (-9, 9, -2)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** full isometry group order 2 (the site mirror, improper): achiral solid; type OPEN in the 2-dof stratum 24k.
