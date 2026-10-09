"""ARS-A2-02: retain heat-transformed roof nodes behind earned history."""
from copy import deepcopy

from story_format import n


def integrate(payload):
    from storylines import arsinoe_trickster as route
    late = next(s for s in payload["Scenes"] if s["Id"] == "arsinoe.trickster.late.commit")
    if any(n["Id"] == "rubric2_cauldron_night" for n in late["Nodes"]):
        return
    offer = late["Nodes"][0]
    for old, new, beat in (
        ("night", "rubric2_cauldron_night", "first late night earned through cauldron collection; no invented roof memory"),
        ("late_return", "rubric2_cauldron_return", "returning late night earned through cauldron collection; no invented roof memory"),
    ):
        node = next(n for n in late["Nodes"] if n["Id"] == old)
        incoming = next(c for c in offer["Choices"] if c["Next"] == old)
        alternate = deepcopy(incoming)
        incoming["Requires"].append("arsinoe.roof_shared")
        alternate["Next"] = new
        alternate["Forbids"].append("arsinoe.roof_shared")
        # Shared payoff integration gates the saved first answer by index.
        # Its appended twins must consume the same earned outcome explicitly.
        alternate["Requires"].append(route.LATE_COMMITTED)
        offer["Choices"].append(alternate)
        late["Nodes"].append(n(new, node["Speaker"], "[PROSE PENDING: " + beat + "]",
                               *deepcopy(node["Choices"])))
