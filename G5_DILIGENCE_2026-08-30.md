# G5 novelty diligence — 11 G4-certified candidates (2026-08-30)

Gate: `ANCHORS.md` G5 (BLOCKING for any public claim). **Language rule applied
throughout: every verdict below is "not matched against the catalog snapshot of
2026-08-30"; the phrase "new to science" appears nowhere and must not.** G5 is
evidence accumulation, not proof of novelty: Schmitt's survey is a grid sampling
with one printed representative per (group, f-vector); Bernhard prints face
counts, not full combinatorics; absence is evidence, never proof (the standing
structural caveat).

Auditor: G5 diligence agent. Inputs: `harness/TRIAGE_RESULT.md`,
`harness/G4_RESULTS.md`, `harness/SCHMITT_COLLISION_RESULTS.md`,
`references/Schmitt_2016_dissertation.pdf`,
`references/Bernhard_2026_josehedron_arxiv2604.07160.pdf`, web sources cited
inline. New artifacts: `harness/rekey_tables.json`, `harness/g5_rekey_check.py`
(gate, exit 0, deterministic — main-session re-run required for acceptance).

## The 11 candidates

| # | id | group | f-vector | p-vector | aut |
|---|---|---|---|---|---|
| 1 | `ceb70631e274e727` | 212 P4_332 | (37,57,22) | 3^6 4^6 5^6 10^3 12^1 | 3 |
| 2 | `359beee832567a71` | 230 Ia-3d | (40,61,23) | 4^20 11^2 20^1 | 4 |
| 3 | `8cf50403cf88c455` | 220 I-43d | (16,25,11) | 3^2 4^1 5^8 | 4 |
| 4 | `c314dedd38208a2e` | 212 P4_332 | (30,46,18) | 3^4 4^2 5^8 7^2 9^2 | 2 |
| 5 | `aa6b0077c3234d24` | 214 I4_132 | (30,47,19) | 3^4 4^5 5^6 6^2 10^2 | 2 |
| 6 | `f3d0f39a0b9676b9` | 214 I4_132 | (10,17,9) | 3^4 4^3 5^2 | 2 |
| 7 | `2de0a21129cabe90` | 201 Pn-3 | (20,33,15) | 3^6 4^3 5^2 6^2 7^2 | 1 |
| 8 | `c4ea3f32fdd6dc51` | 224 Pn-3m | (14,23,11) | 3^4 4^4 6^3 | 2 |
| 9 | `9b69eefb8bd8437c` | 224 Pn-3m | (11,18,9) | 3^2 4^5 5^2 | 2 |
| 10 | `d2d935e5499e6e11` | 224 Pn-3m | (6,11,7) | 3^6 4^1 | 4 |
| 11 | `f98a3ee5675fc121` | 224 Pn-3m | (10,15,7) | 3^2 4^3 6^2 | 4 |

## Duty 1 — independent re-key of the Schmitt digitization: CLEAN

Method. The complete printed f-vector tables (Schmitt 2016 Sec. 2.2.5) for the
six distinct groups hosting the 11 candidates — IT(201) printed p.124 (PDF 129),
IT(212)/IT(213) shared table pp.133-135 (PDF 138-140), IT(214) pp.136-138 (PDF
141-143), IT(220) pp.141-143 (PDF 146-148), IT(224) p.145 (PDF 150), IT(230)
pp.149-150 (PDF 154-155) — were transcribed FRESH from visual reads of the
rendered PDF pages into `harness/rekey_tables.json` (f-vectors AND frequencies,
printed order) WITHOUT consulting `triage_phase1.py`'s digitization, which was
opened only afterwards for the diff. Provenance disclosure (in the JSON `_meta`
too): the re-keyer had previously read STATUS/TRIAGE aggregate claims (881 total
rows; 220 contains (12,22,12); the 224 table has 8 f-vectors; the per-candidate
P/A flags) but not one row of the row-level digitization.

Three-way check (`harness/g5_rekey_check.py`, exit 0, byte-identical across
re-runs):

- (A) visual re-key vs (B) PDF text layer (`pdftotext -layout`, parsed
  programmatically — a different extraction modality of the same printed
  source): **IDENTICAL on all 386 rows of all six tables, f-vectors AND
  frequencies, full sequences.**
- (A) visual re-key vs (C) `SCHMITT_FVECTORS` in `triage_phase1.py`: **IDENTICAL
  as ordered sequences for all six groups** — 201: 16 rows, 212/213: 105, 214:
  102, 220: 62, 224: 8, 230: 93 (= 386 of the 881 digitized rows; the 213 alias
  to 212 verified).

