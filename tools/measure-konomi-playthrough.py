"""Source-level selected Konomi trajectories, not Unity reachability certification.

Assumes a living embodied commander, sufficient waits and correct scene location.
Counts visited prose and chosen answers, including exactly one eligible ending.
Native fixture flags are supplied explicitly, never manufactured by story choices.
"""
import argparse
import hashlib
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
words = runpy.run_path(str(ROOT / "tools/measure-story-content.py"))["words"]


def allowed(item, flags):
    overrides = item.get("ForbidOverrides", {})
    return (all(x in flags for x in item.get("Requires", []))
            and (not item.get("RequiresAny") or any(x in flags for x in item["RequiresAny"]))
            and all(any(x in flags for x in group) for group in item.get("RequiresAnyGroups", []))
            and not any(x in flags and overrides.get(x) not in flags for x in item.get("Forbids", [])))


def walk(scene, flags):
    nodes = {n["Id"]: n for n in scene["Nodes"]}

    def visit(node_id, current, count, trace):
        node = nodes[node_id]
        for i, choice in enumerate(node["Choices"]):
            if choice.get("Abort") or not allowed(choice, current):
                continue
            after = current | set(choice.get("Set", []))
            if "konomi.closed" in after:
                continue
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


def relevant(scenes):
    keys = set()
    for scene in scenes:
        for item in [scene, *(c for n in scene["Nodes"] for c in n["Choices"])]:
            for name in ("Requires", "Forbids", "RequiresAny"):
                keys.update(item.get(name, []))
            keys.update(item.get("ForbidOverrides", {}).values())
            keys.update(x for group in item.get("RequiresAnyGroups", []) for x in group)
    return keys | {"konomi.closed", "konomi.committed", "konomi.private_future"}


def measure(scenes, sequence, initial):
    # Each state retains both complete prefix extrema; future predicates decide
    # which prefix can actually continue, avoiding sums of incompatible maxima.
    states = {frozenset(initial): [(0, [])]}
    chapter = 3
    for index, event in enumerate(sequence):
        if isinstance(event, dict):
            chapter = event.get("chapter", chapter)
            changed = {}
            for flags, values in states.items():
                key = frozenset((set(flags) - set(event.get("remove", []))) | set(event.get("add", [])))
                combined = changed.get(key, []) + values
                changed[key] = [min(combined, key=lambda x: x[0]), max(combined, key=lambda x: x[0])]
            states = changed
            continue
        scene = scenes[event]
        assert scene.get("MinChapter", 0) <= chapter <= scene.get("MaxChapter", 99)
        assert not scene.get("Chapters") or chapter in scene["Chapters"]
        future = relevant([scenes[x] for x in sequence[index + 1:] if isinstance(x, str)])
        out = {}
        for flags, extrema in states.items():
            if not allowed(scene, flags):
                continue
            for after, count, trace in walk(scene, set(flags)):
                key = frozenset(after & future)
                for prior_count, prior_trace in extrema:
                    value = (prior_count + count, prior_trace + trace)
                    old = out.get(key, [])
                    values = old + [value]
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
    args = parser.parse_args()
    raw = args.story.read_bytes()
    scenes = {s["Id"].removeprefix("konomi."): s for s in json.loads(raw)["Scenes"] if s.get("Relationship") == "konomi"}
    initial = {"konomi.present", "trickster"}
    early = "margin reception letter evening disagreement leak reckoning".split()
    hearing = "hearing hearing_after new_letter".split()
    late = "return political_account power a_useful_supper the_upper_passage two_bad_prices the_trial_day a_name_beside_hers the_evening_she_kept ordinary farewell ending_private".split()
    dismiss = {"remove": ["konomi.present"], "add": ["konomi.dismissed", "konomi.office_completed"]}
    private = "fate_post fate_reply private_meeting private_history carriers before_road private_departure capital_letter return_offer private_reunion".split()
    private_end = "private_political_account lease_offer chosen_evening private_future_choice ending_distance".split()
    private.insert(private.index("capital_letter"), {"chapter": 5})
    scenarios = {
        "ordinary_required": early + [{"chapter": 5}] + late,
        "ordinary_hearing_and_abyss": early + hearing + [{"chapter": 4}, "unsent", {"chapter": 5}] + late,
        "private_fresh": [dismiss] + [x for x in private if x != "private_history"] + private_end,
        "private_established_pending_hearing": early + [dismiss] + private + "private_hearing private_hearing_after private_new_letter".split() + private_end,
    }
    results = {name: measure(scenes, sequence, initial) for name, sequence in scenarios.items()}
    print("Story SHA256:", hashlib.sha256(raw).hexdigest().upper())
    for name, (shortest, longest) in results.items():
        print(name, shortest[0], longest[0], "selected words")
        totals = {}
        for sid, nid, i, _ in longest[1]:
            scene_id = sid.removeprefix("konomi.")
            node = next(n for n in scenes[scene_id]["Nodes"] if n["Id"] == nid)
            totals[scene_id] = totals.get(scene_id, 0) + words(node["Text"]) + words(node["Choices"][i]["Text"])
        assert sum(totals.values()) == longest[0]
        print("  longest scene totals:", totals)
    if args.read_path:
        for sid, nid, i, _ in results[args.read_path][1][1]:
            node = next(n for n in scenes[sid.removeprefix("konomi.")]["Nodes"] if n["Id"] == nid)
            print(f"\n{sid}/{nid}\n{node['Text']}\n> {node['Choices'][i]['Text']}")


if __name__ == "__main__":
    main()
