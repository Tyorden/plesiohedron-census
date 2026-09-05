#!/usr/bin/env python
"""g4_certify.py — G4 finalist certificate ladder (ANCHORS G4, verbatim gate):
V0 exact re-derivation, V1 tiling certificate + INDEPENDENT adapted audit,
V2 symmetry certification (stabilizer over ALL orthogonal maps; Bravais point
group of the ACTUAL lattice, not signed-perms-by-assumption), V3 Burnside
identity on the candidate's polyform counts. Parameterized by stored type id
(phase1_types.json); default = the FULL 11-candidate 2026-08-30 G4 queue,
batch 1 (the 3 priority candidates, accepted earlier today) first, then
batch 2 (the 2 remaining collision-screen survivors + the 6 remaining
ABSENT-all triage types).  The results doc is regenerated whole each run,
batch 2 marked, so a no-args re-run remains the acceptance criterion.

Ladder spec: ../HARNESS_DESIGN_FABLE5_2026-08-27.md §3 (V0–V3), modeled on the
JIS/paper-I patterns it cites (g1_verify, audit_t1_independent C1–C6,
burnside_generic).  House invariant: floats PROPOSE (scipy sweep, atan2 facet
ordering), Fractions DECIDE — every certified claim below is exact arithmetic.

STAGES (per candidate)
  V0  From the stored witnessing (group, point): orbit (frozen G1
      spacegroups.json) -> float sweep W=2 (W=3 retry) -> exact clip
      (4*rho^2 <= D^2 cutoff asserted) -> canonical code.  Assert code,
      f-vector, p-vector, aut, and all witness metadata match the store.
      Kill criterion LIVE: facet count > 38 aborts (assume bug).
  V1  Tiling certificate for the complex {rep-cell_t + L : t < T}:
      (a) exact primitive lattice L (mint_tables.derive_lattice pattern),
          T = n*detL/P^3 == stored orbit_primitive; exact cells for ALL T
          type representatives; identical (F, p-vector, canonical code)
          across reps (combinatorial congruence);
      (b) volume identity: per-rep volume from facet geometry (exact fan
          decomposition), all equal, T * vol == detL == P^3/n * T;
      (c) full-facet pairing: every one of the T*F facet slots is shared,
          vertex-set-exactly, with EXACTLY ONE neighbor cell facet whose
          reciprocal neighbor is the central site;
      (d) translate-completeness + interior disjointness: every site r with
          0 < |r-c_t|^2 <= 4*rho^2 (exhaustive block enumeration; sites
          beyond cannot meet the cell: any shared point x has
          |x-c|<=rho, |x-r|<=rho => |r-c|<=2rho) satisfies: all cell
          vertices weakly on c_t's side of bisector(c_t, r), and if the
          on-bisector vertex set spans 2 dimensions then r IS a listed
          facet neighbor.  Hence all distinct cells of the complex have
          disjoint interiors; with (b), coverage follows by the measure
          argument on R^3/L (orden_rev1 §3 pattern): disjoint interiors +
          volumes summing to the torus volume => tiling.
      Then the INDEPENDENT ADAPTED AUDIT (v1_audit_* functions below):
      a second implementation of facet extraction (supporting-plane triple
      scan), volume, and the pairing check, sharing NO geometry code with
      exact_cell/mint_tables (fresh vector/det/facet/volume functions; only
      canon_code import is permitted by the tasking and is not needed).
      The audit consumes the certificate as DATA (vertex coordinate strings,
      lattice basis, pairing claims) and re-verifies every claim.
  V2  Symmetry certification: cell stabilizer over ALL orthogonal maps
      (Gram-triple matching about the vertex centroid — audit_t1 C6 pattern,
      NO signed-perm assumption); site symmetry from orbit.site_stabilizer;
      combinatorial aut order from the canonical code.  Assert the subgroup
      chain site <= stab_geo (containment of linear parts) and the
      divisibility site | stab_geo | aut; report all three.  Bravais point
      group of the ACTUAL lattice: all U in GL3(Z) with U^T G_L U == G_L,
      enumerated with a PROVEN coefficient bound (u_j^2 <= (G^-1)_jj * |w|^2
      by Cauchy-Schwarz against the dual basis) — reported, and whether its
      ambient embedding happens to be the signed permutations (checked, not
      assumed).
  V3  Burnside identity: honeycomb tables derived (generalized mint_tables:
      nbr table via id_of_site; ops = ALL (R, c) with R in the Bravais group
      embedding and R*S + c == S exactly, one op per R mod lattice, identity
      + closure asserted in ID space) -> banked export_tables.py -> banked
      compiled enumerate binary, n <= 4 -> fixed/free counts -> banked
      burnside_generic.py (independent growth enumeration): assert
      |ops| * free(n) == sum_m Fix_m(n) for n <= 4, and its own fixed-count
      recount equals the enumerator's.  enumerate.cpp limits asserted
      (T <= 127, uniform neighbor count).  Soft budget: if a candidate's
      elapsed time exceeds BUDGET_S before the enumeration step, V3 is
      recorded TIMEOUT-DEFERRED with what completed.

LANGUAGE (stated once, applies throughout): G4 passing does NOT establish
novelty — these types remain "not matched against the catalog snapshot of
2026-08-28"; novelty diligence is G5, which has not run on these types.

Run:
  python3 g4_certify.py \
      [type_id ...]
Writes: g4_tables_<id>.json (+ enumerator .txt), G4_RESULTS.md.
Exit 0 iff every stage of every requested candidate is PASS (DEFERRED also
exits nonzero=0? No: DEFERRED exits 0 only if explicitly a budget deferral,
recorded as such — a FAIL always exits 1).
"""
import itertools
import json
import math
import os
import subprocess
import sys
import time
import traceback
from fractions import Fraction as F

