"""Aivu's friendship campaign alongside the native Azata companion story.

The existing pet remains native-owned. No recruitment, cure or mythic conversion.
"""
from story_format import c, n, scene

SCENES = []
UNIT = "32a037e97c3d5c54b85da8f639616c57"
DREZEN = "2570015799edf594daf2f076f2f975d8"
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"
ANSWERS = "f1a65c6d838f58d49ad4ff40544b895b"
COMPLETED_QUESTS = {"aivu.native_rescue_complete": "1ad9b8fa1fe3cb84b932e8a889fc1897"}
SEEN_CUES = {"aivu.native_fear_told": ["9bbebfddf8861584d89b097263329352"]}
BLOCKERS = ("aivu.closed", "aivu.absent", "aivu.detached", "devil", "swarm", "true_lich", "legend", "dragon")


def s(id, title, entry, nodes, requires=(), forbids=(), chapters=(3, 5), area=DREZEN, delay=24):
    for node in nodes:
        node["Portrait"] = "Aivu" if node["Speaker"] in ("Aivu", "Narrator") else ""
    SCENES.append(scene("aivu." + id, title, "Aivu", min(chapters), entry, nodes,
        Relationship="aivu", Chapters=list(chapters), last=max(chapters), Areas=[area],
        AnswerLists=[ANSWERS], ContactUnit=UNIT, requires=("azata", *requires),
        forbids=(*BLOCKERS, *forbids), optional=True, delay=delay))


s("a_garden_that_can_go", "A garden that can go",
  '"I brought your arrow-stone. Which way are we turning the city today?"', [
    n("start", "Aivu", '''"Right way up first! We can try another way afterwards."
{n}Aivu is waiting beside the throne-room door, with her map rolled under one forepaw. She leans forward to inspect the stone as though you might have accidentally exchanged it for another city during your travels.{/n}
"The arrow's still blue. Good. I wondered if important stones changed color when you weren't looking. Important people change their clothes all the time."
{n}She has a thin stick tucked through the rolled paper. A new length of string keeps it from slipping out.{/n}
"Jori told me about the garden cart. Its owner is called Pella. She doesn't sell gardens. She sells things she grows in one. That's a terrible difference to find out after you've already asked how much the whole garden costs."
{n}Aivu moves toward the door, then stops.{/n}
"But we said something about the copy, didn't we? I remember what we said. I'm checking whether you remember."''',
      c('"We were going to make the laundry copy. Let us do that first."', "copy", requires=("aivu.laundry_copy",)),
      c('"We said the garden would come next. Has Nessa been able to wait?"', "garden", requires=("aivu.garden_next",)),
      c('"Keep the city upright until I can join you."', abort=True)),
    n("copy", "Aivu", '''{n}At the laundry gate, Nessa has saved a sheet large enough for the map. Jori brings the ink, then sets it on the far side of your elbow. He has learned something about tails since your last visit.{/n}
"All the birds," {n}Aivu reminds you.{/n}
"I remember."
"Even the bird that might be a leaf. We can't prove it wasn't a bird."
{n}You hold the new sheet against the original while Jori traces the places people need to find. Aivu redraws the fantastic buildings herself. It takes longer than copying their outlines would have taken. She notices this, complains that straight houses get an unfair advantage, and keeps drawing.{/n}
{n}Nessa hangs the finished copy beside her door, beneath a board that shelters the top from rain. There is still room to read her ordinary sign. Aivu steps back twice, examining the map from the height of a customer rather than from the air.{/n}
"That's mine," {n}she says.{/n} "Except people can use it when I'm somewhere else."
"That was the idea," {n}Nessa replies.{/n}
"I know. It's different when it's actually doing it."
{n}She rolls the original around its stick. Jori points down the lane toward Pella's garden cart.{/n}''', c('[Follow her to the cart.]', "pella")),
    n("garden", "Aivu", '''"Yes. She had lots of shirts to be cross with. She didn't need a map as well."
{n}At the laundry, Nessa says she can manage without the copy a little longer. She asks only that Aivu keep it out of the pump. Aivu objects that this happened to a corner, once, and the corner did not contain anything that needed to stay dry.{/n}
"A house," {n}Jori says.{/n}
"A drawing of a house. The people weren't in it."
{n}Jori gives you directions to Pella's cart. He is busy with the washing today, so the introduction consists of calling Pella's name very loudly down the lane and informing her that the dragon with the map is coming.{/n}
"There," {n}Aivu says.{/n} "Now she won't think the noise is a roof falling."
{n}She tucks the original map beneath a wing before starting out. The laundry copy remains a job for another afternoon; Nessa has not mistaken your visit for a promise to finish it today.{/n}''', c('[Walk down the lane with her.]', "pella")),
    n("pella", "Aivu", '''{n}The cart stands beneath a strip of clear sky between two houses. Its box is filled with soil, a few onions, and several herbs whose leaves tremble when Aivu sniffs them. One wheel is intact. The other rests beside the wall, its broken spokes neatly bundled inside its rim.{/n}
{n}Pella is an older woman with a crooked little knife and a hat that has been repaired in two different colors. She greets Aivu by lifting a hand before the dragon can put her nose into the soil.{/n}
{n}When Aivu asks to draw, Pella supplies a separate scrap for the garden. The original street map stays rolled beside it.{/n}
"Smell it from there. That one's sorrel."
"I wasn't going to eat it."
"Good. That one's for my supper."
"I might have been going to ask."
"Then I might have said no."
{n}Aivu looks intrigued by this tidy arrangement.{/n}
"Did the garden come before the wheel broke?"
"After. I couldn't move the cart, and I could grow something where it stood."
"So the broken bit made the garden!"
"The broken bit made extra work. I made the garden."
{n}Pella cuts a leaf, wipes it, and lets Aivu taste the end. The dragon's eyes narrow at its sharpness.{/n}
"That tastes like a green argument. I think I like it. I need another little argument to be sure."
{n}Pella gives her a second leaf. Aivu studies the empty axle socket.{/n}
"If we fixed the wheel, could the garden go places? It could follow the sunshine! Or visit other gardens and find out what they're doing."
"It could come with me when I move," {n}Pella says.{/n}
{n}That answer interrupts Aivu's list of gardens. Pella points to the shutter above you. The owner needs this space for a stack of timber before the next repairs begin. Pella has found another patch by a neighbor's shed, but the cart cannot reach it on one wheel.{/n}''',
      c('"We could help you move it. Where is the new place?"', "move"),
      c('"Aivu, would you rather draw the garden here before it goes?"', "draw")),
    n("move", "Aivu", '''"Both! We can draw where it is and where it goes. Then someone who finds the first garden can find the second."
{n}Pella shows you the way to the shed. It is a short journey, but the lane narrows at one corner. Aivu measures the cart with her forelegs, then measures the gap. Her first answer is that it will fit if the wall moves a little.{/n}
"The wall is occupied," {n}Pella says.{/n}
"Then we'll try the cart."
{n}You inspect the broken wheel together. The axle appears sound. A cartwright should be able to judge whether another wheel will fit, but Pella cannot pay for an entire new cart. Aivu offers to pull. Pella asks her to wait until there is something safe to pull.{/n}
{n}Before leaving, Aivu draws a little wheel beside the garden on the new page. She leaves the line to its new home unfinished.{/n}
"We'll ask about the wheel first. Then we'll know whether the line can go all the way."
{n}Pella wraps a small cutting in damp cloth for her. Aivu sniffs it with great concentration.{/n}
"For growing," {n}Pella says.{/n} "Not another argument."
"I can grow an argument. I'm very good at arguments."''',
      c('[Keep the cutting safe while Aivu carries the map.]', flags=("aivu.campaign_started", "aivu.garden_moving"))),
    n("draw", "Aivu", '''{n}Aivu considers the patch of sun on the herbs.{/n}
"Yes. If it goes, this will be the only garden that was here. We should have a picture of it."
{n}Pella brings out a stool for you. Aivu lies beside the cart, where she can see the plants at their own height. She draws the onions much larger than the other leaves. Pella says they are not the most important part; Aivu says they look as though they believe they are.{/n}
{n}While you work, Pella explains where the cart must go. There is a new patch by a neighbor's shed, a narrow corner on the way, and a broken wheel between her and the move. Aivu abandons one enormous onion to examine the axle.{/n}
"We can ask about that. I don't know how to fix it, but I know how to ask loudly."
"Ordinarily," {n}you remind her.{/n}
"I can ask ordinarily loudly."
{n}Pella gives her a cutting wrapped in damp cloth. Aivu leaves a space beside the old garden for a new drawing. The first garden is finished on the page; its journey has not begun.{/n}
"Can you hold this?" {n}she asks, passing you the cutting.{/n} "If I put it next to my mouth, I might forget which sort of present it is."
{n}She returns the knife Pella lent you for sharpening the drawing stick, blade first toward herself and handle toward its owner. Then she remembers the unfinished onion and makes it a little larger.{/n}''',
      c('[Take the cutting and leave the original garden on the map.]', flags=("aivu.campaign_started", "aivu.garden_drawn"))),
], requires=("aivu.someone_elses_turn", "aivu.opening_kept"), forbids=("aivu.campaign_started",))


s("a_late_garden", "A garden still to find",
  '"What would you like to do in Drezen when we have an afternoon free?"', [
    n("start", "Aivu", '''"Find something we haven't already looked at! It's a city. It must have something left."
{n}Aivu shakes out a piece of paper. The marks on it are notes, scraps of a street, a building that has acquired a face. They do not yet form a map you can follow.{/n}
"I was making a city from the sky. But when you land, people have doors in completely different places. And shops have names! Very small names. You can't read them when you're flying."
{n}She points to a drawing of a cart full of leaves.{/n}
"I found this. A woman is growing her garden in something that ought to go places, but it doesn't. I want to know why. Will you come? You can ask the door questions."
{n}You find the cart in a narrow lane. Its owner, Pella, is cutting sorrel with a little crooked knife. Aivu introduces herself before sniffing the plants, then asks whether the garden grew before the wheel broke or afterwards.{/n}
"After," {n}Pella says.{/n} "I couldn't move the cart, so I grew something where it stood. Now I need to move it again."
{n}A pile of timber is due to take its place. Pella has a new patch by a neighbor's shed, but one wheel is broken. Its spokes lie bundled within the rim beside the wall.{/n}
"We can look at that," {n}Aivu says.{/n} "Looking is the first part of lots of things I'm good at. Sometimes the second part is biting, but probably not this time."''',
      c('"Let us look at the route to the shed first."', "route"),
      c('"Would you like a drawing before the garden moves?"', "picture"),
      c('"Keep the idea. I must return to something else."', abort=True)),
    n("route", "Aivu", '''{n}Pella shows you the way. The cart must turn through a narrow corner, pass beneath a washing line, and stop beside the neighbor's shed. Aivu examines the washing line as though it were a particularly devious enemy.{/n}
"We should tell whoever owns that before we come through. I can see something embarrassing happening. It might be me."
{n}Back at the garden, you inspect the axle. Neither of you pretends to be a cartwright. Pella knows a man who repairs wheels, but she is worried that he will tell her to replace the whole cart. She cannot afford that.{/n}
"Then we'll ask what this cart needs," {n}Aivu says.{/n} "It already knows how to be a garden. A new one would have to learn."
{n}Pella gives her a cutting wrapped in damp cloth. You carry it while Aivu draws two patches on her paper, leaving the line between them unfinished.{/n}
"There. Now we have something to do besides walking through Drezen looking important. We can walk through it looking for a wheel."
{n}She glances back at you.{/n}
"And we can still look important if we find one. I'll carry it very grandly."''',
      c('[Keep the cutting safe for the next visit.]', flags=("aivu.started", "aivu.campaign_started", "aivu.garden_moving", "aivu.late_garden_started"))),
    n("picture", "Aivu", '''"Yes! Before the onions start pretending they always lived at the new place."
{n}Pella lends you a stool. Aivu settles beside the cart and begins with the plants that look most opinionated. Soon the onions loom over everything. Pella objects; Aivu adds a tiny crown to the largest and says the matter has already been decided.{/n}
{n}While you draw, Pella explains the journey to the shed and the narrow turn along the way. The axle seems sound, but the broken wheel needs a cartwright. Aivu asks his name, then writes it below the garden as though he were another landmark.{/n}
"If we put people on the map, it will have to change when they go for their supper," {n}she says.{/n} "Perhaps just the places where they usually are. People are very bad at standing still."
{n}Pella gives her a cutting wrapped in damp cloth. Aivu asks you to carry it, having already discovered how difficult it is to hold a drawing stick and something edible at once.{/n}
"For growing," {n}Pella tells her.{/n}
"I know! That's why I'm giving it to somebody who isn't thinking about eating it."
{n}She leaves a blank patch beside the drawing. It is large enough for a second garden.{/n}''',
      c('[Take the cutting and help her roll the picture.]', flags=("aivu.started", "aivu.campaign_started", "aivu.garden_drawn", "aivu.late_garden_started"))),
], chapters=(5,), delay=0, forbids=("aivu.campaign_started", "aivu.opening_kept"))


