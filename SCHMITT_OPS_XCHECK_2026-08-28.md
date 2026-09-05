# Schmitt 2016 space-group operations vs frozen G1 spacegroups.json — independent historical cross-check (2026-08-28)

Script: `harness/xcheck_schmitt_ops.py` (deterministic; exit 0 iff no MISMATCH
and no PARSE-FAIL). Verified deterministic: two consecutive runs byte-identical.
Read-only on the recovered repo and on `harness/spacegroups.json`.

**Comparands.**
- Ours: `harness/spacegroups.json` — frozen, generated from spglib 2.7.0, all
  230 groups, full conventional coset lists, exact n/12 rational translations,
  G1-audited (identity/closure/inverses/orders). Setting: smallest spglib hall
  number per ITA number (origin choice 1 where two exist; monoclinic unique
  axis b cell choice 1; rhombohedral on hexagonal axes).
- His: Moritz Schmitt's 2016 `plesiohedron` suite, recovered 2026-08-28 from
  Software Heritage (see `SCHMITT_DATA_RECOVERY_2026-08-28.md`; repo frozen on
  GitHub after 2016-06-21). Files: `data/3d/space_group_3d_N.cpp` for
  N=2..230 (group 1 absent, trivial) + the `splitters_` tables in
  `spacegrp.cpp`. This is a fully independent 2016-era derivation, produced
  before our pipeline existed and with no shared code path.

## 1. Schmitt's data format (reverse-engineered before comparing)

From `data/3d/space_group_3d_{195,220,19,146}.cpp`, `plesiohedron.h`,
`spacegrp.cpp`:

- Each `init_3d_reps_N()` pushes 4×4 **exact rational** affine matrices onto
  `SpaceGroup::reps_` (`RationalMatrix`), one per isometry, entries set as
  `(*isom)[i][j].set(numerator, denominator);` — integers only, no floats
  anywhere in the 229 files (the parser rejects any non-integer `.set`
  argument; none occurred). Max translation denominator over all groups: **6**.
- Layout: rows 0–2 × cols 0–2 = linear part R; column 3 rows 0–2 =
  translation t; row 3 = (0,0,0,1). **Column-vector convention** x ↦ Rx + t
  (confirmed: group 19's ops reproduce IT's (−x+½,−y,z+½) family verbatim).
  Translations are not always reduced mod 1 in the files (e.g. −1/2); reduced
  during parsing.
- `reps_` holds **one coset representative per point-group element** (coset
  reps modulo the *full* translation lattice), not the conventional-cell
  expansion. The lattice mod Z³ is given separately by `splitters_` in the
  `dim_==3` switch of `spacegrp.cpp`: length-4 rational vectors (last entry
  0), first always (0,0,0) — these are the centering vectors of his cell.
- **Settings are not uniformly ITA-conventional:**
  - Trigonal + hexagonal groups (143–194) are given in an **orthohexagonal
    C-centered basis**: R entries take values ±1/2, ±3/2 (hence
    `RationalMatrix`), and every hexagonal-family group carries the extra
    splitter (1/2,1/2,0) (rhombohedral ones additionally the two
    R-centering translations expressed in that basis, 6 splitters total).
  - The 24 IT two-origin groups are given at **origin choice 2** (our freeze
    is origin choice 1).
  - Everything else matches our spglib settings directly (monoclinic unique
    axis b confirmed in his data).
- **Recovered-code gap:** the `dim_==3` switch covers cases 16..230 only;
  for N=2..15 the constructor throws ("no splitters were defined") although
  the `data/3d` rep files exist. So for N=2..15 the centering is *not present
  in his data*. For the 9 primitive groups among them (2,3,4,6,7,10,11,13,14)
  nothing is lost (trivial lattice, and we verified his reps close as a group
  mod Z³). For the 5 C-centered monoclinics (5,8,9,12,15) our centering
  vector had to be assumed — flagged, and those groups are capped at
  CONJUGATE-VERIFIED regardless of how well they match.

## 2. Method (all arithmetic exact — `fractions.Fraction`; no floats, no tolerances)

Per group, comparison ladder:

- **L1** op count: #(his reps, deduplicated mod his lattice) == our
  n_ops / centering multiplicity (= point-group order).
- **L2** conjugacy-invariant fingerprint: multiset of
  (det R, trace R, order of R) over coset representatives (basis-independent).
- **L3** exact affine equivalence: find (M, v) with x_his = M·x_ours + v such
  that M maps our full translation lattice (Z³ + centering) **onto his**
  (checked via |det M| = mult_ours/mult_his and images of generators, using
  *his* splitters as recovered) and
  {(M R M⁻¹, M t + (I − M R M⁻¹)v)} equals his op set modulo his lattice —
  exact set equality of all coset representatives. Candidate M: identity, the
  48 signed permutations, and the hexagonal→orthohexagonal family
  M(a,b) = [[a,b,0],[a+2b,−2a−b,0],[0,0,±1]] (derived from commutation with
  his 3-fold matrices) composed with signed permutations. v is solved exactly
  from (I − R*)v ≡ τ − Mt (mod his lattice) using an op R* maximizing
  |det(I − R*)|, all lattice branches enumerated, then verified against the
  full op set.
- Additionally verified per group: **closure** of his expanded op set
  (products land in the set; identity present) — a format-understanding check.

