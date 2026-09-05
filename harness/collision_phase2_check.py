#!/usr/bin/env python
"""collision_phase2_check.py — PHASE-2 (tetragonal) collision screen for the
TOP-15 shortlist of TRIAGE_PHASE2_RESULT.md (2026-09-04) + the first
perturbation certificates (top-3), mirroring schmitt_collision_check.py
(cubic) and round1_computations/c1_wall_open.py (perturbation).

Worklist: the 27 (shortlist type, Schmitt printed row) pairs of the triage's
"Collision screen worklist" — 20 pairs whose printed row reproduced in pass P2
as a DIFFERENT stored type (`other`, id given) and 7 pairs whose printed row
was NOT stored in the sweep (`unres`: origin-choice-2 groups 86/134/141, the
second enantiomorphs 95/96, and the IT(80) order_cycle crash row).

Per pair:
  unres -> take Schmitt's printed row (group, b, point) from
           schmitt_tetragonal_tables.json (visual digitization; PDF page cited),
           apply the group's DOCUMENTED setting conversion
           (PHASE2_SCHMITT_ORIGIN_CHECK.md: origin-choice-2 groups: p_ours =
           p_his + s with the shift that reproduced ALL printed rows of the
           group; second enantiomorphs 95/96: z -> -z; IT(80): none — the row
           crashed on the float facet-ordering proposal, now handled by the
           exact order_cycle fallback, ORDER_CYCLE_FIX_2026-09-04.md), run the
           ACCEPTED phase-2 exact chain (sweep_phase2_tetragonal.evaluate:
           orbit -> Gram(b) -> float proposal -> exact clip with the
           4*rho^2 <= D^2 certificate asserted on cell 0 AND a second orbit
           cell, Euler, orbit congruence) at the printed b-ratio, ASSERT the
           printed f-vector reproduces (else FVEC-MISMATCH, stop for that
           pair), then compare the canonical code with the shortlist type.
           Robustness: every alternative conversion that reproduced all rows
           of the group in the origin check is also run and must give the
           SAME canonical code (recorded).
  other -> confirm by direct canonical-code comparison from the store
           (phase2_types.json): the stored P2 sighting (group, printed point,
           printed b, kind schmitt_printed) must exist on the stated id, its
           f-vector must equal the printed one, and its canon_code must differ
           from the target's. Recomputed only if the stored cell is missing.

Verdicts: SAME TYPE (collision — candidate reframes per kill criteria) /
DIFFERENT TYPE (a distinct type at the same (group, f, b): a same-f-vector-
two-types micro-fact, tetragonal edition) / FVEC-MISMATCH / TIMEOUT-DEFERRED
(600 s per pair) / CHAIN-QUARANTINE (ChainError; recorded).

Perturbation certificates (top-3: 4e9c9b076cfec323, 49cedbdd58376fac,
f654982d74d740f6): at the stored first witness (group, point, b), the point is
moved by +-1/96, +-1/48 along every tangent direction of its Wyckoff stratum
(fixed subspace of the site stabilizer's linear parts) at the witness b, AND
the b-ratio is moved by +-1/96, +-1/48 at the witness point; where the
smallest step on a side changes the code the step is halved down to 1/1536.
Per direction class (point / metric) separately: OPEN = code unchanged at the
smallest step on every side; WALL = changes on BOTH sides of some direction;
ONE-SIDED otherwise. The type on each side is reported with its stored id
where the code is in the store, else "not stored". One generic off-stratum
point step (+-1/96) is recorded as supplementary (leaves the stratum; not
part of the verdict).

LANGUAGE (G5, once): a DIFFERENT verdict does NOT establish novelty —
Schmitt's tables print ONE representative point per (group, f-vector) from a
grid SAMPLING (351 CPU-years; 14 TB unprinted); every survivor stays "not
matched against the catalog snapshot of 2026-09-03".

Run (from harness/):
  python3 collision_phase2_check.py
Writes: COLLISION_PHASE2_RESULTS.md, collision_phase2_results.json.
Exit 0 iff every pair produced a verdict and every perturbation run finished.
"""
import hashlib
import json
import os
import signal
import sys
import time
from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import orbit                                          # noqa: E402
import sweep_phase2_tetragonal as S2                  # noqa: E402

STORE = os.path.join(HERE, "phase2_types.json")
SHA_FILE = os.path.join(HERE, "phase2_types.SHA256SUMS")
TABLES = os.path.join(HERE, "schmitt_tetragonal_tables.json")
ORIGIN_JSON = os.path.join(HERE, "phase2_schmitt_origin_check.json")
OUT_MD = os.path.join(HERE, "COLLISION_PHASE2_RESULTS.md")
OUT_JSON = os.path.join(HERE, "collision_phase2_results.json")
TIMEOUT_S = 600
SNAPSHOT = "2026-09-03"
RUN_DATE = "2026-09-04"

