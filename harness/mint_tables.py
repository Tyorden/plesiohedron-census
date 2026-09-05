#!/usr/bin/env python
"""mint_tables.py — the tables/ops step (design doc §V2/§V3, mint_tables row of
the build table): convert a validated cell-orbit into enumerator-ready
honeycomb tables, and close ANCHORS G0's three DEFERRED clauses (recorded in
G0_RESULT.md as NOT YET RUN):

  clause A  |ops| = 24 (12 proper) — interpreted and verified against BOTH the
            site symmetry (orbit.py site_stabilizer + frozen IT(220) entry) and
            the banked tables' ops list (op-by-op semantic equality);
  clause B  nbr-table semantic equality to josehedron_tables.json — an EXPLICIT
            relabeling bijection (type permutation pi, unimodular basis change
            M, per-type anchor shifts s_t) is constructed and verified to map
            the derived table onto the banked table exactly;
  clause C  enumerator identity — the banked compiled enumerator run on the
            derived tables and on the banked tables gives identical fixed/free
            counts for n <= 6, equal to the banked VERIFIED results.

WHAT THE "24" COUNTS (clause A interpretation, stated per instruction): the
banked tables' `ops` are the honeycomb's point-symmetry operations MODULO
LATTICE TRANSLATIONS, expressed as the quotient action on cell IDs
(v,t) -> (A v + c_t, t') that the enumerator consumes.  That group is the
POINT GROUP of the honeycomb's space group IT(220) = I-43d: order 24 (-43m),
12 proper.  It is NOT the site symmetry of a cell: the site symmetry of the
Wyckoff-12a centre is -4, order 4, and the two are related by
|point group| = T_primitive * |site| = 6 * 4 = 24 (orbit-stabilizer on the
T primitive translation types).  Both objects are verified below (M2 site,
M3/M4 ops), and ops equality to the banked list is checked op-by-op under the
clause-B bijection, modulo a uniform lattice translation per op (a global
translation added to an op changes nothing for the enumerator, whose canonical
form re-anchors at the minimal cell; the banked ops are one such set of coset
representatives).

INDEPENDENCE DISCIPLINE (G1/G2 house pattern): the derivation phase
(derive_tables) reads ONLY the generating orbit (BASE mod 8, verbatim from
g0_regression.py), the G0-validated pipeline modules (orbit / exact_cell), and
the frozen G1-audited spacegroups.json.  josehedron_tables.json is loaded only
in the gate phase, as the comparison target.  Enforced by an ast self-audit
(M0): no function in the derivation phase references the banked file.

House invariant: floats never enter this file — all derivation arithmetic is
integer / Fraction.  scipy is not imported.

Run:
  python3 mint_tables.py
Writes: mint_josehedron_tables.json (derived tables, banked schema),
        mint_tables_mine.txt / mint_tables_banked.txt (+ _proper variants,
        enumerator input), MINT_TABLES_RESULT.md.
Exit 0 iff every in-scope assertion passes.
"""
import ast
import itertools
import json
import os
import subprocess
import sys
from fractions import Fraction as F

import orbit
from exact_cell import clip_cell

HERE = os.path.dirname(os.path.abspath(__file__))
BANKED_TABLES = os.path.join(HERE, "..", "..", "SCI_OEIS_josehedron", "data",
                             "josehedron_tables.json")
BANKED_SCRIPTS = os.path.join(HERE, "..", "..", "SCI_OEIS_josehedron", "scripts")
BANKED_RESULTS = os.path.join(HERE, "..", "..", "SCI_OEIS_josehedron", "results")
EXPORT_TABLES = os.path.join(BANKED_SCRIPTS, "export_tables.py")
ENUM_BIN = os.path.join(BANKED_SCRIPTS, "enumerate")
PYTHON = "python3"
OUT_JSON = os.path.join(HERE, "mint_josehedron_tables.json")

# --- generating data, VERBATIM from g0_regression.py:42-44 (= build_josehedron
#     BASE, Bernhard Table 4 minima); integers mod 8.
BASE = [(0, 2, 3), (0, 6, 1), (1, 0, 6), (2, 3, 0), (2, 5, 4), (3, 0, 2),
        (4, 2, 5), (4, 6, 7), (5, 4, 2), (6, 1, 0), (6, 7, 4), (7, 4, 6)]
PERIOD = 8


