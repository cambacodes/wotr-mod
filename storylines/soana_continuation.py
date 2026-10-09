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
        Areas=["0a5654e7dc18f074d9356009d55eb51b"],
        AnswerLists=[ANSWERS], ContactUnit=ACTOR,
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", "soana.opening_kept", *requires),
        forbids=("soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman"),
        delay=delay, optional=True))


s("one_account", "A warning small enough to hear", '"I brought the account. It has a serious weakness."', [
    n("start", "Soana", '''{n}Soana holds out her hand for the folded page. She has cleared a flat stone for it and weighted the corners with pebbles before she reads a word.{/n}
"You might have brought a better one."
"I wanted you to see the weakness before we tried it."
{n}The page describes a watcher's line: loose wooden clappers connected by cord above a narrow crossing. Something large pushing through disturbs the line. Small animals can pass beneath it. There is no spirit in the wood, and nothing capable of defending the crossing once the sound has been heard.{/n}
"A hunter's rattle," {n}she says.{/n} "With more writing."
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
      c('"Nothing holding Orso. We have no way here to release him safely. I want to test a warning that demands no captive."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead", "soana.medallion_pulverized")),
      c('"It cannot take Orso\'s place. A warning at one crossing might still be worth having while you search."', "dead", requires=("soana.bear_dead",)),
      # Polish (Sol CAN): the medallion bitten to dust (SoanaBear/Cue_0023) withers Orso with no BearDead etude.
      c('"It cannot take Orso\'s place. A warning at one crossing might still be worth having while you search."', "dead", requires=("soana.medallion_pulverized",), forbids=("soana.bear_dead",))),
    n("bound", "Soana", '''"A string and two scraps of wood. At least you have brought no beast on a leash."
"I still object to the one you hold."
{n}Her finger presses harder against the paper.{/n}
"He is still out there. Your rattle will not keep the things beyond this forest from devouring it. Do not come back tomorrow boasting that a clever knot has done a guardian's work."
"I won't. Show me a crossing."
"Above the stream. Near enough to hear, far enough to give me more warning than a claw through the cave mouth."
{n}She measures a length of cord against her forearm, stops, and measures again. This time she leaves more slack.{/n}''', c('[Hold the cord while she cuts it.]', "author")),
    n("dead", "Soana", '''"While I search," {n}she repeats.{/n} "You have no objection to that part?"
"Searching is not the same as binding another creature."
"To you. To me it is the work that must be done before the next horror finds us undefended."
{n}She lifts the little wooden pieces, strikes them together, and listens until the sound has died.{/n}
"There is a crossing above the stream. I used to hear larger feet there."
{n}She puts the pieces down separately.{/n}
"We will try your warning. If I hear it in the night, I will know it is not him. I would know that without your invention, of course. Do not look pleased with the lesson."''', c('[Lay out enough cord for the crossing.]', "author")),
    n("author", "Soana", '''"No incantation?" {n}she asks.{/n}
"None in this proposal."
"Good. I told the rulers of Sarkoris to wipe out the mages without mercy. They would not listen. And still the clever people insist that the next spell will repair what the last clever person ruined."
{n}She is addressing the paper, but watching you.{/n}''',
      c('"I cast spells. Judge the ones I cast, as you judge these knots."', "mage", flags=("soana.magic_declared",)),
      c('"A dangerous spell is no cause to slaughter every mage."', "challenge"),
      c('"Judge this proposal first. I have not asked you to trust a spell."', "limited", flags=("soana.argument_deferred",))),
    n("mage", "Soana", '''"Then keep those hands in sight while we tie the knots."
"They carried your water. They cast spells too."
{n}She straightens, chin raised.{/n}
"A mage with a bucket is still a mage. The rulers of Sarkoris listened to smooth tongues like yours. Look what became of them!"
"The bucket was full when I brought it. Judge the spells as closely."
{n}Her gaze drops to the cord you are holding. She takes the loose end and pulls it taut.{/n}
"I have not forgotten the water."
"Or who carried it?"
"Pff! Must I praise you for fetching a bucket? Hold that end. You have let it slip."''', c('[Hold the cord and tie the next knot.]', "end")),
    n("challenge", "Soana", '''"Mercy for the people who tore our country open! An easy sermon when it was not your country."
"Your advice would have killed children who had never cast a spell against anyone."
{n}The twig snaps in her hand. She sets both broken pieces on the stone.{/n}
"And how many children did Sarkoris lose when its rulers spared the mages?"
"I came with a warning made of wood. You brought the mages into it."
{n}She stares at you. Then she turns the page back to the drawing and jabs a finger at the lower knot.{/n}
"Here. Tie it there, and the clapper will strike your leg. I have heard enough foolishness today without you beating it out on yourself."
{n}She holds the paper flat while you move the cord.{/n}''', c('[Move the knot to the marked place.]', "end")),
    n("limited", "Soana", '''"It has one merit. I can cut it with a knife."
"If it fails, we will see where it failed."
"If it fails with a demon on the path, I shall be busy with something besides your drawing. We test it by daylight."
{n}She folds the paper along its old crease and sets her knife on top.{/n}''', c('[Agree to a daylight trial.]', "end")),
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
"Then we take it down. Leave it unwatched, and it will catch some fool by the throat."
{n}You help carry the pieces back to the cave. She leaves them in their bowl.{/n}''', c('[Return when you can stay.]', abort=True)),
    n("watch", "Narrator", '''{n}A small bird lands on the line. The cord sags, but the wooden pieces do not meet. It departs without sounding your warning.{/n}
{n}Soana rests her hands on her knees. A gust travels through the leaves above you. Nothing sounds. The next gust comes lower, dragging a bough across the far end of the line. The clappers knock sharply together.{/n}
"There is your first invader," {n}she says.{/n}
{n}You move the rubbing bough clear and return to the trunk. Minutes pass. Then the clappers strike again, softly this time. Neither of you has seen anything cross.{/n}
{n}The low sound repeats. A reed bends beside the bank, though the leaves above it are still.{/n}''',
      c('[Perception] [Find what is moving before you disturb the crossing.]', check=dict(Skill="SkillPerception", DC=22, Success="found", Failure="missed", CommanderOnly=True), forbids=("soana.watch_found", "soana.watch_missed", "soana.watch_patient")),
      c('[Recall the movement you identified before returning to the line.]', "found", requires=("soana.watch_found",)),
      c('[Return to the evidence left after the boar fled.]', "missed", requires=("soana.watch_missed",)),
      c('[Wait for the movement to repeat. Ask Soana to watch the bank while you watch the line.]', "patient", flags=("soana.watch_patient",), forbids=("soana.watch_found", "soana.watch_missed"))),
    n("found", "Narrator", '''{n}Something dark and bristled shifts beyond the reeds. A young boar has pushed beneath the cord. Its back cleared the line, but a forked twig caught in its bristles is dragging the far end down. The loose twig slips free. The animal snorts and moves out of sight.{/n}
{n}You touch Soana's sleeve and point before she rises. She follows your finger, then settles back.{/n}
"A twig riding a boar. Teach your string to tell them apart, if you are so clever."
{n}You have seen exactly how it happened. The cord itself is clear of the trail.{/n}''', c('[Tell her what caught and what passed beneath.]', "choice", flags=("soana.watch_found",))),
    n("missed", "Narrator", '''{n}You rise to look past the bank. A sharp snort answers you. Something crashes through the reeds away from the crossing, and the line shakes hard enough to send the clappers rattling.{/n}
{n}Soana catches the bowl before your heel tips it down the bank.{/n}
"Now it knows about you as well."
{n}When the movement stops, you find a few stiff bristles on a snag and a forked twig hanging from the cord. The tracks belong to a young boar. You cannot tell whether its body or the twig moved the line first.{/n}
"We will have to watch again," {n}you say.{/n}
"Yes. Sit where you can rise without kicking our belongings into the water."
{n}The second watch is longer. The boar does not return. When you try a loose twig against the line yourself, it catches readily enough to explain the softer noise, though you have missed the chance to watch the animal do it.{/n}''', c('[Set the recovered twig beside the bowl.]', "choice", flags=("soana.watch_missed",))),
    n("patient", "Soana", '''{n}Soana points two fingers at her own eyes, then toward the bank. You remain still. For a while there is nothing to see except a blade of grass quivering against the cord.{/n}
{n}The movement begins again. A boar emerges with a twig caught in its bristles. The twig has hooked the loose end of the line. It pulls free when the animal turns. The wood gives one last tap.{/n}
{n}Soana waits until the boar has gone before speaking.{/n}
"A patient hunter would have had supper. We have an explanation."
"Would you rather have had supper?"
"Both, child. And we have wasted the daylight in which I might have caught supper."
{n}She eases one stiff leg straight, then bends it again. You move the bowl nearer so she need not reach for it.{/n}
"Leave it there. I can manage."
{n}She reaches for it, considers the distance, and leaves it where you put it.{/n}''', c('[Look together at the loose end of the line.]', "choice")),
    n("choice", "Soana", '''"Raise it. Let the smaller creatures crawl under."
"Anything that travels low could crawl under."
"Then lower it, and I can spend every night greeting rabbits with a knife. A fine occupation for Soana the Wise!"
{n}She lifts the line, then lets it sag again. The clappers give a single dry knock.{/n}
"It cannot smell a demon. It cannot shout over the stream. Tell me where to hang it, and spare me another drawing."''',
      c('"Raise it. Sleep through the rabbits. Listen for larger feet."', "high", flags=("soana.line_high",), forbids=("soana.line_daywatch",)),
      c('"Keep it low. Unhook it when you stop listening. It cannot guard you in your sleep."', "low", flags=("soana.line_daywatch",), forbids=("soana.line_high",))),
    n("high", "Soana", '''{n}You shorten the hanging ends and move the line up. Soana crosses beneath it without crouching, then stops and looks back at you.{/n}
"There. I have invaded my own forest undetected."
"Something taller would sound it."
"Something taller with the courtesy to use this path."
{n}She makes you pass through once more, while she listens from the first bend toward the cave. This time she calls back that she heard only the final knock. You move one wooden piece so it strikes more cleanly. She then listens beside the rushing stream while you sound the clappers again. There she misses two knocks out of three.{/n}
"Leave it for now," {n}she says.{/n} "I will hear what it has to say. I shall not sleep with my knife on the far side of the cave."''', c('[Walk back with her.]', "finish")),
    n("low", "Soana", '''{n}You leave the cord at its lower height and tie a loose loop at the near end, so she can take it down without reaching across the crossing.{/n}
"When I stop listening, I unhook it," {n}she says.{/n} "Another knot to untie before I sleep. As if I had too little work."
"It may not be worth keeping."
"I intend to discover that for myself."
{n}She makes you sit in her place while she trips the line. You can hear it plainly. Then you exchange places. She listens from the bend toward the cave while you trip the line again, and calls back that she heard. Beside the rushing stream, she misses two knocks out of three.{/n}
{n}On the return, she unhooks the line and hangs the clappers beside the path. They will wait for someone to listen.{/n}''', c('[Walk back with her.]', "finish")),
    n("finish", "Soana", '''{n}At the cave, Soana sits before she puts the bowl down. Her breath comes hard. She glares at you over the rim.{/n}
"You wanted an account. Now you can write one. Include the boar. It contributed more than your first heading."
"And what did we learn?"
"That I dislike sitting on that trunk. Find me a flat stone next time."
{n}She waits until you have stopped smiling.{/n}
"Also that I can hear the clappers from the bend, and not reliably over running water. Write that plainly. It is the part someone might die from misunderstanding."''', c('[Write down the warning\'s actual limits.]', flags=("soana.watch_kept",))),
], requires=("soana.proposal_kept",))


