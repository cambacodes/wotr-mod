"""An authored living Chapter 3 Soana arc, not a native forest restoration.

The new shrine, hunter, curse and rites are alternate fiction in dialogue.
No existing scene, native outcome, actor, inventory or game statistic is changed.
"""
from story_format import c, n, scene

SCENES = []
ACTOR = "64805abb52739e44280a758f850b300c"
ANSWERS = "2b1776f3e398685479ff6b16290b4cc2"


def s(id, title, entry, nodes, previous, delay=24):
    for page in nodes:
        page["Portrait"] = "Soana"
    SCENES.append(scene("soana." + id, title, "Soana", 3, entry, nodes,
        Relationship="soana", Chapters=[3], last=3, ContactUnit=ACTOR,
        AnswerLists=[ANSWERS], RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", "soana.continuation_kept", previous),
        forbids=("soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman"),
        delay=delay, optional=True))


s("the_thing_in_the_sack", "The thing in the sack", '"You have company."', [
    n("start", "Soana", '''{n}A woman stands outside Soana's cave with a leather sack held away from her body. Her cropped hair is full of pine needles. A hunting bow hangs unstrung across her back.{/n}
"It said my name again," she tells Soana.
"Then stop answering it."
"I didn't answer. I told it to shut up."
"Pff! Perhaps it thanked you, too."
{n}Soana notices you and points to a bare patch of stone, well away from the entrance.{/n}
"Stand there. She has brought me something that ought to have stayed where she found it. I will not let it sniff at you as well."
{n}The woman puts the sack down. Its contents strike the stone with a hollow click.{/n}
"Meret," she says. "That's my name. If you hear anyone else say it, don't be polite."
{n}From inside the sack comes a second, softer click, although nothing has moved.{/n}''',
        c('"Tell me what happened before we open it."', "account"),
        c('"I cannot stay for this. Keep it covered until you have help."', abort=True)),
    n("account", "Soana", '''"She found a little shrine on a shelf above the stream," Soana says. "Three standing stones, a hollow beneath the middle one, and a warning she could not read. So she put her hands in the hollow."
"I can read enough," Meret objects.
"Enough to remove the bowl."
"It was a sound bowl. Someone could have used it."
{n}Meret crouches beside the sack without touching it.{/n}
"I thought the place was abandoned. Everything else was broken. I took the bowl, and that night someone called from the trees. My brother's voice. He has been dead twelve years. I knew it couldn't be him. I still went to the edge of the fire."
"Did you cross it?" Soana asks.
"No. It said something he used to say. But it said it twice, exactly the same, like a bird copying a whistle. I threw a branch."
"At the voice?"
"At where I thought the mouth would be."
{n}Soana almost smiles. Then the sack clicks again, and the moment passes.{/n}
"I have kept it wrapped since then," Meret says. "At first I thought I could put it back myself. When I took the path to the stream, I heard my own voice calling from ahead. I came here instead."
"At last, a hunter who walks toward help instead of another hole," Soana says. "Show me your hands."
{n}Meret holds them out. Soana looks beneath each fingernail, then releases her without explanation.{/n}''', c('"You know the shrine?"', "keeper")),
    n("keeper", "Soana", '''"I knew the woman who tended it. Before the Wound. There was no grand temple, no priest with a silver staff. A bowl of water for travelers. A place to leave the first mouthful before drinking."
"Who received it?"
"The thirsty dead, she said. Her grandmother had said it before her. Let scholars squabble over whose dead were thirsty. Something has been drinking there since. I want to see its mouth."
{n}She takes a stick and lifts the sack's mouth. Within it lies a shallow black bowl, its rim chipped in two places. A thin white crust marks the inside.{/n}
"There were offerings for the living as well. Water, a dry place to sit, news from the road. Nobody sings about carrying water or sweeping the shelf. Leave that work undone, and see what becomes of a holy place."
"And you helped tend it?"
"I spoke for its keeper when hunters wanted the shelf cleared. They said the stones crowded a useful trail. I said they could go around. They did. For a time."
{n}Meret's eyes narrow.{/n}
"My grandmother told me about that path. She also told me someone made the hunters swear never to take anything from the shelf."
"They wanted my protection for their camp," Soana says. "I wanted their hands kept off the stones. They kept their hands off my shrine. I kept their camp safe."
"And now you think the oath belongs to me."
{n}Soana does not look away from the bowl.{/n}
"You have carried away the very thing they promised to leave."''', c('"First we find out what is in it. Leave the old oath until then."', "test")),
    n("test", "Soana", '''{n}Soana sprinkles a little clean water on the bare stone beside the sack. Nothing happens. She moves the stick through the wet patch, then touches its end to the white crust inside the bowl.{/n}
{n}A dark line runs along the wood against the slope. Meret steps back. Soana drops the stick on the stone and covers the bowl again.{/n}
"Hungry," she says. "And able to follow what touches its dish. Do not give it blood. Do not give it a name to practice."
"Can it hear us?"
"Keep your tongue as though it can."
{n}The stick lies still. At its end, the wet wood has become pale and dry.{/n}
"It took the water," Meret says.
"Something did. We have not yet seen where it went."
{n}Soana takes a second stick and pushes the first into an empty stone hollow. She covers that with a flat rock, too.{/n}
"You asked why I looked at her hands. If she had scratched herself on that rim, it would have tasted her blood. Her hands are whole. Keep them that way."
{n}Meret looks at her own fingers again. She turns each hand over, examining the skin beside the nails.{/n}
"I didn't steal from a grave."
"I know," Soana says. "It stole a sound. Your brother is not rattling in that sack, child."''',
        c('"We should examine the shelf while it is light."', "terms"),
        c('"Can you contain it until we understand the shrine?"', "terms")),
    n("terms", "Soana", '''"For a little while. We will put the sack in a second hollow, on dry stone, with nothing living touching it. If it begins calling, nobody answers. If it begins moving, nobody tries to catch it in their hands."
{n}She speaks to Meret as directly as to you. Meret repeats the instructions without being asked, then adds one of her own.{/n}
"And if it uses my voice, you look for me before deciding I said anything."
"Yes," Soana says. "That too."
{n}Together you shift the sack using two long branches. Meret carries the covering stone. The work is awkward, but the bowl remains wrapped and no one touches its rim.{/n}
{n}When it is covered, Soana draws a line in the dust around the hollow. She deepens the line with the end of her stick.{/n}
"A line for your feet, not a ward. Step over it and you may lose a toe before you remember why it is there."
{n}Meret offers to sit watch. Soana sends her to sleep in the daylight instead, within calling distance but beyond the marked stone.{/n}
"I will hear it," she says.
"You cannot hear everything," you remind her.
"This is one bowl, hunter. Even you could keep an eye on it."
{n}After Meret leaves, Soana looks from you to the covered stone.{/n}
"I remember that shrine with clean water in it. Now its bowl rattles in a sack and steals dead men's voices. Curse the hands that left it so."
"I will bring thicker boots."
"Good. Then come back ready to walk, and spare me a speech about better days."''', c('[Agree to examine the abandoned shelf together.]', flags=("soana.bowl_contained",))),
], "soana.continuation_kept")

