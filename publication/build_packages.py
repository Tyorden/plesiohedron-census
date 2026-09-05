#!/usr/bin/env python
"""build_packages.py — publication packager for the seven MINT finalists.

Builds, per finalist, publication/<id8>_<name-or-desc>/:
  COORDS.md            exact generating data + exact vertex coordinates (Fractions)
  render.png           matplotlib 3D render, faces colored by gon count
                       (p-vector ASSERTED against the store before rendering)
  g4_tables_<id>.json  copied verbatim from the banked harness artifact
  g4_tables_<id>.txt   copied verbatim (full-ops enumerator input)
  g4_tables_<id>_proper.txt  exported from the banked json (proper_ops)
  counts.md            fixed / free / one-sided counts, n as far as the cap allowed
plus (four publishable-now shapes only) oeis_draft_{fixed,free,onesided}.txt and
oeis_afile.txt, and top-level publication/ROUNDNESS.md.

Sources of truth (verify-not-guess): harness/phase1_types.json (witness, f, p,
aut, canonical code — every derivation below is asserted against it),
harness/g4_tables_<id>.json (banked, byte-copied), harness/G4_RESULTS.md
(accepted n<=4 counts — asserted equal to fresh enumerator prefixes).
Numbers printed into the packages are computed HERE from those inputs, with
assertions; nothing is transcribed by hand except the banked-doc citations.

Every count re-derivation runs the BANKED workflow (export_tables.py + the
compiled enumerate binary published as the A398957 a-file). Per-shape cap for
the n<=6 extension: 15 minutes; on timeout the run falls back to n=5, then to
the banked n<=4 (recorded, never silent).

Roundness (Bernhard's metric, arXiv:2604.07160 p. 6): V(cell) / V(outer
circumsphere), outer circumsphere = the site-centered sphere through the
farthest vertices (radius^2 = rho2, exact, from clip_cell). The Josehedron
control must reproduce his printed ~47.98%.

Run: python3 build_packages.py
Deterministic except wall-clock notes. Exit 0 iff all assertions pass.
"""
import json
import math
import os
import shutil
import subprocess
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
HARNESS = os.path.join(PROJ, "harness")
sys.path.insert(0, HARNESS)

import orbit                                    # noqa: E402
from exact_cell import clip_cell                # noqa: E402
from canon_code import canonical_code           # noqa: E402

import matplotlib                               # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                 # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

PYTHON = "python3"
BANKED_SCRIPTS = os.path.join(PROJ, "..", "SCI_OEIS_josehedron", "scripts")
EXPORT_TABLES = os.path.join(BANKED_SCRIPTS, "export_tables.py")
ENUM_BIN = os.path.join(BANKED_SCRIPTS, "enumerate")
BURNSIDE = os.path.join(PROJ, "..", "POLYFORMS_II_sphenoid_josehedron",
                        "burnside_generic.py")
STORE = os.path.join(HARNESS, "phase1_types.json")

SNAPSHOT = ("not matched against the records checked as of 2026-09-01 "
            "(Schmitt 2016 printed cubic tables incl. exact recomputation at "
            "every printed representative point, Bernhard 2026 printed cell "
            "data, classical space-filler lists)")

CAP_S = 15 * 60          # per-shape enumerator-extension cap (tasking)
BURNSIDE_CAP_S = 600     # optional n<=6 Burnside attempt cap
BURNSIDE_MAX_FIXED6 = 1_500_000   # attempt Burnside n<=6 only below this

