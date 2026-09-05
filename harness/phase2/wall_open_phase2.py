#!/usr/bin/env python
"""wall_open_phase2.py — COMPUTED open/wall classification of the 165 G4-certified
phase-2 cells (14 tetragonal + 151 hexagonal-family) by exact perturbation, per
the scheme pre-registered in ../../ANCHORS.md ("PERTURBATION CLASSIFICATION,
PHASE 2 — pre-registered 2026-09-04"), which this file implements verbatim.

WHAT IT REPLACES: the heuristic labels (open-likely / indeterminate / wall-suspect,
from counts of stored b-ratios) carried through TRIAGE_PHASE2_RESULT.md,
TRIAGE_PHASE2_HEX_RESULT.md, G4_PHASE2_RESULTS.md and G4_PHASE2_HEX_RESULTS.md.

CHAIN (accepted modules, imported unchanged; nothing here edits them):
  sweep_phase2_tetragonal.evaluate  (tetragonal family, metric.gram_tetragonal)
  sweep_phase2_hexagonal.evaluate   (hexagonal family,  metric.gram_hexagonal)
  = orbit (frozen G1 ops) -> Gram with R^T G R = G asserted -> sweep_gram float
  PROPOSAL (W = 2..4) -> exact_cell_gram clip (warm start; 4 rho^2 <= D^2 and Euler
  asserted) -> canonical code; orbit-congruence check; G3 invariant (float/exact
  agreement or degeneracy flag => exact supersedes, float_superseded recorded);
  kill criteria live (> 38 facets). ChainError => QUARANTINE row (recorded,
  never SAME, never DIFFERENT).

DIRECTIONS (exact rationals):
  (i)  POINT within the witness stratum: tangent basis = nullspace_basis of
       round1_computations/c1_wall_open.py (copied verbatim below), steps
       delta in {-1/48, -1/96, +1/96, +1/48} along each basis vector; refinement
       halving to 1/1536 on any side whose smallest step is not SAME (c1).
       dim 0 => point direction NOT APPLICABLE.
  (ii) METRIC: c/a -> c/a * (1 + eps), eps in {-1/96, -1/192, +1/192, +1/96};
       refinement halving to 1/3072.
VERDICTS: side status SAME / DIFFERENT / QUARANTINE at the finest step; a
direction is WALL when both sides are DIFFERENT. POINT / METRIC / COMBINED
verdicts by c1 lines 103-109 (OPEN / WALL / ONE-SIDED), plus INDETERMINATE when
a side ends in QUARANTINE; COMBINED = over all applicable directions together.
FLAGS: LINE-ISOLATED (dim 1 and the point direction is WALL), NON-SIMPLE-VERTEX
(nonsimple_vertices > 0 at the witness), STAB-CHANGE (a perturbed point whose
site-stabilizer order differs from the witness's).

DETERMINISM: WALL_OPEN_PHASE2.json has sorted keys and NO timings; a second full
run must reproduce it byte for byte. Per-cell records in wall_open_cells/<id>.json
(atomic writes) allow resume at a clean boundary; exit 3 = budget stop, re-run
the same command to resume. Timings go to the .md only.

RUN (from harness/phase2/; ~8 forked workers, foreground, rule 29):
  nice -n 10 python3 \
      wall_open_phase2.py --jobs 8 --budget-s 540          # exit 0 done / 3 resume
  ... --fresh   wipes wall_open_cells/ first (full recompute for the md5 check)
Writes: WALL_OPEN_PHASE2.json, WALL_OPEN_PHASE2.md, wall_open_cells/*.json.
Read-only inputs: phase2_types.json, phase2_hexagonal_types.json (sha256 asserted
before and after), the two G4 result docs, the two Schmitt table digitizations.
LANGUAGE: no naming; every type stays "not matched against the records checked
as of 2026-09-04"; OPEN = holds on the tested neighbourhood, not an interval proof.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import argparse                                      # noqa: E402
import hashlib                                       # noqa: E402
import json                                          # noqa: E402
import multiprocessing as mp                         # noqa: E402
import re                                            # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
from collections import Counter, OrderedDict         # noqa: E402
from fractions import Fraction as F                  # noqa: E402
from math import gcd, lcm                            # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.dirname(HERE)
sys.path.insert(0, HARNESS)
sys.path.insert(0, HERE)

import orbit                                         # noqa: E402
from sweep_phase1 import ChainError, pvec_compact, frac_str, code_id  # noqa: E402
import sweep_phase2_tetragonal as S2                 # noqa: E402
import sweep_phase2_hexagonal as SH                  # noqa: E402

GROUPS = S2.GROUPS
STORE_TET = os.path.join(HARNESS, "phase2_types.json")
STORE_HEX = os.path.join(HARNESS, "phase2_hexagonal_types.json")
SHA_TET = "71685b9ab41b4dc0c2ee1763fdd64f06b41fc51f5a0702d362f137822969f7a3"
SHA_HEX = "7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55"
DOC_TET = os.path.join(HARNESS, "G4_PHASE2_RESULTS.md")
DOC_HEX = os.path.join(HARNESS, "G4_PHASE2_HEX_RESULTS.md")
TABLES_TET = os.path.join(HARNESS, "schmitt_tetragonal_tables.json")
TABLES_HEX = os.path.join(HARNESS, "schmitt_hexagonal_tables.json")
COLLISION_TET = os.path.join(HARNESS, "collision_phase2_results.json")
OUT_JSON = os.path.join(HERE, "WALL_OPEN_PHASE2.json")
OUT_MD = os.path.join(HERE, "WALL_OPEN_PHASE2.md")
CELLS_DIR = os.path.join(HERE, "wall_open_cells")
SNAPSHOT = "2026-09-04"

POINT_EPS = [F(-1, 48), F(-1, 96), F(1, 96), F(1, 48)]
POINT_REFINE_START, POINT_REFINE_LIMIT = 96, 1536
METRIC_EPS = [F(-1, 96), F(-1, 192), F(1, 192), F(1, 96)]
METRIC_REFINE_START, METRIC_REFINE_LIMIT = 192, 3072
OFF_STRATUM_EPS = (F(-1, 96), F(1, 96))
KIND = "wall_open_phase2"
SCHEME = OrderedDict([
    ("pre_registration", "ANCHORS.md: PERTURBATION CLASSIFICATION, PHASE 2 — pre-registered 2026-09-04"),
    ("point_steps", [frac_str(e) for e in POINT_EPS]),
    ("point_refine_to", f"1/{POINT_REFINE_LIMIT}"),
    ("point_units", "fractional coordinates of the ITA conventional cell (hexagonal basis for IT 143-194)"),
    ("metric_steps_relative", [frac_str(e) for e in METRIC_EPS]),
    ("metric_rule", "c/a -> c/a * (1 + eps)"),
    ("metric_refine_to", f"1/{METRIC_REFINE_LIMIT}"),
    ("off_stratum_supplementary", [frac_str(e) for e in OFF_STRATUM_EPS]),
    ("chain", "sweep_phase2_tetragonal.evaluate / sweep_phase2_hexagonal.evaluate (accepted, unmodified)"),
    ("verdict_rule", "c1_wall_open.py lines 103-109 per direction class; COMBINED over point basis + metric; "
                     "INDETERMINATE if any side ends in QUARANTINE"),
])

# regression targets (COLLISION_PHASE2_RESULTS.md, top-3 point verdicts; same steps, same chain)
REGRESSION_POINT = {"4e9c9b076cfec323": ("OPEN", []),
                    "49cedbdd58376fac": ("WALL", [(1, 1, 0)]),
                    "f654982d74d740f6": ("OPEN", [])}


# ------------------------------------------------------------ helpers ---
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pt_str(p):
    return "(" + ", ".join(frac_str(x) for x in p) + ")"


def nullspace_basis(mats):
    """Exact basis of {v : (R - I) v = 0 for all R in mats}.
    COPIED VERBATIM from round1_computations/c1_wall_open.py (the accepted cubic
    computation) so the tangent basis is the same function of the stabilizer."""
    rows = []
    for R in mats:
        for i in range(3):
            rows.append([F(R[i][j] - (1 if i == j else 0)) for j in range(3)])
    piv_cols, r = [], 0
    A = [row[:] for row in rows]
    for c in range(3):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv_cols.append(c); r += 1
    free = [c for c in range(3) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F(0)] * 3; v[fc] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -A[i][fc]
        den = 1
        for x in v: den = lcm(den, x.denominator)
        vi = [int(x * den) for x in v]
        g = 0
        for x in vi: g = gcd(g, abs(x))
        basis.append(tuple(x // g for x in vi))
    return basis


def rank_of(vecs):
    A = [[F(x) for x in v] for v in vecs]
    r = 0
    for c in range(3):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def parse_cells():
    """The 165 certified cells + carried labels, in the two docs' table order."""
    cells = []
    for line in open(DOC_TET):
        c = [x.strip() for x in line.split("|")]
        if len(c) >= 14 and re.fullmatch(r"\d+", c[1]) and re.fullmatch(r"`[0-9a-f]{16}`", c[2]) and c[6] == "PASS":
            cells.append(dict(family="tetragonal", rank=int(c[1]), id=c[2].strip("`"),
                              doc_group=int(c[3].split()[0]), doc_ca=c[4], previous_label=c[12]))
    n_tet = len(cells)
    for line in open(DOC_HEX):
        c = [x.strip() for x in line.split("|")]
        if len(c) >= 17 and re.fullmatch(r"\d+", c[1]) and re.fullmatch(r"`[0-9a-f]{16}`", c[2]) and c[7] == "PASS":
            cells.append(dict(family="hexagonal", rank=int(c[1]), id=c[2].strip("`"),
                              doc_group=int(c[3].split()[0]), doc_ca=c[4], previous_label=c[15]))
    assert n_tet == 14 and len(cells) == 165, (n_tet, len(cells))
    assert len({c["id"] for c in cells}) == 165
    return cells


