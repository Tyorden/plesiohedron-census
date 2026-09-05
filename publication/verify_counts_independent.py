#!/usr/bin/env python3
"""verify_counts_independent.py — second, independently written polyform
enumerator for the MINT honeycomb tables (dual-implementation bar).

Written 2026-09-03 from the table SEMANTICS only (schema in the g4_tables_*.json
files: T translation types; nbr[t] = list of [lattice delta, type'];
ops / proper_ops = coset representatives acting on cell IDs as
(v, t) -> (A . v + c_t, t') with map[t] = [c_t, t'], A a 3x3 unimodular
integer matrix acting on column vectors).  Shares NO code with the banked
export_tables.py / compiled `enumerate` binary, nor with harness/mint_tables.py,
nor with the Josehedron reference_enum.py (which grows FREE forms directly under
a full-ops canonical form).  This program uses a different route:

  1. FIXED forms: translation-canonical connected n-cell sets grown level by
     level (n -> n+1) from every cell of every parent, deduplicated as packed
     integers.  Canonical form = translate the lexicographically least cell
     (x, y, z, t) to the origin, sort.  No symmetry op is ever consulted here,
     so the fixed column is a symmetry-free check of the nbr table semantics.
  2. FREE / ONE-SIDED forms: quotient of the fixed set by the honeycomb ops
     (all ops -> free; proper_ops -> one-sided).  A fixed form is counted iff
     it is the lexicographic minimum of its own orbit (orbit-representative
     count).  As an internal cross-check the Burnside identity
         |G| * orbits == sum_g |Fix(g)|
     is evaluated from the same images and asserted for both groups.

Stdlib only (pure Python + multiprocessing).  Deterministic: the results are
set cardinalities; chunking order cannot change them.

Usage:
  verify_counts_independent.py TABLES.json [--n N] [--workers W] [--json OUT]
      [--expect-fixed a,b,c,...] [--expect-free ...] [--expect-onesided ...]
Exit status 0 iff every requested check (table sanity, Burnside, expectations)
passed.
"""
import argparse
import json
import multiprocessing as mp
import os
import sys
import time

# ---------------------------------------------------------------- encoding ---
# One cell (x, y, z, t) is packed into one int:
#   ((x+B) << SX) | ((y+B) << SY) | ((z+B) << SZ) | t
# with each coordinate field CB bits wide and the type field TB bits wide.
# Integer order of packed keys == lexicographic order of (x, y, z, t), which is
# what makes "min(keys)" the lexicographically least cell.
CB = 6            # coordinate bits: fields hold x+B in [0, 64)
B = 1 << (CB - 1)  # 32: coordinates representable in [-32, 31]
TB = 6            # type bits: T <= 63
SZ = TB
SY = TB + CB
SX = TB + 2 * CB
CELLBITS = TB + 3 * CB     # 24
TMASK = (1 << TB) - 1
CMASK = (1 << CB) - 1
ORIGIN = (B << SX) | (B << SY) | (B << SZ)   # coordinate part of ((0,0,0), *)


def enc(x, y, z, t):
    return ((x + B) << SX) | ((y + B) << SY) | ((z + B) << SZ) | t


def dec(k):
    return ((k >> SX) - B, ((k >> SY) & CMASK) - B, ((k >> SZ) & CMASK) - B,
            k & TMASK)


def pack_form(keys):
    """keys: iterable of packed cell ints (already canonical + sorted)."""
    out = 0
    for i, k in enumerate(keys):
        out |= k << (CELLBITS * i)
    return out


def unpack_form(p, n):
    m = (1 << CELLBITS) - 1
    return tuple((p >> (CELLBITS * i)) & m for i in range(n))


# ------------------------------------------------------------------ tables ---
G = {}   # globals shared with forked workers