Verdicts: **EXACT** (M=I, v=0, and his splitter set equals our centering
set), **CONJUGATE-VERIFIED** (exact equality after some (M,v), or any match
that needed the assumed centering), **FINGERPRINT-ONLY** (L1+L2 pass, no
affine map found — would appear in EXCEPTIONS), **MISMATCH**, **PARSE-FAIL**.

**Enantiomorph guard.** Affine equivalence with improper M would silently
identify the 11 enantiomorphic pairs (e.g. P4₁2₁2 ↔ P4₃2₁2). The script
therefore asserts that each of the 22 chiral-pair groups matched with
**det M > 0**. (In the orthohexagonal family the found composite M for every
chiral screw group is proper, det = +1/2; achiral groups may match through an
improper M, which is type-preserving for them.)

## 3. Results (run 2026-08-28, exit 0)

| Level | Count |
|---|---|
| EXACT | 148 |
| CONJUGATE-VERIFIED | 81 |
| FINGERPRINT-ONLY | 0 |
| MISMATCH | 0 |
| PARSE-FAIL | 0 |

All 229 parsed cleanly (229/229 L1 pass, 229/229 L2 pass, 229/229 closure
verified). **Exception list: empty.** Enantiomorph guard: PASS.

CONJUGATE-VERIFIED decomposes exactly into the three predicted setting
differences, with nothing left over:

1. **Borrowed centering, M=I, v=0 (5 groups):** 5, 8, 9, 12, 15 — the
   C-centered monoclinics whose splitters are absent from the recovered code
   (§1). His reps match ours identically; only the centering vector is ours.
2. **Pure origin shift, M=I (24 groups):** 48, 50, 59, 68, 70, 85, 86, 88,
   125, 126, 129, 130, 133, 134, 137, 138, 141, 142, 201, 203, 222, 224, 227,
   228 — machine-verified to be **exactly** the 24 IT two-origin groups; the
   recovered shifts are the tabulated origin-1↔origin-2 shifts (quarters, and
   eighths for the d-glide groups 70, 88, 141, 142, 203, 227, 228; e.g.
   Fddd v=(7/8,7/8,7/8) ≡ −(1/8,1/8,1/8)).
3. **Basis change (52 groups):** 143–194 — machine-verified to be exactly the
   trigonal/hexagonal families, all mapped by the *same* lattice
   transformation M = [[1/2,0,0],[1/2,−1,0],[0,0,±1]] (hexagonal →
   orthohexagonal C-centered; ±1 chosen per group so that chiral screw groups
   map properly; a few screw groups additionally take an allowed z-origin
   shift, e.g. P3₁21 v=(0,0,5/6)).

## 4. Negative controls (machinery validation, ad hoc, not in the repo)

The comparator was exercised against deliberate corruptions: (a) one screw
translation of IT(19) altered by 1/4 or 1/2 → no affine map (FINGERPRINT-ONLY,
listed as exception); (b) IT(19) replaced by translation-free P222 ops (a
*valid* group with identical point group) → detected; (c) IT(173) 6₃ screw
removed → detected; (d) IT(23) given C instead of I centering → detected;
(e) enantiomorph swap (96's data checked as 92) → matches only with det M = −1,
which the enantiomorph guard flags; (f) wrong point group (16's data vs 3) →
L1-FAIL. The all-green result is therefore not vacuous.

## 5. Honest limits

- **What this verifies:** for every group 2–230, Schmitt's 2016 isometry
  representation and our frozen spglib 2.7.0 table define the **same space
  group up to the documented exact affine change of setting** (and identically
  the same group, same setting, for the 139 EXACT groups ≥16 plus 9 primitive
  groups <16). Both sides exact rational; no tolerances anywhere.
- Group 1 (P1) is absent from his data (trivial group) — not checked, nothing
  to check.
- For groups 5, 8, 9, 12, 15 the centering vector is not in the recovered
  code; his reps alone match ours exactly, but the centering part of those 5
  comparisons is assumed, not independently confirmed (hence capped at
  CONJUGATE-VERIFIED).
- CONJUGATE-VERIFIED groups are verified through a change of setting *found by
  our own search*; the (M, v) used is printed per group and is in every case
  one of the standard crystallographic setting relations (origin choice 2;
  orthohexagonal cell). No general (unconstrained) affine search was needed —
  the curated candidate family sufficed for all 229 groups.
- Independence caveat: Schmitt's ultimate source for his tables is not
  documented in the recovered repo (README is one line). His data
  demonstrably encode origin choice 2 and an orthohexagonal setting, i.e.
  NOT a re-export of spglib's choices — consistent with an independent
  derivation, but "independent of the same upstream IT tables" cannot be
  proven from the repo alone.
- The exit-code contract is exactly as specified (exit 1 iff MISMATCH or
  PARSE-FAIL). Note that a translation-level error in either table would
  surface as FINGERPRINT-ONLY, which appears in the EXCEPTIONS list but not
  in the exit code; the actual run has zero such groups.

**Verdict.** Schmitt's fully independent 2016 operation tables agree exactly —
group-by-group, operation-by-operation, in exact rational arithmetic — with
our frozen G1 `spacegroups.json` for all 229 comparable groups, once his three
documented setting choices (origin choice 2 on the 24 two-origin groups,
orthohexagonal basis on 143–194, undefined centering for N<16) are accounted
for by explicit exact affine equivalences. Zero mismatches, zero parse
failures, zero unresolved groups. This is a strong external, historically
independent confirmation of the G1 freeze.
