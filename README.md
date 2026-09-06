# plesiohedron-census

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22502081.svg)](https://doi.org/10.5281/zenodo.22502081)

Archived at Zenodo: version DOI 10.5281/zenodo.22502081, concept DOI 10.5281/zenodo.22502080 (all versions). Cite the version DOI for the catalog v5 snapshot of 2026-09-04.

Certified space-filling polyhedra from a gated agentic search: code, certificates, catalog.

A plesiohedron is the Voronoi cell of a point orbit under a crystallographic space group;
every plesiohedron tiles space isohedrally. This repository is the complete public record of
a search for their combinatorial types across the 36 cubic, 68 tetragonal and 52
trigonal/hexagonal space groups (IT 75-230; the 36 cubic groups are IT 195-230): the exact-arithmetic harness, the frozen
space-group operation store, the pre-registered gates and every gate result, the per-cell
certificates, the digitized comparison tables, and the resulting machine-readable catalog
(version 5, snapshot 2026-09-04).

Everything here was produced by a pipeline that had to re-derive the known before it was
allowed to look for anything else, and every result document names the command that
reproduces it. Nothing in this repository claims a shape is new to science; the strongest
statement made anywhere is that a type is "not matched against the records checked as of
2026-09-04" (see "Wording" below).

## The census in numbers (catalog v5)

| quantity | value | source |
|---|---|---|
| combinatorial types in the catalog | **1,583** (102 cubic-first, 789 tetragonal-first, 692 hexagonal-first) | `catalog/catalog.json.gz` summary block |
| distinct f-vectors | 196 | same |
| most facets observed in this census | 35 (tetragonal); literature observed maximum 38 (Schmitt 2016), refereed bound 92 | same; `ANCHORS.md` G5 amendment |
| exact Voronoi cells computed | 1,597 cubic orbits; 294,772 tetragonal; 212,912 trigonal/hexagonal | `harness/PHASE1_RESULT.md`, `PHASE2_RESULT.md`, `PHASE2_HEX_RESULT.md` |
| G4-certified cells (tiling + symmetry + Burnside certificates) | **177** = 12 cubic + 14 tetragonal + 151 trigonal/hexagonal | `harness/G4_RESULTS.md`, `G4_PHASE2_RESULTS.md`, `G4_PHASE2_HEX_RESULTS.md`, `track4/` |
| open / wall classification of the 165 phase-2 certified cells | 115 OPEN, 41 WALL, 9 ONE-SIDED (on the tested neighbourhood) | `harness/phase2/WALL_OPEN_PHASE2.md` |
| f-vector reconciliation against Schmitt's printed per-group tables (matched / ours absent from his table for that group / his rows unreached by our sample) | cubic 292 / 33 / 694; tetragonal 700 / 67 / 939; trigonal-hexagonal 510 / 40 / 766 | `catalog/RECONCILIATION.md` |
| type-level status of menu-sighted phase-2 types at every printed representative point | tetragonal 201 COLLISION / 203 SURVIVOR / 0 UNRESOLVED (of 404); hexagonal family 124 / 151 / 13 (of 288) | `harness/COLLISION_PHASE2_RESULTS.md`, `COLLISION_PHASE2_HEX_RESULTS.md` |
| digitized rows of Schmitt's 2016 tables | 881 cubic, 1,476 tetragonal, 958 trigonal/hexagonal (the last blind re-keyed, 0 discrepancies) | `SCHMITT_*_DIGITIZATION_2026-09-04.md`, `SCHMITT_HEXAGONAL_REKEY_2026-09-04.md` |

"Ours absent from his table" is evidence, not proof: Schmitt's survey is a grid sampling
that prints one representative point per (group, f-vector), not an enumeration. "His rows
unreached" measures the coverage of our sample points, not of his.

Related machine-readable data (added 2026-09-05). Ed Pegg has assembled, in a Wolfram Cloud
notebook (https://www.wolframcloud.com/obj/5a7894fc-4cd0-439f-9d83-25d28bb47b37), a database of
3,903 plesiohedra taken from Schmitt's printed tables, with generated geometry. That count equals
our own per-group expansion of his 3,315 printed rows (986 cubic + 1,641 tetragonal + 1,276
trigonal/hexagonal (group, row) pairs, `catalog/RECONCILIATION.md`), so it is a machine-readable
form of the printed representative points. This catalog is a different object: deduplicated
combinatorial types with canonical identifiers, every sighting attached, certificates for 177 and a
type-level reconciliation, of which 794 types come from our own point menus. The notebook returned
HTTP 503 at every fetch on 2026-09-05 (a scheduled Wolfram Cloud outage), so its description here is
as relayed to the author and will be re-verified. No statement in this repository claims to be the
first machine-readable form of anything; the claim made is "to our knowledge the first catalog of
exact-confirmed types with certificates and a type-level reconciliation", dated 2026-09-05.

## The two named cells

Two cubic cells carry names (`NAMING_DECISION_BRIEF_2026-09-01.md`); the other certified
cells carry systematic labels (group, f-vector, canonical type id).

| name | group | f-vector | facets | symmetry | package |
|---|---|---|---|---|---|
| **Satchelhedron** | IT 220, I-43d, generating point (0, 0, 1/4) | (16, 25, 11) | 3^2 4^1 5^8 | aut 4, site 2 | `publication/8cf50403_Satchelhedron/` |
| **Ordenhedron** | IT 201, Pn-3, generating point (1/8, 1/6, 5/12) | (20, 33, 15) | 3^6 4^3 5^2 6^2 7^2 | aut 1 (trivial) | `publication/2de0a211_Ordenhedron/` |

Diligence scope for both, stated once: each passed the V0-V3 certificate ladder
(`harness/G4_RESULTS.md`), its polyform counts to n = 6 were reproduced by a second,
independently written enumerator (`publication/INDEPENDENT_COUNTS_2026-09-03.md`, 72/72),
and its combinatorial type was compared against the seeded classical catalog, Bernhard
(arXiv:2604.07160), and Schmitt's 2016 printed tables at f-vector level and, at every
printed representative point of its (group, f-vector) pairs, at type level
(`G5_DILIGENCE_2026-08-30.md`, `harness/SCHMITT_COLLISION_RESULTS.md`,
`catalog/SATCHELHEDRON_TETRAGONAL_ROWS.md`). The Satchelhedron's f-vector is absent from
Schmitt's printed cubic survey; it is printed in two tetragonal tables, IT(134) and IT(141),
and both of those rows were recomputed exactly and are different types. Two print-only
catalogs (Engel 1981, Koch 1972) had not been read at the time of this release; three
further cubic cells whose groups fall in that ground (IT 212, 214, 230) are included as
certified-but-held and are deliberately unnamed.

## What is in the tree

| path | contents |
|---|---|
| `ANCHORS.md` | the pre-registered gates G0-G5, kill criteria, and the later pre-registered blocks (G2b, G2c, perturbation classification), each written before its computation ran |
| `STATUS.md`, `PROVENANCE.md`, `VERIFICATION_INDEX.md` | the attempt-level scorecard, the model-per-block provenance record, and the pointer index of every result document |
| `HARNESS_DESIGN_FABLE5_2026-08-27.md`, `PROGRAM_PLAN_2026-08-27.md`, `PHASE2_PLAN.md` | design and plan documents |
| `harness/` | the exact-arithmetic pipeline: `spacegroup_ops.py` + frozen `spacegroups.json` (230 groups, 4,425 operations, exact rationals; confirmed operation by operation against Schmitt's 2016 derivation, zero discrepancies on all 229 comparable groups), `orbit.py`, `sweep_voronoi.py` (float proposal), `exact_cell.py` (exact rational confirmation), `canon_code.py`, the phase-1 cubic sweep and triage, the gate scripts (`g0_regression.py`, `audit_g1.py`, `g2_controls.py`, `g4_certify*.py`, `g5_rekey_check.py`), the Schmitt cross-checks, the phase-2 sweeps (`sweep_phase2_tetragonal.py`, `sweep_phase2_hexagonal.py`), every `*_RESULT(S).md`, the type stores (`phase1_types.json`; `phase2_types.json.gz`, `phase2_hexagonal_types.json.gz` with `*.SHA256SUMS`), the digitized Schmitt tables (`schmitt_*_tables.json`, `schmitt_hexagonal_rekey.json`), and the per-cell certificates `g4_tables_*`, `g4p2_tables_*`, `g4p2hex_tables_*` (+ `_indep.json` independent-enumerator records) |
| `harness/phase2/` | Gram-metric modules (`metric.py`, `sweep_voronoi_gram.py`, `exact_cell_gram.py`), metric controls (`g2b_controls.py`, `g2c_controls.py`), the computed open/wall classification (`wall_open_phase2.py`, `WALL_OPEN_PHASE2.{md,json}`, `wall_open_cells/`), the pre-registered pool ranking and nice-point search with their JSON outputs |
| `harness/round1_computations/`, `round2_computations/` | exact computations answering the cold reviews of the seven-cell paper (wall/open on the Wyckoff stratum, isometry groups, roundness under both conventions, Schmitt grid membership) |
| `publication/` | one package per certified cubic finalist: `COORDS.md` (exact vertex coordinates), `render.png`, banked `g4_tables_<id>.json/.txt`, `counts.md`, OEIS draft texts and a-files where applicable; `build_packages.py` regenerates all of it; `independent_runs/` and `verify_counts_independent.py` are the second-implementation count checks |
| `track4/` | G4 certificates for two literature cells rediscovered by the sweep (the Laves-graph plesiohedron, Engel's 38-facet stereohedron) |
| `catalog/` | THE CATALOG v5: `catalog.json.gz`, `catalog.csv.gz`, `catalog_sightings.json.gz`, `catalog.SHA256SUMS`; `build_catalog.py`, `reconcile_schmitt.py`, `verify_counts_independent.py` (shares no code with the builder), `RECONCILIATION.md` (append-only across versions), `DATA_DESCRIPTOR_DRAFT.md`, `STATUS.md`, `reconciliation_*.csv/json` |
| `SCHMITT_*.md` | primary read, data-recovery provenance (Software Heritage identifiers), operation cross-check, and the three digitization/re-key reports |

Not included, on purpose: the raw uncompressed stores (> 5 MB; every one has a committed
`.gz` twin whose decompressed SHA-256 is in the `SHA256SUMS` files), the 90 MB nice-point
cell caches (regenerable), the manuscript drafts, the third-party PDFs (cite: Schmitt
doi:10.17169/refubium-14374; Bernhard arXiv:2604.07160; the Schmitt repository recovery is
referenced by its Software Heritage identifiers in `SCHMITT_DATA_RECOVERY_2026-08-28.md`),
and the compiled polyform enumerator (its source is the OEIS A398957 a-file).

## The gate chain in one paragraph

G0 regression: the harness had to reproduce the Josehedron (Bernhard 2026) from its
generating orbit, with tables semantically equal to the banked A398957 record, before
anything else ran. G1: the frozen space-group store passes identity, exact closure, inverses
and ITA order for all 230 groups under a checker sharing no code with the generator, and
was then confirmed operation by operation against an independently derived 2016 store.
G2 (and G2b, G2c for the tetragonal and hexagonal metrics): the sweep must return the cube,
rhombic dodecahedron, truncated octahedron and hexagonal prism at the lattice orbits where
they are known to sit, on both sides of every metric transition that was predicted, with
the prediction recorded before the run and one recorded as wrong. G3: no type enters a store
unless the exact rational re-derivation agrees with the float proposal on facet count,
facet-size multiset and canonical code. G4: any cell advanced toward naming passes V0 exact
re-derivation, V1 tiling certificate verified by an independent adapted audit, V2 symmetry
certification over all orthogonal maps with the Bravais group of the actual lattice, and V3
the Burnside identity on its polyform counts. G5: novelty diligence against the seeded
catalog, Schmitt's tables at f-vector and type level, Bernhard, and (pending) the print-only
catalogs, with wording fixed in advance. A failed gate quarantines everything downstream.

## How to verify

Python 3.13 (3.10+ should work). The exact chain, the certificates and the catalog scripts
use the standard library only. `numpy` and `scipy` are needed for the float Voronoi proposal
inside the sweeps and the phase-2 controls, `spglib` only to regenerate `spacegroups.json`
(the frozen file is committed) and for three round-1/2 computations, `matplotlib` only for
`publication/build_packages.py` renders.

```sh
git clone https://github.com/Tyorden/plesiohedron-census
cd plesiohedron-census
python3 -m pip install numpy scipy            # only for the sweep-side checks below

# 0. Recreate the raw stores and the raw catalog from their committed .gz twins.
gunzip -k harness/phase2_types.json.gz harness/phase2_hexagonal_types.json.gz
gunzip -k catalog/catalog.json.gz catalog/catalog.csv.gz
shasum -a 256 harness/phase2_types.json harness/phase2_hexagonal_types.json catalog/catalog.json catalog/catalog.csv
#    Expected: 71685b9a..., 7494c7b2..., 4768f18b..., a83a205e... exactly as listed in
#    harness/phase2_types.SHA256SUMS, harness/phase2_hexagonal_types.SHA256SUMS and catalog/catalog.SHA256SUMS.

# 1. Independent recount of every catalog number (no shared code with the builder).
#    Expected: "0 failures", exit 0. Seconds.
python3 catalog/verify_counts_independent.py

# 2. Metric controls, hexagonal family (pre-registered G2c). Expected: exit 0, ~6 s.
(cd harness/phase2 && python3 g2c_controls.py)

# 3. Deterministic triage recount, hexagonal family. Expected: exit 0 and
#    harness/TRIAGE_PHASE2_HEX_RESULT.md byte-identical.
(cd harness && python3 triage_phase2_hexagonal.py)

# 4. Open/wall classification of all 165 phase-2 certified cells. Expected: exit 0
#    (exit 3 = time budget reached: re-run without --fresh to resume) and
#    md5 of WALL_OPEN_PHASE2.json = 6b257c551f6fb275dfabb03e992f57c2. ~90 s on 8 cores.
(cd harness/phase2 && python3 wall_open_phase2.py --fresh --jobs 8 --budget-s 540; md5 -q WALL_OPEN_PHASE2.json)

# 5. Pool ranking (pre-registered scoring). Expected: exit 0, md5 75cacf7e762bda859234d2843888cb94. ~70 s.
(cd harness/phase2 && POOL_JOBS=6 python3 pool_ranking_2026-09-04.py; md5 -q POOL_RANKING_2026-09-04.json)

# 6. Nice-point search. Expected: exit 0, md5 cf6645fcbb96a530cbb71a2d20bb325a. ~18 min, 8 workers.
(cd harness/phase2 && NICE_JOBS=8 python3 nice_points_2026-09-04.py; md5 -q NICE_POINTS_2026-09-04.json)

# 7. G4 certificates, hexagonal family (151 cells). Expected: exit 0 and, with timings masked,
#    md5 of G4_PHASE2_HEX_RESULTS.md = 4fee579c8f6faf69b47818a86fb71525 (the committed copy; the
#    value 9a84d24be576713a002d4f0387839760 quoted in STATUS.md is the same document before the
#    local absolute path in its final "Re-run for acceptance" line was replaced by <repo>). ~8 min.
(cd harness && python3 g4_certify_hex.py --fresh --budget-s 420; rc=$?; while [ $rc -eq 3 ]; do python3 g4_certify_hex.py --resume --budget-s 420; rc=$?; done; echo exit $rc; python3 g4_certify_hex.py --resume --mask-timings && md5 -q G4_PHASE2_HEX_RESULTS.md; python3 g4_certify_hex.py --resume)

# 8. G4 certificates, tetragonal gates only. Expected: exit 0.
(cd harness && python3 g4_certify_gram.py --gate-only)

# 9. The 62 unstored tetragonal printed rows recomputed at Schmitt's points. Expected: exit 0 and the line
#    "rows JSON md5 4d27ce41466509feab6a180249330af7; overlay JSON md5 a3716a2330c6dbe9c93414dfe8e832ee;
#     addendum appended: False; correction appended: False; store sha unchanged: True". ~45 s.
(cd harness && python3 collision_phase2_tetragonal_rows_recompute.py)

# 10. Rebuild the catalog and reconcile. Expected: exit 0 each; catalog/catalog.SHA256SUMS,
#     RECONCILIATION.md and reconciliation_summary.json unchanged (git status clean for those three).
python3 catalog/build_catalog.py && python3 catalog/reconcile_schmitt.py && python3 catalog/verify_counts_independent.py
```

The phase-1 gates (`harness/g0_regression.py`, `audit_g1.py`, `g2_controls.py`) and the
seven-cell package builder record their expected outputs in `harness/G0_RESULT.md`,
`G1_RESULT.md`, `G2_RESULT.md` and `publication/PUBLICATION_STATUS.md`; G0 additionally
needs the Josehedron tables from the A398957 record, which are not part of this repository.
Every determinism claim above was established by two fresh runs and re-run once more by the
author, separately from the agent that wrote the script, before the result was accepted
(`STATUS.md`, "MAIN-SESSION RE-RUN" lines).

## Wording

Every statement about a type's novelty in this repository is catalog-relative by rule:
"not matched against the records checked as of <date>". Survival of every printed
representative is evidence, never proof; "new to science" appears nowhere. The literature
facet maximum of 38 is an observed value from Schmitt's exact sampling, not a proven bound
(the refereed bound is 92). "OPEN" means the type holds on the tested neighbourhood of the
witness, never on an interval. Absence claims carry their scope noun ("absent from
Schmitt's printed cubic survey").

## Disclosure

The software, gate scripts, catalog builders and documents in this repository were developed
with the assistance of Claude (Anthropic), a large language model, under the author's
direction; it wrote the code, ran the sweeps and certificates, transcribed and re-keyed the
printed tables, and drafted the documents. Every gate script was re-run by the author,
separately from the agent that built it, with exit code zero required before acceptance, and
every quoted number traces to a file in this tree. The model used for each block is recorded
in `PROVENANCE.md`. The author takes full responsibility for the content.

## Citation

Tyler Satchel Orden (ORCID 0009-0004-9205-7422), *plesiohedron-census: certified
space-filling polyhedra from a gated agentic search (code, certificates, catalog)*, version
2026.09.04, https://github.com/Tyorden/plesiohedron-census. See `CITATION.cff`.

Cite alongside: M. Schmitt, *On Space Groups and Dirichlet-Voronoi Stereohedra*,
dissertation, FU Berlin, 2016, doi:10.17169/refubium-14374; M. Bernhard, *The Josehedron: A
space-filling plesiohedron based on the Fischer-Koch S Triply Periodic Minimal Surface*,
arXiv:2604.07160 (2026); OEIS A398957, A398958, A398959.

## License

Code (`*.py`, `*.sh`): MIT. Data, tables, certificates, renders and documents: CC BY 4.0.
See `LICENSE`.
