# Computed open/wall classification of the 165 G4-certified phase-2 cells (14 tetragonal + 151 hexagonal-family) — 2026-09-04

AI disclosure: computed and written by an AI subagent (Claude Fable 5.1, #148) under the scheme pre-registered in ANCHORS.md by the same agent before the run; PROVISIONAL until the main session re-runs `wall_open_phase2.py --fresh` and reproduces the JSON md5 below. Nothing here is a novelty or naming claim.

Pre-registered scheme: `../../ANCHORS.md`, block "PERTURBATION CLASSIFICATION, PHASE 2 — pre-registered 2026-09-04" (appended before this run). Generator: `wall_open_phase2.py` (this file's sibling). Chain: the ACCEPTED `sweep_phase2_tetragonal.evaluate` / `sweep_phase2_hexagonal.evaluate` (orbit -> Gram with R^T G R = G asserted -> float proposal -> exact clip with the 4 rho^2 <= D^2 certificate -> canonical code; orbit congruence; G3 invariant: float/exact agreement or degeneracy flag with exact superseding, recorded per perturbed cell; kill criteria live). Stores read-only (`phase2_types.json` sha256 71685b9ab41b4dc0..., `phase2_hexagonal_types.json` sha256 7494c7b26114a68f...; unchanged after the run: True).

**Scheme (verbatim from the pre-registration).** POINT: tangent basis of the witness stratum (c1 `nullspace_basis`, verbatim), steps delta in {-1/48, -1/96, 1/96, 1/48} (fractional coordinates of the ITA conventional cell; hexagonal basis for IT 143-194), refinement halving to 1/1536 on any side whose smallest step is not SAME; dim 0 => point direction not applicable. METRIC: c/a -> c/a * (1 + eps), eps in {-1/96, -1/192, 1/192, 1/96} (relative), refinement halving to 1/3072. Side status at the finest step: SAME / DIFFERENT / QUARANTINE; a direction is WALL when both sides are DIFFERENT. Verdicts per c1 lines 103-109: OPEN = every side SAME; WALL = some direction WALL; ONE-SIDED = otherwise; INDETERMINATE = a side ended in QUARANTINE. POINT and METRIC verdicts are reported separately; the COMBINED verdict (over all applicable directions) is the classification compared with the carried heuristic label. Flags (never verdict inputs): LINE-ISOLATED = dim 1 and the point direction is WALL; NON-SIMPLE-VERTEX = nonsimple_vertices > 0 at the witness; STAB-CHANGE = a perturbed point with a different site-stabilizer order. Off-stratum rows (special positions, +-1/96 along a generic direction) are supplementary and not verdict inputs.

**Language (stated once).** OPEN means the type holds on the tested neighbourhood, not an interval proof. No naming here. Every type stays "not matched against the records checked as of 2026-09-04"; a neighbour's "Schmitt-printed TYPE" status means the stored type has a pass-P2 sighting (Schmitt's printed representative cell for that (group, b, point) reproduced by the chain with the same canonical code); "f printed" is the weaker f-vector-level fact against the accepted digitizations of his tetragonal / trigonal-hexagonal tables. Facet counts never exceeded 38 (kill bar live).

**Determinism.** `WALL_OPEN_PHASE2.json` (sorted keys, no timings) md5 = `6b257c551f6fb275dfabb03e992f57c2`; a second full run (`--fresh`) must reproduce it byte for byte (see the STATUS entry for the re-run record).

**Runtime.** 85 s wall for this invocation (8 forked workers; sum of per-cell walls 609 s); cells: 165 (0 crashed).

## Summary table (doc order: tetragonal verdict-table order, then hexagonal summary-table order)

| # | id | family | IT | c/a | f | dim | ns | previous heuristic label | POINT | METRIC | **COMPUTED (combined)** | flags | agree? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | tet | 92 P4_12_12 | 5/4 | (40, 60, 22) | 1 | 0 | OPEN (perturbation: point OPEN / b OPEN) | OPEN | OPEN | **OPEN** | - | yes |
| 3 | `f654982d74d740f6` | tet | 141 I4_1/amd | 1/2 | (38, 57, 21) | 2 | 0 | OPEN (perturbation: point OPEN / b OPEN) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 4 | `4f6d3e68cbd9e729` | tet | 98 I4_122 | 3/4 | (42, 63, 23) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 5 | `1497877268495988` | tet | 91 P4_122 | 1/2 | (32, 48, 18) | 1 | 0 | open-likely (triage, 7 b) | OPEN | OPEN | **OPEN** | - | yes |
| 6 | `e0d18e5ea938d649` | tet | 122 I-42d | 1 | (36, 54, 20) | 1 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 7 | `6797ab70c6015039` | tet | 76 P4_1 | 3/2 | (32, 48, 18) | 3 | 0 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 9 | `086ac96faf390886` | tet | 76 P4_1 | 7/5 | (36, 54, 20) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 10 | `164d4bd63d82d0c3` | tet | 76 P4_1 | 5/4 | (40, 60, 22) | 3 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | - | yes |
| 11 | `5dc2479b9bc14edc` | tet | 98 I4_122 | 9/16 | (42, 63, 23) | 3 | 0 | open-likely (triage, 3 b; metric-thin P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 12 | `3ebbca7ed2eda199` | tet | 98 I4_122 | 1/2 | (40, 60, 22) | 3 | 0 | indeterminate (triage, 2 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | n/a |
| 13 | `7575121042ade3b3` | tet | 98 I4_122 | 7/4 | (32, 48, 18) | 1 | 0 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | - | yes |
| 14 | `213c7a114d5a97a8` | tet | 98 I4_122 | 11/16 | (42, 63, 23) | 3 | 0 | indeterminate (triage, 2 b; metric-thin P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | n/a |
| 15 | `2e8e49eb28497267` | tet | 95 P4_322 | 53/40 | (40, 60, 22) | 3 | 0 | open-likely (triage, 4 b; metric-thin P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 2 | `49cedbdd58376fac` | tet | 92 P4_12_12 | 19/16 | (44, 66, 24) | 1 | 0 | WALL/THIN BAND (perturbation: point WALL to 1/1536 / b OPEN) | WALL [[1, 1, 0]] | OPEN | **WALL** | line_isolated | yes |
| 1 | `c49077384aaebeb0` | hex | 178 P6_122 | 5/4 | (44, 66, 24) | 1 | 0 | open-likely (triage, 12 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 2 | `59585d778cb3a7a4` | hex | 178 P6_122 | 3/4 | (40, 60, 22) | 1 | 0 | open-likely (triage, 22 b) | OPEN | OPEN | **OPEN** | - | yes |
| 3 | `095ce61d28388c98` | hex | 178 P6_122 | 1 | (40, 60, 22) | 1 | 0 | open-likely (triage, 24 b) | OPEN | OPEN | **OPEN** | - | yes |
| 4 | `9be0f2271a14b6a9` | hex | 178 P6_122 | 1 | (36, 54, 20) | 1 | 0 | open-likely (triage, 20 b) | OPEN | OPEN | **OPEN** | - | yes |
| 5 | `2d654c836f3731c6` | hex | 178 P6_122 | 1 | (36, 54, 20) | 1 | 0 | open-likely (triage, 30 b) | OPEN | OPEN | **OPEN** | - | yes |
| 6 | `b0f80776885f3ae1` | hex | 178 P6_122 | 1/2 | (36, 54, 20) | 1 | 0 | open-likely (triage, 17 b) | OPEN | OPEN | **OPEN** | - | yes |
| 7 | `a348875c3f707895` | hex | 178 P6_122 | 1/2 | (36, 54, 20) | 1 | 0 | open-likely (triage, 21 b) | OPEN | OPEN | **OPEN** | - | yes |
| 8 | `dcc38ea9177089b9` | hex | 178 P6_122 | 1/2 | (36, 54, 20) | 1 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | - | yes |
| 9 | `5b86a254c715306c` | hex | 169 P6_1 | 797/1000 | (40, 60, 22) | 3 | 0 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | - | yes |
| 10 | `f05f0b009e0929f6` | hex | 169 P6_1 | 3/4 | (32, 48, 18) | 3 | 0 | open-likely (triage, 39 b) | OPEN | OPEN | **OPEN** | - | yes |
| 11 | `d70e6901953070e7` | hex | 155 R32 | 3/4 | (38, 58, 22) | 3 | 2 | open-likely (triage, 3 b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any, nonsimple_vertex | NO |
| 12 | `e1a38303b2378f17` | hex | 169 P6_1 | 1277/2000 | (40, 60, 22) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 13 | `c82ebc15c49c1413` | hex | 154 P3_221 | 527/1000 | (38, 57, 21) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 14 | `f6f8b3050a1eef42` | hex | 178 P6_122 | 3/4 | (38, 57, 21) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 15 | `9c0b7e0c29dfebb2` | hex | 169 P6_1 | 3/4 | (36, 54, 20) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 16 | `87c94384d7851cb2` | hex | 155 R32 | 797/1000 | (34, 52, 20) | 3 | 2 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 17 | `a35623e347ef03b4` | hex | 169 P6_1 | 5/4 | (32, 48, 18) | 3 | 0 | open-likely (triage, 32 b) | OPEN | OPEN | **OPEN** | - | yes |
| 18 | `e98412e7cb95aea2` | hex | 152 P3_121 | 3/4 | (32, 48, 18) | 1 | 0 | open-likely (triage, 30 b) | OPEN | OPEN | **OPEN** | - | yes |
| 19 | `ac4489d658eb445e` | hex | 178 P6_122 | 797/1000 | (36, 54, 20) | 3 | 0 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 20 | `c53bc05bc306c97d` | hex | 166 R-3m | 7/8 | (31, 48, 19) | 2 | 3 | open-likely (triage, 14 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 21 | `8cc8c5ab3cf36d8f` | hex | 178 P6_122 | 5/4 | (36, 54, 20) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 22 | `646b518ccf3bd724` | hex | 169 P6_1 | 15/16 | (36, 54, 20) | 3 | 0 | open-likely (triage, 6 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 23 | `7a448bed1119dfad` | hex | 178 P6_122 | 1/2 | (36, 54, 20) | 3 | 0 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 24 | `7e023be581e7c50a` | hex | 154 P3_221 | 3/4 | (36, 54, 20) | 3 | 0 | open-likely (triage, 4 b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any | NO |
| 25 | `7e05ce00d8a7cbf6` | hex | 178 P6_122 | 137/160 | (38, 57, 21) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 26 | `59b28b3a59c27092` | hex | 155 R32 | 1277/2000 | (34, 52, 20) | 3 | 2 | open-likely (triage, 6 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 27 | `d9ac68100a276dfe` | hex | 169 P6_1 | 2777/4000 | (36, 54, 20) | 3 | 0 | open-likely (triage, 3 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 28 | `6f4101f83371033d` | hex | 169 P6_1 | 2331/4000 | (36, 54, 20) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 29 | `f0b07b168368759b` | hex | 148 R-3 | 3/4 | (14, 24, 12) | 0 | 6 | open-likely (triage, 41 b) | n/a | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 30 | `56918d2cff883e22` | hex | 148 R-3 | 1 | (22, 34, 14) | 3 | 2 | open-likely (triage, 49 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 31 | `f429e996b3f455a6` | hex | 148 R-3 | 3/4 | (26, 40, 16) | 3 | 2 | open-likely (triage, 16 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 32 | `71d2c9953ca110b8` | hex | 169 P6_1 | 39/32 | (36, 54, 20) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | - | NO |
| 33 | `8d90c524c89922d9` | hex | 169 P6_1 | 11/8 | (36, 54, 20) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | - | NO |
| 34 | `9d4396ca0b08fc3c` | hex | 166 R-3m | 3/4 | (19, 30, 13) | 2 | 3 | open-likely (triage, 63 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 35 | `07d543d89e2934f2` | hex | 152 P3_121 | 33/32 | (36, 54, 20) | 3 | 0 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | n/a |
| 36 | `2081d7b9a734e4fe` | hex | 155 R32 | 11/8 | (32, 50, 20) | 3 | 4 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | NO |
| 37 | `257b627a90b78038` | hex | 180 P6_222 | 1 | (22, 35, 15) | 1 | 4 | open-likely (triage, 24 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 38 | `3ddc41389e6d484f` | hex | 171 P6_2 | 1 | (32, 48, 18) | 3 | 0 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | - | yes |
| 39 | `64203f15fcf6c09b` | hex | 155 R32 | 1/2 | (20, 32, 14) | 1 | 4 | open-likely (triage, 23 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 40 | `d718e083bd23d2b1` | hex | 178 P6_122 | 1 | (32, 48, 18) | 3 | 0 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | - | yes |
| 41 | `f14a8c4e7c5b3e3a` | hex | 180 P6_222 | 7/4 | (32, 48, 18) | 3 | 0 | open-likely (triage, 10 b) | OPEN | OPEN | **OPEN** | - | yes |
| 42 | `29bbba1adec778da` | hex | 171 P6_2 | 5/4 | (28, 42, 16) | 3 | 0 | open-likely (triage, 15 b) | OPEN | OPEN | **OPEN** | - | yes |
| 43 | `66563d07a1110a25` | hex | 154 P3_221 | 1 | (36, 54, 20) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any | NO |
| 44 | `ce3b42c8a4ceff6f` | hex | 151 P3_112 | 1/2 | (34, 51, 19) | 3 | 0 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | - | yes |
| 45 | `7b9cfe26fe4a9c4b` | hex | 146 R3 | 5/4 | (18, 30, 14) | 3 | 6 | open-likely (triage, 32 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 46 | `2b9726574a0a8bed` | hex | 171 P6_2 | 1/2 | (30, 45, 17) | 3 | 0 | open-likely (triage, 9 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 47 | `f07d69523ef41b37` | hex | 178 P6_122 | 3/2 | (20, 36, 18) | 1 | 12 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 2, 0]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 48 | `16025e0680843c36` | hex | 169 P6_1 | 1 | (32, 48, 18) | 3 | 0 | open-likely (triage, 7 b) | OPEN | OPEN | **OPEN** | - | yes |
| 49 | `d10bb4a25bbf4c80` | hex | 154 P3_221 | 797/1000 | (32, 48, 18) | 3 | 0 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 50 | `e0bf1a48f096c10d` | hex | 180 P6_222 | 1 | (32, 48, 18) | 3 | 0 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 51 | `b2430fc4bea4e06d` | hex | 154 P3_221 | 1/2 | (34, 51, 19) | 3 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 52 | `bff9b24ce78050f5` | hex | 144 P3_1 | 1 | (28, 42, 16) | 3 | 0 | open-likely (triage, 9 b) | OPEN | OPEN | **OPEN** | - | yes |
| 53 | `4db369a636f4396b` | hex | 151 P3_112 | 3/2 | (18, 30, 14) | 1 | 6 | indeterminate (triage, 2 b) | WALL [[2, 1, 0]] | WALL | **WALL** | line_isolated, nonsimple_vertex | n/a |
| 54 | `042c19cbfdc869cb` | hex | 178 P6_122 | 3/2 | (32, 48, 18) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 55 | `23594bd7053503aa` | hex | 153 P3_212 | 1 | (32, 48, 18) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 56 | `f5fbebffa76808d5` | hex | 179 P6_522 | 5/4 | (31, 47, 18) | 3 | 1 | open-likely (triage, 5 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 57 | `057255f61286b052` | hex | 167 R-3c | 1/2 | (24, 38, 16) | 1 | 4 | open-likely (triage, 7 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 58 | `e198aac88f223892` | hex | 153 P3_212 | 3/4 | (30, 45, 17) | 3 | 0 | open-likely (triage, 12 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 59 | `d07f950b8309de82` | hex | 171 P6_2 | 67/80 | (30, 45, 17) | 3 | 0 | open-likely (triage, 5 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 60 | `a182e87006c7a00d` | hex | 179 P6_522 | 3/2 | (32, 48, 18) | 3 | 0 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 61 | `a46cbaad3c23e834` | hex | 155 R32 | 1/2 | (32, 49, 19) | 3 | 2 | indeterminate (triage, 2 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 62 | `dd3fb07fe11d73d3` | hex | 179 P6_522 | 2 | (31, 47, 18) | 3 | 1 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 63 | `36c92427e3d084dc` | hex | 166 R-3m | 5/4 | (19, 30, 13) | 2 | 3 | open-likely (triage, 16 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 64 | `bc59e5d778f60d1f` | hex | 178 P6_122 | 3/4 | (29, 44, 17) | 3 | 1 | open-likely (triage, 7 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 65 | `cbead3df2d2f1d0e` | hex | 154 P3_221 | 1277/2000 | (34, 51, 19) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 66 | `85244add8d1f2d55` | hex | 169 P6_1 | 1/2 | (32, 48, 18) | 3 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | - | yes |
| 67 | `2165f5c5260120de` | hex | 152 P3_121 | 527/1000 | (30, 45, 17) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 68 | `437fbe758a6dd8e3` | hex | 179 P6_522 | 1/2 | (32, 48, 18) | 3 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | - | yes |
| 69 | `36ec4ad2f530e145` | hex | 151 P3_112 | 3/4 | (30, 45, 17) | 3 | 0 | open-likely (triage, 9 b) | OPEN | OPEN | **OPEN** | - | yes |
| 70 | `fcffad0da2b5b62f` | hex | 154 P3_221 | 15/16 | (32, 48, 18) | 3 | 0 | open-likely (triage, 6 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 71 | `505a4911e298c933` | hex | 181 P6_422 | 2 | (28, 42, 16) | 3 | 0 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | - | yes |
| 72 | `24a6b511067d37b2` | hex | 178 P6_122 | 5/4 | (30, 45, 17) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | - | yes |
| 73 | `30f2a1e483babf55` | hex | 178 P6_122 | 11/4 | (29, 44, 17) | 3 | 1 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 74 | `37aa18e6e10583be` | hex | 155 R32 | 9/8 | (30, 47, 19) | 3 | 4 | open-likely (triage, 3 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 75 | `7715c7010e513b71` | hex | 181 P6_422 | 1 | (30, 45, 17) | 3 | 0 | open-likely (triage, 8 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 76 | `0b5d9beb0fc972f6` | hex | 179 P6_522 | 13/8 | (32, 48, 18) | 3 | 0 | open-likely (triage, 5 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 77 | `322d5ff451e4101d` | hex | 169 P6_1 | 11/8 | (32, 48, 18) | 3 | 0 | indeterminate (triage, 3 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | n/a |
| 78 | `34351050a4f29035` | hex | 178 P6_122 | 1 | (28, 42, 16) | 3 | 0 | open-likely (triage, 11 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 79 | `c0071756347c5a8a` | hex | 144 P3_1 | 1 | (28, 42, 16) | 3 | 0 | open-likely (triage, 9 b) | OPEN | OPEN | **OPEN** | - | yes |
| 80 | `d9bf7fb7a80eaa38` | hex | 155 R32 | 5/4 | (30, 47, 19) | 3 | 4 | indeterminate (triage, 2 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 81 | `847d2695a14ae424` | hex | 152 P3_121 | 5/4 | (29, 44, 17) | 3 | 1 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 82 | `090dcafb7ce9cb08` | hex | 166 R-3m | 1/2 | (20, 32, 14) | 2 | 4 | open-likely (triage, 6 b) | WALL [[1, 2, 0], [0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 83 | `9bc4922a7b574aa6` | hex | 166 R-3m | 3/4 | (17, 28, 13) | 2 | 5 | open-likely (triage, 10 b) | WALL [[1, 2, 0], [0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 84 | `43e4e46001b4d8b9` | hex | 181 P6_422 | 31/16 | (32, 48, 18) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | yes |
| 85 | `af8b2135c913b13b` | hex | 181 P6_422 | 7/8 | (32, 48, 18) | 3 | 0 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | - | yes |
| 86 | `74a69fba4266de3b` | hex | 167 R-3c | 527/1000 | (28, 43, 17) | 3 | 2 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 87 | `c3b4b14633c9d4d5` | hex | 155 R32 | 1 | (28, 43, 17) | 3 | 2 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 88 | `e19babba732f5fd4` | hex | 179 P6_522 | 7/4 | (29, 44, 17) | 3 | 1 | open-likely (triage, 3 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 89 | `7472d8ba000c8056` | hex | 152 P3_121 | 9/8 | (22, 36, 16) | 1 | 6 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | WALL [[0, 1, 0]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 90 | `d0c5a15c25ab6413` | hex | 152 P3_121 | 17/16 | (32, 48, 18) | 3 | 0 | open-likely (triage, 3 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 91 | `d770abfcee4deb90` | hex | 153 P3_212 | 19/16 | (32, 48, 18) | 3 | 0 | open-likely (triage, 3 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 92 | `4a560e459032166a` | hex | 154 P3_221 | 7/8 | (28, 42, 16) | 3 | 0 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 93 | `5beb94b61eb66eb1` | hex | 178 P6_122 | 1/2 | (27, 41, 16) | 3 | 1 | open-likely (triage, 5 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 94 | `95934e84555dc2ea` | hex | 179 P6_522 | 1/2 | (26, 40, 16) | 3 | 2 | open-likely (triage, 5 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 95 | `d0ed9179c6947b5f` | hex | 155 R32 | 1/2 | (16, 26, 12) | 3 | 3 | open-likely (triage, 25 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 96 | `0948aa6184f13a8a` | hex | 179 P6_522 | 5/4 | (30, 45, 17) | 3 | 0 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | - | yes |
| 97 | `272aefcd5e48ba49` | hex | 179 P6_522 | 9/8 | (29, 44, 17) | 3 | 1 | open-likely (triage, 5 b; metric-thin: P5-only) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 98 | `466b12546dd936c3` | hex | 161 R3c | 527/1000 | (26, 40, 16) | 3 | 2 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 99 | `4885ce1e70fa9713` | hex | 179 P6_522 | 3/4 | (27, 41, 16) | 3 | 1 | open-likely (triage, 7 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 100 | `3d6b109f392fda19` | hex | 154 P3_221 | 3/2 | (33, 50, 19) | 3 | 1 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | NO |
| 101 | `e598ffd8a1cac138` | hex | 144 P3_1 | 29/32 | (32, 48, 18) | 3 | 0 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | - | n/a |
| 102 | `a93f8fe7ecdc5851` | hex | 144 P3_1 | 9/8 | (32, 48, 18) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | - | NO |
| 103 | `aef8972953d53d20` | hex | 171 P6_2 | 81/64 | (32, 48, 18) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | - | NO |
| 104 | `72bcd959be4ab7dd` | hex | 152 P3_121 | 5/4 | (28, 42, 16) | 3 | 0 | open-likely (triage, 5 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | yes |
| 105 | `ab801b11bead62ef` | hex | 166 R-3m | 7/4 | (19, 30, 13) | 2 | 3 | open-likely (triage, 6 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 106 | `2c121297dbaa80af` | hex | 154 P3_221 | 1 | (28, 42, 16) | 3 | 0 | open-likely (triage, 7 b) | OPEN | OPEN | **OPEN** | - | yes |
| 107 | `9d0b36ad5caceb2e` | hex | 167 R-3c | 7/8 | (22, 35, 15) | 3 | 3 | open-likely (triage, 5 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 108 | `d176b8d859dd651a` | hex | 178 P6_122 | 5/2 | (32, 48, 18) | 3 | 0 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | degenerate_flag_any | NO |
| 109 | `60eb4282db04fca2` | hex | 179 P6_522 | 11/8 | (30, 45, 17) | 3 | 0 | open-likely (triage, 4 b; metric-thin: P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any | NO |
| 110 | `f43b45fd6383b36b` | hex | 155 R32 | 19/16 | (26, 41, 17) | 3 | 4 | open-likely (triage, 3 b; metric-thin: P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any, nonsimple_vertex | NO |
| 111 | `4ff9d77aa9f8194a` | hex | 167 R-3c | 3/4 | (24, 37, 15) | 3 | 2 | open-likely (triage, 8 b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any, nonsimple_vertex | NO |
| 112 | `6de3dac5f334cfed` | hex | 167 R-3c | 1/2 | (26, 40, 16) | 3 | 2 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 113 | `105e41c2798e6180` | hex | 148 R-3 | 2 | (16, 27, 13) | 1 | 4 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 114 | `542cbe76934b484b` | hex | 154 P3_221 | 5/4 | (29, 44, 17) | 3 | 1 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | NO |
| 115 | `75bbbcb4a37e70e8` | hex | 146 R3 | 67/80 | (27, 41, 16) | 3 | 1 | open-likely (triage, 4 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 116 | `cff2d5fb5e0d4149` | hex | 171 P6_2 | 1/2 | (23, 35, 14) | 3 | 1 | open-likely (triage, 4 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 117 | `4b6055c7aa3d341b` | hex | 178 P6_122 | 17/8 | (25, 38, 15) | 3 | 1 | open-likely (triage, 4 b; metric-thin: P5-only) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 118 | `7e79f1c38b5516bf` | hex | 178 P6_122 | 3/2 | (22, 34, 14) | 1 | 2 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[0, 1, 0]] | WALL | **WALL** | line_isolated, nonsimple_vertex | yes |
| 119 | `d7c638d7fa23127e` | hex | 169 P6_1 | 3/2 | (25, 39, 16) | 3 | 3 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 120 | `0417061f8f56488e` | hex | 152 P3_121 | 1/2 | (20, 32, 14) | 3 | 4 | open-likely (triage, 9 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 121 | `6cc34ed38aa354e1` | hex | 181 P6_422 | 1/2 | (22, 34, 14) | 3 | 2 | open-likely (triage, 4 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 122 | `5838282f46223111` | hex | 152 P3_121 | 7/4 | (29, 44, 17) | 3 | 1 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | NO |
| 123 | `cda1d1c03659b67d` | hex | 148 R-3 | 527/1000 | (22, 34, 14) | 3 | 2 | open-likely (triage, 7 b) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | yes |
| 124 | `161b09808f4c1863` | hex | 178 P6_122 | 2 | (18, 30, 14) | 1 | 6 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[0, 1, 0]] | WALL | **WALL** | line_isolated, nonsimple_vertex | yes |
| 125 | `c92eef8763d02d8a` | hex | 179 P6_522 | 3/2 | (25, 39, 16) | 3 | 3 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 126 | `3a491fd6426d90b2` | hex | 146 R3 | 33/32 | (24, 38, 16) | 3 | 4 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 127 | `5b679d8b0a3147c3` | hex | 152 P3_121 | 17/16 | (24, 38, 16) | 3 | 4 | indeterminate (triage, 2 b; metric-thin: P5-only) | WALL [[0, 0, 1]] | ONE-SIDED | **WALL** | degenerate_flag_any, nonsimple_vertex | n/a |
| 128 | `fac4317d5a65b959` | hex | 148 R-3 | 9/8 | (24, 38, 16) | 3 | 4 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 129 | `27d463eac6cda5ea` | hex | 171 P6_2 | 5331/8000 | (27, 41, 16) | 3 | 1 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 130 | `919d30fd9021b5ee` | hex | 154 P3_221 | 51/32 | (25, 38, 15) | 3 | 1 | open-likely (triage, 3 b; metric-thin: P5-only) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 131 | `6074c5fa5d2dffc5` | hex | 148 R-3 | 3/4 | (16, 26, 12) | 3 | 3 | open-likely (triage, 19 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 132 | `5e68ffe7582a0657` | hex | 167 R-3c | 1/2 | (20, 31, 13) | 3 | 2 | open-likely (triage, 8 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 133 | `1ba26ab2c0999b93` | hex | 148 R-3 | 1/2 | (20, 32, 14) | 3 | 3 | open-likely (triage, 4 b) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | NO |
| 134 | `27dbb77012555d28` | hex | 161 R3c | 4439/8000 | (26, 40, 16) | 3 | 2 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | NO |
| 135 | `c18a9b1cb2a5d168` | hex | 148 R-3 | 1/2 | (26, 40, 16) | 3 | 2 | wall-suspect (triage, 1 b; metric-thin: 1b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any, nonsimple_vertex | NO |
| 136 | `d1f1121757598de0` | hex | 154 P3_221 | 9/4 | (15, 25, 12) | 3 | 5 | indeterminate (triage, 2 b) | WALL [[1, 0, 0], [0, 1, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | n/a |
| 137 | `b27ba8dbcbc2891a` | hex | 161 R3c | 1/2 | (22, 34, 14) | 3 | 2 | open-likely (triage, 4 b) | ONE-SIDED | OPEN | **ONE-SIDED** | degenerate_flag_any, nonsimple_vertex | NO |
| 138 | `457c20cf036ae496` | hex | 180 P6_222 | 3/2 | (11, 20, 11) | 1 | 7 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 139 | `11a9fe078850b5cd` | hex | 179 P6_522 | 65/32 | (25, 38, 15) | 3 | 1 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 140 | `5f812747976b224a` | hex | 148 R-3 | 39/32 | (20, 32, 14) | 3 | 4 | indeterminate (triage, 2 b; metric-thin: P5-only) | OPEN | OPEN | **OPEN** | degenerate_flag_any, nonsimple_vertex | n/a |
| 141 | `c95a5fcf4d681568` | hex | 166 R-3m | 3/2 | (12, 21, 11) | 2 | 4 | indeterminate (triage, 2 b) | WALL [[1, 2, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | n/a |
| 142 | `f7bd7cd9eae6436b` | hex | 166 R-3m | 1 | (16, 27, 13) | 2 | 5 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 2, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 143 | `75c9be976d704515` | hex | 152 P3_121 | 9/8 | (18, 28, 12) | 1 | 2 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | WALL [[0, 1, 0]] | WALL | **WALL** | line_isolated, nonsimple_vertex | yes |
| 144 | `8463196a30c6643f` | hex | 179 P6_522 | 2 | (23, 36, 15) | 3 | 3 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 145 | `487490cdf474e568` | hex | 148 R-3 | 1277/2000 | (20, 32, 14) | 3 | 3 | indeterminate (triage, 2 b; metric-thin: P5-only) | WALL [[0, 0, 1]] | OPEN | **WALL** | degenerate_flag_any, nonsimple_vertex | n/a |
| 146 | `f0e2036d295195b4` | hex | 152 P3_121 | 9/8 | (12, 20, 10) | 1 | 4 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | WALL [[0, 1, 0]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 147 | `67b1ede4b021a4fc` | hex | 155 R32 | 3/2 | (17, 29, 14) | 3 | 5 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 148 | `34e5e7acce18b5cd` | hex | 166 R-3m | 3/2 | (14, 23, 11) | 2 | 4 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 2, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 149 | `fa9c370d30741970` | hex | 180 P6_222 | 3/2 | (9, 16, 9) | 1 | 5 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 2, 0]] | WALL | **WALL** | degenerate_flag_any, line_isolated, nonsimple_vertex | yes |
| 150 | `400cba5c78326d1d` | hex | 167 R-3c | 1 | (17, 28, 13) | 3 | 5 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0], [0, 0, 1]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |
| 151 | `78e755ffdff3a2f5` | hex | 146 R3 | 3/4 | (14, 24, 12) | 3 | 6 | wall-suspect (triage, 1 b; metric-thin: 1b) | WALL [[1, 0, 0], [0, 1, 0]] | WALL | **WALL** | degenerate_flag_any, nonsimple_vertex | yes |

## Aggregate (per verdict, per family)

- **tetragonal** (n = 14): COMBINED {'OPEN': 13, 'WALL': 1}; POINT {'OPEN': 13, 'WALL': 1}; METRIC {'OPEN': 14}; agreement with the heuristic label {'n/a': 2, 'yes': 12}; flags: line-isolated 1, non-simple-vertex 0, stab-change 0, float-superseded 0, quarantine 0.
- **hexagonal** (n = 151): COMBINED {'ONE-SIDED': 9, 'OPEN': 102, 'WALL': 40}; POINT {'ONE-SIDED': 9, 'OPEN': 101, 'WALL': 40, 'n/a': 1}; METRIC {'ONE-SIDED': 1, 'OPEN': 130, 'WALL': 20}; agreement with the heuristic label {'NO': 35, 'n/a': 14, 'yes': 102}; flags: line-isolated 10, non-simple-vertex 81, stab-change 0, float-superseded 0, quarantine 0.
- **all 165**: COMBINED {'ONE-SIDED': 9, 'OPEN': 115, 'WALL': 41}; agreement {'NO': 35, 'n/a': 16, 'yes': 114}.
- Non-simple vertices at the witness vs verdict (a non-simple vertex at a general position is expected to split under a generic move unless it is symmetry-forced, e.g. lies on a rotation axis of the group): OPEN with ns>0: 36, ns=0: 79; WALL with ns>0: 40, ns=0: 1; ONE-SIDED with ns>0: 5, ns=0: 4. WALL cells with ns = 0 (simple witness cell on a transition): ['49cedbdd58376fac'].
- Verdict step size in c/a: the relative verdict step 1/192 is <= 1/96 absolute for the 160 cells with c/a <= 2; the cells with c/a > 2 are `30f2a1e483babf55` (c/a 11/4, absolute step 11/768), `d176b8d859dd651a` (c/a 5/2, absolute step 5/384), `4b6055c7aa3d341b` (c/a 17/8, absolute step 17/1536), `d1f1121757598de0` (c/a 9/4, absolute step 3/256), `11a9fe078850b5cd` (c/a 65/32, absolute step 65/6144).

## Cells where the computed verdict contradicts the heuristic label (35)

| # | id | family | IT | c/a | previous label | POINT | METRIC | COMPUTED | reading |
|---|---|---|---|---|---|---|---|---|---|
| 11 | `d70e6901953070e7` | hex | 155 R32 | 3/4 | open-likely (triage, 3 b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |
| 24 | `7e023be581e7c50a` | hex | 154 P3_221 | 3/4 | open-likely (triage, 4 b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |
| 32 | `71d2c9953ca110b8` | hex | 169 P6_1 | 39/32 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted a wall; the type changes on one side only |
| 33 | `8d90c524c89922d9` | hex | 169 P6_1 | 11/8 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 36 | `2081d7b9a734e4fe` | hex | 155 R32 | 11/8 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 43 | `66563d07a1110a25` | hex | 154 P3_221 | 1 | wall-suspect (triage, 1 b; metric-thin: 1b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted a wall; the type changes on one side only |
| 56 | `f5fbebffa76808d5` | hex | 179 P6_522 | 5/4 | open-likely (triage, 5 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 64 | `bc59e5d778f60d1f` | hex | 178 P6_122 | 3/4 | open-likely (triage, 7 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 82 | `090dcafb7ce9cb08` | hex | 166 R-3m | 1/2 | open-likely (triage, 6 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 83 | `9bc4922a7b574aa6` | hex | 166 R-3m | 3/4 | open-likely (triage, 10 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 93 | `5beb94b61eb66eb1` | hex | 178 P6_122 | 1/2 | open-likely (triage, 5 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 94 | `95934e84555dc2ea` | hex | 179 P6_522 | 1/2 | open-likely (triage, 5 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 95 | `d0ed9179c6947b5f` | hex | 155 R32 | 1/2 | open-likely (triage, 25 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 97 | `272aefcd5e48ba49` | hex | 179 P6_522 | 9/8 | open-likely (triage, 5 b; metric-thin: P5-only) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 99 | `4885ce1e70fa9713` | hex | 179 P6_522 | 3/4 | open-likely (triage, 7 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 100 | `3d6b109f392fda19` | hex | 154 P3_221 | 3/2 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 102 | `a93f8fe7ecdc5851` | hex | 144 P3_1 | 9/8 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 103 | `aef8972953d53d20` | hex | 171 P6_2 | 81/64 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 107 | `9d0b36ad5caceb2e` | hex | 167 R-3c | 7/8 | open-likely (triage, 5 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 108 | `d176b8d859dd651a` | hex | 178 P6_122 | 5/2 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 109 | `60eb4282db04fca2` | hex | 179 P6_522 | 11/8 | open-likely (triage, 4 b; metric-thin: P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |
| 110 | `f43b45fd6383b36b` | hex | 155 R32 | 19/16 | open-likely (triage, 3 b; metric-thin: P5-only) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |
| 111 | `4ff9d77aa9f8194a` | hex | 167 R-3c | 3/4 | open-likely (triage, 8 b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |
| 114 | `542cbe76934b484b` | hex | 154 P3_221 | 5/4 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 117 | `4b6055c7aa3d341b` | hex | 178 P6_122 | 17/8 | open-likely (triage, 4 b; metric-thin: P5-only) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 120 | `0417061f8f56488e` | hex | 152 P3_121 | 1/2 | open-likely (triage, 9 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 121 | `6cc34ed38aa354e1` | hex | 181 P6_422 | 1/2 | open-likely (triage, 4 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 122 | `5838282f46223111` | hex | 152 P3_121 | 7/4 | wall-suspect (triage, 1 b; metric-thin: 1b) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 130 | `919d30fd9021b5ee` | hex | 154 P3_221 | 51/32 | open-likely (triage, 3 b; metric-thin: P5-only) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 131 | `6074c5fa5d2dffc5` | hex | 148 R-3 | 3/4 | open-likely (triage, 19 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 132 | `5e68ffe7582a0657` | hex | 167 R-3c | 1/2 | open-likely (triage, 8 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 133 | `1ba26ab2c0999b93` | hex | 148 R-3 | 1/2 | open-likely (triage, 4 b) | WALL | OPEN | **WALL** | label predicted open; the witness sits on a transition |
| 134 | `27dbb77012555d28` | hex | 161 R3c | 4439/8000 | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | OPEN | OPEN | **OPEN** | label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood |
| 135 | `c18a9b1cb2a5d168` | hex | 148 R-3 | 1/2 | wall-suspect (triage, 1 b; metric-thin: 1b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted a wall; the type changes on one side only |
| 137 | `b27ba8dbcbc2891a` | hex | 161 R3c | 1/2 | open-likely (triage, 4 b) | ONE-SIDED | OPEN | **ONE-SIDED** | label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall) |

Indeterminate labels resolved (n/a for agreement, 16): `3ebbca7ed2eda199` -> OPEN, `213c7a114d5a97a8` -> OPEN, `07d543d89e2934f2` -> OPEN, `4db369a636f4396b` -> WALL, `a46cbaad3c23e834` -> OPEN, `322d5ff451e4101d` -> OPEN, `d9bf7fb7a80eaa38` -> OPEN, `e598ffd8a1cac138` -> OPEN, `3a491fd6426d90b2` -> OPEN, `5b679d8b0a3147c3` -> WALL, `fac4317d5a65b959` -> OPEN, `27d463eac6cda5ea` -> OPEN, `d1f1121757598de0` -> WALL, `5f812747976b224a` -> OPEN, `c95a5fcf4d681568` -> WALL, `487490cdf474e568` -> WALL.

## Wall cells (41) and their neighbouring types (the naming-relevant fact)

For each wall direction the type on each side at the finest step is named by f-vector, p-vector, aut, non-simple count, stored id (union of the two phase-2 stores), whether that stored type is a Schmitt-printed TYPE (pass-P2 sighting, groups listed) and whether its f-vector is printed in the witness group's table.

**Wall-neighbour summary.** Wall-side cells at the finest step: {'stored': 125, 'not stored': 31}. Wall cells whose every wall-side neighbour is a stored type: 24; with at least one wall-side neighbour that is a Schmitt-printed TYPE: 25 (`49cedbdd58376fac`, `f07d69523ef41b37`, `4db369a636f4396b`, `090dcafb7ce9cb08`, `9bc4922a7b574aa6`, `7472d8ba000c8056`, `d0ed9179c6947b5f`, `105e41c2798e6180`, `7e79f1c38b5516bf`, `d7c638d7fa23127e`, `0417061f8f56488e`, `161b09808f4c1863`, `6074c5fa5d2dffc5`, `d1f1121757598de0`, `457c20cf036ae496`, `11a9fe078850b5cd`, `c95a5fcf4d681568`, `f7bd7cd9eae6436b`, `75c9be976d704515`, `f0e2036d295195b4`, `67b1ede4b021a4fc`, `34e5e7acce18b5cd`, `fa9c370d30741970`, `400cba5c78326d1d`, `78e755ffdff3a2f5`); with a wall-side neighbour that is itself one of the 165 certified cells: 16 (`49cedbdd58376fac`, `f07d69523ef41b37`, `9bc4922a7b574aa6`, `7472d8ba000c8056`, `5beb94b61eb66eb1`, `7e79f1c38b5516bf`, `d7c638d7fa23127e`, `0417061f8f56488e`, `c92eef8763d02d8a`, `5b679d8b0a3147c3`, `6074c5fa5d2dffc5`, `5e68ffe7582a0657`, `c95a5fcf4d681568`, `f7bd7cd9eae6436b`, `8463196a30c6643f`, `400cba5c78326d1d`); with a wall-side neighbour NOT in any store (a type the sweeps never sampled; recorded here only): 17 (`f5fbebffa76808d5`, `bc59e5d778f60d1f`, `5beb94b61eb66eb1`, `95934e84555dc2ea`, `d0ed9179c6947b5f`, `272aefcd5e48ba49`, `4885ce1e70fa9713`, `9d0b36ad5caceb2e`, `4b6055c7aa3d341b`, `6cc34ed38aa354e1`, `919d30fd9021b5ee`, `5e68ffe7582a0657`, `1ba26ab2c0999b93`, `11a9fe078850b5cd`, `8463196a30c6643f`, `487490cdf474e568`, `67b1ede4b021a4fc`). Previous label classes of the wall cells: {'carried WALL': 1, 'wall-suspect': 18, 'indeterminate': 5, 'open-likely': 17}.

### `49cedbdd58376fac` — tetragonal, IT(92) P4_12_12, witness (5/24, 5/24, 0) c/a = 19/16, f = (44, 66, 24) 3^10 4^4 6^4 7^2 12^4 aut 2, dim 1, ns 0; POINT WALL walls [[1, 1, 0]]; METRIC OPEN; flags: line_isolated; previous label: WALL/THIN BAND (perturbation: point WALL to 1/1536 / b OPEN)

- point (1, 1, 0) - side (finest step -1/1536, point = (319/1536, 319/1536, 0)): f=(40, 60, 22) 3^8 4^4 5^4 8^2 11^4 aut 2 ns 0 [4e9c9b076cfec323; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 1, 0) eps=-1/192, point(1, 1, 0) eps=-1/384, point(1, 1, 0) eps=-1/768, point(1, 1, 0) eps=-1/1536
- point (1, 1, 0) + side (finest step 1/1536, point = (107/512, 107/512, 0)): f=(36, 54, 20) 3^4 4^4 5^8 10^4 aut 8 ns 0 [60c6a7023f6e4280; Schmitt-printed TYPE in IT(109); f printed in witness group table: True] via point(1, 1, 0) eps=1/96, point(1, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 1, 0) eps=1/192, point(1, 1, 0) eps=1/384, point(1, 1, 0) eps=1/768, point(1, 1, 0) eps=1/1536
- all neighbouring types seen on-stratum (3): f=(32, 48, 18) 4^12 8^6 aut 6 ns 0 [afeb1ae44c1a3443; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 1, 0) eps=-1/48, point(1, 1, 0) eps=-1/96 ; f=(36, 54, 20) 3^4 4^4 5^8 10^4 aut 8 ns 0 [60c6a7023f6e4280; Schmitt-printed TYPE in IT(109); f printed in witness group table: True] via point(1, 1, 0) eps=1/96, point(1, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 1, 0) eps=1/192, point(1, 1, 0) eps=1/384, point(1, 1, 0) eps=1/768, point(1, 1, 0) eps=1/1536 ; f=(40, 60, 22) 3^8 4^4 5^4 8^2 11^4 aut 2 ns 0 [4e9c9b076cfec323; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 1, 0) eps=-1/192, point(1, 1, 0) eps=-1/384, point(1, 1, 0) eps=-1/768, point(1, 1, 0) eps=-1/1536

### `f07d69523ef41b37` — hexagonal, IT(178) P6_122, witness (1/6, 1/3, 1/4) c/a = 3/2, f = (20, 36, 18) 3^10 4^4 5^2 8^2 aut 2, dim 1, ns 12; POINT WALL walls [[1, 2, 0]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 2, 0) - side (finest step -1/1536, point = (85/512, 85/256, 1/4)): f=(30, 46, 18) 3^6 5^6 6^4 10^2 aut 2 ns 2 [254345236188cc50; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 2, 0) + side (finest step 1/1536, point = (257/1536, 257/768, 1/4)): f=(30, 46, 18) 3^6 5^6 6^4 10^2 aut 2 ns 2 [254345236188cc50; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(44, 66, 24) 3^8 4^2 5^6 6^4 9^2 14^2 aut 2 ns 0 [c49077384aaebeb0; not a Schmitt-printed type; f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(30, 46, 18) 3^6 5^6 6^4 10^2 aut 2 ns 2 [254345236188cc50; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(30, 46, 18) 3^6 5^6 6^4 10^2 aut 2 ns 2 [254345236188cc50; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(44, 66, 24) 3^8 4^2 5^6 6^4 9^2 14^2 aut 2 ns 0 [c49077384aaebeb0; not a Schmitt-printed type; f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `4db369a636f4396b` — hexagonal, IT(151) P3_112, witness (0, 1/2, 0) c/a = 3/2, f = (18, 30, 14) 3^4 4^6 6^4 aut 4, dim 1, ns 6; POINT WALL walls [[2, 1, 0]]; METRIC WALL; flags: line_isolated, nonsimple_vertex; previous label: indeterminate (triage, 2 b)

- point (2, 1, 0) - side (finest step -1/1536, point = (-1/768, 767/1536, 0)): f=(24, 36, 14) 4^4 5^4 6^6 aut 4 ns 0 [e948828e76447bbb; Schmitt-printed TYPE in IT(120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179); f printed in witness group table: True] via point(2, 1, 0) eps=-1/48, point(2, 1, 0) eps=-1/96, point(2, 1, 0) eps=1/96, point(2, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(2, 1, 0) eps=-1/192, point(2, 1, 0) eps=-1/384, point(2, 1, 0) eps=-1/768, point(2, 1, 0) eps=-1/1536, point(2, 1, 0) eps=1/192, point(2, 1, 0) eps=1/384, point(2, 1, 0) eps=1/768, point(2, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (2, 1, 0) + side (finest step 1/1536, point = (1/768, 769/1536, 0)): f=(24, 36, 14) 4^4 5^4 6^6 aut 4 ns 0 [e948828e76447bbb; Schmitt-printed TYPE in IT(120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179); f printed in witness group table: True] via point(2, 1, 0) eps=-1/48, point(2, 1, 0) eps=-1/96, point(2, 1, 0) eps=1/96, point(2, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(2, 1, 0) eps=-1/192, point(2, 1, 0) eps=-1/384, point(2, 1, 0) eps=-1/768, point(2, 1, 0) eps=-1/1536, point(2, 1, 0) eps=1/192, point(2, 1, 0) eps=1/384, point(2, 1, 0) eps=1/768, point(2, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 ns 0 [e5760549017956be; Schmitt-printed TYPE in IT(76, 78, 109, 151, 153); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(24, 36, 14) 4^4 5^4 6^6 aut 4 ns 0 [e948828e76447bbb; Schmitt-printed TYPE in IT(120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179); f printed in witness group table: True] via point(2, 1, 0) eps=-1/48, point(2, 1, 0) eps=-1/96, point(2, 1, 0) eps=1/96, point(2, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(2, 1, 0) eps=-1/192, point(2, 1, 0) eps=-1/384, point(2, 1, 0) eps=-1/768, point(2, 1, 0) eps=-1/1536, point(2, 1, 0) eps=1/192, point(2, 1, 0) eps=1/384, point(2, 1, 0) eps=1/768, point(2, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(24, 36, 14) 4^4 5^4 6^6 aut 4 ns 0 [e948828e76447bbb; Schmitt-printed TYPE in IT(120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179); f printed in witness group table: True] via point(2, 1, 0) eps=-1/48, point(2, 1, 0) eps=-1/96, point(2, 1, 0) eps=1/96, point(2, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(2, 1, 0) eps=-1/192, point(2, 1, 0) eps=-1/384, point(2, 1, 0) eps=-1/768, point(2, 1, 0) eps=-1/1536, point(2, 1, 0) eps=1/192, point(2, 1, 0) eps=1/384, point(2, 1, 0) eps=1/768, point(2, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 ns 0 [e5760549017956be; Schmitt-printed TYPE in IT(76, 78, 109, 151, 153); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `f5fbebffa76808d5` — hexagonal, IT(179) P6_522, witness (1/12, 3/8, 1/6) c/a = 5/4, f = (31, 47, 18) 3^3 4^2 5^7 6^3 7^2 10^1 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 5 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(36, 54, 20) 3^4 4^3 5^4 6^6 8^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(36, 54, 20) 3^4 4^3 5^4 6^5 7^2 8^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(28, 42, 16) 3^2 4^5 5^2 6^4 8^3 aut 1 ns 0 [34351050a4f29035; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96 ; f=(29, 44, 17) 3^3 4^3 5^3 6^5 7^2 8^1 aut 1 ns 1 [272aefcd5e48ba49; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=-1/48 ; f=(36, 54, 20) 3^4 4^3 5^4 6^5 7^2 8^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(40, 60, 22) 3^4 4^6 5^2 6^7 8^1 10^1 14^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48 ; f=(36, 54, 20) 3^4 4^3 5^4 6^6 8^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536

### `bc59e5d778f60d1f` — hexagonal, IT(178) P6_122, witness (1/8, 1/6, 5/12) c/a = 3/4, f = (29, 44, 17) 3^3 4^6 5^3 6^2 9^2 10^1 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 7 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(34, 51, 19) 3^4 4^7 6^4 8^1 9^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(34, 51, 19) 3^4 4^5 5^4 6^3 10^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(26, 39, 15) 4^7 5^2 6^4 8^2 aut 4 ns 0 [59f890334e777569; Schmitt-printed TYPE in IT(181); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48 ; f=(23, 36, 15) 3^2 4^8 6^3 8^2 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/48 ; f=(27, 41, 16) 3^3 4^7 6^2 7^1 8^1 9^2 aut 1 ns 1 [5beb94b61eb66eb1; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96 ; f=(34, 51, 19) 3^4 4^7 6^4 8^1 9^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(34, 51, 19) 3^4 4^5 5^4 6^3 10^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `090dcafb7ce9cb08` — hexagonal, IT(166) R-3m, witness (1/24, 1/12, 11/24) c/a = 1/2, f = (20, 32, 14) 3^2 4^9 7^2 8^1 aut 2, dim 2, ns 4; POINT WALL walls [[1, 2, 0], [0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 6 b)

- point (1, 2, 0) - side (finest step -1/1536, point = (21/512, 21/256, 11/24)): f=(30, 46, 18) 3^4 4^7 6^4 8^2 12^1 aut 2 ns 2 [88da140bdfed6c6d; Schmitt-printed TYPE in IT(167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (1, 2, 0) + side (finest step 1/1536, point = (65/1536, 65/768, 11/24)): f=(34, 52, 20) 3^4 4^9 5^4 10^2 16^1 aut 2 ns 2 [ff65c54d78bb4e50; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- point (0, 0, 1) - side (finest step -1/1536, point = (1/24, 1/12, 703/1536)): f=(30, 46, 18) 3^4 4^7 6^4 8^2 12^1 aut 2 ns 2 [88da140bdfed6c6d; Schmitt-printed TYPE in IT(167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/24, 1/12, 235/512)): f=(34, 52, 20) 3^4 4^9 5^4 10^2 16^1 aut 2 ns 2 [ff65c54d78bb4e50; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(27, 42, 17) 3^8 5^2 6^4 7^2 12^1 aut 2 ns 3 [991a5023fc8d713a; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48 ; f=(30, 46, 18) 3^4 4^7 6^4 8^2 12^1 aut 2 ns 2 [88da140bdfed6c6d; Schmitt-printed TYPE in IT(167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(38, 58, 22) 3^8 4^8 6^3 12^2 18^1 aut 2 ns 2 [1b1288f460af270d; Schmitt-printed TYPE in IT(166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48 ; f=(25, 40, 17) 3^8 4^2 6^6 12^1 aut 2 ns 5 [a66305b551fd919e; Schmitt-printed TYPE in IT(166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(34, 52, 20) 3^4 4^9 5^4 10^2 16^1 aut 2 ns 2 [ff65c54d78bb4e50; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `9bc4922a7b574aa6` — hexagonal, IT(166) R-3m, witness (1/24, 1/12, 11/24) c/a = 3/4, f = (17, 28, 13) 3^4 4^4 5^4 8^1 aut 2, dim 2, ns 5; POINT WALL walls [[1, 2, 0], [0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 10 b)

- point (1, 2, 0) - side (finest step -1/1536, point = (21/512, 21/256, 11/24)): f=(27, 42, 17) 3^8 5^2 6^4 7^2 12^1 aut 2 ns 3 [991a5023fc8d713a; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (1, 2, 0) + side (finest step 1/1536, point = (65/1536, 65/768, 11/24)): f=(31, 48, 19) 3^4 4^8 5^4 8^2 16^1 aut 2 ns 3 [c53bc05bc306c97d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(0, 0, 1) eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- point (0, 0, 1) - side (finest step -1/1536, point = (1/24, 1/12, 703/1536)): f=(27, 42, 17) 3^8 5^2 6^4 7^2 12^1 aut 2 ns 3 [991a5023fc8d713a; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/24, 1/12, 235/512)): f=(31, 48, 19) 3^4 4^8 5^4 8^2 16^1 aut 2 ns 3 [c53bc05bc306c97d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(0, 0, 1) eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 [9d4396ca0b08fc3c; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48 ; f=(27, 42, 17) 3^8 5^2 6^4 7^2 12^1 aut 2 ns 3 [991a5023fc8d713a; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(31, 48, 19) 3^4 4^8 5^4 8^2 16^1 aut 2 ns 3 [c53bc05bc306c97d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(0, 0, 1) eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(29, 46, 19) 3^4 4^12 8^2 16^1 aut 2 ns 5 [9f88c069215c2229; Schmitt-printed TYPE in IT(166); f printed in witness group table: True] via point(1, 2, 0) eps=1/48 ; f=(34, 52, 20) 3^4 4^9 5^4 10^2 16^1 aut 2 ns 2 [ff65c54d78bb4e50; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(0, 0, 1) eps=1/48

### `7472d8ba000c8056` — hexagonal, IT(152) P3_121, witness (0, 1/4, 1/6) c/a = 9/8, f = (22, 36, 16) 3^8 4^2 6^2 7^4 aut 2, dim 1, ns 6; POINT WALL walls [[0, 1, 0]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b,P5-only)

- point (0, 1, 0) - side (finest step -1/1536, point = (0, 383/1536, 1/6)): f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (0, 385/1536, 1/6)): f=(32, 48, 18) 3^4 4^6 6^2 8^6 aut 2 ns 0 [e98412e7cb95aea2; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 9213/8192): f=(32, 48, 18) 3^4 4^6 6^2 8^6 aut 2 ns 0 [e98412e7cb95aea2; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 9219/8192): f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(32, 48, 18) 3^4 4^6 6^2 8^6 aut 2 ns 0 [e98412e7cb95aea2; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `5beb94b61eb66eb1` — hexagonal, IT(178) P6_122, witness (1/8, 1/6, 5/12) c/a = 1/2, f = (27, 41, 16) 3^3 4^7 6^2 7^1 8^1 9^2 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 5 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(32, 48, 18) 3^2 4^10 6^1 8^2 9^2 10^1 aut 2 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(32, 48, 18) 3^4 4^6 5^2 6^2 8^1 10^3 aut 1 ns 0 [437fbe758a6dd8e3; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (3): f=(29, 44, 17) 3^3 4^6 5^3 6^2 9^2 10^1 aut 1 ns 1 [bc59e5d778f60d1f; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48 ; f=(32, 48, 18) 3^2 4^10 6^1 8^2 9^2 10^1 aut 2 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(32, 48, 18) 3^4 4^6 5^2 6^2 8^1 10^3 aut 1 ns 0 [437fbe758a6dd8e3; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `95934e84555dc2ea` — hexagonal, IT(179) P6_522, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (26, 40, 16) 3^2 4^7 5^1 6^3 7^1 8^2 aut 1, dim 3, ns 2; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 5 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(34, 51, 19) 3^4 4^7 6^2 7^2 8^2 10^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(38, 57, 21) 3^6 4^6 6^4 8^3 12^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (3): f=(34, 51, 19) 3^4 4^7 6^2 7^2 8^2 10^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(38, 57, 21) 3^6 4^6 6^4 8^3 12^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(44, 66, 24) 3^6 4^8 5^2 6^4 8^2 16^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48

### `d0ed9179c6947b5f` — hexagonal, IT(155) R32, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (16, 26, 12) 3^2 4^6 5^2 6^2 aut 2, dim 3, ns 3; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 25 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(20, 32, 14) 3^4 4^2 5^4 6^4 aut 4 ns 4 [47b6d29f5de536f0; Schmitt-printed TYPE in IT(155, 160, 161, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(24, 38, 16) 3^4 4^5 5^2 6^3 8^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (4): f=(16, 26, 12) 3^6 4^2 6^2 7^2 aut 2 ns 4 [4eaa641c282f54ad; Schmitt-printed TYPE in IT(155, 166); f printed in witness group table: True] via point(0, 1, 0) eps=1/48 ; f=(20, 32, 14) 3^4 4^2 5^4 6^4 aut 4 ns 4 [47b6d29f5de536f0; Schmitt-printed TYPE in IT(155, 160, 161, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(24, 38, 16) 3^4 4^5 5^2 6^3 8^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(28, 44, 18) 3^8 4^4 6^2 8^2 10^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48

### `272aefcd5e48ba49` — hexagonal, IT(179) P6_522, witness (1/12, 3/8, 1/6) c/a = 9/8, f = (29, 44, 17) 3^3 4^3 5^3 6^5 7^2 8^1 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 5 b; metric-thin: P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(34, 51, 19) 3^4 4^4 5^2 6^4 7^2 8^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(34, 51, 19) 3^4 4^4 6^7 7^2 8^1 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (4): f=(28, 42, 16) 3^2 4^5 5^2 6^4 8^3 aut 1 ns 0 [34351050a4f29035; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(34, 51, 19) 3^4 4^4 5^2 6^4 7^2 8^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(34, 51, 19) 3^4 4^4 6^7 7^2 8^1 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(38, 57, 21) 3^2 4^9 5^2 6^3 7^2 8^1 10^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48

### `4885ce1e70fa9713` — hexagonal, IT(179) P6_522, witness (1/12, 3/8, 1/6) c/a = 3/4, f = (27, 41, 16) 3^3 4^5 6^4 7^3 8^1 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 7 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(32, 48, 18) 3^4 4^6 6^2 7^2 8^3 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(32, 48, 18) 3^2 4^8 6^3 7^2 8^2 10^1 aut 2 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (4): f=(32, 48, 18) 3^4 4^6 6^2 7^2 8^3 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(36, 54, 20) 3^4 4^7 6^4 7^2 8^1 10^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192 ; f=(40, 60, 22) 3^2 4^8 5^6 6^4 14^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48 ; f=(32, 48, 18) 3^2 4^8 6^3 7^2 8^2 10^1 aut 2 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `9d0b36ad5caceb2e` — hexagonal, IT(167) R-3c, witness (1/12, 3/8, 1/6) c/a = 7/8, f = (22, 35, 15) 3^6 4^2 5^4 6^1 8^1 10^1 aut 1, dim 3, ns 3; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 5 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(30, 47, 19) 3^8 4^4 6^2 7^2 8^1 10^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(26, 41, 17) 3^6 4^4 6^5 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (8): f=(16, 26, 12) 3^2 4^6 5^2 6^2 aut 2 ns 3 [d0ed9179c6947b5f; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=-1/48 ; f=(20, 31, 13) 3^4 4^3 6^5 8^1 aut 1 ns 2 [5e68ffe7582a0657; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768 ; f=(26, 40, 16) 3^4 4^5 6^4 8^3 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(28, 43, 17) 4^10 5^2 6^3 8^1 10^1 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384 ; f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192 ; f=(26, 41, 17) 3^4 4^5 5^2 6^4 8^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/768 ; f=(30, 47, 19) 3^8 4^4 6^2 7^2 8^1 10^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/1536 ; f=(26, 41, 17) 3^6 4^4 6^5 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `105e41c2798e6180` — hexagonal, IT(148) R-3, witness (0, 0, 5/24) c/a = 2, f = (16, 27, 13) 3^6 4^3 6^4 aut 6, dim 1, ns 4; POINT WALL walls [[0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (0, 0, 1) - side (finest step -1/1536, point = (0, 0, 319/1536)): f=(31, 48, 19) 3^12 6^1 8^3 10^3 aut 6 ns 3 [f593cb348adf804b; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (0, 0, 107/512)): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 3071/1536): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/1536): f=(31, 48, 19) 3^12 6^1 8^3 10^3 aut 6 ns 3 [f593cb348adf804b; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(31, 48, 19) 3^12 6^1 8^3 10^3 aut 6 ns 3 [f593cb348adf804b; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `4b6055c7aa3d341b` — hexagonal, IT(178) P6_122, witness (1/8, 1/6, 5/12) c/a = 17/8, f = (25, 38, 15) 3^2 4^4 5^5 6^1 7^2 9^1 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 4 b; metric-thin: P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(30, 45, 17) 3^2 4^5 5^2 6^5 7^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(30, 45, 17) 3^4 4^4 6^6 8^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (6): f=(28, 42, 16) 4^9 6^4 8^3 aut 4 ns 0 [2a139a0af47705e5; Schmitt-printed TYPE in IT(181); f printed in witness group table: True] via point(1, 0, 0) eps=1/48 ; f=(22, 34, 14) 3^4 4^4 6^5 10^1 aut 2 ns 2 [8e6a80eb6f0f31a9; Schmitt-printed TYPE in IT(151, 153, 180, 181); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48 ; f=(30, 45, 17) 3^4 4^4 6^6 8^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(26, 39, 15) 4^4 5^4 6^7 aut 2 ns 0 [5ff09c7df2d7975b; Schmitt-printed TYPE in IT(178, 179); f printed in witness group table: True] via point(0, 0, 1) eps=1/48 ; f=(32, 48, 18) 3^6 4^3 5^2 6^1 7^2 8^3 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192 ; f=(30, 45, 17) 3^2 4^5 5^2 6^5 7^2 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536

### `7e79f1c38b5516bf` — hexagonal, IT(178) P6_122, witness (0, 1/4, 1/3) c/a = 3/2, f = (22, 34, 14) 3^4 4^2 5^4 6^2 8^2 aut 2, dim 1, ns 2; POINT WALL walls [[0, 1, 0]]; METRIC WALL; flags: line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (0, 1, 0) - side (finest step -1/1536, point = (0, 383/1536, 1/3)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (0, 385/1536, 1/3)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(32, 48, 18) 4^10 6^6 10^2 aut 2 ns 0 [a35623e347ef03b4; not a Schmitt-printed type; f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(32, 48, 18) 4^10 6^6 10^2 aut 2 ns 0 [a35623e347ef03b4; not a Schmitt-printed type; f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `d7c638d7fa23127e` — hexagonal, IT(169) P6_1, witness (1/12, 3/8, 1/6) c/a = 3/2, f = (25, 39, 16) 3^4 4^4 5^4 7^2 8^2 aut 1, dim 3, ns 3; POINT WALL walls [[1, 0, 0], [0, 1, 0]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (127/1536, 3/8, 1/6)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (43/512, 3/8, 1/6)): f=(32, 48, 18) 3^2 4^6 5^4 6^2 7^2 10^2 aut 1 ns 0 [322d5ff451e4101d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/12, 575/1536, 1/6)): f=(32, 48, 18) 3^2 4^6 5^4 6^2 7^2 10^2 aut 1 ns 0 [322d5ff451e4101d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/12, 577/1536, 1/6)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(32, 48, 18) 3^2 4^6 5^4 6^2 7^2 10^2 aut 1 ns 0 [322d5ff451e4101d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(32, 48, 18) 3^2 4^6 5^4 6^2 7^2 10^2 aut 1 ns 0 [322d5ff451e4101d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `0417061f8f56488e` — hexagonal, IT(152) P3_121, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (20, 32, 14) 3^4 4^5 6^4 8^1 aut 1, dim 3, ns 4; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 9 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(34, 51, 19) 3^8 4^2 5^2 6^2 8^3 12^2 aut 1 ns 0 [b2430fc4bea4e06d; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(26, 39, 15) 4^7 5^2 6^4 8^2 aut 4 ns 0 [59f890334e777569; Schmitt-printed TYPE in IT(181); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (3): f=(29, 44, 17) 3^7 4^2 5^2 6^2 8^2 10^1 11^1 aut 1 ns 1 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(34, 51, 19) 3^8 4^2 5^2 6^2 8^3 12^2 aut 1 ns 0 [b2430fc4bea4e06d; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(26, 39, 15) 4^7 5^2 6^4 8^2 aut 4 ns 0 [59f890334e777569; Schmitt-printed TYPE in IT(181); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `6cc34ed38aa354e1` — hexagonal, IT(181) P6_422, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (22, 34, 14) 3^2 4^4 5^4 6^3 8^1 aut 1, dim 3, ns 2; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 4 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(28, 42, 16) 4^7 5^2 6^6 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(28, 42, 16) 4^7 5^2 6^5 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (2): f=(28, 42, 16) 4^7 5^2 6^6 10^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(28, 42, 16) 4^7 5^2 6^5 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `161b09808f4c1863` — hexagonal, IT(178) P6_122, witness (0, 1/3, 1/3) c/a = 2, f = (18, 30, 14) 3^4 4^6 6^4 aut 4, dim 1, ns 6; POINT WALL walls [[0, 1, 0]]; METRIC WALL; flags: line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (0, 1, 0) - side (finest step -1/1536, point = (0, 511/1536, 1/3)): f=(32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 ns 0 [e5760549017956be; Schmitt-printed TYPE in IT(76, 78, 109, 151, 153); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (0, 171/512, 1/3)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 3071/1536): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/1536): f=(32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 ns 0 [e5760549017956be; Schmitt-printed TYPE in IT(76, 78, 109, 151, 153); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 ns 0 [e5760549017956be; Schmitt-printed TYPE in IT(76, 78, 109, 151, 153); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `c92eef8763d02d8a` — hexagonal, IT(179) P6_522, witness (1/12, 3/8, 1/6) c/a = 3/2, f = (25, 39, 16) 3^2 4^8 5^2 7^2 8^2 aut 1, dim 3, ns 3; POINT WALL walls [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (127/1536, 3/8, 1/6)): f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 [0b5d9beb0fc972f6; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (43/512, 3/8, 1/6)): f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 [60eb4282db04fca2; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/12, 575/1536, 1/6)): f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 [60eb4282db04fca2; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/12, 577/1536, 1/6)): f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 [0b5d9beb0fc972f6; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 [60eb4282db04fca2; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 [0b5d9beb0fc972f6; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 [60eb4282db04fca2; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 [0b5d9beb0fc972f6; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (5): f=(29, 45, 18) 3^2 4^7 5^4 6^1 7^2 8^2 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48 ; f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 [0b5d9beb0fc972f6; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 [60eb4282db04fca2; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(38, 57, 21) 3^4 4^2 5^8 6^2 7^2 8^2 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192 ; f=(37, 56, 21) 3^2 4^10 5^2 6^4 8^1 10^1 14^1 aut 1 ns 1 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48

### `5b679d8b0a3147c3` — hexagonal, IT(152) P3_121, witness (1/12, 3/8, 1/6) c/a = 17/16, f = (24, 38, 16) 3^6 4^5 7^2 8^3 aut 1, dim 3, ns 4; POINT WALL walls [[0, 0, 1]]; METRIC ONE-SIDED; flags: degenerate_flag_any, nonsimple_vertex; previous label: indeterminate (triage, 2 b; metric-thin: P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(34, 51, 19) 3^8 4^2 5^2 6^2 8^3 12^2 aut 1 ns 0 [b2430fc4bea4e06d; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(30, 45, 17) 3^4 4^3 5^4 6^1 7^2 8^2 10^1 aut 1 ns 0 [2165f5c5260120de; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (7): f=(20, 32, 14) 3^4 4^5 6^4 8^1 aut 1 ns 4 [0417061f8f56488e; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(28, 42, 16) 3^4 4^2 6^8 8^2 aut 1 ns 0 [2c121297dbaa80af; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/48 ; f=(29, 44, 17) 3^1 4^11 6^1 8^2 9^1 10^1 aut 1 ns 1 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(34, 51, 19) 3^2 4^10 6^3 8^2 10^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96 ; f=(30, 45, 17) 3^6 4^1 6^6 8^4 aut 2 ns 0 [56b1d49a0766cc47; Schmitt-printed TYPE in IT(181); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48 ; f=(34, 51, 19) 3^8 4^2 5^2 6^2 8^3 12^2 aut 1 ns 0 [b2430fc4bea4e06d; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(30, 45, 17) 3^4 4^3 5^4 6^1 7^2 8^2 10^1 aut 1 ns 0 [2165f5c5260120de; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `919d30fd9021b5ee` — hexagonal, IT(154) P3_221, witness (1/12, 3/8, 1/6) c/a = 51/32, f = (25, 38, 15) 3^3 4^3 5^2 6^4 7^3 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 3 b; metric-thin: P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(30, 45, 17) 3^4 4^4 5^2 6^2 8^5 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(30, 45, 17) 3^2 4^6 6^6 8^3 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192 ; f=(22, 34, 14) 3^4 4^4 5^2 6^1 8^3 aut 1 ns 2 [08fd2cc91bbad73c; Schmitt-printed TYPE in IT(152, 154); f printed in witness group table: True] via point(0, 1, 0) eps=1/48 ; f=(32, 48, 18) 3^4 4^5 5^2 6^4 10^3 aut 1 ns 0 [44201ed9cae489c1; Schmitt-printed TYPE in IT(152); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48 ; f=(30, 45, 17) 3^4 4^4 5^2 6^2 8^5 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(30, 45, 17) 3^2 4^6 6^6 8^3 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `6074c5fa5d2dffc5` — hexagonal, IT(148) R-3, witness (1/12, 3/8, 1/6) c/a = 3/4, f = (16, 26, 12) 3^2 4^5 5^4 6^1 aut 1, dim 3, ns 3; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 19 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(24, 38, 16) 3^6 4^2 5^2 6^2 7^4 aut 1 ns 4 [fac4317d5a65b959; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(20, 32, 14) 3^2 4^6 5^2 6^4 aut 1 ns 4 [f7c3e10af5321d77; Schmitt-printed TYPE in IT(163); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (3): f=(20, 32, 14) 3^2 4^6 5^4 7^2 aut 1 ns 4 [5f812747976b224a; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(24, 38, 16) 3^6 4^2 5^2 6^2 7^4 aut 1 ns 4 [fac4317d5a65b959; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(20, 32, 14) 3^2 4^6 5^2 6^4 aut 1 ns 4 [f7c3e10af5321d77; Schmitt-printed TYPE in IT(163); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `5e68ffe7582a0657` — hexagonal, IT(167) R-3c, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (20, 31, 13) 3^4 4^3 6^5 8^1 aut 1, dim 3, ns 2; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 8 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(26, 40, 16) 3^4 4^5 6^4 8^3 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(26, 40, 16) 3^4 4^6 6^2 8^4 aut 1 ns 2 [6de3dac5f334cfed; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (2): f=(26, 40, 16) 3^4 4^5 6^4 8^3 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(26, 40, 16) 3^4 4^6 6^2 8^4 aut 1 ns 2 [6de3dac5f334cfed; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `1ba26ab2c0999b93` — hexagonal, IT(148) R-3, witness (1/12, 3/8, 1/6) c/a = 1/2, f = (20, 32, 14) 3^4 4^3 5^2 6^5 aut 1, dim 3, ns 3; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: open-likely (triage, 4 b)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(28, 44, 18) 3^6 4^5 6^2 7^2 8^3 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(24, 38, 16) 3^4 4^5 6^6 8^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (4): f=(19, 29, 12) 3^2 4^4 6^6 aut 1 ns 1 [d40ab48fae3b8762; Schmitt-printed TYPE in IT(148); f printed in witness group table: True] via point(0, 1, 0) eps=1/48 ; f=(24, 38, 16) 3^6 4^2 6^6 7^2 aut 2 ns 4 [057255f61286b052; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96 ; f=(24, 38, 16) 3^4 4^5 6^6 8^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(28, 44, 18) 3^6 4^5 6^2 7^2 8^3 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536

### `d1f1121757598de0` — hexagonal, IT(154) P3_221, witness (1/8, 1/6, 5/12) c/a = 9/4, f = (15, 25, 12) 3^2 4^8 6^2 aut 2, dim 3, ns 5; POINT WALL walls [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: indeterminate (triage, 2 b)

- point (1, 0, 0) - side (finest step -1/1536, point = (191/1536, 1/6, 5/12)): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [f905851c28b76464; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (193/1536, 1/6, 5/12)): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [29148698f93136e6; Schmitt-printed TYPE in IT(169, 170, 178, 179); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/8, 85/512, 5/12)): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [29148698f93136e6; Schmitt-printed TYPE in IT(169, 170, 178, 179); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/8, 257/1536, 5/12)): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [f905851c28b76464; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [f905851c28b76464; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [29148698f93136e6; Schmitt-printed TYPE in IT(169, 170, 178, 179); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 9213/4096): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [f905851c28b76464; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 9219/4096): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [29148698f93136e6; Schmitt-printed TYPE in IT(169, 170, 178, 179); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [f905851c28b76464; Schmitt-printed TYPE in IT(169, 170); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [29148698f93136e6; Schmitt-printed TYPE in IT(169, 170, 178, 179); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072

### `457c20cf036ae496` — hexagonal, IT(180) P6_222, witness (0, 1/2, 0) c/a = 3/2, f = (11, 20, 11) 3^6 4^3 5^2 aut 2, dim 1, ns 7; POINT WALL walls [[0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (0, 0, 1) - side (finest step -1/1536, point = (0, 1/2, -1/1536)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (0, 1/2, 1/1536)): f=(22, 35, 15) 3^4 4^6 6^3 8^2 aut 2 ns 4 [df40917011e94d04; Schmitt-printed TYPE in IT(151, 153); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(16, 26, 12) 3^2 4^6 5^2 6^2 aut 2 ns 4 [0cea04a8f66814e0; Schmitt-printed TYPE in IT(151, 152, 153, 154, 178, 179); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(13, 22, 11) 3^4 4^5 6^2 aut 2 ns 5 [f1e0d6a24a06b752; Schmitt-printed TYPE in IT(151, 152, 153, 154, 178, 179); f printed in witness group table: True] via metric eps=1/192, metric eps=1/96, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (4): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(22, 35, 15) 3^4 4^6 6^3 8^2 aut 2 ns 4 [df40917011e94d04; Schmitt-printed TYPE in IT(151, 153); f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(16, 26, 12) 3^2 4^6 5^2 6^2 aut 2 ns 4 [0cea04a8f66814e0; Schmitt-printed TYPE in IT(151, 152, 153, 154, 178, 179); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(13, 22, 11) 3^4 4^5 6^2 aut 2 ns 5 [f1e0d6a24a06b752; Schmitt-printed TYPE in IT(151, 152, 153, 154, 178, 179); f printed in witness group table: True] via metric eps=1/192, metric eps=1/96, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072

### `11a9fe078850b5cd` — hexagonal, IT(179) P6_522, witness (1/8, 1/6, 5/12) c/a = 65/32, f = (25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1, dim 3, ns 1; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b,P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(30, 45, 17) 3^2 4^5 6^8 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(30, 45, 17) 3^4 4^3 5^2 6^4 8^4 aut 1 ns 0 [e77398f50b295584; Schmitt-printed TYPE in IT(179); f printed in witness group table: True] via point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (6): f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384 ; f=(25, 38, 15) 3^2 4^4 5^4 6^1 7^4 aut 1 ns 1 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/48 ; f=(22, 34, 14) 3^4 4^3 5^2 6^3 8^2 aut 1 ns 2 [b3981da714598974; Schmitt-printed TYPE in IT(178, 179); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96 ; f=(32, 48, 18) 3^4 4^5 5^2 6^3 8^2 10^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384 ; f=(30, 45, 17) 3^2 4^5 6^8 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(30, 45, 17) 3^4 4^3 5^2 6^4 8^4 aut 1 ns 0 [e77398f50b295584; Schmitt-printed TYPE in IT(179); f printed in witness group table: True] via point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `c95a5fcf4d681568` — hexagonal, IT(166) R-3m, witness (1/24, 1/12, 1/6) c/a = 3/2, f = (12, 21, 11) 3^4 4^5 5^2 aut 2, dim 2, ns 4; POINT WALL walls [[1, 2, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: indeterminate (triage, 2 b)

- point (1, 2, 0) - side (finest step -1/1536, point = (21/512, 21/256, 1/6)): f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 [9d4396ca0b08fc3c; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (1, 2, 0) + side (finest step 1/1536, point = (65/1536, 65/768, 1/6)): f=(13, 22, 11) 3^4 4^5 6^2 aut 2 ns 4 [9fa7f38938046e47; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/24, 1/12, 85/512)): f=(17, 28, 13) 3^2 4^9 7^2 aut 2 ns 5 [346c81a0f2121bf1; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/24, 1/12, 257/1536)): f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 [9d4396ca0b08fc3c; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 [9d4396ca0b08fc3c; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(13, 22, 11) 3^4 4^5 6^2 aut 2 ns 4 [9fa7f38938046e47; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (3): f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 [9d4396ca0b08fc3c; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(13, 22, 11) 3^4 4^5 6^2 aut 2 ns 4 [9fa7f38938046e47; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(17, 28, 13) 3^2 4^9 7^2 aut 2 ns 5 [346c81a0f2121bf1; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536

### `f7bd7cd9eae6436b` — hexagonal, IT(166) R-3m, witness (1/12, 1/6, 11/24) c/a = 1, f = (16, 27, 13) 3^6 4^4 6^2 8^1 aut 2, dim 2, ns 5; POINT WALL walls [[1, 2, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 2, 0) - side (finest step -1/1536, point = (127/1536, 127/768, 11/24)): f=(34, 53, 21) 3^8 4^6 6^4 7^2 20^1 aut 2 ns 4 [b3d52575f76a33bd; Schmitt-printed TYPE in IT(148, 166); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (1, 2, 0) + side (finest step 1/1536, point = (43/512, 43/256, 11/24)): f=(19, 30, 13) 3^4 4^4 5^2 7^2 8^1 aut 2 ns 3 [36c92427e3d084dc; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 1/6, 703/1536)): f=(34, 53, 21) 3^8 4^6 6^4 7^2 20^1 aut 2 ns 4 [b3d52575f76a33bd; Schmitt-printed TYPE in IT(148, 166); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 1/6, 235/512)): f=(19, 30, 13) 3^4 4^4 5^2 7^2 8^1 aut 2 ns 3 [36c92427e3d084dc; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/3072): f=(34, 53, 21) 3^8 4^6 6^4 7^2 20^1 aut 2 ns 4 [b3d52575f76a33bd; Schmitt-printed TYPE in IT(148, 166); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/3072): f=(19, 30, 13) 3^4 4^4 5^2 7^2 8^1 aut 2 ns 3 [36c92427e3d084dc; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (5): f=(31, 48, 19) 3^4 4^8 5^4 8^2 16^1 aut 2 ns 3 [c53bc05bc306c97d; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(1, 2, 0) eps=-1/192 ; f=(19, 30, 13) 3^4 4^4 5^2 7^2 8^1 aut 2 ns 3 [36c92427e3d084dc; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 2, 0) eps=1/96, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(18, 29, 13) 3^6 4^2 5^2 7^2 8^1 aut 2 ns 4 [a1b2ac427f563716; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96 ; f=(16, 27, 13) 3^6 4^4 6^2 8^1 aut 2 ns 6 [cf213e55efccc5f8; Schmitt-printed TYPE in IT(155, 166); f printed in witness group table: True] via point(0, 0, 1) eps=1/48 ; f=(34, 53, 21) 3^8 4^6 6^4 7^2 20^1 aut 2 ns 4 [b3d52575f76a33bd; Schmitt-printed TYPE in IT(148, 166); f printed in witness group table: True] via metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `75c9be976d704515` — hexagonal, IT(152) P3_121, witness (0, 3/8, 1/6) c/a = 9/8, f = (18, 28, 12) 4^8 6^4 aut 2, dim 1, ns 2; POINT WALL walls [[0, 1, 0]]; METRIC WALL; flags: line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b,P5-only)

- point (0, 1, 0) - side (finest step -1/1536, point = (0, 575/1536, 1/6)): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (0, 577/1536, 1/6)): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 9213/8192): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 9219/8192): f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(28, 42, 16) 4^8 5^4 8^4 aut 4 ns 0 [1a36f90bbc759307; Schmitt-printed TYPE in IT(144, 145, 151, 153, 169, 170); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072

### `8463196a30c6643f` — hexagonal, IT(179) P6_522, witness (1/8, 1/6, 5/12) c/a = 2, f = (23, 36, 15) 3^2 4^5 5^2 6^6 aut 1, dim 3, ns 3; POINT WALL walls [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (191/1536, 1/6, 5/12)): f=(25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1 ns 1 [11a9fe078850b5cd; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (193/1536, 1/6, 5/12)): f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/8, 85/512, 5/12)): f=(25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1 ns 1 [11a9fe078850b5cd; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/8, 257/1536, 5/12)): f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(30, 45, 17) 3^2 4^5 6^8 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 3071/1536): f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/1536): f=(25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1 ns 1 [11a9fe078850b5cd; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (6): f=(25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1 ns 1 [11a9fe078850b5cd; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(28, 42, 16) 4^8 6^6 8^2 aut 2 ns 0 [99e39b85a778ce64; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(22, 34, 14) 3^4 4^3 5^2 6^3 8^2 aut 1 ns 2 [b3981da714598974; Schmitt-printed TYPE in IT(178, 179); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48 ; f=(32, 48, 18) 3^4 4^5 5^2 6^3 8^2 10^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96 ; f=(25, 39, 16) 3^4 4^3 5^4 6^3 8^2 aut 1 ns 3 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/192 ; f=(30, 45, 17) 3^2 4^5 6^8 8^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536

### `487490cdf474e568` — hexagonal, IT(148) R-3, witness (1/12, 3/8, 1/6) c/a = 1277/2000, f = (20, 32, 14) 3^4 4^5 6^3 7^2 aut 1, dim 3, ns 3; POINT WALL walls [[0, 0, 1]]; METRIC OPEN; flags: degenerate_flag_any, nonsimple_vertex; previous label: indeterminate (triage, 2 b; metric-thin: P5-only)

- point (0, 0, 1) - side (finest step -1/1536, point = (1/12, 3/8, 85/512)): f=(28, 44, 18) 3^6 4^5 6^4 8^1 9^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536
- point (0, 0, 1) + side (finest step 1/1536, point = (1/12, 3/8, 257/1536)): f=(24, 38, 16) 3^6 4^1 5^4 6^2 7^2 8^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536
- all neighbouring types seen on-stratum (5): f=(16, 26, 12) 3^2 4^5 5^4 6^1 aut 1 ns 3 [6074c5fa5d2dffc5; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(1, 0, 0) eps=-1/192 ; f=(20, 32, 14) 3^4 4^3 5^2 6^5 aut 1 ns 3 [1ba26ab2c0999b93; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48 ; f=(20, 32, 14) 3^4 4^2 5^4 6^4 aut 4 ns 4 [47b6d29f5de536f0; Schmitt-printed TYPE in IT(155, 160, 161, 166); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(28, 44, 18) 3^6 4^5 6^4 8^1 9^2 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(24, 38, 16) 3^6 4^1 5^4 6^2 7^2 8^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536

### `f0e2036d295195b4` — hexagonal, IT(152) P3_121, witness (0, 1/8, 1/6) c/a = 9/8, f = (12, 20, 10) 3^4 4^4 6^2 aut 2, dim 1, ns 4; POINT WALL walls [[0, 1, 0]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b,P5-only)

- point (0, 1, 0) - side (finest step -1/1536, point = (0, 191/1536, 1/6)): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [1d2c47d061a6ab6c; Schmitt-printed TYPE in IT(144, 145, 152, 154); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (0, 193/1536, 1/6)): f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 9213/8192): f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 9219/8192): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [1d2c47d061a6ab6c; Schmitt-printed TYPE in IT(144, 145, 152, 154); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(18, 28, 12) 4^6 5^4 6^2 aut 2 ns 2 [1d2c47d061a6ab6c; Schmitt-printed TYPE in IT(144, 145, 152, 154); f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(26, 40, 16) 3^4 4^6 7^4 8^2 aut 2 ns 2 [4a31af4ea18688a8; Schmitt-printed TYPE in IT(144, 145); f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `67b1ede4b021a4fc` — hexagonal, IT(155) R32, witness (1/8, 1/6, 5/12) c/a = 3/2, f = (17, 29, 14) 3^4 4^6 5^2 6^2 aut 1, dim 3, ns 5; POINT WALL walls [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (191/1536, 1/6, 5/12)): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 1 ns 6 [52c5120f1148da14; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (193/1536, 1/6, 5/12)): f=(28, 44, 18) 3^2 4^8 5^4 6^2 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/8, 85/512, 5/12)): f=(28, 44, 18) 3^2 4^8 5^4 6^2 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/8, 257/1536, 5/12)): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 1 ns 6 [52c5120f1148da14; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(28, 44, 18) 3^2 4^8 5^4 6^2 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 1 ns 6 [52c5120f1148da14; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(28, 44, 18) 3^2 4^8 5^4 6^2 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 1 ns 6 [52c5120f1148da14; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (3): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 1 ns 6 [52c5120f1148da14; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(28, 44, 18) 3^2 4^8 5^4 6^2 8^1 10^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(30, 47, 19) 3^4 4^6 5^4 6^3 10^2 aut 1 ns 4 [d9bf7fb7a80eaa38; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48

### `34e5e7acce18b5cd` — hexagonal, IT(166) R-3m, witness (1/24, 1/12, 5/12) c/a = 3/2, f = (14, 23, 11) 3^6 4^2 6^2 8^1 aut 2, dim 2, ns 4; POINT WALL walls [[1, 2, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 2, 0) - side (finest step -1/1536, point = (21/512, 21/256, 5/12)): f=(20, 31, 13) 3^4 4^6 7^2 12^1 aut 2 ns 2 [fa027394e7e22a9e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (1, 2, 0) + side (finest step 1/1536, point = (65/1536, 65/768, 5/12)): f=(16, 25, 11) 3^4 4^2 5^2 6^2 8^1 aut 2 ns 2 [3f5fce0d11d8899e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/24, 1/12, 213/512)): f=(20, 31, 13) 3^4 4^6 7^2 12^1 aut 2 ns 2 [fa027394e7e22a9e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/24, 1/12, 641/1536)): f=(16, 25, 11) 3^4 4^2 5^2 6^2 8^1 aut 2 ns 2 [3f5fce0d11d8899e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(20, 31, 13) 3^4 4^6 7^2 12^1 aut 2 ns 2 [fa027394e7e22a9e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(16, 25, 11) 3^4 4^2 5^2 6^2 8^1 aut 2 ns 2 [3f5fce0d11d8899e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(20, 31, 13) 3^4 4^6 7^2 12^1 aut 2 ns 2 [fa027394e7e22a9e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(16, 25, 11) 3^4 4^2 5^2 6^2 8^1 aut 2 ns 2 [3f5fce0d11d8899e; Schmitt-printed TYPE in IT(148, 155, 166, 167); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072

### `fa9c370d30741970` — hexagonal, IT(180) P6_222, witness (1/6, 1/3, 0) c/a = 3/2, f = (9, 16, 9) 3^4 4^5 aut 2, dim 1, ns 5; POINT WALL walls [[1, 2, 0]]; METRIC WALL; flags: degenerate_flag_any, line_isolated, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 2, 0) - side (finest step -1/1536, point = (85/512, 85/256, 0)): f=(22, 35, 15) 3^4 4^6 6^3 8^2 aut 2 ns 4 [4a6f33270c17ba66; Schmitt-printed TYPE in IT(152, 154, 171, 172, 178, 179, 180, 181); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536
- point (1, 2, 0) + side (finest step 1/1536, point = (257/1536, 257/768, 0)): f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [c57d8f62f90c0cf0; Schmitt-printed TYPE in IT(171, 172); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536
- metric - side (finest step -1/3072, c/a = 3071/2048): f=(20, 31, 13) 3^2 4^3 5^4 6^4 aut 2 ns 2 [6a892fdc51b24155; Schmitt-printed TYPE in IT(171, 172); f printed in witness group table: False] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/2048): f=(12, 19, 9) 3^4 4^2 6^3 aut 2 ns 2 [03b5c7cc17c5e015; Schmitt-printed TYPE in IT(119, 171, 172); f printed in witness group table: False] via metric eps=1/192, metric eps=1/96, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (4): f=(22, 35, 15) 3^4 4^6 6^3 8^2 aut 2 ns 4 [4a6f33270c17ba66; Schmitt-printed TYPE in IT(152, 154, 171, 172, 178, 179, 180, 181); f printed in witness group table: True] via point(1, 2, 0) eps=-1/48, point(1, 2, 0) eps=-1/96, point(1, 2, 0) eps=-1/192, point(1, 2, 0) eps=-1/384, point(1, 2, 0) eps=-1/768, point(1, 2, 0) eps=-1/1536 ; f=(22, 34, 14) 3^4 4^4 6^4 8^2 aut 2 ns 2 [c57d8f62f90c0cf0; Schmitt-printed TYPE in IT(171, 172); f printed in witness group table: True] via point(1, 2, 0) eps=1/96, point(1, 2, 0) eps=1/48, point(1, 2, 0) eps=1/192, point(1, 2, 0) eps=1/384, point(1, 2, 0) eps=1/768, point(1, 2, 0) eps=1/1536 ; f=(20, 31, 13) 3^2 4^3 5^4 6^4 aut 2 ns 2 [6a892fdc51b24155; Schmitt-printed TYPE in IT(171, 172); f printed in witness group table: False] via metric eps=-1/96, metric eps=-1/192, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072 ; f=(12, 19, 9) 3^4 4^2 6^3 aut 2 ns 2 [03b5c7cc17c5e015; Schmitt-printed TYPE in IT(119, 171, 172); f printed in witness group table: False] via metric eps=1/192, metric eps=1/96, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072

### `400cba5c78326d1d` — hexagonal, IT(167) R-3c, witness (1/8, 1/6, 5/12) c/a = 1, f = (17, 28, 13) 4^10 5^2 6^1 aut 1, dim 3, ns 5; POINT WALL walls [[1, 0, 0], [0, 1, 0], [0, 0, 1]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (191/1536, 1/6, 5/12)): f=(22, 34, 14) 4^7 5^4 6^2 8^1 aut 2 ns 2 [4297fd505b9cc36d; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (193/1536, 1/6, 5/12)): f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/8, 85/512, 5/12)): f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/8, 257/1536, 5/12)): f=(22, 34, 14) 4^7 5^4 6^2 8^1 aut 2 ns 2 [4297fd505b9cc36d; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) - side (finest step -1/1536, point = (1/8, 1/6, 213/512)): f=(22, 34, 14) 4^7 5^4 6^2 8^1 aut 2 ns 2 [4297fd505b9cc36d; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (0, 0, 1) + side (finest step 1/1536, point = (1/8, 1/6, 641/1536)): f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric - side (finest step -1/3072, c/a = 3071/3072): f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/3072): f=(22, 34, 14) 4^7 5^4 6^2 8^1 aut 2 ns 2 [4297fd505b9cc36d; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (2): f=(22, 34, 14) 4^7 5^4 6^2 8^1 aut 2 ns 2 [4297fd505b9cc36d; Schmitt-printed TYPE in IT(148, 155, 166); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 [4ff9d77aa9f8194a; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

### `78e755ffdff3a2f5` — hexagonal, IT(146) R3, witness (1/12, 3/8, 1/6) c/a = 3/4, f = (14, 24, 12) 3^4 4^6 6^2 aut 2, dim 3, ns 6; POINT WALL walls [[1, 0, 0], [0, 1, 0]]; METRIC WALL; flags: degenerate_flag_any, nonsimple_vertex; previous label: wall-suspect (triage, 1 b; metric-thin: 1b)

- point (1, 0, 0) - side (finest step -1/1536, point = (127/1536, 3/8, 1/6)): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 2 ns 6 [c97273f4df7f3fdc; Schmitt-printed TYPE in IT(146); f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- point (1, 0, 0) + side (finest step 1/1536, point = (43/512, 3/8, 1/6)): f=(24, 38, 16) 3^6 5^6 6^2 8^2 aut 2 ns 4 [efc24204486dde03; Schmitt-printed TYPE in IT(146, 155); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) - side (finest step -1/1536, point = (1/12, 575/1536, 1/6)): f=(24, 38, 16) 3^6 5^6 6^2 8^2 aut 2 ns 4 [efc24204486dde03; Schmitt-printed TYPE in IT(146, 155); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- point (0, 1, 0) + side (finest step 1/1536, point = (1/12, 577/1536, 1/6)): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 2 ns 6 [c97273f4df7f3fdc; Schmitt-printed TYPE in IT(146); f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- metric - side (finest step -1/3072, c/a = 3071/4096): f=(24, 38, 16) 3^6 5^6 6^2 8^2 aut 2 ns 4 [efc24204486dde03; Schmitt-printed TYPE in IT(146, 155); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072
- metric + side (finest step 1/3072, c/a = 3073/4096): f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 2 ns 6 [c97273f4df7f3fdc; Schmitt-printed TYPE in IT(146); f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072
- all neighbouring types seen on-stratum (3): f=(18, 30, 14) 3^4 4^6 6^4 aut 2 ns 6 [7b9cfe26fe4a9c4b; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48 ; f=(18, 30, 14) 3^4 4^4 5^4 6^2 aut 2 ns 6 [c97273f4df7f3fdc; Schmitt-printed TYPE in IT(146); f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768, metric eps=1/1536, metric eps=1/3072 ; f=(24, 38, 16) 3^6 5^6 6^2 8^2 aut 2 ns 4 [efc24204486dde03; Schmitt-printed TYPE in IT(146, 155); f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, metric eps=-1/384, metric eps=-1/768, metric eps=-1/1536, metric eps=-1/3072

## One-sided cells (9): the changing side(s)

- `d70e6901953070e7` hex IT(155) c/a 3/4 f (38, 58, 22): changing side(s) ['point(0, 1, 0):-', 'point(1, 0, 0):+']; neighbours: f=(34, 52, 20) 3^8 4^2 5^2 6^4 8^3 14^1 aut 1 ns 2 [59b28b3a59c27092; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(0, 1, 0) eps=1/192 ; f=(19, 31, 14) 3^4 4^5 5^2 6^2 8^1 aut 1 ns 5 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96 ; f=(28, 43, 17) 4^9 5^2 6^4 8^2 aut 1 ns 2 [c3b4b14633c9d4d5; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48 ; f=(24, 39, 17) 3^4 4^8 6^4 10^1 aut 1 ns 6 [1d81d76adec2770e; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(0, 1, 0) eps=-1/96 ; f=(24, 37, 15) 3^2 4^5 5^2 6^5 8^1 aut 1 ns 2 [550900e445751dbc; Schmitt-printed TYPE in IT(155); f printed in witness group table: True] via point(0, 0, 1) eps=-1/48 ; f=(30, 46, 18) 3^2 4^8 5^2 6^4 8^1 12^1 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/96 ; f=(34, 52, 20) 3^4 4^6 5^2 6^6 8^1 14^1 aut 1 ns 2 [87c94384d7851cb2; not a Schmitt-printed type; f printed in witness group table: True] via metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768
- `7e023be581e7c50a` hex IT(154) c/a 3/4 f (36, 54, 20): changing side(s) ['point(1, 0, 0):+']; neighbours: f=(36, 54, 20) 3^2 4^11 5^2 6^1 8^2 12^1 14^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(0, 0, 1) eps=1/48 ; f=(34, 51, 19) 3^2 4^11 6^1 8^3 10^1 12^1 aut 1 ns 0 [cbead3df2d2f1d0e; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96 ; f=(32, 48, 18) 3^6 4^2 5^4 7^2 8^2 10^2 aut 1 ns 0 [d10bb4a25bbf4c80; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768 ; f=(24, 36, 14) 4^6 6^8 aut 48 ns 0 [31d09faf7fb2bf6f; Schmitt-printed TYPE in IT(76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167); f printed in witness group table: True] via point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48 ; f=(29, 44, 17) 3^1 4^11 6^1 8^3 11^1 aut 1 ns 1 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/48
- `71d2c9953ca110b8` hex IT(169) c/a 39/32 f (36, 54, 20): changing side(s) ['point(0, 1, 0):+', 'point(1, 0, 0):-']; neighbours: f=(32, 48, 18) 4^10 6^6 10^2 aut 2 ns 0 [a35623e347ef03b4; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, metric eps=1/384, metric eps=1/768 ; f=(32, 48, 18) 3^2 4^4 5^8 6^2 11^2 aut 1 ns 0 [16025e0680843c36; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, metric eps=-1/384, metric eps=-1/768
- `66563d07a1110a25` hex IT(154) c/a 1 f (36, 54, 20): changing side(s) ['point(0, 1, 0):-', 'point(1, 0, 0):+']; neighbours: f=(38, 57, 21) 3^4 4^8 5^2 6^3 8^2 12^1 14^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(0, 0, 1) eps=1/48 ; f=(36, 54, 20) 3^6 4^4 5^2 6^3 8^1 9^2 10^2 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96 ; f=(28, 42, 16) 3^4 4^1 5^4 6^4 8^3 aut 1 ns 0 [72bcd959be4ab7dd; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=1/96, point(1, 0, 0) eps=1/48, point(0, 1, 0) eps=-1/48, point(0, 0, 1) eps=-1/48 ; f=(32, 48, 18) 3^4 4^5 5^2 7^2 8^5 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(1, 0, 0) eps=1/192, point(1, 0, 0) eps=1/384, point(1, 0, 0) eps=1/768, point(1, 0, 0) eps=1/1536, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768 ; f=(32, 48, 18) 3^4 4^4 5^2 6^3 7^2 8^2 10^1 aut 1 ns 0 [fcffad0da2b5b62f; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 0, 1) eps=1/96, metric eps=-1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384 ; f=(26, 40, 16) 3^2 4^8 5^2 8^4 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/48
- `60eb4282db04fca2` hex IT(179) c/a 11/8 f (30, 45, 17): changing side(s) ['point(0, 0, 1):+']; neighbours: f=(31, 47, 18) 3^3 4^2 5^7 6^3 7^2 10^1 aut 1 ns 1 [f5fbebffa76808d5; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384 ; f=(36, 54, 20) 3^4 4^3 5^4 6^5 7^2 8^1 12^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536 ; f=(40, 60, 22) 3^4 4^6 5^2 6^7 8^1 10^1 14^1 aut 1 ns 0 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48
- `f43b45fd6383b36b` hex IT(155) c/a 19/16 f (26, 41, 17): changing side(s) ['point(0, 0, 1):-', 'point(1, 0, 0):-']; neighbours: f=(30, 47, 19) 3^4 4^7 5^2 6^4 8^1 12^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96 ; f=(30, 47, 19) 3^2 4^8 5^6 6^1 8^1 12^1 aut 1 ns 4 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48 ; f=(30, 47, 19) 3^6 4^5 5^2 6^3 8^1 10^2 aut 1 ns 4 [37aa18e6e10583be; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536 ; f=(30, 47, 19) 3^4 4^6 5^4 6^3 10^2 aut 1 ns 4 [d9bf7fb7a80eaa38; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/96 ; f=(22, 36, 16) 3^4 4^8 6^2 8^2 aut 1 ns 6 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48
- `4ff9d77aa9f8194a` hex IT(167) c/a 3/4 f (24, 37, 15): changing side(s) ['point(0, 0, 1):+', 'point(0, 1, 0):+', 'point(1, 0, 0):-']; neighbours: f=(26, 40, 16) 3^4 4^6 6^3 8^2 10^1 aut 2 ns 2 [ddbf7770e983e608; Schmitt-printed TYPE in IT(155, 166, 167); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48 ; f=(28, 43, 17) 3^10 6^1 8^5 10^1 aut 1 ns 2 [74a69fba4266de3b; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/96, point(0, 1, 0) eps=1/48, point(0, 0, 1) eps=1/96, point(0, 0, 1) eps=1/48, metric eps=-1/96, metric eps=-1/192, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768, point(0, 1, 0) eps=1/1536, point(0, 0, 1) eps=1/192, point(0, 0, 1) eps=1/384, point(0, 0, 1) eps=1/768, point(0, 0, 1) eps=1/1536, metric eps=-1/384, metric eps=-1/768
- `c18a9b1cb2a5d168` hex IT(148) c/a 1/2 f (26, 40, 16): changing side(s) ['point(0, 0, 1):-', 'point(0, 1, 0):-']; neighbours: f=(26, 40, 16) 4^7 5^6 7^2 8^1 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(1, 0, 0) eps=-1/48 ; f=(22, 34, 14) 4^6 5^4 6^4 aut 1 ns 2 [cda1d1c03659b67d; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=-1/48, point(0, 1, 0) eps=-1/96, point(0, 0, 1) eps=-1/48, point(0, 0, 1) eps=-1/96, metric eps=1/192, metric eps=1/96, point(0, 1, 0) eps=-1/192, point(0, 1, 0) eps=-1/384, point(0, 1, 0) eps=-1/768, point(0, 1, 0) eps=-1/1536, point(0, 0, 1) eps=-1/192, point(0, 0, 1) eps=-1/384, point(0, 0, 1) eps=-1/768, point(0, 0, 1) eps=-1/1536, metric eps=1/384, metric eps=1/768 ; f=(26, 40, 16) 3^4 4^3 5^2 6^4 7^2 8^1 aut 1 ns 2 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/48 ; f=(23, 36, 15) 3^6 5^2 6^5 7^2 aut 1 ns 3 [not stored; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 0, 1) eps=1/48
- `b27ba8dbcbc2891a` hex IT(161) c/a 1/2 f (22, 34, 14): changing side(s) ['point(1, 0, 0):-']; neighbours: f=(22, 34, 14) 3^2 4^2 5^6 6^4 aut 1 ns 2 [bbf85b4df505dab4; Schmitt-printed TYPE in IT(161); f printed in witness group table: True] via point(1, 0, 0) eps=-1/48, point(1, 0, 0) eps=-1/96, point(0, 1, 0) eps=1/48 ; f=(26, 40, 16) 3^6 5^4 6^2 7^2 8^2 aut 1 ns 2 [466b12546dd936c3; not a Schmitt-printed type; f printed in witness group table: True] via point(0, 1, 0) eps=1/96, metric eps=1/96, point(1, 0, 0) eps=-1/192, point(1, 0, 0) eps=-1/384, point(1, 0, 0) eps=-1/768, point(1, 0, 0) eps=-1/1536, point(0, 1, 0) eps=1/192, point(0, 1, 0) eps=1/384, point(0, 1, 0) eps=1/768

## Indeterminate cells (chain quarantine on a side; 0)

None.

## Regression against COLLISION_PHASE2_RESULTS.md (top-3 tetragonal point verdicts; same steps, same chain; ASSERTED)

| id | expected POINT (walls) | got POINT (walls) | agrees | its b verdict there (absolute steps) | METRIC verdict here (relative steps) |
|---|---|---|---|---|---|
| `4e9c9b076cfec323` | OPEN [] | OPEN [] | True | OPEN | OPEN |
| `49cedbdd58376fac` | WALL [[1, 1, 0]] | WALL [[1, 1, 0]] | True | OPEN | OPEN |
| `f654982d74d740f6` | OPEN [] | OPEN [] | True | OPEN | OPEN |

Regression: PASS.

## G3 bookkeeping

- Perturbed cells whose float proposal was degeneracy-flagged and superseded by the exact clip: 0 rows over 0 cells .
- Quarantine rows (ChainError, recorded, never SAME): 0.
- Rows with a site-stabilizer change (the step landed on a special point of the stratum): 0.
- Total chain evaluations: 3879.

## Honest limits

- Finite steps only: OPEN = the code is unchanged at every tested step (largest 1/48 point / 1/96 relative metric; smallest 1/96 point / 1/192 relative metric, refined to 1/1536 and 1/3072 on failing sides). A change seen at the LARGER coarse step with SAME at the smaller one leaves the verdict OPEN (c1 rule: the verdict uses the smallest step on each side) and is recorded as a neighbour.
- The classification is at the FIRST WITNESS only; other sightings of the same type (other groups, points, b-ratios) are not perturbed here.
- The metric direction is the family's single free ratio c/a; no lattice-angle direction exists in these families.
- Neighbour naming is by stored id in the two phase-2 stores plus the cubic seeds; a "not stored" neighbour is a type the sweeps never sampled (recorded here only, not added to any store).
- Schmitt-printed TYPE status relies on the pass-P2 sightings of the accepted sweeps (his printed representative reproduced at his printed point under the accepted conversions); it is type-level evidence at his printed points only, not a statement about his unprinted data.

## Per-cell detail (every row; off-stratum rows marked)

**`4e9c9b076cfec323`** tetragonal IT(92) P4_12_12 witness (5/24, 5/24, 0) c/a 5/4 basis [[1, 1, 0]] base f=(40, 60, 22) 3^8 4^4 5^4 8^2 11^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 1, 0) | -1/48 | (3/16, 3/16, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| point | (1, 1, 0) | -1/96 | (19/96, 19/96, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| point | (1, 1, 0) | 1/96 | (7/32, 7/32, 0) | 5/4 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point | (1, 1, 0) | 1/48 | (11/48, 11/48, 0) | 5/4 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| metric | - | -1/96 | (5/24, 5/24, 0) | 475/384 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| metric | - | -1/192 | (5/24, 5/24, 0) | 955/768 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| metric | - | 1/192 | (5/24, 5/24, 0) | 965/768 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| metric | - | 1/96 | (5/24, 5/24, 0) | 485/384 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| point (refine) | (1, 1, 0) | 1/192 | (41/192, 41/192, 0) | 5/4 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | DIFFERENT | 49cedbdd58376fac | - | True | False |
| point (refine) | (1, 1, 0) | 1/384 | (27/128, 27/128, 0) | 5/4 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | DIFFERENT | 49cedbdd58376fac | - | True | False |
| point (refine) | (1, 1, 0) | 1/768 | (161/768, 161/768, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (19/96, 5/24, 0) | 5/4 | 1 | (36, 54, 20) | 3^4 4^4 5^6 6^2 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (7/32, 5/24, 0) | 5/4 | 1 | (34, 51, 19) | 3^4 4^3 5^4 6^4 8^2 9^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`f654982d74d740f6`** tetragonal IT(141) I4_1/amd witness (0, 1/12, 1/12) c/a 1/2 basis [[0, 1, 0], [0, 0, 1]] base f=(38, 57, 21) 3^6 4^7 6^3 8^2 10^2 14^1 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 1/16, 1/12) | 1/2 | 2 | (29, 45, 18) | 3^4 4^6 6^7 12^1 | 2 | 3 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 7/96, 1/12) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 3/32, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 5/48, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point | (0, 0, 1) | -1/48 | (0, 1/12, 1/16) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (0, 1/12, 7/96) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (0, 1/12, 3/32) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | - | True | False |
| point | (0, 0, 1) | 1/48 | (0, 1/12, 5/48) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | - | True | False |
| metric | - | -1/96 | (0, 1/12, 1/12) | 95/192 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| metric | - | -1/192 | (0, 1/12, 1/12) | 191/384 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| metric | - | 1/192 | (0, 1/12, 1/12) | 193/384 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| metric | - | 1/96 | (0, 1/12, 1/12) | 97/192 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 5/64, 1/12) | 1/2 | 2 | (31, 48, 19) | 3^4 4^8 6^4 8^2 12^1 | 2 | 3 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 31/384, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (0, 1/12, 17/192) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/12, 1/12) | 1/2 | 1 | (20, 30, 12) | 3^1 4^6 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/12, 1/12) | 1/2 | 1 | (20, 30, 12) | 3^1 4^6 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`4f6d3e68cbd9e729`** tetragonal IT(98) I4_122 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(42, 63, 23) 3^6 4^5 5^2 6^6 8^2 12^1 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^1 7^2 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (44, 66, 24) | 3^6 4^9 5^2 6^2 8^2 10^1 12^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | DIFFERENT | 213c7a114d5a97a8 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (44, 66, 24) | 3^6 4^5 5^6 6^3 8^1 10^2 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (44, 66, 24) | 3^6 4^5 5^6 6^3 8^1 10^2 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/4 | 1 | (32, 50, 20) | 3^6 4^5 5^2 6^5 10^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 3/4 | 1 | (32, 50, 20) | 3^6 4^5 5^2 6^5 10^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^2 4^8 6^9 10^1 12^1 | 1 | 0 | DIFFERENT | 14ee43e7e7821ec9 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 3/4 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 3/4 | 1 | (37, 56, 21) | 3^4 4^6 5^3 6^5 7^1 10^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 3/4 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | SAME | 4f6d3e68cbd9e729 | - | True | False |

**`1497877268495988`** tetragonal IT(91) P4_122 witness (0, 1/12, 0) c/a 1/2 basis [[0, 1, 0]] base f=(32, 48, 18) 3^4 4^4 5^4 6^2 8^2 10^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 1/16, 0) | 1/2 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 7/96, 0) | 1/2 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 3/32, 0) | 1/2 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 5/48, 0) | 1/2 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| metric | - | -1/96 | (0, 1/12, 0) | 95/192 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| metric | - | -1/192 | (0, 1/12, 0) | 191/384 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| metric | - | 1/192 | (0, 1/12, 0) | 193/384 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| metric | - | 1/96 | (0, 1/12, 0) | 97/192 | 2 | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 0 | SAME | 1497877268495988 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/12, 0) | 1/2 | 1 | (24, 37, 15) | 3^2 4^6 5^3 6^1 7^1 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/12, 0) | 1/2 | 1 | (24, 37, 15) | 3^2 4^6 5^3 6^1 7^1 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |

**`e0d18e5ea938d649`** tetragonal IT(122) I-42d witness (1/24, 1/4, 1/8) c/a 1 basis [[1, 0, 0]] base f=(36, 54, 20) 3^4 4^8 8^8 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/48, 1/4, 1/8) | 1 | 2 | (32, 48, 18) | 3^4 5^8 7^4 8^2 | 2 | 0 | DIFFERENT | ed4e2709d136f0fc | - | True | False |
| point | (1, 0, 0) | -1/96 | (1/32, 1/4, 1/8) | 1 | 2 | (40, 60, 22) | 3^6 4^8 7^2 9^4 10^2 | 2 | 0 | DIFFERENT | be493ac6bdf911f9 | 82 | True | False |
| point | (1, 0, 0) | 1/96 | (5/96, 1/4, 1/8) | 1 | 2 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (1, 0, 0) | 1/48 | (1/16, 1/4, 1/8) | 1 | 2 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric | - | -1/96 | (1/24, 1/4, 1/8) | 95/96 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| metric | - | -1/192 | (1/24, 1/4, 1/8) | 191/192 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| metric | - | 1/192 | (1/24, 1/4, 1/8) | 193/192 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| metric | - | 1/96 | (1/24, 1/4, 1/8) | 97/96 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (7/192, 1/4, 1/8) | 1 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (3/64, 1/4, 1/8) | 1 | 2 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (17/384, 1/4, 1/8) | 1 | 2 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (11/256, 1/4, 1/8) | 1 | 2 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (65/1536, 1/4, 1/8) | 1 | 2 | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 0 | SAME | e0d18e5ea938d649 | - | True | False |
| point (off-stratum) | (0, 1, 0) | -1/96 | (1/24, 23/96, 1/8) | 1 | 1 | (34, 51, 19) | 3^4 4^8 5^2 8^2 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (0, 1, 0) | 1/96 | (1/24, 25/96, 1/8) | 1 | 1 | (34, 51, 19) | 3^4 4^8 5^2 8^2 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`6797ab70c6015039`** tetragonal IT(76) P4_1 witness (1/8, 1/6, 5/12) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^4 4^4 5^4 6^2 9^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/2 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/2 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/2 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/2 | 1 | (29, 45, 18) | 3^4 4^8 5^2 9^4 | 2 | 3 | DIFFERENT | not stored | - | False | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/64 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/128 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/128 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/64 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | SAME | 6797ab70c6015039 | - | True | False |

**`086ac96faf390886`** tetragonal IT(76) P4_1 witness (1/8, 1/6, 5/12) c/a 7/5 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^2 4^8 5^6 10^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 133/96 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 1337/960 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 1351/960 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 679/480 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 7/5 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 7/5 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | SAME | 086ac96faf390886 | - | True | False |

**`164d4bd63d82d0c3`** tetragonal IT(76) P4_1 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(40, 60, 22) 3^6 4^6 5^2 6^4 11^4 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 0 | DIFFERENT | 6797ab70c6015039 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (44, 66, 24) | 3^10 4^2 5^4 6^2 7^2 11^2 13^2 | 1 | 0 | DIFFERENT | c5eec049a827aebd | 76, 78 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 7^2 10^4 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 0 | DIFFERENT | 086ac96faf390886 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 5/4 | 1 | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 0 | SAME | 164d4bd63d82d0c3 | - | True | False |

**`5dc2479b9bc14edc`** tetragonal IT(98) I4_122 witness (1/12, 3/8, 1/6) c/a 9/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(42, 63, 23) 3^8 4^5 5^2 6^2 8^3 10^2 16^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 9/16 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | DIFFERENT | 3ebbca7ed2eda199 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 9/16 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | DIFFERENT | 3ebbca7ed2eda199 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 9/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^2 4^13 5^2 6^3 8^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 9/16 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | DIFFERENT | 3ebbca7ed2eda199 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 9/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 9/16 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 9/16 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^5 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 9/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 9/16 | 1 | (42, 63, 23) | 3^2 4^13 5^2 6^3 8^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 9/16 | 1 | (42, 63, 23) | 3^2 4^13 5^2 6^3 8^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 285/512 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 573/1024 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 579/1024 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 291/512 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 9/16 | 1 | (37, 56, 21) | 3^7 4^5 5^2 6^2 8^2 9^1 10^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 9/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | SAME | 5dc2479b9bc14edc | - | True | False |

**`3ebbca7ed2eda199`** tetragonal IT(98) I4_122 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(40, 60, 22) 3^4 4^8 5^2 6^5 8^1 12^1 16^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (44, 66, 24) | 3^8 4^7 6^5 8^1 10^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (44, 66, 24) | 3^8 4^7 6^5 8^1 10^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | DIFFERENT | 5dc2479b9bc14edc | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (32, 50, 20) | 3^6 4^5 5^2 6^5 10^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (46, 69, 25) | 3^6 4^12 6^3 8^1 10^1 16^1 20^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (44, 66, 24) | 3^8 4^7 6^5 8^1 10^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | DIFFERENT | 5dc2479b9bc14edc | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^5 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (36, 54, 20) | 3^4 4^8 6^3 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (36, 54, 20) | 3^4 4^8 6^3 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (42, 63, 23) | 3^2 4^13 5^2 6^3 8^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (42, 63, 23) | 3^2 4^13 5^2 6^3 8^1 14^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 1/2 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | DIFFERENT | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 1/2 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | DIFFERENT | 5dc2479b9bc14edc | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (35, 53, 20) | 3^3 4^9 5^2 6^3 8^1 11^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 0 | SAME | 3ebbca7ed2eda199 | - | True | False |

**`7575121042ade3b3`** tetragonal IT(98) I4_122 witness (1/12, 1/12, 0) c/a 7/4 basis [[1, 1, 0]] base f=(32, 48, 18) 4^11 6^4 8^1 10^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 1, 0) | -1/48 | (1/16, 1/16, 0) | 7/4 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| point | (1, 1, 0) | -1/96 | (7/96, 7/96, 0) | 7/4 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| point | (1, 1, 0) | 1/96 | (3/32, 3/32, 0) | 7/4 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| point | (1, 1, 0) | 1/48 | (5/48, 5/48, 0) | 7/4 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| metric | - | -1/96 | (1/12, 1/12, 0) | 665/384 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| metric | - | -1/192 | (1/12, 1/12, 0) | 1337/768 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| metric | - | 1/192 | (1/12, 1/12, 0) | 1351/768 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| metric | - | 1/96 | (1/12, 1/12, 0) | 679/384 | 2 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | SAME | 7575121042ade3b3 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/12, 0) | 7/4 | 1 | (20, 32, 14) | 3^1 4^7 5^3 6^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/12, 0) | 7/4 | 1 | (20, 32, 14) | 3^1 4^7 5^3 6^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |

**`213c7a114d5a97a8`** tetragonal IT(98) I4_122 witness (1/12, 3/8, 1/6) c/a 11/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(42, 63, 23) 3^6 4^4 5^4 6^5 8^2 10^1 16^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 0 | DIFFERENT | 5dc2479b9bc14edc | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^2 4^8 6^9 10^1 12^1 | 1 | 0 | DIFFERENT | 14ee43e7e7821ec9 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 11/16 | 1 | (44, 66, 24) | 3^6 4^9 5^2 6^2 8^2 10^1 12^1 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^2 4^8 6^9 10^1 12^1 | 1 | 0 | DIFFERENT | 14ee43e7e7821ec9 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 11/16 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^2 7^2 8^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 11/16 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^5 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 11/16 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^5 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 11/16 | 1 | (44, 66, 24) | 3^6 4^5 5^6 6^3 8^1 10^2 18^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 11/16 | 1 | (48, 72, 26) | 3^6 4^11 5^2 6^2 8^1 10^2 12^1 20^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1045/1536 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2101/3072 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2123/3072 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1067/1536 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 11/16 | 1 | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 0 | DIFFERENT | f91f4b104fcf5351 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 11/16 | 1 | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 4f6d3e68cbd9e729 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 11/16 | 1 | (37, 56, 21) | 3^5 4^5 5^4 6^3 7^1 8^1 10^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 11/16 | 1 | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 0 | SAME | 213c7a114d5a97a8 | - | True | False |

**`2e8e49eb28497267`** tetragonal IT(95) P4_322 witness (1/12, 3/8, 1/6) c/a 53/40 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(40, 60, 22) 3^6 4^7 5^2 6^1 8^3 10^2 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 53/40 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 7391016f434c6483 | 91 | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 53/40 | 1 | (32, 48, 18) | 3^2 4^6 5^2 6^5 8^2 10^1 | 1 | 0 | DIFFERENT | 9e9ed09ab338b2d5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 53/40 | 1 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | DIFFERENT | 7575121042ade3b3 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 53/40 | 1 | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 0 | DIFFERENT | 7575121042ade3b3 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 53/40 | 1 | (37, 56, 21) | 3^8 4^4 5^2 6^1 7^2 8^2 10^1 16^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1007/768 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 10123/7680 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 10229/7680 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 5141/3840 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 53/40 | 1 | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 9b708cb2bde13500 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 53/40 | 1 | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 0 | SAME | 2e8e49eb28497267 | - | True | False |

**`49cedbdd58376fac`** tetragonal IT(92) P4_12_12 witness (5/24, 5/24, 0) c/a 19/16 basis [[1, 1, 0]] base f=(44, 66, 24) 3^10 4^4 6^4 7^2 12^4 aut 2 ns 0 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 1, 0) | -1/48 | (3/16, 3/16, 0) | 19/16 | 2 | (32, 48, 18) | 4^12 8^6 | 6 | 0 | DIFFERENT | afeb1ae44c1a3443 | - | True | False |
| point | (1, 1, 0) | -1/96 | (19/96, 19/96, 0) | 19/16 | 2 | (32, 48, 18) | 4^12 8^6 | 6 | 0 | DIFFERENT | afeb1ae44c1a3443 | - | True | False |
| point | (1, 1, 0) | 1/96 | (7/32, 7/32, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point | (1, 1, 0) | 1/48 | (11/48, 11/48, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| metric | - | -1/96 | (5/24, 5/24, 0) | 1805/1536 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| metric | - | -1/192 | (5/24, 5/24, 0) | 3629/3072 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| metric | - | 1/192 | (5/24, 5/24, 0) | 3667/3072 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | SAME | 49cedbdd58376fac | - | True | False |
| metric | - | 1/96 | (5/24, 5/24, 0) | 1843/1536 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | SAME | 49cedbdd58376fac | - | True | False |
| point (refine) | (1, 1, 0) | -1/192 | (13/64, 13/64, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | - | True | False |
| point (refine) | (1, 1, 0) | -1/384 | (79/384, 79/384, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | - | True | False |
| point (refine) | (1, 1, 0) | -1/768 | (53/256, 53/256, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | - | True | False |
| point (refine) | (1, 1, 0) | -1/1536 | (319/1536, 319/1536, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | - | True | False |
| point (refine) | (1, 1, 0) | 1/192 | (41/192, 41/192, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point (refine) | (1, 1, 0) | 1/384 | (27/128, 27/128, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point (refine) | (1, 1, 0) | 1/768 | (161/768, 161/768, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| point (refine) | (1, 1, 0) | 1/1536 | (107/512, 107/512, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | 109 | True | False |
| metric (refine) | - | -1/384 | (5/24, 5/24, 0) | 7277/6144 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | SAME | 49cedbdd58376fac | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (19/96, 5/24, 0) | 19/16 | 1 | (29, 44, 17) | 3^4 4^4 5^3 6^1 7^2 8^2 9^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (7/32, 5/24, 0) | 19/16 | 1 | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 12 | 0 | DIFFERENT | 8c69db9e84095469 | 80, 91 | True | False |

**`c49077384aaebeb0`** hexagonal IT(178) P6_122 witness (1/12, 1/6, 1/4) c/a 5/4 basis [[1, 2, 0]] base f=(44, 66, 24) 3^8 4^2 5^6 6^4 9^2 14^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 1/4) | 5/4 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 1/4) | 5/4 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 1/4) | 5/4 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | DIFFERENT | 095ce61d28388c98 | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 1/4) | 5/4 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | DIFFERENT | 095ce61d28388c98 | - | True | False |
| metric | - | -1/96 | (1/12, 1/6, 1/4) | 475/384 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 1/4) | 955/768 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 1/4) | 965/768 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 1/4) | 485/384 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (5/64, 5/32, 1/4) | 5/4 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (17/192, 17/96, 1/4) | 5/4 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | SAME | c49077384aaebeb0 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 1/4) | 5/4 | 1 | (38, 57, 21) | 3^8 4^2 5^2 6^1 7^2 8^4 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 1/4) | 5/4 | 1 | (38, 57, 21) | 3^8 4^2 5^2 6^1 7^2 8^4 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`59585d778cb3a7a4`** hexagonal IT(178) P6_122 witness (1/12, 1/6, 1/4) c/a 3/4 basis [[1, 2, 0]] base f=(40, 60, 22) 3^8 4^4 5^4 6^2 10^2 14^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 1/4) | 3/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 1/4) | 3/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 1/4) | 3/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 1/4) | 3/4 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | b0f80776885f3ae1 | - | True | False |
| metric | - | -1/96 | (1/12, 1/6, 1/4) | 95/128 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 1/4) | 191/256 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 1/4) | 193/256 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 1/4) | 97/128 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | SAME | 59585d778cb3a7a4 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 1/4) | 3/4 | 1 | (32, 48, 18) | 4^9 5^2 6^2 7^2 8^3 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 1/4) | 3/4 | 1 | (32, 48, 18) | 4^9 5^2 6^2 7^2 8^3 | 2 | 0 | DIFFERENT | not stored | - | True | False |

**`095ce61d28388c98`** hexagonal IT(178) P6_122 witness (1/12, 1/6, 1/4) c/a 1 basis [[1, 2, 0]] base f=(40, 60, 22) 3^6 4^6 6^6 7^2 14^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 1/4) | 1 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 1/4) | 1 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 1/4) | 1 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 1/4) | 1 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | DIFFERENT | 9be0f2271a14b6a9 | - | True | False |
| metric | - | -1/96 | (1/12, 1/6, 1/4) | 95/96 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 1/4) | 191/192 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 1/4) | 193/192 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 1/4) | 97/96 | 2 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 0 | SAME | 095ce61d28388c98 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 1/4) | 1 | 1 | (36, 54, 20) | 3^6 4^5 6^2 7^2 8^3 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 1/4) | 1 | 1 | (36, 54, 20) | 3^6 4^5 6^2 7^2 8^3 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`9be0f2271a14b6a9`** hexagonal IT(178) P6_122 witness (1/8, 1/4, 1/4) c/a 1 basis [[1, 2, 0]] base f=(36, 54, 20) 3^2 4^12 6^2 9^2 12^2 aut 4 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (5/48, 5/24, 1/4) | 1 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| point | (1, 2, 0) | -1/96 | (11/96, 11/48, 1/4) | 1 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| point | (1, 2, 0) | 1/96 | (13/96, 13/48, 1/4) | 1 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | DIFFERENT | 59585d778cb3a7a4 | - | True | False |
| point | (1, 2, 0) | 1/48 | (7/48, 7/24, 1/4) | 1 | 2 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 0 | DIFFERENT | 59585d778cb3a7a4 | - | True | False |
| metric | - | -1/96 | (1/8, 1/4, 1/4) | 95/96 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| metric | - | -1/192 | (1/8, 1/4, 1/4) | 191/192 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| metric | - | 1/192 | (1/8, 1/4, 1/4) | 193/192 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| metric | - | 1/96 | (1/8, 1/4, 1/4) | 97/96 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (25/192, 25/96, 1/4) | 1 | 2 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 0 | SAME | 9be0f2271a14b6a9 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (11/96, 1/4, 1/4) | 1 | 1 | (34, 51, 19) | 3^4 4^6 6^4 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (13/96, 1/4, 1/4) | 1 | 1 | (34, 51, 19) | 3^4 4^6 6^4 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`2d654c836f3731c6`** hexagonal IT(178) P6_122 witness (0, 1/8, 1/3) c/a 1 basis [[0, 1, 0]] base f=(36, 54, 20) 3^8 4^2 6^4 7^4 12^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 5/48, 1/3) | 1 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 11/96, 1/3) | 1 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 13/96, 1/3) | 1 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 7/48, 1/3) | 1 | 2 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| metric | - | -1/96 | (0, 1/8, 1/3) | 95/96 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| metric | - | -1/192 | (0, 1/8, 1/3) | 191/192 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| metric | - | 1/192 | (0, 1/8, 1/3) | 193/192 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| metric | - | 1/96 | (0, 1/8, 1/3) | 97/96 | 2 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 0 | SAME | 2d654c836f3731c6 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/8, 1/3) | 1 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | DIFFERENT | 272aefcd5e48ba49 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/8, 1/3) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |

**`b0f80776885f3ae1`** hexagonal IT(178) P6_122 witness (1/12, 1/6, 1/4) c/a 1/2 basis [[1, 2, 0]] base f=(36, 54, 20) 3^6 4^6 5^2 6^2 8^2 14^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 1/4) | 1/2 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 1/4) | 1/2 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 1/4) | 1/2 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 1/4) | 1/2 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| metric | - | -1/96 | (1/12, 1/6, 1/4) | 95/192 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 1/4) | 191/384 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 1/4) | 193/384 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 1/4) | 97/192 | 2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | SAME | b0f80776885f3ae1 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 1/4) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^2 10^1 | 1 | 4 | DIFFERENT | fee2122be9f75053 | 178, 179 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 1/4) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^2 10^1 | 1 | 4 | DIFFERENT | fee2122be9f75053 | 178, 179 | True | False |

**`a348875c3f707895`** hexagonal IT(178) P6_122 witness (0, 1/12, 1/3) c/a 1/2 basis [[0, 1, 0]] base f=(36, 54, 20) 3^4 4^10 6^2 8^2 14^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 1/16, 1/3) | 1/2 | 2 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 7/96, 1/3) | 1/2 | 2 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 3/32, 1/3) | 1/2 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 5/48, 1/3) | 1/2 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| metric | - | -1/96 | (0, 1/12, 1/3) | 95/192 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| metric | - | -1/192 | (0, 1/12, 1/3) | 191/384 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| metric | - | 1/192 | (0, 1/12, 1/3) | 193/384 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| metric | - | 1/96 | (0, 1/12, 1/3) | 97/192 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 5/64, 1/3) | 1/2 | 2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | SAME | a348875c3f707895 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/12, 1/3) | 1/2 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | DIFFERENT | 4885ce1e70fa9713 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/12, 1/3) | 1/2 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | DIFFERENT | 4885ce1e70fa9713 | - | True | False |

**`dcc38ea9177089b9`** hexagonal IT(178) P6_122 witness (1/6, 7/12, 1/12) c/a 1/2 basis [[2, 1, 0]] base f=(36, 54, 20) 3^2 4^8 5^2 7^4 8^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (2, 1, 0) | -1/48 | (1/8, 9/16, 1/12) | 1/2 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| point | (2, 1, 0) | -1/96 | (7/48, 55/96, 1/12) | 1/2 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| point | (2, 1, 0) | 1/96 | (3/16, 19/32, 1/12) | 1/2 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| point | (2, 1, 0) | 1/48 | (5/24, 29/48, 1/12) | 1/2 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| metric | - | -1/96 | (1/6, 7/12, 1/12) | 95/192 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| metric | - | -1/192 | (1/6, 7/12, 1/12) | 191/384 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| metric | - | 1/192 | (1/6, 7/12, 1/12) | 193/384 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| metric | - | 1/96 | (1/6, 7/12, 1/12) | 97/192 | 2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 0 | SAME | dcc38ea9177089b9 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (5/32, 7/12, 1/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 5^1 6^1 7^3 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (17/96, 7/12, 1/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 5^1 6^1 7^3 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |

**`5b86a254c715306c`** hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 797/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(40, 60, 22) 3^8 4^6 6^4 10^2 14^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | DIFFERENT | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 15143/19200 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 152227/192000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 153821/192000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 77309/96000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 797/1000 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | SAME | 5b86a254c715306c | - | True | False |

**`f05f0b009e0929f6`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^6 5^6 6^2 12^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^2 4^10 5^4 8^2 13^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | DIFFERENT | d9ac68100a276dfe | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | SAME | f05f0b009e0929f6 | - | True | False |

**`d70e6901953070e7`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(38, 58, 22) 3^6 4^8 6^3 7^2 8^1 10^1 16^1 aut 1 ns 2 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (19, 31, 14) | 3^4 4^5 5^2 6^2 8^1 | 1 | 5 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (24, 39, 17) | 3^4 4^8 6^4 10^1 | 1 | 6 | DIFFERENT | 1d81d76adec2770e | 155 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (24, 37, 15) | 3^2 4^5 5^2 6^5 8^1 | 1 | 2 | DIFFERENT | 550900e445751dbc | 155 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (30, 46, 18) | 3^2 4^8 5^2 6^4 8^1 12^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 3/4 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 3/4 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 3/4 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 3/4 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | SAME | d70e6901953070e7 | - | True | False |

**`e1a38303b2378f17`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 1277/2000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(40, 60, 22) 3^8 4^6 6^2 7^2 8^2 15^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 5^2 7^2 9^2 15^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 24263/38400 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 243907/384000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 246461/384000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 123869/192000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1277/2000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | SAME | e1a38303b2378f17 | - | True | False |

**`c82ebc15c49c1413`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 527/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(38, 57, 21) 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 527/1000 | 1 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | b0f80776885f3ae1 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | cbead3df2d2f1d0e | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 527/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 527/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | cbead3df2d2f1d0e | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 527/1000 | 1 | (29, 44, 17) | 3^7 4^2 5^2 6^2 8^2 10^1 11^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 527/1000 | 1 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | b0f80776885f3ae1 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 10013/19200 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 100657/192000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 101711/192000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 51119/96000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 527/1000 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 527/1000 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | SAME | c82ebc15c49c1413 | - | True | False |

**`f6f8b3050a1eef42`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(38, 57, 21) 3^4 4^11 6^2 10^2 12^1 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 7e05ce00d8a7cbf6 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | DIFFERENT | ac4489d658eb445e | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^6 4^7 6^2 8^1 10^3 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (31, 47, 18) | 3^4 4^8 5^1 6^1 9^1 10^3 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^4 4^11 5^2 6^2 10^1 11^2 16^1 | 1 | 0 | DIFFERENT | a23144f3446070e6 | 178, 179 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (36, 54, 20) | 3^6 4^7 6^2 8^1 10^3 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (42, 63, 23) | 3^4 4^11 5^2 6^2 10^1 11^2 16^1 | 1 | 0 | DIFFERENT | a23144f3446070e6 | 178, 179 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | DIFFERENT | ac4489d658eb445e | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/4 | 1 | (42, 63, 23) | 3^4 4^11 5^2 6^2 10^1 11^2 16^1 | 1 | 0 | DIFFERENT | a23144f3446070e6 | 178, 179 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 3/4 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | SAME | f6f8b3050a1eef42 | - | True | False |

**`9c0b7e0c29dfebb2`** hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^4 4^8 5^2 7^4 13^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 3/4 | 1 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 0 | DIFFERENT | 5b86a254c715306c | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 3/4 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |
| metric (refine) | - | 1/384 | (1/12, 3/8, 1/6) | 385/512 | 1 | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 0 | SAME | 9c0b7e0c29dfebb2 | - | True | False |

**`87c94384d7851cb2`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 797/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(34, 52, 20) 3^4 4^6 5^2 6^6 8^1 14^1 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 797/1000 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 797/1000 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 797/1000 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^5 5^4 6^4 8^2 12^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 797/1000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 797/1000 | 1 | (24, 37, 15) | 3^2 4^5 5^2 6^5 8^1 | 1 | 2 | DIFFERENT | 550900e445751dbc | 155 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 797/1000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 797/1000 | 1 | (40, 61, 23) | 3^10 4^3 5^2 6^2 7^2 8^1 10^2 16^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 15143/19200 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 152227/192000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 153821/192000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 77309/96000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 797/1000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 797/1000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 797/1000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 797/1000 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | SAME | 87c94384d7851cb2 | - | True | False |

**`a35623e347ef03b4`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 4^10 6^6 10^2 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | SAME | a35623e347ef03b4 | - | True | False |

**`e98412e7cb95aea2`** hexagonal IT(152) P3_121 witness (0, 1/8, 1/6) c/a 3/4 basis [[0, 1, 0]] base f=(32, 48, 18) 3^4 4^6 6^2 8^6 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 5/48, 1/6) | 3/4 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 11/96, 1/6) | 3/4 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 13/96, 1/6) | 3/4 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 7/48, 1/6) | 3/4 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | -1/96 | (0, 1/8, 1/6) | 95/128 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| metric | - | -1/192 | (0, 1/8, 1/6) | 191/256 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| metric | - | 1/192 | (0, 1/8, 1/6) | 193/256 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| metric | - | 1/96 | (0, 1/8, 1/6) | 97/128 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | SAME | e98412e7cb95aea2 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | DIFFERENT | 5b679d8b0a3147c3 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | DIFFERENT | 5b679d8b0a3147c3 | - | True | False |

**`ac4489d658eb445e`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 797/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 4^13 5^2 6^1 9^2 10^1 12^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 797/1000 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 7e05ce00d8a7cbf6 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 797/1000 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | 7e05ce00d8a7cbf6 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 797/1000 | 1 | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 0 | DIFFERENT | f6f8b3050a1eef42 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^7 6^2 8^1 10^3 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 797/1000 | 1 | (33, 50, 19) | 3^5 4^7 5^2 8^1 9^3 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 797/1000 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 797/1000 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 797/1000 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 9^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 15143/19200 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 152227/192000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 153821/192000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 77309/96000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 797/1000 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | SAME | ac4489d658eb445e | - | True | False |

**`c53bc05bc306c97d`** hexagonal IT(166) R-3m witness (1/12, 1/6, 11/24) c/a 7/8 basis [[1, 2, 0], [0, 0, 1]] base f=(31, 48, 19) 3^4 4^8 5^4 8^2 16^1 aut 2 ns 3 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 11/24) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 11/24) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 11/24) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 11/24) | 7/8 | 2 | (29, 45, 18) | 3^10 4^2 8^5 12^1 | 2 | 3 | DIFFERENT | cfa3bfb9fefaaa21 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 1/6, 7/16) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 1/6, 43/96) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 1/6, 15/32) | 7/8 | 2 | (30, 46, 18) | 3^4 4^8 6^2 8^3 12^1 | 2 | 2 | DIFFERENT | b8a3099f8963dc67 | 148, 155, 166 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 1/6, 23/48) | 7/8 | 2 | (30, 46, 18) | 3^4 4^8 6^2 8^3 12^1 | 2 | 2 | DIFFERENT | b8a3099f8963dc67 | 148, 155, 166 | True | False |
| metric | - | -1/96 | (1/12, 1/6, 11/24) | 665/768 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| metric | - | -1/192 | (1/12, 1/6, 11/24) | 1337/1536 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 11/24) | 1351/1536 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 11/24) | 679/768 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (17/192, 17/96, 11/24) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (11/128, 11/64, 11/24) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (65/768, 65/384, 11/24) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 1/6, 89/192) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 1/6, 59/128) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 1/6, 353/768) | 7/8 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 1/6, 235/512) | 7/8 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | SAME | c53bc05bc306c97d | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 11/24) | 7/8 | 1 | (18, 27, 11) | 3^2 4^4 5^3 8^1 9^1 | 1 | 0 | DIFFERENT | f9490a5b6fce3ae5 | 166 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 11/24) | 7/8 | 1 | (18, 27, 11) | 3^2 4^4 5^3 8^1 9^1 | 1 | 0 | DIFFERENT | f9490a5b6fce3ae5 | 166 | True | False |

**`8cc8c5ab3cf36d8f`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^6 4^4 5^4 6^2 9^2 10^1 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 5/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 5/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 5/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 6^6 7^2 8^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 475/384 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 955/768 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 965/768 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 485/384 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 5/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 5/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 5/4 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | SAME | 8cc8c5ab3cf36d8f | - | True | False |

**`646b518ccf3bd724`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 15/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^6 4^4 5^2 6^4 7^2 13^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 15/16 | 1 | (40, 60, 22) | 3^8 4^4 5^4 7^2 9^2 14^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/512 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/1024 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/1024 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/512 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 0 | SAME | 646b518ccf3bd724 | - | True | False |

**`7a448bed1119dfad`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^2 4^10 5^2 6^2 8^2 12^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (34, 51, 19) | 3^2 4^9 6^4 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (29, 44, 17) | 3^1 4^10 6^2 8^3 9^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (34, 51, 19) | 3^2 4^9 6^4 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (34, 51, 19) | 3^2 4^9 6^4 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 0 | SAME | 7a448bed1119dfad | - | True | False |

**`7e023be581e7c50a`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^6 4^6 6^2 8^4 10^1 12^1 aut 1 ns 0 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^2 4^11 5^2 6^1 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | cbead3df2d2f1d0e | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | DIFFERENT | cbead3df2d2f1d0e | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^1 4^11 6^1 8^3 11^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (36, 54, 20) | 3^2 4^11 5^2 6^1 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 3/4 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | SAME | 7e023be581e7c50a | - | True | False |

**`7e05ce00d8a7cbf6`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 137/160 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(38, 57, 21) 3^4 4^8 5^2 6^3 8^2 12^1 14^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^10 6^2 8^1 9^2 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 137/160 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 137/160 | 1 | (33, 50, 19) | 3^5 4^7 5^2 8^1 9^3 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^10 6^2 8^1 9^2 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 137/160 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 137/160 | 1 | (38, 57, 21) | 3^4 4^10 5^2 8^1 10^3 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 9^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 2603/3072 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 26167/30720 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 26441/30720 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 13289/15360 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 137/160 | 1 | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 0 | DIFFERENT | ac4489d658eb445e | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 137/160 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | DIFFERENT | d718e083bd23d2b1 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 137/160 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | DIFFERENT | d718e083bd23d2b1 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 137/160 | 1 | (38, 57, 21) | 3^4 4^10 6^2 8^1 9^2 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 137/160 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | DIFFERENT | d718e083bd23d2b1 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 137/160 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | DIFFERENT | d718e083bd23d2b1 | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 137/160 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | SAME | 7e05ce00d8a7cbf6 | - | True | False |

**`59b28b3a59c27092`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 1277/2000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(34, 52, 20) 3^8 4^2 5^2 6^4 8^3 14^1 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1277/2000 | 1 | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 2 | DIFFERENT | d70e6901953070e7 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1277/2000 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^4 4^5 5^4 6^4 8^2 12^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1277/2000 | 1 | (28, 43, 17) | 3^4 4^5 5^2 6^3 8^2 10^1 | 1 | 2 | DIFFERENT | 819dfbe16f40f3f9 | 155 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 24263/38400 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 243907/384000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 246461/384000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 123869/192000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1277/2000 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | SAME | 59b28b3a59c27092 | - | True | False |

**`d9ac68100a276dfe`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 2777/4000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^4 4^6 5^4 6^2 7^2 13^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 2777/4000 | 1 | (40, 60, 22) | 3^8 4^6 5^2 7^2 9^2 15^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 2777/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 2777/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 52763/76800 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 530407/768000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 535961/768000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 269369/384000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 2777/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 2777/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 2777/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 2777/4000 | 1 | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 0 | SAME | d9ac68100a276dfe | - | True | False |

**`6f4101f83371033d`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 2331/4000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^4 4^8 6^4 7^2 13^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 2331/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | DIFFERENT | 85244add8d1f2d55 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 2331/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | DIFFERENT | 85244add8d1f2d55 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 2331/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | a348875c3f707895 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 2331/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 2331/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | DIFFERENT | 85244add8d1f2d55 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 2331/4000 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | DIFFERENT | 85244add8d1f2d55 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 14763/25600 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 148407/256000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 149961/256000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 75369/128000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 2331/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 2331/4000 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 2331/4000 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | SAME | 6f4101f83371033d | - | True | False |

**`f0b07b168368759b`** hexagonal IT(148) R-3 witness (0, 1/2, 0) c/a 3/4 basis [] base f=(14, 24, 12) 3^4 4^4 5^4 aut 4 ns 6 — POINT n/a / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| metric | - | -1/96 | (0, 1/2, 0) | 95/128 | 2 | (14, 24, 12) | 3^4 4^4 5^4 | 4 | 6 | SAME | f0b07b168368759b | - | True | False |
| metric | - | -1/192 | (0, 1/2, 0) | 191/256 | 2 | (14, 24, 12) | 3^4 4^4 5^4 | 4 | 6 | SAME | f0b07b168368759b | - | True | False |
| metric | - | 1/192 | (0, 1/2, 0) | 193/256 | 2 | (14, 24, 12) | 3^4 4^4 5^4 | 4 | 6 | SAME | f0b07b168368759b | - | True | False |
| metric | - | 1/96 | (0, 1/2, 0) | 97/128 | 2 | (14, 24, 12) | 3^4 4^4 5^4 | 4 | 6 | SAME | f0b07b168368759b | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/2, 0) | 3/4 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/2, 0) | 3/4 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |

**`56918d2cff883e22`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(22, 34, 14) 4^8 5^2 6^2 7^2 aut 2 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | DIFFERENT | f429e996b3f455a6 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | DIFFERENT | f429e996b3f455a6 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | DIFFERENT | f429e996b3f455a6 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | SAME | 56918d2cff883e22 | - | True | False |

**`f429e996b3f455a6`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^6 5^6 8^4 aut 2 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^2 4^1 5^10 6^2 8^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 2 | SAME | f429e996b3f455a6 | - | True | False |

**`71d2c9953ca110b8`** hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 39/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^4 4^2 5^8 6^2 7^2 11^2 aut 1 ns 0 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1235/1024 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2483/2048 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2509/2048 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1261/1024 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 39/32 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/12, 575/1536, 1/6) | 39/32 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 39/32 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 4979/4096 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 9971/8192 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | DIFFERENT | 16025e0680843c36 | - | True | False |
| metric (refine) | - | -1/1536 | (1/12, 3/8, 1/6) | 19955/16384 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |
| metric (refine) | - | 1/384 | (1/12, 3/8, 1/6) | 5005/4096 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | 1/768 | (1/12, 3/8, 1/6) | 9997/8192 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | 1/1536 | (1/12, 3/8, 1/6) | 19981/16384 | 1 | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 0 | SAME | 71d2c9953ca110b8 | - | True | False |

**`8d90c524c89922d9`** hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 11/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^4 4^4 5^4 6^4 7^2 11^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 11/8 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 11/8 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 11/8 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1045/768 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2101/1536 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2123/1536 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1067/768 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | SAME | 8d90c524c89922d9 | - | True | False |

**`9d4396ca0b08fc3c`** hexagonal IT(166) R-3m witness (1/24, 1/12, 1/12) c/a 3/4 basis [[1, 2, 0], [0, 0, 1]] base f=(19, 30, 13) 4^8 5^4 8^1 aut 2 ns 3 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/48, 1/24, 1/12) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | -1/96 | (1/32, 1/16, 1/12) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | 1/96 | (5/96, 5/48, 1/12) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | 1/48 | (1/16, 1/8, 1/12) | 3/4 | 2 | (17, 28, 13) | 4^12 8^1 | 8 | 5 | DIFFERENT | a3164ecfcd75d3ec | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/24, 1/12, 1/16) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/24, 1/12, 7/96) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/24, 1/12, 3/32) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/24, 1/12, 5/48) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| metric | - | -1/96 | (1/24, 1/12, 1/12) | 95/128 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| metric | - | -1/192 | (1/24, 1/12, 1/12) | 191/256 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| metric | - | 1/192 | (1/24, 1/12, 1/12) | 193/256 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| metric | - | 1/96 | (1/24, 1/12, 1/12) | 97/128 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | SAME | 9d4396ca0b08fc3c | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (1/32, 1/12, 1/12) | 3/4 | 1 | (12, 18, 8) | 4^4 5^4 | 8 | 0 | DIFFERENT | abfdf73c2f298784 | 76, 78, 80, 88, 91, 92, 109, 141, 148, 160, 167 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (5/96, 1/12, 1/12) | 3/4 | 1 | (12, 18, 8) | 4^4 5^4 | 8 | 0 | DIFFERENT | abfdf73c2f298784 | 76, 78, 80, 88, 91, 92, 109, 141, 148, 160, 167 | True | False |

**`07d543d89e2934f2`** hexagonal IT(152) P3_121 witness (1/8, 1/6, 5/12) c/a 33/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^6 4^4 5^2 6^4 10^4 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 33/32 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | DIFFERENT | d0c5a15c25ab6413 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 33/32 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 33/32 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 33/32 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 33/32 | 1 | (32, 48, 18) | 3^4 4^2 5^4 6^4 8^4 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 33/32 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | DIFFERENT | d0c5a15c25ab6413 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 33/32 | 1 | (34, 51, 19) | 3^2 4^11 6^2 10^4 | 2 | 0 | DIFFERENT | 364e84ece2d20d22 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1045/1024 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 2101/2048 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 2123/2048 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1067/1024 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | DIFFERENT | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 33/32 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | DIFFERENT | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 33/32 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | DIFFERENT | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 33/32 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | SAME | 07d543d89e2934f2 | - | True | False |

**`2081d7b9a734e4fe`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 11/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 50, 20) 3^6 4^4 5^4 6^4 10^1 12^1 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 11/8 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 11/8 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | DIFFERENT | d9bf7fb7a80eaa38 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 11/8 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 11/8 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 11/8 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 11/8 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | DIFFERENT | d9bf7fb7a80eaa38 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 11/8 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 11/8 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1045/768 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 2101/1536 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 2123/1536 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1067/768 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 11/8 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | SAME | 2081d7b9a734e4fe | - | True | False |

**`257b627a90b78038`** hexagonal IT(180) P6_222 witness (1/6, 7/12, 1/6) c/a 1 basis [[2, 1, 0]] base f=(22, 35, 15) 3^4 4^6 6^3 8^2 aut 2 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (2, 1, 0) | -1/48 | (1/8, 9/16, 1/6) | 1 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| point | (2, 1, 0) | -1/96 | (7/48, 55/96, 1/6) | 1 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| point | (2, 1, 0) | 1/96 | (3/16, 19/32, 1/6) | 1 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| point | (2, 1, 0) | 1/48 | (5/24, 29/48, 1/6) | 1 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| metric | - | -1/96 | (1/6, 7/12, 1/6) | 95/96 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| metric | - | -1/192 | (1/6, 7/12, 1/6) | 191/192 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| metric | - | 1/192 | (1/6, 7/12, 1/6) | 193/192 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| metric | - | 1/96 | (1/6, 7/12, 1/6) | 97/96 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | SAME | 257b627a90b78038 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (5/32, 7/12, 1/6) | 1 | 1 | (16, 26, 12) | 3^1 4^8 5^1 6^2 | 1 | 4 | DIFFERENT | dc51033babc85fc2 | 180, 181 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (17/96, 7/12, 1/6) | 1 | 1 | (16, 26, 12) | 3^1 4^8 5^1 6^2 | 1 | 4 | DIFFERENT | dc51033babc85fc2 | 180, 181 | True | False |

**`3ddc41389e6d484f`** hexagonal IT(171) P6_2 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^2 5^2 6^3 7^2 9^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^8 5^2 8^3 10^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^8 5^2 8^3 10^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 0 | SAME | 3ddc41389e6d484f | - | True | False |

**`64203f15fcf6c09b`** hexagonal IT(155) R32 witness (0, 1/24, 0) c/a 1/2 basis [[0, 1, 0]] base f=(20, 32, 14) 3^4 4^4 5^2 6^2 7^2 aut 2 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 1/48, 0) | 1/2 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| point | (0, 1, 0) | -1/96 | (0, 1/32, 0) | 1/2 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| point | (0, 1, 0) | 1/96 | (0, 5/96, 0) | 1/2 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 1/16, 0) | 1/2 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| metric | - | -1/96 | (0, 1/24, 0) | 95/192 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| metric | - | -1/192 | (0, 1/24, 0) | 191/384 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| metric | - | 1/192 | (0, 1/24, 0) | 193/384 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| metric | - | 1/96 | (0, 1/24, 0) | 97/192 | 2 | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 4 | SAME | 64203f15fcf6c09b | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/24, 0) | 1/2 | 1 | (16, 26, 12) | 3^6 4^2 6^2 7^2 | 2 | 4 | DIFFERENT | 4eaa641c282f54ad | 155, 166 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/24, 0) | 1/2 | 1 | (16, 26, 12) | 3^6 4^2 6^2 7^2 | 2 | 4 | DIFFERENT | 4eaa641c282f54ad | 155, 166 | True | False |

**`d718e083bd23d2b1`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 4^13 8^4 12^1 aut 4 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1 | 1 | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 0 | DIFFERENT | 8cc8c5ab3cf36d8f | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 9^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/96 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/192 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/192 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/96 | 1 | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 0 | SAME | d718e083bd23d2b1 | - | True | False |

**`f14a8c4e7c5b3e3a`** hexagonal IT(180) P6_222 witness (1/8, 1/6, 5/12) c/a 7/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^2 5^2 6^4 8^2 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 7/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 665/384 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 1337/768 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 1351/768 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 679/384 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 0 | SAME | f14a8c4e7c5b3e3a | - | True | False |

**`29bbba1adec778da`** hexagonal IT(171) P6_2 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^2 4^4 5^4 6^3 7^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^4 8^3 10^1 | 1 | 0 | DIFFERENT | 42b088d0062340e5 | 171, 172 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^4 8^3 10^1 | 1 | 0 | DIFFERENT | 42b088d0062340e5 | 171, 172 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 0 | SAME | 29bbba1adec778da | - | True | False |

**`66563d07a1110a25`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(36, 54, 20) 3^8 4^2 6^5 8^2 10^3 aut 1 ns 0 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^3 8^1 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (26, 40, 16) | 3^2 4^8 5^2 8^4 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 1 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 1 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 1 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 1 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 385/384 | 1 | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 0 | SAME | 66563d07a1110a25 | - | True | False |

**`ce3b42c8a4ceff6f`** hexagonal IT(151) P3_112 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(34, 51, 19) 3^6 4^6 6^2 8^3 12^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | DIFFERENT | 36ec4ad2f530e145 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | DIFFERENT | e198aac88f223892 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 0 | SAME | ce3b42c8a4ceff6f | - | True | False |

**`7b9cfe26fe4a9c4b`** hexagonal IT(146) R3 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(18, 30, 14) 3^4 4^6 6^4 aut 2 ns 6 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 5/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | SAME | 7b9cfe26fe4a9c4b | - | True | False |

**`2b9726574a0a8bed`** hexagonal IT(171) P6_2 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^4 4^4 5^2 6^1 7^4 9^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | DIFFERENT | 27d463eac6cda5ea | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | SAME | 2b9726574a0a8bed | - | True | False |

**`f07d69523ef41b37`** hexagonal IT(178) P6_122 witness (1/6, 1/3, 1/4) c/a 3/2 basis [[1, 2, 0]] base f=(20, 36, 18) 3^10 4^4 5^2 8^2 aut 2 ns 12 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (7/48, 7/24, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point | (1, 2, 0) | -1/96 | (5/32, 5/16, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point | (1, 2, 0) | 1/96 | (17/96, 17/48, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point | (1, 2, 0) | 1/48 | (3/16, 3/8, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric | - | -1/96 | (1/6, 1/3, 1/4) | 95/64 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric | - | -1/192 | (1/6, 1/3, 1/4) | 191/128 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric | - | 1/192 | (1/6, 1/3, 1/4) | 193/128 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric | - | 1/96 | (1/6, 1/3, 1/4) | 97/64 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (31/192, 31/96, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (21/128, 21/64, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (127/768, 127/384, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (85/512, 85/256, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (11/64, 11/32, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (65/384, 65/192, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (43/256, 43/128, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (257/1536, 257/768, 1/4) | 3/2 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric (refine) | - | -1/384 | (1/6, 1/3, 1/4) | 383/256 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric (refine) | - | -1/768 | (1/6, 1/3, 1/4) | 767/512 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric (refine) | - | -1/1536 | (1/6, 1/3, 1/4) | 1535/1024 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric (refine) | - | -1/3072 | (1/6, 1/3, 1/4) | 3071/2048 | 2 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 0 | DIFFERENT | c49077384aaebeb0 | - | True | False |
| metric (refine) | - | 1/384 | (1/6, 1/3, 1/4) | 385/256 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric (refine) | - | 1/768 | (1/6, 1/3, 1/4) | 769/512 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric (refine) | - | 1/1536 | (1/6, 1/3, 1/4) | 1537/1024 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| metric (refine) | - | 1/3072 | (1/6, 1/3, 1/4) | 3073/2048 | 2 | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 2 | DIFFERENT | 254345236188cc50 | 169, 170 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (5/32, 1/3, 1/4) | 3/2 | 1 | (34, 51, 19) | 3^2 4^8 6^5 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (17/96, 1/3, 1/4) | 3/2 | 1 | (34, 51, 19) | 3^2 4^8 6^5 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`16025e0680843c36`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^4 5^8 6^2 11^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^4 5^8 8^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 0 | SAME | 16025e0680843c36 | - | True | False |

**`d10bb4a25bbf4c80`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 797/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^2 5^4 7^2 8^2 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^2 4^11 5^2 6^1 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 797/1000 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 797/1000 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 797/1000 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 797/1000 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 797/1000 | 1 | (29, 44, 17) | 3^1 4^11 6^1 8^3 11^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 797/1000 | 1 | (38, 57, 21) | 3^4 4^9 6^4 7^2 12^1 16^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 15143/19200 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 152227/192000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 153821/192000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 77309/96000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 797/1000 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 797/1000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | SAME | d10bb4a25bbf4c80 | - | True | False |

**`e0bf1a48f096c10d`** hexagonal IT(180) P6_222 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 4^8 5^6 6^2 10^1 12^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^10 6^2 10^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^10 6^2 10^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^8 5^4 6^2 8^1 12^2 | 1 | 0 | DIFFERENT | 1f08da5f6863d52a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^10 6^2 10^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (34, 51, 19) | 3^2 4^8 5^4 6^2 8^1 12^2 | 1 | 0 | DIFFERENT | 1f08da5f6863d52a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (25, 39, 16) | 4^11 5^2 6^1 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1 | 1 | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | 7311ebf1145936e7 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 1 | 1 | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 0 | SAME | e0bf1a48f096c10d | - | True | False |

**`b2430fc4bea4e06d`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(34, 51, 19) 3^8 4^2 5^2 6^2 8^3 12^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | b0f80776885f3ae1 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | DIFFERENT | c82ebc15c49c1413 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | DIFFERENT | c82ebc15c49c1413 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (29, 44, 17) | 3^7 4^2 5^2 6^2 8^2 10^1 11^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | DIFFERENT | c82ebc15c49c1413 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 0 | DIFFERENT | b0f80776885f3ae1 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1/2 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | DIFFERENT | c82ebc15c49c1413 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1/2 | 1 | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 0 | DIFFERENT | c82ebc15c49c1413 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | SAME | b2430fc4bea4e06d | - | True | False |

**`bff9b24ce78050f5`** hexagonal IT(144) P3_1 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 4^8 5^4 8^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | SAME | bff9b24ce78050f5 | - | True | False |

**`4db369a636f4396b`** hexagonal IT(151) P3_112 witness (0, 1/2, 0) c/a 3/2 basis [[2, 1, 0]] base f=(18, 30, 14) 3^4 4^6 6^4 aut 4 ns 6 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (2, 1, 0) | -1/48 | (-1/24, 23/48, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point | (2, 1, 0) | -1/96 | (-1/48, 47/96, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point | (2, 1, 0) | 1/96 | (1/48, 49/96, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point | (2, 1, 0) | 1/48 | (1/24, 25/48, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric | - | -1/96 | (0, 1/2, 0) | 95/64 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric | - | -1/192 | (0, 1/2, 0) | 191/128 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric | - | 1/192 | (0, 1/2, 0) | 193/128 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric | - | 1/96 | (0, 1/2, 0) | 97/64 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | -1/192 | (-1/96, 95/192, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | -1/384 | (-1/192, 191/384, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | -1/768 | (-1/384, 383/768, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | -1/1536 | (-1/768, 767/1536, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | 1/192 | (1/96, 97/192, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | 1/384 | (1/192, 193/384, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | 1/768 | (1/384, 385/768, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (refine) | (2, 1, 0) | 1/1536 | (1/768, 769/1536, 0) | 3/2 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric (refine) | - | -1/384 | (0, 1/2, 0) | 383/256 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | -1/768 | (0, 1/2, 0) | 767/512 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | -1/1536 | (0, 1/2, 0) | 1535/1024 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | -1/3072 | (0, 1/2, 0) | 3071/2048 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | 1/384 | (0, 1/2, 0) | 385/256 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric (refine) | - | 1/768 | (0, 1/2, 0) | 769/512 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/2, 0) | 1537/1024 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/2, 0) | 3073/2048 | 2 | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 0 | DIFFERENT | e948828e76447bbb | 120, 144, 145, 151, 152, 153, 154, 169, 170, 171, 172, 178, 179 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/2, 0) | 3/2 | 1 | (22, 34, 14) | 3^4 4^4 6^5 10^1 | 2 | 2 | DIFFERENT | 8e6a80eb6f0f31a9 | 151, 153, 180, 181 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/2, 0) | 3/2 | 1 | (22, 34, 14) | 3^4 4^4 6^5 10^1 | 2 | 2 | DIFFERENT | 8e6a80eb6f0f31a9 | 151, 153, 180, 181 | True | False |

**`042c19cbfdc869cb`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^2 5^2 6^2 7^2 8^3 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/2 | 1 | (25, 39, 16) | 3^4 4^3 5^4 6^2 7^2 8^1 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/2 | 1 | (25, 39, 16) | 3^4 4^3 5^4 6^2 7^2 8^1 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/64 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/128 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/128 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/64 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/2 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | SAME | 042c19cbfdc869cb | - | True | False |

**`23594bd7053503aa`** hexagonal IT(153) P3_212 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^2 5^2 6^3 7^2 8^1 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (34, 51, 19) | 3^4 4^6 5^2 6^3 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (34, 51, 19) | 3^4 4^6 5^2 6^3 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (34, 51, 19) | 3^4 4^6 5^2 6^3 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (27, 41, 16) | 3^4 4^3 5^3 6^2 7^2 8^1 9^1 | 1 | 1 | DIFFERENT | 92ad2666bcd9d321 | 151, 153 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (34, 51, 19) | 3^4 4^6 5^2 6^3 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (34, 51, 19) | 3^4 4^6 5^2 6^3 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 1 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 1 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | SAME | 23594bd7053503aa | - | True | False |

**`f5fbebffa76808d5`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(31, 47, 18) 3^3 4^2 5^7 6^3 7^2 10^1 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 5/4 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | DIFFERENT | 272aefcd5e48ba49 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 5/4 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 5/4 | 1 | (40, 60, 22) | 3^4 4^6 5^2 6^7 8^1 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 475/384 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 955/768 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 965/768 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 485/384 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | SAME | f5fbebffa76808d5 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^6 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^6 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^6 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^6 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 5/4 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`057255f61286b052`** hexagonal IT(167) R-3c witness (0, 3/8, 1/4) c/a 1/2 basis [[0, 1, 0]] base f=(24, 38, 16) 3^6 4^2 6^6 7^2 aut 2 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 17/48, 1/4) | 1/2 | 2 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 35/96, 1/4) | 1/2 | 2 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 37/96, 1/4) | 1/2 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 19/48, 1/4) | 1/2 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| metric | - | -1/96 | (0, 3/8, 1/4) | 95/192 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| metric | - | -1/192 | (0, 3/8, 1/4) | 191/384 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| metric | - | 1/192 | (0, 3/8, 1/4) | 193/384 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| metric | - | 1/96 | (0, 3/8, 1/4) | 97/192 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 71/192, 1/4) | 1/2 | 2 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 143/384, 1/4) | 1/2 | 2 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | SAME | 057255f61286b052 | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 3/8, 1/4) | 1/2 | 1 | (23, 36, 15) | 3^4 4^4 5^2 6^2 7^2 8^1 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 3/8, 1/4) | 1/2 | 1 | (23, 36, 15) | 3^4 4^4 5^2 6^2 7^2 8^1 | 1 | 3 | DIFFERENT | not stored | - | True | False |

**`e198aac88f223892`** hexagonal IT(153) P3_212 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^2 4^5 5^4 6^4 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | 23594bd7053503aa | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (25, 38, 15) | 3^1 4^6 5^4 6^2 8^1 9^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | 23594bd7053503aa | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 0 | DIFFERENT | f05f0b009e0929f6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | 23594bd7053503aa | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 0 | SAME | e198aac88f223892 | - | True | False |

**`d07f950b8309de82`** hexagonal IT(171) P6_2 witness (1/8, 1/6, 5/12) c/a 67/80 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^4 4^3 5^2 6^5 8^2 10^1 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^4 8^4 | 2 | 0 | DIFFERENT | 303d3c41bbb6461d | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 67/80 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 67/80 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 67/80 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 67/80 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 67/80 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 67/80 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 67/80 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1273/1536 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 12797/15360 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 12931/15360 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 6499/7680 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 67/80 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 67/80 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 67/80 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 67/80 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 0 | SAME | d07f950b8309de82 | - | True | False |

**`a182e87006c7a00d`** hexagonal IT(179) P6_522 witness (1/8, 1/6, 5/12) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^1 5^2 6^3 7^2 8^4 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/2 | 1 | (25, 39, 16) | 3^4 4^3 5^2 6^5 7^2 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/2 | 1 | (25, 39, 16) | 3^4 4^3 5^2 6^5 7^2 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/2 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/2 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | DIFFERENT | 0948aa6184f13a8a | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/64 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/128 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/128 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/64 | 1 | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 0 | SAME | a182e87006c7a00d | - | True | False |

**`a46cbaad3c23e834`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 49, 19) 3^4 4^8 5^2 6^2 8^1 10^1 14^1 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 2 | DIFFERENT | 59b28b3a59c27092 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (32, 49, 19) | 3^8 4^2 6^5 8^3 12^1 | 1 | 2 | DIFFERENT | 852443780b89673b | 155 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (27, 43, 18) | 3^6 4^7 6^3 8^1 14^1 | 1 | 5 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1/2 | 1 | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 2 | SAME | a46cbaad3c23e834 | - | True | False |

**`dd3fb07fe11d73d3`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(31, 47, 18) 3^4 4^7 6^3 7^2 10^1 12^1 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 2 | 1 | (31, 47, 18) | 3^4 4^5 5^4 7^2 8^1 10^2 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 2 | 1 | (26, 41, 17) | 3^8 4^2 5^2 6^1 7^2 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/48 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/96 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/96 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/48 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | SAME | dd3fb07fe11d73d3 | - | True | False |

**`36c92427e3d084dc`** hexagonal IT(166) R-3m witness (1/12, 1/6, 11/24) c/a 5/4 basis [[1, 2, 0], [0, 0, 1]] base f=(19, 30, 13) 3^4 4^4 5^2 7^2 8^1 aut 2 ns 3 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 11/24) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 11/24) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 11/24) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 11/24) | 5/4 | 2 | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 4 | DIFFERENT | a1b2ac427f563716 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 1/6, 7/16) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 1/6, 43/96) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 1/6, 15/32) | 5/4 | 2 | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 4 | DIFFERENT | a1b2ac427f563716 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 1/6, 23/48) | 5/4 | 2 | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 4 | DIFFERENT | a1b2ac427f563716 | 148, 155, 166, 167 | True | False |
| metric | - | -1/96 | (1/12, 1/6, 11/24) | 475/384 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 11/24) | 955/768 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 11/24) | 965/768 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 11/24) | 485/384 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 1/6, 89/192) | 5/4 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | SAME | 36c92427e3d084dc | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 11/24) | 5/4 | 1 | (12, 18, 8) | 3^2 4^2 5^3 7^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 11/24) | 5/4 | 1 | (12, 18, 8) | 3^2 4^2 5^3 7^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |

**`bc59e5d778f60d1f`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^3 4^6 5^3 6^2 9^2 10^1 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (23, 36, 15) | 3^2 4^8 6^3 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | DIFFERENT | 5beb94b61eb66eb1 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (23, 36, 15) | 3^2 4^8 6^3 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | SAME | bc59e5d778f60d1f | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 3/4 | 1 | (34, 51, 19) | 3^4 4^7 6^4 8^1 9^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^3 10^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`cbead3df2d2f1d0e`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 1277/2000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(34, 51, 19) 3^2 4^11 6^1 8^3 10^1 12^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1277/2000 | 1 | (40, 60, 22) | 3^8 4^6 5^2 6^1 8^1 9^2 14^1 16^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1277/2000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1277/2000 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1277/2000 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1277/2000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1277/2000 | 1 | (33, 50, 19) | 3^9 4^2 5^2 6^1 8^1 9^2 10^1 13^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1277/2000 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1277/2000 | 1 | (36, 54, 20) | 3^2 4^11 5^2 6^1 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 24263/38400 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 243907/384000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 246461/384000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 123869/192000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1277/2000 | 1 | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 0 | SAME | cbead3df2d2f1d0e | - | True | False |

**`85244add8d1f2d55`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^6 5^6 6^2 12^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 0 | DIFFERENT | e1a38303b2378f17 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 0 | DIFFERENT | 6f4101f83371033d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 0 | SAME | 85244add8d1f2d55 | - | True | False |

**`2165f5c5260120de`** hexagonal IT(152) P3_121 witness (1/8, 1/6, 5/12) c/a 527/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^4 4^3 5^4 6^1 7^2 8^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 527/1000 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 10013/19200 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 100657/192000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 101711/192000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 51119/96000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 527/1000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 527/1000 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | SAME | 2165f5c5260120de | - | True | False |

**`437fbe758a6dd8e3`** hexagonal IT(179) P6_522 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^4 4^6 5^2 6^2 8^1 10^3 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (30, 45, 17) | 4^9 5^2 6^2 8^4 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | SAME | 437fbe758a6dd8e3 | - | True | False |

**`36ec4ad2f530e145`** hexagonal IT(151) P3_112 witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^2 4^6 6^7 8^1 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 3/4 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | SAME | 36ec4ad2f530e145 | - | True | False |

**`fcffad0da2b5b62f`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 15/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^4 4^4 5^2 6^3 7^2 8^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 15/16 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^3 8^1 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 15/16 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 15/16 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 15/16 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 15/16 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^3 8^1 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 15/16 | 1 | (26, 40, 16) | 3^2 4^8 5^2 8^4 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 15/16 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 15/16 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 15/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^3 8^1 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 15/16 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/512 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/1024 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/1024 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/512 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 15/16 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | DIFFERENT | 4a560e459032166a | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 15/16 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 0 | SAME | fcffad0da2b5b62f | - | True | False |

**`505a4911e298c933`** hexagonal IT(181) P6_422 witness (1/8, 1/6, 5/12) c/a 2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^2 4^6 6^6 8^1 10^1 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 2 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 2 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 43e4e46001b4d8b9 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/48 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 43e4e46001b4d8b9 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/96 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/96 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/48 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 2 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 2 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 2 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | DIFFERENT | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 2 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | SAME | 505a4911e298c933 | - | True | False |

**`24a6b511067d37b2`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^2 4^5 5^4 6^3 8^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | 042c19cbfdc869cb | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | 042c19cbfdc869cb | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 5/4 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | SAME | 24a6b511067d37b2 | - | True | False |

**`30f2a1e483babf55`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 11/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^4 4^5 5^2 6^1 7^2 8^1 9^2 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 11/4 | 1 | (26, 39, 15) | 4^4 5^4 6^7 | 2 | 0 | DIFFERENT | 5ff09c7df2d7975b | 178, 179 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 11/4 | 1 | (29, 44, 17) | 3^2 4^9 6^3 8^1 10^2 | 1 | 1 | DIFFERENT | 3b9dfad98f70b4e9 | 178, 179 | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 11/4 | 1 | (29, 44, 17) | 3^2 4^9 6^3 8^1 10^2 | 1 | 1 | DIFFERENT | 3b9dfad98f70b4e9 | 178, 179 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1045/384 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2101/768 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2123/768 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1067/384 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 11/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | SAME | 30f2a1e483babf55 | - | True | False |

**`37aa18e6e10583be`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 9/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 47, 19) 3^6 4^5 5^2 6^3 8^1 10^2 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 9/8 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 9/8 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 9/8 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^4 4^7 5^2 6^4 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^4 4^7 5^2 6^4 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 9/8 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | DIFFERENT | d9bf7fb7a80eaa38 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 285/256 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 573/512 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 579/512 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 291/256 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 9/8 | 1 | (21, 34, 15) | 3^4 4^5 5^2 6^3 8^1 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 9/8 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | DIFFERENT | c3b4b14633c9d4d5 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 9/8 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | SAME | 37aa18e6e10583be | - | True | False |

**`7715c7010e513b71`** hexagonal IT(181) P6_422 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 4^10 6^4 8^2 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (25, 39, 16) | 3^2 4^9 6^3 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | DIFFERENT | af8b2135c913b13b | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1 | 1 | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 0 | SAME | 7715c7010e513b71 | - | True | False |

**`0b5d9beb0fc972f6`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 13/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^5 5^6 6^1 8^3 10^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 13/8 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | DIFFERENT | e19babba732f5fd4 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 13/8 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | DIFFERENT | e19babba732f5fd4 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 13/8 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | DIFFERENT | e19babba732f5fd4 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 13/8 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | DIFFERENT | e19babba732f5fd4 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 13/8 | 1 | (35, 53, 20) | 3^2 4^8 5^4 6^3 8^2 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 13/8 | 1 | (33, 50, 19) | 3^2 4^6 5^6 6^3 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1235/768 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2483/1536 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2509/1536 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1261/768 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 13/8 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | DIFFERENT | e19babba732f5fd4 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 13/8 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | SAME | 0b5d9beb0fc972f6 | - | True | False |

**`322d5ff451e4101d`** hexagonal IT(169) P6_1 witness (1/8, 1/6, 5/12) c/a 11/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^6 5^4 6^2 7^2 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 11/8 | 1 | (36, 54, 20) | 3^6 4^2 5^4 6^4 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 11/8 | 1 | (36, 54, 20) | 3^6 4^2 5^4 6^4 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 11/8 | 1 | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 0 | DIFFERENT | 8d90c524c89922d9 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1045/768 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 2101/1536 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 2123/1536 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1067/768 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 11/8 | 1 | (36, 54, 20) | 3^6 4^2 5^4 6^4 7^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 11/8 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | SAME | 322d5ff451e4101d | - | True | False |

**`34351050a4f29035`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^2 4^5 5^2 6^4 8^3 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (31, 47, 18) | 3^5 4^5 5^3 6^1 8^1 9^2 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 0 | DIFFERENT | 24a6b511067d37b2 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | SAME | 34351050a4f29035 | - | True | False |

**`c0071756347c5a8a`** hexagonal IT(144) P3_1 witness (1/12, 3/8, 1/6) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^2 4^4 5^4 7^6 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1 | 1 | (32, 48, 18) | 3^4 4^4 5^2 6^4 8^2 9^2 | 1 | 0 | DIFFERENT | a99e46dd535bab3b | 144, 145 | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/96 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/192 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/192 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/96 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 1 | 1 | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 0 | SAME | c0071756347c5a8a | - | True | False |

**`d9bf7fb7a80eaa38`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 47, 19) 3^4 4^6 5^4 6^3 10^2 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^2 4^8 5^6 6^1 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^2 4^8 5^6 6^1 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^2 4^8 5^6 6^1 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 4 | DIFFERENT | 2081d7b9a734e4fe | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 5/4 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | DIFFERENT | f43b45fd6383b36b | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 5/4 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | SAME | d9bf7fb7a80eaa38 | - | True | False |

**`847d2695a14ae424`** hexagonal IT(152) P3_121 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^4 4^4 5^4 6^1 8^2 9^2 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | SAME | 847d2695a14ae424 | - | True | False |

**`090dcafb7ce9cb08`** hexagonal IT(166) R-3m witness (1/24, 1/12, 11/24) c/a 1/2 basis [[1, 2, 0], [0, 0, 1]] base f=(20, 32, 14) 3^2 4^9 7^2 8^1 aut 2 ns 4 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/48, 1/24, 11/24) | 1/2 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | -1/96 | (1/32, 1/16, 11/24) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point | (1, 2, 0) | 1/96 | (5/96, 5/48, 11/24) | 1/2 | 2 | (38, 58, 22) | 3^8 4^8 6^3 12^2 18^1 | 2 | 2 | DIFFERENT | 1b1288f460af270d | 166, 167 | True | False |
| point | (1, 2, 0) | 1/48 | (1/16, 1/8, 11/24) | 1/2 | 2 | (38, 58, 22) | 3^8 4^8 6^3 12^2 18^1 | 2 | 2 | DIFFERENT | 1b1288f460af270d | 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/24, 1/12, 7/16) | 1/2 | 2 | (25, 40, 17) | 3^8 4^2 6^6 12^1 | 2 | 5 | DIFFERENT | a66305b551fd919e | 166 | True | False |
| point | (0, 0, 1) | -1/96 | (1/24, 1/12, 43/96) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point | (0, 0, 1) | 1/96 | (1/24, 1/12, 15/32) | 1/2 | 2 | (38, 58, 22) | 3^8 4^8 6^3 12^2 18^1 | 2 | 2 | DIFFERENT | 1b1288f460af270d | 166, 167 | True | False |
| point | (0, 0, 1) | 1/48 | (1/24, 1/12, 23/48) | 1/2 | 2 | (38, 58, 22) | 3^8 4^8 6^3 12^2 18^1 | 2 | 2 | DIFFERENT | 1b1288f460af270d | 166, 167 | True | False |
| metric | - | -1/96 | (1/24, 1/12, 11/24) | 95/192 | 2 | (20, 32, 14) | 3^2 4^9 7^2 8^1 | 2 | 4 | SAME | 090dcafb7ce9cb08 | - | True | False |
| metric | - | -1/192 | (1/24, 1/12, 11/24) | 191/384 | 2 | (20, 32, 14) | 3^2 4^9 7^2 8^1 | 2 | 4 | SAME | 090dcafb7ce9cb08 | - | True | False |
| metric | - | 1/192 | (1/24, 1/12, 11/24) | 193/384 | 2 | (20, 32, 14) | 3^2 4^9 7^2 8^1 | 2 | 4 | SAME | 090dcafb7ce9cb08 | - | True | False |
| metric | - | 1/96 | (1/24, 1/12, 11/24) | 97/192 | 2 | (20, 32, 14) | 3^2 4^9 7^2 8^1 | 2 | 4 | SAME | 090dcafb7ce9cb08 | - | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (7/192, 7/96, 11/24) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (5/128, 5/64, 11/24) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (31/768, 31/384, 11/24) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (21/512, 21/256, 11/24) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (3/64, 3/32, 11/24) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (17/384, 17/192, 11/24) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (11/256, 11/128, 11/24) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (65/1536, 65/768, 11/24) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/24, 1/12, 29/64) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/24, 1/12, 175/384) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/24, 1/12, 117/256) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/24, 1/12, 703/1536) | 1/2 | 2 | (30, 46, 18) | 3^4 4^7 6^4 8^2 12^1 | 2 | 2 | DIFFERENT | 88da140bdfed6c6d | 167 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/24, 1/12, 89/192) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/24, 1/12, 59/128) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/24, 1/12, 353/768) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/24, 1/12, 235/512) | 1/2 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (1/32, 1/12, 11/24) | 1/2 | 1 | (18, 27, 11) | 3^3 4^3 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (5/96, 1/12, 11/24) | 1/2 | 1 | (18, 27, 11) | 3^3 4^3 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`9bc4922a7b574aa6`** hexagonal IT(166) R-3m witness (1/24, 1/12, 11/24) c/a 3/4 basis [[1, 2, 0], [0, 0, 1]] base f=(17, 28, 13) 3^4 4^4 5^4 8^1 aut 2 ns 5 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/48, 1/24, 11/24) | 3/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | -1/96 | (1/32, 1/16, 11/24) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | 1/96 | (5/96, 5/48, 11/24) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (1, 2, 0) | 1/48 | (1/16, 1/8, 11/24) | 3/4 | 2 | (29, 46, 19) | 3^4 4^12 8^2 16^1 | 2 | 5 | DIFFERENT | 9f88c069215c2229 | 166 | True | False |
| point | (0, 0, 1) | -1/48 | (1/24, 1/12, 7/16) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/24, 1/12, 43/96) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/96 | (1/24, 1/12, 15/32) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/24, 1/12, 23/48) | 3/4 | 2 | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 2 | DIFFERENT | ff65c54d78bb4e50 | 148, 155, 166 | True | False |
| metric | - | -1/96 | (1/24, 1/12, 11/24) | 95/128 | 2 | (17, 28, 13) | 3^4 4^4 5^4 8^1 | 2 | 5 | SAME | 9bc4922a7b574aa6 | - | True | False |
| metric | - | -1/192 | (1/24, 1/12, 11/24) | 191/256 | 2 | (17, 28, 13) | 3^4 4^4 5^4 8^1 | 2 | 5 | SAME | 9bc4922a7b574aa6 | - | True | False |
| metric | - | 1/192 | (1/24, 1/12, 11/24) | 193/256 | 2 | (17, 28, 13) | 3^4 4^4 5^4 8^1 | 2 | 5 | SAME | 9bc4922a7b574aa6 | - | True | False |
| metric | - | 1/96 | (1/24, 1/12, 11/24) | 97/128 | 2 | (17, 28, 13) | 3^4 4^4 5^4 8^1 | 2 | 5 | SAME | 9bc4922a7b574aa6 | - | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (7/192, 7/96, 11/24) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (5/128, 5/64, 11/24) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (31/768, 31/384, 11/24) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (21/512, 21/256, 11/24) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (3/64, 3/32, 11/24) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (17/384, 17/192, 11/24) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (11/256, 11/128, 11/24) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (65/1536, 65/768, 11/24) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/24, 1/12, 29/64) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/24, 1/12, 175/384) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/24, 1/12, 117/256) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/24, 1/12, 703/1536) | 3/4 | 2 | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 3 | DIFFERENT | 991a5023fc8d713a | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/24, 1/12, 89/192) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/24, 1/12, 59/128) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/24, 1/12, 353/768) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/24, 1/12, 235/512) | 3/4 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (1/32, 1/12, 11/24) | 3/4 | 1 | (16, 24, 10) | 3^4 5^2 6^2 7^2 | 2 | 0 | DIFFERENT | 3d888d502de4fbd7 | 166 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (5/96, 1/12, 11/24) | 3/4 | 1 | (16, 24, 10) | 3^4 5^2 6^2 7^2 | 2 | 0 | DIFFERENT | 3d888d502de4fbd7 | 166 | True | False |

**`43e4e46001b4d8b9`** hexagonal IT(181) P6_422 witness (1/8, 1/6, 5/12) c/a 31/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^3 5^2 6^2 8^3 10^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 31/16 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | DIFFERENT | 505a4911e298c933 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 31/16 | 1 | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 0 | DIFFERENT | 505a4911e298c933 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 2945/1536 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 5921/3072 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 5983/3072 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 3007/1536 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 31/16 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 31/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 0 | SAME | 43e4e46001b4d8b9 | - | True | False |

**`af8b2135c913b13b`** hexagonal IT(181) P6_422 witness (1/8, 1/6, 5/12) c/a 7/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^4 6^4 8^1 10^3 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 7/8 | 1 | (36, 54, 20) | 3^4 4^10 6^1 8^3 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 665/768 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 1337/1536 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 1351/1536 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 679/768 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 7/8 | 1 | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 0 | DIFFERENT | cc1e165a04008058 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 7/8 | 1 | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 0 | SAME | af8b2135c913b13b | - | True | False |

**`74a69fba4266de3b`** hexagonal IT(167) R-3c witness (1/8, 1/6, 5/12) c/a 527/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 43, 17) 3^10 6^1 8^5 10^1 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 10013/19200 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 100657/192000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 101711/192000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 51119/96000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 527/1000 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 527/1000 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | SAME | 74a69fba4266de3b | - | True | False |

**`c3b4b14633c9d4d5`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 43, 17) 4^9 5^2 6^4 8^2 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 2 | DIFFERENT | 87c94384d7851cb2 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (32, 49, 19) | 3^6 4^3 5^2 6^3 7^2 8^2 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (40, 61, 23) | 3^10 4^3 5^2 6^2 7^2 8^1 10^2 16^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (25, 40, 17) | 3^4 4^5 5^2 6^5 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (22, 36, 16) | 3^4 4^7 5^2 6^1 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 2 | SAME | c3b4b14633c9d4d5 | - | True | False |

**`e19babba732f5fd4`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 7/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 4^11 5^2 7^2 10^2 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 7/4 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 7/4 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 7/4 | 1 | (35, 53, 20) | 3^4 4^9 6^2 7^2 8^1 12^2 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 7/4 | 1 | (33, 50, 19) | 3^2 4^6 5^6 6^3 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 665/384 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 1337/768 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 1351/768 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 679/384 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 7/4 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 7/4 | 1 | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 1 | SAME | e19babba732f5fd4 | - | True | False |

**`7472d8ba000c8056`** hexagonal IT(152) P3_121 witness (0, 1/4, 1/6) c/a 9/8 basis [[0, 1, 0]] base f=(22, 36, 16) 3^8 4^2 6^2 7^4 aut 2 ns 6 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 11/48, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 23/96, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 25/96, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| point | (0, 1, 0) | 1/48 | (0, 13/48, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric | - | -1/96 | (0, 1/4, 1/6) | 285/256 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric | - | -1/192 | (0, 1/4, 1/6) | 573/512 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric | - | 1/192 | (0, 1/4, 1/6) | 579/512 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric | - | 1/96 | (0, 1/4, 1/6) | 291/256 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 47/192, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 95/384, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (0, 191/768, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (0, 383/1536, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (0, 49/192, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (0, 97/384, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (0, 193/768, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (0, 385/1536, 1/6) | 9/8 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric (refine) | - | -1/384 | (0, 1/4, 1/6) | 1149/1024 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric (refine) | - | -1/768 | (0, 1/4, 1/6) | 2301/2048 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric (refine) | - | -1/1536 | (0, 1/4, 1/6) | 4605/4096 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric (refine) | - | -1/3072 | (0, 1/4, 1/6) | 9213/8192 | 2 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| metric (refine) | - | 1/384 | (0, 1/4, 1/6) | 1155/1024 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | 1/768 | (0, 1/4, 1/6) | 2307/2048 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/4, 1/6) | 4611/4096 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/4, 1/6) | 9219/8192 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/4, 1/6) | 9/8 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | DIFFERENT | 2c121297dbaa80af | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/4, 1/6) | 9/8 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | DIFFERENT | 2c121297dbaa80af | - | True | False |

**`d0c5a15c25ab6413`** hexagonal IT(152) P3_121 witness (1/8, 1/6, 5/12) c/a 17/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^7 5^2 6^3 8^2 9^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 17/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | DIFFERENT | 07d543d89e2934f2 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 17/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | DIFFERENT | 07d543d89e2934f2 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 17/16 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 0 | DIFFERENT | 07d543d89e2934f2 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1615/1536 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 3247/3072 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 3281/3072 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1649/1536 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 17/16 | 1 | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 1 | DIFFERENT | 847d2695a14ae424 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 17/16 | 1 | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 0 | SAME | d0c5a15c25ab6413 | - | True | False |

**`d770abfcee4deb90`** hexagonal IT(153) P3_212 witness (1/8, 1/6, 5/12) c/a 19/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^6 4^3 5^2 6^2 8^4 12^1 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^2 6^5 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 19/16 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^2 6^5 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 19/16 | 1 | (29, 44, 17) | 3^5 4^2 5^4 6^3 8^1 9^1 10^1 | 1 | 1 | DIFFERENT | 93f0d1afa520923e | 151, 153 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 19/16 | 1 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^2 6^5 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1805/1536 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 3629/3072 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 3667/3072 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1843/1536 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 19/16 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | DIFFERENT | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 19/16 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | DIFFERENT | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 19/16 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | DIFFERENT | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 19/16 | 1 | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | c47838ebe2b50e1a | 151, 153 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 19/16 | 1 | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 0 | DIFFERENT | 36ec4ad2f530e145 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 19/16 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 0 | SAME | d770abfcee4deb90 | - | True | False |

**`4a560e459032166a`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 7/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^4 5^8 8^4 aut 2 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 7/8 | 1 | (42, 63, 23) | 3^8 4^2 5^8 6^1 9^2 14^1 16^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 7/8 | 1 | (40, 60, 22) | 3^8 4^2 5^6 6^1 8^1 10^2 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 7/8 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 7/8 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 7/8 | 1 | (26, 40, 16) | 3^4 4^5 5^2 6^1 7^2 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 7/8 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 7/8 | 1 | (36, 54, 20) | 3^6 4^4 5^2 6^3 8^1 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 7/8 | 1 | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 665/768 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 1337/1536 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 1351/1536 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 679/768 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 7/8 | 1 | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 0 | DIFFERENT | 7e023be581e7c50a | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 7/8 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 7/8 | 1 | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | d10bb4a25bbf4c80 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 7/8 | 1 | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 0 | SAME | 4a560e459032166a | - | True | False |

**`5beb94b61eb66eb1`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(27, 41, 16) 3^3 4^7 6^2 7^1 8^1 9^2 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | DIFFERENT | bc59e5d778f60d1f | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 1 | DIFFERENT | bc59e5d778f60d1f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 1 | SAME | 5beb94b61eb66eb1 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 1/2 | 1 | (32, 48, 18) | 3^2 4^10 6^1 8^2 9^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 1/2 | 1 | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 0 | DIFFERENT | 437fbe758a6dd8e3 | - | True | False |

**`95934e84555dc2ea`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^2 4^7 5^1 6^3 7^1 8^2 aut 1 ns 2 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (38, 57, 21) | 3^6 4^6 6^4 8^3 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (44, 66, 24) | 3^6 4^8 5^2 6^4 8^2 16^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 2 | SAME | 95934e84555dc2ea | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (34, 51, 19) | 3^4 4^7 6^2 7^2 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (38, 57, 21) | 3^6 4^6 6^4 8^3 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (38, 57, 21) | 3^6 4^6 6^4 8^3 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (38, 57, 21) | 3^6 4^6 6^4 8^3 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (38, 57, 21) | 3^6 4^6 6^4 8^3 12^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`d0ed9179c6947b5f`** hexagonal IT(155) R32 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(16, 26, 12) 3^2 4^6 5^2 6^2 aut 2 ns 3 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (16, 26, 12) | 3^6 4^2 6^2 7^2 | 2 | 4 | DIFFERENT | 4eaa641c282f54ad | 155, 166 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^3 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (28, 44, 18) | 3^8 4^4 6^2 8^2 10^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | SAME | d0ed9179c6947b5f | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^3 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^3 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^3 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^3 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |

**`0948aa6184f13a8a`** hexagonal IT(179) P6_522 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^4 4^4 6^4 7^2 8^3 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 5/4 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 5/4 | 1 | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 0 | SAME | 0948aa6184f13a8a | - | True | False |

**`272aefcd5e48ba49`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 9/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^3 4^3 5^3 6^5 7^2 8^1 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 9/8 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 9/8 | 1 | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 0 | DIFFERENT | 34351050a4f29035 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 5^2 6^4 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 6^7 7^2 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 9/8 | 1 | (38, 57, 21) | 3^2 4^9 5^2 6^3 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 285/256 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 573/512 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 579/512 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 291/256 | 1 | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 1 | SAME | 272aefcd5e48ba49 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 5^2 6^4 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 5^2 6^4 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 5^2 6^4 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 5^2 6^4 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 6^7 7^2 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 6^7 7^2 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 6^7 7^2 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 9/8 | 1 | (34, 51, 19) | 3^4 4^4 6^7 7^2 8^1 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`466b12546dd936c3`** hexagonal IT(161) R3c witness (1/8, 1/6, 5/12) c/a 527/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^6 5^4 6^2 7^2 8^2 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 10013/19200 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 100657/192000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 101711/192000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 51119/96000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 527/1000 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 527/1000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | SAME | 466b12546dd936c3 | - | True | False |

**`4885ce1e70fa9713`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(27, 41, 16) 3^3 4^5 6^4 7^3 8^1 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (36, 54, 20) | 3^4 4^7 6^4 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (40, 60, 22) | 3^2 4^8 5^6 6^4 14^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 1 | SAME | 4885ce1e70fa9713 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 3/4 | 1 | (32, 48, 18) | 3^4 4^6 6^2 7^2 8^3 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 3/4 | 1 | (36, 54, 20) | 3^4 4^7 6^4 7^2 8^1 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 3/4 | 1 | (32, 48, 18) | 3^2 4^8 6^3 7^2 8^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 3/4 | 1 | (32, 48, 18) | 3^2 4^8 6^3 7^2 8^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 3/4 | 1 | (32, 48, 18) | 3^2 4^8 6^3 7^2 8^2 10^1 | 2 | 0 | DIFFERENT | not stored | - | True | False |

**`3d6b109f392fda19`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(33, 50, 19) 3^6 4^4 5^2 6^3 8^2 10^1 12^1 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/2 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/2 | 1 | (30, 46, 18) | 3^4 4^6 5^4 7^2 10^1 12^1 | 1 | 2 | DIFFERENT | 15f476f9f9696b0e | 152, 154 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^2 4^9 5^4 8^2 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/2 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | DIFFERENT | 542cbe76934b484b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/2 | 1 | (19, 30, 13) | 3^4 4^3 5^2 6^3 8^1 | 1 | 3 | DIFFERENT | 06afb32833d8e7b7 | 152, 154 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/2 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | DIFFERENT | 542cbe76934b484b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/2 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | DIFFERENT | 542cbe76934b484b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/2 | 1 | (19, 31, 14) | 3^6 4^4 6^2 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/2 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/64 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/128 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/128 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/64 | 1 | (33, 50, 19) | 3^2 4^9 5^4 8^2 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^2 4^9 5^4 8^2 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/2 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | DIFFERENT | 542cbe76934b484b | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 3/2 | 1 | (28, 44, 18) | 3^6 4^4 5^4 7^2 10^2 | 1 | 4 | DIFFERENT | 7ddf6d7c3a56512f | 152, 154 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 3/2 | 1 | (33, 50, 19) | 3^2 4^9 5^4 8^2 10^1 12^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 3/2 | 1 | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 1 | SAME | 3d6b109f392fda19 | - | True | False |

**`e598ffd8a1cac138`** hexagonal IT(144) P3_1 witness (1/8, 1/6, 5/12) c/a 29/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^4 4^4 5^4 6^2 9^4 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 29/32 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 29/32 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 29/32 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 29/32 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 29/32 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 2755/3072 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 5539/6144 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 5597/6144 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 2813/3072 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 29/32 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 29/32 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | DIFFERENT | a93f8fe7ecdc5851 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 29/32 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 11165/12288 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 0 | SAME | e598ffd8a1cac138 | - | True | False |

**`a93f8fe7ecdc5851`** hexagonal IT(144) P3_1 witness (1/12, 3/8, 1/6) c/a 9/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^8 5^2 7^2 8^2 9^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 0 | DIFFERENT | e98412e7cb95aea2 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 9/8 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 285/256 | 1 | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 0 | DIFFERENT | 6dba530a0828bdcf | 144, 145 | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 573/512 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 579/512 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 291/256 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 9/8 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 0 | DIFFERENT | bff9b24ce78050f5 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 9/8 | 1 | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 0 | SAME | a93f8fe7ecdc5851 | - | True | False |

**`aef8972953d53d20`** hexagonal IT(171) P6_2 witness (1/12, 3/8, 1/6) c/a 81/64 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^4 4^3 5^2 6^6 8^1 9^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 81/64 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 81/64 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 81/64 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 2565/2048 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 5157/4096 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 5211/4096 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 2619/2048 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 81/64 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 81/64 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 81/64 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 81/64 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 10341/8192 | 1 | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 0 | DIFFERENT | 66b85b9283c62463 | 171, 172 | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 20709/16384 | 1 | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 0 | SAME | aef8972953d53d20 | - | True | False |

**`72bcd959be4ab7dd`** hexagonal IT(152) P3_121 witness (1/12, 3/8, 1/6) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^4 4^1 5^4 6^4 8^3 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 5/4 | 1 | (27, 41, 16) | 3^4 4^4 6^5 7^2 10^1 | 1 | 1 | DIFFERENT | 483b95ab4d952a2c | 152, 154 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 5/4 | 1 | (19, 30, 13) | 3^4 4^3 5^2 6^3 8^1 | 1 | 3 | DIFFERENT | 06afb32833d8e7b7 | 152, 154 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 5/4 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 475/384 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 955/768 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 965/768 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 485/384 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 5/4 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 5/4 | 1 | (32, 48, 18) | 3^4 4^5 5^2 7^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 5/4 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | SAME | 72bcd959be4ab7dd | - | True | False |

**`ab801b11bead62ef`** hexagonal IT(166) R-3m witness (1/12, 1/6, 7/24) c/a 7/4 basis [[1, 2, 0], [0, 0, 1]] base f=(19, 30, 13) 3^6 4^2 5^2 6^2 12^1 aut 2 ns 3 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 7/24) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 7/24) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 7/24) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 7/24) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 1/6, 13/48) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 1/6, 9/32) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 1/6, 29/96) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 1/6, 5/16) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| metric | - | -1/96 | (1/12, 1/6, 7/24) | 665/384 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric | - | -1/192 | (1/12, 1/6, 7/24) | 1337/768 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| metric | - | 1/192 | (1/12, 1/6, 7/24) | 1351/768 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 7/24) | 679/384 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (5/64, 5/32, 7/24) | 7/4 | 2 | (12, 21, 11) | 3^6 4^4 8^1 | 2 | 4 | DIFFERENT | f2af171517f10480 | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (31/384, 31/192, 7/24) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 1/6, 55/192) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 1/6, 37/128) | 7/4 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 1/6, 223/768) | 7/4 | 2 | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 3 | SAME | ab801b11bead62ef | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 7/24) | 7/4 | 1 | (12, 18, 8) | 3^3 4^1 5^2 6^1 7^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 7/24) | 7/4 | 1 | (12, 18, 8) | 3^3 4^1 5^2 6^1 7^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`2c121297dbaa80af`** hexagonal IT(154) P3_221 witness (1/12, 3/8, 1/6) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(28, 42, 16) 3^4 4^2 6^8 8^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1 | 1 | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 0 | DIFFERENT | 95ea57030a106887 | 152, 154 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/96 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/192 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/192 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/96 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 1 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | SAME | 2c121297dbaa80af | - | True | False |

**`9d0b36ad5caceb2e`** hexagonal IT(167) R-3c witness (1/12, 3/8, 1/6) c/a 7/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(22, 35, 15) 3^6 4^2 5^4 6^1 8^1 10^1 aut 1 ns 3 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 7/8 | 1 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 3 | DIFFERENT | d0ed9179c6947b5f | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 7/8 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 7/8 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 7/8 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 7/8 | 1 | (28, 43, 17) | 4^10 5^2 6^3 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 7/8 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 7/8 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 665/768 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 1337/1536 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 1351/1536 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 679/768 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 7/8 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 7/8 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 7/8 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | DIFFERENT | 5e68ffe7582a0657 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 7/8 | 1 | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 3 | SAME | 9d0b36ad5caceb2e | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 7/8 | 1 | (28, 43, 17) | 4^10 5^2 6^3 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 7/8 | 1 | (28, 43, 17) | 4^10 5^2 6^3 8^1 10^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 7/8 | 1 | (26, 41, 17) | 3^4 4^5 5^2 6^4 8^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 7/8 | 1 | (30, 47, 19) | 3^8 4^4 6^2 7^2 8^1 10^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 7/8 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 7/8 | 1 | (26, 41, 17) | 3^6 4^4 6^5 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 7/8 | 1 | (26, 41, 17) | 3^6 4^4 6^5 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 7/8 | 1 | (26, 41, 17) | 3^6 4^4 6^5 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |

**`d176b8d859dd651a`** hexagonal IT(178) P6_122 witness (1/12, 3/8, 1/6) c/a 5/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(32, 48, 18) 3^2 4^8 5^2 6^1 8^3 9^2 aut 1 ns 0 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 5/2 | 1 | (34, 51, 19) | 3^2 4^11 6^2 10^4 | 2 | 0 | DIFFERENT | 364e84ece2d20d22 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 5/2 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | DIFFERENT | 30f2a1e483babf55 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 5/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^1 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 5/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^1 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 5/2 | 1 | (27, 42, 17) | 3^4 4^7 6^2 7^2 9^2 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 5/2 | 1 | (32, 48, 18) | 3^4 4^4 5^4 6^1 7^2 8^1 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 475/192 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 955/384 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 965/384 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 485/192 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 5/2 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 1 | DIFFERENT | 30f2a1e483babf55 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 5/2 | 1 | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 0 | SAME | d176b8d859dd651a | - | True | False |

**`60eb4282db04fca2`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 11/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(30, 45, 17) 3^2 4^6 5^2 6^3 8^4 aut 1 ns 0 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 11/8 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 11/8 | 1 | (40, 60, 22) | 3^4 4^6 5^2 6^7 8^1 10^1 14^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1045/768 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 2101/1536 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 2123/1536 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1067/768 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 11/8 | 1 | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 1 | DIFFERENT | f5fbebffa76808d5 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 11/8 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 11/8 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 11/8 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 11/8 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 11/8 | 1 | (36, 54, 20) | 3^4 4^3 5^4 6^5 7^2 8^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 4213/3072 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | SAME | 60eb4282db04fca2 | - | True | False |

**`f43b45fd6383b36b`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 19/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 41, 17) 3^4 4^5 5^4 6^1 8^3 aut 1 ns 4 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^4 4^7 5^2 6^4 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^4 4^7 5^2 6^4 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^2 4^8 5^6 6^1 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^2 4^8 5^6 6^1 8^1 12^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 19/16 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | DIFFERENT | d9bf7fb7a80eaa38 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 19/16 | 1 | (22, 36, 16) | 3^4 4^8 6^2 8^2 | 1 | 6 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1805/1536 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 3629/3072 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 3667/3072 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1843/1536 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 19/16 | 1 | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 4 | DIFFERENT | 37aa18e6e10583be | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 19/16 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 7277/6144 | 1 | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 4 | SAME | f43b45fd6383b36b | - | True | False |

**`4ff9d77aa9f8194a`** hexagonal IT(167) R-3c witness (1/8, 1/6, 5/12) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(24, 37, 15) 3^2 4^7 6^4 8^2 aut 1 ns 2 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/4 | 1 | (26, 40, 16) | 3^4 4^6 6^3 8^2 10^1 | 2 | 2 | DIFFERENT | ddbf7770e983e608 | 155, 166, 167 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/4 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/128 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/256 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/256 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/128 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 3/4 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 383/512 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric (refine) | - | -1/768 | (1/8, 1/6, 5/12) | 767/1024 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| metric (refine) | - | -1/1536 | (1/8, 1/6, 5/12) | 1535/2048 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | SAME | 4ff9d77aa9f8194a | - | True | False |

**`6de3dac5f334cfed`** hexagonal IT(167) R-3c witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^4 4^6 6^2 8^4 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1/2 | 1 | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 2 | DIFFERENT | 74a69fba4266de3b | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | SAME | 6de3dac5f334cfed | - | True | False |

**`105e41c2798e6180`** hexagonal IT(148) R-3 witness (0, 0, 5/24) c/a 2 basis [[0, 0, 1]] base f=(16, 27, 13) 3^6 4^3 6^4 aut 6 ns 4 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 0, 1) | -1/48 | (0, 0, 3/16) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point | (0, 0, 1) | -1/96 | (0, 0, 19/96) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point | (0, 0, 1) | 1/96 | (0, 0, 7/32) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | 1/48 | (0, 0, 11/48) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | -1/96 | (0, 0, 5/24) | 95/48 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | -1/192 | (0, 0, 5/24) | 191/96 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | 1/192 | (0, 0, 5/24) | 193/96 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| metric | - | 1/96 | (0, 0, 5/24) | 97/48 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (0, 0, 13/64) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (0, 0, 79/384) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (0, 0, 53/256) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (0, 0, 319/1536) | 2 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (0, 0, 41/192) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (0, 0, 27/128) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (0, 0, 161/768) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (0, 0, 107/512) | 2 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/384 | (0, 0, 5/24) | 383/192 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/768 | (0, 0, 5/24) | 767/384 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/1536 | (0, 0, 5/24) | 1535/768 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/3072 | (0, 0, 5/24) | 3071/1536 | 3 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | 1/384 | (0, 0, 5/24) | 385/192 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| metric (refine) | - | 1/768 | (0, 0, 5/24) | 769/384 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| metric (refine) | - | 1/1536 | (0, 0, 5/24) | 1537/768 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| metric (refine) | - | 1/3072 | (0, 0, 5/24) | 3073/1536 | 3 | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 3 | DIFFERENT | f593cb348adf804b | 148, 155, 166 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 0, 5/24) | 2 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 0, 5/24) | 2 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |

**`542cbe76934b484b`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 5/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^6 4^2 5^2 6^3 8^3 10^1 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 5/4 | 1 | (33, 50, 19) | 3^6 4^4 6^5 7^2 8^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 5/4 | 1 | (19, 30, 13) | 3^4 4^3 5^2 6^3 8^1 | 1 | 3 | DIFFERENT | 06afb32833d8e7b7 | 152, 154 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 5/4 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 5/4 | 1 | (33, 50, 19) | 3^6 4^4 6^5 7^2 8^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 475/384 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 955/768 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 965/768 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 485/384 | 1 | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 1 | SAME | 542cbe76934b484b | - | True | False |

**`75bbbcb4a37e70e8`** hexagonal IT(146) R3 witness (1/8, 1/6, 5/12) c/a 67/80 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(27, 41, 16) 3^2 4^4 5^4 6^2 7^4 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^4 4^2 5^4 6^2 7^2 8^2 | 1 | 1 | DIFFERENT | cc73376b3d575c00 | 146 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^4 4^2 5^4 6^2 7^2 8^2 | 1 | 1 | DIFFERENT | cc73376b3d575c00 | 146 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 67/80 | 1 | (23, 35, 14) | 3^2 4^2 5^4 6^6 | 1 | 1 | DIFFERENT | f73b315d6a9ed826 | 146 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 67/80 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1273/1536 | 1 | (23, 35, 14) | 3^2 4^2 5^4 6^6 | 1 | 1 | DIFFERENT | f73b315d6a9ed826 | 146 | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 12797/15360 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 12931/15360 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 6499/7680 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 67/80 | 1 | (23, 35, 14) | 3^2 4^2 5^4 6^6 | 1 | 1 | DIFFERENT | f73b315d6a9ed826 | 146 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 67/80 | 1 | (23, 35, 14) | 3^2 4^2 5^4 6^6 | 1 | 1 | DIFFERENT | f73b315d6a9ed826 | 146 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 67/80 | 1 | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 1 | SAME | 75bbbcb4a37e70e8 | - | True | False |

**`cff2d5fb5e0d4149`** hexagonal IT(171) P6_2 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(23, 35, 14) 4^5 5^6 6^1 7^2 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | SAME | cff2d5fb5e0d4149 | - | True | False |

**`4b6055c7aa3d341b`** hexagonal IT(178) P6_122 witness (1/8, 1/6, 5/12) c/a 17/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(25, 38, 15) 3^2 4^4 5^5 6^1 7^2 9^1 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 17/8 | 1 | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 0 | DIFFERENT | 2a139a0af47705e5 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 17/8 | 1 | (22, 34, 14) | 3^4 4^4 6^5 10^1 | 2 | 2 | DIFFERENT | 8e6a80eb6f0f31a9 | 151, 153, 180, 181 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 17/8 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 17/8 | 1 | (26, 39, 15) | 4^4 5^4 6^7 | 2 | 0 | DIFFERENT | 5ff09c7df2d7975b | 178, 179 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1615/768 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 3247/1536 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 3281/1536 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1649/768 | 1 | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 1 | SAME | 4b6055c7aa3d341b | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 17/8 | 1 | (32, 48, 18) | 3^6 4^3 5^2 6^1 7^2 8^3 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 17/8 | 1 | (30, 45, 17) | 3^2 4^5 5^2 6^5 7^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 17/8 | 1 | (30, 45, 17) | 3^2 4^5 5^2 6^5 7^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 17/8 | 1 | (30, 45, 17) | 3^2 4^5 5^2 6^5 7^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 17/8 | 1 | (30, 45, 17) | 3^4 4^4 6^6 8^2 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`7e79f1c38b5516bf`** hexagonal IT(178) P6_122 witness (0, 1/4, 1/3) c/a 3/2 basis [[0, 1, 0]] base f=(22, 34, 14) 3^4 4^2 5^4 6^2 8^2 aut 2 ns 2 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 11/48, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 23/96, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 25/96, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | 1/48 | (0, 13/48, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | -1/96 | (0, 1/4, 1/3) | 95/64 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric | - | -1/192 | (0, 1/4, 1/3) | 191/128 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric | - | 1/192 | (0, 1/4, 1/3) | 193/128 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | 1/96 | (0, 1/4, 1/3) | 97/64 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 47/192, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 95/384, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (0, 191/768, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (0, 383/1536, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (0, 49/192, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (0, 97/384, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (0, 193/768, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (0, 385/1536, 1/3) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/384 | (0, 1/4, 1/3) | 383/256 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | -1/768 | (0, 1/4, 1/3) | 767/512 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | -1/1536 | (0, 1/4, 1/3) | 1535/1024 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | -1/3072 | (0, 1/4, 1/3) | 3071/2048 | 2 | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 0 | DIFFERENT | a35623e347ef03b4 | - | True | False |
| metric (refine) | - | 1/384 | (0, 1/4, 1/3) | 385/256 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/768 | (0, 1/4, 1/3) | 769/512 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/4, 1/3) | 1537/1024 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/4, 1/3) | 3073/2048 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/4, 1/3) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/4, 1/3) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |

**`d7c638d7fa23127e`** hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(25, 39, 16) 3^4 4^4 5^4 7^2 8^2 aut 1 ns 3 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/2 | 1 | (25, 39, 16) | 3^4 4^4 5^4 7^2 8^2 | 1 | 3 | SAME | d7c638d7fa23127e | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/2 | 1 | (25, 39, 16) | 3^4 4^4 5^4 7^2 8^2 | 1 | 3 | SAME | d7c638d7fa23127e | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/2 | 1 | (25, 39, 16) | 3^4 4^4 5^4 7^2 8^2 | 1 | 3 | SAME | d7c638d7fa23127e | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/2 | 1 | (25, 39, 16) | 3^4 4^4 5^4 7^2 8^2 | 1 | 3 | SAME | d7c638d7fa23127e | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/64 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/128 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/128 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/64 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/12, 575/1536, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 3/2 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 383/256 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 767/512 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric (refine) | - | -1/1536 | (1/12, 3/8, 1/6) | 1535/1024 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric (refine) | - | -1/3072 | (1/12, 3/8, 1/6) | 3071/2048 | 1 | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 0 | DIFFERENT | 322d5ff451e4101d | - | True | False |
| metric (refine) | - | 1/384 | (1/12, 3/8, 1/6) | 385/256 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/768 | (1/12, 3/8, 1/6) | 769/512 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/1536 | (1/12, 3/8, 1/6) | 1537/1024 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/3072 | (1/12, 3/8, 1/6) | 3073/2048 | 1 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |

**`0417061f8f56488e`** hexagonal IT(152) P3_121 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(20, 32, 14) 3^4 4^5 6^4 8^1 aut 1 ns 4 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (29, 44, 17) | 3^7 4^2 5^2 6^2 8^2 10^1 11^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | SAME | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |

**`6cc34ed38aa354e1`** hexagonal IT(181) P6_422 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(22, 34, 14) 3^2 4^4 5^4 6^3 8^1 aut 1 ns 2 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 2 | SAME | 6cc34ed38aa354e1 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^6 10^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (28, 42, 16) | 4^7 5^2 6^5 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`5838282f46223111`** hexagonal IT(152) P3_121 witness (1/8, 1/6, 5/12) c/a 7/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(29, 44, 17) 3^2 4^9 6^2 8^3 10^1 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 7/4 | 1 | (26, 40, 16) | 3^6 4^2 5^2 6^2 7^2 8^1 10^1 | 1 | 2 | DIFFERENT | 8cdfcf810038e858 | 152, 154 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 7/4 | 1 | (26, 40, 16) | 3^6 4^2 5^2 6^2 7^2 8^1 10^1 | 1 | 2 | DIFFERENT | 8cdfcf810038e858 | 152, 154 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 7/4 | 1 | (26, 40, 16) | 3^6 4^2 5^2 6^2 7^2 8^1 10^1 | 1 | 2 | DIFFERENT | 8cdfcf810038e858 | 152, 154 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 7/4 | 1 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 665/384 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 1337/768 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 1351/768 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 679/384 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^2 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 7/4 | 1 | (26, 40, 16) | 3^6 4^2 5^2 6^2 7^2 8^1 10^1 | 1 | 2 | DIFFERENT | 8cdfcf810038e858 | 152, 154 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 7/4 | 1 | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 1 | SAME | 5838282f46223111 | - | True | False |

**`cda1d1c03659b67d`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 527/1000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(22, 34, 14) 4^6 5^4 6^4 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 527/1000 | 1 | (26, 40, 16) | 4^7 5^6 7^2 8^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 527/1000 | 1 | (26, 40, 16) | 4^7 5^6 7^2 8^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 527/1000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 527/1000 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | DIFFERENT | c18a9b1cb2a5d168 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 10013/19200 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 100657/192000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 101711/192000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 51119/96000 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | SAME | cda1d1c03659b67d | - | True | False |

**`161b09808f4c1863`** hexagonal IT(178) P6_122 witness (0, 1/3, 1/3) c/a 2 basis [[0, 1, 0]] base f=(18, 30, 14) 3^4 4^6 6^4 aut 4 ns 6 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 5/16, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 31/96, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 11/32, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | 1/48 | (0, 17/48, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | -1/96 | (0, 1/3, 1/3) | 95/48 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | -1/192 | (0, 1/3, 1/3) | 191/96 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | 1/192 | (0, 1/3, 1/3) | 193/96 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric | - | 1/96 | (0, 1/3, 1/3) | 97/48 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 21/64, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 127/384, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (0, 85/256, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (0, 511/1536, 1/3) | 2 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (0, 65/192, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (0, 43/128, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (0, 257/768, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (0, 171/512, 1/3) | 2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/384 | (0, 1/3, 1/3) | 383/192 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/768 | (0, 1/3, 1/3) | 767/384 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/1536 | (0, 1/3, 1/3) | 1535/768 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/3072 | (0, 1/3, 1/3) | 3071/1536 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/384 | (0, 1/3, 1/3) | 385/192 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | 1/768 | (0, 1/3, 1/3) | 769/384 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/3, 1/3) | 1537/768 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/3, 1/3) | 3073/1536 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | 76, 78, 109, 151, 153 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/3, 1/3) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/3, 1/3) | 2 | 1 | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 1 | DIFFERENT | dd3fb07fe11d73d3 | - | True | False |

**`c92eef8763d02d8a`** hexagonal IT(179) P6_522 witness (1/12, 3/8, 1/6) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(25, 39, 16) 3^2 4^8 5^2 7^2 8^2 aut 1 ns 3 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/2 | 1 | (29, 45, 18) | 3^2 4^7 5^4 6^1 7^2 8^2 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/2 | 1 | (38, 57, 21) | 3^4 4^2 5^8 6^2 7^2 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/2 | 1 | (37, 56, 21) | 3^2 4^10 5^2 6^4 8^1 10^1 14^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/64 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/128 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/128 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/64 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/12, 575/1536, 1/6) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 3/2 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 3/2 | 1 | (38, 57, 21) | 3^4 4^2 5^8 6^2 7^2 8^2 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 3/2 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 383/256 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 767/512 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric (refine) | - | -1/1536 | (1/12, 3/8, 1/6) | 1535/1024 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric (refine) | - | -1/3072 | (1/12, 3/8, 1/6) | 3071/2048 | 1 | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 0 | DIFFERENT | 60eb4282db04fca2 | - | True | False |
| metric (refine) | - | 1/384 | (1/12, 3/8, 1/6) | 385/256 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| metric (refine) | - | 1/768 | (1/12, 3/8, 1/6) | 769/512 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| metric (refine) | - | 1/1536 | (1/12, 3/8, 1/6) | 1537/1024 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |
| metric (refine) | - | 1/3072 | (1/12, 3/8, 1/6) | 3073/2048 | 1 | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 0 | DIFFERENT | 0b5d9beb0fc972f6 | - | True | False |

**`3a491fd6426d90b2`** hexagonal IT(146) R3 witness (1/8, 1/6, 5/12) c/a 33/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(24, 38, 16) 3^4 4^4 5^2 6^4 7^2 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 33/32 | 1 | (22, 36, 16) | 3^6 4^4 5^2 6^2 8^2 | 2 | 6 | DIFFERENT | 01a494d767bd713c | 146 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 33/32 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | DIFFERENT | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 33/32 | 1 | (22, 36, 16) | 3^6 4^4 5^2 6^2 8^2 | 2 | 6 | DIFFERENT | 01a494d767bd713c | 146 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1045/1024 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 2101/2048 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 2123/2048 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1067/1024 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 33/32 | 1 | (20, 32, 14) | 4^10 6^4 | 2 | 4 | DIFFERENT | 7fc05363d689d31c | 146 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 33/32 | 1 | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 4 | SAME | 3a491fd6426d90b2 | - | True | False |

**`5b679d8b0a3147c3`** hexagonal IT(152) P3_121 witness (1/12, 3/8, 1/6) c/a 17/16 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(24, 38, 16) 3^6 4^5 7^2 8^3 aut 1 ns 4 — POINT WALL / METRIC ONE-SIDED / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 17/16 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | SAME | 5b679d8b0a3147c3 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 17/16 | 1 | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 0 | DIFFERENT | 2c121297dbaa80af | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 17/16 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | SAME | 5b679d8b0a3147c3 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 17/16 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | SAME | 5b679d8b0a3147c3 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 17/16 | 1 | (29, 44, 17) | 3^1 4^11 6^1 8^2 9^1 10^1 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 17/16 | 1 | (34, 51, 19) | 3^2 4^10 6^3 8^2 10^1 12^1 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 17/16 | 1 | (30, 45, 17) | 3^6 4^1 6^6 8^4 | 2 | 0 | DIFFERENT | 56b1d49a0766cc47 | 181 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 17/16 | 1 | (30, 45, 17) | 3^6 4^1 6^6 8^4 | 2 | 0 | DIFFERENT | 56b1d49a0766cc47 | 181 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1615/1536 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 3247/3072 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 3281/3072 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | SAME | 5b679d8b0a3147c3 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1649/1536 | 1 | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 4 | SAME | 5b679d8b0a3147c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 17/16 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 17/16 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 17/16 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 17/16 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 17/16 | 1 | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 0 | DIFFERENT | b2430fc4bea4e06d | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 17/16 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 17/16 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 17/16 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | 2165f5c5260120de | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 17/16 | 1 | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 0 | DIFFERENT | 2165f5c5260120de | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 6511/6144 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 13039/12288 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| metric (refine) | - | -1/1536 | (1/12, 3/8, 1/6) | 26095/24576 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |
| metric (refine) | - | -1/3072 | (1/12, 3/8, 1/6) | 52207/49152 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |

**`fac4317d5a65b959`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 9/8 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(24, 38, 16) 3^6 4^2 5^2 6^2 7^4 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 9/8 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | DIFFERENT | 5f812747976b224a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^1 7^4 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^1 7^4 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 9/8 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 285/256 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 573/512 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 579/512 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 291/256 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 9/8 | 1 | (15, 25, 12) | 3^2 4^7 5^2 6^1 | 1 | 3 | DIFFERENT | 989e182598ebe414 | 148 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 9/8 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 9/8 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | SAME | fac4317d5a65b959 | - | True | False |

**`27d463eac6cda5ea`** hexagonal IT(171) P6_2 witness (1/12, 3/8, 1/6) c/a 5331/8000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(27, 41, 16) 3^2 4^7 6^4 8^3 aut 1 ns 1 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 5331/8000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 5331/8000 | 1 | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 0 | DIFFERENT | 59f890334e777569 | 181 | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 5331/8000 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 0 | DIFFERENT | 2b9726574a0a8bed | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 33763/51200 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 339407/512000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 342961/512000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 172369/256000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 5331/8000 | 1 | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 1 | DIFFERENT | cff2d5fb5e0d4149 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 5331/8000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 680591/1024000 | 1 | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 1 | SAME | 27d463eac6cda5ea | - | True | False |

**`919d30fd9021b5ee`** hexagonal IT(154) P3_221 witness (1/12, 3/8, 1/6) c/a 51/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(25, 38, 15) 3^3 4^3 5^2 6^4 7^3 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 51/32 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 51/32 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 51/32 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 51/32 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 51/32 | 1 | (22, 34, 14) | 3^4 4^4 5^2 6^1 8^3 | 1 | 2 | DIFFERENT | 08fd2cc91bbad73c | 152, 154 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 51/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^4 10^3 | 1 | 0 | DIFFERENT | 44201ed9cae489c1 | 152 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 51/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^4 10^3 | 1 | 0 | DIFFERENT | 44201ed9cae489c1 | 152 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 1615/1024 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 3247/2048 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 3281/2048 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 1649/1024 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 51/32 | 1 | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 1 | SAME | 919d30fd9021b5ee | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 51/32 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 51/32 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 51/32 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 51/32 | 1 | (30, 45, 17) | 3^4 4^4 5^2 6^2 8^5 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 51/32 | 1 | (30, 45, 17) | 3^2 4^6 6^6 8^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 51/32 | 1 | (30, 45, 17) | 3^2 4^6 6^6 8^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 51/32 | 1 | (30, 45, 17) | 3^2 4^6 6^6 8^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 51/32 | 1 | (30, 45, 17) | 3^2 4^6 6^6 8^3 | 1 | 0 | DIFFERENT | not stored | - | True | False |

**`6074c5fa5d2dffc5`** hexagonal IT(148) R-3 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(16, 26, 12) 3^2 4^5 5^4 6^1 aut 1 ns 3 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | DIFFERENT | 5f812747976b224a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | SAME | 6074c5fa5d2dffc5 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 3/4 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 3/4 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 3/4 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 3/4 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 3/4 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 4 | DIFFERENT | f7c3e10af5321d77 | 163 | True | False |

**`5e68ffe7582a0657`** hexagonal IT(167) R-3c witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(20, 31, 13) 3^4 4^3 6^5 8^1 aut 1 ns 2 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 2 | SAME | 5e68ffe7582a0657 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (26, 40, 16) | 3^4 4^5 6^4 8^3 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 2 | DIFFERENT | 6de3dac5f334cfed | - | True | False |

**`1ba26ab2c0999b93`** hexagonal IT(148) R-3 witness (1/12, 3/8, 1/6) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(20, 32, 14) 3^4 4^3 5^2 6^5 aut 1 ns 3 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1/2 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1/2 | 1 | (19, 29, 12) | 3^2 4^4 6^6 | 1 | 1 | DIFFERENT | d40ab48fae3b8762 | 148 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1/2 | 1 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | DIFFERENT | 057255f61286b052 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1/2 | 1 | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 4 | DIFFERENT | 057255f61286b052 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/192 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/384 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/384 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/192 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | SAME | 1ba26ab2c0999b93 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^2 7^2 8^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^2 7^2 8^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^2 7^2 8^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1/2 | 1 | (28, 44, 18) | 3^6 4^5 6^2 7^2 8^3 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1/2 | 1 | (24, 38, 16) | 3^4 4^5 6^6 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |

**`27dbb77012555d28`** hexagonal IT(161) R3c witness (1/12, 3/8, 1/6) c/a 4439/8000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^4 4^2 5^6 6^2 9^2 aut 1 ns 2 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 4439/8000 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 84341/153600 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 847849/1536000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 856727/1536000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 430583/768000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | DIFFERENT | b27ba8dbcbc2891a | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/12, 575/1536, 1/6) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 4439/8000 | 1 | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 2 | DIFFERENT | 56918d2cff883e22 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 4439/8000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 1700137/3072000 | 1 | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 2 | SAME | 27dbb77012555d28 | - | True | False |

**`c18a9b1cb2a5d168`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(26, 40, 16) 3^6 4^1 5^2 6^1 7^6 aut 1 ns 2 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 4^7 5^6 7^2 8^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^4 4^3 5^2 6^4 7^2 8^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (23, 36, 15) | 3^6 5^2 6^5 7^2 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 1/2 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 385/768 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| metric (refine) | - | 1/768 | (1/8, 1/6, 5/12) | 769/1536 | 1 | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 2 | DIFFERENT | cda1d1c03659b67d | - | True | False |
| metric (refine) | - | 1/1536 | (1/8, 1/6, 5/12) | 1537/3072 | 1 | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 2 | SAME | c18a9b1cb2a5d168 | - | True | False |

**`d1f1121757598de0`** hexagonal IT(154) P3_221 witness (1/8, 1/6, 5/12) c/a 9/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(15, 25, 12) 3^2 4^8 6^2 aut 2 ns 5 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 285/128 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 573/256 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 579/256 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 291/128 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 9/4 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 9/4 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 1149/512 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric (refine) | - | -1/768 | (1/8, 1/6, 5/12) | 2301/1024 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric (refine) | - | -1/1536 | (1/8, 1/6, 5/12) | 4605/2048 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric (refine) | - | -1/3072 | (1/8, 1/6, 5/12) | 9213/4096 | 1 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | f905851c28b76464 | 169, 170 | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 1155/512 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric (refine) | - | 1/768 | (1/8, 1/6, 5/12) | 2307/1024 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric (refine) | - | 1/1536 | (1/8, 1/6, 5/12) | 4611/2048 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |
| metric (refine) | - | 1/3072 | (1/8, 1/6, 5/12) | 9219/4096 | 1 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 29148698f93136e6 | 169, 170, 178, 179 | True | False |

**`b27ba8dbcbc2891a`** hexagonal IT(161) R3c witness (1/8, 1/6, 5/12) c/a 1/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(22, 34, 14) 4^8 6^6 aut 1 ns 2 — POINT ONE-SIDED / METRIC OPEN / COMBINED **ONE-SIDED**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1/2 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1/2 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1/2 | 1 | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 2 | DIFFERENT | bbf85b4df505dab4 | 161 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/192 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/384 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/384 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/192 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 1/2 | 1 | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 2 | DIFFERENT | 466b12546dd936c3 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 1/2 | 1 | (22, 34, 14) | 4^8 6^6 | 1 | 2 | SAME | b27ba8dbcbc2891a | - | True | False |

**`457c20cf036ae496`** hexagonal IT(180) P6_222 witness (0, 1/2, 0) c/a 3/2 basis [[0, 0, 1]] base f=(11, 20, 11) 3^6 4^3 5^2 aut 2 ns 7 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 0, 1) | -1/48 | (0, 1/2, -1/48) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 0, 1) | -1/96 | (0, 1/2, -1/96) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 0, 1) | 1/96 | (0, 1/2, 1/96) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| point | (0, 0, 1) | 1/48 | (0, 1/2, 1/48) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| metric | - | -1/96 | (0, 1/2, 0) | 95/64 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric | - | -1/192 | (0, 1/2, 0) | 191/128 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric | - | 1/192 | (0, 1/2, 0) | 193/128 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| metric | - | 1/96 | (0, 1/2, 0) | 97/64 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (0, 1/2, -1/192) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (0, 1/2, -1/384) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (0, 1/2, -1/768) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (0, 1/2, -1/1536) | 3/2 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (0, 1/2, 1/192) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (0, 1/2, 1/384) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (0, 1/2, 1/768) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (0, 1/2, 1/1536) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | df40917011e94d04 | 151, 153 | True | False |
| metric (refine) | - | -1/384 | (0, 1/2, 0) | 383/256 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | -1/768 | (0, 1/2, 0) | 767/512 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | -1/1536 | (0, 1/2, 0) | 1535/1024 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | -1/3072 | (0, 1/2, 0) | 3071/2048 | 2 | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 4 | DIFFERENT | 0cea04a8f66814e0 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | 1/384 | (0, 1/2, 0) | 385/256 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | 1/768 | (0, 1/2, 0) | 769/512 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/2, 0) | 1537/1024 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/2, 0) | 3073/2048 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 5 | DIFFERENT | f1e0d6a24a06b752 | 151, 152, 153, 154, 178, 179 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/2, 0) | 3/2 | 1 | (19, 31, 14) | 3^4 4^8 8^1 10^1 | 1 | 5 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/2, 0) | 3/2 | 1 | (19, 31, 14) | 3^4 4^8 8^1 10^1 | 1 | 5 | DIFFERENT | not stored | - | True | False |

**`11a9fe078850b5cd`** hexagonal IT(179) P6_522 witness (1/8, 1/6, 5/12) c/a 65/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(25, 38, 15) 3^2 4^3 5^4 6^4 7^2 aut 1 ns 1 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 65/32 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^4 5^4 6^1 7^4 | 1 | 1 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 65/32 | 1 | (22, 34, 14) | 3^4 4^3 5^2 6^3 8^2 | 1 | 2 | DIFFERENT | b3981da714598974 | 178, 179 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 65/32 | 1 | (22, 34, 14) | 3^4 4^3 5^2 6^3 8^2 | 1 | 2 | DIFFERENT | b3981da714598974 | 178, 179 | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 65/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 65/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 65/32 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 65/32 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 6175/3072 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 12415/6144 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 12545/6144 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 6305/3072 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 65/32 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | SAME | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 65/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 65/32 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 65/32 | 1 | (30, 45, 17) | 3^2 4^5 6^8 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 65/32 | 1 | (30, 45, 17) | 3^2 4^5 6^8 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 65/32 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 65/32 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 65/32 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^4 8^4 | 1 | 0 | DIFFERENT | e77398f50b295584 | 179 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 65/32 | 1 | (30, 45, 17) | 3^4 4^3 5^2 6^4 8^4 | 1 | 0 | DIFFERENT | e77398f50b295584 | 179 | True | False |

**`5f812747976b224a`** hexagonal IT(148) R-3 witness (1/8, 1/6, 5/12) c/a 39/32 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(20, 32, 14) 3^2 4^6 5^4 7^2 aut 1 ns 4 — POINT OPEN / METRIC OPEN / COMBINED **OPEN**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 39/32 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^1 7^4 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 39/32 | 1 | (24, 38, 16) | 3^4 4^5 5^2 6^1 7^4 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^4 5^6 6^2 | 2 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^4 5^6 6^2 | 2 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 39/32 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 39/32 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 39/32 | 1 | (18, 30, 14) | 3^8 6^6 | 12 | 6 | DIFFERENT | 76108b085b4e40f8 | 147, 148, 149, 150, 158, 161, 162, 163, 164, 165, 167, 169, 170, 173, 176, 182, 185, 186, 188, 193, 194 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 1235/1024 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 2483/2048 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 2509/2048 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 1261/1024 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 39/32 | 1 | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 4 | DIFFERENT | fac4317d5a65b959 | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 4 | DIFFERENT | af480ebac6f37935 | 148 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 39/32 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 5005/4096 | 1 | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 4 | SAME | 5f812747976b224a | - | True | False |

**`c95a5fcf4d681568`** hexagonal IT(166) R-3m witness (1/24, 1/12, 1/6) c/a 3/2 basis [[1, 2, 0], [0, 0, 1]] base f=(12, 21, 11) 3^4 4^5 5^2 aut 2 ns 4 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/48, 1/24, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | -1/96 | (1/32, 1/16, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (1, 2, 0) | 1/96 | (5/96, 5/48, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | 1/48 | (1/16, 1/8, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/24, 1/12, 7/48) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/24, 1/12, 5/32) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/96 | (1/24, 1/12, 17/96) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/24, 1/12, 3/16) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric | - | -1/96 | (1/24, 1/12, 1/6) | 95/64 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric | - | -1/192 | (1/24, 1/12, 1/6) | 191/128 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric | - | 1/192 | (1/24, 1/12, 1/6) | 193/128 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| metric | - | 1/96 | (1/24, 1/12, 1/6) | 97/64 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (7/192, 7/96, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (5/128, 5/64, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (31/768, 31/384, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (21/512, 21/256, 1/6) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (3/64, 3/32, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (17/384, 17/192, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (11/256, 11/128, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (65/1536, 65/768, 1/6) | 3/2 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/24, 1/12, 31/192) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/24, 1/12, 21/128) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/24, 1/12, 127/768) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/24, 1/12, 85/512) | 3/2 | 2 | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 5 | DIFFERENT | 346c81a0f2121bf1 | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/24, 1/12, 11/64) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/24, 1/12, 65/384) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/24, 1/12, 43/256) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/24, 1/12, 257/1536) | 3/2 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric (refine) | - | -1/384 | (1/24, 1/12, 1/6) | 383/256 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric (refine) | - | -1/768 | (1/24, 1/12, 1/6) | 767/512 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric (refine) | - | -1/1536 | (1/24, 1/12, 1/6) | 1535/1024 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric (refine) | - | -1/3072 | (1/24, 1/12, 1/6) | 3071/2048 | 2 | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 3 | DIFFERENT | 9d4396ca0b08fc3c | - | True | False |
| metric (refine) | - | 1/384 | (1/24, 1/12, 1/6) | 385/256 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/768 | (1/24, 1/12, 1/6) | 769/512 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/1536 | (1/24, 1/12, 1/6) | 1537/1024 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/3072 | (1/24, 1/12, 1/6) | 3073/2048 | 2 | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 4 | DIFFERENT | 9fa7f38938046e47 | 148, 155, 166, 167 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (1/32, 1/12, 1/6) | 3/2 | 1 | (8, 13, 7) | 3^3 4^3 5^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (5/96, 1/12, 1/6) | 3/2 | 1 | (8, 13, 7) | 3^3 4^3 5^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |

**`f7bd7cd9eae6436b`** hexagonal IT(166) R-3m witness (1/12, 1/6, 11/24) c/a 1 basis [[1, 2, 0], [0, 0, 1]] base f=(16, 27, 13) 3^6 4^4 6^2 8^1 aut 2 ns 5 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/16, 1/8, 11/24) | 1 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (1, 2, 0) | -1/96 | (7/96, 7/48, 11/24) | 1 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (1, 2, 0) | 1/96 | (3/32, 3/16, 11/24) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point | (1, 2, 0) | 1/48 | (5/48, 5/24, 11/24) | 1 | 2 | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 4 | DIFFERENT | a1b2ac427f563716 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 1/6, 7/16) | 1 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 1/6, 43/96) | 1 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 1/6, 15/32) | 1 | 2 | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 4 | DIFFERENT | a1b2ac427f563716 | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 1/6, 23/48) | 1 | 2 | (16, 27, 13) | 3^6 4^4 6^2 8^1 | 2 | 6 | DIFFERENT | cf213e55efccc5f8 | 155, 166 | True | False |
| metric | - | -1/96 | (1/12, 1/6, 11/24) | 95/96 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric | - | -1/192 | (1/12, 1/6, 11/24) | 191/192 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric | - | 1/192 | (1/12, 1/6, 11/24) | 193/192 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| metric | - | 1/96 | (1/12, 1/6, 11/24) | 97/96 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (5/64, 5/32, 11/24) | 1 | 2 | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 3 | DIFFERENT | c53bc05bc306c97d | - | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (31/384, 31/192, 11/24) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (21/256, 21/128, 11/24) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (127/1536, 127/768, 11/24) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (17/192, 17/96, 11/24) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (11/128, 11/64, 11/24) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (65/768, 65/384, 11/24) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (43/512, 43/256, 11/24) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 1/6, 29/64) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 1/6, 175/384) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 1/6, 117/256) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 1/6, 703/1536) | 1 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 1/6, 89/192) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 1/6, 59/128) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 1/6, 353/768) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 1/6, 235/512) | 1 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| metric (refine) | - | -1/384 | (1/12, 1/6, 11/24) | 383/384 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric (refine) | - | -1/768 | (1/12, 1/6, 11/24) | 767/768 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric (refine) | - | -1/1536 | (1/12, 1/6, 11/24) | 1535/1536 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric (refine) | - | -1/3072 | (1/12, 1/6, 11/24) | 3071/3072 | 2 | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 4 | DIFFERENT | b3d52575f76a33bd | 148, 166 | True | False |
| metric (refine) | - | 1/384 | (1/12, 1/6, 11/24) | 385/384 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| metric (refine) | - | 1/768 | (1/12, 1/6, 11/24) | 769/768 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| metric (refine) | - | 1/1536 | (1/12, 1/6, 11/24) | 1537/1536 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| metric (refine) | - | 1/3072 | (1/12, 1/6, 11/24) | 3073/3072 | 2 | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 3 | DIFFERENT | 36c92427e3d084dc | - | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (7/96, 1/6, 11/24) | 1 | 1 | (10, 16, 8) | 3^3 4^3 5^1 6^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (3/32, 1/6, 11/24) | 1 | 1 | (10, 16, 8) | 3^3 4^3 5^1 6^1 | 1 | 2 | DIFFERENT | not stored | - | True | False |