s("price_of_warning", "The keeper cannot hear everything", '"Has the warning earned its place?"', [
    n("start", "Soana", '''{n}Soana has your page open on the stone again. Beside the drawing she has made several short marks. One has been crossed out so heavily that the paper has worn thin.{/n}
"Can you teach that rattle to hold its tongue?"
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
"Yes. And I left food ungathered to sit beside a stick. I shall be eating late for the sake of your rattle."
{n}She picks a burr from her sleeve and crushes it between two fingernails.{/n}
"You might put that in the account as well."''', c('[Ask what happened to the food gathering.]', "outcome")),
    n("outcome", "Soana", '''"I gathered enough. I was late returning. The pot was cold, and I was hungry, and the forest continued to require attention without consulting my appetite."
{n}She looks toward the cave mouth.{/n}''',
      c('"Orso is still carrying what you bound to him. Our experiment has not reduced that burden."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead", "soana.medallion_pulverized")),
      c('"Without Orso, you are trying to be everywhere. This cannot make one pair of hands enough."', "dead", requires=("soana.bear_dead",)),
      # Polish (Sol CAN): the medallion bitten to dust (SoanaBear/Cue_0023) withers Orso with no BearDead etude.
      c('"Without Orso, you are trying to be everywhere. This cannot make one pair of hands enough."', "dead", requires=("soana.medallion_pulverized",), forbids=("soana.bear_dead",))),
    n("bound", "Soana", '''"No. Your string has given me something else to tend."
"It has shown us how far a warning carries."
"Had I told you at the start, you would have called it an excuse to keep him bound."
{n}She grips the stone's edge. The skin pulls tight over her knuckles.{/n}
"Perhaps. He is still suffering."
"You think I never hear him?"
{n}She bites off the next words. Her hand leaves the stone.{/n}
"Keep your answer. I bound him. I know. Show me how to undo it without leaving the forest to be eaten, and I shall listen. Until then, there is work."''', c('[Ask what she can change about the warning.]', "choice")),
    n("dead", "Soana", '''"You speak as if I had not noticed my own hands."
"What happens when they cannot do the work?"
"What happens when your soldiers cannot hold a wall? Something gets through."
{n}She turns her palms upward, then shuts them into fists.{/n}
"Orso is gone. Shall I name the next beast Orso and call my old friend back? I am not such a fool. Something must stand where I cannot."
"Whatever you find will have its own life."
"And the forest has thousands!"
{n}She snatches up the page and brushes a little dirt from it.{/n}''', c('[Ask what she can actually change today.]', "choice")),
    n("choice", "Soana", '''"You would have me call for help."
"From whom?"
"You tell me! The village has its own mouths to feed. Your soldiers have their war. Shall I shake a tree until a guardian drops out?"
{n}She pulls the page toward herself and scores out the crossing with her twig.{/n}
"I can leave that path unwatched. Hang a smaller line near the cave, or take it down altogether. Somewhere a creature will pass unheard. Your invention has not grown me another pair of ears."''',
      c('"Hang a smaller line near the cave. You cannot tend the forest if you drop from exhaustion."', "near", flags=("soana.watch_near_cave",), forbids=("soana.watch_removed",)),
      c('"Take it down. Keep the account so we do not waste another day on the same mistake."', "remove", flags=("soana.watch_removed",), forbids=("soana.watch_near_cave",)),
      c('"I cannot keep visiting while another binding remains your answer. I will help remove the line, then leave."', "leave", flags=("soana.closed",))),
    n("near", "Soana", '''"You have a gift for making retreat sound like good housekeeping."
"Would you rather call it something grander?"
"I would rather hold the ground."
{n}She rises. You go back to the crossing together, untie the cord, and carry it to a narrow approach within sight of the cave. Here the clappers can hang from a dead branch. No living tree needs to carry the strain.{/n}
{n}Soana tests it herself. The knock is sharp in the sheltered entrance.{/n}
"That I can hear."
"Will you keep it?"
"For now. When I want silence, I shall unhook it. A warning that never shuts up is a poor companion."
{n}She looks sideways at you, one eyebrow raised.{/n}''', c('[Help her make the end easy to unhook.]', "finish")),
    n("remove", "Soana", '''{n}She studies you, the page still held flat beneath her hand.{/n}
"You will take it down yourself?"
"I helped put it up."
"Good. The far knot has tightened. You may enjoy undoing your own excellent work."
{n}You do not enjoy it. Soana watches your struggle, then passes you her awl without comment. The point loosens the cord enough to pull it free.{/n}
{n}Back at the cave, she coils the line and keeps the clappers in their bowl. She does not throw them into the fire.{/n}
"Useful wood," {n}she says when she catches you looking.{/n}
"And an account?"
"A shorter one, now that we know how it ends."''', c('[Amend the account with her.]', "finish")),
    n("leave", "Soana", '''"Then take your string down before you go. I will not climb that bank to undo your knots."
{n}You dismantle the line together. She keeps the wood and gives you back the page, with all her corrections still on it.{/n}
"I have not changed my mind."
"I know."
"The clappers could still warn someone. Use them where they can be heard."
{n}She winds the cord around her hand and returns to the cave. You step aside to let her pass.{/n}''', c('[End the private visits.]')),
    n("finish", "Soana", '''{n}Soana adds one final sentence beneath the drawing. She pushes the page toward you before laying down the twig.{/n}
"A watcher must eat and sleep. Even this one."
{n}The last words are cramped against the edge of the page.{/n}
"Write smaller next time."
"There is room on the back."
"I have finished."
{n}She folds the page and puts it away. Then she reaches for a little covered pot you have not seen her open before.{/n}
"Come next time without a proposal. I have food that will spoil while you wait for a victory worth feasting over. We shall eat it anyway."''', c('[Accept an afternoon without another experiment.]', flags=("soana.warning_reckoned",))),
], requires=("soana.watch_kept",))


s("ordinary_feast", "A feast for an ordinary afternoon", '"You said something would spoil if we waited for an occasion."', [
    n("start", "Soana", '''{n}Soana takes the cover off the pot. Inside is a little honey, thick enough to cling to the spoon. A dish of tart berries waits beside it.{/n}
"I had hoped for sweeter fruit. The fruit had other ambitions. Sit down."
{n}She has put a folded cloth on a flat stone. You sit beside her, with the dish of berries between your knees.{/n}
"No new plans?" {n}she asks.{/n}
"You told me not to bring one."
"It is a relief to discover you can follow an instruction without first enlarging it."
{n}She gives you a spoon and takes the smaller one herself. The first berry draws her lips tight. She dips the next in more honey.{/n}
"The bees did their work. I shall blame the bushes."''',
      c('[Taste a berry before adding honey.]', "sour"),
      c('"I trust your judgment." [Take enough honey the first time.]', "sweet"),
      c('"I cannot stay today. Keep some for yourself."', abort=True)),
    n("sour", "Soana", '''{n}She watches your face with undisguised interest.{/n}
"Sour enough for you?"
"That would wake the dead."
"It has certainly woken you."
{n}Her laugh comes out full and rough. She sets her spoon down before it spills, then pushes the honey toward you with a finger.{/n}
"You could have warned me."
"I did. You went sniffing after it anyway, like a young fox at a wasp nest."''', c('[Add honey and let her enjoy being right.]', "song")),
    n("sweet", "Soana", '''"Trust my judgment, do you? Hold out your spoon."
"About berries. Don't grow ambitious."
{n}She sets a particularly small berry on it and dribbles honey over the top.{/n}
"Such a little thing to frighten a commander. Open your mouth."
{n}You eat it. The honey is almost enough to conceal the sourness.{/n}
"Your judgment wants more honey."
"Your tongue wants sweeter work. Here."
{n}She passes the pot back, smiling into her own dish.{/n}''', c('[Move the dish where both of you can reach it.]', "song")),
    n("song", "Soana", '''{n}For a while you eat. A bee finds the rim of the honey pot. Soana waits for it to move before she replaces the cover.{/n}
{n}Then she begins humming. The tune climbs as if it intends to become solemn, loses its footing, and comes down again in a quick run of notes.{/n}
"That does not sound like a sacred song."
"It is not."
{n}She hums the first notes again, watching you over her spoon.{/n}''',
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
"You reached the end. The trees have not fled. Try it again."
{n}She adds words about a foolish young man and an exceptionally well-dressed goat. You lose the tune again, this time because you laugh before the end.{/n}
"A reasonable place to stop," {n}she says.{/n} "The goat usually receives the applause."''', c('[Ask where she used to sing it.]', "festival")),
    n("listen", "Soana", '''{n}She lifts one eyebrow, but keeps the tune going. Without words, its little hesitation becomes funnier each time she repeats it. You begin to recognize where the singer is expected to linger and where the listener is expected to laugh.{/n}
{n}At the end she gives the final phrase an outrageous flourish. It exhausts her breath and leaves her shaking her head at herself.{/n}
"I used to do that better."
"I liked it."
"So did I. That is why I kept the foolish ending."
{n}She rests for a moment before reaching for her spoon again.{/n}''', c('[Ask where she used to sing it.]', "festival")),
    n("festival", "Soana", '''"At the Sun Festival, away from whoever was trying to conduct a solemn rite. Hundreds of voices in the Meadow of the Spirits, and the forest singing back! You should have heard it."
{n}She sets the covered honey pot beside her knee.{/n}
"There were flowers underfoot, water in the holy spring. Mead when night fell, and young fools jumping the bonfire to catch one another's eye. I remember one who drank so much he was sick behind a bush."
"You miss him too?"
"I miss having enough mead to waste on such a fool. I sent him farther from the spring."
{n}She laughs, wiping a drop of honey from the spoon with her thumb.{/n}
"Sarkoris could afford a few fools then. We had more than ashes to sing over."''',
      c('"Were you ever one of those fools?"', "foolish"),
      c('"What would you bring here from that festival?"', "choose")),
    n("foolish", "Soana", '''"Who was going to forbid me?"
"The song, then?"
"Among other things. I once shouted down a singer through an entire chorus. He had the words wrong. I knew the older ones."
"Did you?"
"Older words. A different song."
{n}She fixes you with a stern look.{/n}
"Close your mouth before a bee flies into it."
"I shall remember this next time you correct me."
"Remember it while you do the work again. You will have plenty of time."''', c('[Finish the last berries together.]', "end")),
    n("choose", "Soana", '''"Another singer to begin before someone came tugging at my sleeve. Soana the Wise, settle our quarrel! Soana the Seer, tell us whether it will rain! They could see the clouds as well as I could."
"Shall I begin a song?"
"Do you know one? I have fed you honey. Do not repay me with a crow's squawking."
{n}You draw breath. She beats you to the first note of the little falling phrase.{/n}
"Too late. Catch up."
{n}She taps the spoon against the dish again, watching your mouth as she sings.{/n}''', c('[Finish the last berries together.]', "end")),
    n("end", "Soana", '''{n}Soana holds the dish while you scrape the last honey from its edge. She tips it toward your spoon, then checks the bottom herself.{/n}
"There. The berries have found a use."
"And the afternoon?"
"There is some of it left. Do not start boasting yet."
{n}She sets the empty dish aside. Her knee brushes yours as she settles back on the cloth.{/n}
"Stay until the light changes. I have fed you. I am not chasing you off."''',
      c('[Stay beside her until the light changes.]', flags=("soana.feast_kept",)),
      c('"I enjoyed this. I have to go while there is still light."', flags=("soana.feast_kept",))),
], requires=("soana.warning_reckoned",))


s("name_between", "The name she keeps", '"I have come for another afternoon."', [
    n("start", "Soana", '''{n}Soana has spread a piece of cloth over the stone where you ate. She lifts a corner, finds a seed beneath it, and flicks it toward the cave mouth.{/n}
"Sit. The honey is gone. You will have to endure the company unsweetened."
{n}You sit. She folds the cloth once, then shakes it out and folds it again.{/n}
"You heard me speak of Corven. Do not start looking for a grave I never showed you."
{n}She drops the folded cloth onto the stone between you.{/n}''',
      c('[Sit and listen.]', "marriage"),
      c('"I would like to hear it when I can stay. Not in a hurried visit."', abort=True)),
    n("marriage", "Soana", '''"Corven is my husband. He put a wreath on my head at the Sun Festival. Flowers from Orso's footsteps. I became his wife. The flowers are dust now. I have never called that a burial."
{n}She looks straight at you, her chin jutting.{/n}
"I do not know whether he lives. No grave. No last message. No farewell between us. You will not hear me invent one."
{n}She plants both hands on her knees.{/n}
"And still I watch the path when you are late. Curse you, I have work enough without listening for your boots."
"Shall I stay away?"
"No. Come again. Sit close. I want you here, and I will not blame the honey for it."''',
      c('"I want to court you. I heard what you said about Corven."', "court", flags=("soana.courtship_chosen",), forbids=("soana.friendship_chosen", "soana.courtship_waiting")),
      c('"I shall come as your friend. I will not court you while you may still have a husband."', "friend", flags=("soana.friendship_chosen",), forbids=("soana.courtship_chosen", "soana.courtship_waiting")),
      c('"Ask me another day. I want another afternoon with you first."', "wait", flags=("soana.courtship_waiting",), forbids=("soana.courtship_chosen", "soana.friendship_chosen")),
      c('"Then this is my last private visit. Farewell, Soana."', "leave", flags=("soana.closed",))),
    n("court", "Soana", '''"Then come as a suitor. No grand speeches. I have heard enough of those to outlive Sarkoris."
{n}She lifts the folded cloth from between you and lays it on her other side.{/n}
"And no tales about time burying Corven for me. If he is dead, he is dead. The years cannot tell me where he lies."
"I heard you."
"Good. Sit nearer. I want your hand."
{n}She holds out hers, palm upward. The fingers tremble, but she keeps them extended and fixes you with a glare.{/n}
"Do not stare at it as though I had shown you a new species of root."''',
      c('[Take her offered hand.]', "hand", flags=("soana.hand_taken",)),
      c('"Another afternoon first. I shall come, but keep your hand for now."', "slow")),
    n("hand", "Soana", '''{n}Her fingers close around yours. She presses once, then turns your joined hands until neither wrist is bent.{/n}
"There. You grip a hand better than you tie a knot."
"Another thing for the account?"
"Write it down and I shall burn the page."
{n}Color rises in her weathered face. She keeps your hand against her knee.{/n}
"No, child. You do not get it back yet."
{n}You sit together until a draft reaches the stone. She releases your hand to shift nearer the cave wall, then catches your sleeve and draws you beside her.{/n}''', c('[Stay beside her.]', "end")),
    n("slow", "Soana", '''{n}She curls her fingers into her palm and lowers her hand.{/n}
"Another afternoon, then. A hare would have reached me sooner."
"I shall come."
"See that you do. The last berry will not wait forever for a bird to swallow it."
{n}She shifts nearer the cave wall, out of the draft, and pats the stone beside her.{/n}
"Come away from the entrance. You can sit here without taking hold of me. Though I shall still call you a fool if you freeze."''', c('[Take the place beside her.]', "end")),
    n("friend", "Soana", '''{n}Her mouth tightens. She gives the folded cloth a sharp shake.{/n}
"Friends, then. You have picked a thorny one."
"I shall still come."
"Then come. I have a tongue as well as a hand you will not take."
{n}She folds the cloth again and sets it beside her.{/n}
"And bring something to talk about. I refuse to supply every word while you sit there looking sorry for me."
"You would never let me."
"You have learned that much. Sit. There is daylight left."''', c('[Sit with her as a friend.]', "end")),
    n("wait", "Soana", '''"Another afternoon? The first has already eaten all my honey. You had better like sour berries."
"I liked the company."
"Then we shall see whether it holds your tongue again."
{n}She presses the folded cloth flat beneath her palms.{/n}
"I would rather have had your answer. I shall ask again."
"I know."
"For now, tell me what you saw on the path. If you say a tree, I shall put you outside to count the rest."
{n}You turn toward the light at the entrance. She leans forward when you begin to speak.{/n}''', c('[Tell her what you saw on the path.]', "end")),
    n("leave", "Soana", '''"Then go. Better now than after you have worn a hollow in that stone."
{n}She rises with one hand against the wall. You stand and step aside.{/n}
"Take the account. It is yours."
{n}She gives you the folded page. Its corners are worn, and a smear of charcoal crosses the crease.{/n}
"I shall remember these afternoons."
"So shall I. You made me correct enough of your knots."
{n}She turns to the stone and flicks another seed from beneath the cloth. It lands by your boot.{/n}''', c('[End these private visits.]')),
    n("end", "Soana", '''{n}Outside, the wind turns the leaves, showing their pale undersides. Soana watches until the gust has passed.{/n}
"The lower bend. Where the water leaves the stones. I have not sat there in too long."
"Shall I come with you?"
"Why else would I tell you? The water has not changed its course. You could have found it yourself."
{n}She gathers up the folded cloth and shakes a little grit from its hem.{/n}
"Next time, we walk there. Bring no proposal. I want to sit without finding fault with a drawing."''', c('[Agree to walk with her.]', flags=("soana.present_named",))),
], requires=("soana.feast_kept",))


s("lower_bend", "A place she has not lost", '"You asked me to walk to the lower bend."', [
    n("start", "Soana", '''{n}Soana is ready when you arrive. She has a walking stick and a folded cloth beneath one arm. She sees you notice the stick.{/n}
"A branch, child. The ground has grown troublesome. This one has the sense to hold still when I lean on it."
{n}She tests the end against the stone, then turns toward the path.{/n}''',
      c('[Walk beside her, leaving room for the stick.]', "line"),
      c('"I cannot stay for the walk today."', abort=True)),
    n("line", "Narrator", '''{n}At the cave mouth she pauses to deal with the warning experiment's remains.{/n}''',
      c('[Wait while she unhooks the warning beside the cave.]', "kept", requires=("soana.watch_near_cave",)),
      c('[Watch her set the bowl of unused clappers farther inside.]', "removed", requires=("soana.watch_removed",))),
    n("kept", "Soana", '''"Let the wind rattle it. I will not come running uphill to greet a gust."
{n}She hangs the slack loop over the dead branch. The wooden pieces rest against each other without striking.{/n}
"It has warned me about two visitors with feathers and one with hooves. No demons have presented themselves for our convenience."
"It is still an experiment."
"Yes. One I can leave hanging on a branch. That is its finest quality."''', c('[Follow the path down to the water.]', "walk")),
    n("removed", "Soana", '''"The cord will make a better carrying strap. I have not decided what the wood will become."
"It could remain wood for a while."
"An extravagant idea. I shall consider it."
{n}She moves the bowl out of reach of the entrance and retrieves her stick.{/n}
"There. It can sit in its bowl. We are going down to the water."''', c('[Follow the path down to the water.]', "walk")),
    n("walk", "Narrator", '''{n}The lower bend is close enough that you can still make out the pale stone above the cave when the trees open. Soana takes the path around a steep patch, testing the earth with her stick before each step.{/n}
{n}At the water she spreads the cloth on a broad dry rock. She lowers herself onto it, rests the stick within reach, and lets out a breath she has held through the last few steps.{/n}
"Still dry. Still flat. All these days wasted sitting in the cave."
{n}The water moves around a stone worn hollow at its center. Fallen leaves turn in the little basin before spilling over the far edge.{/n}''',
      c('"Tell me what you used to do here."', "memory"),
      c('[Sit beside her and watch a leaf escape the hollow stone.]', "water")),
    n("memory", "Soana", '''"Mended things. Avoided people who wished to be advised. On one memorable afternoon, fell asleep and left a very important visitor to consult the entrance of an empty cave."
"What did you tell them?"
"That the forest had required my attention. It had. I had been snoring in it."
{n}She laughs, then grows thoughtful.{/n}
"Do not go making a legend of it. Soana the Seer was asleep, and the visitor had to wait. That is all."
"I shall spare the visitor the telling."
"Good. There may be hope for your accounts yet."''', c('[Look toward the trees beyond the stream.]', "outcome")),
    n("water", "Soana", '''{n}A leaf turns twice in the hollow, catches against another, and stays there. Soana watches with an increasingly disapproving expression.{/n}
"You would think it had found a comfortable home."
"Perhaps it has."
"In a puddle, with someone else's leaf sitting on it?"
{n}The next little surge lifts both leaves free. They tumble away together.{/n}
"Off it goes. A leaf takes advice better than most visitors."
{n}She leans back on one hand. The other lies loose in her lap.{/n}''', c('[Look toward the trees beyond the stream.]', "outcome")),
    n("outcome", "Soana", '''{n}A branch creaks somewhere beyond the water. Soana's head turns toward it before the sound has ended. She waits, listening, until the forest falls quiet again.{/n}''',
      c('"You are listening for Orso."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead", "soana.medallion_pulverized")),
      c('"It still sounds as though something large might come down that path."', "dead", requires=("soana.bear_dead",)),
      # Polish (Sol CAN): the medallion bitten to dust (SoanaBear/Cue_0023) withers Orso with no BearDead etude.
      c('"It still sounds as though something large might come down that path."', "dead", requires=("soana.medallion_pulverized",), forbids=("soana.bear_dead",))),
    n("bound", "Soana", '''"Yes. He is still out there."
{n}She keeps looking into the trees.{/n}
"You have not frightened the thought away by sitting beside me. Nor will I spend the afternoon reciting it for you."
"I still want another answer for him."
"Then find something better than a wooden rattle. Bring me a method worth trying, and I shall examine it."
{n}She turns back toward you, both hands on the head of her stick.{/n}
"I will not undo the binding because the water sings prettily today. Those trees will still be here after we go back to the cave. Something must guard them."
{n}She plants the stick beside her knee and settles on the cloth.{/n}''', c('[Sit beside her and look toward the trees.]', "pace")),
    n("dead", "Soana", '''"Sometimes I turn before I remember."
{n}She grips the head of her stick with both hands.{/n}
"A new guardian would be a new creature. I know that. You can keep your lecture."
"Only that one?"
"Do not become greedy."
{n}She watches the empty path, rubbing a rough patch of bark beneath her thumb.{/n}
"The forest must be defended. I have not found how. But I will not give another beast his name and pretend my friend has come back. Let it have its own name, whatever it is."
{n}She turns toward you. A leaf falls onto the path behind her.{/n}''', c('[Stay with her beside the water.]', "pace")),
    n("pace", "Soana", '''{n}The shade has moved while you talked. Soana draws the edge of the cloth nearer her leg, then looks at the place you occupy beside her.{/n}''',
      c('"I want to kiss you."', "kiss_offer", requires=("soana.courtship_chosen",), forbids=("soana.bend_hand", "soana.slow_courtship")),
      c('"Give me your hand."', "hand", requires=("soana.courtship_chosen",), forbids=("soana.first_kiss", "soana.slow_courtship")),
      c('"I am glad we came. I would like another walk."', "friend", requires=("soana.friendship_chosen",)),
      c('"Ask me again another day. I am glad I came."', "waiting", requires=("soana.courtship_waiting",)),
      c('"No kisses today. I want to sit here with you awhile."', "slow", requires=("soana.courtship_chosen",), forbids=("soana.first_kiss", "soana.bend_hand"))),
    n("kiss_offer", "Soana", '''"Yes. Come here."
{n}She shifts the stick to her other side and catches the front of your clothing.{/n}
"Nearer. I will not tumble into the stream reaching for that mouth."
{n}You turn toward her. Her rough fingers cup your cheek; she draws you down and kisses you. Her lips are warm, and she keeps her grip when you lift your head, pulling you back for a second kiss.{/n}
"There. You have silenced me. A rare feat."
"For how long?"
{n}She laughs against your mouth, then sits back. Her fingers still hold your collar.{/n}
"Not long enough for you to grow proud of it."
"Was it worth the wait?"
"Ask again and I shall set you to counting trees."
{n}Her thumb brushes the corner of your mouth. She draws you close once more before letting go.{/n}''', c('[Stay close while the light moves over the water.]', "end", flags=("soana.first_kiss",))),
    n("hand", "Soana", '''{n}She turns her palm upward. You take it, and her fingers close hard around yours.{/n}
"About time."
{n}Her thumb rubs across your knuckles. She looks out over the water, keeping your hand on her knee.{/n}
"If I scold you on the way back, do not go sulking. This has not improved your knots."
"A useful warning."
"One your ears can hear, at least."
{n}She pulls a splinter from your sleeve with her free hand and tosses it into the stream.{/n}''', c('[Hold her hand and watch the stream.]', "end", flags=("soana.bend_hand",))),
    n("friend", "Soana", '''"Another walk? We might even reach a different stone."
{n}She looks at you sidelong, then points her stick toward a snag farther downstream.{/n}
"That one. Next time. You can test it first."
"For what?"
"Wetness, child. I shall trust my friend with that much wisdom."
{n}She nudges your boot with the end of the stick.{/n}
"You can still argue with me there. I have not used up every foolish thing you say."
"Nor I every scolding."
"Then bring dry clothing. I will not spend the walk listening to you squelch."''', c('[Agree to another walk.]', "end", flags=("soana.friendship_kept",))),
    n("waiting", "Soana", '''"No answer yet? You have had time to watch a leaf travel half the stream."
{n}She takes up the stick, tests the ground beside the rock, then lays it across her knees.{/n}
"Stay where you are. I did not drag you down here to watch you climb back up."
"I have not forgotten what you asked."
"See that you do not. I have a tongue, and I shall use it again."
{n}She shifts the cloth beneath her and tips her face toward a patch of sunlight.{/n}
"When the shade reaches the water, we go. Until then, you can tell me another tale."''', c('[Stay and tell her another tale.]', "end", flags=("soana.pace_unresolved",))),
    n("slow", "Soana", '''"Then sit. Keep your mouth for talking."
{n}She tucks the cloth beneath her hip and stretches one leg toward the sun.{/n}
"I have spent half my life sending people running before nightfall. Now I have caught a commander on a rock. Your soldiers must wonder where you have gone."
"They can wait."
"So can the trees, for an afternoon."
{n}She lifts your sleeve out of the damp at the edge of the stone and drops it across your knee.{/n}
"There. I have kept you from drowning by the cuff. Already a useful walk."''', c('[Enjoy the rest of the afternoon beside her.]', "end", flags=("soana.slow_courtship",))),
    n("end", "Soana", '''{n}When the shade reaches the water, Soana gets to her feet with the help of her stick. You shake the grit from the cloth and fold it.{/n}
"On the stone beside the pot when we get back. I shall want it again."
{n}The uphill path takes longer. She stops beneath a tree, leaning on the stick. You stop beside her until she starts uphill again.{/n}
{n}At the cave she takes the cloth and sets it beside the pot. Then she turns back.{/n}
"Next time, the lower bend again. That stone was dry. I will not trust every rock in the stream because one behaved itself."
"Another afternoon, then."
"Yes. Come before the sun slips behind the trees."
{n}She leaves the stick beside the entrance, its worn handle within reach.{/n}''', c('[Leave the stick at the entrance and return another afternoon.]', flags=("soana.continuation_kept",))),
], requires=("soana.present_named",))