s("the_wheel_with_no_cart", "The wheel with no cart",
  '"Shall we ask the cartwright about Pella\'s garden?"', [
    n("start", "Aivu", '''"Yes. I put the cutting in a pot, so it can't fall out of the garden while we're away. It has one new leaf. I told Pella and she said that was what leaves do. She could have sounded more surprised."
{n}Aivu meets you at the throne-room door. Together you visit Pella, who shows you the cartwright's chalk marks on her axle. He visits while you are there, measures the axle, and asks you to examine two spare wheels at his shed.{/n}
{n}The cartwright, Torren, is shaving a wooden peg when you arrive. He has set out a small wheel with fresh spokes and a larger one darkened by weather. The smaller would hold the cart crooked. The larger appears the right size, but a line crosses its hub.{/n}
"That's either a split or an old mark," {n}Torren says.{/n} "I want a better look at the inside before anybody pulls a cart full of soil on it."
"It's full of garden," {n}Aivu corrects him.{/n}
"That weighs much the same."
"It sounds heavier when you say soil."
{n}Torren offers to open the hub for inspection. That will take most of the afternoon. Aivu looks at the narrow stripe of sunlight outside, calculating how much of her grand moving day it will consume.{/n}
"Can we tell without taking it apart? You find all sorts of tiny things. Sometimes I don't even know they were there until you're telling everyone what they mean."
{n}The line near the hub continues beneath a rim of dried grease. You could examine it yourself, or leave Torren to open the wheel while you and Aivu help Pella carry the loose pots ahead.{/n}''',
      c('[Inspect the hub before deciding whether the wheel is sound.]', check=dict(Skill="SkillPerception", DC=25, CommanderOnly=True, Success="found", Failure="missed")),
      c('"Let Torren inspect it properly. We can carry the loose pots meanwhile."', "expert"),
      c('"We should leave this for a day when we can finish it."', abort=True)),
    n("found", "Aivu", '''{n}The mark is old. Beneath it, however, a pale splinter catches against the inner ring. You turn the wheel until the light falls through the center and find the real crack, running from the axle hole toward one spoke.{/n}
"There," {n}you say.{/n} "It opens under pressure."
{n}Torren examines it and nods. The hub cannot safely take Pella's cart, but the rim and most of the spokes can be reused. He has a sound hub from another repair. Knowing what is wrong saves him dismantling the wrong part first.{/n}
"Come back before supper. I'll have it ready."
"Today?" {n}Aivu asks.{/n}
"Today. If you let me work."
"We can do that. We can do that somewhere else."
{n}Outside, she turns back once to look at the rejected hub.{/n}
"It looked like the best wheel. It's annoying when things hide the part you ought to notice."
{n}You help Pella carry her loose pots ahead. By late afternoon Torren arrives with the repaired wheel. There is still enough light for the move, and Pella offers to show Aivu how to settle the cutting into a deeper pot afterwards.{/n}''',
      c('[Stay for the wheel fitting and the lesson with the cutting.]', "early")),
    n("missed", "Aivu", '''{n}You clean away the grease and find no obvious widening of the line. When Torren tests the wheel under his own weight, however, a different crack opens inside the axle hole.{/n}
"There it is. Easy to miss from that side."
{n}Aivu peers over your shoulder, then withdraws when Torren lifts the wheel onto his bench.{/n}
"So we don't know enough yet."
"I know enough to change the hub," {n}he says.{/n} "But I've a customer's repair promised first. You'll have it tomorrow."
{n}Aivu's tail drops. She had been waiting for him to say that knowing the answer would make the work disappear.{/n}
"The garden's still going," {n}you tell her.{/n}
"I know. Tomorrow is just such a long word when it was meant to be today."
{n}Pella is disappointed too. She uses the extra time to carry the loose pots ahead and asks whether you can help. Aivu takes the largest pot she can carry safely. She announces that this part of the garden has started moving and the rest will have to catch up.{/n}
{n}By the time the new hub is ready on the following afternoon, Pella's neighbor has begun stacking timber beside the old patch. You arrange a later space to turn the cart. Pella has no time left for the potting lesson she hoped to give; she shows Aivu where to put the cutting's pot and promises to look at it another day.{/n}''',
      c('[Help clear the later turning space.]', "late")),
    n("expert", "Aivu", '''"All right. But I want to see what was inside when he knows. It would be rude of the wheel to keep it a secret after all this."
{n}Torren takes it apart while you and Aivu carry the loose pots. Pella has a surprising number of them tucked beneath the cart. Aivu counts each one and begins giving them ranks. The pot with the drooping stem becomes Captain, since it already seems exhausted by responsibility.{/n}
{n}When you return, Torren shows you the split hub. The outer mark was harmless; the crack was inside. He has fitted another hub and is tightening the last spoke.{/n}
"So you had to break the wheel to fix the wheel," {n}Aivu says.{/n}
"Take it apart."
"I like my version better."
{n}He finishes before evening, but the time carrying pots has used up Pella's spare daylight. There will be no lesson with the cutting today. Instead she leaves Aivu a spare deep pot and tells her to bring it back when they can work together.{/n}
"That's an appointment," {n}Aivu tells you as you walk back.{/n} "I've got an appointment. I hope it doesn't make me boring."
{n}She tries walking like someone with an appointment, chin high and tail very still. It lasts until the tail catches a fallen leaf.{/n}''',
      c('[Carry the repaired wheel to the cart.]', "steady")),
    n("early", "Aivu", '''{n}Torren fits the wheel. With the cart supported, Pella lets Aivu scoop fresh soil into the cutting's deeper pot. You hold the pot steady while she tries to stop exactly at the mark. The first scoop goes over. Pella shows her how to scrape it back with the flat of a claw.{/n}
"Leave room for the water."
"I thought the water went in the spaces."
"It does. First it needs somewhere to sit while it finds them."
{n}Aivu studies the dark soil after the first watering. The plant is small enough that she can watch every leaf without moving her head.{/n}
"I'm going to draw this one properly," {n}she says.{/n} "It hasn't decided to be an onion yet."
{n}Pella keeps the newly potted cutting overnight. Tomorrow's first job will be moving the cart, with its repaired wheel already in place.{/n}''',
      c('[Agree to meet when Pella is ready to move.]', flags=("aivu.wheel_ready", "aivu.wheel_found", "aivu.cutting_potted"))),
    n("late", "Aivu", '''{n}The wheel fits. The cart stands level for the first time since Pella planted it, and a little loose soil falls through a gap in the boards.{/n}
"It's waking up," {n}Aivu says.{/n}
"It's leaking," {n}Pella replies, pushing a rag into the gap.{/n}
"It could be doing both."
{n}The new turning space is awkward, but usable. You leave the route clear for the move. Aivu takes her cutting back to its original pot, where it will stay until Pella can teach her to move it.{/n}
"The little garden has to wait for the big garden," {n}she says.{/n} "I suppose that's fair. The big one was here first."
{n}She does not sound delighted by fairness. She does bring the empty deeper pot Pella lends her, carrying it carefully between her forepaws for the short walk to the gate.{/n}''',
      c('[Make a new meeting time for the delayed move.]', flags=("aivu.wheel_ready", "aivu.wheel_missed"))),
    n("steady", "Aivu", '''{n}Torren fits the wheel and shows Pella where to put grease before the move. Aivu asks whether you could grease a dragon to make it faster. Torren says he has never accepted such a commission.{/n}
"Would you?"
"No."
"I was only finding out."
{n}The cart stands level. Pella checks the narrow corner once more and leaves the handles propped up, ready for the next visit. Aivu draws a wheel beside the new patch on her paper. She has not drawn the connecting line yet.{/n}
"It can go now," {n}she says.{/n} "Next time we make it actually go. Those are different exciting things."
{n}She carries the spare pot back for her future appointment, holding it far enough from her mouth that the leaves cannot tempt her before there are any leaves in it.{/n}''',
      c('[Return with her, leaving the fitted cart ready.]', flags=("aivu.wheel_ready", "aivu.wheel_expert"))),
], requires=("aivu.campaign_started",), delay=48)


s("the_garden_procession", "The garden procession",
  '"Pella is ready. Shall we help the garden change its address?"', [
    n("start", "Aivu", '''"I've thought of a name for it! The Garden That Went Looking for Better Sunshine."
{n}Aivu meets you with a strip of cloth painted green. She has not fastened it to anything yet. The letters are large enough to be read from the other end of the lane, if the reader has time to wait for all of them.{/n}
"Pella said I could put a name on it as long as it came off afterwards. I asked. Before painting. That was difficult because I had already thought of the painting."
{n}At the cart, Pella is tying the tallest stalks to short stakes so they will not break on the journey. She lets Aivu fasten the cloth between the handles. You take the handles while the dragon waits beside the sound wheel, ready to push where Pella directs.{/n}
"There's one thing," {n}Pella says.{/n} "No flying it. I want the onions to arrive in the cart."
"I wasn't going to fly it. I was going to announce it."
{n}The first few yards go well. The cart rolls. Aivu declares that the garden is under way. Two people stop to watch, and a boy runs ahead to tell someone else. Soon there are enough spectators to make the narrow turn considerably narrower.{/n}
"I didn't ask them to stand in the road," {n}Aivu whispers.{/n}
"You did make it sound like something to stand in the road for."
"I was right, though. Look at it!"
{n}Pella rests a hand on the cart's side. She is smiling, but the handles are beginning to weigh on your arms. The cart needs room to turn.{/n}''',
      c('"Aivu, make a procession. Put the spectators ahead of us, where they can lead the way."', "procession"),
      c('"Let us stop the announcements until we reach the shed. Pella needs the lane clear."', "quiet")),
    n("procession", "Aivu", '''"An escort! Yes! You there, with the very good hat. You can be in front."
{n}The man with the hat turns to see whom she means. Aivu points at him with great ceremony. He bows to Pella, then walks ahead, asking the spectators to follow him instead of the cart.{/n}
{n}It is not a grand parade. There are six people, one child who keeps running backwards until a woman catches his shoulder, and an onion flower trembling above the green sign. Aivu supplies a marching tune. She has remembered two lines and fills the rest with descriptions of vegetables.{/n}
"That part didn't rhyme," {n}you tell her.{/n}
"It will when we find the right vegetable. Keep going!"
{n}At the turn, the man in the hat holds back the others while you swing the handles. Aivu pushes against the sound side. Pella guides the wheel past the wall, with inches to spare. Then the procession carries on to the shed.{/n}
{n}The spectators applaud when the cart stops. Pella laughs in surprise and takes off her patched hat. Aivu looks pleased enough to burst.{/n}
"It got here with a song! That must help the growing."
"Sun and water will do," {n}Pella says.{/n} "But I liked the song."
{n}The man in the hat asks whether she sells the herbs. She does, once they have recovered from their journey. He promises to return. Aivu immediately wants to draw him on the map, but Pella tells her his name and address are enough for today.{/n}''', c('[Help settle the cart in its new patch.]', "procession_settle")),
    n("quiet", "Aivu", '''"But it was going very well."
{n}Pella looks down the crowded lane, then at the handles in your hands.{/n}
"For everyone except the garden."
{n}Aivu's mouth opens. She closes it, takes a breath, and addresses the nearest spectators at a much smaller volume.{/n}
"We need to get through. You can look at it when it's stopped. It's going to be a garden there for quite a while."
{n}The boy asks whether she is going to carry the whole cart. Aivu admits that she is not. He looks disappointed. She looks offended by his disappointment, but steps aside while the woman leads him out of the way.{/n}
{n}At the corner, Pella directs you to lower the handles. Aivu pushes only when asked. The wheel clears the wall. Without an audience asking what happens next, the last stretch is almost easy.{/n}
{n}Beside the shed, Pella removes her hat and wipes her forehead. She offers you both a place in the shade. Aivu sits with her chin on her forepaws.{/n}
"It was a very good sign," {n}she says.{/n}
"It still is," {n}Pella replies.{/n} "I could see it the whole way."
"I wanted everyone to see it."
"I wanted my garden here. Now it is."
{n}Aivu raises her head to inspect the patch of sun falling across the leaves. After a while she admits that the onions seem pleased. She keeps the sign on until Pella asks for help taking it down.{/n}''', c('[Help settle the cart in its new patch.]', "quiet_settle")),
    n("procession_settle", "Aivu", '''{n}You wedge the wheels so the cart cannot roll. Aivu helps untie the stakes. She saves the green sign, folding it carefully enough that the letters can still be read when it opens.{/n}
"We should have another procession. For something that doesn't mind stopping in the road."
"Such as?"
"I'll think of something. That's the part I'm good at."
{n}Pella asks for a drawing showing where the garden is now. Aivu unrolls her paper and puts the shed in the right place. The line from the old patch finally reaches the new one.{/n}
"There. It moved on the map too. That part was much easier."
{n}The new customer returns with a small cloth bag for herbs. He and Pella talk while Aivu adds the washing line to her drawing. She has found a use for a procession that she had not planned, and wants to know whether you noticed.{/n}''',
      c('"I noticed. He found Pella because you made him curious."', flags=("aivu.garden_arrived", "aivu.garden_procession"))),
    n("quiet_settle", "Aivu", '''{n}You wedge the wheels. Aivu helps untie the stakes, then folds the green sign along a blank space between two words. She wants to keep it for a procession that can stop whenever it likes.{/n}
"Something with feet," {n}she decides.{/n} "Feet can get out of the road more easily than gardens. Usually."
{n}Pella brings a jug of water. While you share the shade, Aivu draws the shed and finishes the line from the old patch. She asks whether the garden can still keep its enormous name even though fewer people heard it.{/n}
"It can," {n}Pella says.{/n} "I'll know what you mean."
{n}Aivu adds the first few words beside the cart and runs out of room. The remaining words climb up the side of the shed. Pella watches them grow with a resigned smile.{/n}
"You'll have to read it to me."
"I can do that. Quietly. Except the best bits."
{n}She reads the whole name, every word of it apparently one of the best bits.{/n}''',
      c('[Stay in the shade until she has finished the drawing.]', flags=("aivu.garden_arrived", "aivu.garden_quiet"))),
], requires=("aivu.wheel_ready",))


