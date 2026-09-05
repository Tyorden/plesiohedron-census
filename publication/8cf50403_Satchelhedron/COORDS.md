# Satchelhedron — exact generating data and coordinates

Type id `8cf50403cf88c455` · status: **PUBLISHABLE-NOW** · the IT(220) I-43d pentagon-dominant 11-facet cell.

All numbers below are recomputed from the banked witness (`harness/phase1_types.json`) through the G0/G2-validated exact pipeline at build time and asserted against the stored canonical code, f-vector, p-vector and aut order; certificate values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and the banked `g4_tables_8cf50403cf88c455.json`.

## Generating data

- Space group: IT(220) = I-43d (frozen G1 `spacegroups.json`, origin choice 1 for two-origin groups)
- Generating point (fractional): (0, 0, 1/4) — special position (Wyckoff stratum dimension 1, site-symmetry order 2)
- Orbit: 24 points per conventional cell, T = 12 translation classes (primitive)
- Integer scaling: PERIOD = 12 (orbit cleared to integer triples mod PERIOD)
- Primitive lattice basis (columns, integer, from banked tables): [[-6, -6, -6], [-6, -6, 6], [-6, 6, -6]] with |det| = 864
- Exact cell volume: 72 (T x vol = detL certified in G4/V1)

## Combinatorics and symmetry

- f-vector (V, E, F): (16, 25, 11)
- p-vector: 3^2 4^1 5^8
- Combinatorial automorphism order: 4 (canonical code)
- Site symmetry order: 2; geometric stabilizer order: 2 (over ALL orthogonal maps, G4/V2)
- Honeycomb point ops mod lattice: |ops| = 24 (12 proper, 12 improper)
- Chirality status: amphichiral as a combinatorial map (aut 4, 2 improper map symmetries) but geometric stabilizer order 2 — a combinatorial-vs-geometric symmetry gap (G4/V2)
- Non-simple vertices: 2 (flagged per design; not an error)

## Certification (banked, accepted)

G4 ladder V0–V3 ALL PASS in exact rational arithmetic (`harness/G4_RESULTS.md`): exact re-derivation; tiling certificate (full-facet 1:1 pairing of all T*F slots, T x vol = detL, exhaustive 2rho-ball disjointness) verified twice — generator + an independent adapted audit sharing no geometry code; symmetry over all orthogonal maps; Burnside identity on the polyform counts (n <= 4). free(1) = 1: the ops act transitively on the T cell types (plesiohedral quotient).

Diligence status: not matched against the records checked as of 2026-09-01 (Schmitt 2016 printed cubic tables incl. exact recomputation at every printed representative point, Bernhard 2026 printed cell data, classical space-filler lists). Survival of every printed representative is evidence, not proof of novelty (Schmitt's survey is a grid sampling printing one representative per (group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and `G5_DILIGENCE_2026-08-30.md`.

## Scaled generating orbit (integer, mod 12)

```
(0, 0, 3)
(0, 3, 0)
(0, 3, 9)
(0, 6, 3)
(0, 9, 6)
(0, 9, 9)
(3, 0, 0)
(3, 0, 6)
(3, 3, 6)
(3, 6, 3)
(3, 6, 9)
(3, 9, 0)
(6, 0, 9)
(6, 3, 0)
(6, 3, 3)
(6, 6, 9)
(6, 9, 3)
(6, 9, 6)
(9, 0, 3)
(9, 0, 9)
(9, 3, 6)
(9, 6, 0)
(9, 6, 6)
(9, 9, 0)
```

## Exact vertex coordinates of one cell (site (0, 0, 3), same integer scaling)

16 vertices (exact Fractions), followed by the 11 facet cycles (vertex indices, CCW from outside) and each facet's neighbor site.

```
v0: (-3/2, -3, 3)
v1: (-3/2, 0, 0)
v2: (-3/2, 0, 6)
v3: (-3/2, 3, 3)
v4: (-1/2, -1/2, -1/2)
v5: (-1/2, 1/2, 13/2)
v6: (0, -3, 3/2)
v7: (0, -3/2, 0)
v8: (0, 3/2, 6)
v9: (0, 3, 9/2)
v10: (3/2, -3, 3)
v11: (3/2, 3, 3)
v12: (5/2, -5/2, 7/2)
v13: (5/2, 5/2, 5/2)
v14: (3, -3/2, 3)
v15: (3, 3/2, 3)

facet 4-gon [0, 2, 3, 1]  neighbor site (-3, 0, 3)
facet 5-gon [5, 2, 0, 10, 12]  neighbor site (0, -3, 6)
facet 5-gon [3, 11, 13, 4, 1]  neighbor site (0, 3, 0)
facet 5-gon [13, 15, 14, 7, 4]  neighbor site (3, 0, 0)
facet 5-gon [5, 12, 14, 15, 8]  neighbor site (3, 0, 6)
facet 5-gon [1, 4, 7, 6, 0]  neighbor site (-3, -3, 0)
facet 5-gon [9, 3, 2, 5, 8]  neighbor site (-3, 3, 6)
facet 5-gon [12, 10, 6, 7, 14]  neighbor site (3, -3, 0)
facet 5-gon [11, 9, 8, 15, 13]  neighbor site (3, 3, 6)
facet 3-gon [0, 6, 10]  neighbor site (0, -6, 3)
facet 3-gon [9, 11, 3]  neighbor site (0, 6, 3)
```



**Update 2026-09-03 (round-1 C1/C2, harness/round1_computations/RESULTS.md):** full isometry group order 2 (= site), no improper isometry: chiral solid; 6 + 6 translation classes of the two hands. Type is a WALL on the 24d line (x,0,1/4): both neighbours are (22,35,15) types (3^4 5^10 8^1 for x<0, stored 0ee26ed471c923e2; 3^6 4^1 6^8 for 0<x<1/12, not stored), and (22,35,15) is printed in Schmitt's IT(220) table.
