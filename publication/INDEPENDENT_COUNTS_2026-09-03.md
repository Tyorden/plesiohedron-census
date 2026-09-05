# Independent polyform-count verification — 2026-09-03

Closes the gap noted in each package's `counts.md`: the n = 5..6 fixed /
one-sided / free counts for the four publishable-now cells had been produced
by a single implementation (banked `export_tables.py` + compiled `enumerate`,
the A398957 a-file program). This document records a second, independently
written enumerator reproducing every banked value at n <= 6 for all four
shapes, after first reproducing the Josehedron banked record exactly as its
correctness certificate (the "dual-implementation bar" met by the Josehedron
OEIS work).

Verdict: CONTROL MATCH (18/18 cells) and ALL FOUR SHAPES MATCH (72/72 cells).
No mismatch, no table problem, no Burnside failure. Nothing was adjusted
toward agreement; the expected values were passed in only as post-hoc labels.

## Program

`publication/verify_counts_independent.py` (sha256
`33f55a6b1adbcb8175e12374df365a34962e62f6d65d385ffd12f5dd7d14479d`),
pure Python 3 standard library (no numpy), multiprocessing over 14 workers.
Written 2026-09-03 from the table schema alone; shares no code with the banked
`export_tables.py` / `enumerate` binary, with `harness/mint_tables.py` (read
only to confirm the op action convention), or with the Josehedron
`scripts/reference_enum.py` (read for the precedent; different algorithm, see
below).

Table semantics used (from the `g4_tables_*.json` schema):
- `T` translation types; a cell is `(v, t)` with `v` an integer lattice vector.
- `nbr[t]` = list of `[delta, t']`: cell `(v, t)` is adjacent to `(v+delta, t')`.
- `ops` / `proper_ops` = coset representatives of the honeycomb symmetry group
  modulo lattice translations, each `{A, map}` acting as
  `(v, t) -> (A . v + c_t, t')` with `map[t] = [c_t, t']`, `A` a 3x3
  unimodular integer matrix on column vectors.

Method (deliberately different route from the precedent, which grows free
forms directly under a full-ops canonical form):
1. FIXED forms: connected n-cell sets grown level by level from every cell of
   every (n-1)-cell parent, canonicalized under lattice translation only
   (translate the lexicographically least `(x,y,z,t)` cell to the origin,
   sort), deduplicated as packed integers. No symmetry op is consulted, so the
   fixed column checks the `nbr` semantics with no dependence on `ops`.
2. FREE / ONE-SIDED forms: quotient of the fixed set by `ops` (free) and by
   `proper_ops` (one-sided). A fixed form is counted iff it is the
   lexicographic minimum of its own orbit (orbit-representative count).
3. Internal cross-check at every n and both groups: the Burnside identity
   `|G| * orbits == sum over g of |Fix(g)|`, evaluated from the same op images,
   is asserted. (This would expose a non-closed or mis-read op set.)
4. Table sanity before enumeration: adjacency symmetric; every op unimodular;
   proper ops have det +1 and lie in `ops`; every op is an automorphism of the
   adjacency structure (checked for every (op, type) pair). All tables passed.

Encoding bounds: 6-bit coordinate fields (range [-32, 31]) and 6-bit type
field; with max |delta| <= 2 and n <= 6 all normalized coordinates lie within
+-10, asserted in the sanity step. Op images are computed unpacked (no
overflow possible) and packed only after translation normalization.

Determinism: all outputs are set cardinalities; chunking order cannot change
them. Exact integers throughout.

## Control: Josehedron (correctness certificate)

Tables: `paper_prep/SCI_OEIS_josehedron/data/josehedron_tables.json`
(sha256 `cc02ecd94ef9d294167450e5bbdc476903488099c119ad53ed18f112d457ec66`),
T = 6, 12 neighbours/type, |ops| = 24, |proper| = 12.
Banked record: free 1,2,15,131,1360,15133 / fixed 6,36,308,3030,32262,362010 /
one-sided 1,4,30,261,2717,30265.

| n | fixed (banked) | fixed (this) | one-sided (banked) | one-sided (this) | free (banked) | free (this) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 1 | 1 | 1 | 1 | MATCH / MATCH / MATCH |
| 2 | 36 | 36 | 4 | 4 | 2 | 2 | MATCH / MATCH / MATCH |
| 3 | 308 | 308 | 30 | 30 | 15 | 15 | MATCH / MATCH / MATCH |
| 4 | 3030 | 3030 | 261 | 261 | 131 | 131 | MATCH / MATCH / MATCH |
| 5 | 32262 | 32262 | 2717 | 2717 | 1360 | 1360 | MATCH / MATCH / MATCH |
| 6 | 362010 | 362010 | 30265 | 30265 | 15133 | 15133 | MATCH / MATCH / MATCH |