**Verdict: 0 discrepancies. No third read was needed anywhere.** The
single-pass-transcription caveat on the triage digitization is hereby CLOSED for
these six groups (the other 30 cubic groups remain single-pass, Euler- and
remark-checked only).

Candidate P/A flags re-verified against the re-key: PRESENT for #1 (37,57,22) in
212/213, #2 (40,61,23) in 230, #4 (30,46,18) in 212/213, #5 (30,47,19) in 214;
ABSENT from every sighted group's printed table for #3 (16,25,11) in 220, #6
(10,17,9) in 214, #7 (20,33,15) in 201, and #8-#11 in 224. All 11 flags match
TRIAGE_RESULT.md. For #1/#2/#4/#5 the type-level question at the sighted-group
printed representatives was already resolved DIFFERENT-TYPE by the accepted
collision screen (`SCHMITT_COLLISION_RESULTS.md`).

Incidental confirmations from the visual reads: IT(214) max printed f2 = 38
(rows end (70,106,38)) matching Engel's I4_132 record; IT(220) contains
(12,22,12) at (143/1746, 289/3492, 295/3492) freq 46 exactly as banked in
SCHMITT_220_CHECK_RESULT.md; IT(224)'s printed table is exactly 8 rows.

### NEW: cross-group scan of candidate f-vectors (all 36 digitized tables)

The triage "ABSENT-all" flag is scoped to SIGHTED groups. Scanning each
candidate f-vector across all 36 digitized cubic tables:

| # | f-vector | printed in groups (whole cubic survey) |
|---|---|---|
| 1 | (37,57,22) | 199, 212/213, 214, 230 |
| 2 | (40,61,23) | 206, 212/213, 214, 220, 230 |
| 3 | (16,25,11) | **NONE — absent from the entire printed cubic survey** |
| 4 | (30,46,18) | 198, 206, 212/213, 214, 220, 230 |
| 5 | (30,47,19) | 199, 206, 212/213, 214, 230 |
| 6 | (10,17,9) | 197, 199, 211, 212/213, 217, 218, 230 |
| 7 | (20,33,15) | 197, 206, 208, 210, 212/213, 214, 218, 220, 230 |
| 8 | (14,23,11) | 197, 208, 212/213, 217, 218, 222, 230 |
| 9 | (11,18,9) | 208 |
| 10 | (6,11,7) | 195, 200, 202, 204, 208, 228 |
| 11 | (10,15,7) | 203, 204, 210, 211, 217, 222, 223, 227, 229 |

Consequence: only #3 `8cf50403cf88c455` (the 5^8-pentagon 11-hedron) has an
f-vector unseen anywhere in Schmitt's printed cubic tables. For the other ten,
a cell with the same f-vector exists somewhere in his survey, in OTHER groups —
and a same-type coincidence across groups is not excluded by anything run so
far (the collision screen covered sighted-group pairs only). The same honeycomb
type can genuinely recur across groups (e.g. stored type `36ea4b551873828d`
(6,11,7) p=3^6 4^1 in 200/202 vs candidate #10, SAME f AND p, different
canonical code — proving p-vector agreement wouldn't settle it either; the
canonical code at his representative points is the bar). This defines the
concrete remaining type-closure queue: ~60 cross-group (group, f-vector)
representative points to push through the `schmitt_collision_check.py` pattern
(each ran 0.1-60s in the accepted screen). Caveat: cross-group rows in the 30
non-re-keyed tables rest on the single-pass digitization.

## Duty 2 — Bernhard diff (Table 1 + Fig 12 / Sec 7.3): all 11 NO-MATCH on printed data

Everything Bernhard prints about his cells (Table 1, p.3; main text; Sec 7.3 /
Fig 12, p.17 — seven line drawings (a)-(g), no numeric tables in the appendix
for them):

