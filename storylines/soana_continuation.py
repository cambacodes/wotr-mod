"""Living Chapter 3 continuation. New incidents do not change native forest outcomes."""
from story_format import c, n, scene

SCENES = []
ACTOR = "64805abb52739e44280a758f850b300c"
ANSWERS = "2b1776f3e398685479ff6b16290b4cc2"


def s(id, title, entry, nodes, requires, delay=24):
    for page in nodes:
        page["Portrait"] = "Soana"
    SCENES.append(scene(
        "soana." + id, title, "Soana", 3, entry, nodes,
        Relationship="soana", Chapters=[3], last=3,
        AnswerLists=[ANSWERS], ContactUnit=ACTOR,
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", "soana.opening_kept", *requires),
        forbids=("soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman"),
        delay=delay, optional=True))


s("one_account", "A warning small enough to hear", '"I brought the account. It has a serious weakness."', [
    n("start", "Soana", '''{n}Soana holds out her hand for the folded page. She has cleared a flat stone for it and weighted the corners with pebbles before she reads a word.{/n}
"You might have found a better one."
"I wanted you to see the weakness before we tried it."
{n}The page describes a watcher's line: loose wooden clappers connected by cord above a narrow crossing. Something large pushing through disturbs the line. Small animals can pass beneath it. There is no spirit in the wood, and nothing capable of defending the crossing once the sound has been heard.{/n}
"A hunter's rattle," she says. "With more writing."
"A warning. It might give you time to reach shelter, or discover what is coming before it reaches the cave."
"And here I was hoping you had brought an army small enough to fit between the folds."
{n}She turns the page over. The reverse is blank.{/n}
"Whose account?"''',
      c('"Mine. A proposal I wrote out so you could find the mistakes. I have no field report to hide behind."', "honest"),
      c('"I should have brought an account of a proven method. This is only a proposal. We can leave it today."', abort=True)),
    n("honest", "Soana", '''"Then call it a proposal. An account tells me what happened."
{n}She draws a line through the heading with a charred twig and writes a shorter one above it. Her letters are angular and quite legible.{/n}
"You have written that the line should be beyond the reach of rabbits. What of a deer? What of rain? What of a branch falling across it while I sleep?"
"Those are things we can test."
"They are things you could have considered before bringing it."
{n}She reads further anyway. At the drawing of the clapper she turns the page toward the light, studying the gap between its two wooden pieces.{/n}
"This will jam when the wood swells. Leave more room. And do not tie the end to a young tree. It will pull every time the wind moves the crown."
"You have begun improving it."
"Bad work offends me even when I intend to refuse it."''', c('[Ask where a warning could actually be useful.]', "outcome")),
    n("outcome", "Soana", '''{n}She places one finger on the drawing of the crossing.{/n}
"Before we go any further, tell me what you expect this thing to replace."''',
      c('"Nothing holding Orso. We have no way here to release him safely. I want to test a warning that demands no captive."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
      c('"It cannot take Orso\'s place. A warning at one crossing might still be worth having while you search."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"You have learned to bring me something I can refuse without first condemning myself."
"You can refuse it. I will still object to what holds him."
{n}Her finger presses harder against the paper.{/n}
"He is still out there. A rattle will not keep the things beyond this forest from devouring it. Do not come back tomorrow and tell me a clever knot has settled what we argued about."
"I won't. Will you show me a crossing?"
"One close enough for me to hear. Far enough that hearing would matter. There is a place above the stream."
{n}She measures a length of cord against her forearm, stops, and measures again. This time she leaves more slack.{/n}''', c('[Hold the cord while she cuts it.]', "author")),
    n("dead", "Soana", '''"While I search," she repeats. "You have no objection to that part?"
"Searching is not the same as binding another creature."
"To you. To me it is the work that must be done before the next horror finds us undefended."
{n}She lifts the little wooden pieces, strikes them together, and listens until the sound has died.{/n}
"There is a crossing above the stream. I used to hear larger feet there."
{n}She puts the pieces down separately.{/n}
"We will try your warning. If I hear it in the night, I will know it is not him. I would know that without your invention, of course. Do not look pleased with the lesson."''', c('[Lay out enough cord for the crossing.]', "author")),
    n("author", "Soana", '''"No incantation?" she asks.
"None in this proposal."
"Good. I told the rulers of Sarkoris to wipe out the mages without mercy. They would not listen. And still the clever people insist that the next spell will repair what the last clever person ruined."
{n}She is addressing the paper, but watching you.{/n}''',
      c('"I practice magic. If we work together, you will have to judge what I actually do."', "mage", flags=("soana.magic_declared",)),
      c('"A method can be dangerous. That does not justify killing everyone who studies it."', "challenge"),
      c('"Judge this proposal first. I have not asked you to trust a spell."', "limited", flags=("soana.argument_deferred",))),
    n("mage", "Soana", '''"Then keep your hands where I can see them while we tie the knots."
"That was not a joke worth making."
{n}She draws herself up. For a moment the cave feels smaller.{/n}
"You come into my forest and tell me which dangers I may remember?"
"Remember them. You have also watched these hands hold a basket and carry your water. Neither act makes every spell safe. Neither disappears because you dislike what else I can do."
{n}Her gaze drops to the cord you are holding.{/n}
"I have not forgotten the water."
"Then begin with that much."
"I said I have not forgotten. You may decide for yourself whether it is enough to begin with."''', c('[Continue the work without pretending the prejudice is resolved.]', "end")),
    n("challenge", "Soana", '''"You speak very easily of mercy toward the people who tore open our country."
"Your advice would have killed people who had nothing to do with it. Children who had never cast a spell against anyone."
{n}The twig snaps in her hand. She looks at the broken end, then sets both pieces down.{/n}
"You have come to put the whole of Sarkoris on this stone between us."
"I came with a warning made of wood. You brought the mages into it."
{n}For several breaths she says nothing. Then she turns the page back to the drawing.{/n}
"The lower knot belongs here. If you make it there, the clapper will strike your leg."
{n}She has not answered you. She has chosen to continue working beside someone who contradicted her, which is less than agreement and more than she appeared ready to offer.{/n}''', c('[Move the knot to the marked place.]', "end")),
    n("limited", "Soana", '''"Very well. Your proposal has one considerable merit. I can cut it with a knife."
"If it fails, we will know what failed."
"If it fails while something is coming to kill me, I may have more immediate concerns. We shall test it by daylight."
{n}She folds the paper along its old crease. The dispute remains where you left it, plainly visible whenever either of you chooses to return to it.{/n}''', c('[Agree to a daylight trial.]', "end")),
    n("end", "Soana", '''{n}Soana gathers the clappers into a shallow bowl. She keeps your amended page beneath it rather than giving it back.{/n}
"Come when you have time to sit still. People who command armies often imagine that watching is what happens between useful acts."
"And what should I bring?"
"Your ears. Perhaps a little less satisfaction with your own answers."
{n}She looks at the page again. The corner of her mouth moves.{/n}
"Leave the handwriting. I could read it."''', c('[Return for the daylight trial.]', flags=("soana.proposal_kept",))),
], requires=("soana.inquiry_invited",))


s("watch_line", "What moves the branch", '"Shall we try the warning?"', [
    n("start", "Soana", '''{n}The clappers are waiting in their bowl. Soana puts the coil of cord over her shoulder and gives you the bowl to carry.{/n}
"Do not let them strike together until we are there. I would prefer to frighten things only once."
{n}The crossing lies a short walk above the stream. Two banks narrow around a patch of firm ground, and several trails meet there before dividing beneath the trees. Soana points to a place beside a fallen trunk where she can sit without losing sight of the path.{/n}
"I can hear this place from the cave when the wind is right. We shall discover what happens when it is wrong."
{n}Together you stretch the line between stout branches, high enough to leave a gap beneath it. She refuses your first knot, accepts your second, and pulls hard enough to make you check the branch you chose.{/n}
"Now cross it. Slowly. Imagine you have more sense than a commander."
{n}The cord catches against your upper arm. Wood taps wood. From her seat, Soana raises one finger to show she heard.{/n}''',
      c('[Join her beside the fallen trunk and watch the crossing.]', "watch"),
      c('"I cannot stay for the trial today."', "defer")),
    n("defer", "Soana", '''{n}She unties the nearest end and winds the loose cord around the clappers.{/n}
"Then we take it down. An unattended experiment is merely a hazard with an ambitious name."
{n}You help carry the pieces back to the cave. She leaves them in their bowl.{/n}''', c('[Return when you can stay.]', abort=True)),
    n("watch", "Narrator", '''{n}A small bird lands on the line. The cord sags, but the wooden pieces do not meet. It departs without sounding your warning.{/n}
{n}Soana rests her hands on her knees. A gust travels through the leaves above you. Nothing sounds. The next gust comes lower, dragging a bough across the far end of the line. The clappers knock sharply together.{/n}
"There is your first invader," she says.
{n}You move the rubbing bough clear and return to the trunk. Minutes pass. Then the clappers strike again, softly this time. Neither of you has seen anything cross.{/n}
{n}The low sound repeats. A reed bends beside the bank, though the leaves above it are still.{/n}''',
      c('[Perception] [Find what is moving before you disturb the crossing.]', check=dict(Skill="SkillPerception", DC=22, Success="found", Failure="missed", CommanderOnly=True), forbids=("soana.watch_found", "soana.watch_missed", "soana.watch_patient")),
      c('[Recall the movement you identified before returning to the line.]', "found", requires=("soana.watch_found",)),
      c('[Return to the evidence left after the boar fled.]', "missed", requires=("soana.watch_missed",)),
      c('[Wait for the movement to repeat. Ask Soana to watch the bank while you watch the line.]', "patient", flags=("soana.watch_patient",), forbids=("soana.watch_found", "soana.watch_missed"))),
    n("found", "Narrator", '''{n}Something dark and bristled shifts beyond the reeds. A young boar has pushed beneath the cord. Its back cleared the line, but a forked twig caught in its bristles is dragging the far end down. The loose twig slips free. The animal snorts and moves out of sight.{/n}
{n}You touch Soana's sleeve and point before she rises. She follows your finger, then settles back.{/n}
"A passenger on the animal, rather than the animal. That will be a troublesome distinction to teach your string."
{n}You have seen exactly how it happened. The cord itself is clear of the trail.{/n}''', c('[Tell her what caught and what passed beneath.]', "choice", flags=("soana.watch_found",))),
    n("missed", "Narrator", '''{n}You rise to look past the bank. A sharp snort answers you. Something crashes through the reeds away from the crossing, and the line shakes hard enough to send the clappers rattling.{/n}
{n}Soana catches the bowl before your heel tips it down the bank.{/n}
"Now it knows about you as well."
{n}When the movement stops, you find a few stiff bristles on a snag and a forked twig hanging from the cord. The tracks belong to a young boar. You cannot tell whether its body or the twig moved the line first.{/n}
"We will have to watch again," you say.
"Yes. Sit where you can rise without kicking our belongings into the water."
{n}The second watch is longer. The boar does not return. When you try a loose twig against the line yourself, it catches readily enough to explain the softer noise, though you have missed the chance to watch the animal do it.{/n}''', c('[Set the recovered twig beside the bowl.]', "choice", flags=("soana.watch_missed",))),
    n("patient", "Soana", '''{n}Soana points two fingers at her own eyes, then toward the bank. You remain still. For a while there is nothing to see except a blade of grass quivering against the cord.{/n}
{n}The movement begins again. A boar emerges with a twig caught in its bristles. The twig has hooked the loose end of the line. It pulls free when the animal turns. The wood gives one last tap.{/n}
{n}Soana waits until the boar has gone before speaking.{/n}
"A patient hunter would have had supper. We have an explanation."
"Would you rather have had supper?"
"At present, I would rather have both. We have used more daylight than I intended."
{n}She eases one stiff leg straight, then bends it again. You move the bowl nearer so she need not reach for it.{/n}
"Leave it there. I can manage."
{n}She reaches for it, considers the distance, and leaves it where you put it.{/n}''', c('[Look together at the loose end of the line.]', "choice")),
    n("choice", "Soana", '''"Raise it," she says. "A smaller creature can pass without sounding the clappers."
"So can anything else that travels low to the ground."
"Lower it, then, and I can spend every night coming to meet a rabbit."
{n}The line hangs between you. Neither position would distinguish a demon from an animal. Neither would give a warning to anyone too far away to hear it.{/n}
"The useful question," she says at last, "is which failure I can endure beside my own cave."''',
      c('"Raise it. You need sleep more than a warning for every small movement."', "high", flags=("soana.line_high",), forbids=("soana.line_daywatch",)),
      c('"Keep it lower, but only use it while you are awake and listening. A watch, not a promise of safety."', "low", flags=("soana.line_daywatch",), forbids=("soana.line_high",))),
    n("high", "Soana", '''{n}You shorten the hanging ends and move the line up. Soana crosses beneath it without crouching, then stops and looks back at you.{/n}
"There. I have invaded my own forest undetected."
"Something taller would sound it."
"Something taller with the courtesy to use this path."
{n}She makes you pass through once more, while she listens from the first bend toward the cave. This time she calls back that she heard only the final knock. You move one wooden piece so it strikes more cleanly. She then listens beside the rushing stream while you sound the clappers again. There she misses two knocks out of three.{/n}
"Leave it for now," she says. "I will hear what it has to say. I shall not sleep with my knife on the far side of the cave."''', c('[Walk back with her.]', "finish")),
    n("low", "Soana", '''{n}You leave the cord at its lower height and tie a loose loop at the near end, so she can take it down without reaching across the crossing.{/n}
"When I stop listening, I unhook it," she says. "A device designed to remind me of another thing I must remember."
"It may not be worth keeping."
"I intend to discover that for myself."
{n}She makes you sit in her place while she trips the line. You can hear it plainly. Then you exchange places. She listens from the bend toward the cave while you trip the line again, and calls back that she heard. Beside the rushing stream, she misses two knocks out of three.{/n}
{n}On the return, she unhooks the line and hangs the clappers beside the path. They will wait for someone to listen.{/n}''', c('[Walk back with her.]', "finish")),
    n("finish", "Soana", '''{n}At the cave, Soana sits before she puts the bowl down. The walk has tired her, and she is in no mood to have that pointed out.{/n}
"You wanted an account. Now you can write one. Include the boar. It contributed more than your first heading."
"And what did we learn?"
"That I dislike sitting on that trunk. Find me a flat stone next time."
{n}She waits until you have stopped smiling.{/n}
"Also that I can hear the clappers from the bend, and not reliably over running water. Write that plainly. It is the part someone might die from misunderstanding."''', c('[Write down the warning\'s actual limits.]', flags=("soana.watch_kept",))),
], requires=("soana.proposal_kept",))


s("price_of_warning", "The keeper cannot hear everything", '"Has the warning earned its place?"', [
    n("start", "Soana", '''{n}Soana has your page open on the stone again. Beside the drawing she has made several short marks. One has been crossed out so heavily that the paper has worn thin.{/n}
"I was going to ask you whether an invention can be taught to keep its opinions to itself."
{n}She pushes the page toward you.{/n}''',
      c('[Read the marks beside the raised line.]', "high", requires=("soana.line_high",)),
      c('[Read the marks beside the daylight watch.]', "low", requires=("soana.line_daywatch",))),
    n("high", "Soana", '''"Two branches. One deer. The deer sounded it twice. Once going out, once deciding it preferred the other direction."
{n}She taps the crossed-out mark.{/n}
"That one was me. I forgot where we tied it. I expect you will wish to record the triumph of catching the keeper herself."
"Did you sleep?"
"Eventually."
{n}She takes a gnawed root from a dish and lays it below the page.{/n}
"Something smaller reached the food outside the cave. Your line had nothing to say about it. I knew it might. Knowing is less satisfying when one is scraping teeth marks off supper."
"We can take it down."
"I have not finished complaining."''', c('[Wait for the rest of her account.]', "outcome")),
    n("low", "Soana", '''"I sat with it yesterday. I heard a hare disturb the hanging end. Then I heard something larger, and found only mud and a print too spoiled to read."
"No danger?"
"No danger I saw. That is a different answer."
{n}She taps the crossed-out mark.{/n}
"Today I took it down because I needed to gather food. A young deer used the crossing while I was away. Its prints were quite clear."
"The warning needs someone to hear it."
"Yes. We established that admirably. What I had not established was how much I resent leaving useful work to sit beside a stick."
{n}She picks a burr from her sleeve and crushes it between two fingernails.{/n}
"You might put that in the account as well."''', c('[Ask what happened to the food gathering.]', "outcome")),
    n("outcome", "Soana", '''"I gathered enough. I was late returning. The pot was cold, and I was hungry, and the forest continued to require attention without consulting my appetite."
{n}She looks toward the cave mouth.{/n}''',
      c('"Orso is still carrying what you bound to him. Our experiment has not reduced that burden."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
      c('"Without Orso, you are trying to be everywhere. This cannot make one pair of hands enough."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"No. It has given me one more thing to tend."
"It has also shown us what one warning can and cannot do."
"And if I had told you all of that at the beginning, you would have called it an excuse to keep him bound."
{n}There is a challenge in her face. There is also the fatigue she has been refusing to show you.{/n}
"Perhaps I would," you say. "It would still matter that he is suffering."
"You think I never hear him?"
{n}The question escapes more sharply than she intended. She presses her lips together.{/n}
"Do not answer that. You have answered it before. I know what I did. What I do not know is how to undo it without leaving everything else to die."''', c('[Stay with the practical question without offering absolution.]', "choice")),
    n("dead", "Soana", '''"You speak as if I had not noticed my own hands."
"I have watched you use them. I am asking what happens when you cannot."
"The same thing that happens when the Commander cannot hold a wall. Something gets through."
{n}She turns her palms upward. The gesture is brief and furious.{/n}
"There. A plain enough answer for you? Orso is gone. I cannot make another friend by naming a beast after him. I still need something that can stand where I cannot."
"And whatever you find will have its own life."
"I know that."
{n}She says it as though knowledge itself were a wound you keep touching.{/n}''', c('[Ask what she can actually change today.]', "choice")),
    n("choice", "Soana", '''"You would have me ask for help."
"Would you?"
"From whom? A village has its own needs. Your soldiers have a war. Shall I call into the trees until a willing guardian falls out of them?"
{n}She pulls the page back toward herself.{/n}
"I can give up this crossing. I can keep a smaller watch near the cave. I can spend less of myself trying to hear every movement. Each choice leaves something unwatched. Tell me which one your proposal has made easy."''',
      c('"Keep a smaller watch near the cave. Protecting your own rest gives you something left for the forest."', "near", flags=("soana.watch_near_cave",), forbids=("soana.watch_removed",)),
      c('"Take the line down. Keep the account. A failed method is still worth refusing before it costs more."', "remove", flags=("soana.watch_removed",), forbids=("soana.watch_near_cave",)),
      c('"I cannot keep visiting while another binding remains your answer. I will help remove the line, then leave."', "leave", flags=("soana.closed",))),
    n("near", "Soana", '''"You have a gift for making retreat sound like good housekeeping."
"Would you rather call it something grander?"
"I would rather need no retreat."
{n}She rises. You go back to the crossing together, untie the cord, and carry it to a narrow approach within sight of the cave. Here the clappers can hang from a dead branch. No living tree needs to carry the strain.{/n}
{n}Soana tests it herself. The knock is sharp in the sheltered entrance.{/n}
"That I can hear."
"Will you keep it?"
"For now. I will unhook it when I need quiet. A warning that never stops speaking is a poor companion."
{n}She gives you a sideways glance. It is not entirely a rebuke.{/n}''', c('[Help her make the end easy to unhook.]', "finish")),
    n("remove", "Soana", '''{n}She studies you for a moment, apparently waiting for you to rescue your invention with another argument.{/n}
"You will take it down yourself?"
"I helped put it up."
"Good. The far knot has tightened. You may enjoy undoing your own excellent work."
{n}You do not enjoy it. Soana watches your struggle, then passes you her awl without comment. The point loosens the cord enough to pull it free.{/n}
{n}Back at the cave, she coils the line and keeps the clappers in their bowl. She does not throw them into the fire.{/n}
"Useful wood," she says when she catches you looking.
"And an account?"
"A shorter one, now that we know how it ends."''', c('[Amend the account with her.]', "finish")),
    n("leave", "Soana", '''"Then we had better do that before you leave in such a hurry that I must climb the bank myself."
{n}You take down the cord together. She keeps the wood and gives you back the page, with all her corrections still on it.{/n}
"I have not changed my mind because you are going."
"I know."
"Nor was the work worthless because it failed to make us agree."
{n}She folds the cord around her hand and returns to the cave. You leave the path clear behind you.{/n}''', c('[End the private visits.]')),
    n("finish", "Soana", '''{n}Soana adds one final sentence beneath the drawing. She lets you read it before laying the twig down.{/n}
"The watcher must be able to stop watching."
{n}Her handwriting grows smaller toward the edge of the page.{/n}
"I dislike it," she says.
"The sentence?"
"That it is true."
{n}She folds the page and puts it away. Then she reaches for a little covered pot you have not seen her open before.{/n}
"Next time, come without a proposal. I have something that will spoil if I keep waiting for a good occasion. We may have to endure an ordinary one."''', c('[Accept an afternoon without another experiment.]', flags=("soana.warning_reckoned",))),
], requires=("soana.watch_kept",))


s("ordinary_feast", "A feast for an ordinary afternoon", '"You said something would spoil if we waited for an occasion."', [
    n("start", "Soana", '''{n}Soana takes the cover off the pot. Inside is a little honey, thick enough to cling to the spoon. A dish of tart berries waits beside it.{/n}
"I had hoped for sweeter fruit. The fruit had other ambitions. Sit down."
{n}She has put a folded cloth on a flat stone. There is room for you beside her, though the dish between you prevents any accidental closeness.{/n}
"No new plans?" she asks.
"You told me not to bring one."
"It is a relief to discover you can follow an instruction without first enlarging it."
{n}She gives you a spoon and takes the smaller one herself. The first berry draws her lips tight. She dips the next in more honey.{/n}
"The bees did their work. I shall blame the bushes."''',
      c('[Taste a berry before adding honey.]', "sour"),
      c('"I trust your judgment." [Take enough honey the first time.]', "sweet"),
      c('"I cannot stay today. Keep some for yourself."', abort=True)),
    n("sour", "Soana", '''{n}She watches your face with undisguised interest.{/n}
"Well?"
"It is awake."
"So are you, now."
{n}Her laugh is short and unexpectedly full. She has to set her spoon down before it spills. When you reach for the honey, she moves the pot nearer without surrendering the pleasure of having watched you discover the obvious.{/n}
"You could have warned me."
"I did. You chose an independent investigation. I thought you valued those."''', c('[Add honey and let her enjoy being right.]', "song")),
    n("sweet", "Soana", '''"A dangerous habit. I might decide to test how far it extends."
"As far as berries. Further matters will require discussion."
{n}She makes a thoughtful noise and puts a particularly small berry on your spoon.{/n}
"Then we begin cautiously."
{n}You eat it. The honey is almost enough to conceal the sourness.{/n}
"Your judgment needs more honey."
"Most people's does. Few can afford so much."
{n}She passes the pot back, smiling into her own dish.{/n}''', c('[Move the dish where both of you can reach it.]', "song")),
    n("song", "Soana", '''{n}For a while you eat without discussing anything that needs saving. A bee finds the rim of the honey pot. Soana waits for it to move before she replaces the cover.{/n}
{n}Then she begins humming. The tune climbs as if it intends to become solemn, loses its footing, and comes down again in a quick run of notes.{/n}
"That does not sound like a sacred song."
"It is not."
{n}She leaves a deliberate silence where the next line should be.{/n}''',
      c('"Now I want to hear the words."', "words", flags=("soana.song_heard",)),
      c('[Try to hum the falling phrase back to her.]', "hum", flags=("soana.tune_tried",)),
      c('"Keep singing. I like it without an explanation."', "listen", flags=("soana.song_listened",))),
    n("words", "Soana", '''"A young man took his finest cloak,
And swore the rain would spare it.
He met his lover by the oak,
And found her goat would wear it."
{n}Soana stops singing and takes another berry.{/n}
"There are other verses. The young man becomes considerably less well dressed."
"And the goat?"
"Prospers."
{n}You ask whether the lover ever intervenes. Soana looks scandalized.{/n}
"Against a creature of such excellent taste? She is a sensible woman."
{n}She sings the next verse after all. The young man attempts a dignified retreat without his belt. His lover admires his determination, loudly enough for the neighbors to hear.{/n}''', c('[Ask where she used to sing it.]', "festival")),
    n("hum", "Soana", '''{n}You begin too high. Halfway down, the tune escapes you. Soana finishes it, then starts again a little lower.{/n}
"There. Give yourself somewhere to land."
{n}The second attempt reaches the final note. She taps her spoon against the dish to give you the rhythm, and you try the phrase once more.{/n}
"Do I pass?"
"You arrive. We can decide what to call it later."
{n}She adds words about a foolish young man and an exceptionally well-dressed goat. You lose the tune again, this time because you laugh before the end.{/n}
"A reasonable place to stop," she says. "The goat usually receives the applause."''', c('[Ask where she used to sing it.]', "festival")),
    n("listen", "Soana", '''{n}She lifts one eyebrow, but keeps the tune going. Without words, its little hesitation becomes funnier each time she repeats it. You begin to recognize where the singer is expected to linger and where the listener is expected to laugh.{/n}
{n}At the end she gives the final phrase an outrageous flourish. It exhausts her breath and leaves her shaking her head at herself.{/n}
"I used to do that better."
"I liked it."
"So did I. That is why I kept the foolish ending."
{n}She rests for a moment before reaching for her spoon again.{/n}''', c('[Ask where she used to sing it.]', "festival")),
    n("festival", "Soana", '''"Away from anyone who was trying to conduct a serious rite. People came to the festival to honor the spirits. They also came because the person they hoped to kiss might be there. Both purposes generally survived."
{n}She looks at the covered honey pot.{/n}
"There were flowers underfoot, and water in the holy spring. When we sang, voices answered through the trees. It was all there. So was somebody being sick behind a bush because he had mistaken a mead cup for a challenge."
"You miss that too?"
"I miss telling him to move farther from the spring."
{n}The answer surprises her into another small laugh. Then her face grows quiet.{/n}
"You can remember a place until no one in it is allowed to be foolish. It becomes a tiresome place to live."''',
      c('"You were allowed to be foolish too?"', "foolish"),
      c('"What would you keep for an afternoon here, if you could choose one part?"', "choose")),
    n("foolish", "Soana", '''"I was not allowed. I managed it without permission."
"The song?"
"Among other things. I once contradicted the wrong singer through an entire chorus because I was certain I knew the older words."
"Did you?"
"The words were older. The song was different."
{n}She fixes you with a stern look.{/n}
"You are enjoying this excessively."
"I may remember it next time you correct me."
"Do. It will give you something to think about while you do the work again."''', c('[Finish the last berries together.]', "end")),
    n("choose", "Soana", '''{n}She considers the question without immediately refusing its premise.{/n}
"Someone else deciding when to begin the next song. I had responsibilities. I was consulted. I was also followed around by people who thought every silence required my wisdom."
"Would you like me to begin one?"
"Only if you know one. This is a meal, not a trial of your courage."
{n}You leave the offer there. She hums the little falling phrase once more, softly enough that it belongs to the space between you.{/n}
"There. I have begun it myself again. Old habits are difficult company."''', c('[Finish the last berries together.]', "end")),
    n("end", "Soana", '''{n}Soana holds the dish while you scrape the last of the honey from its edge. She could do it herself. She keeps holding it until you put the spoon down.{/n}
"A satisfactory use of berries," she says.
"And of an afternoon?"
"I am still considering the afternoon."
{n}She takes the empty dish from between you. For the first time since you sat down, there is nothing occupying that little space.{/n}
"You may stay until the light changes. I have no further entertainment prepared."''',
      c('[Stay beside her without making the invitation into a demand for more.]', flags=("soana.feast_kept",)),
      c('"I enjoyed this. I have to go while there is still light."', flags=("soana.feast_kept",))),
], requires=("soana.warning_reckoned",))


s("name_between", "The name she keeps", '"May I sit with you again?"', [
    n("start", "Soana", '''{n}Soana has spread a piece of cloth over the stone where you ate. She lifts one corner, finds a seed beneath it, and flicks the seed toward the cave mouth before answering.{/n}
"Yes. Though I have no honey left to improve your opinion of the company."
{n}You sit. She folds the cloth once, then once again. The work does not need so much attention.{/n}
"There is something I ought to say while neither of us is reaching for a tool."
{n}She puts the folded cloth down.{/n}''',
      c('[Give her time to choose her own beginning.]', "marriage"),
      c('"I would like to hear it when I can stay. Not in a hurried visit."', abort=True)),
    n("marriage", "Soana", '''"Corven is my husband. I have used the past when I spoke of our wedding, because the wedding is in the past. That is not the same as telling you the marriage ended."
{n}She watches your face, refusing to look away first.{/n}
"I do not know whether he lives. I do not have a grave to show you, or a last message that makes everything tidy. We did not sit down together and release each other from our promises."
{n}Her hands remain on her knees.{/n}
"I can speak plainly about what I want now. I cannot borrow an answer from him to make it easier."
"What do you want?"
"To keep seeing you. To find out whether I want you closer. I have been waiting for the wanting to become convenient. It shows no sign of doing so."''',
      c('"I want to court you. I understand you have not said Corven agreed, or that the marriage ended."', "court", flags=("soana.courtship_chosen",), forbids=("soana.friendship_chosen", "soana.courtship_waiting")),
      c('"I care for you, but I do not want a romance while that remains unresolved. I would like to keep our friendship."', "friend", flags=("soana.friendship_chosen",), forbids=("soana.courtship_chosen", "soana.courtship_waiting")),
      c('"I am not ready to answer. I would like another ordinary afternoon before I do."', "wait", flags=("soana.courtship_waiting",), forbids=("soana.courtship_chosen", "soana.friendship_chosen")),
      c('"I cannot continue these private visits. Thank you for telling me plainly."', "leave", flags=("soana.closed",))),
    n("court", "Soana", '''"I heard you. You need not repeat it like an oath being witnessed."
{n}Her fingers loosen on her knee.{/n}
"I was afraid you would say that time had settled the matter. Or that I deserved some happiness, as though deserving could answer a question I had not faced."
"I would rather hear what you decide."
"Then hear this. I want another afternoon. I want to sit close enough to discover whether I still have the nerve to touch someone because I wish to."
{n}She holds out her hand, palm upward. It trembles slightly. Her expression dares you to attribute that to only one cause.{/n}''',
      c('[Take her offered hand.]', "hand", flags=("soana.hand_taken",)),
      c('"I want that afternoon. Let us begin there, without hurrying."', "slow")),
    n("hand", "Soana", '''{n}Her fingers close around yours. She presses once, testing the comfort of the grip, then turns your joined hands until neither wrist is bent.{/n}
"There. A practical matter disposed of."
"Was that the practical part?"
"The wrist was."
{n}She looks up at you. A little color has risen in her face, and her amusement does not quite conceal it.{/n}
"You may enjoy the rest without requiring me to describe it."
{n}You sit until the warmth of her hand becomes familiar. When she lets go, she does it to move nearer the cave wall, where the stone shields her from a draft. She gestures for you to move beside her.{/n}''', c('[Stay beside her.]', "end")),
    n("slow", "Soana", '''{n}She lowers her hand. There is a moment of disappointment, which she does not disguise quickly enough to pretend it was never there.{/n}
"Very well. Another afternoon."
"I meant what I said."
"So did I. We shall have to endure meaning things at different speeds."
{n}She shifts nearer the cave wall, out of the draft, and leaves room beside her.{/n}
"Come away from the entrance, at least. Caution need not be cold."''', c('[Take the place beside her.]', "end")),
    n("friend", "Soana", '''{n}She nods once. Her mouth tightens before she can prevent it.{/n}
"A clear answer. I asked for one."
"I do want to keep coming."
"Then come. I have not become unfit for company because you will not court me."
{n}She picks up the folded cloth, considers it, and puts it down again without finding more work for it.{/n}
"I may be cross for a little while. You are familiar with that part of me."
"I am."
"Good. Then we need not begin our acquaintance again."''', c('[Stay for the conversation you offered.]', "end")),
    n("wait", "Soana", '''"Another ordinary afternoon. I shall have to discover whether I have enough ordinary conversation for two."
"We managed one."
"With the help of honey. We must not underestimate it."
{n}She rests her hands on the folded cloth.{/n}
"I can wait. I will not claim that waiting is the answer I hoped for."
"I would not ask you to."
"Then we have saved ourselves a rather dull performance. Tell me something you noticed on the path here. Something that does not require me to rescue it."
{n}You turn toward the light at the entrance. For a while the conversation can be as small as she asked.{/n}''', c('[Stay without giving an answer you do not have.]', "end")),
    n("leave", "Soana", '''"Then I am glad I said it before we asked more of each other."
{n}She rises with a hand against the wall. You stand too, leaving her room to steady herself.{/n}
"Keep the account," she says. "You should remember what happened to your proposal."
{n}She gives you the folded page. The corners are worn from both your hands.{/n}
"I will remember more than that."
"Yes. So will I."
{n}She does not ask you to make the farewell kinder by withdrawing it.{/n}''', c('[End these private visits.]')),
    n("end", "Soana", '''{n}Outside, the wind turns the leaves so their pale undersides show. Soana watches them for a while before speaking again.{/n}
"There is a walk I have been avoiding. No great journey. The lower bend, where the water leaves the stones. It used to be a pleasant place to sit."
"Would you like company?"
"That is what I am taking so long to ask."
{n}She gives you a look both impatient and rueful.{/n}
"Next time. Bring nothing that needs improvement. I cannot promise to resist the temptation."''', c('[Agree to walk with her.]', flags=("soana.present_named",))),
], requires=("soana.feast_kept",))


s("lower_bend", "A place she has not lost", '"You asked me to walk to the lower bend."', [
    n("start", "Soana", '''{n}Soana is ready when you arrive. She has a walking stick and a folded cloth beneath one arm. She sees you notice the stick.{/n}
"A branch. A very useful discovery. I recommend it to anyone who has spent too long pretending the ground is level."
{n}She tests the end against the stone, then turns toward the path.{/n}''',
      c('[Walk beside her, leaving room for the stick.]', "line"),
      c('"I cannot give the walk its time today."', abort=True)),
    n("line", "Narrator", '''{n}At the cave mouth she pauses to deal with the warning experiment's remains.{/n}''',
      c('[Wait while she unhooks the warning beside the cave.]', "kept", requires=("soana.watch_near_cave",)),
      c('[Watch her set the bowl of unused clappers farther inside.]', "removed", requires=("soana.watch_removed",))),
    n("kept", "Soana", '''"I have no wish to come running back every time the wind expresses itself."
{n}She hangs the slack loop over the dead branch. The wooden pieces rest against each other without striking.{/n}
"It has warned me about two visitors with feathers and one with hooves. No demons have presented themselves for our convenience."
"It is still an experiment."
"Yes. One I can leave hanging on a branch. That is its finest quality."''', c('[Follow the path down to the water.]', "walk")),
    n("removed", "Soana", '''"The cord will make a better carrying strap. I have not decided what the wood will become."
"It could remain wood for a while."
"An extravagant idea. I shall consider it."
{n}She moves the bowl out of reach of the entrance and retrieves her stick.{/n}
"There. No invention awaiting our return. We may have an afternoon without reporting our conclusions to it."''', c('[Follow the path down to the water.]', "walk")),
    n("walk", "Narrator", '''{n}The lower bend is close enough that you can still make out the pale stone above the cave when the trees open. Soana chooses a slower path around a steep patch rather than letting you hurry ahead to help her down it.{/n}
{n}At the water she spreads the cloth on a broad dry rock. She lowers herself onto it, rests the stick within reach, and lets out a breath she has held through the last few steps.{/n}
"There. It remains a place to sit. I had begun to imagine it required some great reason to come back."
{n}The water moves around a stone worn hollow at its center. Fallen leaves turn in the little basin before spilling over the far edge.{/n}''',
      c('"Tell me what you used to do here."', "memory"),
      c('[Sit beside her and watch a leaf escape the hollow stone.]', "water")),
    n("memory", "Soana", '''"Mended things. Avoided people who wished to be advised. On one memorable afternoon, fell asleep and left a very important visitor to consult the entrance of an empty cave."
"What did you tell them?"
"That the forest had required my attention. It had. I had been snoring in it."
{n}She laughs, then grows thoughtful.{/n}
"Do not make a legend of that. I was not secretly wise in every foolish thing I did. Sometimes I was tired."
"I can remember it that way."
"Good. There may be hope for your accounts yet."''', c('[Look toward the trees beyond the stream.]', "outcome")),
    n("water", "Soana", '''{n}A leaf turns twice in the hollow, catches against another, and stays there. Soana watches with an increasingly disapproving expression.{/n}
"You would think it had found a comfortable home."
"Perhaps it has."
"In a puddle, with someone else's leaf sitting on it?"
{n}The next little surge lifts both leaves free. They tumble away together.{/n}
"There. I have successfully advised a leaf. We may consider the day's obligations fulfilled."
{n}She leans back on one hand. The other lies loose in her lap.{/n}''', c('[Look toward the trees beyond the stream.]', "outcome")),
    n("outcome", "Soana", '''{n}A branch creaks somewhere beyond the water. Soana's head turns toward it before the sound has ended. She waits, listening, until the forest falls quiet again.{/n}''',
      c('"You are listening for Orso."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
      c('"It still sounds as though something large might come down that path."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"Yes."
{n}She keeps looking into the trees.{/n}
"I can sit beside you and enjoy it. He can still be suffering elsewhere. Both things remain true. You need not remind me every time I smile."
"I do not want you to stop smiling. I do not want us to stop looking for another answer either."
"Then we shall have to find something better than a wooden rattle."
{n}She turns back toward you.{/n}
"I will examine another method. When there is one worth examining. I will not unmake what holds him because an afternoon by the water has made me wish the world were gentler."
{n}Her voice has lost none of its stubbornness. She moves the stick closer to her knee and stays beside you.{/n}''', c('[Let the disagreement remain part of the afternoon.]', "pace")),
    n("dead", "Soana", '''"Sometimes I turn before I remember."
{n}She rests both hands around the head of the stick.{/n}
"I will not tell you a new guardian would be the old Orso returned. You would argue with me, and you would be right about that much."
"Only that much?"
"Do not become greedy."
{n}The answer has some warmth in it. She watches the empty path a little longer.{/n}
"I still want the forest defended. I have not solved what I am willing to do for it. But I will not name the next creature after a friend and pretend I have put things back as they were."
{n}She turns toward you. No footsteps follow her out of the silence.{/n}''', c('[Stay with her beside the water.]', "pace")),
    n("pace", "Soana", '''{n}The shade has moved while you talked. Soana draws the edge of the cloth nearer her leg, then looks at the place you occupy beside her.{/n}''',
      c('"I would like to kiss you, if you still want me closer."', "kiss_offer", requires=("soana.courtship_chosen",), forbids=("soana.bend_hand", "soana.slow_courtship")),
      c('"May I take your hand?"', "hand", requires=("soana.courtship_chosen",), forbids=("soana.first_kiss", "soana.slow_courtship")),
      c('"I am glad we came. I would like another walk."', "friend", requires=("soana.friendship_chosen",)),
      c('"I still need time. I am glad you asked me to come."', "waiting", requires=("soana.courtship_waiting",)),
      c('"I am enjoying this pace. There is no need to hurry it."', "slow", requires=("soana.courtship_chosen",), forbids=("soana.first_kiss", "soana.bend_hand"))),
    n("kiss_offer", "Soana", '''"I do."
{n}She says it before she has time to improve the answer. Then she laughs at her own haste, quietly, and shifts the stick out of the space between you.{/n}
"Come nearer. I would prefer not to fall into the stream attempting a dignified reception."
{n}You turn toward her. She touches your cheek first, with a lightness that makes the roughness of her fingertips more apparent.{/n}
"Still?" she asks.
"Yes."
{n}Her mouth is warm. The first kiss is brief, almost testing. She keeps her hand against your cheek when you draw back, and this time she is the one who closes the small distance.{/n}
{n}Afterward she looks at you with an expression you have not seen before, pleased and disconcerted and unwilling to apologize for either.{/n}
"I had forgotten how much anticipation interferes with breathing."
"Was the anticipation worth it?"
"You are asking me to praise you at a very convenient moment."
{n}She brushes her thumb once along your cheek before lowering her hand.{/n}
"Yes."''', c('[Stay close while the light moves over the water.]', "end", flags=("soana.first_kiss",))),
    n("hand", "Soana", '''{n}She offers it, turning her palm toward you so neither wrist will be bent.{/n}
"You may."
{n}Her thumb moves across your knuckles. She looks out over the water, leaving you free to watch her without needing to answer a challenge.{/n}
"This is pleasant," she says after a while. "I intend to complain about something else later. I thought I should establish the distinction."
"I appreciate the warning."
"Good. We have found one that works."''', c('[Hold her hand without asking for more.]', "end", flags=("soana.bend_hand",))),
    n("friend", "Soana", '''"You may have one. We might even reach a different stone."
{n}She looks at you sidelong.{/n}
"I thought it would be more difficult to sit beside you after you answered me. It is difficult in places. Then something foolish occurs to me, and I want to tell you, and I discover I am still enjoying myself."
"I am too."
"Then we need not ruin a serviceable friendship by insisting it resemble the thing it did not become."
{n}She points toward a snag farther downstream.{/n}
"Next time, that stone. If it is dry. I make no promises to wet clothing."''', c('[Agree to another walk.]', "end", flags=("soana.friendship_kept",))),
    n("waiting", "Soana", '''"Time, then. I brought you here because I wanted the company. I have had it."
{n}She reaches for the stick, tests the ground beside the rock, and decides she is not ready to stand.{/n}
"I would like an answer eventually. I can also survive an afternoon without one."
"I won't pretend I have forgotten the question."
"See that you do not. I am capable of asking it again."
{n}She lets the stick rest. For a little longer, neither of you needs to move.{/n}''', c('[Keep her company without making a promise.]', "end", flags=("soana.pace_unresolved",))),
    n("slow", "Soana", '''"No. There is not."
{n}She looks at your face, then toward the water, allowing the quiet to last.{/n}
"I have spent a great many years telling other people what must happen before nightfall. It is strange to sit here and find that nothing need happen beyond the thing we are already doing."
"Does that trouble you?"
"A little. I am attempting to endure it."
{n}She settles more comfortably on the cloth. The attempt appears to be going well.{/n}''', c('[Enjoy the rest of the afternoon beside her.]', "end", flags=("soana.slow_courtship",))),
    n("end", "Soana", '''{n}When the shade reaches the water, Soana gets to her feet with the help of her stick. You lift the cloth and shake the grit from it before folding it.{/n}
"Leave it on the stone beside the pot when we return," she says. "I shall want it again."
{n}The uphill path is slower. Once, she stops to rest, and you stop with her. She does not fill the pause with an account of why she is entitled to it.{/n}
{n}At the cave she takes the folded cloth from you and puts it where she said. Then she turns back.{/n}
"The lower bend has not ceased to belong to my life. I had been treating it as if it had."
"Shall we return?"
"Yes. When we can."
{n}She keeps the stick beside the entrance. It will be easy to reach.{/n}''', c('[Leave with another visit welcome and the larger questions still open.]', flags=("soana.continuation_kept",))),
], requires=("soana.present_named",))
