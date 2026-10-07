"""Authored Ch3 Table supper; S32 remains fixed comic, with no ladder.

Voice anchor (not remembered history): NenioVenduag/banter4_pack2,
5f58209d46d1bc7409879fcf82e3a09c; enGB 791f6a36-3178-4ad9-92e0-42817c0ad83a
and 17933ab3-3474-46a1-bc7c-cecff341eb22. Wenduag wants the hunter's rank,
Nenio evidence, Seelah fed soldiers. No native fact, echo or intimate interval
is changed. Body-bearing party etudes qualify all three speakers independently
of commitment; current route/epoch checks still apply through Participants.
"""
from copy import deepcopy

from story_format import c, n, scene

ID = "household.ensemble.ch3.supper"
SEEN = ID + ".seen"
WOMEN = ("seelah", "nenio", "wenduag")
OBJECTIONS = {
    a + ".harem.enmity." + b: a + ".harem.reconciled." + b
    for a, b in (("seelah", "wenduag"), ("wenduag", "seelah"),
                 ("seelah", "nenio"), ("nenio", "seelah"))
}


def supper():
    return scene(ID, "Something in the stew", "Nenio", 3,
        "[Join the argument over supper.]", [
            n("start", "Nenio", '''{n}A bowl of stew stands beside Nenio's notebook. Wenduag has pushed hers away. Seelah scrapes the last of hers up with bread.{/n}
"Spider girl says a hunter can smell a cultist through a pot of boiling meat. I have requested a demonstration."
"You stink of ink. She stinks of armor. The cultists stink of fear," {n}Wenduag says, baring her teeth.{/n} "Send me ahead of your marching soldiers. I'll find something better to eat."
"And leave them to chase you on empty bellies?" {n}Seelah pulls Wenduag's bowl back from the notebook.{/n} "Eat first. Then boast."
{n}Nenio lifts her pencil. Wenduag watches your hand near the covered pot.{/n}''',
                c('"Here. Identify this before Nenio writes it down."', "sample"),
                c('"The pot is for supper. Keep your experiment out of it."', "supper"),
                c("[Later.]", abort=True)),
            n("sample", "Wenduag", '''{n}You fish a bone from the pot and set it on Nenio's empty plate. Wenduag sniffs it, then snaps off the soft end between her teeth.{/n}
"Goat. Old. Cooked too long. Your cook would last one day hunting with me."
"And now the sample has been consumed!" {n}Nenio turns the plate, examining the tooth marks.{/n} "Does the fear remain detectable after boiling?"
"Of course. Bring me a cultist and I'll show you," {n}Wenduag says.{/n}
"You're not dragging a prisoner into the kitchen," {n}Seelah says.{/n} "If you're so hungry, finish your bowl. We need you on your feet when the scouts come back."
{n}Wenduag hooks the bowl towards herself with a claw. Nenio reaches for another bone; Seelah moves the pot to the middle of the table.{/n}''',
                c("[Pass the bread and finish supper.]", flags=(SEEN,))),
            n("supper", "Seelah", '''{n}Seelah ladles the remaining stew into Wenduag's bowl.{/n}
"There. No cultist required."
"A demonstration postponed," {n}Nenio says. She closes the notebook over her pencil.{/n}
"I'll bring you something with teeth next time, scholar. See how much you write while it bites you," {n}Wenduag says.{/n}
"Bring back the scouts first," {n}Seelah says, breaking the loaf.{/n} "They've been out since dawn."
{n}Wenduag tears a piece from the loaf before Seelah can pass it. Nenio opens her notebook again and makes a small sketch of the bite.{/n}''',
                c("[Eat before the scouts return.]", flags=(SEEN,))),
        ], requires=("trickster", "trickster.now", "foresight.page_taken",
                     "household.stance_eligible", "household.table.kept",
                     *(w + ".harem.eligible" for w in WOMEN),
                     *(w + ".present_now" for w in WOMEN),
                     *(w + ".in_party" for w in WOMEN)),
        forbids=(SEEN, "fool_king.gone", "trickster.failed", "sacrifice", *OBJECTIONS),
        ForbidOverrides={"sacrifice": "trickster.commander_back", **OBJECTIONS},
        optional=True, last=3, Chapters=[3], Relationship="household",
        Areas=["2570015799edf594daf2f076f2f975d8"], InteractionHub="household.table",
        Participants=list(WOMEN), RestAllowance="household.pair",
        HouseholdCategory="dynamic", HouseholdWitness=SEEN)


def register(payload, scenes, refs):
    """Append one ensemble to the existing menu, charging its existing allowance."""
    if any(body["Id"] == ID for body in scenes):
        return
    # Registration reads existing native party bodies, never creates attendance.
    for woman in WOMEN:
        if woman + ".in_party" not in payload.get("Etudes", {}):
            raise ValueError("Ch3 ensemble needs the native party body: " + woman)
    scenes.append(deepcopy(supper()))
    payload.setdefault("ForesightConsumers", {})[ID] = "foresight.page_taken"
