# Phase-2 pool ranking — staging for flagship choice (2026-09-04)

Staging only. Naming is Tyler's alone; this document proposes NO names. Every cell
below is a certified space-filler (G4 ladder V0-V3, twice-derived) whose computed
open/wall verdict is OPEN (harness/phase2/WALL_OPEN_PHASE2.json, md5
6b257c551f6fb275dfabb03e992f57c2, accepted 2026-09-04 14:10). Novelty wording,
everywhere: "not matched against the records checked as of 2026-09-04" — never
"new". AI disclosure: computed and written by a Claude subagent (#149) on
2026-09-04; provisional until the main session re-runs the verify command at the end.

<!-- PREREG-BEGIN -->
## Pre-registered scoring (written 2026-09-04 13:41 PDT, BEFORE any feature was computed)

Pool = every cell with COMBINED verdict OPEN in WALL_OPEN_PHASE2.json: 13 tetragonal
+ 102 hexagonal-family = 115. Systems for the per-system lists: tetragonal (IT 75-142),
trigonal (IT 143-167), hexagonal (IT 168-194).

Score = F + P + A + C + R + I + D + E + S, with:

| term | feature | rule (fixed before computing) |
|---|---|---|
| F | facet count | F = f2 / 4 |
| P | polygon richness | P = (number of distinct polygon sizes) + min(#pentagons, 8)/2 + min(#odd polygons of size >= 7, 4) |
| A | symmetry | A = 1.5 * log2(aut_comb) + 1 if Isom(solid) = aut_comb (every combinatorial symmetry realized by an isometry), else no bonus |
| C | chirality | C = 1.5 if the solid is chiral (Isom(solid) contains no improper element) + 0.5 more if the space group is one of the 11 enantiomorphic pairs (76/78, 91/95, 92/96, 144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181, 212/213) |
| R | roundness | R = 10 * roundness_site / 47.9833 (Bernhard's Josehedron control through the same pipeline, publication/ROUNDNESS.md); site-centred convention is the scored one, minimal-enclosing-sphere value reported alongside, not scored |
| I | presentation | I = 2 if the minimal integer scale m <= 24; 1 if m <= 96; else 0. Tetragonal: m = least m with m*x, m*y and m*(p/q)*z integers for every site-centred vertex vector (x,y,z) in conventional fractional coordinates, c/a = p/q — i.e. integer CARTESIAN coordinates in units a/m. Hexagonal family: an integer Cartesian presentation does not exist in general (the 120-degree a-b angle puts sqrt(3) into the y coordinate), so m = least common denominator of the site-centred vertex vectors in the hexagonal LATTICE basis (a, b, c): integer coordinates in that basis after scaling; the JSON records which definition applies |
| D | stratum | D = 3 - stratum_dim (fixed Wyckoff point 3, line 2, plane 1, general position 0) |
| E | Engel/Koch exposure | E = -2 if the cell's group is one G5_DILIGENCE_2026-08-30.md records as mined by Engel 1981 / Koch 1972; 0 if UNKNOWN. G5 records only cubic groups (212/213, 214, 220, 230). For tetragonal, trigonal and hexagonal groups the exposure is UNKNOWN pending the ILL, so E = 0 for all 115 today and the term cannot discriminate; it is pre-registered so it can be re-applied once the ILL arrives |
| S | story flags | +2 record facet count within the cell's family pool (tetragonal pool / hexagonal-family pool; ties share); +2 fully asymmetric (aut_comb = 1); +1 f-vector absent from the printed Schmitt table of its own group (tiebreaker only — per the 2026-09-04 14:45 ledger note, absence follows the open verdict and never replaces it); +1 symmetry fully forced by the group (site symmetry = Isom(solid) = aut_comb). The brief's "Josehedron's own group" flag is cubic (IT 220) and cannot fire in this pool |

Ties: broken by roundness_site (desc), then f2 (desc), then id (ascending, lexicographic).

Certificate facts (f, p, aut, site, Isom(solid), Isom+, improper, chirality, c/a, stratum
dim) are read from G4_PHASE2_RESULTS.md / G4_PHASE2_HEX_RESULTS.md and
WALL_OPEN_PHASE2.json; Isom(solid) is independently re-derived here by the Gram-triple
stabilizer (g4_certify_gram.cell_stabilizer_gram) and must agree. Roundness uses the
exact cell re-derived through the accepted chain (g4_certify_gram.v0_rederive, which
asserts the canonical code against the store): volume exact in the crystal basis,
Euclidean volume = that * sqrt(det G), radius^2 = rho^2 of the certificate (the
G-norm distance from the site to its farthest vertex = the site-centred outer
circumsphere, the definition ROUNDNESS.md uses); one float division per percentage.
The minimal enclosing sphere is computed exactly (Welzl in the G inner product,
verified by containment + support; cross-checked against the c4 brute-force method of
round1_computations/c4_roundness.py on every cell with at most 30 vertices).

What the score does NOT capture: what the cell looks like (no renders were made);
behaviour at the type's other sightings (the open verdict is at one witness);
recurrence of the type across groups; edge-length and aspect extremes (thin slivers
score like fat cells); the size of the open neighbourhood (OPEN = holds on the tested
neighbourhood, never an interval proof); whether a simpler presentation exists at
another origin choice or c/a; personal taste. F and P are correlated (heavier cells
carry more polygon kinds) — deliberate, both are tellable. The weights are judgment
calls fixed here; every raw feature is in the JSON so any re-weighting is a one-line
change and a re-run.
<!-- PREREG-END -->

## Inputs and checks

- Pool: 115 cells = 51 hexagonal, 13 tetragonal, 51 trigonal (WALL_OPEN_PHASE2.json md5 6b257c551f6fb275dfabb03e992f57c2; stores sha256 unchanged: True).
- Every cell re-derived through the accepted chain (v0_rederive asserts canonical code, f, p, aut against the frozen store); Isom(solid), Isom+, improper, chirality, site symmetry and aut cross-checked against G4_PHASE2_RESULTS.md / G4_PHASE2_HEX_RESULTS.md (all 115 agree); f, p, aut, c/a, stratum dim, witness point cross-checked against WALL_OPEN_PHASE2.json (all agree); the own-group printed-f flag agrees with the wall/open store for all 115.
- Minimal enclosing sphere cross-checked against the c4 brute force on 45 cells (all with <= 30 vertices): identical.
- Roundness: site-centred outer circumsphere (radius^2 = rho^2 of the certificate, the ROUNDNESS.md definition), scored; MES value reported, not scored. Benchmark 47.9833% (Josehedron control).
- Engel/Koch exposure: UNKNOWN for every cell in this pool (both catalogs are print-only, unread for the tetragonal/trigonal/hexagonal systems; ILL pending); E = 0 throughout, so it does not move the ranking today.
- Output JSON: harness/phase2/POOL_RANKING_2026-09-04.json (sorted keys, no timings), md5 in the ledger line / STATUS entry.

## Top 5 per system

### Tetragonal (IT 75-142), top 5 of 13

| rank | id | group | c/a | f | p | aut / Isom | chiral | stratum | roundness site / MES | presentation | exposure | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | IT(92) P4_12_12 | 5/4 | (40,60,22) | 3^8 4^4 5^4 8^2 11^4 | 2 / 2 | yes | 1 | 35.78% / 35.78% | m=7608384 (Cartesian) | UNKNOWN (ILL) | 31.46 |
| 2 | `164d4bd63d82d0c3` | IT(76) P4_1 | 5/4 | (40,60,22) | 3^6 4^6 5^2 6^4 11^4 | 1 / 1 | yes | 3 | 30.22% / 30.22% | m=1451520 (Cartesian) | UNKNOWN (ILL) | 27.80 |
| 3 | `6797ab70c6015039` | IT(76) P4_1 | 3/2 | (32,48,18) | 3^4 4^4 5^4 6^2 9^4 | 2 / 1 | yes | 3 | 31.54% / 31.63% | m=155520 (Cartesian) | UNKNOWN (ILL) | 25.57 |
| 4 | `213c7a114d5a97a8` | IT(98) I4_122 | 11/16 | (42,63,23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 / 1 | yes | 3 | 15.44% / 16.61% | m=448061644800 (Cartesian) | UNKNOWN (ILL) | 25.47 |
| 5 | `4f6d3e68cbd9e729` | IT(98) I4_122 | 3/4 | (42,63,23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 / 1 | yes | 3 | 16.20% / 17.23% | m=7637414400 (Cartesian) | UNKNOWN (ILL) | 24.63 |

- **#1 `4e9c9b076cfec323`** — 22-faced cell (8 triangles, 4 quadrilaterals, 4 pentagons, 2 octagons, 4 11-gons); symmetry order 2 (all of it realized by isometries); chiral (comes in two mirror-image hands); sits on a symmetry line; roundness 35.78% of its circumsphere (75% of the Josehedron benchmark).
  Score terms: F=5.5, P=11.0, A=2.5, C=2.0, R=7.4575, I=0, D=2, E=0, S=1; overall rank 2/115.
  A name here would attach to the fact that it is chiral and its group P4_12_12 is one of an enantiomorphic pair, so the tiling itself has a handedness; 4 of its faces are pentagons; it has 4 odd polygons of seven or more sides (largest face an 11-gon); every symmetry it has is forced by its site symmetry. Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#2 `164d4bd63d82d0c3`** — 22-faced cell (6 triangles, 6 quadrilaterals, 2 pentagons, 4 hexagons, 4 11-gons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 30.22% of its circumsphere (63% of the Josehedron benchmark).
  Score terms: F=5.5, P=10.0, A=1.0, C=2.0, R=6.2971, I=0, D=0, E=0, S=3; overall rank 11/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P4_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 4 odd polygons of seven or more sides (largest face an 11-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#3 `6797ab70c6015039`** — 18-faced cell (4 triangles, 4 quadrilaterals, 4 pentagons, 2 hexagons, 4 nonagons); symmetry order 2 combinatorially, 1 realized by isometries; chiral (comes in two mirror-image hands); sits in general position; roundness 31.54% of its circumsphere (66% of the Josehedron benchmark).
  Score terms: F=4.5, P=11.0, A=1.5, C=2.0, R=6.5732, I=0, D=0, E=0, S=0; overall rank 25/115.
  A name here would attach to the fact that it is chiral and its group P4_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; 4 of its faces are pentagons; it has 4 odd polygons of seven or more sides (largest face a 9-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#4 `213c7a114d5a97a8`** — 23-faced cell (6 triangles, 4 quadrilaterals, 4 pentagons, 5 hexagons, 2 octagons, 1 decagon, 1 16-gon); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 15.44% of its circumsphere (32% of the Josehedron benchmark).
  Score terms: F=5.75, P=9.0, A=1.0, C=1.5, R=3.2181, I=0, D=0, E=0, S=5; overall rank 26/115.
  A name here would attach to the fact that it carries the most facets (23) of any open cell in its family pool (the printed Schmitt maximum for IT(98) is 35); it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; the solid is chiral (no mirror or inversion among its isometries); 4 of its faces are pentagons. Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#5 `4f6d3e68cbd9e729`** — 23-faced cell (6 triangles, 5 quadrilaterals, 2 pentagons, 6 hexagons, 2 octagons, 1 12-gon, 1 14-gon); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 16.20% of its circumsphere (34% of the Josehedron benchmark).
  Score terms: F=5.75, P=8.0, A=1.0, C=1.5, R=3.3755, I=0, D=0, E=0, S=5; overall rank 42/115.
  A name here would attach to the fact that it carries the most facets (23) of any open cell in its family pool (the printed Schmitt maximum for IT(98) is 35); it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; the solid is chiral (no mirror or inversion among its isometries). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.

### Trigonal (IT 143-167), top 5 of 51

| rank | id | group | c/a | f | p | aut / Isom | chiral | stratum | roundness site / MES | presentation | exposure | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `a93f8fe7ecdc5851` | IT(144) P3_1 | 9/8 | (32,48,18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 / 1 | yes | 3 | 42.99% / 42.99% | m=174960 (lattice basis) | UNKNOWN (ILL) | 30.46 |
| 2 | `e598ffd8a1cac138` | IT(144) P3_1 | 29/32 | (32,48,18) | 3^4 4^4 5^4 6^2 9^4 | 1 / 1 | yes | 3 | 37.30% / 37.88% | m=3400600320 (lattice basis) | UNKNOWN (ILL) | 29.27 |
| 3 | `c0071756347c5a8a` | IT(144) P3_1 | 1 | (28,42,16) | 3^2 4^4 5^4 7^6 | 1 / 1 | yes | 3 | 43.46% / 43.48% | m=6073608960 (lattice basis) | UNKNOWN (ILL) | 29.06 |
| 4 | `466b12546dd936c3` | IT(161) R3c | 527/1000 | (26,40,16) | 3^6 5^4 6^2 7^2 8^2 | 1 / 1 | yes | 3 | 41.00% / 43.47% | m=2534879524335376023000000 (lattice basis) | UNKNOWN (ILL) | 27.04 |
| 5 | `c82ebc15c49c1413` | IT(154) P3_221 | 527/1000 | (38,57,21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 / 1 | yes | 3 | 17.65% / 24.93% | m=385324475138460000000 (lattice basis) | UNKNOWN (ILL) | 25.93 |

- **#1 `a93f8fe7ecdc5851`** — 18-faced cell (2 triangles, 8 quadrilaterals, 2 pentagons, 2 heptagons, 2 octagons, 2 nonagons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 42.99% of its circumsphere (90% of the Josehedron benchmark).
  Score terms: F=4.5, P=11.0, A=1.0, C=2.0, R=8.9602, I=0, D=0, E=0, S=3; overall rank 3/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P3_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 4 odd polygons of seven or more sides (largest face a 9-gon); it fills 43.0% of its circumsphere (rank 2 of 115 in the pool; the Josehedron benchmark is 47.98%). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#2 `e598ffd8a1cac138`** — 18-faced cell (4 triangles, 4 quadrilaterals, 4 pentagons, 2 hexagons, 4 nonagons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 37.30% of its circumsphere (78% of the Josehedron benchmark).
  Score terms: F=4.5, P=11.0, A=1.0, C=2.0, R=7.7745, I=0, D=0, E=0, S=3; overall rank 5/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P3_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; 4 of its faces are pentagons; it has 4 odd polygons of seven or more sides (largest face a 9-gon); it fills 37.3% of its circumsphere (rank 10 of 115 in the pool; the Josehedron benchmark is 47.98%). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#3 `c0071756347c5a8a`** — 16-faced cell (2 triangles, 4 quadrilaterals, 4 pentagons, 6 heptagons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 43.46% of its circumsphere (91% of the Josehedron benchmark).
  Score terms: F=4.0, P=10.0, A=1.0, C=2.0, R=9.0569, I=0, D=0, E=0, S=3; overall rank 7/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P3_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; 4 of its faces are pentagons; it has 6 odd polygons of seven or more sides (largest face a 7-gon); it fills 43.5% of its circumsphere (rank 1 of 115 in the pool; the Josehedron benchmark is 47.98%). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#4 `466b12546dd936c3`** — 16-faced cell (6 triangles, 4 pentagons, 2 hexagons, 2 heptagons, 2 octagons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 41.00% of its circumsphere (85% of the Josehedron benchmark).
  Score terms: F=4.0, P=9.0, A=1.0, C=1.5, R=8.5437, I=0, D=0, E=0, S=3; overall rank 13/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; the solid is chiral (no mirror or inversion among its isometries); 4 of its faces are pentagons; it has 2 odd polygons of seven or more sides (largest face an 8-gon); it fills 41.0% of its circumsphere (rank 5 of 115 in the pool; the Josehedron benchmark is 47.98%). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#5 `c82ebc15c49c1413`** — 21-faced cell (10 triangles, 2 quadrilaterals, 2 pentagons, 2 hexagons, 2 nonagons, 1 decagon, 1 12-gon, 1 14-gon); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 17.65% of its circumsphere (37% of the Josehedron benchmark).
  Score terms: F=5.25, P=11.0, A=1.0, C=2.0, R=3.6785, I=0, D=0, E=0, S=3; overall rank 21/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P3_221 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 2 odd polygons of seven or more sides (largest face a 14-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.

### Hexagonal (IT 168-194), top 5 of 51

| rank | id | group | c/a | f | p | aut / Isom | chiral | stratum | roundness site / MES | presentation | exposure | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | IT(178) P6_122 | 5/4 | (44,66,24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 / 2 | yes | 1 | 24.45% / 24.45% | m=415800 (lattice basis) | UNKNOWN (ILL) | 31.60 |
| 2 | `8d90c524c89922d9` | IT(169) P6_1 | 11/8 | (36,54,20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 / 1 | yes | 3 | 32.76% / 33.51% | m=1352261721498364508832 (lattice basis) | UNKNOWN (ILL) | 29.83 |
| 3 | `9c0b7e0c29dfebb2` | IT(169) P6_1 | 3/4 | (36,54,20) | 3^4 4^8 5^2 7^4 13^2 | 1 / 1 | yes | 3 | 39.39% / 41.08% | m=804980880 (lattice basis) | UNKNOWN (ILL) | 29.21 |
| 4 | `3ddc41389e6d484f` | IT(171) P6_2 | 1 | (32,48,18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 / 1 | yes | 3 | 26.45% / 27.04% | m=205530624 (lattice basis) | UNKNOWN (ILL) | 28.01 |
| 5 | `30f2a1e483babf55` | IT(178) P6_122 | 11/4 | (29,44,17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 / 1 | yes | 3 | 26.82% / 27.39% | m=31101840 (lattice basis) | UNKNOWN (ILL) | 27.84 |

- **#1 `c49077384aaebeb0`** — 24-faced cell (8 triangles, 2 quadrilaterals, 6 pentagons, 4 hexagons, 2 nonagons, 2 14-gons); symmetry order 2 (all of it realized by isometries); chiral (comes in two mirror-image hands); sits on a symmetry line; roundness 24.45% of its circumsphere (51% of the Josehedron benchmark).
  Score terms: F=6.0, P=11.0, A=2.5, C=2.0, R=5.096, I=0, D=2, E=0, S=3; overall rank 1/115.
  A name here would attach to the fact that it carries the most facets (24) of any open cell in its family pool (the printed Schmitt maximum for IT(178) is 34); it is chiral and its group P6_122 is one of an enantiomorphic pair, so the tiling itself has a handedness; 6 of its faces are pentagons; it has 2 odd polygons of seven or more sides (largest face a 14-gon); every symmetry it has is forced by its site symmetry. Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#2 `8d90c524c89922d9`** — 20-faced cell (4 triangles, 4 quadrilaterals, 4 pentagons, 4 hexagons, 2 heptagons, 2 11-gons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 32.76% of its circumsphere (68% of the Josehedron benchmark).
  Score terms: F=5.0, P=12.0, A=1.0, C=2.0, R=6.8269, I=0, D=0, E=0, S=3; overall rank 4/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P6_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; 4 of its faces are pentagons; it has 4 odd polygons of seven or more sides (largest face an 11-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#3 `9c0b7e0c29dfebb2`** — 20-faced cell (4 triangles, 8 quadrilaterals, 2 pentagons, 4 heptagons, 2 13-gons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 39.39% of its circumsphere (82% of the Josehedron benchmark).
  Score terms: F=5.0, P=10.0, A=1.0, C=2.0, R=8.2092, I=0, D=0, E=0, S=3; overall rank 6/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P6_1 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 6 odd polygons of seven or more sides (largest face a 13-gon); it fills 39.4% of its circumsphere (rank 8 of 115 in the pool; the Josehedron benchmark is 47.98%). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#4 `3ddc41389e6d484f`** — 18-faced cell (6 triangles, 2 quadrilaterals, 2 pentagons, 3 hexagons, 2 heptagons, 2 nonagons, 1 decagon); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 26.45% of its circumsphere (55% of the Josehedron benchmark).
  Score terms: F=4.5, P=12.0, A=1.0, C=2.0, R=5.5128, I=0, D=0, E=0, S=3; overall rank 8/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P6_2 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 4 odd polygons of seven or more sides (largest face a 10-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.
- **#5 `30f2a1e483babf55`** — 17-faced cell (4 triangles, 5 quadrilaterals, 2 pentagons, 1 hexagon, 2 heptagons, 1 octagon, 2 nonagons); no symmetry at all; chiral (comes in two mirror-image hands); sits in general position; roundness 26.82% of its circumsphere (56% of the Josehedron benchmark).
  Score terms: F=4.25, P=12.0, A=1.0, C=2.0, R=5.5895, I=0, D=0, E=0, S=3; overall rank 9/115.
  A name here would attach to the fact that it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape; it is chiral and its group P6_122 is one of an enantiomorphic pair, so the tiling itself has a handedness; it has 4 odd polygons of seven or more sides (largest face a 9-gon). Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL.

## Records within the pool

- Roundest (site-centred): `c0071756347c5a8a` IT(144) P3_1 c/a 1 f=(28,42,16) 43.46%; `a93f8fe7ecdc5851` IT(144) P3_1 c/a 9/8 f=(32,48,18) 42.99%; `27d463eac6cda5ea` IT(171) P6_2 c/a 5331/8000 f=(27,41,16) 41.99%. None reaches the Josehedron's 47.98%.
- Roundest (minimal enclosing sphere): `cff2d5fb5e0d4149` IT(171) P6_2 c/a 1/2 f=(23,35,14) 46.73%; `27d463eac6cda5ea` IT(171) P6_2 c/a 5331/8000 f=(27,41,16) 43.53%; `c0071756347c5a8a` IT(144) P3_1 c/a 1 f=(28,42,16) 43.48%.
- Most facets: 24 — `c49077384aaebeb0` IT(178) P6_122 c/a 5/4 f=(44,66,24).
  - tetragonal: 23 — `213c7a114d5a97a8` IT(98) I4_122 c/a 11/16 f=(42,63,23); `4f6d3e68cbd9e729` IT(98) I4_122 c/a 3/4 f=(42,63,23); `5dc2479b9bc14edc` IT(98) I4_122 c/a 9/16 f=(42,63,23).
  - trigonal: 21 — `c82ebc15c49c1413` IT(154) P3_221 c/a 527/1000 f=(38,57,21).
  - hexagonal: 24 — `c49077384aaebeb0` IT(178) P6_122 c/a 5/4 f=(44,66,24).
- Most pentagons: 8 — `16025e0680843c36` IT(169) P6_1 c/a 1 f=(32,48,18); `4a560e459032166a` IT(154) P3_221 c/a 7/8 f=(28,42,16).
- Most odd polygons of >= 7 sides: 6 — `9c0b7e0c29dfebb2` IT(169) P6_1 c/a 3/4 f=(36,54,20); `c0071756347c5a8a` IT(144) P3_1 c/a 1 f=(28,42,16); `2b9726574a0a8bed` IT(171) P6_2 c/a 1/2 f=(30,45,17).
- Largest face: 16-gon — `213c7a114d5a97a8` IT(98) I4_122 c/a 11/16 f=(42,63,23); `5dc2479b9bc14edc` IT(98) I4_122 c/a 9/16 f=(42,63,23); `3ebbca7ed2eda199` IT(98) I4_122 c/a 1/2 f=(40,60,22); `c53bc05bc306c97d` IT(166) R-3m c/a 7/8 f=(31,48,19).
- Highest symmetry (aut_comb): 4 — `9be0f2271a14b6a9` IT(178) P6_122 c/a 1 f=(36,54,20) Isom 2; `f0b07b168368759b` IT(148) R-3 c/a 3/4 f=(14,24,12) Isom 4; `d718e083bd23d2b1` IT(178) P6_122 c/a 1 f=(32,48,18) Isom 1.
- Fully asymmetric (aut = 1): 81 of 115 cells (the pool is mostly general-position witnesses); the ten best-scoring: `a93f8fe7ecdc5851` IT(144) P3_1 c/a 9/8 f=(32,48,18); `8d90c524c89922d9` IT(169) P6_1 c/a 11/8 f=(36,54,20); `e598ffd8a1cac138` IT(144) P3_1 c/a 29/32 f=(32,48,18); `9c0b7e0c29dfebb2` IT(169) P6_1 c/a 3/4 f=(36,54,20); `c0071756347c5a8a` IT(144) P3_1 c/a 1 f=(28,42,16); `3ddc41389e6d484f` IT(171) P6_2 c/a 1 f=(32,48,18); `30f2a1e483babf55` IT(178) P6_122 c/a 11/4 f=(29,44,17); `8cc8c5ab3cf36d8f` IT(178) P6_122 c/a 5/4 f=(36,54,20); `164d4bd63d82d0c3` IT(76) P4_1 c/a 5/4 f=(40,60,22); `d9ac68100a276dfe` IT(169) P6_1 c/a 2777/4000 f=(36,54,20) (the rest: full table, aut/Isom column 1/1).
- Chiral solids: 109 of 115; achiral: 6.
- Symmetry fully realized (Isom = aut): 102; fully forced by the site (site = Isom = aut): 101.
- Stratum: dim 0: 1, dim 1: 16, dim 2: 5, dim 3: 93.
- Smallest integer presentation scale m: 108 — `f0b07b168368759b` IT(148) R-3 c/a 3/4 f=(14,24,12) (integer coordinates in the hexagonal lattice basis).
- Smallest integer CARTESIAN scale (tetragonal only): 5280 — `1497877268495988` IT(91) P4_122 c/a 1/2 f=(32,48,18).
- f-vector absent from its own group's printed Schmitt table: 0 cells; absent from every printed table of its system: 0 cells — none. (Evidence, never proof; the open verdict comes first.)
- Facet count above the printed Schmitt maximum of its own group: 0 cells — none.

## Score-blind notes (things the pre-registered weights under-rank; recorded, not re-weighted)

- The only fixed-Wyckoff-point cell in the pool: `f0b07b168368759b` IT(148) R-3 c/a 3/4 f=(14,24,12), p=3^4 4^4 5^4, aut 4 all realized (Isom 4: 2 proper + 2 improper, achiral), site symmetry 2, roundness 30.94%, the smallest presentation scale in the pool (m = 108 in the lattice basis), and the smallest facet count (12). Its shape is pinned by the group and c/a alone (no point coordinate to choose); the score's F, P and D terms leave it at overall rank 77. If a small, symmetric, pinned cell is wanted as a flagship, this is the one the score hides.
- Achiral cells (6 of 115): `f0b07b168368759b` IT(148) R-3 c/a 3/4 f=(14,24,12) Isom 4 (rank 77); `f654982d74d740f6` IT(141) I4_1/amd c/a 1/2 f=(38,57,21) Isom 2 (rank 89); `c53bc05bc306c97d` IT(166) R-3m c/a 7/8 f=(31,48,19) Isom 2 (rank 102); `36c92427e3d084dc` IT(166) R-3m c/a 5/4 f=(19,30,13) Isom 2 (rank 106); `9d4396ca0b08fc3c` IT(166) R-3m c/a 3/4 f=(19,30,13) Isom 2 (rank 111); `ab801b11bead62ef` IT(166) R-3m c/a 7/4 f=(19,30,13) Isom 2 (rank 112). Chirality is the norm in this pool (109/115) because the sweep's open survivors are overwhelmingly general-position witnesses in Sohncke groups; a mirror-symmetric cell is the rarer story here.
- Presentation: NO pool cell has a small-denominator presentation at its witness (best tetragonal Cartesian scale 5280; best hexagonal-family lattice-basis scale 108; the I term is 0 for all 115). The Josehedron-style integer-coordinate hook does not exist at these witnesses. Caveat: the witness is the sweep's grid point; a nicer point on the same open stratum, or a nicer c/a inside the tested band c/a(1 +- 1/96), could present better and was not searched here.
- c/a values such as 527/1000, 797/1000, 1277/2000 are the sweep's b-grid values, not chosen constants; the metric verdict OPEN covers only c/a(1 +- 1/96) around them (WALL_OPEN_PHASE2.json). Any published presentation should pick its c/a inside that band and re-certify at the chosen value.
- Combinatorial symmetry not honoured by the geometry (aut_comb > Isom(solid)): `6797ab70c6015039` IT(76) P4_1 c/a 3/2 f=(32,48,18) aut 2 vs Isom 1; `9be0f2271a14b6a9` IT(178) P6_122 c/a 1 f=(36,54,20) aut 4 vs Isom 2; `086ac96faf390886` IT(76) P4_1 c/a 7/5 f=(36,54,20) aut 2 vs Isom 1; `bff9b24ce78050f5` IT(144) P3_1 c/a 1 f=(28,42,16) aut 2 vs Isom 1; `f05f0b009e0929f6` IT(169) P6_1 c/a 3/4 f=(32,48,18) aut 2 vs Isom 1; `d07f950b8309de82` IT(171) P6_2 c/a 67/80 f=(30,45,17) aut 2 vs Isom 1; `4a560e459032166a` IT(154) P3_221 c/a 7/8 f=(28,42,16) aut 2 vs Isom 1; `d718e083bd23d2b1` IT(178) P6_122 c/a 1 f=(32,48,18) aut 4 vs Isom 1; `505a4911e298c933` IT(181) P6_422 c/a 2 f=(28,42,16) aut 2 vs Isom 1; `f429e996b3f455a6` IT(148) R-3 c/a 3/4 f=(26,40,16) aut 2 vs Isom 1; `a35623e347ef03b4` IT(169) P6_1 c/a 5/4 f=(32,48,18) aut 2 vs Isom 1; `56918d2cff883e22` IT(148) R-3 c/a 1 f=(22,34,14) aut 2 vs Isom 1; `7b9cfe26fe4a9c4b` IT(146) R3 c/a 5/4 f=(18,30,14) aut 2 vs Isom 1. The A term credits aut_comb by the pre-registered rule; the certificate is what it is.

## Full ranked table (all 115)

| # | sys | id | group | c/a | f | p | aut/Isom(+,-) | chiral | dim | site | round site | round MES | m | f-printed (own grp) | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | hexa | `c49077384aaebeb0` | 178 P6_122 | 5/4 | (44,66,24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2/2(2,0) | y | 1 | 2 | 24.45 | 24.45 | 415800L | y | 31.60 |
| 2 | tetr | `4e9c9b076cfec323` | 92 P4_12_12 | 5/4 | (40,60,22) | 3^8 4^4 5^4 8^2 11^4 | 2/2(2,0) | y | 1 | 2 | 35.78 | 35.78 | 7608384C | y | 31.46 |
| 3 | trig | `a93f8fe7ecdc5851` | 144 P3_1 | 9/8 | (32,48,18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1/1(1,0) | y | 3 | 1 | 42.99 | 42.99 | 174960L | y | 30.46 |
| 4 | hexa | `8d90c524c89922d9` | 169 P6_1 | 11/8 | (36,54,20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1/1(1,0) | y | 3 | 1 | 32.76 | 33.51 | 1352261721498364508832L | y | 29.83 |
| 5 | trig | `e598ffd8a1cac138` | 144 P3_1 | 29/32 | (32,48,18) | 3^4 4^4 5^4 6^2 9^4 | 1/1(1,0) | y | 3 | 1 | 37.30 | 37.88 | 3400600320L | y | 29.27 |
| 6 | hexa | `9c0b7e0c29dfebb2` | 169 P6_1 | 3/4 | (36,54,20) | 3^4 4^8 5^2 7^4 13^2 | 1/1(1,0) | y | 3 | 1 | 39.39 | 41.08 | 804980880L | y | 29.21 |
| 7 | trig | `c0071756347c5a8a` | 144 P3_1 | 1 | (28,42,16) | 3^2 4^4 5^4 7^6 | 1/1(1,0) | y | 3 | 1 | 43.46 | 43.48 | 6073608960L | y | 29.06 |
| 8 | hexa | `3ddc41389e6d484f` | 171 P6_2 | 1 | (32,48,18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1/1(1,0) | y | 3 | 1 | 26.45 | 27.04 | 205530624L | y | 28.01 |
| 9 | hexa | `30f2a1e483babf55` | 178 P6_122 | 11/4 | (29,44,17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1/1(1,0) | y | 3 | 1 | 26.82 | 27.39 | 31101840L | y | 27.84 |
| 10 | hexa | `8cc8c5ab3cf36d8f` | 178 P6_122 | 5/4 | (36,54,20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1/1(1,0) | y | 3 | 1 | 27.91 | 29.84 | 9668148336000L | y | 27.82 |
| 11 | tetr | `164d4bd63d82d0c3` | 76 P4_1 | 5/4 | (40,60,22) | 3^6 4^6 5^2 6^4 11^4 | 1/1(1,0) | y | 3 | 1 | 30.22 | 30.22 | 1451520C | y | 27.80 |
| 12 | hexa | `d9ac68100a276dfe` | 169 P6_1 | 2777/4000 | (36,54,20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1/1(1,0) | y | 3 | 1 | 20.53 | 26.33 | 49716509007882298261680000000L | y | 27.28 |
| 13 | trig | `466b12546dd936c3` | 161 R3c | 527/1000 | (26,40,16) | 3^6 5^4 6^2 7^2 8^2 | 1/1(1,0) | y | 3 | 1 | 41.00 | 43.47 | 2534879524335376023000000L | y | 27.04 |
| 14 | hexa | `646b518ccf3bd724` | 169 P6_1 | 15/16 | (36,54,20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1/1(1,0) | y | 3 | 1 | 23.30 | 24.57 | 2679261418892448000L | y | 26.86 |
| 15 | hexa | `cff2d5fb5e0d4149` | 171 P6_2 | 1/2 | (23,35,14) | 4^5 5^6 6^1 7^2 | 1/1(1,0) | y | 3 | 1 | 39.81 | 46.73 | 8504712L | y | 26.80 |
| 16 | hexa | `29bbba1adec778da` | 171 P6_2 | 5/4 | (28,42,16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1/1(1,0) | y | 3 | 1 | 31.43 | 31.92 | 525600L | y | 26.55 |
| 17 | hexa | `16025e0680843c36` | 169 P6_1 | 1 | (32,48,18) | 3^2 4^4 5^8 6^2 11^2 | 1/1(1,0) | y | 3 | 1 | 23.98 | 24.88 | 119729053033200L | y | 26.50 |
| 18 | hexa | `322d5ff451e4101d` | 169 P6_1 | 11/8 | (32,48,18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1/1(1,0) | y | 3 | 1 | 27.80 | 27.87 | 1055128845980880L | y | 26.29 |
| 19 | hexa | `2d654c836f3731c6` | 178 P6_122 | 1 | (36,54,20) | 3^8 4^2 6^4 7^4 12^2 | 2/2(2,0) | y | 1 | 2 | 22.28 | 22.28 | 373464L | y | 26.14 |
| 20 | hexa | `aef8972953d53d20` | 171 P6_2 | 81/64 | (32,48,18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1/1(1,0) | y | 3 | 1 | 31.77 | 31.80 | 3416623323144192L | y | 26.12 |
| 21 | trig | `c82ebc15c49c1413` | 154 P3_221 | 527/1000 | (38,57,21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1/1(1,0) | y | 3 | 1 | 17.65 | 24.93 | 385324475138460000000L | y | 25.93 |
| 22 | trig | `847d2695a14ae424` | 152 P3_121 | 5/4 | (29,44,17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1/1(1,0) | y | 3 | 1 | 27.06 | 27.92 | 38556000L | y | 25.89 |
| 23 | hexa | `ac4489d658eb445e` | 178 P6_122 | 797/1000 | (36,54,20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 27.37 | 27.97 | 478159403402375640000000L | y | 25.70 |
| 24 | hexa | `e1a38303b2378f17` | 169 P6_1 | 1277/2000 | (40,60,22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1/1(1,0) | y | 3 | 1 | 19.74 | 27.72 | 2635263362010218940000000L | y | 25.61 |
| 25 | tetr | `6797ab70c6015039` | 76 P4_1 | 3/2 | (32,48,18) | 3^4 4^4 5^4 6^2 9^4 | 2/1(1,0) | y | 3 | 1 | 31.54 | 31.63 | 155520C | y | 25.57 |
| 26 | tetr | `213c7a114d5a97a8` | 98 I4_122 | 11/16 | (42,63,23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1/1(1,0) | y | 3 | 1 | 15.44 | 16.61 | 448061644800C | y | 25.47 |
| 27 | trig | `23594bd7053503aa` | 153 P3_212 | 1 | (32,48,18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1/1(1,0) | y | 3 | 1 | 23.59 | 25.17 | 20148894445680L | y | 25.42 |
| 28 | hexa | `59585d778cb3a7a4` | 178 P6_122 | 3/4 | (40,60,22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2/2(2,0) | y | 1 | 2 | 20.63 | 21.91 | 19872L | y | 25.30 |
| 29 | trig | `fcffad0da2b5b62f` | 154 P3_221 | 15/16 | (32,48,18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1/1(1,0) | y | 3 | 1 | 22.68 | 23.29 | 1054729821600000L | y | 25.23 |
| 30 | hexa | `042c19cbfdc869cb` | 178 P6_122 | 3/2 | (32,48,18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1/1(1,0) | y | 3 | 1 | 21.98 | 27.28 | 106109640L | y | 25.08 |
| 31 | trig | `75bbbcb4a37e70e8` | 146 R3 | 67/80 | (27,41,16) | 3^2 4^4 5^4 6^2 7^4 | 1/1(1,0) | y | 3 | 1 | 21.85 | 22.16 | 143662352230800L | y | 25.05 |
| 32 | hexa | `9be0f2271a14b6a9` | 178 P6_122 | 1 | (36,54,20) | 3^2 4^12 6^2 9^2 12^2 | 4/2(2,0) | y | 1 | 2 | 29.02 | 29.02 | 309960L | y | 25.05 |
| 33 | hexa | `dcc38ea9177089b9` | 178 P6_122 | 1/2 | (36,54,20) | 3^2 4^8 5^2 7^4 8^4 | 2/2(2,0) | y | 1 | 2 | 12.09 | 13.64 | 7560L | y | 25.02 |
| 34 | trig | `d10bb4a25bbf4c80` | 154 P3_221 | 797/1000 | (32,48,18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1/1(1,0) | y | 3 | 1 | 21.66 | 24.43 | 11875131482479719597000000L | y | 25.01 |
| 35 | hexa | `7e05ce00d8a7cbf6` | 178 P6_122 | 137/160 | (38,57,21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1/1(1,0) | y | 3 | 1 | 27.53 | 28.38 | 116013948885052416000L | y | 24.99 |
| 36 | trig | `2165f5c5260120de` | 152 P3_121 | 527/1000 | (30,45,17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1/1(1,0) | y | 3 | 1 | 17.65 | 24.55 | 672406904610000000L | y | 24.93 |
| 37 | hexa | `2b9726574a0a8bed` | 171 P6_2 | 1/2 | (30,45,17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1/1(1,0) | y | 3 | 1 | 17.62 | 26.67 | 39824235360L | y | 24.92 |
| 38 | hexa | `095ce61d28388c98` | 178 P6_122 | 1 | (40,60,22) | 3^6 4^6 6^6 7^2 14^2 | 2/2(2,0) | y | 1 | 2 | 23.43 | 24.37 | 166320L | y | 24.88 |
| 39 | trig | `d0c5a15c25ab6413` | 152 P3_121 | 17/16 | (32,48,18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1/1(1,0) | y | 3 | 1 | 25.25 | 25.36 | 2377105920L | y | 24.76 |
| 40 | hexa | `d176b8d859dd651a` | 178 P6_122 | 5/2 | (32,48,18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1/1(1,0) | y | 3 | 1 | 25.12 | 25.70 | 25704000L | y | 24.74 |
| 41 | hexa | `5b86a254c715306c` | 169 P6_1 | 797/1000 | (40,60,22) | 3^8 4^6 6^4 10^2 14^2 | 1/1(1,0) | y | 3 | 1 | 39.08 | 40.46 | 444953931410623635000000L | y | 24.64 |
| 42 | tetr | `4f6d3e68cbd9e729` | 98 I4_122 | 3/4 | (42,63,23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1/1(1,0) | y | 3 | 1 | 16.20 | 17.23 | 7637414400C | y | 24.63 |
| 43 | tetr | `2e8e49eb28497267` | 95 P4_322 | 53/40 | (40,60,22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1/1(1,0) | y | 3 | 1 | 24.50 | 27.00 | 1982073139200C | y | 24.61 |
| 44 | trig | `3d6b109f392fda19` | 154 P3_221 | 3/2 | (33,50,19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 26.94 | 27.05 | 105897792L | y | 24.36 |
| 45 | tetr | `5dc2479b9bc14edc` | 98 I4_122 | 9/16 | (42,63,23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1/1(1,0) | y | 3 | 1 | 14.34 | 16.62 | 1160516418969600C | y | 24.24 |
| 46 | trig | `27dbb77012555d28` | 161 R3c | 4439/8000 | (26,40,16) | 3^4 4^2 5^6 6^2 9^2 | 1/1(1,0) | y | 3 | 1 | 22.15 | 29.33 | 262659832348032000000L | y | 24.12 |
| 47 | hexa | `6f4101f83371033d` | 169 P6_1 | 2331/4000 | (36,54,20) | 3^4 4^8 6^4 7^2 13^2 | 1/1(1,0) | y | 3 | 1 | 18.77 | 29.02 | 15377560542424080000000L | y | 23.91 |
| 48 | trig | `64203f15fcf6c09b` | 155 R32 | 1/2 | (20,32,14) | 3^4 4^4 5^2 6^2 7^2 | 2/2(2,0) | y | 1 | 2 | 25.74 | 28.66 | 504L | y | 23.86 |
| 49 | hexa | `a182e87006c7a00d` | 179 P6_522 | 3/2 | (32,48,18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1/1(1,0) | y | 3 | 1 | 20.31 | 22.62 | 152741160L | y | 23.73 |
| 50 | hexa | `0b5d9beb0fc972f6` | 179 P6_522 | 13/8 | (32,48,18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1/1(1,0) | y | 3 | 1 | 20.08 | 21.62 | 35736622549056L | y | 23.68 |
| 51 | hexa | `dd3fb07fe11d73d3` | 179 P6_522 | 2 | (31,47,18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 23.46 | 25.28 | 46012412160L | y | 23.39 |
| 52 | hexa | `b0f80776885f3ae1` | 178 P6_122 | 1/2 | (36,54,20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2/2(2,0) | y | 1 | 2 | 17.31 | 32.63 | 648L | y | 23.11 |
| 53 | trig | `e98412e7cb95aea2` | 152 P3_121 | 3/4 | (32,48,18) | 3^4 4^6 6^2 8^6 | 2/2(2,0) | y | 1 | 2 | 33.96 | 33.96 | 312L | y | 23.08 |
| 54 | trig | `a46cbaad3c23e834` | 155 R32 | 1/2 | (32,49,19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1/1(1,0) | y | 3 | 1 | 23.07 | 25.59 | 2314773720L | y | 23.06 |
| 55 | hexa | `f6f8b3050a1eef42` | 178 P6_122 | 3/4 | (38,57,21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1/1(1,0) | y | 3 | 1 | 27.73 | 27.81 | 307646951040L | y | 23.03 |
| 56 | trig | `d770abfcee4deb90` | 153 P3_212 | 19/16 | (32,48,18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1/1(1,0) | y | 3 | 1 | 26.39 | 26.42 | 191301120L | y | 23.00 |
| 57 | hexa | `43e4e46001b4d8b9` | 181 P6_422 | 31/16 | (32,48,18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1/1(1,0) | y | 3 | 1 | 25.48 | 25.76 | 5079799872L | y | 22.81 |
| 58 | hexa | `27d463eac6cda5ea` | 171 P6_2 | 5331/8000 | (27,41,16) | 3^2 4^7 6^4 8^3 | 1/1(1,0) | y | 3 | 1 | 41.99 | 43.53 | 7737736731206016000000L | y | 22.75 |
| 59 | trig | `542cbe76934b484b` | 154 P3_221 | 5/4 | (29,44,17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1/1(1,0) | y | 3 | 1 | 26.06 | 27.21 | 947664900000L | y | 22.68 |
| 60 | trig | `2c121297dbaa80af` | 154 P3_221 | 1 | (28,42,16) | 3^4 4^2 6^8 8^2 | 1/1(1,0) | y | 3 | 1 | 41.58 | 42.70 | 63431424L | y | 22.66 |
| 61 | hexa | `24a6b511067d37b2` | 178 P6_122 | 5/4 | (30,45,17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1/1(1,0) | y | 3 | 1 | 19.32 | 26.28 | 168588000L | y | 22.28 |
| 62 | hexa | `f14a8c4e7c5b3e3a` | 180 P6_222 | 7/4 | (32,48,18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1/1(1,0) | y | 3 | 1 | 22.82 | 23.11 | 465696L | y | 22.26 |
| 63 | hexa | `7a448bed1119dfad` | 178 P6_122 | 1/2 | (36,54,20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1/1(1,0) | y | 3 | 1 | 20.32 | 25.48 | 216833760L | y | 22.23 |
| 64 | trig | `59b28b3a59c27092` | 155 R32 | 1277/2000 | (34,52,20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1/1(1,0) | y | 3 | 1 | 22.61 | 24.99 | 51811743664987740000000L | y | 22.21 |
| 65 | tetr | `1497877268495988` | 91 P4_122 | 1/2 | (32,48,18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2/2(2,0) | y | 1 | 2 | 10.55 | 20.75 | 5280C | y | 22.20 |
| 66 | trig | `07d543d89e2934f2` | 152 P3_121 | 33/32 | (36,54,20) | 3^6 4^4 5^2 6^4 10^4 | 1/1(1,0) | y | 3 | 1 | 24.82 | 25.06 | 11943106560L | y | 22.17 |
| 67 | hexa | `85244add8d1f2d55` | 169 P6_1 | 1/2 | (32,48,18) | 3^2 4^6 5^6 6^2 12^2 | 1/1(1,0) | y | 3 | 1 | 17.10 | 31.61 | 3570840L | y | 22.06 |
| 68 | trig | `72bcd959be4ab7dd` | 152 P3_121 | 5/4 | (28,42,16) | 3^4 4^1 5^4 6^4 8^3 | 1/1(1,0) | y | 3 | 1 | 23.79 | 25.75 | 20979000L | y | 21.96 |
| 69 | tetr | `086ac96faf390886` | 76 P4_1 | 7/5 | (36,54,20) | 3^2 4^8 5^6 10^4 | 2/1(1,0) | y | 3 | 1 | 30.89 | 30.89 | 1814400C | y | 21.94 |
| 70 | tetr | `3ebbca7ed2eda199` | 98 I4_122 | 1/2 | (40,60,22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1/1(1,0) | y | 3 | 1 | 13.46 | 16.84 | 599821622400C | y | 21.81 |
| 71 | trig | `fac4317d5a65b959` | 148 R-3 | 9/8 | (24,38,16) | 3^6 4^2 5^2 6^2 7^4 | 1/1(1,0) | y | 3 | 1 | 11.01 | 15.97 | 1640859021504L | y | 21.79 |
| 72 | trig | `5838282f46223111` | 152 P3_121 | 7/4 | (29,44,17) | 3^2 4^9 6^2 8^3 10^1 | 1/1(1,0) | y | 3 | 1 | 31.31 | 31.31 | 740880L | y | 21.78 |
| 73 | trig | `3a491fd6426d90b2` | 146 R3 | 33/32 | (24,38,16) | 3^4 4^4 5^2 6^4 7^2 | 1/1(1,0) | y | 3 | 1 | 20.31 | 22.18 | 4718697984L | y | 21.73 |
| 74 | tetr | `e0d18e5ea938d649` | 122 I-42d | 1 | (36,54,20) | 3^4 4^8 8^8 | 2/2(2,0) | y | 1 | 2 | 32.18 | 32.38 | 30424968C | y | 21.71 |
| 75 | hexa | `e19babba732f5fd4` | 179 P6_522 | 7/4 | (29,44,17) | 4^11 5^2 7^2 10^2 | 1/1(1,0) | y | 3 | 1 | 21.27 | 22.90 | 413696490480L | y | 21.68 |
| 76 | hexa | `e0bf1a48f096c10d` | 180 P6_222 | 1 | (32,48,18) | 4^8 5^6 6^2 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 15.15 | 16.53 | 472325040L | y | 21.66 |
| 77 | trig | `f0b07b168368759b` | 148 R-3 | 3/4 | (14,24,12) | 3^4 4^4 5^4 | 4/4(2,2) | n | 0 | 2 | 30.94 | 30.94 | 108L | y | 21.45 |
| 78 | trig | `87c94384d7851cb2` | 155 R32 | 797/1000 | (34,52,20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1/1(1,0) | y | 3 | 1 | 18.91 | 20.94 | 62428340520000000L | y | 21.44 |
| 79 | trig | `b2430fc4bea4e06d` | 154 P3_221 | 1/2 | (34,51,19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1/1(1,0) | y | 3 | 1 | 17.10 | 26.19 | 1836432L | y | 21.31 |
| 80 | trig | `e198aac88f223892` | 153 P3_212 | 3/4 | (30,45,17) | 3^2 4^5 5^4 6^4 10^2 | 1/1(1,0) | y | 3 | 1 | 19.19 | 22.33 | 8756581680L | y | 21.25 |
| 81 | trig | `2081d7b9a734e4fe` | 155 R32 | 11/8 | (32,50,20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 13.10 | 18.45 | 2011426560L | y | 21.23 |
| 82 | hexa | `0948aa6184f13a8a` | 179 P6_522 | 5/4 | (30,45,17) | 3^4 4^4 6^4 7^2 8^3 | 1/1(1,0) | y | 3 | 1 | 17.76 | 21.47 | 1060668000L | y | 20.95 |
| 83 | trig | `cbead3df2d2f1d0e` | 154 P3_221 | 1277/2000 | (34,51,19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1/1(1,0) | y | 3 | 1 | 19.83 | 24.99 | 7963370477592616944000000L | y | 20.88 |
| 84 | trig | `bff9b24ce78050f5` | 144 P3_1 | 1 | (28,42,16) | 4^8 5^4 8^4 | 2/1(1,0) | y | 3 | 1 | 40.05 | 40.42 | 207360L | y | 20.85 |
| 85 | tetr | `7575121042ade3b3` | 98 I4_122 | 7/4 | (32,48,18) | 4^11 6^4 8^1 10^2 | 2/2(2,0) | y | 1 | 2 | 25.22 | 26.79 | 1182720C | y | 20.76 |
| 86 | trig | `cda1d1c03659b67d` | 148 R-3 | 527/1000 | (22,34,14) | 4^6 5^4 6^4 | 1/1(1,0) | y | 3 | 1 | 31.14 | 32.04 | 14592227867250885000000L | y | 20.49 |
| 87 | trig | `057255f61286b052` | 167 R-3c | 1/2 | (24,38,16) | 3^6 4^2 6^6 7^2 | 2/2(2,0) | y | 1 | 2 | 16.66 | 19.17 | 1080L | y | 20.47 |
| 88 | hexa | `f05f0b009e0929f6` | 169 P6_1 | 3/4 | (32,48,18) | 3^2 4^6 5^6 6^2 12^2 | 2/1(1,0) | y | 3 | 1 | 21.21 | 25.93 | 1605992946480L | y | 20.42 |
| 89 | tetr | `f654982d74d740f6` | 141 I4_1/amd | 1/2 | (38,57,21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2/2(1,1) | n | 2 | 2 | 21.63 | 29.07 | 32640C | y | 20.26 |
| 90 | hexa | `a348875c3f707895` | 178 P6_122 | 1/2 | (36,54,20) | 3^4 4^10 6^2 8^2 14^2 | 2/2(2,0) | y | 1 | 2 | 12.14 | 22.98 | 3960L | y | 20.03 |
| 91 | trig | `74a69fba4266de3b` | 167 R-3c | 527/1000 | (28,43,17) | 3^10 6^1 8^5 10^1 | 1/1(1,0) | y | 3 | 1 | 28.99 | 35.99 | 15397295760000000L | y | 19.79 |
| 92 | trig | `d9bf7fb7a80eaa38` | 155 R32 | 5/4 | (30,47,19) | 3^4 4^6 5^4 6^3 10^2 | 1/1(1,0) | y | 3 | 1 | 12.08 | 17.18 | 103896000L | y | 19.77 |
| 93 | hexa | `d07f950b8309de82` | 171 P6_2 | 67/80 | (30,45,17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2/1(1,0) | y | 3 | 1 | 23.93 | 26.95 | 334841050203660000L | y | 19.74 |
| 94 | hexa | `257b627a90b78038` | 180 P6_222 | 1 | (22,35,15) | 3^4 4^6 6^3 8^2 | 2/2(2,0) | y | 1 | 2 | 21.12 | 23.40 | 4320L | y | 19.65 |
| 95 | hexa | `34351050a4f29035` | 178 P6_122 | 1 | (28,42,16) | 3^2 4^5 5^2 6^4 8^3 | 1/1(1,0) | y | 3 | 1 | 17.04 | 27.21 | 1685880L | y | 19.55 |
| 96 | trig | `37aa18e6e10583be` | 155 R32 | 9/8 | (30,47,19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1/1(1,0) | y | 3 | 1 | 11.01 | 15.94 | 31207680L | y | 19.54 |
| 97 | hexa | `437fbe758a6dd8e3` | 179 P6_522 | 1/2 | (32,48,18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1/1(1,0) | y | 3 | 1 | 9.78 | 28.24 | 3984120L | y | 19.54 |
| 98 | trig | `6de3dac5f334cfed` | 167 R-3c | 1/2 | (26,40,16) | 3^4 4^6 6^2 8^4 | 1/1(1,0) | y | 3 | 1 | 28.65 | 36.06 | 2882880L | y | 19.47 |
| 99 | trig | `5f812747976b224a` | 148 R-3 | 39/32 | (20,32,14) | 3^2 4^6 5^4 7^2 | 1/1(1,0) | y | 3 | 1 | 11.82 | 16.60 | 4112199936L | y | 19.46 |
| 100 | trig | `36ec4ad2f530e145` | 151 P3_112 | 3/4 | (30,45,17) | 3^2 4^6 6^7 8^1 10^1 | 1/1(1,0) | y | 3 | 1 | 18.59 | 20.62 | 376804060920L | y | 19.12 |
| 101 | trig | `4a560e459032166a` | 154 P3_221 | 7/8 | (28,42,16) | 3^4 5^8 8^4 | 2/1(1,0) | y | 3 | 1 | 22.13 | 23.66 | 56170527259392L | y | 19.11 |
| 102 | trig | `c53bc05bc306c97d` | 166 R-3m | 7/8 | (31,48,19) | 3^4 4^8 5^4 8^2 16^1 | 2/2(1,1) | n | 2 | 2 | 12.98 | 16.09 | 517345920L | y | 18.95 |
| 103 | trig | `ce3b42c8a4ceff6f` | 151 P3_112 | 1/2 | (34,51,19) | 3^6 4^6 6^2 8^3 12^2 | 1/1(1,0) | y | 3 | 1 | 13.75 | 18.88 | 653609880L | y | 18.62 |
| 104 | hexa | `af8b2135c913b13b` | 181 P6_422 | 7/8 | (32,48,18) | 3^6 4^4 6^4 8^1 10^3 | 1/1(1,0) | y | 3 | 1 | 14.38 | 25.30 | 150202612254240L | y | 18.50 |
| 105 | hexa | `d718e083bd23d2b1` | 178 P6_122 | 1 | (32,48,18) | 4^13 8^4 12^1 | 4/1(1,0) | y | 3 | 1 | 28.62 | 29.93 | 375019725960L | y | 18.46 |
| 106 | trig | `36c92427e3d084dc` | 166 R-3m | 5/4 | (19,30,13) | 3^4 4^4 5^2 7^2 8^1 | 2/2(1,1) | n | 2 | 2 | 11.13 | 16.04 | 28800L | y | 18.07 |
| 107 | hexa | `505a4911e298c933` | 181 P6_422 | 2 | (28,42,16) | 3^2 4^6 6^6 8^1 10^1 | 2/1(1,0) | y | 3 | 1 | 26.17 | 26.42 | 27648L | y | 17.95 |
| 108 | hexa | `7715c7010e513b71` | 181 P6_422 | 1 | (30,45,17) | 4^10 6^4 8^2 10^1 | 1/1(1,0) | y | 3 | 1 | 15.75 | 26.13 | 148496401440L | y | 17.53 |
| 109 | trig | `c3b4b14633c9d4d5` | 155 R32 | 1 | (28,43,17) | 4^9 5^2 6^4 8^2 | 1/1(1,0) | y | 3 | 1 | 13.22 | 17.54 | 393120L | y | 17.50 |
| 110 | trig | `f429e996b3f455a6` | 148 R-3 | 3/4 | (26,40,16) | 3^6 5^6 8^4 | 2/1(1,0) | y | 3 | 1 | 20.66 | 25.08 | 2218741997040L | y | 17.31 |
| 111 | trig | `9d4396ca0b08fc3c` | 166 R-3m | 3/4 | (19,30,13) | 4^8 5^4 8^1 | 2/2(1,1) | n | 2 | 2 | 20.66 | 38.86 | 7560L | y | 17.06 |
| 112 | trig | `ab801b11bead62ef` | 166 R-3m | 7/4 | (19,30,13) | 3^6 4^2 5^2 6^2 12^1 | 2/2(1,1) | n | 2 | 2 | 13.85 | 14.60 | 296352L | y | 16.64 |
| 113 | hexa | `a35623e347ef03b4` | 169 P6_1 | 5/4 | (32,48,18) | 4^10 6^6 10^2 | 2/1(1,0) | y | 3 | 1 | 26.32 | 26.49 | 125346016338709257000L | y | 16.49 |
| 114 | trig | `56918d2cff883e22` | 148 R-3 | 1 | (22,34,14) | 4^8 5^2 6^2 7^2 | 2/1(1,0) | y | 3 | 1 | 13.22 | 17.85 | 828608839344L | y | 16.25 |
| 115 | trig | `7b9cfe26fe4a9c4b` | 146 R3 | 5/4 | (18,30,14) | 3^4 4^6 6^4 | 2/1(1,0) | y | 3 | 1 | 22.17 | 26.28 | 335400L | y | 14.12 |

m: C = integer Cartesian scale (tetragonal), L = lattice-basis scale (hexagonal family). round = % of circumsphere volume, site-centred / minimal enclosing sphere.

## Verify (main session, before acceptance)

```
cd <repo>/harness/phase2 && nice -n 10 python3 pool_ranking_2026-09-04.py; echo exit $?; md5 -q POOL_RANKING_2026-09-04.json
```

Exit 0 and the md5 printed in the STATUS entry are required. The script rewrites this file below the pre-registration block; the block itself is read back and never regenerated.
