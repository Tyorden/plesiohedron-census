#!/usr/bin/env python
"""digitize_schmitt_hexagonal.py — Schmitt 2016 Sec. 2.2.3 (Trigonal) + 2.2.4
(Hexagonal) tables, IT(143)-IT(194), from the PDF text layer into
schmitt_hexagonal_tables.json (same schema as schmitt_tetragonal_tables.json).

Method (recorded in SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md): the primary
source is `pdftotext -layout` of PDF pages 86-123 (printed 81-118; PDF page =
printed + 5); rows are parsed with the same regular expression the batch-1
harvest used (f-vector | b-ratio | generating grid point); every row is Euler-
checked; block header facts are parsed from the text layer with the fraction
glyphs of the normalizer bases normalized (the text layer prints a fraction
p/q as the two digits in unreliable order, e.g. "32 b01" or "23 b01" for
2/3 b1'; all such fractions are in (0,1), so min/max of the two digits is the
fraction — confirmed against the rendered pages 88, 114, 123). A VISUAL
cross-read of the rendered pages (pdftoppm 120 dpi) covered every row of PDF
pages 88, 97, 105, 114, 123 (153 rows) plus the block headers there; the
diff is recorded in the digitization note. NOT an independent second re-key.

Run: python3 digitize_schmitt_hexagonal.py
"""
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(os.path.dirname(HERE), "references", "Schmitt_2016_dissertation.pdf")
OUT = os.path.join(HERE, "schmitt_hexagonal_tables.json")
FIRST_PDF, LAST_PDF = 86, 123           # Sec. 2.2.3 starts on PDF 86 (printed 81); IT(194) ends PDF 123
PAGE_OFFSET = 5
GROUPS = set(range(143, 195))
VISUAL_PAGES = [88, 97, 105, 114, 123]

ROW = re.compile(r"^\s*\((\d+),\s*(\d+),\s*(\d+)\)\s+(\d+(?:/\d+)?)\s+"
                 r"\((-?\d+(?:/\d+)?),\s*(-?\d+(?:/\d+)?),\s*(-?\d+(?:/\d+)?)\)\s*$")
HDR = re.compile(r"Space group type \(([^)]*)\);\s*(.*)")
ITRE = re.compile(r"IT\((\d+)\)")
TUP = re.compile(r"\((-?\d+(?:/\d+)?),\s*(-?\d+(?:/\d+)?),\s*(-?\d+(?:/\d+)?)\)")

# Hermann-Mauguin short symbols, thesis index (printed pp. 181-182), _ = subscript, - = bar
SYMBOLS = {143: "P3", 144: "P3_1", 145: "P3_2", 146: "R3", 147: "P-3", 148: "R-3",
           149: "P312", 150: "P321", 151: "P3_112", 152: "P3_121", 153: "P3_212",
           154: "P3_221", 155: "R32", 156: "P3m1", 157: "P31m", 158: "P3c1",
           159: "P31c", 160: "R3m", 161: "R3c", 162: "P-31m", 163: "P-31c",
           164: "P-3m1", 165: "P-3c1", 166: "R-3m", 167: "R-3c", 168: "P6",
           169: "P6_1", 170: "P6_5", 171: "P6_2", 172: "P6_4", 173: "P6_3",
           174: "P-6", 175: "P6/m", 176: "P6_3/m", 177: "P622", 178: "P6_122",
           179: "P6_522", 180: "P6_222", 181: "P6_422", 182: "P6_322", 183: "P6mm",
           184: "P6cc", 185: "P6_3cm", 186: "P6_3mc", 187: "P-6m2", 188: "P-6c2",
           189: "P-62m", 190: "P-62c", 191: "P6/mmm", 192: "P6/mcc",
           193: "P6_3/mcm", 194: "P6_3/mmc"}


def text_pages():
    txt = subprocess.run(["pdftotext", "-layout", "-f", str(FIRST_PDF), "-l", str(LAST_PDF),
                          PDF, "-"], check=True, capture_output=True, text=True).stdout
    txt = txt.replace("−", "-").replace("ε", "eps ")
    pages = txt.split("\f")
    return {FIRST_PDF + i: p for i, p in enumerate(pages) if p.strip()}


