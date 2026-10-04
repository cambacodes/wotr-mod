"""eng7-l06: finale placement fallbacks require durable, earned observation receipts."""
import argparse
import json
from pathlib import Path


def check(story):
    hard = []
    receipts = story.get("PresenceFailureReceipts") or {}
    temporary = {name + ".failed" for name in receipts}
    authored = {f for s in story.get("Scenes") or [] for n in s.get("Nodes") or []
                for c in n.get("Choices") or [] for f in c.get("Set") or []}
    for name, receipt in receipts.items():
        rel = name.split(".presence")[0]
        returns = set(((story.get("Relationships") or {}).get(rel) or {}).get("UnavailableOverrides", {}).values())
        flag = receipt.get("Flag")
        if (name not in (story.get("Presences") or {}) or flag != rel + ".presence.failure_observed"
                or not set(receipt.get("Requires") or []) & returns or flag in authored
                or flag in (story.get("Derived") or {})):
            hard.append("PF1 invalid earned failure receipt: " + name)

    def transient(key, seen=()):
        if key in temporary:
            return True
        if key in seen:
            return False
        return any(transient(k, (*seen, key)) for g in (story.get("Derived") or {}).get(key, []) for k in g)

    for scene in story.get("Scenes") or []:
        if not scene.get("Owner", "").endswith("Epilogue"):
            continue
        blocks = [scene, *(scene.get("Nodes") or [])]
        blocks.extend(p for n in scene.get("Nodes") or [] for p in n.get("Paragraphs") or [])
        for block in blocks:
            keys = [*block.get("Requires", []), *block.get("Forbids", []), *block.get("RequiresAny", [])]
            keys.extend(k for g in block.get("RequiresAnyGroups") or [] for k in g)
            if any(transient(k) for k in keys):
                hard.append("PF2 finale reads transient placement evidence: " + scene["Id"])
    return hard


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", default="development/Story.json")
    args = parser.parse_args()
    hard = check(json.loads(Path(args.story).read_text(encoding="utf-8")))
    for error in hard:
        print(error)
    print("presence failure receipts: %d hard" % len(hard))
    return bool(hard)


if __name__ == "__main__":
    raise SystemExit(main())
