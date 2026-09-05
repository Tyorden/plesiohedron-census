# DATA DESCRIPTOR v2, Scientific Data structure (staging text, 2026-09-04, subagent #165)

House rule: staging text written by an agent; Tyler rewrites every prose sentence before any
submission. Every number is read from `catalog/catalog.json` v5 (`summary` block, snapshot
2026-09-04, `catalog.SHA256SUMS` corrected 15:29 PDT), `catalog/RECONCILIATION.md` v5,
`catalog/STATUS.md` (v5 entry + correction), `harness/phase2/WALL_OPEN_PHASE2.md`, or the
named banked document; none is from memory. Snapshot language throughout; "new to science"
appears nowhere; the literature facet maximum is an observed 38, never a bound; the
open/wall verdict is "holds on the tested neighbourhood", never an interval proof.

Venue limits applied (Scientific Data submission guidelines, fetched 2026-09-04 17:55 PDT,
recorded in `catalog/SUBMIT_READINESS_2026-09-04.md` (f)): title <= 110 characters including
spaces, no colons or parentheses; abstract <= 170 words and no claims of new scientific
findings; mandated headings Background & Summary / Methods / Data Records / Technical
Validation / Usage Notes / Data Availability / Code Availability; no results, discussion or
analyses (a short Data Overview table is tolerated); data downloadable from a URL for the
first review round and in a formal repository (Zenodo qualifies) afterwards.

## Title

Exact generating points and combinatorial types of 1,583 plesiohedra from three crystal families

(96 characters including spaces; no colon; no parenthesis.)

## Abstract

Plesiohedra are the Voronoi cells of orbits of points under crystallographic space groups;
each tiles space with congruent copies. We release a catalog of 1,583 combinatorial types
of plesiohedra, each with an exact rational generating point in a frozen space-group setting,
the space group, the axial ratio where the metric has one, the f-vector, the facet-size
multiset, the combinatorial automorphism order, a canonical code that identifies the type, and
every sighting. The types come from exact-arithmetic Voronoi sweeps of all 36 cubic, 68
tetragonal and 52 trigonal and hexagonal space groups; a type enters the catalog only after a
floating-point proposal and an exact rational re-derivation agree. For 177 types the record
carries tiling, symmetry and polyform-count certificates, and for 172 a computed open or wall
verdict at the stored generating point. The catalog is reconciled at f-vector and type level
against the 3,315 rows of Schmitt's 2016 printed per-group tables. Machine-readable JSON and
CSV files, a sightings sidecar, SHA-256 sums, and the builder and recount scripts are
included.

(169 words, counted by script on 2026-09-04; limit 170.)

## Background & Summary

A plesiohedron is the Voronoi cell of a point relative to its orbit under a crystallographic
space group; the cells of the orbit tile space and the group acts transitively on them. The
combinatorial types that occur are known only by sampling. Schmitt's 2016 dissertation sampled
145 space groups on rational grids of about one billion points per group in exact arithmetic
and printed, per group, one representative generating point for each f-vector observed (3,315
rows across the cubic, tetragonal and trigonal/hexagonal systems, 238 distinct f-vectors,
observed maximum 38 facets); the full type data, about 14 TB, was never published and is not
recoverable online (`SCHMITT_DATA_RECOVERY_2026-08-28.md`). Engel's 1981 cubic catalogs and
Koch's 1972 thesis are print-only. To the extent of the records checked as of 2026-09-04, no
machine-readable list of plesiohedron combinatorial types with exact generating data existed
before this release.

