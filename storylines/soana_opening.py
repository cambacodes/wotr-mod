"""Development Soana introduction gated by native outcomes and live local contact.

Unity contact behavior and the complete route still require verification.
"""
from story_format import c, n, scene

SCENES = []
RELATIONSHIP = dict(
    Title="At the edge of her forest",
    Description="Soana has work for me at her cave. There are reeds to gather, a pot to mend and a question about Orso that she means to hear.",
    Objective="Return to Soana",
    Guidance="Speak to Soana at her cave after resolving the bear quest while she remains alive and willing to talk. Allow time between visits.",
    StartedFlag="soana.started", ClosedFlag="soana.closed", CommittedFlag="soana.committed",
    UnavailableFlags=["soana.dead", "soana.killed_by_camellia", "soana.forest_dead"], FailureFlags=[],
)


def s(id, title, entry, nodes, requires=(), delay=24):
    for page in nodes:
        page["Portrait"] = "SoanaForest" if id == "water_carrier" and page["Id"] in {
            "start", "promised", "work", "hands", "own_work"
        } else "Soana"
    SCENES.append(scene(
        "soana." + id, title, "Soana", 3, entry, nodes,
        Relationship="soana", Chapters=[3], last=3,
        Areas=["0a5654e7dc18f074d9356009d55eb51b"],
        AnswerLists=["2b1776f3e398685479ff6b16290b4cc2"],
        ContactUnit="64805abb52739e44280a758f850b300c",
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", *requires),
        forbids=("soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman"),
        delay=delay, optional=True))