s("the_dry_offering", "The dry offering", '"I am ready to see the shrine."', [
    n("start", "Soana", '''{n}Soana has packed charcoal, a length of plain cord, and a small knife. Meret waits outside with an empty waterskin. The sack remains beneath its covering stone.{/n}
"It spoke once," Soana says. "It asked where the water had gone. It used no voice I recognized."
"Did you sleep?"
"Enough to resent being asked."
{n}She tests the end of her walking stick before setting off. Meret takes the lead, but Soana stops her at the first fork.{/n}
"The upper path."
"The lower one is shorter."
"The upper one lets us see the shelf before we stand on it."
{n}Meret changes direction. The climb is slow, broken by pauses that Soana uses to inspect the undergrowth. She identifies a place where a deer has rubbed bark from a sapling and another where rain has exposed roots. Neither interests her long. At a patch of dry moss, she kneels.{/n}
"Here. This is uphill from the bowl's hollow. It should still be damp."
{n}The moss crumbles between her fingers. Farther along, the same gray patch appears beneath an overhang sheltered from the sun.{/n}''',
        c('[Inspect the shrine and the traces of its offerings. Lore Religion DC 24.]', check=dict(Skill="SkillLoreReligion", DC=24, Success="read", Failure="wrong")),
        c('"Let Meret show us every place she stopped with the bowl. We can compare them."', "patient"),
        c('"We should return when we can give this our full attention."', abort=True)),
    n("read", "Soana", '''{n}The stones carry a shallow carving: an open hand beneath three falling drops. The offering hollow is below the hand, where water once overflowed onto the shelf. Someone has cut a second groove above it. The newer cut closes the hand around a small circular shape.{/n}
{n}You explain the change. A gift left to pass onward has been redrawn as something held. The white crust follows the newer groove but does not extend into the older one.{/n}
"So it did not merely crawl into a forgotten bowl," Soana says. "Someone altered the invitation."
{n}Meret crouches without crossing onto the shelf.{/n}
"Recently?"
"Not recently enough for the knife marks to be clean," you answer. "That is all I can tell from here."
{n}Soana passes you the charcoal. You take a rubbing of both cuts on a scrap of cloth, keeping your fingers clear of the crust.{/n}
"Someone made this cut," she says. "Find the edge of a cut and you can close it. Give me the charcoal."
{n}She studies the closed hand, her own fingers tightening around the stick.{/n}
"I drove hunters away from these stones. Then I let the path grow over. Now something else drinks here. Do not pat my shoulder about it."
{n}With the altered groove identified, you can keep to the clean side of the shelf while examining the hollow. You find a clear strip of stone beneath the lip, enough to anchor a temporary seal without touching the new carving.{/n}''', c('[Mark the clean strip on the rubbing.]', "paths")),
    n("wrong", "Soana", '''{n}You recognize the open hand and take the newer circular cut for a worn offering mark. When you reach toward it with the charcoal, the dust gathers against the slope. A dry rasp comes from inside the stone.{/n}
"Back," Soana says.
{n}You withdraw. The charcoal breaks between your fingers. Half of it falls onto the shelf and turns white.{/n}
{n}For a moment everyone waits for something worse. Nothing follows. Meret lets out a breath through her teeth.{/n}
"That part is newer," Soana says. "And it wanted what you brought. Keep your fingers out of it, bloody hunter."
"I read it wrongly."
"Yes. Now we know one part of the answer at the cost of charcoal. Cheap schooling. Keep what you learned."
{n}The direct approach is no longer worth risking. You move back along the path and compare the dry patches with the places Meret rested. It takes most of the afternoon. At each stop she has to decide whether she truly remembers putting the sack down or merely thinks this looks like somewhere she would have stopped.{/n}
{n}By the time the pattern becomes clear, Soana is leaning heavily on her stick. You return to the cave for food and rest before finishing the comparison in the morning. At sunrise Meret brings the waterskin, and you take the upper path again.{/n}''', c('[Complete the slower survey with them.]', "survey")),
    n("patient", "Soana", '''{n}Meret walks the route again, stopping where she rested with the sack. Sometimes she is certain; sometimes she argues with her own memory. You mark only the places she can identify by more than a familiar-looking tree.{/n}
{n}At two of them the moss beneath the sack has dried. At a third, bare stone shows no visible change. Soana pours one drop from the waterskin onto each patch, then watches without touching it.{/n}
"You can sit while we wait," Meret tells her.
"My knees have told me."
"Then sit. If you fall into the water, I shall have two things to haul out."
{n}Soana gives her a hostile look and sits. Meret bends over the wet moss.{/n}
{n}The comparison takes the afternoon and part of the following morning. You return to the cave to sleep between observations. The marks on your cloth grow crowded. Two patches dry; the fern beside them stays wet.{/n}
"If you tell this to anyone," Soana says, "tell them we sat on damp rocks until our backs ached. They will want a tale of thunder and spirits. Let them sit here first."
{n}When you return to the shelf, she has a different question to put to the altered stone.{/n}''', c('[Compare the survey with the shrine.]', "survey")),
    n("survey", "Soana", '''{n}The drying follows contact with the sack, not Meret's footprints. A damp fern she brushed on the way past remains green. The moss on which she rested the bowl has withered.{/n}
"It travels with its dish," Soana says. "It can call beyond it. It cannot drink every drop of water it can see."
{n}At the shrine, she uses a long twig to lay a thread across the edge of the newer carving. The thread stiffens. A second thread, laid below the old open hand, remains loose.{/n}
"Two workings," she says. "The old invitation and something that closes it. Whoever cut that second line wanted to keep what came. Or wanted what came to keep feeding."
{n}You take a rubbing from the clean side, using the long stick to hold the cloth against the dangerous part. It is clumsier than working by hand, but the lines are legible.{/n}
{n}There is a clear strip beneath the hollow's lip. Soana marks it on the cloth. It may hold a temporary seal while you deal with the dish.{/n}
"I do not know who changed it," she says. "Some living hand cut this. Do not blame a dead keeper because we cannot find the knife."''', c('[Ask where the thing can be made to go.]', "paths")),
    n("paths", "Soana", '''"There are two ways I would attempt," she says. "Neither leaves us with clean hands and nothing lost."
{n}She points uphill, toward a sheltered strip of young trees.{/n}
"The old path to the dry ridge passes through my nursery. I have watered those seedlings through three summers. If we lay the bowl's trail through them, the thing can be drawn to bare rock and shut away from the stream. It will drink what it touches on the way. I expect to lose the young trees."
"And the other way?"
"Someone can carry an invitation instead of laying one on the ground. A voice, offered deliberately, with the bowl sealed at the end of the calling. It would have a road for one night. We would close it before dawn."
{n}Meret's jaw sets.{/n}
"Mine. That is what you have been working toward."
"You already answered it once," Soana says. "It knows where to listen."
"That isn't the same as my offering."
"No. But it knows your tongue already."
{n}Meret folds her arms. Soana plants her stick in the path. Behind her, the nursery fence creaks in the wind.{/n}
"We discuss this with the bowl covered," Soana says. "I will not let that thirsty filth listen while we quarrel over my trees."''', c('[Return by the upper path with the rubbing.]', flags=("soana.shrine_examined",))),
], "soana.bowl_contained")

