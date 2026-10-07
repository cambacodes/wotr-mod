"""S13: authored refusal acknowledgment and observation-bench courtship.

hs-D S13/common optional contract; harem-lore-check S13 supersedes the
private-name morning. Canon voice anchor only (not a SeenCue): BarkBanter
d9385a06a241d7740bef2a585da1edda, NenioArueshalae_banter3; enGB
70e86d99-0ef8-4a25-a017-75c79a18c4d7 / a50efc76-6ed7-41e4-9419-419c098a714d.
Verified directly in /wrath/blueprints.zip and enGB.json. No native rewrite,
return, echo, attraction check, commitment, stance or reconciliation producer.
Optional scenes remain retired until sheet BUDGET-D is reviewed. No new cap.
W5 owns qualified contact/Notes/Last Call readers; the integrator owns attitudes.
"""
from story_format import c, n
from storylines import household

P = "household.pair.nenio_arueshalae."
PAIR = ("nenio", "arueshalae")
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"
REFUSED = "nenio.experiment_refused"
COMMON = ("trickster.now", "nenio.present_now", "arueshalae.present_now",
          P + "body.nenio", P + "body.arueshalae", "arueshalae.redeemed")
EXCLUDED = ("arueshalae.corrupted", "trickster.failed", "fool_king.gone",
            "household.closed", "engine.l12.commander_unreturned",
            "nenio.closed", "arueshalae.closed", "nenio.epoch_unavailable",
            "arueshalae.epoch_unavailable", "nenio.killed_by_commander",
            "arueshalae_dead", "arueshalae.evil_dead")
COMPANY = ("company.kept", "deed.a_company", "deed.b_company", "cost.a_company", "cost.b_company")
DESIRE = ("desire.named", "deed.a_personal_answer", "deed.b_personal_answer",
          "cost.a_personal_answer", "cost.b_personal_answer")
CHOICE = ("choice.both_yes", "deed.a_chose", "deed.b_chose")


def flags(*suffixes):
    return tuple(P + key for key in suffixes)


def page(key, speaker, text, *answers):
    return n(key, speaker, text, *answers, portrait=speaker if speaker != "Narrator" else "")


def terminal(key, speaker, text, *writes):
    return page(key, speaker, text, c(flags=flags(*writes)))


def later():
    return c("[Later.]", abort=True)


def declined(step, text):
    return terminal("declined", "Arueshalae", text, step + ".seen", step + ".declined", "arc.declined")


def acknowledgment():
    return [
        page("start", "Arueshalae", '''{n}Nenio has brought a chronometer to the corner table. Arueshalae keeps her hands beneath it. Outside, a wagon rattles toward the siege stores.{/n}
"Commander, she wants to time a kiss. I told her no."
"A potentially informative measurement," {n}Nenio says.{/n}
"I know what it is to kill someone with a kiss. I am not making an experiment of it."''',
             c('"Hear why she refused."', "refusal"), later()),
        page("refusal", "Arueshalae", '''"I spent too long taking things from people. You come to me with a clock, as if none of that matters."
{n}She pushes the chronometer back toward Nenio without touching her hand.{/n}
"Do not ask me for that experiment again."
"Then the proposed experiment cannot be performed," {n}Nenio says. She shuts its case.{/n}''',
             c("Continue", "heard")),
        page("heard", "Nenio", '''"A refusal, not a result. I shall have to find a different question."
{n}Arueshalae takes her cup from the far end of the table. Nenio makes no move to follow her.{/n}''',
             c(flags=(P + "ack.seen", P + "ack.heard", REFUSED))),
    ]