The catalog is the deduplicated type store of a gated search pipeline (Track 3 of the program
plan of 2026-08-27) whose cubic results are the subject of a companion paper (seven certified
cells, two of them named) and whose method is the subject of a second companion paper. It is
organised by combinatorial type, not by group: a type sighted in several groups or at several
axial ratios appears once, with every sighting attached. Of the 1,583 types, 102 were first
sighted in cubic groups, 789 in tetragonal groups and 692 in the hexagonal family (398
trigonal, 294 hexagonal by crystal system of the first witness; 3 seeded types have no sweep
witness). Seven types were seeded from published vertex data as controls (the five
parallelohedra, the Josehedron, and Schmitt's printed IT(220) general-position (12,22,12)
cell, the last never sighted by any sweep). Two types carry program names (Satchelhedron,
IT(220), f = (16,25,11); Ordenhedron, IT(201), f = (20,33,15)); three cubic cells carry a
"held" marker and two a descriptive package name; two literature cells were rediscovered by
the sweep (the Laves-graph plesiohedron and the triakis truncated tetrahedron). No other type
is named.

## Methods

Frozen operations (gate G1). The 230 space groups were frozen into one table of 4,425
operations with exact rational translations (denominators dividing 12) from spglib 2.7.0 in
the conventional ITA setting (origin choice 1 for the two-origin groups; rhombohedral groups
on hexagonal axes). A checker sharing no code with the generator audited identity, closure,
inverses and operation counts; an operation-by-operation comparison with Schmitt's 2016
operation tables, recovered through Software Heritage, agreed on all 229 comparable groups
(148 in the identical setting, 81 after documented changes of setting, zero mismatches;
`SCHMITT_OPS_XCHECK_2026-08-28.md`).

Regression and controls (gates G0, G2, G2b, G2c). Before the cubic sweep the chain had to
re-derive the Josehedron from its 12-point generating orbit and reproduce its published
polyform sequences, and the origin orbits of the three cubic lattices had to return the cube,
the rhombic dodecahedron and the truncated octahedron by canonical code against a seed
catalog built by separate code from published vertices. Before the tetragonal sweep the
hexagonal prism and the elongated dodecahedron had to return through the metric path and
three of Schmitt's printed tetragonal rows had to reproduce their printed f-vectors from the
printed points (`harness/phase2/G2B_RESULT.md`). Before the hexagonal-family sweep the
rhombohedral lattice at the face-centred and body-centred axial ratios had to return the
rhombic dodecahedron and the truncated octahedron, and six printed trigonal/hexagonal rows,
including Schmitt's 34-facet family maximum, had to reproduce their printed f-vectors
(`harness/phase2/G2C_RESULT.md`). Each control block was written into `ANCHORS.md` before
its sweep ran.

Sweeps. Cubic (36 groups): every special-position orbit on the grid of points whose
coordinates have denominators in {1, 2, 3, 4, 6, 8, 12}, plus two general-position control
points per group; 1,597 orbits, 102 types (`harness/PHASE1_RESULT.md`). Tetragonal (68
groups): 5,825 coarse orbits and 1,014 line orbits at 13 coarse axial ratios, five of
Schmitt's printed ratios, and a one-dimensional bisection, plus every printed tetragonal row
evaluated at his own point; 148,816 (orbit, axial ratio) evaluations, 294,772 exact cells
(`harness/PHASE2_RESULT.md`). Hexagonal family (52 groups): 4,651 coarse orbits and 676 line
orbits under the same pass structure; 108,580 evaluations, 212,912 exact cells
(`harness/PHASE2_HEX_RESULT.md`). The metric enters as an exact Gram matrix in the
conventional basis; all distances, bisectors and the neighbour cutoff are evaluated in the
Gram norm.

Exact confirmation (gate G3, the store invariant). For each candidate a floating-point
Voronoi computation proposes facets and neighbour sites; the cell is then re-derived by exact
rational clipping of the bisector half-spaces of all sites within a cutoff, with the lemma
4 rho^2 <= D^2 checked after the fact so that no site was missed. A type enters the store
only if the floating-point and exact cells agree on facet count, facet-size multiset and
canonical code (or the float cell is degeneracy-flagged and the exact cell decides); in the
tetragonal and hexagonal sweeps a second orbit cell is clipped exactly and must give the same
code. Any sighting above 38 facets would have aborted the run for inspection; none occurred.

