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
"Something I would like to win. Come and see."
{n}She leads you to a narrow yard behind a cooper's shed. Empty barrels mark a crooked course. Two women are arguing over a length of cord: a lean woman with a gray braid and another, younger woman with thick calves and an ink stain on her cheek.{/n}
"Tavia used to carry messages for a living," Seelah says. "Dena still does. They claim that running in a straight line has made soldiers lazy. I felt I ought to defend us."
{n}"She asked to enter before I mentioned soldiers," Tavia says.{/n}
"Some people cannot be trusted with a perfectly good explanation."''',
      c('[Ask them to show you the course.]', "course"),
      c('"Show me when I can stay. I would like to give this my attention."', abort=True)),
    n("course", "Narrator", '''{n}Dena runs from the chalk line, rounds two barrels and ducks beneath a cord without touching it. At the far end she picks a wooden hoop off a peg, carries it back around a third barrel and drops it over the starting post. She finishes with a little flourish toward Seelah.{/n}
{n}"Pairs," Tavia explains. "First runner brings the hoop back. Second takes it out and puts it where it began. No armor, spells or hired substitutes. The shed owner has given us the yard for an afternoon, provided we move everything back."{/n}
"She thinks I will go straight through the barrel."
{n}"I think you might try to apologize to it afterward."{/n}
{n}Seelah laughs, studies the turn, then walks it slowly. On her second attempt she plants her foot closer to the barrel and reaches the peg without breaking stride. Dena stops smiling quite so broadly.{/n}''',
      c('"I would like to run with you."', "runner", flags=("seelah.late_running",)),
      c('"I would rather watch you compete. Could they use someone at the finish?"', "watcher", flags=("seelah.late_watching",))),
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
"Watch that," Seelah says to you. "I expect to look splendid. If I don't, try to remember how splendidly I intended to look."
{n}She seems pleased by the prospect of having you there, without trying to turn your answer into an agreement to run.{/n}''', c('[Ask when they intend to hold the race.]', "invitation")),
    n("invitation", "Seelah", '''"Once we've had a little practice. There's room for an audience by the shed. Nothing grand. Somebody suggested a prize, but then we'd spend the afternoon arguing about who could afford to lose it."
{n}Tavia proposes that the winners choose a song everyone else has to sing. Seelah approves this immediately and begins considering songs with entirely too many verses.{/n}
{n}On your way back she takes the chalk from her pocket and turns it between her fingers.{/n}
"There's another thing. I offered to show a few women how to use a shield when they have to get somebody out of trouble. Istra asked me. She used to fight. Her hand doesn't close properly now, and she wants to teach with me."
{n}She looks back toward the yard.{/n}
"I want to do that. I also want to practice until I can beat a woman who apparently remembers every alley she ever ran through."''',
      c('"Choose a regular lesson you can keep. Practice around it."', "fixed", flags=("seelah.late_fixed_lessons",)),
      c('"Build the lesson with Istra so she can lead it when you are away."', "shared", flags=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"One regular lesson. Not 'find me whenever something worries you.'"
{n}She says it again, more quietly, working out whether she means it.{/n}
"Istra can tell me what hour suits the women. I'll tell her which days I can actually offer. That leaves less room to practice, but it leaves some."
"Would you resent that?"
"Sometimes. I would like to be naturally wonderful at everything and never have to choose."
{n}She rubs a streak of chalk off her thumb.{/n}
"I'll take the early hour if the women can come then. If I leave practice until evening, I'll spend the whole lesson wondering whether Tavia has learned another trick."
{n}She points the chalk at you.{/n}
"You may come and watch. You are not permitted to call me naturally wonderful where Istra can hear."''', c('"I would like to see what the two of you make of it."', "end")),
    n("shared", "Seelah", '''"That would leave more practice. It would also mean letting Istra teach something differently from the way I would."
{n}She smiles at the objection before you have time to make it.{/n}
"I heard myself. Yes, I know. She has rather more experience of fighting with her hand than I do."
{n}Seelah turns the chalk lengthwise and breaks it in two. She keeps both pieces.{/n}
"I'll ask her what she wants to lead. I can demonstrate the parts that need two strong hands, and she can stop me teaching everybody to solve trouble by being built like me."
"And when you disagree?"
"We'll try it without hitting anybody first. I'm prepared to make that concession."
{n}She glances back toward the yard.{/n}
"And then I am coming straight back here. Before somebody moves the barrels and I have to learn it all again."''', c('"Then invite me to the lesson. I want to see you put it together."', "end")),
    n("end", "Seelah", '''{n}At the next corner she stops and catches your hand.{/n}
"I like that you came. I know I dragged you halfway across Drezen before explaining why."
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
"We aren't making soldiers this afternoon," Seelah tells you. "We're practicing getting somebody past a narrow place without leaving our own faces uncovered."''',
      c('[Stay for the lesson.]', "arrangement"),
      c('"I cannot stay today. Begin without me."', abort=True)),
    n("arrangement", "Seelah", '''{n}Istra gives Seelah the largest shield. Seelah tests the strap, loosens it and turns toward the waiting women.{/n}''',
      c('[Watch her explain the regular lesson.]', "fixed", requires=("seelah.late_fixed_lessons",)),
      c('[Watch them divide the work.]', "shared", requires=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"This is the hour I can offer when I'm in Drezen. If I'm called away, Istra will hear from me before you spend your afternoon waiting. We haven't promised the next lesson will be more than this one. First we find out whether this helps."
{n}The woman with the sandglass asks if they can begin. Seelah answers by lifting the shield.{/n}
{n}She demonstrates a step sideways, keeping her weight beneath her. Istra watches twice before asking her to stop.{/n}
{n}"You can hold that there for a long time. Most of us can't. Show the part before the arm starts shaking."{/n}
{n}Seelah lowers the shield and starts again. This time she explains the short movement instead of the position she can maintain through it. Istra takes the smallest shield and braces its lower edge against her leg, showing how she supports it without relying on her injured hand. The women try both methods in pairs. Istra walks between them, tapping the ground with her toe where a foot needs to move.{/n}''', c('[Help hold a shield while Istra adjusts its strap.]', "pressure")),
    n("shared", "Narrator", '''{n}Istra takes the smallest shield and demonstrates how to brace its lower edge against her leg. Seelah stands beside her, empty-handed, so that everyone can see the difference in their balance.{/n}
{n}"She can keep moving with hers high," Istra says. "I can't. If you need my way, learn my way. There isn't a prize for copying the strongest woman in the yard."{/n}
{n}Seelah demonstrates the same short turn with a larger shield. When one of the women tries to imitate her reach, she stops and points to Istra instead.{/n}
"Watch her feet. Mine are showing off."
{n}The joke gets the woman to look down. She moves her foot, and the shield stops pulling her sideways.{/n}
{n}Istra directs the second exercise herself. Seelah starts to add something, waits until the pair has finished and asks to demonstrate it. Istra agrees, then makes her repeat it more slowly.{/n}''', c('[Help hold a shield while Istra adjusts its strap.]', "pressure")),
    n("pressure", "Narrator", '''{n}The next exercise puts you behind a shield while Seelah presses against its front. The wooden edge is worn smooth. Even without striking it she can drive it toward you, making the space between you and the barrel feel abruptly small.{/n}
"Say when."
{n}You do. She eases off immediately, and Istra has the women look at where your feet ended up.{/n}
{n}"If there isn't room, don't keep shoving. Find the gap. Call for help before you've used up your breath."{/n}
{n}Seelah tries a shorter approach. It works better, though the shield still catches the barrel. She moves the barrel back only after Istra has shown everyone why it caught.{/n}
{n}When the sand runs out, the woman carrying it sets down her shield. Seelah has just begun explaining another variation.{/n}''',
      c('"Show her the one movement to practice before she goes."', "one", flags=("seelah.late_one_movement",)),
      c('"Let her go on time. Ask which part was useful."', "answer", flags=("seelah.late_asked_use",))),
    n("one", "Seelah", '''"This one. Slowly. You can do it without a shield."
{n}She shows the step again, then has the woman take it while turning toward the exit. The woman laughs when she realizes Seelah has brought her to the gate.{/n}
{n}"That I can remember. I nearly put my foot across my own other foot twice."{/n}
"Then don't practice it on stairs. I would like my first lesson to end without a report."
{n}After she leaves, Seelah looks at the three women remaining.{/n}
"Same step once more, if you have the time. Then we're done. I could keep adding things until nobody remembers any of them."
{n}Istra brings the smallest shield back to the wall. She leaves space beside it for the others.{/n}''', c('[Help gather the shields.]', "after")),
    n("answer", "Narrator", '''{n}"The way she braced it," the woman says, pointing to Istra. "I thought I'd have to get stronger before there was any use trying."{/n}
{n}Seelah glances at the shield she has been holding, then sets it down.{/n}
"Good. Try that slowly next time. You don't have to remember my other three explanations on the way back to work."
{n}The woman leaves. Istra asks the others the same question and discovers that one has misunderstood which shoulder to keep behind the shield. They correct it before collecting the equipment.{/n}
{n}"You can teach her something next time," Istra tells Seelah. "Today I needed to know she was leaving with that wrong."{/n}
{n}Seelah nods. When she helps carry the shields, she takes only two. Istra carries the smallest herself.{/n}''', c('[Walk out with Seelah.]', "after")),
    n("after", "Seelah", '''"I enjoyed showing off. Istra caught me halfway through my finest demonstration."
{n}She rolls her shoulder, working out the stiffness left by the demonstration.{/n}
"I should have expected the corrections. She had hardly let me put a barrel down without one."
{n}She looks toward the chalk course still waiting at the other end of the yard.{/n}
"Come on. I have been looking at that third turn all afternoon."
{n}She takes a few quick steps and turns back toward you.{/n}
"One practice before we go? Or would you rather sit and watch me invent excuses for the turns?"''',
      c('[Stay for her practice.]', "practice"),
      c('"I need to go. Tell me tomorrow which excuse was best."', "part")),
    n("practice", "Narrator", '''{n}Seelah runs the course twice. On the first pass she takes the third barrel too wide; on the second she corrects it and catches the low cord with her hair. She stops, laughing, and ties it back more firmly.{/n}
"There. The course has identified a weakness."
{n}She walks back beside you while her breathing settles. You can see the effort in her flushed face, and the pleasure she takes in measuring it against something that can be tried again.{/n}
{n}Before leaving she puts the cord back where it belongs. The yard is still a working yard, and neither Tavia nor the cooper has offered to clear up after a victorious paladin.{/n}''', c('[Leave with her when the yard is clear.]', flags=("seelah.late_lesson_kept",))),
    n("part", "Seelah", '''"The barrel moved. That's my best one so far. I intend to develop it."
{n}She catches your hand briefly, smiling, then lets you go.{/n}
"Thank you for coming to the lesson. I wanted you to see what I was choosing, not just hear that I had somewhere else to be."
{n}As you leave, she goes back to the starting line and tests the ground with one foot. She has already stopped performing for you. Her attention is on the first turn.{/n}''', c('[Leave her to the practice she wanted.]', flags=("seelah.late_lesson_kept",))),
], requires=("seelah.late_course_planned",))