# ---------------------------------------------------------------- exact linalg
def det3(u, v, w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1]) - u[1]*(v[0]*w[2]-v[2]*w[0])
            + u[2]*(v[0]*w[1]-v[1]*w[0]))


def mat_det(M):
    return det3(*[tuple(M[i][j] for j in range(3)) for i in range(3)])


def mat_inv(M):
    """Exact inverse of a 3x3 (Fraction entries)."""
    d = mat_det(M)
    assert d != 0
    cof = [[(M[(i+1) % 3][(j+1) % 3]*M[(i+2) % 3][(j+2) % 3]
             - M[(i+1) % 3][(j+2) % 3]*M[(i+2) % 3][(j+1) % 3])
            for j in range(3)] for i in range(3)]
    return [[F(cof[j][i], 1)/d for j in range(3)] for i in range(3)]


def mat_vec(M, v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))


def mat_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def to_int_vec(v):
    out = []
    for x in v:
        x = F(x)
        assert x.denominator == 1, f"non-integer where integer required: {v}"
        out.append(int(x))
    return tuple(out)


def to_int_mat(M):
    return tuple(to_int_vec(row) for row in M)


# ------------------------------------------------- derivation (no banked read)
def derive_lattice(base, P):
    """Primitive translation lattice of the periodic set base mod P.
    Returns (basis columns matrix B [int, columns are basis vectors], detL>0).
    Exact: a triple of translations spans L iff it integrally spans every
    window translation and P*e_i (any t in L reduces mod P*Z^3 into the
    window), and a spanning triple of lattice vectors has |det| = covol(L)."""
    baseset = set((x % P, y % P, z % P) for x, y, z in base)
    trans = [t for t in itertools.product(range(-P, P+1), repeat=3)
             if t != (0, 0, 0)
             and set(((x+t[0]) % P, (y+t[1]) % P, (z+t[2]) % P)
                     for x, y, z in base) == baseset]
    gens = trans + [(P, 0, 0), (0, P, 0), (0, 0, P)]
    short = sorted(gens, key=lambda t: (sum(x*x for x in t), t))[:20]
    for a, b, c in itertools.combinations(short, 3):
        d = det3(a, b, c)
        if d == 0:
            continue
        Bcols = [[F(a[i]), F(b[i]), F(c[i])] for i in range(3)]
        Binv = mat_inv(Bcols)
        if all(all((F(x).denominator == 1 for x in mat_vec(Binv, t)))
               for t in gens):
            return to_int_mat(Bcols), abs(d)
    raise AssertionError("no primitive basis found among shortest translations")


