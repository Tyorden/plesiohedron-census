# Phase-2 (tetragonal) collision screen + first perturbation certificates — TOP-15 shortlist (2026-09-04)

Script: `collision_phase2_check.py` (pattern: `schmitt_collision_check.py`, `round1_computations/c1_wall_open.py`). Inputs: `phase2_types.json` (sha256 `71685b9ab41b4dc0...`, MATCHES `phase2_types.SHA256SUMS`), `schmitt_tetragonal_tables.json` (VISUAL digitization 2026-09-04, single pass, text-layer cross-checked, NOT re-keyed), `phase2_schmitt_origin_check.json` / `PHASE2_SCHMITT_ORIGIN_CHECK.md` (setting conversions), worklist = `TRIAGE_PHASE2_RESULT.md` (27 pairs: 20 `other` + 7 `unres`). Chain: the ACCEPTED phase-2 modules (`phase2/metric.py`, `phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`) via `sweep_phase2_tetragonal.evaluate` with the `exact_cell.order_cycle` exact fallback (ORDER_CYCLE_FIX_2026-09-04.md). Certificate asserted per cell: 4*rho^2 <= D^2 on cell 0 AND on a second orbit cell, Euler, float/exact agreement, one canonical code across the orbit, stab | aut. Per-pair wall-clock cap 600 s -> TIMEOUT-DEFERRED (recorded, never silent). Exact arithmetic decides.

**LANGUAGE (G5, stated ONCE for every verdict below): a DIFFERENT-TYPE verdict does NOT establish novelty.** Schmitt 2016 prints ONE representative generating point per (group, f-vector) from a grid SAMPLING (351 CPU-years, ~14 TB unprinted); a type absent at his printed point may still occur in his unprinted data. Every survivor stays "not matched against the catalog snapshot of 2026-09-03". A SAME-TYPE verdict IS decisive (collision: reframe to first-realization per the kill criteria). A DIFFERENT verdict at the same (group, f, b) is a same-f-vector-two-types micro-fact (tetragonal edition of the Josehedron / Schmitt-220 pair).

## Citations and conversions (27 pairs)

Printed rows keyed (f, b, point) in `schmitt_tetragonal_tables.json`; PDF page = printed page + 5. Conversions (PHASE2_SCHMITT_ORIGIN_CHECK.md, each verified on ALL printed rows of its group): origin-choice-2 groups: p_ours = p_his + s (s = the check's best_shift; the other shifts that also reproduced every row are re-run as a robustness check and must give the same canonical code); second enantiomorphs 95/96: z -> -z; IT(80): none (order_cycle crash row, now exact fallback). `other` rows: the stored P2 cell (printed point verbatim, origin choice 1 = Schmitt's for one-origin groups).

| pair | rank | target | IT | printed f | printed b | printed point (Schmitt coords) | PDF p. (printed p.) | P2 outcome | conversion applied | point in our setting |
|---|---|---|---|---|---|---|---|---|---|---|
| Q01 | 1 | `4e9c9b076cfec323` | 92 P4_12_12 | (40, 60, 22) | 7/5 | (1951/3996, 1/3996, 1/7992) | 47 (42) | other `cf92c5d0bb79041b` | none (stored P2 cell, printed point verbatim) | (1951/3996, 1/3996, 1/7992) |
| Q02 | 1 | `4e9c9b076cfec323` | 96 P4_32_12 | (40, 60, 22) | 7/5 | (1951/3996, 1/3996, 1/7992) | 47 (42) | unres (not stored) | second enantiomorph: z -> -z | (1951/3996, 1/3996, -1/7992) |
| Q03 | 2 | `49cedbdd58376fac` | 92 P4_12_12 | (44, 66, 24) | 797/1000 | (57/125, 2/125, 1/8) | 47 (42) | other `ab93cbeb7be9da28` | none (stored P2 cell, printed point verbatim) | (57/125, 2/125, 1/8) |
| Q04 | 2 | `49cedbdd58376fac` | 96 P4_32_12 | (44, 66, 24) | 797/1000 | (57/125, 2/125, 1/8) | 47 (42) | unres (not stored) | second enantiomorph: z -> -z | (57/125, 2/125, -1/8) |
| Q05 | 3 | `f654982d74d740f6` | 141 I4_1/amd | (38, 57, 21) | 797/1000 | (1/2, 47/125, 31/250) | 84 (79) | unres (not stored) | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 563/500, 249/1000) |
| Q06 | 4 | `4f6d3e68cbd9e729` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 (48) | other `2f2e04c27de95ac3` | none (stored P2 cell, printed point verbatim) | (1129/2518, 859/2518, 565/5036) |
| Q07 | 5 | `1497877268495988` | 91 P4_122 | (32, 48, 18) | 14/25 | (229/3996, 71/3996, 61/2664) | 45 (40) | other `e5db0e3617afd976` | none (stored P2 cell, printed point verbatim) | (229/3996, 71/3996, 61/2664) |
| Q08 | 5 | `1497877268495988` | 95 P4_322 | (32, 48, 18) | 14/25 | (229/3996, 71/3996, 61/2664) | 45 (40) | other `e2bae62d988092d4` | none (stored P2 cell, printed point verbatim) | (229/3996, 71/3996, 61/2664) |
| Q09 | 6 | `e0d18e5ea938d649` | 122 I-42d | (36, 54, 20) | 3497/1000 | (34/125, 34/125, 31/250) | 70 (65) | other `5af057df372beee8` | none (stored P2 cell, printed point verbatim) | (34/125, 34/125, 31/250) |
| Q10 | 7 | `6797ab70c6015039` | 76 P4_1 | (32, 48, 18) | 797/1000 | (1/4, -1/4, 0) | 33 (28) | other `e5760549017956be` | none (stored P2 cell, printed point verbatim) | (1/4, -1/4, 0) |
| Q11 | 7 | `6797ab70c6015039` | 78 P4_3 | (32, 48, 18) | 797/1000 | (1/4, -1/4, 0) | 33 (28) | other `e5760549017956be` | none (stored P2 cell, printed point verbatim) | (1/4, -1/4, 0) |
| Q12 | 7 | `6797ab70c6015039` | 92 P4_12_12 | (32, 48, 18) | 7/5 | (22/333, 44/999, 61/2664) | 47 (42) | other `1614109bcc5801ed` | none (stored P2 cell, printed point verbatim) | (22/333, 44/999, 61/2664) |
| Q13 | 7 | `6797ab70c6015039` | 96 P4_32_12 | (32, 48, 18) | 7/5 | (22/333, 44/999, 61/2664) | 47 (42) | other `3a7c6d5f00cde1ae` | none (stored P2 cell, printed point verbatim) | (22/333, 44/999, 61/2664) |
| Q14 | 8 | `cd4fb52572edcb73` | 86 P4_2/n | (30, 45, 17) | 3497/1000 | (59/125, 0, 31/125) | 40 (35) | unres (not stored) | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (361/500, 1/4, 249/500) |
| Q15 | 8 | `cd4fb52572edcb73` | 93 P4_222 | (30, 45, 17) | 3497/1000 | (231/500, -17/500, 107/500) | 48 (43) | other `adbb83c95151fc35` | none (stored P2 cell, printed point verbatim) | (231/500, -17/500, 107/500) |
| Q16 | 8 | `cd4fb52572edcb73` | 118 P-4n2 | (30, 45, 17) | 3497/1000 | (247/500, -1/500, 123/500) | 66 (61) | other `da1833391efcd38c` | none (stored P2 cell, printed point verbatim) | (247/500, -1/500, 123/500) |
| Q17 | 8 | `cd4fb52572edcb73` | 134 P4_2/nnm | (30, 45, 17) | 797/1000 | (219/500, -31/500, 47/250) | 79 (74) | unres (not stored) | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (86/125, 86/125, 219/500) |
| Q18 | 9 | `086ac96faf390886` | 76 P4_1 | (36, 54, 20) | 797/1000 | (1597/3996, 401/3996, 0) | 33 (28) | other `0087d56fd2a8a610` | none (stored P2 cell, printed point verbatim) | (1597/3996, 401/3996, 0) |
| Q19 | 9 | `086ac96faf390886` | 78 P4_3 | (36, 54, 20) | 797/1000 | (1597/3996, 401/3996, 0) | 33 (28) | other `0087d56fd2a8a610` | none (stored P2 cell, printed point verbatim) | (1597/3996, 401/3996, 0) |
| Q20 | 10 | `164d4bd63d82d0c3` | 76 P4_1 | (40, 60, 22) | 797/1000 | (1807/3996, 191/3996, 0) | 33 (28) | other `c1a62b4c22e7c6e8` | none (stored P2 cell, printed point verbatim) | (1807/3996, 191/3996, 0) |
| Q21 | 10 | `164d4bd63d82d0c3` | 78 P4_3 | (40, 60, 22) | 797/1000 | (1807/3996, 191/3996, 0) | 33 (28) | other `c1a62b4c22e7c6e8` | none (stored P2 cell, printed point verbatim) | (1807/3996, 191/3996, 0) |
| Q22 | 11 | `5dc2479b9bc14edc` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 (48) | other `2f2e04c27de95ac3` | none (stored P2 cell, printed point verbatim) | (1129/2518, 859/2518, 565/5036) |
| Q23 | 12 | `3ebbca7ed2eda199` | 98 I4_122 | (40, 60, 22) | 38/25 | (1129/2518, 553/1259, 565/5036) | 53 (48) | other `1d68503f7c026843` | none (stored P2 cell, printed point verbatim) | (1129/2518, 553/1259, 565/5036) |
| Q24 | 13 | `7575121042ade3b3` | 80 I4_1 | (32, 48, 18) | 3497/1000 | (353/1413, 235/942, 0) | 35 (30) | unres (not stored) | none (printed point verbatim) | (353/1413, 235/942, 0) |
| Q25 | 13 | `7575121042ade3b3` | 98 I4_122 | (32, 48, 18) | 38/25 | (1129/2518, 129/2518, 565/5036) | 52 (47) | other `014a0747d02498e7` | none (stored P2 cell, printed point verbatim) | (1129/2518, 129/2518, 565/5036) |
| Q26 | 14 | `213c7a114d5a97a8` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 (48) | other `2f2e04c27de95ac3` | none (stored P2 cell, printed point verbatim) | (1129/2518, 859/2518, 565/5036) |
| Q27 | 15 | `2e8e49eb28497267` | 95 P4_322 | (40, 60, 22) | 14/25 | (223/444, 355/1332, 239/7992) | 45 (40) | unres (not stored) | second enantiomorph: z -> -z | (223/444, 355/1332, -239/7992) |

## Per-pair verdicts