s("the_most_important_tail", "The most important tail",
  '"Have you found something with feet for your next procession?"', [
    n("start", "Aivu", '''"Something better. An absolutely terrifying creature. You."
{n}Aivu brings you a loop of soft rope with strips of cloth tied along its length. It has no metal hooks, teeth, or immediately visible intention to explode. She seems faintly disappointed by your relief.{/n}
"It's a tail. For a game. I've got one already, but you might need an extra."
{n}She has chosen a clear patch beside an unused wall. Three chalk circles mark different places on the ground. A rolled cloth lies in the nearest. Aivu calls it the royal turnip.{/n}
"You have to take it from one castle to another without the dreadful creature stealing your tail. If the dreadful creature gets the tail, you become dreadful and I get to run. No grabbing people, just the loose end. I practiced with a post, but it was very bad at running."
{n}She shows you how the rope will lie through a belt or sash and slip free when pulled, rather than dragging its wearer. If you would rather carry it, that works too. Aivu has provided a second rope for herself, since her actual tail is emphatically not part of the rules.{/n}
"I only have one real one. Even if I do want a different end sometimes."
{n}She drops the royal turnip into your hands with considerable dignity.{/n}''',
      c('"I will be the courier first. Show me how dreadful you are."', "courier"),
      c('"You carry the turnip. I want to practice my dreadful speech."', "dreadful"),
      c('"Save the turnip. I cannot play today."', abort=True)),
    n("courier", "Aivu", '''{n}You choose how to carry the loose tail and step into the first chalk circle. Aivu crouches beyond it, leaving you room to leave on either side.{/n}
"I am the dreadful dragon of... of vegetables! No, wait. You're holding the vegetable. I am the dreadful dragon who has no vegetables and is very cross about it."
{n}You make a dash for the second circle. She lunges for the rope and catches empty air. The next attempt is closer. By the third, you have discovered that she watches your shoulders before your feet.{/n}
{n}You feint left. Aivu turns, realizes what happened, and makes a noise of magnificent outrage. You reach the circle with the turnip intact.{/n}
"That was sneaky! Do it again. I want to catch it."
{n}The next run ends with your rope in her mouth. She drops it at once and declares the turnip successfully imperiled. Then she asks whether you would rather change places or keep trying to fool her.{/n}
"I can do one more," {n}you say.{/n}
"One more ordinary one, or the one where one more means lots more?"
{n}She is pleased when you give her an exact answer. She is less pleased when you fool her again, and delighted when she catches the trick on the following turn.{/n}''', c('[Sit by the wall after the last agreed round.]', "rest")),
    n("dreadful", "Aivu", '''{n}Aivu takes the rolled cloth carefully in her mouth, then sets it down so she can object to your first dreadful speech.{/n}
"Too many long words. The turnip will have reached the castle before you've finished being horrible."
{n}You shorten it. She considers the revision, then suggests a noise at the end. The noise startles a pigeon. Aivu approves.{/n}
{n}She begins her run without flying. At first you can hardly follow the rope trailing from the loose sash around her middle. Then she stops to make a face, and you seize the end while she is busy being impressive.{/n}
"That shouldn't count!"
"Why?"
"Because I was doing a different excellent thing."
{n}You hold up the rope. Aivu studies it, then admits that the turnip was not being guarded by her excellent face. She takes your place and demands the chance to steal your tail while you make a speech.{/n}
{n}The second speech is very short. She catches the rope anyway. By the time you stop, the royal turnip has been rescued and imperiled so often that one cloth end has begun to unravel.{/n}
"It needs a holiday," {n}Aivu says, setting it in the shade.{/n} "From royalty."''', c('[Sit by the wall after the last agreed round.]', "rest")),
    n("rest", "Aivu", '''{n}The stones beside the wall are warm. Aivu lies down with both false tails folded in front of her. Her real tail keeps moving as though it has not accepted that the game is over.{/n}
"What games did you play before you were important?"
{n}She asks it casually, but looks straight at you after asking.{/n}
"People tell me about places you conquered and things you killed. I know you do those. I was there for some of them. I want something I wasn't there for."
{n}She rolls the turnip beneath one forepaw.{/n}
"Unless you were always important. That would have been exhausting. Especially when you were asleep."''',
      c('"I liked games where I could make up the story. Winning mattered less."', "story"),
      c('"I wanted to win. I was sometimes a poor loser."', "winning"),
      c('"I did not have much chance to play. I am enjoying learning now."', "learning")),
    n("story", "Aivu", '''"Yes! Except sometimes the other people change the story when it's finally getting good. Then you have to explain why your version has better monsters."
{n}You tell her about a story you used to make up, choosing how much to share. She wants to know where you put the secret entrance, what happened to the person who found it, and whether the monster was allowed to change sides.{/n}
"It could be lonely being the monster all the time," {n}she says.{/n} "Unless the monster liked it. I'd like it for a bit."
{n}She makes you describe one small place in the imagined world. Then she supplies an absurd detail of her own and watches to see whether you will let it stay. When you do, her ears lift.{/n}
"There. Now I know a place you were before. Even if it wasn't anywhere."
{n}She hands you the royal turnip and keeps the false tails. Next time, she says, you should each invent a castle. Hers will have a kitchen that attacks intruders with biscuits. She has not yet decided whether this would deter anybody.{/n}''',
      c('[Keep the cloth turnip until the next game.]', flags=("aivu.game_shared", "aivu.commander_story"))),
    n("winning", "Aivu", '''"Me too. I like winning. Losing is very educational, which is how you know it's probably awful."
{n}You admit to a small, undignified defeat. She listens with open delight, then tries to hide it when you describe how miserable you felt. The attempt is unsuccessful.{/n}
"I'm not laughing at the miserable part. I'm laughing at the thing you said. Did you really say that?"
{n}You did, or something close enough. Aivu puts a forepaw over her mouth. When she can speak again, she asks whether you ever played with those people afterwards.{/n}
{n}You give the answer that belongs to your memory. She listens, then nudges one false tail toward you.{/n}
"If I say something very stupid because you win, you can tell me. I might still be cross first. But you can tell me."
{n}She picks the rope up again before you can mistake it for a permanent gift. The turnip is your responsibility until next time, she says. A monarch should not be left lying in the street after an embarrassing defeat.{/n}''',
      c('[Take the turnip, promising it no easy victories.]', flags=("aivu.game_shared", "aivu.commander_competitive"))),
    n("learning", "Aivu", '''{n}Aivu stops rolling the turnip.{/n}
"Oh."
{n}For a moment she seems ready to ask every question at once. Then she looks at the chalk circles instead.{/n}
"This is a good one to start with. It has a turnip, so it can't be too serious. Even when somebody is dreadful."
{n}You tell her what you liked about the game. She asks what made it difficult, then shifts one circle a little farther from the wall so there is more room to turn.{/n}
"That isn't making it easy," {n}she says.{/n} "That's making it better. I wanted more room too."
{n}She draws a little crown over the new circle. The chalk snaps. She gives you half, as though the chalk itself has suggested how to share the next part.{/n}
"We can make another one up. If you don't know the rules yet, nobody can tell you they're wrong."
{n}She puts the turnip in your care and keeps the two false tails. Before leaving, she looks back at the patch of ground where your half of the chalk has made a crooked little flag.{/n}
"That can be your castle. I'll try to steal something from it next time."''',
      c('[Keep the turnip and your half of the chalk.]', flags=("aivu.game_shared", "aivu.commander_learning"))),
], requires=("aivu.garden_arrived",))


s("a_very_important_guest", "A very important guest",
  '"What have you planned for our next game?"', [
    n("start", "Aivu", '''"A visitor! Not today. Soon. Maybe. I've asked someone."
{n}Aivu's false tails lie beside her, neatly coiled. She has also brought three cloth scraps, a wooden spoon, and the green sign from the garden cart. The sign now has a dragon drawn above its enormous name.{/n}
"Pella knows a man who plays a little drum. He said he could come when he brings her another bag of soil. Then we could have a game with a proper beginning, and a song, and people could come who don't know how to play yet."
{n}She spreads the scraps before you. One has become a flag. Another seems to be an extremely ambitious hat.{/n}
"I thought everyone could be the dreadful creature for a bit. Except me. I'll explain things, and sing, and show them the rules, and make sure nobody grabs a real tail, and tell them when to stop."
{n}She lifts her head proudly.{/n}
"They'll need me for all of it."
{n}You look at the two coiled tails. She follows your glance.{/n}
"I'll play afterwards. There might be time. There usually is if people hurry."''',
      c('"Which part do you actually want to do most?"', "want"),
      c('"Give me one of those jobs. I would like a turn too."', "job"),
      c('"We should plan this when I can stay."', abort=True)),
    n("want", "Aivu", '''"All of it."
{n}You wait. She picks up the wooden spoon, puts it down, and nudges a false tail with one claw.{/n}
"The first bit. When everyone sees it and knows I made it. And then the playing."
"Those sound like two good parts."
"But if someone else explains it badly, they'll think my game is boring. Or they'll have fun without knowing I thought of it."
{n}She says the last part quickly and watches to see whether you will laugh. When you do not, she tries explaining it again.{/n}
"I don't mind them having fun. Obviously I don't. I just want to be in the fun I made."
{n}You offer to explain the running game while she gives it a magnificent opening. The drum player can choose his own song. Pella can say where the cart and pots are not to be touched. Aivu looks at the shrinking pile of her responsibilities with suspicion.{/n}
"What if I want to help anyway?"
"Then help. You can still let us do what we agreed to do."
{n}She gives you the spoon. It is apparently the signal that a round has ended. She has not yet found anything suitable to hit with it.{/n}''', c('[Try a short practice introduction together.]', "practice")),
    n("job", "Aivu", '''"You want a job? On your afternoon off?"
"I want one of these jobs. There is a difference."
{n}She considers that, then offers you the wooden spoon. When you ask what it does, she says you will make a noise with it when a round is over. She had planned to hit a bucket, until Nessa pointed out that buckets were already doing several useful things.{/n}
"We can clap," {n}you suggest.{/n}
"That's less grand."
"It's harder to lose."
{n}Aivu claps her forepaws once. The sound is very different from yours, which makes her want to try again. Soon you are testing signals: two claps for a start, one long call for a stop, a thoroughly undignified noise for a royal turnip emergency.{/n}
"I could do the introduction," {n}she says,{/n} "and then play. You'd tell the people who came late."
"I could."
"And if I go to see what the drummer is doing, you won't decide the game is over because the important dragon went away."
{n}You agree. She lays the spoon aside and begins composing her introduction aloud.{/n}''', c('[Try a short practice introduction together.]', "practice")),
    n("practice", "Aivu", '''{n}Aivu rises onto a low, broad step. Her wings spread just far enough to make a fine shadow on the wall.{/n}
"People of the... of this bit of Drezen! Prepare to face something beyond your most terrible..."
{n}She stops.{/n}
"That sounds like demons. I don't want it to sound like demons."
{n}She tries again, this time announcing a tournament in defense of the royal turnip. The turnip, currently in your keeping, will attend in person. There will be no speeches from actual royalty unless somebody has brought another vegetable.{/n}
{n}You clap twice. She jumps down and makes a dash for the chalk circle. Then she stops again, laughing.{/n}
"I forgot I wasn't meant to explain it. That's your bit. Do your bit!"
{n}You explain the game to an imaginary latecomer. Aivu plays the latecomer with such a talent for misunderstanding that you have to demonstrate every rule. By the time you finish, both of you have a better idea of what a real newcomer will need.{/n}
{n}Pella passes on her way from the shed. She listens to Aivu's plan and agrees to let the game begin near the garden, provided it moves to the clear patch for running. The drummer, Berrit, will come in two days if his delivery reaches Drezen on time.{/n}
"If it doesn't," {n}Aivu says,{/n} "we can still clap. We've practiced."''',
      c('"Let us invite people to join a game, with the music as a welcome extra."', "open"),
      c('"Keep the first gathering small. We can invite more people after we have tried it."', "small")),
    n("open", "Aivu", '''"I can do that. The game will definitely be there. I'll be there. The turnip will be there. Three very reliable things."
{n}You walk the lane together, telling people where the game will begin and how long you mean to stay. Some want to come. Others are working. Aivu makes a face when one man says he is too old for such nonsense, then asks whether he is old enough to cheer from his door. He says he might be.{/n}
{n}By the time you return, she has a list of names written along the blank back of her sign. She reads them aloud twice, pleased by how different they sound together.{/n}
"We won't make them all play the same way," {n}she decides.{/n} "Some can be dreadful sitting down. That man would be very good at it."
{n}She asks you to bring the turnip and the chalk. She will bring the tails, the flags, and her extremely important self. Then she picks up the wooden spoon after all. Someone might turn up with a bucket they are not using.{/n}''',
      c('[Keep the afternoon for the neighborhood game.]', flags=("aivu.game_invited", "aivu.game_open"))),
    n("small", "Aivu", '''"A secret beginning. Not a secret from everyone. Just from everyone who isn't coming."
{n}You invite Pella, Berrit if he arrives, and a few people who have already stopped to ask about the chalk circles. Aivu insists that anyone passing may watch. She does not want to spend her first game turning away somebody who looks lonely.{/n}
"Watching isn't the same as promising them all a turn before supper," {n}she says, testing the distinction aloud.{/n}
{n}You agree. She shortens her introduction by almost half, then adds a new title to herself and loses most of the time she saved. Pella says she can listen while she waters the garden.{/n}
{n}Before you leave, Aivu lays the two false tails side by side.{/n}
"We'll actually get to play," {n}she says.{/n} "I nearly forgot that part. It's a funny part to forget when it's the whole reason."
{n}She asks you to bring the turnip and the chalk. The first gathering will have room to change its mind if something does not work, which she finds reassuring until she notices how much it sounds like practice.{/n}''',
      c('[Keep the afternoon for a first gathering.]', flags=("aivu.game_invited", "aivu.game_small"))),
], requires=("aivu.game_shared",), delay=48)


