"""ARS-A2-02: retain heat-transformed roof nodes behind earned history."""
from copy import deepcopy

from story_format import n


NIGHT = """{n}Arsinoe turned the key in the lock behind her. The lease lay on the sideboard where she had set it, folded, and she did not look at it. Her fingers were already at the Commander's collar.{/n}
"Three renewals, every one paid late, and I entered every one as punctual. I have never falsified an account in my life." {n}She caught their hands and kissed them hard.{/n} "Rent has a date and a sum. This has neither. I have spent a season being patient across a counter, and I am done with it."
{n}She undid the rest of the fastenings herself, quick and exact, and let the robes fall where they fell. Her hair came loose as she pushed the Commander back toward the bed. She climbed over them, put their hands on her waist, and held them there until the fingers tightened.{/n}
"The lien stands. This is outside it. Look at me."
{n}Her composure broke on a breath, and she bent to their mouth.{/n}"""
RETURN = """{n}Arsinoe did not stop to remark on the room. She shut the door with her heel and laid her gloves on the table beside the lease, and she looked at neither.{/n}
"I remember the counter, and the pen on the floor, and the tea gone cold in the cup. I remember that I did not once look at the clock." {n}She crossed to the Commander and took their face in both hands.{/n} "The lease has not changed. Neither has this. I have been entering your payments as late for weeks, and I have been in no hurry whatever to collect."
{n}She was out of her robe before the Commander had finished answering, and her hair followed it. She pushed them down, straddled them, and kissed them as if there were a debt outstanding.{/n}
"Outside the lease, as before. I intend to be insufferable about it."
{n}Her hands found theirs, and she held them against her waist.{/n}"""


def integrate(payload):
    from storylines import arsinoe_trickster as route
    late = next(s for s in payload["Scenes"] if s["Id"] == "arsinoe.trickster.late.commit")
    if any(n["Id"] == "rubric2_cauldron_night" for n in late["Nodes"]):
        return
    offer = late["Nodes"][0]
    for old, new, beat in (
        ("night", "rubric2_cauldron_night", NIGHT),
        ("late_return", "rubric2_cauldron_return", RETURN),
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
        late["Nodes"].append(n(new, node["Speaker"], beat,
                               *deepcopy(node["Choices"])))
