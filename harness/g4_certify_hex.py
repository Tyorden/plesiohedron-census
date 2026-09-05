#!/usr/bin/env python
"""g4_certify_hex.py — G4 finalist certificate ladder (ANCHORS G4, verbatim
gate) for PHASE 2 BATCH 2 (hexagonal family: trigonal + hexagonal systems,
IT 143-194, rational Gram metric in the ITA HEXAGONAL basis of the frozen G1
ops — ANCHORS G2c).  Sibling driver of the ACCEPTED tetragonal ladder
g4_certify_gram.py, whose ladder functions are IMPORTED UNCHANGED
(v0_rederive, v1_generate, v1_audit_gram, v2_symmetry, v3_tables_burnside,
run_ladder); the only edits to g4_certify_gram.py are the family switch in
gram_of (hexagonal -> metric.gram_hexagonal) and the optional INDEP_WORKERS
hook (default None = its previous behaviour; tetragonal --gate-only re-run
identical after the edit).

METRIC CONVENTIONS (ANCHORS G2c): sites and vertices in the ITA hexagonal
basis (a = b, gamma = 120 deg; rhombohedral groups on hexagonal axes, obverse
setting), scaled by an integer PERIOD; the metric is the integer Gram matrix
G = metric.gram_hexagonal(c/a) = [[2q^2, -q^2, 0], [-q^2, 2q^2, 0],
[0, 0, 2p^2]] for c/a = p/q (= 2q^2 * the a = 1 Gram [[1,-1/2,0],[-1/2,1,0],
[0,0,(c/a)^2]]).  Distances are G-norms; bisectors 2(r-c)^T G x = r^T G r -
c^T G c; the cutoff 4 rho^2 <= D^2 is held in the G-norm with the candidate
block proven complete by |x_i| <= D sqrt((G^-1)_ii).  VOLUMES are crystal-
basis (coordinate-space) measures; the Euclidean volume (a = 1) is that times
the SAME factor sqrt(det G_1) = (sqrt 3 / 2) (c/a) for the cell, the lattice
covolume and the torus, so T * vol(cell) = covol(L) = detL is an exact-
rational identity in the crystal basis, equivalent to the Euclidean one.
Facets and full-facet pairings are affine (metric-free); the metric enters
the tiling certificate through the Voronoi bisector claims (generator V1d +
the audit's fresh Gram layer).  V3 tables are metric-independent adjacency
data.

SANITY GATES (run first; the batch does not start unless all PASS):
  (i)   HEXAGONAL PRISM: P6/mmm #191 origin orbit at c/a = 1 through the
        hexagonal ladder must give the seed hexagonal_prism certificate:
        f = (12,18,8), aut 24, geometric stabilizer (Isom_fix_site) 24,
        Bravais point group 24, T = 1, |H/L| = 24 = T*|site|, and Burnside
        counts (fixed / free / one-sided, n <= 4) EQUAL to an INDEPENDENT
        enumeration of hexagonal-prism polyforms written here from scratch
        (cells Z^3 in the hexagonal basis, 8 neighbours = the 8 vectors of
        minimal G-norm at c/a = 1, point group = the 24 integer matrices
        preserving G, brute-forced).
  (ii)  RHOMBIC DODECAHEDRON: R-3m #166 origin orbit at c/a = 3 (rhombic
        dodecahedron per G2C_RESULT.md, stable at +-1/24) must reproduce the
        ACCEPTED cubic ladder (g4_certify.py functions, unmodified) on the
        Fm-3m #225 origin orbit number for number in the lattice-independent
        quantities: canonical code (== seed rhombic_dodecahedron), f, p,
        aut 48, T = 1, slots 12, FIXED counts n <= 4.  Differences are
        expected ONLY in the metric-dependent symmetry numbers and are
        explained + verified here: at c/a = 3 the rhombohedral lattice is
        NOT metrically cubic (FCC is at the irrational c/a = sqrt 6), so its
        Bravais group / site symmetry / honeycomb group are -3m (12) instead
        of m-3m (48); the FREE counts (orbits under the honeycomb's OWN
        symmetry group, |H/L| = 12 vs 48) therefore differ for n >= 2 —
        recorded as a pre-run prediction (free_hex(2) = 2 vs free_cubic(2) =
        1) — while the fixed counts (translation classes) are identical.
        Verified explicitly: a unimodular change of basis M carries the 12
        hexagonal-basis neighbour vectors onto the 12 cubic-basis ones and
        conjugates the 12 hexagonal honeycomb ops into a subgroup of the 48
        cubic ones (fresh code, brute force).
  (iii) BANKED TETRAGONAL ROW: g4p2 row 1497877268495988 (IT 91, #5 of
        G4_PHASE2_RESULTS.md) through the extended code: tables JSON byte-
        identical to the banked g4p2_tables_1497877268495988.json, banked +
        independent counts identical to the banked _indep.json rows, and the
        symmetry numbers identical to the banked results doc.

LADDER per survivor: identical to the tetragonal run (V0 exact re-derivation
at the stored witness; V1 tiling certificate in the G-norm + independent
adapted audit; V2 site / Isom_fix_site / Isom(solid) / aut chain over
G-orthogonal maps, Bravais group of L in G, |H/L| vs T*|site|; V3 banked
enumerate n<=4 + burnside_generic + INDEPENDENT enumerator to n<=5).  Kill
criteria live: > 38 facets asserts in V0 (the store's hexagonal-family menu
maximum is 24; "observed max 38" is folklore, never proven); ANY V-rung FAIL
stops the batch at once (pending cells cancelled, partial doc written,
exit 1).

RULE 29 (foreground batches): the driver runs the cells in a process pool
(--jobs, default 5; the independent enumerator gets --workers INDEP_WORKERS
= 2 per cell so the load stays under ~14 on 16 cores with 3 protected
processes) and STOPS SUBMITTING at --budget-s (default 420 s), lets running
cells finish, writes the (partial) results doc atomically and exits 3;
re-invoke with --resume until exit 0.  Per-cell records live in
g4p2hex_cells/<id>.json (resume boundary = whole cells; never half-written).

Run (main-session acceptance; deterministic doc up to the timing columns —
use --mask-timings for a byte-stable file, and the md5 of the masked text is
printed at the end of every complete run):
  PY=python3
  cd <repo>/harness
  $PY g4_certify_hex.py --fresh --budget-s 420; rc=$?; \\
    while [ $rc -eq 3 ]; do $PY g4_certify_hex.py --resume --budget-s 420; rc=$?; done; echo exit $rc
  $PY g4_certify_hex.py --gate-only            (gates only, ~1-2 min)
Exit 0 iff the gates and every stage of every survivor PASS; 3 = incomplete
(resume); 1 = FAIL or DEFERRED.

LANGUAGE (stated once): G4 passing does NOT establish novelty — every type
here stays "not matched against the records checked as of 2026-09-04"; no
naming; G5 is separate.
"""
import argparse
import hashlib
import itertools
import json
import os
import re
import shutil
import sys
import time
import traceback
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "phase2"))

import orbit                                                    # noqa: E402
import metric                                                   # noqa: E402
import g4_certify as G4C                                        # noqa: E402
import g4_certify_gram as G4G                                   # noqa: E402
from g4_certify_gram import run_ladder, N_ENUM, N_INDEP, STAGE_CAP_S  # noqa: E402
from g4_certify import pvec_compact, vsub                       # noqa: E402
from canon_code import canonical_code                           # noqa: E402
from mint_tables import mat_det, mat_mul, mat_inv, to_int_mat   # noqa: E402

STORE_HEX = os.path.join(HERE, "phase2_hexagonal_types.json")
STORE_HEX_SHA256 = ("7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633"
                    "858983a55")
STORE_TET = os.path.join(HERE, "phase2_types.json")
SEEDS = os.path.join(HERE, "seed_catalog.json")
TRIAGE_JSON = os.path.join(HERE, "triage_phase2_hex_shortlist.json")
TRIAGE_MD = os.path.join(HERE, "TRIAGE_PHASE2_HEX_RESULT.md")
RESULTS_MD = os.path.join(HERE, "G4_PHASE2_HEX_RESULTS.md")
CELL_DIR = os.path.join(HERE, "g4p2hex_cells")
GATE_RECORD = os.path.join(CELL_DIR, "_gates.json")
PREFIX = "g4p2hex_tables_"
CTRL_PREFIX = "g4p2hex_control_"
TET_CONTROL_ID = "1497877268495988"
SNAPSHOT = "2026-09-04"
MAX_FACETS = 38
INDEP_WORKERS = 2
INDEP_CAP_S = 240          # per-cell cap of the independent enumerator (its
                           # --wall-cap is 0.6 x this); 15 min in the
                           # tetragonal run — lowered so that a cell always
                           # fits a rule-29 foreground batch; a cell hitting
                           # it is reported as "reached n < 5" (deferral)
