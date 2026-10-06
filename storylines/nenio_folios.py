"""Nenio: the spine between her entry and her question (the dictation sessions, the Abyss, page one), and the beats after.

The Commander takes her dictation for the Encyclopedia Golarionnica, and every time she reaches the word "Commander" she says
"leave a space". Each session engages a canon anchor of hers:
- the follower who walks behind her "writing down my deepest thoughts" (CompanionDialogues/Nenio/Cue_0008); the Encyclopedia,
  "one hundred volumes" (Cue_0106), one percent written (Cue_0109); "your name is irrelevant" (Cue_0052);
- her examination of the Commander, which found "something of the trickster in you" (Cue_0161), and her fondness for testing
  whether the Commander bites (Cue_0123, Cue_0133);
- "names I am happy to remember... Areelu Vorlesh!" (Cue_0077), "the experiment of the century" (Cue_0080), and the dead as
  "unfortunate but unavoidable sacrifices made at the altar of science" (Cue_0085);
- "an experiment of a... personal nature" (Cue_0186); point five (Answer_0353); her universal gossip slips (Cue_0288, Cue_0321);
- the kitsune she forgot she was (FoxReveal/Cue_0031, Cue_0032) and the tail "you can comfortably wrap around you as you go to
  sleep" (FoxReveal/Answer_0071);
- the Nameless Ruins and the entity that "can easily unveil secrets" (FoxReveal/Cue_0049), her fear that it will be her
  "triumph" or her "fiasco" (Cue_0397), and "tell all of Golarion about the heroic death of its greatest daughter" (Cue_0398);
- "Now or never — that's my motto!" (Cue_0254); "Unless I forget." (Cue_0066, Cue_0141, Cue_0163).
Chapter 4 is the Abyss: while she travels in the company the sessions come at a rest; while she waits in Drezen, she writes.
Acknowledgments of other women are in Nenio's voice only; no scene between partners.
"""
from story_format import c, scene
from storylines.nenio_trickster import (ARCH_AGREED, ARCH_DEAD, ARCH_TRICK, CLOSED, COMMITTED, FOX_REVEALED, FRIEND_DONE,
                                        ENIGMA_RESOLVED, WHO_SILENT, KENABRES_SAID, HUB, UNIT, REL, TOLD_BITE, DEBT_DEFAULTED, DEBT_SETTLED,
                                        MANUSCRIPT, NAME_GONE, P, RECREATED, RIDDLE_DONE, SCRIBE, STARTED, UNREMEMBERED,
                                        SENT_AWAY, VISITOR, F, KENABRES_LIED, KENABRES_SECRET, KENABRES_TOLD, OWES,
                                        meet, nar, nen, twin_ids, visit, KENABRES_PENDING,
                                        POETRY_FAILED, GOSSIP_PREPARED, GOSSIP_UNIVERSAL, BROUGHT_SAFE,
                                        RECRUITMENT_REFUSED, FRIEND_SKETCH, FRIEND_TONGUE, FRIEND_CREDIT, FRIEND_REFUSED)

SCENES = []

FIRST = F + "dictation"
FIRST_IDS = (FIRST,)
DEMONS = F + "demons"
ARCHITECT = F + "architect"
PULSE = F + "pulse"
TAIL = F + "tail"
SLIPS = F + "slips"
LAMP = F + "abyss.lamp"
SHOULDER = F + "abyss.shoulder"
REPORT = F + "drezen.report"
PAGE_ONE = F + "page_one"
VOLUME_ONE = F + "volume_one"
LONG = F + "longitudinal"
BOAST = F + "dictation.boast"
LIED_PULSE = F + "demons.lied"
KISSED_EARLY = F + "pulse.kissed"
FINISHED_SENTENCE = F + "abyss.finished_sentence"
MORNING_AFTER = P + "morning_after"


def m(id, title, entry, nodes, requires, **kw):
    meet(id, title, entry, nodes, requires, into=SCENES, **kw)


def v(id, title, nodes, requires, **kw):
    visit(id, title, nodes, requires, into=SCENES, **kw)


def hub4(id, title, entry, nodes, requires, forbids=(), delay=24, **extra):
    """Sol r1 (COX, ledger R2-5): Nenio travels with the company in the Abyss, so her Chapter 4 beats are on her own hub,
    in person, not rest deliveries."""
    SCENES.append(scene(id, title, "Nenio", 4, entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, id, VISITOR, *forbids), delay=delay, last=4, optional=True, Relationship=REL,
                        Chapters=[4], AnswerLists=[HUB], ContactUnit=UNIT, **extra))


# --- Chapter 3 (and on): the first session. She conscripts a scribe, and leaves a space. -------------------------------------

m(FIRST, "A follower with a pencil", '"What are you writing?"', [
    nar("open", '''{n}Nenio has turned @DESK@ into a desk and is bent over it, glaring at a sheet of paper from very close, the way you would glare at somebody who owed you money. Several more sheets are pinned under a stone, and the stone is a demon's knucklebone, and it has a label on it.{/n}''',
        c("Continue", "nothing")),
    nen("nothing", '''"Nothing! That is precisely the problem. I am writing nothing." {n}She stabs the sheet with her pencil.{/n} "Yesterday I observed a vrock moult. Nobody in the history of scholarship has observed a vrock moult; they are too busy being eaten by the vrock. I wrote down everything. And today I cannot read a single word of it."
"My handwriting has always been a safeguard against plagiarism. It is now also a safeguard against me."''',
        c("Continue", "encyclopedia")),
    nen("encyclopedia", '''"You understand the scale of the difficulty. The Encyclopedia Golarionnica will be published in one hundred volumes, one thousand pages each, plus addenda. I have finished one percent of it." {n}She holds up one finger, in case you had not grasped how small one percent was.{/n}
"At my present rate of legibility I shall finish the rest shortly after the sun goes out." {n}She looks at you with sudden, horrible interest.{/n} "You write dispatches. I have seen them on the command table. Every letter separate. Every line straight. It is almost vulgar."''',
        c('"No."', "no"),
        c('[Flirt] "What does the scribe get?"', "gets"),
        c('"I command an army, Nenio."', "army")),
    nen("no", '''"You have not heard the question." {n}She sounds genuinely hurt on behalf of the question.{/n} "The question is this: would you like to be present at the greatest scholarly undertaking of the modern age, and have your hand, your actual hand, preserved in the libraries of Absalom for a thousand years? The answer is yes. I have saved you the effort of saying it."''',
        c("Continue", "terms")),
    nen("gets", '''"The scribe gets to walk behind me, writing down my deepest thoughts, and to admire the profundity of my intellect at close range." {n}She considers.{/n} "Also I will stop examining your teeth. For a time."''',
        c("Continue", "terms")),
    nen("army", '''"Yes, and the army is going to be over by the end of the decade one way or the other, and the Encyclopedia is not. Think of your posterity." {n}She waves at the Worldwound's glow on the horizon as if it were an unpromising student.{/n} "Besides, most of what I am writing is about that. You are commanding the subject of my research. It would be absurd not to take notes."''',
        c("Continue", "terms")),
    nen("terms", '''{n}She thrusts the pencil at you, point first, and a clean sheet after it.{/n}
"We begin with something easy. The letter C. 'Crusade, the Fifth.'" {n}She clasps her hands behind her back and begins to walk, three steps, turn, three steps.{/n} "Composition: knights of Mendev, the paladins of several gods, a large number of mercenaries, a smaller number of lunatics, and the people who had nowhere else to go. Morale: variable. Smell: considerable. Commander of the..."''',
        c("Continue", "space")),
    nen("space", '''{n}She stops walking. "Leave a space," she says.{/n}
"Why?" {n}She answers the question you have not yet asked.{/n} "Because on the grand scale of world history your name is irrelevant. I rank names below observations, and I have made a point of forgetting it. When it becomes relevant, it will be filled in. Leave a space. Ruled. Neat. The width of three fingers." {n}She holds up three fingers.{/n} "A name the size of the Commander's will need three fingers, I think. Possibly four, by the end."''',
        c("Continue", "friend", requires=(FRIEND_DONE,)),
        c("Continue", "go_on", forbids=(FRIEND_DONE,))),
    nen("friend", '''{n}She pauses, and adds, severely:{/n} "And this is not friendship. Friendship is concluded. I have written my conclusion; it is the most foolish of all occupations. This is employment. Employment has a different list, and nothing on it involves underwear."''',
        c("Continue", "go_on")),
    nen("go_on", '''"Next. 'Crusade, the Fifth, its equipment.' Write quickly, I am about to be brilliant and I cannot guarantee it will last."''',
        c("[Leave the space, ruled and neat, and write on.]", flags=(SCRIBE, STARTED)),
        c('[Write something in the space anyway] "The Commander, greatest trickster of the modern age."', "boast",
          mythic="Trickster", flags=(SCRIBE, STARTED, BOAST))),
    nen("boast", '''{n}She reads it upside down, because she can read your hand from any angle, which is the whole point of you. Her nose wrinkles.{/n}
"That is not a name. That is a boast. It is also a misappropriation of my own title." {n}She reaches for the sheet to strike it, and stops, and takes her hand back.{/n} "No. It stays. It is evidence: a specimen of the scribe's vanity, collected in the wild on the first day. Those are rare." {n}She sniffs.{/n} "As a footnote. In very small type. Next."''',
        c("[Write on.]")),
], requires=("trickster",), forbids=(SCRIBE,), delay=0, places=("hub",))


m(DEMONS, "Demons, by smell", '"Ready when you are. Which letter?"', [
    nen("open", '''"D. Demons, classification of." {n}She is sitting on @SEAT@ with her knees drawn up and her notes spread around her on the ground like the pieces of a broken plate.{/n}
"The priests classify them by the layer of the Abyss they come from, which is useless, because nobody can get to the layers to check. The Pathfinders classify them by what they are called, which is worse, because demons lie. I classify them by smell. Smell does not lie. Write."''',
        c("Continue", "smells")),
    nen("smells", '''"Babau: vinegar, and something like a tannery. Vrock: wet feathers and old graves; the graves may be circumstantial. Brimorak: burnt hair. Their own. Hezrou: I decline to describe the hezrou; the students of Absalom are young and have their whole lives ahead of them." {n}She pauses to let you catch up.{/n}
"Succubus: expensive. Which is suspicious in itself. Nothing in the Worldwound should smell expensive. I have written a note to investigate where they get it."
"Mark the Worldwound's edge as 'variable'. At the edge everything smells of everything else. It is the closest thing to a scientific description of the place that I have."''',
        c('"And people? What do people smell of, by your system?"', "people"),
        c('"You\'ve been this close to all of them?"', "close")),
    nen("people", '''"Irrelevant. People are not demons. Mostly." {n}She leans in without warning and sniffs your collar, briskly, like a cook testing milk.{/n} "Ink. Steel polish. Somebody else's campfire. And something I have no category for, which is annoying." {n}She sits back.{/n} "Do not write that down."''',
        c("Continue", "test")),
    nen("close", '''"Close enough to measure the teeth. Further research would require a better boot." {n}She lifts one foot.{/n} "A hezrou could swallow this without chewing. Its jaw would still have room for my ankle. I prefer to calculate that from the outside."''',
        c("Continue", "test")),
    nen("test", '''{n}She turns a page, and her eyes narrow, and she looks up at you over it in a way that you have learned means an experiment is coming.{/n}
"The whole army calls you the trickster now. Rejecting universal rules, a distinct unwillingness to choose between good and evil, and so on; the stories get worse every time I hear them. An army is a very poor instrument. I want to test its conclusion myself." {n}She holds out her hand, palm up.{/n} "Wrist. Then tell me a lie. I want to see what your pulse does."''',
        c('[Lie to her] "I\'ve never once cheated at cards."', "lied", flags=(LIED_PULSE,)),
        c('[Tell her the truth, and say it\'s a lie] "I think you\'re the most interesting person in this army."', "truth"),
        c('"You first."', "you_first")),
    nen("lied", '''{n}Her fingers find the pulse and settle. She counts under her breath, and frowns, and counts again.{/n}
"No change." {n}She is quiet a moment.{/n} "That is either very bad or very interesting. A normal person's heart jumps when they lie. Yours sat there like a cat in a window." {n}She writes something.{/n} "I shall record it as very interesting. If I record it as very bad I shall have to do something about it, and I have a war to classify."''',
        c("Continue", "hand")),
    nen("truth", '''{n}Her fingers find the pulse and settle. She counts under her breath, and stops, and looks at you, and counts again.{/n}
"That was not a lie." {n}Flatly.{/n} "Your pulse did not do what it does when you lie. It did something else. It went up." {n}She takes her hand back and writes very fast, and does not show you what.{/n} "Inconclusive. I shall need a larger sample. Next."''',
        c("Continue", "hand")),
    nen("you_first", '''"I do not lie. It is inefficient; you have to remember what you said." {n}She considers.{/n} "I forget things instead. It comes to the same result and takes less effort." {n}She presses two fingers to your wrist anyway and holds them there, eyes on the sky, counting.{/n} "Your pulse is up. You have not said anything. That is interesting too."''',
        c("Continue", "hand")),
    nen("hand", '''{n}She has not let go of your wrist. She notices this at the same moment you do, and looks at her own hand as if it had wandered off without asking.{/n}
"The instrument is still attached," {n}she says.{/n} "It is taking a second reading. Ignore it." {n}She lets go, after the second reading, or perhaps the third.{/n} "Back to demons. 'Nabasu: wet stone and a sort of hunger.' Write it. And under 'Crusade, Commander of the', leave the space. I noticed you were about to fill it in. Do not."''',
        c("[Leave the space.]")),
], requires=(SCRIBE,), delay=24)


