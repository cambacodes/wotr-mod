"""S47: authored evidence commission and limited restitution inspection.

Yaniel attends her own presence; Areelu responds remotely at the native cell.
Fixed X: no affection, enmity, reconciliation or intimate-slot producer.
See tools/route_packs/harem/s47.md for canon evidence and registration timing.
"""
from story_format import c, n, p, scene

P = "household.pair.yaniel_areelu."
BEAT = "yaniel.trickster.beat.areelu"
HOST = "74989c07fc5fd8a42b18b333dc40acc1"
RETURN = "3d63aae9686620845acc8be95e490c26"
DESTROYED = P + "projector.destroyed"
LIVE = ("yaniel.trickster.returned", "yaniel.freed.latched", "yaniel.present_now")
LOSS = ("yaniel.closed", "yaniel.killed.latched", "yaniel.trickster.left_free")


def later():
    return c("[Later.]", abort=True)


def request(completion=()):
    return n("household_face_request", "Yaniel",
             '{n}Yaniel takes a scrap of paper and the lamp from the gate stair. She blackens a finger and draws the line of her cheek, the scar, the mouth. A horn sounds from the wall; she keeps working.{/n} '
             '"You saw her take off my face in Drezen. Tell her what you saw. Take this to her laboratory and make her show you where she will stop using my name and likeness. I want the original back. She has had enough of me." '
             '{n}She folds the comparison with the marked side inward.{/n} "Go before you lose your chance to speak to her there. Smashing her crystal will not answer this."',
             c("[Carry the comparison and her demand for an inspection.]",
               flags=(*completion, P + "commission.seen", P + "proof.ready", P + "cost.yaniel_comparison")),
             c('"I will not carry it."', flags=(*completion, P + "commission.seen", P + "commission.declined")),
             later())


def inspection():
    def finish(text, *flags):
        return c(text, flags=(P + "inspection.seen", *(P + flag for flag in flags)))
    return scene(P + "inspection", "The borrowed face", "Areelu", 5,
                 '"Yaniel sent evidence. I brought it without borrowing her face."', [
        n("start", "conversant",
          '{n}The projection turns toward the folded paper. Beside the crystal lie the pages of the guise, taken down from life while Yaniel lay on her tables: the voice, the stance, the scar, the way she carries her sword hand.{/n} "She survived the Fane and now sends me a likeness. Does she think I have forgotten it? I studied that face for years before I wore it. Unfold it. I can see from here."',
          c("[Lay the comparison beside the projected face.]", "comparison"),
          c('"Forget it. Keep using what you took."', "declined"), later()),
        n("comparison", "conversant",
          '''"Yes. That is the face I wore. It opened doors that would have closed against mine, and men wept to see it and told it everything." {n}The projection indicates a line in the pages without touching it.{/n} "Her name. Her appearance. Useful among crusaders. Less useful now that she walks your walls and can contradict me."
{n}A cult lookout could still be deceived by that face. The comparison lies within your reach.{/n}''',
          c('"Give up using her name and likeness in your reconnaissance and published work. I will give up the lookout con."', "undertaking"),
          c("[Leave the original comparison in Areelu's laboratory.]", "retained"),
          c("[Take the evidence away without a remedy.]", "unsettled"), later()),
        n("undertaking", "conversant",
          '''"Strike out that entry. Name and likeness, both. I will retire the guise; I have worn better. My notes remain mine. So do my other faces." {n}She watches the pen in your hand.{/n} "And you will not put her name to a lie made from my work. I have enough enemies producing those without your assistance."
{n}Yaniel's original lies beside the pages. The exclusion is still waiting for your pen.{/n}''',
          finish("[Strike out the entry, check the exclusion and take the originals home.]",
                 "inspection.remedied", "proof.quest_done", "face.excluded", "original.returned",
                 "cost.areelu_specific_guise", "cost.commander_reconnaissance"), later()),
        n("retained", "conversant",
          '"Leave it on the bench. I may want to wear her again when my work here resumes, and a fresh likeness saves a great deal of guessing." {n}The original is still in your hand. Yaniel lent it for inspection; leaving it would give the witch a fresh likeness to keep.{/n}',
          finish("[Leave the original on the bench.]", "inspection.unsettled", "original.retained", "mandate.broken"), later()),
        n("unsettled", "conversant",
          '"Then take it. She can keep her accusation. I can keep my methods." '
          '{n}The index remains open, its entry untouched.{/n}',
          finish("[End the inspection.]", "inspection.unsettled", "inspection.withdrawn"), later()),
        n("declined", "conversant",
          '"You intend to withdraw her demand yourself? Does Yaniel know how readily you speak for her?" '
          '{n}The projection waits. The paper remains beside the untouched index.{/n}',
          finish("[End the inspection.]", "inspection.declined", "face.unanswered"), later()),
    ], requires=("trickster", "foresight.page_taken", P + "proof.ready", P + "contact.open", *LIVE),
       forbids=(*LOSS, "areelu.closed", DESTROYED, P + "inspection.seen", P + "commission.declined", "trickster.failed"),
       last=5, Chapters=[5], Relationship="household", AnswerLists=[HOST], NativeReturnCue=RETURN,
       RestAllowance="household.protected", HouseholdCategory="protected", HouseholdWitness=P + "inspection.seen")


