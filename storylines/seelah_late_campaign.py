"""Unexported Chapter 5 Seelah continuation; guest incidents are authored additions.

No native quest, friendship, inventory, resurrection or exclusivity state changes.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, entry, nodes, requires=(), delay=24):
    for node in nodes:
        node["Portrait"] = "Seelah"
    SCENES.append(scene(
        "seelah." + id, title, "Seelah", 5, entry, nodes,
        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
        Areas=[DREZEN], Chapters=[5], requires=("seelah.courting", "seelah.aftermath_ready", *requires),
        forbids=("inhuman", "seelah.farewell", "seelah_dead", "seelah_gone"),
        ForbidOverrides={"seelah.farewell": "seelah.catchup_requested"},
        optional=True, delay=delay))


s("late_course", "The turn she means to take", '"You have chalk on your sleeve. What are you planning?"', [
    n("start", "Seelah", '''{n}Seelah looks at her sleeve, then at the chalk in her hand, as if considering an accusation she cannot quite refute.{/n}
"A race. Which I'm going to win. Come and see."
{n}She leads you to a narrow yard behind a cooper's shed. Empty barrels mark a crooked course. Two women are arguing over a length of cord: a lean woman with a gray braid and another, younger woman with thick calves and an ink stain on her cheek.{/n}
"Tavia used to carry messages for a living," {n}Seelah says.{/n} "Dena still does. They claim that running in a straight line has made soldiers lazy. I felt I ought to defend us."
{n}"She asked to enter before I mentioned soldiers," Tavia says.{/n}
"Some people cannot be trusted with a perfectly good explanation."''',
      c('[Ask them to show you the course.]', "course"),
      c('"Show me later. I have to go."', abort=True)),
    n("course", "Narrator", '''{n}Dena runs from the chalk line, rounds two barrels and ducks beneath a cord without touching it. At the far end she picks a wooden hoop off a peg, carries it back around a third barrel and drops it over the starting post. She finishes with a little flourish toward Seelah.{/n}
{n}"Pairs," Tavia explains. "First runner brings the hoop back. Second takes it out and puts it where it began. No armor, spells or hired substitutes. The shed owner has given us the yard for an afternoon, provided we move everything back."{/n}
"She thinks I will go straight through the barrel."
{n}"I think you might try to apologize to it afterward."{/n}
{n}Seelah laughs, studies the turn, then walks it slowly. On her second attempt she plants her foot closer to the barrel and reaches the peg without breaking stride. Dena stops smiling quite so broadly.{/n}''',
      c('"I will run with you."', "runner", flags=("seelah.late_running",)),
      c('"I will watch. Do you need a judge at the finish?"', "watcher", flags=("seelah.late_watching",))),
    n("runner", "Seelah", '''"Good. I hoped you would say that."
{n}She hands you the hoop and points out the place where the loose gravel gives way to packed earth.{/n}
"We should try the exchange before we become impressive in public. I give it to you here, not wherever I happen to be when my lungs start complaining."
{n}The first exchange is awkward. She holds on a fraction too long, and the hoop turns between your hands. On the second she opens her fingers as yours close. It passes cleanly.{/n}
"There. We have mastered handing somebody an object. At this rate they'll have to invent a harder contest."
{n}Dena beckons a broad woman out of the shed doorway. "Breva, Tavia needs a partner." Breva sets down her mug, looks at the course and asks which of you she will have to beat.{/n}
{n}Dena asks for a trial. Seelah raises one finger.{/n}
"Not yet. I want to surprise you. It will be much more annoying that way."''', c('[Walk the turns together before leaving the yard.]', "invitation")),
    n("watcher", "Seelah", '''"Yes. Someone has to stop Tavia deciding that every close finish belongs to her."
{n}"Someone with working eyes," Tavia says. "I don't mind whose."{/n}
{n}Dena offers to run with Seelah. Tavia promptly recruits another courier from the shed doorway, a broad woman named Breva who has watched the preparations with a mug in her hands.{/n}
{n}"Now I have to put this down," Breva says. "I hope you appreciate the sacrifice."{/n}
{n}Seelah shows Dena where she wants the exchange. They disagree over which side of the post is faster, try both and settle on Dena's suggestion.{/n}
"Watch that," {n}Seelah says to you.{/n} "I expect to look splendid. If I don't, try to remember how splendidly I intended to look."
{n}She grins at you over Dena's shoulder, then bends to check the cord.{/n}''', c('[Ask when they intend to hold the race.]', "invitation")),
    n("invitation", "Seelah", '''"Once we've had a little practice. There's room for an audience by the shed. Nothing grand. Somebody suggested a prize, but then we'd spend the afternoon arguing about who could afford to lose it."
{n}Tavia proposes that the winners choose a song everyone else has to sing. Seelah approves this immediately and begins considering songs with entirely too many verses.{/n}
{n}On your way back she takes the chalk from her pocket and turns it between her fingers.{/n}
"There's another thing. I offered to show a few women how to use a shield when they have to get somebody out of trouble. Istra asked me. She used to fight. Her hand doesn't close properly now, and she wants to teach with me."
{n}She looks back toward the yard.{/n}
"I want to do that. I also want to practice until I can beat a woman who apparently remembers every alley she ever ran through."''',
      c('"Set an hour for the lesson. Run before or after."', "fixed", flags=("seelah.late_fixed_lessons",)),
      c('"Split the teaching with Istra. She can carry on when you are away."', "shared", flags=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"One lesson, same hour. Otherwise I'll be hauling shields around Drezen every time somebody shouts my name."
{n}She counts off the days on her chalk-stained fingers.{/n}
"I'll ask Istra when the women can come, and give her the days I'm here. Fewer runs before the race. Still a few.
Of course I'll grumble! I want to teach them and beat Tavia. Iomedae gave me two legs, and somehow that still isn't enough."
{n}She rubs a streak of chalk off her thumb.{/n}
"Early, if they can come then. Get the lesson done before I start craning over the shields to see what Tavia's up to."
{n}She points the chalk at you.{/n}
"You may come and watch. You are not permitted to call me naturally wonderful where Istra can hear."''', c('"I will come and see you both teach."', "end")),
    n("shared", "Seelah", '''"More practice for me. And Istra will do half of it her own way."
{n}She opens her mouth, shuts it, and laughs.{/n}
"Which she should! It's her hand. She's the one who knows how to fight with it."
{n}Seelah turns the chalk lengthwise and breaks it in two. She keeps both pieces.{/n}
"I'll ask which parts she wants. I'll show the work that takes two strong hands. She can show them how to do it without growing another Seelah.
If we disagree, we'll try it without hitting anybody first. I'm prepared to make that concession."
{n}She glances back toward the yard.{/n}
"And then I am coming straight back here. Before somebody moves the barrels and I have to learn it all again."''', c('"Send for me when you teach. I want to watch."', "end")),
    n("end", "Seelah", '''{n}At the next corner she stops and catches your hand.{/n}
"Glad you came. Halfway across Drezen, and I hadn't even told you what for!"
{n}Her palm is dusted with chalk. She notices the mark it leaves on your fingers and grins.{/n}
"There. Now you look involved."
{n}She leaves you with a time to meet Istra, a description of the yard and an increasingly elaborate proposal for the losing song. The proposal follows you several paces after you part.{/n}
"Actually, I know a worse one!"
{n}You look back. She is already laughing too hard to sing it.{/n}''', c('[Keep the invitation.]', flags=("seelah.late_course_planned",))),
])


s("late_lesson", "A shield held low", '"You invited me to Istra\'s lesson."', [
    n("start", "Narrator", '''{n}Istra has laid three battered practice shields against the yard wall. Her left hand holds a piece of bread; her right rests in the crook of her belt, the last two fingers curled inward. She is an older woman with a close crop of iron-gray hair and a voice that carries without growing loud.{/n}
{n}"You can move that barrel," she tells Seelah. "If I leave it there, they'll all steer around it. I want them to notice where they're stepping."{/n}
{n}Seelah moves it. Four women arrive, all grown, all with work to return to afterward. One carries folded laundry; another keeps checking a small sandglass. Istra asks each how much time she has, then changes where she has put the shields.{/n}
"We aren't making soldiers this afternoon," {n}Seelah tells you.{/n} "We're practicing getting somebody past a narrow place without leaving our own faces uncovered."''',
      c('[Stay for the lesson.]', "arrangement"),
      c('"I cannot stay today. Begin without me."', abort=True)),
    n("arrangement", "Seelah", '''{n}Istra gives Seelah the largest shield. Seelah tests the strap, loosens it and turns toward the waiting women.{/n}''',
      c('[Watch her explain the regular lesson.]', "fixed", requires=("seelah.late_fixed_lessons",)),
      c('[Watch them divide the work.]', "shared", requires=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"When I'm in Drezen, we meet at this hour. If the crusade drags me off, I'll tell Istra. No standing about with a shield while I'm halfway to a demon's doorstep. Today we try this. If it works, we do it again."
{n}The woman with the sandglass asks if they can begin. Seelah answers by lifting the shield.{/n}
{n}She demonstrates a step sideways, keeping her weight beneath her. Istra watches twice before asking her to stop.{/n}
{n}"You can hold that there for a long time. Most of us can't. Show the part before the arm starts shaking."{/n}
{n}Seelah lowers the shield and starts again. This time she explains the short movement instead of the position she can maintain through it. Istra takes the smallest shield and braces its lower edge against her leg, showing how she supports it without relying on her injured hand. The women try both methods in pairs. Istra walks between them, tapping the ground with her toe where a foot needs to move.{/n}''', c('[Help hold a shield while Istra adjusts its strap.]', "pressure")),
    n("shared", "Narrator", '''{n}Istra takes the smallest shield and demonstrates how to brace its lower edge against her leg. Seelah stands beside her, empty-handed, so that everyone can see the difference in their balance.{/n}
{n}"She can keep moving with hers high," Istra says. "I can't. If you need my way, learn my way. There isn't a prize for copying the strongest woman in the yard."{/n}
{n}Seelah demonstrates the same short turn with a larger shield. When one of the women tries to imitate her reach, she stops and points to Istra instead.{/n}
"Watch her feet. Mine are showing off."
{n}The joke gets the woman to look down. She moves her foot, and the shield stops pulling her sideways.{/n}
{n}Istra directs the second exercise. Seelah raises a finger, but the pair is already turning. Once they finish, she steps forward. "I've got a trick for that." Istra waves her into position, then makes her repeat it more slowly.{/n}''', c('[Help hold a shield while Istra adjusts its strap.]', "pressure")),
    n("pressure", "Narrator", '''{n}The next exercise puts you behind a shield while Seelah presses against its front. The wooden edge is worn smooth. Even without striking it she can drive it toward you, making the space between you and the barrel feel abruptly small.{/n}
"Say when."
{n}You do. She eases off immediately, and Istra has the women look at where your feet ended up.{/n}
{n}"If there isn't room, don't keep shoving. Find the gap. Call for help before you've used up your breath."{/n}
{n}Seelah tries a shorter approach. It works better, though the shield still catches the barrel. She moves the barrel back only after Istra has shown everyone why it caught.{/n}
{n}When the sand runs out, the woman carrying it sets down her shield. Seelah has just begun explaining another variation.{/n}''',
      c('"Show her the one movement to practice before she goes."', "one", flags=("seelah.late_one_movement",)),
      c('"Her sand has run out. Ask what she learned, then send her off."', "answer", flags=("seelah.late_asked_use",))),
    n("one", "Seelah", '''"This one. Slowly. You can do it without a shield."
{n}She shows the step again, then has the woman take it while turning toward the exit. The woman laughs when she realizes Seelah has brought her to the gate.{/n}
{n}"That I can remember. I nearly put my foot across my own other foot twice."{/n}
"Then stay off the stairs! I don't want my first lesson ending with somebody fetching a healer."
{n}After she leaves, Seelah looks at the three women remaining.{/n}
"Time for one more? Same step, then we're done. Before I cram six more into your heads and knock the first one out."
{n}Istra brings the smallest shield back to the wall. She leaves space beside it for the others.{/n}''', c('[Help gather the shields.]', "after")),
    n("answer", "Narrator", '''{n}"The way she braced it," the woman says, pointing to Istra. "I thought I'd have to get stronger before there was any use trying."{/n}
{n}Seelah glances at the shield she has been holding, then sets it down.{/n}
"Good. Start with that next time, slowly. Forget my other three speeches. I nearly have."
{n}The woman leaves. Istra asks the others the same question and discovers that one has misunderstood which shoulder to keep behind the shield. They correct it before collecting the equipment.{/n}
{n}"Save the next trick for next time," Istra tells Seelah. "Send her out with the wrong shoulder forward, and somebody will knock her teeth out."{/n}
{n}Seelah nods. When she helps carry the shields, she takes only two. Istra carries the smallest herself.{/n}''', c('[Walk out with Seelah.]', "after")),
    n("after", "Seelah", '''"I enjoyed showing off. Istra caught me halfway through my finest demonstration."
{n}She rolls her shoulder, working out the stiffness left by the demonstration.{/n}
"Should've seen that coming. I couldn't even put a barrel down to her satisfaction."
{n}She looks toward the chalk course still waiting at the other end of the yard.{/n}
"Come on. I have been looking at that third turn all afternoon."
{n}She takes a few quick steps and turns back toward you.{/n}
"One practice before we go? Or would you rather sit and watch me invent excuses for the turns?"''',
      c('[Stay for her practice.]', "practice"),
      c('"I have to go. Save your best excuse for tomorrow."', "part")),
    n("practice", "Narrator", '''{n}Seelah runs the course twice. On the first pass she takes the third barrel too wide; on the second she corrects it and catches the low cord with her hair. She stops, laughing, and ties it back more firmly.{/n}
"Defeated by my own hair. Don't tell the demons."
{n}She walks back beside you, flushed and panting, then glances at the cord and tightens her hair tie another notch.{/n}
{n}Before leaving she puts the cord back where it belongs. The yard is still a working yard, and neither Tavia nor the cooper has offered to clear up after a victorious paladin.{/n}''', c('[Leave with her when the yard is clear.]', flags=("seelah.late_lesson_kept",))),
    n("part", "Seelah", '''"The barrel moved. That's my best one so far. I intend to develop it."
{n}She catches your hand briefly, smiling, then lets you go.{/n}
"Glad you saw the lesson. 'Busy with shields' doesn't tell you much, does it? Especially when I spend half of it being told off."
{n}As you leave, she returns to the starting line. She tests the ground with one foot, squints at the first barrel, and takes a step back for her run.{/n}''', c('[Leave her to the practice she wanted.]', flags=("seelah.late_lesson_kept",))),
], requires=("seelah.late_course_planned",))


s("late_page", "A page she keeps", '"You said you had something to show me."', [
    n("start", "Seelah", '''{n}Seelah has bought a small stitched booklet. Most of its pages are empty. On the first she has written a heading, crossed it out and begun again beneath it.{/n}
"I bought this to write down things I want to do. First thing I put was 'help people.' Very noble. Try making an afternoon out of it. I nearly threw it in a bucket."
{n}She puts it between you on the bench.{/n}
"Somebody asks for a hand, and there goes the afternoon. Then I wonder why I never did the thing I bought the booklet for. Might as well write 'be Seelah' and save the ink."
{n}Under the crossed-out heading she has written, very plainly, 'Run again. Teach with Istra. Go somewhere I haven't been ordered to go.'{/n}''',
      c('"Running, teaching, and a road of your own. A better list."', "outcome"),
      c('"Keep it for later. I cannot stay to hear it now."', abort=True)),
    n("outcome", "Seelah", '''"Yes. Now this page has been giving me trouble."
{n}She turns a blank leaf, holding it down against the breeze.{/n}''',
      c('[Ask what she will do now that the souls are back.]', "grief", requires=("seelah.souls_returned", "seelah.ending_bad")),
      c('[Ask where she will go looking for answers.]', "questions", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
      c('[Ask about her plans for seeing her friends.]', "hope", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate")),
      c('[Ask what she will do while the rescue is unfinished.]', "unfinished", forbids=("seelah.souls_returned",))),
    n("grief", "Seelah", '''"I'm still angry. The next poor fool who bumps into me hasn't earned a tongue-lashing for it. I can remember that for an afternoon. Years? Ask me after supper."
{n}She smooths the corner of the page.{/n}
"We got the souls back. That was worth doing. Some mornings I wake up and all I can count is what we didn't fix. When the fighting lets me, I'll take a road on my own for a while. See what I do without somebody looking to me for the answer.
I'll write. Even if all I've found is rain. Three pages of it, perhaps. Curse me for wasting paper, then turn the page. There'll be more."
{n}She writes 'Letters, even in the rain' and leaves the next line empty.{/n}''', c('[Look at the blank line beneath her plans.]', "elan_gate")),
    n("questions", "Seelah", '''"I'll find people who've wrestled with the same questions. Hear what they did. If I only seek out people who'll clap me on the back and say I was right, I might as well stay here and talk to my boots."
{n}She taps the line about going somewhere.{/n}
"I may take that road without you. I'd miss you. But put you beside me, and I'll be pointing out the way before I've worked out where I'm going.
Somebody asks, and out comes my answer. Even when I haven't got one! I ought to shut up long enough to hear theirs."
{n}She writes a short sentence, then shows it to you: 'Ask before explaining.'{/n}
"Starting here. I can't blame my boots for everything."
{n}She leaves a space beneath it for an address she does not yet have.{/n}''', c('[Keep her company while she turns the page.]', "elan_gate")),
    n("hope", "Seelah", '''"I keep wanting to get them all in one room. Food, drink, a good evening. This time it'll go right! Then I remember I haven't asked whether any of them want to come."
{n}She draws a little square, considers it, then crosses out one wall.{/n}
"There. They can escape."
{n}She smiles, but keeps her pen poised beside the gap.{/n}
"Supper, if they want supper. No speeches about how everything's put right. And a journey with you. We pick the road, nobody sends us down it. Yes, there's a war to finish. I still want that journey when it's done."
{n}She writes 'Ask where they want to go' beneath the drawing, then underlines 'ask' once.{/n}''', c('[Wait while she writes down the question.]', "elan_gate")),
    n("unfinished", "Seelah", '''"I can't write 'all's well.' It isn't. But if we sit here staring at empty paper, we'll wear a hole in this bench before anything changes."
{n}She rests the pen across the booklet.{/n}
"The rescue isn't finished. I'm not forgetting that because I had a good afternoon. I'm also not going to beat myself with it every time I laugh. That won't bring anyone back.
I'll put down the next thing I can try. The rescue first. I won't forget it just because I've packed my boots."
{n}She writes 'Find another way,' then, on a separate line, 'Keep the lesson.'{/n}
"Both. Strange neighbors on a page. They'll have to get along."
{n}She runs the pen beneath both lines and turns the page.{/n}''', c('[Ask what she wants to put on the next page.]', "own")),
    n("elan_gate", "Narrator", '''{n}The next page has Elan's name at the top. Nothing follows it yet.{/n}''',
      c('[Wait while she decides what to write about him.]', "elan_dead", requires=("seelah.elan_dead",)),
      c('[Ask what she would want to tell him.]', "elan_letter", forbids=("seelah.elan_dead",))),
    n("elan_dead", "Seelah", '''"I said I wouldn't put words in his mouth now he can't argue back. Look at all that paper. Turns out I had quite a speech ready for him."
{n}She looks toward the far end of the bench. Then she takes up the pen.{/n}
"He always sounded so sure. Sometimes I wished I could do that. Sometimes I wanted to shake him. I'm not going to pretend we never argued just because I miss him."
{n}She writes slowly, shielding the page with her hand until she is finished. When she shows it to you, there is only one sentence beneath his name: 'I miss being able to disagree with you.'{/n}
"Yes. That's what I miss. I'll keep that."
{n}She presses the crease flat with her thumb and tucks the page beneath the next leaf, beside her untidy plans.{/n}''', c('[Sit with her until she is ready to turn the page.]', "own", flags=("seelah.late_elan_memory",))),
    n("elan_letter", "Seelah", '''"I'll tell him about Istra. Ask how he's doing. Then stop before I've answered for him."
{n}She starts a sentence, frowns and draws a line through it.{/n}
"Listen to that. 'Dear Elan, haven't I done splendidly?' I wanted to write a letter, not beg him to pin a medal on me."
{n}She begins again with a short description of the yard and the shields. This time she laughs at what she has written.{/n}
"I put in the barrel. Both times I had to move it. He'll get a laugh out of that, I hope."
{n}She folds a loose sheet into the booklet.{/n}
"I'll decide how to send it when I know where it can reach him. Writing his name doesn't put him in the next street."
{n}She tucks the folded draft under the cover and rests her hand on it.{/n}''', c('[Wait while she puts the letter away.]', "own", flags=("seelah.late_elan_draft",))),
    n("own", "Seelah", '''"Your turn. What do you want? And don't just pick something off my list."
{n}She shuts the booklet, lays the pen on top, and turns toward you on the bench.{/n}
"Something small will do. We haven't got all day. Supper's coming."
{n}When you hesitate, she smiles.{/n}
"Ha! You too. I wasted half a page before I could answer that."
{n}Her fingers rest beside yours on the bench, close without quite touching.{/n}''',
      c('"I want to take you to something I like. One hour with no errands."', "chosen", flags=("seelah.late_pc_delight",)),
      c('"I want a place where I can leave a few things and expect to find them when I return."', "place", flags=("seelah.late_pc_place",))),
    n("chosen", "Seelah", '''"Pick it, then. And if I start saying we could deliver something on the way, remind me I have two feet and can do that tomorrow."
{n}She gives you a sideways look.{/n}
"I'll ask questions. And if it's terrible music, I'll complain. Loudly. You've been warned."
{n}She pockets the booklet and leans her shoulder against yours before either of you rises.{/n}
"Good. Now I have to guess where you're taking me. Much better than guessing which chore you'll offer to do."''', c('[Arrange the afternoon of the race.]', flags=("seelah.late_page_kept",))),
    n("place", "Seelah", '''"A few things. Good thing you said that. I nearly offered a house, and then I'd have filled it with half the street."
{n}She laughs, then looks at you more seriously.{/n}
"Your things, where you put them. No finding your cup moved because somebody else wanted the shelf. Yes. I can find us that."
{n}She touches your fingers.{/n}
"We'll start smaller than a house. Yours beside mine, under a key we keep. See if we can manage a shelf before we start choosing rooftiles."''', c('[Arrange the afternoon of the race.]', flags=("seelah.late_page_kept",))),
], requires=("seelah.late_lesson_kept",))


s("late_race", "A song worth losing", '"Is this the afternoon you become intolerable?"', [
    n("start", "Seelah", '''"I have been intolerable for years. Today I receive public recognition."
{n}Seelah has tied her hair firmly back and left her armor behind. The yard is swept. Tavia has checked the cord, Breva is shifting the last empty barrel into position, and Dena has drawn a fresh starting line. A handful of spectators stand by the shed with their work baskets at their feet.{/n}
{n}Istra arrives carrying a stool. She plants it where she can see the exchange and tells Seelah that looking at the finish before making the last turn is an excellent way to kiss a barrel.{/n}
"I have other plans for my mouth," {n}Seelah says, glancing at you.{/n}
{n}The glance lasts just long enough to be deliberate.{/n}''',
      c('[Take your place for the race.]', "preparation"),
      c('"I have to leave. Save my place for another day."', abort=True)),
    n("preparation", "Narrator", '''{n}Before anyone runs, Seelah takes one turn around the course at a walk. She checks the gravel, ducks beneath the cord and brushes her fingertips over the peg. When she comes back, the amusement on her face has sharpened into concentration.{/n}''',
      c('[Ask about the practice she fitted around the regular lesson.]', "fixed", requires=("seelah.late_fixed_lessons",)),
      c('[Ask what the extra practice changed.]', "shared", requires=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"I know what I do wrong. That is an achievement. Doing it right takes a little longer."
{n}She shows you the turn where she still loses speed.{/n}
"Kept Istra's hour. Fewer runs than I wanted. I grumbled about it, too. Didn't burst into flame. A promising discovery."
{n}She watches Tavia test the same turn without quite touching the barrel.{/n}
"I'd give Istra the same hour again. Ask me after Tavia beats me, though. You'll get the answer with more swearing."
{n}Istra calls that she can hear them perfectly well. Seelah waves back, unapologetic.{/n}
"She knows. I told her I wanted to win before we picked the hour. Istra's seen me eyeing those barrels. No danger of her mistaking me for a saint."''', c('[Join the others at the line.]', "role")),
    n("shared", "Seelah", '''"That turn. And that one. Istra took the second half of the last practice lesson while I came here."
{n}She points to a scuff beside the third barrel.{/n}
"Nearly went back to check on her. As if she couldn't lift a shield without me hovering! Stayed here instead, and ran until I stopped kicking that stone."
{n}Istra catches her pointing and raises an eyebrow.{/n}
"I was saying you are very difficult to supervise," {n}Seelah calls.{/n}
{n}"A condition I intend to maintain."{/n}
{n}Seelah smiles, then looks down the course again.{/n}
"Now I can't blame lack of practice. I shall need a more inventive explanation if I lose. We have ruled out the barrel moving. Apparently someone marked where it was."''', c('[Join the others at the line.]', "role")),
    n("role", "Narrator", '''{n}Tavia repeats the rules for the spectators, who immediately discover several opinions nobody asked for. Istra insists on one false start being forgiven, then tells everyone the second will not be.{/n}''',
      c('[Take the second-runner position beside Seelah.]', "running", requires=("seelah.late_running",)),
      c('[Take the finishing post while Dena joins Seelah.]', "watching", requires=("seelah.late_watching",))),
    n("running", "Narrator", '''{n}Seelah runs first against Tavia. Tavia gains half a pace at the cord; Seelah takes it back at the far peg. When she comes toward you, she holds the hoop low, exactly where you practiced. You take it without a stumble.{/n}
{n}Breva starts almost level with you. The first barrel passes, then the second. You duck beneath the cord and hear the spectators calling from somewhere behind you. At the third barrel there is room for a close turn, though it would force you to change your stride. The wider line is clear.{/n}
{n}Seelah shouts your name from behind the starting line.{/n}''',
      c('[Take the close turn and reach for the peg.]', flags=("seelah.late_close_turn",), check=dict(Skill="SkillMobility", DC=26, Success="narrow", Failure="stumble", CommanderOnly=True)),
      c('[Keep your stride on the wider line and finish cleanly.]', "wide", flags=("seelah.late_wide_turn", "seelah.late_race_lost"))),
    n("narrow", "Narrator", '''{n}You plant your foot close to the barrel, turn and stretch the hoop toward its peg. It catches, swings once and settles. Breva's hoop lands a moment later.{/n}
{n}Seelah throws both arms up. Then she remembers she has to move out of the lane and does so just before Breva arrives with a breathless complaint about the width of the universe.{/n}
"I knew you could do it," {n}Seelah says, taking your hands.{/n}
{n}"She was making the face of a woman who knew nothing of the sort," Istra observes.{/n}
"I was saving the cheering until we won!"
{n}Seelah is flushed and grinning. She squeezes your hands once more before letting you catch your breath. Tavia comes to inspect the pegs, finds nothing to dispute and asks how many verses they have condemned themselves to sing.{/n}''', c('[Let Seelah choose the song.]', "won", flags=("seelah.late_race_won",))),
    n("stumble", "Narrator", '''{n}Your planted foot slides over loose grit. You catch yourself against the barrel, keep the hoop in your hand and reach the peg after Breva. By the time yours settles, she is walking back toward Tavia with both hands raised.{/n}
{n}Seelah meets you beyond the course, looking first at your footing and then at your face.{/n}
"Still in one piece? Good. Now I can curse about losing."
{n}She waits while you test your balance. There is a scuff on your sleeve where you caught the barrel, but nothing that stops you walking beside her.{/n}
"I was about to complain that they put the gravel in our way. Then I remembered showing you where it was. That would have spoiled the argument."
{n}She takes your hand and bows toward the spectators with exaggerated dignity. Tavia begins considering songs.{/n}''', c('[Face the losing song together.]', "lost", flags=("seelah.late_race_lost", "seelah.late_race_stumbled"))),
    n("wide", "Narrator", '''{n}You take the wider line without losing your footing. Breva makes the shorter turn and reaches the peg first. Your hoop lands after hers, upright and entirely too late.{/n}
{n}Seelah meets you beyond the course. She looks at the two hoops, then back at you.{/n}
"I had a whole speech ready. It was going to be unbearable.
I'd give it anyway, but Tavia would enjoy stopping me too much."
{n}She takes your hand and raises it briefly toward the spectators before bowing with exaggerated dignity. The applause makes her laugh.{/n}
{n}"Finishing without breaking my barrels counts for something," the cooper calls from the shed.{/n}
"There. We have won a very particular kind of admiration."
{n}She draws you out of the lane while Tavia confers with Breva about the song.{/n}''', c('[Face the losing song together.]', "lost")),
    n("watching", "Narrator", '''{n}Seelah runs first against Tavia, loses a little ground beneath the cord and gains it at the peg. She returns with the hoop low. Dena takes it cleanly, and Breva launches herself after her.{/n}
{n}From the post you can see the difference at the last turn. Dena takes it tightly enough to slow; Breva goes wider without breaking stride. Dena reaches her peg first, but the hoop strikes the end and falls. Breva's hoop settles a heartbeat later.{/n}
{n}Dena looks back at you. Tavia has begun celebrating. Seelah saw the fallen hoop too.{/n}
"The hoop has to stay," {n}she says before anyone asks.{/n} "That was the rule."
{n}Dena groans, picks it up and replaces it with immense care. Seelah goes to meet her, clapping her on the shoulder.{/n}
"You were fast enough. Next time we negotiate with the peg beforehand."
{n}She comes to stand beside you, still breathing hard.{/n}
"Did I at least look as though I intended to win?"''',
      c('"Very convincingly. I particularly admired your expression at the peg."', "lost", flags=("seelah.late_race_lost",)),
      c('"I liked seeing you tear down that course. You were hungry for that win."', "lost", flags=("seelah.late_race_lost",))),
    n("won", "Seelah", '''"The shortest song I know."
{n}Tavia looks suspicious. Seelah sings the first line, and the entire audience discovers why: it is a washing song whose last word becomes the first word of the next verse. Nobody can agree on when it ends.{/n}
{n}Breva makes it through three verses before pointing out that victory has made Seelah cruel. Seelah accepts surrender and joins the fourth verse herself, badly enough that Istra threatens to teach her breathing as well as footwork.{/n}
{n}When the laughter quiets, Seelah leans close to you.{/n}
"I am going to remember that turn for a very long time. You should prepare to hear about it when I am old and impossible."
{n}The cooper calls for his yard back. Seelah bends to lift the starting post, still humming the fourth verse.{/n}''', c('[Help clear the course.]', "clear")),
    n("lost", "Seelah", '''{n}Tavia chooses a song about a woman who keeps returning to a house because she has forgotten something, until everybody but the woman knows why she goes there. Seelah learns the first verse, invents the words of the second and becomes unexpectedly convincing by the third.{/n}
{n}At the line about forgetting her own good sense, she looks straight at you. Dena notices and sings louder to cover her laugh.{/n}
"I have lost with grace," {n}Seelah announces afterward.{/n} "Anybody saying otherwise will have to sing it again."
{n}She leans close enough that the next words are yours alone.{/n}
"I would still prefer to have won. I had a much worse song ready."
{n}She helps Tavia wind up the cord, mumbling the verse she got wrong. Tavia corrects her. "I liked mine better," Seelah says.{/n}''', c('[Help clear the course.]', "clear")),
    n("clear", "Narrator", '''{n}The barrels go back against the shed. Istra carries her stool away after making Seelah promise only to tell her when another race is planned, not to organize one before anyone has recovered from this one.{/n}
{n}When the yard is empty, Seelah finds a scrap of cord still caught around the post. She unwinds it, puts it with the rest and turns to you.{/n}
"There. Now, can I ask you for another evening after you heard me sing?"
{n}She hooks a thumb into her belt and gives you a hopeful grin.{/n}''', c('"Ask me."', flags=("seelah.late_race_kept",))),
], requires=("seelah.late_lesson_kept", "seelah.late_page_kept"), delay=48)


s("late_afterglow", "The verse she remembers", '"You were going to ask me for an evening."', [
    n("start", "Seelah", '''"I was. Somewhere with a door, and no audience to correct the words. I've had that blasted tune in my head ever since the race."
{n}She has hired the little room above the cooper's shed until morning. The cooper took her coin and made one condition: no practising turns on his floorboards. There is a bed built for one and a half, a basin, and a chair whose missing rung has been replaced with a darker piece of wood.{/n}
{n}Seelah puts a jug of water on the table. The shirt she wore at the race hangs over the chair, a loose thread trailing from the sleeve. She brought it to mend, she says, and has not the slightest intention of mending it tonight.{/n}
"I'm going to kiss you. Been thinking about it all the way up the stairs. Nearly missed a step."''',
      c('[Come in and close the door.]', "race"),
      c('"I cannot stay tonight. Ask me again."', abort=True)),
    n("race", "Seelah", '''{n}She pours the water, drinks half of hers in one go, and hands you the other cup. The room is so small that wherever you stand, you are standing next to her.{/n}''',
      c('"Have you stopped enjoying the victory?"', "victory", requires=("seelah.late_race_won",)),
      c('"Do you remember the song?"', "song", requires=("seelah.late_race_lost",))),
    n("victory", "Seelah", '''"No. I tried modesty on the stairs. It didn't suit me."
{n}She demonstrates the last turn with two fingers on the table, then catches herself smiling at the tiny performance.{/n}
"I keep remembering the hoop settling. The moment before it did, I was certain we had lost it. Then there it was."
{n}She puts down her cup and looks at you.{/n}
"Then you looked at me. I nearly forgot the hoop. Don't tell Tavia. I still want to boast about my magnificent victory."
{n}She touches the back of your hand, still smiling.{/n}
"Come here. I've had enough of admiring you from the far end of a yard."''', c('[Turn your hand beneath hers.]', "ask")),
    n("song", "Seelah", '''"Most of it. Unfortunately."
{n}She hums the tune, then tries the verse about the forgotten key. Halfway through she realizes she has combined it with the verse about the woman returning for her scarf.{/n}
"A well-prepared woman. She never runs out of reasons."
{n}She stops humming and looks at you over the rim of her cup.{/n}
"So much for sneaking a look at you. Dena caught me every time. Nearly swallowed the last verse trying not to laugh. I thought I'd die of shame. Still here!"
{n}She sets the cup aside.{/n}
"Worth it. Every time I looked, there you were. And now I'm trying to say how much I liked that without comparing you to a barrel. Blasted race. It's eaten all my best words."''', c('"You are doing rather well."', "ask")),
    n("ask", "Seelah", '''{n}She steps in. There is a smear of chalk she missed at the side of one finger, and she does not care about it now.{/n}
"Then let me finish before I improve it to death. I want you. I want to kiss you until I run out of clever things to say, and then I want to keep going."
{n}Her hand finds your waist and pulls, not gently, until your hips meet hers. Her breath has gone short. The swagger of the race is still in her, and something hungrier underneath it.{/n}
"Or we sit on that bed and laugh about the song all night, and I tell everyone that was the plan." {n}She grins up at you.{/n} "It wasn't the plan."''',
      c('[Kiss her and ask to stay the night.]', "night", flags=("seelah.late_night_chosen",)),
      c('[Kiss her. Spend the evening trading kisses.]', "kisses", flags=("seelah.late_kisses_chosen",)),
      c('"Sit with me. Tonight I want to talk and hold your hand."', "quiet", flags=("seelah.late_quiet_chosen",))),
    n("night", "Seelah", '''"Yes. Iomedae, yes."
{n}She kisses you before the word is quite out of her mouth, one hand at the back of your neck and the other hauling you in by the belt, and for a while neither of you has any use for speech.{/n}
{n}When she draws back she is breathless and laughing at herself.{/n}
"There. Every clever thing, gone."
{n}She strips the way a soldier does, fast and without ceremony: boots kicked under the chair, shirt over her head in one pull, and then a curse because she has got her elbow tangled in the sleeve. You free her. She does not let you do anything else for yourself. Your belt, your shirt, your boots: she takes them off you one by one like a thief turning out a mark's pockets, and drops each on the floor with a satisfied little "mine."{/n}
{n}Then she shoves you down onto the bed, swings a leg over your hips, freckled and bare and grinning, and pins your wrists to the pillow with both hands.{/n}
"Hold still," {n}she says against your mouth.{/n} "I've been waiting a whole race for this."
{n}In the morning she wakes before you. A hammer starts up below. She pulls you closer instead of rising, her thumb stroking your shoulder.{/n}
"Morning. Try getting me out of this bed. Go on. I dare you."''',
      c('"Begin with five more minutes."', "morning", flags=("seelah.late_night_kept", "seelah.kissed"))),
    n("morning", "Narrator", '''{n}Five minutes pass. Seelah buries her face against your neck and demands five more. By the time she sits up, the cooper is hammering hard enough to shake the basin.{/n}
{n}Seelah washes, finds her clothes and returns your things before collecting her own. At one point she drops a boot, winces at the noise and listens for a complaint from below.{/n}
"I promised not to practice turns. I said nothing about managing footwear with grace."
{n}At the door she kisses you again, slower than the hurried sounds from the yard would seem to allow.{/n}
"I want another morning like this one. Soon. Find us a night when nothing's on fire, Commander, or I'll pick one myself and you'll hear about it from the guard."''', c('[Leave the room together.]', "plans")),
    n("kisses", "Narrator", '''{n}She meets your kiss with a pleased sound and gives it back with interest. You draw apart, her fingers still tangled in your collar. She looks from your mouth to the bed and groans at the ceiling.{/n}
"Kisses, then. Lots of them. Come here."
{n}You sit together on the edge of the bed because the chair would never hold two. Seelah makes one attempt at humming the race's tune, gives it up when you touch her cheek, and kisses you again.{/n}
{n}The evening goes in drinks of water, half-remembered jokes and her fingers in your hair whenever she runs out of things to say, which happens more often than she would like you to notice.{/n}
{n}Before it is time to go she rests her forehead against yours.{/n}
"I'm asking you to stay next time. Already planning it. Paladin's word."''', c('[Hold her close before leaving.]', "plans", flags=("seelah.kissed",))),
    n("quiet", "Seelah", '''"All right. Come here."
{n}She sits on the bed and shoves a folded blanket out of the way. When you sit beside her she takes your hand, as though she had won it at cards, and keeps it.{/n}
"I won't sing unless asked. That is the most valuable thing I have offered anyone today."
{n}You talk about the race: Tavia repeating the rules over everyone's helpful objections, the cooper counting his barrels afterward, Istra's unconcealed delight whenever Seelah was contradicted. Seelah admits that she has already thought of a different way to take the third turn.{/n}
"You see what you have encouraged. There will be diagrams."
{n}She draws one on her palm with a fingertip, then discovers that the most important barrel has ended up on the side of her thumb. The explanation collapses into laughter.{/n}
{n}When you rise to leave, she holds your hand a moment longer before letting it go.{/n}
"Come again. I'd have kept you here till morning, you know. I'll try my luck again next time."''', c('[Arrange another time together.]', "plans")),
    n("plans", "Seelah", '''{n}Before you part, she brings out the little booklet. The page of plans is more crowded now, with a short description of the race wedged beneath the first line.{/n}
"Your wish. The thing you asked for in the middle of all my lists. Don't think I forgot it."
{n}She taps the page with a chalky finger.{/n}
"We start a piece of it here, this week, before the next lot of demons gets a vote. The big version can wait till I've worked out how to steal it for you."
{n}She puts the booklet away and holds out her hand for yours, as if the next meeting were already a thing she had in her pocket.{/n}''', c('[Make time for the next visit.]', flags=("seelah.late_evening_kept",))),
], requires=("seelah.late_race_kept",))


s("late_first_step", "Something left for next time", '"Let us try the thing we talked about."', [
    n("start", "Narrator", '''{n}Seelah meets you without armor, her little booklet tucked into her belt. She has left the afternoon clear long enough to begin without watching every movement of the sun.{/n}
"Ready? I was afraid I'd be late. Istra asked me a question at the gate, and I had to explain why I was answering while backing away."
{n}She waits while you finish what brought you to the meeting place. When you are ready, she offers you her arm.{/n}''',
      c('[Go with her.]', "wish"),
      c('"We will have to go another day."', abort=True)),
    n("wish", "Seelah", '''"Your idea today. I haven't forgotten. Lead on."''',
      c('[Take her to the music you chose.]', "music", requires=("seelah.late_pc_delight",)),
      c('[Ask to see the place she found for your things.]', "shelf", requires=("seelah.late_pc_place",))),
    n("music", "Narrator", '''{n}You have chosen a small gathering in a courtyard, where a woman with a reed pipe plays for whoever can spare the time to listen. Her hair is silver, her fingers quick, and she announces each tune by the person who taught it to her rather than the name anyone expects.{/n}
{n}Seelah settles beside you and listens. During the first tune she looks as though she wants to say something, then keeps it until the last note has faded.{/n}
"I thought it was going somewhere else. The part in the middle. I kept waiting for it to come back."
{n}The musician hears her and plays the passage again, more slowly. This time Seelah follows the turn of it, tapping one finger against her knee.{/n}
{n}When the musician begins the next tune, Seelah looks at you instead of the gathering.{/n}
"Which bit made you bring me here? Show me."''',
      c('[Point out the quiet phrase before the tune rises.]', "quiet_phrase", flags=("seelah.late_music_quiet",)),
      c('[Tap the quick rhythm that made you choose it.]', "quick_phrase", flags=("seelah.late_music_quick",))),
    n("quiet_phrase", "Seelah", '''{n}She waits for the phrase. When it comes, her tapping finger stills. She leans forward through the quiet that follows, listening for the next note.{/n}
"There. It leaves you expecting the next bit."
{n}She tries to hum it afterward and loses the last note. The musician supplies it without interrupting her packing, then asks if she wants to learn the whole tune.{/n}
"Not today," {n}Seelah says.{/n} "Play it for me once more. I'll spare you my singing."
{n}She finds your hand beneath the edge of the bench.{/n}
"I'd come back just for that bit. You chose well."''', c('[Stay until the musician finishes packing.]', "carry")),
    n("quick_phrase", "Seelah", '''{n}She catches the rhythm under your fingers and answers it on her knee. When the tune quickens she looks delighted, then loses the beat and laughs at herself.{/n}
"All right. That was an unreasonable number of notes."
{n}Afterward the musician shows her the beat again on the side of the pipe case. Seelah gets it on the second attempt and immediately tries to make you keep it while she adds the wrong accent.{/n}
"You chose the music. You knew what sort of company you were inviting."
{n}The musician lifts an eyebrow at the racket. Seelah grins, stops tapping, and curls her fingers around yours.{/n}
"Yes. I would like to come again. Next time I will have forgotten the difficult part and be very confident about it."''', c('[Stay until the musician finishes packing.]', "carry")),
    n("shelf", "Narrator", '''{n}The cooper has agreed to rent Seelah a small locking cupboard in the room above the shed. It is hardly bigger than a chest stood on end. The key turns stiffly, and the lower shelf has a dark mark where something once leaked.{/n}
"Look at our fine house," {n}Seelah says.{/n} "Mind your head. And your knees. All right, it's a cupboard. But I paid for it. Our things stay here even when we don't, and the cooper can keep his hands off the shelf."
{n}She has left a small parcel beside the cupboard. She unwraps it to reveal a plain cup and a strip of cloth, neatly folded. She puts them on the lower shelf, then moves them to one side to leave room.{/n}
"What are you putting here? Something you'll want when you come back. I've brought a cup, so don't go trying to outdo me with a trophy."''',
      c('[Choose an ordinary keepsake to leave beside her cup.]', "keepsake", flags=("seelah.late_shelf_keepsake",)),
      c('"Keep my part empty. I will bring something another day."', "space", flags=("seelah.late_shelf_space",))),
    n("keepsake", "Narrator", '''{n}You set a small personal keepsake beside the cup. Seelah shifts the cup a little farther back so that its handle will not catch when you reach for your things.{/n}
"That looks more like it."
{n}She closes the cupboard, turns the key and hands it to you. Then she holds up its mate.{/n}
"I asked for two. The cooper asked whether I meant to lose both. I said I would begin with one and judge my progress."
{n}She opens it again before you leave, simply to look. The keepsake and cup are exactly where you put them. She seems almost embarrassed by how much she enjoys that.{/n}''', c('[Close it together.]', "carry")),
    n("space", "Seelah", '''"Then it stays empty."
{n}She starts to move the cloth into the gap, catches herself and folds it beneath the cup instead.{/n}
"Ha! Nearly filled your half before you had the key."
{n}She shuts the cupboard and turns the key, then gives it to you. She has a second one for herself.{/n}
"There. If you find it stuffed with practice shields, drag me up here and make me carry them out."
{n}Before you leave, she opens the cupboard once more, rests her hand on the door, and looks at the gap beside her cup.{/n}
"Now I'm going to spend the week guessing what you'll bring. Come back before I settle on something ridiculous."''', c('[Close it together.]', "carry")),
    n("carry", "Seelah", '''{n}Outside, Seelah finds a quiet place to stand before the traffic of the street can carry you apart.{/n}
"Another afternoon. Soon. Let's pick it before I promise to haul barrels for somebody."
{n}She brings out the booklet, though she does not open it yet.{/n}
"I'm still thinking about that journey. I'll still have questions when I pack my boots. But now I can picture coming back and finding you here."
{n}She meets your eyes, the unopened booklet held against her belt.{/n}
"So. Are we talking about the promise we've made, or am I getting ahead of you? Better tell me before I fill this thing with plans."''',
      c('"I meant my promise. And I want more days like this with you."', "committed", requires=("seelah.committed",)),
      c('"Ask me for another afternoon. I am not ready to swear a vow."', "courting", forbids=("seelah.committed",))),
    n("committed", "Seelah", '''"Good. I meant mine, too. And I want you beside me on days when all we're fighting over is a song."
{n}She opens the booklet and adds a short line beneath the description of the race. She lets you read it before closing the cover.{/n}
"Still don't know where that road will take me. But when I come back, I'm dragging you out for another afternoon."
{n}She offers you her hand.{/n}
"And I would like another race, eventually. I think I have begun to understand the third turn. Please don't tell Tavia I said that. She'll arrange another barrel."
{n}She laughs, folds the booklet shut, and tucks it beside her belt buckle.{/n}''', c('[Keep her hand as you walk back.]', "end")),
    n("courting", "Seelah", '''"Another afternoon, then. I'm not going to hold up a cupboard key and claim you've sworn an oath on it."
{n}She smiles and taps the booklet against her palm.{/n}
"I will ask about that vow again. But first, pick an evening. One you can actually give me. Don't promise me a whole week and spend it chasing demons."
{n}She opens the booklet and adds a short line beneath the description of the race. Then she puts it away and offers you her hand.{/n}
"I've got plenty to keep me busy until then. Istra's next lesson. Another crack at those barrels. And you showing me something else you like. I've only heard one tune!"
{n}She waits for you before starting back toward the busier street.{/n}''', c('[Walk back with her.]', "end")),
    n("end", "Narrator", '''{n}At the corner, Seelah pauses to let a cart pass. There is somewhere she needs to be, and she tells you when she expects to be free again.{/n}
{n}She glances down the street toward the yard.{/n}
"Next time, we try the course the other way around. I want to see who complains first."
{n}She squeezes your hand before letting it go.{/n}
"Don't be late."''', c('[Keep the next visit in mind.]', flags=("seelah.late_campaign_kept",))),
], requires=("seelah.late_evening_kept",))
