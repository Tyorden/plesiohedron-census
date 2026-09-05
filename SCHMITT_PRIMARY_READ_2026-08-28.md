# Schmitt 2016 — primary-source read (Tyler gate CLOSED 2026-08-28)

Source: M. W. Schmitt, "On Space Groups and Dirichlet–Voronoi Stereohedra,"
dissertation, FU Berlin, 2016, doi:10.17169/refubium-14374. PDF downloaded by
Tyler (browser, Refubium anti-bot wall) 2026-08-28, archived at
references/Schmitt_2016_dissertation.pdf (2.4 MB, 190 pp). Advisor: G. M.
Ziegler; external referee: A. Schürmann. Read: Preface, ch. 2 §2.1–2.2 opening
(pp. 23–35), §2.3 Discussion complete (pp. 151–156), Appendix B complete
(pp. 168–173). Reader: Fable 5 (main session), direct page reads.

## What chapter 2 actually is

A **grid-sampling survey**, not an enumeration/classification:
- Scope: **145 space groups** — tetragonal, trigonal, hexagonal, cubic.
  Triclinic summarized from literature (IT(1): 5 parallelohedron types, max 14
  facets, Fedorov; IT(2): 165 types, max 20 facets, Štogrin 1975). Monoclinic
  + orthorhombic **omitted**, justified as "already understood or would not
  have been able to produce stereohedra with more than 38 facets" citing
  [BS01; BS06; SS08; SS11] (p. 151).
- Method (§2.2 + App. B): for each group, reduce the fundamental domain by the
  **normalizer** N(Γ) ("Cheshire groups", Hirshfeld), triangulate the reduced
  domain R_k, generate rational-barycenter grids (~10^6 points per metrical
  parameter; b-ratios stepped 1/2..7/2 in 1001 steps of 3/1000), compute each
  grid point's DV-cell **in exact arithmetic** (C++ + Polymake callable
  library + GMP), record f-vector + generating point. Orbit points bounded by
  Koch's open-slab lemma (Lemma B.2 = the relevant-points bound). 3,073,014
  CPU-hours ≈ **351 CPU-years**; ~14 TB output. Software `plesiohedron` +
  data: github.com/moritzschmitt/plesiohedron.
- Rigor status **in his own words**: semicontinuity of f-vectors means a fine
  enough grid finds the extremal cell, but "finding a lower bound for the
  radius r seems to be difficult" (p. 26) — i.e. **no proven grid-fineness
  bound; the 38 max is observed, not a theorem.**

## Headline results (§2.3, p. 151)

- "We investigated a total of 145 space groups and found **3315 combinatorial
  types** of stereohedra, most of them new. These stereohedra yield **238
  different f-vectors**."
- All facet counts 4–38 realized; all vertex counts 4–70. Both maxima realized
  by **Engel's stereohedron in IT(214) = I4₁32**. Engel's four combinatorial
  types with f = (70, 106, 38) **confirmed; no further 38-facet types found**.
- Runners-up: IT(98) second-most facets (bound improved 29→35), IT(178) third
  (32→34). Many groups: "no previous work done on them and our results are
  the first."
- Prior-literature corrections he documents: Koch & Fischer [KF72] coordinate
  errors (they did not compute exactly — told to him by Koch); **Engel's own
  diagram [Eng81a, Abb. 3] "contains a few mistakes"** (his Fig. 2.2 vs 2.3);
  Smith [Smi65] claims not reproducible ("skeptical about his rather vague
  claims").

## Gate verdicts

1. **KILL CRITERION 1 DOES NOT TRIGGER in the strong form.** Ch. 2 is not a
   complete combinatorial-type enumeration for its systems — it is a very
   deep sample. A new plesiohedron in a covered group is *possible* (missed by
   grid/parameter stepping, or at a special position between grid points).
   HOWEVER the diligence duty inverts: any candidate of ours in a covered
   group MUST be checked against his group's table (f-vector level, in the
   thesis) and against the GitHub data (type level). "Absent from Schmitt's
   3315-type, 351-CPU-year survey" is strong novelty evidence; "present" ⇒
   reframe to first-realization/naming per ANCHORS.