| Bernhard cell | printed data |
|---|---|
| Josehedron (FKS min; max = mirror) | 12 F = 4 triangles + 8 quadrilaterals; f=(12,22,12) — our seeded/G0 shape, IT(220) 12a |
| FKS both (Fig 6) | "14 faces and 16 vertices" => f=(16,28,14) by Euler |
| Gyroid min | 17 F, Voronoi cell of the Laves graph (classical, see Duty 3) |
| Gyroid both (Fig 12a) | new type, 17 F, two parallel regular hexagons |
| Double Gyroid both (Fig 12b) | new type, 20 F, two big parallel faces |
| FRP both (Fig 12c) | new type, 20 F |
| Lidinoid max (Fig 12d) | new type, 14 F, 2 truncated pyramids with chamfered edges |
| Lidinoid both | "various new types, (to be verified...)" — NO counts printed |
| Split-P max (Fig 12e) | new type, 17 F, truncated hexagonal pyramid with chamfered edges |
| Split-P both (Fig 12f) | 2 types, 17 F and 20 F |
| KP both (Fig 12g) | 2 types, "single side truncated flat octahedron + capsule with rhombic tips" — NO counts printed |
| IWP min | 12 F = 4 squares + 8 isosceles triangles ("cube with pyramids") |
| others (classical) | cube, truncated octahedron, rhombic dodecahedron, triakis truncated tetrahedron, flat octahedra, square pyramid, chamfered cubes + octahedra (DP both), Octo both incl. a 14 F polyhedron |

His own epistemic status for the Fig 12 shapes (Sec 7.3, quoted): "It remains an
assumption for now that the polyhedra shown in Fig. 12 are unique... a study as
profound as for the Josehedron... has not yet been conducted... statistically
significant similarity in face count and volume is used as a first indicator."
So even his strongest appendix data IS the face count.

Comparison: Bernhard's printed face counts are {5, 8, 12, 14, 17, 20} (+
classical cells). The 11 candidates' facet counts are {7, 9, 11, 15, 18, 19,
22, 23}. **The intersection is EMPTY: every candidate is NO-MATCH against every
Bernhard cell with printed data — no POSSIBLE-BERNHARD-MATCH flags raised.**
Two Bernhard entries are UNDECIDABLE-FROM-PAPER (KP both: 2 types, no counts;
Lidinoid both: unspecified "various new types"): no candidate can be cleared or
matched against those from the paper alone. Qualitatively, Fig 12g's two KP
cells (a once-truncated flat octahedron and a rhombic-tipped "capsule") resemble
none of the 11 (none of ours is a truncated bipyramid or a rhombic-tipped
prism), but that is a drawing-level judgment, not data. If any candidate ever
needed clearing against those two entries specifically, the paper is
insufficient and the check would need his meshes (author contact) or a
recomputation of the KP/Lidinoid extremal-point Voronoi cells from the printed
TPMS formulae (Table 6/7 — which the paper does print, making that recomputation
fully specified).

Note: Bernhard's shapes live at TPMS extremal points (FKS/Gyroid territory =
the 214/220 corridor), so the group overlap with our candidates is real; the
face-count separation is therefore a meaningful negative, not an apples-oranges
one.

## Duty 3 — classical named space-fillers diff: all 11 NO-MATCH

Classical list (LANDSCAPE_SCOUT + standard), with verified f-vectors and
sources:

| classical cell | f-vector | face types | source |
|---|---|---|---|
| cube | (8,12,6) | 4^6 | seeded catalog (G2, published integer vertices) |
| hexagonal prism | (12,18,8) | 4^6 6^2 | seeded catalog (G2) |
| rhombic dodecahedron | (14,24,12) | 4^12 | seeded catalog (G2) |
| elongated dodecahedron | (18,28,12) | 4^8 6^4 | seeded catalog (G2, Fedorov) |
| truncated octahedron | (24,36,14) | 4^6 6^8 | seeded catalog (G2) |
| triakis truncated tetrahedron | **(16,30,16)** | 3^12 6^4 | en.wikipedia.org/wiki/Triakis_truncated_tetrahedron (fetched 2026-08-30): 16 faces (4 hexagons + 12 isosceles triangles), 30 edges, 16 vertices; diamond-lattice Voronoi cell |
| sphenoid hendecahedron | (11,20,11) | 3^4 4^7 (2 triangle sizes; 3 kite sizes + 1 rhombus) | steelpillow.com/polyhedra/five_sf/five.html (Inchbald, "Five Space-Filling Polyhedra", Math. Gaz. 80 (1996) 466-475; fetched 2026-08-30): 11 faces, 11 vertices => E=20 by Euler |
| bisymmetric hendecahedron | (11,20,11) | 3^4 4^7 (4 triangles, 4 kites, 3 rhombi) | same source; 11 faces, 11 vertices |
| gyrobifastigium | (8,14,8) | 3^4 4^4 | en.wikipedia.org/wiki/Gyrobifastigium (fetched 2026-08-30) |
| trapezo-rhombic dodecahedron | (14,24,12) | 6 rhombi + 6 trapezoids (4^12) | en.wikipedia.org/wiki/Trapezo-rhombic_dodecahedron (fetched 2026-08-30); HCP Voronoi cell |
| 17-face Laves-graph cell | F=17 (V,E not stated) | not stated | en.wikipedia.org/wiki/Laves_graph (fetched 2026-08-30): "heptadecahedra with 17 faces each", plesiohedra |

