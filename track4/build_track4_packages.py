#!/usr/bin/env python
"""build_track4_packages.py — OEIS draft packages for the Track-4 cells.

Input : track4_results.json (written by track4_certify.py; every number below
        is read from there, nothing hand-typed except literature citations),
        g4_tables_<cid>.{json,txt,_proper.txt}, independent_runs/*.json
        (verify_counts_independent.py output, if present).
Output: track4/<key>_<Name>/ with COORDS.md, counts.md, oeis_draft_{fixed,
        onesided,free}.txt, oeis_afile.txt, render.png; and per-cell asserts:
        counts prefixes == V3 counts, independent run (if present) == banked,
        fixed >= one-sided >= free, one-sided <= 2*free.

House format: publication/build_packages.py (write_oeis / a-file), adapted:
the cells are KNOWN (literature names + citations in NAME/COMMENTS), so the
snapshot/novelty sentence is replaced by an attribution sentence — the
sequences are new, the cells are not.  AI-disclosure sentence + ~~~~ kept.

Run: python3 build_track4_packages.py
"""
import json
import os
import shutil
import sys
import time
from collections import Counter
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "harness"))

import matplotlib                               # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                 # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

RES = json.load(open(os.path.join(HERE, "track4_results.json")))

SPEC = {
    "laves": dict(
        dirname="laves17_LavesGraphPlesiohedron", cid="laves17",
        shortname="Laves graph plesiohedron", article="The",
        # NAME-line noun; OEIS names end in a period
        oeis_name="Laves graph plesiohedron",
        name_genitive="the Laves graph plesiohedron",
        gen=("the Voronoi cell of the vertex set of the Laves graph (the srs "
             "net), i.e. of Wyckoff position 8a of space group I4_132 (IT 214), "
             "generating point (1/8, 1/8, 1/8), site symmetry .32"),
        known=("The cell is the well-known 17-faced plesiohedron of the Laves "
               "graph (Coxeter 1955; Schoen 2008); it is not new. Only the "
               "polyform sequences are new here."),
        links=[
            "H. S. M. Coxeter, <a href=\"https://doi.org/10.4153/CJM-1955-003-7\">"
            "On Laves' graph of girth ten</a>, Canad. J. Math. 7 (1955), 18-23.",
            "Alan H. Schoen, On the graph (10,3)-a, Notices Amer. Math. Soc. "
            "55 (2008), no. 6, 663.",
            "Wikipedia, <a href=\"https://en.wikipedia.org/wiki/Laves_graph\">"
            "Laves graph</a>.",
            "Moritz W. Schmitt, <a href=\"https://doi.org/10.17169/refubium-14374\">"
            "On Space Groups and Dirichlet-Voronoi Stereohedra</a>, "
            "dissertation, FU Berlin, 2016 (IT(214) table, f-vector (30,45,17) "
            "at (1/8,1/8,1/8)).",
        ]),
    "engel": dict(
        dirname="engel38_EngelStereohedron", cid="engel38",
        shortname="Engel 38-facet stereohedron", article="",
        oeis_name="Engel's 38-facet stereohedron",
        name_genitive="Engel's 38-facet stereohedron", view=(16, 126),
        gen=("the Voronoi cell of the orbit of the general-position point "
             "(427/6984, 761/6984, 1421/6984) under space group I4_132 "
             "(IT 214), the representative point printed by Schmitt (2016) "
             "for the f-vector (70,106,38) in that group"),
        known=("The cell is one of Engel's (1981) four combinatorial types of "
               "38-facet Dirichlet stereohedra in I4_132, the largest facet "
               "count observed for any plesiohedron (Schmitt 2016 confirms the "
               "four types and finds no fifth in a 145-group exact grid "
               "sampling); it is not new. Which of Engel's four types this "
               "printed representative realizes is not identified here. "
               "Only the polyform sequences are new."),
        links=[
            "Peter Engel, <a href=\"https://doi.org/10.1524/zkri.1981.154.3-4.199\">"
            "Über Wirkungsbereichsteilungen von kubischer Symmetrie</a>, "
            "Z. Kristallogr. 154 (1981), 199-215.",
            "Moritz W. Schmitt, <a href=\"https://doi.org/10.17169/refubium-14374\">"
            "On Space Groups and Dirichlet-Voronoi Stereohedra</a>, "
            "dissertation, FU Berlin, 2016 (IT(214) table, f-vector "
            "(70,106,38), generating point (427/6984, 761/6984, 1421/6984)).",
            "Wikipedia, <a href=\"https://en.wikipedia.org/wiki/Plesiohedron\">"
            "Plesiohedron</a>.",
        ]),
}