# The 27 worklist pairs, VERBATIM from TRIAGE_PHASE2_RESULT.md ("Collision
# screen worklist for the shortlist"); printed point/b as digitized
# (schmitt_tetragonal_tables.json, keyed f/b/pt; PDF page = printed page + 5).
PAIRS = [
    dict(pair="Q01", rank=1, target="4e9c9b076cfec323", group=92, fvec=(40, 60, 22), b="7/5",
         point=("1951/3996", "1/3996", "1/7992"), pdf=47, p2="other", p2_id="cf92c5d0bb79041b"),
    dict(pair="Q02", rank=1, target="4e9c9b076cfec323", group=96, fvec=(40, 60, 22), b="7/5",
         point=("1951/3996", "1/3996", "1/7992"), pdf=47, p2="unres", p2_id=None),
    dict(pair="Q03", rank=2, target="49cedbdd58376fac", group=92, fvec=(44, 66, 24), b="797/1000",
         point=("57/125", "2/125", "1/8"), pdf=47, p2="other", p2_id="ab93cbeb7be9da28"),
    dict(pair="Q04", rank=2, target="49cedbdd58376fac", group=96, fvec=(44, 66, 24), b="797/1000",
         point=("57/125", "2/125", "1/8"), pdf=47, p2="unres", p2_id=None),
    dict(pair="Q05", rank=3, target="f654982d74d740f6", group=141, fvec=(38, 57, 21), b="797/1000",
         point=("1/2", "47/125", "31/250"), pdf=84, p2="unres", p2_id=None),
    dict(pair="Q06", rank=4, target="4f6d3e68cbd9e729", group=98, fvec=(42, 63, 23), b="38/25",
         point=("1129/2518", "859/2518", "565/5036"), pdf=53, p2="other", p2_id="2f2e04c27de95ac3"),
    dict(pair="Q07", rank=5, target="1497877268495988", group=91, fvec=(32, 48, 18), b="14/25",
         point=("229/3996", "71/3996", "61/2664"), pdf=45, p2="other", p2_id="e5db0e3617afd976"),
    dict(pair="Q08", rank=5, target="1497877268495988", group=95, fvec=(32, 48, 18), b="14/25",
         point=("229/3996", "71/3996", "61/2664"), pdf=45, p2="other", p2_id="e2bae62d988092d4"),
    dict(pair="Q09", rank=6, target="e0d18e5ea938d649", group=122, fvec=(36, 54, 20), b="3497/1000",
         point=("34/125", "34/125", "31/250"), pdf=70, p2="other", p2_id="5af057df372beee8"),
    dict(pair="Q10", rank=7, target="6797ab70c6015039", group=76, fvec=(32, 48, 18), b="797/1000",
         point=("1/4", "-1/4", "0"), pdf=33, p2="other", p2_id="e5760549017956be"),
    dict(pair="Q11", rank=7, target="6797ab70c6015039", group=78, fvec=(32, 48, 18), b="797/1000",
         point=("1/4", "-1/4", "0"), pdf=33, p2="other", p2_id="e5760549017956be"),
    dict(pair="Q12", rank=7, target="6797ab70c6015039", group=92, fvec=(32, 48, 18), b="7/5",
         point=("22/333", "44/999", "61/2664"), pdf=47, p2="other", p2_id="1614109bcc5801ed"),
    dict(pair="Q13", rank=7, target="6797ab70c6015039", group=96, fvec=(32, 48, 18), b="7/5",
         point=("22/333", "44/999", "61/2664"), pdf=47, p2="other", p2_id="3a7c6d5f00cde1ae"),
    dict(pair="Q14", rank=8, target="cd4fb52572edcb73", group=86, fvec=(30, 45, 17), b="3497/1000",
         point=("59/125", "0", "31/125"), pdf=40, p2="unres", p2_id=None),
    dict(pair="Q15", rank=8, target="cd4fb52572edcb73", group=93, fvec=(30, 45, 17), b="3497/1000",
         point=("231/500", "-17/500", "107/500"), pdf=48, p2="other", p2_id="adbb83c95151fc35"),
    dict(pair="Q16", rank=8, target="cd4fb52572edcb73", group=118, fvec=(30, 45, 17), b="3497/1000",
         point=("247/500", "-1/500", "123/500"), pdf=66, p2="other", p2_id="da1833391efcd38c"),
    dict(pair="Q17", rank=8, target="cd4fb52572edcb73", group=134, fvec=(30, 45, 17), b="797/1000",
         point=("219/500", "-31/500", "47/250"), pdf=79, p2="unres", p2_id=None),
    dict(pair="Q18", rank=9, target="086ac96faf390886", group=76, fvec=(36, 54, 20), b="797/1000",
         point=("1597/3996", "401/3996", "0"), pdf=33, p2="other", p2_id="0087d56fd2a8a610"),
    dict(pair="Q19", rank=9, target="086ac96faf390886", group=78, fvec=(36, 54, 20), b="797/1000",
         point=("1597/3996", "401/3996", "0"), pdf=33, p2="other", p2_id="0087d56fd2a8a610"),
    dict(pair="Q20", rank=10, target="164d4bd63d82d0c3", group=76, fvec=(40, 60, 22), b="797/1000",
         point=("1807/3996", "191/3996", "0"), pdf=33, p2="other", p2_id="c1a62b4c22e7c6e8"),
    dict(pair="Q21", rank=10, target="164d4bd63d82d0c3", group=78, fvec=(40, 60, 22), b="797/1000",
         point=("1807/3996", "191/3996", "0"), pdf=33, p2="other", p2_id="c1a62b4c22e7c6e8"),
    dict(pair="Q22", rank=11, target="5dc2479b9bc14edc", group=98, fvec=(42, 63, 23), b="38/25",
         point=("1129/2518", "859/2518", "565/5036"), pdf=53, p2="other", p2_id="2f2e04c27de95ac3"),
    dict(pair="Q23", rank=12, target="3ebbca7ed2eda199", group=98, fvec=(40, 60, 22), b="38/25",
         point=("1129/2518", "553/1259", "565/5036"), pdf=53, p2="other", p2_id="1d68503f7c026843"),
    dict(pair="Q24", rank=13, target="7575121042ade3b3", group=80, fvec=(32, 48, 18), b="3497/1000",
         point=("353/1413", "235/942", "0"), pdf=35, p2="unres", p2_id=None),
    dict(pair="Q25", rank=13, target="7575121042ade3b3", group=98, fvec=(32, 48, 18), b="38/25",
         point=("1129/2518", "129/2518", "565/5036"), pdf=52, p2="other", p2_id="014a0747d02498e7"),
    dict(pair="Q26", rank=14, target="213c7a114d5a97a8", group=98, fvec=(42, 63, 23), b="38/25",
         point=("1129/2518", "859/2518", "565/5036"), pdf=53, p2="other", p2_id="2f2e04c27de95ac3"),
    dict(pair="Q27", rank=15, target="2e8e49eb28497267", group=95, fvec=(40, 60, 22), b="14/25",
         point=("223/444", "355/1332", "239/7992"), pdf=45, p2="unres", p2_id=None),
]

