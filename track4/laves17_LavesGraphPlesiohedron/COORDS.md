# Laves graph plesiohedron — exact generating data and coordinates

The cell is the well-known 17-faced plesiohedron of the Laves graph (Coxeter 1955; Schoen 2008); it is not new. Only the polyform sequences are new here.

All numbers recomputed by `track4/track4_certify.py` (frozen G1 `spacegroups.json`, exact-Fraction pipeline; certificates in `track4/TRACK4_CERT_LOG.md`).

## Generating data

- Space group: IT(214) = I4_132 (single-origin group)
- Generating point (fractional): (1/8, 1/8, 1/8) — site-symmetry order 6, Wyckoff stratum dimension 0
- Orbit: 8 points per conventional cell, T = 4 translation classes (primitive)
- Integer scaling: PERIOD = 24
- Primitive lattice basis (columns, integer): [[12, 12, 12], [0, 0, 24], [0, 24, 0]] with |det| = 6912
- Exact cell volume: 1728 (T x vol = detL certified)

## Combinatorics and symmetry

- f-vector (V, E, F): (30, 45, 17)
- p-vector: 4^6 5^6 6^2 8^3
- Combinatorial automorphism order: 12
- Site symmetry order: 6; geometric stabilizer order: 6 (over ALL orthogonal maps)
- Honeycomb point ops mod lattice: |ops| = 24 (24 proper, 0 improper) — CHIRAL honeycomb (all ops proper): one-sided == free
- Bravais point group of the actual lattice: order 48
- Non-simple vertices: 0 (flagged per design; not an error)

## Scaled generating orbit (integer, mod 24)

```
(3, 3, 3)
(3, 21, 9)
(9, 3, 21)
(9, 21, 15)
(15, 9, 21)
(15, 15, 15)
(21, 9, 3)
(21, 15, 9)
```

## Exact vertex coordinates of one cell (site (3, 3, 3), same scaling)

30 vertices, then the 17 facet cycles (CCW from outside) with neighbor sites.

```
v0: (-7, -1, 3)
v1: (-6, -3, 0)
v2: (-6, 0, 0)
v3: (-6, 0, 6)
v4: (-5, -1, -3)
v5: (-3, -5, -1)
v6: (-3, 0, -6)
v7: (-1, -3, -5)
v8: (-1, 3, -7)
v9: (0, -6, -3)
v10: (0, -6, 0)
v11: (0, 0, -6)
v12: (0, 6, -6)
v13: (0, 6, 12)
v14: (3, -7, -1)
v15: (3, 7, 13)
v16: (6, -6, 0)
v17: (6, 6, 12)
v18: (6, 9, 12)
v19: (6, 12, 0)
v20: (6, 12, 6)
v21: (7, 11, 9)
v22: (7, 13, 3)
v23: (9, 7, 11)
v24: (9, 12, 6)
v25: (11, 9, 7)
v26: (12, 0, 6)
v27: (12, 6, 6)
v28: (12, 6, 9)
v29: (13, 3, 7)

facet 8-gon [12, 2, 0, 3, 13, 20, 22, 19]  neighbor site (-3, 9, 3)
facet 8-gon [10, 14, 16, 26, 17, 15, 13, 3]  neighbor site (3, -3, 9)
facet 8-gon [19, 27, 29, 26, 16, 11, 8, 12]  neighbor site (9, 3, -3)
facet 5-gon [8, 6, 4, 2, 12]  neighbor site (-9, 9, -3)
facet 5-gon [3, 0, 1, 5, 10]  neighbor site (-3, -9, 9)
facet 5-gon [15, 18, 21, 20, 13]  neighbor site (-3, 15, 9)
facet 5-gon [16, 14, 9, 7, 11]  neighbor site (9, -3, -9)
facet 5-gon [29, 28, 23, 17, 26]  neighbor site (9, -3, 15)
facet 5-gon [19, 22, 24, 25, 27]  neighbor site (15, 9, -3)
facet 4-gon [4, 1, 0, 2]  neighbor site (-15, 3, -3)
facet 4-gon [5, 9, 14, 10]  neighbor site (-3, -15, 3)
facet 4-gon [8, 11, 7, 6]  neighbor site (3, -3, -15)
facet 4-gon [21, 24, 22, 20]  neighbor site (3, 21, 9)
facet 4-gon [15, 17, 23, 18]  neighbor site (9, 3, 21)
facet 4-gon [29, 27, 25, 28]  neighbor site (21, 9, 3)
facet 6-gon [7, 9, 5, 1, 4, 6]  neighbor site (-9, -9, -9)
facet 6-gon [23, 28, 25, 24, 21, 18]  neighbor site (15, 15, 15)
```
