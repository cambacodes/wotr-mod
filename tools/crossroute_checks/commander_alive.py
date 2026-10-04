"""L2: living postwar/Last Call Commander, reusing earned_presence policy."""
import re
from .common import OR, lit, finding, postwar, ep

LIVING = re.compile(r"\b(?:you (?:stand|sit|take|touch|kiss|walk|hold|return|wake|smile|laugh|reach|enter|lie|are)|your (?:hand|lips|mouth|arms|bed)|Commander (?:stands|sits|takes|touches|returns|walks|holds))\b", re.I)


def check(model, blocks, proof):
    out = []
    target = OR(lit(ep.SACRIFICE, False), lit(ep.COMMANDER_BACK))
    for b in blocks:
        if not postwar(b.scene) or b.scene["Owner"] == "AeonEpilogue":
            continue
        # Independent/mourning pages remain legitimate; a new living action in
        # one still gets checked. Paragraph guards are proved individually.
        independent = b.scene["Id"] in ep.COMMANDER_ABSENT or ep.mourning(b.scene, model.composites)
        mourning = ep.mourning(b.spec, model.composites)
        if (independent or mourning) and not LIVING.search(b.text):
            continue
        if b.slot in ("Entry", "ReturnText") or b.text in ("Continue", "Next", "End"):
            continue
        if not proof.implies(b.context, target):
            out.append(finding("L2", b, "Forbid sacrifice, lifted only by trickster.commander_back (or a proven alive witness)", required=target))
    return out