import orbit
from sweep_voronoi import sweep
from exact_cell import clip_cell, candidates_near
from canon_code import canonical_code
from sweep_phase1 import wyckoff_dim
from mint_tables import (det3, mat_det, mat_inv, mat_vec, mat_mul,
                         to_int_vec, to_int_mat, derive_lattice)

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "phase1_types.json")
BANKED_SCRIPTS = os.path.join(HERE, "..", "..", "SCI_OEIS_josehedron", "scripts")
EXPORT_TABLES = os.path.join(BANKED_SCRIPTS, "export_tables.py")
ENUM_BIN = os.path.join(BANKED_SCRIPTS, "enumerate")
BURNSIDE = os.path.join(HERE, "..", "..", "POLYFORMS_II_sphenoid_josehedron",
                        "burnside_generic.py")
PYTHON = "python3"

BATCH1_IDS = ["ceb70631e274e727", "359beee832567a71", "8cf50403cf88c455"]
BATCH2_IDS = ["c314dedd38208a2e", "aa6b0077c3234d24",   # collision survivors
              "f3d0f39a0b9676b9", "2de0a21129cabe90",   # ABSENT-all (triage)
              "c4ea3f32fdd6dc51", "9b69eefb8bd8437c",
              "d2d935e5499e6e11", "f98a3ee5675fc121"]
DEFAULT_IDS = BATCH1_IDS + BATCH2_IDS
MAX_FACETS = 38                # ANCHORS kill criterion, live
N_ENUM = 4                     # V3 depth (high-F cells fan out fast)
BUDGET_S = 40 * 60             # per-candidate soft budget before V3 enum


# --------------------------------------------------- shared exact vector bits
def vsub(a, b): return tuple(a[k] - b[k] for k in range(3))
def vdot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def vcross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
                          a[0]*b[1]-a[1]*b[0])