m(ARCHITECT, "Names worth remembering", '"Which letter today?"', [
    nen("open", '''"A." {n}She is more careful than usual; she has already sharpened three pencils and laid them in a row.{/n} "'Areelu Vorlesh.' I have been saving her. Some entries one saves, the way one saves the good cake."
"There are names I am obliged to remember: gods, kings, conquerors, all very tiresome. And there are names I am happy to remember. Irori. Nethys. Areelu Vorlesh." {n}Her eyes are shining.{/n} "Write this. 'The greatest of the greatest. She opened a rift from Golarion to the Abyss. No one knew how, no one believed it possible, and she simply did it. The experiment of the century.'"''',
        c("Continue", "sacrifices")),
    nen("sacrifices", '''{n}She keeps walking, three steps and turn, three steps and turn, and she is quoting herself now, a speech she has plainly made before.{/n}
"'Some part of Golarion's population died as a result of her experiment, and the crusaders are still wrestling with its consequences. But the essence of what she did was a breakthrough of cosmic significance. The victims will be remembered as unfortunate but unavoidable sacrifices made at the altar of science.'" {n}She stops.{/n} "Have you got that? 'Altar of science.' I am rather proud of 'altar of science.'"''',
        c('[Make her read the dead] "Then put them in the entry. Every town in Sarkoris that was on the map before she opened it. By name. You read them out; I\'ll write."',
          "dead", flags=(ARCH_DEAD,), alignment=("Good", 1)),
        c('[Agree with her] "She did what nobody else could have. Write it that way."', "agreed", flags=(ARCH_AGREED,),
          alignment=("Evil", 1)),
        c('[Write it her way] "Altar of science. Got it." {n}And plan a footnote of your own, later, in a hand she can read.{/n}', "footnote",
          flags=(ARCH_TRICK,), mythic="Trickster")),
    nen("dead", '''"By name?" {n}She looks at you as if you had asked her to count the grains in a sack of flour.{/n} "That is a very long list. That is a tedious list. Sarkoris had a great many small towns with a great many consonants in them."
{n}You hold the pencil and wait. The camp noises go on around you. After a while, with a sigh that would befit a grief-stricken old man, she takes a map out of her sleeve, unfolds it, and puts her finger at the top left corner.{/n}''',
        c("Continue", "reading")),
    nen("reading", '''"Kenabres, which is ours, and which is not in Sarkoris, and which she also hurt. Very well. Sarkoris. Iz. Undarin. Storasta, where the library was..." {n}She reads them flat, one after another, like a quartermaster reading a list of stores.{/n}
{n}Somewhere after thirty she slows. Somewhere after fifty she stops, with her finger on a town whose name nobody can say, and looks at it.{/n}
"I had forgotten these," {n}she says.{/n} "On purpose. All of them. I decided they were irrelevant a long time ago, when I first read about her, and I was right; they do not change the result." {n}She looks at you, and her chin comes up.{/n} "They change the length of the entry. That is not the same thing, and I will not have you pretend it is."''',
        c("Continue", "both")),
    nen("both", '''"The entry stands. 'Altar of science' stands. She did what nobody believed possible, and I will say so to every paladin who throws a boot at me." {n}She folds the map.{/n}
"But an altar has a price list, and I had left it off, which is sloppy. Put the list after the entry. All of it. It will make the entry twice as long and three times as dull, and the students of Absalom will skip it." {n}Her mouth goes thin.{/n} "Let them try. I shall set it in the examination. A scholar who cannot recite what a breakthrough cost does not understand the breakthrough."''',
        c("[Write the list.]")),
    nen("agreed", '''"Exactly!" {n}She beams at you, the warm, delighted beam of a scholar who has found a colleague.{/n} "Nobody on this crusade will say that to me. They go red, or they reach for their swords. A paladin threw a boot at me once. It was not even her boot."
"You understand. The experiment is what matters. The rest is weather." {n}She takes the pencil from you and underlines "altar of science" twice, herself, in a line that goes through the paper.{/n} "I am very pleased with you, follower. I did not expect to be."''',
        c("[Take the pencil back.]")),
    nen("footnote", '''"Good." {n}She beams.{/n} "Nobody on this crusade will let me say that without reaching for a sword. You simply write it down. It is very restful."
{n}She does not see you mark a small cross in the margin, beside the altar of science. You know what goes there. She will find out, when the footnote comes, and it will be long, and it will be legible, and it will have every town in Sarkoris in it by name.{/n}''',
        c("[Write on.]")),
], requires=(SCRIBE,), delay=24)


m(PULSE, "An experiment of a personal nature", '"You said you needed me for something."', [
    nen("open", '''"I did. I do. It is an experiment." {n}She has cleared @DESK@ entirely, which you have never seen her do. On it there is one sheet of paper, one pencil and a stopwatch, set out with the precision of a surgeon's tray.{/n}
"An experiment of a... personal nature." {n}She rubs her nose.{/n} "But no less exciting for that, mark my words."''',
        c("Continue", "design")),
    nen("design", '''"The Encyclopedia requires an entry on attraction. Physical attraction. Between people." {n}She says it fast, like somebody jumping into cold water.{/n} "I have more observations of other people's attraction than anyone living, taken in taverns, temples and the backs of carts. They are very good observations. They are also all from the outside."
"The method is this. You will look at a series of objects, and I will take your pulse. A sword. A map. A bottle of wine, for comparison with my earlier work. Myself." {n}She says the last one in exactly the same voice as the others, and her ears go back.{/n} "The last one is a control."''',
        c('"A control."', "control"),
        c('[Flirt] "You want to know if I find you attractive."', "direct"),
        c('"Fine. Wrist."', "run")),
    nen("control", '''"A control. Obviously." {n}She does not look at you.{/n} "One must have something against which to measure the others. I chose myself because I was the nearest thing to hand. It is purely a matter of convenience."''',
        c("Continue", "run")),
    nen("direct", '''"I want to know what happens to a pulse when a person looks at another person they find attractive." {n}Very precisely.{/n} "Whether that person happens to be me is incidental to the design. It is also, I suppose, a possible outcome. All outcomes are possible until measured. That is the beauty of the method."''',
        c("Continue", "run")),
    nar("run", '''{n}She takes your wrist. Her fingers are cool. She starts the watch and holds up a sword, a notched crusader's blade somebody has left lying about, and counts, and writes. Then a map of the Worldwound's edge. Then a bottle, which she eyes with deep suspicion even while she holds it.{/n}
{n}Then she puts the bottle down and sits there with her hand on your wrist and the watch in her other hand, and looks at you, and waits.{/n}''',
        c("Continue", "result")),
    nen("result", '''{n}She counts. She counts much longer than she did for the sword. Then she writes the number down, looks at it, and turns the sheet face down on the desk.{/n}
"Inconclusive," {n}she says.{/n}
{n}Her voice is odd. She clears her throat.{/n} "The instrument is unreliable. The instrument is also me. My own pulse interfered with the reading; I could feel it in my thumb. That is a flaw in the design, and I shall correct it."''',
        c('[Kiss her] "Take another reading."', "kiss", flags=(KISSED_EARLY,)),
        c('"What was the number?"', "number"),
        c("[Let her have her flaw in the design.]", "leave")),
    nen("kiss", '''{n}She holds very still for it, the way she holds still for anything she is observing. Her mouth is warm and surprised, and the watch goes on ticking between you, and her fingers on your wrist tighten until you can feel your own pulse in them.{/n}
{n}Then she pulls back, and looks at the watch, and at you, and her face does something you have never seen it do.{/n}
"I did not stop the watch." {n}She stares at its face.{/n} "The reading includes the kiss, the staring afterwards, and whatever that was. I have wasted a data point." {n}She stands up, knocking the stool over.{/n} "The experiment is suspended. It is not cancelled. Nothing is cancelled. Go away, I need to think, and I cannot think while you are sitting there being a variable."''',
        c("[Go away, and leave her with the watch.]")),
    nen("number", '''"Irrelevant." {n}She puts her hand flat on the face-down sheet.{/n} "A number without a method is a rumour. When I have corrected the method, I will tell you the number. Or I will forget it, which is also a method." {n}A pause.{/n} "I will not forget it."''',
        c("[Let her keep it.]")),
    nen("leave", '''"Thank you." {n}She says it with real gratitude, the way a drowning woman thanks a plank.{/n} "Go on. Leave. I shall write it up." {n}As you go, you hear her turn the sheet back over, and sit without writing anything at all.{/n}''',
        c("[Leave her with the sheet.]")),
], requires=(SCRIBE,), forbids=(COMMITTED,), delay=24, RequiresAnyGroups=[list(twin_ids(DEMONS)) + list(twin_ids(ARCHITECT))])


m(TAIL, "A confounding variable", '"Nenio? Is that... your tail?"', [
    nar("open", '''{n}Nenio is sitting cross-legged with her back to you and a length of knotted measuring string in her teeth. She is trying, with great concentration and no success, to measure her own tail. It is thick, russet and silky, and it keeps moving out of the way of the string, as if it had opinions.{/n}''',
        c("Continue", "measure")),
    nen("measure", '''"It is. It was. It has been all along, apparently." {n}She takes the string out of her teeth.{/n} "I decided some time ago that my being a kitsune was irrelevant to my work, and I forgot it. Then a trap in the Nameless Ruins asked me who I was and would not accept my name as an answer, and here we are. I have a tail. I am trying to classify it."
"It will not hold still. I have asked it."''',
        c('"How could you forget you were a kitsune?"', "forget"),
        c('"Do you want help?"', "help")),
    nen("forget", '''"Easily. I stopped thinking about it." {n}She shrugs.{/n} "It is the same as forgetting anything else. You decide it does not matter, and you look at something else, and after some centuries it is simply not there. I did not need a tail to write an encyclopedia."
"I am beginning to think I have made a methodological error. If I could forget I was a fox, what else have I filed under 'irrelevant' that was holding up the ceiling?" {n}She frowns at the tail. The tail does not answer.{/n}''',
        c("Continue", "help")),
    nen("help", '''"Yes. Hold this end. At the base. No, the base. There." {n}She hands you the string without turning round and guides your hand back, to where the tail meets the small of her back above her belt.{/n}
{n}It is very warm. The fur is softer than it looks, and under it you can feel the muscle move. You hold the string where she says and she stretches the other end out along the tail, counting knots under her breath.{/n}''',
        c("Continue", "curl")),
    nar("curl", '''{n}At the ninth knot the tail curls back on itself, slides across your forearm and wraps your wrist, once, twice, snug as a sleeve.{/n}
{n}Nenio stops counting. She looks down over her shoulder at your wrist and her own tail around it, and her ears go flat, then straight up, then flat again.{/n}
"It does that," {n}she says.{/n} "I do not do it. It does it. It is the least scientific part of me. It is a confounding variable."''',
        c('[Flirt] "I don\'t mind being confounded."', "flirt"),
        c("[Stay very still, and let it hold on.]", "still"),
        c("[Ease your hand out, gently.]", "free")),
    nen("flirt", '''"You would not. You enjoy being in the way of things." {n}She does not unwind it. After a moment she lets her weight rest back very slightly against your knees, as if by accident, which it is not.{/n}
"Measurement: forty-three inches, root to tip, with a margin of error that is currently wrapped round your arm." {n}She writes it down.{/n} "I shall have to take it again. When it is less... engaged."''',
        c("[Stay until she has written it all down.]")),
    nen("still", '''{n}You stay still. The tail stays where it is. Somewhere in the camp somebody is sharpening a sword, and the Worldwound's light goes from red to a worse red, and neither of you mentions any of it.{/n}
"You are very good at holding still," {n}she says at last, without turning round.{/n} "It is a rare talent in a subject. I shall make a note of it." {n}She does not make a note of it.{/n}''',
        c("[Stay until the tail lets go on its own.]")),
    nen("free", '''{n}You slide your hand out, slowly, and the tail lets you go with a reluctance you can feel in the fur.{/n}
"Thank you." {n}Brisk, and a little too quick.{/n} "That was the correct procedure. One does not let the instrument take hold of the scientist. It corrupts the readings." {n}She measures the tail again, alone, and gets it wrong, and does not start over.{/n}''',
        c("[Leave her with her string.]")),
], requires=(SCRIBE, FOX_REVEALED), delay=24, places=("hub",))


