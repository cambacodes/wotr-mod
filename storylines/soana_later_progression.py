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
"An important distinction. I am sure it appreciates your care."
{n}Soana notices you and points to a bare patch of stone, well away from the entrance.{/n}
"Stand there. She has brought me something that ought to have stayed where she found it. I would prefer not to discover whether it likes you better."
{n}The woman puts the sack down. Its contents strike the stone with a hollow click.{/n}
"Meret," she says. "That's my name. If you hear anyone else say it, don't be polite."
{n}From inside the sack comes a second, softer click, although nothing has moved.{/n}''',
        c('"Tell me what happened before we open it."', "account"),
        c('"I cannot stay for this. Keep it covered until you have help."', abort=True)),
    n("account", "Soana", '''"She found a little shrine on a shelf above the stream," Soana says. "Three standing stones, a hollow beneath the middle one, and a warning that had the misfortune to be written in a language she cannot read."
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
"A sensible decision reached by an exhausting road," Soana says. "Show me your hands."
{n}Meret holds them out. Soana looks beneath each fingernail, then releases her without explanation.{/n}''', c('"You know the shrine?"', "keeper")),
    n("keeper", "Soana", '''"I knew the woman who tended it. Before the Wound. There was no grand temple, no priest with a silver staff. A bowl of water for travelers. A place to leave the first mouthful before drinking."
"Who received it?"
"The thirsty dead, she said. Her grandmother had said it before her. You may spend the day deciding whether their account satisfies a scholar. I would rather discover what has been drinking there since."
{n}She takes a stick and lifts the sack's mouth. Within it lies a shallow black bowl, its rim chipped in two places. A thin white crust marks the inside.{/n}
"There were offerings for the living as well. Water, a dry place to sit, news from the road. People remember the strange part and forget the ordinary work that kept a holy place from becoming a hole in the ground."
"And you helped tend it?"
"I spoke for its keeper when hunters wanted the shelf cleared. They said the stones crowded a useful trail. I said they could go around. They did. For a time."
{n}Meret's eyes narrow.{/n}
"My grandmother told me about that path. She also told me someone made the hunters swear never to take anything from the shelf."
"They wanted my protection for their camp," Soana says. "I wanted their hands kept off the stones. Each received something."
"And now you think the oath belongs to me."
{n}Soana does not look away from the bowl.{/n}
"You have carried away the very thing they promised to leave."''', c('"First we find out what is in it. Then we discuss what anyone owes."', "test")),
    n("test", "Soana", '''{n}Soana sprinkles a little clean water on the bare stone beside the sack. Nothing happens. She moves the stick through the wet patch, then touches its end to the white crust inside the bowl.{/n}
{n}A dark line runs along the wood against the slope. Meret steps back. Soana drops the stick on the stone and covers the bowl again.{/n}
"Hungry," she says. "And able to follow what touches its dish. Do not give it blood. Do not give it a name to practice."
"Can it hear us?"
"I would prefer to assume so."
{n}The stick lies still. At its end, the wet wood has become pale and dry.{/n}
"It took the water," Meret says.
"Something did. We have not yet seen where it went."
{n}Soana takes a second stick and pushes the first into an empty stone hollow. She covers that with a flat rock, too.{/n}
"You asked why I looked at her hands. If she had scratched herself on that rim, we would be having a different conversation. As it is, we may still have time to be careful."
{n}Meret looks at her own fingers again. For the first time she seems less angry than frightened.{/n}
"I didn't steal from a grave."
"I know," Soana says. "Whatever is in that bowl has no right to your brother's voice. Keep hold of that much."''',
        c('"We should examine the shelf while it is light."', "terms"),
        c('"Can you contain it until we understand the shrine?"', "terms")),
    n("terms", "Soana", '''"For a little while. We will put the sack in a second hollow, on dry stone, with nothing living touching it. If it begins calling, nobody answers. If it begins moving, nobody tries to catch it in their hands."
{n}She speaks to Meret as directly as to you. Meret repeats the instructions without being asked, then adds one of her own.{/n}
"And if it uses my voice, you look for me before deciding I said anything."
"Yes," Soana says. "That too."
{n}Together you shift the sack using two long branches. Meret carries the covering stone. The work is awkward, but the bowl remains wrapped and no one touches its rim.{/n}
{n}When it is covered, Soana draws a line in the dust around the hollow. She does not call the line a ward.{/n}
"So nobody steps too close while thinking of something else. I have learned what an excellent talent people have for doing that."
{n}Meret offers to sit watch. Soana sends her to sleep in the daylight instead, within calling distance but beyond the marked stone.{/n}
"I will hear it," she says.
"You cannot hear everything," you remind her.
"No. This is one bowl. Allow me to apply a lesson without reciting the whole of it."
{n}After Meret leaves, Soana looks at you for a long moment.{/n}
"I remember that shrine with clean water in it. Do not be surprised if I am unpleasant while we find out what has become of it."
"You have prepared me thoroughly."
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
"An alteration can be understood," she says. "That is something. I had begun to imagine a wound with no edge."
{n}She studies the closed hand, her own fingers tightening around the stick.{/n}
"I defended this place. Then I stopped coming. Both things are true. Do not choose the one that makes the kinder story."
{n}With the altered groove identified, you can keep to the clean side of the shelf while examining the hollow. You find a clear strip of stone beneath the lip, enough to anchor a temporary seal without touching the new carving.{/n}''', c('[Mark the clean strip on the rubbing.]', "paths")),
    n("wrong", "Soana", '''{n}You recognize the open hand and take the newer circular cut for a worn offering mark. When you reach toward it with the charcoal, the dust gathers against the slope. A dry rasp comes from inside the stone.{/n}
"Back," Soana says.
{n}You withdraw. The charcoal breaks between your fingers. Half of it falls onto the shelf and turns white.{/n}
{n}For a moment everyone waits for something worse. Nothing follows. Meret lets out a breath through her teeth.{/n}
"That part is newer," Soana says. "And it wanted what you brought. I would rather you were offended by my tone than tried it twice."
"I read it wrongly."
"Yes. Now we know one part of the answer at the cost of charcoal. An affordable education."
{n}The direct approach is no longer worth risking. You move back along the path and compare the dry patches with the places Meret rested. It takes most of the afternoon. At each stop she has to decide whether she truly remembers putting the sack down or merely thinks this looks like somewhere she would have stopped.{/n}
{n}By the time the pattern becomes clear, Soana is leaning heavily on her stick. You return to the cave for food and rest before finishing the comparison in the morning. The failed examination has cost you a day, but nobody needs to repeat it to make progress.{/n}''', c('[Complete the slower survey with them.]', "survey")),
    n("patient", "Soana", '''{n}Meret walks the route again, stopping where she rested with the sack. Sometimes she is certain; sometimes she argues with her own memory. You mark only the places she can identify by more than a familiar-looking tree.{/n}
{n}At two of them the moss beneath the sack has dried. At a third, bare stone shows no visible change. Soana pours one drop from the waterskin onto each patch, then watches without touching it.{/n}
"You can sit while we wait," Meret tells her.
"I am aware of the possibility."
"Then use it. I need you watching the water, not falling into it."
{n}Soana gives her a hostile look and sits. Meret pretends not to notice the surrender.{/n}
{n}The comparison takes the afternoon and part of the following morning. You return to the cave to sleep between observations. There is no single brilliant discovery, only the steady exclusion of things the bowl does not seem able to do.{/n}
"If you write this down," Soana says, "include the sitting. People are very fond of leaving out the part where someone waited long enough to notice anything."
{n}When you return to the shelf, she has a different question to put to the altered stone.{/n}''', c('[Compare the survey with the shrine.]', "survey")),
    n("survey", "Soana", '''{n}The drying follows contact with the sack, not Meret's footprints. A damp fern she brushed on the way past remains green. The moss on which she rested the bowl has withered.{/n}
