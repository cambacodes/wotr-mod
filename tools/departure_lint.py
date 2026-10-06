"""Class B: inventory of current presence, permitted letters and explicit absences."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
CONTRACT = Path(__file__).with_name("departure_contracts.json")


def contracts():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def check(story, data=None):
    data = data or contracts()
    errors = []
    by = {s["Id"]: s for s in story.get("Scenes", [])}
    for key, groups in data.get("return_predicates", {}).items():
        if story.get("Derived", {}).get(key) != groups:
            errors.append(key + ": missing declared physical survival predicate")
    for key, groups in data.get("absence_predicates", {}).items():
        if story.get("Derived", {}).get(key) != groups or story.get("DerivedForbids", {}).get(key, []) != data.get("absence_forbids", {}).get(key, []):
            errors.append(key + ": altered explicit absence report")
    for surface in data.get("additional_choice_gates", []):
        node = next((n for n in by.get(surface["scene"], {}).get("Nodes", []) if n["Id"] == surface["node"]), {})
        choices = node.get("Choices", [])
        if len(choices) <= surface["choice"] or not set(surface["requires"]) <= set(choices[surface["choice"]].get("Requires", [])):
            errors.append(surface["scene"] + ": missing current departure report gate")
    for surface in data.get("preserve_choice_forbids", []):
        scene = by.get(surface["scene"], {})
        node = next((n for n in scene.get("Nodes", []) if n["Id"] == surface["node"]), {})
        choices = node.get("Choices", [])
        if len(choices) <= surface["choice"] or not set(surface["forbids"]) <= set(choices[surface["choice"]].get("Forbids", [])):
            errors.append(surface["scene"] + ": weakened shipped answer negative")
    for woman, contract in data["women"].items():
        route = contract["relationship"]
        if route not in story.get("Relationships", {}):
            continue
        epoch = story.get("DepartureEpochs", {}).get(woman)
        if not epoch or epoch.get("Losses") != contract["losses"] or epoch.get("Overrides") != contract["overrides"]:
            errors.append(f"{woman}/DepartureEpochs: missing or altered loss/return contract")
        if epoch and (epoch.get("Returns") != contract["returns"] or epoch.get("NativeClearReturns") != contract.get("native_clear_returns", {})):
            errors.append(f"{woman}/DepartureEpochs: altered return provenance")
        if epoch and epoch.get("ReturnTriggers", {}) != contract.get("return_triggers", {}):
            errors.append(f"{woman}/DepartureEpochs: altered earned return event sources")
        if epoch and epoch.get("AdditionalRelationships", []) != contract.get("additional_relationships", []):
            errors.append(f"{woman}/DepartureEpochs: altered shared-household availability")
        for participant_route in [route, *contract.get("additional_relationships", [])]:
            flags = story["Relationships"][participant_route].get("EpochUnavailableFlags", [])
            seats = data.get("seat_epoch_guards", {}).get(participant_route, [])
            if seats:
                guard = participant_route + ".epoch_unavailable"
                if woman not in seats or guard not in flags or story.get("Derived", {}).get(guard) != [[seat + ".epoch_unavailable" for seat in seats]]:
                    errors.append(f"{woman}/{participant_route}: ignores current independent seat epochs")
            elif woman + ".epoch_unavailable" not in flags:
                errors.append(f"{woman}/{participant_route}: ignores current departure epoch")
        key = woman + ".present_now"
        if woman + ".epoch_unavailable" not in story.get("DerivedForbids", {}).get(key, []):
            errors.append(f"{woman}/{key}: lacks current epoch guard")
        inputs = list(contract.get("body_requires", []))
        for i, loss in enumerate(contract["losses"]):
            clear = key + ".clear." + str(i)
            if story.get("Derived", {}).get(clear) != [["availability.observed"]] or story.get("DerivedForbids", {}).get(clear) != [loss]:
                errors.append(f"{woman}/{clear}: altered current loss reader")
            back = contract["overrides"].get(loss)
            if back:
                lifted = key + ".loss." + str(i)
                if story.get("Derived", {}).get(lifted) != [[clear], [back]]:
                    errors.append(f"{woman}/{lifted}: altered nominated return")
                inputs.append(lifted)
            else:
                inputs.append(clear)
        if story.get("Derived", {}).get(key) != [["availability.observed", *inputs]]:
            errors.append(f"{woman}/{key}: altered body or loss requirements")
        letter = woman + ".reachable_by_letter"
        permitted_groups = [[key]]
        for i, permitted in enumerate(contract.get("letter_terms", []), 1):
            departed = letter + ".departed." + str(i)
            if story.get("Derived", {}).get(departed) != [permitted["requires"]] or story.get("DerivedForbids", {}).get(departed) != permitted["forbids"]:
                errors.append(f"{woman}/{departed}: altered living departure terms")
            permitted_groups.append([departed])
        if story.get("Derived", {}).get(letter) != permitted_groups:
            errors.append(f"{woman}/{letter}: permits uncontracted correspondence")
        for surface in contract["surfaces"]:
            scene = by.get(surface["scene"])
            gate = woman + (".reachable_by_letter" if surface.get("letter") else ".present_now")
            target = scene or {}
            if "paragraph" in surface or "choice" in surface:
                node = next((n for n in target.get("Nodes", []) if n["Id"] == surface["node"]), {})
                field = "choice" if "choice" in surface else "paragraph"
                blocks = node.get("Choices" if field == "choice" else "Paragraphs", [])
                target = blocks[surface[field]] if len(blocks) > surface[field] else {}
            if gate not in target.get("Requires", []):
                errors.append(f"{woman}/{surface['scene']}: missing {gate}")
        registered = {s["scene"] for s in contract["surfaces"] + contract["absence_variants"]}
        for scene in story.get("Scenes", []):
            if scene.get("Relationship") in [route, *contract.get("additional_relationships", [])] and scene["Id"] not in registered:
                # Named solo pages of pair relationships are registered only for
                # the woman actually there; their other seat is explicitly absent.
                if route == "minagho_chivarro" and any(
                    scene["Id"] in {s["scene"] for s in seat["surfaces"] + seat["absence_variants"]}
                    for seat in data["women"].values() if seat["relationship"] == route
                ):
                    continue
                errors.append(f"{woman}/{scene['Id']}: unclassified presence surface")
        for name in contract["presences"]:
            presence = story.get("Presences", {}).get(name)
            if presence is None:
                errors.append(f"{woman}/{name}: missing inventoried presence")
            elif name not in contract.get("acquisition_presences", []) and key not in presence.get("Requires", []):
                errors.append(f"{woman}/{name}: lacks current availability")
            elif name in contract.get("acquisition_presences", []) and woman + ".epoch_redeparted" not in presence.get("Forbids", []):
                errors.append(f"{woman}/{name}: bootstrap answers a later loss")
        for book in story.get("Books", {}).values():
            for entry in book.get("Entries", []):
                if entry["Id"] in contract["guests"] and key not in entry.get("Requires", []):
                    errors.append(f"{woman}/{entry['Id']}: lacks current availability")
        registered_books = set(contract["guests"]) | {v["entry"] for v in contract.get("book_absence_variants", [])}
        for book in story.get("Books", {}).values():
            for entry in book.get("Entries", []):
                if (entry["Id"] in ("guest." + woman, "owed." + woman) or entry["Id"].startswith(("guest." + woman + ".", "owed." + woman + "."))) and entry["Id"] not in registered_books:
                    errors.append(f"{woman}/{entry['Id']}: unclassified living/history book surface")
    for surface in data.get("choice_rewrites", []):
        scene = by.get(surface["scene"], {})
        node = next((n for n in scene.get("Nodes", []) if n["Id"] == surface["node"]), {})
        choices = node.get("Choices", [])
        if len(choices) <= surface["choice"] or surface["new"] not in choices[surface["choice"]].get(surface["field"], []):
            errors.append(f"{surface['scene']}/{surface['node']}/{surface['choice']}: historical return still depicts departed participant")
    for target, spec in story.get("NativeEpilogueEdits", {}).items():
        for index, variant in enumerate([spec, *spec.get("Variants", [])]):
            scene = by.get(variant.get("Replacement"), {})
            gates = [key for key in scene.get("Requires", []) if key.endswith((".present_now", ".reachable_by_letter"))]
            if any(not set(gates) <= set(group) for group in variant.get("When", [])):
                errors.append(f"{scene.get('Relationship', 'tirabade')}/{target}/variant[{index}]: native selector lacks current availability")
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
    for woman, contract in data["women"].items():
        for residual in contract.get("residuals", []):
            print("REVIEW", woman + ":", residual)
    print(f"Departure contracts: {len(data['women'])} women; {len(errors)} hard failures")
    return int(args.strict and bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