| pair | rank | target | IT | f | b | source | orbit | stab | PERIOD | Schmitt cell p-vector | aut | verdict | Schmitt cell = stored type | alt conversions agree | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q01 | 1 | `4e9c9b076cfec323` | 92 | (40, 60, 22) | 7/5 | store | 8 | 1 | - | `3^8 4^6 5^2 8^1 10^4 14^1` | 1 | **DIFFERENT TYPE** | `cf92c5d0bb79041b` | - | 0.0 |
| Q02 | 1 | `4e9c9b076cfec323` | 96 | (40, 60, 22) | 7/5 | exact chain (this run) | 8 | 1 | 7992 | `3^8 4^6 5^2 8^1 10^4 14^1` | 1 | **DIFFERENT TYPE** | `cf92c5d0bb79041b` | YES (3) | 0.7 |
| Q03 | 2 | `49cedbdd58376fac` | 92 | (44, 66, 24) | 797/1000 | store | 8 | 1 | - | `3^4 4^12 6^2 8^4 14^2` | 2 | **DIFFERENT TYPE** | `ab93cbeb7be9da28` | - | 0.0 |
| Q04 | 2 | `49cedbdd58376fac` | 96 | (44, 66, 24) | 797/1000 | exact chain (this run) | 8 | 1 | 3000 | `3^4 4^12 6^2 8^4 14^2` | 2 | **DIFFERENT TYPE** | `ab93cbeb7be9da28` | YES (3) | 1.0 |
| Q05 | 3 | `f654982d74d740f6` | 141 | (38, 57, 21) | 797/1000 | exact chain (this run) | 16 | 2 | 3000 | `3^6 4^7 6^4 10^3 14^1` | 2 | **DIFFERENT TYPE** | not stored | YES (3) | 1.0 |
| Q06 | 4 | `4f6d3e68cbd9e729` | 98 | (42, 63, 23) | 38/25 | store | 16 | 1 | - | `3^6 4^6 6^8 10^2 16^1` | 1 | **DIFFERENT TYPE** | `2f2e04c27de95ac3` | - | 0.0 |
| Q07 | 5 | `1497877268495988` | 91 | (32, 48, 18) | 14/25 | store | 8 | 1 | - | `3^4 4^3 5^2 6^6 8^2 10^1` | 1 | **DIFFERENT TYPE** | `e5db0e3617afd976` | - | 0.0 |
| Q08 | 5 | `1497877268495988` | 95 | (32, 48, 18) | 14/25 | store | 8 | 1 | - | `3^4 4^3 5^2 6^5 7^2 8^1 10^1` | 1 | **DIFFERENT TYPE** | `e2bae62d988092d4` | - | 0.0 |
| Q09 | 6 | `e0d18e5ea938d649` | 122 | (36, 54, 20) | 3497/1000 | store | 16 | 1 | - | `3^8 4^4 6^3 8^3 12^1 14^1` | 1 | **DIFFERENT TYPE** | `5af057df372beee8` | - | 0.0 |
| Q10 | 7 | `6797ab70c6015039` | 76 | (32, 48, 18) | 797/1000 | store | 4 | 1 | - | `3^8 4^2 6^4 10^4` | 8 | **DIFFERENT TYPE** | `e5760549017956be` | - | 0.0 |
| Q11 | 7 | `6797ab70c6015039` | 78 | (32, 48, 18) | 797/1000 | store | 4 | 1 | - | `3^8 4^2 6^4 10^4` | 8 | **DIFFERENT TYPE** | `e5760549017956be` | - | 0.0 |
| Q12 | 7 | `6797ab70c6015039` | 92 | (32, 48, 18) | 7/5 | store | 8 | 1 | - | `3^4 4^2 5^4 6^5 7^2 12^1` | 1 | **DIFFERENT TYPE** | `1614109bcc5801ed` | - | 0.0 |
| Q13 | 7 | `6797ab70c6015039` | 96 | (32, 48, 18) | 7/5 | store | 8 | 1 | - | `3^8 4^2 6^3 8^2 10^3` | 1 | **DIFFERENT TYPE** | `3a7c6d5f00cde1ae` | - | 0.0 |
| Q14 | 8 | `cd4fb52572edcb73` | 86 | (30, 45, 17) | 3497/1000 | exact chain (this run) | 8 | 1 | 1500 | `3^4 4^3 6^7 7^2 10^1` | 1 | **DIFFERENT TYPE** | not stored | YES (3) | 0.5 |
| Q15 | 8 | `cd4fb52572edcb73` | 93 | (30, 45, 17) | 3497/1000 | store | 8 | 1 | - | `3^4 4^3 5^2 6^6 10^2` | 1 | **DIFFERENT TYPE** | `adbb83c95151fc35` | - | 0.0 |
| Q16 | 8 | `cd4fb52572edcb73` | 118 | (30, 45, 17) | 3497/1000 | store | 8 | 1 | - | `3^4 4^1 5^6 6^4 10^2` | 1 | **DIFFERENT TYPE** | `da1833391efcd38c` | - | 0.0 |
| Q17 | 8 | `cd4fb52572edcb73` | 134 | (30, 45, 17) | 797/1000 | exact chain (this run) | 8 | 2 | 1500 | `4^9 5^4 6^1 8^2 12^1` | 2 | **SAME TYPE** | `cd4fb52572edcb73` | YES (3) | 0.6 |
| Q18 | 9 | `086ac96faf390886` | 76 | (36, 54, 20) | 797/1000 | store | 4 | 1 | - | `3^6 4^4 5^4 9^6` | 2 | **DIFFERENT TYPE** | `0087d56fd2a8a610` | - | 0.0 |
| Q19 | 9 | `086ac96faf390886` | 78 | (36, 54, 20) | 797/1000 | store | 4 | 1 | - | `3^6 4^4 5^4 9^6` | 2 | **DIFFERENT TYPE** | `0087d56fd2a8a610` | - | 0.0 |
| Q20 | 10 | `164d4bd63d82d0c3` | 76 | (40, 60, 22) | 797/1000 | store | 4 | 1 | - | `3^8 4^4 5^4 10^6` | 2 | **DIFFERENT TYPE** | `c1a62b4c22e7c6e8` | - | 0.0 |
| Q21 | 10 | `164d4bd63d82d0c3` | 78 | (40, 60, 22) | 797/1000 | store | 4 | 1 | - | `3^8 4^4 5^4 10^6` | 2 | **DIFFERENT TYPE** | `c1a62b4c22e7c6e8` | - | 0.0 |
| Q22 | 11 | `5dc2479b9bc14edc` | 98 | (42, 63, 23) | 38/25 | store | 16 | 1 | - | `3^6 4^6 6^8 10^2 16^1` | 1 | **DIFFERENT TYPE** | `2f2e04c27de95ac3` | - | 0.0 |
| Q23 | 12 | `3ebbca7ed2eda199` | 98 | (40, 60, 22) | 38/25 | store | 16 | 1 | - | `3^4 4^10 5^2 6^3 10^1 12^1 18^1` | 1 | **DIFFERENT TYPE** | `1d68503f7c026843` | - | 0.0 |
| Q24 | 13 | `7575121042ade3b3` | 80 | (32, 48, 18) | 3497/1000 | exact chain (this run) | 8 | 1 | 5652 | `3^4 4^6 5^2 6^1 8^2 9^2 10^1` | 1 | **DIFFERENT TYPE** | `19c7c8de77b6ce20` | n/a (none) | 0.1 |
| Q25 | 13 | `7575121042ade3b3` | 98 | (32, 48, 18) | 38/25 | store | 16 | 1 | - | `3^2 4^9 6^3 8^3 12^1` | 1 | **DIFFERENT TYPE** | `014a0747d02498e7` | - | 0.0 |
| Q26 | 14 | `213c7a114d5a97a8` | 98 | (42, 63, 23) | 38/25 | store | 16 | 1 | - | `3^6 4^6 6^8 10^2 16^1` | 1 | **DIFFERENT TYPE** | `2f2e04c27de95ac3` | - | 0.0 |
| Q27 | 15 | `2e8e49eb28497267` | 95 | (40, 60, 22) | 14/25 | exact chain (this run) | 8 | 1 | 7992 | `3^10 4^2 5^2 6^2 8^3 10^1 12^1 14^1` | 1 | **DIFFERENT TYPE** | `f6abc569d035765a` | YES (3) | 0.8 |

## Summary per shortlist type