Burnside identity held at every n for both groups. Wall 6.8 s.
CONTROL VERDICT: EXACT MATCH, 18/18 cells. Gate passed before any new shape
was run.

## Satchelhedron (8cf50403)

Tables: `8cf50403_Satchelhedron/g4_tables_8cf50403cf88c455.json`
(sha256 `7178dfe471c5fb170fb3c89c438640accb55f8a65dc2165f003782775500ddef`),
T = 12, 11 neighbours/type, max |delta| = 2, |ops| = 24, |proper| = 12.

| n | fixed (banked) | fixed (this) | one-sided (banked) | one-sided (this) | free (banked) | free (this) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 12 | 12 | 2 | 2 | 1 | 1 | MATCH / MATCH / MATCH |
| 2 | 66 | 66 | 7 | 7 | 4 | 4 | MATCH / MATCH / MATCH |
| 3 | 524 | 524 | 50 | 50 | 25 | 25 | MATCH / MATCH / MATCH |
| 4 | 4866 | 4866 | 417 | 417 | 209 | 209 | MATCH / MATCH / MATCH |
| 5 | 49152 | 49152 | 4140 | 4140 | 2070 | 2070 | MATCH / MATCH / MATCH |
| 6 | 523626 | 523626 | 43759 | 43759 | 21882 | 21882 | MATCH / MATCH / MATCH |

Burnside identity held at every n for both groups. Reached n = 6. Wall 9.3 s.

## Ordenhedron (2de0a211)

Tables: `2de0a211_Ordenhedron/g4_tables_2de0a21129cabe90.json`
(sha256 `5466275db3e4286fe23f6a176c926715ec5f2d7ab881ba1085bd074473185d3d`),
T = 24, 15 neighbours/type, max |delta| = 1, |ops| = 24, |proper| = 12.

| n | fixed (banked) | fixed (this) | one-sided (banked) | one-sided (this) | free (banked) | free (this) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 24 | 24 | 2 | 2 | 1 | 1 | MATCH / MATCH / MATCH |
| 2 | 180 | 180 | 18 | 18 | 9 | 9 | MATCH / MATCH / MATCH |
| 3 | 1992 | 1992 | 170 | 170 | 85 | 85 | MATCH / MATCH / MATCH |
| 4 | 25974 | 25974 | 2196 | 2196 | 1099 | 1099 | MATCH / MATCH / MATCH |
| 5 | 371136 | 371136 | 30928 | 30928 | 15464 | 15464 | MATCH / MATCH / MATCH |
| 6 | 5619868 | 5619868 | 468793 | 468793 | 234420 | 234420 | MATCH / MATCH / MATCH |

Burnside identity held at every n for both groups. Reached n = 6. Wall 85.5 s.
Note: this is the shape whose `counts.md` said no independent Burnside/growth
verification had been run at n = 5, 6; that gap is now closed by this run
(independent growth AND the Burnside identity, both at n = 5 and 6).

## Pn-3m 11-facet cell (c4ea3f32)

Tables: `c4ea3f32_Pn3m_11facet/g4_tables_c4ea3f32fdd6dc51.json`
(sha256 `8148cb20df9af3f8d9e195bb6915cded446a900493f552633768fe2c9a28b96a`),
T = 24, 11 neighbours/type, max |delta| = 1, |ops| = 48, |proper| = 24.

| n | fixed (banked) | fixed (this) | one-sided (banked) | one-sided (this) | free (banked) | free (this) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 24 | 24 | 1 | 1 | 1 | 1 | MATCH / MATCH / MATCH |
| 2 | 132 | 132 | 9 | 9 | 6 | 6 | MATCH / MATCH / MATCH |
| 3 | 1048 | 1048 | 45 | 45 | 25 | 25 | MATCH / MATCH / MATCH |
| 4 | 9630 | 9630 | 427 | 427 | 225 | 225 | MATCH / MATCH / MATCH |
| 5 | 96240 | 96240 | 4010 | 4010 | 2027 | 2027 | MATCH / MATCH / MATCH |
| 6 | 1016472 | 1016472 | 42607 | 42607 | 21408 | 21408 | MATCH / MATCH / MATCH |

Burnside identity held at every n for both groups. Reached n = 6. Wall 31.3 s.

## Pn-3m 7-facet cell (f98a3ee5)

