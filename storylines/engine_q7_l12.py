"""eng7-l12: authored staging and ending corrections, applied after route assembly.

These are text/venue variants of existing events, not new outcome devices.
Original scene/node/answer order is retained. Native finale facts select factual
paragraphs; their neutral siblings keep earned endings available in other worlds.
"""
import copy
import json
from pathlib import Path
from tools.player_text_lint import narration_free

ROOT = Path(__file__).resolve().parents[1]
DEAD = "engine.l12.commander_unreturned"


def inventory(name):
    return json.loads((ROOT / "tools" / name).read_text(encoding="utf-8"))


def add(record, field, key):
    record[field] = list(dict.fromkeys([*(record.get(field) or []), key]))


def variant(node, paragraph, fact, neutral):
    """Keep the old paragraph position; append the disjoint authored alternative."""
    other = copy.deepcopy(paragraph)
    other["Text"] = neutral
    add(paragraph, "Requires", fact)
    add(other, "Forbids", fact)
    node.setdefault("Paragraphs", []).append(other)


def requires_fact(spec, fact, derived, seen=()):
    """Leave already-correct factual blocks intact, including derived witnesses."""
    def implies(key):
        if key == fact:
            return True
        if key in seen or key not in derived:
            return False
        return bool(derived[key]) and all(
            any(requires_fact({"Requires": [source]}, fact, derived, (*seen, key)) for source in group)
            for group in derived[key])
    return any(implies(key) for key in spec.get("Requires", []))