CORRECTION to the tasking note: the triakis truncated tetrahedron is
(16,30,16), NOT the queried "(16,28,14)?" — verified above. Consistency bonus:
(16,30,16) with p=3^12 6^4 is exactly stored type `2001fe7ea92fd0ad` (the
top-10 rank 6 killed by the collision screen as Schmitt's printed cell in
203/210/212/227) — i.e. the pipeline independently found the diamond Voronoi
cell and the screen correctly identified it as known; it is NOT one of the 11.

Comparison: classical facet counts {6, 8, 8, 11, 12, 12, 12, 14, 16, 17} vs
candidate facet counts {7, 9, 11, 15, 18, 19, 22, 23}. The only overlap is
F=11, and both classical 11-hedra are f=(11,20,11) with p=3^4 4^7, while our
F=11 candidates are #3 (16,25,11) p=3^2 4^1 5^8 (eight pentagons — no classical
cell has pentagons) and #8 (14,23,11) p=3^4 4^4 6^3: **different f-vectors AND
different face-type multisets. No f-vector collision exists between any of the
11 candidates and any classical cell**, so no type-level check is required on
this leg. (Had one collided, the type-level check would need published vertex
data for the classical cell through `canon_code`, the seeded-catalog pattern.)
The Laves cell's unstated V/E don't matter: F=17 misses all candidates.

Flag outside the 11 (recorded for honesty, no action): stored non-candidate
`ea22673a3a17c26a` (8,14,8) p=3^4 4^4 in 212/213 matches the gyrobifastigium at
f-vector AND face-type level; if it is ever advanced, a type-level (canonical
code from published vertices) check is mandatory first.

## Per-candidate G5 verdict table

Columns: re-key = digitization of the hosting group's printed table
independently re-keyed and consistent; Schmitt = f-vector status in his printed
tables (sighted groups / whole cubic survey) + type status where checked;
Bernhard = vs every cell with printed data; classical = vs the cited list.

| # | id (group, f) | re-key | Schmitt printed tables | Bernhard | classical |
|---|---|---|---|---|---|
| 1 | `ceb70631e274e727` (212, (37,57,22)) | CLEAN | present (sighted: 212/213; also 199,214,230); sighted-group reps = DIFFERENT TYPE (accepted screen); cross-group reps UNCHECKED | NO-MATCH | NO-MATCH |
| 2 | `359beee832567a71` (230, (40,61,23)) | CLEAN | present (sighted: 230; also 206,212/213,214,220); sighted rep = DIFFERENT TYPE; cross-group UNCHECKED | NO-MATCH | NO-MATCH |
| 3 | `8cf50403cf88c455` (220, (16,25,11)) | CLEAN | **f-vector absent from the ENTIRE printed cubic survey** (strongest Schmitt-side candidate; sampling caveat stands) | NO-MATCH | NO-MATCH |
| 4 | `c314dedd38208a2e` (212, (30,46,18)) | CLEAN | present (sighted: 212/213; also 198,206,214,220,230); sighted rep = DIFFERENT TYPE; cross-group UNCHECKED | NO-MATCH | NO-MATCH |
| 5 | `aa6b0077c3234d24` (214, (30,47,19)) | CLEAN | present (sighted: 214; also 199,206,212/213,230); sighted rep = DIFFERENT TYPE; cross-group UNCHECKED | NO-MATCH | NO-MATCH |
| 6 | `f3d0f39a0b9676b9` (214, (10,17,9)) | CLEAN | absent from sighted 214; printed for 7 other groups — cross-group reps UNCHECKED | NO-MATCH | NO-MATCH |
| 7 | `2de0a21129cabe90` (201, (20,33,15)) | CLEAN | absent from sighted 201; printed for 9 other groups — cross-group reps UNCHECKED | NO-MATCH | NO-MATCH |
| 8 | `c4ea3f32fdd6dc51` (224, (14,23,11)) | CLEAN | absent from sighted 224; printed for 7 other groups — cross-group reps UNCHECKED | NO-MATCH | NO-MATCH |
| 9 | `9b69eefb8bd8437c` (224, (11,18,9)) | CLEAN | absent from sighted 224; printed for 208 only — 1 cross-group rep UNCHECKED | NO-MATCH | NO-MATCH |
| 10 | `d2d935e5499e6e11` (224, (6,11,7)) | CLEAN | absent from sighted 224; printed for 6 other groups — cross-group reps UNCHECKED (note: store already holds a 2nd distinct type with same f AND p) | NO-MATCH | NO-MATCH |
| 11 | `f98a3ee5675fc121` (224, (10,15,7)) | CLEAN | absent from sighted 224; printed for 9 other groups — cross-group reps UNCHECKED | NO-MATCH | NO-MATCH |

