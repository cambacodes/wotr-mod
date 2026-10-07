"""Static W5 reader inventory; never installed as runtime paragraph-index gates."""
import json
from pathlib import Path


PREFIX = "household.readers.w5."
MANIFEST = Path(__file__).with_name("harem_w5_readers.json")


def check(story, data=None):
    # Authoring tests deliberately assemble a story without the optional rows.
    # Their native pages have different paragraph counts; do not write to them.
    if not any(key.startswith(PREFIX) for key in story.get("Derived", {})):
        return []
    data = data or json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = []
    by_id = {scene["Id"]: scene for scene in story.get("Scenes", [])}
    for key, spec in data["current_predicates"].items():
        if story.get("Derived", {}).get(key) != [spec["requires"]]:
            errors.append(key + ": current page/body/survival gates differ from inventory")
        if story.get("DerivedForbids", {}).get(key) != spec["forbids"]:
            errors.append(key + ": current loss gates differ from inventory")
        if story.get("DerivedOpenRoutes", {}).get(key) != spec["open_routes"]:
            errors.append(key + ": missing current route/epoch checks")
    alive = PREFIX + "commander.alive"
    clear = PREFIX + "commander.not_sacrificed"
    if (story.get("Derived", {}).get(alive) != [[clear], ["trickster.commander_back"]]
            or story.get("Derived", {}).get(clear) != [["availability.observed"]]
            or story.get("DerivedForbids", {}).get(clear) != ["sacrifice"]):
        errors.append(alive + ": missing scoped Commander survival check")
    classified = set()
    for surface in data["living"]:
        sid, nid, index = surface["scene"], surface["node"], surface["paragraph"]
        classified.add((sid, nid, index))
        scene = by_id.get(sid, {})
        node = next((node for node in scene.get("Nodes", []) if node["Id"] == nid), {})
        paragraphs = node.get("Paragraphs", [])
        if scene.get("Owner") != "Epilogue" or index >= len(paragraphs):
            errors.append(sid + ": missing classified Epilogue reader")
            continue
        paragraph = paragraphs[index]
        if (not set(surface["requires"]) <= set(paragraph.get("Requires", []))
                or not set(surface["forbids"]) <= set(paragraph.get("Forbids", []))
                or any(group not in paragraph.get("AnyGroups", []) for group in surface["any_groups"])):
            errors.append(sid + ": missing W5 deed/cost/current presence guard")
    for scene in story.get("Scenes", []):
        for node in scene.get("Nodes", []):
            for index, paragraph in enumerate(node.get("Paragraphs", [])):
                if (any(key.startswith(PREFIX) for key in paragraph.get("Requires", []))
                        and (scene["Id"], node["Id"], index) not in classified):
                    errors.append(scene["Id"] + ": unclassified W5 reader")
    books = {entry["Id"]: entry for entry in story.get("Books", {}).get("trickster.ledger", {}).get("Entries", [])}
    for surface in data["book_surfaces"]:
        entry = books.get(surface["entry"], {})
        lines = entry.get("Lines", [])
        if entry.get("Requires") != surface["requires"] or len(lines) != len(surface["lines"]):
            errors.append(surface["entry"] + ": missing historical/current Notes classification")
            continue
        for index, expected in enumerate(surface["lines"]):
            line = lines[index]
            if (line.get("Requires") != expected["requires"] or line.get("Forbids") != expected["forbids"]
                    or line.get("AnyGroups") != expected["any_groups"]):
                errors.append(surface["entry"] + ": missing deed/cost or stage/partner precedence")
    return errors
