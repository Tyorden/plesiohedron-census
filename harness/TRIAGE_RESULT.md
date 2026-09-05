# TRIAGE result — Phase-1 unmatched types -> G4 shortlist (2026-08-30)

Script: `triage_phase1.py` (deterministic; byte-identical across re-runs). Store: `phase1_types.json` (Phase-1 ACCEPTED 2026-08-29). Gates: `../ANCHORS.md` G4 (finalist certificates) and G5 (novelty diligence — NOT run here).

**LANGUAGE (G5): every type below is "not matched against the catalog snapshot of 2026-08-28". No novelty claim. The Schmitt column is f-vector-level evidence from his printed in-text tables (a 351-CPU-year grid SAMPLING, not an enumeration): "A" = absent there (stronger candidate, still only snapshot language), "P" = present (same f-vector does NOT mean same type — the Josehedron/Schmitt-220 pair proves this — so a G5 type-level check is required).**

## Sanity duties

- Schmitt digitization self-check: 881 f-vector rows over 36 cubic groups (212/213 shared), all Euler-consistent, no in-group duplicates, per-group max facet counts agree with Schmitt's Sec. 2.3 remarks for the 11 groups he comments on: PASS
- Euler V-E+F=2: checked for all 102 stored types: ALL PASS
- p-vector consistency (|p|=F and sum(p)=2E) for all 102 types: ALL PASS
- site-stabilizer divides aut, every sighting: ALL PASS
- kill criterion (>38 facets): max stored facet count = 23: NO HITS
- recount: 95 unmatched + 7 seeded = 102 types; STATUS/PHASE1_RESULT claim 95 + 7 = 102: MATCH

## Schmitt in-text table digitization (new this step)

All 36 cubic per-group f-vector tables from Schmitt 2016 Sec. 2.2.5 (`references/Schmitt_2016_dissertation.pdf`, printed pp. 119-150, PDF pages 124-155) were transcribed at f-vector level into `triage_phase1.py` (881 rows; 212/213 share one printed table for the enantiomorphic pair). Verification applied: every row passes Euler; per-group max facet counts agree with Schmitt's own Sec. 2.3 discussion for all 11 groups he comments on (197,198,199,205,206,210,212,214,220,227,228). LIMIT: single-pass visual transcription, not yet independently double-keyed — flags are provisional; an independent re-key is queued as a G5 duty. The previously banked IT(220) row f=(12,22,12) (SCHMITT_220_CHECK_RESULT.md) is contained in the digitized 220 table: CONSISTENT.

## TOP-10 G4 SHORTLIST

1. `ceb70631e274e727` — **212 P4_332** at (1/12, 1/12, 1/12), f=(37, 57, 22), p=3^6 4^6 5^6 10^3 12^1, aut=3 [score 110.69]  
   22 facets; aut 3; corridor 212 P4_332/213 P4_132; faces incl. 5-gon,10-gon,12-gon; special-position stratum (dim 1, stab 3); 4 sighting(s); Schmitt f-vec present -> G5 type-level check
2. `359beee832567a71` — **230 Ia-3d** at (1/12, 1/6, 1/8), f=(40, 61, 23), p=4^20 11^2 20^1, aut=4 [score 107.5]  
   23 facets; aut 4; 230 Ia-3d; faces incl. 11-gon,20-gon; special-position stratum (dim 1, stab 2); 1 sighting(s); Schmitt f-vec present -> G5 type-level check
3. `fd96e7fc36481986` — **199 I2_13** at (1/12, 1/12, 1/12), f=(36, 54, 20), p=3^12 6^2 10^6, aut=12 [score 96.59]  
   20 facets; aut 12; corridor 199 I2_13; faces incl. 10-gon; special-position stratum (dim 1, stab 3); 4 sighting(s); Schmitt f-vec present -> G5 type-level check
4. `998994bcf8df722b` — **206 Ia-3** at (1/12, 1/12, 1/12), f=(30, 45, 17), p=4^12 6^2 10^3, aut=12 [score 94.89]  
   17 facets; aut 12; corridor 206 Ia-3/220 I-43d; 230 Ia-3d; faces incl. 10-gon; special-position stratum (dim 0, stab 6); 5 sighting(s); Schmitt f-vec present -> G5 type-level check
