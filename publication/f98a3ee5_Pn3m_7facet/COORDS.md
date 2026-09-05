# the Pn-3m 7-facet cell — exact generating data and coordinates

Type id `f98a3ee5675fc121` · status: **PUBLISHABLE-NOW (name pending Tyler)** · descriptive name pending Tyler's choice.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_f98a3ee5675fc121.json`.

## Generating data

- Space group: IT(224) = Pn-3m (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (1/8, 1/6, 5/12) — general position (trivial site symmetry)
- Orbit: 48 points per conventional cell, T = 48 translation classes (primitive)
- Integer scaling: PERIOD = 24 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-24, 0, 0], [0, -24, 0], [0, 0, -24]] with |det| = 13824
- Exact cell volume: 288 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (10, 15, 7)
- p-vector: 3^2 4^3 6^2
- Combinatorial automorphism order: 4 (canonical code)
- Site symmetry order: 1; geometric stabilizer order: 1 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 48 (24 proper, 24 improper)
- Chirality status: site = stab_geo = 1 < aut = 4 — combinatorial-vs-geometric symmetry gap (G4/V2); achiral honeycomb
- Non-simple vertices: 0 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 24)

```
(2, 8, 9)
(2, 9, 8)
(2, 15, 16)
(2, 16, 15)
(3, 4, 10)
(3, 10, 4)
(3, 14, 20)
(3, 20, 14)
(4, 3, 10)
(4, 10, 3)
(4, 14, 21)
(4, 21, 14)
(8, 2, 9)
(8, 9, 2)
(8, 15, 22)
(8, 22, 15)
(9, 2, 8)
(9, 8, 2)
(9, 16, 22)
(9, 22, 16)
(10, 3, 4)
(10, 4, 3)
(10, 20, 21)
(10, 21, 20)
(14, 3, 20)
(14, 4, 21)
(14, 20, 3)
(14, 21, 4)
(15, 2, 16)
(15, 8, 22)
(15, 16, 2)
(15, 22, 8)
(16, 2, 15)
(16, 9, 22)
(16, 15, 2)
(16, 22, 9)
(20, 3, 14)
(20, 10, 21)
(20, 14, 3)
(20, 21, 10)
(21, 4, 14)
(21, 10, 20)
(21, 14, 4)
(21, 20, 10)
(22, 8, 15)
(22, 9, 16)
(22, 15, 8)
(22, 16, 9)
```

## Exact vertex coordinates of one cell (site (2, 8, 9), same integer scaling)

10 vertices (exact Fractions), followed by the 7 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-6, 6, 6)
v1: (-72/13, 108/13, 108/13)
v2: (-48/13, 48/13, 84/13)
v3: (-3, 3, 3)
v4: (0, 6, 12)
v5: (0, 12, 12)
v6: (72/13, 108/13, 204/13)
v7: (6, 6, 6)
v8: (9, 9, 15)
v9: (12, 12, 12)

facet 6-gon [5, 9, 7, 3, 0, 1]  neighbor site (2, 9, 8)
facet 6-gon [2, 3, 7, 8, 6, 4]  neighbor site (3, 4, 10)
facet 4-gon [1, 4, 6, 5]  neighbor site (-2, 8, 15)
facet 4-gon [0, 2, 4, 1]  neighbor site (-3, 4, 14)
facet 3-gon [9, 8, 7]  neighbor site (8, 2, 9)
facet 4-gon [5, 6, 8, 9]  neighbor site (2, 15, 16)
facet 3-gon [3, 2, 0]  neighbor site (-8, -2, 9)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** isometry group trivial (centre-free check): none of the 4 map automorphisms (2 reversing) preserves the vertex distances; type OPEN in general position.