def label_class(label):
    head = label.split(" (")[0].strip()
    if head.startswith("open-likely"):
        return "open-likely"
    if head.startswith("wall-suspect"):
        return "wall-suspect"
    if head.startswith("indeterminate"):
        return "indeterminate"
    if head.startswith("OPEN"):
        return "carried OPEN"
    if head.startswith("WALL"):
        return "carried WALL"
    raise ValueError(label)


def agree(lclass, verdict):
    if lclass == "indeterminate":
        return "n/a"
    ok = {("open-likely", "OPEN"), ("wall-suspect", "WALL"),
          ("carried OPEN", "OPEN"), ("carried WALL", "WALL")}
    return "yes" if (lclass, verdict) in ok else "NO"


def printed_fvectors(path):
    d = json.load(open(path))
    out = {}
    for key, blk in d.items():
        if key == "_meta":
            continue
        fs = {tuple(r["f"]) for r in blk["rows"]}
        for g in blk["groups"]:
            out[int(g)] = fs
    return out


# ------------------------------------------------------- per-cell work ---
CTX = {}   # filled in the parent before the fork: witnesses, code map, printed f


def evaluate(num, p, b):
    fam = GROUPS[num]["crystal_family"]
    p = tuple(F(x) for x in p)
    if fam == "tetragonal":
        return S2.evaluate(num, p, F(b), KIND)
    assert fam == "hexagonal", fam
    return SH.evaluate(num, p, F(b), KIND)


