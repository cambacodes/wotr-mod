"""S25: authored display quarrel; optional courtship retired pending a real stay.

Canon anchors and the body-window blocker are documented in the S25 pack.
Only deed witnesses are written here; household policy remains engine-owned.
"""
import copy

from story_format import c, n, scene
from storylines import household

P = "household.pair.camellia_vellexia."
PAIR = ("camellia", "vellexia")
DREZEN = "2570015799edf594daf2f076f2f975d8"
BODY = ("camellia.present_now", "vellexia.present_now", "vellexia.trickster.in_person")
ENVELOPE = ("trickster", "foresight.page_taken", "household.stance_eligible", "household.table.kept",
            "camellia.harem.eligible", "vellexia.harem.eligible", *BODY)
EXCLUSIONS = ("household.closed", "fool_king.gone", "trickster.failed", "engine.l12.commander_unreturned",
              "camellia.closed", "vellexia.closed", "camellia.epoch_unavailable", "vellexia.epoch_unavailable",
              "vellexia.trickster.kept_as_mirror", "vellexia.trickster.visited", "vellexia.presence.failed")
RESPECT = ("display.answer_kept", "camellia.appraisal_owned", "vellexia.answer_given",
           "cost.camellia.public_poised_mask_spent", "cost.vellexia.easy_applause_lost")
FRIEND = (*RESPECT, "company.both_friends", "camellia.criticism_entrusted", "vellexia.private_answer_kept",
          "cost.camellia.private_envy_owned", "cost.vellexia.spectacle_abandoned")
LOVER = (*FRIEND, "desire.both_interested", "camellia.counterinvited", "vellexia.display_left", "choice.both_yes")


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


def result(node, speaker, text, *writes):
    return n(node, speaker, text, c(flags=flags(*writes)), portrait=speaker if speaker != "Narrator" else "")


def settlement(step):
    """Both methods reach the same personal concessions before publishing deeds."""
    writes = (step + ".seen", step + ".kept", *RESPECT, "cost.commander.clearing_time")
    return [
        n("answer", "Camellia", '''"You have made quite a study of being admired. The dress, the pause before you speak... Do your guests ever notice how little you have said?"
{n}Camellia's smile holds, but her fingers tighten on the edge of the table.{/n}
"I would enjoy seeing them applaud me for that little effort."''', c(next="vellexia"), portrait="Camellia"),
        n("cleared", "Narrator", '''{n}You carry the gilded display stand away from the table. The courtiers drift back toward the King's beer. Camellia does not follow them.{/n}
"If you want an ornament, buy one. I came to speak," {n}she says.{/n}
"Then speak, darling. I have just lost a perfectly serviceable audience."''', c(next="answer")),
        result("vellexia", "Vellexia", '''"Little effort? You are watching every inch of it. Poor darling. All that polish, and you still look hungry."
{n}Vellexia turns her chair toward Camellia, leaving the departing courtiers behind her.{/n}
"Keep the pretty smile for your crusaders. Tell me what you want to know. I shall answer you — if the question amuses me."
{n}Camellia draws her chair closer. Outside, a horn calls another company to the walls.{/n}''', *writes),
    ]


def primary_nodes():
    return [
        n("start", "Narrator", '''{n}A gilded stand crowds the corner table. Vellexia has perched her cup on it; Camellia watches the courtiers laugh at the demon's latest insult. Beyond the tavern windows, soldiers haul siege bolts toward the wall.{/n}
"Such ease," {n}Camellia says.{/n} "You hardly trouble to conceal what you want."
"And you trouble yourself so much. Come here, darling. You would improve this dreary display."
{n}Camellia remains beside the table.{/n} "I said I admired your ease. I did not offer to decorate it."''',
          c('"Give her an answer worth keeping, Camellia."', check=dict(Skill="CheckDiplomacy", DC=22,
            Success="answer", Failure="botched", CommanderOnly=True)),
          c('"I\'ll clear the display. You can argue without an audience."', "cleared"),
          c('"Keep your separate evenings."', "declined"), c("Later.", abort=True)),
        *settlement("settle"),
        result("botched", "Camellia", '''{n}A courtier laughs before Camellia can finish. She gives him a smile sharp enough to stop him.{/n}
"How delightful. I came to speak, and you have found me a chorus."
"A chorus needs a better song," {n}Vellexia says. She turns back to her guests. Camellia leaves the stand between them.{/n}''',
               "settle.seen", "settle.failed", "display.answer_cut_off"),
        result("declined", "Vellexia", '''"Then take your lovely manners elsewhere, darling. I have seen enough of them for tonight."
{n}Camellia inclines her head without bowing. Neither moves her chair toward the other.{/n}''', "settle.seen", "settle.declined"),
    ]