"It travels with its dish," Soana says. "It can call beyond it. It cannot drink every drop of water it can see."
{n}At the shrine, she uses a long twig to lay a thread across the edge of the newer carving. The thread stiffens. A second thread, laid below the old open hand, remains loose.{/n}
"Two workings," she says. "The old invitation and something that closes it. Whoever cut that second line wanted to keep what came. Or wanted what came to keep feeding."
{n}You take a rubbing from the clean side, using the long stick to hold the cloth against the dangerous part. It is clumsier than working by hand, but the lines are legible.{/n}
{n}There is a clear strip beneath the hollow's lip. Soana marks it on the cloth. It may hold a temporary seal while you deal with the dish.{/n}
"I do not know who changed it," she says. "I do not intend to give the dead credit for every cruelty merely because the living have misplaced its author."''', c('[Ask where the thing can be made to go.]', "paths")),
    n("paths", "Soana", '''"There are two ways I would attempt," she says. "Neither is an afternoon's kindness."
{n}She points uphill, toward a sheltered strip of young trees.{/n}
"The old path to the dry ridge passes through my nursery. I have watered those seedlings through three summers. If we lay the bowl's trail through them, the thing can be drawn to bare rock and shut away from the stream. It will drink what it touches on the way. I expect to lose the young trees."
"And the other way?"
"Someone can carry an invitation instead of laying one on the ground. A voice, offered deliberately, with the bowl sealed at the end of the calling. It would have a road for one night. We would close it before dawn."
{n}Meret's jaw sets.{/n}
"Mine. That is what you have been working toward."
"You already answered it once," Soana says. "It knows where to listen."
"That isn't the same as my offering."
"No," Soana replies, after a silence. "It is not."
{n}The admission does not soften either woman's face. Meret has heard a demand approaching. Soana has heard a refusal that may cost her three summers of work.{/n}
"We discuss this with the bowl covered," Soana says. "I will not negotiate over my own forest while that thing sits close enough to enjoy it."''', c('[Return by the upper path with the rubbing.]', flags=("soana.shrine_examined",))),
], "soana.bowl_contained")

s("the_inherited_debt", "The inherited debt", '"We should decide who is being asked to pay."', [
    n("start", "Soana", '''{n}Meret has laid three things outside the cave: her hunting knife, a small purse, and a strip of leather bearing a family mark. Soana stands over them without touching any.{/n}
"I can give you the knife," Meret says. "I can give you what is in the purse. I cannot give you my grandmother's obedience. She took it with her."
"Keep the knife. You will need it more than I will."
"And the money?"
"Will it water a tree?"
"It might buy a pair of hands to carry water."
{n}Soana looks toward you as you approach.{/n}
"There. A merchant's answer. Everything can be made equivalent if one counts long enough."
"It was an offer," Meret says. "I came to you instead of leaving the cursed thing beside someone else's camp. You might remember that part."
{n}The leather strip bears a crude deer with a forked antler. Soana recognizes it. Her expression changes before she can hide the recognition.{/n}
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
"I do not deny the help," Meret says. "I deny that it lets you spend me."
"And I deny that remembering only the help frees you to take whatever protected it."
{n}Meret turns the worn leather over in her hands. Soana follows the movement, then looks away before the younger woman can catch her watching.{/n}
"Would you have helped her if she had no mark?" you ask.
"I have already helped her," Soana answers. "I am deciding how much more of myself I must give while everyone else discovers reasons to give less."''', c('[Ask what carrying the voice would mean in practice.]', "price")),
    n("price", "Soana", '''"One person calls the thing along a prepared road," Soana says. "The words are an invitation to follow the sound, nothing more. No promise of a body. No promise to feed it. The speaker must remain awake and must not answer when it begins using other voices."
"For how long?"
"Until the bowl is sealed. Perhaps hours. If the speaker loses the words, we break the line and carry the dish to the nursery road instead. That is the escape. I will prepare both roads."
{n}She looks directly at Meret.{/n}
"It will hear what is near the surface of your thoughts. It may use your brother again. Afterwards, for a few nights, you may hear his voice when there is nobody there. I cannot promise you will sleep easily. I can promise I will not call that a sign you ought to continue."
{n}Meret rubs the back of her neck. The anger has not left her, but it now has something precise to work upon.{/n}
"Will it keep him?"
"It has never had him. A stolen sound is not your brother."
"Easy to say when it isn't speaking."
"Yes," Soana says. "That is why I am saying it now."
{n}She kneels slowly and pushes the knife and purse back toward Meret.{/n}
"I will not take those and then ask for the voice as though you had paid nothing. Choose after you have heard the whole of it."''', c('"What if you carried the voice, Soana?"', "her_price")),
    n("her_price", "Soana", '''"Then it would have a much larger store of unpleasant things to say."
"That was not an answer."
"It was an excellent reason to dislike the question."
{n}She rises, using the wall rather than accepting a hand she has not asked for.{/n}
"I could carry it. You would have to close the bowl when I told you. Meret would watch the escape line. Neither of you would leave your place because you heard someone in distress beyond it. Especially if the voice was mine."
"And you would be the one hearing it afterwards."
"Yes."
{n}She says the word sharply, before you can make it gentle.{/n}
"Those trees are not decorations. When I am gone, someone may sit beneath them and never know there was a choice. I am allowed to want that enough to lose several nights' sleep."
{n}Meret watches her without looking grateful.{/n}
"You are. You aren't allowed to choose for me because you chose for yourself."
"I have grasped your argument," Soana says. "It has been admirably persistent."
{n}Then she takes the strip of leather by one corner, turns the deer upright, and lays it back among Meret's belongings.{/n}
"I will carry the voice if we keep the nursery. That is my offer. I want the trees. I also want the two of you to do exactly what we agree when the thing starts lying. Can you distinguish that from demanding a lifetime's service?"''',
        c('"Yes. Keep the nursery. We accept your offered night and the escape plan."', "voice"),
        c('"Use the ridge road. I would rather help you plant again than give it your memories to imitate."', "ridge")),
    n("voice", "Soana", '''{n}Soana does not thank you for accepting her risk. She asks you to repeat your part in the working. You do so. Meret repeats hers, then asks where she should stand if the escape line has to be broken.{/n}
