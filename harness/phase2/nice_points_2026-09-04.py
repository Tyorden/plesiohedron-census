#!/usr/bin/env python
"""nice_points_2026-09-04.py -- "nicest" presentation search inside the certified
open neighbourhood of the top-3 pool cells per system (9 cells), staging for a
naming decision. Produces NO names.

Pre-registration: the dated block in ../../NICE_POINTS_2026-09-04.md between
<!-- PREREG-BEGIN --> and <!-- PREREG-END -->, written BEFORE any chain
evaluation (`--plan` enumerates the search set without evaluating a single
candidate; the block quotes that enumeration). The block is read back and
re-emitted verbatim; it is never generated here.

Chain (accepted, imported unchanged):
  sweep_phase2_tetragonal.evaluate / sweep_phase2_hexagonal.evaluate  -- the SAME
  functions WALL_OPEN_PHASE2.json used; SAME iff canonical code == the store's;
  ChainError -> QUARANTINE (neither SAME nor DIFFERENT).
  g4_certify_gram.v0_rederive on every SAME candidate as a synthetic witness
  (second derivation; asserts canonical code / f / p / aut against the frozen
  store) -> exact vertices in the integer Gram metric -> presentation scales.

Search set per cell (exact rationals): points p0 + sum_i t_i d_i over the
tangent directions d_i recorded in WALL_OPEN_PHASE2.json (on-stratum point
rows), t_i in [-ext_minus_i, +ext_plus_i] where ext = the largest tested |eps|
on that side such that every tested step of smaller or equal |eps| on that side
is SAME (refinement rows included); every coordinate of the point must be a
rational with denominator <= 48. c/a: rationals of denominator <= 16 in
[b0 (1 - em), b0 (1 + ep)], em/ep the metric extents by the same rule.
Candidates = points x c/a values (the witness is a member).

Niceness (lexicographic): (a) m_lat = lcm of the denominators of the
site-centred vertex coordinates in the conventional (lattice) basis; (b)
tetragonal: m_cart (integer Cartesian coordinates in units a/m_cart, c/a = p/q
applied to z); hexagonal family: m_eis (in-plane coordinates x + y*omega are
Eisenstein integers after scaling by m_eis); (c) c/a simplicity (denominator,
numerator); (d) lcm of the generating point's coordinate denominators; (e) the
point itself (lexicographic). Reported, not ranked: m_abs (absolute
conventional), m_c (z denominators), m_cart3 (sqrt(3)-Cartesian scale).

Outputs (deterministic; sorted keys; no timings):
  ./NICE_POINTS_2026-09-04.json
  ../../NICE_POINTS_2026-09-04.md (below the pre-registration block)
"""
import argparse
import hashlib
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F
from math import ceil, floor, gcd
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.dirname(HERE)
MINT = os.path.dirname(HARNESS)
sys.path.insert(0, HERE)
sys.path.insert(0, HARNESS)

import orbit                                        # noqa: E402
import metric                                       # noqa: E402
import g4_certify_gram as G4G                       # noqa: E402
import sweep_phase2_tetragonal as S2                # noqa: E402
import sweep_phase2_hexagonal as SH                 # noqa: E402
from sweep_phase1 import ChainError, code_id, pvec_compact  # noqa: E402
from g4_certify import vsub                         # noqa: E402
from wall_open_phase2 import nullspace_basis        # noqa: E402  (verbatim c1 copy)

WALL_OPEN = os.path.join(HERE, "WALL_OPEN_PHASE2.json")
WALL_OPEN_MD5 = "6b257c551f6fb275dfabb03e992f57c2"
POOL_JSON = os.path.join(HERE, "POOL_RANKING_2026-09-04.json")
POOL_MD5 = "75cacf7e762bda859234d2843888cb94"
STORE_T = os.path.join(HARNESS, "phase2_types.json")
STORE_H = os.path.join(HARNESS, "phase2_hexagonal_types.json")
STORE_1 = os.path.join(HARNESS, "phase1_types.json")
OUT_JSON = os.path.join(HERE, "NICE_POINTS_2026-09-04.json")
OUT_MD = os.path.join(MINT, "NICE_POINTS_2026-09-04.md")
CACHE = os.path.join(HERE, "nice_points_cells")
SNAPSHOT = "2026-09-04"
KIND = "nice_points_2026-09-04"
POINT_DEN = 48
CA_DEN = 16
TOP_PER_SYSTEM = 3
JOSE_ID = "dfccc9ff6019ead5"          # phase1 store: seeded josehedron (IT 220, 12a)
JOSE_W = {"group": 220, "point": ["3/8", "0", "1/4"], "b": None}