def load_tables(path):
    d = json.load(open(path))
    T = int(d['T'])
    nbr = [[((int(dv[0]), int(dv[1]), int(dv[2])), int(tj)) for dv, tj in row]
           for row in d['nbr']]

    def parse_ops(lst):
        res = []
        for op in lst:
            A = tuple(tuple(int(x) for x in row) for row in op['A'])
            mp_ = [((int(c[0]), int(c[1]), int(c[2])), int(tj))
                   for c, tj in op['map']]
            res.append((A, mp_))
        return res
    ops = parse_ops(d['ops'])
    props = parse_ops(d['proper_ops'])
    return T, nbr, ops, props


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def apply_op(op, cell):
    """(A, map) applied to an unpacked cell (x, y, z, t)."""
    A, mp_ = op
    x, y, z, t = cell
    c, tj = mp_[t]
    return (A[0][0] * x + A[0][1] * y + A[0][2] * z + c[0],
            A[1][0] * x + A[1][1] * y + A[1][2] * z + c[1],
            A[2][0] * x + A[2][1] * y + A[2][2] * z + c[2], tj)


def sanity(T, nbr, ops, props, n_max):
    """Table sanity checks that do not touch any enumeration."""
    problems = []
    if T > TMASK:
        problems.append(f"T={T} exceeds type field ({TMASK})")
    if any(len(row) == 0 for row in nbr) or len(nbr) != T:
        problems.append("nbr table shape wrong")
    maxd = max(abs(v) for row in nbr for dv, _ in row for v in dv)
    if (n_max - 1) * maxd >= B - 1:
        problems.append(f"coordinate field too narrow for n={n_max}, maxd={maxd}")
    # every type appears in the table range
    for t, row in enumerate(nbr):
        for dv, tj in row:
            if not (0 <= tj < T):
                problems.append(f"nbr[{t}] references type {tj}")
    # adjacency is symmetric: (0,t)~(d,t')  <=>  (0,t')~(-d,t)
    nbrset = set()
    for t, row in enumerate(nbr):
        for dv, tj in row:
            nbrset.add((t, dv, tj))
    for t, dv, tj in nbrset:
        if (tj, (-dv[0], -dv[1], -dv[2]), t) not in nbrset:
            problems.append(f"adjacency not symmetric at ({t},{dv},{tj})")
            break
    # ops: unimodular, maps well-formed, proper subset of ops with det +1,
    # and each op is an automorphism of the adjacency structure.
    opkeys = set()
    for A, mp_ in ops:
        if abs(det3(A)) != 1:
            problems.append(f"op det {det3(A)} not unimodular")
        if len(mp_) != T:
            problems.append("op map length != T")
        opkeys.add((A, tuple(mp_)))
    if len(opkeys) != len(ops):
        problems.append("duplicate ops")
    for A, mp_ in props:
        if det3(A) != 1:
            problems.append("proper op with det != +1")
        if (A, tuple(mp_)) not in opkeys:
            problems.append("proper op not in ops")
    n_auto_bad = 0
    for op in ops:
        for t in range(T):
            img0 = apply_op(op, (0, 0, 0, t))
            x0, y0, z0, t0 = img0
            expect = set()
            for dv, tj in nbr[t0]:
                expect.add((x0 + dv[0], y0 + dv[1], z0 + dv[2], tj))
            got = set()
            for dv, tj in nbr[t]:
                got.add(apply_op(op, (dv[0], dv[1], dv[2], tj)))
            if got != expect:
                n_auto_bad += 1
    if n_auto_bad:
        problems.append(f"{n_auto_bad} (op,type) pairs are NOT adjacency "
                        f"automorphisms")
    return problems, maxd


