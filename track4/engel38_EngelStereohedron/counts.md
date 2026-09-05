# Engel 38-facet stereohedron — polyform counts

Banked workflow: `export_tables.py` + compiled `enumerate` (the A398957 a-file program) on `g4_tables_engel38.json`; full ops -> fixed + free, proper ops -> one-sided (fixed column identical, asserted). Per-run cap 20 min. Full run: n<=6 completed in 169s. Proper run: n<=6 completed in 169s.

| n | fixed | free | one-sided | independent (verify_counts_independent.py) |
|---|---|---|---|---|
| 1 | 24 | 1 | 1 | MATCH (fixed/free/one-sided, Burnside ok) |
| 2 | 456 | 25 | 25 | MATCH (fixed/free/one-sided, Burnside ok) |
| 3 | 13384 | 559 | 559 | MATCH (fixed/free/one-sided, Burnside ok) |
| 4 | 477102 | 20051 | 20051 | MATCH (fixed/free/one-sided, Burnside ok) |
| 5 | 18876408 | 786517 | 786517 | MATCH (fixed/free/one-sided, Burnside ok) |
| 6 | 796541508 | 33195798 | 33195798 | not run |

Burnside identity |G|*free(n) = Sum Fix_g(n): banked burnside_generic.py ALL PASS for n <= 4 (G4/V3); the independent enumerator asserts it at every n <= 5 for both the full and the proper group.

Dual-implementation bar: MET for n <= 5; n = 6..6 rest on the single banked enumerator.