m(SLIPS, "Yesterday I saw the Commander...", '"What are all those slips of paper?"', [
    nen("open", '''"Gossip." {n}She fans the slips out on @DESK@ like a card-sharp: a dozen scraps, each with one line on it.{/n}''',
        c("Continue", "gossip_old", requires=(GOSSIP_UNIVERSAL,), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "gossip_prepared", requires=(GOSSIP_PREPARED,), forbids=(GOSSIP_UNIVERSAL, UNREMEMBERED, RECREATED)),
        c("Continue", "gossip_new", requires=(UNREMEMBERED,)),
        c("Continue", "gossip_new", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "gossip_new", forbids=(UNREMEMBERED, RECREATED, GOSSIP_PREPARED, GOSSIP_UNIVERSAL))),
    nen("reads", '''{n}She picks one up and reads it, in the voice of a clerk reading a charge.{/n}
"'Yesterday I saw the Commander talk a demon into its own grave.' Unverified. I was not there." {n}Another.{/n} "'Yesterday I saw the Commander steal the Queen's spoons, and give them back, and she thanked {mf|him|her}.' Unverified. The kitchen denies losing any." {n}Another.{/n} "'Yesterday I saw the Commander take dictation from Nenio.' Verified. I was there. It was me."''',
        c('"Where did you get these?"', "sources"),
        c('[Flirt] "Write one about yourself."', "herself")),
    nen("sources", '''"Soldiers, traders, and a sergeant who owes me money. Nobody agrees on the missing wine. Everybody agrees on you. That makes you a particularly poor control."''',
        c("Continue", "herself")),
    nen("herself", '''"About myself? I have been measuring demon teeth and interrupting crusaders at supper. That scarcely requires a clandestine report." {n}She takes a clean slip.{/n} "Very well. 'Yesterday I saw Nenio ______ the Commander.' I cannot find a sufficiently exact verb."''',
        c('"Measure."', "verb"),
        c("[Say nothing, and let her keep the blank.]", "keep")),
    nen("verb", '''"'Measure.' Yes, that would be accurate." {n}She takes the slip out again, looks at it, and does not write the word in.{/n} "Accurate. Not sufficient. I shall think about it."''',
        c("[Leave her to her slips.]")),
    nen("keep", '''"Leave it empty, then." {n}She puts the slip in her sleeve.{/n} "I shall come back to it. Do not fill it in while I am looking at the others."''',
        c("[Leave her to her slips.]")),
    nen("gossip_old", '''"These are revisions of the slips I prepared for our friendship experiment. They could be used about anybody. This time I want names and sources. The crusade has quite enough reports that identify nothing."''', c("Continue", "reads")),
    nen("gossip_prepared", '''"I prepared these slips for our gossip experiment. Now I am checking them against the crusade's reports. Someone has to."''', c("Continue", "reads")),
    nen("gossip_new", '''"I have been collecting reports about the Commander. The crusaders call them gossip, which appears to mean a report nobody has checked. Here are twelve. I intend to check them."''', c("Continue", "reads")),
], requires=(SCRIBE,), delay=48, RequiresAnyGroups=[list(twin_ids(DEMONS)) + list(twin_ids(ARCHITECT))])


# --- Chapter 4, the Abyss: the company travels with her; the sessions come at a rest. While she waits in Drezen, she writes. --

hub4(LAMP, "Hold the lamp still", '"You want me to hold the lamp?"', [
    nar("open", '''{n}The harbour lamps leave the terrace in strips of light and deep shadow. Tonight the company has made camp on a terrace above the harbour, and Nenio has made you hold the lamp for an hour while she measures shadows.{/n}
{n}"Not that shadow," she says. "The long one. The one that is lying." She puts a stake in the ground at the end of a shadow thrown by a statue of a woman with too many rings, and writes down its length, and then the length of the statue, and scowls at the difference.{/n}''',
        c("Continue", "lady")),
    nen("lady", '''"Nothing in this city casts the shadow it should. The towers are too short for their shadows. The people are too tall for theirs. There is a queen here, the Lady in Shadow they call her, and I measured the shadow of her statue in the great square during the changing of the guards, which took a great deal of explaining to her guards." {n}She holds up a sheet with a very long number on it.{/n}
"It was the only honest thing in the square. It was exactly as long as the statue. Everything else in Alushinyrra lies about its length. She does not bother. She is quite sure of herself." {n}A pause.{/n} "I found that very attractive in a demon lord, and I do not wish to discuss it further."''',
        c('"Write it down: \'Abyss, the. Revised.\'"', "entry"),
        c('[Flirt] "Should I be jealous of a demon lord\'s shadow?"', "jealous")),
    nen("jealous", '''"Of her shadow? No. Of her, possibly, but not for the reasons you think." {n}She squints at you over the lamp.{/n} "She has had several thousand years to become perfectly consistent. You are a trickster, and you have not been consistent for three minutes together since I met you. It is very inconvenient for my charts." {n}She takes the lamp from you and gives it back, so that you are holding it slightly differently.{/n} "There. Now your shadow is lying too."''',
        c("Continue", "entry")),
    nen("entry", '''"'Abyss, the. Revised.'" {n}She dictates, walking along the edge of the terrace with the harbour's wrong-coloured light on her face.{/n} "'Earlier editions describe the Abyss as infinite. This is inaccurate. It is merely very large and badly organised. Its inhabitants are, on the whole, less interesting than they believe themselves to be, and more dangerous. The author has visited in person, in the company of the Commander of the Fifth Crusade, whose name...'"''',
        c("Continue", "space_filed", requires=(NAME_GONE,)),
        c("Continue", "space", forbids=(NAME_GONE,))),
    nen("space", '''"'...whose name...'" {n}She stops at the edge of the terrace, with her back to you.{/n} "Leave a space."
{n}You leave a space. She does not go on for a while. Below you a ship with black sails is coming into the harbour and nobody on it is singing.{/n}
"I have left a space for you in every entry that mentions you," {n}she says.{/n} "I counted them last night, instead of sleeping. Twenty-three. That is a great many spaces for an irrelevant name." {n}She turns round.{/n} "Hold the lamp higher. I need to see the page."''',
        c("[Hold the lamp higher.]")),
    nen("space_filed", '''"'...whose name...'" {n}She stops, with her back to you, and her hand goes to her sleeve and stays there.{/n} "Leave a space. It is filed. It is not coming back. Leave one anyway."
{n}You leave a space. Below you a ship with black sails is coming into the harbour and nobody on it is singing.{/n}
"I keep telling you to leave them," {n}she says,{/n} "and there is nothing left to put in them. I have counted. Twenty-three. That is a great many spaces for a name I paid away." {n}She turns round.{/n} "Hold the lamp higher. I need to see the page."''',
        c("[Hold the lamp higher.]")),
], requires=(SCRIBE,), delay=12)


hub4(SHOULDER, "A sentence finished", '"Sit down before you fall down, Nenio."', [
    nar("open", '''{n}The company moves through the lower terraces during a lull in the crowds, with the sentries watching the alleys. At the halt somebody lights a fire of things that burn badly. Nenio sits down beside you on a flat stone with her notebook on her knee, begins dictating an entry on the fungi of the lower terraces, and falls asleep in the middle of the word "spore".{/n}
{n}She falls asleep sitting up, and then slowly less upright, and then her head is on your shoulder, heavy and warm, and the pencil is still in her fist.{/n}''',
        c("Continue", "sleep")),
    nar("sleep", '''{n}She sleeps like a scholar: frowning, as if she disagreed with the dream. Her breath is slow against your neck. Her notebook slides off her knee onto yours, open at the unfinished entry, "The fungi of the lower terraces are notable for their spore", and after "spore" there is nothing.{/n}
{n}You have her pencil. She is holding it. You could take it.{/n}''',
        c('[Finish her sentence, as well as you can: "...which, according to the author\'s follower, smells like the inside of an old boot and should not be eaten."]', "finished",
          flags=(FINISHED_SENTENCE,)),
        c('[Finish it truthfully: "...and the author fell asleep here, on a march, in the Abyss, on her follower\'s shoulder, and was not woken."]', "truthful",
          flags=(FINISHED_SENTENCE,)),
        c("[Leave the sentence as it is, and don't move until she wakes.]", "still")),
    nen("finished", '''{n}When she wakes she reads it with her nose almost touching the page. Then she reads it again.{/n}
"'Smells like the inside of an old boot.'" {n}She looks up at you.{/n} "Unverified. Anecdotal. Written in another hand in my own notebook, uninvited." {n}She taps the page.{/n} "Also correct. I had forgotten. I had decided that the smell was irrelevant, and it is not; one of the corporals ate one."
"I shall keep it. With attribution. 'The author's follower, personal communication, the lower terraces, while the author was indisposed.'" {n}She sniffs.{/n} "Indisposed. I was not asleep. I was thinking with my eyes shut."''',
        c("[Let her have been thinking.]")),
    nen("truthful", '''{n}When she wakes she reads it with her nose almost touching the page. She reads it three times. Her ears do not move at all, which is how you know she is not breathing properly.{/n}
"That is not about fungi," {n}she says eventually.{/n}
"It is in my notebook. In the fungi entry." {n}She looks at the sentence as if it had been written by a stranger in a language she half knows.{/n} {n}Her pencil goes to the line to strike it, and stays there, and does not move.{/n} "I am keeping it. As evidence. Of what, I have not determined." {n}She closes the notebook and holds it against her chest.{/n} "It stays. I shall have to write a new entry for the fungi. This one is spoiled for fungi."''',
        c("[Let her keep the notebook.]")),
    nar("still", '''{n}You do not move. The fire burns down. Somewhere out in the dark something large goes past the camp without stopping, and the sentries let it. Her weight on your shoulder never shifts, and neither do you, and when she wakes your arm is dead from the elbow down and you do not regret it.{/n}
{n}When she wakes she sits up very straight, as if she had been sitting up very straight all along, and looks at the notebook, and at the word "spore", and says, "Where was I?", and then, without waiting for an answer, "No. Do not tell me. I remember exactly where I was." She does not look at your shoulder. She does not need to.{/n}''',
        c("[Flex your dead arm, carefully.]")),
], requires=(LAMP,), delay=24)