s("the_inherited_debt", "The inherited debt", '"Who carries the voice? We have not settled that."', [
    n("start", "Soana", '''{n}Meret has laid three things outside the cave: her hunting knife, a small purse, and a strip of leather bearing a family mark. Soana stands over them without touching any.{/n}
"I can give you the knife," Meret says. "I can give you what is in the purse. I cannot give you my grandmother's obedience. Her bones are in the ground."
"Keep the knife. You will need it more than I will."
"And the money?"
"Will it water a tree?"
"It might buy a pair of hands to carry water."
{n}Soana looks toward you as you approach.{/n}
"A merchant's tongue on a hunter. Shall we count coins while the roots dry out?"
"It was an offer," Meret says. "I came to you instead of leaving the cursed thing beside someone else's camp. You might remember that part."
{n}The leather strip bears a crude deer with a forked antler. Soana recognizes it. She touches the forked antler with a finger, then pulls her hand back.{/n}
"Your grandmother wore that at her belt."
"She gave it to me. Not to you."''',
        c('"Tell me what the old agreement actually required."', "oath"),
        c('"I will return when we have time to settle this properly."', abort=True)),
    n("oath", "Soana", '''"They kept the shelf clear of traps. They left the bowl and stones untouched. In return, I showed them which paths would hold after rain, and where the animals could be taken without stripping a hollow bare. When something came down from the dark places, I warned them."
"You did more than warn them," Meret says quietly.
{n}Soana looks at her.{/n}
"My grandmother said you stood outside their camp all night once. She never said what you were keeping away. She said she woke and saw you still there."
"She should have slept."
"She said that too."
{n}For a little while the two women look at the worn leather rather than each other.{/n}
"You kept her camp safe," Meret says. "You will not drag me into this working by her belt."
"And you took the bowl from the stones that kept her safe. Your own hands did that."
{n}Meret turns the worn leather over in her hands. Soana follows the movement, then looks away before the younger woman can catch her watching.{/n}
"Would you have helped her if she had no mark?" you ask.
"I have already helped her," Soana answers. "The thing is beneath my stone. My trees stand on the road to the ridge. It will be my water it drinks while you two argue."''', c('[Ask what carrying the voice would mean in practice.]', "price")),
    n("price", "Soana", '''"One person calls the thing along a prepared road," Soana says. "The words are an invitation to follow the sound, nothing more. No promise of a body. No promise to feed it. The speaker must remain awake and must not answer when it begins using other voices."
"For how long?"
"Until the bowl is sealed. Perhaps hours. If the speaker loses the words, we break the line and carry the dish to the nursery road instead. That is the escape. I will prepare both roads."
{n}She looks directly at Meret.{/n}
"It will hear what is near the surface of your thoughts. It may use your brother again. Afterwards, for a few nights, you may hear his voice when there is nobody there. I cannot promise you will sleep easily. If the voices come afterwards, they are scraps it has left behind. Do not follow them into the trees."
{n}Meret rubs the back of her neck. She looks toward the covered stone and bites the inside of her cheek.{/n}
"Will it keep him?"
"It has never had him. A stolen sound is not your brother."
"Easy to say when it isn't speaking."
"Yes," Soana says. "That is why I am saying it now."
{n}She kneels slowly and pushes the knife and purse back toward Meret.{/n}
"Keep your knife and your purse. They cannot call it. That is the working, and that is what it will do to the caller."''', c('"What if you carried the voice, Soana?"', "her_price")),
    n("her_price", "Soana", '''"Then it would have a great deal of filth to spit back at me."
"Can you do it?"
"Yes, child. I heard you the first time."
{n}She braces a palm against the wall and gets to her feet. Dust falls from beneath her fingers.{/n}
"You close the bowl when I give the word. Meret watches the escape line. Neither of you leaves your stone for a cry in the trees. Not a child's cry, not mine. Especially not mine."
"And afterwards it is you who hears the voices."
"My ears still work. You have tested them thoroughly."
{n}She looks past you, toward the nursery fence.{/n}
"Those trees will outlive us if something does not drink them first. There will be shade there. Birds. Perhaps some fool asleep beneath the branches, with no notion who carried the water. I want that forest. A few sleepless nights will not kill me."
"My grandmother is still not speaking through my mouth," Meret says.
"Pff! Neither is mine. Spare me another telling."
{n}Soana picks up the strip of leather, turns the deer upright, and puts it back beside Meret's purse.{/n}
"I will call it. You two hold your places. When it begins whining in a stolen voice, remember what is under that rock. A thirsty thing with a bowl for a belly. Nothing more."''',
        c('"Keep the nursery. Call it, and we will hold the lid and the escape line."', "voice"),
        c('"Use the ridge road. I would rather help you plant again than give it your memories to imitate."', "ridge")),
    n("voice", "Soana", '''{n}Soana makes you recite the movements for closing the bowl. Meret repeats hers, then points to the escape cord.{/n}
"Where do I stand if we break the line?"
"Outside the turn. Get between the bowl and the ridge and it will drink through you."
"Show me."
{n}You walk to the bare stone where the working will end. Soana puts down three pebbles. Meret moves hers a little to the left, then crouches and looks toward Soana's stone.{/n}
"There. I can see your mouth and the dish. If it calls out with your voice, I will know which mouth moved."
"Keep looking, then. And no brave leaps into the middle of the cord. The forest has enough dead fools in it."
{n}On the way back, Soana stops at the nursery fence. The saplings stand in uneven rows. One has pushed a new green shoot through a split in its bark.{/n}
"Look at that one. I thought the frost had finished it."
"It proved you wrong."
"It had better keep doing so."
{n}She hooks a wandering stem back behind the fence with a finger. A drop of water hangs from its tip and wets her sleeve. She leaves the sleeve wet.{/n}''', c('[Set the night and mark where each of you will stand.]', flags=("soana.rite_voice",))),
    n("ridge", "Soana", '''{n}Soana stares toward the nursery. Meret gathers the knife, purse and leather strip, buckling them back at her belt.{/n}
"You think a sack of seed will mend this?" Soana asks.
"No. I think I would rather carry water with you next summer than hear that thing calling with your voice."
"Three summers already. Buckets when the stream ran low. Shade dragged over the youngest shoots. And still some died."
"I heard you."
{n}Her jaw works. Then she plants her stick in the dust.{/n}
"The ridge. We will clear the road before sunset. Do not stand there looking as though you have won something."
"I can bring seed from the eastern slope," Meret says. "The cones there are sound."
"A handful of cones is not a forest."
"It is a handful of cones. I said seed."
{n}Soana snorts, but leads you down the proposed road. You mark the turns where damp cord will draw the thing uphill, and the bare rock beyond which it must not spread.{/n}
{n}A low branch hangs across the nursery gate. Soana cuts it off, checks the leaves, and tucks the green piece inside her sleeve. She shuts the gate with more force than it requires.{/n}''', c('[Agree on the road and the night of the working.]', flags=("soana.rite_ridge",))),
], "soana.shrine_examined", delay=24)