5. `8c69db9e84095469` — **199 I2_13** at (1/8, 1/8, 1/8), f=(30, 45, 17), p=4^6 5^6 6^2 8^3, aut=12 [score 94.22]  
   17 facets; aut 12; corridor 199 I2_13/212 P4_332/213 P4_132/214 I4_132; faces incl. 5-gon,8-gon; special-position stratum (dim 0, stab 6); 6 sighting(s); Schmitt f-vec present -> G5 type-level check
6. `2001fe7ea92fd0ad` — **212 P4_332** at (0, 0, 0), f=(16, 30, 16), p=3^12 6^4, aut=24 [score 92.8]  
   16 facets; aut 24; corridor 212 P4_332/213 P4_132; special-position stratum (dim 0, stab 24); 10 sighting(s); Schmitt f-vec present -> G5 type-level check
7. `afeb1ae44c1a3443` — **198 P2_13** at (1/8, 1/8, 1/8), f=(32, 48, 18), p=4^12 8^6, aut=6 [score 90.96]  
   18 facets; aut 6; corridor 198 P2_13/212 P4_332/213 P4_132; faces incl. 8-gon; special-position stratum (dim 0, stab 6); 8 sighting(s); Schmitt f-vec present -> G5 type-level check
8. `c314dedd38208a2e` — **212 P4_332** at (1/12, 1/6, 1/8), f=(30, 46, 18), p=3^4 4^2 5^8 7^2 9^2, aut=2 [score 84.48]  
   18 facets; aut 2; corridor 212 P4_332/213 P4_132; faces incl. 5-gon,7-gon,9-gon; special-position stratum (dim 1, stab 2); 4 sighting(s); Schmitt f-vec present -> G5 type-level check
9. `aa6b0077c3234d24` — **214 I4_132** at (0, 1/4, 1/12), f=(30, 47, 19), p=3^4 4^5 5^6 6^2 10^2, aut=2 [score 83.38]  
   19 facets; aut 2; corridor 214 I4_132; faces incl. 5-gon,10-gon; special-position stratum (dim 1, stab 2); 2 sighting(s); Schmitt f-vec present -> G5 type-level check
10. `ea1baec328356a32` — **201 Pn-3** at (1/12, 1/12, 1/12), f=(25, 39, 16), p=4^12 6^3 12^1, aut=6 [score 78.6]  
   16 facets; aut 6; faces incl. 12-gon; special-position stratum (dim 1, stab 6); 20 sighting(s); Schmitt f-vec present -> G5 type-level check

## Full ranked table (all unmatched types)

Schmitt column: per sighted group, P = f-vector in his printed table for that group, A = absent, U = table not digitized. min-dim: 0 fixed Wyckoff point / 1 line sample / 2 plane sample / 3 general position (minimum over sightings).

