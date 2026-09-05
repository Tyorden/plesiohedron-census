# Schmitt printed-point collision screen, batch 2 — CROSS-GROUP pairs for the 11 G4-certified candidates (G5, 2026-08-30)

Script: `schmitt_crossgroup_check.py` (this run: 55 of 55 pair(s)); verdict machinery = `run_pair` IMPORTED from the accepted batch-1 `schmitt_collision_check.py`. Sources: Schmitt 2016 dissertation (`../references/Schmitt_2016_dissertation.pdf`), Sec. 2.2.5 per-group tables, printed pp. 119-150 (PDF page = printed + 5); frozen `spacegroups.json` (G1); `phase1_types.json` (Phase-1 ACCEPTED 2026-08-29); queue per the cross-group scan in `../G5_DILIGENCE_2026-08-30.md` (re-derived at runtime from the accepted digitization and asserted equal).

**LANGUAGE (stated once for every verdict below): a DIFFERENT-TYPE verdict does NOT establish novelty, and surviving ALL printed representatives still does not.** Schmitt's tables print ONE representative generating point per (group, f-vector) from a grid SAMPLING; a candidate type absent at every printed point may still occur in his unprinted ~14TB data. Every surviving candidate remains only "not matched against the catalog snapshot of 2026-08-30". A SAME-TYPE verdict IS decisive: the candidate's combinatorial type appears in Schmitt 2016 at his printed point for another group (collision; reframe per kill criteria).

## Transcription record (2026-08-30)

All 55 printed generating points extracted from the archived PDF's text layer (`pdftotext -layout`, per-page tracked) and verified four ways before use: (a) parsed f-vector sequences of all 36 cubic tables identical to the accepted triage digitization (881 rows); (b) parsed f-vectors AND frequencies identical to the accepted independent re-key (`rekey_tables.json`, 386 rows, six groups); (c) parser reproduces all 21 batch-1 visually-transcribed rows (point, frequency, page) verbatim; (d) each of the 55 rows below verified against a fresh visual read of its rendered PDF page this session. IT(212)/IT(213) share one printed table; runs use the frozen IT(212) ops — `canon_code` identifies mirror images, so verdicts cover both enantiomorphs.

Two-origin groups in this batch (IT 203, 222, 227, 228): printed points are origin choice 2, converted as x_ours = x_his - v (mod 1). v for 203/227/228 = the accepted batch-1 values; v for IT(222) = (3/4, 3/4, 3/4), NEW in this batch, machine-recovered from Schmitt's own 2016 ops (accepted `xcheck_schmitt_ops` machinery). `verify_origin_shifts()` re-derives ALL applied shifts at runtime and asserts agreement before any pair runs; independently, every pair must reproduce the printed f-vector (else FVEC-MISMATCH, the conversion-failure STOP).