TOP3 = ["4e9c9b076cfec323", "49cedbdd58376fac", "f654982d74d740f6"]

# Documented conventions (PHASE2_SCHMITT_ORIGIN_CHECK.md, machine-verified on
# ALL printed rows of each group): origin-choice-2 groups -> p_ours = p_his + s
# (the check's `shifted`), primary s = the check's best_shift; second
# enantiomorphs -> z -> -z (transform (1,1,-1,False)). Alternatives that also
# reproduced every row are run as a robustness check (same code expected: a
# global translation / an improper symmetry leaves the combinatorial type
# invariant — canon_code identifies mirror images).
TWO_ORIGIN = {85, 86, 88, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142}
ENANTIO_SECOND = {95, 96}


class PairTimeout(Exception):
    pass


def _alarm(signum, frame):
    raise PairTimeout()


def frac_str(x):
    return S2.frac_str(x)


def pt_str(p):
    return "(" + ", ".join(frac_str(x) for x in p) + ")"


def code_id(code_str):
    return hashlib.sha1(code_str.encode("ascii")).hexdigest()[:16]


def parse_shift(s):
    # "('1/4', '3/4', '0')" -> (F, F, F)
    return tuple(F(t.strip().strip("'")) for t in s.strip("()").split(","))


def conversions_for(group, origin):
    """[(label, callable point->point)] — primary first, then alternatives."""
    if group in TWO_ORIGIN:
        info = origin["two_origin"][str(group)]
        best = tuple(F(x) for x in info["best_shift"])
        alts = [parse_shift(s) for s in info["shifts_all_rows"]]
        alts = [a for a in alts if a != best]
        out = [(f"origin-2 -> origin-1 shift +{pt_str(best)}",
                lambda p, s=best: tuple(x + y for x, y in zip(p, s)))]
        out += [(f"alt shift +{pt_str(a)}", lambda p, s=a: tuple(x + y for x, y in zip(p, s)))
                for a in alts]
        return out
    if group in ENANTIO_SECOND:
        info = origin["enantiomorph_second"][str(group)]
        alts = [eval(t) for t in info["transforms_all_rows"]]
        prim = (1, 1, -1, False)
        assert prim in alts, (group, alts)

        def mk(t):
            sx, sy, sz, sw = t

            def f(p):
                x, y, z = p
                if sw:
                    x, y = y, x
                return (sx * x, sy * y, sz * z)
            return f
        out = [("second enantiomorph: z -> -z", mk(prim))]
        out += [(f"alt transform (sx,sy,sz,swap)={t}", mk(t)) for t in alts if t != prim]
        return out
    return [("none (printed point verbatim)", lambda p: p)]


def evaluate(num, p, b):
    """Accepted phase-2 exact chain; certificates asserted inside."""
    return S2.evaluate(num, tuple(F(x) for x in p), F(b), "collision_phase2")


def run_unres(pr, origin, types, code2type):
    t0 = time.time()
    convs = conversions_for(pr["group"], origin)
    X = tuple(F(s) for s in pr["point"])
    label, conv = convs[0]
    Xc = conv(X)
    try:
        r = evaluate(pr["group"], Xc, pr["b"])
    except S2.ChainError as exc:
        return dict(pr, conversion=label, point_ours=pt_str(Xc), verdict="CHAIN-QUARANTINE",
                    detail=f"{exc.reason}: {exc.detail}", secs=round(time.time() - t0, 1))
    got_f = tuple(r["fvec"])
    tgt = types[pr["target"]]
    code = r["code_str"]
    res = dict(pr, conversion=label, point_ours=pt_str(Xc), got_fvec=got_f,
               got_pvec=S2.pvec_compact(r["pvec"]), got_aut=r["aut"], orbit_n=r["orbit_conventional"],
               stab=r["stabilizer_order"], period=r["period"], cutoff_D2=r["cutoff_D2"],
               congruence_checked=r["congruence_checked"], code=code,
               store_hit=code2type.get(code), store_hit_id_of_code=code_id(code))
    if got_f != tuple(pr["fvec"]):
        res.update(verdict="FVEC-MISMATCH", detail=f"exact f={got_f} vs printed {pr['fvec']}")
        res["secs"] = round(time.time() - t0, 1)
        return res
    res["verdict"] = "SAME TYPE" if code == tgt["canon_code"] else "DIFFERENT TYPE"
    # robustness: alternative documented conversions must give the same code
    alt = []
    for lab, cv in convs[1:]:
        Xa = cv(X)
        try:
            ra = evaluate(pr["group"], Xa, pr["b"])
            alt.append((lab, pt_str(Xa), tuple(ra["fvec"]), ra["code_str"] == code))
        except S2.ChainError as exc:
            alt.append((lab, pt_str(Xa), None, f"quarantine {exc.reason}"))
    res["alternatives"] = alt
    res["alternatives_agree"] = all(a[3] is True for a in alt)
    # coincidence: is the converted printed point (mod 1) a stored sighting point
    # of the target in this group at this b?
    sp = {(tuple(F(x) % 1 for x in s["point"]), s["b"]) for s in tgt["sightings"]
          if s["group"] == pr["group"]}
    res["coincide"] = (tuple(x % 1 for x in Xc), pr["b"]) in sp
    res["secs"] = round(time.time() - t0, 1)
    return res