def retry_nodes():
    return [
        n("start", "Camellia", '''{n}Camellia stops beside the display stand. The tavern is loud with soldiers back from the walls; her voice cuts through the noise.{/n}
"There it is again. Perhaps we might finish without someone laughing on command."
"You remembered," {n}Vellexia says, delighted.{/n} "I was beginning to think you had nothing under that smile."''',
          c('"I\'ll clear it. Let each answer for herself."', "cleared"),
          c('"Camellia can be part of the display."', "failed"),
          c('"Leave them apart."', "declined"), c("Later.", abort=True), portrait="Camellia"),
        *settlement("retry"),
        result("failed", "Camellia", '''"Can I? How generous of you to find me a place."
{n}Camellia lifts Vellexia's cup from the stand and sets it down hard enough to spill.{/n}
"Put your ornaments there. I am leaving."
"Oh, do," {n}Vellexia says. Her amusement has gone cold.{/n}''', "retry.seen", "retry.failed", "display.answer_cut_off"),
        result("declined", "Camellia", '''"A sensible arrangement. I have my own diversions."
{n}She turns away. Vellexia beckons one of the courtiers closer without looking after her.{/n}''', "retry.seen", "retry.declined"),
    ]


def optional_nodes():
    """Reserved sequence, structurally complete but unavailable in this build."""
    company = [
        n("start", "Narrator", '''{n}The march has thinned the Fool King's court. In the upper room, Camellia examines the half-dismantled display while Vellexia sends the last yawning guest downstairs.{/n}
"You have left me with the only critic who was not begging to be invited," {n}Vellexia says.{/n}
"And you have left me something worth criticizing," {n}Camellia replies.{/n}''',
          c('"The salon is closing. I\'ll leave you the workbench."', "company"),
          c('"Keep this an ordinary salon evening."', "declined"), c("Later.", abort=True)),
        result("company", "Camellia", '''"I envy you. There — enjoy hearing it. You need not dress your appetite in a pious little story."
{n}Vellexia reaches for the cloth meant to unveil her display, then pulls it off and drops it over a chair.{/n}
"I had a spectacle prepared. It would bore you. Sit down. Tell me which of my guests you most wanted to silence. Permanently."
{n}Camellia taps her nail against the chair arm.{/n} "The one who laughed before I spoke."
{n}Vellexia smiles.{/n} "Then he can find other company. I want a friend with better conversation. You will do nicely."
{n}Camellia takes the chair beside her.{/n} "A friend, then. How fortunate that we have such similar tastes. I shall come for you — your guests have very little to recommend them."''',
               "company.seen", "company.both_friends", "camellia.criticism_entrusted", "vellexia.private_answer_kept",
               "cost.camellia.private_envy_owned", "cost.vellexia.spectacle_abandoned"),
        result("declined", "Camellia", '''"Then call your guests back. I have no wish to speak over them."
{n}She leaves for the crowded stairs. Vellexia lets the display cloth fall back into place.{/n}''', "company.seen", "company.declined"),
    ]
    desire = [
        n("start", "Vellexia", '''{n}The last soldiers are leaving the salon for muster. Vellexia stands on the bare display platform, looking down at Camellia.{/n}
"One last exhibit. Come up here. I have been looking forward to you all evening."
{n}Camellia rests her hand on the platform's edge, beside Vellexia's foot.{/n} "Still asking me to pose?"''',
          c('"I\'ll take the last of the audience downstairs."', "invitation"),
          c('"Let the salon end here."', "declined"), c("Later.", abort=True), portrait="Vellexia"),
        result("invitation", "Camellia", '''"Come down. I have looked at you long enough."
{n}She offers her hand. Vellexia takes it and steps off the platform, close enough to brush Camellia's skirt.{/n}
"I wanted you up there. I find I want you down here rather more."
{n}Camellia does not release her hand.{/n} "Then stop looking for an audience."''',
               "desire.seen", "desire.both_interested", "camellia.counterinvited", "vellexia.display_left"),
        result("declined", "Vellexia", '''"How tiresome. Put the cloth back, then."
{n}Camellia takes her hand off the platform. They descend the stairs separately.{/n}''', "desire.seen", "desire.declined"),
    ]
    choice = [
        n("start", "Narrator", '''{n}The courtiers have gone. Camellia holds the door of the upper room; Vellexia has already turned the display's painted face toward the wall. A muster horn sounds below.{/n}
"They can march without an audience too," {n}Vellexia says. Camellia watches her rather than the window.{/n}''',
          c('"I\'ll clear the room."', "camellia_answer"),
          c('"Camellia, the march preparations are still waiting."', "camellia_no"),
          c('"Vellexia, your audience is still downstairs."', "vellexia_no"),
          c('"Finish the evening as friends."', "friends_only"), c("Later.", abort=True)),
        n("camellia_answer", "Camellia", '''{n}You leave and draw the door shut behind you. Camellia turns the key, then catches Vellexia by the open edge of her gown.{/n}
"No applause. No pretty little mortal on your stand. I want you here, with me."
{n}Her other hand settles against Vellexia's neck. She draws her closer.{/n}''', c(next="vellexia_answer"), portrait="Camellia"),
        n("vellexia_answer", "Vellexia", '''"You are very demanding for someone who pretends so beautifully."
{n}Vellexia catches Camellia's waist and pulls her hard against her.{/n}
"Yes, darling. Here. With you."
{n}Camellia answers with a kiss. Vellexia's fingers work at the fastening of her dress; Camellia pushes the demon's gown from one shoulder without breaking away.{/n}''', c(next="mutual"), portrait="Vellexia"),
        n("mutual", "Narrator", '''{n}Vellexia backs into the platform. It scrapes across the floor; Camellia laughs against her mouth and pulls her away from it. Cloth slips onto the painted wood.{/n}''', c(next="explicit.1")),
        n("explicit.1", "Narrator", "{n}They leave the dismantled display for someone else to clear.{/n}", c(next="after")),
        result("after", "Narrator", '''{n}The room stays locked. Below, the court's noise dwindles; beyond the walls, the watch calls the hour.{/n}''',
               "choice.seen", "choice.both_yes", "choice.room_cleared"),
        result("camellia_no", "Camellia", '''"Indeed. The officers are expecting me at muster. I would rather get it over with than listen to them complain all tomorrow."
{n}She takes her cloak. Vellexia watches her go, one hand still resting on the platform.{/n}''', "choice.seen", "choice.camellia_no"),
        result("vellexia_no", "Vellexia", '''"So it is. I should hate to leave them thinking they had bored me into bed."
{n}She gathers her skirts and opens the door. Camellia's hand falls from the key.{/n}''', "choice.seen", "choice.vellexia_no"),
        result("friends_only", "Camellia", '''"Bring the chairs back, then. I have not finished describing that ridiculous dress downstairs."
{n}Vellexia laughs and pulls a chair alongside hers.{/n}''', "choice.seen", "choice.friends_only"),
    ]
    morning = [
        n("start", "Narrator", '''{n}The muster drums reach the upper room. One leg of the display has snapped. Camellia fastens her collar beside the wreckage while Vellexia nudges the broken wood with her bare foot.{/n}
"You put it in the way," {n}Camellia says.{/n}
"You shoved me into it. I ought to keep the pieces. My next guests can guess what happened."
{n}Camellia's hand stills at her collar.{/n} "Do that, and I shall tell them what you paid for that ugly thing."
{n}Vellexia laughs.{/n} "Come back and do it yourself. I shall seat you beside me."''',
          c('"Leave them their argument. The march is coming."', "end"), c("Later.", abort=True)),
        result("end", "Narrator", '''{n}Camellia takes her weapons from the chair. Vellexia pulls the cloth over the damaged stand, leaving two chairs together beside it. The drums continue outside.{/n}''',
               "morning.seen", "morning.blame_contested"),
    ]
    return dict(company=company, desire=desire, choice=choice, morning=morning)


