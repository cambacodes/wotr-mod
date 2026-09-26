"""Aivu's authored Chapter 3 friendship project, using the existing Azata pet.

No romance, age change, new pet, power grant, rescue claim or quest mutation.
Capital attachment still requires live verification of the native default dialogue.
"""
from story_format import c, n, scene

UNIT = "32a037e97c3d5c54b85da8f639616c57"
AREA = "2570015799edf594daf2f076f2f975d8"
ANSWER_LIST = "f1a65c6d838f58d49ad4ff40544b895b"
ETUDES = {
    "aivu.absent": "39008f5a372a6dc42bddfcf4f334bd95",
    "aivu.detached": "0ece5844b86deb44ea9d54190de1463e",
}
RELATIONSHIP = dict(
    Title="The city underneath", Description="Aivu is making a map of Drezen. She has asked for help with the parts that cannot be seen from the air.",
    Objective="Help Aivu explore Drezen", Guidance="During Chapter 3, speak with your existing Azata companion in Drezen. Leave time between outings.",
    StartedFlag="aivu.started", ClosedFlag="aivu.closed", CommittedFlag="aivu.trusted",
    UnavailableFlags=["aivu.absent", "aivu.detached", "devil", "swarm", "true_lich", "legend", "dragon"], FailureFlags=[],
)
SCENES = []


def s(id, title, entry, nodes, requires=(), delay=24):
    SCENES.append(scene("aivu." + id, title, "Aivu", 3, entry, nodes,
        Relationship="aivu", Chapters=[3], last=3, Areas=[AREA],
        AnswerLists=[ANSWER_LIST], ContactUnit=UNIT,
        requires=("azata", *requires), forbids=("aivu.closed", *RELATIONSHIP["UnavailableFlags"]),
        optional=True, delay=delay))


s("a_city_with_wings", "A city with wings", '"What are you drawing, Aivu?"', [
    n("start", "Aivu", '''{n}Aivu has spread a scrap of wrapping paper on the ground. Several stones hold its edges down. The largest drawing resembles a boot with three chimneys; a smaller one has teeth.{/n}
"Don't step on that! That's where we are. If you stand on it, I can't draw you standing on it. There won't be room."
{n}She moves a stone with great care. It uncovers another, smaller boot.{/n}
"It's Drezen. From above. Everyone keeps pointing at corners and saying things like 'after the other corner,' and then nobody knows where anyone is. I asked a man where he lived and he said opposite the place that used to sell buckets. It doesn't sell buckets now! How am I supposed to find that?"
{n}She puts a claw beside the toothed building.{/n}
"That's the Terrible House of Things That Smell Like Boiled Socks. I think they do laundry. Or they're making a very bad soup. We should find out."''',
        c('"You want me to explore it with you?"', "plan"),
        c('"Keep a place for me. I have to go."', abort=True)),
    n("plan", "Aivu", '''"Yes! You can do the doors. People are very particular about doors. They say 'come in,' but if you come in through a window, suddenly that's wrong."
{n}She considers the paper, then adds a tiny door to the toothed house.{/n}
"I can see all the roofs. I can see where the birds go, and the bits of wall people can't reach, and somebody has a garden in a broken cart. But I don't know what happens underneath. Maybe the bucket man has something wonderful inside his house and everyone keeps asking him about buckets."
"Do you want this to be useful, or wonderful?"
"Both. A useful thing should be allowed to be wonderful. Otherwise who would want to use it?"
{n}Her tail curls around a loose corner before the breeze can take it.{/n}
"But I want it to be mine. Not a map somebody makes me copy because mine has too many birds. I know how many birds I saw."''',
        c('"Choose our first place. I will ask the questions."', "names"),
        c('"Then show me something the soldiers\' maps leave out."', "names")),
    n("names", "Aivu", '''{n}She leads you to the lane beside the laundry. A woman with her sleeves tied above her elbows is trying to work a wooden peg free of a washing line. Aivu stops well clear of the hanging sheets.{/n}
"Excuse me! Is this the Terrible House of Things That Smell Like Boiled Socks?"
{n}The woman looks at Aivu, then at you.{/n}
"Only before noon. Afterwards it's the House of Things That Still Smell Like Boiled Socks. Name's Nessa. What do you need?"
"A name for my map."
"Laundry will do."
"But it won't tell people which one."
"The only one with my name over the door."
{n}Aivu looks up. The lettering is faded and partly hidden by a sheet.{/n}
"Oh. I couldn't see that from the sky."
{n}Nessa finally frees the peg. She points it toward a narrow passage beside the house.{/n}
"Put that on your map if you're making one. New hands keep taking the long way to the pump. And mark the step. Somebody will break a tooth on it."
{n}Aivu peers into the passage. Her fanciful city has acquired its first instruction from someone who lives in it.{/n}''',
        c('"Give it both names. Nessa\'s Laundry, also known as the Terrible House."', "two_names"),
        c('"Keep your wonderful names on one side. Put the names people ask for on the other."', "two_sides")),
    n("two_names", "Aivu", '''"An enormous name! It will need an enormous house."
{n}Aivu studies the scrap, then turns it sideways.{/n}
"Or smaller writing. That might be less work."
{n}Nessa agrees to the double name, provided her customers can find the laundry without first reading an adventure. Aivu insists that finding clean socks can be an adventure. Nessa agrees with that, too.{/n}
{n}You copy the ordinary name in clear letters. Aivu adds her own beneath it, with a sock hanging from the last letter. Then the two of you walk the passage and count the steps to the pump. She tries to draw the dangerous step large enough to look dangerous, but the result appears to block the whole lane.{/n}
"I'll put an arrow. That means look here. It doesn't mean the step is chasing you."
{n}Nessa supplies a clean piece of discarded wrapping paper. Aivu accepts it as gravely as a treaty.{/n}
"Tomorrow I want to see the roofs from down here. You can come. But don't tell me all the answers before I've looked."''',
        c('"I will leave some discoveries for you."', flags=("aivu.started", "aivu.map_both_names"))),
    n("two_sides", "Aivu", '''"Then people can get lost twice! No, wait. They could turn it over and stop being lost. That's better."
{n}Nessa finds a clean piece of discarded wrapping paper. You mark the laundry on one side; Aivu draws it on the other, matching the position by holding the sheet against the light.{/n}
"This side is for finding things. This side is for telling someone what you found."
{n}You walk the passage and count the steps to the pump. Aivu wants to call the awkward step the Tooth Collector. Nessa says that is a fine name as long as it makes people look down. On the practical side, you draw a warning beside it.{/n}
{n}Aivu turns the paper over and back several times, pleased by the existence of two cities in the same place.{/n}
"Tomorrow I want to see the roofs from down here. You can come. But don't tell me all the answers before I've looked. I don't want the whole city finished while I'm asleep."''',
        c('"We will discover the next part together."', flags=("aivu.started", "aivu.map_two_sides"))),
], delay=0)

