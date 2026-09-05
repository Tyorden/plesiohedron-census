# the IT(230) (40,61,23) cell — polyform counts (banked enumerator workflow)

Workflow: banked `export_tables.py` + the compiled `enumerate` binary (the A398957 a-file program) on the banked `g4_tables_359beee832567a71.json` (byte-copied here). Full-ops run gives fixed + free; proper-ops run gives fixed (identical column, asserted) + one-sided. n <= 4 prefixes asserted equal to the accepted G4 values (`harness/G4_RESULTS.md`). Per-shape extension cap 15 min.

| n | fixed | free | one-sided |
|---|---|---|---|
| 1 | 24 | 1 | 2 |
| 2 | 276 | 7 | 14 |
| 3 | 5096 | 112 | 224 |
| 4 | 111732 | 2349 | 4694 |
| 5 | 2695656 | 56280 | 112560 |
| 6 | 68781576 | 1433432 | 2866790 |

Full-ops run reached n <= 6; proper-ops run reached n <= 6.

Consistency checks (this build): fixed columns of the two runs identical at every common n; fixed >= one-sided >= free and one-sided <= 2*free at every n (achiral count 2*free - one-sided >= 0). Burnside identity: verified for n <= 4 in the accepted G4 run; an independent Burnside/growth verification at n = 5, 6 was NOT run in this build (counts at n = 5, 6 rest on the single banked enumerator; the fixed column is reproduced identically by the proper-ops run).