s("when_the_drum_does_not_come", "When the drum does not come",
  '"I have the turnip and the chalk. Is everyone ready?"', [
    n("start", "Aivu", '''"Almost. Almost is being very stubborn."
{n}Aivu has fastened the flags low enough that nobody needs to climb to reach them. The false tails lie beside your chalk circles. Pella brings word from the delivery gate: Berrit's cart broke a shaft on the road. He is safe, but he will not arrive today.{/n}
"I knew he might not," {n}Aivu says.{/n} "We said he might not."
{n}She looks at the wooden spoon.{/n}
"I still wanted the drum."
{n}The first guests arrive while she is staring at it. Pella begins watering her plants. A woman with a bandaged wrist asks whether she can take a turn without running. Aivu starts to answer, then remembers that you agreed to explain the game.{/n}
"Ask the Commander. I have to... I have an introduction."
{n}She climbs the low step. Her opening is loud, splendid, and interrupted halfway through by a boy asking whether the royal turnip can be eaten. Aivu tells him that consuming the monarch would be a different game, with much more serious rules.{/n}
{n}The first round begins. Without the drum, there is no music to fill the pauses while people change places. Aivu supplies some herself. Then she tries to explain a rule you have already explained. Then she rushes to fetch a tail somebody has dropped. By the time it is her turn, she is too busy to notice.{/n}''',
      c('"Aivu. Your castle needs you. I can manage the next round."', "play"),
      c('"Take a pause with me. Let Pella announce a quiet round while we sit."', "pause")),
    n("play", "Aivu", '''"But she's holding the tail too tightly."
"I can show her."
"And he keeps starting before the claps."
"I can tell him."
{n}Aivu looks between the two participants, then at the chalk circle waiting for her.{/n}
"All right. But if something goes wrong, call me."
{n}You do not have to call. The woman loosens her grip. The boy waits. Aivu takes the turnip and faces a man whose stiff knee confines him to the nearest circle. He can steal a tail only if the courier comes within reach.{/n}
{n}Aivu could keep well away from him. Instead she edges closer, making a magnificently foolish face. His hand snaps out and pulls the loose rope clear. She darts back too late, shrieking with laughter, and nearly drops the turnip herself.{/n}
"He tricked me! He pretended to be slower!"
"I am slower," {n}the man says.{/n} "You were showing off."
{n}She demands another round. This time she makes the face from farther away. The spectators laugh, and Aivu forgets to supply the missing music.{/n}
{n}When her turn ends, she returns to you breathing hard and looking much more like someone at her own game.{/n}''', c('[Give her a place beside you for the next round.]', "after")),
    n("pause", "Aivu", '''"They'll think I've gone away."
"We will be sitting where they can see us."
{n}Pella claps for a change of round and announces that the turnip is taking a short holiday. The next players must pass a rolled cloth between the circles while inventing its increasingly ridiculous title. Running is optional. Forgetting a title is almost inevitable.{/n}
{n}You sit beside Aivu on the low step. She tries to correct the first title, stops, and watches two players argue cheerfully about whether a vegetable can be both Admiral and Moon.{/n}
"That's not my game," {n}she whispers.{/n}
"Do you want it to stop?"
{n}She considers the question seriously. Then somebody announces the Admiral Moon of All Turnips, and she snorts.{/n}
"No. But mine was good too."
"It was. We can play it again after this round."
{n}She leans forward as the bandaged woman supplies the next title. Soon Aivu is trying to remember the whole list along with everyone else. When it reaches Pella, the gardener forgets the second word and blames the onions for distracting her.{/n}
{n}Aivu laughs so hard she has to begin her own turn twice. Afterwards she asks to carry the turnip through a running round. This time she leaves you to explain the rules. She faces the man with the stiff knee, ventures too close while making a face, and loses her loose tail to his quick hand. Her indignant demand for another round makes him laugh.{/n}''', c('[Keep the place beside you free when she returns.]', "after")),
    n("after", "Aivu", '''{n}The agreed end arrives before everyone has had enough. You clap the final signal. Aivu looks at the sky, then at the guests, plainly tempted to declare that the sun has made a mistake.{/n}
{n}Pella needs to go. The woman with the bandaged wrist is tired. They thank Aivu as they leave, each for something different. The woman liked being able to join without making her wrist worse. The man with the stiff knee liked catching a dragon who thought she was too clever to catch.{/n}
"That only happened once," {n}Aivu tells him.{/n}
"Once today."
{n}She points a claw at him, delighted by the threat of another attempt.{/n}
{n}When the others have gone, Aivu collects the flags while you rub out the chalk where it crosses the ordinary walking route. The missing drum no longer leaves an obvious hole. She still mentions it.{/n}
"Next time he might come."
"He might."
"It was good without him. But it could be good with him too."
{n}She has one flag left to untie. Instead of reaching for it, she looks at you.{/n}
"Did you like it? Really? You can tell me a bit you didn't like. Not every bit at once."''',
      c('"I liked playing beside you. I missed you when you were trying to do every job."', "company"),
      c('"The rules took a while to explain. Next time, demonstrate one round first."', "practice")),
    n("company", "Aivu", '''"I was right there."
{n}She thinks about it before you answer.{/n}
"Oh. You mean there with you."
{n}You untie the last flag together. She begins folding it, stops when the corners refuse to match, and hands you one side.{/n}
"I wanted you to see I could do it. Then I couldn't stop doing it long enough for you to see anything except me running about."
{n}She does not look pleased with that discovery. She does look pleased when you remind her of the round she lost by making faces.{/n}
"I was being very expressive. It is dangerous work."
{n}On the way back, she asks which part you would choose for another gathering. She listens to the answer without immediately assigning you three more jobs. Then she announces what she wants: the introduction, one particularly good round, and enough time to sit down with a friend afterwards.{/n}
"That's this bit," {n}she says.{/n} "I wanted this bit too."''',
      c('[Walk back together with the rolled flags.]', flags=("aivu.gathering_kept", "aivu.company_requested"))),
    n("practice", "Aivu", '''"One round with someone who's very good at being wrong. I was very good at that when we practiced."
{n}You agree. She invents a demonstration in which the dreadful creature tries to steal the whole castle instead of the tail. You point out that it might give people ideas. She revises it to a creature trying to eat the chalk.{/n}
"No actual eating. We should say that part."
{n}You fold the last flag together. She asks another question, this one quieter: whether you had time to enjoy yourself while she kept finding jobs for both of you.{/n}
{n}You tell her which round you liked. She remembers it and supplies a detail you missed, something a spectator said while you were concentrating. The story takes you most of the way back to the throne room.{/n}
"Next time we show them once," {n}she decides.{/n} "Then we let them be wrong in their own interesting ways. Except about real tails."
{n}She glances at the flags in your hands.{/n}
"You can have the first turn. I want to see what you try when I'm not telling you how everything goes."''',
      c('[Keep a demonstration round in mind for next time.]', flags=("aivu.gathering_kept", "aivu.demo_planned"))),
], requires=("aivu.game_invited",), delay=48)


s("a_castle_in_a_bad_place", "A castle in a bad place",
  '"Would you like a little time together before we leave the Nexus again?"', [
    n("start", "Aivu", '''"Yes. Something that isn't looking for somebody who wants to hurt somebody else. I know we have to do that. I want something else for a bit."
{n}Aivu has found a patch of level stone away from the usual foot traffic. She has arranged several pebbles in a crooked circle. There is no royal turnip here, and no crowd waiting to be entertained. She moves one pebble with the edge of a claw.{/n}
"This is a castle. It has a door that opens properly and windows that don't make faces. I started with those because they seem quite important here."
{n}She leaves a space in the circle for another stone.{/n}
"You can put something in. But it has to be something you'd want to find when you came back. Not a trap. Unless it's a trap for something awful and it takes all its teeth away."
{n}The strange light of the Nexus catches along her wings. She shifts them so they do not brush the stones. In the distance, someone calls to another person getting ready to leave. Aivu waits until the noise has passed before looking back at you.{/n}''',
      c('"A room where nobody asks me to decide anything for a little while."', "room"),
      c('"A window looking toward somewhere I miss."', "window"),
      c('"A kitchen. We should begin with something both of us understand."', "kitchen"),
      c('"Keep the castle for me. I cannot sit down yet."', abort=True)),
    n("room", "Aivu", '''"Would I be allowed in? I ask things. Quite a lot of things."
"You would. We could decide beforehand which things needed asking."
{n}She finds a flat pebble for the room and puts it just inside the circle.{/n}
"I wouldn't ask whether to fight someone. I'd ask if you wanted to hear a story, or if the room needed another window. Those are easier decisions."
{n}You admit that sometimes even easy decisions arrive when you have no room left for them. Aivu looks briefly alarmed, as though she has been carrying an armful of questions into a space already full.{/n}
"Then I'd tell you what I was doing," {n}she says.{/n} "And if you wanted to join, you could. I'd put the story near enough that you could hear it."
{n}She begins a story about a castle whose inhabitants were all very important and kept accidentally appointing one another to things. Before long, the soup has been made Governor of the Kitchen. It immediately abolishes spoons.{/n}
{n}You laugh. Aivu stops trying to improve the room and keeps telling the story.{/n}''', c('[Add a stone for the kitchen governor.]', "finish")),
    n("window", "Aivu", '''"Only looking? Or could you go through?"
"Let us start with looking."
{n}You describe a place you miss, choosing a detail small enough that she can imagine it. She asks about its colors, then its noises. When you tell her how it smelled, she puts a striped pebble beside the opening in the circle.{/n}
"That's the window. If I look through, will it show me your place or mine?"
"We can give it two shutters."
"Yes! Mine will have leaves outside. Not all the same kind. And there will be people arguing about something unimportant very loudly, because that's how you know nobody is being eaten."
{n}She lies down beside the little window. For a while you take turns describing what could be on the other side. She contributes a cousin who pretends not to like a particular fruit, then eats it whenever nobody is watching. You contribute something she does not expect about your own place.{/n}
"I thought it would all be very heroic," {n}she says.{/n} "I'm glad it has that bit in it too."
{n}The pebble shows you only stone. The places remain clear enough between you.{/n}''', c('[Leave both imagined shutters open.]', "finish")),
    n("kitchen", "Aivu", '''"A big kitchen. With something going wrong in it, but only a little wrong. Like too much icing."
{n}She chooses a pale stone for the table and a round one for an oven. When you ask what she means to cook, she starts with six desserts and has reached nine before admitting that someone ought to make supper first.{/n}
"We could put supper between the desserts. Then nobody could complain it wasn't there."
{n}You describe a food that reminds you of an ordinary day. She asks who made it, or where you found it, and whether it was as good as you remember. You admit whatever uncertainty belongs to the memory.{/n}
"I think things taste different when you miss them," {n}she says.{/n} "I keep thinking of a fruit from home. Sometimes I remember it as sweeter. Sometimes I remember a bit that stuck in my teeth. I wouldn't mind that bit now."
{n}You invent a meal for the stone kitchen. She objects to one ingredient, suggests a stranger one, and then agrees that perhaps the cook should get to taste it before serving it to everyone else.{/n}
{n}The oven stone rolls away while she gestures. She catches it with a forepaw and declares that the kitchen has suffered its first disaster, successfully contained before anyone lost their pudding.{/n}''', c('[Put the oven back on level stone.]', "finish")),
    n("finish", "Aivu", '''{n}The castle has acquired more rooms than either of you meant to build. Aivu counts them, forgets which stone is the last wall, and decides that the building may be allowed to have a secret passage without knowing exactly where it is.{/n}
"We should leave it for someone to find. Do you think they'll understand?"
"Some of it."
"They can make up the other bits. Unless they think it's rubbish and kick it over."
{n}She looks at the little building. Then she takes one stone from its edge and puts it beside you.{/n}
"Keep that part in your head. I'll keep this part. If the stones go, we'll still know how it started."
{n}When it is time to rise, she checks that the arrangement will not trip anyone. You shift two stones away from the walking route. The castle loses a tower and gains a courtyard.{/n}
"Better," {n}she says.{/n} "Now people can come in without breaking the whole front."
{n}She walks with you until the next task calls you apart, occasionally suggesting another room and then answering her own objection to it. Her voice sounds ordinary for a little while, even here.{/n}''',
      c('[Leave the stone castle where someone may discover it.]', flags=("aivu.nexus_castle_kept",))),
], requires=("aivu.gathering_kept",), chapters=(4,), area=NEXUS)