s("threshold", "A way out of the basket", '"What work have you for me?"', [
    n("start", "Soana", '''{n}Soana peers past your shoulder. At the cave mouth, wicker scrapes against stone, falls silent, then scrapes again.{/n}
"Out of the light, child. I have a thief to deal with."
{n}Behind an overturned basket crouches a fox. A loop of the broken carrying strap grips one hind leg. Whenever it struggles, the basket strikes a stone and draws the loop tighter.{/n}
{n}Soana reaches for a folded cloth beside the basket. The fox bares its teeth.{/n}
"It came for a scrap of hide. Now it would rather have my fingers. Hold the basket. I will cut the strap."
{n}She closes and opens her small, dry hands. The swollen knuckles crack. She reaches down again.{/n}''',
      c('[Kneel beside the basket, leaving the cave mouth clear.]', "look"),
      c('"I cannot stay. I will leave the entrance clear."', abort=True)),
    n("look", "Narrator", '''{n}The fox jerks its leg. Soana stops, the cloth stretched between her hands. Beneath the loop, a raw line shows through the fur.{/n}
"An ordinary thief. Save your exorcisms."
"Can you cut the strap without pinning it down?"
"When it stops trying to drag its bones through that crack."
{n}You could ease the basket around the stone to widen the opening. The fox watches every movement of your hand. Soana's knife lies beside her on a flat stone.{/n}''',
      c('"Move the basket a little at a time. Let it find the larger gap before you reach for the strap."', "wait", flags=("soana.fox_waited",)),
      c('"Cover its eyes. I will hold the basket while you cut. We should end this quickly."', "hold", flags=("soana.fox_held",))),
    n("wait", "Soana", '''"And if the little fool sits there until nightfall?"
"The cloth will still be here."
{n}Soana glances at the strip of sunlight on the cave floor. She drops the cloth into her lap. You ease the basket away from the stone. The fox lunges; you stop before the wicker strikes it.{/n}
"Less. You are moving a basket, not uprooting an oak."
{n}You shift it a finger's width. This time the animal stays still. Between the wicker and the rock, the opening widens. You hear its quick breathing.{/n}
{n}Soana reaches toward the knife. You shake your head. Her look would sour milk, but her hand falls back to her knee.{/n}
{n}The fox sniffs the gap, lowers its head and steps forward. The strap slackens. Soana slips her knife beneath the loop and cuts outward, away from the leg.{/n}
{n}The fox scrambles free. It sets its injured foot down cautiously, then limps into the bracken.{/n}''',
      c('[Release the basket and sit back on your heels.]', "wait_cost")),
    n("wait_cost", "Soana", '''{n}Soana lays the severed strap across her knee.{/n}
"Gone. And my hide with it, I'll wager."
{n}The scrap has vanished.{/n}
"Half an afternoon to show a fox three steps."
"It took them."
"Pff. With stolen goods in its teeth."
{n}She turns the cut strap over. Outside, the trees cast long shadows. The sunlight has left the cave floor.{/n}
"Too late for the reeds now. Dry ones, for a carrier. That thief has left me two things to mend."
"I can bring a bundle next time."
"Dry reeds. Bring green stalks and you can sit here until they dry."
{n}She puts a clean, pale length in your hand. When you reach for a thicker sample, she raps your fingers with it.{/n}
"That one. Look at it before you start pulling things out of my forest."''',
      c('"Show me where they grow. I will bring dry reeds tomorrow."', "end_wait", flags=("soana.reeds_promised",)),
      c('"I cannot come tomorrow. Keep that reed to show me when I return."', "end_wait")),
    n("hold", "Soana", '''{n}You steady the basket. Soana throws the cloth over the fox's head and shoulders. It twists beneath the folds, knocking her hand against the stone.{/n}
"That corner! Hold the basket, not its leg."
{n}You press down on the wicker. Her knife cuts the strap on the second attempt. She lifts the cloth, but the fox drags its freed leg across the basket's broken edge. Blood streaks the wicker.{/n}
{n}It bolts through the cave mouth into the bracken. Soana remains on her knees. A bead of blood rises on her scraped hand.{/n}
"There. Off with you, ungrateful beast."
{n}Your gaze catches on the bloodied wicker. Soana follows it.{/n}
"I saw. It would not keep still."
"We knew it wouldn't."
{n}She folds the cloth over the stain, pressing it flat with her thumb.{/n}
"Yes. We knew."''',
      c('"Next time, move the basket first. Give it a wider way out before we grab it."', "hold_room", flags=("soana.fox_reconsidered",)),
      c('"The strap had to come off quickly. Next time, pad the broken edge first."', "hold_pad", flags=("soana.fox_expedience",))),
    n("hold_room", "Soana", '''"Your hand was on the basket too."
"Next time it will move the basket first."
{n}She unfolds the stained cloth and leaves it beside the knife.{/n}
"There. A fine bit of work for both of us to look at. Spare me the sermon."
"Will you try the wider gap?"
"When there is a fox to put through it! Shall I swear an oath to an empty floor?"
{n}She pushes herself upright with her unhurt hand. You hold the basket while she cuts away the rest of the broken strap. The stained cloth stays beside the knife.{/n}''', c('[Help her put the basket aside.]', "end_held")),
    n("hold_pad", "Soana", '''"Fetch the felt under that pot. Fold it twice."
{n}You bring her the worn scrap. She binds it over the broken wicker with the remaining strap, then tugs until no rough edge shows.{/n}
"There. Let the next thief chew that. You can use your eyes before we put another creature under your hands."
"I will pad the edge first."
{n}She turns your hand over, inspecting the fingers that held the basket.{/n}
"And keep those away from its teeth. I have enough to mend."
{n}Daylight remains. She takes a small sickle from beside the cave wall and leads you to the reeds. You carry the repaired basket. She cuts the dry stalks and leaves the green ones standing.{/n}''', c('[Bring the reeds back with her.]', "end_held")),
    n("end_wait", "Soana", '''{n}Soana lifts the damaged basket. The severed strap dangles against her sleeve.{/n}
"I will cut off the other loop before another thief finds it. Go tell your soldiers you conquered a basket."
"Will you bear witness?"
"Bring trumpets and I will set the fox on them."
{n}You laugh. She turns the basket over and begins picking at the remaining strap.{/n}
"Come by daylight next time. The water pot's cradle is splitting. We shall see what your patient hands can do with a reed."''',
      c('"I would like to come again."', flags=("soana.threshold_kept",)),
      c('"I will help with the pot. Keep the sermons short."', flags=("soana.threshold_kept", "soana.work_first"))),
    n("end_held", "Soana", '''{n}Soana sets the basket beyond the narrow animal track. She flexes her scraped hand, scowls at it and tucks it into her sleeve.{/n}
"The water pot's cradle is broken too. Come by daylight if you want work. Clay has no teeth."
"That sounds better."
"It has water. Mend it badly and you will carry a bootful home."
{n}A crooked smile pulls at her mouth. She rubs the scraped hand through her sleeve, then points you toward the path.{/n}
"Mind the bracken. Our thief is in there somewhere."''',
      c('"I would like to come again."', flags=("soana.threshold_kept",)),
      c('"I will help with the pot. Keep the sermons short."', flags=("soana.threshold_kept", "soana.work_first"))),
], delay=0)


