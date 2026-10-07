"""Authored S50 custody errand; fixed hostility, not a pair romance.

Native evidence and integration dependencies: tools/route_packs/harem/s50.md.
The child's feed is never an intimate consideration. Devarra is discussed only.
"""
from copy import deepcopy

from story_format import c, n, p, scene

P = "household.pair.nidalynn_devarra."
N = "nidalynn.trickster."
BILL = "devarra.trickster.cost.egg_withheld"
DEBT = "devarra.trickster.debt_claimed"
RENOUNCED = N + "cost.claim_given_up"
BODIES = {
    "widow": ("nidalynn.presence", "e24a8cb4f83960748b5bead99d58a36e"),
    "chosen": ("nidalynn.presence.chosen", "3191b154bbed71b4595a5154ad067e90"),
}
DEEDS = ("resolved", "guardian_kept", "feed_delivered", "cost.nidalynn_guard_night",
         "cost.nidalynn_own_feed", "cost.commander_luxury_lost")


def writes(step, *outcomes):
    return tuple(P + key for key in (step + ".seen", *outcomes))


def notice_nodes():
    return [
        n("start", "Nidalynn", '''{n}Nidalynn stops you on the jeweller's steps with an empty feed sack. A crusader carrying a bundle of arrows squeezes past her.{/n}
"She's eaten. Don't look so worried. But she's growing, and I won't have the soldiers teaching her to hunt whatever runs. Come and choose the next load with me."
{n}She puts the sack in your hand.{/n}
"You took one egg. I'm raising what came out of it. We have different work to do."''',
          c('"Tell me what she needs. The bill is mine."', "account"),
          c('"I am not answering for this."', "refused"),
          c('[Later.]', abort=True)),
        n("account", "Nidalynn", '"And what did the grey one ask of you?"',
          c('"She named her price for the smallest egg."', "bill", requires=(BILL,)),
          c('"She has claimed a debt. She has not named the egg\'s price."', "debt",
            requires=(DEBT,), forbids=(BILL,)),
          c('"She has not named a bill for it."', "unnamed", forbids=(BILL, DEBT))),
        n("bill", "Nidalynn", '''"Then you still owe it. Sending food here won't pay her."
{n}She folds the mouth of the sack down twice.{/n}
"Bring this back in two days. I'll have the cart ready. She has a mother. She has someone raising her. Put your load where I tell you."''',
          c('[Take the sack.]', flags=writes("notice", "notice.opened"))),
        n("debt", "Nidalynn", '''"A debt isn't the same as the price of her egg. Don't mix them up when she comes collecting."
{n}She points toward the kiln below the wall.{/n}
"Two days. Bring the sack there. I'll choose what goes in it."''',
          c('[Take the sack.]', flags=writes("notice", "notice.opened"))),
        n("unnamed", "Nidalynn", '''"Then taking it is still yours to answer for. Not the little one's."
{n}She points toward the kiln below the wall.{/n}
"Come in two days. I'll choose her feed. She's already tried to eat a sentry's boot. I don't want her learning the rest of him is dinner."''',
          c('[Take the sack.]', flags=writes("notice", "notice.opened"))),
        n("refused", "Nidalynn", '''{n}She takes the sack back.{/n}
"All right. I'll fill it. She'll eat, and I'll stay at the kiln tonight. The men on the wall need their sleep."
{n}She goes down the steps without waiting for you.{/n}''',
          c('[Leave.]', flags=writes("notice", "notice.refused", "unanswered"))),
    ]


MENU = '''{n}Nidalynn has set a bowl of goat meat beside the empty cart. She pushes aside the strip of bloody hunting meat you brought.{/n}
"No. That teaches her to follow the smell to your soldiers. Goat, cut small. She can bite it without dragging it through the ashes."
{n}She tips the bowl into a sack, then adds meat from her own stores.{/n}
"I'll keep the kiln tonight. You can give up the roast they were saving for your supper. There'll be enough without it, but the extra load will last. Bring it to me whole."'''


