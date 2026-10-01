"""Eritrice: the standing debate that turns a carried motion into a courtship.

Every scene is in the Council hall, on her own private list (Council_Eritrice/AnswersList_0002), after the private
debate has opened (eritrice_trickster). Each engages a canon anchor of hers:
- her element and her method (Council_Eritrice/Cue_0010 ea54bde3, Cue_0011 de26ea2b, Cue_0012 964c59cf);
- the Worldwound as a mistake that truth can refute (Cue_0013 ffd7f359) and force that "doesn't prove anything"
  (Cue_0022 b3e5d929), her dream of a neutral table for all the planes (Cue_0025 98643438, Council_5-2/Cue_0001 3d07c9e5);
- the quill and the snow-white scroll (Council_2/Cue_0030 6cc3a4f0, Council_3/Cue_0014 07c13d2e);
- Alichino, "noble in their own way" (Cue_0016 ecfda3ea, Cue_0017 2a0504b6), and Socothbenoth, who "suggested I convene
  the Council" (Cue_0018 3b128644, Cue_0019 9b90dc19);
- the mortal "narrow outlook on life" (Council_1/Cue_0024 68981c2d);
- the usurped chair (Council_3/Cue_0045 cf4e1e43, Council_5-1/Cue_0010 512981db) and the walk-out (Council_Lexicon2/Cue_0048 222e6f61);
- the cipher she could not read (Lexicon2/Cue_0050 88a1ec4c);
- "Why, you, of course!" and "At worst, you'll die" (Lexicon2/Cue_0040 c4551626, Cue_0046 3d5645ec);
- essence extraction, "a very serious matter" (Council_5-2/Cue_0020 93bbb373), and "I am used to suffering for the
  sake of truth" (Cue_0026 449c6513).
Her history before the Council is her own telling in her own voice, and she says as much; nothing here states it as fact.
"""
from story_format import c, p, scene
from storylines.eritrice_trickster import CAUGHT, CLOSED, COMMITTED, DEBATED, DECLINED, LIST, LOST, STARTED, STRAIGHT, e, nar

SCENES = []
M = "eritrice.minutes."

# Canon moments this module reads (SeenCues).
CHAIR_USURPED = "eritrice.chair_usurped"      # Council_3/Cue_0045: "I don't recall appointing you chairperson..."
CHAIR_IGNORED = "eritrice.chair_ignored"      # Council_5-1/Cue_0010: "I'm the... chairperson... Grrrgh!"
WALKED_OUT = "eritrice.council_walked_out"    # Council_Lexicon2/Cue_0048: members leave over her protests
TOLD_ALICHINO = "eritrice.told_alichino"      # Council_Eritrice/Cue_0016: "How could I ... not have noticed"
TOLD_SOCOTH = "eritrice.told_socoth"          # Council_Eritrice/Cue_0018 or Cue_0019
NARROW = "eritrice.narrow_outlook"            # Council_1/Cue_0024: "the mortal brain is capable of conceiving an idea"
CIPHER = "eritrice.cipher_unread"             # Council_Lexicon2/Cue_0050: "But I can't read it. You try."
PROPOSED_KEY = "eritrice.proposed_key"        # Council_Lexicon2/Cue_0040 "Why, you, of course!" or Cue_0046 "At worst, you'll die"
ESSENCE_GIVEN = "eritrice.essence_given"      # Council_Eritrice/Cue_0026 "I won't lie, it was excruciating." (she gave hers, allied branch)

SEEN_CUES = {
    CHAIR_USURPED: ["cf4e1e4352bb4fe4ea85d93d82c4b4b5"],
    CHAIR_IGNORED: ["512981db805f7184aa9af6361286323a"],
    WALKED_OUT: ["222e6f61837a88c42825b4e4bf800e78"],
    TOLD_ALICHINO: ["ecfda3ea2f76d2e4c8a970c09a449ed4"],
    TOLD_SOCOTH: ["3b128644f6776f94ca41902a85a2b2a1", "9b90dc19d38651741b19e380a2bfe2ff"],
    NARROW: ["68981c2d5949c2744a2a985813222f01"],
    CIPHER: ["88a1ec4c7221d0e4ea21a18133b43749"],
    PROPOSED_KEY: ["c455162655e5aa74fa10d6445315c7a3", "3d5645ec9fcc0b147bcae86edb345795"],
    ESSENCE_GIVEN: ["449c6513d5c3b9844bf29547b3ce33ab"],
}

POINT_ONE = M + "point_one"
CONVENING = M + "the_convening"
QUILL = DEBATED                                # M + "quill": the last point before the second reading
DEVIL = M + "a_noble_devil"
SUGGESTED = M + "who_suggested_it"
NARROWED = M + "a_narrow_outlook"
ORDER = M + "point_of_order"
CIPHERED = M + "the_cipher"
AT_WORST = M + "at_worst"
SEATS = M + "stay_in_your_seats"
ESSENCE = M + "a_serious_matter"
ADJOURNED = M + "adjourned"
RECORD = M + "the_record"
STANDING = M + "a_standing_item"
BLANK = M + "the_blank_line"

# Outcomes other scenes and the epilogue read.
CONCEDED = M + "conceded_a_point"
FORCE = M + "argued_force"
TABLE = M + "argued_the_table"
WROTE = M + "wrote_in_the_minutes"
DEVIL_DEFENDED = M + "alichino_defended"
DEVIL_EXPOSED = M + "alichino_exposed"
SOCOTH_EXPOSED = M + "socoth_exposed"
SOCOTH_COVERED = M + "socoth_covered"
KEY_FORGIVEN = M + "key_forgiven"
KEY_HELD = M + "key_held_against_her"
KEY_USED = M + "key_used"
PROMISED = M + "essence_promised"
URGED = M + "essence_urged"
WARNED = M + "warned_of_betrayal"
MINUTED = M + "night_minuted"
OMITTED = M + "night_left_blank"
AFTER_WAR = M + "after_the_war"