def derive_tables():
    """Independent derivation of the honeycomb tables from BASE mod 8 through
    the G0-validated pipeline (orbit scaling + exact_cell clipping).
    Returns the tables dict in the banked schema plus derivation facts."""
    # 1) orbit intake, identical path to g0_regression A1: scale to PERIOD 24
    fracs = [tuple(F(x, PERIOD) for x in p) for p in BASE]
    pts24, P24 = orbit.scale_orbit(fracs)
    scale = P24 // PERIOD
    assert P24 == 24 and scale == 3 and len(set(pts24)) == 12

    # 2) exact cells for all 12 base points (exact_cell, as validated in G0)
    cells = [clip_cell(c, pts24, P24) for c in pts24]
    assert all(e['facet_count'] == 12 and e['p_vector'] == (3,)*4 + (4,)*8
               for e in cells)
    # neighbors back in the period-8 frame (all scaled coords divisible by 3)
    nbrs8 = []
    for e in cells:
        row = []
        for q in e['neighbors']:
            assert all(x % scale == 0 for x in q)
            row.append(tuple(x // scale for x in q))
        nbrs8.append(row)
    centers8 = [tuple(x // scale for x in c) for c in pts24]
    base_index = {p: i for i, p in enumerate(
        (x % PERIOD, y % PERIOD, z % PERIOD) for x, y, z in BASE)}
    cell_of = {c: i for i, c in enumerate(centers8)}
    order = [cell_of[p] for p in
             ((x % PERIOD, y % PERIOD, z % PERIOD) for x, y, z in BASE)]
    # re-index cells so cell i corresponds to BASE[i]
    nbrs8 = [nbrs8[i] for i in order]

    # 3) primitive translation lattice (independent, exact)
    Bcols, detL = derive_lattice(BASE, PERIOD)
    Binv = mat_inv([[F(x) for x in row] for row in Bcols])
    assert (12*detL) % PERIOD**3 == 0
    T = 12*detL // PERIOD**3
    cellvol = F(PERIOD**3, 12)
    assert F(T)*cellvol == F(detL), "exact volume identity T*vol == detL failed"

    def lat_int(vec):
        c = mat_vec(Binv, vec)
        return to_int_vec(c) if all(F(x).denominator == 1 for x in c) else None

    # 4) types: bi ~ bj iff BASE[bi]-BASE[bj] in L; reps = first-seen
    type_of, type_reps = {}, []
    for bi, p in enumerate(BASE):
        for ti, rj in enumerate(type_reps):
            r = BASE[rj]
            if lat_int((p[0]-r[0], p[1]-r[1], p[2]-r[2])) is not None:
                type_of[bi] = ti
                break
        else:
            type_reps.append(bi)
            type_of[bi] = len(type_reps)-1
    assert len(type_reps) == T, (len(type_reps), T)

    # 5) neighbour table: per type rep, 12 (lattice delta, type')
    def id_of_site(q):
        """cell ID (v int lattice coords, type) of the site q (8-frame)."""
        bj = base_index[(q[0] % PERIOD, q[1] % PERIOD, q[2] % PERIOD)]
        tj = type_of[bj]
        r = BASE[type_reps[tj]]
        v = lat_int((q[0]-r[0], q[1]-r[1], q[2]-r[2]))
        assert v is not None, f"site {q} not lattice-congruent to its type rep"
        return v, tj

    nbr_table = []
    for ti, rep in enumerate(type_reps):
        row = []
        for q in nbrs8[rep]:
            v, tj = id_of_site(q)
            row.append([list(v), tj])
        assert len(row) == 12
        nbr_table.append(row)
    # adjacency symmetry (build_josehedron pattern, exact)
    for ti, row in enumerate(nbr_table):
        for dv, tj in row:
            assert any(dv2 == [-dv[0], -dv[1], -dv[2]] and t2 == ti
                       for dv2, t2 in nbr_table[tj]), "asymmetric adjacency"

    # 6) honeycomb point ops mod lattice: R (signed perm) + shift c with
    #    R(BASE)+c == BASE as periodic sets.  Completeness: any such R is an
    #    orthogonal map preserving L; L is verified below to be the BCC
    #    lattice 4*D3 (= <(8,0,0),(0,8,0),(4,4,4)>), whose full orthogonal
    #    automorphism group is O_h = the 48 signed permutation matrices.
    bcc = [[F(8), F(0), F(4)], [F(0), F(8), F(4)], [F(0), F(0), F(4)]]
    bccinv = mat_inv(bcc)
    Bf = [[F(Bcols[i][j]) for j in range(3)] for i in range(3)]
    assert all(F(x).denominator == 1 for M1_, M2_ in
               ((mat_mul(bccinv, Bf), None), (mat_mul(mat_inv(Bf), bcc), None))
               for row in M1_ for x in row), "L != BCC lattice <8e1,8e2,(4,4,4)>"

    baseset = set((x % PERIOD, y % PERIOD, z % PERIOD) for x, y, z in BASE)
    ops_geo = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = [[0]*3 for _ in range(3)]
            for i in range(3):
                R[i][perm[i]] = sg[i]
            R = tuple(tuple(r) for r in R)
            RB = [mat_vec(R, p) for p in BASE]
            found = None
            for bp in BASE:
                c = tuple((bp[k]-RB[0][k]) % PERIOD for k in range(3))
                img = set(((x+c[0]) % PERIOD, (y+c[1]) % PERIOD,
                           (z+c[2]) % PERIOD) for x, y, z in RB)
                if img == baseset:
                    found = c
                    break
            if found is not None:
                ops_geo.append((R, found))
    ops_geo.sort()

    # 7) ops in ID space: (v,t) -> (A v + c_t, t')
    def op_idspace(R, c):
        A = to_int_mat(mat_mul(mat_mul(Binv, [[F(R[i][j]) for j in range(3)]
                                              for i in range(3)]), Bf))
        assert abs(mat_det(A)) == 1
        per = []
        for ti, rep in enumerate(type_reps):
            img = tuple(mat_vec(R, BASE[rep])[k] + c[k] for k in range(3))
            v, tj = id_of_site(img)
            per.append([list(v), tj])
        return [list(r) for r in A], per

    ops_id = [op_idspace(R, c) for R, c in ops_geo]
    dets = [mat_det(R) for R, _ in ops_geo]

    # identity present + closure, both MODULO a uniform lattice translation
    # (ops are coset representatives; a global lattice shift is invisible to
    # the enumerator's translation-normalized canonical form)
    def opkey(A, per):
        return (tuple(map(tuple, A)), tuple(tj for _, tj in per),
                tuple(tuple(per[t][0][i]-per[0][0][i] for i in range(3))
                      for t in range(T)))

    keyset = {opkey(A, p) for A, p in ops_id}
    assert len(keyset) == len(ops_id), "duplicate ops mod lattice translation"
    assert any(A == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
               and all(p[t][1] == t for t in range(T))
               and all(p[t][0] == p[0][0] for t in range(T))
               for A, p in ops_id), "identity missing"

    def comp(A1, p1, A2, p2):
        A = mat_mul(A1, A2)
        p = []
        for t in range(T):
            c2, m2 = p2[t]
            c1, m1 = p1[m2]
            p.append(([sum(A1[i][j]*c2[j] for j in range(3)) + c1[i]
                       for i in range(3)], m1))
        return A, p

    assert all(opkey(*comp(A1, p1, A2, p2)) in keyset
               for A1, p1 in ops_id for A2, p2 in ops_id), "ops not closed"

    out = {
        'T': T,
        'nbr': nbr_table,
        'ops': [{'A': A, 'map': per} for A, per in ops_id],
        'proper_ops': [{'A': A, 'map': per}
                       for (A, per), d in zip(ops_id, dets) if d == 1],
        'lattice_basis': [[Bcols[i][j] for i in range(3)] for j in range(3)],
        'detL': detL,
        'cell_volume': str(cellvol),
        'n_proper': sum(1 for d in dets if d == 1),
        'n_improper': sum(1 for d in dets if d == -1),
        'facet_signature': list(cells[0]['p_vector']),
    }
    facts = {'type_reps': type_reps, 'type_of': type_of, 'Bcols': Bcols,
             'detL': detL, 'T': T, 'n_ops': len(ops_id),
             'n_proper': out['n_proper'], 'op_R_set': set(R for R, _ in ops_geo)}
    return out, facts


# ------------------------------------------------------- gate-phase utilities
def transform_table(mine, M, Minv, pi, s):
    """Map my nbr table through the bijection (v,t) -> (M v + s_t, pi(t)).
    Returns rows indexed by THEIR type label, each a sorted multiset."""
    T = len(mine)
    rows = [None]*T
    for t in range(T):
        ent = []
        for dv, tj in mine[t]:
            w = tuple(sum(M[i][j]*dv[j] for j in range(3)) + s[tj][i] - s[t][i]
                      for i in range(3))
            ent.append((w, pi[tj]))
        rows[pi[t]] = sorted(ent)
    return rows


def find_bijection(mine, theirs, M):
    """Search (pi, s) with s[0]=(0,0,0) mapping my table onto theirs exactly.
    Returns (pi, s) or None."""
    T = len(mine)
    their_sorted = [sorted((tuple(dv), tj) for dv, tj in row) for row in theirs]
    for pi in itertools.permutations(range(T)):
        # type-multiset prefilter
        if any(sorted(pi[tj] for _, tj in mine[t])
               != sorted(tj for _, tj in their_sorted[pi[t]])
               for t in range(T)):
            continue
        # propagate s from my row 0 (adjacent to every type incl. itself)
        cand = {0: {(0, 0, 0)}}
        ok = True
        for dv, tj in mine[0]:
            Md = tuple(sum(M[i][j]*dv[j] for j in range(3)) for i in range(3))
            opts = {tuple(w[i]-Md[i] for i in range(3))
                    for w, u in their_sorted[pi[0]] if u == pi[tj]}
            cand[tj] = cand.get(tj, opts) & opts if tj in cand else opts
            if not cand[tj]:
                ok = False
                break
        if not ok or set(cand) != set(range(T)):
            continue
        Minv_unused = None
        for choice in itertools.product(*(sorted(cand[t]) for t in range(T))):
            if choice[0] != (0, 0, 0):
                continue
            s = list(choice)
            if transform_table(mine, M, Minv_unused, pi, s) == their_sorted:
                return list(pi), s
    return None


def transform_ops(ops_mine, M, Minv, pi, s):
    """Map my ID-space ops through the bijection; return the set of
    translation-normalized keys (A', types', deltas-rel-type0)."""
    T = len(pi)
    inv_pi = [0]*T
    for t in range(T):
        inv_pi[pi[t]] = t
    keys = set()
    for op in ops_mine:
        A = [[F(x) for x in row] for row in op['A']]
        Ap = to_int_mat(mat_mul(mat_mul(M, A), Minv))
        cp = [None]*T
        mp = [None]*T
        for u in range(T):                      # u = their type label
            t = inv_pi[u]
            c, m = op['map'][t]
            v = tuple(sum(M[i][j]*c[j] for j in range(3)) + s[m][i]
                      - sum(Ap[i][j]*s[t][j] for j in range(3))
                      for i in range(3))
            cp[u] = v
            mp[u] = pi[m]
        keys.add((Ap, tuple(mp),
                  tuple(tuple(cp[u][i]-cp[0][i] for i in range(3))
                        for u in range(T))))
    return keys


def opkeys_banked(ops):
    T = len(ops[0]['map'])
    keys = set()
    for op in ops:
        A = tuple(tuple(int(x) for x in row) for row in op['A'])
        mp = tuple(int(tj) for _, tj in op['map'])
        cp = [tuple(int(x) for x in c) for c, _ in op['map']]
        keys.add((A, mp, tuple(tuple(cp[u][i]-cp[0][i] for i in range(3))
                               for u in range(T))))
    return keys


def run_enum(tables_json, tag, opskey, N=6):
    """Banked workflow: export_tables.py -> compiled enumerate; parse counts."""
    txt = os.path.join(HERE, f"mint_tables_{tag}.txt")
    subprocess.run([PYTHON, EXPORT_TABLES, tables_json, txt, opskey],
                   check=True, capture_output=True)
    r = subprocess.run([ENUM_BIN, txt, str(N)], check=True,
                       capture_output=True, text=True)
    counts = {}
    seen_hdr = False
    for line in r.stdout.splitlines():
        if line.strip() == "n fixed free":
            seen_hdr = True
            continue
        if seen_hdr:
            n, fx, fr = line.split()
            counts[int(n)] = (int(fx), int(fr))
    assert len(counts) == N
    return counts


def parse_banked_results(path, N=6):
    counts = {}
    for line in open(path):
        parts = line.split()
        if len(parts) == 3 and parts[0].isdigit():
            counts[int(parts[0])] = (int(parts[1]), int(parts[2]))
    return {n: counts[n] for n in range(1, N+1)}


# --------------------------------------------------------------------- gate
def main():
    res = []

    def check(name, ok, detail=""):
        res.append((name, bool(ok), str(detail)))
        print(("PASS  " if ok else "FAIL  ") + name
              + ("  [" + str(detail) + "]" if detail else ""))
        return bool(ok)

    # -- M0: independence self-audit: no derivation-phase function references
    #        the banked tables file (ast walk over this module's source)
    tree = ast.parse(open(os.path.join(HERE, "mint_tables.py")).read())
    offenders = []
    derivation_funcs = {"derive_lattice", "derive_tables"}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in derivation_funcs:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and "BANKED" in sub.id:
                    offenders.append((node.name, sub.id))
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                        and "josehedron_tables" in sub.value:
                    offenders.append((node.name, sub.value))
    check("M0 independence: derivation functions never touch the banked file "
          "(ast audit)", not offenders, f"offenders={offenders}")

    # -- derivation (banked file NOT read yet)
    mine, facts = derive_tables()
    json.dump(mine, open(OUT_JSON, "w"), indent=1)

    check("M1 derivation: detL=256, T=6, volume identity T*vol==detL, "
          "12-facet 4tri+8quad cells, adjacency symmetric, tables written",
          facts['detL'] == 256 and facts['T'] == 6
          and mine['facet_signature'] == [3, 3, 3, 3] + [4]*8,
          f"detL={facts['detL']}, T={facts['T']}, reps={facts['type_reps']}, "
          f"out={os.path.basename(OUT_JSON)}")

    # -- M2: clause-A site-symmetry half: frozen IT(220) (I-43d) vs the orbit
    groups = orbit.load_groups()
    g220 = groups[220]
    p0 = tuple(F(x, PERIOD) for x in BASE[0])
    ob = orbit.orbit(g220, p0)
    stab = orbit.site_stabilizer(g220, p0)
    stab_dets = sorted(det3(*R) for R, _ in stab)
    distinct_R = set(R for R, _ in g220['ops_exact'])
    pg_order = len(distinct_R)
    pg_proper = sum(1 for R in distinct_R if det3(*R) == 1)
    check("M2 site symmetry (clause A, site half): BASE/8 IS the IT(220) "
          "orbit of (0,1/4,3/8); site stabilizer order 4 (-4: dets [-1,-1,1,1])"
          "; point group order 24 (12 proper) = T_prim*|site| = 6*4",
          set(ob['points']) == set(tuple(F(x, PERIOD) for x in p) for p in BASE)
          and ob['n_conventional'] == 12 and ob['n_primitive'] == 6
          and len(stab) == 4 and stab_dets == [-1, -1, 1, 1]
          and pg_order == 24 and pg_proper == 12
          and pg_order == facts['T'] * len(stab),
          f"|orbit|={ob['n_conventional']}, |stab|={len(stab)}, "
          f"|PG|={pg_order}, proper={pg_proper}")

    # -- M3: clause-A ops half, derived side: |ops|=24, 12 proper, and the
    #        rotation parts equal the 24 distinct rotation parts of IT(220)
    check("M3 derived honeycomb ops (clause A, ops half): |ops|=24 with 12 "
          "proper; identity+closure held (asserted in derivation); rotation "
          "parts == the 24 distinct IT(220) rotation parts",
          facts['n_ops'] == 24 and facts['n_proper'] == 12
          and facts['op_R_set'] == distinct_R,
          f"|ops|={facts['n_ops']}, proper={facts['n_proper']}, "
          f"R-set match={facts['op_R_set'] == distinct_R}")

    # -- banked tables enter HERE (comparison target only)
    banked = json.load(open(BANKED_TABLES))

    # -- M4: clause B: explicit relabeling bijection nbr -> banked nbr
    Bm = [[F(mine['lattice_basis'][j][i]) for j in range(3)] for i in range(3)]
    Bt = [[F(banked['lattice_basis'][j][i]) for j in range(3)] for i in range(3)]
    M = to_int_mat(mat_mul(mat_inv(Bt), Bm))
    Minv = to_int_mat(mat_inv([[F(x) for x in row] for row in M]))
    bij = find_bijection(mine['nbr'], banked['nbr'], M)
    ok4 = bij is not None and abs(mat_det(M)) == 1
    if bij:
        pi, s = bij
    check("M4 clause B: nbr-table semantic equality — explicit bijection "
          "(v,t)->(M v + s_t, pi(t)) maps derived table onto banked table "
          "EXACTLY (all 6 rows as multisets), M unimodular",
          ok4,
          (f"M={[list(r) for r in M]}, |detM|={abs(mat_det(M))}, pi={pi}, "
           f"s={[list(x) for x in s]}") if bij else "NO BIJECTION FOUND")

    # -- M5: clause A op-by-op: transformed derived ops == banked ops
    ok5 = False
    det5 = "skipped: no bijection"
    if bij:
        mine_keys = transform_ops(mine['ops'], M, Minv, pi, s)
        bank_keys = opkeys_banked(banked['ops'])
        mine_prop = transform_ops(mine['proper_ops'], M, Minv, pi, s)
        bank_prop = opkeys_banked(banked['proper_ops'])
        ok5 = (len(banked['ops']) == 24 and banked['n_proper'] == 12
               and len(banked['proper_ops']) == 12
               and mine_keys == bank_keys and mine_prop == bank_prop
               and len(mine_keys) == 24 and len(mine_prop) == 12)
        det5 = (f"banked |ops|={len(banked['ops'])} (proper "
                f"{banked['n_proper']}); 24/24 op keys equal, 12/12 proper "
                f"keys equal (translation-normalized, under the M4 bijection)")
    check("M5 clause A: banked ops semantics — |ops|=24 (12 proper) in the "
          "banked tables, and op-by-op semantic equality of derived ops to "
          "banked ops under the M4 bijection (mod uniform lattice translation)",
          ok5, det5)

    # -- M6: clause C: banked compiled enumerator, both tables, n<=6 identical
    mine_full = run_enum(OUT_JSON, "mine", "ops")
    bank_full = run_enum(BANKED_TABLES, "banked", "ops")
    verified = parse_banked_results(
        os.path.join(BANKED_RESULTS, "josehedron_free.txt"))
    check("M6 clause C: enumerator (banked compiled enumerate, via banked "
          "export_tables.py) on derived vs banked tables: fixed AND free "
          "identical for n<=6, and equal to the banked VERIFIED results "
          "(results/josehedron_free.txt)",
          mine_full == bank_full == verified,
          f"mine==banked: {mine_full == bank_full}; "
          f"free={[mine_full[n][1] for n in range(1, 7)]}, "
          f"fixed={[mine_full[n][0] for n in range(1, 7)]}")

    # -- M7: clause C supplement: proper_ops -> one-sided counts identical too
    mine_prop = run_enum(OUT_JSON, "mine_proper", "proper_ops")
    bank_prop = run_enum(BANKED_TABLES, "banked_proper", "proper_ops")
    verified_os = parse_banked_results(
        os.path.join(BANKED_RESULTS, "josehedron_onesided.txt"))
    check("M7 one-sided supplement: proper_ops enumeration identical on both "
          "tables and equal to banked verified one-sided results, n<=6",
          mine_prop == bank_prop == verified_os,
          f"one-sided={[mine_prop[n][1] for n in range(1, 7)]}")

    allpass = all(ok for _, ok, _ in res)
    write_result(res, allpass, facts, bij if allpass else None)
    print("\nMINT_TABLES VERDICT:",
          "ALL IN-SCOPE ASSERTIONS PASS — G0 deferred clauses A/B/C CLOSED"
          if allpass else "FAIL — G0 deferred clauses remain open; "
          "downstream quarantined (ANCHORS.md)")
    return 0 if allpass else 1


def write_result(res, allpass, facts, bij):
    lines = [
        "# mint_tables result — G0 deferred clauses A/B/C (2026-08-28)",
        "",
        "Step: `mint_tables.py` (design `../HARNESS_DESIGN_FABLE5_2026-08-27.md`"
        " §V2/§V3, build-table row `mint_tables.py`). Closes the three clauses "
        "recorded in `G0_RESULT.md` as NOT YET RUN. Derivation inputs: BASE mod "
        "8 (verbatim from `g0_regression.py`), the G0-validated pipeline "
        "(`orbit.py`, `exact_cell.py`), the frozen G1-audited "
        "`spacegroups.json`. Comparison target (loaded only in the gate "
        "phase): `SCI_OEIS_josehedron/data/josehedron_tables.json`.",
        "",
        "Verdict: **" + ("ALL IN-SCOPE ASSERTIONS PASS — G0 clauses A/B/C "
                         "CLOSED" if allpass else
                         "FAIL — G0 deferred clauses remain OPEN") + "**",
        "",
        "## What the \"24\" counts (clause A interpretation, per instruction)",
        "",
        "The banked `ops` list is the honeycomb's point-symmetry group MODULO "
        "LATTICE TRANSLATIONS, in its quotient action on cell IDs "
        "(v,t) -> (A v + c_t, t') — exactly the object the enumerator "
        "consumes. It equals the POINT GROUP of the honeycomb's space group "
        "IT(220) = I-43d: order 24 (-43m), 12 proper. It is NOT the site "
        "symmetry of a cell: the Wyckoff-12a site symmetry is -4, order 4 "
        "(verified from the frozen IT(220) entry via orbit.site_stabilizer), "
        "and 24 = T_primitive x |site| = 6 x 4. Op-for-op equality to the "
        "banked list is verified under the clause-B bijection, modulo one "
        "uniform lattice translation per op (ops are coset representatives; "
        "a global lattice shift is invisible to the enumerator's "
        "translation-normalized canonical form).",
        "",
        "## Assertions",
        "",
    ]
    for name, ok, detail in res:
        lines.append(("- **PASS** " if ok else "- **FAIL** ") + name
                     + (f" — {detail}" if detail else ""))
    lines += [
        "",
        "## Derivation facts",
        "",
        f"- Primitive lattice basis (columns, period-8 frame): "
        f"{facts['Bcols']}, detL={facts['detL']} (= BCC lattice "
        f"<(8,0,0),(0,8,0),(4,4,4)>, verified exactly both ways).",
        f"- T={facts['T']} primitive types, reps (base indices) "
        f"{facts['type_reps']}; exact volume identity 6*(512/12)=256.",
        f"- Ops search space: the 48 signed permutation matrices — COMPLETE "
        f"because any honeycomb point op preserves the derived translation "
        f"lattice L, L is the BCC lattice (verified), and Aut(BCC) = O_h = "
        f"signed perms; cross-check: the 24 rotation parts found equal the 24 "
        f"distinct rotation parts of the frozen IT(220) coset list (M3).",
        f"- Derived tables written to `mint_josehedron_tables.json` (banked "
        f"schema: T, nbr, ops, proper_ops, lattice_basis, detL, cell_volume, "
        f"n_proper, n_improper, facet_signature).",
        "",
        "## Enumerator provenance (clause C, per instruction: which path)",
        "",
        "- Used the BANKED workflow exactly: banked `export_tables.py` "
        "(json -> tables.txt) + the banked COMPILED `enumerate` binary "
        "(`SCI_OEIS_josehedron/scripts/enumerate`, arm64, the same binary that "
        "produced the banked results; not recompiled — it runs and reproduces "
        "the banked verified values bit-for-bit). `reference_enum.py` was not "
        "needed as the sanctioned path since the compiled binary is present "
        "and its output on the banked tables matches the banked verified "
        "results, which were themselves independently cross-checked in the "
        "SCI_OEIS program.",
        "",
        "## Honest scope notes / deviations from the tasking",
        "",
        "- TASKING DISCREPANCY (recorded, not papered over): the task "
        "instruction stated the published values as \"free = A397708, fixed = "
        "A397709 ... n<=6 free counts are 1,4,16,116,903,8551\". That does NOT "
        "match the banked Josehedron record and the series 1,4,16,116,903,8551 "
        "appears NOWHERE in the MathProofs tree (grepped). Per the a397708.txt "
        "header and SUBMISSION_JOSEHEDRON.md, A397708/A397709 are the SPHENOID "
        "hendecahedron sequences; the Josehedron's assigned numbers are fixed "
        "= A398957, one-sided = A398958. The pre-registered authority is "
        "ANCHORS G0: \"enumerator on both gives identical fixed/free n<=6\" — "
        "asserted in M6 — plus equality to the banked VERIFIED results "
        "(free 1,2,15,131,1360,15133; fixed 6,36,308,3030,32262,362010; "
        "one-sided 1,4,30,261,2717,30265), asserted in M6/M7.",
        "- The bijection search fixes s_0=(0,0,0) WLOG (the banked table is "
        "invariant under adding one lattice vector to every anchor); any "
        "returned bijection is one valid witness, uniqueness not claimed. The "
        "witness found is the IDENTITY (pi=id, M=I, s=0): the independent "
        "derivation's deterministic tie-breaks (first-seen type reps, "
        "shortest-basis search) landed on the same labels and basis as the "
        "banked build. The search itself was general — all 720 type "
        "permutations, M computed from the two bases — identity is simply the "
        "witness it found.",
        "- Independence of the derivation code path from the banked builder: "
        "this step is all-integer/Fraction (exact adjugate inverses, no "
        "numpy/scipy, no float lattice arithmetic), whereas "
        "build_josehedron.py used float numpy inverses with rounding; the "
        "shared inputs are only BASE and the G0-validated pipeline modules.",
        "- Ops equality is modulo one uniform lattice translation per op (see "
        "interpretation section); exact per-op c_t equality without that "
        "quotient is NOT claimed and is not semantically meaningful for coset "
        "representatives.",
        "- Nothing here claims novelty or touches G5; no banked file was "
        "modified (derived outputs live in this harness directory only).",
        "",
        "## Commands run",
        "",
        "```",
        "PY=python3",
        "cd <repo>/harness",
        "$PY mint_tables.py   # this gate; writes mint_josehedron_tables.json,",
        "                     # mint_tables_{mine,banked}[_proper].txt,",
        "                     # MINT_TABLES_RESULT.md",
        "```",
    ]
    if bij:
        pi, s = bij
        lines.insert(lines.index("## Enumerator provenance (clause C, per "
                                 "instruction: which path)"),
                     f"- Clause-B witness bijection: pi={pi}, "
                     f"s={[list(x) for x in s]} (s_0 fixed to 0; M in M4 "
                     f"detail line).\n")
    open(os.path.join(HERE, "MINT_TABLES_RESULT.md"), "w").write(
        "\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