def integrate(payload):
    # Route appenders may share COMMON paragraph dictionaries between pages.
    # Each consumer needs its own factual and bereavement alternatives.
    for scene in payload["Scenes"]:
        scene["Nodes"] = [copy.deepcopy(node) for node in scene["Nodes"]]
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    # Existing Derived/DerivedForbids semantics express survival without a new
    # runtime mechanic. Paragraphs do not support ForbidOverrides.
    payload.setdefault("Derived", {})[DEAD] = [["sacrifice"]]
    payload.setdefault("DerivedForbids", {})[DEAD] = ["trickster.commander_back"]

    for contract in inventory("location_inventory_contracts.json")["venues"]:
        scene = scenes[contract["scene"]]
        scene["Areas"] = contract["areas"]
        if "chapters" in contract:
            scene["Chapters"] = contract["chapters"]

    # A location-neutral aftermath covers both the Drezen and Threshold roads.
    # No new scene or chapter-dependent outcome can strand an old continuation.
    night = scenes["horzalah.trickster.late.at_night"]
    for node in night["Nodes"]:
        if "whole citadel knows" in node["Text"]:
            node["Text"] = node["Text"].replace("whole citadel knows", "whole watch knows").replace(
                "Two of the lords who lend the crusade their men write to ask whether their sons are safer at home.",
                "Two young knights ask their sergeant whether the Commander will survive the next night.")
        if node["Id"] == "no_priest":
            node["Text"] = node["Text"].replace("My people in your city", "My people among your sentries")
    for scene in payload["Scenes"]:
        for node in scene["Nodes"]:
            for paragraph in node.get("Paragraphs") or []:
                if "night a demon walked past every sentry in the citadel" in paragraph["Text"]:
                    paragraph["Text"] = paragraph["Text"].replace("in the citadel", "at the Commander's quarters")

    # All authored visitors stay visitors. Only the native companion's volume
    # promises to march; this includes both the first and replacement volume.
    for suffix in ("_visitor", "_arcade"):
        for node in scenes["nenio.folio.volume_one" + suffix]["Nodes"]:
            if node["Id"] in ("give", "give_new"):
                node["Text"] = node["Text"].replace("Because I am going into the same battle as you, and if I am... if I become irrelevant,",
                    "Because I am staying in Drezen, and if this city becomes irrelevant,")
    # A native companion can be nearby at Threshold. Do not infer current
    # presence from a farewell heard earlier; the visitor predicate is the
    # implemented placement contract. Neutral distance covers native party splits.
    page = scenes["nenio.lastcall.page"]["Nodes"][0]
    original = page["Text"]
    page["Text"] = "{n}Nenio headed the last sheet of the war THRESHOLD, OBSERVATIONS.{/n}"
    page.setdefault("Paragraphs", []).extend([
        dict(Text=original, Requires=["nenio.trickster.visitor"]),
        dict(Text=original.replace("on the roof of the citadel in Drezen with a spyglass, a stopwatch", "watching Threshold with a stopwatch"),
             Forbids=["nenio.trickster.visitor"]),
    ])
    for paragraph in page["Paragraphs"]:
        paragraph["Text"] = paragraph["Text"].replace(
            "Far off, on a roof in Drezen, a kitsune who never raised her voice stood up and shouted back,",
            "Nenio stood up and shouted back,").replace(
            "loud enough that a sentry on the next tower dropped his spear", "loud enough to startle a sentry")
    call = scenes["nenio.lastcall.call"]["Nodes"][0]
    call["Text"] = call["Text"].replace("into the dark where Drezen is", "into the dark").replace(
        "very far off, precise", "precise")

    # AeonFinalWorld erases the courtship. Native Cue_0024 leaves Irabeth
    # unmarried and Cue_0021 leaves Anevia dead; no Trickster return alters it.
    scenes["irabeth.ending_aeon"]["Nodes"][0]["Text"] = (
        "{n}When the Worldwound's history was rewritten, the evenings Irabeth and the Commander had spent together went with it. "
        "In the world that followed, a half-orc paladin kept her post in Kenabres and never started a family. "
        "The spy she might have married died far away, in the River Kingdoms. They never met.{/n}")

    world = inventory("epilogue_world_inventory_contracts.json")
    for scene in payload["Scenes"]:
        if not scene.get("Owner", "").endswith("Epilogue") or scene["Owner"] == "AeonEpilogue":
            continue
        for node in scene["Nodes"]:
            # Authored neutral lead-ins retain the entire ending on every
            # legitimate finale; only asserted factual paragraphs are gated.
            if not requires_fact(scene, "ending.wound_closed", payload["Derived"]):
                for old, new in world["neutral_phrases"].items():
                    node["Text"] = node["Text"].replace(old, new)
            for paragraph in list(node.get("Paragraphs") or []):
                neutral = paragraph["Text"]
                for old, new in world["neutral_phrases"].items():
                    neutral = neutral.replace(old, new)
                if (neutral != paragraph["Text"]
                        and not requires_fact(scene, "ending.wound_closed", payload["Derived"])
                        and not requires_fact(paragraph, "ending.wound_closed", payload["Derived"])):
                    variant(node, paragraph, "ending.wound_closed", neutral)
                elif "rebuilt cathedral" in neutral:
                    # The attested cue proves the city, not this building.
                    paragraph["Text"] = neutral.replace("the rebuilt cathedral", "Kenabres as its streets were rebuilt")
                    variant(node, paragraph, "engine.l12.kenabres_rebuilding",
                            neutral.replace("the rebuilt cathedral", "the cathedral's old site"))
                elif "standing orders of the Crossroads of Worlds" in neutral:
                    variant(node, paragraph, "engine.l12.crossroads",
                            neutral.replace("standing orders of the Crossroads of Worlds", "orders they had drawn up together"))
    payload.setdefault("SeenCues", {})["engine.l12.kenabres_rebuilding"] = ["fc65929e0c9e4a9fa03309418c2d29bb"]
    payload["Derived"]["engine.l12.crossroads"] = [["ending.trickster_allplanes"], ["ending.trickster_allplanes_fw"]]

    # Guard the complete continuation class, including letters and friendship.
    # Historical costs stay visible after death; only living futures get variants.
    contracts = inventory("commander_block_contracts.json")["continuations"]
    for scene in payload["Scenes"]:
        if not scene.get("Owner", "").endswith("Epilogue"):
            continue
        for node in scene["Nodes"]:
            for paragraph in list(node.get("Paragraphs") or []):
                for contract in contracts:
                    if narration_free(paragraph["Text"]).startswith(contract["prefix"]):
                        other = copy.deepcopy(paragraph)
                        other["Text"] = "{n}" + contract["bereavement"] + "{/n}"
                        add(paragraph, "Forbids", DEAD)
                        add(other, "Requires", DEAD)
                        node["Paragraphs"].append(other)
                        break
