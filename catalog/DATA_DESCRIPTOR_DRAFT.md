# DATA DESCRIPTOR DRAFT (staging text, 2026-09-04)

House rule: this is staging text written by an agent; Tyler rewrites all prose from
memory before any submission. Every number below is read from `catalog.json`
(`summary` block), `reconciliation_summary.json`, or the named banked document;
none is from memory. Snapshot language throughout: types are "not matched against
the records checked as of 2026-09-04"; "new to science" appears nowhere; the
literature facet maximum is an observed 38, not a proven bound.

## Title

A machine-readable census of 891 exact-confirmed plesiohedron combinatorial types
from gated Voronoi sweeps of the 36 cubic and 68 tetragonal space groups

## Abstract (draft)

We release a catalog of 891 combinatorial types of plesiohedra (Voronoi cells of
space-group orbits, i.e. isohedral space-filling polyhedra) produced by two exact-
arithmetic sweeps: a special-position sweep of all 36 cubic space groups (1,597
orbits, 102 types) and a sweep of all 68 tetragonal space groups over a grid of
generating points and 13 coarse c/a ratios plus targeted passes (148,816 candidates,
294,772 exact cells, 789 further types). Each record carries an exact generating
point (rational coordinates in the frozen ITA setting), the space group, the metric
parameter where relevant, the f-vector, the facet-size multiset, the combinatorial
automorphism order, a canonical code that identifies the type, and every sighting.
Types entered the store only after a float proposal and an exact rational
re-derivation agreed on facet count, facet-size multiset and canonical code
(gate G3). Twelve types additionally carry tiling, symmetry and Burnside
certificates (gate G4). The catalog is reconciled at f-vector level against the
1,476 tetragonal and 881 cubic rows of Schmitt's 2016 printed per-group tables and
at type level against 103 exact recomputations at his printed representative points
plus 1,215 stored reproductions of his tetragonal rows. The reconciliation is
two-sided: 33 cubic and 67 tetragonal (group, f-vector) pairs of ours are absent
from his table for that group, while 694 cubic and 939 tetragonal printed pairs were
never reached by our own sample points, which measures the coverage of our sweeps
rather than of his. Absence from a printed table is evidence, not proof; his survey
is a sampling, not an enumeration.

## Background and summary

Plesiohedra are the Voronoi cells of orbits of points under crystallographic
groups; each one tiles space isohedrally. The combinatorial types that occur are
known only by sampling. Schmitt (2016, dissertation) sampled 145 groups on grids of
about 10^9 points per group in exact arithmetic and printed, per group, one
representative generating point per f-vector observed (3,315 types, 238 f-vectors,
observed maximum 38 facets); the full type data (about 14 TB) was never published
and is not recoverable online (SCHMITT_DATA_RECOVERY_2026-08-28.md). Engel's 1981
tables cover symmorphic cubic groups in print only. No machine-readable list of
plesiohedron combinatorial types with exact generating data existed before this
release, to the extent of the records checked as of 2026-09-04.

This catalog is the dedupe store of a gated search pipeline (PROGRAM_PLAN
2026-08-27, Track 3). It is organised by combinatorial type, not by group: a type
sighted in several groups or at several metric parameters appears once, with every
sighting attached. Two cells in the catalog carry program names (Satchelhedron,
IT(220), f=(16,25,11); Ordenhedron, IT(201), f=(20,33,15)); two are described by
literature names because the sweep rediscovered them (the Laves-graph
plesiohedron and the triakis truncated tetrahedron); five are the classical
parallelohedra seeded as controls.

## Methods (the gate chain in one page; each gate cites its record)

- G1, frozen space-group operations: `harness/spacegroups.json`, 230 groups,
  4,425 operations, translations exact n/12 rationals (spglib 2.7.0, origin
  choice 1); verified by a no-shared-code audit (`harness/G1_RESULT.md`) and by an
  operation-by-operation comparison with Schmitt's independent 2016 C++
  representations for groups 2-230 (148 exact, 81 conjugate-verified, 0 mismatch;
  `SCHMITT_OPS_XCHECK_2026-08-28.md`).
- G0, regression: the pipeline re-derives the Josehedron (Bernhard 2026) from its
  generating orbit, including its enumerator tables (`harness/G0_RESULT.md`,
  `harness/MINT_TABLES_RESULT.md`).
- G2/G2b, controls: cube, rhombic dodecahedron and truncated octahedron from the
  SC/FCC/BCC lattices by canonical code against a seed catalog built from published
  vertex data; hexagonal prism and elongated dodecahedron through the metric (Gram)
  path; three of Schmitt's printed tetragonal rows reproduced exactly
  (`harness/G2_RESULT.md`, `harness/phase2/G2B_RESULT.md`).
- G3, exact confirmation (the store invariant): each candidate orbit gives a float
  Voronoi proposal; the cell is then re-derived by exact rational clipping with a
  provable neighbour cutoff (4 rho^2 <= D^2 in the metric norm); a type enters the
  store only if float and exact agree on facet count, facet-size multiset and
  canonical code, or the float cell is degeneracy-flagged and the exact cell
  decides. In phase 2 a second orbit cell is clipped exactly and must give the same
  code (`harness/PHASE1_RESULT.md`, `harness/PHASE2_RESULT.md`).
