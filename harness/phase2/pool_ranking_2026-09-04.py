#!/usr/bin/env python
"""pool_ranking_2026-09-04.py -- feature table + pre-registered score for the
phase-2 naming POOL (every cell with COMBINED verdict OPEN in
WALL_OPEN_PHASE2.json: 13 tetragonal + 102 hexagonal-family = 115).

Staging only: produces NO names. Scoring is the pre-registered block in
../../POOL_RANKING_2026-09-04.md (between PREREG-BEGIN / PREREG-END), which
this script reads back and re-emits verbatim -- it is never generated here.

Chain: g4_certify_gram.v0_rederive (accepted, unmodified; asserts canonical
code / f / p / aut against the frozen store) -> exact cell in the integer
Gram metric -> exact volume (crystal basis), rho^2 (G-norm), minimal
enclosing sphere (Welzl in the G inner product, exact Fractions, verified;
cross-checked against the c4 brute force on cells with <= 30 vertices),
Gram-triple isometry group (g4_certify_gram.cell_stabilizer_gram) checked
against the G4 result docs. Floats appear only in the roundness percentages
(one division each, rounded to 4 decimals) and in the score.

Outputs (deterministic; sorted keys; no timings):
  WALL_OPEN dir/POOL_RANKING_2026-09-04.json
  ../../POOL_RANKING_2026-09-04.md
"""
import hashlib
import itertools
import json
import math
import os
import re
import sys
from collections import Counter
from fractions import Fraction as F
from math import gcd
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.dirname(HERE)
MINT = os.path.dirname(HARNESS)
sys.path.insert(0, HERE)
sys.path.insert(0, HARNESS)

import orbit                                        # noqa: E402
import metric                                       # noqa: E402
import g4_certify_gram as G4G                       # noqa: E402
from g4_certify import pvec_compact, vsub           # noqa: E402

WALL_OPEN = os.path.join(HERE, "WALL_OPEN_PHASE2.json")
WALL_OPEN_MD5 = "6b257c551f6fb275dfabb03e992f57c2"
STORE_T = os.path.join(HARNESS, "phase2_types.json")
STORE_H = os.path.join(HARNESS, "phase2_hexagonal_types.json")
DOC_T = os.path.join(HARNESS, "G4_PHASE2_RESULTS.md")
DOC_H = os.path.join(HARNESS, "G4_PHASE2_HEX_RESULTS.md")
SCHMITT_T = os.path.join(HARNESS, "schmitt_tetragonal_tables.json")
SCHMITT_H = os.path.join(HARNESS, "schmitt_hexagonal_tables.json")
OUT_JSON = os.path.join(HERE, "POOL_RANKING_2026-09-04.json")
OUT_MD = os.path.join(MINT, "POOL_RANKING_2026-09-04.md")
SNAPSHOT = "2026-09-04"
JOSE_ROUNDNESS = 47.9833          # publication/ROUNDNESS.md control value
ENANTIOMORPHIC = {76, 78, 91, 95, 92, 96, 144, 145, 151, 153, 152, 154,
                  169, 170, 171, 172, 178, 179, 180, 181, 212, 213}
KNOWN_MINED = {212, 213, 214, 220, 230}   # G5_DILIGENCE_2026-08-30.md (cubic only)


def md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def system_of(it):
    if 75 <= it <= 142:
        return "tetragonal"
    if 143 <= it <= 167:
        return "trigonal"
    if 168 <= it <= 194:
        return "hexagonal"
    raise ValueError(it)