def company():
    return [
        page("start", "Narrator", '''{n}Nenio has dragged a bench beneath the tavern window to watch the bats above Drezen's wall. Arueshalae stops beside her with a patrol quiver under her arm.{/n}
"Demon girl! You can distinguish them from here?" {n}Nenio asks.{/n}
"Yes. But I am not catching them for you," {n}Arueshalae says.{/n}
"I require someone to count them. There is room on the bench," {n}Nenio says.{/n}''',
             c('"Let them keep ordinary company."', "observation"),
             c('"Leave the observation for another evening."', "declined"), later()),
        page("observation", "Nenio", '''"Three crossed the tower."
"Four. One flew behind the others," {n}Arueshalae says.{/n}
{n}Nenio moves her notebook so Arueshalae can sit without their bodies touching.{/n}
"Show me where."
{n}Arueshalae points past the parapet, then sits down. Her quiver lies across her knees.{/n}
"I have a little time before the patrol. I wanted to see them, too."''', c("Continue", "kept")),
        terminal("kept", "Arueshalae", '''"That one has a torn wing. It still comes here."
"Repeated observation will establish its route," {n}Nenio says.{/n}
"Then save this end of the bench. I will look again."
{n}Nenio moves her pile of notes off it. They watch until the patrol horn sounds.{/n}''',
                 "company.seen", *COMPANY),
        declined("company", '''{n}Arueshalae lifts her quiver.{/n} "I should go to the wall."
"I shall count them myself, then," {n}Nenio says, retrieving her notebook from the empty end of the bench.{/n}'''),
    ]


def desire():
    return [
        page("start", "Nenio", '''{n}The bench is free again. Beyond the window, a relief patrol climbs the tower steps. Nenio has her chronometer open, but watches Arueshalae instead of its hands.{/n}
"I have a question. The instrument will not answer it."
"Then why is it out?" {n}Arueshalae asks.{/n}''',
             c('[Put the chronometer away.]', "nenio_answer"),
             c('"Keep this an evening of observation."', "declined"), later()),
        page("nenio_answer", "Nenio", '''{n}You shut the case. Nenio puts it in her bag.{/n}
"I am looking at you instead of the bats. Repeatedly. I want you to stay after they have gone."
"For another experiment?" {n}Arueshalae asks.{/n}
"No. That question was refused. This one concerns what I want."''', c("Continue", "arueshalae_answer")),
        page("arueshalae_answer", "Arueshalae", '''"I come here even when I know you have nothing new to show me. I want to sit beside you. Sometimes I want much more."
{n}Her eyes drop to Nenio's mouth. She grips the edge of the bench rather than reaching for her.{/n}
"That frightens me. But it is you I want, Nenio. Not the question."''', c("Continue", "named")),
        terminal("named", "Nenio", '''"Then I want to meet you here when neither of us is observing bats."
"You will still notice them," {n}Arueshalae says. She is smiling now.{/n}
"Possibly. I shall remain on the bench."
{n}They stay until Arueshalae must take her bow to the wall.{/n}''', "desire.seen", *DESIRE),
        declined("desire", '''"The bench is enough," {n}Arueshalae says. She turns toward the window.{/n}
{n}Nenio opens her notebook. They resume counting the bats above the siege tower.{/n}'''),
    ]