s("water_carrier", "The weight of water", '"You said the water pot needed a carrier."', [
    n("start", "Narrator", '''{n}Soana has dragged an empty clay pot into the daylight. Its sides are sound, but one handle of the wicker cradle has split. Beside it lie an awl, a shallow dish of water and lengths of reed.{/n}
"The pot outlasted its handle. I will not throw good clay away because some fool hurried the weaving."
"Which fool?"
"The one who is mending it. Sit. Keep your shadow off my hands."''',
      c('[Set down the promised dry reeds and take the place she indicates.]', "promised", requires=("soana.reeds_promised",)),
      c('[Sit beside the pot and examine the broken handle.]', "work", forbids=("soana.reeds_promised",))),
    n("promised", "Soana", '''{n}Soana sorts your bundle. She throws two stalks aside and lays the others within reach.{/n}
"These will do."
"Only those?"
"Must I sing a blessing over each reed? They are good. Give me the awl."
{n}She lays the rejected stalks across the water dish, pinning down the soaking lengths. Their bent ends stick out beyond the rim.{/n}''', c('[Hold the cradle while she loosens the broken weave.]', "work")),
    n("work", "Soana", '''{n}Soana pushes the awl beneath a tight crossing and twists out the broken strip. You hold the cradle against your knees, taking its weight off her hand.{/n}
"Under this one. Over that. Leave a tail, or you will have nothing to turn back."
{n}Your reed cuts diagonally across the old weave. She hooks it with the awl and makes you draw it out. On the second attempt it bends without splitting.{/n}
"Better. You are weaving a cradle, child, not a cage. I still have to take the pot out to wash it."
{n}She reaches between your hands to turn the loose end. Her fingers brush yours, warm and dry. She leaves her thumb against the reed while you draw it through.{/n}''',
      c('[Ask her to guide the next crossing while you hold the reed.]', "hands", flags=("soana.accepted_guidance",)),
      c('"Let me make the next crossing myself. Tell me if I miss it."', "own_work", flags=("soana.tried_weave",))),
    n("hands", "Soana", '''{n}She puts two fingers over yours and turns the reed edgewise.{/n}
"There. All that strength, and you were pushing against the weave."
{n}You follow her fingers. The reed slides through. She withdraws her hand and taps the next crossing with the awl. This time you thread it yourself.{/n}
"Hah. Something got through that thick skull."
{n}She tugs the finished strip, then slides another reed across your knee.{/n}''', c('[Finish the row.]', "flowers")),
    n("own_work", "Soana", '''{n}Soana rests the awl across her knees. At the last crossing, your fingers stop between two strips.{/n}
"Follow it back. It has not changed its path to spite you."
{n}You trace the strip and slip the reed beneath it. She presses her thumb into the finished row.{/n}
"That will hold."
"You waited for me."
"The reed was not running away. The pot was empty. Even you had time."''', c('[Finish the handle.]', "flowers")),
    n("flowers", "Soana", '''{n}The new handle is pale against the old wicker. Soana rubs the join and turns it toward the cave wall, then back into the light.{/n}
"There. Let it show. I want to see if it pulls loose."
{n}A small white flower lies tangled among your reeds. You lift it out before the next crossing crushes it.{/n}''',
      c('"Would you like this?" [Offer her the flower.]', "flower", flags=("soana.flower_offered",)),
      c('[Lay the flower beside the water dish and ask how she learned this work.]', "learned")),
    n("flower", "Soana", '''{n}She takes the flower by its stem. Her lips draw tight.{/n}
"Flowers like these grew in Orso's tracks. At the Sun Festival, you could follow them through the wood. Corven made me a wreath. I wore it when I became his wife."
{n}She rolls the stem between her fingers and looks up at you.{/n}
"What are you staring at? Did you think I had never worn flowers?"
"I was wondering how this one would look in your hair."
"One flower? Corven brought an armful."
{n}She lays it across the dish. The blossom stays above the water, its stem dipping below the rim.{/n}''',
      c('"Corven, then. I will remember his name."', "marriage", flags=("soana.marriage_acknowledged",)),
      c('"Keep it as thanks for the lesson. I meant nothing more."', "thanks", flags=("soana.flower_thanks", "soana.marriage_acknowledged"))),
    n("learned", "Soana", '''"A handle breaks. You mend it, or drink on your knees at the stream. That teaches quickly enough."
{n}Her eyes fall on the flower beside the dish.{/n}
"Corven had a better use for weaving. He made my wreath from the flowers in Orso's tracks. I wore it when I became his wife. Our children I washed in the holy spring. Strong children."
{n}She presses a loose reed down with her nail.{/n}
"Now there are reeds, and a pot to carry. Hold that end."
"Did he teach you?"
"I could weave before I married, child. He put flowers on my head, not wit in it."
{n}The little flower rocks against the dish as she pulls the next strip taut.{/n}''',
      c('[Repeat Corven\'s name, then take up the loose reed.]', "marriage", flags=("soana.marriage_acknowledged",))),
    n("marriage", "Soana", '''{n}Soana pulls the last reed through the handle and trims it. Her knife scrapes against the old wicker. Water drips from the cut end onto the stone.{/n}
"That is enough about Corven. There is work here, and your army has not turned into trees while you sat idle."
{n}She fits the pot into its cradle and thrusts the handle toward you.{/n}
"Take it to the stream. Empty first! I will watch that join. If your weaving comes apart, you can fish the pot out yourself."''', c('[Take the carrier and walk beside her.]', "stream")),
    n("thanks", "Soana", '''"Then fetch the pot, before you thank me for teaching you to break it."
"I was wondering whether the handle would hold."
"Use your hands and find out. Your tongue has worked enough."
{n}She settles the pot into its cradle and gives you the handle. The flower remains beside the water dish. She glances back at it once before following you down the path.{/n}''', c('[Carry the empty pot while she watches the join.]', "stream")),
    n("stream", "Narrator", '''{n}The path descends to a shallow run between stones. Soana braces a hand against a tree, tests the lower foothold and steps down. You stand beside the pot until she reaches you.{/n}
{n}She lowers it into the stream. When she hands it back, the repaired handle takes the weight. The wicker creaks once and holds.{/n}
"Slowly up the hill. Spill it and you will be coming back down."
{n}On the return she stops beside a tree. Her breath rasps. She plants each foot before lifting the other; when you turn toward her, she raises a finger beneath your nose.{/n}
"Drink that water if your mouth is itching. Spare me your advice."''',
      c('[Flirt] "I would kiss those hands, if they were not busy threatening me."', "attraction", forbids=("soana.flower_thanks",), flags=("soana.attraction_named",)),
      c('"The work was worth doing. I would help again."', "company", flags=("soana.practical_company",))),
    n("attraction", "Soana", '''"A bold mouth for a fool who can scarcely thread a reed."
{n}She looks down at her dry, crooked fingers on the bark, then back at your face.{/n}
"These hands? You would kiss these?"
"Yes. And the woman they belong to. I heard you about Corven."
{n}One corner of her mouth lifts. She catches your sleeve between two fingers.{/n}
"You heard a little. Do not grow clever on it."
"I haven't forgotten your temper either."
"You have scarcely felt it. Come back with green reeds and you will."
{n}She releases your sleeve and pushes away from the tree. You smooth the fold her fingers pulled in the cloth.{/n}
"Bring the water, then, before I die of thirst listening to you."''', c('[Walk beside her and carry the water back.]', "finish")),
    n("company", "Soana", '''"You will find work here. Heavy work, if you keep offering so lightly."
"The pot is a good start."
{n}She tests the ground with her foot and pushes away from the tree.{/n}
"Carry it on this side. I want to see if the new handle pulls crooked. And walk beside me. I cannot inspect it through your back."''', c('[Walk beside her and carry the water back.]', "finish")),
    n("finish", "Soana", '''{n}At the cave you lower the pot onto level stone. Soana runs a finger beneath the damp join. The weave has held.{/n}
"Bring that question next time. It has been rattling in your head all afternoon. I could hear it over the reeds."
"About Orso?"
"What else? Every bloody hunter who comes here has something to say about my bear."
{n}She lays the knife beside the awl, clear of the full pot.{/n}
"Come, then. Bring your argument. And drink first. I will not have you coughing through mine."''', c('"I will come back to speak about Orso."', flags=("soana.water_kept",))),
], requires=("soana.threshold_kept",))