| pair | cand | IT | printed f-vector | printed generating point | freq | printed p. | shift v |
|---|---|---|---|---|---|---|---|
| X01 | #1 | 199 | (37, 57, 22) | (1/12, 35/388, 77/388) | 7 | 123 | — |
| X02 | #1 | 214 | (37, 57, 22) | (75/776, 7/72, 407/2328) | 101 | 137 | — |
| X03 | #1 | 230 | (37, 57, 22) | (499/6984, 83/6984, 821/3492) | 1 | 150 | — |
| X04 | #2 | 206 | (40, 61, 23) | (1/8, 125/2328, 499/2328) | 22842322 | 129 | — |
| X05 | #2 | 212 | (40, 61, 23) | (-217/1062, -115/1062, 23/4248) | 2574890 | 135 | — |
| X06 | #2 | 214 | (40, 61, 23) | (10/97, 361/3492, 1123/6984) | 1660625 | 137 | — |
| X07 | #2 | 220 | (40, 61, 23) | (1/8, 365/6984, 373/1746) | 12841602 | 143 | — |
| X08 | #4 | 198 | (30, 46, 18) | (1/8, 1/24, 5/24) | 843 | 122 | — |
| X09 | #4 | 206 | (30, 46, 18) | (785/6984, 787/6984, 425/3492) | 30035545 | 128 | — |
| X10 | #4 | 214 | (30, 46, 18) | (31/1746, 109/873, 1309/6984) | 19665278 | 136 | — |
| X11 | #4 | 220 | (30, 46, 18) | (88/873, 353/3492, 127/1164) | 96509074 | 142 | — |
| X12 | #4 | 230 | (30, 46, 18) | (-455/6984, -73/776, 545/3492) | 53229871 | 150 | — |
| X13 | #5 | 199 | (30, 47, 19) | (439/6984, 49/776, 527/2328) | 168 | 123 | — |
| X14 | #5 | 206 | (30, 47, 19) | (-461/6984, -473/6984, 545/3492) | 8842620 | 128 | — |
| X15 | #5 | 212 | (30, 47, 19) | (-151/2124, -179/2124, -65/2124) | 52233655 | 134 | — |
| X16 | #5 | 230 | (30, 47, 19) | (-659/6984, -869/6984, 545/3492) | 5218967 | 150 | — |
| X17 | #6 | 197 | (10, 17, 9) | (909/3632, 909/3632, 453/1816) | 453 | 120 | — |
| X18 | #6 | 199 | (10, 17, 9) | (0, 0, 1/2328) | 436 | 122 | — |
| X19 | #6 | 211 | (10, 17, 9) | (121/454, 967/3632, 789/3632) | 179872 | 132 | — |
| X20 | #6 | 212 | (10, 17, 9) | (-1/4, -353/4248, 89/1062) | 177 | 133 | — |
| X21 | #6 | 217 | (10, 17, 9) | (909/3632, 909/3632, 453/1816) | 453 | 139 | — |
| X22 | #6 | 218 | (10, 17, 9) | (909/3632, 909/3632, 453/1816) | 453 | 140 | — |
| X23 | #6 | 230 | (10, 17, 9) | (-1/6984, -1/6984, 1745/6984) | 70 | 149 | — |
| X24 | #7 | 197 | (20, 33, 15) | (3285/7264, 3283/7264, 229/7264) | 20486921 | 121 | — |
| X25 | #7 | 206 | (20, 33, 15) | (-457/6984, -211/2328, 545/3492) | 36467 | 128 | — |
| X26 | #7 | 208 | (20, 33, 15) | (1937/7264, 1935/7264, 1577/7264) | 111858167 | 130 | — |
| X27 | #7 | 210 | (20, 33, 15) | (219/11528, 201/11528, 185/11528) | 110275905 | 132 | — |
| X28 | #7 | 212 | (20, 33, 15) | (-355/4248, -179/2124, -44/531) | 22087236 | 134 | — |
| X29 | #7 | 214 | (20, 33, 15) | (-73/776, -659/6984, 121/776) | 983215 | 136 | — |
| X30 | #7 | 218 | (20, 33, 15) | (3285/7264, 3283/7264, 229/7264) | 23274317 | 140 | — |
| X31 | #7 | 220 | (20, 33, 15) | (0, 9/388, 105/776) | 1 | 142 | — |
| X32 | #7 | 230 | (20, 33, 15) | (-53/1164, -43/582, 119/1164) | 11 | 149 | — |
| X33 | #8 | 197 | (14, 23, 11) | (1817/7264, 1817/7264, 1813/7264) | 491821 | 121 | — |
| X34 | #8 | 208 | (14, 23, 11) | (121/454, 967/3632, 789/3632) | 1027254 | 130 | — |
| X35 | #8 | 212 | (14, 23, 11) | (-103/1416, -103/1416, 103/1416) | 353 | 133 | — |
| X36 | #8 | 217 | (14, 23, 11) | (1817/7264, 1817/7264, 1813/7264) | 491821 | 139 | — |
| X37 | #8 | 218 | (14, 23, 11) | (1817/7264, 1817/7264, 1813/7264) | 491821 | 140 | — |
| X38 | #8 | 222 | (14, 23, 11) | (15/227, 45/3632, 7/3632) | 846570215 | 144 | (3/4, 3/4, 3/4) |
| X39 | #8 | 230 | (14, 23, 11) | (281/6984, 289/2328, 1453/6984) | 118 | 149 | — |
| X40 | #9 | 208 | (11, 18, 9) | (909/3632, 909/3632, 453/1816) | 453 | 130 | — |
| X41 | #10 | 195 | (6, 11, 7) | (1815/3632, 907/1816, 0) | 1646205 | 119 | — |
| X42 | #10 | 200 | (6, 11, 7) | (1815/3632, 907/1816, 0) | 1646205 | 124 | — |
| X43 | #10 | 202 | (6, 11, 7) | (247/7264, 13/1816, 7/3632) | 609531852 | 125 | — |
| X44 | #10 | 204 | (6, 11, 7) | (179/3632, 125/3632, 67/3632) | 1475 | 126 | — |
| X45 | #10 | 208 | (6, 11, 7) | (1817/7264, 1817/7264, 1815/7264) | 3630 | 130 | — |
| X46 | #10 | 228 | (6, 11, 7) | (721/5764, 180/1441, -180/1441) | 4320 | 147 | (1/8, 1/8, 5/8) |
| X47 | #11 | 203 | (10, 15, 7) | (180/1441, 180/1441, 180/1441) | 2880 | 125 | (7/8, 7/8, 7/8) |
| X48 | #11 | 204 | (10, 15, 7) | (1815/7264, 1815/7264, 1815/7264) | 1815 | 126 | — |
| X49 | #11 | 210 | (10, 15, 7) | (180/1441, 180/1441, 180/1441) | 1440 | 131 | — |
| X50 | #11 | 211 | (10, 15, 7) | (1815/7264, 1815/7264, 1815/7264) | 1815 | 132 | — |
| X51 | #11 | 217 | (10, 15, 7) | (1819/7264, 1817/7264, 1695/7264) | 148432727 | 139 | — |
| X52 | #11 | 222 | (10, 15, 7) | (1817/7264, 1817/7264, 1815/7264) | 5445 | 143 | (3/4, 3/4, 3/4) |
| X53 | #11 | 223 | (10, 15, 7) | (1815/7264, 1815/7264, 1815/7264) | 1815 | 144 | — |
| X54 | #11 | 227 | (10, 15, 7) | (180/1441, 180/1441, 180/1441) | 2880 | 147 | (7/8, 7/8, 7/8) |
| X55 | #11 | 229 | (10, 15, 7) | (1815/7264, 1815/7264, 1815/7264) | 1815 | 148 | — |