def append_nodes(body, nodes):
    ids = {node["Id"] for node in body["Nodes"]}
    body["Nodes"].extend(node for node in nodes if node["Id"] not in ids)


def append_choice(node, choice):
    if not any(old.get("Next") == choice.get("Next") for old in node["Choices"]):
        node["Choices"].append(choice)


def register(payload, scenes, refs):
    # Work on the assembled copies; source dialogue must survive repeat builds.
    from storylines import yaniel_trickster
    beat = next(s for s in scenes if s["Id"] == BEAT)
    for node in beat["Nodes"]:
        if node["Id"] in ("end", "end_refused", "end_unknown"):
            append_choice(node, c("[Ask what she wants carried to the witch.]", "household_face_request",
                                  requires=("trickster", "foresight.page_taken", *LIVE),
                                  forbids=(*LOSS, P + "commission.seen")))
    append_nodes(beat, [request((BEAT,))])

    # The old beat excludes commitment and becomes spent after completion.
    # This presence entry covers those histories without a second commission.
    commission = scene(P + "commission", "Yaniel's comparison", "Yaniel", 5,
                       '"What do you want done about your stolen face?"', [request()],
                       requires=("trickster", "foresight.page_taken", "yaniel.areelu_unmasked", *LIVE),
                       forbids=(*LOSS, P + "commission.seen", "trickster.failed"),
                       last=5, Chapters=[5], Relationship="yaniel", InteractionHub="yaniel.presence",
                       Areas=[yaniel_trickster.DREZEN], ContactUnit=yaniel_trickster.UNIT,
                       RequiresAnyGroups=[["yaniel.committed", BEAT]])
    # Presence commission is a private discovery, not another protected docket.
    commission["Nodes"][0]["Id"] = "start"
    for body in (commission, inspection()):
        if not any(s["Id"] == body["Id"] for s in scenes):
            scenes.append(body)
    # Bind the observed projector destruction on this assembled payload.
    payload.setdefault("SeenCues", {})[DESTROYED] = ["591acfaf8500cc94aa7a8918db767d43"]
    payload.setdefault("Derived", {})[P + "contact.open"] = [["areelu.trickster.primed"]]
    payload.setdefault("DerivedOpenRoutes", {})[P + "contact.open"] = ["areelu", "yaniel"]

    watch = next(s for s in scenes if s["Id"] == "yaniel.trickster.after.watch")
    start = next(n for n in watch["Nodes"] if n["Id"] == "start")
    append_choice(start, c("[Return her comparison and describe the exclusion.]", "household_face_returned",
                          requires=(P + "proof.quest_done", P + "original.returned", *LIVE)))
    append_choice(start, c("[Tell her you left the original in the laboratory.]", "household_face_broken",
                          requires=(P + "mandate.broken", *LIVE), forbids=(P + "original.returned",)))
    append_nodes(watch, [
        n("household_face_returned", "Yaniel",
          '{n}She checks the blackened paper against her cheek, then folds it away.{/n} "My face, my name. Those were what I sent you for. Good. You have given up a useful lie yourself." '
          '{n}She takes the spear from the wall.{/n} "She still poisoned me. She still left me in the Fane. This does not buy her a place on my watch."', c("Continue", "talk")),
        n("household_face_broken", "Yaniel",
          '{n}Her hand closes on the spear shaft.{/n} "I lent it to you. Not to her. You have given the woman who wore my face another one to study. Bring the original back, Commander." '
          '{n}The relief horn sounds. She turns toward the stair without offering you the second cup.{/n}',
          c("[Finish the watch.]", flags=("yaniel.trickster.after.watch_stood",))),
    ])
    wager = next(s for s in scenes if s["Id"] == "areelu.trickster.wager.raised")
    append_choice(wager["Nodes"][0], c('"You excluded Yaniel\'s face from your work."', "household_face_price",
                                     requires=(P + "cost.areelu_specific_guise",)))
    append_nodes(wager, [n("household_face_price", "conversant",
                          '"One useful disguise, discarded. My observations remain. If you expect me to weep over the page you crossed out, you will wait longer than either of us has before this Wound closes."',
                          c("[Return to the wager.]", "start"))])

    entry = dict(Id=P + "record", Section="Seating Notes", Portrait="Yaniel", Title="Yaniel's stolen face",
                 Text="{n}Yaniel's stolen face.{/n}",
                 Requires=[P + "commission.seen"], Forbids=[], AnyGroups=[], Lines=[
        dict(Text="{n}Yaniel's comparison must reach the laboratory projection before I leave it behind or smash its crystal.{/n}", Requires=[P + "proof.ready"], Forbids=[P + "inspection.seen"]),
        dict(Text="{n}She wore Yaniel's face. I have brought back no undertaking about the next time.{/n}", Requires=[], Forbids=[P + "proof.quest_done", P + "mandate.broken"]),
        dict(Text="{n}One face excluded from the work. The woman who took it still keeps her notes. I gave up using that face against a cult lookout; Yaniel spent a watch making the comparison.{/n}", Requires=[P + "proof.quest_done"], Forbids=[]),
        dict(Text="{n}Yaniel lent me her comparison. I lent it on. She knows whose hands did that.{/n}", Requires=[P + "mandate.broken"], Forbids=[]),
    ])
    entries = payload["Books"]["trickster.ledger"]["Entries"]
    if not any(e["Id"] == entry["Id"] for e in entries):
        entries.append(entry)
    # Epilogue-only historical readers: no new living attendance after a death
    # or an unreturned Commander sacrifice, and no implication of forgiveness.
    records = {
        "yaniel": [
            p("{n}Before Threshold, Yaniel spent a watch making a comparison of the face Areelu had stolen. The Commander carried it under an inspection-only mandate.{/n}", requires=(P + "cost.yaniel_comparison",)),
            p("{n}The original came home. The exclusion covered Yaniel's name and likeness; it answered neither her captivity nor the poison.{/n}", requires=(P + "proof.quest_done", P + "original.returned")),
            p("{n}The Commander left Yaniel's original in Areelu's laboratory. That breach remained beside the accusation; no returned original answered it.{/n}", requires=(P + "mandate.broken",), forbids=(P + "original.returned",)),
        ],

    }
    for partner, paragraphs in records.items():
        host = next(s for s in scenes if s["Id"] == partner + ".lastcall.page")
        target = host["Nodes"][0].setdefault("Paragraphs", [])
        have = {para["Text"] for para in target}
        target.extend(para for para in paragraphs if para["Text"] not in have)
