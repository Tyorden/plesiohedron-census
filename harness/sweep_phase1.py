#!/usr/bin/env python
"""sweep_phase1.py — PHASE 1 cubic sweep (the first hunt phase).

Scope per PROGRAM_PLAN_2026-08-27.md / HARNESS_DESIGN §2.1 Phase 1: the 36
cubic groups (IT 195-230, no free metric parameters), prioritizing the
chiral-corridor set the LANDSCAPE_SCOUT flagged. The scout names 6 of its
"8-group chiral corridor" explicitly (198, 199, 212, 213, 214, 220); the
standard quarter-cubic octet (Sabariego-Santos IV) is completed by Pa-3 (205)
and Ia-3 (206) — RECORDED READING, not the scout's verbatim list. Corridor
groups run first; the remaining cubic groups follow in numeric order under the
wall-clock budget (cuts, if any, are counted per group, never silent).

Point menu per group (frozen G1-audited spacegroups.json entries ONLY):
  (a) SPECIAL POSITIONS: scan the rational grid of points whose coordinates
      each have denominator in {1,2,3,4,6,8,12} (the 16-value/coordinate
      subgrid of the 1/24 grid; 4096 points), keep points with site-stabilizer
      order > 1 (exact test, integer arithmetic mod 24 — ops' translations are
      n/12 so they scale to integers), dedupe by full orbit, one canonical
      representative (min orbit point) per orbit. Fixed Wyckoff points
      (stratum dim 0) and rational SAMPLES of 1-parameter Wyckoff lines
      (dim 1) and 2-parameter planes (dim 2) all arise from this scan; the
      stratum dimension is recorded per orbit (dim of the stabilizer's common
      fixed linear space, exact rank computation).
  (b) GENERAL-POSITION CONTROLS: the first 2 points from a fixed rational
      candidate list whose stabilizer is trivial in the group.

Chain per orbit (the validated G0/G2/schmitt_220_check chain, one exact
representative cell per orbit — cells within an orbit are congruent, since the
group acts transitively on the orbit by isometries (cubic R are signed
permutation matrices) and Voronoi commutes with isometries; the float sweep
additionally checks (facet_count, p_vector) uniformity across ALL cells):
  orbit.py (exact, Fractions) -> sweep_voronoi.sweep float W=2 (W=3 retry on
  window-guard RuntimeError) -> exact_cell.clip_cell (all-Fraction, provable
  cutoff 4*rho2 <= D^2 asserted) -> canon_code.canonical_code.

G3 INVARIANT ENFORCED: nothing enters the dedupe store as a type without the
exact re-derivation agreeing with the float sighting (facet count, p-vector,
neighbor site set); canonical codes are computed from exact facet cycles ONLY.
Degenerate flags route per design §6.2 and the G0 amendment: flag, not fatal —
where the float cell is degeneracy-flagged, exact supersedes the float
proposal (recorded as float_superseded). Non-simple vertices are recorded,
never fatal.

Lattice-degenerate orbits (orbit closed under difference => a lattice => cell
is a parallelohedron by Fedorov): detected exactly, still run through the full
chain, recorded with lattice_degenerate=True; their type MUST match a seeded
parallelohedron code (quarantined as a bug if not).

KILL CRITERIA LIVE (ANCHORS): any cell with >38 facets (float or exact) =>
assume bug, quarantine the orbit's record, do not store as a type. Any crash
or unflagged float/exact disagreement => quarantine record, skip, never patch
mid-run. Extra consistency kill: the site-stabilizer order must divide the
combinatorial aut order (the stabilizer injects into the cell's map
automorphisms); violation quarantines.

DEDUPE STORE seeding (known types FIRST, recomputed where the source is this
pipeline — never hardcoded codes):
  - 5 parallelohedra: canonical codes from seed_catalog.json (built
    independently by g2_seed_catalog.py from published vertex data; G2-gated).
  - Josehedron: recomputed here from the G0 generating orbit (Bernhard Table 4
    minima, verbatim constants), asserted f=(12,22,12), p=3^4 4^8, aut 4.
  - Schmitt IT(220) general-position representative: recomputed here from his
    printed p.141 grid point (schmitt_220_check.py constants), asserted
    f=(12,22,12), p=3^6 4^4 5^2, aut 1, code != Josehedron code.

G5 LANGUAGE ONLY: types marked NEW below mean "not matched against catalog
snapshot of 2026-08-28 (5 parallelohedra + Josehedron + Schmitt-220
representative + all sightings of this run)". NO novelty claims, NO naming;
novelty diligence is a later gate.

Deterministic: fixed iteration order, sorted stores; phase1_types.json
contains no timestamps/timings (byte-identical across re-runs); PHASE1_RESULT
timing annotations are the only run-varying text.

Run:
  python3 sweep_phase1.py
Writes: phase1_types.json, PHASE1_RESULT.md. Exit 0 iff the sweep ran to
completion (quarantines are recorded findings, not failures).
"""
import hashlib
import itertools
import json
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F

