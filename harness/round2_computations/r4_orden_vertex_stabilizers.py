#!/usr/bin/env python
"""R4 -- site symmetry of the Ordenhedron's non-simple vertices.

For each vertex v of the exact cell of (1/8, 1/6, 5/12) in IT(201) Pn-3 with
more than three incident facets:
  * H = Stab_G(v): all frozen operations (R, t) with R v + t == v (mod Z^3),
    with the point-group type read from (det, trace) of the linear parts;
  * N(v): the set of orbit sites at the minimal distance from v (the sites
    whose cells meet at v); H permutes N(v), and since the generating point is
    in general position H acts freely on N(v), so |N(v)| is a multiple of |H|;
  * the number of facets of the cell at v (= the degree of the site in the
    Delaunay polytope conv N(v)).
A nontrivial H with |H| not dividing 4 forces |N(v)| > 4, i.e. more than four
cells meet at v for EVERY general-position generating point: that degeneracy
is forced by the group.  Whether the cell itself has >= 4 facets at v (the
paper's 'non-simple vertex') is the degree of the site in the Delaunay
polytope and is read from the cell, not derived from H.  Exact; deterministic."""
import os, json, itertools
from fractions import Fraction as F
from common2 import *  # noqa
import orbit  # noqa: E402

r = rederive("2de0a21129cabe90")
assert r["f"] == (20, 33, 15) and r["stab"] == 1
ec, per = r["ec"], r["period"]
g = GROUPS[201]
verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
inc = [0] * len(verts)
for cyc in ec["facet_cycles"]:
    for i in cyc:
        inc[i] += 1
site = tuple(F(x) for x in ec["center"])
# all orbit sites in a box of translates around the cell
pts = r["pts"]
sites = [tuple(F(p[k] + per * sh[k]) for k in range(3)) for p in pts for sh in itertools.product((-2, -1, 0, 1, 2), repeat=3)]


def pg_type(ops):
    """Name the point group of a stabilizer from its linear parts (subgroups of m-3)."""
    dt = sorted((det3(*R), sum(R[i][i] for i in range(3))) for R, _ in ops)
    n = len(ops)
    has_inv = (-1, -3) in dt
    order3 = sum(1 for d, t in dt if d == 1 and t == 0)
    order2 = sum(1 for d, t in dt if d == 1 and t == -1)
    if n == 1: return "1"
    if n == 2: return "-1" if has_inv else ("2" if order2 else "?")
    if n == 3: return "3"
    if n == 4: return "2/m" if has_inv else "222"
    if n == 6: return "-3" if has_inv else ("32" if order2 == 3 else "?")
    if n == 8: return "mmm"
    if n == 12: return "23" if not has_inv else "?"
    if n == 24: return "m-3"
    return f"order {n}"


L = ["## R4 -- site symmetry of the Ordenhedron's non-simple vertices (IT(201) Pn-3, generating point (1/8, 1/6, 5/12))", "",
     "| vertex (integer scaling, PERIOD 24) | fractional | facets at v | |Stab_G(v)| | point group | |N(v)| (equidistant sites) | |N(v)| mod |H| | H free on N(v) | forced |N(v)| > 4? |",
     "|---|---|---|---|---|---|---|---|---|"]
out = []
for i, v in enumerate(verts):
    if inc[i] <= 3:
        continue
    vf = tuple(x / per for x in v)
    stab = [(R, t) for R, t in g["ops_exact"] if all(((sum(R[a][b] * vf[b] for b in range(3)) + t[a]) - vf[a]).denominator == 1 for a in range(3))]
    d2 = [sum((s[k] - v[k]) ** 2 for k in range(3)) for s in sites]
    m = min(d2)
    N = [s for s, dd in zip(sites, d2) if dd == m]
    assert site in N
    # H acts on N(v): each stabilizer op, with its translation adjusted by the integer vector that
    # makes it fix v EXACTLY (not just mod Z^3), is an isometry of R^3 fixing v; it must permute
    # N(v) as a set, and it fixes no site (the generating point is in general position).
    Nset = set(N)
    free = True
    ident = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for R, t in stab:
        n_adj = tuple(vf[a] - (sum(R[a][b] * vf[b] for b in range(3)) + t[a]) for a in range(3))
        assert all(x.denominator == 1 for x in n_adj)
        tt = tuple(t[a] + n_adj[a] for a in range(3))          # exact op h = (R, tt), h(v) = v
        assert tuple(sum(R[a][b] * vf[b] for b in range(3)) + tt[a] for a in range(3)) == vf
        for s in N:
            sf = tuple(x / per for x in s)
            img = tuple((sum(R[a][b] * sf[b] for b in range(3)) + tt[a]) * per for a in range(3))
            assert img in Nset, "H does not permute N(v)"
            if img == s and not (R == ident and all(x == 0 for x in tt)):
                free = False
    h = len(stab)
    forced = (4 % h != 0)
    out.append(dict(vertex=pt_str(v), frac=pt_str(vf), facets=inc[i], stab=h, pg=pg_type(stab), N=len(N), free=free, forced=forced))
    L.append(f"| {pt_str(v)} | {pt_str(vf)} | {inc[i]} | {h} | {pg_type(stab)} | {len(N)} | {len(N) % h} | {'yes' if free else 'NO'} | {'yes' if forced else 'no'} |")
assert len(out) == 5 and sum(o["facets"] - 3 for o in out) == 6
assert all(o["N"] % o["stab"] == 0 and o["free"] for o in out)
L += ["", "Reading: a stabilizer of order h acting freely on the equidistant sites makes |N(v)| a multiple of h; with h in {3, 6, 12} no multiple of h equals 4, so more than four sites are "
      "equidistant from v for every general-position generating point of Pn-3 on the same symmetry element, and more than four cells meet at v. That degeneracy is forced by the group. "
      "The number of facets of the Ordenhedron at v (4 or 5) equals the degree of the site in the Delaunay polytope conv N(v) and is a property of the cell at this generating point; "
      "a free action of order 3 on six cospherical sites is compatible with a triangular prism (degree 3) as well as an octahedron (degree 4), so the facet count is read from the cell, not derived from H.",
      f"Summary: stabilizer orders {[o['stab'] for o in out]}, point groups {[o['pg'] for o in out]}, |N(v)| = {[o['N'] for o in out]}, facets at v = {[o['facets'] for o in out]}; all five forced in the sense above: {all(o['forced'] for o in out)}."]
open(os.path.join(HERE, "r4_orden_vertex_stabilizers.md"), "w").write("\n".join(L) + "\n")
json.dump(out, open(os.path.join(HERE, "r4_orden_vertex_stabilizers.json"), "w"), indent=1)
print("\n".join(L))