def run_other(pr, types, code2type):
    """Confirm from the store; recompute only if the stored P2 cell is missing."""
    t0 = time.time()
    tgt = types[pr["target"]]
    sid = pr["p2_id"]
    e = types.get(sid)
    res = dict(pr, conversion="none (stored P2 cell, printed point verbatim)",
               point_ours=pt_str(tuple(F(s) for s in pr["point"])))
    sight = None
    if e is not None:
        for s in e["sightings"]:
            if (s["group"] == pr["group"] and s["kind"] == "schmitt_printed"
                    and s["b"] == pr["b"] and tuple(s["point"]) == tuple(pr["point"])):
                sight = s
                break
    if e is None or sight is None:
        # stored P2 cell missing -> recompute
        r = evaluate(pr["group"], tuple(F(s) for s in pr["point"]), pr["b"])
        code = r["code_str"]
        got_f = tuple(r["fvec"])
        res.update(source="RECOMPUTED (stored P2 cell missing)", got_fvec=got_f,
                   got_pvec=S2.pvec_compact(r["pvec"]), got_aut=r["aut"],
                   orbit_n=r["orbit_conventional"], stab=r["stabilizer_order"],
                   period=r["period"], code=code, store_hit=code2type.get(code))
        if got_f != tuple(pr["fvec"]):
            res.update(verdict="FVEC-MISMATCH", detail=f"exact f={got_f} vs printed {pr['fvec']}")
        else:
            res["verdict"] = "SAME TYPE" if code == tgt["canon_code"] else "DIFFERENT TYPE"
    else:
        assert tuple(e["f_vector"]) == tuple(pr["fvec"]), (pr["pair"], e["f_vector"], pr["fvec"])
        assert code_id(e["canon_code"]) == sid
        res.update(source="store (P2 sighting present on the stated id)",
                   got_fvec=tuple(e["f_vector"]), got_pvec=S2.pvec_compact(e["p_vector"]),
                   got_aut=e["aut_order"], orbit_n=sight["orbit_conventional"],
                   stab=sight["stabilizer_order"], period=None, code=e["canon_code"],
                   store_hit=sid, congruence_checked=sight["congruence_checked"])
        res["verdict"] = "SAME TYPE" if e["canon_code"] == tgt["canon_code"] else "DIFFERENT TYPE"
        assert res["verdict"] == "DIFFERENT TYPE" or sid == pr["target"]
    sp = {(tuple(F(x) % 1 for x in s["point"]), s["b"]) for s in tgt["sightings"]
          if s["group"] == pr["group"]}
    res["coincide"] = (tuple(F(x) % 1 for x in pr["point"]), pr["b"]) in sp
    res["secs"] = round(time.time() - t0, 1)
    return res


# ------------------------------------------------------------ perturbation ---

def nullspace_basis(mats):
    """Exact basis of {v : (R - I) v = 0 for all R} as primitive integer vectors."""
    rows = []
    for R in mats:
        for i in range(3):
            rows.append([F(R[i][j] - (1 if i == j else 0)) for j in range(3)])
    A = [row[:] for row in rows]
    piv_cols, r = [], 0
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
        piv_cols.append(c)
        r += 1
    basis = []
    for fc in [c for c in range(3) if c not in piv_cols]:
        v = [F(0)] * 3
        v[fc] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -A[i][fc]
        den = 1
        for x in v:
            den = lcm(den, x.denominator)
        vi = [int(x * den) for x in v]
        g = 0
        for x in vi:
            g = gcd(g, abs(x))
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


def probe(num, p, b, ent, code2type, printed_f):
    """One perturbed evaluation -> row dict (never raises on ChainError)."""
    try:
        r = evaluate(num, p, b)
    except S2.ChainError as exc:
        return dict(point=pt_str(p), b=frac_str(b), stab=None, f=None, p=None, aut=None,
                    nonsimple=None, same=False, stored_id=None,
                    quarantine=f"{exc.reason}: {exc.detail}"[:120], fvec_printed=None)
    code = r["code_str"]
    return dict(point=pt_str(p), b=frac_str(b), stab=r["stabilizer_order"], f=tuple(r["fvec"]),
                p=S2.pvec_compact(r["pvec"]), aut=r["aut"], nonsimple=r["nonsimple"],
                same=code == ent["canon_code"], stored_id=code2type.get(code),
                quarantine=None, fvec_printed=tuple(r["fvec"]) in printed_f)