import orbit
from sweep_voronoi import sweep
from exact_cell import clip_cell
from canon_code import canonical_code

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(HERE, "seed_catalog.json")

SCAN = 24                               # lcm of the allowed denominators
ALLOWED_DENS = (1, 2, 3, 4, 6, 8, 12)   # per-coordinate denominators scanned
CUBIC = list(range(195, 231))
CORRIDOR = [198, 199, 205, 206, 212, 213, 214, 220]   # reading recorded above
GROUP_ORDER = CORRIDOR + [n for n in CUBIC if n not in CORRIDOR]
MAX_FACETS = 38                         # ANCHORS kill criterion (observed max)
BUDGET_S = float(os.environ.get("PHASE1_BUDGET_S", 100 * 60))
N_GENERAL = 2

GENERAL_CANDIDATES = [
    (F(1, 8), F(1, 6), F(5, 12)),
    (F(1, 12), F(3, 8), F(1, 6)),
    (F(1, 8), F(1, 4), F(1, 6)),
    (F(1, 6), F(3, 8), F(1, 12)),
    (F(1, 12), F(1, 8), F(1, 3)),
    (F(5, 12), F(1, 8), F(1, 6)),
]

# Josehedron generating orbit, VERBATIM from g0_regression.py (Table 4 minima)
JOSE_BASE = [(0, 2, 3), (0, 6, 1), (1, 0, 6), (2, 3, 0), (2, 5, 4), (3, 0, 2),
             (4, 2, 5), (4, 6, 7), (5, 4, 2), (6, 1, 0), (6, 7, 4), (7, 4, 6)]
JOSE_PERIOD = 8
# Schmitt's IT(220) grid point, VERBATIM from schmitt_220_check.py (p. 141)
SCHMITT_X = (F(143, 1746), F(289, 3492), F(295, 3492))


