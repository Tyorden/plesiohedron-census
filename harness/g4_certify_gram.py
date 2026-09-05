#!/usr/bin/env python
"""g4_certify_gram.py — G4 finalist certificate ladder (ANCHORS G4, verbatim
gate) for PHASE 2 (tetragonal, rational Gram metric).  Sibling of the ACCEPTED
cubic ladder g4_certify.py (unmodified; its metric-independent pieces are
imported and reused: exact vector bits, the coordinate-space fan volume, the
INDEPENDENT affine audit `v1_audit` with its `_a_*` supporting-plane scan, and
the banked V3 tool paths).  Everything metric-dependent is re-derived here
through the accepted Gram chain (phase2/metric.py, phase2/sweep_voronoi_gram.py,
phase2/exact_cell_gram.py).

METRIC CONVENTIONS (ANCHORS G2b block): sites and vertices live in the ITA
conventional (crystal) basis of the frozen G1 ops, scaled by an integer PERIOD;
the metric is the integer Gram matrix G = diag(q^2, q^2, p^2) for c/a = p/q
(G = I for a cubic group).  Distances are G-norms |x|_G^2 = x^T G x; bisectors
are 2(r-c)^T G x = r^T G r - c^T G c; the cutoff certificate 4 rho^2 <= D^2 is
held in the G-norm with the candidate block proven complete by the coordinate
bound |x_i| <= D sqrt((G^-1)_ii).  VOLUMES: every volume in this file is the
coordinate-space (crystal-basis) Lebesgue measure; the Euclidean volume is that
times the SAME factor sqrt(det G)/q^3 (uniform for the cell, the lattice
covolume and the torus), so the tiling identity T * vol(cell) = covol(L) is an
exact-rational identity in the crystal basis and equivalent to the Euclidean
one.  Facets of a convex polytope and full-facet pairings are affine notions
(metric-free); the metric enters the tiling certificate only through the
Voronoi bisector claims, which are re-verified in the G-norm.

STAGES (per candidate; per-stage cap STAGE_CAP_S -> TIMEOUT-DEFERRED)
  V0  exact re-derivation at the stored witness (group, point, b): orbit
      (frozen ops) -> sweep_gram float proposal (W=2, W=3 retry) -> exact
      clip_cell_gram (cutoff asserted, R^T G R = G asserted) -> canonical code.
      Assert code, f-vector, p-vector, aut and every witness field match the
      store.  KILL criterion live: > 38 facets aborts.
  V1  tiling certificate in the G-norm: exact primitive lattice L (metric-
      independent translation lattice), T = n detL / P^3 == orbit_primitive,
      exact Gram cells for ALL T type representatives (identical code),
      volume identity T*vol == detL == P^3/n * T (crystal basis, exact),
      full-facet 1:1 pairing over all T*F slots, translate-completeness +
      interior disjointness over the certified G-ball |r-c|_G^2 <= 4 rho^2
      (candidates_near_gram, coordinate bound) — every in-ball site's
      G-bisector weakly satisfied by every vertex, 2-face contacts only with
      listed neighbours.  Then the INDEPENDENT ADAPTED AUDIT: g4_certify's
      fresh supporting-plane scan / volume / pairing audit (affine, verbatim)
      PLUS a fresh Gram layer here (own quadratic form code, no metric.py):
      every shared facet vertex is G-equidistant from the two centres, every
      vertex of every rep is weakly G-closer to its own centre than to every
      paired neighbour centre, and every shared facet's supporting normal is
      parallel to G (r - c).  The audit consumes the certificate as DATA.
  V2  symmetry: site stabilizer from the frozen ops; combinatorial aut from the
      canonical code; SOLID isometry group = the map automorphisms (all
      enumerated from the code machinery, c2_isometry pattern) whose vertex
      permutation preserves the G-quadratic form on every vertex pair (exact),
      each realised by an affine map A x + t solved exactly and asserted
      A^T G A = G; independently re-derived by a G-Gram-triple scan about the
      vertex centroid (audit_t1 C6 pattern in the G-inner product) and
      asserted equal.  Reported: |site|, |Isom_fix_site|, |Isom|, |Isom+|,
      chirality of the solid, aut; containment site <= Isom_fix_site (linear
      parts) and divisibility site | Isom_fix | Isom | aut.  Bravais point
      group of the ACTUAL lattice in the G metric (GL3(Z) preserving
      G_L = B^T G B, proven coefficient bound).  Honeycomb point group H/L =
      all Bravais-embedded R with a translation carrying the site set to
      itself; |H/L| == T*|site| iff the full symmetry group of the honeycomb
      is exactly the generating space group G (checked, reported).  Hands of
      the translation classes from det of the ops.
  V3  Burnside on the derived honeycomb tables — TABLES ARE METRIC-INDEPENDENT
      ADJACENCY DATA (which cells share a facet, and the point ops mod L
      acting on cell IDs); the metric already did its work in V1/V2.  Banked
      export_tables.py + compiled enumerate n<=4 + burnside_generic.py
      (identity |ops|*free(n) == sum Fix_m(n)); then the INDEPENDENT
      enumerator publication/verify_counts_independent.py to n<=5 under a
      15-min cap (dual-implementation bar: fixed/free must agree for n<=4;
      the reached n is recorded).

SANITY GATE (runs first, must pass before any tetragonal cell): the truncated
octahedron control — I4/mmm #139 origin orbit at c/a = 1 (identity metric)
through THIS ladder must reproduce, number for number, the ACCEPTED cubic
ladder (g4_certify.py functions) on the Im-3m #229 origin orbit: code, f, p,
aut, T, detL, volume, slots, site / stabilizer / aut orders, Bravais order,
|ops|, proper count, fixed/free n<=4.  Second control: the banked cubic G4
certificate row for ceb70631e274e727 (IT 212, G4_RESULTS.md) reproduced by this
ladder with G = I.

LANGUAGE (stated once): G4 passing does NOT establish novelty — every type
here stays "not matched against the catalog snapshot of 2026-09-03"; G5 is
separate.  Snapshot language throughout.

Run:
  python3 \
      g4_certify_gram.py [type_id ...]            (default: the 14 survivors)
Writes: g4p2_tables_<id>.json / .txt (+ _indep.json), G4_PHASE2_RESULTS.md.
Exit 0 iff the sanity gate and every stage of every candidate PASS (DEFERRED
counts as non-zero exit; a FAIL always exits 1).
"""
import itertools
import json
import os
import subprocess
import sys
import time
import traceback
from collections import Counter
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "phase2"))

import orbit                                                    # noqa: E402
import metric                                                   # noqa: E402
from sweep_voronoi_gram import sweep_gram                       # noqa: E402
from exact_cell_gram import clip_cell_gram, candidates_near_gram  # noqa: E402
from canon_code import canonical_code, rotation_system          # noqa: E402
from sweep_phase1 import wyckoff_dim, is_lattice                # noqa: E402
from mint_tables import (det3, mat_det, mat_inv, mat_vec, mat_mul,  # noqa: E402
                         to_int_vec, to_int_mat, derive_lattice)
import g4_certify as G4C                                        # noqa: E402
from g4_certify import (vsub, vdot, vcross, pvec_compact,        # noqa: E402
                        cell_volume_from_cycles, isqrt_frac_floor,
                        EXPORT_TABLES, ENUM_BIN, BURNSIDE, PYTHON)

STORE = os.path.join(HERE, "phase2_types.json")
STORE_P1 = os.path.join(HERE, "phase1_types.json")
SEEDS = os.path.join(HERE, "seed_catalog.json")
INDEP = os.path.join(HERE, "..", "publication", "verify_counts_independent.py")
RESULTS_MD = os.path.join(HERE, "G4_PHASE2_RESULTS.md")

# priority order (COLLISION_PHASE2_RESULTS.md ranks): #8 reframed (excluded),
# #2 (wall / transition type) last, labelled.
QUEUE = [("1", "4e9c9b076cfec323"), ("3", "f654982d74d740f6"),
         ("4", "4f6d3e68cbd9e729"), ("5", "1497877268495988"),
         ("6", "e0d18e5ea938d649"), ("7", "6797ab70c6015039"),
         ("9", "086ac96faf390886"), ("10", "164d4bd63d82d0c3"),
         ("11", "5dc2479b9bc14edc"), ("12", "3ebbca7ed2eda199"),
         ("13", "7575121042ade3b3"), ("14", "213c7a114d5a97a8"),
         ("15", "2e8e49eb28497267"), ("2", "49cedbdd58376fac")]