def custody_nodes():
    return [
        n("start", "Nidalynn", MENU,
          c('[Athletics] "Your feed. I will bring the cart down myself."',
            requires=(RENOUNCED,), check=dict(Skill="SkillAthletics", DC=18,
                Success="delivered", Failure="spilled", CommanderOnly=True)),
          c('"Hire the delivery. Use my supper for the extra load."', "hire", requires=(RENOUNCED,)),
          c('"Keep her here. I won\'t supply the next feed."', "refused"),
          c('[Later.]', abort=True)),
        n("delivered", "Nidalynn", '''{n}You brace the cart against the slope while arrows rattle overhead on their way to the wall. At the kiln Nidalynn opens every sack, feels for splinters and carries the meat inside.{/n}
"Whole. Good. Put the cart against the wall. She'll climb it if you leave it there."
{n}From inside comes a scrape of claws. Nidalynn pulls the door shut before the little head can force it open.{/n}
"Not yet, you greedy thing. I've got to cut it first."''',
          c('[Unload the last sack.]', flags=writes("custody", *DEEDS))),
        n("hire", "Nidalynn", '''{n}The delivery men wait beside the loaded cart. Nidalynn lifts the cover from a sack and examines the meat.{/n}
"That's what I chose. Have them bring it to the kiln, and I'll check it again there. No hunting scraps hidden underneath."
{n}She takes her own bowl and turns toward the slope.{/n}''',
          c('[Spend 100 Materials. Deliver the load for her inspection.]',
            flags=writes("custody", *DEEDS, "cost.commander_delivery_paid"),
            requires=(RENOUNCED,), crusade=("Materials", -100))),
        n("spilled", "Nidalynn", '''{n}The cart slews against a stone. A sack splits, spilling the extra meat into the gutter. Nidalynn catches the cart before it overturns, then looks at the mud.{/n}
"Leave that. She isn't eating it. I've enough in my own bowl for tonight."
{n}She lifts the bowl away from your hands.{/n}
"If you're replacing it, come in two days. And get someone who can hold a cart."''',
          c('[Right the cart.]', flags=writes("custody", "custody.failed", "cost.commander_feed_spilled"))),
        n("refused", "Nidalynn", '''{n}Nidalynn lifts her own sack from the cart.{/n}
"She stays with me. She eats tonight. You keep your supper."
{n}She shoulders the sack and sets off down the slope.{/n}
"If you change your mind, bring a fresh load in two days."''',
          c('[Leave the cart.]', flags=writes("custody", "custody.refused", "guardian_kept"))),
    ]


def repair_nodes():
    return [
        n("start", "Nidalynn", '''{n}The replacement cart waits on level ground this time. Nidalynn has filled another bowl from her stores. The watch changes on Drezen's wall above the kiln.{/n}
"She's fed. This is the extra load. Goat, not those scraps you wanted her chasing. The men will bring it down if you supply the materials."
{n}She opens the cover for you.{/n}
"I'm staying tonight. If she starts gnawing the door, I want to hear it before the watch does. Are you sending this down?"''',
          c('[Spend 150 Materials. Replace my supper with her chosen feed; deliver it for inspection.]',
            flags=writes("repair", *DEEDS, "cost.commander_delivery_paid"),
            requires=(RENOUNCED,), crusade=("Materials", -150)),
          c('"No delivery."', "refused"),
          c('[Later.]', abort=True)),
        n("refused", "Nidalynn", '''{n}Nidalynn closes the cover. She takes her own bowl and leaves the hired men beside the cart.{/n}
"Then we're finished with this. I'll feed her myself."
{n}The kiln door closes behind her. The cart stays where it is.{/n}''',
          c('[Leave.]', flags=writes("repair", "repair.refused", "unanswered", "guardian_kept"))),
    ]


