# COLLISION screen — Phase-2 batch 2 (hexagonal family) at Schmitt's printed points (2026-09-04)

Script: `collision_phase2_hex_check.py` (model `collision_phase2_check.py`). Store: `phase2_hexagonal_types.json` sha256 7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55 (verified before and after: unchanged). Rows: `schmitt_hexagonal_tables.json`. Shortlist/worklist: `triage_phase2_hex_shortlist.json`. Chain: `sweep_phase2_hexagonal.evaluate` (accepted Gram modules; certificate asserted on two orbit cells; Euler; congruence). Conversion: H1 (ANCHORS G2c); second enantiomorphs verbatim then z -> -z.

**LANGUAGE (G5): DIFFERENT TYPE does not establish novelty; every survivor is "not matched against the records checked as of 2026-09-04" (Schmitt's tables print one representative per (group, f-vector) from a sampling).**

## 1. Store-side screen (all menu-sighted hexagonal types), recomputed here

- Verdicts: SURVIVOR 151, COLLISION 124, UNRESOLVED 13 of 288 menu-sighted types — MATCH with the triage's counts {'SURVIVOR': 151, 'UNRESOLVED': 13, 'COLLISION': 124}; survivor ranking identical.
- Definition: SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed row with that (group, f) reproduced (P2) as a different stored type; COLLISION = the type reproduces one of his printed cells (S-cell / SAME); UNRESOLVED = a printed row with that (group, f) was quarantined (schmitt_fvec_mismatch after both conversions), so no type-level statement is possible for that pair.

## 2. Recomputation at the printed points — top-10 survivors

| # | survivor | IT | printed f | printed b | printed point (B'') | PDF | conversion | point (ITA) | exact f | p | aut | stab | orbit | store hit | verdict | store-consistent | s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 | (44, 66, 24) | 797/1000 | (56/125, -14/125, 0) | 114 | H1 | (112/125, 42/125, 0) | (44, 66, 24) | 3^6 4^8 5^4 6^2 11^2 12^1 16^1 | 1 | 1 | 12 | 7069f26515a08a42 | **DIFFERENT TYPE** | True | 0.2 |
| 1 | `c49077384aaebeb0` | 179 | (44, 66, 24) | 797/1000 | (56/125, -14/125, 0) | 114 | H1 | (112/125, 42/125, 0) | (44, 66, 24) | 3^6 4^8 5^4 6^2 11^2 12^1 16^1 | 1 | 1 | 12 | 7069f26515a08a42 | **DIFFERENT TYPE** | True | 0.1 |
| 2 | `59585d778cb3a7a4` | 178 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | H1 | (1, 83/125, 13/500) | (40, 60, 22) | 3^6 4^7 5^4 8^2 10^1 14^2 | 1 | 1 | 12 | b7e607ffe0fdc6a6 | **DIFFERENT TYPE** | True | 0.1 |
| 2 | `59585d778cb3a7a4` | 179 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | H1+zflip | (1, 83/125, -13/500) | (40, 60, 22) | 3^6 4^7 5^4 8^2 10^1 14^2 | 1 | 1 | 12 | b7e607ffe0fdc6a6 | **DIFFERENT TYPE** | True | 0.3 |
| 3 | `095ce61d28388c98` | 178 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | H1 | (1, 83/125, 13/500) | (40, 60, 22) | 3^6 4^7 5^4 8^2 10^1 14^2 | 1 | 1 | 12 | b7e607ffe0fdc6a6 | **DIFFERENT TYPE** | True | 0.1 |
| 3 | `095ce61d28388c98` | 179 | (40, 60, 22) | 3497/1000 | (1/2, 41/250, 13/500) | 114 | H1+zflip | (1, 83/125, -13/500) | (40, 60, 22) | 3^6 4^7 5^4 8^2 10^1 14^2 | 1 | 1 | 12 | b7e607ffe0fdc6a6 | **DIFFERENT TYPE** | True | 0.2 |
| 4 | `9be0f2271a14b6a9` | 178 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1 | (1, 76/125, 19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.1 |
| 4 | `9be0f2271a14b6a9` | 179 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1+zflip | (1, 76/125, -19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.2 |
| 5 | `2d654c836f3731c6` | 169 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | H1 | (1/2, 857/1998, 0) | (36, 54, 20) | 3^4 4^4 5^4 6^2 7^4 10^2 | 1 | 1 | 6 | 04a532437a590239 | **DIFFERENT TYPE** | True | 0.1 |
| 5 | `2d654c836f3731c6` | 170 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | H1 | (1/2, 857/1998, 0) | (36, 54, 20) | 3^4 4^4 5^4 6^2 7^4 10^2 | 1 | 1 | 6 | 04a532437a590239 | **DIFFERENT TYPE** | True | 0.1 |
| 5 | `2d654c836f3731c6` | 178 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1 | (1, 76/125, 19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.1 |
| 5 | `2d654c836f3731c6` | 179 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1+zflip | (1, 76/125, -19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.3 |
| 6 | `b0f80776885f3ae1` | 178 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1 | (1, 76/125, 19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.1 |
| 6 | `b0f80776885f3ae1` | 179 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1+zflip | (1, 76/125, -19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.2 |
| 7 | `a348875c3f707895` | 169 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | H1 | (1/2, 857/1998, 0) | (36, 54, 20) | 3^4 4^4 5^4 6^2 7^4 10^2 | 1 | 1 | 6 | 04a532437a590239 | **DIFFERENT TYPE** | True | 0.1 |
| 7 | `a348875c3f707895` | 170 | (36, 54, 20) | 797/1000 | (1/4, 715/3996, 0) | 108 | H1 | (1/2, 857/1998, 0) | (36, 54, 20) | 3^4 4^4 5^4 6^2 7^4 10^2 | 1 | 1 | 6 | 04a532437a590239 | **DIFFERENT TYPE** | True | 0.1 |
| 7 | `a348875c3f707895` | 178 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1 | (1, 76/125, 19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.1 |
| 7 | `a348875c3f707895` | 179 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1+zflip | (1, 76/125, -19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.2 |
| 8 | `dcc38ea9177089b9` | 178 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1 | (1, 76/125, 19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.1 |
| 8 | `dcc38ea9177089b9` | 179 | (36, 54, 20) | 3497/1000 | (1/2, 27/250, 19/375) | 113 | H1+zflip | (1, 76/125, -19/375) | (36, 54, 20) | 3^6 4^5 5^2 6^2 8^2 10^2 12^1 | 1 | 1 | 12 | b3a4321d9c054113 | **DIFFERENT TYPE** | True | 0.4 |
| 9 | `5b86a254c715306c` | 169 | (40, 60, 22) | 797/1000 | (1/4, 685/3996, 0) | 108 | H1 | (1/2, 421/999, 0) | (40, 60, 22) | 3^6 4^2 5^4 6^6 8^2 11^2 | 1 | 1 | 6 | ed6e6228fdbafd09 | **DIFFERENT TYPE** | True | 0.1 |
| 9 | `5b86a254c715306c` | 170 | (40, 60, 22) | 797/1000 | (1/4, 685/3996, 0) | 108 | H1 | (1/2, 421/999, 0) | (40, 60, 22) | 3^6 4^2 5^4 6^6 8^2 11^2 | 1 | 1 | 6 | ed6e6228fdbafd09 | **DIFFERENT TYPE** | True | 0.1 |
| 10 | `f05f0b009e0929f6` | 169 | (32, 48, 18) | 797/1000 | (1595/5994, 403/1998, 0) | 108 | H1 | (1595/2997, 1402/2997, 0) | (32, 48, 18) | 3^2 4^8 6^2 7^2 8^4 | 2 | 1 | 6 | f94c2ae7de04a72e | **DIFFERENT TYPE** | True | 0.1 |
| 10 | `f05f0b009e0929f6` | 170 | (32, 48, 18) | 797/1000 | (1595/5994, 403/1998, 0) | 108 | H1 | (1595/2997, 1402/2997, 0) | (32, 48, 18) | 3^2 4^8 6^2 7^2 8^4 | 2 | 1 | 6 | f94c2ae7de04a72e | **DIFFERENT TYPE** | True | 0.1 |
| 10 | `f05f0b009e0929f6` | 178 | (32, 48, 18) | 3497/1000 | (19/50, 19/50, 19/300) | 113 | H1 | (19/25, 19/25, 19/300) | (32, 48, 18) | 3^8 4^2 6^2 8^4 10^2 | 1 | 1 | 12 | 3bb4e5b783529bc7 | **DIFFERENT TYPE** | True | 0.1 |
| 10 | `f05f0b009e0929f6` | 179 | (32, 48, 18) | 3497/1000 | (19/50, 19/50, 19/300) | 113 | H1+zflip | (19/25, 19/25, -19/300) | (32, 48, 18) | 3^8 4^2 6^2 8^4 10^2 | 1 | 1 | 12 | 3bb4e5b783529bc7 | **DIFFERENT TYPE** | True | 0.2 |

## Post-screen verdict, top-10 survivors

- #1 `c49077384aaebeb0` IT(178) f=(44, 66, 24) aut 2 b=5/4 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #2 `59585d778cb3a7a4` IT(178) f=(40, 60, 22) aut 2 b=3/4 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #3 `095ce61d28388c98` IT(178) f=(40, 60, 22) aut 2 b=1 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #4 `9be0f2271a14b6a9` IT(178) f=(36, 54, 20) aut 4 b=1 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #5 `2d654c836f3731c6` IT(178) f=(36, 54, 20) aut 2 b=1 O/W label open-likely: SURVIVES (all 4 printed pair(s) DIFFERENT by recomputation)
- #6 `b0f80776885f3ae1` IT(178) f=(36, 54, 20) aut 2 b=1/2 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #7 `a348875c3f707895` IT(178) f=(36, 54, 20) aut 2 b=1/2 O/W label open-likely: SURVIVES (all 4 printed pair(s) DIFFERENT by recomputation)
- #8 `dcc38ea9177089b9` IT(178) f=(36, 54, 20) aut 2 b=1/2 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #9 `5b86a254c715306c` IT(169) f=(40, 60, 22) aut 1 b=797/1000 O/W label open-likely: SURVIVES (all 2 printed pair(s) DIFFERENT by recomputation)
- #10 `f05f0b009e0929f6` IT(169) f=(32, 48, 18) aut 2 b=3/4 O/W label open-likely: SURVIVES (all 4 printed pair(s) DIFFERENT by recomputation)

## Honest limits

- Type-level only at Schmitt's printed representatives; every other Schmitt flag stays f-vector-level.
- UNRESOLVED pairs (printed rows that failed to reproduce after both documented conversions) are listed in the sweep's quarantines; no verdict is claimed for them.
- No perturbation certificates and no G4 (roundness / geometric symmetry / Burnside / Engel / Bernhard) here.
- The digitization is a text-layer parse with a 153-row visual cross-read, not an independent re-key.

Wall 4 s, single process. Deterministic except the timing columns.