**`75c9be976d704515`** hexagonal IT(152) P3_121 witness (0, 3/8, 1/6) c/a 9/8 basis [[0, 1, 0]] base f=(18, 28, 12) 4^8 6^4 aut 2 ns 2 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 17/48, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 35/96, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 37/96, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point | (0, 1, 0) | 1/48 | (0, 19/48, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | -1/96 | (0, 3/8, 1/6) | 285/256 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | -1/192 | (0, 3/8, 1/6) | 573/512 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric | - | 1/192 | (0, 3/8, 1/6) | 579/512 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric | - | 1/96 | (0, 3/8, 1/6) | 291/256 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 71/192, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 143/384, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (0, 287/768, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (0, 575/1536, 1/6) | 9/8 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (0, 73/192, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (0, 145/384, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (0, 289/768, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (0, 577/1536, 1/6) | 9/8 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | -1/384 | (0, 3/8, 1/6) | 1149/1024 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/768 | (0, 3/8, 1/6) | 2301/2048 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/1536 | (0, 3/8, 1/6) | 4605/4096 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | -1/3072 | (0, 3/8, 1/6) | 9213/8192 | 2 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| metric (refine) | - | 1/384 | (0, 3/8, 1/6) | 1155/1024 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/768 | (0, 3/8, 1/6) | 2307/2048 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/1536 | (0, 3/8, 1/6) | 4611/4096 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| metric (refine) | - | 1/3072 | (0, 3/8, 1/6) | 9219/8192 | 2 | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 0 | DIFFERENT | 1a36f90bbc759307 | 144, 145, 151, 153, 169, 170 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 3/8, 1/6) | 9/8 | 1 | (27, 43, 18) | 3^6 4^4 5^4 6^1 7^2 12^1 | 1 | 5 | DIFFERENT | 6fb79c742896c91e | 152, 154 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 3/8, 1/6) | 9/8 | 1 | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 4 | DIFFERENT | 0417061f8f56488e | - | True | False |

**`8463196a30c6643f`** hexagonal IT(179) P6_522 witness (1/8, 1/6, 5/12) c/a 2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(23, 36, 15) 3^2 4^5 5^2 6^6 aut 1 ns 3 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 2 | 1 | (22, 34, 14) | 3^4 4^3 5^2 6^3 8^2 | 1 | 2 | DIFFERENT | b3981da714598974 | 178, 179 | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 2 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 2 | 1 | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/48 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/96 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/96 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/48 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 2 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 2 | 1 | (25, 39, 16) | 3^4 4^3 5^4 6^3 8^2 | 1 | 3 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 2 | 1 | (30, 45, 17) | 3^2 4^5 6^8 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 2 | 1 | (30, 45, 17) | 3^2 4^5 6^8 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 2 | 1 | (30, 45, 17) | 3^2 4^5 6^8 8^2 | 1 | 0 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 2 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 383/192 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric (refine) | - | -1/768 | (1/8, 1/6, 5/12) | 767/384 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric (refine) | - | -1/1536 | (1/8, 1/6, 5/12) | 1535/768 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric (refine) | - | -1/3072 | (1/8, 1/6, 5/12) | 3071/1536 | 1 | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 0 | DIFFERENT | 99e39b85a778ce64 | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 385/192 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| metric (refine) | - | 1/768 | (1/8, 1/6, 5/12) | 769/384 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| metric (refine) | - | 1/1536 | (1/8, 1/6, 5/12) | 1537/768 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |
| metric (refine) | - | 1/3072 | (1/8, 1/6, 5/12) | 3073/1536 | 1 | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 1 | DIFFERENT | 11a9fe078850b5cd | - | True | False |

**`487490cdf474e568`** hexagonal IT(148) R-3 witness (1/12, 3/8, 1/6) c/a 1277/2000 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(20, 32, 14) 3^4 4^5 6^3 7^2 aut 1 ns 3 — POINT WALL / METRIC OPEN / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 1277/2000 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | DIFFERENT | 6074c5fa5d2dffc5 | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 1277/2000 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | DIFFERENT | 6074c5fa5d2dffc5 | - | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | DIFFERENT | 1ba26ab2c0999b93 | - | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 3 | DIFFERENT | 1ba26ab2c0999b93 | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 4 | DIFFERENT | 47b6d29f5de536f0 | 155, 160, 161, 166 | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 1277/2000 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^1 9^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 24263/38400 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 243907/384000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 246461/384000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 123869/192000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 1277/2000 | 1 | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 3 | DIFFERENT | 6074c5fa5d2dffc5 | - | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 1277/2000 | 1 | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 3 | SAME | 487490cdf474e568 | - | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/12, 3/8, 31/192) | 1277/2000 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^1 9^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/12, 3/8, 21/128) | 1277/2000 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^1 9^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/12, 3/8, 127/768) | 1277/2000 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^1 9^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/12, 3/8, 85/512) | 1277/2000 | 1 | (28, 44, 18) | 3^6 4^5 6^4 8^1 9^2 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/12, 3/8, 11/64) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/12, 3/8, 65/384) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/12, 3/8, 43/256) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/12, 3/8, 257/1536) | 1277/2000 | 1 | (24, 38, 16) | 3^6 4^1 5^4 6^2 7^2 8^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |

