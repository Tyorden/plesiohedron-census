# TRIAGE result — Phase-2 (tetragonal) MENU-sighted types -> G4 shortlist (2026-09-04)

Script: `triage_phase2.py` (deterministic; byte-identical across re-runs on the same inputs; model `triage_phase1.py`). Store: `phase2_types.json` (Phase-2 batch 1, run 2026-09-03; sha256 verified). Schmitt rows: schmitt_tetragonal_tables.json (VISUAL digitization, single pass, 2026-09-04). Gates: `../ANCHORS.md` G4 (finalist certificates), G5 (novelty diligence — NOT run here) and KILL CRITERIA.

**LANGUAGE (G5): every type below is "not matched against the catalog snapshot of 2026-09-03". No novelty claim. The Schmitt column is f-vector-level evidence from his printed Sec. 2.2.2 tables (a 351-CPU-year grid SAMPLING, not an enumeration): "A" = absent there (stronger candidate, still only snapshot language), "P"/"Pb" = present (same f-vector does NOT mean same type — the Josehedron/Schmitt-220 pair proves this — so a G5 type-level check is required; Pb = present at a b-ratio at which we sighted the type in that group). "S-cell" = the type IS one of his printed cells (reproduced at his generating point in pass P2): type-level match, excluded from the shortlist by the kill criterion "Schmitt-contains-candidate => reframe to first-realization".**

**SOURCE STATUS of the Schmitt flags: visual single-pass + text-layer cross-checked (0 row discrepancies, re-verified below), NOT independently re-keyed (G5 duty still owed) — flags provisional.**

## Sanity duties

- phase2_types.json sha256 71685b9ab41b4dc0c2ee1763fdd64f06b41fc51f5a0702d362f137822969f7a3: MATCHES phase2_types.SHA256SUMS [raw file present]
- Schmitt tetragonal rows: 1476 rows over 68 groups from schmitt_tetragonal_tables.json (VISUAL digitization, single pass, 2026-09-04); Euler V-E+F=2 on every row: PASS; row count vs claim 1476: MATCH
- Digitization vs text-layer harvest, row-for-row multiset on (groups, f, b, point mod 1): 1476 vs 1476 rows, 0 only in digitization, 0 only in harvest: IDENTICAL. Flag-relevant projection (group, f, b): 0 symmetric-difference entries => the Schmitt P/Pb/A flags below are IDENTICAL under either source (visual tables used as primary).
- Euler V-E+F=2: checked for all 891 stored types: ALL PASS
- p-vector consistency (|p|=F and sum(p)=2E) for all 891 types: ALL PASS
- site-stabilizer divides aut, every stored sighting (148390 sightings): ALL PASS
- kill criterion (>38 facets): max stored facet count = 35 (from our menu: 26): NO HITS
- recount: 102 cubic-store + 789 tetragonal = 891 types; tetragonal split 404 menu-sighted + 385 Schmitt-printed-only; store fields say 102/789/404/385; PHASE2_RESULT/STATUS claim 102/789/404/385: MATCH
- menu/S-only flags consistent with stored pass labels for all 789 tetragonal types: PASS
- note: 1 cubic-store type(s) carry schmitt_printed_only=True (re-sighted in tetragonal groups only at his printed points; not part of the 385): `2001fe7ea92fd0ad` f=(16,30,16)
- P2 sightings keyed by (group, printed point mod 1, b): 1215 stored cells; printed (row x group) evaluations resolved to a stored type: 1215 (PHASE2_RESULT: 1215 reproduced of 1641 evaluations)

## Headline counts (the 404 menu-sighted tetragonal types)