# The seven finalists.  Names per Tyler's greenlit naming decision
# (NAMING_DECISION_BRIEF_2026-09-01.md, option A executed with personal names);
# G4 metadata cited from harness/G4_RESULTS.md (accepted); status per
# STATUS.md 2026-09-01 (cross-group batch accepted).
FINALISTS = [
    dict(cid="8cf50403cf88c455", dirname="8cf50403_Satchelhedron",
         name="Satchelhedron", status="PUBLISHABLE-NOW",
         desc="the IT(220) I-43d pentagon-dominant 11-facet cell",
         stab_geo=2, oeis=True,
         chirality=("amphichiral as a combinatorial map (aut 4, 2 improper "
                    "map symmetries) but geometric stabilizer order 2 — a "
                    "combinatorial-vs-geometric symmetry gap (G4/V2)")),
    dict(cid="2de0a21129cabe90", dirname="2de0a211_Ordenhedron",
         name="Ordenhedron", status="PUBLISHABLE-NOW",
         desc="the IT(201) Pn-3 fully asymmetric cell",
         stab_geo=1, oeis=True,
         chirality=("fully asymmetric: site symmetry = geometric stabilizer "
                    "= combinatorial aut = 1 (trivial); the cell has NO "
                    "symmetry of its own yet tiles under |ops|=24")),
    dict(cid="c4ea3f32fdd6dc51", dirname="c4ea3f32_Pn3m_11facet",
         name="the Pn-3m 11-facet cell", status="PUBLISHABLE-NOW (name pending Tyler)",
         desc="descriptive name pending Tyler's choice",
         stab_geo=2, oeis=True,
         chirality="site = stab_geo = aut = 2; achiral honeycomb (24 improper ops)"),
    dict(cid="f98a3ee5675fc121", dirname="f98a3ee5_Pn3m_7facet",
         name="the Pn-3m 7-facet cell", status="PUBLISHABLE-NOW (name pending Tyler)",
         desc="descriptive name pending Tyler's choice",
         stab_geo=1, oeis=True,
         chirality=("site = stab_geo = 1 < aut = 4 — combinatorial-vs-"
                    "geometric symmetry gap (G4/V2); achiral honeycomb")),
    dict(cid="ceb70631e274e727", dirname="ceb70631_IT212_37-57-22_HELD",
         name="the IT(212) (37,57,22) cell", status="HELD (Engel/Koch ILL check)",
         desc="mined-group finalist; NOT to be named before the ILL check",
         stab_geo=3, oeis=False,
         chirality=("CHIRAL honeycomb: all 24 honeycomb ops proper; site = "
                    "stab_geo = aut = 3")),
    dict(cid="359beee832567a71", dirname="359beee8_IT230_40-61-23_HELD",
         name="the IT(230) (40,61,23) cell", status="HELD (Engel/Koch ILL check)",
         desc="mined-group finalist; NOT to be named before the ILL check",
         stab_geo=2, oeis=False, view=(22, 118),  # show the 20-gon (faces azim 135)
         chirality=("site = stab_geo = 2 < aut = 4 — combinatorial-vs-"
                    "geometric symmetry gap (G4/V2); p-vector carries two "
                    "11-gons and a 20-gon")),
    dict(cid="aa6b0077c3234d24", dirname="aa6b0077_IT214_30-47-19_HELD",
         name="the IT(214) (30,47,19) cell", status="HELD (Engel/Koch ILL check)",
         desc="mined-group finalist; NOT to be named before the ILL check",
         stab_geo=2, oeis=False,
         chirality=("CHIRAL honeycomb: all 24 honeycomb ops proper; site = "
                    "stab_geo = aut = 2")),
]

# Banked n<=4 counts from harness/G4_RESULTS.md (accepted 2026-08-30) —
# asserted below against fresh enumerator prefixes.
G4_BANKED = {
    "ceb70631e274e727": dict(fixed=[8, 88, 1384, 25064], free=[1, 5, 59, 1065]),
    "359beee832567a71": dict(fixed=[24, 276, 5096, 111732], free=[1, 7, 112, 2349]),
    "8cf50403cf88c455": dict(fixed=[12, 66, 524, 4866], free=[1, 4, 25, 209]),
    "aa6b0077c3234d24": dict(fixed=[12, 114, 1588, 25734], free=[1, 8, 72, 1118]),
    "2de0a21129cabe90": dict(fixed=[24, 180, 1992, 25974], free=[1, 9, 85, 1099]),
    "c4ea3f32fdd6dc51": dict(fixed=[24, 132, 1048, 9630], free=[1, 6, 25, 225]),
    "f98a3ee5675fc121": dict(fixed=[48, 168, 912, 5748], free=[1, 7, 19, 135]),
}

# Josehedron control (roundness): generating orbit verbatim from
# harness/g0_regression.py / MATHAI_2026/paper/make_figs.py (Bernhard Table 4
# minima, BASE mod 8).  Bernhard prints ~47.98% (arXiv:2604.07160 p. 6).
JOSE_BASE = [(0, 2, 3), (0, 6, 1), (1, 0, 6), (2, 3, 0), (2, 5, 4), (3, 0, 2),
             (4, 2, 5), (4, 6, 7), (5, 4, 2), (6, 1, 0), (6, 7, 4), (7, 4, 6)]
JOSE_PERIOD = 8
BERNHARD_PCT = 47.98

# Okabe-Ito-first CVD-aware hues by gon count; identity also carried by the
# legend text, never by color alone (make_figs.py pattern, extended).
FACE_COLOR = {3: "#0072B2", 4: "#E69F00", 5: "#009E73", 6: "#CC79A7",
              7: "#56B4E9", 10: "#D55E00", 11: "#F0E442", 12: "#999999",
              20: "#882255"}
