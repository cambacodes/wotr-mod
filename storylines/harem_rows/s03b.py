"""S03b: authored Ch5 hearing, hs-B sections 1–11; no intimacy or new lore.

Native voice evidence (not a dialog attachment): BlueprintBarkBanter
f5eef02280c7c2041b8356a483e8129a, SeelahEvilArueshalae/banter1_pack2;
enGB 2ea11ef8-776c-4560-8652-315c90602d8a / f62bedb2-1896-4fa8-9fc1-126dc73050a8.
Fall evidence: ArueshalaeIsEvil, e85e8acd74d231e44ad7d6d2d5dab43c,
already read by household.ARUESHALAE_BRANCH. Neither evidence supplies a body.

The controller owns attitudes/enmity. STAGE_INPUTS specifies its reviewed
directional inputs, without writing those states or choosing a failure owner.
Ruling 21 approves the existing deed-only primary and single retry; no second
tool, roll or extra charge is required. Failure direction stays controller-owned.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.pair.seelah_arueshalae.fallen."
PAIR = ("seelah", "arueshalae")


def p(suffix):
    return PREFIX + suffix


DEEDS = (
    "deed.arueshalae_owned_fall", "deed.seelah_named_account",
    "cost.arueshalae_desnan_cover_lost", "cost.seelah_sister_address_lost",
    "cost.commander_hearing",
)
OUTCOMES = {
    "settle": {
        "heard": ("settle.seen", "settle.done") + DEEDS,
        "misheard": ("settle.seen", "settle.failed", "cost.commander_false_account"),
        "refused": ("settle.seen", "settle.refused", "unsettled"),
    },
    "retry": {
        "heard": ("retry.seen", "retry.done", "settle.done") + DEEDS,
        "refused": ("retry.seen", "retry.refused", "unsettled"),
    },
}
STAGE_INPUTS = {
    ("seelah", "arueshalae", "rival"): [[p("settle.seen")]],
    ("arueshalae", "seelah", "rival"): [[p("settle.seen")]],
    ("seelah", "arueshalae", "respect"): [[p(s) for s in DEEDS[:4]]],
}


def _terminal(step, result, speaker, text):
    return n(result, speaker, text, c("Continue", flags=tuple(p(s) for s in OUTCOMES[step][result])))


def _nodes(step):
    retry = step == "retry"
    opening = (
        '''{n}The boy with the Desnan star on his bridle is back from the Wound road, alive, and saddling again. Arueshalae turns the little star over with one claw while Seelah watches from the stable door.{/n}
"Still hiding behind Desna, sister? Ask me again. I liked the answer."'''
        if retry else
        '''{n}In the stable yard three of Seelah's scouts are saddling for the Wound road. The youngest still has a little Desnan star tied to his bridle, the kind Arueshalae used to bless for anyone who asked. Seelah sees it, and sees Arueshalae watching it, and plants herself between them.{/n}
"They ride with you at dawn, and half of them think they're riding with a servant of Desna. I backed you once. I'm not going to pretend I didn't. So tell them what they're riding with. Your mouth, not mine."
{n}Arueshalae leans back against the stable door and stretches her wings until the horses shy.{/n}
"A succubus. They might even enjoy being disappointed."'''
    )
    choices = [c('"Let her tell them herself."' if retry else
                 '"Let her tell them herself. Every word."', "heard")]
    if not retry:
        choices.append(c('"Leave the boy his star. It keeps him brave."', "misheard"))
    choices.extend([
        c('"Nobody tells them anything."' if retry else '"Nobody tells them anything. Turn the horses out."', "refused"),
        c("[Later.]", abort=True),
    ])
    nodes = [n("start", "Arueshalae" if retry else "Seelah", opening, *choices),
             _terminal(step, "heard", "Arueshalae", '''{n}She walks down the line of horses, slowly, and stops at the youngest scout, the one with a little Desnan star still tied to his bridle. She flicks it with one claw.{/n} "I gave that up. The goddess, the prayers, the dreary little promises. I wanted to be hungry again, and now I am." {n}She leans in until he leans back against his horse.{/n} "Ride close to me tomorrow and you'll come home. Come close to me tonight and you won't. That's all you need to know about me, sweet."
{n}The boy cuts the star off his bridle himself. Seelah watches him do it, then turns to Arueshalae.{/n} "I was right to help you try. You chose what to do with it. I won't call you sister."
"Oh, I shall keep calling you sister. That face you make is delicious."
{n}Before nightfall Seelah moves the scouts' tents to the far side of the yard. Arueshalae laughs at that, and leaves them alone. For now.{/n}''')]
    if not retry:
        nodes.append(_terminal(step, "misheard", "Seelah", '''{n}Seelah turns on you, not on her.{/n}
"No. Desna's star doesn't make it true. She hasn't offered these boys a damned thing but her teeth."
{n}Arueshalae stretches, grinning at the paladin.{/n}
"But you liked me so much better that way. Leave him his trinket. It'll give him something to hold on to while I eat."
{n}Seelah says nothing more. The star stays on the bridle, and the scouts ride out at dawn believing what they believed.{/n}'''))
    nodes.append(_terminal(step, "refused", "Seelah", '''{n}Seelah turns the scouts' horses round with her own hands.{/n} "Then they don't ride with her. I'll take them up the Wound road myself."
"Do describe me properly on the way. Some of them have such dull imaginations."
{n}Arueshalae bares her teeth at Seelah. The paladin leads the horses out of the yard and does not look back.{/n}'''))
    return nodes


def _scene(payload, step):
    requires = ["trickster", "trickster.now", household.PAGE_TAKEN, household.STANCE_ELIGIBLE,
                household.KEPT, "arueshalae.corrupted", "arueshalae.evil_recruited",
                p("seelah_body"), p("ready")]
    forbids = ["fool_king.gone", "trickster.failed", "sacrifice", p(step + ".seen")]
    overrides = {"sacrifice": "trickster.commander_back"}
    for woman in PAIR:
        requires.extend([woman + ".harem.eligible", woman + ".present_now"])
        route = payload["Relationships"][woman]
        forbids.extend([route["ClosedFlag"], *route.get("UnavailableFlags", []),
                        *route.get("EpochUnavailableFlags", []), woman + ".returned_actor_lost"])
        # Seelah's existing return lifts only its declared loss. S03b never
        # revives either Arueshalae body, even when a legacy return flag survives.
        if woman == "seelah":
            overrides.update(route.get("UnavailableOverrides", {}))
    for woman, other in (PAIR, PAIR[::-1]):
        key = household.enmity(woman, other)
        forbids.append(key)
        overrides[key] = woman + ".harem.reconciled." + other
    if step == "retry":
        requires.append(p("settle.failed"))
        forbids.extend([p("settle.done"), p("unsettled")])
    return scene(
        p(step), "Whose colors", "Seelah", 5,
        "[Seelah and Arueshalae: the boy with the star]" if step == "retry" else
        "[Seelah and Arueshalae: whose colors?]", _nodes(step),
        requires=tuple(dict.fromkeys(requires)), forbids=tuple(dict.fromkeys(forbids)),
        last=5, delay=48 if step == "retry" else 0,
        Relationship="household", Chapters=[5], Areas=[household.DREZEN],
        InteractionHub=household.TABLE_HUB,
        Participants=list(PAIR), ParticipantWomen=[], Pair=list(PAIR),
        ForbidOverrides=overrides, RestAllowance="household.protected",
        HouseholdCategory="protected", HouseholdWitness=p(step + ".seen"),
    )


def register(payload, scenes, refs):
    """Append only S03b; the caller supplies the assembled relationship contracts."""
    if any(s["Id"] == p("settle") for s in scenes):
        return
    # Reserve controller-owned readers exactly as the household already does.
    # Pending hooks have no producer and grant no reconciliation or enmity.
    pending = payload.setdefault("PendingHooks", [])
    for woman, other in (PAIR, PAIR[::-1]):
        for key in (household.enmity(woman, other), woman + ".harem.reconciled." + other):
            if key not in pending:
                pending.append(key)
    payload.setdefault("Derived", {})[p("ready")] = [[
        "seelah.harem.eligible", "arueshalae.harem.eligible",
        "seelah.present_now", "arueshalae.present_now", "arueshalae.corrupted",
    ]]
    # present_now is a loss guard, not proof of an actor. The fallen woman
    # must be actually recruited; Seelah can attend with her native party body
    # or her existing, currently placeable Drezen copy. No letter-only arm.
    presence = payload["Presences"]["seelah.presence"]
    payload["Derived"][p("seelah_copy")] = [list(presence["Requires"])]
    payload.setdefault("DerivedForbids", {})[p("seelah_copy")] = list(dict.fromkeys([
        *presence["Forbids"], "seelah.presence.failed", "seelah.epoch_unavailable",
    ]))
    payload["Derived"][p("seelah_body")] = [["seelah.in_party"], [p("seelah_copy")]]
    scenes.extend(_scene(payload, step) for step in ("settle", "retry"))
    # The older builder aliases this map to an authoring global. Copy it so
    # isolated fixture registrations cannot leak into the next story build.
    consumers = dict(payload.get("ForesightConsumers", {}))
    consumers.update({p(step): household.PAGE_TAKEN for step in ("settle", "retry")})
    payload["ForesightConsumers"] = consumers