s("the_roof_below", "The roof below", '"Shall we look at your city from underneath?"', [
    n("start", "Aivu", '''{n}Aivu brings the map rolled around a stick. She has added three birds, a patch of weeds, and a shape labeled 'probably a cat.'{/n}
"It was asleep. I didn't want to wake it just to ask."
{n}At the laundry lane she stops. One of the poles supporting a drying awning leans away from its socket. A strip of fabric hangs from it. Beneath the awning, a young laundry hand is gathering damp shirts out of the dirt.{/n}
"I did that," Aivu says.
{n}The words come out before you can ask.{/n}
"Yesterday. After we went away. I came back because the map didn't have the courtyard. I thought I could land on the wall. Then the cloth moved and I tried to miss it, and my wing hit the pole."
{n}The laundry hand glances over. His knuckles are scraped. He lowers his eyes when he recognizes you.{/n}
"I said I'd fix everything," Aivu adds. "I brought another pole. But it doesn't fit in the hole. And he won't tell me where they keep the tools."
"My name's Jori," the young man says. "And I'm not putting a saw in a dragon's mouth."''',
        c('"Let us hear what Jori needs before we promise anything else."', "listen"),
        c('"We should ask Nessa to lend us the proper tools and show us."', "listen"),
        c('"We need time to do this properly. I will return."', abort=True)),
    n("listen", "Aivu", '''{n}Nessa comes out carrying a basket. She sets it down beyond reach of the mud.{/n}
"The pole needs its end shaved. The socket needs clearing. The shirts need washing again. Nobody was killed, which is very welcome, but doesn't make the shirts clean."
"I know! I said I was sorry."
"You did. Jori heard you. He also heard you coming down behind him. Give him a little room."
{n}Aivu retreats a pace. Jori's shoulders loosen.{/n}
"I thought the whole wall was falling," he says. "Then I thought it was a demon. Then I thought I was an idiot for thinking it was a demon. It was a busy moment."
"I'm not a demon."
"I know that now."
{n}Aivu looks at his scraped hand. She does not repeat herself.{/n}
"I can carry water. I won't spill it."
"You might," Nessa says. "Everyone does. Start with one bucket."
{n}The awning can be restored today if you work beside Nessa while Jori rewashes the shirts. Or you can help with the shirts, leaving Jori the quieter task of fitting the pole with Nessa. Neither job will finish itself.{/n}''',
        c('[Work on the awning. Give Jori space to choose when he speaks to Aivu.]', "pole"),
        c('[Help wash the shirts. Let Aivu carry water to your shared work.]', "water")),
    n("pole", "Aivu", '''{n}Nessa hands you a rasp and shows you where the new pole catches. Aivu watches the first few strokes, then takes her bucket toward the pump. She walks, although the detour visibly annoys her.{/n}
{n}By the fourth trip she has learned to stop before putting the bucket down. By the sixth, Jori has begun to point where he wants it. Neither makes a ceremony of this.{/n}
"How many more?" she asks.
"Two. Then clean water for the rinse."
"That sounds like more than two."
"It is."
{n}She looks longingly up the lane, then takes the empty bucket.{/n}
{n}You fit the pole twice before Nessa is satisfied. When it stands firm, Aivu asks whether she may hold the fabric clear while you tie it. Jori says he can manage. She lets him.{/n}
{n}At last the awning throws a straight-edged patch of shade across the courtyard. Jori sits in it to eat. Aivu remains by the gate.{/n}
"He still doesn't want me close," she whispers.
"He may need longer."
"The pole didn't."
{n}She knows the difference. The unfairness of it still troubles her.{/n}
"I'll ask before I come into the courtyard next time. Then he won't have to guess what the noise is."''',
        c('"That is a promise you can keep."', flags=("aivu.repaired", "aivu.jori_space"))),
    n("water", "Aivu", '''{n}Jori gives you the shirts as readily as if you had always worked here. His relief at leaving the washing trough is rather less professional.{/n}
{n}Aivu carries water from the pump. She fills the first bucket too high and arrives with wet forelegs. You wring out a shirt and wait while she experiments with the second. She learns to stop before lowering it, instead of setting it down at the end of a lurch.{/n}
"This shirt is much smaller than it was," she observes.
"It is folded."
"I know! I was checking whether you knew."
{n}From the pole comes a brief laugh. Jori works the rasp again before Aivu can look around.{/n}
{n}The shirts take longer than you expect. Aivu offers to hurry the drying with her wings; Nessa points out the mud around your feet. Aivu closes them.{/n}
"Right. Another bad idea nearly escaped."
{n}When the awning stands, Jori brings his scraped hand to the trough to wash it. Aivu asks whether it hurts. He says yes. She asks whether he wants her to go away. He considers that one before answering.{/n}
"Just tell me before you land behind me."
"I can do that. Loudly?"
"Ordinarily will do."
{n}She practices a thoroughly ordinary hello. The second attempt is quieter than the first.{/n}''',
        c('[Finish the washing before leaving together.]', flags=("aivu.repaired", "aivu.jori_talked"))),
], requires=("aivu.a_city_with_wings",))