Canonical code. A relabelling-invariant, mirror-invariant encoding of the facet-cycle
structure of the boundary map (`harness/canon_code.py`, unit tests `harness/test_canon.py`);
the type identifier is the first 16 hexadecimal digits of the SHA-1 of the code.

Certificates (gate G4). For 177 types: exact re-derivation from the stored witness; a tiling
certificate (all T translation-class representatives return the same code, T*vol = |det L|,
every facet slot paired one-to-one with a neighbouring cell's facet, bisector disjointness
over every site within the certified ball) re-proved by a second implementation sharing no
geometry code; the isometry group of the solid; and polyform counts with the Burnside
identity (`harness/G4_RESULTS.md`, `harness/G4_PHASE2_RESULTS.md`,
`harness/G4_PHASE2_HEX_RESULTS.md`, `track4/TRACK4_RESULTS.md`).

Open/wall classification. For the 7 cubic finalists (2026-09-03) and the 165 certified
tetragonal and hexagonal-family cells (scheme pre-registered in `ANCHORS.md` on 2026-09-04
before the run), the generating point was moved by +-1/48 and +-1/96 along each tangent
direction of its Wyckoff stratum (refined by halving to 1/1536 on any side that changed) and,
where the metric has a parameter, the axial ratio by relative steps +-1/96 and +-1/192
(refined to 1/3072). A direction is a wall when both of its sides change type at the finest
step; a presentation is OPEN when every tested side keeps the type, and ONE-SIDED otherwise
(`harness/phase2/WALL_OPEN_PHASE2.md`; `harness/round1_computations/RESULTS.md` C1).

