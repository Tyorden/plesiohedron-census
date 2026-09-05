# Schmitt printed-point collision screen — TOP-10 shortlist (pre-G4, 2026-08-30)

Script: `schmitt_collision_check.py` (this run: 21 pair(s)). Pattern: `schmitt_220_check.py`. Sources: Schmitt 2016 dissertation (`../references/Schmitt_2016_dissertation.pdf`), Sec. 2.2.5 per-group tables, printed pp. 119-150 (PDF page = printed + 5); frozen `spacegroups.json` (G1); `phase1_types.json` (Phase-1 ACCEPTED 2026-08-29); shortlist per `TRIAGE_RESULT.md` (2026-08-30).

**LANGUAGE (G5, stated once for every verdict below): a DIFFERENT-TYPE verdict does NOT establish novelty.** Schmitt's tables print ONE representative generating point per (group, f-vector) from a grid SAMPLING; a type absent at his printed point may still occur in his unprinted data. Every surviving candidate remains only "not matched against the catalog snapshot of 2026-08-28". A SAME-TYPE verdict IS decisive: our candidate's combinatorial type appears in Schmitt 2016 at his printed point (collision; reframe per kill criteria).

## Transcription record (visual page reads, 2026-08-30)

All 21 generating points transcribed from visual reads of the archived PDF pages and cross-checked against the pdftotext text layer; both agree verbatim on all 21 rows. Every (group, f-vector) pair flagged P by the triage digitization was found on re-read — NO discrepancies vs `triage_phase1.py`. IT(212)/IT(213) share one printed table (printed pp. 133-135); runs use the frozen IT(212) ops — `canon_code` identifies mirror images, so the verdict covers both enantiomorphs.

Two-origin groups (IT 201, 203, 224, 227, 228): Schmitt's data are origin choice 2, the G1 freeze is origin choice 1 (`SCHMITT_OPS_XCHECK_2026-08-28.md`, machine-verified x_his = x_ours + v, M = I); the printed point is converted as x_ours = x_his - v (mod 1) before orbiting (global translation — type-invariant). The v used is shown in the last column.

| pair | IT | printed f-vector | printed generating point | freq | printed p. | origin-2 -> origin-1 shift v |
|---|---|---|---|---|---|---|
| P01 | 212 | (37, 57, 22) | (-511/2124, -29/236, 1/72) | 1027 | 135 | — |
| P02 | 230 | (40, 61, 23) | (-263/2328, -149/2328, 787/3492) | 132168 | 150 | — |
| P03 | 199 | (36, 54, 20) | (379/3492, 379/3492, 379/3492) | 758 | 123 | — |
| P04 | 206 | (30, 45, 17) | (1/8, 1/8, 1/8) | 873 | 128 | — |
| P05 | 220 | (30, 45, 17) | (1/8, 1/8, 1/8) | 291 | 142 | — |
| P06 | 230 | (30, 45, 17) | (1/8, 1/8, 1/8) | 582 | 150 | — |
| P07 | 199 | (30, 45, 17) | (1/8, 1/8, 1/8) | 115 | 123 | — |
| P08 | 212 | (30, 45, 17) | (-3/8, -1/8, 1/8) | 179 | 134 | — |
| P09 | 214 | (30, 45, 17) | (1/8, 1/8, 1/8) | 1 | 136 | — |
| P10 | 203 | (16, 30, 16) | (1/8, 1/8, 1/8) | 1 | 125 | (7/8, 7/8, 7/8) |
| P11 | 210 | (16, 30, 16) | (0, 0, 0) | 1 | 132 | — |
| P12 | 212 | (16, 30, 16) | (0, 0, 0) | 1 | 134 | — |
| P13 | 227 | (16, 30, 16) | (1/8, 1/8, 1/8) | 1 | 147 | (7/8, 7/8, 7/8) |
| P14 | 198 | (32, 48, 18) | (1/8, 1/8, 1/8) | 207 | 122 | — |
| P15 | 212 | (32, 48, 18) | (1/8, 1/8, 1/8) | 1 | 134 | — |
| P16 | 212 | (30, 46, 18) | (-55/708, -239/2124, -329/4248) | 7322558 | 134 | — |
| P17 | 214 | (30, 47, 19) | (-455/6984, -73/776, 545/3492) | 48889552 | 136 | — |
| P18 | 201 | (25, 39, 16) | (1817/7264, 1817/7264, 1815/7264) | 5445 | 124 | (3/4, 3/4, 3/4) |
| P19 | 208 | (25, 39, 16) | (1815/7264, 1815/7264, 1815/7264) | 1815 | 130 | — |
| P20 | 224 | (25, 39, 16) | (1817/7264, 1817/7264, 1815/7264) | 5445 | 145 | (3/4, 3/4, 3/4) |
| P21 | 228 | (25, 39, 16) | (180/1441, 180/1441, 180/1441) | 4320 | 147 | (1/8, 1/8, 5/8) |

