# TRIAGE result — Phase-2 batch 2 (hexagonal family) MENU-sighted types -> G4 shortlist + collision screen (2026-09-04)

Script: `triage_phase2_hexagonal.py` (deterministic; model `triage_phase2.py`). Store: `phase2_hexagonal_types.json` (Phase-2 batch 2, run 2026-09-04; sha256 verified). Schmitt rows: schmitt_hexagonal_tables.json (text layer + visual cross-read of 153 rows, 2026-09-04). Gates: `../ANCHORS.md` G4 (NOT run here), G5 (NOT run here), KILL CRITERIA.

**LANGUAGE (G5): every type below is "not matched against the records checked as of 2026-09-04". No novelty claim. The Schmitt column is f-vector-level evidence from his printed Sec. 2.2.3-2.2.4 tables (a grid SAMPLING, not an enumeration): "A" = absent there, "P"/"Pb" = present (same f-vector does NOT mean same type), "S-cell" = the type IS one of his printed cells (reproduced at his generating point in pass P2) => excluded from the shortlist by the kill criterion "Schmitt-contains-candidate => reframe to first-realization". COLLISION VERDICT per type: SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed row with that (group, f) reproduced as a DIFFERENT stored type; COLLISION = the type is one of his printed cells (S-cell / SAME); UNRESOLVED = some printed row with that (group, f) did not reproduce (quarantined) so no type-level statement is possible there.**

**SOURCE STATUS of the Schmitt flags: text-layer parse cross-read visually on 153 of 958 rows (0 discrepancies), every row re-derived computationally in pass P2 (f-vector reproduced or quarantined), NOT independently re-keyed (G5 duty still owed) — flags provisional.**

## Sanity duties

- phase2_hexagonal_types.json sha256 7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55: MATCHES phase2_hexagonal_types.SHA256SUMS [raw file present]
- Schmitt hexagonal-family rows: 958 rows over 52 groups from schmitt_hexagonal_tables.json (text layer + visual cross-read of 153 rows, 2026-09-04); Euler on every row: PASS; row count vs _meta 958: MATCH
- Euler V-E+F=2 on all 1583 stored types: ALL PASS
- p-vector consistency (|p|=F, sum p = 2E) on all 1583 types: ALL PASS
- site-stabilizer divides aut on every stored sighting (108534 sightings): ALL PASS
- kill criterion (>38 facets): max stored facet count = 35 (hexagonal types: 34; from our menu: 24): NO HITS
- recount: 891 prior-store + 692 hexagonal = 1583 types; hexagonal split 288 menu-sighted + 404 Schmitt-printed-only; store fields say 891/692/288/404: MATCH
- prior store by system: cubic (phase 1 store): 102, tetragonal (phase 2): 789
- menu/S-only flags consistent with stored pass labels for all 692 hexagonal types: PASS
- quarantines in the store: 46 (schmitt_fvec_mismatch: 46); (group,b) congruence purges: 0; Schmitt screen {"conv_H1": 1085, "conv_H1+zflip": 145, "mismatch": 46, "reproduced": 1230}
- P2 sightings keyed by (group, printed point, b): 1230 stored cells; printed (row x group) evaluations resolved to a stored type: 1230 of 1276

## Headline counts (the 288 menu-sighted hexagonal types)