s("late_page", "A page she keeps", '"You said you had something to show me."', [
    n("start", "Seelah", '''{n}Seelah has bought a small stitched booklet. Most of its pages are empty. On the first she has written a heading, crossed it out and begun again beneath it.{/n}
"I meant to make a list of what I want to do when there is time. Then I wrote 'help people' and stared at it until I wanted to throw the whole thing into a bucket."
{n}She puts it between you on the bench.{/n}
"That isn't a plan. It's what I say before deciding somebody else's plan must be more important than mine. I could have written 'be Seelah' and saved the ink."
{n}Under the crossed-out heading she has written, very plainly, 'Run again. Teach with Istra. Go somewhere I haven't been ordered to go.'{/n}''',
      c('"Those sound like things you actually want."', "outcome"),
      c('"Show me when you have time to talk properly."', abort=True)),
    n("outcome", "Seelah", '''"They are. There's another page I haven't known how to begin."
{n}She turns a blank leaf, holding it down against the breeze.{/n}''',
      c('[Hear what she wants to do with the grief that remains.]', "grief", requires=("seelah.souls_returned", "seelah.ending_bad")),
      c('[Hear where her unanswered questions are taking her.]', "questions", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
      c('[Ask how her friends enter the plans.]', "hope", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate")),
      c('[Ask what she can plan while the rescue remains unresolved.]', "unfinished", forbids=("seelah.souls_returned",))),
    n("grief", "Seelah", '''"I want to leave room for being angry without turning everyone I meet into somebody who has to answer for it. I can manage that for an afternoon. I don't know how to promise years of it."
{n}She smooths the corner of the page.{/n}
"The rescue mattered. I can say that and still wake up thinking about what it didn't change. When the fighting lets me, I want to travel alone for a while. I need to find out who I am when nobody is waiting for me to sound certain."
"Would you write?"
"Yes. Not only when I've found something encouraging. If I send you three pages about the rain, you may complain that I have wasted good paper. You mustn't decide it means I have nothing else to say."
{n}She writes 'Letters, even in the rain' and leaves the next line empty.{/n}''', c('[Let the unfinished line remain.]', "elan_gate")),
    n("questions", "Seelah", '''"I want to hear how other people have lived with questions they couldn't put down. I don't mean finding somebody who will prove I was right all along. I'd know I was cheating."
{n}She taps the line about going somewhere.{/n}
"I may need to go without you. Not because I have stopped wanting your company. Because if you're beside me, I can spend an entire journey being the person I think you need and never notice I've done it."
"You think I need certainty?"
"Sometimes I think everyone does. That's part of what I want to find out."
{n}She writes a short sentence, then shows it to you: 'Ask before explaining.'{/n}
"I can begin that here. I don't get to postpone every difficult thing until I've bought better boots."
{n}She leaves a space beneath it for an address she does not yet have.{/n}''', c('[Keep her company while she turns the page.]', "elan_gate")),
    n("hope", "Seelah", '''"I want to see what they choose when I stop trying to arrange the next happy occasion. I keep wanting to put everybody in the same room and have it go right this time."
{n}She draws a little square, considers it, then crosses out one wall.{/n}
"There. They can escape."
{n}The joke comes easily, but she keeps looking at the opening she has made.{/n}
"I would like some invitations with no hidden work in them. No ceremony somebody has to endure so that I can feel we are all better. And I want to take a journey with you because we both chose it. I haven't forgotten that there is still a war to finish. I would like the wanting to survive it."
{n}She writes 'Ask where they want to go' beneath the drawing, then underlines 'ask' once.{/n}''', c('[Leave room for their answers.]', "elan_gate")),
    n("unfinished", "Seelah", '''"I can't write as though everything has been put right. It hasn't. And I can't ask you to sit beside a blank page until I know whether it ever will be."
{n}She rests the pen across the booklet.{/n}
"I am still carrying the unfinished rescue. I won't turn a pleasant afternoon into proof that I've accepted how things are. I also don't want to make suffering the only way I know to show I care."
"What goes on the page?"
"What I can do next. Not a story about a rescue we haven't made. Not a promise that a journey will repair me."
{n}She writes 'Keep asking what remains possible,' then, on a separate line, 'Keep the lesson.'{/n}
"Both. They look very strange beside each other. I suppose my life does too."
{n}She turns the page without writing anybody else's future on it.{/n}''', c('[Ask about the first thing she wants to remember for herself.]', "own")),
    n("elan_gate", "Narrator", '''{n}The next page has Elan's name at the top. Nothing follows it yet.{/n}''',
      c('[Wait while she decides what to write about him.]', "elan_dead", requires=("seelah.elan_dead",)),
      c('[Ask what she would want to tell him.]', "elan_letter", forbids=("seelah.elan_dead",))),
    n("elan_dead", "Seelah", '''"I said I didn't want to make him agree with me just because he couldn't interrupt. That leaves a surprising amount of empty paper."
{n}She looks toward the far end of the bench. Then she takes up the pen.{/n}
"He could be so certain. I used to want to borrow it. I also wanted to argue with him. I don't want to lose that part because I've decided every memory has to be gentle."
{n}She writes slowly, shielding the page with her hand until she is finished. When she shows it to you, there is only one sentence beneath his name: 'I miss being able to disagree with you.'{/n}
"That is true. It doesn't tell anybody else how to remember him. I think I'll leave it there."
{n}She does not tear out the page or make it a message for you to deliver. It stays in her booklet, beside the untidy plans for her own life.{/n}''', c('[Sit with her until she is ready to turn the page.]', "own", flags=("seelah.late_elan_memory",))),
    n("elan_letter", "Seelah", '''"I could tell him about Istra. I could ask him something and leave enough space for an answer."
{n}She starts a sentence, frowns and draws a line through it.{/n}
"That sounded as though I was asking him to tell me I have learned the right lesson. I don't want to send him an examination of my character disguised as a letter."
{n}She begins again with a short description of the yard and the shields. This time she laughs at what she has written.{/n}
"I put in the part where I had to move the barrel twice. He is allowed to enjoy that."
{n}She folds a loose sheet into the booklet.{/n}
"I'll decide how to send it when I know where it can reach him. Writing his name doesn't put him in the next street."
{n}The draft remains with her. No answer is promised on his behalf.{/n}''', c('[Let the letter remain hers to send.]', "own", flags=("seelah.late_elan_draft",))),
    n("own", "Seelah", '''"Your turn. One thing you want that isn't an answer to something I have just said."
{n}She closes the booklet and puts the pen down, making it clear that she does not intend to keep minutes.{/n}
"And it can be small. You don't have to invent a new life before supper."
{n}When you hesitate, she smiles.{/n}
"This is harder when somebody actually asks, isn't it? I spent half a page proving it."
{n}Her fingers rest beside yours on the bench, close without quite touching.{/n}''',
      c('"I want to show you something I chose, without being useful to anyone for an hour."', "chosen", flags=("seelah.late_pc_delight",)),
      c('"I want a place where I can leave a few things and expect to find them when I return."', "place", flags=("seelah.late_pc_place",))),
    n("chosen", "Seelah", '''"Then choose it. I won't add a task on the way so that we can justify going."
{n}She gives you a sideways look.{/n}
"I may ask questions. And if you choose terrible music, I may have opinions. I would like the chance to find that out."
{n}She puts the booklet away without recording your wish as a duty she must perform. Before you rise, she leans her shoulder against yours for a moment.{/n}
"I'm glad you told me something I couldn't have guessed just by asking what would make my day easier."''', c('[Arrange the afternoon of the race.]', flags=("seelah.late_page_kept",))),
    n("place", "Seelah", '''"A few things. Not a building I have already filled with everybody who needs somewhere to sleep."
{n}She laughs, then looks at you more seriously.{/n}
"Yes. I think I would have misunderstood that. I would have offered to make a home and then started inviting half the street into it. You mean something you don't have to earn back each time you come through the door."
{n}She touches your fingers.{/n}
"We can try something smaller than a house. A place for something of yours, and mine, that nobody has to explain away. We'll see how it feels before we name the rest."''', c('[Arrange the afternoon of the race.]', flags=("seelah.late_page_kept",))),
], requires=("seelah.late_lesson_kept",))


s("late_race", "A song worth losing", '"Is this the afternoon you become intolerable?"', [
    n("start", "Seelah", '''"I have been intolerable for years. Today I receive public recognition."
{n}Seelah has tied her hair firmly back and left her armor behind. The yard is swept. Tavia has checked the cord, Breva is shifting the last empty barrel into position, and Dena has drawn a fresh starting line. A handful of spectators stand by the shed with their work baskets at their feet.{/n}
{n}Istra arrives carrying a stool. She plants it where she can see the exchange and tells Seelah that looking at the finish before making the last turn is an excellent way to kiss a barrel.{/n}
"I have other plans for my mouth," Seelah says, glancing at you.
{n}The glance lasts just long enough to be deliberate.{/n}''',
      c('[Take your place for the race.]', "preparation"),
      c('"I need to leave. Let us do this when I can stay."', abort=True)),
    n("preparation", "Narrator", '''{n}Before anyone runs, Seelah takes one turn around the course at a walk. She checks the gravel, ducks beneath the cord and brushes her fingertips over the peg. When she comes back, the amusement on her face has sharpened into concentration.{/n}''',
      c('[Ask about the practice she fitted around the regular lesson.]', "fixed", requires=("seelah.late_fixed_lessons",)),
      c('[Ask what the extra practice changed.]', "shared", requires=("seelah.late_shared_lessons",))),
    n("fixed", "Seelah", '''"I know what I do wrong. That is an achievement. Doing it right takes a little longer."
{n}She shows you the turn where she still loses speed.{/n}
"I kept Istra's hour. I had less practice than I wanted, and I spent some of it wanting more. Nobody burst into flame because I was annoyed about my own decision."
{n}She watches Tavia test the same turn without quite touching the barrel.{/n}
"I would make it again. Ask me after she beats me, though. I may explain it with worse manners."
{n}Istra calls that she can hear them perfectly well. Seelah waves back, unapologetic.{/n}
"She knows. I told her I wanted to win before I agreed on the hour. We have not built our friendship on the belief that I am wonderfully selfless."''', c('[Join the others at the line.]', "role")),
    n("shared", "Seelah", '''"That turn. And that one. Istra took the second half of the last practice lesson while I came here."
{n}She points to a scuff beside the third barrel.{/n}
"I nearly went back to see how she was doing. Then I remembered she would still be doing it if I stood beside her looking worried. I stayed and ran until I stopped kicking that stone."
{n}Istra catches her pointing and raises an eyebrow.{/n}
"I was saying you are very difficult to supervise," Seelah calls.
{n}"A condition I intend to maintain."{/n}
{n}Seelah smiles, then looks down the course again.{/n}
"Now I can't blame lack of practice. I shall need a more inventive explanation if I lose. We have ruled out the barrel moving. Apparently someone marked where it was."''', c('[Join the others at the line.]', "role")),
    n("role", "Narrator", '''{n}Tavia repeats the rules for the spectators, who immediately discover several opinions nobody asked for. Istra insists on one false start being forgiven, then tells everyone the second will not be.{/n}''',
      c('[Take the second-runner position beside Seelah.]', "running", requires=("seelah.late_running",)),
      c('[Take the finishing post while Dena joins Seelah.]', "watching", requires=("seelah.late_watching",))),
    n("running", "Narrator", '''{n}Seelah runs first against Tavia. Tavia gains half a pace at the cord; Seelah takes it back at the far peg. When she comes toward you, she holds the hoop low, exactly where you practiced. You take it without a stumble.{/n}
{n}Breva starts almost level with you. The first barrel passes, then the second. You duck beneath the cord and hear the spectators calling from somewhere behind you. At the third barrel there is room for a close turn, though it would force you to change your stride. The wider line is clear.{/n}
{n}Seelah calls your name. She does not tell you which way to go.{/n}''',
      c('[Take the close turn and reach for the peg.]', flags=("seelah.late_close_turn",), check=dict(Skill="SkillMobility", DC=26, Success="narrow", Failure="stumble", CommanderOnly=True)),
      c('[Keep your stride on the wider line and finish cleanly.]', "wide", flags=("seelah.late_wide_turn", "seelah.late_race_lost"))),
    n("narrow", "Narrator", '''{n}You plant your foot close to the barrel, turn and stretch the hoop toward its peg. It catches, swings once and settles. Breva's hoop lands a moment later.{/n}
{n}Seelah throws both arms up. Then she remembers she has to move out of the lane and does so just before Breva arrives with a breathless complaint about the width of the universe.{/n}
"I knew you could do it," Seelah says, taking your hands.
{n}"She was making the face of a woman who knew nothing of the sort," Istra observes.{/n}
"I was experiencing a private victory in advance."
{n}Seelah is flushed and grinning. She squeezes your hands once more before letting you catch your breath. Tavia comes to inspect the pegs, finds nothing to dispute and asks how many verses they have condemned themselves to sing.{/n}''', c('[Let Seelah choose the song.]', "won", flags=("seelah.late_race_won",))),
    n("stumble", "Narrator", '''{n}Your planted foot slides over loose grit. You catch yourself against the barrel, keep the hoop in your hand and reach the peg after Breva. By the time yours settles, she is walking back toward Tavia with both hands raised.{/n}
{n}Seelah meets you beyond the course, looking first at your footing and then at your face.{/n}
"Still in one piece? Good. Then I can be disappointed about the race instead of frightened about you."
{n}She waits while you test your balance. There is a scuff on your sleeve where you caught the barrel, but nothing that stops you walking beside her.{/n}
"I was about to complain that they put the gravel in our way. Then I remembered showing you where it was. That would have spoiled the argument."
{n}She takes your hand and bows toward the spectators with exaggerated dignity. Tavia begins considering songs.{/n}''', c('[Face the losing song together.]', "lost", flags=("seelah.late_race_lost", "seelah.late_race_stumbled"))),
    n("wide", "Narrator", '''{n}You take the wider line without losing your footing. Breva makes the shorter turn and reaches the peg first. Your hoop lands after hers, upright and entirely too late.{/n}
{n}Seelah meets you beyond the course. She looks at the two hoops, then back at you.{/n}
"I had a whole speech ready. It was going to be unbearable."
"You could give it anyway."
"No. Tavia would enjoy stopping me too much."
{n}She takes your hand and raises it briefly toward the spectators before bowing with exaggerated dignity. The applause makes her laugh.{/n}
{n}"Finishing without breaking my barrels counts for something," the cooper calls from the shed.{/n}
"There. We have won a very particular kind of admiration."
{n}She draws you out of the lane while Tavia confers with Breva about the song.{/n}''', c('[Face the losing song together.]', "lost")),
    n("watching", "Narrator", '''{n}Seelah runs first against Tavia, loses a little ground beneath the cord and gains it at the peg. She returns with the hoop low. Dena takes it cleanly, and Breva launches herself after her.{/n}
{n}From the post you can see the difference at the last turn. Dena takes it tightly enough to slow; Breva goes wider without breaking stride. Dena reaches her peg first, but the hoop strikes the end and falls. Breva's hoop settles a heartbeat later.{/n}
{n}Dena looks back at you. Tavia has begun celebrating. Seelah saw the fallen hoop too.{/n}
"The hoop has to stay," she says before anyone asks. "That was the rule."
{n}Dena groans, picks it up and replaces it with immense care. Seelah goes to meet her, clapping her on the shoulder.{/n}
"You were fast enough. Next time we negotiate with the peg beforehand."
{n}She comes to stand beside you, still breathing hard.{/n}
"Did I at least look as though I intended to win?"''',
      c('"Very convincingly. I particularly admired your expression at the peg."', "lost", flags=("seelah.late_race_lost",)),
      c('"I liked watching you want something that much."', "lost", flags=("seelah.late_race_lost",))),
    n("won", "Seelah", '''"The shortest song I know."
{n}Tavia looks suspicious. Seelah sings the first line, and the entire audience discovers why: it is a washing song whose last word becomes the first word of the next verse. Nobody can agree on when it ends.{/n}
{n}Breva makes it through three verses before pointing out that victory has made Seelah cruel. Seelah accepts surrender and joins the fourth verse herself, badly enough that Istra threatens to teach her breathing as well as footwork.{/n}
{n}When the laughter quiets, Seelah leans close to you.{/n}
"I am going to remember that turn for a very long time. You should prepare to hear about it when I am old and impossible."
{n}Then she bends to lift the starting post. The cooper wants the yard back, and winning has not changed whose hands are available.{/n}''', c('[Help clear the course.]', "clear")),
    n("lost", "Seelah", '''{n}Tavia chooses a song about a woman who keeps returning to a house because she has forgotten something, until everybody but the woman knows why she goes there. Seelah learns the first verse, invents the words of the second and becomes unexpectedly convincing by the third.{/n}
{n}At the line about forgetting her own good sense, she looks straight at you. Dena notices and sings louder to cover her laugh.{/n}
"I have lost with grace," Seelah announces afterward. "Anybody saying otherwise will have to sing it again."
{n}She leans close enough that the next words are yours alone.{/n}
"I would still prefer to have won. I had a much worse song ready."
{n}Then she helps Tavia wind up the cord. The disappointment has not vanished, but it has become part of an afternoon she plainly wants to keep.{/n}''', c('[Help clear the course.]', "clear")),
    n("clear", "Narrator", '''{n}The barrels go back against the shed. Istra carries her stool away after making Seelah promise only to tell her when another race is planned, not to organize one before anyone has recovered from this one.{/n}
{n}When the yard is empty, Seelah finds a scrap of cord still caught around the post. She unwinds it, puts it with the rest and turns to you.{/n}
"There. Now I would like to find out whether I have enough dignity left to ask you for another evening."
{n}Her smile makes it clear that dignity is unlikely to stop her.{/n}''', c('"Ask me."', flags=("seelah.late_race_kept",))),
], requires=("seelah.late_lesson_kept", "seelah.late_page_kept"), delay=48)


s("late_afterglow", "The verse she remembers", '"You were going to ask me for an evening."', [
    n("start", "Seelah", '''"I was. Somewhere with a door and no audience permitted to correct the words. I've had the tune from the race in my head ever since."
{n}You meet again on a later evening. She has arranged the use of a small room above the cooper's shed until morning. The owner has taken her payment and made one request: no practicing turns on the floorboards. There is a narrow bed, a basin and a chair whose missing rung has been replaced with a darker piece of wood.{/n}
{n}Seelah puts a jug of water on the table. She has washed the shirt she wore at the race and brought it to mend: a caught thread trails from the sleeve where it brushed the cord. She leaves it folded over the chair.{/n}
"I would like to kiss you. I would also like you to know that before you spend the evening wondering why I keep losing my place in perfectly simple sentences."''',
      c('[Come in and close the door.]', "race"),
      c('"I cannot stay tonight. Ask me again."', abort=True)),
    n("race", "Seelah", '''{n}She pours the water, takes a drink and gives you the other cup. The room has just enough space to move without deciding in advance who will stand where.{/n}''',
      c('"Have you stopped enjoying the victory?"', "victory", requires=("seelah.late_race_won",)),
      c('"Do you remember the song?"', "song", requires=("seelah.late_race_lost",))),
    n("victory", "Seelah", '''"No. I tried modesty on the stairs. It didn't suit me."
{n}She demonstrates the last turn with two fingers on the table, then catches herself smiling at the tiny performance.{/n}
"I keep remembering the hoop settling. The moment before it did, I was certain we had lost it. Then there it was."
{n}She puts down her cup and looks at you.{/n}
"And then you looked back at me. That is the part I keep getting to after I've finished pretending this is all about my magnificent victory."
{n}She touches the back of your hand, still smiling.{/n}
"Come closer. I have spent quite enough time describing how you looked from the other end of a yard."''', c('[Turn your hand beneath hers.]', "ask")),
    n("song", "Seelah", '''"Most of it. Unfortunately."
{n}She hums the tune, then tries the verse about the forgotten key. Halfway through she realizes she has combined it with the verse about the woman returning for her scarf.{/n}
"A well-prepared woman. She never runs out of reasons."
{n}She stops humming and looks at you over the rim of her cup.{/n}
"I used to think it would be terribly embarrassing to have everyone know whom you wanted to look at. Apparently I can survive several people noticing. Dena certainly noticed. She nearly swallowed the last verse."
{n}She sets the cup aside.{/n}
"I didn't hate it. I liked knowing you were there when I looked. I am trying to tell you something flattering without comparing you to a peg or a barrel. Give me a moment."''', c('"You are doing rather well."', "ask")),
    n("ask", "Seelah", '''{n}She steps closer. You can see where she has missed a little chalk at the side of one finger.{/n}
"Then let me finish before I improve it to death. I want you close. I want to kiss you until I stop planning the next clever thing to say."
{n}Her hand settles at your waist, lightly enough that you can move away. She waits for your answer, the confidence of the race giving way to something more intent.{/n}
"And if what you want tonight is to sit with me and laugh about the song, I can want that too. I won't pretend I asked for it first."
{n}She smiles at that, but does not turn the question into a joke.{/n}''',
      c('[Kiss her and ask to stay the night.]', "night", flags=("seelah.late_night_chosen",)),
      c('[Kiss her, keeping the evening to that closeness.]', "kisses", flags=("seelah.late_kisses_chosen",)),
      c('"Sit with me. I want your company without going further tonight."', "quiet", flags=("seelah.late_quiet_chosen",))),
    n("night", "Seelah", '''"Yes."
{n}She kisses you before the word has quite left her mouth. One hand moves to the back of your neck; the other draws you nearer, and for a while neither of you finds a use for speech.{/n}
{n}When she draws back, she is laughing softly at herself.{/n}
"There. I have forgotten every clever thing."
{n}You touch the chalk still caught beside her finger. She looks down, rubs it away and takes your hand again. This time she brings it to her lips.{/n}
{n}The room grows quiet around you. She pauses to ask what you like, listens to your answer and tells you what she wants in return. Clothes are set aside without haste. Later, when you settle together beneath the blanket, she reaches for you with none of the uncertainty of the first question.{/n}
{n}In the morning she wakes before you and stays long enough to make staying obvious. Her thumb moves once across your shoulder.{/n}
"Good morning. I am considering being very difficult to get out of bed."''',
      c('"Begin with five more minutes."', "morning", flags=("seelah.late_night_kept", "seelah.kissed"))),
    n("morning", "Narrator", '''{n}She grants the five minutes and negotiates shamelessly for several more. Eventually the sounds of the shed beginning its day's work settle the matter.{/n}
{n}Seelah washes, finds her clothes and returns your things before collecting her own. At one point she drops a boot, winces at the noise and listens for a complaint from below.{/n}
"I promised not to practice turns. I said nothing about managing footwear with grace."
{n}At the door she kisses you again, slower than the hurried sounds from the yard would seem to allow.{/n}
"I want another morning. We can find out when it fits. I wanted to say the wanting first."''', c('[Leave the room together.]', "plans")),
    n("kisses", "Narrator", '''{n}She meets your kiss with a pleased sound, then lets you draw back far enough to tell her what you mean. Her hand stays warm at your waist.{/n}
"Then that is what we do."
{n}You sit together at the edge of the bed because the chair is too narrow for two. Seelah makes one attempt at humming the afternoon's tune, abandons it when you touch her cheek and kisses you again.{/n}
{n}The evening passes in pauses that are no longer awkward: a drink of water, a remembered joke, the brush of her fingers against your cheek when you lean closer. She does not treat each pause as another chance to ask for more.{/n}
{n}Before it is time to go, she rests her forehead briefly against yours.{/n}
"I wanted this. I am glad I didn't waste the evening being brave enough to hint."''', c('[Hold her close before leaving.]', "plans", flags=("seelah.kissed",))),
    n("quiet", "Seelah", '''"All right. Come here."
{n}She sits on the bed and moves a folded blanket out of the way. When you sit beside her, she offers her hand without drawing you any closer than you choose.{/n}
"I won't sing unless asked. That is the most valuable thing I have offered anyone today."
{n}You talk about the afternoon: Tavia repeating the rules over everyone's helpful objections, the cooper counting his barrels afterward, Istra's unconcealed delight whenever Seelah was contradicted. Seelah admits that she has already thought of a different way to take the third turn.{/n}
"You see what you have encouraged. There will be diagrams."
{n}She draws one on her palm with a fingertip, then discovers that the most important barrel has ended up on the side of her thumb. The explanation collapses into laughter.{/n}
{n}When you rise to leave, she holds your hand a moment longer before letting it go.{/n}
"I would like you to come again. Exactly as much as I would have before I asked the other question."''', c('[Arrange another time together.]', "plans")),
    n("plans", "Seelah", '''{n}Before you part, she brings out the little booklet. The page of plans is more crowded now, with a short description of the race wedged beneath the first line.{/n}
"There's one thing we could begin before we start talking as though a future has to arrive all at once."
{n}She looks from the page to you.{/n}
"Your wish. I remember it. Let's find a piece of it we can actually do here. After that we can decide what the larger version means."
{n}She puts the booklet away. This time she is offering a particular next meeting, not the whole unwritten life beneath it.{/n}''', c('[Make time for the next visit.]', flags=("seelah.late_evening_kept",))),
], requires=("seelah.late_race_kept",))


s("late_first_step", "Something left for next time", '"Let us try the thing we talked about."', [
    n("start", "Narrator", '''{n}Seelah meets you without armor, her little booklet tucked into her belt. She has left the afternoon clear long enough to begin without watching every movement of the sun.{/n}
"Ready? I was afraid I'd be late. Istra asked me a question at the gate, and I had to explain why I was answering while backing away."
{n}She waits while you finish what brought you to the meeting place. When you are ready, she offers you her arm.{/n}''',
      c('[Go with her.]', "wish"),
      c('"I need to choose another day for our outing."', abort=True)),
    n("wish", "Seelah", '''"You asked for something of your own in the middle of all my planning. I would like to begin there."''',
      c('[Take her to the music you chose.]', "music", requires=("seelah.late_pc_delight",)),
      c('[Ask to see the place she found for your things.]', "shelf", requires=("seelah.late_pc_place",))),
    n("music", "Narrator", '''{n}You have chosen a small gathering in a courtyard, where a woman with a reed pipe plays for whoever can spare the time to listen. Her hair is silver, her fingers quick, and she announces each tune by the person who taught it to her rather than the name anyone expects.{/n}
{n}Seelah settles beside you and listens. During the first tune she looks as though she wants to say something, then keeps it until the last note has faded.{/n}
"I thought it was going somewhere else. The part in the middle. I kept waiting for it to come back."
{n}The musician hears her and plays the passage again, more slowly. This time Seelah follows the turn of it, tapping one finger against her knee.{/n}
{n}When the musician begins the next tune, Seelah looks at you instead of the gathering.{/n}
"Show me the part you like. I won't try to guess what I ought to like first."''',
      c('[Point out the quiet phrase before the tune rises.]', "quiet_phrase", flags=("seelah.late_music_quiet",)),
      c('[Tap the quick rhythm that made you choose it.]', "quick_phrase", flags=("seelah.late_music_quick",))),
    n("quiet_phrase", "Seelah", '''{n}She waits for the phrase. When it comes, she stops tapping. Her attention holds through the brief quiet after it, and you see her understand why you wanted her to wait.{/n}
"There. It leaves you expecting the next bit."
{n}She tries to hum it afterward and loses the last note. The musician supplies it without interrupting her packing, then asks if she wants to learn the whole tune.{/n}
"Not today," Seelah says. "I want to listen to it once without making it something I have to be able to do."
{n}She finds your hand beneath the edge of the bench.{/n}
"I would come back for that. You don't have to sell me the rest of the afternoon."''', c('[Stay until the musician finishes packing.]', "carry")),
    n("quick_phrase", "Seelah", '''{n}She catches the rhythm under your fingers and answers it on her knee. When the tune quickens she looks delighted, then loses the beat and laughs at herself.{/n}
"All right. That was an unreasonable number of notes."
{n}Afterward the musician shows her the beat again on the side of the pipe case. Seelah gets it on the second attempt and immediately tries to make you keep it while she adds the wrong accent.{/n}
"You chose the music. You knew what sort of company you were inviting."
{n}She stops before the joke becomes a performance for the whole courtyard. Her fingers curl around yours instead.{/n}
"Yes. I would like to come again. Next time I will have forgotten the difficult part and be very confident about it."''', c('[Stay until the musician finishes packing.]', "carry")),
    n("shelf", "Narrator", '''{n}The cooper has agreed to rent Seelah a small locking cupboard in the room above the shed. It is hardly bigger than a chest stood on end. The key turns stiffly, and the lower shelf has a dark mark where something once leaked.{/n}
"It isn't a house," Seelah says. "It isn't even a very persuasive beginning of a house. But it's ours to use for the period I've paid for. Nobody else gets to decide that the space is wasted because we aren't standing in front of it."
{n}She has left a small parcel beside the cupboard. She unwraps it to reveal a plain cup and a strip of cloth, neatly folded. She puts them on the lower shelf, then moves them to one side to leave room.{/n}
"What would you put here? Something you would actually want to find again. We don't have to make it impressive."''',
      c('[Choose an ordinary keepsake to leave beside her cup.]', "keepsake", flags=("seelah.late_shelf_keepsake",)),
      c('"Leave my part empty today. I want to know it will still be there when I choose."', "space", flags=("seelah.late_shelf_space",))),
    n("keepsake", "Narrator", '''{n}You set a small personal keepsake beside the cup. Seelah shifts the cup a little farther back so that its handle will not catch when you reach for your things.{/n}
"That looks more like it."
{n}She closes the cupboard, turns the key and hands it to you. Then she holds up its mate.{/n}
"I asked for two. The cooper asked whether I meant to lose both. I said I would begin with one and judge my progress."
{n}She opens it again before you leave, simply to look. The keepsake and cup are exactly where you put them. She seems almost embarrassed by how much she enjoys that.{/n}''', c('[Close it together.]', "carry")),
    n("space", "Seelah", '''"Then it stays empty."
{n}She starts to move the cloth into the gap, catches herself and folds it beneath the cup instead.{/n}
"I was doing it already. Making the space useful."
{n}She shuts the cupboard and turns the key, then gives it to you. She has a second one for herself.{/n}
"There. You can check whether I've filled it with worthy causes. I will try to spare you the investigation."
{n}Before you leave, she opens the cupboard once more and looks at the empty part of the shelf. This time she leaves it alone without having to stop her hand.{/n}
"I like that you can bring something later. It makes later feel like a visit we might actually make."''', c('[Close it together.]', "carry")),
    n("carry", "Seelah", '''{n}Outside, Seelah finds a quiet place to stand before the traffic of the street can carry you apart.{/n}
"Again, please. I want another afternoon, and I'd rather ask you now than discover I've volunteered us both for something else."
{n}She brings out the booklet, though she does not open it yet.{/n}
"What I said about journeys and questions still matters. Today didn't settle it. It gave me something I would want to come back to."
{n}Her eyes meet yours.{/n}
"And I want to know what you think that means. Especially if we have already started using words that sound as though everything has been decided."''',
      c('"We have made a commitment. These are things I want inside it."', "committed", requires=("seelah.committed",)),
      c('"I want to keep learning this before making a larger promise."', "courting", forbids=("seelah.committed",))),
    n("committed", "Seelah", '''"So do I. I still mean what I promised. I want the promise to have days in it that resemble us."
{n}She opens the booklet and adds a short line beneath the description of the race. She lets you read it before closing the cover.{/n}
"That doesn't decide where I will need to go. It tells me one thing I want to do when I can return."
{n}She offers you her hand.{/n}
"And I would like another race, eventually. I think I have begun to understand the third turn. Please don't tell Tavia I said that. She'll arrange another barrel."
{n}The laugh that follows is easy, though she has left the harder question where both of you can see it.{/n}''', c('[Keep her hand as you walk back.]', "end")),
    n("courting", "Seelah", '''"Then we keep learning it. I haven't mistaken a cupboard or a tune for a vow."
{n}She smiles, but lets the answer stand without asking you to soften it.{/n}
"I want the larger conversation when we are ready. Until then I would rather know which evening you actually want than be told every evening belongs to me."
{n}She opens the booklet and adds a short line beneath the description of the race. Then she puts it away and offers you her hand.{/n}
"For now, I have several very particular wishes. Another lesson that works. Another run. Another chance to discover what you like when nobody needs us to like it."
{n}She waits for you before starting back toward the busier street.{/n}''', c('[Walk back with her.]', "end")),
    n("end", "Narrator", '''{n}At the corner, Seelah pauses to let a cart pass. There is somewhere she needs to be, and she tells you when she expects to be free again.{/n}
{n}She glances down the street toward the yard.{/n}
"Next time, we try the course the other way around. I want to see who complains first."
{n}She squeezes your hand before letting it go.{/n}
"Don't be late."''', c('[Keep the next visit in mind.]', flags=("seelah.late_campaign_kept",))),
], requires=("seelah.late_evening_kept",))
