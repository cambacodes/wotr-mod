"""W4 Ch5 ensemble: authored supper at the existing Fool King's Table.

S32 is fixed comedy; Delamere/Nenio and Delamere/Wenduag stay cordial.
No ladder, native rewrite, recollection, echo or intimate interval is supplied.
The public paid page opens coexistence; current qualified bodies supply speech.
See tools/route_packs/harem/W4-household-ensemble-ch5.md for native evidence.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.ensemble.ch5."
SCENE_ID = PREFIX + "arrows"
WOMEN = ("nenio", "wenduag", "delamere")
SEEN = PREFIX + "arrows.seen"


def supper():
    return scene(SCENE_ID, "Feathers in the supper", "Nenio", 5,
        "[Nenio, Wenduag and Delamere: arrows at supper]", [
            n("start", "Nenio", '''{n}A bundle of salvaged arrows lies across the Table. Wenduag eats beside it. Nenio holds a black feather over her notebook; Delamere keeps the arrowheads well clear of the bowls. Boots tramp past outside, bound for the walls.{/n}
"Mongrel girl! What species supplied this feather?"
"A demon that flies backward. Makes it harder to see the hunter coming." {n}Wenduag tears meat off a bone.{/n} "My hunters brought it down."
"Then the feather's wear should be reversed," {n}Nenio says, turning the feather over.{/n} "I shall compare the others."
"You will straighten the shafts first," {n}Delamere says.{/n} "The watch needs arrows. Not your book."
{n}Wenduag grins around her mouthful and slides a bent shaft toward Nenio.{/n} "Go on. Show us what those clever hands can do."''',
                c("[Help straighten the shafts; leave Nenio a feather.]", "shafts"),
                c("[Spread the feathers beside Nenio's notebook.]", "feathers"),
                c("[Later.]", abort=True)),
            n("shafts", "Narrator", '''{n}You brace a shaft against the table's edge. Delamere turns it beneath your hand until the bend faces upward. Wenduag watches, then sets down her bone and starts sorting the split shafts from the sound ones.{/n}
"These won't survive a second shot. Give them to the girl. Plenty to scribble on."
"A useful division!" {n}Nenio lays the feather alongside a split shaft.{/n} "But your account of backward flight remains unconfirmed."
"Go out and find one yourself. My hunters aren't carrying you."
{n}Delamere gathers the straightened arrows against her bow.{/n} "Keep her off the parapet while she looks. The archers have enough to aim around."
{n}Nenio measures the feather. Wenduag draws her bowl closer before the ruler can reach it. Delamere carries the arrows out to the watch.{/n}''',
                c("[Finish supper.]", flags=(SEEN, PREFIX + "arrows.shafts"))),
            n("feathers", "Narrator", '''{n}You clear a patch of table and spread the loose feathers on it. Nenio lines them up by length. Wenduag wipes grease from her fingers and picks out the largest.{/n}
"This one came from their leader. He shrieked louder than the rest."
"Your criterion is volume? That would make the cook our commander."
{n}Wenduag chokes on a laugh.{/n} "Tell him that. Tell him I sent you."
{n}Delamere pulls the sound shafts out from under the notebook.{/n} "Laugh after the watch has its arrows. Hold these."
{n}She puts a bundle into Wenduag's hands. Wenduag scowls, then tucks it beneath one arm and takes her last mouthful standing. Nenio keeps the loose feathers and begins a new sketch.{/n}''',
                c("[Let them get on with it.]", flags=(SEEN, PREFIX + "arrows.feathers"))),
        ], requires=("trickster", "trickster.now", household.PAGE_TAKEN,
                     household.STANCE_ELIGIBLE, household.KEPT,
                     *(w + suffix for w in WOMEN
                       for suffix in (".harem.eligible", ".present_now"))),
        forbids=(SEEN, "fool_king.gone", "trickster.failed", "sacrifice"),
        optional=True, Relationship="household", Chapters=[5],
        Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
        Participants=list(WOMEN), ParticipantWomen=list(WOMEN),
        RestAllowance="household.pair", HouseholdCategory="dynamic",
        HouseholdWitness=SEEN,
        ForbidOverrides={"sacrifice": "trickster.commander_back"})


def register(payload, scenes, refs):
    if any(s["Id"] == SCENE_ID for s in scenes):
        return
    # Single-woman seats copy the current route's exact loss/return scopes.
    # S09 already supplies Wenduag's party-or-returned-Drezen body reader;
    # Delamere's existing earned visitor is never an undead companion copy.
    seats = payload.setdefault("SeatWomen", {})
    for woman, body in (
        ("wenduag", "household.pair.wenduag_arueshalae.body.wenduag"),
        ("delamere", "delamere.trickster.returned"),
    ):
        if woman not in seats:
            route = payload["Relationships"][woman]
            seats[woman] = dict(
                Relationship=woman, Requires=[woman + ".present_now", body],
                UnavailableFlags=list(dict.fromkeys(
                    route.get("UnavailableFlags", []) + route.get("EpochUnavailableFlags", []))),
                UnavailableOverrides=dict(route.get("UnavailableOverrides", {})))
    # Reuse the integrator's Nenio party-or-current-Drezen-body contract.
    for woman in WOMEN:
        seat = payload.get("SeatWomen", {}).get(woman)
        if not seat or seat.get("Relationship") != woman or not seat.get("Requires"):
            raise ValueError("Ch5 ensemble needs current bodily SeatWomen: " + woman)
    scenes.append(supper())
    household.CONSUMERS[SCENE_ID] = household.PAGE_TAKEN