# --------------------------------------------------------- fixed growth -----
def _grow_chunk(parents_packed_and_n):
    """Worker: extend each packed parent (n-1 cells) by one neighbour cell,
    return the set of packed translation-canonical children."""
    parents, n1 = parents_packed_and_n
    OFF = G['OFF']
    out = set()
    m = (1 << CELLBITS) - 1
    for p in parents:
        cells = [(p >> (CELLBITS * i)) & m for i in range(n1)]
        cset = set(cells)
        for k in cells:
            for off in OFF[k & TMASK]:
                nb = k + off
                if nb in cset:
                    continue
                child = cells + [nb]
                mn = min(child)
                shift = (mn & ~TMASK) - ORIGIN
                child = sorted(c - shift for c in child)
                out.add(pack_form(child))
    return out


def grow_level(level, n1, pool, workers):
    """level: list of packed (n1)-cell forms -> set of packed (n1+1)-cell forms."""
    if not level:
        return set()
    nchunks = max(1, min(len(level) // 20000 + 1, workers * 4))
    step = (len(level) + nchunks - 1) // nchunks
    chunks = [(level[i:i + step], n1) for i in range(0, len(level), step)]
    result = set()
    for s in pool.imap_unordered(_grow_chunk, chunks):
        result |= s
    return result


# ------------------------------------------------------- orbit quotient -----
def _orbit_chunk(args):
    """Worker: for each packed n-cell form compute all op images (translation-
    canonical, packed).  Returns (reps_all, reps_proper, fix_all, fix_proper)
    where reps_* counts forms that are the minimum of their orbit and fix_* is a
    per-op list of the number of forms fixed by that op."""
    forms, n = args
    ops = G['ops']
    proper_idx = G['proper_idx']
    nops = len(ops)
    fix = [0] * nops
    reps_all = 0
    reps_prop = 0
    m = (1 << CELLBITS) - 1
    pset = set(proper_idx)
    for p in forms:
        cells = [dec((p >> (CELLBITS * i)) & m) for i in range(n)]
        is_min_all = True
        is_min_prop = True
        for gi, (A, mp_) in enumerate(ops):
            img = []
            for (x, y, z, t) in cells:
                c, tj = mp_[t]
                img.append((A[0][0] * x + A[0][1] * y + A[0][2] * z + c[0],
                            A[1][0] * x + A[1][1] * y + A[1][2] * z + c[1],
                            A[2][0] * x + A[2][1] * y + A[2][2] * z + c[2],
                            tj))
            mx, my, mz, _ = min(img)
            keys = sorted(enc(x - mx, y - my, z - mz, t) for x, y, z, t in img)
            q = pack_form(keys)
            if q == p:
                fix[gi] += 1
            elif q < p:
                is_min_all = False
                if gi in pset:
                    is_min_prop = False
        if is_min_all:
            reps_all += 1
        if is_min_prop:
            reps_prop += 1
    return reps_all, reps_prop, fix


def quotient(level, n, pool, workers):
    if not level:
        return 0, 0, [0] * len(G['ops'])
    nchunks = max(1, min(len(level) // 5000 + 1, workers * 6))
    step = (len(level) + nchunks - 1) // nchunks
    chunks = [(level[i:i + step], n) for i in range(0, len(level), step)]
    ra = rp = 0
    fix = [0] * len(G['ops'])
    for a, b, f in pool.imap_unordered(_orbit_chunk, chunks):
        ra += a
        rp += b
        for i, v in enumerate(f):
            fix[i] += v
    return ra, rp, fix


# -------------------------------------------------------------------- main ---
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tables')
    ap.add_argument('--n', type=int, default=6)
    ap.add_argument('--workers', type=int, default=max(1, os.cpu_count() - 2))
    ap.add_argument('--json', default=None)
    ap.add_argument('--expect-fixed', default=None)
    ap.add_argument('--expect-free', default=None)
    ap.add_argument('--expect-onesided', default=None)
    ap.add_argument('--wall-cap', type=float, default=None,
                    help='seconds; stop before starting a level if exceeded')
    a = ap.parse_args()

    T, nbr, ops, props = load_tables(a.tables)
    problems, maxd = sanity(T, nbr, ops, props, a.n)
    print(f"tables: {a.tables}")
    print(f"T={T} neighbours/type={sorted(set(len(r) for r in nbr))} "
          f"max|delta|={maxd} |ops|={len(ops)} |proper|={len(props)}")
    ok = True
    if problems:
        ok = False
        for p in problems:
            print("TABLE PROBLEM:", p)

    # neighbour offsets in packed space (delta and type change fold into one add)
    OFF = []
    for t in range(T):
        row = []
        for (dx, dy, dz), tj in nbr[t]:
            row.append((dx << SX) + (dy << SY) + (dz << SZ) + (tj - t))
        OFF.append(row)
    G['OFF'] = OFF
    G['ops'] = ops
    opindex = {(A, tuple(mp_)): i for i, (A, mp_) in enumerate(ops)}
    G['proper_idx'] = [opindex[(A, tuple(mp_))] for A, mp_ in props]

    expects = {}
    for name in ('fixed', 'free', 'onesided'):
        v = getattr(a, 'expect_' + name)
        if v:
            expects[name] = [int(x) for x in v.split(',')]

    ctx = mp.get_context('fork')
    t_start = time.time()
    rows = []
    with ctx.Pool(a.workers) as pool:
        level = [pack_form([enc(0, 0, 0, t)]) for t in range(T)]
        for n in range(1, a.n + 1):
            if n > 1:
                if a.wall_cap and (time.time() - t_start) > a.wall_cap:
                    print(f"wall cap reached before n={n}; stopping")
                    break
                t0 = time.time()
                level = sorted(grow_level(level, n - 1, pool, a.workers))
                t_grow = time.time() - t0
            else:
                t_grow = 0.0
            fixed = len(level)
            t0 = time.time()
            free, onesided, fix = quotient(level, n, pool, a.workers)
            t_q = time.time() - t0
            # Burnside identities (internal cross-check of the orbit counts)
            burn_all = sum(fix)
            burn_prop = sum(fix[i] for i in G['proper_idx'])
            b_ok_all = (burn_all == len(ops) * free)
            b_ok_prop = (burn_prop == len(props) * onesided)
            row = {'n': n, 'fixed': fixed, 'free': free, 'onesided': onesided,
                   'burnside_all_ok': b_ok_all, 'burnside_proper_ok': b_ok_prop,
                   'sum_fix_all': burn_all, 'sum_fix_proper': burn_prop,
                   't_grow_s': round(t_grow, 2), 't_quotient_s': round(t_q, 2)}
            flags = []
            for name, val in (('fixed', fixed), ('free', free),
                              ('onesided', onesided)):
                if name in expects and len(expects[name]) >= n:
                    exp = expects[name][n - 1]
                    m = 'MATCH' if exp == val else 'MISMATCH'
                    row['expect_' + name] = exp
                    row['match_' + name] = m
                    flags.append(f"{name}:{m}")
                    if m != 'MATCH':
                        ok = False
            if not (b_ok_all and b_ok_prop):
                ok = False
                flags.append("BURNSIDE-FAIL")
            rows.append(row)
            print(f"n={n} fixed={fixed} free={free} onesided={onesided} "
                  f"burnside(all={'ok' if b_ok_all else 'FAIL'},"
                  f"proper={'ok' if b_ok_prop else 'FAIL'}) "
                  f"grow={t_grow:.1f}s quot={t_q:.1f}s "
                  f"{' '.join(flags)}", flush=True)
    total = time.time() - t_start
    print(f"total wall {total:.1f}s  workers={a.workers}  "
          f"{'ALL CHECKS PASSED' if ok else 'CHECKS FAILED'}")
    if a.json:
        json.dump({'tables': os.path.abspath(a.tables), 'T': T,
                   'n_ops': len(ops), 'n_proper': len(props),
                   'table_problems': problems, 'rows': rows,
                   'wall_s': round(total, 1), 'workers': a.workers,
                   'ok': ok, 'python': sys.version.split()[0]},
                  open(a.json, 'w'), indent=1)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