s("the_watch_she_chooses", "The watch she chooses",
  '"We can stay here a while, if you would like company."', [
    n("start", "Aivu", '''{n}Aivu lifts her head at your approach. She has chosen a place in the Nexus with open space on either side. When somebody passes behind you, her eyes follow them until she knows who it is.{/n}
"Here is good," {n}she says.{/n} "I can see who's coming."
{n}She shifts a forepaw to make room beside her. The invitation is clear; the reason for it is hers to give.{/n}''',
      c('"Is this like the frightened feeling you told me about?"', "remembered", requires=("aivu.native_fear_told",)),
      c('"What would help you feel comfortable here?"', "present", forbids=("aivu.native_fear_told",)),
      c('"I will come back when I can stay."', abort=True)),
    n("remembered", "Aivu", '''"A bit. It comes back when I don't ask it to. Very rude."
{n}She makes an annoyed face at the empty space ahead of her, then looks at you again.{/n}
"When they had me, I kept listening for someone I knew. Sometimes there was a noise and I thought it might be you. Then it wasn't."
{n}She watches your face closely.{/n}
"I know you came. I'm glad you came. That part happened. The other part happened too."
{n}Aivu stretches one wing and folds it again, testing how much room she has.{/n}
"I'd like to know when you get up. That's all. Don't go very quietly because you think I'm asleep. I might be listening with my eyes shut."
{n}You agree to tell her before leaving. She settles a little lower, no longer watching your hands quite so closely.{/n}''', c('[Stay where she can see you.]', "choice")),
    n("present", "Aivu", '''"If you tell me when you're going. Even if you think I haven't noticed you're here anymore. I notice."
{n}She presses one claw against the stone, then releases it.{/n}
"When they caught me, I kept waiting for a noise that meant somebody had found me. I heard lots of noises. Most of them weren't that one."
{n}Her tail lies very still.{/n}
"I'm brave. I am. But I was scared as well. I don't know why those things have to happen together."
{n}You tell her that you can stay now and will tell her when you must leave. She does not ask for a larger promise. After a while she moves her paw away from the place beside her, making the space wider.{/n}
"Good. We could do something. Something that doesn't have a surprise ending."''', c('[Stay where she can see you.]', "choice")),
    n("choice", "Aivu", '''{n}There are several pebbles within reach. Aivu taps one, then pushes it toward you.{/n}
"We could make up a very boring story. Not boring to listen to. Boring for demons, because nothing horrible happens in it. They'd hate it."
{n}She looks toward the open space beyond you.{/n}
"Or we can watch. I keep watching anyway. If we did it on purpose, maybe I could stop trying to pretend I wasn't."
{n}Her voice becomes brisk, almost official.{/n}
"You can pick which you'd like. I can pick again if I don't like it when we start."''',
      c('"Let us tell the sort of story a demon would abandon in disgust."', "story"),
      c('"We can watch together. Tell me what you notice."', "watch")),
    n("story", "Aivu", '''"Once there was a person who went to get a loaf of bread," {n}Aivu begins.{/n} "And they got one."
{n}She waits for you to add something. You suggest that the loaf was still warm. She nods solemnly.{/n}
"That was good. They took it home. The door was where they'd left it."
{n}The story accumulates ordinary things. A knife that cuts properly. A cup that belongs to someone who will be back for supper. A neighbor who borrows salt and returns with a ridiculous explanation for needing it.{/n}
{n}Aivu laughs at the explanation. Then a sharp noise sounds across the Nexus, and she stops. You wait while she looks. It is someone setting down a piece of equipment. She watches until she is satisfied.{/n}
"The neighbor," {n}she says at last,{/n} "had been trying to make a cake without knowing what salt was for."
{n}You continue. Nobody steals the house. Nobody turns out to have been a monster all along. The cake is bad, but the people have bread, and somebody finds something sweet to put on it.{/n}
"That would make a demon absolutely furious," {n}she says.{/n} "It would want a different book."
{n}She nudges the pebble back to you, giving you the last sentence. You bring the people to supper. Aivu listens until they are all sitting down.{/n}''', c('[Tell her before you need to rise.]', "leave_story")),
    n("watch", "Aivu", '''{n}You settle facing the same direction. Aivu points out the places where someone might appear, the sounds she can identify, and one sound neither of you can explain. You do not invent a harmless answer for it. After a while the sound repeats and you see a loose strap tapping a buckle nearby.{/n}
"That one was a very small mystery," {n}she says.{/n} "Annoyingly persistent."
{n}The next few minutes pass without much happening. Aivu describes a person walking as though their boots disagree about where to go. You point out another who has stopped to check a pack for the third time.{/n}
"I do that," {n}she says.{/n} "I count things I know are there. Then I know them again."
{n}You tell her one thing you do when you cannot settle. She asks a practical question about it, then tries to explain her own habit more precisely. The conversation comes and goes between periods of watching.{/n}
{n}When you shift your weight, she looks toward you. You tell her you are making yourself more comfortable. She nods and returns to the open space.{/n}
"You can move," {n}she says.{/n} "I just like knowing what the movement means."
{n}A little later she yawns, enormously and without apology. Watching has become tiring enough that she wants to rest her head. You remain beside her for the last part of the visit.{/n}''', c('[Tell her before you need to rise.]', "leave_watch")),
    n("leave_story", "Aivu", '''{n}You tell Aivu that you will need to go soon. She asks for enough time to finish one thought.{/n}
"The person with the bad cake should try again. Not today. They've already had supper. Another day."
{n}You agree. She stretches, looks around, and chooses where she wants to settle next. It is nearer the ordinary bustle, where she can recognize the voices.{/n}
"You can tell me another bit when you have time," {n}she says.{/n} "Or I can tell you. I've got an idea about the salt."
{n}She leaves the pebbles in a small cluster beside the place you sat. There is no claim that they will keep anything away. She simply wants to recognize the spot when she passes it again.{/n}''',
      c('[Walk with her as far as the familiar voices.]', flags=("aivu.rescue_company_kept", "aivu.rescue_story"))),
    n("leave_watch", "Aivu", '''{n}You tell Aivu that you will need to go soon. She lifts her head, checks the open space once more, and decides to move nearer the ordinary bustle.{/n}
"It's easier when I know which noise belongs to which person," {n}she says.{/n} "The quiet noises are sometimes worse. They could be anything."
{n}You walk with her until she finds the place she wants. Before you part, she asks whether you noticed how many times the person checked their pack. You did not count. She did, and is delighted to have an answer you lack.{/n}
"I'll watch something else next time. You can try to guess."
{n}She settles where familiar voices can reach her. The next time you move away, she knows you are going because you have told her. She watches you leave, then turns toward someone calling her name.{/n}''',
      c('[Leave after she has found the company she wants.]', flags=("aivu.rescue_company_kept", "aivu.rescue_watch"))),
], requires=("aivu.started", "aivu.native_rescue_complete"), chapters=(4,), area=NEXUS, delay=24)


s("a_family_with_too_many_names", "A family with too many names",
  '"You look as though you are trying to remember something."', [
    n("start", "Aivu", '''"A sound. Which is difficult, because every time I try to make it, I can only hear me making it wrong."
{n}Aivu has arranged several leaves on a folded cloth beside the throne-room door. One is broad and stiff, another long and narrow. She blows across the narrow one. It trembles without making the noise she wants.{/n}
"At home we had leaves that did a sort of..."
{n}She makes a noise halfway between a whistle and a very offended bird.{/n}
"Not that. Better than that. My cousin could do it with an ordinary leaf too, but she wouldn't show me how because I kept saying it was easy. It was easy for her. That's what I meant."
{n}She tries again. The leaf folds against her nose.{/n}
"Now I could ask properly, except she's in Elysium and this leaf is here. Very inconvenient."
{n}Pella has offered a few leaves from the garden for the experiment. Aivu wants to find the sound before she forgets exactly how it differed from the noises she is making now.{/n}''',
      c('"Show me how your cousin held it. We can try to work it out."', "try"),
      c('"Tell me what you remember around the sound. That might help."', "memory"),
      c('"Save the leaves. I cannot stay long enough today."', abort=True)),
    n("try", "Aivu", '''{n}You walk to Pella's patch, where there is room to experiment without supplying the court with a series of alarming noises. Aivu holds a leaf between two claws and demonstrates the angle she remembers.{/n}
"She was smaller than me. I mean, smaller than I am now. Not smaller than me then. It's very unfair how many different sizes a person can remember."
{n}You try the leaf between your thumbs. The first breath does nothing. The next makes a thin rasp. Aivu leans so close that her breath changes yours into a completely different sound.{/n}
"Again! That had a bit of it."
{n}Pella brings a firmer leaf. She used to make a similar noise as a girl, but her way of holding it is different. You try both arrangements, keeping the leaves far enough from Aivu's teeth that she does not accidentally solve the problem by eating it.{/n}
{n}At last the leaf gives a clear, sharp note. Aivu jumps, then bursts into laughter.{/n}
"That's nearly it! Except hers went up at the end, like it was asking a very nosy question."
{n}You cannot quite make it rise. The note is still enough to set her talking about the place where she heard it.{/n}''', c('[Listen while she keeps the leaf steady.]', "home")),
    n("memory", "Aivu", '''{n}You walk with her to Pella's garden. Aivu puts the leaves down in the shade and tries remembering the day without performing the sound.{/n}
"There was fruit. There is fruit in lots of things I remember, so that doesn't narrow it down. And someone was calling us back, but we were pretending not to hear because we'd found something more interesting."
"The leaf?"
"No, the leaf was later. We found a beetle with a very shiny back. My cousin said it looked like an important person in armor. I said it probably thought we looked ridiculous without any."
{n}She pauses, amused by the memory.{/n}
"Then she made the sound to see whether it would move. It didn't. Very dignified beetle. That's why I kept saying it was easy. I wanted a turn."
{n}Pella listens while she tends the garden. She brings you a firmer leaf and shows you a way to make it rasp between your thumbs. Aivu recognizes enough of the motion to lean forward eagerly.{/n}
{n}Your first clear note makes her laugh. It is lower than the sound she remembers, but she knows where she wants it to go now.{/n}
"Up at the end. Like the beetle was meant to answer."''', c('[Try the sound once more, then let her talk.]', "home")),
    n("home", "Aivu", '''"I wonder if she still does it. She might have found a better thing by now."
{n}Aivu turns the leaf over. A thin line has split along its edge. It will not keep making the sound forever.{/n}
"Everyone here knows me as your dragon. At home I'm the one who wanted a tail tuft and lost a race because she stopped to shout that she was winning."
{n}She gives you a stern look.{/n}
"That happened once. It was an excellent shout."
{n}You promise to judge the shout and the race separately. She seems satisfied.{/n}
"I want to tell them about the garden. And the game. And about you doing something that isn't defeating a terrible monster. They already expect terrible monsters."
{n}She looks at the old green sign, folded beside her leaves.{/n}
"If I tell them I had a good day here, will it sound as if I don't miss them? I do miss them. I just don't miss them every single moment. Sometimes I'm busy having the day."
{n}Pella leaves you to talk while she carries an empty pot to the shed. Aivu watches the leaves stir in her absence.{/n}''',
      c('"Tell them the day you want to share. Missing them is why you want them to hear it."', "tell"),
      c('"You can tell them something you miss, and something you found here. Both are true."', "both")),
    n("tell", "Aivu", '''"Then I want the part where the man caught my tail. I could make him sound a little less pleased with himself. He was terribly pleased."
{n}You raise an eyebrow. She revises the sentence before you need to speak.{/n}
"All right. Exactly as pleased. I can make the noises better instead."
{n}She begins dictating a story for her family. You write what she says on the blank side of a scrap, stopping when she decides a word is not grand enough. Soon the account has a garden, a turnip, and a Commander who has apparently become an expert in protecting vegetables of state.{/n}
{n}When she reaches the end, she asks you to add a question for her cousin about the leaf. Then she studies the paper.{/n}
"We haven't got someone to carry this."
"Not yet."
"Then we'll keep it. When there's someone, it will be ready."
{n}She folds the scrap around the leaf and decides against that arrangement immediately. The damp leaf might spoil the words. You keep the paper separate while she finds a dry place for her botanical instrument.{/n}''',
      c('[Keep the account safe until there is a real way to send it.]', flags=("aivu.home_story_ready", "aivu.home_game_story"))),
    n("both", "Aivu", '''"The leaf and the garden. One thing that doesn't do what I remember, and one thing that did something I hadn't thought of."
{n}You write while she talks. The story begins in Elysium with the dignified beetle, wanders into Drezen, and ends with Pella's cart finding another patch of sun. Aivu asks you to leave room for a drawing, then uses rather more than the room you left.{/n}
"The wheel is important. They have to see it was broken."
{n}She adds a question for her cousin about making the leaf's note rise. After a while she also adds that she would like to hear what everyone has been doing, including anything that sounds ordinary to them.{/n}
"I might have forgotten which bits were ordinary," {n}she explains.{/n}
{n}There is no courier to Elysium waiting at the garden gate. You say so plainly when she asks how the page will travel. She is disappointed, then folds it carefully.{/n}
"We'll find someone to ask. It doesn't have to fly away just because we finished writing it."
{n}She gives the page to you for safekeeping and keeps the leaf. On the way back she manages one more rasping note. It is still wrong at the end, and she is still pleased by it.{/n}''',
      c('[Keep the page dry while she practices the leaf note.]', flags=("aivu.home_story_ready", "aivu.home_two_places"))),
], requires=("aivu.gathering_kept",), delay=48)


s("paint_for_a_weather_day", "Paint for a weather day",
  '"Pella has a spare board. Did you still want something bright beside the garden?"', [
    n("start", "Aivu", '''"Yes! Something that doesn't look as though it was already bored when somebody built it."
{n}Aivu joins you at the throne-room door carrying a narrow board beneath one wing. Pella has asked for a sign small enough to hang on the shed. She has supplied the words she wants on it. Aivu has supplied several possible monsters to surround them.{/n}
"This one guards the herbs. This one eats people who call everything a weed. This one is just there because I like its ears."
{n}The monster with the ears occupies most of the available space. Pella's name has been squeezed into a corner.{/n}
"That's the practice bit," {n}Aivu says quickly.{/n} "I know the actual letters have to fit."
{n}At the garden, Pella brings out two pots of color she has bought from a painter using leftover pigment. One is a bright yellow that makes Aivu's eyes widen. The other is a dark green. There is enough for a small sign, but little to waste.{/n}
"And no painting the shed itself," {n}Pella says.{/n}
"Even a little?"
"The board."
{n}Aivu sighs with all the sorrow of an artist denied a continent.{/n}
"Then it had better be a very good board."
{n}You sketch the letters first. Aivu places the eared monster beneath them, curled around the edge. Its tail points toward the garden without covering the words. She asks you to choose what the monster is doing.{/n}''',
      c('"Let it look fierce, but give it a little watering can."', "fierce"),
      c('"Let it peer out as though it wants to know who is coming."', "curious")),
    n("fierce", "Aivu", '''"A terrifying gardener. Good. Nobody will dare step on the onions."
{n}She paints a row of teeth, then gives the monster a watering can too small for its enormous paws. You suggest a longer handle. She insists that the monster has learned to be careful. Pella says she approves of this monster more than the one that ate people.{/n}
{n}The bright yellow makes a splendid stripe along its back. Aivu adds another. Soon she is reaching for more color than the little brush can hold, and a drop falls across the lower edge of a letter.{/n}
"That can be a sun," {n}she says.{/n}
"In the middle of Pella's name?"
"A very small sun."
{n}You lift the excess paint with a clean rag before it spreads. Aivu watches, then touches up the letter herself. The sun must find another place.{/n}
{n}When the paint is dry enough to handle, you hang the board on a hook beneath the shed's eave. Pella steps back and reads it without help. Aivu waits for her opinion of the monster.{/n}
"Looks fierce," {n}Pella says.{/n} "I'd trust it with a watering can."
"Exactly!"''', c('[Return after the paint has had a day outside.]', "weather")),
    n("curious", "Aivu", '''"It can have its nose round the corner. Like this."
{n}Aivu demonstrates, leaning so far around the board that she nearly tips the yellow pot. You catch it. She withdraws her nose and redraws the creature a little farther from the edge.{/n}
"It doesn't have to know everything all at once."
{n}You paint the letters while she fills in the monster's ears. One yellow ear becomes larger than the other. She studies the difference, then decides the creature must be hearing something especially interesting on that side.{/n}
{n}Pella likes the face. She asks why it has so many teeth. Aivu says curiosity might lead it somewhere that requires them. Pella cannot argue with that.{/n}
{n}When the paint is dry enough, you hang the board beneath the eave. From the lane, the monster appears to be peering out at arriving customers. Aivu walks past three times to make sure it keeps doing so.{/n}
"There. It looks like the garden wants to know who you are."
"The garden wants watering," {n}Pella says.{/n}
"It can want two things."''', c('[Return after the paint has had a day outside.]', "weather")),
    n("weather", "Aivu", '''{n}When you next meet Aivu at the throne-room door, she is carrying the board again. The letters remain legible. The bright yellow has dulled, and a thin streak trails from one painted edge.{/n}
"It rained sideways," {n}she says.{/n} "Apparently the sky thought the little roof was cheating."
{n}Pella has taken the sign down before more color washes away. The painter explains that the yellow was mixed for indoor use. He can add a protective finish, but it will darken the color. Or he can supply a duller outdoor pigment when his next batch is ready.{/n}
"Why does making it last have to make it less yellow?" {n}Aivu asks.{/n}
{n}The painter shows her two scraps so she can see the difference. She looks from one to the other with genuine distress. The monster she imagined was bright enough to make a stranger stop. The weather has opinions of its own.{/n}
"Could we keep the yellow one inside and make another for outside?"
{n}Pella can pay for enough color to repair this sign, not two new signs. You could help Aivu repaint it with the outdoor pigment, keeping the bold shape, or preserve the existing picture under the darker finish. Either will change what she made.{/n}''',
      c('"Keep your picture. Let us see what the finish does to it."', "finish"),
      c('"We can keep the creature and paint it in colors that survive here."', "repaint")),
    n("finish", "Aivu", '''{n}Aivu asks the painter to show her the finish on a small corner first. The yellow deepens into gold. It is quieter, but the black outline stands out more clearly against it.{/n}
"It looks older," {n}she says.{/n} "Not the monster. The day it's standing in."
{n}She considers that description, then asks him to finish the rest. You hold the board steady while he works. When it dries, Aivu adds one clean bright dot to each eye, sheltered well beneath the eave when the sign returns to its hook.{/n}
{n}Pella reads it from the lane. The monster's enormous ears stand out beneath her name. Aivu traces their shape in the air, then steps aside to see the whole sign.{/n}
"I want to paint something indoors next time," {n}Aivu says.{/n} "Then the sky can look through a window and be jealous."
{n}She keeps the painter's test scrap. It fits within her rolled map without hiding any of the streets.{/n}''',
      c('[Walk past once more to admire the finished sign.]', flags=("aivu.sign_kept", "aivu.sign_finished"))),
    n("repaint", "Aivu", '''{n}Aivu asks to keep the original outline. The painter gives her a scrap on which to test the outdoor color. It is less brilliant, but thick enough to make a clean stroke without running.{/n}
"That's quite nice," {n}she admits.{/n} "It goes where I tell it."
{n}You help clean the damaged parts of the sign. Aivu repaints the monster, making its ears a little larger and its eye easier to see from the lane. The letters remain clear. Pella objects only when the tail threatens to curl through the name again.{/n}
"It likes you," {n}Aivu explains.{/n}
"Then it can stop interrupting me."
{n}The revised sign returns to its hook. Aivu walks past, stops, and backs up to look again.{/n}
"I miss the yellow. I like this face better. Both things at once. Very inconvenient."
{n}She keeps the scrap bearing the old bright color, dry inside her rolled paper. The outdoor creature can guard the garden. The impossible yellow can remain somewhere she may still look at it.{/n}''',
      c('[Leave the sign to its first ordinary day of weather.]', flags=("aivu.sign_kept", "aivu.sign_repainted"))),
], requires=("aivu.home_story_ready",), delay=48)


