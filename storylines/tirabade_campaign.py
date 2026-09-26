"""Authored civilian leisure and its consequences after the shared Tirabade outing.

The yard, its adult players, and the bakery lesson are new fiction.
No native quest result, skill check, inventory reward, or romance exclusion is changed.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, owner, entry, nodes, requires=(), delay=48):
    SCENES.append(scene(id, title, owner, 3, entry, nodes,
                        requires=("three_outing.kept", "kept_terms", *requires),
                        forbids=("closed", "loss", "inhuman", "irabeth_away",
                                 "anevia_away", "last_watch"),
                        delay=delay, optional=True, Relationship="tirabade",
                        Areas=[DREZEN], Chapters=[3, 5],
                        ForbidOverrides={"last_watch": "three_progression.catchup_requested"}))


s("three_yard", "A game with no useful purpose", "Together",
  '"Anevia said you had found somewhere to spend an afternoon."', [
    n("start", "Irabeth", '''{n}Irabeth is holding a wooden ball. Anevia stands beside her with a narrow strip of red cloth draped over one shoulder.{/n}
"I found it," Irabeth says. "She has already begun inspecting the prize."
"Wanted to know what we were riskin' our reputations for. Good cloth. Could patch a very small catastrophe."
{n}Irabeth takes the strip from her wife and lays it on the counter behind them.{/n}
"We have not entered anything yet."
{n}Beyond the counter, nine wooden pins stand at the end of a lane made from old planks. A woman with gray braids finishes sweeping the approach and rests her broom against the wall.{/n}
"Tessa," she introduces herself. "I keep the yard. Afternoon fee pays for the lane, not advice. Advice is free and generally ignored."''',
      c('"What are the rules?"', "rules"),
      c('[Arrange to join them another afternoon.]', abort=True)),
    n("rules", "Narrator", '''{n}Tessa puts a ball on the counter. It is smaller than the one Irabeth is holding.{/n}
{n}"Choose a weight you can roll comfortably. Three to a team. One roll each, pins reset between rolls. Pins down are points. Feet behind the chalk until the ball leaves your hand. The side boards count as part of the lane, so you can bounce off them if you think it helps."{/n}
{n}She points to the low fence behind the pins.{/n}
{n}"Roll, don't throw. That fence belongs to my neighbor, and she has heard every apology I know."{/n}
{n}Anevia turns a ball between her palms. Irabeth has not put hers down.{/n}
"You have played before," Anevia says.
"Years ago. Badly. I would like to discover whether I still do."
"Always admired your ambition, Beth."''',
      c('"Show us how you would begin, Irabeth."', "beth"),
      c('"Anevia, you are looking at those boards as if you have an idea."', "anevia")),
    n("beth", "Irabeth", '''{n}Irabeth steps to the chalk, leaving the ball on the counter while she tries the movement empty-handed.{/n}
"I used to put everything into the release. It was impressive until it reached the pins."
{n}She retrieves the ball and rolls it. It strikes the front pin, knocks down four more, and stops against the fence.{/n}
"Five. An improvement."
{n}Anevia waits until Tessa has cleared the lane before going to examine the fallen pins.{/n}
"You look pleased."
"I am pleased. Were you expecting an apology for the other four?"
{n}Anevia looks back over her shoulder, grinning.{/n}
"Might've prepared one. Didn't want you disappointed."
{n}Irabeth holds out the smaller ball to you.{/n}
"Keep your eyes on the place you want it to go. And leave yourself room to stop."''',
      c('[Practice the straight roll with her.]', "straight", flags=("three_yard.straight",))),
    n("straight", "Narrator", '''{n}Your first roll wanders toward the side. Irabeth follows it with her whole body, leaning until Anevia catches the back of her coat.{/n}
{n}"Won't help, love. I've tried."{/n}
{n}The second attempt knocks down three pins. Irabeth asks where you aimed, then crouches at the start of the lane to look along the same line.{/n}
{n}"That dark knot. Try a little to its left. The board rises there."{/n}
{n}Anevia takes her turn while the pins are reset. She banks her ball off the right-hand board and strikes a pin near the back.{/n}
{n}"One," Tessa announces.{/n}
{n}"A very difficult one," Anevia replies.{/n}''', c('[Give Anevia another ball.]', "together")),
    n("anevia", "Anevia", '''"There's a bend near the far end. Might as well make use of it."
{n}She rolls the ball toward the right-hand board. It rebounds much sooner than she intended and knocks over one pin.{/n}
"There. Left the rest for you."
{n}Irabeth laughs before she can make it polite. Anevia turns toward her, one hand on her hip.{/n}
"Enjoyin' yourself?"
"Very much."
"Good. That was the expensive part of the trick."
{n}She offers you the next ball and points out the patched section of the board.{/n}
"A little farther along. Unless you're fond of that one pin."''',
      c('[Try her banked roll.]', "bank", flags=("three_yard.bank",))),
    n("bank", "Narrator", '''{n}Your ball reaches the patch and turns across the lane. Two pins fall. A third rocks, considers the matter, and remains standing.{/n}
{n}"Stubborn little thing," Anevia says.{/n}
{n}Irabeth takes her own turn with a straight roll. Five pins fall. She looks from them to Anevia, plainly waiting.{/n}
{n}"Five ordinary pins," Anevia says. "Anybody could knock those down."{/n}
{n}"You are welcome to demonstrate."{/n}
{n}Anevia comes back from the counter with another ball and nudges your shoulder with hers.{/n}
{n}"She's goin' to be unbearable. We should've taken her somewhere dull."{/n}''', c('[Make room for her next attempt.]', "together")),
    n("together", "Irabeth", '''{n}After several turns, Tessa carries over a slate with three names already written on it.{/n}
"There is a match when enough people want one," Tessa says. "Two teams of three. Olva, Nessa, and Perrin usually come together. They would be pleased to have opponents."
{n}Irabeth's hand closes around the ball she has just retrieved.{/n}
"I would like that."
"Would you?" Anevia asks. "Can't imagine what gave her that idea, Tessa."
{n}Irabeth puts the ball down and looks at her wife.{/n}
"Would you? I want to play with you. I do not want to drag you through an afternoon you are only tolerating."
{n}Anevia's reply comes without the expected joke.{/n}
"I like seein' what you do when you want to win something small. Yes. I'll play."
{n}She turns to you.{/n}
"Your decision. She'll recruit you very politely if you give her time."''',
      c('"I want to be on your team. I also want you to let me make my own mistakes."', "mistakes", flags=("three_yard.own_roll",)),
      c('"I want both of you arguing over how to improve my score."', "coaches", flags=("three_yard.coaches",))),
    n("mistakes", "Irabeth", '''"Fair. I will ask before offering advice."
{n}Anevia opens her mouth. Irabeth looks at her.{/n}
"Both of us will ask."
"Was goin' to agree. With an impressive amount of dignity."
{n}Irabeth writes all three names across Tessa's slate, leaving a column beneath each for the scores.{/n}
"There. You can blame your own score on the boards. We shall have to find something else."''', c('[Choose a day for the match together.]', "date")),
    n("coaches", "Anevia", '''"Dangerous offer. She'll have diagrams."
"You have already scratched one on the counter."
{n}Anevia covers the mark with her palm. Tessa gives her a cloth.{/n}
"It'll come off," Anevia assures her.
"I know. You are going to take it off."
{n}While Anevia rubs at the mark, Irabeth writes the three names on the slate. She shows it to you both before returning it.{/n}
"If the advice becomes tiresome, say so. I intend to enjoy having you there."''', c('[Choose a day for the match together.]', "date")),
    n("date", "Narrator", '''{n}Tessa records the afternoon you agree upon. Anevia pays for today's lane and retrieves her coat. Irabeth returns both balls to their shelf.{/n}
{n}At the gate, Anevia draws her wife down for a kiss. Irabeth looks surprised, then puts a hand at Anevia's waist and takes her time answering it.{/n}
{n}"That was for the five ordinary pins," Anevia tells her.{/n}
{n}Irabeth looks at you, her smile still unguarded.{/n}
{n}"Apparently I should practice."{/n}''',
      c('[Offer them your arms for the walk back.]', flags=("three_yard.booked",))),
])


s("three_match", "The point they could not agree on", "Together",
  '"Tessa is expecting our team. Are you ready?"', [
    n("start", "Narrator", '''{n}Olva, Nessa, and Perrin have arrived before you. Tessa introduces them as a candlemaker, a cook, and a cooper, respectively. The two women wait while Perrin, a broad-shouldered man with gray in his beard, tells you that he remembers when the sign above the gate advertised turnips.{/n}
{n}Olva shakes Irabeth's hand, recognizes you, and gives Tessa an anxious glance.{/n}
{n}"Same line? Same balls?" she asks.{/n}
{n}"Same fee, too," Tessa says. "Nobody is campaigning in my yard."{/n}
{n}Anevia picks up a ball and turns the worst dent toward you.{/n}
{n}"This one's ours. Hasn't got any ambitions."{/n}''',
      c('[Take your place with the team.]', "rounds"),
      c('[Explain that you cannot play today and ask to rearrange the match.]', abort=True)),
    n("rounds", "Narrator", '''{n}The first rounds go quickly. Nessa rolls left-handed and bowls so slowly that the ball seems unlikely to reach the pins, then scatters seven of them. Anevia watches the next attempt without pretending to look elsewhere.{/n}
{n}Perrin counts every score aloud for Tessa's slate. Irabeth checks her own total, catches Olva checking hers, and turns the slate so they can both see.{/n}
{n}By the last round, you are all laughing at Perrin's elaborate preparations. They do not prevent him from knocking down eight.{/n}
{n}The other team finishes with twenty points for this round. Tessa announces that the teams were level beforehand, so twenty-one will win the match. Irabeth rolls first and scores seven.{/n}
{n}She comes back to stand beside Anevia, rubbing her palms together.{/n}
{n}"Your turn," she tells you.{/n}''',
      c('[Take a moment to choose your line without advice.]', "alone", requires=("three_yard.own_roll",)),
      c('[Ask your two coaches what they suggest.]', "advice", requires=("three_yard.coaches",))),
    n("alone", "Anevia", '''{n}Anevia starts to point, remembers, and scratches her ear instead. Irabeth catches the movement. Her lips twitch.{/n}
"Don't," Anevia whispers.
"I said nothing."
"Very loud nothing."
{n}They step back together and let you study the lane. When you turn toward them, neither is looking at the score.{/n}''', c('[Choose the roll you practiced.]', "technique")),
    n("advice", "Irabeth", '''"The left side is running true today. Use the knot as your marker."
"Or the patch," Anevia adds. "If you want to make it interesting."
"We are already interested."
{n}Anevia touches her wife's wrist with two fingers.{/n}
"You have to admit it looked good when it worked."
"I will admit that when it works twice."
{n}They both look to you. Irabeth lifts her hands, leaving the choice with you.{/n}''', c('[Choose the roll you practiced.]', "technique")),
    n("technique", "Narrator", '''{n}Tessa steps away from the pins and signals that the lane is clear.{/n}''',
      c('[Aim to the left of the knot and roll straight.]', "straight", requires=("three_yard.straight",)),
      c('[Use the patched board for a banked roll.]', "bank", requires=("three_yard.bank",))),
    n("straight", "Narrator", '''{n}The ball follows the line Irabeth helped you find. Six pins go down. She lets out a sharp breath and reaches for your hand before you have quite turned around.{/n}
{n}"Six. That gives us thirteen."{/n}
{n}"And leaves me a perfectly reasonable eight," Anevia says. "Could've knocked down another one, if you wanted to be considerate."{/n}
{n}She squeezes your shoulder as she passes.{/n}''', c('[Watch Anevia take the last roll.]', "last")),
    n("bank", "Narrator", '''{n}Your ball strikes the patch, turns across the lane, and brings down six pins. Anevia raises both hands.{/n}
{n}"Twice!"{/n}
{n}"Six points," Irabeth says. "I am not counting demonstrations."{/n}
{n}She takes your hand and squeezes it. Anevia retrieves the remaining ball from the counter.{/n}
{n}"Thirteen. Eight for me, then. Easy. Probably."{/n}''', c('[Watch Anevia take the last roll.]', "last")),
    n("last", "Narrator", '''{n}Anevia pauses behind the chalk. Her next movement is quick and low, the ball running straight down the middle. Eight pins fall.{/n}
{n}Irabeth gives a shout that startles Perrin. You turn toward her just as Olva raises a hand.{/n}
{n}"Her foot. I thought it touched the line."{/n}
{n}Anevia looks down. The chalk is scuffed where several people have planted their feet. Tessa was watching the pins; you were, too.{/n}
{n}"I stayed behind it," Anevia says.{/n}
{n}"I think you meant to," Olva replies. "I don't think you did."{/n}
{n}Tessa walks to the mark, examines it, and straightens.{/n}
{n}"I didn't see a foul. I can't strike off points because somebody might have committed one. The score stands unless both teams agree to a fresh roll."{/n}''', c('[Hear what your teammates want.]', "decision")),
    n("decision", "Irabeth", '''"I would prefer another roll."
{n}Anevia looks at her wife.{/n}
"I didn't cross it."
"I heard you. I want us to finish with a score everyone can accept."
"Olva can accept the keeper's decision. That's what she's here for."
{n}Olva starts to answer, but Nessa draws her a few paces away. Irabeth lowers her voice.{/n}
"People already wonder whether they can play properly against us."
"Then let 'em lose properly against us. You don't fix that by handin' back every point somebody dislikes."
{n}Anevia turns the ball in her hands. Irabeth looks at you.{/n}
"We do not agree. I could keep the score, though I would dislike it."
"And I can roll again," Anevia says. "Won't make me agree I fouled."
{n}Tessa waits at the counter for the team's answer.{/n}''',
      c('"Keep the keeper\'s decision. We did not see a foul, and we should not invent one."', "stand", flags=("three_match.stood",)),
      c('"Offer a fresh roll without admitting a foul. Let us settle this on the lane."', "replay", flags=("three_match.replayed",))),
    n("stand", "Narrator", '''{n}Irabeth nods once. Anevia returns the ball to its shelf.{/n}
{n}"We will keep the score," Irabeth tells Tessa. "Your decision stands."{/n}
{n}Olva's expression closes. She shakes your hands, but when Nessa suggests a drink together she says she has work waiting. Perrin follows her. Nessa stays long enough to tell Anevia that the last roll was well aimed, whatever happened at her feet.{/n}
{n}Tessa gives you the red strip that serves as the yard's pennant. Irabeth folds it. Anevia watches her hands.{/n}
{n}"You wanted to win," she says quietly.{/n}
{n}"I did."{/n}
{n}Irabeth does not add anything. She puts the pennant in her coat pocket, and the three of you leave together.{/n}''',
      c('[Walk home with them, letting the argument rest for now.]', flags=("three_match.finished", "three_match.pennant",))),
    n("replay", "Narrator", '''{n}Anevia asks Tessa to draw the line again. Olva agrees to accept the new roll as the score. Nessa takes a place beside the chalk where both teams can see her watching.{/n}
{n}This time Anevia leaves an exaggerated gap before the mark. Her ball drifts right and knocks down six. Nessa immediately says that her feet were clear.{/n}
{n}"Nineteen," Tessa announces. "Olva's team wins."{/n}
{n}Olva looks relieved, then catches Anevia watching her and offers a hand. Anevia shakes it.{/n}
{n}"I'll be askin' for another match," she says.{/n}
{n}"We will be here," Nessa replies, before Olva can answer.{/n}
{n}Irabeth helps reset the pins for the next players. When she comes back, Anevia has returned the balls and collected their coats. She gives Irabeth hers without a joke.{/n}''',
      c('[Walk home with them, letting the argument rest for now.]', flags=("three_match.finished",))),
], requires=("three_yard.booked",))


s("three_beth_score", "What she wanted to win", "Irabeth",
  '"You were quiet after the match. May I ask about it?"', [
    n("start", "Irabeth", '''{n}Irabeth is unfastening the laces of a practice guard. She lays it beside its mate and makes room for you on the bench.{/n}
"Yes. I wanted to speak to you, too."
{n}She rubs the red mark the guard has left on her wrist.{/n}
"Anevia and I talked after you went home. She thinks I would have asked anyone on our team to roll again. She is right. It did not stop her feeling that I had been particularly quick to ask her."
{n}Irabeth looks toward you.{/n}
"I told her I believed her. Then I tried to explain it three more ways, which did not improve the evening."''',
      c('"Did you believe she kept her foot behind the line?"', "believe"),
      c('"You seemed worried that the other team was afraid of us."', "rank"),
      c('[Ask to return when you can give her your attention.]', abort=True)),
    n("believe", "Irabeth", '''"I believed she meant to. I did not see her foot. Neither did she."
{n}She turns the guard over to loosen a twisted lace.{/n}
"There. That is the sentence I should have used. It sounds less generous than declaring complete faith in somebody, but at least it describes what I know."
{n}She leaves the lace loose.{/n}
"I also wanted nobody to have a reason to say we won because of who we are. That part was mine. I put it into her hand and asked her to roll it down a lane."''',
      c('"You can tell her that part without asking her to change her account."', "hers")),
    n("rank", "Irabeth", '''"I saw Olva look at you before she looked at the line. I have been on the other side of that glance. Wondering whether an ordinary objection will sound like insolence."
{n}She sets the guard down.{/n}
"Then she did object. Perhaps I should have given her more credit for it. She did not need me to imagine every answer on her behalf."
{n}Irabeth looks at you directly.{/n}
"I wanted an afternoon where I could be good at something without anybody needing me to be. I was enjoying it so much that I tried to protect it from becoming untidy."''',
      c('"It was untidy. You still played well."', "hers")),
    n("hers", "Irabeth", '''"I know."
{n}The answer is quiet, but immediate.{/n}
"I would like to enjoy that without first apologizing for how much I cared about seven wooden pins. I have cared less about larger things, on days when I was tired."
{n}She notices you looking at her and gives a brief smile.{/n}
"That was not an invitation to tell me how much the larger things need me."
{n}Irabeth reaches for your hand, palm open on the bench.{/n}
"What did you want from the afternoon? I have been so occupied with the ending that I have scarcely asked."''',
      c('"I liked being useful to a team without anybody depending on us to survive."', "team", flags=("three_beth_score.team",)),
      c('"I wanted you to notice me doing something well. I enjoyed your hand finding mine."', "noticed", flags=("three_beth_score.noticed",))),
    n("team", "Irabeth", '''"Then we ought to play again. That much was real."
{n}She takes your offered hand and presses her thumb against your knuckles.{/n}
"I keep discovering that I would like another turn. I used to think leisure was what happened when nothing remained to be done. An impossible condition."
{n}A smile spreads slowly across her face.{/n}
"And I want to see whether Nessa can make that ridiculous slow roll work twice. She looks so certain of it. I would like to be the person who makes her look less certain."''', c('[Tell her you want another turn beside her.]', "outcome")),
    n("noticed", "Irabeth", '''"I noticed."
{n}She takes your hand and draws it onto her knee. Her fingers close over it.{/n}
"When you looked back at us, I wanted to pull you straight off the lane. I remembered Anevia still needed to play."
{n}Her ears redden. This time she does not look away.{/n}
"I also liked that she saw me want to. I have spent enough time trying to make every feeling occur in a separate room."
{n}She lets your hand rest against her for a moment before loosening her grip.{/n}
"You were very distracting for someone asking me to watch a game."''', c('[Enjoy her attention without hurrying her.]', "outcome")),
    n("outcome", "Narrator", '''{n}Irabeth puts the guards together and slides them beneath the bench. Her hand remains near yours.{/n}''',
      c('"What will you do with the pennant?"', "pennant", requires=("three_match.pennant",)),
      c('"Will you ask Anevia about the return match?"', "return_match", forbids=("three_match.pennant",))),
    n("pennant", "Irabeth", '''"Bring it back when we play again. That is how the yard uses it. The winning team keeps it until another team wins."
{n}She looks almost defiant.{/n}
"I have not hidden it. Anevia hung it on the back of a chair this morning. She said we might as well enjoy our scandalous wealth."
{n}Irabeth laughs, then grows quieter.{/n}
"I am glad she did. I had made it seem as though keeping the score meant being ashamed of the whole afternoon. It did not."''', c('[Make room for a second afternoon.]', "finish")),
    n("return_match", "Irabeth", '''"She has already asked me. I said yes. Then she told me that next time, if I want her advice about a roll, I should ask her before inventing a safer one."
{n}Irabeth gives a reluctant laugh.{/n}
"She can be very precise when she is annoyed. I suspect you have noticed."
{n}Her smile softens.{/n}
"She did take my hand afterward. That helped more than a fourth explanation would have."''', c('[Make room for a second afternoon.]', "finish")),
    n("finish", "Irabeth", '''"I will tell her we spoke. About my part in it. The rest is yours to share."
{n}She stands, leaving the guards where they are.{/n}
"Before you go, may I kiss you?"
{n}There is no room in her expression for a guess about what you ought to answer.{/n}''',
      c('[Stand and kiss her.]', "kiss", flags=("three_beth_score.kissed",)),
      c('[Take her hand and ask her to walk with you instead.]', "walk")),
    n("kiss", "Narrator", '''{n}Irabeth's hand settles against your back. Her kiss begins carefully, then becomes less careful when you lean closer. She laughs softly against your mouth before letting you go.{/n}
{n}"I had been considering that since the lane."{/n}
{n}She picks up the guards and leaves with you, looking pleased enough that you need not ask whether the interruption was welcome.{/n}''', c('[Walk back together.]', flags=("three_beth_score.heard",))),
    n("walk", "Narrator", '''{n}She threads her fingers through yours and picks up the guards with her free hand. At the door she pauses to let you choose the direction.{/n}
{n}"I have a little time," she says. "Use it well. That is advice, not a command."{/n}''', c('[Choose a quieter way back.]', flags=("three_beth_score.heard",))),
], requires=("three_match.finished",), delay=24)


s("three_anevia_flour", "The loaf she wanted to make", "Anevia",
  '"You said you would be at the bakery this afternoon."', [
    n("start", "Anevia", '''{n}Anevia has flour on her sleeve and a small, hard lump of dough on the board before her. An older woman wearing a blue apron takes one look at it and pours a little water into a cup.{/n}
"Dalia," Anevia tells you. "She agreed to teach me. Thought she ought to know what she was gettin' into, so I paid first."
{n}Dalia sets the cup beside the board.{/n}
"You paid for flour and oven space. I offered to teach. At present I am trying to persuade you to use the water."
"Makes it stick."
"Yes."
{n}Anevia looks at you as if hoping you might produce a more useful answer.{/n}
"She's been right about everything so far. Very difficult to work with."''',
      c('[Wash your hands at the basin and join her.]', "dough"),
      c('[Ask to visit when she has finished the lesson.]', abort=True)),
    n("dough", "Narrator", '''{n}Dalia has already baked the day's orders. She shows Anevia how to wet her fingers and fold the dough, then leaves you both at the rear worktable while she measures flour for tomorrow.{/n}
{n}Anevia folds, presses, and immediately reaches for more flour. You cover the flour bowl with your hand.{/n}
{n}"Traitor."{/n}
{n}She tries the fold again. Dough clings to her palm. She lifts her hand, stretching a long pale strand between her fingers and the board.{/n}
{n}"I've escaped worse things."{/n}
{n}Dalia calls from the other end of the room.{/n}
{n}"Do not escape it. Fold it."{/n}
{n}Anevia looks so affronted that you laugh. After a moment she does, too.{/n}''',
      c('"You really want to learn this."', "want"),
      c('"What do you hope this lesson will do for your bread?"', "imagined")),
    n("want", "Anevia", '''"Yes. Had the idea for ages. Kept findin' reasons not to ask somebody to watch me get it wrong. One day I'll have an oven of my own. Until then, Dalia's toleratin' me."
{n}She folds the dough as Dalia showed her. This time it releases from the board without tearing.{/n}
"Figured I'd get somebody to explain it, understand the trick, skip straight to bein' tolerable. Turns out the trick's mostly doin' the part you aren't good at yet."
{n}She glances toward the flour shelves, checking that Dalia is occupied.{/n}
"Don't tell her I said that. She'll make me embroider it on an apron."''',
      c('[Stay beside her while she works.]', "match"),
      c('"Will Beth still get the worst bit of crust?"', "old_crust", requires=("a_errand",))),
    n("imagined", "Anevia", '''"Round. Brown. Recognizable from a safe distance."
{n}She gives the dough another fold.{/n}
"I'd like to put a loaf down in front of Beth without explainin' which bit to avoid. Let her break it open while I pretend I'm not watchin' her face."
{n}Anevia looks at you, her hands still working.{/n}
"I suppose I've spoiled the surprise by invitin' you to witness the evidence. You can still be convincingly impressed later."''', c('"I will give the bread a fair hearing."', "match")),
    n("old_crust", "Anevia", '''"She'll try. You've seen how she operates. Gets hold of the evidence before anybody can stop her."
{n}Anevia folds the dough, then presses a sticky thumb against the board.{/n}
"This time I'm askin' Dalia when it's done. Beth can save somebody else from their own cookin'."
"And if she says she likes it crisp?"
"Then she can have the end. After I've tried it."''', c('[Help her keep the dough from sticking.]', "match")),
    n("match", "Anevia", '''{n}She rolls the dough into a loose ball and puts it beneath a damp cloth. Dalia inspects it, nods, and tells her to leave it alone until it has risen. Anevia wipes the board rather more thoroughly than it needs.{/n}
"Used to put all this after the war. My own kitchen, Beth comin' downstairs because of the smell, nobody expectin' either of us to report anywhere. Still want that morning."
{n}She looks at the covered dough.{/n}
"Thought I might do a little practicin' for it."
"I wanted to be good at the game, too. If you're wonderin'."
{n}She keeps her voice low enough that Dalia can continue weighing flour without becoming part of the conversation.{/n}
"Beth looked so pleased when I picked up the last ball. I liked havin' her wait for something I could do. You, too. Then we were arguin' about my foot."
{n}She drops the cloth into the basin.{/n}''',
      c('[Ask how she feels about keeping the score.]', "stood", requires=("three_match.stood",)),
      c('[Ask how she feels about the second roll.]', "replayed", requires=("three_match.replayed",))),
    n("stood", "Anevia", '''"Glad we kept it. Still am."
{n}She leans against the worktable.{/n}
"Wish Olva had stayed. Could've told me I was a nuisance over a drink. I would've agreed with half of it."
{n}Anevia scratches a speck of dried dough from her sleeve.{/n}
"Beth thinks bein' fair ought to help everybody breathe easier. Sometimes it just gives 'em a decision to dislike. She knows that when she's workin'. I think she wanted an afternoon off from knowin' it."
{n}Her mouth softens.{/n}
"So did I, probably."''', c('[Let her continue.]', "motive")),
    n("replayed", "Anevia", '''"Didn't enjoy losin'. You may have detected that."
{n}She tries to rub the flour off her sleeve, then gives up.{/n}
"I agreed to the roll. You didn't put the ball in my hand. I don't get to pretend otherwise because six pins looked miserable beside the eight I'd already knocked down."
{n}She looks toward the covered dough.{/n}
"What stung was Beth lookin' relieved before I took the second shot. As if the difficult part was over. It was about to be mine."
{n}Anevia turns back to you.{/n}
"I told her. She heard me. Didn't stop wantin' the replay. We managed to leave it there."''', c('[Let her continue.]', "motive")),
    n("motive", "Anevia", '''"I don't want you adjudicatin' our marriage. Beth isn't sendin' you to collect an apology, is she?"
{n}You shake your head. Anevia nods, accepting it.{/n}
"Good. Then tell me what you thought. About your choice. I know what we both said while you were tryin' to make it."''',
      c('"I would choose the same again. I also want to understand what it cost you."', "same", flags=("three_anevia_flour.same",)),
      c('"I was trying to end the argument quickly. I should have taken more time."', "quick", flags=("three_anevia_flour.quick",)),
      c('"I thought keeping the ruling was enough. Now I think a replay might have been worth the risk of losing."', "reconsider_stood", requires=("three_match.stood",), flags=("three_anevia_flour.reconsidered",)),
      c('"I thought a replay would settle it. Now I think we should have let the keeper\'s ruling stand."', "reconsider_replayed", requires=("three_match.replayed",), flags=("three_anevia_flour.reconsidered",))),
    n("reconsider_stood", "Anevia", '''"Maybe. I still wanted my eight pins."
{n}She rubs a trace of flour between her fingers.{/n}
"If you'd said that then, I'd have taken the roll. Might've complained afterward, too. You don't have to prove you made the only possible choice to sit here with me."
{n}She nudges your foot with hers beneath the table.{/n}
"Just don't tell Olva I admitted there was another one before I've had my drink."''', c('[Stay beside her while the dough rises.]', "shape")),
    n("reconsider_replayed", "Anevia", '''"I would've liked that answer at the time."
{n}She says it without a smile, then rests her shoulder against yours.{/n}
"But I agreed to the replay. Don't take that bit away from me because you've changed your mind. I got a say. I used it."
"I remember."
"Good. Next time we might both do it differently. Still want you on my team."''', c('[Lean against her until Dalia returns.]', "shape")),
    n("same", "Anevia", '''"Then you can ask me without lookin' like you expect a sentence."
{n}She reaches for your hand, checks the flour on her fingers, and washes them before taking it.{/n}
"I wanted you to think I was brilliant. Instead you got the part where I keep an argument goin' after everyone else would like a nice ending."
{n}Her thumb traces the side of your hand.{/n}
"You'll get more of both. I hope you're still interested."''', c('"I am. Including another attempt at the brilliant part."', "shape")),
    n("quick", "Anevia", '''"We weren't exactly givin' you a quiet place to think."
{n}She washes her hands and dries them before returning to your side.{/n}
"Next time, tell us to stop talkin' for a moment. I'll complain. Beth will apologize, then explain why she was explainin'. Eventually we'll both stop."
{n}She rests a hand at your waist for a brief moment.{/n}
"I can wait for your answer. I'd rather get yours than the one you think will get us out the gate."''', c('[Promise to take the time you need.]', "shape")),
    n("shape", "Narrator", '''{n}Dalia returns to check the dough. It has risen. Anevia looks absurdly proud of something she was instructed not to touch.{/n}
{n}"Now shape it," Dalia says.{/n}
{n}Anevia folds the edges under as shown. A seam opens. She closes it, presses too hard, and looks toward the flour bowl.{/n}
{n}"Don't," you and Dalia say together.{/n}
{n}"Very well. I know when I'm outnumbered."{/n}
{n}Dalia places the shaped loaf near the warm oven to rise again. While you wait, she gives you both a bowl of cooled rolls to split for tomorrow's breadcrumbs. Anevia steals a small piece and offers half to you. Dalia sees and tells her which ones have seeds.{/n}''', c('[Help with the rolls while the loaf rises.]', "baked")),
    n("baked", "Anevia", '''{n}By the time Dalia takes the loaf from the oven, the bread smells better than Anevia had dared to predict. One side has split along the seam. She crouches beside the cooling rack to inspect it.{/n}
"Looks like it tried to leave. Can't blame it."
"Leave it on the rack," Dalia says. "You can take it when it has cooled."
{n}Anevia waits with you at the open back door. Her shoulder rests against yours.{/n}
"I'm tellin' Beth you saw all of it. Then she can't give you a better account than I deserve."
{n}She looks up at you.{/n}
"Will you come when I give it to her? I want both of you there for the verdict."''',
      c('"Yes. I want to try the loaf you made."', "leave")),
    n("leave", "Narrator", '''{n}Dalia finally wraps the loaf in a clean cloth Anevia brought with her. Anevia pays for another lesson, asks when Dalia has room, and writes down the answer herself.{/n}
{n}Outside, she carries the warm bundle against her coat. You open the gate for her.{/n}
{n}"That went better than my first lock," she says. "Nobody threatened to cut my fingers off."{/n}
{n}She sees your expression and nudges you gently with her elbow.{/n}
{n}"This was a good afternoon. Let me have the terrible joke."{/n}''',
      c('[Walk with her to find Irabeth and share the loaf.]', "share")),
    n("share", "Irabeth", '''{n}Irabeth is at their rooms when you arrive. Anevia puts the bundle on the table, unwraps it, and immediately turns the split side toward her wife.{/n}
"That's the seam. Didn't quite hold."
{n}Irabeth fetches a knife and three plates. She cuts through the center and gives each of you a piece before tasting her own.{/n}
"It is good."
"You can say if it's heavy."
"It is a little heavy. It is also good."
{n}Anevia breaks her piece open and studies it. You take a bite. The middle is cooked through, the crust tougher than she had hoped.{/n}
"Next one needs a little more water," she says.
{n}Irabeth puts down her plate and takes Anevia's flour-marked sleeve gently between her fingers.{/n}
"Then I would like to try the next one. You have flour here."
"Have it everywhere."
"I had noticed."
{n}She kisses her wife. Anevia leaves the loaf alone long enough to answer properly, then turns toward you, smiling.{/n}
"All right. Now you can tell her about the dough tryin' to escape."''',
      c('[Tell Irabeth about the lesson while you share the bread.]', flags=("three_anevia_flour.baked",))),
], requires=("three_match.finished",), delay=24)


s("three_return_game", "A line everyone can see", "Together",
  '"Have you arranged our return match?"', [
    n("start", "Anevia", '''"Tessa has. Nessa asked her before we did."
{n}Anevia hands you the keeper's note. It names an afternoon, then adds a request: arrive early enough to help choose a clearer place for the chalk.{/n}
"No fee for offerin' opinions. She's learnin' our weaknesses."
{n}Irabeth has brought a short straightedge.{/n}
"The line crossed a join between two boards. We could move it back a little, onto one surface."
"And now you know what she's been thinkin' about."
{n}Irabeth looks at her wife.{/n}
"Among other things."
{n}The look Anevia gives her in return has nothing to do with the lane.{/n}''',
      c('[Go to the yard together.]', "arrival"),
      c('[Ask them to arrange a later match.]', abort=True)),
    n("arrival", "Narrator", '''{n}Tessa meets you with a bucket, a rag, and a thick piece of chalk. The other team arrives while Irabeth is showing her the join between the boards.{/n}
{n}Perrin kneels, runs a palm over it, and nods.{/n}
{n}"We can mark a full board instead of a thin line. Feet stay behind its near edge. Much easier to see."{/n}
{n}Nessa asks Tessa to name a watcher for each throw, alternating between the teams. Tessa agrees, provided the watcher stands outside the lane and says immediately if a foot touches the marked board before the ball is released.{/n}
{n}Anevia waits for Olva to finish reading the note before speaking to her.{/n}
{n}"We can use that from now on. Doesn't decide where my foot was last time."{/n}
{n}"No," Olva replies. "It doesn't."{/n}''',
      c('[Listen as they settle what they can.]', "won", requires=("three_match.pennant",)),
      c('[Listen as they settle what they can.]', "lost", forbids=("three_match.pennant",))),
    n("won", "Irabeth", '''{n}Irabeth takes the folded red pennant from her pocket and gives it to Tessa to hang above the counter.{/n}
"We have brought it back for the next winners. We are keeping the recorded score."
{n}Olva looks at the pennant, then at Anevia.{/n}
"I still think I saw it."
"I know. I still don't think you did."
{n}Anevia offers her hand. Olva takes it after a moment.{/n}
"I should not have left Nessa to congratulate you for all of us," Olva says.
"You can make up for it by losin' graciously today."
{n}Olva laughs despite herself. Irabeth exhales and picks up the bucket.{/n}''', c('[Help prepare the lane.]', "line")),
    n("lost", "Anevia", '''{n}Olva returns the red pennant to Tessa. Nessa notices Anevia looking at it.{/n}
"You can try to take it home this time."
"That was the plan last time. Had some complications."
{n}Irabeth stands beside her wife.{/n}
"I asked for the replay. I do not want this afternoon to begin with an apology from Anevia for agreeing to it."
{n}Nessa nods. Olva rubs her hands together, looking for an answer before choosing a simpler one.{/n}
"Then shall we play?"
"As soon as you've helped us make this line visible," Anevia tells her.''', c('[Help prepare the lane.]', "line")),
    n("line", "Narrator", '''{n}You hold the straightedge Irabeth brought while Irabeth washes off the old chalk. Anevia and Olva mark the new boundary, one at each end. Tessa checks it from both sides before letting anyone retrieve a ball.{/n}
{n}The first watcher is Nessa. She crouches beside the lane, points at the full marked board, and makes Perrin move his foot back before his practice roll.{/n}
{n}"See? Very difficult for the cooper," Anevia says. "Can't bear to be separated from a board."{/n}
{n}Perrin's ball misses every pin. He declares this a protest against the new regime. Nessa writes a large zero on the practice slate.{/n}
{n}Irabeth bends her head toward yours.{/n}
{n}"I wanted to hear that laugh again," she says. Anevia is still laughing at Perrin.{/n}''',
      c('"I wanted another turn on our team."', "team", requires=("three_beth_score.team",)),
      c('"You can keep looking at me like that, too."', "noticed", requires=("three_beth_score.noticed",))),
    n("team", "Irabeth", '''"Then take the second roll again. I like knowing you are behind me when I begin."
{n}Anevia returns the chalk and reaches for a ball.{/n}
"And I'm behind both of you. Restorin' order."
"You may have to settle for eight pins."
"Nine. Been thinkin' about that last one."
{n}Irabeth smiles at you before stepping to the new mark.{/n}''', c('[Take your places for the match.]', "game")),
    n("noticed", "Irabeth", '''"I can. I may neglect the scoreboard."
{n}Anevia catches the last sentence as she returns from the counter.{/n}
"I'll keep score. You two can concentrate on lookin' pleased with yourselves."
{n}Irabeth reaches for her wife's hand and kisses her knuckles.{/n}
"That was also meant for you."
{n}Anevia's answer arrives a little late.{/n}
"Yes. Well. Naturally."''', c('[Take your places for the match.]', "game")),
    n("game", "Narrator", '''{n}This match is decided before the last roll. Nessa scores nine, then eight, using the same slow delivery both times. Irabeth crouches behind the fence to watch the second one and comes back shaking her head in admiration.{/n}
{n}By Anevia's final turn, you cannot catch the other team's total. She studies the pins anyway. Her ball knocks down seven, leaving two against the left board.{/n}
{n}"Again," she says, reaching for another ball.{/n}
{n}"Match is over," Tessa reminds her.{/n}
{n}"Good. Nobody can object to how long I take."{/n}
{n}Tessa checks that the watcher is clear, then lets her roll. This time both remaining pins go down.{/n}
{n}Irabeth claps. You join her. Anevia bows deeply enough that Olva tells her she has crossed the line by several feet.{/n}''', c('[Join the other team at the counter.]', "after")),
    n("after", "Narrator", '''{n}Nessa buys a jug of cider. Olva stays to pour it. The pennant goes into Perrin's pocket while he explains the devastating tactical advantage of having Nessa on one's team.{/n}
{n}Anevia draws three small rolls from a paper bag and passes them to you and Irabeth.{/n}
{n}"Bought these from Dalia on the way. Don't ask if mine looked as good."{/n}
{n}Irabeth breaks hers open. The crumb is lighter than the loaf Anevia made at her lesson.{/n}
{n}"I could not make either of them," she says. "You have learned something I have not."{/n}
{n}"She also threatened the flour bowl," you tell her.{/n}
{n}"That was a private conversation," Anevia says.{/n}
{n}Irabeth laughs, then brings her wife's hand briefly to her cheek. Anevia leaves it there until Tessa asks who wants another cup.{/n}''',
      c('[Stay for the drink and conversation.]', "invitation")),
    n("invitation", "Anevia", '''{n}By the time you leave, another pair of teams has begun a match. Irabeth pauses at the gate to watch a roll, then makes herself turn back.{/n}
"We can come again," Anevia tells her. "Even when you aren't carryin' a prize."
"I know. I wanted to see whether she used the side board."
{n}Anevia takes one of her hands and offers the other to you.{/n}
"Come to ours when we've all got an evening. Beth wants to show us somethin'."
{n}Irabeth looks faintly embarrassed.{/n}
"It is a map. You need not make it sound mysterious."
"Too late. Now they've got expectations."''',
      c('[Arrange the evening with them.]', flags=("three_return_game.kept",))),
], requires=("three_beth_score.heard", "three_anevia_flour.baked"))


s("three_small_journeys", "Places they had not gone", "Together",
  '"I was promised a mysterious map."', [
    n("start", "Irabeth", '''"Anevia promised that. I promised a map."
{n}Irabeth opens it across the low table. It is a traveler's sketch copied onto cheap paper, with uneven roads and small pictures beside some of the towns. Anevia settles on the rug with three cups and a jug of water.{/n}
"I bought it from a woman who repairs wagon covers," Irabeth explains. "She drew the route for a customer, then sold me a copy. It is not a military survey."
"Strong recommendation," Anevia says. "Where's the place with the pastry?"
"It is a mill."
"Could have both."''',
      c('[Sit with them and examine the map.]', "places"),
      c('[Ask to keep the evening for another day.]', abort=True)),
    n("places", "Irabeth", '''{n}Irabeth points to a small circle beside a river.{/n}
"There is a public garden here. The woman said they grow fruit against warm walls and open the gate when it is in flower. I would like to go when nobody expects me to inspect the walls."
"I'd like the market town," Anevia says, touching another mark. "According to the woman, half the stalls sell things the other half have just bought. Sounds educational."
{n}Irabeth looks at her wife.{/n}
"You want to watch people steal from each other?"
"No. I want to spend an entire afternoon decidin' whether to buy something useless. Could watch people while I do it."
{n}She glances toward you.{/n}
"You get a place, too. Doesn't have to be on her map."''',
      c('"Somewhere beside water. I would like to hear it without looking for a crossing."', "water", flags=("three_small_journeys.water",)),
      c('"A crowded street where nobody knows us. I want to find out what catches your attention."', "street", flags=("three_small_journeys.street",))),
    n("water", "Anevia", '''"A little boat. One of the broad ones, so Beth doesn't spend the day expectin' to capsize us."
"I would expect you to rock it deliberately."
"Once. To establish what we're workin' with."
{n}Irabeth draws a small boat beside the river, then hands you the pencil.{/n}
"You should choose where it stops. Somewhere with dry ground and enough room to put our things down."
{n}Anevia leans against her wife's knee.{/n}
"I like this. We've been away ten minutes and already she's requisitioned a landing."''',
      c('[Mark a quiet landing near the garden.]', "order")),
    n("street", "Irabeth", '''"Anevia would find a door she wanted to open. I would find something to eat before she convinced us to follow her."
"Slander. I'd feed you first. Makes you more agreeable."
{n}Irabeth takes the pencil and draws three small marks beside the market town.{/n}
"Then we could separate for an hour and each bring back something for the other two to see."
{n}Anevia's expression warms.{/n}
"An hour? I'd have a terrible time choosin'."
"That is what you said you wanted."''',
      c('[Add a meeting place where the three routes can end.]', "order")),
    n("order", "Narrator", '''{n}You add your mark. Anevia puts her cup down and studies the space between the garden and the town.{/n}
{n}"We can't do all of it in one day."{/n}
{n}"No," Irabeth says. "I thought perhaps we could stop trying to plan only one day."{/n}
{n}Her wife looks up. Irabeth has kept her attention on the map, but her hand is still beside Anevia's shoulder.{/n}
{n}"I do not know when," Irabeth continues. "I know there are things I want to do when I can. I would like you both to help me choose."{/n}''',
      c('"Begin with the garden. Let Irabeth choose a day we do not have to hurry."', "garden", flags=("three_small_journeys.garden_first",)),
      c('"Begin with the market. Let Anevia take us somewhere she has never had to work."', "market", flags=("three_small_journeys.market_first",))),
    n("garden", "Irabeth", '''{n}Irabeth circles the garden. Anevia takes the pencil from her and draws a basket beside it.{/n}
"I'll bring the bread. Something better than the lesson loaf."
"I liked that one."
"You liked me puttin' it in front of you."
"I liked that very much. I also liked the bread. You must allow me two opinions."
{n}Anevia looks down, smiling. Irabeth bends to kiss the side of her head.{/n}
"We can go to the market afterward. I would like to see what you find."''', c('[Keep both places on the map.]', "near")),
    n("market", "Anevia", '''"Then I get to buy something that has no practical use. You're both witnesses."
"I shall remind you when you begin inspecting the stitching," Irabeth says.
"The useless thing can be well made."
{n}Anevia circles the town, then connects it to the garden with a dotted line.{/n}
"We stay long enough to see your flowers. I don't want you spendin' the whole day pretendin' you aren't wonderin' about them."
{n}Irabeth rests her cheek briefly against her wife's hair.{/n}
"Thank you. I would have wondered."''', c('[Keep both places on the map.]', "near")),
    n("near", "Irabeth", '''{n}Irabeth folds the map along its old creases, leaving the pencil inside, and puts it on the shelf. Anevia moves the cups onto the table before getting up from the rug.{/n}
"We have this evening," Irabeth says. "I would like to spend the rest of it closer to you."
{n}She looks at you, then at her wife. Anevia steps into her arms and kisses her. Irabeth's hand spreads across her back, drawing her in.{/n}
{n}When they part, Anevia offers you a hand.{/n}
"Beth's got an excellent idea. I intend to encourage it."''',
      c('[Join them for kisses, then stay together through the night.]', "night", flags=("three_small_journeys.night",)),
      c('[Join them on the cushions and ask for a quiet evening together.]', "quiet", flags=("three_small_journeys.quiet",)),
      c('"I want to be here. I need to leave later for another promise I have made."', "time", flags=("three_small_journeys.later_promise",))),
    n("night", "Narrator", '''{n}Anevia draws you close. Irabeth touches your cheek before kissing you, and Anevia's hand remains linked with yours while you answer. When you turn toward Anevia, she is already smiling.{/n}
{n}"Took you long enough," she murmurs, then kisses you before you can defend yourself.{/n}
{n}Irabeth laughs and catches her wife's wrist. Anevia turns into the next kiss with an eagerness that leaves the joke unfinished.{/n}
{n}You stay close while they find their way back to you. Later, Irabeth banks the fire and Anevia checks the latch. Neither task takes her far. They return together, and you make room for them.{/n}
{n}In the morning, Anevia wakes first and tells you, with great solemnity, that she has thought of another place for the map. Irabeth pulls the blanket over her own ear.{/n}
{n}"After breakfast."{/n}
{n}"You're goin' to like it."{/n}
{n}"Then I should like to be awake."{/n}
{n}Anevia settles back, laughing quietly, and rests a hand where both of you can reach it.{/n}''',
      c('[Stay until all three of you are ready to begin the day.]', flags=("three_small_journeys.kept",))),
    n("quiet", "Narrator", '''{n}Irabeth fetches another cushion and sits with her back against the couch. Anevia settles beside her, leaving a place for you. You choose it, and Irabeth puts an arm along the back of your cushion.{/n}
{n}Anevia traces a road on her wife's palm with one finger. Irabeth guesses the wrong town deliberately. After the third attempt, Anevia looks at you.{/n}
{n}"She's usually brighter than this."{/n}
{n}"Your geography is poor," Irabeth says.{/n}
{n}You take Anevia's offered hand and trace your own route. She holds it still until you finish. Irabeth watches, her chin near your shoulder.{/n}
{n}Eventually the game stops. Anevia's head rests against her wife's arm, and Irabeth's hand finds yours. When you leave for the night, they walk you to the door together and ask when you would like to come back.{/n}''',
      c('[Choose another evening before saying goodnight.]', flags=("three_small_journeys.kept",))),
    n("time", "Anevia", '''"Then tell us when, before I get comfortable and make an unreasonable case for another hour."
{n}You give them the time. Irabeth moves the little clock where all three of you can see it.{/n}
"There. We can enjoy what we have."
{n}She fetches cushions. Anevia sits beside you and draws Irabeth down on her other side, then shifts until nobody has been left balancing on an edge.{/n}
"Give me your hand," she tells her wife. "I've thought of a game."
{n}She begins drawing a route on Irabeth's palm and asks you to guess the destination. Irabeth supplies wrong answers so confidently that Anevia finally tells her to stop helping.{/n}
{n}When the agreed time comes, Irabeth notices first. She touches your arm. Anevia gives a disappointed sigh, then stands to fetch your things.{/n}
"Another evening," she says. "I'm keepin' the map."''',
      c('[Thank them for the evening and keep your other promise.]', flags=("three_small_journeys.kept",))),
], requires=("three_return_game.kept",))