s("guardian_question", "What a protector may demand", '"You asked me to bring my question about Orso."', [
    n("start", "Narrator", '''{n}Soana sits beside the repaired water carrier. Her fingers have darkened the pale reed at the handle. The pot stands between her knees and the bare patch of stone beside her.{/n}
"Sit. There is water. Get your question out before the cup grows moss."
{n}She shifts the pot aside with her heel. The knife lies beside the awl, where she left it after the mending. Her eyes follow you as you sit.{/n}''',
      c('"Orso still guards the forest. Can he ever leave the duty you bound him to?"', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead", "soana.medallion_pulverized")),
      c('"Orso is dead. You spoke of finding another guardian. What would you do differently?"', "dead", requires=("soana.bear_dead",)),
      # Polish (Sol CAN): the medallion bitten to dust (SoanaBear/Cue_0023) withers Orso with no BearDead etude.
      c('"Orso is dead. You spoke of finding another guardian. What would you do differently?"', "dead", requires=("soana.medallion_pulverized",), forbids=("soana.bear_dead",))),
    n("bound", "Soana", '''"Grass feeds the deer. The deer feed the smilodons. Orso guards the wood. You have seen what prowls beyond it."
"And you bound him to that duty."
{n}Her shoulders rise beneath the worn cloth.{/n}
"Shall I loose him, then? You can stand in his place. Every hollow, every night. Bring your soldiers out from behind their walls!"
"I cannot guard all of it."
"No. But you can tell me how to guard it."
{n}She scoops water into the cup, drinks and sets it down hard.{/n}
"I knew Orso when flowers grew beneath his feet. My friend. You think I mistook that thing from the Abyss for him? I knew what I was binding."
"And you did it anyway."
"Yes, child. The forest was dying. I did it."''', c('[Answer her.]', "position", flags=("soana.orso_bound_discussed",))),
    n("dead", "Soana", '''"A spirit that will bear the binding. An animal that will survive it. Neither grows on a tree for me to pluck."
"That is the same thing again."
{n}Soana turns on you.{/n}
"And what have you brought instead? A mouthful of questions! The guardian is dead. Shall I lie down beside him and let the Wound take the trees? Would that satisfy you?"
{n}Her knee knocks the carrier. She catches the pot with both hands before it tips, then drags it back against the stone.{/n}
"Orso was my friend. I knew him before you were born. Do not tell me what I have lost."
"Another creature will not take his place."
"Do you think I am looking for a friend? I am looking for something that can keep this forest alive!"''', c('[Answer her demand for a guardian.]', "position", flags=("soana.orso_dead_discussed",))),
    n("position", "Soana", '''"Enough circling, child. What do you want from me?"
{n}Her hands grip the pot's rim. A drop of spilled water runs over one knuckle. She wipes it on her sleeve and glares at you.{/n}''',
      c('"A different method. I will help look for one, but I will not praise another binding merely because you call it protection."', "alternative", flags=("soana.seeks_alternative",)),
      c('"I have sent others into danger to save lives. Your binding kept the forest alive, but Orso bore it. Help me find a way to end that burden."', "command", flags=("soana.accepts_hardship",)),
      c('"I cannot court you while this stands between us. The pot is mended. I will go."', "leave", flags=("soana.closed",))),
    n("alternative", "Soana", '''"Look where? Under a stone? In your reed basket?"
"You know the forest. I can bring accounts of other workings. Read one."
"Mages' workings, I suppose. Dig in the dark, wake what sleeps there, then howl when it eats your city. Sarkoris had enough of those."
"Read it. Then tell me where it fails."
{n}She barks a laugh.{/n}
"I could tell you now."
"You could guess."
{n}Her hands come off the pot. She plants one against the stone, half rising, then settles back with a scowl.{/n}
"One account. You will read it first. No scholar's rubbish passed along because the scroll looked costly."
"And if it works?"
"Bring it here before you crow. I have heard enough victories proclaimed over empty hands."''', c('"One account, then. We will see what it is worth."', "memory")),
    n("command", "Soana", '''"You have sent people to their deaths. I can hear it."
{n}She rubs her thumb over the carrier's new handle.{/n}
"Can they put down their spears and walk away? Or do your orders bite harder than my binding?"''',
      c('"They can refuse. I would have to fight without them."', "command_refusal"),
      c('"I give orders and expect obedience. But if my orders destroy the army, I change them."', "command_orders"),
      c('"I have given bad orders too. Blaming you will not mend them. Let us find a better way here."', "command_regret")),
    n("command_refusal", "Soana", '''"And those they leave behind? The wolf does not ask which shepherd threw down his staff."
"You asked whether they could leave. They can."
{n}She glances at her swollen knuckles and folds her hands over the handle.{/n}
"Then find something that will stay. I cannot set your fine words to watch the trees."''', c('"Will you look at another working if I bring it?"', "cost")),
    n("command_orders", "Soana", '''"Hah. There is a commander under all that soft talk."
"You asked."
"And your orders are always wise, I suppose? Your dead were all well spent?"
"I will not call a ruined army a victory. Nor a ruined guardian."
{n}Soana rubs a rough splinter off the handle. She drops it into the dirt.{/n}
"Then bring your better way. We shall see how you speak when it is your work under the knife."''', c('"Will you look at another working if I bring it?"', "cost")),
    n("command_regret", "Soana", '''"I did not ask you to weep over your dead."
"I am not. I have given bad orders. I would rather we found a better way here."
{n}Her thumb stops against the reed.{/n}
"The axe has fallen. Wishing it back into your hand does not mend the tree."
"Then let us look before the next stroke."
"Look, then. Bring me something besides an axe and a sigh."''', c('"Will you look at another working if I bring it?"', "cost")),
    n("cost", "Soana", '''"I will read it. If it is foolish, you will hear that too."
{n}She looks out through the cave mouth at the trees.{/n}
"A working, a record, something from a shaman who lived through this land. Bring that. No more judgments carried here in an empty basket."
"Read it before you curse its author."
"Do not ask for miracles. I can curse and read at the same time."''', c('"I will search for an account worth bringing."', "memory")),
    n("memory", "Narrator", '''{n}Soana draws the pot nearer and fills the cup. She rubs a fleck of dirt off its rim with her thumb before thrusting it into your hand.{/n}''',
      c('[Remember the fox finding its own way out.]', "fox_wait", requires=("soana.fox_waited",)),
      c('[Remember the blood on the wicker and the wider gap you proposed.]', "fox_change", requires=("soana.fox_reconsidered",)),
      c('[Remember the bloodied leg and the felt over the broken edge.]', "fox_speed", requires=("soana.fox_expedience",))),
    n("fox_wait", "Soana", '''"Do not say it."
"Say what?"
"Push the forest a little to the left. Perhaps the Abyss will trot through the gap and leave us alone."
"I was remembering the fox. You waited."
{n}She points at the knife beside the awl.{/n}
"That was ready if the fox stayed caught."
"You left it on the stone."
{n}She snorts and holds out her hand for the cup. When you raise it for another swallow, she drops her hand back to her knee.{/n}''', c('[Ask what to bring on your next visit.]', "terms")),
    n("fox_change", "Soana", '''"I left the bloody cloth by my knife. You saw."
"I remember."
"I washed it this morning. Blood brings flies. There is no wisdom in sitting among flies."
"Did the blood wash out?"
"Most of it."
{n}She shows you the scrape on her hand. A dry scab covers it.{/n}
"And this will close. The fox is still limping somewhere. Find me something that does better than leaving another scar."''', c('[Ask what to bring on your next visit.]', "terms")),
    n("fox_speed", "Soana", '''"Your hand held that basket down. Remember it before you start preaching about my bear."
"I remember the blood. The felt will save the next leg. It did nothing for that one."
"No."
{n}She drinks from the cup, watching you over its rim.{/n}
"Good. At least you have not washed your hands and called yourself spotless. Bring the account. We shall see if it holds up as well as your wicker."''', c('[Ask what to bring on your next visit.]', "terms")),
    n("terms", "Soana", '''"Bring your account. I will read it."
"And if it is useless?"
"Then you can take it away again. Perhaps its author can weave it into a better basket."
{n}She puts the empty cup beside the pot and picks a loose thread from her sleeve.{/n}
"Come by daylight. I will not burn good oil for a mage's scrawl."''',
      c('"I would still like the afternoon in your company."', "warm", requires=("soana.attraction_named",)),
      c('"Then I will return with the account."', "practical")),
    n("warm", "Soana", '''{n}Soana narrows her eyes at you. Her thumb catches the thread again and snaps it.{/n}
"You want an afternoon of being scolded?"
"With you? Yes."
"Fool. You could get that from any old woman in a village."
"I came here."
{n}She catches your wrist as you reach for the cup and pushes it toward the full pot.{/n}
"Drink before you go. And bring a legible account. I will not waste daylight on scratches when I could be looking at you."
{n}Her mouth crooks. She gives your wrist a shove toward the water.{/n}
"The cup, child. You have forgotten what it is for."''', c('[Take a last drink and leave to find the account.]', flags=("soana.inquiry_invited", "soana.opening_kept"))),
    n("practical", "Soana", '''"Good. Something useful has come out of all this noise."
{n}She rises and lifts the carrier into the shade. The new handle holds without a creak.{/n}
"Legible writing. Bring me a scroll full of a scholar's flourishes and you can read it aloud. Every word. Let your tongue trip over his folly."
"That could take all afternoon."
"Then start early. I have no wish to listen to you after dark."
{n}She turns the pot so the repaired handle faces the light, then waves you toward the path.{/n}''', c('[Leave to search for another way to guard the forest.]', flags=("soana.inquiry_invited", "soana.opening_kept"))),
    n("leave", "Soana", '''{n}Soana takes her hands off the pot.{/n}
"Go, then. The path is where you left it."
"The handle should last."
"It holds water. So far it has done better than your argument."
{n}She turns the cup upside down on the stone. As you reach the cave mouth, she tugs at the new handle once more. It creaks but holds. She sets the pot in the shade and takes up her knife.{/n}''', c('[End these private visits.]')),
], requires=("soana.water_kept",))
