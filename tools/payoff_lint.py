"""Class A: declarative earned-payoff contracts and their revokers.

Unresolved route writing/receipt defects are printed separately as REVIEW;
strict mode fails on missing inventory or missing mechanical contract gates.
"""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.crossroute_checks.common import Proof, lit, verify

CONTRACT = Path(__file__).with_name("payoff_contracts.json")


def contracts():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def check(story, data=None):
    data = data or contracts()
    from tools.harem_w5_readers_lint import check as check_w5_readers
    errors = check_w5_readers(story)
    by = {s["Id"]: s for s in story.get("Scenes", [])}
    model = verify.Model(story)
    proof = Proof(model)
    for key, sources in data.get("latches", {}).items():
        if story.get("Latches", {}).get(key) != sources:
            errors.append(key + ": missing declared observed-history latch")
    for field, readers in data.get("native_readers", {}).items():
        for key, source in readers.items():
            if story.get(field, {}).get(key) != source:
                errors.append(key + ": missing verified native observation")
    for key, groups in data.get("derived", {}).items():
        if story.get("Derived", {}).get(key) != groups:
            errors.append(key + ": missing declared earned predicate")
    for surface in data.get("additional_scene_gates", []):
        scene = by.get(surface["scene"])
        if scene is None or not set(surface["requires"]) <= set(scene.get("Requires", [])):
            errors.append(surface["scene"] + ": missing observed-death gate")
    for surface in data.get("additional_presence_gates", []):
        presence = story.get("Presences", {}).get(surface["presence"])
        if presence is None or not set(surface["requires"]) <= set(presence.get("Requires", [])):
            errors.append(surface["presence"] + ": coffin bootstrap lacks observed death")
    for route, contract in data["routes"].items():
        if route not in story.get("Relationships", {}):
            continue
        for producer in contract.get("producers", []):
            if "effects" not in producer:
                continue  # upstream history inventory includes retired answers
            node = next((n for n in by.get(producer["scene"], {}).get("Nodes", [])
                         if n["Id"] == producer["node"]), {})
            choices = node.get("Choices", [])
            index = producer["choice"]
            if index >= len(choices) or choices[index].get("Set", []) != producer["effects"]:
                errors.append(f"{route}/{producer['scene']}/{producer['node']}/choice[{index}]: altered integrated acceptance receipts")
        key = route + ".payoff.ordinary"
        if story.get("Derived", {}).get(key) != contract["ordinary"]:
            errors.append(f"{route}/Derived: earned ordinary history differs from contract")
        if story.get("Derived", {}).get(route + ".payoff.partner") != contract["partner"]:
            errors.append(f"{route}/Derived: partner alternatives differ from the earned contract")
        ordinary_revokers = contract.get("ordinary_revokers", contract["revokers"])
        for group in story.get("Derived", {}).get(key, []):
            conflicts = set(group) & set(story.get("DerivedForbids", {}).get(key, []))
            if conflicts:
                errors.append(f"{route}/{key}: earned arm also forbids {sorted(conflicts)}")
        for revoker in ordinary_revokers:
            if not proof.implies(lit(key), lit(revoker, False)):
                errors.append(f"{route}/{key}: permits later revoker {revoker}")
        late = route + ".trickster.late_committed"
        if late in story.get("Derived", {}):
            for revoker in contract["revokers"]:
                if not proof.implies(lit(late), lit(revoker, False)):
                    errors.append(f"{route}/{late}: permits revoker {revoker}")
            for group in story["Derived"][late]:
                if not any(set(earned) <= set(group) for earned in contract["late"]):
                    errors.append(f"{route}/{late}: arm lacks its earned history")
        callable_contract = contract.get("callable_contract")
        if callable_contract:
            call = callable_contract["predicate"]
            if story.get("Derived", {}).get(call) != callable_contract["earned"]:
                errors.append(f"{route}/{call}: lacks its specific incurred cost/deed")
            if story.get("DerivedOpenRoutes", {}).get(call, []) != callable_contract["open_routes"]:
                errors.append(f"{route}/{call}: ignores current route availability")
            if not set(callable_contract["revokers"]) <= set(story.get("DerivedForbids", {}).get(call, [])):
                errors.append(f"{route}/{call}: ignores a resolved debt or revoker")
        for surface in contract["surfaces"]:
            scene = by.get(surface["scene"])
            target = scene or {}
            if "choice" in surface:
                node = next((n for n in target.get("Nodes", []) if n["Id"] == surface["node"]), {})
                choices = node.get("Choices", [])
                target = choices[surface["choice"]] if surface["choice"] < len(choices) else {}
            if scene is None or surface["predicate"] not in target.get("Requires", []):
                errors.append(f"{route}/{surface['scene']}: missing payoff contract {surface['predicate']}")
        registered = {surface["scene"] for surface in contract["surfaces"] + contract.get("absence_surfaces", [])}
        committed = story["Relationships"][route]["CommittedFlag"]
        for scene in story.get("Scenes", []):
            belongs = scene.get("Relationship", "tirabade") == route or scene["Id"].startswith(route + ".") or route == "minagho_chivarro" and scene["Id"].startswith("minachiv.")
            if not belongs or not ("epilogue" in scene["Id"] or "lastcall.page" in scene["Id"] or scene.get("Owner", "").endswith("Epilogue")):
                continue
            positive = scene.get("Requires", []) + scene.get("RequiresAny", []) + sum(scene.get("RequiresAnyGroups", []), [])
            if any(k in positive for k in (committed, late, route + ".trickster.partner")) and scene["Id"] not in registered:
                errors.append(f"{route}/{scene['Id']}: unclassified romantic payoff surface")
        for surface in contract.get("guest_surfaces", []) + contract.get("book_surfaces", []):
            entry = next((e for e in story.get("Books", {}).get(surface["book"], {}).get("Entries", []) if e["Id"] == surface["entry"]), {})
            if surface["predicate"] not in entry.get("Requires", []):
                errors.append(f"{route}/{surface['entry']}: missing earned book-entry history")
        native_partner = route + ".trickster.partner"
        if any(story["Relationships"][route]["CommittedFlag"] in g for g in story.get("Derived", {}).get(native_partner, [])):
            errors.append(f"{route}/{native_partner}: uses coarse commitment instead of earned history")
        eligible = route + ".harem.eligible"
        if eligible in story.get("Derived", {}):
            committed = story["Relationships"][route]["CommittedFlag"]
            coarse = {r["CommittedFlag"] for r in story["Relationships"].values()}
            if any(coarse.intersection(g) for g in story["Derived"][eligible]):
                errors.append(f"{route}/{eligible}: uses coarse commitment instead of earned history")
    for surface in data["paragraphs"]:
        if surface["route"] not in story.get("Relationships", {}):
            continue
        scene = by.get(surface["scene"])
        node = next((n for n in (scene or {}).get("Nodes", []) if n["Id"] == surface["node"]), {})
        paragraphs = node.get("Paragraphs", [])
        label = f"{surface['route']}/{surface['scene']}/{surface['node']}/paragraph[{surface['paragraph']}]"
        if len(paragraphs) <= surface["paragraph"]:
            errors.append(label + ": missing payoff surface")
            continue
        paragraph = paragraphs[surface["paragraph"]]
        if (not set(surface["requires"]) <= set(paragraph.get("Requires", []))
                or not set(surface["forbids"]) <= set(paragraph.get("Forbids", []))
                or any(group not in paragraph.get("AnyGroups", []) for group in surface.get("any_groups", []))):
            errors.append(label + ": missing deed or revoker")
    for target, spec in story.get("NativeEpilogueEdits", {}).items():
        for index, variant in enumerate([spec, *spec.get("Variants", [])]):
            scene = by.get(variant.get("Replacement"), {})
            gates = [key for key in scene.get("Requires", []) if ".payoff." in key]
            if any(not set(gates) <= set(group) for group in variant.get("When", [])):
                errors.append(f"{scene.get('Relationship', 'tirabade')}/{target}/variant[{index}]: native selector lacks earned payoff")
    registered_stances = set()
    for contract in data.get("stance_guards", []):
        for sid, nid, index in contract["surfaces"]:
            registered_stances.add((sid, nid, index))
            node = next((n for n in by.get(sid, {}).get("Nodes", []) if n["Id"] == nid), {})
            blocks = node.get("Paragraphs", [])
            block = blocks[index] if index < len(blocks) else {}
            if (not set(contract["requires"]) <= set(block.get("Requires", []))
                    or not set(contract["forbids"]) <= set(block.get("Forbids", []))
                    or any(group not in block.get("AnyGroups", []) for group in contract["any_groups"])
                    or index >= len(blocks)):
                errors.append(f"{sid}/{nid}/paragraph[{index}]: missing stance acceptance/history guard")
    for scene in story.get("Scenes", []):
        for node in scene.get("Nodes", []):
            for index, block in enumerate(node.get("Paragraphs", [])):
                keys = block.get("Requires", []) + block.get("Forbids", []) + sum(block.get("AnyGroups", []), [])
                if any(".partner_stance." in k or ".partner." in k or ".partner_state." in k for k in keys):
                    if (scene["Id"], node["Id"], index) not in registered_stances:
                        errors.append(f"{scene['Id']}/{node['Id']}/paragraph[{index}]: unclassified stance payoff")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", default=str(CONTRACT.parent.parent / "development/Story.json"))
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    story = json.loads(Path(args.story).read_text(encoding="utf-8-sig"))
    data = contracts()
    errors = check(story, data)
    for error in errors:
        print("HARD", error)
    for route, contract in data["routes"].items():
        for residual in contract["residuals"]:
            print("REVIEW", route + ":", residual)
    print(f"Payoff contracts: {len(data['routes'])} routes; {len(errors)} hard failures")
    return int(args.strict and bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
