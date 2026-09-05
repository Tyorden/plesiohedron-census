All source files read. Here is the design doc.

---

# Design: Plesiohedron Minting Harness (PMH)

**Status: design only — no code written.** Sweep point orbits under crystallographic space groups, compute Voronoi cells, canonicalize combinatorial types, dedupe, surface novel candidates, and feed finalists into the existing verified certificate + polyform pipeline.

**Ancestry (read and cited below):**
- `<MathProofs>/paper_prep/SCI_OEIS_josehedron/scripts/build_josehedron.py` — closest ancestor: float-Voronoi construction of an integer-mod-P orbit, lattice extraction, type reduction, op search, `{'T','nbr','ops','proper_ops',...}` JSON emit.
- `<MathProofs>/paper_prep/SCI_OEIS_josehedron/scripts/g1_verify.py` — `clip_cell`: exact-Fraction halfspace intersection with vertex/plane incidence sets; independent lattice det; canonical fixed-polyform enumeration (`canon`/`reduce_anchor`).
- `<MathProofs>/track_b_polyforms/audit_t1_independent.py` — the certificate verifier pattern: `facets()` (float-propose cyclic order, exact convexity verify), `volume()`, C3 face pairings, C4 SAT witnesses, C5 translate-completeness via exact interval solve, C6 all-orthogonal stabilizer via Gram-triple matching.
- `<MathProofs>/track_b_polyforms/build_honeycomb.py` — gluing search; not on the critical path here (Voronoi route supersedes it), but its `rigid_from_correspondence` and patch validation are the fallback if a candidate needs a non-Voronoi realization.
- `enumerate.cpp` / `export_tables.py` / `reference_enum.py` / `burnside_n8.py` / `make_cubic_tables.py` — the enumeration back end, reusable unchanged (constraints checked in §3.4).
- `<MathProofs>/paper/orden_rev1.tex` §"A finite certificate that the complex is a tiling" + "The symmetry quotient" — the standard a finalist must meet.

**Runtime:** `python3` (Python 3.13.1, scipy 1.18.0, numpy 2.5.1, sympy 1.14.0). System `python3` has no scipy. Machine: Apple M3 Max, 16 cores.

**House invariant (already the codebase norm, keep it):** floats may *propose*, only exact Fractions may *decide*. Stated verbatim in the `audit_t1_independent.py` header and practiced in `facets()` (float `atan2` ordering, exact cross-product convexity assert). The search phase is float; anything that enters the dedupe store as a *new type*, and every finalist, is exactly re-derived.

---

## 1. Pipeline

### 1.1 Space-group representation — hand-rolled affine ops, spglib as a one-time data source

A space-group element is `(R, t)`: `R` an integer 3×3 acting on fractional (lattice-basis) coordinates, `t` ∈ ℚ³ mod 1 with denominators dividing 12. This is exactly representable; no library needed at runtime.

- **Source of the 230 groups:** `spglib.get_symmetry_from_database(hall_number)` (pip install into `paper_prep_venv`) returns the full coset list (rotations as ints, translations as floats that are multiples of 1/12 — rationalize by `Fraction(round(12*t), 12)`). One-time script freezes all groups into a checked-in `spacegroups.json`. Trust-but-verify: after rationalizing, verify **exactly** in Fractions that the op set contains the identity, is closed under composition mod 1, and has inverses — the same closure pattern as `build_josehedron.py` lines 233–246 (`key`/`comp`/`keyset`). Fallback with zero dependencies: parse ITA general-position strings ("x, -y+1/2, z+1/2"); ~60 lines.
- **Can we reuse the ops-table format from `honeycomb_tables.json`?** Two different layers, two answers:
  - **Input layer (space-group ops): no.** The `honeycomb_tables.json` `ops` entries (`{'A': int 3×3, 'map': [(offset, type'), ...]}`) are the *quotient action on cell IDs* — a downstream product. Space-group ops need rational translations mod 1. Extend the schema: `{'R': [[int]], 't': ["num/den", ...]}` per op, plus centering vectors and the crystal-family metric constraints.
  - **Output layer: yes, byte-for-byte.** Every candidate that survives emits the josehedron variant of the JSON (`T`, `nbr`, `ops`, `proper_ops`, `lattice_basis`, `detL`, `cell_volume`, `facet_signature` — the `out` dict at `build_josehedron.py:249–254`), which `SCI_OEIS_josehedron/scripts/export_tables.py` (the argv-taking variant, with `proper_ops` support for one-sided counts) converts to `tables.txt` for `enumerate.cpp` unchanged.