Diligence (gate G5). Schmitt's printed per-group tables were digitized: 881 cubic rows
(the six tables hosting the cubic finalists, 386 rows, independently re-keyed with zero
discrepancies), 1,476 tetragonal rows (single visual pass, cross-checked row for row against
the PDF text layer), and 958 trigonal/hexagonal rows (blind independent re-key, zero
discrepancies). Type-level identity with Schmitt's printed cells is decided by canonical code:
his printed representative points were recomputed through the chain (76 cubic pairs; every
tetragonal and hexagonal-family row through the sweep's P2 pass or a read-only re-run), so
his printed cells are stored types and any coincidence is a code equality.

Every gate script and the independent recount were re-run by the operator's main session
with exit code zero before acceptance (`STATUS.md`, `catalog/STATUS.md`, dated entries
2026-08-28 to 2026-09-04).

## Data Records

Files (committed forms; `catalog.SHA256SUMS` v5, corrected 2026-09-04 15:29 PDT):

| file | bytes | SHA-256 (first 16) | content |
|---|---|---|---|
| catalog.json.gz | 858,911 | 6ffea7ee7a264134 | one record per type, plus `summary`, `inputs`, `field_sources`, `build` |
| catalog.csv.gz | 577,635 | c1c0ae4b6eaf8583 | the same records, one row per type |
| catalog_sightings.json.gz | 1,217,329 | aab7fda4b4f8c15d | {type_id: [sighting, ...]}; 258,521 sightings (1,597 cubic orbit records, 148,390 tetragonal, 108,534 hexagonal-family) |
| catalog.SHA256SUMS | 1,686 | (the sums file) | sums and sizes of the five catalog files, raw JSON (10,891,630 bytes) and CSV (5,645,919) included |

One record per combinatorial type, 1,583 records. Column families (every column's provenance
is in `catalog.json["field_sources"]`):

- Identity: `catalog_id` (MINT-C001..C102, MINT-T001..T789, MINT-H001..H692 in first-sighting
  order), `type_id`, `canon_code`, `canon_code_sha256`.
- First witness: `witness_group`, `witness_group_symbol`, `witness_point` (exact rational
  fractional coordinates in the frozen setting), `witness_kind`, `witness_c_over_a`,
  `witness_stratum_dim`, `witness_site_stabilizer_order`, `witness_orbit_conventional`,
  `witness_orbit_primitive`, `first_sighting_family`, `first_sighting_crystal_system`.
- Combinatorics: `f_vector`, `V`, `E`, `F`, `p_vector`, `p_vector_str`, `aut_order`, the
  degeneracy flags at the witness (`nonsimple_vertices_witness`, `degenerate_flag_witness`,
  `lattice_degenerate_witness`, `float_superseded_witness`).
- Sightings: per-family counts, groups and axial ratios (menu vs all), `systems_sighted`,
  `crystal_families_sighted`, `crystal_systems_sighted`, `schmitt_printed_only_*`.
- Gates: `gate_G3`, `g4_status` (accepted-cubic 12 / certified-tetragonal 14 /
  certified-hexagonal 151 / none 1,406), `g4_certificate_file`, `g4_results_doc`,
  `g4_acceptance`, `g4_chiral_solid` (153 chiral, 12 achiral, 12 not recorded in the cubic
  certificates), `g4_chiral_honeycomb` (138 of 177).
- Open/wall: `open_wall_verdict` (OPEN 121 / WALL 42 / ONE-SIDED 9 / not-computed 1,411),
  `open_wall_point_verdict`, `open_wall_metric_verdict`, `open_wall_flags`,
  `open_wall_verdict_source`, `open_wall_verdict_pointer`, `open_wall_scheme`,
  `open_wall_scheme_date`.
- Schmitt reconciliation: `schmitt_fvector_printed_anywhere_{cubic,tetragonal,hexagonal}`,
  `schmitt_fvector_flag_sighted_groups` (P 1,568 / A 14 / n/a 1),
  `schmitt_type_level_status` (SAME 1,125 / DIFFERENT 449 / unchecked 9),
  `schmitt_type_status` with `schmitt_type_status_source` (tetragonal-first: SURVIVOR 203 /
  COLLISION 201 / UNRESOLVED 0 / printed-only 385; hexagonal-first: 151 / 124 / 13 / 404;
  cubic-first: not-screened 102 by construction), `schmitt_match_hexagonal`.
- Names: `name`, `name_status` (2 program, 3 held, 2 descriptive, 2 literature, 5 seeded
  classical, the rest none); `wyckoff_letter` and `wyckoff_site_symmetry` for the seven cubic
  finalists and the Laves cell only.
- `novelty_wording`: the fixed sentence "not matched against the records checked as of
  2026-09-04".

Summary block (`catalog.json["summary"]`, catalog_version 5): 1,583 types = 102 + 789 + 692;
7 seeded (1 never sighted); 404 tetragonal-first and 288 hexagonal-first types met by our
own menus, 385 and 404 seen only at Schmitt's printed points; 19 cubic-first types re-sighted
in tetragonal groups and 43 prior types (17 cubic-first, 26 tetragonal-first) in the
hexagonal family; 196 distinct f-vectors (65 / 153 / 167 by first family); observed maximum
35 facets (cubic-first 23; tetragonal menu 26, tetragonal-first 35; hexagonal menu 24,
hexagonal-first 34); G4 certified 177.

## Technical Validation

1. Store invariant (G3) for every non-seeded type in all three stores; 0 quarantines in the
   cubic sweep; 426 tetragonal quarantines all classified (424 coordinate-convention
   mismatches resolved by one origin shift per group or the enantiomorph map, 2 order_cycle
   crashes resolved 2026-09-04); 46 hexagonal-family quarantines, all IT(180) rows whose
   printed points are IT(181)'s per Schmitt's own remark, reproduced by a read-only re-run
   (`harness/PHASE2_HEX_SCHMITT_180_CHECK.md`); none stored.
2. Controls: G0 (Josehedron re-derived, counts equal to A398957-A398959), G2 (three cubic
   lattice cells), G2b (21/21 assertions), G2c (all required assertions), each accepted after
   a main-session re-run; the truncated octahedron from the body-centred tetragonal lattice at
   c/a = 1 passes the Gram certificate ladder with every number equal to the cubic run.
3. Operation tables: independent audit plus the 229-group comparison with Schmitt's recovered
   tables (148 exact, 81 conjugate-verified, 0 mismatches).
4. Certificates: 177 cells (12 cubic incl. the Laves cell; 14 tetragonal; 151
   hexagonal-family), every batch re-run in full by the main session with exit 0 before
   acceptance; the tiling certificate is re-proved by a second implementation; the
   independent polyform enumerator reached n = 5 for every phase-2 cell and n = 6 for the four
   cubic cells with OEIS drafts.
5. Diligence: 386 cubic rows re-keyed (0 discrepancies); 1,476 tetragonal rows cross-checked
   against the text layer; 958 trigonal/hexagonal rows blind re-keyed (0 discrepancies);
   1,476/1,476 printed tetragonal rows and 1,276/1,276 (row x group) hexagonal evaluations
   reproduce their printed f-vector through the chain; the 62 tetragonal rows the sweep could
   not store were recomputed under every documented setting convention (62/62 reproduce, one
   canonical code per row), which settled all 106 previously unresolved tetragonal types.
6. Open/wall: 3,879 exact evaluations, 0 quarantines, deterministic JSON (sorted keys, no
   timings) with md5 6b257c551f6fb275dfabb03e992f57c2 reproduced by the main session;
   regression against the earlier absolute-step run on the three top tetragonal cells.
7. Independent recount (`verify_counts_independent.py`, no code shared with the builder):
   recounts every headline, per-family, per-group, per-status and chirality number from the
   raw stores, certificate files and verdict/screen files, re-derives every type id from its
   code, checks Euler and the p-vector identities for all 1,583 types, re-implements the
   store-side screen rule and the 62-row overlay with its own keying, and asserts equality
   with `catalog.json`: 0 failures, exit 0 (v5).
8. Determinism: two consecutive builds byte-identical on all five catalog files;
   `RECONCILIATION.md` is append-only (each committed version an exact prefix of the next,
   asserted), and its v1 and v2 sections are regenerated from the v5 catalog and asserted
   equal before the later sections are appended.
9. Reconciliation against Schmitt's printed tables (f-vector level, `RECONCILIATION.md`):
   cubic, 986 printed (group, f) pairs: 292 matched by our menu, 33 of ours absent from his
   table for that group, 694 of his unreached by our menu (whole-system distinct f-vectors his
   194 / ours 63 / shared 62); tetragonal, 1,639 pairs: 700 matched, 67 absent, 939 unreached
   (669 stored through his own printed points, 270 with no stored type; his 163 / ours 80 /
   shared 80); hexagonal family, 1,276 pairs: 510 matched, 40 absent, 766 unreached (733
   through his points, 33 by the read-only re-run, 0 with no stored type; his 177 / ours 95 /
   shared 94). Exactly one f-vector of ours, (20,36,18) (hexagonal-first, IT(178) at c/a =
   3/2, a wall cell), is printed in none of his tables in any of the three families.
10. A follow-up type-level check raised by the reconciliation: (16,25,11), the Satchelhedron's
    f-vector, is printed in Schmitt's tetragonal IT(134) and IT(141) tables; both cells,
    recomputed exactly under every documented origin shift, are different types from the
    Satchelhedron and from each other (`SATCHELHEDRON_TETRAGONAL_ROWS.md`; main-session re-run
    2026-09-04).

## Usage Notes

- To test whether a cell is in the catalog, compute its canonical code with
  `harness/canon_code.py` and look up `type_id = sha1(code)[:16]`; the p-vector alone does
  not settle identity (two distinct codes share f = (6,11,7) and p = 3^6 4^1).
- Generating points are in the frozen ITA setting (origin choice 1 for the 24 two-origin
  groups; hexagonal axes for the rhombohedral groups). Schmitt's printed points use origin
  choice 2 and, for the trigonal/hexagonal groups, his orthohexagonal basis; the documented
  conversions are in `harness/phase2_schmitt_origin_check.json`,
  `harness/PHASE2_SCHMITT_ORIGIN_CHECK.md` and `ANCHORS.md` (G2c block).
- `aut_order` is combinatorial (automorphisms of the code, mirror included); the isometry
  group of the solid is recorded only for certified cells and can be smaller.
- A P flag means only that Schmitt's table prints the same f-vector for that group;
  `schmitt_type_status` SURVIVOR means the type differs from his cell at every printed
  representative of every (group, f) pair it occupies, COLLISION that it reproduces one of his
  printed cells, and neither is a statement about his unprinted data.
- `open_wall_verdict` describes the stored first witness only (one point, one axial ratio);
  OPEN means the type held on the tested neighbourhood along each axis, not on a box (a later
  search inside the product of per-axis extents found type changes at points that move two or
  more coordinates at once, `NICE_POINTS_2026-09-04.md`); a WALL witness does not preclude an
  open region of the same type elsewhere.
- Coverage: the "unreached" counts in `RECONCILIATION.md` measure how much of his printed
  survey our menus reached (51 of his 56 tetragonal and 29 of his 38 hexagonal-family printed
  axial ratios were never swept). The catalog records what these samples found; it is not an
  enumeration, and absence from a printed table is evidence, not proof.
- The tetragonal digitization is a single visual pass cross-checked against the text layer,
  not an independent re-key; a changed row can move a type between statuses. Engel 1981 and
  Koch 1972 are print-only and have not been read; the interlibrary request is pending.
  Orthorhombic, monoclinic and triclinic groups are not covered.

## Data Availability

The five catalog files, the three type stores (compressed, with SHA-256 sums), the
digitizations and re-keys of Schmitt's tables, the certificate tables, the open/wall
classification and the pre-registered gate texts are deposited at Zenodo (DOI minted at
deposit; record contents in `publication/ZENODO_MANIFEST.md`, v2 section) and mirrored at
https://github.com/Tyorden/plesiohedron-census (repository being created 2026-09-04; verify
before submission). Schmitt's recovered 2016 software is cited by its Software Heritage
identifiers (`SCHMITT_DATA_RECOVERY_2026-08-28.md`) and is not redistributed. Data, tables
and text are released under CC BY 4.0.