s("a_way_for_feet", "A way for feet", '"Have you found the next place for your map?"', [
    n("start", "Aivu", '''"I found a shortcut! A real one. Not a dragon shortcut. You don't have to fly over anything."
{n}Aivu unrolls the map. An alley behind the laundry leads toward a narrow archway, then emerges near the pump. She traces it with the blunt side of a claw.{/n}
"Nessa says people used to go through there, but there's rubbish in the middle now. If we clear it, Jori won't have to carry all his buckets around the other way."
{n}Her excitement falters a little.{/n}
"I haven't promised him. I thought I'd look at the rubbish first."
{n}Beyond the arch, fallen plaster surrounds a broken handcart. Its axle has wedged between two stones. There is room for a person to squeeze past, but the handles obstruct anyone carrying a full bucket. Aivu approaches the arch, folds her wings, then stops.{/n}
"It gets smaller after the corner."
{n}A loose pebble falls from the cart as you test its handle. The sound echoes sharply. Aivu's claws scrape the ground.{/n}
"I don't want to put my wings in there. I thought I would when I got here, but I don't."''',
        c('"Stay outside. We can work out what to do from here."', "outside"),
        c('"We can leave the cart. Your map can mark the long way."', "long_way"),
        c('"Let us return when we have time to inspect it."', abort=True)),
    n("outside", "Aivu", '''"You aren't going to say I'm too big to be frightened?"
"Would that make the passage wider?"
"No. It would make me want to bite it. Which probably wouldn't help."
{n}She settles back from the entrance, where she can spread her wings without touching either wall.{/n}
"I can watch the outside. And you can tell me what the cart is doing. No going quiet and then making a crash."
{n}You inspect the stones around the axle. The arch itself appears sound, but hauling on the cart might dislodge the loose heap beside it. Nessa has a rope; she also has work to finish before she can lend a hand. There is no urgent reason to hurry.{/n}
"Could we take the cart apart?" Aivu asks. "It doesn't look as if anyone is going to use it. Except spiders. We'd have to warn them."
{n}A crow lands on the wall above her. She looks up, offended by its easy view.{/n}
"Or you could find which stone is holding it. I can see the top, but not the bottom."''',
        c('[Inspect the axle and the heap before moving anything. Perception DC 18.]', check=dict(Skill="SkillPerception", DC=18, Success="lever", Failure="wait")),
        c('"We will wait for Nessa and dismantle it carefully."', "wait")),
    n("lever", "Aivu", '''{n}A pale scrape shows where one stone has shifted against the axle. You wedge a piece of timber beneath the cart before easing the stone back. The wheel turns a fraction.{/n}
"It moved! Did you want it to?"
"Yes. Now we stop and get the rope."
{n}Aivu looks disappointed, then pleased that this is an errand she can do. She calls to Nessa from outside the courtyard. When she returns, the rope trails from her mouth, carefully kept out of the dirt.{/n}
{n}With the rope looped around the cart, you guide it while Aivu pulls from the open lane. You call each movement before it happens. She calls back, sometimes adding suggestions that have nothing to do with carts. Gradually the axle comes free.{/n}
{n}The cart emerges with a sudden scraping rush. Aivu plants her feet and stops it before it can strike the opposite wall.{/n}
"Ha! That was a good crash. A crash we knew about."
{n}You move the loose plaster aside. The passage is usable again, though Aivu declines to try it herself. She draws an arrow through it, then another around the outside.{/n}
"One for feet. One for wings. You can use whichever one fits."''',
        c('[Help her mark both ways accurately.]', flags=("aivu.shortcut_open", "aivu.cart_whole"))),
    n("wait", "Aivu", '''{n}The heap refuses to reveal a safe first move. You leave the cart where it is and ask Nessa for help. She cannot come until the washing is hung. Aivu wants to assist, but waits at the courtyard entrance until invited.{/n}
{n}The three of you return with a saw, a hammer, and rope. Nessa braces the cart while you remove the handles. Aivu holds the rope from the open lane, keeping the broken frame from sliding farther into the passage. It is slow work. Twice she asks whether the next part will be the last. Twice Nessa says no.{/n}
"I thought being helpful would have more exciting bits," Aivu confides.
"You can stop when you need to," Nessa says. "Tell us first."
{n}Aivu asks for a break. You prop the frame securely and sit in the sun. When she is ready, the work resumes without anyone calling her lazy.{/n}
{n}By the time the cart is out, it is a stack of salvageable boards. Nessa takes those home for kindling. Aivu marks the cleared passage but keeps a second arrow around the outside.{/n}
"That's my way. The other one is for buckets. And people carrying buckets. The buckets shouldn't go alone."
{n}Her wings stay folded loosely now, with empty air on either side.{/n}''',
        c('[Walk the cleared passage to check the map.]', flags=("aivu.shortcut_open", "aivu.cart_dismantled"))),
    n("long_way", "Aivu", '''"Even if the long way is longer?"
"It is still a way."
{n}Aivu considers the dark corner, then backs into the lane. She shakes her wings out one at a time.{/n}
"We should tell Nessa before she thinks we've fixed it. I didn't promise, but I did say it was a very good shortcut."
{n}Nessa listens to your account of the wedged axle. She is disappointed, but agrees that moving the cart without proper help is a poor bargain for a few saved steps. She will ask a carpenter when one next comes for laundry.{/n}
"So my map has a wrong bit," Aivu says.
"Your map has a bit that needs changing," Nessa replies. "Mine would have the old passage open. Yours will be better."
{n}You retrace the longer route with an empty bucket. Aivu counts your steps aloud until you lose count laughing. On the second attempt she keeps quiet, tapping a claw against the paper at each turn.{/n}
{n}She draws a cross over the blocked alley. Beside it she adds the crooked outline of the cart, so no one will mistake the mark for a closed shop.{/n}
"I don't like leaving it there," she says. "But I like knowing where it is. Someone else can decide about the cart. I'm deciding about the map."''',
        c('[Finish the longer route with her.]', flags=("aivu.shortcut_marked",))),
], requires=("aivu.the_roof_below",), delay=48)