| rank | id | f-vector | p-vector | aut | witness | stab | min-dim | sgt | sighted groups | Schmitt | score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `ceb70631e274e727` | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | 212 P4_332 | 3 | 1 | 4 | 212:P 213:P | present | 110.69 |
| 2 | `359beee832567a71` | (40, 61, 23) | 4^20 11^2 20^1 | 4 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 107.5 |
| 3 | `fd96e7fc36481986` | (36, 54, 20) | 3^12 6^2 10^6 | 12 | 199 I2_13 | 3 | 1 | 4 | 199:P | present | 96.59 |
| 4 | `998994bcf8df722b` | (30, 45, 17) | 4^12 6^2 10^3 | 12 | 206 Ia-3 | 6 | 0 | 5 | 206:P 220:P 230:P | present | 94.89 |
| 5 | `8c69db9e84095469` | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 12 | 199 I2_13 | 6 | 0 | 6 | 199:P 212:P 213:P 214:P | present | 94.22 |
| 6 | `2001fe7ea92fd0ad` | (16, 30, 16) | 3^12 6^4 | 24 | 212 P4_332 | 24 | 0 | 10 | 203:P 210:P 212:P 213:P 227:P | present | 92.8 |
| 7 | `afeb1ae44c1a3443` | (32, 48, 18) | 4^12 8^6 | 6 | 198 P2_13 | 6 | 0 | 8 | 198:P 212:P 213:P | present | 90.96 |
| 8 | `c314dedd38208a2e` | (30, 46, 18) | 3^4 4^2 5^8 7^2 9^2 | 2 | 212 P4_332 | 2 | 1 | 4 | 212:P 213:P | present | 84.48 |
| 9 | `aa6b0077c3234d24` | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 2 | 214 I4_132 | 2 | 1 | 2 | 214:P | present | 83.38 |
| 10 | `ea1baec328356a32` | (25, 39, 16) | 4^12 6^3 12^1 | 6 | 201 Pn-3 | 6 | 1 | 20 | 201:P 208:P 224:P 228:P | present | 78.6 |
| 11 | `1148b1810c34b982` | (26, 39, 15) | 4^6 6^9 | 12 | 197 I23 | 6 | 1 | 18 | 197:P 217:P 218:P | present | 76.48 |
| 12 | `df70dc799acd7711` | (28, 45, 19) | 3^6 4^5 5^2 6^4 8^1 10^1 | 1 | 213 P4_132 | 1 | 3 | 1 | 213:P | present | 76.3 |
| 13 | `9effc8684d8a0250` | (10, 20, 12) | 3^8 4^4 | 16 | 197 I23 | 16 | 0 | 22 | 197:P 201:A 203:P 204:P 208:P 210:P 211:P 217:P 218:P 222:A 223:P 224:A 227:P 228:P 229:P 230:A | present | 76.29 |
| 14 | `3cb6c70abd57e0b9` | (6, 12, 8) | 3^8 | 48 | 206 Ia-3 | 16 | 0 | 93 | 195:P 196:P 200:P 202:P 203:A 204:P 206:A 207:P 209:P 210:A 211:P 215:P 216:P 217:P 219:P 221:P 222:P 223:P 224:P 225:P 226:P 227:A 229:P | present | 75.27 |
| 15 | `effc729383b9ec06` | (22, 36, 16) | 3^6 4^6 6^1 8^3 | 3 | 212 P4_332 | 3 | 1 | 4 | 212:P 213:P | present | 75.19 |
| 16 | `f0163697449d793a` | (26, 40, 16) | 4^8 5^4 7^4 | 2 | 199 I2_13 | 2 | 1 | 4 | 199:P | present | 75.08 |
| 17 | `dab82b770ec34253` | (16, 28, 14) | 3^8 4^2 6^4 | 4 | 206 Ia-3 | 4 | 0 | 8 | 206:A 213:P 214:P 230:P | present | 74.85 |
| 18 | `0ee26ed471c923e2` | (22, 35, 15) | 3^4 5^10 8^1 | 2 | 220 I-43d | 2 | 1 | 2 | 220:P | present | 74.58 |
| 19 | `80f5582684f3bd01` | (22, 36, 16) | 3^4 4^4 5^4 6^4 | 2 | 198 P2_13 | 2 | 1 | 17 | 198:P 212:P 213:P | present | 74.45 |
| 20 | `1006ba9d7710fc74` | (20, 32, 14) | 4^10 6^4 | 4 | 206 Ia-3 | 4 | 0 | 5 | 206:P 220:P 230:P | present | 74.38 |
| 21 | `a3164ecfcd75d3ec` | (17, 28, 13) | 4^12 8^1 | 8 | 197 I23 | 8 | 1 | 80 | 197:P 201:P 204:P 208:P 211:P 217:P 218:P 222:P 223:P 224:P 228:P 229:P | present | 74.21 |
| 22 | `cb7114c8a5122943` | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 2 | 214 I4_132 | 2 | 1 | 2 | 214:P | present | 73.78 |
| 23 | `3497979d000ba708` | (30, 47, 19) | 3^6 4^5 5^4 6^2 12^2 | 1 | 214 I4_132 | 1 | 3 | 1 | 214:P | present | 73.5 |
| 24 | `d92507e86522ff33` | (19, 32, 15) | 3^8 4^3 7^4 | 2 | 206 Ia-3 | 2 | 1 | 3 | 206:P 220:P 230:P | present | 71.9 |
| 25 | `cea2f3246210cd55` | (22, 35, 15) | 3^2 4^7 5^4 8^2 | 2 | 199 I2_13 | 2 | 1 | 4 | 199:P 212:P 214:P | present | 71.68 |
| 26 | `8cf50403cf88c455` | (16, 25, 11) | 3^2 4^1 5^8 | 4 | 220 I-43d | 2 | 1 | 2 | 220:A | ABSENT-all | 67.98 |
| 27 | `e6ba9617aaf7ab80` | (16, 28, 14) | 3^8 4^4 8^2 | 4 | 208 P4_232 | 4 | 1 | 18 | 208:P 218:P 223:P | present | 67.97 |
| 28 | `61793797a474ca0c` | (24, 38, 16) | 3^8 4^1 6^4 8^3 | 2 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 67.9 |
| 29 | `971596772f324b8e` | (12, 22, 12) | 3^8 5^4 | 4 | 199 I2_13 | 4 | 0 | 8 | 199:A 212:P 213:P 214:A | present | 67.45 |
| 30 | `37c8918c625da53c` | (26, 40, 16) | 4^10 5^2 6^1 7^2 10^1 | 1 | 214 I4_132 | 1 | 3 | 1 | 214:P | present | 67.1 |
| 31 | `bad4b371f5bd4e3e` | (19, 30, 13) | 4^6 5^6 6^1 | 3 | 205 Pa-3 | 3 | 1 | 6 | 205:P | present | 66.62 |
| 32 | `3d1a3ee0cfdc0206` | (8, 16, 10) | 3^8 4^2 | 8 | 195 P23 | 8 | 0 | 61 | 195:P 196:P 200:P 202:P 208:P 210:P 218:P 223:P 230:A | present | 66.23 |
| 33 | `dd90029f74b374ae` | (15, 26, 13) | 3^4 4^5 5^4 | 2 | 220 I-43d | 2 | 1 | 2 | 220:P | present | 64.88 |
| 34 | `d5455821196c461d` | (14, 25, 13) | 3^8 5^4 6^1 | 4 | 197 I23 | 4 | 1 | 18 | 197:P 201:A 204:P | present | 64.77 |
| 35 | `9d34332ec1120aff` | (22, 36, 16) | 3^6 4^2 5^6 8^2 | 1 | 205 Pa-3 | 1 | 3 | 1 | 205:P | present | 63.7 |
| 36 | `18391c406d2fe823` | (12, 20, 10) | 4^10 | 16 | 204 Im-3 | 4 | 1 | 33 | 204:P 211:P 217:P 222:P 223:P 224:P 229:P | present | 61.83 |
| 37 | `7d9cb42d3e017b02` | (16, 27, 13) | 3^4 4^6 5^2 8^1 | 2 | 195 P23 | 2 | 1 | 16 | 195:P 208:P 210:P | present | 61.73 |
| 38 | `3dae45da9b1de603` | (22, 34, 14) | 4^4 5^8 6^2 | 2 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 61.7 |
| 39 | `d6d4863002a0c8c3` | (15, 27, 14) | 3^6 4^6 6^2 | 3 | 230 Ia-3d | 3 | 1 | 1 | 230:P | present | 61.51 |
| 40 | `81ae9d74bed8fad3` | (20, 32, 14) | 4^11 6^2 8^1 | 2 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 61.5 |
| 41 | `ff0921cada9796e2` | (16, 27, 13) | 3^6 4^4 6^2 8^1 | 2 | 214 I4_132 | 2 | 1 | 2 | 214:P | present | 60.98 |
| 42 | `093e6d425d7e4fc0` | (24, 38, 16) | 3^6 4^3 5^2 6^3 8^1 10^1 | 1 | 208 P4_232 | 1 | 3 | 1 | 208:P | present | 60.9 |
| 43 | `ddd534b6185c5da1` | (12, 22, 12) | 3^4 4^8 | 8 | 203 Fd-3 | 4 | 1 | 6 | 203:P 210:P 227:P | present | 60.41 |
| 44 | `2aafa354bb5e01d9` | (16, 27, 13) | 3^2 4^9 6^2 | 2 | 199 I2_13 | 2 | 1 | 6 | 199:P 212:P 214:P | present | 59.81 |
| 45 | `2de0a21129cabe90` | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 1 | 201 Pn-3 | 1 | 3 | 1 | 201:A | ABSENT-all | 59.5 |
| 46 | `e5f952f88b3beade` | (9, 18, 11) | 3^8 4^3 | 3 | 220 I-43d | 3 | 1 | 2 | 220:P | present | 58.79 |
| 47 | `8993441351ed232f` | (21, 34, 15) | 3^2 4^8 5^4 10^1 | 1 | 230 Ia-3d | 1 | 3 | 1 | 230:P | present | 58.6 |
| 48 | `21d94ee4a2af0f9f` | (22, 35, 15) | 3^6 4^1 5^4 6^1 7^2 8^1 | 1 | 218 P-43n | 1 | 3 | 2 | 218:P | present | 58.58 |
| 49 | `ec7cd8bf24cc544f` | (18, 29, 13) | 4^7 5^6 | 2 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 58.3 |
| 50 | `c5b97d7745060a86` | (22, 35, 15) | 3^6 4^3 5^2 7^2 8^2 | 1 | 201 Pn-3 | 1 | 3 | 1 | 201:P | present | 57.7 |
| 51 | `e7f0765aca44108d` | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 1 | 206 Ia-3 | 1 | 3 | 1 | 206:P | present | 57.5 |
| 52 | `c4c06de9148a1d5e` | (18, 30, 14) | 3^4 4^6 5^2 7^2 | 1 | 205 Pa-3 | 1 | 3 | 1 | 205:P | present | 57.3 |
| 53 | `f037247acdde20aa` | (13, 22, 11) | 3^2 4^7 5^2 | 2 | 214 I4_132 | 2 | 1 | 2 | 214:P | present | 54.68 |
| 54 | `b1f554d5e1c1ffe1` | (20, 32, 14) | 3^6 4^3 5^2 6^1 8^1 10^1 | 1 | 211 I432 | 1 | 3 | 1 | 211:P | present | 54.5 |
| 55 | `5c4afde4a99b7e18` | (11, 19, 10) | 3^4 4^4 5^2 | 4 | 204 Im-3 | 4 | 1 | 11 | 204:P 211:P 217:P 222:A 223:P 224:A 229:P | present | 54.48 |
| 56 | `1c61fe8a173a95f3` | (14, 24, 12) | 3^4 4^4 5^4 | 2 | 203 Fd-3 | 2 | 1 | 6 | 203:P 219:P 228:P | present | 53.61 |
| 57 | `f3d0f39a0b9676b9` | (10, 17, 9) | 3^4 4^3 5^2 | 2 | 214 I4_132 | 2 | 1 | 2 | 214:A | ABSENT-all | 53.38 |
| 58 | `4fc0ad99c617364f` | (10, 19, 11) | 3^6 4^5 | 4 | 230 Ia-3d | 2 | 1 | 1 | 230:P | present | 52.5 |
| 59 | `b12aa22b226a2f18` | (17, 28, 13) | 3^4 4^5 5^2 6^1 8^1 | 1 | 230 Ia-3d | 1 | 3 | 1 | 230:P | present | 52.2 |
| 60 | `2508b5bfd6393c2c` | (14, 24, 12) | 3^2 4^8 5^2 | 1 | 220 I-43d | 1 | 3 | 1 | 220:P | present | 51.9 |
| 61 | `54b54f88d19759a3` | (20, 33, 15) | 3^6 4^4 6^4 8^1 | 1 | 208 P4_232 | 1 | 3 | 1 | 208:P | present | 51.5 |
| 62 | `e1c6bb874212013b` | (4, 6, 4) | 3^4 | 24 | 197 I23 | 8 | 0 | 103 | 197:P 201:A 204:P 207:P 211:P 215:P 216:P 217:P 221:P 222:A 224:A 225:P 226:P 227:P 228:A 229:P | present | 51.29 |
| 63 | `8f286dc3c145b5c1` | (5, 9, 6) | 3^6 | 12 | 200 Pm-3 | 6 | 1 | 100 | 200:P 202:P 204:P 207:P 209:P 211:P 215:P 217:P 221:P 222:A 223:P 224:A 225:P 226:P 229:P | present | 51.0 |
| 64 | `1c845578c03feb42` | (9, 17, 10) | 3^6 4^4 | 4 | 204 Im-3 | 4 | 1 | 7 | 204:P 211:P 217:P 222:A 223:P 224:A 229:P | present | 50.4 |
| 65 | `c4ea3f32fdd6dc51` | (14, 23, 11) | 3^4 4^4 6^3 | 2 | 224 Pn-3m | 2 | 2 | 4 | 224:A | ABSENT-all | 50.38 |
| 66 | `ca9a19039647d676` | (10, 15, 7) | 3^3 5^3 6^1 | 6 | 203 Fd-3 | 6 | 1 | 21 | 203:P 204:P 210:P 211:P 222:P 223:P 227:P 229:P | present | 50.2 |
| 67 | `4adc28c1904f92e2` | (11, 19, 10) | 3^4 4^4 5^2 | 2 | 204 Im-3 | 2 | 2 | 44 | 204:P 223:P | present | 49.84 |
| 68 | `bc4a89d3111082c9` | (13, 22, 11) | 3^1 4^9 5^1 | 2 | 204 Im-3 | 2 | 2 | 8 | 204:P 223:P | present | 49.55 |
| 69 | `c5962af3dcab8e26` | (12, 19, 9) | 4^8 6^1 | 4 | 217 I-43m | 2 | 2 | 46 | 217:P 224:P | present | 48.03 |
| 70 | `42bc5c5af1f296ae` | (5, 8, 5) | 3^4 4^1 | 8 | 195 P23 | 8 | 1 | 196 | 195:P 200:P 202:P 207:P 209:P 215:P 216:P 219:P 221:P 225:P 226:P 227:P 229:P | present | 47.93 |
| 71 | `481d26d16f89a9f8` | (13, 22, 11) | 3^5 4^3 5^1 6^2 | 2 | 223 Pm-3n | 2 | 2 | 2 | 223:P | present | 47.18 |
| 72 | `f5d10226705a540c` | (13, 22, 11) | 3^5 4^1 5^5 | 2 | 204 Im-3 | 2 | 2 | 2 | 204:P | present | 47.18 |
| 73 | `73ae50cb39507abf` | (8, 15, 9) | 3^6 4^3 | 6 | 209 F432 | 2 | 2 | 8 | 209:P 226:P | present | 46.39 |
| 74 | `9b69eefb8bd8437c` | (11, 18, 9) | 3^2 4^5 5^2 | 2 | 224 Pn-3m | 2 | 2 | 2 | 224:A | ABSENT-all | 45.98 |
| 75 | `864f0730e9e2ab41` | (11, 19, 10) | 3^4 4^4 5^2 | 2 | 223 Pm-3n | 2 | 2 | 6 | 223:P | present | 45.81 |
| 76 | `bb9b4185aaf3bd6c` | (16, 26, 12) | 3^2 4^7 5^2 8^1 | 1 | 211 I432 | 1 | 3 | 1 | 211:P | present | 45.1 |
| 77 | `a1053191a6317676` | (6, 9, 5) | 3^2 4^3 | 12 | 211 I432 | 4 | 1 | 29 | 211:P 215:P 217:P 222:A 224:A 227:P 228:A 229:P | present | 44.3 |
| 78 | `4ab699adbeb533b0` | (8, 13, 7) | 3^2 4^5 | 4 | 204 Im-3 | 2 | 2 | 116 | 204:P 215:P 223:P 227:P 229:P | present | 43.61 |
| 79 | `ea22673a3a17c26a` | (8, 14, 8) | 3^4 4^4 | 2 | 212 P4_332 | 2 | 1 | 4 | 212:P 213:P | present | 43.28 |
| 80 | `63fe22ddbb5dc8f2` | (18, 29, 13) | 3^2 4^7 6^4 | 1 | 197 I23 | 1 | 3 | 2 | 197:P | present | 43.18 |
| 81 | `6f76cff2845e50c4` | (10, 18, 10) | 3^4 4^6 | 2 | 204 Im-3 | 2 | 2 | 6 | 204:P | present | 42.71 |
| 82 | `d2d935e5499e6e11` | (6, 11, 7) | 3^6 4^1 | 4 | 224 Pn-3m | 2 | 2 | 6 | 224:A | ABSENT-all | 42.31 |
| 83 | `cb203d1497f608a6` | (8, 15, 9) | 3^6 4^3 | 2 | 207 P432 | 2 | 1 | 8 | 207:P 211:P | present | 41.55 |
| 84 | `e1c8fb393143bb7d` | (8, 16, 10) | 3^8 4^2 | 2 | 223 Pm-3n | 2 | 2 | 2 | 223:P | present | 40.68 |
| 85 | `d995cf9c001c7056` | (14, 23, 11) | 3^2 4^5 5^4 | 1 | 222 Pn-3n | 1 | 3 | 2 | 222:P | present | 39.78 |
| 86 | `36ea4b551873828d` | (6, 11, 7) | 3^6 4^1 | 2 | 200 Pm-3 | 2 | 2 | 86 | 200:P 202:P | present | 38.76 |
| 87 | `1c5d013b7a344bfb` | (10, 17, 9) | 3^2 4^7 | 2 | 217 I-43m | 2 | 2 | 2 | 217:P | present | 37.88 |
| 88 | `f98a3ee5675fc121` | (10, 15, 7) | 3^2 4^3 6^2 | 4 | 224 Pn-3m | 1 | 3 | 1 | 224:A | ABSENT-all | 36.5 |
| 89 | `656d9056ac5f71b1` | (7, 13, 8) | 3^6 4^2 | 2 | 223 Pm-3n | 2 | 2 | 6 | 223:P | present | 36.41 |
| 90 | `3689e6843979c9c4` | (9, 14, 7) | 3^2 4^4 6^1 | 4 | 229 Im-3m | 2 | 2 | 3 | 229:P | present | 36.4 |
| 91 | `d724d08efce3fe5f` | (8, 13, 7) | 3^4 4^2 6^1 | 4 | 227 Fd-3m | 2 | 2 | 2 | 227:P | present | 35.68 |
| 92 | `d1fe8ecee64ce269` | (8, 12, 6) | 3^2 4^2 5^2 | 4 | 229 Im-3m | 2 | 2 | 1 | 229:P | present | 34.8 |
| 93 | `920b287204a10d5a` | (6, 10, 6) | 3^4 4^2 | 2 | 200 Pm-3 | 2 | 1 | 8 | 200:P 223:P | present | 32.35 |
| 94 | `26df90c2289ea27c` | (7, 11, 6) | 3^3 4^2 5^1 | 2 | 229 Im-3m | 2 | 2 | 1 | 229:P | present | 30.7 |
| 95 | `ab4f647ac25e875b` | (7, 12, 7) | 3^5 4^1 5^1 | 1 | 226 Fm-3c | 1 | 3 | 2 | 226:P | present | 27.08 |