s("a_small_garden_of_her_own", "A small garden of her own",
  '"How is the cutting Pella gave you?"', [
    n("start", "Aivu", '''"Alive. But cross with me. Or with the place I put it. It's very hard to tell when something only has leaves to explain with."
{n}Aivu brings you to Pella's shed. The cutting stands on a low bench, its newest leaves curled inward. Pella has asked Aivu to describe everything she did before deciding what needs changing.{/n}
"I put it where it could have lots of sunshine," {n}Aivu says.{/n} "Because the big garden wanted sunshine. And I gave it water."
"How much?"
"Enough that I could see it had some."
{n}Pella lifts the pot. Water drips from a hole in its bottom. Aivu's tail gives an unhappy twitch.{/n}
"It was thirsty before. I didn't want it to be thirsty again."
"Let us see the roots," {n}Pella says.{/n} "Then we will know more."
{n}She lays a cloth on the bench and asks Aivu to hold the pot sideways while she loosens the soil. The cutting comes free with a small mass of pale roots, some healthy, some softened and dark. Aivu peers at them without touching.{/n}''',
      c('"You showed her how to pot it earlier. Can we use that deeper pot again?"', "potted", requires=("aivu.cutting_potted",)),
      c('"You had an appointment to pot it together. Is there still time?"', "appointment", forbids=("aivu.cutting_potted",))),
    n("potted", "Aivu", '''"We left room for the water," {n}Aivu says.{/n} "I remembered that part."
"You did," {n}Pella replies.{/n} "Then you filled the room too often."
{n}She lets Aivu feel the difference between the wet soil near the roots and the drier soil in a spare pot. Aivu rubs the damp soil between two claws, then tests the drier handful again.{/n}
"It's got a bigger home now," {n}Aivu says.{/n} "I thought that meant it would want more of everything."
{n}Pella cleans the pot and asks you for a little dry soil from the sack beside the shed. Aivu watches the damaged roots as the gardener trims them away. She does not like this part, but she wants to see it.{/n}
"Can it grow those back?"
"If we keep the healthy ones from sitting in water."
{n}The plant returns to the same deep pot, with fresh soil around it. Pella presses the surface gently and hands Aivu a narrow stick for checking how damp it is below.{/n}''', c('[Stay while Aivu practices the check.]', "growth")),
    n("appointment", "Aivu", '''"Yes," {n}Pella says.{/n} "This is a good time. We have something worth looking at."
{n}Aivu fetches the deep pot she has been saving. She had expected the appointment to be a celebration of how well her plant was doing. Instead she watches Pella trim away the damaged roots and explains, in a small voice, that she thought extra water would help it grow faster.{/n}
"It wants enough," {n}Pella says.{/n} "That takes some learning."
{n}You hold the pot while Aivu scoops in fresh soil. Pella shows her where to stop, leaving room for water to settle before it drains. Then she gives Aivu a narrow stick to test the moisture beneath the surface.{/n}
"I can check before I add anything."
"That's the idea."
{n}Aivu puts the stick in, pulls it out, and studies the dark mark along its lower end. The plant has supplied an answer without acquiring a voice. She seems almost disappointed by how simple the answer is.{/n}''', c('[Stay while she tries the moisture check again.]', "growth")),
    n("growth", "Aivu", '''{n}Pella moves the plant into lighter shade. She expects it to recover, but will not promise every curled leaf will straighten. Aivu keeps looking at the smallest one.{/n}
"I grow when your power gets bigger," {n}she says to you.{/n} "It doesn't grow when I want it harder. That's different."
{n}She considers the plant beside her paw.{/n}
"Sometimes people see how big I am and think I've learned everything that fits inside the big bits. But I haven't. I'm still me. I don't suddenly know how much water a leaf wants."
{n}Pella has gone to rinse the cloth. Aivu lowers her voice.{/n}
"Do you ever forget? About me still being little, I mean. I like doing big things. I don't want everyone to make all the choices for me. I just don't always know what I'm doing."
{n}Her expression is serious enough that a reassuring joke would not quite answer the question.{/n}''',
      c('"Sometimes I expect too much. Tell me when I do, and I will try to notice sooner."', "expect"),
      c('"I know you are still learning. I want you to be able to ask without feeling small."', "ask")),
    n("expect", "Aivu", '''"I might tell you very loudly."
"I suspected that."
{n}She relaxes enough to smile, then returns to the question.{/n}
"Sometimes I say I can do something because I want to be the sort of dragon who can. Then everyone is waiting, and it's horrible finding out I can't while they're all looking."
{n}You ask whether the garden game felt like that. She thinks for a while before answering.{/n}
"A little. Until you did your bit and I remembered I wanted to play."
{n}You tell her one way she can call a pause when she needs help. She rejects your first suggestion as too solemn and invents another, involving the royal turnip issuing a temporary decree. You agree on an ordinary phrase as well, for times when neither of you feels like joking.{/n}
{n}Pella returns with the cloth. Aivu asks her to look after the cutting while you are away from Drezen. She will visit and help when she is here. She has stopped pretending she can be in every place that needs her at once.{/n}
"It can still be mine," {n}she tells you, watching Pella place it beside the other pots.{/n} "And Pella can know what it's doing when I'm somewhere else."''',
      c('[Agree to help her remember the plant when you return.]', flags=("aivu.plant_care_agreed", "aivu.pause_named"))),
    n("ask", "Aivu", '''"That's a nice thing to want. Sometimes asking makes me feel small anyway. Especially if the answer is something everybody else already knows."
{n}You admit that this happens to you too. She looks delighted, then catches herself.{/n}
"Not delighted that it feels bad. Delighted that you don't know everything either."
{n}She asks you to name something ordinary you learned late. You choose a true small embarrassment. Aivu listens intently and then admits that she once thought roots were the part a plant used to hold onto the world when the wind came.{/n}
"They do that too," {n}you tell her.{/n}
"I was partly right! That's my favorite sort of not knowing."
{n}When Pella returns, Aivu asks whether the plant can stay in her care while you travel. Pella agrees. Aivu will help and learn when she is in Drezen, and the cutting will not have to survive every absence on enthusiasm and extra water.{/n}
{n}She puts the checking stick beside its pot. Before leaving, she asks Pella one more question about roots. This time she does not preface it by explaining how much she already knows.{/n}''',
      c('[Wait while Pella answers her question.]', flags=("aivu.plant_care_agreed", "aivu.questions_welcome"))),
], requires=("aivu.sign_kept",), delay=48)


s("the_people_on_the_map", "The people on the map",
  '"Shall we see how Pella and the garden are doing?"', [
    n("start", "Aivu", '''{n}Aivu brings her rolled paper to the throne-room door. The edges have softened from use, and the string has been replaced with a longer piece. She turns it once between her forepaws before speaking.{/n}
"I keep thinking I know Drezen. Then I go round a corner and somebody has changed something. You'd think they'd tell the map."
{n}At the garden, Pella has put a new board under the cart to keep it level. Aivu's cutting has grown new leaves. A few of the old curled leaves have fallen. Pella saved none of them; she shows Aivu the healthy growth instead.{/n}
"It looks different," {n}Aivu says.{/n}
"It has been busy."
{n}She accepts that answer and gets the checking stick. The soil needs no water today.{/n}
{n}Pella tells you that she has agreed to spend part of the coming season helping her sister with another garden. A neighbor will tend the cart while she is away. She means to leave when her arrangements are ready, and return if the work permits.{/n}
"But you live here," {n}Aivu says.{/n}
"I do. I have a sister elsewhere too."
{n}Aivu glances at the sign you painted. It still hangs beneath the eave, pointing to a person who is making plans beyond its little corner of the city.{/n}''',
      c('"What does your sister grow?"', "sister"),
      c('"Aivu, would you like to ask how to find Pella while she is away?"', "address")),
    n("sister", "Aivu", '''{n}Pella describes a larger plot, more work than her sister can manage alone, and a neighbor who gives very confident advice about plants he has never grown. Aivu becomes interested in the neighbor at once.{/n}
"Does he know he's doing that?"
"Not yet. My sister expects me to tell him."
"Then you have to go. That's important garden business."
{n}The joke makes it easier to ask the next question.{/n}
"Will you come back for this one?"
"If I can. If I cannot, I will write to the neighbor who is looking after it. She'll tell you."
{n}Pella gives you the name of the place and a practical route by which ordinary letters can reach her sister. Aivu asks you to write the address on a separate scrap so the garden's map does not have to stretch across the whole country.{/n}
{n}She studies the address after you write it. Unlike the page intended for Elysium, this one has a known way to go.{/n}''', c('[Help her choose what to say before Pella leaves.]', "want")),
    n("address", "Aivu", '''"Yes. Except if I ask like that, it sounds as if I've decided it's all right for her to go."
{n}Pella puts down her little knife.{/n}
"Do you want me to stay because you haven't decided?"
{n}Aivu stares at the soil, then shakes her head.{/n}
"No. I want to like it more than I do."
"You can write while you work on that."
{n}Pella gives you her sister's address and explains how ordinary letters can reach it. Aivu asks you to write clearly enough that nobody will have to guess which part is a bird. The joke is small and a little strained, but she makes it herself.{/n}
{n}You put the address on a separate scrap. Pella will leave word with the neighbor tending the cart if her plans change. There is no promise that every message will arrive quickly. There is a person who knows where another person means to be.{/n}
"That's better than drawing an arrow into nothing," {n}Aivu says.{/n} "I still wish the arrow were shorter."''', c('[Help her choose what to say before Pella leaves.]', "want")),
    n("want", "Aivu", '''{n}Pella leaves you beside the garden while she fetches a pot for the neighbor. Aivu watches the path to the shed.{/n}
"I don't want her to think I only liked her because she knew how to keep my plant alive. I like how she says things. Even when they're annoying things."
{n}She takes the rolled paper from beneath her wing. The garden, the shed, and the painted sign are all there. Pella herself appears only as a small face beside the cart.{/n}
"I could give her the picture. Then she'd know. But I want to keep it too. It's got the first place and this place and all the parts we did."
{n}There is time to make a small separate drawing, or to give Pella the original garden page while keeping your other papers. Neither choice will make the departure stop.{/n}''',
      c('"Make her a new picture. Put yourself in it, so she knows who will be thinking of her."', "new"),
      c('"If you want her to have the original garden page, give it to her. We can keep the story."', "original")),
    n("new", "Aivu", '''{n}Aivu draws herself beside the garden. At first she makes her wings so large that they cover the shed. Then she starts again, grumbling that fitting into a picture is harder than fitting into a place.{/n}
{n}You add a small outline of yourself where she asks. She gives you a turnip, then decides this is confusing and erases it. The final picture has Pella at the cart, Aivu beside the cutting, and you trying to keep a curling piece of paper from escaping.{/n}
"That happened often enough," {n}she says.{/n}
{n}Pella returns and accepts the drawing with both hands. She asks Aivu to write her name on the back. Aivu does, slowly and proudly, using the short name that is hers now.{/n}
"Tell your sister I hope her garden is very good," {n}she says.{/n} "And tell the neighbor not to be too certain about the bits he doesn't know."
{n}Pella promises to pass on the first message and consider the best way of delivering the second. Aivu laughs and lets her return to her arrangements.{/n}''',
      c('[Keep the original papers and Pella\'s address together.]', flags=("aivu.pella_farewell_kept", "aivu.pella_new_picture"))),
    n("original", "Aivu", '''{n}Aivu separates the garden page from her other papers. She examines the stains, the crooked first outline of the cart, the line joining the old patch to the new one. Then she smooths it with the flat of a forepaw.{/n}
"I want her to have this one. It already knows her."
{n}You help her fold it so the drawing stays inside. When Pella returns, Aivu gives it to her before explaining, as though too much explanation might make her change her mind.{/n}
"For the other garden. So it knows you've had practice."
{n}Pella opens the page and recognizes the old broken wheel. She stands looking at it longer than Aivu expects. Then she asks whether Aivu is sure.{/n}
"Yes. I still know where everything is. And if I forget, you can show me when you come back. Or write about the bit I've forgotten."
{n}Pella thanks her and folds the picture carefully. Aivu's remaining papers feel thinner beneath her wing. She notices, shifts them once, and leaves the gift where she put it.{/n}''',
      c('[Keep Pella\'s address with the papers Aivu retains.]', flags=("aivu.pella_farewell_kept", "aivu.pella_original_picture"))),
], requires=("aivu.plant_care_agreed",), chapters=(5,), delay=48)


