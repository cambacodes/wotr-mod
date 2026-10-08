"""Bounded shortest-path measure for the Nocticula base route.

Same fixture and counting policy as tools/measure_nocticula_n1.py (node and
choice text, ending receipts; explicit fills and pending prose count zero), but
it never enumerates path histograms, whose state space exhausts memory:
- lower_bound: every live visit is mandatory (progression gates), and within
  each scene every choice/check branch is treated as available, so the true
  shortest accepted path cannot be shorter;
- beam_upper: an actually reachable path found by keeping the BEAM cheapest
  flag states per visit (BEAM env var, default 3000).
Runs in seconds and well under 1 GB. Writer measurement, not release approval.
"""
import sys, json, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tools.measure_nocticula_n1 as M  # noqa: E402
from copy import deepcopy
from functools import lru_cache
from storylines.nocticula_trickster_concession import outcomes
from storylines.nocticula_trickster_acquisition import allowed
route, partners, words = M.route, M.partners, M.words
BEAM = int(os.environ.get("BEAM", "3000"))
payload = {"Scenes": deepcopy(route.SCENES + M.nocticula_acquired_harbor.SCENES + M.nocticula_trickster.SCENES + M.nocticula_trickster_concession.SCENES)}
partners.integrate(payload)
P = "[N2 PROSE PENDING:"
sel = [s for s in payload["Scenes"] if s.get("Relationship") == "nocticula" and ".acquired." not in s["Id"] and s["Id"].startswith("noct.") and "noct.retired" not in s["Requires"]]
visits = [s for s in sel if s["Owner"] == "Memory"]
endings = [s for s in sel if s["Id"] in ("noct.ending_company", "noct.ending_alliance")]
pending = sorted({s["Id"] for s in sel for n in s["Nodes"] for b in (n, *n.get("Paragraphs", [])) if P in b.get("Text", "")})
for s in sel:
    for n in s["Nodes"]:
        if ".explicit." in n["Id"] or P in n["Text"]:
            n["Text"] = ""
def relaxed_min(s):
    nodes = {n["Id"]: n for n in s["Nodes"]}
    @lru_cache(None)
    def best(key):
        n = nodes[key]; out = []
        for c in n["Choices"]:
            if c["Abort"] or "noct.closed" in c.get("Set", []): continue
            ck = c.get("Check"); tg = (ck["Success"], ck["Failure"]) if ck else (c.get("Next"),)
            base = words(n["Text"]) + words(c["Text"])
            out.append(base + min(best(t) if t else 0 for t in tg))
        return min(out) if out else 10**9
    return best(s["Nodes"][0]["Id"])
lb_rows = [(s["Id"], relaxed_min(s)) for s in visits]
lb_end = min(relaxed_min(s) for s in endings)
LB = sum(r[1] for r in lb_rows) + lb_end
# beam UB
states = {frozenset({"trickster", "noct.parent_active", "noct.parent_agreement_seen", "noct.gift"}): (0, ())}
for s in visits:
    upd = {}
    for st, (cnt, trail) in states.items():
        if not allowed(s, st):
            raise AssertionError((s["Id"], "missing progression gate"))
        for final, c in outcomes(s, st, words):
            if "noct.closed" in final or partners.P+"secret" in final or partners.P+"exclusive" in final: continue
            k = frozenset(final); v = cnt + c
            if k not in upd or v < upd[k][0]: upd[k] = (v, trail + ((s["Id"], c),))
    states = dict(sorted(upd.items(), key=lambda kv: kv[1][0])[:BEAM])
UB = None
for st, (cnt, trail) in states.items():
    for s in endings:
        if not allowed(s, st): continue
        r = sum(words(p["Text"]) for n in s["Nodes"] for p in n.get("Paragraphs", []) if allowed(p, st) and P not in p["Text"])
        for final, c in outcomes(s, st, words):
            if UB is None or cnt + c + r < UB[0]: UB = (cnt + c + r, trail + ((s["Id"], c + r),))
print(json.dumps(dict(lower_bound=LB, beam_upper=UB[0], beam=BEAM, pending_scenes=pending,
    lb_rows=lb_rows, lb_ending=lb_end, ub_path=UB[1])))
