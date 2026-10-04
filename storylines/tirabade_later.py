"""Further shared Tirabade scenes, keeping the original save identifiers intact."""
from story_format import c, n, scene

SCENES = [scene("three_locks", "A respectable use for a bad habit", "Together", 3,
    '"Have you two decided what we are doing with our next evening?"', [
    n("start", "Anevia", '''"Depends. Can you keep your hands steady when someone's watchin'?"
{n}Anevia puts a small wooden box on the bench beside you. Three mismatched padlocks hang from its hasp.{/n}
"Before Beth starts: mine, bought honestly, not evidence, and there's nothin' alive in it."
{n}Irabeth arrives carrying a folded cloth and a lantern.{/n}
"I was going to ask whether you remembered the keys."
"That too. But I liked my version better."''',
      c('"What is in the box?"', "box"),
      c('"I take it this is a lesson."', "lesson"),
      c('[Arrange another time when you can stay.]', abort=True)),
    n("box", "Irabeth", '''"Three suggestions for an evening. We each wrote one before you arrived. Yours is the blank piece of paper."
{n}Anevia produces a narrow roll of tools.{/n}
"Whoever opens a lock gets to argue for a suggestion. If all three of us manage it, we'll have to do somethin' dreadful like make plans together."
"The locks were her addition," Irabeth says.
"You said you wanted a challenge."
"I meant an evening without work. Apparently I should have been more precise."''', c('[Make room for the box.]', "lesson")),
    n("lesson", "Anevia", '''{n}You take the box to a sheltered corner of the courtyard. Anevia spreads the cloth beneath it and sets two tools on your palm.{/n}
"The cloth catches what you drop. Beth's improvement. Saves crawlin' about on your knees pretendin' that was part of the lesson."
{n}Irabeth sits on your other side and adjusts the lantern.{/n}
"I have been practicing."
{n}Anevia's head turns.{/n}
"Have you, now?"
"You leave that box open whenever you go looking for the keys."
{n}For a moment Anevia looks as if she cannot decide whether to be proud or offended. Pride wins.{/n}
"That's my wife."''',
      c('"Anevia, show me how you would begin."', "anevia"),
      c('"Irabeth, I would like to see what you have learned."', "irabeth")),
    n("anevia", "Anevia", '''{n}Anevia settles close enough that her shoulder touches yours. She guides one tool into the oldest lock, then lays a finger lightly over your hand.{/n}
"Less force. You're listenin' through your fingers, not demandin' an answer."
{n}The lock gives a faint click. You begin to turn the tool, and she stops you.{/n}
"Nearly. That's the bit where I used to get impatient."
"Used to?" Irabeth asks.
{n}Anevia ignores her with considerable effort.{/n}
"Try it again. Slower."''',
      c('[Follow her guidance.]', "guided", flags=("three_locks.anevia_taught",)),
      c('"Your hand is making it difficult to concentrate."', "distracted")),
    n("distracted", "Anevia", '''"Terrible. I'll report myself."
{n}She removes her hand, though not her shoulder.{/n}
"Better?"
{n}Across the box, Irabeth makes a small sound suspiciously unlike a cough.{/n}
"I believe you promised to teach."
"I am. There's a whole lesson in distractions. Very advanced."''',
      c('[Give the lock your attention again.]', "guided", flags=("three_locks.anevia_taught",))),
    n("guided", "Narrator", '''{n}On the next attempt, the lock opens. Anevia grins at you before remembering to look as though she expected nothing less.{/n}
{n}"There. Nicely done."{/n}
{n}Irabeth lifts the opened lock from the hasp and lays it on the cloth.{/n}
{n}"And now she will tell everyone she taught the Commander patience."{/n}
{n}"Only people who'd enjoy hearin' it."{/n}''', c('[Pass the tools to Irabeth.]', "beth_turn")),
    n("irabeth", "Irabeth", '''{n}Irabeth takes the tools. Her first attempt produces a scrape. Anevia opens her mouth, then closes it when her wife looks up.{/n}
"I know. Too much pressure."
{n}On the second attempt, Irabeth pauses after the click. The lock opens. She lays it on the cloth.{/n}
{n}Anevia leans forward to inspect it.{/n}
"You really have been practicin'. Behind my back."
"You told me to surprise you."
"I meant with supper."''',
      c('[Give Irabeth time to enjoy her success.]', "beth_proud", flags=("three_locks.irabeth_taught",))),
    n("beth_proud", "Irabeth", '''"I know. You are very surprised to find that someone else can be secretive."
{n}She is smiling now. Anevia reaches across you to squeeze her wife's wrist, and Irabeth turns her hand to catch the offered fingers.{/n}
"Your turn," Irabeth tells you. "You have the advantage of seeing exactly which mistake to avoid."''', c('[Let her show you the second lock.]', "your_turn")),
    n("beth_turn", "Irabeth", '''{n}Irabeth studies the second lock before touching it. Anevia watches her hands with an attention she has not bothered to disguise.{/n}
"You can look at my face occasionally," Irabeth says.
"Know what your face looks like."
"So you keep telling me."
{n}The lock clicks open. Anevia's smile answers the satisfaction in her wife's face.{/n}''', c('[Set the second lock aside.]', "last")),
    n("your_turn", "Irabeth", '''{n}Irabeth points out where she found resistance and waits while you try. When your hand slips, she steadies the box instead of taking the tools away.{/n}
"Again. There is no one waiting on the other side of a door."
{n}Anevia rests her chin on her folded arms and watches. It takes longer than you hoped, but eventually the lock opens.{/n}
"Good," Irabeth says, with enough pleasure that you look up from the hasp.''', c('[Set the second lock aside.]', "last")),
    n("last", "Anevia", '''{n}Anevia takes the final lock with the air of someone about to restore the proper order of things. It does not open.{/n}
{n}She tries again. Irabeth reaches into her pocket and sets a key beside the box.{/n}
"That one sticks. I meant to tell you before we came out."
{n}Anevia looks at the key, then at her wife.{/n}
"You could've told me just now."
"I could."
{n}Anevia laughs. She uses the key without further ceremony.{/n}''', c('[Open the box together.]', "plans")),
    n("plans", "Narrator", '''{n}Inside are three folded pieces of paper. Anevia's proposes finding somewhere to hear music without being asked to make a speech. Irabeth's proposes a walk outside the busiest streets, followed by a meal she has no intention of helping to prepare.{/n}
{n}The third page is blank. Anevia passes you a pencil.{/n}
{n}"Go on. Tell us what you want."{/n}''',
      c('[Write: music first, and a walk home when we have had enough.]', "music", flags=("three_locks.music",)),
      c('[Write: the meal first, somewhere we can stay as long as we like.]', "meal", flags=("three_locks.meal",))),
    n("music", "Anevia", '''"Good. Beth can rescue us if I pick somewhere dreadful."
"You picked our last dreadful place deliberately."
"Had a very nice door to leave through."
{n}Irabeth shakes her head and gets up to collect the lantern. Anevia catches her free hand as she passes. Both look to you as you suggest a day.{/n}''', c('[Arrange the evening together.]', flags=("three_locks.planned",))),
    n("meal", "Irabeth", '''"Then we choose somewhere that will feed us before anyone recognizes our titles."
"That's a disguise problem," Anevia says. "I can help."
{n}Irabeth gives her a long look.{/n}
"Ordinary clothes."
"You take all the adventure out of things."
{n}Anevia is still smiling when you suggest a day, and Irabeth reaches for the pencil to write it down.{/n}''', c('[Arrange the evening together.]', flags=("three_locks.planned",))),
], requires=("ordinary", "kept_terms"),
    forbids=("closed", "loss", "inhuman", "irabeth_away", "anevia_away", "last_watch"), delay=48, optional=True,
    ForbidOverrides={"last_watch": "three_progression.catchup_requested"},
    Relationship="tirabade", Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[3, 5])]