PER_CELL_DEADLINE_S = 3600


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mask_timings(text):
    return re.sub(r"\b\d+(?:\.\d+)?s\b", "<t>", text)


# ------------------------------------------------ gate (i): independent
# hexagonal-prism polyform enumerator (fresh code; nothing imported)
def hexprism_polyforms_independent(nmax=N_ENUM):
    G = ((2, -1, 0), (-1, 2, 0), (0, 0, 2))          # gram_hexagonal(1)

    def q(u):
        return sum(u[i] * G[i][j] * u[j] for i in range(3) for j in range(3))

    # 8 neighbours = all integer vectors of minimal positive G-norm (= 2)
    nbrs = [v for v in itertools.product(range(-2, 3), repeat=3)
            if v != (0, 0, 0) and q(v) == 2]
    assert sorted(nbrs) == sorted([(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                                   (0, -1, 0), (1, 1, 0), (-1, -1, 0),
                                   (0, 0, 1), (0, 0, -1)]), nbrs
    # point group: integer matrices with entries in [-2, 2] preserving G
    ops = []
    for e in itertools.product(range(-2, 3), repeat=9):
        U = ((e[0], e[1], e[2]), (e[3], e[4], e[5]), (e[6], e[7], e[8]))
        ok = True
        for i in range(3):
            for j in range(3):
                if sum(U[k][i] * G[k][l] * U[l][j]
                       for k in range(3) for l in range(3)) != G[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ops.append(U)
    assert len(ops) == 24, len(ops)
    dets = [mat_det(U) for U in ops]
    proper = [U for U, d in zip(ops, dets) if d == 1]
    assert len(proper) == 12
    # sanity: the neighbour set is invariant under every op
    nset = set(nbrs)
    for U in ops:
        assert {tuple(sum(U[i][j] * v[j] for j in range(3)) for i in range(3))
                for v in nbrs} == nset

    def canon(cells):
        m = min(cells)
        return tuple(sorted((c[0]-m[0], c[1]-m[1], c[2]-m[2]) for c in cells))

    def apply(U, cells):
        return canon([tuple(sum(U[i][j] * c[j] for j in range(3))
                            for i in range(3)) for c in cells])

    fixed, free, onesided = [], [], []
    level = {canon([(0, 0, 0)])}
    for n in range(1, nmax + 1):
        if n > 1:
            nxt = set()
            for shape in level:
                sset = set(shape)
                for c in shape:
                    for d in nbrs:
                        w = (c[0]+d[0], c[1]+d[1], c[2]+d[2])
                        if w not in sset:
                            nxt.add(canon(list(shape) + [w]))
            level = nxt
        fixed.append(len(level))
        free.append(len({min(apply(U, s) for U in ops) for s in level}))
        onesided.append(len({min(apply(U, s) for U in proper) for s in level}))
    return {"fixed": fixed, "free": free, "onesided": onesided,
            "n_ops": len(ops), "n_proper": len(proper)}


# ------------------------------------------------ gate (ii): cubic reference
def cubic_path_reference(groups, number, cid, say):
    """ACCEPTED cubic ladder (g4_certify.py functions, unmodified) on the
    origin orbit of a cubic group; artifacts renamed under CTRL_PREFIX."""
    from sweep_voronoi import sweep
    from exact_cell import clip_cell
    g = groups[number]
    p = (F(0), F(0), F(0))
    ob = orbit.orbit(g, p)
    pts, period = orbit.scale_orbit(ob["points"])
    cells_f = sweep(pts, period, W=2)
    ec = clip_cell(pts[0], pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2
    code, aut = canonical_code(ec["facet_cycles"])
    Fc, V = ec["facet_count"], ec["n_vertices"]
    E = sum(len(c) for c in ec["facet_cycles"]) // 2
    ctx = {"cid": cid, "g": g, "p": p, "ob": ob, "pts": pts, "period": period,
           "ec": ec, "code": code.decode("ascii"), "aut": aut, "Fc": Fc,
           "V": V, "E": E, "site_ops": orbit.site_stabilizer(g, p)}
    f0 = cells_f[0]
    assert f0["facet_count"] == Fc and f0["p_vector"] == ec["p_vector"]
    cert, lat, _ = G4C.v1_generate(ctx)
    G4C.v1_audit(json.loads(json.dumps(cert)))
    sym = G4C.v2_symmetry(ctx, lat)
    v3 = G4C.v3_tables_burnside(ctx, lat, sym, time.time() + STAGE_CAP_S)
    for ext in (".json", ".txt"):
        src = os.path.join(HERE, f"g4_tables_{cid}{ext}")
        dst = os.path.join(HERE, f"{CTRL_PREFIX}{cid}{ext}")
        os.replace(src, dst)
    ref = {"code": ctx["code"], "f": (V, E, Fc), "p": tuple(ec["p_vector"]),
           "aut": aut, "T": lat["T"], "detL": lat["detL"], "vol": str(lat["vol"]),
           "slots": lat["T"] * Fc, "site": sym["n_site"],
           "stab_geo": sym["n_geo"], "brav": sym["n_brav"],
           "n_ops": v3["n_ops"], "n_proper": v3["n_proper"],
           "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
           "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)]}
    say(f"  cubic path (g4_certify functions, {g['international_short']} "
        f"#{number} origin): {ref}")
    return ref, os.path.join(HERE, f"{CTRL_PREFIX}{cid}.json")


def lattice_conjugacy_check(hex_tables_path, cubic_tables_path):
    """Fresh code.  Both tables have T = 1: neighbour deltas D_h, D_c (12
    lattice vectors each) and point ops A_h (12), A_c (48) as integer
    matrices in their own lattice coordinates.  Find unimodular M with
    M D_h = D_c (as sets) and check M A_h M^-1 <= A_c (subgroup)."""
    th = json.load(open(hex_tables_path))
    tc = json.load(open(cubic_tables_path))
    assert th["T"] == 1 and tc["T"] == 1
    Dh = [tuple(dv) for dv, _ in th["nbr"][0]]
    Dc = [tuple(dv) for dv, _ in tc["nbr"][0]]
    assert len(Dh) == len(Dc) == 12 and len(set(Dh)) == 12 and len(set(Dc)) == 12
    Ah = [tuple(tuple(r) for r in op["A"]) for op in th["ops"]]
    Ac = {tuple(tuple(r) for r in op["A"]) for op in tc["ops"]}
    assert len(Ah) == 12 and len(Ac) == 48
    # three independent hex deltas
    for d1, d2, d3 in itertools.combinations(Dh, 3):
        if mat_det((d1, d2, d3)) != 0:
            break
    Dm = [[F(d1[i]), F(d2[i]), F(d3[i])] for i in range(3)]   # columns
    Dinv = mat_inv(Dm)
    found = []
    for c1, c2, c3 in itertools.permutations(Dc, 3):
        Cm = [[F(c1[i]), F(c2[i]), F(c3[i])] for i in range(3)]
        M = mat_mul(Cm, Dinv)
        if any(x.denominator != 1 for row in M for x in row):
            continue
        M = tuple(tuple(int(x) for x in row) for row in M)
        if abs(mat_det(M)) != 1:
            continue
        img = {tuple(sum(M[i][j] * d[j] for j in range(3)) for i in range(3))
               for d in Dh}
        if img == set(Dc):
            found.append(M)
            break
    assert found, "no unimodular M carries the hexagonal deltas onto the cubic"
    M = found[0]
    Mf = [[F(x) for x in row] for row in M]
    Minv = mat_inv(Mf)
    conj = []
    for A in Ah:
        B = mat_mul(mat_mul(Mf, [[F(x) for x in row] for row in A]), Minv)
        B = tuple(tuple(int(x) for x in row) for row in B)
        assert B in Ac, f"conjugated hexagonal op {A} -> {B} not a cubic op"
        conj.append(B)
    assert len(set(conj)) == 12
    return M


# ------------------------------------------------ result reduction (workers)
def _fs(x):
    return str(F(x))


def reduce_result(rank, r, lines, label):
    ctx, lat, sym, v3 = r["ctx"], r["lat"], r["sym"], r["v3"]
    ent, w = r["ent"], r["witness"]
    out = {"rank": rank, "cid": r["cid"], "label": label,
           "f_vector": list(ent["f_vector"]), "p_vector": list(ent["p_vector"]),
           "p_compact": pvec_compact(ent["p_vector"]),
           "aut_order": ent["aut_order"], "witness": w,
           "group_symbol": ent["first_witness"]["group_symbol"]
           if "first_witness" in ent else None,
           "stages": r["stages"], "elapsed": r["elapsed"], "log": lines,
           "ctx": None, "lat": None, "sym": None, "v3": None}
    if ctx is not None:
        out["ctx"] = {"V": ctx["V"], "E": ctx["E"], "F": ctx["Fc"],
                      "aut": ctx["aut"], "G": [list(row) for row in ctx["G"]],
                      "period": ctx["period"], "n_conv": len(ctx["pts"]),
                      "site": ctx["ob"]["stabilizer_order"], "W": ctx["W"],
                      "nonsimple": ctx["ec"]["nonsimple_vertices"],
                      "code": ctx["code"]}
        assert ctx["Fc"] <= MAX_FACETS, f"KILL: {ctx['Fc']} facets > {MAX_FACETS}"
    if lat is not None:
        out["lat"] = {"T": lat["T"], "detL": lat["detL"], "vol": str(lat["vol"])}
    if sym is not None:
        out["sym"] = {k: sym[k] for k in ("n_site", "n_fix", "n_iso", "n_proper",
                                          "chiral", "n_aut", "n_brav", "n_ops",
                                          "n_ops_improper", "h_cell", "full_is_G")}
        out["sym"]["iso"] = [{"A": [[_fs(x) for x in row] for row in x["A"]],
                              "t": [_fs(x) for x in x["t"]], "det": int(x["det"]),
                              "fixes_site": x["fixes_site"]} for x in sym["iso"]]
        # DOUBLE CHECK (fresh, in-worker) whenever Isom(solid) > site or
        # Isom_fix_site > site: every listed isometry re-verified as a
        # G-orthogonal affine map permuting the vertex set; whether it also
        # maps the site set to itself (then it is a honeycomb symmetry).
        if sym["n_iso"] > sym["n_site"] or sym["n_fix"] > sym["n_site"]:
            G = ctx["G"]
            verts = {tuple(F(x) for x in v) for v in ctx["ec"]["vertices"]}
            P = ctx["period"]
            sites = {tuple(F(x) for x in q) for q in ctx["pts"]}
            site_R = {tuple(tuple(F(x) for x in row) for row in Rm)
                      for Rm, _ in ctx["site_ops"]}
            dc = []
            for x in sym["iso"]:
                A, t = x["A"], x["t"]
                AtGA = [[sum(A[k][i] * G[k][l] * A[l][j] for k in range(3)
                             for l in range(3)) for j in range(3)] for i in range(3)]
                orth = AtGA == [[F(G[i][j]) for j in range(3)] for i in range(3)]
                img = {tuple(sum(A[k][j] * v[j] for j in range(3)) + t[k]
                             for k in range(3)) for v in verts}
                permutes = img == verts
                simg = {tuple((sum(A[k][j] * s[j] for j in range(3)) + t[k]) % P
                              for k in range(3)) for s in sites}
                dc.append({"det": int(x["det"]), "fixes_site": x["fixes_site"],
                           "G_orthogonal": orth, "permutes_vertices": permutes,
                           "linear_part_in_site_group": A in site_R,
                           "maps_site_set_to_itself": simg == sites})
            assert all(d["G_orthogonal"] and d["permutes_vertices"] for d in dc)
            out["sym"]["double_check"] = dc
    if v3 is not None:
        out["v3"] = {"deferred": v3.get("deferred", False),
                     "detail": v3.get("detail", "")}
        if v3.get("counts"):
            ind = v3["indep"]
            out["v3"].update({
                "counts": {str(n): list(v3["counts"][n]) for n in v3["counts"]},
                "n_ops": v3["n_ops"], "n_proper": v3["n_proper"],
                "hand_consistent": v3["hand_consistent"],
                "n_other_hand": v3["n_other_hand"],
                "indep": {"reached": ind["reached"], "target": ind["target"],
                          "timed_out": ind["timed_out"], "wall": ind["wall"],
                          "capped_by_field": ind["capped_by_field"],
                          "rows": {str(n): list(ind["rows"][n])
                                   for n in ind["rows"]}}})
    return out


_W = {}


def _init(indep_workers, indep_cap):
    _W["groups"] = orbit.load_groups()
    G4G.INDEP_WORKERS = indep_workers
    G4G.INDEP_CAP_S = indep_cap


def _work(job):
    rank, cid, ent, w, label = job
    lines = []
    r = run_ladder(cid, ent, _W["groups"], w, lines.append,
                   time.time() + PER_CELL_DEADLINE_S, prefix=PREFIX)
    return reduce_result(rank, r, lines, label)


# ------------------------------------------------ triage labels (carried)
def load_triage_labels():
    """O/W label per type from the triage's full ranked table (carried over,
    NOT re-derived): 'open-likely (triage, 12 b)' etc., plus the full-table
    rank and the metric-thin flag."""
    txt = open(TRIAGE_MD).read()
    sec = txt.split("## Full ranked table")[1].split("\n## ")[0]
    labels = {}
    for line in sec.splitlines():
        if not line.startswith("| ") or line.startswith("| rank") \
                or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        assert len(cells) == 18, (len(cells), line[:80])
        rank_full, cid = int(cells[0]), cells[1].strip("`")
        n_b, thin, ow, verdict = cells[8], cells[13], cells[14], cells[16]
        lab = f"{ow} (triage, {n_b} b{'; metric-thin: ' + thin if thin else ''})"
        labels[cid] = {"label": lab, "rank_full": rank_full, "ow": ow,
                       "n_b": int(n_b), "thin": thin, "verdict": verdict}
    return labels


# ------------------------------------------------ gates
def run_gates(groups, seeds, say):
    G4G.INDEP_WORKERS = INDEP_WORKERS
    G4G.INDEP_CAP_S = INDEP_CAP_S
    gate = {"lines": [], "pass": True}
    seed = {e["name"]: e for e in seeds}

    # ---- (i) hexagonal prism
    say("== GATE (i): hexagonal prism, P6/mmm #191 origin at c/a = 1 ==")
    t0 = time.time()
    s = seed["hexagonal_prism"]
    ent = {"canon_code": s["canon_code"], "f_vector": s["f_vector"],
           "p_vector": s["p_vector"], "aut_order": s["aut_order"]}
    w = {"group": 191, "point": ["0", "0", "0"], "b": "1"}
    r = run_ladder("ctrl_hexprism_P6mmm_ca1", ent, groups, w, say,
                   time.time() + STAGE_CAP_S, prefix=CTRL_PREFIX)
    assert all(st["verdict"] == "PASS" for st in r["stages"]) and \
        len(r["stages"]) == 5, "hexagonal ladder failed on the prism control"
    ctx, lat, sym, v3 = r["ctx"], r["lat"], r["sym"], r["v3"]
    got = {"code_is_seed": ctx["code"] == s["canon_code"],
           "f": (ctx["V"], ctx["E"], ctx["Fc"]), "aut": ctx["aut"],
           "site": sym["n_site"], "stab_geo": sym["n_fix"],
           "Isom": sym["n_iso"], "brav": sym["n_brav"], "T": lat["T"],
           "H_over_L": sym["n_ops"], "full_is_G": sym["full_is_G"],
           "G": ctx["G"], "period": ctx["period"],
           "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
           "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)],
           "onesided_indep": [v3["indep"]["rows"][n][2]
                              for n in range(1, N_ENUM+1)],
           "indep_reached": v3["indep"]["reached"]}
    exp = {"code_is_seed": True, "f": (12, 18, 8), "aut": 24, "site": 24,
           "stab_geo": 24, "Isom": 24, "brav": 24, "T": 1, "H_over_L": 24,
           "full_is_G": True, "G": ((2, -1, 0), (-1, 2, 0), (0, 0, 2)),
           "period": 12}
    diffs = {k: (exp[k], got[k]) for k in exp if exp[k] != got[k]}
    assert not diffs, f"GATE (i) FAILED: {diffs}"
    ind = hexprism_polyforms_independent(N_ENUM)
    cmp_ = {"fixed": (got["fixed"], ind["fixed"]),
            "free": (got["free"], ind["free"]),
            "onesided": (got["onesided_indep"], ind["onesided"])}
    bad = {k: v for k, v in cmp_.items() if v[0] != v[1]}
    assert not bad, f"GATE (i) Burnside counts differ from the independent " \
                    f"hexagonal-prism enumeration: {bad}"
    assert ind["n_ops"] == 24 and ind["n_proper"] == 12
    line = (f"GATE (i) PASS: P6/mmm #191 origin orbit at c/a=1 (G="
            f"{ctx['G']}, period 12, 1 site) through the hexagonal ladder == "
            f"the seed hexagonal-prism certificate: code == seed, f=(12,18,8), "
            f"aut 24, site 24, geometric stabilizer (Isom_fix_site) 24, "
            f"Isom(solid) 24 (Isom+ {sym['n_proper']}), Bravais point group of "
            f"the hexagonal lattice 24, T=1, |H/L|=24 = T*|site|; Burnside "
            f"counts n<=4 from the ladder (banked enumerate + independent "
            f"verify_counts_independent.py, reached n={got['indep_reached']}) "
            f"fixed={got['fixed']} free={got['free']} one-sided="
            f"{got['onesided_indep']} EQUAL to the fresh independent hexagonal-"
            f"prism polyform enumeration written in this file (8 neighbours = "
            f"the 8 integer vectors of minimal G-norm; point group = the 24 "
            f"integer matrices preserving G, brute-forced in [-2,2]^9, 12 "
            f"proper): fixed={ind['fixed']} free={ind['free']} one-sided="
            f"{ind['onesided']} ({time.time()-t0:.0f}s)")
    say(line)
    gate["lines"].append(line)
    gate["prism"] = {"ladder": {k: (list(v) if isinstance(v, tuple) else v)
                                for k, v in got.items()}, "independent": ind}

    # ---- (ii) rhombic dodecahedron
    say("== GATE (ii): rhombic dodecahedron, R-3m #166 origin at c/a = 3 vs "
        "accepted cubic ladder on Fm-3m #225 origin ==")
    t0 = time.time()
    ref, cubic_tables = cubic_path_reference(groups, 225,
                                             "ctrl_cubicpath_rhombdod", say)
    s = seed["rhombic_dodecahedron"]
    assert ref["code"] == s["canon_code"] and ref["aut"] == 48
    ent = {"canon_code": s["canon_code"], "f_vector": s["f_vector"],
           "p_vector": s["p_vector"], "aut_order": s["aut_order"]}
    w = {"group": 166, "point": ["0", "0", "0"], "b": "3"}
    r2 = run_ladder("ctrl_rhombdod_R3m_ca3", ent, groups, w, say,
                    time.time() + STAGE_CAP_S, prefix=CTRL_PREFIX)
    assert all(st["verdict"] == "PASS" for st in r2["stages"]) and \
        len(r2["stages"]) == 5, "hexagonal ladder failed on the R-3m control"
    ctx, lat, sym, v3 = r2["ctx"], r2["lat"], r2["sym"], r2["v3"]
    got = {"code": ctx["code"], "f": (ctx["V"], ctx["E"], ctx["Fc"]),
           "p": tuple(ctx["ec"]["p_vector"]), "aut": ctx["aut"], "T": lat["T"],
           "detL": lat["detL"], "vol": str(lat["vol"]), "slots": lat["T"]*ctx["Fc"],
           "site": sym["n_site"], "stab_geo": sym["n_fix"], "brav": sym["n_brav"],
           "n_ops": v3["n_ops"], "n_proper": v3["n_proper"],
           "fixed": [v3["counts"][n][0] for n in range(1, N_ENUM+1)],
           "free": [v3["counts"][n][1] for n in range(1, N_ENUM+1)]}
    lattice_independent = ("code", "f", "p", "aut", "T", "slots", "fixed")
    diffs = {k: (ref[k], got[k]) for k in lattice_independent if ref[k] != got[k]}
    assert not diffs, f"GATE (ii) FAILED (lattice-independent quantities): {diffs}"
    metric_dependent = {k: (ref[k], got[k]) for k in
                        ("site", "stab_geo", "brav", "n_ops", "n_proper",
                         "free", "detL", "vol") if ref[k] != got[k]}
    # pre-run predictions (recorded in the docstring): -3m (12) vs m-3m (48)
    assert got["site"] == 12 and got["stab_geo"] == 12 and got["brav"] == 12 \
        and got["n_ops"] == 12 and sym["n_iso"] == 12 and sym["full_is_G"], \
        (got, sym["n_iso"], sym["full_is_G"])
    assert ref["site"] == 48 and ref["brav"] == 48 and ref["n_ops"] == 48
    assert got["free"][0] == ref["free"][0] == 1 and got["free"][1] == 2 \
        and ref["free"][1] == 1, (got["free"], ref["free"])
    assert all(got["free"][i] >= ref["free"][i] for i in range(N_ENUM))
    assert ctx["ec"]["nonsimple_vertices"] == 6          # the 6 four-valent apices
    M = lattice_conjugacy_check(
        os.path.join(HERE, f"{CTRL_PREFIX}ctrl_rhombdod_R3m_ca3.json"),
        cubic_tables)
    line = (f"GATE (ii) PASS: R-3m #166 origin orbit at c/a=3 (rhombohedral "
            f"lattice on hexagonal axes, 3 sites/conventional cell, period "
            f"{ctx['period']}, G={ctx['G']}) through the hexagonal ladder "
            f"reproduces the ACCEPTED cubic ladder (g4_certify.py functions, "
            f"unmodified) on the Fm-3m #225 origin orbit number for number in "
            f"every lattice-independent quantity: canonical code (== seed "
            f"rhombic_dodecahedron), f={got['f']}, p={pvec_compact(got['p'])}, "
            f"aut {got['aut']}, T={got['T']}, slots {got['slots']}, 6 non-simple "
            f"vertices, FIXED counts n<=4 {got['fixed']} == {ref['fixed']}. "
            f"EXPECTED metric-dependent differences, all explained: "
            f"{metric_dependent} — at c/a=3 the rhombohedral lattice is not "
            f"metrically cubic (FCC is at the irrational c/a=sqrt6), so site "
            f"symmetry, Isom_fix_site, Isom(solid), Bravais group and |H/L| "
            f"are all -3m (12) instead of m-3m (48) [|H/L|=12=T*|site|, full "
            f"group IS R-3m]; FREE counts are orbits under the honeycomb's OWN "
            f"symmetry group (12 vs 48 ops), hence free_hex(n) >= free_cubic(n) "
            f"with equality only at n=1 (pre-run prediction free_hex(2)=2 vs 1: "
            f"confirmed); detL/vol are crystal-basis measures in different "
            f"bases (rhombohedral-on-hexagonal-axes vs cubic F) and are not "
            f"comparable. VERIFIED: the unimodular change of basis M={M} carries "
            f"the 12 hexagonal-basis neighbour vectors onto the 12 cubic-basis "
            f"ones and conjugates the 12 hexagonal honeycomb ops into a "
            f"subgroup of the 48 cubic ones (fresh code); independent "
            f"enumerator reached n={v3['indep']['reached']} "
            f"({time.time()-t0:.0f}s)")
    say(line)
    gate["lines"].append(line)
    gate["rhombdod"] = {"cubic_ref": {k: (list(v) if isinstance(v, tuple) else v)
                                      for k, v in ref.items()},
                        "hex": {k: (list(v) if isinstance(v, tuple) else v)
                                for k, v in got.items()},
                        "M": [list(row) for row in M]}

    # ---- (iii) banked tetragonal row through the extended code
    say(f"== GATE (iii): banked tetragonal g4p2 row {TET_CONTROL_ID} ==")
    t0 = time.time()
    tet = json.load(open(STORE_TET))["types"][TET_CONTROL_ID]
    r3 = run_ladder(f"tet_{TET_CONTROL_ID}", tet, groups, tet["first_witness"],
                    say, time.time() + STAGE_CAP_S, prefix=CTRL_PREFIX)
    assert all(st["verdict"] == "PASS" for st in r3["stages"]) and \
        len(r3["stages"]) == 5, "extended code failed on the banked tetragonal row"
    ctx, lat, sym, v3 = r3["ctx"], r3["lat"], r3["sym"], r3["v3"]
    mine = open(os.path.join(HERE, f"{CTRL_PREFIX}tet_{TET_CONTROL_ID}.json"),
                "rb").read()
    banked = open(os.path.join(HERE, f"g4p2_tables_{TET_CONTROL_ID}.json"),
                  "rb").read()
    assert mine == banked, "tables JSON differs from the banked g4p2 tables"
    bi = json.load(open(os.path.join(HERE,
                                     f"g4p2_tables_{TET_CONTROL_ID}_indep.json")))
    brows = {row["n"]: (row["fixed"], row["free"], row["onesided"])
             for row in bi["rows"]}
    mrows = {n: tuple(v3["indep"]["rows"][n][:3]) for n in v3["indep"]["rows"]}
    assert mrows == brows, f"independent rows differ: {mrows} vs {brows}"
    assert all(tuple(v3["counts"][n]) == brows[n][:2] for n in range(1, N_ENUM+1))
    md = open(os.path.join(HERE, "G4_PHASE2_RESULTS.md")).read()
    sect = md.split(f"`{TET_CONTROL_ID}`")[1].split("\n## ")[0]
    m = re.search(r"site=(\d+), Isom_fix_site=(\d+), Isom\(solid\)=(\d+) "
                  r"\(Isom\+=(\d+), improper=(\d+);.*?aut_comb=(\d+).*?"
                  r"Bravais point group of L in G: order (\d+).*?"
                  r"\|H/L\|=(\d+)", sect, re.S)
    assert m, "could not parse the banked V2 line"
    bank_sym = tuple(int(x) for x in m.groups())
    my_sym = (sym["n_site"], sym["n_fix"], sym["n_iso"], sym["n_proper"],
              sym["n_iso"] - sym["n_proper"], sym["n_aut"], sym["n_brav"],
              sym["n_ops"])
    assert my_sym == bank_sym, (my_sym, bank_sym)
    m2 = re.search(r"banked enumerate n<=4: fixed=(\[[^\]]*\]), free=(\[[^\]]*\])",
                   sect)
    assert json.loads(m2.group(1)) == [v3["counts"][n][0] for n in range(1, 5)]
    assert json.loads(m2.group(2)) == [v3["counts"][n][1] for n in range(1, 5)]
    line = (f"GATE (iii) PASS: banked tetragonal g4p2 row {TET_CONTROL_ID} "
            f"(IT(91) P4_122, #5 of G4_PHASE2_RESULTS.md) through the extended "
            f"code: V0-V3 all PASS; tables JSON byte-identical to the banked "
            f"g4p2_tables_{TET_CONTROL_ID}.json ({len(banked)} bytes); banked "
            f"counts fixed={[v3['counts'][n][0] for n in range(1, 5)]} "
            f"free={[v3['counts'][n][1] for n in range(1, 5)]} and the "
            f"independent rows n<={max(mrows)} identical to the banked "
            f"_indep.json; V2 numbers (site, Isom_fix, Isom, Isom+, improper, "
            f"aut, Bravais, |H/L|) = {my_sym} identical to the banked doc "
            f"({time.time()-t0:.0f}s)")
    say(line)
    gate["lines"].append(line)
    gate["tet"] = {"sym": list(my_sym), "bytes": len(banked)}
    return gate


# ------------------------------------------------ generating-group check
def generating_group_check(rec, groups):
    """Fresh double-check of |H/L| against the frozen ops (parent process):
    every hexagonal-family group whose orbit of the witness point equals the
    cell's site set (both from orbit.orbit on the frozen G1 ops).  The largest
    point-op count |H_conv|/centering among them can never exceed the ladder's
    |H/L| (the ladder enumerates ALL honeycomb symmetries via the Bravais
    embedding) — asserted; equality identifies the honeycomb's full symmetry
    group within the frozen list (same setting).  For such a group its site
    stabilizer order must equal |H/L|/T (orbit-stabilizer) — asserted."""
    w = rec["witness"]
    p = tuple(F(x) for x in w["point"])
    S0 = set(orbit.orbit(groups[w["group"]], p)["points"])
    hits = []
    for num in sorted(groups):
        g = groups[num]
        if g["crystal_family"] != "hexagonal":
            continue
        ob = orbit.orbit(g, p)
        if set(ob["points"]) == S0:
            hits.append({"group": num, "symbol": g["international_short"],
                         "site": ob["stabilizer_order"],
                         "point_ops": len(g["ops_exact"])
                         // g["centering"]["multiplicity"]})
    assert any(h["group"] == w["group"] for h in hits)
    mx = max(h["point_ops"] for h in hits)
    n_ops = rec["sym"]["n_ops"]
    assert mx <= n_ops, (f"{rec['cid']}: a frozen-list group reproduces the "
                         f"site set with {mx} point ops > |H/L| = {n_ops}")
    best = [h for h in hits if h["point_ops"] == mx]
    if mx == n_ops:
        assert all(h["site"] == rec["sym"]["h_cell"] for h in best), (best, rec["sym"])
        return {"hits": hits, "max_point_ops": mx, "identified": True,
                "shift": None, "full_groups": best}
    # second pass: the full group may sit in the frozen list with a DIFFERENT
    # origin — try every origin shift s in (Z/P)^3 for the groups whose
    # point-op count equals |H/L|: S0 == orbit_H(p + s) - s (mod 1)
    P = rec["ctx"]["period"]
    shifted = []
    for num in sorted(groups):
        g = groups[num]
        if g["crystal_family"] != "hexagonal" or \
                len(g["ops_exact"]) // g["centering"]["multiplicity"] != n_ops:
            continue
        for sh in itertools.product(range(P), repeat=3):
            sv = tuple(F(x, P) for x in sh)
            ob = orbit.orbit(g, tuple(p[i] + sv[i] for i in range(3)))
            img = {tuple((q[i] - sv[i]) % 1 for i in range(3)) for q in ob["points"]}
            if img == S0:
                assert ob["stabilizer_order"] == rec["sym"]["h_cell"]
                shifted.append({"group": num, "symbol": g["international_short"],
                                "site": ob["stabilizer_order"], "point_ops": n_ops,
                                "shift": [str(x) for x in sv]})
                break
    return {"hits": hits, "max_point_ops": mx, "identified": bool(shifted),
            "shift": [h["shift"] for h in shifted] if shifted else None,
            "full_groups": shifted}


# ------------------------------------------------ results doc
def write_results(gate, records, total_s, complete, mask, fail_msgs,
                  n_expected):
    L = ["# G4 certificate results — PHASE 2 BATCH 2 (hexagonal family, Gram "
         "metric in the ITA hexagonal basis), V0-V3 ladder (2026-09-04)", ""]
    if not complete:
        L += ["**PARTIAL RESULTS — the batch is NOT complete "
              f"({len(records)} of {n_expected} survivors certified so far; "
              "resume with `--resume`). Nothing below is final.**", ""]
    if fail_msgs:
        L += ["**BATCH STOPPED ON FAIL (kill criterion: any V-rung FAIL stops "
              "the batch):**"] + [f"- {m}" for m in fail_msgs] + [""]
    L += ["Gate: `../ANCHORS.md` G4 (paper-I-standard ladder V0-V3, "
          "`../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3) applied through the "
          "accepted Gram chain (`phase2/metric.py` gram_hexagonal, "
          "`phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`; G2b + "
          "G2c). Generator: `g4_certify_hex.py` (this run) driving the ladder "
          "functions of the accepted tetragonal `g4_certify_gram.py` UNCHANGED "
          "(V0-V3, `run_ladder`); the only edits to that file are the family "
          "switch in `gram_of` (hexagonal -> `metric.gram_hexagonal`) and the "
          "optional `INDEP_WORKERS` hook (default None = previous behaviour; "
          "its tetragonal `--gate-only` output is identical after the edit). "
          "The metric-independent pieces of the accepted cubic "
          "`g4_certify.py` (exact vector bits, fan volume, the independent "
          "affine audit `v1_audit`/`_a_*`, banked V3 tool paths) are imported "
          "as before. Inputs: `phase2_hexagonal_types.json` (sha256 "
          f"{STORE_HEX_SHA256[:16]}... verified before the run) stored "
          "witnesses of the 151 collision-screen survivors "
          "(`COLLISION_PHASE2_HEX_RESULTS.md`, ranking = "
          "`triage_phase2_hex_shortlist.json` survivors_ranked), frozen G1 "
          "`spacegroups.json`. V3 uses the banked `export_tables.py` + "
          "compiled `enumerate` + `burnside_generic.py` (POLYFORMS_II) and "
          "then the INDEPENDENT `../publication/verify_counts_independent.py` "
          f"(dual-implementation bar, n<=5 under a {INDEP_CAP_S//60}-min cap, "
          f"--workers {INDEP_WORKERS} per cell).", "",
          "**METRIC CONVENTIONS.** Sites/vertices in the ITA HEXAGONAL basis of "
          "the frozen ops (a = b, gamma = 120 deg; rhombohedral groups on "
          "hexagonal axes, obverse setting), integer-scaled by PERIOD; metric "
          "= integer Gram G = [[2q^2, -q^2, 0], [-q^2, 2q^2, 0], [0, 0, 2p^2]] "
          "for c/a = p/q. All distances are G-norms; bisectors 2(r-c)^T G x = "
          "r^T G r - c^T G c; the cutoff 4 rho^2 <= D^2 holds in the G-norm "
          "with the candidate block proven complete by |x_i| <= D "
          "sqrt((G^-1)_ii). **Volumes are crystal-basis (coordinate-space) "
          "measures**; the Euclidean volume (a = 1) is that times the SAME "
          "factor (sqrt 3 / 2)(c/a) for the cell, the lattice covolume and the "
          "torus, so T * vol(cell) = covol(L) = detL is an exact-rational "
          "identity in the crystal basis, equivalent to the Euclidean one. "
          "Facets and full-facet pairings are affine (metric-free); the metric "
          "enters the tiling certificate through the Voronoi bisector claims, "
          "verified in the G-norm by the generator (V1d) and re-verified by "
          "the audit's fresh Gram layer.", "",
          "**V3 tables are metric-independent adjacency data** (which cells "
          "share a facet; point ops mod L acting on cell IDs) — stated once; "
          "the metric has already done its work in V1/V2.", "",
          "**LANGUAGE (stated once): G4 passing does NOT establish novelty. "
          "Every type below remains \"not matched against the records checked "
          f"as of {SNAPSHOT}\"; no naming; G5 is separate and has not closed. "
          "Kill criteria were live (facet count > 38 asserts in V0 — the "
          "family's menu maximum is 24; \"observed max 38\" is folklore, never "
          "proven; any V-rung FAIL stops the batch).**", "",
          "## Sanity gates (run first, all three PASS before any survivor)", ""]
    for g in gate["lines"]:
        L.append(f"- {g}")
    L.append("")
    pr = gate["prism"]
    L += ["Gate (i) Burnside comparison (n = 1..4):", "",
          "| source | fixed | free | one-sided |", "|---|---|---|---|",
          f"| ladder (banked enumerate + independent verify_counts_independent.py) "
          f"| {pr['ladder']['fixed']} | {pr['ladder']['free']} | "
          f"{pr['ladder']['onesided_indep']} |",
          f"| fresh hexagonal-prism polyform enumerator (this file) | "
          f"{pr['independent']['fixed']} | {pr['independent']['free']} | "
          f"{pr['independent']['onesided']} |", ""]
    rd = gate["rhombdod"]
    L += ["Gate (ii) number-for-number table (cubic reference = accepted "
          "g4_certify.py functions on Fm-3m #225 origin; hexagonal = this "
          "ladder on R-3m #166 origin at c/a = 3):", "",
          "| quantity | cubic Fm-3m #225 | hexagonal R-3m #166 c/a=3 | class |",
          "|---|---|---|---|"]
    for k in ("code", "f", "p", "aut", "T", "slots", "fixed", "free", "site",
              "stab_geo", "brav", "n_ops", "n_proper", "detL", "vol"):
        a, b = rd["cubic_ref"][k], rd["hex"][k]
        if k == "code":
            a, b = ("== seed" if a == b else "DIFFERENT"), "== seed"
        if k == "p":
            a, b = pvec_compact(a), pvec_compact(b)
        cls = ("lattice-independent (must agree)" if k in
               ("code", "f", "p", "aut", "T", "slots", "fixed") else
               "metric-dependent (expected to differ, explained above)")
        L.append(f"| {k} | {a} | {b} | {cls} |")
    L.append("")

    # ---- summary table
    recs = sorted(records, key=lambda r: r["rank"])
    L += ["## Summary table (all survivors, collision-screen rank order)", "",
          "| # | id | IT | c/a | f | aut | V0 | V1 gen | V1 audit | V2 | V3 | "
          "chiral? | site = Isom? | \\|H/L\\| = T·\\|site\\|? | open/wall "
          "(carried from triage) | wall |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    per_rung = {k: Counter() for k in ("V0", "V1 gen", "V1 audit", "V2", "V3")}
    for r in recs:
        vd = {}
        for st in r["stages"]:
            key = ("V0" if st["name"].startswith("V0") else
                   "V1 gen" if "generator" in st["name"] else
                   "V1 audit" if "audit" in st["name"] else
                   "V2" if st["name"].startswith("V2") else "V3")
            vd[key] = st["verdict"]
        for key in per_rung:
            per_rung[key][vd.get(key, "NOT REACHED")] += 1
        sy = r["sym"]
        chir = ("chiral" if sy["chiral"] else "achiral") if sy else "—"
        s_iso = ("yes" if sy["n_iso"] == sy["n_site"] else
                 f"NO ({sy['n_site']} vs {sy['n_iso']})") if sy else "—"
        hl = ("yes" if sy["full_is_G"] else
              f"NO ({sy['n_ops']} vs {r['lat']['T']*sy['n_site']})") if sy else "—"
        grp = f"{r['witness']['group']} {r['group_symbol']}"
        wall = f"{r['elapsed']:.0f}s"
        L.append(f"| {r['rank']} | `{r['cid']}` | {grp} | {r['witness']['b']} | "
                 f"{tuple(r['f_vector'])} | {r['aut_order']} | "
                 f"{vd.get('V0', 'NOT REACHED')} | {vd.get('V1 gen', 'NOT REACHED')} | "
                 f"{vd.get('V1 audit', 'NOT REACHED')} | {vd.get('V2', 'NOT REACHED')} | "
                 f"{vd.get('V3', 'NOT REACHED')} | {chir} | {s_iso} | {hl} | "
                 f"{r['label']} | {wall} |")
    L.append("")

    # ---- aggregate
    n = len(recs)
    allpass = all(st["verdict"] == "PASS" for r in recs for st in r["stages"]) \
        and all(len(r["stages"]) == 5 for r in recs) and complete and not fail_msgs
    n_pass = sum(1 for r in recs if len(r["stages"]) == 5
                 and all(st["verdict"] == "PASS" for st in r["stages"]))
    n_fail = sum(1 for r in recs if any(st["verdict"] == "FAIL" for st in r["stages"]))
    n_def = sum(1 for r in recs if any(st["verdict"].startswith("DEFERRED")
                                        or st["verdict"].startswith("PASS (over")
                                        for st in r["stages"]))
    syms = [r for r in recs if r["sym"]]
    chiral = [r for r in syms if r["sym"]["chiral"]]
    achiral = [r for r in syms if not r["sym"]["chiral"]]
    iso_gt_site = [r for r in syms if r["sym"]["n_iso"] > r["sym"]["n_site"]]
    fix_gt_site = [r for r in syms if r["sym"]["n_fix"] > r["sym"]["n_site"]]
    comb_only = [r for r in syms if r["sym"]["n_aut"] > r["sym"]["n_iso"]]
    not_full = [r for r in syms if not r["sym"]["full_is_G"]]
    brav = Counter(r["sym"]["n_brav"] for r in syms)
    reached = Counter(r["v3"]["indep"]["reached"] for r in recs
                      if r["v3"] and r["v3"].get("indep"))
    indep_def = [r for r in recs if r["v3"] and r["v3"].get("indep")
                 and r["v3"]["indep"]["reached"] < N_INDEP]
    maxF = max((r["f_vector"][2] for r in recs), default=0)
    hands = Counter()
    for r in recs:
        if r["v3"] and r["v3"].get("counts") and r["sym"]["chiral"]:
            hands[r["v3"]["n_other_hand"] == 0] += 1
    L += ["## Aggregate", "",
          f"- Survivors certified: {n} of {n_expected}"
          f"{'' if complete else ' (PARTIAL)'}; ALL FIVE RUNGS PASS: {n_pass}; "
          f"any FAIL: {n_fail}; any DEFERRED / over-cap: {n_def}.",
          "- Per-rung verdict counts: " + "; ".join(
              f"{k}: " + ", ".join(f"{v} {c}" for v, c in sorted(per_rung[k].items()))
              for k in per_rung) + ".",
          f"- Max facet count observed among the survivors: {maxF} (kill bar 38 "
          f"never approached; store menu max 24).",
          f"- Chirality of the solids: {len(chiral)} chiral, {len(achiral)} "
          f"achiral" + (" (" + ", ".join(f"#{r['rank']} `{r['cid']}`" for r in achiral)
                        + ")" if achiral else "") + ".",
          f"- Chiral honeycombs with all translation classes of one hand: "
          f"{hands[True]}; chiral solids with classes of BOTH hands present "
          f"(the honeycomb is achiral although the solid is chiral — its group "
          f"contains improper ops: inversion in R-3 / R-3c, the c-glide in "
          f"R3c): {hands[False]}" + (", by first-witness group: " + ", ".join(
              f"{k}: {v}" for k, v in sorted(Counter(
                  f"IT({r['witness']['group']}) {r['group_symbol']}"
                  for r in recs if r['v3'] and r['v3'].get('counts')
                  and r['sym']['chiral'] and r['v3']['n_other_hand'] > 0).items()))
              if hands[False] else "") + ".",
          f"- Isom(solid) > site symmetry: {len(iso_gt_site)} cell(s)"
          + (" — " + "; ".join(
              f"#{r['rank']} `{r['cid']}` IT({r['witness']['group']}) site "
              f"{r['sym']['n_site']}, Isom_fix_site {r['sym']['n_fix']}, "
              f"Isom(solid) {r['sym']['n_iso']} (Isom+ {r['sym']['n_proper']}), "
              f"aut {r['sym']['n_aut']}, |H/L| {r['sym']['n_ops']} vs T*|site| "
              f"{r['lat']['T']*r['sym']['n_site']} "
              f"({'full group = G' if r['sym']['full_is_G'] else 'full group LARGER than G'}); "
              f"double-check (fresh, in-worker): every listed isometry re-verified "
              f"G-orthogonal and vertex-permuting; per isometry "
              f"(det, fixes site, linear part in site group, maps site set to itself) = "
              + str([(d['det'], d['fixes_site'], d['linear_part_in_site_group'],
                      d['maps_site_set_to_itself'])
                     for d in r['sym'].get('double_check', [])])
              for r in iso_gt_site) if iso_gt_site else
             " (none — as in every earlier round of this program).") + ".",
          f"- Isom_fix_site > site symmetry: {len(fix_gt_site)} cell(s)"
          + (" — " + ", ".join(f"#{r['rank']} `{r['cid']}`" for r in fix_gt_site)
             if fix_gt_site else " (none).") + ".",
          f"- Combinatorial-only symmetry (aut > Isom(solid)): {len(comb_only)} "
          f"cell(s)" + (" — " + ", ".join(
              f"#{r['rank']} `{r['cid']}` (aut {r['sym']['n_aut']}, Isom "
              f"{r['sym']['n_iso']})" for r in comb_only) if comb_only else
              " (none).") + ".",
          f"- |H/L| != T*|site| (full symmetry group larger than the generating "
          f"group): {len(not_full)} cell(s)" + (" — " + ", ".join(
              f"#{r['rank']} `{r['cid']}` (|H/L| {r['sym']['n_ops']}, T*|site| "
              f"{r['lat']['T']*r['sym']['n_site']})" for r in not_full)
              if not_full else " (none: every honeycomb's full symmetry group "
              "is exactly its generating space group).") + ".",
          "- Generating-group identification (fresh check from the frozen ops, "
          "parent process: every hexagonal-family group whose orbit of the "
          "witness point equals the cell's site set; the largest point-op count "
          "|H_conv|/centering among them can never exceed the ladder's |H/L| — "
          "asserted for every cell — and equals it when the full group is in "
          f"the frozen list, directly or after an origin shift in (Z/P)^3): identified for "
          f"{sum(1 for r in recs if r.get('gen_groups', {}).get('identified'))} "
          f"of {n} cells" + (
              "; the cells with |H/L| > T*|site| are honeycombs of a SUPERGROUP "
              "of the first-witness group (the witness point is a special "
              "position whose orbit is the same set under the supergroup, where "
              "its site symmetry is larger): " + "; ".join(
                  f"#{r['rank']} `{r['cid']}` first witness IT({r['witness']['group']}) "
                  f"site {r['sym']['n_site']} -> full group "
                  + (" / ".join(f"IT({h['group']}) {h['symbol']}"
                                f"{' with origin shift ' + str(tuple(h['shift'])) if h.get('shift') else ''}"
                                f" (site symmetry {h['site']} there = |H/L|/T"
                                f"{' = Isom_fix_site' if h['site'] == r['sym']['n_fix'] else ''})"
                                for h in r['gen_groups']['full_groups'])
                     if r['gen_groups']['identified'] else
                     "NOT identified within the frozen list (no setting/shift tried reproduces the site set)")
                  + f"; store sightings in the full group: "
                  f"{r.get('sightings_in_full_group', 'n/a')}"
                  for r in not_full) if not_full else "") + ".",
          f"- Bravais point-group orders of the actual lattices in G: "
          + ", ".join(f"{k}: {v}" for k, v in sorted(brav.items()))
          + " (24 = hexagonal P lattice 6/mmm; 12 = rhombohedral R lattice -3m; "
          "no rational c/a makes either metrically cubic).",
          f"- Independent enumerator depth reached: "
          + ", ".join(f"n={k}: {v}" for k, v in sorted(reached.items()))
          + (f"; below n=5: " + ", ".join(
              f"#{r['rank']} `{r['cid']}` (n={r['v3']['indep']['reached']}, "
              f"{'cap' if r['v3']['indep']['timed_out'] else 'field'})"
              for r in indep_def) if indep_def else "") + ".",
          f"- Total wall time this doc: {total_s:.0f}s (sum of per-cell walls "
          f"{sum(r['elapsed'] for r in recs):.0f}s; cells ran {JOBS_USED} in "
          f"parallel, independent enumerator --workers {INDEP_WORKERS}).",
          ""]

    # ---- isometry summary table
    L += ["## Isometry vs site vs aut summary", "",
          "| # | id | IT | site | Isom_fix_site | Isom(solid) | Isom+ | solid | "
          "aut | \\|H/L\\| | T*site | full group = G | full group (frozen-list "
          "identification) | Bravais |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in syms:
        sy = r["sym"]
        gg = r.get("gen_groups") or {}
        ident = (" / ".join(f"{h['group']} {h['symbol']}"
                            f"{' (origin shift ' + str(tuple(h['shift'])) + ')' if h.get('shift') else ''}"
                            for h in gg["full_groups"])
                 if gg.get("identified") else "NOT identified in the frozen list")
        L.append(f"| {r['rank']} | `{r['cid']}` | {r['witness']['group']} | "
                 f"{sy['n_site']} | {sy['n_fix']} | {sy['n_iso']} | "
                 f"{sy['n_proper']} | {'chiral' if sy['chiral'] else 'achiral'} | "
                 f"{sy['n_aut']} | {sy['n_ops']} | {r['lat']['T']*sy['n_site']} | "
                 f"{'yes' if sy['full_is_G'] else 'NO'} | {ident} | {sy['n_brav']} |")
    L.append("")

    # ---- counts table
    L += ["## Counts reached (banked n<=4 == independent; independent to n<=5)",
          "", "| # | id | fixed (indep, n=1..reached) | free | one-sided | "
          "indep reached | indep wall |", "|---|---|---|---|---|---|---|"]
    for r in recs:
        if r["v3"] and r["v3"].get("indep"):
            ind = r["v3"]["indep"]
            ns = sorted(ind["rows"], key=int)
            L.append(f"| {r['rank']} | `{r['cid']}` | "
                     f"{[ind['rows'][k][0] for k in ns]} | "
                     f"{[ind['rows'][k][1] for k in ns]} | "
                     f"{[ind['rows'][k][2] for k in ns]} | {ind['reached']}"
                     f"{' (cap)' if ind['timed_out'] else ''} | {ind['wall']:.0f}s |")
    L.append("")

    # ---- per-cell detail
    L += ["## Per-cell certificates", ""]
    for r in recs:
        w = r["witness"]
        L.append(f"### #{r['rank']} `{r['cid']}` — IT({w['group']}) "
                 f"{r['group_symbol']}, f={tuple(r['f_vector'])}, "
                 f"p={r['p_compact']}, aut={r['aut_order']}")
        L.append("")
        L.append(f"Witness point ({', '.join(w['point'])}), c/a = {w['b']}, "
                 f"site stabilizer {w['stabilizer_order']}, orbit "
                 f"{w['orbit_conventional']} conventional / "
                 f"{w['orbit_primitive']} primitive, stratum dim "
                 f"{w['stratum_dim']}. Open/wall label (triage, carried): "
                 f"{r['label']}. Candidate wall time {r['elapsed']:.1f}s.")
        L.append("")
        L.append("| stage | verdict | wall | key numbers |")
        L.append("|---|---|---|---|")
        for st in r["stages"]:
            L.append(f"| {st['name']} | **{st['verdict']}** | {st['t']:.1f}s | "
                     f"{st['detail']} |")
        done = {st["name"].split()[0] for st in r["stages"]}
        for missing in ("V0", "V1", "V2", "V3"):
            if missing not in done:
                L.append(f"| {missing} | **NOT REACHED** | — | quarantined "
                         f"downstream of the failure above |")
        L.append("")
        sy = r["sym"]
        if sy:
            L.append(f"Symmetry reconciliation: site symmetry {sy['n_site']} <= "
                     f"Isom_fix_site {sy['n_fix']} <= Isom(solid) {sy['n_iso']} "
                     f"(Isom+ {sy['n_proper']}, solid "
                     f"{'chiral' if sy['chiral'] else 'achiral'}) <= combinatorial "
                     f"aut {sy['n_aut']} (containment + divisibility verified "
                     f"exactly; Gram-triple re-derivation agrees). Bravais point "
                     f"group of the actual lattice in G: order {sy['n_brav']}. "
                     f"Honeycomb point group |H/L| = {sy['n_ops']} "
                     f"({sy['n_ops_improper']} improper) vs T*|site| = "
                     f"{r['lat']['T']*sy['n_site']}: the full symmetry group of "
                     f"the honeycomb "
                     f"{'IS exactly the generating group G' if sy['full_is_G'] else 'is LARGER than G'}.")
            L.append("")

    # ---- deferrals / failures
    L += ["## Deferrals / failures", ""]
    items = list(fail_msgs)
    for r in recs:
        for st in r["stages"]:
            if st["verdict"] != "PASS":
                items.append(f"#{r['rank']} `{r['cid']}`: {st['name']} "
                             f"{st['verdict']} — {st['detail']}")
        if len(r["stages"]) < 5:
            items.append(f"#{r['rank']} `{r['cid']}`: ladder stopped after "
                         f"{len(r['stages'])} stage(s)")
    for r in indep_def:
        items.append(f"#{r['rank']} `{r['cid']}`: independent enumerator reached "
                     f"n={r['v3']['indep']['reached']} < {N_INDEP} "
                     f"({'cap' if r['v3']['indep']['timed_out'] else 'coordinate-field cap'})")
    L += [f"- {x}" for x in items] if items else ["- none"]
    L += ["", f"Total wall time {total_s:.0f}s. Deterministic except the timing "
          "columns (`--mask-timings` writes them as `<t>`; the md5 of the "
          "masked text is printed by the driver). Artifacts: "
          "`g4p2hex_tables_<id>.json` (+ `.txt` enumerator input, "
          "`_indep.json` independent-enumerator record) per cell; "
          "`g4p2hex_cells/<id>.json` per-cell records (resume boundary); "
          "`g4p2hex_control_*` for the sanity gates.", "",
          "Re-run for acceptance (see the docstring of `g4_certify_hex.py`): "
          "`PY=python3; "
          "cd <repo>/harness; "
          "$PY g4_certify_hex.py --fresh --budget-s 420; rc=$?; while [ $rc -eq 3 ]; "
          "do $PY g4_certify_hex.py --resume --budget-s 420; rc=$?; done; echo exit $rc` "
          "(exit 0 required).", ""]
    text = "\n".join(L)
    masked = mask_timings(text) + "\n"
    md5_masked = hashlib.md5(masked.encode()).hexdigest()   # == md5 of the
    tmp = RESULTS_MD + ".tmp"                                # --mask-timings file
    open(tmp, "w").write(masked if mask else text + "\n")
    os.replace(tmp, RESULTS_MD)
    return allpass, md5_masked


JOBS_USED = 0


def main(argv):
    global JOBS_USED, INDEP_WORKERS
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--gate-only", action="store_true")
    ap.add_argument("--fresh", action="store_true",
                    help="delete per-cell records and start over (runs gates)")
    ap.add_argument("--resume", action="store_true",
                    help="continue: skip cells with a record, reuse gate record")
    ap.add_argument("--jobs", type=int, default=5)
    ap.add_argument("--indep-workers", type=int, default=INDEP_WORKERS)
    ap.add_argument("--budget-s", type=float, default=420.0)
    ap.add_argument("--mask-timings", action="store_true")
    a = ap.parse_args(argv[1:])
    INDEP_WORKERS = a.indep_workers
    JOBS_USED = a.jobs
    say = print
    t0 = time.time()

    sha = sha256_file(STORE_HEX)
    assert sha == STORE_HEX_SHA256, f"store sha256 drift: {sha}"
    say(f"store sha256 verified: {sha}")
    store_all = json.load(open(STORE_HEX))
    store = store_all["types"]
    assert store_all["catalog_snapshot"] == SNAPSHOT
    groups = orbit.load_groups()
    seeds = json.load(open(SEEDS))["entries"]
    tri = json.load(open(TRIAGE_JSON))
    assert tri["store_sha256"] == STORE_HEX_SHA256
    survivors = tri["survivors_ranked"]
    assert len(survivors) == 151 and len(set(survivors)) == 151
    labels = load_triage_labels()
    for cid in survivors:
        assert labels[cid]["verdict"] == "SURVIVOR", cid
    for r, cid in enumerate(tri["top10_survivors"], 1):
        assert survivors[r - 1] == cid["id"] and labels[cid["id"]]["ow"] == cid["ow"]

    os.makedirs(CELL_DIR, exist_ok=True)
    if a.gate_only or a.fresh or not a.resume:
        if a.fresh and not a.gate_only:
            for fn in os.listdir(CELL_DIR):
                os.remove(os.path.join(CELL_DIR, fn))
        gate = run_gates(groups, seeds, say)
        json.dump(gate, open(GATE_RECORD, "w"), indent=1)
        say(f"gates: ALL PASS ({time.time()-t0:.0f}s)")
        if a.gate_only:
            say("gate-only run: PASS")
            return 0
    else:
        assert os.path.exists(GATE_RECORD), "no gate record: run with --fresh first"
        gate = json.load(open(GATE_RECORD))
        say("gates: reusing the gate record of this run (--resume)")

    ids = a.ids or survivors
    rank_of = {cid: i + 1 for i, cid in enumerate(survivors)}
    records, pending = [], []
    for cid in ids:
        assert cid in store and cid in rank_of, f"not a survivor: {cid}"
        rec_path = os.path.join(CELL_DIR, f"{cid}.json")
        if a.resume and os.path.exists(rec_path):
            records.append(json.load(open(rec_path)))
        else:
            pending.append((rank_of[cid], cid, store[cid],
                            store[cid]["first_witness"], labels[cid]["label"]))
    pending.sort()
    say(f"{len(records)} cell(s) already recorded, {len(pending)} pending; "
        f"jobs={a.jobs}, indep workers={INDEP_WORKERS}, budget {a.budget_s:.0f}s")

    fail_msgs, complete = [], True
    if pending:
        with ProcessPoolExecutor(max_workers=a.jobs, initializer=_init,
                                 initargs=(INDEP_WORKERS, INDEP_CAP_S)) as ex:
            futs = {ex.submit(_work, job): job for job in pending}
            stopped = False
            for fut in as_completed(futs):
                if fut.cancelled():
                    continue
                job = futs[fut]
                try:
                    rec = fut.result()
                except Exception:
                    tb = traceback.format_exc().strip().splitlines()[-1]
                    fail_msgs.append(f"#{job[0]} `{job[1]}`: worker crashed — {tb}")
                    say(f"!! #{job[0]} {job[1]}: WORKER CRASH {tb}")
                    ex.shutdown(wait=False, cancel_futures=True)
                    stopped = True
                    continue
                rec_path = os.path.join(CELL_DIR, f"{rec['cid']}.json")
                with open(rec_path + ".tmp", "w") as fh:      # never half-written
                    json.dump(rec, fh, indent=1)
                os.replace(rec_path + ".tmp", rec_path)
                records.append(rec)
                vds = [st["verdict"] for st in rec["stages"]]
                say(f"[{len(records)}/{len(ids)}] #{rec['rank']} {rec['cid']} "
                    f"IT({rec['witness']['group']}) f={tuple(rec['f_vector'])}: "
                    f"{' '.join(vds)} ({rec['elapsed']:.0f}s)")
                if any(v != "PASS" for v in vds) or len(vds) < 5:
                    bad = [st for st in rec["stages"] if st["verdict"] != "PASS"]
                    msg = (f"#{rec['rank']} `{rec['cid']}`: "
                           + "; ".join(f"{st['name']} {st['verdict']} — {st['detail']}"
                                       for st in bad))
                    fail_msgs.append(msg)
                    say(f"!! V-RUNG FAIL — batch stopped: {msg}")
                    if not stopped:
                        ex.shutdown(wait=False, cancel_futures=True)
                        stopped = True
                elif not stopped and time.time() - t0 > a.budget_s:
                    say(f"-- budget {a.budget_s:.0f}s reached: no new cells "
                        f"submitted, finishing the running ones")
                    ex.shutdown(wait=False, cancel_futures=True)
                    stopped = True
    have = {r["cid"] for r in records}
    complete = all(cid in have for cid in ids)
    t_gg = time.time()
    for rec in records:
        if rec["sym"] is None:
            continue
        rec["gen_groups"] = generating_group_check(rec, groups)
        if not rec["sym"]["full_is_G"] and rec["gen_groups"]["identified"]:
            fg = {h["group"] for h in rec["gen_groups"]["full_groups"]}
            rec["sightings_in_full_group"] = sum(
                1 for x in store[rec["cid"]]["sightings"] if x["group"] in fg)
        rec_path = os.path.join(CELL_DIR, f"{rec['cid']}.json")
        with open(rec_path + ".tmp", "w") as fh:
            json.dump(rec, fh, indent=1)
        os.replace(rec_path + ".tmp", rec_path)
    say(f"generating-group check (frozen ops) on {len(records)} cell(s): "
        f"{sum(1 for r in records if r.get('gen_groups', {}).get('identified'))} "
        f"identified, {sum(1 for r in records if r['sym'] and not r['sym']['full_is_G'])} "
        f"with a full group larger than the first-witness group "
        f"({time.time()-t_gg:.0f}s)")
    allpass, md5m = write_results(gate, records, time.time() - t0, complete,
                                  a.mask_timings, fail_msgs, len(ids))
    say(f"\nwrote {os.path.basename(RESULTS_MD)} ({len(records)}/{len(ids)} cells"
        f"{', COMPLETE' if complete else ', PARTIAL'}); md5 with timings masked: "
        f"{md5m}")
    if fail_msgs:
        say(f"G4 PHASE-2 HEX VERDICT: FAIL — batch stopped ({time.time()-t0:.0f}s)")
        return 1
    if not complete:
        say(f"G4 PHASE-2 HEX: INCOMPLETE — resume with --resume "
            f"({time.time()-t0:.0f}s)")
        return 3
    say(f"G4 PHASE-2 HEX VERDICT: {'ALL STAGES PASS' if allpass else 'FAIL/DEFERRED'} "
        f"({time.time()-t0:.0f}s)")
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