## Per-pair verdicts

| pair | rank | target type | IT | f-vector | orbit | stab | PERIOD | Schmitt cell p-vector | aut | verdict | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 1 | `ceb70631e274e727` | 212 | (37, 57, 22) | 24 | 1 | 4248 | `3^9 4^4 6^2 7^2 8^4 13^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 4.2 |
| P02 | 2 | `359beee832567a71` | 230 | (40, 61, 23) | 96 | 1 | 6984 | `3^2 4^10 5^6 6^1 8^1 10^2 12^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 59.9 |
| P03 | 3 | `fd96e7fc36481986` | 199 | (36, 54, 20) | 8 | 3 | 3492 | `3^12 6^2 10^6` | 12 | **SAME TYPE** | 0.5 |
| P04 | 4 | `998994bcf8df722b` | 206 | (30, 45, 17) | 16 | 3 | 24 | `4^12 6^2 10^3` | 12 | **SAME TYPE** [point = stored sighting point: collision foregone] | 1.2 |
| P05 | 4 | `998994bcf8df722b` | 220 | (30, 45, 17) | 16 | 3 | 24 | `4^12 6^2 10^3` | 12 | **SAME TYPE** [point = stored sighting point: collision foregone] | 1.2 |
| P06 | 4 | `998994bcf8df722b` | 230 | (30, 45, 17) | 16 | 6 | 24 | `4^12 6^2 10^3` | 12 | **SAME TYPE** [point = stored sighting point: collision foregone] | 1.2 |
| P07 | 5 | `8c69db9e84095469` | 199 | (30, 45, 17) | 8 | 3 | 24 | `4^6 5^6 6^2 8^3` | 12 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.3 |
| P08 | 5 | `8c69db9e84095469` | 212 | (30, 45, 17) | 8 | 3 | 24 | `4^6 5^6 6^2 8^3` | 12 | **SAME TYPE** | 0.3 |
| P09 | 5 | `8c69db9e84095469` | 214 | (30, 45, 17) | 8 | 6 | 24 | `4^6 5^6 6^2 8^3` | 12 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.3 |
| P10 | 6 | `2001fe7ea92fd0ad` | 203 | (16, 30, 16) | 8 | 12 | 12 | `3^12 6^4` | 24 | **SAME TYPE** | 0.2 |
| P11 | 6 | `2001fe7ea92fd0ad` | 210 | (16, 30, 16) | 8 | 12 | 12 | `3^12 6^4` | 24 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.2 |
| P12 | 6 | `2001fe7ea92fd0ad` | 212 | (16, 30, 16) | 8 | 3 | 12 | `3^12 6^4` | 24 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.2 |
| P13 | 6 | `2001fe7ea92fd0ad` | 227 | (16, 30, 16) | 8 | 24 | 12 | `3^12 6^4` | 24 | **SAME TYPE** | 0.2 |
| P14 | 7 | `afeb1ae44c1a3443` | 198 | (32, 48, 18) | 4 | 3 | 24 | `4^12 8^6` | 6 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.1 |
| P15 | 7 | `afeb1ae44c1a3443` | 212 | (32, 48, 18) | 4 | 6 | 24 | `4^12 8^6` | 6 | **SAME TYPE** [point = stored sighting point: collision foregone] | 0.1 |
| P16 | 8 | `c314dedd38208a2e` | 212 | (30, 46, 18) | 24 | 1 | 4248 | `4^7 5^4 6^5 7^2` | 1 | **DIFFERENT TYPE** (not any stored type) | 2.9 |
| P17 | 9 | `aa6b0077c3234d24` | 214 | (30, 47, 19) | 48 | 1 | 6984 | `3^4 4^10 6^1 7^2 8^1 14^1` | 1 | **DIFFERENT TYPE** (not any stored type) | 11.3 |
| P18 | 10 | `ea1baec328356a32` | 201 | (25, 39, 16) | 8 | 3 | 21792 | `4^12 6^3 12^1` | 6 | **SAME TYPE** | 0.3 |
| P19 | 10 | `ea1baec328356a32` | 208 | (25, 39, 16) | 8 | 3 | 21792 | `4^12 6^3 12^1` | 6 | **SAME TYPE** | 0.3 |
| P20 | 10 | `ea1baec328356a32` | 224 | (25, 39, 16) | 8 | 6 | 21792 | `4^12 6^3 12^1` | 6 | **SAME TYPE** | 0.3 |
| P21 | 10 | `ea1baec328356a32` | 228 | (25, 39, 16) | 64 | 3 | 34584 | `4^12 6^3 12^1` | 6 | **SAME TYPE** | 15.8 |

