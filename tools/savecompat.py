"""Frozen save-reference inventory, independent of mutable dialogue text.

Identity rules mirror Main.BuildScene: ordinary answers use their index;
single, inert terminal epilogue answers use the legacy ``continue`` suffix.
Choice Id metadata overrides the suffix for BuildScene answers, as in the runtime.
"""
import json
from pathlib import Path

BASELINE_PATH = Path(__file__).with_name("savecompat_baseline.json")
BASELINE_REVISION = "a68bb988"

# A frozen .continue exit is inert, even when new answers follow it.
EXIT_MECHANICS = ("Next", "Check", "Requires", "Forbids", "Set", "Abort", "Revive",
                  "NativeNext", "Mythic", "Alignment", "Crusade", "RemoveItem", "StartEtude")


def choice_identities(scene, node):
    choices = node.get("Choices", [])
    if scene.get("ContinueBefore"):
        # BuildContinueBefore registers a cue, with no authored answers.
        return [dict(Id=choice.get("Id"), GuidFor=[]) for choice in choices]
    if scene.get("ReturnToList"):
        # BuildReturnToList creates a separate inline graph for each host list.
        return [dict(Id=choice.get("Id"), GuidFor=[
            "answer.%s.%s.%s.%d" % (scene["Id"], host, node["Id"], index)
            for host in scene.get("AnswerLists", [])])
            for index, choice in enumerate(choices)]
    legacy = False
    if scene.get("Owner", "").endswith("Epilogue") and len(choices) == 1:
        choice = choices[0]
        legacy = choice.get("Text", "Continue") == "Continue" and not any(
            choice.get(key) for key in
            ("Next", "Check", "Requires", "Forbids", "Set", "Abort", "Revive"))
    prefix = "answer.%s.%s." % (scene["Id"], node["Id"])
    return [dict(Id=choice.get("Id"), GuidFor=prefix + (choice.get("Id") or ("continue" if legacy else str(index))))
            for index, choice in enumerate(choices)]


def inventory(story):
    return {
        "Scenes": {scene["Id"]: {
            node["Id"]: choice_identities(scene, node)
            for node in scene.get("Nodes", [])}
            for scene in story.get("Scenes", [])}}


def check(story, baseline=None):
    """Return hard failures; new scenes, nodes and trailing choices are allowed."""
    if baseline is None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    failures = []
    scenes = {}
    for scene in story.get("Scenes", []):
        sid = scene["Id"]
        if sid in scenes:
            failures.append("Duplicate scene: " + sid)
        scenes[sid] = scene
    for sid, old_nodes in baseline["Scenes"].items():
        if sid not in scenes:
            failures.append("Missing scene: " + sid)
            continue
        scene = scenes[sid]
        nodes = {}
        for node in scene.get("Nodes", []):
            if node["Id"] in nodes:
                failures.append("Duplicate node: %s/%s" % (sid, node["Id"]))
            nodes[node["Id"]] = node
        for nid, old_choices in old_nodes.items():
            location = sid + "/" + nid
            if nid not in nodes:
                failures.append("Missing node: " + location)
                continue
            choices = nodes[nid].get("Choices", [])
            if (len(old_choices) == 1
                    and old_choices[0]["GuidFor"] == "answer.%s.%s.continue" % (sid, nid)
                    and choices and any(choices[0].get(key) for key in EXIT_MECHANICS)):
                failures.append("Legacy ending exit mechanics changed: " + location)
            current = choice_identities(scene, nodes[nid])
            if len(current) < len(old_choices):
                failures.append("Choice count shrank: %s (%d -> %d)" %
                                (location, len(old_choices), len(current)))
            for index, (old, new) in enumerate(zip(old_choices, current)):
                # An explicit suffix may preserve an implicit old identity; pre-existing Id metadata stays frozen.
                if old["GuidFor"] != new["GuidFor"] or old["Id"] is not None and old["Id"] != new["Id"]:
                    failures.append("Choice identity changed: %s[%d] (%r -> %r)" %
                                    (location, index, old, new))
    return failures


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path,
                        default=Path(__file__).resolve().parents[1] / "development/Story.json")
    args = parser.parse_args()
    failures = check(json.loads(args.story.read_text(encoding="utf-8-sig")))
    for failure in failures:
        print(failure)
    print("Save compatibility: %d hard failures" % len(failures))
    raise SystemExit(bool(failures))
