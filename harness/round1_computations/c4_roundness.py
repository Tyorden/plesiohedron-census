#!/usr/bin/env python
"""C4 -- roundness under both conventions: (a) site-centred circumsphere
(radius^2 = rho^2 of the certificate), (b) minimal enclosing sphere of the
vertex set.  The MES is computed EXACTLY: it is the smallest sphere among the
minimal spheres of all vertex subsets of size 1..4 (midpoint sphere,
circumcircle sphere, circumsphere) that contain every vertex; exact Fractions
throughout, one float division per percentage at the end."""
import json, os, sys, itertools, math
from fractions import Fraction as F
from common import *  # noqa
sys.path.insert(0, os.path.join(HARNESS, "..", "publication"))
from build_packages import JOSE_BASE, JOSE_PERIOD  # noqa


def solve3(M, b):
    A = [list(map(F, M[i])) + [F(b[i])] for i in range(3)]
    for c in range(3):
        piv = next((i for i in range(c, 3) if A[i][c] != 0), None)
        if piv is None: return None
        A[c], A[piv] = A[piv], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for i in range(3):
            if i != c and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * bb for a, bb in zip(A[i], A[c])]
    return [A[i][3] for i in range(3)]


def sub(a, b): return tuple(a[k] - b[k] for k in range(3))
def dot(a, b): return sum(a[k] * b[k] for k in range(3))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def min_sphere_of(S):
    """Smallest sphere with the points of S on its boundary (|S| in 1..4); None if degenerate."""
    if len(S) == 1: return S[0], F(0)
    if len(S) == 2:
        c = tuple((S[0][k] + S[1][k]) / 2 for k in range(3)); return c, dot(sub(S[0], c), sub(S[0], c))
    a = S[0]
    if len(S) == 3:
        u, v = sub(S[1], a), sub(S[2], a); nrm = cross(u, v)
        if nrm == (0, 0, 0): return None
        x = solve3([list(u), list(v), list(nrm)], [dot(u, u) / 2, dot(v, v) / 2, 0])
        if x is None: return None
        c = tuple(a[k] + x[k] for k in range(3)); return c, dot(x, x)
    u, v, w = sub(S[1], a), sub(S[2], a), sub(S[3], a)
    if det3(u, v, w) == 0: return None
    x = solve3([list(u), list(v), list(w)], [dot(u, u) / 2, dot(v, v) / 2, dot(w, w) / 2])
    c = tuple(a[k] + x[k] for k in range(3)); return c, dot(x, x)


def mes(verts):
    best = None
    n = len(verts)
    for k in (2, 3, 4):
        for S in itertools.combinations(range(n), k):
            s = min_sphere_of([verts[i] for i in S])
            if s is None: continue
            c, r2 = s
            if best is not None and r2 >= best[1]: continue
            if all(dot(sub(v, c), sub(v, c)) <= r2 for v in verts):
                best = (c, r2, S)
    return best


def pct(vol, r2):
    return 100.0 * float(vol) / (4.0 / 3.0 * math.pi * float(r2) ** 1.5)


rows = []
# Josehedron control
site = JOSE_BASE[0]
jec = clip_cell(site, JOSE_BASE, JOSE_PERIOD)
assert 4 * jec["rho2"] <= jec["cutoff_D"] ** 2
jverts = [tuple(F(x) for x in v) for v in jec["vertices"]]
c, r2, S = mes(jverts)
jvol = cell_volume(jec)
rows.append(("Josehedron (control)", tuple(F(x) for x in site), jec["rho2"], c, r2, jvol))
for cid, label, name in CELLS:
    r = rederive(cid); ec = r["ec"]
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    c, r2, S = mes(verts)
    rows.append((label + " " + name, tuple(F(x) for x in ec["center"]), ec["rho2"], c, r2, cell_volume(ec)))
    print(label, "site", pt_str(ec["center"]), "rho2", ec["rho2"], "MES centre", pt_str(c), "r2", r2, "support", S)

L = ["## C4 -- roundness under both conventions", "",
     "| cell | site | site-centred rho^2 | MES centre | MES r^2 | centres coincide | roundness (site-centred) | roundness (MES) |",
     "|---|---|---|---|---|---|---|---|"]
for name, site, rho2, c, r2, vol in rows:
    same = (tuple(c) == tuple(site))
    assert r2 <= rho2 and (same == (r2 == rho2))
    L.append(f"| {name} | {pt_str(site)} | {frac_str(rho2)} | {pt_str(c)} | {frac_str(r2)} | {'YES' if same else 'NO'} | {pct(vol, rho2):.4f}% | {pct(vol, r2):.4f}% |")
L += ["", "Reading: where the centres coincide the two conventions give the same number; the Josehedron control coincides by symmetry "
      "(site symmetry -4 fixes only the site), so the control cannot discriminate the conventions. Cells whose MES is not site-centred "
      "get a strictly larger ratio under the MES convention; none reaches 47.98% under either."]
open(os.path.join(HERE, "c4_roundness.md"), "w").write("\n".join(L) + "\n")
json.dump([dict(name=name, site=pt_str(site), rho2=frac_str(rho2), mes_centre=pt_str(c), mes_r2=frac_str(r2),
                coincide=(tuple(c) == tuple(site)), round_site=round(pct(vol, rho2), 4), round_mes=round(pct(vol, r2), 4))
           for name, site, rho2, c, r2, vol in rows], open(os.path.join(HERE, "c4_roundness.json"), "w"), indent=1)
print("\n".join(L))