RANK_OF = {cid: r for r, cid in QUEUE}
# open/wall status carried over (NOT re-derived here): perturbation verdicts
# from COLLISION_PHASE2_RESULTS.md for the top-3, triage labels
# (TRIAGE_PHASE2_RESULT.md, orbit-b counts) for the rest.
OPEN_WALL = {
    "4e9c9b076cfec323": "OPEN (perturbation: point OPEN / b OPEN)",
    "49cedbdd58376fac": "WALL/THIN BAND (perturbation: point WALL to 1/1536 / b OPEN)",
    "f654982d74d740f6": "OPEN (perturbation: point OPEN / b OPEN)",
    "4f6d3e68cbd9e729": "open-likely (triage, 5 b)",
    "1497877268495988": "open-likely (triage, 7 b)",
    "e0d18e5ea938d649": "open-likely (triage, 5 b)",
    "6797ab70c6015039": "open-likely (triage, 8 b)",
    "086ac96faf390886": "open-likely (triage, 5 b)",
    "164d4bd63d82d0c3": "open-likely (triage, 3 b)",
    "5dc2479b9bc14edc": "open-likely (triage, 3 b; metric-thin P5-only)",
    "3ebbca7ed2eda199": "indeterminate (triage, 2 b)",
    "7575121042ade3b3": "open-likely (triage, 8 b)",
    "213c7a114d5a97a8": "indeterminate (triage, 2 b; metric-thin P5-only)",
    "2e8e49eb28497267": "open-likely (triage, 4 b; metric-thin P5-only)",
}
LABEL = {"49cedbdd58376fac": "WALL/TRANSITION TYPE (thin band in (x,b), "
                             "COLLISION_PHASE2_RESULTS.md perturbation #2) — "
                             "certified as a tiling like the others; its "
                             "finalist status is a main-session call"}
MAX_FACETS = 38
N_ENUM = 4                    # banked depth
N_INDEP = 5                   # independent enumerator target depth
STAGE_CAP_S = 30 * 60         # per-stage cap -> TIMEOUT-DEFERRED
INDEP_CAP_S = 15 * 60         # dual-implementation bar
INDEP_WORKERS = None          # None = the enumerator's own default (unchanged);
                              # g4_certify_hex.py sets an integer so that
                              # parallel cells do not each spawn a full pool
TOTAL_BUDGET_S = 3 * 3600


# ------------------------------------------------------------- exact helpers
def gq(G, u):
    """u^T G u (exact)."""
    return sum(u[i] * G[i][j] * u[j] for i in range(3) for j in range(3))


def gform(G, u, v):
    return sum(u[i] * G[i][j] * v[j] for i in range(3) for j in range(3))


def gram_of(g, b):
    """Family / Gram switch (2026-09-04, hexagonal branch added for the
    batch-2 ladder g4_certify_hex.py; cubic + tetragonal behaviour unchanged).
    Hexagonal family = trigonal + hexagonal systems, ITA HEXAGONAL basis of the
    frozen ops (ANCHORS G2c): G = metric.gram_hexagonal(c/a)."""
    if g["crystal_family"] == "cubic":
        return metric.gram_cubic()
    if g["crystal_family"] == "hexagonal":
        return metric.gram_hexagonal(b)
    assert g["crystal_family"] == "tetragonal", g["crystal_family"]
    return metric.gram_tetragonal(b)


def fstr(x):
    return str(F(x))


# --------------------------------------------------------------------- V0
def v0_rederive(cid, ent, groups, w):
    g = groups[w["group"]]
    p = tuple(F(s) for s in w["point"])
    b = F(w["b"]) if w.get("b") is not None else None
    G0 = gram_of(g, b)
    assert metric.gram_compatible(g, G0), "R^T G R != G for some op"
    Gi, gscale = metric.scale_to_integers(G0)
    ob = orbit.orbit(g, p)
    dim = 3 if ob["stabilizer_order"] == 1 else wyckoff_dim(g, p)

    def chk(key, val):
        if key in w:
            assert w[key] == val, f"{key} drift: store {w[key]} vs {val}"
    chk("stabilizer_order", ob["stabilizer_order"])
    chk("orbit_conventional", ob["n_conventional"])
    chk("orbit_primitive", ob["n_primitive"])
    chk("stratum_dim", dim)
    pts, period = orbit.scale_orbit(ob["points"])
    chk("lattice_degenerate", is_lattice(pts, period))

    W = 2
    try:
        cells_f = sweep_gram(pts, period, G0, W=2, entry=g)
    except RuntimeError:
        cells_f, W = sweep_gram(pts, period, G0, W=3, entry=g), 3
    chk("W", W)

    ec = clip_cell_gram(pts[0], pts, period, G0)
    assert 4 * ec["rho2"] <= ec["cutoff_D2"], "cutoff certificate violated"
    assert ec["gram"] == Gi, "integer Gram drift"
    Fc, V, E = ec["facet_count"], ec["n_vertices"], ec["n_edges"]
    assert V - E + Fc == 2, "Euler failure"
    assert Fc <= MAX_FACETS, f"KILL: {Fc} > {MAX_FACETS} facets (assume bug)"

    f0 = cells_f[0]
    nbr_f = {tuple(pts[0][k] + d[k] for k in range(3))
             for d in f0["neighbor_deltas"]}
    agree = (f0["facet_count"] == Fc and f0["p_vector"] == ec["p_vector"]
             and nbr_f == set(ec["neighbors"]))
    assert agree or f0["degenerate_flag"], "float/exact disagree, unflagged"
    chk("degenerate_flag", f0["degenerate_flag"])
    chk("float_superseded", (not agree) and f0["degenerate_flag"])
    chk("nonsimple_vertices", ec["nonsimple_vertices"])

    code, aut = canonical_code(ec["facet_cycles"])
    assert code.decode("ascii") == ent["canon_code"], "canonical code MISMATCH"
    assert [V, E, Fc] == list(ent["f_vector"]), "f-vector mismatch"
    assert list(ec["p_vector"]) == list(ent["p_vector"]), "p-vector mismatch"
    assert aut == ent["aut_order"], "aut order mismatch"

    return {
        "cid": cid, "ent": ent, "witness": w, "g": g, "p": p, "b": b,
        "G0": G0, "G": Gi, "gscale": gscale, "ob": ob, "pts": pts,
        "period": period, "ec": ec, "code": code.decode("ascii"), "aut": aut,
        "Fc": Fc, "V": V, "E": E, "W": W,
        "site_ops": orbit.site_stabilizer(g, p),
        "detail": (f"IT({w['group']}) {g['international_short']} "
                   f"p=({', '.join(w['point'])}) c/a={b if b is not None else 'cubic'} "
                   f"G=diag({Gi[0][0]},{Gi[1][1]},{Gi[2][2]}) period={period} "
                   f"n_conv={ob['n_conventional']} T={ob['n_primitive']} "
                   f"site={ob['stabilizer_order']} dim={dim} f=({V},{E},{Fc}) "
                   f"p-vec {pvec_compact(ec['p_vector'])} aut={aut} W={W} "
                   f"nonsimple={ec['nonsimple_vertices']} "
                   f"cutoff_D2={ec['cutoff_D2']} 4rho2_G={4*ec['rho2']}"),
    }