def choice(warded=False):
    finish = "kept_warded" if warded else "kept_safe"
    after_yes = "ward_application" if warded else "cut"
    nodes = [
        page("start", "Narrator", '''{n}The evening patrol has gone. Nenio clears the notes from the bench; Arueshalae leaves her bow beside the window.{/n}
"I came for you," {n}Arueshalae says.{/n}
"Good. I have put the chronometer away," {n}Nenio replies.{/n}''',
             c('[Leave them their personal answer.]', "nenio_yes",
               requires=("arueshalae.ward_held",) if warded else ()),
             c('"Keep this friendship at the bench."', "declined"), later()),
        page("nenio_yes", "Nenio", '''"I want to kiss you. Not to time it."
{n}She leaves her bag beneath the bench and waits, looking directly at Arueshalae.{/n}''',
             c("Continue", "arueshalae_yes")),
        page("arueshalae_yes", "Arueshalae", '''"Yes. I want your mouth on mine."
{n}Arueshalae loosens the fastening at her throat. Nenio's gaze follows her fingers.{/n}''',
             c("Continue", after_yes)),
        page("cut", "Narrator", ('''{n}The chapel's ward is still cold on Nenio's skin when she returns. Arueshalae draws her close and kisses her. Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands. They leave the bench for the room above, with seven minutes before the ward expires.{/n}'''
             if warded else '''{n}Arueshalae draws Nenio close and kisses her. Nenio catches the loosened collar in her fingers; Arueshalae presses into her hands. They leave the observation unfinished and climb the stairs together.{/n}'''),
             c("Continue", P + "choice.explicit.1")),
        terminal(finish, "Arueshalae", ('''{n}They separate before the ward fades. Arueshalae straightens Nenio's collar, then retrieves her bow downstairs.{/n}
"I will see you at the bench."
"After your patrol," {n}Nenio says, taking her bag to her own room.{/n}'''
             if warded else '''{n}Later, Arueshalae retrieves her bow downstairs. Nenio follows with her bag under her arm.{/n}
"I will see you at the bench," {n}Arueshalae says.{/n}
"After your patrol," {n}Nenio replies. They part at the stairs.{/n}'''),
                 "choice.seen", *CHOICE, *(("choice.ward_spent",) if warded else ())),
        declined("choice", '''"Then stay beside me here," {n}Arueshalae says.{/n}
{n}Nenio sits at the other end of the bench. They watch the patrol lights pass along the wall.{/n}'''),
    ]
    if warded:
        # Fallback remains selectable if inventory changes after the root answer.
        nodes.append(page("ward_application", "Narrator", '''{n}Nenio takes a scroll to the chapel. Arueshalae waits at the bench. They have not touched.{/n}''',
            c('[Have the chaplain read Death Ward over Nenio.]', "cut", requires=("arueshalae.ward_held",),
              remove_item=SCROLL, flags=flags("choice.ward_spent")),
            c('[Leave the scroll and return to ordinary company.]', "declined")))
    # Slot carries no effects; empty/filled text leads to the same aftermath.
    nodes.append(page(P + "choice.explicit.1", "Narrator",
                      "{n}The chronometer stays in its case downstairs.{/n}", c("Continue", finish)))
    return nodes


def morning():
    return [
        page("start", "Narrator", '''{n}Arueshalae returns from the dawn patrol. Nenio has opened her notebook at the observation bench, leaving the other end clear.{/n}
"I have another watch tonight," {n}Arueshalae says.{/n}''',
             c('"Will you meet here again?"', "meeting"), later()),
        page("meeting", "Nenio", '''"I intend to examine the marks on the north tower before dusk. After that, I will come here."
"I can come after the watch. Without my bow this time," {n}Arueshalae says.{/n}
"Bring it if you need it. I am asking for you."
{n}Arueshalae sits long enough to share the bread she brought back from the wall.{/n}''', c("Continue", "done")),
        terminal("done", "Arueshalae", '''"After the watch, then. Save my place."
{n}She goes to inspect her arrows. Nenio packs her notes for the tower, leaving the chronometer in her bag. The bench waits for their next meeting.{/n}''',
                 "morning.seen", "morning.done", "deed.a_returned_to_duty", "deed.b_returned_to_duty"),
    ]