- rank 1 `4e9c9b076cfec323`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 2 `49cedbdd58376fac`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 3 `f654982d74d740f6`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 4 `4f6d3e68cbd9e729`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 5 `1497877268495988`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 6 `e0d18e5ea938d649`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 7 `6797ab70c6015039`: survives this screen (all 4 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 8 `cd4fb52572edcb73`: COLLISION — Schmitt's printed cell IS this type in 1/4 checked pair(s); reframe per kill criteria (first-realization, not a new sighting-class candidate).
- rank 9 `086ac96faf390886`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 10 `164d4bd63d82d0c3`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 11 `5dc2479b9bc14edc`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 12 `3ebbca7ed2eda199`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 13 `7575121042ade3b3`: survives this screen (all 2 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 14 `213c7a114d5a97a8`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 15 `2e8e49eb28497267`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.

Notes on the 7 `unres` rows (all 7 reproduce the printed f-vector after the documented conversion, so no FVEC-MISMATCH; the conversions are therefore confirmed row-by-row here as well): Q02 IT(96) -> Schmitt's cell is stored type `cf92c5d0bb79041b`; Q04 IT(96) -> Schmitt's cell is stored type `ab93cbeb7be9da28`; Q05 IT(141) -> Schmitt's cell is NOT in the store (a type the menu never sampled; read-only, not added); Q14 IT(86) -> Schmitt's cell is NOT in the store (a type the menu never sampled; read-only, not added); Q17 IT(134) -> Schmitt's cell is stored type `cd4fb52572edcb73`; Q24 IT(80) -> Schmitt's cell is stored type `19c7c8de77b6ce20`; Q27 IT(95) -> Schmitt's cell is stored type `f6abc569d035765a`.

## Perturbation certificates (top-3)

Method: at the stored first witness (group, point, b) the point is moved by +-1/96, +-1/48 (fractional coordinates, conventional cell) along every tangent direction of its Wyckoff stratum (fixed subspace of the site stabilizer's linear parts) at the witness b, and the b-ratio is moved by +-1/96, +-1/48 at the witness point; where the smallest step on a side changes the canonical code the step is halved down to 1/1536. Point directions and the metric direction are classified SEPARATELY: OPEN = code unchanged at the smallest step on every side; WALL = changes on both sides of some direction; ONE-SIDED otherwise. The type on each side of a wall is reported with its stored id (else "not stored"). The off-stratum row (special positions only) is supplementary: it leaves the stratum and is not part of the verdict. Every perturbed cell went through the same certified chain (certificate asserted per cell); a ChainError is recorded as a quarantine row, never counted as SAME.

| # | type | IT | witness point | witness b | stratum dim (stab) | tangent basis | POINT verdict | METRIC (b) verdict | neighbouring types seen (f, p, aut, stored id; f printed in the group's Schmitt table) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | 92 P4_12_12 | (5/24, 5/24, 0) | 5/4 | 1 (2) | [(1, 1, 0)] | **OPEN** | **OPEN** | (36, 54, 20) 3^4 4^4 5^8 10^4 aut 8 [60c6a7023f6e4280; printed=True; via point]; (44, 66, 24) 3^10 4^4 6^4 7^2 12^4 aut 2 [49cedbdd58376fac; printed=True; via point] |
| 2 | `49cedbdd58376fac` | 92 P4_12_12 | (5/24, 5/24, 0) | 19/16 | 1 (2) | [(1, 1, 0)] | **WALL** walls [(1, 1, 0)] | **OPEN** | (32, 48, 18) 4^12 8^6 aut 6 [afeb1ae44c1a3443; printed=True; via point]; (36, 54, 20) 3^4 4^4 5^8 10^4 aut 8 [60c6a7023f6e4280; printed=True; via b, point]; (32, 48, 18) 3^8 4^2 6^4 10^4 aut 8 [e5760549017956be; printed=True; via b]; (40, 60, 22) 3^8 4^4 5^4 8^2 11^4 aut 2 [4e9c9b076cfec323; printed=True; via b, point] |
| 3 | `f654982d74d740f6` | 141 I4_1/amd | (0, 1/12, 1/12) | 1/2 | 2 (2) | [(0, 1, 0), (0, 0, 1)] | **OPEN** | **OPEN** | (29, 45, 18) 3^4 4^6 6^7 12^1 aut 2 [not stored; printed=True; via point]; (34, 51, 19) 4^11 6^5 8^2 12^1 aut 2 [9ff7306e4a6cbf44; printed=True; via b, point]; (31, 48, 19) 3^4 4^8 6^4 8^2 12^1 aut 2 [not stored; printed=True; via point] |

### Per-step detail

**`4e9c9b076cfec323`** IT(92) P4_12_12 witness (5/24, 5/24, 0) b=5/4, base f=(40, 60, 22) p=3^8 4^4 5^4 8^2 11^4 aut 2 (rederived from the witness; agrees with the store):

| kind | direction | eps | point | b | site stab | f | p | aut | non-simple | code | stored id | f printed in group table |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 1, 0) | -1/48 | (3/16, 3/16, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) | -1/96 | (19/96, 19/96, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) | 1/96 | (7/32, 7/32, 0) | 5/4 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| point | (1, 1, 0) | 1/48 | (11/48, 11/48, 0) | 5/4 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| b | b | -1/48 | (5/24, 5/24, 0) | 59/48 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| b | b | -1/96 | (5/24, 5/24, 0) | 119/96 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| b | b | 1/96 | (5/24, 5/24, 0) | 121/96 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| b | b | 1/48 | (5/24, 5/24, 0) | 61/48 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | 1/192 | (41/192, 41/192, 0) | 5/4 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | DIFFERENT | 49cedbdd58376fac | True |
| point | (1, 1, 0) (refine) | 1/384 | (27/128, 27/128, 0) | 5/4 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | DIFFERENT | 49cedbdd58376fac | True |
| point | (1, 1, 0) (refine) | 1/768 | (161/768, 161/768, 0) | 5/4 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | SAME | 4e9c9b076cfec323 | True |
| point | (1, 0, 0) (off-stratum, supplementary) | -1/96 | (19/96, 5/24, 0) | 5/4 | 1 | (36, 54, 20) | 3^4 4^4 5^6 6^2 9^2 10^2 | 1 | 0 | DIFFERENT | not stored | True |
| point | (1, 0, 0) (off-stratum, supplementary) | 1/96 | (7/32, 5/24, 0) | 5/4 | 1 | (34, 51, 19) | 3^4 4^3 5^4 6^4 8^2 9^2 | 1 | 0 | DIFFERENT | not stored | True |

**`49cedbdd58376fac`** IT(92) P4_12_12 witness (5/24, 5/24, 0) b=19/16, base f=(44, 66, 24) p=3^10 4^4 6^4 7^2 12^4 aut 2 (rederived from the witness; agrees with the store):

| kind | direction | eps | point | b | site stab | f | p | aut | non-simple | code | stored id | f printed in group table |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (1, 1, 0) | -1/48 | (3/16, 3/16, 0) | 19/16 | 2 | (32, 48, 18) | 4^12 8^6 | 6 | 0 | DIFFERENT | afeb1ae44c1a3443 | True |
| point | (1, 1, 0) | -1/96 | (19/96, 19/96, 0) | 19/16 | 2 | (32, 48, 18) | 4^12 8^6 | 6 | 0 | DIFFERENT | afeb1ae44c1a3443 | True |
| point | (1, 1, 0) | 1/96 | (7/32, 7/32, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| point | (1, 1, 0) | 1/48 | (11/48, 11/48, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| b | b | -1/48 | (5/24, 5/24, 0) | 7/6 | 2 | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 0 | DIFFERENT | e5760549017956be | True |
| b | b | -1/96 | (5/24, 5/24, 0) | 113/96 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| b | b | 1/96 | (5/24, 5/24, 0) | 115/96 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | SAME | 49cedbdd58376fac | True |
| b | b | 1/48 | (5/24, 5/24, 0) | 29/24 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | -1/192 | (13/64, 13/64, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | -1/384 | (79/384, 79/384, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | -1/768 | (53/256, 53/256, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | -1/1536 | (319/1536, 319/1536, 0) | 19/16 | 2 | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 0 | DIFFERENT | 4e9c9b076cfec323 | True |
| point | (1, 1, 0) (refine) | 1/192 | (41/192, 41/192, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| point | (1, 1, 0) (refine) | 1/384 | (27/128, 27/128, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| point | (1, 1, 0) (refine) | 1/768 | (161/768, 161/768, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| point | (1, 1, 0) (refine) | 1/1536 | (107/512, 107/512, 0) | 19/16 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| b | b (refine) | -1/192 | (5/24, 5/24, 0) | 227/192 | 2 | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 0 | DIFFERENT | 60c6a7023f6e4280 | True |
| b | b (refine) | -1/384 | (5/24, 5/24, 0) | 455/384 | 2 | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 0 | SAME | 49cedbdd58376fac | True |
| point | (1, 0, 0) (off-stratum, supplementary) | -1/96 | (19/96, 5/24, 0) | 19/16 | 1 | (29, 44, 17) | 3^4 4^4 5^3 6^1 7^2 8^2 9^1 | 1 | 1 | DIFFERENT | not stored | True |
| point | (1, 0, 0) (off-stratum, supplementary) | 1/96 | (7/32, 5/24, 0) | 19/16 | 1 | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 12 | 0 | DIFFERENT | 8c69db9e84095469 | True |

**`f654982d74d740f6`** IT(141) I4_1/amd witness (0, 1/12, 1/12) b=1/2, base f=(38, 57, 21) p=3^6 4^7 6^3 8^2 10^2 14^1 aut 2 (rederived from the witness; agrees with the store):

| kind | direction | eps | point | b | site stab | f | p | aut | non-simple | code | stored id | f printed in group table |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| point | (0, 1, 0) | -1/48 | (0, 1/16, 1/12) | 1/2 | 2 | (29, 45, 18) | 3^4 4^6 6^7 12^1 | 2 | 3 | DIFFERENT | not stored | True |
| point | (0, 1, 0) | -1/96 | (0, 7/96, 1/12) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | True |
| point | (0, 1, 0) | 1/96 | (0, 3/32, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (0, 1, 0) | 1/48 | (0, 5/48, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (0, 0, 1) | -1/48 | (0, 1/12, 1/16) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (0, 0, 1) | -1/96 | (0, 1/12, 7/96) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (0, 0, 1) | 1/96 | (0, 1/12, 3/32) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | True |
| point | (0, 0, 1) | 1/48 | (0, 1/12, 5/48) | 1/2 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | True |
| b | b | -1/48 | (0, 1/12, 1/12) | 23/48 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| b | b | -1/96 | (0, 1/12, 1/12) | 47/96 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| b | b | 1/96 | (0, 1/12, 1/12) | 49/96 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| b | b | 1/48 | (0, 1/12, 1/12) | 25/48 | 2 | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 0 | DIFFERENT | 9ff7306e4a6cbf44 | True |
| point | (0, 1, 0) (refine) | -1/192 | (0, 5/64, 1/12) | 1/2 | 2 | (31, 48, 19) | 3^4 4^8 6^4 8^2 12^1 | 2 | 3 | DIFFERENT | not stored | True |
| point | (0, 1, 0) (refine) | -1/384 | (0, 31/384, 1/12) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (0, 0, 1) (refine) | 1/192 | (0, 1/12, 17/192) | 1/2 | 2 | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 0 | SAME | f654982d74d740f6 | True |
| point | (1, 0, 0) (off-stratum, supplementary) | -1/96 | (-1/96, 1/12, 1/12) | 1/2 | 1 | (20, 30, 12) | 3^1 4^6 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | True |
| point | (1, 0, 0) (off-stratum, supplementary) | 1/96 | (1/96, 1/12, 1/12) | 1/2 | 1 | (20, 30, 12) | 3^1 4^6 6^3 7^1 8^1 | 1 | 0 | DIFFERENT | not stored | True |

### Reading of the perturbation results (hand-written from the tables above; asserted against the computed verdicts on every run)

- #1 `4e9c9b076cfec323` (IT 92, line (x,x,0), x = 5/24, b = 5/4): OPEN in the point direction and in b, but the open interval on the +x side is SHORT: +1/768 is SAME, +1/384 and +1/192 give `49cedbdd58376fac` (= shortlist #2), +1/96 and +1/48 give `60c6a7023f6e4280` (36,54,20); the -x side and both b sides hold at every tested step (b from 59/48 to 61/48). So #1 holds on a neighbourhood, with #2 as its immediate +x neighbour at b = 5/4.
- #2 `49cedbdd58376fac` (same line, x = 5/24, b = 19/16): WALL in the point direction at every tested step down to +-1/1536 (-x side: `4e9c9b076cfec323` = #1; +x side: `60c6a7023f6e4280`), yet OPEN in b at the witness point (SAME at b = 455/384 and 115/96; -1/192 gives `60c6a7023f6e4280`, -1/48 gives `e5760549017956be`, +1/48 gives #1). Together with the #1 scan (where #2 occupies x = 5/24 + 1/384 .. + 1/192 at b = 5/4) this reads as a THIN BAND in the (x, b) plane running from about (5/24, 19/16) to (5/24 + ~1/300, 5/4): not a strict codimension-1 wall (it has b-width), but of width < 1/768 in x at b = 19/16. The cell is simple (0 non-simple vertices) so the x-interval is nonempty; only its width is below the tested resolution. CORRECTION to the triage labels: the 'wall-suspect' / METRIC-THIN (1 b) label on #2 was b-based and is refuted in b (open on [455/384, 115/96] at x = 5/24) and #2 is now also sighted at b = 5/4 (at x = 5/24 + 1/384, + 1/192, read-only, NOT added to the store); the label survives only as 'thin in x'. Whether #2 deserves a G4 slot of its own or is best presented as the transition type between #1 and `60c6a7023f6e4280` is a judgment for the main session.
- #3 `f654982d74d740f6` (IT 141, plane (0,y,z), witness (0,1/12,1/12), b = 1/2): OPEN in both point directions and in b; the -y side is short (-1/384 SAME; -1/192 gives a NOT-STORED (31,48,19) cell with 3 non-simple vertices, i.e. a wall cell; -1/96 gives `9ff7306e4a6cbf44` (34,51,19); -1/48 gives a NOT-STORED (29,45,18) cell with 3 non-simple vertices), the +z side is short (+1/192 SAME, +1/96 gives `9ff7306e4a6cbf44`), and b holds on [23/48, 49/96] (+1/48 gives `9ff7306e4a6cbf44`). Neighbourhood radius between 1/384 and 1/192 in y; the type holds on a neighbourhood.
- Off-stratum (supplementary) steps leave the special position (stab 2 -> 1) and change the type in every case, as expected for a special-position type; two of the off-stratum cells are NOT stored (general-position types the menu never sampled) and one is the cubic-store type `8c69db9e84095469` (30,45,17).
- Read-only: no perturbed cell and no Schmitt cell computed here was added to `phase2_types.json` (sha256 unchanged); 'not stored' cells are recorded in `collision_phase2_results.json` only.

## Post-screen shortlist

- Survive this screen (all pairs DIFFERENT): #1 `4e9c9b076cfec323`, #2 `49cedbdd58376fac`, #3 `f654982d74d740f6`, #4 `4f6d3e68cbd9e729`, #5 `1497877268495988`, #6 `e0d18e5ea938d649`, #7 `6797ab70c6015039`, #9 `086ac96faf390886`, #10 `164d4bd63d82d0c3`, #11 `5dc2479b9bc14edc`, #12 `3ebbca7ed2eda199`, #13 `7575121042ade3b3`, #14 `213c7a114d5a97a8`, #15 `2e8e49eb28497267`.
- Reframe (SAME TYPE somewhere): #8 `cd4fb52572edcb73`.
- Incomplete / deferred: none.
- Perturbation (top-3): `4e9c9b076cfec323` point OPEN / metric OPEN; `49cedbdd58376fac` point WALL / metric OPEN; `f654982d74d740f6` point OPEN / metric OPEN.

## Honest limits

- This screen is TYPE-level only at Schmitt's 27 printed representatives named in the worklist; every other Schmitt flag in the triage remains f-vector-level (his tables print one point per f-vector). 51 of the 56 printed b-ratios were never swept by our menu (TRIAGE_PHASE2_RESULT.md); a DIFFERENT verdict says nothing about those.
- The digitization is a single visual pass cross-checked against the text layer, NOT independently re-keyed; a G5 verdict that leans on a specific row must first re-read the cited PDF page.
- Setting conversions are the machine-verified ones of PHASE2_SCHMITT_ORIGIN_CHECK.md (every printed row of each group reproduces under them); they are coordinate conversions, not perturbations, and the robustness column shows every alternative documented conversion gives the same code.
- The perturbation certificates cover the top-3 only, at their first witness, with finite steps (down to 1/1536); OPEN here means "holds on the tested neighbourhood", not an interval proof; a WALL side's type is named only where its code is in the store.
- No G4 (roundness / geometric symmetry / Burnside polyform counts / Engel / Bernhard cross-checks) is run here; those remain owed for every survivor.
- Snapshot language throughout: every survivor is "not matched against the catalog snapshot of 2026-09-03".

Wall 15 s, single process. Deterministic except the timing columns.

## Addendum 2026-09-04 (subagent #152, Claude Fable 5.1): store-side rule applied to all 404 menu-sighted tetragonal types

Script: `collision_phase2_tetragonal_storeside.py` (plain python3, wall 1 s). Stores read-only and sha256-verified: `phase2_types.json.gz` decompressed 71685b9ab41b4dc0c2ee1763fdd64f06b41fc51f5a0702d362f137822969f7a3 (raw .json present, sha256 matches); `phase2_hexagonal_types.json.gz` decompressed 7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55. Rows: `schmitt_tetragonal_tables.json` (1476). Output: `collision_phase2_tetragonal_storeside.json` (sorted keys, deterministic; md5 64cc7bb82e85164914d7ec441cfc1304).

**Rule (the hexagonal screen's store-side rule, COLLISION_PHASE2_HEX_RESULTS.md section 1, re-implemented as a pure function):** SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed row with that (group, f) reproduced (P2) as a different stored type; COLLISION = the type reproduces one of his printed cells (S-cell / SAME); UNRESOLVED = a printed row with that (group, f) was not stored (quarantined in the sweep), so no type-level statement is possible for that pair. Rows are matched to stored P2 cells by (group, printed point, b-ratio): exact printed_point_Bpp in the hexagonal store, point mod 1 in the tetragonal store (triage_phase2.py frac_key; the tetragonal store keeps the printed point verbatim in `point`).

- Equivalence assertion (run FIRST, on the 288 menu-sighted hexagonal-first types): {'COLLISION': 124, 'SURVIVOR': 151, 'UNRESOLVED': 13} == the hexagonal screen's {'SURVIVOR': 151, 'COLLISION': 124, 'UNRESOLVED': 13}; per-type verdict equal to TRIAGE_PHASE2_HEX_RESULT.md's full table for all 288; survivor ranking identical. PASS.
- Tetragonal, PURE rule over the 404 menu-sighted types (1215 stored P2 cells keyed by (group, point mod 1, b) as in triage_phase2.py; exact keying would change 0 verdict(s)): COLLISION 176, SURVIVOR 116, UNRESOLVED 112; S-cells 176.
- Overlay (this document's 27 recomputed pairs resolve their rows: SAME -> COLLISION; DIFFERENT on an unstored row -> that row resolved): COLLISION 177, SURVIVOR 121, UNRESOLVED 106.
- Against catalog v3 (15 shortlist statuses + 389 not-screened): COLLISION -> COLLISION: 1; SURVIVOR -> SURVIVOR: 14; not-screened -> COLLISION: 176; not-screened -> SURVIVOR: 107; not-screened -> UNRESOLVED: 106.
- Shortlist consistency: the 15 'Summary per shortlist type' lines above vs the combined status: 0 disagreement(s). The 14 certified survivors are SURVIVOR: True; `cd4fb52572edcb73` stays COLLISION: True.
- Under the PURE rule the certified survivors whose worklist had `unres` rows read UNRESOLVED (their unstored two-origin / second-enantiomorph / IT(80) rows); the recomputation above resolved exactly those rows, which is why the combined status is the catalog's. Every other UNRESOLVED type has an unstored printed row at its (group, f) that no recomputation has touched (listed per type in the JSON) — no verdict is claimed for those pairs.
- LANGUAGE (G5): SURVIVOR = 'not matched against the records checked as of 2026-09-04', never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe).
- No new mathematics: no cell was computed; nothing was added to any store (sha256 unchanged). Digitization caveat as above (single visual pass, text-layer cross-checked, not re-keyed).

## Addendum 2026-09-04 (subagent #154, Claude Fable 5.1): the 62 unstored printed rows recomputed with the documented conventions; the 106 UNRESOLVED tetragonal statuses settled

Script: `collision_phase2_tetragonal_rows_recompute.py` (venv python, single process, wall 43 s). Store `phase2_types.json` read-only, sha256 71685b9ab41b4dc0c2ee1763fdd64f06b41fc51f5a0702d362f137822969f7a3 before and after (= `phase2_types.SHA256SUMS`; .gz decompressed equal). Inputs: `collision_phase2_tetragonal_storeside.json` (md5 64cc7bb82e85164914d7ec441cfc1304; its 106 UNRESOLVED types and their `unstored_rows` = the 62 rows below), `schmitt_tetragonal_tables.json` (row citations; PDF page = printed + 5), `phase2_schmitt_origin_check.json` (conventions). Chain: `sweep_phase2_tetragonal.evaluate` (accepted phase-2 modules; exact order_cycle fallback), certificate asserted per cell. Outputs: `collision_phase2_tetragonal_rows_recomputed.json` (every computed cell: 306 cells over 62 rows; sorted keys; md5 90b8b94b7585e95afa5025f54bd4b941) and `collision_phase2_tetragonal_unresolved_overlay.json` (the 106 verdicts; sorted keys; md5 6d0ee2362e93ea9f8e154f610fd4f289).

**Conventions (PHASE2_SCHMITT_ORIGIN_CHECK.md, each verified on ALL printed rows of its group; `collision_phase2_check.conversions_for` reused verbatim):** two-origin groups: p_ours = p_his + s for every shift s that reproduced all rows (primary = best_shift); second enantiomorphs 95/96: z -> -z primary, the other signed-axis transforms as robustness alternatives; IT(80): printed point verbatim. The OTHER reading (printed point verbatim in our setting for two-origin / 95 / 96 rows = what pass P2 ran and quarantined) was run and recorded per row but never counted. Row status: REPRODUCED = printed f under >= 1 documented convention with one canonical code across the reproducing conventions; else QUARANTINE (f-vectors obtained listed) / AMBIGUOUS. Type verdict (per the 106 UNRESOLVED): any hung-on row SAME -> COLLISION; all hung-on rows REPRODUCED and DIFFERENT -> SURVIVOR; any hung-on row not REPRODUCED and no SAME -> UNRESOLVED.

- Rows: 62 recomputed; status counts {'REPRODUCED': 62}; documented conventions agree on the code in 62/62 rows; the other (verbatim) reading reproduces the printed f in 0/62 rows (expected 0: those runs are exactly the P2 quarantines). Regression: the two rows already recomputed for the shortlist (Q14 IT(86), Q24 IT(80)) give the same codes here.
- Types: the 106 UNRESOLVED -> COLLISION 24, SURVIVOR 82. Tetragonal menu-sighted totals (404): before (v4) COLLISION 177, SURVIVOR 121, UNRESOLVED 106; after COLLISION 201, SURVIVOR 203, UNRESOLVED 0. The 14 certified survivors were never UNRESOLVED and are untouched (asserted); `cd4fb52572edcb73` stays COLLISION.
- Secondary check (a type's code equal to the cell of a row it does NOT hang on): 1 case(s): `5c6382a9ef3bc209` (COLLISION by its hung-on rows) at [[142, '3497/1000', ['58/125', '58/125', '29/250']]]; no status effect
- Row cells that are stored types OUTSIDE the 106 (statuses not changed here): 17 = 15 S-cells already COLLISION / printed-only (expected: an S-cell reproducing one more printed row: IT(95) b=3497/1000 -> `a1c0f033a4e0a342` (printed-only), IT(96) b=7/5 -> `822163f15ffc16d1` (COLLISION), IT(95) b=14/25 -> `d059d2ebab300484` (COLLISION), IT(142) b=3497/1000 -> `8c0bde1b0fee079d` (COLLISION), IT(96) b=7/5 -> `62ca11329dfd99e4` (COLLISION), IT(141) b=3497/1000 -> `2a089105ae08c36d` (COLLISION), IT(88) b=3497/1000 -> `bf5eadab641c997b` (COLLISION), IT(96) b=7/5 -> `5ba951cdd58406f2` (printed-only), IT(95) b=4/5 -> `c8c6299f9321c3cb` (COLLISION), IT(141) b=797/1000 -> `e4200db43401702b` (COLLISION), IT(96) b=7/5 -> `fdecd8c917108d43` (COLLISION), IT(95) b=14/25 -> `6f79177bf480b895` (COLLISION), IT(141) b=797/1000 -> `e956ba4b05a47f01` (COLLISION), IT(96) b=7/5 -> `327ca8d2dd09e1c0` (COLLISION), IT(86) b=3497/1000 -> `1457e9a93eea5438` (COLLISION)) + 2 cubic-first store types (cross-system fact, not-screened by construction: IT(137) b=3497/1000 pt=(1/4, -1/4, 1/4) -> `c1824c64dfbb3615` f (18, 28, 12) p `4^8 6^4` aut 16, IT(95) b=797/1000 pt=(309/500, 59/500, 1/8) -> `8c69db9e84095469` f (30, 45, 17) p `4^6 5^6 6^2 8^3` aut 12) + 0 SURVIVOR types (would contradict v4); row cells stored under no id: 18 (types the menu never sampled; read-only, not added).
- Surprises recorded: 3
  - IT(137) b=3497/1000 pt=(1/4, -1/4, 1/4): row cell = cubic-first store type c1824c64dfbb3615 (f (18, 28, 12), p 4^8 6^4, aut 16): a cubic-store type IS Schmitt's printed representative at this tetragonal row (cross-system fact; cubic-first types are not-screened by the phase-2 screens by construction; recorded only)
  - IT(95) b=797/1000 pt=(309/500, 59/500, 1/8): row cell = cubic-first store type 8c69db9e84095469 (f (30, 45, 17), p 4^6 5^6 6^2 8^3, aut 12): a cubic-store type IS Schmitt's printed representative at this tetragonal row (cross-system fact; cubic-first types are not-screened by the phase-2 screens by construction; recorded only)
  - type 5c6382a9ef3bc209 (COLLISION by its hung-on rows) also equals the recomputed cell of a row it does not hang on (a printed cell of the type in a group where our menu never sighted it): [[142, '3497/1000', ['58/125', '58/125', '29/250']]]; no status effect
- LANGUAGE (G5): SURVIVOR = 'not matched against the records checked as of 2026-09-04', never novelty (Schmitt prints ONE representative per (group, f) from a grid sampling); COLLISION = the type reproduces one of his printed cells (first-realization reframe). Digitization caveat as above (single visual pass, text-layer cross-checked, not re-keyed); every row below cites its PDF page.

### Row-level results (62 rows)

| # | IT | b | printed point | PDF p. (printed) | printed f | status | convention used | point in our setting | f | p | aut | stab | code id / store hit (v4 status) | conv. agree | other reading reproduces f | types hanging | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 130 P4/ncc | 3497/1000 | (52/125, 0, 31/125) | 76 (71) | (22, 34, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 0) | (333/500, 3/4, 31/125) | (22, 34, 14) | `3^4 4^1 5^4 6^4 8^1` | 1 | 1 | `05578fa7044fded7` = stored `05578fa7044fded7` (UNRESOLVED) | YES (4) | False | 1 | 0.8 |
| 2 | 133 P4_2/nbc | 3497/1000 | (56/125, 0, 31/125) | 78 (73) | (34, 51, 19) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (349/500, 3/4, 249/500) | (34, 51, 19) | `3^4 4^8 6^2 8^2 9^2 12^1` | 1 | 1 | `790d421c7d8f507c` (not stored) | YES (4) | False | 1 | 0.6 |
| 3 | 86 P4_2/n | 3497/1000 | (58/125, 0, 29/125) | 40 (35) | (28, 42, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (357/500, 1/4, 241/500) | (28, 42, 16) | `4^8 6^7 10^1` | 2 | 1 | `5be2e092046ee24b` = stored `5be2e092046ee24b` (UNRESOLVED) | YES (4) | False | 5 | 0.4 |
| 4 | 95 P4_322 | 3497/1000 | (37/50, 61/250, 31/250) | 45 (40) | (36, 54, 20) | **REPRODUCED** | second enantiomorph: z -> -z | (37/50, 61/250, -31/250) | (36, 54, 20) | `3^8 4^5 6^1 8^2 10^3 12^1` | 1 | 1 | `a1c0f033a4e0a342` = stored `a1c0f033a4e0a342` (printed-only) | YES (4) | False | 1 | 0.6 |
| 5 | 141 I4_1/amd | 3497/1000 | (1/2, 0, 31/250) | 84 (79) | (21, 32, 13) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 3/4, 249/1000) | (21, 32, 13) | `3^5 4^4 6^1 8^2 11^1` | 2 | 2 | `0d55f30856d2734f` = stored `0d55f30856d2734f` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 6 | 134 P4_2/nnm | 3497/1000 | (62/125, 0, 31/125) | 79 (74) | (18, 27, 11) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (373/500, 3/4, 249/500) | (18, 27, 11) | `3^2 4^5 6^1 7^2 8^1` | 1 | 1 | `0e291742552bfd85` = stored `0e291742552bfd85` (UNRESOLVED) | YES (4) | False | 2 | 0.6 |
| 7 | 96 P4_32_12 | 7/5 | (49/999, -7/999, 61/2664) | 46 (41) | (30, 45, 17) | **REPRODUCED** | second enantiomorph: z -> -z | (49/999, -7/999, -61/2664) | (30, 45, 17) | `3^2 4^5 5^2 6^5 7^2 10^1` | 1 | 1 | `822163f15ffc16d1` = stored `822163f15ffc16d1` (COLLISION) | YES (4) | False | 5 | 0.4 |
| 8 | 138 P4_2/ncm | 3497/1000 | (62/125, 0, 31/125) | 82 (77) | (18, 27, 11) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (373/500, 3/4, 249/500) | (18, 27, 11) | `3^2 4^5 7^4` | 2 | 1 | `15a334b4c643f5b6` = stored `15a334b4c643f5b6` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 9 | 134 P4_2/nnm | 3497/1000 | (58/125, 0, 29/125) | 78 (73) | (16, 24, 10) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (357/500, 3/4, 241/500) | (16, 24, 10) | `3^3 4^1 5^2 6^3 7^1` | 1 | 1 | `1811b0d16d82bdda` = stored `1811b0d16d82bdda` (UNRESOLVED) | YES (4) | False | 1 | 0.6 |
| 10 | 138 P4_2/ncm | 3497/1000 | (58/125, 0, 29/125) | 81 (76) | (16, 24, 10) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (357/500, 3/4, 241/500) | (16, 24, 10) | `3^3 4^1 5^2 6^3 7^1` | 1 | 1 | `1811b0d16d82bdda` = stored `1811b0d16d82bdda` (UNRESOLVED) | YES (4) | False | 2 | 0.4 |
| 11 | 95 P4_322 | 14/25 | (7/333, -2/999, 61/2664) | 45 (40) | (31, 47, 18) | **REPRODUCED** | second enantiomorph: z -> -z | (7/333, -2/999, -61/2664) | (31, 47, 18) | `3^4 4^6 6^4 7^2 8^1 12^1` | 1 | 1 | `d059d2ebab300484` = stored `d059d2ebab300484` (COLLISION) | YES (4) | False | 1 | 0.7 |
| 12 | 80 I4_1 | 3497/1000 | (353/1413, 235/942, 0) | 35 (30) | (32, 48, 18) | **REPRODUCED** | none (printed point verbatim) | (353/1413, 235/942, 0) | (32, 48, 18) | `3^4 4^6 5^2 6^1 8^2 9^2 10^1` | 1 | 1 | `19c7c8de77b6ce20` = stored `19c7c8de77b6ce20` (UNRESOLVED) | YES (1) | False | 4 | 0.1 |
| 13 | 88 I4_1/a | 3497/1000 | (11/25, 11/25, 11/100) | 42 (37) | (30, 45, 17) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (11/25, 69/100, 47/200) | (30, 45, 17) | `3^2 4^7 6^3 7^2 8^3` | 1 | 1 | `1dcbbedea6d41f23` (not stored) | YES (4) | False | 4 | 0.6 |
| 14 | 88 I4_1/a | 3497/1000 | (62/125, 62/125, 31/250) | 42 (37) | (34, 51, 19) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (62/125, 373/500, 249/1000) | (34, 51, 19) | `3^6 4^3 5^2 6^2 8^5 10^1` | 1 | 1 | `9f7f5010b17cc9db` (not stored) | YES (4) | False | 4 | 0.8 |
| 15 | 88 I4_1/a | 3497/1000 | (21/50, 21/50, 21/200) | 42 (37) | (26, 39, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (21/50, 67/100, 23/100) | (26, 39, 15) | `4^5 5^4 6^4 7^2` | 1 | 1 | `503375aa4e8d2f36` (not stored) | YES (4) | False | 5 | 0.7 |
| 16 | 142 I4_1/acd | 3497/1000 | (58/125, 58/125, 29/250) | 86 (81) | (30, 45, 17) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (58/125, 607/500, 241/1000) | (30, 45, 17) | `3^2 4^9 6^2 8^2 10^2` | 2 | 1 | `5c6382a9ef3bc209` = stored `5c6382a9ef3bc209` (UNRESOLVED) | YES (4) | False | 5 | 1.3 |
| 17 | 142 I4_1/acd | 7/2 | (57/125, 38/125, 4/125) | 86 (81) | (23, 36, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (57/125, 527/500, 157/1000) | (23, 36, 15) | `3^2 4^7 6^5 8^1` | 1 | 1 | `e9bac39d5a13cba7` (not stored) | YES (4) | False | 1 | 1.1 |
| 18 | 138 P4_2/ncm | 797/1000 | (123/250, 0, 1/500) | 82 (77) | (20, 30, 12) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (371/500, 3/4, 63/250) | (20, 30, 12) | `3^3 4^2 5^3 7^4` | 1 | 1 | `230e451f710229a7` = stored `230e451f710229a7` (UNRESOLVED) | YES (4) | False | 1 | 0.6 |
| 19 | 142 I4_1/acd | 3497/1000 | (33/250, 33/250, 31/250) | 86 (81) | (32, 48, 18) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (33/250, 441/500, 249/1000) | (32, 48, 18) | `3^2 4^8 5^2 6^1 7^2 8^2 12^1` | 1 | 1 | `8c0bde1b0fee079d` = stored `8c0bde1b0fee079d` (COLLISION) | YES (4) | False | 2 | 1.4 |
| 20 | 96 P4_32_12 | 7/5 | (133/1998, 91/1998, 61/2664) | 46 (41) | (28, 42, 16) | **REPRODUCED** | second enantiomorph: z -> -z | (133/1998, 91/1998, -61/2664) | (28, 42, 16) | `3^2 4^4 5^4 6^3 8^3` | 1 | 1 | `62ca11329dfd99e4` = stored `62ca11329dfd99e4` (COLLISION) | YES (4) | False | 3 | 0.4 |
| 21 | 141 I4_1/amd | 797/1000 | (97/250, 97/250, 97/1000) | 84 (79) | (24, 36, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (97/250, 569/500, 111/500) | (24, 36, 14) | `3^4 4^4 5^2 6^1 7^1 10^1 11^1` | 1 | 1 | `0ecfae17ab770551` (not stored) | YES (4) | False | 1 | 1.1 |
| 22 | 141 I4_1/amd | 3497/1000 | (62/125, 62/125, 31/250) | 84 (79) | (14, 21, 9) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (62/125, 623/500, 249/1000) | (14, 21, 9) | `3^3 4^2 5^2 7^1 8^1` | 2 | 1 | `2a089105ae08c36d` = stored `2a089105ae08c36d` (COLLISION) | YES (4) | False | 2 | 0.9 |
| 23 | 86 P4_2/n | 3497/1000 | (59/125, 0, 31/125) | 40 (35) | (30, 45, 17) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (361/500, 1/4, 249/500) | (30, 45, 17) | `3^4 4^3 6^7 7^2 10^1` | 1 | 1 | `ee2ed254a2e46a56` (not stored) | YES (4) | False | 1 | 0.5 |
| 24 | 137 P4_2/nmc | 3497/1000 | (1/4, -1/4, 1/4) | 81 (76) | (18, 28, 12) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (1/2, 1/2, 1/2) | (18, 28, 12) | `4^8 6^4` | 16 | 8 | `c1824c64dfbb3615` = stored `c1824c64dfbb3615` (cubic-first) | YES (4) | False | 1 | 0.1 |
| 25 | 126 P4/nnc | 3497/1000 | (59/125, 0, 1/500) | 73 (68) | (20, 31, 13) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (361/500, 1/4, 63/250) | (20, 31, 13) | `4^7 5^2 6^4` | 1 | 1 | `32b4d3d2ab4957a6` = stored `32b4d3d2ab4957a6` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 26 | 88 I4_1/a | 3497/1000 | (3/250, 3/250, 3/1000) | 42 (37) | (28, 42, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (3/250, 131/500, 16/125) | (28, 42, 16) | `3^4 4^2 5^2 6^4 7^2 8^2` | 1 | 1 | `bf5eadab641c997b` = stored `bf5eadab641c997b` (COLLISION) | YES (4) | False | 3 | 0.8 |
| 27 | 96 P4_32_12 | 7/5 | (85/1998, -29/1998, 61/2664) | 47 (42) | (34, 51, 19) | **REPRODUCED** | second enantiomorph: z -> -z | (85/1998, -29/1998, -61/2664) | (34, 51, 19) | `3^4 4^5 5^2 6^4 8^3 12^1` | 1 | 1 | `5ba951cdd58406f2` = stored `5ba951cdd58406f2` (printed-only) | YES (4) | False | 2 | 0.4 |
| 28 | 142 I4_1/acd | 3497/1000 | (93/250, 93/250, 93/1000) | 86 (81) | (28, 42, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (93/250, 561/500, 109/500) | (28, 42, 16) | `3^4 4^3 5^2 6^3 7^2 8^1 10^1` | 1 | 1 | `d167fc392cd667a6` = stored `d167fc392cd667a6` (UNRESOLVED) | YES (4) | False | 7 | 1.2 |
| 29 | 141 I4_1/amd | 4/5 | (1/5, 2/125, 1/20) | 83 (78) | (10, 16, 8) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/5, 383/500, 7/40) | (10, 16, 8) | `3^4 4^2 6^2` | 2 | 1 | `ba5c53fa257d38ee` (not stored) | YES (4) | False | 1 | 0.9 |
| 30 | 133 P4_2/nbc | 3497/1000 | (59/125, 0, 31/125) | 78 (73) | (28, 42, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (361/500, 3/4, 249/500) | (28, 42, 16) | `3^2 4^7 6^2 7^2 8^3` | 1 | 1 | `8ac4f8b1c6ca250e` = stored `8ac4f8b1c6ca250e` (UNRESOLVED) | YES (4) | False | 2 | 0.7 |
| 31 | 133 P4_2/nbc | 3497/1000 | (103/250, 0, 31/125) | 78 (73) | (30, 45, 17) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (331/500, 3/4, 249/500) | (30, 45, 17) | `3^2 4^9 6^2 8^2 10^2` | 2 | 1 | `5c6382a9ef3bc209` = stored `5c6382a9ef3bc209` (UNRESOLVED) | YES (4) | False | 2 | 0.6 |
| 32 | 95 P4_322 | 4/5 | (1997/3996, 1075/3996, 5/7992) | 45 (40) | (28, 42, 16) | **REPRODUCED** | second enantiomorph: z -> -z | (1997/3996, 1075/3996, -5/7992) | (28, 42, 16) | `4^8 6^6 8^2` | 2 | 1 | `c8c6299f9321c3cb` = stored `c8c6299f9321c3cb` (COLLISION) | YES (4) | False | 1 | 0.5 |
| 33 | 141 I4_1/amd | 797/1000 | (0, 0, 0) | 84 (79) | (28, 42, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (0, 3/4, 1/8) | (28, 42, 16) | `3^4 4^4 6^4 8^4` | 8 | 4 | `e4200db43401702b` = stored `e4200db43401702b` (COLLISION) | YES (4) | False | 1 | 0.3 |
| 34 | 86 P4_2/n | 3497/1000 | (12/25, 0, 6/25) | 40 (35) | (32, 48, 18) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (73/100, 1/4, 49/100) | (32, 48, 18) | `3^2 4^8 5^2 6^1 7^2 8^2 12^1` | 1 | 1 | `b4ff381c9014f14c` (not stored) | YES (4) | False | 7 | 0.4 |
| 35 | 141 I4_1/amd | 797/1000 | (1/2, 0, 31/250) | 84 (79) | (23, 35, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 3/4, 249/1000) | (23, 35, 14) | `3^1 4^3 5^5 6^5` | 2 | 2 | `686f3af67d8e9d60` = stored `686f3af67d8e9d60` (UNRESOLVED) | YES (4) | False | 1 | 0.6 |
| 36 | 142 I4_1/acd | 797/1000 | (23/50, 23/50, 23/200) | 86 (81) | (26, 39, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (23/50, 121/100, 6/25) | (26, 39, 15) | `4^7 6^7 8^1` | 2 | 1 | `b96cf29a9246cd2c` = stored `b96cf29a9246cd2c` (UNRESOLVED) | YES (4) | False | 3 | 1.2 |
| 37 | 133 P4_2/nbc | 3497/1000 | (62/125, 0, 31/125) | 78 (73) | (24, 36, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (373/500, 3/4, 249/500) | (24, 36, 14) | `4^3 5^6 6^5` | 1 | 1 | `74076f8341f71199` = stored `74076f8341f71199` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 38 | 142 I4_1/acd | 3497/1000 | (109/250, 109/250, 109/1000) | 86 (81) | (24, 36, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (109/250, 593/500, 117/500) | (24, 36, 14) | `4^3 5^6 6^5` | 1 | 1 | `74076f8341f71199` = stored `74076f8341f71199` (UNRESOLVED) | YES (4) | False | 1 | 1.3 |
| 39 | 137 P4_2/nmc | 3497/1000 | (141/500, -107/500, 17/500) | 81 (76) | (14, 21, 9) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (133/250, 67/125, 71/250) | (14, 21, 9) | `3^3 4^2 5^1 6^2 8^1` | 1 | 1 | `7bde4c1d5a885234` = stored `7bde4c1d5a885234` (UNRESOLVED) | YES (4) | False | 1 | 0.4 |
| 40 | 88 I4_1/a | 3497/1000 | (1/250, 1/250, 61/500) | 42 (37) | (38, 57, 21) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (1/250, 127/500, 247/1000) | (38, 57, 21) | `3^4 4^8 6^3 7^2 8^1 9^2 12^1` | 1 | 1 | `15b43127f72b56e7` (not stored) | YES (4) | False | 1 | 0.9 |
| 41 | 141 I4_1/amd | 4/5 | (1/2, 19/50, 1/8) | 84 (79) | (15, 25, 12) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 113/100, 1/4) | (15, 25, 12) | `4^10 5^2` | 2 | 2 | `03d1f56619ac3f4a` (not stored) | YES (4) | False | 1 | 0.4 |
| 42 | 134 P4_2/nnm | 797/1000 | (42/125, 0, 31/125) | 79 (74) | (22, 33, 13) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 1/4) | (293/500, 3/4, 249/500) | (22, 33, 13) | `3^3 4^5 5^1 6^1 7^1 9^1 10^1` | 1 | 1 | `82b129fb96de7dae` = stored `82b129fb96de7dae` (UNRESOLVED) | YES (4) | False | 1 | 0.6 |
| 43 | 142 I4_1/acd | 3497/1000 | (62/125, 62/125, 31/250) | 86 (81) | (34, 51, 19) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (62/125, 623/500, 249/1000) | (34, 51, 19) | `3^8 4^1 5^2 6^4 8^2 12^2` | 1 | 1 | `70be474815baf42b` (not stored) | YES (4) | False | 2 | 1.4 |
| 44 | 141 I4_1/amd | 4/5 | (47/125, 7/125, 2/25) | 84 (79) | (18, 28, 12) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (47/125, 403/500, 41/200) | (18, 28, 12) | `3^6 4^1 5^1 6^2 8^1 9^1` | 1 | 1 | `771186009d020142` (not stored) | YES (4) | False | 2 | 1.0 |
| 45 | 86 P4_2/n | 3497/1000 | (79/250, 0, 119/500) | 40 (35) | (34, 51, 19) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (283/500, 1/4, 61/125) | (34, 51, 19) | `3^8 5^4 6^2 7^2 8^1 12^2` | 1 | 1 | `8b96d46626c486fe` = stored `8b96d46626c486fe` (UNRESOLVED) | YES (4) | False | 1 | 0.4 |
| 46 | 96 P4_32_12 | 7/5 | (73/999, 22/333, 61/2664) | 47 (42) | (36, 54, 20) | **REPRODUCED** | second enantiomorph: z -> -z | (73/999, 22/333, -61/2664) | (36, 54, 20) | `3^8 4^4 5^2 8^1 9^2 10^2 12^1` | 1 | 1 | `fdecd8c917108d43` = stored `fdecd8c917108d43` (COLLISION) | YES (4) | False | 1 | 0.6 |
| 47 | 141 I4_1/amd | 797/1000 | (1/2, 19/50, 1/8) | 84 (79) | (20, 32, 14) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 113/100, 1/4) | (20, 32, 14) | `3^2 4^8 6^2 7^2` | 2 | 2 | `925e5163e8cf6e42` = stored `925e5163e8cf6e42` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 48 | 141 I4_1/amd | 299/250 | (1/2, 62/125, 1/500) | 84 (79) | (23, 36, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 623/500, 127/1000) | (23, 36, 15) | `3^4 4^6 5^1 7^3 10^1` | 2 | 2 | `974ed1256562acc3` = stored `974ed1256562acc3` (UNRESOLVED) | YES (4) | False | 1 | 0.7 |
| 49 | 95 P4_322 | 14/25 | (677/1332, 347/1332, 263/7992) | 45 (40) | (34, 51, 19) | **REPRODUCED** | second enantiomorph: z -> -z | (677/1332, 347/1332, -263/7992) | (34, 51, 19) | `3^4 4^5 6^7 8^1 10^2` | 1 | 1 | `6f79177bf480b895` = stored `6f79177bf480b895` (COLLISION) | YES (4) | False | 1 | 0.5 |
| 50 | 141 I4_1/amd | 797/1000 | (0, 0, 1/8) | 84 (79) | (20, 31, 13) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (0, 3/4, 1/4) | (20, 31, 13) | `4^5 5^6 6^2` | 2 | 2 | `e956ba4b05a47f01` = stored `e956ba4b05a47f01` (COLLISION) | YES (4) | False | 1 | 0.6 |
| 51 | 96 P4_32_12 | 7/5 | (46/999, -16/999, 61/2664) | 46 (41) | (26, 39, 15) | **REPRODUCED** | second enantiomorph: z -> -z | (46/999, -16/999, -61/2664) | (26, 39, 15) | `3^2 4^2 5^4 6^6 8^1` | 2 | 1 | `327ca8d2dd09e1c0` = stored `327ca8d2dd09e1c0` (COLLISION) | YES (4) | False | 1 | 0.4 |
| 52 | 141 I4_1/amd | 797/1000 | (1/2, 2/5, 1/10) | 84 (79) | (34, 51, 19) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 23/20, 9/40) | (34, 51, 19) | `4^12 6^3 8^3 12^1` | 2 | 2 | `2ab69895d37a722a` (not stored) | YES (4) | False | 1 | 0.8 |
| 53 | 142 I4_1/acd | 3497/1000 | (13/50, 13/50, 31/250) | 86 (81) | (36, 54, 20) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (13/50, 101/100, 249/1000) | (36, 54, 20) | `3^8 4^1 5^2 6^5 8^2 10^1 14^1` | 1 | 1 | `c4788e9cca25e7d2` (not stored) | YES (4) | False | 1 | 1.5 |
| 54 | 141 I4_1/amd | 797/1000 | (26/125, 26/125, 1/8) | 84 (79) | (16, 24, 10) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (26/125, 479/500, 1/4) | (16, 24, 10) | `3^1 4^4 5^1 6^4` | 2 | 1 | `d0db3b3d60ce68a2` = stored `d0db3b3d60ce68a2` (UNRESOLVED) | YES (4) | False | 1 | 0.9 |
| 55 | 141 I4_1/amd | 5/4 | (1/2, 7/25, 7/100) | 84 (79) | (16, 26, 12) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (1/2, 103/100, 39/200) | (16, 26, 12) | `3^2 4^8 6^1 8^1` | 2 | 2 | `1cdcaee40c97428f` (not stored) | YES (4) | False | 1 | 0.5 |
| 56 | 126 P4/nnc | 3497/1000 | (56/125, 0, 1/250) | 73 (68) | (24, 37, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (349/500, 1/4, 127/500) | (24, 37, 15) | `3^2 4^5 5^2 6^5 8^1` | 1 | 1 | `d70cf5c792428eab` = stored `d70cf5c792428eab` (UNRESOLVED) | YES (4) | False | 1 | 0.7 |
| 57 | 130 P4/ncc | 3497/1000 | (59/125, 0, 1/500) | 76 (71) | (20, 31, 13) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 0) | (361/500, 3/4, 1/500) | (20, 31, 13) | `4^7 5^2 6^4` | 1 | 1 | `d84f3b8159a92b4b` = stored `d84f3b8159a92b4b` (UNRESOLVED) | YES (4) | False | 1 | 0.5 |
| 58 | 130 P4/ncc | 3497/1000 | (59/125, 0, 31/125) | 76 (71) | (26, 40, 16) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 3/4, 0) | (361/500, 3/4, 31/125) | (26, 40, 16) | `3^4 4^5 5^2 6^1 7^2 8^1 10^1` | 1 | 1 | `db9ffdbe1d267b0a` = stored `db9ffdbe1d267b0a` (UNRESOLVED) | YES (4) | False | 1 | 0.7 |
| 59 | 88 I4_1/a | 3497/1000 | (62/125, 123/250, 0) | 42 (37) | (32, 48, 18) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 1/4, 1/8) | (62/125, 371/500, 1/8) | (32, 48, 18) | `3^4 4^4 5^4 6^2 8^2 10^2` | 2 | 1 | `89f6df138c88edf8` (not stored) | YES (4) | False | 1 | 0.8 |
| 60 | 95 P4_322 | 797/1000 | (309/500, 59/500, 1/8) | 45 (40) | (30, 45, 17) | **REPRODUCED** | second enantiomorph: z -> -z | (309/500, 59/500, -1/8) | (30, 45, 17) | `4^6 5^6 6^2 8^3` | 12 | 1 | `8c69db9e84095469` = stored `8c69db9e84095469` (cubic-first) | YES (4) | False | 1 | 0.4 |
| 61 | 86 P4_2/n | 3497/1000 | (117/250, 0, 31/125) | 40 (35) | (26, 39, 15) | **REPRODUCED** | origin-2 -> origin-1 shift +(1/4, 1/4, 1/4) | (359/500, 1/4, 249/500) | (26, 39, 15) | `4^5 5^4 6^5 8^1` | 2 | 1 | `1457e9a93eea5438` = stored `1457e9a93eea5438` (COLLISION) | YES (4) | False | 1 | 0.3 |
| 62 | 141 I4_1/amd | 797/1000 | (62/125, 69/250, 121/1000) | 84 (79) | (30, 45, 17) | **REPRODUCED** | origin-2 -> origin-1 shift +(0, 3/4, 1/8) | (62/125, 513/500, 123/500) | (30, 45, 17) | `3^7 4^3 5^1 6^3 7^1 13^1 14^1` | 1 | 1 | `318f50f8f38fd957` (not stored) | YES (4) | False | 1 | 1.3 |

### Type-level verdicts (106 types)

| type | f | groups sighted | rows hung on: IT b -> verdict (row cell id) | verdict |
|---|---|---|---|---|
| `05578fa7044fded7` | (22, 34, 14) | [130] | IT130 3497/1000 -> SAME TYPE (`05578fa7044fded7`) | **COLLISION** |
| `05f9eab1c6915aef` | (34, 51, 19) | [133] | IT133 3497/1000 -> DIFFERENT TYPE (`790d421c7d8f507c`) | **SURVIVOR** |
| `0882fd4b5b8cb62e` | (28, 42, 16) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`5be2e092046ee24b`) | **SURVIVOR** |
| `0b6473b240a3c9e9` | (36, 54, 20) | [95] | IT95 3497/1000 -> DIFFERENT TYPE (`a1c0f033a4e0a342`) | **SURVIVOR** |
| `0d55f30856d2734f` | (21, 32, 13) | [141] | IT141 3497/1000 -> SAME TYPE (`0d55f30856d2734f`) | **COLLISION** |
| `0e291742552bfd85` | (18, 27, 11) | [134] | IT134 3497/1000 -> SAME TYPE (`0e291742552bfd85`) | **COLLISION** |
| `10f9a0d8ff07b3e4` | (30, 45, 17) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`822163f15ffc16d1`) | **SURVIVOR** |
| `15a334b4c643f5b6` | (18, 27, 11) | [138] | IT138 3497/1000 -> SAME TYPE (`15a334b4c643f5b6`) | **COLLISION** |
| `1811b0d16d82bdda` | (16, 24, 10) | [134, 138] | IT134 3497/1000 -> SAME TYPE (`1811b0d16d82bdda`); IT138 3497/1000 -> SAME TYPE (`1811b0d16d82bdda`) | **COLLISION** |
| `18b35afa85c5a929` | (31, 47, 18) | [95] | IT95 14/25 -> DIFFERENT TYPE (`d059d2ebab300484`) | **SURVIVOR** |
| `19c7c8de77b6ce20` | (32, 48, 18) | [80] | IT80 3497/1000 -> SAME TYPE (`19c7c8de77b6ce20`) | **COLLISION** |
| `1a1a0de250f0da27` | (30, 45, 17) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`1dcbbedea6d41f23`) | **SURVIVOR** |
| `1a1c3bd1605b8d49` | (34, 51, 19) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`9f7f5010b17cc9db`) | **SURVIVOR** |
| `1b269a7a84560401` | (26, 39, 15) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`503375aa4e8d2f36`) | **SURVIVOR** |
| `1c45cdaed191693e` | (34, 51, 19) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`9f7f5010b17cc9db`) | **SURVIVOR** |
| `1f2332434c9e64b8` | (30, 45, 17) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `1fcd5245be090d59` | (23, 36, 15) | [142] | IT142 7/2 -> DIFFERENT TYPE (`e9bac39d5a13cba7`) | **SURVIVOR** |
| `2204c0ceea51430d` | (28, 42, 16) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`5be2e092046ee24b`) | **SURVIVOR** |
| `230e451f710229a7` | (20, 30, 12) | [138] | IT138 797/1000 -> SAME TYPE (`230e451f710229a7`) | **COLLISION** |
| `26a8212cbd6c8b62` | (30, 45, 17) | [96] | IT96 7/5 -> DIFFERENT TYPE (`822163f15ffc16d1`) | **SURVIVOR** |
| `278f5cc0bdb53b51` | (32, 48, 18) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`8c0bde1b0fee079d`) | **SURVIVOR** |
| `29f80b9c127f79a9` | (28, 42, 16) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`62ca11329dfd99e4`) | **SURVIVOR** |
| `2a3cf777c624752c` | (24, 36, 14) | [141] | IT141 797/1000 -> DIFFERENT TYPE (`0ecfae17ab770551`) | **SURVIVOR** |
| `2ae9d568eb9bfb4c` | (14, 21, 9) | [141] | IT141 3497/1000 -> DIFFERENT TYPE (`2a089105ae08c36d`) | **SURVIVOR** |
| `32451695e287120d` | (30, 45, 17) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`ee2ed254a2e46a56`) | **SURVIVOR** |
| `32810102c8039911` | (18, 28, 12) | [137] | IT137 3497/1000 -> DIFFERENT TYPE (`c1824c64dfbb3615`) | **SURVIVOR** |
| `32b4d3d2ab4957a6` | (20, 31, 13) | [126] | IT126 3497/1000 -> SAME TYPE (`32b4d3d2ab4957a6`) | **COLLISION** |
| `343d241f8d586edb` | (28, 42, 16) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`bf5eadab641c997b`) | **SURVIVOR** |
| `35398c494f7e95b0` | (34, 51, 19) | [96] | IT96 7/5 -> DIFFERENT TYPE (`5ba951cdd58406f2`) | **SURVIVOR** |
| `3c177440d8084cb5` | (18, 27, 11) | [134] | IT134 3497/1000 -> DIFFERENT TYPE (`0e291742552bfd85`) | **SURVIVOR** |
| `42f6d76b9fc019fd` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `4e702e95c290afbd` | (34, 51, 19) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`9f7f5010b17cc9db`) | **SURVIVOR** |
| `519d875aa973e258` | (10, 16, 8) | [141] | IT141 4/5 -> DIFFERENT TYPE (`ba5c53fa257d38ee`) | **SURVIVOR** |
| `5561cb5efa0a7c0c` | (28, 42, 16) | [96] | IT96 7/5 -> DIFFERENT TYPE (`62ca11329dfd99e4`) | **SURVIVOR** |
| `5a7de3df1296531a` | (28, 42, 16) | [133] | IT133 3497/1000 -> DIFFERENT TYPE (`8ac4f8b1c6ca250e`) | **SURVIVOR** |
| `5ae136b2bdd40066` | (28, 42, 16) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`5be2e092046ee24b`) | **SURVIVOR** |
| `5be2e092046ee24b` | (28, 42, 16) | [86, 92, 96, 122] | IT86 3497/1000 -> SAME TYPE (`5be2e092046ee24b`); IT96 7/5 -> DIFFERENT TYPE (`62ca11329dfd99e4`) | **COLLISION** |
| `5c6382a9ef3bc209` | (30, 45, 17) | [133] | IT133 3497/1000 -> SAME TYPE (`5c6382a9ef3bc209`) | **COLLISION** |
| `5ebc1b8c073a87a9` | (28, 42, 16) | [88, 95, 98, 122, 141] | IT88 3497/1000 -> DIFFERENT TYPE (`bf5eadab641c997b`); IT95 4/5 -> DIFFERENT TYPE (`c8c6299f9321c3cb`); IT141 797/1000 -> DIFFERENT TYPE (`e4200db43401702b`) | **SURVIVOR** |
| `5f2e35e62d0aa64d` | (32, 48, 18) | [80] | IT80 3497/1000 -> DIFFERENT TYPE (`19c7c8de77b6ce20`) | **SURVIVOR** |
| `675cc4f2c640cd11` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `686f3af67d8e9d60` | (23, 35, 14) | [141] | IT141 797/1000 -> SAME TYPE (`686f3af67d8e9d60`) | **COLLISION** |
| `6eb2bc88106b9dcd` | (26, 39, 15) | [142] | IT142 797/1000 -> DIFFERENT TYPE (`b96cf29a9246cd2c`) | **SURVIVOR** |
| `72d03fdd4ab546d7` | (30, 45, 17) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `74076f8341f71199` | (24, 36, 14) | [88, 133, 142] | IT133 3497/1000 -> SAME TYPE (`74076f8341f71199`); IT142 3497/1000 -> SAME TYPE (`74076f8341f71199`) | **COLLISION** |
| `74b20b492f403316` | (26, 39, 15) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`503375aa4e8d2f36`) | **SURVIVOR** |
| `799b17ae5c44c23a` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `7bde4c1d5a885234` | (14, 21, 9) | [137, 141] | IT137 3497/1000 -> SAME TYPE (`7bde4c1d5a885234`); IT141 3497/1000 -> DIFFERENT TYPE (`2a089105ae08c36d`) | **COLLISION** |
| `804dd9fb0c1a57ca` | (38, 57, 21) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`15b43127f72b56e7`) | **SURVIVOR** |
| `818521767ac611bd` | (15, 25, 12) | [141] | IT141 4/5 -> DIFFERENT TYPE (`03d1f56619ac3f4a`) | **SURVIVOR** |
| `81d176073d947bda` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `82b129fb96de7dae` | (22, 33, 13) | [134] | IT134 797/1000 -> SAME TYPE (`82b129fb96de7dae`) | **COLLISION** |
| `8357998c809f5d36` | (28, 42, 16) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`bf5eadab641c997b`) | **SURVIVOR** |
| `841ca21dc8f5c770` | (32, 48, 18) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`8c0bde1b0fee079d`) | **SURVIVOR** |
| `8a3d9b4f9a849029` | (34, 51, 19) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`70be474815baf42b`) | **SURVIVOR** |
| `8ac4f8b1c6ca250e` | (28, 42, 16) | [133] | IT133 3497/1000 -> SAME TYPE (`8ac4f8b1c6ca250e`) | **COLLISION** |
| `8b7f38eb72520356` | (18, 28, 12) | [141] | IT141 4/5 -> DIFFERENT TYPE (`771186009d020142`) | **SURVIVOR** |
| `8b96d46626c486fe` | (34, 51, 19) | [86] | IT86 3497/1000 -> SAME TYPE (`8b96d46626c486fe`) | **COLLISION** |
| `8b991972fb6aab30` | (36, 54, 20) | [96] | IT96 7/5 -> DIFFERENT TYPE (`fdecd8c917108d43`) | **SURVIVOR** |
| `8dce1cb5e78590f9` | (30, 45, 17) | [96] | IT96 7/5 -> DIFFERENT TYPE (`822163f15ffc16d1`) | **SURVIVOR** |
| `8fc19c6bf41cc1fd` | (32, 48, 18) | [80] | IT80 3497/1000 -> DIFFERENT TYPE (`19c7c8de77b6ce20`) | **SURVIVOR** |
| `8fc980b921be3244` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `900973c9cdd62294` | (34, 51, 19) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`9f7f5010b17cc9db`) | **SURVIVOR** |
| `925e5163e8cf6e42` | (20, 32, 14) | [141] | IT141 797/1000 -> SAME TYPE (`925e5163e8cf6e42`) | **COLLISION** |
| `94a19a39b99e1366` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `96c135294ff83fe2` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `974ed1256562acc3` | (23, 36, 15) | [141] | IT141 299/250 -> SAME TYPE (`974ed1256562acc3`) | **COLLISION** |
| `9aa9148ffc66fe2e` | (32, 48, 18) | [80] | IT80 3497/1000 -> DIFFERENT TYPE (`19c7c8de77b6ce20`) | **SURVIVOR** |
| `9b708cb2bde13500` | (34, 51, 19) | [95] | IT95 14/25 -> DIFFERENT TYPE (`6f79177bf480b895`) | **SURVIVOR** |
| `9ccf2947d0051c0c` | (20, 31, 13) | [141] | IT141 797/1000 -> DIFFERENT TYPE (`e956ba4b05a47f01`) | **SURVIVOR** |
| `9dd29764e82d4595` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `9ed821a3c69a01f6` | (30, 45, 17) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`822163f15ffc16d1`) | **SURVIVOR** |
| `9f3af33a5a619342` | (26, 39, 15) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`327ca8d2dd09e1c0`) | **SURVIVOR** |
| `9ff7306e4a6cbf44` | (34, 51, 19) | [141] | IT141 797/1000 -> DIFFERENT TYPE (`2ab69895d37a722a`) | **SURVIVOR** |
| `a0be76769745bbaf` | (30, 45, 17) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `acb8eed6b8a82612` | (36, 54, 20) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`c4788e9cca25e7d2`) | **SURVIVOR** |
| `b1355d63057fb8b6` | (30, 45, 17) | [88, 110, 142] | IT88 3497/1000 -> DIFFERENT TYPE (`1dcbbedea6d41f23`); IT142 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `b504635d2b404e93` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `b77e98e2c4a01aad` | (30, 45, 17) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`1dcbbedea6d41f23`) | **SURVIVOR** |
| `b96cf29a9246cd2c` | (26, 39, 15) | [142] | IT142 797/1000 -> SAME TYPE (`b96cf29a9246cd2c`) | **COLLISION** |
| `c64d7a44fc7eafce` | (30, 45, 17) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`1dcbbedea6d41f23`) | **SURVIVOR** |
| `cc1e165a04008058` | (30, 45, 17) | [133] | IT133 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `cde6f488fa3b5e98` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `d0db3b3d60ce68a2` | (16, 24, 10) | [141] | IT141 797/1000 -> SAME TYPE (`d0db3b3d60ce68a2`) | **COLLISION** |
| `d167fc392cd667a6` | (28, 42, 16) | [142] | IT142 3497/1000 -> SAME TYPE (`d167fc392cd667a6`) | **COLLISION** |
| `d1c13a36caa38829` | (16, 26, 12) | [141] | IT141 5/4 -> DIFFERENT TYPE (`1cdcaee40c97428f`) | **SURVIVOR** |
| `d25aa9f2dff2be4e` | (34, 51, 19) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`70be474815baf42b`) | **SURVIVOR** |
| `d25e09a426bd8ecf` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `d70cf5c792428eab` | (24, 37, 15) | [126] | IT126 3497/1000 -> SAME TYPE (`d70cf5c792428eab`) | **COLLISION** |
| `d84f3b8159a92b4b` | (20, 31, 13) | [130] | IT130 3497/1000 -> SAME TYPE (`d84f3b8159a92b4b`) | **COLLISION** |
| `db0320ad071ab1eb` | (34, 51, 19) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`5ba951cdd58406f2`) | **SURVIVOR** |
| `db9ffdbe1d267b0a` | (26, 40, 16) | [130] | IT130 3497/1000 -> SAME TYPE (`db9ffdbe1d267b0a`) | **COLLISION** |
| `dfe1108b777824fa` | (26, 39, 15) | [88, 142] | IT88 3497/1000 -> DIFFERENT TYPE (`503375aa4e8d2f36`); IT142 797/1000 -> DIFFERENT TYPE (`b96cf29a9246cd2c`) | **SURVIVOR** |
| `e127689d5833b02a` | (16, 24, 10) | [138] | IT138 3497/1000 -> DIFFERENT TYPE (`1811b0d16d82bdda`) | **SURVIVOR** |
| `e23ad48c69ddca62` | (32, 48, 18) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`89f6df138c88edf8`) | **SURVIVOR** |
| `e64ff7d1f133b6c9` | (30, 45, 17) | [91, 95] | IT95 797/1000 -> DIFFERENT TYPE (`8c69db9e84095469`) | **SURVIVOR** |
| `e73ddea1cde2be65` | (26, 39, 15) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`1457e9a93eea5438`) | **SURVIVOR** |
| `e969c24510c5b82b` | (32, 48, 18) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`b4ff381c9014f14c`) | **SURVIVOR** |
| `eab762a24b28a094` | (26, 39, 15) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`503375aa4e8d2f36`) | **SURVIVOR** |
| `eaf8f8e7b00c0da0` | (26, 39, 15) | [88] | IT88 3497/1000 -> DIFFERENT TYPE (`503375aa4e8d2f36`) | **SURVIVOR** |
| `ec59577573c34683` | (30, 45, 17) | [141] | IT141 797/1000 -> DIFFERENT TYPE (`318f50f8f38fd957`) | **SURVIVOR** |
| `edc763d5d4420075` | (28, 42, 16) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`d167fc392cd667a6`) | **SURVIVOR** |
| `ee87e3504746e36b` | (30, 45, 17) | [92, 96] | IT96 7/5 -> DIFFERENT TYPE (`822163f15ffc16d1`) | **SURVIVOR** |
| `f2338eb96662d54f` | (18, 28, 12) | [141] | IT141 4/5 -> DIFFERENT TYPE (`771186009d020142`) | **SURVIVOR** |
| `f5534a0cdd155dd1` | (30, 45, 17) | [142] | IT142 3497/1000 -> DIFFERENT TYPE (`5c6382a9ef3bc209`) | **SURVIVOR** |
| `f78cb8eda2f6b557` | (28, 42, 16) | [86] | IT86 3497/1000 -> DIFFERENT TYPE (`5be2e092046ee24b`) | **SURVIVOR** |

Still UNRESOLVED after this pass: 0.

### CORRECTION 2026-09-04 15:25 PDT (subagent #154): stable md5s

The md5s stated in the #154 addendum text above were RUN-DEPENDENT: the first version of the rows JSON carried a top-level `wall_seconds` and a per-cell `secs`, and the overlay JSON referenced the rows file by that changing md5, so the main-session re-run produced different hashes with identical verdict content. Timings were moved to the run log (no timing field in either JSON), and the two files are now byte-identical across runs. STABLE md5s: `collision_phase2_tetragonal_rows_recomputed.json` md5 4d27ce41466509feab6a180249330af7; `collision_phase2_tetragonal_unresolved_overlay.json` md5 a3716a2330c6dbe9c93414dfe8e832ee. Content unchanged: rows {'REPRODUCED': 62}; the 106 -> COLLISION 24, SURVIVOR 82; 404 after: COLLISION 201, SURVIVOR 203, UNRESOLVED 0; the row-level and type-level tables above are the content of record and are asserted equal to the JSONs by build_catalog.py and verify_counts_independent.py (v5).