"Outside the turn," Soana says. "You must not put yourself between the bowl and the ridge."
"Show me."
{n}The three of you walk the short distance to the bare stone where the working will end. Soana places an ordinary pebble for each person's position. Meret moves hers until she can see both the bowl and Soana's face.{/n}
"There. If you tell me to stop, I want to see you saying it."
{n}Soana considers that, then nods.{/n}
"Good. Do not improve the plan because you feel brave halfway through. I have seen what bravery does to carefully placed feet."
{n}On the way back she pauses beside the nursery. The young trees are thin, uneven, and stubbornly green.{/n}
"They are not grateful," she says.
"Did you expect them to be?"
"No. It is one of their more restful qualities."
{n}She rests her hand on the fence for a moment. This is what she has chosen to keep, at a cost she understands well enough to fear.{/n}''', c('[Agree on the night and each person\'s place.]', flags=("soana.rite_voice",))),
    n("ridge", "Soana", '''{n}Soana looks toward the nursery for so long that Meret begins to gather her belongings merely to have something to do.{/n}
"You think the trees can be replaced," Soana says.
"I think you can choose to lose them. I am not calling them worthless."
"Three summers. Buckets when the stream ran low. Shade moved by hand over the youngest shoots. The ones that died despite all of it."
"I heard you."
{n}She closes her eyes briefly, then opens them.{/n}
"The ridge, then. I will not agree and spend the night making you guess whether I mean it."
{n}Meret puts her purse away. She offers something else instead.{/n}
"When the ground is safe, I can bring seed from the eastern slope. I know where the cones are sound."
"Do not promise me a forest."
"I promised seed."
{n}Soana gives her a grudging nod. Together you walk the proposed road, marking where the damp cord will lead the thing uphill and where the bare rock will stop it spreading farther.{/n}
{n}At the nursery, Soana cuts one low branch from a tree that stands directly in the way. She keeps the green piece tucked inside her sleeve. Neither of you asks her to explain it.{/n}''', c('[Agree on the road and the night of the working.]', flags=("soana.rite_ridge",))),
], "soana.shrine_examined", delay=24)

s("a_voice_in_the_dark", "A voice in the dark", '"Is everything ready for the working?"', [
    n("start", "Soana", '''{n}Soana meets you before sunset. She has tied back her hair and fastened her sleeves close to her wrists. Meret carries the sack between two forked branches, keeping it clear of her clothing.{/n}
"We begin while we can still see the ground," Soana says. "Darkness has received enough credit for other people's carelessness."
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
{n}The words are plain. Their repetition is not. By the third time, the silence after them has begun to feel occupied.{/n}
{n}A child's laugh comes from behind the trees. Meret flinches. Soana does not turn.{/n}
"Follow the sound."
{n}The laugh becomes a cough. Then a man's voice asks whether the water is ready.{/n}
{n}Soana's next breath catches. She puts one hand against her ribs and continues. You do not know the voice. You know that she does.{/n}
{n}The white crust loosens from the bowl's inner wall. It gathers in the center like fine ash stirred by an invisible finger. Beneath it, for the first time, you see the dark glazed bottom.{/n}
"Not yet," Soana says between repetitions.
{n}You keep your hands on the lid. Meret watches Soana's mouth. The voice behind the trees says the same question again, in precisely the same tone.{/n}
"It cannot make a conversation," Soana says, though you cannot tell whether she is speaking to you or herself. "It can only steal one side."
{n}Then it uses her own voice, younger and furious, ordering someone to leave the spring. Her face goes pale.{/n}''', c('[Keep your place and watch for her signal.]', "strain")),
    n("strain", "Soana", '''{n}The last pale thread clings to the rim. Soana's words have become hoarse. Meret touches the dry end of the escape cord but does not join it to the bowl.{/n}
"I can continue," Soana says.
{n}She is looking at you. The stolen voice carries on behind her, describing a quarrel whose other half you cannot hear. Soana lifts two fingers, the sign you agreed would mean she is still choosing the work. Her hand shakes; the sign is clear.{/n}
"A little longer."
{n}The thread stretches toward her, almost transparent. It has not crossed the bare stone. If you wait for it to leave the bowl completely, you may close the vessel without sending it along the nursery road. If you break the invitation now, the prepared escape will take it uphill through the seedlings.{/n}
{n}Soana sees you glance at the cord.{/n}
"Do not decide that I have ceased to understand because you dislike seeing the price."
{n}Meret says nothing. Her fingers remain on the escape line. She is ready to follow either instruction, but will not disguise whose choice it is.{/n}''',
        c('"I see your signal. I will wait for the word we agreed."', "held"),
        c('"The ridge. I am ending my part before this goes farther."', "broken")),
    n("held", "Soana", '''{n}You keep the lid steady. Soana closes her eyes for one breath, opens them, and speaks the phrase again. This time she does not compete with the voice behind her. She gives the words slowly, each one distinct.{/n}
{n}The pale thread lifts from the rim. The bowl is empty.{/n}
"Now."
{n}You press the lid down and turn it through the half-circle she marked. Clay squeezes into the seam between lid and rim. Meret draws the dry escape cord away before any loose thread can find it.{/n}
{n}The voice stops in the middle of a word. The absence strikes harder than a cry would have. Soana sways, catches herself with her stick, and remains standing.{/n}
"Again," she says.
{n}You ask what she means. She stares at the sealed bowl, then shakes her head.{/n}
"Nothing. It had already stopped. I was still listening."
{n}Meret brings a cup of water but waits for Soana to take it. Her first swallow hurts. The second goes down more easily.{/n}
"The trees?" she asks.
"Untouched," Meret says.
{n}Only then does Soana sit. Her hand remains around the cup so tightly that you can see the pressure in her knuckles.{/n}
"Do not congratulate me yet. We have a bowl to bury in dry stone, and a shrine whose invitation must be closed. This was the loud part. There is work after it."''', c('[Stay through the remaining work and the return to the cave.]', flags=("soana.nursery_saved", "soana.voice_carried", "soana.working_done"))),
    n("broken", "Soana", '''"I told you I could continue."
{n}There is no time to answer. You lower the lid without turning it; Meret joins the wet cord to the bowl's base. Soana stops speaking and steps sideways onto clear stone.{/n}
{n}The pale thread drops into the damp groove. It runs uphill faster than water should, bleaching the cord behind it. In the nursery, leaves fold as if a sudden frost has passed over them.{/n}
{n}Soana watches until the thread has reached bare rock. Then she comes to your side, presses two fingers to the lid, and directs the turn that closes the bowl.{/n}
"Now. Keep it level."
{n}Her voice is steady again. That makes the anger in it easier to hear.{/n}
{n}The last strand vanishes beneath the seal. Meret pulls the dry end of the cord free. No sound follows from the trees.{/n}
"You may refuse a part in my working," Soana says. "I told you the escape for that reason. Do not tell me afterwards that I asked you to use it."
"I won't."
"See that you remember."
{n}She walks to the nursery. The nearest sapling has lost every leaf. She touches its stem with the back of her hand, then turns away before either of you can offer comfort she has not requested.{/n}
"We finish closing the shrine," she says. "We can disagree while doing it. I have not forgotten how."''', c('[Complete the work without claiming her agreement to the interruption.]', flags=("soana.nursery_lost", "soana.voice_interrupted", "soana.working_done"))),
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
"I agreed," she says when Meret approaches. "You need not remind me."
"I wasn't going to."
{n}Meret stands beside her without touching the tree. After a while Soana returns to the sealed bowl.{/n}
"We close the shrine before we rest. I do not intend to pay twice because I was tired after the first payment."''', c('[Help close the old invitation and secure the sealed bowl on dry stone.]', flags=("soana.nursery_lost", "soana.ridge_used", "soana.working_done"))),
], "soana.the_inherited_debt", delay=48)