v(REPORT, "A report from the capital", [
    nar("open", '''{n}The letter comes in the pouch with the crusade's dispatches, through whatever way the Queen's mages keep open to you in this place; the pouch smells of ozone and old paper. Tucked among the reports on stores and sieges is one folded eight times, with a note on the outside in a clerk's hand: "Paid for in advance, in Drezen, by a woman in a grey coat, who told us to deliver it wherever the Commander has got to, even there."{/n}
{n}The hand is illegible, except where she has written slowly, on purpose, for you.{/n}''',
        c("Continue", "letter")),
    nen("letter", '''"Report from the capital in the Commander's absence. Observer: the author.
"Morale: variable. Price of pepper: absurd; the spice trader blames the demons, and the demons blame nobody, being demons. The market has been told you are dead four times this month. I have recorded each rumour, its source and its time of death. None of them survived a week. I had expected no less of you, and have written so."
"The crusade misses you in a disorganised way. The spice trader misses his crates. I have not missed you, because missing is not an observable phenomenon, but I have noticed that I leave the stool beside mine empty when I work, and I cannot account for it."''',
        c("Continue", "ask")),
    nen("ask", '''"Request: bring me a sample from the Abyss. Anything. A stone, a feather, a demon's toenail. Label it. You know how.
"In every entry I have written since you left, I have left a space for you. There are nineteen. I am recording the number in case it is significant. It is probably not significant. Come back and I will tell you."
"The author."''',
        c("[Write back: \"Sample enclosed. One stone from the harbour. It casts the wrong shadow.\"]"),
        c("[Write back: \"Nineteen is significant. Keep counting.\"]"),
    ),
], requires=(SCRIBE, VISITOR), forbids=("trickster.ever",), delay=24, kind="letter", chapters=(4,))   # retired (Sol r1 COX, R2-5)

m(F + "drezen.handed", "A report from the capital", '"You kept a report on the market?"', [
    nen("open", '''"A report from the capital. Recorded by the author." {n}She unfolds a sheet and reads it herself.{/n} "Morale: variable. Price of pepper: absurd. The spice trader attributes both to demons. Soldiers attribute both to the quartermaster. Neither has supplied measurements. I have started with the pepper. It holds still."''',
        c("Continue", "stool")),
    nen("stool", '''"Also, I have kept the seat beside mine empty." {n}She looks at it as if it had failed an examination.{/n} "For dictation. Obviously. There are nineteen spaces in my current notes for the Commander. None is filled. Sit down; I should like to finish at least one entry."''',
        c('"Nineteen is significant. Keep counting."', "count"),
        c("[Put a labelled stone from the scouts\' collection on her desk.]", "stone")),
    nen("count", '''"Significant of what? You are not permitted to say 'significant' without a unit." {n}But she writes 19 at the top of a clean sheet, and underlines it, and leaves the rest of the page empty.{/n}''',
        c("[Sit on @SEAT@.]")),
    nen("stone", '''{n}She takes it at once, checks the label, and turns it in the light.{/n} "Location, depth, date. Adequate. A specimen with a provenance. You are becoming useful." {n}She sets it beside the report.{/n} "Now hold the page while I dictate."''',
        c("[Sit on @SEAT@.]")),
], requires=(SCRIBE,), delay=24, chapter=5, places=("visitor", "arcade"))


# --- Chapter 5: page one, volume one, and the study after. --------------------------------------------------------------------

m(PAGE_ONE, "Page one", '"You\'ve got a clean sheet. That\'s a bad sign."', [
    nen("open", '''"It is an extremely bad sign." {n}She is sitting very straight at @DESK@ with a single clean sheet in front of her and her hands folded on top of it, like a pupil waiting for an examination to begin.{/n}
"There is one entry I have never written. I have described kings and bees and the correct way to kick a linnorm, and I have never written one line about the author." {n}She pushes the sheet toward you.{/n} "It would be vanity. So I shall dictate it, and you will write it, and then it will be your vanity and not mine."''',
        c("Continue", "pre", requires=(FOX_REVEALED,), forbids=(RIDDLE_DONE, VISITOR, ENIGMA_RESOLVED)),
        c("Continue", "post", requires=(RIDDLE_DONE,)),
        c("Continue", "visiting", requires=(VISITOR,), forbids=(RIDDLE_DONE,)),
        c("Continue", "unvisited", forbids=(FOX_REVEALED, RIDDLE_DONE, VISITOR, ENIGMA_RESOLVED)),
        c("Continue", "resolved", requires=(ENIGMA_RESOLVED,), forbids=(RIDDLE_DONE, VISITOR))),
    nen("pre", '''"You know why. We are going to the Enigma. The masks are nearly found, and the entity that asked me who I was is going to ask again, and this time I intend to answer it with something better than my name." {n}Her ears are flat, and she is making no attempt to stand them up.{/n}
"It will be my triumph. The experiment of the millennium. Or it will be my downfall, a complete fiasco. Those are the only two outcomes I can calculate." {n}She taps the sheet.{/n} "If it gobbles me up, run while it is distracted, and tell Golarion about the heroic death of its greatest daughter. You will need the entry. Write."''',
        c("Continue", "entry")),
    nen("unvisited", '''"You know why. Somewhere in this country there are ruins that ask the people who walk into them who they are. I have read about them. I intend to walk into them, and people who walk into ruins ought to leave an entry behind." {n}She taps the sheet.{/n} "It is not morbid. It is filing. Write."''',
        c("Continue", "entry_plain")),
    nen("resolved", '''"You know why. I went into the Enigma as nothing and argued my way out with my name, with some help, and I thanked the help, which I do not usually do." {n}She does not look at you.{/n} "A thing that was very nearly lost should be written down. Otherwise one forgets how nearly, and then one is careless with it."''',
        c("Continue", "entry")),
    nen("post", '''"You know why. I went into the Enigma as nothing and came out with my name. Somebody paid for it." {n}She does not look at you.{/n} "A thing that has been paid for should be written down. Otherwise one forgets what it cost, and then one spends it carelessly."''',
        c("Continue", "entry")),
    nen("visiting", '''"A scholar should keep an account of the scientist. Mine is incomplete. Let us correct it."''',
        c("Continue", "visiting_recreated", requires=(UNREMEMBERED,)),
        c("Continue", "visiting_recreated", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "visiting_away", forbids=(UNREMEMBERED, RECREATED))),
    nen("entry_plain", '''"'Nenio.'" {n}She says it the way a herald says a name at a door.{/n} "'Greatest scientist of the modern age. Author of the Encyclopedia Golarionnica, in progress. Species: irrelevant; the author has more important things to classify. Age: considerable. Origin: irrelevant.'"
{n}She stops. You wait with the pencil over the page.{/n} "No. Strike 'irrelevant'. Strike it properly, one clean line, so the next reader can see it was wrong. Write after it: 'Origin: under review.'"''',
        c("Continue", "habits")),
    nen("entry", '''"'Nenio.'" {n}She says it the way a herald says a name at a door.{/n} "'Greatest scientist of the modern age. Author of the Encyclopedia Golarionnica, in progress. Species: kitsune. Age: approximately four thousand years, give or take a few centuries. Origin: irrelevant.'"
{n}She stops. You wait with the pencil over the page.{/n} "No. Strike 'irrelevant'. Strike it properly, one clean line, so the next reader can see it was wrong. Write after it: 'Origin: under review.'"''',
        c("Continue", "habits")),
    nen("habits", '''"'Habits: forgets on purpose whatever she ranks irrelevant. Has occasionally been wrong about what is irrelevant. Is working on this.'" {n}Her voice is quite steady, and she is not looking at you.{/n} "'Conducts experiments of a personal nature. Their results are filed separately.'"
"'Associates: one follower.'" {n}She stops again.{/n}''',
        c("Continue", "assoc_filed", requires=(NAME_GONE,)),
        c("Continue", "assoc", forbids=(NAME_GONE,))),
    nen("assoc", '''"Leave a space." {n}And then, at once:{/n} "No. Do not leave a space. Write it. Your name. Here, in the entry on me, where I will never have to read it unless I want to." {n}She slides the pencil across to you and sits back with her arms folded, looking at the Worldwound's light, very hard, so as not to look at the page.{/n}
"This is not a conclusion," {n}she says.{/n} "It is a citation. There is a difference and it is the entire difference."''',
        c("[Write your name in her entry.]", "written"),
        c('[Leave the space] "Not yet. Not until you\'ve decided what it means."', "not_yet")),
    nen("assoc_filed", '''"I filed the name as agreed. I cannot fill the space. Leave it."''',
        c("[Leave the space.]", "space_left"),
        c('[Write "follower" in it, very small.]', "follower")),
    nen("written", '''{n}She does not look while you write it. When you slide the page back she reads it, once, and her face does nothing at all, and she folds the sheet into four and puts it in her sleeve among the others, in a particular place near the cuff.{/n}
"Citation noted," {n}she says.{/n} "Next entry. 'Nightshade, common.' Write quickly, I am feeling uncharacteristically unscientific and I wish to recover."''',
        c("[Write on.]")),
    nen("not_yet", '''{n}She looks at you then, directly, for as long as it takes to be sure you mean it.{/n}
"Not yet." {n}She repeats it as if testing its weight.{/n} "Until I have decided what it means. Yes. That is methodologically sound. It is also..." {n}She does not finish. She takes the page, folds it and puts it in her sleeve with the blank still in it.{/n} "Next entry."''',
        c("[Write on.]")),
    nen("space_left", '''"Thank you." {n}She takes the page and folds it into her sleeve, carefully, near the cuff.{/n} "Next entry. Something with no people in it. Rocks."''',
        c("[Write on.]")),
    nen("follower", '''{n}She reads it. "Follower." Her mouth moves, not quite a smile.{/n}
"Accurate. Not a name. Better than a name, possibly; a name only says who. That says what." {n}She folds the page into her sleeve, near the cuff.{/n} "It stays. Next entry. Rocks."''',
        c("[Write on.]")),
    nen("visiting_recreated", '''"I woke on the road outside Drezen with my bound working draft and gaps in my records. I have been filling them with observations. The scientist remains poorly documented. Write before I decide that is irrelevant."''',
        c("Continue", "entry", requires=(FOX_REVEALED,)),
        c("Continue", "entry_plain", forbids=(FOX_REVEALED,))),
    nen("visiting_away", '''"I came to correct your vrock and remained to correct your handwriting. That is an adequate account of my arrival. It says nothing about the author. I intend to remedy that."''',
        c("Continue", "entry", requires=(FOX_REVEALED,)),
        c("Continue", "entry_plain", forbids=(FOX_REVEALED,))),
], requires=(SCRIBE,), delay=24, chapter=5)


m(VOLUME_ONE, "Volume one", '"You\'re packing."', [
    nen("open", '''"I am redistributing." {n}She has volume one of the Encyclopedia Golarionnica on @DESK@ in front of her, wrapped in oilcloth and tied with string, the knot done and redone until it is a very small, very angry lump.{/n}
"The crusade is going to the Threshold. I have calculated your chances." {n}She pats the bundle.{/n} "I shall tell you the number another time. It is not a number for today. It is a number for writing on a slate and then wiping off with your sleeve."''',
        c("Continue", "give", forbids=(DEBT_DEFAULTED,)),
        c("Continue", "give_new", requires=(DEBT_DEFAULTED,))),
    nen("give_new", '''"This is volume one. Again. Aardvark to Abadar, so far, in your hand, from my dictation, because the Sphinx has the other one and I have had to begin at A like a schoolchild." {n}Her ears go back at the word 'Sphinx', and stay back.{/n} "I am still angry about that. I shall be angry about it in a hundred years. Carry it anyway."
"The crusade goes to the Threshold. If this working draft survives with you, the next edition will have somewhere to begin."''',
        c("Continue", "committed", requires=(COMMITTED,)),
        c("Continue", "not_yet", forbids=(COMMITTED,))),
    nen("give", '''"This is the only bound volume of the Encyclopedia. Volume one, a working draft. Aardvark to Azlant, with a digression on Abadar that nobody asked for." {n}She pushes it across to you.{/n} "Carry it."
"The crusade goes to the Threshold. If this working draft survives with you, the next edition will have somewhere to begin."''',
        c("Continue", "committed", requires=(COMMITTED,)),
        c("Continue", "not_yet", forbids=(COMMITTED,))),
    nen("committed", '''"Also," {n}she says, much less briskly,{/n} "I would like you to have something of mine that is not a list. The study is longitudinal. That means it has to continue, which means you have to continue, which means I am going to be very angry if you do not, and I would like there to be something in your pack to remind you of how angry." {n}She folds her hands on the desk.{/n} "That is all. It is a very practical arrangement."''',
        c('"I\'ll carry it. And I\'ll bring it back."', "back"),
        c("[Take her hands instead of the book.]", "hands")),
    nen("not_yet", '''{n}She hesitates with one hand still on the oilcloth.{/n}
"There is a question I have not finished asking you. I do not know how to ask it yet. I do not want it to be answered by somebody else's death, or by mine, before I have." {n}She takes her hand off the book.{/n} "So carry that, and do not become irrelevant, and I shall work out the question in the meantime."''',
        c('"I\'ll carry it. And I\'ll bring it back."', "back"),
        c("[Take her hands instead of the book.]", "hands")),
    nen("back", '''"Bring it back. Obviously. With no stains on it, and no pages folded down, and nobody's blood on the cover, especially yours." {n}She sniffs.{/n} "I have read too many field journals that came back with blood on the cover. It spoils the index."''',
        c("[Put volume one in your pack.]")),
    nen("hands", '''{n}She lets you. Her hands are cold and ink-stained and they will not settle; they turn over in yours as if looking for somewhere to write.{/n}
"You are not holding the book," {n}she observes.{/n} "The book is the point of the exercise."
"Take the book as well." {n}She does not take her hands back.{/n} "In a moment. I am measuring something. Do not ask me what. I will forget it immediately, if I can, and I think I cannot."''',
        c("[Take the book as well, in a moment.]")),
], requires=(SCRIBE,), delay=48, chapter=5, RequiresAnyGroups=[list(twin_ids(PAGE_ONE))])


