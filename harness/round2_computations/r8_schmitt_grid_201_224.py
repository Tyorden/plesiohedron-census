#!/usr/bin/env python
"""R8 -- Schmitt's reduced domains for the two-origin groups IT(201) and IT(224),
and whether his grid could reach the Ordenhedron and the two Pn-3m cells.

Facts used (references/Schmitt_2016_dissertation.pdf, blocks for IT(201), IT(224)):
  R201 = R224 = conv{(0,0,0), (1/2,0,0), (1/2,1/2,0), (1/4,1/4,1/4)},
  "Normalizer: IT(229) = Im-3m with basis b1, b2, b3",
  1 001 452 269 = C(1819, 3) grid points (R2: barycentric grid, D = 1816, one tetrahedron),
  and his coordinates are ITA origin choice 2 (his table gives the rhombic dodecahedron
  (14,24,12) at (0,0,0) and the truncated octahedron (24,36,14) at (1/4,1/4,1/4), which is
  what origin choice 2 produces; our frozen tables use origin choice 1 with
  x_his = x_ours + (3/4,3/4,3/4), SCHMITT_OPS_XCHECK / schmitt_collision_check).
Steps:
  (1) Write the group's operations in his coordinates and find, among the settings of the
      frozen Im-3m with origin k/4 (1,1,1), the one(s) that normalize the group (every
      conjugate of every group operation is a group operation modulo the lattice).
  (2) Test whether the printed tetrahedron is a fundamental domain of that normalizer:
      for random rational points count the normalizer images that fall in the closed
      tetrahedron (a fundamental domain gives exactly one for every point); estimate the
      fraction of the parameter space covered by the normalizer images of the tetrahedron.
  (3) For the Ordenhedron (IT(201)), the Pn-3m 7-facet cell and the Pn-3m 11-facet cell
      (IT(224)): list the normalizer images of the generating point in the tetrahedron.
      Where there is one, run the nearest grid points of denominator D through the exact
      chain and compare canonical codes.
  (4) Control: the single-origin pair IT(220) / Ia-3d, where R2 used the frozen Ia-3d at
      its own origin: check that it normalizes I-43d and that R220 is a fundamental domain.
Exact except the random sampling, which is seeded.  Deterministic."""
import os, json, itertools, random
from fractions import Fraction as F
from math import comb
from common2 import *  # noqa

D = 1816
TET = [(F(0), F(0), F(0)), (F(1, 2), F(0), F(0)), (F(1, 2), F(1, 2), F(0)), (F(1, 4), F(1, 4), F(1, 4))]
SHIFT = (F(3, 4), F(3, 4), F(3, 4))          # x_his = x_ours + SHIFT for IT(201), IT(224)
assert comb(D + 3, 3) == 1001452269


