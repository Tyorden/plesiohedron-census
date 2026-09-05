#!/usr/bin/env python
"""metric.py — exact Gram matrices for the conventional lattices of each crystal
family, as functions of RATIONAL metrical parameters (design doc §1.1
"Metric", §Phase 2). Phase-2 sibling module: nothing here edits an accepted
module; exact_cell_gram.py / sweep_voronoi_gram.py import from here.

All arithmetic is fractions.Fraction / int. Floats appear in exactly one
function (float_embedding) and are a PROPOSAL for Qhull only.

BASIS DECISION (recorded, pre-registered in ANCHORS G2b): every group runs in
the basis of the frozen G1-audited spacegroups.json ops, i.e. the ITA
conventional basis — for trigonal/hexagonal groups that is the HEXAGONAL
basis (a = b, gamma = 120 degrees; rhombohedral groups on hexagonal axes,
choice 'H'). Schmitt 2016 (Appendix B, printed pp. 171-172) changed to an
orthohexagonal C-centered basis B'' = (2b1 + b2, b2, b3) because his
implementation needed a cuboidal sublattice cell and Cartesian-style
coordinates (the hexagonal lattice's Cartesian coordinates involve sqrt 3,
which forced QuadraticExtension<Rational>). The Gram form makes both
unnecessary: in the hexagonal basis the Gram matrix is RATIONAL
([[1, -1/2, 0], [-1/2, 1, 0], [0, 0, (c/a)^2]]), every bisector plane and
vertex stays rational, and the frozen integer rotation parts R are used as-is
(the orthohexagonal basis would give half-integer R entries — exactly the
+-1/2, +-3/2 entries SCHMITT_OPS_XCHECK found in his files — i.e. would require
re-freezing G1 data, which the rules forbid). Compatibility is asserted
exactly per group by gram_compatible(): R^T G R = G for every op.

Metrical parameters follow Schmitt's convention (printed p. 27):
b-ratio = ||b3'|| / ||b1'|| = c/a (a LENGTH ratio, not squared), rational.
Gram matrices are returned SCALED TO INTEGERS (uniform scaling by a positive
rational is an isometry up to similarity and leaves the Voronoi cell's
combinatorial type — and the whole tiling's combinatorics — unchanged):

  cubic         G = I
  tetragonal    G = diag(q^2, q^2, p^2)            for c/a = p/q
  hexagonal     G = [[2q^2, -q^2, 0], [-q^2, 2q^2, 0], [0, 0, 2p^2]]
                (= 2 q^2 * [[1,-1/2,0],[-1/2,1,0],[0,0,(p/q)^2]])
  orthorhombic  G = diag((q1 q2)^2, (p1 q2)^2, (p2 q1)^2)   for b/a=p1/q1,
                c/a = p2/q2   (phase 3; provided for completeness, untested
                by G2b)
  monoclinic / triclinic: NotImplementedError (deferred by design §2.1).

Exact utilities used by the exact clipper:
  gdot(G,u,v), gnorm2(G,u)      G-inner product / squared G-norm
  bisector(G, c, r) -> (a, b)   the halfspace {x : a.x <= b} of points at
                                least as close (in G) to c as to r:
                                a = 2 G (r - c),  b = r^T G r - c^T G c
  inverse_diagonal(G)           exact (G^-1)_ii = cofactor_ii / det G
  coord_bound(G, D2)            integers B_i with B_i^2 >= D2 * (G^-1)_ii, so
                                |x|_G <= D  =>  |x_i| <= B_i  (Cauchy-Schwarz
                                in the G-inner product: x_i = <G^-1 e_i, x>_G)
  is_positive_definite(G)       Sylvester: all leading principal minors > 0
  gram_compatible(entry, G)     R^T G R == G for every op of a frozen group
"""
import itertools
import math
from fractions import Fraction as F

# ---------------------------------------------------------------- basics ---

IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def _as_frac_matrix(G):
    return tuple(tuple(F(x) for x in row) for row in G)


def is_symmetric(G):
    G = _as_frac_matrix(G)
    return all(G[i][j] == G[j][i] for i in range(3) for j in range(3))


def det3(M):
    M = _as_frac_matrix(M)
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def is_positive_definite(G):
    """Sylvester's criterion, exact: symmetric and all leading minors > 0."""
    if not is_symmetric(G):
        return False
    G = _as_frac_matrix(G)
    m1 = G[0][0]
    m2 = G[0][0] * G[1][1] - G[0][1] * G[1][0]
    m3 = det3(G)
    return m1 > 0 and m2 > 0 and m3 > 0