m(LONG, "Longitudinal", '"How is the study going?"', [
    nen("open", '''"Productively." {n}She is at @DESK@ with a sheet headed LONGITUDINAL STUDY, SUBJECT [          ], and under the heading three columns of figures in a hand that is, for once, nearly legible.{/n}
"Sleep: four hours and some minutes on an ordinary night; fewer before a battle and more after one, which is the wrong way round, and I intend to find out why. You wake at doors. Not trumpets. Not screams; there were screams on the second night and you slept through them. Doors." {n}She makes a mark.{/n} "I have been opening and shutting mine at intervals of an hour since the morning after, to be sure."''',
        c('"You\'ve been opening doors all night to wake me?"', "crossed"),
        c('[Flirt] "What\'s in the third column?"', "adjectives")),
    nen("crossed", '''"To test you. Waking you was a side effect." {n}She does not look up.{/n} "Your objection is in the next column." {n}She makes another mark.{/n} "Three more nights. Then I shall compare the results."''',
        c("Continue", "question")),
    nen("adjectives", '''"You return to my desk. You take dictation. You leave the blank when I ask. None explains why I keep waiting for the next visit." {n}She taps the third column.{/n} "I intend to find out what it measures. I am not going to guess."''',
        c("Continue", "question")),
    nen("question", '''"I am going to ask you a question. I mean to ask this one. I have drafted it." {n}She takes a slip of paper from her sleeve and reads it.{/n}
"When this war is over, what do you want?"
{n}She puts the slip down.{/n} "Not the crusade. Not the Worldwound. You. It is not for the Encyclopedia. It is for me. I will not write the answer down."''',
        c('"A long study. Very long. No end date."', "study"),
        c('"I don\'t know yet. Ask me again after the Threshold."', "after"),
        c('"More questions like that one."', "questions")),
    nen("study", '''"No end date." {n}She considers it with the grave pleasure of a scholar handed an unlimited budget.{/n} "That is not how studies work. Studies have an end date, and a conclusion, and a publication." {n}Her ears come up, slowly.{/n} "I shall make an exception. I am the author. I am permitted exceptions. I have never used one before, and I was saving it."''',
        c("[Leave her with her crossed-out adjectives.]")),
    nen("after", '''"After the Threshold." {n}She nods, and writes nothing, as promised.{/n} "Very well. I shall ask you again, then, in exactly those words. If you are not there to be asked, I shall be extremely put out. I have a great deal of put-out stored up for the occasion."''',
        c("[Leave her with her crossed-out adjectives.]")),
    nen("questions", '''"That is a trick answer." {n}But she is almost smiling.{/n} "You want me to go on asking you things. That is not a want; that is a subscription." {n}She puts the slip back in her sleeve, near the cuff, next to something else folded there.{/n} "Very well. Subscribed. Do not complain about the volume of correspondence."''',
        c("[Leave her with her crossed-out adjectives.]")),
], requires=(COMMITTED, MORNING_AFTER), delay=48)


# --- More sessions: the rhyme, the question in the emptiness, the edge of the Wound, Kenabres, the market. --------------------

RHYMES = F + "rhymes"
WHO = F + "who_are_you"
EDGE = F + "edge"
INQUISITORS = F + "inquisitors"
MARKET = F + "market"
DRINK = F + "abyss.drink"
VOID_DAYS = F + "void_days"
WHO_NAMED = F + "who_are_you.named"
WHO_LIED = F + "who_are_you.lied"
EDGE_SHIELDS = F + "edge.shields"

m(RHYMES, "Crustacean, cogitation", '"Are you... writing poetry?"', [
    nen("open", '''"I am conducting an experiment in whether I can write poetry." {n}She has a sheet covered in crossings-out.{/n} "Not the same thing. Poetry is a result. I am only at the method."''',
        c("Continue", "poetry_again", requires=(POETRY_FAILED,), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "poetry_first", requires=(UNREMEMBERED,)),
        c("Continue", "poetry_first", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "poetry_first", forbids=(UNREMEMBERED, RECREATED, POETRY_FAILED,))),
    nen("method", '''"Method: I read the poems of Golarion's great love poets, all of them, in four evenings. Result: they are mostly about eyes." {n}She shuffles her pages.{/n} "Eyes like stars. Eyes like the sea. Eyes like two dark pools. One Taldan poet compares his lady's eyes to a pair of well-maintained siege engines, which I found the most honest of the lot."
"So I am attempting one of my own. Subject: eyes. Anyone's. I chose yours because you were standing in the light."''',
        c('"Read it to me."', "read"),
        c('[Flirt] "My eyes? Not a siege engine\'s?"', "siege")),
    nen("siege", '''"Your eyes are not remotely like siege engines. That was the whole difficulty." {n}She frowns at the page.{/n} "Siege engines are consistent. Your eyes do something different every time I look at them. It is very hard to rhyme with."''',
        c("Continue", "read")),
    nen("read", '''{n}She clears her throat and reads.{/n}
"'Your eyes interrupt calculation.
Your thighs interrupt classification.
I require a rhyme for observation.
...Copulation?'" {n}She crosses out the last word.{/n} "Premature conclusion. The metre is also wrong."''',
        c('"It\'s the best poem anyone\'s written about me."', "best"),
        c('"The last line is very good."', "last"),
        c('[Rhyme back] "Your nose is always inky at the tip. I\'ve counted. That\'s the one thing I\'d not skip."', "back")),
    nen("best", '''"That is a statement about the poems other people have written about you, not about mine." {n}But her ears have come up.{/n} "I shall record it as a comparative result. Comparative results are always suspicious. I shall record it anyway."''',
        c("Continue", "end")),
    nen("last", '''"The last line is the only one I did not have to think about." {n}She looks at it.{/n} "That is either the mark of true poetry or of an observation too obvious to require thought. I cannot tell which. It is very distressing."''',
        c("Continue", "end")),
    nen("back", '''{n}She stares at you. Then she touches the tip of her own nose, looks at her finger, and finds it inky.{/n}
"That scans," {n}she says, as if accusing you of theft.{/n} "Badly, but it scans. And it is accurate." {n}She writes it under hers, and draws a line between them, and looks at the two couplets side by side for rather longer than a scholar needs to look at anything.{/n}''',
        c("Continue", "end")),
    nen("end", '''"Conclusion: no poetic talent detected. I shall print the attempt beside the method. Perhaps the students can make it scan. I have demons to classify." {n}She folds the sheet very small.{/n} "The volunteer will not be named. There is a space."''',
        c("[Leave her with her couplet.]")),
    nen("poetry_again", '''"Our earlier rhyme experiment was unsuccessful. I kept the result. The Encyclopedia still needs an entry on love poetry. These crusaders have supplied twenty specimens and not one useful measurement. I shall try again."''',
        c("Continue", "method")),
    nen("poetry_first", '''"The Encyclopedia needs an entry on love poetry. I have collected specimens from the crusaders. Most mention eyes. Several mention thighs. None gives measurements. I shall try the method myself."''',
        c("Continue", "method")),
], requires=(SCRIBE,), delay=48, RequiresAnyGroups=[list(twin_ids(DEMONS)) + list(twin_ids(ARCHITECT))])


m(WHO, "Who are you?", '"You\'ve been quiet since the Ruins."', [
    nen("open", '''"The voice asked who I was. My name was not enough. Judging by your reaction, it asked you too. What did you say?" {n}She sits with her tail curled around her feet, her notebook open.{/n}''',
        c('"My name. It didn\'t work for me either."', "named", flags=(WHO_NAMED,)),
        c('"I lied. I told it I was somebody else."', "lied", flags=(WHO_LIED,)),
        c('"Nothing. I didn\'t answer."', "silent", flags=(WHO_SILENT,))),
    nen("named", '''"Your name. And it was not enough for you either. Informative." {n}She draws a small circle beside the note.{/n} "I would have called a name a sufficient label. Apparently the trap wanted more than a label."''',
        c("Continue", "question")),
    nen("lied", '''"You lied to the void." {n}She looks at you with something between horror and admiration.{/n} "To an entity that sees through masks, that solves people like riddles, that took my face off with one question. You lied to it."
"And it knew. It told you so, and asked again, the way it asked me." {n}She writes that down, fast.{/n} "Hypothesis: a trickster's face is already a mask, all the way down, and the void had to dig for the bottom. That is either terrifying or the most interesting thing I have learned this year."''',
        c("Continue", "question")),
    nen("silent", '''"You did not answer." {n}Her ears go forward.{/n} "And it did not let you off for that. It told you that sooner or later you would have to. So it made you wait too." {n}She shakes her head slowly.{/n} "I shouted my name at it like a fishwife, and you simply stood there and made it wait. Neither of us won. You lost more slowly. I am jealous. I will get over it."''',
        c("Continue", "question")),
    nen("question", '''"Here is what I want to know, and it is not for the Encyclopedia." {n}She says it quickly, before she can decide it is irrelevant.{/n} "When it asked you who you were, what did you think? Not say. Think. In the moment before you answered."
"I thought: 'Nenio, greatest scientist of the modern age.' The trap was unimpressed."''',
        c('"I thought: \'I\'m the one they sent.\'"', "sent"),
        c('"I thought of you, shouting at it."', "you"),
        c('"I thought: \'Nobody. Yet.\'"', "nobody")),
    nen("sent", '''"The one they sent." {n}She repeats it without mockery.{/n} "That is not a name. It is a job. The void probably respects a job; it is very businesslike." {n}She writes nothing.{/n} "I think you are more than the one they sent. I have no evidence for that. I am recording it as a hunch, which I never do."''',
        c("Continue", "end")),
    nen("you", '''{n}She goes very still.{/n}
"That is a very bad answer to 'who are you'," {n}she says at last.{/n} "It is not about you at all. It is about me." {n}Her tail tightens around her ankles.{/n} "The void would not have accepted it. I do not know whether I accept it. I am going to think about it for some time, and I would be grateful if you did not stand there while I do."''',
        c("Continue", "end")),
    nen("nobody", '''"'Yet.'" {n}She writes the word beside the circle.{/n} "Then I shall leave the date blank too. Tell me when you have an answer worth recording."''',
        c("Continue", "end")),
    nen("end", '''"We shall find the masks. We shall open the way. And I shall stand in front of whatever it is and it will ask me again, and this time..." {n}She stops.{/n} "This time I do not know what I shall say. That is the first time I can remember walking toward an experiment without a hypothesis. It is very uncomfortable. I am looking forward to it enormously."''',
        c("[Leave her to think.]")),
], requires=(SCRIBE, FOX_REVEALED), forbids=(RIDDLE_DONE, ENIGMA_RESOLVED), delay=24, places=("hub",))