SCENES.append(scene("three_outing", "The evening on the folded page", "Together", 3,
    '"We chose an evening. Shall we keep it?"', [
    n("start", "Irabeth", '''{n}Irabeth has changed into a plain shirt and a coat without insignia. Anevia stands behind her, straightening a fold at the shoulder.{/n}
"You are making it worse," Irabeth says.
"Keep movin' and I'll make it interesting."
{n}Anevia steps back to inspect her work, then notices you watching.{/n}
"Ready? She's been ready for a quarter of an hour. Keeps inventin' things to check so I won't notice."
{n}Irabeth takes her wife's hand before she can begin another adjustment.{/n}
"We can leave now."''',
      c('[Go to hear the music you chose.]', "music", requires=("three_locks.music",)),
      c('[Go out for the meal you chose.]', "meal", requires=("three_locks.meal",)),
      c('[Explain that something has changed, and arrange another evening.]', abort=True)),
    n("music", "Anevia", '''{n}The room Anevia has chosen is crowded enough to be warm without a fire. A fiddler stands on a low platform, stamping time with one boot. You find space near the end of a bench. Anevia brings over a cup of cider and sets it safely out of the way of passing elbows.{/n}
"No speeches," Anevia says, sounding pleased. "Can't hear yourself think, never mind deliver one."
{n}Irabeth leans close to answer. Anevia turns her head to listen, and their foreheads nearly meet.{/n}
"What?"
"I said, can you hear anything but the drum?"
"Drummer's very committed."
{n}You can feel the beat through the bench. Irabeth winces at a particularly determined flourish.{/n}''',
      c('"Let us stay for one tune, then take our walk."', "one_tune"),
      c('[Point out a quieter place near the far wall.]', "far_wall")),
    n("one_tune", "Irabeth", '''"One tune. I would like to hear you both afterward."
{n}Anevia looks toward the platform, then back at her wife.{/n}
"Pick a good one, then. Don't waste our single tune on whatever she's doin' now."
{n}Irabeth catches the fiddler's attention between pieces and names a tune. The woman nods. When she begins, the drummer puts down his sticks and listens.{/n}
{n}Anevia's surprise lasts only a moment before she offers Irabeth her hand.{/n}
"Well. If you're goin' to arrange things that neatly."''', c('[Make room for them to stand.]', "dance")),
    n("far_wall", "Anevia", '''{n}Anevia retrieves her cup and finds a gap through the crowd. You make room for yourselves on a bench against the far wall, where the fiddle rises above the drum instead of struggling beneath it. Anevia sets her cup beside her before turning to you both.{/n}
"Better," Irabeth says.
"Good. Now you can hear me say you look lovely."
{n}Irabeth gives her a sideways look.{/n}
"You could have said that while you were pulling at my coat."
"Didn't want you gettin' complacent."
{n}The next tune is slower. Anevia offers her wife a hand, and Irabeth takes it.{/n}''', c('[Watch them take a turn together.]', "dance")),
    n("dance", "Narrator", '''{n}They do not attempt anything elaborate. There is barely room to turn, and Anevia laughs when Irabeth steers them around a chair as carefully as if it were a siege engine.{/n}
{n}Then Anevia says something too quiet for you to hear. Irabeth's expression softens. For a few steps they forget the room, until someone jostles them and Anevia remembers to look indignant.{/n}
{n}When they return, Irabeth reaches toward you.{/n}
{n}"Your turn, if you want one."{/n}''',
      c('[Take Irabeth\'s hand.]', "beth_dance"),
      c('"Anevia, will you dance with me?"', "anevia_dance"),
      c('"I am enjoying watching you both. Stay with me for the end of the tune."', "listen")),
    n("beth_dance", "Irabeth", '''{n}Irabeth draws you into the little space the dancers have left. Her hand settles at your back; she smiles when you find the rhythm together.{/n}
"Tell me if I tread on you. Anevia claims I improve only when threatened."
{n}You turn. Anevia raises her cup in a small salute. Irabeth answers with a smile before drawing your attention back to her.{/n}
{n}At the end of the tune, she keeps your hand until all three of you have found each other again.{/n}''', c('[Leave together for the walk home.]', "walk", flags=("three_outing.beth_dance",))),
    n("anevia_dance", "Anevia", '''"Thought you'd never ask. Well, I was givin' you another minute."
{n}Anevia takes your hand. Her movements are small and assured; when another couple comes too close, she turns the collision into a change of direction and grins at you.{/n}
"See? Completely planned."
{n}Irabeth waits at the edge of the room, holding Anevia's cup. As the tune ends, Anevia leans toward her to reclaim it and steals a brief kiss instead.{/n}
"Better than the drink," she says, then reaches back for you.''', c('[Leave together for the walk home.]', "walk", flags=("three_outing.anevia_dance",))),
    n("listen", "Anevia", '''{n}Anevia settles beside you. Irabeth stays standing close enough that you can hear her humming the melody.{/n}
"She knows all the words," Anevia murmurs. "Won't sing 'em unless you catch her at the right moment."
"You are not going to make this the right moment by announcing it."
{n}Anevia laughs and rests her head briefly against Irabeth's arm. You listen together until the tune ends.{/n}''', c('[Leave together for the walk home.]', "walk", flags=("three_outing.listened",))),
    n("meal", "Irabeth", '''{n}The place you choose has a short menu and a window overlooking a narrow lane. Irabeth reaches for the chair beside the window. Anevia pauses at the other side of the table, looking from the window to the door.{/n}
"You can see both from here," Irabeth tells her, shifting the chair facing the door a little.
{n}Anevia sits, caught in a habit she had hoped no one would notice.{/n}
"Wasn't goin' to say anything."
"I know. I would like you to taste your supper."
{n}Irabeth takes the window chair and opens the menu. You take the third place, between her view of the lane and Anevia's view of the room.{/n}''',
      c('"What would you order if you did not have to be sensible?"', "order"),
      c('"We promised you a meal you would not have to organize, Irabeth. Let us choose."', "choose")),
    n("order", "Irabeth", '''"The pie. I have been thinking about the pie since we passed the window."
{n}Anevia leans over to inspect the menu.{/n}
"It's listed under sweets."
"I can read."
{n}Anevia looks at you, delighted.{/n}
"This is what happens when you let her out without a schedule."''', c('[Order something sweet before anything sensible.]', "supper", flags=("three_outing.sweets_first",))),
    n("choose", "Anevia", '''"Right. Put it down, Beth. You're off duty."
{n}Irabeth relinquishes the menu, but keeps watching it until you turn it out of her line of sight.{/n}
"One thing. The pie. Everything else is your decision."
"Heard her," Anevia says. "Don't get distracted by anythin' sensible."
{n}Anevia glances at you, then lowers her voice.{/n}
"She's been lookin' at it since we arrived. I believe you've been entrusted with a very serious matter."''', c('[Include the pie in the order.]', "supper", flags=("three_outing.chosen_for_beth",))),
    n("supper", "Narrator", '''{n}The meal arrives without incident, which Irabeth seems to consider an achievement. The pie is still warm. Anevia cuts a small piece from her own portion and sets it on her wife's plate.{/n}
{n}"You were lookin' at mine."{/n}
{n}"I was looking at you."{/n}
{n}Anevia's hand stops over the plates. Then she pushes the piece a little closer to Irabeth and looks down to hide her smile.{/n}
{n}Under the table, Irabeth's knee touches yours. She does not move it away when you look at her. Anevia notices the look that passes between you and smiles more openly.{/n}''',
      c('[Let the meal take as long as it takes.]', "walk")),
    n("walk", "Narrator", '''{n}Outside, the air is cool enough to make the three of you draw closer. Anevia begins along the familiar route, then pauses at a turning.{/n}
{n}"Long way?"{/n}
{n}Irabeth looks at you. For once she does not check the position of the moon before answering.{/n}
{n}"I have time."{/n}''',
      c('"The long way. We kept this evening for ourselves."', "long", flags=("three_outing.long_walk",)),
      c('"Home. I would like another hour with you both indoors."', "home", flags=("three_outing.home",))),
    n("long", "Irabeth", '''{n}Irabeth offers you her arm. Anevia takes her other hand, and for a while the three of you have to negotiate the uneven paving together.{/n}
"This is not a practical formation," Irabeth observes.
"Good thing we're not marchin'."
{n}Anevia squeezes her hand. You choose the next turning, where the lane is wide enough that no one has to let go.{/n}''', c('[Take the longer walk together.]', flags=("three_outing.kept",))),
    n("home", "Anevia", '''"Now that's a plan I can support."
{n}At the door, Irabeth waits while you find the latch. Anevia kisses her wife's cheek, then turns toward you with a question in her expression.{/n}''',
      c('[Kiss her, and go inside together.]', "inside", flags=("three_outing.kissed",)),
      c('[Take her hand and go inside together.]', "inside")),
    n("inside", "Irabeth", '''{n}Irabeth closes the door behind you. Anevia is already looking for somewhere to put the things she has carried home in her pockets.{/n}
"Leave them," Irabeth says. "They will still be there in the morning."
{n}Anevia turns back. Irabeth holds out a hand to each of you, and waits for you both to come closer.{/n}''', c('[Stay with them.]', flags=("three_outing.kept",))),
], requires=("three_locks.planned",),
    forbids=("closed", "loss", "inhuman", "irabeth_away", "anevia_away", "last_watch"), delay=48, optional=True,
    ForbidOverrides={"last_watch": "three_progression.catchup_requested"},
    Relationship="tirabade", Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[3, 5]))