def register(payload, scenes, refs):
    """Call before household.integrate; also supports a completed payload for tests.

    refs is the integration signature's native binding inventory. This row adds
    no native binding. The passed scenes list is the destination for all rows.
    """
    if any(s["Id"] == P + "settle" for s in scenes):
        return
    # This curated pair is absent from the old friction inventory. Declare
    # policy-owned readers for Rules.Validate without producing policy state.
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [["camellia.harem.eligible", "vellexia.harem.eligible", *BODY]]
    for stage, deeds in (("rival", ("ready",)), ("respect", RESPECT), ("friend", FRIEND), ("lover", LOVER)):
        for woman in PAIR:
            derived[P + woman + "." + stage] = [list(flags(*deeds))]
    for step, nodes, needs, excluded, delay in (
        ("settle", primary_nodes(), (), ("settle.seen",), 0),
        ("retry", retry_nodes(), ("settle.failed",), ("retry.seen", "settle.kept", "settle.declined"), 48),
    ):
        body = household.table_entry(P + step, "An ornament with teeth", '[Camellia and Vellexia: the display]', nodes,
            PAIR, P + "ready", requires=BODY + flags(*needs), forbids=EXCLUSIONS + flags(*excluded),
            delay=delay, chapters=(5,), RestAllowance="household.protected", HouseholdCategory="protected",
            HouseholdWitness=P + step + ".seen", ParticipantWomen=[])
        # Do not leave process-global entries for a second make_expansion call.
        household.ENTRIES.pop()
        body["MaxChapter"] = 5
        scenes.append(body)
    needs = {
        "company": ("display.answer_kept",),
        "desire": ("company.both_friends", "company.seen"),
        "choice": ("desire.both_interested", "camellia.friend", "vellexia.friend", "company.both_friends"),
        "morning": ("choice.both_yes",),
    }
    for step, nodes in optional_nodes().items():
        # Deliberate retirement gate, not a fabricated stay producer. See lore
        # check S25: current one-visit presence cannot warrant a 152-hour arc.
        # Retain every reserved node/destination for later coordinator activation.
        forbids = EXCLUSIONS + flags(step + ".seen", "ready") + tuple(household.enmity(a, b) for a, b in (PAIR, PAIR[::-1]))
        body = scene(P + step, "Off the display", "Camellia", 5, '[Camellia and Vellexia: the empty salon]', nodes,
            requires=ENVELOPE + flags("ready", *needs[step]), forbids=forbids, delay=8 if step == "morning" else 48,
            last=5, Relationship="household", Chapters=[5], Areas=[DREZEN], Remote=True, ManualOnly=True, Kind="event",
            Participants=list(PAIR), ParticipantWomen=[], Pair=list(PAIR), RestAllowance="household.pair",
            HouseholdCategory="pair", HouseholdArc=P.rstrip("."), HouseholdArcStart=step == "company",
            HouseholdWitness=P + step + ".seen",
            ForbidOverrides={household.enmity(a, b): a + ".harem.reconciled." + b for a, b in (PAIR, PAIR[::-1])})
        if step == "company":
            body["RequiresAnyGroups"] = [list(flags("settle.kept", "retry.kept"))]
        scenes.append(body)
        household.CONSUMERS[body["Id"]] = household.PAGE_TAKEN
    payload.setdefault("ForesightConsumers", {}).update({P + step: household.PAGE_TAKEN
        for step in ("settle", "retry", "company", "desire", "choice", "morning")})
    # W5 owns attachment: the shared HouseholdTests currently require exactly
    # the five seeded Seating Notes. Keep the row's reader ready for that pass
    # rather than altering the shared census or inventing a new book section.


