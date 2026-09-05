#!/usr/bin/env python
"""Fold the 2026-09-03 independent-enumerator verdict into build_summary.json.
Reads publication/independent_runs/*.json (written by verify_counts_independent.py),
asserts ok == True and that every fixed/free/onesided value at n <= 6 equals the
value already in build_summary.json, and then rewrites the `burnside` status
string of that shape and adds `independent_2026_09_03: true`.  Deterministic;
nothing numeric is changed.  Run after build_packages.py, before make_tables.py."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = {"satchelhedron": "8cf50403cf88c455", "ordenhedron": "2de0a21129cabe90",
        "pn3m_11facet": "c4ea3f32fdd6dc51", "pn3m_7facet": "f98a3ee5675fc121"}
path = os.path.join(HERE, "build_summary.json")
summary = json.load(open(path))
for run, cid in RUNS.items():
    d = json.load(open(os.path.join(HERE, "independent_runs", run + ".json")))
    assert d["ok"] is True, run
    assert cid in d["tables"], (run, d["tables"])
    k = summary["counts"][cid]
    for row in d["rows"]:
        n = row["n"]
        assert n <= 6 and row["burnside_all_ok"] and row["burnside_proper_ok"]
        assert row["fixed"] == k["fixed"][n-1] and row["free"] == k["free"][n-1] \
            and row["onesided"] == k["onesided"][n-1], (run, n)
    assert len(d["rows"]) == 6
    prior = k["burnside"]
    tag = ("burnside_generic.py growth check n<=6 (build of 2026-09-01)" if prior.startswith("EXTENDED")
           else "burnside_generic.py growth check n<=4 only (G4)")
    k["burnside"] = ("INDEPENDENT n<=6: second, code-disjoint enumerator (verify_counts_independent.py, "
                     "INDEPENDENT_COUNTS_2026-09-03.md) reproduced every fixed/one-sided/free term and asserted the "
                     "Burnside identity for both groups at every n <= 6; " + tag)
    k["independent_2026_09_03"] = True
    print(cid, "->", k["burnside"])
json.dump(summary, open(path, "w"), indent=1)
print("build_summary.json updated")