- Ranked: 404. S-cell (type reproduces one of Schmitt's printed cells): 176; menu-only (never at a printed point): 228.
- Schmitt f-vector flag: ABSENT-all 4; present (P/Pb in >= 1 sighted group) 400; unknown 0.
- ABSENT-all and menu-only: 4.
- Open/wall label (label only, no perturbation runs): open-likely 292, indeterminate 52, wall-suspect 60.
- Metric-thin: 126 (reasons: 1b 60, P3-only 1, P5-only 85).
- Distinct b-ratio histogram (#b: types): 1: 60, 2: 45, 3: 40, 4: 42, 5: 28, 6: 29, 7: 20, 8: 10, 9: 18, 10: 7, 11: 10, 12: 7, 13: 9, 14: 2, 15: 5, 16: 1, 17: 5, 18: 3, 19: 3, 20: 6, 21: 3, 22: 2, 23: 5, 24: 3, 25: 3, 26: 3, 27: 1, 28: 3, 29: 3, 30: 2, 31: 2, 32: 2, 33: 3, 34: 1, 35: 1, 36: 2, 37: 1, 38: 1, 41: 2, 42: 1, 44: 1, 49: 2, 51: 1, 59: 2, 60: 1, 62: 1, 67: 1, 107: 1.
- Facet count: max 26; F >= 20: 61; aut > 1: 173; fixed-point witness (dim 0): 7; line (dim 1): 56; plane (dim 2): 81; general only (dim 3): 260.

## TOP-15 G4 SHORTLIST (S-cell types excluded; rank in the full table in brackets)

1. `4e9c9b076cfec323` [#1] — **92 P4_12_12** at (5/24, 5/24, 0) b=5/4, f=(40, 60, 22), p=3^8 4^4 5^4 8^2 11^4, aut=2, b-ratios: 77/64, 39/32, 5/4, 41/32, 83/64, Schmitt 92:P[other1] 96:P[unres1] [score 111.68]  
   22 facets; aut 2; faces incl. 5-gon,8-gon,11-gon; special-position stratum (dim 1, stab 2); 5 b-ratio(s) [coarse, bisect], orbit-b max 5 -> open-likely; 2 group(s), 40 menu sighting(s); Schmitt f-vec present (92:other, 96:unres) -> G5 type-level check
2. `49cedbdd58376fac` [#4] — **92 P4_12_12** at (5/24, 5/24, 0) b=19/16, f=(44, 66, 24), p=3^10 4^4 6^4 7^2 12^4, aut=2, b-ratios: 19/16, Schmitt 92:P[other1] 96:P[unres1] [score 103.15]  
   24 facets; aut 2; faces incl. 7-gon,12-gon; special-position stratum (dim 1, stab 2); 1 b-ratio(s) [bisect], orbit-b max 1 -> wall-suspect; 2 group(s), 8 menu sighting(s); METRIC-THIN (1b,P5-only); Schmitt f-vec present (92:other, 96:unres) -> G5 type-level check
3. `f654982d74d740f6` [#5] — **141 I4_1/amd** at (0, 1/12, 1/12) b=1/2, f=(38, 57, 21), p=3^6 4^7 6^3 8^2 10^2 14^1, aut=2, b-ratios: 1/2, 9/16, 19/32, Schmitt 141:P[unres1] [score 101.22]  
   21 facets; aut 2; faces incl. 8-gon,10-gon,14-gon; plane stratum only; 3 b-ratio(s) [coarse, bisect], orbit-b max 3 -> open-likely; 1 group(s), 8 menu sighting(s); Schmitt f-vec present (141:unres) -> G5 type-level check
4. `4f6d3e68cbd9e729` [#6] — **98 I4_122** at (1/12, 3/8, 1/6) b=3/4, f=(42, 63, 23), p=3^6 4^5 5^2 6^6 8^2 12^1 14^1, aut=1, b-ratios: 23/32, 3/4, 797/1000, 4/5, 33/40, Schmitt 98:P[other1] [score 100.72]  
   23 facets; faces incl. 5-gon,8-gon,12-gon,14-gon; general position only; 5 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 5 -> open-likely; 1 group(s), 5 menu sighting(s); Schmitt f-vec present (98:other) -> G5 type-level check
5. `1497877268495988` [#7] — **91 P4_122** at (0, 1/12, 0) b=1/2, f=(32, 48, 18), p=3^4 4^4 5^4 6^2 8^2 10^2, aut=2, b-ratios: 1/2, 17/32, 9/16, 19/32, 5/8, 11/16, ... (+14), Schmitt 91:P[other1] 95:P[other1] [score 97.61]  
   18 facets; aut 2; faces incl. 5-gon,8-gon,10-gon; special-position stratum (dim 1, stab 2); 20 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 7 -> open-likely; 2 group(s), 363 menu sighting(s); Schmitt f-vec present (91:other, 95:other) -> G5 type-level check
6. `e0d18e5ea938d649` [#8] — **122 I-42d** at (1/24, 1/4, 1/8) b=1, f=(36, 54, 20), p=3^4 4^8 8^8, aut=2, b-ratios: 55/64, 7/8, 1, 5/4, 41/32, Schmitt 122:P[other1] [score 96.83]  
   20 facets; aut 2; faces incl. 8-gon; special-position stratum (dim 1, stab 2); 5 b-ratio(s) [coarse, bisect], orbit-b max 5 -> open-likely; 1 group(s), 20 menu sighting(s); Schmitt f-vec present (122:other) -> G5 type-level check
7. `6797ab70c6015039` [#10] — **76 P4_1** at (1/8, 1/6, 5/12) b=3/2, f=(32, 48, 18), p=3^4 4^4 5^4 6^2 9^4, aut=2, b-ratios: 25/32, 13/16, 67/64, 17/16, 9/8, 73/64, ... (+20), Schmitt 76:P[other1] 78:P[other1] 92:Pb[other1] 96:Pb[other1] [score 95.08]  
   18 facets; aut 2; faces incl. 5-gon,9-gon; special-position stratum (dim 1, stab 2); 26 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 8 -> open-likely; 4 group(s), 200 menu sighting(s); Schmitt f-vec present (76:other, 78:other, 92:other, 96:other) -> G5 type-level check
8. `cd4fb52572edcb73` [#11] — **86 P4_2/n** at (1/8, 1/6, 5/12) b=1, f=(30, 45, 17), p=4^9 5^4 6^1 8^2 12^1, aut=2, b-ratios: 37/64, 19/32, 39/64, 5/8, 21/32, 43/64, ... (+23), Schmitt 86:P[unres1] 93:P[other1] 118:P[other1] 134:Pb[unres1] [score 94.49]  
   17 facets; aut 2; faces incl. 5-gon,8-gon,12-gon; plane stratum only; 29 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 9 -> open-likely; 4 group(s), 290 menu sighting(s); Schmitt f-vec present (86:unres, 93:other, 118:other, 134:unres) -> G5 type-level check
9. `086ac96faf390886` [#12] — **76 P4_1** at (1/8, 1/6, 5/12) b=7/5, f=(36, 54, 20), p=3^2 4^8 5^6 10^4, aut=2, b-ratios: 203/160, 103/80, 53/40, 7/5, 113/80, Schmitt 76:P[other1] 78:P[other1] [score 94.43]  
   20 facets; aut 2; faces incl. 5-gon,10-gon; general position only; 5 b-ratio(s) [schmittb, bisect], orbit-b max 5 -> open-likely; 2 group(s), 10 menu sighting(s); Schmitt f-vec present (76:other, 78:other) -> G5 type-level check
10. `164d4bd63d82d0c3` [#13] — **76 P4_1** at (1/8, 1/6, 5/12) b=5/4, f=(40, 60, 22), p=3^6 4^6 5^2 6^4 11^4, aut=1, b-ratios: 79/64, 5/4, 403/320, Schmitt 76:P[other1] 78:P[other1] [score 94.38]  
   22 facets; faces incl. 5-gon,11-gon; general position only; 3 b-ratio(s) [coarse, bisect], orbit-b max 3 -> open-likely; 2 group(s), 6 menu sighting(s); Schmitt f-vec present (76:other, 78:other) -> G5 type-level check
11. `5dc2479b9bc14edc` [#14] — **98 I4_122** at (1/12, 3/8, 1/6) b=9/16, f=(42, 63, 23), p=3^8 4^5 5^2 6^2 8^3 10^2 16^1, aut=1, b-ratios: 17/32, 9/16, 19/32, Schmitt 98:P[other1] [score 94.37]  
   23 facets; faces incl. 5-gon,8-gon,10-gon,16-gon; general position only; 3 b-ratio(s) [bisect], orbit-b max 3 -> open-likely; 1 group(s), 3 menu sighting(s); METRIC-THIN (P5-only); Schmitt f-vec present (98:other) -> G5 type-level check
12. `3ebbca7ed2eda199` [#15] — **98 I4_122** at (1/12, 3/8, 1/6) b=1/2, f=(40, 60, 22), p=3^4 4^8 5^2 6^5 8^1 12^1 16^1, aut=1, b-ratios: 1/2, 33/64, Schmitt 98:P[other1] [score 93.38]  
   22 facets; faces incl. 5-gon,8-gon,12-gon,16-gon; general position only; 2 b-ratio(s) [coarse, bisect], orbit-b max 2 -> indeterminate; 1 group(s), 2 menu sighting(s); Schmitt f-vec present (98:other) -> G5 type-level check
13. `7575121042ade3b3` [#16] — **98 I4_122** at (1/12, 1/12, 0) b=7/4, f=(32, 48, 18), p=4^11 6^4 8^1 10^2, aut=2, b-ratios: 53/64, 27/32, 7/8, 1, 17/16, 35/32, ... (+23), Schmitt 80:P[unres1] 98:Pb[other1] [score 93.29]  
   18 facets; aut 2; faces incl. 8-gon,10-gon; special-position stratum (dim 1, stab 2); 29 b-ratio(s) [coarse, schmittb, bisect], orbit-b max 8 -> open-likely; 2 group(s), 120 menu sighting(s); Schmitt f-vec present (80:unres, 98:other) -> G5 type-level check
14. `213c7a114d5a97a8` [#17] — **98 I4_122** at (1/12, 3/8, 1/6) b=11/16, f=(42, 63, 23), p=3^6 4^4 5^4 6^5 8^2 10^1 16^1, aut=1, b-ratios: 11/16, 45/64, Schmitt 98:P[other1] [score 92.58]  
   23 facets; faces incl. 5-gon,8-gon,10-gon,16-gon; general position only; 2 b-ratio(s) [bisect], orbit-b max 2 -> indeterminate; 1 group(s), 2 menu sighting(s); METRIC-THIN (P5-only); Schmitt f-vec present (98:other) -> G5 type-level check
15. `2e8e49eb28497267` [#18] — **95 P4_322** at (1/12, 3/8, 1/6) b=53/40, f=(40, 60, 22), p=3^6 4^7 5^2 6^1 8^3 10^2 14^1, aut=1, b-ratios: 83/64, 209/160, 53/40, 427/320, Schmitt 95:P[unres1] [score 92.48]  
   22 facets; faces incl. 5-gon,8-gon,10-gon,14-gon; general position only; 4 b-ratio(s) [bisect], orbit-b max 4 -> open-likely; 1 group(s), 4 menu sighting(s); METRIC-THIN (P5-only); Schmitt f-vec present (95:unres) -> G5 type-level check

## Collision screen worklist for the shortlist (what to run first once the digitization is accepted)

For each shortlisted type flagged P/Pb: the printed rows in that group with the same f-vector, and how each reproduced in pass P2 (`other` = a different stored type, id given; `unres` = row not stored in the sweep — the two-origin / second-enantiomorph groups — re-run with the shifted setting first; `same` cannot occur here by construction). A-flagged shortlist types have no printed row to collide with.

| # | id | group | f-vector | printed b | printed point | PDF p. | P2 outcome |
|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | 92 P4_12_12 | (40, 60, 22) | 7/5 | (1951/3996, 1/3996, 1/7992) | 47 | other `cf92c5d0bb79041b` |
| 1 | `4e9c9b076cfec323` | 96 P4_32_12 | (40, 60, 22) | 7/5 | (1951/3996, 1/3996, 1/7992) | 47 | unres (not stored; re-run shifted) |
| 2 | `49cedbdd58376fac` | 92 P4_12_12 | (44, 66, 24) | 797/1000 | (57/125, 2/125, 1/8) | 47 | other `ab93cbeb7be9da28` |
| 2 | `49cedbdd58376fac` | 96 P4_32_12 | (44, 66, 24) | 797/1000 | (57/125, 2/125, 1/8) | 47 | unres (not stored; re-run shifted) |
| 3 | `f654982d74d740f6` | 141 I4_1/amd | (38, 57, 21) | 797/1000 | (1/2, 47/125, 31/250) | 84 | unres (not stored; re-run shifted) |
| 4 | `4f6d3e68cbd9e729` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 | other `2f2e04c27de95ac3` |
| 5 | `1497877268495988` | 91 P4_122 | (32, 48, 18) | 14/25 | (229/3996, 71/3996, 61/2664) | 45 | other `e5db0e3617afd976` |
| 5 | `1497877268495988` | 95 P4_322 | (32, 48, 18) | 14/25 | (229/3996, 71/3996, 61/2664) | 45 | other `e2bae62d988092d4` |
| 6 | `e0d18e5ea938d649` | 122 I-42d | (36, 54, 20) | 3497/1000 | (34/125, 34/125, 31/250) | 70 | other `5af057df372beee8` |
| 7 | `6797ab70c6015039` | 76 P4_1 | (32, 48, 18) | 797/1000 | (1/4, -1/4, 0) | 33 | other `e5760549017956be` |
| 7 | `6797ab70c6015039` | 78 P4_3 | (32, 48, 18) | 797/1000 | (1/4, -1/4, 0) | 33 | other `e5760549017956be` |
| 7 | `6797ab70c6015039` | 92 P4_12_12 | (32, 48, 18) | 7/5 | (22/333, 44/999, 61/2664) | 47 | other `1614109bcc5801ed` |
| 7 | `6797ab70c6015039` | 96 P4_32_12 | (32, 48, 18) | 7/5 | (22/333, 44/999, 61/2664) | 47 | other `3a7c6d5f00cde1ae` |
| 8 | `cd4fb52572edcb73` | 86 P4_2/n | (30, 45, 17) | 3497/1000 | (59/125, 0, 31/125) | 40 | unres (not stored; re-run shifted) |
| 8 | `cd4fb52572edcb73` | 93 P4_222 | (30, 45, 17) | 3497/1000 | (231/500, -17/500, 107/500) | 48 | other `adbb83c95151fc35` |
| 8 | `cd4fb52572edcb73` | 118 P-4n2 | (30, 45, 17) | 3497/1000 | (247/500, -1/500, 123/500) | 66 | other `da1833391efcd38c` |
| 8 | `cd4fb52572edcb73` | 134 P4_2/nnm | (30, 45, 17) | 797/1000 | (219/500, -31/500, 47/250) | 79 | unres (not stored; re-run shifted) |
| 9 | `086ac96faf390886` | 76 P4_1 | (36, 54, 20) | 797/1000 | (1597/3996, 401/3996, 0) | 33 | other `0087d56fd2a8a610` |
| 9 | `086ac96faf390886` | 78 P4_3 | (36, 54, 20) | 797/1000 | (1597/3996, 401/3996, 0) | 33 | other `0087d56fd2a8a610` |
| 10 | `164d4bd63d82d0c3` | 76 P4_1 | (40, 60, 22) | 797/1000 | (1807/3996, 191/3996, 0) | 33 | other `c1a62b4c22e7c6e8` |
| 10 | `164d4bd63d82d0c3` | 78 P4_3 | (40, 60, 22) | 797/1000 | (1807/3996, 191/3996, 0) | 33 | other `c1a62b4c22e7c6e8` |
| 11 | `5dc2479b9bc14edc` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 | other `2f2e04c27de95ac3` |
| 12 | `3ebbca7ed2eda199` | 98 I4_122 | (40, 60, 22) | 38/25 | (1129/2518, 553/1259, 565/5036) | 53 | other `1d68503f7c026843` |
| 13 | `7575121042ade3b3` | 80 I4_1 | (32, 48, 18) | 3497/1000 | (353/1413, 235/942, 0) | 35 | unres (not stored; re-run shifted) |
| 13 | `7575121042ade3b3` | 98 I4_122 | (32, 48, 18) | 38/25 | (1129/2518, 129/2518, 565/5036) | 52 | other `014a0747d02498e7` |
| 14 | `213c7a114d5a97a8` | 98 I4_122 | (42, 63, 23) | 38/25 | (1129/2518, 859/2518, 565/5036) | 53 | other `2f2e04c27de95ac3` |
| 15 | `2e8e49eb28497267` | 95 P4_322 | (40, 60, 22) | 14/25 | (223/444, 355/1332, 239/7992) | 45 | unres (not stored; re-run shifted) |

## Full ranked table (all 404 menu-sighted tetragonal types)

witness = first MENU sighting (group, point, b); stab = max site-stabilizer over menu sightings; dim = min stratum (0 fixed point / 1 line / 2 plane / 3 general); #b = distinct b-ratios (menu); ob = max distinct b on one orbit; sgt = menu sightings; grp = groups sighted (all passes); S = S-cell (P2 sightings count); thin = metric-thin reasons; O/W = open/wall label; Schmitt = per group flag with P-resolution [same/other/unres counts].

| rank | id | f-vector | p-vector | aut | witness | stab | dim | #b | ob | sgt | grp | S | thin | O/W | Schmitt | score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | (40, 60, 22) | 3^8 4^4 5^4 8^2 11^4 | 2 | 92 P4_12_12 (5/24,5/24,0) b=5/4 | 2 | 1 | 5 | 5 | 40 | 2 |  |  | open-likely | 92:P[other1] 96:P[unres1] | 111.68 |
| 2 | `698bcaf0b95bcece` | (48, 72, 26) | 3^12 4^2 5^4 6^2 8^2 12^2 14^2 | 2 | 98 I4_122 (1/12,1/4,1/8) b=5/4 | 2 | 1 | 23 | 6 | 100 | 3 | 2 |  | open-likely | 80:Pb[same1] 92:Pb[same1] 98:P[other1] | 106.42 |
| 3 | `60c6a7023f6e4280` | (36, 54, 20) | 3^4 4^4 5^8 10^4 | 8 | 80 I4_1 (0,0,0) b=5/4 | 8 | 0 | 27 | 6 | 546 | 12 | 1 |  | open-likely | 76:P[other1] 78:P[other1] 80:P[other1] 88:P[unres1] 91:P[other1] 92:Pb[other1] 95:P[unres1] 96:Pb[unres1] 98:P[other1] 109:Pb[same1] 122:P[other1] 141:A | 103.84 |
| 4 | `49cedbdd58376fac` | (44, 66, 24) | 3^10 4^4 6^4 7^2 12^4 | 2 | 92 P4_12_12 (5/24,5/24,0) b=19/16 | 2 | 1 | 1 | 1 | 8 | 2 |  | 1b,P5-only | wall-suspect | 92:P[other1] 96:P[unres1] | 103.15 |
| 5 | `f654982d74d740f6` | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 2 | 141 I4_1/amd (0,1/12,1/12) b=1/2 | 2 | 2 | 3 | 3 | 8 | 1 |  |  | open-likely | 141:P[unres1] | 101.22 |
| 6 | `4f6d3e68cbd9e729` | (42, 63, 23) | 3^6 4^5 5^2 6^6 8^2 12^1 14^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 98:P[other1] | 100.72 |
| 7 | `1497877268495988` | (32, 48, 18) | 3^4 4^4 5^4 6^2 8^2 10^2 | 2 | 91 P4_122 (0,1/12,0) b=1/2 | 2 | 1 | 20 | 7 | 363 | 2 |  |  | open-likely | 91:P[other1] 95:P[other1] | 97.61 |
| 8 | `e0d18e5ea938d649` | (36, 54, 20) | 3^4 4^8 8^8 | 2 | 122 I-42d (1/24,1/4,1/8) b=1 | 2 | 1 | 5 | 5 | 20 | 1 |  |  | open-likely | 122:P[other1] | 96.83 |
| 9 | `ab93cbeb7be9da28` | (44, 66, 24) | 3^4 4^12 6^2 8^4 14^2 | 2 | 98 I4_122 (1/8,1/4,1/8) b=5/4 | 2 | 1 | 17 | 6 | 72 | 3 | 2 |  | open-likely | 80:Pb[same1] 92:Pb[same1] 98:P[other1] | 95.44 |
| 10 | `6797ab70c6015039` | (32, 48, 18) | 3^4 4^4 5^4 6^2 9^4 | 2 | 76 P4_1 (1/8,1/6,5/12) b=3/2 | 2 | 1 | 26 | 8 | 200 | 4 |  |  | open-likely | 76:P[other1] 78:P[other1] 92:Pb[other1] 96:Pb[other1] | 95.08 |
| 11 | `cd4fb52572edcb73` | (30, 45, 17) | 4^9 5^4 6^1 8^2 12^1 | 2 | 86 P4_2/n (1/8,1/6,5/12) b=1 | 2 | 2 | 29 | 9 | 290 | 4 |  |  | open-likely | 86:P[unres1] 93:P[other1] 118:P[other1] 134:Pb[unres1] | 94.49 |
| 12 | `086ac96faf390886` | (36, 54, 20) | 3^2 4^8 5^6 10^4 | 2 | 76 P4_1 (1/8,1/6,5/12) b=7/5 | 1 | 3 | 5 | 5 | 10 | 2 |  |  | open-likely | 76:P[other1] 78:P[other1] | 94.43 |
| 13 | `164d4bd63d82d0c3` | (40, 60, 22) | 3^6 4^6 5^2 6^4 11^4 | 1 | 76 P4_1 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 3 | 3 | 6 | 2 |  |  | open-likely | 76:P[other1] 78:P[other1] | 94.38 |
| 14 | `5dc2479b9bc14edc` | (42, 63, 23) | 3^8 4^5 5^2 6^2 8^3 10^2 16^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=9/16 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 98:P[other1] | 94.37 |
| 15 | `3ebbca7ed2eda199` | (40, 60, 22) | 3^4 4^8 5^2 6^5 8^1 12^1 16^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 98:P[other1] | 93.38 |
| 16 | `7575121042ade3b3` | (32, 48, 18) | 4^11 6^4 8^1 10^2 | 2 | 98 I4_122 (1/12,1/12,0) b=7/4 | 2 | 1 | 29 | 8 | 120 | 2 |  |  | open-likely | 80:P[unres1] 98:Pb[other1] | 93.29 |
| 17 | `213c7a114d5a97a8` | (42, 63, 23) | 3^6 4^4 5^4 6^5 8^2 10^1 16^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=11/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 98:P[other1] | 92.58 |
| 18 | `2e8e49eb28497267` | (40, 60, 22) | 3^6 4^7 5^2 6^1 8^3 10^2 14^1 | 1 | 95 P4_322 (1/12,3/8,1/6) b=53/40 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 95:P[unres1] | 92.48 |
| 19 | `7abaf90ae92699d9` | (36, 54, 20) | 3^2 4^9 5^4 6^1 8^2 12^2 | 1 | 98 I4_122 (1/8,1/6,5/12) b=11/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 98:P[other1] | 91.98 |
| 20 | `61fc4ef8c8ac459a` | (40, 60, 22) | 3^6 4^6 5^2 6^4 10^2 12^2 | 1 | 76 P4_1 (1/8,1/6,5/12) b=19/16 | 1 | 3 | 2 | 2 | 4 | 2 |  | P5-only | indeterminate | 76:P[other1] 78:P[other1] | 91.48 |
| 21 | `1e910e0da7668cc3` | (32, 48, 18) | 3^4 4^2 5^4 6^4 8^4 | 2 | 98 I4_122 (1/12,1/4,1/8) b=1 | 2 | 1 | 21 | 8 | 112 | 1 |  |  | open-likely | 98:P[other1] | 91.21 |
| 22 | `fb1d7781b51e80a4` | (36, 54, 20) | 3^2 4^10 5^2 6^1 8^3 10^1 12^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 91:P[other1] | 91.12 |
| 23 | `b27e5415727dba6f` | (35, 53, 20) | 3^6 4^3 5^4 6^4 8^1 10^1 14^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 91:P[other1] | 91.02 |
| 24 | `5ebc1b8c073a87a9` | (28, 42, 16) | 3^4 4^2 5^4 6^2 8^4 | 4 | 95 P4_322 (1/8,1/6,5/12) b=9/4 | 4 | 1 | 13 | 9 | 79 | 5 |  |  | open-likely | 88:P[unres1] 95:P[unres1] 98:P[other1] 122:P[other1] 141:P[unres1] | 91.01 |
| 25 | `21c64995b621173f` | (38, 57, 21) | 3^6 4^7 6^3 8^2 10^2 14^1 | 1 | 94 P4_22_12 (1/8,1/6,5/12) b=7/5 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 94:P[other1] | 90.18 |
| 26 | `0b6473b240a3c9e9` | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^3 12^2 | 1 | 95 P4_322 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 95:P[unres1] | 90.08 |
| 27 | `acb8eed6b8a82612` | (36, 54, 20) | 3^6 4^7 6^3 10^2 12^2 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=7/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 142:P[unres1] | 89.71 |
| 28 | `35f1b5368eef3104` | (40, 60, 22) | 3^4 4^6 5^2 6^7 8^1 12^2 | 1 | 98 I4_122 (1/12,3/8,1/6) b=39/40 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 98:P[other1] | 89.38 |
| 29 | `eb2a39308c77a5f2` | (40, 60, 22) | 3^4 4^12 6^1 8^2 10^2 18^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=17/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 98:P[other1] | 89.38 |
| 30 | `f91f4b104fcf5351` | (38, 57, 21) | 3^4 4^7 5^2 6^4 8^2 10^1 14^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=5/8 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 98:P[other1] | 89.28 |
| 31 | `c8f0574fc8252b45` | (38, 57, 21) | 3^4 4^10 6^3 8^1 12^3 | 1 | 98 I4_122 (1/8,1/6,5/12) b=3 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 98:P[other1] | 88.97 |
| 32 | `18748e6ed02d0e2a` | (36, 54, 20) | 3^6 4^3 5^4 6^3 8^1 10^1 11^2 | 1 | 80 I4_1 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 3 | 2 | 3 | 1 |  |  | indeterminate | 80:P[other1] | 88.77 |
| 33 | `5ca658605515696d` | (36, 54, 20) | 3^2 4^9 5^4 7^2 8^1 10^1 14^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=1 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 98:P[other1] | 88.77 |
| 34 | `7431ec8f1f876c60` | (36, 54, 20) | 3^6 4^4 6^3 7^4 9^2 10^1 | 1 | 80 I4_1 (1/8,1/6,5/12) b=17/20 | 1 | 3 | 7 | 4 | 7 | 1 |  | P5-only | open-likely | 80:P[other1] | 88.71 |
| 35 | `81ad1d3d87b8288c` | (33, 51, 20) | 3^8 4^4 5^2 6^2 8^2 12^2 | 1 | 91 P4_122 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 91:P[other1] | 88.47 |
| 36 | `8c2cebc1a5598689` | (32, 48, 18) | 3^6 5^4 6^2 7^4 9^2 | 2 | 122 I-42d (1/12,1/4,1/8) b=3/4 | 2 | 1 | 7 | 3 | 28 | 1 |  |  | open-likely | 122:P[other1] | 88.1 |
| 37 | `33e3eaedc0ac1c33` | (36, 54, 20) | 3^4 4^8 5^2 9^6 | 1 | 76 P4_1 (1/12,3/8,1/6) b=1 | 1 | 3 | 3 | 3 | 6 | 2 |  |  | open-likely | 76:P[other1] 78:P[other1] | 87.98 |
| 38 | `16a9b6f95073dfbb` | (30, 45, 17) | 3^2 4^5 5^4 6^1 7^4 10^1 | 2 | 116 P-4c2 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 9 | 4 | 99 | 2 |  |  | open-likely | 116:P[other1] 138:A | 87.81 |
| 39 | `bfcb72a81fce8c4a` | (36, 54, 20) | 3^6 4^7 6^3 10^3 14^1 | 1 | 118 P-4n2 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 118:P[other1] | 87.08 |
| 40 | `408752c46c2d7c90` | (36, 54, 20) | 3^6 4^6 6^2 8^2 9^2 10^2 | 1 | 76 P4_1 (1/12,3/8,1/6) b=19/16 | 1 | 3 | 3 | 3 | 6 | 2 |  | P5-only | open-likely | 76:P[other1] 78:P[other1] | 86.98 |
| 41 | `8b991972fb6aab30` | (36, 54, 20) | 3^2 4^11 5^2 6^1 8^1 10^2 14^1 | 1 | 96 P4_32_12 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 96:P[unres1] | 86.98 |
| 42 | `c1a62b4c22e7c6e8` | (40, 60, 22) | 3^8 4^4 5^4 10^6 | 2 | 92 P4_12_12 (1/12,1/12,0) b=1 | 2 | 1 | 7 | 3 | 56 | 4 | 2 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 92:P[other1] 96:P[unres1] | 86.36 |
| 43 | `14ee43e7e7821ec9` | (38, 57, 21) | 3^2 4^8 6^9 10^1 12^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=9/10 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 98:P[other1] | 86.28 |
| 44 | `804dd9fb0c1a57ca` | (38, 57, 21) | 3^6 4^7 5^2 8^3 11^2 12^1 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=11/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 88:P[unres1] | 86.18 |
| 45 | `b755f1dd6635f8a8` | (38, 57, 21) | 3^4 4^4 5^6 6^5 12^1 14^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=35/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 98:P[other1] | 86.18 |
| 46 | `b1355d63057fb8b6` | (30, 45, 17) | 3^4 4^2 5^6 8^5 | 2 | 88 I4_1/a (1/12,3/8,1/6) b=3/4 | 2 | 1 | 14 | 6 | 39 | 3 |  |  | open-likely | 88:P[unres1] 110:P[other1] 142:P[unres1] | 86.18 |
| 47 | `0a848b954870c137` | (36, 54, 20) | 3^6 4^5 5^2 7^2 8^1 9^2 10^2 | 1 | 80 I4_1 (1/8,1/6,5/12) b=11/16 | 1 | 3 | 4 | 2 | 4 | 1 |  | P5-only | indeterminate | 80:P[other1] | 86.08 |
| 48 | `e5760549017956be` | (32, 48, 18) | 3^8 4^2 6^4 10^4 | 8 | 76 P4_1 (1/8,1/6,5/12) b=1 | 8 | 0 | 17 | 8 | 640 | 12 | 3 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 80:P[unres1] 88:P[unres1] 91:P[other1] 92:P[other1] 95:P[other1] 96:P[other1] 98:P[other1] 109:Pb[same1] 122:P[other1] 141:P[unres1] | 83.45 |
| 49 | `1045f2420adbbe89` | (38, 57, 21) | 3^8 4^2 5^4 6^2 8^1 10^2 11^2 | 1 | 80 I4_1 (1/12,3/8,1/6) b=38/25 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P3-only | wall-suspect | 80:P[other1] | 83.3 |
| 50 | `3ad771f657b3824c` | (38, 57, 21) | 3^6 4^6 5^2 6^3 10^3 14^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=1/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 122:P[other1] | 83.3 |
| 51 | `d43d8d2dd9836ed4` | (38, 57, 21) | 3^6 4^7 6^2 7^2 8^2 12^1 14^1 | 1 | 118 P-4n2 (1/8,1/6,5/12) b=59/32 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 118:P[other1] | 83.3 |
| 52 | `eca7be02cb8e2296` | (38, 57, 21) | 3^2 4^9 5^2 6^2 7^2 8^2 10^2 | 1 | 98 I4_122 (1/12,3/8,1/6) b=9/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 98:P[other1] | 83.3 |
| 53 | `0087d56fd2a8a610` | (36, 54, 20) | 3^6 4^4 5^4 9^6 | 2 | 92 P4_12_12 (1/12,1/12,0) b=3/4 | 2 | 1 | 13 | 4 | 104 | 4 | 2 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 92:P[other1] 96:P[unres1] | 83.07 |
| 54 | `06c5da3bdc942c6f` | (36, 54, 20) | 3^8 4^2 6^6 10^4 | 2 | 92 P4_12_12 (1/8,1/6,5/12) b=5/2 | 2 | 1 | 21 | 14 | 253 | 3 | 1 |  | open-likely | 80:Pb[same1] 92:P[other1] 98:Pb[other1] | 82.95 |
| 55 | `99e39b85a778ce64` | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 122 I-42d (1/12,1/4,1/8) b=1 | 2 | 1 | 20 | 9 | 102 | 2 |  |  | open-likely | 82:P[other1] 122:P[other1] | 82.47 |
| 56 | `a3a8447783e42486` | (24, 38, 16) | 3^8 5^4 8^4 | 8 | 80 I4_1 (0,0,0) b=3/2 | 8 | 0 | 31 | 10 | 896 | 12 | 4 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 80:P[other1] 88:P[unres1] 91:P[other1] 92:Pb[same1] 95:P[unres1] 96:P[unres1] 98:P[other1] 109:Pb[same1] 122:P[other1] 141:P[unres1] | 82.11 |
| 57 | `b2284df87d426947` | (36, 54, 20) | 3^8 4^4 6^2 7^2 10^2 11^2 | 1 | 76 P4_1 (1/8,1/6,5/12) b=65/64 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 76:P[other1] 78:P[other1] | 81.98 |
| 58 | `9ff7306e4a6cbf44` | (34, 51, 19) | 4^11 6^5 8^2 12^1 | 2 | 141 I4_1/amd (0,1/12,1/12) b=9/16 | 2 | 2 | 7 | 4 | 14 | 1 |  | P5-only | open-likely | 141:P[unres1] | 81.38 |
| 59 | `2a3cf777c624752c` | (24, 36, 14) | 3^4 4^2 5^4 6^2 8^1 12^1 | 2 | 141 I4_1/amd (0,1/12,1/12) b=3/2 | 2 | 2 | 32 | 9 | 122 | 1 |  |  | open-likely | 141:P[unres1] | 81.31 |
| 60 | `835d94261e1b65c1` | (38, 57, 21) | 3^6 4^8 6^2 8^2 12^3 | 1 | 98 I4_122 (1/8,1/6,5/12) b=25/8 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 98:P[other1] | 80.3 |
| 61 | `fe3a62d422ed4d82` | (40, 61, 23) | 3^8 4^9 6^3 13^2 18^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=1/2 | 2 | 2 | 4 | 4 | 8 | 1 | 1 |  | open-likely | 141:Pb[same1] | 80.25 |
| 62 | `d9b73e02d62b6d79` | (36, 54, 20) | 3^2 4^9 6^6 8^1 10^1 12^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 98:P[other1] | 80.1 |
| 63 | `6983d731cb2a7d98` | (36, 55, 21) | 3^6 4^7 5^4 6^1 11^2 16^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=3/4 | 2 | 2 | 5 | 5 | 10 | 3 | 3 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:Pb[same1] | 79.52 |
| 64 | `d49d430cb3198a1c` | (32, 48, 18) | 3^2 4^8 5^2 6^2 8^3 12^1 | 1 | 93 P4_222 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 12 | 12 | 1 |  |  | open-likely | 93:P[other1] | 78.92 |
| 65 | `19c7c8de77b6ce20` | (32, 48, 18) | 3^4 4^6 5^2 6^1 8^2 9^2 10^1 | 1 | 80 I4_1 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 9 | 9 | 17 | 1 |  |  | open-likely | 80:Pb[unres1] | 78.79 |
| 66 | `e8f8dcf6c6a09601` | (34, 51, 19) | 3^8 4^2 7^4 8^4 10^1 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 92:P[other1] | 78.78 |
| 67 | `ed4e2709d136f0fc` | (32, 48, 18) | 3^4 5^8 7^4 8^2 | 2 | 122 I-42d (1/24,1/4,1/8) b=27/32 | 2 | 1 | 2 | 2 | 8 | 1 |  | P5-only | indeterminate | 122:P[other1] | 77.95 |
| 68 | `844e2ca1a4cc7678` | (34, 51, 19) | 3^4 4^9 7^2 8^2 12^2 | 1 | 122 I-42d (1/8,1/6,5/12) b=7/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 122:P[other1] | 77.92 |
| 69 | `e827fb0a11642e9f` | (32, 48, 18) | 3^4 4^4 5^4 7^2 8^2 9^2 | 1 | 76 P4_1 (1/12,3/8,1/6) b=4/5 | 1 | 3 | 6 | 6 | 12 | 2 |  |  | open-likely | 76:Pb[other1] 78:Pb[other1] | 77.92 |
| 70 | `10ce641e92adc9fa` | (33, 50, 19) | 3^4 4^8 5^2 7^2 8^1 10^1 14^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=7/5 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 91:P[other1] | 77.82 |
| 71 | `32810102c8039911` | (18, 28, 12) | 3^6 4^1 6^4 10^1 | 4 | 137 P4_2/nmc (0,1/6,1/12) b=3/2 | 2 | 2 | 49 | 17 | 608 | 1 |  |  | open-likely | 137:P[unres1] | 77.4 |
| 72 | `747a6712c328a5cf` | (32, 48, 18) | 3^4 4^6 6^3 8^4 10^1 | 2 | 96 P4_32_12 (1/8,1/6,5/12) b=9/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 96:P[other1] | 77.31 |
| 73 | `05f9eab1c6915aef` | (34, 51, 19) | 3^4 4^8 6^4 10^1 12^2 | 1 | 133 P4_2/nbc (1/12,3/8,1/6) b=3/4 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 133:P[unres1] | 77.15 |
| 74 | `2204c0ceea51430d` | (28, 42, 16) | 3^4 4^2 5^4 6^3 8^2 10^1 | 2 | 86 P4_2/n (1/8,1/6,5/12) b=2 | 1 | 3 | 11 | 10 | 17 | 1 |  |  | open-likely | 86:Pb[unres1] | 76.97 |
| 75 | `e969c24510c5b82b` | (32, 48, 18) | 3^4 4^4 5^4 7^4 8^1 12^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=5/4 | 1 | 3 | 8 | 8 | 8 | 1 |  |  | open-likely | 86:P[unres1] | 76.95 |
| 76 | `181818daaf2fdcb8` | (34, 51, 19) | 3^6 4^4 5^4 8^2 10^2 12^1 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=1 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 110:P[other1] | 76.88 |
| 77 | `6912c8e94df60725` | (34, 51, 19) | 3^4 4^6 5^2 6^2 8^3 10^2 | 1 | 98 I4_122 (1/12,3/8,1/6) b=3 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 98:P[other1] | 76.88 |
| 78 | `2ef5e3844229f89f` | (34, 51, 19) | 3^4 4^7 5^2 6^1 8^3 10^1 12^1 | 1 | 94 P4_22_12 (1/8,1/6,5/12) b=29/20 | 1 | 3 | 9 | 5 | 9 | 1 |  | P5-only | open-likely | 94:P[other1] | 76.72 |
| 79 | `8ce6c8b7341edeb2` | (32, 48, 18) | 3^2 4^8 5^2 6^1 7^2 8^2 12^1 | 1 | 116 P-4c2 (1/8,1/6,5/12) b=1 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 116:P[other1] | 76.31 |
| 80 | `e4200db43401702b` | (28, 42, 16) | 3^4 4^4 6^4 8^4 | 8 | 88 I4_1/a (0,1/4,1/8) b=1/2 | 4 | 0 | 24 | 6 | 888 | 8 | 4 |  | open-likely | 80:Pb[same1] 88:P[unres1] 98:P[other1] 109:Pb[same1] 118:Pb[same1] 119:Pb[same1] 122:P[other1] 141:Pb[unres1] | 76.16 |
| 81 | `ec59577573c34683` | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 2 | 141 I4_1/amd (0,1/6,1/6) b=1/2 | 2 | 2 | 2 | 2 | 4 | 1 |  |  | indeterminate | 141:P[unres1] | 75.98 |
| 82 | `db0320ad071ab1eb` | (34, 51, 19) | 3^6 4^4 6^4 8^2 9^2 10^1 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=19/20 | 1 | 3 | 6 | 3 | 6 | 2 |  | P5-only | open-likely | 92:P[other1] 96:P[unres1] | 75.78 |
| 83 | `a04f0c895fcd35ec` | (32, 48, 18) | 4^10 5^4 9^4 | 4 | 76 P4_1 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 6 | 2 |  | P5-only | open-likely | 76:P[other1] 78:P[other1] | 75.58 |
| 84 | `278f5cc0bdb53b51` | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=3/2 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 142:P[unres1] | 75.58 |
| 85 | `cde6f488fa3b5e98` | (32, 48, 18) | 3^6 4^3 5^2 6^1 7^2 8^3 12^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=3/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 86:P[unres1] | 75.58 |
| 86 | `7923a7fad737ae23` | (34, 51, 19) | 3^8 4^1 5^2 6^4 8^1 10^2 12^1 | 1 | 98 I4_122 (1/8,1/6,5/12) b=13/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 98:P[other1] | 75.57 |
| 87 | `8b96d46626c486fe` | (34, 51, 19) | 3^8 5^4 6^2 7^2 8^1 12^2 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=9/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 86:P[unres1] | 75.57 |
| 88 | `fa88164038f13cf0` | (33, 51, 20) | 3^6 4^8 5^2 8^1 9^2 16^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=1 | 2 | 2 | 6 | 6 | 12 | 1 | 1 |  | open-likely | 141:Pb[same1] | 75.52 |
| 89 | `3fc289d8d4944791` | (34, 51, 19) | 3^4 4^7 6^3 7^2 8^1 10^1 12^1 | 1 | 116 P-4c2 (1/8,1/6,5/12) b=631/400 | 1 | 3 | 7 | 4 | 7 | 1 |  | P5-only | open-likely | 116:P[other1] | 75.51 |
| 90 | `b8e16e8d04fc1057` | (34, 51, 19) | 3^4 4^8 6^2 8^3 10^1 12^1 | 1 | 93 P4_222 (1/8,1/6,5/12) b=631/400 | 1 | 3 | 7 | 4 | 7 | 1 |  | P5-only | open-likely | 93:P[other1] | 75.51 |
| 91 | `18b35afa85c5a929` | (31, 47, 18) | 3^4 4^7 6^2 7^2 8^2 12^1 | 1 | 95 P4_322 (1/12,3/8,1/6) b=7/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 95:P[unres1] | 75.48 |
| 92 | `dfe1108b777824fa` | (26, 39, 15) | 3^2 4^5 6^6 8^2 | 4 | 88 I4_1/a (1/12,3/8,1/6) b=1/2 | 2 | 1 | 6 | 4 | 12 | 2 |  |  | open-likely | 88:P[unres1] 142:P[unres1] | 75.32 |
| 93 | `96c135294ff83fe2` | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 142 I4_1/acd (1/12,1/4,3/8) b=1/2 | 2 | 1 | 6 | 4 | 28 | 1 |  |  | open-likely | 142:P[unres1] | 75.26 |
| 94 | `9b708cb2bde13500` | (34, 51, 19) | 3^2 4^10 6^2 8^3 10^2 | 1 | 95 P4_322 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 95:P[unres1] | 74.92 |
| 95 | `9ae45735b2d716dd` | (44, 66, 24) | 3^4 4^10 6^4 7^2 8^2 12^1 14^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=5/2 | 1 | 3 | 2 | 2 | 2 | 1 | 1 |  | indeterminate | 98:Pb[same1] | 74.78 |
| 96 | `9e9ed09ab338b2d5` | (32, 48, 18) | 3^2 4^6 5^2 6^5 8^2 10^1 | 1 | 95 P4_322 (1/12,3/8,1/6) b=1 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 95:P[other1] | 74.72 |
| 97 | `f2ac84eeafc07509` | (32, 48, 18) | 3^4 4^4 5^2 6^4 7^2 10^2 | 1 | 122 I-42d (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 122:P[other1] | 74.72 |
| 98 | `5be2e092046ee24b` | (28, 42, 16) | 4^8 6^7 10^1 | 2 | 86 P4_2/n (1/8,1/6,5/12) b=7/4 | 1 | 3 | 15 | 6 | 19 | 4 |  |  | open-likely | 86:P[unres1] 92:Pb[other1] 96:Pb[unres1] 122:P[other1] | 74.1 |
| 99 | `8fc19c6bf41cc1fd` | (32, 48, 18) | 3^2 4^6 5^4 6^1 8^5 | 1 | 80 I4_1 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 8 | 4 | 8 | 1 |  |  | open-likely | 80:P[unres1] | 73.95 |
| 100 | `6f6ee36de8dbda72` | (34, 51, 19) | 3^4 4^7 6^3 7^2 8^1 10^1 12^1 | 1 | 118 P-4n2 (1/8,1/6,5/12) b=15/8 | 1 | 3 | 5 | 3 | 5 | 1 |  | P5-only | open-likely | 118:P[other1] | 73.92 |
| 101 | `9ed821a3c69a01f6` | (30, 45, 17) | 3^2 4^6 5^4 8^5 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 12 | 8 | 12 | 2 |  |  | open-likely | 92:P[other1] 96:P[unres1] | 73.72 |
| 102 | `81f7cb02d9bd215e` | (32, 48, 18) | 3^4 4^3 5^4 6^2 7^2 8^2 10^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=5/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 122:P[other1] | 73.68 |
| 103 | `c6485dad3118cbd5` | (30, 45, 17) | 3^4 4^2 5^6 7^2 8^2 10^1 | 1 | 110 I4_1cd (1/12,3/8,1/6) b=1 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 110:Pb[other1] | 73.11 |
| 104 | `33f2ba7ec7b99fa4` | (28, 42, 16) | 3^2 4^4 5^4 6^2 7^2 8^2 | 1 | 76 P4_1 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 8 | 6 | 16 | 2 |  |  | open-likely | 76:P[other1] 78:P[other1] | 72.93 |
| 105 | `c5eec049a827aebd` | (44, 66, 24) | 3^10 4^2 5^4 6^2 7^2 11^2 13^2 | 1 | 76 P4_1 (1/8,1/6,5/12) b=39/32 | 1 | 3 | 2 | 2 | 4 | 2 | 2 | P5-only | indeterminate | 76:Pb[same1] 78:Pb[same1] | 72.88 |
| 106 | `d25aa9f2dff2be4e` | (34, 51, 19) | 3^4 4^5 5^2 6^6 10^1 14^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=31/16 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 142:P[unres1] | 72.88 |
| 107 | `10f9a0d8ff07b3e4` | (30, 45, 17) | 3^4 4^2 5^4 6^3 8^4 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=1 | 1 | 3 | 10 | 7 | 10 | 2 |  |  | open-likely | 92:P[other1] 96:P[unres1] | 72.83 |
| 108 | `e64ff7d1f133b6c9` | (30, 45, 17) | 3^4 4^5 6^4 8^3 10^1 | 1 | 91 P4_122 (1/12,3/8,1/6) b=1 | 1 | 3 | 10 | 7 | 10 | 2 |  |  | open-likely | 91:P[other1] 95:P[unres1] | 72.83 |
| 109 | `5e4688ed5001cc7c` | (24, 36, 14) | 4^2 5^8 6^4 | 2 | 82 I-4 (1/12,3/8,1/6) b=1/2 | 2 | 1 | 10 | 4 | 54 | 2 |  |  | open-likely | 82:P[other1] 122:P[other1] | 72.72 |
| 110 | `1c45cdaed191693e` | (34, 51, 19) | 3^6 4^3 5^4 6^2 10^4 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=3/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 88:P[unres1] | 72.57 |
| 111 | `974ed1256562acc3` | (23, 36, 15) | 3^4 4^6 5^1 7^3 10^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=5/4 | 2 | 2 | 4 | 4 | 8 | 1 |  |  | open-likely | 141:P[unres1] | 72.55 |
| 112 | `8c1c95e91814d6a2` | (28, 42, 16) | 3^2 4^4 5^4 6^4 8^1 10^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 6 | 12 | 1 |  |  | open-likely | 122:P[other1] | 72.52 |
| 113 | `08c9708977b15d14` | (30, 45, 17) | 3^4 4^4 5^2 7^4 8^3 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 92:Pb[other1] | 72.38 |
| 114 | `a0be76769745bbaf` | (30, 45, 17) | 3^4 4^2 5^4 6^4 8^2 10^1 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=5/4 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 142:P[unres1] | 72.38 |
| 115 | `bb0c84c025667b98` | (30, 45, 17) | 3^2 4^5 5^4 6^3 8^2 10^1 | 1 | 94 P4_22_12 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 94:P[other1] | 72.38 |
| 116 | `133690822bdda4b1` | (32, 48, 18) | 3^6 4^3 5^2 6^1 7^2 8^1 9^2 10^1 | 1 | 96 P4_32_12 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 96:P[other1] | 72.37 |
| 117 | `184a74b1373839c8` | (32, 48, 18) | 3^2 4^8 5^2 6^1 7^2 8^2 12^1 | 1 | 94 P4_22_12 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 94:P[other1] | 72.37 |
| 118 | `d61dc4c2a6bcba4c` | (32, 48, 18) | 3^2 4^4 5^6 6^3 8^2 10^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 98:P[other1] | 72.37 |
| 119 | `db9ffdbe1d267b0a` | (26, 40, 16) | 3^4 4^5 5^2 6^1 7^2 8^1 10^1 | 1 | 130 P4/ncc (1/12,3/8,1/6) b=5/4 | 1 | 3 | 11 | 11 | 11 | 1 |  |  | open-likely | 130:P[unres1] | 71.9 |
| 120 | `caf680c78915ba1d` | (26, 39, 15) | 3^2 4^2 5^4 6^6 8^1 | 2 | 122 I-42d (1/8,1/6,5/12) b=1 | 1 | 3 | 15 | 9 | 17 | 1 |  |  | open-likely | 122:Pb[other1] | 71.67 |
| 121 | `4e702e95c290afbd` | (34, 51, 19) | 3^6 4^2 5^4 6^2 8^2 9^2 10^1 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=17/20 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 88:P[unres1] | 71.57 |
| 122 | `8a3d9b4f9a849029` | (34, 51, 19) | 3^2 4^9 5^2 6^2 8^2 10^1 12^1 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=19/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 142:P[unres1] | 71.57 |
| 123 | `de71f6925d09ec9a` | (30, 45, 17) | 4^10 5^2 7^2 8^1 9^2 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 110:P[other1] | 71.52 |
| 124 | `823d10214adbceef` | (34, 51, 19) | 3^6 4^4 6^4 8^3 10^2 | 2 | 80 I4_1 (1/8,1/6,5/12) b=5/4 | 2 | 1 | 28 | 9 | 117 | 2 | 1 |  | open-likely | 80:Pb[same1] 98:Pb[other1] | 71.34 |
| 125 | `31a32605d919fa4a` | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 112 P-42c (1/8,1/6,5/12) b=2 | 1 | 3 | 12 | 10 | 34 | 2 |  |  | open-likely | 112:Pb[other1] 114:Pb[other1] | 71.26 |
| 126 | `e1f32acb6ba6b519` | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^2 10^2 | 1 | 82 I-4 (1/8,1/6,5/12) b=5/8 | 1 | 3 | 4 | 4 | 8 | 1 |  | P5-only | open-likely | 82:P[other1] | 70.95 |
| 127 | `cd3c192b4e0547ef` | (34, 51, 19) | 3^6 4^6 6^2 8^1 10^4 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 92:P[other1] | 70.78 |
| 128 | `b504635d2b404e93` | (32, 48, 18) | 3^4 4^5 5^2 6^3 8^3 12^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=5/8 | 1 | 3 | 5 | 5 | 5 | 1 |  | P5-only | open-likely | 86:P[unres1] | 70.72 |
| 129 | `a19179f2621b5623` | (32, 48, 18) | 3^2 4^8 5^2 7^2 8^2 9^2 | 1 | 76 P4_1 (1/12,3/8,1/6) b=9/8 | 1 | 3 | 3 | 3 | 6 | 2 |  | P5-only | open-likely | 76:P[other1] 78:P[other1] | 70.58 |
| 130 | `b530335e09b88d43` | (32, 48, 18) | 3^4 4^2 5^6 6^2 8^3 10^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=7/4 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 98:Pb[other1] | 70.58 |
| 131 | `9b13c651d989772a` | (30, 45, 17) | 3^4 4^4 5^2 7^4 8^3 | 1 | 110 I4_1cd (1/12,3/8,1/6) b=3/4 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 110:P[other1] | 70.48 |
| 132 | `c64d7a44fc7eafce` | (30, 45, 17) | 4^10 5^2 6^1 8^2 9^2 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=1 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 88:P[unres1] | 70.48 |
| 133 | `f5534a0cdd155dd1` | (30, 45, 17) | 4^9 5^4 7^2 8^1 12^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=7/4 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 142:P[unres1] | 70.48 |
| 134 | `5c6382a9ef3bc209` | (30, 45, 17) | 3^2 4^9 6^2 8^2 10^2 | 2 | 133 P4_2/nbc (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 133:P[unres1] | 70.17 |
| 135 | `1451aa79a85162c1` | (34, 51, 19) | 3^6 4^4 5^4 8^3 12^2 | 2 | 142 I4_1/acd (1/8,1/8,1/4) b=3/4 | 2 | 1 | 13 | 6 | 45 | 2 | 1 |  | open-likely | 110:Pb[same1] 142:P[unres1] | 70.09 |
| 136 | `8357998c809f5d36` | (28, 42, 16) | 3^2 4^4 5^2 6^6 8^2 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=5/4 | 1 | 3 | 13 | 8 | 13 | 1 |  |  | open-likely | 88:P[unres1] | 69.91 |
| 137 | `d167fc392cd667a6` | (28, 42, 16) | 3^4 4^3 5^2 6^3 7^2 8^1 10^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=9/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 142:Pb[unres1] | 69.91 |
| 138 | `35398c494f7e95b0` | (34, 51, 19) | 3^8 5^4 6^2 8^1 9^2 10^2 | 1 | 96 P4_32_12 (1/12,3/8,1/6) b=5/8 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 96:P[unres1] | 69.78 |
| 139 | `3dd10b67f0ea1611` | (34, 51, 19) | 3^2 4^8 5^2 7^4 8^1 9^2 | 1 | 80 I4_1 (1/8,1/6,5/12) b=9/10 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 80:P[other1] | 69.78 |
| 140 | `900973c9cdd62294` | (34, 51, 19) | 3^4 4^6 5^2 6^3 8^1 10^3 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=5/8 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 88:P[unres1] | 69.78 |
| 141 | `799b17ae5c44c23a` | (32, 48, 18) | 3^6 4^3 6^4 7^2 8^2 12^1 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=37/16 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 86:P[unres1] | 69.68 |
| 142 | `ca0eff8176f46d8d` | (30, 45, 17) | 3^4 4^4 6^3 7^4 8^2 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 92:P[other1] | 69.38 |
| 143 | `4c8f59f850756091` | (30, 45, 17) | 3^4 4^3 5^2 6^5 8^2 10^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=5/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 122:P[other1] | 69.17 |
| 144 | `8dce1cb5e78590f9` | (30, 45, 17) | 3^4 4^3 5^2 6^3 7^2 8^3 | 1 | 96 P4_32_12 (1/12,3/8,1/6) b=327/200 | 1 | 3 | 7 | 7 | 7 | 1 |  | P5-only | open-likely | 96:P[unres1] | 69.11 |
| 145 | `c6c1f93f18915d8d` | (32, 48, 18) | 4^10 6^6 10^2 | 1 | 95 P4_322 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 95:P[other1] | 68.72 |
| 146 | `35953737803092f0` | (16, 24, 10) | 3^4 4^1 6^4 8^1 | 8 | 82 I-4 (0,0,1/12) b=1/2 | 8 | 1 | 107 | 19 | 7527 | 37 | 32 |  | open-likely | 77:Pb[same1] 81:Pb[same1] 82:Pb[same1] 84:Pb[same1] 86:P[unres1] 87:Pb[same1] 91:Pb[same1] 92:Pb[same1] 93:Pb[same1] 94:Pb[same1] 95:Pb[same1] 96:Pb[same1] 97:Pb[same1] 98:Pb[same1] 101:Pb[same1] 102:Pb[same1] 105:Pb[same1] 111:Pb[same1] 112:Pb[same1] 113:Pb[same1] 114:Pb[same1] 115:Pb[same1] 116:Pb[same1] 118:Pb[same1] 119:Pb[same1] 121:Pb[same1] 126:A 128:Pb[same1] 131:Pb[same1] 132:Pb[same1] 134:P[unres1] 135:Pb[same1] 136:Pb[same1] 137:P[unres1] 138:P[unres1] 139:Pb[same1] 142:Pb[same1] | 68.61 |
| 147 | `925e5163e8cf6e42` | (20, 32, 14) | 3^2 4^8 6^2 7^2 | 2 | 141 I4_1/amd (0,1/12,0) b=1/2 | 2 | 2 | 10 | 7 | 30 | 1 |  |  | open-likely | 141:Pb[unres1] | 68.58 |
| 148 | `72d03fdd4ab546d7` | (30, 45, 17) | 3^6 4^3 6^3 8^4 10^1 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 142:P[unres1] | 68.52 |
| 149 | `f4b8ca8a468d040d` | (30, 45, 17) | 3^2 4^4 5^6 6^1 8^4 | 1 | 98 I4_122 (1/8,1/6,5/12) b=5/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 98:P[other1] | 68.52 |
| 150 | `675cc4f2c640cd11` | (32, 48, 18) | 3^2 4^8 5^2 6^1 7^2 8^2 12^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 86:P[unres1] | 68.37 |
| 151 | `841ca21dc8f5c770` | (32, 48, 18) | 3^6 4^2 5^2 6^2 7^4 8^1 12^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=677/400 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 142:P[unres1] | 68.37 |
| 152 | `d25e09a426bd8ecf` | (32, 48, 18) | 3^4 4^5 5^2 6^2 7^2 9^2 10^1 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=9/16 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 86:P[unres1] | 68.37 |
| 153 | `e23ad48c69ddca62` | (32, 48, 18) | 3^4 4^5 5^2 6^1 7^2 8^2 9^2 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 88:P[unres1] | 68.37 |
| 154 | `d9532f4f2d8bff33` | (28, 42, 16) | 3^4 4^2 5^2 6^5 8^3 | 1 | 114 P-42_1c (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 6 | 10 | 1 |  |  | open-likely | 114:P[other1] | 68.33 |
| 155 | `5af057df372beee8` | (36, 54, 20) | 3^8 4^4 6^3 8^3 12^1 14^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=2 | 1 | 3 | 7 | 7 | 9 | 1 | 1 |  | open-likely | 122:Pb[same1] | 68.2 |
| 156 | `3c8373805b3b0aab` | (24, 36, 14) | 4^2 5^8 6^4 | 8 | 77 P4_2 (1/8,1/6,5/12) b=1 | 2 | 1 | 41 | 19 | 1417 | 5 | 1 |  | open-likely | 77:P[other1] 81:Pb[other1] 82:Pb[other1] 84:Pb[same1] 122:P[other1] | 68.14 |
| 157 | `8ac4f8b1c6ca250e` | (28, 42, 16) | 3^2 4^7 6^2 7^2 8^3 | 1 | 133 P4_2/nbc (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 9 | 9 | 1 |  |  | open-likely | 133:P[unres1] | 68.12 |
| 158 | `7391016f434c6483` | (38, 57, 21) | 3^4 4^8 5^2 6^3 8^2 12^1 14^1 | 1 | 95 P4_322 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 3 | 3 | 3 | 2 | 1 |  | open-likely | 91:Pb[same1] 95:P[unres1] | 67.97 |
| 159 | `67d7f938f580079f` | (28, 42, 16) | 4^9 6^5 8^1 10^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=3/2 | 1 | 3 | 8 | 5 | 9 | 1 |  |  | open-likely | 122:P[other1] | 67.78 |
| 160 | `e1eb97228b6a2e0a` | (30, 45, 17) | 3^4 4^4 5^2 6^4 8^1 10^2 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=5/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 92:P[other1] | 67.38 |
| 161 | `a62c85c4c77303e5` | (27, 41, 16) | 3^3 4^5 5^2 6^3 7^2 11^1 | 1 | 118 P-4n2 (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 118:P[other1] | 67.18 |
| 162 | `1a1c3bd1605b8d49` | (34, 51, 19) | 3^4 4^7 5^2 7^2 8^1 10^3 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=45/64 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 88:P[unres1] | 66.9 |
| 163 | `380af25f9f89e9cb` | (34, 51, 19) | 3^4 4^6 6^4 7^2 8^2 12^1 | 1 | 122 I-42d (1/8,1/6,5/12) b=231/160 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 122:P[other1] | 66.9 |
| 164 | `92bf045ba0459aac` | (34, 51, 19) | 3^6 4^2 5^4 6^2 8^1 9^4 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=11/16 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 110:P[other1] | 66.9 |
| 165 | `a61431a36c84685b` | (34, 51, 19) | 3^4 4^5 5^2 6^6 10^1 14^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=9/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 122:P[other1] | 66.9 |
| 166 | `aa01fff49d9706e8` | (34, 51, 19) | 3^4 4^8 7^2 8^4 12^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=29/16 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 122:P[other1] | 66.9 |
| 167 | `50296e97987286bc` | (33, 50, 19) | 3^4 4^8 6^2 8^2 9^2 10^1 | 1 | 80 I4_1 (1/12,3/8,1/6) b=13/16 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 80:P[other1] | 66.8 |
| 168 | `e73ddea1cde2be65` | (26, 39, 15) | 4^5 5^6 6^2 8^2 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=3/4 | 1 | 3 | 13 | 13 | 13 | 1 |  |  | open-likely | 86:P[unres1] | 66.71 |
| 169 | `9ccf2947d0051c0c` | (20, 31, 13) | 3^1 4^6 5^2 6^3 7^1 | 2 | 141 I4_1/amd (0,1/4,1/12) b=1 | 2 | 2 | 8 | 8 | 16 | 1 |  |  | open-likely | 141:P[unres1] | 66.63 |
| 170 | `205e338c517ee1e4` | (34, 51, 19) | 3^2 4^11 6^3 10^2 14^1 | 2 | 93 P4_222 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 9 | 4 | 119 | 2 | 1 |  | open-likely | 93:P[other1] 134:Pb[same1] | 66.6 |
| 171 | `5f2e35e62d0aa64d` | (32, 48, 18) | 3^2 4^6 5^2 6^5 8^2 10^1 | 1 | 80 I4_1 (1/12,3/8,1/6) b=39/40 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 80:P[unres1] | 66.58 |
| 172 | `9f05491e6b5385fa` | (32, 48, 18) | 3^4 5^10 7^2 8^1 12^1 | 1 | 96 P4_32_12 (1/8,1/6,5/12) b=19/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 96:P[other1] | 66.58 |
| 173 | `32451695e287120d` | (30, 45, 17) | 3^2 4^7 5^2 6^2 7^2 10^2 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=17/8 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 86:P[unres1] | 66.48 |
| 174 | `74076f8341f71199` | (24, 36, 14) | 4^3 5^6 6^5 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=1 | 1 | 3 | 24 | 16 | 43 | 3 |  |  | open-likely | 88:P[other1] 133:Pb[unres1] 142:Pb[unres1] | 66.34 |
| 175 | `9dd29764e82d4595` | (28, 42, 16) | 4^9 6^4 8^3 | 2 | 142 I4_1/acd (1/8,1/6,5/12) b=3/4 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 142:P[unres1] | 66.32 |
| 176 | `18a28588043ce475` | (28, 42, 16) | 4^7 5^2 6^4 7^2 8^1 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 |  |  | open-likely | 92:P[other1] | 65.97 |
| 177 | `36148833db116d9b` | (32, 48, 18) | 3^6 5^4 6^1 7^6 10^1 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=57/40 | 1 | 3 | 1 | 1 | 2 | 2 |  | 1b,P5-only | wall-suspect | 92:P[other1] 96:P[other1] | 65.58 |
| 178 | `ee87e3504746e36b` | (30, 45, 17) | 3^4 4^4 6^4 7^2 8^3 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=5/8 | 1 | 3 | 5 | 3 | 5 | 2 |  | P5-only | open-likely | 92:P[other1] 96:P[unres1] | 65.52 |
| 179 | `686f3af67d8e9d60` | (23, 35, 14) | 3^1 4^3 5^5 6^5 | 2 | 141 I4_1/amd (0,1/4,1/12) b=1/2 | 2 | 2 | 6 | 6 | 12 | 1 |  |  | open-likely | 141:Pb[unres1] | 65.52 |
| 180 | `46f335670d41c77e` | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 1 | 80 I4_1 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 6 | 4 | 6 | 1 |  | P5-only | open-likely | 80:P[other1] | 65.38 |
| 181 | `29f80b9c127f79a9` | (28, 42, 16) | 3^2 4^5 5^2 6^3 7^2 8^2 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=9/8 | 1 | 3 | 5 | 3 | 5 | 2 |  | P5-only | open-likely | 92:P[other1] 96:P[unres1] | 65.32 |
| 182 | `94a19a39b99e1366` | (28, 42, 16) | 3^2 4^6 5^2 6^2 8^4 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=1/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 142:P[unres1] | 65.32 |
| 183 | `1722d568b932f832` | (27, 41, 16) | 4^10 5^2 6^2 8^1 12^1 | 2 | 134 P4_2/nnm (1/12,1/12,1/12) b=5/4 | 2 | 2 | 29 | 14 | 224 | 3 | 2 |  | open-likely | 93:Pb[same1] 134:P[unres1] 142:Pb[same1] | 65.22 |
| 184 | `1177844bd4d28549` | (38, 57, 21) | 3^6 4^8 6^3 10^2 12^1 14^1 | 1 | 93 P4_222 (1/12,3/8,1/6) b=2 | 1 | 3 | 2 | 2 | 2 | 1 | 1 |  | indeterminate | 93:Pb[same1] | 65.18 |
| 185 | `27c3157c53e6288d` | (28, 42, 16) | 4^7 5^4 6^2 8^3 | 2 | 122 I-42d (1/12,3/8,1/6) b=7/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 122:P[other1] | 65.18 |
| 186 | `26a8212cbd6c8b62` | (30, 45, 17) | 3^2 4^3 5^8 6^1 8^2 10^1 | 1 | 96 P4_32_12 (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 96:P[unres1] | 65.17 |
| 187 | `c6005fa4af1a744c` | (21, 32, 13) | 4^2 5^10 6^1 | 4 | 77 P4_2 (1/12,3/8,1/6) b=1/2 | 4 | 1 | 42 | 10 | 1922 | 12 | 12 |  | open-likely | 77:Pb[same1] 81:Pb[same1] 84:Pb[same1] 92:Pb[same1] 94:Pb[same1] 96:Pb[same1] 102:Pb[same1] 110:Pb[same1] 113:Pb[same1] 114:Pb[same1] 118:Pb[same1] 136:Pb[same1] | 64.83 |
| 188 | `b8b72db4ab55a296` | (24, 37, 15) | 3^5 4^2 5^2 6^4 7^1 10^1 | 2 | 134 P4_2/nnm (1/12,1/12,1/12) b=3/2 | 2 | 2 | 38 | 9 | 368 | 6 | 4 |  | open-likely | 93:Pb[same1] 94:Pb[same1] 116:Pb[same1] 118:Pb[same1] 134:P[unres1] 138:A | 64.77 |
| 189 | `9f3af33a5a619342` | (26, 39, 15) | 4^6 5^4 6^3 8^2 | 1 | 92 P4_12_12 (1/12,3/8,1/6) b=7/4 | 1 | 3 | 6 | 5 | 9 | 2 |  |  | open-likely | 92:P[other1] 96:P[unres1] | 64.75 |
| 190 | `779fb53b92dfc3fe` | (22, 34, 14) | 4^8 6^6 | 4 | 88 I4_1/a (0,1/4,1/8) b=1 | 4 | 0 | 36 | 9 | 1308 | 9 | 5 |  | open-likely | 80:Pb[same1] 82:Pb[same1] 88:P[unres1] 98:P[other1] 109:Pb[same1] 118:Pb[same1] 119:Pb[same1] 122:Pb[other1] 141:P[unres1] | 64.74 |
| 191 | `21b95840a9be0aaf` | (30, 45, 17) | 3^6 4^3 6^3 8^4 10^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 122:P[other1] | 64.38 |
| 192 | `cc1e165a04008058` | (30, 45, 17) | 3^2 4^8 6^4 8^1 10^2 | 1 | 133 P4_2/nbc (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 133:P[unres1] | 64.38 |
| 193 | `42f6d76b9fc019fd` | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 142:P[unres1] | 64.28 |
| 194 | `5ae136b2bdd40066` | (28, 42, 16) | 3^2 4^4 5^2 6^5 7^2 8^1 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 86:P[unres1] | 64.18 |
| 195 | `f78cb8eda2f6b557` | (28, 42, 16) | 3^2 4^3 5^4 6^4 7^2 8^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 86:P[unres1] | 64.18 |
| 196 | `343d241f8d586edb` | (28, 42, 16) | 3^4 4^3 6^6 8^3 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=3/2 | 1 | 3 | 6 | 6 | 10 | 1 |  |  | open-likely | 88:P[unres1] | 64.16 |
| 197 | `81d176073d947bda` | (28, 42, 16) | 3^2 4^5 6^8 10^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=5/4 | 1 | 3 | 7 | 7 | 7 | 1 |  |  | open-likely | 142:P[unres1] | 63.91 |
| 198 | `82552e4e499d0b46` | (34, 51, 19) | 3^8 4^2 6^4 8^2 10^3 | 1 | 122 I-42d (1/12,3/8,1/6) b=41/64 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 122:P[other1] | 63.9 |
| 199 | `fdecd8c917108d43` | (36, 54, 20) | 3^8 4^4 5^2 8^1 9^2 10^2 12^1 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=11/4 | 1 | 3 | 3 | 3 | 3 | 1 | 1 |  | open-likely | 92:Pb[same1] | 63.77 |
| 200 | `621f14b6f0a7b371` | (32, 48, 18) | 3^6 4^2 5^2 7^4 8^4 | 1 | 96 P4_32_12 (1/8,1/6,5/12) b=2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 96:P[other1] | 63.7 |
| 201 | `8fc980b921be3244` | (32, 48, 18) | 3^6 4^3 6^4 7^2 8^2 12^1 | 1 | 86 P4_2/n (1/8,1/6,5/12) b=121/64 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 86:P[unres1] | 63.7 |
| 202 | `9aa9148ffc66fe2e` | (32, 48, 18) | 3^6 4^3 6^3 7^2 8^2 9^2 | 1 | 80 I4_1 (1/8,1/6,5/12) b=43/64 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 80:P[unres1] | 63.7 |
| 203 | `a7860d1366230469` | (32, 48, 18) | 3^2 4^6 5^6 8^2 10^2 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=9/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 92:P[other1] | 63.7 |
| 204 | `8534b49823b5b2ed` | (31, 47, 18) | 3^4 4^6 6^4 7^2 8^1 12^1 | 2 | 141 I4_1/amd (0,1/8,1/12) b=3/4 | 2 | 2 | 11 | 7 | 24 | 2 | 1 |  | open-likely | 122:Pb[same1] 141:Pb[unres1] | 63.48 |
| 205 | `c10281b956e50c34` | (26, 39, 15) | 3^2 4^3 6^10 | 4 | 88 I4_1/a (0,0,1/12) b=3/2 | 4 | 1 | 36 | 10 | 322 | 8 | 1 |  | open-likely | 88:P[unres1] 91:Pb[same1] 92:P[other1] 95:P[unres1] 96:Pb[unres1] 98:P[other1] 122:P[other1] 141:P[unres1] | 63.44 |
| 206 | `1a1a0de250f0da27` | (30, 45, 17) | 4^9 5^2 6^3 8^1 9^2 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=19/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 88:P[unres1] | 63.38 |
| 207 | `a3906799b3b200e1` | (30, 45, 17) | 4^9 5^2 6^1 7^2 8^3 | 1 | 122 I-42d (1/12,3/8,1/6) b=11/16 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 122:P[other1] | 63.38 |
| 208 | `f3322045c6a474d6` | (30, 45, 17) | 3^2 4^6 5^2 6^1 7^4 8^2 | 1 | 110 I4_1cd (1/12,3/8,1/6) b=21/32 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 110:P[other1] | 63.38 |
| 209 | `0882fd4b5b8cb62e` | (28, 42, 16) | 4^7 5^2 6^4 7^2 8^1 | 1 | 86 P4_2/n (1/12,3/8,1/6) b=5/8 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 86:P[unres1] | 63.28 |
| 210 | `4051049d6635c527` | (28, 42, 16) | 3^4 4^1 5^4 6^3 7^2 8^2 | 1 | 110 I4_1cd (1/12,3/8,1/6) b=29/20 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 110:P[other1] | 63.28 |
| 211 | `6eb2bc88106b9dcd` | (26, 39, 15) | 4^4 5^4 6^7 | 2 | 142 I4_1/acd (1/8,1/6,5/12) b=1 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 142:P[unres1] | 63.12 |
| 212 | `b96cf29a9246cd2c` | (26, 39, 15) | 4^7 6^7 8^1 | 2 | 142 I4_1/acd (1/12,3/8,1/6) b=1 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 142:P[unres1] | 63.12 |
| 213 | `c8c6299f9321c3cb` | (28, 42, 16) | 4^8 6^6 8^2 | 2 | 91 P4_122 (0,1/12,0) b=3/4 | 2 | 1 | 33 | 9 | 534 | 3 | 1 |  | open-likely | 91:Pb[same1] 95:Pb[unres1] 96:P[unres1] | 63.07 |
| 214 | `f053ea3ad815eb3c` | (26, 39, 15) | 3^2 4^3 5^2 6^7 8^1 | 1 | 98 I4_122 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 98:P[other1] | 62.98 |
| 215 | `dbbd406100689384` | (26, 41, 17) | 3^4 4^8 6^2 8^2 10^1 | 2 | 98 I4_122 (1/12,1/12,0) b=1/2 | 2 | 1 | 13 | 7 | 80 | 5 | 5 |  | open-likely | 80:Pb[same1] 91:Pb[same1] 92:Pb[same1] 96:Pb[same1] 98:Pb[same1] | 62.83 |
| 216 | `d70cf5c792428eab` | (24, 37, 15) | 3^2 4^5 5^2 6^5 8^1 | 1 | 126 P4/nnc (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 126:P[unres1] | 62.78 |
| 217 | `c7bba76d2396a322` | (28, 42, 16) | 3^4 5^8 8^4 | 2 | 76 P4_1 (1/8,1/6,5/12) b=1/2 | 2 | 1 | 17 | 6 | 202 | 4 | 2 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 92:P[other1] 96:P[unres1] | 62.47 |
| 218 | `0498a4ecb657609d` | (26, 40, 16) | 3^8 4^2 6^1 8^4 10^1 | 2 | 98 I4_122 (1/12,1/12,0) b=2 | 2 | 1 | 20 | 12 | 212 | 3 | 3 |  | open-likely | 80:Pb[same1] 91:Pb[same1] 98:Pb[same1] | 62.43 |
| 219 | `10424bd99b31c5f2` | (20, 30, 12) | 4^10 10^2 | 40 | 141 I4_1/amd (0,1/12,1/12) b=7/4 | 2 | 2 | 28 | 11 | 112 | 3 | 2 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:Pb[unres1] | 62.22 |
| 220 | `0dfdfb923fdc461b` | (26, 39, 15) | 4^6 5^2 6^5 7^2 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 3 | 6 | 1 |  |  | open-likely | 110:P[other1] | 61.81 |
| 221 | `de4e90813b269574` | (28, 42, 16) | 3^2 4^3 5^4 6^3 7^4 | 1 | 82 I-4 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 2 | 2 | 3 | 1 |  |  | indeterminate | 82:P[other1] | 61.8 |
| 222 | `5a7de3df1296531a` | (28, 42, 16) | 3^2 4^6 6^5 8^3 | 1 | 133 P4_2/nbc (1/12,3/8,1/6) b=1 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 133:P[unres1] | 61.28 |
| 223 | `82a5a88ccba80d26` | (13, 20, 9) | 4^5 5^4 | 8 | 82 I-4 (0,0,1/12) b=7/4 | 8 | 1 | 59 | 16 | 3064 | 28 | 23 |  | open-likely | 82:Pb[same1] 84:Pb[same1] 86:Pb[unres1] 87:Pb[same1] 91:Pb[same1] 92:Pb[same1] 93:Pb[same1] 94:Pb[same1] 95:Pb[same1] 96:Pb[same1] 97:Pb[same1] 112:Pb[same1] 114:Pb[same1] 116:Pb[same1] 118:Pb[same1] 119:Pb[same1] 121:Pb[same1] 126:A 128:Pb[same1] 131:Pb[same1] 132:Pb[same1] 134:Pb[same1] 135:Pb[same1] 136:Pb[same1] 137:Pb[unres1] 138:Pb[unres1] 139:Pb[same1] 142:Pb[unres1] | 61.25 |
| 224 | `4a1fffe528971ffb` | (23, 35, 14) | 4^6 5^6 8^2 | 2 | 138 P4_2/ncm (1/12,5/12,1/12) b=5/4 | 2 | 2 | 60 | 14 | 656 | 6 | 4 |  | open-likely | 94:Pb[same1] 98:Pb[same1] 116:Pb[same1] 122:Pb[same1] 138:A 141:Pb[unres1] | 61.24 |
| 225 | `3e1c2f08dd535cc5` | (38, 57, 21) | 3^6 4^7 5^2 6^2 10^2 12^1 14^1 | 1 | 94 P4_22_12 (1/12,3/8,1/6) b=37/16 | 1 | 3 | 2 | 2 | 2 | 1 | 1 | P5-only | indeterminate | 94:Pb[same1] | 61.18 |
| 226 | `edc763d5d4420075` | (28, 42, 16) | 3^2 4^5 5^2 6^4 8^3 | 1 | 142 I4_1/acd (1/12,3/8,1/6) b=5/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 142:P[unres1] | 61.18 |
| 227 | `dcc0a70baf02d3d7` | (14, 21, 9) | 4^3 5^6 | 12 | 87 I4/m (0,1/12,0) b=1/2 | 4 | 1 | 62 | 13 | 2564 | 21 | 13 |  | open-likely | 79:Pb[same1] 82:Pb[same1] 87:Pb[same1] 90:Pb[same1] 97:Pb[same1] 102:Pb[same1] 104:Pb[same1] 107:Pb[same1] 113:Pb[same1] 114:Pb[same1] 119:P[other1] 121:Pb[same1] 126:Pb[unres1] 128:P[other1] 129:P[unres1] 134:Pb[unres1] 136:P[other1] 137:P[unres1] 138:Pb[same1] 139:Pb[same1] 141:P[unres1] | 61.03 |
| 228 | `6fe445ec5becddde` | (20, 31, 13) | 4^9 5^2 8^2 | 4 | 88 I4_1/a (0,0,1/12) b=7/4 | 4 | 1 | 23 | 11 | 304 | 6 | 3 |  | open-likely | 88:P[unres1] 91:Pb[same1] 95:Pb[same1] 98:Pb[same1] 122:P[other1] 141:P[unres1] | 61.01 |
| 229 | `be5425f5a03b6db4` | (18, 27, 11) | 4^2 5^8 6^1 | 4 | 84 P4_2/m (1/8,1/6,5/12) b=5/4 | 1 | 3 | 16 | 15 | 24 | 1 |  |  | open-likely | 84:Pb[other1] | 60.77 |
| 230 | `b77e98e2c4a01aad` | (30, 45, 17) | 3^2 4^5 5^4 6^1 7^2 8^3 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=37/64 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 88:P[unres1] | 60.5 |
| 231 | `1f2332434c9e64b8` | (30, 45, 17) | 3^4 4^3 6^7 8^3 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=17/20 | 1 | 3 | 4 | 4 | 4 | 1 |  | P5-only | open-likely | 142:P[unres1] | 60.48 |
| 232 | `0d55f30856d2734f` | (21, 32, 13) | 3^5 4^4 6^1 8^2 11^1 | 2 | 141 I4_1/amd (0,1/4,1/12) b=327/200 | 2 | 2 | 5 | 5 | 10 | 1 |  | P5-only | open-likely | 141:P[unres1] | 60.43 |
| 233 | `8d5cf695b24cb063` | (28, 42, 16) | 3^4 4^3 5^2 6^1 7^4 8^2 | 2 | 94 P4_22_12 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 10 | 5 | 74 | 4 | 3 |  | open-likely | 94:P[other1] 106:Pb[same1] 117:Pb[same1] 135:Pb[same1] | 60.29 |
| 234 | `52392121966e66eb` | (10, 15, 7) | 4^5 5^2 | 20 | 75 P4 (1/8,1/6,5/12) b=1/2 | 4 | 1 | 59 | 18 | 7218 | 27 | 25 |  | open-likely | 75:Pb[same1] 81:Pb[same1] 83:Pb[same1] 84:Pb[same1] 87:Pb[same1] 88:Pb[unres1] 90:Pb[same1] 91:Pb[same1] 93:Pb[same1] 94:Pb[same1] 98:Pb[same1] 100:Pb[same1] 104:Pb[same1] 106:Pb[same1] 112:Pb[same1] 113:Pb[same1] 114:Pb[same1] 117:Pb[same1] 118:Pb[same1] 122:Pb[same1] 127:Pb[same1] 128:Pb[same1] 131:Pb[same1] 132:Pb[same1] 135:Pb[same1] 136:Pb[same1] 141:Pb[unres1] | 60.03 |
| 235 | `1457e9a93eea5438` | (26, 39, 15) | 4^5 5^4 6^5 8^1 | 2 | 94 P4_22_12 (1/12,3/8,1/6) b=3/4 | 2 | 2 | 31 | 10 | 308 | 3 | 2 |  | open-likely | 94:Pb[same1] 116:Pb[same1] 138:A | 60.0 |
| 236 | `896e9cc347268b4d` | (38, 57, 21) | 3^6 4^7 6^1 8^6 14^1 | 1 | 118 P-4n2 (1/12,3/8,1/6) b=29/20 | 1 | 3 | 3 | 3 | 3 | 1 | 1 | P5-only | open-likely | 118:Pb[same1] | 59.97 |
| 237 | `637fec5274f3a3e2` | (30, 45, 17) | 3^2 4^5 5^4 6^2 8^4 | 2 | 112 P-42c (1/12,3/8,1/6) b=1/2 | 2 | 2 | 9 | 4 | 103 | 2 | 1 |  | open-likely | 112:P[other1] 121:Pb[same1] | 59.89 |
| 238 | `b062a24492a59606` | (23, 35, 14) | 3^6 4^2 6^3 8^2 10^1 | 2 | 119 I-4m2 (0,1/12,1/12) b=5/4 | 2 | 2 | 44 | 15 | 752 | 3 | 3 |  | open-likely | 82:Pb[same1] 118:Pb[same1] 119:Pb[same1] | 59.64 |
| 239 | `8b7f38eb72520356` | (18, 28, 12) | 3^6 6^5 8^1 | 2 | 141 I4_1/amd (0,1/12,1/3) b=7/2 | 2 | 2 | 3 | 3 | 42 | 1 |  |  | open-likely | 141:P[unres1] | 59.61 |
| 240 | `05578fa7044fded7` | (22, 34, 14) | 3^4 4^1 5^4 6^4 8^1 | 1 | 130 P4/ncc (1/12,3/8,1/6) b=1/2 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 130:P[unres1] | 59.58 |
| 241 | `e948828e76447bbb` | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 88 I4_1/a (1/8,1/6,5/12) b=5/4 | 2 | 1 | 37 | 17 | 204 | 4 | 1 |  | open-likely | 88:P[other1] 110:Pb[unres1] 120:Pb[same1] 142:Pb[unres1] | 59.34 |
| 242 | `822fbf394c878292` | (34, 51, 19) | 3^4 4^7 6^2 7^4 10^1 12^1 | 1 | 116 P-4c2 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 14 | 8 | 17 | 2 | 2 |  | open-likely | 116:Pb[same1] 118:Pb[same1] | 59.27 |
| 243 | `96671ea7ca1f2450` | (28, 42, 16) | 3^4 4^2 6^6 7^4 | 2 | 84 P4_2/m (1/12,1/8,0) b=3/4 | 2 | 2 | 26 | 6 | 240 | 3 | 3 |  | open-likely | 77:Pb[same1] 81:Pb[same1] 84:Pb[same1] | 59.16 |
| 244 | `9b7039e0c295ff94` | (12, 18, 8) | 3^4 6^4 | 24 | 87 I4/m (1/12,1/12,0) b=1/2 | 4 | 1 | 67 | 15 | 2128 | 21 | 11 |  | open-likely | 79:Pb[same1] 84:Pb[same1] 87:P[other1] 90:Pb[same1] 93:Pb[same1] 97:Pb[same1] 104:Pb[same1] 105:Pb[same1] 107:Pb[same1] 115:P[other1] 119:P[other1] 121:P[other1] 126:A 128:Pb[same1] 129:A 131:Pb[same1] 132:P[other1] 134:P[unres1] 136:P[other1] 137:P[unres1] 139:Pb[same1] | 58.65 |
| 245 | `7824c3404ec7c532` | (14, 23, 11) | 4^10 6^1 | 4 | 79 I4 (1/8,1/6,5/12) b=1 | 4 | 1 | 49 | 20 | 4881 | 24 | 19 |  | open-likely | 79:Pb[same1] 82:Pb[same1] 85:Pb[unres1] 87:Pb[same1] 89:Pb[same1] 94:Pb[same1] 97:Pb[same1] 103:Pb[same1] 106:Pb[same1] 108:Pb[same1] 112:Pb[same1] 114:Pb[same1] 116:Pb[same1] 117:Pb[same1] 120:Pb[same1] 121:Pb[same1] 124:Pb[same1] 125:Pb[same1] 126:Pb[unres1] 130:Pb[unres1] 133:Pb[unres1] 135:Pb[same1] 138:A 140:Pb[same1] | 58.59 |
| 246 | `adc735c0ace21b40` | (20, 33, 15) | 3^2 4^10 6^2 8^1 | 2 | 98 I4_122 (1/6,1/6,0) b=1 | 2 | 1 | 1 | 1 | 4 | 1 |  | 1b | wall-suspect | 98:P[other1] | 58.48 |
| 247 | `ef0bcf47327dee5c` | (38, 57, 21) | 3^6 4^7 6^2 7^2 8^2 12^1 14^1 | 1 | 116 P-4c2 (1/8,1/6,5/12) b=1239/800 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1b,P5-only | wall-suspect | 116:Pb[same1] | 58.3 |
| 248 | `5fdbcfbd23c2a589` | (36, 54, 20) | 3^6 4^4 5^2 6^5 8^1 12^1 14^1 | 1 | 116 P-4c2 (1/12,3/8,1/6) b=73/32 | 1 | 3 | 2 | 2 | 2 | 1 | 1 | P5-only | indeterminate | 116:Pb[same1] | 57.98 |
| 249 | `89e47e7dcaab4687` | (36, 54, 20) | 3^2 4^12 6^3 10^1 12^1 14^1 | 1 | 93 P4_222 (1/12,3/8,1/6) b=59/32 | 1 | 3 | 2 | 2 | 2 | 1 | 1 | P5-only | indeterminate | 93:Pb[same1] | 57.98 |
| 250 | `eab762a24b28a094` | (26, 39, 15) | 3^2 4^2 5^6 6^3 8^2 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 88:P[unres1] | 57.98 |
| 251 | `75fb0b80b43ec683` | (34, 51, 19) | 3^4 4^7 6^4 8^2 10^1 12^1 | 1 | 93 P4_222 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 11 | 6 | 11 | 2 | 2 |  | open-likely | 93:Pb[same1] 94:Pb[same1] | 57.7 |
| 252 | `82b129fb96de7dae` | (22, 33, 13) | 3^3 4^5 5^1 6^1 7^1 9^1 10^1 | 1 | 134 P4_2/nnm (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 134:P[unres1] | 57.68 |
| 253 | `d1c13a36caa38829` | (16, 26, 12) | 4^9 5^2 6^1 | 4 | 141 I4_1/amd (0,1/8,5/12) b=3/2 | 2 | 2 | 2 | 1 | 4 | 1 |  |  | indeterminate | 141:P[unres1] | 57.58 |
| 254 | `5561cb5efa0a7c0c` | (28, 42, 16) | 3^4 4^2 5^4 6^1 7^2 8^3 | 1 | 96 P4_32_12 (1/12,3/8,1/6) b=23/8 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b,P5-only | wall-suspect | 96:P[unres1] | 57.3 |
| 255 | `ae7f4681011715ee` | (25, 38, 15) | 3^4 5^6 6^1 7^4 | 2 | 80 I4_1 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 11 | 7 | 482 | 2 | 2 |  | open-likely | 80:Pb[same1] 109:Pb[same1] | 57.29 |
| 256 | `2626c0b5370635a6` | (18, 29, 13) | 3^6 4^1 6^6 | 4 | 79 I4 (1/12,3/8,1/6) b=1/2 | 4 | 1 | 20 | 7 | 455 | 23 | 19 |  | open-likely | 79:Pb[same1] 82:Pb[same1] 85:Pb[same1] 87:Pb[same1] 89:Pb[same1] 94:Pb[same1] 97:Pb[same1] 103:Pb[same1] 106:Pb[same1] 108:Pb[same1] 112:Pb[same1] 116:Pb[same1] 117:Pb[same1] 120:Pb[same1] 121:Pb[same1] 124:Pb[same1] 125:P[unres1] 126:P[unres1] 130:P[unres1] 133:Pb[same1] 135:Pb[same1] 138:A 140:Pb[same1] | 57.22 |
| 257 | `9cab1436007f3c03` | (22, 34, 14) | 3^6 5^2 6^4 8^2 | 4 | 88 I4_1/a (0,0,1/6) b=7/2 | 4 | 1 | 8 | 3 | 46 | 6 | 2 |  | open-likely | 88:P[unres1] 91:Pb[same1] 95:Pb[same1] 98:P[other1] 122:P[other1] 141:P[unres1] | 57.12 |
| 258 | `80b68f2e4481cfeb` | (25, 39, 16) | 4^9 5^4 7^2 8^1 | 1 | 80 I4_1 (1/12,3/8,1/6) b=1 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 80:P[other1] | 57.0 |
| 259 | `2af1083dea2057de` | (26, 40, 16) | 3^6 4^1 5^4 7^4 10^1 | 2 | 109 I4_1md (0,1/12,0) b=5/4 | 2 | 2 | 4 | 4 | 128 | 1 | 1 |  | open-likely | 109:Pb[same1] | 56.62 |
| 260 | `d58442effff48685` | (16, 24, 10) | 4^6 6^4 | 8 | 121 I-42m (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 9 | 13 | 1 |  |  | open-likely | 121:P[other1] | 56.48 |
| 261 | `3c177440d8084cb5` | (18, 27, 11) | 3^1 4^5 5^2 6^1 7^1 8^1 | 1 | 134 P4_2/nnm (1/8,1/6,5/12) b=3/4 | 1 | 3 | 11 | 8 | 12 | 1 |  |  | open-likely | 134:P[unres1] | 56.27 |
| 262 | `fc7f08307d0c3900` | (34, 51, 19) | 3^4 4^8 6^3 9^2 10^1 12^1 | 1 | 120 I-4c2 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 6 | 11 | 1 | 1 |  | open-likely | 120:Pb[same1] | 56.12 |
| 263 | `27d2f55670d4f85c` | (27, 41, 16) | 3^1 4^9 5^1 6^2 8^2 10^1 | 2 | 134 P4_2/nnm (1/6,1/6,1/12) b=5/4 | 2 | 2 | 7 | 7 | 28 | 2 | 1 |  | open-likely | 118:Pb[same1] 134:P[unres1] | 56.1 |
| 264 | `6a8a2df1eaf9f29d` | (24, 36, 14) | 4^4 5^4 6^6 | 2 | 94 P4_22_12 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 30 | 21 | 763 | 4 | 2 |  | open-likely | 94:P[other1] 106:Pb[other1] 117:Pb[same1] 135:Pb[same1] | 56.08 |
| 265 | `b9d2f3e02e91b42b` | (30, 47, 19) | 3^11 5^2 6^2 7^1 9^2 14^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=19/16 | 2 | 2 | 3 | 3 | 6 | 2 | 2 | P5-only | open-likely | 122:Pb[same1] 141:Pb[same1] | 55.88 |
| 266 | `32b4d3d2ab4957a6` | (20, 31, 13) | 4^7 5^2 6^4 | 1 | 126 P4/nnc (1/8,1/6,5/12) b=1/2 | 1 | 3 | 9 | 6 | 10 | 1 |  |  | open-likely | 126:P[unres1] | 55.53 |
| 267 | `3e83ba1555125b93` | (25, 38, 15) | 3^2 4^3 5^4 6^5 8^1 | 2 | 84 P4_2/m (1/12,1/4,0) b=4/5 | 2 | 2 | 15 | 4 | 104 | 3 | 3 |  | open-likely | 77:Pb[same1] 81:Pb[same1] 84:Pb[same1] | 55.47 |
| 268 | `7b0441c8ac019b55` | (25, 38, 15) | 3^2 4^8 6^1 8^4 | 2 | 90 P42_12 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 21 | 9 | 161 | 5 | 5 |  | open-likely | 90:Pb[same1] 104:Pb[same1] 114:Pb[same1] 118:Pb[same1] 128:Pb[same1] | 55.12 |
| 269 | `419d0b18626b622e` | (31, 48, 19) | 3^6 4^7 6^2 8^2 10^1 12^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=1 | 1 | 3 | 8 | 8 | 8 | 1 | 1 |  | open-likely | 91:Pb[same1] | 54.85 |
| 270 | `d648a739129d46df` | (26, 39, 15) | 4^7 6^7 8^1 | 2 | 98 I4_122 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 22 | 8 | 147 | 3 | 2 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:Pb[unres1] | 54.42 |
| 271 | `03132752288b78be` | (32, 48, 18) | 3^2 4^8 5^2 6^3 8^1 10^1 12^1 | 1 | 93 P4_222 (1/12,3/8,1/6) b=1 | 1 | 3 | 13 | 13 | 13 | 1 | 1 |  | open-likely | 93:Pb[same1] | 54.31 |
| 272 | `1b269a7a84560401` | (26, 39, 15) | 4^4 5^6 6^3 7^2 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=5/8 | 1 | 3 | 2 | 2 | 2 | 1 |  | P5-only | indeterminate | 88:P[unres1] | 53.98 |
| 273 | `1811b0d16d82bdda` | (16, 24, 10) | 3^3 4^1 5^2 6^3 7^1 | 1 | 134 P4_2/nnm (1/8,1/6,5/12) b=5/4 | 1 | 3 | 19 | 8 | 22 | 2 |  |  | open-likely | 134:P[unres1] 138:P[unres1] | 53.88 |
| 274 | `f2338eb96662d54f` | (18, 28, 12) | 3^2 4^8 8^1 10^1 | 4 | 141 I4_1/amd (0,1/8,1/12) b=3/2 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 141:P[unres1] | 53.68 |
| 275 | `abfdf73c2f298784` | (12, 18, 8) | 4^4 5^4 | 8 | 80 I4_1 (0,0,0) b=9/4 | 8 | 0 | 24 | 12 | 1112 | 12 | 8 |  | open-likely | 76:Pb[same1] 78:Pb[same1] 80:Pb[same1] 88:Pb[same1] 91:Pb[same1] 92:Pb[same1] 95:Pb[unres1] 96:P[unres1] 98:P[other1] 109:Pb[same1] 122:P[other1] 141:Pb[same1] | 53.64 |
| 276 | `d84f3b8159a92b4b` | (20, 31, 13) | 4^7 5^2 6^4 | 1 | 130 P4/ncc (1/8,1/6,5/12) b=1/2 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 130:P[unres1] | 53.38 |
| 277 | `6b1f36550e2f6ec6` | (22, 34, 14) | 3^6 4^2 6^3 8^3 | 2 | 137 P4_2/nmc (0,1/12,1/12) b=5/4 | 2 | 2 | 33 | 11 | 196 | 3 | 2 |  | open-likely | 94:Pb[same1] 114:Pb[same1] 137:P[unres1] | 52.81 |
| 278 | `da1833391efcd38c` | (30, 45, 17) | 3^4 4^1 5^6 6^4 10^2 | 1 | 116 P-4c2 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 18 | 12 | 41 | 2 | 2 |  | open-likely | 116:Pb[same1] 118:Pb[same1] | 52.43 |
| 279 | `adbb83c95151fc35` | (30, 45, 17) | 3^4 4^3 5^2 6^6 10^2 | 1 | 93 P4_222 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 18 | 12 | 40 | 2 | 2 |  | open-likely | 93:Pb[same1] 94:Pb[same1] | 52.38 |
| 280 | `2ae9d568eb9bfb4c` | (14, 21, 9) | 3^2 4^2 5^3 6^1 7^1 | 2 | 141 I4_1/amd (1/8,1/6,5/12) b=1 | 1 | 3 | 15 | 9 | 16 | 1 |  |  | open-likely | 141:P[unres1] | 52.34 |
| 281 | `15a334b4c643f5b6` | (18, 27, 11) | 3^2 4^5 7^4 | 2 | 138 P4_2/ncm (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 6 | 6 | 1 |  |  | open-likely | 138:P[unres1] | 51.18 |
| 282 | `cc7af78c512b51be` | (13, 20, 9) | 3^3 4^1 5^4 7^1 | 2 | 84 P4_2/m (1/8,1/6,5/12) b=1/2 | 2 | 2 | 3 | 1 | 9 | 2 |  |  | indeterminate | 84:P[other1] 136:P[other1] | 50.95 |
| 283 | `8c0bde1b0fee079d` | (32, 48, 18) | 3^2 4^8 5^2 6^1 7^2 8^2 12^1 | 1 | 118 P-4n2 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 6 | 4 | 7 | 1 | 1 |  | open-likely | 118:Pb[same1] | 50.87 |
| 284 | `1fcd5245be090d59` | (23, 36, 15) | 3^2 4^6 5^2 6^4 8^1 | 1 | 142 I4_1/acd (1/8,1/6,5/12) b=2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 142:P[unres1] | 50.8 |
| 285 | `206c7c14af9927b2` | (18, 29, 13) | 3^4 4^4 6^5 | 2 | 90 P42_12 (1/8,1/6,5/12) b=3/4 | 2 | 2 | 35 | 20 | 704 | 5 | 5 |  | open-likely | 90:Pb[same1] 104:Pb[same1] 114:Pb[same1] 118:Pb[same1] 128:Pb[same1] | 50.07 |
| 286 | `8fa1790edfd55a9f` | (17, 26, 11) | 3^2 4^4 5^1 6^3 7^1 | 2 | 134 P4_2/nnm (1/12,1/12,1/12) b=2 | 2 | 2 | 34 | 12 | 672 | 6 | 4 |  | open-likely | 93:Pb[same1] 94:Pb[same1] 116:Pb[same1] 118:Pb[same1] 134:Pb[unres1] 138:A | 50.05 |
| 287 | `d059d2ebab300484` | (31, 47, 18) | 3^4 4^6 6^4 7^2 8^1 12^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=7/4 | 1 | 3 | 5 | 5 | 5 | 1 | 1 |  | open-likely | 91:Pb[same1] | 49.62 |
| 288 | `b17c6249a65c9ab6` | (30, 45, 17) | 3^4 4^4 5^2 6^3 8^3 10^1 | 1 | 120 I-4c2 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 9 | 5 | 10 | 1 | 1 |  | open-likely | 120:Pb[same1] | 49.53 |
| 289 | `9ca699788f254f08` | (30, 46, 18) | 3^4 4^8 6^2 7^2 8^1 14^1 | 1 | 97 I422 (1/8,1/6,5/12) b=1 | 1 | 3 | 5 | 5 | 5 | 1 | 1 |  | open-likely | 97:Pb[same1] | 49.52 |
| 290 | `07db8b31cf7776c5` | (21, 32, 13) | 4^4 5^6 6^3 | 2 | 141 I4_1/amd (0,1/12,1/3) b=3/2 | 2 | 2 | 41 | 13 | 174 | 2 | 1 |  | open-likely | 122:Pb[same1] 141:P[unres1] | 49.49 |
| 291 | `ad192c7f4c277ecf` | (29, 44, 17) | 3^5 4^2 5^2 6^5 7^2 11^1 | 1 | 118 P-4n2 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 9 | 9 | 9 | 1 | 1 |  | open-likely | 118:Pb[same1] | 49.22 |
| 292 | `74b20b492f403316` | (26, 39, 15) | 4^6 6^9 | 2 | 88 I4_1/a (1/12,3/8,1/6) b=9/4 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 88:P[unres1] | 49.1 |
| 293 | `eda7881fe2bb6928` | (25, 39, 16) | 3^6 4^4 7^4 8^2 | 2 | 109 I4_1md (0,1/6,0) b=53/40 | 2 | 2 | 3 | 3 | 96 | 2 | 2 | P5-only | open-likely | 80:Pb[same1] 109:Pb[same1] | 49.07 |
| 294 | `63e69de5b43a9887` | (16, 24, 10) | 3^2 4^1 5^5 6^1 7^1 | 1 | 87 I4/m (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 9 | 9 | 1 |  |  | open-likely | 87:P[other1] | 48.92 |
| 295 | `c6ba6d87ea9c38b4` | (29, 44, 17) | 3^4 4^4 5^2 6^2 7^2 8^3 | 1 | 80 I4_1 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 8 | 6 | 9 | 1 | 1 |  | open-likely | 80:Pb[same1] | 48.88 |
| 296 | `1f2da25d4fd3e5d7` | (21, 32, 13) | 3^2 4^2 5^4 6^5 | 2 | 79 I4 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 25 | 9 | 158 | 4 | 3 |  | open-likely | 79:Pb[same1] 82:Pb[same1] 85:P[unres1] 87:Pb[same1] | 48.86 |
| 297 | `3da00cbdd50d4759` | (32, 48, 18) | 3^4 4^5 5^4 8^3 10^2 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=5/4 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 110:Pb[same1] | 48.68 |
| 298 | `56dcc17ff0060c44` | (32, 48, 18) | 3^6 4^3 5^2 6^2 8^3 10^2 | 1 | 114 P-42_1c (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 114:Pb[same1] | 48.68 |
| 299 | `72aba762a764b251` | (32, 48, 18) | 3^2 4^10 6^2 8^2 10^1 12^1 | 1 | 94 P4_22_12 (1/12,3/8,1/6) b=9/4 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 94:Pb[same1] | 48.68 |
| 300 | `1ec753f439979bfc` | (18, 29, 13) | 3^4 4^2 5^4 6^3 | 2 | 142 I4_1/acd (1/12,1/12,1/4) b=7/4 | 2 | 1 | 26 | 15 | 126 | 2 | 1 |  | open-likely | 110:Pb[same1] 142:P[unres1] | 48.68 |
| 301 | `230e451f710229a7` | (20, 30, 12) | 3^3 4^2 5^3 7^4 | 1 | 138 P4_2/ncm (1/12,3/8,1/6) b=1/2 | 1 | 3 | 2 | 2 | 2 | 1 |  |  | indeterminate | 138:P[unres1] | 48.38 |
| 302 | `9acb8f9a91b47b51` | (14, 24, 12) | 4^12 | 2 | 141 I4_1/amd (0,1/8,3/8) b=1 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 141:A | 48.28 |
| 303 | `1d2c47d061a6ab6c` | (18, 28, 12) | 4^6 5^4 6^2 | 2 | 142 I4_1/acd (1/8,1/4,3/8) b=1 | 2 | 1 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 142:P[other1] | 48.18 |
| 304 | `eaf8f8e7b00c0da0` | (26, 39, 15) | 3^2 4^2 5^2 6^9 | 1 | 88 I4_1/a (1/8,1/6,5/12) b=5/2 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 88:P[unres1] | 48.1 |
| 305 | `4e7f52911cb9c8b0` | (28, 42, 16) | 3^4 4^2 5^4 6^2 8^4 | 2 | 98 I4_122 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 10 | 10 | 10 | 1 | 1 |  | open-likely | 98:Pb[same1] | 47.63 |
| 306 | `e0cb47c4a5901ef9` | (22, 36, 16) | 3^8 4^4 8^4 | 8 | 91 P4_122 (1/8,1/8,3/8) b=1 | 2 | 1 | 1 | 1 | 8 | 3 | 1 | 1b | wall-suspect | 91:P[other1] 92:Pb[same1] 95:P[unres1] | 47.54 |
| 307 | `9679c9e830167325` | (28, 42, 16) | 3^2 4^4 5^4 6^4 8^1 10^1 | 1 | 116 P-4c2 (1/12,3/8,1/6) b=1 | 1 | 3 | 12 | 12 | 12 | 1 | 1 |  | open-likely | 116:Pb[same1] | 47.52 |
| 308 | `3c3aac0251a9d3dd` | (32, 48, 18) | 3^2 4^8 5^2 6^2 7^2 10^1 12^1 | 1 | 116 P-4c2 (1/12,3/8,1/6) b=17/8 | 1 | 3 | 7 | 7 | 7 | 1 | 1 | P5-only | open-likely | 116:Pb[same1] | 47.31 |
| 309 | `3a7c6d5f00cde1ae` | (32, 48, 18) | 3^8 4^2 6^3 8^2 10^3 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=7/2 | 1 | 3 | 4 | 2 | 4 | 3 | 1 |  | indeterminate | 92:P[other1] 96:Pb[same1] 133:P[unres1] | 47.27 |
| 310 | `28fa1abcd5fcfcae` | (28, 42, 16) | 3^2 4^4 5^4 6^4 8^1 10^1 | 1 | 94 P4_22_12 (1/12,3/8,1/6) b=5/4 | 1 | 3 | 11 | 11 | 11 | 1 | 1 |  | open-likely | 94:Pb[same1] | 47.1 |
| 311 | `3d3095468486d3ff` | (22, 33, 13) | 3^5 4^2 5^2 6^2 9^1 12^1 | 2 | 141 I4_1/amd (0,1/12,1/12) b=5/2 | 2 | 2 | 9 | 6 | 18 | 3 | 2 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:P[unres1] | 47.0 |
| 312 | `b509653535640869` | (19, 29, 12) | 3^4 4^2 6^5 8^1 | 2 | 109 I4_1md (0,1/12,0) b=3/2 | 2 | 2 | 17 | 9 | 768 | 2 | 2 |  | open-likely | 80:Pb[same1] 109:Pb[same1] | 46.96 |
| 313 | `6869d9adc5f8c737` | (18, 27, 11) | 3^6 6^2 8^3 | 12 | 141 I4_1/amd (1/12,1/4,1/8) b=1/2 | 2 | 1 | 9 | 5 | 23 | 3 | 2 |  | open-likely | 109:Pb[same1] 119:Pb[same1] 141:P[unres1] | 46.94 |
| 314 | `e127689d5833b02a` | (16, 24, 10) | 3^1 4^3 5^3 6^3 | 1 | 138 P4_2/ncm (1/8,1/6,5/12) b=1/2 | 1 | 3 | 11 | 6 | 11 | 1 |  |  | open-likely | 138:P[unres1] | 46.9 |
| 315 | `7bde4c1d5a885234` | (14, 21, 9) | 3^3 4^2 5^1 6^2 8^1 | 1 | 137 P4_2/nmc (1/8,1/6,5/12) b=1 | 1 | 3 | 9 | 6 | 9 | 2 |  |  | open-likely | 137:P[unres1] 141:P[unres1] | 46.72 |
| 316 | `bf5eadab641c997b` | (28, 42, 16) | 3^4 4^2 5^2 6^4 7^2 8^2 | 1 | 88 I4_1/a (1/12,3/8,1/6) b=7/2 | 1 | 3 | 8 | 5 | 8 | 2 | 1 |  | open-likely | 88:Pb[unres1] 114:Pb[same1] | 46.55 |
| 317 | `818521767ac611bd` | (15, 25, 12) | 4^10 5^2 | 2 | 141 I4_1/amd (0,1/4,0) b=1 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 141:P[unres1] | 46.38 |
| 318 | `73c67ccc167782ff` | (24, 38, 16) | 3^2 4^9 6^4 10^1 | 2 | 141 I4_1/amd (0,1/8,1/8) b=1/2 | 2 | 2 | 4 | 3 | 10 | 2 | 1 |  | open-likely | 98:Pb[same1] 141:P[unres1] | 46.09 |
| 319 | `d0db3b3d60ce68a2` | (16, 24, 10) | 3^1 4^4 5^1 6^4 | 2 | 141 I4_1/amd (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 |  |  | open-likely | 141:P[unres1] | 46.08 |
| 320 | `f7b981bc1af0046a` | (28, 42, 16) | 3^4 4^2 5^2 6^5 8^3 | 1 | 110 I4_1cd (1/8,1/6,5/12) b=3/2 | 1 | 3 | 15 | 15 | 15 | 1 | 1 |  | open-likely | 110:Pb[same1] | 45.61 |
| 321 | `fc4719574cb9d459` | (30, 45, 17) | 3^4 4^3 5^4 6^1 7^2 8^2 10^1 | 1 | 114 P-42_1c (1/12,3/8,1/6) b=9/4 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 114:Pb[same1] | 45.48 |
| 322 | `59ec3e1d88f29e8b` | (30, 45, 17) | 3^2 4^6 6^6 7^2 10^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=3/2 | 1 | 3 | 7 | 4 | 7 | 1 | 1 |  | open-likely | 122:Pb[same1] | 45.11 |
| 323 | `845f058b04ddb75c` | (21, 32, 13) | 3^4 4^1 5^2 6^4 7^2 | 2 | 90 P42_12 (1/12,3/8,1/6) b=1/2 | 2 | 2 | 7 | 4 | 43 | 3 | 3 |  | open-likely | 90:Pb[same1] 104:Pb[same1] 128:Pb[same1] | 44.99 |
| 324 | `b39783cb7395f454` | (11, 19, 10) | 3^6 4^3 8^1 | 2 | 141 I4_1/amd (0,1/6,1/6) b=2 | 2 | 2 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 141:A | 44.98 |
| 325 | `d7e9a753e8e2e449` | (28, 42, 16) | 3^4 4^2 5^2 6^4 7^2 8^2 | 1 | 120 I-4c2 (1/8,1/6,5/12) b=1 | 1 | 3 | 6 | 4 | 8 | 1 | 1 |  | open-likely | 120:Pb[same1] | 44.72 |
| 326 | `e956ba4b05a47f01` | (20, 31, 13) | 4^5 5^6 6^2 | 2 | 141 I4_1/amd (0,1/12,0) b=1 | 2 | 2 | 19 | 8 | 54 | 2 | 1 |  | open-likely | 122:Pb[same1] 141:Pb[unres1] | 44.67 |
| 327 | `4af32e5d248c23da` | (16, 24, 10) | 3^4 5^2 6^2 7^2 | 4 | 141 I4_1/amd (1/12,1/12,0) b=1 | 2 | 1 | 25 | 6 | 51 | 2 | 1 |  | open-likely | 109:Pb[same1] 141:Pb[unres1] | 44.44 |
| 328 | `3eb68e3019868bb0` | (26, 39, 15) | 3^2 4^2 5^4 6^6 8^1 | 1 | 114 P-42_1c (1/12,3/8,1/6) b=3/4 | 1 | 3 | 17 | 13 | 17 | 2 | 1 |  | open-likely | 110:Pb[same1] 114:P[other1] | 44.03 |
| 329 | `9da8963ab70c9719` | (17, 27, 12) | 4^7 5^4 6^1 | 2 | 141 I4_1/amd (0,1/12,0) b=3/2 | 2 | 2 | 23 | 13 | 144 | 2 | 1 |  | open-likely | 122:Pb[same1] 141:P[unres1] | 44.02 |
| 330 | `327ca8d2dd09e1c0` | (26, 39, 15) | 3^2 4^2 5^4 6^6 8^1 | 2 | 96 P4_32_12 (1/8,1/6,5/12) b=1 | 1 | 3 | 7 | 4 | 8 | 2 | 1 |  | open-likely | 92:Pb[same1] 96:P[unres1] | 43.97 |
| 331 | `62ca11329dfd99e4` | (28, 42, 16) | 3^2 4^4 5^4 6^3 8^3 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=3/2 | 1 | 3 | 7 | 7 | 11 | 2 | 1 |  | open-likely | 92:Pb[same1] 96:P[unres1] | 43.79 |
| 332 | `3fea442a4ead6925` | (25, 38, 15) | 3^2 4^7 6^2 7^2 8^2 | 1 | 91 P4_122 (1/12,3/8,1/6) b=9/4 | 1 | 3 | 13 | 8 | 21 | 2 | 1 |  | open-likely | 91:Pb[same1] 95:P[unres1] | 43.59 |
| 333 | `6ab2e96429e81ed7` | (26, 40, 16) | 3^4 4^4 5^2 6^5 12^1 | 1 | 97 I422 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 9 | 7 | 10 | 1 | 1 |  | open-likely | 97:Pb[same1] | 43.13 |
| 334 | `8e1a1fd6069d5392` | (12, 19, 9) | 4^7 5^2 | 4 | 87 I4/m (1/8,1/6,5/12) b=5/4 | 2 | 2 | 32 | 20 | 376 | 6 | 6 |  | open-likely | 87:Pb[same1] 97:Pb[same1] 120:Pb[same1] 124:Pb[same1] 135:Pb[same1] 140:Pb[same1] | 43.12 |
| 335 | `f478cd4934ed8ab6` | (14, 21, 9) | 4^6 6^3 | 12 | 109 I4_1md (1/8,1/6,5/12) b=3/4 | 2 | 1 | 25 | 10 | 79 | 3 | 1 |  | open-likely | 109:Pb[same1] 119:P[other1] 141:P[unres1] | 43.1 |
| 336 | `0e291742552bfd85` | (18, 27, 11) | 3^2 4^5 6^1 7^2 8^1 | 1 | 134 P4_2/nnm (1/8,1/6,5/12) b=9/8 | 1 | 3 | 3 | 3 | 3 | 1 |  | P5-only | open-likely | 134:P[unres1] | 42.97 |
| 337 | `6016ea01a4fa7b58` | (29, 45, 18) | 3^2 4^10 6^4 10^2 | 1 | 91 P4_122 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 91:Pb[same1] | 42.38 |
| 338 | `be16ed915b8f257e` | (30, 45, 17) | 3^2 4^4 5^4 6^5 8^1 10^1 | 1 | 98 I4_122 (1/12,3/8,1/6) b=3/2 | 1 | 3 | 2 | 2 | 2 | 1 | 1 |  | indeterminate | 98:Pb[same1] | 42.38 |
| 339 | `be5b1b5360c30bf4` | (17, 26, 11) | 3^5 4^2 6^2 8^1 9^1 | 2 | 141 I4_1/amd (0,1/12,1/6) b=3 | 2 | 2 | 23 | 12 | 64 | 2 | 1 |  | open-likely | 122:Pb[same1] 141:Pb[unres1] | 42.28 |
| 340 | `b25a63276e96e094` | (19, 30, 13) | 4^5 5^8 | 4 | 84 P4_2/m (1/8,3/8,0) b=1 | 4 | 1 | 1 | 1 | 52 | 8 | 6 | 1b | wall-suspect | 81:Pb[same1] 84:Pb[same1] 94:P[other1] 102:A 113:Pb[same1] 118:Pb[same1] 122:Pb[same1] 136:Pb[same1] | 41.49 |
| 341 | `3f6b28d5f7a72d60` | (14, 21, 9) | 3^2 4^1 5^5 7^1 | 2 | 84 P4_2/m (1/12,3/8,1/6) b=1/2 | 2 | 2 | 30 | 14 | 353 | 4 | 4 |  | open-likely | 84:Pb[same1] 94:Pb[same1] 118:Pb[same1] 136:Pb[same1] | 41.42 |
| 342 | `34020552fab1d2e4` | (26, 41, 17) | 3^6 4^5 5^2 7^2 10^2 | 1 | 130 P4/ncc (1/8,1/6,5/12) b=9/10 | 1 | 3 | 4 | 4 | 4 | 1 | 1 | P5-only | open-likely | 130:Pb[same1] | 41.08 |
| 343 | `ea9086a7f597b73b` | (12, 18, 8) | 3^3 4^1 5^1 6^3 | 2 | 141 I4_1/amd (1/8,1/6,5/12) b=5/2 | 1 | 3 | 5 | 5 | 5 | 1 |  |  | open-likely | 141:P[other1] | 40.72 |
| 344 | `97fb7fde62d174ad` | (23, 36, 15) | 4^12 8^3 | 2 | 93 P4_222 (1/8,1/6,5/12) b=1/2 | 2 | 2 | 2 | 1 | 5 | 3 | 2 |  | indeterminate | 93:Pb[same1] 118:Pb[same1] 134:P[unres1] | 40.26 |
| 345 | `e3b3aae804f2c179` | (10, 15, 7) | 3^1 4^3 5^3 | 6 | 136 P4_2/mnm (1/8,1/6,5/12) b=1/2 | 2 | 2 | 51 | 15 | 406 | 4 | 3 |  | open-likely | 97:Pb[same1] 121:Pb[same1] 136:P[other1] 139:Pb[same1] | 40.19 |
| 346 | `822163f15ffc16d1` | (30, 45, 17) | 3^2 4^5 5^2 6^5 7^2 10^1 | 1 | 92 P4_12_12 (1/8,1/6,5/12) b=19/16 | 1 | 3 | 3 | 3 | 3 | 1 | 1 | P5-only | open-likely | 92:Pb[same1] | 40.17 |
| 347 | `2bb95af9090a5ea1` | (24, 37, 15) | 4^10 5^2 6^1 8^1 10^1 | 1 | 97 I422 (1/8,1/6,5/12) b=1/2 | 1 | 3 | 4 | 4 | 8 | 1 | 1 |  | open-likely | 97:Pb[same1] | 40.15 |
| 348 | `6f79177bf480b895` | (34, 51, 19) | 3^4 4^5 6^7 8^1 10^2 | 1 | 95 P4_322 (1/12,3/8,1/6) b=33/40 | 1 | 3 | 1 | 1 | 1 | 2 | 1 | 1b,P5-only | wall-suspect | 91:Pb[same1] 95:P[unres1] | 39.9 |
| 349 | `9b1c0d54955637e5` | (8, 14, 8) | 3^5 4^2 5^1 | 2 | 140 I4/mcm (1/12,1/3,0) b=1/2 | 2 | 2 | 1 | 1 | 4 | 1 |  | 1b | wall-suspect | 140:A | 39.78 |
| 350 | `519d875aa973e258` | (10, 16, 8) | 3^4 5^4 | 4 | 141 I4_1/amd (1/8,1/8,0) b=1 | 2 | 1 | 1 | 1 | 2 | 1 |  | 1b | wall-suspect | 141:P[unres1] | 39.38 |
| 351 | `9d6af8d171ee45f1` | (21, 33, 14) | 4^8 5^4 6^1 8^1 | 2 | 141 I4_1/amd (0,1/12,1/6) b=1/2 | 2 | 2 | 2 | 1 | 4 | 2 | 1 |  | indeterminate | 98:Pb[same1] 141:P[unres1] | 39.08 |
| 352 | `a69e19eb2dcae98b` | (16, 24, 10) | 3^2 4^2 5^4 7^2 | 2 | 109 I4_1md (1/8,1/6,5/12) b=1/2 | 2 | 1 | 13 | 7 | 48 | 3 | 1 |  | open-likely | 109:Pb[other1] 122:Pb[same1] 141:Pb[unres1] | 39.01 |
| 353 | `0c6ba5cadd15c06e` | (9, 16, 9) | 3^4 4^5 | 8 | 82 I-4 (0,0,1/8) b=2 | 8 | 1 | 2 | 1 | 48 | 24 | 12 |  | indeterminate | 82:Pb[same1] 84:Pb[same1] 86:P[unres1] 87:P[other1] 91:Pb[same1] 93:Pb[same1] 94:Pb[same1] 95:Pb[same1] 97:P[other1] 112:A 114:A 116:Pb[same1] 118:Pb[same1] 119:Pb[same1] 121:A 126:A 128:A 131:A 132:Pb[same1] 134:P[unres1] 135:Pb[same1] 136:Pb[same1] 137:A 139:A | 38.91 |
| 354 | `f1d0ab0fb88d1c9d` | (32, 48, 18) | 3^4 4^3 5^4 6^3 7^2 8^1 12^1 | 1 | 122 I-42d (1/12,3/8,1/6) b=2501/1600 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1b,P5-only | wall-suspect | 122:Pb[same1] | 38.7 |
| 355 | `0bc1139de57a9670` | (29, 45, 18) | 3^6 4^4 5^2 6^4 10^1 12^1 | 1 | 116 P-4c2 (1/12,3/8,1/6) b=9/4 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1b | wall-suspect | 116:Pb[same1] | 38.4 |
| 356 | `fe7ee18a2838e181` | (14, 22, 10) | 3^6 6^3 8^1 | 2 | 87 I4/m (1/12,3/8,1/6) b=3/4 | 2 | 2 | 18 | 8 | 108 | 7 | 7 |  | open-likely | 87:Pb[same1] 97:Pb[same1] 120:Pb[same1] 124:Pb[same1] 130:Pb[same1] 135:Pb[same1] 140:Pb[same1] | 38.2 |
| 357 | `38d3ab5e6be25619` | (28, 42, 16) | 3^4 4^2 6^6 7^4 | 2 | 82 I-4 (1/8,1/6,5/12) b=63/32 | 1 | 3 | 6 | 4 | 6 | 1 | 1 | P5-only | open-likely | 82:Pb[same1] | 38.18 |
| 358 | `bf5f699aaeed9ea9` | (17, 26, 11) | 4^3 5^8 | 2 | 85 P4/n (1/8,1/6,5/12) b=1/2 | 2 | 2 | 9 | 3 | 66 | 4 | 3 |  | open-likely | 79:Pb[same1] 82:Pb[same1] 85:P[unres1] 87:Pb[same1] | 37.64 |
| 359 | `68f4290f946a6883` | (28, 42, 16) | 3^4 4^3 6^5 7^2 8^2 | 1 | 112 P-42c (1/8,1/6,5/12) b=59/32 | 1 | 3 | 6 | 4 | 6 | 1 | 1 | P5-only | open-likely | 112:Pb[same1] | 37.18 |
| 360 | `6eec925b71cecc49` | (21, 33, 14) | 4^8 5^4 6^1 8^1 | 2 | 138 P4_2/ncm (1/12,5/12,1/12) b=1 | 2 | 2 | 1 | 1 | 12 | 3 | 2 | 1b | wall-suspect | 94:Pb[same1] 116:Pb[same1] 138:A | 35.74 |
| 361 | `54886fac17fe023a` | (28, 43, 17) | 3^8 4^1 6^4 7^2 8^1 12^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=15/8 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1b,P5-only | wall-suspect | 91:Pb[same1] | 35.3 |
| 362 | `b6892ba92de5db43` | (19, 30, 13) | 4^7 5^4 6^2 | 2 | 121 I-42m (1/12,1/12,1/6) b=2 | 2 | 2 | 2 | 1 | 8 | 4 | 4 |  | indeterminate | 82:Pb[same1] 112:Pb[same1] 114:Pb[same1] 121:Pb[same1] | 35.15 |
| 363 | `2a089105ae08c36d` | (14, 21, 9) | 3^3 4^2 5^2 7^1 8^1 | 2 | 141 I4_1/amd (0,1/6,1/12) b=3/2 | 2 | 2 | 10 | 10 | 20 | 3 | 2 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:P[unres1] | 34.72 |
| 364 | `c7258adeebded3ae` | (23, 36, 15) | 3^4 4^1 5^4 6^6 | 2 | 84 P4_2/m (1/12,1/3,0) b=1 | 2 | 2 | 1 | 1 | 8 | 2 | 2 | 1b | wall-suspect | 81:Pb[same1] 84:Pb[same1] | 34.55 |
| 365 | `04b26311800821b8` | (20, 32, 14) | 3^4 4^5 6^4 8^1 | 1 | 97 I422 (1/12,3/8,1/6) b=3/4 | 1 | 3 | 9 | 5 | 9 | 2 | 1 |  | open-likely | 97:Pb[same1] 130:P[unres1] | 34.32 |
| 366 | `c56e8a772aacdc9a` | (16, 26, 12) | 3^2 4^6 5^2 6^2 | 1 | 97 I422 (1/8,1/6,5/12) b=5/4 | 1 | 3 | 22 | 17 | 55 | 2 | 1 |  | open-likely | 97:Pb[same1] 130:Pb[unres1] | 34.23 |
| 367 | `7d5559ec4f268c7c` | (16, 27, 13) | 3^2 4^9 6^2 | 4 | 88 I4_1/a (0,0,1/8) b=2 | 4 | 1 | 1 | 1 | 8 | 7 | 4 | 1b | wall-suspect | 88:A 91:Pb[same1] 92:Pb[same1] 96:Pb[same1] 98:Pb[same1] 122:P[other1] 141:A | 34.16 |
| 368 | `f398b0e4ecd40949` | (12, 19, 9) | 3^3 4^3 5^1 6^2 | 1 | 109 I4_1md (1/12,3/8,1/6) b=1 | 1 | 3 | 1 | 1 | 1 | 1 |  | 1b | wall-suspect | 109:A | 33.7 |
| 369 | `37e188e9b012345e` | (20, 32, 14) | 3^4 4^4 5^2 6^3 8^1 | 2 | 134 P4_2/nnm (1/12,1/12,1/6) b=2 | 2 | 2 | 1 | 1 | 4 | 3 | 2 | 1b | wall-suspect | 93:Pb[same1] 118:Pb[same1] 134:P[unres1] | 33.57 |
| 370 | `567d6e6c92a6ba19` | (20, 32, 14) | 3^4 4^2 5^6 6^1 8^1 | 2 | 138 P4_2/ncm (1/8,3/8,1/8) b=2 | 2 | 2 | 1 | 1 | 4 | 3 | 2 | 1b | wall-suspect | 94:Pb[same1] 116:Pb[same1] 138:A | 33.57 |
| 371 | `3cfb144a2ce5e86d` | (18, 27, 11) | 4^3 5^6 6^2 | 2 | 135 P4_2/mbc (1/8,1/6,5/12) b=3/4 | 1 | 3 | 20 | 19 | 37 | 1 | 1 |  | open-likely | 135:Pb[same1] | 33.32 |
| 372 | `e73fedd244190768` | (12, 18, 8) | 3^2 4^2 5^2 6^2 | 2 | 109 I4_1md (1/8,1/6,5/12) b=1 | 2 | 1 | 33 | 9 | 77 | 3 | 1 |  | open-likely | 109:P[other1] 122:Pb[same1] 141:P[other1] | 33.3 |
| 373 | `b19b176b005235de` | (12, 20, 10) | 3^6 4^1 6^3 | 2 | 141 I4_1/amd (0,1/12,0) b=9/4 | 2 | 2 | 11 | 11 | 154 | 3 | 2 |  | open-likely | 98:Pb[same1] 122:Pb[same1] 141:Pb[unres1] | 33.12 |
| 374 | `61a294835c4c4a23` | (10, 16, 8) | 3^2 4^5 6^1 | 4 | 84 P4_2/m (0,1/4,0) b=1 | 4 | 1 | 4 | 1 | 84 | 20 | 18 |  | indeterminate | 81:Pb[same1] 82:Pb[same1] 84:Pb[same1] 91:Pb[same1] 93:Pb[same1] 94:Pb[same1] 95:Pb[same1] 105:A 111:Pb[same1] 112:Pb[same1] 113:Pb[same1] 114:Pb[same1] 115:Pb[same1] 116:Pb[same1] 118:Pb[same1] 119:Pb[same1] 131:Pb[same1] 132:Pb[same1] 136:Pb[same1] 137:P[unres1] | 32.94 |
| 375 | `342dd2988fa48b2c` | (10, 16, 8) | 3^2 4^5 6^1 | 2 | 108 I4cm (1/8,1/6,5/12) b=1/2 | 2 | 2 | 23 | 21 | 421 | 6 | 5 |  | open-likely | 97:Pb[same1] 108:Pb[same1] 120:Pb[same1] 121:Pb[same1] 125:Pb[unres1] 140:Pb[same1] | 32.21 |
| 376 | `c128d63b9df85e43` | (20, 30, 12) | 3^4 4^3 5^1 7^2 8^1 9^1 | 1 | 135 P4_2/mbc (1/8,1/6,5/12) b=1/2 | 1 | 3 | 6 | 4 | 7 | 1 | 1 |  | open-likely | 135:Pb[same1] | 31.67 |
| 377 | `98c931691e70cf8a` | (18, 27, 11) | 3^2 4^4 5^1 6^2 7^1 8^1 | 1 | 128 P4/mnc (1/8,1/6,5/12) b=1/2 | 1 | 3 | 11 | 8 | 11 | 1 | 1 |  | open-likely | 128:Pb[same1] | 31.1 |
| 378 | `11ee80fc3799d1eb` | (8, 14, 8) | 3^4 4^4 | 8 | 80 I4_1 (0,0,0) b=2 | 8 | 0 | 1 | 1 | 64 | 12 | 7 | 1b | wall-suspect | 76:Pb[same1] 78:Pb[same1] 80:Pb[same1] 88:A 91:Pb[same1] 92:A 95:P[unres1] 96:A 98:Pb[same1] 109:Pb[same1] 122:Pb[same1] 141:A | 30.92 |
| 379 | `7534d49b2a3cdb08` | (14, 22, 10) | 3^5 5^2 6^2 7^1 | 2 | 108 I4cm (1/12,3/8,1/6) b=1/2 | 2 | 2 | 3 | 3 | 11 | 4 | 2 |  | open-likely | 108:Pb[same1] 121:Pb[same1] 125:P[unres1] 140:P[other1] | 30.45 |
| 380 | `5c8e13e6c13789b4` | (20, 30, 12) | 3^3 4^2 5^2 6^3 7^1 8^1 | 1 | 121 I-42m (1/8,1/6,5/12) b=1/2 | 1 | 3 | 3 | 3 | 3 | 1 | 1 |  | open-likely | 121:Pb[same1] | 28.17 |
| 381 | `feaa57edee15810f` | (16, 28, 14) | 3^8 4^2 6^4 | 2 | 98 I4_122 (1/8,1/4,1/8) b=1 | 2 | 1 | 1 | 1 | 4 | 2 | 1 | 1b | wall-suspect | 92:Pb[same1] 98:P[other1] | 28.08 |
| 382 | `f286ea0db04f5993` | (18, 27, 11) | 3^3 4^1 5^3 6^3 8^1 | 2 | 84 P4_2/m (1/12,3/8,1/6) b=7/4 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 84:Pb[same1] | 27.28 |
| 383 | `4097fba12952569e` | (12, 18, 8) | 3^1 4^3 5^3 6^1 | 2 | 87 I4/m (1/8,1/6,5/12) b=1/2 | 1 | 3 | 28 | 15 | 54 | 3 | 1 |  | open-likely | 87:Pb[same1] 134:Pb[unres1] 138:Pb[unres1] | 27.07 |
| 384 | `19942a41247151a2` | (14, 21, 9) | 3^3 4^2 5^1 6^2 8^1 | 2 | 119 I-4m2 (1/8,1/6,5/12) b=3/4 | 1 | 3 | 12 | 9 | 17 | 1 | 1 |  | open-likely | 119:Pb[same1] | 26.82 |
| 385 | `29f83598c9f23455` | (15, 23, 10) | 4^6 5^2 6^2 | 4 | 91 P4_122 (1/8,1/6,5/12) b=3 | 1 | 3 | 4 | 4 | 4 | 2 | 2 |  | open-likely | 91:Pb[same1] 92:Pb[same1] | 25.98 |
| 386 | `ae628f6d86085d69` | (19, 30, 13) | 4^7 5^4 6^2 | 2 | 141 I4_1/amd (0,1/6,1/3) b=1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1b | wall-suspect | 98:Pb[same1] 141:A | 25.78 |
| 387 | `061365c5df56dac1` | (23, 35, 14) | 4^5 5^6 6^2 8^1 | 1 | 91 P4_122 (1/12,3/8,1/6) b=67/32 | 1 | 3 | 2 | 2 | 2 | 1 | 1 | P5-only | indeterminate | 91:Pb[same1] | 25.68 |
| 388 | `c65fa384abfb3249` | (20, 30, 12) | 3^5 5^2 6^2 7^2 9^1 | 1 | 84 P4_2/m (1/8,1/6,5/12) b=69/64 | 1 | 3 | 4 | 3 | 4 | 1 | 1 | P5-only | open-likely | 84:Pb[same1] | 25.48 |
| 389 | `619b6d447540877f` | (14, 22, 10) | 3^2 4^3 5^4 6^1 | 1 | 128 P4/mnc (1/8,1/6,5/12) b=5/4 | 1 | 3 | 19 | 18 | 32 | 1 | 1 |  | open-likely | 128:Pb[same1] | 25.46 |
| 390 | `6d418b925cf725c2` | (14, 24, 12) | 3^4 4^4 5^4 | 2 | 122 I-42d (1/8,1/4,1/8) b=1 | 2 | 1 | 1 | 1 | 4 | 2 | 1 | 1b | wall-suspect | 82:Pb[same1] 122:P[other1] | 24.88 |
| 391 | `607da7953fa0fa4e` | (17, 28, 13) | 3^6 4^2 6^5 | 2 | 128 P4/mnc (1/12,1/6,0) b=1 | 2 | 2 | 1 | 1 | 4 | 4 | 4 | 1b | wall-suspect | 90:Pb[same1] 114:Pb[same1] 118:Pb[same1] 128:Pb[same1] | 24.68 |
| 392 | `a4d2e4badea1fc0f` | (7, 11, 6) | 3^2 4^4 | 4 | 87 I4/m (1/8,1/8,0) b=1 | 4 | 1 | 3 | 1 | 49 | 19 | 9 |  | indeterminate | 82:Pb[same1] 87:P[other1] 90:Pb[same1] 93:Pb[same1] 97:P[other1] 107:A 112:Pb[same1] 114:Pb[same1] 115:Pb[same1] 118:Pb[same1] 119:Pb[same1] 121:P[other1] 126:P[unres1] 128:P[other1] 129:A 131:Pb[same1] 134:P[unres1] 137:P[unres1] 139:P[other1] | 24.58 |
| 393 | `f089902bc80ee80e` | (15, 25, 12) | 3^4 4^5 6^3 | 2 | 119 I-4m2 (0,1/12,1/12) b=1 | 2 | 2 | 1 | 1 | 24 | 3 | 3 | 1b | wall-suspect | 82:Pb[same1] 118:Pb[same1] 119:Pb[same1] | 24.55 |
| 394 | `7780851c54681bc6` | (15, 25, 12) | 3^4 4^5 6^3 | 2 | 137 P4_2/nmc (0,1/8,1/6) b=3/2 | 2 | 2 | 1 | 1 | 4 | 3 | 2 | 1b | wall-suspect | 94:Pb[same1] 114:Pb[same1] 137:P[unres1] | 21.07 |
| 395 | `59efe85d44daca83` | (8, 13, 7) | 3^3 4^3 5^1 | 2 | 131 P4_2/mmc (0,1/12,1/6) b=1 | 2 | 2 | 3 | 1 | 22 | 8 | 7 |  | indeterminate | 84:Pb[same1] 93:Pb[same1] 98:Pb[same1] 112:Pb[same1] 122:Pb[same1] 131:Pb[same1] 132:Pb[same1] 141:P[unres1] | 20.26 |
| 396 | `9e6521c05bcbd3ea` | (9, 14, 7) | 3^1 4^5 5^1 | 2 | 140 I4/mcm (1/8,1/6,5/12) b=1/2 | 1 | 3 | 20 | 18 | 34 | 1 | 1 |  | open-likely | 140:Pb[same1] | 20.24 |
| 397 | `1b0972bcbf773402` | (10, 18, 10) | 3^6 4^2 5^2 | 2 | 141 I4_1/amd (0,1/12,0) b=2 | 2 | 2 | 1 | 1 | 14 | 3 | 2 | 1b | wall-suspect | 98:Pb[same1] 122:Pb[same1] 141:Pb[unres1] | 19.95 |
| 398 | `339e92c4209e1e59` | (14, 21, 9) | 3^3 5^3 6^3 | 2 | 128 P4/mnc (1/12,3/8,1/6) b=1/2 | 1 | 3 | 4 | 4 | 4 | 1 | 1 |  | open-likely | 128:Pb[same1] | 17.88 |
| 399 | `49f36a9ed073276e` | (13, 22, 11) | 3^2 4^8 6^1 | 2 | 87 I4/m (1/12,1/6,0) b=1 | 2 | 2 | 1 | 1 | 4 | 2 | 2 | 1b | wall-suspect | 82:Pb[same1] 87:Pb[same1] | 17.28 |
| 400 | `7b1d7f753e6c14bc` | (11, 19, 10) | 3^4 4^5 6^1 | 2 | 137 P4_2/nmc (0,1/3,1/12) b=1 | 2 | 2 | 1 | 1 | 12 | 3 | 2 | 1b | wall-suspect | 94:Pb[same1] 114:Pb[same1] 137:P[unres1] | 16.74 |
| 401 | `cf917b63c9edf773` | (9, 16, 9) | 3^5 4^3 5^1 | 2 | 140 I4/mcm (1/8,3/8,1/6) b=1 | 2 | 2 | 1 | 1 | 4 | 5 | 5 | 1b | wall-suspect | 87:Pb[same1] 97:Pb[same1] 120:Pb[same1] 124:Pb[same1] 140:Pb[same1] | 15.2 |
| 402 | `bff9a9e578e112a7` | (12, 19, 9) | 3^3 4^1 5^5 | 2 | 136 P4_2/mnm (1/12,1/6,0) b=1 | 2 | 2 | 1 | 1 | 4 | 4 | 4 | 1b | wall-suspect | 94:Pb[same1] 113:Pb[same1] 118:Pb[same1] 136:Pb[same1] | 15.18 |
| 403 | `fca9c7004291eab4` | (15, 25, 12) | 3^4 4^6 6^1 8^1 | 1 | 91 P4_122 (1/8,1/6,5/12) b=2 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1b | wall-suspect | 91:Pb[same1] | 13.0 |
| 404 | `da212d4bfb576e6e` | (11, 17, 8) | 3^4 5^2 6^2 | 1 | 140 I4/mcm (1/12,3/8,1/6) b=1/2 | 1 | 3 | 6 | 6 | 6 | 1 | 1 |  | open-likely | 140:Pb[same1] | 12.48 |

## f-vectors ABSENT from every sighted group's printed Schmitt table (4 of 404)

Sorted by rank. His grid sampled these groups without printing this f-vector (evidence, not proof); S-cell cannot occur here (an S-cell type reproduces a printed row, hence is P in that group).

- #302 `9acb8f9a91b47b51` f=(14, 24, 12) p=4^12 aut=2 — sighted in 141 I4_1/amd — #b 1, wall-suspect, METRIC-THIN
- #324 `b39783cb7395f454` f=(11, 19, 10) p=3^6 4^3 8^1 aut=2 — sighted in 141 I4_1/amd — #b 1, wall-suspect, METRIC-THIN
- #349 `9b1c0d54955637e5` f=(8, 14, 8) p=3^5 4^2 5^1 aut=2 — sighted in 140 I4/mcm — #b 1, wall-suspect, METRIC-THIN
- #368 `f398b0e4ecd40949` f=(12, 19, 9) p=3^3 4^3 5^1 6^2 aut=1 — sighted in 109 I4_1md — #b 1, wall-suspect, METRIC-THIN

## Metric-thin list (126 of 404)

1b = exactly one b-ratio value; P5-only = seen only at bisection midpoints; P3-only = seen only at Schmitt's non-grid b-ratios. Interesting but fragile: a single metric value can be a transition wall.

| rank | id | f-vector | aut | witness | b-ratio(s) | reasons | O/W | Schmitt |
|---|---|---|---|---|---|---|---|---|
| 4 | `49cedbdd58376fac` | (44, 66, 24) | 2 | 92 P4_12_12 (5/24,5/24,0) | 19/16 | 1b,P5-only | wall-suspect | present |
| 14 | `5dc2479b9bc14edc` | (42, 63, 23) | 1 | 98 I4_122 (1/12,3/8,1/6) | 17/32, 9/16, 19/32 | P5-only | open-likely | present |
| 17 | `213c7a114d5a97a8` | (42, 63, 23) | 1 | 98 I4_122 (1/12,3/8,1/6) | 11/16, 45/64 | P5-only | indeterminate | present |
| 18 | `2e8e49eb28497267` | (40, 60, 22) | 1 | 95 P4_322 (1/12,3/8,1/6) | 83/64, 209/160, 53/40, 427/320 | P5-only | open-likely | present |
| 20 | `61fc4ef8c8ac459a` | (40, 60, 22) | 1 | 76 P4_1 (1/8,1/6,5/12) | 37/32, 19/16 | P5-only | indeterminate | present |
| 28 | `35f1b5368eef3104` | (40, 60, 22) | 1 | 98 I4_122 (1/12,3/8,1/6) | 77/80, 39/40 | P5-only | indeterminate | present |
| 29 | `eb2a39308c77a5f2` | (40, 60, 22) | 1 | 98 I4_122 (1/12,3/8,1/6) | 67/64, 17/16 | P5-only | indeterminate | present |
| 30 | `f91f4b104fcf5351` | (38, 57, 21) | 1 | 98 I4_122 (1/12,3/8,1/6) | 39/64, 5/8, 21/32, 43/64 | P5-only | open-likely | present |
| 34 | `7431ec8f1f876c60` | (36, 54, 20) | 1 | 80 I4_1 (1/8,1/6,5/12) | 13/16, 33/40, 17/20, 7/8, ... (+3) | P5-only | open-likely | present |
| 40 | `408752c46c2d7c90` | (36, 54, 20) | 1 | 76 P4_1 (1/12,3/8,1/6) | 73/64, 37/32, 19/16 | P5-only | open-likely | present |
| 43 | `14ee43e7e7821ec9` | (38, 57, 21) | 1 | 98 I4_122 (1/12,3/8,1/6) | 67/80, 17/20, 9/10, 19/20 | P5-only | open-likely | present |
| 44 | `804dd9fb0c1a57ca` | (38, 57, 21) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 43/64, 11/16 | P5-only | indeterminate | present |
| 45 | `b755f1dd6635f8a8` | (38, 57, 21) | 1 | 98 I4_122 (1/12,3/8,1/6) | 69/64, 35/32 | P5-only | indeterminate | present |
| 47 | `0a848b954870c137` | (36, 54, 20) | 1 | 80 I4_1 (1/8,1/6,5/12) | 11/16, 23/32, 33/40, 17/20 | P5-only | indeterminate | present |
| 49 | `1045f2420adbbe89` | (38, 57, 21) | 1 | 80 I4_1 (1/12,3/8,1/6) | 38/25 | 1b,P3-only | wall-suspect | present |
| 50 | `3ad771f657b3824c` | (38, 57, 21) | 1 | 122 I-42d (1/8,1/6,5/12) | 1/2 | 1b | wall-suspect | present |
| 51 | `d43d8d2dd9836ed4` | (38, 57, 21) | 1 | 118 P-4n2 (1/8,1/6,5/12) | 59/32 | 1b,P5-only | wall-suspect | present |
| 52 | `eca7be02cb8e2296` | (38, 57, 21) | 1 | 98 I4_122 (1/12,3/8,1/6) | 9/4 | 1b | wall-suspect | present |
| 57 | `b2284df87d426947` | (36, 54, 20) | 1 | 76 P4_1 (1/8,1/6,5/12) | 65/64 | 1b,P5-only | wall-suspect | present |
| 58 | `9ff7306e4a6cbf44` | (34, 51, 19) | 2 | 141 I4_1/amd (0,1/12,1/12) | 33/64, 17/32, 9/16, 39/64, ... (+3) | P5-only | open-likely | present |
| 60 | `835d94261e1b65c1` | (38, 57, 21) | 1 | 98 I4_122 (1/8,1/6,5/12) | 25/8 | 1b,P5-only | wall-suspect | present |
| 62 | `d9b73e02d62b6d79` | (36, 54, 20) | 1 | 98 I4_122 (1/12,3/8,1/6) | 2 | 1b | wall-suspect | present |
| 67 | `ed4e2709d136f0fc` | (32, 48, 18) | 2 | 122 I-42d (1/24,1/4,1/8) | 53/64, 27/32 | P5-only | indeterminate | present |
| 78 | `2ef5e3844229f89f` | (34, 51, 19) | 1 | 94 P4_22_12 (1/8,1/6,5/12) | 113/80, 57/40, 29/20, 59/40, ... (+5) | P5-only | open-likely | present |
| 82 | `db0320ad071ab1eb` | (34, 51, 19) | 1 | 92 P4_12_12 (1/12,3/8,1/6) | 5/8, 11/16, 45/64, 15/16, ... (+2) | P5-only | open-likely | present |
| 83 | `a04f0c895fcd35ec` | (32, 48, 18) | 4 | 76 P4_1 (1/8,1/6,5/12) | 33/32, 17/16, 9/8 | P5-only | open-likely | present |
| 89 | `3fc289d8d4944791` | (34, 51, 19) | 1 | 116 P-4c2 (1/8,1/6,5/12) | 2501/1600, 631/400, 257/160, 2593/1600, ... (+3) | P5-only | open-likely | present |
| 90 | `b8e16e8d04fc1057` | (34, 51, 19) | 1 | 93 P4_222 (1/8,1/6,5/12) | 1239/800, 631/400, 2547/1600, 129/64, ... (+3) | P5-only | open-likely | present |
| 100 | `6f6ee36de8dbda72` | (34, 51, 19) | 1 | 118 P-4n2 (1/8,1/6,5/12) | 47/32, 59/40, 237/160, 119/64, ... (+1) | P5-only | open-likely | present |
| 105 | `c5eec049a827aebd` | (44, 66, 24) | 1 | 76 P4_1 (1/8,1/6,5/12) | 77/64, 39/32 | P5-only | indeterminate | present |
| 106 | `d25aa9f2dff2be4e` | (34, 51, 19) | 1 | 142 I4_1/acd (1/8,1/6,5/12) | 123/64, 31/16, 63/32, 127/64 | P5-only | open-likely | present |
| 121 | `4e702e95c290afbd` | (34, 51, 19) | 1 | 88 I4_1/a (1/12,3/8,1/6) | 67/80, 17/20, 7/8 | P5-only | open-likely | present |
| 122 | `8a3d9b4f9a849029` | (34, 51, 19) | 1 | 142 I4_1/acd (1/12,3/8,1/6) | 37/16, 19/8, 39/16 | P5-only | open-likely | present |
| 126 | `e1f32acb6ba6b519` | (32, 48, 18) | 1 | 82 I-4 (1/8,1/6,5/12) | 35/64, 9/16, 5/8, 11/16 | P5-only | open-likely | present |
| 128 | `b504635d2b404e93` | (32, 48, 18) | 1 | 86 P4_2/n (1/8,1/6,5/12) | 37/64, 19/32, 5/8, 11/16, ... (+1) | P5-only | open-likely | present |
| 129 | `a19179f2621b5623` | (32, 48, 18) | 1 | 76 P4_1 (1/12,3/8,1/6) | 33/32, 17/16, 9/8 | P5-only | open-likely | present |
| 138 | `35398c494f7e95b0` | (34, 51, 19) | 1 | 96 P4_32_12 (1/12,3/8,1/6) | 9/16, 5/8 | P5-only | indeterminate | present |
| 139 | `3dd10b67f0ea1611` | (34, 51, 19) | 1 | 80 I4_1 (1/8,1/6,5/12) | 71/80, 9/10 | P5-only | indeterminate | present |
| 140 | `900973c9cdd62294` | (34, 51, 19) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 5/8, 21/32 | P5-only | indeterminate | present |
| 141 | `799b17ae5c44c23a` | (32, 48, 18) | 1 | 86 P4_2/n (1/12,3/8,1/6) | 147/64, 37/16, 75/32, 151/64 | P5-only | open-likely | present |
| 144 | `8dce1cb5e78590f9` | (30, 45, 17) | 1 | 96 P4_32_12 (1/12,3/8,1/6) | 491/320, 1239/800, 631/400, 327/200, ... (+3) | P5-only | open-likely | present |
| 150 | `675cc4f2c640cd11` | (32, 48, 18) | 1 | 86 P4_2/n (1/8,1/6,5/12) | 9/8, 19/16, 39/32 | P5-only | open-likely | present |
| 151 | `841ca21dc8f5c770` | (32, 48, 18) | 1 | 142 I4_1/acd (1/8,1/6,5/12) | 1331/800, 677/400, 1377/800 | P5-only | open-likely | present |
| 152 | `d25e09a426bd8ecf` | (32, 48, 18) | 1 | 86 P4_2/n (1/12,3/8,1/6) | 35/64, 9/16, 19/32 | P5-only | open-likely | present |
| 153 | `e23ad48c69ddca62` | (32, 48, 18) | 1 | 88 I4_1/a (1/12,3/8,1/6) | 69/64, 35/32, 9/8 | P5-only | open-likely | present |
| 162 | `1a1c3bd1605b8d49` | (34, 51, 19) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 45/64 | 1b,P5-only | wall-suspect | present |
| 163 | `380af25f9f89e9cb` | (34, 51, 19) | 1 | 122 I-42d (1/8,1/6,5/12) | 231/160 | 1b,P5-only | wall-suspect | present |
| 164 | `92bf045ba0459aac` | (34, 51, 19) | 1 | 110 I4_1cd (1/8,1/6,5/12) | 11/16 | 1b,P5-only | wall-suspect | present |
| 165 | `a61431a36c84685b` | (34, 51, 19) | 1 | 122 I-42d (1/12,3/8,1/6) | 9/4 | 1b | wall-suspect | present |
| 166 | `aa01fff49d9706e8` | (34, 51, 19) | 1 | 122 I-42d (1/12,3/8,1/6) | 29/16 | 1b,P5-only | wall-suspect | present |
| 167 | `50296e97987286bc` | (33, 50, 19) | 1 | 80 I4_1 (1/12,3/8,1/6) | 13/16 | 1b,P5-only | wall-suspect | present |
| 171 | `5f2e35e62d0aa64d` | (32, 48, 18) | 1 | 80 I4_1 (1/12,3/8,1/6) | 39/40, 79/80 | P5-only | indeterminate | present |
| 172 | `9f05491e6b5385fa` | (32, 48, 18) | 1 | 96 P4_32_12 (1/8,1/6,5/12) | 75/64, 19/16 | P5-only | indeterminate | present |
| 173 | `32451695e287120d` | (30, 45, 17) | 1 | 86 P4_2/n (1/12,3/8,1/6) | 67/32, 17/8, 69/32, 139/64 | P5-only | open-likely | present |
| 177 | `36148833db116d9b` | (32, 48, 18) | 1 | 92 P4_12_12 (1/8,1/6,5/12) | 57/40 | 1b,P5-only | wall-suspect | present |
| 178 | `ee87e3504746e36b` | (30, 45, 17) | 1 | 92 P4_12_12 (1/8,1/6,5/12) | 19/32, 5/8, 41/64, 21/32, ... (+1) | P5-only | open-likely | present |
| 180 | `46f335670d41c77e` | (30, 45, 17) | 1 | 80 I4_1 (1/8,1/6,5/12) | 69/64, 35/32, 9/8, 37/32, ... (+2) | P5-only | open-likely | present |
| 181 | `29f80b9c127f79a9` | (28, 42, 16) | 1 | 92 P4_12_12 (1/12,3/8,1/6) | 67/64, 17/16, 69/64, 35/32, ... (+1) | P5-only | open-likely | present |
| 186 | `26a8212cbd6c8b62` | (30, 45, 17) | 1 | 96 P4_32_12 (1/8,1/6,5/12) | 35/32, 9/8, 37/32 | P5-only | open-likely | present |
| 198 | `82552e4e499d0b46` | (34, 51, 19) | 1 | 122 I-42d (1/12,3/8,1/6) | 41/64 | 1b,P5-only | wall-suspect | present |
| 200 | `621f14b6f0a7b371` | (32, 48, 18) | 1 | 96 P4_32_12 (1/8,1/6,5/12) | 2 | 1b | wall-suspect | present |
| 201 | `8fc980b921be3244` | (32, 48, 18) | 1 | 86 P4_2/n (1/8,1/6,5/12) | 121/64 | 1b,P5-only | wall-suspect | present |
| 202 | `9aa9148ffc66fe2e` | (32, 48, 18) | 1 | 80 I4_1 (1/8,1/6,5/12) | 43/64 | 1b,P5-only | wall-suspect | present |
| 203 | `a7860d1366230469` | (32, 48, 18) | 1 | 92 P4_12_12 (1/8,1/6,5/12) | 9/4 | 1b | wall-suspect | present |
| 206 | `1a1a0de250f0da27` | (30, 45, 17) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 19/32, 39/64 | P5-only | indeterminate | present |
| 207 | `a3906799b3b200e1` | (30, 45, 17) | 1 | 122 I-42d (1/12,3/8,1/6) | 21/32, 11/16 | P5-only | indeterminate | present |
| 208 | `f3322045c6a474d6` | (30, 45, 17) | 1 | 110 I4_1cd (1/12,3/8,1/6) | 21/32, 43/64 | P5-only | indeterminate | present |
| 209 | `0882fd4b5b8cb62e` | (28, 42, 16) | 1 | 86 P4_2/n (1/12,3/8,1/6) | 39/64, 5/8, 11/16, 45/64 | P5-only | open-likely | present |
| 210 | `4051049d6635c527` | (28, 42, 16) | 1 | 110 I4_1cd (1/12,3/8,1/6) | 227/160, 57/40, 29/20, 59/40 | P5-only | open-likely | present |
| 225 | `3e1c2f08dd535cc5` | (38, 57, 21) | 1 | 94 P4_22_12 (1/12,3/8,1/6) | 147/64, 37/16 | P5-only | indeterminate | present |
| 230 | `b77e98e2c4a01aad` | (30, 45, 17) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 37/64 | 1b,P5-only | wall-suspect | present |
| 231 | `1f2332434c9e64b8` | (30, 45, 17) | 1 | 142 I4_1/acd (1/8,1/6,5/12) | 33/40, 17/20, 7/8, 71/80 | P5-only | open-likely | present |
| 232 | `0d55f30856d2734f` | (21, 32, 13) | 2 | 141 I4_1/amd (0,1/4,1/12) | 2501/1600, 631/400, 327/200, 677/400, ... (+1) | P5-only | open-likely | present |
| 236 | `896e9cc347268b4d` | (38, 57, 21) | 1 | 118 P-4n2 (1/12,3/8,1/6) | 23/16, 29/20, 117/80 | P5-only | open-likely | present |
| 246 | `adc735c0ace21b40` | (20, 33, 15) | 2 | 98 I4_122 (1/6,1/6,0) | 1 | 1b | wall-suspect | present |
| 247 | `ef0bcf47327dee5c` | (38, 57, 21) | 1 | 116 P-4c2 (1/8,1/6,5/12) | 1239/800 | 1b,P5-only | wall-suspect | present |
| 248 | `5fdbcfbd23c2a589` | (36, 54, 20) | 1 | 116 P-4c2 (1/12,3/8,1/6) | 145/64, 73/32 | P5-only | indeterminate | present |
| 249 | `89e47e7dcaab4687` | (36, 54, 20) | 1 | 93 P4_222 (1/12,3/8,1/6) | 59/32, 119/64 | P5-only | indeterminate | present |
| 254 | `5561cb5efa0a7c0c` | (28, 42, 16) | 1 | 96 P4_32_12 (1/12,3/8,1/6) | 23/8 | 1b,P5-only | wall-suspect | present |
| 258 | `80b68f2e4481cfeb` | (25, 39, 16) | 1 | 80 I4_1 (1/12,3/8,1/6) | 1 | 1b | wall-suspect | present |
| 265 | `b9d2f3e02e91b42b` | (30, 47, 19) | 2 | 141 I4_1/amd (0,1/6,1/12) | 37/32, 19/16, 77/64 | P5-only | open-likely | present |
| 272 | `1b269a7a84560401` | (26, 39, 15) | 1 | 88 I4_1/a (1/12,3/8,1/6) | 5/8, 21/32 | P5-only | indeterminate | present |
| 274 | `f2338eb96662d54f` | (18, 28, 12) | 4 | 141 I4_1/amd (0,1/8,1/12) | 3/2 | 1b | wall-suspect | present |
| 284 | `1fcd5245be090d59` | (23, 36, 15) | 1 | 142 I4_1/acd (1/8,1/6,5/12) | 2 | 1b | wall-suspect | present |
| 292 | `74b20b492f403316` | (26, 39, 15) | 2 | 88 I4_1/a (1/12,3/8,1/6) | 9/4 | 1b | wall-suspect | present |
| 293 | `eda7881fe2bb6928` | (25, 39, 16) | 2 | 109 I4_1md (0,1/6,0) | 83/64, 209/160, 53/40 | P5-only | open-likely | present |
| 302 | `9acb8f9a91b47b51` | (14, 24, 12) | 2 | 141 I4_1/amd (0,1/8,3/8) | 1 | 1b | wall-suspect | ABSENT-all |
| 303 | `1d2c47d061a6ab6c` | (18, 28, 12) | 2 | 142 I4_1/acd (1/8,1/4,3/8) | 1 | 1b | wall-suspect | present |
| 304 | `eaf8f8e7b00c0da0` | (26, 39, 15) | 1 | 88 I4_1/a (1/8,1/6,5/12) | 5/2 | 1b | wall-suspect | present |
| 306 | `e0cb47c4a5901ef9` | (22, 36, 16) | 8 | 91 P4_122 (1/8,1/8,3/8) | 1 | 1b | wall-suspect | present |
| 308 | `3c3aac0251a9d3dd` | (32, 48, 18) | 1 | 116 P-4c2 (1/12,3/8,1/6) | 129/64, 65/32, 33/16, 17/8, ... (+3) | P5-only | open-likely | present |
| 317 | `818521767ac611bd` | (15, 25, 12) | 2 | 141 I4_1/amd (0,1/4,0) | 1 | 1b | wall-suspect | present |
| 324 | `b39783cb7395f454` | (11, 19, 10) | 2 | 141 I4_1/amd (0,1/6,1/6) | 2 | 1b | wall-suspect | ABSENT-all |
| 336 | `0e291742552bfd85` | (18, 27, 11) | 1 | 134 P4_2/nnm (1/8,1/6,5/12) | 9/8, 19/16, 39/32 | P5-only | open-likely | present |
| 340 | `b25a63276e96e094` | (19, 30, 13) | 4 | 84 P4_2/m (1/8,3/8,0) | 1 | 1b | wall-suspect | present |
| 342 | `34020552fab1d2e4` | (26, 41, 17) | 1 | 130 P4/ncc (1/8,1/6,5/12) | 7/8, 9/10, 19/20, 77/80 | P5-only | open-likely | present |
| 346 | `822163f15ffc16d1` | (30, 45, 17) | 1 | 92 P4_12_12 (1/8,1/6,5/12) | 75/64, 19/16, 39/32 | P5-only | open-likely | present |
| 348 | `6f79177bf480b895` | (34, 51, 19) | 1 | 95 P4_322 (1/12,3/8,1/6) | 33/40 | 1b,P5-only | wall-suspect | present |
| 349 | `9b1c0d54955637e5` | (8, 14, 8) | 2 | 140 I4/mcm (1/12,1/3,0) | 1/2 | 1b | wall-suspect | ABSENT-all |
| 350 | `519d875aa973e258` | (10, 16, 8) | 4 | 141 I4_1/amd (1/8,1/8,0) | 1 | 1b | wall-suspect | present |
| 354 | `f1d0ab0fb88d1c9d` | (32, 48, 18) | 1 | 122 I-42d (1/12,3/8,1/6) | 2501/1600 | 1b,P5-only | wall-suspect | present |
| 355 | `0bc1139de57a9670` | (29, 45, 18) | 1 | 116 P-4c2 (1/12,3/8,1/6) | 9/4 | 1b | wall-suspect | present |
| 357 | `38d3ab5e6be25619` | (28, 42, 16) | 2 | 82 I-4 (1/8,1/6,5/12) | 117/64, 59/32, 15/8, 61/32, ... (+2) | P5-only | open-likely | present |
| 359 | `68f4290f946a6883` | (28, 42, 16) | 1 | 112 P-42c (1/8,1/6,5/12) | 115/64, 29/16, 59/32, 119/64, ... (+2) | P5-only | open-likely | present |
| 360 | `6eec925b71cecc49` | (21, 33, 14) | 2 | 138 P4_2/ncm (1/12,5/12,1/12) | 1 | 1b | wall-suspect | present |
| 361 | `54886fac17fe023a` | (28, 43, 17) | 1 | 91 P4_122 (1/8,1/6,5/12) | 15/8 | 1b,P5-only | wall-suspect | present |
| 364 | `c7258adeebded3ae` | (23, 36, 15) | 2 | 84 P4_2/m (1/12,1/3,0) | 1 | 1b | wall-suspect | present |
| 367 | `7d5559ec4f268c7c` | (16, 27, 13) | 4 | 88 I4_1/a (0,0,1/8) | 2 | 1b | wall-suspect | present |
| 368 | `f398b0e4ecd40949` | (12, 19, 9) | 1 | 109 I4_1md (1/12,3/8,1/6) | 1 | 1b | wall-suspect | ABSENT-all |
| 369 | `37e188e9b012345e` | (20, 32, 14) | 2 | 134 P4_2/nnm (1/12,1/12,1/6) | 2 | 1b | wall-suspect | present |
| 370 | `567d6e6c92a6ba19` | (20, 32, 14) | 2 | 138 P4_2/ncm (1/8,3/8,1/8) | 2 | 1b | wall-suspect | present |
| 378 | `11ee80fc3799d1eb` | (8, 14, 8) | 8 | 80 I4_1 (0,0,0) | 2 | 1b | wall-suspect | present |
| 381 | `feaa57edee15810f` | (16, 28, 14) | 2 | 98 I4_122 (1/8,1/4,1/8) | 1 | 1b | wall-suspect | present |
| 386 | `ae628f6d86085d69` | (19, 30, 13) | 2 | 141 I4_1/amd (0,1/6,1/3) | 1 | 1b | wall-suspect | present |
| 387 | `061365c5df56dac1` | (23, 35, 14) | 1 | 91 P4_122 (1/12,3/8,1/6) | 67/32, 135/64 | P5-only | indeterminate | present |
| 388 | `c65fa384abfb3249` | (20, 30, 12) | 1 | 84 P4_2/m (1/8,1/6,5/12) | 69/64, 15/8, 31/16, 63/32 | P5-only | open-likely | present |
| 390 | `6d418b925cf725c2` | (14, 24, 12) | 2 | 122 I-42d (1/8,1/4,1/8) | 1 | 1b | wall-suspect | present |
| 391 | `607da7953fa0fa4e` | (17, 28, 13) | 2 | 128 P4/mnc (1/12,1/6,0) | 1 | 1b | wall-suspect | present |
| 393 | `f089902bc80ee80e` | (15, 25, 12) | 2 | 119 I-4m2 (0,1/12,1/12) | 1 | 1b | wall-suspect | present |
| 394 | `7780851c54681bc6` | (15, 25, 12) | 2 | 137 P4_2/nmc (0,1/8,1/6) | 3/2 | 1b | wall-suspect | present |
| 397 | `1b0972bcbf773402` | (10, 18, 10) | 2 | 141 I4_1/amd (0,1/12,0) | 2 | 1b | wall-suspect | present |
| 399 | `49f36a9ed073276e` | (13, 22, 11) | 2 | 87 I4/m (1/12,1/6,0) | 1 | 1b | wall-suspect | present |
| 400 | `7b1d7f753e6c14bc` | (11, 19, 10) | 2 | 137 P4_2/nmc (0,1/3,1/12) | 1 | 1b | wall-suspect | present |
| 401 | `cf917b63c9edf773` | (9, 16, 9) | 2 | 140 I4/mcm (1/8,3/8,1/6) | 1 | 1b | wall-suspect | present |
| 402 | `bff9a9e578e112a7` | (12, 19, 9) | 2 | 136 P4_2/mnm (1/12,1/6,0) | 1 | 1b | wall-suspect | present |
| 403 | `fca9c7004291eab4` | (15, 25, 12) | 1 | 91 P4_122 (1/8,1/6,5/12) | 2 | 1b | wall-suspect | present |

## S-cell types (menu-sighted AND reproduce one of Schmitt's printed cells: 176)

Type-level matches with his printed representatives; excluded from the shortlist. Listed compactly.

| rank | id | f-vector | aut | P2 cells | groups |
|---|---|---|---|---|---|
| 2 | `698bcaf0b95bcece` | (48, 72, 26) | 2 | 2 | 80 92 98 |
| 3 | `60c6a7023f6e4280` | (36, 54, 20) | 8 | 1 | 76 78 80 88 91 92 95 96 98 109 122 141 |
| 9 | `ab93cbeb7be9da28` | (44, 66, 24) | 2 | 2 | 80 92 98 |
| 42 | `c1a62b4c22e7c6e8` | (40, 60, 22) | 2 | 2 | 76 78 92 96 |
| 48 | `e5760549017956be` | (32, 48, 18) | 8 | 3 | 76 78 80 88 91 92 95 96 98 109 122 141 |
| 53 | `0087d56fd2a8a610` | (36, 54, 20) | 2 | 2 | 76 78 92 96 |
| 54 | `06c5da3bdc942c6f` | (36, 54, 20) | 2 | 1 | 80 92 98 |
| 56 | `a3a8447783e42486` | (24, 38, 16) | 8 | 4 | 76 78 80 88 91 92 95 96 98 109 122 141 |
| 61 | `fe3a62d422ed4d82` | (40, 61, 23) | 2 | 1 | 141 |
| 63 | `6983d731cb2a7d98` | (36, 55, 21) | 2 | 3 | 98 122 141 |
| 80 | `e4200db43401702b` | (28, 42, 16) | 8 | 4 | 80 88 98 109 118 119 122 141 |
| 88 | `fa88164038f13cf0` | (33, 51, 20) | 2 | 1 | 141 |
| 95 | `9ae45735b2d716dd` | (44, 66, 24) | 1 | 1 | 98 |
| 105 | `c5eec049a827aebd` | (44, 66, 24) | 1 | 2 | 76 78 |
| 124 | `823d10214adbceef` | (34, 51, 19) | 2 | 1 | 80 98 |
| 135 | `1451aa79a85162c1` | (34, 51, 19) | 2 | 1 | 110 142 |
| 146 | `35953737803092f0` | (16, 24, 10) | 8 | 32 | 77 81 82 84 86 87 91 92 93 94 95 96 97 98 101 102 105 111 112 113 114 115 116 118 119 121 126 128 131 132 134 135 136 137 138 139 142 |
| 155 | `5af057df372beee8` | (36, 54, 20) | 1 | 1 | 122 |
| 156 | `3c8373805b3b0aab` | (24, 36, 14) | 8 | 1 | 77 81 82 84 122 |
| 158 | `7391016f434c6483` | (38, 57, 21) | 1 | 1 | 91 95 |
| 170 | `205e338c517ee1e4` | (34, 51, 19) | 2 | 1 | 93 134 |
| 183 | `1722d568b932f832` | (27, 41, 16) | 2 | 2 | 93 134 142 |
| 184 | `1177844bd4d28549` | (38, 57, 21) | 1 | 1 | 93 |
| 187 | `c6005fa4af1a744c` | (21, 32, 13) | 4 | 12 | 77 81 84 92 94 96 102 110 113 114 118 136 |
| 188 | `b8b72db4ab55a296` | (24, 37, 15) | 2 | 4 | 93 94 116 118 134 138 |
| 190 | `779fb53b92dfc3fe` | (22, 34, 14) | 4 | 5 | 80 82 88 98 109 118 119 122 141 |
| 199 | `fdecd8c917108d43` | (36, 54, 20) | 1 | 1 | 92 |
| 204 | `8534b49823b5b2ed` | (31, 47, 18) | 2 | 1 | 122 141 |
| 205 | `c10281b956e50c34` | (26, 39, 15) | 4 | 1 | 88 91 92 95 96 98 122 141 |
| 213 | `c8c6299f9321c3cb` | (28, 42, 16) | 2 | 1 | 91 95 96 |
| 215 | `dbbd406100689384` | (26, 41, 17) | 2 | 5 | 80 91 92 96 98 |
| 217 | `c7bba76d2396a322` | (28, 42, 16) | 2 | 2 | 76 78 92 96 |
| 218 | `0498a4ecb657609d` | (26, 40, 16) | 2 | 3 | 80 91 98 |
| 219 | `10424bd99b31c5f2` | (20, 30, 12) | 40 | 2 | 98 122 141 |
| 223 | `82a5a88ccba80d26` | (13, 20, 9) | 8 | 23 | 82 84 86 87 91 92 93 94 95 96 97 112 114 116 118 119 121 126 128 131 132 134 135 136 137 138 139 142 |
| 224 | `4a1fffe528971ffb` | (23, 35, 14) | 2 | 4 | 94 98 116 122 138 141 |
| 225 | `3e1c2f08dd535cc5` | (38, 57, 21) | 1 | 1 | 94 |
| 227 | `dcc0a70baf02d3d7` | (14, 21, 9) | 12 | 13 | 79 82 87 90 97 102 104 107 113 114 119 121 126 128 129 134 136 137 138 139 141 |
| 228 | `6fe445ec5becddde` | (20, 31, 13) | 4 | 3 | 88 91 95 98 122 141 |
| 233 | `8d5cf695b24cb063` | (28, 42, 16) | 2 | 3 | 94 106 117 135 |
| 234 | `52392121966e66eb` | (10, 15, 7) | 20 | 25 | 75 81 83 84 87 88 90 91 93 94 98 100 104 106 112 113 114 117 118 122 127 128 131 132 135 136 141 |
| 235 | `1457e9a93eea5438` | (26, 39, 15) | 2 | 2 | 94 116 138 |
| 236 | `896e9cc347268b4d` | (38, 57, 21) | 1 | 1 | 118 |
| 237 | `637fec5274f3a3e2` | (30, 45, 17) | 2 | 1 | 112 121 |
| 238 | `b062a24492a59606` | (23, 35, 14) | 2 | 3 | 82 118 119 |
| 241 | `e948828e76447bbb` | (24, 36, 14) | 4 | 1 | 88 110 120 142 |
| 242 | `822fbf394c878292` | (34, 51, 19) | 1 | 2 | 116 118 |
| 243 | `96671ea7ca1f2450` | (28, 42, 16) | 2 | 3 | 77 81 84 |
| 244 | `9b7039e0c295ff94` | (12, 18, 8) | 24 | 11 | 79 84 87 90 93 97 104 105 107 115 119 121 126 128 129 131 132 134 136 137 139 |
| 245 | `7824c3404ec7c532` | (14, 23, 11) | 4 | 19 | 79 82 85 87 89 94 97 103 106 108 112 114 116 117 120 121 124 125 126 130 133 135 138 140 |
| 247 | `ef0bcf47327dee5c` | (38, 57, 21) | 1 | 1 | 116 |
| 248 | `5fdbcfbd23c2a589` | (36, 54, 20) | 1 | 1 | 116 |
| 249 | `89e47e7dcaab4687` | (36, 54, 20) | 1 | 1 | 93 |
| 251 | `75fb0b80b43ec683` | (34, 51, 19) | 1 | 2 | 93 94 |
| 255 | `ae7f4681011715ee` | (25, 38, 15) | 2 | 2 | 80 109 |
| 256 | `2626c0b5370635a6` | (18, 29, 13) | 4 | 19 | 79 82 85 87 89 94 97 103 106 108 112 116 117 120 121 124 125 126 130 133 135 138 140 |
| 257 | `9cab1436007f3c03` | (22, 34, 14) | 4 | 2 | 88 91 95 98 122 141 |
| 259 | `2af1083dea2057de` | (26, 40, 16) | 2 | 1 | 109 |
| 262 | `fc7f08307d0c3900` | (34, 51, 19) | 1 | 1 | 120 |
| 263 | `27d2f55670d4f85c` | (27, 41, 16) | 2 | 1 | 118 134 |
| 264 | `6a8a2df1eaf9f29d` | (24, 36, 14) | 2 | 2 | 94 106 117 135 |
| 265 | `b9d2f3e02e91b42b` | (30, 47, 19) | 2 | 2 | 122 141 |
| 267 | `3e83ba1555125b93` | (25, 38, 15) | 2 | 3 | 77 81 84 |
| 268 | `7b0441c8ac019b55` | (25, 38, 15) | 2 | 5 | 90 104 114 118 128 |
| 269 | `419d0b18626b622e` | (31, 48, 19) | 1 | 1 | 91 |
| 270 | `d648a739129d46df` | (26, 39, 15) | 2 | 2 | 98 122 141 |
| 271 | `03132752288b78be` | (32, 48, 18) | 1 | 1 | 93 |
| 275 | `abfdf73c2f298784` | (12, 18, 8) | 8 | 8 | 76 78 80 88 91 92 95 96 98 109 122 141 |
| 277 | `6b1f36550e2f6ec6` | (22, 34, 14) | 2 | 2 | 94 114 137 |
| 278 | `da1833391efcd38c` | (30, 45, 17) | 1 | 2 | 116 118 |
| 279 | `adbb83c95151fc35` | (30, 45, 17) | 1 | 2 | 93 94 |
| 283 | `8c0bde1b0fee079d` | (32, 48, 18) | 1 | 1 | 118 |
| 285 | `206c7c14af9927b2` | (18, 29, 13) | 2 | 5 | 90 104 114 118 128 |
| 286 | `8fa1790edfd55a9f` | (17, 26, 11) | 2 | 4 | 93 94 116 118 134 138 |
| 287 | `d059d2ebab300484` | (31, 47, 18) | 1 | 1 | 91 |
| 288 | `b17c6249a65c9ab6` | (30, 45, 17) | 1 | 1 | 120 |
| 289 | `9ca699788f254f08` | (30, 46, 18) | 1 | 1 | 97 |
| 290 | `07db8b31cf7776c5` | (21, 32, 13) | 2 | 1 | 122 141 |
| 291 | `ad192c7f4c277ecf` | (29, 44, 17) | 1 | 1 | 118 |
| 293 | `eda7881fe2bb6928` | (25, 39, 16) | 2 | 2 | 80 109 |
| 295 | `c6ba6d87ea9c38b4` | (29, 44, 17) | 1 | 1 | 80 |
| 296 | `1f2da25d4fd3e5d7` | (21, 32, 13) | 2 | 3 | 79 82 85 87 |
| 297 | `3da00cbdd50d4759` | (32, 48, 18) | 1 | 1 | 110 |
| 298 | `56dcc17ff0060c44` | (32, 48, 18) | 1 | 1 | 114 |
| 299 | `72aba762a764b251` | (32, 48, 18) | 1 | 1 | 94 |
| 300 | `1ec753f439979bfc` | (18, 29, 13) | 2 | 1 | 110 142 |
| 305 | `4e7f52911cb9c8b0` | (28, 42, 16) | 2 | 1 | 98 |
| 306 | `e0cb47c4a5901ef9` | (22, 36, 16) | 8 | 1 | 91 92 95 |
| 307 | `9679c9e830167325` | (28, 42, 16) | 1 | 1 | 116 |
| 308 | `3c3aac0251a9d3dd` | (32, 48, 18) | 1 | 1 | 116 |
| 309 | `3a7c6d5f00cde1ae` | (32, 48, 18) | 1 | 1 | 92 96 133 |
| 310 | `28fa1abcd5fcfcae` | (28, 42, 16) | 1 | 1 | 94 |
| 311 | `3d3095468486d3ff` | (22, 33, 13) | 2 | 2 | 98 122 141 |
| 312 | `b509653535640869` | (19, 29, 12) | 2 | 2 | 80 109 |
| 313 | `6869d9adc5f8c737` | (18, 27, 11) | 12 | 2 | 109 119 141 |
| 316 | `bf5eadab641c997b` | (28, 42, 16) | 1 | 1 | 88 114 |
| 318 | `73c67ccc167782ff` | (24, 38, 16) | 2 | 1 | 98 141 |
| 320 | `f7b981bc1af0046a` | (28, 42, 16) | 1 | 1 | 110 |
| 321 | `fc4719574cb9d459` | (30, 45, 17) | 1 | 1 | 114 |
| 322 | `59ec3e1d88f29e8b` | (30, 45, 17) | 1 | 1 | 122 |
| 323 | `845f058b04ddb75c` | (21, 32, 13) | 2 | 3 | 90 104 128 |
| 325 | `d7e9a753e8e2e449` | (28, 42, 16) | 1 | 1 | 120 |
| 326 | `e956ba4b05a47f01` | (20, 31, 13) | 2 | 1 | 122 141 |
| 327 | `4af32e5d248c23da` | (16, 24, 10) | 4 | 1 | 109 141 |
| 328 | `3eb68e3019868bb0` | (26, 39, 15) | 1 | 1 | 110 114 |
| 329 | `9da8963ab70c9719` | (17, 27, 12) | 2 | 1 | 122 141 |
| 330 | `327ca8d2dd09e1c0` | (26, 39, 15) | 2 | 1 | 92 96 |
| 331 | `62ca11329dfd99e4` | (28, 42, 16) | 1 | 1 | 92 96 |
| 332 | `3fea442a4ead6925` | (25, 38, 15) | 1 | 1 | 91 95 |
| 333 | `6ab2e96429e81ed7` | (26, 40, 16) | 1 | 1 | 97 |
| 334 | `8e1a1fd6069d5392` | (12, 19, 9) | 4 | 6 | 87 97 120 124 135 140 |
| 335 | `f478cd4934ed8ab6` | (14, 21, 9) | 12 | 1 | 109 119 141 |
| 337 | `6016ea01a4fa7b58` | (29, 45, 18) | 1 | 1 | 91 |
| 338 | `be16ed915b8f257e` | (30, 45, 17) | 1 | 1 | 98 |
| 339 | `be5b1b5360c30bf4` | (17, 26, 11) | 2 | 1 | 122 141 |
| 340 | `b25a63276e96e094` | (19, 30, 13) | 4 | 6 | 81 84 94 102 113 118 122 136 |
| 341 | `3f6b28d5f7a72d60` | (14, 21, 9) | 2 | 4 | 84 94 118 136 |
| 342 | `34020552fab1d2e4` | (26, 41, 17) | 1 | 1 | 130 |
| 344 | `97fb7fde62d174ad` | (23, 36, 15) | 2 | 2 | 93 118 134 |
| 345 | `e3b3aae804f2c179` | (10, 15, 7) | 6 | 3 | 97 121 136 139 |
| 346 | `822163f15ffc16d1` | (30, 45, 17) | 1 | 1 | 92 |
| 347 | `2bb95af9090a5ea1` | (24, 37, 15) | 1 | 1 | 97 |
| 348 | `6f79177bf480b895` | (34, 51, 19) | 1 | 1 | 91 95 |
| 351 | `9d6af8d171ee45f1` | (21, 33, 14) | 2 | 1 | 98 141 |
| 352 | `a69e19eb2dcae98b` | (16, 24, 10) | 2 | 1 | 109 122 141 |
| 353 | `0c6ba5cadd15c06e` | (9, 16, 9) | 8 | 12 | 82 84 86 87 91 93 94 95 97 112 114 116 118 119 121 126 128 131 132 134 135 136 137 139 |
| 354 | `f1d0ab0fb88d1c9d` | (32, 48, 18) | 1 | 1 | 122 |
| 355 | `0bc1139de57a9670` | (29, 45, 18) | 1 | 1 | 116 |
| 356 | `fe7ee18a2838e181` | (14, 22, 10) | 2 | 7 | 87 97 120 124 130 135 140 |
| 357 | `38d3ab5e6be25619` | (28, 42, 16) | 2 | 1 | 82 |
| 358 | `bf5f699aaeed9ea9` | (17, 26, 11) | 2 | 3 | 79 82 85 87 |
| 359 | `68f4290f946a6883` | (28, 42, 16) | 1 | 1 | 112 |
| 360 | `6eec925b71cecc49` | (21, 33, 14) | 2 | 2 | 94 116 138 |
| 361 | `54886fac17fe023a` | (28, 43, 17) | 1 | 1 | 91 |
| 362 | `b6892ba92de5db43` | (19, 30, 13) | 2 | 4 | 82 112 114 121 |
| 363 | `2a089105ae08c36d` | (14, 21, 9) | 2 | 2 | 98 122 141 |
| 364 | `c7258adeebded3ae` | (23, 36, 15) | 2 | 2 | 81 84 |
| 365 | `04b26311800821b8` | (20, 32, 14) | 1 | 1 | 97 130 |
| 366 | `c56e8a772aacdc9a` | (16, 26, 12) | 1 | 1 | 97 130 |
| 367 | `7d5559ec4f268c7c` | (16, 27, 13) | 4 | 4 | 88 91 92 96 98 122 141 |
| 369 | `37e188e9b012345e` | (20, 32, 14) | 2 | 2 | 93 118 134 |
| 370 | `567d6e6c92a6ba19` | (20, 32, 14) | 2 | 2 | 94 116 138 |
| 371 | `3cfb144a2ce5e86d` | (18, 27, 11) | 2 | 1 | 135 |
| 372 | `e73fedd244190768` | (12, 18, 8) | 2 | 1 | 109 122 141 |
| 373 | `b19b176b005235de` | (12, 20, 10) | 2 | 2 | 98 122 141 |
| 374 | `61a294835c4c4a23` | (10, 16, 8) | 4 | 18 | 81 82 84 91 93 94 95 105 111 112 113 114 115 116 118 119 131 132 136 137 |
| 375 | `342dd2988fa48b2c` | (10, 16, 8) | 2 | 5 | 97 108 120 121 125 140 |
| 376 | `c128d63b9df85e43` | (20, 30, 12) | 1 | 1 | 135 |
| 377 | `98c931691e70cf8a` | (18, 27, 11) | 1 | 1 | 128 |
| 378 | `11ee80fc3799d1eb` | (8, 14, 8) | 8 | 7 | 76 78 80 88 91 92 95 96 98 109 122 141 |
| 379 | `7534d49b2a3cdb08` | (14, 22, 10) | 2 | 2 | 108 121 125 140 |
| 380 | `5c8e13e6c13789b4` | (20, 30, 12) | 1 | 1 | 121 |
| 381 | `feaa57edee15810f` | (16, 28, 14) | 2 | 1 | 92 98 |
| 382 | `f286ea0db04f5993` | (18, 27, 11) | 2 | 1 | 84 |
| 383 | `4097fba12952569e` | (12, 18, 8) | 2 | 1 | 87 134 138 |
| 384 | `19942a41247151a2` | (14, 21, 9) | 2 | 1 | 119 |
| 385 | `29f83598c9f23455` | (15, 23, 10) | 4 | 2 | 91 92 |
| 386 | `ae628f6d86085d69` | (19, 30, 13) | 2 | 1 | 98 141 |
| 387 | `061365c5df56dac1` | (23, 35, 14) | 1 | 1 | 91 |
| 388 | `c65fa384abfb3249` | (20, 30, 12) | 1 | 1 | 84 |
| 389 | `619b6d447540877f` | (14, 22, 10) | 1 | 1 | 128 |
| 390 | `6d418b925cf725c2` | (14, 24, 12) | 2 | 1 | 82 122 |
| 391 | `607da7953fa0fa4e` | (17, 28, 13) | 2 | 4 | 90 114 118 128 |
| 392 | `a4d2e4badea1fc0f` | (7, 11, 6) | 4 | 9 | 82 87 90 93 97 107 112 114 115 118 119 121 126 128 129 131 134 137 139 |
| 393 | `f089902bc80ee80e` | (15, 25, 12) | 2 | 3 | 82 118 119 |
| 394 | `7780851c54681bc6` | (15, 25, 12) | 2 | 2 | 94 114 137 |
| 395 | `59efe85d44daca83` | (8, 13, 7) | 2 | 7 | 84 93 98 112 122 131 132 141 |
| 396 | `9e6521c05bcbd3ea` | (9, 14, 7) | 2 | 1 | 140 |
| 397 | `1b0972bcbf773402` | (10, 18, 10) | 2 | 2 | 98 122 141 |
| 398 | `339e92c4209e1e59` | (14, 21, 9) | 2 | 1 | 128 |
| 399 | `49f36a9ed073276e` | (13, 22, 11) | 2 | 2 | 82 87 |
| 400 | `7b1d7f753e6c14bc` | (11, 19, 10) | 2 | 2 | 94 114 137 |
| 401 | `cf917b63c9edf773` | (9, 16, 9) | 2 | 5 | 87 97 120 124 140 |
| 402 | `bff9a9e578e112a7` | (12, 19, 9) | 2 | 4 | 94 113 118 136 |
| 403 | `fca9c7004291eab4` | (15, 25, 12) | 1 | 1 | 91 |
| 404 | `da212d4bfb576e6e` | (11, 17, 8) | 1 | 1 | 140 |

## Per-group counts (menu-sighted tetragonal types)

| group | symbol | first menu witness here | sighted here (menu) | sighted here (any pass) | S-cell here | f-vec A here |
|---|---|---|---|---|---|---|
| 75 | P4 | 1 | 1 | 1 | 1 | 0 |
| 76 | P4_1 | 14 | 15 | 20 | 9 | 0 |
| 77 | P4_2 | 2 | 4 | 5 | 5 | 0 |
| 78 | P4_3 | 0 | 15 | 20 | 9 | 0 |
| 79 | I4 | 3 | 3 | 6 | 6 | 0 |
| 80 | I4_1 | 19 | 21 | 30 | 17 | 0 |
| 81 | P-4 | 0 | 4 | 9 | 9 | 0 |
| 82 | I-4 | 7 | 9 | 22 | 18 | 0 |
| 83 | P4/m | 0 | 1 | 1 | 1 | 0 |
| 84 | P4_2/m | 10 | 15 | 18 | 16 | 0 |
| 85 | P4/n | 1 | 4 | 4 | 4 | 0 |
| 86 | P4_2/n | 16 | 19 | 19 | 3 | 0 |
| 87 | I4/m | 8 | 15 | 17 | 16 | 0 |
| 88 | I4_1/a | 26 | 33 | 33 | 14 | 2 |
| 89 | P422 | 0 | 2 | 2 | 2 | 0 |
| 90 | P42_12 | 3 | 4 | 8 | 8 | 0 |
| 91 | P4_122 | 16 | 23 | 34 | 28 | 0 |
| 92 | P4_12_12 | 23 | 33 | 43 | 25 | 1 |
| 93 | P4_222 | 9 | 14 | 22 | 19 | 0 |
| 94 | P4_22_12 | 10 | 17 | 31 | 27 | 0 |
| 95 | P4_322 | 9 | 21 | 26 | 17 | 0 |
| 96 | P4_32_12 | 10 | 32 | 38 | 18 | 1 |
| 97 | I422 | 5 | 13 | 18 | 18 | 0 |
| 98 | I4_122 | 33 | 48 | 60 | 35 | 0 |
| 100 | P4bm | 0 | 1 | 1 | 1 | 0 |
| 101 | P4_2cm | 0 | 1 | 1 | 1 | 0 |
| 102 | P4_2nm | 0 | 4 | 4 | 4 | 1 |
| 103 | P4cc | 0 | 2 | 2 | 2 | 0 |
| 104 | P4nc | 0 | 2 | 6 | 6 | 0 |
| 105 | P4_2mc | 0 | 3 | 3 | 3 | 1 |
| 106 | P4_2bc | 0 | 2 | 5 | 5 | 0 |
| 107 | I4mm | 0 | 3 | 3 | 3 | 1 |
| 108 | I4cm | 2 | 4 | 4 | 4 | 0 |
| 109 | I4_1md | 7 | 17 | 17 | 16 | 1 |
| 110 | I4_1cd | 10 | 14 | 16 | 7 | 0 |
| 111 | P-42m | 0 | 1 | 2 | 2 | 0 |
| 112 | P-42c | 3 | 7 | 13 | 12 | 1 |
| 113 | P-42_1m | 0 | 5 | 7 | 7 | 0 |
| 114 | P-42_1c | 4 | 9 | 22 | 20 | 1 |
| 115 | P-4m2 | 0 | 3 | 4 | 4 | 0 |
| 116 | P-4c2 | 10 | 11 | 22 | 19 | 0 |
| 117 | P-4b2 | 0 | 3 | 5 | 5 | 0 |
| 118 | P-4n2 | 7 | 15 | 32 | 27 | 0 |
| 119 | I-4m2 | 3 | 13 | 14 | 14 | 0 |
| 120 | I-4c2 | 3 | 6 | 10 | 10 | 0 |
| 121 | I-42m | 3 | 12 | 15 | 14 | 1 |
| 122 | I-42d | 23 | 39 | 57 | 35 | 0 |
| 124 | P4/mcc | 0 | 4 | 5 | 5 | 0 |
| 125 | P4/nbm | 0 | 4 | 4 | 4 | 0 |
| 126 | P4/nnc | 2 | 10 | 10 | 8 | 4 |
| 127 | P4/mbm | 0 | 1 | 1 | 1 | 0 |
| 128 | P4/mnc | 4 | 14 | 14 | 14 | 1 |
| 129 | P4/nmm | 0 | 3 | 3 | 3 | 2 |
| 130 | P4/ncc | 4 | 8 | 9 | 6 | 0 |
| 131 | P4_2/mmc | 1 | 8 | 8 | 8 | 1 |
| 132 | P4_2/mcm | 0 | 5 | 7 | 7 | 0 |
| 133 | P4_2/nbc | 5 | 9 | 9 | 3 | 0 |
| 134 | P4_2/nnm | 9 | 19 | 19 | 14 | 0 |
| 135 | P4_2/mbc | 2 | 8 | 12 | 12 | 0 |
| 136 | P4_2/mnm | 2 | 12 | 13 | 12 | 0 |
| 137 | P4_2/nmc | 5 | 12 | 12 | 10 | 1 |
| 138 | P4_2/ncm | 6 | 17 | 17 | 12 | 9 |
| 139 | I4/mmm | 0 | 7 | 7 | 7 | 1 |
| 140 | I4/mcm | 4 | 10 | 10 | 9 | 1 |
| 141 | I4_1/amd | 38 | 59 | 59 | 38 | 6 |
| 142 | I4_1/acd | 22 | 28 | 29 | 6 | 0 |

## Ranking recipe (all weights explicit, deterministic)

score = 3.0*F + 10.0*[F>=20] + 4.0*log2(aut) + 2.0*log2(max stab) + 3.0*min(3, #face sizes odd>=5 or >=7) + 1.5*log2(1+#menu sightings) + 1.5*(3 - min stratum dim) + 0.1*V + 2.0*log2(#b) + 1.0*log2(#groups) + 5.0*[Schmitt ABSENT-all] -4.0*[metric-thin] -25.0*[S-cell]. Tie-break: F desc, aut desc, id asc. Shortlist = top-15 among non-S-cell rows. Weights are triage judgment, not measurements; they are stated so the ranking is reproducible and criticizable.

## Honest limits

- Schmitt flags are PROVISIONAL: visual single-pass + text-layer cross-checked (0 row discrepancies, re-verified below), NOT independently re-keyed (G5 duty still owed) — flags provisional. Any G5 verdict that leans on a specific P/A cell must first re-read that printed page (PDF page given in the worklist).
- The Schmitt cross-check is F-VECTOR level (his tables print one representative point per f-vector); the P-resolution column only says how HIS PRINTED representative reproduced in our pipeline. `other` means his printed cell for that f-vector is a different type than ours — his unprinted 14 TB may still contain ours (sampling, not enumeration; SCHMITT_DATA_RECOVERY_2026-08-28.md). `unres` rows (origin-choice-2 groups 85,86,88,125,126,129,130,133,134,137,138,141,142 and second-enantiomorph 95/96, plus the two order_cycle rows) were re-run read-only in PHASE2_SCHMITT_ORIGIN_CHECK.md but NOT stored, so their types are unknown to this triage.
- OPEN vs WALL is a LABEL from stored sightings only (same orbit persisting across >= 3 b-values vs a single b-value); no perturbation or interval computation was run. A wall-suspect type may be open in the point direction; an open-likely label is not a certificate.
- #b counts menu sightings only (P1/P3/P4/P5); the sweep ran 13 coarse + 5 Schmitt + bisection b-values, so #b is bounded by the menu, and 51 of 56 printed b-ratios were never swept.
- Aut orders are combinatorial map automorphism counts; geometric stabilizer certification is G4/V2, not claimed. Roundness, Wyckoff letters, polyform counts (G4 Burnside), Engel-1981 and Bernhard cross-checks are NOT computed here.
- The 385 Schmitt-printed-only types are not ranked (his cells, not our hunt) and the 19 cubic-store types re-sighted in tetragonal groups are out of scope here (phase-1 triage covers them).
- The ranking weights are stated judgment calls; re-ranking is one `triage_phase2.py` edit away and does not touch the store.