## Code Availability

`catalog/build_catalog.py`, `catalog/reconcile_schmitt.py`,
`catalog/verify_counts_independent.py`, `catalog/check_satchelhedron_tetragonal_rows.py`
(Python 3.13 standard library except the last, which imports the harness); the pipeline in
`harness/` (`sweep_phase1.py`, `sweep_phase2_tetragonal.py`, `sweep_phase2_hexagonal.py`,
`exact_cell.py`, `canon_code.py`, `orbit.py`, `phase2/{metric,sweep_voronoi_gram,
exact_cell_gram}.py`, `g4_certify.py`, `g4_certify_gram.py`, `g4_certify_hex.py`,
`phase2/wall_open_phase2.py`, the collision and digitization scripts); the polyform enumerator
is the one published with OEIS A398957. Code is released under the MIT license. Every script
that produced a number in this descriptor is named next to it in the banked result document
it cites.

## Acknowledgements

The author thanks Mathias Bernhard for publishing the Josehedron's generating points in full.

## Author contributions

T.S.O. designed the gates, directed the computation, verified every gate result by re-running
it, and wrote the paper.

## Competing interests

The author declares no competing interests.

## AI disclosure (house form)

%% REWRITE CONDITION: "which I rewrote" is true only after Tyler's rewrite of this text.
I used Claude (Anthropic), a large language model, throughout this work under my direction:
it wrote the sweep, catalog builder, reconciliation and recount scripts, ran the sweeps and
certificates, performed the transcriptions and the blind re-key of the printed tables,
checked the bibliographic references against their sources, and produced an initial draft of
this text, which I rewrote. Every gate script and the independent recount were re-run by me,
separately from the agent that built them, with exit code zero required before acceptance,
and every number in this descriptor is read from the generated files. I take full
responsibility for the content.