- Canonical code: a relabelling-invariant, mirror-invariant encoding of the facet
  cycle structure (`harness/canon_code.py`, unit tests `harness/test_canon.py`);
  the type id is sha1(code)[:16].
- G4, certificates for advanced cells: exact re-derivation from the stored witness,
  a tiling certificate (facet pairing, T*vol = det L, disjointness balls) verified
  by a second independent implementation, symmetry certification over all
  orthogonal maps, and the Burnside identity on polyform counts
  (`harness/G4_RESULTS.md`, `track4/TRACK4_RESULTS.md`).
- G5, diligence against printed records: independent re-key of 386 cubic rows,
  cross-checks of the tetragonal digitization against the PDF text layer, exact
  recomputation at 21 + 55 cubic and 27 tetragonal printed representative points
  (`G5_DILIGENCE_2026-08-30.md`, `harness/SCHMITT_COLLISION_RESULTS.md`,
  `harness/CROSS_GROUP_RESULTS.md`, `harness/COLLISION_PHASE2_RESULTS.md`).
- Every gate script was re-run by the operator's main session with exit 0 before
  acceptance (STATUS.md entries dated 2026-08-28 to 2026-09-04).

Sampling design, stated plainly: phase 1 sampled special positions on the
{1,2,3,4,6,8,12}-denominator grid plus two general-position controls per cubic
group; phase 2 sampled 5,825 orbits per group set at 13 c/a values, five of
Schmitt's printed c/a values, 1,014 extra line orbits, and a one-dimensional c/a
bisection, and separately evaluated all 1,476 printed tetragonal rows. 51 of his 56
printed c/a values were never swept. The catalog therefore records what these
samples found; it is not an enumeration.

## Data records (schema of `catalog.json` / `catalog.csv`)

One record per combinatorial type; 891 records. Key columns (full provenance of
every column in `catalog.json["field_sources"]`):

| column | meaning | source |
|---|---|---|
| catalog_id | MINT-C001..C102 (cubic-first), MINT-T001..T789 (tetragonal-first), in first-sighting order | assigned |
| type_id | sha1(canon_code)[:16], the store key | store |
| canon_code, canon_code_sha256 | the canonical facet-cycle code and its SHA-256 | store |
| first_sighting_system, systems_sighted | cubic / tetragonal | store |
| witness_group, witness_group_symbol, witness_point, witness_kind, witness_c_over_a, witness_stratum_dim, witness_site_stabilizer_order, witness_orbit_conventional, witness_orbit_primitive | the first witness: IT number and symbol, exact rational generating point, stratum dimension, site-symmetry order, orbit sizes; c/a for tetragonal | store (first_witness) |
| wyckoff_letter, wyckoff_site_symmetry | only for the seven cubic finalists (spglib 2.7.0) and the Laves cell; null elsewhere: NOT a store field | paper/wyckoff_check.txt |
| f_vector, V, E, F, p_vector, p_vector_str, aut_order | f-vector, facet-size multiset, combinatorial automorphism order | store |
| nonsimple_vertices_witness, degenerate_flag_witness, lattice_degenerate_witness, float_superseded_witness | degeneracy flags at the witness | store |
| open_wall | OPEN / WALL from documented perturbation runs (7 cubic finalists, 3 tetragonal shortlist types); null elsewhere: NOT a store field | c1_wall_open.json, collision_phase2_results.json |
| seeded, seed_source | the 7 seed-catalog types | store |
| n_sightings_*, groups_sighted_*, c_over_a_values_* | sighting counts, groups, c/a values (menu vs all) | store |
| gate_G3, gate_G4_certified, gate_G4_pointer | G3 by store invariant; G4 accepted / provisional / no, with file pointer | store; harness files |
| name, name_status | program name, literature name, descriptive, HELD, or none | publication/ tree |
| schmitt_fvector_flag_sighted_groups (P/A), schmitt_fvector_present/absent_in_sighted_groups, schmitt_fvector_printed_anywhere_cubic/tetragonal | f-vector-level status against the digitized tables | digitizations |
| schmitt_type_level_status, schmitt_type_level_detail | SAME / DIFFERENT / unchecked with pair pointers | accepted screens; P2 sightings; dedupe inference |
| novelty_wording | the snapshot sentence | fixed |

Sidecar `catalog_sightings.json.gz`: {type_id: [sighting]} with, per sighting,
system, group, symbol, exact point, kind (special / general / line24 /
schmitt_printed), c/a, pass, stratum_dim, site_stabilizer_order, orbit sizes,
degeneracy flags, W, congruence_checked. 149,987 sightings in total (1,597 cubic
orbit records + 148,390 tetragonal).

Summary numbers (from `catalog.json["summary"]`): 891 types = 102 cubic-first +
789 tetragonal-first; 7 seeded (1 never sighted by any sweep: Schmitt's IT(220)
general-position (12,22,12) representative, kept as a seed); tetragonal-first
split 404 menu-sighted / 385 seen only at his printed points; 19 cubic-first types
re-sighted in tetragonal groups (18 by our menu); 175 distinct f-vectors (65 among
cubic-first, 153 among tetragonal-first); maximum facet count 35 (from our own
menu 26; cubic 23); G4 accepted 12 (11 cubic + the Laves cell), 14 further types
with provisional phase-2 certificate tables on disk at build time; names: 2
program, 2 descriptive, 3 held; Schmitt type-level status SAME 589, DIFFERENT 282,
unchecked 20; f-vector flag over sighted groups P 880, A 10, n/a 1.