s("a_voice_in_the_dark", "A voice in the dark", '"Is everything ready for the working?"', [
    n("start", "Soana", '''{n}Soana meets you before sunset. She has tied back her hair and fastened her sleeves close to her wrists. Meret carries the sack between two forked branches, keeping it clear of her clothing.{/n}
"We begin while we can still see the ground," Soana says. "I will not have you tripping over the cord and blaming the dark."
{n}The path to the bare stone has been cleared of loose branches. A shallow groove cut in packed earth leads toward the nursery and then the ridge. Soana has laid damp cord in it, but left a gap near the sack. A flat lid and a wedge of clean clay wait on the stone.{/n}
"The clay closes the dish," she explains. "I copied the old open hand onto this lid. It draws the thing's reach outward while we close the mouth it drinks through. When the bowl is empty, press the lid down and turn it to seat the clay against the rim. Afterwards we fill the newer cut on the shrine stone. Two openings. Both must be shut."
"And if it reaches the stream?" Meret asks.
"Then we have failed. That is why we brought it uphill, and why the wet road leads farther from the water."
{n}Soana has each of you mark your position with a pebble, checking that Meret can see both her mouth and the bowl. You kneel by the lid. The three of you rehearse the movements with an empty wooden cup; then the real bowl comes out of its sack.{/n}
{n}The air above it shivers, though the evening is still. A smell of old dust fills your mouth.{/n}''',
        c('[Take your agreed place while Soana prepares to carry the voice.]', "voice", requires=("soana.rite_voice",)),
        c('[Check the wet road toward the ridge.]', "ridge", requires=("soana.rite_ridge",)),
        c('"Not tonight. We should cover it and wait until we are ready."', abort=True)),
    n("voice", "Soana", '''{n}Soana stands beyond the bowl, with the nursery behind her and open stone at her feet. She speaks a short phrase in a language Meret does not know, then repeats its meaning for you both.{/n}
"Follow the sound. Take nothing beyond the sound. Leave when the sound is ended."
{n}Soana repeats the words three times. On the third, the leaves behind her begin to rustle. No wind touches the nursery.{/n}
{n}A child's laugh comes from behind the trees. Meret flinches. Soana does not turn.{/n}
"Follow the sound."
{n}The laugh becomes a cough. Then a man's voice asks whether the water is ready.{/n}
{n}Soana's next breath catches. She puts one hand against her ribs and continues. Her mouth stays open over the next word. Then she forces it out.{/n}
{n}The white crust loosens from the bowl's inner wall. It gathers in the center like fine ash stirred by an invisible finger. Beneath it, for the first time, you see the dark glazed bottom.{/n}
"Not yet," Soana says between repetitions.
{n}You keep your hands on the lid. Meret watches Soana's mouth. The voice behind the trees says the same question again, in precisely the same tone.{/n}
"It cannot make a conversation," Soana says, her eyes on the bowl. "It can only steal one side."
{n}Then it uses her own voice, younger and furious, ordering someone to leave the spring. Her face goes pale.{/n}''', c('[Keep your place and watch for her signal.]', "strain")),
    n("strain", "Soana", '''{n}One pale thread still clings to the rim. Soana's voice scrapes in her throat. Meret takes hold of the dry end of the escape cord, keeping it clear of the bowl.{/n}
"I am not finished."
{n}The stolen voice quarrels on behind Soana. You hear only one side. She lifts two fingers, the signal to hold the lid ready. Her hand shakes, but the fingers stay raised.{/n}
"A little longer."
{n}The thread stretches toward her across the bare stone. Its end trembles in the air. The nursery road lies beyond the gap in the cord, wet and ready.{/n}
{n}Soana follows your glance toward Meret's hand.{/n}
"Watch the rim, hunter. I can hear it. I can still count to two."
{n}Behind her, the younger voice spits another accusation. Soana bares her teeth and repeats the calling words. Meret shifts her grip on the cord; her eyes flick from the white strand to the lid.{/n}''',
        c('"Your fingers are raised. I will hold until you give the word."', "held"),
        c('"Break the line. Send it to the ridge before it reaches you."', "broken")),
    n("held", "Soana", '''{n}You keep the lid steady. Soana closes her eyes for one breath, opens them, and speaks the phrase again. This time she does not compete with the voice behind her. She gives the words slowly, each one distinct.{/n}
{n}The pale thread lifts from the rim. The bowl is empty.{/n}
"Now."
{n}You press the lid down and turn it through the half-circle she marked. Clay squeezes into the seam between lid and rim. Meret draws the dry escape cord away before any loose thread can find it.{/n}
{n}The voice stops in the middle of a word. Soana's lips move once without sound. She sways, catches herself with her stick, and remains standing.{/n}
"Again," she says.
{n}You ask what she means. She stares at the sealed bowl, then shakes her head.{/n}
"Nothing. It had already stopped. I was still listening."
{n}Meret puts a cup of water into Soana's hand. Her first swallow hurts. The second goes down more easily.{/n}
"The trees?" she asks.
"Untouched," Meret says.
{n}Only then does Soana sit. Her hand remains around the cup so tightly that you can see the pressure in her knuckles.{/n}
"Do not congratulate me yet. We have a bowl to bury in dry stone, and a shrine whose invitation must be closed. This was the loud part. There is work after it."''', c('[Stay through the remaining work and the return to the cave.]', flags=("soana.nursery_saved", "soana.voice_carried", "soana.working_done"))),
    n("broken", "Soana", '''"I told you to wait!"
{n}You lower the lid without turning it. Meret joins the wet cord to the bowl's base. Soana breaks off the calling words and steps sideways onto clear stone.{/n}
{n}The pale thread drops into the damp groove. It runs uphill faster than water, bleaching the cord behind it. Leaves fold in the nursery as though struck by frost.{/n}
{n}Soana watches until it reaches bare rock. Then she comes to your side, presses two fingers to the lid and shoves your hand toward the mark.{/n}
"Turn. Keep it level, curse you!"
{n}Clay squeezes into the seam. The last strand vanishes beneath the seal, and Meret pulls the dry end of the cord free. The trees are silent.{/n}
"You heard my signal."
"I did."
"Then do not say you mistook it."
"I won't."
{n}Soana walks to the nursery. The nearest sapling has lost every leaf. She touches its stem with the back of her hand. It breaks under the touch.{/n}
"Three summers," she says.
{n}She drops the broken stem at your feet and takes up her stick.{/n}
"Bring the clay. The shrine is still open. I will not leave a second mouth for it to drink through while we stand here quarrelling."''', c('[Finish sealing the shrine. You broke the line against her word.]', flags=("soana.nursery_lost", "soana.voice_interrupted", "soana.working_done"))),
    n("ridge", "Soana", '''{n}You follow the damp cord with your eyes, checking that no end trails toward the stream. Meret kneels at the gap. Soana holds the bowl level with the forked branches.{/n}
"Join it."
{n}Meret lays the final length in place. Soana tips one spoonful of water into the bowl. The surface goes still, then rises into a thin point.{/n}
{n}A voice asks Meret to come closer. She steps away instead.{/n}
"No," Soana says to the bowl. "There is your road."
{n}She lifts one branch and tilts the dish toward the wet cord. Something pale runs over the rim. It follows the damp thread uphill, pausing at each knot as if tasting it.{/n}
{n}When it reaches the nursery, the first sapling bends. Its leaves curl inward. A second follows, then a third. Soana's grip tightens, but the bowl remains level.{/n}
"Watch the dish," she tells you.
{n}You had been watching her. You return your attention to the rim, where the last pale strand is thinning. The movement toward the ridge draws it out slowly. Meret holds the dry end of the cord, ready to separate the road once the seal is closed.{/n}
{n}A branch snaps in the nursery. Soana does not turn.{/n}
"Now."
{n}You lower the lid and turn it through the marked half-circle. Clay fills the seam between lid and rim. Meret draws the loose cord away. The strand on the ridge contracts and disappears beneath the stone's edge.{/n}
{n}Silence follows. Soana sets the branches down and walks to the trees. She stops beside the smallest one, touches a curled leaf, and lets it fall.{/n}
"The road held," she says when Meret approaches. "I saw it."
"So did I," Meret says.
{n}Meret stands beside her without touching the tree. After a while Soana returns to the sealed bowl.{/n}
"We close the shrine before we rest. I do not intend to pay twice because I was tired after the first payment."''', c('[Help close the old invitation and secure the sealed bowl on dry stone.]', flags=("soana.nursery_lost", "soana.ridge_used", "soana.working_done"))),
], "soana.the_inherited_debt", delay=48)

