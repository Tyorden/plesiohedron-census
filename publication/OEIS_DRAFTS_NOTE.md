# OEIS drafts — slot discipline note (2026-09-01)

The per-shape `oeis_draft_{fixed,onesided,free}.txt` files in the four
publishable-now packages are **DRAFTS, not submissions**. Up to 12 sequences
are staged (4 shapes x fixed/one-sided/free).

**OEIS submission slots are limited (5 concurrent per contributor), and
wave-gamma items are already staged elsewhere in the program. Tyler sequences
all submissions** — nothing here goes to oeis.org until he slots it. Suggested
order per shape (the A398957 precedent): fixed first (hosts the program
a-file per OEIS rule 17), then one-sided, then free, cross-referencing as
A-numbers are assigned.

Pre-submission checklist per draft (mirrors the Josehedron package):
1. Run the OEIS existence search on the DATA terms (record the "no results"
   screenshot/date).
2. Decide the depth: n <= 6 is staged; if a deeper run is wanted first,
   the a-file's tables + the published A398957 enumerator extend it
   (the Josehedron went to n = 11 with two independent implementations
   before submission — that bar has NOT been met here; n = 5..6 terms
   currently rest on the single banked enumerator plus the internal
   identities recorded in each `counts.md`).
3. Substitute the assigned A-number into the a-file placeholder and the
   cross-refs.
4. Comments end with " - ~~~~" so the editor auto-signs; never hand-type
   name/date.
5. Names in NAME lines are Tyler's greenlit ones (Satchelhedron,
   Ordenhedron); the two Pn-3m cells use descriptive wording until Tyler
   chooses — if he picks personal names, update NAME + COMMENTS before
   submission, not after.

The three HELD shapes (IT 212/230/214) get NO OEIS drafts by design — their
counts are banked in their packages, but no public sequence is staged until
the Engel/Koch ILL check clears (`ILL_REQUEST_STAGED.md`).
