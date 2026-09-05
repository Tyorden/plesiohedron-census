#!/usr/bin/env python
"""sweep_phase2_hexagonal.py — PHASE 2, batch 2: the hexagonal family
(trigonal + hexagonal groups, IT 143-194, 52 groups), same machinery and gate
discipline as the accepted batch-1 driver sweep_phase2_tetragonal.py.

Spec: ../PHASE2_PLAN.md (sections 1-3, hexagonal batch), ../ANCHORS.md (G3
invariant, the G2b and G2c blocks, kill criteria). Gate: phase2/g2c_controls.py
must have exited 0 (G2C_RESULT.md) before this runs — asserted at start.

REUSE (imported, not re-typed): sweep_phase2_tetragonal.{scan_grid, build_menu,
exact_cell_warm, Store2, frac_str, pvec_compact, code_id, ...} and the
sweep_phase1 helpers; the ACCEPTED phase-2 Gram modules (phase2/metric.py,
sweep_voronoi_gram.py, exact_cell_gram.py; G2b 21/21 + G2c PASS) unmodified.
What differs from batch 1, and only that:
  * Gram = metric.gram_hexagonal(b) in the ITA hexagonal basis of the frozen
    ops (rhombohedral groups on hexagonal axes); R^T G R = G asserted per cell.
  * Schmitt rows come from the digitization schmitt_hexagonal_tables.json
    (text layer + visual cross-read, 2026-09-04), NOT harvested at run time;
    the printed points are B'' coordinates and are converted by the G2c-
    confirmed convention H1: x' = 2x'', y' = x''+y'', z' = z''. Second members
    of the seven enantiomorphic pairs sharing one printed table run the
    printed point verbatim first, then z -> -z (the batch-1 95/96 rule); the
    conversion used is recorded per sighting; failure of both = quarantine
    schmitt_fvec_mismatch (never patched).
  * The store is seeded with ALL 891 types of the batch-1 store
    phase2_types.json (102 cubic-first + 789 tetragonal-first, sha256
    verified) so cross-system coincidences are visible; types minted here are
    marked first_sighting_system = "hexagonal (phase 2 batch 2)".
  * RULE 29 RESUMABILITY: the run is a sequence of FOREGROUND invocations,
    each with a wall budget (PHASE2_BUDGET_S, default 480 s). Every completed
    task's records are appended (one JSON line, flushed + fsynced) to
    phase2_hexagonal_records.jsonl IN TASK ORDER; on start the log is
    re-absorbed (deterministic, task order) and the run continues from the
    first task not in the log. A budget stop writes the store with
    complete=false and exits 0 with the resume command; the final invocation
    writes complete=true. The store is therefore a deterministic function of
    the log, and the log a deterministic function of the task list.

Pipeline per candidate (group, orbit point, b-ratio = c/a):
  orbit.py (exact) -> metric.gram_hexagonal(b) with R^T G R = G asserted
  -> sweep_gram float proposal (W=2; W=3, W=4 retries on the window guard)
  -> exact_cell_gram.clip_cell_gram on pts[0] (warm-started cutoff; the
     G-norm certificate 4*rho^2 <= D^2 asserted) -> canon_code
  -> ORBIT-CONGRUENCE CHECK on a second orbit cell (same F, p, code, aut) —
     a violation quarantines the whole (group, b) pair (purged, skipped).
G3 INVARIANT, kill criteria (>38 facets float or exact = quarantine; crash =
quarantine; float/exact disagreement without degeneracy flag = quarantine;
stab | aut; lattice-degenerate orbits must be seeded parallelohedra) exactly
as in batch 1.

PASSES (deterministic order): P1 coarse grid (all metric-independent orbits x
13 b-ratios 1/2..7/2 step 1/4); P2 Schmitt collision screen (every printed
row, both groups of a shared table, at the printed b); P3 the P1 orbits x the
N_SCHMITT_B most frequent printed NON-grid b-ratios; P4 Wyckoff-line
refinement (1/24 grid, dim <= 1) x 13 b; P5 transition bisection (depth <= 4,
cap 26 evaluations/orbit).

Run (from harness/), repeat until "COMPLETE":
  nice -n 10 python3 \
      sweep_phase2_hexagonal.py
Env: PHASE2_BUDGET_S (480), PHASE2_WORKERS (10), PHASE2_SMOKE=1 (3 groups,
2 b-ratios; writes to *_smoke files).
Writes: phase2_hexagonal_types.json, phase2_hexagonal_records.jsonl (resume
log, gitignored like the raw store), PHASE2_HEX_RESULT.md. Exit 0 iff the
invocation ended cleanly (budget stop or completion); exit 2 if the G2c gate
result is missing.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import hashlib                                       # noqa: E402
import json                                          # noqa: E402
import multiprocessing as mp                         # noqa: E402
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
from canon_code import canonical_code                # noqa: E402
from sweep_phase1 import (MAX_FACETS, wyckoff_dim, is_lattice, ChainError,   # noqa: E402
                          frac_str, pvec_compact, code_id)
import sweep_phase2_tetragonal as S2                 # noqa: E402
from sweep_phase2_tetragonal import (build_menu, exact_cell_warm, Store2,     # noqa: E402
                                     BISECT_DEPTH, BISECT_CAP_PER_ORBIT,
                                     PARALLELOHEDRA, MAX_W)

GROUPS = S2.GROUPS
SMOKE = os.environ.get("PHASE2_SMOKE") == "1"
SFX = "_smoke" if SMOKE else ""
PRIOR_STORE = os.path.join(HERE, "phase2_types.json")
PRIOR_SUMS = os.path.join(HERE, "phase2_types.SHA256SUMS")
TABLES = os.path.join(HERE, "schmitt_hexagonal_tables.json")
G2C_RESULT = os.path.join(HERE, "phase2", "G2C_RESULT.md")
OUT_JSON = os.path.join(HERE, f"phase2_hexagonal_types{SFX}.json")
OUT_LOG = os.path.join(HERE, f"phase2_hexagonal_records{SFX}.jsonl")
OUT_MD = os.path.join(HERE, f"PHASE2_HEX_RESULT{SFX}.md")

SNAPSHOT = "2026-09-04"
SYSTEM = "hexagonal (phase 2 batch 2)"
HEX = list(range(143, 195))
B_COARSE = [F(k, 4) for k in range(2, 15)]          # 1/2 .. 7/2 step 1/4
N_SCHMITT_B = 5
ENANTIO_SECOND = {145, 153, 154, 170, 172, 179, 181}
BUDGET_S = float(os.environ.get("PHASE2_BUDGET_S", 480))
WORKERS = int(os.environ.get("PHASE2_WORKERS", 10))
if SMOKE:
    HEX = [143, 166, 178]
    B_COARSE = [F(1, 2), F(2)]
    N_SCHMITT_B = 1

PASSES = ("P1", "P2", "P3", "P4", "P5")


# ------------------------------------------------------------ conversions ---

def h1(p):
    """Schmitt's B'' = (2b1'+b2', b2', b3') coordinates -> ITA hexagonal basis
    (ANCHORS G2c H1, confirmed by g2c_controls.py on six printed rows)."""
    x, y, z = p
    return (2 * x, x + y, z)


def zflip(p):
    return (p[0], p[1], -p[2])


# ------------------------------------------------------------------ chain ---

def evaluate(num, p, b, kind):
    """Full chain on one candidate (batch-1 evaluate with the hexagonal Gram).
    Raises ChainError on any kill criterion."""
    entry = GROUPS[num]
    t0 = time.time()
    ob = orbit.orbit(entry, p)
    dim = 3 if ob["stabilizer_order"] == 1 else wyckoff_dim(entry, p)
    pts, period = orbit.scale_orbit(ob["points"])
    lat = is_lattice(pts, period)
    G = metric.gram_hexagonal(b)
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


def eval_schmitt(num, printed_pt, b, extra):
    """P2: printed B'' point -> H1; second enantiomorphs: verbatim, then z->-z.
    Returns ONE record (the reproducing conversion, else the last attempt
    with reason schmitt_fvec_mismatch carrying every attempt)."""
    fv = tuple(extra["schmitt_fvec"])
    convs = [("H1", h1(printed_pt))]
    if num in ENANTIO_SECOND:
        convs.append(("H1+zflip", h1(zflip(printed_pt))))
    attempts = []
    for label, p in convs:
        rec = eval_record(num, p, b, "schmitt_printed", "P2",
                          dict(extra, conversion=label, printed_point=[frac_str(x) for x in printed_pt]))
        attempts.append((label, rec.get("fvec") if rec["verdict"] == "ok" else rec.get("reason")))
        if rec["verdict"] == "ok" and tuple(rec["fvec"]) == fv:
            rec["conversion_attempts"] = attempts
            return rec
        if rec["verdict"] == "quarantined" and rec["reason"] != "schmitt_fvec_mismatch" \
                and label == convs[-1][0] and len(convs) == 1:
            rec["conversion_attempts"] = attempts
            return rec                              # a genuine chain quarantine
    rec = dict(rec)
    if rec["verdict"] == "ok":
        rec.update(verdict="quarantined", reason="schmitt_fvec_mismatch",
                   detail=f"printed {fv}; attempts {attempts}")
    else:
        rec.update(detail=f"{rec.get('detail')}; printed {fv}; attempts {attempts}")
    rec["conversion_attempts"] = attempts
    return rec


def bisect_orbit(num, p, kind, chain):
    """Batch-1 bisection (verbatim logic) on the hexagonal chain."""
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
    if pname == "P2":
        num, pstr, bstr, extra = pay
        return tid, [eval_schmitt(num, tuple(F(s) for s in pstr), F(bstr), extra)]
    num, pstr, kind, bstr = pay[:4]
    extra = pay[4] if len(pay) > 4 else None
    p = tuple(F(s) for s in pstr)
    return tid, [eval_record(num, p, F(bstr), kind, pname, extra)]


# ----------------------------------------------------------------- store ---

class Store3(Store2):
    """Batch-1 Store2 + seeding from the batch-1 store (cubic + tetragonal)."""

    def add_prior(self, cid, e):
        assert cid not in self.types
        self.types[cid] = {
            "canon_code": e["canon_code"], "f_vector": list(e["f_vector"]),
            "p_vector": list(e["p_vector"]), "aut_order": e["aut_order"],
            "first_sighting_system": e["first_sighting_system"],
            "seeded": e["seeded"], "seed_name": e.get("seed_name"),
            "seed_source": e.get("seed_source"),
            "prior_first_witness": e.get("first_witness") or e.get("phase1_first_witness"),
            "prior_sightings": len(e["sightings"]) + e.get("phase1_sightings", 0),
            "first_witness": None, "sightings": [],
        }
        self.order.append(cid)

    def sight(self, code_str, fvec, pvec, aut, sighting):
        cid, is_new = S2.Store.sight(self, code_str, fvec, pvec, aut, sighting)
        e = self.types[cid]
        if is_new:
            e["first_sighting_system"] = SYSTEM
            e["prior_sightings"] = 0
        elif e["first_witness"] is None:
            e["first_witness"] = sighting      # first HEX sighting of a prior type
        return cid, is_new

    def purge_group_b(self, num, b_str):
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
            if not keep and e["first_sighting_system"] == SYSTEM:
                dropped.append(cid)
                del self.types[cid]
                self.order.remove(cid)
        return removed, dropped


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------ main ---

class Run:
    def __init__(self):
        self.t_start = time.time()
        self.log = []
        self.store = Store3()
        self.prior_ids = set()
        self.prior_system = {}
        self.records = []
        self.quarantines = []
        self.gb_quarantined = set()
        self.gb_purges = []
        self.evaluated = Counter()
        self.skipped = Counter()
        self.stats = defaultdict(self.new_stat)
        self.max_f_stored = 0
        self.max_f_menu = 0
        self.menu_F = Counter()
        self.max_f_quarantined = 0
        self.budget_hit = False
        self.stopped_in = None
        self.menus = {}
        self.schmitt_rows = []
        self.schmitt_b_all = []
        self.schmitt_b_used = []
        self.schmitt_screen = Counter()
        self.codes_at = defaultdict(dict)
        self.bisect_caps = 0
        self.bisect_evals = 0
        self.pass_summary = {}
        self.pass_done = Counter()       # pass -> tasks absorbed (log + this run)
        self.pass_total = {}
        self.n_from_log = 0
        self.n_this_run = 0
        self.invocations = 0

    @staticmethod
    def new_stat():
        return {"cells_exact": 0, "types": set(), "new_first_here": [],
                "quar": 0, "max_f": 0, "prior_types": set(), "hex_types": set(),
                "lattice": 0, "float_superseded": 0, "nonsimple_cells": 0,
                "seconds": 0.0}

    def say(self, s):
        print(s, flush=True)
        self.log.append(s)

    # ---- absorb one evaluation record into the store (batch-1 logic)
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
            if rec.get("reason") == "schmitt_fvec_mismatch":
                self.schmitt_screen["mismatch"] += 1
            elif rec["kind"] == "schmitt_printed":
                self.schmitt_screen["quarantined_other"] += 1
            self._quarantine(rec)
            self.codes_at[key][b_str] = None
            return
        st["seconds"] += rec["seconds"]
        cid = code_id(rec["code_str"])
        if rec["lattice_degenerate"]:
            ok = (cid in self.prior_ids
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
            assert tuple(rec["fvec"]) == tuple(rec["schmitt_fvec"])
            self.schmitt_screen["reproduced"] += 1
            self.schmitt_screen["conv_" + rec["conversion"]] += 1
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
        if rec["kind"] == "schmitt_printed":
            sighting["printed_point_Bpp"] = rec["printed_point"]
            sighting["conversion"] = rec["conversion"]
            sighting["schmitt_primary_group"] = rec["schmitt_primary_group"]
            sighting["pdf_page"] = rec["pdf_page"]
        cid, is_new = self.store.sight(rec["code_str"], rec["fvec"], rec["pvec"],
                                       rec["aut"], sighting)
        self.codes_at[key][b_str] = cid
        st["cells_exact"] += 2 if rec["congruence_checked"] else 1
        st["types"].add(cid)
        (st["prior_types"] if cid in self.prior_ids else st["hex_types"]).add(cid)
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
                                 "reason", "detail", "conversion_attempts") if k in rec}
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

    def absorb_task(self, pname, out):
        for rec in out:
            self.absorb(rec)
        self.pass_done[pname] += 1

    # ---- passes with log-resume
    def run_pass(self, pool, pname, tasks, logged, logfh):
        """tasks: full deterministic task list for the pass. logged: {tid: out}
        from the resume log. Absorbs logged tasks in order, runs the rest
        through the pool (ordered imap), appends each completed task to the
        log. Returns True if the pass completed within budget."""
        t0 = time.time()
        self.pass_total[pname] = len(tasks)
        n_logged = 0
        for tid, _, _ in tasks:
            if tid in logged:
                self.absorb_task(pname, logged[tid])
                n_logged += 1
            else:
                break
        # a logged task after a gap would violate task order; assert none
        assert not any(t[0] in logged for t in tasks[n_logged:]), "resume log out of order"
        self.n_from_log += n_logged
        todo = tasks[n_logged:]
        if n_logged:
            self.say(f"pass {pname}: {n_logged}/{len(tasks)} tasks absorbed from the resume log")
        if not todo:
            self.pass_summary[pname] = {"tasks": len(tasks), "seconds_this_run": 0.0}
            return True
        if time.time() - self.t_start > BUDGET_S:
            self.budget_hit, self.stopped_in = True, pname
            self.say(f"BUDGET HIT before {pname}: {len(todo)}/{len(tasks)} tasks remain")
            return False
        it = pool.imap(worker, todo, chunksize=4 if pname != "P5" else 1)
        n_done = 0
        for (tid, out) in it:
            assert tid == todo[n_done][0]
            logfh.write(json.dumps({"tid": tid, "pass": pname, "out": out},
                                   separators=(",", ":")) + "\n")
            logfh.flush()
            os.fsync(logfh.fileno())
            self.absorb_task(pname, out)
            n_done += 1
            self.n_this_run += 1
            if n_done % 2000 == 0:
                self.say(f"  {pname}: {n_logged + n_done}/{len(tasks)} tasks, store "
                         f"{len(self.store.order)} types, quar {len(self.quarantines)}, "
                         f"{time.time() - self.t_start:.0f}s")
            if time.time() - self.t_start > BUDGET_S and n_done < len(todo):
                self.budget_hit, self.stopped_in = True, pname
                self.say(f"BUDGET HIT in {pname} after {n_logged + n_done}/{len(tasks)} "
                         f"tasks ({len(todo) - n_done} remain for the next invocation)")
                pool.terminate()
                return False
        self.pass_summary[pname] = {"tasks": len(tasks), "seconds_this_run": time.time() - t0}
        self.say(f"pass {pname} complete: {len(tasks)} tasks ({n_done} this run) in "
                 f"{time.time() - t0:.0f}s (store {len(self.store.order)} types, "
                 f"quarantines {len(self.quarantines)})")
        return True

    # ---- output
    def menu_sighted(self, cid):
        return any(s["kind"] != "schmitt_printed"
                   for s in self.store.types[cid]["sightings"])

    def snapshot(self, complete):
        elapsed = time.time() - self.t_start
        for cid in self.store.order:
            e = self.store.types[cid]
            e["sighted_by_kinds"] = sorted({s["kind"] for s in e["sightings"]})
            e["schmitt_printed_only"] = (bool(e["sightings"])
                                         and not self.menu_sighted(cid))
        groups_summary = [self.group_row(num) for num in HEX]
        new_ids = [c for c in self.store.order if c not in self.prior_ids]
        return {
            "generated_by": "sweep_phase2_hexagonal.py (Phase 2 batch 2, hexagonal family, "
                            + SNAPSHOT + ")",
            "complete": complete,
            "catalog_snapshot": SNAPSHOT,
            "language_note": "types with first_sighting_system '" + SYSTEM + "' are NOT "
                "MATCHED AGAINST THE RECORDS CHECKED AS OF " + SNAPSHOT + " (= the batch-1 "
                "store: cubic + tetragonal, + this run); no novelty claim is made; the P2 "
                "screen is f-vector-level and one-directional; type-level collision against "
                "Schmitt's printed hexagonal-family cells is the triage/collision step",
            "resume": {"invocations_seen_in_log": self.invocations,
                       "tasks_from_log": self.n_from_log, "tasks_this_run": self.n_this_run,
                       "pass_done": dict(self.pass_done), "pass_total": self.pass_total,
                       "log_file": os.path.basename(OUT_LOG)},
            "scan": {"groups": HEX, "grid_denominators": list(S2.ALLOWED_DENS),
                     "scan_period": S2.SCAN, "fine_scan": S2.FINE_SCAN,
                     "general_controls_per_group": S2.N_GENERAL,
                     "b_coarse": [frac_str(b) for b in B_COARSE],
                     "schmitt_b_all_digitized": self.schmitt_b_all,
                     "schmitt_b_used": self.schmitt_b_used,
                     "n_schmitt_b_cap": N_SCHMITT_B,
                     "schmitt_point_convention": "H1: x'=2x'', y'=x''+y'', z'=z'' (ANCHORS G2c); "
                                                 "second enantiomorphs verbatim then z->-z",
                     "bisect_depth": BISECT_DEPTH,
                     "bisect_cap_per_orbit": BISECT_CAP_PER_ORBIT,
                     "max_facets_kill": MAX_FACETS, "max_W": MAX_W,
                     "workers": WORKERS, "budget_s_per_invocation": BUDGET_S, "smoke": SMOKE},
            "seed_store": {"file": "phase2_types.json", "sha256": self.prior_sha,
                           "n_types": len(self.prior_ids),
                           "by_system": dict(Counter(self.prior_system.values()))},
            "types": {cid: self.store.types[cid] for cid in self.store.order},
            "type_order": self.store.order,
            "n_types_prior_store": len(self.prior_ids),
            "n_types_hexagonal_new": len(new_ids),
            "n_types_hexagonal_menu_sighted": sum(1 for c in new_ids if self.menu_sighted(c)),
            "n_types_hexagonal_schmitt_printed_only": sum(
                1 for c in new_ids if not self.menu_sighted(c)),
            "groups_summary": groups_summary,
            "pass_summary": self.pass_summary,
            "schmitt_screen": dict(self.schmitt_screen),
            "quarantines": self.quarantines,
            "group_b_quarantined": sorted(self.gb_quarantined),
            "group_b_purges": self.gb_purges,
            "bisect_cap_hits": self.bisect_caps,
            "max_facets_stored": self.max_f_stored,
            "max_facets_from_our_menu": self.max_f_menu,
            "max_facets_quarantined": self.max_f_quarantined,
            "budget_hit": self.budget_hit, "stopped_in_pass": self.stopped_in,
            "elapsed_s_this_invocation": round(elapsed),
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
            "evaluated": {p: self.evaluated[(num, p)] for p in PASSES},
            "skipped": {p: self.skipped[(num, p)] for p in PASSES},
            "cells_exact": st["cells_exact"],
            "types_distinct": len(st["types"]),
            "types_prior_store": len(st["prior_types"]),
            "types_hexagonal": len(st["hex_types"]),
            "types_hexagonal_menu_sighted": sum(
                1 for c in st["hex_types"] if self.menu_sighted(c)),
            "types_hexagonal_schmitt_only": sum(
                1 for c in st["hex_types"] if not self.menu_sighted(c)),
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
        self.say(f"  [checkpoint {'FINAL' if complete else 'partial'} "
                 f"{os.path.basename(OUT_JSON)}: {len(self.store.order)} types, "
                 f"{len(self.records)} records, {time.time()-t0:.1f}s]")
        return snap


def load_log():
    """{pass: {tid: out}} from the resume log; a torn last line is dropped."""
    logged = defaultdict(dict)
    n_inv = 0
    if not os.path.exists(OUT_LOG):
        return logged, n_inv
    with open(OUT_LOG) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                break                                   # torn tail: stop here
            if "invocation" in d:
                n_inv += 1
                continue
            logged[d["pass"]][d["tid"]] = d["out"]
    return logged, n_inv


def main():
    if not os.path.exists(G2C_RESULT) or "ALL REQUIRED ASSERTIONS PASS" not in open(G2C_RESULT).read():
        print("G2c gate result missing or not PASS — batch 2 does not run (ANCHORS G2c)")
        return 2
    run = Run()
    say = run.say
    logged, n_inv = load_log()
    run.invocations = n_inv + 1
    say(f"PHASE 2 hexagonal sweep — invocation {run.invocations} (workers {WORKERS}, "
        f"budget {BUDGET_S:.0f} s per invocation{', SMOKE' if SMOKE else ''}); resume log has "
        f"{sum(len(v) for v in logged.values())} tasks")

    # ---- seed: the whole batch-1 store (cubic + tetragonal), sha verified
    sha = sha256_file(PRIOR_STORE)
    expected = open(PRIOR_SUMS).read().split()[2]
    assert sha == expected, f"phase2_types.json sha256 {sha} != {expected}"
    prior = json.load(open(PRIOR_STORE))
    assert prior["complete"] and not prior["budget_hit"]
    for cid in prior["type_order"]:
        e = prior["types"][cid]
        run.store.add_prior(cid, e)
        run.prior_system[cid] = e["first_sighting_system"]
    run.prior_ids = set(run.store.order)
    run.prior_sha = sha
    assert len(run.prior_ids) == 891
    say(f"seeded {len(run.prior_ids)} types from phase2_types.json (sha256 {sha[:16]}...): "
        f"{dict(Counter(run.prior_system.values()))}")

    # ---- Schmitt rows from the digitization
    tables = json.load(open(TABLES))
    rows = []
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            rows.append({"groups": list(blk["groups"]), "f_vector": list(r["f"]),
                         "b_ratio": r["b"], "point": list(r["pt"]), "pdf_page": r["pdf_page"]})
    run.schmitt_rows = rows
    g2c = {(143, "3497/1000", ("1/6", "0", "0")), (147, "3497/1000", ("33/100", "-1/500", "0")),
           (155, "797/1000", ("-193/750", "-53/250", "6/125")),
           (166, "527/1000", ("-16/375", "-16/125", "31/500")),
           (178, "163/200", ("32/125", "-19/125", "43/1500")), (194, "797/1000", ("1/3", "0", "1/4"))}
    have = {(g, r["b_ratio"], tuple(r["point"])) for r in rows for g in r["groups"]}
    assert g2c <= have, "G2c rows missing from the digitization"
    bc = Counter(r["b_ratio"] for r in rows)
    grid = {frac_str(b) for b in B_COARSE}
    run.schmitt_b_all = [{"b": b, "rows": n} for b, n in
                         sorted(bc.items(), key=lambda kv: (-kv[1], F(kv[0])))]
    run.schmitt_b_used = [b for b, _ in sorted(bc.items(), key=lambda kv: (-kv[1], F(kv[0])))
                          if b not in grid][:N_SCHMITT_B]
    say(f"digitized {len(rows)} Schmitt hexagonal-family rows over "
        f"{len({g for r in rows for g in r['groups']})} groups ({tables['_meta']['n_blocks']} blocks); "
        f"{len(bc)} distinct printed b-ratios; using non-grid b-ratios "
        f"{run.schmitt_b_used} for P3 (cap {N_SCHMITT_B})")

    ctx = mp.get_context("fork")
    pool = ctx.Pool(WORKERS)
    logfh = open(OUT_LOG, "a")
    logfh.write(json.dumps({"invocation": run.invocations, "started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                            "budget_s": BUDGET_S, "workers": WORKERS}) + "\n")
    logfh.flush()
    completed = False
    try:
        # ---- menus (recomputed each invocation; deterministic, seconds)
        tasks = [(i, "menu", num) for i, num in enumerate(HEX)]
        for tid, out in pool.imap(worker, tasks, chunksize=1):
            run.menus[out["group"]] = out
        n_coarse = sum(len(m["coarse"]) for m in run.menus.values())
        n_fine = sum(len(m["fine"]) for m in run.menus.values())
        n_pl = sum(m["planes24_skipped"] for m in run.menus.values())
        say(f"menus: {n_coarse} coarse orbits (special + general), {n_fine} "
            f"line/fixed orbits new on the 1/24 grid, {n_pl} plane orbits at "
            f"1/24 skipped by design")

        def orbit_tasks(pname, kinds_from, b_list):
            tasks = []
            for num in HEX:
                for pstr, kind in run.menus[num][kinds_from]:
                    for b in b_list:
                        tasks.append((len(tasks), pname, (num, pstr, kind, frac_str(b))))
            return tasks

        # ---- P1
        if not run.run_pass(pool, "P1", orbit_tasks("P1", "coarse", B_COARSE), logged["P1"], logfh):
            raise StopIteration
        # ---- P2 Schmitt screen (printed B'' points; conversions in eval_schmitt)
        tasks = []
        for r in rows:
            for g in r["groups"]:
                if g not in HEX:
                    continue
                tasks.append((len(tasks), "P2", (g, r["point"], r["b_ratio"],
                                                 {"schmitt_fvec": r["f_vector"],
                                                  "schmitt_primary_group": r["groups"][0],
                                                  "pdf_page": r["pdf_page"]})))
        if not run.run_pass(pool, "P2", tasks, logged["P2"], logfh):
            raise StopIteration
        say(f"Schmitt screen: {dict(run.schmitt_screen)}")
        # ---- P3
        if not run.run_pass(pool, "P3", orbit_tasks("P3", "coarse", [F(b) for b in run.schmitt_b_used]),
                            logged["P3"], logfh):
            raise StopIteration
        # ---- P4
        if not run.run_pass(pool, "P4", orbit_tasks("P4", "fine", B_COARSE), logged["P4"], logfh):
            raise StopIteration
        # ---- P5
        tasks = []
        for num in HEX:
            for pstr, kind in run.menus[num]["coarse"] + run.menus[num]["fine"]:
                key = (num, tuple(pstr), kind)
                chain = sorted(run.codes_at[key].items(), key=lambda kv: F(kv[0]))
                if any(c0 != c1 and c0 is not None and c1 is not None
                       for (_, c0), (_, c1) in zip(chain, chain[1:])):
                    tasks.append((len(tasks), "P5", (num, pstr, kind, chain)))
        say(f"P5: {len(tasks)} orbits with at least one code transition")
        if not run.run_pass(pool, "P5", tasks, logged["P5"], logfh):
            raise StopIteration
        completed = True
    except StopIteration:
        pass
    finally:
        pool.terminate()
        pool.join()
        logfh.close()

    elapsed = time.time() - run.t_start
    new_ids = [c for c in run.store.order if c not in run.prior_ids]
    say("")
    if completed:
        say(f"COMPLETE in this invocation after {elapsed:.0f}s: "
            f"{sum(run.evaluated.values())} candidates evaluated ({sum(run.skipped.values())} skipped), "
            f"{len(run.store.order)} types in store ({len(run.prior_ids)} prior store + "
            f"{len(new_ids)} hexagonal, not matched against the records checked as of {SNAPSHOT}), "
            f"max stored facets {run.max_f_stored}, {len(run.quarantines)} quarantines")
        snap = run.checkpoint(True)
        write_result(run, snap, new_ids, elapsed)
        say("wrote " + os.path.basename(OUT_MD))
    else:
        say(f"INCOMPLETE (budget stop in pass {run.stopped_in}) after {elapsed:.0f}s: "
            f"{run.n_this_run} tasks this invocation, {run.n_from_log} from the log; "
            f"pass_done={dict(run.pass_done)} of {run.pass_total}")
        run.checkpoint(False)
        say("RESUME: cd " + HERE + " && nice -n 10 <MathProofs>/"
            "paper_prep_venv/bin/python sweep_phase2_hexagonal.py")
    return 0


# ---------------------------------------------------------------- report ---

def write_result(run, snap, new_ids, elapsed):
    store = run.store
    L = []
    L.append(f"# PHASE 2 result — hexagonal-family sweep (batch 2, {SNAPSHOT})"
             + (" [SMOKE RUN]" if SMOKE else ""))
    L.append("")
    L.append("Spec: `../PHASE2_PLAN.md` (hexagonal batch); gates `../ANCHORS.md` G3 "
             "(enforced per stored sighting), G2b + G2c blocks (accepted Gram modules; "
             "`phase2/G2C_RESULT.md` PASS asserted at start), KILL CRITERIA (>38 facets = "
             "quarantine; congruence violation = (group, b) quarantine). Pipeline: "
             "`orbit.py` -> `phase2/metric.py` (integer Gram [[2q^2,-q^2,0],[-q^2,2q^2,0],"
             "[0,0,2p^2]] in the ITA hexagonal basis, R^T G R = G asserted) -> "
             "`phase2/sweep_voronoi_gram.py` (float proposal, W=2..4) -> "
             "`phase2/exact_cell_gram.py` (all-Fraction, G-norm certificate 4 rho^2 <= D^2 "
             "asserted; warm-started cutoff) -> `canon_code.py`; a second orbit cell is "
             "clipped exactly on every candidate with orbit size > 1. Frozen G1 "
             "`spacegroups.json` only (rhombohedral groups on hexagonal axes). Store seeded "
             "with all 891 batch-1 types (cubic + tetragonal). Driver: "
             "`sweep_phase2_hexagonal.py` (batch-1 driver's menu/passes/store imported; "
             "resumable foreground invocations per rule 29, resume log "
             f"`{os.path.basename(OUT_LOG)}`).")
    L.append("")
    L.append(f"**LANGUAGE (G5): every type marked hexagonal below means \"not matched "
             f"against the records checked as of {SNAPSHOT}\" (= the batch-1 store + this "
             f"run). NO novelty claim, NO naming. The P2 screen is f-vector-level and "
             f"one-directional; type-level collision against Schmitt's printed "
             f"hexagonal-family cells is the triage/collision step.**")
    L.append("")
    ev = sum(run.evaluated.values())
    sk = sum(run.skipped.values())
    L.append("## Headline")
    L.append("")
    L.append(f"- Groups: {len(HEX)} (IT {HEX[0]}-{HEX[-1]}); coarse orbits "
             f"{sum(r['orbits_coarse'] for r in snap['groups_summary'])} "
             f"({sum(r['orbits_special'] for r in snap['groups_summary'])} special + "
             f"{sum(r['orbits_general'] for r in snap['groups_summary'])} general); "
             f"1/24-grid line/fixed orbits {sum(r['orbits_line24'] for r in snap['groups_summary'])} "
             f"(plane samples at 1/24 skipped by design: "
             f"{sum(r['planes24_skipped_by_design'] for r in snap['groups_summary'])}).")
    L.append(f"- b-ratios: coarse {[frac_str(b) for b in B_COARSE]}; Schmitt "
             f"non-grid values used (P3) {run.schmitt_b_used} (cap {N_SCHMITT_B}; all "
             f"{len(run.schmitt_b_all)} digitized values listed below); bisection "
             f"midpoints (P5) depth <= {BISECT_DEPTH}, cap {BISECT_CAP_PER_ORBIT}/orbit.")
    L.append(f"- Candidates evaluated: {ev} (skipped on quarantine: {sk}); "
             f"exact cells: {sum(r['cells_exact'] for r in snap['groups_summary'])}.")
    menu_ids = [c for c in new_ids if run.menu_sighted(c)]
    schmitt_only_ids = [c for c in new_ids if not run.menu_sighted(c)]
    prior_resighted = [c for c in run.prior_ids if store.types[c]["sightings"]]
    L.append(f"- Store: {len(store.order)} types = {len(run.prior_ids)} prior-store + "
             f"**{len(new_ids)} hexagonal** (first sighted in this run), of which "
             f"**{len(menu_ids)} were sighted by OUR orbit menu** (P1/P3/P4/P5) and "
             f"{len(schmitt_only_ids)} were seen ONLY at Schmitt's printed generating "
             f"points (P2). Prior-store types re-sighted in hexagonal-family groups: "
             f"{len(prior_resighted)} ({sum(1 for c in prior_resighted if run.prior_system[c].startswith('cubic'))} "
             f"cubic-first, {sum(1 for c in prior_resighted if run.prior_system[c].startswith('tetragonal'))} "
             f"tetragonal-first).")
    L.append(f"- Max facet count stored: **{run.max_f_stored}** (from our own menu: "
             f"**{run.max_f_menu}**; the rest is Schmitt's printed rows)"
             + (f"; max in quarantine: {run.max_f_quarantined}." if run.max_f_quarantined
                else "; no >38 sighting at all."))
    L.append(f"- Quarantines: {len(run.quarantines)}; (group, b) pairs quarantined "
             f"for congruence: {len(run.gb_quarantined)}; bisection cap hits: "
             f"{run.bisect_caps}.")
    ss = run.schmitt_screen
    L.append(f"- Schmitt screen (P2): {ss['reproduced']} printed (row x group) evaluations "
             f"reproduced exactly (f-vector; conversion H1 {ss.get('conv_H1', 0)}, "
             f"H1+zflip {ss.get('conv_H1+zflip', 0)}), {ss['mismatch']} mismatches, "
             f"{ss.get('quarantined_other', 0)} other quarantines, of {len(run.schmitt_rows)} rows x groups "
             f"{sum(r['schmitt_rows'] for r in snap['groups_summary'])} evaluations.")
    L.append(f"- Invocations: {run.invocations} (resume log); this invocation wall {elapsed:.0f} s "
             f"on {WORKERS} workers; tasks from log {run.n_from_log}, this run {run.n_this_run}.")
    for p, s in run.pass_summary.items():
        L.append(f"  - pass {p}: {s['tasks']} tasks")
    L.append("")
    L.append("## Per-group table")
    L.append("")
    L.append("| group | symbol | ops | orbits (spec+gen) | line24 | Schmitt rows | "
             "evaluated P1/P2/P3/P4/P5 | skipped | exact cells | types | prior | "
             "hex(menu) | hex(S-only) | NEW (menu) | quar | max F menu / all |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in snap["groups_summary"]:
        e, s = r["evaluated"], r["skipped"]
        L.append(f"| {r['group']} | {r['symbol']} | {r['n_ops']} | {r['orbits_coarse']} "
                 f"({r['orbits_special']}+{r['orbits_general']}) | {r['orbits_line24']} | "
                 f"{r['schmitt_rows']} | {e['P1']}/{e['P2']}/{e['P3']}/{e['P4']}/{e['P5']} | "
                 f"{sum(s.values())} | {r['cells_exact']} | {r['types_distinct']} | "
                 f"{r['types_prior_store']} | {r['types_hexagonal_menu_sighted']} | "
                 f"{r['types_hexagonal_schmitt_only']} | "
                 f"{r['new_types_first_here']} ({r['new_types_first_here_menu']}) | "
                 f"{r['quarantines']} | {r['max_facets_menu']} / {r['max_facets']} |")
    L.append("")
    L.append("## b-ratio dependence (hexagonal types sighted by OUR menu)")
    L.append("")
    by_b = defaultdict(set)
    nb_hist = Counter()
    for cid in menu_ids:
        sg = [s for s in store.types[cid]["sightings"] if s["kind"] != "schmitt_printed"]
        bs = {s["b"] for s in sg}
        nb_hist[len(bs)] += 1
        for b in bs:
            by_b[b].add(cid)
    L.append("- Distinct b-ratio values per menu-sighted hexagonal type (histogram): "
             + ", ".join(f"{k}: {v}" for k, v in sorted(nb_hist.items())) + ".")
    L.append("")
    L.append("| b-ratio | menu-sighted hexagonal types seen | seen ONLY here |")
    L.append("|---|---|---|")
    for b in sorted(by_b, key=lambda s: F(s)):
        only = sum(1 for cid in by_b[b]
                   if {s["b"] for s in store.types[cid]["sightings"]
                       if s["kind"] != "schmitt_printed"} == {b})
        L.append(f"| {b} | {len(by_b[b])} | {only} |")
    L.append("")
    L.append("## Schmitt printed b-ratios (digitized, all)")
    L.append("")
    L.append(", ".join(f"{d['b']} ({d['rows']} rows)" for d in run.schmitt_b_all))
    L.append("")
    L.append("## Prior-store types re-sighted in hexagonal-family groups")
    L.append("")
    L.append("| id | system | name | F | f-vector | p-vector | aut | prior sightings | "
             "hex sightings | first hex witness |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for cid in store.order:
        e = store.types[cid]
        if cid not in run.prior_ids or not e["sightings"]:
            continue
        w = e["first_witness"]
        L.append(f"| `{cid}` | {e['first_sighting_system']} | {e.get('seed_name') or ''} | "
                 f"{e['f_vector'][2]} | {tuple(e['f_vector'])} | {pvec_compact(e['p_vector'])} | "
                 f"{e['aut_order']} | {e['prior_sightings']} | {len(e['sightings'])} | "
                 f"{w['group']} {w['group_symbol']} ({', '.join(w['point'])}) b={w['b']} |")
    L.append("")
    L.append(f"## Hexagonal types NOT matched against the records checked as of {SNAPSHOT} "
             f"({len(new_ids)})")
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
        L.append(f"- ... {len(run.quarantines) - 400} more in the store JSON")
    L.append("")
    L.append("## Honest limits (what this sweep did NOT do)")
    L.append("")
    L.append("- Orbits: special positions on the per-coordinate {1,2,3,4,6,8,12} grid plus "
             "1/24-grid samples of Wyckoff LINES (dim <= 1); plane strata at the coarse grid "
             "only; general position = 2 rational controls per group.")
    L.append(f"- Metric: {len(B_COARSE)} coarse rational b-ratios, {len(run.schmitt_b_used)} "
             f"Schmitt printed non-grid values (cap {N_SCHMITT_B} of {len(run.schmitt_b_all)} "
             f"digitized), bisection midpoints to depth {BISECT_DEPTH} ({run.bisect_caps} cap "
             f"hits). Irrational transition values (sqrt6, sqrt6/2, sqrt6/4 for the "
             f"rhombohedral lattice) are bracketed, not hit.")
    L.append("- Two exact cells per orbit (representative + one congruence check).")
    L.append("- Aut orders are combinatorial map automorphism counts (G4/V2 not claimed).")
    L.append("- Schmitt screen is f-vector-level and one-directional; the digitization is a "
             "text-layer parse with a visual cross-read of 153 rows, not an independent re-key.")
    L.append("- Enantiomorphic pairs (144/145, 151/153, 152/154, 169/170, 171/172, 178/179, "
             "180/181) share Schmitt's printed table; each row was run in both groups "
             "(second member: verbatim, then z -> -z; conversion recorded per sighting).")
    L.append("")
    L.append("## Run log (this invocation)")
    L.append("")
    L.append("```")
    L.extend(run.log)
    L.append("```")
    open(OUT_MD, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