## Technical validation

1. G3 (store invariant) for every non-seeded type; 0 quarantines in phase 1; 426
   phase-2 quarantines all classified (424 coordinate-convention mismatches
   resolved by one origin shift per group or the z -> -z enantiomorph map, 2
   order_cycle crashes resolved 2026-09-04), none stored.
2. G4 for 12 types (11 cubic accepted 2026-08-30; Laves cell accepted 2026-09-03).
3. G2b metric controls 21/21 (accepted 2026-09-03).
4. G5 records as cited above; 1,476/1,476 printed tetragonal rows reproduce their
   printed f-vector (1,215 stored + 261 through the read-only origin check).
5. Independent recount (`verify_counts_independent.py`, this folder, shares no
   code with the builder): recounts every headline number and every per-group
   count directly from the two stores, re-derives every type id from its code,
   checks Euler and the p-vector identities for all 891 types, and asserts
   equality with `catalog.json`: 0 failures, exit 0 (2026-09-04).
6. Both builders are deterministic: `catalog.json`, `catalog.csv` and
   `RECONCILIATION.md` are byte-identical across re-runs on the same inputs.
7. Reconciliation against Schmitt's printed tables (`RECONCILIATION.md`), headline:
   cubic, 986 printed (group, f) pairs, 292 matched by our menu (309 of our
   (type, group) sightings), 33 of ours absent from his table for that group, 694
   of his unreached by our menu; whole-system distinct f-vectors his 194 / ours 63 /
   shared 62, the only f-vector of ours printed in no cubic table being (16,25,11).
   Tetragonal, 1,639 printed (group, f) pairs, 700 matched (355 at a c/a we also
   sampled; 988 of our sightings), 67 of ours absent from his table for that
   group, 939 of his unreached by our menu (669 of those stored through the P2
   pass at his own point, 270 with no stored type); whole-system his 163 / ours
   80 / shared 80.
8. Follow-up type-level check raised by the reconciliation: (16,25,11) is printed
   in Schmitt's tetragonal IT(134) and IT(141) tables; both cells recomputed
   exactly under every documented origin shift are DIFFERENT types from the
   Satchelhedron (`SATCHELHEDRON_TETRAGONAL_ROWS.md`; provisional until the main
   session re-runs it).

## Usage notes

- Types are identified by `canon_code`; to test whether a new cell is in the
  catalog, compute its canonical code with `harness/canon_code.py` and look up
  `type_id = sha1(code)[:16]`.
- The generating point is in the frozen ITA setting (origin choice 1 for the 24
  two-origin groups). Schmitt's printed points use origin choice 2; the shifts are
  in `harness/phase2_schmitt_origin_check.json` and `SCHMITT_OPS_XCHECK_2026-08-28.md`.
- `aut_order` is combinatorial (automorphisms of the code, mirror included); the
  geometric stabilizer is smaller for the certified "symmetry-gap" cells (see G4).
- A P (present) flag means only that his table prints the same f-vector for that
  group; identity or difference at type level is in `schmitt_type_level_*`.
- Coverage: the (c) counts in `RECONCILIATION.md` say how much of his printed
  survey our menu reached; they are the honest measure of what this catalog is not.

## Code availability