## Summary (this run)

- rank 1 `ceb70631e274e727`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 2 `359beee832567a71`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 3 `fd96e7fc36481986`: COLLISION — the type is Schmitt's printed cell in 1/1 checked group(s); reframe per kill criteria (not a new sighting-class candidate).
- rank 4 `998994bcf8df722b`: COLLISION — the type is Schmitt's printed cell in 3/3 checked group(s); reframe per kill criteria (not a new sighting-class candidate).
- rank 5 `8c69db9e84095469`: COLLISION — the type is Schmitt's printed cell in 3/3 checked group(s); reframe per kill criteria (not a new sighting-class candidate).
- rank 6 `2001fe7ea92fd0ad`: COLLISION — the type is Schmitt's printed cell in 4/4 checked group(s); reframe per kill criteria (not a new sighting-class candidate).
- rank 7 `afeb1ae44c1a3443`: COLLISION — the type is Schmitt's printed cell in 2/2 checked group(s); reframe per kill criteria (not a new sighting-class candidate).
- rank 8 `c314dedd38208a2e`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 9 `aa6b0077c3234d24`: survives this screen (all 1 pair(s) DIFFERENT); proceeds to G4 under snapshot language only.
- rank 10 `ea1baec328356a32`: COLLISION — the type is Schmitt's printed cell in 4/4 checked group(s); reframe per kill criteria (not a new sighting-class candidate).

## Notes

- Special positions (stab > 1) handled by `orbit.py` normally; the orbit/stab columns record them.
- "[point = stored sighting point]" marks pairs where Schmitt's printed representative point, converted to our setting, is EXACTLY a point our Phase-1 sweep already sampled for the target type — the SAME verdict there is a deterministic recomputation, recorded for completeness.
- Where a DIFFERENT verdict names a stored type, that means Schmitt's printed representative for the f-vector is itself a type our sweep also found — the two types share an f-vector in that group (same class of micro-fact as the Josehedron / Schmitt-220 result, `SCHMITT_220_CHECK_RESULT.md`).
- Per-pair wall-clock cap 600 s -> TIMEOUT-DEFERRED (recorded, never silent).
- Certificate asserted per cell: float/exact facet-count and p-vector agreement, and 4*rho^2 <= D^2 exact cutoff; one canonical code across the whole orbit.
