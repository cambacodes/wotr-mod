"""Class A/B mechanical gates over existing earned history and availability.

Authored engine addition, eng3-ab. The registries cite their source gates and
explicit unresolved findings. No scene, node, choice or prose is replaced.
"""
import json
from pathlib import Path
from tools.departure_epochs import install, require

ROOT = Path(__file__).resolve().parents[1] / "tools"


def integrate(story):
    payoffs = json.loads((ROOT / "payoff_contracts.json").read_text(encoding="utf-8"))
    by = {s["Id"]: s for s in story["Scenes"]}
    derived = story.setdefault("Derived", {})
    forbids = story.setdefault("DerivedForbids", {})
    derived.update(payoffs.get("derived", {}))
    forbids.update(payoffs.get("forbids", {}))
    for field, readers in payoffs.get("native_readers", {}).items():
        story.setdefault(field, {}).update(readers)
    if "eliandra" in story["Relationships"]:
        losses = story["Relationships"]["eliandra"].setdefault("UnavailableFlags", [])
        if "eliandra.attacked" not in losses:
            losses.append("eliandra.attacked")
    story.setdefault("Latches", {}).update(payoffs.get("latches", {}))
    for surface in payoffs.get("additional_scene_gates", []):
        if surface["scene"] in by:
            for key in surface["requires"]:
                require(by[surface["scene"]], key)
    for surface in payoffs.get("additional_presence_gates", []):
        if surface["presence"] in story.get("Presences", {}):
            for key in surface["requires"]:
                require(story["Presences"][surface["presence"]], key)
    for route, contract in payoffs["routes"].items():
        if route not in story["Relationships"]:
            continue
        ordinary = route + ".payoff.ordinary"
        derived[ordinary] = contract["ordinary"]
        ordinary_revokers = contract.get("ordinary_revokers", contract["revokers"])
        if ordinary_revokers:
            forbids[ordinary] = list(dict.fromkeys([*forbids.get(ordinary, []), *ordinary_revokers]))
        derived[route + ".payoff.partner"] = contract["partner"]
        late = route + ".trickster.late_committed"
        if late in derived and contract["late"]:
            # Preserve every existing route/negative guard in each late arm.
            guards = list(dict.fromkeys(k for g in derived[late] for k in g
                if ".outcome." in k or ".without." in k or ".refusal_lifted." in k))
            derived[late] = [list(dict.fromkeys(g + guards)) for g in contract["late"]]
            if contract["revokers"]:
                forbids[late] = list(dict.fromkeys([*forbids.get(late, []), *contract["revokers"]]))
        for surface in contract["surfaces"]:
            if surface["scene"] in by:
                target = by[surface["scene"]]
                if "choice" in surface:
                    node = next(n for n in target["Nodes"] if n["Id"] == surface["node"])
                    target = node["Choices"][surface["choice"]]
                require(target, surface["predicate"])
        for surface in contract.get("book_surfaces", []):
            entries = story.get("Books", {}).get(surface["book"], {}).get("Entries", [])
            entry = next((e for e in entries if e["Id"] == surface["entry"]), None)
            if entry is not None:
                require(entry, surface["predicate"])
        # Last Call/native partner readers retain their own alternatives, but
        # an ordinary commitment arm now reads its specific earned history.
        native_partner = route + ".trickster.partner"
        if native_partner in derived:
            committed = story["Relationships"][route]["CommittedFlag"]
            derived[native_partner] = [[ordinary if k == committed else k for k in g] for g in derived[native_partner]]
        eligible = route + ".harem.eligible"
        if eligible in derived:
            committed = story["Relationships"][route]["CommittedFlag"]
            derived[eligible] = [[ordinary if k == committed else k for k in g] for g in derived[eligible]]
    # The acquisition agreement is a second route's commitment bit. Its
    # co-produced personal-risk acceptance guards the merged Nocticula seat.
    for key in ("nocticula.harem.eligible", "nocticula.trickster.partner"):
        if key in derived:
            derived[key] = [["nocticula.acquisition.payoff.ordinary" if k == "noct.acq.renewed_agreement" else k
                             for k in group] for group in derived[key]]
    for surface in payoffs["paragraphs"]:
        if surface["scene"] not in by:
            continue
        node = next(n for n in by[surface["scene"]]["Nodes"] if n["Id"] == surface["node"])
        block = node["Paragraphs"][surface["paragraph"]]
        for key in surface["requires"]:
            require(block, key)
        block["Forbids"] = list(dict.fromkeys([*block.get("Forbids", []), *surface["forbids"]]))
        for group in surface.get("any_groups", []):
            if group not in block.setdefault("AnyGroups", []):
                block["AnyGroups"].append(group)
    # Integrated stance outcomes keep their own acceptance and refusal guards.
    # These are existing route receipts, never new conditions on legacy exits.
    for contract in payoffs.get("stance_guards", []):
        for sid, nid, index in contract["surfaces"]:
            node = next(n for n in by[sid]["Nodes"] if n["Id"] == nid)
            block = node["Paragraphs"][index]
            for key in contract["requires"]:
                require(block, key)
            block["Forbids"] = list(dict.fromkeys([*block.get("Forbids", []), *contract["forbids"]]))
            for group in contract["any_groups"]:
                if group not in block.setdefault("AnyGroups", []):
                    block["AnyGroups"].append(group)
    # The late coda must read the effective yes, including later revokers.
    for node in by.get("arsinoe.lastcall.page", {}).get("Nodes", []):
        for paragraph in node.get("Paragraphs", []):
            if "arsinoe.trickster.late_committed" in paragraph.get("Requires", []):
                paragraph["Forbids"] = list(dict.fromkeys([*paragraph.get("Forbids", []), "arsinoe.future_spoken"]))
    departures = json.loads((ROOT / "departure_contracts.json").read_text(encoding="utf-8"))
    install(story, departures)
    for surface in departures.get("choice_rewrites", []):
        if surface["scene"] not in by:
            continue
        node = next(n for n in by[surface["scene"]]["Nodes"] if n["Id"] == surface["node"])
        choice = node["Choices"][surface["choice"]]
        choice[surface["field"]] = [surface["new"] if k == surface["old"] else k for k in choice.get(surface["field"], [])]

    for surface in departures.get("additional_choice_gates", []):
        node = next(n for n in by[surface["scene"]]["Nodes"] if n["Id"] == surface["node"])
        for key in surface["requires"]:
            require(node["Choices"][surface["choice"]], key)

    # Retain the shipped answer negatives even where an earlier integration
    # pass classified their theological reference as an optional reaction.
    for surface in departures.get("preserve_choice_forbids", []):
        node = next(n for n in by[surface["scene"]]["Nodes"] if n["Id"] == surface["node"])
        choice = node["Choices"][surface["choice"]]
        choice["Forbids"] = list(dict.fromkeys([*choice.get("Forbids", []), *surface["forbids"]]))

    # Native selectors and their replacements must read the same final gates.
    # Keep every existing selector alternative and negative intact.
    from tools.native_contradictions import ending_contracts, ending_when
    for row in ending_contracts()["Rows"]:
        spec = story.get(row["Field"], {}).get(row["Target"])
        if spec is None:
            continue
        outcomes = [by[key] for key in row["Outcomes"]]
        if row["Field"] == "NativeEpilogueSuppressions":
            spec["When"] = [group for outcome in outcomes for group in ending_when(outcome)]
        else:
            for variant, outcome in zip([spec, *spec.get("Variants", [])], outcomes):
                variant["When"] = ending_when(outcome)
    for spec in story.get("NativeEpilogueEdits", {}).values():
        for variant in [spec, *spec.get("Variants", [])]:
            scene = by.get(variant.get("Replacement"), {})
            gates = [key for key in scene.get("Requires", [])
                     if ".payoff." in key or key.endswith((".present_now", ".reachable_by_letter"))]
            variant["When"] = [list(dict.fromkeys([*group, *gates])) for group in variant.get("When", [])]

    # Job 4 runs after indexed contracts: preserve their historical paragraph slots.
    from storylines import endings_job4
    endings_job4.integrate(story)

    # J01: contact classification follows the final loss/return epoch registry.
    from storylines import contract_j01
    contract_j01.install(story)