- Ranked: 288. S-cell: 124; menu-only (never at a printed point): 164.
- Schmitt f-vector flag: ABSENT-all 5; present (P/Pb in >= 1 sighted group) 283; unknown 0.
- COLLISION SCREEN (store-side, all 288 types): SURVIVOR 151, COLLISION 124, UNRESOLVED 13.
- Open/wall label (label only, no perturbation runs): open-likely 214, indeterminate 24, wall-suspect 50.
- Metric-thin: 91 (reasons: 1b 50, P5-only 51).
- Distinct b-ratio histogram (#b: types): 1: 50, 2: 22, 3: 20, 4: 30, 5: 25, 6: 16, 7: 9, 8: 11, 9: 11, 10: 6, 11: 3, 12: 7, 13: 5, 14: 5, 15: 6, 16: 6, 17: 1, 18: 2, 19: 2, 20: 6, 21: 2, 22: 2, 23: 3, 24: 4, 25: 3, 26: 2, 27: 1, 28: 1, 29: 4, 30: 3, 31: 1, 32: 3, 33: 1, 34: 1, 35: 2, 38: 1, 39: 1, 41: 1, 47: 1, 49: 1, 56: 1, 58: 1, 60: 1, 63: 1, 70: 1, 86: 1, 92: 1.
- Facet count: max 24; F >= 20: 41; aut > 1: 135; fixed-point witness (dim 0): 7; line (dim 1): 75; plane (dim 2): 42; general only (dim 3): 164.
- Printed b-ratios swept by our menu: 9 of 38 distinct printed values.

## TOP-15 G4 SHORTLIST (S-cell types excluded; rank in the full table in brackets)

1. `c49077384aaebeb0` [#1] — **178 P6_122** at (1/12, 1/6, 1/4) b=5/4, f=(44, 66, 24), p=3^8 4^2 5^6 6^4 9^2 14^2, aut=2, b-ratios: 15/16, 31/32, 63/64, 79/64, 5/4, 41/32, ... (+6), Schmitt 178:P[other1] 179:P[other1] [score 122.28]  
   24 facets; aut 2; faces incl. 5-gon,9-gon,14-gon; special-position stratum (dim 1, stab 2); 12 b-ratio(s) [coarse, bisect], orbit-b max 4 -> open-likely; 2 group(s), 88 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
2. `59585d778cb3a7a4` [#2] — **178 P6_122** at (1/12, 1/6, 1/4) b=3/4, f=(40, 60, 22), p=3^8 4^4 5^4 6^2 10^2 14^2, aut=2, b-ratios: 17/32, 9/16, 5/8, 21/32, 43/64, 11/16, ... (+16), Schmitt 178:P[other1] 179:P[other1] [score 118.3]  
   22 facets; aut 2; faces incl. 5-gon,10-gon,14-gon; special-position stratum (dim 1, stab 2); 22 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 6 -> open-likely; 2 group(s), 120 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
3. `095ce61d28388c98` [#3] — **178 P6_122** at (1/12, 1/6, 1/4) b=1, f=(40, 60, 22), p=3^6 4^6 6^6 7^2 14^2, aut=2, b-ratios: 23/32, 3/4, 51/64, 13/16, 7/8, 29/32, ... (+18), Schmitt 178:P[other1] 179:P[other1] [score 116.06]  
   22 facets; aut 2; faces incl. 7-gon,14-gon; special-position stratum (dim 1, stab 2); 24 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 6 -> open-likely; 2 group(s), 152 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
4. `9be0f2271a14b6a9` [#4] — **178 P6_122** at (1/8, 1/4, 1/4) b=1, f=(36, 54, 20), p=3^2 4^12 6^2 9^2 12^2, aut=4, b-ratios: 43/64, 11/16, 45/64, 23/32, 3/4, 25/32, ... (+14), Schmitt 178:P[other1] 179:P[other1] [score 112.47]  
   20 facets; aut 4; faces incl. 9-gon,12-gon; special-position stratum (dim 1, stab 2); 20 b-ratio(s) [coarse, bisect], orbit-b max 5 -> open-likely; 2 group(s), 112 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
5. `2d654c836f3731c6` [#5] — **178 P6_122** at (0, 1/8, 1/3) b=1, f=(36, 54, 20), p=3^8 4^2 6^4 7^4 12^2, aut=2, b-ratios: 19/32, 5/8, 21/32, 43/64, 11/16, 45/64, ... (+24), Schmitt 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] [score 111.64]  
   20 facets; aut 2; faces incl. 7-gon,12-gon; special-position stratum (dim 1, stab 2); 30 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 6 -> open-likely; 4 group(s), 178 menu sighting(s); Schmitt f-vec present (169:different, 170:different, 178:different, 179:different); collision verdict SURVIVOR
6. `b0f80776885f3ae1` [#6] — **178 P6_122** at (1/12, 1/6, 1/4) b=1/2, f=(36, 54, 20), p=3^6 4^6 5^2 6^2 8^2 14^2, aut=2, b-ratios: 1/2, 33/64, 527/1000, 5/8, 1277/2000, 21/32, ... (+11), Schmitt 178:P[other1] 179:P[other1] [score 111.48]  
   20 facets; aut 2; faces incl. 5-gon,8-gon,14-gon; special-position stratum (dim 1, stab 2); 17 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 7 -> open-likely; 2 group(s), 140 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
7. `a348875c3f707895` [#7] — **178 P6_122** at (0, 1/12, 1/3) b=1/2, f=(36, 54, 20), p=3^4 4^10 6^2 8^2 14^2, aut=2, b-ratios: 1/2, 1027/2000, 33/64, 2081/4000, 4189/8000, 527/1000, ... (+15), Schmitt 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] [score 110.46]  
   20 facets; aut 2; faces incl. 8-gon,14-gon; special-position stratum (dim 1, stab 2); 21 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 7 -> open-likely; 4 group(s), 166 menu sighting(s); Schmitt f-vec present (169:different, 170:different, 178:different, 179:different); collision verdict SURVIVOR
8. `dcc38ea9177089b9` [#8] — **178 P6_122** at (1/6, 7/12, 1/12) b=1/2, f=(36, 54, 20), p=3^2 4^8 5^2 7^4 8^4, aut=2, b-ratios: 1/2, 527/1000, 1731/3200, Schmitt 178:P[other1] 179:P[other1] [score 101.32]  
   20 facets; aut 2; faces incl. 5-gon,7-gon,8-gon; special-position stratum (dim 1, stab 2); 3 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 3 -> open-likely; 2 group(s), 12 menu sighting(s); Schmitt f-vec present (178:different, 179:different); collision verdict SURVIVOR
9. `3d920f206ca7a132` [#9] — **180 P6_222** at (1/8, 1/6, 5/12) b=1/2, f=(42, 63, 23), p=3^4 4^12 6^3 8^2 14^1 18^1, aut=1, b-ratios: 1/2, 527/1000, 2331/4000, Schmitt 180:P[unres1] [score 98.37]  
   23 facets; faces incl. 8-gon,14-gon,18-gon; general position only; 3 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 3 -> open-likely; 1 group(s), 3 menu sighting(s); Schmitt f-vec present (180:unresolved); collision verdict UNRESOLVED
10. `5b86a254c715306c` [#10] — **169 P6_1** at (1/12, 3/8, 1/6) b=797/1000, f=(40, 60, 22), p=3^8 4^6 6^4 10^2 14^2, aut=1, b-ratios: 6047/8000, 3047/4000, 1547/2000, 797/1000, 4/5, 131/160, Schmitt 169:Pb[other1] 170:Pb[other1] [score 97.72]  
   22 facets; faces incl. 10-gon,14-gon; general position only; 6 b-ratio(s) [schmittb, bisect], orbit-b max 6 -> open-likely; 2 group(s), 12 menu sighting(s); Schmitt f-vec present (169:different, 170:different); collision verdict SURVIVOR
11. `f05f0b009e0929f6` [#11] — **169 P6_1** at (1/8, 1/6, 5/12) b=3/4, f=(32, 48, 18), p=3^2 4^6 5^6 6^2 12^2, aut=2, b-ratios: 1/2, 1681/3200, 527/1000, 17/32, 9/16, 37/64, ... (+33), Schmitt 169:Pb[other1] 170:Pb[other1] 178:P[other1] 179:P[other1] [score 97.05]  
   18 facets; aut 2; faces incl. 5-gon,12-gon; special-position stratum (dim 1, stab 2); 39 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 8 -> open-likely; 4 group(s), 290 menu sighting(s); Schmitt f-vec present (169:different, 170:different, 178:different, 179:different); collision verdict SURVIVOR
12. `b24fc960c48a9c3c` [#12] — **180 P6_222** at (1/8, 1/6, 5/12) b=977/1600, f=(44, 66, 24), p=3^6 4^8 5^4 6^1 8^3 14^1 18^1, aut=1, b-ratios: 9547/16000, 977/1600, Schmitt 180:P[unres1] [score 95.78]  
   24 facets; faces incl. 5-gon,8-gon,14-gon,18-gon; general position only; 2 b-ratio(s) [bisect], orbit-b max 2 -> indeterminate; 1 group(s), 2 menu sighting(s); METRIC-THIN (P5-only); Schmitt f-vec present (180:unresolved); collision verdict UNRESOLVED
13. `d70e6901953070e7` [#13] — **155 R32** at (1/8, 1/6, 5/12) b=3/4, f=(38, 58, 22), p=3^6 4^8 6^3 7^2 8^1 10^1 16^1, aut=1, b-ratios: 11777/16000, 3/4, 12047/16000, Schmitt 155:P[other1] [score 94.97]  
   22 facets; faces incl. 7-gon,8-gon,10-gon,16-gon; general position only; 3 b-ratio(s) [coarse, bisect], orbit-b max 3 -> open-likely; 1 group(s), 3 menu sighting(s); Schmitt f-vec present (155:different); collision verdict SURVIVOR
14. `e1a38303b2378f17` [#14] — **169 P6_1** at (1/8, 1/6, 5/12) b=1277/2000, f=(40, 60, 22), p=3^8 4^6 6^2 7^2 8^2 15^2, aut=1, b-ratios: 9993/16000, 1277/2000, 5331/8000, 2177/3200, Schmitt 169:P[other1] 170:P[other1] [score 94.75]  
   22 facets; faces incl. 7-gon,8-gon,15-gon; general position only; 4 b-ratio(s) [bisect], orbit-b max 4 -> open-likely; 2 group(s), 8 menu sighting(s); METRIC-THIN (P5-only); Schmitt f-vec present (169:different, 170:different); collision verdict SURVIVOR
15. `c82ebc15c49c1413` [#15] — **154 P3_221** at (1/8, 1/6, 5/12) b=527/1000, f=(38, 57, 21), p=3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1, aut=1, b-ratios: 8351/16000, 4189/8000, 527/1000, 4439/8000, 9101/16000, Schmitt 154:P[other1] [score 94.32]  
   21 facets; faces incl. 5-gon,9-gon,10-gon,12-gon,14-gon; general position only; 5 b-ratio(s) [schmittb, bisect], orbit-b max 5 -> open-likely; 1 group(s), 5 menu sighting(s); Schmitt f-vec present (154:different); collision verdict SURVIVOR

## COLLISION-SCREEN SURVIVORS (151 of 288; top 10 shown, all in the full table)

| # | id | witness group | c/a (b) | f-vector | p-vector | aut | #b | O/W label | Schmitt per group |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 P6_122 (1/12, 1/6, 1/4) | 5/4 | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 12 | open-likely | 178:P[other1] 179:P[other1] |
| 2 | `59585d778cb3a7a4` | 178 P6_122 (1/12, 1/6, 1/4) | 3/4 | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 22 | open-likely | 178:P[other1] 179:P[other1] |
| 3 | `095ce61d28388c98` | 178 P6_122 (1/12, 1/6, 1/4) | 1 | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 24 | open-likely | 178:P[other1] 179:P[other1] |
| 4 | `9be0f2271a14b6a9` | 178 P6_122 (1/8, 1/4, 1/4) | 1 | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 20 | open-likely | 178:P[other1] 179:P[other1] |
| 5 | `2d654c836f3731c6` | 178 P6_122 (0, 1/8, 1/3) | 1 | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 30 | open-likely | 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] |
| 6 | `b0f80776885f3ae1` | 178 P6_122 (1/12, 1/6, 1/4) | 1/2 | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 17 | open-likely | 178:P[other1] 179:P[other1] |
| 7 | `a348875c3f707895` | 178 P6_122 (0, 1/12, 1/3) | 1/2 | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 21 | open-likely | 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] |
| 8 | `dcc38ea9177089b9` | 178 P6_122 (1/6, 7/12, 1/12) | 1/2 | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 3 | open-likely | 178:P[other1] 179:P[other1] |
| 9 | `5b86a254c715306c` | 169 P6_1 (1/12, 3/8, 1/6) | 797/1000 | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 6 | open-likely | 169:Pb[other1] 170:Pb[other1] |
| 10 | `f05f0b009e0929f6` | 169 P6_1 (1/8, 1/6, 5/12) | 3/4 | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 39 | open-likely | 169:Pb[other1] 170:Pb[other1] 178:P[other1] 179:P[other1] |

## Collision worklist for the top-10 survivors (recomputed independently by collision_phase2_hex_check.py)

Every printed row of a sighted group with the survivor's f-vector; P2 outcome from the store (`other` = a different stored type, id given; `unres` cannot occur for a survivor by definition).

| # | id | group | f-vector | printed b | printed point (B'') | PDF p. | P2 outcome |
|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 P6_122 | (44, 66, 24) | 797/1000 | (56/125, -14/125, 0) | 114 | other `7069f26515a08a42` |
| 1 | `c49077384aaebeb0` | 179 P6_522 | (44, 66, 24) | 797/1000 | (56/125, -14/125, 0) | 114 | other `7069f26515a08a42` |
| 2 | `59585d778cb3a7a4` | 178 P6_122 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | other `b7e607ffe0fdc6a6` |
| 2 | `59585d778cb3a7a4` | 179 P6_522 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | other `b7e607ffe0fdc6a6` |
| 3 | `095ce61d28388c98` | 178 P6_122 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | other `b7e607ffe0fdc6a6` |
| 3 | `095ce61d28388c98` | 179 P6_522 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | other `b7e607ffe0fdc6a6` |
| 4 | `9be0f2271a14b6a9` | 178 P6_122 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 4 | `9be0f2271a14b6a9` | 179 P6_522 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 5 | `2d654c836f3731c6` | 169 P6_1 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | other `04a532437a590239` |
| 5 | `2d654c836f3731c6` | 170 P6_5 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | other `04a532437a590239` |
| 5 | `2d654c836f3731c6` | 178 P6_122 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 5 | `2d654c836f3731c6` | 179 P6_522 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 6 | `b0f80776885f3ae1` | 178 P6_122 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 6 | `b0f80776885f3ae1` | 179 P6_522 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 7 | `a348875c3f707895` | 169 P6_1 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | other `04a532437a590239` |
| 7 | `a348875c3f707895` | 170 P6_5 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | other `04a532437a590239` |
| 7 | `a348875c3f707895` | 178 P6_122 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 7 | `a348875c3f707895` | 179 P6_522 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 8 | `dcc38ea9177089b9` | 178 P6_122 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 8 | `dcc38ea9177089b9` | 179 P6_522 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | other `b3a4321d9c054113` |
| 9 | `5b86a254c715306c` | 169 P6_1 | (40, 60, 22) | 797/1000 | (1/4, 685/3996, 0) | 108 | other `ed6e6228fdbafd09` |
| 9 | `5b86a254c715306c` | 170 P6_5 | (40, 60, 22) | 797/1000 | (1/4, 685/3996, 0) | 108 | other `ed6e6228fdbafd09` |
| 10 | `f05f0b009e0929f6` | 169 P6_1 | (32, 48, 18) | 797/1000 | (1595/5994, 403/1998, 0) | 108 | other `f94c2ae7de04a72e` |
| 10 | `f05f0b009e0929f6` | 170 P6_5 | (32, 48, 18) | 797/1000 | (1595/5994, 403/1998, 0) | 108 | other `f94c2ae7de04a72e` |
| 10 | `f05f0b009e0929f6` | 178 P6_122 | (32, 48, 18) | 3497/1000 | (19/50, 19/50, 19/300) | 113 | other `3bb4e5b783529bc7` |
| 10 | `f05f0b009e0929f6` | 179 P6_522 | (32, 48, 18) | 3497/1000 | (19/50, 19/50, 19/300) | 113 | other `3bb4e5b783529bc7` |

## Full ranked table (all 288 menu-sighted hexagonal types)

witness = first MENU sighting (group, point, b); stab = max site-stabilizer over menu sightings; dim = min stratum; #b = distinct b-ratios (menu); ob = max distinct b on one orbit; sgt = menu sightings; grp = groups sighted; S = S-cell (P2 sightings count); thin; O/W label; Schmitt = per-group flag with P-resolution [same/other/unres]; verdict = collision-screen verdict.

| rank | id | f-vector | p-vector | aut | witness | stab | dim | #b | ob | sgt | grp | S | thin | O/W | Schmitt | verdict | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | (44, 66, 24) | 3^8 4^2 5^6 6^4 9^2 14^2 | 2 | 178 P6_122 (1/12,1/6,1/4) b=5/4 | 2 | 1 | 12 | 4 | 88 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 122.28 |
| 2 | `59585d778cb3a7a4` | (40, 60, 22) | 3^8 4^4 5^4 6^2 10^2 14^2 | 2 | 178 P6_122 (1/12,1/6,1/4) b=3/4 | 2 | 1 | 22 | 6 | 120 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 118.3 |
| 3 | `095ce61d28388c98` | (40, 60, 22) | 3^6 4^6 6^6 7^2 14^2 | 2 | 178 P6_122 (1/12,1/6,1/4) b=1 | 2 | 1 | 24 | 6 | 152 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 116.06 |
| 4 | `9be0f2271a14b6a9` | (36, 54, 20) | 3^2 4^12 6^2 9^2 12^2 | 4 | 178 P6_122 (1/8,1/4,1/4) b=1 | 2 | 1 | 20 | 5 | 112 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 112.47 |
| 5 | `2d654c836f3731c6` | (36, 54, 20) | 3^8 4^2 6^4 7^4 12^2 | 2 | 178 P6_122 (0,1/8,1/3) b=1 | 2 | 1 | 30 | 6 | 178 | 4 |  |  | open-likely | 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] | SURVIVOR | 111.64 |
| 6 | `b0f80776885f3ae1` | (36, 54, 20) | 3^6 4^6 5^2 6^2 8^2 14^2 | 2 | 178 P6_122 (1/12,1/6,1/4) b=1/2 | 2 | 1 | 17 | 7 | 140 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 111.48 |
| 7 | `a348875c3f707895` | (36, 54, 20) | 3^4 4^10 6^2 8^2 14^2 | 2 | 178 P6_122 (0,1/12,1/3) b=1/2 | 2 | 1 | 21 | 7 | 166 | 4 |  |  | open-likely | 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] | SURVIVOR | 110.46 |
| 8 | `dcc38ea9177089b9` | (36, 54, 20) | 3^2 4^8 5^2 7^4 8^4 | 2 | 178 P6_122 (1/6,7/12,1/12) b=1/2 | 2 | 1 | 3 | 3 | 12 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 101.32 |
| 9 | `3d920f206ca7a132` | (42, 63, 23) | 3^4 4^12 6^3 8^2 14^1 18^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 180:P[unres1] | UNRESOLVED | 98.37 |
| 10 | `5b86a254c715306c` | (40, 60, 22) | 3^8 4^6 6^4 10^2 14^2 | 1 | 169 P6_1 (1/12,3/8,1/6) b=797/1000 | 1 | 3 | 6 | 6 | 12 | 2 |  |  | open-likely | 169:Pb[other1] 170:Pb[other1] | SURVIVOR | 97.72 |
| 11 | `f05f0b009e0929f6` | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 2 | 169 P6_1 (1/8,1/6,5/12) b=3/4 | 2 | 1 | 39 | 8 | 290 | 4 |  |  | open-likely | 169:Pb[other1] 170:Pb[other1] 178:P[other1] 179:P[other1] | SURVIVOR | 97.05 |
| 12 | `b24fc960c48a9c3c` | (44, 66, 24) | 3^6 4^8 5^4 6^1 8^3 14^1 18^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=977/1600 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 180:P[unres1] | UNRESOLVED | 95.78 |
| 13 | `d70e6901953070e7` | (38, 58, 22) | 3^6 4^8 6^3 7^2 8^1 10^1 16^1 | 1 | 155 R32 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 155:P[other1] | SURVIVOR | 94.97 |
| 14 | `e1a38303b2378f17` | (40, 60, 22) | 3^8 4^6 6^2 7^2 8^2 15^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=1277/2000 | 1 | 3 | 4 | 4 | 8 | 2 |  | P5-only | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 94.75 |
| 15 | `c82ebc15c49c1413` | (38, 57, 21) | 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=527/1000 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 154:P[other1] | SURVIVOR | 94.32 |
| 16 | `f6f8b3050a1eef42` | (38, 57, 21) | 3^4 4^11 6^2 10^2 12^1 14^1 | 1 | 178 P6_122 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 94.32 |
| 17 | `9c0b7e0c29dfebb2` | (36, 54, 20) | 3^4 4^8 5^2 7^4 13^2 | 1 | 169 P6_1 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 10 | 2 |  |  | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 93.43 |
| 18 | `87c94384d7851cb2` | (34, 52, 20) | 3^4 4^6 5^2 6^6 8^1 14^1 | 1 | 155 R32 (1/8,1/6,5/12) b=797/1000 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 155:Pb[other1] | SURVIVOR | 93.15 |
| 19 | `a35623e347ef03b4` | (32, 48, 18) | 4^10 6^6 10^2 | 2 | 169 P6_1 (1/8,1/6,5/12) b=5/4 | 2 | 1 | 32 | 7 | 246 | 4 |  |  | open-likely | 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] | SURVIVOR | 93.12 |
| 20 | `54ec9db30372ac68` | (38, 57, 21) | 3^6 4^7 6^4 8^2 14^2 | 1 | 180 P6_222 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 180:P[unres1] | UNRESOLVED | 92.91 |
| 21 | `e98412e7cb95aea2` | (32, 48, 18) | 3^4 4^6 6^2 8^6 | 2 | 152 P3_121 (0,1/8,1/6) b=3/4 | 2 | 1 | 30 | 7 | 272 | 2 |  |  | open-likely | 152:P[other1] 154:P[other1] | SURVIVOR | 92.15 |
| 22 | `261f28c9d7f6135a` | (36, 54, 20) | 3^4 4^8 6^4 8^1 10^2 12^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 180:P[unres1] | UNRESOLVED | 91.98 |
| 23 | `ac4489d658eb445e` | (36, 54, 20) | 4^13 5^2 6^1 9^2 10^1 12^1 | 1 | 178 P6_122 (1/12,3/8,1/6) b=797/1000 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 91.98 |
| 24 | `c53bc05bc306c97d` | (31, 48, 19) | 3^4 4^8 5^4 8^2 16^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=7/8 | 2 | 2 | 14 | 9 | 28 | 1 |  |  | open-likely | 166:P[other1] | SURVIVOR | 91.5 |
| 25 | `8cc8c5ab3cf36d8f` | (36, 54, 20) | 3^6 4^4 5^4 6^2 9^2 10^1 14^1 | 1 | 178 P6_122 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 91.12 |
| 26 | `364e84ece2d20d22` | (34, 51, 19) | 3^2 4^11 6^2 10^4 | 2 | 152 P3_121 (1/8,1/6,5/12) b=1 | 2 | 1 | 14 | 5 | 59 | 3 |  |  | open-likely | 152:P[other1] 180:P[unres1] 181:P[other1] | UNRESOLVED | 90.46 |
| 27 | `646b518ccf3bd724` | (36, 54, 20) | 3^6 4^4 5^2 6^4 7^2 13^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=15/16 | 1 | 3 | 6 | 4 | 12 | 2 |  | P5-only | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 90.32 |
| 28 | `7a448bed1119dfad` | (36, 54, 20) | 3^2 4^10 5^2 6^2 8^2 12^2 | 1 | 178 P6_122 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 90.08 |
| 29 | `7e023be581e7c50a` | (36, 54, 20) | 3^6 4^6 6^2 8^4 10^1 12^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 154:P[other1] | SURVIVOR | 90.08 |
| 30 | `dd68dc31f1bba1af` | (40, 60, 22) | 3^8 4^7 6^2 8^1 10^1 12^2 14^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=49/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 180:P[unres1] | UNRESOLVED | 89.38 |
| 31 | `303d3c41bbb6461d` | (30, 45, 17) | 3^4 4^3 5^2 6^4 8^4 | 2 | 178 P6_122 (1/12,3/8,1/6) b=2 | 2 | 1 | 20 | 9 | 86 | 4 |  |  | open-likely | 152:P[other1] 178:P[other1] 180:P[unres1] 181:P[other1] | UNRESOLVED | 89.31 |
| 32 | `7e05ce00d8a7cbf6` | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 178 P6_122 (1/12,3/8,1/6) b=137/160 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 178:P[other1] | SURVIVOR | 89.28 |
| 33 | `59b28b3a59c27092` | (34, 52, 20) | 3^8 4^2 5^2 6^4 8^3 14^1 | 1 | 155 R32 (1/8,1/6,5/12) b=1277/2000 | 1 | 3 | 6 | 6 | 6 | 1 |  | P5-only | open-likely | 155:P[other1] | SURVIVOR | 87.78 |
| 34 | `d9ac68100a276dfe` | (36, 54, 20) | 3^4 4^6 5^4 6^2 7^2 13^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=2777/4000 | 1 | 3 | 3 | 3 | 6 | 2 |  | P5-only | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 86.98 |
| 35 | `6f4101f83371033d` | (36, 54, 20) | 3^4 4^8 6^4 7^2 13^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=2331/4000 | 1 | 3 | 4 | 4 | 8 | 2 |  | P5-only | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 85.35 |
| 36 | `f0b07b168368759b` | (14, 24, 12) | 3^4 4^4 5^4 | 4 | 148 R-3 (0,1/2,0) b=3/4 | 4 | 0 | 41 | 10 | 1168 | 5 |  |  | open-likely | 148:P[other1] 155:P[other1] 160:P[other1] 166:P[other1] 167:P[other1] | SURVIVOR | 85.22 |
| 37 | `56918d2cff883e22` | (22, 34, 14) | 4^8 5^2 6^2 7^2 | 2 | 148 R-3 (1/8,1/6,5/12) b=1 | 2 | 1 | 49 | 16 | 183 | 3 |  |  | open-likely | 148:P[other1] 161:P[other1] 167:P[other1] | SURVIVOR | 83.3 |
| 38 | `8126183cde7ea2f3` | (36, 54, 20) | 3^6 4^7 6^1 8^3 10^2 12^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=25/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 180:P[unres1] | UNRESOLVED | 82.98 |
| 39 | `f429e996b3f455a6` | (26, 40, 16) | 3^6 5^6 8^4 | 2 | 148 R-3 (1/8,1/6,5/12) b=3/4 | 2 | 1 | 16 | 7 | 41 | 2 |  |  | open-likely | 148:Pb[other1] 167:P[other1] | SURVIVOR | 82.69 |
| 40 | `71d2c9953ca110b8` | (36, 54, 20) | 3^4 4^2 5^8 6^2 7^2 11^2 | 1 | 169 P6_1 (1/12,3/8,1/6) b=39/32 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 169:P[other1] 170:P[other1] | SURVIVOR | 81.98 |
| 41 | `8d90c524c89922d9` | (36, 54, 20) | 3^4 4^4 5^4 6^4 7^2 11^2 | 1 | 169 P6_1 (1/12,3/8,1/6) b=11/8 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 169:P[other1] 170:P[other1] | SURVIVOR | 81.98 |
| 42 | `ff65c54d78bb4e50` | (34, 52, 20) | 3^4 4^9 5^4 10^2 16^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=3/4 | 2 | 2 | 15 | 8 | 32 | 3 | 3 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] | COLLISION | 81.87 |
| 43 | `1db3ca5e82f8746f` | (31, 48, 19) | 3^6 4^3 5^6 6^1 10^3 | 6 | 148 R-3 (0,0,1/12) b=3/2 | 6 | 1 | 22 | 7 | 110 | 4 | 1 |  | open-likely | 148:P[other1] 155:P[other1] 166:P[other1] 167:Pb[same1] | COLLISION | 80.72 |
| 44 | `5a0120ccceb4ecc4` | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 180 P6_222 (1/4,1/2,0) b=5/4 | 2 | 1 | 15 | 7 | 60 | 2 |  |  | open-likely | 180:P[unres1] 181:P[other1] | UNRESOLVED | 80.51 |
| 45 | `9d4396ca0b08fc3c` | (19, 30, 13) | 4^8 5^4 8^1 | 2 | 166 R-3m (1/24,1/12,1/12) b=3/4 | 2 | 2 | 63 | 15 | 381 | 2 |  |  | open-likely | 166:P[other1] 167:P[other1] | SURVIVOR | 80.22 |
| 46 | `07d543d89e2934f2` | (36, 54, 20) | 3^6 4^4 5^2 6^4 10^4 | 1 | 152 P3_121 (1/8,1/6,5/12) b=33/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 152:P[other1] | SURVIVOR | 79.98 |
| 47 | `1a36f90bbc759307` | (28, 42, 16) | 4^8 5^4 8^4 | 4 | 151 P3_112 (0,1/2,0) b=1/2 | 4 | 0 | 58 | 14 | 1570 | 14 | 6 |  | open-likely | 144:Pb[same1] 145:Pb[same1] 151:Pb[same1] 152:P[other1] 153:Pb[same1] 154:P[other1] 169:Pb[same1] 170:Pb[same1] 171:P[other1] 172:P[other1] 178:P[other1] 179:P[other1] 180:P[unres1] 181:P[other1] | COLLISION | 79.75 |
| 48 | `76108b085b4e40f8` | (18, 30, 14) | 3^8 6^6 | 12 | 147 P-3 (1/3,2/3,1/12) b=1/2 | 12 | 0 | 92 | 19 | 2892 | 25 | 21 |  | open-likely | 147:Pb[same1] 148:Pb[same1] 149:Pb[same1] 150:Pb[same1] 158:Pb[same1] 159:P[other1] 161:Pb[same1] 162:Pb[same1] 163:Pb[same1] 164:Pb[same1] 165:Pb[same1] 167:Pb[same1] 169:Pb[same1] 170:Pb[same1] 173:Pb[same1] 176:Pb[same1] 178:Pb[other1] 179:Pb[other1] 182:Pb[same1] 185:Pb[same1] 186:Pb[same1] 188:Pb[same1] 190:P[other1] 193:Pb[same1] 194:Pb[same1] | COLLISION | 79.75 |
| 49 | `2081d7b9a734e4fe` | (32, 50, 20) | 3^6 4^4 5^4 6^4 10^1 12^1 | 1 | 155 R32 (1/8,1/6,5/12) b=11/8 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 155:P[other1] | SURVIVOR | 79.7 |
| 50 | `257b627a90b78038` | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 180 P6_222 (1/6,7/12,1/6) b=1 | 2 | 1 | 24 | 11 | 112 | 2 |  |  | open-likely | 180:P[other1] 181:P[other1] | SURVIVOR | 79.6 |
| 51 | `1b1288f460af270d` | (38, 58, 22) | 3^8 4^8 6^3 12^2 18^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=1/2 | 2 | 2 | 5 | 4 | 12 | 2 | 2 |  | open-likely | 166:Pb[same1] 167:Pb[same1] | COLLISION | 79.49 |
| 52 | `3ddc41389e6d484f` | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 9^2 10^1 | 1 | 171 P6_2 (1/8,1/6,5/12) b=1 | 1 | 3 | 8 | 5 | 16 | 2 |  |  | open-likely | 171:P[other1] 172:P[other1] | SURVIVOR | 79.33 |
| 53 | `64203f15fcf6c09b` | (20, 32, 14) | 3^4 4^4 5^2 6^2 7^2 | 2 | 155 R32 (0,1/24,0) b=1/2 | 2 | 1 | 23 | 9 | 180 | 1 |  |  | open-likely | 155:Pb[other1] | SURVIVOR | 79.3 |
| 54 | `d718e083bd23d2b1` | (32, 48, 18) | 4^13 8^4 12^1 | 4 | 178 P6_122 (1/12,3/8,1/6) b=1 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 78.68 |
| 55 | `f14a8c4e7c5b3e3a` | (32, 48, 18) | 3^6 4^2 5^2 6^4 8^2 10^2 | 1 | 180 P6_222 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 10 | 10 | 10 | 1 |  |  | open-likely | 180:Pb[other1] | SURVIVOR | 78.03 |
| 56 | `f593cb348adf804b` | (31, 48, 19) | 3^12 6^1 8^3 10^3 | 6 | 148 R-3 (0,0,5/24) b=9/4 | 6 | 1 | 12 | 12 | 72 | 3 | 3 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] | COLLISION | 77.65 |
| 57 | `29bbba1adec778da` | (28, 42, 16) | 3^2 4^4 5^4 6^3 7^2 10^1 | 1 | 171 P6_2 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 15 | 13 | 50 | 2 |  |  | open-likely | 171:Pb[other1] 172:Pb[other1] | SURVIVOR | 77.12 |
| 58 | `66563d07a1110a25` | (36, 54, 20) | 3^8 4^2 6^5 8^2 10^3 | 1 | 154 P3_221 (1/8,1/6,5/12) b=1 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 154:P[other1] | SURVIVOR | 77.1 |
| 59 | `ce3b42c8a4ceff6f` | (34, 51, 19) | 3^6 4^6 6^2 8^3 12^2 | 1 | 151 P3_112 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 6 | 4 | 7 | 2 |  |  | open-likely | 151:P[other1] 153:P[other1] | SURVIVOR | 77.07 |
| 60 | `7b9cfe26fe4a9c4b` | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 146 R3 (1/8,1/6,5/12) b=5/4 | 2 | 1 | 32 | 18 | 434 | 2 |  |  | open-likely | 146:Pb[other1] 155:Pb[other1] | SURVIVOR | 76.95 |
| 61 | `1f08da5f6863d52a` | (34, 51, 19) | 3^2 4^8 5^4 6^2 8^1 12^2 | 1 | 180 P6_222 (1/8,1/6,5/12) b=797/1000 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 180:P[unres1] | UNRESOLVED | 76.88 |
| 62 | `2b9726574a0a8bed` | (30, 45, 17) | 3^4 4^4 5^2 6^1 7^4 9^2 | 1 | 171 P6_2 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 9 | 5 | 18 | 2 |  |  | open-likely | 171:Pb[other1] 172:Pb[other1] | SURVIVOR | 76.71 |
| 63 | `f07d69523ef41b37` | (20, 36, 18) | 3^10 4^4 5^2 8^2 | 2 | 178 P6_122 (1/6,1/3,1/4) b=3/2 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 178:A 179:A | SURVIVOR | 76.48 |
| 64 | `0fef47b559fef709` | (14, 24, 12) | 4^12 | 12 | 147 P-3 (1/3,2/3,1/12) b=7/4 | 12 | 0 | 86 | 20 | 11072 | 25 | 20 |  | open-likely | 147:Pb[same1] 148:Pb[other1] 149:Pb[same1] 150:Pb[same1] 158:Pb[same1] 159:Pb[same1] 161:Pb[other1] 162:Pb[same1] 163:Pb[same1] 164:Pb[same1] 165:Pb[same1] 167:Pb[other1] 169:Pb[same1] 170:Pb[same1] 173:Pb[same1] 176:Pb[same1] 178:A 179:A 182:Pb[same1] 185:Pb[same1] 186:Pb[same1] 188:Pb[same1] 190:Pb[same1] 193:Pb[same1] 194:Pb[same1] | COLLISION | 76.06 |
| 65 | `16025e0680843c36` | (32, 48, 18) | 3^2 4^4 5^8 6^2 11^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=1 | 1 | 3 | 7 | 4 | 16 | 2 |  |  | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 75.95 |
| 66 | `d10bb4a25bbf4c80` | (32, 48, 18) | 3^6 4^2 5^4 7^2 8^2 10^2 | 1 | 154 P3_221 (1/8,1/6,5/12) b=797/1000 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 154:P[other1] | SURVIVOR | 75.58 |
| 67 | `e0bf1a48f096c10d` | (32, 48, 18) | 4^8 5^6 6^2 10^1 12^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 180:P[other1] | SURVIVOR | 75.58 |
| 68 | `b2430fc4bea4e06d` | (34, 51, 19) | 3^8 4^2 5^2 6^2 8^3 12^2 | 1 | 154 P3_221 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 154:P[other1] | SURVIVOR | 75.57 |
| 69 | `bff9b24ce78050f5` | (28, 42, 16) | 4^8 5^4 8^4 | 2 | 144 P3_1 (1/8,1/6,5/12) b=1 | 1 | 3 | 9 | 5 | 18 | 4 |  |  | open-likely | 144:P[other1] 145:P[other1] 169:P[other1] 170:P[other1] | SURVIVOR | 75.51 |
| 70 | `4db369a636f4396b` | (18, 30, 14) | 3^4 4^6 6^4 | 4 | 151 P3_112 (0,1/2,0) b=3/2 | 4 | 0 | 2 | 1 | 74 | 10 |  |  | indeterminate | 151:P[other1] 152:A 153:P[other1] 154:A 171:P[other1] 172:P[other1] 178:P[other1] 179:P[other1] 180:P[other1] 181:P[other1] | SURVIVOR | 74.97 |
| 71 | `042c19cbfdc869cb` | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^2 8^3 10^1 | 1 | 178 P6_122 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 74.72 |
| 72 | `23594bd7053503aa` | (32, 48, 18) | 3^6 4^2 5^2 6^3 7^2 8^1 10^2 | 1 | 153 P3_212 (1/8,1/6,5/12) b=1 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 153:P[other1] | SURVIVOR | 74.72 |
| 73 | `f5fbebffa76808d5` | (31, 47, 18) | 3^3 4^2 5^7 6^3 7^2 10^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 74.62 |
| 74 | `057255f61286b052` | (24, 38, 16) | 3^6 4^2 6^6 7^2 | 2 | 167 R-3c (0,3/8,1/4) b=1/2 | 2 | 1 | 7 | 4 | 18 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 74.39 |
| 75 | `e198aac88f223892` | (30, 45, 17) | 3^2 4^5 5^4 6^4 10^2 | 1 | 153 P3_212 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 7 | 13 | 2 |  |  | open-likely | 151:P[other1] 153:P[other1] | SURVIVOR | 73.88 |
| 76 | `d07f950b8309de82` | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 2 | 171 P6_2 (1/8,1/6,5/12) b=67/80 | 1 | 3 | 5 | 5 | 10 | 2 |  | P5-only | open-likely | 171:P[other1] 172:P[other1] | SURVIVOR | 73.83 |
| 77 | `a182e87006c7a00d` | (32, 48, 18) | 3^6 4^1 5^2 6^3 7^2 8^4 | 1 | 179 P6_522 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 73.68 |
| 78 | `a46cbaad3c23e834` | (32, 49, 19) | 3^4 4^8 5^2 6^2 8^1 10^1 14^1 | 1 | 155 R32 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 155:P[other1] | SURVIVOR | 73.58 |
| 79 | `dd3fb07fe11d73d3` | (31, 47, 18) | 3^4 4^7 6^3 7^2 10^1 12^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 73.58 |
| 80 | `36c92427e3d084dc` | (19, 30, 13) | 3^4 4^4 5^2 7^2 8^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=5/4 | 2 | 2 | 16 | 9 | 34 | 1 |  |  | open-likely | 166:P[other1] | SURVIVOR | 73.09 |
| 81 | `bc59e5d778f60d1f` | (29, 44, 17) | 3^3 4^6 5^3 6^2 9^2 10^1 | 1 | 178 P6_122 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 73.01 |
| 82 | `cbead3df2d2f1d0e` | (34, 51, 19) | 3^2 4^11 6^1 8^3 10^1 12^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=1277/2000 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 154:P[other1] | SURVIVOR | 72.88 |
| 83 | `85244add8d1f2d55` | (32, 48, 18) | 3^2 4^6 5^6 6^2 12^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 10 | 2 |  |  | open-likely | 169:P[other1] 170:P[other1] | SURVIVOR | 72.56 |
| 84 | `2165f5c5260120de` | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 152 P3_121 (1/8,1/6,5/12) b=527/1000 | 1 | 3 | 5 | 4 | 5 | 2 |  |  | open-likely | 152:P[other1] 154:P[other1] | SURVIVOR | 72.52 |
| 85 | `437fbe758a6dd8e3` | (32, 48, 18) | 3^4 4^6 5^2 6^2 8^1 10^3 | 1 | 179 P6_522 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 72.37 |
| 86 | `36ec4ad2f530e145` | (30, 45, 17) | 3^2 4^6 6^7 8^1 10^1 | 1 | 151 P3_112 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 6 | 9 | 2 |  |  | open-likely | 151:P[other1] 153:P[other1] | SURVIVOR | 72.32 |
| 87 | `b3d52575f76a33bd` | (34, 53, 21) | 3^8 4^6 6^4 7^2 20^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=63/64 | 2 | 2 | 5 | 3 | 10 | 2 | 2 | P5-only | open-likely | 148:Pb[same1] 166:Pb[same1] | COLLISION | 71.73 |
| 88 | `fcffad0da2b5b62f` | (32, 48, 18) | 3^4 4^4 5^2 6^3 7^2 8^2 10^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=15/16 | 1 | 3 | 6 | 6 | 6 | 1 |  | P5-only | open-likely | 154:P[other1] | SURVIVOR | 71.58 |
| 89 | `505a4911e298c933` | (28, 42, 16) | 3^2 4^6 6^6 8^1 10^1 | 2 | 181 P6_422 (1/8,1/6,5/12) b=2 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 181:Pb[other1] | SURVIVOR | 71.55 |
| 90 | `24a6b511067d37b2` | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 178 P6_122 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 5 | 3 | 5 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 71.52 |
| 91 | `30f2a1e483babf55` | (29, 44, 17) | 3^4 4^5 5^2 6^1 7^2 8^1 9^2 | 1 | 178 P6_122 (1/12,3/8,1/6) b=11/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 178:Pb[other1] | SURVIVOR | 71.42 |
| 92 | `37aa18e6e10583be` | (30, 47, 19) | 3^6 4^5 5^2 6^3 8^1 10^2 | 1 | 155 R32 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 155:P[other1] | SURVIVOR | 71.17 |
| 93 | `7715c7010e513b71` | (30, 45, 17) | 4^10 6^4 8^2 10^1 | 1 | 181 P6_422 (1/8,1/6,5/12) b=1 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 181:P[other1] | SURVIVOR | 70.75 |
| 94 | `0b5d9beb0fc972f6` | (32, 48, 18) | 3^2 4^5 5^6 6^1 8^3 10^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=13/8 | 1 | 3 | 5 | 5 | 5 | 1 |  | P5-only | open-likely | 179:P[other1] | SURVIVOR | 70.72 |
| 95 | `322d5ff451e4101d` | (32, 48, 18) | 3^2 4^6 5^4 6^2 7^2 10^2 | 1 | 169 P6_1 (1/8,1/6,5/12) b=11/8 | 1 | 3 | 3 | 2 | 6 | 2 |  | P5-only | indeterminate | 169:P[other1] 170:P[other1] | SURVIVOR | 70.58 |
| 96 | `34351050a4f29035` | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 178 P6_122 (1/8,1/6,5/12) b=1 | 1 | 3 | 11 | 6 | 14 | 2 |  |  | open-likely | 178:P[other1] 179:P[other1] | SURVIVOR | 70.58 |
| 97 | `c0071756347c5a8a` | (28, 42, 16) | 3^2 4^4 5^4 7^6 | 1 | 144 P3_1 (1/12,3/8,1/6) b=1 | 1 | 3 | 9 | 5 | 18 | 2 |  |  | open-likely | 144:P[other1] 145:P[other1] | SURVIVOR | 70.51 |
| 98 | `d9bf7fb7a80eaa38` | (30, 47, 19) | 3^4 4^6 5^4 6^3 10^2 | 1 | 155 R32 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 155:P[other1] | SURVIVOR | 70.38 |
| 99 | `847d2695a14ae424` | (29, 44, 17) | 3^4 4^4 5^4 6^1 8^2 9^2 | 1 | 152 P3_121 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 152:P[other1] | SURVIVOR | 70.38 |
| 100 | `090dcafb7ce9cb08` | (20, 32, 14) | 3^2 4^9 7^2 8^1 | 2 | 166 R-3m (1/24,1/12,11/24) b=1/2 | 2 | 2 | 6 | 5 | 26 | 1 |  |  | open-likely | 166:P[other1] | SURVIVOR | 69.8 |
| 101 | `7311ebf1145936e7` | (34, 51, 19) | 3^2 4^7 5^4 6^3 8^1 10^1 12^1 | 1 | 180 P6_222 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 180:P[unres1] | UNRESOLVED | 69.78 |
| 102 | `9bc4922a7b574aa6` | (17, 28, 13) | 3^4 4^4 5^4 8^1 | 2 | 166 R-3m (1/24,1/12,11/24) b=3/4 | 2 | 2 | 10 | 10 | 60 | 1 |  |  | open-likely | 166:P[other1] | SURVIVOR | 69.74 |
| 103 | `43e4e46001b4d8b9` | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 181 P6_422 (1/8,1/6,5/12) b=31/16 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 181:P[other1] | SURVIVOR | 69.68 |
| 104 | `af8b2135c913b13b` | (32, 48, 18) | 3^6 4^4 6^4 8^1 10^3 | 1 | 181 P6_422 (1/8,1/6,5/12) b=7/8 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 181:P[other1] | SURVIVOR | 69.37 |
| 105 | `6dba530a0828bdcf` | (36, 54, 20) | 3^8 4^2 5^2 7^4 9^2 10^2 | 1 | 144 P3_1 (1/8,1/6,5/12) b=7/8 | 1 | 3 | 6 | 3 | 12 | 2 | 2 |  | open-likely | 144:Pb[same1] 145:Pb[same1] | COLLISION | 69.32 |
| 106 | `74a69fba4266de3b` | (28, 43, 17) | 3^10 6^1 8^5 10^1 | 1 | 167 R-3c (1/8,1/6,5/12) b=527/1000 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 69.18 |
| 107 | `c3b4b14633c9d4d5` | (28, 43, 17) | 4^9 5^2 6^4 8^2 | 1 | 155 R32 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 155:P[other1] | SURVIVOR | 69.18 |
| 108 | `e19babba732f5fd4` | (29, 44, 17) | 4^11 5^2 7^2 10^2 | 1 | 179 P6_522 (1/12,3/8,1/6) b=7/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 69.07 |
| 109 | `2a139a0af47705e5` | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 151 P3_112 (1/12,3/8,1/6) b=1 | 2 | 1 | 56 | 11 | 373 | 7 | 1 |  | open-likely | 151:P[other1] 153:Pb[other1] 171:P[other1] 172:P[other1] 178:P[other1] 180:P[unres1] 181:Pb[same1] | COLLISION | 69.04 |
| 110 | `7472d8ba000c8056` | (22, 36, 16) | 3^8 4^2 6^2 7^4 | 2 | 152 P3_121 (0,1/4,1/6) b=9/8 | 2 | 1 | 1 | 1 | 8 | 2 |  | 1b,P5-only | wall-suspect | 152:A 154:A | SURVIVOR | 68.95 |
| 111 | `181713b518d1112b` | (22, 36, 16) | 3^6 4^6 6^3 12^1 | 6 | 148 R-3 (0,0,1/24) b=3/2 | 6 | 1 | 25 | 9 | 144 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 68.77 |
| 112 | `a23144f3446070e6` | (42, 63, 23) | 3^4 4^11 5^2 6^2 10^1 11^2 16^1 | 1 | 178 P6_122 (1/12,3/8,1/6) b=1547/2000 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | P5-only | indeterminate | 178:Pb[same1] 179:Pb[same1] | COLLISION | 68.58 |
| 113 | `d0c5a15c25ab6413` | (32, 48, 18) | 3^2 4^7 5^2 6^3 8^2 9^2 | 1 | 152 P3_121 (1/8,1/6,5/12) b=17/16 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 152:P[other1] | SURVIVOR | 68.37 |
| 114 | `d770abfcee4deb90` | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^4 12^1 | 1 | 153 P3_212 (1/8,1/6,5/12) b=19/16 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 153:P[other1] | SURVIVOR | 68.37 |
| 115 | `4a560e459032166a` | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 154 P3_221 (1/8,1/6,5/12) b=7/8 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 154:P[other1] | SURVIVOR | 68.28 |
| 116 | `5beb94b61eb66eb1` | (27, 41, 16) | 3^3 4^7 6^2 7^1 8^1 9^2 | 1 | 178 P6_122 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 178:P[other1] | SURVIVOR | 68.22 |
| 117 | `95934e84555dc2ea` | (26, 40, 16) | 3^2 4^7 5^1 6^3 7^1 8^2 | 1 | 179 P6_522 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 68.12 |
| 118 | `254345236188cc50` | (30, 46, 18) | 3^6 5^6 6^4 10^2 | 2 | 178 P6_122 (1/8,1/4,1/4) b=3/2 | 2 | 1 | 18 | 6 | 136 | 4 | 2 |  | open-likely | 169:Pb[same1] 170:Pb[same1] 178:P[other1] 179:P[other1] | COLLISION | 67.99 |
| 119 | `d0ed9179c6947b5f` | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 155 R32 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 25 | 9 | 59 | 3 |  |  | open-likely | 155:P[other1] 166:Pb[other1] 167:P[other1] | SURVIVOR | 67.83 |
| 120 | `0948aa6184f13a8a` | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 179 P6_522 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 67.48 |
| 121 | `272aefcd5e48ba49` | (29, 44, 17) | 3^3 4^3 5^3 6^5 7^2 8^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=9/8 | 1 | 3 | 5 | 5 | 5 | 1 |  | P5-only | open-likely | 179:P[other1] | SURVIVOR | 67.42 |
| 122 | `466b12546dd936c3` | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 161 R3c (1/8,1/6,5/12) b=527/1000 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 161:P[other1] | SURVIVOR | 67.08 |
| 123 | `4885ce1e70fa9713` | (27, 41, 16) | 3^3 4^5 6^4 7^3 8^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 179:P[other1] | SURVIVOR | 66.81 |
| 124 | `3d6b109f392fda19` | (33, 50, 19) | 3^6 4^4 5^2 6^3 8^2 10^1 12^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 154:P[other1] | SURVIVOR | 66.8 |
| 125 | `f94c2ae7de04a72e` | (32, 48, 18) | 3^2 4^8 6^2 7^2 8^4 | 2 | 178 P6_122 (1/6,7/12,1/12) b=3/4 | 2 | 1 | 13 | 9 | 80 | 4 | 2 |  | open-likely | 169:Pb[same1] 170:Pb[same1] 178:P[other1] 179:P[other1] | COLLISION | 66.11 |
| 126 | `e598ffd8a1cac138` | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 1 | 144 P3_1 (1/8,1/6,5/12) b=29/32 | 1 | 3 | 2 | 2 | 4 | 2 |  | P5-only | indeterminate | 144:P[other1] 145:P[other1] | SURVIVOR | 65.68 |
| 127 | `a93f8fe7ecdc5851` | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 144 P3_1 (1/12,3/8,1/6) b=9/8 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 144:P[other1] 145:P[other1] | SURVIVOR | 65.58 |
| 128 | `aef8972953d53d20` | (32, 48, 18) | 3^4 4^3 5^2 6^6 8^1 9^2 | 1 | 171 P6_2 (1/12,3/8,1/6) b=81/64 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 171:P[other1] 172:P[other1] | SURVIVOR | 65.58 |
| 129 | `72bcd959be4ab7dd` | (28, 42, 16) | 3^4 4^1 5^4 6^4 8^3 | 1 | 152 P3_121 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 152:P[other1] | SURVIVOR | 65.32 |
| 130 | `ab801b11bead62ef` | (19, 30, 13) | 3^6 4^2 5^2 6^2 12^1 | 2 | 166 R-3m (1/12,1/6,7/24) b=7/4 | 2 | 2 | 6 | 6 | 12 | 1 |  |  | open-likely | 166:P[other1] | SURVIVOR | 65.12 |
| 131 | `2c121297dbaa80af` | (28, 42, 16) | 3^4 4^2 6^8 8^2 | 1 | 154 P3_221 (1/12,3/8,1/6) b=1 | 1 | 3 | 7 | 4 | 7 | 2 |  |  | open-likely | 152:P[other1] 154:P[other1] | SURVIVOR | 64.91 |
| 132 | `d712ebc96a2dc4d9` | (36, 54, 20) | 3^6 4^6 6^3 7^2 10^2 14^1 | 1 | 153 P3_212 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 3 | 3 | 3 | 2 | 2 |  | open-likely | 151:Pb[same1] 153:Pb[same1] | COLLISION | 64.77 |
| 133 | `96db1db2ceed20c0` | (24, 38, 16) | 3^6 4^5 6^2 8^2 10^1 | 2 | 151 P3_112 (1/12,3/8,1/6) b=1/2 | 2 | 1 | 30 | 9 | 206 | 8 | 8 |  | open-likely | 151:Pb[same1] 153:Pb[same1] 171:Pb[same1] 172:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 64.75 |
| 134 | `9d0b36ad5caceb2e` | (22, 35, 15) | 3^6 4^2 5^4 6^1 8^1 10^1 | 1 | 167 R-3c (1/12,3/8,1/6) b=7/8 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 64.72 |
| 135 | `4a31af4ea18688a8` | (26, 40, 16) | 3^4 4^6 7^4 8^2 | 2 | 152 P3_121 (0,1/12,1/6) b=3/4 | 2 | 1 | 29 | 8 | 304 | 4 | 2 |  | open-likely | 144:Pb[same1] 145:Pb[same1] 152:P[other1] 154:P[other1] | COLLISION | 64.69 |
| 136 | `47b6d29f5de536f0` | (20, 32, 14) | 3^4 4^2 5^4 6^4 | 4 | 148 R-3 (0,1/2,0) b=1/2 | 4 | 0 | 35 | 11 | 380 | 6 | 4 |  | open-likely | 148:P[other1] 155:Pb[same1] 160:Pb[same1] 161:Pb[same1] 166:Pb[same1] 167:P[other1] | COLLISION | 64.2 |
| 137 | `d176b8d859dd651a` | (32, 48, 18) | 3^2 4^8 5^2 6^1 8^3 9^2 | 1 | 178 P6_122 (1/12,3/8,1/6) b=5/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 178:P[other1] | SURVIVOR | 63.7 |
| 138 | `60eb4282db04fca2` | (30, 45, 17) | 3^2 4^6 5^2 6^3 8^4 | 1 | 179 P6_522 (1/12,3/8,1/6) b=11/8 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 179:P[other1] | SURVIVOR | 63.48 |
| 139 | `59f890334e777569` | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 152 P3_121 (1/8,1/6,5/12) b=1/2 | 2 | 1 | 24 | 10 | 120 | 5 | 1 |  | open-likely | 152:P[other1] 154:P[other1] 179:P[other1] 180:P[unres1] 181:Pb[same1] | COLLISION | 63.47 |
| 140 | `ce4b84e9cad35f0a` | (25, 39, 16) | 3^6 4^4 6^2 8^4 | 2 | 180 P6_222 (0,1/2,3/8) b=3 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 180:P[unres1] 181:P[other1] | UNRESOLVED | 62.98 |
| 141 | `b7c0d3d85242db64` | (28, 42, 16) | 3^2 4^6 5^2 6^2 8^4 | 2 | 169 P6_1 (1/8,1/6,5/12) b=2 | 2 | 1 | 19 | 10 | 108 | 6 | 2 |  | open-likely | 152:Pb[same1] 154:Pb[same1] 169:P[other1] 170:P[other1] 178:P[other1] 179:P[other1] | COLLISION | 62.03 |
| 142 | `f43b45fd6383b36b` | (26, 41, 17) | 3^4 4^5 5^4 6^1 8^3 | 1 | 155 R32 (1/8,1/6,5/12) b=19/16 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 155:P[other1] | SURVIVOR | 61.77 |
| 143 | `4ff9d77aa9f8194a` | (24, 37, 15) | 3^2 4^7 6^4 8^2 | 1 | 167 R-3c (1/8,1/6,5/12) b=3/4 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 61.15 |
| 144 | `6de3dac5f334cfed` | (26, 40, 16) | 3^4 4^6 6^2 8^4 | 1 | 167 R-3c (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 61.08 |
| 145 | `01a494d767bd713c` | (22, 36, 16) | 3^6 4^4 5^2 6^2 8^2 | 2 | 155 R32 (0,1/8,0) b=1 | 2 | 1 | 26 | 9 | 121 | 2 | 1 |  | open-likely | 146:Pb[same1] 155:P[other1] | COLLISION | 61.0 |
| 146 | `105e41c2798e6180` | (16, 27, 13) | 3^6 4^3 6^4 | 6 | 148 R-3 (0,0,5/24) b=2 | 6 | 1 | 1 | 1 | 6 | 3 |  | 1b | wall-suspect | 148:P[other1] 155:P[other1] 166:P[other1] | SURVIVOR | 60.91 |
| 147 | `991a5023fc8d713a` | (27, 42, 17) | 3^8 5^2 6^4 7^2 12^1 | 2 | 166 R-3m (1/24,1/12,5/12) b=1/2 | 2 | 2 | 10 | 7 | 22 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 60.63 |
| 148 | `542cbe76934b484b` | (29, 44, 17) | 3^6 4^2 5^2 6^3 8^3 10^1 | 1 | 154 P3_221 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 154:P[other1] | SURVIVOR | 60.4 |
| 149 | `56b1d49a0766cc47` | (30, 45, 17) | 3^6 4^1 6^6 8^4 | 2 | 180 P6_222 (1/4,1/2,0) b=1 | 2 | 1 | 20 | 10 | 88 | 2 | 1 |  | open-likely | 180:P[unres1] 181:Pb[same1] | COLLISION | 60.36 |
| 150 | `2a07738610416021` | (25, 39, 16) | 3^2 4^10 8^4 | 2 | 190 P-62c (1/12,11/24,1/4) b=1/2 | 2 | 2 | 34 | 10 | 316 | 3 | 3 |  | open-likely | 150:Pb[same1] 159:Pb[same1] 190:Pb[same1] | COLLISION | 60.22 |
| 151 | `75bbbcb4a37e70e8` | (27, 41, 16) | 3^2 4^4 5^4 6^2 7^4 | 1 | 146 R3 (1/8,1/6,5/12) b=67/80 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 146:P[other1] | SURVIVOR | 60.18 |
| 152 | `efc24204486dde03` | (24, 38, 16) | 3^6 5^6 6^2 8^2 | 2 | 155 R32 (0,3/8,0) b=1/2 | 2 | 1 | 21 | 10 | 99 | 2 | 2 |  | open-likely | 146:Pb[same1] 155:Pb[same1] | COLLISION | 60.15 |
| 153 | `cff2d5fb5e0d4149` | (23, 35, 14) | 4^5 5^6 6^1 7^2 | 1 | 171 P6_2 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 8 | 2 |  |  | open-likely | 171:P[other1] 172:P[other1] | SURVIVOR | 60.05 |
| 154 | `4b6055c7aa3d341b` | (25, 38, 15) | 3^2 4^4 5^5 6^1 7^2 9^1 | 1 | 178 P6_122 (1/8,1/6,5/12) b=17/8 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 178:P[other1] | SURVIVOR | 59.98 |
| 155 | `7e79f1c38b5516bf` | (22, 34, 14) | 3^4 4^2 5^4 6^2 8^2 | 2 | 178 P6_122 (0,1/4,1/3) b=3/2 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 178:P[other1] 179:P[other1] | SURVIVOR | 59.68 |
| 156 | `d7c638d7fa23127e` | (25, 39, 16) | 3^4 4^4 5^4 7^2 8^2 | 1 | 169 P6_1 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b | wall-suspect | 169:P[other1] 170:P[other1] | SURVIVOR | 58.88 |
| 157 | `0417061f8f56488e` | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 152 P3_121 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 9 | 9 | 9 | 1 |  |  | open-likely | 152:Pb[other1] | SURVIVOR | 58.32 |
| 158 | `6cc34ed38aa354e1` | (22, 34, 14) | 3^2 4^4 5^4 6^3 8^1 | 1 | 181 P6_422 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 181:P[other1] | SURVIVOR | 57.68 |
| 159 | `5838282f46223111` | (29, 44, 17) | 3^2 4^9 6^2 8^3 10^1 | 1 | 152 P3_121 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 152:P[other1] | SURVIVOR | 57.4 |
| 160 | `cda1d1c03659b67d` | (22, 34, 14) | 4^6 5^4 6^4 | 1 | 148 R-3 (1/8,1/6,5/12) b=527/1000 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 148:P[other1] | SURVIVOR | 57.31 |
| 161 | `161b09808f4c1863` | (18, 30, 14) | 3^4 4^6 6^4 | 4 | 178 P6_122 (0,1/3,1/3) b=2 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 178:P[other1] 179:P[other1] | SURVIVOR | 57.28 |
| 162 | `c92eef8763d02d8a` | (25, 39, 16) | 3^2 4^8 5^2 7^2 8^2 | 1 | 179 P6_522 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 179:P[other1] | SURVIVOR | 57.0 |
| 163 | `8e6a80eb6f0f31a9` | (22, 34, 14) | 3^4 4^4 6^5 10^1 | 2 | 151 P3_112 (1/12,3/8,1/6) b=3/2 | 2 | 1 | 29 | 15 | 554 | 5 | 4 |  | open-likely | 151:Pb[same1] 153:Pb[same1] 178:Pb[other1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 56.91 |
| 164 | `4a6f33270c17ba66` | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 180 P6_222 (1/12,1/6,0) b=5/4 | 2 | 1 | 20 | 15 | 160 | 8 | 8 |  | open-likely | 152:Pb[same1] 154:Pb[same1] 171:Pb[same1] 172:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 56.84 |
| 165 | `3a491fd6426d90b2` | (24, 38, 16) | 3^4 4^4 5^2 6^4 7^2 | 1 | 146 R3 (1/8,1/6,5/12) b=33/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 146:P[other1] | SURVIVOR | 56.78 |
| 166 | `5b679d8b0a3147c3` | (24, 38, 16) | 3^6 4^5 7^2 8^3 | 1 | 152 P3_121 (1/12,3/8,1/6) b=17/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 152:P[other1] | SURVIVOR | 56.78 |
| 167 | `fac4317d5a65b959` | (24, 38, 16) | 3^6 4^2 5^2 6^2 7^4 | 1 | 148 R-3 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 148:P[other1] | SURVIVOR | 56.78 |
| 168 | `4b3b208f06666863` | (23, 36, 15) | 3^4 4^3 6^8 | 2 | 180 P6_222 (7/24,7/12,0) b=3/4 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 180:P[unres1] 181:P[other1] | UNRESOLVED | 56.78 |
| 169 | `4a24e04257d3d0f4` | (13, 21, 10) | 4^9 6^1 | 6 | 148 R-3 (0,0,1/24) b=9/4 | 6 | 1 | 70 | 19 | 1392 | 12 | 12 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 163:Pb[same1] 165:Pb[same1] 166:Pb[same1] 167:Pb[same1] 176:Pb[same1] 182:Pb[same1] 188:Pb[same1] 190:Pb[same1] 193:Pb[same1] 194:Pb[same1] | COLLISION | 56.32 |
| 170 | `a1b2ac427f563716` | (18, 29, 13) | 3^6 4^2 5^2 7^2 8^1 | 2 | 166 R-3m (0,1/2,1/24) b=3/4 | 2 | 2 | 47 | 14 | 150 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 56.27 |
| 171 | `27d463eac6cda5ea` | (27, 41, 16) | 3^2 4^7 6^4 8^3 | 1 | 171 P6_2 (1/12,3/8,1/6) b=5331/8000 | 1 | 3 | 2 | 2 | 4 | 2 |  | P5-only | indeterminate | 171:P[other1] 172:P[other1] | SURVIVOR | 56.18 |
| 172 | `919d30fd9021b5ee` | (25, 38, 15) | 3^3 4^3 5^2 6^4 7^3 | 1 | 154 P3_221 (1/12,3/8,1/6) b=51/32 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 154:P[other1] | SURVIVOR | 55.67 |
| 173 | `67cf3994cfeceb8b` | (21, 33, 14) | 3^6 5^2 6^4 7^2 | 2 | 150 P321 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 24 | 6 | 285 | 3 | 3 |  | open-likely | 150:Pb[same1] 159:Pb[same1] 190:Pb[same1] | COLLISION | 55.59 |
| 174 | `6074c5fa5d2dffc5` | (16, 26, 12) | 3^2 4^5 5^4 6^1 | 1 | 148 R-3 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 19 | 19 | 19 | 1 |  |  | open-likely | 148:Pb[other1] | SURVIVOR | 55.58 |
| 175 | `df40917011e94d04` | (22, 35, 15) | 3^4 4^6 6^3 8^2 | 2 | 180 P6_222 (0,1/2,1/24) b=3/2 | 2 | 1 | 23 | 12 | 112 | 4 | 2 |  | open-likely | 151:Pb[same1] 153:Pb[same1] 180:P[other1] 181:P[other1] | COLLISION | 55.48 |
| 176 | `687010310906c548` | (19, 30, 13) | 3^6 4^3 6^1 8^3 | 6 | 148 R-3 (0,0,1/6) b=7/4 | 6 | 1 | 11 | 10 | 66 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 55.43 |
| 177 | `f905851c28b76464` | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 154 P3_221 (1/8,1/6,5/12) b=7/4 | 2 | 1 | 29 | 14 | 258 | 5 | 2 |  | open-likely | 154:P[other1] 169:Pb[same1] 170:Pb[same1] 178:P[other1] 179:P[other1] | COLLISION | 55.26 |
| 178 | `c47838ebe2b50e1a` | (34, 51, 19) | 3^4 4^5 5^4 6^1 7^2 8^1 10^1 12^1 | 1 | 151 P3_112 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 2 | 2 |  | open-likely | 151:Pb[same1] 153:Pb[same1] | COLLISION | 54.78 |
| 179 | `5e68ffe7582a0657` | (20, 31, 13) | 3^4 4^3 6^5 8^1 | 1 | 167 R-3c (1/12,3/8,1/6) b=1/2 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 167:P[other1] | SURVIVOR | 54.75 |
| 180 | `a53e946faf92e440` | (8, 14, 8) | 3^4 4^4 | 8 | 148 R-3 (0,1/2,0) b=5/4 | 4 | 0 | 60 | 19 | 4632 | 19 | 18 |  | open-likely | 146:Pb[same1] 147:Pb[same1] 148:Pb[same1] 150:Pb[same1] 155:Pb[same1] 159:Pb[same1] 160:Pb[same1] 161:Pb[same1] 163:Pb[same1] 164:Pb[same1] 165:Pb[same1] 166:Pb[same1] 167:A 173:Pb[same1] 176:Pb[same1] 182:Pb[same1] 186:Pb[same1] 190:Pb[same1] 194:Pb[same1] | COLLISION | 54.63 |
| 181 | `75ed0d99a1ca0d26` | (18, 31, 15) | 3^8 4^2 5^2 6^2 8^1 | 2 | 180 P6_222 (1/6,7/12,1/6) b=1/2 | 2 | 1 | 9 | 6 | 48 | 8 | 8 |  | open-likely | 152:Pb[same1] 154:Pb[same1] 171:Pb[same1] 172:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 54.56 |
| 182 | `1ba26ab2c0999b93` | (20, 32, 14) | 3^4 4^3 5^2 6^5 | 1 | 148 R-3 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 148:P[other1] | SURVIVOR | 54.48 |
| 183 | `6784d6995cabf9df` | (18, 30, 14) | 3^4 4^6 6^4 | 2 | 150 P321 (1/8,1/6,5/12) b=3/4 | 2 | 2 | 35 | 19 | 1781 | 3 | 2 |  | open-likely | 150:Pb[other1] 159:Pb[same1] 190:Pb[same1] | COLLISION | 54.34 |
| 184 | `4297fd505b9cc36d` | (22, 34, 14) | 4^7 5^4 6^2 8^1 | 2 | 166 R-3m (1/24,1/12,1/12) b=1/2 | 2 | 2 | 26 | 9 | 106 | 4 | 3 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:P[other1] | COLLISION | 54.21 |
| 185 | `27dbb77012555d28` | (26, 40, 16) | 3^4 4^2 5^6 6^2 9^2 | 1 | 161 R3c (1/12,3/8,1/6) b=4439/8000 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 161:P[other1] | SURVIVOR | 54.1 |
| 186 | `c18a9b1cb2a5d168` | (26, 40, 16) | 3^6 4^1 5^2 6^1 7^6 | 1 | 148 R-3 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 148:P[other1] | SURVIVOR | 54.1 |
| 187 | `d1f1121757598de0` | (15, 25, 12) | 3^2 4^8 6^2 | 2 | 154 P3_221 (1/8,1/6,5/12) b=9/4 | 2 | 1 | 2 | 1 | 5 | 3 |  |  | indeterminate | 154:P[other1] 178:P[other1] 179:P[other1] | SURVIVOR | 53.96 |
| 188 | `a99e46dd535bab3b` | (32, 48, 18) | 3^4 4^4 5^2 6^4 8^2 9^2 | 1 | 144 P3_1 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 7 | 6 | 14 | 2 | 2 |  | open-likely | 144:Pb[same1] 145:Pb[same1] | COLLISION | 53.68 |
| 189 | `f3ed2550b3b58d01` | (14, 22, 10) | 3^2 4^2 5^6 | 4 | 163 P-31c (1/12,1/6,1/4) b=1/2 | 4 | 1 | 38 | 10 | 1094 | 12 | 12 |  | open-likely | 147:Pb[same1] 150:Pb[same1] 159:Pb[same1] 163:Pb[same1] 164:Pb[same1] 165:Pb[same1] 173:Pb[same1] 176:Pb[same1] 182:Pb[same1] 186:Pb[same1] 190:Pb[same1] 194:Pb[same1] | COLLISION | 53.63 |
| 190 | `18e92e9e3cc1b7a7` | (21, 33, 14) | 3^2 4^4 5^4 6^4 | 2 | 176 P6_3/m (1/8,13/24,1/4) b=1/2 | 2 | 2 | 33 | 9 | 216 | 3 | 3 |  | open-likely | 147:Pb[same1] 173:Pb[same1] 176:Pb[same1] | COLLISION | 52.92 |
| 191 | `c97273f4df7f3fdc` | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 2 | 146 R3 (1/12,3/8,1/6) b=1 | 2 | 1 | 25 | 19 | 199 | 2 | 1 |  | open-likely | 146:Pb[same1] 155:Pb[other1] | COLLISION | 52.55 |
| 192 | `b27ba8dbcbc2891a` | (22, 34, 14) | 4^8 6^6 | 1 | 161 R3c (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 3 | 5 | 1 |  |  | open-likely | 161:P[other1] | SURVIVOR | 52.08 |
| 193 | `c57d8f62f90c0cf0` | (22, 34, 14) | 3^4 4^4 6^4 8^2 | 2 | 180 P6_222 (1/4,1/2,0) b=3/2 | 2 | 1 | 16 | 12 | 136 | 4 | 2 |  | open-likely | 171:Pb[same1] 172:Pb[same1] 180:Pb[other1] 181:Pb[other1] | COLLISION | 51.85 |
| 194 | `457c20cf036ae496` | (11, 20, 11) | 3^6 4^3 5^2 | 2 | 180 P6_222 (0,1/2,0) b=3/2 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 180:A 181:A | SURVIVOR | 51.58 |
| 195 | `af480ebac6f37935` | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 2 | 148 R-3 (1/8,1/6,5/12) b=5/4 | 2 | 1 | 28 | 10 | 72 | 3 | 1 |  | open-likely | 148:Pb[same1] 161:P[other1] 167:P[other1] | COLLISION | 51.48 |
| 196 | `23c44d599f52e151` | (26, 42, 18) | 3^8 4^4 5^2 6^1 8^1 10^2 | 1 | 182 P6_322 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 8 | 8 | 8 | 1 | 1 |  | open-likely | 182:Pb[same1] | COLLISION | 51.35 |
| 197 | `11a9fe078850b5cd` | (25, 38, 15) | 3^2 4^3 5^4 6^4 7^2 | 1 | 179 P6_522 (1/8,1/6,5/12) b=65/32 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 179:P[other1] | SURVIVOR | 51.0 |
| 198 | `5f812747976b224a` | (20, 32, 14) | 3^2 4^6 5^4 7^2 | 1 | 148 R-3 (1/8,1/6,5/12) b=39/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 148:P[other1] | SURVIVOR | 50.38 |
| 199 | `c95a5fcf4d681568` | (12, 21, 11) | 3^4 4^5 5^2 | 2 | 166 R-3m (1/24,1/12,1/6) b=3/2 | 2 | 2 | 2 | 1 | 4 | 1 |  |  | indeterminate | 166:P[other1] | SURVIVOR | 50.18 |
| 200 | `f7bd7cd9eae6436b` | (16, 27, 13) | 3^6 4^4 6^2 8^1 | 2 | 166 R-3m (1/12,1/6,11/24) b=1 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 166:P[other1] | SURVIVOR | 49.48 |
| 201 | `15b6ef3944666056` | (26, 40, 16) | 3^6 5^4 6^2 7^2 8^2 | 1 | 161 R3c (1/8,1/6,5/12) b=1 | 1 | 3 | 16 | 9 | 16 | 1 | 1 |  | open-likely | 161:Pb[same1] | COLLISION | 48.73 |
| 202 | `75c9be976d704515` | (18, 28, 12) | 4^8 6^4 | 2 | 152 P3_121 (0,3/8,1/6) b=9/8 | 2 | 1 | 1 | 1 | 8 | 2 |  | 1b,P5-only | wall-suspect | 152:P[other1] 154:P[other1] | SURVIVOR | 48.55 |
| 203 | `c23407c24f02fc46` | (20, 32, 14) | 3^2 4^7 6^5 | 2 | 180 P6_222 (0,1/2,1/24) b=1/2 | 2 | 1 | 13 | 10 | 112 | 6 | 4 |  | open-likely | 151:Pb[same1] 153:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:P[unres1] 181:P[other1] | COLLISION | 48.22 |
| 204 | `346c81a0f2121bf1` | (17, 28, 13) | 3^2 4^9 7^2 | 2 | 166 R-3m (0,1/2,5/24) b=5/4 | 2 | 2 | 32 | 9 | 96 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 48.1 |
| 205 | `ddbf7770e983e608` | (26, 40, 16) | 3^4 4^6 6^3 8^2 10^1 | 2 | 166 R-3m (1/12,1/6,1/24) b=1/2 | 2 | 2 | 3 | 3 | 6 | 3 | 3 |  | open-likely | 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 48.07 |
| 206 | `8463196a30c6643f` | (23, 36, 15) | 3^2 4^5 5^2 6^6 | 1 | 179 P6_522 (1/8,1/6,5/12) b=2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 179:P[other1] | SURVIVOR | 47.8 |
| 207 | `487490cdf474e568` | (20, 32, 14) | 3^4 4^5 6^3 7^2 | 1 | 148 R-3 (1/12,3/8,1/6) b=1277/2000 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 148:P[other1] | SURVIVOR | 47.38 |
| 208 | `f0e2036d295195b4` | (12, 20, 10) | 3^4 4^4 6^2 | 2 | 152 P3_121 (0,1/8,1/6) b=9/8 | 2 | 1 | 1 | 1 | 8 | 2 |  | 1b,P5-only | wall-suspect | 152:A 154:A | SURVIVOR | 46.95 |
| 209 | `9f88c069215c2229` | (29, 46, 19) | 3^4 4^12 8^2 16^1 | 2 | 166 R-3m (1/12,13/24,1/12) b=3/4 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1b | wall-suspect | 166:Pb[same1] | COLLISION | 46.78 |
| 210 | `878c796cf524cdb7` | (22, 36, 16) | 3^6 4^4 5^2 6^2 8^2 | 2 | 150 P321 (1/8,1/6,5/12) b=2331/4000 | 2 | 2 | 4 | 2 | 18 | 3 | 3 | P5-only | indeterminate | 150:Pb[same1] 159:Pb[same1] 190:Pb[same1] | COLLISION | 46.66 |
| 211 | `3781e6ffb4480fca` | (18, 27, 11) | 4^4 5^4 6^3 | 4 | 180 P6_222 (0,1/2,1/24) b=13/4 | 2 | 1 | 15 | 10 | 100 | 8 | 6 |  | open-likely | 151:Pb[same1] 152:Pb[same1] 153:Pb[same1] 154:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:A 181:A | COLLISION | 46.6 |
| 212 | `bb3eeb50e1c37ee6` | (18, 29, 13) | 3^4 4^4 6^5 | 2 | 180 P6_222 (1/6,7/12,1/6) b=5/4 | 2 | 1 | 16 | 14 | 144 | 8 | 8 |  | open-likely | 152:Pb[same1] 154:Pb[same1] 171:Pb[same1] 172:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 46.57 |
| 213 | `d2a47816896b676a` | (17, 27, 12) | 3^2 4^2 5^8 | 2 | 147 P-3 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 23 | 7 | 347 | 3 | 3 |  | open-likely | 147:Pb[same1] 173:Pb[same1] 176:Pb[same1] | COLLISION | 46.5 |
| 214 | `0bbbe41ef60154b9` | (24, 38, 16) | 3^10 6^3 9^2 10^1 | 2 | 166 R-3m (1/12,13/24,1/24) b=1/2 | 2 | 2 | 3 | 3 | 6 | 1 | 1 |  | open-likely | 166:Pb[same1] | COLLISION | 46.28 |
| 215 | `6a892fdc51b24155` | (20, 31, 13) | 3^2 4^3 5^4 6^4 | 2 | 180 P6_222 (1/6,1/3,0) b=1 | 2 | 1 | 13 | 13 | 52 | 4 | 2 |  | open-likely | 171:Pb[same1] 172:Pb[same1] 180:A 181:A | COLLISION | 45.99 |
| 216 | `d0a0a455a34f3fcb` | (19, 29, 12) | 4^4 5^6 6^2 | 2 | 146 R3 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 10 | 7 | 642 | 3 | 3 |  | open-likely | 146:Pb[same1] 160:Pb[same1] 161:Pb[same1] | COLLISION | 45.62 |
| 217 | `fa027394e7e22a9e` | (20, 31, 13) | 3^4 4^6 7^2 12^1 | 2 | 166 R-3m (1/12,1/6,3/8) b=3/2 | 2 | 2 | 10 | 6 | 24 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 45.11 |
| 218 | `29148698f93136e6` | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 154 P3_221 (1/8,1/6,5/12) b=5/2 | 2 | 1 | 13 | 9 | 130 | 5 | 4 |  | open-likely | 154:Pb[other1] 169:Pb[same1] 170:Pb[same1] 178:Pb[same1] 179:Pb[same1] | COLLISION | 45.07 |
| 219 | `67b1ede4b021a4fc` | (17, 29, 14) | 3^4 4^6 5^2 6^2 | 1 | 155 R32 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 155:P[other1] | SURVIVOR | 44.2 |
| 220 | `7c2110f9291ac134` | (21, 33, 14) | 3^2 4^7 6^4 8^1 | 2 | 166 R-3m (0,1/2,1/24) b=1/2 | 2 | 2 | 7 | 4 | 24 | 3 | 3 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] | COLLISION | 43.77 |
| 221 | `66b85b9283c62463` | (26, 39, 15) | 4^5 5^4 6^4 7^2 | 1 | 171 P6_2 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 6 | 24 | 2 | 2 |  | open-likely | 171:Pb[same1] 172:Pb[same1] | COLLISION | 43.74 |
| 222 | `34e5e7acce18b5cd` | (14, 23, 11) | 3^6 4^2 6^2 8^1 | 2 | 166 R-3m (1/24,1/12,5/12) b=3/2 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 166:P[other1] | SURVIVOR | 43.28 |
| 223 | `11b5eb68110c797d` | (25, 38, 15) | 3^2 4^4 5^5 6^2 8^1 9^1 | 1 | 153 P3_212 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 8 | 4 | 8 | 2 | 2 |  | open-likely | 151:Pb[same1] 153:Pb[same1] | COLLISION | 43.25 |
| 224 | `0cea04a8f66814e0` | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 2 | 180 P6_222 (0,1/2,0) b=1/2 | 2 | 1 | 12 | 12 | 48 | 8 | 6 |  | open-likely | 151:Pb[same1] 152:Pb[same1] 153:Pb[same1] 154:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[other1] 181:Pb[other1] | COLLISION | 43.19 |
| 225 | `b508d80454515935` | (25, 38, 15) | 3^2 4^6 5^2 6^2 8^3 | 1 | 152 P3_121 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 14 | 12 | 15 | 2 | 2 |  | open-likely | 152:Pb[same1] 154:Pb[same1] | COLLISION | 43.11 |
| 226 | `4b7239e30e871c23` | (21, 33, 14) | 3^2 4^6 6^6 | 2 | 160 R3m (1/24,1/12,0) b=33/32 | 2 | 2 | 8 | 5 | 336 | 3 | 3 | P5-only | open-likely | 146:Pb[same1] 160:Pb[same1] 161:Pb[same1] | COLLISION | 42.78 |
| 227 | `95ea57030a106887` | (26, 39, 15) | 4^6 5^2 6^6 8^1 | 1 | 152 P3_121 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 11 | 9 | 14 | 2 | 2 |  | open-likely | 152:Pb[same1] 154:Pb[same1] | COLLISION | 42.38 |
| 228 | `fa9c370d30741970` | (9, 16, 9) | 3^4 4^5 | 2 | 180 P6_222 (1/6,1/3,0) b=3/2 | 2 | 1 | 1 | 1 | 4 | 2 |  | 1b | wall-suspect | 180:A 181:A | SURVIVOR | 42.38 |
| 229 | `6f8ed3373dca0105` | (26, 41, 17) | 3^6 4^3 5^2 6^5 12^1 | 1 | 182 P6_322 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 182:Pb[same1] | COLLISION | 42.08 |
| 230 | `5f2ba5306000a4b5` | (24, 38, 16) | 3^2 4^9 5^2 6^1 8^1 10^1 | 1 | 182 P6_322 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 182:Pb[same1] | COLLISION | 41.88 |
| 231 | `7f99db4f8ceb12b6` | (14, 23, 11) | 3^6 4^2 5^2 10^1 | 2 | 166 R-3m (1/24,1/12,1/3) b=7/4 | 2 | 2 | 15 | 13 | 68 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 41.88 |
| 232 | `a81aa52ff8097087` | (22, 35, 15) | 3^6 5^4 6^4 8^1 | 1 | 165 P-3c1 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 9 | 16 | 1 | 1 |  | open-likely | 165:Pb[same1] | COLLISION | 41.5 |
| 233 | `400cba5c78326d1d` | (17, 28, 13) | 4^10 5^2 6^1 | 1 | 167 R-3c (1/8,1/6,5/12) b=1 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 167:P[other1] | SURVIVOR | 41.2 |
| 234 | `001cbd004f823a98` | (20, 33, 15) | 3^6 4^4 6^4 8^1 | 1 | 165 P-3c1 (1/8,1/6,5/12) b=1 | 1 | 3 | 16 | 8 | 20 | 3 | 3 |  | open-likely | 165:Pb[same1] 167:Pb[same1] 182:Pb[same1] | COLLISION | 41.17 |
| 235 | `35eb3afa3bddf1b7` | (24, 38, 16) | 3^6 4^4 6^2 7^2 8^2 | 1 | 161 R3c (1/12,3/8,1/6) b=7/8 | 1 | 3 | 6 | 6 | 6 | 1 | 1 |  | open-likely | 161:Pb[same1] | COLLISION | 40.78 |
| 236 | `9fa7f38938046e47` | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 155 R32 (1/12,3/8,1/6) b=1 | 2 | 2 | 31 | 18 | 210 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 40.29 |
| 237 | `42b6cf7b856d357a` | (30, 46, 18) | 3^4 4^6 6^2 7^4 8^2 | 1 | 161 R3c (1/8,1/6,5/12) b=27/16 | 1 | 3 | 3 | 3 | 3 | 1 | 1 | P5-only | open-likely | 161:Pb[same1] | COLLISION | 40.17 |
| 238 | `3f5fce0d11d8899e` | (16, 25, 11) | 3^4 4^2 5^2 6^2 8^1 | 2 | 166 R-3m (1/24,1/12,5/12) b=7/4 | 2 | 2 | 14 | 8 | 30 | 4 | 4 |  | open-likely | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 40.15 |
| 239 | `8cdfcf810038e858` | (26, 40, 16) | 3^6 4^2 5^2 6^2 7^2 8^1 10^1 | 1 | 152 P3_121 (1/8,1/6,5/12) b=2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 |  | indeterminate | 152:Pb[same1] 154:Pb[same1] | COLLISION | 39.98 |
| 240 | `4eaa641c282f54ad` | (16, 26, 12) | 3^6 4^2 6^2 7^2 | 2 | 166 R-3m (1/24,1/12,0) b=1/2 | 2 | 2 | 14 | 9 | 42 | 2 | 2 |  | open-likely | 155:Pb[same1] 166:Pb[same1] | COLLISION | 39.85 |
| 241 | `1a804bb88ddff3e2` | (20, 33, 15) | 3^8 4^2 6^4 10^1 | 2 | 166 R-3m (1/12,13/24,0) b=1/2 | 2 | 2 | 2 | 2 | 4 | 2 | 2 |  | indeterminate | 155:Pb[same1] 166:Pb[same1] | COLLISION | 38.98 |
| 242 | `78e755ffdff3a2f5` | (14, 24, 12) | 3^4 4^6 6^2 | 2 | 146 R3 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 146:P[other1] | SURVIVOR | 38.9 |
| 243 | `08fd2cc91bbad73c` | (22, 34, 14) | 3^4 4^4 5^2 6^1 8^3 | 1 | 154 P3_221 (1/12,3/8,1/6) b=7/4 | 1 | 3 | 10 | 10 | 10 | 2 | 2 |  | open-likely | 152:Pb[same1] 154:Pb[same1] | COLLISION | 38.03 |
| 244 | `b3981da714598974` | (22, 34, 14) | 3^4 4^3 5^2 6^3 8^2 | 1 | 179 P6_522 (1/8,1/6,5/12) b=9/4 | 1 | 3 | 9 | 9 | 9 | 2 | 2 |  | open-likely | 178:Pb[same1] 179:Pb[same1] | COLLISION | 37.52 |
| 245 | `3a714f5cd139122d` | (16, 27, 13) | 3^2 4^8 5^2 6^1 | 1 | 165 P-3c1 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 20 | 14 | 54 | 3 | 3 |  | open-likely | 165:Pb[same1] 167:Pb[same1] 182:Pb[same1] | COLLISION | 37.5 |
| 246 | `a66305b551fd919e` | (25, 40, 17) | 3^8 4^2 6^6 12^1 | 2 | 166 R-3m (1/12,1/6,3/8) b=1/2 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1b | wall-suspect | 166:Pb[same1] | COLLISION | 37.38 |
| 247 | `f1e0d6a24a06b752` | (13, 22, 11) | 3^4 4^5 6^2 | 2 | 180 P6_222 (0,1/2,0) b=7/4 | 2 | 1 | 13 | 13 | 52 | 8 | 6 |  | open-likely | 151:Pb[same1] 152:Pb[same1] 153:Pb[same1] 154:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:Pb[other1] 181:Pb[other1] | COLLISION | 37.29 |
| 248 | `5ecea070beaf2efa` | (20, 33, 15) | 3^6 4^5 6^2 8^2 | 2 | 180 P6_222 (1/24,1/12,0) b=3/4 | 2 | 1 | 1 | 1 | 4 | 4 | 2 | 1b | wall-suspect | 171:Pb[same1] 172:Pb[same1] 180:P[unres1] 181:P[other1] | COLLISION | 35.48 |
| 249 | `67c9c7e50c25b4ff` | (23, 35, 14) | 4^6 5^4 6^3 8^1 | 1 | 179 P6_522 (1/12,3/8,1/6) b=11/4 | 1 | 3 | 5 | 5 | 5 | 2 | 2 |  | open-likely | 178:Pb[same1] 179:Pb[same1] | COLLISION | 34.82 |
| 250 | `ef8048ef68ceb307` | (11, 17, 8) | 3^2 4^3 5^2 6^1 | 2 | 194 P6_3/mmc (1/12,1/6,1/12) b=1/2 | 2 | 2 | 29 | 12 | 220 | 5 | 5 |  | open-likely | 163:Pb[same1] 176:Pb[same1] 182:Pb[same1] 190:Pb[same1] 194:Pb[same1] | COLLISION | 34.32 |
| 251 | `92965ea970aa430a` | (19, 30, 13) | 3^1 4^9 5^1 8^2 | 1 | 181 P6_422 (1/12,3/8,1/6) b=797/1000 | 1 | 3 | 9 | 9 | 9 | 2 | 2 |  | open-likely | 180:Pb[same1] 181:Pb[same1] | COLLISION | 34.22 |
| 252 | `7fc05363d689d31c` | (20, 32, 14) | 4^10 6^4 | 2 | 146 R3 (1/8,1/6,5/12) b=1 | 1 | 3 | 8 | 4 | 8 | 1 | 1 |  | open-likely | 146:Pb[same1] | COLLISION | 33.75 |
| 253 | `f73b315d6a9ed826` | (23, 35, 14) | 3^2 4^2 5^4 6^6 | 1 | 146 R3 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 9 | 9 | 1 | 1 |  | open-likely | 146:Pb[same1] | COLLISION | 33.62 |
| 254 | `52c5120f1148da14` | (18, 30, 14) | 3^4 4^4 5^4 6^2 | 1 | 155 R32 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 9 | 9 | 9 | 1 | 1 |  | open-likely | 155:Pb[same1] | COLLISION | 33.12 |
| 255 | `bbf85b4df505dab4` | (22, 34, 14) | 3^2 4^2 5^6 6^4 | 1 | 161 R3c (1/8,1/6,5/12) b=3/4 | 1 | 3 | 8 | 8 | 8 | 1 | 1 |  | open-likely | 161:Pb[same1] | COLLISION | 32.95 |
| 256 | `9bf0299ebc6762cc` | (18, 30, 14) | 3^4 4^7 6^2 8^1 | 2 | 180 P6_222 (0,1/4,1/6) b=3/4 | 2 | 1 | 1 | 1 | 4 | 6 | 4 | 1b | wall-suspect | 151:Pb[same1] 153:Pb[same1] 171:Pb[same1] 172:Pb[same1] 180:P[other1] 181:P[other1] | COLLISION | 32.87 |
| 257 | `a0d5da53a88ce913` | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 165 P-3c1 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 5 | 5 | 10 | 1 | 1 |  | open-likely | 165:Pb[same1] | COLLISION | 31.83 |
| 258 | `161778d5fb8390c6` | (11, 21, 12) | 3^6 4^6 | 12 | 167 R-3c (0,1/3,1/12) b=2 | 2 | 1 | 1 | 1 | 2 | 4 | 3 | 1b | wall-suspect | 148:Pb[same1] 161:Pb[same1] 163:Pb[same1] 167:A | COLLISION | 31.82 |
| 259 | `f7c3e10af5321d77` | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 1 | 163 P-31c (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 8 | 1 | 1 |  | open-likely | 163:Pb[same1] | COLLISION | 30.75 |
| 260 | `3ab0f86bf4aa2403` | (10, 18, 10) | 3^6 4^3 6^1 | 6 | 148 R-3 (0,0,1/24) b=2 | 6 | 1 | 1 | 1 | 16 | 11 | 5 | 1b | wall-suspect | 148:A 155:A 163:Pb[other1] 165:Pb[same1] 166:A 176:Pb[same1] 182:Pb[same1] 188:Pb[same1] 190:A 193:Pb[same1] 194:A | COLLISION | 30.1 |
| 261 | `a9c85108747f254c` | (15, 27, 14) | 3^8 4^2 5^2 6^2 | 2 | 155 R32 (0,1/6,0) b=1 | 2 | 1 | 1 | 1 | 4 | 1 | 1 | 1b | wall-suspect | 155:Pb[same1] | COLLISION | 29.98 |
| 262 | `c430780986390d29` | (15, 24, 11) | 3^2 4^5 5^2 6^2 | 1 | 190 P-62c (1/8,1/6,5/12) b=1 | 1 | 3 | 20 | 18 | 35 | 2 | 1 |  | open-likely | 155:Pb[same1] 190:Pb[other1] | COLLISION | 29.9 |
| 263 | `ac1d4522145eba72` | (12, 23, 13) | 3^8 4^4 6^1 | 4 | 180 P6_222 (1/6,7/12,1/6) b=3/4 | 2 | 1 | 1 | 1 | 4 | 4 | 2 | 1b | wall-suspect | 171:Pb[same1] 172:Pb[same1] 180:A 181:A | COLLISION | 29.68 |
| 264 | `5aa8e199fd7ddb2f` | (10, 15, 7) | 3^2 4^2 5^2 6^1 | 2 | 160 R3m (1/8,1/6,5/12) b=1 | 2 | 1 | 27 | 11 | 63 | 4 | 4 |  | open-likely | 148:Pb[same1] 160:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 29.51 |
| 265 | `23e145b7ec91e9b7` | (14, 21, 9) | 3^4 5^2 6^2 8^1 | 4 | 166 R-3m (0,11/24,0) b=1/2 | 2 | 1 | 2 | 2 | 4 | 3 | 2 |  | indeterminate | 148:Pb[same1] 166:P[other1] 167:Pb[same1] | COLLISION | 29.47 |
| 266 | `683431bb18c151a5` | (16, 27, 13) | 3^7 4^2 6^3 7^1 | 1 | 180 P6_222 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 5 | 5 | 5 | 2 | 2 |  | open-likely | 180:Pb[same1] 181:Pb[same1] | COLLISION | 28.12 |
| 267 | `dc51033babc85fc2` | (16, 26, 12) | 3^1 4^8 5^1 6^2 | 1 | 180 P6_222 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 9 | 9 | 9 | 2 | 2 |  | open-likely | 180:Pb[same1] 181:Pb[same1] | COLLISION | 27.92 |
| 268 | `4dc56d72019ce2e1` | (16, 27, 13) | 3^2 4^9 6^2 | 2 | 180 P6_222 (1/6,1/3,0) b=3/4 | 2 | 1 | 1 | 1 | 8 | 4 | 2 | 1b | wall-suspect | 178:Pb[same1] 179:Pb[same1] 180:P[other1] 181:P[other1] | COLLISION | 27.35 |
| 269 | `fcfb951dfb823866` | (15, 25, 12) | 3^6 5^4 6^2 | 2 | 178 P6_122 (1/12,1/6,1/4) b=3/2 | 2 | 1 | 1 | 1 | 8 | 4 | 2 | 1b | wall-suspect | 152:Pb[same1] 154:Pb[same1] 178:P[other1] 179:P[other1] | COLLISION | 27.25 |
| 270 | `39d791c3a1a9be00` | (17, 27, 12) | 3^5 4^4 6^1 8^1 9^1 | 1 | 190 P-62c (1/8,1/6,5/12) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 | 1 |  | open-likely | 190:Pb[same1] | COLLISION | 27.22 |
| 271 | `52cd1a7da3dc17c7` | (17, 29, 14) | 3^6 4^4 6^4 | 2 | 190 P-62c (1/4,7/12,1/4) b=1 | 2 | 2 | 1 | 1 | 4 | 2 | 2 | 1b | wall-suspect | 150:Pb[same1] 190:Pb[same1] | COLLISION | 26.68 |
| 272 | `484e0e43bcc91678` | (16, 26, 12) | 3^2 4^7 6^3 | 1 | 167 R-3c (1/12,3/8,1/6) b=5/4 | 1 | 3 | 12 | 12 | 12 | 1 | 1 |  | open-likely | 167:Pb[same1] | COLLISION | 25.32 |
| 273 | `54909494e08efe19` | (13, 22, 11) | 3^4 4^5 6^2 | 1 | 180 P6_222 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 15 | 13 | 25 | 2 | 2 |  | open-likely | 180:Pb[same1] 181:Pb[same1] | COLLISION | 25.16 |
| 274 | `8cb03a3652c58a13` | (13, 23, 12) | 3^2 4^10 | 4 | 176 P6_3/m (1/4,7/12,1/4) b=1 | 2 | 2 | 1 | 1 | 4 | 3 | 3 | 1b | wall-suspect | 147:Pb[same1] 148:Pb[same1] 176:Pb[same1] | COLLISION | 24.87 |
| 275 | `6f204b14872fdfe3` | (12, 22, 12) | 3^6 4^4 5^2 | 2 | 155 R32 (0,5/24,0) b=3/4 | 2 | 1 | 1 | 1 | 4 | 2 | 1 | 1b | wall-suspect | 146:Pb[same1] 155:P[other1] | COLLISION | 24.68 |
| 276 | `3d888d502de4fbd7` | (16, 24, 10) | 3^4 5^2 6^2 7^2 | 2 | 166 R-3m (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 166:Pb[same1] | COLLISION | 24.08 |
| 277 | `2dd4332c2d59834e` | (12, 22, 12) | 3^6 4^4 5^2 | 2 | 166 R-3m (1/12,1/6,1/12) b=3/2 | 2 | 2 | 1 | 1 | 2 | 4 | 4 | 1b | wall-suspect | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 23.08 |
| 278 | `f5ca5d72e1182852` | (15, 26, 13) | 3^4 4^7 6^2 | 2 | 166 R-3m (0,1/2,5/24) b=1 | 2 | 2 | 1 | 1 | 2 | 3 | 3 | 1b | wall-suspect | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] | COLLISION | 22.96 |
| 279 | `508e73881e1a160f` | (13, 20, 9) | 3^2 4^3 5^3 7^1 | 2 | 176 P6_3/m (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 8 | 1 | 1 |  | open-likely | 176:Pb[same1] | COLLISION | 22.05 |
| 280 | `a088ecb81ead0c2e` | (15, 23, 10) | 3^4 5^3 6^2 7^1 | 1 | 190 P-62c (1/8,1/6,5/12) b=1/2 | 1 | 3 | 5 | 4 | 8 | 1 | 1 |  | open-likely | 190:Pb[same1] | COLLISION | 21.9 |
| 281 | `f2af171517f10480` | (12, 21, 11) | 3^6 4^4 8^1 | 2 | 166 R-3m (1/12,1/6,1/3) b=3/2 | 2 | 2 | 1 | 1 | 2 | 4 | 4 | 1b | wall-suspect | 148:Pb[same1] 155:Pb[same1] 166:Pb[same1] 167:Pb[same1] | COLLISION | 20.08 |
| 282 | `c4f881b551b2d197` | (13, 23, 12) | 3^6 4^2 5^4 | 2 | 148 R-3 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 1 | 1 | 2 | 2 | 1 | 1b | wall-suspect | 148:P[other1] 161:Pb[same1] | COLLISION | 18.68 |
| 283 | `8f6b3652ccfef570` | (12, 19, 9) | 3^4 4^2 6^3 | 4 | 180 P6_222 (0,1/2,1/24) b=3 | 2 | 1 | 1 | 1 | 4 | 6 | 4 | 1b | wall-suspect | 151:Pb[same1] 153:Pb[same1] 178:Pb[same1] 179:Pb[same1] 180:A 181:A | COLLISION | 18.27 |
| 284 | `e6d5851e0f0ae203` | (19, 29, 12) | 3^2 4^6 6^2 8^2 | 1 | 190 P-62c (1/12,3/8,1/6) b=2777/4000 | 1 | 3 | 2 | 2 | 2 | 1 | 1 | P5-only | indeterminate | 190:Pb[same1] | COLLISION | 16.28 |
| 285 | `09db8da0e3d736f9` | (9, 14, 7) | 3^3 4^2 5^1 6^1 | 1 | 166 R-3m (1/12,3/8,1/6) b=3/4 | 1 | 3 | 18 | 18 | 18 | 3 | 3 |  | open-likely | 166:Pb[same1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 16.2 |
| 286 | `124ad8c2b2beb9cd` | (12, 18, 8) | 3^2 4^4 7^2 | 4 | 166 R-3m (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 | 1 | P5-only | open-likely | 166:Pb[same1] | COLLISION | 13.37 |
| 287 | `106d395ff6b33d4d` | (11, 17, 8) | 3^3 4^2 5^1 6^2 | 1 | 166 R-3m (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 3 | 2 |  | open-likely | 166:P[other1] 180:Pb[same1] 181:Pb[same1] | COLLISION | 12.17 |
| 288 | `91f7061ce1442584` | (14, 21, 9) | 3^3 4^2 6^3 7^1 | 1 | 160 R3m (1/8,1/6,5/12) b=67/80 | 1 | 3 | 5 | 5 | 5 | 1 | 1 | P5-only | open-likely | 160:Pb[same1] | COLLISION | 10.92 |

## f-vectors ABSENT from every sighted group's printed Schmitt table (5 of 288)

- #63 `f07d69523ef41b37` f=(20, 36, 18) p=3^10 4^4 5^2 8^2 aut=2 — sighted in 178 P6_122, 179 P6_522 — #b 1, wall-suspect, METRIC-THIN
- #110 `7472d8ba000c8056` f=(22, 36, 16) p=3^8 4^2 6^2 7^4 aut=2 — sighted in 152 P3_121, 154 P3_221 — #b 1, wall-suspect, METRIC-THIN
- #194 `457c20cf036ae496` f=(11, 20, 11) p=3^6 4^3 5^2 aut=2 — sighted in 180 P6_222, 181 P6_422 — #b 1, wall-suspect, METRIC-THIN
- #208 `f0e2036d295195b4` f=(12, 20, 10) p=3^4 4^4 6^2 aut=2 — sighted in 152 P3_121, 154 P3_221 — #b 1, wall-suspect, METRIC-THIN
- #228 `fa9c370d30741970` f=(9, 16, 9) p=3^4 4^5 aut=2 — sighted in 180 P6_222, 181 P6_422 — #b 1, wall-suspect, METRIC-THIN

## Metric-thin list (91 of 288)

| rank | id | f-vector | aut | witness | b-ratio(s) | reasons | O/W | Schmitt |
|---|---|---|---|---|---|---|---|---|
| 12 | `b24fc960c48a9c3c` | (44, 66, 24) | 1 | 180 P6_222 (1/8,1/6,5/12) | 9547/16000, 977/1600 | P5-only | indeterminate | present |
| 14 | `e1a38303b2378f17` | (40, 60, 22) | 1 | 169 P6_1 (1/8,1/6,5/12) | 9993/16000, 1277/2000, 5331/8000, 2177/3200 | P5-only | open-likely | present |
| 27 | `646b518ccf3bd724` | (36, 54, 20) | 1 | 169 P6_1 (1/8,1/6,5/12) | 29/32, 15/16, 61/64, 123/128, ... (+2) | P5-only | open-likely | present |
| 30 | `dd68dc31f1bba1af` | (40, 60, 22) | 1 | 180 P6_222 (1/8,1/6,5/12) | 49/32, 99/64 | P5-only | indeterminate | present |
| 32 | `7e05ce00d8a7cbf6` | (38, 57, 21) | 1 | 178 P6_122 (1/12,3/8,1/6) | 539/640, 271/320, 137/160, 277/320 | P5-only | open-likely | present |
| 33 | `59b28b3a59c27092` | (34, 52, 20) | 1 | 155 R32 (1/8,1/6,5/12) | 1731/3200, 4439/8000, 2331/4000, 1277/2000, ... (+2) | P5-only | open-likely | present |
| 34 | `d9ac68100a276dfe` | (36, 54, 20) | 1 | 169 P6_1 (1/8,1/6,5/12) | 2777/4000, 5777/8000, 11777/16000 | P5-only | open-likely | present |
| 35 | `6f4101f83371033d` | (36, 54, 20) | 1 | 169 P6_1 (1/8,1/6,5/12) | 1731/3200, 4439/8000, 2331/4000, 977/1600 | P5-only | open-likely | present |
| 38 | `8126183cde7ea2f3` | (36, 54, 20) | 1 | 180 P6_222 (1/8,1/6,5/12) | 25/16, 51/32 | P5-only | indeterminate | present |
| 40 | `71d2c9953ca110b8` | (36, 54, 20) | 1 | 169 P6_1 (1/12,3/8,1/6) | 39/32 | 1b,P5-only | wall-suspect | present |
| 41 | `8d90c524c89922d9` | (36, 54, 20) | 1 | 169 P6_1 (1/12,3/8,1/6) | 11/8 | 1b,P5-only | wall-suspect | present |
| 46 | `07d543d89e2934f2` | (36, 54, 20) | 1 | 152 P3_121 (1/8,1/6,5/12) | 65/64, 33/32 | P5-only | indeterminate | present |
| 49 | `2081d7b9a734e4fe` | (32, 50, 20) | 1 | 155 R32 (1/8,1/6,5/12) | 11/8 | 1b,P5-only | wall-suspect | present |
| 58 | `66563d07a1110a25` | (36, 54, 20) | 1 | 154 P3_221 (1/8,1/6,5/12) | 1 | 1b | wall-suspect | present |
| 63 | `f07d69523ef41b37` | (20, 36, 18) | 2 | 178 P6_122 (1/6,1/3,1/4) | 3/2 | 1b | wall-suspect | ABSENT-all |
| 76 | `d07f950b8309de82` | (30, 45, 17) | 2 | 171 P6_2 (1/8,1/6,5/12) | 259/320, 131/160, 67/80, 137/160, ... (+1) | P5-only | open-likely | present |
| 82 | `cbead3df2d2f1d0e` | (34, 51, 19) | 1 | 154 P3_221 (1/8,1/6,5/12) | 2331/4000, 1277/2000, 5331/8000, 2177/3200 | P5-only | open-likely | present |
| 87 | `b3d52575f76a33bd` | (34, 53, 21) | 2 | 166 R-3m (1/12,1/6,11/24) | 67/80, 137/160, 277/320, 63/64, ... (+1) | P5-only | open-likely | present |
| 88 | `fcffad0da2b5b62f` | (32, 48, 18) | 1 | 154 P3_221 (1/8,1/6,5/12) | 117/128, 59/64, 15/16, 31/32, ... (+2) | P5-only | open-likely | present |
| 92 | `37aa18e6e10583be` | (30, 47, 19) | 1 | 155 R32 (1/8,1/6,5/12) | 9/8, 37/32, 75/64 | P5-only | open-likely | present |
| 94 | `0b5d9beb0fc972f6` | (32, 48, 18) | 1 | 179 P6_522 (1/12,3/8,1/6) | 97/64, 49/32, 25/16, 13/8, ... (+1) | P5-only | open-likely | present |
| 95 | `322d5ff451e4101d` | (32, 48, 18) | 1 | 169 P6_1 (1/8,1/6,5/12) | 43/32, 11/8, 23/16 | P5-only | indeterminate | present |
| 101 | `7311ebf1145936e7` | (34, 51, 19) | 1 | 180 P6_222 (1/8,1/6,5/12) | 17/16, 9/8 | P5-only | indeterminate | present |
| 103 | `43e4e46001b4d8b9` | (32, 48, 18) | 1 | 181 P6_422 (1/8,1/6,5/12) | 61/32, 31/16, 63/32, 127/64 | P5-only | open-likely | present |
| 110 | `7472d8ba000c8056` | (22, 36, 16) | 2 | 152 P3_121 (0,1/4,1/6) | 9/8 | 1b,P5-only | wall-suspect | ABSENT-all |
| 112 | `a23144f3446070e6` | (42, 63, 23) | 1 | 178 P6_122 (1/12,3/8,1/6) | 6141/8000, 1547/2000 | P5-only | indeterminate | present |
| 113 | `d0c5a15c25ab6413` | (32, 48, 18) | 1 | 152 P3_121 (1/8,1/6,5/12) | 67/64, 17/16, 35/32 | P5-only | open-likely | present |
| 114 | `d770abfcee4deb90` | (32, 48, 18) | 1 | 153 P3_212 (1/8,1/6,5/12) | 19/16, 39/32, 79/64 | P5-only | open-likely | present |
| 121 | `272aefcd5e48ba49` | (29, 44, 17) | 1 | 179 P6_522 (1/12,3/8,1/6) | 69/64, 35/32, 9/8, 19/16, ... (+1) | P5-only | open-likely | present |
| 124 | `3d6b109f392fda19` | (33, 50, 19) | 1 | 154 P3_221 (1/8,1/6,5/12) | 3/2 | 1b | wall-suspect | present |
| 126 | `e598ffd8a1cac138` | (32, 48, 18) | 1 | 144 P3_1 (1/8,1/6,5/12) | 115/128, 29/32 | P5-only | indeterminate | present |
| 127 | `a93f8fe7ecdc5851` | (32, 48, 18) | 1 | 144 P3_1 (1/12,3/8,1/6) | 9/8 | 1b,P5-only | wall-suspect | present |
| 128 | `aef8972953d53d20` | (32, 48, 18) | 1 | 171 P6_2 (1/12,3/8,1/6) | 81/64 | 1b,P5-only | wall-suspect | present |
| 137 | `d176b8d859dd651a` | (32, 48, 18) | 1 | 178 P6_122 (1/12,3/8,1/6) | 5/2 | 1b | wall-suspect | present |
| 138 | `60eb4282db04fca2` | (30, 45, 17) | 1 | 179 P6_522 (1/12,3/8,1/6) | 11/8, 23/16, 47/32, 95/64 | P5-only | open-likely | present |
| 140 | `ce4b84e9cad35f0a` | (25, 39, 16) | 2 | 180 P6_222 (0,1/2,3/8) | 3 | 1b | wall-suspect | present |
| 142 | `f43b45fd6383b36b` | (26, 41, 17) | 1 | 155 R32 (1/8,1/6,5/12) | 19/16, 39/32, 79/64 | P5-only | open-likely | present |
| 146 | `105e41c2798e6180` | (16, 27, 13) | 6 | 148 R-3 (0,0,5/24) | 2 | 1b | wall-suspect | present |
| 148 | `542cbe76934b484b` | (29, 44, 17) | 1 | 154 P3_221 (1/8,1/6,5/12) | 5/4 | 1b | wall-suspect | present |
| 151 | `75bbbcb4a37e70e8` | (27, 41, 16) | 1 | 146 R3 (1/8,1/6,5/12) | 533/640, 67/80, 137/160, 277/320 | P5-only | open-likely | present |
| 154 | `4b6055c7aa3d341b` | (25, 38, 15) | 1 | 178 P6_122 (1/8,1/6,5/12) | 65/32, 33/16, 17/8, 69/32 | P5-only | open-likely | present |
| 155 | `7e79f1c38b5516bf` | (22, 34, 14) | 2 | 178 P6_122 (0,1/4,1/3) | 3/2 | 1b | wall-suspect | present |
| 156 | `d7c638d7fa23127e` | (25, 39, 16) | 1 | 169 P6_1 (1/12,3/8,1/6) | 3/2 | 1b | wall-suspect | present |
| 159 | `5838282f46223111` | (29, 44, 17) | 1 | 152 P3_121 (1/8,1/6,5/12) | 7/4 | 1b | wall-suspect | present |
| 161 | `161b09808f4c1863` | (18, 30, 14) | 4 | 178 P6_122 (0,1/3,1/3) | 2 | 1b | wall-suspect | present |
| 162 | `c92eef8763d02d8a` | (25, 39, 16) | 1 | 179 P6_522 (1/12,3/8,1/6) | 3/2 | 1b | wall-suspect | present |
| 165 | `3a491fd6426d90b2` | (24, 38, 16) | 1 | 146 R3 (1/8,1/6,5/12) | 33/32, 67/64 | P5-only | indeterminate | present |
| 166 | `5b679d8b0a3147c3` | (24, 38, 16) | 1 | 152 P3_121 (1/12,3/8,1/6) | 17/16, 35/32 | P5-only | indeterminate | present |
| 167 | `fac4317d5a65b959` | (24, 38, 16) | 1 | 148 R-3 (1/8,1/6,5/12) | 9/8, 19/16 | P5-only | indeterminate | present |
| 168 | `4b3b208f06666863` | (23, 36, 15) | 2 | 180 P6_222 (7/24,7/12,0) | 3/4 | 1b | wall-suspect | present |
| 171 | `27d463eac6cda5ea` | (27, 41, 16) | 1 | 171 P6_2 (1/12,3/8,1/6) | 5331/8000, 2177/3200 | P5-only | indeterminate | present |
| 172 | `919d30fd9021b5ee` | (25, 38, 15) | 1 | 154 P3_221 (1/12,3/8,1/6) | 101/64, 51/32, 103/64 | P5-only | open-likely | present |
| 185 | `27dbb77012555d28` | (26, 40, 16) | 1 | 161 R3c (1/12,3/8,1/6) | 4439/8000 | 1b,P5-only | wall-suspect | present |
| 186 | `c18a9b1cb2a5d168` | (26, 40, 16) | 1 | 148 R-3 (1/8,1/6,5/12) | 1/2 | 1b | wall-suspect | present |
| 194 | `457c20cf036ae496` | (11, 20, 11) | 2 | 180 P6_222 (0,1/2,0) | 3/2 | 1b | wall-suspect | ABSENT-all |
| 197 | `11a9fe078850b5cd` | (25, 38, 15) | 1 | 179 P6_522 (1/8,1/6,5/12) | 65/32 | 1b,P5-only | wall-suspect | present |
| 198 | `5f812747976b224a` | (20, 32, 14) | 1 | 148 R-3 (1/8,1/6,5/12) | 77/64, 39/32 | P5-only | indeterminate | present |
| 200 | `f7bd7cd9eae6436b` | (16, 27, 13) | 2 | 166 R-3m (1/12,1/6,11/24) | 1 | 1b | wall-suspect | present |
| 202 | `75c9be976d704515` | (18, 28, 12) | 2 | 152 P3_121 (0,3/8,1/6) | 9/8 | 1b,P5-only | wall-suspect | present |
| 206 | `8463196a30c6643f` | (23, 36, 15) | 1 | 179 P6_522 (1/8,1/6,5/12) | 2 | 1b | wall-suspect | present |
| 207 | `487490cdf474e568` | (20, 32, 14) | 1 | 148 R-3 (1/12,3/8,1/6) | 9993/16000, 1277/2000 | P5-only | indeterminate | present |
| 208 | `f0e2036d295195b4` | (12, 20, 10) | 2 | 152 P3_121 (0,1/8,1/6) | 9/8 | 1b,P5-only | wall-suspect | ABSENT-all |
| 209 | `9f88c069215c2229` | (29, 46, 19) | 2 | 166 R-3m (1/12,13/24,1/12) | 3/4 | 1b | wall-suspect | present |
| 210 | `878c796cf524cdb7` | (22, 36, 16) | 2 | 150 P321 (1/8,1/6,5/12) | 4439/8000, 2331/4000, 9547/16000, 11331/16000 | P5-only | indeterminate | present |
| 219 | `67b1ede4b021a4fc` | (17, 29, 14) | 1 | 155 R32 (1/8,1/6,5/12) | 3/2 | 1b | wall-suspect | present |
| 222 | `34e5e7acce18b5cd` | (14, 23, 11) | 2 | 166 R-3m (1/24,1/12,5/12) | 3/2 | 1b | wall-suspect | present |
| 226 | `4b7239e30e871c23` | (21, 33, 14) | 2 | 160 R3m (1/24,1/12,0) | 521/640, 131/160, 67/80, 137/160, ... (+4) | P5-only | open-likely | present |
| 228 | `fa9c370d30741970` | (9, 16, 9) | 2 | 180 P6_222 (1/6,1/3,0) | 3/2 | 1b | wall-suspect | ABSENT-all |
| 233 | `400cba5c78326d1d` | (17, 28, 13) | 1 | 167 R-3c (1/8,1/6,5/12) | 1 | 1b | wall-suspect | present |
| 237 | `42b6cf7b856d357a` | (30, 46, 18) | 1 | 161 R3c (1/8,1/6,5/12) | 107/64, 27/16, 55/32 | P5-only | open-likely | present |
| 242 | `78e755ffdff3a2f5` | (14, 24, 12) | 2 | 146 R3 (1/12,3/8,1/6) | 3/4 | 1b | wall-suspect | present |
| 246 | `a66305b551fd919e` | (25, 40, 17) | 2 | 166 R-3m (1/12,1/6,3/8) | 1/2 | 1b | wall-suspect | present |
| 248 | `5ecea070beaf2efa` | (20, 33, 15) | 2 | 180 P6_222 (1/24,1/12,0) | 3/4 | 1b | wall-suspect | present |
| 256 | `9bf0299ebc6762cc` | (18, 30, 14) | 2 | 180 P6_222 (0,1/4,1/6) | 3/4 | 1b | wall-suspect | present |
| 258 | `161778d5fb8390c6` | (11, 21, 12) | 12 | 167 R-3c (0,1/3,1/12) | 2 | 1b | wall-suspect | present |
| 260 | `3ab0f86bf4aa2403` | (10, 18, 10) | 6 | 148 R-3 (0,0,1/24) | 2 | 1b | wall-suspect | present |
| 261 | `a9c85108747f254c` | (15, 27, 14) | 2 | 155 R32 (0,1/6,0) | 1 | 1b | wall-suspect | present |
| 263 | `ac1d4522145eba72` | (12, 23, 13) | 4 | 180 P6_222 (1/6,7/12,1/6) | 3/4 | 1b | wall-suspect | present |
| 268 | `4dc56d72019ce2e1` | (16, 27, 13) | 2 | 180 P6_222 (1/6,1/3,0) | 3/4 | 1b | wall-suspect | present |
| 269 | `fcfb951dfb823866` | (15, 25, 12) | 2 | 178 P6_122 (1/12,1/6,1/4) | 3/2 | 1b | wall-suspect | present |
| 271 | `52cd1a7da3dc17c7` | (17, 29, 14) | 2 | 190 P-62c (1/4,7/12,1/4) | 1 | 1b | wall-suspect | present |
| 274 | `8cb03a3652c58a13` | (13, 23, 12) | 4 | 176 P6_3/m (1/4,7/12,1/4) | 1 | 1b | wall-suspect | present |
| 275 | `6f204b14872fdfe3` | (12, 22, 12) | 2 | 155 R32 (0,5/24,0) | 3/4 | 1b | wall-suspect | present |
| 277 | `2dd4332c2d59834e` | (12, 22, 12) | 2 | 166 R-3m (1/12,1/6,1/12) | 3/2 | 1b | wall-suspect | present |
| 278 | `f5ca5d72e1182852` | (15, 26, 13) | 2 | 166 R-3m (0,1/2,5/24) | 1 | 1b | wall-suspect | present |
| 281 | `f2af171517f10480` | (12, 21, 11) | 2 | 166 R-3m (1/12,1/6,1/3) | 3/2 | 1b | wall-suspect | present |
| 282 | `c4f881b551b2d197` | (13, 23, 12) | 2 | 148 R-3 (1/8,1/6,5/12) | 3/2 | 1b | wall-suspect | present |
| 283 | `8f6b3652ccfef570` | (12, 19, 9) | 4 | 180 P6_222 (0,1/2,1/24) | 3 | 1b | wall-suspect | present |
| 284 | `e6d5851e0f0ae203` | (19, 29, 12) | 1 | 190 P-62c (1/12,3/8,1/6) | 2177/3200, 2777/4000 | P5-only | indeterminate | present |
| 286 | `124ad8c2b2beb9cd` | (12, 18, 8) | 4 | 166 R-3m (1/8,1/6,5/12) | 9/8, 19/16, 39/32 | P5-only | open-likely | present |
| 288 | `91f7061ce1442584` | (14, 21, 9) | 1 | 160 R3m (1/8,1/6,5/12) | 521/640, 131/160, 67/80, 137/160, ... (+1) | P5-only | open-likely | present |

## S-cell types (menu-sighted AND reproduce one of Schmitt's printed cells: 124)

| rank | id | f-vector | aut | P2 cells | groups |
|---|---|---|---|---|---|
| 42 | `ff65c54d78bb4e50` | (34, 52, 20) | 2 | 3 | 148 155 166 |
| 43 | `1db3ca5e82f8746f` | (31, 48, 19) | 6 | 1 | 148 155 166 167 |
| 47 | `1a36f90bbc759307` | (28, 42, 16) | 4 | 6 | 144 145 151 152 153 154 169 170 171 172 178 179 180 181 |
| 48 | `76108b085b4e40f8` | (18, 30, 14) | 12 | 21 | 147 148 149 150 158 159 161 162 163 164 165 167 169 170 173 176 178 179 182 185 186 188 190 193 194 |
| 51 | `1b1288f460af270d` | (38, 58, 22) | 2 | 2 | 166 167 |
| 56 | `f593cb348adf804b` | (31, 48, 19) | 6 | 3 | 148 155 166 |
| 64 | `0fef47b559fef709` | (14, 24, 12) | 12 | 20 | 147 148 149 150 158 159 161 162 163 164 165 167 169 170 173 176 178 179 182 185 186 188 190 193 194 |
| 87 | `b3d52575f76a33bd` | (34, 53, 21) | 2 | 2 | 148 166 |
| 105 | `6dba530a0828bdcf` | (36, 54, 20) | 1 | 2 | 144 145 |
| 109 | `2a139a0af47705e5` | (28, 42, 16) | 4 | 1 | 151 153 171 172 178 180 181 |
| 111 | `181713b518d1112b` | (22, 36, 16) | 6 | 4 | 148 155 166 167 |
| 112 | `a23144f3446070e6` | (42, 63, 23) | 1 | 2 | 178 179 |
| 118 | `254345236188cc50` | (30, 46, 18) | 2 | 2 | 169 170 178 179 |
| 125 | `f94c2ae7de04a72e` | (32, 48, 18) | 2 | 2 | 169 170 178 179 |
| 132 | `d712ebc96a2dc4d9` | (36, 54, 20) | 1 | 2 | 151 153 |
| 133 | `96db1db2ceed20c0` | (24, 38, 16) | 2 | 8 | 151 153 171 172 178 179 180 181 |
| 135 | `4a31af4ea18688a8` | (26, 40, 16) | 2 | 2 | 144 145 152 154 |
| 136 | `47b6d29f5de536f0` | (20, 32, 14) | 4 | 4 | 148 155 160 161 166 167 |
| 139 | `59f890334e777569` | (26, 39, 15) | 4 | 1 | 152 154 179 180 181 |
| 141 | `b7c0d3d85242db64` | (28, 42, 16) | 2 | 2 | 152 154 169 170 178 179 |
| 145 | `01a494d767bd713c` | (22, 36, 16) | 2 | 1 | 146 155 |
| 147 | `991a5023fc8d713a` | (27, 42, 17) | 2 | 4 | 148 155 166 167 |
| 149 | `56b1d49a0766cc47` | (30, 45, 17) | 2 | 1 | 180 181 |
| 150 | `2a07738610416021` | (25, 39, 16) | 2 | 3 | 150 159 190 |
| 152 | `efc24204486dde03` | (24, 38, 16) | 2 | 2 | 146 155 |
| 163 | `8e6a80eb6f0f31a9` | (22, 34, 14) | 2 | 4 | 151 153 178 180 181 |
| 164 | `4a6f33270c17ba66` | (22, 35, 15) | 2 | 8 | 152 154 171 172 178 179 180 181 |
| 169 | `4a24e04257d3d0f4` | (13, 21, 10) | 6 | 12 | 148 155 163 165 166 167 176 182 188 190 193 194 |
| 170 | `a1b2ac427f563716` | (18, 29, 13) | 2 | 4 | 148 155 166 167 |
| 173 | `67cf3994cfeceb8b` | (21, 33, 14) | 2 | 3 | 150 159 190 |
| 175 | `df40917011e94d04` | (22, 35, 15) | 2 | 2 | 151 153 180 181 |
| 176 | `687010310906c548` | (19, 30, 13) | 6 | 4 | 148 155 166 167 |
| 177 | `f905851c28b76464` | (22, 34, 14) | 2 | 2 | 154 169 170 178 179 |
| 178 | `c47838ebe2b50e1a` | (34, 51, 19) | 1 | 2 | 151 153 |
| 180 | `a53e946faf92e440` | (8, 14, 8) | 8 | 18 | 146 147 148 150 155 159 160 161 163 164 165 166 167 173 176 182 186 190 194 |
| 181 | `75ed0d99a1ca0d26` | (18, 31, 15) | 2 | 8 | 152 154 171 172 178 179 180 181 |
| 183 | `6784d6995cabf9df` | (18, 30, 14) | 2 | 2 | 150 159 190 |
| 184 | `4297fd505b9cc36d` | (22, 34, 14) | 2 | 3 | 148 155 166 167 |
| 188 | `a99e46dd535bab3b` | (32, 48, 18) | 1 | 2 | 144 145 |
| 189 | `f3ed2550b3b58d01` | (14, 22, 10) | 4 | 12 | 147 150 159 163 164 165 173 176 182 186 190 194 |
| 190 | `18e92e9e3cc1b7a7` | (21, 33, 14) | 2 | 3 | 147 173 176 |
| 191 | `c97273f4df7f3fdc` | (18, 30, 14) | 2 | 1 | 146 155 |
| 193 | `c57d8f62f90c0cf0` | (22, 34, 14) | 2 | 2 | 171 172 180 181 |
| 195 | `af480ebac6f37935` | (20, 32, 14) | 2 | 1 | 148 161 167 |
| 196 | `23c44d599f52e151` | (26, 42, 18) | 1 | 1 | 182 |
| 201 | `15b6ef3944666056` | (26, 40, 16) | 1 | 1 | 161 |
| 203 | `c23407c24f02fc46` | (20, 32, 14) | 2 | 4 | 151 153 178 179 180 181 |
| 204 | `346c81a0f2121bf1` | (17, 28, 13) | 2 | 4 | 148 155 166 167 |
| 205 | `ddbf7770e983e608` | (26, 40, 16) | 2 | 3 | 155 166 167 |
| 209 | `9f88c069215c2229` | (29, 46, 19) | 2 | 1 | 166 |
| 210 | `878c796cf524cdb7` | (22, 36, 16) | 2 | 3 | 150 159 190 |
| 211 | `3781e6ffb4480fca` | (18, 27, 11) | 4 | 6 | 151 152 153 154 178 179 180 181 |
| 212 | `bb3eeb50e1c37ee6` | (18, 29, 13) | 2 | 8 | 152 154 171 172 178 179 180 181 |
| 213 | `d2a47816896b676a` | (17, 27, 12) | 2 | 3 | 147 173 176 |
| 214 | `0bbbe41ef60154b9` | (24, 38, 16) | 2 | 1 | 166 |
| 215 | `6a892fdc51b24155` | (20, 31, 13) | 2 | 2 | 171 172 180 181 |
| 216 | `d0a0a455a34f3fcb` | (19, 29, 12) | 2 | 3 | 146 160 161 |
| 217 | `fa027394e7e22a9e` | (20, 31, 13) | 2 | 4 | 148 155 166 167 |
| 218 | `29148698f93136e6` | (18, 28, 12) | 2 | 4 | 154 169 170 178 179 |
| 220 | `7c2110f9291ac134` | (21, 33, 14) | 2 | 3 | 148 155 166 |
| 221 | `66b85b9283c62463` | (26, 39, 15) | 1 | 2 | 171 172 |
| 223 | `11b5eb68110c797d` | (25, 38, 15) | 1 | 2 | 151 153 |
| 224 | `0cea04a8f66814e0` | (16, 26, 12) | 2 | 6 | 151 152 153 154 178 179 180 181 |
| 225 | `b508d80454515935` | (25, 38, 15) | 1 | 2 | 152 154 |
| 226 | `4b7239e30e871c23` | (21, 33, 14) | 2 | 3 | 146 160 161 |
| 227 | `95ea57030a106887` | (26, 39, 15) | 1 | 2 | 152 154 |
| 229 | `6f8ed3373dca0105` | (26, 41, 17) | 1 | 1 | 182 |
| 230 | `5f2ba5306000a4b5` | (24, 38, 16) | 1 | 1 | 182 |
| 231 | `7f99db4f8ceb12b6` | (14, 23, 11) | 2 | 4 | 148 155 166 167 |
| 232 | `a81aa52ff8097087` | (22, 35, 15) | 1 | 1 | 165 |
| 234 | `001cbd004f823a98` | (20, 33, 15) | 1 | 3 | 165 167 182 |
| 235 | `35eb3afa3bddf1b7` | (24, 38, 16) | 1 | 1 | 161 |
| 236 | `9fa7f38938046e47` | (13, 22, 11) | 2 | 4 | 148 155 166 167 |
| 237 | `42b6cf7b856d357a` | (30, 46, 18) | 1 | 1 | 161 |
| 238 | `3f5fce0d11d8899e` | (16, 25, 11) | 2 | 4 | 148 155 166 167 |
| 239 | `8cdfcf810038e858` | (26, 40, 16) | 1 | 2 | 152 154 |
| 240 | `4eaa641c282f54ad` | (16, 26, 12) | 2 | 2 | 155 166 |
| 241 | `1a804bb88ddff3e2` | (20, 33, 15) | 2 | 2 | 155 166 |
| 243 | `08fd2cc91bbad73c` | (22, 34, 14) | 1 | 2 | 152 154 |
| 244 | `b3981da714598974` | (22, 34, 14) | 1 | 2 | 178 179 |
| 245 | `3a714f5cd139122d` | (16, 27, 13) | 1 | 3 | 165 167 182 |
| 246 | `a66305b551fd919e` | (25, 40, 17) | 2 | 1 | 166 |
| 247 | `f1e0d6a24a06b752` | (13, 22, 11) | 2 | 6 | 151 152 153 154 178 179 180 181 |
| 248 | `5ecea070beaf2efa` | (20, 33, 15) | 2 | 2 | 171 172 180 181 |
| 249 | `67c9c7e50c25b4ff` | (23, 35, 14) | 1 | 2 | 178 179 |
| 250 | `ef8048ef68ceb307` | (11, 17, 8) | 2 | 5 | 163 176 182 190 194 |
| 251 | `92965ea970aa430a` | (19, 30, 13) | 1 | 2 | 180 181 |
| 252 | `7fc05363d689d31c` | (20, 32, 14) | 2 | 1 | 146 |
| 253 | `f73b315d6a9ed826` | (23, 35, 14) | 1 | 1 | 146 |
| 254 | `52c5120f1148da14` | (18, 30, 14) | 1 | 1 | 155 |
| 255 | `bbf85b4df505dab4` | (22, 34, 14) | 1 | 1 | 161 |
| 256 | `9bf0299ebc6762cc` | (18, 30, 14) | 2 | 4 | 151 153 171 172 180 181 |
| 257 | `a0d5da53a88ce913` | (20, 32, 14) | 1 | 1 | 165 |
| 258 | `161778d5fb8390c6` | (11, 21, 12) | 12 | 3 | 148 161 163 167 |
| 259 | `f7c3e10af5321d77` | (20, 32, 14) | 1 | 1 | 163 |
| 260 | `3ab0f86bf4aa2403` | (10, 18, 10) | 6 | 5 | 148 155 163 165 166 176 182 188 190 193 194 |
| 261 | `a9c85108747f254c` | (15, 27, 14) | 2 | 1 | 155 |
| 262 | `c430780986390d29` | (15, 24, 11) | 1 | 1 | 155 190 |
| 263 | `ac1d4522145eba72` | (12, 23, 13) | 4 | 2 | 171 172 180 181 |
| 264 | `5aa8e199fd7ddb2f` | (10, 15, 7) | 2 | 4 | 148 160 166 167 |
| 265 | `23e145b7ec91e9b7` | (14, 21, 9) | 4 | 2 | 148 166 167 |
| 266 | `683431bb18c151a5` | (16, 27, 13) | 1 | 2 | 180 181 |
| 267 | `dc51033babc85fc2` | (16, 26, 12) | 1 | 2 | 180 181 |
| 268 | `4dc56d72019ce2e1` | (16, 27, 13) | 2 | 2 | 178 179 180 181 |
| 269 | `fcfb951dfb823866` | (15, 25, 12) | 2 | 2 | 152 154 178 179 |
| 270 | `39d791c3a1a9be00` | (17, 27, 12) | 1 | 1 | 190 |
| 271 | `52cd1a7da3dc17c7` | (17, 29, 14) | 2 | 2 | 150 190 |
| 272 | `484e0e43bcc91678` | (16, 26, 12) | 1 | 1 | 167 |
| 273 | `54909494e08efe19` | (13, 22, 11) | 1 | 2 | 180 181 |
| 274 | `8cb03a3652c58a13` | (13, 23, 12) | 4 | 3 | 147 148 176 |
| 275 | `6f204b14872fdfe3` | (12, 22, 12) | 2 | 1 | 146 155 |
| 276 | `3d888d502de4fbd7` | (16, 24, 10) | 2 | 1 | 166 |
| 277 | `2dd4332c2d59834e` | (12, 22, 12) | 2 | 4 | 148 155 166 167 |
| 278 | `f5ca5d72e1182852` | (15, 26, 13) | 2 | 3 | 148 155 166 |
| 279 | `508e73881e1a160f` | (13, 20, 9) | 2 | 1 | 176 |
| 280 | `a088ecb81ead0c2e` | (15, 23, 10) | 1 | 1 | 190 |
| 281 | `f2af171517f10480` | (12, 21, 11) | 2 | 4 | 148 155 166 167 |
| 282 | `c4f881b551b2d197` | (13, 23, 12) | 2 | 1 | 148 161 |
| 283 | `8f6b3652ccfef570` | (12, 19, 9) | 4 | 4 | 151 153 178 179 180 181 |
| 284 | `e6d5851e0f0ae203` | (19, 29, 12) | 1 | 1 | 190 |
| 285 | `09db8da0e3d736f9` | (9, 14, 7) | 1 | 3 | 166 180 181 |
| 286 | `124ad8c2b2beb9cd` | (12, 18, 8) | 4 | 1 | 166 |
| 287 | `106d395ff6b33d4d` | (11, 17, 8) | 1 | 2 | 166 180 181 |
| 288 | `91f7061ce1442584` | (14, 21, 9) | 1 | 1 | 160 |

## Per-group counts (menu-sighted hexagonal types)

| group | symbol | first menu witness here | sighted here (menu) | sighted here (any pass) | S-cell here | f-vec A here |
|---|---|---|---|---|---|---|
| 144 | P3_1 | 6 | 6 | 8 | 4 | 0 |
| 145 | P3_2 | 0 | 6 | 8 | 4 | 0 |
| 146 | R3 | 8 | 10 | 13 | 9 | 0 |
| 147 | P-3 | 3 | 3 | 7 | 7 | 0 |
| 148 | R-3 | 21 | 23 | 41 | 30 | 1 |
| 149 | P312 | 0 | 2 | 2 | 2 | 0 |
| 150 | P321 | 3 | 6 | 9 | 9 | 0 |
| 151 | P3_112 | 8 | 10 | 18 | 14 | 0 |
| 152 | P3_121 | 18 | 22 | 31 | 15 | 3 |
| 153 | P3_212 | 5 | 12 | 20 | 14 | 0 |
| 154 | P3_221 | 16 | 26 | 36 | 17 | 3 |
| 155 | R32 | 18 | 30 | 46 | 31 | 1 |
| 158 | P3c1 | 0 | 2 | 2 | 2 | 0 |
| 159 | P31c | 0 | 5 | 8 | 8 | 0 |
| 160 | R3m | 3 | 7 | 7 | 6 | 0 |
| 161 | R3c | 7 | 12 | 17 | 13 | 0 |
| 162 | P-31m | 0 | 2 | 2 | 2 | 0 |
| 163 | P-31c | 2 | 7 | 9 | 9 | 0 |
| 164 | P-3m1 | 0 | 4 | 4 | 4 | 0 |
| 165 | P-3c1 | 4 | 6 | 10 | 10 | 0 |
| 166 | R-3m | 34 | 47 | 47 | 35 | 1 |
| 167 | R-3c | 9 | 24 | 39 | 27 | 2 |
| 169 | P6_1 | 15 | 19 | 25 | 8 | 0 |
| 170 | P6_5 | 0 | 19 | 25 | 8 | 0 |
| 171 | P6_2 | 8 | 11 | 20 | 12 | 0 |
| 172 | P6_4 | 0 | 11 | 20 | 12 | 0 |
| 173 | P6_3 | 0 | 3 | 6 | 6 | 0 |
| 176 | P6_3/m | 3 | 10 | 11 | 11 | 0 |
| 178 | P6_122 | 30 | 42 | 54 | 24 | 2 |
| 179 | P6_522 | 16 | 42 | 53 | 23 | 2 |
| 180 | P6_222 | 35 | 43 | 46 | 27 | 6 |
| 181 | P6_422 | 6 | 37 | 41 | 27 | 6 |
| 182 | P6_322 | 3 | 11 | 12 | 12 | 0 |
| 185 | P6_3cm | 0 | 2 | 2 | 2 | 0 |
| 186 | P6_3mc | 0 | 4 | 4 | 4 | 0 |
| 188 | P-6c2 | 0 | 3 | 4 | 4 | 0 |
| 190 | P-62c | 6 | 15 | 16 | 16 | 1 |
| 193 | P6_3/mcm | 0 | 3 | 4 | 4 | 0 |
| 194 | P6_3/mmc | 1 | 7 | 7 | 7 | 1 |

## Ranking recipe (all weights explicit, deterministic; identical to batch 1)

score = 3.0*F + 10.0*[F>=20] + 4.0*log2(aut) + 2.0*log2(max stab) + 3.0*min(3, #face sizes odd>=5 or >=7) + 1.5*log2(1+#menu sightings) + 1.5*(3 - min stratum dim) + 0.1*V + 2.0*log2(#b) + 1.0*log2(#groups) + 5.0*[Schmitt ABSENT-all] -4.0*[metric-thin] -25.0*[S-cell]. Tie-break: F desc, aut desc, id asc.

## Honest limits

- Schmitt flags are PROVISIONAL: text-layer parse cross-read visually on 153 of 958 rows (0 discrepancies), every row re-derived computationally in pass P2 (f-vector reproduced or quarantined), NOT independently re-keyed (G5 duty still owed) — flags provisional.
- The collision screen is TYPE-level only at Schmitt's printed representatives (one point per (group, f-vector)); a SURVIVOR verdict says his printed cell for that f-vector is a different type — his unprinted 14 TB may still contain ours (sampling, not enumeration). The top-10 survivors' pairs are re-confirmed by recomputation in collision_phase2_hex_check.py.
- OPEN vs WALL is a LABEL from stored sightings only; no perturbation runs here.
- #b counts menu sightings only; 29 of 38 printed b-ratios were never swept.
- Aut orders are combinatorial; no roundness / geometric symmetry / Burnside / Engel / Bernhard checks.
- Schmitt-printed-only types are not ranked; prior-store types re-sighted here are out of scope.
