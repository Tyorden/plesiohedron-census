# Batch-2 read-only check: the 46 IT(180) P6_222 Schmitt f-vector mismatches (2026-09-04)

Store `phase2_hexagonal_types.json` sha256 7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55 (unchanged after: True); nothing added.
Cause (Schmitt's own remark on the 180/181 table, PDF 114): the normalizer/basis given is "only the normalizer for IT(181) but not for IT(180)" — the printed points are IT(181)'s (the second-listed member); the pre-registered rule applied z -> -z only to the second-listed group, so IT(180) ran verbatim and 46 of 69 rows failed (the 23 that passed are z-flip-insensitive). IT(181) reproduced all 69 verbatim. Same pattern as 178/179 (remark names 178; 179 needed z -> -z on 77 of 97 rows) and as 95/96 in batch 1.

Result: **46 of 46 quarantined rows reproduce the printed f-vector under z -> -z (then H1)**; 46 of those cells are already in the store, 0 are not (read-only, not added).

| printed f | b | printed point (B'') | PDF | point (ITA) | exact f | p | aut | stab | store hit |
|---|---|---|---|---|---|---|---|---|---|
| (14, 22, 10) | 3497/1000 | (83/250, 1/250, 83/1500) | 115 | (83/125, 42/125, -83/1500) | (14, 22, 10) | 3^2 4^3 5^4 6^1 | 1 | 1 | 7dd584f7924de471 |
| (15, 27, 14) | 4/5 | (47/125, 0, 1/60) | 115 | (94/125, 47/125, -1/60) | (15, 27, 14) | 3^7 4^5 6^1 7^1 | 1 | 1 | 6b03d68d8d6171af |
| (17, 29, 14) | 7/2 | (38/125, 38/125, 3/125) | 115 | (76/125, 76/125, -3/125) | (17, 29, 14) | 3^7 4^2 5^1 6^4 | 1 | 1 | 7576968c4324ffe3 |
| (20, 32, 14) | 3497/1000 | (123/250, 123/250, 1/1500) | 115 | (123/125, 123/125, -1/1500) | (20, 32, 14) | 3^3 4^6 6^4 7^1 | 1 | 1 | 9525899c411056fa |
| (21, 33, 14) | 797/1000 | (109/250, -77/250, 109/1500) | 115 | (109/125, 16/125, -109/1500) | (21, 33, 14) | 3^2 4^6 5^1 6^4 7^1 | 1 | 1 | ef777e629db11061 |
| (20, 33, 15) | 3497/1000 | (62/125, 0, 11/375) | 115 | (124/125, 62/125, -11/375) | (20, 33, 15) | 3^5 4^6 6^2 7^1 8^1 | 1 | 1 | 6e1c279805390881 |
| (21, 34, 15) | 3497/1000 | (4/25, 4/25, 2/75) | 115 | (8/25, 8/25, -2/75) | (21, 34, 15) | 3^6 4^3 5^2 6^2 8^2 | 1 | 1 | 52f9e465a88e02ac |
| (23, 36, 15) | 3497/1000 | (62/125, -61/125, 1/1500) | 115 | (124/125, 1/125, -1/1500) | (23, 36, 15) | 3^6 4^3 6^3 7^1 8^1 9^1 | 1 | 1 | 0356e39f6df73395 |
| (26, 39, 15) | 797/1000 | (79/250, -3/250, 79/1500) | 115 | (79/125, 38/125, -79/1500) | (26, 39, 15) | 4^7 5^2 6^4 8^2 | 4 | 1 | 59f890334e777569 |
| (25, 39, 16) | 7/2 | (34/125, -3/125, 4/375) | 115 | (68/125, 31/125, -4/375) | (25, 39, 16) | 3^4 4^4 5^2 6^4 8^2 | 1 | 1 | ea936ae21d441585 |
| (26, 40, 16) | 3497/1000 | (1/2, 121/250, 1/1500) | 115 | (1, 123/125, -1/1500) | (26, 40, 16) | 3^3 4^6 5^2 6^2 8^2 9^1 | 1 | 1 | 8430e7743b5ddeed |
| (28, 42, 16) | 3497/1000 | (1/2, -1/50, 1/25) | 115 | (1, 12/25, -1/25) | (28, 42, 16) | 4^9 6^4 8^3 | 4 | 1 | 2a139a0af47705e5 |
| (27, 42, 17) | 7/2 | (21/50, -33/250, 3/125) | 115 | (21/25, 36/125, -3/125) | (27, 42, 17) | 3^6 4^4 5^2 6^1 8^3 10^1 | 1 | 1 | ed4d1cdf15633bb1 |
| (29, 44, 17) | 1037/1000 | (46/125, 26/125, 1/15) | 115 | (92/125, 72/125, -1/15) | (29, 44, 17) | 4^10 5^3 6^2 10^1 11^1 | 1 | 1 | 548f98c25d7dd1e0 |
| (30, 45, 17) | 3497/1000 | (51/250, 27/250, 17/500) | 115 | (51/125, 39/125, -17/500) | (30, 45, 17) | 3^6 4^1 6^6 8^4 | 2 | 1 | 56b1d49a0766cc47 |
| (29, 45, 18) | 4/5 | (62/125, 48/125, 1/60) | 116 | (124/125, 22/25, -1/60) | (29, 45, 18) | 3^6 4^6 6^4 12^2 | 1 | 1 | 99ef4fc6720ffa5d |
| (31, 47, 18) | 239/250 | (44/125, 19/125, 2/25) | 116 | (88/125, 63/125, -2/25) | (31, 47, 18) | 3^5 4^4 5^2 6^3 8^3 11^1 | 1 | 1 | c9def3cd6baea0bf |
| (31, 48, 19) | 7/2 | (12/25, 6/125, 3/125) | 116 | (24/25, 66/125, -3/125) | (31, 48, 19) | 3^8 4^5 6^1 8^3 10^1 12^1 | 1 | 1 | b7ef0f94aba2ed89 |
| (33, 50, 19) | 797/1000 | (91/250, 69/250, 1/12) | 116 | (91/125, 16/25, -1/12) | (33, 50, 19) | 3^1 4^12 5^2 6^2 12^1 15^1 | 1 | 1 | d576e34a75c5486d |
| (34, 51, 19) | 3497/1000 | (51/250, 29/250, 17/500) | 116 | (51/125, 8/25, -17/500) | (34, 51, 19) | 3^4 4^8 6^2 8^2 10^3 | 1 | 1 | 67d482ba9032f1f3 |
| (33, 51, 20) | 7/2 | (38/125, 16/125, 2/125) | 116 | (76/125, 54/125, -2/125) | (33, 51, 20) | 3^6 4^8 6^2 8^1 10^2 12^1 | 1 | 1 | d3cab063f07b542b |
| (35, 53, 20) | 797/1000 | (17/50, 3/50, 1/30) | 116 | (17/25, 2/5, -1/30) | (35, 53, 20) | 3^3 4^10 6^4 8^1 11^1 14^1 | 1 | 1 | d7205a2af75f3a5d |
| (36, 54, 20) | 3497/1000 | (51/250, 33/250, 17/500) | 116 | (51/125, 42/125, -17/500) | (36, 54, 20) | 3^4 4^9 6^2 8^2 10^2 12^1 | 1 | 1 | 3b621bdbd8e8299d |
| (34, 53, 21) | 4/5 | (38/125, -17/125, 1/20) | 116 | (76/125, 21/125, -1/20) | (34, 53, 21) | 3^6 4^9 5^1 6^1 8^1 9^1 10^1 14^1 | 1 | 1 | 84921e8510cd5928 |
| (35, 54, 21) | 797/1000 | (89/250, 41/250, 1/12) | 116 | (89/125, 13/25, -1/12) | (35, 54, 21) | 3^8 4^6 6^3 8^1 10^2 14^1 | 1 | 1 | 3376116a2ea4e253 |
| (37, 56, 21) | 797/1000 | (17/50, 13/50, 1/20) | 116 | (17/25, 3/5, -1/20) | (37, 56, 21) | 3^8 4^5 5^2 6^2 10^2 12^1 14^1 | 1 | 1 | e9f44af869caa1b9 |
| (38, 57, 21) | 3497/1000 | (11/125, -2/125, 11/750) | 116 | (22/125, 9/125, -11/750) | (38, 57, 21) | 3^6 4^5 5^4 6^1 8^2 10^1 12^2 | 1 | 1 | 29d339694a25bff4 |
| (37, 57, 22) | 797/1000 | (52/125, 49/125, 1/12) | 116 | (104/125, 101/125, -1/12) | (37, 57, 22) | 3^4 4^11 5^2 6^2 10^1 12^1 14^1 | 1 | 1 | 8bd6a83d55f18ed6 |
| (39, 59, 22) | 3497/1000 | (91/250, 73/250, 1/150) | 116 | (91/125, 82/125, -1/150) | (39, 59, 22) | 3^8 4^5 5^1 6^2 8^3 9^1 12^2 | 1 | 1 | 70de5928430e4dfa |
| (40, 60, 22) | 3497/1000 | (51/250, 31/250, 17/500) | 116 | (51/125, 41/125, -17/500) | (40, 60, 22) | 3^6 4^9 6^3 10^1 12^2 14^1 | 1 | 1 | 64fc858ce31f237e |
| (39, 60, 23) | 797/1000 | (2/5, 9/25, 1/15) | 116 | (4/5, 19/25, -1/15) | (39, 60, 23) | 3^8 4^7 5^2 6^1 8^3 12^1 16^1 | 1 | 1 | 93562a81bb92cc58 |
| (41, 62, 23) | 797/1000 | (37/125, -18/125, 1/30) | 116 | (74/125, 19/125, -1/30) | (41, 62, 23) | 3^8 4^6 5^3 8^2 9^1 10^2 16^1 | 1 | 1 | d5a14515db2d8250 |
| (42, 63, 23) | 3497/1000 | (19/50, -37/250, 29/1500) | 116 | (19/25, 29/125, -29/1500) | (42, 63, 23) | 3^8 4^7 5^2 8^3 12^2 16^1 | 1 | 1 | 48f3d1fe4be770c7 |
| (41, 63, 24) | 7/2 | (38/125, 31/125, 4/375) | 116 | (76/125, 69/125, -4/375) | (41, 63, 24) | 3^6 4^12 6^2 8^1 10^1 14^1 16^1 | 1 | 1 | c4ec28114da0d78d |
| (43, 65, 24) | 5/4 | (87/250, 33/250, 1/30) | 116 | (87/125, 12/25, -1/30) | (43, 65, 24) | 3^8 4^5 5^5 6^3 11^1 14^1 18^1 | 1 | 1 | f0839c8e1fb11aaf |
| (44, 66, 24) | 3497/1000 | (11/25, 49/125, 1/1500) | 116 | (22/25, 104/125, -1/1500) | (44, 66, 24) | 3^8 4^5 5^2 6^3 8^3 10^1 12^1 14^1 | 1 | 1 | ab408b51ce561d60 |
| (43, 66, 25) | 797/1000 | (9/25, 8/25, 1/12) | 116 | (18/25, 17/25, -1/12) | (43, 66, 25) | 3^10 4^7 5^2 6^1 8^2 12^2 18^1 | 1 | 1 | e0211b03b98be76b |
| (45, 68, 25) | 797/1000 | (49/125, 44/125, 1/15) | 116 | (98/125, 93/125, -1/15) | (45, 68, 25) | 3^10 4^7 5^1 6^3 10^1 12^1 14^1 19^1 | 1 | 1 | cf1c666e448aec63 |
| (46, 69, 25) | 3497/1000 | (99/250, 63/250, 1/1500) | 116 | (99/125, 81/125, -1/1500) | (46, 69, 25) | 3^6 4^9 5^4 6^1 8^2 10^1 14^1 18^1 | 1 | 1 | 0354bcf48e5bebdd |
| (45, 69, 26) | 2 | (33/125, 6/25, 9/125) | 116 | (66/125, 63/125, -9/125) | (45, 69, 26) | 3^4 4^15 5^2 6^2 10^1 16^1 18^1 | 1 | 1 | 5cc36d137c7f7ea3 |
| (47, 71, 26) | 1289/1000 | (37/125, -28/125, 1/15) | 116 | (74/125, 9/125, -1/15) | (47, 71, 26) | 3^7 4^11 5^2 6^2 8^1 11^1 14^1 22^1 | 1 | 1 | ebc3cb62fc458909 |
| (48, 72, 26) | 3497/1000 | (47/125, 19/125, 1/750) | 116 | (94/125, 66/125, -1/750) | (48, 72, 26) | 3^10 4^4 5^2 6^6 8^1 10^1 14^1 20^1 | 1 | 1 | 66fff2600d007e47 |
| (50, 75, 27) | 3497/1000 | (51/125, 31/125, 1/1500) | 116 | (102/125, 82/125, -1/1500) | (50, 75, 27) | 3^8 4^9 5^4 6^1 8^2 10^1 18^1 20^1 | 1 | 1 | 997f6bb57a677b06 |
| (52, 78, 28) | 3497/1000 | (9/25, 17/125, 1/300) | 116 | (18/25, 62/125, -1/300) | (52, 78, 28) | 3^6 4^12 5^4 6^3 12^1 16^1 24^1 | 1 | 1 | 06add8f1c3ab58b2 |
| (54, 81, 29) | 3497/1000 | (87/250, 23/250, 1/500) | 116 | (87/125, 11/25, -1/500) | (54, 81, 29) | 3^8 4^12 5^2 6^2 8^2 10^1 18^1 24^1 | 1 | 1 | fd698eb31be754ab |
| (56, 84, 30) | 607/500 | (34/125, -31/125, 67/1500) | 116 | (68/125, 3/125, -67/1500) | (56, 84, 30) | 3^10 4^9 5^2 6^2 7^2 8^2 12^1 16^1 22^1 | 1 | 1 | 37a9ed6e464c98df |

## Menu-sighted hexagonal types with an IT(180) sighting and an f-vector among these 46 rows (19; of which 13 are the triage's UNRESOLVED types), resolved read-only

| id | f | aut | printed 180 rows with this f | triage class | SAME | verdict |
|---|---|---|---|---|---|---|
| `1a36f90bbc759307` | (28, 42, 16) | 4 | 1 | COLLISION (S-cell already) | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `1f08da5f6863d52a` | (34, 51, 19) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `261f28c9d7f6135a` | (36, 54, 20) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `2a139a0af47705e5` | (28, 42, 16) | 4 | 1 | COLLISION (S-cell already) | 1 | SAME TYPE at a printed 180 row -> would be COLLISION (reframe) |
| `303d3c41bbb6461d` | (30, 45, 17) | 2 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `364e84ece2d20d22` | (34, 51, 19) | 2 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `3d920f206ca7a132` | (42, 63, 23) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `4b3b208f06666863` | (23, 36, 15) | 2 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `54ec9db30372ac68` | (38, 57, 21) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `56b1d49a0766cc47` | (30, 45, 17) | 2 | 1 | COLLISION (S-cell already) | 1 | SAME TYPE at a printed 180 row -> would be COLLISION (reframe) |
| `59f890334e777569` | (26, 39, 15) | 4 | 1 | COLLISION (S-cell already) | 1 | SAME TYPE at a printed 180 row -> would be COLLISION (reframe) |
| `5a0120ccceb4ecc4` | (28, 42, 16) | 2 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `5ecea070beaf2efa` | (20, 33, 15) | 2 | 1 | COLLISION (S-cell already) | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `7311ebf1145936e7` | (34, 51, 19) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `8126183cde7ea2f3` | (36, 54, 20) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `b24fc960c48a9c3c` | (44, 66, 24) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `c23407c24f02fc46` | (20, 32, 14) | 2 | 1 | COLLISION (S-cell already) | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `ce4b84e9cad35f0a` | (25, 39, 16) | 2 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |
| `dd68dc31f1bba1af` | (40, 60, 22) | 1 | 1 | UNRESOLVED in the triage | 0 | DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only) |

Limits: read-only; the store's 46 quarantines stand as recorded (the sweep is not patched); these cells enter no count. Language: a DIFFERENT verdict is not novelty; snapshot language only.

Wall 8 s.