s("what_followed_home", "What followed home", '"I came to see what the working left behind."', [
    n("start", "Soana", '''{n}Meret sits outside the cave, cutting the damaged cord into short lengths. She lays each piece on bare stone. Soana sits farther inside, beyond the sunlight.{/n}
"The bowl is sealed," Meret says. "We checked at dawn. The stone around it is dry. Nothing has called from the shrine."
"And here?"
{n}Meret glances into the cave. Her knife stops against the cord.{/n}
"Ask her."
"My tongue has not fallen out, hunter," Soana calls. "You can ask me yourself."
{n}You step inside. There is no cup by your usual stone. Soana's walking stick lies across her knees, both hands gripping its worn head. She follows you with her eyes.{/n}''',
        c('"Tell me how the night was."', "voice", requires=("soana.voice_carried",)),
        c('"I broke the line. Tell me what happened afterwards."', "interrupted", requires=("soana.voice_interrupted",)),
        c('"Have you been back to the nursery?"', "lost", requires=("soana.ridge_used",)),
        c('"I can return when you want company."', abort=True)),
    n("voice", "Soana", '''"Three times I heard him ask for water after I lay down. Then I dreamed I had answered. I got up and kicked the fire apart. There was nothing in it."
{n}She looks toward the cave mouth.{/n}
"Corven. That was his voice. I hope you were watching the bowl instead of trying to put a name to it."
"I watched your signal."
"Good."
{n}She swallows and presses her fingers against her throat.{/n}
"He had carried water for half the village that afternoon. When he asked for ours, I told him to wait. I was busy. Always busy."
"Why did it take that memory?"
"Ask the thing under the rock. Perhaps it liked the sound. I will not bow to a bowl of dust because it can spit my husband's words at me."
{n}Her stick strikes the floor. Outside, Meret's knife stops, then resumes.{/n}
"The trees are green. I went and looked before sunrise. I would do it again. Curse the thing and its borrowed tongue."
"Will you sleep tonight?"
"Meret sat outside until I slept this morning. She is going back to her camp before dark. I sent her."
{n}She knocks the foot of her stick against the stone beside her.{/n}
"Sit there a while. Talk if you have something to say. And if I fall asleep, do not wake me to ask about it."''', c('[Sit on the stone beside her.]', "visitors")),
    n("interrupted", "Soana", '''"The trees. All those nights carrying water. And now I must find someone who can hold a lid without deciding he knows better than the shaman."
{n}Her hands tighten on the stick.{/n}
"I saw your signal. I broke the line anyway."
"Yes. You did."
{n}Meret's knife stops outside. The loose end of the cord scrapes over stone as she draws another length toward her.{/n}
"Were you afraid? So was I. The thing had Corven's voice. Do you think I did not hear it?"
"I thought it would take you."
"And I thought I could draw it clear. My trees are dead now. You may congratulate yourself on my breathing if you like. Do it somewhere else."
{n}She turns toward the nursery path. A patch of morning light falls across her mouth.{/n}
"If there is another working, someone else holds the lid. You can carry the clay. You did that well enough."
"I will carry it."
"You will carry buckets first. Meret has brought seed."
{n}She lifts the stick off her knees and leans it against the wall. With her foot she nudges a loose stone away from your seat.{/n}
"Sit down. You can be a fool on your feet or a fool beside me. I am tired of looking up at you."''', c('[Sit. Someone else will hold the lid next time.]', "visitors")),
    n("lost", "Soana", '''"At first light. I counted them. Then I counted again, as though one might have hidden behind another."
{n}She pulls the green branch from her sleeve. Its leaves droop, but none have curled white like the leaves on the trees.{/n}
"I cut this before we began. Look. Still green. A poor forest to fit inside a sleeve."
"Meret offered seed."
"She brought it. Sound seed. I will plant when the ground has had rain."
"You sound surprised."
"No. Angry. I know how to plant a tree, child. I have no wish to spend another three summers learning the same lesson."
{n}She turns the branch toward the light, then scrapes a thumbnail along the bark. Green shows beneath.{/n}
"The road held. The stream is untouched. That is what we went there for. Do not tell me to smile about the rest."
"Would you use the ridge again?"
"Bring me that question when there are leaves on the new trees. Today, bring water."
{n}She lays the branch beside the cup and draws her skirt clear of the stone where you sit.{/n}
"But sit first. I have been counting dead saplings since sunrise. You can hear the count once, at least."''', c('[Sit beside her and the green branch.]', "visitors")),
    n("visitors", "Soana", '''{n}Meret brings the cut cord to the entrance. The clean pieces lie apart from those that touched the bowl.{/n}
"I will burn these on the bare ridge. I won't leave them for something to chew."
"Good."
"I will look at the eastern paths after rain, too. When I am here. The deer mark stays on my belt; I am doing this with my own feet."
{n}Soana looks at the leather strip, then at the hunter's muddy boots.{/n}
"Look beneath the overhang. Stones come loose there after heavy rain."
"I know."
"Then I shall be spared telling you twice."
"You told me yesterday."
{n}A dry laugh catches in Soana's sore throat. She coughs and waves Meret away.{/n}
"Go, bloody hunter. Before I find something else for you to know already."
{n}Soana watches until the bow on Meret's back disappears among the trees.{/n}
"Her grandmother had a tongue like that."
"You said she was less troublesome."
"She is not here to contradict me. Let the dead be useful for something."''', c('[Ask what becomes of the old agreement.]', "old")),
    n("old", "Soana", '''"Their oath is old. It was not nothing. I stood between their camp and things that would have emptied it by morning."
"Meret knows."
"Then she can keep the shelf clear when she walks that way. I shall not put a bowl back there."
{n}Soana rubs charcoal dust from one finger. A black streak remains beside the nail.{/n}
"Water for the thirsty dead. That was what the keeper called it. We left the first mouthful and drank the rest. Now look what has come to drink."
"What will travelers do?"
"Carry water. Ask a living person if their skins run dry. The shelf is shut, and it stays shut. I will not feed the forest to a memory of how things were done in Sarkoris."
"And the forest's guardian?"
{n}Her finger stops against the charcoal stain. She looks up sharply.{/n}''',
        c('"Orso remains bound. This has not freed him."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
        c('"Orso remains dead. This has not replaced him."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"No. Orso is still bound. You saw the knot. A bowl buried on the ridge has not loosened it."
"I know."
"Remember it when you are pleased with me. I will not watch my forest die so that hunters can praise my clean hands."
{n}She looks toward the path Meret took. A leaf drifts across the cave mouth and sticks against a wet stone.{/n}
"One hungry thing shut away. That is what we have done. The stream can run. Those saplings can put out leaves. Orso still carries what I bound to him."
"I have not forgotten."
"Good. Do not start telling people I have freed him. I would have to correct you, and you already hear enough of my tongue."''', c('[Stay. The shrine is sealed; Orso is another matter.]', "end")),
    n("dead", "Soana", '''"No. Sometimes I still listen for his feet among the trees. There is nothing."
{n}She rubs her thumb across the other hand, then closes both into fists.{/n}
"I am searching for another guardian. Sitting beside me will not stop that. Nor will kissing me, if that is the grand stratagem you have brought."
"I know you are searching."
"Then keep knowing it. Hunters grow deaf when they think they have tamed something."
{n}She looks toward the path to the closed shelf.{/n}
"We shut that mouth without putting it inside an animal. I saw it. I will remember how. But the forest is larger than one cursed dish, child, and I will not leave it undefended while I wait for a gentler spirit."''', c('[Stay. The shrine is sealed; Orso is another matter.]', "end")),
    n("end", "Soana", '''{n}The afternoon passes. Nothing calls from the covered stone. Soana opens her mouth once, shuts it, then points toward the eastern slope.{/n}
"The wind has turned. It will be cold there tonight."
"I heard."
{n}She pulls her shawl tighter. Before you leave, she puts a hand on your sleeve.{/n}
"Come back when the cord is burnt and the clay has dried. There is something else. I have let a bowl and two hunters keep my tongue busy long enough."
"I will come."
{n}Her hand drops. Beside the cup, the green branch casts a thin shadow over a scrap of bark.{/n}''', c('[Tell her you will come back.]', flags=("soana.aftermath_heard",))),
], "soana.working_done", delay=48)

s("a_promise_still_spoken", "A promise still spoken", '"You wanted to finish a conversation."', [
    n("start", "Soana", '''{n}A strip of bark lies on Soana's lap. Charcoal words crowd one end. The other bears a black smear where she has rubbed the writing out.{/n}
"A letter," she says. "I have worn a hole in it arguing."
"To Corven?"
"Who else? No, I have nowhere to send it. Put away that mournful face."
{n}She turns the bark over. The blank side leaves a charcoal print on her skirt.{/n}
"He used to let me have the last word. Sometimes he would come back with it the next morning, when I had quite finished being right. I have had a great many last words since then."
{n}She lays the bark beside her cup.{/n}
"No grave. No message. I know no more today than yesterday. But you are here, and I am tired of talking to a piece of bark."''',
        c('"Speak. I am listening."', "choice"),
        c('"I cannot stay today. I will come back to hear you."', abort=True)),
    n("choice", "Soana", '''"Corven put flowers on my head. I became his wife. I did not think there would come a day when I could not find him, or even learn whether he was alive."
{n}She brushes a black fleck from her skirt. It smears under her thumb.{/n}
"If he came up that path tomorrow, he would find me here. I would tell him about you. He might curse me. He might sit down and ask for water. I do not know."
"You have thought about his return."
"Often enough. I hear a foot on the path and look up before I can help it. Then some hunter appears with a broken snare or a thorn in his hand."
{n}She picks up the bark, holds it by its unmarked edge, and puts it down again.{/n}
"I remember the flowers. The bonfire. The mead on his beard. I will not tear those things out to please you."
"I have not asked you to."
"Then hear the rest. I want you here. I want your hand on mine, if you still want to give it. Corven has not answered me. Perhaps he never will. There. No wreath, no clever words to make it tidy."''', c('[Answer her.]', "history")),
    n("history", "Soana", '''{n}Soana watches you. Outside, a branch brushes the rock, scrapes once, and falls still. Her hand rests beside the unfinished letter.{/n}''',
        c('"I still want to court you. Even with no word from Corven."', "court", requires=("soana.courtship_chosen",)),
        c('"I wanted to court you. With no word from Corven, I can only be your friend."', "friend", requires=("soana.courtship_chosen",)),
        c('"I asked you to wait. I have thought enough. I want to court you."', "court", requires=("soana.courtship_waiting",)),
        c('"I asked you to wait. I have thought about it. Let us stay friends."', "friend", requires=("soana.courtship_waiting",)),
        c('"I came as your friend. I still am."', "friend", requires=("soana.friendship_chosen",))),
    n("court", "Soana", '''{n}Soana pushes the bark farther from her knee.{/n}
"Then come to my cave. Not only when something has teeth in it. Come while the fish is still warm, before I have eaten it all and decided you are a fool."
"Will you be here?"
"If I am in the woods, I will leave a mark on the upper path. You know my tracks by now. If you do not, I have wasted a good deal of walking."
{n}She hooks a finger beneath the edge of your sleeve and pulls out a pine needle.{/n}
"I will leave the blanket dry. I will go to the stream with you when there is no curse to drag out of it. And I will tell you to come back when I want you here. That ought to keep your ears busy."
"And the forest?"
"It comes first when it is burning. You know that already. When it is not, you may have to endure an evening with nothing worse than me."
{n}She drops the needle, takes your hand, and tugs.{/n}
"Come closer. I have been talking to that wretched letter all morning. It has neither a mouth to kiss nor the sense to answer."''',
        c('[Take her hand and sit close.]', "near"),
        c('"Not to bed yet. I still want to court you. I am not going anywhere."', "slow")),
    n("near", "Soana", '''{n}You sit beside her. Soana pulls your hand onto her knee and closes her rough fingers around it.{/n}
"There. No witnesses."
"There is a letter."
"It has disgraced itself. Turn your back on it."
{n}You laugh. She plucks a loose thread from your sleeve, then runs her thumb along the wrist beneath it. Her eyes stay on your face.{/n}
"Soana the Wise, sitting here pulling threads from a hunter's sleeve. The old fools who came for my counsel would have stared."
"What would you have told them?"
"To stop staring. They were slow to learn."
{n}She leans against your shoulder. At the cave mouth the sun reaches the cup, then the bark. She watches the light creep over her rubbed-out words.{/n}
"Next time I tell you to stay after dark, do not arrive with a shovel and three questions about spirits."
"What should I bring?"
"Yourself. A fish, if you can catch one. I will not pretend I called you here for the fish."
{n}Her thumb moves over your wrist again, and she presses her cheek against your shoulder.{/n}
"Though I will eat it."''', c('[Stay close to her until it is time to leave.]', flags=("soana.later_courting", "soana.promise_spoken"))),
    n("slow", "Soana", '''{n}Soana lets go of your hand. Her fingers close around her own knee.{/n}
"Not tonight, then. Sit down before you retreat all the way to Drezen."
"I am staying. I only want to wait before we go to bed together."
"I heard you. I have waited through longer winters than this one."
{n}You sit on the stone beside her. She gathers the unfinished letter and slips it beneath the cup, out of the wind.{/n}
"Upstream, there is a hollow where owls used to nest. The water sounds deep there. It is no deeper than your knee. Corven always stepped around it and soaked his boots in the mud instead."
"You let him?"
"He had eyes. I had told him once."
{n}She traces the bend of the stream in dust with her stick. The line runs past your boot; she taps it until you lift your foot.{/n}
"We can walk there another day. Wear those boots. I want to see whether you are any cleverer."
"And tonight?"
"Tonight you sit here. I have not finished insulting you."''', c('[Keep courting her. Wait before going to bed together.]', flags=("soana.later_courting", "soana.later_slow", "soana.promise_spoken"))),
    n("friend", "Soana", '''{n}Soana nods once. She picks up the bark and rubs at a word with her thumb.{/n}
"Friends, then. You can stop looking at me as though I have set a snare under your feet."
"I want to keep coming."
"You have worn a path to my cave. I noticed."
{n}She turns the bark over and studies the blank side.{/n}
"I may finish this. He always said I should put a quarrel on bark before I shouted it. By the time I had found the charcoal, I would have thought of something worse to say."
"Shall I help?"
"No. Your spelling will only give me another quarrel. And do not let me read it to you six times. Take the charcoal away on the third."
{n}She sets the bark down. A crooked smile draws up one corner of her mouth.{/n}
"Come back when I have finished with the shrine. We will take the upper path. There are things in this forest worth looking at before they go wrong."
"I look forward to it."
"Bring food. Looking makes a hunter hungry, and I am tired of feeding you."''', c('[Tell her you will return as her friend.]', flags=("soana.later_friends", "soana.promise_spoken"))),
], "soana.aftermath_heard", delay=48)

s("the_unwelcome_path", "The unwelcome path", '"Meret said you wanted me to hear a proposal of hers."', [
    n("start", "Soana", '''{n}Meret has brought a second hunter, a broad-shouldered man called Varn who keeps his bow on the ground while speaking to Soana. He does not look comfortable without it.{/n}
"I am not asking to settle here," he says. "I am asking to use the upper path when the river rises. Two families travel it. We can keep clear of the shelf."
"You can keep clear of the shelf now that someone else has made it safe to approach," Soana replies.
"Yes. That is why I am asking now."
{n}Meret beckons you closer and points toward the upper path.{/n}
"The lower crossing washed out last spring," she explains. "They went three days around. There were children with them, and one old man who could not keep up. He lived. Before anyone turns that into a tale about a dead man, he lived, and he was furious."
"He should curse Varn for trying that crossing again," Soana says.
"Then let us avoid the next three."
{n}Soana taps her stick against the ground once.{/n}
"The upper path passes the hollow where the deer shelter in hard weather. A road is never only the feet of the first person who asks to walk it."''',
        c('"Walk it with us. Let us see where the trouble would be."', "walk"),
        c('"I cannot hear the whole proposal today. I will return."', abort=True)),
    n("walk", "Soana", '''{n}Soana gets her stick. Varn starts to speak, sees her face, and shuts his mouth. Meret retrieves his bow and hands it to him unstrung.{/n}
"We are looking at a path," she says. "You will not need to shoot it."
{n}The upper route narrows between two roots, then opens onto a strip of firmer ground. Soana points out the low branches that conceal the deer hollow from above. Varn notices the same thing for a different reason: the branches would make good shelter for a night's camp.{/n}
"No fires there," Soana says before he can finish the thought.
"We would not leave one burning."
"You would leave the smell, the cut branches, and the belief that the next traveler may do the same."
{n}He looks toward Meret. She points farther along the path.{/n}
"There is bare ground farther on," she says. "A cold camp could go there."
"Farther on is farther in the rain."
"Yes."
{n}Soana looks faintly pleased to hear someone else give that answer.{/n}
{n}At the bend, Varn stops beside a narrow cleft that would let travelers avoid the deer hollow entirely. Its floor is rough but passable on foot. A loaded handcart would not get through without widening it.{/n}
"We could cut this back," he says.
"You could carry less," Soana replies.
{n}Varn looks toward the cleft. Soana taps the exposed roots with her stick.{/n}''', c('[Ask how they will get the loads through without cutting roots.]', "interests")),
    n("interests", "Soana", '''Varn answers first. "We can leave the carts below and carry the loads through. We cannot do that in one journey. Someone must watch the things left behind. And I cannot swear every wet, frozen traveler will stay out of the driest hollow."
"Then do not promise for every traveler," Soana says.
"You keep asking for a guarantee nobody can give."
"I said feet may pass. Your axe stays at your belt. Those roots hold the bank together."
{n}Meret turns to Soana.{/n}
"Will you leave anything at the camp?"
"I have walked the ground with you, have I not?"
"We have walked it. What will be there when the families come?"
{n}Soana plants her stick against the root. Her knuckles whiten.{/n}
"I can mark the cold camp," she says at last. "I can leave a dry bundle beneath stone, enough to start a fire beyond the hollow if the weather is dangerous. I will not tend it every week for people who cannot be bothered to bring their own."
"We can replace what we use," Varn says.
"You can. Whether you will is what I shall discover."
{n}She looks toward you.{/n}
"You have been quiet, hunter. Which road would you take with a sack on your back?"''',
        c('"Let them walk through the cleft and carry the loads in stages. Keep them out of the hollow."', "cleft"),
        c('"Open the wider path when the river is dangerous. Mark a cold camp. No cutting."', "flood")),
    n("cleft", "Soana", '''"Then they carry," Soana says.
{n}Varn looks at the rough floor of the cleft. He lifts a loose stone with his boot, considers kicking it aside, and instead picks it up.{/n}
"We will have to clear the worst of these. No roots cut. Stones moved by hand."
"Move the stones. Touch no roots."
"And we need somewhere dry for the loads while we go back."
{n}Meret finds a shallow overhang beyond the cleft. It will not hold all the baggage at once, but it will shelter the things most easily spoiled. Varn measures it against the length of his bow, calculating rather than arguing now.{/n}
"It costs us time," he says.
"It does," you answer.
"Try carrying a sack through before you call it easy."
{n}Soana gives him a searching look.{/n}
"I have carried enough buckets uphill. I know what a load weighs."
{n}Together you move enough loose stones to make the first section safe. The gap still stops Varn's cart at the first root. Soana shows Varn where a footstep will break the edge above a root; he shows her where a person with a load cannot see that edge until too late. The final line curves farther outward than either first proposed.{/n}
{n}When you return to the cave, Varn has a route he dislikes less than the flooded crossing. Soana has kept the deer hollow quiet. Meret has agreed to show the two families the cleft once, not guide every later journey through it.{/n}''', c('[Repeat the rules for the cleft and the promise of kindling.]', "terms_cleft")),
    n("terms_cleft", "Soana", '''{n}Soana makes Varn repeat the part about roots before she repeats her own promise to leave emergency kindling beyond the hollow. He listens with an expression that suggests he will enjoy reminding her if she forgets.{/n}
"There," Meret says. "Now everyone has something to be irritated about. It may last."
{n}Varn goes ahead to fetch a second sack of supplies from his camp. You wait by the cleft for him to bring his load through. When he returns, it does, though he has to turn sideways at the narrowest point.{/n}
"No widening," Soana says.
"I remember."
{n}His patience is thin. He still takes the narrow route.{/n}
{n}Later, alone with you, Soana watches the deer hollow from a distance. Nothing moves there while you wait.{/n}
"The deer may go elsewhere," she says. "But we will not put a camp over their heads."
{n}She turns back toward the cave. At the bend she checks the first exposed root. Varn's boot has left a mark beside it. She rubs the earth back into place.{/n}''', c('[Return with her by the path you have kept clear.]', flags=("soana.path_cleft", "soana.path_agreed"))),
    n("flood", "Soana", '''{n}Soana looks at the wider path, then down toward the river. She does not answer until the others have stopped preparing objections.{/n}
"When the lower crossing is dangerous," she says. "Not whenever the upper path is more convenient. No traps. No branches cut for bedding. No fires in the hollow."
"Agreed," Varn says quickly.
"Hear the rest before you discover how agreeable you are. You leave word when you pass, if I am here. If I am not, you leave the marker at the bend turned toward the river. I will know to look for disturbed ground before I take an animal trail."
{n}Meret proposes a marked stone rather than a carved post. A post might invite every traveler to treat the path as a road. Varn dislikes the obscurity but accepts it when Soana points out that his two families will be shown where it is.{/n}
{n}You walk the wider route together, choosing a cold camp beyond the hollow and a place for emergency kindling. Varn has to abandon the shelter he liked best. Soana stops beside the hollow, watching the grass where the deer have lain. She does not set the camp marker there.{/n}
"If they leave," she tells you, "do not promise me they will come back. You have no tongue for calling deer."
"I won't."
"Good. Carry the kindling."
{n}At the bend, she turns the marker toward the river herself, then turns it back. The two positions are clear even in dim light.{/n}''', c('[Make sure Varn can find the agreed marker and camp.]', "terms_flood")),
    n("terms_flood", "Soana", '''{n}Varn repeats the restrictions, this time without trying to shorten them. Soana repeats her promise to leave emergency kindling where a fire will not drive smoke into the hollow.{/n}
"And if someone ignores you?" you ask.
"I will find out who," she says. "He will hear me. Varn will answer for Varn. If another fool brings an axe, I shall ask that fool what he is doing."
{n}She turns her stick toward Varn. He nods hurriedly and takes up his sack.{/n}
{n}The first test is his own walk back with a full sack from camp. He uses the marked stopping place instead of the sheltered hollow. It is less comfortable. He says so, and remains there while he adjusts his load.{/n}
{n}After he leaves, Soana watches the trees above the deer path. A bird calls twice from the same branch.{/n}
"I wanted them farther away," she says. "I still do. But I will not pull a drowned child from the river and tell its father how quiet my trees are."
{n}She points her stick at you.{/n}
"This crossing. These travelers. Do not arrive tomorrow with an army and quote me at myself."
"I understood the limits."
"Then we may get on tolerably well."''', c('[Return to the cave. Varn has a crossing and rules to keep.]', flags=("soana.path_flood", "soana.path_agreed"))),
], "soana.promise_spoken", delay=48)

s("after_the_last_visitor", "After the last visitor", '"You asked me to come when the others had gone."', [
    n("start", "Soana", '''{n}Soana watches two birds quarrel over a branch. A clean shawl covers her shoulders, held by the old clasp. She has a pine needle caught in its hem.{/n}
"They have been at it since I came out. All those branches, and they want that one."
{n}One bird flies to a higher bough. The other follows it and begins scolding again.{/n}
"Meret is on the eastern paths. Varn knows where to cross. The bowl is shut. If something comes whining before morning, I may throw a stone at it."
{n}She turns toward you and catches the needle in her hem. She pulls it free, but keeps it between her fingers.{/n}
"I wanted you here. There is no sack to carry. Sit."''',
        c('"I wanted to come. The evening is yours."', "consequence"),
        c('"I want an evening with you, but I cannot stay now. Another night."', abort=True)),
    n("consequence", "Soana", '''{n}You sit beside her outside the cave. Beyond the trees, the upper path is quiet.{/n}''',
        c('"Varn managed the narrow cleft with his load."', "cleft", requires=("soana.path_cleft",)),
        c('"He used the marked camp, even though he disliked it."', "flood", requires=("soana.path_flood",))),
    n("cleft", "Soana", '''"He did. He called one of the stones a name I shall remember the next time I strike my foot against it."
{n}Her mouth twitches.{/n}
"Two deer came to the hollow this morning. One cropped the grass. The other kept watching me as though I had stolen something."
"You stayed to watch?"
"Until the grass eater lay down. Then I left. They can keep watch over their own hollow for an afternoon."
{n}She turns toward the cave, glancing once at the upper path.{/n}
"Varn has another load to carry. He will curse the cleft again. Let him. His feet will be dry, and he will have neither a root nor a deer's neck under his cart wheels."
{n}She picks a burr from her shawl and throws it into the grass.{/n}
"There. Enough about Varn and his sacks. I have spent the day listening to him. Come inside before I start sounding like him."''', c('[Let the evening turn toward the two of you.]', "private")),
    n("flood", "Soana", '''"He did. There were fresh tracks below the hollow afterwards, none inside. I found no cut branches. He may yet keep his hands off a tree."
{n}Her mouth twitches.{/n}
"The kindling is dry. I looked twice."
"You expect him to look too."
"Let him. I stacked it myself. He will have to find something else to grumble about."
{n}She brushes a burr from her shawl. It catches on her finger; she flicks it away.{/n}
"I would rather have the hunters down by the river. But I will not fish children out of it because their father has annoyed me. He has a path now. If he starts widening it with an axe, I will be waiting."
"He remembered the marked camp."
"And you have reminded me twice. Are we to spend the whole evening counting the man's good deeds?"
{n}She gets up, bringing the shawl close around her shoulders.{/n}
"Come inside. I did not call you here to warm Varn's ears."''', c('[Let the evening turn toward the two of you.]', "private")),
    n("private", "Soana", '''{n}The air cools. Soana rises and gestures toward the shelter of the cave. She has moved her tools away from the place where you usually sit. A folded blanket lies there instead.{/n}
"It is clean," she says. "I mention that before you decide I have become mysterious."
{n}She loosens the clasp of her shawl and hangs it on a peg. Her hair has escaped its tie at one temple. She catches you looking and leaves the strand where it is.{/n}''',
        c('"A blanket instead of tools. You were expecting me."', "desire", requires=("soana.later_courting",)),
        c('"I brought a story that has nothing to do with protecting anything."', "friend", requires=("soana.later_friends",))),
    n("desire", "Soana", '''"Yes. And moved the tools. You might yet be worth the trouble."
{n}She catches your sleeve and pulls you toward the blanket. Her palm settles against your side.{/n}
"I want your mouth, hunter. And I want you here when the light goes."
"You have no rite prepared?"
"Pff! No flowers. No spirits peering over my shoulder. I have had enough things in these woods calling out when they were not invited."
{n}She laughs, low in her throat, and draws her hand along your side to your belt. Her fingers curl there. The loose strand of hair at her temple brushes your cheek.{/n}
"I have thought about kissing you while you stood there talking of cord and clay. You were very thorough. I could have bitten you."
"Only thought about it?"
"So far."
{n}She tilts her face toward yours. Her grip tightens on the belt.{/n}
"Come here before I hear another word about the shrine."''',
        c('[Kiss her] "I\'m staying."', "night"),
        c('"I want the kiss. I will leave tonight, and come back another day."', "kiss"),
        c('"I want to sit beside you tonight. Not to bed yet."', "quiet")),
    n("night", "Soana", '''"Good."
{n}She pulls you down by your belt. The first kiss is slow. In the second she bites your lip and laughs against your mouth when your arms close around her.{/n}
"The stone is hard. Get that blanket under us. No, child, the other end. I folded it for a reason."
{n}You spread it with one hand while she works at your collar. She pulls the cloth free and puts her mouth against the warm skin beneath.{/n}
"All day I have wanted this. Hunters at the cave mouth, hunters on the path. Not the hunter I wanted."
{n}Her braid comes loose under your fingers. She shakes it out, lifts her clothes over her head and drops them across the tools. Bare skin meets yours as she drags you onto the blanket. Her knees press into the folded wool on either side of your hips. She bends over you, kisses you hard, then straightens and draws you against her as she lowers herself.{/n}
{n}In the morning she is awake first. Her hand lies over yours beneath the blanket. A fold of your discarded shirt props up her shoulder.{/n}
"Worth moving the tools," she says.
"High praise."
"Do not grow proud. You put the blanket down badly."
{n}She catches your chin and kisses you again. When you get up, she points to a piece of smoked fish beside the cold hearth.{/n}
"Eat before you go. You look thin."''', c('[Eat, kiss her, and tell her you will come back.]', flags=("soana.later_night", "soana.lovers", "soana.progression_kept"))),
    n("kiss", "Soana", '''"Then I had better give you something to remember on the road."
{n}You lean toward her. Soana's hand slips behind your neck and draws you the rest of the way. She kisses you once, then again before you can speak. Her fingers tighten in your hair.{/n}
"There. Try thinking about cord and clay now."
"I would rather come back."
"You have not left yet. You can boast of returning when I see your feet on the path."
{n}She pulls you onto the blanket beside her. The remaining light thins at the cave mouth. She asks what you will do when you get back, and interrupts your account of duty with a snort.{/n}
"After that. Have you no fish to catch, no fool to fleece at dice? Must I find all your pleasures for you?"
{n}When you rise, she takes the shawl from its peg and follows you to the entrance. The old clasp catches; you fasten it, and her hand closes over yours.{/n}
"Watch the root at the bend. It will trip you if you go dreaming down the path."
"Of cord and clay?"
{n}She gives your hand a sharp squeeze.{/n}
"Bloody hunter. Come back while I still have fish."''', c('[Kiss her goodbye and take the path before dark.]', flags=("soana.later_kiss", "soana.progression_kept"))),
    n("quiet", "Soana", '''"Sit, then. The blanket is there for sitting on."
{n}She settles beside you and spreads it over both your knees. Your hands meet under the wool. She threads her fingers through yours, then gives a pleased grunt when you close your grip.{/n}
"You look as though you expect something to leap out of the corner. The bowl is on the ridge, hunter."
"I was looking at the tools."
"They will survive a night without me. Varn tried to recite every word I had said to him this afternoon. I could have put him to work sharpening knives and got something useful from it."
{n}Her imitation of Varn's weary voice makes you laugh. She tries it again, adding his bowed shoulders and the hitch with which he hefted his sack.{/n}
"I moved those tools three times. Each time I found another sharp thing under the blanket. You should admire my thoroughness."
{n}Darkness gathers at the cave mouth. She rests her head against your shoulder. Outside, one of the birds calls; its rival answers from farther away.{/n}
"Still quarrelling. Even you have managed to sit quietly."
{n}When you rise to leave, she folds the blanket and puts it back where you sat. The tools stay in their new corner.{/n}
"I will leave it there. Come before dark next time. I want to see your face when I insult you."''', c('[Say goodnight. Leave the folded blanket where she put it.]', flags=("soana.later_quiet", "soana.progression_kept"))),
    n("friend", "Soana", '''"A story with no guardian in it? Sit. I will count."
{n}You tell her about a traveler who tried to sell a mule by calling its refusal to move a sign of excellent judgment. She interrupts to ask whether the buyer knew anything about mules. When you describe the end of the argument, her laugh startles the birds outside.{/n}
"The mule had more sense than both of them. I hope it bit the seller."
{n}She tells you about a festival singer who lost a wager and had to sing an entire song without naming the person it was written for. The listeners shouted the missing name each time he tried to pass it. She imitates his voice rising as he fought to be heard, then the audience roaring over him.{/n}
"He sang until his throat gave out. The woman went home before the third verse. A wise woman."
{n}You sit until the cave mouth is dark against the last light in the sky. Soana reaches for her shawl.{/n}
"You can bring another story next time. That one was almost worth feeding you."
"Almost?"
"There was no biting."
{n}She walks you to the entrance and takes up her stick.{/n}
"The war will take you far from these woods. Come back with something to tell me when you can. Do not swear it. I have heard enough fine oaths to last me."
{n}She taps the path with her stick, then turns back to the folded blanket.{/n}''', c('[Take your leave as her friend.]', flags=("soana.later_friend_evening", "soana.progression_kept"))),
], "soana.path_agreed", delay=48)
