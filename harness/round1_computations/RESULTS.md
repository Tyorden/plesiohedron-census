# Round-1 computations for the seven-shape paper (2026-09-03)

Scripts c1-c5 in this directory; all exact (fractions.Fraction) on the frozen harness (orbit.py, exact_cell.py, canon_code.py, phase1_types.json, the banked g4 tables). Regenerate with run_all.sh; each script's stdout is in c*_run.log. Written by Claude (Fable 5.1) in a Claude Code session as the round-1 fix-editor task; machine results, not AI-generated numbers. Acceptance: main-session re-run of run_all.sh, exit 0.

## C1 -- wall/open classification within the Wyckoff stratum

Method: tangent directions of the stratum = fixed subspace of the site stabilizer's linear parts; steps of +-1/96 and +-1/48 (fractional, conventional cell) along each; exact chain; canonical code compared with the store. OPEN = unchanged in every step; WALL = changes on both sides along some direction. Off-stratum rows (marked) are supplementary only.

| cell | group | point | stratum dim | tangent basis | verdict | perturbed types seen (f, p, stored id, f printed in the group's Schmitt table) |
|---|---|---|---|---|---|---|
| S | 220 | (0, 0, 1/4) | 1 | [(1, 0, 0)] | **WALL** | (22, 35, 15) 3^4 5^10 8^1 [0ee26ed471c923e2; printed=True]; (22, 35, 15) 3^6 4^1 6^8 [not stored; printed=True] |
| O | 201 | (1/8, 1/6, 5/12) | 3 | [(1, 0, 0), (0, 1, 0), (0, 0, 1)] | **OPEN** | none (all SAME) |
| P11 | 224 | (1/12, 3/8, 3/8) | 2 | [(1, 0, 0), (0, 1, 1)] | **OPEN** | none (all SAME) |
| P7 | 224 | (1/8, 1/6, 5/12) | 3 | [(1, 0, 0), (0, 1, 0), (0, 0, 1)] | **OPEN** | none (all SAME) |
| H212 | 212 | (1/12, 1/12, 1/12) | 1 | [(1, 1, 1)] | **OPEN** | none (all SAME) |
| H230 | 230 | (1/12, 1/6, 1/8) | 1 | [(-1, 1, 0)] | **OPEN** | none (all SAME) |
| H214 | 214 | (0, 1/4, 1/12) | 1 | [(0, 0, 1)] | **OPEN** (open interval is short: the +1/96 step leaves it, +1/192 does not; see line scan) | (30, 47, 19) 3^6 4^7 6^2 8^2 10^2 [not stored; printed=True]; (34, 53, 21) 3^2 4^13 6^4 12^2 [not stored; printed=True]; (38, 59, 23) 3^8 4^4 6^6 7^2 8^1 10^2 [not stored; printed=True] |

### Per-step detail

**S Satchelhedron** (8cf50403cf88c455), base f=(16, 25, 11) p=3^2 4^1 5^8:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (1, 0, 0) | -1/48 | (-1/48, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) | -1/96 | (-1/96, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) | 1/96 | (1/96, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) | 1/48 | (1/48, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) | -1/24 | (-1/24, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) | 1/24 | (1/24, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (refine) | -1/192 | (-1/192, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) (refine) | -1/384 | (-1/384, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) (refine) | -1/768 | (-1/768, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) (refine) | -1/1536 | (-1/1536, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | DIFFERENT | 0ee26ed471c923e2 | True |
| (1, 0, 0) (refine) | 1/192 | (1/192, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (refine) | 1/384 | (1/384, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (refine) | 1/768 | (1/768, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (refine) | 1/1536 | (1/1536, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | DIFFERENT | - | True |
| (0, 1, 0) (off-stratum) | -1/96 | (0, -1/96, 1/4) | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 4 | DIFFERENT | - | True |
| (0, 1, 0) (off-stratum) | 1/96 | (0, 1/96, 1/4) | 1 | (20, 32, 14) | 3^2 4^6 5^2 6^4 | 4 | DIFFERENT | - | True |

**O Ordenhedron** (2de0a21129cabe90), base f=(20, 33, 15) p=3^6 4^3 5^2 6^2 7^2:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |
| (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | 5 | SAME | 2de0a21129cabe90 | False |

**P11 Pn-3m 11-facet cell** (c4ea3f32fdd6dc51), base f=(14, 23, 11) p=3^4 4^4 6^3:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (1, 0, 0) | -1/48 | (1/16, 3/8, 3/8) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (1, 0, 0) | -1/96 | (7/96, 3/8, 3/8) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (1, 0, 0) | 1/96 | (3/32, 3/8, 3/8) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (1, 0, 0) | 1/48 | (5/48, 3/8, 3/8) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (0, 1, 1) | -1/48 | (1/12, 17/48, 17/48) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (0, 1, 1) | -1/96 | (1/12, 35/96, 35/96) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (0, 1, 1) | 1/96 | (1/12, 37/96, 37/96) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (0, 1, 1) | 1/48 | (1/12, 19/48, 19/48) | 2 | (14, 23, 11) | 3^4 4^4 6^3 | 4 | SAME | c4ea3f32fdd6dc51 | False |
| (0, 1, 0) (off-stratum) | -1/96 | (1/12, 35/96, 3/8) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | DIFFERENT | f98a3ee5675fc121 | False |
| (0, 1, 0) (off-stratum) | 1/96 | (1/12, 37/96, 3/8) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | DIFFERENT | f98a3ee5675fc121 | False |

**P7 Pn-3m 7-facet cell** (f98a3ee5675fc121), base f=(10, 15, 7) p=3^2 4^3 6^2:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (1, 0, 0) | -1/48 | (5/48, 1/6, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (1, 0, 0) | -1/96 | (11/96, 1/6, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (1, 0, 0) | 1/96 | (13/96, 1/6, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (1, 0, 0) | 1/48 | (7/48, 1/6, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 1, 0) | -1/48 | (1/8, 7/48, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 1, 0) | -1/96 | (1/8, 5/32, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 1, 0) | 1/96 | (1/8, 17/96, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 1, 0) | 1/48 | (1/8, 3/16, 5/12) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 0, 1) | -1/48 | (1/8, 1/6, 19/48) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 0, 1) | -1/96 | (1/8, 1/6, 13/32) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 0, 1) | 1/96 | (1/8, 1/6, 41/96) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |
| (0, 0, 1) | 1/48 | (1/8, 1/6, 7/16) | 1 | (10, 15, 7) | 3^2 4^3 6^2 | 0 | SAME | f98a3ee5675fc121 | False |

**H212 IT(212) (37,57,22) cell** (ceb70631e274e727), base f=(37, 57, 22) p=3^6 4^6 5^6 10^3 12^1:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (1, 1, 1) | -1/48 | (1/16, 1/16, 1/16) | 3 | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | SAME | ceb70631e274e727 | True |
| (1, 1, 1) | -1/96 | (7/96, 7/96, 7/96) | 3 | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | SAME | ceb70631e274e727 | True |
| (1, 1, 1) | 1/96 | (3/32, 3/32, 3/32) | 3 | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | SAME | ceb70631e274e727 | True |
| (1, 1, 1) | 1/48 | (5/48, 5/48, 5/48) | 3 | (37, 57, 22) | 3^6 4^6 5^6 10^3 12^1 | 3 | SAME | ceb70631e274e727 | True |
| (1, 0, 0) (off-stratum) | -1/96 | (7/96, 1/12, 1/12) | 1 | (24, 38, 16) | 3^4 4^2 5^6 6^2 7^2 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (off-stratum) | 1/96 | (3/32, 1/12, 1/12) | 1 | (28, 45, 19) | 3^8 4^1 5^4 6^4 8^1 10^1 | 6 | DIFFERENT | - | True |

**H230 IT(230) (40,61,23) cell** (359beee832567a71), base f=(40, 61, 23) p=4^20 11^2 20^1:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (-1, 1, 0) | -1/48 | (5/48, 7/48, 1/8) | 2 | (40, 61, 23) | 4^20 11^2 20^1 | 2 | SAME | 359beee832567a71 | True |
| (-1, 1, 0) | -1/96 | (3/32, 5/32, 1/8) | 2 | (40, 61, 23) | 4^20 11^2 20^1 | 2 | SAME | 359beee832567a71 | True |
| (-1, 1, 0) | 1/96 | (7/96, 17/96, 1/8) | 2 | (40, 61, 23) | 4^20 11^2 20^1 | 2 | SAME | 359beee832567a71 | True |
| (-1, 1, 0) | 1/48 | (1/16, 3/16, 1/8) | 2 | (40, 61, 23) | 4^20 11^2 20^1 | 2 | SAME | 359beee832567a71 | True |
| (1, 0, 0) (off-stratum) | -1/96 | (7/96, 1/6, 1/8) | 1 | (23, 36, 15) | 4^10 5^3 6^1 11^1 | 3 | DIFFERENT | - | True |
| (1, 0, 0) (off-stratum) | 1/96 | (3/32, 1/6, 1/8) | 1 | (23, 36, 15) | 4^10 5^3 6^1 11^1 | 3 | DIFFERENT | - | True |

**H214 IT(214) (30,47,19) cell** (aa6b0077c3234d24), base f=(30, 47, 19) p=3^4 4^5 5^6 6^2 10^2:

| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |
|---|---|---|---|---|---|---|---|---|---|
| (0, 0, 1) | -1/48 | (0, 1/4, 1/16) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | DIFFERENT | - | True |
| (0, 0, 1) | -1/96 | (0, 1/4, 7/96) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | SAME | aa6b0077c3234d24 | True |
| (0, 0, 1) | 1/96 | (0, 1/4, 3/32) | 2 | (34, 53, 21) | 3^2 4^13 6^4 12^2 | 4 | DIFFERENT | - | True |
| (0, 0, 1) | 1/48 | (0, 1/4, 5/48) | 2 | (38, 59, 23) | 3^8 4^4 6^6 7^2 8^1 10^2 | 4 | DIFFERENT | - | True |
| (0, 0, 1) (refine) | 1/192 | (0, 1/4, 17/192) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | SAME | aa6b0077c3234d24 | True |
| (1, 0, 0) (off-stratum) | -1/96 | (-1/96, 1/4, 1/12) | 1 | (32, 50, 20) | 3^10 4^3 6^2 7^2 8^1 10^1 14^1 | 4 | DIFFERENT | - | True |
| (1, 0, 0) (off-stratum) | 1/96 | (1/96, 1/4, 1/12) | 1 | (32, 50, 20) | 3^10 4^3 6^2 7^2 8^1 10^1 14^1 | 4 | DIFFERENT | - | True |

Satchelhedron: (22,35,15) is PRESENT in the digitized Schmitt IT(220) table (triage_phase1.py).

### Context: type along the whole line (grid of the sweep was k/24 at most)

### Line scan for S (24d line x,0,1/4): p0 + t*(1, 0, 0), t = k/96

| t | point | site stab | f | p | non-simple | stored id | same as witness |
|---|---|---|---|---|---|---|---|
| -1/8 | (-1/8, 0, 1/4) | 4 | (12, 22, 12) | 3^4 4^8 | 8 | dfccc9ff6019ead5 | False |
| -11/96 | (-11/96, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -5/48 | (-5/48, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -3/32 | (-3/32, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/12 | (-1/12, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -7/96 | (-7/96, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/16 | (-1/16, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -5/96 | (-5/96, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/24 | (-1/24, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/32 | (-1/32, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/48 | (-1/48, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| -1/96 | (-1/96, 0, 1/4) | 2 | (22, 35, 15) | 3^4 5^10 8^1 | 4 | 0ee26ed471c923e2 | False |
| 0 | (0, 0, 1/4) | 2 | (16, 25, 11) | 3^2 4^1 5^8 | 2 | 8cf50403cf88c455 | True |
| 1/96 | (1/96, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 1/48 | (1/48, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 1/32 | (1/32, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 1/24 | (1/24, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 5/96 | (5/96, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 1/16 | (1/16, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 7/96 | (7/96, 0, 1/4) | 2 | (22, 35, 15) | 3^6 4^1 6^8 | 4 | - | False |
| 1/12 | (1/12, 0, 1/4) | 2 | (15, 26, 13) | 3^4 4^5 5^4 | 7 | dd90029f74b374ae | False |
| 3/32 | (3/32, 0, 1/4) | 2 | (20, 32, 14) | 4^10 6^4 | 4 | 1006ba9d7710fc74 | False |
| 5/48 | (5/48, 0, 1/4) | 2 | (20, 32, 14) | 4^10 6^4 | 4 | 1006ba9d7710fc74 | False |
| 11/96 | (11/96, 0, 1/4) | 2 | (20, 32, 14) | 4^10 6^4 | 4 | 1006ba9d7710fc74 | False |
| 1/8 | (1/8, 0, 1/4) | 2 | (20, 32, 14) | 4^10 6^4 | 4 | 1006ba9d7710fc74 | False |

### Line scan for H214 (24f line 0,1/4,z): p0 + t*(0, 0, 1), t = k/192

| t | point | site stab | f | p | non-simple | stored id | same as witness |
|---|---|---|---|---|---|---|---|
| -1/24 | (0, 1/4, 1/24) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -7/192 | (0, 1/4, 3/64) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -1/32 | (0, 1/4, 5/96) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -5/192 | (0, 1/4, 11/192) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -1/48 | (0, 1/4, 1/16) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -1/64 | (0, 1/4, 13/192) | 2 | (30, 47, 19) | 3^6 4^7 6^2 8^2 10^2 | 4 | - | False |
| -1/96 | (0, 1/4, 7/96) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | aa6b0077c3234d24 | True |
| -1/192 | (0, 1/4, 5/64) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | aa6b0077c3234d24 | True |
| 0 | (0, 1/4, 1/12) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | aa6b0077c3234d24 | True |
| 1/192 | (0, 1/4, 17/192) | 2 | (30, 47, 19) | 3^4 4^5 5^6 6^2 10^2 | 4 | aa6b0077c3234d24 | True |
| 1/96 | (0, 1/4, 3/32) | 2 | (34, 53, 21) | 3^2 4^13 6^4 12^2 | 4 | - | False |
| 1/64 | (0, 1/4, 19/192) | 2 | (34, 53, 21) | 3^2 4^13 6^4 12^2 | 4 | - | False |
| 1/48 | (0, 1/4, 5/48) | 2 | (38, 59, 23) | 3^8 4^4 6^6 7^2 8^1 10^2 | 4 | - | False |
| 5/192 | (0, 1/4, 7/64) | 2 | (38, 59, 23) | 3^8 4^4 6^6 7^2 8^1 10^2 | 4 | - | False |
| 1/32 | (0, 1/4, 11/96) | 2 | (38, 59, 23) | 3^8 4^4 6^6 7^2 8^1 10^2 | 4 | - | False |
| 7/192 | (0, 1/4, 23/192) | 2 | (38, 59, 23) | 3^8 4^4 6^6 7^2 8^1 10^2 | 4 | - | False |
| 1/24 | (0, 1/4, 1/8) | 4 | (12, 22, 12) | 3^8 5^4 | 8 | 971596772f324b8e | False |


## C2 -- full isometry group of each solid (centre-free) and the honeycomb hands

Method: all aut map automorphisms enumerated from the canonical code; an automorphism is an isometry iff its vertex permutation preserves all pairwise squared distances (exact); the affine map is then solved, asserted orthogonal, det and site-fixing recorded. Honeycomb columns come from the banked g4 tables (det of each point operation in the lattice basis; the hand of a translation class is the det of any operation carrying class 0 to it, asserted consistent).

| cell | aut (reversing) | Isom | Isom+ | improper isometries | Isom fixing site | site sym | solid | ops (improper) | T | classes of the other hand |
|---|---|---|---|---|---|---|---|---|---|---|
| S | 4 (2) | 2 | 2 | 0 | 2 | 2 | chiral | 24 (12) | 12 | 6 |
| O | 1 (0) | 1 | 1 | 0 | 1 | 1 | chiral | 24 (12) | 24 | 12 |
| P11 | 2 (1) | 2 | 1 | 1 | 2 | 2 | achiral | 48 (24) | 24 | n/a (achiral solid) |
| P7 | 4 (2) | 1 | 1 | 0 | 1 | 1 | chiral | 48 (24) | 48 | 24 |
| H212 | 3 (0) | 3 | 3 | 0 | 3 | 3 | chiral | 24 (0) | 8 | 0 |
| H230 | 4 (2) | 2 | 2 | 0 | 2 | 2 | chiral | 48 (24) | 24 | 12 |
| H214 | 2 (0) | 2 | 2 | 0 | 2 | 2 | chiral | 24 (0) | 12 | 0 |

Findings: for every cell |Isom| equals the site-symmetry order and every isometry of the solid fixes its Voronoi site, so the about-site stabilizer certified in G4/V2 IS the full isometry group of the solid, and since the site-symmetry operations of G are isometries of the cell (V2 containment), Isom(cell) = site group of G. Consequence for the honeycomb: an isometry of the tiling carries the cell to some cell; composing with the element of G that carries it back gives an isometry of the solid, hence an element of G; so the full symmetry group of every honeycomb here is exactly G. Solids: P11 has one improper isometry (the site mirror) and is achiral; the other six have no improper isometry and are chiral as solids. In an achiral honeycomb (S, O, P7, H230) each improper operation carries the solid-chiral cell to its mirror image (a direct congruence would compose to an improper isometry of the cell), and the hand count above shows exactly half the translation classes of each hand. In the chiral honeycombs (H212, H214) every class has the same hand.

## C3 -- the Laves-graph cell (IT(214) I4_132, Wyckoff 8a, (1/8,1/8,1/8))

- exact chain: f = (30, 45, 17), p = 4^6 5^6 6^2 8^3, aut = 12, site symmetry order 6, orbit 8 per conventional cell, T = 4, non-simple vertices 0, cell volume 1728 (PERIOD 24)
- spglib 2.7.0 on the orbit: IT(214) I4_132, Wyckoff ['a'], site symmetry ['.32']
- canonical code id: 8c69db9e84095469; in phase1_types.json: YES
- stored entry: f (30, 45, 17), p 4^6 5^6 6^2 8^3, aut 12, first witness 199 I2_13 (1/8, 1/8, 1/8); sightings: 199 (1/8, 1/8, 1/8); 199 (1/8, 3/8, 5/8); 212 (1/8, 3/8, 5/8); 213 (1/8, 1/8, 1/8); 214 (1/8, 1/8, 1/8); 214 (1/8, 3/8, 5/8)
- collision screen (harness/SCHMITT_COLLISION_RESULTS.md P07-P09): this stored type was identified as SAME TYPE as Schmitt's printed (30,45,17) representative in IT(199), IT(212) and IT(214) (the 214 point being (1/8,1/8,1/8) itself), and eliminated from the candidate list.
- verdict: the sweep REDISCOVERED the Laves-graph plesiohedron (stored as 8c69db9e84095469, triage rank 5) and the collision screen correctly identified it as Schmitts printed cell; it has six pentagonal facets.

## C4 -- roundness under both conventions

| cell | site | site-centred rho^2 | MES centre | MES r^2 | centres coincide | roundness (site-centred) | roundness (MES) |
|---|---|---|---|---|---|---|---|
| Josehedron (control) | (0, 2, 3) | 23/3 | (0, 2, 3) | 23/3 | YES | 47.9833% | 47.9833% |
| S Satchelhedron | (0, 0, 3) | 51/4 | (0, 0, 3) | 51/4 | YES | 37.7554% | 37.7554% |
| O Ordenhedron | (3, 4, 10) | 125 | (57/16, 57/16, 69/8) | 12771/128 | NO | 9.8394% | 13.7979% |
| P11 Pn-3m 11-facet cell | (2, 9, 9) | 118 | (3, 9, 9) | 99 | NO | 10.7278% | 13.9599% |
| P7 Pn-3m 7-facet cell | (3, 4, 10) | 125 | (57/16, 57/16, 69/8) | 12771/128 | NO | 4.9197% | 6.8989% |
| H212 IT(212) (37,57,22) cell | (1, 1, 1) | 507/16 | (3/4, 3/4, 3/4) | 63/2 | NO | 28.9090% | 29.1675% |
| H230 IT(230) (40,61,23) cell | (2, 4, 3) | 44 | (9/10, 51/10, 3) | 3969/100 | NO | 23.5573% | 27.4968% |
| H214 IT(214) (30,47,19) cell | (0, 3, 1) | 115/4 | (0, 3, -3/10) | 19773/800 | NO | 11.1503% | 13.9885% |

Reading: where the centres coincide the two conventions give the same number; the Josehedron control coincides by symmetry (site symmetry -4 fixes only the site), so the control cannot discriminate the conventions. Cells whose MES is not site-centred get a strictly larger ratio under the MES convention; none reaches 47.98% under either.

## C5 -- Bernhard's Josehedron generating orbit: group and Wyckoff label

- spglib 2.7.0 on Bernhard's 12 integer points (mod 8): IT(220) I-43d, Wyckoff ['a'], site symmetry ['-4..'], origin shift [0.0, 0.0, 0.0]
- exact cell from those points: f (12, 22, 12), p 3^4 4^8, aut 4; code id dfccc9ff6019ead5 = stored seed 'josehedron'
- orbit of the point (0, 1/4, 3/8) under the frozen IT(220) operations: 12 points per conventional cell, site symmetry order 4, T = 6; its cell has code id dfccc9ff6019ead5 (SAME as Bernhard's cell), f (12, 22, 12), p 3^4 4^8
- point set identity: frozen-orbit points EQUAL Bernhard's points (after rescaling to PERIOD 24)