def minutes(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5)):
    """A physical sitting of the standing debate, on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Eritrice", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="eritrice", Chapters=list(chapters), AnswerLists=[LIST]))


# --- 1. Point one. ---------------------------------------------------------------------------------------------------

minutes(POINT_ONE, "Point one", '"You said, point by point."', [
    nar("open", '''{n}The hall is empty. The Council's chairs stand pushed in along the long table, and the lamps have burned down to the colour of old brass. Eritrice sits alone at the head of the table with a fresh scroll unrolled in front of her. At the top, in her upright hand, is a heading: "Standing debate. The chair against the Commander."{/n}''',
        c("Continue", "lied", requires=(CAUGHT,)),
        c("Continue", "straight", requires=(STRAIGHT,), forbids=(CAUGHT,)),
        c("Continue", "rules", forbids=(CAUGHT, STRAIGHT))),
    e("lied", '''"Sit. The last time you addressed the chair, you tried to carry a vote with your own voice pretending to be six. It is minuted." {n}She taps the line without looking at it.{/n}
"I will not hold it against you in the debate. I will hold it against you in everything else. Proceed."''',
      c("Continue", "rules")),
    e("straight", '''"Sit. The last time you addressed the chair, you argued straight, and you argued that I like losing to you." {n}Her whiskers twitch.{/n}
"It is minuted. I have read it eleven times. It does not become less impertinent."''',
      c("Continue", "rules")),
    e("rules", '''"Here are the rules. I have written them down, so that neither of us can pretend later that they were otherwise." {n}She turns the scroll so you can read it.{/n}
"One. Each of us may raise one point per sitting. Two. A point is answered honestly or not at all. Three. A point conceded stays conceded. Four. The chair keeps the minutes." {n}Her quill hovers.{/n} "Five. The debate ends when one of us concedes the motion. It has no fixed end otherwise. I have debated angels on smaller matters than this, for longer than you would believe."''',
      c('"What is the motion, exactly?"', "motion"),
      c('[Flirt] "Rule six: the chair sits closer."', "closer")),
    e("closer", '''"There is no rule six." {n}She writes, however: "Rule six moved from the floor. Not seconded."{/n}
"And the chair sits where the chair sits. At the head of the table." {n}She does not move her chair. After a moment she moves the lamp, which puts the two of you in the same circle of light, and does not remark on it.{/n}''',
      c('"What is the motion, exactly?"', "motion")),
    e("motion", '''"You moved that the chair is in dire need of a private debate. I have since refined it. It was badly drafted." {n}She reads it aloud.{/n}
"Resolved: that the chair, who has convened celestials and demons and devils and the Eldest at one table in search of the truth about the Worldwound, is in need of a debate with one mortal who does not want anything from her." {n}The quill stops.{/n} "The last clause is the one I object to. Everybody wants something from me."''',
      c('"I want your vote. On the Worldwound. On me."', "honest"),
      c('"I don\'t want anything. I just like watching you lose."', "tease"),
      c('[Trickster] "I want your minutes. Everything you write turns out true."', "minutes")),
    e("honest", '''{n}A long, considering silence. Her amethyst eyes do not move from you.{/n}
"That is an honest answer. It is also two points, and I will allow only one tonight." {n}She writes "The Commander wants the chair's vote" and underlines "vote" twice.{/n}
"Everyone who has ever sat at this table has wanted my vote. You are the first who has said so without dressing it up as a principle."''',
      c("Continue", "concede_ask")),
    e("tease", '''"You have not yet seen me lose." {n}A low growl, the kind that begins in the chest and does not quite reach the throat.{/n}
"If you ever see me concede an adjournment, it will be because arguing about it with the whole Council watching would be undignified. That is not losing. That is chairing." {n}She writes: "The Commander claims to enjoy the chair's defeats. The chair notes there have been none."{/n}''',
      c("Continue", "concede_ask")),
    e("minutes", '''{n}Her claws come down on the scroll, flat, as if to hold it against a wind.{/n}
"My minutes are true because I do not write lies. Not because the ink is enchanted, not because I am. You understand the difference? If I ever write down a lie, the whole record is worthless. Centuries of it." {n}She looks at the word "carried" at the foot of the older scroll, beside her elbow.{/n}
"You made me write one down that was true. I have not forgiven you for being right."''',
      c("Continue", "concede_ask")),
    e("concede_ask", '''"Now. The rules say one point per sitting, and you have made yours. Mine."
{n}She sets the quill down and folds her hands on the scroll. On the table between you lies the crusade's latest casualty list, weighted with her inkwell. She has read it. You can tell by the pinholes where her claws rested.{/n}
"Point one, for the chair: you did not come to this Council for the truth. You came because Socothbenoth brought you, and you stayed because we are useful. Concede it, or refute it."''',
      c('"Conceded. I came for what you could give the crusade. I stay for other reasons."', "conceded", flags=(CONCEDED,)),
      c('"Refuted. I came because nobody else was trying to close the Worldwound without dying of it."', "refuted"),
      c('[Lie] "I came for the truth, same as you."', "lie")),
    e("conceded", '''"Conceded." {n}She writes it, and pauses over "other reasons", and does not ask what they are, which costs her something you can watch.{/n}
"You concede quickly. It is a dangerous habit in a debater. It makes the other side wonder what you are saving."''',
      c("[Leave her with the scroll.]")),
    e("refuted", '''"Refuted." {n}She considers it.{/n} "Partly. You have refuted 'came'. You have not refuted 'stayed'." {n}She writes it down anyway, in full, and marks the point as contested.{/n}
"Contested points are carried over to the next sitting. You will find, Commander, that I carry things over for a very long time."''',
      c("[Leave her with the scroll.]")),
    e("lie", '''{n}She does not write it down. That is the first thing you notice. The quill stays where it is, and her eyes stay on you, and something in her face closes like a door that has been left ajar in a draught.{/n}
"No, you did not." {n}Quietly.{/n} "The chair will not minute a lie. Take your point back and give me a true one, or give me none."''',
      c('"...Conceded. I came for what you could give the crusade."', "conceded", flags=(CONCEDED,)),
      c('"None, then."', "none")),
    e("none", '''"None, then." {n}She rules a thin line under the point, which in her minutes means "unanswered".{/n}
"Unanswered points are also carried over. They are heavier than the contested ones. You will feel it."''',
      c("[Leave her with the scroll.]")),
], requires=(STARTED,), forbids=(POINT_ONE,))


# --- 2. Why a Council. ------------------------------------------------------------------------------------------------

minutes(CONVENING, "Why a Council", '"Point two. Why a Council?"', [
    e("start", '''"Because every other way has been tried." {n}She says it at once, as if the question had been waiting in her mouth for years for someone to ask it.{/n}
"Many have tried to solve the problem of the Worldwound with weapons, and none have succeeded. I convened this Council when the Wound was still new, to try another way, and do what no one had tried before: resolve everything through negotiation. Since then, four crusades. Four. How many dead, Commander? Your own clerks cannot tell me. I asked."''',
      c('"How successful has it been?"', "success"),
      c('"You could have fought. You\'re an empyreal lord."', "fight")),
    e("success", '''{n}She pauses to think, and then answers in a voice with no doubt left in it at all.{/n}
"Up until now, there have been few successes. But we keep trying. The truth always comes out, sooner or later."
{n}Her claws tap the table: once, twice, three times.{/n} "You are about to tell me that 'sooner or later' is a luxury the people of Mendev do not have. Everyone tells me that. It is not a refutation. It is an impatience."''',
      c("Continue", "fight")),
    e("fight", '''"A victory obtained through brute force doesn't prove anything. The more blows you deal to Deskari and his followers, the more convinced they are of their rectitude."
{n}She leans forward, and the lamplight catches the amethyst of her eyes.{/n}
"The Worldwound is a mistake, Commander. An aberration in the world order. And like any mistake, it can be corrected if the truth that refutes it is found and made public. I do not need an army to refute a mistake. I need a table and an honest room."''',
      c('"Tell that to the dead at Kenabres. The demons weren\'t debating."', "force"),
      c('"Then let me help you set the table. I\'ve brought the Worldwound itself to this one."', "table"),
      c('"You\'re both wrong. I\'ll win the war and you\'ll win the argument afterwards."', "both")),
    e("force", '''{n}The growl is louder this time. It is the sound she makes when the Council ignores her, and when you adjourn her meetings for her, and she does not seem to know she is making it.{/n}
"I know what the demons were doing at Kenabres. I have read every report your crusade has filed, and a great many it has not." {n}Her claws have come out, the tips pale against the dark wood.{/n}
"And after Kenabres, your crusade killed a great many demons, and the Worldwound is exactly as wide as it was. Refute that, Commander. With a sword, if you like."''',
      c('"I can\'t. Not yet. But I\'m still going to swing it."', "force_end", flags=(FORCE,))),
    e("force_end", '''"Yes. You are." {n}She sheathes the claws, slowly, one by one, and writes.{/n}
"Point two: the Commander holds that force is necessary. The chair holds that it proves nothing. Contested." {n}She looks up.{/n} "The chair also notes that the Commander is the only member of this Council who has ever made her growl on purpose. That is not part of the point. I am writing it down anyway."''',
      c("[Leave her with the scroll.]")),
    e("table", '''{n}For a moment she does not answer at all. Then she smiles, and it changes her face entirely: the lion recedes and something very old and very pleased looks out.{/n}
"You did, didn't you. A wormhole to every plane at once. A crossroads where the wound was." {n}She says it the way other people say the names of places they grew up.{/n}
"On neutral ground, equally remote from all the planes, we could lay down our weapons and hear one another out for the first time in the history of the multiverse. Angels and devils, fey and aeons, in a battle of arguments. You gave me that. I have been trying to draft it for longer than your crusades have had numbers."''',
      c('"Then vote for it. And for me."', "table_end", flags=(TABLE,))),
    e("table_end", '''"One point per sitting, Commander." {n}But she writes it all down, and at the end, very small, as if it were a note to herself: "The chair was moved."{/n}
"Point two: the Commander holds that the table can be built. The chair agrees. Carried." {n}She blots it.{/n} "That is the first point you have carried against me. Do not let it go to your head. The chair was already of that opinion."''',
      c("[Leave her with the scroll.]")),
    e("both", '''"That is not a position. That is a truce." {n}But she tilts her head, the way a cat tilts it at a noise it has not placed.{/n}
"And yet. The Council has been winning the argument for a very long time, and nobody has been listening. If someone won the war first, they might listen." {n}She taps her quill on the scroll.{/n}
"I dislike it. I dislike that I cannot refute it. The chair minutes the point as carried, with reservations, and the reservations run to a page."''',
      c("[Watch her write the page.]", flags=(FORCE, TABLE))),
], requires=(POINT_ONE,), forbids=(CONVENING,))


# --- 3. The quill: the last point before the second reading. --------------------------------------------------------

minutes(QUILL, "The quill", '"Can I ask about the quill?"', [
    nar("open", '''{n}She is writing when you come in, and she finishes her line before she looks up: a long one, about a skirmish at the edge of the Worldwound that your own couriers reported only this morning. The quill is white, very long, and very plain. You have never seen it out of her hand.{/n}''',
        c("Continue", "start")),
    e("start", '''"You may ask. It is a quill." {n}She holds it up to the lamp, as if the answer might be written on it.{/n}
"It is not magical. It is not holy. It was not given to me by a god in a shaft of light. I have had many. When one wears out, I cut another. This is the six hundred and twelfth." {n}A pause.{/n} "I keep count. Of course I keep count."''',
      c('"Why do you never put it down?"', "down"),
      c('"Has anyone else ever held it?"', "held")),
    e("down", '''"Because the moment I put it down, something will be said that nobody writes down. And then, a year later, someone will say it was never said at all." {n}Her voice has gone very quiet.{/n}
"That is how the lies begin, Commander. Not with a demon whispering. With a room where nobody kept the minutes. Every war I have ever seen started in a room like that."''',
      c("Continue", "held")),
    e("held", '''"No one." {n}She says it too quickly, and hears herself say it too quickly, and her whiskers flatten.{/n}
"Alichino asked once. To 'correct a clerical error'. Socothbenoth asked, often, for reasons he made very clear. Chadali asked to draw a flower in the margin." {n}Something almost like a laugh.{/n} "I let her dictate the flower to me. I drew it myself. It was a very poor flower."''',
      c('[Hold out your hand for the quill.]', "hand", requires=(CAUGHT,)),
      c('"I wouldn\'t ask. It\'s yours."', "wouldnt"),
      c('[Hold out your hand for the quill.]', "hand_honest", forbids=(CAUGHT,))),
    e("hand_honest", '''{n}She looks at your open hand as if it were a motion she had not expected on the agenda.{/n}
"You are asking the chair to hand the record to the Commander. The Commander who raised one hand in an empty hall, counted it as the whole Council, and made the chair write 'carried' on a motion with no floor."
{n}Her claws turn the quill over, once. Then she lays it across your palm, and her fingers stay on it a moment longer than the quill needs.{/n}
"One line. True. I will be watching."''',
      c("[Write: \"The chair is not what I expected.\"]", "wrote", flags=(WROTE,)),
      c("[Write: \"The Commander concedes nothing.\"]", "wrote_joke", flags=(WROTE,)),
      c("[Hand it back, unused.]", "unused")),
    e("hand", '''{n}She looks at your open hand as if it were a motion she had not expected on the agenda.{/n}
"You are asking the chair to hand the record to the Commander. The Commander who once carried a vote by pretending to be six people, and who made the chair write 'carried' on a motion with no floor."
{n}Her claws turn the quill over, once. Then she lays it across your palm, and her fingers stay on it a moment longer than the quill needs.{/n}
"One line. True. I will be watching."''',
      c("[Write: \"The chair is not what I expected.\"]", "wrote", flags=(WROTE,)),
      c("[Write: \"The Commander concedes nothing.\"]", "wrote_joke", flags=(WROTE,)),
      c("[Hand it back, unused.]", "unused")),
    e("wouldnt", '''"No. You would not." {n}She looks at you, the quill very still between her claws.{/n}
"Alichino asked for it. Socothbenoth asked for it. Chadali asked for it. You are the first person at this table who has declined to ask for the one thing I would have refused." {n}Something in her face shifts, like a verdict being reconsidered.{/n}
"Which is precisely why I am going to offer it." {n}She turns the quill around and holds it out to you, feather first.{/n} "One line. True. I will be watching."''',
      c("[Write: \"The chair is not what I expected.\"]", "wrote", flags=(WROTE,)),
      c("[Write: \"The Commander concedes nothing.\"]", "wrote_joke", flags=(WROTE,)),
      c("[Hand it back, unused.]", "unused")),
    e("wrote", '''{n}She reads it upside down, before you have finished the last word. Her ears go back, and then forward again.{/n}
{n}She says it as though accusing you:{/n} "That is true. I checked. I cannot find the lie in it." {n}She takes the quill back and, under your line, writes her own: "Nor is the Commander."{/n}
"Both made in good faith." {n}Her voice is not steady.{/n} "I am out of breath, Commander. I do not know why. That is a lie. I think I do."''',
      c("Continue", "close")),
    e("wrote_joke", '''"That is a lie." {n}She is already reaching for it, and stops.{/n} "No. It is a joke. It is written as a joke, so it is true as a joke." {n}Her whiskers twitch, violently.{/n}
"You have found the one thing in my minutes I have no rule for. Nobody has ever made a joke in them before." {n}She does not strike it out. She writes, underneath: "Minuted as a jest. The chair concedes that it was funny."{/n}
"That is my first concession, Commander. Look at it. It will not happen often."''',
      c("Continue", "close", flags=(CONCEDED,))),
    e("unused", '''{n}You hand it back. She takes it, and does not write anything for a while.{/n}
{n}At last:{/n} "You could have written anything. Anything at all, and I would have had to keep it, because I promised to keep the minutes true, and a line in your hand would be a true record of what you wrote." {n}She turns the quill over.{/n}
"You gave it back." {n}Her whiskers twitch.{/n} "I had a rule ready for whatever impertinence you wrote. You have left the chair holding an unused rule. I resent it, and I respect it, and I am minuting both."''',
      c("Continue", "close")),
    e("close", '''{n}She rolls the scroll up, slowly, and does not look at you while she does it.{/n}
"I have been debating you because you are the only one at this table who argues with me as if the argument mattered more than winning. The others want my vote. You wanted it too, and said so, and then argued with me anyway." {n}A breath.{/n}
{n}She ties the scroll, and her claws fumble the knot, which you have never seen them do.{/n} "I think you know what I am going to ask you next. Do not answer. I have not asked it yet, and when I do, I want to have the courage to ask it properly."''',
      c("[Leave the hall without answering.]")),
], requires=(CONVENING,), forbids=(QUILL,))


# --- 4. A noble devil (Alichino). ---------------------------------------------------------------------------------------

minutes(DEVIL, "A noble devil", '"Point of information. About Alichino."', [
    nar("open", '''{n}Alichino's chair is empty, as it usually is. A small black notebook lies on the seat, forgotten or left on purpose. Eritrice has not touched it. She is looking at it the way one looks at a snake that may be asleep.{/n}''',
        c("Continue", "told", requires=(TOLD_ALICHINO,)),
        c("Continue", "start", forbids=(TOLD_ALICHINO,))),
    e("told", '''"You told me once that he is a weasel. That he is interested in personal gain, not debate." {n}Her amethyst eyes narrow.{/n}
"I said I would take a closer look at him and form my own conclusions. I have taken a closer look. I have not yet formed the conclusions. That is why the notebook is still on the chair."''',
      c("Continue", "start")),
    e("start", '''"Devils are evil. But they are also noble in their own way. Alichino searches for the truth for his own benefit. As do we all." {n}She says it like a lesson she has recited to herself many times, and has begun to doubt.{/n}
"The nature of the truth is such that, when it is discovered, it does good for everyone, whatever their reasons for seeking it. That is what I have always believed. Tell me it is still true."''',
      c('"It\'s still true. Even a devil can find the truth. He just won\'t share it."', "defend"),
      c('"He\'s selling you, Madam Chair. Whatever you find, he\'s already found a buyer."', "expose"),
      c('[Pick up the notebook.]', "notebook")),
    e("defend", '''{n}Her shoulders come down a clear inch, as if she had been holding them up since before you came in.{/n}
"Yes. That is the distinction. Finding and sharing are different verbs." {n}She writes: "The Commander holds that a devil may find the truth. Carried."{/n}
"You have made the chair feel less foolish. That is a dangerous gift, Commander. Devils give it too, and I usually notice."''',
      c("[Leave the notebook where it is.]", flags=(DEVIL_DEFENDED,))),
    e("expose", '''"He would not." {n}A flat, instant denial. Then, slower:{/n} "He would. He has a gift for attending the sessions at which something can be sold, and for being elsewhere when the rest are decided." {n}She lifts one claw and pushes the notebook, very slightly, as if it were hot.{/n}
"I will tell you what I have never told the Council. I invited him because I thought a Council without Hell would be a lie. A Council with him in it may be a worse one."''',
      c('"Then keep him. And watch him. You\'re good at watching."', "expose_end", flags=(DEVIL_EXPOSED,))),
    e("expose_end", '''"I am." {n}Something in her face softens, very slightly.{/n} "I keep the minutes. He keeps a little black book. We will see whose record is the longer."
{n}She writes: "Motion from the floor: that the chair watch Alichino. Carried. The chair notes that she had already been doing so, but badly."{/n}''',
      c("[Leave the notebook where it is.]")),
    e("notebook", '''{n}Her hand is on your wrist before you have lifted it an inch. It is warm, and very strong, and the claws are sheathed, but only just.{/n}
"No." {n}Softly.{/n} "If you read it, you will know what he knows. And then you will be tempted to use it, and I will have to minute that you did." {n}She lets go.{/n}
"Everyone at this table has a book they would rather nobody read. Leave him his. Ask me your point instead."''',
      c('"Then my point: he\'s selling you."', "expose"),
      c('"Then my point: even a devil can find the truth."', "defend")),
], requires=(POINT_ONE,), forbids=(DEVIL,))


# --- 5. Who suggested the Council (Socothbenoth). -------------------------------------------------------------------

minutes(SUGGESTED, "Who suggested it", '"Point of information. Who suggested the Council?"', [
    e("start", '''"Socothbenoth." {n}No hesitation at all; she has never lied about it, and it does not occur to her to begin now.{/n}
"It was Socothbenoth who suggested I convene the Council. He may be a demon, but we are united by something much more than a difference of planes. A shared search for the common truth." {n}She hears it as she says it, and her ears go back a fraction.{/n}
"You are going to tell me that is not what he is searching for."''',
      c("Continue", "told", requires=(TOLD_SOCOTH,)),
      c("Continue", "ask", forbids=(TOLD_SOCOTH,))),
    e("told", '''"You told me before that he joined only to get under my skin. I said I knew about his feelings. He does not conceal them." {n}Her claws drift, as they did then, toward the hilt of the dagger at her belt, and stop.{/n}
"Above affinity he is tempted by intimacy, and it does not matter with whom. I thought I could turn a blind eye to that for the sake of the common goal. I am no longer sure what the common goal is."''',
      c("Continue", "ask")),
    e("ask", '''"So. Your point. What does Socothbenoth want from my Council?"
{n}She does not pick up the quill. That is how you know she is afraid of the answer.{/n}''',
      c('"Something from his sister. He wants a table full of powers to lean on her. You\'re the table."', "expose"),
      c('[Lie] "Company. He\'s bored. Demons get bored."', "cover"),
      c('"I don\'t know yet. When I do, you\'ll hear it first."', "promise")),
    e("expose", '''{n}She is very still. Then she stands, walks the length of the long table to his empty chair, and stands behind it with her hands on its back, as if she might lift it and throw it across the hall.{/n}
"Nocticula." {n}The name comes out of her like a growl with words in it.{/n} "If you are right, he brought me the idea of a Council, and then he brought me you, and all the while he wanted something from his sister. I thought I was the chair. I may have been the furniture. I will find out which, and when I do, it will be minuted."''',
      c("Continue", "expose_end")),
    e("expose_end", '''{n}She comes back and sits down, and picks up the quill at last, and her hand is quite steady.{/n}
"Thank you. It is a horrible thing to be told, and you told it to me plainly. Nobody else at this table would have." {n}She writes, and goes on writing.{/n}
"I will not expel him. A Council that expels its liars is left with nobody to debate. But I will never again mistake his reasons for mine."''',
      c("[Leave her to her writing.]", flags=(SOCOTH_EXPOSED,))),
    e("cover", '''{n}She looks at you, and then, visibly, decides to believe you, the way one decides to step onto ice.{/n}
"Bored. Yes. That is very like him." {n}She writes it down: "The Commander holds that Socothbenoth is bored." She underlines nothing.{/n}
"Thank you, Commander. I was afraid you would tell me something I would have to act on." {n}She rolls the scroll. She does not look at it again while you are there.{/n}''',
      c("[Leave her with the lie.]", flags=(SOCOTH_COVERED,))),
    e("promise", '''"That is not a point. That is a promise." {n}But she writes it down, word for word, and reads it back to you in the chair's voice, and waits.{/n}
"If you do not keep it, it will be the first broken promise in my minutes. I have kept these minutes a very long time, Commander. I would prefer not to begin with you."''',
      c("[Say it again, word for word, so that she has heard it twice.]")),
], requires=(POINT_ONE,), forbids=(SUGGESTED,))


# --- 6. A narrow outlook (mortals). ----------------------------------------------------------------------------------

minutes(NARROWED, "A narrow outlook", '"Point of order. About mortals."', [
    nar("open", '''{n}She is reading your crusade's dispatches again, the ones you did not send her. There is a stack of them at her elbow, sorted by date, annotated in the margins in a hand much smaller than her minutes.{/n}''',
        c("Continue", "quoted", requires=(NARROW,)),
        c("Continue", "start", forbids=(NARROW,))),
    e("quoted", '''"You want to quote me to myself. Go on. I know which line." {n}She recites it before you can:{/n} "'Maybe, despite their narrow outlook on life, the mortal brain is capable of conceiving an idea worthy of consideration.'"
"It is minuted. I said it the day Socothbenoth brought you in. I have regretted the adjective ever since, and the noun, and most of the verbs."''',
      c("Continue", "start")),
    e("start", '''"Very well. The point." {n}She folds her hands.{/n} "You are going to tell me that the chair looks down on mortals. It is true. I do. Not because you are small. Because you are brief." {n}Her claws tap the dispatches.{/n}
"You live sixty years if the demons allow it. You forget what you promised in a decade. Your crusades are numbered because each one forgets the last. I have watched it four times now. How am I to trust a debate with someone who will not be here to hear the answer?"''',
      c('"That\'s why we argue harder. We don\'t have time to be wrong slowly."', "harder"),
      c('"You\'ve had a century of sessions and got nowhere. I took a month to give you a crossroads."', "month"),
      c('"Then trust me for as long as I\'m here. I\'ll try to make it long."', "long")),
    e("harder", '''{n}She opens her mouth to answer, and closes it, and opens it again.{/n}
"'Wrong slowly.'" {n}She tastes the phrase.{/n} "That is my whole Council, Commander. That is every session I have ever chaired. Wrong slowly, with minutes." {n}She writes, and her quill digs into the scroll hard enough to catch.{/n}
"Point conceded. The chair concedes that the mortal brain has, on this occasion, conceived an idea she would rather not have heard."''',
      c("[Leave her with the concession.]", flags=(CONCEDED,))),
    e("month", '''"A century is not 'nowhere'." {n}Her ears have gone flat against her skull.{/n} "A century of sessions is a century of minutes, and minutes are how the truth is..."
{n}She stops. And then, unwillingly, something like a laugh, low in her chest.{/n} "No. You are right. A century. And a month. One mortal. A crossroads." {n}She writes it down, and underlines "one mortal" twice.{/n}
"That is not a refutation. It is worse. It is an example."''',
      c("[Leave her with the example.]", flags=(CONCEDED,))),
    e("long", '''{n}She does not answer at once. Her eyes go to the dispatches, to the casualty lists at the bottom of the stack, to the names on them she has read and you have not.{/n}
"You say that as if it were in your power." {n}Very quietly.{/n} "It is the least honest thing you have said at this table, and the kindest, and I cannot decide which I should minute."
{n}She minutes both.{/n}''',
      c("[Leave her with both.]")),
], requires=(CONVENING,), forbids=(NARROWED,))


# --- 7. Point of order (the usurped chair). -------------------------------------------------------------------------

minutes(ORDER, "Point of order", '"You wanted to see me, Madam Chair?"', [
    nar("open", '''{n}She is standing when you come in, which she never is, at the head of the table with both hands flat on it. The quill is lying on the scroll. She has not written a word.{/n}''',
        c("Continue", "ignored", requires=(CHAIR_IGNORED,)),
        c("Continue", "usurped", requires=(CHAIR_USURPED,), forbids=(CHAIR_IGNORED,))),
    e("usurped", '''"'I think our meeting can be adjourned. Get to work.'" {n}She quotes you exactly, down to the pause.{/n}
"My dear {name}, with all due respect, I do not recall appointing you chairperson. I said so at the time. And then I adjourned the meeting anyway, because you had already done it, and the whole Council had heard you, and to argue would have been undignified." {n}A growl, low.{/n}
"I have been undignified about it privately ever since."''',
      c("Continue", "point")),
    e("ignored", '''"'What? No, you can't do that. I'm the... chairperson...'" {n}She quotes herself, flatly, and her lip lifts off one long tooth.{/n}
"And then I growled. In session. In front of Cobblehoof, who snorted, and Socothbenoth, who applauded. It is in my own minutes. I had to write down that I growled." {n}She sits down, at last, hard.{/n}
"I convened this Council. I set its table. They walk out on me. They adjourn over me. And you, Commander, laugh. I have seen you."''',
      c("Continue", "point")),
    e("point", '''"Point of order. The chair demands to know why the Commander does it."''',
      c('"Because your meetings would still be going on if I didn\'t."', "true"),
      c('"Because you growl. I like it when you growl."', "growl"),
      c('"I\'m sorry. I\'ll stop."', "sorry")),
    e("true", '''"That is true." {n}She says it with enormous reluctance.{/n} "Some of them would. The session on demonic taxation would still be going on. Alichino was only at page nine of his proposal."
"But it is my table. When you adjourn it for me, they see that anyone can. And a Council where anyone can end the debate is a Council where the debate never ends honestly."''',
      c('"Then give me a gavel. I\'ll only use it when you nod."', "gavel"),
      c('"Then I\'ll stop."', "sorry")),
    e("growl", '''{n}The growl she was about to make stops halfway, which produces a sound somewhere between a lion and a kettle.{/n}
"That is not a reason. That is a provocation." {n}Her breath catches.{/n} "The chair will not be provoked into growling for the Commander's amusement. The chair..."
{n}She growls. She hears it. She puts her face in her hands, briefly, and when she takes them away she is almost smiling.{/n}
"Minute that, and I will have you removed from the hall."''',
      c("[Do not minute it.]", "gavel")),
    e("sorry", '''{n}She looks at you with an expression you have not seen on her before, as if you had done something slightly unfair.{/n}
"No. Do not stop. If you stop, I will only wonder what else you are holding back." {n}She picks up the quill.{/n}
"The chair rules that the Commander may adjourn one meeting in three, on a sign from the chair. The sign is this." {n}She taps the scroll twice with her claw.{/n} "Nobody else will ever know it. That is the only secret in my minutes, and I am writing it down anyway."''',
      c("[Learn the sign.]")),
    e("gavel", '''"There is no gavel. This is not a tavern." {n}But she taps the scroll twice with her claw, deliberately, watching you.{/n}
"That is the sign. When I do that, and only then, you may say 'Get to work', and I will pretend to be scandalised." {n}She writes it down, in the smaller hand she uses for her own notes.{/n}
"The chair notes that she has delegated one power of the chair, which she has not done since the Council was convened. The chair is not sure she will survive it."''',
      c("[Learn the sign.]")),
], requires=(POINT_ONE,), forbids=(ORDER,))
ORDER_SCENE = SCENES[-1]
ORDER_SCENE["RequiresAnyGroups"] = [[CHAIR_USURPED, CHAIR_IGNORED]]


# --- 8. The cipher (Chapter 5). ---------------------------------------------------------------------------------------

minutes(CIPHERED, "What the truth could not read", '"You looked at the Lexicon pages again."', [
    e("start", '''{n}The pages of the Lexicon of Paradox lie on the table in front of her, in the order you left them. She has laid a sheet of clear glass over them, to keep them from curling, and has plainly been looking at them for days.{/n}
"There is something hidden within these pages. A cipher. I held them up close, and at a distance, and from every angle, and I could not read it. Alichino wanted a key. Shyka could read it, and would not." {n}Her voice is perfectly level.{/n} "And you told us to lay both parts side by side, as though that were obvious."''',
      c('"You wanted it to be true or false. It\'s both."', "both"),
      c('"You read for the truth. Areelu wrote for the lie."', "lie")),
    e("both", '''"Both." {n}She says the word as if it were in a language she had heard of but never spoken.{/n}
"A paradox. The Lexicon of Paradox. I read the title, and then I read the pages as if the title were an exaggeration." {n}Her claws rest on the glass.{/n}
"I have spent my whole existence finding the one truth that refutes a lie. It never occurred to me that the lie might need to be true as well, to be read. Everything I cannot read, I cannot read because I will not believe two things at once."''',
      c("Continue", "humbled")),
    e("lie", '''"She wrote it for someone who lies." {n}A slow, terrible understanding.{/n} "Of course. A cipher is a locked room, and a lock is made to keep out an honest hand. Alichino could not see into it either, for all his glasses."
"If there is a way in, a trickster would see it: believe the lie long enough to walk through it, and come back out with the truth in your hand. Nobody at this table has read those pages. Not even you. Not yet." {n}She looks at you as if you had done something at once very clever and very indecent.{/n}''',
      c("Continue", "humbled")),
    e("humbled", '''"I have a request, and it is not a point." {n}She lifts the glass off the pages.{/n}
"Teach me. Not the cipher. I do not want Areelu's secrets; I have read enough of what she did with them. Teach me to hold two things true for long enough to see what lies behind them. Once. So that I know what it feels like."''',
      c('"Close your eyes. Tell me something you know is true, and something you know is false."', "teach"),
      c('"No. You\'d stop being you."', "refuse")),
    e("teach", '''{n}She closes her eyes, and her whiskers tremble with the effort of keeping them closed.{/n}
"True: the Worldwound is a mistake. False: the Worldwound can be a door." {n}A long pause.{/n} "...Both. Both at once. It is a mistake, and it is a door, and the crossroads is what you get if you do not choose."
{n}Her eyes open, and they are wet, which you did not know they could be.{/n}
"That was horrible. Do it again next week."''',
      c("[Promise to.]", flags=(CONCEDED,))),
    e("refuse", '''"You think so little of me." {n}But she does not sound angry. She sounds, of all things, uncertain.{/n}
"Perhaps you are right. Perhaps the only reason I am any use at all is that I cannot do what you do." {n}She lays the glass back down over the pages, precisely.{/n}
"Keep reading ciphers for me, then. And tell me the truth about what they say. That, I can do. I will write it down."''',
      c("[Promise to.]")),
], requires=(POINT_ONE, CIPHER), forbids=(CIPHERED,), chapters=(5,))


# --- 9. "At worst, you'll die" (Chapters 4-5): the pivotal point. --------------------------------------------------
# PP6 (pacing, window only): she named the Commander the key at the Chapter 4 session (Council_Lexicon2/Cue_0040, Cue_0046), and
# the hall stays open after it (the members at rest, After_Council_Lexicon2), so the sitting opens that same night: [5] -> [4, 5].

KEY_CHOICES = (
    c('"You were honest. That\'s all I\'ve ever asked of you."', "forgive", flags=(KEY_FORGIVEN,)),
    c('"Then I\'ll remember it. Every time you vote."', "held", flags=(KEY_HELD,)),
    c('"Then you owe me. One vote, cast the way I tell you. Tonight."', "used", flags=(KEY_USED,),
      alignment=("Evil", 1)),
)

minutes(AT_WORST, "At worst", '"About the key. About naming me."', [
    nar("open", '''{n}She knew this sitting was coming. The scroll in front of her is already open at the session in question, and the line where she named you the key is there in her own upright hand, exactly as she spoke it.{/n}''',
        c("Continue", "lover", requires=(COMMITTED,)),
        c("Continue", "chair", forbids=(COMMITTED,))),
    e("chair", '''"You want to know whether I meant it." {n}She does not wait for you to answer.{/n}
"The Lexicon said a key was needed. A creature whose mortal nature is merged with the essence of another plane. The Worldwound is killing you slowly, and the energy of the good planes might offset it, or it might not. And so I proposed you, in front of the whole Council, as calmly as if I were reading out the agenda. I knew what it might cost you. I proposed you anyway."''',
      c("Continue", "truth")),
    e("lover", '''"You want to know whether I meant it." {n}Her voice is very even, the way it is when she is holding a session together by force of will.{/n}
"I proposed you as the key. In front of the whole Council, as if I were reading out the agenda. And I have voted aye on you, Commander, in this hall. Both are in my minutes, in the same hand." {n}Her claws are dug into the edge of the table. The wood has split under two of them.{/n}''',
      c("Continue", "truth")),
    e("truth", '''"I will not lie to you. It is the one thing I have never done, and I will not begin now to make this easier for either of us."
{n}She lifts her head.{/n} "Yes. I meant it. If the truth about the Worldwound had required your death, I would have minuted it, and grieved, and considered it well spent. That is what I am. I am the thing that would rather be right than kind."
{n}Her hands are flat on the table, and she does not take them away, and she does not look down.{/n} "The proposal was sound. I will not withdraw it. Tell me what you are going to do about it."''', *KEY_CHOICES),
    e("forgive", '''{n}She stares at you as if you had spoken in a language she did not know she understood.{/n}
"That is not a refutation." {n}Her voice has gone rough.{/n} "That is a pardon. I did not ask for one, and I do not need one: the proposal was sound, and I would make it again. You have pardoned me anyway, as if you had the standing to."
{n}She writes it down, and her hand shakes so badly the line runs downhill across the scroll. She does not rewrite it.{/n}
"You heard the proposal, on the record, and you stayed at the table." {n}She looks at the crooked line as if it were a wound that had closed wrong and would have to stay that way.{/n} "I will remember it for longer than you will live. I am sorry for that. I am not sorry for anything else."''',
      c("[Stay at the table.]")),
    e("held", '''"Yes. You should." {n}She says it at once, and it seems to steady her, as if she had been braced for something worse.{/n}
"Remember it every time I vote. Remember it when I am kind to you. It will make you a better judge of me than I am."
{n}She is quiet a moment, and when she speaks again it is very low.{/n} "I would not trust anyone who forgot it. Least of all myself."''',
      c("[Let the point stand.]")),
    e("used", '''{n}Her ears go flat. For a heartbeat you think she is going to reach across the table.{/n}
"You are trading on my guilt." {n}Very quietly.{/n} "That is what Alichino would do."
{n}She writes. You can read it upside down, and she lets you: "The chair agrees to vote once as the Commander instructs. The chair records that the Commander asked it, and why."{/n}
"There. It is minuted, Commander. Name the motion." {n}You name it on the spot: that the chair's minutes of this war record the key as a volunteer, and not as a sacrifice. She looks at the motion for a long time. Then she casts her vote where she sits, aloud, to an empty hall, "Aye", and writes it down, and her claws go through the paper beside the Commander's name.{/n} "Paid. And every time anyone opens this scroll, they will see exactly what you charged me."''',
      c("[Take the vote.]")),
], requires=(POINT_ONE, PROPOSED_KEY), forbids=(AT_WORST,), chapters=(4, 5))


# --- 10. Stay in your seats (Chapters 4-5): her temper. -------------------------------------------------------------
# PP6 (pacing, window only): the walk-out is the end of the Chapter 4 session (Council_Lexicon2/Cue_0048; Answer_0047 is that
# session's only way out), and the sitting reads as that session's aftermath (the chairs as they left them): [5] -> [4, 5].

minutes(SEATS, "Stay in your seats", '"They walked out on you."', [
    nar("open", '''{n}The chairs are not pushed in. They stand where the Council left them when it stood up and walked out over her protests: turned, scattered, one of them on its side. She has not righted it. She is sitting very straight at the head of the table, and the fur along her shoulders is standing up under her robe.{/n}''',
        c("Continue", "start")),
    e("start", '''"'Please, stay in your seats, the meeting is not...'" {n}She quotes herself, in a voice that would be steady if it were not so quiet.{/n}
"They left. While I was speaking. Shyka was laughing. Socothbenoth did not even look back." {n}Her claws are out. She is looking at them as if they belonged to someone else.{/n}
"I have been trying to run this Council on my own for a very long time, Commander. I did not know until they walked out how angry that has made me."''',
      c("[Right the fallen chair.]", "chair"),
      c('"Then stop running it on your own."', "alone")),
    e("chair", '''{n}You set the chair back on its legs and push it in to the table. She watches you do it, and the fur on her shoulders slowly lies down again.{/n}
"That is Chadali's chair. She will not know it fell." {n}A breath.{/n} "Thank you. It is absurd, how much better that is."''',
      c("Continue", "alone")),
    e("alone", '''"There is no one else." {n}Flatly.{/n} "Alichino wants to sell the result. Socothbenoth wants something he will not name. Cobblehoof wants whatever Abadar wants. Shyka wants a better story. Chadali wants everyone to be happy, which is not a position." {n}Her claws scrape the wood.{/n}
"If they betray this table, Commander, I do not know what I will do. No. That is a lie, and I do not tell them. I know exactly what I will do. I have seen it in my own hands tonight."''',
      c('"The day you draw that dagger at this table, you\'ve lost the argument for good."', "warn"),
      c('"Then make them stay. You\'re an empyreal lord, not a secretary."', "feed"),
      c('[Take her hand, claws and all.]', "hand")),
    e("warn", '''"Yes." {n}She looks at the dagger at her belt, and then back at you.{/n} "Force proves nothing. I said it to you. I have said it to Deskari, in my heart, a thousand times." {n}She sheathes her claws, one at a time.{/n}
"Minute it. In your hand, not mine: 'The Commander warned the chair.' If the day comes, I want to be able to read that someone did."''',
      c("[Write it.]", flags=(M + "temper_warned",))),
    e("feed", '''{n}Something moves behind her eyes that is not the chair at all. It is older, and it is a lion.{/n}
"You should not say that to me." {n}But she is smiling, very slightly, with her teeth.{/n} "Not everything that is true should be said at a table. I learned that when they walked out, and you have made me forget it already." {n}She does not sheathe the claws.{/n}
"Go. Before I ask you to say it again."''',
      c("[Go.]", flags=(M + "temper_fed",))),
    e("hand", '''{n}Her claws close around your fingers. They do not cut. It is a near thing, and you both know it, and neither of you lets go.{/n}
{n}At last:{/n} "Every one of them leaves after a session, and you come back. I have noticed. I notice everything; it is a fault." {n}The claws draw in, slowly, until it is only a hand.{/n}
"I will remember that. I am not writing it down. Some things are not for the record, and I did not know until now that I had any."''',
      c("[Stay a while.]")),
], requires=(POINT_ONE, WALKED_OUT), forbids=(SEATS,), chapters=(4, 5))


# --- 11. A serious matter (Chapter 5): essence extraction. ---------------------------------------------------------

minutes(ESSENCE, "A very serious matter", '"The cauldron. The essences."', [
    e("start", '''"Essence extraction is a very serious matter." {n}She says it carefully, and then drops the care.{/n}
"The Council has the cauldron now. The plan needs an essence from every plane the crossroads will touch. Mine is Nirvana's. Everyone at this table is prepared to sacrifice for such a good cause, of course. Everyone has also found an urgent reason why it should be someone else." {n}Her claws tap the scroll: once, twice.{/n}
"I have not. That is what I wanted to tell you. If no one else will, I will give mine."''',
      c('"Does it hurt?"', "hurt"),
      c('"You don\'t have to be the one who pays for everything."', "pays")),
    e("hurt", '''"Shyka says it is agonizing. Shyka says it cheerfully. I have not endured it myself." {n}She considers.{/n}
"I expect so. I am used to suffering for the sake of truth, Commander. Everyone who keeps honest minutes is. It is only a larger version of the same thing."''',
      c("Continue", "choice")),
    e("pays", '''"Someone always pays. The only question is whether they are told." {n}She rolls the quill between her fingers.{/n}
"Everyone else on this Council is hoping that someone else will pay without being told. I would rather pay knowingly. It is the only way I know to keep the record clean."''',
      c("Continue", "choice")),
    e("choice", '''"So. Tell me what you think I should do. I will not promise to do it. But I will listen, and I will write down what you said, and I will read it again when the time comes."''',
      c('"Nobody takes anything from you. Not the Council, not by force. I\'ll see to it."', "promised", flags=(PROMISED,)),
      c('"Give it. The crossroads is worth it, and you\'re the only one who\'ll keep your word."', "urged", flags=(URGED,)),
      c('"They\'ll betray you before it comes to that. When they do, don\'t draw your claws."', "warned", flags=(WARNED,))),
    e("promised", '''"You cannot promise that." {n}At once.{/n} "You do not command this Council. You barely attend it."
{n}And then, slower, with her claws flat on the scroll:{/n} "You have done several things at this table that could not be done. I will write it down as you said it. If you break it, the record will show only that you meant it." {n}She writes. It is a short line, and she takes a long time over it.{/n}''',
      c("[Watch her write it.]")),
    e("urged", '''"Yes." {n}Something in her shoulders loosens, as if a weight she had been carrying alone had been taken by the other end.{/n}
"Thank you. Everyone else has been telling me to wait, to vote, to consider it from all sides. You told me the truth: that someone has to, and it should be someone who means it." {n}She writes it down.{/n}
"If it is excruciating, Commander, I will tell you so. That is my side of the bargain."''',
      c("[Watch her write it.]")),
    e("warned", '''{n}Her ears flatten.{/n} "You think they will." {n}It is not a question.{/n}
"I think so too. I have thought so since they walked out. I have been hoping, which is not the same as thinking, and I have been letting the hope chair the session." {n}She looks at her own hands.{/n}
"If they betray this table, and I draw my claws anyway, it will be in the minutes that you told me not to. That is the worst punishment I know how to give myself. Write it."''',
      c("[Write it.]")),
], requires=(CONVENING, "council.cauldron_given"), forbids=(ESSENCE, ESSENCE_GIVEN, "council.walked_out"), chapters=(5,))


# --- 12. Adjourned: the night after the vote (heat up to the cut). --------------------------------------------------

minutes(ADJOURNED, "Adjourned", '"The chair called for an adjournment?"', [
    nar("open", '''{n}The hall is dark but for one lamp at the head of the table. She has sent the Council's servants away. The scroll of the second reading lies rolled and tied with an amethyst ribbon, set to one side, as far from the edge as the table allows.{/n}''',
        c("Continue", "start")),
    e("start", '''{n}She is standing by the lamp, and she has taken off the long robe of office; underneath is something much simpler, belted at the waist, and the dagger is not on it.{/n}
"I sent them all away an hour ago." {n}She does not come toward you. Her hands are at her sides, and they are not quite still.{/n} "I have been standing here since, trying to find a way to say this that I could defend afterwards. There is none. I want you. Tonight, in this hall, at my own table. Refute it."''',
      c('[Kiss her.]', "kiss"),
      c('"I\'ve got no refutation. I\'ve got a counter-motion."', "counter"),
      c('[Take the quill out of her hand.]', "quill")),
    e("quill", '''{n}She is holding the quill, of course. She did not notice she had picked it up. You take it from her fingers, slowly, and she lets it go, watching it leave her hand as if it were a part of her.{/n}
"I have never once let it go without finishing the line." {n}Her breath is short.{/n} "Put it somewhere I cannot reach it. Now."''',
      c("[Set it on the far end of the table, and come back.]", "kiss")),
    e("counter", '''"State it." {n}A growl, deep and immediate, and not at all displeased.{/n}
{n}You state it, at some length and in some detail, and she listens with her eyes half-closed and her claws curled into her own palms, and when you have finished she lets out a long breath that is almost a purr.{/n}
"Seconded. Carried. Come here."''',
      c("[Go to her.]", "kiss")),
    e("kiss", '''{n}Her mouth is warm and her breath is warmer, like standing too near a banked fire. She kisses the way she debates: thoroughly, without hurry, conceding nothing. The fur along her jaw is softer than it looks. Her hands close on your shoulders and the claws come out, not quite enough to cut, and she makes a low sound in her throat that you feel before you hear.{/n}
{n}Against your mouth:{/n} "Point of order. You are wearing a great deal of armour for a private session."''',
      c("Continue", "armour")),
    e("armour", '''{n}She undoes the buckles herself, one by one, with the same patient attention she gives to a long agenda, and every time a strap comes free she says its name, as if entering it in the record. You have never heard anyone make the word "vambrace" sound like that.{/n}
{n}When the last of it is on the floor she pushes you back until you are sitting on the edge of the Council's long table, among the inkwells, and stands between your knees, and looks at you in the lamplight, unhurried, the way she reads a motion twice before she votes.{/n}''',
      c("Continue", "look")),
    e("look", '''{n}For once she says nothing at all. Her amethyst eyes are very dark, and her breathing is the only sound in the hall. She pulls the belt of her gown loose with one claw, and it falls open, and she watches your face, not the gown, while it does.{/n}
"The floor has the question, Commander."''',
      c('[Pull her down to you by the open gown.]', "cut", flags=(M + "night",))),
    e("cut", '''{n}She comes the whole way: one knee on the table beside your hip and then the other, until she is astride you among the inkwells and her weight settles onto your thighs, and she pushes you flat on your back on the Council's table with one hand spread on your chest. She reaches past you, without taking her eyes from yours, and turns the lamp down to nothing; and in the last of its light you see her other hand move the second reading's scroll to safety at the far end of the table, even now, even then.{/n}''',
      c("[...]")),
], requires=(COMMITTED,), forbids=(ADJOURNED,), delay=12)


# --- 13. The record of the night. --------------------------------------------------------------------------------------

minutes(RECORD, "The record", '"You\'re writing already?"', [
    nar("open", '''{n}Morning, or what passes for it in the hall. She is sitting at the head of the table in yesterday's simple gown with the robe of office over her shoulders like a blanket, and she is writing. There is ink on her fingers, and on the table, and on you. Two inkwells did not survive the night.{/n}''',
        c("Continue", "start")),
    e("start", '''"I keep the minutes." {n}She does not look up.{/n} "Every session. That was a session. I adjourned it myself, at the end, and you seconded. Twice."
{n}She dips the quill.{/n} "I have written the date and the members present. I am now at the point where I must decide what was said. I would like your view, since you said a good deal of it."''',
      c('"Write it all. It was true."', "all"),
      c('"Leave it blank. Some things aren\'t for the record."', "blank"),
      c('[Read over her shoulder.]', "read")),
    e("read", '''{n}You lean over her shoulder. She lets you. In her upright hand, under the date: "Private session. Present: the chair; the Commander. Business: the motion carried at second reading, enacted." Beneath that, a space, and the quill hovering over it.{/n}
"You see my difficulty. 'Enacted' is true, but it is not the whole truth. And a partial truth is how every lie I have ever refuted began."''',
      c('"Then write it all."', "all"),
      c('"Then leave the rest blank."', "blank")),
    e("all", '''{n}She writes. It takes some time. She does not use the smaller hand she keeps for her private notes; she uses the upright one, the one the Council reads.{/n}
"There." {n}She sands it, and her whiskers are twitching.{/n} "The chair has never before written the word 'purred' in the minutes of this Council. The chair has now written it three times." {n}She rolls the scroll and ties it.{/n}
"If Alichino ever reads this, I will take it by force. I say so knowing exactly what I am saying."''',
      c("[Kiss the ink off her fingers.]", flags=(MINUTED,))),
    e("blank", '''{n}The quill stops. She simply looks at the empty space under the date.{/n}
{n}Slowly, as if arguing it with herself:{/n} "An omission is not a lie. The record shows that a session took place. It does not claim that nothing happened." {n}She writes, at last, in a small tight hand: "The chair was otherwise occupied."{/n}
"That is true. That is entirely true. I have never in my existence written something true in order to hide something." {n}She stares at it.{/n} "I do not know whether I have just learned something from you, or lost something."''',
      c("[Take her ink-stained hand.]", flags=(OMITTED,))),
], requires=(ADJOURNED,), forbids=(RECORD,), delay=6)


# --- 14. A standing item: after the war. ----------------------------------------------------------------------------

minutes(STANDING, "A standing item", '"You\'ve added something to the agenda."', [
    e("start", '''"A standing item. It will appear on every agenda from now on, until the chair or the floor removes it." {n}She turns the scroll so you can read it:{/n} "Item: what the Commander intends to do after the war."
"You do not have to answer tonight. Standing items are carried over. But you will have to answer eventually, because I will keep asking, and I do not get tired."''',
      c('"Honestly? I don\'t know if there is an after. The Worldwound might have me first."', "honest", requires=(PROPOSED_KEY,)),
      c('"Build your crossroads. Sit at your table. Argue with you until one of us concedes."', "table"),
      c('[Flirt] "Keep adjourning your meetings for you."', "tease"),
      c('"Honestly? I don\'t know if there is an after. The Worldwound might have me first."', "honest_early", forbids=(PROPOSED_KEY,))),
    e("honest_early", '''{n}She is quiet for a while. When she speaks it is without any of the chair in her voice at all.{/n}
"I know. I have read every report you have sent this Council, and some you did not send. I know what the Wound does to the ones who go nearest it." {n}She puts her hand flat over yours on the table.{/n}
"If the Worldwound has you, I will write down that it was a theft. I will write it down in every plane that keeps records, and I will keep writing it."''',
      c("Continue", "close")),
    e("honest", '''{n}She is quiet for a while. When she speaks it is without any of the chair in her voice at all.{/n}
"I know. I have read the Lexicon. I know what it says about keys and wounds and mortal bodies." {n}She puts her hand flat over yours on the table.{/n}
"I proposed you once as a sacrifice and called it a great deed. I will not do it again. If the Worldwound has you, I will write down that it was a theft. I will write it down in every plane that keeps records, and I will keep writing it."''',
      c("Continue", "close")),
    e("table", '''"Until one of us concedes." {n}She repeats it, and her chin lifts.{/n} "You realise that I have never conceded a motion. You realise I have forever, and you do not."
{n}She does not wait for an answer.{/n} "Then we will need a very long debate, and a very good record, so that when you are gone, the argument is not." {n}Her voice falters on "gone", and she refuses to let it, and goes on.{/n}
"I will keep the minutes. That is what I can do for you that no one else can."''',
      c("Continue", "close")),
    e("tease", '''"You will do no such thing." {n}And then, because it is her rule, and she keeps her rules:{/n} "...One meeting in three. And you ask the chair first."
{n}She taps the scroll twice with a claw, watching you. Then, more quietly:{/n} "That was not an answer, Commander. That was a very charming refusal to answer. The item stands."''',
      c('"...Build your crossroads. Sit at your table. Argue with you."', "table")),
    e("close", '''"The item is answered. For now." {n}She writes, and then does something you have never seen her do: she reads the item back aloud, in the voice she uses for the full Council, to a hall with nobody in it but you.{/n}
"It wants a second. Not for the chair. For the record. The Council will pretend one day that it never met, Commander. I know it will; I know them. I would like there to be one scroll somewhere that says otherwise, and says who seconded it."''',
      c("[Second it, aloud.]", flags=(AFTER_WAR,))),
], requires=(RECORD,), forbids=(STANDING,), delay=48)


# --- 15. The blank line: her soft no, and what waits after it. ------------------------------------------------------

minutes(BLANK, "The blank line", '"Is the motion still on the table?"', [
    nar("open", '''{n}The scroll of the second reading lies at the head of the table, unrolled, as if it had never been put away. The heading is still there: "Motion: that the chair and the Commander be..." The rest of the line is still blank. A weight sits on each corner to keep it flat: an inkwell, a Lexicon page, a paperweight shaped like a hippogriff, and the dagger.{/n}''',
        c("Continue", "start")),
    e("start", '''"It is on the table. It is not before the chair." {n}She is precise about the difference.{/n} "A motion declined may be moved once more, by the rules I wrote. Once. When the mover is ready to stand behind it."
"I have been looking at this line every day." {n}Her claws rest on the blank space and do not tap.{/n} "It is the only incomplete sentence in all of my minutes. It keeps me awake. That is not a reason to finish it."''',
      c('"Why did you decline?"', "why"),
      c('"I\'m not ready. But I haven\'t withdrawn it."', "wait")),
    e("why", '''"Because you tried to carry it by a trick, or because you asked me to vote for you. Either way, you tried to make it my motion instead of ours." {n}She says it without heat.{/n}
"I have been at a table for a very long time with people who wanted me to carry their motions for them. I did not want you to be one of them. I still do not."''',
      c("Continue", "wait")),
    e("wait", '''"Then it stays on the table." {n}She moves the dagger from the corner of the scroll back to her belt, which lets the corner curl, a little, toward her.{/n}
"At a third reading the chair hears the case against. You will not like who has to make it. I will not make it easier because I want you to win." {n}She meets your eyes.{/n} "I want you to win. I have never before wanted one side of a debate to win at my table. I do not like what that says about the chair, and I am not going to stop wanting it."''',
      c("[Leave the line blank a while longer.]")),
], requires=(DECLINED,), forbids=(BLANK, COMMITTED))


# --- Epilogue paragraphs on the committed page (eritrice.trickster.epilogue.we_did_meet). ---------------------------

EPILOGUE_PARAGRAPHS = [
    (KEY_FORGIVEN, "{n}In the volume for the year of Threshold there is a line that runs downhill across the page, as if written with a shaking hand. It records that the Commander was told the worst thing about the chair, on the record, and stayed at the table. She never rewrote it.{/n}"),
    (KEY_HELD, "{n}She asked the Commander, every year, whether the point about the key was still remembered. Every year the answer was yes, and every year she wrote \"Good\" beside it.{/n}"),
    (KEY_USED, "{n}One vote in all her minutes is marked as cast on instruction, with the Commander's name beside it and the reason in full. Scholars of Nirvana still argue about it. She never struck it out, and never explained it, and never voted that way again.{/n}"),
    (MINUTED, "{n}The minutes of one private session were sealed by the chair and marked \"not to be read by Alichino\". Alichino read them. He was not seen at the Council for a decade, and when he returned, he did not meet the chair's eyes.{/n}", ("council.epilogue_convened",)),
    (MINUTED, "{n}The minutes of one private session were sealed by the chair and marked \"not to be read by Alichino\". Alichino read them. For a decade afterwards he avoided every room she was in, and when at last he could not, he did not meet her eyes.{/n}", (), ("council.epilogue_convened",)),
    (OMITTED, "{n}Among thousands of pages of minutes there is one entry that reads only \"The chair was otherwise occupied.\" It is the only evasion ever found in her records, and she annotated it, in her smallest hand: \"Learned from the Commander. Not regretted.\"{/n}"),
    (AFTER_WAR, "{n}The standing item remained on every agenda for as long as there were agendas: what the Commander intends to do after the war. The answer was entered anew every session, in two hands. It never changed much.{/n}"),
    ((URGED, ESSENCE_GIVEN), "{n}She gave her essence to the cauldron, and afterwards she told the Commander that it had been excruciating, because she had promised to say so.{/n}"),
    (PROMISED, "{n}The Commander's promise that nobody would take anything from her by force was entered in her minutes the week the cauldron came. She kept the page folded down.{/n}"),
    (M + "temper_warned", "{n}In the Commander's hand, in the margin of a session that ended in overturned chairs: \"The Commander warned the chair.\" She read it more often than anyone knew.{/n}"),
]


def integrate(payload):
    """Bind this module's own reads, and give her committed page the standing debate's consequences."""
    for key, cues in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != cues:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["eritrice.trickster.epilogue.we_did_meet"]["Nodes"][0]
    for flag, text, *extra in EPILOGUE_PARAGRAPHS:
        req = flag if isinstance(flag, tuple) else (flag,)
        more = extra[0] if extra else ()
        forb = extra[1] if len(extra) > 1 else ()
        page.setdefault("Paragraphs", []).append(p(text, requires=req + tuple(more), forbids=forb))