## Honest limits (standing, restated once)

1. Schmitt's printed tables are a grid SAMPLING (351 CPU-years, exact
   arithmetic) with ONE representative point per (group, f-vector); his full
   type data (~14TB) is not recoverable online. Absence from the tables is
   evidence, not proof; presence with a different-type representative leaves
   unprinted same-f types possible. Special positions — where all 11 candidates
   except #7/#11 live — are exactly what his general-position-dense grid
   under-covers, and also exactly where his sampling could have hit types he
   did not print.
2. Bernhard's appendix shapes are published-but-unstudied drawings with face
   counts at best; a face-count NO-MATCH is decisive as printed, but his
   KP-both and Lidinoid-both entries print no counts at all
   (UNDECIDABLE-FROM-PAPER for those two entries only).
3. The re-key covers the six hosting groups (386/881 rows); the other 30 cubic
   tables remain single-pass (Euler- and remark-checked). The cross-group scan
   table above partially rests on those.
4. Aut orders in the candidate table are combinatorial; geometric stabilizers
   are the G4/V2 certified values.
5. Engel 1981 (ILL) remains an open optional leg (priority recalibrated down
   2026-08-28, Tyler's call) — Schmitt confirms+corrects Engel, but Engel's
   plates themselves were never primary-read by this program.

## What remains before ANY public wording

1. **Type-closure queue (concrete, cheap, unblocked):** extend
   `schmitt_collision_check.py` to the ~60 cross-group (group, f-vector) pairs
   in the scan table — push Schmitt's printed representative point for each
   through the exact pipeline and compare canonical codes (0.1-60s per pair in
   the accepted screen; two-origin-group shifts already solved). Until then,
   candidates #1/#2/#4-#11 carry "cross-group reps UNCHECKED".
2. **Type-closure beyond the printed representatives (Tyler gate):** the only
   routes past limit 1 are (a) recomputation with the recovered Schmitt suite
   (`references/schmitt_repo_recovery/`) at candidate-relevant strata, or (b)
   author contact (committer identity preserved in
   SCHMITT_DATA_RECOVERY_2026-08-28.md). Operator decision required; neither
   performed.
3. **Bernhard KP/Lidinoid closure (optional):** recompute his KP and
   Lidinoid-both cells from the printed TPMS formulae, or author contact —
   only needed if a candidate must be cleared against those two entries
   specifically (no current face-count proximity motivates it).
4. **Operator decisions (Tyler):** whether Engel/ILL stays waived; naming; any
   OSF/public deposit sequencing. House rules: AI-disclosure standard applies
   to all of the above; wording stays "not matched against catalog snapshot of
   2026-08-30" everywhere, "observed max 38" for the folklore bound.
5. **Acceptance:** main-session re-run of `harness/g5_rekey_check.py` (exit 0)
   before this document's Duty-1 verdict is banked as accepted.


## Correction 2026-09-03 (round-1 C3)

The parenthetical above, "no classical cell has pentagons", overreached the table: the 17-face Laves-graph cell's face types were "not stated" there. Computed 2026-09-03 through the exact chain (IT(214) I4_132, Wyckoff 8a, (1/8,1/8,1/8)): f = (30,45,17), p = 4^6 5^6 6^2 8^3, aut 12, all vertices simple, SIX pentagons. That cell is stored type `8c69db9e84095469` (triage rank 5), which the collision screen (P07-P09) identified as Schmitt's printed (30,45,17) cell in 199/212/214: a second classical rediscovery. The Duty-3 conclusion (no f-vector collision between the 11 candidates and any classical cell) is unaffected: (30,45,17) is not a candidate f-vector.