m(EDGE, "The edge of the Wound", '"You want to go where?"', [
    nen("open", '''"The edge. Not the Wound itself; I am not a fool. The edge, where the ground changes its mind." {n}She has a satchel packed with jars, a surveyor's chain and a sausage.{/n} "I need a sample of soil from each side of the line, and from the line itself if there is one, which I doubt. You are coming, because I cannot carry the chain and the sausage and also fight whatever lives at the edge."''',
        c('"Fine. We go now."', "walk"),
        c('"That\'s not safe, Nenio."', "safe")),
    nen("safe", '''"The Worldwound is dangerous, walking under a hanging icicle is dangerous, and choking on a badly chewed sausage can lead to a fatal outcome. Living is dangerous." {n}She hands you the sausage, for safety.{/n} "But what is danger compared to knowledge? Come on."''',
        c("Continue", "walk")),
    nar("walk", '''{n}The edge is an hour's ride from the last picket, where the crusade's burned fields turn into something that was never a field. The grass is the wrong colour, and then it is not grass. The air tastes of pennies. Nenio walks the line with her chain, taking a sample every ten paces, and talks the whole time, mostly to the jars.{/n}
{n}Where the ground changes its mind there is a crusader's shield half buried, and another beyond it, and then more, a line of them, the way a tide leaves a line of weed.{/n}''',
        c("Continue", "shields")),
    nen("shields", '''{n}She stops at the first one. The paint is still on it: a hand holding a sword, some knight's badge from the first crusade or the third.{/n}
"The edge has moved," {n}she says, in her lecturing voice.{/n} "Here is the line where it was. The shields mark it. They fell where the ground turned under them." {n}She kneels and measures the distance from the shield to the new edge, and writes down the number, and does not get up.{/n}
"I have a chapter on the Worldwound's expansion. I wrote it from maps. My estimate from the maps was three miles of growth. It does not say anything about shields."''',
        c('[Read the badges to her] "Then put the shields in. One by one. I\'ll read them, you write."', "read", flags=(EDGE_SHIELDS,)),
        c('"The maps are enough. We should go."', "maps"),
        c("[Say nothing, and let her look.]", "look")),
    nen("read", '''{n}You read them. A hand and a sword. A white horse. Three stars on blue. A badge you do not know, and she does, and says it without being asked. She writes them all down, one to a line, with the distance from the edge beside each, and the list goes over onto the back of the page.{/n}
"This is not science," {n}she says, halfway down the second side.{/n} "This is a list of the dead. I do not do lists of the dead."''',
        c("Continue", "sarkoris", requires=(ARCH_DEAD,)),
        c("Continue", "read_first", forbids=(ARCH_DEAD,))),
    nen("read_first", '''"I kept the losses as a total. This field report needs the badges too." {n}She writes the next badge anyway, and the next.{/n} "The number for this line is somewhere past two hundred. I have written every name so far to arrive at it. It is a very inefficient way to count, and I find I cannot stop, and I do not like finding things out about myself on a battlefield."''',
        c("Continue", "home")),
    nen("maps", '''"The maps are not enough." {n}She says it sharply, and then seems surprised at herself.{/n} "My estimate from the maps was three miles. The shields say three miles of people. I did not know that until I stood here. I should have known it. I am supposed to know everything." {n}She takes one more measurement and gets up.{/n} "Very well. We go. But I am coming back with a longer chain."''',
        c("Continue", "home")),
    nar("look", '''{n}You let her look. She looks for a long while, and then she takes the pencil from behind her ear and writes something at the bottom of the chapter on the Worldwound's expansion, in capitals, slowly, so that anyone could read it: "SEE SHIELDS."{/n}''',
        c("Continue", "home")),
    nen("sarkoris", '''"I did Sarkoris once, because you made me read it aloud. It did not change my opinion of the Architect. It has not left me either." {n}She writes the next badge anyway.{/n} "It turns out the dead are also data. Everything is. It is extremely inconvenient."''',
        c("Continue", "home")),
    nen("home", '''{n}On the ride back she sits behind you, because she says the horse dislikes her, and holds the jars in her lap and her other arm around your waist, for balance.{/n}
"Thank you for coming," {n}she says to your back, somewhere near the picket line.{/n} "I would have gone alone. I would have measured the shields and written down the numbers and come home and not felt anything, and then in a hundred years I would have wondered why that chapter was wrong." {n}Her arm tightens, briefly.{/n} "It is less wrong now. That is your fault."''',
        c("[Ride on.]")),
], requires=(SCRIBE,), delay=48, RequiresAnyGroups=[list(twin_ids(DEMONS)) + list(twin_ids(ARCHITECT))])