# --------------------------------------------------------- V1 (generator)
def v1_generate(ctx):
    pts, P, G = ctx["pts"], ctx["period"], ctx["G"]
    n = len(pts)
    Bcols, detL = derive_lattice(pts, P)          # translations: metric-free
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
        bidx = base_index[tuple(x % P for x in q)]
        tj = type_of[bidx]
        v = lat_int(vsub(q, pts[type_reps[tj]]))
        assert v is not None, f"site {q} not L-congruent to its type rep"
        return v, tj

    # exact Gram cells for ALL T reps (rep 0 = the V0 cell)
    cells = [ctx["ec"] if r == 0 else clip_cell_gram(pts[r], pts, P, ctx["G0"])
             for r in type_reps]
    for e in cells:
        assert 4 * e["rho2"] <= e["cutoff_D2"]
        assert e["gram"] == G
        assert e["facet_count"] == ctx["Fc"]
        assert e["p_vector"] == ctx["ec"]["p_vector"]
        code, _ = canonical_code(e["facet_cycles"])
        assert code.decode("ascii") == ctx["code"], \
            "rep cell combinatorial type differs (congruence broken)"

    # V1b volume identity — crystal-basis measure, exact rational
    vols = [cell_volume_from_cycles(e) for e in cells]
    assert all(v == vols[0] for v in vols), "rep volumes differ"
    assert T * vols[0] == F(detL), "T*vol != detL"
    assert vols[0] == F(P**3, n), "vol != P^3/n"

    facets_per = []
    for e in cells:
        facets_per.append([(frozenset(e["vertices"][i] for i in cyc), q)
                           for cyc, q in zip(e["facet_cycles"], e["neighbors"])])

    # V1c full-facet pairing (affine, metric-free)
    Fc = ctx["Fc"]
    pairings = []
    for ti, e in enumerate(cells):
        c = e["center"]
        for fs, q in facets_per[ti]:
            lam, tj = id_of_site(q)
            delta = vsub(q, pts[type_reps[tj]])
            assert to_int_vec(mat_vec(Bf, lam)) == tuple(delta)
            hits = 0
            for fs2, q2 in facets_per[tj]:
                if tuple(q2[k] + delta[k] for k in range(3)) == c:
                    tv = frozenset(tuple(wv[k] + delta[k] for k in range(3))
                                   for wv in fs2)
                    if tv == fs:
                        hits += 1
            assert hits == 1, f"facet slot ({ti}) pairing count {hits} != 1"
            pairings.append({"rep": ti, "nbr_type": tj, "delta": list(delta),
                             "shared": [[str(x) for x in wv]
                                        for wv in sorted(fs)]})
    assert len(pairings) == T * Fc

    # V1d translate-completeness + interior disjointness in the G-norm.
    # Sites beyond the G-ball of radius 2 rho cannot meet the cell (triangle
    # inequality in the G-norm); every site inside it is checked.
    rho2 = cells[0]["rho2"]
    assert all(e["rho2"] == rho2 for e in cells), "rep circumradii differ"
    D2 = 4 * rho2
    ball_sizes = []
    for ti, e in enumerate(cells):
        c = e["center"]
        ball, Bb = candidates_near_gram(c, pts, P, G, D2)
        ball_sizes.append(len(ball))
        nbrset = set(e["neighbors"])
        assert nbrset <= set(ball), "facet neighbour beyond the 2rho G-ball"
        for r in ball:
            a, bb = metric.bisector(G, c, r)
            onv = []
            for wv in e["vertices"]:
                s = vdot(a, wv) - bb
                assert s <= 0, \
                    f"cell vertex strictly beyond G-bisector of in-ball site {r}"
                if s == 0:
                    onv.append(wv)
            if r not in nbrset and len(onv) >= 3:
                u0 = vsub(onv[1], onv[0])
                assert all(vcross(u0, vsub(wv, onv[0])) == (0, 0, 0)
                           for wv in onv[2:]), \
                    f"2-face contact with unlisted site {r}"

    cert = {
        "type_id": ctx["cid"], "T": T, "F": Fc, "detL": detL, "period": P,
        "n_sites_conventional": n,
        "gram": [[int(x) for x in row] for row in G],
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
           "vol": vols[0]}
    detail = (f"detL={detL} T={T} vol={vols[0]} T*vol={T*vols[0]} (crystal-"
              f"basis measure) slots={T*Fc} paired 1:1; disjointness G-ball "
              f"D2=4rho2={D2} (coord bound {Bb}), ball sizes "
              f"{min(ball_sizes)}..{max(ball_sizes)} sites/rep, all G-bisectors "
              f"weakly satisfied, no unlisted 2-face contact")
    return cert, lat, detail


# ------------------------------------------- V1 independent audit (Gram layer)
# Fresh code: own quadratic form / cross product, no metric.py, no exact_cell*.
# Certificate consumed as DATA only.  The affine part (facet scan, closed
# surface, Euler, volumes, full-facet pairing both sides, slot coverage) is
# g4_certify.v1_audit verbatim — it is metric-free and accepted.
def _q(G, u):
    return (u[0] * (G[0][0]*u[0] + G[0][1]*u[1] + G[0][2]*u[2])
            + u[1] * (G[1][0]*u[0] + G[1][1]*u[1] + G[1][2]*u[2])
            + u[2] * (G[2][0]*u[0] + G[2][1]*u[1] + G[2][2]*u[2]))


def _gv(G, u):
    return tuple(G[i][0]*u[0] + G[i][1]*u[1] + G[i][2]*u[2] for i in range(3))


def _x(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def _s(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])


def v1_audit_gram(cert):
    affine = G4C.v1_audit(cert)
    G = [[F(x) for x in row] for row in cert["gram"]]
    assert all(G[i][j] == G[j][i] for i in range(3) for j in range(3))
    reps = [[tuple(F(s) for s in v) for v in cell]
            for cell in cert["representatives"]]
    cen = [tuple(F(x) for x in c) for c in cert["rep_centers"]]
    n_eq = n_side = n_par = 0
    for pr in cert["pairings"]:
        ti, tj = pr["rep"], pr["nbr_type"]
        delta = tuple(F(int(x)) for x in pr["delta"])
        c1 = cen[ti]
        c2 = tuple(cen[tj][k] + delta[k] for k in range(3))
        assert c1 != c2
        shared = [tuple(F(s) for s in v) for v in pr["shared"]]
        for v in shared:                                   # on the G-bisector
            assert _q(G, _s(v, c1)) == _q(G, _s(v, c2)), \
                "audit: shared vertex not G-equidistant from the two centres"
            n_eq += 1
        for v in reps[ti]:                                 # Voronoi side
            assert _q(G, _s(v, c1)) <= _q(G, _s(v, c2)), \
                "audit: rep vertex G-closer to a paired neighbour centre"
            n_side += 1
        # supporting normal of the shared facet parallel to G (c2 - c1)
        nrm = None
        for a, b, c in itertools.combinations(shared, 3):
            nrm = _x(_s(b, a), _s(c, a))
            if nrm != (0, 0, 0):
                break
        assert nrm is not None and nrm != (0, 0, 0), "audit: degenerate facet"
        assert _x(nrm, _gv(G, _s(c2, c1))) == (0, 0, 0), \
            "audit: facet normal not parallel to G (r - c)"
        n_par += 1
    return (affine + f"; Gram layer: {n_eq} shared-vertex G-equidistance "
            f"checks, {n_side} vertex-side checks, {n_par} facet normals "
            f"parallel to G(r-c) — all exact")


# --------------------------------------------------------------------- V2
def _labelling(start, rot, n):
    label = {start[0]: 0}; order = [start[0]]; entry = {start[0]: start}; code = []
    i = 0
    while i < len(order):
        x = order[i]; i += 1
        d0 = entry[x]; d = d0; row = []
        while True:
            w = d[1]
            if w not in label:
                label[w] = len(order); order.append(w); entry[w] = (w, x)
            row.append(label[w]); d = rot[d]
            if d == d0:
                break
        code.append(tuple(row))
    assert len(order) == n
    return tuple(code), label


def map_automorphisms(face_cycles):
    """All map automorphisms as (vertex permutation, orientation-preserving)
    — c2_isometry.py pattern on the canonical-code machinery."""
    sigma, sigma_inv = rotation_system(face_cycles)
    n = len({v for cyc in face_cycles for v in cyc})
    best = None; hits = []
    for rot, pres in ((sigma, True), (sigma_inv, False)):
        for d in sigma:
            c, lab = _labelling(d, rot, n)
            if best is None or c < best:
                best, hits = c, [(lab, pres)]
            elif c == best:
                hits.append((lab, pres))
    lab0, pres0 = hits[0]
    auts = []
    for lab, pres in hits:
        inv = {l: v for v, l in lab.items()}
        perm = {v: inv[lab0[v]] for v in lab0}
        auts.append((perm, pres == pres0))
    return auts


