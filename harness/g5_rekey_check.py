#!/usr/bin/env python3
"""G5 duty 1 gate (2026-08-30): independent re-key verification of the Schmitt
Sec. 2.2.5 table digitization for the six distinct groups hosting the 11
G4-certified candidates (201, 212/213 shared, 214, 220, 224, 230).

Three-way comparison:
  (A) rekey_tables.json  — fresh VISUAL transcription from rendered PDF pages,
      made without consulting triage_phase1.py (see its _meta for provenance),
  (B) the PDF text layer — pdftotext -layout, parsed programmatically here
      (a different extraction modality of the same printed source),
  (C) SCHMITT_FVECTORS in triage_phase1.py — the original single-pass
      digitization under audit.

A vs B validates the re-key transcription itself (f-vectors AND frequencies);
A vs C is the re-key diff proper (f-vector level, all rows, printed order).
Exit 0 iff all three agree on every row of every audited group.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "..", "references", "Schmitt_2016_dissertation.pdf")
REKEY = os.path.join(HERE, "rekey_tables.json")
TRIAGE = os.path.join(HERE, "triage_phase1.py")
RANGES = [(129, 129), (138, 143), (146, 150), (153, 155)]  # PDF pages (printed = PDF-5)
TARGETS = {"201", "212_213", "214", "220", "224", "230"}
KEYMAP = {"201": 201, "212_213": 212, "214": 214, "220": 220, "224": 224, "230": 230}

row_re = re.compile(r"^\s*\((\d+),\s*(\d+),\s*(\d+)\)\s+\(.*\)\s+([\d   ]+?)\s*$")
hdr_re = re.compile(r"IT\((\d{3})\)")

def parse_text_layer():
    tables = {}
    for a, b in RANGES:
        out = subprocess.run(["pdftotext", "-layout", "-f", str(a), "-l", str(b), PDF, "-"],
                             capture_output=True, text=True, check=True).stdout
        group = None
        for line in out.splitlines():
            if "Space group type" in line:
                m = hdr_re.search(line)
                if m:
                    g = m.group(1)
                    group = "212_213" if g in ("212", "213") else g
                continue
            m = row_re.match(line)
            if m and group in TARGETS:
                v, e, f = int(m.group(1)), int(m.group(2)), int(m.group(3))
                freq = int(re.sub(r"\D", "", m.group(4)))
                assert v - e + f == 2 and v >= 4, f"non-Euler table line: {line!r}"
                tables.setdefault(group, []).append([[v, e, f], freq])
    return tables

def load_triage_fvectors():
    src = open(TRIAGE).read()
    ns = {"__file__": TRIAGE}
    exec(compile(src.split("def main()")[0], "triage_head", "exec"), ns)
    return ns["SCHMITT_FVECTORS"]

def main():
    rekey = json.load(open(REKEY))
    text = parse_text_layer()
    triage = load_triage_fvectors()
    fails = 0
    total = 0
    for g in sorted(TARGETS):
        mine = rekey[g]["rows"]
        fv_mine = [tuple(r[0]) for r in mine]
        total += len(mine)
        # A vs B: visual re-key vs text layer, f-vectors AND frequencies, ordered
        tl = text.get(g, [])
        ab = "IDENTICAL" if [list(r) for r in mine] == tl else "MISMATCH"
        # A vs C: re-key vs triage digitization, f-vector level, ordered
        fv_triage = [tuple(r) for r in triage[KEYMAP[g]]]
        ac = "IDENTICAL" if fv_mine == fv_triage else "MISMATCH"
        print(f"group {g:8s}: rows rekey={len(mine)} text={len(tl)} triage={len(fv_triage)} | "
              f"rekey-vs-textlayer {ab} | rekey-vs-triage {ac}")
        if ab != "IDENTICAL" or ac != "IDENTICAL":
            fails += 1
            for i in range(max(len(mine), len(tl), len(fv_triage))):
                a = mine[i] if i < len(mine) else None
                b = tl[i] if i < len(tl) else None
                c = fv_triage[i] if i < len(fv_triage) else None
                if (a is None or b is None or list(a) != b) or \
                   (a is None or c is None or tuple(a[0]) != c):
                    print(f"  row {i}: rekey={a} textlayer={b} triage={c}")
    # 213 must alias 212's table in the triage digitization
    assert triage[213] is triage[212] or triage[213] == triage[212], "213 not aliased to 212"
    print(f"\naudited rows per source: {total} (six tables); "
          f"triage digitization total rows (all 36 groups, 213 aliased): "
          f"{sum(len(v) for k, v in triage.items() if k != 213)}")
    print("VERDICT:", "ALL PASS — re-key CLEAN, 0 discrepancies" if fails == 0
          else f"{fails} GROUP(S) DISCREPANT")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
