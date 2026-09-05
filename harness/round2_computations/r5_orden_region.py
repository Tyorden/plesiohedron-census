#!/usr/bin/env python
"""R5 -- a coarse estimate of the extent of the Ordenhedron's type region in
the general position 24h of IT(201) Pn-3 (referee W9): the exact chain is run
on the cubic box of points (1/8 + i/96, 1/6 + j/96, 5/12 + k/96), i, j, k in
-4..4 (729 points, step 1/96, half-width 1/24 of the cube edge), and every
canonical code is compared with the stored Ordenhedron code.  Points that
fall on special positions are recorded as such.  Also reports, per axis, the
first step at which the type changes (scan in steps of 1/96 up to 1/8).
Exact; deterministic."""
import os, json, itertools
from fractions import Fraction as F
from common2 import *  # noqa

ent = TYPES["2de0a21129cabe90"]
p0 = (F(1, 8), F(1, 6), F(5, 12))
step = F(1, 96)
hits = 0; total = 0; special = 0; other = {}
grid = {}
for i, j, k in itertools.product(range(-4, 5), repeat=3):
    q = (p0[0] + i * step, p0[1] + j * step, p0[2] + k * step)
    r = exact_cell_at(201, q)
    total += 1
    if r["stab"] != 1:
        special += 1
    same = r["code"] == ent["canon_code"]
    grid[(i, j, k)] = same
    if same:
        hits += 1
    else:
        key = (r["f"], pvec_compact(r["p"]))
        other[key] = other.get(key, 0) + 1
# per-axis extent
ext = {}
for ax, d in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
    for sign in (-1, 1):
        n = 0
        while n < 12:
            n += 1
            q = tuple(p0[a] + sign * n * step * d[a] for a in range(3))
            r = exact_cell_at(201, q)
            if r["code"] != ent["canon_code"]:
                break
        else:
            n = None
        ext[(ax, sign)] = n   # first failing step count (None: none up to 12/96 = 1/8)
L = ["## R5 -- extent of the Ordenhedron's type region (coarse box scan, IT(201) 24h)", "",
     f"Box (1/8, 1/6, 5/12) + (i, j, k)/96, i, j, k in -4..4: {hits} of {total} points give the Ordenhedron type ({100*hits/total:.1f}%); {special} of the {total} points lie on special positions.",
     "Other types met in the box (f, p: count): " + "; ".join(f"{f} {p}: {c}" for (f, p), c in sorted(other.items(), key=lambda t: -t[1])) if other else "no other type met in the box.", "",
     "First step (in units of 1/96) at which the type changes along each axis, up to 12 steps: " +
     ", ".join(f"{'xyz'[ax]}{'+' if s > 0 else '-'}: {('none up to 1/8' if n is None else str(n))}" for (ax, s), n in sorted(ext.items())), "",
     "Reading: this is a sampling estimate on a grid of step 1/96 in a box of half-width 1/24, not a computation of the region; it bounds the region from inside only where every sampled point in a direction agreed."]
open(os.path.join(HERE, "r5_orden_region.md"), "w").write("\n".join(L) + "\n")
json.dump(dict(hits=hits, total=total, special=special, other={str(k): v for k, v in other.items()},
               extent={f"{'xyz'[ax]}{'+' if s > 0 else '-'}": n for (ax, s), n in ext.items()}), open(os.path.join(HERE, "r5_orden_region.json"), "w"), indent=1)
print("\n".join(L))
