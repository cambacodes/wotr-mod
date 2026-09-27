"""Inventory authored story text without treating word volume as release approval.

Run with development/Story.json, or --self-test for the small counting check.
Existing game/RanRomance material is not credited by this tool.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re

SINGLE_CHARACTER_FLOOR = 21000

def normalize(text):
    return " ".join(re.sub(r"\{[^}]*\}|<[^>]*>", "", text).split())


def words(text):
    return len(re.findall(r"\b[^\W_]+(?:['’][^\W_]+)*\b", normalize(text)))


def inventory(story):
    routes = defaultdict(list)
    scenes = defaultdict(int)
    for scene in story["Scenes"]:
        route = scene.get("Relationship", "tirabade")
        scenes[route] += 1
        for node in scene["Nodes"]:
            routes[route].append(("prose", node["Text"]))
            routes[route].extend(("choice", choice["Text"]) for choice in node["Choices"])
    output = {}
    for route, segments in routes.items():
        unique = {normalize(text) for _, text in segments}
        raw = sum(words(text) for _, text in segments)
        distinct = sum(words(text) for text in unique)
        output[route] = {
            "planning_floor_words": SINGLE_CHARACTER_FLOOR * (2 if route in {"tirabade", "minagho_chivarro"} else 1),
            "scenes": scenes[route],
            "raw_words": raw,
            "prose_words": sum(words(text) for kind, text in segments if kind == "prose"),
            "choice_words": sum(words(text) for kind, text in segments if kind == "choice"),
            "distinct_segment_words": distinct,
            "exact_repeat_words": raw - distinct,
            "integrated_external_words": None,
            "attainable_playthrough_words": None,
            "full_route_approved": False,
        }
    return output


def self_test():
    repeated = {"Text": "{n}Two words.{/n}", "Choices": [{"Text": "Continue"}]}
    data = {"Scenes": [{"Relationship": "one", "Nodes": [repeated, repeated]},
                       {"Relationship": "two", "Nodes": [repeated]}]}
    measured = inventory(data)
    assert measured["one"]["raw_words"] == 6
    assert measured["one"]["distinct_segment_words"] == 3
    assert measured["two"]["distinct_segment_words"] == 3
    assert normalize("<b>{n}Two\n words.{/n}</b>") == "Two words."
    assert words("don't blue-green") == 3
    assert measured["one"]["attainable_playthrough_words"] is None
    print("PASS: formatting, repeated segments, route separation and unsupported-credit checks")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story", type=Path, nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.story is None:
        parser.error("provide a Story.json file or --self-test")
    raw = args.story.read_bytes()
    report = {
        "scope": "Authored prose and choices. Exact normalized whole-segment deduplication only; not semantic originality, reachable content, per-character attribution or quality approval.",
        "story_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "tokenizer": "Same as the RanRomance source audit: Unicode alphanumerics, internal apostrophes retained, hyphens split, underscores excluded; curly and angle markup removed; whitespace normalized.",
        "exclusions": ["titles", "journal metadata", "entry labels", "external game and RanRomance text"],
        "planning_floor_per_character": SINGLE_CHARACTER_FLOOR,
        "relationships": inventory(json.loads(raw)),
    }
    output = args.output or args.story.parent / "content-volume-inventory.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for route, data in report["relationships"].items():
        print(f"{route}: {data['raw_words']} raw words; {data['distinct_segment_words']} distinct-segment words; {data['scenes']} scenes; planning floor {data['planning_floor_words']}")
    print(f"Inventory only, no release approval: {output}")


if __name__ == "__main__":
    main()