**Metric.** Non-cubic groups have free lattice parameters. Represent the conventional cell by a **rational Gram matrix** `G` (from rational a², b², c², a·b cos γ, …). All Voronoi arithmetic runs in fractional coordinates with the `G`-inner product: the bisector of centers `p`, `r` is `2(r−p)ᵀG x = rᵀGr − pᵀGp` — rational plane, rational offsets. Cartesian embedding (float Cholesky of `G`) is used only for scipy in the search phase and for plots.

### 1.2 Orbit generation

Candidate = `(group g, rational Gram G consistent with g's crystal family, base point p ∈ asymmetric unit, rational coords)`. Orbit = `{R_i p + t_i mod 1}` over the coset list.

- **General-position gate (exact):** reject/flag `p` whose site stabilizer is nontrivial: any op with `R p + t ≡ p (mod 1)` other than identity. Plesiohedron requires the orbit to be a Delone set on which the group acts transitively with the cell as Voronoi region; special Wyckoff positions are a *separate stratum* (still legitimate plesiohedra — e.g. triakis truncated tetrahedron sits at diamond sites — so don't discard: route to a "special-position" sub-sweep keyed by Wyckoff letter, where the stabilizer must also stabilize the cell).
- **Integer scaling:** clear denominators. If `p` has denominator `d` and translations denominator 12, multiply by `PERIOD = lcm(d, 12)` → integer points mod `PERIOD`, exactly the `BASE`/`PERIOD` pattern of `build_josehedron.py:33–35` and `g1_verify.py:10–12`. Everything downstream (translation-lattice extraction, exact clipping) then runs on integers.
- `T` = orbit size per **primitive** cell = |G/T| = point-group order ≤ 48. (Conventional multiplicity up to 192 for F-centered cubic; ÷ centering.)

### 1.3 Voronoi computation — float for search, exact for decisions

- **Search phase (float, scipy/Qhull): acceptable — this is precedent, not a compromise.** `build_josehedron.py:80–115` builds a 7³-cell replicated block, runs `scipy.spatial.Voronoi`, and reads ridges (`ridge_points`/`ridge_vertices`, dropping any with `-1`); exactness came later and independently (`g1_verify.py`). PMH does the same per candidate: replicate the orbit over a `(2W+1)³` block (W=2 generally; W=3 for sparse orbits — apply the g1 guard: assert no bounding-box face survives on a central cell, `g1_verify.py:83–84`), extract each central cell's facet polygon sizes, ridge neighbors, and vertex coordinates.
- **Exact phase:** generalize `g1_verify.py:clip_cell` (lines 27–77) — the exact halfspace clipper where vertices carry frozensets of defining planes — in two ways: (a) bisector planes use the Gram form above instead of the Euclidean `a = 2(r−c)`, `b = Σ r²−c²`; (b) candidate centers from `centers_near` sorted by **G-norm** distance. Everything else (cut detection, edge-crossing points via `t = val_i/(val_i−val_j)`, dedup, facet readoff) transfers verbatim. Output: exact facets with vertex sets → cyclic orders via the `facets()` float-propose/exact-verify method of `audit_t1_independent.py:38–76`.
- **When is exact run?** (i) whenever the float fingerprint of a cell is *not already in the dedupe store*; (ii) whenever a degeneracy flag trips (§6); (iii) always, for finalists. Cells matching an already-exactly-confirmed type by canonical code are accepted on the float result.

### 1.4 Combinatorial-type canonicalization

The graph of a 3-polytope is planar and 3-connected (Steinitz), and the geometry hands us the **rotation system** (cyclic edge order around each vertex, from the exact facet cycles). Canonical form = plantri-style embedding code:

- For each of the 2E darts as start, for both orientations (mirror), produce the BFS face-tracing code; the lexicographic minimum over all 4E traversals is the **canonical code** (a byte string).
- Cost: O(E²) with E ≤ ~114 (38 faces × Euler) → < 60k dart-steps per cell; microseconds-to-milliseconds. No nauty dependency, fully deterministic, and the traversal count that achieves the minimum yields the **combinatorial automorphism group order** for free (used in the fingerprint, §4).
- Two-level key: cheap prefilter = `(F, V, E, sorted face-degree multiset, sorted vertex-degree multiset)`; full key = canonical code. Only prefilter collisions compute/compare full codes.

### 1.5 Dedup store

SQLite (`minted.db`), append-only in keeping with the no-loss protocol:
- `types(canon_code PRIMARY KEY, F, V, E, p_vector, v_vector, aut_order, first_seen_group, first_seen_params, exact_confirmed BOOL, exemplar_json)` — `exemplar_json` holds the exact rational cell (planes + vertices) of the first exactly-confirmed witness.
- `sightings(canon_code, group, hall, gram_params, point_p, wyckoff, timestamp)` — every (group, param, point) that produced the type, for transition mapping.
- `catalog(canon_code, source, name)` — literature matches (§4).

---

## 2. Sweep strategy

### 2.1 Parameterization

Rational grid in the asymmetric unit (asymmetric-unit boxes per group are in ITA; conservative alternative: sweep the whole unit cell with denominator-N grid and let the orbit dedupe — wasteful by ≤ 48× but removes a data-entry risk; recommended for v1, with the AU boxes as a later optimization).

- Point grid: `p ∈ {(i/N, j/N, k/N)}`, N = 8 first pass, N = 16 refinement. Skip points failing the general-position gate into the special-position sub-sweep.
- Lattice parameters, scoped by phase:
  - **Phase 1 — cubic (36 groups, no free metric params):** pure point sweep. Richest known territory (Engel's record cells are cubic).
  - **Phase 2 — hexagonal/trigonal/tetragonal (one param, c/a):** c/a² ∈ {1/4, 1/2, 3/4, 1, 3/2, 2, 3} × point grid.
  - **Phase 3 — orthorhombic (two params):** coarse 5×5 ratio grid.
  - **Defer monoclinic/triclinic** (3–6 params; combinatorial budget blows up, and the low-symmetry cells are the least publishable).

### 2.2 Expected cell-type counts (literature anchors — to be re-confirmed during the catalog pass, treat as data not gospel)

The combinatorics of the Voronoi cell is **piecewise constant** in `(p, G)`: parameter space decomposes into open strata (constant type) separated by algebraic degeneracy surfaces where a Voronoi vertex becomes >4-valent or a ridge shrinks. Anchors: lattice Voronoi cells (orbit under translations alone) realize exactly the 5 parallelohedron types; Engel's cubic-group computations (Engel 1981) found Dirichlet stereohedra with up to **38 faces** (the standing record, from high-order cubic groups) and on the order of hundreds of distinct combinatorial types within single cubic groups; the total across all groups runs well into the thousands and no published catalog is complete — that incompleteness is precisely the minting opportunity. Expect per cubic group: a handful of types at N=8 for small groups, dozens to low hundreds for the big I/F-centered groups.

### 2.3 Transition detection

- Compare canonical codes between grid-adjacent points. Different codes on an edge ⇒ a transition surface crosses it: **bisect along the segment** (denominator doubling, depth ≤ 4) to harvest thin strata that a coarse grid steps over. This is where most *new* types hide — thin slivers between fat strata.
- A grid point lying exactly **on** a transition surface shows up as a degenerate cell (§6); log it, perturb by 1/(2N), continue.

### 2.4 Cost per candidate (float phase, measured against the josehedron precedent)

`build_josehedron.py` runs Voronoi on 7³×12 = 4116 points in well under a second. PMH worst case: 5³ × 48 = 6000 points → Qhull ~0.1–0.3 s; ridge extraction + fingerprints for ≤ 48 central cells ~10 ms; canonical codes ~1 ms each. **Budget ≈ 0.3 s per (group, G, p) candidate.** Exact `clip_cell` confirmation: `g1_verify.py` clips 12 cells with an R=9 window (≥ 6800 candidate centers each) in pure-Python Fractions in seconds; PMH exact cost ≈ 1–5 s per *new type*, paid rarely.

---

## 3. Verification ladder for a finalist

A finalist = a stored type flagged novel + interesting. Ladder mirrors the orden_rev1.tex §3 standard (face pairing / interior disjointness via separating axes / volume-coverage on the torus, then symmetry quotient with the [G:L] coset lemma). Voronoi cells of a Delone set tile *by construction* — but the house standard (and the paper standard) is a certificate **independent of the construction**, so every rung is checked as if the tiling claim were unproven.

- **V0 — exact re-derivation.** Rerun generalized `clip_cell` at the exact rational `(G, p)`; assert facet count/sizes match the float sighting; assert adjacency symmetry (the `G1b` loop, `g1_verify.py:93–99`); recompute the translation lattice independently (`g1_verify.py:102–121` det extraction) and the exact volume identity `T·vol(cell) = |det L|` (`build_josehedron.py:168–170`).
- **V1 — tiling certificate.** Generate, then verify with an adapted `audit_t1_independent.py` (new file, same checks, shares no code with the generator):
  - C1: |det basis| exact triple product.
  - C2: per-representative volume recomputed **from geometry** via its own `facets()`/`volume()` (lines 38–91); sum = |det L|.
  - C3: all `T × F` face slots paired, shared vertex set = a full facet of *both* cells (lines 95–110).
  - C4: separating-axis witness per bbox-overlapping ordered pair, verified exactly (lines 113–123).
  - C5: completeness — exact interval solve of `L·v` over bbox-difference boxes (`inv3` + corner enumeration, lines 125–161) proves the translate cutoff instead of asserting it.
  - Coverage then follows by the measure argument exactly as in orden_rev1.tex item 3 (disjoint interiors + volumes summing to the torus volume ⇒ cover).
- **V2 — symmetry certification.**
  - Cell stabilizer over **all** orthogonal maps by Gram-triple matching (C6, lines 163–192) — already fully general, no signed-perm assumption; drop only the `is_signed_perm` cosmetic check for non-cubic cells.
  - Honeycomb point ops: **generalize** `build_josehedron.py:signed_perms` (cubic-only, lines 176–181) to the Bravais point group of the actual lattice: enumerate `A ∈ GL₃(ℤ)` with `AᵀG_L A = G_L` by matching lattice vectors of equal G-norm to the basis (same Gram-triple technique as C6, applied to the lattice) — finite, exact, ≤ 48 results. Then reuse `op_idspace` + the closure check (`key`/`comp`, lines 208–246) verbatim.
  - The coset-counting lemma ([G:L] ≤ T × |stab|, orden_rev1.tex Lemma 3.1) certifies the quotient order; **plesiohedrality** is certified by exhibiting ops acting transitively on the T types (transitive `σ` action, as in the paper's closing check).
- **V3 — polyform enumeration (the payoff product).** Emit the JSON → `export_tables.py` → `enumerate.cpp`. Cross-checks per house standard: (a) independent pure-Python fixed enumeration to n≈5–6 (`reference_enum.py` pattern / `g1_verify.py:123–158` `canon`/`reduce_anchor`); (b) Burnside identity `Σ_m Fix_m(n) = |ops|·free(n)` (adapt `burnside_n8.py`, which hard-codes 4 types/16 ops at lines 11–16 — parameterize `T` and op count); (c) the simple-cubic control substrate (`make_cubic_tables.py`) as the smoke test that the toolchain still reproduces A001931/A000162/A006759.

### 3.4 enumerate.cpp compatibility (checked against the source)

Reusable unchanged, with these hard limits to assert at export time: neighbor count `nnb` is uniform per type (true for any plesiohedron — cells congruent); `poly[32]` ⇒ n ≤ 31; grid `R = 24`, coords int8; `PK` packs `t` into 8 bits and coords offset +64 ⇒ **T ≤ 127** and per-polyform coordinate spread within ±63 — satisfied since T ≤ 48. `blocked` is `S³·T` bytes = 117,649·48 ≈ 5.6 MB — fine. One real risk: a 38-neighbor cell fans out fast; n=8–10 may already be the practical ceiling for high-F cells (fine — early terms are what OEIS wants).

---

## 4. Novelty-check mechanics

**Fingerprint per type** (stored in `types`):
1. `F, V, E`;
2. face-degree multiset (p-vector, e.g. `3^4 4^8` for the josehedron) and vertex-degree multiset;
3. canonical planar code (the identity of the type);
4. combinatorial automorphism order (from the canonicalization traversal count) **and** geometric stabilizer order (C6) — a gap between them is itself interesting (combinatorially symmetric, geometrically not);
5. central symmetry flag (is `−(cell−centroid)` = cell−centroid as a vertex set — exact);
6. context: space group(s), Wyckoff position, T, lattice type, parameter window.

**Catalog comparison.** Seed `catalog` with canonical codes computed *by this same pipeline* from published vertex data (never by transcribing face counts): the 5 parallelohedra; the classical non-parallelohedral plesiohedra (triangular prism, trapezo-rhombic dodecahedron = HCP Voronoi cell, triakis truncated tetrahedron = diamond Voronoi cell, gyrobifastigium); Engel's published cells including the two 38-face types (vertex data from the 1981 paper / Engel's later tables — a literature pass is a prerequisite deliverable); the josehedron itself (`josehedron_tables.json` regenerated through PMH is also the end-to-end integration test — it must come out as a known type with T=12, 4 triangles + 8 quads). Novelty tiers: **Tier A** canon code absent from catalog and from all prior sightings; **Tier B** known combinatorics, new symmetry/group context; **Tier C** known. Interest score for surfacing: high F (approaching/exceeding 38 would be a headline), unusual p-vectors, small automorphism groups at high F, Tier-A in small groups.

---

## 5. Compute + effort estimate

**Laptop feasibility: yes, comfortably** (M3 Max, 16 cores; embarrassingly parallel over candidates via `multiprocessing`).

Wall-clock, float phase at 0.3 s/candidate:
- Cubic phase 1: 36 groups × 9³ grid ≈ 26k candidates ≈ 2.2 h single-core ≈ **~15 min on 12 workers**; N=16 refinement near transitions adds ~2×.
- Phase 2 (tet/hex/trig, ~95 groups × 7 ratios × 729) ≈ 485k candidates ≈ **~3.5 h on 12 workers**.
- Phase 3 (orthorhombic, 59 groups × 25 × 729) ≈ ~9 h parallel. Total program ≈ **a weekend of background compute**.
- Exact confirmations: (number of distinct types, est. 10²–10³) × 1–5 s ≈ minutes–an hour. Finalist V1–V2 certificate: minutes each (T ≤ 48 vs. the audited T=4 case scales C3–C5 linearly in T×F and quadratically in bbox pairs — est. 10–60 min pure Python per finalist; acceptable). V3 enumeration: `enumerate.cpp` at n≈10 on a 38-neighbor T=48 substrate is hours, same class as the banked josehedron n=11 runs.

**New vs adapted (file, function granularity):**

| Component | Basis | Status |
|---|---|---|
| `spacegroup_ops.py` + frozen `spacegroups.json` | spglib dump + exact closure check reusing `key`/`comp` pattern (`build_josehedron.py:233–246`) | **new**, ~200 lines |
| `orbit.py` (orbit gen, stabilizer gate, integer scaling) | `BASE`/`PERIOD` pattern | **new**, ~120 lines |
| `sweep_voronoi.py` (float phase) | `build_josehedron.py:80–115` Voronoi block + ridge readoff, generalized to Gram metric via Cholesky embed | **adapted**, ~200 lines |
| `exact_cell.py` | `g1_verify.py:clip_cell` + `centers_near`, Gram-metric bisectors | **adapted**, ~180 lines |
| `canon_code.py` (rotation-system canonical form + aut order) | none in repo | **new**, ~150 lines |
| `store.py` (SQLite, append-only) | — | **new**, ~100 lines |
| `mint_tables.py` (lattice/types/nbr/ops → JSON) | `build_josehedron.py:117–254` incl. `op_idspace`; op search generalized per §V2 | **adapted**, ~250 lines |
| `mint_certificate.py` + independent `mint_audit.py` | `audit_t1_independent.py` C1–C6 wholesale; C6 already general | **adapted**, ~350 lines |
| Enumeration back end | `export_tables.py`, `enumerate.cpp`, `reference_enum.py`, `make_cubic_tables.py` | **unchanged**; `burnside_n8.py` parameterized (T, ops hard-coded at lines 11–16, 29–30) |

Est. total effort: ~1.5–2.5 kloc new/adapted Python; the risky novel pieces are only `canon_code.py` and the Bravais-point-group generalization.

---

## 6. Risks

1. **Exact-arithmetic cost concentration.** `clip_cell` vertex coordinates have denominators bounded by 3×3 plane-system determinants — benign for integer centers. The blowup vector is **rational lattice parameters**: a Gram entry with denominator q multiplies through every bisector; keep sweep Gram entries at denominator ≤ 8 and re-clear to integers (scale PERIOD by q). Never let float-derived rationals (e.g. `Fraction(float)`) enter — construct all rationals symbolically.
2. **Degenerate positions / non-simple cells.** On transition surfaces, Voronoi vertices become >4-valent; Qhull will resolve them arbitrarily (or merge under joggle), producing a *wrong but plausible* combinatorial type. Mitigations: (a) flag any float Voronoi vertex where >4 centers are near-equidistant (tolerance 1e-9 relative) → force exact clip; (b) in exact clip, a vertex with >3 defining non-redundant planes is decisive proof of degeneracy → tag the sighting `degenerate`, exclude from type minting, log for the transition map. Same for special Wyckoff positions: caught exactly by the stabilizer gate, routed to the separate stratum, never silently mixed.
3. **Float/exact disagreement at store time.** Since only exactly-confirmed types mint, the failure mode degrades to wasted exact recomputation, not wrong data — but a systematically biased float phase could *miss* thin strata entirely. The bisection refinement (§2.3) plus a random-jitter spot check (random rational points, exact-clipped, compared against the stratum's claimed type) bounds this.
4. **Combinatorial explosion.** Bisection near a curved transition surface can cascade; cap refinement depth (4) and cap sightings per (group, type). Phase-3+ metric sweeps multiply candidate counts — the phase gating and the deferral of monoclinic/triclinic are the control.
5. **Cubic-only assumptions latent in ancestor code.** `signed_perms` (`build_josehedron.py:176`) and the mod-P periodic-set matching assume a cubic frame; the audit's `is_signed_perm` (line 189–190) is cubic cosmetics. All flagged in §V2 for generalization — the one place where copying the ancestor verbatim would produce *silently incomplete symmetry groups* (under-merged free counts). The Burnside cross-check (V3b) is the safety net: a missing op breaks `Σ Fix = |ops|·free`.
6. **Canonical-code correctness.** The rotation system must come from exact facet cycles (the `facets()` exact-convexity assert), never from float angular sort alone; a wrong cyclic order canonicalizes to a *different valid-looking* code and forks a phantom type. Unit test: random relabelings/reflections of stored exemplars must canonicalize identically; the josehedron and all five parallelohedra as golden cases.
7. **Novelty-claim risk (non-computational).** The published record is scattered (Engel's tables are not machine-readable); a Tier-A flag is "not in *our* catalog", not "new to science" until the literature pass is done. The measurement-framing house rule applies: report "not matched against catalog snapshot of date X", and gate any minting announcement on a dedicated prior-art review.

---

**Recommended build order:** `spacegroup_ops.py` + closure audit → josehedron end-to-end regression through the new pipeline (must reproduce `josehedron_tables.json` semantics: T=12, 12 facets, 4△+8□, op count) → cubic phase-1 sweep → catalog seeding → first Tier-A finalist through V0–V3.