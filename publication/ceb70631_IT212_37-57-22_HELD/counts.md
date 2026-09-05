# the IT(212) (37,57,22) cell — polyform counts (banked enumerator workflow)

Workflow: banked `export_tables.py` + the compiled `enumerate` binary (the A398957 a-file program) on the banked `g4_tables_ceb70631e274e727.json` (byte-copied here). Full-ops run gives fixed + free; proper-ops run gives fixed (identical column, asserted) + one-sided. n <= 4 prefixes asserted equal to the accepted G4 values (`harness/G4_RESULTS.md`). Per-shape extension cap 15 min.

| n | fixed | free | one-sided |
|---|---|---|---|
| 1 | 8 | 1 | 1 |
| 2 | 88 | 5 | 5 |
| 3 | 1384 | 59 | 59 |
| 4 | 25064 | 1065 | 1065 |
| 5 | 492672 | 20532 | 20532 |
| 6 | 10213156 | 425874 | 425874 |

Full-ops run reached n <= 6; proper-ops run reached n <= 6.

Consistency checks (this build): fixed columns of the two runs identical at every common n; fixed >= one-sided >= free and one-sided <= 2*free at every n (achiral count 2*free - one-sided >= 0). Burnside identity: verified for n <= 4 in the accepted G4 run; an independent Burnside/growth verification at n = 5, 6 was NOT run in this build (counts at n = 5, 6 rest on the single banked enumerator; the fixed column is reproduced identically by the proper-ops run).

