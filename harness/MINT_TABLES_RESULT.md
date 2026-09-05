# mint_tables result — G0 deferred clauses A/B/C (2026-08-28)

Step: `mint_tables.py` (design `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §V2/§V3, build-table row `mint_tables.py`). Closes the three clauses recorded in `G0_RESULT.md` as NOT YET RUN. Derivation inputs: BASE mod 8 (verbatim from `g0_regression.py`), the G0-validated pipeline (`orbit.py`, `exact_cell.py`), the frozen G1-audited `spacegroups.json`. Comparison target (loaded only in the gate phase): `SCI_OEIS_josehedron/data/josehedron_tables.json`.

Verdict: **ALL IN-SCOPE ASSERTIONS PASS — G0 clauses A/B/C CLOSED**

## What the "24" counts (clause A interpretation, per instruction)

The banked `ops` list is the honeycomb's point-symmetry group MODULO LATTICE TRANSLATIONS, in its quotient action on cell IDs (v,t) -> (A v + c_t, t') — exactly the object the enumerator consumes. It equals the POINT GROUP of the honeycomb's space group IT(220) = I-43d: order 24 (-43m), 12 proper. It is NOT the site symmetry of a cell: the Wyckoff-12a site symmetry is -4, order 4 (verified from the frozen IT(220) entry via orbit.site_stabilizer), and 24 = T_primitive x |site| = 6 x 4. Op-for-op equality to the banked list is verified under the clause-B bijection, modulo one uniform lattice translation per op (ops are coset representatives; a global lattice shift is invisible to the enumerator's translation-normalized canonical form).

## Assertions

- **PASS** M0 independence: derivation functions never touch the banked file (ast audit) — offenders=[]
- **PASS** M1 derivation: detL=256, T=6, volume identity T*vol==detL, 12-facet 4tri+8quad cells, adjacency symmetric, tables written — detL=256, T=6, reps=[0, 1, 2, 3, 4, 5], out=mint_josehedron_tables.json
- **PASS** M2 site symmetry (clause A, site half): BASE/8 IS the IT(220) orbit of (0,1/4,3/8); site stabilizer order 4 (-4: dets [-1,-1,1,1]); point group order 24 (12 proper) = T_prim*|site| = 6*4 — |orbit|=12, |stab|=4, |PG|=24, proper=12
- **PASS** M3 derived honeycomb ops (clause A, ops half): |ops|=24 with 12 proper; identity+closure held (asserted in derivation); rotation parts == the 24 distinct IT(220) rotation parts — |ops|=24, proper=12, R-set match=True
- **PASS** M4 clause B: nbr-table semantic equality — explicit bijection (v,t)->(M v + s_t, pi(t)) maps derived table onto banked table EXACTLY (all 6 rows as multisets), M unimodular — M=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], |detM|=1, pi=[0, 1, 2, 3, 4, 5], s=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
- **PASS** M5 clause A: banked ops semantics — |ops|=24 (12 proper) in the banked tables, and op-by-op semantic equality of derived ops to banked ops under the M4 bijection (mod uniform lattice translation) — banked |ops|=24 (proper 12); 24/24 op keys equal, 12/12 proper keys equal (translation-normalized, under the M4 bijection)
- **PASS** M6 clause C: enumerator (banked compiled enumerate, via banked export_tables.py) on derived vs banked tables: fixed AND free identical for n<=6, and equal to the banked VERIFIED results (results/josehedron_free.txt) — mine==banked: True; free=[1, 2, 15, 131, 1360, 15133], fixed=[6, 36, 308, 3030, 32262, 362010]
- **PASS** M7 one-sided supplement: proper_ops enumeration identical on both tables and equal to banked verified one-sided results, n<=6 — one-sided=[1, 4, 30, 261, 2717, 30265]

## Derivation facts

- Primitive lattice basis (columns, period-8 frame): ((-4, -4, -4), (-4, -4, 4), (-4, 4, -4)), detL=256 (= BCC lattice <(8,0,0),(0,8,0),(4,4,4)>, verified exactly both ways).
- T=6 primitive types, reps (base indices) [0, 1, 2, 3, 4, 5]; exact volume identity 6*(512/12)=256.
- Ops search space: the 48 signed permutation matrices — COMPLETE because any honeycomb point op preserves the derived translation lattice L, L is the BCC lattice (verified), and Aut(BCC) = O_h = signed perms; cross-check: the 24 rotation parts found equal the 24 distinct rotation parts of the frozen IT(220) coset list (M3).
- Derived tables written to `mint_josehedron_tables.json` (banked schema: T, nbr, ops, proper_ops, lattice_basis, detL, cell_volume, n_proper, n_improper, facet_signature).

- Clause-B witness bijection: pi=[0, 1, 2, 3, 4, 5], s=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] (s_0 fixed to 0; M in M4 detail line).

## Enumerator provenance (clause C, per instruction: which path)

- Used the BANKED workflow exactly: banked `export_tables.py` (json -> tables.txt) + the banked COMPILED `enumerate` binary (`SCI_OEIS_josehedron/scripts/enumerate`, arm64, the same binary that produced the banked results; not recompiled — it runs and reproduces the banked verified values bit-for-bit). `reference_enum.py` was not needed as the sanctioned path since the compiled binary is present and its output on the banked tables matches the banked verified results, which were themselves independently cross-checked in the SCI_OEIS program.

## Honest scope notes / deviations from the tasking

- TASKING DISCREPANCY (recorded, not papered over): the task instruction stated the published values as "free = A397708, fixed = A397709 ... n<=6 free counts are 1,4,16,116,903,8551". That does NOT match the banked Josehedron record and the series 1,4,16,116,903,8551 appears NOWHERE in the MathProofs tree (grepped). Per the a397708.txt header and SUBMISSION_JOSEHEDRON.md, A397708/A397709 are the SPHENOID hendecahedron sequences; the Josehedron's assigned numbers are fixed = A398957, one-sided = A398958. The pre-registered authority is ANCHORS G0: "enumerator on both gives identical fixed/free n<=6" — asserted in M6 — plus equality to the banked VERIFIED results (free 1,2,15,131,1360,15133; fixed 6,36,308,3030,32262,362010; one-sided 1,4,30,261,2717,30265), asserted in M6/M7.
- The bijection search fixes s_0=(0,0,0) WLOG (the banked table is invariant under adding one lattice vector to every anchor); any returned bijection is one valid witness, uniqueness not claimed. The witness found is the IDENTITY (pi=id, M=I, s=0): the independent derivation's deterministic tie-breaks (first-seen type reps, shortest-basis search) landed on the same labels and basis as the banked build. The search itself was general — all 720 type permutations, M computed from the two bases — identity is simply the witness it found.
- Independence of the derivation code path from the banked builder: this step is all-integer/Fraction (exact adjugate inverses, no numpy/scipy, no float lattice arithmetic), whereas build_josehedron.py used float numpy inverses with rounding; the shared inputs are only BASE and the G0-validated pipeline modules.
- Ops equality is modulo one uniform lattice translation per op (see interpretation section); exact per-op c_t equality without that quotient is NOT claimed and is not semantically meaningful for coset representatives.
- Nothing here claims novelty or touches G5; no banked file was modified (derived outputs live in this harness directory only).

## Commands run

```
PY=python3
cd <repo>/harness
$PY mint_tables.py   # this gate; writes mint_josehedron_tables.json,
                     # mint_tables_{mine,banked}[_proper].txt,
                     # MINT_TABLES_RESULT.md
```