FACE_NAME = {3: "triangles", 4: "quadrilaterals", 5: "pentagons",
             6: "hexagons", 7: "heptagons", 10: "10-gons", 11: "11-gons",
             12: "12-gons", 20: "20-gons"}


def pvec_compact(pv):
    from collections import Counter
    return " ".join(f"{k}^{m}" for k, m in sorted(Counter(pv).items()))


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


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


def rederive(ent):
    """Witness -> orbit -> exact cell; assert store agreement (V0 pattern)."""
    w = ent["first_witness"]
    groups = orbit.load_groups()
    p = tuple(F(s) for s in w["point"])
    ob = orbit.orbit(groups[w["group"]], p)
    assert ob["stabilizer_order"] == w["stabilizer_order"]
    assert ob["n_conventional"] == w["orbit_conventional"]
    assert ob["n_primitive"] == w["orbit_primitive"]
    pts, period = orbit.scale_orbit(ob["points"])
    ec = clip_cell(pts[0], pts, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2
    code, aut = canonical_code(ec["facet_cycles"])
    assert code.decode("ascii") == ent["canon_code"], "canonical code MISMATCH"
    Vv = ec["n_vertices"]
    Ee = sum(len(c) for c in ec["facet_cycles"]) // 2
    assert [Vv, Ee, ec["facet_count"]] == list(ent["f_vector"])
    assert list(ec["p_vector"]) == list(ent["p_vector"])
    assert aut == ent["aut_order"]
    return dict(w=w, ob=ob, pts=pts, period=period, ec=ec, aut=aut,
                vol=cell_volume(ec))


def roundness(ec, vol):
    """Bernhard's metric: V(cell)/V(site-centered outer circumsphere)."""
    rho = math.sqrt(float(ec["rho2"]))
    return float(vol) / (4.0/3.0 * math.pi * rho**3)


def render(shape, ent, ctx, out_png):
    ec = ctx["ec"]
    # ASSERT the p-vector against the store before rendering (tasking rule)
    assert list(ec["p_vector"]) == list(ent["p_vector"]), "p-vector drift"
    c = ec["center"]
    verts = [tuple(float(v[k]-c[k]) for k in range(3)) for v in ec["vertices"]]
    rad = max(sum(x*x for x in v) for v in verts) ** 0.5
    verts = [tuple(x/rad for x in v) for v in verts]
    gons = sorted({len(cyc) for cyc in ec["facet_cycles"]})
    fig = plt.figure(figsize=(5.2, 5.2))
    ax = fig.add_subplot(projection="3d")
    for cyc in sorted(ec["facet_cycles"], key=len):
        poly = [verts[i] for i in cyc]
        ax.add_collection3d(Poly3DCollection(
            [poly], facecolors=FACE_COLOR[len(cyc)], edgecolors="#222222",
            linewidths=0.7, alpha=1.0))
    ax.set_xlim(-0.72, 0.72); ax.set_ylim(-0.72, 0.72); ax.set_zlim(-0.72, 0.72)
    ax.set_box_aspect((1, 1, 1))
    elev, azim = shape.get("view", (16, -54))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    w = ctx["w"]
    ax.set_title(f"{shape['name']}\nIT({w['group']}) {w['group_symbol']}, "
                 f"f={tuple(ent['f_vector'])}, {pvec_compact(ec['p_vector'])}, "
                 f"aut {ent['aut_order']}", fontsize=10)
    handles = [plt.Rectangle((0, 0), 1, 1, fc=FACE_COLOR[g], ec="#222222",
                             label=FACE_NAME[g]) for g in gons]
    fig.legend(handles=handles, loc="lower center", ncol=min(len(gons), 5),
               frameon=False, fontsize=8)
    fig.subplots_adjust(left=0, right=1, top=0.92, bottom=0.05)
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close(fig)


def run_enum(txt, n, timeout):
    r = subprocess.run([ENUM_BIN, txt, str(n)], check=True,
                       capture_output=True, text=True, timeout=timeout)
    counts, hdr = {}, False
    for line in r.stdout.splitlines():
        if line.strip() == "n fixed free":
            hdr = True
            continue
        if hdr and line.split():
            nn, fx, fr = line.split()
            counts[int(nn)] = (int(fx), int(fr))
    assert len(counts) == n
    return counts


def enum_with_cap(txt, cap_deadline):
    """Try n<=6, fall back n<=5, then n<=4.  Returns (counts, nmax, note)."""
    for n in (6, 5, 4):
        left = cap_deadline - time.time()
        if left <= 5:
            return None, 0, "cap exhausted before any run completed"
        try:
            return run_enum(txt, n, left), n, ""
        except subprocess.TimeoutExpired:
            continue
    return None, 0, "unreachable"


def write_coords(shape, ent, ctx, g4, path):
    w, ec = ctx["w"], ctx["ec"]
    L = []
    L.append(f"# {shape['name']} — exact generating data and coordinates")
    L.append("")
    L.append(f"Type id `{shape['cid']}` · status: **{shape['status']}** · "
             f"{shape['desc']}.")
    L.append("")
    L.append("All numbers below are recomputed from the banked witness "
             "(`harness/phase1_types.json`) through the G0/G2-validated exact "
             "pipeline at build time and asserted against the stored "
             "canonical code, f-vector, p-vector and aut order; certificate "
             "values cite `harness/G4_RESULTS.md` (accepted 2026-08-30) and "
             f"the banked `g4_tables_{shape['cid']}.json`.")
    L.append("")
    L.append("## Generating data")
    L.append("")
    L.append(f"- Space group: IT({w['group']}) = {w['group_symbol']} "
             f"(frozen G1 `spacegroups.json`, origin choice 1 for two-origin "
             f"groups)")
    kind = ("special position (Wyckoff stratum dimension "
            f"{w['stratum_dim']}, site-symmetry order {w['stabilizer_order']})"
            if w["kind"] == "special" else
            "general position (trivial site symmetry)")
    L.append(f"- Generating point (fractional): "
             f"({', '.join(w['point'])}) — {kind}")
    L.append(f"- Orbit: {w['orbit_conventional']} points per conventional "
             f"cell, T = {w['orbit_primitive']} translation classes "
             f"(primitive)")
    L.append(f"- Integer scaling: PERIOD = {ctx['period']} (orbit cleared to "
             f"integer triples mod PERIOD)")
    L.append(f"- Primitive lattice basis (columns, integer, from banked "
             f"tables): {g4['lattice_basis']} with |det| = {g4['detL']}")
    L.append(f"- Exact cell volume: {g4['cell_volume']} "
             f"(T x vol = detL certified in G4/V1)")
    L.append("")
    L.append("## Combinatorics and symmetry")
    L.append("")
    fv = tuple(ent["f_vector"])
    L.append(f"- f-vector (V, E, F): {fv}")
    L.append(f"- p-vector: {pvec_compact(ec['p_vector'])}")
    L.append(f"- Combinatorial automorphism order: {ent['aut_order']} "
             f"(canonical code)")
    L.append(f"- Site symmetry order: {w['stabilizer_order']}; geometric "
             f"stabilizer order: {shape['stab_geo']} (over ALL orthogonal "
             f"maps, G4/V2)")
    L.append(f"- Honeycomb point ops mod lattice: |ops| = "
             f"{g4['n_proper'] + g4['n_improper']} ({g4['n_proper']} proper, "
             f"{g4['n_improper']} improper)")
    L.append(f"- Chirality status: {shape['chirality']}")
    L.append(f"- Non-simple vertices: {w['nonsimple_vertices']} (flagged per "
             f"design; not an error)")
    L.append("")
    L.append("## Certification (banked, accepted)")
    L.append("")
    L.append("G4 ladder V0–V3 ALL PASS in exact rational arithmetic "
             "(`harness/G4_RESULTS.md`): exact re-derivation; tiling "
             "certificate (full-facet 1:1 pairing of all T*F slots, "
             "T x vol = detL, exhaustive 2rho-ball disjointness) verified "
             "twice — generator + an independent adapted audit sharing no "
             "geometry code; symmetry over all orthogonal maps; Burnside "
             "identity on the polyform counts (n <= 4). free(1) = 1: the ops "
             "act transitively on the T cell types (plesiohedral quotient).")
    L.append("")
    L.append(f"Diligence status: {SNAPSHOT}. Survival of every printed "
             "representative is evidence, not proof of novelty (Schmitt's "
             "survey is a grid sampling printing one representative per "
             "(group, f-vector)); see `harness/CROSS_GROUP_RESULTS.md` and "
             "`G5_DILIGENCE_2026-08-30.md`.")
    L.append("")
    L.append(f"## Scaled generating orbit (integer, mod {ctx['period']})")
    L.append("")
    L.append("```")
    for q in ctx["pts"]:
        L.append(f"({q[0]}, {q[1]}, {q[2]})")
    L.append("```")
    L.append("")
    L.append(f"## Exact vertex coordinates of one cell (site "
             f"({ctx['pts'][0][0]}, {ctx['pts'][0][1]}, {ctx['pts'][0][2]}), "
             f"same integer scaling)")
    L.append("")
    L.append(f"{ec['n_vertices']} vertices (exact Fractions), followed by the "
             f"{ec['facet_count']} facet cycles (vertex indices, CCW from "
             f"outside) and each facet's neighbor site.")
    L.append("")
    L.append("```")
    for i, v in enumerate(ec["vertices"]):
        L.append(f"v{i}: ({v[0]}, {v[1]}, {v[2]})")
    L.append("")
    for cyc, nbr in zip(ec["facet_cycles"], ec["neighbors"]):
        L.append(f"facet {len(cyc)}-gon {cyc}  neighbor site {nbr}")
    L.append("```")
    L.append("")
    open(path, "w").write("\n".join(L) + "\n")


def write_counts(shape, res_full, res_proper, burnside_note, path):
    counts, nmax, note = res_full
    pcounts, pnmax, pnote = res_proper
    L = [f"# {shape['name']} — polyform counts (banked enumerator workflow)",
         "",
         "Workflow: banked `export_tables.py` + the compiled `enumerate` "
         "binary (the A398957 a-file program) on the banked "
         f"`g4_tables_{shape['cid']}.json` (byte-copied here). Full-ops run "
         "gives fixed + free; proper-ops run gives fixed (identical column, "
         "asserted) + one-sided. n <= 4 prefixes asserted equal to the "
         "accepted G4 values (`harness/G4_RESULTS.md`). Per-shape extension "
         "cap 15 min.", ""]
    if nmax:
        L.append(f"| n | fixed | free | one-sided |")
        L.append("|---|---|---|---|")
        for n in range(1, nmax+1):
            os_v = pcounts[n][1] if (pcounts and n <= pnmax) else "—"
            L.append(f"| {n} | {counts[n][0]} | {counts[n][1]} | {os_v} |")
    L.append("")
    L.append(f"Full-ops run reached n <= {nmax}" + (f" ({note})" if note else "") +
             f"; proper-ops run reached n <= {pnmax}" +
             (f" ({pnote})" if pnote else "") + ".")
    L.append("")
    L.append("Consistency checks (this build): fixed columns of the two runs "
             "identical at every common n; fixed >= one-sided >= free and "
             "one-sided <= 2*free at every n (achiral count "
             "2*free - one-sided >= 0). Burnside identity: verified for "
             "n <= 4 in the accepted G4 run; " + burnside_note)
    L.append("")
    open(path, "w").write("\n".join(L) + "\n")


OEIS_VARIANTS = [
    ("fixed", "fixed", "counted up to lattice translation only"),
    ("onesided", "one-sided", "counted up to lattice translation and the "
     "proper (orientation-preserving) symmetries of the honeycomb"),
    ("free", "free", "counted up to the full point-symmetry group of the "
     "honeycomb (translations, rotations and improper maps)"),
]


def write_oeis(shape, ent, ctx, g4, res_full, res_proper, outdir):
    counts, nmax, _ = res_full
    pcounts, pnmax, _ = res_proper
    w = ctx["w"]
    fv = tuple(ent["f_vector"])
    pv = pvec_compact(ctx["ec"]["p_vector"])
    T = w["orbit_primitive"]
    nops = g4["n_proper"] + g4["n_improper"]
    nbrs = fv[2]
    art = "The" if shape["name"][0].isupper() else "the"
    shortname = shape["name"].replace("the ", "")
    an = "an" if str(fv[2]).startswith(("8", "11", "18")) else "a"
    defsent = (f"{art} {shortname} is {an} {fv[2]}-faced space-filling "
               f"polyhedron ({pv} faces) arising as the Voronoi cell of the "
               f"orbit of the point ({', '.join(w['point'])}) under space "
               f"group {w['group_symbol']} (IT {w['group']}); its honeycomb "
               f"has {T} cell types (translation classes), each cell with "
               f"{nbrs} face-neighbors.")
    cert = ("The tiling, its symmetry group (order "
            f"{nops} modulo lattice translations, {g4['n_proper']} proper) "
            "and the counts are certified in exact rational arithmetic: "
            "facet-pairing tiling certificate verified by two independent "
            "implementations, and the Burnside identity |G|*free(n) = "
            "Sum_g Fix_g(n) checked exactly for n <= 4.")
    dilig = (f"The cell's combinatorial type is {SNAPSHOT}; this is a "
             "diligence statement, not a proof of novelty.")
    disclose = ("Computed with the assistance of Claude (Anthropic); every "
                "count produced by the same published enumerator that "
                "generated A398957-A398959, with the exact-arithmetic "
                "verification above.")
    drafts = []
    for key, label, countdef in OEIS_VARIANTS:
        if key == "fixed":
            data = [counts[n][0] for n in range(1, nmax+1)]
        elif key == "free":
            data = [counts[n][1] for n in range(1, nmax+1)]
        else:
            data = [pcounts[n][1] for n in range(1, pnmax+1)]
        nn = len(data)
        L = [f"OEIS DRAFT (staged {time.strftime('%Y-%m-%d')} — NOT submitted; "
             "Tyler sequences submissions, see ../OEIS_DRAFTS_NOTE.md)",
             "",
             "%N (NAME — ends in a period)",
             f"Number of {label} polyforms of the {shortname} honeycomb "
             "with n cells.",
             "",
             "%O (OFFSET)",
             "1",
             "",
             f"%D (DATA, n = 1..{nn})",
             ", ".join(str(x) for x in data),
             "",
             "%C (COMMENTS — each paragraph pasted separately, signed with "
             "~~~~ so the OEIS editor auto-signs; do not type a name or date "
             "by hand)",
             defsent + f" Polyforms are face-connected clusters of cells, {countdef}.",
             cert,
             dilig,
             disclose + " - ~~~~",
             "",
             "%H (LINKS)",
             "Tyler Satchel Orden, <a href=\"/A______/a______.txt\">"
             "Honeycomb adjacency and symmetry tables, with the enumeration "
             "program and run instructions</a> [a-file: oeis_afile.txt in "
             "this folder]",
             "Mathias Bernhard, <a href=\"https://arxiv.org/abs/2604.07160\">"
             "The Josehedron</a>, arXiv:2604.07160 [math.MG], 2026 (method "
             "precedent; roundness benchmark).",
             "",
             "%o (PROG)",
             "(C++) // Redelmeier-style table-driven enumerator; see the "
             "a-file (same program as A398957).",
             "",
             "%K (KEYWORD)",
             "nonn",
             "",
             "%Y (CROSSREFS)",
             "Cf. A398957, A398958, A398959 (Josehedron polyforms, same "
             "enumerator); A385028, A397707-A397709 (polyforms on other "
             "space-filler honeycombs). [Cross-reference this shape's other "
             "two sequences once A-numbers exist.]",
             "",
             "%A (AUTHOR)",
             "Tyler Satchel Orden, [date auto-filled by ~~~~ in the editor]",
             "",
             "NOTE before submitting: (1) run the OEIS existence search on "
             "the terms; (2) replace the a-file placeholder with the "
             "assigned A-number; (3) per OEIS rule 17, host the program on "
             "the first assigned entry and cite it from the others; "
             "(4) b-file not needed at this term count (DATA line "
             "suffices).",
             ""]
        p = os.path.join(outdir, f"oeis_draft_{key}.txt")
        open(p, "w").write("\n".join(L))
        drafts.append(p)
    # a-file: tables + run instructions (both ops variants, one file)
    full_txt = open(os.path.join(outdir, f"g4_tables_{shape['cid']}.txt")).read()
    prop_txt = open(os.path.join(outdir,
                                 f"g4_tables_{shape['cid']}_proper.txt")).read()
    A = [f"a-file for the {shortname} polyform sequences (fixed / one-sided / "
         "free).",
         "",
         defsent,
         "",
         "Program: the table-driven Redelmeier enumerator published as the "
         "a-file of A398957 (enumerate.cpp).  Save a tables block below to "
         "tables.txt and run:  ./enumerate tables.txt N",
         "With TABLES-FULL the output columns are n, fixed, free.",
         "With TABLES-PROPER the 'free' column is the one-sided count "
         "(fixed column identical).",
         "",
         f"===== TABLES-FULL ({nops} ops) =====",
         full_txt.rstrip(),
         "===== END TABLES-FULL =====",
         "",
         f"===== TABLES-PROPER ({g4['n_proper']} proper ops) =====",
         prop_txt.rstrip(),
         "===== END TABLES-PROPER =====",
         ""]
    open(os.path.join(outdir, "oeis_afile.txt"), "w").write("\n".join(A))
    return drafts


def main():
    store = json.load(open(STORE))["types"]
    results = []
    roundness_rows = []

    # ---- Josehedron roundness control first
    fracs = [tuple(F(x, JOSE_PERIOD) for x in p) for p in JOSE_BASE]
    jpts, jP = orbit.scale_orbit(fracs)
    jec = clip_cell(jpts[0], jpts, jP)
    jcode, jaut = canonical_code(jec["facet_cycles"])
    assert jec["p_vector"] == (3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4) and jaut == 4
    jvol = cell_volume(jec)
    jr = roundness(jec, jvol)
    control_ok = abs(jr*100 - BERNHARD_PCT) < 0.005
    roundness_rows.append(("Josehedron (control, Bernhard 2026)", "220",
                           "(12,22,12)", jr, "control: printed ~47.98%"))
    print(f"CONTROL Josehedron roundness = {jr*100:.4f}% "
          f"(Bernhard prints ~{BERNHARD_PCT}%) -> "
          f"{'MATCH' if control_ok else 'MISMATCH'}")
    assert control_ok, "Josehedron roundness control failed"

    for shape in FINALISTS:
        cid = shape["cid"]
        t0 = time.time()
        ent = store[cid]
        outdir = os.path.join(HERE, shape["dirname"])
        os.makedirs(outdir, exist_ok=True)
        print(f"\n=== {shape['dirname']} ===")
        ctx = rederive(ent)
        print(f"  rederived: f={tuple(ent['f_vector'])} aut={ent['aut_order']} "
              f"OK ({time.time()-t0:.1f}s)")

        # banked tables copied verbatim + proper export
        src_json = os.path.join(HARNESS, f"g4_tables_{cid}.json")
        src_txt = os.path.join(HARNESS, f"g4_tables_{cid}.txt")
        shutil.copy2(src_json, outdir)
        shutil.copy2(src_txt, outdir)
        prop_txt = os.path.join(outdir, f"g4_tables_{cid}_proper.txt")
        subprocess.run([PYTHON, EXPORT_TABLES, src_json, prop_txt,
                        "proper_ops"], check=True, capture_output=True)
        g4 = json.load(open(src_json))
        assert F(g4["cell_volume"]) == ctx["vol"], "volume vs banked tables"

        # roundness
        r = roundness(ctx["ec"], ctx["vol"])
        beats = r*100 > BERNHARD_PCT
        roundness_rows.append((shape["name"], str(ctx["w"]["group"]),
                               str(tuple(ent["f_vector"])), r,
                               "BEATS 47.98% — flag" if beats else ""))
        print(f"  roundness = {r*100:.4f}%" +
              ("  *** BEATS Bernhard's 47.98% ***" if beats else ""))

        # coords + render
        write_coords(shape, ent, ctx, g4, os.path.join(outdir, "COORDS.md"))
        render(shape, ent, ctx, os.path.join(outdir, "render.png"))
        print("  COORDS.md + render.png written")

        # counts, capped
        deadline = time.time() + CAP_S
        res_full = enum_with_cap(os.path.join(outdir,
                                              f"g4_tables_{cid}.txt"), deadline)
        res_prop = enum_with_cap(prop_txt, deadline)
        counts, nmax, _ = res_full
        pcounts, pnmax, _ = res_prop
        assert counts is not None and nmax >= 4, "full-ops enum failed"
        assert pcounts is not None and pnmax >= 4, "proper-ops enum failed"
        b = G4_BANKED[cid]
        assert [counts[n][0] for n in range(1, 5)] == b["fixed"], \
            "fixed prefix != accepted G4"
        assert [counts[n][1] for n in range(1, 5)] == b["free"], \
            "free prefix != accepted G4"
        for n in range(1, min(nmax, pnmax)+1):
            assert pcounts[n][0] == counts[n][0], "fixed columns differ"
            assert counts[n][0] >= pcounts[n][1] >= counts[n][1] > 0
            assert pcounts[n][1] <= 2*counts[n][1], "one-sided > 2*free"
        print(f"  counts: full n<={nmax}, proper n<={pnmax}; "
              f"n<=4 == accepted G4; identities OK "
              f"({time.time()-t0:.1f}s elapsed)")

        # optional Burnside extension for small shapes
        burnnote = ("an independent Burnside/growth verification at n = 5, 6 "
                    "was NOT run in this build (counts at n = 5, 6 rest on "
                    "the single banked enumerator; the fixed column is "
                    "reproduced identically by the proper-ops run).")
        if nmax == 6 and counts[6][0] <= BURNSIDE_MAX_FIXED6:
            try:
                free_s = ",".join(str(counts[n][1]) for n in range(1, 7))
                fixed_s = ",".join(str(counts[n][0]) for n in range(1, 7))
                rb = subprocess.run(
                    [PYTHON, BURNSIDE, cid, src_json, "6", free_s, fixed_s],
                    capture_output=True, text=True, timeout=BURNSIDE_CAP_S)
                if rb.returncode == 0 and "ALL PASS" in rb.stdout:
                    burnnote = ("EXTENDED in this build: banked "
                                "burnside_generic.py (independent growth "
                                "enumeration) verified |G|*free(n) = "
                                "Sum Fix_g(n) with an independent fixed "
                                "recount for ALL n <= 6.")
                    print("  burnside n<=6: ALL PASS")
                else:
                    print("  burnside n<=6: not clean, recorded as not run")
            except subprocess.TimeoutExpired:
                print("  burnside n<=6: timeout, recorded as not run")
        write_counts(shape, res_full, res_prop, burnnote,
                     os.path.join(outdir, "counts.md"))

        drafts = []
        if shape["oeis"]:
            drafts = write_oeis(shape, ent, ctx, g4, res_full, res_prop,
                                outdir)
            print(f"  OEIS drafts: {len(drafts)}")
        results.append(dict(shape=shape, nmax=nmax, pnmax=pnmax,
                            counts=counts, pcounts=pcounts, r=r,
                            drafts=len(drafts), burn=burnnote))

    # ---- top-level ROUNDNESS.md
    L = ["# Roundness of the seven finalists (Bernhard's metric)",
         "",
         "Metric (Bernhard, arXiv:2604.07160, p. 6): the fraction of the "
         "volume of the cell's OUTER CIRCUMSPHERE filled by the cell, where "
         "the outer circumsphere is the site-centered sphere through the "
         "farthest vertices (radius^2 = the exact rho2 of the certified "
         "cell). Cell volumes are exact (banked, T x vol = detL certified); "
         "only the final division is floating point (reported to 4 "
         "decimals). Benchmark: Bernhard prints ~47.98% for the Josehedron "
         "and calls it the roundest space-filling polyhedron known to him "
         "(vs 47.75% rhombic dodecahedron / hexagonal prism).",
         "",
         "Control: the Josehedron through this exact pipeline reproduces "
         f"his printed value ({roundness_rows[0][3]*100:.4f}% vs ~47.98% "
         "printed); NOTE (2026-09-03): the control cannot discriminate the site-centered convention from the smallest-enclosing-sphere convention (its -4 site symmetry forces the two to coincide); see harness/round1_computations/RESULTS.md C4.",
         "",
         "| cell | IT | f-vector | V(cell)/V(circumsphere) | note |",
         "|---|---|---|---|---|"]
    for name, grp, fvs, r, note in roundness_rows:
        L.append(f"| {name} | {grp} | {fvs} | {r*100:.4f}% | {note} |")
    L.append("")
    beats_any = [row for row in roundness_rows[1:] if row[3]*100 > BERNHARD_PCT]
    if beats_any:
        L.append("**FLAG: finalist(s) above EXCEED Bernhard's 47.98% — on "
                 "the snapshot record (his metric, his benchmark) that would "
                 "be a new roundness record. Verify before any wording.**")
    else:
        L.append("No finalist beats Bernhard's 47.98% on his metric; the "
                 "Josehedron's roundness record stands on the snapshot "
                 "record. (Several finalists are heavier-faceted cells; the "
                 "record was a hook, not an expectation.)")
    L.append("")
    L.append("Convention note: for a cell with trivial geometric symmetry "
             "(e.g. the Ordenhedron) a smallest-enclosing sphere not "
             "centered at the site could be smaller than the site-centered "
             "circumsphere, which would only RAISE that cell's ratio; the "
             "site-centered convention above is the one the Josehedron "
             "control cannot validate (see the 2026-09-03 note); both conventions are tabulated in harness/round1_computations/RESULTS.md C4.")
    L.append("")
    L.append(f"Generated by publication/build_packages.py, "
             f"{time.strftime('%Y-%m-%d')}; deterministic.")
    open(os.path.join(HERE, "ROUNDNESS.md"), "w").write("\n".join(L) + "\n")

    # machine-readable summary for the status docs
    summary = dict(
        roundness={name: round(r*100, 4) for name, _, _, r, _ in
                   roundness_rows},
        counts={res["shape"]["cid"]: dict(
            nmax=res["nmax"], pnmax=res["pnmax"],
            fixed=[res["counts"][n][0] for n in range(1, res["nmax"]+1)],
            free=[res["counts"][n][1] for n in range(1, res["nmax"]+1)],
            onesided=[res["pcounts"][n][1] for n in range(1, res["pnmax"]+1)],
            burnside=res["burn"].split(":")[0],
            drafts=res["drafts"]) for res in results})
    json.dump(summary, open(os.path.join(HERE, "build_summary.json"), "w"),
              indent=1)
    print("\nALL PACKAGES BUILT — ROUNDNESS.md + build_summary.json written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