2. **The "38-max proven" folklore (Wikipedia/MathWorld/Pegg) OVERSTATES the
   thesis.** Correct citation for our paper: refereed record remains
   38 ≤ max ≤ 92 open (Sabariego–Santos); Schmitt's exhaustive *sampling*
   found nothing above 38. This is measurement framing — house style anyway.
3. **Engel 1981 ILL priority RECALIBRATED down** (Tyler's call to still order
   it or not): Schmitt confirmed Engel's I4₁32 results, corrected his diagram,
   and flagged Koch–Fischer's coordinates as unreliable. Schmitt's data
   supersedes Engel for diligence purposes; Engel remains nice-to-have as the
   independent historical source.
4. **Our MINT harness design is validated by precedent**: normalizer-reduced
   domain → orbit → exact Voronoi cell → invariants is exactly his pipeline
   (we add canonical codes = type-level identification up front, where his
   in-text tables stop at f-vectors). His Lemma B.2 (Koch's slab bound) is
   citable for our sweep's neighbor-completeness argument.

## New concrete next steps

- **G2-adjacent check — EXECUTED SAME DAY (see below)**: determine the
  Josehedron's generating space group, then check that group's ch. 2 table
  for f = (12, 22, 12).
- **Ask Tyler**: permission to clone github.com/moritzschmitt/plesiohedron
  (code + data) for machine-checkable type-level diligence.
- Cubic sweep (G2) prompt/docs should cite Schmitt as method precedent and
  use "observed max 38" wording.

## SAME-DAY FOLLOW-THROUGH (2026-08-28, main session)

1. **Space group settled**: spglib (symprec 1e-5 and 1e-9 agree) on the
   generating orbit (the 12 FKS extremal points mod 8): **IT(220) = I4̄3d,
   Wyckoff 12a, site symmetry 4̄** — order 4, exactly the G0 canonical-code
   automorphism order (independent cross-check). Bernhard's paper never
   states the group; this is a new recorded fact. IT(220) is one of the 8
   chiral-corridor cubic groups the LANDSCAPE_SCOUT flagged as the sweet
   spot.
2. **Schmitt's IT(220) table (printed p. 141) CONTAINS f = (12, 22, 12)**:
   generating point x = (143/1746, 289/3492, 295/3492), frequency 46 of
   1,000,677,997 grid points. Also present: his group-220 remark improves
   Koch's 17-facet record to 25 (his table's max row set: up to 38,58,22).
3. **Exact type comparison run** (harness/schmitt_220_check.py, result in
   harness/SCHMITT_220_CHECK_RESULT.md): orbit of x under the frozen
   G1-verified IT(220) coset list (48 points/conv. cell, general position,
   PERIOD 3492) through the same float-sweep → exact-clip → canonical-code
   pipeline as G0. **VERDICT: NO MATCH.** Schmitt's cell: p-vector
   6△+4□+2⬠, aut 1. Josehedron: 4△+8□, aut 4. Same f-vector, different
   combinatorial type.
4. **New small fact worth keeping**: IT(220) realizes f = (12, 22, 12) by at
   least two distinct combinatorial types (Schmitt's general-position type
   and the Josehedron at special position 12a).
5. **Honest limit**: his in-text table lists ONE representative point per
   f-vector; the frequency-46 region and the rest of his 14 TB could still
   contain the Josehedron type at other points (in particular if his grid
   ever hit the 12a special orbit). Table-level absence is evidence, not
   proof — type-level closure needs his published data (GitHub clone,
   pending Tyler's ok). Consistent with the scout's thesis: special-position
   orbits are exactly the corridor grid sampling under-covers, and the
   Josehedron sits at one.