## Per-pair verdicts

| pair | cand | target type | IT | f-vector | orbit | stab | PERIOD | Schmitt cell p-vector | aut | verdict | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X01 | #1 | `ceb70631e274e727` | 199 | (37, 57, 22) | 24 | 1 | 1164 | `3^10 4^2 6^4 7^4 10^1 14^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 3.5 |
| X02 | #1 | `ceb70631e274e727` | 214 | (37, 57, 22) | 48 | 1 | 6984 | `3^6 4^7 5^2 6^4 10^1 11^1 13^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 13.3 |
| X03 | #1 | `ceb70631e274e727` | 230 | (37, 57, 22) | 96 | 1 | 6984 | `3^6 4^8 5^3 6^1 8^2 11^1 16^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 54.8 |
| X04 | #2 | `359beee832567a71` | 206 | (40, 61, 23) | 48 | 1 | 2328 | `3^2 4^12 5^6 10^2 18^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 15.3 |
| X05 | #2 | `359beee832567a71` | 212 | (40, 61, 23) | 24 | 1 | 4248 | `3^6 4^6 6^4 7^4 8^2 12^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 4.1 |
| X06 | #2 | `359beee832567a71` | 214 | (40, 61, 23) | 48 | 1 | 6984 | `3^6 4^11 8^1 10^4 12^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 15.0 |
| X07 | #2 | `359beee832567a71` | 220 | (40, 61, 23) | 48 | 1 | 6984 | `3^4 4^8 5^8 10^2 18^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 15.8 |
| X08 | #4 | `c314dedd38208a2e` | 198 | (30, 46, 18) | 12 | 1 | 24 | `3^4 4^2 5^8 7^2 9^2` | 2 | **SAME TYPE** | 0.8 |
| X09 | #4 | `c314dedd38208a2e` | 206 | (30, 46, 18) | 48 | 1 | 6984 | `3^4 4^5 6^6 7^2 10^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 11.9 |
| X10 | #4 | `c314dedd38208a2e` | 214 | (30, 46, 18) | 48 | 1 | 6984 | `3^2 4^9 5^2 6^3 10^1 12^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 11.2 |
| X11 | #4 | `c314dedd38208a2e` | 220 | (30, 46, 18) | 48 | 1 | 3492 | `3^6 4^4 6^4 7^2 8^1 12^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 11.7 |
| X12 | #4 | `c314dedd38208a2e` | 230 | (30, 46, 18) | 96 | 1 | 6984 | `4^10 5^2 6^2 7^2 8^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 45.8 |
| X13 | #5 | `aa6b0077c3234d24` | 199 | (30, 47, 19) | 24 | 1 | 6984 | `3^6 4^2 5^4 6^5 8^1 10^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 3.0 |
| X14 | #5 | `aa6b0077c3234d24` | 206 | (30, 47, 19) | 48 | 1 | 6984 | `3^2 4^10 5^2 6^1 7^2 9^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 11.6 |
| X15 | #5 | `aa6b0077c3234d24` | 212 | (30, 47, 19) | 24 | 1 | 2124 | `3^2 4^10 5^2 7^4 10^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 3.1 |
| X16 | #5 | `aa6b0077c3234d24` | 230 | (30, 47, 19) | 96 | 1 | 6984 | `3^4 4^9 6^1 7^2 8^2 10^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 45.2 |
| X17 | #6 | `f3d0f39a0b9676b9` | 197 | (10, 17, 9) | 24 | 1 | 10896 | `3^2 4^7` | 2 | **DIFFERENT TYPE** (= stored type `1c5d013b7a344bfb`) | 1.0 |
| X18 | #6 | `f3d0f39a0b9676b9` | 199 | (10, 17, 9) | 24 | 1 | 2328 | `3^3 4^5 5^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 1.0 |
| X19 | #6 | `f3d0f39a0b9676b9` | 211 | (10, 17, 9) | 48 | 1 | 10896 | `3^5 4^2 5^1 6^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 3.9 |
| X20 | #6 | `f3d0f39a0b9676b9` | 212 | (10, 17, 9) | 24 | 1 | 4248 | `3^4 4^3 5^2` | 2 | **SAME TYPE** | 1.1 |
| X21 | #6 | `f3d0f39a0b9676b9` | 217 | (10, 17, 9) | 24 | 2 | 10896 | `3^2 4^7` | 2 | **DIFFERENT TYPE** (= stored type `1c5d013b7a344bfb`) | 1.0 |
| X22 | #6 | `f3d0f39a0b9676b9` | 218 | (10, 17, 9) | 24 | 1 | 10896 | `3^2 4^7` | 2 | **DIFFERENT TYPE** (= stored type `1c5d013b7a344bfb`) | 1.0 |
| X23 | #6 | `f3d0f39a0b9676b9` | 230 | (10, 17, 9) | 96 | 1 | 6984 | `3^4 4^3 5^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 14.9 |
| X24 | #7 | `2de0a21129cabe90` | 197 | (20, 33, 15) | 24 | 1 | 21792 | `3^4 4^7 6^3 8^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 2.1 |
| X25 | #7 | `2de0a21129cabe90` | 206 | (20, 33, 15) | 48 | 1 | 6984 | `3^6 4^5 7^4` | 1 | **DIFFERENT TYPE** (not any stored type) | 7.9 |
| X26 | #7 | `2de0a21129cabe90` | 208 | (20, 33, 15) | 24 | 1 | 21792 | `3^6 4^4 6^4 8^1` | 1 | **DIFFERENT TYPE** (= stored type `54b54f88d19759a3`) | 2.2 |
| X27 | #7 | `2de0a21129cabe90` | 210 | (20, 33, 15) | 96 | 1 | 34584 | `3^4 4^8 6^1 8^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 31.6 |
| X28 | #7 | `2de0a21129cabe90` | 212 | (20, 33, 15) | 24 | 1 | 4248 | `3^6 4^3 6^6` | 1 | **DIFFERENT TYPE** (not any stored type) | 2.0 |
| X29 | #7 | `2de0a21129cabe90` | 214 | (20, 33, 15) | 48 | 1 | 6984 | `3^5 4^8 9^1 10^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 7.3 |
| X30 | #7 | `2de0a21129cabe90` | 218 | (20, 33, 15) | 24 | 1 | 21792 | `3^4 4^5 5^4 6^1 8^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 2.1 |
| X31 | #7 | `2de0a21129cabe90` | 220 | (20, 33, 15) | 48 | 1 | 2328 | `3^5 4^4 5^3 6^2 8^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 7.5 |
| X32 | #7 | `2de0a21129cabe90` | 230 | (20, 33, 15) | 96 | 1 | 1164 | `3^7 4^2 5^1 6^3 7^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 30.2 |
| X33 | #8 | `c4ea3f32fdd6dc51` | 197 | (14, 23, 11) | 24 | 1 | 21792 | `3^2 4^5 5^4` | 2 | **DIFFERENT TYPE** (not any stored type) | 1.4 |
| X34 | #8 | `c4ea3f32fdd6dc51` | 208 | (14, 23, 11) | 24 | 1 | 10896 | `3^4 4^3 5^2 6^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 1.5 |
| X35 | #8 | `c4ea3f32fdd6dc51` | 212 | (14, 23, 11) | 24 | 1 | 1416 | `3^6 4^2 6^2 8^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 1.4 |
| X36 | #8 | `c4ea3f32fdd6dc51` | 217 | (14, 23, 11) | 24 | 2 | 21792 | `3^2 4^5 5^4` | 2 | **DIFFERENT TYPE** (not any stored type) | 1.4 |
| X37 | #8 | `c4ea3f32fdd6dc51` | 218 | (14, 23, 11) | 24 | 1 | 21792 | `3^2 4^5 5^4` | 2 | **DIFFERENT TYPE** (not any stored type) | 1.4 |
| X38 | #8 | `c4ea3f32fdd6dc51` | 222 | (14, 23, 11) | 48 | 1 | 10896 | `3^2 4^5 5^4` | 1 | **DIFFERENT TYPE** (= stored type `d995cf9c001c7056`) | 5.5 |
| X39 | #8 | `c4ea3f32fdd6dc51` | 230 | (14, 23, 11) | 96 | 1 | 6984 | `3^2 4^5 5^4` | 1 | **DIFFERENT TYPE** (not any stored type) | 21.2 |
| X40 | #9 | `9b69eefb8bd8437c` | 208 | (11, 18, 9) | 24 | 1 | 10896 | `3^2 4^5 5^2` | 2 | **SAME TYPE** | 1.2 |
| X41 | #10 | `d2d935e5499e6e11` | 195 | (6, 11, 7) | 12 | 1 | 10896 | `3^6 4^1` | 2 | **DIFFERENT TYPE** (= stored type `36ea4b551873828d`) | 0.2 |
| X42 | #10 | `d2d935e5499e6e11` | 200 | (6, 11, 7) | 12 | 2 | 10896 | `3^6 4^1` | 2 | **DIFFERENT TYPE** (= stored type `36ea4b551873828d`) | 0.2 |
| X43 | #10 | `d2d935e5499e6e11` | 202 | (6, 11, 7) | 96 | 1 | 21792 | `3^6 4^1` | 2 | **DIFFERENT TYPE** (= stored type `36ea4b551873828d`) | 10.5 |
| X44 | #10 | `d2d935e5499e6e11` | 204 | (6, 11, 7) | 48 | 1 | 10896 | `3^6 4^1` | 4 | **SAME TYPE** | 2.4 |
| X45 | #10 | `d2d935e5499e6e11` | 208 | (6, 11, 7) | 24 | 1 | 21792 | `3^6 4^1` | 4 | **SAME TYPE** | 0.7 |
| X46 | #10 | `d2d935e5499e6e11` | 228 | (6, 11, 7) | 192 | 1 | 34584 | `3^6 4^1` | 4 | **SAME TYPE** | 38.4 |
| X47 | #11 | `f98a3ee5675fc121` | 203 | (10, 15, 7) | 32 | 3 | 34584 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 1.9 |
| X48 | #11 | `f98a3ee5675fc121` | 204 | (10, 15, 7) | 16 | 3 | 21792 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 0.5 |
| X49 | #11 | `f98a3ee5675fc121` | 210 | (10, 15, 7) | 32 | 3 | 17292 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 1.8 |
| X50 | #11 | `f98a3ee5675fc121` | 211 | (10, 15, 7) | 16 | 3 | 21792 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 0.5 |
| X51 | #11 | `f98a3ee5675fc121` | 217 | (10, 15, 7) | 48 | 1 | 21792 | `3^2 4^2 5^2 6^1` | 2 | **DIFFERENT TYPE** (not any stored type) | 3.9 |
| X52 | #11 | `f98a3ee5675fc121` | 222 | (10, 15, 7) | 16 | 3 | 21792 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 0.4 |
| X53 | #11 | `f98a3ee5675fc121` | 223 | (10, 15, 7) | 16 | 3 | 21792 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 0.5 |
| X54 | #11 | `f98a3ee5675fc121` | 227 | (10, 15, 7) | 32 | 6 | 34584 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 1.9 |
| X55 | #11 | `f98a3ee5675fc121` | 229 | (10, 15, 7) | 16 | 6 | 21792 | `3^3 5^3 6^1` | 6 | **DIFFERENT TYPE** (= stored type `ca9a19039647d676`) | 0.5 |