def register(payload, scenes, refs):
    if any(s["Id"] == P + "ack" for s in scenes):
        return
    derived = payload.setdefault("Derived", {})
    negative = payload.setdefault("DerivedForbids", {})
    derived[P + "ack.ready"] = [["household.table.kept", "nenio.harem.eligible",
                                 "arueshalae.harem.eligible", "arueshalae.redeemed"]]
    # S10 integration supplies Nenio's current party/capital-copy body reader.
    seat = payload.get("SeatWomen", {}).get("nenio", {})
    if not seat.get("Requires"):
        raise ValueError("S13 needs Nenio's qualified bodily SeatWomen contract")
    derived[P + "body.nenio"] = [list(seat["Requires"])]
    derived[P + "body.arueshalae"] = [["arueshalae.recruited_drezen", "arueshalae.native_alive"],
                                      ["arueshalae.recruited_redoubt", "arueshalae.native_alive"]]
    for key in ("body.nenio", "body.arueshalae"):
        payload.setdefault("DerivedOpenRoutes", {})[P + key] = list(PAIR)
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b,
                    a + ".harem.attitude." + b + ".friend"):
            if key not in pending:
                pending.append(key)
    # Local earned descriptions; shared attitudes remain the integrator's job.
    for woman, other_side in (("nenio", "b"), ("arueshalae", "a")):
        friendship = ("company.kept", "deed." + other_side + "_company", "cost." + other_side + "_company",
                      "deed." + other_side + "_personal_answer", "cost." + other_side + "_personal_answer")
        derived[P + woman + ".friend"] = [[REFUSED, *flags("ack.heard", *friendship)]]
        earned = [REFUSED, *flags("ack.heard", *COMPANY, *DESIRE, *CHOICE), "arueshalae.redeemed"]
        derived[P + woman + ".lover"] = [earned + ["arueshalae.changed"], earned + [P + "choice.ward_spent"]]
        for stage in ("friend", "lover"):
            key = P + woman + "." + stage
            payload.setdefault("DerivedOpenRoutes", {})[key] = list(PAIR)
            negative[key] = ["arueshalae.corrupted"]
    definitions = [
        ("ack", acknowledgment(), "ack.ready", (), (), 0, (3, 5)),
        ("company", company(), "ack.heard", (REFUSED,), (), 0, (3, 5)),
        ("desire", desire(), "company.kept", flags(*COMPANY), (), 48, (5,)),
        ("choice", choice(), "desire.named", ("arueshalae.changed",), (), 48, (5,)),
        ("choice.warded", choice(True), "desire.named", (), ("arueshalae.changed",), 48, (5,)),
        ("morning", morning(), "choice.both_yes", flags(*COMPANY, *DESIRE), (), 8, (5,)),
    ]
    for step, nodes, trigger, needs, excludes, delay, chapters in definitions:
        lock = "choice" if step.startswith("choice") else step
        protected = step == "ack"
        if not protected:
            needs += flags("ack.heard")
        if lock == "choice":
            needs += (REFUSED, *flags(*COMPANY, *DESIRE),
                      "nenio.harem.attitude.arueshalae.friend", "arueshalae.harem.attitude.nenio.friend")
        body = household.table_entry(P + step, "The chronometer put away",
            "[Nenio and Arueshalae: " + ("the refused experiment" if protected else "the observation bench") + "]",
            nodes, PAIR, P + trigger, requires=COMMON + tuple(needs),
            forbids=EXCLUDED + flags(lock + ".seen") + tuple(excludes)
                    + (() if protected else flags("arc.declined", "ack.heard")),
            delay=delay, chapters=chapters, ParticipantWomen=list(PAIR),
            RestAllowance="household.protected" if protected else "household.pair",
            HouseholdCategory="discovery" if protected else "pair", HouseholdWitness=P + lock + ".seen",
            HouseholdArc=P.rstrip("."), HouseholdArcStart=step == "company")
        # BUDGET-D retirement uses the already-required acknowledgment witness;
        # no new gate, mechanic, shortened arc or continuation cap is invented.
        if not protected:
            body.update(ManualOnly=True, Remote=True, Kind="event")
            body.pop("InteractionHub", None)
        household.ENTRIES.pop()
        scenes.append(body)
        payload.setdefault("ForesightConsumers", {})[body["Id"]] = household.PAGE_TAKEN


def ledger_entry():
    """W5 reservation: historical account only; no speech/attendance assertion."""
    return dict(Id=P + "record", Section="Seating Notes", Portrait="Nenio", Title="Nenio and Arueshalae",
                Text="{n}The chronometer put away.{/n}", Requires=[P + "ack.heard"], Forbids=[], Lines=[
                    dict(Text="{n}The scientific request stayed refused.{/n}", Requires=[REFUSED], Forbids=[]),
                    dict(Text="{n}They made another appointment at the bench, after their separate duties.{/n}",
                         Requires=[P + "morning.done"], Forbids=[]),
                    dict(Text="{n}They kept their company; the private invitation ended there.{/n}",
                         Requires=[P + "arc.declined"], Forbids=[])])
