# Laves graph plesiohedron — polyform counts

Banked workflow: `export_tables.py` + compiled `enumerate` (the A398957 a-file program) on `g4_tables_laves17.json`; full ops -> fixed + free, proper ops -> one-sided (fixed column identical, asserted). Per-run cap 20 min. Full run: n<=6 completed in 0s. Proper run: n<=6 completed in 0s.

| n | fixed | free | one-sided | independent (verify_counts_independent.py) |
|---|---|---|---|---|
| 1 | 4 | 1 | 1 | MATCH (fixed/free/one-sided, Burnside ok) |
| 2 | 34 | 4 | 4 | MATCH (fixed/free/one-sided, Burnside ok) |
| 3 | 416 | 22 | 22 | MATCH (fixed/free/one-sided, Burnside ok) |
| 4 | 6000 | 278 | 278 | MATCH (fixed/free/one-sided, Burnside ok) |
| 5 | 94740 | 4005 | 4005 | MATCH (fixed/free/one-sided, Burnside ok) |
| 6 | 1582610 | 66346 | 66346 | MATCH (fixed/free/one-sided, Burnside ok) |

Burnside identity |G|*free(n) = Sum Fix_g(n): banked burnside_generic.py ALL PASS for n <= 4 (G4/V3); the independent enumerator asserts it at every n <= 6 for both the full and the proper group.

Dual-implementation bar: MET for n <= 6.