def probe(num, p, b, ent, w, printed_f):
    """One perturbed evaluation -> row dict (never raises on ChainError)."""
    try:
        r = evaluate(num, p, b)
    except ChainError as exc:
        return dict(point=pt_str(p), b=frac_str(b), status="QUARANTINE",
                    quarantine=f"{exc.reason}: {exc.detail}"[:160],
                    stab=None, f=None, p=None, aut=None, nonsimple=None,
                    stored_id=None, code_id=None, schmitt_type_groups=None,
                    fvec_printed=None, float_superseded=None, degenerate_flag=None,
                    W=None, stab_change=None)
    code = r["code_str"]
    same = code == ent["canon_code"]
    sid = CTX["code2id"].get(code)
    return dict(point=pt_str(p), b=frac_str(b), status="SAME" if same else "DIFFERENT",
                quarantine=None, stab=r["stabilizer_order"], f=list(r["fvec"]),
                p=pvec_compact(r["pvec"]), aut=r["aut"], nonsimple=r["nonsimple"],
                stored_id=sid, code_id=code_id(code),
                schmitt_type_groups=(CTX["schmitt_groups"].get(sid) if sid else None),
                fvec_printed=tuple(r["fvec"]) in printed_f,
                float_superseded=r["float_superseded"], degenerate_flag=r["degen_flag0"],
                W=r["W"], stab_change=r["stabilizer_order"] != w["stabilizer_order"])


def classify(cell):
    ent = CTX["witness"][cell["id"]]
    w = ent["first_witness"]
    num, b0 = w["group"], F(w["b"])
    p0 = tuple(F(s) for s in w["point"])
    assert num == cell["doc_group"] and b0 == F(cell["doc_ca"]), (cell, w)
    printed_f = CTX["printed_f"].get(num, set())
    # V0 pattern: witness -> exact -> must agree with the store
    base = evaluate(num, p0, b0)
    assert base["code_str"] == ent["canon_code"], "canonical code MISMATCH vs store"
    assert list(base["fvec"]) == list(ent["f_vector"]) and list(base["pvec"]) == list(ent["p_vector"])
    assert base["aut"] == ent["aut_order"] and base["stabilizer_order"] == w["stabilizer_order"]
    assert base["nonsimple"] == w["nonsimple_vertices"]
    stab_ops = orbit.site_stabilizer(GROUPS[num], p0)
    basis = nullspace_basis([R for R, _ in stab_ops])
    assert len(basis) == w["stratum_dim"], (len(basis), w["stratum_dim"])
    rows = []

    def add(kind, d, eps, refine=False):
        if kind == "point":
            q = tuple(p0[k] + eps * d[k] for k in range(3))
            row = probe(num, q, b0, ent, w, printed_f)
        else:
            row = probe(num, p0, b0 * (1 + eps), ent, w, printed_f)
        row.update(kind=kind, direction=list(d) if d else None, eps=frac_str(eps),
                   refine=refine, off_stratum=False)
        rows.append(row)
        return row["status"]

    dirs = [("point", d) for d in basis] + [("metric", None)]
    for kind, d in dirs:
        for eps in (POINT_EPS if kind == "point" else METRIC_EPS):
            add(kind, d, eps)
    side = {}
    for kind, d in dirs:
        start, limit = ((POINT_REFINE_START, POINT_REFINE_LIMIT) if kind == "point"
                        else (METRIC_REFINE_START, METRIC_REFINE_LIMIT))
        for sign in (-1, 1):
            cand = [x for x in rows if x["kind"] == kind and x["direction"] == (list(d) if d else None)
                    and not x["off_stratum"] and sign * F(x["eps"]) > 0]
            smallest = min(cand, key=lambda x: abs(F(x["eps"])))
            status, den = smallest["status"], start
            while status != "SAME" and den < limit:
                den *= 2
                status = add(kind, d, F(sign, den), True)
            side[(kind, tuple(d) if d else None, sign)] = status

    def verdict_for(kinds):
        ds = [(k, d) for k, d in dirs if k in kinds]
        if not ds:
            return "n/a", []
        st = {(k, tuple(d) if d else None): (side[(k, tuple(d) if d else None, -1)],
                                             side[(k, tuple(d) if d else None, 1)]) for k, d in ds}
        walls = [k if k == "metric" else list(d) for (k, d), (a, b) in st.items()
                 if a == "DIFFERENT" and b == "DIFFERENT"]
        if any("QUARANTINE" in ab for ab in st.values()):
            return "INDETERMINATE", walls
        if all(ab == ("SAME", "SAME") for ab in st.values()):
            return "OPEN", walls
        return ("WALL" if walls else "ONE-SIDED"), walls

    pv, pw = verdict_for({"point"})
    mv, mw = verdict_for({"metric"})
    cv, cw = verdict_for({"point", "metric"})
    # supplementary off-stratum step (special positions only; not a verdict input)
    if len(basis) < 3:
        for dgen in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3)]:
            if rank_of(list(basis) + [dgen]) == len(basis) + 1:
                break
        for eps in OFF_STRATUM_EPS:
            q = tuple(p0[k] + eps * dgen[k] for k in range(3))
            row = probe(num, q, b0, ent, w, printed_f)
            row.update(kind="point", direction=list(dgen), eps=frac_str(eps), refine=False, off_stratum=True)
            rows.append(row)
    # neighbours: distinct DIFFERENT types over on-stratum rows, with where seen
    nb = OrderedDict()
    for x in rows:
        if x["off_stratum"] or x["status"] != "DIFFERENT":
            continue
        key = x["code_id"]
        e = nb.setdefault(key, dict(code_id=key, stored_id=x["stored_id"], f=x["f"], p=x["p"], aut=x["aut"],
                                    nonsimple=x["nonsimple"], schmitt_type_groups=x["schmitt_type_groups"],
                                    fvec_printed_in_witness_group=x["fvec_printed"], seen=[]))
        e["seen"].append(f"{x['kind']}{'' if x['direction'] is None else tuple(x['direction'])} eps={x['eps']}")
    on = [x for x in rows if not x["off_stratum"]]
    lclass = label_class(cell["previous_label"])
    flags = OrderedDict([
        ("line_isolated", w["stratum_dim"] == 1 and pv == "WALL"),
        ("nonsimple_vertex", base["nonsimple"] > 0),
        ("stab_change_any", any(x["stab_change"] for x in on if x["stab_change"] is not None)),
        ("float_superseded_any", any(x["float_superseded"] for x in on if x["float_superseded"] is not None)),
        ("degenerate_flag_any", any(x["degenerate_flag"] for x in on if x["degenerate_flag"] is not None)),
        ("quarantine_any", any(x["status"] == "QUARANTINE" for x in on)),
    ])
    sides_out = {f"{k}{'' if d is None else d}:{'+' if s > 0 else '-'}": v for (k, d, s), v in side.items()}
    return OrderedDict([
        ("id", cell["id"]), ("family", cell["family"]), ("rank", cell["rank"]),
        ("IT", num), ("symbol", GROUPS[num]["international_short"]),
        ("witness_point", pt_str(p0)), ("c_over_a", frac_str(b0)),
        ("stratum_dim", w["stratum_dim"]), ("site_stab", w["stabilizer_order"]),
        ("tangent_basis", [list(d) for d in basis]),
        ("point_direction_applicable", len(basis) > 0),
        ("base_f", list(base["fvec"])), ("base_p", pvec_compact(base["pvec"])),
        ("base_aut", base["aut"]), ("base_nonsimple", base["nonsimple"]),
        ("previous_label", cell["previous_label"]), ("previous_label_class", lclass),
        ("point_verdict", pv), ("point_walls", pw),
        ("metric_verdict", mv), ("metric_wall", bool(mw)),
        ("combined_verdict", cv), ("combined_walls", cw),
        ("agree", agree(lclass, cv)),
        ("flags", flags), ("sides", sides_out),
        ("neighbours", list(nb.values())),
        ("n_evaluations", len(rows) + 1),
        ("rows", rows),
    ])