**`f0e2036d295195b4`** hexagonal IT(152) P3_121 witness (0, 1/8, 1/6) c/a 9/8 basis [[0, 1, 0]] base f=(12, 20, 10) 3^4 4^4 6^2 aut 2 ns 4 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 5/48, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point | (0, 1, 0) | -1/96 | (0, 11/96, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point | (0, 1, 0) | 1/96 | (0, 13/96, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point | (0, 1, 0) | 1/48 | (0, 7/48, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric | - | -1/96 | (0, 1/8, 1/6) | 285/256 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric | - | -1/192 | (0, 1/8, 1/6) | 573/512 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric | - | 1/192 | (0, 1/8, 1/6) | 579/512 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| metric | - | 1/96 | (0, 1/8, 1/6) | 291/256 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (0, 23/192, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (0, 47/384, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (0, 95/768, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (0, 191/1536, 1/6) | 9/8 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (0, 25/192, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (0, 49/384, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (0, 97/768, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (0, 193/1536, 1/6) | 9/8 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | -1/384 | (0, 1/8, 1/6) | 1149/1024 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | -1/768 | (0, 1/8, 1/6) | 2301/2048 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | -1/1536 | (0, 1/8, 1/6) | 4605/4096 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | -1/3072 | (0, 1/8, 1/6) | 9213/8192 | 2 | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 2 | DIFFERENT | 4a31af4ea18688a8 | 144, 145 | True | False |
| metric (refine) | - | 1/384 | (0, 1/8, 1/6) | 1155/1024 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| metric (refine) | - | 1/768 | (0, 1/8, 1/6) | 2307/2048 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| metric (refine) | - | 1/1536 | (0, 1/8, 1/6) | 4611/4096 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| metric (refine) | - | 1/3072 | (0, 1/8, 1/6) | 9219/8192 | 2 | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 2 | DIFFERENT | 1d2c47d061a6ab6c | 144, 145, 152, 154 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (-1/96, 1/8, 1/6) | 9/8 | 1 | (24, 36, 14) | 4^6 6^8 | 48 | 0 | DIFFERENT | 31d09faf7fb2bf6f | 76, 77, 78, 79, 81, 82, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 101, 102, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 128, 131, 132, 134, 136, 139, 146, 148, 155, 160, 161, 166, 167 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (1/96, 1/8, 1/6) | 9/8 | 1 | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 0 | DIFFERENT | 72bcd959be4ab7dd | - | True | False |

**`67b1ede4b021a4fc`** hexagonal IT(155) R32 witness (1/8, 1/6, 5/12) c/a 3/2 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(17, 29, 14) 3^4 4^6 5^2 6^2 aut 1 ns 5 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 3/2 | 1 | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 4 | DIFFERENT | d9bf7fb7a80eaa38 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/64 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/128 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/128 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/64 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 3/2 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 3/2 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 383/256 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric (refine) | - | -1/768 | (1/8, 1/6, 5/12) | 767/512 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric (refine) | - | -1/1536 | (1/8, 1/6, 5/12) | 1535/1024 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric (refine) | - | -1/3072 | (1/8, 1/6, 5/12) | 3071/2048 | 1 | (28, 44, 18) | 3^2 4^8 5^4 6^2 8^1 10^1 | 1 | 4 | DIFFERENT | not stored | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 385/256 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric (refine) | - | 1/768 | (1/8, 1/6, 5/12) | 769/512 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric (refine) | - | 1/1536 | (1/8, 1/6, 5/12) | 1537/1024 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |
| metric (refine) | - | 1/3072 | (1/8, 1/6, 5/12) | 3073/2048 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 6 | DIFFERENT | 52c5120f1148da14 | 155 | True | False |

**`34e5e7acce18b5cd`** hexagonal IT(166) R-3m witness (1/24, 1/12, 5/12) c/a 3/2 basis [[1, 2, 0], [0, 0, 1]] base f=(14, 23, 11) 3^6 4^2 6^2 8^1 aut 2 ns 4 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (1/48, 1/24, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | -1/96 | (1/32, 1/16, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | 1/96 | (5/96, 5/48, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point | (1, 2, 0) | 1/48 | (1/16, 1/8, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/48 | (1/24, 1/12, 19/48) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | -1/96 | (1/24, 1/12, 13/32) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/96 | (1/24, 1/12, 41/96) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point | (0, 0, 1) | 1/48 | (1/24, 1/12, 7/16) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric | - | -1/96 | (1/24, 1/12, 5/12) | 95/64 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric | - | -1/192 | (1/24, 1/12, 5/12) | 191/128 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric | - | 1/192 | (1/24, 1/12, 5/12) | 193/128 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric | - | 1/96 | (1/24, 1/12, 5/12) | 97/64 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/192 | (7/192, 7/96, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (5/128, 5/64, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (31/768, 31/384, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (21/512, 21/256, 5/12) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (3/64, 3/32, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (17/384, 17/192, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (11/256, 11/128, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (65/1536, 65/768, 5/12) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/24, 1/12, 79/192) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/24, 1/12, 53/128) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/24, 1/12, 319/768) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/24, 1/12, 213/512) | 3/2 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/24, 1/12, 27/64) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/24, 1/12, 161/384) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/24, 1/12, 107/256) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/24, 1/12, 641/1536) | 3/2 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | -1/384 | (1/24, 1/12, 5/12) | 383/256 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | -1/768 | (1/24, 1/12, 5/12) | 767/512 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | -1/1536 | (1/24, 1/12, 5/12) | 1535/1024 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | -1/3072 | (1/24, 1/12, 5/12) | 3071/2048 | 2 | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 2 | DIFFERENT | fa027394e7e22a9e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/384 | (1/24, 1/12, 5/12) | 385/256 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/768 | (1/24, 1/12, 5/12) | 769/512 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/1536 | (1/24, 1/12, 5/12) | 1537/1024 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| metric (refine) | - | 1/3072 | (1/24, 1/12, 5/12) | 3073/2048 | 2 | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 2 | DIFFERENT | 3f5fce0d11d8899e | 148, 155, 166, 167 | True | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (1/32, 1/12, 5/12) | 3/2 | 1 | (9, 14, 7) | 3^3 4^2 5^1 6^1 | 1 | 1 | DIFFERENT | 09db8da0e3d736f9 | 166, 180, 181 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (5/96, 1/12, 5/12) | 3/2 | 1 | (9, 14, 7) | 3^3 4^2 5^1 6^1 | 1 | 1 | DIFFERENT | 09db8da0e3d736f9 | 166, 180, 181 | True | False |

**`fa9c370d30741970`** hexagonal IT(180) P6_222 witness (1/6, 1/3, 0) c/a 3/2 basis [[1, 2, 0]] base f=(9, 16, 9) 3^4 4^5 aut 2 ns 5 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 2, 0) | -1/48 | (7/48, 7/24, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point | (1, 2, 0) | -1/96 | (5/32, 5/16, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point | (1, 2, 0) | 1/96 | (17/96, 17/48, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| point | (1, 2, 0) | 1/48 | (3/16, 3/8, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| metric | - | -1/96 | (1/6, 1/3, 0) | 95/64 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric | - | -1/192 | (1/6, 1/3, 0) | 191/128 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric | - | 1/192 | (1/6, 1/3, 0) | 193/128 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| metric | - | 1/96 | (1/6, 1/3, 0) | 97/64 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| point (refine) | (1, 2, 0) | -1/192 | (31/192, 31/96, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point (refine) | (1, 2, 0) | -1/384 | (21/128, 21/64, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point (refine) | (1, 2, 0) | -1/768 | (127/768, 127/384, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point (refine) | (1, 2, 0) | -1/1536 | (85/512, 85/256, 0) | 3/2 | 2 | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 4 | DIFFERENT | 4a6f33270c17ba66 | 152, 154, 171, 172, 178, 179, 180, 181 | True | False |
| point (refine) | (1, 2, 0) | 1/192 | (11/64, 11/32, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| point (refine) | (1, 2, 0) | 1/384 | (65/384, 65/192, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| point (refine) | (1, 2, 0) | 1/768 | (43/256, 43/128, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| point (refine) | (1, 2, 0) | 1/1536 | (257/1536, 257/768, 0) | 3/2 | 2 | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 2 | DIFFERENT | c57d8f62f90c0cf0 | 171, 172 | True | False |
| metric (refine) | - | -1/384 | (1/6, 1/3, 0) | 383/256 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric (refine) | - | -1/768 | (1/6, 1/3, 0) | 767/512 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric (refine) | - | -1/1536 | (1/6, 1/3, 0) | 1535/1024 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric (refine) | - | -1/3072 | (1/6, 1/3, 0) | 3071/2048 | 2 | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 2 | DIFFERENT | 6a892fdc51b24155 | 171, 172 | False | False |
| metric (refine) | - | 1/384 | (1/6, 1/3, 0) | 385/256 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| metric (refine) | - | 1/768 | (1/6, 1/3, 0) | 769/512 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| metric (refine) | - | 1/1536 | (1/6, 1/3, 0) | 1537/1024 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| metric (refine) | - | 1/3072 | (1/6, 1/3, 0) | 3073/2048 | 2 | (12, 19, 9) | 3^4 4^2 6^3 | 2 | 2 | DIFFERENT | 03b5c7cc17c5e015 | 119, 171, 172 | False | False |
| point (off-stratum) | (1, 0, 0) | -1/96 | (5/32, 1/3, 0) | 3/2 | 1 | (19, 31, 14) | 3^4 4^8 8^1 10^1 | 1 | 5 | DIFFERENT | a5350e795ad47e82 | 180, 181 | True | False |
| point (off-stratum) | (1, 0, 0) | 1/96 | (17/96, 1/3, 0) | 3/2 | 1 | (19, 31, 14) | 3^4 4^8 8^1 10^1 | 1 | 5 | DIFFERENT | a5350e795ad47e82 | 180, 181 | True | False |

**`400cba5c78326d1d`** hexagonal IT(167) R-3c witness (1/8, 1/6, 5/12) c/a 1 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(17, 28, 13) 4^10 5^2 6^1 aut 1 ns 5 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point | (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric | - | -1/96 | (1/8, 1/6, 5/12) | 95/96 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric | - | -1/192 | (1/8, 1/6, 5/12) | 191/192 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric | - | 1/192 | (1/8, 1/6, 5/12) | 193/192 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| metric | - | 1/96 | (1/8, 1/6, 5/12) | 97/96 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (23/192, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (47/384, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (95/768, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (191/1536, 1/6, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (25/192, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (49/384, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (97/768, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (193/1536, 1/6, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/8, 31/192, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/8, 21/128, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/8, 127/768, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/8, 85/512, 5/12) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/8, 11/64, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/8, 65/384, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/8, 43/256, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/8, 257/1536, 5/12) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/192 | (1/8, 1/6, 79/192) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/384 | (1/8, 1/6, 53/128) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/768 | (1/8, 1/6, 319/768) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | -1/1536 | (1/8, 1/6, 213/512) | 1 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| point (refine) | (0, 0, 1) | 1/192 | (1/8, 1/6, 27/64) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 0, 1) | 1/384 | (1/8, 1/6, 161/384) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 0, 1) | 1/768 | (1/8, 1/6, 107/256) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| point (refine) | (0, 0, 1) | 1/1536 | (1/8, 1/6, 641/1536) | 1 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric (refine) | - | -1/384 | (1/8, 1/6, 5/12) | 383/384 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric (refine) | - | -1/768 | (1/8, 1/6, 5/12) | 767/768 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric (refine) | - | -1/1536 | (1/8, 1/6, 5/12) | 1535/1536 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric (refine) | - | -1/3072 | (1/8, 1/6, 5/12) | 3071/3072 | 1 | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 2 | DIFFERENT | 4ff9d77aa9f8194a | - | True | False |
| metric (refine) | - | 1/384 | (1/8, 1/6, 5/12) | 385/384 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| metric (refine) | - | 1/768 | (1/8, 1/6, 5/12) | 769/768 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| metric (refine) | - | 1/1536 | (1/8, 1/6, 5/12) | 1537/1536 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |
| metric (refine) | - | 1/3072 | (1/8, 1/6, 5/12) | 3073/3072 | 1 | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 2 | DIFFERENT | 4297fd505b9cc36d | 148, 155, 166 | True | False |

**`78e755ffdff3a2f5`** hexagonal IT(146) R3 witness (1/12, 3/8, 1/6) c/a 3/4 basis [[1, 0, 0], [0, 1, 0], [0, 0, 1]] base f=(14, 24, 12) 3^4 4^6 6^2 aut 2 ns 6 — POINT WALL / METRIC WALL / COMBINED **WALL**

| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 0, 0) | -1/48 | (1/16, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | DIFFERENT | 7b9cfe26fe4a9c4b | - | True | False |
| point | (1, 0, 0) | -1/96 | (7/96, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point | (1, 0, 0) | 1/96 | (3/32, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point | (1, 0, 0) | 1/48 | (5/48, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point | (0, 1, 0) | -1/48 | (1/12, 17/48, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point | (0, 1, 0) | -1/96 | (1/12, 35/96, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point | (0, 1, 0) | 1/96 | (1/12, 37/96, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | DIFFERENT | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 1, 0) | 1/48 | (1/12, 19/48, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 6 | DIFFERENT | 7b9cfe26fe4a9c4b | - | True | False |
| point | (0, 0, 1) | -1/48 | (1/12, 3/8, 7/48) | 3/4 | 1 | (14, 24, 12) | 3^4 4^6 6^2 | 2 | 6 | SAME | 78e755ffdff3a2f5 | - | True | False |
| point | (0, 0, 1) | -1/96 | (1/12, 3/8, 5/32) | 3/4 | 1 | (14, 24, 12) | 3^4 4^6 6^2 | 2 | 6 | SAME | 78e755ffdff3a2f5 | - | True | False |
| point | (0, 0, 1) | 1/96 | (1/12, 3/8, 17/96) | 3/4 | 1 | (14, 24, 12) | 3^4 4^6 6^2 | 2 | 6 | SAME | 78e755ffdff3a2f5 | - | True | False |
| point | (0, 0, 1) | 1/48 | (1/12, 3/8, 3/16) | 3/4 | 1 | (14, 24, 12) | 3^4 4^6 6^2 | 2 | 6 | SAME | 78e755ffdff3a2f5 | - | True | False |
| metric | - | -1/96 | (1/12, 3/8, 1/6) | 95/128 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric | - | -1/192 | (1/12, 3/8, 1/6) | 191/256 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric | - | 1/192 | (1/12, 3/8, 1/6) | 193/256 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| metric | - | 1/96 | (1/12, 3/8, 1/6) | 97/128 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/192 | (5/64, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/384 | (31/384, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/768 | (21/256, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (1, 0, 0) | -1/1536 | (127/1536, 3/8, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (1, 0, 0) | 1/192 | (17/192, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (1, 0, 0) | 1/384 | (11/128, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (1, 0, 0) | 1/768 | (65/768, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (1, 0, 0) | 1/1536 | (43/512, 3/8, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (0, 1, 0) | -1/192 | (1/12, 71/192, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (0, 1, 0) | -1/384 | (1/12, 143/384, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (0, 1, 0) | -1/768 | (1/12, 287/768, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (0, 1, 0) | -1/1536 | (1/12, 575/1536, 1/6) | 3/4 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| point (refine) | (0, 1, 0) | 1/192 | (1/12, 73/192, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (0, 1, 0) | 1/384 | (1/12, 145/384, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (0, 1, 0) | 1/768 | (1/12, 289/768, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| point (refine) | (0, 1, 0) | 1/1536 | (1/12, 577/1536, 1/6) | 3/4 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| metric (refine) | - | -1/384 | (1/12, 3/8, 1/6) | 383/512 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric (refine) | - | -1/768 | (1/12, 3/8, 1/6) | 767/1024 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric (refine) | - | -1/1536 | (1/12, 3/8, 1/6) | 1535/2048 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric (refine) | - | -1/3072 | (1/12, 3/8, 1/6) | 3071/4096 | 1 | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 4 | DIFFERENT | efc24204486dde03 | 146, 155 | True | False |
| metric (refine) | - | 1/384 | (1/12, 3/8, 1/6) | 385/512 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| metric (refine) | - | 1/768 | (1/12, 3/8, 1/6) | 769/1024 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| metric (refine) | - | 1/1536 | (1/12, 3/8, 1/6) | 1537/2048 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |
| metric (refine) | - | 1/3072 | (1/12, 3/8, 1/6) | 3073/4096 | 1 | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 6 | DIFFERENT | c97273f4df7f3fdc | 146 | True | False |