## f-vectors ABSENT from every sighted group's printed Schmitt table (7 of 95)

- `8cf50403cf88c455` f=(16, 25, 11) p=3^2 4^1 5^8 aut=4 — sighted in 220 I-43d — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `2de0a21129cabe90` f=(20, 33, 15) p=3^6 4^3 5^2 6^2 7^2 aut=1 — sighted in 201 Pn-3 — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `f3d0f39a0b9676b9` f=(10, 17, 9) p=3^4 4^3 5^2 aut=2 — sighted in 214 I4_132 — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `c4ea3f32fdd6dc51` f=(14, 23, 11) p=3^4 4^4 6^3 aut=2 — sighted in 224 Pn-3m — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `9b69eefb8bd8437c` f=(11, 18, 9) p=3^2 4^5 5^2 aut=2 — sighted in 224 Pn-3m — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `d2d935e5499e6e11` f=(6, 11, 7) p=3^6 4^1 aut=4 — sighted in 224 Pn-3m — his grid sampled these groups without printing this f-vector (evidence, not proof).
- `f98a3ee5675fc121` f=(10, 15, 7) p=3^2 4^3 6^2 aut=4 — sighted in 224 Pn-3m — his grid sampled these groups without printing this f-vector (evidence, not proof).

## Per-group counts (unmatched types)

