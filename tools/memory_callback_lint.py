"""eng7-l09: check all incoming memory callbacks, their gaps and twins."""
import json
from pathlib import Path
from tools.player_text_lint import surfaces, PATTERNS
from tools.draft_contract_lint import targets

CONTRACTS = Path(__file__).with_name("memory_callback_contracts.json")


def check(story, contracts=None):
    contracts = json.loads(CONTRACTS.read_text(encoding="utf-8")) if contracts is None else contracts
    scenes = {s["Id"]: s for s in story["Scenes"]}
    hard, executed, absent = [], [], []
    for contract in contracts:
        sid, target, gone = contract["scene"], contract["node"], contract["gone"]
        if sid not in scenes:
            if contract.get("optional_absent"):
                absent.append(sid)
                continue
            hard.append(sid + ": missing callback host")
            continue
        nodes = {n["Id"]: n for n in scenes[sid]["Nodes"]}
        key = sid + "/" + target
        original, gap = nodes.get(target), nodes.get("gap." + target)
        incoming = {(n["Id"], i) for n in nodes.values() for i, c in enumerate(n["Choices"]) if target in targets(c)}
        if incoming != {tuple(v) for v in contract["vias"]}:
            hard.append(key + ": incoming callback contract drift")
        if not original or not gap or gap["Choices"] != original["Choices"]:
            hard.append(key + ": missing gap or changed continuation")
            continue
        if any(term in gap["Text"] for term in contract["forbidden_sensory"]):
            hard.append(key + ": sold sensory recollection in gap")
        twin = scenes.get(contract["twin"], {})
        twin_gap = next((n for n in twin.get("Nodes", []) if n["Id"] == "gap." + target), {})
        if (twin or not contract.get("optional_twin_absent")) and (twin_gap.get("Text") != gap["Text"] or twin_gap.get("Choices") != gap["Choices"]):
            hard.append(key + ": twin gap drift")
        for via, index in contract["vias"]:
            original_choice = nodes.get(via, {}).get("Choices", [])[index]
            alternatives = [c for c in nodes[via]["Choices"] if c.get("Next") == "gap." + target]
            # Each incoming old choice has its own appended copy, including its effects.
            expected = {**original_choice, "Next": "gap." + target,
                        "Requires": list(dict.fromkeys(original_choice.get("Requires", []) + ["trickster.ever", gone])),
                        "Forbids": [f for f in original_choice.get("Forbids", []) if f != gone]}
            if gone not in original_choice.get("Forbids", []) or expected not in alternatives:
                hard.append(key + ": unguarded incoming choice " + via + "[%d]" % index)
            else:
                executed.append(dict(scene=sid, via=via, index=index, sold_text=gap["Text"], unsold_text=original["Text"]))
    review = [dict(scene=sid, location=location, code="vision-justification", start=m.start(), end=m.end(), match=m.group())
              for sid, location, text, _, _ in surfaces(story) for m in PATTERNS["vision-justification"].finditer(text)]
    return dict(hard=sorted(set(hard)), executed=executed, no_change_needed=absent, review=review)