def clean_basis(s):
    """Normalize the text-layer rendering of a normalizer basis: b0k -> bk',
    two-digit fraction glyphs 'pq bk' -> 'min/max bk' (all in (0,1))."""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"b0(\d)", r"b\1'", s)
    s = re.sub(r"\b([1-9])([1-9]) (b\d')", lambda m: f"{min(m[1], m[2])}/{max(m[1], m[2])} {m[3]}", s)
    s = s.replace("eps b", "eps b").replace(" ,", ",")
    s = s.replace("3̄", "-3").replace("6̄", "-6")
    return s


def main():
    pages = text_pages()
    blocks = OrderedDict()
    cur = None
    state = None                      # which header field we are collecting
    for pdfp in sorted(pages):
        for line in pages[pdfp].split("\n"):
            if not line.strip():
                continue
            m = HDR.search(line)
            if m:
                nums = tuple(int(x) for x in ITRE.findall(m.group(2)))
                if not nums or nums[0] not in GROUPS:
                    cur = None
                    continue
                key = "_".join(str(n) for n in nums)
                cur = blocks[key] = {
                    "groups": list(nums),
                    "symbols": {str(n): SYMBOLS[n] for n in nums},
                    "space_group_type": m.group(1).strip(),
                    "header_line": re.sub(r"\s+", " ", line.strip()),
                    "pdf_pages": [pdfp], "printed_pages": [pdfp - PAGE_OFFSET],
                    "_norm_raw": "", "_dom_raw": "", "_ub_raw": "", "_lb_raw": "", "_met_raw": "",
                    "rows": [],
                }
                state = None
                continue
            if cur is None:
                continue
            if pdfp not in cur["pdf_pages"]:
                cur["pdf_pages"].append(pdfp)
                cur["printed_pages"].append(pdfp - PAGE_OFFSET)
            s = line.strip()
            if s.startswith("Normalizer:"):
                state = "_norm_raw"
            elif s.startswith("Reduced fundamental domain"):
                state = "_dom_raw"
            elif s.startswith("Upper bound on number of facets"):
                state = "_ub_raw"
            elif s.startswith("Remarks concerning lower bounds"):
                state = "_lb_raw"
            elif s.startswith("Metrical parameters"):
                state = "_met_raw"
            elif re.match(r"^f\s*-vector", s):
                state = None
                continue
            elif re.fullmatch(r"\d+", s):          # printed page number
                continue
            r = ROW.match(line)
            if r:
                fv = [int(r[1]), int(r[2]), int(r[3])]
                assert fv[0] - fv[1] + fv[2] == 2, (cur["groups"], fv)
                for x in (r[4], r[5], r[6], r[7]):
                    F(x)                                   # parses
                cur["rows"].append({"f": fv, "b": r[4], "pt": [r[5], r[6], r[7]],
                                    "freq": None, "pdf_page": pdfp})
                state = None
                continue
            if state:
                cur[state] += " " + s
    # finalize header fields
    out = OrderedDict()
    n_rows = 0
    for key, b in blocks.items():
        norm = clean_basis(b.pop("_norm_raw").replace("Normalizer:", ""))
        dom = b.pop("_dom_raw")
        verts = ["(" + ", ".join(t) + ")" for t in TUP.findall(dom)]
        ub = re.sub(r"\s+", " ", b.pop("_ub_raw").replace("Upper bound on number of facets:", "")).strip()
        lb = re.sub(r"\s+", " ", b.pop("_lb_raw").replace("Remarks concerning lower bounds:", "")).strip() or None
        met = re.sub(r"\s+", " ", b.pop("_met_raw").replace("Metrical parameters:", "")).strip()
        mb = re.search(r"b-ratio varies from (\S+), \. \. \. , (\S+) in (\d+) steps of (\S+)\.", met)
        assert mb, (key, met)
        brange = f"{mb[1]} .. {mb[2]} in {mb[3]} steps of {mb[4]}"
        mg = re.search(r"(?:uses|used) ([\d ]+?) (?:grid )?points", met)
        assert mg, (key, met)
        grid = mg[1].replace(" ", "")
        finer = "Initially" in met or "finer" in met
        rows = b.pop("rows")
        b.update({
            "normalizer": norm,
            "reduced_domain_vertices": verts,
            "upper_bound": ub,
            "lower_bound_remark": lb,
            "b_ratio_range": brange,
            "grid_points": grid,
            "metrical_parameters_text": met,
            "finer_grid_mentioned": finer,
            "n_rows": len(rows),
            "max_facets": max(r["f"][2] for r in rows),
            "euler_ok": all(r["f"][0] - r["f"][1] + r["f"][2] == 2 for r in rows),
            "rows": rows,
        })
        n_rows += len(rows)
        out[key] = b
    covered = sorted({g for b in out.values() for g in b["groups"]})
    assert covered == sorted(GROUPS), set(GROUPS) - set(covered)
    meta = OrderedDict([
        ("purpose", "Digitization of Schmitt 2016 (dissertation, references/Schmitt_2016_dissertation.pdf) "
                    "Sections 2.2.3 Trigonal groups and 2.2.4 Hexagonal groups, IT(143)-IT(194): every printed "
                    "per-group table (f-vector | b-ratio | generating grid point) plus block header facts."),
        ("source_pages", f"printed pp. 81-118 = PDF pages {FIRST_PDF}-{LAST_PDF} (PDF page = printed + {PAGE_OFFSET}); "
                         "Sec. 2.2.5 Cubic begins on printed p. 119 / PDF 124 after the IT(194) table"),
        ("method", "TEXT-LAYER PRIMARY (pdftotext -layout, parsed by digitize_schmitt_hexagonal.py, 2026-09-04) with a "
                   "VISUAL cross-read (pdftoppm 120 dpi, read by Fable 5.1) of every row and header on PDF pages "
                   + ", ".join(str(p) for p in VISUAL_PAGES) + " (153 rows); Euler V-E+F=2 asserted on every row. "
                   "Normalizer-basis fractions are normalized from the text layer's two-digit glyphs (see script "
                   "docstring). NOT a second independent re-key: G5 re-key duty stays owed for any finalist-hosting group."),
        ("conventions", "f-vector = (vertices, edges, facets) as printed; b-ratio = ||b3'||/||b1'|| = c/a as an exact "
                        "rational string (his headers use the primed = ITA basis for this ratio); generating grid point "
                        "= exact rational triple AS PRINTED, in Schmitt's orthohexagonal basis B'' = (2b1'+b2', b2', b3') "
                        "(App. B / Sec. 2.2.3) — conversion to the ITA hexagonal basis: x' = 2x'', y' = x''+y'', z' = z'' "
                        "(hypothesis H1 of ANCHORS G2c; the gate records which convention the exact chain confirms). "
                        "Rhombohedral groups on hexagonal axes (obverse). No origin-choice ambiguity in this family. "
                        "No frequency column is printed in any trigonal/hexagonal table: 'freq' is null throughout."),
        ("shared_tables", "Enantiomorphic pairs printed as ONE table each: 144/145, 151/153, 152/154, 169/170, 171/172, "
                          "178/179, 180/181 (45 printed blocks for 52 groups); the normalizer remark says which member "
                          "the stated normalizer belongs to."),
        ("checks", f"Euler on all {n_rows} rows; ANCHORS G2c rows S143/S147/S155/S166/S178/S194 asserted present by "
                   "phase2/g2c_controls.py; per-group max facets vs Sec. 2.3 remarks recorded in "
                   "SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md"),
        ("row_format", {"f": "[V,E,F]", "b": "b-ratio rational string", "pt": "[x,y,z] rational strings (B'' basis as printed)",
                        "freq": "null (not printed)", "pdf_page": "PDF page the row is printed on"}),
        ("n_blocks", len(out)),
        ("n_rows", n_rows),
        ("digitized_by", "Fable 5.1 (subagent #143), 2026-09-04; script digitize_schmitt_hexagonal.py"),
        ("symbols_note", "Hermann-Mauguin short symbols (thesis index, printed pp. 181-182; subscripts written with _ and bar as -)"),
    ])
    final = OrderedDict([("_meta", meta)])
    final.update(out)
    with open(OUT, "w") as fh:
        json.dump(final, fh, indent=1)
    print(f"wrote {OUT}: {len(out)} blocks, {n_rows} rows, groups {covered[0]}-{covered[-1]} ({len(covered)})")
    for key, b in out.items():
        print(f"  {key:8s} rows {b['n_rows']:3d} maxF {b['max_facets']:2d} pdf {b['pdf_pages']} grid {b['grid_points']} "
              f"| {b['normalizer'][:60]} | dom {len(b['reduced_domain_vertices'])} | ub {b['upper_bound'][:40]}"
              + (f" | LB {b['lower_bound_remark'][:40]}" if b['lower_bound_remark'] else "")
              + (" | FINER" if b['finer_grid_mentioned'] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