FACE_COLOR = {3: "#0072B2", 4: "#E69F00", 5: "#009E73", 6: "#CC79A7",
              7: "#56B4E9", 8: "#D55E00", 16: "#F0E442", 20: "#999999",
              28: "#882255"}

OEIS_VARIANTS = [
    ("fixed", "fixed", "counted up to lattice translation only"),
    ("onesided", "one-sided", "counted up to lattice translation and the "
     "proper (orientation-preserving) symmetries of the honeycomb"),
    ("free", "free", "counted up to the full point-symmetry group of the "
     "honeycomb (translations, rotations and improper maps)"),
]


def pvec_str(p):
    return p


def render(sp, r, out_png):
    verts = [tuple(float(F(x)) for x in v) for v in r["vertices"]]
    c = r["scaled_orbit"][0]
    verts = [tuple(v[k] - c[k] for k in range(3)) for v in verts]
    rad = max(sum(x*x for x in v) for v in verts) ** 0.5
    verts = [tuple(x / rad for x in v) for v in verts]
    gons = sorted({len(cyc) for cyc in r["facet_cycles"]})
    fig = plt.figure(figsize=(5.2, 5.2))
    ax = fig.add_subplot(projection="3d")
    for cyc in sorted(r["facet_cycles"], key=len):
        ax.add_collection3d(Poly3DCollection(
            [[verts[i] for i in cyc]], facecolors=FACE_COLOR[len(cyc)],
            edgecolors="#222222", linewidths=0.7, alpha=1.0))
    ax.set_xlim(-0.72, 0.72); ax.set_ylim(-0.72, 0.72); ax.set_zlim(-0.72, 0.72)
    ax.set_box_aspect((1, 1, 1))
    # Engel: thin wedge; (16,126) shows the 28-, 20- and 16-gon plus the slivers
    elev, azim = sp.get("view", (16, -54))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(f"{sp['shortname']}\nIT(214) I4_132, f={tuple(r['f_vector'])}, "
                 f"{r['p_vector']}, aut {r['aut']}", fontsize=10)
    handles = [plt.Rectangle((0, 0), 1, 1, fc=FACE_COLOR[g], ec="#222222",
                             label=f"{g}-gons") for g in gons]
    fig.legend(handles=handles, loc="lower center", ncol=min(len(gons), 5),
               frameon=False, fontsize=8)
    fig.subplots_adjust(left=0, right=1, top=0.9, bottom=0.06)
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close(fig)