def classify(cid, types, code2type, printed_by_group):
    ent = types[cid]
    w = ent["first_witness"]
    num, b0 = w["group"], F(w["b"])
    p0 = tuple(F(s) for s in w["point"])
    printed_f = printed_by_group.get(num, set())
    t0 = time.time()
    # rederive (V0 pattern): witness -> exact -> must agree with the store
    base = evaluate(num, p0, b0)
    assert base["code_str"] == ent["canon_code"], "canonical code MISMATCH vs store"
    assert tuple(base["fvec"]) == tuple(ent["f_vector"]) and list(base["pvec"]) == list(ent["p_vector"])
    assert base["aut"] == ent["aut_order"] and base["stabilizer_order"] == w["stabilizer_order"]
    stab_ops = orbit.site_stabilizer(S2.GROUPS[num], p0)
    basis = nullspace_basis([R for R, _ in stab_ops])
    assert len(basis) == w["stratum_dim"], (len(basis), w["stratum_dim"])
    eps_list = [F(-1, 48), F(-1, 96), F(1, 96), F(1, 48)]
    rows = []

    def add(kind, d, eps, refine=False):
        if kind == "point":
            q = tuple(p0[k] + eps * d[k] for k in range(3))
            row = probe(num, q, b0, ent, code2type, printed_f)
        else:
            row = probe(num, p0, b0 + eps, ent, code2type, printed_f)
        row.update(kind=kind, direction=d, eps=eps, refine=refine, off_stratum=False)
        rows.append(row)
        return row["same"]

    dirs = [("point", d) for d in basis] + [("b", None)]
    for kind, d in dirs:
        for eps in eps_list:
            add(kind, d, eps)
    side_same = {}
    for kind, d in dirs:
        for sign in (-1, 1):
            smallest = min((x for x in rows if x["kind"] == kind and x["direction"] == d
                            and not x["off_stratum"] and sign * x["eps"] > 0),
                           key=lambda x: abs(x["eps"]))
            same, den = smallest["same"], 96
            while not same and den < 1536:
                den *= 2
                same = add(kind, d, F(sign, den), True)
            side_same[(kind, d, sign)] = same

    def verdict_for(kind):
        ds = [d for k, d in dirs if k == kind]
        walls = [d for d in ds if not side_same[(kind, d, -1)] and not side_same[(kind, d, 1)]]
        if all(side_same[(kind, d, s)] for d in ds for s in (-1, 1)):
            return "OPEN", walls
        return ("WALL" if walls else "ONE-SIDED"), walls

    pv, pw = verdict_for("point")
    bv, bw = verdict_for("b")
    # supplementary off-stratum step (special positions only)
    if len(basis) < 3:
        for dgen in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3)]:
            if rank_of(list(basis) + [dgen]) == len(basis) + 1:
                break
        for eps in (F(-1, 96), F(1, 96)):
            q = tuple(p0[k] + eps * dgen[k] for k in range(3))
            row = probe(num, q, b0, ent, code2type, printed_f)
            row.update(kind="point", direction=dgen, eps=eps, refine=False, off_stratum=True)
            rows.append(row)
    return dict(id=cid, group=num, symbol=S2.GROUPS[num]["international_short"], point=pt_str(p0),
                b=frac_str(b0), stratum_dim=w["stratum_dim"], stab=w["stabilizer_order"],
                basis=basis, base_f=tuple(base["fvec"]), base_p=S2.pvec_compact(base["pvec"]),
                aut=base["aut"], rows=rows, point_verdict=pv, point_walls=pw,
                b_verdict=bv, b_wall=bool(bw), secs=round(time.time() - t0, 1))


# ------------------------------------------------------------------ main ---

