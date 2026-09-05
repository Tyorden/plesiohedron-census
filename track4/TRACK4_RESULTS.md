# Track-4 results — OEIS polyform sequences for two KNOWN cells (2026-09-03)

Scope (PROGRAM_PLAN Track 4): authored polyform sequences (fixed / one-sided /
free) for (A) the 17-facet Laves-graph plesiohedron and (B) Engel's 38-facet
stereohedron. **Neither cell is claimed as new** — both are established
literature objects; only the sequences are new. No snapshot/novelty language
is used in the drafts; attribution sentences replace it.

Scripts (all in `track4/`): `track4_certify.py` (V0 literature-anchored
derivation + the verbatim `harness/g4_certify.py` V1-V3 stages, imported not
copied + banked-enumerator counts; writes `track4_results.json`,
`TRACK4_CERT_LOG.md`, `g4_tables_<cid>.{json,txt,_proper.txt}`),
`build_track4_packages.py` (packages + OEIS drafts + a-files, every number read
from `track4_results.json` and asserted), `../publication/verify_counts_independent.py`
(dual-implementation check; logs + JSON in `independent_runs/`).

Re-run for acceptance (main session, exit 0 required):
```
cd <repo>/track4
python3 track4_certify.py          # both cells, ~20 min (Engel audit ~9 min, Engel n=6 enumerations ~7 min)
python3 build_track4_packages.py   # packages (asserts vs results + independent JSON)
python3 ../publication/verify_counts_independent.py g4_tables_laves17.json --n 6 --expect-fixed 4,34,416,6000,94740,1582610 --expect-free 1,4,22,278,4005,66346 --expect-onesided 1,4,22,278,4005,66346
python3 ../publication/verify_counts_independent.py g4_tables_engel38.json --n 5 --expect-fixed 24,456,13384,477102,18876408 --expect-free 1,25,559,20051,786517 --expect-onesided 1,25,559,20051,786517
```

## 1. Literature facts used (web-verified 2026-09-03, then confirmed by computation)

| fact | source | our check |
|---|---|---|
| Laves graph symmetry group is I4_132 | Wikipedia "Laves graph" (citing Kuz'min et al., Eur. Phys. J. Plus 135 (2020) 750, doi:10.1140/epjp/s13360-020-00722-z) | spglib 2.7.0 on the orbit of (1/8,1/8,1/8) under the frozen IT(214) coset list: IT 214 I4_132, Wyckoff **8a**, site symmetry **.32** (order 6) |
| Laves graph vertex set = integer points (0,0,0),(1,2,3),(2,3,1),(3,1,2),(2,2,2),(3,0,1),(0,1,3),(1,3,0) mod 4 | Wikipedia "Laves graph" | equals the MIRROR IMAGE of our 8a orbit translated by (1/8,1/8,1/8) and scaled by 4 (exact set comparison; the two enantiomorphs are the two settings of the chiral graph; `canon_code` identifies mirror images, so the combinatorial type is setting-independent) |
| Voronoi cells of the Laves graph are 17-faced plesiohedra | Wikipedia (citing Schoen, Notices AMS 55(6) (2008) 663; Baez, AMS Visual Insight 2016); Coxeter, Canad. J. Math. 7 (1955) 18-23, doi:10.4153/CJM-1955-003-7 for the graph | exact cell: **17 facets**, f=(30,45,17), p=4^6 5^6 6^2 8^3 |
| Schmitt 2016 IT(214) table lists f=(30,45,17) at (1/8,1/8,1/8) | `references/Schmitt_2016_dissertation.pdf` printed p.136 (banked in `harness/SCHMITT_COLLISION_RESULTS.md` P09) | same point, same f-vector; canonical code == Phase-1 store type `8c69db9e84095469` (already sighted at IT(214) (1/8,1/8,1/8) and five other (group, point) pairs) |
| Engel 1981 found four 38-facet Dirichlet stereohedra in I4_132; Schmitt 2016 confirms the four, finds no fifth | Engel, Z. Kristallogr. 154 (1981) 199-215, doi:10.1524/zkri.1981.154.3-4.199 (citation confirmed via Wikipedia "Plesiohedron"); Schmitt sec. 2.3 (`SCHMITT_PRIMARY_READ_2026-08-28.md`) | — |
| Schmitt's printed IT(214) representative for f=(70,106,38): (427/6984, 761/6984, 1421/6984), frequency 153 | printed p.138 = PDF p.143; **visual read of the rendered page** (`schmitt_p138-143.png`) and the pdftotext layer agree verbatim | exact cell: **38 facets**, f=(70,106,38); IT(214) is single-origin (no shift; `SCHMITT_COLLISION_RESULTS.md` convention) |

## 2. Facet reproduction (V0) — both cells match the literature; nothing forced

| cell | IT(214) point | orbit (conv/T) | site sym | f-vector | p-vector | aut | nonsimple vtx | float vs exact |
|---|---|---|---|---|---|---|---|---|
| Laves graph plesiohedron | (1/8, 1/8, 1/8), Wyckoff 8a | 8 / 4 | 6 (.32) | **(30, 45, 17)** = lit. 17 faces | 4^6 5^6 6^2 8^3 | 12 | 0 | agree (W=2) |
| Engel's 38-facet stereohedron | (427/6984, 761/6984, 1421/6984), general 48i | 48 / 24 | 1 | **(70, 106, 38)** = Schmitt/Engel | 3^12 4^11 5^6 6^5 8^1 16^1 20^1 28^1 | 1 | 2 | float flagged degenerate; exact decides, neighbor sets agree |

T = 24 for the Engel cell = Engel's "24 aspects" (Sabariego-Santos III, quoted
in the scout). Its canonical code is not in the Phase-1 store (general
position; the sweep sampled special positions). WHICH of Engel's four 38-facet
types Schmitt's printed representative realizes is NOT identified here (Engel
1981 not in hand; ILL optional per STATUS 2026-08-28).