def build(key):
    sp = SPEC[key]
    r = RES[key]
    assert r["ladder_allpass"], f"{key}: ladder not all-pass; no package"
    outdir = os.path.join(HERE, sp["dirname"])
    os.makedirs(outdir, exist_ok=True)
    cid = sp["cid"]
    for suf in (".json", ".txt", "_proper.txt"):
        shutil.copy2(os.path.join(HERE, f"g4_tables_{cid}{suf}"), outdir)
    g4 = json.load(open(os.path.join(HERE, f"g4_tables_{cid}.json")))
    nops = g4["n_proper"] + g4["n_improper"]
    T = r["T"]
    fixed, free, ones = r["counts_fixed"], r["counts_free"], r["counts_onesided"]
    nf, no = len(fixed), len(ones)
    # prefix asserts against the V3 (Burnside-verified) counts
    for n, (fx, fr) in r["g4_counts"].items():
        n = int(n)
        assert fixed[n-1] == fx and free[n-1] == fr, "prefix != V3 counts"
    for n in range(min(nf, no)):
        assert fixed[n] >= ones[n] >= free[n] > 0 and ones[n] <= 2*free[n]
    # independent verifier (if run)
    ind_path = os.path.join(HERE, "independent_runs", f"{cid}_independent.json")
    ind = None
    if os.path.exists(ind_path):
        ind = json.load(open(ind_path))
        for row in ind["rows"]:
            n = row["n"]
            assert row["burnside_all_ok"] and row["burnside_proper_ok"]
            if n <= nf:
                assert row["fixed"] == fixed[n-1] and row["free"] == free[n-1]
            if n <= no:
                assert row["onesided"] == ones[n-1]
    n_ind = max(row["n"] for row in ind["rows"]) if ind else 0
    n_burn = max(int(n) for n in r["g4_counts"])

    # ---- COORDS.md
    L = [f"# {sp['shortname']} — exact generating data and coordinates", "",
         f"{sp['known']}", "",
         "All numbers recomputed by `track4/track4_certify.py` (frozen G1 "
         "`spacegroups.json`, exact-Fraction pipeline; certificates in "
         "`track4/TRACK4_CERT_LOG.md`).", "",
         "## Generating data", "",
         f"- Space group: IT(214) = I4_132 (single-origin group)",
         f"- Generating point (fractional): ({', '.join(RES[key]['stages'][0]['detail'].split('p=(')[1].split(')')[0].split(', '))}) — "
         f"site-symmetry order {r['stabilizer']}, Wyckoff stratum dimension {r['stratum_dim']}",
         f"- Orbit: {r['n_conv']} points per conventional cell, T = {T} "
         f"translation classes (primitive)",
         f"- Integer scaling: PERIOD = {r['period']}",
         f"- Primitive lattice basis (columns, integer): {r['lattice_basis']} "
         f"with |det| = {r['detL']}",
         f"- Exact cell volume: {r['cell_volume']} (T x vol = detL certified)", "",
         "## Combinatorics and symmetry", "",
         f"- f-vector (V, E, F): {tuple(r['f_vector'])}",
         f"- p-vector: {r['p_vector']}",
         f"- Combinatorial automorphism order: {r['aut']}",
         f"- Site symmetry order: {r['n_site']}; geometric stabilizer order: "
         f"{r['n_geo']} (over ALL orthogonal maps)",
         f"- Honeycomb point ops mod lattice: |ops| = {nops} ({g4['n_proper']} "
         f"proper, {g4['n_improper']} improper) — "
         f"{'CHIRAL honeycomb (all ops proper): one-sided == free' if g4['n_improper'] == 0 else 'achiral honeycomb'}",
         f"- Bravais point group of the actual lattice: order {r['n_brav']}",
         f"- Non-simple vertices: {r['nonsimple']} (flagged per design; not an error)",
         "",
         f"## Scaled generating orbit (integer, mod {r['period']})", "", "```"]
    L += [f"({q[0]}, {q[1]}, {q[2]})" for q in r["scaled_orbit"]]
    L += ["```", "",
          f"## Exact vertex coordinates of one cell (site "
          f"{tuple(r['scaled_orbit'][0])}, same scaling)", "",
          f"{len(r['vertices'])} vertices, then the {len(r['facet_cycles'])} "
          "facet cycles (CCW from outside) with neighbor sites.", "", "```"]
    L += [f"v{i}: ({v[0]}, {v[1]}, {v[2]})" for i, v in enumerate(r["vertices"])]
    L.append("")
    L += [f"facet {len(cyc)}-gon {cyc}  neighbor site {tuple(nb)}"
          for cyc, nb in zip(r["facet_cycles"], r["neighbors"])]
    L += ["```", ""]
    open(os.path.join(outdir, "COORDS.md"), "w").write("\n".join(L))

    # ---- counts.md
    L = [f"# {sp['shortname']} — polyform counts", "",
         "Banked workflow: `export_tables.py` + compiled `enumerate` (the "
         f"A398957 a-file program) on `g4_tables_{cid}.json`; full ops -> fixed "
         "+ free, proper ops -> one-sided (fixed column identical, asserted). "
         f"Per-run cap 20 min. Full run: {r['note_full']}. Proper run: "
         f"{r['note_proper']}.", "",
         "| n | fixed | free | one-sided | independent (verify_counts_independent.py) |",
         "|---|---|---|---|---|"]
    for n in range(1, nf + 1):
        o = ones[n-1] if n <= no else "—"
        i = "MATCH (fixed/free/one-sided, Burnside ok)" if n <= n_ind else "not run"
        L.append(f"| {n} | {fixed[n-1]} | {free[n-1]} | {o} | {i} |")
    L += ["",
          f"Burnside identity |G|*free(n) = Sum Fix_g(n): banked "
          f"burnside_generic.py ALL PASS for n <= {n_burn} (G4/V3); the "
          f"independent enumerator asserts it at every n <= {n_ind} for both "
          "the full and the proper group." if ind else
          f"Burnside identity verified n <= {n_burn} (G4/V3); independent "
          "enumerator NOT run.",
          "",
          f"Dual-implementation bar: {'MET for n <= ' + str(n_ind) if ind else 'NOT met'}"
          + (f"; n = {n_ind+1}..{nf} rest on the single banked enumerator." if n_ind < nf else "."),
          ""]
    open(os.path.join(outdir, "counts.md"), "w").write("\n".join(L))

    # ---- OEIS drafts
    defsent = (f"{sp['article']} {sp['oeis_name']} is the {r['f_vector'][2]}-faced "
               f"space-filling polyhedron ({r['p_vector']} faces, "
               f"f-vector {tuple(r['f_vector'])}) that is {sp['gen']}; its "
               f"honeycomb has {T} cell types (translation classes), each cell "
               f"with {r['f_vector'][2]} face-neighbors.").strip()
    cert = ("The tiling, its symmetry group (order "
            f"{nops} modulo lattice translations, {g4['n_proper']} proper) and "
            "the counts are certified in exact rational arithmetic: "
            "facet-pairing tiling certificate verified by two independent "
            "implementations; the Burnside identity |G|*free(n) = Sum_g Fix_g(n) "
            f"checked exactly for n <= {max(n_burn, n_ind)}"
            + (f"; all terms n <= {n_ind} reproduced by a second, independently "
               "written enumerator" if ind else "") + ".")
    disclose = ("Computed with the assistance of Claude (Anthropic); every "
                "count produced by the same published enumerator that "
                "generated A398957-A398959, with the exact-arithmetic "
                "verification above.")
    chiral = ("The honeycomb is chiral (all honeycomb symmetries are proper), "
              "so the one-sided and free counts coincide."
              if g4["n_improper"] == 0 else None)
    for vkey, label, countdef in OEIS_VARIANTS:
        data = {"fixed": fixed, "free": free, "onesided": ones}[vkey]
        L = [f"OEIS DRAFT (staged {time.strftime('%Y-%m-%d')} — NOT submitted; "
             "Tyler sequences submissions, see ../../publication/OEIS_DRAFTS_NOTE.md)",
             "",
             "%N (NAME — ends in a period)",
             f"Number of {label} polyforms of the honeycomb of "
             f"{sp['name_genitive']} with n cells.",
             "",
             "%O (OFFSET)", "1", "",
             f"%D (DATA, n = 1..{len(data)})",
             ", ".join(str(x) for x in data),
             "",
             "%C (COMMENTS — each paragraph pasted separately, signed with "
             "~~~~ so the OEIS editor auto-signs; do not type a name or date "
             "by hand)",
             defsent + f" Polyforms are face-connected clusters of cells, {countdef}.",
             sp["known"]]
        if chiral:
            L.append(chiral)
        L += [cert, disclose + " - ~~~~", "",
              "%H (LINKS)",
              "Tyler Satchel Orden, <a href=\"/A______/a______.txt\">Honeycomb "
              "adjacency and symmetry tables, with the enumeration program and "
              "run instructions</a> [a-file: oeis_afile.txt in this folder]"]
        L += sp["links"]
        if n_ind < len(data):
            L += ["",
                  f"DEPTH NOTE (not an OEIS field): terms n <= {n_ind} are "
                  "reproduced by the second, independently written enumerator; "
                  f"term(s) n = {n_ind+1}..{len(data)} rest on the banked "
                  "enumerator alone (the pure-Python verifier is infeasible at "
                  "that size). Tyler decides: submit DATA to n <= "
                  f"{n_ind} (dual-verified) or to n <= {len(data)}."]
        L += ["", "%o (PROG)",
              "(C++) // Redelmeier-style table-driven enumerator; see the "
              "a-file (same program as A398957).", "",
              "%K (KEYWORD)", "nonn", "",
              "%Y (CROSSREFS)",
              "Cf. A398957, A398958, A398959 (Josehedron polyforms, same "
              "enumerator); A385028, A385276, A397707-A397709 (polyforms on "
              "other space-filler honeycombs). [Cross-reference this cell's "
              "other two sequences once A-numbers exist.]", "",
              "%A (AUTHOR)",
              "Tyler Satchel Orden, [date auto-filled by ~~~~ in the editor]",
              "",
              "NOTE before submitting: (1) run the OEIS existence search on the "
              "terms; (2) replace the a-file placeholder with the assigned "
              "A-number; (3) per OEIS rule 17, host the program on the first "
              "assigned entry and cite it from the others; (4) b-file not needed "
              "at this term count; (5) for a chiral honeycomb the one-sided and "
              "free sequences are IDENTICAL — submit ONE entry with both "
              "interpretations in the NAME/COMMENTS rather than a duplicate."
              if chiral else
              "NOTE before submitting: (1) run the OEIS existence search on the "
              "terms; (2) replace the a-file placeholder with the assigned "
              "A-number; (3) per OEIS rule 17, host the program on the first "
              "assigned entry and cite it from the others; (4) b-file not needed "
              "at this term count.", ""]
        open(os.path.join(outdir, f"oeis_draft_{vkey}.txt"), "w").write("\n".join(L))

    full_txt = open(os.path.join(outdir, f"g4_tables_{cid}.txt")).read()
    prop_txt = open(os.path.join(outdir, f"g4_tables_{cid}_proper.txt")).read()
    A = [f"a-file for the {sp['oeis_name']} polyform sequences (fixed / "
         "one-sided / free).", "", defsent, "", sp["known"], "",
         "Program: the table-driven Redelmeier enumerator published as the "
         "a-file of A398957 (enumerate.cpp).  Save a tables block below to "
         "tables.txt and run:  ./enumerate tables.txt N",
         "With TABLES-FULL the output columns are n, fixed, free.",
         "With TABLES-PROPER the 'free' column is the one-sided count "
         "(fixed column identical).",
         "Exact generating data (space group, point, lattice basis, vertex "
         "coordinates): COORDS.md in the same package.", "",
         f"===== TABLES-FULL ({nops} ops) =====", full_txt.rstrip(),
         "===== END TABLES-FULL =====", "",
         f"===== TABLES-PROPER ({g4['n_proper']} proper ops) =====",
         prop_txt.rstrip(), "===== END TABLES-PROPER =====", ""]
    open(os.path.join(outdir, "oeis_afile.txt"), "w").write("\n".join(A))
    render(sp, r, os.path.join(outdir, "render.png"))
    print(f"{key}: package built in {outdir} (n_fixed<={nf}, one-sided<={no}, "
          f"independent<={n_ind}, burnside<={n_burn})")


if __name__ == "__main__":
    keys = sys.argv[1:] or [k for k in SPEC if k in RES]
    for k in keys:
        build(k)