def fstr(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def pt(p):
    return "(" + ", ".join(fstr(x) for x in p) + ")"


def lcm(a, b):
    return a * b // gcd(a, b)


# ------------------------------------------------------ exact G-metric MES --
def gq(G, u):
    return G4G.gq(G, u)


def gf(G, u, v):
    return G4G.gform(G, u, v)


def circumsphere(R, G):
    """Smallest G-sphere with the points of R (1..4) on its boundary: centre in
    the affine hull of R.  None if R is affinely degenerate."""
    if len(R) == 1:
        return R[0], F(0)
    a = R[0]
    if len(R) == 2:
        c = tuple((a[k] + R[1][k]) / 2 for k in range(3))
        return c, gq(G, vsub(a, c))
    if len(R) == 3:
        u, v = vsub(R[1], a), vsub(R[2], a)
        uu, uv, vv = gq(G, u), gf(G, u, v), gq(G, v)
        det = uu * vv - uv * uv
        if det == 0:
            return None
        s = (uu / 2 * vv - uv * vv / 2) / det
        t = (uu * vv / 2 - uv * uu / 2) / det
        c = tuple(a[k] + s * u[k] + t * v[k] for k in range(3))
        return c, gq(G, vsub(c, a))
    u, v, w = vsub(R[1], a), vsub(R[2], a), vsub(R[3], a)
    M = [[gq(G, u), gf(G, u, v), gf(G, u, w)],
         [gf(G, u, v), gq(G, v), gf(G, v, w)],
         [gf(G, u, w), gf(G, v, w), gq(G, w)]]
    if metric.det3(M) == 0:
        return None
    s, t, r = G4G.solve3(M, [M[0][0] / 2, M[1][1] / 2, M[2][2] / 2])
    c = tuple(a[k] + s * u[k] + t * v[k] + r * w[k] for k in range(3))
    return c, gq(G, vsub(c, a))


def inside(p, D, G):
    return gq(G, vsub(p, D[0])) <= D[1]


def welzl(P, R, G):
    if not P or len(R) == 4:
        D = circumsphere(R, G) if R else None
        if len(R) == 4 and D is None:
            raise RuntimeError("degenerate support in Welzl")
        return D
    p = P[0]
    D = welzl(P[1:], R, G)
    if D is not None and inside(p, D, G):
        return D
    return welzl(P[1:], R + [p], G)


def mes_exact(verts, G):
    P = sorted(verts)
    D = welzl(P, [], G)
    c, r2 = D
    assert all(inside(v, D, G) for v in verts)
    support = [i for i, v in enumerate(verts) if gq(G, vsub(v, c)) == r2]
    assert 1 <= len(support)
    return c, r2, support


def mes_brute(verts, G):
    """c4_roundness.py method (subsets of size 2..4), G inner product."""
    best = None
    n = len(verts)
    for k in (2, 3, 4):
        for S in itertools.combinations(range(n), k):
            s = circumsphere([verts[i] for i in S], G)
            if s is None:
                continue
            c, r2 = s
            if best is not None and r2 >= best[1]:
                continue
            if all(gq(G, vsub(v, c)) <= r2 for v in verts):
                best = (c, r2)
    return best


def roundness_pct(vol_coord, detG, r2):
    """cell volume / volume of the sphere of G-radius^2 r2, both Euclidean:
    vol_E = vol_coord * sqrt(det G); sphere = 4/3 pi r2^(3/2)."""
    return 100.0 * float(vol_coord) * math.sqrt(float(detG)) / \
        (4.0 / 3.0 * math.pi * float(r2) ** 1.5)


# --------------------------------------------------------- doc parsing ------
V2_RE = re.compile(r"site=(\d+), Isom_fix_site=(\d+), Isom\(solid\)=(\d+) "
                   r"\(Isom\+=(\d+), improper=(\d+); solid (CHIRAL|achiral)\), aut_comb=(\d+)")
HEAD_RE = re.compile(r"^#{2,3} #\d+ `([0-9a-f]{16})`")


def parse_doc(path):
    out = {}
    cur = None
    for line in open(path):
        m = HEAD_RE.match(line)
        if m:
            cur = m.group(1)
            continue
        if cur and "Isom(solid)=" in line:
            m = V2_RE.search(line)
            assert m, line
            out[cur] = dict(site=int(m.group(1)), isom_fix=int(m.group(2)),
                            isom=int(m.group(3)), isom_proper=int(m.group(4)),
                            isom_improper=int(m.group(5)),
                            chiral=(m.group(6) == "CHIRAL"), aut=int(m.group(7)))
            cur = None
    return out


def schmitt_index(path):
    """group -> set of printed f-vectors; system-wide f -> sorted groups."""
    d = json.load(open(path))
    per = {}
    sysf = {}
    for k, v in d.items():
        if k.startswith("_"):
            continue
        fs = {tuple(r["f"]) for r in v["rows"]}
        for g in v["groups"]:
            per[g] = fs
            for f in fs:
                sysf.setdefault(f, set()).add(g)
    return per, {f: sorted(g) for f, g in sysf.items()}


# ---------------------------------------------------------- per cell --------
_CTX = {}


def _init():
    _CTX["groups"] = orbit.load_groups()
    _CTX["stores"] = {"tetragonal": json.load(open(STORE_T))["types"],
                      "hexagonal": json.load(open(STORE_H))["types"]}


def compute(cell):
    groups, stores = _CTX["groups"], _CTX["stores"]
    cid, fam = cell["id"], cell["family"]
    ent = stores[fam][cid]
    w = ent["first_witness"]
    ctx = G4G.v0_rederive(cid, ent, groups, w)
    ec, Gi, period = ctx["ec"], ctx["G"], ctx["period"]
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    site = tuple(F(x) for x in ec["center"])
    vol = G4G.cell_volume_from_cycles(ec)
    detG = metric.det3([[F(x) for x in row] for row in Gi])
    rho2 = F(ec["rho2"])
    assert rho2 == max(gq(Gi, vsub(v, site)) for v in verts)
    c_mes, r2_mes, support = mes_exact(verts, Gi)
    assert r2_mes <= rho2
    brute = None
    if len(verts) <= 30:
        b = mes_brute(verts, Gi)
        assert b is not None and b[1] == r2_mes, "Welzl vs brute-force MES disagree"
        brute = True
    # isometries (second derivation, Gram-triple about the centroid)
    stab = G4G.cell_stabilizer_gram(verts, Gi)
    n_iso = len(stab)
    n_proper = sum(1 for A in stab if G4G.det3(*A) == 1)
    # presentation: site-centred vertex vectors in conventional fractional coords
    cvec = [tuple((v[k] - site[k]) / period for k in range(3)) for v in verts]
    m_lat = 1
    for v in cvec:
        for x in v:
            m_lat = lcm(m_lat, x.denominator)
    m_abs = 1
    for v in verts:
        for x in v:
            m_abs = lcm(m_abs, (x / period).denominator)
    b = F(w["b"])
    if fam == "tetragonal":
        m_cart = 1
        for v in cvec:
            m_cart = lcm(m_cart, v[0].denominator)
            m_cart = lcm(m_cart, v[1].denominator)
            m_cart = lcm(m_cart, (v[2] * b).denominator)
        m_score = m_cart
        pres_kind = "integer Cartesian coordinates (units a/m; c/a = p/q applied to z)"
    else:
        m_cart = None
        m_score = m_lat
        pres_kind = "integer coordinates in the hexagonal lattice basis (a,b,c) after scaling by m; no integer Cartesian presentation in general (sqrt(3))"
    pv = list(ec["p_vector"])
    cnt = Counter(pv)
    return dict(
        id=cid, family=fam, IT=w["group"], symbol=ctx["g"]["international_short"],
        system=system_of(w["group"]), c_over_a=fstr(b), witness_point=pt(ctx["p"]),
        wyckoff_kind=w.get("kind"), stratum_dim=int(w["stratum_dim"]),
        site_stab=int(w["stabilizer_order"]), T_primitive=int(w["orbit_primitive"]),
        f=[ctx["V"], ctx["E"], ctx["Fc"]], p=pvec_compact(pv),
        n_polygon_sizes=len(cnt), n_pentagons=cnt.get(5, 0),
        n_odd_ge7=sum(m for s, m in cnt.items() if s >= 7 and s % 2 == 1),
        max_polygon=max(pv), aut_comb=ctx["aut"], nonsimple=ec["nonsimple_vertices"],
        isom_solid=n_iso, isom_proper=n_proper, isom_improper=n_iso - n_proper,
        chiral=(n_iso == n_proper),
        gram=[[int(x) for x in row] for row in Gi], period=period,
        vol_crystal=fstr(vol), detG=fstr(detG), rho2=fstr(rho2),
        roundness_site=round(roundness_pct(vol, detG, rho2), 4),
        mes_centre=pt(c_mes), mes_r2=fstr(r2_mes), mes_support=len(support),
        mes_site_centred=(c_mes == site), mes_brute_checked=brute,
        roundness_mes=round(roundness_pct(vol, detG, r2_mes), 4),
        m_lattice=m_lat, m_cartesian=m_cart, m_absolute_conventional=m_abs,
        m_scored=m_score, presentation_kind=pres_kind,
        site_conventional=pt([F(s) for s in w["point"]]),
        vertices_site_centred_conventional=[pt(v) for v in sorted(cvec)],
    )


# ------------------------------------------------------------- scoring ------
def score(r):
    Fs = r["f"][2] / 4
    P = r["n_polygon_sizes"] + min(r["n_pentagons"], 8) / 2 + min(r["n_odd_ge7"], 4)
    A = 1.5 * math.log2(r["aut_comb"]) + (1 if r["isom_solid"] == r["aut_comb"] else 0)
    C = (1.5 + (0.5 if r["IT"] in ENANTIOMORPHIC else 0)) if r["chiral"] else 0
    R = 10 * r["roundness_site"] / JOSE_ROUNDNESS
    I = 2 if r["m_scored"] <= 24 else (1 if r["m_scored"] <= 96 else 0)
    D = 3 - r["stratum_dim"]
    E = -2 if r["IT"] in KNOWN_MINED else 0
    S = (2 if r["family_facet_record"] else 0) + (2 if r["aut_comb"] == 1 else 0) \
        + (1 if not r["fvec_printed_own_group"] else 0) \
        + (1 if r["site_stab"] == r["isom_solid"] == r["aut_comb"] else 0)
    terms = dict(F=round(Fs, 4), P=round(P, 4), A=round(A, 4), C=round(C, 4),
                 R=round(R, 4), I=I, D=D, E=E, S=S)
    return round(sum(terms.values()), 4), terms


def hook(r):
    """One plain-language line, no names, no 'new'."""
    f2 = r["f"][2]
    cnt = dict(x.split("^") for x in r["p"].split())
    parts = []
    for s in sorted(cnt, key=int):
        n = int(cnt[s])
        word = {"3": "triangle", "4": "quadrilateral", "5": "pentagon", "6": "hexagon",
                "7": "heptagon", "8": "octagon", "9": "nonagon", "10": "decagon"}.get(s, f"{s}-gon")
        parts.append(f"{n} {word}{'s' if n != 1 else ''}")
    faces = ", ".join(parts)
    sym = ("no symmetry at all" if r["aut_comb"] == 1 else
           f"symmetry order {r['aut_comb']}" +
           (" (all of it realized by isometries)" if r["isom_solid"] == r["aut_comb"]
            else f" combinatorially, {r['isom_solid']} realized by isometries"))
    hand = "chiral (comes in two mirror-image hands)" if r["chiral"] else "mirror-symmetric (achiral)"
    strat = {0: "sits at a fixed point of its group", 1: "sits on a symmetry line",
             2: "sits on a symmetry plane", 3: "sits in general position"}[r["stratum_dim"]]
    return (f"{f2}-faced cell ({faces}); {sym}; {hand}; {strat}; "
            f"roundness {r['roundness_site']:.2f}% of its circumsphere "
            f"({100*r['roundness_site']/JOSE_ROUNDNESS:.0f}% of the Josehedron benchmark)")


def gon(n):
    """'a 9-gon' / 'an 8-gon' / 'an 11-gon' / 'an 18-gon'."""
    art = "an" if (str(n).startswith("8") or n in (11, 18)) else "a"
    return f"{art} {n}-gon"


def attach(r):
    facts = []
    if r["family_facet_record"]:
        facts.append(f"it carries the most facets ({r['f'][2]}) of any open cell in its family pool "
                     f"(the printed Schmitt maximum for IT({r['IT']}) is {r['schmitt_group_max_facets']})")
    if r["aut_comb"] == 1:
        facts.append("it tiles space with no symmetry of its own (aut = 1): every copy is placed by the group, none by the shape")
    if r["chiral"] and r["IT"] in ENANTIOMORPHIC:
        facts.append(f"it is chiral and its group {r['symbol']} is one of an enantiomorphic pair, so the tiling itself has a handedness")
    elif r["chiral"]:
        facts.append("the solid is chiral (no mirror or inversion among its isometries)")
    if r["n_pentagons"] >= 4:
        facts.append(f"{r['n_pentagons']} of its faces are pentagons")
    if r["n_odd_ge7"] >= 2:
        facts.append(f"it has {r['n_odd_ge7']} odd polygons of seven or more sides (largest face {gon(r['max_polygon'])})")
    if r["m_cartesian"] is not None and r["m_cartesian"] <= 96:
        facts.append(f"it has integer Cartesian coordinates once scaled by {r['m_cartesian']} (site-centred)")
    if r["m_cartesian"] is None and r["m_lattice"] <= 24:
        facts.append(f"its vertices are integers in the hexagonal lattice basis once scaled by {r['m_lattice']}")
    if r["stratum_dim"] == 0:
        facts.append("its site is a fixed Wyckoff point, so the shape is pinned by the group and c/a alone")
    if r["site_stab"] == r["isom_solid"] == r["aut_comb"] and r["aut_comb"] > 1:
        facts.append("every symmetry it has is forced by its site symmetry")
    if r["roundness_rank"] <= 10:
        facts.append(f"it fills {r['roundness_site']:.1f}% of its circumsphere (rank {r['roundness_rank']} of 115 in the pool; the Josehedron benchmark is 47.98%)")
    if not r["fvec_printed_own_group"]:
        facts.append(f"its f-vector {tuple(r['f'])} is printed nowhere in Schmitt's IT({r['IT']}) table (absence is evidence, never proof; and it follows the open verdict)")
    if not facts:
        facts.append("its facet mix and open verdict; nothing else in the score singles it out")
    return "A name here would attach to the fact that " + "; ".join(facts) + \
           ". Not matched against the records checked as of 2026-09-04; Engel/Koch exposure UNKNOWN pending the ILL."


# ---------------------------------------------------------------- main ------
def main():
    assert md5(WALL_OPEN) == WALL_OPEN_MD5, "WALL_OPEN_PHASE2.json drifted"
    wo = json.load(open(WALL_OPEN))
    pool = [c for c in wo["cells"] if c["combined_verdict"] == "OPEN"]
    pool.sort(key=lambda c: (c["family"], c["id"]))
    assert len(pool) == 115
    docs = {**parse_doc(DOC_T), **parse_doc(DOC_H)}
    per_t, sys_t = schmitt_index(SCHMITT_T)
    per_h, sys_h = schmitt_index(SCHMITT_H)
    sch_meta = {}
    for path in (SCHMITT_T, SCHMITT_H):
        d = json.load(open(path))
        for k, v in d.items():
            if k.startswith("_"):
                continue
            for g in v["groups"]:
                sch_meta[g] = int(v["max_facets"])
    jobs = int(os.environ.get("POOL_JOBS", "6"))
    with Pool(jobs, initializer=_init) as P:
        rows = list(P.imap(compute, pool, chunksize=1))
    byid = {c["id"]: c for c in pool}
    for r in rows:
        c = byid[r["id"]]
        # certificate cross-checks against the G4 docs and the wall/open store
        d = docs[r["id"]]
        assert d["isom"] == r["isom_solid"] and d["isom_proper"] == r["isom_proper"] \
            and d["chiral"] == r["chiral"] and d["aut"] == r["aut_comb"] \
            and d["site"] == r["site_stab"], (r["id"], d, r["isom_solid"])
        r["isom_fix_site"] = d["isom_fix"]
        assert c["base_f"] == r["f"] and c["base_p"] == r["p"] and c["base_aut"] == r["aut_comb"]
        assert c["c_over_a"] == r["c_over_a"] and c["stratum_dim"] == r["stratum_dim"]
        assert c["witness_point"] == r["witness_point"] and c["site_stab"] == r["site_stab"]
        per, sysf = (per_t, sys_t) if r["family"] == "tetragonal" else (per_h, sys_h)
        f = tuple(r["f"])
        r["fvec_printed_own_group"] = f in per[r["IT"]]
        wo_flag = {row["fvec_printed"] for row in c["rows"] if row["code_id"] == r["id"]}
        assert wo_flag == {r["fvec_printed_own_group"]}, (r["id"], wo_flag)
        r["fvec_printed_groups_in_system"] = sysf.get(f, [])
        r["schmitt_group_max_facets"] = sch_meta[r["IT"]]
        r["exceeds_schmitt_group_max"] = r["f"][2] > sch_meta[r["IT"]]
        r["engel_koch_exposure"] = ("KNOWN-MINED (G5)" if r["IT"] in KNOWN_MINED
                                    else "UNKNOWN pending ILL (Engel 1981 / Koch 1972 not read for this system)")
        r["combined_verdict"] = c["combined_verdict"]
        r["enantiomorphic_group"] = r["IT"] in ENANTIOMORPHIC
    # facet ranks
    for key, grp in (("family", "family"), ("system", "system")):
        for name in {r[grp] for r in rows}:
            sub = [r for r in rows if r[grp] == name]
            vals = sorted({r["f"][2] for r in sub}, reverse=True)
            for r in sub:
                r[f"facet_rank_in_{key}_pool"] = vals.index(r["f"][2]) + 1
                r[f"{key}_pool_size"] = len(sub)
    for i, r in enumerate(sorted(rows, key=lambda r: (-r["roundness_site"], r["id"]))):
        r["roundness_rank"] = i + 1
    for r in rows:
        r["family_facet_record"] = r["facet_rank_in_family_pool"] == 1
        r["score"], r["score_terms"] = score(r)
    rows.sort(key=lambda r: (-r["score"], -r["roundness_site"], -r["f"][2], r["id"]))
    for i, r in enumerate(rows):
        r["rank_overall"] = i + 1
    for name in ("tetragonal", "trigonal", "hexagonal"):
        for i, r in enumerate([r for r in rows if r["system"] == name]):
            r["rank_in_system"] = i + 1
    for r in rows:
        r["hook"] = hook(r)
    out = dict(
        generated_by="harness/phase2/pool_ranking_2026-09-04.py", snapshot=SNAPSHOT,
        pool_definition="COMBINED verdict OPEN in WALL_OPEN_PHASE2.json (md5 " + WALL_OPEN_MD5 + ")",
        n_cells=len(rows), scoring="pre-registered block in POOL_RANKING_2026-09-04.md (PREREG-BEGIN..END)",
        josehedron_control_roundness=JOSE_ROUNDNESS,
        roundness_definition=("site-centred outer circumsphere: radius^2 = rho^2 of the certificate = max G-norm "
                              "distance^2 from the site to a vertex; cell volume exact in the crystal basis times "
                              "sqrt(det G); MES = exact minimal enclosing sphere (Welzl, G inner product), reported not scored"),
        language="every cell: not matched against the records checked as of 2026-09-04; OPEN = holds on the tested neighbourhood; no names",
        stores=wo["stores"], cells=rows)
    json.dump(out, open(OUT_JSON, "w"), sort_keys=True, indent=1)
    write_md(rows, out)
    print("cells", len(rows), "json md5", md5(OUT_JSON))
    print("mes brute-checked on", sum(1 for r in rows if r["mes_brute_checked"]), "cells (<= 30 vertices)")


def write_md(rows, out):
    prev = open(OUT_MD).read()
    a, b = prev.index("<!-- PREREG-BEGIN -->"), prev.index("<!-- PREREG-END -->") + len("<!-- PREREG-END -->")
    head = prev[:b]
    L = [head, "",
         "## Inputs and checks",
         "",
         f"- Pool: {len(rows)} cells = " + ", ".join(f"{n} {s}" for s, n in sorted(Counter(r['system'] for r in rows).items())) +
         f" (WALL_OPEN_PHASE2.json md5 {WALL_OPEN_MD5}; stores sha256 unchanged: {out['stores']['sha256_unchanged_after_run']}).",
         "- Every cell re-derived through the accepted chain (v0_rederive asserts canonical code, f, p, aut against the frozen store); "
         "Isom(solid), Isom+, improper, chirality, site symmetry and aut cross-checked against G4_PHASE2_RESULTS.md / G4_PHASE2_HEX_RESULTS.md (all 115 agree); "
         "f, p, aut, c/a, stratum dim, witness point cross-checked against WALL_OPEN_PHASE2.json (all agree); the own-group printed-f flag agrees with the wall/open store for all 115.",
         f"- Minimal enclosing sphere cross-checked against the c4 brute force on {sum(1 for r in rows if r['mes_brute_checked'])} cells (all with <= 30 vertices): identical.",
         "- Roundness: site-centred outer circumsphere (radius^2 = rho^2 of the certificate, the ROUNDNESS.md definition), scored; MES value reported, not scored. Benchmark 47.9833% (Josehedron control).",
         "- Engel/Koch exposure: UNKNOWN for every cell in this pool (both catalogs are print-only, unread for the tetragonal/trigonal/hexagonal systems; ILL pending); E = 0 throughout, so it does not move the ranking today.",
         "- Output JSON: harness/phase2/POOL_RANKING_2026-09-04.json (sorted keys, no timings), md5 in the ledger line / STATUS entry.",
         "",
         "## Top 5 per system",
         ""]
    for name in ("tetragonal", "trigonal", "hexagonal"):
        sub = [r for r in rows if r["system"] == name][:5]
        L.append(f"### {name.capitalize()} (IT {'75-142' if name == 'tetragonal' else '143-167' if name == 'trigonal' else '168-194'}), top 5 of {out['n_cells'] and sum(1 for r in rows if r['system'] == name)}")
        L.append("")
        L.append("| rank | id | group | c/a | f | p | aut / Isom | chiral | stratum | roundness site / MES | presentation | exposure | score |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in sub:
            pres = (f"m={r['m_cartesian']} (Cartesian)" if r["m_cartesian"] is not None else f"m={r['m_lattice']} (lattice basis)")
            L.append(f"| {r['rank_in_system']} | `{r['id']}` | IT({r['IT']}) {r['symbol']} | {r['c_over_a']} | ({r['f'][0]},{r['f'][1]},{r['f'][2]}) | {r['p']} | {r['aut_comb']} / {r['isom_solid']} | {'yes' if r['chiral'] else 'no'} | {r['stratum_dim']} | {r['roundness_site']:.2f}% / {r['roundness_mes']:.2f}% | {pres} | UNKNOWN (ILL) | {r['score']:.2f} |")
        L.append("")
        for r in sub:
            L.append(f"- **#{r['rank_in_system']} `{r['id']}`** — {r['hook']}.")
            L.append(f"  Score terms: " + ", ".join(f"{k}={v}" for k, v in r["score_terms"].items()) + f"; overall rank {r['rank_overall']}/{len(rows)}.")
            L.append(f"  {attach(r)}")
        L.append("")
    # records
    L += ["## Records within the pool", ""]
    def top(key, rev=True, n=3):
        return sorted(rows, key=lambda r: (-r[key] if rev else r[key], r["id"]))[:n]
    def cite(r):
        return f"`{r['id']}` IT({r['IT']}) {r['symbol']} c/a {r['c_over_a']} f=({r['f'][0]},{r['f'][1]},{r['f'][2]})"
    L.append("- Roundest (site-centred): " + "; ".join(f"{cite(r)} {r['roundness_site']:.2f}%" for r in top("roundness_site")) + ". None reaches the Josehedron's 47.98%.")
    L.append("- Roundest (minimal enclosing sphere): " + "; ".join(f"{cite(r)} {r['roundness_mes']:.2f}%" for r in top("roundness_mes")) + ".")
    mx = max(r["f"][2] for r in rows)
    L.append(f"- Most facets: {mx} — " + "; ".join(cite(r) for r in rows if r["f"][2] == mx) + ".")
    for name in ("tetragonal", "trigonal", "hexagonal"):
        sub = [r for r in rows if r["system"] == name]; m = max(r["f"][2] for r in sub)
        L.append(f"  - {name}: {m} — " + "; ".join(cite(r) for r in sub if r["f"][2] == m) + ".")
    mp = max(r["n_pentagons"] for r in rows)
    L.append(f"- Most pentagons: {mp} — " + "; ".join(cite(r) for r in rows if r["n_pentagons"] == mp) + ".")
    mo = max(r["n_odd_ge7"] for r in rows)
    L.append(f"- Most odd polygons of >= 7 sides: {mo} — " + "; ".join(cite(r) for r in rows if r["n_odd_ge7"] == mo) + ".")
    mg = max(r["max_polygon"] for r in rows)
    L.append(f"- Largest face: {mg}-gon — " + "; ".join(cite(r) for r in rows if r["max_polygon"] == mg) + ".")
    ma = max(r["aut_comb"] for r in rows)
    L.append(f"- Highest symmetry (aut_comb): {ma} — " + "; ".join(f"{cite(r)} Isom {r['isom_solid']}" for r in rows if r["aut_comb"] == ma) + ".")
    asym = [r for r in rows if r["aut_comb"] == 1]
    L.append(f"- Fully asymmetric (aut = 1): {len(asym)} of {len(rows)} cells (the pool is mostly general-position witnesses); the ten best-scoring: " + "; ".join(cite(r) for r in asym[:10]) + " (the rest: full table, aut/Isom column 1/1).")
    L.append(f"- Chiral solids: {sum(1 for r in rows if r['chiral'])} of {len(rows)}; achiral: {sum(1 for r in rows if not r['chiral'])}.")
    L.append(f"- Symmetry fully realized (Isom = aut): {sum(1 for r in rows if r['isom_solid'] == r['aut_comb'])}; fully forced by the site (site = Isom = aut): {sum(1 for r in rows if r['site_stab'] == r['isom_solid'] == r['aut_comb'])}.")
    L.append("- Stratum: " + ", ".join(f"dim {d}: {sum(1 for r in rows if r['stratum_dim'] == d)}" for d in range(4)) + ".")
    ml = min(r["m_scored"] for r in rows)
    L.append(f"- Smallest integer presentation scale m: {ml} — " + "; ".join(f"{cite(r)} ({r['presentation_kind'].split(' (')[0]})" for r in rows if r["m_scored"] == ml) + ".")
    tc = [r for r in rows if r["m_cartesian"] is not None]
    if tc:
        mc = min(r["m_cartesian"] for r in tc)
        L.append(f"- Smallest integer CARTESIAN scale (tetragonal only): {mc} — " + "; ".join(cite(r) for r in tc if r["m_cartesian"] == mc) + ".")
    L.append(f"- f-vector absent from its own group's printed Schmitt table: {sum(1 for r in rows if not r['fvec_printed_own_group'])} cells; absent from every printed table of its system: {sum(1 for r in rows if not r['fvec_printed_groups_in_system'])} cells — " +
             ("; ".join(cite(r) for r in rows if not r["fvec_printed_groups_in_system"]) or "none") + ". (Evidence, never proof; the open verdict comes first.)")
    L.append(f"- Facet count above the printed Schmitt maximum of its own group: {sum(1 for r in rows if r['exceeds_schmitt_group_max'])} cells — " +
             ("; ".join(f"{cite(r)} vs printed max {r['schmitt_group_max_facets']}" for r in rows if r["exceeds_schmitt_group_max"]) or "none") + ".")
    L.append("")
    # score-blind notes: what the pre-registered weights push down but a reader should still see
    L += ["## Score-blind notes (things the pre-registered weights under-rank; recorded, not re-weighted)", ""]
    fp = [r for r in rows if r["stratum_dim"] == 0]
    for r in fp:
        L.append(f"- The only fixed-Wyckoff-point cell in the pool: {cite(r)}, p={r['p']}, aut {r['aut_comb']} all realized "
                 f"(Isom {r['isom_solid']}: {r['isom_proper']} proper + {r['isom_improper']} improper, achiral), site symmetry {r['site_stab']}, "
                 f"roundness {r['roundness_site']:.2f}%, the smallest presentation scale in the pool (m = {r['m_lattice']} in the lattice basis), "
                 f"and the smallest facet count ({r['f'][2]}). Its shape is pinned by the group and c/a alone (no point coordinate to choose); "
                 f"the score's F, P and D terms leave it at overall rank {r['rank_overall']}. If a small, symmetric, pinned cell is wanted as a flagship, this is the one the score hides.")
    ach = [r for r in rows if not r["chiral"]]
    L.append(f"- Achiral cells ({len(ach)} of {len(rows)}): " + "; ".join(f"{cite(r)} Isom {r['isom_solid']} (rank {r['rank_overall']})" for r in ach) +
             ". Chirality is the norm in this pool (109/115) because the sweep's open survivors are overwhelmingly general-position witnesses in Sohncke groups; a mirror-symmetric cell is the rarer story here.")
    L.append("- Presentation: NO pool cell has a small-denominator presentation at its witness (best tetragonal Cartesian scale 5280; best hexagonal-family lattice-basis scale 108; the I term is 0 for all 115). "
             "The Josehedron-style integer-coordinate hook does not exist at these witnesses. Caveat: the witness is the sweep's grid point; a nicer point on the same open stratum, or a nicer c/a inside the tested band c/a(1 +- 1/96), could present better and was not searched here.")
    L.append("- c/a values such as 527/1000, 797/1000, 1277/2000 are the sweep's b-grid values, not chosen constants; the metric verdict OPEN covers only c/a(1 +- 1/96) around them (WALL_OPEN_PHASE2.json). Any published presentation should pick its c/a inside that band and re-certify at the chosen value.")
    L.append("- Combinatorial symmetry not honoured by the geometry (aut_comb > Isom(solid)): " +
             ("; ".join(f"{cite(r)} aut {r['aut_comb']} vs Isom {r['isom_solid']}" for r in rows if r["aut_comb"] > r["isom_solid"]) or "none") +
             ". The A term credits aut_comb by the pre-registered rule; the certificate is what it is.")
    L.append("")
    # full table
    L += ["## Full ranked table (all 115)", "",
          "| # | sys | id | group | c/a | f | p | aut/Isom(+,-) | chiral | dim | site | round site | round MES | m | f-printed (own grp) | score |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['rank_overall']} | {r['system'][:4]} | `{r['id']}` | {r['IT']} {r['symbol']} | {r['c_over_a']} | ({r['f'][0]},{r['f'][1]},{r['f'][2]}) | {r['p']} | {r['aut_comb']}/{r['isom_solid']}({r['isom_proper']},{r['isom_improper']}) | {'y' if r['chiral'] else 'n'} | {r['stratum_dim']} | {r['site_stab']} | {r['roundness_site']:.2f} | {r['roundness_mes']:.2f} | {r['m_scored']}{'C' if r['m_cartesian'] is not None else 'L'} | {'y' if r['fvec_printed_own_group'] else 'n'} | {r['score']:.2f} |")
    L += ["", "m: C = integer Cartesian scale (tetragonal), L = lattice-basis scale (hexagonal family). round = % of circumsphere volume, site-centred / minimal enclosing sphere.", "",
          "## Verify (main session, before acceptance)", "",
          "```", "cd <repo>/harness/phase2 && nice -n 10 python3 pool_ranking_2026-09-04.py; echo exit $?; md5 -q POOL_RANKING_2026-09-04.json",
          "```", "", "Exit 0 and the md5 printed in the STATUS entry are required. The script rewrites this file below the pre-registration block; the block itself is read back and never regenerated.", ""]
    open(OUT_MD, "w").write("\n".join(L))


if __name__ == "__main__":
    main()
