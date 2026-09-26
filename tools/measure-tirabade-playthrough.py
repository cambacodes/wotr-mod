"""Count coherent Tirabade source paths, not Unity or ending-dispatch verification.

Counts visited prose and chosen answers once, with exactly one selected ending.
Assumes living present wives, a living Commander, correct locations and waits.
Native chapter and mythic history is explicit; no native flags are authored here.
"""
import argparse
import hashlib
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / "tools/measure-konomi-playthrough.py"))
allowed, relevant, words = BASE["allowed"], BASE["relevant"], BASE["words"]


def walk(scene, flags):
    nodes = {n["Id"]: n for n in scene["Nodes"]}

    def visit(node_id, current, count, trace):
        node = nodes[node_id]
        for i, choice in enumerate(node["Choices"]):
            if choice.get("Abort") or not allowed(choice, current):
                continue
            after = current | set(choice.get("Set", []))
            total = count + words(node["Text"]) + words(choice["Text"])
            check = choice.get("Check")
            destinations = [check["Success"], check["Failure"]] if check else [choice.get("Next")]
            for destination in destinations:
                path = trace + [(scene["Id"], node_id, i, destination)]
                if destination:
                    yield from visit(destination, after, total, path)
                else:
                    yield after | {scene["Id"]}, total, path

    yield from visit(scene["Nodes"][0]["Id"], flags, 0, [])


def measure(scenes, sequence, initial):
    states = {frozenset(initial): [(0, [])]}
    chapter = 1
    for index, event in enumerate(sequence):
        if isinstance(event, dict):
            chapter = event.get("chapter", chapter)
            states = {frozenset((set(flags) - set(event.get("remove", []))) | set(event.get("add", []))): values
                      for flags, values in states.items()}
            continue
        scene = scenes[event]
        assert scene.get("MinChapter", 0) <= chapter <= scene.get("MaxChapter", 99)
        assert not scene.get("Chapters") or chapter in scene["Chapters"]
        future = relevant([scenes[x] for x in sequence[index + 1:] if isinstance(x, str)]) | {"closed"}
        out = {}
        for flags, extrema in states.items():
            if not allowed(scene, flags) or ("closed" in flags and not event.startswith("ending_")):
                continue
            for after, count, trace in walk(scene, set(flags)):
                key = frozenset(after & future)
                for prior_count, prior_trace in extrema:
                    values = out.get(key, []) + [(prior_count + count, prior_trace + trace)]
                    out[key] = [min(values, key=lambda x: x[0]), max(values, key=lambda x: x[0])]
        if not out:
            raise ValueError(f"No eligible completed trajectory at {event}")
        states = out
    values = [v for pair in states.values() for v in pair]
    return min(values, key=lambda x: x[0]), max(values, key=lambda x: x[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--read-path", help="Print maximum selected prose for one named scenario")
    parser.add_argument("--scenes", nargs="*", help="Restrict printed prose to these scene IDs")
    args = parser.parse_args()
    raw = args.story.read_bytes()
    scenes = {s["Id"]: s for s in json.loads(raw)["Scenes"] if s.get("Relationship", "tirabade") == "tirabade"}
    early = ["a_cup", "i_watch", {"chapter": 2, "remove": ["chapter_one"]}, "a_errand", "i_hands", {"chapter": 3}]
    middle = "a_roof i_respite a_crossing i_crossing a_morning i_morning reckoning a_truth i_truth table ordinary a_self i_self".split()
    campaign = [sid for sid in scenes if sid.startswith("three_") and sid not in {"three_choose_days", "three_more_days", "three_kept_days"}]
    abroad = ["departure", {"chapter": 4}, "abyss_letter", "abyss_dream", {"chapter": 5}]
    late = "return power future shared_night".split()
    scenarios = {
        "developed_with_abyss": early + middle + campaign + abroad + late + ["three_kept_days", "last_watch", "ending_together"],
        "short_with_abyss": early + middle + abroad + late + ["three_choose_days", "last_watch", "ending_promised"],
        "late_install_developed": [{"chapter": 5}] + [x for x in early if isinstance(x, str)] + middle + campaign + late + ["three_kept_days", "last_watch", "ending_together"],
        "short_then_catchup": early + middle + abroad + late + ["three_choose_days", "last_watch", "three_more_days"] + campaign + ["three_kept_days", "ending_together"],
        "honest_parting": early + middle + ["parting", "ending_apart"],
    }
    print("Story SHA256:", hashlib.sha256(raw).hexdigest().upper())
    print("Tirabade subset SHA256:", hashlib.sha256(json.dumps(list(scenes.values()), sort_keys=True, separators=(",", ":")).encode()).hexdigest().upper())
    for name, sequence in scenarios.items():
        ids = [x for x in sequence if isinstance(x, str)]
        assert len(ids) == len(set(ids)), "A scene would be credited twice"
        assert sum(x.startswith("ending_") for x in ids) == 1, "Expected exactly one ending"
        initial = {"trickster", "encouraged"} | ({"chapter_one"} if not name.startswith("late_install") else set())
        shortest, longest = measure(scenes, sequence, initial)
        print(name, shortest[0], longest[0], "selected words;", sum(isinstance(x, str) for x in sequence), "scenes")
        if args.read_path == name:
            for sid, nid, i, _ in longest[1]:
                if args.scenes and sid not in args.scenes:
                    continue
                node = next(n for n in scenes[sid]["Nodes"] if n["Id"] == nid)
                print(f"\n{sid}/{nid}\n{node['Text']}\n> {node['Choices'][i]['Text']}")


if __name__ == "__main__":
    main()
