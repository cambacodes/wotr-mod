"""S10: authored oath inquiry, friend/friend ceiling; no native event rewrite.

Native voice anchor only: NenioSeelah/Banter_NenioSeelah_banter2,
35a022dfb980b3e4cb98661b9d2a6a9c; enGB e0b58e0d-61c3-4066-9169-eeff982300c8
and f6509bb2-e2e4-40ab-85f8-75f1ecfcbfd8. Never presume that bark was played,
or that a recreated Nenio remembers it. Sheet D, S10; lore-check S10/shared.
"""
import copy

from story_format import c, n, scene

PREFIX = "household.pair.seelah_nenio."
QUESTION = PREFIX + "question"
ANSWERED = tuple(PREFIX + key for key in (
    "question.seen", "question.answered", "deed.nenio_revised_question",
    "deed.seelah_named_decision", "cost.nenio_dropped_word_list",
    "cost.seelah_watch_account"))
FRIENDS = ("seelah.harem.attitude.nenio.friend", "nenio.harem.attitude.seelah.friend")


def question():
    return scene(QUESTION, "The question after the curse", "Seelah", 3,
        "[Seelah and Nenio: a question about the watch]", [
            n("start", "Nenio", '''{n}Seelah sets a cracked watch lantern on the corner table. Nenio leans over her open notebook.{/n}
"Paladin girl! I heard you say 'shit' on the wall. Then you invoked Iomedae. Was the second utterance intended to cancel the first?"
{n}Seelah pulls off a gauntlet. A strip of bloodied cloth clings to its edge.{/n}
"No. The shit was for the cultist who shot our lantern. The prayer was for the fellow beside me. He couldn't see the ladder anymore."
"Excellent. Two recipients! Commander, I require her account," {n}Nenio says.{/n}
"And I'd like her to hear it before she starts asking the next watch for curses," {n}Seelah says.{/n}''',
                c('"Ask her what the oath meant on watch."', "account"),
                c('"Leave that question alone."', "declined"),
                c("[Later.]", abort=True)),
            n("account", "Seelah", '''"He'd taken a bolt through the hand. Wanted me to pull him down the ladder. There were still people coming up behind him, and a cultist drawing another bead on us."
{n}Seelah lays the lantern on its side, showing Nenio the hole through the shutter.{/n}
"I put him behind the parapet and stood where the light had been. Told him to keep shouting so the others could find the ladder. I'd have liked to get below just as much as he did."
"Did the prayer remove that preference?" {n}Nenio asks.{/n}
"No! I was scared. I stayed anyway. Put down what I did. You've got enough bloody words," {n}Seelah says.{/n}''',
                c("[Hear Nenio's revised question.]", "revised")),
            n("revised", "Nenio", '''{n}Nenio draws a line through her heading and turns to a clean page.{/n}
"Actions, then. Your oath does not predict your vocabulary. What would you have done if the wounded man could no longer shout?"
"Dragged him clear first. Then yelled myself," {n}Seelah says.{/n}
"That would have disclosed your position," {n}Nenio says.{/n}
"So did standing in front of a bloody ladder. He wasn't bait, Nenio," {n}Seelah says.{/n}
{n}Nenio writes that down. Seelah reaches for the lantern, but Nenio holds the broken shutter against the page to sketch the angle of the shot.{/n}
"Leave this here, paladin girl. I have further questions."
"All right. But I'm getting a drink before your next one," {n}Seelah says.{/n}''',
                c("[Leave them to the lantern and the next question.]", flags=ANSWERED)),
            n("declined", "Seelah", '''{n}Seelah wraps the broken lantern in the bloodied cloth.{/n}
"I'd rather she asked me than made up an answer. But I've got another watch coming."
"An incomplete observation," {n}Nenio mutters, keeping her pencil poised over the word list.{/n}
{n}Seelah puts her gauntlet back on. Neither woman has given the account Nenio requested.{/n}''',
                c("[Return to your duties.]", flags=(PREFIX + "question.seen", PREFIX + "question.declined"))),
        ], requires=("trickster", "foresight.page_taken", "household.table.kept",
                     "household.stance_eligible", PREFIX + "ready",
                     "seelah.harem.eligible", "nenio.harem.eligible", *FRIENDS),
        forbids=("fool_king.gone", "trickster.failed", PREFIX + "question.seen",
                 "seelah.harem.enmity.nenio", "nenio.harem.enmity.seelah"),
        optional=True, Relationship="household", Chapters=[3, 5],
        Areas=["2570015799edf594daf2f076f2f975d8"], InteractionHub="household.table",
        Participants=["seelah", "nenio"], ParticipantWomen=["seelah", "nenio"],
        Pair=["seelah", "nenio"], RestAllowance="household.pair",
        HouseholdCategory="dynamic", HouseholdWitness=PREFIX + "question.seen",
        ForbidOverrides={"seelah.harem.enmity.nenio": "seelah.harem.reconciled.nenio",
                         "nenio.harem.enmity.seelah": "nenio.harem.reconciled.seelah"})


def register(payload, scenes, refs):
    """Register once; consume integrator-owned friendship and current attendance.

    Qualified body-bearing SeatWomen records must be supplied by integration.
    Do not replace them with commitment, old return flags or present_now alone.
    Failing closed here prevents a partial integration from fabricating attendance.
    """
    if any(s["Id"] == QUESTION for s in scenes):
        return
    for woman in ("seelah", "nenio"):
        seat = payload.get("SeatWomen", {}).get(woman)
        if not seat or seat.get("Relationship") != woman or not seat.get("Requires"):
            raise ValueError("S10 needs the integrator's current bodily SeatWomen contract: " + woman)
    derived = payload.setdefault("Derived", {})
    derived[PREFIX + "ready"] = [["household.table.kept", "seelah.harem.eligible", "nenio.harem.eligible"]]
    derived[PREFIX + "alliance.kept"] = [list(ANSWERED[1:])]
    # These are inputs, never attitude/first-wins producers owned by this row.
    pending = payload.setdefault("PendingHooks", [])
    for key in (*FRIENDS, "seelah.harem.enmity.nenio", "nenio.harem.enmity.seelah",
                "seelah.harem.reconciled.nenio", "nenio.harem.reconciled.seelah"):
        if key not in pending:
            pending.append(key)
    scenes.append(copy.deepcopy(question()))
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        ledger["Entries"].append(dict(
            Id=PREFIX + "seating", Section="Seating Notes", Portrait="Seelah",
            Title="Seelah and Nenio", Text="{n}A question about the watch.{/n}",
            Requires=[PREFIX + "question.seen"], Forbids=[], AnyGroups=[],
            Tooltip="RRT_SeatingNotes", Lines=[
                dict(Text="{n}Nenio crossed out her list of curses. Seelah gave her the decision at the ladder instead. Their next question is still open.{/n}",
                     Requires=[PREFIX + "alliance.kept"], Forbids=[], AnyGroups=[]),
                dict(Text="{n}I left their question unanswered.{/n}",
                     Requires=[PREFIX + "question.declined"], Forbids=[], AnyGroups=[])]))
    # Apply the existing dynamic cap to the assembled rows; never raise its limit.
    from storylines import harem_caps
    harem_caps.apply(payload)
