#!/usr/bin/env python
"""sweep_phase2_tetragonal.py — PHASE 2, batch 1: the tetragonal groups
(IT 75-142, 68 groups), the first non-cubic hunt sweep.

Spec: ../PHASE2_PLAN.md (sections 1-3), ../ANCHORS.md (G3 invariant, the G2b
block, kill criteria). Structural model: sweep_phase1.py (point menu, dedupe
store, quarantine handling, deterministic ordering, no silent caps); its
helpers are IMPORTED, not re-typed (special-position scan adapted to a
parameterizable grid, rank3 / wyckoff_dim / is_lattice / Store / ChainError /
formatting verbatim by import).

Pipeline per candidate (group, orbit point, b-ratio = c/a), all on the frozen
G1-audited spacegroups.json ops and the ACCEPTED phase-2 Gram modules
(phase2/metric.py, phase2/sweep_voronoi_gram.py, phase2/exact_cell_gram.py;
G2b 21/21 PASS, main-session accepted):
  orbit.py (exact)  ->  metric.gram_tetragonal(b) with R^T G R = G asserted
  ->  sweep_gram float proposal (W=2; W=3, W=4 retries on the window guard)
  ->  exact_cell_gram.clip_cell_gram on the representative cell pts[0]
      (all-Fraction; G-norm certificate 4*rho^2 <= D^2 asserted; the initial
      cutoff D^2 is WARM-STARTED from an exact pre-clip by the float-proposed
      neighbors only — 4*rho_pre^2, capped at the module default — so the
      certified clip usually passes its certificate on the first try; the
      certificate, not the warm start, decides: a wrong proposal only makes
      the clipper quadruple D^2 and rerun)
  ->  canon_code.canonical_code (from exact facet cycles only)
  ->  ORBIT-CONGRUENCE CHECK (PHASE2_PLAN section 3, phase-2 specific): a
      SECOND orbit cell (pts[n//2]) is clipped exactly and must have the same
      (F, p-vector, canonical code); float (F, p-vector) uniformity over ALL
      orbit cells is checked as in phase 1. A violation quarantines the whole
      (group, b-ratio) — every earlier sighting from that pair is purged from
      the store and the pair is skipped from then on (counted, never silent).

G3 INVARIANT ENFORCED: nothing enters the store without the exact
re-derivation agreeing with the float sighting (facet count, p-vector,
neighbor site set), or the float cell carrying the degeneracy flag (exact
supersedes, recorded as float_superseded). Non-simple vertices recorded,
never fatal. Lattice-degenerate orbits must match a seeded parallelohedron
(Fedorov) or are quarantined as a bug. Site-stabilizer order must divide the
combinatorial aut order. >38 facets (float or exact) => quarantine, never a
type ("assume bug" — ANCHORS kill criterion). Crashes => quarantine, skip.

STORE: seeded with ALL 102 types of phase1_types.json (the cubic store, 5
parallelohedra + Josehedron + Schmitt-220 representative + 95 cubic
sightings), each marked first_sighting_system = "cubic (phase 1 store)";
every type minted here is marked "tetragonal (phase 2)". Cross-system
coincidences are therefore visible as tetragonal sightings of cubic-store
types. Witnesses record (group, point, kind, stratum dim, b-ratio, pass).

PASSES (deterministic order; a budget stop cuts LATER passes first and
counts every skipped candidate per group and pass):
  P1 coarse grid: every metric-independent orbit (special positions on the
     per-coordinate {1,2,3,4,6,8,12} grid, orbit-deduped, + 2 general
     controls) x the 13 b-ratios 1/2..7/2 step 1/4.
  P2 Schmitt collision screen: every row of Schmitt 2016's printed
     tetragonal tables (printed pp. 27-48 = PDF pp. 32-86), harvested from
     the pdftotext layer AT RUN TIME (rows written to
     schmitt_tetragonal_rows_harvested.json; the three G2b rows are asserted
     present as the cross-read check), run at the printed b-ratio; the exact
     f-vector must reproduce the printed one (else schmitt_fvec_mismatch
     quarantine); sightings are tagged kind = "schmitt_printed". Rows of an
     enantiomorphic pair's shared table are run in BOTH groups.
  P3 Schmitt b-ratios: the P1 orbits x the N_SCHMITT_B most frequent
     printed NON-grid b-ratios (all harvested values are listed in the
     result; the cap is explicit).
  P4 Wyckoff-line refinement: new orbits of the full 1/24 grid (13,824
     points) whose stratum dimension is <= 1 (line samples one level deeper
     than the coarse grid; plane samples at 1/24 are counted and skipped BY
     DESIGN) x the 13 coarse b-ratios.
  P5 transition bisection (design 2.3, 1-D): for every orbit, adjacent
     b-ratio values (over the union of P1/P3 values) with different codes get
     the interval bisected (midpoints, depth <= 4), capped at
     BISECT_CAP_PER_ORBIT evaluations per orbit (cap hits counted).

PARALLELISM: 12 forked worker processes (run under `nice -n 10`); the main
process owns the store; results are absorbed in task order (ordered imap) so
the store is deterministic regardless of worker timing. The store is
checkpointed to phase2_types.json every CHECKPOINT_S seconds (complete=false)
and finally with complete=true.

LANGUAGE (G5): every type minted here is "not matched against the catalog
snapshot of 2026-09-03" (= the phase-1 cubic store + this run's sightings).
NO novelty claim. Diligence against Schmitt's tetragonal tables at type level
is a LATER step (the machine-readable digitization covers cubic only; the P2
screen is f-vector-level and one-directional).

Run (from harness/):
  nice -n 10 python3 \
      sweep_phase2_tetragonal.py
Env: PHASE2_BUDGET_S (default 8400 = 2.5 h minus write margin),
     PHASE2_WORKERS (12), PHASE2_SMOKE=1 (3 groups, 2 b-ratios, quick test).
Writes: phase2_types.json, PHASE2_RESULT.md,
        schmitt_tetragonal_rows_harvested.json. Exit 0 iff the run ended
        (budget stops are recorded findings, not failures).
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import itertools                                     # noqa: E402
import json                                          # noqa: E402
import math                                          # noqa: E402
import multiprocessing as mp                         # noqa: E402
import re                                            # noqa: E402
import subprocess                                    # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
from collections import Counter, defaultdict         # noqa: E402
from fractions import Fraction as F                  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "phase2"))

import orbit                                         # noqa: E402
import metric                                        # noqa: E402
from sweep_voronoi_gram import sweep_gram            # noqa: E402
from exact_cell_gram import clip_cell_gram, _clip_gram   # noqa: E402
from canon_code import canonical_code                # noqa: E402
from sweep_phase1 import (SCAN, ALLOWED_DENS, GENERAL_CANDIDATES, N_GENERAL,   # noqa: E402
                          MAX_FACETS, wyckoff_dim, is_lattice, Store,
                          ChainError, frac_str, point_str, pvec_compact,
                          code_id)

PHASE1_STORE = os.path.join(HERE, "phase1_types.json")
SCHMITT_PDF = os.path.join(os.path.dirname(HERE), "references",
                           "Schmitt_2016_dissertation.pdf")
SCHMITT_PDF_PAGES = (32, 86)          # PDF pages of the tetragonal tables
OUT_JSON = os.path.join(HERE, "phase2_types.json")
OUT_MD = os.path.join(HERE, "PHASE2_RESULT.md")
OUT_ROWS = os.path.join(HERE, "schmitt_tetragonal_rows_harvested.json")

SNAPSHOT = "2026-09-03"
TET = list(range(75, 143))
B_COARSE = [F(k, 4) for k in range(2, 15)]          # 1/2 .. 7/2 step 1/4
N_SCHMITT_B = 5
FINE_SCAN = 24                                       # 1/24 grid (P4)
MAX_W = 4
BISECT_DEPTH = 4
BISECT_CAP_PER_ORBIT = 26                            # 2 x the coarse grid
PARALLELOHEDRA = ("cube", "hexagonal_prism", "rhombic_dodecahedron",
                  "elongated_dodecahedron", "truncated_octahedron")
BUDGET_S = float(os.environ.get("PHASE2_BUDGET_S", 8400))
WORKERS = int(os.environ.get("PHASE2_WORKERS", 12))
CHECKPOINT_S = 300.0
SMOKE = os.environ.get("PHASE2_SMOKE") == "1"
if SMOKE:
    TET = [75, 98, 139]
    B_COARSE = [F(1, 2), F(2)]
    N_SCHMITT_B = 1

GROUPS = orbit.load_groups()          # loaded before the fork: inherited


# ------------------------------------------------------------- point menu ---

def scan_grid(entry, scan, allowed_dens, exclude=frozenset()):
    """Special-position orbit reps on the grid (1/scan)Z^3 restricted to the
    per-coordinate denominators allowed_dens (adapted from
    sweep_phase1.special_scan: integer arithmetic mod scan, exact since the
    translations are n/12 and 12 | scan). Points whose orbit meets `exclude`
    (int triples mod scan) are skipped. Returns (sorted reps
    [(point_ints, stab, orbit_size)], set of all orbit points seen)."""
    ops = []
    for R, t in entry["ops_exact"]:
        ts = tuple(int(x * scan) for x in t)
        assert all((x * scan).denominator == 1 for x in t), "non-n/12 translation"
        ops.append((R, ts))
    allowed = [k for k in range(scan)
               if scan // math.gcd(k, scan) in allowed_dens]
    seen, reps = set(exclude), []
    for p in itertools.product(allowed, repeat=3):
        if p in seen:
            continue
        orb, stab = set(), 0
        for R, t in ops:
            q = tuple((R[i][0]*p[0] + R[i][1]*p[1] + R[i][2]*p[2] + t[i]) % scan
                      for i in range(3))
            orb.add(q)
            if q == p:
                stab += 1
        seen |= orb
        if stab > 1:
            reps.append((min(orb), stab, len(orb)))
    return sorted(reps), seen


def build_menu(num):
    """(coarse menu, fine-line menu, fine-plane-skipped count). Points as
    Fraction triples; kinds: special / general / line24 / fixed24."""
    entry = GROUPS[num]
    reps, seen = scan_grid(entry, SCAN, ALLOWED_DENS)
    coarse = [((F(p[0], SCAN), F(p[1], SCAN), F(p[2], SCAN)), "special")
              for p, _, _ in reps]
    n_general = 0
    for cand in GENERAL_CANDIDATES:
        if n_general >= N_GENERAL:
            break
        if len(orbit.site_stabilizer(entry, cand)) == 1:
            coarse.append((cand, "general"))
            n_general += 1
    # P4: the full 1/24 grid, orbits not already seen, stratum dim <= 1
    assert FINE_SCAN == SCAN
    reps24, _ = scan_grid(entry, FINE_SCAN, set(range(1, FINE_SCAN + 1)),
                          exclude=seen)
    fine, planes_skipped = [], 0
    for p, _, _ in reps24:
        q = (F(p[0], FINE_SCAN), F(p[1], FINE_SCAN), F(p[2], FINE_SCAN))
        d = wyckoff_dim(entry, q)
        if d >= 2:
            planes_skipped += 1
        else:
            fine.append((q, "line24" if d == 1 else "fixed24"))
    return coarse, fine, planes_skipped


# --------------------------------------------------- Schmitt table harvest ---

def harvest_schmitt_rows():
    """Rows (groups, f-vector, b-ratio, point) of Schmitt's printed tetragonal
    tables from the pdftotext layer (PDF pages SCHMITT_PDF_PAGES). Group
    headers 'Space group type (...); IT(a) = X, IT(b) = Y' list every group
    sharing the table (enantiomorphic pairs)."""
    txt = subprocess.run(
        ["pdftotext", "-layout", "-f", str(SCHMITT_PDF_PAGES[0]),
         "-l", str(SCHMITT_PDF_PAGES[1]), SCHMITT_PDF, "-"],
        check=True, capture_output=True, text=True).stdout
    txt = txt.replace("−", "-")
    hdr = re.compile(r"Space group type \([^)]*\);\s*(.*)")
    itre = re.compile(r"IT\((\d+)\)")
    rowre = re.compile(r"^\s*\((\d+),\s*(\d+),\s*(\d+)\)\s+(\d+(?:/\d+)?)\s+"
                       r"\((-?\d+(?:/\d+)?),\s*(-?\d+(?:/\d+)?),\s*"
                       r"(-?\d+(?:/\d+)?)\)\s*$")
    cur, rows = None, []
    for line in txt.split("\n"):
        m = hdr.search(line)
        if m:
            cur = tuple(int(x) for x in itre.findall(m.group(1)))
            continue
        m = rowre.match(line)
        if m and cur and all(75 <= g <= 142 for g in cur):
            rows.append({
                "groups": list(cur),
                "f_vector": [int(m[1]), int(m[2]), int(m[3])],
                "b_ratio": m[4],
                "point": [m[5], m[6], m[7]],
            })
    return rows


# ------------------------------------------------------------ the chain ---

def exact_cell_warm(center, pts, period, G, cell_f):
    """clip_cell_gram with the cutoff warm-started from an exact pre-clip by
    the float-proposed neighbors (4*rho_pre^2, capped at the module default).
    The certified clipper decides; this only chooses its starting D^2."""
    Gi, _ = metric.scale_to_integers(G)
    D2_default = 4 * period * period * max(Gi[i][i] for i in range(3))
    nbrs = [tuple(center[k] + d[k] for k in range(3))
            for d in cell_f["neighbor_deltas"]]
    B = metric.coord_bound(Gi, D2_default)
    verts, _ = _clip_gram(center, nbrs, Gi, B)
    rho2 = max(metric.gnorm2(Gi, (v[0] - center[0], v[1] - center[1],
                                  v[2] - center[2])) for v, _ in verts)
    D2 = min(4 * rho2, F(D2_default))
    return clip_cell_gram(center, pts, period, G, D2=D2)


def evaluate(num, p, b, kind):
    """Full chain on one candidate. Returns a result dict; raises ChainError
    on any kill criterion (the caller records it as a quarantine)."""
    entry = GROUPS[num]
    t0 = time.time()
    ob = orbit.orbit(entry, p)
    dim = 3 if ob["stabilizer_order"] == 1 else wyckoff_dim(entry, p)
    pts, period = orbit.scale_orbit(ob["points"])
    lat = is_lattice(pts, period)
    G = metric.gram_tetragonal(b)
    if not metric.gram_compatible(entry, G):
        raise ChainError("gram_incompatible", "R^T G R != G for some op")
    W = 2
    while True:
        try:
            cells_f = sweep_gram(pts, period, G, W=W, entry=entry)
            break
        except RuntimeError as exc:
            W += 1
            if W > MAX_W:
                raise ChainError("window_guard", f"W>{MAX_W}: {exc}")
    degen_any = any(c["degenerate_flag"] for c in cells_f)
    fps = {(c["facet_count"], c["p_vector"]) for c in cells_f}
    float_uniform = len(fps) == 1
    float_max_F = max(c["facet_count"] for c in cells_f)
    if float_max_F > MAX_FACETS:
        raise ChainError("kill_gt38_float",
                         f"float facet count {float_max_F} > {MAX_FACETS}")
    if not float_uniform and not degen_any:
        raise ChainError("float_nonuniform_orbit",
                         f"orbit cells not float-congruent, no degeneracy "
                         f"flag: {sorted(fps)}")
    ec = exact_cell_warm(pts[0], pts, period, G, cells_f[0])
    assert 4 * ec["rho2"] <= ec["cutoff_D2"], "cutoff certificate violated"
    Fc, V = ec["facet_count"], ec["n_vertices"]
    E = ec["n_edges"]
    assert V - E + Fc == 2, "Euler failure"
    if Fc > MAX_FACETS:
        raise ChainError("kill_gt38_exact",
                         f"exact facet count {Fc} > {MAX_FACETS}")
    f0 = cells_f[0]
    nbr_f = {tuple(pts[0][k] + d[k] for k in range(3))
             for d in f0["neighbor_deltas"]}
    agree = (f0["facet_count"] == Fc and f0["p_vector"] == ec["p_vector"]
             and nbr_f == set(ec["neighbors"]))
    if not agree and not f0["degenerate_flag"]:
        raise ChainError("float_exact_disagree",
                         f"float ({f0['facet_count']}, {f0['p_vector']}) vs "
                         f"exact ({Fc}, {ec['p_vector']}), no degeneracy flag")
    code, aut = canonical_code(ec["facet_cycles"])
    congruence = None
    if len(pts) > 1:
        j = len(pts) // 2
        e1 = exact_cell_warm(pts[j], pts, period, G, cells_f[j])
        assert 4 * e1["rho2"] <= e1["cutoff_D2"], "cutoff certificate violated (2nd cell)"
        code1, aut1 = canonical_code(e1["facet_cycles"])
        congruence = (e1["facet_count"] == Fc and e1["p_vector"] == ec["p_vector"]
                      and code1 == code and aut1 == aut)
        if not congruence:
            raise ChainError(
                "orbit_congruence_violation",
                f"cell 0 ({Fc}, {pvec_compact(ec['p_vector'])}, aut {aut}) vs "
                f"cell {j} ({e1['facet_count']}, "
                f"{pvec_compact(e1['p_vector'])}, aut {aut1})")
    if aut % ob["stabilizer_order"] != 0:
        raise ChainError("stab_not_dividing_aut",
                         f"stab {ob['stabilizer_order']} does not divide aut {aut}")
    return {
        "stabilizer_order": ob["stabilizer_order"],
        "orbit_conventional": ob["n_conventional"],
        "orbit_primitive": ob["n_primitive"], "stratum_dim": dim,
        "period": period, "lattice_degenerate": lat,
        "W": W, "float_max_F": float_max_F, "float_uniform": float_uniform,
        "degen_any": degen_any, "degen_flag0": f0["degenerate_flag"],
        "float_superseded": (not agree) and f0["degenerate_flag"],
        "fvec": (V, E, Fc), "pvec": ec["p_vector"], "Fc": Fc,
        "nonsimple": ec["nonsimple_vertices"], "cutoff_D2": str(ec["cutoff_D2"]),
        "code_str": code.decode("ascii"), "aut": aut,
        "congruence_checked": congruence is not None,
        "seconds": time.time() - t0,
    }


def eval_record(num, p, b, kind, pass_name, extra=None):
    rec = {"group": num, "point": [frac_str(x) for x in p], "kind": kind,
           "b": frac_str(b), "pass": pass_name}
    if extra:
        rec.update(extra)
    try:
        rec.update(verdict="ok", **evaluate(num, p, b, kind))
    except ChainError as exc:
        rec.update(verdict="quarantined", reason=exc.reason, detail=exc.detail)
    except Exception as exc:                       # crash: record and skip
        rec.update(verdict="quarantined", reason="crash",
                   detail=f"{type(exc).__name__}: {exc}"[:300])
    return rec


def worker(task):
    """task = (task_id, pass_name, payload). Returns (task_id, [records])."""
    tid, pname, pay = task
    if pname == "menu":
        num = pay
        coarse, fine, skipped = build_menu(num)
        return tid, {"group": num,
                     "coarse": [([frac_str(x) for x in p], k) for p, k in coarse],
                     "fine": [([frac_str(x) for x in p], k) for p, k in fine],
                     "planes24_skipped": skipped}
    if pname == "P5":
        num, pstr, kind, chain = pay
        p = tuple(F(s) for s in pstr)
        return tid, bisect_orbit(num, p, kind, chain)
    num, pstr, kind, bstr = pay[:4]
    extra = pay[4] if len(pay) > 4 else None
    p = tuple(F(s) for s in pstr)
    return tid, [eval_record(num, p, F(bstr), kind, pname, extra)]


def bisect_orbit(num, p, kind, chain):
    """chain: sorted [(b_str, code_id or None)] from the grid passes. Bisect
    every adjacent pair with different (non-None) codes; depth <= BISECT_DEPTH,
    <= BISECT_CAP_PER_ORBIT evaluations. Returns the records (in evaluation
    order) plus a final cap note record if the cap was hit."""
    out, n_eval = [], 0
    cap_hit = False

    def code_of(rec):
        return code_id(rec["code_str"]) if rec["verdict"] == "ok" else None

    def rec_at(b, lo, hi, depth):
        nonlocal n_eval
        r = eval_record(num, p, b, kind, "P5",
                        {"bisect_depth": depth, "bisect_lo": frac_str(lo),
                         "bisect_hi": frac_str(hi)})
        out.append(r)
        n_eval += 1
        return r

    def go(lo, hi, clo, chi, depth):
        nonlocal cap_hit
        if depth > BISECT_DEPTH:
            return
        if n_eval >= BISECT_CAP_PER_ORBIT:
            cap_hit = True
            return
        mid = (lo + hi) / 2
        cm = code_of(rec_at(mid, lo, hi, depth))
        if cm is None:
            return
        if cm != clo:
            go(lo, mid, clo, cm, depth + 1)
        if cm != chi:
            go(mid, hi, cm, chi, depth + 1)

    for (b0, c0), (b1, c1) in zip(chain, chain[1:]):
        if c0 is None or c1 is None or c0 == c1:
            continue
        go(F(b0), F(b1), c0, c1, 1)
    if cap_hit:
        out.append({"group": num, "point": [frac_str(x) for x in p],
                    "kind": kind, "pass": "P5", "verdict": "bisect_cap",
                    "evaluations": n_eval})
    return out


# ----------------------------------------------------------------- store ---

class Store2(Store):
    """Phase-1 Store + first-sighting system and per-(group,b) purge."""

    def add_phase1(self, cid, e):
        assert cid not in self.types
        self.types[cid] = {
            "canon_code": e["canon_code"], "f_vector": list(e["f_vector"]),
            "p_vector": list(e["p_vector"]), "aut_order": e["aut_order"],
            "first_sighting_system": "cubic (phase 1 store)",
            "seeded": e["seeded"], "seed_name": e.get("seed_name"),
            "seed_source": e.get("seed_source"),
            "phase1_first_witness": e.get("first_witness"),
            "phase1_sightings": len(e["sightings"]),
            "first_witness": None, "sightings": [],
        }
        self.order.append(cid)

    def sight(self, code_str, fvec, pvec, aut, sighting):
        cid, is_new = Store.sight(self, code_str, fvec, pvec, aut, sighting)
        e = self.types[cid]
        if is_new:
            e["first_sighting_system"] = "tetragonal (phase 2)"
            e["phase1_sightings"] = 0
        elif e["first_witness"] is None:
            e["first_witness"] = sighting      # first PHASE-2 sighting of a cubic type
        return cid, is_new

    def purge_group_b(self, num, b_str):
        """Remove every sighting from (group, b); drop unseeded types left with
        no sightings. Returns (n_sightings_removed, [dropped type ids])."""
        removed, dropped = 0, []
        for cid in list(self.order):
            e = self.types[cid]
            keep = [s for s in e["sightings"]
                    if not (s["group"] == num and s["b"] == b_str)]
            removed += len(e["sightings"]) - len(keep)
            e["sightings"] = keep
            if e["first_witness"] is not None and \
                    e["first_witness"]["group"] == num and \
                    e["first_witness"]["b"] == b_str:
                e["first_witness"] = keep[0] if keep else None
            if not keep and e["first_sighting_system"].startswith("tetragonal"):
                dropped.append(cid)
                del self.types[cid]
                self.order.remove(cid)
        return removed, dropped


# ------------------------------------------------------------------ main ---

class Run:
    def __init__(self):
        self.t_start = time.time()
        self.t_ckpt = self.t_start
        self.log = []
        self.store = Store2()
        self.cubic_ids = set()
        self.records = []          # compact per-candidate rows
        self.quarantines = []
        self.gb_quarantined = set()          # (group, b_str)
        self.gb_purges = []
        self.skipped = Counter()             # (group, pass) -> n
        self.evaluated = Counter()           # (group, pass) -> n
        self.stats = defaultdict(lambda: {
            "cells_exact": 0, "types": set(), "new_first_here": [],
            "quar": 0, "max_f": 0, "cubic_types": set(), "tet_types": set(),
            "lattice": 0, "float_superseded": 0, "nonsimple_cells": 0,
            "seconds": 0.0})
        self.max_f_stored = 0
        self.max_f_menu = 0                  # max facets from OUR menu (not Schmitt rows)
        self.menu_F = Counter()              # group -> max facets from our menu
        self.max_f_quarantined = 0
        self.budget_hit = False
        self.stopped_in = None
        self.menus = {}
        self.schmitt_rows = []
        self.schmitt_b_all = []
        self.schmitt_b_used = []
        self.schmitt_screen = {"reproduced": 0, "mismatch": 0, "quarantined_other": 0}
        self.codes_at = defaultdict(dict)    # (group, point_str, kind) -> {b_str: cid|None}
        self.bisect_caps = 0
        self.bisect_evals = 0
        self.pass_summary = {}

    def say(self, s):
        print(s, flush=True)
        self.log.append(s)

    # ---- absorb one evaluation record into the store
    def absorb(self, rec):
        num, pname = rec["group"], rec["pass"]
        st = self.stats[num]
        key = (num, rec["point"] and tuple(rec["point"]), rec["kind"])
        if rec["verdict"] == "bisect_cap":
            self.bisect_caps += 1
            self.records.append([num, ",".join(rec["point"]), rec["kind"], "",
                                 pname, "bisect_cap", rec["evaluations"], ""])
            return
        self.evaluated[(num, pname)] += 1
        if pname == "P5":
            self.bisect_evals += 1
        b_str = rec["b"]
        if (num, b_str) in self.gb_quarantined:
            self.skipped[(num, pname)] += 1
            self.records.append([num, ",".join(rec["point"]), rec["kind"], b_str,
                                 pname, "skipped_group_b_quarantined", "", ""])
            return
        if rec["verdict"] == "quarantined":
            self._quarantine(rec)
            self.codes_at[key][b_str] = None
            return
        st["seconds"] += rec["seconds"]
        # lattice-degenerate orbits must be seeded parallelohedra (Fedorov)
        cid = code_id(rec["code_str"])
        if rec["lattice_degenerate"]:
            ok = (cid in self.cubic_ids
                  and self.store.types[cid].get("seed_name") in PARALLELOHEDRA)
            if not ok:
                rec = dict(rec, verdict="quarantined",
                           reason="lattice_orbit_nonparallelohedron",
                           detail="lattice-degenerate orbit produced a "
                                  "non-parallelohedron type (Fedorov violation = bug)")
                self._quarantine(rec)
                self.codes_at[key][b_str] = None
                return
        if rec["kind"] == "schmitt_printed":
            if tuple(rec["fvec"]) != tuple(rec["schmitt_fvec"]):
                rec = dict(rec, verdict="quarantined", reason="schmitt_fvec_mismatch",
                           detail=f"exact f={tuple(rec['fvec'])} vs printed "
                                  f"{tuple(rec['schmitt_fvec'])}")
                self.schmitt_screen["mismatch"] += 1
                self._quarantine(rec)
                return
            self.schmitt_screen["reproduced"] += 1
        sighting = {
            "group": num, "group_symbol": GROUPS[num]["international_short"],
            "point": rec["point"], "kind": rec["kind"], "b": b_str,
            "pass": pname, "stratum_dim": rec["stratum_dim"],
            "stabilizer_order": rec["stabilizer_order"],
            "orbit_conventional": rec["orbit_conventional"],
            "orbit_primitive": rec["orbit_primitive"],
            "lattice_degenerate": rec["lattice_degenerate"],
            "degenerate_flag": rec["degen_flag0"],
            "float_superseded": rec["float_superseded"],
            "nonsimple_vertices": rec["nonsimple"], "W": rec["W"],
            "congruence_checked": rec["congruence_checked"],
        }
        cid, is_new = self.store.sight(rec["code_str"], rec["fvec"], rec["pvec"],
                                       rec["aut"], sighting)
        self.codes_at[key][b_str] = cid
        st["cells_exact"] += 2 if rec["congruence_checked"] else 1
        st["types"].add(cid)
        (st["cubic_types"] if cid in self.cubic_ids else st["tet_types"]).add(cid)
        st["max_f"] = max(st["max_f"], rec["Fc"])
        st["lattice"] += rec["lattice_degenerate"]
        st["float_superseded"] += rec["float_superseded"]
        st["nonsimple_cells"] += rec["nonsimple"] > 0
        self.max_f_stored = max(self.max_f_stored, rec["Fc"])
        if rec["kind"] != "schmitt_printed":
            self.max_f_menu = max(self.max_f_menu, rec["Fc"])
            if rec["Fc"] > self.menu_F[num]:
                self.menu_F[num] = rec["Fc"]
        if is_new:
            st["new_first_here"].append(cid)
        self.records.append([num, ",".join(rec["point"]), rec["kind"], b_str,
                             pname, "stored", cid, rec["Fc"]])

    def _quarantine(self, rec):
        num = rec["group"]
        self.stats[num]["quar"] += 1
        q = {k: rec[k] for k in ("group", "point", "kind", "b", "pass",
                                 "reason", "detail") if k in rec}
        self.quarantines.append(q)
        self.records.append([num, ",".join(rec["point"]), rec["kind"], rec["b"],
                             rec["pass"], "quarantined", rec["reason"], ""])
        if rec["reason"].startswith("kill_gt38"):
            mf = int(rec["detail"].split()[3])
            self.max_f_quarantined = max(self.max_f_quarantined, mf)
        if rec["reason"] == "orbit_congruence_violation":
            self.gb_quarantined.add((num, rec["b"]))
            removed, dropped = self.store.purge_group_b(num, rec["b"])
            self.gb_purges.append({"group": num, "b": rec["b"],
                                   "sightings_removed": removed,
                                   "types_dropped": dropped})
            self.say(f"  !! (group {num}, b={rec['b']}) QUARANTINED: "
                     f"congruence violation; purged {removed} sightings, "
                     f"dropped {len(dropped)} types")

    # ---- passes
    def run_pass(self, pool, pname, tasks, per_group_total):
        """Ordered imap; absorbs in task order; budget + checkpoint checks.
        Returns True if the pass completed."""
        t0 = time.time()
        done_in_group = Counter()
        n_done = 0
        it = pool.imap(worker, tasks, chunksize=4 if pname != "P5" else 1)
        for i, (tid, out) in enumerate(it):
            num = tasks[i][2][0] if pname != "menu" else tasks[i][2]
            if pname == "menu":
                self.menus[num] = out
            else:
                for rec in out:
                    self.absorb(rec)
            n_done += 1
            done_in_group[num] += 1
            if done_in_group[num] == per_group_total[num] and pname != "menu":
                self.group_line(num, pname, time.time() - t0)
            if time.time() - self.t_ckpt > CHECKPOINT_S:
                self.checkpoint(False)
            if time.time() - self.t_start > BUDGET_S:
                self.budget_hit = True
                self.stopped_in = pname
                for t in tasks[n_done:]:
                    g = t[2][0] if pname != "menu" else t[2]
                    self.skipped[(g, pname)] += 1
                self.say(f"BUDGET HIT in {pname} after {n_done}/{len(tasks)} tasks; "
                         f"{len(tasks) - n_done} skipped (counted per group)")
                pool.terminate()
                return False
        self.pass_summary[pname] = {"tasks": len(tasks), "seconds": time.time() - t0}
        self.say(f"pass {pname} complete: {len(tasks)} tasks in {time.time()-t0:.0f}s "
                 f"(store {len(self.store.order)} types, quarantines {len(self.quarantines)})")
        return True

    def group_line(self, num, pname, t):
        st = self.stats[num]
        self.say(f"  {pname} #{num} {GROUPS[num]['international_short']:9s} "
                 f"eval={self.evaluated[(num, pname)]:5d} types={len(st['types']):3d} "
                 f"(tet {len(st['tet_types'])}, cubic {len(st['cubic_types'])}) "
                 f"new={len(st['new_first_here']):3d} quar={st['quar']} "
                 f"maxF={st['max_f']:2d} [{t:.0f}s]")

    # ---- output
    def menu_sighted(self, cid):
        """True iff the type has a sighting from OUR orbit menu (any kind other
        than Schmitt's printed points)."""
        return any(s["kind"] != "schmitt_printed"
                   for s in self.store.types[cid]["sightings"])

    def snapshot(self, complete):
        elapsed = time.time() - self.t_start
        for cid in self.store.order:
            e = self.store.types[cid]
            e["sighted_by_kinds"] = sorted({s["kind"] for s in e["sightings"]})
            e["schmitt_printed_only"] = (bool(e["sightings"])
                                         and not self.menu_sighted(cid))
        groups_summary = [self.group_row(num) for num in TET]
        new_ids = [c for c in self.store.order if c not in self.cubic_ids]
        return {
            "generated_by": "sweep_phase2_tetragonal.py (Phase 2 batch 1, tetragonal, "
                            + SNAPSHOT + ")",
            "complete": complete,
            "catalog_snapshot": SNAPSHOT,
            "language_note": "types with first_sighting_system 'tetragonal (phase 2)' "
                "are NOT MATCHED AGAINST THE CATALOG SNAPSHOT OF " + SNAPSHOT +
                " (= phase-1 cubic store + this run); no novelty claim is made; "
                "type-level diligence vs Schmitt's tetragonal tables is a later "
                "step (digitization covers cubic only)",
            "scan": {"groups": TET, "grid_denominators": list(ALLOWED_DENS),
                     "scan_period": SCAN, "fine_scan": FINE_SCAN,
                     "general_controls_per_group": N_GENERAL,
                     "b_coarse": [frac_str(b) for b in B_COARSE],
                     "schmitt_b_all_harvested": self.schmitt_b_all,
                     "schmitt_b_used": self.schmitt_b_used,
                     "n_schmitt_b_cap": N_SCHMITT_B,
                     "bisect_depth": BISECT_DEPTH,
                     "bisect_cap_per_orbit": BISECT_CAP_PER_ORBIT,
                     "max_facets_kill": MAX_FACETS, "max_W": MAX_W,
                     "workers": WORKERS, "budget_s": BUDGET_S, "smoke": SMOKE},
            "types": {cid: self.store.types[cid] for cid in self.store.order},
            "type_order": self.store.order,
            "n_types_cubic_store": len(self.cubic_ids),
            "n_types_tetragonal_new": len(new_ids),
            "n_types_tetragonal_menu_sighted": sum(1 for c in new_ids if self.menu_sighted(c)),
            "n_types_tetragonal_schmitt_printed_only": sum(
                1 for c in new_ids if not self.menu_sighted(c)),
            "groups_summary": groups_summary,
            "pass_summary": self.pass_summary,
            "schmitt_screen": self.schmitt_screen,
            "quarantines": self.quarantines,
            "group_b_quarantined": sorted(self.gb_quarantined),
            "group_b_purges": self.gb_purges,
            "bisect_cap_hits": self.bisect_caps,
            "max_facets_stored": self.max_f_stored,
            "max_facets_from_our_menu": self.max_f_menu,
            "max_facets_quarantined": self.max_f_quarantined,
            "budget_hit": self.budget_hit, "stopped_in_pass": self.stopped_in,
            "elapsed_s": round(elapsed),
            "record_columns": ["group", "point", "kind", "b", "pass", "verdict",
                               "type_id_or_reason", "F"],
            "records": self.records,
        }

    def group_row(self, num):
        st = self.stats[num]
        m = self.menus.get(num, {})
        return {
            "group": num, "symbol": GROUPS[num]["international_short"],
            "n_ops": GROUPS[num]["n_ops"],
            "orbits_coarse": len(m.get("coarse", [])),
            "orbits_special": sum(1 for _, k in m.get("coarse", []) if k == "special"),
            "orbits_general": sum(1 for _, k in m.get("coarse", []) if k == "general"),
            "orbits_line24": len(m.get("fine", [])),
            "planes24_skipped_by_design": m.get("planes24_skipped", 0),
            "schmitt_rows": sum(1 for r in self.schmitt_rows if num in r["groups"]),
            "evaluated": {p: self.evaluated[(num, p)] for p in ("P1", "P2", "P3", "P4", "P5")},
            "skipped": {p: self.skipped[(num, p)] for p in ("P1", "P2", "P3", "P4", "P5")},
            "cells_exact": st["cells_exact"],
            "types_distinct": len(st["types"]),
            "types_cubic_store": len(st["cubic_types"]),
            "types_tetragonal": len(st["tet_types"]),
            "types_tetragonal_menu_sighted": sum(
                1 for c in st["tet_types"] if self.menu_sighted(c)),
            "types_tetragonal_schmitt_only": sum(
                1 for c in st["tet_types"] if not self.menu_sighted(c)),
            "new_types_first_here": len(st["new_first_here"]),
            "new_types_first_here_menu": sum(
                1 for c in st["new_first_here"] if self.menu_sighted(c)),
            "max_facets_menu": self.menu_F.get(num, 0),
            "quarantines": st["quar"], "max_facets": st["max_f"],
            "lattice_degenerate_sightings": st["lattice"],
            "float_superseded": st["float_superseded"],
            "seconds_cpu": round(st["seconds"], 1),
        }

    def checkpoint(self, complete):
        t0 = time.time()
        snap = self.snapshot(complete)
        tmp = OUT_JSON + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(snap, fh, indent=1)
        os.replace(tmp, OUT_JSON)
        self.t_ckpt = time.time()
        self.say(f"  [checkpoint {'FINAL' if complete else ''} phase2_types.json: "
                 f"{len(self.store.order)} types, {len(self.records)} records, "
                 f"{time.time()-t0:.1f}s]")
        return snap


def main():
    run = Run()
    say = run.say
    say(f"PHASE 2 tetragonal sweep — start (workers {WORKERS}, budget {BUDGET_S:.0f} s"
        f"{', SMOKE' if SMOKE else ''})")

    # ---- seed: all phase-1 types
    p1 = json.load(open(PHASE1_STORE))
    for cid in p1["type_order"]:
        run.store.add_phase1(cid, p1["types"][cid])
    run.cubic_ids = set(run.store.order)
    assert len(run.cubic_ids) == 102 and not p1["budget_hit"]
    say(f"seeded {len(run.cubic_ids)} types from phase1_types.json (cubic store)")

    # ---- Schmitt rows (harvest + cross-read)
    rows = harvest_schmitt_rows()
    run.schmitt_rows = rows
    g2b = {(75, "1/2", ("2825/5652", "-1/5652", "0")),
           (76, "797/1000", ("20/333", "44/999", "0")),
           (77, "1/2", ("539/5652", "-187/5652", "0"))}
    have = {(g, r["b_ratio"], tuple(r["point"])) for r in rows for g in r["groups"]}
    assert g2b <= have, "G2b cross-read rows missing from the harvest"
    bc = Counter(r["b_ratio"] for r in rows)
    grid = {frac_str(b) for b in B_COARSE}
    run.schmitt_b_all = [{"b": b, "rows": n} for b, n in
                         sorted(bc.items(), key=lambda kv: (-kv[1], F(kv[0])))]
    run.schmitt_b_used = [b for b, _ in sorted(bc.items(), key=lambda kv: (-kv[1], F(kv[0])))
                          if b not in grid][:N_SCHMITT_B]
    json.dump({"source": "Schmitt 2016 dissertation, pdftotext -layout, PDF pages "
                         f"{SCHMITT_PDF_PAGES[0]}-{SCHMITT_PDF_PAGES[1]} (printed pp. 27-48)",
               "harvested": SNAPSHOT, "rows": rows}, open(OUT_ROWS, "w"), indent=1)
    say(f"harvested {len(rows)} Schmitt tetragonal rows over "
        f"{len({g for r in rows for g in r['groups']})} groups; "
        f"{len(bc)} distinct printed b-ratios; using non-grid b-ratios "
        f"{run.schmitt_b_used} for P3 (cap {N_SCHMITT_B})")

    ctx = mp.get_context("fork")
    pool = ctx.Pool(WORKERS)
    try:
        # ---- menus
        tasks = [(i, "menu", num) for i, num in enumerate(TET)]
        run.run_pass(pool, "menu", tasks, Counter({num: 1 for num in TET}))
        n_coarse = sum(len(m["coarse"]) for m in run.menus.values())
        n_fine = sum(len(m["fine"]) for m in run.menus.values())
        n_pl = sum(m["planes24_skipped"] for m in run.menus.values())
        say(f"menus: {n_coarse} coarse orbits (special + general), {n_fine} "
            f"line/fixed orbits new on the 1/24 grid, {n_pl} plane orbits at "
            f"1/24 skipped by design")

        def orbit_tasks(pname, kinds_from, b_list):
            tasks, per_group = [], Counter()
            for num in TET:
                for pstr, kind in run.menus[num][kinds_from]:
                    for b in b_list:
                        tasks.append((len(tasks), pname, (num, pstr, kind, frac_str(b))))
                        per_group[num] += 1
            return tasks, per_group

        # ---- P1
        tasks, pg = orbit_tasks("P1", "coarse", B_COARSE)
        if not run.run_pass(pool, "P1", tasks, pg):
            raise StopIteration
        # ---- P2 Schmitt screen
        tasks, pg = [], Counter()
        for r in rows:
            for g in r["groups"]:
                if g not in TET:
                    continue
                tasks.append((len(tasks), "P2", (g, r["point"], "schmitt_printed",
                                                 r["b_ratio"],
                                                 {"schmitt_fvec": r["f_vector"],
                                                  "schmitt_primary_group": r["groups"][0]})))
                pg[g] += 1
        if not run.run_pass(pool, "P2", tasks, pg):
            raise StopIteration
        say(f"Schmitt screen: {run.schmitt_screen}")
        # ---- P3
        tasks, pg = orbit_tasks("P3", "coarse", [F(b) for b in run.schmitt_b_used])
        if not run.run_pass(pool, "P3", tasks, pg):
            raise StopIteration
        # ---- P4
        tasks, pg = orbit_tasks("P4", "fine", B_COARSE)
        if not run.run_pass(pool, "P4", tasks, pg):
            raise StopIteration
        # ---- P5
        tasks, pg = [], Counter()
        for num in TET:
            for pstr, kind in run.menus[num]["coarse"] + run.menus[num]["fine"]:
                key = (num, tuple(pstr), kind)
                chain = sorted(run.codes_at[key].items(), key=lambda kv: F(kv[0]))
                if any(c0 != c1 and c0 is not None and c1 is not None
                       for (_, c0), (_, c1) in zip(chain, chain[1:])):
                    tasks.append((len(tasks), "P5", (num, pstr, kind, chain)))
                    pg[num] += 1
        say(f"P5: {len(tasks)} orbits with at least one code transition")
        if not run.run_pass(pool, "P5", tasks, pg):
            raise StopIteration
    except StopIteration:
        pass
    finally:
        pool.terminate()
        pool.join()

    elapsed = time.time() - run.t_start
    new_ids = [c for c in run.store.order if c not in run.cubic_ids]
    say("")
    say(f"DONE in {elapsed:.0f}s: {sum(run.evaluated.values())} candidates evaluated "
        f"({sum(run.skipped.values())} skipped), {len(run.store.order)} types in store "
        f"({len(run.cubic_ids)} cubic store + {len(new_ids)} tetragonal, not matched "
        f"against catalog snapshot of {SNAPSHOT}), max stored facets {run.max_f_stored}, "
        f"{len(run.quarantines)} quarantines, budget_hit={run.budget_hit}")
    snap = run.checkpoint(True)
    write_result(run, snap, new_ids, elapsed)
    say("wrote PHASE2_RESULT.md")
    return 0


# ---------------------------------------------------------------- report ---

def write_result(run, snap, new_ids, elapsed):
    store = run.store
    L = []
    L.append(f"# PHASE 2 result — tetragonal sweep (batch 1, {SNAPSHOT})"
             + (" [SMOKE RUN]" if SMOKE else ""))
    L.append("")
    L.append("Spec: `../PHASE2_PLAN.md`; gates `../ANCHORS.md` G3 (enforced per "
             "stored sighting), G2b block (accepted Gram modules), KILL CRITERIA "
             "(>38 facets = quarantine; congruence violation = (group, b) "
             "quarantine). Pipeline: `orbit.py` -> `phase2/metric.py` (integer "
             "Gram diag(q^2,q^2,p^2), R^T G R = G asserted) -> "
             "`phase2/sweep_voronoi_gram.py` (float proposal, W=2..4) -> "
             "`phase2/exact_cell_gram.py` (all-Fraction, G-norm certificate "
             "4 rho^2 <= D^2 asserted; cutoff warm-started from a float-neighbor "
             "pre-clip, capped at the module default) -> `canon_code.py`; a "
             "second orbit cell is clipped exactly on every candidate with "
             "orbit size > 1 (orbit-congruence check). Frozen G1 "
             "`spacegroups.json` only. Store seeded with all 102 phase-1 (cubic) "
             "types.")
    L.append("")
    L.append(f"**LANGUAGE (G5): every type marked tetragonal below means \"not "
             f"matched against catalog snapshot of {SNAPSHOT}\" (= the phase-1 "
             f"cubic store + this run). NO novelty claim, NO naming. Type-level "
             f"diligence against Schmitt's tetragonal tables is a LATER step: the "
             f"machine-readable Schmitt digitization covers the cubic groups "
             f"only; the P2 screen here is f-vector-level and one-directional "
             f"(his printed rows reproduce in our pipeline; it says nothing about "
             f"whether our types appear in his 14 TB).**")
    L.append("")
    ev = sum(run.evaluated.values())
    sk = sum(run.skipped.values())
    L.append("## Headline")
    L.append("")
    L.append(f"- Groups: {len(TET)} (IT {TET[0]}-{TET[-1]}); coarse orbits "
             f"{sum(r['orbits_coarse'] for r in snap['groups_summary'])} "
             f"({sum(r['orbits_special'] for r in snap['groups_summary'])} special + "
             f"{sum(r['orbits_general'] for r in snap['groups_summary'])} general); "
             f"1/24-grid line/fixed orbits {sum(r['orbits_line24'] for r in snap['groups_summary'])} "
             f"(plane samples at 1/24 skipped by design: "
             f"{sum(r['planes24_skipped_by_design'] for r in snap['groups_summary'])}).")
    L.append(f"- b-ratios: coarse {[frac_str(b) for b in B_COARSE]}; Schmitt "
             f"non-grid values used (P3) {run.schmitt_b_used} (cap {N_SCHMITT_B}; all "
             f"{len(run.schmitt_b_all)} harvested values listed below); bisection "
             f"midpoints (P5) depth <= {BISECT_DEPTH}, cap {BISECT_CAP_PER_ORBIT}/orbit.")
    L.append(f"- Candidates evaluated: {ev} (skipped on budget/quarantine: {sk}); "
             f"exact cells: {sum(r['cells_exact'] for r in snap['groups_summary'])}.")
    menu_ids = [c for c in new_ids if run.menu_sighted(c)]
    schmitt_only_ids = [c for c in new_ids if not run.menu_sighted(c)]
    L.append(f"- Store: {len(store.order)} types = {len(run.cubic_ids)} cubic-store + "
             f"**{len(new_ids)} tetragonal** (first sighted in this run), of which "
             f"**{len(menu_ids)} were sighted by OUR orbit menu** (P1/P3/P4/P5) and "
             f"{len(schmitt_only_ids)} were seen ONLY at Schmitt's printed generating "
             f"points (P2: his cells reproduced through our pipeline, not our hunt). "
             f"Cubic-store types re-sighted in tetragonal groups: "
             f"{sum(1 for c in run.cubic_ids if store.types[c]['sightings'])}.")
    L.append(f"- Max facet count stored: **{run.max_f_stored}** (from our own menu: "
             f"**{run.max_f_menu}**; the rest is Schmitt's printed rows)"
             + (f"; max in quarantine: {run.max_f_quarantined}." if run.max_f_quarantined
                else "; no >38 sighting at all."))
    L.append(f"- Quarantines: {len(run.quarantines)}; (group, b) pairs quarantined "
             f"for congruence: {len(run.gb_quarantined)}; bisection cap hits: "
             f"{run.bisect_caps}.")
    L.append(f"- Schmitt screen (P2): {run.schmitt_screen['reproduced']} printed rows "
             f"reproduced exactly (f-vector), {run.schmitt_screen['mismatch']} "
             f"mismatches, of {len(run.schmitt_rows)} rows x groups "
             f"{sum(r['schmitt_rows'] for r in snap['groups_summary'])} evaluations.")
    L.append(f"- Budget: {'HIT in pass ' + str(run.stopped_in) if run.budget_hit else 'not hit'}; "
             f"wall {elapsed:.0f} s on {WORKERS} workers.")
    for p, s in run.pass_summary.items():
        L.append(f"  - pass {p}: {s['tasks']} tasks, {s['seconds']:.0f} s")
    L.append("")
    L.append("## Per-group table")
    L.append("")
    L.append("Columns: orbits = coarse menu (special + general); line24 = extra "
             "1/24-grid line/fixed orbits; evaluated = candidates per pass; "
             "types = distinct types sighted in the group; cubic = of those, in "
             "the cubic store; tet(menu) = tetragonal types sighted by our menu; "
             "tet(S-only) = seen only at Schmitt's printed points; NEW = types "
             "first minted in this group (menu-sighted in parentheses); max F "
             "(menu) = max facets over our menu / over Schmitt's rows too.")
    L.append("")
    L.append("| group | symbol | ops | orbits (spec+gen) | line24 | Schmitt rows | "
             "evaluated P1/P2/P3/P4/P5 | skipped | exact cells | types | cubic | "
             "tet(menu) | tet(S-only) | NEW (menu) | quar | max F menu / all |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in snap["groups_summary"]:
        e, s = r["evaluated"], r["skipped"]
        L.append(f"| {r['group']} | {r['symbol']} | {r['n_ops']} | {r['orbits_coarse']} "
                 f"({r['orbits_special']}+{r['orbits_general']}) | {r['orbits_line24']} | "
                 f"{r['schmitt_rows']} | {e['P1']}/{e['P2']}/{e['P3']}/{e['P4']}/{e['P5']} | "
                 f"{sum(s.values())} | {r['cells_exact']} | {r['types_distinct']} | "
                 f"{r['types_cubic_store']} | {r['types_tetragonal_menu_sighted']} | "
                 f"{r['types_tetragonal_schmitt_only']} | "
                 f"{r['new_types_first_here']} ({r['new_types_first_here_menu']}) | "
                 f"{r['quarantines']} | {r['max_facets_menu']} / {r['max_facets']} |")
    L.append("")
    # ---- b-ratio dependence
    L.append("## b-ratio dependence (tetragonal types sighted by OUR menu; "
             "Schmitt-printed sightings excluded)")
    L.append("")
    by_b = defaultdict(set)
    nb_hist = Counter()
    only_nongrid = 0
    only_bisect = 0
    only_schmitt_b = 0
    grid_set = {frac_str(b) for b in B_COARSE}
    schmitt_b_set = set(run.schmitt_b_used)
    for cid in menu_ids:
        sg = [s for s in store.types[cid]["sightings"] if s["kind"] != "schmitt_printed"]
        bs = {s["b"] for s in sg}
        nb_hist[len(bs)] += 1
        for b in bs:
            by_b[b].add(cid)
        if not (bs & grid_set):
            only_nongrid += 1
        if bs <= schmitt_b_set:
            only_schmitt_b += 1
        if all(s["pass"] == "P5" for s in sg):
            only_bisect += 1
    L.append(f"- Number of distinct b-ratio values each menu-sighted tetragonal type "
             f"was seen at (histogram): "
             + ", ".join(f"{k} value(s): {v} types" for k, v in sorted(nb_hist.items()))
             + ".")
    L.append(f"- Types seen at exactly ONE b-ratio value: {nb_hist.get(1, 0)} of "
             f"{len(menu_ids)}.")
    L.append(f"- Types seen ONLY at non-grid b-ratios: {only_nongrid} (only at "
             f"Schmitt's printed b-ratio values via P3: {only_schmitt_b}; only at "
             f"bisection midpoints, P5: {only_bisect}).")
    L.append("")
    L.append("| b-ratio | menu-sighted tetragonal types seen | seen ONLY here |")
    L.append("|---|---|---|")
    for b in sorted(by_b, key=lambda s: F(s)):
        only = sum(1 for cid in by_b[b]
                   if {s["b"] for s in store.types[cid]["sightings"]
                       if s["kind"] != "schmitt_printed"} == {b})
        L.append(f"| {b} | {len(by_b[b])} | {only} |")
    L.append("")
    L.append("## Schmitt printed b-ratios harvested (all)")
    L.append("")
    L.append(", ".join(f"{d['b']} ({d['rows']} rows)" for d in run.schmitt_b_all))
    L.append("")
    L.append("## Cubic-store types re-sighted in tetragonal groups")
    L.append("")
    L.append("| id | name | F | f-vector | p-vector | aut | phase-1 sightings | "
             "tetragonal sightings | first tetragonal witness |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for cid in store.order:
        e = store.types[cid]
        if cid not in run.cubic_ids or not e["sightings"]:
            continue
        w = e["first_witness"]
        L.append(f"| `{cid}` | {e.get('seed_name') or ''} | {e['f_vector'][2]} | "
                 f"{tuple(e['f_vector'])} | {pvec_compact(e['p_vector'])} | "
                 f"{e['aut_order']} | {e['phase1_sightings']} | {len(e['sightings'])} | "
                 f"{w['group']} {w['group_symbol']} ({', '.join(w['point'])}) b={w['b']} |")
    L.append("")
    L.append(f"## Tetragonal types NOT matched against catalog snapshot of {SNAPSHOT} "
             f"({len(new_ids)})")
    L.append("")
    L.append("Sorted by (facets, p-vector). Witness = first sighting in run order "
             "(kind schmitt_printed = Schmitt's printed generating point; the "
             "S-only column marks types seen ONLY there). dim: 0 fixed point / 1 "
             "line sample / 2 plane sample / 3 general. #b = number of distinct "
             "b-ratio values the type was seen at.")
    L.append("")
    L.append("| id | F | f-vector | p-vector | aut | witness group | point | kind | "
             "stab | dim | orbit | b | #b | sightings | S-only |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for cid in sorted(new_ids, key=lambda c: (store.types[c]["f_vector"][2],
                                              store.types[c]["p_vector"], c)):
        e = store.types[cid]
        w = e["first_witness"]
        nb = len({s["b"] for s in e["sightings"]})
        L.append(f"| `{cid}` | {e['f_vector'][2]} | {tuple(e['f_vector'])} | "
                 f"{pvec_compact(e['p_vector'])} | {e['aut_order']} | "
                 f"{w['group']} {w['group_symbol']} | ({', '.join(w['point'])}) | "
                 f"{w['kind']} | {w['stabilizer_order']} | {w['stratum_dim']} | "
                 f"{w['orbit_conventional']} | {w['b']} | {nb} | {len(e['sightings'])} | "
                 f"{'Y' if e['schmitt_printed_only'] else ''} |")
    L.append("")
    L.append(f"## Quarantines ({len(run.quarantines)})")
    L.append("")
    if not run.quarantines:
        L.append("None. No >38-facet sighting, no float/exact disagreement, no "
                 "crash, no Fedorov violation, no stab/aut inconsistency, no "
                 "orbit-congruence violation, no Schmitt f-vector mismatch.")
    qc = Counter(q["reason"] for q in run.quarantines)
    if qc:
        L.append("By reason: " + ", ".join(f"{k}: {v}" for k, v in sorted(qc.items())))
        L.append("")
    for q in run.quarantines[:400]:
        L.append(f"- group {q['group']} point ({', '.join(q['point'])}) [{q['kind']}, "
                 f"b={q.get('b')}, {q['pass']}]: **{q['reason']}** — {q['detail']}")
    if len(run.quarantines) > 400:
        L.append(f"- ... {len(run.quarantines) - 400} more in phase2_types.json")
    if run.gb_purges:
        L.append("")
        L.append("(group, b) purges: " + "; ".join(
            f"#{p['group']} b={p['b']}: {p['sightings_removed']} sightings removed, "
            f"{len(p['types_dropped'])} types dropped" for p in run.gb_purges))
    L.append("")
    L.append("## Honest limits (what this sweep did NOT do)")
    L.append("")
    L.append("- Orbits: special positions on the per-coordinate {1,2,3,4,6,8,12} "
             "grid plus 1/24-grid samples of Wyckoff LINES (dim <= 1) only; "
             "plane strata are sampled at the coarse grid only (1/24 plane "
             "samples counted and skipped by design); denominators beyond 24 "
             "not scanned; general position = 2 rational controls per group "
             "(Schmitt's survey covers general position densely).")
    L.append(f"- Metric: {len(B_COARSE)} coarse rational b-ratios, "
             f"{len(run.schmitt_b_used)} Schmitt printed non-grid values "
             f"(cap {N_SCHMITT_B} of {len(run.schmitt_b_all)} harvested — the "
             f"rest were NOT run), bisection midpoints to depth {BISECT_DEPTH} "
             f"(cap {BISECT_CAP_PER_ORBIT} evaluations/orbit, {run.bisect_caps} "
             f"cap hits). Irrational transition values (e.g. sqrt 2) are not "
             f"representable and were bracketed, not hit. Schmitt's 1001-step "
             f"b-ratio grid is far finer than ours.")
    L.append("- Two exact cells per orbit (representative + one congruence "
             "check); the other cells were float-checked for (F, p-vector) only.")
    L.append("- Aut orders are combinatorial map automorphism counts; geometric "
             "stabilizer certification is G4/V2, not claimed.")
    L.append("- Type identity relies on canon_code; f/p-vector collisions between "
             "distinct codes are not merged.")
    L.append("- Schmitt screen is f-vector-level (his tables print f-vectors, not "
             "types) and one-directional; type-level diligence against his "
             "tetragonal data is NOT done (digitization covers cubic only).")
    L.append("- Enantiomorphic pairs (76/78, 91/95, 92/96) share Schmitt's printed "
             "table; each row was run in both groups with the printed point.")
    if run.budget_hit:
        L.append(f"- BUDGET HIT in pass {run.stopped_in}: {sk} candidates skipped "
                 f"(counted per group and pass in phase2_types.json); every later "
                 f"pass did not run.")
    else:
        L.append("- Budget NOT hit: all five passes completed for all 68 groups; "
                 "nothing was cut except the explicit caps above.")
    L.append("")
    L.append(f"Run wall time: {elapsed:.0f} s ({WORKERS} worker processes, ordered "
             f"absorption; phase2_types.json contains no timings except elapsed_s "
             f"and per-group CPU seconds).")
    L.append("")
    L.append("## Run log")
    L.append("")
    L.append("```")
    L.extend(run.log)
    L.append("```")
    open(OUT_MD, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
