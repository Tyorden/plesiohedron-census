# Ordenhedron — polyform counts (banked enumerator workflow)

Workflow: banked `export_tables.py` + the compiled `enumerate` binary (the A398957 a-file program) on the banked `g4_tables_2de0a21129cabe90.json` (byte-copied here). Full-ops run gives fixed + free; proper-ops run gives fixed (identical column, asserted) + one-sided. n <= 4 prefixes asserted equal to the accepted G4 values (`harness/G4_RESULTS.md`). Per-shape extension cap 15 min.

| n | fixed | free | one-sided |
|---|---|---|---|
| 1 | 24 | 1 | 2 |
| 2 | 180 | 9 | 18 |
| 3 | 1992 | 85 | 170 |
| 4 | 25974 | 1099 | 2196 |
| 5 | 371136 | 15464 | 30928 |
| 6 | 5619868 | 234420 | 468793 |

Full-ops run reached n <= 6; proper-ops run reached n <= 6.

Consistency checks (this build): fixed columns of the two runs identical at every common n; fixed >= one-sided >= free and one-sided <= 2*free at every n (achiral count 2*free - one-sided >= 0). Burnside identity: verified for n <= 4 in the accepted G4 run; an independent Burnside/growth verification at n = 5, 6 was NOT run in this build (counts at n = 5, 6 rest on the single banked enumerator; the fixed column is reproduced identically by the proper-ops run).



**Update 2026-09-03:** the n<=6 fixed/one-sided/free values above were reproduced exactly by a second, independently written enumerator (publication/verify_counts_independent.py; INDEPENDENT_COUNTS_2026-09-03.md; main-session re-run exit 0). The dual-implementation bar is met for this shape.
