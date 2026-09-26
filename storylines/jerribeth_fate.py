"""An authored Trickster correspondence experiment at Jerribeth's native Act 4 contact.

No actor is spawned, restored, moved, or made friendly by these scenes.
"""
from story_format import c, n, scene

ACTOR = "417ce3dcf3a9707488f2b9b2a790814b"
ANSWERS = "19786fae9c29f9d439e374bb857c2e84"
UPPER_CITY = "8217b05e37078414981d994151f0ffb1"
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"
DREZEN = "2570015799edf594daf2f076f2f975d8"

INTEGRATION_REQUIREMENTS = dict(
    Implemented=False,
    Scope="Living Act 4 native contact and authored later letter only; no death or despawn recovery.",
    NativeDialog="992c44e6775d87444b562e855fd64af1",
    NativeDialogConditions="3f75915712ea4810a3d800d92b4b1eb5",
    DefaultSpawner="5f976e09-1f17-4f78-907c-fb133d947090",
    ThirdDateSpawner="da348c4f-6c2a-452c-9c20-0d65fdba7168",
    Actor=ACTOR,
    RequiredVerification=[
        "Confirm native answer-list delivery after hearing the refuge cue, before departing the native dialogue.",
        "Verify one eligible actor when default and third-date scene mechanics overlap; never accept a hidden or duplicate live actor.",
        "Run focused Rules tests, bindings and managed construction before export.",
        "Review book presentation and saves; paper effects are authored scene events, not physical inventory objects.",
    ],
)

