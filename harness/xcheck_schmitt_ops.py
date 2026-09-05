#!/usr/bin/env python3
"""
xcheck_schmitt_ops.py — independent historical cross-check of the frozen
spacegroups.json (spglib 2.7.0, G1-audited) against Moritz Schmitt's 2016
`plesiohedron` space-group data (recovered from Software Heritage).

Schmitt data format (reverse-engineered, see SCHMITT_OPS_XCHECK_2026-08-28.md):
  - data/3d/space_group_3d_N.cpp (N=2..230): each isometry is a 4x4 rational
    affine matrix filled entry-by-entry via (*isom)[i][j].set(num, den);
    rows 0..2 cols 0..2 = linear part R (rational, NOT always integer: the
    trigonal/hexagonal families use an orthohexagonal basis with halves),
    column 3 rows 0..2 = translation t, row 3 = (0,0,0,1).
    Column-vector convention: x -> R x + t.  These are coset representatives
    modulo the FULL translation lattice (one per point-group element).
  - spacegrp.cpp, dim_==3 switch (cases 16..230 only): `splitters_` =
    translation vectors (length-4, last entry 0) generating the lattice mod
    Z^3, i.e. the centering vectors of his conventional cell. Groups 2..15
    have NO splitters in the recovered code (constructor throws for them);
    their data files exist but the centering must be assumed (flagged).

Comparison ladder per group (all arithmetic exact, fractions.Fraction):
  L1  point-group-order equality: len(his reps mod his lattice) ==
      ours n_ops / centering multiplicity.
  L2  conjugacy-invariant fingerprint: multiset of (det R, trace R, order R)
      over coset representatives must match (basis-independent).
  L3  exact affine equivalence: find (M, v), x_his = M x_ours + v, with
      M mapping our full translation lattice onto his, such that
      { (M R M^-1, M t + (I - M R M^-1) v) } == his ops modulo his lattice.
      M candidates: identity, the 48 signed permutations, and the
      hexagonal->orthohexagonal family M(a,b) composed with signed perms.
      v solved exactly from the linear system (I - R') v = delta (mod T_his).

Verdicts: EXACT (M=I, v=0, and his splitter set == our centering set;
groups 2..15 need no assumed centering i.e. primitive only),
CONJUGATE-VERIFIED (exact match after some (M, v), or any match that
needed assumed centering), FINGERPRINT-ONLY (L1+L2 pass, no (M,v) found),
MISMATCH (L1 or L2 fail), PARSE-FAIL.

Exit 0 iff no MISMATCH and no PARSE-FAIL; else exit 1 and list them.
Read-only on the recovered repo and on spacegroups.json. Deterministic.
"""

import json
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

BASE = Path("<repo>")
WORKTREE = BASE / "references" / "schmitt_repo_recovery" / "plesiohedron_worktree"
DATA3D = WORKTREE / "data" / "3d"
SPACEGRP = WORKTREE / "spacegrp.cpp"
FROZEN = BASE / "harness" / "spacegroups.json"

F0, F1 = Fraction(0), Fraction(1)
IDENT = ((F1, F0, F0), (F0, F1, F0), (F0, F0, F1))


# ---------------------------------------------------------------- linear algebra
def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def matvec(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inv3(m):
    d = det3(m)
    if d == 0:
        return None
    c = [
        [
            (m[(i + 1) % 3][(j + 1) % 3] * m[(i + 2) % 3][(j + 2) % 3]
             - m[(i + 1) % 3][(j + 2) % 3] * m[(i + 2) % 3][(j + 1) % 3])
            for i in range(3)
        ]
        for j in range(3)
    ]
    return tuple(tuple(c[i][j] / d for j in range(3)) for i in range(3))


def mat_sub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3))


def vec_add(u, v):
    return tuple(u[i] + v[i] for i in range(3))


def vec_sub(u, v):
    return tuple(u[i] - v[i] for i in range(3))


def mod1(v):
    return tuple(x % 1 for x in v)


def rot_order(r):
    p = r
    for k in range(1, 13):
        if p == IDENT:
            return k
        p = matmul(p, r)
    return None