## Figures and tables to prepare (Data Overview, tolerated by the venue)

- Table 1: the census by family (groups, evaluations, exact cells, types first sighted
  split menu / printed-only, certified, open / wall / one-sided): 36 / 1,597 / -- / 102 (95 /
  7 seeded) / 12 / 6-1-0; 68 / 148,816 / 294,772 / 789 (404 / 385) / 14 / 13-1-0; 52 / 108,580
  / 212,912 / 692 (288 / 404) / 151 / 102-40-9.
- Figure 1: the gate chain as a flow diagram (G1, G0/G2/G2b/G2c, sweep, G3, canonical code,
  G4, open/wall, G5) with the file that records each gate.
- Figure 2: facet-count histogram of the 1,583 types by first family, with Schmitt's printed
  maximum (38) and the catalog maximum (35) marked.

---------------------------------------------------------------------------
## Appendix A. Acta Crystallographica Section A: alternative framing

Acta Cryst. A (Foundations and Advances) publishes research papers and short communications
in mathematical crystallography and would read this release as a table of Dirichlet-domain
(Wirkungsbereich) types, the lineage of Koch 1972, Engel 1981 and Schmitt 2016. Differences
from the Scientific Data framing:

- Title (working): "A machine-readable catalogue of Dirichlet domain types for the cubic,
  tetragonal, trigonal and hexagonal space groups". No length limit was verified
  (journals.iucr.org returned HTTP 403 to the fetcher on 2026-09-04; article types, APC and
  AI policy remain UNVERIFIED, `catalog/VENUE_SCOUT.md` rows 2 and 5).
