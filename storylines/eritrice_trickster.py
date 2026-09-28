"""Eritrice on the Trickster path: "Motion carried" (Writer/handoffs/trickster/eritrice.md; family F10).

Canon: the empyreal lord who convened the Council of the Trickster path. "My element is truth. The eternal truth,
shining through the endless lies. The insights born only through honest, thoughtful debate." (Council_Eritrice/Cue_0010
ea54bde3). She keeps the minutes on a long scroll (Council_2/Cue_0030 6cc3a4f0), votes on everything ("Passed
unanimously.", Council_3/Cue_0040 55eecf75) and has already conceded one usurped adjournment to the Commander
(Council_3/Cue_0045 cf4e1e43). In 5-2 she turns on her own Council: "if you don't offer it up willingly, I'll take it by
force!" (Council_5-2/Cue_0035 b138a1a4). If the Commander fights the Council, its members are left unconscious and
bled of their essence (Shyka_Offer/Cue_0002 c3b8e7f1), then pretend they never met (Epilogues/Cue_0568 0ffd4b0b):
hostility and a sealed hall, not death.

F10 root: the minutes are true by her own law, so a motion she wrote down as carried was carried. Nothing moves her pen
but her own honesty. Her private dialog sits on the hall spawner and her unit has no dialog component, so every physical
scene is a hall scene on Council_Eritrice/AnswersList_0002; once the hall is sealed she can only write. The courtship
that the spine opens is eritrice_minutes (the standing debate).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
P = "eritrice.trickster."
UNIT = "4a47d14a45ce264408a1c6a33345dd89"          # Eritrice (hostile variant EritriceEnemy 8e161cb3)
HALL = "28a49e115795ed44397b5a1503cef4f0"          # Area TricksterCouncil
LIST = "d07bffc320b9127459c40869ab3e8ee4"          # Council_Eritrice/AnswersList_0002
WELCOME = "2abad22288daf834f950acb6b2b7a812"       # Council_Eritrice/Cue_0001 "Welcome to the Council, Commander." (clean)
CHADALI_LIST = "e649f211c6b002a49a0c633061877927"  # Council_Chadali/AnswersList_0003
NENIO_HUB = "1ab909cc3a6194840b1475b99547c263"     # CompanionDialogues/Nenio/AnswersList_0015
COUNCIL_PAGE = "b2fd1f720322d6749b921cdd34328c3a"  # Epilogues BookPage_0187 (the Council's page, Cue_0568)

STARTED = "eritrice.started"
CLOSED = "eritrice.closed"
COMMITTED = "eritrice.committed"
LOST = "eritrice.lost_at_council"
LATCHED = LOST + ".latched"
PRIMED = P + "primed"
RETURNED = P + "returned"
DECLINED = P + "declined"
MINUTES_READ = P + "minutes_read"
STRAIGHT = P + "argued_straight"
CENSURED = P + "cost.censured"
CAUGHT = P + "cost.caught_lying"
ON_RECORD = P + "cost.on_the_record"
LATE = P + "cost.late"
GRUDGE = P + "cost.grudge"
ESSENCE = P + "cost.essence_taken"
APOLOGISED = P + "cost.apologised"
ON_AGENDA = P + "cost.grudge_on_agenda"
LATE_COMMITTED = P + "late_committed"
# The standing debate's last pre-commit point (eritrice_minutes): the second reading is heard only after it.
DEBATED = "eritrice.minutes.quill"

RELATIONSHIP = dict(
    Title="Motion carried",
    Description=("Eritrice keeps the minutes of the Council, and she does not write lies. She wrote down my motion from "
                 "the floor as carried, so, by her own law, it was. The chair now owes me a private debate."),
    Objective="Debate Eritrice, point by point",
    Guidance=("On the Trickster path, move a motion from the floor in a private audience with Eritrice in the Council "
              "hall, then return after a Council session has been minuted. The debate continues in the hall in "
              "Chapters 3 and 5. If the hall is sealed, the chair writes."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[LOST], FailureFlags=[],
    UnavailableOverrides={LOST: RETURNED},
    TricksterAccess={LOST: dict(detect=[LOST], device=P + "fought.tabled", returned=RETURNED)},
)

DERIVED = {LATE_COMMITTED: [["trickster.ever", STARTED], ["trickster.ever", RETURNED]]}


def e(id, text, *choices, **kw):
    return n(id, "Eritrice", text, *choices, portrait="Eritrice", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Eritrice", **kw)


def hall(id, title, entry, nodes, requires, forbids=(), delay=0, chapters=(3, 5), optional=False, **extra):
    """A physical scene on her own private list in the Council hall (while the hall is open)."""
    SCENES.append(scene(id, title, "Eritrice", min(chapters), entry, nodes, requires=requires,
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=optional,
                        Relationship="eritrice", Chapters=list(chapters), AnswerLists=[LIST], **extra))


def letter(id, title, nodes, requires, forbids=(), delay=0, **extra):
    """A remote scene: the hall no longer opens, so the chair writes (Chapter 5 only)."""
    SCENES.append(scene(id, title, "Eritrice", 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="eritrice", Remote=True, **extra))


# --- 5.1 council_active: the motion (primer), inline on her private list. -----------------------------------------

SCENES.append(scene(P + "council.motion", "Motion carried", "Eritrice", 3, '"Madam Chair. A motion."', [
    e("start", '''"There is no quorum. There is no floor. This is a private audience, Commander, and a motion requires a session, a second, a..."
{n}But she has already dipped the quill. It is the oldest habit she has: every question put in her hearing is written down, so that no one can say afterwards it was never asked. The long scroll is open at the foot of the last session, and her claws are waiting over it.{/n}''',
      c('[Move a motion from the floor] "I move that the chair is in dire need of a private debate. All in favour?"', "carried",
        flags=(PRIMED, CENSURED), mythic="Trickster", alignment=("Chaotic", 1)),
      c("Never mind.", abort=True)),
    e("carried", '''{n}She writes the motion down, word for word, because it was put. She writes "In favour: the mover." Then she writes "Opposed:", and the quill stops, and stays stopped.{/n}
{n}You watch her try. Her claws tighten on the quill. She cannot write her own name after that word, because it would not be true, and she has never once written a thing that was not true. The silence goes on long enough to be an answer.{/n}
{n}She writes "Carried." Then, lower, in a smaller and much harder hand: "The chair censures the mover for moving it."{/n}''',
      c("Continue", "law")),
    e("law", '''"You asked me a question I could only answer honestly. That is a very low trick, Commander, and a very good one."
{n}A growl, deep in her chest, the sound of a lion that has been cornered by a rule it wrote itself.{/n}
"Standing Order One of this Council. I drafted it, and every member signed it on the first day, Socothbenoth in rouge: the minutes are not amended. Alichino asked for an exception that same afternoon. I refused him. If I strike this line, I must write beside it why, that I opposed the motion, which is a lie; and I must grant Alichino his exception, which is worse."''',
      c("Continue", "terms")),
    e("terms", '''{n}She sands the ink with a hard flick of the wrist.{/n}
"So it stands, and here is exactly what it buys you. It binds the chair to hear you out, in private, point by point. It does not bind the Council. It does not bind my vote. And the censure goes into the Council's own minutes, which every member reads: you are now the only member of this Council ever to be censured. Alichino will have it copied into his little black book before the ink is dry."
"Come back when the Council has sat again. I will read the censure into the record first."''',
      c("[Let her sand the ink dry.]")),
], requires=("trickster",), forbids=(PRIMED, LOST), last=5, Relationship="eritrice", Chapters=[3, 5],
    AnswerLists=[LIST], NativeReturnCue=WELCOME))


# --- The payoff: the private debate, once a Council session has been minuted. ------------------------------------

SCENES.append(scene(P + "council.private_debate", "The minutes stand", "Eritrice", 3, '"About my motion, Madam Chair."', [
    nar("start", '''{n}She unrolls the scroll of the last session and turns it so you can read it. Among the Council's business, in her own upright hand: "Motion from the floor, the Commander: that the chair is in dire need of a private debate. Carried unanimously."{/n}''',
        c("Continue", "record")),
    e("record", '''"I do not write lies. My element is truth, the truth that only honest debate can reach, and it seems the truth is that I agreed."
{n}Her claws tap the scroll, once for each word.{/n} "The censure stands too. It is read into the record first: the mover is rebuked for moving a motion in a room with no floor."
"Now: the debate. Point by point, until one of us concedes. I have never lost an argument, Commander. I have been at this table longer than your crusade has had a name."''',
      c("Continue.", "honest"),
      c('[Win the vote with a trick] "I move the question be called. The ayes have it: I heard them."', "trick")),
    e("honest", '''{n}A low growl, not entirely displeased.{/n} "Objection noted. ...Sustained. ...Overruled."
{n}She sets down the quill.{/n} "Proceed. The chair is listening. And the chair will remember that you argued it straight."''',
      c('[Argue it honestly] "Point one: you like losing to me. Prove it isn\'t true."', flags=(STARTED, MINUTES_READ, STRAIGHT))),
    e("trick", '''{n}Her claws come out and go into the table, all five, and the wood creaks. For a moment she is not the chair of anything. She is a lion someone has lied to.{/n}
"I heard no ayes. I heard one Commander, speaking in several voices, at my table, in the one room in the multiverse where nobody has ever dared." {n}She draws the claws back, slowly, and writes it down, and her hand is not steady.{/n} "Minuted: 'the Commander attempted to carry a vote by acclamation of the Commander.'"
"I will debate you anyway. I do not abandon a debate because one side cheats. But I will remember, every time you speak, that you are capable of it."''',
      c('[Let her win the round] "Then the debate goes on."', flags=(STARTED, MINUTES_READ, CAUGHT))),
], requires=("trickster.ever", PRIMED, "council.session_minuted"), forbids=(STARTED, LOST), delay=24, last=5,
    Relationship="eritrice", Chapters=[3, 5], AnswerLists=[LIST], NativeReturnCue=WELCOME))


# --- The commit: the second reading, a vote she is free to lose. ---------------------------------------------------

READING = (
    c('[Make the case honestly] "Here is the case for."', "case"),
    c('[Carry it by a trick] "I move the motion carries, the chair concurring."', "refused"),
)

hall(P + "council.second_reading", "The second reading", '"You called for a second reading?"', [
    nar("open", '''{n}The hall is empty but for the two of you. The long table has been cleared, the other chairs pushed in. In front of her lies a fresh scroll, and the heading is already written: "Motion: that the chair and the Commander be..." The rest of the line is blank.{/n}''',
        c("Continue", "start_lied", requires=(CAUGHT,)),
        c("Continue", "start", forbids=(CAUGHT,))),
    e("start", '''"The chair calls a second reading."
{n}She does not look up from the blank line.{/n} "The chair will hear the case for. Then the chair will vote. The chair votes last, and the chair is not bound to agree with the floor. Proceed."''', *READING),
    e("start_lied", '''"The chair calls a second reading. The minutes of the first also record that you lied to carry it."
{n}She reads the line aloud, flatly, the way she reads Alichino's apologies for absence.{/n} "'The Commander attempted to carry a vote by acclamation of the Commander.' The case for will have to overcome that. Proceed."''', *READING),
    e("case", '''{n}She listens without writing, which you have never seen her do. When you finish, she is quiet for a long moment. Her claws rest on the blank line and do not tap.{/n}
"The truth shines through the endless lies. I said that to you the day we met. I did not expect to be the one it shone on."''',
      c('[Call the question] "Then call the question."', "carried", flags=(COMMITTED,)),
      c('[Ask her to vote for you] "You decide. For both of us."', "refused")),
    e("carried", '''"All those in favour."
{n}She raises her own hand. The hall is silent. She writes the rest of the heading, and it takes her a long time, because her hand is not steady: "...the chair and the Commander be, henceforth, one another's."{/n}
"Carried." {n}Her voice has dropped to something close to a purr.{/n} "I voted aye before you had finished speaking. I have never once in my existence voted before the floor had finished. I do not care."''',
      c("[Stay while she sands the line.]")),
    e("refused", '''"The chair does not vote on behalf of the floor, and the chair does not carry motions by trickery. Not this one."
{n}She rolls the scroll closed, gently.{/n} "The chair declines to put the question. It may be moved again, once, when the mover is ready to stand behind it."''',
      c('[Accept the ruling] "So be it."', flags=(DECLINED,))),
], requires=("trickster.ever", STARTED, DEBATED), forbids=(COMMITTED, DECLINED), delay=48)


# --- The one priced second ask after her soft no. -----------------------------------------------------------------

hall(P + "council.third_reading", "The third reading", '"The motion, Madam Chair. Once more."', [
    e("start", '''"Third reading."
{n}She does not open a new scroll. She opens the crusade's own gazette, the one read out in Drezen's square, and lays it flat on the Council's table.{/n}
"The chair will put the question on one condition. You answer one question on the record, where your soldiers will read it: what did you fear this Council would find? Answer it truthfully and the chair votes. Refuse, and the motion is withdrawn for good."''',
      c('[Answer on the record] "That it would find me out. It has."', "aye", crusade=("Favors", -100),
        flags=(COMMITTED, ON_RECORD)),
      c('[Withdraw the motion] "No."', "withdrawn", flags=(CLOSED,))),
    e("aye", '''{n}She writes your answer into the gazette word for word, and signs it, and blots it. Tomorrow half of Drezen will be reading it over its porridge.{/n}
"There. That was the truth, and you paid for it where it costs." {n}She lifts her own hand.{/n} "The chair votes aye. Carried."''',
      c("[Take her hand.]")),
    e("withdrawn", '''"Then the motion is withdrawn. For good." {n}She rules a line across the heading, one clean stroke.{/n}
"The chair does not debate a question the floor will not answer."''',
      c("[Go.]")),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED,), delay=72)


# --- 5.2 Hall lost before the payoff (primed): the minutes by courier. -------------------------------------------

CHADALI_PS = nar("postscript", '''{n}In the margin someone has drawn a small heart, and beside it, in a round, happy hand:{/n} "She let me! She said it wasn't minuted, so it doesn't count. It counts. C."''',
                 c("[Fold the letter away.]"))

letter(P + "council.minutes_letter", "The minutes by courier", [
    nar("start", '''{n}A scroll case arrives by courier, sealed with a lion's head in amethyst wax. Inside is a fair copy of the minutes of the Council's last session, and one item is underlined in red: "Motion from the floor, the Commander: that the chair is in dire need of a private debate. Carried unanimously."{/n}''',
        c("Read the letter.", "letter")),
    e("letter", '''{n}Beneath it, in the same upright hand:{/n} "The hall is sealed, and the Council no longer convenes. The minutes stand. A motion carried under my pen cannot be struck, and so the chair is obliged to hold the debate by correspondence. The chair notes the delay. Your opening argument, Commander. Keep it short. Keep it true."''',
      c('[Countersign the minutes] "Carried. Signed. Point one: you kept the minutes."', "postscript",
        flags=(STARTED, MINUTES_READ, LATE), forbids=("chadali.lost_at_council",)),
      c('[Countersign the minutes] "Carried. Signed. Point one: you kept the minutes."',
        flags=(STARTED, MINUTES_READ, LATE), requires=("chadali.lost_at_council",))),
    CHADALI_PS,
], requires=("trickster.ever", PRIMED), forbids=(STARTED, LOST), delay=24,
    RequiresAnyGroups=[["council.debrief_motion", "trickster.failed"]])


# --- 5.3 Allied, hall lost, no primer: a motion filed with surety (late fallback). -------------------------------

letter(P + "council.late_motion", "A motion filed with surety", [
    nar("start", '''{n}The Council's last circular reaches Drezen: its hall is sealed, and "any business still pending before this body may be filed with the chair in writing, with surety, for the record". You have no motion pending. You write one now, and the Office of Finances writes the surety: a crusade bond, forfeit if the motion is frivolous.{/n}''',
        c('[File the motion and post the bond] "I move that the chair is in dire need of a private debate. Surety enclosed."', "reply",
          crusade=("Favors", -100)),
        c("Let the Council lie.", abort=True)),
    e("reply", '''{n}The reply comes back within the week, in an upright hand.{/n} "A motion filed after adjournment, with money behind it. Irregular. Also, the chair notes, sincere: nobody posts a bond for a joke. The motion is admitted. The debate will be held by correspondence. The chair notes the delay, and the price."''',
      c('[Begin the debate by post] "Received. My opening argument follows."', "postscript",
        flags=(PRIMED, STARTED, MINUTES_READ, LATE), forbids=("chadali.lost_at_council",)),
      c('[Begin the debate by post] "Received. My opening argument follows."',
        flags=(PRIMED, STARTED, MINUTES_READ, LATE), requires=("chadali.lost_at_council",))),
    CHADALI_PS,
], requires=("trickster", "council.debrief_motion"), forbids=(PRIMED, STARTED, LOST))


# --- 5.4 council_fought: the grudge is tabled, on her terms (the ER-2 device). ------------------------------------

letter(P + "fought.tabled", "Point of order", [
    nar("start", '''{n}The letter is three lines long, sealed in amethyst wax pressed so hard the lion's head has cracked.{/n}''',
        c("Continue", "lover", requires=(COMMITTED,)),
        c("Continue", "stranger", forbids=(COMMITTED,))),
    e("stranger", '''"You struck the chair of this Council unconscious and let its members be bled of their essence. The chair has not forgotten that it was the chair who threatened it first. The chair is not interested in your apology unless it is on the record. State your business."''',
      c('[Raise a point of order] "Point of order: \'contribute your essence or I\'ll take it by force\' was the chair\'s own motion. I seconded it. I move we table the grudge."',
        "ruling", mythic="Trickster", alignment=("Chaotic", 1))),
    e("lover", '''"You struck the chair of this Council unconscious. You, who had her vote. The chair woke on the floor of her own hall with her essence gone and your name in her mouth, and she has not decided which was worse."
"The chair has not forgotten that it was the chair who threatened you first. The chair is not interested in your apology unless it is on the record. State your business."''',
      c('[Raise a point of order] "Point of order: \'contribute your essence or I\'ll take it by force\' was the chair\'s own motion. I seconded it. I move we table the grudge."',
        "ruling", mythic="Trickster", alignment=("Chaotic", 1))),
    e("ruling", '''{n}The answer is longer, and written with a steadier hand.{/n} "Point of order noted. It is, regrettably, correct: 'contribute your essence or I'll take it by force' was the chair's own motion. The chair rules that the grudge may be tabled. Tabled, Commander, not withdrawn."
"The chair imposes terms. Either you make a formal apology, entered in the minutes and read aloud at a special session the chair will convene for that one purpose, or the grudge stands on every agenda for as long as there is an agenda, and the chair reads it aloud whenever you are present. Choose."''',
      c('[Make the formal apology before the reconvened Council] "Convene your session. I\'ll say it."', crusade=("Favors", -200),
        flags=(RETURNED, GRUDGE, ESSENCE, APOLOGISED)),
      c('[Let the grudge stand on every agenda] "Read it every time. I\'ll be there to hear it."',
        flags=(RETURNED, GRUDGE, ESSENCE, ON_AGENDA)),
      c('[Move to strike the grudge] "Then I move the grudge be struck from the record."', "struck")),
    e("struck", '''"The chair declines. Truth is not struck from the record, not even to spare the chair."
{n}The seal on this one is pressed so hard it has split in two.{/n} "This correspondence is closed."''',
      c('[Close the correspondence] "Accepted."', flags=(CLOSED,))),
], requires=("trickster", LATCHED), forbids=(RETURNED,), delay=24, TricksterDevice=True, TricksterState=LOST)


# --- 5.5 Epilogue pages (Owner EritriceEpilogue; after the Council's own page; no effects). -----------------------

EP = dict(last=6, Relationship="eritrice", EpilogueAfter=COUNCIL_PAGE)

SCENES.append(scene(P + "epilogue.commit", "", "EritriceEpilogue", 6, "", [
    nar("page", '''{n}The debate the war had interrupted resumed after Threshold, by correspondence, and ran to forty letters in an upright hand, point by point, conceding nothing. The forty-first was a single line: "The chair has heard the case for, and the case against. The chair will vote when the floor answers one question, in its own hand: aye, or nay."{/n}''',
        c('[Write back one word: "Aye."]', "aye"),
        c('[Write back: "Nay. But keep writing."]', "nay"),
        c("[Leave the forty-first letter unanswered.]", "silence"),
        paragraphs=(
            p("{n}The first of the forty letters began, as the chair's letters always did, by noting the delay.{/n}", requires=(LATE,)),
            p("{n}Every letter opened with the grudge, read into the record in full.{/n}", requires=(ON_AGENDA,)),
            p("{n}The apology the Commander had made before the reconvened Council was bound into the front of her scroll, where she could find it quickly.{/n}", requires=(APOLOGISED,)),
        )),
    nar("aye", '''{n}The reply came back within the week: "The chair votes aye. Minuted." Eritrice arrived in person three days later, with the scroll, to make sure the minutes were accurate, and did not leave for a long time.{/n}'''),
    nar("nay", '''{n}The chair minuted the motion as lost, by one vote, and did not move it again. She did keep writing. The correspondence ran on for the rest of the Commander's life, point by point, the only debate either of them ever looked forward to; and it never once touched the question that had been answered.{/n}'''),
    nar("silence", '''{n}The forty-first letter was never answered. In the minutes Eritrice kept for the rest of her long life it stands as the only unanswered item, carried from agenda to agenda, marked neither aye nor nay: "Awaiting the floor."{/n}'''),
],
    requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED, "council.fought", "council.fought_nocta_allied", "sacrifice"),
    RequiresAnyGroups=[[STARTED, RETURNED]], ForbidOverrides={"council.fought": RETURNED, "council.fought_nocta_allied": RETURNED, "sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.declined", "", "EritriceEpilogue", 6, "", [
    nar("page", '''{n}The motion was never moved a third time. In the minutes Eritrice kept for the rest of her long life there is a standing item, carried over from session to session and never called: "Motion: that the chair and the Commander be..." The rest of the line is blank.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, "council.fought", "council.fought_nocta_allied"), ForbidOverrides={"council.fought": RETURNED, "council.fought_nocta_allied": RETURNED}, **EP))

SCENES.append(scene(P + "epilogue.we_did_meet", "", "EritriceEpilogue", 6, "", [
    nar("page", '''{n}The Council's members pretended ever after that they had never met. Its chair kept minutes anyway. The later volumes are much concerned with a standing debate between the chair and a certain Commander, conducted point by point, and every entry ends the same way: "Carried."{/n}''',
        c('[Move that the record be corrected] "I move that the Council did, in fact, meet. Twice nightly. All in favour?"'),
        paragraphs=(
            p("{n}She never admitted in public that the Council had met, which was the only lie anyone ever caught her telling. The minutes, which were not public, admitted everything.{/n}", requires=("council.epilogue_ceased",)),
            p("{n}At the Council's victory feast the members could not shake the feeling they had forgotten to invite someone. The chair had not forgotten. The chair had simply declined to share.{/n}", requires=("council.epilogue_feast",)),
            p("{n}The Council went on convening, and went on arguing about the Worldwound. Its chair adjourned every session on time, which the members found suspicious, and went home early, which they found more suspicious still.{/n}", requires=("council.epilogue_convened",)),
            p("{n}The grudge stayed on the agenda. She read it aloud at every session the Commander attended, and then, in the minutes, noted the Commander's reply. The replies grew shorter over the years, and warmer, and in the last volumes they are only one word long.{/n}", requires=(ON_AGENDA,)),
            p("{n}The gazette with the Commander's answer on the record hung framed in the chair's study, in Nirvana, beside a scroll she refused to lend to anyone.{/n}", requires=(ON_RECORD,)),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, DECLINED, "council.fought", "council.fought_nocta_allied", "sacrifice"),
    ForbidOverrides={DECLINED: COMMITTED, "council.fought": RETURNED, "council.fought_nocta_allied": RETURNED, "sacrifice": "trickster.cheated_death"}, **EP))


# --- Reactions (exactly two reactors: Chadali and Nenio, each behind its reactor's availability guard). -----------

NENIO_GUARD = ("nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out", "nenio.dissolved")

SCENES.append(reaction("Chadali", P + "react.chadali_motion", (PRIMED,),
    '''"Can I second it? I want to second it! Is it too late?" {n}Chadali cranes over the table to read the scroll, and her whole face lights up.{/n}
"Oh, she's written 'seconded, retroactively'. She never lets me do anything retroactively. I asked to retroactively win the last three votes and she fined me a sonnet!"''',
    answer_list=CHADALI_LIST, forbids=("chadali.lost_at_council", LOST), chapter=3, last=5, Chapters=[3, 5],
    entry='"Eritrice passed my motion."', portrait="Chadali"))

SCENES.append(reaction("Nenio", P + "react.nenio_motion", (STARTED,),
    '''"I have measured the chair. Sessions chaired: all of them. Votes carried: all of them. Votes contested before you: none. Conclusion: she is not a chairwoman, she is a weather system, and you have changed the weather."
{n}Nenio holds out a ruler.{/n} "I require one whisker. For scale."''',
    answer_list=NENIO_HUB, forbids=NENIO_GUARD, chapter=3, last=5, Chapters=[3, 5],
    entry='"About Eritrice..."', portrait="Nenio"))

SCENES.append(reaction("Nenio", P + "react.nenio_tabled", (RETURNED,),
    '''"How much essence does a lion-headed empyreal lord yield? Does it regrow? At what rate?" {n}Nenio flips a page.{/n}
"Put me on her agenda. Item seven: measurements. Item eight: whether a grudge that is read aloud every session gets heavier or lighter. I have a hypothesis. It is 'heavier'."''',
    answer_list=NENIO_HUB, forbids=NENIO_GUARD, chapter=5, last=5, Chapters=[5],
    entry='"Eritrice tabled her grudge."', portrait="Nenio"))


def integrate(payload):
    """Register the new relationship's own derived keys. Scenes are added by expansion.py; world keys bind on demand."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