def register(payload, scenes, refs):
    """Append this row only; no native effects, stance writers or solo-route changes."""
    derived = payload.setdefault("Derived", {})
    ready = [[N + "hatched", N + "egg_owed"]]
    if P + "ready" in derived and derived[P + "ready"] != ready:
        raise ValueError("Conflicting S50 ready adapter")
    derived[P + "ready"] = ready
    definitions = (
        ("notice", notice_nodes(), (P + "ready",), (P + "notice.seen",), (), 0),
        ("custody", custody_nodes(), (P + "notice.opened", N + "hatched"),
         (P + "custody.seen", P + "notice.refused", N + "lie_kept"), (), 48),
        ("repair", repair_nodes(), (N + "hatched",),
         (P + "repair.seen", P + "resolved", N + "lie_kept"),
         ((P + "custody.failed", P + "custody.refused"),), 48),
    )
    existing = {s["Id"] for s in scenes}
    for step, nodes, requires, forbids, groups, delay in definitions:
        for body, (hub, unit) in BODIES.items():
            sid = P + step + "." + body
            if sid in existing:
                continue
            presence_gates = (N + "hearth.grey_stone",) if body == "widow" else (N + "form_chosen",)
            body_veto = (N + "form_chosen",) if body == "widow" else ()
            scenes.append(scene(sid, "The next feed", "Nidalynn", 5,
                '"About the little one\'s next feed."', deepcopy(nodes),
                requires=("trickster", *requires, *presence_gates,
                          "nidalynn.presence.route_open", "nidalynn.present_now"),
                forbids=("nidalynn.closed", N + "left_with_it", "nidalynn.epoch_unavailable",
                         "trickster.failed", *forbids, *body_veto),
                delay=delay, last=5, Relationship="household", Chapters=[5],
                Areas=["2570015799edf594daf2f076f2f975d8"], InteractionHub=hub, ContactUnit=unit,
                Participants=["nidalynn"], RequiresAnyGroups=[list(g) for g in groups],
                RestAllowance="household.protected", HouseholdCategory="protected",
                HouseholdWitness=P + step + ".seen"))
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger:
        entries = ledger["Entries"]
        if not any(e["Id"] == P + "custody.record" for e in entries):
            entries.append(dict(Id=P + "custody.record", Section="Seating Notes", Portrait="Nidalynn",
                Title="Nidalynn's next feed", Text="{n}The saved child stays with Nidalynn.{/n}",
                Requires=[P + "notice.seen"], Forbids=[], AnyGroups=[], Lines=[
                    dict(Text="{n}The child stayed with Nidalynn. Her feed arrived. The woundwyrm's bill is still mine.{/n}",
                         Requires=[P + "resolved", BILL], Forbids=[], AnyGroups=[]),
                    dict(Text="{n}The child stayed with Nidalynn. Her feed arrived. Taking the egg is still mine to answer for.{/n}",
                         Requires=[P + "resolved"], Forbids=[BILL], AnyGroups=[]),
                    dict(Text="{n}Nidalynn kept the child and fed her herself. I refused the load.{/n}",
                         Requires=[P + "unanswered"], Forbids=[], AnyGroups=[]),
                ]))
    # Append only to Nidalynn's own epilogue page, retaining all existing answers.
    for host in scenes:
        if host["Id"] in (N + "epilogue.salt", N + "epilogue.late", "nidalynn.lastcall.page"):
            paragraph = p("{n}Nidalynn remembered the load brought to her kiln, and the night she spent guarding it. The youngster had stayed with her; feeding her had settled no quarrel with her mother.{/n}",
                          requires=(P + "resolved", P + "cost.nidalynn_guard_night", P + "cost.nidalynn_own_feed"))
            paragraphs = host["Nodes"][0].setdefault("Paragraphs", [])
            if paragraph not in paragraphs:
                paragraphs.append(paragraph)
        if host["Id"] == "trickster.lastcall.page.last_word":
            paragraph = p("{n}I gave up my supper for the youngster's next feed. Nidalynn supplied her own meat and stayed beside the kiln that night. She kept the child; the load I brought did not buy her from her mother.{/n}",
                          requires=(P + "resolved", P + "cost.commander_luxury_lost",
                                    P + "cost.nidalynn_guard_night", P + "cost.nidalynn_own_feed"))
            paragraphs = host["Nodes"][0].setdefault("Paragraphs", [])
            if paragraph not in paragraphs:
                paragraphs.append(paragraph)