def ball_D(rho2):
    """Smallest integer D with D^2 >= 4*rho2 (exact)."""
    x = 4 * F(rho2)
    D = math.isqrt(x.numerator // x.denominator)
    while D * D < x:
        D += 1
    return D


def isqrt_frac_floor(x):
    """Largest integer m with m^2 <= x (x a nonneg Fraction)."""
    m = math.isqrt(x.numerator // x.denominator)
    while (m + 1) * (m + 1) <= x:
        m += 1
    return m


def cell_volume_from_cycles(ec):
    """Exact cell volume from the oriented facet cycles (fan from cycle vertex
    0 to the site, all tetra dets positive since cycles are CCW-from-outside
    and the site is interior)."""
    vs = ec["vertices"]
    c = tuple(F(x) for x in ec["center"])
    six_vol = F(0)
    for cyc in ec["facet_cycles"]:
        p0 = vsub(vs[cyc[0]], c)
        for t in range(1, len(cyc) - 1):
            d = det3(p0, vsub(vs[cyc[t]], c), vsub(vs[cyc[t+1]], c))
            assert d > 0, "non-positive fan tetra: orientation broken"
            six_vol += d
    return six_vol / 6


def pvec_compact(pv):
    from collections import Counter
    return " ".join(f"{k}^{m}" for k, m in sorted(Counter(pv).items()))


def is_signed_perm(A):
    rows_ok = all(sorted(abs(x) for x in row) == [0, 0, 1] for row in A)
    cols_ok = all(sorted(abs(A[i][j]) for i in range(3)) == [0, 0, 1]
                  for j in range(3))
    return rows_ok and cols_ok


# ------------------------------------------------------------------------ V0
def v0_rederive(cid, ent, groups):
    w = ent["first_witness"]
    g = groups[w["group"]]
    p = tuple(F(s) for s in w["point"])
    ob = orbit.orbit(g, p)
    assert ob["stabilizer_order"] == w["stabilizer_order"], "stabilizer drift"
    assert ob["n_conventional"] == w["orbit_conventional"], "orbit size drift"
    assert ob["n_primitive"] == w["orbit_primitive"], "primitive count drift"
    assert wyckoff_dim(g, p) == w["stratum_dim"], "stratum dim drift"
    pts, period = orbit.scale_orbit(ob["points"])

    try:
        cells_f, W = sweep(pts, period, W=2), 2
    except RuntimeError:
        cells_f, W = sweep(pts, period, W=3), 3
    assert W == w["W"], "window drift"

    ec = clip_cell(pts[0], pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2, "cutoff certificate violated"
    Fc = ec["facet_count"]
    V = ec["n_vertices"]
    E = sum(len(c) for c in ec["facet_cycles"]) // 2
    assert V - E + Fc == 2, "Euler failure"
    assert Fc <= MAX_FACETS, f"KILL: {Fc} > {MAX_FACETS} facets (assume bug)"

    f0 = cells_f[0]
    nbr_f = {tuple(pts[0][k] + d[k] for k in range(3))
             for d in f0["neighbor_deltas"]}
    agree = (f0["facet_count"] == Fc and f0["p_vector"] == ec["p_vector"]
             and nbr_f == set(ec["neighbors"]))
    assert agree or f0["degenerate_flag"], "float/exact disagree, unflagged"
    assert f0["degenerate_flag"] == w["degenerate_flag"], "degen flag drift"
    assert ((not agree) and f0["degenerate_flag"]) == w["float_superseded"]
    assert ec["nonsimple_vertices"] == w["nonsimple_vertices"], "nonsimple drift"

    code, aut = canonical_code(ec["facet_cycles"])
    assert code.decode("ascii") == ent["canon_code"], "canonical code MISMATCH"
    assert [V, E, Fc] == list(ent["f_vector"]), "f-vector mismatch"
    assert list(ec["p_vector"]) == list(ent["p_vector"]), "p-vector mismatch"
    assert aut == ent["aut_order"], "aut order mismatch"

    return {
        "cid": cid, "ent": ent, "witness": w, "g": g, "p": p, "ob": ob,
        "pts": pts, "period": period, "ec": ec,
        "code": code.decode("ascii"), "aut": aut, "Fc": Fc, "V": V, "E": E,
        "site_ops": orbit.site_stabilizer(g, p),
        "detail": (f"IT({w['group']}) {w['group_symbol']} p=({', '.join(w['point'])}) "
                   f"period={period} n_conv={ob['n_conventional']} "
                   f"T={ob['n_primitive']} f=({V},{E},{Fc}) "
                   f"p-vec {pvec_compact(ec['p_vector'])} aut={aut} "
                   f"cutoff_D={ec['cutoff_D']} 4rho2={4*ec['rho2']}"),
    }


# ------------------------------------------------------- V1 (generator side)
def v1_generate(ctx):
    pts, P = ctx["pts"], ctx["period"]
    n = len(pts)
    Bcols, detL = derive_lattice(pts, P)
    assert (n * detL) % P**3 == 0, "site density not integral"
    T = n * detL // P**3
    assert T == ctx["ob"]["n_primitive"], "T != stored orbit_primitive"
    Bf = [[F(Bcols[i][j]) for j in range(3)] for i in range(3)]
    Binv = mat_inv(Bf)

    def lat_int(vec):
        cc = mat_vec(Binv, vec)
        return to_int_vec(cc) if all(F(x).denominator == 1 for x in cc) \
            else None

    for e in ((P, 0, 0), (0, P, 0), (0, 0, P)):
        assert lat_int(e) is not None, "P*e_i not in L"

    # types: partition sites by L-congruence, first-seen reps in pts order
    type_of, type_reps = {}, []
    for i, q in enumerate(pts):
        for ti, r in enumerate(type_reps):
            if lat_int(vsub(q, pts[r])) is not None:
                type_of[i] = ti
                break
        else:
            type_of[i] = len(type_reps)
            type_reps.append(i)
    assert len(type_reps) == T and type_reps[0] == 0

    base_index = {q: i for i, q in enumerate(pts)}

    def id_of_site(q):
        b = base_index[tuple(x % P for x in q)]
        tj = type_of[b]
        v = lat_int(vsub(q, pts[type_reps[tj]]))
        assert v is not None, f"site {q} not L-congruent to its type rep"
        return v, tj

    # exact cells for ALL T representatives (rep 0 = the V0 cell, reused)
    cells = [ctx["ec"] if r == 0 else clip_cell(pts[r], pts, P)
             for r in type_reps]
    for e in cells:
        assert 4 * e["rho2"] <= e["cutoff_D"] ** 2
        assert e["facet_count"] == ctx["Fc"]
        assert e["p_vector"] == ctx["ec"]["p_vector"]
        code, _ = canonical_code(e["facet_cycles"])
        assert code.decode("ascii") == ctx["code"], \
            "rep cell combinatorial type differs (congruence broken)"

    # V1b volume identity (exact, from geometry)
    vols = [cell_volume_from_cycles(e) for e in cells]
    assert all(v == vols[0] for v in vols), "rep volumes differ"
    assert T * vols[0] == F(detL), "T*vol != detL"
    assert vols[0] == F(P**3, n), "vol != P^3/n"

    # facet data: per rep, list of (frozenset of vertex coords, neighbor site)
    facets_per = []
    for e in cells:
        facets_per.append([(frozenset(e["vertices"][i] for i in cyc), q)
                           for cyc, q in zip(e["facet_cycles"], e["neighbors"])])

    # V1c full-facet pairing: every T*F slot pairs with EXACTLY ONE reciprocal
    Fc = ctx["Fc"]
    pairings = []
    for ti, e in enumerate(cells):
        c = e["center"]
        for fs, q in facets_per[ti]:
            lam, tj = id_of_site(q)
            delta = vsub(q, pts[type_reps[tj]])          # == B*lam, integer
            assert to_int_vec(mat_vec(Bf, lam)) == tuple(delta)
            hits = 0
            for fs2, q2 in facets_per[tj]:
                if tuple(q2[k] + delta[k] for k in range(3)) == c:
                    tv = frozenset(tuple(wv[k] + delta[k] for k in range(3))
                                   for wv in fs2)
                    if tv == fs:
                        hits += 1
            assert hits == 1, f"facet slot ({ti}) pairing count {hits} != 1"
            pairings.append({"rep": ti, "nbr_type": tj,
                             "delta": list(delta),
                             "shared": [[str(x) for x in wv] for wv in
                                        sorted(fs)]})
    assert len(pairings) == T * Fc

    # V1d translate-completeness + interior disjointness
    rho2 = cells[0]["rho2"]
    assert all(e["rho2"] == rho2 for e in cells), "rep circumradii differ"
    D = ball_D(rho2)
    ball_sizes = []
    for ti, e in enumerate(cells):
        c = e["center"]
        ball = candidates_near(c, pts, P, D)
        ball_sizes.append(len(ball))
        nbrset = set(e["neighbors"])
        assert nbrset <= set(ball), "facet neighbor beyond the 2rho ball"
        for r in ball:
            a = tuple(2 * (r[k] - c[k]) for k in range(3))
            b = sum(r[k]*r[k] - c[k]*c[k] for k in range(3))
            onv = []
            for wv in e["vertices"]:
                s = vdot(a, wv) - b
                assert s <= 0, \
                    f"cell vertex strictly beyond bisector of in-ball site {r}"
                if s == 0:
                    onv.append(wv)
            if r not in nbrset and len(onv) >= 3:
                u0 = vsub(onv[1], onv[0])
                assert all(vcross(u0, vsub(wv, onv[0])) == (0, 0, 0)
                           for wv in onv[2:]), \
                    f"2-face contact with unlisted site {r}"

    cert = {
        "type_id": ctx["cid"], "T": T, "F": Fc, "detL": detL,
        "period": P, "n_sites_conventional": n,
        "lattice_basis_columns": [[Bcols[i][j] for i in range(3)]
                                  for j in range(3)],
        "volume_each": str(vols[0]),
        "representatives": [[[str(x) for x in v] for v in e["vertices"]]
                            for e in cells],
        "rep_centers": [list(e["center"]) for e in cells],
        "pairings": pairings,
    }
    lat = {"Bcols": Bcols, "Bf": Bf, "Binv": Binv, "detL": detL, "T": T,
           "type_of": type_of, "type_reps": type_reps, "cells": cells,
           "lat_int": lat_int, "id_of_site": id_of_site, "rho2": rho2,
           "ball_D": D, "vol": vols[0]}
    detail = (f"detL={detL} T={T} vol={vols[0]} T*vol={T*vols[0]} "
              f"slots={T*Fc} paired 1:1; disjointness ball D={D} "
              f"(D^2={D*D} >= 4rho2={4*rho2}), ball sizes "
              f"{min(ball_sizes)}..{max(ball_sizes)} sites/rep, all bisectors "
              f"weakly satisfied, no unlisted 2-face contact")
    return cert, lat, detail


# ---------------------------------------------- V1 INDEPENDENT ADAPTED AUDIT
# Fresh geometry code below this line: shares NOTHING with exact_cell /
# mint_tables / the generator above (own vector ops, own det, own
# supporting-plane facet scan, own volume; audit_t1_independent.py C1-C3
# adapted).  Input is the certificate DATA only.
def _a_sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def _a_add(a, b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def _a_dot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def _a_cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def _a_det3(a, b, c):
    return _a_dot(a, _a_cross(b, c))


def _a_facets(pts):
    """Exact facet list of the convex hull of pts: supporting-plane scan over
    vertex triples, deduped by on-plane vertex set; cyclic order proposed by
    float atan2, VERIFIED by exact convexity (every consecutive edge cross
    aligned with the outward normal)."""
    npts = len(pts)
    out, seen = [], set()
    for i, j, k in itertools.combinations(range(npts), 3):
        nrm = _a_cross(_a_sub(pts[j], pts[i]), _a_sub(pts[k], pts[i]))
        if nrm == (0, 0, 0):
            continue
        offs = _a_dot(nrm, pts[i])
        sides = [_a_dot(nrm, q) - offs for q in pts]
        pos = any(s > 0 for s in sides)
        neg = any(s < 0 for s in sides)
        if pos and neg:
            continue
        if pos:                                   # make normal outward
            nrm = tuple(-x for x in nrm)
            offs = -offs
        onv = frozenset(m for m in range(npts)
                        if _a_dot(nrm, pts[m]) == offs)
        if onv in seen:
            continue
        seen.add(onv)
        fp = [pts[m] for m in sorted(onv)]
        cen = tuple(sum(col) / len(fp) for col in zip(*fp))
        u = _a_sub(fp[1], fp[0])
        wax = _a_cross(nrm, u)
        ang = sorted(range(len(fp)),
                     key=lambda m: math.atan2(
                         float(_a_dot(_a_sub(fp[m], cen), wax)),
                         float(_a_dot(_a_sub(fp[m], cen), u))))
        poly = [fp[m] for m in ang]
        for t in range(len(poly)):
            a, b, cc = poly[t], poly[(t+1) % len(poly)], poly[(t+2) % len(poly)]
            assert _a_dot(_a_cross(_a_sub(b, a), _a_sub(cc, b)), nrm) > 0, \
                "audit: facet cyclic order failed exact convexity"
        out.append((nrm, offs, poly, onv))
    return out


def _a_volume(pts, fs):
    c = pts[0]
    vol = F(0)
    for nrm, offs, poly, _ in fs:
        for t in range(1, len(poly) - 1):
            vol += abs(_a_det3(_a_sub(poly[0], c), _a_sub(poly[t], c),
                               _a_sub(poly[t+1], c)))
    return vol / 6


def v1_audit(cert):
    T, Fc, detL = cert["T"], cert["F"], cert["detL"]
    reps = [[tuple(F(s) for s in v) for v in cell]
            for cell in cert["representatives"]]
    cols = cert["lattice_basis_columns"]
    b1, b2, b3 = (tuple(F(cols[j][i]) for i in range(3)) for j in range(3))
    d = _a_det3(b1, b2, b3)
    assert abs(d) == detL, "audit: |det basis| != claimed detL"

    repfacets, vols = [], []
    for pts in reps:
        fs = _a_facets(pts)
        assert len(fs) == Fc, f"audit: facet count {len(fs)} != {Fc}"
        # closed surface: every edge of the facet polygons in exactly 2 facets
        from collections import Counter
        ecount = Counter()
        for _, _, poly, _ in fs:
            for t in range(len(poly)):
                ecount[frozenset((poly[t], poly[(t+1) % len(poly)]))] += 1
        assert all(v == 2 for v in ecount.values()), "audit: surface not closed"
        Vv, Ee = len(pts), len(ecount)
        assert Vv - Ee + Fc == 2, "audit: Euler failure"
        repfacets.append(fs)
        vols.append(_a_volume(pts, fs))
    assert all(v == vols[0] for v in vols), "audit: volumes differ"
    assert vols[0] == F(cert["volume_each"]), "audit: volume != claimed"
    assert T * vols[0] == abs(d), "audit: T*vol != |det basis|"

    onsets = [{fs[3]: fi for fi, fs in enumerate(rfs)} for rfs in repfacets]
    vert_index = [{v: m for m, v in enumerate(pts)} for pts in reps]
    slots = set()
    for pr in cert["pairings"]:
        ti, tj = pr["rep"], pr["nbr_type"]
        delta = tuple(int(x) for x in pr["delta"])
        shared = frozenset(tuple(F(s) for s in v) for v in pr["shared"])
        # shared set must be a FULL facet of the rep cell (audit's own facets)
        on_rep = frozenset(vert_index[ti][v] for v in shared)
        assert on_rep in onsets[ti], "audit: shared set is not a rep facet"
        fi = onsets[ti][on_rep]
        assert frozenset(repfacets[ti][fi][2]) == shared
        # ... and a FULL facet of the translated neighbor cell
        back = frozenset(_a_sub(v, delta) for v in shared)
        on_nbr = frozenset(vert_index[tj][v] for v in back)
        assert on_nbr in onsets[tj], "audit: shared set is not a nbr facet"
        key = (ti, fi)
        assert key not in slots, "audit: facet slot paired twice"
        slots.add(key)
    assert slots == {(t, f) for t in range(T) for f in range(Fc)}, \
        "audit: pairing table does not cover all T*F slots exactly once"
    return (f"audit re-derived {T} cells x {Fc} facets (supporting-plane "
            f"scan), closed surfaces, Euler ok; volumes {vols[0]} each, "
            f"T*vol == |det|; all {T*Fc} pairing claims verified full-facet "
            f"both sides, slots covered exactly once")


# ------------------------------------------------------------------------ V2
def cell_stabilizer(verts):
    """All orthogonal maps (about the vertex centroid) preserving the vertex
    set — Gram-triple matching, audit_t1 C6 pattern (fully general, no
    signed-perm assumption)."""
    npts = len(verts)
    cen = tuple(sum(col) / npts for col in zip(*verts))
    cent = [vsub(v, cen) for v in verts]
    centset = set(cent)
    b1 = cent[0]
    b2 = next(q for q in cent[1:] if vcross(b1, q) != (0, 0, 0))
    b3 = next(q for q in cent if det3(b1, b2, q) != 0)
    G = [[vdot(a, b) for b in (b1, b2, b3)] for a in (b1, b2, b3)]
    Bm = [[b1[i], b2[i], b3[i]] for i in range(3)]
    Binv = mat_inv(Bm)
    stab = set()
    for w1 in cent:
        if vdot(w1, w1) != G[0][0]:
            continue
        for w2 in cent:
            if vdot(w2, w2) != G[1][1] or vdot(w1, w2) != G[0][1]:
                continue
            for w3 in cent:
                if vdot(w3, w3) != G[2][2] or vdot(w1, w3) != G[0][2] \
                        or vdot(w2, w3) != G[1][2]:
                    continue
                Wm = [[w1[i], w2[i], w3[i]] for i in range(3)]
                A = mat_mul(Wm, Binv)
                AtA = [[sum(A[k][i]*A[k][j] for k in range(3))
                        for j in range(3)] for i in range(3)]
                if AtA != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
                    continue
                img = set(tuple(sum(A[i][j]*q[j] for j in range(3))
                                for i in range(3)) for q in cent)
                if img == centset:
                    stab.add(tuple(tuple(F(x) for x in row) for row in A))
    return stab


def bravais_point_group(Bcols):
    """All U in GL3(Z) with U^T G U == G for G = B^T B (the Bravais point
    group of the actual lattice, in the lattice basis).  Completeness: column
    j of U is the coefficient vector u of a lattice vector w with
    |w|^2 == G[j][j]; u_i = e_i^T B^{-1} w, so by Cauchy-Schwarz
    u_i^2 <= (G^{-1})_{ii} * |w|^2 — an exact enumeration bound."""
    Bf = [[F(Bcols[i][j]) for j in range(3)] for i in range(3)]
    G = [[sum(Bf[k][i]*Bf[k][j] for k in range(3)) for j in range(3)]
         for i in range(3)]
    Ginv = mat_inv(G)
    nmax = max(G[i][i] for i in range(3))
    bnd = [isqrt_frac_floor(Ginv[i][i] * nmax) for i in range(3)]
    cand = {i: [] for i in range(3)}
    for u in itertools.product(*(range(-bnd[i], bnd[i]+1) for i in range(3))):
        q = sum(u[i]*G[i][j]*u[j] for i in range(3) for j in range(3))
        for i in range(3):
            if q == G[i][i]:
                cand[i].append(u)
    group = []
    for u1 in cand[0]:
        for u2 in cand[1]:
            if sum(u1[i]*G[i][j]*u2[j] for i in range(3)
                   for j in range(3)) != G[0][1]:
                continue
            for u3 in cand[2]:
                if sum(u1[i]*G[i][j]*u3[j] for i in range(3)
                       for j in range(3)) != G[0][2]:
                    continue
                if sum(u2[i]*G[i][j]*u3[j] for i in range(3)
                       for j in range(3)) != G[1][2]:
                    continue
                U = tuple(tuple((u1, u2, u3)[j][i] for j in range(3))
                          for i in range(3))
                assert abs(mat_det(U)) == 1
                group.append(U)
    Binv = mat_inv(Bf)
    embedded = []
    for U in group:
        Rm = mat_mul(mat_mul(Bf, [[F(U[i][j]) for j in range(3)]
                                  for i in range(3)]), Binv)
        RtR = [[sum(Rm[k][i]*Rm[k][j] for k in range(3)) for j in range(3)]
               for i in range(3)]
        assert RtR == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], \
            "embedded Bravais op not orthogonal (impossible if G preserved)"
        embedded.append((U, tuple(tuple(x for x in row) for row in Rm)))
    return embedded


def v2_symmetry(ctx, lat):
    stab = cell_stabilizer(ctx["ec"]["vertices"])
    site_R = {tuple(tuple(F(x) for x in row) for row in Rm)
              for Rm, _ in ctx["site_ops"]}
    assert len(site_R) == len(ctx["site_ops"]), "site ops with equal R (!)"
    assert site_R <= stab, "site symmetry not contained in cell stabilizer"
    n_site, n_geo, n_aut = len(site_R), len(stab), ctx["aut"]
    assert n_geo % n_site == 0, "site order does not divide stabilizer order"
    assert n_aut % n_geo == 0, "stabilizer order does not divide aut order"
    brav = bravais_point_group(lat["Bcols"])
    n_brav = len(brav)
    all_sp_stab = all(is_signed_perm([[x for x in row] for row in A])
                      for A in stab)
    all_sp_brav = all(is_signed_perm([[x for x in row] for row in Rm])
                      for _, Rm in brav)
    detail = (f"site={n_site}, stab_geo={n_geo} (ALL orthogonal maps, "
              f"Gram-triple), aut_comb={n_aut}; chain site<=stab_geo "
              f"contained, divisibility {n_site}|{n_geo}|{n_aut} holds; "
              f"Bravais point group of L: order {n_brav} "
              f"(GL3(Z) Gram-preserving, proven coefficient bound), embedded "
              f"ops {'all' if all_sp_brav else 'NOT all'} signed perms "
              f"(checked, not assumed); stabilizer elements "
              f"{'all' if all_sp_stab else 'NOT all'} signed perms")
    return {"n_site": n_site, "n_geo": n_geo, "n_aut": n_aut,
            "n_brav": n_brav, "brav": brav, "all_sp_brav": all_sp_brav,
            "all_sp_stab": all_sp_stab, "detail": detail}


# ------------------------------------------------------------------------ V3
def v3_tables_burnside(ctx, lat, sym, deadline):
    pts, P = ctx["pts"], ctx["period"]
    T, Fc = lat["T"], ctx["Fc"]
    Bf, Binv = lat["Bf"], lat["Binv"]
    type_reps, cells = lat["type_reps"], lat["cells"]
    id_of_site = lat["id_of_site"]
    assert T <= 127, "enumerate.cpp limit T<=127"

    # nbr table (uniform neighbor count per type — congruent cells)
    nbr_table = []
    for ti, e in enumerate(cells):
        row = []
        for q in e["neighbors"]:
            v, tj = id_of_site(q)
            row.append([list(v), tj])
        assert len(row) == Fc
        nbr_table.append(row)
    for ti, row in enumerate(nbr_table):
        for dv, tj in row:
            assert any(dv2 == [-dv[0], -dv[1], -dv[2]] and t2 == ti
                       for dv2, t2 in nbr_table[tj]), "asymmetric adjacency"

    # ops: for each Bravais-embedded orthogonal R, the (unique mod L)
    # translation c with R*S + c == S, if any.  Complete: any honeycomb point
    # op preserves L (=> R in the Bravais embedding, enumerated exhaustively
    # with a proven bound) and maps site pts[0] to a site (=> c is one of the
    # tried anchors mod L; translations preserving S are exactly L, so at
    # most one op per R mod lattice).
    siteset = {tuple(F(x) for x in q) for q in pts}
    ops_geo = []
    for U, Rm in sym["brav"]:
        found = None
        for bp in pts:
            c = tuple(F(bp[k]) - sum(Rm[k][j]*pts[0][j] for j in range(3))
                      for k in range(3))
            img = set(tuple((sum(Rm[k][j]*s[j] for j in range(3)) + c[k]) % P
                            for k in range(3)) for s in pts)
            if img == siteset:
                found = (U, Rm, c)
                break
        if found is not None:
            ops_geo.append(found)

    def op_idspace(Rm, c):
        A = to_int_mat(mat_mul(mat_mul(Binv, [[F(x) for x in row]
                                              for row in Rm]), Bf))
        assert abs(mat_det(A)) == 1
        per = []
        for ti, rep in enumerate(type_reps):
            img = tuple(sum(Rm[k][j]*pts[rep][j] for j in range(3)) + c[k]
                        for k in range(3))
            v, tj = id_of_site(to_int_vec(img))
            per.append([list(v), tj])
        return [list(r) for r in A], per

    # identity FIRST (burnside_generic.py convention: Fix of ops[0] is
    # compared to the translation-fixed count), rest in deterministic order
    ops_geo.sort(key=lambda t: (t[0] != ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                t[0]))
    ops_id = [op_idspace(Rm, c) for _, Rm, c in ops_geo]
    dets = [mat_det(U) for U, _, _ in ops_geo]

    def opkey(A, per):
        return (tuple(map(tuple, A)), tuple(tj for _, tj in per),
                tuple(tuple(per[t][0][i] - per[0][0][i] for i in range(3))
                      for t in range(T)))

    keyset = {opkey(A, p) for A, p in ops_id}
    assert len(keyset) == len(ops_id), "duplicate ops mod lattice translation"
    assert any(A == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
               and all(p[t][1] == t for t in range(T))
               and all(p[t][0] == p[0][0] for t in range(T))
               for A, p in ops_id), "identity op missing"

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

    n_proper = sum(1 for d in dets if d == 1)
    tables = {
        "T": T, "nbr": nbr_table,
        "ops": [{"A": A, "map": per} for A, per in ops_id],
        "proper_ops": [{"A": A, "map": per}
                       for (A, per), d in zip(ops_id, dets) if d == 1],
        "lattice_basis": [[lat["Bcols"][i][j] for i in range(3)]
                          for j in range(3)],
        "detL": lat["detL"], "cell_volume": str(lat["vol"]),
        "n_proper": n_proper, "n_improper": len(ops_id) - n_proper,
        "facet_signature": list(ctx["ec"]["p_vector"]),
    }
    tables_path = os.path.join(HERE, f"g4_tables_{ctx['cid']}.json")
    json.dump(tables, open(tables_path, "w"), indent=1)

    if time.time() > deadline:
        return {"deferred": True,
                "detail": (f"TIMEOUT-DEFERRED before enumeration: tables "
                           f"derived and written ({os.path.basename(tables_path)}: "
                           f"T={T}, nbrs={Fc}, |ops|={len(ops_id)} "
                           f"({n_proper} proper), closed); enumerator + "
                           f"Burnside not run")}

    # banked workflow: export -> compiled enumerate -> counts
    txt = os.path.join(HERE, f"g4_tables_{ctx['cid']}.txt")
    subprocess.run([PYTHON, EXPORT_TABLES, tables_path, txt, "ops"],
                   check=True, capture_output=True)
    r = subprocess.run([ENUM_BIN, txt, str(N_ENUM)], check=True,
                       capture_output=True, text=True)
    counts, seen_hdr = {}, False
    for line in r.stdout.splitlines():
        if line.strip() == "n fixed free":
            seen_hdr = True
            continue
        if seen_hdr and line.split():
            nn, fx, fr = line.split()
            counts[int(nn)] = (int(fx), int(fr))
    assert len(counts) == N_ENUM, "enumerator output parse failure"

    # banked burnside_generic.py: independent growth enumeration + identity
    free_s = ",".join(str(counts[n][1]) for n in range(1, N_ENUM+1))
    fixed_s = ",".join(str(counts[n][0]) for n in range(1, N_ENUM+1))
    rb = subprocess.run([PYTHON, BURNSIDE, ctx["cid"], tables_path,
                         str(N_ENUM), free_s, fixed_s],
                        capture_output=True, text=True)
    assert rb.returncode == 0, f"burnside_generic crashed: {rb.stderr[-400:]}"
    assert "ALL PASS" in rb.stdout, f"BURNSIDE FAILED:\n{rb.stdout}"

    detail = (f"tables T={T} nbrs={Fc} |ops|={len(ops_id)} "
              f"({n_proper} proper, {len(ops_id)-n_proper} improper; "
              f"T*|site|={T*sym['n_site']}), identity+closure exact; banked "
              f"enumerate n<={N_ENUM}: "
              f"fixed={[counts[n][0] for n in range(1, N_ENUM+1)]}, "
              f"free={[counts[n][1] for n in range(1, N_ENUM+1)]}; "
              f"burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS "
              f"n<={N_ENUM} (its independent fixed recount agrees)")
    return {"deferred": False, "counts": counts, "n_ops": len(ops_id),
            "n_proper": n_proper, "detail": detail}


# --------------------------------------------------------------------- driver
def certify_one(cid, ent, groups, say):
    t_c0 = time.time()
    deadline = t_c0 + BUDGET_S
    stages = []
    ctx = lat = sym = None

    def stage(name, fn):
        t0 = time.time()
        try:
            out = fn()
            dt = time.time() - t0
            verdict = "DEFERRED" if isinstance(out, dict) \
                and out.get("deferred") else "PASS"
            detail = out["detail"] if isinstance(out, dict) and "detail" in out \
                else out if isinstance(out, str) else ""
            stages.append({"name": name, "verdict": verdict,
                           "detail": detail, "t": dt})
            say(f"  {name}: {verdict} ({dt:.1f}s) {detail[:110]}")
            return out
        except Exception:
            dt = time.time() - t0
            tb = traceback.format_exc().strip().splitlines()[-1]
            stages.append({"name": name, "verdict": "FAIL",
                           "detail": tb, "t": dt})
            say(f"  {name}: FAIL ({dt:.1f}s) {tb}")
            raise

    say(f"[{cid}] f={tuple(ent['f_vector'])} "
        f"p={pvec_compact(ent['p_vector'])} aut={ent['aut_order']} "
        f"witness IT({ent['first_witness']['group']}) "
        f"{ent['first_witness']['group_symbol']}")
    try:
        ctx = stage("V0 exact re-derivation",
                    lambda: v0_rederive(cid, ent, groups))
        cert_lat = stage("V1 tiling certificate (generator)",
                         lambda: dict(zip(("cert", "lat", "detail"),
                                          v1_generate(ctx))))
        cert, lat = cert_lat["cert"], cert_lat["lat"]
        stage("V1 independent adapted audit",
              lambda: v1_audit(json.loads(json.dumps(cert))))
        sym = stage("V2 symmetry certification", lambda: v2_symmetry(ctx, lat))
        stage("V3 Burnside identity",
              lambda: v3_tables_burnside(ctx, lat, sym, deadline))
    except Exception:
        pass                                   # recorded; ladder stops here
    return {"cid": cid, "ent": ent, "stages": stages,
            "elapsed": time.time() - t_c0, "ctx": ctx, "sym": sym, "lat": lat}


def write_results(results, total_s):
    L = ["# G4 certificate results — V0-V3 ladder (2026-08-30)", "",
         "Gate: `../ANCHORS.md` G4 (paper-I-standard ladder, V0-V3 per "
         "`../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3). Generator: "
         "`g4_certify.py` (this run). Inputs: `phase1_types.json` stored "
         "witnesses, frozen G1 `spacegroups.json`, the G0/G2-validated "
         "pipeline. V1's independent audit shares no geometry code with "
         "`exact_cell.py`/`mint_tables.py` (fresh facet/volume/pairing "
         "implementations inside `g4_certify.py`, `_a_*`/`v1_audit`). V3 "
         "uses the banked `export_tables.py` + compiled `enumerate` + "
         "`burnside_generic.py` (POLYFORMS_II).", "",
         "**LANGUAGE (stated once): G4 passing does NOT establish novelty. "
         "These types remain \"not matched against the catalog snapshot of "
         "2026-08-28\"; novelty diligence is G5 and has not run on them. "
         "Kill criteria were live (facet count > 38 asserts; none hit).**",
         ""]
    allpass = True
    for r in results:
        ent, w = r["ent"], r["ent"]["first_witness"]
        if r["cid"] == BATCH2_IDS[0]:
            L.append("---")
            L.append("")
            L.append("# BATCH 2 (2026-08-30, later) — remaining 8 of the "
                     "11-candidate G4 queue")
            L.append("")
            L.append("The 2 remaining Schmitt-collision-screen survivors "
                     "(`SCHMITT_COLLISION_RESULTS.md`) followed by the 6 "
                     "remaining ABSENT-all triage types "
                     "(`TRIAGE_RESULT.md`; `8cf50403cf88c455` was certified "
                     "in batch 1). Same ladder, same script, same language "
                     "gate as above.")
            L.append("")
        L.append(f"## `{r['cid']}` — IT({w['group']}) {w['group_symbol']}, "
                 f"f={tuple(ent['f_vector'])}, "
                 f"p={pvec_compact(ent['p_vector'])}, aut={ent['aut_order']}")
        L.append("")
        L.append(f"Witness point ({', '.join(w['point'])}), site stabilizer "
                 f"{w['stabilizer_order']}, orbit {w['orbit_conventional']} "
                 f"conventional / {w['orbit_primitive']} primitive. "
                 f"Candidate wall time {r['elapsed']:.1f}s.")
        L.append("")
        L.append("| stage | verdict | wall | key numbers |")
        L.append("|---|---|---|---|")
        for s in r["stages"]:
            allpass &= s["verdict"] == "PASS"
            L.append(f"| {s['name']} | **{s['verdict']}** | {s['t']:.1f}s | "
                     f"{s['detail']} |")
        done = {s["name"].split()[0] for s in r["stages"]}
        for missing in ("V0", "V1", "V2", "V3"):
            if missing not in done:
                allpass = False
                L.append(f"| {missing} | **NOT REACHED** | — | quarantined "
                         f"downstream of the failure above |")
        L.append("")
        if r["sym"] is not None:
            sy = r["sym"]
            L.append(f"Symmetry reconciliation: site symmetry "
                     f"{sy['n_site']} <= geometric stabilizer {sy['n_geo']} "
                     f"<= combinatorial aut {sy['n_aut']} (containment + "
                     f"divisibility verified exactly). Bravais point group "
                     f"of the actual lattice: order {sy['n_brav']}, embedded "
                     f"ops {'ARE' if sy['all_sp_brav'] else 'are NOT'} the "
                     f"signed permutations (checked, not assumed).")
            L.append("")
    L.append(f"Total wall time {total_s:.0f}s. Deterministic except the "
             f"timing decimals. Certified artifacts: `g4_tables_<id>.json` "
             f"(+ `.txt` enumerator input) per candidate.")
    L.append("")
    L.append("Re-run for acceptance: "
             "`python3 "
             "g4_certify.py` (exit 0 required).")
    open(os.path.join(HERE, "G4_RESULTS.md"), "w").write("\n".join(L) + "\n")
    return allpass


def main(argv):
    ids = argv[1:] or DEFAULT_IDS
    store = json.load(open(STORE))["types"]
    groups = orbit.load_groups()
    t0 = time.time()
    results = []
    for cid in ids:
        assert cid in store, f"unknown type id {cid}"
        results.append(certify_one(cid, store[cid], groups, print))
    allpass = write_results(results, time.time() - t0)
    print(f"\nG4 VERDICT: {'ALL STAGES PASS' if allpass else 'FAIL/DEFERRED'} "
          f"({time.time()-t0:.0f}s) — wrote G4_RESULTS.md")
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
