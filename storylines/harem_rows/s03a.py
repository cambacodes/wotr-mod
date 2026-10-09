"""S03a: authored shield-bench arc, hs-D optional contract and lore correction.

Native voice only: SeelahArueshalae/Banter_SeelahArueshalae_banter1.jbp,
c0d3797a796e0f74499eaa878fab87a9; enGB 6204233f-191e-4e2b-bcd7-7bc5da92d168
and bd4ddec6-ccbb-4510-8fc9-d0fac6a048d9. No bark is a dialogue attachment.
The existing Table is the entry; no native facts or route text are rewritten.
Attitude/stance/enmity producers remain controller-owned. No new echo.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.pair.seelah_arueshalae."
PAIR = ("seelah", "arueshalae")
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"
STEPS = ("company", "desire", "choice", "morning")


def p(suffix):
    return PREFIX + suffix


def flags(*suffixes):
    return tuple(p(s) for s in suffixes)


OUTCOMES = {
    ("company", "kept"): flags("company.seen", "company.kept", "deed.a_company",
                               "deed.b_company", "cost.a_company", "cost.b_company"),
    ("desire", "named"): flags("desire.seen", "desire.named", "deed.a_personal_answer",
                               "deed.b_personal_answer", "cost.a_personal_answer", "cost.b_personal_answer"),
    ("choice", "kept_safe"): flags("choice.seen", "choice.both_yes", "deed.a_chose", "deed.b_chose"),
    ("morning", "done"): flags("morning.seen", "morning.done", "deed.a_returned_to_duty", "deed.b_returned_to_duty"),
}
OUTCOMES["choice", "kept_warded"] = OUTCOMES["choice", "kept_safe"] + flags("choice.ward_spent")
for _step in STEPS[:3]:
    OUTCOMES[_step, "declined"] = flags(_step + ".seen", _step + ".declined", "arc.declined")

# Reviewed inputs for the controller; this module never writes attitude flags.
_lover = list(OUTCOMES["company", "kept"][1:] + OUTCOMES["desire", "named"][1:]
              + OUTCOMES["choice", "kept_safe"][1:])
STAGE_INPUTS = {
    (a, b, "lover"): [
        _lover + ["arueshalae.redeemed", "arueshalae.changed"],
        _lover + ["arueshalae.redeemed", p("choice.ward_spent")],
    ] for a, b in (PAIR, PAIR[::-1])
}


def terminal(step, result, speaker, text):
    return n(result, speaker, text, c("Continue", flags=OUTCOMES[step, result]))


def later():
    return c("[Later.]", abort=True)


def nodes(step):
    if step == "company":
        return [
            n("start", "Seelah", '''{n}The mess is emptying. Seelah has a dented shield across her knees; tomorrow's gate roster lies beside it. Arueshalae stands with the last stack of bowls.{/n}
"Sister! Put those down. I've got room here, and this damned strap needs another pair of hands."
"I could stay," {n}Arueshalae says, looking at the space beside her rather than the shield.{/n}''',
              c('"Leave them room on the bench."', "bench"),
              c('"Keep it to supper tonight."', "declined"), later()),
            n("bench", "Arueshalae", '''{n}Arueshalae sets down the bowls and takes the loose strap. Seelah turns the shield so they can work without their hands meeting.{/n}
"They asked me to sit with them again tomorrow. I thought they were only being polite."
"They liked having you there. So did I," {n}Seelah says. She passes over the awl, handle first.{/n} "Pull that tight. Cultists don't wait for a paladin to pick her shield up."''', c("Continue", "kept")),
            terminal(step, "kept", "Seelah", '''{n}Arueshalae holds the strap while Seelah drives the awl through it. The last soldiers leave; neither woman follows them.{/n}
"There. A shield that stays on my arm. Come back next supper?"
"Yes. Even if there is nothing to mend," {n}Arueshalae says.{/n}
{n}Seelah moves the bowls off the bench and leaves the place beside her clear.{/n}'''),
            terminal(step, "declined", "Seelah", '''"Supper, then. Bring your bowl over next time."
{n}Arueshalae smiles and takes the empty bowls away. Seelah braces the shield between her knees and finishes the strap herself.{/n}'''),
        ]
    if step == "desire":
        return [
            n("start", "Arueshalae", '''{n}After the mess clears, Arueshalae returns to Seelah's bench with a clean rag. Seelah has already scrubbed the shield twice. The muster bell will ring at dawn.{/n}
"You have missed a spot."
"Have I? Well, sit down and show me," {n}Seelah says.{/n}
{n}Arueshalae sits. She leaves the rag folded between them.{/n}''',
              c('"Let the work wait."', "seelah_answer"),
              c('"Keep it company."', "declined"), later()),
            n("seelah_answer", "Seelah", '''{n}Seelah puts the shield down.{/n} "You're not here for that spot. I'm glad. I wanted you to stay after the others left."
{n}She lays her bare hand on her own knee, close to Arueshalae without reaching for her.{/n}
"What did you come back for?"''', c("Continue", "arueshalae_answer")),
            n("arueshalae_answer", "Arueshalae", '''"You. I like hearing you laugh when nobody needs you to be brave."
{n}Arueshalae unfolds the rag, then folds it again.{/n} "The shield was an excuse. I wanted to stay."
"Good. I was running out of dents," {n}Seelah says.{/n}''', c("Continue", "named")),
            terminal(step, "named", "Arueshalae", '''"Will you meet me here again? Just you."
"Yes. And leave the rag behind," {n}Seelah says.{/n}
{n}Arueshalae takes it anyway, smiling. Seelah leaves the shield unfinished and walks with her as far as the soldiers' quarters.{/n}'''),
            terminal(step, "declined", "Seelah", '''"Then sit down. Tell me what happened on your watch."
{n}Arueshalae settles beside the shield. She tells Seelah about a sentry who mistook her wings for a cultist's shadow; Seelah's laughter brings the cook back to the door.{/n}'''),
        ]
    if step == "choice":
        return [
            n("start", "Seelah", '''{n}Seelah waits at the bench, out of her armor. Arueshalae comes without the rag. Seelah nudges the shield under the bench with her boot.{/n}
"Well. No work left to hide behind."
{n}Arueshalae looks at her mouth, then meets her eyes.{/n}''',
              c('"Leave them together."', "seelah_yes", requires=(p("choice.offer_ready"),)),
              c('"Keep it friendship."', "declined"), later()),
            n("seelah_yes", "Seelah", '''"I want to kiss you. I've been thinking about it on the bloody gate."
{n}Seelah laughs once, without looking away.{/n} "Your turn, sister."''',
              c("[Hear Arueshalae's answer.]", "arueshalae_yes"),
              c("[Let Seelah leave it at company.]", "seelah_no")),
            n("arueshalae_yes", "Arueshalae", '''"Yes. I want your mouth on mine."
{n}Her wings shift against the bench. She keeps her hands in her lap until Seelah gets up.{/n}''',
              c("[Leave them to each other.]", "cut", requires=("arueshalae.changed",)),
              c("[Bring the scroll to the shrine reader.]", "ward_application",
                requires=("arueshalae.ward_held",), forbids=("arueshalae.changed",)),
              c("[Let Arueshalae leave it at company.]", "arueshalae_no"),
              c("[Return with the scroll later.]", abort=True, forbids=(p("choice.offer_ready"),))),
            n("ward_application", "Seelah", '''{n}At the shrine steps, Seelah holds out her wrist to the chaplain. Arueshalae waits beside the unbroken scroll.{/n}
"Read it over me. We have seven minutes; I don't intend to spend them all on the stairs."''',
              c("[Have the reader spend the scroll on Seelah.]", "cut_warded",
                flags=flags("choice.ward_spent"), requires=("arueshalae.ward_held",), remove_item=SCROLL),
              c("[Return with the scroll later.]", abort=True, forbids=("arueshalae.ward_held",))),
            n("cut", "Arueshalae", '''{n}Arueshalae kisses Seelah before they reach the bench. Seelah catches her by the waist and answers, pulling her close.{/n}
"Not sister like that," {n}Arueshalae whispers against her lips.{/n}
"No. Not like that," {n}Seelah answers.{/n}
{n}The shield remains on the bench when they leave together.{/n}''', c("Continue", "explicit.1")),
            n("cut_warded", "Arueshalae", '''{n}The scroll burns away in the chaplain's hand. Back at the bench, Arueshalae kisses Seelah; Seelah pulls her against her chest and answers.{/n}
"Not sister like that."
"No. Not like that," {n}Seelah answers.{/n}
{n}Seelah glances at the chapel clock, then draws her toward the quarters. The shield remains on the bench.{/n}
{n}They do not make it decently down the corridor. Seelah has her pinned against the door of her room before it is shut, laughing against her neck, one hand already working the ties of the succubus's dress. Arueshalae's wings shudder and fold. "Seven minutes," she breathes. "I want every one of them." "Then stop talking, sister," Seelah says, and kisses her again, deep and greedy, and shoves the door closed with her boot. The dress goes. The shirt goes. Seelah's armour was left on the bench, and there is nothing now between the paladin's warm bare skin and the demon's, only the ward on Seelah's wrist and the loud, honest want in both of them. Arueshalae takes her in with her eyes, devout and starving. "Look at you," she says. "Gods. Look at you." Seelah drags her onto the bed.{/n}''', c("Continue", "explicit.1.warded")),
            n("explicit.1", "Narrator", "{n}Their door closes. The shield waits where Seelah left it.{/n}", c("Continue", "kept_safe")),
            n("explicit.1.warded", "Narrator", "{n}Their door closes. Before the seven minutes end, Arueshalae draws back and Seelah gathers the fallen blanket between them.{/n}", c("Continue", "kept_warded")),
            terminal(step, "kept_safe", "Arueshalae", '''"Your shield is still on the bench."
"It can wait until morning," {n}Seelah says, drawing her back down.{/n}'''),
            terminal(step, "kept_warded", "Arueshalae", '''"Your shield is still on the bench."
"It can wait. Come sit where I can see you," {n}Seelah says.{/n}
{n}Seelah makes room across the blanket. Arueshalae stays, keeping the cloth between their bare skin as the chapel clock strikes.{/n}'''),
            n("seelah_no", "Seelah", '''"I like having you here. But tonight I want your company, nothing more."
"Then I will stay for that," {n}Arueshalae says.{/n}''', c("Continue", "declined")),
            n("arueshalae_no", "Arueshalae", '''"I thought I wanted this tonight. I don't want to kiss you yet."
{n}Seelah sits back down.{/n} "All right. Tell me about that sentry again. The idiot with the spear," {n}she says.{/n}''', c("Continue", "declined")),
            terminal(step, "declined", "Seelah", '''{n}Seelah retrieves the shield. Arueshalae stays beside her while she finishes its rim; they leave for their separate quarters when the cook puts out the lamps.{/n}
"Supper tomorrow?"
"Of course," {n}Arueshalae says.{/n}'''),
        ]
    return [
        n("start", "Seelah", '''{n}The morning muster sounds. Seelah comes for her shield; Arueshalae waits beside it, bow strung.{/n}
"There it is. I thought you'd taken it to make me come looking."''',
          c("[Hear their next postings.]", "postings"), later()),
        n("postings", "Arueshalae", '''"East gate?"
"Until noon. You?" {n}Seelah asks.{/n}
"The scouts on the north road. I promised to watch the ridge," {n}Arueshalae says.{/n}
{n}Seelah slides her arm through the strap they mended together. Arueshalae checks her bowstring.{/n}''', c("Continue", "done")),
        terminal(step, "done", "Seelah", '''"Supper, then. Save me a place."
"Beside me," {n}Arueshalae says.{/n}
{n}Seelah goes toward the gate. Arueshalae takes the stairs to the north wall, looking back once before she joins the scouts.{/n}'''),
    ]


def register(payload, scenes, refs):
    if any(s["Id"] == p("company") for s in scenes):
        return
    for woman in ("seelah",):
        seat = payload.get("SeatWomen", {}).get(woman)
        if not seat or seat.get("Relationship") != woman or not seat.get("Requires"):
            raise ValueError("S03a needs current bodily SeatWomen: " + woman)
    payload.setdefault("Derived", {})[p("ready")] = [[household.KEPT,
        "seelah.harem.eligible", "arueshalae.harem.eligible", "arueshalae.redeemed"]]
    # Good recruitment is a Playing native read, separate from personality and
    # old return history. Current loss/epoch guards below still apply to it.
    payload["Derived"][p("arueshalae_body")] = [["arueshalae.recruited_drezen"],
                                               ["arueshalae.recruited_redoubt"]]
    # Offer availability only: holding a scroll does not mean a ward is applied.
    # Every draining contact still lies after this execution's actual removal.
    payload["Derived"][p("choice.offer_ready")] = [["arueshalae.changed"], ["arueshalae.ward_held"]]
    route = payload["Relationships"]["arueshalae"]
    payload["SeatWomen"].setdefault("arueshalae", dict(Relationship="arueshalae",
        Requires=["arueshalae.present_now", p("arueshalae_body")],
        UnavailableFlags=list(dict.fromkeys(route.get("UnavailableFlags", [])
                                            + route.get("EpochUnavailableFlags", []))),
        UnavailableOverrides={}))
    friends = tuple(a + ".harem.attitude." + b + ".friend" for a, b in (PAIR, PAIR[::-1]))
    pending = payload.setdefault("PendingHooks", [])
    for key in friends:
        if key not in pending:
            pending.append(key)
    for step, prior, delay in (("company", None, 0), ("desire", "company.kept", 48),
                               ("choice", "desire.named", 48), ("morning", "choice.both_yes", 8)):
        requires = ["trickster", "trickster.now", household.PAGE_TAKEN, household.KEPT,
                    household.STANCE_ELIGIBLE, p("ready"), "arueshalae.redeemed", p("arueshalae_body")]
        forbids = ["fool_king.gone", "trickster.failed", "arueshalae.corrupted",
                   "sacrifice", p(step + ".seen"), p("arc.declined")]
        overrides = {"sacrifice": "trickster.commander_back"}
        if prior:
            requires.append(p(prior))
        if step == "choice":
            requires.extend(friends + OUTCOMES["company", "kept"][1:] + OUTCOMES["desire", "named"][1:])
        for a, b in (PAIR, PAIR[::-1]):
            route = payload["Relationships"][a]
            requires.extend([a + ".harem.eligible", a + ".present_now"])
            forbids.extend([route["ClosedFlag"], *route.get("UnavailableFlags", []),
                            *route.get("EpochUnavailableFlags", []), a + ".returned_actor_lost", household.enmity(a, b)])
            if a == "seelah":
                overrides.update(route.get("UnavailableOverrides", {}))
            overrides[household.enmity(a, b)] = a + ".harem.reconciled." + b
            for key in (household.enmity(a, b), overrides[household.enmity(a, b)]):
                if key not in pending:
                    pending.append(key)
        body = scene(p(step), "The shield on the bench", "Seelah", 3 if step == "company" else 5,
            "[Seelah and Arueshalae: " + step + "]", nodes(step),
            requires=tuple(dict.fromkeys(requires)), forbids=tuple(dict.fromkeys(forbids)),
            delay=delay, optional=True, Relationship="household", Chapters=[3, 5] if step == "company" else [5],
            Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
            Participants=list(PAIR), ParticipantWomen=list(PAIR), Pair=list(PAIR),
            ForbidOverrides=overrides, RestAllowance="household.pair", HouseholdCategory="pair",
            HouseholdWitness=p(step + ".seen"), HouseholdArc=p("arc"), HouseholdArcStart=step == "company")
        scenes.append(body)
    consumers = dict(payload.get("ForesightConsumers", {}))
    consumers.update({p(step): household.PAGE_TAKEN for step in STEPS})
    payload["ForesightConsumers"] = consumers
    # Extend existing arc-start census only; never cap a continuation.
    for chapter in (3, 5):
        key = "household.cap.ch%d.arcs" % chapter
        count = payload.get("Counts", {}).get(key)
        if count is not None:
            if p("company.seen") not in count["Of"]:
                count["Of"].append(p("company.seen"))
            scenes[-4]["Forbids"].append(key)