def frac_str(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 \
        else str(x.numerator)


def point_str(p):
    return "(" + ", ".join(frac_str(x) for x in p) + ")"


def pvec_compact(pv):
    return " ".join(f"{k}^{m}" for k, m in sorted(Counter(pv).items()))


def code_id(code_str):
    return hashlib.sha1(code_str.encode("ascii")).hexdigest()[:16]


def special_scan(entry):
    """Special-position orbit representatives on the allowed-denominator grid.

    Integer arithmetic mod SCAN (exact: translations are n/12, SCAN=24).
    Returns sorted list of (rep_point_int_mod_24, stab_order, orbit_size)."""
    ops = []
    for R, t in entry["ops_exact"]:
        t24 = tuple(int(x * SCAN) for x in t)
        assert all((x * SCAN).denominator == 1 for x in t), "non-n/12 translation"
        ops.append((R, t24))
    allowed = [k for k in range(SCAN)
               if SCAN // math.gcd(k, SCAN) in ALLOWED_DENS]
    seen, reps = set(), []
    for p in itertools.product(allowed, repeat=3):
        if p in seen:
            continue
        orb, stab = set(), 0
        for R, t in ops:
            q = tuple((R[i][0]*p[0] + R[i][1]*p[1] + R[i][2]*p[2] + t[i]) % SCAN
                      for i in range(3))
            orb.add(q)
            if q == p:
                stab += 1
        seen |= orb
        if stab > 1:
            reps.append((min(orb), stab, len(orb)))
    return sorted(reps)


def rank3(rows):
    """Exact rank of a list of rational 3-vectors (Gaussian elimination)."""
    rows = [[F(x) for x in r] for r in rows]
    rank, col = 0, 0
    while col < 3 and rank < len(rows):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pr = rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                f = rows[i][col] / pr[col]
                rows[i] = [a - f * b for a, b in zip(rows[i], pr)]
        rank += 1
        col += 1
    return rank


def wyckoff_dim(entry, p):
    """Dim of the stabilizer's common fixed linear space = local stratum dim."""
    stab = orbit.site_stabilizer(entry, p)
    rows = []
    for R, _ in stab:
        for i in range(3):
            rows.append([R[i][j] - (1 if i == j else 0) for j in range(3)])
    return 3 - rank3(rows)


def is_lattice(pts, period):
    """Exact: is the periodic point set a lattice (closed under difference)?"""
    p0 = pts[0]
    S = {tuple((q[i] - p0[i]) % period for i in range(3)) for q in pts}
    for a in S:
        if tuple(-x % period for x in a) not in S:
            return False
        for b in S:
            if tuple((a[i] + b[i]) % period for i in range(3)) not in S:
                return False
    return True


class Store:
    def __init__(self):
        self.types = {}          # code_id -> entry
        self.order = []          # discovery order of code_ids

    def add_seed(self, code_str, fvec, pvec, aut, name, source):
        cid = code_id(code_str)
        assert cid not in self.types, f"seed collision: {name}"
        self.types[cid] = {
            "canon_code": code_str, "f_vector": list(fvec),
            "p_vector": list(pvec), "aut_order": aut,
            "seeded": True, "seed_name": name, "seed_source": source,
            "first_witness": None, "sightings": [],
        }
        self.order.append(cid)

    def sight(self, code_str, fvec, pvec, aut, sighting):
        """Returns (code_id, is_new). G3: caller guarantees exact-derived."""
        cid = code_id(code_str)
        if cid in self.types:
            e = self.types[cid]
            assert e["canon_code"] == code_str, "sha1 collision (!)"
            assert (tuple(e["f_vector"]) == tuple(fvec)
                    and tuple(e["p_vector"]) == tuple(pvec)
                    and e["aut_order"] == aut), \
                f"same code, different invariants: {cid}"
            e["sightings"].append(sighting)
            return cid, False
        self.types[cid] = {
            "canon_code": code_str, "f_vector": list(fvec),
            "p_vector": list(pvec), "aut_order": aut,
            "seeded": False, "first_witness": sighting,
            "sightings": [sighting],
        }
        self.order.append(cid)
        return cid, True


def run_chain(pts, period, label):
    """Float sweep (W=2, retry W=3) + exact clip of representative cell 0 +
    canonical code. Returns dict with everything the caller needs; raises
    ChainError with a reason on any kill criterion."""
    try:
        cells_f, W = sweep(pts, period, W=2), 2
    except RuntimeError:
        cells_f, W = sweep(pts, period, W=3), 3   # 2nd failure propagates
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
    ec = clip_cell(pts[0], pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2, f"{label}: cutoff violated"
    Fc = ec["facet_count"]
    V = ec["n_vertices"]
    E = sum(len(c) for c in ec["facet_cycles"]) // 2
    assert V - E + Fc == 2, f"{label}: Euler failure"
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
    return {
        "W": W, "float_max_F": float_max_F, "float_uniform": float_uniform,
        "degen_any": degen_any, "degen_flag0": f0["degenerate_flag"],
        "float_superseded": (not agree) and f0["degenerate_flag"],
        "fvec": (V, E, Fc), "pvec": ec["p_vector"], "Fc": Fc,
        "nonsimple": ec["nonsimple_vertices"], "cutoff_D": ec["cutoff_D"],
        "code_str": code.decode("ascii"), "aut": aut,
    }


class ChainError(Exception):
    def __init__(self, reason, detail):
        self.reason, self.detail = reason, detail
        super().__init__(f"{reason}: {detail}")


def seed_store(store, say):
    # 1) 5 parallelohedra from the G2 seed catalog (published vertex data)
    cat = json.load(open(CATALOG))["entries"]
    for e in sorted(cat, key=lambda e: e["name"]):
        store.add_seed(e["canon_code"], e["f_vector"], e["p_vector"],
                       e["aut_order"], e["name"],
                       "seed_catalog.json (g2_seed_catalog.py, published "
                       "vertex data, G2-gated)")
    say(f"seeded 5 parallelohedra from seed_catalog.json")

    # 2) Josehedron — recomputed through the pipeline (G0 orbit)
    fracs = [tuple(F(x, JOSE_PERIOD) for x in p) for p in JOSE_BASE]
    jpts, jP = orbit.scale_orbit(fracs)
    r = run_chain(jpts, jP, "josehedron-seed")
    assert r["fvec"] == (12, 22, 12) and r["pvec"] == (3,)*4 + (4,)*8 \
        and r["aut"] == 4, f"Josehedron seed regression: {r['fvec']}, " \
        f"{r['pvec']}, aut={r['aut']}"
    store.add_seed(r["code_str"], r["fvec"], r["pvec"], r["aut"], "josehedron",
                   "recomputed this run from the G0 generating orbit "
                   "(Bernhard Table 4 minima; IT(220) Wyckoff 12a)")
    say(f"seeded josehedron (recomputed): f={r['fvec']}, "
        f"p={pvec_compact(r['pvec'])}, aut={r['aut']}")

    # 3) Schmitt IT(220) general-position representative — recomputed
    groups = orbit.load_groups()
    ob = orbit.orbit(groups[220], SCHMITT_X)
    assert ob["general_position"] and ob["n_conventional"] == 48
    spts, sP = orbit.scale_orbit(ob["points"])
    r = run_chain(spts, sP, "schmitt220-seed")
    assert r["fvec"] == (12, 22, 12) \
        and r["pvec"] == (3,)*6 + (4,)*4 + (5,)*2 and r["aut"] == 1, \
        f"Schmitt-220 seed regression: {r['fvec']}, {r['pvec']}, aut={r['aut']}"
    jose_cid = next(c for c in store.order
                    if store.types[c].get("seed_name") == "josehedron")
    assert code_id(r["code_str"]) != jose_cid, \
        "Schmitt-220 code == Josehedron code (contradicts banked NO MATCH)"
    store.add_seed(r["code_str"], r["fvec"], r["pvec"], r["aut"],
                   "schmitt220_general_f12_22_12",
                   "recomputed this run from Schmitt 2016 p.141 point "
                   "(143/1746, 289/3492, 295/3492), IT(220) general position")
    say(f"seeded schmitt220 representative (recomputed): f={r['fvec']}, "
        f"p={pvec_compact(r['pvec'])}, aut={r['aut']}")


def main():
    t_start = time.time()
    lines = []

    def say(s):
        print(s, flush=True)
        lines.append(s)

    say(f"PHASE 1 cubic sweep — start (budget {BUDGET_S:.0f} s)")
    store = Store()
    seed_store(store, say)
    seeded_ids = set(store.order)

    groups = orbit.load_groups()
    orbit_records = []      # every orbit tried (compact, deterministic)
    quarantines = []
    group_rows = []
    max_f_stored = 0
    max_f_quarantined = 0
    budget_hit = False

    for num in GROUP_ORDER:
        entry = groups[num]
        gname = entry["international_short"]
        in_corridor = num in CORRIDOR
        t_g0 = time.time()

        # --- point menu
        specials = special_scan(entry)
        menu = [((F(p[0], SCAN), F(p[1], SCAN), F(p[2], SCAN)), "special")
                for p, _, _ in specials]
        n_general = 0
        for cand in GENERAL_CANDIDATES:
            if n_general >= N_GENERAL:
                break
            if len(orbit.site_stabilizer(entry, cand)) == 1:
                menu.append((cand, "general"))
                n_general += 1

        g_orbits = g_cells_float = g_exact = g_lat = g_quar = g_skipped = 0
        g_types = set()
        g_new = []
        g_max_f = 0

        for p, kind in menu:
            if time.time() - t_start > BUDGET_S:
                budget_hit = True
            if budget_hit:
                g_skipped += 1
                continue
            g_orbits += 1
            rec = {"group": num, "point": [frac_str(x) for x in p],
                   "kind": kind}
            try:
                ob = orbit.orbit(entry, p)
                dim = wyckoff_dim(entry, p) if kind == "special" else 3
                pts, period = orbit.scale_orbit(ob["points"])
                lat = is_lattice(pts, period)
                rec.update(stabilizer_order=ob["stabilizer_order"],
                           orbit_conventional=ob["n_conventional"],
                           orbit_primitive=ob["n_primitive"],
                           stratum_dim=dim, period=period,
                           lattice_degenerate=lat)
                g_cells_float += ob["n_conventional"]
                r = run_chain(pts, period, f"#{num} {point_str(p)}")
                g_exact += 1
                if lat:
                    g_lat += 1
                # consistency kill: stabilizer injects into map auts
                if r["aut"] % ob["stabilizer_order"] != 0:
                    raise ChainError(
                        "stab_not_dividing_aut",
                        f"stab {ob['stabilizer_order']} does not divide "
                        f"aut {r['aut']}")
                cid = code_id(r["code_str"])
                if lat:
                    lat_ok = (cid in seeded_ids
                              and store.types[cid].get("seed_name")
                              in ("cube", "hexagonal_prism",
                                  "rhombic_dodecahedron",
                                  "elongated_dodecahedron",
                                  "truncated_octahedron"))
                    if not lat_ok:
                        raise ChainError(
                            "lattice_orbit_nonparallelohedron",
                            "lattice-degenerate orbit produced a "
                            "non-parallelohedron type (Fedorov violation "
                            "= bug)")
                sighting = {
                    "group": num, "group_symbol": gname,
                    "point": [frac_str(x) for x in p], "kind": kind,
                    "stratum_dim": dim,
                    "stabilizer_order": ob["stabilizer_order"],
                    "orbit_conventional": ob["n_conventional"],
                    "orbit_primitive": ob["n_primitive"],
                    "lattice_degenerate": lat,
                    "degenerate_flag": r["degen_flag0"],
                    "float_superseded": r["float_superseded"],
                    "nonsimple_vertices": r["nonsimple"], "W": r["W"],
                }
                cid, is_new = store.sight(r["code_str"], r["fvec"], r["pvec"],
                                          r["aut"], sighting)
                g_types.add(cid)
                g_max_f = max(g_max_f, r["Fc"])
                max_f_stored = max(max_f_stored, r["Fc"])
                rec.update(verdict="stored", type_id=cid,
                           f_vector=list(r["fvec"]),
                           p_vector=pvec_compact(r["pvec"]), aut=r["aut"],
                           new_type=is_new)
                if is_new:
                    g_new.append(cid)
            except ChainError as exc:
                g_quar += 1
                rec.update(verdict="quarantined", reason=exc.reason,
                           detail=exc.detail)
                quarantines.append(dict(rec))
                if exc.reason.startswith("kill_gt38"):
                    mf = int(exc.detail.split()[3])
                    max_f_quarantined = max(max_f_quarantined, mf)
            except Exception as exc:            # crash: record and skip
                g_quar += 1
                rec.update(verdict="quarantined", reason="crash",
                           detail=f"{type(exc).__name__}: {exc}")
                quarantines.append(dict(rec))
            orbit_records.append(rec)

        n_new_here = len(g_new)
        group_rows.append({
            "group": num, "symbol": gname, "corridor": in_corridor,
            "n_ops": entry["n_ops"],
            "orbits_tried": g_orbits, "orbits_skipped_budget": g_skipped,
            "special_orbits": sum(1 for _, k in menu if k == "special"),
            "general_controls": n_general,
            "cells_float": g_cells_float, "cells_exact": g_exact,
            "lattice_degenerate": g_lat,
            "types_distinct": len(g_types), "new_types_first_here": n_new_here,
            "quarantines": g_quar, "max_facets": g_max_f,
        })
        say(f"#{num} {gname:8s}{' [corridor]' if in_corridor else '':11s} "
            f"orbits={g_orbits:4d} (skip {g_skipped}) exact={g_exact:4d} "
            f"lat={g_lat:2d} types={len(g_types):3d} new={n_new_here:3d} "
            f"quar={g_quar} maxF={g_max_f:2d}  [{time.time()-t_g0:.1f}s]")

    elapsed = time.time() - t_start
    new_ids = [cid for cid in store.order if cid not in seeded_ids]
    say("")
    say(f"DONE in {elapsed:.0f}s: {sum(r['orbits_tried'] for r in group_rows)} "
        f"orbits tried, {len(store.order)} types in store "
        f"({len(seeded_ids)} seeded + {len(new_ids)} not matched against "
        f"catalog snapshot of 2026-08-28), max stored facets {max_f_stored}, "
        f"{len(quarantines)} quarantines, budget_hit={budget_hit}")

    # ---- phase1_types.json (deterministic: no timings)
    out = {
        "generated_by": "sweep_phase1.py (Phase 1 cubic sweep, 2026-08-28)",
        "catalog_snapshot": "2026-08-28",
        "language_note": "types with seeded=false are NOT MATCHED AGAINST THE "
            "CATALOG SNAPSHOT OF 2026-08-28; no novelty claim is made (G5 "
            "diligence is a later gate)",
        "scan": {"grid_denominators": list(ALLOWED_DENS), "scan_period": SCAN,
                 "general_controls_per_group": N_GENERAL,
                 "group_order": GROUP_ORDER, "corridor": CORRIDOR,
                 "max_facets_kill": MAX_FACETS},
        "types": {cid: store.types[cid] for cid in store.order},
        "type_order": store.order,
        "orbits": orbit_records,
        "quarantines": quarantines,
        "groups_summary": group_rows,
        "max_facets_stored": max_f_stored,
        "max_facets_quarantined": max_f_quarantined,
        "budget_hit": budget_hit,
    }
    with open(os.path.join(HERE, "phase1_types.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=False)
    say(f"wrote phase1_types.json ({len(store.order)} types, "
        f"{len(orbit_records)} orbit records)")

    write_result(store, seeded_ids, new_ids, group_rows, quarantines,
                 max_f_stored, max_f_quarantined, budget_hit, elapsed, lines)
    say("wrote PHASE1_RESULT.md")
    return 0


def write_result(store, seeded_ids, new_ids, group_rows, quarantines,
                 max_f_stored, max_f_quarantined, budget_hit, elapsed, log):
    L = []
    L.append("# PHASE 1 result — cubic sweep (2026-08-28)")
    L.append("")
    L.append("Spec: `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §2.1 Phase 1 + "
             "`../PROGRAM_PLAN_2026-08-27.md` step 4. Gates: `../ANCHORS.md` "
             "G3 (exact-confirmation invariant, ENFORCED per stored sighting) "
             "and the KILL CRITERIA (>38 facets = quarantine). Pipeline: the "
             "G0/G2-validated chain `orbit.py` -> `sweep_voronoi.py` (float, "
             "W=2, W=3 retry) -> `exact_cell.py` (all-Fraction, provable "
             "cutoff asserted) -> `canon_code.py`. Frozen G1 "
             "`spacegroups.json` only.")
    L.append("")
    L.append("**LANGUAGE (G5): every type below marked NEW means \"not "
             "matched against catalog snapshot of 2026-08-28\" (5 "
             "parallelohedra + Josehedron + Schmitt-220 representative). NO "
             "novelty claim, NO naming — novelty diligence is a later gate. "
             "Schmitt ch.2 is a sampling survey: absence there is evidence, "
             "not proof.**")
    L.append("")
    L.append("## Method")
    L.append("")
    L.append("- Point menu per group: ALL special-position orbits on the "
             "per-coordinate denominator {2,3,4,6,8,12} grid (4096 scanned "
             "points, exact stabilizer test, orbit-deduped to one "
             "representative), + 2 general-position rational controls. "
             "1-parameter Wyckoff lines and 2-parameter planes enter as their "
             "rational grid samples; the stratum dimension (0=fixed point, "
             "1=line sample, 2=plane sample, 3=general) is recorded per "
             "orbit.")
    L.append("- One exact representative cell per orbit (orbit cells are "
             "congruent: the group acts transitively by isometries — cubic "
             "R are signed permutations — and Voronoi commutes with "
             "isometries); float sweep covers ALL orbit cells and their "
             "(F, p-vector) uniformity is checked.")
    L.append("- G3 per stored sighting: exact facet count, p-vector and "
             "neighbor site set must agree with the float proposal (or the "
             "float cell carries the degeneracy flag, in which case exact "
             "supersedes — flagged, not fatal, per the G0 amendment); "
             "canonical codes from exact facet cycles only.")
    L.append("- Lattice-degenerate orbits (exact closure test) still run the "
             "chain and MUST match a seeded parallelohedron (Fedorov); "
             "recorded, counted separately.")
    L.append("- Consistency kill added: site-stabilizer order must divide "
             "the combinatorial aut order (the stabilizer injects into the "
             "cell's map automorphism group).")
    L.append("- Corridor reading (recorded): the scout names 198, 199, 212, "
             "213, 214, 220 of its \"8-group chiral corridor\"; the standard "
             "quarter-cubic octet is completed by 205, 206 (Pa-3, Ia-3) — "
             "those two are my addition, flagged as such. Corridor ran "
             "first; all 36 cubic groups were processed.")
    L.append("")
    L.append("## Per-group table")
    L.append("")
    L.append("| group | symbol | corr | ops | orbits (spec+gen) | skipped | "
             "exact cells | lattice-degen | types | NEW first here | quar | "
             "max F |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(group_rows, key=lambda r: r["group"]):
        L.append(f"| {r['group']} | {r['symbol']} | "
                 f"{'Y' if r['corridor'] else ''} | {r['n_ops']} | "
                 f"{r['orbits_tried']} ({r['special_orbits']}+"
                 f"{r['general_controls']}) | {r['orbits_skipped_budget']} | "
                 f"{r['cells_exact']} | {r['lattice_degenerate']} | "
                 f"{r['types_distinct']} | {r['new_types_first_here']} | "
                 f"{r['quarantines']} | {r['max_facets']} |")
    tot_orb = sum(r["orbits_tried"] for r in group_rows)
    tot_skip = sum(r["orbits_skipped_budget"] for r in group_rows)
    tot_ex = sum(r["cells_exact"] for r in group_rows)
    tot_fl = sum(r["cells_float"] for r in group_rows)
    L.append("")
    L.append(f"Totals: {tot_orb} orbits tried ({tot_skip} skipped on "
             f"budget), {tot_fl} float cells summarized, {tot_ex} exact "
             f"representative cells, {len(new_ids)} distinct types not "
             f"matched against the catalog snapshot, "
             f"{len(quarantines)} quarantines. Max facet count stored: "
             f"**{max_f_stored}**"
             + (f"; max facet count in quarantine: {max_f_quarantined}."
                if max_f_quarantined else " (no >38 sightings at all)."))
    L.append("")
    L.append("## Seeded types and their re-sightings this run")
    L.append("")
    for cid in store.order:
        e = store.types[cid]
        if not e["seeded"]:
            continue
        L.append(f"- `{cid}` **{e['seed_name']}** f={tuple(e['f_vector'])} "
                 f"p={pvec_compact(e['p_vector'])} aut={e['aut_order']} — "
                 f"{len(e['sightings'])} sightings in the sweep")
    L.append("")
    L.append(f"## Types NOT matched against catalog snapshot of 2026-08-28 "
             f"({len(new_ids)})")
    L.append("")
    L.append("Sorted by (facets, p-vector). Witness = first sighting in run "
             "order (corridor first). dim: 0 fixed Wyckoff point / 1 line "
             "sample / 2 plane sample / 3 general position.")
    L.append("")
    L.append("| id | F | f-vector | p-vector | aut | witness group | witness "
             "point | stab | dim | orbit(conv) | sightings |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for cid in sorted(new_ids, key=lambda c: (store.types[c]["f_vector"][2],
                                              store.types[c]["p_vector"],
                                              c)):
        e = store.types[cid]
        w = e["first_witness"]
        L.append(f"| `{cid}` | {e['f_vector'][2]} | {tuple(e['f_vector'])} | "
                 f"{pvec_compact(e['p_vector'])} | {e['aut_order']} | "
                 f"{w['group']} {w['group_symbol']} | "
                 f"({', '.join(w['point'])}) | {w['stabilizer_order']} | "
                 f"{w['stratum_dim']} | {w['orbit_conventional']} | "
                 f"{len(e['sightings'])} |")
    L.append("")
    L.append(f"## Quarantines ({len(quarantines)})")
    L.append("")
    if not quarantines:
        L.append("None. No >38-facet sighting, no float/exact disagreement, "
                 "no crash, no Fedorov violation, no stab/aut inconsistency.")
    for q in quarantines:
        L.append(f"- group {q['group']} point ({', '.join(q['point'])}) "
                 f"[{q['kind']}]: **{q['reason']}** — {q['detail']}")
    L.append("")
    L.append("## Honest limits (what this sweep did NOT do)")
    L.append("")
    L.append("- Denominators: special positions scanned only with "
             "per-coordinate denominators in {2,3,4,6,8,12}. Fixed Wyckoff "
             "points of cubic groups all have such coordinates in the IT "
             "setting (spot-belief, not verified against ITA tables); "
             "Wyckoff LINES/PLANES are only SAMPLED at these rational grid "
             "points — strata thinner than the grid, and line regions "
             "between samples, are not covered. No transition bisection "
             "(design §2.3) was run in this phase.")
    L.append("- General positions: 2 rational controls per group, not the "
             "design's N=8 grid (that general-position sweep remains open; "
             "Schmitt's survey already covers general position densely — "
             "the corridor rationale here was special positions).")
    L.append("- One exact cell per orbit (congruence argument above); the "
             "other cells were float-checked only.")
    L.append("- Aut orders are combinatorial map automorphism counts; "
             "geometric stabilizer certification is G4/V2, not claimed.")
    L.append("- Type identity relies on canon_code (unit-tested in "
             "test_canon.py, G2-exercised); f/p-vector collisions between "
             "distinct codes are expected and are NOT merged.")
    if budget_hit:
        L.append(f"- BUDGET HIT: {tot_skip} orbits skipped (counted per "
                 f"group in the table); groups listed with skipped>0 are "
                 f"incomplete.")
    else:
        L.append("- Budget NOT hit: all 36 cubic groups completed; nothing "
                 "was cut.")
    L.append("")
    L.append(f"Run wall time: {elapsed:.0f} s (single process, "
             "deterministic order; phase1_types.json contains no timings and "
             "is byte-identical across re-runs).")
    L.append("")
    L.append("## Run log")
    L.append("")
    L.append("```")
    L.extend(log)
    L.append("```")
    open(os.path.join(HERE, "PHASE1_RESULT.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