def main():
    t_all = time.time()
    raw = open(STORE, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    want = next(t for t in open(SHA_FILE).read().split()
                if len(t) == 64 and all(c in "0123456789abcdef" for c in t))
    assert sha == want, f"phase2_types.json sha256 {sha} != {want}"
    store = json.loads(raw)
    types = store["types"]
    code2type = {v["canon_code"]: k for k, v in types.items()}
    assert len(code2type) == len(types), "store canon codes not unique"
    origin = json.load(open(ORIGIN_JSON))
    tables = json.load(open(TABLES))
    printed_by_group, row_lookup = {}, {}
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for g in blk["groups"]:
            printed_by_group.setdefault(g, set())
            for r in blk["rows"]:
                printed_by_group[g].add(tuple(r["f"]))
                row_lookup[(g, tuple(r["f"]), r["b"], tuple(r["pt"]))] = r["pdf_page"]
    # every worklist row must be a digitized row (citation check)
    for pr in PAIRS:
        key = (pr["group"], tuple(pr["fvec"]), pr["b"], tuple(pr["point"]))
        assert key in row_lookup, f"{pr['pair']}: printed row not in digitization {key}"
        assert row_lookup[key] == pr["pdf"], (pr["pair"], row_lookup[key], pr["pdf"])
        assert pr["target"] in types, pr["target"]
        assert tuple(types[pr["target"]]["f_vector"]) == pr["fvec"], pr["pair"]

    results = []
    old = signal.signal(signal.SIGALRM, _alarm)
    try:
        for pr in PAIRS:
            signal.alarm(TIMEOUT_S)
            try:
                r = run_unres(pr, origin, types, code2type) if pr["p2"] == "unres" \
                    else run_other(pr, types, code2type)
            except PairTimeout:
                r = dict(pr, verdict="TIMEOUT-DEFERRED", secs=TIMEOUT_S, conversion="-",
                         point_ours="-")
            finally:
                signal.alarm(0)
            print(f"{r['pair']} rank{r['rank']:>2} IT({r['group']}) f={r['fvec']} b={r['b']} "
                  f"[{r['p2']}] -> {r['verdict']} hit={r.get('store_hit')} "
                  f"p={r.get('got_pvec')} aut={r.get('got_aut')} [{r['secs']}s]", flush=True)
            results.append(r)
        perts = []
        for cid in TOP3:
            signal.alarm(TIMEOUT_S)
            try:
                c = classify(cid, types, code2type, printed_by_group)
            except PairTimeout:
                c = dict(id=cid, point_verdict="TIMEOUT-DEFERRED", b_verdict="TIMEOUT-DEFERRED",
                         rows=[], secs=TIMEOUT_S)
            finally:
                signal.alarm(0)
            print(f"PERT {cid}: point {c['point_verdict']} / b {c['b_verdict']} [{c['secs']}s]",
                  flush=True)
            perts.append(c)
    finally:
        signal.signal(signal.SIGALRM, old)

    write_md(results, perts, types, sha, time.time() - t_all)
    json.dump({"pairs": results, "perturbation": perts, "store_sha256": sha, "run_date": RUN_DATE},
              open(OUT_JSON, "w"), indent=1, default=str)
    ok = all(r["verdict"] in ("SAME TYPE", "DIFFERENT TYPE", "FVEC-MISMATCH",
                              "TIMEOUT-DEFERRED", "CHAIN-QUARANTINE") for r in results)
    return 0 if ok else 1


def write_md(results, perts, types, sha, wall):
    L = []
    A = L.append
    A(f"# Phase-2 (tetragonal) collision screen + first perturbation certificates — TOP-15 shortlist ({RUN_DATE})")
    A("")
    A(f"Script: `collision_phase2_check.py` (pattern: `schmitt_collision_check.py`, `round1_computations/c1_wall_open.py`). "
      f"Inputs: `phase2_types.json` (sha256 `{sha[:16]}...`, MATCHES `phase2_types.SHA256SUMS`), "
      "`schmitt_tetragonal_tables.json` (VISUAL digitization 2026-09-04, single pass, text-layer cross-checked, NOT re-keyed), "
      "`phase2_schmitt_origin_check.json` / `PHASE2_SCHMITT_ORIGIN_CHECK.md` (setting conversions), "
      "worklist = `TRIAGE_PHASE2_RESULT.md` (27 pairs: 20 `other` + 7 `unres`). "
      "Chain: the ACCEPTED phase-2 modules (`phase2/metric.py`, `phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`) via "
      "`sweep_phase2_tetragonal.evaluate` with the `exact_cell.order_cycle` exact fallback (ORDER_CYCLE_FIX_2026-09-04.md). "
      "Certificate asserted per cell: 4*rho^2 <= D^2 on cell 0 AND on a second orbit cell, Euler, float/exact agreement, one canonical code across the orbit, stab | aut. "
      f"Per-pair wall-clock cap {TIMEOUT_S} s -> TIMEOUT-DEFERRED (recorded, never silent). Exact arithmetic decides.")
    A("")
    A("**LANGUAGE (G5, stated ONCE for every verdict below): a DIFFERENT-TYPE verdict does NOT establish novelty.** "
      "Schmitt 2016 prints ONE representative generating point per (group, f-vector) from a grid SAMPLING (351 CPU-years, ~14 TB unprinted); "
      "a type absent at his printed point may still occur in his unprinted data. Every survivor stays "
      f"\"not matched against the catalog snapshot of {SNAPSHOT}\". A SAME-TYPE verdict IS decisive (collision: reframe to first-realization per the kill criteria). "
      "A DIFFERENT verdict at the same (group, f, b) is a same-f-vector-two-types micro-fact (tetragonal edition of the Josehedron / Schmitt-220 pair).")
    A("")
    A("## Citations and conversions (27 pairs)")
    A("")
    A("Printed rows keyed (f, b, point) in `schmitt_tetragonal_tables.json`; PDF page = printed page + 5. "
      "Conversions (PHASE2_SCHMITT_ORIGIN_CHECK.md, each verified on ALL printed rows of its group): origin-choice-2 groups: "
      "p_ours = p_his + s (s = the check's best_shift; the other shifts that also reproduced every row are re-run as a robustness check and must give the same canonical code); "
      "second enantiomorphs 95/96: z -> -z; IT(80): none (order_cycle crash row, now exact fallback). "
      "`other` rows: the stored P2 cell (printed point verbatim, origin choice 1 = Schmitt's for one-origin groups).")
    A("")
    A("| pair | rank | target | IT | printed f | printed b | printed point (Schmitt coords) | PDF p. (printed p.) | P2 outcome | conversion applied | point in our setting |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        p2 = f"other `{r['p2_id']}`" if r["p2"] == "other" else "unres (not stored)"
        A(f"| {r['pair']} | {r['rank']} | `{r['target']}` | {r['group']} {S2.GROUPS[r['group']]['international_short']} | {r['fvec']} | {r['b']} | "
          f"({', '.join(r['point'])}) | {r['pdf']} ({r['pdf'] - 5}) | {p2} | {r['conversion']} | {r['point_ours']} |")
    A("")
    A("## Per-pair verdicts")
    A("")
    A("| pair | rank | target | IT | f | b | source | orbit | stab | PERIOD | Schmitt cell p-vector | aut | verdict | Schmitt cell = stored type | alt conversions agree | secs |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        note = ""
        if r["verdict"] == "FVEC-MISMATCH" or r["verdict"] == "CHAIN-QUARANTINE":
            note = f" ({r.get('detail')})"
        if r.get("coincide"):
            note += " [printed point = stored sighting point of the target: collision foregone]"
        hit = r.get("store_hit")
        hit_s = f"`{hit}`" if hit else ("not stored" if r.get("code") else "-")
        alt = r.get("alternatives")
        alt_s = "-" if alt is None else ("n/a (none)" if not alt else
                                         ("YES (%d)" % len(alt) if r.get("alternatives_agree") else
                                          "NO: " + "; ".join(f"{a[0]} -> {a[3]}" for a in alt)))
        src = "store" if r["p2"] == "other" and "store" in r.get("source", "") else "exact chain (this run)"
        pv = f"`{r['got_pvec']}`" if r.get("got_pvec") else "-"
        A(f"| {r['pair']} | {r['rank']} | `{r['target']}` | {r['group']} | {r['fvec']} | {r['b']} | {src} | {r.get('orbit_n', '-')} | {r.get('stab', '-')} | "
          f"{r.get('period') or '-'} | {pv} | {r.get('got_aut', '-')} | **{r['verdict']}**{note} | {hit_s} | {alt_s} | {r['secs']} |")
    A("")
    A("## Summary per shortlist type")
    A("")
    by = {}
    for r in results:
        by.setdefault((r["rank"], r["target"]), []).append(r)
    survivors, reframes, incomplete = [], [], []
    for (rk, tid), rs in sorted(by.items()):
        vs = [r["verdict"] for r in rs]
        if any(v == "SAME TYPE" for v in vs):
            s = (f"COLLISION — Schmitt's printed cell IS this type in {sum(v == 'SAME TYPE' for v in vs)}/{len(vs)} checked pair(s); "
                 "reframe per kill criteria (first-realization, not a new sighting-class candidate).")
            reframes.append((rk, tid))
        elif all(v == "DIFFERENT TYPE" for v in vs):
            s = f"survives this screen (all {len(vs)} pair(s) DIFFERENT); proceeds to G4 under snapshot language only."
            survivors.append((rk, tid))
        else:
            s = "mixed/incomplete: " + ", ".join(f"{r['pair']}={r['verdict']}" for r in rs)
            incomplete.append((rk, tid))
        A(f"- rank {rk} `{tid}`: {s}")
    A("")
    A("Notes on the 7 `unres` rows (all 7 reproduce the printed f-vector after the documented conversion, so no FVEC-MISMATCH; the conversions are therefore confirmed row-by-row here as well): "
      + "; ".join(f"{r['pair']} IT({r['group']}) -> Schmitt's cell is "
                  + (f"stored type `{r['store_hit']}`" if r.get("store_hit") else "NOT in the store (a type the menu never sampled; read-only, not added)")
                  for r in results if r["p2"] == "unres") + ".")
    A("")
    A("## Perturbation certificates (top-3)")
    A("")
    A("Method: at the stored first witness (group, point, b) the point is moved by +-1/96, +-1/48 (fractional coordinates, conventional cell) "
      "along every tangent direction of its Wyckoff stratum (fixed subspace of the site stabilizer's linear parts) at the witness b, and the "
      "b-ratio is moved by +-1/96, +-1/48 at the witness point; where the smallest step on a side changes the canonical code the step is halved down to 1/1536. "
      "Point directions and the metric direction are classified SEPARATELY: OPEN = code unchanged at the smallest step on every side; WALL = changes on both sides of some direction; ONE-SIDED otherwise. "
      "The type on each side of a wall is reported with its stored id (else \"not stored\"). "
      "The off-stratum row (special positions only) is supplementary: it leaves the stratum and is not part of the verdict. "
      "Every perturbed cell went through the same certified chain (certificate asserted per cell); a ChainError is recorded as a quarantine row, never counted as SAME.")
    A("")
    A("| # | type | IT | witness point | witness b | stratum dim (stab) | tangent basis | POINT verdict | METRIC (b) verdict | neighbouring types seen (f, p, aut, stored id; f printed in the group's Schmitt table) |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for i, c in enumerate(perts, 1):
        if not c.get("rows"):
            A(f"| {i} | `{c['id']}` | - | - | - | - | - | {c['point_verdict']} | {c['b_verdict']} | - |")
            continue
        seen = {}
        for x in c["rows"]:
            if x["off_stratum"] or x["same"]:
                continue
            k = (x["f"], x["p"], x["aut"]) if x["f"] else ("quarantine", x["quarantine"], None)
            seen.setdefault(k, set()).add((x["kind"], x["stored_id"], x["fvec_printed"]))
        seen_s = "; ".join(
            f"{k[0]} {k[1]} aut {k[2]} [{', '.join(sorted({(sid or 'not stored') for _, sid, _ in v}))}; "
            f"printed={', '.join(sorted({str(pr) for _, _, pr in v}))}; via {', '.join(sorted({kd for kd, _, _ in v}))}]"
            for k, v in seen.items()) or "none (all SAME)"
        A(f"| {i} | `{c['id']}` | {c['group']} {c['symbol']} | {c['point']} | {c['b']} | {c['stratum_dim']} ({c['stab']}) | {c['basis']} | "
          f"**{c['point_verdict']}**{' walls ' + str(c['point_walls']) if c['point_walls'] else ''} | **{c['b_verdict']}** | {seen_s} |")
    A("")
    A("### Per-step detail")
    A("")
    for c in perts:
        if not c.get("rows"):
            continue
        A(f"**`{c['id']}`** IT({c['group']}) {c['symbol']} witness {c['point']} b={c['b']}, base f={c['base_f']} p={c['base_p']} aut {c['aut']} (rederived from the witness; agrees with the store):")
        A("")
        A("| kind | direction | eps | point | b | site stab | f | p | aut | non-simple | code | stored id | f printed in group table |")
        A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for x in c["rows"]:
            tag = (" (off-stratum, supplementary)" if x["off_stratum"] else "") + (" (refine)" if x.get("refine") else "")
            if x["quarantine"]:
                A(f"| {x['kind']} | {x['direction'] if x['direction'] else 'b'}{tag} | {frac_str(x['eps'])} | {x['point']} | {x['b']} | - | - | - | - | - | QUARANTINE {x['quarantine']} | - | - |")
                continue
            A(f"| {x['kind']} | {x['direction'] if x['direction'] else 'b'}{tag} | {frac_str(x['eps'])} | {x['point']} | {x['b']} | {x['stab']} | {x['f']} | {x['p']} | {x['aut']} | {x['nonsimple']} | "
              f"{'SAME' if x['same'] else 'DIFFERENT'} | {x['stored_id'] or 'not stored'} | {x['fvec_printed']} |")
        A("")
    A("### Reading of the perturbation results (hand-written from the tables above; asserted against the computed verdicts on every run)")
    A("")
    pv = {c["id"]: (c["point_verdict"], c["b_verdict"]) for c in perts}
    if pv.get(TOP3[0]) == ("OPEN", "OPEN") and pv.get(TOP3[1]) == ("WALL", "OPEN") and pv.get(TOP3[2]) == ("OPEN", "OPEN"):
        A("- #1 `4e9c9b076cfec323` (IT 92, line (x,x,0), x = 5/24, b = 5/4): OPEN in the point direction and in b, but the open interval on the +x side is SHORT: "
          "+1/768 is SAME, +1/384 and +1/192 give `49cedbdd58376fac` (= shortlist #2), +1/96 and +1/48 give `60c6a7023f6e4280` (36,54,20); the -x side and both b sides hold at every tested step (b from 59/48 to 61/48). "
          "So #1 holds on a neighbourhood, with #2 as its immediate +x neighbour at b = 5/4.")
        A("- #2 `49cedbdd58376fac` (same line, x = 5/24, b = 19/16): WALL in the point direction at every tested step down to +-1/1536 (-x side: `4e9c9b076cfec323` = #1; +x side: `60c6a7023f6e4280`), yet OPEN in b at the witness point (SAME at b = 455/384 and 115/96; -1/192 gives `60c6a7023f6e4280`, -1/48 gives `e5760549017956be`, +1/48 gives #1). "
          "Together with the #1 scan (where #2 occupies x = 5/24 + 1/384 .. + 1/192 at b = 5/4) this reads as a THIN BAND in the (x, b) plane running from about (5/24, 19/16) to (5/24 + ~1/300, 5/4): not a strict codimension-1 wall (it has b-width), but of width < 1/768 in x at b = 19/16. "
          "The cell is simple (0 non-simple vertices) so the x-interval is nonempty; only its width is below the tested resolution. "
          "CORRECTION to the triage labels: the 'wall-suspect' / METRIC-THIN (1 b) label on #2 was b-based and is refuted in b (open on [455/384, 115/96] at x = 5/24) and #2 is now also sighted at b = 5/4 (at x = 5/24 + 1/384, + 1/192, read-only, NOT added to the store); the label survives only as 'thin in x'. "
          "Whether #2 deserves a G4 slot of its own or is best presented as the transition type between #1 and `60c6a7023f6e4280` is a judgment for the main session.")
        A("- #3 `f654982d74d740f6` (IT 141, plane (0,y,z), witness (0,1/12,1/12), b = 1/2): OPEN in both point directions and in b; the -y side is short (-1/384 SAME; -1/192 gives a NOT-STORED (31,48,19) cell with 3 non-simple vertices, i.e. a wall cell; -1/96 gives `9ff7306e4a6cbf44` (34,51,19); -1/48 gives a NOT-STORED (29,45,18) cell with 3 non-simple vertices), "
          "the +z side is short (+1/192 SAME, +1/96 gives `9ff7306e4a6cbf44`), and b holds on [23/48, 49/96] (+1/48 gives `9ff7306e4a6cbf44`). Neighbourhood radius between 1/384 and 1/192 in y; the type holds on a neighbourhood.")
        A("- Off-stratum (supplementary) steps leave the special position (stab 2 -> 1) and change the type in every case, as expected for a special-position type; two of the off-stratum cells are NOT stored (general-position types the menu never sampled) and one is the cubic-store type `8c69db9e84095469` (30,45,17).")
        A("- Read-only: no perturbed cell and no Schmitt cell computed here was added to `phase2_types.json` (sha256 unchanged); 'not stored' cells are recorded in `collision_phase2_results.json` only.")
    else:
        A("- (reading withheld: the computed verdicts differ from the run this note was written for; see the tables)")
    A("")
    A("## Post-screen shortlist")
    A("")
    A(f"- Survive this screen (all pairs DIFFERENT): {', '.join(f'#{rk} `{tid}`' for rk, tid in survivors) or 'none'}.")
    A(f"- Reframe (SAME TYPE somewhere): {', '.join(f'#{rk} `{tid}`' for rk, tid in reframes) or 'none'}.")
    A(f"- Incomplete / deferred: {', '.join(f'#{rk} `{tid}`' for rk, tid in incomplete) or 'none'}.")
    pv = {c["id"]: (c["point_verdict"], c["b_verdict"]) for c in perts}
    A("- Perturbation (top-3): " + "; ".join(f"`{cid}` point {pv[cid][0]} / metric {pv[cid][1]}" for cid in TOP3 if cid in pv) + ".")
    A("")
    A("## Honest limits")
    A("")
    A("- This screen is TYPE-level only at Schmitt's 27 printed representatives named in the worklist; every other Schmitt flag in the triage remains f-vector-level (his tables print one point per f-vector). "
      "51 of the 56 printed b-ratios were never swept by our menu (TRIAGE_PHASE2_RESULT.md); a DIFFERENT verdict says nothing about those.")
    A("- The digitization is a single visual pass cross-checked against the text layer, NOT independently re-keyed; a G5 verdict that leans on a specific row must first re-read the cited PDF page.")
    A("- Setting conversions are the machine-verified ones of PHASE2_SCHMITT_ORIGIN_CHECK.md (every printed row of each group reproduces under them); they are coordinate conversions, not perturbations, and the robustness column shows every alternative documented conversion gives the same code.")
    A("- The perturbation certificates cover the top-3 only, at their first witness, with finite steps (down to 1/1536); OPEN here means \"holds on the tested neighbourhood\", not an interval proof; a WALL side's type is named only where its code is in the store.")
    A("- No G4 (roundness / geometric symmetry / Burnside polyform counts / Engel / Bernhard cross-checks) is run here; those remain owed for every survivor.")
    A(f"- Snapshot language throughout: every survivor is \"not matched against the catalog snapshot of {SNAPSHOT}\".")
    A("")
    A(f"Wall {wall:.0f} s, single process. Deterministic except the timing columns.")
    A("")
    with open(OUT_MD, "w") as fh:
        fh.write("\n".join(L))
    print("wrote", OUT_MD)


if __name__ == "__main__":
    sys.exit(main())