## 3. Certificates (G4 ladder, `TRACK4_CERT_LOG.md`, all exact arithmetic)

| stage | Laves-17 | Engel-38 |
|---|---|---|
| V0 exact derivation vs literature | PASS (0.1 s) | PASS (1.3 s) |
| V1 tiling certificate (generator) | PASS: detL=6912, T=4, vol=1728, 68 facet slots paired 1:1, 2rho-ball D=23 disjointness | PASS: detL=170326685952 (=6984^3/2, the I-centering BCC lattice), T=24, vol=7096945248, 912 slots paired 1:1, ball D=6204 |
| V1 independent adapted audit | PASS (1.5 s) | PASS (524 s; 24 reps x 38 facets, supporting-plane scan) |
| V2 symmetry (ALL orthogonal maps) | PASS: site 6 = stab_geo 6, aut 12; Bravais group order 48 | PASS: site 1 = stab_geo 1 = aut 1; Bravais group order 48 |
| V3 tables + Burnside (banked burnside_generic, n<=4) | PASS: \|ops\|=24, all 24 proper (CHIRAL honeycomb) | PASS: \|ops\|=24, all 24 proper (CHIRAL honeycomb) |

Harness note (recorded, not hidden): `mint_tables.derive_lattice` scans
`range(-P,P+1)^3` and is infeasible at the Engel cell's PERIOD 6984 (~2.7e12
iterations; two runs were killed after ~15 min in that loop). `track4_certify.py`
substitutes `derive_lattice_cosets` (same contract; complete by the argument
that a lattice translation maps site 0 to a site, so only the n site deltas
mod P need testing) and self-checks it against the original on the two feasible
controls (Laves P=24: detL 6912; Josehedron P=8: detL 256 — same lattice both
ways). The harness `g4_certify.py` is NOT modified. The G4 soft budget was
raised for this run (the Engel audit alone exceeds the 40-min default's share);
enumerator caps are per run (20 min).

## 4. Counts (banked enumerator = the published A398957 program) vs independent

Both honeycombs are chiral (all 24 point ops proper), so one-sided == free at
every n (the proper-ops run reproduces the full-ops run exactly).

### Laves graph plesiohedron (T=4, 17 neighbors)

| n | fixed | free = one-sided | independent verifier |
|---|---|---|---|
| 1 | 4 | 1 | MATCH |
| 2 | 34 | 4 | MATCH |
| 3 | 416 | 22 | MATCH |
| 4 | 6000 | 278 | MATCH |
| 5 | 94740 | 4005 | MATCH |
| 6 | 1582610 | 66346 | MATCH |

Dual-implementation bar MET n<=6 (18/18 cells; Burnside asserted at every n
for both groups; 48 s). Enumerator wall: 1 s per run.

### Engel's 38-facet stereohedron (T=24, 38 neighbors)

| n | fixed | free = one-sided | independent verifier |
|---|---|---|---|
| 1 | 24 | 1 | MATCH |
| 2 | 456 | 25 | MATCH |
| 3 | 13384 | 559 | MATCH |
| 4 | 477102 | 20051 | MATCH |
| 5 | 18876408 | 786517 | MATCH (366 s) |
| 6 | 796541508 | 33195798 | NOT RUN — infeasible for the pure-Python verifier (8e8 fixed forms held in memory) |

Dual-implementation bar MET n<=5 (15/15 cells, Burnside at every n). n=6
completed in ~205 s per run (full and proper, identical fixed column and
identical free column) — that term rests on the single banked enumerator.
Tasking asked for n<=4 or 5 under a 20-min per-n cap; n<=6 completed.

## 5. Draft inventory (`track4/<pkg>/`)

| package | files | DATA depth |
|---|---|---|
| `laves17_LavesGraphPlesiohedron/` | COORDS.md, counts.md, render.png, g4_tables_laves17.{json,txt,_proper.txt}, oeis_afile.txt, oeis_draft_{fixed,onesided,free}.txt | n<=6 (all dual-verified) |
| `engel38_EngelStereohedron/` | same set for `engel38` | n<=6 (n<=5 dual-verified; n=6 single-implementation, flagged in the draft NOTE — Tyler decides whether to submit n<=5 or n<=6) |

Draft format: house format of `publication/*/oeis_draft_*.txt` — NAME lines use
the literature names ("the Laves graph plesiohedron", "Engel's 38-facet
stereohedron"); COMMENTS carry the definition (space group, Wyckoff/point,
T, neighbors), an attribution sentence ("not new; only the sequences are
new"), the chirality note (one-sided == free), the certificate sentence, and
the AI-disclosure sentence ending in ` - ~~~~`; LINKS carry Coxeter 1955 /
Schoen 2008 / Wikipedia / Schmitt 2016 (Laves) and Engel 1981 / Schmitt 2016 /
Wikipedia (Engel); a-files carry both tables blocks + run instructions.
Because one-sided == free for both cells, the pre-submission NOTE recommends
ONE entry with both interpretations rather than a duplicate sequence (so each
cell yields 2 distinct sequences, not 3). DRAFTS ONLY — Tyler sequences
submissions (`publication/OEIS_DRAFTS_NOTE.md` slot discipline).

## 6. Honest gaps

- Engel n=6 term: single banked enumerator only (see §4). Either trim DATA to
  n<=5 or accept the term on the strength of the published program + the
  identical proper-ops rerun (same binary — not independent).
- Which of Engel's four 38-facet types this is: not identified (Engel 1981 not
  in hand). The draft says so. If the ILL returns, compare Schmitt's Fig. 2.3
  / Engel's Abb. 3 types by p-vector.
- The Wikipedia Laves-graph vertex set is the mirror of the frozen-setting 8a
  orbit; the sequences are setting-independent (mirror-invariant counts), so
  no action, but the a-file tables are for the frozen setting.
- `derive_lattice_cosets` is new code in the certificate path (self-checked on
  two controls, argument stated in its docstring); the main session's re-run
  should read it.
- Engel's float sweep flagged a degenerate vertex (2 non-simple vertices in the
  exact cell): a grid point's cell can carry accidental 4-plane vertices; the
  exact clip decides, and the V1 audit re-derived all 38 facets independently.
- Not done: b-files (not needed at this depth), OEIS existence search on the
  terms (pre-submission step), roundness (not asked).