s("the_turn_the_commander_needs", "The turn the Commander needs",
  '"I could use your company today. Something quiet, if you do not mind."', [
    n("start", "Aivu", '''"I don't mind. I can be quiet. I can be lots of different sorts of quiet."
{n}She demonstrates for perhaps three breaths, then asks which sort you would like. The question is so earnestly meant that it almost makes you laugh.{/n}
{n}You leave the throne room together and find a place where you can sit without attracting an audience. Aivu brings no flags or false tails. She has a small length of string wound around one claw, which she unwinds and winds again while waiting for you to settle.{/n}
"I was going to ask about another game," {n}she says.{/n} "That can be another day. This is something else."
{n}She looks at the space beside you, judges how much room her wings need, and lies down where she will not crowd you.{/n}
"Do you want to tell me why, or do you want me to talk about something that isn't why?"
{n}The afternoon has no assigned task beyond that question. For once, Aivu seems willing to let it remain undecided until you answer.{/n}''',
      c('"I am tired of people expecting me to know what happens next."', "expectation"),
      c('"I keep thinking about people I could not help. I do not need you to make it better."', "grief"),
      c('"Tell me something ordinary. I would like to hear your voice without having to solve anything."', "ordinary"),
      c('"I thought I had time. I need to return later."', abort=True)),
    n("expectation", "Aivu", '''"I do that sometimes. Ask you what happens next."
"Sometimes I like being asked. Today I do not have many answers."
{n}She unwinds the string once, slowly.{/n}
"Then I know what happens next. We sit here. Then we can see."
{n}She says it without grandeur. The small certainty is surprisingly welcome.{/n}
{n}For a while she tells you about a leaf that has begun growing sideways from the cutting's stem. Pella's neighbor thinks it is reaching for the light. Aivu suspects it simply wants to be different from the other leaves. Both explanations fit what she has seen.{/n}
"I haven't decided which," {n}she says.{/n} "I'm allowed not to know yet. So are you."
{n}Then she stops talking and leaves you to watch the light move along the ground. When a question almost escapes her, you see her catch it. She makes a face at herself and tells you she will save that one for a day with more room in it.{/n}
{n}You thank her. She seems pleased by the plainness of the thanks, with no title attached to it.{/n}''', c('[Remain beside her for a little longer.]', "remember")),
    n("grief", "Aivu", '''{n}Aivu's claws stop moving along the string.{/n}
"I don't think I could make it better," {n}she says.{/n} "I wish I could."
{n}You choose how much to tell her. A name, perhaps, or a moment that keeps returning when other things grow quiet. She listens without trying to supply an ending you have not found.{/n}
"When somebody says a battle was good because we won, sometimes I want to ask good for who," {n}she says at last.{/n} "But I know what they mean. I just don't think it's all the things they could mean."
{n}She looks at you, uncertain whether she has spoken too much. You tell her you wanted her company, including her thoughts. She relaxes a little.{/n}
{n}A bird lands near the wall, then flies away before either of you has moved. Aivu watches it go.{/n}
"I can stay for a bit," {n}she says.{/n} "That's something I can actually do."
{n}You sit together. The conversation returns once or twice, then rests. When you do speak, she remembers the part you mentioned earlier and asks a small, specific question about it. You can answer, or say you would rather leave it there. She follows your choice.{/n}''', c('[Let the silence last as long as you need it.]', "remember")),
    n("ordinary", "Aivu", '''"The plant has a leaf growing sideways. That's very ordinary for a plant, but I've become interested."
{n}She tells you about Pella's neighbor checking the soil, a customer who tried to buy the painted monster instead of any herbs, and a pigeon that has claimed the shed roof as though its ancestors built the place.{/n}
"I told it we had done most of the work. It didn't care. Pigeons are worse than very important people. At least important people sometimes pretend to listen."
{n}You laugh, and she looks delighted. She settles back, rolls the string beneath a claw, and continues at the same unhurried pace.{/n}
{n}The pigeon has a rival. The rival may be the same pigeon after flying round the shed, but Aivu believes there are two because she disapproves of both in different ways. She has not decided whether to put either on a future map.{/n}
"They can earn it. By being somewhere interesting when I'm drawing."
{n}You listen without having to make a decision about pigeons. After a while the ordinary story wanders into a memory of a bird in Elysium, then back to the garden. Aivu lets it wander.{/n}''', c('[Listen until you begin to feel ready to rise.]', "remember")),
    n("remember", "Aivu", '''{n}Aivu sets down the string. She has made an uneven loop of it, large enough to fit around two claws.{/n}
"For the next game," {n}she says.{/n} "Or for tying something. It doesn't have to decide yet."
{n}She looks at you with the same direct attention she gives an unfamiliar creature.{/n}''',
      c('"You remember that I like making up the story. Today it helped to leave the story unfinished."', "story", requires=("aivu.commander_story",)),
      c('"You remember that I like to win. Today it helped that there was nothing to win."', "competitive", requires=("aivu.commander_competitive",)),
      c('"You remember that I am learning how to play. This was another thing I needed to learn."', "learning", requires=("aivu.commander_learning",))),
    n("story", "Aivu", '''"Unfinished isn't always abandoned," {n}she says.{/n} "Sometimes it's where you're sitting."
{n}She considers the phrase, then looks suspiciously pleased with herself.{/n}
"That was a good sentence. I'll probably forget it when I want it later. You can remind me."
{n}When you rise, she asks whether you want company on the walk back. You do. She leaves the string in her own keeping. Halfway back, she points out a small cloud that looks like a very cross turnip, and you stop together to see whether you agree.{/n}''',
      c('[Return together, leaving the afternoon without a grand ending.]', flags=("aivu.commander_company_kept",))),
    n("competitive", "Aivu", '''"We could have counted something and argued about who counted better," {n}she says.{/n} "But we didn't. Very restrained of us."
{n}The joke is gentle enough to sit beside what you told her. When you rise, she asks whether you would like company on the walk back. You do.{/n}
{n}She keeps the little loop of string and walks at the pace you choose. The next time she points out something interesting, she leaves room for you simply to look at it before asking what you think.{/n}''',
      c('[Return together without turning the rest into a contest.]', flags=("aivu.commander_company_kept",))),
    n("learning", "Aivu", '''"We can practice this too," {n}she says.{/n} "Only it shouldn't become a lesson. Lessons have people watching to see whether you're doing them properly."
{n}She gathers her string. When you rise, she asks whether you want company on the walk back. You do, and her tail lifts.{/n}
"Then I did think of the right question."
{n}She leaves it at that. On the way back you pass a patch of clear ground that might suit another game. Neither of you stops to plan it. There will be time to ask about that when you want an afternoon of a different kind.{/n}''',
      c('[Walk back with her at an easy pace.]', flags=("aivu.commander_company_kept",))),
], requires=("aivu.pella_farewell_kept",), chapters=(5,), delay=48)


s("a_reply_from_the_other_garden", "A reply from the other garden",
  '"There is a letter for you at the shed. Shall we read it together?"', [
    n("start", "Aivu", '''"For me? Not for you with something about me in it?"
{n}She accompanies you from the throne room with barely concealed impatience. At the shed, Pella's neighbor hands her a folded page delivered with an ordinary merchant's correspondence. Pella has reached her sister's garden. She has written Aivu's name on the outside herself.{/n}
{n}Aivu studies the name before opening the page.{/n}
"That's me. That's definitely for me."
{n}The letter describes the journey, a patch of stubborn soil, and the neighbor whose advice has become less confident since Pella asked him to demonstrate it. Aivu laughs at that part and asks you to read it again, although she followed the words the first time.{/n}
{n}There is a message about the picture she gave Pella.{/n}''',
      c('[Read about the new picture of the three of you.]', "new", requires=("aivu.pella_new_picture",)),
      c('[Read about the original garden page she gave away.]', "original", requires=("aivu.pella_original_picture",))),
    n("new", "Aivu", '''{n}Pella has hung the new drawing beside a window. Her sister recognized the cart, admired the dragon, and wanted to know why the Commander appeared to be losing an argument with a piece of paper.{/n}
"Because the paper had very good arguments," {n}Aivu says.{/n}
{n}Pella writes that she told her sister about the moving day and the game. She did not make the dragon more sensible in the telling. She thought Aivu would prefer to remain recognizable.{/n}
"I would," {n}Aivu says.{/n} "Mostly."
{n}She reads the paragraph again without your help. The picture has reached a place she has not seen, and someone there has looked at it long enough to ask a question. She spends a moment imagining exactly where the window might be.{/n}''', c('[Read the question at the end.]', "question")),
    n("original", "Aivu", '''{n}Pella's sister has spent a long time tracing the line between the garden's two homes. Pella writes that the stains on the paper made her remember things she had not meant to tell: the sound of the wheel fitting, the careful turn through the lane, and Aivu asking whether the garden came before the broken wheel or afterwards.{/n}
"It came after," {n}Aivu says.{/n} "The cart found another thing to do. That was a very important question."
{n}The old garden page now rests inside a cupboard door where it stays dry. Pella's sister looks at it when she fetches her gardening gloves. Aivu asks you to read that part twice.{/n}
"So it isn't just put away. She sees it."
{n}She touches the edge of the letter. Giving the page away has done something she could not watch happen, and the letter has let her see a little of it.{/n}''', c('[Read the question at the end.]', "question")),
    n("question", "Aivu", '''{n}Pella asks how the cutting is doing, whether the sign has survived the weather, and whether the great defender of the royal turnip has suffered any further defeats. She also asks what Aivu has found since they parted.{/n}
"I found out you can be tired without wanting to be alone," {n}Aivu says to you, then pauses.{/n} "That's your thing to tell. I can tell her about the plant instead."
{n}You thank her. She looks pleased, but does not make the thought into a larger discussion.{/n}
{n}The neighbor has spare paper. Aivu dictates an answer while you write: new leaves, the sign holding up, a pigeon whose authority remains disputed. She describes one game without making herself win every round.{/n}
{n}Then she asks to see the older page you have been keeping, the account intended for her family in Elysium. Its folds are still clean. No ordinary road from Pella's sister can carry that one where it needs to go.{/n}
"I want to keep it with me now," {n}she says.{/n} "When I can go home safely, or when we really have someone who can take it, I want to be the one who says what happens to it."
{n}You give it to her. She reads the opening and laughs at something she dictated before the sign, the new leaves, and Pella's reply became things she could tell someone about.{/n}''',
      c('"Would you like to add the parts that happened after we wrote it?"', "add"),
      c('"Keep that day as it was. You can tell another story beside it."', "beside")),
    n("add", "Aivu", '''"Yes. But the new bits go on another page. I don't want to squeeze the first day until it can't breathe."
{n}You take a fresh scrap. She adds the plant, Pella's departure, and the letter now lying beside you. She describes Pella's letter and the new leaf, then reminds you to add her question for her cousin about the leaf's sound.{/n}
"And I want to know what they did while I was doing all this," {n}she adds.{/n} "Not just whether they missed me. They must have done something."
{n}She ties the family pages together with her little loop of string. Pella's reply goes in a separate fold, with the address for answering it. One correspondence has a working road. The other remains a thing Aivu hopes to carry or send when there is a safe way.{/n}
"Don't let me say I have nothing to tell them," {n}she says.{/n} "I've got too much. That's a much better problem."''',
      c('[Leave the family pages in her keeping.]', flags=("aivu.letters_kept", "aivu.family_story_added"))),
    n("beside", "Aivu", '''"A second story. That might be better. The first one was very pleased with itself. I don't want to tell it it wasn't enough."
{n}She folds the old page carefully. On a new scrap, you write her account of the painted sign, the little plant, and Pella's letter. She insists that the pigeon be included, then reduces its part when you point out how much room it has claimed.{/n}
"It does that everywhere," {n}she says darkly.{/n}
{n}At the end she asks her family to send or tell her something ordinary when they next have a real chance to exchange news. She wants to hear the parts nobody would think to put in a tale of great adventures.{/n}
{n}She ties the family pages together with her loop of string. Pella's answer remains separate, with its known address and ordinary road. Aivu knows which letter can travel now and which still needs a safe opportunity.{/n}
"I can wait without pretending I've forgotten," {n}she says.{/n} "I'll probably complain while I wait. But I can wait."''',
      c('[Let her carry the pages she wants to share.]', flags=("aivu.letters_kept", "aivu.family_story_beside"))),
], requires=("aivu.commander_company_kept",), chapters=(5,), delay=96)


