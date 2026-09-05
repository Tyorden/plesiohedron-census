# the Pn-3m 7-facet cell — polyform counts (banked enumerator workflow)

Workflow: banked `export_tables.py` + the compiled `enumerate` binary (the A398957 a-file program) on the banked `g4_tables_f98a3ee5675fc121.json` (byte-copied here). Full-ops run gives fixed + free; proper-ops run gives fixed (identical column, asserted) + one-sided. n <= 4 prefixes asserted equal to the accepted G4 values (`harness/G4_RESULTS.md`). Per-shape extension cap 15 min.

| n | fixed | free | one-sided |
|---|---|---|---|
| 1 | 48 | 1 | 2 |
| 2 | 168 | 7 | 10 |
| 3 | 912 | 19 | 38 |
| 4 | 5748 | 135 | 254 |
| 5 | 39312 | 819 | 1638 |
| 6 | 283856 | 6012 | 11928 |

Full-ops run reached n <= 6; proper-ops run reached n <= 6.

Consistency checks (this build): fixed columns of the two runs identical at every common n; fixed >= one-sided >= free and one-sided <= 2*free at every n (achiral count 2*free - one-sided >= 0). Burnside identity: verified for n <= 4 in the accepted G4 run; EXTENDED in this build: banked burnside_generic.py (independent growth enumeration) verified |G|*free(n) = Sum Fix_g(n) with an independent fixed recount for ALL n <= 6.



**Update 2026-09-03:** the n<=6 fixed/one-sided/free values above were reproduced exactly by a second, independently written enumerator (publication/verify_counts_independent.py; INDEPENDENT_COUNTS_2026-09-03.md; main-session re-run exit 0). The dual-implementation bar is met for this shape.
