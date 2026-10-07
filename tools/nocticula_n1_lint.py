"""Check Nocticula N1 inventories; --release blocks all pending writer prose."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from storylines.nocticula_n1 import RETIRED, NEW_FLAGS


def check(story, release=False):
    errors = []
    contracts = json.loads(Path(__file__).with_name("route_packs").joinpath("plans/nocticula-n1-contracts.json").read_text(encoding="utf-8"))
    by = {s["Id"]: s for s in story["Scenes"]}
    classified = {(x["scene"], x["node"]) for x in contracts["new_nodes"]}
    paragraphs = {(x["scene"], x["node"], x["paragraph"]): x for x in contracts["new_paragraphs"]}
    for sid, nid in classified:
        if not any(n["Id"] == nid for n in by.get(sid, {}).get("Nodes", [])):
            errors.append(sid + "/" + nid + ": missing classified N1 node")
    for key, spec in paragraphs.items():
        sid, nid, index = key
        node = next((n for n in by.get(sid, {}).get("Nodes", []) if n["Id"] == nid), {})
        blocks = node.get("Paragraphs", [])
        if index >= len(blocks) or not set(spec["requires"]) <= set(blocks[index].get("Requires", [])) or not set(spec["forbids"]) <= set(blocks[index].get("Forbids", [])):
            errors.append(sid + "/" + nid + ": missing classified deed paragraph")
    for hook in contracts["native_hooks"].values():
        actual = story.get(hook["field"], {}).get(hook["key"])
        expected = [hook["guid"]] if hook["field"] == "SeenCues" else hook["guid"]
        if actual != expected:
            errors.append(hook["key"] + ": missing read-only native binding")
    scenes = [s for s in story["Scenes"] if s.get("Relationship") in ("nocticula", "nocticula.acquisition")]
    produced = {f for s in scenes for n in s["Nodes"] for a in n["Choices"] for f in a.get("Set", [])}
    if "noct.retired" in produced:
        errors.append("noct.retired must never have an authored producer")
    if "noct.retired" not in story.get("PendingHooks", []):
        errors.append("noct.retired must be registered as a known, unproduced key")
    for flag in set(NEW_FLAGS) - {"noct.retired", "noct.native_trials_seen"}:
        if flag not in produced:
            errors.append(flag + ": missing N0 producer")
    for s in scenes:
        donor = s["Id"].split(".acquired.")[0].removeprefix("noct.")
        if donor in RETIRED or s["Id"] == "noct.acq.the_retained_copy":
            if "noct.retired" not in s["Requires"]:
                errors.append(s["Id"] + ": retired scene can still arrive")
        for node in s["Nodes"]:
            blocks = [node, *node.get("Paragraphs", [])]
            for block in blocks:
                if release and "[N2 PROSE PENDING:" in block.get("Text", ""):
                    errors.append(s["Id"] + "/" + node["Id"] + ": pending writer prose")
            if "[N2 PROSE PENDING:" in node["Text"] and (s["Id"], node["Id"]) not in classified:
                errors.append(s["Id"] + "/" + node["Id"] + ": unclassified N1 node")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=Path(__file__).resolve().parents[1] / "development/Story.json")
    parser.add_argument("--release", action="store_true")
    args = parser.parse_args()
    errors = check(json.loads(args.story.read_text(encoding="utf-8-sig")), args.release)
    for error in errors:
        print("HARD", error)
    print("Nocticula N1: %d hard failures" % len(errors))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