| group | symbol | corridor | first-witness here | sighted here |
|---|---|---|---|---|
| 195 | P23 |  | 3 | 4 |
| 196 | F23 |  | 0 | 2 |
| 197 | I23 |  | 6 | 6 |
| 198 | P2_13 | Y | 2 | 2 |
| 199 | I2_13 | Y | 6 | 6 |
| 200 | Pm-3 |  | 3 | 6 |
| 201 | Pn-3 |  | 3 | 7 |
| 202 | Fm-3 |  | 0 | 5 |
| 203 | Fd-3 |  | 3 | 6 |
| 204 | Im-3 |  | 8 | 15 |
| 205 | Pa-3 | Y | 3 | 3 |
| 206 | Ia-3 | Y | 6 | 6 |
| 207 | P432 |  | 1 | 5 |
| 208 | P4_232 |  | 3 | 8 |
| 209 | F432 |  | 1 | 4 |
| 210 | F4_132 |  | 0 | 7 |
| 211 | I432 |  | 3 | 13 |
| 212 | P4_332 | Y | 5 | 11 |
| 213 | P4_132 | Y | 1 | 11 |
| 214 | I4_132 | Y | 7 | 12 |
| 215 | P-43m |  | 0 | 6 |
| 216 | F-43m |  | 0 | 3 |
| 217 | I-43m |  | 2 | 12 |
| 218 | P-43n |  | 1 | 6 |
| 219 | F-43c |  | 0 | 3 |
| 220 | I-43d | Y | 5 | 8 |
| 221 | Pm-3m |  | 0 | 4 |
| 222 | Pn-3n |  | 1 | 11 |
| 223 | Pm-3n |  | 4 | 18 |
| 224 | Pn-3m |  | 4 | 15 |
| 225 | Fm-3m |  | 0 | 4 |
| 226 | Fm-3c |  | 1 | 6 |
| 227 | Fd-3m |  | 1 | 10 |
| 228 | Fd-3c |  | 0 | 6 |
| 229 | Im-3m |  | 3 | 15 |
| 230 | Ia-3d |  | 9 | 15 |