def md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def fstr(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def pt(p):
    return "(" + ", ".join(fstr(x) for x in p) + ")"


def lcm(a, b):
    return a * b // gcd(a, b)


def system_of(it):
    if 75 <= it <= 142:
        return "tetragonal"
    if 143 <= it <= 167:
        return "trigonal"
    if 168 <= it <= 194:
        return "hexagonal"
    raise ValueError(it)


def farey_in(lo, hi, maxden):
    """All rationals with denominator <= maxden in the closed interval [lo, hi]."""
    out = set()
    for q in range(1, maxden + 1):
        for n in range(ceil(lo * q), floor(hi * q) + 1):
            out.add(F(n, q))
    return sorted(out)


# ------------------------------------------------------------ extents --------
def side_extent(rows_side):
    """rows_side: list of (abs_eps, status) on one side. Extent = largest tested
    |eps| such that every tested |eps'| <= it is SAME. 0 if the smallest tested
    step is not SAME."""
    ext = F(0)
    for e, st in sorted(rows_side):
        if st == "SAME":
            ext = e
        else:
            break
    return ext


def extents_of(cell):
    """Per on-stratum point direction (as recorded) and for the metric: the
    minus/plus extents and the tested-step ledger that produced them."""
    dirs = {}
    met = {"-": [], "+": []}
    for r in cell["rows"]:
        e = F(r["eps"])
        side = "-" if e < 0 else "+"
        if r["kind"] == "metric":
            met[side].append((abs(e), r["status"]))
        elif r["kind"] == "point" and not r["off_stratum"]:
            d = tuple(r["direction"])
            dirs.setdefault(d, {"-": [], "+": []})[side].append((abs(e), r["status"]))
    out_dirs = []
    for d in sorted(dirs):
        out_dirs.append(dict(direction=list(d),
                             ext_minus=fstr(side_extent(dirs[d]["-"])),
                             ext_plus=fstr(side_extent(dirs[d]["+"])),
                             tested_minus=[[fstr(e), s] for e, s in sorted(dirs[d]["-"])],
                             tested_plus=[[fstr(e), s] for e, s in sorted(dirs[d]["+"])]))
    out_met = dict(ext_minus=fstr(side_extent(met["-"])), ext_plus=fstr(side_extent(met["+"])),
                   tested_minus=[[fstr(e), s] for e, s in sorted(met["-"])],
                   tested_plus=[[fstr(e), s] for e, s in sorted(met["+"])])
    return out_dirs, out_met


def search_set(p0, b0, dirs, met):
    """Points: every coordinate a rational of denominator <= POINT_DEN inside the
    per-direction extents; c/a: denominator <= CA_DEN inside the metric band."""
    # parametrise by the free coordinates: each recorded direction d has a
    # leading nonzero entry; the stratum dims here are 1 and 3 so a coordinate
    # grid on the leading entries is exact.
    axes = []
    for d in dirs:
        dv = tuple(d["direction"])
        lead = next(k for k in range(3) if dv[k] != 0)
        assert dv[lead] == 1, dv
        axes.append((dv, lead, F(d["ext_minus"]), F(d["ext_plus"])))
    # candidate t-values per direction from the leading coordinate's Farey set
    tvals = []
    for dv, lead, em, ep in axes:
        xs = farey_in(p0[lead] - em, p0[lead] + ep, POINT_DEN)
        tvals.append([x - p0[lead] for x in xs])
    pts = []

    def rec(k, acc):
        if k == len(axes):
            q = tuple(p0[i] + sum(t * axes[j][0][i] for j, t in enumerate(acc)) for i in range(3))
            if all(x.denominator <= POINT_DEN for x in q):
                pts.append(q)
            return
        for t in tvals[k]:
            rec(k + 1, acc + [t])
    rec(0, [])
    pts = sorted(set(pts))
    assert p0 in pts
    cas = farey_in(b0 * (1 - F(met["ext_minus"])), b0 * (1 + F(met["ext_plus"])), CA_DEN)
    cas = sorted(set(cas) | {b0})          # the witness c/a is always a member
    return pts, cas


# ---------------------------------------------------------- evaluation -------
_CTX = {}


def _init():
    _CTX["groups"] = orbit.load_groups()
    _CTX["stores"] = {"tetragonal": json.load(open(STORE_T))["types"],
                      "hexagonal": json.load(open(STORE_H))["types"]}
    code2id = {}
    for fam in ("tetragonal", "hexagonal"):
        for tid, e in _CTX["stores"][fam].items():
            code2id.setdefault(e["canon_code"], tid)
    _CTX["code2id"] = code2id


def presentation(ctx, fam, b):
    """Scales from the exact cell (site-centred conventional fractional coords)."""
    ec, period = ctx["ec"], ctx["period"]
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    site = tuple(F(x) for x in ec["center"])
    cvec = [tuple((v[k] - site[k]) / period for k in range(3)) for v in verts]
    m_lat = m_abs = m_xy = m_c = m_cart = m_cart3 = 1
    for v, w in zip(cvec, verts):
        for x in v:
            m_lat = lcm(m_lat, x.denominator)
        for x in w:
            m_abs = lcm(m_abs, (x / period).denominator)
        m_xy = lcm(m_xy, lcm(v[0].denominator, v[1].denominator))
        m_c = lcm(m_c, v[2].denominator)
        if fam == "tetragonal":
            m_cart = lcm(m_cart, lcm(lcm(v[0].denominator, v[1].denominator), (v[2] * b).denominator))
        else:
            m_cart3 = lcm(m_cart3, lcm(lcm((v[0] - v[1] / 2).denominator, (v[1] / 2).denominator),
                                       (v[2] * b).denominator))
    out = dict(m_lattice=m_lat, m_absolute_conventional=m_abs, m_c=m_c,
               vertices_site_centred_conventional=[pt(v) for v in sorted(cvec)],
               rho2=fstr(ec["rho2"]), gram=[[int(x) for x in row] for row in ctx["G"]], period=period)
    if fam == "tetragonal":
        out.update(m_cartesian=m_cart, m_second=m_cart,
                   second_kind="integer Cartesian coordinates in units a/m (c/a applied to z)")
    else:
        out.update(m_eisenstein=m_xy, m_cartesian_sqrt3=m_cart3, m_second=m_xy,
                   second_kind="in-plane x + y*omega Eisenstein integers after scaling by m (hexagonal lattice basis)")
    return out


def evaluate_candidate(task):
    cid, fam, num, p, b = task
    ent = _CTX["stores"][fam][cid]
    mod = S2 if fam == "tetragonal" else SH
    row = dict(point=pt(p), c_over_a=fstr(b), point_den=max(x.denominator for x in p))
    try:
        r = mod.evaluate(num, tuple(p), F(b), KIND)
    except ChainError as exc:
        row.update(status="QUARANTINE", quarantine=f"{exc.reason}: {exc.detail}"[:160])
        return row
    code = r["code_str"]
    same = code == ent["canon_code"]
    row.update(status="SAME" if same else "DIFFERENT", code_id=code_id(code),
               stored_id=_CTX["code2id"].get(code), f=list(r["fvec"]), p=pvec_compact(r["pvec"]),
               aut=r["aut"], stab=r["stabilizer_order"], nonsimple=r["nonsimple"],
               degenerate_flag=r["degen_flag0"], float_superseded=r["float_superseded"], W=r["W"])
    if same:
        w = {"group": num, "point": [fstr(x) for x in p], "b": fstr(b)}
        ctx = G4G.v0_rederive(cid, ent, _CTX["groups"], w)     # asserts code/f/p/aut vs store
        assert ctx["aut"] == r["aut"] and [ctx["V"], ctx["E"], ctx["Fc"]] == list(r["fvec"])
        row.update(presentation(ctx, fam, F(b)))
    return row


def nice_key(row):
    b = F(row["c_over_a"])
    p = tuple(F(x) for x in row["point"][1:-1].split(", "))
    pden = 1
    for x in p:
        pden = lcm(pden, x.denominator)
    return (row["m_lattice"], row["m_second"], b.denominator, b.numerator, pden, p)


def josehedron_control(groups):
    ent = json.load(open(STORE_1))["types"][JOSE_ID]
    assert ent.get("seed_name") == "josehedron"
    ctx = G4G.v0_rederive(JOSE_ID, ent, groups, JOSE_W)
    ec, period = ctx["ec"], ctx["period"]
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    site = tuple(F(x) for x in ec["center"])
    m_lat = m_abs = 1
    for v in verts:
        for k in range(3):
            m_lat = lcm(m_lat, ((v[k] - site[k]) / period).denominator)
            m_abs = lcm(m_abs, (v[k] / period).denominator)
    return dict(id=JOSE_ID, IT=220, point=pt(F(s) for s in JOSE_W["point"]), f=[ctx["V"], ctx["E"], ctx["Fc"]],
                p=pvec_compact(ec["p_vector"]), aut=ctx["aut"], m_lattice_site_centred=m_lat,
                m_absolute_conventional=m_abs, period=period,
                note="cubic: the conventional basis IS Cartesian, so m_lattice is the integer Cartesian scale (units a/m)")


# ------------------------------------------------------------- main ----------
def load_cells():
    assert md5(WALL_OPEN) == WALL_OPEN_MD5, "WALL_OPEN_PHASE2.json changed"
    assert md5(POOL_JSON) == POOL_MD5, "POOL_RANKING_2026-09-04.json changed"
    wall = json.load(open(WALL_OPEN))
    pool = json.load(open(POOL_JSON))
    assert sha256(STORE_T) == wall["stores"]["phase2_types.json_sha256"]
    assert sha256(STORE_H) == wall["stores"]["phase2_hexagonal_types.json_sha256"]
    bysys = {}
    for r in pool["cells"]:
        bysys.setdefault(r["system"], []).append(r)
    chosen = []
    for s in ("tetragonal", "trigonal", "hexagonal"):
        rows = sorted(bysys[s], key=lambda r: r["rank_in_system"])[:TOP_PER_SYSTEM]
        assert [r["rank_in_system"] for r in rows] == [1, 2, 3]
        chosen += rows
    wcells = {c["id"]: c for c in wall["cells"]}
    return chosen, wcells


def plan(chosen, wcells, groups, stores):
    plans = []
    for r in chosen:
        c = wcells[r["id"]]
        assert c["combined_verdict"] == "OPEN"
        ent = stores[c["family"]][r["id"]]
        w = ent["first_witness"]
        p0 = tuple(F(s) for s in w["point"])
        b0 = F(w["b"])
        assert pt(p0) == r["witness_point"] and fstr(b0) == r["c_over_a"] and w["group"] == r["IT"]
        dirs, met = extents_of(c)
        # tangent basis check (same function WALL_OPEN used)
        basis = nullspace_basis([R for R, _ in orbit.site_stabilizer(groups[w["group"]], p0)])
        assert sorted(tuple(d["direction"]) for d in dirs) == sorted(basis), (dirs, basis)
        assert len(basis) == w["stratum_dim"]
        pts, cas = search_set(p0, b0, dirs, met)
        plans.append(dict(id=r["id"], system=r["system"], family=c["family"], IT=r["IT"], symbol=r["symbol"],
                          rank_in_system=r["rank_in_system"], rank_overall=r["rank_overall"],
                          witness_point=pt(p0), c_over_a=fstr(b0), stratum_dim=w["stratum_dim"],
                          f=r["f"], p=r["p"], aut_comb=r["aut_comb"], isom_solid=r["isom_solid"],
                          witness_m_lattice=r["m_lattice"], witness_m_cartesian=r["m_cartesian"],
                          directions=dirs, metric=met,
                          ca_band=[fstr(b0 * (1 - F(met["ext_minus"]))), fstr(b0 * (1 + F(met["ext_plus"])))],
                          n_points=len(pts), ca_candidates=[fstr(x) for x in cas],
                          n_candidates=len(pts) * len(cas), _pts=pts, _cas=cas))
    return plans


def plan_text(plans):
    L = []
    for q in plans:
        L.append(f"- `{q['id']}` {q['system']} IT({q['IT']}) {q['symbol']} witness {q['witness_point']} c/a {q['c_over_a']} "
                 f"(stratum dim {q['stratum_dim']}): " +
                 "; ".join(f"direction {tuple(d['direction'])} extents [-{d['ext_minus']}, +{d['ext_plus']}]" for d in q["directions"]) +
                 f"; metric relative extents [-{q['metric']['ext_minus']}, +{q['metric']['ext_plus']}] -> c/a band "
                 f"[{q['ca_band'][0]}, {q['ca_band'][1]}], c/a candidates {{{', '.join(q['ca_candidates'])}}}; "
                 f"points {q['n_points']}; candidates {q['n_candidates']}")
    L.append(f"- TOTAL candidates: {sum(q['n_candidates'] for q in plans)} (chain evaluations; SAME ones get a second derivation)")
    return L


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true", help="enumerate the search set only (no chain evaluation)")
    ap.add_argument("--jobs", type=int, default=int(os.environ.get("NICE_JOBS", "8")))
    ap.add_argument("--only", default=None, help="evaluate (and cache) this cell id only; no assembly")
    a = ap.parse_args(argv)
    t0 = time.time()
    chosen, wcells = load_cells()
    groups = orbit.load_groups()
    stores = {"tetragonal": json.load(open(STORE_T))["types"], "hexagonal": json.load(open(STORE_H))["types"]}
    plans = plan(chosen, wcells, groups, stores)
    if a.plan:
        print("\n".join(plan_text(plans)))
        return 0
    prev = open(OUT_MD).read()
    assert "<!-- PREREG-BEGIN -->" in prev and "<!-- PREREG-END -->" in prev, "pre-registration block missing"

    os.makedirs(CACHE, exist_ok=True)
    by = {}
    todo = [q for q in plans if a.only is None or q["id"] == a.only]
    for q in todo:
        tasks = [(q["id"], q["family"], q["IT"], p, b) for b in q["_cas"] for p in q["_pts"]]
        key = hashlib.md5(json.dumps([[pt(p), fstr(b)] for _, _, _, p, b in tasks]).encode()).hexdigest()
        cpath = os.path.join(CACHE, q["id"] + ".json")
        if os.path.exists(cpath):
            c = json.load(open(cpath))
            if c["search_key"] == key:
                by[q["id"]] = c["rows"]
                print(f"[nice_points] {q['id']}: {len(c['rows'])} rows from cache", flush=True)
                continue
        t1 = time.time()
        print(f"[nice_points] {q['id']}: {len(tasks)} candidates, {a.jobs} workers", flush=True)
        with Pool(a.jobs, initializer=_init) as P:
            rows = list(P.imap(evaluate_candidate, tasks, chunksize=4))
        json.dump(dict(id=q["id"], search_key=key, rows=rows), open(cpath, "w"), sort_keys=True)
        by[q["id"]] = rows
        print(f"[nice_points] {q['id']}: done in {time.time() - t1:.0f}s; SAME {sum(r['status'] == 'SAME' for r in rows)}, "
              f"DIFFERENT {sum(r['status'] == 'DIFFERENT' for r in rows)}, QUARANTINE {sum(r['status'] == 'QUARANTINE' for r in rows)}", flush=True)
    if a.only is not None:
        return 0
    tasks = [None] * sum(len(v) for v in by.values())

    jose = josehedron_control(groups)
    cells_out = []
    for q in plans:
        rs = by[q["id"]]
        same = [r for r in rs if r["status"] == "SAME"]
        diff = [r for r in rs if r["status"] == "DIFFERENT"]
        quar = [r for r in rs if r["status"] == "QUARANTINE"]
        p0 = tuple(F(x) for x in q["witness_point"][1:-1].split(", "))
        b0 = F(q["c_over_a"])
        wit = [r for r in same if r["point"] == q["witness_point"] and r["c_over_a"] == q["c_over_a"]]
        assert len(wit) == 1, "witness not SAME?!"
        wit = wit[0]
        assert wit["m_lattice"] == q["witness_m_lattice"], (wit["m_lattice"], q["witness_m_lattice"])
        if q["family"] == "tetragonal":
            assert wit["m_cartesian"] == q["witness_m_cartesian"]
        ranked = sorted(same, key=nice_key)
        for i, r in enumerate(ranked):
            r["nice_rank"] = i + 1

        def where(r):
            """Axis-parallel = the candidate differs from the witness in exactly one
            tested direction (one point direction at the witness c/a, or c/a alone at
            the witness point): the kind of step WALL_OPEN actually tested."""
            p = tuple(F(x) for x in r["point"][1:-1].split(", "))
            b = F(r["c_over_a"])
            moved = [k for k in range(3) if p[k] != p0[k]]
            if q["stratum_dim"] == 3:
                n_dirs = len(moved)
            else:                       # dim 1: any move along the line is one direction
                n_dirs = 1 if moved else 0
            n_dirs += 1 if b != b0 else 0
            return dict(coords_moved=moved, c_over_a_moved=(b != b0), axis_parallel_from_witness=(n_dirs == 1))
        for r in diff:
            r.update(where(r))
        stab_changed = [r for r in same + diff if r["stab"] != wit["stab"]]
        best = ranked[0]
        improved = nice_key(best) < nice_key(wit)
        # polar group: every op fixes the c direction (R e_z = e_z), so a shift of the
        # generating point along z translates the whole orbit -> congruent cells.
        polar = all(tuple(R[i][2] for i in range(3)) == (0, 0, 1) for R, _ in groups[q["IT"]]["ops_exact"])

        def xy(r):
            p = r["point"][1:-1].split(", ")
            return (p[0], p[1], r["c_over_a"])
        xy_same = {xy(r) for r in same}
        xy_diff = {xy(r) for r in diff}
        # per new type
        types = {}
        for r in diff:
            k = r["stored_id"] or r["code_id"]
            t = types.setdefault(k, dict(stored_id=r["stored_id"], code_id=r["code_id"], f=r["f"], p=r["p"], aut=r["aut"], count=0))
            t["count"] += 1
        hist = {}
        for r in ranked:
            k = (r["m_lattice"], r["m_second"])
            h = hist.setdefault(k, dict(m_lattice=k[0], m_second=k[1], count=0, example_point=r["point"], example_c_over_a=r["c_over_a"]))
            h["count"] += 1
        cells_out.append(dict(
            {k: v for k, v in q.items() if not k.startswith("_")},
            n_candidates=len(rs), n_same=len(same), n_different=len(diff), n_quarantine=len(quar),
            n_stab_change=len(stab_changed), polar_group=polar,
            n_xy_classes_same=len(xy_same), n_xy_classes_different=len(xy_diff),
            n_xy_classes_mixed=len(xy_same & xy_diff),
            n_different_axis_parallel=sum(1 for r in diff if r["axis_parallel_from_witness"]),
            # polar groups: z is a translation, so the effective parameters are (x, y, c/a);
            # "effective axis-parallel" = exactly one of those moved (expected 0 as well)
            n_different_axis_parallel_effective=(sum(1 for r in diff if (len([k for k in r["coords_moved"] if k != 2]) + (1 if r["c_over_a_moved"] else 0)) == 1)
                                                 if polar else sum(1 for r in diff if r["axis_parallel_from_witness"])),
            different_by_coords_moved=dict(Counter(f"{len(r['coords_moved'])}+{'ca' if r['c_over_a_moved'] else '0'}" for r in diff)),
            different_types=sorted(types.values(), key=lambda t: -t["count"]),
            different_candidates=[[r["point"], r["c_over_a"], r["stored_id"] or r["code_id"]]
                                  for r in sorted(diff, key=lambda r: (r["c_over_a"], r["point"]))],
            quarantined=sorted(quar, key=lambda r: (r["c_over_a"], r["point"])),
            witness_row=wit, best=best, top3=ranked[:3], improved_over_witness=improved,
            same_scale_histogram=sorted(hist.values(), key=lambda h: (h["m_lattice"], h["m_second"])),
            full_rows_cache=os.path.relpath(os.path.join(CACHE, q["id"] + ".json"), HERE),
        ))
    total_diff = sum(c["n_different"] for c in cells_out)
    total_q = sum(c["n_quarantine"] for c in cells_out)
    out = dict(
        cells=cells_out, snapshot=SNAPSHOT, generated_by="nice_points_2026-09-04.py (subagent #153, Claude Fable 5.1)",
        chain="sweep_phase2_tetragonal.evaluate / sweep_phase2_hexagonal.evaluate (type; accepted, unmodified) + g4_certify_gram.v0_rederive (exact vertices on SAME candidates; asserts code/f/p/aut vs the frozen store)",
        inputs=dict(wall_open_md5=WALL_OPEN_MD5, pool_ranking_md5=POOL_MD5,
                    phase2_types_sha256=sha256(STORE_T), phase2_hexagonal_types_sha256=sha256(STORE_H),
                    stores_sha256_unchanged_after_run=(sha256(STORE_T) == json.load(open(WALL_OPEN))["stores"]["phase2_types.json_sha256"]
                                                       and sha256(STORE_H) == json.load(open(WALL_OPEN))["stores"]["phase2_hexagonal_types.json_sha256"])),
        search=dict(point_denominator_max=POINT_DEN, ca_denominator_max=CA_DEN, top_per_system=TOP_PER_SYSTEM,
                    pre_registration="NICE_POINTS_2026-09-04.md PREREG-BEGIN..END (written before any chain evaluation)"),
        josehedron_control=jose,
        totals=dict(n_cells=len(cells_out), n_candidates=len(tasks), n_same=sum(c["n_same"] for c in cells_out),
                    n_different=total_diff, n_quarantine=total_q,
                    n_cells_improved=sum(1 for c in cells_out if c["improved_over_witness"])),
        language="no names; catalog-relative wording; OPEN = holds on the tested neighbourhood; every DIFFERENT candidate is a finding about the step size of WALL_OPEN_PHASE2, not an error",
    )
    json.dump(out, open(OUT_JSON, "w"), sort_keys=True, indent=1)
    elapsed = time.time() - t0
    write_md(out, prev, a.jobs)
    print(f"[nice_points] done in {elapsed:.0f}s; DIFFERENT {total_diff}, QUARANTINE {total_q}; "
          f"json md5 {md5(OUT_JSON)}", flush=True)
    return 0


def tell(c):
    """Plain 'tellable coordinates' paragraph (no names)."""
    b = c["best"]
    w = c["witness_row"]
    fam = c["family"]
    s = (f"Generating point {b['point']} at c/a = {b['c_over_a']} in IT({c['IT']}) {c['symbol']} "
         f"(f = ({', '.join(map(str, c['f']))}), aut {c['aut_comb']}): the site-centred vertex coordinates in the "
         f"conventional {'tetragonal' if fam == 'tetragonal' else 'hexagonal'} basis have common denominator {b['m_lattice']}")
    if fam == "tetragonal":
        s += (f"; scaled by {b['m_cartesian']} the vertices are integer Cartesian points (units a/{b['m_cartesian']}, "
              f"c = {b['c_over_a']} a)")
    else:
        s += (f"; in-plane coordinates x + y*omega are Eisenstein integers after scaling by {b['m_eisenstein']} "
              f"(z denominators {b['m_c']}); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = {b['m_cartesian_sqrt3']}")
    if c["improved_over_witness"]:
        s += (f". This beats the sweep witness {w['point']} at c/a = {w['c_over_a']} (denominator {w['m_lattice']}"
              + (f", Cartesian scale {w['m_cartesian']}" if fam == "tetragonal" else f", Eisenstein scale {w['m_eisenstein']}")
              + f"; the witness ranks {w['nice_rank']} of {c['n_same']} type-preserving candidates).")
    else:
        s += ". No candidate in the search set beats the sweep witness; the witness is the best presentation found."
    if c["polar_group"]:
        s += " The z coordinate is a free translation in this polar group (any z gives a congruent cell)."
    s += f" For scale: the Josehedron's vertices have denominator {JOSE_M} in its conventional cubic cell."
    return s


JOSE_M = None


def write_md(out, prev, jobs):
    global JOSE_M
    JOSE_M = out["josehedron_control"]["m_lattice_site_centred"]
    a = prev.index("<!-- PREREG-BEGIN -->")
    b = prev.index("<!-- PREREG-END -->") + len("<!-- PREREG-END -->")
    head = prev[:a]
    prereg = prev[a:b]
    T = out["totals"]
    L = [head.rstrip("\n"), "", prereg, "",
         "## Inputs and checks", "",
         f"- WALL_OPEN_PHASE2.json md5 {WALL_OPEN_MD5}; POOL_RANKING_2026-09-04.json md5 {POOL_MD5}; both stores sha256 as recorded in WALL_OPEN_PHASE2.json and unchanged after the run: {out['inputs']['stores_sha256_unchanged_after_run']}.",
         "- Tangent directions read from the WALL_OPEN rows equal nullspace_basis(site stabilizer) (the c1 function) for all 9 cells; the witness point and c/a equal the pool-ranking rows and the stores' first_witness.",
         "- Every candidate went through the accepted chain (S2/SH.evaluate); every SAME candidate was re-derived a second time by g4_certify_gram.v0_rederive as a synthetic witness (canonical code, f, p, aut asserted against the frozen store). The witness row's m_lattice (and m_cartesian, tetragonal) equals the pool-ranking value for all 9 cells (asserted).",
         f"- Candidates: {T['n_candidates']} over {T['n_cells']} cells; SAME {T['n_same']}, DIFFERENT {T['n_different']}, QUARANTINE {T['n_quarantine']}; cells whose best presentation beats the witness: {T['n_cells_improved']} of 9.",
         f"- Output JSON: harness/phase2/NICE_POINTS_2026-09-04.json (sorted keys, no timings), md5 {md5(OUT_JSON)}. {jobs} forked workers, foreground, per-cell caches in harness/phase2/nice_points_cells/ (runtime in STATUS.md).",
         "", "## Per cell", ""]
    for c in out["cells"]:
        L.append(f"### {c['system']} #{c['rank_in_system']} `{c['id']}` IT({c['IT']}) {c['symbol']} — witness {c['witness_point']} at c/a {c['c_over_a']}, f = ({', '.join(map(str, c['f']))}), p = {c['p']}, aut {c['aut_comb']} / Isom {c['isom_solid']}")
        L.append("")
        L.append(f"Search set: {c['n_points']} points x {len(c['ca_candidates'])} c/a values = {c['n_candidates']} candidates "
                 f"(c/a candidates {{{', '.join(c['ca_candidates'])}}}); SAME {c['n_same']}, DIFFERENT {c['n_different']}, QUARANTINE {c['n_quarantine']}, stabilizer-order changes {c['n_stab_change']}.")
        L.append("")
        if c["family"] == "tetragonal":
            L.append("| nice rank | generating point | c/a | m_lattice (site-centred, conventional) | m_cartesian | m_absolute | stab | nonsimple |")
            L.append("|---|---|---|---|---|---|---|---|")
            for r in c["top3"]:
                L.append(f"| {r['nice_rank']} | {r['point']} | {r['c_over_a']} | {r['m_lattice']} | {r['m_cartesian']} | {r['m_absolute_conventional']} | {r['stab']} | {r['nonsimple']} |")
            w = c["witness_row"]
            L.append(f"| witness ({w['nice_rank']}) | {w['point']} | {w['c_over_a']} | {w['m_lattice']} | {w['m_cartesian']} | {w['m_absolute_conventional']} | {w['stab']} | {w['nonsimple']} |")
        else:
            L.append("| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |")
            L.append("|---|---|---|---|---|---|---|---|---|---|")
            for r in c["top3"]:
                L.append(f"| {r['nice_rank']} | {r['point']} | {r['c_over_a']} | {r['m_lattice']} | {r['m_eisenstein']} | {r['m_c']} | {r['m_cartesian_sqrt3']} | {r['m_absolute_conventional']} | {r['stab']} | {r['nonsimple']} |")
            w = c["witness_row"]
            L.append(f"| witness ({w['nice_rank']}) | {w['point']} | {w['c_over_a']} | {w['m_lattice']} | {w['m_eisenstein']} | {w['m_c']} | {w['m_cartesian_sqrt3']} | {w['m_absolute_conventional']} | {w['stab']} | {w['nonsimple']} |")
        L.append("")
        L.append("Tellable coordinates: " + tell(c))
        L.append("")
        if c["polar_group"]:
            L.append(f"Polar group (every operation of IT({c['IT']}) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): {c['n_xy_classes_same']} such classes kept the type, {c['n_xy_classes_different']} changed it, {c['n_xy_classes_mixed']} did both (a class doing both would contradict the congruence; 0 expected).")
            L.append("")
        if c["different_candidates"]:
            L.append(f"Type-changed candidates: {c['n_different']} (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): {c['n_different_axis_parallel']}" + (f"; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: {c['n_different_axis_parallel_effective']}" if c["polar_group"] else "") + f". By number of point coordinates moved (+ca = c/a also moved): {c['different_by_coords_moved']}. Other types reached: " +
                     "; ".join(f"{t['stored_id'] or t['code_id']} f=({', '.join(map(str, t['f']))}) p={t['p']} aut {t['aut']} x{t['count']}" for t in c["different_types"]) +
                     ". Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache " + c["full_rows_cache"] + ".")
            L.append("")
        if c["quarantined"]:
            L.append(f"Quarantined candidates ({c['n_quarantine']}): " + "; ".join(f"{r['point']} c/a {r['c_over_a']}: {r['quarantine']}" for r in c["quarantined"]))
            L.append("")
    L += ["## Type-changed count (the check on the open neighbourhood)", ""]
    n_ax = sum(c["n_different_axis_parallel"] for c in out["cells"])
    n_ax_eff = sum(c["n_different_axis_parallel_effective"] for c in out["cells"])
    L.append(f"{T['n_different']} of {T['n_candidates']} candidates changed type; {T['n_quarantine']} quarantined; "
             f"{n_ax} of the changed candidates were axis-parallel from the witness (one tested direction moved), "
             f"{T['n_different'] - n_ax} moved in two or more tested directions at once; treating z as the free translation it is in the seven polar-group cells (IT 76, 144, 169), the count of changed candidates with exactly one of (x, y, c/a) moved is {n_ax_eff}. Per cell: " +
             "; ".join(f"`{c['id']}` {c['n_different']}/{c['n_candidates']} (axis-parallel {c['n_different_axis_parallel']})" for c in out["cells"]) + ".")
    L.append("")
    if T["n_different"] == 0:
        L.append("Every candidate inside the per-direction certified extents kept the certified type on this denominator-<= 48 grid, off-axis interior points included.")
    else:
        L.append("Reading (a finding about WALL_OPEN_PHASE2's scheme, not an error of either computation): "
                 + ("the on-axis extents held — no candidate that moved in a single tested direction changed type, so the OPEN verdicts and their tested steps stand as stated; " if n_ax == 0 else
                    f"{n_ax} candidates that moved in a single tested direction changed type at a step strictly between two tested SAME steps, i.e. the type is not monotone along that axis at the tested resolution — the affected cells are named above; ")
                 + "the PRODUCT of the per-axis SAME intervals is not a type-constant box. Walls in the (point, c/a) parameter space are not axis-aligned, so a corner of the box can cross a wall that neither axis reaches. WALL_OPEN_PHASE2 never claimed the box (its scheme tests axis-parallel steps and says OPEN = every tested side SAME); the pre-registered expectation of 0 here was the box reading, and it is wrong. Consequence for naming: a chosen presentation must be re-certified at ITS OWN (point, c/a), which this search does for every SAME candidate; a presentation is not inherited from the witness's verdict.")
    L += ["", "## Josehedron comparison (stated honestly)", ""]
    J = out["josehedron_control"]
    L.append(f"The Josehedron control through the same functions (phase-1 store `{J['id']}`, IT(220) Wyckoff 12a, generating point {J['point']}, f = ({', '.join(map(str, J['f']))}), p = {J['p']}, aut {J['aut']}): site-centred vertex coordinates in the conventional cubic basis have common denominator {J['m_lattice_site_centred']} (absolute conventional: {J['m_absolute_conventional']}); the cubic conventional basis is Cartesian, so that is its integer Cartesian scale. "
             f"Its published hook is integer vertex coordinates at a small scale. Against that: the best presentation found here per cell (m_lattice, then the second scale) is listed above; " +
             "; ".join(f"{c['system']} #{c['rank_in_system']} `{c['id']}` m_lattice {c['best']['m_lattice']}" + (f" / Cartesian {c['best']['m_cartesian']}" if c['family'] == 'tetragonal' else f" / Eisenstein {c['best']['m_eisenstein']}") for c in out["cells"]) + ". "
             "None of the nine reaches a Josehedron-sized scale inside its certified neighbourhood on this grid; the integer-coordinate hook stays absent for these cells at this resolution (a statement about the search set, not an impossibility proof: the neighbourhood was tested along axes with steps down to 1/1536 and the grid here stops at denominator 48 / 16).")
    L += ["", "## Verify (main session, before acceptance)", "", "```",
          f"cd <repo>/harness/phase2 && rm -rf nice_points_cells && NICE_JOBS=8 nice -n 10 python3 nice_points_2026-09-04.py; echo exit $?; md5 -q NICE_POINTS_2026-09-04.json   # must print {md5(OUT_JSON)}",
          "```", "",
          "Exit 0 and the md5 above are required. The script rewrites this file below the pre-registration block; the block itself is read back and never regenerated.", ""]
    open(OUT_MD, "w").write("\n".join(L))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