s("what_followed_home", "What followed home", '"I came to see what the working left behind."', [
    n("start", "Soana", '''{n}Meret is outside the cave, cutting the damaged cord into short lengths. She has laid each piece on bare stone to dry. Soana is farther inside, where the light does not reach her face.{/n}
"The bowl is still sealed," Meret says. "We checked it at dawn. The stone around it is dry. Nothing has called from the shrine."
"And here?"
{n}She glances toward the cave.{/n}
"You should ask her."
{n}Soana hears that much and answers before you can enter.{/n}
"A rare piece of sound advice. You may follow it."
{n}You stop where she can see you clearly. There is no cup offered, no task placed between you. She seems to have decided that the conversation will happen without those defenses.{/n}''',
        c('"Tell me how the night was."', "voice", requires=("soana.voice_carried",)),
        c('"I want to hear what my decision cost you."', "interrupted", requires=("soana.voice_interrupted",)),
        c('"Have you been back to the nursery?"', "lost", requires=("soana.ridge_used",)),
        c('"I can return when you want company."', abort=True)),
    n("voice", "Soana", '''"I heard him asking for water after I lay down. Three times. Then I dreamed I had answered, and woke angry enough to get up."
{n}She looks at the cave mouth rather than at you.{/n}
"Corven. That was his voice. You had probably guessed that it belonged to someone, though I hope you were not occupied with guessing while holding the lid."
"I was watching your signal."
"Good."
{n}She draws a slow breath, testing whether her throat still hurts.{/n}
"I remembered the actual afternoon eventually. He had been carrying water for other people. When he asked whether ours was ready, I told him he could wait. I was busy being useful somewhere more visible."
"Is that why the thing chose it?"
"I do not know. Perhaps it was only an easy scrap to steal. I will not appoint it a wise judge of my marriage because it found a voice that hurt."
{n}Her answer is fierce enough to stop the question becoming an explanation she never asked for.{/n}
"I still choose the trees," she says. "I would prefer the trees without this. That was not on offer."
"What would help tonight?"
"Someone answering when I speak with my own voice. Someone who does not ask what every silence means. Meret sat outside until I slept this morning. She is going to her camp before dark. I told her to go."
{n}She looks at you at last.{/n}
"You may sit a while. I am not asking you to listen all night. I have already had enough of voices that will not stop."''', c('[Sit where she can see you and let her choose when to speak.]', "visitors")),
    n("interrupted", "Soana", '''"The trees. The nights I spent tending them. And an agreement I believed you would keep until I changed my answer."
{n}She watches you closely, as if there is one particular reply she will not forgive.{/n}
"I heard your signal," you say. "I ended my part anyway."
"Yes. That is the reply I needed to hear before anything else."
{n}Outside, Meret's knife stops moving for a moment, then begins again.{/n}
"I will not tell you that you had no right to stop," Soana continues. "I would be a fool to ask someone to stand in a dangerous working and deny them that right. I am angry because your fear overruled what I wanted, and because the price fell on something I have kept alive for years. Both of those things may remain true even if you believe you chose well."
"I do believe it. I also know you did not ask me to save you from your own decision."
"Then we need not spend the morning teaching each other words we already understand."
{n}She looks toward the nursery path.{/n}
"For the next working, I will ask someone else to close the bowl. If there is a next working. You may help in another place."
"That is fair."
"It is necessary. Fairness may arrive later."
{n}Her voice softens by a fraction.{/n}
"You can still sit down. I did not invite only the agreeable parts of you here. I would have had very little company."''', c('[Sit, accepting that practical trust will have to change.]', "visitors")),
    n("lost", "Soana", '''"Yes. This morning. I thought I would count them. Then I found I had been counting them all night without going anywhere."
{n}She takes the green branch from her sleeve. Its leaves have begun to droop, but they have not curled and whitened like the ones left on the trees.{/n}
"I cut this before the working. I knew it would not become a forest in a cup. I wanted one piece that had not been drunk dry."
"Meret offered seed."
"She brought some. Sound seed, too. I shall plant it when the ground is ready."
"You sound surprised."
"By the seed? No. By how much I resent having to begin again. I thought agreeing beforehand would spare me that indignity."
{n}She turns the branch so its least damaged leaf faces the light.{/n}
"It did not. It spared me the additional pleasure of blaming someone who had concealed the cost. That is worth something."
"Would you choose the ridge again?"
"Ask me after the first seedlings survive a summer. Today I would like the right to dislike my own answer without being asked to replace it."
{n}You leave the question there. After a while she lays the branch beside her and shifts enough to make room.{/n}
"Sit. If I must begin again, I can at least complain to someone who knows what I am beginning."''', c('[Take the place she has made.]', "visitors")),
    n("visitors", "Soana", '''{n}Meret finishes cutting the cord and comes to the entrance. She has kept the clean pieces separate from those that touched the bowl.{/n}
"These can be burned on the bare ridge," she says. "I won't leave them where an animal can chew them."
"Good."
"I also wanted to say something before I go. My grandmother's mark stays with me. But if you want a person to look at the eastern paths after rain, I can do that when I am here. Ask me. Don't call it owed."
{n}Soana regards her for a long time.{/n}
"I want the eastern paths watched after rain," she says. "Will you do it?"
"When I am here. Not while I am away."
"I had understood that limitation."
"I thought we should enjoy hearing it twice."
{n}For the first time, Soana laughs at something Meret has said. It is a dry, unwilling sound, but it is a laugh.{/n}
"Go, then. Before I find a third way to ask."
{n}After Meret leaves, Soana watches the path until the bow on her back disappears among the trees.{/n}
"Her grandmother was less troublesome."
"Was she?"
"No. But she is not here to contradict me, and I intend to make use of the advantage."''', c('[Ask what becomes of the old agreement.]', "old")),
    n("old", "Soana", '''"It remains something people did," she says. "I will not pretend I gave nothing because I cannot collect everything I want from their grandchildren."
"No one asked you to forget it."
"People ask that without using those words. They call a promise old, and wait for it to become foolish."
{n}Her hand settles on her knee; she seems to be counting something that has no visible shape.{/n}
"The shelf will stay closed. There will be no bowl inviting whatever wanders near it. If a traveler needs water, someone living can offer it. If no one is there, the traveler must carry a skin. That is a smaller holiness than the one I remember. It may survive better."
"And the forest's guardian?"
{n}Her gaze sharpens. She will not let the day's success answer a different question.{/n}''',
        c('"Orso remains bound. This has not freed him."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
        c('"Orso remains dead. This has not replaced him."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"No. And I have not become someone who would watch the forest die merely to keep clean hands. You should not stay near me in the hope that I have."
"I know what remains between us."
"Then remain with your eyes open."
{n}She looks at the path where Meret vanished.{/n}
"What we did gives me one less hungry thing to account for. One. It is not a new name for what holds Orso. I will remember that when I am tempted to boast. You may remind me if I fail. Once."
{n}The qualification carries enough of her familiar temper to make the invitation recognizable.{/n}''', c('[Stay without calling the unfinished work resolved.]', "end")),
    n("dead", "Soana", '''"No. There is still a place in this forest where I expect to hear his feet. A clever sealing has not filled it."
{n}She rubs one thumb across the other hand, then stops.{/n}
"I am still looking for protection. If I find something dangerous, I will not become harmless merely because you have sat beside me through a difficult night. I would prefer you hear that now."
"I am listening."
"Good. Affection has made people remarkably deaf in my experience."
{n}She looks toward the closed shelf's path.{/n}
"But I have also seen one danger ended without putting it into a creature's flesh. I am capable of remembering an answer that does not flatter my old one."''', c('[Stay without calling the unfinished work resolved.]', "end")),
    n("end", "Soana", '''{n}The afternoon passes without another voice from the covered stone. Once, Soana begins to speak and stops. You wait. Eventually she tells you that the wind has changed and the eastern slope will be cold tonight.{/n}
"That was all," she says.
"I heard you."
{n}She nods, satisfied with the smallness of the answer. Before you leave, she asks you to come again when the practical remnants have been dealt with.{/n}
"There is something I have been putting aside whenever another danger arrived. I can always find a danger. I would rather discover whether I can finish a conversation."
{n}She does not name Corven. She does not need to.{/n}''', c('[Agree to return for the conversation she has chosen.]', flags=("soana.aftermath_heard",))),
], "soana.working_done", delay=48)

s("a_promise_still_spoken", "A promise still spoken", '"You wanted to finish a conversation."', [
    n("start", "Soana", '''{n}Soana has a strip of clean bark on her lap. There are words on it, written in charcoal, and a large black smear where several more have been rubbed away.{/n}
"I attempted a letter," she says. "It became an argument with someone who could not answer. I have conducted enough of those aloud."
"To Corven?"
"Yes. I have nowhere to send it. I know that. You need not make your face gentle before telling me."
{n}She turns the bark over. The other side is blank.{/n}
"I kept finding ways to write that he would understand. Then I remembered that I do not know what he would understand. I know what he used to forgive. Those are different things."
{n}She puts the bark aside and faces you with her hands empty.{/n}
"I have not discovered a death, a grave, or a message. There is no new fact waiting to make this convenient. I want to speak about what I choose while the facts remain as they are."''',
        c('"Then I will listen to your choice."', "choice"),
        c('"I want to give this the time it deserves. May I come back?"', abort=True)),
    n("choice", "Soana", '''"I will not go on calling my life a waiting room," she says. "I made promises to him. I meant them. I have spent years apart from him, and I do not know whether another meeting is possible. I have nevertheless been living those years. I cannot hand them back because I dislike what became of them."
{n}The words come unevenly. She leaves a pause where a more polished speech would have concealed the effort.{/n}
"If he stood here tomorrow, I would have to tell him what I had done. I would not greet him with a tale about how the world had chosen for me. Nor would I tell him that you were a mistake I could erase by being ashamed loudly enough."
"What would you ask of him?"
"To hear me. Perhaps he would refuse. Perhaps he would have something of his own to say that I would find very difficult to hear. I have imagined the first moment often. I have been less generous about imagining the second."
{n}She looks at the bark again.{/n}
"I am choosing to make room for another love if it is offered and if I want it. I will not put a yes in Corven's mouth to make that easier. I wore his flowers. I remember why. If you cannot stand beside me while his answer is missing, tell me. I would rather hear you than invent your answer too."''', c('[Answer from the relationship you have actually chosen.]', "history")),
    n("history", "Soana", '''{n}She waits. Outside the cave, a branch brushes the rock and falls still. There is no interruption available to rescue either of you from speaking plainly.{/n}''',
        c('"I still want our courtship. I want us to choose it with that uncertainty named."', "court", requires=("soana.courtship_chosen",)),
        c('"I wanted to court you. I am choosing friendship now, because I cannot accept this uncertainty."', "friend", requires=("soana.courtship_chosen",)),
        c('"I asked for time. I have had it. I want to court you now."', "court", requires=("soana.courtship_waiting",)),
        c('"I asked for time. My answer is friendship."', "friend", requires=("soana.courtship_waiting",)),
        c('"Our friendship matters to me. That remains my answer."', "friend", requires=("soana.friendship_chosen",))),
    n("court", "Soana", '''{n}Her shoulders ease, but she does not reach for you immediately.{/n}
"There is another thing. I do not want a promise that your life will become a path between this cave and nowhere else. You have people I do not know. You may have loves I do not share. I will ask to be told when a promise to me cannot be kept. I will not ask you to make everyone else disappear so that I need never feel uncertain."
"And what will you promise?"
"To tell you what I offer. To refuse what I cannot give before you build your life around it. To remember that inviting you close does not entitle me to command you when I am afraid."
{n}A crooked smile briefly breaks through the seriousness.{/n}
"I am very practiced at commanding when afraid. You should not mistake the promise for a claim of mastery."
"I would rather know when we fail each other than have us pretend we cannot."
"Good. Then we may have an interesting time, and occasionally an unpleasant one."
{n}She holds out her hand, stopping halfway so you can choose whether to meet it.{/n}
"Come closer for a moment. I have spent a great many words explaining a wish that also has a very simple part."''',
        c('[Take her hand and sit close.]', "near"),
        c('"I want to keep the physical pace slow. I do want the courtship."', "slow")),
    n("near", "Soana", '''{n}Her palm settles against yours. She turns your joined hands so that neither wrist bears the weight, then draws you nearer by no more than the distance she has already offered.{/n}
"There," she says. "No witnesses required."
"You brought a letter."
"The letter has disgraced itself and is not invited."
{n}You laugh. She looks pleased, then unexpectedly shy beneath the pleasure. Her free hand brushes a thread from your sleeve. She leaves it there a moment longer than the task requires.{/n}
"I thought choosing would make me feel younger," she says. "It has made me feel very much myself. That is less familiar than I expected."
"I came for you."
"Yes. I am attempting to believe you without demanding that you repeat it until both of us are exhausted."
{n}She leans against your shoulder. The pressure is slight and deliberate. You stay that way while the light changes at the cave mouth. When she moves, it is to look at you again rather than withdraw.{/n}
"Next time I ask you to stay after dark, I would like you to know why. There may be no working, no visitor, and nothing in need of a guard. I may simply want you here."
"You can ask."
"I have begun."''', c('[Accept the courtship without promising a pace for every future night.]', flags=("soana.later_courting", "soana.promise_spoken"))),
    n("slow", "Soana", '''{n}She lowers her hand onto her own knee. This time the disappointment does not become a challenge.{/n}
"Slow, then. But not so carefully that we become afraid of enjoying anything."
"I am enjoying this."
"You have an alarming appetite for difficult conversations."
"You make them worth having."
{n}She considers that answer with an expression halfway between suspicion and pleasure.{/n}
"I shall try not to make it my only attraction."
{n}You sit beside her, close enough to share the sheltered part of the stone without touching. She tells you about a place upstream where the water sounds deeper than it is, and a hollow where owls used to nest. She does not turn either into a task.{/n}
"When I ask you to stay after dark," she says at last, "you may still answer that you want an evening and your own bed afterwards. I would prefer to know what you want than spend the evening guessing what you will permit."
"I will tell you."
"Good. I shall practice asking things I actually want."''', c('[Keep the courtship and its slower pace.]', flags=("soana.later_courting", "soana.later_slow", "soana.promise_spoken"))),
    n("friend", "Soana", '''{n}She nods. The movement is small, and she takes a moment before answering.{/n}
"Then I will stop leaving spaces in our conversations for an answer you have already given. That is my work, not yours."
"I want to keep coming."
"I know. You have made a rather convincing habit of it."
{n}She takes the bark from beside her and turns it over again. The blank side seems to give her an idea.{/n}
"I may finish the letter anyway. Not to persuade him to approve of a stranger, and not to ask you to become something else. There are things I have never managed to say to either of you because I was too occupied with predicting the reply."
"Would you like help?"
"No. I would like you to tell me if I begin reading it aloud without asking whether you wish to hear it. Friendship should have some defenses."
{n}Her smile returns, rueful but real.{/n}
"Come back when the shrine has stopped occupying every thought. We can take the upper path for a reason other than finding something wrong. I have not exhausted my capacity to enjoy someone who disagrees with me."
"That is fortunate."
"For both of us."''', c('[Keep the friendship she has accepted.]', flags=("soana.later_friends", "soana.promise_spoken"))),
], "soana.aftermath_heard", delay=48)

s("the_unwelcome_path", "The unwelcome path", '"Meret said you wanted me to hear a proposal of hers."', [
    n("start", "Soana", '''{n}Meret has brought a second hunter, a broad-shouldered man called Varn who keeps his bow on the ground while speaking to Soana. He does not look comfortable without it.{/n}
"I am not asking to settle here," he says. "I am asking to use the upper path when the river rises. Two families travel it. We can keep clear of the shelf."
"You can keep clear of the shelf now that someone else has made it safe to approach," Soana replies.
"Yes. That is why I am asking now."
{n}Meret glances at you, plainly relieved to have another person hear the exact shape of the argument.{/n}
"The lower crossing washed out last spring," she explains. "They went three days around. There were children with them, and one old man who could not keep up. He lived. Before anyone turns that into a tale about a dead man, he lived, and he was furious."
"A reasonable response to three unnecessary days," Soana says.
"Then let us avoid the next three."
{n}Soana taps her stick against the ground once.{/n}
"The upper path passes the hollow where the deer shelter in hard weather. A road is never only the feet of the first person who asks to walk it."''',
        c('"Walk it with us. Let us see where the trouble would be."', "walk"),
        c('"I cannot hear the whole proposal today. I will return."', abort=True)),
    n("walk", "Soana", '''{n}Soana agrees to the walk with such reluctance that Varn nearly thanks her for refusing. Meret retrieves his bow and hands it to him unstrung.{/n}
"We are looking at a path," she says. "You will not need to shoot it."
{n}The upper route narrows between two roots, then opens onto a strip of firmer ground. Soana points out the low branches that conceal the deer hollow from above. Varn notices the same thing for a different reason: the branches would make good shelter for a night's camp.{/n}
"No fires there," Soana says before he can finish the thought.
"We would not leave one burning."
"You would leave the smell, the cut branches, and the belief that the next traveler may do the same."
{n}He looks toward Meret, who declines to rescue him from the point.{/n}
"There is bare ground farther on," she says. "A cold camp could go there."
"Farther on is farther in the rain."
"Yes."
{n}Soana looks faintly pleased to hear someone else give that answer.{/n}
{n}At the bend, Varn stops beside a narrow cleft that would let travelers avoid the deer hollow entirely. Its floor is rough but passable on foot. A loaded handcart would not get through without widening it.{/n}
"We could cut this back," he says.
"You could carry less," Soana replies.
{n}Neither suggestion is impossible. Neither is free.{/n}''', c('[Ask each of them what they are willing to give up.]', "interests")),
    n("interests", "Soana", '''Varn answers first. "We can leave the carts below and carry the loads through. We cannot do that in one journey. Someone would have to watch the things left behind. And if we are already wet and cold, I will not promise that every traveler will find the same courage in a rule."
"Then do not promise for every traveler," Soana says.
"You keep asking for a guarantee nobody can give."
"I am asking you to notice the difference between permission and ownership. If I let your two families pass, I have not given you the roots to cut."
{n}Meret turns to Soana.{/n}
"What will you give?"
"My time deciding which ground can bear their feet."
"You have given that. What else?"
{n}Soana's expression hardens. For a moment it seems the visit may end there.{/n}
"I can mark the cold camp," she says at last. "I can leave a dry bundle beneath stone, enough to start a fire beyond the hollow if the weather is dangerous. I will not tend it every week for people who cannot be bothered to bring their own."
"We can replace what we use," Varn says.
"You can. Whether you will is what I shall discover."
{n}She looks toward you.{/n}
"And you? Are you here to recommend generosity with my ground, or do you have a preference you are willing to defend when someone dislikes it?"''',
        c('"Permit foot passage through the cleft, with loads carried in stages. Keep the hollow undisturbed."', "cleft"),
        c('"Permit the wider path only during dangerous river conditions. Mark a cold camp and forbid cutting."', "flood")),
    n("cleft", "Soana", '''"Then they carry," Soana says.
{n}Varn looks at the rough floor of the cleft. He lifts a loose stone with his boot, considers kicking it aside, and instead picks it up.{/n}
"We will have to clear the worst of these. No roots cut. Stones moved by hand."
"That I will allow."
"And we need somewhere dry for the loads while we go back."
{n}Meret finds a shallow overhang beyond the cleft. It will not hold all the baggage at once, but it will shelter the things most easily spoiled. Varn measures it against the length of his bow, calculating rather than arguing now.{/n}
"It costs us time," he says.
"It does," you answer.
"I would like that remembered when someone calls it an easy kindness to the forest."
{n}Soana gives him a searching look.{/n}
"I will remember. I have been the one carrying buckets around other people's easy answers."
{n}Together you move enough loose stones to make the first section safe. This is not a road for carts and nobody calls it one. Soana shows Varn where a footstep will break the edge above a root; he shows her where a person with a load cannot see that edge until too late. The final line curves farther outward than either first proposed.{/n}
{n}When you return to the cave, Varn has a route he dislikes less than the flooded crossing. Soana has kept the deer hollow quiet. Meret has agreed to show the two families the cleft once, not guide every later journey through it.{/n}''', c('[Record the limits in words all three have agreed to.]', "terms_cleft")),
    n("terms_cleft", "Soana", '''{n}Soana makes Varn repeat the part about roots before she repeats her own promise to leave emergency kindling beyond the hollow. He listens with an expression that suggests he will enjoy reminding her if she forgets.{/n}
"There," Meret says. "Now everyone has something to be irritated about. It may last."
{n}Varn goes ahead to fetch a second sack of supplies from his camp. The first practical test is simply whether the cleft will take the load he actually carries. When he returns, it does, though he has to turn sideways at the narrowest point.{/n}
"No widening," Soana says.
"I remember."
{n}His patience is thin. He still takes the narrow route.{/n}
{n}Later, alone with you, Soana watches the deer hollow from a distance. Nothing moves there while you wait.{/n}
"They may cease using it for reasons that have nothing to do with us," she says. "I know that. I still wanted to leave them the choice."
{n}She turns back toward the cave. She has gained no oath over Varn's descendants, only a limited agreement with an irritable living man. She seems prepared to defend that agreement just as fiercely.{/n}''', c('[Return with her by the path you have kept clear.]', flags=("soana.path_cleft", "soana.path_agreed"))),
    n("flood", "Soana", '''{n}Soana looks at the wider path, then down toward the river. She does not answer until the others have stopped preparing objections.{/n}
"When the lower crossing is dangerous," she says. "Not whenever the upper path is more convenient. No traps. No branches cut for bedding. No fires in the hollow."
"Agreed," Varn says quickly.
"Hear the rest before you discover how agreeable you are. You leave word when you pass, if I am here. If I am not, you leave the marker at the bend turned toward the river. I will know to look for disturbed ground before I take an animal trail."
{n}Meret proposes a marked stone rather than a carved post. A post might invite every traveler to treat the path as a road. Varn dislikes the obscurity but accepts it when Soana points out that his two families will be shown where it is.{/n}
{n}You walk the wider route together, choosing a cold camp beyond the hollow and a place for emergency kindling. Varn has to abandon the shelter he liked best. Soana has to accept that frightened deer may leave the hollow when the families pass.{/n}
"If they do," she tells you, "do not comfort me by saying they will certainly return. You do not know that."
"I won't."
"Good. I have enough work without correcting consolation."
{n}At the bend, she turns the marker toward the river herself, then turns it back. The two positions are clear even in dim light.{/n}''', c('[Make sure Varn can find the agreed marker and camp.]', "terms_flood")),
    n("terms_flood", "Soana", '''{n}Varn repeats the restrictions, this time without trying to shorten them. Soana repeats her promise to leave emergency kindling where a fire will not drive smoke into the hollow.{/n}
"And if someone ignores you?" you ask.
"I will find out who," she says. "I may be very unpleasant. I will not pretend a promise made by Varn tells me what every stranger deserves."
{n}Varn looks relieved until she adds that she knows exactly what he has promised.{/n}
{n}The first test is his own walk back with a full sack from camp. He uses the marked stopping place instead of the sheltered hollow. It is less comfortable. He says so, and remains there while he adjusts his load.{/n}
{n}After he leaves, Soana watches the trees above the deer path. A bird calls twice from the same branch.{/n}
"I wanted them farther away," she says. "I still do. But if the river takes one of those people while I congratulate myself on quiet trees, I shall have to live with that preference too."
{n}She gives you a hard look, forestalling any attempt to turn the admission into a general sermon.{/n}
"This crossing. These travelers. Do not arrive tomorrow with an army and quote me at myself."
"I understood the limits."
"Then we may get on tolerably well."''', c('[Return to the cave with the limited agreement intact.]', flags=("soana.path_flood", "soana.path_agreed"))),
], "soana.promise_spoken", delay=48)

s("after_the_last_visitor", "After the last visitor", '"You asked me to come when the others had gone."', [
    n("start", "Soana", '''{n}Soana is outside the cave, watching a pair of birds dispute a branch. She has a clean shawl around her shoulders, fastened with the same worn clasp you have seen before.{/n}
"They have been doing that since I came out," she says. "I was tempted to settle it. Then I remembered I had invited you for an evening in which I settled nothing."
{n}One bird gives up the branch and lands on a better one. Soana looks briefly offended by the ease of the solution.{/n}
"Meret has gone to the eastern paths. Varn knows the crossing. The bowl is sealed. If something needs my attention before morning, it will have to make a convincing noise."
{n}She turns toward you. Without a visitor waiting for judgment, the silence between you has a different weight.{/n}
"I wanted you here. I have been practicing saying that without attaching a task. How did I do?"''',
        c('"Very well. I wanted to come."', "consequence"),
        c('"I want the evening too, but I cannot stay now. May we choose another?"', abort=True)),
    n("consequence", "Soana", '''{n}You sit beside her outside the cave. Beyond the trees, the upper path is quiet.{/n}''',
        c('"Varn managed the narrow cleft with his load."', "cleft", requires=("soana.path_cleft",)),
        c('"He used the marked camp, even though he disliked it."', "flood", requires=("soana.path_flood",))),
    n("cleft", "Soana", '''"He did. He also called one of the stones a name I shall remember the next time I strike my foot against it."
{n}She glances at you, almost smiling.{/n}
"The deer came to the hollow this morning. Two of them. I watched until I began inventing reasons to keep watching, then left them to it."
"You could enjoy it without a reason."
"I am learning that at an inconveniently late hour."
{n}She turns back toward the cave.{/n}
"Varn will be cross when he carries the second load through. He will still be less cold than if he crossed the river. The deer will have a quieter hollow. Nobody will call it a glorious answer. I find I can bear the omission."
{n}She takes a burr from the edge of her shawl and tosses it into the grass.{/n}
"There. I have spoken about the path. If I begin again, remind me that I invited someone I find more interesting than a cleft in the ground."''', c('[Let the evening turn toward the two of you.]', "private")),
    n("flood", "Soana", '''"He did. I checked the hollow after he left. There were fresh tracks below it, but none inside. The deer may have heard us. Or they may have preferred another place. I managed to leave both possibilities alone."
{n}She glances at you, almost smiling.{/n}
"The kindling is where I promised. Dry. I inspected it twice, which was one inspection more than necessary."
"You expect him to inspect it too."
"Certainly. I intend to be irritatingly correct when he does."
{n}The pleasure she takes in that prospect is sufficiently familiar to need no explanation.{/n}
"I do not like a path that depends on people remembering limits," she adds. "I have also seen what becomes of a protection that never lets anything pass. I can dislike both. I have room."
{n}She takes a burr from the edge of her shawl and tosses it into the grass.{/n}
"There. If I begin discussing the crossing again, remind me that I invited someone I find more interesting than a marked stone."''', c('[Let the evening turn toward the two of you.]', "private")),
    n("private", "Soana", '''{n}The air cools. Soana rises and gestures toward the shelter of the cave. She has moved her tools away from the place where you usually sit. A folded blanket lies there instead.{/n}
"It is clean," she says. "I mention that before you decide I have become mysterious."
{n}She loosens the clasp of her shawl and hangs it on a peg. Her hair has escaped its tie at one temple. She catches you looking and leaves the strand where it is.{/n}''',
        c('"You have made room for me."', "desire", requires=("soana.later_courting",)),
        c('"I brought a story that has nothing to do with protecting anything."', "friend", requires=("soana.later_friends",))),
    n("desire", "Soana", '''"Yes. I did. I found it a more satisfactory occupation than wondering whether you would notice."
{n}She comes close enough to touch your sleeve, then waits. The waiting is intentional; so is the warmth in her expression.{/n}
"I want you to kiss me, hunter. Then I want you to stay. Choose one or both, and I shall judge you accordingly."
"And if I stay?"
"Then we discover what we both want after the first answer. I have no ceremony prepared. No flower that will make a marriage by being placed on someone's head. No spirit invited to witness what belongs to us."
{n}She gives a low laugh.{/n}
"I have become particular about invitations."
{n}You touch her hand. She turns it against yours, confident in the small movement now. Her other hand settles at your side and stays there. There is no doubt at all about her interest.{/n}
"Well? I can survive an answer. I would rather enjoy one."''',
        c('[Kiss her] "I\'m staying."', "night"),
        c('"I want the kiss. I will leave tonight, and come back another day."', "kiss"),
        c('"I want to stay beside you for the evening. Let us keep the rest slow."', "quiet")),
    n("night", "Soana", '''"Good."
{n}She draws you down by the hand she is already holding. There is no haste in the first kiss and a great deal of it in the second; she bites your lip, not gently, and laughs low in her chest when you pull her closer.{/n}
"I have imagined this often enough to leave out all the ordinary difficulties. The stone is hard. My shoulder will complain. You will discover that I have extremely firm opinions about where a blanket belongs."
"Show me."
{n}She does, and then she stops arranging anything. She unpins her braid with one hand and your collar with the other. Her fingers are rough as bark and very sure; she strips the road off you piece by piece, lets her rags fall in a heap across the tools, and pulls you down onto the blanket with a strength her age does not advertise. The last light leaves the cave mouth as she settles over you, her knees in the blanket on either side, and does not let you look anywhere but at her.{/n}
{n}In the morning, she is awake before you. Her hand rests over yours beneath the blanket.{/n}
"I have decided that you were worth moving the tools."
"High praise."
"You have not seen how long it took me to arrange them before you came."
{n}She kisses you once more before letting the day begin.{/n}''', c('[Leave when you must, with another visit wanted rather than owed.]', flags=("soana.later_night", "soana.lovers", "soana.progression_kept"))),
    n("kiss", "Soana", '''"Then I shall have to make the kiss worth returning for."
{n}She says it lightly. The hand against your side is less teasing. She waits until you lean toward her, then meets you with an eagerness she no longer tries to disguise.{/n}
{n}The first kiss of the evening is brief. The next lasts longer. You feel her smile before you see it, and when you draw back she keeps her hand on your sleeve.{/n}
"Well?"
"I would return."
"You might wait until you have left before promising that. It would make the judgment more impressive."
{n}You spend the remaining light beside her, sharing the blanket against the evening chill. She asks about something you have been looking forward to, and refuses to accept an answer consisting entirely of duties.{/n}
{n}When it is time to go, she takes her shawl from the peg and walks with you to the entrance, fastening the clasp as she goes.{/n}
"You told me what you wanted," she says. "I enjoyed it. We can manage an ending to an evening without turning it into an ending to everything."
{n}She touches your cheek once, then steps back to leave the path clear.{/n}''', c('[Kiss her goodbye and leave at the time you chose.]', flags=("soana.later_kiss", "soana.progression_kept"))),
    n("quiet", "Soana", '''"Then sit. I have made a space and intend to see it used."
{n}She settles beside you with the blanket over both your knees. After a while she asks whether you would like her hand. When you say yes, she places it in yours without adding another question behind the first.{/n}
"I am not waiting for you to be overcome," she says. "You may stop looking as if I am conducting an ambush."
"You are very good at waiting until the right moment to speak."
"A useful skill. Tonight I shall employ it only to make you laugh when you least expect it."
{n}She succeeds twice. Once by observing that Varn can now recite more of her words than he ever wished to hear; once by admitting that she had moved the tools three times before deciding the blanket needed exactly the space it now occupies.{/n}
{n}As darkness gathers, her head comes to rest against your shoulder. She asks first. For a while you listen to her breathing grow slower. Then she stirs and asks whether the birds have finally settled their quarrel.{/n}
{n}When you rise to leave, she keeps the blanket folded where you sat.{/n}
"I shall not put the tools back yet," she says. "I rather like the alteration."''', c('[Thank her for the evening and keep the pace you chose.]', flags=("soana.later_quiet", "soana.progression_kept"))),
    n("friend", "Soana", '''"An extravagant claim. Sit down and attempt it."
{n}You tell her about a traveler who tried to sell a mule by calling its refusal to move a sign of excellent judgment. She interrupts only to ask whether the buyer knew anything about mules. When you tell her how the argument ended, she laughs loudly enough to startle the birds outside.{/n}
"The mule was the wisest person present. I hope it received a share of the proceeds."
{n}She answers with a story of her own, about a festival singer who lost a wager and had to perform an entire song without mentioning the person it was written about. The audience supplied the missing name so enthusiastically that the song became much longer than intended.{/n}
{n}She interrupts her own story twice to imitate the singer's growing dismay. You sit until the cave mouth has become a dark shape against the last of the sky.{/n}
"I am glad you kept coming," she says at last. "I will not add a qualification. Enjoy the novelty."
"I am glad too."
{n}At the entrance she pauses beside the walking stick. Her hand rests on its worn head.{/n}
"The war may take you far from here. If you can return, I will want to hear what happened. If you cannot, do not invent a promise simply to make this evening end pleasantly. It has been pleasant already."
{n}You leave with the path clear and your place in her life named without disguise.{/n}''', c('[Take your leave as her friend.]', flags=("soana.later_friend_evening", "soana.progression_kept"))),
], "soana.path_agreed", delay=48)