- Results and discussion are permitted, so the reconciliation findings that Scientific Data
  rules out of the abstract belong in the body here: 33 cubic, 67 tetragonal and 40
  hexagonal-family (group, f-vector) pairs of ours absent from Schmitt's table for that
  group; 694 / 939 / 766 of his pairs unreached by our menus; the seven same-f-vector
  micro-facts; the (20,36,18) wall cell as the only f-vector printed nowhere; the
  grid-parity explanation of the Satchelhedron's absence (cited from the companion paper,
  not repeated).
- Crystallographic conventions come first: the frozen setting (origin choice 1; hexagonal
  axes; the Gram-matrix metric), the Wyckoff position and site symmetry of every certified
  witness, the lattice complex where it clarifies Koch's scope, and the setting conversions
  used for Schmitt's printed points (origin choice 2; the orthohexagonal basis B'').
- The comparison with the print-only catalogs would be expected in depth; the interlibrary
  read of Engel 1981 and Koch 1972 should precede an Acta A submission, whereas Scientific
  Data's data-only framing tolerates "not read; request pending".
- The same Zenodo DOI is cited; Acta A has its own supplementary-material route, which the
  Zenodo record can stand in for.

## Appendix B. Recommendation (unchanged from `catalog/SUBMIT_READINESS_2026-09-04.md`)

Zenodo first. The dataset deposit is independent of any venue, every venue would cite its
DOI, and the first review round at Scientific Data only needs a download URL. Then Scientific
Data as the primary venue (the data-only framing fits the catalog exactly; the mathematics
in-scope question is the one risk, `VENUE_SCOUT.md`), with Acta Cryst. A as the alternative if
Scientific Data rules a mathematics dataset out of scope or if the Engel/Koch read arrives
first and a crystallographic results paper becomes the stronger form. arXiv math.MG as a
preprint in either case. Nothing here is executed without Tyler's word; the venue decision
and the rewrite are his.

UNTESTED AGAINST: Scientific Data's view of a mathematics dataset as in scope; both
venues' APC and AI-use pages (bot-walled); a JSON-summary-vs-text recount by a second agent.
