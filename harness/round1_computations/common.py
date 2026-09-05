"""Shared exact helpers for the round-1 computations (2026-09-03).
All arithmetic is fractions.Fraction; floats appear only in the final
roundness percentages of c4.  Reuses the frozen harness (orbit.py,
exact_cell.py, canon_code.py) unchanged."""
import os, sys, json
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.join(HERE, "..")
sys.path.insert(0, HARNESS)
import orbit                                   # noqa: E402
from exact_cell import clip_cell               # noqa: E402
from canon_code import canonical_code, rotation_system  # noqa: E402

STORE = json.load(open(os.path.join(HARNESS, "phase1_types.json")))
TYPES = STORE["types"]
GROUPS = orbit.load_groups()

CELLS = [  # (type id, label, short name)
    ("8cf50403cf88c455", "S",    "Satchelhedron"),
    ("2de0a21129cabe90", "O",    "Ordenhedron"),
    ("c4ea3f32fdd6dc51", "P11",  "Pn-3m 11-facet cell"),
    ("f98a3ee5675fc121", "P7",   "Pn-3m 7-facet cell"),
    ("ceb70631e274e727", "H212", "IT(212) (37,57,22) cell"),
    ("359beee832567a71", "H230", "IT(230) (40,61,23) cell"),
    ("aa6b0077c3234d24", "H214", "IT(214) (30,47,19) cell"),
]
PUB = os.path.join(HARNESS, "..", "publication")
PUBDIR = {"8cf50403cf88c455": "8cf50403_Satchelhedron", "2de0a21129cabe90": "2de0a211_Ordenhedron",
          "c4ea3f32fdd6dc51": "c4ea3f32_Pn3m_11facet", "f98a3ee5675fc121": "f98a3ee5_Pn3m_7facet",
          "ceb70631e274e727": "ceb70631_IT212_37-57-22_HELD", "359beee832567a71": "359beee8_IT230_40-61-23_HELD",
          "aa6b0077c3234d24": "aa6b0077_IT214_30-47-19_HELD"}


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def frac_str(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def pt_str(p):
    return "(" + ", ".join(frac_str(x) for x in p) + ")"


def pvec_compact(pv):
    from collections import Counter
    return " ".join(f"{k}^{m}" for k, m in sorted(Counter(pv).items()))


def exact_cell_at(group_no, p):
    """(group, fractional point) -> dict with orbit data, exact cell, code, aut, f, p."""
    g = GROUPS[group_no]
    p = tuple(F(x) for x in p)
    ob = orbit.orbit(g, p)
    pts, period = orbit.scale_orbit(ob["points"])
    # the site is the scaled image of p itself (clip about it, not about pts[0])
    site = tuple(int(x * period) % period for x in p)
    assert site in pts
    ec = clip_cell(site, pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2, "cutoff certificate violated"
    code, aut = canonical_code(ec["facet_cycles"])
    V = ec["n_vertices"]; Fc = ec["facet_count"]
    E = sum(len(c) for c in ec["facet_cycles"]) // 2
    assert V - E + Fc == 2
    return dict(group=group_no, point=p, ob=ob, pts=pts, period=period, ec=ec,
                code=code.decode("ascii"), aut=aut, f=(V, E, Fc),
                p=tuple(ec["p_vector"]), nonsimple=ec["nonsimple_vertices"],
                stab=ob["stabilizer_order"], T=ob["n_primitive"])


def cell_volume(ec):
    vs, c = ec["vertices"], ec["center"]
    six = F(0)
    for cyc in ec["facet_cycles"]:
        p0 = tuple(vs[cyc[0]][k]-c[k] for k in range(3))
        for t in range(1, len(cyc)-1):
            p1 = tuple(vs[cyc[t]][k]-c[k] for k in range(3))
            p2 = tuple(vs[cyc[t+1]][k]-c[k] for k in range(3))
            d = det3(p0, p1, p2)
            assert d > 0
            six += d
    return six / 6


def code_id(code_str):
    import hashlib
    return hashlib.sha1(code_str.encode("ascii")).hexdigest()[:16]


def rederive(cid):
    """Witness -> exact cell; assert agreement with the store (V0 pattern)."""
    ent = TYPES[cid]
    w = ent["first_witness"]
    r = exact_cell_at(w["group"], [F(s) for s in w["point"]])
    assert r["code"] == ent["canon_code"], "canonical code MISMATCH vs store"
    assert list(r["f"]) == list(ent["f_vector"]) and list(r["p"]) == list(ent["p_vector"])
    assert r["aut"] == ent["aut_order"] and r["stab"] == w["stabilizer_order"]
    return r