## Ranking recipe (all weights explicit, deterministic)

score = 3.0*F + 10.0*[F>20] + 4.0*log2(aut) + 2.0*log2(max stab) + 6.0*[corridor sighting] + 4.0*[sighted in 220 or 230] + 3.0*min(3, #face sizes outside {3,4,6}) + 1.5*log2(1+#sightings) + 1.5*(3 - min stratum dim) + 0.1*V + 5.0*[Schmitt ABSENT-all]. Tie-break: F desc, aut desc, id asc. Weights are triage judgment, not measurements; they are stated so the ranking is reproducible and criticizable.

## Honest limits

- The Schmitt cross-check is F-VECTOR level only (his in-text tables stop there); type-level diligence (canonical-code comparison at his generating points, the schmitt_220_check.py pattern) is a G5 duty for every shortlisted type flagged P. His results storage/14TB data is not recoverable online (SCHMITT_DATA_RECOVERY_2026-08-28.md), so printed tables + our recomputation at his points is the achievable bar.
- The digitized tables are a single-pass visual transcription (Euler- and remark-checked, but not double-keyed). Any G5 verdict that leans on a specific P/A cell must first re-read that printed page.
- A type sighted only at special positions may exist in Schmitt's unprinted data even when flagged A: his table prints one representative point per f-vector and his grid was dense in general position; conversely P does not kill a candidate (different type, same f-vector).
- Aut orders are combinatorial map automorphism counts; geometric stabilizer certification is G4/V2, not claimed. Roundness (the beatable 47.98% benchmark) is NOT computed here — it needs exact metric cells and belongs with the G4 certificate work.
- Features NOT computed: roundness/isoperimetric quotient, geometric symmetry group, polyform counts (G4 Burnside), Wyckoff letter identification for witness points, Engel-1981 cross-check (Tyler-gated, priority recalibrated down), Bernhard Fig. 12 type-level diff (G5 (d)).
- The ranking weights are stated judgment calls; re-ranking under different weights is one `triage_phase1.py` edit away and does not touch the store.