SCENES = [
    scene("jerribeth.fate_envelope", "An answer ahead of its question", "Jerribeth", 4,
          '[Trickster] "You wondered what whim of fate brought me here. Shall we give it a less convenient answer?"', [
        n("start", "Jerribeth", '''{n}Jerribeth's antennae rise. She glances toward the rest of Vellexia's house before returning her attention to you.{/n}
"A proposal like that usually ends with someone expecting me to applaud. What do you intend to make fate do?"
{n}You take a blank piece of paper, fold it once, and address it to yourself at your next quiet evening. There is no city beneath the name.{/n}
"You have forgotten where you live."
"I have declined to tell the letter."
{n}You fold the paper again. A second folded sheet presses against your fingers from inside the first. There was no room for it. Its outer face bears the same address, written in your hand.{/n}
{n}Jerribeth reaches toward it, then pauses to let you offer it. When you do, she opens both sheets and compares their creases.{/n}''',
          c('"I would like a reply that can find me without asking your patron where I am."', "test"),
          c('"On second thought, I should leave fate alone this evening."', abort=True)),
        n("test", "Jerribeth", '''"Two pieces of paper. You could have brought them with you."
{n}She scratches a crooked line inside one fold with the point of her nail. The same line appears in the other. She tears a small notch in its edge; the matching sheet remains whole.{/n}
"An imitation with inconsistent manners."
"An answer arriving before it has been sent. Damage is not an answer."
"How accommodating. You have explained why your trick fails the first test I gave it."
{n}She writes a word inside the folded sheet, shields it from you, and erases it. For an instant the other sheet darkens. Then it becomes blank again.{/n}
{n}Her amusement stops sounding polite.{/n}
"You brought me something I had not finished choosing to say. Then let me change it."
"The address is fixed. The answer is yours."
"That remains to be tested."''',
          c('"Test it. I am asking you to write to me, not asking the paper to answer for you."', "purpose"),
          c('"I wanted a reply you could not take back."', "refused")),
        n("refused", "Jerribeth", '''{n}She tears her sheet through the address. The other loses its brief shimmer.{/n}
"Then you should have asked a less experienced correspondent."
{n}She offers you the pieces, and waits until you take them.{/n}
"I have spent quite enough time being useful to people who misunderstand what they have purchased. We can speak about something else. This experiment is finished."''',
          c('[Put away the paper. Leave her answer unchanged.]', flags=("jerribeth.fate_experiment_refused",))),
        n("purpose", "Jerribeth", '''"What do you want to ask?"
{n}She keeps the unbroken sheet. You still hold the one with the little notch. The copies have ceased trying to resemble each other.{/n}
"I can wait," you say.
"Of course you can. You have found a way to make waiting look clever. I would like to know whether answering will be worth my time."
{n}Her delicate hands come together around the fold.{/n}
"I am not going to put Vellexia's affairs in it. Nor a list of people who can be persuaded to protect you. Those invitations have prices you have not offered to pay."''',
          c('"Tell me about something you want to make. Something you would still want without a patron watching."', "work"),
          c('"Tell me what you would choose for an evening with me, if neither of us had to entertain anyone else."', "company")),
        n("work", "Jerribeth", '''"You are inviting an artist to complain about the audience. A perilous beginning."
{n}She writes a short line, stops, and lets her hand hide it.{/n}
"No. You would mistake that for a proposal. I would rather discover whether I like the idea when you are not standing here waiting to admire it."
{n}She erases the line. Your sheet stays blank.{/n}
"I will consider the question. I may send you something quite unsuitable for an army."
"That was part of the attraction."
{n}A high chitter touches your thoughts.{/n}
"Then you have at least understood the invitation you made."''',
          c('[Leave her the unbroken sheet and keep the notched one for a quiet evening.]', flags=("jerribeth.fate_note_prepared", "jerribeth.fate_question_work"))),
        n("company", "Jerribeth", '''"You have included yourself among the people I would choose to entertain."
"I asked what you would choose."
"So you did. You may discover that I choose something which requires you to be interesting."
{n}She turns the unbroken sheet over, considering the empty space.{/n}
"An evening without borrowing somebody else's room. That would be a promising start. I might wish to leave it halfway through. You might. We could discover whether either of us bothers."
{n}She folds the sheet and keeps it between two fingers.{/n}
"I will give you an answer when you are no longer watching me compose it. You may try to look less pleased about that. It is making me consider a deliberately tiresome one."''',
          c('[Leave the answer with her and keep the notched sheet.]', flags=("jerribeth.fate_note_prepared", "jerribeth.fate_question_company"))),
    ], Relationship="jerribeth", ContactUnit=ACTOR, AnswerLists=[ANSWERS],
          Areas=[UPPER_CITY], Chapters=[4], last=4,
          requires=("trickster", "jerribeth.refuge_known"),
          forbids=("jerribeth.closed", "jerribeth.unavailable", "jerribeth.patron_lost")),

    scene("jerribeth.fate_letter", "The letter that waited for an address", "Jerribeth", 4, "", [
        n("start", "Narrator", '''{n}The notched sheet is no longer blank. You find the words while settling into a quiet evening, although no courier has come to ask where you intended to spend it.{/n}
{n}The first sentence sits at a sharp angle to the crease.{/n}
"I wrote this after you left. Your letter has been taking liberties with the order of events. I intend to charge the next person who asks me to be impressed by that."
{n}Beneath it is a smaller line.{/n}
"If it arrived while you were busy, put it away. I decline to compete with a military emergency for the attention due to my handwriting."''',
          c('[Read the reply about her work.]', "work", requires=("jerribeth.fate_question_work",)),
          c('[Read the reply about a private evening.]', "company", requires=("jerribeth.fate_question_company",), forbids=("jerribeth.fate_question_work",)),
          c('[Put the letter away until you can give it your attention.]', abort=True)),
        n("work", "Narrator", '''"A room in which the distance between two doors depends on which one you wish to reach. No prisoners. They would make the result too easy to predict. I want someone to discover that the door they were rushing toward has become tiresome, turn around, and find the other farther away than before."
{n}A drawing occupies the lower corner. At first it appears to be two doorways. When you turn the paper, a narrow street becomes visible between them. She has fitted it into the space left by the address.{/n}
"You would tell me to let the visitor leave. I would like you to tell me where to put the exit without spoiling the interesting part. That is your next contribution, if you wish to make one."
{n}The last line has been added beneath a small, impatient blot.{/n}
"It is a design. I have not built it, trapped anyone in it, or become grateful for your supervision. You may begin by looking at it."''',
          c('[Consider an exit the visitor can recognize before choosing to enter.]', "answer", flags=("jerribeth.fate_exit_visible",)),
          c('[Consider a door the visitor must choose to stop chasing.]', "answer", flags=("jerribeth.fate_exit_puzzle",))),
        n("company", "Narrator", '''"A bad performance. Preferably one expensive enough that the audience feels obliged to admire it. I would like to hear what you say when nobody can make use of your opinion."
{n}She has drawn a tiny stage. A figure bows beneath a crown which is wider than the curtain. Three smaller figures applaud with identical expressions.{/n}
"Then somewhere else. I would ask whether you thought I could have done better. You would attempt an answer that pleased me. I would tell you which part of it I believed. We might both find that more diverting than the performance."
{n}A second paragraph runs beside the drawing.{/n}
"That is an evening I could choose. I have not promised to enjoy every version of it. I am interested in discovering whether you can disappoint an expectation without becoming dull. Your letter has managed it already."
{n}She has signed only her name. Beneath it, she has begun a flourish and apparently decided against finishing it.{/n}''',
          c('[Answer that you would enjoy finding out what she actually thinks of the performance.]', "answer", flags=("jerribeth.fate_answer_curious",)),
          c('[Answer that you would like the part of the evening after leaving the audience behind.]', "answer", flags=("jerribeth.fate_answer_private",))),
        n("answer", "Narrator", '''{n}You write your answer beneath hers. For a moment your words appear on the outside of the fold, as though the paper has forgotten which side of a conversation it belongs to. Then they settle into place.{/n}
{n}One more sentence appears in her hand.{/n}
"That is enough for one experiment. An invitation need not become a prophecy merely because you have made its delivery impertinent."
{n}The writing stops. The letter remains a letter. There is no unseen hand reaching through it, and no voice you have to silence by turning it over.{/n}''',
          c('[Keep the letter beside the correspondence frame you already accepted.]', "existing", requires=("jerribeth.invitation",)),
          c('[Keep the letter and leave the next invitation for a separate choice.]', "new", forbids=("jerribeth.invitation",))),
        n("existing", "Narrator", '''{n}The frame lies where you left it. You can invite another conversation when you choose; nothing in the letter makes either of you answer it tonight.{/n}
{n}For now you have a drawing, a reply, and a small notch in the paper where Jerribeth tried to discover whether your trick would let her change her mind. She did. You have kept what she chose to send afterward.{/n}''',
          c('[Put away the letter without changing the promises already made.]', flags=("jerribeth.fate_note_read",))),
        n("new", "Narrator", '''{n}The experiment has given her a way to place one invitation before you. It has not supplied an answer to it.{/n}
{n}You fold the sheet with her drawing on the inside. Whatever she sends next, you will still have to decide whether you want to open it.{/n}''',
          c('[Keep the letter. Consider any further correspondence on its own terms.]', flags=("jerribeth.fate_note_read",))),
    ], Relationship="jerribeth", Remote=True, Areas=[NEXUS, DREZEN], Chapters=[4, 5],
          requires=("jerribeth.fate_note_prepared",), delay=24,
          forbids=("jerribeth.closed", "jerribeth.unavailable")),
]

for authored_scene in SCENES:
    for page in authored_scene["Nodes"]:
        page["Portrait"] = "Jerribeth"


def integrate(payload):
    """Let the chosen fate letter precede an unplayed ordinary invitation, additively."""
    by_id = {item["Id"]: item for item in payload["Scenes"]}
    for required in ("jerribeth.invitation", "jerribeth.fate_envelope", "jerribeth.fate_letter"):
        if required not in by_id:
            raise ValueError("Jerribeth fate integration missing scene: " + required)
    invitation = by_id["jerribeth.invitation"]
    if "jerribeth.fate_note_prepared" not in invitation["Forbids"]:
        invitation["Forbids"].append("jerribeth.fate_note_prepared")
    invitation.setdefault("ForbidOverrides", {})["jerribeth.fate_note_prepared"] = "jerribeth.fate_note_read"