## Per-candidate cross-group summary (this run)

- #1 `ceb70631e274e727`: **SURVIVES-ALL** — all 3 cross-group printed representatives are DIFFERENT types (snapshot language only).
- #2 `359beee832567a71`: **SURVIVES-ALL** — all 4 cross-group printed representatives are DIFFERENT types (snapshot language only).
- #3 `8cf50403cf88c455` (IT(220), (16,25,11)): ZERO cross-group pairs — the f-vector is absent from the ENTIRE printed cubic survey (G5 doc); nothing to run. Cross-group status: SURVIVES-ALL vacuously (strongest Schmitt-side candidate; sampling caveat stands).
- #4 `c314dedd38208a2e`: **COLLIDED-AT IT[198]** — the candidate's type IS Schmitt's printed cell there (1/5 pairs SAME); reframe per kill criteria.
- #5 `aa6b0077c3234d24`: **SURVIVES-ALL** — all 4 cross-group printed representatives are DIFFERENT types (snapshot language only).
- #6 `f3d0f39a0b9676b9`: **COLLIDED-AT IT[212]** — the candidate's type IS Schmitt's printed cell there (1/7 pairs SAME); reframe per kill criteria.
- #7 `2de0a21129cabe90`: **SURVIVES-ALL** — all 9 cross-group printed representatives are DIFFERENT types (snapshot language only).
- #8 `c4ea3f32fdd6dc51`: **SURVIVES-ALL** — all 7 cross-group printed representatives are DIFFERENT types (snapshot language only).
- #9 `9b69eefb8bd8437c`: **COLLIDED-AT IT[208]** — the candidate's type IS Schmitt's printed cell there (1/1 pairs SAME); reframe per kill criteria.
- #10 `d2d935e5499e6e11`: **COLLIDED-AT IT[204, 208, 228]** — the candidate's type IS Schmitt's printed cell there (3/6 pairs SAME); reframe per kill criteria.
- #11 `f98a3ee5675fc121`: **SURVIVES-ALL** — all 9 cross-group printed representatives are DIFFERENT types (snapshot language only).

## Notes

- The pair queue (candidate f-vector x other printed group) is re-derived at runtime from `triage_phase1.SCHMITT_FVECTORS` and asserted equal to the hardcoded list — 55 pairs, matching the G5 doc's scan table (3+4+0+5+4+7+9+7+1+6+9).
- Cross-group rows in the 30 non-re-keyed tables rest on the single-pass digitization for their SEQUENCE placement; the specific rows used here were each verified visually this session (points were never digitized before this batch).
- Where a DIFFERENT verdict names a stored type, Schmitt's printed representative for that (group, f-vector) is itself a type our sweep also found — a same-f-two-types micro-fact, as in batch 1.
- Per-pair wall-clock cap 600 s -> TIMEOUT-DEFERRED (recorded, never silent).
- Certificate asserted per cell (run_pair, accepted): float/exact facet-count and p-vector agreement, 4*rho^2 <= D^2 exact cutoff, one canonical code across the whole orbit; printed f-vector reproduced (else FVEC-MISMATCH).
- Kill criteria live; none of these pairs can raise facet counts (max candidate F = 23, observed literature max 38).