s("someone_elses_turn", "Someone else's turn", '"Is your map ready for a traveler?"', [
    n("start", "Aivu", '''"Almost. I keep finding things that aren't on it. Do you think cities do that on purpose?"
{n}Aivu has brought a smooth stone to hold the paper down. Its underside is painted with a small blue arrow. She shows you the arrow before setting it in place.{/n}
"So we can turn the map the right way. That's better than writing 'this way' at the top. I tried that. Then I turned around."
{n}Nessa has agreed to try the map on an errand to the pump. Aivu will remain at the laundry gate with you. She objects to this arrangement until Nessa explains that a map requiring its author to fly overhead giving instructions is not much help to someone alone.{/n}
"I could be very quiet overhead."
"You could. Today you'll be quiet here."
{n}Aivu watches her take the paper. Suddenly she looks less certain of the whole undertaking.{/n}''',
        c('"Let her try it. We can hear what she found when she returns."', "format"),
        c('"She will bring it back. Take your time deciding."', abort=True)),
    n("format", "Aivu", '''{n}Nessa pauses with the map in her hands.{/n}''',
        c('[Show her how the two names share each place.]', "names", requires=("aivu.map_both_names",)),
        c('[Show her which side gives directions.]', "sides", requires=("aivu.map_two_sides",))),
    n("names", "Aivu", '''{n}Nessa locates her laundry, then reads its grander name with a snort.{/n}
"That is going to stick. I can tell."
"It's a good name," Aivu says hopefully.
"It is a very long name. Look here, though. Your sock has covered the turn into the lane."
{n}Aivu reaches toward the paper, then stops herself.{/n}
"I can move the sock when you come back. Can you find the turn anyway?"
"I can. You marked the pump clearly."
{n}Nessa sets off. Aivu waits until she is out of sight before drawing another sock in the dust, testing whether it can be made smaller without becoming a worm.{/n}''', c('[Wait beside Aivu.]', "jori")),
    n("sides", "Aivu", '''{n}Nessa turns the map over, following Aivu's instructions. She finds the laundry, then turns it back to admire the drawing.{/n}
"I've lost where I was."
"It's on the other side!"
"I know. But when I turn it, my left becomes my right. Could you put a little matching mark beside each place?"
{n}Aivu looks at you, then at the stone with its blue arrow.{/n}
"Yes. Different marks. A sock for here. A bucket for the pump. A... something else for the other things."
{n}Nessa sets off with the practical side uppermost. Aivu begins practicing small pictures in the dust. She has discovered a difficulty neither of you noticed when you already knew the way.{/n}''', c('[Wait beside Aivu.]', "jori")),
    n("jori", "Aivu", '''{n}Jori comes to the gate carrying a basket. He notices the drawings at Aivu's feet.{/n}''',
        c('[Give him room to approach.]', "space", requires=("aivu.jori_space",)),
        c('[Ask whether he recognizes the pictures.]', "talked", requires=("aivu.jori_talked",))),
    n("space", "Aivu", '''{n}Jori leaves the basket by the gate. He stays a few steps from Aivu, but points at the smallest drawing.{/n}
"Bucket?"
"Sock. A small sock."
"I'd make the heel stick out."
{n}She does. He nods.{/n}
"You waited at the gate today. Thank you."
{n}He returns to his work. Aivu's tail begins to move, stirring the dust beside her drawings.{/n}
"He looked at the map before he looked at my wings. Did you see?"
"I saw."
"Good. I wanted someone else to see, too."''', c('[Listen for Nessa returning.]', "route")),
    n("talked", "Aivu", '''"That's a sock," Jori says. "Unless you've found a very strange bucket."
"Everyone is very certain about buckets. Have you noticed?"
{n}He laughs and sets the basket down. She moves her tail so it will not strike his ankle.{/n}
"I told Nessa I can come with you next time you look at the roofs," he says. "From the street. Someone should tell you which ones leak."
"You want to come?"
"If you want another pair of eyes."
"Yes! But we aren't going on all of them. We're asking first."
"Good. I don't like heights."
{n}Aivu looks delighted to learn that someone else has a perfectly sensible objection to a place she finds easy.{/n}''', c('[Listen for Nessa returning.]', "route")),
    n("route", "Aivu", '''{n}Nessa returns with her bucket and the map tucked beneath her arm.{/n}''',
        c('"Did the cleared passage help?"', "open", requires=("aivu.shortcut_open",)),
        c('"Was the blocked passage clearly marked?"', "blocked", requires=("aivu.shortcut_marked",))),
    n("open", "Aivu", '''"It did. I took the short way out and the long way back, to see whether I could find both."
{n}Nessa puts the bucket down and returns the map. Aivu searches her face for signs of disaster.{/n}
"One thing. You marked the step, but from this direction the arrow points past it. I nearly trusted the arrow more than my own feet."
"Oh! We should fix that now."
{n}You make the correction together. Aivu insists on walking the passage once more, outside by her own route while you check the arrow from both ends. The map is useful; it still needs work. For once she seems pleased by both facts.{/n}''', c('[Return to the laundry gate.]', "keep")),
    n("blocked", "Aivu", '''"I saw the cart before I reached it. Your mark was clear. I took the long way."
"Did you mind?"
"I minded carrying the water. I didn't mind knowing where to carry it."
{n}Nessa returns the map. She has noticed one confusing arrow at the step. You correct it together, and Aivu makes you approach from both directions to check that neither traveler is sent sprawling.{/n}
"When the carpenter comes," Nessa adds, "I'll tell you if the cart moves."
"Then I'll come change it."
{n}Aivu says this with more confidence than she showed when promising to fix everything. She knows exactly which little cross she will have to rub out.{/n}''', c('[Sit beside the finished corrections.]', "keep")),
    n("keep", "Aivu", '''{n}Aivu rolls the map, then unrolls it again. The paper is softer at its creases now. There are fingerprints near the laundry and a water mark beside the pump.{/n}
"I thought it would look better when it was finished."
"Doesn't it?"
"It looks more used."
{n}She turns that over in her mind, then pushes the smooth arrow-stone toward you.{/n}
"You can keep this until next time. Then we'll have to meet to turn the city the right way up."
{n}Nessa would like to keep a copy by the laundry door for new workers. Aivu also wants the original for her own explorations. Copying it will take another afternoon, especially if every bird must be preserved.{/n}
"You don't have to come for the copying," she says. "I can ask Jori to help with the letters. But you can if you want. Or we can just look for somewhere new. Somewhere with a garden, perhaps."
{n}She has plans that continue when you leave. She still wants to know which of them you would like to share.{/n}''',
        c('"Let us make the laundry copy together. You can decide which birds it needs."', "copy"),
        c('"Keep the original for yourself. Next time, show me the garden in the cart."', "explore")),
    n("copy", "Aivu", '''"All the birds. Obviously. But some can be smaller."
{n}She touches the rolled paper with one claw, pleased to have settled the question without surrendering a single bird.{/n}
"I'll ask Nessa for another piece of paper. And Jori can tell us about the roofs while we draw. You can do the straight letters. Mine keep wanting to go somewhere."
{n}She nudges the arrow-stone against your hand.{/n}
"Don't lose it in your pocket with all the important things. It's an important thing, too."
{n}As you rise, she returns to the gate to ask Nessa about paper. This time she waits for an answer before entering.{/n}''',
        c('[Keep the stone safe for your next afternoon together.]', flags=("aivu.trusted", "aivu.laundry_copy", "aivu.opening_kept"))),
    n("explore", "Aivu", '''"Yes! I want to know whether they planted the garden before the wheel broke or afterwards. Those are two very different gardens."
{n}She nudges the arrow-stone against your hand.{/n}
"I'll ask Nessa if she can wait for a copy. It is my map. I want to take it somewhere before it has to stay by a door."
{n}Nessa agrees to wait. Aivu promises nothing about when the copy will be ready. Instead, she asks whether Jori knows who owns the garden cart. He does, and offers to introduce her.{/n}
{n}Before following him, she looks back at you.{/n}
"Bring the stone next time. If the city is upside down, we'll start by fixing that."''',
        c('[Wave her on, keeping the stone for your next exploration.]', flags=("aivu.trusted", "aivu.garden_next", "aivu.opening_kept"))),
], requires=("aivu.a_way_for_feet",), delay=48)
