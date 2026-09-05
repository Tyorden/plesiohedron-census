#!/usr/bin/env python
"""orbit.py — exact space-group orbit generation (design doc §1.2).

Input: a group entry from the frozen, G1-audited spacegroups.json and a
rational base point p in [0,1)^3. All arithmetic is fractions.Fraction —
floats never enter this module.

Provides:
  load_groups()       — parse spacegroups.json, ops as (int R, Fraction t).
  orbit(entry, p)     — the orbit {R_i p + t_i mod 1} with the site-stabilizer
                        (general-position) gate: a nontrivial stabilizer flags
                        the point as a special (Wyckoff) position; callers must
                        route those to the special-position sub-sweep, never
                        silently mix them (design §1.2, §6.2).
  scale_orbit(points) — integer scaling: PERIOD = lcm(denominators, 12); points
                        become integer triples mod PERIOD (the BASE/PERIOD
                        pattern of build_josehedron.py:33-35, g1_verify.py:10-12).

Orbit sizes: n_conventional = |orbit| in the conventional cell = n_ops /
|stabilizer|; n_primitive = n_conventional / centering multiplicity (the T of
design §1.2, ≤ 48).
"""
import json
import os
from fractions import Fraction as F
from math import lcm

HERE = os.path.dirname(os.path.abspath(__file__))
SPACEGROUPS_JSON = os.path.join(HERE, "spacegroups.json")

IDENTITY_R = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def load_groups(path=SPACEGROUPS_JSON):
    """Return {ITA number: entry dict} with 'ops_exact' = [(R, t)] parsed exactly."""
    raw = json.load(open(path))
    groups = {}
    for e in raw["groups"]:
        e = dict(e)
        e["ops_exact"] = [
            (tuple(tuple(int(x) for x in row) for row in op["R"]),
             tuple(F(s) for s in op["t"]))
            for op in e["ops"]
        ]
        e["centering_vectors"] = [tuple(F(s) for s in v)
                                  for v in e["centering"]["vectors"]]
        groups[e["number"]] = e
    return groups


def mod1(x):
    return x % 1  # Fraction % 1 is exact and lands in [0,1)


def apply_op(R, t, p):
    """(R, t) acting on fractional point p, reduced mod 1. Exact."""
    return tuple(mod1(sum(R[i][j] * p[j] for j in range(3)) + t[i])
                 for i in range(3))


def site_stabilizer(entry, p):
    """All ops with R p + t == p (mod 1). Length 1 (identity) <=> general position."""
    p = tuple(mod1(F(x)) for x in p)
    return [(R, t) for (R, t) in entry["ops_exact"] if apply_op(R, t, p) == p]


def orbit(entry, p):
    """Exact orbit of p under the group's coset list (conventional cell, mod 1)."""
    p = tuple(mod1(F(x)) for x in p)
    stab = site_stabilizer(entry, p)
    pts = sorted(set(apply_op(R, t, p) for (R, t) in entry["ops_exact"]))
    n_ops = len(entry["ops_exact"])
    assert len(pts) * len(stab) == n_ops, \
        f"orbit-stabilizer identity failed: {len(pts)}*{len(stab)} != {n_ops}"
    mult = entry["centering"]["multiplicity"]
    assert len(pts) % mult == 0, "orbit not divisible by centering multiplicity"
    return {
        "point": p,
        "points": pts,
        "stabilizer_order": len(stab),
        "general_position": len(stab) == 1,
        "n_conventional": len(pts),
        "n_primitive": len(pts) // mult,
    }


def scale_orbit(points):
    """Clear denominators: PERIOD = lcm(all coordinate denominators, 12).

    Returns (list of integer triples in [0, PERIOD)^3, PERIOD). Exact; asserts
    the scaling is a bijection (no collisions) and every scaled coordinate is
    a true integer.
    """
    points = [tuple(F(x) for x in p) for p in points]
    dens = {x.denominator for p in points for x in p}
    period = lcm(12, *sorted(dens))
    ints = []
    for p in points:
        q = []
        for x in p:
            s = x * period
            assert s.denominator == 1, "scaling failed to clear a denominator"
            q.append(int(s) % period)
        ints.append(tuple(q))
    assert len(set(ints)) == len(set(points)), "integer scaling collided points"
    return ints, period


def _selftest():
    groups = load_groups()
    # P23 (#195): 12 ops, P centering. General point -> trivial stabilizer, orbit 12.
    g = groups[195]
    p = (F(1, 8), F(1, 6), F(1, 3))
    ob = orbit(g, p)
    assert ob["general_position"] and ob["n_conventional"] == 12 and ob["n_primitive"] == 12, ob
    ints, period = scale_orbit(ob["points"])
    assert period == 24 and len(ints) == 12, (period, len(ints))
    # P23 special position (0,0,0): full point-group stabilizer, orbit 1, flagged.
    ob0 = orbit(g, (F(0), F(0), F(0)))
    assert (not ob0["general_position"]) and ob0["stabilizer_order"] == 12 \
        and ob0["n_conventional"] == 1, ob0
    # Fm-3m (#225): 192 conventional ops, F centering (mult 4) -> T_primitive 48.
    g = groups[225]
    ob = orbit(g, (F(1, 8), F(1, 6), F(5, 12)))
    assert ob["general_position"] and ob["n_conventional"] == 192 \
        and ob["n_primitive"] == 48, (ob["n_conventional"], ob["n_primitive"])
    # Gate catches a SUBTLE special position: (1/8,1/6,1/3) is fixed by the
    # Fm-3m op (x, -z+1/2, -y+1/2) -- stabilizer 2, orbit 96, flagged.
    ob = orbit(g, (F(1, 8), F(1, 6), F(1, 3)))
    assert (not ob["general_position"]) and ob["stabilizer_order"] == 2 \
        and ob["n_conventional"] == 96, (ob["n_conventional"], ob["stabilizer_order"])
    print("orbit.py selftest: PASS (P23 general 12 / special flagged / "
          "Fm-3m 192->48 / subtle glide-mirror special position flagged / PERIOD lcm ok)")


if __name__ == "__main__":
    _selftest()