def solve3(M, b):
    A = [list(map(F, M[i])) + [F(b[i])] for i in range(3)]
    for c in range(3):
        piv = next(i for i in range(c, 3) if A[i][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for i in range(3):
            if i != c and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * bb for a, bb in zip(A[i], A[c])]
    return [A[i][3] for i in range(3)]


def isometry_from_perm_gram(verts, perm, G):
    """Affine map x -> A x + t realising the permutation; asserts A^T G A = G."""
    n = len(verts)
    i0 = 0
    for i1, i2, i3 in itertools.combinations(range(1, n), 3):
        e = [vsub(verts[i], verts[i0]) for i in (i1, i2, i3)]
        if det3(*e) != 0:
            break
    src = [vsub(verts[i], verts[i0]) for i in (i1, i2, i3)]
    dst = [vsub(verts[perm[i]], verts[perm[i0]]) for i in (i1, i2, i3)]
    A = [solve3([list(src[j]) for j in range(3)], [dst[j][r] for j in range(3)])
         for r in range(3)]
    t = [verts[perm[i0]][k] - sum(A[k][j] * verts[i0][j] for j in range(3))
         for k in range(3)]
    AtGA = [[sum(A[k][i] * G[k][l] * A[l][j] for k in range(3) for l in range(3))
             for j in range(3)] for i in range(3)]
    assert AtGA == [[F(G[i][j]) for j in range(3)] for i in range(3)], \
        "G-distance-preserving permutation gave a non-G-orthogonal A (!)"
    for i in range(n):
        img = tuple(sum(A[k][j] * verts[i][j] for j in range(3)) + t[k]
                    for k in range(3))
        assert img == tuple(verts[perm[i]]), "affine map does not realise perm"
    return tuple(tuple(x for x in row) for row in A), tuple(t), det3(*A)


def cell_stabilizer_gram(verts, G):
    """Second derivation: all G-orthogonal maps about the vertex centroid
    preserving the vertex set (Gram-triple matching in the G-inner product)."""
    npts = len(verts)
    cen = tuple(sum(col) / npts for col in zip(*verts))
    cent = [vsub(v, cen) for v in verts]
    centset = set(cent)
    b1 = cent[0]
    b2 = next(q for q in cent[1:] if vcross(b1, q) != (0, 0, 0))
    b3 = next(q for q in cent if det3(b1, b2, q) != 0)
    Gr = [[gform(G, a, b) for b in (b1, b2, b3)] for a in (b1, b2, b3)]
    Bm = [[b1[i], b2[i], b3[i]] for i in range(3)]
    Binv = mat_inv(Bm)
    stab = set()
    for w1 in cent:
        if gq(G, w1) != Gr[0][0]:
            continue
        for w2 in cent:
            if gq(G, w2) != Gr[1][1] or gform(G, w1, w2) != Gr[0][1]:
                continue
            for w3 in cent:
                if gq(G, w3) != Gr[2][2] or gform(G, w1, w3) != Gr[0][2] \
                        or gform(G, w2, w3) != Gr[1][2]:
                    continue
                Wm = [[w1[i], w2[i], w3[i]] for i in range(3)]
                A = mat_mul(Wm, Binv)
                AtGA = [[sum(A[k][i] * G[k][l] * A[l][j]
                             for k in range(3) for l in range(3))
                         for j in range(3)] for i in range(3)]
                if AtGA != [[F(G[i][j]) for j in range(3)] for i in range(3)]:
                    continue
                img = set(tuple(sum(A[i][j]*q[j] for j in range(3))
                                for i in range(3)) for q in cent)
                if img == centset:
                    stab.add(tuple(tuple(F(x) for x in row) for row in A))
    return stab


def bravais_point_group_gram(Bcols, G):
    """All U in GL3(Z) with U^T G_L U == G_L, G_L = B^T G B (Bravais point
    group of the ACTUAL lattice in the G metric).  Coefficient bound: column j
    of U is the coefficient vector u of a lattice vector w with |w|_G^2 =
    G_L[j][j]; u_i = <G_L^-1 e_i, u>_{G_L}, so u_i^2 <= (G_L^-1)_ii |w|^2."""
    Bf = [[F(Bcols[i][j]) for j in range(3)] for i in range(3)]
    GL = [[sum(Bf[k][i] * G[k][l] * Bf[l][j] for k in range(3) for l in range(3))
           for j in range(3)] for i in range(3)]
    GLinv = mat_inv(GL)
    nmax = max(GL[i][i] for i in range(3))
    bnd = [isqrt_frac_floor(GLinv[i][i] * nmax) for i in range(3)]
    cand = {i: [] for i in range(3)}
    for u in itertools.product(*(range(-bnd[i], bnd[i]+1) for i in range(3))):
        q = gq(GL, u)
        for i in range(3):
            if q == GL[i][i]:
                cand[i].append(u)
    group = []
    for u1 in cand[0]:
        for u2 in cand[1]:
            if gform(GL, u1, u2) != GL[0][1]:
                continue
            for u3 in cand[2]:
                if gform(GL, u1, u3) != GL[0][2] or gform(GL, u2, u3) != GL[1][2]:
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
        RtGR = [[sum(Rm[k][i] * G[k][l] * Rm[l][j] for k in range(3)
                     for l in range(3)) for j in range(3)] for i in range(3)]
        assert RtGR == [[F(G[i][j]) for j in range(3)] for i in range(3)], \
            "embedded Bravais op not G-orthogonal (impossible if G_L preserved)"
        embedded.append((U, tuple(tuple(x for x in row) for row in Rm)))
    return embedded


def v2_symmetry(ctx, lat):
    G = ctx["G"]
    ec = ctx["ec"]
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    site = tuple(F(x) for x in ec["center"])
    nv = len(verts)
    d2 = {(i, j): gq(G, vsub(verts[i], verts[j]))
          for i in range(nv) for j in range(i + 1, nv)}
    auts = map_automorphisms(ec["facet_cycles"])
    assert len(auts) == ctx["aut"], "map automorphism count != aut"
    iso = []
    for perm, pres in auts:
        if all(d2[(i, j)] == d2[tuple(sorted((perm[i], perm[j])))]
               for (i, j) in d2):
            A, t, det = isometry_from_perm_gram(verts, perm, G)
            fixes = tuple(sum(A[k][j] * site[j] for j in range(3)) + t[k]
                          for k in range(3)) == site
            assert (det == 1) == pres, "orientation vs det disagree"
            iso.append({"A": A, "t": t, "det": det, "fixes_site": fixes})
    n_iso = len(iso)
    n_proper = sum(1 for x in iso if x["det"] == 1)
    n_fix = sum(1 for x in iso if x["fixes_site"])
    # second derivation (G-Gram-triple about the centroid) must agree
    stab2 = cell_stabilizer_gram(verts, G)
    assert len(stab2) == n_iso and stab2 == {x["A"] for x in iso}, \
        "Gram-triple stabilizer != map-automorphism isometries"
    # site symmetry (frozen ops) inside the site-fixing isometries
    site_R = {tuple(tuple(F(x) for x in row) for row in Rm)
              for Rm, _ in ctx["site_ops"]}
    assert len(site_R) == len(ctx["site_ops"])
    fix_A = {x["A"] for x in iso if x["fixes_site"]}
    assert site_R <= fix_A, "site symmetry not contained in Isom_fix_site"
    n_site, n_aut = len(site_R), ctx["aut"]
    assert n_fix % n_site == 0 and n_iso % n_fix == 0 and n_aut % n_iso == 0
    chiral = (n_iso == n_proper)

    brav = bravais_point_group_gram(lat["Bcols"], G)
    # honeycomb point group H/L: Bravais-embedded R with a translation c
    # carrying the site set to itself (complete: any honeycomb symmetry
    # preserves S hence L, so its linear part is in the Bravais embedding, and
    # it maps pts[0] to a site, so c is one of the tried anchors mod P Z^3).
    pts, P = ctx["pts"], ctx["period"]
    siteset = {tuple(F(x) for x in q) for q in pts}
    ops_geo = []
    for U, Rm in brav:
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
    ops_geo.sort(key=lambda t: (t[0] != ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                t[0]))
    T = lat["T"]
    n_ops = len(ops_geo)
    assert n_ops % T == 0, "H/L not transitive-compatible"
    h_cell = n_ops // T
    assert h_cell % n_site == 0 and n_fix % h_cell == 0
    full_is_G = (n_ops == T * n_site)
    n_ops_improper = sum(1 for U, _, _ in ops_geo if mat_det(U) == -1)
    G4C_all_sp = all(G4C.is_signed_perm([[x for x in row] for row in Rm])
                     for _, Rm in brav)
    detail = (f"site={n_site}, Isom_fix_site={n_fix}, Isom(solid)={n_iso} "
              f"(Isom+={n_proper}, improper={n_iso-n_proper}; solid "
              f"{'CHIRAL' if chiral else 'achiral'}), aut_comb={n_aut}; chain "
              f"site<=Isom_fix (linear parts) contained, divisibility "
              f"{n_site}|{n_fix}|{n_iso}|{n_aut} holds; Gram-triple re-derivation "
              f"agrees; Bravais point group of L in G: order {len(brav)} "
              f"(embedded ops {'all' if G4C_all_sp else 'NOT all'} signed "
              f"perms); honeycomb point group |H/L|={n_ops} "
              f"({n_ops_improper} improper) vs T*|site|={T*n_site}: full symmetry "
              f"group of the honeycomb {'IS exactly G' if full_is_G else 'is LARGER than G'} "
              f"(|H_cell|={h_cell})")
    return {"n_site": n_site, "n_fix": n_fix, "n_iso": n_iso,
            "n_proper": n_proper, "chiral": chiral, "n_aut": n_aut,
            "n_brav": len(brav), "brav": brav, "ops_geo": ops_geo,
            "n_ops": n_ops, "n_ops_improper": n_ops_improper,
            "h_cell": h_cell, "full_is_G": full_is_G, "iso": iso,
            "detail": detail}


# --------------------------------------------------------------------- V3
def v3_tables_burnside(ctx, lat, sym, deadline, prefix="g4p2_tables_"):
    pts, P = ctx["pts"], ctx["period"]
    T, Fc = lat["T"], ctx["Fc"]
    Bf, Binv = lat["Bf"], lat["Binv"]
    type_reps, cells = lat["type_reps"], lat["cells"]
    id_of_site = lat["id_of_site"]
    assert T <= 127, "enumerate.cpp limit T<=127"

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

    ops_geo = sym["ops_geo"]
    ops_id = [op_idspace(Rm, c) for _, Rm, c in ops_geo]
    dets = [mat_det(U) for U, _, _ in ops_geo]

    def opkey(A, per):
        return (tuple(map(tuple, A)), tuple(tj for _, tj in per),
                tuple(tuple(per[t][0][i] - per[0][0][i] for i in range(3))
                      for t in range(T)))

    keyset = {opkey(A, p) for A, p in ops_id}
    assert len(keyset) == len(ops_id), "duplicate ops mod lattice translation"
    assert ops_id[0][0] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]] and \
        all(p[1] == t for t, p in enumerate(ops_id[0][1])) and \
        all(p[0] == ops_id[0][1][0][0] for p in ops_id[0][1]), "identity first"

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
    # hands of the translation classes (det of any op carrying class 0 to t)
    hand, consistent = {}, True
    for (A, per), d in zip(ops_id, dets):
        t = per[0][1]
        if t in hand and hand[t] != d:
            consistent = False
        hand.setdefault(t, d)
    assert len(hand) == T, "ops not transitive on classes"
    n_other_hand = sum(1 for v in hand.values() if v == -1)

    n_proper = sum(1 for d in dets if d == 1)
    tables = {
        "T": T, "nbr": nbr_table,
        "ops": [{"A": A, "map": per} for A, per in ops_id],
        "proper_ops": [{"A": A, "map": per}
                       for (A, per), d in zip(ops_id, dets) if d == 1],
        "lattice_basis": [[lat["Bcols"][i][j] for i in range(3)]
                          for j in range(3)],
        "gram": [[int(x) for x in row] for row in ctx["G"]],
        "detL": lat["detL"], "cell_volume_crystal_basis": str(lat["vol"]),
        "n_proper": n_proper, "n_improper": len(ops_id) - n_proper,
        "facet_signature": list(ctx["ec"]["p_vector"]),
        "note": ("tables are metric-independent adjacency data; the Gram "
                 "matrix is recorded for provenance only"),
    }
    tables_path = os.path.join(HERE, f"{prefix}{ctx['cid']}.json")
    json.dump(tables, open(tables_path, "w"), indent=1)
    maxd = max(abs(v) for row in nbr_table for dv, _ in row for v in dv)
    base = (f"tables T={T} nbrs={Fc} |ops|={len(ops_id)} ({n_proper} proper, "
            f"{len(ops_id)-n_proper} improper; T*|site|={T*sym['n_site']}), "
            f"identity+closure exact; hands: "
            f"{('n/a (achiral solid)' if not sym['chiral'] else f'{n_other_hand} of {T} classes of the other hand') if consistent else 'inconsistent (achiral solid)'}")

    if time.time() > deadline:
        return {"deferred": True, "counts": None, "indep": None,
                "detail": f"TIMEOUT-DEFERRED before enumeration: {base}"}

    txt = os.path.join(HERE, f"{prefix}{ctx['cid']}.txt")
    subprocess.run([PYTHON, EXPORT_TABLES, tables_path, txt, "ops"],
                   check=True, capture_output=True)
    r = subprocess.run([ENUM_BIN, txt, str(N_ENUM)], check=True,
                       capture_output=True, text=True, timeout=STAGE_CAP_S)
    counts, seen_hdr = {}, False
    for line in r.stdout.splitlines():
        if line.strip() == "n fixed free":
            seen_hdr = True
            continue
        if seen_hdr and line.split():
            nn, fx, fr = line.split()
            counts[int(nn)] = (int(fx), int(fr))
    assert len(counts) == N_ENUM, "enumerator output parse failure"
    free_s = ",".join(str(counts[n][1]) for n in range(1, N_ENUM+1))
    fixed_s = ",".join(str(counts[n][0]) for n in range(1, N_ENUM+1))
    rb = subprocess.run([PYTHON, BURNSIDE, ctx["cid"], tables_path,
                         str(N_ENUM), free_s, fixed_s],
                        capture_output=True, text=True, timeout=STAGE_CAP_S)
    assert rb.returncode == 0, f"burnside_generic crashed: {rb.stderr[-400:]}"
    assert "ALL PASS" in rb.stdout, f"BURNSIDE FAILED:\n{rb.stdout}"

    # independent enumerator (dual-implementation bar), n <= N_INDEP capped
    n_ind = min(N_INDEP, 30 // maxd + 1)            # its coordinate field
    ind_json = os.path.join(HERE, f"{prefix}{ctx['cid']}_indep.json")
    t_i = time.time()
    try:
        ri = subprocess.run([PYTHON, INDEP, tables_path, "--n", str(n_ind),
                             "--json", ind_json, "--expect-fixed", fixed_s,
                             "--expect-free", free_s, "--wall-cap",
                             str(INDEP_CAP_S * 0.6)]
                            + ([] if INDEP_WORKERS is None
                               else ["--workers", str(INDEP_WORKERS)]),
                            capture_output=True, text=True, timeout=INDEP_CAP_S)
        out, timed_out, rc = ri.stdout, False, ri.returncode
    except subprocess.TimeoutExpired as exc:
        out = (exc.stdout or b"").decode() if isinstance(exc.stdout, bytes) \
            else (exc.stdout or "")
        timed_out, rc = True, None
    t_i = time.time() - t_i
    ind_rows = {}
    for line in out.splitlines():
        if line.startswith("n=") and "fixed=" in line:
            parts = dict(kv.split("=", 1) for kv in line.split()
                         if "=" in kv and not kv.startswith("burnside"))
            ind_rows[int(parts["n"])] = (int(parts["fixed"]), int(parts["free"]),
                                         int(parts["onesided"]),
                                         "MISMATCH" not in line
                                         and "BURNSIDE-FAIL" not in line)
    reached = max(ind_rows) if ind_rows else 0
    assert reached >= N_ENUM, \
        f"independent enumerator did not reach n={N_ENUM} (reached {reached})"
    for n in range(1, N_ENUM + 1):
        assert ind_rows[n][0] == counts[n][0] and ind_rows[n][1] == counts[n][1] \
            and ind_rows[n][3], f"DUAL-IMPLEMENTATION MISMATCH at n={n}"
    assert all(ind_rows[n][3] for n in ind_rows), "independent Burnside failed"
    if not timed_out:
        assert rc == 0, f"independent enumerator exit {rc}:\n{out[-600:]}"
    indep = {"reached": reached, "target": n_ind, "timed_out": timed_out,
             "wall": t_i, "rows": ind_rows,
             "capped_by_field": n_ind < N_INDEP}
    detail = (f"{base}; banked enumerate n<={N_ENUM}: "
              f"fixed={[counts[n][0] for n in range(1, N_ENUM+1)]}, "
              f"free={[counts[n][1] for n in range(1, N_ENUM+1)]}; "
              f"burnside_generic ALL PASS n<={N_ENUM}; INDEPENDENT enumerator "
              f"(verify_counts_independent.py) reached n={reached}"
              f"{' (target '+str(n_ind)+', 15-min cap hit)' if timed_out else ''}"
              f"{' (n capped by its coordinate field)' if n_ind < N_INDEP else ''}"
              f": fixed={[ind_rows[n][0] for n in sorted(ind_rows)]}, "
              f"free={[ind_rows[n][1] for n in sorted(ind_rows)]}, "
              f"one-sided={[ind_rows[n][2] for n in sorted(ind_rows)]}, "
              f"n<={N_ENUM} identical to banked, its own Burnside (all + "
              f"proper) ok at every n, {t_i:.0f}s")
    return {"deferred": False, "counts": counts, "indep": indep,
            "n_ops": len(ops_id), "n_proper": n_proper, "hand_consistent":
            consistent, "n_other_hand": n_other_hand, "detail": detail}


# ------------------------------------------------------------------ driver
def run_ladder(cid, ent, groups, w, say, deadline_total, prefix="g4p2_tables_"):
    t_c0 = time.time()
    stages = []
    res = {"cid": cid, "ent": ent, "witness": w, "stages": stages,
           "ctx": None, "lat": None, "sym": None, "v3": None, "cert": None}

    def stage(name, fn):
        t0 = time.time()
        try:
            out = fn()
            dt = time.time() - t0
            verdict = "DEFERRED" if isinstance(out, dict) \
                and out.get("deferred") else "PASS"
            if dt > STAGE_CAP_S and verdict == "PASS":
                verdict = "PASS (over stage cap)"
            detail = out["detail"] if isinstance(out, dict) and "detail" in out \
                else out if isinstance(out, str) else ""
            stages.append({"name": name, "verdict": verdict, "detail": detail,
                           "t": dt})
            say(f"  {name}: {verdict} ({dt:.1f}s) {detail[:120]}")
            return out
        except Exception:
            dt = time.time() - t0
            tb = traceback.format_exc().strip().splitlines()[-1]
            stages.append({"name": name, "verdict": "FAIL", "detail": tb,
                           "t": dt})
            say(f"  {name}: FAIL ({dt:.1f}s) {tb}")
            raise

    say(f"[{cid}] f={tuple(ent['f_vector'])} p={pvec_compact(ent['p_vector'])} "
        f"aut={ent['aut_order']} witness IT({w['group']}) point "
        f"({', '.join(w['point'])}) c/a={w.get('b')}")
    try:
        ctx = stage("V0 exact re-derivation (Gram chain)",
                    lambda: v0_rederive(cid, ent, groups, w))
        res["ctx"] = ctx
        cl = stage("V1 tiling certificate in the G-norm (generator)",
                   lambda: dict(zip(("cert", "lat", "detail"), v1_generate(ctx))))
        res["cert"], res["lat"] = cl["cert"], cl["lat"]
        stage("V1 independent adapted audit (affine + Gram layer)",
              lambda: v1_audit_gram(json.loads(json.dumps(cl["cert"]))))
        sym = stage("V2 symmetry certification (G-isometries)",
                    lambda: v2_symmetry(ctx, cl["lat"]))
        res["sym"] = sym
        deadline = min(time.time() + STAGE_CAP_S, deadline_total)
        res["v3"] = stage("V3 Burnside identity (banked + independent)",
                          lambda: v3_tables_burnside(ctx, cl["lat"], sym,
                                                     deadline, prefix))
    except Exception:
        pass
    res["elapsed"] = time.time() - t_c0
    return res


def cubic_path_control(groups, say):
    """ACCEPTED cubic ladder (g4_certify functions) on the Im-3m #229 origin
    orbit = truncated octahedron.  Returns the reference numbers."""
    from sweep_voronoi import sweep
    from exact_cell import clip_cell
    g = groups[229]
    p = (F(0), F(0), F(0))
    ob = orbit.orbit(g, p)
    pts, period = orbit.scale_orbit(ob["points"])
    cells_f = sweep(pts, period, W=2)
    ec = clip_cell(pts[0], pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2
    code, aut = canonical_code(ec["facet_cycles"])
    Fc, V = ec["facet_count"], ec["n_vertices"]
    E = sum(len(c) for c in ec["facet_cycles"]) // 2
    ctx = {"cid": "ctrl_cubicpath_truncoct", "g": g, "p": p, "ob": ob,
           "pts": pts, "period": period, "ec": ec,
           "code": code.decode("ascii"), "aut": aut, "Fc": Fc, "V": V, "E": E,
           "site_ops": orbit.site_stabilizer(g, p)}
    f0 = cells_f[0]
    assert f0["facet_count"] == Fc and f0["p_vector"] == ec["p_vector"]
    cert, lat, d1 = G4C.v1_generate(ctx)
    G4C.v1_audit(json.loads(json.dumps(cert)))
    sym = G4C.v2_symmetry(ctx, lat)
    v3 = G4C.v3_tables_burnside(ctx, lat, sym, time.time() + STAGE_CAP_S)
    # move the cubic function's artifacts under the phase-2 control prefix
    for ext in (".json", ".txt"):
        src = os.path.join(HERE, f"g4_tables_{ctx['cid']}{ext}")
        dst = os.path.join(HERE, f"g4p2_control_cubicpath_tables{ext}")
        os.replace(src, dst)
    ref = {"code": ctx["code"], "f": (V, E, Fc), "p": tuple(ec["p_vector"]),
           "aut": aut, "T": lat["T"], "detL": lat["detL"], "vol": str(lat["vol"]),
           "slots": lat["T"] * Fc, "site": sym["n_site"],
           "stab_geo": sym["n_geo"], "brav": sym["n_brav"],
           "n_ops": v3["n_ops"], "n_proper": v3["n_proper"],
           "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
           "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)]}
    say(f"  cubic path (g4_certify functions, Im-3m #229 origin): {ref}")
    return ref


def sanity_gate(groups, store, seeds, say):
    say("== SANITY GATE 1: truncated octahedron, cubic ladder vs Gram ladder ==")
    t0 = time.time()
    ref = cubic_path_control(groups, say)
    seed = next(e for e in seeds if e["name"] == "truncated_octahedron")
    assert ref["code"] == seed["canon_code"] and ref["aut"] == 48
    ent = {"canon_code": seed["canon_code"], "f_vector": seed["f_vector"],
           "p_vector": seed["p_vector"], "aut_order": seed["aut_order"]}
    w = {"group": 139, "point": ["0", "0", "0"], "b": "1"}
    r = run_ladder("ctrl_truncoct_I4mmm_ca1", ent, groups, w, say,
                   time.time() + STAGE_CAP_S, prefix="g4p2_control_")
    assert all(s["verdict"] == "PASS" for s in r["stages"]) and \
        len(r["stages"]) == 5, "Gram ladder failed on the cubic control"
    ctx, lat, sym, v3 = r["ctx"], r["lat"], r["sym"], r["v3"]
    got = {"code": ctx["code"], "f": (ctx["V"], ctx["E"], ctx["Fc"]),
           "p": tuple(ctx["ec"]["p_vector"]), "aut": ctx["aut"], "T": lat["T"],
           "detL": lat["detL"], "vol": str(lat["vol"]), "slots": lat["T"]*ctx["Fc"],
           "site": sym["n_site"], "stab_geo": sym["n_fix"], "brav": sym["n_brav"],
           "n_ops": v3["n_ops"], "n_proper": v3["n_proper"],
           "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
           "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)]}
    # the SITE symmetry is the one number that legitimately differs: the
    # origin of I4/mmm has site symmetry 4/mmm (16) while the honeycomb's full
    # group is Im-3m (site 48) -- exactly what the |H/L| vs T*|site| check
    # must detect ("full symmetry group LARGER than G").
    diffs = {k: (ref[k], got[k]) for k in ref if k != "site" and ref[k] != got[k]}
    assert not diffs, f"SANITY GATE 1 FAILED: {diffs}"
    assert ref["site"] == 48 and got["site"] == 16, (ref["site"], got["site"])
    assert ctx["G"] == ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    assert ctx["pts"] == [(0, 0, 0), (6, 6, 6)] and ctx["period"] == 12
    assert sym["n_iso"] == 48 and (not sym["full_is_G"]) and sym["n_ops"] == 48
    line1 = (f"GATE 1 PASS: I4/mmm #139 origin orbit at c/a=1 (G=I, same "
             f"integer sites {ctx['pts']} period 12 as Im-3m #229) through the "
             f"Gram ladder == accepted cubic ladder on Im-3m #229 origin: all "
             f"{len(ref)-1} compared numbers identical (code, f, p, aut, T, "
             f"detL, vol, slots, geometric stabilizer 48, Bravais 48, |ops| 48, "
             f"proper 24, fixed/free n<=4): {got}; the one legitimate "
             f"difference is the SITE symmetry (Im-3m origin 48 vs I4/mmm origin "
             f"16) and the ladder's |H/L|={sym['n_ops']} vs T*|site|="
             f"{sym['n_site']} check correctly reports the honeycomb's full "
             f"group as LARGER than I4/mmm (it is Im-3m); Isom(solid)="
             f"{sym['n_iso']} (Isom+={sym['n_proper']}); independent enumerator "
             f"reached n={v3['indep']['reached']} ({time.time()-t0:.0f}s)")
    say(line1)

    say("== SANITY GATE 2: banked cubic G4 row ceb70631e274e727 via Gram ladder ==")
    t0 = time.time()
    p1 = json.load(open(STORE_P1))["types"]["ceb70631e274e727"]
    w2 = dict(p1["first_witness"]); w2["b"] = None
    exp = {"T": 8, "detL": 1728, "vol": "216", "site": 3, "stab_geo": 3,
           "aut": 3, "brav": 48, "n_ops": 24, "n_proper": 24,
           "fixed": [8, 88, 1384, 25064], "free": [1, 5, 59, 1065]}
    r2 = run_ladder("ctrl_ceb70631e274e727_cubic", p1, groups, w2, say,
                    time.time() + STAGE_CAP_S, prefix="g4p2_control_")
    assert all(s["verdict"] == "PASS" for s in r2["stages"]) and \
        len(r2["stages"]) == 5, "Gram ladder failed on banked cubic row"
    ctx, lat, sym, v3 = r2["ctx"], r2["lat"], r2["sym"], r2["v3"]
    got2 = {"T": lat["T"], "detL": lat["detL"], "vol": str(lat["vol"]),
            "site": sym["n_site"], "stab_geo": sym["n_fix"], "aut": ctx["aut"],
            "brav": sym["n_brav"], "n_ops": v3["n_ops"],
            "n_proper": v3["n_proper"],
            "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
            "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)]}
    diffs = {k: (exp[k], got2[k]) for k in exp if exp[k] != got2[k]}
    assert not diffs, f"SANITY GATE 2 FAILED: {diffs}"
    line2 = (f"GATE 2 PASS: ceb70631e274e727 IT(212) witness "
             f"(1/12,1/12,1/12) through the Gram ladder with G=I reproduces "
             f"G4_RESULTS.md exactly: {got2}; Isom(solid)={sym['n_iso']}, "
             f"|H/L|={sym['n_ops']}=T*|site|={lat['T']*sym['n_site']}, "
             f"independent enumerator reached n={v3['indep']['reached']} "
             f"({time.time()-t0:.0f}s)")
    say(line2)
    return [line1, line2], [r, r2]


# --------------------------------------------------------------- results
def write_results(gate_lines, results, total_s, snapshot):
    L = ["# G4 certificate results — PHASE 2 (tetragonal, Gram metric), "
         "V0-V3 ladder (2026-09-04)", "",
         "Gate: `../ANCHORS.md` G4 (paper-I-standard ladder V0-V3, "
         "`../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3) applied through the "
         "accepted Gram chain (`phase2/metric.py`, "
         "`phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`, G2b). "
         "Generator: `g4_certify_gram.py` (this run; sibling of the accepted "
         "cubic `g4_certify.py`, which is unmodified and whose metric-"
         "independent pieces — exact vector bits, coordinate-space fan volume, "
         "the independent affine audit `v1_audit`/`_a_*`, banked V3 tool "
         "paths — are imported). Inputs: `phase2_types.json` stored witnesses "
         "(the 14 collision-screen survivors of "
         "`COLLISION_PHASE2_RESULTS.md`; #8 `cd4fb52572edcb73` reframed and "
         "excluded), frozen G1 `spacegroups.json`. V3 uses the banked "
         "`export_tables.py` + compiled `enumerate` + `burnside_generic.py` "
         "(POLYFORMS_II) and then the INDEPENDENT "
         "`../publication/verify_counts_independent.py` (dual-implementation "
         "bar, n<=5 under a 15-min cap).", "",
         "**METRIC CONVENTIONS.** Sites/vertices in the ITA conventional "
         "(crystal) basis of the frozen ops, integer-scaled by PERIOD; metric "
         "= integer Gram G = diag(q^2, q^2, p^2) for c/a = p/q. All distances "
         "are G-norms; bisectors 2(r-c)^T G x = r^T G r - c^T G c; the cutoff "
         "4 rho^2 <= D^2 holds in the G-norm with the candidate block proven "
         "complete by |x_i| <= D sqrt((G^-1)_ii). **Volumes are crystal-basis "
         "(coordinate-space) measures**; the Euclidean volume is that times "
         "the SAME factor sqrt(det G)/q^3 for the cell, the lattice covolume "
         "and the torus, so T * vol(cell) = covol(L) = detL is an exact-"
         "rational identity in the crystal basis, equivalent to the Euclidean "
         "one. Facets and full-facet pairings are affine (metric-free); the "
         "metric enters the tiling certificate through the Voronoi bisector "
         "claims, verified in the G-norm by the generator (V1d) and re-verified "
         "by the audit's fresh Gram layer.", "",
         "**V3 tables are metric-independent adjacency data** (which cells "
         "share a facet; point ops mod L acting on cell IDs) — stated once; "
         "the metric has already done its work in V1/V2.", "",
         f"**LANGUAGE (stated once): G4 passing does NOT establish novelty. "
         f"Every type below remains \"not matched against the catalog "
         f"snapshot of {snapshot}\"; G5 is separate and has not closed. Kill "
         f"criteria were live (facet count > 38 asserts; none hit).**", "",
         "## Sanity gate (cubic control, run first)", ""]
    for g in gate_lines:
        L.append(f"- {g}")
    L.append("")
    allpass = True
    summary, isoms, counts_rows, deferrals = [], [], [], []
    for r in results:
        cid, ent, w = r["cid"], r["ent"], r["witness"]
        rank = RANK_OF.get(cid, "?")
        L.append(f"## #{rank} `{cid}` — IT({w['group']}) "
                 f"{ent['first_witness']['group_symbol']}, "
                 f"f={tuple(ent['f_vector'])}, p={pvec_compact(ent['p_vector'])}, "
                 f"aut={ent['aut_order']}")
        L.append("")
        if cid in LABEL:
            L.append(f"**LABEL: {LABEL[cid]}.**")
            L.append("")
        L.append(f"Witness point ({', '.join(w['point'])}), c/a = {w['b']}, "
                 f"site stabilizer {w['stabilizer_order']}, orbit "
                 f"{w['orbit_conventional']} conventional / "
                 f"{w['orbit_primitive']} primitive, stratum dim "
                 f"{w['stratum_dim']}. Candidate wall time {r['elapsed']:.1f}s.")
        L.append("")
        L.append("| stage | verdict | wall | key numbers |")
        L.append("|---|---|---|---|")
        verdicts = []
        for s in r["stages"]:
            allpass &= s["verdict"] == "PASS"
            verdicts.append(s["verdict"])
            L.append(f"| {s['name']} | **{s['verdict']}** | {s['t']:.1f}s | "
                     f"{s['detail']} |")
        done = {s["name"].split()[0] for s in r["stages"]}
        for missing in ("V0", "V1", "V2", "V3"):
            if missing not in done:
                allpass = False
                verdicts.append(f"{missing} NOT REACHED")
                L.append(f"| {missing} | **NOT REACHED** | — | quarantined "
                         f"downstream of the failure above |")
        L.append("")
        sy, v3 = r["sym"], r["v3"]
        if sy is not None:
            L.append(f"Symmetry reconciliation: site symmetry {sy['n_site']} "
                     f"<= Isom_fix_site {sy['n_fix']} <= Isom(solid) "
                     f"{sy['n_iso']} (Isom+ {sy['n_proper']}, solid "
                     f"{'chiral' if sy['chiral'] else 'achiral'}) <= "
                     f"combinatorial aut {sy['n_aut']} (containment + "
                     f"divisibility verified exactly; Gram-triple re-derivation "
                     f"agrees). Bravais point group of the actual lattice in G: "
                     f"order {sy['n_brav']}. Honeycomb point group |H/L| = "
                     f"{sy['n_ops']} ({sy['n_ops_improper']} improper) vs "
                     f"T*|site| = {r['lat']['T']*sy['n_site']}: the full "
                     f"symmetry group of the honeycomb "
                     f"{'IS exactly the generating group G' if sy['full_is_G'] else 'is LARGER than G'}.")
            L.append("")
            isoms.append((rank, cid, w["group"], sy["n_site"], sy["n_fix"],
                          sy["n_iso"], sy["n_proper"], sy["chiral"],
                          sy["n_aut"], sy["n_ops"], r["lat"]["T"],
                          sy["full_is_G"]))
        if v3 is not None and v3.get("counts"):
            ind = v3["indep"]
            counts_rows.append((rank, cid, v3["counts"], ind))
            if ind["reached"] < N_INDEP:
                deferrals.append(f"#{rank} `{cid}`: independent enumerator "
                                 f"reached n={ind['reached']} < {N_INDEP} "
                                 f"({'15-min cap' if ind['timed_out'] else 'coordinate-field cap'})")
        elif v3 is not None and v3.get("deferred"):
            deferrals.append(f"#{rank} `{cid}`: V3 TIMEOUT-DEFERRED")
        for s in r["stages"]:
            if s["verdict"] == "FAIL":
                deferrals.append(f"#{rank} `{cid}`: {s['name']} FAIL — {s['detail']}")
        summary.append((rank, cid, w["group"], tuple(ent["f_vector"]), verdicts))

    L.append("## Per-cell verdict table")
    L.append("")
    L.append("| # | type | IT | c/a | f | V0 | V1 gen | V1 audit | V2 | V3 | "
             "Burnside identity | open/wall (carried over) | wall |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for (rank, cid, grp, fv, vd), r in zip(summary, results):
        vd = (vd + ["—"] * 5)[:5]
        v3 = r["v3"]
        if v3 is not None and v3.get("counts"):
            burn = (f"PASS banked n<={N_ENUM} + independent n<="
                    f"{v3['indep']['reached']} (all + proper)")
        else:
            burn = "not reached"
        L.append(f"| {rank} | `{cid}` | {grp} | {r['witness'].get('b')} | {fv} | "
                 + " | ".join(vd) + f" | {burn} | "
                 f"{OPEN_WALL.get(cid, 'n/a')} | {r['elapsed']:.0f}s |")
    L.append("")
    L.append("Notes: (i) `e0d18e5ea938d649` (#6) is witnessed at c/a = 1, where "
             "the BCT lattice of I-42d is metrically cubic (BCC) — its Bravais "
             "point group in G is therefore 48, not 16; the honeycomb point "
             "group is still |H/L| = 8 = T*|site| (the SITE SET, not the "
             "lattice, decides), so its full symmetry group is I-42d. The type "
             "also occurs at c/a in {55/64, 7/8, 5/4, 41/32} in the store, where "
             "the lattice is genuinely tetragonal. (ii) `6797ab70c6015039` (#7) "
             "and `086ac96faf390886` (#9) have combinatorial aut 2 but "
             "Isom(solid) = 1: the map automorphism is not realised by any "
             "G-isometry at the witness (a combinatorial-only symmetry). "
             "(iii) `f654982d74d740f6` (#3, I4_1/amd) is the only achiral solid "
             "(its site symmetry contains a mirror); every other solid is "
             "chiral and every other honeycomb here is a proper (chiral) "
             "honeycomb with all translation classes of one hand. (iv) For "
             "every cell |H/L| = T*|site|: the full symmetry group of each "
             "honeycomb is exactly its generating space group (as in the cubic "
             "round).")
    L.append("")
    L.append("## Isometry vs site vs aut summary")
    L.append("")
    L.append("| # | type | IT | site | Isom_fix_site | Isom(solid) | Isom+ | "
             "solid | aut | \\|H/L\\| | T*site | full group = G |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for row in isoms:
        rank, cid, grp, ns, nf, ni, npr, ch, na, nops, T, fg = row
        L.append(f"| {rank} | `{cid}` | {grp} | {ns} | {nf} | {ni} | {npr} | "
                 f"{'chiral' if ch else 'achiral'} | {na} | {nops} | {T*ns} | "
                 f"{'yes' if fg else 'NO'} |")
    L.append("")
    L.append("## Counts reached (banked n<=4 == independent; independent to n<=5)")
    L.append("")
    L.append("| # | type | fixed (indep, n=1..reached) | free | one-sided | "
             "indep reached | indep wall |")
    L.append("|---|---|---|---|---|---|---|")
    for rank, cid, counts, ind in counts_rows:
        ns = sorted(ind["rows"])
        L.append(f"| {rank} | `{cid}` | {[ind['rows'][n][0] for n in ns]} | "
                 f"{[ind['rows'][n][1] for n in ns]} | "
                 f"{[ind['rows'][n][2] for n in ns]} | {ind['reached']}"
                 f"{' (cap)' if ind['timed_out'] else ''} | {ind['wall']:.0f}s |")
    L.append("")
    L.append("## Deferrals / failures")
    L.append("")
    if deferrals:
        for d in deferrals:
            L.append(f"- {d}")
    else:
        L.append("- none")
    L.append("")
    L.append(f"Total wall time {total_s:.0f}s. Deterministic except the timing "
             f"columns. Artifacts: `g4p2_tables_<id>.json` (+ `.txt` enumerator "
             f"input, `_indep.json` independent-enumerator record) per cell; "
             f"`g4p2_control_*` for the sanity gate.")
    L.append("")
    L.append("Re-run for acceptance: "
             "`python3 "
             "g4_certify_gram.py` (exit 0 required).")
    open(RESULTS_MD, "w").write("\n".join(L) + "\n")
    return allpass


def main(argv):
    gate_only = argv[1:] == ["--gate-only"]
    ids = [] if gate_only else (argv[1:] or [cid for _, cid in QUEUE])
    t0 = time.time()
    say = print
    say("loading phase2_types.json ...")
    store_all = json.load(open(STORE))
    store, snapshot = store_all["types"], store_all["catalog_snapshot"]
    groups = orbit.load_groups()
    seeds = json.load(open(SEEDS))["entries"]
    gate_lines, _ = sanity_gate(groups, store, seeds, say)
    if gate_only:
        say("gate-only run: PASS")
        return 0
    deadline_total = t0 + TOTAL_BUDGET_S
    results = []
    for cid in ids:
        assert cid in store, f"unknown type id {cid}"
        ent = store[cid]
        w = ent["first_witness"]
        if time.time() > deadline_total:
            say(f"[{cid}] TOTAL BUDGET EXHAUSTED before start — deferred")
            results.append({"cid": cid, "ent": ent, "witness": w, "stages": [],
                            "ctx": None, "lat": None, "sym": None, "v3": None,
                            "elapsed": 0.0})
            continue
        results.append(run_ladder(cid, ent, groups, w, say, deadline_total))
    allpass = write_results(gate_lines, results, time.time() - t0, snapshot)
    say(f"\nG4 PHASE-2 VERDICT: {'ALL STAGES PASS' if allpass else 'FAIL/DEFERRED'} "
        f"({time.time()-t0:.0f}s) — wrote G4_PHASE2_RESULTS.md")
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