def worker(cell):
    t0 = time.time()
    try:
        res = classify(cell)
        res["_secs"] = round(time.time() - t0, 1)
        status = "ok"
    except Exception as exc:           # a crash is recorded, never silent
        res = OrderedDict([("id", cell["id"]), ("family", cell["family"]), ("rank", cell["rank"]),
                           ("crash", f"{type(exc).__name__}: {exc}"[:300]),
                           ("_secs", round(time.time() - t0, 1))])
        status = "crash"
    path = os.path.join(CELLS_DIR, cell["id"] + ".json")
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
    os.replace(tmp, path)
    return cell["id"], status, res["_secs"], res.get("combined_verdict", "CRASH")


# ---------------------------------------------------------------- docs ---
def fmt_nb(nb):
    sid = nb["stored_id"] or "not stored"
    st = ("Schmitt-printed TYPE in IT(" + ", ".join(map(str, nb["schmitt_type_groups"])) + ")"
          if nb["schmitt_type_groups"] else "not a Schmitt-printed type")
    return (f"f={tuple(nb['f'])} {nb['p']} aut {nb['aut']} ns {nb['nonsimple']} [{sid}; {st}; "
            f"f printed in witness group table: {nb['fvec_printed_in_witness_group']}] via "
            + ", ".join(nb["seen"]))