def ledger_entry():
    """Historical notes, never a bodily reply from an absent woman."""
    lines = []
    for text, requires, forbids in (
        ("Neither accepts blame for the damaged display.", ("morning.blame_contested",), ()),
        ("They chose each other's company. Neither calls herself the exhibit.", ("camellia.lover", "vellexia.lover"), ()),
        ("Vellexia stepped down; their invitation remains unfinished.", ("desire.both_interested",), ("choice.seen",)),
        ("The empty salon became their own conversation.", ("camellia.friend", "vellexia.friend"), ("desire.seen", "choice.seen")),
        ("Their private answer stopped there.", ("company.declined",), ()),
        ("Their private answer stopped there.", ("desire.declined",), ()),
        ("Their private answer stopped there.", ("choice.friends_only",), ()),
        ("Their private answer stopped there.", ("choice.camellia_no",), ()),
        ("Their private answer stopped there.", ("choice.vellexia_no",), ()),
        ("Camellia owned her appraisal. Vellexia answered it.", ("camellia.respect", "vellexia.respect"), ("company.seen",)),
        ("The display quarrel is still unanswered.", ("settle.failed",), ("retry.kept",)),
        ("They kept their separate evenings.", ("settle.declined",), ()),
        ("The appraisal has not been answered.", (), ("settle.seen",)),
    ):
        lines.append(dict(Text="{n}" + text + "{/n}", Requires=list(flags(*requires)), Forbids=list(flags(*forbids))))
    return dict(Id=P + "record", Section="Seating Notes", Title="Camellia and Vellexia", Portrait="Camellia",
                Text="{n}The display quarrel.{/n}", Requires=["foresight.page_taken", "household.table.kept"],
                Forbids=[], Lines=copy.deepcopy(lines))
