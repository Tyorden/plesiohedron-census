# G1 result — frozen space-group ops (2026-08-28)

Gate: `../ANCHORS.md` G1. Spec: `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §1.1.
Verdict: **G1 AUDIT: ALL PASS** (independent checker, exact Fractions, all 230 groups).

## What was run (command log, in order)

```
mkdir -p <repo>/harness
python3 -c "import spglib; ..."   # -> ModuleNotFoundError
<MathProofs>/paper_prep_venv/bin/pip install spglib               # -> spglib-2.7.0 installed
python3  # (heredoc) probe spglib API: get_spacegroup_type / get_symmetry_from_database fields
python3  # (heredoc) inspect hall-number setting ordering for groups 5,15,68,146,148,167,227
python3 spacegroup_ops.py         # writes spacegroups.json
python3 audit_g1.py               # independent check -> ALL PASS, exit 0 (6.4 s)
python3  # (heredoc) collect setting caveats + translation-denominator census from the frozen JSON
```

No network access beyond the single `pip install spglib`.

## Versions / environment

- Python: `paper_prep_venv` 3.13.1 (`python3`)
- spglib: **2.7.0** (newly installed into `paper_prep_venv`)
- Output: `spacegroups.json` (1,122,954 bytes; 230 groups; 4,425 ops total)

## Setting convention (recorded per group in the JSON)

One setting per ITA number = the **smallest spglib hall number** for that number.
That uniformly selects: origin **choice 1** where two origins exist; monoclinic
**unique axis b, cell choice 1**; rhombohedral groups on **hexagonal (H) axes**
(triple conventional cell, 3 centering vectors). Each group records
`hall_number`, `hall_symbol`, `setting_choice`.

Translations were rationalized as `Fraction(round(12*t), 12)` with a hard-fail
tolerance of 1e-9; zero failures. Reduced-denominator census over all 13,275
translation components: {1: 6993, 2: 4516, 4: 1392, 3: 344, 6: 30} — max
denominator 6, all dividing 12 as required.

## Counts per crystal family

| family | groups | ops (conventional cells) |
|---|---|---|
| triclinic | 2 | 3 |
| monoclinic | 13 | 52 |
| orthorhombic | 59 | 568 |
| tetragonal | 68 | 844 |
| hexagonal (incl. trigonal system) | 52 | 606 |
| cubic | 36 | 2352 |
| **total** | **230** | **4425** |

## Independent audit — output tail (verbatim)

```
per-family summary (groups / ops / failed):
  cubic          36 groups   2352 ops  0 failed
  hexagonal      52 groups    606 ops  0 failed
  monoclinic     13 groups     52 ops  0 failed
  orthorhombic   59 groups    568 ops  0 failed
  tetragonal     68 groups    844 ops  0 failed
  triclinic       2 groups      3 ops  0 failed
cubic smoke test (conventional op counts 24/48/96/192 by centering):
  #195 P23      expected  12  got 12  ok
  #208 P4_232   expected  24  got 24  ok
  #209 F432     expected  96  got 96  ok
  #211 I432     expected  48  got 48  ok
  #221 Pm-3m    expected  48  got 48  ok
  #225 Fm-3m    expected 192  got 192  ok
  #227 Fd-3m    expected 192  got 192  ok
  #229 Im-3m    expected  96  got 96  ok
  #230 Ia-3d    expected  96  got 96  ok
  (josehedron_tables.json 24 ops are a quotient action on cell IDs — intentionally not compared)
G1 AUDIT: ALL PASS (identity, exact closure mod 1, inverses, order = |pointgroup| x centering, centering count — all 230 groups)
```

Audit checks (all in exact `fractions.Fraction`, JSON parsed cold, no code
shared with the generator): schema (int R, det ±1, t in [0,1) with den | 12, no
duplicates); identity present; closure over all ordered pairs mod 1; inverse
for every op; op count = |point class| × centering multiplicity from tables
hardcoded in `audit_g1.py` (ITA Vol. A provenance in its docstring); pure-
translation count = centering multiplicity.

## Sanity cross-check (design-doc deliverable 4)

The 24 ops in `paper_prep/SCI_OEIS_josehedron/data/josehedron_tables.json` are
a **quotient action on cell IDs**, not raw space-group cosets; no direct match
was attempted. Instead the cubic smoke test above spot-checked nine groups —
P23 (#195), **P4_232 (#208, frozen at 24 ops)**, F432 (#209), I432 (#211),
Pm-3m (#221), Fm-3m (#225), Fd-3m (#227), Im-3m (#229), Ia-3d (#230) — and all
conventional op counts landed on the expected 12/24/48/96/192 ladder by point
class × centering.

## Setting caveats

- **Two-origin groups frozen at origin choice 1** (24 groups): 48, 50, 59, 68,
  70, 85, 86, 88, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142, 201, 203,
  222, 224, 227, 228. Much published crystallographic data (and spglib's own
  standardization for some paths) uses origin choice 2 (origin at an inversion
  center); any coordinates imported from literature for these groups must be
  shifted to choice 1 or the group re-frozen at the choice-2 hall number
  (recorded alternative exists in spglib; regeneration is one flag away).
- **Rhombohedral groups (146, 148, 155, 160, 161, 166, 167) frozen on hexagonal
  axes** (`setting_choice: "H"`), so their op lists carry the 3 R-centering
  translations (op counts are 3× the point-class order). Primitive-cell work
  must quotient by the centering vectors stored in `centering.vectors`.
- **Monoclinic groups frozen at unique axis b, cell choice 1** (`b` / `b1`).
- Centered groups generally: op lists are conventional-cell cosets (include
  centering translates); orbit sizes per *primitive* cell need division by
  `centering.multiplicity` (design doc §1.2).
