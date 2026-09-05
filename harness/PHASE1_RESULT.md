# PHASE 1 result — cubic sweep (2026-08-28)

Spec: `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §2.1 Phase 1 + `../PROGRAM_PLAN_2026-08-27.md` step 4. Gates: `../ANCHORS.md` G3 (exact-confirmation invariant, ENFORCED per stored sighting) and the KILL CRITERIA (>38 facets = quarantine). Pipeline: the G0/G2-validated chain `orbit.py` -> `sweep_voronoi.py` (float, W=2, W=3 retry) -> `exact_cell.py` (all-Fraction, provable cutoff asserted) -> `canon_code.py`. Frozen G1 `spacegroups.json` only.

**LANGUAGE (G5): every type below marked NEW means "not matched against catalog snapshot of 2026-08-28" (5 parallelohedra + Josehedron + Schmitt-220 representative). NO novelty claim, NO naming — novelty diligence is a later gate. Schmitt ch.2 is a sampling survey: absence there is evidence, not proof.**

## Method

- Point menu per group: ALL special-position orbits on the per-coordinate denominator {2,3,4,6,8,12} grid (4096 scanned points, exact stabilizer test, orbit-deduped to one representative), + 2 general-position rational controls. 1-parameter Wyckoff lines and 2-parameter planes enter as their rational grid samples; the stratum dimension (0=fixed point, 1=line sample, 2=plane sample, 3=general) is recorded per orbit.
- One exact representative cell per orbit (orbit cells are congruent: the group acts transitively by isometries — cubic R are signed permutations — and Voronoi commutes with isometries); float sweep covers ALL orbit cells and their (F, p-vector) uniformity is checked.
- G3 per stored sighting: exact facet count, p-vector and neighbor site set must agree with the float proposal (or the float cell carries the degeneracy flag, in which case exact supersedes — flagged, not fatal, per the G0 amendment); canonical codes from exact facet cycles only.
- Lattice-degenerate orbits (exact closure test) still run the chain and MUST match a seeded parallelohedron (Fedorov); recorded, counted separately.
- Consistency kill added: site-stabilizer order must divide the combinatorial aut order (the stabilizer injects into the cell's map automorphism group).
- Corridor reading (recorded): the scout names 198, 199, 212, 213, 214, 220 of its "8-group chiral corridor"; the standard quarter-cubic octet is completed by 205, 206 (Pa-3, Ia-3) — those two are my addition, flagged as such. Corridor ran first; all 36 cubic groups were processed.

## Per-group table

| group | symbol | corr | ops | orbits (spec+gen) | skipped | exact cells | lattice-degen | types | NEW first here | quar | max F |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 195 | P23 |  | 12 | 48 (46+2) | 0 | 48 | 4 | 6 | 3 | 0 | 13 |
| 196 | F23 |  | 48 | 32 (30+2) | 0 | 32 | 4 | 4 | 0 | 0 | 12 |
| 197 | I23 |  | 24 | 25 (23+2) | 0 | 25 | 2 | 8 | 6 | 0 | 15 |
| 198 | P2_13 | Y | 12 | 18 (16+2) | 0 | 18 | 4 | 4 | 2 | 0 | 18 |
| 199 | I2_13 | Y | 24 | 26 (24+2) | 0 | 26 | 2 | 8 | 6 | 0 | 20 |
| 200 | Pm-3 |  | 24 | 139 (137+2) | 0 | 139 | 3 | 7 | 3 | 0 | 10 |
| 201 | Pn-3 |  | 24 | 26 (24+2) | 0 | 26 | 3 | 9 | 3 | 0 | 16 |
| 202 | Fm-3 |  | 96 | 46 (44+2) | 0 | 46 | 3 | 7 | 0 | 0 | 12 |
| 203 | Fd-3 |  | 96 | 18 (16+2) | 0 | 18 | 1 | 8 | 3 | 0 | 16 |
| 204 | Im-3 |  | 48 | 71 (69+2) | 0 | 71 | 2 | 17 | 8 | 0 | 14 |
| 205 | Pa-3 | Y | 24 | 11 (9+2) | 0 | 11 | 3 | 5 | 3 | 0 | 16 |
| 206 | Ia-3 | Y | 48 | 15 (13+2) | 0 | 15 | 2 | 7 | 6 | 0 | 17 |
| 207 | P432 |  | 24 | 48 (46+2) | 0 | 48 | 3 | 6 | 1 | 0 | 9 |
| 208 | P4_232 |  | 24 | 39 (37+2) | 0 | 39 | 3 | 10 | 3 | 0 | 16 |
| 209 | F432 |  | 96 | 28 (26+2) | 0 | 28 | 3 | 6 | 1 | 0 | 12 |
| 210 | F4_132 |  | 96 | 24 (22+2) | 0 | 24 | 1 | 9 | 0 | 0 | 16 |
| 211 | I432 |  | 48 | 32 (30+2) | 0 | 32 | 2 | 15 | 3 | 0 | 14 |
| 212 | P4_332 | Y | 24 | 25 (23+2) | 0 | 25 | 0 | 11 | 5 | 0 | 22 |
| 213 | P4_132 | Y | 24 | 25 (23+2) | 0 | 25 | 0 | 11 | 1 | 0 | 22 |
| 214 | I4_132 | Y | 48 | 28 (26+2) | 0 | 28 | 1 | 13 | 7 | 0 | 19 |
| 215 | P-43m |  | 24 | 139 (137+2) | 0 | 139 | 4 | 8 | 0 | 0 | 12 |
| 216 | F-43m |  | 96 | 68 (66+2) | 0 | 68 | 4 | 5 | 0 | 0 | 12 |
| 217 | I-43m |  | 48 | 71 (69+2) | 0 | 71 | 2 | 14 | 2 | 0 | 15 |
| 218 | P-43n |  | 24 | 26 (24+2) | 0 | 26 | 2 | 8 | 1 | 0 | 15 |
| 219 | F-43c |  | 96 | 18 (16+2) | 0 | 18 | 4 | 5 | 0 | 0 | 12 |
| 220 | I-43d | Y | 48 | 15 (13+2) | 0 | 15 | 1 | 10 | 5 | 0 | 17 |
| 221 | Pm-3m |  | 48 | 132 (130+2) | 0 | 132 | 3 | 5 | 0 | 0 | 8 |
| 222 | Pn-3n |  | 48 | 26 (24+2) | 0 | 26 | 2 | 13 | 1 | 0 | 14 |
| 223 | Pm-3n |  | 48 | 78 (76+2) | 0 | 78 | 2 | 20 | 4 | 0 | 14 |
| 224 | Pn-3m |  | 48 | 78 (76+2) | 0 | 78 | 3 | 18 | 4 | 0 | 16 |
| 225 | Fm-3m |  | 192 | 52 (50+2) | 0 | 52 | 3 | 6 | 0 | 0 | 12 |
| 226 | Fm-3c |  | 192 | 30 (28+2) | 0 | 30 | 3 | 7 | 1 | 0 | 9 |
| 227 | Fd-3m |  | 192 | 39 (37+2) | 0 | 39 | 1 | 12 | 1 | 0 | 16 |
| 228 | Fd-3c |  | 192 | 14 (12+2) | 0 | 14 | 3 | 8 | 0 | 0 | 16 |
| 229 | Im-3m |  | 96 | 71 (69+2) | 0 | 71 | 2 | 17 | 3 | 0 | 14 |
| 230 | Ia-3d |  | 96 | 16 (14+2) | 0 | 16 | 1 | 16 | 9 | 0 | 23 |

Totals: 1597 orbits tried (0 skipped on budget), 39288 float cells summarized, 1597 exact representative cells, 95 distinct types not matched against the catalog snapshot, 0 quarantines. Max facet count stored: **23** (no >38 sightings at all).

## Seeded types and their re-sightings this run

- `e3faf0283734fac7` **cube** f=(8, 12, 6) p=4^6 aut=48 — 102 sightings in the sweep
- `c1824c64dfbb3615` **elongated_dodecahedron** f=(18, 28, 12) p=4^8 6^4 aut=16 — 0 sightings in the sweep
- `fd9a9f68ec1db422` **hexagonal_prism** f=(12, 18, 8) p=4^6 6^2 aut=24 — 0 sightings in the sweep
- `1da02fe6c7c6eb73` **rhombic_dodecahedron** f=(14, 24, 12) p=4^12 aut=48 — 79 sightings in the sweep
- `31d09faf7fb2bf6f` **truncated_octahedron** f=(24, 36, 14) p=4^6 6^8 aut=48 — 17 sightings in the sweep
- `dfccc9ff6019ead5` **josehedron** f=(12, 22, 12) p=3^4 4^8 aut=4 — 13 sightings in the sweep
- `55796a72718dbb3d` **schmitt220_general_f12_22_12** f=(12, 22, 12) p=3^6 4^4 5^2 aut=1 — 0 sightings in the sweep

## Types NOT matched against catalog snapshot of 2026-08-28 (95)

Sorted by (facets, p-vector). Witness = first sighting in run order (corridor first). dim: 0 fixed Wyckoff point / 1 line sample / 2 plane sample / 3 general position.

| id | F | f-vector | p-vector | aut | witness group | witness point | stab | dim | orbit(conv) | sightings |
|---|---|---|---|---|---|---|---|---|---|---|
| `e1c6bb874212013b` | 4 | (4, 6, 4) | 3^4 | 24 | 197 I23 | (0, 1/4, 1/2) | 2 | 1 | 12 | 103 |
| `42bc5c5af1f296ae` | 5 | (5, 8, 5) | 3^4 4^1 | 8 | 195 P23 | (0, 0, 1/12) | 2 | 1 | 6 | 196 |
| `a1053191a6317676` | 5 | (6, 9, 5) | 3^2 4^3 | 12 | 211 I432 | (0, 1/12, 1/2) | 2 | 1 | 24 | 29 |
| `8f286dc3c145b5c1` | 6 | (5, 9, 6) | 3^6 | 12 | 200 Pm-3 | (0, 1/12, 1/12) | 2 | 2 | 12 | 100 |
| `920b287204a10d5a` | 6 | (6, 10, 6) | 3^4 4^2 | 2 | 200 Pm-3 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 8 |
| `26df90c2289ea27c` | 6 | (7, 11, 6) | 3^3 4^2 5^1 | 2 | 229 Im-3m | (0, 1/3, 3/8) | 2 | 2 | 48 | 1 |
| `d1fe8ecee64ce269` | 6 | (8, 12, 6) | 3^2 4^2 5^2 | 4 | 229 Im-3m | (0, 3/8, 5/12) | 2 | 2 | 48 | 1 |
| `36ea4b551873828d` | 7 | (6, 11, 7) | 3^6 4^1 | 2 | 200 Pm-3 | (0, 1/12, 1/8) | 2 | 2 | 12 | 86 |
| `d2d935e5499e6e11` | 7 | (6, 11, 7) | 3^6 4^1 | 4 | 224 Pn-3m | (1/12, 1/12, 5/12) | 2 | 2 | 24 | 6 |
| `ab4f647ac25e875b` | 7 | (7, 12, 7) | 3^5 4^1 5^1 | 1 | 226 Fm-3c | (1/8, 1/6, 5/12) | 1 | 3 | 192 | 2 |
| `d724d08efce3fe5f` | 7 | (8, 13, 7) | 3^4 4^2 6^1 | 4 | 227 Fd-3m | (1/12, 1/12, 1/6) | 2 | 2 | 96 | 2 |
| `ca9a19039647d676` | 7 | (10, 15, 7) | 3^3 5^3 6^1 | 6 | 203 Fd-3 | (1/12, 1/12, 1/12) | 3 | 1 | 32 | 21 |
| `4ab699adbeb533b0` | 7 | (8, 13, 7) | 3^2 4^5 | 4 | 204 Im-3 | (1/8, 1/6, 5/12) | 1 | 3 | 48 | 116 |
| `3689e6843979c9c4` | 7 | (9, 14, 7) | 3^2 4^4 6^1 | 4 | 229 Im-3m | (1/12, 1/8, 1/8) | 2 | 2 | 48 | 3 |
| `f98a3ee5675fc121` | 7 | (10, 15, 7) | 3^2 4^3 6^2 | 4 | 224 Pn-3m | (1/8, 1/6, 5/12) | 1 | 3 | 48 | 1 |
| `3cb6c70abd57e0b9` | 8 | (6, 12, 8) | 3^8 | 48 | 206 Ia-3 | (0, 0, 1/4) | 2 | 1 | 24 | 93 |
| `656d9056ac5f71b1` | 8 | (7, 13, 8) | 3^6 4^2 | 2 | 223 Pm-3n | (0, 1/12, 1/6) | 2 | 2 | 24 | 6 |
| `ea22673a3a17c26a` | 8 | (8, 14, 8) | 3^4 4^4 | 2 | 212 P4_332 | (1/8, 1/8, 5/8) | 2 | 1 | 12 | 4 |
| `73ae50cb39507abf` | 9 | (8, 15, 9) | 3^6 4^3 | 6 | 209 F432 | (1/8, 1/6, 5/12) | 1 | 3 | 96 | 8 |
| `cb203d1497f608a6` | 9 | (8, 15, 9) | 3^6 4^3 | 2 | 207 P432 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 8 |
| `f3d0f39a0b9676b9` | 9 | (10, 17, 9) | 3^4 4^3 5^2 | 2 | 214 I4_132 | (0, 0, 1/4) | 2 | 1 | 24 | 2 |
| `1c5d013b7a344bfb` | 9 | (10, 17, 9) | 3^2 4^7 | 2 | 217 I-43m | (1/12, 1/3, 1/3) | 2 | 2 | 24 | 2 |
| `9b69eefb8bd8437c` | 9 | (11, 18, 9) | 3^2 4^5 5^2 | 2 | 224 Pn-3m | (1/12, 1/3, 1/3) | 2 | 2 | 24 | 2 |
| `c5962af3dcab8e26` | 9 | (12, 19, 9) | 4^8 6^1 | 4 | 217 I-43m | (1/12, 1/12, 1/8) | 2 | 2 | 24 | 46 |
| `3d1a3ee0cfdc0206` | 10 | (8, 16, 10) | 3^8 4^2 | 8 | 195 P23 | (0, 1/12, 1/2) | 2 | 1 | 6 | 61 |
| `e1c8fb393143bb7d` | 10 | (8, 16, 10) | 3^8 4^2 | 2 | 223 Pm-3n | (0, 1/6, 1/4) | 2 | 2 | 24 | 2 |
| `1c845578c03feb42` | 10 | (9, 17, 10) | 3^6 4^4 | 4 | 204 Im-3 | (0, 1/3, 1/3) | 2 | 2 | 24 | 7 |
| `6f76cff2845e50c4` | 10 | (10, 18, 10) | 3^4 4^6 | 2 | 204 Im-3 | (0, 1/4, 1/3) | 2 | 2 | 24 | 6 |
| `4adc28c1904f92e2` | 10 | (11, 19, 10) | 3^4 4^4 5^2 | 2 | 204 Im-3 | (0, 1/12, 1/6) | 2 | 2 | 24 | 44 |
| `5c4afde4a99b7e18` | 10 | (11, 19, 10) | 3^4 4^4 5^2 | 4 | 204 Im-3 | (0, 3/8, 5/12) | 2 | 2 | 24 | 11 |
| `864f0730e9e2ab41` | 10 | (11, 19, 10) | 3^4 4^4 5^2 | 2 | 223 Pm-3n | (0, 1/4, 1/3) | 2 | 2 | 24 | 6 |
| `18391c406d2fe823` | 10 | (12, 20, 10) | 4^10 | 16 | 204 Im-3 | (0, 1/12, 1/12) | 2 | 2 | 24 | 33 |
| `e5f952f88b3beade` | 11 | (9, 18, 11) | 3^8 4^3 | 3 | 220 I-43d | (1/12, 1/12, 1/12) | 3 | 1 | 16 | 2 |
| `4fc0ad99c617364f` | 11 | (10, 19, 11) | 3^6 4^5 | 4 | 230 Ia-3d | (1/8, 1/8, 3/8) | 2 | 1 | 48 | 1 |
| `481d26d16f89a9f8` | 11 | (13, 22, 11) | 3^5 4^3 5^1 6^2 | 2 | 223 Pm-3n | (0, 1/3, 3/8) | 2 | 2 | 24 | 2 |
| `f5d10226705a540c` | 11 | (13, 22, 11) | 3^5 4^1 5^5 | 2 | 204 Im-3 | (0, 1/3, 3/8) | 2 | 2 | 24 | 2 |
| `c4ea3f32fdd6dc51` | 11 | (14, 23, 11) | 3^4 4^4 6^3 | 2 | 224 Pn-3m | (1/12, 3/8, 3/8) | 2 | 2 | 24 | 4 |
| `f037247acdde20aa` | 11 | (13, 22, 11) | 3^2 4^7 5^2 | 2 | 214 I4_132 | (1/8, 1/8, 3/8) | 2 | 1 | 24 | 2 |
| `d995cf9c001c7056` | 11 | (14, 23, 11) | 3^2 4^5 5^4 | 1 | 222 Pn-3n | (1/8, 1/6, 5/12) | 1 | 3 | 48 | 2 |
| `8cf50403cf88c455` | 11 | (16, 25, 11) | 3^2 4^1 5^8 | 4 | 220 I-43d | (0, 0, 1/4) | 2 | 1 | 24 | 2 |
| `bc4a89d3111082c9` | 11 | (13, 22, 11) | 3^1 4^9 5^1 | 2 | 204 Im-3 | (0, 1/12, 1/8) | 2 | 2 | 24 | 8 |
| `9effc8684d8a0250` | 12 | (10, 20, 12) | 3^8 4^4 | 16 | 197 I23 | (0, 0, 1/2) | 4 | 0 | 6 | 22 |
| `971596772f324b8e` | 12 | (12, 22, 12) | 3^8 5^4 | 4 | 199 I2_13 | (0, 1/4, 1/8) | 2 | 1 | 12 | 8 |
| `ddd534b6185c5da1` | 12 | (12, 22, 12) | 3^4 4^8 | 8 | 203 Fd-3 | (0, 0, 1/12) | 2 | 1 | 48 | 6 |
| `1c61fe8a173a95f3` | 12 | (14, 24, 12) | 3^4 4^4 5^4 | 2 | 203 Fd-3 | (1/8, 1/6, 5/12) | 1 | 3 | 96 | 6 |
| `2508b5bfd6393c2c` | 12 | (14, 24, 12) | 3^2 4^8 5^2 | 1 | 220 I-43d | (1/12, 3/8, 1/6) | 1 | 3 | 48 | 1 |
| `bb9b4185aaf3bd6c` | 12 | (16, 26, 12) | 3^2 4^7 5^2 8^1 | 1 | 211 I432 | (1/12, 3/8, 1/6) | 1 | 3 | 48 | 1 |
| `d5455821196c461d` | 13 | (14, 25, 13) | 3^8 5^4 6^1 | 4 | 197 I23 | (0, 1/12, 1/2) | 2 | 1 | 12 | 18 |
| `ff0921cada9796e2` | 13 | (16, 27, 13) | 3^6 4^4 6^2 8^1 | 2 | 214 I4_132 | (1/12, 1/6, 1/8) | 2 | 1 | 24 | 2 |
| `7d9cb42d3e017b02` | 13 | (16, 27, 13) | 3^4 4^6 5^2 8^1 | 2 | 195 P23 | (1/8, 1/6, 5/12) | 1 | 3 | 12 | 16 |
| `dd90029f74b374ae` | 13 | (15, 26, 13) | 3^4 4^5 5^4 | 2 | 220 I-43d | (0, 1/4, 1/12) | 2 | 1 | 24 | 2 |
| `b12aa22b226a2f18` | 13 | (17, 28, 13) | 3^4 4^5 5^2 6^1 8^1 | 1 | 230 Ia-3d | (1/12, 3/8, 1/6) | 1 | 3 | 96 | 1 |
| `2aafa354bb5e01d9` | 13 | (16, 27, 13) | 3^2 4^9 6^2 | 2 | 199 I2_13 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 6 |
| `63fe22ddbb5dc8f2` | 13 | (18, 29, 13) | 3^2 4^7 6^4 | 1 | 197 I23 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 2 |
| `a3164ecfcd75d3ec` | 13 | (17, 28, 13) | 4^12 8^1 | 8 | 197 I23 | (0, 0, 1/12) | 2 | 1 | 12 | 80 |
| `ec7cd8bf24cc544f` | 13 | (18, 29, 13) | 4^7 5^6 | 2 | 230 Ia-3d | (1/12, 1/6, 5/8) | 2 | 1 | 48 | 1 |
| `bad4b371f5bd4e3e` | 13 | (19, 30, 13) | 4^6 5^6 6^1 | 3 | 205 Pa-3 | (1/12, 1/12, 1/12) | 3 | 1 | 8 | 6 |
| `e6ba9617aaf7ab80` | 14 | (16, 28, 14) | 3^8 4^4 8^2 | 4 | 208 P4_232 | (0, 1/12, 1/2) | 2 | 1 | 12 | 18 |
| `dab82b770ec34253` | 14 | (16, 28, 14) | 3^8 4^2 6^4 | 4 | 206 Ia-3 | (0, 1/4, 1/3) | 2 | 1 | 24 | 8 |
| `d6d4863002a0c8c3` | 14 | (15, 27, 14) | 3^6 4^6 6^2 | 3 | 230 Ia-3d | (1/12, 1/12, 1/12) | 3 | 1 | 32 | 1 |
| `b1f554d5e1c1ffe1` | 14 | (20, 32, 14) | 3^6 4^3 5^2 6^1 8^1 10^1 | 1 | 211 I432 | (1/8, 1/6, 5/12) | 1 | 3 | 48 | 1 |
| `c4c06de9148a1d5e` | 14 | (18, 30, 14) | 3^4 4^6 5^2 7^2 | 1 | 205 Pa-3 | (1/12, 3/8, 1/6) | 1 | 3 | 24 | 1 |
| `e7f0765aca44108d` | 14 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 1 | 206 Ia-3 | (1/12, 3/8, 1/6) | 1 | 3 | 48 | 1 |
| `81ae9d74bed8fad3` | 14 | (20, 32, 14) | 4^11 6^2 8^1 | 2 | 230 Ia-3d | (0, 1/4, 1/3) | 2 | 1 | 48 | 1 |
| `1006ba9d7710fc74` | 14 | (20, 32, 14) | 4^10 6^4 | 4 | 206 Ia-3 | (0, 1/4, 1/12) | 2 | 1 | 24 | 5 |
| `3dae45da9b1de603` | 14 | (22, 34, 14) | 4^4 5^8 6^2 | 2 | 230 Ia-3d | (1/12, 1/8, 1/6) | 2 | 1 | 48 | 1 |
| `d92507e86522ff33` | 15 | (19, 32, 15) | 3^8 4^3 7^4 | 2 | 206 Ia-3 | (1/8, 1/6, 5/12) | 1 | 3 | 48 | 3 |
| `54b54f88d19759a3` | 15 | (20, 33, 15) | 3^6 4^4 6^4 8^1 | 1 | 208 P4_232 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 1 |
| `2de0a21129cabe90` | 15 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 1 | 201 Pn-3 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 1 |
| `c5b97d7745060a86` | 15 | (22, 35, 15) | 3^6 4^3 5^2 7^2 8^2 | 1 | 201 Pn-3 | (1/12, 3/8, 1/6) | 1 | 3 | 24 | 1 |
| `21d94ee4a2af0f9f` | 15 | (22, 35, 15) | 3^6 4^1 5^4 6^1 7^2 8^1 | 1 | 218 P-43n | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 2 |
| `0ee26ed471c923e2` | 15 | (22, 35, 15) | 3^4 5^10 8^1 | 2 | 220 I-43d | (0, 1/4, 1/3) | 2 | 1 | 24 | 2 |
| `8993441351ed232f` | 15 | (21, 34, 15) | 3^2 4^8 5^4 10^1 | 1 | 230 Ia-3d | (1/8, 1/4, 1/6) | 1 | 3 | 96 | 1 |
| `cea2f3246210cd55` | 15 | (22, 35, 15) | 3^2 4^7 5^4 8^2 | 2 | 199 I2_13 | (1/12, 3/8, 1/6) | 1 | 3 | 24 | 4 |
| `1148b1810c34b982` | 15 | (26, 39, 15) | 4^6 6^9 | 12 | 197 I23 | (1/12, 1/12, 1/12) | 3 | 1 | 8 | 18 |
| `2001fe7ea92fd0ad` | 16 | (16, 30, 16) | 3^12 6^4 | 24 | 212 P4_332 | (0, 0, 0) | 3 | 1 | 8 | 10 |
| `61793797a474ca0c` | 16 | (24, 38, 16) | 3^8 4^1 6^4 8^3 | 2 | 230 Ia-3d | (0, 1/4, 1/12) | 2 | 1 | 48 | 1 |
| `effc729383b9ec06` | 16 | (22, 36, 16) | 3^6 4^6 6^1 8^3 | 3 | 212 P4_332 | (1/12, 5/12, 7/12) | 3 | 1 | 8 | 4 |
| `093e6d425d7e4fc0` | 16 | (24, 38, 16) | 3^6 4^3 5^2 6^3 8^1 10^1 | 1 | 208 P4_232 | (1/12, 3/8, 1/6) | 1 | 3 | 24 | 1 |
| `9d34332ec1120aff` | 16 | (22, 36, 16) | 3^6 4^2 5^6 8^2 | 1 | 205 Pa-3 | (1/8, 1/6, 5/12) | 1 | 3 | 24 | 1 |
| `80f5582684f3bd01` | 16 | (22, 36, 16) | 3^4 4^4 5^4 6^4 | 2 | 198 P2_13 | (1/8, 1/6, 5/12) | 1 | 3 | 12 | 17 |
| `cb7114c8a5122943` | 16 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 2 | 214 I4_132 | (1/12, 1/8, 1/6) | 2 | 1 | 24 | 2 |
| `ea1baec328356a32` | 16 | (25, 39, 16) | 4^12 6^3 12^1 | 6 | 201 Pn-3 | (1/12, 1/12, 1/12) | 3 | 1 | 8 | 20 |
| `37c8918c625da53c` | 16 | (26, 40, 16) | 4^10 5^2 6^1 7^2 10^1 | 1 | 214 I4_132 | (1/8, 1/4, 1/6) | 1 | 3 | 48 | 1 |
| `f0163697449d793a` | 16 | (26, 40, 16) | 4^8 5^4 7^4 | 2 | 199 I2_13 | (0, 1/4, 1/12) | 2 | 1 | 12 | 4 |
| `998994bcf8df722b` | 17 | (30, 45, 17) | 4^12 6^2 10^3 | 12 | 206 Ia-3 | (1/12, 1/12, 1/12) | 3 | 1 | 16 | 5 |
| `8c69db9e84095469` | 17 | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 12 | 199 I2_13 | (1/8, 1/8, 1/8) | 3 | 1 | 8 | 6 |
| `c314dedd38208a2e` | 18 | (30, 46, 18) | 3^4 4^2 5^8 7^2 9^2 | 2 | 212 P4_332 | (1/12, 1/6, 1/8) | 2 | 1 | 12 | 4 |
| `afeb1ae44c1a3443` | 18 | (32, 48, 18) | 4^12 8^6 | 6 | 198 P2_13 | (1/8, 1/8, 1/8) | 3 | 1 | 4 | 8 |
| `3497979d000ba708` | 19 | (30, 47, 19) | 3^6 4^5 5^4 6^2 12^2 | 1 | 214 I4_132 | (1/12, 3/8, 1/6) | 1 | 3 | 48 | 1 |
| `df70dc799acd7711` | 19 | (28, 45, 19) | 3^6 4^5 5^2 6^4 8^1 10^1 | 1 | 213 P4_132 | (1/8, 1/4, 1/6) | 1 | 3 | 24 | 1 |
| `aa6b0077c3234d24` | 19 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 2 | 214 I4_132 | (0, 1/4, 1/12) | 2 | 1 | 24 | 2 |
| `fd96e7fc36481986` | 20 | (36, 54, 20) | 3^12 6^2 10^6 | 12 | 199 I2_13 | (1/12, 1/12, 1/12) | 3 | 1 | 8 | 4 |
| `ceb70631e274e727` | 22 | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | 212 P4_332 | (1/12, 1/12, 1/12) | 3 | 1 | 8 | 4 |
| `359beee832567a71` | 23 | (40, 61, 23) | 4^20 11^2 20^1 | 4 | 230 Ia-3d | (1/12, 1/6, 1/8) | 2 | 1 | 48 | 1 |

## Quarantines (0)

None. No >38-facet sighting, no float/exact disagreement, no crash, no Fedorov violation, no stab/aut inconsistency.

## Honest limits (what this sweep did NOT do)

- Denominators: special positions scanned only with per-coordinate denominators in {2,3,4,6,8,12}. Fixed Wyckoff points of cubic groups all have such coordinates in the IT setting (spot-belief, not verified against ITA tables); Wyckoff LINES/PLANES are only SAMPLED at these rational grid points — strata thinner than the grid, and line regions between samples, are not covered. No transition bisection (design §2.3) was run in this phase.
- General positions: 2 rational controls per group, not the design's N=8 grid (that general-position sweep remains open; Schmitt's survey already covers general position densely — the corridor rationale here was special positions).
- One exact cell per orbit (congruence argument above); the other cells were float-checked only.
- Aut orders are combinatorial map automorphism counts; geometric stabilizer certification is G4/V2, not claimed.
- Type identity relies on canon_code (unit-tested in test_canon.py, G2-exercised); f/p-vector collisions between distinct codes are expected and are NOT merged.
- Budget NOT hit: all 36 cubic groups completed; nothing was cut.

Run wall time: 215 s (single process, deterministic order; phase1_types.json contains no timings and is byte-identical across re-runs).

## Run log

```
PHASE 1 cubic sweep — start (budget 6000 s)
seeded 5 parallelohedra from seed_catalog.json
seeded josehedron (recomputed): f=(12, 22, 12), p=3^4 4^8, aut=4
seeded schmitt220 representative (recomputed): f=(12, 22, 12), p=3^6 4^4 5^2, aut=1
#198 P2_13    [corridor] orbits=  18 (skip 0) exact=  18 lat= 4 types=  4 new=  2 quar=0 maxF=18  [0.6s]
#199 I2_13    [corridor] orbits=  26 (skip 0) exact=  26 lat= 2 types=  8 new=  6 quar=0 maxF=20  [2.3s]
#205 Pa-3     [corridor] orbits=  11 (skip 0) exact=  11 lat= 3 types=  5 new=  3 quar=0 maxF=16  [0.8s]
#206 Ia-3     [corridor] orbits=  15 (skip 0) exact=  15 lat= 2 types=  7 new=  6 quar=0 maxF=17  [2.6s]
#212 P4_332   [corridor] orbits=  25 (skip 0) exact=  25 lat= 0 types= 11 new=  5 quar=0 maxF=22  [2.3s]
#213 P4_132   [corridor] orbits=  25 (skip 0) exact=  25 lat= 0 types= 11 new=  1 quar=0 maxF=22  [2.4s]
#214 I4_132   [corridor] orbits=  28 (skip 0) exact=  28 lat= 1 types= 13 new=  7 quar=0 maxF=19  [5.2s]
#220 I-43d    [corridor] orbits=  15 (skip 0) exact=  15 lat= 1 types= 10 new=  5 quar=0 maxF=17  [2.6s]
#195 P23                 orbits=  48 (skip 0) exact=  48 lat= 4 types=  6 new=  3 quar=0 maxF=13  [1.3s]
#196 F23                 orbits=  32 (skip 0) exact=  32 lat= 4 types=  4 new=  0 quar=0 maxF=12  [3.1s]
#197 I23                 orbits=  25 (skip 0) exact=  25 lat= 2 types=  8 new=  6 quar=0 maxF=15  [1.9s]
#200 Pm-3                orbits= 139 (skip 0) exact= 139 lat= 3 types=  7 new=  3 quar=0 maxF=10  [6.2s]
#201 Pn-3                orbits=  26 (skip 0) exact=  26 lat= 3 types=  9 new=  3 quar=0 maxF=16  [2.0s]
#202 Fm-3                orbits=  46 (skip 0) exact=  46 lat= 3 types=  7 new=  0 quar=0 maxF=12  [9.6s]
#203 Fd-3                orbits=  18 (skip 0) exact=  18 lat= 1 types=  8 new=  3 quar=0 maxF=16  [4.8s]
#204 Im-3                orbits=  71 (skip 0) exact=  71 lat= 2 types= 17 new=  8 quar=0 maxF=14  [8.6s]
#207 P432                orbits=  48 (skip 0) exact=  48 lat= 3 types=  6 new=  1 quar=0 maxF= 9  [1.8s]
#208 P4_232              orbits=  39 (skip 0) exact=  39 lat= 3 types= 10 new=  3 quar=0 maxF=16  [3.1s]
#209 F432                orbits=  28 (skip 0) exact=  28 lat= 3 types=  6 new=  1 quar=0 maxF=12  [4.9s]
#210 F4_132              orbits=  24 (skip 0) exact=  24 lat= 1 types=  9 new=  0 quar=0 maxF=16  [6.7s]
#211 I432                orbits=  32 (skip 0) exact=  32 lat= 2 types= 15 new=  3 quar=0 maxF=14  [3.7s]
#215 P-43m               orbits= 139 (skip 0) exact= 139 lat= 4 types=  8 new=  0 quar=0 maxF=12  [6.7s]
#216 F-43m               orbits=  68 (skip 0) exact=  68 lat= 4 types=  5 new=  0 quar=0 maxF=12  [10.9s]
#217 I-43m               orbits=  71 (skip 0) exact=  71 lat= 2 types= 14 new=  2 quar=0 maxF=15  [8.6s]
#218 P-43n               orbits=  26 (skip 0) exact=  26 lat= 2 types=  8 new=  1 quar=0 maxF=15  [2.0s]
#219 F-43c               orbits=  18 (skip 0) exact=  18 lat= 4 types=  5 new=  0 quar=0 maxF=12  [4.4s]
#221 Pm-3m               orbits= 132 (skip 0) exact= 132 lat= 3 types=  5 new=  0 quar=0 maxF= 8  [9.6s]
#222 Pn-3n               orbits=  26 (skip 0) exact=  26 lat= 2 types= 13 new=  1 quar=0 maxF=14  [2.9s]
#223 Pm-3n               orbits=  78 (skip 0) exact=  78 lat= 2 types= 20 new=  4 quar=0 maxF=14  [9.2s]
#224 Pn-3m               orbits=  78 (skip 0) exact=  78 lat= 3 types= 18 new=  4 quar=0 maxF=16  [9.2s]
#225 Fm-3m               orbits=  52 (skip 0) exact=  52 lat= 3 types=  6 new=  0 quar=0 maxF=12  [15.8s]
#226 Fm-3c               orbits=  30 (skip 0) exact=  30 lat= 3 types=  7 new=  1 quar=0 maxF= 9  [12.8s]
#227 Fd-3m               orbits=  39 (skip 0) exact=  39 lat= 1 types= 12 new=  1 quar=0 maxF=16  [16.2s]
#228 Fd-3c               orbits=  14 (skip 0) exact=  14 lat= 3 types=  8 new=  0 quar=0 maxF=16  [9.0s]
#229 Im-3m               orbits=  71 (skip 0) exact=  71 lat= 2 types= 17 new=  3 quar=0 maxF=14  [13.6s]
#230 Ia-3d               orbits=  16 (skip 0) exact=  16 lat= 1 types= 16 new=  9 quar=0 maxF=23  [6.5s]

DONE in 215s: 1597 orbits tried, 102 types in store (7 seeded + 95 not matched against catalog snapshot of 2026-08-28), max stored facets 23, 0 quarantines, budget_hit=False
wrote phase1_types.json (102 types, 1597 orbit records)
```