s("the_next_excellent_thing", "The next excellent thing",
  '"I kept the afternoon free. What would you like to do with it?"', [
    n("start", "Aivu", '''"I've got several ideas. One of them is sensible. I'm trying not to let it take over."
{n}Aivu has brought the false tails, the cloth turnip, and a fresh piece of chalk. She collected the turnip from your keeping when you arranged today's visit. There is no crowd waiting at the garden, although Pella's neighbor has agreed to watch a round from the shade.{/n}
"We could have another gathering later. Today I want to play with you. Not organize you. You're difficult to organize anyway."
{n}She uncoils the rope and checks that it will slip free when pulled. The cloth turnip has been mended along its frayed edge. Aivu points out the repair proudly.{/n}
"I asked for help with the stitching. I supplied the very important instructions about not changing its royal shape."
{n}The garden sign moves a little in the breeze. The cutting stands among the other pots, healthy enough to be unremarkable to anyone who does not know its earlier trouble. Aivu checks it once, finds it needs nothing today, and returns to the chalk circles.{/n}''',
      c('[Begin with the demonstration you planned together.]', "demo", requires=("aivu.demo_planned",)),
      c('[Give her the first turn, leaving the organizing aside.]', "company", requires=("aivu.company_requested",))),
    n("demo", "Aivu", '''{n}You demonstrate the game for Pella's neighbor, with Aivu playing the participant who has misunderstood everything. She tries to rescue the circle, steal her own false tail, and appoint the turnip to a higher office midway through the round.{/n}
{n}The neighbor laughs and says she understands. Aivu promptly becomes competent, which makes her much harder to catch.{/n}
"I was doing the mistakes on purpose before," {n}she reminds you.{/n}
"I had guessed."
"Just so you know. Some of them were very convincing."
{n}The first proper round is close. The second ends when you both stop to argue whether the turnip has crossed the line or merely looked over it. You agree on a rule and replay the last few steps. Aivu accepts the result, loudly, with a detailed account of how she means to defeat it next time.{/n}
{n}Pella's neighbor joins a stationary round, guarding one castle from the shade. Aivu discovers that the gardener has quick hands. She returns to you after losing her false tail and announces that the garden employs nothing but secret champions.{/n}''', c('[Rest by the wall when the round ends.]', "rest")),
    n("company", "Aivu", '''{n}Aivu takes the cloth turnip and makes you wait while she considers which castle is least defensible. You remind her that she is meant to defend it. She says she likes a challenge, then changes her mind when you take one very easy step toward her tail.{/n}
{n}The first round ends in laughter. The second takes more concentration. On your first attempt, you fool Aivu with a sudden turn. On the next, she watches your shoulders and catches the rope just before you reach the circle.{/n}
"I remembered! That's better than guessing. Except guessing feels more mysterious."
{n}Pella's neighbor joins a stationary round from the shade. Aivu could keep beyond her reach, but the temptation to make a face is still considerable. This time she makes it after reaching the castle. The gardener promises to remember for the next game.{/n}
{n}There are pauses in which nobody performs. You drink water, inspect a loose stitch, and discuss whether the chalk circle should move. Aivu lets the pauses remain pauses. When she asks for another round, she waits for your answer before carrying the turnip into place.{/n}''', c('[Rest by the wall after the last agreed round.]', "rest")),
    n("rest", "Aivu", '''{n}Aivu settles beside the folded flags. The papers for her family are tied safely inside a cloth, away from the cup of water. She pats the bundle once before turning to you.{/n}
"When I tell them about you, I don't want it to sound as if all I did was follow a very important person around. I did things. We did things. Different kinds."
{n}She looks toward the little plant.{/n}
"And some things kept happening when we weren't looking. I like knowing they're there."
{n}The afternoon has lasted long enough that the shade has moved across the chalk. Aivu gets up to gather the loose ropes, then sits down again, unwilling to finish before she has said something more.{/n}''',
      c('"I am glad we kept finding things to share."', "ordinary"),
      c('"I remember the story we made after you came back. We can keep making different sorts of days."', "rescue_story", requires=("aivu.rescue_story",)),
      c('"I remember watching beside you. I am glad you still tell me what company you want."', "rescue_watch", requires=("aivu.rescue_watch",))),
    n("ordinary", "Aivu", '''"Me too. I liked the terrible bits of the game. The pretend terrible bits. And the sign. And being able to ask you to sit down without having to find an adventure first."
{n}She considers whether that has sounded insufficiently adventurous.{/n}
"We can still have adventures. Lots. I just want these bits as well."
{n}You tell her which part you would like another afternoon for. She listens, then supplies a suggestion of her own. Neither of you has to turn it into an appointment immediately.{/n}
"There," {n}she says.{/n} "Now we know what we're looking forward to."''', c('[Help gather the game pieces.]', "keep")),
    n("rescue_story", "Aivu", '''"The people with the bad cake. I remember. They ought to have learned to bake by now."
{n}She smiles, then speaks more quietly.{/n}
"I still get scared sometimes. I don't want every good day to have to prove I don't. This one can just have been good."
{n}You agree. She taps the cloth turnip with a claw.{/n}
"This one had a very convincing vegetable. That should be enough for anybody."
{n}She asks which part you would like to do again. When you answer, she remembers a detail you mentioned in the Nexus and finds a place for it in an entirely different, much sillier story. The old afternoon remains recognizable without making this one repeat it.{/n}''', c('[Help gather the game pieces.]', "keep")),
    n("rescue_watch", "Aivu", '''"I still like knowing when people are going," {n}she says.{/n} "That hasn't stopped."
{n}She looks toward the lane, then back at you.{/n}
"But I don't have to watch every place all the time here. Sometimes I can look at the person I'm actually with."
{n}She demonstrates by staring at you with exaggerated concentration until you laugh.{/n}
"There. Very interesting. Much better than a buckle making mysterious noises."
{n}You ask what she would like to do another day. She suggests a place you have not explored, then admits she would also like another quiet rest by the garden. Both wishes seem comfortable beside her now.{/n}''', c('[Help gather the game pieces.]', "keep")),
    n("keep", "Aivu", '''{n}You wind the false tails while Aivu folds the cloth turnip. She leaves the chalk with Pella's neighbor so the clear patch can be used for games when you are away. The neighbor agrees to keep the running well clear of the plants.{/n}
"And no making the monster on the sign referee," {n}Aivu adds.{/n} "It looks very biased."
{n}She takes her family pages herself. The story is hers to carry when a safe journey becomes possible. She tucks the bundle snugly beneath a wing before gathering the last rope.{/n}
{n}At the lane's end, she stops and looks back at the garden. There is a painted sign, a cart that has learned to stay put in a different place, and a little plant that will need checking tomorrow. Then she looks forward again.{/n}
"I haven't decided the next excellent thing," {n}she says.{/n} "But I'd like you in it. If you'd like to be."
{n}Your answer makes her grin. She starts telling you about the sensible idea she mentioned at the beginning. It turns out to involve painting a picture indoors, where the weather cannot interfere, and making the dreadful creature considerably more ridiculous than before.{/n}''',
      c('"I would like that. Tell me about the creature on the way back."', flags=("aivu.trusted", "aivu.campaign_developed"))),
], requires=("aivu.letters_kept",), chapters=(5,), delay=48)


def ending(id, title, text, requires, forbids=(), owner="Epilogue"):
    SCENES.append(scene("aivu." + id, title, owner, 1, "", [n("start", "Narrator", text, portrait="Aivu")],
        requires=requires, forbids=forbids, Relationship="aivu", last=6))


NORMAL_END = ("aivu.closed", "aivu.absent", "aivu.detached", "devil", "swarm", "true_lich", "legend", "dragon", "sacrifice", "ascended")
ending("ending_garden_friend", "Places worth coming back to", '''{n}Aivu still wanted adventures. The Commander had never persuaded her to become a quiet dragon with sensible ambitions, and could hardly have claimed to want such a thing after helping defend a royal turnip. There were games to invent, places to explore, and unsuspecting people who had yet to appreciate the virtues of a particularly ridiculous painted monster.{/n}
{n}The friendship also had places in which nothing spectacular was required. Aivu could ask for company, be disappointed, enjoy herself, and tell the Commander when a plan had grown too large for the afternoon. She sometimes forgot what she had learned. She was considerably better at noticing when she wanted another chance.{/n}
{n}The garden remained part of Drezen while the people who tended it made journeys of their own. Pella's letters brought news when ordinary roads permitted. The plant continued to require water in amounts it could use, a demand that even a very important dragon had to learn to judge.{/n}
{n}When Aivu visited her family in Elysium, she had more than the great battles to tell them about. She took the pages she had kept and discovered that some of her best stories needed the Commander's foolish voice to be told properly. That supplied an excellent reason to return and practice them together.{/n}''',
    ("azata", "aivu.campaign_developed"), NORMAL_END)
ending("ending_afternoons_unfinished", "Another excellent idea", '''{n}The time the Commander and Aivu had shared did not become a finished map of their friendship. There were places they had not explored together and ideas that had not become afternoons. Aivu could remember what had happened without being made to remember the things they had only discussed.{/n}
{n}She still had opinions about what they should try next. Some were impractical. Some sounded ordinary until she explained them. When she found the Commander between greater tasks, she would begin with the important question: was there time to do something together?{/n}
{n}A later afternoon could answer that question. The earlier ones were reason enough to ask.{/n}''',
    ("azata", "aivu.started"), (*NORMAL_END, "aivu.campaign_developed"))
ending("ending_absence_unresolved", "The place where she should have been", '''{n}Aivu had not returned to the Commander's side. The absence was a fact the remembered afternoons could not alter. A joke she would have made might come to mind, or a place she would have wanted to inspect, and each would bring the missing dragon sharply into the present.{/n}
{n}Whatever had been shared before her disappearance remained real. It did not supply news of where she was now or make an unperformed rescue part of the story. Finding her still required finding her.{/n}''',
    ("aivu.started", "aivu.absent"), ("aivu.detached", "swarm", "devil", "sacrifice", "ascended"))
ending("ending_power_changed", "The distance between visits", '''{n}The power that had let Aivu accompany the Commander into danger no longer sustained that life. Their earlier friendship did not make the little dragon safe among enemies who could destroy her. Nor did it give the Commander a right to demand she remain merely because parting hurt.{/n}
{n}Aivu had wanted another meeting. The Commander could remember that wish alongside the things they had actually done together: her questions, her impatience, the ordinary pleasure of an afternoon she had chosen to share. A safe later visit would need its own opportunity. It could not be made real by repeating the old promise more loudly.{/n}''',
    ("aivu.started", "legend"), ("aivu.absent", "aivu.detached", "swarm", "devil", "sacrifice", "ascended"))
ending("ending_dragon_distance", "A friend remembered across a changed path", '''{n}The Commander's transformation did not preserve the old bond with Aivu simply because both could be called dragons. Her safety and place beside the Commander had depended on a particular power, and the new path could not silently stand in for it.{/n}
{n}The friendship that had actually grown between them still belonged to their history. There were questions Aivu had asked, things she had wanted to show, and afternoons in which being impressive mattered less than being together. A later meeting would need a safe way to happen, with room for the little dragon to choose what she wanted next.{/n}''',
    ("aivu.started", "dragon"), ("aivu.absent", "aivu.detached", "swarm", "devil", "legend", "sacrifice", "ascended"))
ending("ending_parted", "A voice no longer at the door", '''{n}The Commander no longer had Aivu's company. Earlier affection did not erase what had driven them apart, and a remembered joke was no substitute for hearing what the absent dragon would say now.{/n}
{n}Aivu had always been more than the help she could give or the delight she brought to a room. Her friendship could be hurt. The days already shared remained part of both lives, but they did not grant a right to resume as though nothing had followed them.{/n}
{n}Any future reconciliation would need to begin with the actual separation, and with a safe, voluntary chance to speak. That chance had not yet been made.{/n}''',
    ("aivu.started", "aivu.detached"), ("swarm", "sacrifice", "ascended"))
ending("ending_swarm_loss", "What the hunger could not keep", '''{n}The Commander's new existence could not be described as a continuation of the friendship Aivu had offered. Her voice, her questions, and the games she wanted to play belonged to the life before that choice. Hunger did not preserve her trust.{/n}
{n}The earlier afternoons remained events that had happened. They offered no gentler name for what came afterwards, and no living reunion could be written in their place without confronting that history.{/n}''',
    ("aivu.started", "swarm"), ("sacrifice", "ascended"))
ending("ending_sacrifice", "The next game without her friend", '''{n}The Commander's sacrifice left Aivu with the next things she had wanted to say. Great explanations for the victory could not answer those small unfinished invitations. She wanted her friend, and for a while wanting was all she could do.{/n}
{n}The free crusaders and the azatas who brought her home could offer company. They could not become the particular person she missed. In time there would be other games, other journeys, and people with whom she could laugh without forgetting.{/n}
{n}The afternoons she had actually shared with the Commander remained hers to remember. She did not have to make every memory brave.{/n}''',
    ("azata", "aivu.started", "sacrifice"), ("aivu.absent", "aivu.detached", "swarm", "devil", "legend", "dragon", "ascended"))
ending("ending_ascended", "A dragon's measure of importance", '''{n}Ascension gave the Commander's choices a reach Aivu could scarcely have imagined when she first asked for an afternoon. It did not retrospectively turn their ordinary days into preparations for divinity. She had wanted company, play, and someone who would answer her particular questions.{/n}
{n}Those were still the terms by which their friendship could be remembered. Whatever further meetings might become possible, they would have to include the dragon who could be delighted, cross, frightened, or simply busy with an idea of her own. Greater power did not make her earlier wishes too small to matter.{/n}''',
    ("aivu.started", "ascended"), ("aivu.absent", "aivu.detached", "swarm", "devil"))
ending("ending_rewritten", "A city never drawn together", '''{n}The rewritten world did not owe Aivu memories of the Commander's friendship. The afternoons they had shared belonged to a history whose circumstances had changed, not to a hidden obligation the new world must make her fulfill.{/n}
{n}Somewhere there might still be a curious little dragon with excellent ideas and very strong opinions about boring places. Her life would be her own. Any meeting in that life would have to begin as a meeting, without asking her to recognize a story she had never lived.{/n}''',
    ("aivu.started",), (), owner="AeonEpilogue")