def write_docs(results, cells, total_s, sums, sha_after, jobs):
    order = [c["id"] for c in cells]
    res = [results[i] for i in order]
    crashes = [r for r in res if "crash" in r]
    good = [r for r in res if "crash" not in r]
    md5 = None
    agg = OrderedDict()
    for fam in ("tetragonal", "hexagonal"):
        rs = [r for r in good if r["family"] == fam]
        agg[fam] = OrderedDict([
            ("n", len(rs)),
            ("combined", dict(sorted(Counter(r["combined_verdict"] for r in rs).items()))),
            ("point", dict(sorted(Counter(r["point_verdict"] for r in rs).items()))),
            ("metric", dict(sorted(Counter(r["metric_verdict"] for r in rs).items()))),
            ("agree", dict(sorted(Counter(r["agree"] for r in rs).items()))),
            ("line_isolated", sum(1 for r in rs if r["flags"]["line_isolated"])),
            ("nonsimple_vertex", sum(1 for r in rs if r["flags"]["nonsimple_vertex"])),
            ("stab_change_any", sum(1 for r in rs if r["flags"]["stab_change_any"])),
            ("float_superseded_any", sum(1 for r in rs if r["flags"]["float_superseded_any"])),
            ("quarantine_any", sum(1 for r in rs if r["flags"]["quarantine_any"])),
        ])
    # regression (asserted): top-3 tetragonal point verdicts vs COLLISION_PHASE2_RESULTS.md
    reg = OrderedDict()
    coll = json.load(open(COLLISION_TET))["perturbation"] if os.path.exists(COLLISION_TET) else []
    coll_by = {c["id"]: c for c in coll}
    for cid, (pv_exp, walls_exp) in REGRESSION_POINT.items():
        r = results.get(cid)
        got = (r["point_verdict"], [tuple(x) for x in r["point_walls"]]) if r and "crash" not in r else None
        ok = got == (pv_exp, walls_exp)
        c = coll_by.get(cid, {})
        reg[cid] = OrderedDict([("expected_point", pv_exp), ("expected_walls", [list(x) for x in walls_exp]),
                                ("got_point", got[0] if got else None), ("got_walls", [list(x) for x in got[1]] if got else None),
                                ("point_agrees", ok),
                                ("collision_json_point_verdict", c.get("point_verdict")),
                                ("collision_json_b_verdict", c.get("b_verdict")),
                                ("metric_verdict_here", r["metric_verdict"] if got else None)])
    reg_ok = all(v["point_agrees"] for v in reg.values())
    out = OrderedDict([
        ("generated_by", "harness/phase2/wall_open_phase2.py"),
        ("snapshot", SNAPSHOT),
        ("scheme", SCHEME),
        ("stores", OrderedDict([("phase2_types.json_sha256", SHA_TET), ("phase2_hexagonal_types.json_sha256", SHA_HEX),
                                ("sha256_unchanged_after_run", sha_after)])),
        ("n_cells", len(res)), ("n_crash", len(crashes)),
        ("aggregate", agg),
        ("regression_top3_point_verdicts", reg), ("regression_ok", reg_ok),
        ("cells", [OrderedDict((k, v) for k, v in r.items() if k != "_secs") for r in res]),
    ])
    tmp = OUT_JSON + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, OUT_JSON)
    md5 = hashlib.md5(open(OUT_JSON, "rb").read()).hexdigest()

    L = [f"# Computed open/wall classification of the 165 G4-certified phase-2 cells (14 tetragonal + 151 hexagonal-family) — {SNAPSHOT}", "",
         "AI disclosure: computed and written by an AI subagent (Claude Fable 5.1, #148) under the scheme pre-registered in ANCHORS.md by the same agent before the run; "
         "PROVISIONAL until the main session re-runs `wall_open_phase2.py --fresh` and reproduces the JSON md5 below. Nothing here is a novelty or naming claim.", "",
         "Pre-registered scheme: `../../ANCHORS.md`, block \"PERTURBATION CLASSIFICATION, PHASE 2 — pre-registered 2026-09-04\" (appended before this run). "
         "Generator: `wall_open_phase2.py` (this file's sibling). Chain: the ACCEPTED `sweep_phase2_tetragonal.evaluate` / `sweep_phase2_hexagonal.evaluate` "
         "(orbit -> Gram with R^T G R = G asserted -> float proposal -> exact clip with the 4 rho^2 <= D^2 certificate -> canonical code; orbit congruence; G3 invariant: "
         "float/exact agreement or degeneracy flag with exact superseding, recorded per perturbed cell; kill criteria live). Stores read-only "
         f"(`phase2_types.json` sha256 {SHA_TET[:16]}..., `phase2_hexagonal_types.json` sha256 {SHA_HEX[:16]}...; unchanged after the run: {sha_after}).", "",
         "**Scheme (verbatim from the pre-registration).** POINT: tangent basis of the witness stratum (c1 `nullspace_basis`, verbatim), steps "
         f"delta in {{{', '.join(SCHEME['point_steps'])}}} (fractional coordinates of the ITA conventional cell; hexagonal basis for IT 143-194), refinement halving to 1/{POINT_REFINE_LIMIT} "
         "on any side whose smallest step is not SAME; dim 0 => point direction not applicable. METRIC: c/a -> c/a * (1 + eps), eps in "
         f"{{{', '.join(SCHEME['metric_steps_relative'])}}} (relative), refinement halving to 1/{METRIC_REFINE_LIMIT}. Side status at the finest step: SAME / DIFFERENT / QUARANTINE; "
         "a direction is WALL when both sides are DIFFERENT. Verdicts per c1 lines 103-109: OPEN = every side SAME; WALL = some direction WALL; ONE-SIDED = otherwise; "
         "INDETERMINATE = a side ended in QUARANTINE. POINT and METRIC verdicts are reported separately; the COMBINED verdict (over all applicable directions) is the "
         "classification compared with the carried heuristic label. Flags (never verdict inputs): LINE-ISOLATED = dim 1 and the point direction is WALL; NON-SIMPLE-VERTEX = "
         "nonsimple_vertices > 0 at the witness; STAB-CHANGE = a perturbed point with a different site-stabilizer order. Off-stratum rows (special positions, +-1/96 along a "
         "generic direction) are supplementary and not verdict inputs.", "",
         "**Language (stated once).** OPEN means the type holds on the tested neighbourhood, not an interval proof. No naming here. Every type stays "
         f"\"not matched against the records checked as of {SNAPSHOT}\"; a neighbour's \"Schmitt-printed TYPE\" status means the stored type has a pass-P2 sighting "
         "(Schmitt's printed representative cell for that (group, b, point) reproduced by the chain with the same canonical code); \"f printed\" is the weaker f-vector-level fact "
         "against the accepted digitizations of his tetragonal / trigonal-hexagonal tables. Facet counts never exceeded 38 (kill bar live).", "",
         f"**Determinism.** `WALL_OPEN_PHASE2.json` (sorted keys, no timings) md5 = `{md5}`; a second full run (`--fresh`) must reproduce it byte for byte (see the STATUS entry for the re-run record).", "",
         f"**Runtime.** {total_s:.0f} s wall for this invocation ({jobs} forked workers; sum of per-cell walls {sums:.0f} s); cells: {len(res)} ({len(crashes)} crashed).", "",
         "## Summary table (doc order: tetragonal verdict-table order, then hexagonal summary-table order)", "",
         "| # | id | family | IT | c/a | f | dim | ns | previous heuristic label | POINT | METRIC | **COMPUTED (combined)** | flags | agree? |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        if "crash" in r:
            L.append(f"| {r['rank']} | `{r['id']}` | {r['family']} | | | | | | | | | **CRASH** {r['crash']} | | |")
            continue
        fl = [k for k, v in r["flags"].items() if v]
        L.append(f"| {r['rank']} | `{r['id']}` | {r['family'][:3]} | {r['IT']} {r['symbol']} | {r['c_over_a']} | {tuple(r['base_f'])} | {r['stratum_dim']} | {r['base_nonsimple']} | "
                 f"{r['previous_label']} | {r['point_verdict']}{(' ' + str(r['point_walls'])) if r['point_walls'] else ''} | {r['metric_verdict']} | **{r['combined_verdict']}** | "
                 f"{', '.join(fl) or '-'} | {r['agree']} |")
    L += ["", "## Aggregate (per verdict, per family)", ""]
    for fam, a in agg.items():
        L.append(f"- **{fam}** (n = {a['n']}): COMBINED {a['combined']}; POINT {a['point']}; METRIC {a['metric']}; agreement with the heuristic label {a['agree']}; "
                 f"flags: line-isolated {a['line_isolated']}, non-simple-vertex {a['nonsimple_vertex']}, stab-change {a['stab_change_any']}, float-superseded {a['float_superseded_any']}, "
                 f"quarantine {a['quarantine_any']}.")
    both = Counter(r["combined_verdict"] for r in good)
    L.append(f"- **all 165**: COMBINED {dict(sorted(both.items()))}; agreement {dict(sorted(Counter(r['agree'] for r in good).items()))}.")
    ns_tab = Counter((r["combined_verdict"], r["base_nonsimple"] > 0) for r in good)
    L.append("- Non-simple vertices at the witness vs verdict (a non-simple vertex at a general position is expected to split under a generic move unless it is "
             "symmetry-forced, e.g. lies on a rotation axis of the group): "
             + "; ".join(f"{v} with ns>0: {ns_tab[(v, True)]}, ns=0: {ns_tab[(v, False)]}" for v in ("OPEN", "WALL", "ONE-SIDED", "INDETERMINATE") if ns_tab[(v, True)] + ns_tab[(v, False)])
             + f". WALL cells with ns = 0 (simple witness cell on a transition): {[r['id'] for r in good if r['combined_verdict'] == 'WALL' and r['base_nonsimple'] == 0]}.")
    L.append(f"- Verdict step size in c/a: the relative verdict step 1/192 is <= 1/96 absolute for the {sum(1 for r in good if F(r['c_over_a']) <= 2)} cells with c/a <= 2; the cells with c/a > 2 are "
             + ", ".join(f"`{r['id']}` (c/a {r['c_over_a']}, absolute step {frac_str(F(r['c_over_a']) / 192)})" for r in good if F(r["c_over_a"]) > 2) + ".")
    dis = [r for r in good if r["agree"] == "NO"]
    L += ["", f"## Cells where the computed verdict contradicts the heuristic label ({len(dis)})", ""]
    if dis:
        L += ["| # | id | family | IT | c/a | previous label | POINT | METRIC | COMPUTED | reading |", "|---|---|---|---|---|---|---|---|---|---|"]
        for r in dis:
            reading = {("open-likely", "WALL"): "label predicted open; the witness sits on a transition",
                       ("open-likely", "ONE-SIDED"): "label predicted open; one side of some direction changes at the finest step (short neighbourhood, not a wall)",
                       ("wall-suspect", "OPEN"): "label (1 stored b-ratio) predicted a wall; the type holds on the tested neighbourhood",
                       ("wall-suspect", "ONE-SIDED"): "label predicted a wall; the type changes on one side only",
                       ("carried OPEN", "ONE-SIDED"): "carried verdict OPEN (absolute b-steps); one side changes under the relative metric scheme",
                       ("carried WALL", "ONE-SIDED"): "carried WALL; one-sided here"}.get((r["previous_label_class"], r["combined_verdict"]), "")
            L.append(f"| {r['rank']} | `{r['id']}` | {r['family'][:3]} | {r['IT']} {r['symbol']} | {r['c_over_a']} | {r['previous_label']} | {r['point_verdict']} | {r['metric_verdict']} | **{r['combined_verdict']}** | {reading} |")
    else:
        L.append("None.")
    na = [r for r in good if r["agree"] == "n/a"]
    L += ["", f"Indeterminate labels resolved (n/a for agreement, {len(na)}): " + (", ".join(f"`{r['id']}` -> {r['combined_verdict']}" for r in na) or "none") + "."]
    walls = [r for r in good if r["combined_verdict"] == "WALL"]
    L += ["", f"## Wall cells ({len(walls)}) and their neighbouring types (the naming-relevant fact)", "",
          "For each wall direction the type on each side at the finest step is named by f-vector, p-vector, aut, non-simple count, stored id (union of the two phase-2 stores), "
          "whether that stored type is a Schmitt-printed TYPE (pass-P2 sighting, groups listed) and whether its f-vector is printed in the witness group's table.", ""]
    cert = {r["id"] for r in good}
    ws = Counter(); all_stored, with_schmitt, with_cert, with_unstored = [], [], [], []
    for r in walls:
        fins = []
        for wd in r["combined_walls"]:
            kind = "metric" if wd == "metric" else "point"
            d = None if wd == "metric" else list(wd)
            for sign in (-1, 1):
                cand = [x for x in r["rows"] if x["kind"] == kind and x["direction"] == d and not x["off_stratum"] and (F(x["eps"]) > 0) == (sign > 0)]
                fins.append(min(cand, key=lambda x: abs(F(x["eps"]))))
        ws.update("stored" if x["stored_id"] else "not stored" for x in fins)
        if all(x["stored_id"] for x in fins):
            all_stored.append(r["id"])
        if any(x["schmitt_type_groups"] for x in fins):
            with_schmitt.append(r["id"])
        if any(x["stored_id"] in cert for x in fins):
            with_cert.append(r["id"])
        if any(not x["stored_id"] for x in fins):
            with_unstored.append(r["id"])
    L += ["**Wall-neighbour summary.** " + f"Wall-side cells at the finest step: {dict(ws)}. Wall cells whose every wall-side neighbour is a stored type: {len(all_stored)}; "
          f"with at least one wall-side neighbour that is a Schmitt-printed TYPE: {len(with_schmitt)} ({', '.join('`' + i + '`' for i in with_schmitt)}); "
          f"with a wall-side neighbour that is itself one of the 165 certified cells: {len(with_cert)} ({', '.join('`' + i + '`' for i in with_cert)}); "
          f"with a wall-side neighbour NOT in any store (a type the sweeps never sampled; recorded here only): {len(with_unstored)} ({', '.join('`' + i + '`' for i in with_unstored)}). "
          "Previous label classes of the wall cells: " + str(dict(Counter(r["previous_label_class"] for r in walls))) + ".", ""]
    for r in walls:
        L.append(f"### `{r['id']}` — {r['family']}, IT({r['IT']}) {r['symbol']}, witness {r['witness_point']} c/a = {r['c_over_a']}, f = {tuple(r['base_f'])} {r['base_p']} aut {r['base_aut']}, "
                 f"dim {r['stratum_dim']}, ns {r['base_nonsimple']}; POINT {r['point_verdict']} walls {r['point_walls']}; METRIC {r['metric_verdict']}; flags: "
                 f"{', '.join(k for k, v in r['flags'].items() if v) or '-'}; previous label: {r['previous_label']}")
        L.append("")
        for wd in r["combined_walls"]:
            kind = "metric" if wd == "metric" else "point"
            d = None if wd == "metric" else list(wd)
            for sign in (-1, 1):
                cand = [x for x in r["rows"] if x["kind"] == kind and x["direction"] == d and not x["off_stratum"] and (F(x["eps"]) > 0) == (sign > 0)]
                fin = min(cand, key=lambda x: abs(F(x["eps"])))
                nb = next((n for n in r["neighbours"] if n["code_id"] == fin["code_id"]), None)
                side_txt = f"{'metric' if kind == 'metric' else 'point ' + str(tuple(d))} {'+' if sign > 0 else '-'} side (finest step {fin['eps']}, {'c/a' if kind == 'metric' else 'point'} = {fin['b'] if kind == 'metric' else fin['point']})"
                L.append(f"- {side_txt}: " + (fmt_nb(nb) if nb else f"{fin['status']} {fin.get('quarantine') or ''}"))
        others = [n for n in r["neighbours"]]
        if others:
            L.append(f"- all neighbouring types seen on-stratum ({len(others)}): " + " ; ".join(fmt_nb(n) for n in others))
        L.append("")
    ones = [r for r in good if r["combined_verdict"] == "ONE-SIDED"]
    L += [f"## One-sided cells ({len(ones)}): the changing side(s)", ""]
    for r in ones:
        ch = [k for k, v in r["sides"].items() if v != "SAME"]
        L.append(f"- `{r['id']}` {r['family'][:3]} IT({r['IT']}) c/a {r['c_over_a']} f {tuple(r['base_f'])}: changing side(s) {ch}; neighbours: " + (" ; ".join(fmt_nb(n) for n in r["neighbours"]) or "none"))
    ind = [r for r in good if r["combined_verdict"] == "INDETERMINATE"]
    L += ["", f"## Indeterminate cells (chain quarantine on a side; {len(ind)})", ""]
    for r in ind:
        q = [(x["kind"], x["direction"], x["eps"], x["quarantine"]) for x in r["rows"] if x["status"] == "QUARANTINE"]
        L.append(f"- `{r['id']}` {r['family'][:3]} IT({r['IT']}) c/a {r['c_over_a']}: {q}")
    if not ind:
        L.append("None.")
    L += ["", "## Regression against COLLISION_PHASE2_RESULTS.md (top-3 tetragonal point verdicts; same steps, same chain; ASSERTED)", "",
          "| id | expected POINT (walls) | got POINT (walls) | agrees | its b verdict there (absolute steps) | METRIC verdict here (relative steps) |", "|---|---|---|---|---|---|"]
    for cid, v in reg.items():
        L.append(f"| `{cid}` | {v['expected_point']} {v['expected_walls']} | {v['got_point']} {v['got_walls']} | {v['point_agrees']} | {v['collision_json_b_verdict']} | {v['metric_verdict_here']} |")
    L.append(f"\nRegression: {'PASS' if reg_ok else 'FAIL'}.")
    sup = Counter()
    for r in good:
        for x in r["rows"]:
            if x["float_superseded"]:
                sup[r["id"]] += 1
    L += ["", "## G3 bookkeeping", "",
          f"- Perturbed cells whose float proposal was degeneracy-flagged and superseded by the exact clip: {sum(sup.values())} rows over {len(sup)} cells "
          + ("(" + ", ".join(f"`{k}` x{v}" for k, v in sorted(sup.items())) + ")" if sup else "") + ".",
          f"- Quarantine rows (ChainError, recorded, never SAME): {sum(1 for r in good for x in r['rows'] if x['status'] == 'QUARANTINE')}.",
          f"- Rows with a site-stabilizer change (the step landed on a special point of the stratum): {sum(1 for r in good for x in r['rows'] if x.get('stab_change') and not x['off_stratum'])}.",
          f"- Total chain evaluations: {sum(r['n_evaluations'] for r in good)}.",
          "", "## Honest limits", "",
          "- Finite steps only: OPEN = the code is unchanged at every tested step (largest 1/48 point / 1/96 relative metric; smallest 1/96 point / 1/192 relative metric, refined to 1/1536 and 1/3072 on failing sides). "
          "A change seen at the LARGER coarse step with SAME at the smaller one leaves the verdict OPEN (c1 rule: the verdict uses the smallest step on each side) and is recorded as a neighbour.",
          "- The classification is at the FIRST WITNESS only; other sightings of the same type (other groups, points, b-ratios) are not perturbed here.",
          "- The metric direction is the family's single free ratio c/a; no lattice-angle direction exists in these families.",
          "- Neighbour naming is by stored id in the two phase-2 stores plus the cubic seeds; a \"not stored\" neighbour is a type the sweeps never sampled (recorded here only, not added to any store).",
          "- Schmitt-printed TYPE status relies on the pass-P2 sightings of the accepted sweeps (his printed representative reproduced at his printed point under the accepted conversions); it is type-level evidence at his printed points only, not a statement about his unprinted data.",
          "", "## Per-cell detail (every row; off-stratum rows marked)", ""]
    for r in res:
        if "crash" in r:
            L.append(f"**`{r['id']}`** CRASH: {r['crash']}\n")
            continue
        L.append(f"**`{r['id']}`** {r['family']} IT({r['IT']}) {r['symbol']} witness {r['witness_point']} c/a {r['c_over_a']} basis {r['tangent_basis']} base f={tuple(r['base_f'])} {r['base_p']} aut {r['base_aut']} ns {r['base_nonsimple']} — "
                 f"POINT {r['point_verdict']} / METRIC {r['metric_verdict']} / COMBINED **{r['combined_verdict']}**")
        L.append("")
        L.append("| kind | direction | eps | point | c/a | stab | f | p | aut | ns | status | stored id | Schmitt type in | f printed | float superseded |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for x in r["rows"]:
            tag = (" (off-stratum)" if x["off_stratum"] else "") + (" (refine)" if x["refine"] else "")
            L.append(f"| {x['kind']}{tag} | {tuple(x['direction']) if x['direction'] else '-'} | {x['eps']} | {x['point']} | {x['b']} | {x['stab']} | {tuple(x['f']) if x['f'] else '-'} | {x['p'] or '-'} | {x['aut']} | {x['nonsimple']} | "
                     f"{x['status']}{(' ' + x['quarantine']) if x['quarantine'] else ''} | {x['stored_id'] or ('-' if x['status'] != 'DIFFERENT' else 'not stored')} | "
                     f"{', '.join(map(str, x['schmitt_type_groups'])) if x['schmitt_type_groups'] else '-'} | {x['fvec_printed']} | {x['float_superseded']} |")
        L.append("")
    tmp = OUT_MD + ".tmp"
    open(tmp, "w").write("\n".join(L) + "\n")
    os.replace(tmp, OUT_MD)
    return md5, reg_ok, len(crashes)


# ---------------------------------------------------------------- main ---
def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--budget-s", type=float, default=540.0)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--only", default=None, help="comma-separated ids (debug)")
    a = ap.parse_args(argv)
    t_all = time.time()
    os.makedirs(CELLS_DIR, exist_ok=True)
    if a.fresh:
        for fn in os.listdir(CELLS_DIR):
            os.remove(os.path.join(CELLS_DIR, fn))
    assert sha256_file(STORE_TET) == SHA_TET, "phase2_types.json sha256 drift"
    assert sha256_file(STORE_HEX) == SHA_HEX, "phase2_hexagonal_types.json sha256 drift"
    cells = parse_cells()
    if a.only:
        keep = set(a.only.split(","))
        cells = [c for c in cells if c["id"] in keep]
    # context for the workers (built in the parent, inherited by fork; the big
    # stores are dropped before the fork)
    tet = json.load(open(STORE_TET))["types"]
    hx = json.load(open(STORE_HEX))["types"]
    assert all(i in hx for i in tet), "hexagonal store does not contain every tetragonal-store type"
    code2id, schmitt_groups, witness = {}, {}, {}
    for store in (tet, hx):
        for tid, e in store.items():
            code2id.setdefault(e["canon_code"], tid)
            gs = sorted({s["group"] for s in e.get("sightings", []) if s.get("pass") == "P2"})
            if gs:
                schmitt_groups[tid] = sorted(set(schmitt_groups.get(tid, [])) | set(gs))
    for c in cells:
        e = (tet if c["family"] == "tetragonal" else hx)[c["id"]]
        witness[c["id"]] = {"canon_code": e["canon_code"], "f_vector": e["f_vector"], "p_vector": e["p_vector"],
                            "aut_order": e["aut_order"], "first_witness": e["first_witness"]}
    del tet, hx
    printed_f = {}
    printed_f.update(printed_fvectors(TABLES_TET))
    printed_f.update(printed_fvectors(TABLES_HEX))
    CTX.update(code2id=code2id, schmitt_groups=schmitt_groups, witness=witness, printed_f=printed_f)
    print(f"[wall_open_phase2] {len(cells)} cells; code map {len(code2id)} types, {len(schmitt_groups)} Schmitt-printed types; "
          f"jobs={a.jobs} budget {a.budget_s:.0f}s", flush=True)

    results = {}
    for c in cells:
        p = os.path.join(CELLS_DIR, c["id"] + ".json")
        if os.path.exists(p):
            results[c["id"]] = json.load(open(p), object_pairs_hook=OrderedDict)
    pending = [c for c in cells if c["id"] not in results]
    print(f"[wall_open_phase2] {len(results)} records present, {len(pending)} pending", flush=True)
    stopped = False
    if pending:
        ctx = mp.get_context("fork")
        with ctx.Pool(a.jobs) as pool:
            for cid, status, secs, verdict in pool.imap_unordered(worker, pending):
                results[cid] = json.load(open(os.path.join(CELLS_DIR, cid + ".json")), object_pairs_hook=OrderedDict)
                print(f"  {cid} {status:5s} {secs:6.1f}s {verdict}", flush=True)
                if time.time() - t_all > a.budget_s:
                    stopped = True
                    pool.terminate()
                    break
    done = [c for c in cells if c["id"] in results]
    if stopped or len(done) < len(cells):
        print(f"[wall_open_phase2] BUDGET STOP at a clean boundary: {len(done)}/{len(cells)} records on disk; "
              f"re-run the same command to resume (exit 3).", flush=True)
        return 3
    # sanity: every record must belong to this run's scheme (crash records are kept and reported)
    sha_after = (sha256_file(STORE_TET) == SHA_TET) and (sha256_file(STORE_HEX) == SHA_HEX)
    sums = sum(r.get("_secs", 0) for r in results.values())
    md5, reg_ok, ncrash = write_docs(results, cells, time.time() - t_all, sums, sha_after, a.jobs)
    print(f"[wall_open_phase2] wrote {OUT_JSON} (md5 {md5}) and {OUT_MD}; regression {'PASS' if reg_ok else 'FAIL'}; "
          f"crashes {ncrash}; stores unchanged {sha_after}; {time.time() - t_all:.0f}s", flush=True)
    assert sha_after, "store sha256 changed during the run"
    assert reg_ok, "REGRESSION FAIL: top-3 point verdicts differ from COLLISION_PHASE2_RESULTS.md"
    return 0 if ncrash == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