`catalog/build_catalog.py`, `catalog/reconcile_schmitt.py`,
`catalog/verify_counts_independent.py`, `catalog/check_satchelhedron_tetragonal_rows.py`
(this folder; pure Python 3.13 standard library except the last, which imports the
accepted harness modules); the pipeline in `harness/` (sweep_phase1.py,
sweep_phase2_tetragonal.py, exact_cell.py, canon_code.py, orbit.py, phase2/*).
Schmitt's recovered 2016 software is cited by SWHID in
`SCHMITT_DATA_RECOVERY_2026-08-28.md` and is not redistributed here. Deposit
packaging follows `publication/ZENODO_MANIFEST.md` (Tyler pushes; the wall
re-sweep of every artifact precedes any deposit).

## AI disclosure (house standard)

Analysis and drafting assisted by Claude (Anthropic). Claude agents wrote the
pipeline and this catalog's builders, ran the gates, and drafted this document,
under gate specifications and acceptance criteria written by the author before
computation. Gate verdicts are produced by deterministic rational-arithmetic
checks; agents do not judge their own results; every gate script and the
independent recount were re-run in the operator's main session with exit code
zero required before acceptance, and every count in this document is read from
the generated files, not from memory. The prose of any submitted version is the
author's own.

## Limitations

- Sampling, not enumeration: special positions on a coarse grid (cubic), 13 + 5
  c/a values and a coarse grid (tetragonal); 51 of Schmitt's 56 printed c/a values
  were never swept; trigonal, hexagonal, orthorhombic, monoclinic and triclinic
  groups are not covered.
- The catalog's novelty statements are catalog-relative: "not matched against the
  records checked as of 2026-09-04". Schmitt's unprinted type data is not
  recoverable; Engel 1981 is print-only and has not been primary-read.
- The tetragonal digitization is a single-pass visual read cross-checked against
  the PDF text layer, not an independent re-key; 30 of 36 cubic tables are
  single-pass.
- Wyckoff letters are recorded for 8 types only; open/wall status for 10.
- The phase-2 store does not carry the phase-1 sightings of cubic-first types; the
  catalog merges the two stores, and the independent recount checks the merge.
- G4 certificates for the 14 tetragonal shortlist types were in progress at build
  time and are marked provisional; their number changes until that run is
  accepted.

## v2 (2026-09-04): hexagonal family folded in; both phase-2 G4 batches accepted

Staging text (subagent #146); Tyler rewrites all prose. Every number below is read
from `catalog.json` v2 (`summary`), `reconciliation_summary.json` v2 or the named
banked document; none is from memory. The v1 text above is preserved unchanged
(append-only); where a v1 number is superseded, the v2 number is given here with its
source. Snapshot language throughout; "new to science" appears nowhere; G4
certification is not novelty; the literature facet maximum is an observed 38.

### Title (v2)

A machine-readable census of 1,583 exact-confirmed plesiohedron combinatorial types
from gated Voronoi sweeps of the 36 cubic, 68 tetragonal and 52 trigonal/hexagonal
space groups

### Abstract deltas (v2)

Three sweeps instead of two: the hexagonal-family sweep (IT 143-194, 52 groups; 4,651
coarse + 676 line orbits; passes P1-P5; 108,580 candidates, 212,912 exact cells;
`harness/PHASE2_HEX_RESULT.md`) adds 692 hexagonal-first types (288 from our own
sample points, 404 seen only at Schmitt's printed points) and re-sights 43 of the 891
prior types, for 1,583 types in all (102 cubic-first, 789 tetragonal-first, 692
hexagonal-first; 196 distinct f-vectors; observed maximum 35 facets, 34 within the
hexagonal family, 24 from our own hexagonal menu). 177 types carry G4 certificates
(tiling, symmetry, Burnside): 12 cubic (accepted 2026-08-30 and 2026-09-03), 14
tetragonal (Gram-metric ladder, accepted 2026-09-04) and 151 hexagonal-family (Gram
metric in the ITA hexagonal basis, accepted 2026-09-04); the two phase-2 batches also
record the solid's chirality (tetragonal 13 chiral / 1 achiral; hexagonal 140 / 11).
The reconciliation now covers all three of Schmitt's printed families: 881 cubic,
1,476 tetragonal and 958 trigonal/hexagonal rows (3,315 rows; 238 distinct f-vectors
across the three, printed maximum 38). Hexagonal family, f-vector level: 1,276 printed
(group, f) pairs (seven enantiomorphic pairs share one table), 510 matched by our menu
(278 at a c/a we also sampled), 40 of ours absent from his table for that group, 766 of
his unreached by our menu (733 of them stored through pass P2 at his own point, 33 IT(180)
rows reproduced by a read-only re-run with the cell already stored, none with no stored
type). Type level: a store-side collision screen of the 288 menu-sighted hexagonal-first
types gives 151 survivors (all 151 certified), 124 collisions (his printed cell
reproduced by our menu: first-realization framing) and 13 unresolved only at IT(180) rows.

### Data records, additions (v2)

| column | meaning | source |
|---|---|---|
| catalog_id | MINT-H001..H692 added for hexagonal-first types; v1 ids unchanged | assigned |
| first_sighting_family, first_sighting_crystal_system, crystal_families_sighted, crystal_systems_sighted | family (cubic / tetragonal / hexagonal) and crystal system (trigonal and hexagonal split) of the first witness and of every sighting | store + spacegroups.json |
| n_sightings_hexagonal(_menu), groups_sighted_hexagonal(_menu), c_over_a_values_hexagonal_menu/all, sighted_by_kinds_hexagonal, schmitt_printed_only_hexagonal | hexagonal-family sightings (b-ratio = c/a in the ITA hexagonal basis) | hexagonal store |
| g4_status | accepted-cubic / certified-tetragonal / certified-hexagonal / none | certificate files on disk, asserted against each results document |
| g4_certificate_file, g4_results_doc, g4_acceptance | the V3 tables file, the results document, the main-session acceptance record | harness/, track4/, STATUS.md, PROGRAM_LEDGER.md |
| g4_chiral_solid (+ _source) | solid chirality from the V2 rung; null for the 12 cubic certificates (rung not recorded there) | G4_PHASE2_RESULTS.md, g4p2hex_cells/<id>.json == G4_PHASE2_HEX_RESULTS.md |
| g4_chiral_honeycomb | every point operation of the honeycomb's symmetry group is proper (n_improper == 0 in the tables file); all 177 certificates | tables files |
| schmitt_fvector_printed_anywhere_hexagonal | trigonal/hexagonal groups whose table prints the f-vector | hexagonal digitization |
| schmitt_match_hexagonal | SURVIVOR / COLLISION / UNRESOLVED for the 288 menu-sighted hexagonal-first types (re-derived from the store and asserted against the triage document), S-cell for the 404 printed-only, f-vector-level note for the 43 prior types re-sighted in the family, n/a otherwise | store, digitization, TRIAGE_PHASE2_HEX_RESULT.md |

Sidecar `catalog_sightings.json.gz`: 258,521 sightings (1,597 cubic orbit records +
148,390 tetragonal + 108,534 hexagonal-family); each carries crystal_system, and
hexagonal P2 sightings carry his point as printed (B'' basis), the conversion used (H1 or
H1 with z -> -z), the primary group of the shared table and the PDF page. Committed
forms: `catalog.json.gz`, `catalog.csv.gz`, `catalog_sightings.json.gz`, all hashed in
`catalog.SHA256SUMS` (the raw `catalog.json` is 9.2 MB).

Summary numbers (v2): 1,583 types = 102 + 789 + 692; 7 seeded (1 never sighted); 43
prior types re-sighted in the hexagonal family (17 cubic-first, 26 tetragonal-first);
types with at least one sighting: cubic 99, tetragonal 808, hexagonal family 735; 196
distinct f-vectors (65 / 153 / 167 by first family); G4 177 = 12 + 14 + 151; chiral
solids where recorded 153 / 12; chiral honeycombs 138 of 177; Schmitt type-level SAME
1,125 / DIFFERENT 449 / unchecked 9; f-vector flag over sighted groups P 1,568 / A 14 /
n/a 1; exactly one f-vector of ours, (20,36,18) (hexagonal-first, IT(178) at c/a = 3/2,
certified), is printed in none of his tables in any of the three digitized families.

### Technical validation (v2 paragraph)

1. G3 (store invariant) for every non-seeded type in all three stores; batch-2
   quarantines 46, all IT(180) rows explained by Schmitt's own normalizer remark and
   reproduced by the read-only re-run (`PHASE2_HEX_SCHMITT_180_CHECK.md`), none stored.
2. G2c pre-registered controls for the hexagonal family (hexagonal prism; rhombohedral-
   lattice brackets including the cube transition; six printed rows including his
   34-facet maximum), accepted 2026-09-04 (`phase2/G2C_RESULT.md`).
3. G4 for 177 types across two phase-2 batches (14 tetragonal, 151 hexagonal) plus the
   12 cubic; each batch re-run in full by the operator's main session with exit 0
   before acceptance (`harness/G4_PHASE2_RESULTS.md`, `harness/G4_PHASE2_HEX_RESULTS.md`).
4. G5 records: 1,476 tetragonal + 958 trigonal/hexagonal digitized rows (the latter:
   text layer primary, 153 rows visually cross-read, 0 discrepancies; NOT yet
   independently re-keyed); 1,276/1,276 (row x group) hexagonal evaluations reproduce
   their printed f-vector (1,230 verbatim + 46 read-only); the three digitizations total
   3,315 rows with 238 distinct f-vectors and printed maximum 38, equal to the totals
   Schmitt's text states for his survey.
5. Independent recount v2 (`verify_counts_independent.py`, no shared code with the
   builder): recounts every headline, per-family, per-group, per-G4-status and chirality
   number from the three raw stores, the certificate files and the two G4 documents,
   re-derives every type id from its code, checks Euler and the p-vector identities for
   all 1,583 types and asserts equality with `catalog.json`: 0 failures, exit 0.
6. Determinism: two consecutive builds give byte-identical `catalog.json`, `catalog.csv`,
   their .gz forms and the sightings sidecar (`catalog.SHA256SUMS`); `RECONCILIATION.md`
   preserves the v1 text byte for byte and its cubic/tetragonal headline numbers are
   asserted equal to those recomputed from the v2 catalog.
7. Reconciliation, hexagonal family (`RECONCILIATION.md` v2 section): 1,276 printed
   (group, f) pairs from 958 rows; 510 matched (278 at a shared c/a; 728 of our
   sightings), 40 absent, 766 unreached (733 via P2, 33 read-only, 0 unstored);
   whole-family distinct f-vectors his 177 / ours 95 / shared 94; his f-vectors unreached
   by our menu anywhere in the family 83 (0 counting P2 and the read-only rows).

### Limitations (v2)

- Sampling, not enumeration, in all three families; the hexagonal menu reached 9 of his
  38 printed b-ratios (5 sampled directly); orthorhombic, monoclinic and triclinic groups
  are not covered.
- Hexagonal G5 diligence is still owed: the trigonal/hexagonal digitization is a
  single-pass text-layer parse with a 16 % visual cross-read, not an independent re-key
  (in progress as a blind re-key); no perturbation (open/wall) certificates exist yet
  for any phase-2 certified cell (the open_wall column covers 10 cubic/tetragonal types
  only); the 43 prior types re-sighted in the family were not collision-screened there.
- Print-only exposure: Engel 1981 and Koch's tables are print-only and have not been
  primary-read; this applies to the cubic finalists and equally to the hexagonal groups.
- Solid chirality is recorded only where a certificate's V2 rung reports it (the 165
  phase-2 certificates); the 12 cubic certificates carry the honeycomb-level fact only.
- Novelty statements remain catalog-relative: "not matched against the records checked
  as of 2026-09-04"; Schmitt's unprinted type data is not recoverable.

## v3 (2026-09-04): computed open/wall verdicts and type-level Schmitt status folded in

Staging text (subagent #150, Claude Fable 5.1); Tyler rewrites all prose. Every number
below is read from `catalog.json` v3 (`summary`), `reconciliation_summary.json` v3 or the
named banked document; none is from memory. The v1 and v2 text above is preserved unchanged
(append-only). Snapshot language throughout; OPEN means "holds on the tested neighbourhood";
SURVIVOR is catalog-relative and never novelty; no type is named.

### Data records, additions (v3)

| column | meaning | source |
|---|---|---|
| open_wall_verdict | OPEN / WALL / ONE-SIDED / not-computed: the computed perturbation verdict at the stored first witness; 172 computed (7 cubic finalists + 165 G4-certified phase-2 cells), 1,411 not-computed | harness/phase2/WALL_OPEN_PHASE2.json (cells[].combined_verdict); harness/round1_computations/c1_wall_open.json (.verdict) |
| open_wall_verdict_source | c1 cubic / phase2 #148 / none (the v2 column `open_wall_source` already exists and is kept verbatim, hence the name) | same |
| open_wall_point_verdict, open_wall_metric_verdict | the POINT (stratum directions) and METRIC (c/a) verdicts separately; metric n/a for cubic; point n/a at stratum dimension 0 | WALL_OPEN_PHASE2.json |
| open_wall_flags | the true flags among degenerate_flag_any, float_superseded_any, line_isolated, nonsimple_vertex, quarantine_any, stab_change_any (recorded, never verdict inputs); null for c1 cells and not-computed types | WALL_OPEN_PHASE2.json cells[].flags |
| open_wall_verdict_pointer | file + record pointer, doc rank, wall directions, the previous heuristic label with its agreement flag, and the acceptance record | WALL_OPEN_PHASE2.md; PROGRAM_LEDGER 2026-09-04 14:10 (phase 2) / 2026-09-03 (c1) |
| open_wall_scheme, open_wall_scheme_date | the perturbation scheme as text and its date: 2026-09-04 (pre-registered in ANCHORS.md before the run) or 2026-09-03 (c1 round, not pre-registered) | ANCHORS.md 'PERTURBATION CLASSIFICATION, PHASE 2'; c1_wall_open.md |
| schmitt_type_status | SURVIVOR / COLLISION / UNRESOLVED / printed-only / not-screened, from the two phase-2 collision screens | COLLISION_PHASE2_RESULTS.md (tetragonal top-15, 27 printed pairs), COLLISION_PHASE2_HEX_RESULTS.md (the 288 menu-sighted hexagonal-first types), the stores' schmitt_printed_only flags |
| schmitt_type_status_source | the doc pointer, rank and pair counts behind the status | same |

Summary blocks added: `open_wall_verdict_counts`, `open_wall_verdict_source_counts`,
`schmitt_type_status_counts`, `open_wall_x_schmitt_type_status` (per first-sighting family)
and `naming_pool` (certified AND OPEN AND unnamed, with the ids). Every v1/v2 column keeps its
name, position and value (0 differences over 1,583 rows x 78 columns against the v2 file); the
CSV header is the v2 header plus the ten new columns. Committed forms as in v2 (`catalog.json.gz`
0.84 MB, `catalog.csv.gz` 0.56 MB, `catalog_sightings.json.gz` byte-identical to v2), hashed in
`catalog.SHA256SUMS`; the raw `catalog.json` is 10.7 MB and `catalog.csv` 5.5 MB (both ignored).

Summary numbers (v3): verdicts - tetragonal-first 13 OPEN / 1 WALL; hexagonal-first 102 OPEN /
40 WALL / 9 ONE-SIDED; cubic finalists 6 OPEN / 1 WALL (the Satchelhedron); all other types
not-computed. Type-level status - tetragonal-first 14 SURVIVOR / 1 COLLISION / 385 printed-only /
389 not-screened; hexagonal-first 151 SURVIVOR / 124 COLLISION / 13 UNRESOLVED / 404 printed-only;
cubic-first 102 not-screened (the phase-2 screens cover phase-2-first types only). Every certified
phase-2 cell is a SURVIVOR (the certificate sets equal the screens' survivor sets). Naming pool:
13 tetragonal + 102 hexagonal-family + 0 cubic (the six OPEN cubic cells already carry a program
name, a descriptive package name or a HELD marker).

### Technical validation (v3 paragraph)

8. Pre-registered perturbation classification (`harness/phase2/WALL_OPEN_PHASE2.json`, agent
   #148; scheme appended to ANCHORS.md BEFORE the run): each of the 165 G4-certified phase-2
   cells was perturbed at its stored first witness along the tangent basis of its Wyckoff
   stratum (steps 1/48 and 1/96 in fractional coordinates of the ITA conventional cell, halved
   to 1/1536 on any side whose smallest step changed the type) and in the metric direction
   c/a -> c/a(1 + eps), eps = 1/96 and 1/192 relative, halved to 1/3072, through the accepted
   exact chain imported unchanged (3,879 exact evaluations, 0 quarantines, kill bar live). A
   direction is WALL when both of its sides change at the finest step; OPEN = every side SAME;
   ONE-SIDED = otherwise. Regression: the three top-3 tetragonal POINT verdicts equal the
   earlier absolute-step run (COLLISION_PHASE2_RESULTS.md). Determinism: sorted keys, no
   timings; the operator's main session re-ran the classification fresh, reproduced the JSON
   md5 (6b257c551f6fb275dfabb03e992f57c2) and accepted it 2026-09-04 14:10. The heuristic
   open-likely / wall-suspect / indeterminate labels of the triage documents disagreed with the
   computed verdict on 35 of the 165 cells, in both directions, and are retired for naming
   purposes; the catalog carries the computed verdict and keeps the label only inside the
   pointer column.
9. Before use the builder asserts: the JSON md5 equals the value its results document states;
   its store hashes equal the two verified stores and were unchanged after the run; its 165 ids
   equal the certificate files on disk; its per-family verdict counts equal its own aggregate
   block; witness point, c/a, group, f-vector, automorphism order and stratum dimension equal
   the stores; the 7 cubic c1 verdicts equal the v1/v2 open_wall head tokens; the tetragonal
   per-target status equals the 'Summary per shortlist type' lines of
   COLLISION_PHASE2_RESULTS.md; the hexagonal counts equal both collision_phase2_hex_results.json
   and the section-1 line of COLLISION_PHASE2_HEX_RESULTS.md, and the top-10 post-screen block
   equals the document.
10. Independent recount (`verify_counts_independent.py` v3, no code shared with the builder):
    rebuilds every per-row v3 value and every v3 summary block from the raw verdict, screen and
    certificate files and from the publication folder names (the only naming record), and
    asserts the naming pool equals 13 + 102: 0 failures, exit 0.
11. Determinism (v3): two consecutive builds byte-identical on all five catalog files;
    RECONCILIATION.md and reconciliation_summary.json byte-identical across two reconcile runs;
    the v1 + v2 text of RECONCILIATION.md asserted equal to the sections regenerated from the v3
    catalog before the v3 section is appended.

### Limitations (v3)

- First witness only: every verdict describes the stored first witness (one point, one c/a) of
  the type; the type's other sightings were not perturbed; a WALL witness does not preclude an
  open region of the same type elsewhere, and an OPEN witness does not certify one.
- Finite steps: 1/1536 (point) and 1/3072 relative (metric) are the finest steps tested. OPEN
  means the type held on the tested neighbourhood; ONE-SIDED means one side changed at the
  finest step (a short neighbourhood, not a wall); neither is an interval proof. The relative
  metric step is coarser than 1/96 absolute for the five cells with c/a > 2 (listed in
  WALL_OPEN_PHASE2.md).
- Non-simple vertices at the witness are not a wall criterion (40 of the 41 wall cells have
  them, but so do 36 OPEN cells); flags are recorded, never verdict inputs.
- The tetragonal collision screen covered the top-15 shortlist only, so 389 menu-sighted
  tetragonal-first types are not-screened; 176 of them are S-cells (type-level SAME by pass P2,
  recorded in schmitt_type_level_status) and would be COLLISION under the hexagonal screen's
  store-side rule, which was not run on the tetragonal family. Cubic-first types are
  not-screened by the phase-2 screens by construction (their cubic-round verdicts stay in the
  schmitt_type_level_* columns).
- The hexagonal-family statuses rest on a single-pass digitization until the blind re-key
  (agent #147) is accepted; a changed row can move a type between SURVIVOR, COLLISION and
  UNRESOLVED.
- Naming-pool membership is catalog-relative ("not matched against the records checked as of
  2026-09-04"); G5 diligence for print-only records (Engel 1981, Koch) still applies to every
  pool member before any name; no name is proposed here.

## v4 (2026-09-04): tetragonal type-level Schmitt status under the store-side rule (both phase-2 families consistent)

Appended by subagent #152 (Claude Fable 5.1); provisional until the main session re-runs the four
commands in catalog/STATUS.md (v4 entry). No column is added or renamed; the schmitt_type_status
column now carries the same semantics for both phase-2 families. v3 of the three scripts =
`git show e01618b:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`.

### Data records, changes (v4)

- schmitt_type_status (tetragonal-first, 404 menu-sighted types): v3's 'not-screened' (389) is
  replaced by the store-side screen verdict of harness/collision_phase2_tetragonal_storeside.json,
  i.e. the hexagonal screen's rule (COLLISION_PHASE2_HEX_RESULTS.md section 1) applied to the
  tetragonal family after its equivalence on the hexagonal family was asserted (151/124/13, per
  type). Values: SURVIVOR 121 / COLLISION 177 / UNRESOLVED 106 / printed-only 385 / not-screened 0.
  The 15 shortlist statuses (14 SURVIVOR = the 14 certificates, 1 COLLISION) are unchanged.
- schmitt_type_status_source: per type, the addendum pointer, the S-cell fact or the per-group
  [same/other/unres] resolution of the printed rows at its (group, f), and the unresolved-row count.
- summary.schmitt_type_status_tetragonal_storeside: pure-rule counts (176/116/112), overlaid counts
  (177/121/106), v3 counts, transitions, JSON md5; inputs.collision_screen_tetragonal_storeside_v4:
  file, md5, sha256. Exactly 404 rows differ from the v3 catalog, in those two columns only.

### Technical validation (v4 paragraph)

12. Rule equivalence: the store-side rule is re-implemented as a pure function and run on the
    hexagonal family BEFORE the tetragonal family; it must reproduce the accepted hexagonal screen
    (SURVIVOR 151 / COLLISION 124 / UNRESOLVED 13; per-type verdict equal to the triage table for
    all 288; survivor ranking identical). verify_counts_independent.py re-implements the rule a
    second time (no shared code) and asserts the same, then re-derives all 404 tetragonal verdicts
    (pure rule and with the 27 recomputed pairs overlaid) and asserts them equal to the JSON, to
    every catalog row, and the JSON md5 equal to the value stated in the results addendum.
13. Overlay: a printed pair recomputed SAME TYPE in COLLISION_PHASE2_RESULTS.md makes its target
    COLLISION; a pair recomputed DIFFERENT TYPE on an unstored row resolves that row. Both the
    pure-rule and the overlaid verdict are stored per type; the zero-disagreement check against the
    15 shortlist summary lines is asserted in three places (harness script, builder, verifier).

### Limitations (v4)

- UNRESOLVED (106 tetragonal types) means a printed row at the type's (group, f) was never stored
  (rows quarantined in the sweep: two-origin groups, the second enantiomorphs 95/96, IT(80)) and
  has not been recomputed; it is neither survivor nor collision. A recomputation pass with the
  documented conversions, as done for the shortlist's 27 pairs, would resolve them.
- COLLISION under the rule = the type reproduces one of Schmitt's printed cells (first-realization
  reframe), not a statement about his unprinted data; SURVIVOR = catalog-relative ("not matched
  against the records checked as of 2026-09-04"), never novelty.
- The tetragonal digitization remains a single visual pass, text-layer cross-checked, not
  independently re-keyed; a changed row can move a type between the three statuses.
- The v3 'Limitations' bullet on the tetragonal screen covering the top-15 only is superseded by
  this section; the v3 text is kept verbatim above as the pre-rule record.

## v5 (2026-09-04): the 62 unstored tetragonal printed rows recomputed; the 106 UNRESOLVED settled

Appended by subagent #154 (Claude Fable 5.1); provisional until the main session re-runs the four
commands in catalog/STATUS.md (v5 entry). No column is added or renamed. v4 of the three scripts =
`git show 27e0083:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`.

### Data records, changes (v5)

- schmitt_type_status (tetragonal-first, the 106 types UNRESOLVED in v4): the 62 printed rows they hung
  on (rows pass P2 could not store: Schmitt's origin-choice-2 / second-enantiomorph coordinates, and the
  IT(80) crash row) were recomputed at the printed points with the documented setting conversions
  (harness/collision_phase2_tetragonal_rows_recompute.py; every computed cell in
  collision_phase2_tetragonal_rows_recomputed.json, the verdicts in
  collision_phase2_tetragonal_unresolved_overlay.json; dated addendum in COLLISION_PHASE2_RESULTS.md).
  All 62 rows reproduce their printed f-vector (one canonical code across the documented conventions of
  each row). Rule: any hung-on row SAME -> COLLISION (24); all DIFFERENT -> SURVIVOR (82); none stays
  UNRESOLVED. Tetragonal values: SURVIVOR 203 / COLLISION 201 / UNRESOLVED 0 / printed-only 385 /
  not-screened 0. The 15 shortlist statuses (14 SURVIVOR = the 14 certificates, 1 COLLISION) are unchanged.
- schmitt_type_status_source: those 106 rows gain a [v5] clause naming each recomputed row (group, b, point,
  PDF page), its verdict and the row cell's canonical-code id (stored id where the cell is a stored type).
- summary.schmitt_type_status_tetragonal_unresolved_recomputed: md5s of both JSONs, row status counts, cells
  computed (306), the classification of row cells that are stored types outside the 106, counts before / after,
  transitions, still_unresolved (empty), secondary hits and the recorded facts; inputs.collision_screen_
  tetragonal_rows_recomputed_v5: both files with md5 + sha256. Exactly 106 rows differ from the v4 catalog, in
  those two columns only.

### Technical validation (v5 paragraph)

14. Row reproduction: every recomputed cell went through the accepted exact chain with the certificate
    asserted (4*rho^2 <= D^2 on cell 0 and a second orbit cell, Euler, float/exact agreement, orbit
    congruence, stab | aut); a row counts as reproduced only if the printed f-vector comes back under a
    documented convention and every documented convention that reproduces it gives the same canonical code.
    The other origin / enantiomorph reading was run for every two-origin / 95 / 96 row and recorded; it
    reproduced the printed f-vector in 0 of 62 rows, which is exactly pass P2's quarantine record.
15. Three-way agreement: the harness script derives the 106 verdicts; build_catalog.py re-derives them from
    the rows file and the store's canonical codes and asserts equality with the overlay JSON; verify_counts_
    independent.py re-derives them a third time with its own keying and asserts equality with the overlay
    JSON, every catalog row, and the md5s stated in the results addendum and the catalog.

### Limitations (v5)

- SURVIVOR is now type-level at every printed representative of a menu-sighted tetragonal type's (group,
  f) pairs, but remains catalog-relative: Schmitt prints ONE point per (group, f) from a grid sampling, so
  a type absent at his printed point may occur in his unprinted data. COLLISION = the type reproduces one of
  his printed cells (first-realization reframe).
- Two of the 62 recomputed rows are cubic-store types (the accepted-cubic Laves-cell type at IT(95) b =
  797/1000 and the elongated-dodecahedron-type cell at IT(137) b = 3497/1000); recorded as cross-system facts,
  not folded into schmitt_type_status (cubic-first types stay not-screened by construction).
- The tetragonal digitization remains a single visual pass, text-layer cross-checked, not independently
  re-keyed; the setting conversions are the machine-verified ones of PHASE2_SCHMITT_ORIGIN_CHECK.md.
- The v4 'Limitations' bullet on UNRESOLVED is superseded by this section; the v4 text is kept verbatim above.