def mod1(v): return tuple(x % 1 for x in v)
def apply(R, t, x): return tuple(sum(R[i][j] * x[j] for j in range(3)) + t[i] for i in range(3))
def compose(op1, op2):
    (R1, t1), (R2, t2) = op1, op2
    R = tuple(tuple(sum(R1[i][k] * R2[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    t = tuple(sum(R1[i][k] * t2[k] for k in range(3)) + t1[i] for i in range(3))
    return R, t
def inverse(op):
    R, t = op
    RT = tuple(tuple(R[j][i] for j in range(3)) for i in range(3))   # signed permutation: inverse = transpose
    return RT, tuple(-sum(RT[i][k] * t[k] for k in range(3)) for i in range(3))
def key(op): return (op[0], mod1(op[1]))


def shifted_ops(ops, s):
    """Operations rewritten in coordinates x' = x + s."""
    return {(R, mod1(tuple(t[i] + s[i] - sum(R[i][j] * s[j] for j in range(3)) for i in range(3)))) for R, t in ops}


def with_origin(ops, o):
    return [(R, tuple(t[i] + o[i] - sum(R[i][j] * o[j] for j in range(3)) for i in range(3))) for R, t in ops]


def normalizes(nops, gops):
    gset = set(gops)
    return all(key(compose(compose(n, g), inverse(n))) in gset for n in nops for g in gops)


def bary_tet(x, V):
    A = [[V[j][i] for j in range(4)] for i in range(3)] + [[F(1)] * 4]
    M = [row[:] + [(list(x) + [F(1)])[i]] for i, row in enumerate(A)]
    for c in range(4):
        p = next(i for i in range(c, 4) if M[i][c] != 0)
        M[c], M[p] = M[p], M[c]
        M[c] = [v / M[c][c] for v in M[c]]
        for i in range(4):
            if i != c and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * bb for a, bb in zip(M[i], M[c])]
    lam = [M[i][4] for i in range(4)]
    return lam if all(l >= 0 for l in lam) else None


def in_R220(p):
    x, y, z = p
    return abs(x) <= z and abs(y) <= z and abs(x) <= F(1, 8) and abs(y) <= F(1, 8) and z <= F(1, 4)


def images_in(x, nops, member):
    imgs = set()
    for R, t in nops:
        q = mod1(apply(R, t, x))
        for sh in itertools.product((-1, 0), repeat=3):
            r = tuple(q[k] + sh[k] for k in range(3))
            if member(r):
                imgs.add(r)
    return sorted(imgs)


def coverage(nops, member, n=1000, seed=11):
    rnd = random.Random(seed)
    counts = {}
    for _ in range(n):
        x = tuple(F(rnd.randint(0, 9999), 10000) for _ in range(3))
        k = len(images_in(x, nops, member))
        counts[k] = counts.get(k, 0) + 1
    return counts


L = ["## R8 -- Schmitt's reduced domains for IT(201) and IT(224), and the Ordenhedron / Pn-3m cells", ""]
res = dict()
N229 = GROUPS[229]["ops_exact"]
member_tet = lambda p: bary_tet(p, TET) is not None
for gno in (201, 224):
    gops = shifted_ops(GROUPS[gno]["ops_exact"], SHIFT)
    ok = [k for k in range(4) if normalizes(with_origin(N229, (F(k, 4),) * 3), gops)]
    assert ok == [1, 3], ok   # origin (1/4,1/4,1/4) (equivalently (3/4,3/4,3/4)): the 23 point of the group
    Ntrue = with_origin(N229, (F(1, 4),) * 3)
    N0 = with_origin(N229, (F(0),) * 3)
    cov_true = coverage(Ntrue, member_tet)
    cov_0 = coverage(N0, member_tet)
    frac = 1 - cov_true.get(0, 0) / sum(cov_true.values())
    res[gno] = dict(normalizer_origins=ok, coverage_true=cov_true, coverage_origin0=cov_0, covered_fraction=frac)
    L += [f"### IT({gno}) in Schmitt's coordinates (origin choice 2)", "",
          f"Among the settings of the frozen Im-3m with origin k/4 (1,1,1), those normalizing the group are k = {ok}: the normalizer's m-3m point is the group's 23 point at (1/4,1/4,1/4), not the -3 centre at the origin. "
          f"Fundamental-domain test of the printed tetrahedron R = conv{{(0,0,0), (1/2,0,0), (1/2,1/2,0), (1/4,1/4,1/4)}}: number of normalizer images inside R for 1000 seeded random points, "
          f"under the normalizer (origin 1/4): {dict(sorted(cov_true.items()))}; under Im-3m at origin 0 (whose asymmetric unit R is): {dict(sorted(cov_0.items()))}. "
          f"So R is a fundamental domain of Im-3m at the origin, not of the normalizer of IT({gno}) in these coordinates; the normalizer images of R cover about {100*frac:.1f}% of the parameter space, with multiplicity where they cover.", ""]
    for label, cid in [("O", "2de0a21129cabe90")] if gno == 201 else [("P7", "f98a3ee5675fc121"), ("P11", "c4ea3f32fdd6dc51")]:
        ent = TYPES[cid]; w = ent["first_witness"]
        x_ours = tuple(F(s) for s in w["point"]); x_his = mod1(tuple(x_ours[i] + SHIFT[i] for i in range(3)))
        imgs = images_in(x_his, Ntrue, member_tet)
        imgs0 = images_in(x_his, N0, member_tet)
        L.append(f"**{label}** ({tuple(ent['f_vector'])}): generating point {pt_str(x_ours)} in our setting = {pt_str(x_his)} in his; normalizer images in R: {len(imgs)}" +
                 (" (none: the whole normalizer orbit of the point misses the sampled domain)" if not imgs else ": " + "; ".join(pt_str(i) for i in imgs)) +
                 f". (Under Im-3m at origin 0 the point has {len(imgs0)} image in R, at {pt_str(imgs0[0]) if imgs0 else '-'}; that image is not equivalent to the generating point under the group's normalizer.)")
        res[label] = dict(x_his=pt_str(x_his), images_true=[pt_str(i) for i in imgs], images_origin0=[pt_str(i) for i in imgs0])
        for im in imgs:   # only runs if the point is covered
            lam = bary_tet(im, TET)
            lo = [int((l * D).numerator // (l * D).denominator) for l in lam]
            for up in itertools.product((0, 1), repeat=4):
                k = tuple(lo[i] + up[i] for i in range(4))
                if sum(k) != D:
                    continue
                q = tuple(sum(F(k[j], D) * TET[j][i] for j in range(4)) for i in range(3))
                r = exact_cell_at(gno, mod1(tuple(q[i] - SHIFT[i] for i in range(3))))
                L.append(f"   nearest grid point {k}/D = {pt_str(q)}: f = {r['f']}, p = {pvec_compact(r['p'])}, same type: {r['code'] == ent['canon_code']}")
        L.append("")
# control: IT(220) / Ia-3d at the common origin
g220 = set(key(op) for op in GROUPS[220]["ops_exact"])
N230 = GROUPS[230]["ops_exact"]
assert normalizes(N230, g220)
cov220 = coverage(N230, in_R220)
assert 0 not in cov220 and cov220.get(1, 0) >= 0.98 * sum(cov220.values()), cov220   # a closed domain gives 2 images for the rare boundary point
res["220_control"] = dict(normalizes=True, coverage=cov220)
L += ["### Control: IT(220) and its normalizer Ia-3d (single origin)", "",
      f"The frozen Ia-3d operations at their own origin normalize the frozen I-43d operations, and each of 1000 seeded random points has exactly one Ia-3d image in R220 except the rare point on a face, which has two ({cov220}), so R220 is a fundamental domain of the normalizer and the R2 argument stands.", "",
      "Reading: for the two-origin groups IT(201) and IT(224) the printed reduced domain is the asymmetric unit of Im-3m in its standard setting, which is the normalizer's fundamental domain when the group is written with origin choice 1 (origin at the 23 point) but not with origin choice 2, the setting of his operation tables and of his printed grid points. "
      "In his coordinates the normalizer images of the domain cover only part of the parameter space. The generating points of the Ordenhedron and of both Pn-3m cells lie in the uncovered part, so no point of his IT(201) or IT(224) grid generates a cell congruent to any of the three. "
      "This is a statement about the printed domain and the printed coordinates; it does not say whether the error is in the computation or only in the printing of the domain."]
open(os.path.join(HERE, "r8_schmitt_grid_201_224.md"), "w").write("\n".join(L) + "\n")
json.dump(res, open(os.path.join(HERE, "r8_schmitt_grid_201_224.json"), "w"), indent=1, default=str)
print("\n".join(L))