def scale_to_integers(G):
    """Multiply a rational symmetric G by the lcm of its denominators, then
    divide by the gcd of the entries. Returns (integer G, positive rational
    factor s with G_int = s * G). Type-preserving (uniform similarity)."""
    G = _as_frac_matrix(G)
    L = 1
    for row in G:
        for x in row:
            L = L * x.denominator // math.gcd(L, x.denominator)
    ints = [[int(x * L) for x in row] for row in G]
    g = 0
    for row in ints:
        for x in row:
            g = math.gcd(g, abs(x))
    g = g or 1
    ints = tuple(tuple(x // g for x in row) for row in ints)
    return ints, F(L, g)


def gdot(G, u, v):
    """u^T G v, exact."""
    return sum(u[i] * G[i][j] * v[j] for i in range(3) for j in range(3))


def gnorm2(G, u):
    return gdot(G, u, u)


def bisector(G, c, r):
    """Halfspace {x : a.x <= b} = points at least as close (in G) to c as to r.

    |x-r|_G^2 - |x-c|_G^2 = -2 x^T G (r-c) + (r^T G r - c^T G c) >= 0
    <=>  2 (r-c)^T G x <= r^T G r - c^T G c.
    With integer G, c, r both a and b are integers."""
    d = (r[0] - c[0], r[1] - c[1], r[2] - c[2])
    a = tuple(2 * sum(G[i][j] * d[j] for j in range(3)) for i in range(3))
    b = gnorm2(G, r) - gnorm2(G, c)
    return a, b


def cofactor(G, i, j):
    rows = [k for k in range(3) if k != i]
    cols = [k for k in range(3) if k != j]
    m = (G[rows[0]][cols[0]] * G[rows[1]][cols[1]]
         - G[rows[0]][cols[1]] * G[rows[1]][cols[0]])
    return m if (i + j) % 2 == 0 else -m


def inverse_diagonal(G):
    """Exact (G^-1)_ii, i = 0,1,2, as Fractions."""
    d = det3(G)
    assert d > 0, "Gram matrix must be positive definite"
    return tuple(F(cofactor(G, i, i)) / F(d) for i in range(3))


def isqrt_ceil(x):
    """Smallest integer n with n^2 >= x, for rational x >= 0 (exact)."""
    x = F(x)
    assert x >= 0
    n = math.isqrt(x.numerator // x.denominator)     # floor sqrt of floor(x)
    while F(n * n) < x:
        n += 1
    return n


def coord_bound(G, D2):
    """Integers B_i >= D * sqrt((G^-1)_ii) (exactly: B_i^2 >= D2 * (G^-1)_ii).

    Proof of the bound: for any x, x_i = e_i^T x = <G^-1 e_i, x>_G, so by
    Cauchy-Schwarz |x_i| <= |G^-1 e_i|_G |x|_G = sqrt((G^-1)_ii) |x|_G.
    Hence every x with |x|_G^2 <= D2 has |x_i| <= B_i."""
    inv = inverse_diagonal(G)
    return tuple(isqrt_ceil(F(D2) * inv[i]) for i in range(3))


# ------------------------------------------------------------- families ---

def gram_cubic():
    return IDENTITY


def gram_tetragonal(c_over_a):
    """Conventional tetragonal cell a = b, c = (c/a) a, all angles 90 deg.
    Rational c/a = p/q  ->  integer G = diag(q^2, q^2, p^2)  (= q^2 * the
    a = 1 Gram diag(1, 1, (p/q)^2))."""
    r = F(c_over_a)
    assert r > 0
    p, q = r.numerator, r.denominator
    return ((q * q, 0, 0), (0, q * q, 0), (0, 0, p * p))


def gram_hexagonal(c_over_a):
    """Conventional hexagonal cell a = b, gamma = 120 deg, c = (c/a) a.
    a.b = a^2 cos 120 = -a^2/2. Rational c/a = p/q ->
    integer G = 2 q^2 * [[1, -1/2, 0], [-1/2, 1, 0], [0, 0, (p/q)^2]]
             = [[2q^2, -q^2, 0], [-q^2, 2q^2, 0], [0, 0, 2p^2]]."""
    r = F(c_over_a)
    assert r > 0
    p, q = r.numerator, r.denominator
    return ((2 * q * q, -q * q, 0), (-q * q, 2 * q * q, 0), (0, 0, 2 * p * p))


def gram_orthorhombic(b_over_a, c_over_a):
    """Conventional orthorhombic cell, all angles 90 deg. Phase-3 readiness;
    not exercised by G2b."""
    rb, rc = F(b_over_a), F(c_over_a)
    assert rb > 0 and rc > 0
    G = ((F(1), F(0), F(0)), (F(0), rb * rb, F(0)), (F(0), F(0), rc * rc))
    return scale_to_integers(G)[0]


def gram_for_group(entry, params=None):
    """Integer Gram matrix for a frozen spacegroups.json entry.

    params: None for cubic; {'c_over_a': Fraction} for tetragonal and for
    the hexagonal family (trigonal + hexagonal systems, all on hexagonal axes
    in the freeze); {'b_over_a', 'c_over_a'} for orthorhombic. Monoclinic and
    triclinic raise NotImplementedError (deferred by design §2.1)."""
    fam = entry["crystal_family"]
    params = params or {}
    if fam == "cubic":
        G = gram_cubic()
    elif fam == "tetragonal":
        G = gram_tetragonal(params["c_over_a"])
    elif fam == "hexagonal":
        G = gram_hexagonal(params["c_over_a"])
    elif fam == "orthorhombic":
        G = gram_orthorhombic(params["b_over_a"], params["c_over_a"])
    else:
        raise NotImplementedError(
            f"crystal family {fam!r}: metric parameters deferred (design §2.1)")
    assert gram_compatible(entry, G), \
        f"group #{entry['number']}: Gram matrix not preserved by its ops"
    return G


def gram_compatible(entry, G):
    """R^T G R == G exactly for every op (R, t) of the group. This is the
    crystal-family constraint on the metric, checked rather than assumed."""
    ops = entry.get("ops_exact")
    if ops is None:                        # raw JSON entry
        ops = [(tuple(tuple(int(x) for x in row) for row in op["R"]), None)
               for op in entry["ops"]]
    for R, _ in ops:
        # (R^T G R)_ij = sum_kl R_ki G_kl R_lj
        for i in range(3):
            for j in range(3):
                s = sum(R[k][i] * G[k][l] * R[l][j]
                        for k in range(3) for l in range(3))
                if s != G[i][j]:
                    return False
    return True


# --------------------------------------------------------- float proposal ---

def float_embedding(G):
    """Float Cholesky factor A (upper-triangular, x^T G x ~= |A x|^2), for the
    Qhull search phase and plots ONLY. Never feeds a decision."""
    import numpy as np
    Gf = np.array([[float(x) for x in row] for row in G])
    return np.linalg.cholesky(Gf).T


# -------------------------------------------------------------- selftest ---

def _selftest():
    # tetragonal c/a = 7/2 -> diag(4, 4, 49); hexagonal c/a = 1 -> 2*[[1,-1/2,0],..]
    assert gram_tetragonal(F(7, 2)) == ((4, 0, 0), (0, 4, 0), (0, 0, 49))
    assert gram_hexagonal(1) == ((2, -1, 0), (-1, 2, 0), (0, 0, 2))
    assert gram_hexagonal(F(1, 2)) == ((8, -4, 0), (-4, 8, 0), (0, 0, 2))
    for G in (gram_cubic(), gram_tetragonal(F(797, 1000)), gram_hexagonal(F(3, 7))):
        assert is_positive_definite(G)
    assert not is_positive_definite(((1, 2, 0), (2, 1, 0), (0, 0, 1)))
    # hexagonal lattice: |a| = |b|, angle 120 -> |a + b| = |a|
    G = gram_hexagonal(1)
    assert gnorm2(G, (1, 0, 0)) == gnorm2(G, (0, 1, 0)) == gnorm2(G, (1, 1, 0)) == 2
    assert gnorm2(G, (1, -1, 0)) == 6                      # |a - b|^2 = 3 a^2
    # bisector: the midpoint lies on the plane, c strictly inside
    c, r = (0, 0, 0), (2, 4, 6)
    a, b = bisector(G, c, r)
    mid = (F(1), F(2), F(3))
    assert sum(a[i] * mid[i] for i in range(3)) == b
    assert sum(a[i] * c[i] for i in range(3)) < b
    # coordinate bound: every lattice vector with |x|_G^2 <= D2 obeys |x_i| <= B_i
    # (brute force check on a box much larger than the bound)
    for G in (gram_hexagonal(F(1, 3)), gram_tetragonal(F(5, 2))):
        D2 = 200
        B = coord_bound(G, D2)
        big = max(B) + 3
        for x in itertools.product(range(-big, big + 1), repeat=3):
            if gnorm2(G, x) <= D2:
                assert all(abs(x[i]) <= B[i] for i in range(3)), (G, x, B)
    # inverse diagonal against a hand value: hexagonal a=1 G=[[1,-1/2],[-1/2,1]]*2
    inv = inverse_diagonal(gram_hexagonal(1))
    assert inv == (F(2, 3), F(2, 3), F(1, 2)), inv
    # scale_to_integers
    Gi, s = scale_to_integers(((1, F(-1, 2), 0), (F(-1, 2), 1, 0), (0, 0, F(9, 4))))
    assert Gi == ((4, -2, 0), (-2, 4, 0), (0, 0, 9)) and s == 4, (Gi, s)
    print("metric.py selftest: PASS (families / PD / bisector / coordinate "
          "bound brute-forced / inverse diagonal / integer scaling)")


if __name__ == "__main__":
    _selftest()