Tables: `f98a3ee5_Pn3m_7facet/g4_tables_f98a3ee5675fc121.json`
(sha256 `9a62d8dc23a16d78c2f2d0215ab69d322943da7c9e86fb5d5b1619926502f1ac`),
T = 48, 7 neighbours/type, max |delta| = 1, |ops| = 48, |proper| = 24.

| n | fixed (banked) | fixed (this) | one-sided (banked) | one-sided (this) | free (banked) | free (this) | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 48 | 48 | 2 | 2 | 1 | 1 | MATCH / MATCH / MATCH |
| 2 | 168 | 168 | 10 | 10 | 7 | 7 | MATCH / MATCH / MATCH |
| 3 | 912 | 912 | 38 | 38 | 19 | 19 | MATCH / MATCH / MATCH |
| 4 | 5748 | 5748 | 254 | 254 | 135 | 135 | MATCH / MATCH / MATCH |
| 5 | 39312 | 39312 | 1638 | 1638 | 819 | 819 | MATCH / MATCH / MATCH |
| 6 | 283856 | 283856 | 11928 | 11928 | 6012 | 6012 | MATCH / MATCH / MATCH |

Burnside identity held at every n for both groups. Reached n = 6. Wall 10.6 s.

## Runtime and environment

Python 3.13.1, macOS (Darwin 25.5.0), 16 cores, 14 worker processes.
Per-shape wall: control 6.8 s; Satchelhedron 9.3 s; Pn-3m 7-facet 10.6 s;
Pn-3m 11-facet 31.3 s; Ordenhedron 85.5 s. Every shape reached n = 6, far
inside the 30 min per-shape cap. Raw logs and machine-readable results
(`--json`) are in `publication/independent_runs/` (one `.log` + `.json` per
run; each JSON carries the absolute table path, per-n counts, Burnside sums,
timings, and `ok`).

## Scope and limits

- Verified: n <= 6 for the four publishable-now cells; the three HELD cells
  (359beee8, aa6b0077, ceb70631) were not run (not in scope of this gap).
- What this does NOT check: that the `g4_tables_*.json` tables are the
  correct tables for the geometric cells (that is the G4 certification's job,
  `harness/G4_RESULTS.md` / `harness/MINT_TABLES_RESULT.md`). This document
  certifies only that, GIVEN those tables, the banked counts are what an
  independent enumeration of the tables produces.
- Sharing: the two implementations consume the same table files; a defect in
  a table would be common-mode. The op-automorphism and adjacency-symmetry
  checks here are partial guards against a corrupted table, not a substitute
  for the geometric certification.

## Re-run (main session, before acceptance)

From `paper_prep/MINT_plesiohedron/publication/`:

```
python3 verify_counts_independent.py ../../SCI_OEIS_josehedron/data/josehedron_tables.json --n 6 --expect-fixed 6,36,308,3030,32262,362010 --expect-free 1,2,15,131,1360,15133 --expect-onesided 1,4,30,261,2717,30265
python3 verify_counts_independent.py 8cf50403_Satchelhedron/g4_tables_8cf50403cf88c455.json --n 6 --expect-fixed 12,66,524,4866,49152,523626 --expect-free 1,4,25,209,2070,21882 --expect-onesided 2,7,50,417,4140,43759
python3 verify_counts_independent.py f98a3ee5_Pn3m_7facet/g4_tables_f98a3ee5675fc121.json --n 6 --expect-fixed 48,168,912,5748,39312,283856 --expect-free 1,7,19,135,819,6012 --expect-onesided 2,10,38,254,1638,11928
python3 verify_counts_independent.py c4ea3f32_Pn3m_11facet/g4_tables_c4ea3f32fdd6dc51.json --n 6 --expect-fixed 24,132,1048,9630,96240,1016472 --expect-free 1,6,25,225,2027,21408 --expect-onesided 1,9,45,427,4010,42607
python3 verify_counts_independent.py 2de0a211_Ordenhedron/g4_tables_2de0a21129cabe90.json --n 6 --expect-fixed 24,180,1992,25974,371136,5619868 --expect-free 1,9,85,1099,15464,234420 --expect-onesided 2,18,170,2196,30928,468793
```

Each command exits 0 iff every cell matches and every Burnside identity holds;
any nonzero exit is a finding to report, not to fix toward agreement.

AI disclosure: program and this document written by Claude (Fable 5.1) in a
Claude Code session on 2026-09-03 as an independent-verifier task; the counts
are machine results, not AI-generated numbers. Status: awaiting main-session
re-run for acceptance.
