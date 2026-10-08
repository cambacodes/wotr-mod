"""Selected N1 base paths: shortest and path-count-weighted median commitment.

Uses the route's existing outcomes/word counter, with future-reader projection.
Explicit fill defaults and pending paragraphs contribute zero words. This is a
writer measurement, not release approval or a substitute for prose review.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from functools import cache
from pathlib import Path
import json
import runpy
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from storylines import nocticula_continuation as route, nocticula_partners as partners
from storylines import nocticula_acquired_harbor, nocticula_trickster, nocticula_trickster_concession
from storylines.nocticula_trickster_acquisition import allowed
from storylines.nocticula_trickster_concession import outcomes

words = cache(runpy.run_path(str(Path(__file__).with_name("measure-story-content.py")))["words"])


def measure():
    payload = {"Scenes": deepcopy(route.SCENES + nocticula_acquired_harbor.SCENES
                                 + nocticula_trickster.SCENES + nocticula_trickster_concession.SCENES)}
    partners.integrate(payload)
    selected = [s for s in payload["Scenes"] if s.get("Relationship") == "nocticula"
                and ".acquired." not in s["Id"] and s["Id"].startswith("noct.")
                and "noct.retired" not in s["Requires"]]
    visits = [s for s in selected if s["Owner"] == "Memory"]
    endings = [s for s in selected if s["Id"] in ("noct.ending_company", "noct.ending_alliance")]
    pending_prose = any("[N2 PROSE PENDING:" in block.get("Text", "")
                        for s in selected for node in s["Nodes"]
                        for block in (node, *node.get("Paragraphs", [])))
    # Keep the existing paragraph-address policy: paragraph text is counted only
    # after its actual gates hold, never all variants on the same page.
    for s in selected:
        for node in s["Nodes"]:
            if ".explicit." in node["Id"] or "[N2 PROSE PENDING:" in node["Text"]:
                node["Text"] = ""

    def readers(scenes):
        used = {"noct.closed"}
        for s in scenes:
            for item in (s, *(c for n in s["Nodes"] for c in n["Choices"]),
                         *(p for n in s["Nodes"] for p in n.get("Paragraphs", []))):
                if "[N2 PROSE PENDING:" in item.get("Text", ""):
                    continue  # empty receipt text cannot affect this measurement
                used.update(item.get("Requires", [])); used.update(item.get("Forbids", []))
                used.update(k for g in item.get("AnyGroups", []) for k in g)
        return used

    initial = {"trickster", "noct.parent_active", "noct.parent_agreement_seen", "noct.gift"}
    states = {frozenset(initial): Counter({0: 1})}
    for i, s in enumerate(visits):
        later = readers(visits[i + 1:] + endings)
        updated = defaultdict(Counter)
        for state, histogram in states.items():
            if not allowed(s, state):
                raise AssertionError((s["Id"], "missing progression gate", sorted(state)))
            transitions = Counter((frozenset(final & later), count)
                                  for final, count in outcomes(s, state, words)
                                  if "noct.closed" not in final
                                  and partners.P + "secret" not in final
                                  and partners.P + "exclusive" not in final)
            for (final, count), multiplicity in transitions.items():
                target = updated[final]
                for old_count, paths in histogram.items():
                    target[old_count + count] += paths * multiplicity
        states = updated
    final_counts = Counter()
    for state, histogram in states.items():
        for s in endings:
            if not allowed(s, state):
                continue
            receipt_words = sum(words(p["Text"]) for n in s["Nodes"] for p in n.get("Paragraphs", [])
                                if allowed(p, state) and "[N2 PROSE PENDING:" not in p["Text"])
            for final, count in outcomes(s, state, words):
                for old_count, paths in histogram.items():
                    final_counts[old_count + count + receipt_words] += paths
    total = sum(final_counts.values())
    cumulative = 0
    median = None
    for count, paths in sorted(final_counts.items()):
        cumulative += paths
        if cumulative * 2 >= total:
            median = count
            break
    return dict(live_visits=len(visits), accepted_paths=total, shortest=min(final_counts), median=median,
                maximum=max(final_counts), pending_prose=pending_prose, explicit_defaults_counted=False,
                fixture="Trickster, original Gift and parent agreement; accepted shared terms; Shamira alive; no companions present")


if __name__ == "__main__":
    print(json.dumps(measure(), indent=2))
