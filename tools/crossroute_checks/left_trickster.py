"""L6: adapt existing T1-T7 diagnostics; do not duplicate producer T7.

T7 covers the full recursive return/device producer class and revivals.
T6 covers native edits, suppressions, gates and settlements, distinguishing
new power (trickster.now) from consequences of a specific already-earned act.
Add replacement cue context to the native diagnostics, including every variant.
"""
import re
from tools import earned_presence_lint as earned
from .common import Block, finding, scene_context


def check(model, blocks, proof):
    hard, _ = earned.check(model.story)
    out = []
    index = {(b.scene["Id"], b.node.get("Id"), b.slot): b for b in blocks}
    for message in hard:
        if not re.match(r"T[1-7](?:[ab])? ", message):
            continue
        match = re.match(r"T\d(?:[ab])? ([^ :/]+)(?:/([^/ :]+)(?:/(choice\[\d+\]))?)?:", message)
        if match and match[1] in model.by_id:
            s = model.by_id[match[1]]
            n = next((n for n in s["Nodes"] if n["Id"] == match[2]), s["Nodes"][0] if s["Nodes"] else {"Id": ""})
            b = index.get((s["Id"], n["Id"], match[3] or "text"))
            b = b or Block(s, n, s, "scene", n.get("Text", ""), scene_context(model, s))
            out.append(finding("L6", b, message, message.split()[0]))
            continue
        linked = []
        for cue, edit in (model.story.get("NativeEpilogueEdits") or {}).items():
            if "native edit " + cue + " / " in message:
                for v in [edit] + list(edit.get("Variants") or []):
                    if " / %s:" % v.get("Replacement") in message and v.get("Replacement") in model.by_id:
                        linked.append((model.by_id[v["Replacement"]], "native edit " + cue))
        if linked:
            for s, slot in linked:
                n = s["Nodes"][0] if s["Nodes"] else {"Id": ""}
                out.append(finding("L6", Block(s, n, s, slot, n.get("Text", ""), scene_context(model, s)), message, slot))
        else:
            # Relationship metadata / suppression / native gate has no authored
            # node. Report its actual key rather than inventing a scene id.
            route = match[1] if match and match[1] in model.rels else "@native"
            target = message.split(":", 1)[0]
            for field, label in (("NativeEpilogueSuppressions", "native suppression"), ("NativeGates", "native gate"),
                                 ("NativeObjectiveSettlements", "native settlement")):
                for key, spec in (model.story.get(field) or {}).items():
                    if label + " " + key + ":" in message:
                        route, target = spec.get("Relationship", "@native"), key
            if match and match[1].startswith("foresight."):
                route, target = "foresight", match[1]
            s = dict(Id=target, Relationship=route)
            out.append(finding("L6", Block(s, {"Id": "@condition"}, {}, "condition", message, ("and",)), message, message.split()[0]))
    return out