m(INQUISITORS, "Five minutes in Kenabres", '"What have you recorded about Kenabres?"', [
    nen("open", '''{n}Nenio draws a heading on a clean sheet: KENABRES.{/n}''',
        c("Continue", "remembered_open", forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "records_open", requires=(UNREMEMBERED,)),
        c("Continue", "records_open", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("run", '''"I ran. It took five times as long to shake them off, which proved that running in heavy armour is not burdensome for an inquisitor at all. I have a table." {n}She taps a page.{/n} "Afterwards I met you. There were enough specimens in Kenabres to occupy several scholars. You were already collecting companions."''',
        c("Continue", "remember", requires=(BROUGHT_SAFE,), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "remember_sent", requires=(RECRUITMENT_REFUSED,), forbids=(BROUGHT_SAFE, UNREMEMBERED, RECREATED)),
        c("Continue", "remember_new", forbids=(BROUGHT_SAFE, RECRUITMENT_REFUSED, UNREMEMBERED, RECREATED)),
        c("Continue", "remember_new", requires=(UNREMEMBERED,)),
        c("Continue", "remember_new", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("remember", '''"I gave you an assignment: take me somewhere safe. You did. I told you I was pleased with you." {n}She taps the page.{/n} "It was a useful result. I remembered it long after I had forgotten much more distinguished people. I should like to know why."''',
        c('"What do you believe?"', "believe"),
        c('[Flirt] "And what have you written about me?"', "talk")),
    nen("remember_sent", '''"I offered to hire you. You declined and left. There was no expedition to record, only a rejection." {n}She taps the page.{/n} "Twenty-eight. I kept that number. Now you are taking dictation. I shall need to revise the table."''',
        c('"What do you believe?"', "believe"),
        c('[Flirt] "And what have you written about me?"', "talk")),
    nen("believe", '''"I believe that is an unscientific question." {n}She puts the pencil behind her ear.{/n} "Scientists do not believe. They observe, and then they decide what to think about what they observed, and the deciding is the part that nobody writes down, because it is embarrassing."
"I have not concluded. Ask when I have finished comparing the notes."''',
        c("[Leave her to compare the notes.]")),
    nen("talk", '''"'Follower: acceptable.'" {n}She shows you the page, the words written slowly enough to read.{/n} "A provisional result. Do not look so pleased. There is space beneath it for corrections."''',
        c("[Give the page back.]")),
    nen("remembered_open", '''"Measuring cultists." {n}She taps a fresh sheet.{/n} "Before the attack I tried to examine the prisoners in Kenabres. The inquisitors decided that anyone interested in cultists must be one. Five minutes to reach a verdict. I timed it."''', c("Continue", "run")),
    nen("records_open", '''"Kenabres? My records are incomplete. Your crusade has reports about it; I shall compare those before dictating an entry." {n}She leaves room at the top of the sheet.{/n} "For now, we have observations from Drezen."''', c("Continue", "remember_new")),
    nen("remember_new", '''"Our current work is much better documented than that encounter." {n}She pushes a clean sheet toward you.{/n} "I shall judge the follower by the work I can examine."''',
        c('"What do you believe?"', "believe"),
        c('[Flirt] "And what have you written about me?"', "talk")),
], requires=(SCRIBE,), delay=48, chapter=5,
    RequiresAnyGroups=[list(twin_ids(PAGE_ONE))])


m(MARKET, "A census of the market", '"How many people have you measured today?"', [
    nen("open", '''"Two hundred and eleven. Two hundred and twelve, now; you are taller than yesterday, which is impossible, so you are standing differently." {n}She has a ledger open on @DESK@ with columns in it: height, weight estimated, gait, smell, and a last column headed simply "?".{/n}
"Drezen is an excellent laboratory. Everyone in the crusade passes through this market sooner or later, and none of them notices a woman writing, because a woman writing is invisible in a market. It is the single most useful thing I have discovered since I arrived."''',
        c('"What goes in the question-mark column?"', "question"),
        c('"Aren\'t you lonely, out here on your own?"', "lonely")),
    nen("question", '''"Whatever I cannot classify." {n}She runs her finger down it.{/n} "A Mendevian knight who wept at a pie stall. A dwarf who bought a single cinnamon stick every day and never used it. A tiefling child who stole a pear and paid for it afterwards, which I cannot explain at all."
"And you. You are in the question-mark column every day. I have tried moving you to the others. You do not stay."''',
        c("Continue", "stay")),
    nen("lonely", '''"Loneliness is a sign of uniqueness. The one who leads the way is always alone." {n}She says it like a creed, and then she looks at the empty crate beside her own, which she has not given back to the spice trader, although he has asked.{/n}
"I keep that one empty for whoever is taking dictation," {n}she says.{/n} "Nobody usually is. I keep it empty anyway. It is a habit. It is probably irrelevant."''',
        c("Continue", "stay")),
    nen("stay", '''"Sit, if you are going to stand there. You are casting a shadow on my columns." {n}She shifts along. There is exactly room.{/n}
"The spice trader has asked me four times to give back his crates. I have explained to him that they are now scientific equipment. He has asked the market wardens to explain it back to me. They have not managed." {n}She pushes the ledger across to you and the pencil after it.{/n} "Take the next ten. I shall dictate. Tall man, limping, left. Write: 'veteran, Third Crusade, or wants to be taken for one.'"''',
        c("[Take the next ten.]"),
        c('[Flirt] "And me? What would you write about me?"', "me")),
    nen("me", '''"'Question mark.'" {n}She does not look up.{/n} "'Persistent.' That is all I have been able to establish. It has taken weeks." {n}She taps the last column.{/n} "Tall woman with a basket, right. Write."''',
        c("[Write.]")),
], requires=(SCRIBE, VISITOR), delay=48, places=("visitor", "arcade"))


hub4(DRINK, "Once a year, where nobody sees", '"You\'re up late."', [
    nar("open", '''{n}The camp is asleep except for the sentries, and the sentries are facing outward, and Nenio has found the one spot on the terrace that neither of them can see. She is sitting on the flagstones with a bottle of something Abyssal, uncorked, and two cups, and when you come past she holds one of them up without a word.{/n}''',
        c("Continue", "rule")),
    nen("rule", '''"Once a year. And only if no one sees me." {n}She pours, badly.{/n} "I have a reputation to maintain. The Abyss seemed the safest place in the multiverse for it. Nobody I respect is watching, and nobody who is watching will be believed."
"You are not nobody. I have made an exception. The experiment requires a witness who can be trusted to report accurately and then never mention it again."''',
        c("[Sit, and drink with her.]", "drink"),
        c('"Is this for science?"', "science")),
    nen("science", '''"Everything is for science." {n}She drinks, and makes a face that would curdle milk.{/n} "That is disgusting. The demons of this city have had ten thousand years to learn to make wine, and they have learned to make this." {n}She drinks again.{/n} "No. This one is not for science. It is for once a year."''',
        c("[Sit, and drink with her.]", "drink")),
    nar("drink", '''{n}It is disgusting. It is also strong, and by the third cup the terrace has gone soft at the edges and the Abyssal sky has become almost beautiful, in the way a bruise can be beautiful if you stop minding that it is a bruise.{/n}
{n}Nenio has taken off her boots and is sitting with her bare feet out in front of her, wiggling her toes at the harbour.{/n}''',
        c("Continue", "honest")),
    nen("honest", '''"I am going to say something now that I shall forget in the morning," {n}she announces.{/n} "I shall forget it on purpose. So you may as well hear it; it will not count."
"I have been leaving a space for you in every entry. You know that. What you do not know is that when I dictate the word 'Commander', I hear it in my own head, the whole time, with the name in it. The space is a lie. The space was always a lie." {n}She points her cup at you.{/n} "There. It is out. It does not count. I am very drunk and I am a scientist of great standing and none of this is happening."''',
        c("Continue", "honest_filed", requires=(NAME_GONE,)),
        c("[Say nothing, and pour her another half cup.]", "pour", forbids=(NAME_GONE,)),
        c('"Then fill it in."', "fill", forbids=(NAME_GONE,))),
    nen("honest_filed", '''{n}She frowns, and puts the cup down.{/n} "No. That was true once. It is not true now. I paid it away. Now there is only the space, and I hear the space, the whole time, like a note on a lute that is not being played." {n}She laughs, and it wobbles.{/n} "I cannot tell which is worse. I shall decide in the morning, and then forget I decided."''',
        c("[Say nothing, and pour her another half cup.]", "pour")),
    nen("pour", '''"Thank you." {n}She drinks it, and leans against your shoulder, and does not appear to notice that she has.{/n} "You are a very good witness. You do not interrupt. You do not write anything down. You are completely useless as a scientist and I am extremely glad you are here."
{n}Then she closes her eyes, and some while after that she opens them again, crystal clear, sits up very straight, and says, "All right. I am fine now." She puts her boots back on. She does not look at you. She does not let go of your sleeve, either, until you are both back among the tents.{/n}''',
        c("[See her back to her tent.]")),
    nen("fill", '''"No." {n}At once, drunk and absolute.{/n} "A space is filled when the thing becomes relevant, and the deciding is mine, and I am not deciding anything tonight, because tonight does not count." {n}She leans against your shoulder, heavily.{/n} "Ask me when I am sober. No. Do not ask me. Let me ask. I shall know when."
{n}Then she closes her eyes, and some while after that opens them again, crystal clear, sits up very straight, and says, "All right. I am fine now." She puts her boots back on. She does not let go of your sleeve until you are both back among the tents.{/n}''',
        c("[See her back to her tent.]")),
], requires=(SCRIBE,), delay=48, RequiresAnyGroups=[[LAMP, SHOULDER]])


# Between the voided night and her question: she works, and does not look up.
m(VOID_DAYS, "The margins", '"Nenio?"', [
    nen("open", '''"Busy." {n}She does not look up from @DESK@. She has volume one open, and she is going through it page by page with a magnifying glass, and every time she finds one of your initials in a margin she draws a very small, very neat circle around it and writes the page number on a list.{/n}''',
        c('"Let me explain."', "explain"),
        c('"How many have you found?"', "count"),
        c("[Leave her to it.]", abort=True)),
    nen("explain", '''"Not yet." {n}She turns a page.{/n} "When I have finished the evidence, I shall ask the question. Before that, anything you say is testimony without an examination, and testimony without an examination is gossip."
"Come back in three days. I shall have a list, and a comparison of pencil strokes, and one question. Answer the question." {n}She still does not look up.{/n} "Do not answer anything else. I would not be able to forget it, and I have enough of those."''',
        c("[Leave her to it.]")),
    nen("count", '''"Eleven." {n}Flatly.{/n} "And the sketch. Eleven initials and a sketch, placed with care, in the places I look most often. Whoever did this knows exactly which pages I read when I cannot sleep." {n}She turns a page, and circles something.{/n} "That is a very small list of people. Come back in three days. I shall have one question. I would like it answered truthfully. I would like that very much."''',
        c("[Leave her to it.]")),
], requires=(P + "declined", P + "tampered"), forbids=(COMMITTED,), delay=24)


# --- The bite she promised to test, the box marked KENABRES?, and the answer owed to the Sphinx. ------------------------------

TEETH = F + "teeth"
KENABRES_BOX = F + "kenabres_box"
SPHINX_LIST = F + "sphinx_list"
BITTEN = F + "teeth.bitten"

m(TEETH, "A test of the bite", '"You\'re looking at my mouth again."', [
    nen("open", '''"I am. It is overdue." {n}She has a small mirror, a spatula of the kind used by physicians and a sheet headed BITE, CIVILISED, CORRELATIONS.{/n}
"Soldiers tell me, when I examine their teeth, that they could bite hard enough if somebody got on their nerves. All of them. Not one has ever let me measure it. I have been waiting for a suitable subject, and a suitable occasion, and I have concluded that there will never be an occasion, and that I must simply create the conditions."''',
        c('"What conditions?"', "conditions"),
        c('"You want me to bite you."', "direct"),
        c('"I told you in the camp. If somebody gets on my nerves, I can bite hard enough."', "told", requires=(TOLD_BITE,))),
    nen("told", '''"You did. It is in your file, under 'claims, unverified'." {n}She taps the sheet.{/n} "Most people who say that are boasting. I am going to find out whether you are, and then I am going to move it to the other column, or cross it out in front of you."''',
        c("Continue", "arm")),
    nen("conditions", '''"Irritation, primarily. The bite is a response to irritation; that is the hypothesis." {n}She considers you.{/n} "I have spent a great deal of time trying to irritate you, with poor results. You simply write it down. So I shall have to take the measurement without the irritation, which is methodologically weak, but I am prepared to live with it."''',
        c("Continue", "arm")),
    nen("direct", '''"I want to measure the force of a civilised bite in a subject who has claimed it could be considerable." {n}Very primly.{/n} "Whether it is me that is bitten is incidental. I considered a cheese. A cheese has no nerve endings, and I wish to know what it feels like; the Encyclopedia is otherwise going to be very thin on the subject."''',
        c("Continue", "arm")),
    nen("arm", '''{n}She rolls her sleeve up past the elbow, which releases three crumpled pages, a pencil stub and what appears to be a dried beetle, and holds out her forearm, pale on the inside, with the veins blue under the skin.{/n}
"Here. Not the wrist; the wrist is for pulses. Moderate force. I shall count. Then I shall describe it." {n}She looks away, at the Worldwound's glow, as if bracing for an injection.{/n} "Begin whenever you like. Now or never; that is my motto."''',
        c("[Bite, gently, and hold it.]", "gentle", flags=(BITTEN,)),
        c("[Bite properly.]", "hard", flags=(BITTEN,)),
        c("[Kiss the inside of her arm instead.]", "kiss")),
    nen("gentle", '''{n}You take her arm in both hands and set your teeth against the soft inside of it, not hard, and hold. She stops counting at three. She makes a noise that is not a word in any language she has ever catalogued.{/n}
"That," {n}she says, when you let go,{/n} "was not moderate force. That was a completely different variable." {n}There is a faint pink crescent on her skin. She looks at it, and then at you, and her pupils are enormous.{/n} "I shall have to describe it. I do not have the words. I have more words than anyone alive and none of them are the right ones. This is intolerable."''',
        c("Continue", "record")),
    nen("hard", '''{n}You bite properly. She yelps, loud enough to turn a sentry's head, and snatches the arm back and looks at the marks, a clean double crescent, already reddening.{/n}
"Considerable!" {n}She sounds delighted.{/n} "Considerable force! The soldiers were not boasting after all. Or you were not." {n}She rubs the arm, and does not stop looking at the marks, and her breathing has gone quick in a way that has nothing to do with pain.{/n} "I shall need to measure it. The radius. The depth. Keep your jaw where it is while I... no. Give me your jaw. I shall measure you."''',
        c("Continue", "record")),
    nen("kiss", '''{n}You put your mouth to the inside of her arm, just below the elbow, where the skin is thinnest, and leave it there.{/n}
{n}She does not pull away. She does not count either. When you lift your head her eyes are closed and her ears are flat back against her hair.{/n}
"That," {n}she says, without opening her eyes,{/n} "was not a bite. That was a control. You have given me the control before the experiment. That is backwards." {n}She opens her eyes.{/n} "It was also a very good control. Now bite."''',
        c("[Bite, gently, and hold it.]", "gentle", flags=(BITTEN,)),
        c('"Another day."', "record")),
    nen("record", '''{n}She rolls her sleeve down over whatever is on her arm now, slowly, and smooths it.{/n}
"The entry will say that a civilised bite is civilised in form only, and that the author tested it on herself, in the field, and found the results... incompatible with further study at this time." {n}She writes it down. Her handwriting is worse than usual, which is an achievement.{/n}
"That is a lie. The results are entirely compatible with further study. I am simply not telling the students of Absalom about the further study." {n}She sniffs.{/n} "Go away. I have to describe this, and I cannot do it while you are standing there with that mouth."''',
        c("[Go away, with that mouth.]")),
], requires=(SCRIBE,), forbids=(COMMITTED,), delay=48, RequiresAnyGroups=[list(twin_ids(PULSE)) + list(twin_ids(RHYMES))])


m(KENABRES_BOX, "KENABRES?", '"You\'ve drawn a box round a word."', [
    nen("open", '''"I have." {n}Her volume one is open on @DESK@ at the flyleaf. In the margin, in her impossible hand, is the only word on the page anybody could read: KENABRES?, with a box ruled round it, and the box gone over so many times that the pencil has nearly worn through the paper.{/n}
"I have records of places I have never been. I have records of places that do not exist, for comparison. I have no record of Kenabres at all. It is the only hole in my geography that is the exact shape of a city." {n}She turns the book to face you.{/n} "You said, the day we met, that we had met once before, in Kenabres, and that it went badly. I have been considering 'badly'. Tell me."''',
        c('"I killed you in Kenabres. Then I paid the Sphinx to make you again. She did not return that memory."', "truth"),
        c('[Lie] "A misunderstanding at the gate. You were arrested; I didn\'t help. That\'s all."', "lie"),
        c('"Some things are better in a box."', "box")),
    nen("truth", '''"You killed me." {n}Her pencil remains above the page.{/n} "And then bought a vessel without that memory. You have been taking my dictation. This belonged in the record before anything else. I shall have to examine the source."''',
        c('"I didn\'t know how."', "how"),
        c('"I was afraid you\'d leave."', "how")),
    nen("how", '''{n}She writes your account beneath KENABRES?, then closes the book.{/n} "I do not remember it. That does not make your account harmless. Leave it with me. I shall read it again, then decide what I think of the person who did it." {n}She puts her hand flat on the cover.{/n} "Your account is recorded. Do not ask me to forgive you while I am still reading it."''',
        c("[Leave the account with her.]", flags=(KENABRES_TOLD,))),
    nen("lie", '''"Arrested at the gate." {n}She writes it down beside the box, slowly, in a hand you can read.{/n} "Five minutes. That is the time it takes the inquisitors of Kenabres to find anyone guilty; I know that somehow. I do not know how I know it." {n}She looks at the box, and at your account beside it, and at you.{/n}
"It fits," {n}she says.{/n} "It fits very neatly." {n}She rubs out the question mark, and leaves the box around the word.{/n} "I dislike things that fit very neatly. But I have no other data."''',
        c("[Let it stand.]", flags=(KENABRES_LIED, KENABRES_SECRET))),
    nen("box", '''"Better in a box for whom?" {n}She looks at you for some time.{/n} "Very well. It stays in a box. I shall not open it. That is not the same as forgetting it; I want that understood. I will leave the question mark. When I open it, I shall expect an answer."''',
        c("[Leave the box shut.]")),
], requires=(SCRIBE, UNREMEMBERED, KENABRES_SAID), forbids=(DEBT_DEFAULTED,), delay=72, places=("visitor", "arcade"), chapter=5)


m(SPHINX_LIST, "One answer, owed", '"What\'s this list?"', [
    nen("open", '''"Preparation." {n}The list is on three sheets pinned edge to edge, and it has grown columns.{/n} "You owe the Faceless Sphinx one answer, when she asks, any question, the true answer, not a riddle. I have found out. It was not difficult; I am very good at finding things out, and you talk in your sleep."
"You bought me with a debt you cannot see the bottom of. That is very poor accounting. So I am doing the accounting." {n}She taps the first column.{/n} "These are the questions she is likely to ask. These are the answers you are likely to give. These are the answers you must on no account give, and why."''',
        c('"How many questions?"', "how_many"),
        c('"You don\'t have to do this."', "have_to")),
    nen("how_many", '''"Three hundred and six. So far." {n}She does not blink.{/n} "She is a demon lord of secrets. She will not ask where you were born. She will ask something you have never asked yourself, and she will know it before you do, and she will want to watch you find out." {n}She runs her finger down the second column.{/n} "Number forty-one: 'What did you give up for her?' The only safe answer is the true one. I have written it in. It is my notes. I have spelled out the whole inventory, to spare you counting."''',
        c("Continue", "forty_two")),
    nen("have_to", '''"I do not have to do anything. I am four thousand years old and a scientist of great standing." {n}She does not stop writing.{/n} "I want to. I am the reason for the debt. A debt is an experiment with a result nobody has recorded yet. I intend to record it first."''',
        c("Continue", "forty_two")),
    nen("forty_two", '''"Number forty-two." {n}She reads it without looking at you.{/n} "'Was she worth it?'"
{n}She puts the pencil down. The second column beside that line is empty. So is the third.{/n}
"I have not been able to write your answer to that one. I have tried every night for a week. I keep leaving it blank." {n}Her ears are flat.{/n} "You will have to give it yourself, when she asks. I would rather not be in the room."''',
        c('"Write \'yes\'."', "yes"),
        c('"I\'ll answer it when she asks. Truthfully. You won\'t like how long it takes."', "long"),
        c("[Take the pencil and write the answer yourself, where she can't see.]", "write")),
    nen("yes", '''"No." {n}Quickly.{/n} "I cannot write your answers for you. That is the whole point of the column. And 'yes' is a conclusion, and conclusions are observed, not..." {n}She stops herself, and looks at you, and something in her face gives.{/n} "Say it aloud, then. Once. I shall not write it down. I shall only have heard it."''',
        c("Continue", "end")),
    nen("long", '''"Good." {n}She almost smiles.{/n} "Take a very long time. Make the Sphinx wait. Nobody has ever made her wait; she is going to find it extremely instructive, and I am going to write it down afterwards, from memory, in detail."''',
        c("Continue", "end")),
    nen("write", '''{n}She turns her back while you do it, rigidly, with her arms folded. When you hand back the sheet she folds it over at that line, so that the answer is on the inside, and presses the fold flat with her thumbnail, twice.{/n}
"I shall not read it," {n}she says.{/n} "It is yours to give. I am only keeping it where it will not get wet."''',
        c("Continue", "end")),
    nen("end", '''{n}She pins the sheets back together and rolls them up and ties them with string.{/n}
"Three hundred and six questions. One of them she will ask. I shall have the answer ready, whichever it is." {n}She sniffs.{/n} "Except forty-two. Forty-two is yours. I have ruled a space."''',
        c("[Leave her to her columns.]")),
], requires=(SCRIBE, MANUSCRIPT, OWES), forbids=DEBT_SETTLED, delay=48, chapter=5)


# --- The friendship article, revisited (only if she concluded it; her own point five, and the model she could not credit). ------

POINT_FIVE = F + "point_five"

m(POINT_FIVE, "Point five, a correction", '"That\'s the friendship article."', [
    nen("open", '''{n}Nenio heads a fresh sheet FRIENDSHIP, POINT FIVE.{/n}''',
        c('"Maybe the error is the conclusion."', "conclusion", forbids=("trickster.ever",)),
        c('"What happened to the sketch?"', "sketch", requires=(FRIEND_SKETCH,), forbids=("trickster.ever", UNREMEMBERED, RECREATED)),
        c('[Flirt] "Point five went badly. That\'s your error."', "five", forbids=("trickster.ever",)),
        c('"What did you record instead?"', "no_sketch", forbids=("trickster.ever", FRIEND_SKETCH, UNREMEMBERED, RECREATED)),
        c("Continue", "review_retained", forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "review_new", requires=(UNREMEMBERED,)),
        c("Continue", "review_new", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("conclusion", '''"Point five: no copulation observed. That records this trial. It does not settle the whole subject of friendship."''',
        c("Continue", "five")),
    nen("sketch", '''{n}She adds a heading to the review: DRAWING.{/n}''',
        c("Continue", "credit", requires=(FRIEND_CREDIT,), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "drawing", requires=(FRIEND_SKETCH,), forbids=(FRIEND_CREDIT, UNREMEMBERED, RECREATED)),
        c("Continue", "record_unknown", requires=(UNREMEMBERED,)),
        c("Continue", "record_unknown", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "record_unknown", forbids=(FRIEND_SKETCH, FRIEND_CREDIT, UNREMEMBERED, RECREATED))),
    nen("five", '''{n}Nenio leaves a line for the result beneath point five.{/n}''',
        c('"And now?"', "now", forbids=("trickster.ever",)),
        c('"You could run it again."', "again", forbids=("trickster.ever",)),
        c("Continue", "result_refused_tongue", requires=(FRIEND_REFUSED, FRIEND_TONGUE), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "result_refused_drawing", requires=(FRIEND_REFUSED, FRIEND_SKETCH), forbids=(FRIEND_TONGUE, UNREMEMBERED, RECREATED)),
        c("Continue", "result_refused", requires=(FRIEND_REFUSED,), forbids=(FRIEND_SKETCH, FRIEND_TONGUE, UNREMEMBERED, RECREATED)),
        c("Continue", "result_tongue", requires=(FRIEND_TONGUE,), forbids=(FRIEND_REFUSED, UNREMEMBERED, RECREATED)),
        c("Continue", "result_drawing", requires=(FRIEND_SKETCH,), forbids=(FRIEND_REFUSED, FRIEND_TONGUE, UNREMEMBERED, RECREATED)),
        c("Continue", "result_unknown", forbids=(FRIEND_REFUSED, FRIEND_SKETCH, FRIEND_TONGUE, UNREMEMBERED, RECREATED)),
        c("Continue", "result_unknown", requires=(UNREMEMBERED,)),
        c("Continue", "result_unknown", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("now", '''"Now I am going to issue an erratum." {n}She takes the pencil from behind her ear and writes, in small, careful, legible capitals, at the foot of point five: "SEE ALSO: FOLLOW-UP, PENDING." Then she looks at it, and her ears go back, and she leaves it where it is.{/n}
"It is a footnote," {n}she says.{/n} "Not a conclusion. A footnote is a promise that there is more to say. I do not know yet what it is."''',
        c("Continue", "end")),
    nen("again", '''"Run it again." {n}She says it slowly, as if the words had a taste.{/n} "A replication. With the same subject. Without the pencil." {n}She looks down at point five.{/n}
"That would be methodologically sound," {n}she says, in a voice that is not methodological at all.{/n} "I shall have to design it. Properly. With conditions. It will take some time." {n}She writes, at the foot of point five, in legible capitals: "SEE ALSO: FOLLOW-UP, PENDING."{/n}''',
        c("Continue", "end")),
    nen("end", '''{n}She sets the review beside a clean sheet.{/n}''',
        c("[Get out of the way of it.]", forbids=("trickster.ever",)),
        c("Continue", "end_drawing", requires=(FRIEND_SKETCH,), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "end_new", requires=(UNREMEMBERED,)),
        c("Continue", "end_new", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "end_new", forbids=(FRIEND_SKETCH, UNREMEMBERED, RECREATED))),
    nen("no_sketch", '''{n}She checks the account beneath the heading.{/n}''',
        c("Continue", "no_trial", requires=(FRIEND_REFUSED,), forbids=(FRIEND_SKETCH, UNREMEMBERED, RECREATED)),
        c("Continue", "record_unknown", forbids=(FRIEND_REFUSED, UNREMEMBERED, RECREATED)),
        c("Continue", "record_unknown", requires=(FRIEND_SKETCH, FRIEND_REFUSED), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "record_unknown", requires=(UNREMEMBERED,)),
        c("Continue", "record_unknown", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("no_trial", '''"No trial took place. You objected, and I was pleased to abandon it." {n}She writes that beneath the heading.{/n} "Then I concluded that friendship was foolish. I shall need a less ambitious conclusion."''', c("Continue", "five")),
    nen("record_unknown", '"No result recorded for this procedure. I cannot turn that into evidence by underlining it."', c("Continue", "five")),
    nen("credit", '''"I said I could not credit the model. I even said 'alas'." {n}She writes ATTRIBUTION beneath the account of the drawing.{/n} "Now I have a correction to make before the students see it."''', c("Continue", "five")),
    nen("drawing", '''"I began drawing instead of conducting the trial. That is the observation worth keeping." {n}She adds it to the review.{/n} "The drawing was of you. I can record that much without guessing what the experiment would have proved."''', c("Continue", "five")),
    nen("result_refused_tongue", '"I began drawing, bit my tongue, and then you objected to the trial. We stopped. No copulation. Plenty of corrections for the article."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("result_refused_drawing", '"I began drawing. Then you objected to the trial, and I was pleased to abandon it. The drawing and the refusal are separate observations."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("result_refused", '"We chose not to conduct it. No drawing, no copulation. I still have an entry to correct."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("result_tongue", '"I became absorbed in drawing and bit my tongue. No copulation took place. I documented the subject and forgot the procedure."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("result_drawing", '"I drew the subject instead of conducting the experiment. Documentation, not an observation of copulation."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("result_unknown", '"The record does not establish a trial. I shall leave \'not observed\' and correct the conclusion that followed it."',
        c('"And now?"', "now"), c('"You could run it again."', "again")),
    nen("end_drawing", '''{n}She adds the model's attribution to the review.{/n} "There. Now go away, follower. I am designing an experiment."''', c("[Get out of the way of it.]")),
    nen("end_new", '''{n}She leaves a clean sheet beside the review.{/n} "A new procedure. No conclusion yet. Go away, follower. I need to design it."''', c("[Get out of the way of it.]")),
    nen("review_retained", '''"It is a review of it." {n}She heads a fresh sheet FRIENDSHIP, POINT FIVE.{/n} "I concluded that the whole occupation was foolish. The evidence is less satisfactory. I am checking point five before the entry goes to a printer."''',
        c('"Maybe the error is the conclusion."', "conclusion"),
        c('"What happened to the sketch?"', "sketch", requires=(FRIEND_SKETCH,), forbids=(UNREMEMBERED, RECREATED)),
        c('[Flirt] "Point five went badly. That\'s your error."', "five"),
        c('"What did you record instead?"', "no_sketch", forbids=(FRIEND_SKETCH, UNREMEMBERED, RECREATED))),
    nen("review_new", '''"Your account says that I called friendship foolish. It does not give a result for point five. I shall review the observations, not borrow the conclusion."''', c("Continue", "five")),
], requires=(SCRIBE, FRIEND_DONE), forbids=(COMMITTED,), delay=48, places=("hub",),
    RequiresAnyGroups=[list(twin_ids(DEMONS)) + list(twin_ids(ARCHITECT))])


# Authored follow-up to the existing account; continuing work buys no romantic yes.
m(F + "kenabres_judgment", "The source examined", '"Have you read the account?"', [
    nen("open", '''{n}Nenio has your account open beside her notes on the crusade. She reads its last line, folds it, and looks directly at you.{/n} "I have read it again. I believe you killed me. I also believe you paid to have me made again. The second observation does not cancel the first."''', c("Continue", "judgment")),
    nen("judgment", '''"I will continue the work. With you, for now. I want to know what you do when you cannot erase the inconvenient part of an account." {n}She sets a clean page between you.{/n} "I have not forgiven you. I have decided to remain. Those are different entries."''',
        c('"Leave both entries. I will not ask you to erase either."', "continue_work"),
        c('"I brought you back. You owe me forgiveness."', "close"),
        c('"Then we should end this."', "part")),
    nen("continue_work", '''"Good. Hold the page." {n}She places the pencil in your hand and keeps her other hand on the folded account.{/n} "We start with what we can observe. Write the date. I want this page legible."''', c("[Take dictation.]")),
    nen("close", '''"No. The bargain was with the Sphinx. You did not buy my judgment." {n}She takes the clean sheet back.{/n} "I shall find another follower. Leave."''', c("[Leave.]", flags=(CLOSED,))),
    nen("part", '''"Then we end it." {n}She writes the date beneath your account.{/n} "I will keep the evidence. You will keep out of my notes."''', c("[Go.]", flags=(CLOSED, P + "refused_her"))),
], requires=(SCRIBE, UNREMEMBERED, KENABRES_TOLD), delay=72, chapter=5, places=("visitor", "arcade"))