def solve_particular(a, b):
    """One exact solution x of a x = b (3x3 Fractions), free vars = 0; None if
    inconsistent."""
    m = [[a[i][0], a[i][1], a[i][2], b[i]] for i in range(3)]
    piv_cols, r = [], 0
    for c in range(3):
        p = next((i for i in range(r, 3) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        m[r] = [x / m[r][c] for x in m[r]]
        for i in range(3):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [m[i][j] - f * m[r][j] for j in range(4)]
        piv_cols.append(c)
        r += 1
    for i in range(r, 3):
        if m[i][3] != 0:
            return None
    x = [F0, F0, F0]
    for i, c in enumerate(piv_cols):
        x[c] = m[i][3]
    return tuple(x)


# ---------------------------------------------------------------- Schmitt parse
SET_RE = re.compile(r"\(\*isom\)\[(\d)\]\[(\d)\]\.set\((-?\d+),\s*(-?\d+)\);")
VSET_RE = re.compile(r"\(\*vec\)\[(\d)\]\.set\((-?\d+),\s*(-?\d+)\);")


def parse_schmitt_group(n):
    """Return (ops, notes) or raise ValueError. ops = list of (R, t) with R a
    3x3 tuple of Fractions, t a 3-tuple of Fractions reduced mod 1."""
    path = DATA3D / f"space_group_3d_{n}.cpp"
    if not path.exists():
        raise ValueError(f"file missing: {path.name}")
    ops, cur, nset = [], None, 0
    for line in path.read_text().splitlines():
        if "new RationalMatrix" in line:
            if cur is not None:
                raise ValueError(f"group {n}: matrix opened before previous closed")
            cur = [[None] * 4 for _ in range(4)]
            nset = 0
            continue
        mm = SET_RE.search(line)
        if mm:
            if cur is None:
                raise ValueError(f"group {n}: .set outside matrix block")
            i, j, num, den = (int(g) for g in mm.groups())
            if den == 0:
                raise ValueError(f"group {n}: zero denominator")
            if cur[i][j] is not None:
                raise ValueError(f"group {n}: entry [{i}][{j}] set twice")
            cur[i][j] = Fraction(num, den)
            nset += 1
            continue
        if "reps_.push_back" in line:
            if cur is None or nset != 16 or any(x is None for row in cur for x in row):
                raise ValueError(f"group {n}: incomplete matrix ({nset}/16 entries)")
            if tuple(cur[3]) != (F0, F0, F0, F1):
                raise ValueError(f"group {n}: bottom row is not (0,0,0,1)")
            r = tuple(tuple(cur[i][j] for j in range(3)) for i in range(3))
            t = mod1(tuple(cur[i][3] for i in range(3)))
            if det3(r) not in (F1, -F1):
                raise ValueError(f"group {n}: det R = {det3(r)} not +-1")
            if rot_order(r) is None:
                raise ValueError(f"group {n}: R has no finite order <= 12")
            ops.append((r, t))
            cur = None
    if cur is not None:
        raise ValueError(f"group {n}: trailing unclosed matrix")
    if not ops:
        raise ValueError(f"group {n}: no isometries parsed")
    return ops


def parse_splitters():
    """Parse spacegrp.cpp dim_==3 switch -> {n: [3-tuples of Fractions]}."""
    text = SPACEGRP.read_text()
    start = text.index("} else if (dim_ == 3) {")
    end = text.index("} else if (dim_ == 4) {", start)
    section = text[start:end]
    out, cur_case, cur_vec, nset = {}, None, None, 0
    for line in section.splitlines():
        mc = re.search(r"case (\d+):", line)
        if mc:
            cur_case = int(mc.group(1))
            out[cur_case] = []
            continue
        if "new RationalVector" in line and cur_case is not None:
            cur_vec, nset = [None] * 4, 0
            continue
        mv = VSET_RE.search(line)
        if mv and cur_vec is not None:
            i, num, den = (int(g) for g in mv.groups())
            cur_vec[i] = Fraction(num, den)
            nset += 1
            continue
        if "splitters_.push_back" in line and cur_case is not None:
            if cur_vec is None or nset != 4 or cur_vec[3] != 0:
                raise ValueError(f"splitters case {cur_case}: malformed vector")
            out[cur_case].append(mod1(tuple(cur_vec[:3])))
            cur_vec = None
    return out


# ---------------------------------------------------------------- frozen parse
def load_frozen():
    d = json.loads(FROZEN.read_text())
    assert d["n_groups"] == 230
    groups = {}
    for e in d["groups"]:
        ops = [
            (
                tuple(tuple(Fraction(x) for x in row) for row in op["R"]),
                tuple(Fraction(s) for s in op["t"]),
            )
            for op in e["ops"]
        ]
        cent = [tuple(Fraction(s) for s in v) for v in e["centering"]["vectors"]]
        groups[e["number"]] = {
            "ops": ops,
            "cent": cent,
            "mult": e["centering"]["multiplicity"],
            "n_ops": e["n_ops"],
            "symbol": e["international_short"],
        }
    return groups, d.get("spglib_version"), d.get("setting_convention")


# ---------------------------------------------------------------- group algebra
def canon_t(t, splitters):
    """Canonical coset representative of t modulo (Z^3 + splitters)."""
    return min(mod1(vec_add(t, s)) for s in splitters)


def coset_set(ops, splitters):
    return frozenset((r, canon_t(t, splitters)) for r, t in ops)


def fingerprint(cosets):
    return tuple(sorted((det3(r), sum(r[i][i] for i in range(3)), rot_order(r))
                        for r, _ in cosets))


def closure_ok(cosets, splitters):
    s = set(cosets)
    for r1, t1 in cosets:
        for r2, t2 in cosets:
            r = matmul(r1, r2)
            t = canon_t(vec_add(matvec(r1, t2), t1), splitters)
            if (r, t) not in s:
                return False
    return ((IDENT, canon_t((F0, F0, F0), splitters)) in s)


# ---------------------------------------------------------------- basis library
def signed_perms():
    out = []
    for perm in permutations(range(3)):
        for signs in product((F1, -F1), repeat=3):
            m = [[F0] * 3 for _ in range(3)]
            for i in range(3):
                m[i][perm[i]] = signs[i]
            out.append(tuple(tuple(row) for row in m))
    return out


SIGNED_PERMS = signed_perms()
H = Fraction(1, 2)


def hex_family():
    """M(a,b) = [[a,b,0],[a+2b,-2a-b,0],[0,0,1]]: maps hexagonal axes onto
    Schmitt's orthohexagonal basis (derived from his 3-fold matrices)."""
    out = []
    for a, b in [(H, F0), (F0, H), (-H, F0), (F0, -H),
                 (H, -H), (-H, H), (H, H), (-H, -H)]:
        m = ((a, b, F0), (a + 2 * b, -2 * a - b, F0), (F0, F0, F1))
        if det3(m) != 0:
            out.append(m)
    return out


HEX_FAMILY = hex_family()


def candidate_bases():
    cands = [IDENT]
    cands += [m for m in SIGNED_PERMS if m != IDENT]
    for h in HEX_FAMILY:
        for s in SIGNED_PERMS:
            cands.append(matmul(h, s))
    seen, out = set(), []
    for m in cands:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out


CANDIDATE_BASES = candidate_bases()


# ---------------------------------------------------------------- L3 search
def lattice_compatible(m, our_cent, his_splitters, his_mult, our_mult):
    """Does M map (Z^3 + our_cent) onto (Z^3 + his_splitters)?"""
    if abs(det3(m)) != Fraction(our_mult, his_mult):
        return False
    his_set = frozenset(mod1(s) for s in his_splitters)
    gens = [tuple(m[i][j] for i in range(3)) for j in range(3)]  # M e_j
    gens += [matvec(m, s) for s in our_cent]
    return all(mod1(g) in his_set for g in gens)


def try_basis(m, our_cosets, our_cent, his_cosets, his_splitters,
              his_mult, our_mult, check_lattice=True):
    """Try to find v so that x -> Mx + v maps our group onto his. Returns v or
    None."""
    if check_lattice and not lattice_compatible(m, our_cent, his_splitters,
                                               his_mult, our_mult):
        return None
    minv = inv3(m)
    transformed = [(matmul(matmul(m, r), minv), matvec(m, t))
                   for r, t in our_cosets]
    if sorted(r for r, _ in transformed) != sorted(r for r, _ in his_cosets):
        return None
    his_set = his_cosets

    def verify(v):
        got = frozenset(
            (rp, canon_t(vec_add(tp, matvec(mat_sub(IDENT, rp), v)), his_splitters))
            for rp, tp in transformed
        )
        return got == his_set

    if verify((F0, F0, F0)):
        return (F0, F0, F0)
    # pick R' maximizing |det(I - R')| to pin down v
    best = max(transformed, key=lambda o: abs(det3(mat_sub(IDENT, o[0]))))
    rstar = best[0]
    a = mat_sub(IDENT, rstar)
    his_with_rstar = [t for r, t in his_cosets if r == rstar]
    ours_with_rstar = [t for r, t in transformed if r == rstar]
    lam_range = range(0, 6) if det3(a) != 0 else range(-1, 2)
    tried = set()
    for tau in his_with_rstar:
        for tp in ours_with_rstar:
            delta0 = vec_sub(tau, tp)
            for s in his_splitters:
                for z in product(lam_range, repeat=3):
                    delta = vec_add(vec_add(delta0, s),
                                    tuple(Fraction(k) for k in z))
                    v = solve_particular(a, delta)
                    if v is None:
                        continue
                    vk = mod1(v)
                    if vk in tried:
                        continue
                    tried.add(vk)
                    if verify(v):
                        return v
    return None


# ---------------------------------------------------------------- main
def main():
    frozen, spglib_ver, convention = load_frozen()
    splitters_all = parse_splitters()
    results = {}
    for n in range(2, 231):
        sym = frozen[n]["symbol"]
        try:
            his_ops = parse_schmitt_group(n)
        except ValueError as e:
            results[n] = {"level": "PARSE-FAIL", "symbol": sym, "detail": str(e)}
            continue
        his_splitters = splitters_all.get(n)
        assumed = his_splitters is None or len(his_splitters) == 0
        notes = []

        ours = frozen[n]
        our_cosets = sorted(coset_set(ours["ops"], ours["cent"]))
        pg_order = len(our_cosets)
        if ours["n_ops"] != pg_order * ours["mult"]:
            notes.append("frozen n_ops != pg_order*mult (unexpected)")

        # translation rationality (his): always exact by construction; verify
        # denominators are sane
        max_den = max((x.denominator for _, t in his_ops for x in t), default=1)

        detail = {
            "symbol": sym,
            "n_reps": len(his_ops),
            "n_splitters": None if assumed else len(his_splitters),
            "assumed_centering": assumed,
            "max_t_denominator": max_den,
            "nonint_R": any(x.denominator != 1 for r, _ in his_ops
                            for row in r for x in row),
        }

        level = None
        found_m = found_v = None
        # ---- L1
        l1 = len(his_ops) == pg_order
        detail["L1_op_count"] = l1
        if not l1:
            detail["L1_detail"] = (f"his reps={len(his_ops)}, "
                                   f"our pg order={pg_order}")
        # try candidate bases; for assumed centering the his-lattice is taken
        # as M(our lattice) (borrowed -- capped below)
        l2 = False
        if l1:
            for m in CANDIDATE_BASES:
                if assumed:
                    minv_check = det3(m)
                    if abs(minv_check) != 1:
                        continue  # borrowed lattice: only unimodular M sensible
                    hs = sorted({mod1(matvec(m, s)) for s in ours["cent"]})
                    his_mult = len(hs)
                else:
                    hs = his_splitters
                    his_mult = len({mod1(s) for s in hs})
                his_cosets = coset_set(his_ops, hs)
                if len(his_cosets) != len(his_ops):
                    continue  # reps collide mod this lattice; wrong lattice
                if m == CANDIDATE_BASES[0]:
                    # compute fingerprints once, with the first viable lattice
                    l2 = fingerprint(his_cosets) == fingerprint(our_cosets)
                    detail["L2_fingerprint"] = l2
                    detail["closure_his"] = closure_ok(his_cosets, hs)
                v = try_basis(m, our_cosets, ours["cent"], his_cosets, hs,
                              his_mult, ours["mult"],
                              check_lattice=not assumed)
                if v is not None:
                    found_m, found_v = m, v
                    if not assumed:
                        splitter_match = ({mod1(s) for s in hs}
                                          == {mod1(s) for s in ours["cent"]})
                    else:
                        splitter_match = False
                    if (m == IDENT and mod1(v) == (F0, F0, F0)
                            and (splitter_match or (assumed and ours["mult"] == 1))):
                        level = "EXACT"
                    else:
                        level = "CONJUGATE-VERIFIED"
                    break
        if level is None:
            if "L2_fingerprint" not in detail:
                # no viable lattice in loop (or L1 failed): fingerprint with
                # his own splitters if known, else trivial lattice
                hs = his_splitters if not assumed else [(F0, F0, F0)]
                his_cosets = coset_set(his_ops, hs)
                l2 = fingerprint(his_cosets) == fingerprint(our_cosets)
                detail["L2_fingerprint"] = l2
                detail["closure_his"] = closure_ok(his_cosets, hs)
            else:
                l2 = detail["L2_fingerprint"]
            level = "FINGERPRINT-ONLY" if (l1 and l2) else "MISMATCH"
        if found_m is not None:
            detail["M"] = [[str(x) for x in row] for row in found_m]
            detail["v"] = [str(x) for x in mod1(found_v)]
        detail["level"] = level
        if assumed and level in ("EXACT", "CONJUGATE-VERIFIED") and ours["mult"] > 1:
            detail["note"] = ("centering vectors undefined in recovered code "
                              "(constructor throws for N<16); our centering "
                              "assumed -- reps-only evidence")
            if level == "EXACT":
                detail["level"] = level = "CONJUGATE-VERIFIED"
        results[n] = detail

    # ------------------------------------------------------------ report
    counts = {}
    for n, d in sorted(results.items()):
        counts[d["level"]] = counts.get(d["level"], 0) + 1
    print(f"# Schmitt 2016 data/3d vs frozen spacegroups.json "
          f"(spglib {spglib_ver})")
    print(f"# groups checked: {len(results)} (N=2..230)")
    for lvl in ("EXACT", "CONJUGATE-VERIFIED", "FINGERPRINT-ONLY",
                "MISMATCH", "PARSE-FAIL"):
        print(f"{lvl:20s} {counts.get(lvl, 0)}")
    ok = [d for d in results.values() if d["level"] != "PARSE-FAIL"]
    print()
    print(f"L1 op-count pass: {sum(1 for d in ok if d.get('L1_op_count'))}"
          f"/{len(ok)}")
    print(f"L2 fingerprint pass: "
          f"{sum(1 for d in ok if d.get('L2_fingerprint'))}/{len(ok)}")
    print(f"his-group closure verified: "
          f"{sum(1 for d in ok if d.get('closure_his'))}/{len(ok)}")
    print(f"all translations exact rationals: yes (parser rejects non-integer "
          f".set args); max denominator over all groups = "
          f"{max(d.get('max_t_denominator', 1) for d in ok)}")
    idm = [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]
    conj = {n: d for n, d in sorted(results.items())
            if d["level"] == "CONJUGATE-VERIFIED"}
    sub_assumed = [n for n, d in conj.items() if d.get("assumed_centering")]
    sub_origin = [n for n, d in conj.items()
                  if not d.get("assumed_centering") and d.get("M") == idm]
    sub_basis = [n for n, d in conj.items()
                 if not d.get("assumed_centering") and d.get("M") != idm]
    print()
    print(f"CONJUGATE-VERIFIED breakdown:")
    print(f"  borrowed centering, M=I v=0 (N<16, splitters absent from "
          f"recovered code): {sub_assumed}")
    print(f"  pure origin shift (M=I, v!=0): {sub_origin}")
    print(f"  basis change (hexagonal family -> orthohexagonal): {sub_basis}")
    two_origin_it = [48, 50, 59, 68, 70, 85, 86, 88, 125, 126, 129, 130, 133,
                     134, 137, 138, 141, 142, 201, 203, 222, 224, 227, 228]
    print(f"  origin-shift set == the 24 IT two-origin groups: "
          f"{sub_origin == two_origin_it}")
    print(f"  basis-change set == trigonal/hexagonal 143..194: "
          f"{sub_basis == list(range(143, 195))}")
    # Enantiomorph guard: for the 22 groups in the 11 enantiomorphic pairs,
    # the matching M must be PROPER (det > 0), otherwise we would only have
    # matched the mirror-image type.
    enant = [76, 78, 91, 95, 92, 96, 144, 145, 151, 153, 152, 154,
             169, 170, 171, 172, 178, 179, 180, 181, 212, 213]
    bad_hand = []
    for n in enant:
        d = results[n]
        if d["level"] in ("EXACT", "CONJUGATE-VERIFIED"):
            m = (IDENT if "M" not in d else
                 tuple(tuple(Fraction(x) for x in row) for row in d["M"]))
            if det3(m) <= 0:
                bad_hand.append(n)
        else:
            bad_hand.append(n)
    print(f"  enantiomorph guard (all 22 chiral-pair groups matched with "
          f"proper M, det>0): {'PASS' if not bad_hand else f'FAIL {bad_hand}'}")
    print()
    bad = []
    for n, d in sorted(results.items()):
        lvl = d["level"]
        flag = ""
        if d.get("assumed_centering") and lvl != "PARSE-FAIL":
            flag = " [assumed-centering]"
        if lvl in ("MISMATCH", "PARSE-FAIL", "FINGERPRINT-ONLY"):
            bad.append((n, d))
        mtxt = ""
        if "M" in d:
            mid = d["M"] == [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]
            v0 = d.get("v") == ["0", "0", "0"]
            if not mid or not v0:
                mtxt = f"  M={'I' if mid else d['M']} v={d.get('v')}"
        print(f"{n:3d} {d.get('symbol', ''):12s} {lvl}{flag}{mtxt}")
    print()
    if bad:
        print("EXCEPTIONS:")
        for n, d in bad:
            print(f"  {n} {d.get('symbol','')}: {d['level']} :: "
                  f"{d.get('detail', d)}")
    else:
        print("EXCEPTIONS: none")
    sys.exit(1 if any(d["level"] in ("MISMATCH", "PARSE-FAIL")
                      for d in results.values()) else 0)


if __name__ == "__main__":
    main()
