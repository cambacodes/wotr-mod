#!/usr/bin/env python3
"""Reconcile the approved 167 E4 hooks against the actual export, without inference."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "tools/route_packs/plans/j02-policy.json"
IDENTITY = "5bc667258cd57637cc922f31223c8b45ed3431bfbefc4a149992a52e6f54adeb"


def census(story):
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    hooks = policy["hooks"]
    assert len(hooks) == len(set(hooks)) == 167
    assert hashlib.sha256("\n".join(sorted(hooks)).encode()).hexdigest() == IDENTITY
    terminals = {}
    for scene in story["Scenes"]:
        for node in scene["Nodes"]:
            for index, choice in enumerate(node["Choices"]):
                for flag in choice["Set"]:
                    terminals.setdefault(flag, []).append(dict(
                        scene=scene["Id"], node=node["Id"], choice=index,
                        requires=choice["Requires"], forbids=choice["Forbids"]))
    rows = []
    for hook in hooks:
        row = dict(hook=hook, ruling=29 if ".attitude." in hook else
                   30 if ".enmity." in hook else 31 if ".reconciled." in hook else 32)
        if hook.endswith("bodies_current"):
            row["ruling"] = 33
        elif hook.endswith(("captivity_remedy_ready", "remedy.authorized")):
            row["ruling"] = 34
        elif hook == "camellia.harem.strain.galfrey.1":
            row["ruling"] = 35
        if hook in terminals:
            row.update(status="produced", terminals=terminals[hook])
        elif hook in story.get("Derived", {}):
            row.update(status="derived", witnesses=story["Derived"][hook],
                       forbids=story.get("DerivedForbids", {}).get(hook, []))
        elif any(scene.get("ContactWitness") == hook and scene.get("ParticipantContacts")
                 for scene in story["Scenes"]):
            row.update(status="runtime-evaluated", contact_scenes=[
                scene["Id"] for scene in story["Scenes"]
                if scene.get("ContactWitness") == hook and scene.get("ParticipantContacts")])
        elif any(hook in story.get(kind, {}) for kind in
                 ("Etudes", "SeenCues", "SelectedAnswers", "Latches")):
            row.update(status="runtime-evaluated")
        else:
            if ".attitude." in hook:
                reason = "No approved directional group: below/above friendship-only ceiling or unearned stage."
            elif ".reconciled." in hook:
                reason = "No approved one-reconciliation terminal; ordinary success, X remedy and reciprocal receipts are excluded."
            elif ".enmity." in hook:
                reason = ("Composite alias is inert; use the qualified woman only."
                          if hook in policy["aliases"] else
                          "No emitted approved final terminal with this exact claimant direction; see row dispositions.")
            else:
                reason = {
                    "household.docket.horzalah_hepzamirah.captivity_remedy_ready": "Awaiting J05's actual surrender, ruling 05.",
                    "household.docket.gesmerha_jerribeth.remedy.authorized": "Awaiting J05's actual cache delivery, ruling 07.",
                    "camellia.harem.strain.galfrey.1": "No approved knowledge beat; presence cannot produce jealousy.",
                }.get(hook, "No approved producer emitted by its owning job.")
            row.update(status="legitimately-inert", reason=reason)
        rows.append(row)
    return dict(schema=1, hook_count=167, hook_sha256=IDENTITY,
                counts={status: sum(r["status"] == status for r in rows) for status in
                        ("produced", "derived", "runtime-evaluated", "legitimately-inert")},
                rows=rows, failure_mappings=policy["failures"],
                dispositions=policy["dispositions"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = census(json.loads(args.story.read_text(encoding="utf-8-sig")))
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("J02 census: 167 hooks; " + str(result["counts"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
