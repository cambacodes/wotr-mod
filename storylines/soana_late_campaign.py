"""Earned living Chapter 5 Soana return and authored campaign conclusions.

Contact remains the native Wintersun unit; no actor, guardian or forest is restored.
New people, temporary rites and local incidents exist in dialogue, not world-state APIs.
"""
from copy import deepcopy
from story_format import c, n, scene

SCENES = []
ACTOR = "64805abb52739e44280a758f850b300c"
ANSWERS = "2b1776f3e398685479ff6b16290b4cc2"
WINTERSUN = "0a5654e7dc18f074d9356009d55eb51b"
LOSS = ("soana.dead", "soana.killed_by_camellia", "soana.forest_dead")


def s(id, title, entry, nodes, previous, delay=24):
    for page in nodes:
        page["Portrait"] = "Soana"
    SCENES.append(scene("soana." + id, title, "Soana", 5, entry, nodes,
        Relationship="soana", Chapters=[5], last=5, ContactUnit=ACTOR,
        Areas=[WINTERSUN], AnswerLists=[ANSWERS],
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", "soana.progression_kept", previous),
        forbids=(*LOSS, "soana.closed", "inhuman"), delay=delay, optional=True))


s("when_the_road_returns", "When the road returns", '"I wondered what you would say when I came back."', [
    n("start", "Soana", '''{n}Soana turns at the sound of your voice. She has a small bundle of roots in one hand. For a moment she simply looks at you. Then she puts the roots down in a place where they promptly begin to roll apart.{/n}
"Something sharper. I had an excellent beginning prepared."
{n}One root reaches the edge of the stone. She catches it without looking away from you.{/n}
"You have been gone long enough for me to improve it several times. Now I shall have to make do with what occurs to me."
"I came back."
"Yes. I can see that. Do not require me to make it a sensible matter immediately."
{n}She leaves the scattered bundle where it is and comes toward you.{/n}''',
        c('[Meet her as the woman you have been courting.]', "welcome", requires=("soana.later_courting",)),
        c('[Greet the friend whose company you have missed.]', "friend", requires=("soana.later_friends",)),
        c('"I cannot stay yet. I wanted you to know I was here."', abort=True)),
    n("welcome", "Soana", '''{n}She holds out both hands. You take them, and she draws you close enough to examine your face without tilting her head so far.{/n}
"There. That is a more useful distance."
"For examining me?"
"Among other things. I shall ask before undertaking a more thorough examination."
{n}Her smile arrives slowly, then gives way to an expression less easily teased away.{/n}
"I wanted to know whether you would still want to stand here. I disliked having to wait for the answer. I am pleased with the one I have."
"I missed you."
"Tell me something of it while we walk. Not every danger. Something you wished I had been there to hear."
{n}She keeps one of your hands while reaching for her stick with the other. At the first uneven patch she lets go to find her footing, then offers her hand again when the ground permits it.{/n}
"And if there is something you cannot tell me yet, say that. I have managed not knowing. I shall not promise to enjoy further practice."''', c('[Walk with her toward the nursery.]', "nursery")),
    n("friend", "Soana", '''"You have come back with the same unfortunate opening. I ought to have taught you better."
"You could begin again."
"An alarming proposal. We should first discover whether I am pleased to see you."
{n}She picks up her stick and gestures for you to come beside her. The roots remain scattered on the stone.{/n}
"Leave those. They will not become less edible because someone saw me hurry."
{n}You tell her one small thing you remember from the road: a place where the wind sounded as though it were moving water, until you found only dry grass. She listens, asks which way the ground sloped, and lets the description remain a description after you answer.{/n}
"I should have liked to hear it," she says. "I am pleased you thought of telling me. There. We have settled the question without beginning our entire acquaintance again."
{n}She turns toward the nursery path. You walk beside her, matching the pace she chooses.{/n}''', c('[Ask what the nursery looks like now.]', "nursery")),
    n("nursery", "Narrator", '''{n}The path is familiar enough for you to anticipate its turn. Soana notices when you avoid the loose stone without being told.{/n}
"Some education survives travel," she says.
{n}She stops where the young trees stand, or stood, between the sheltering banks.{/n}''',
        c('[Look at the trees she carried the voice to save.]', "saved", requires=("soana.nursery_saved",)),
        c('[Look at the ground the working left bare.]', "lost", requires=("soana.nursery_lost",))),
    n("saved", "Soana", '''"Two died despite all our cleverness. A third has grown sideways as if to demonstrate its independence."
{n}She points out the crooked sapling. The surviving leaves look ordinary, which is startling after remembering what they cost her.{/n}
"The nights stopped speaking in borrowed voices," she says. "Eventually. I had an afternoon when I caught myself being angry about something entirely new. It was a relief."
"You could have told me that first."
"I wanted to show you the trees. I still choose them. I have not spent your absence turning my answer into a mistake so that our next meeting might be easier."
{n}She bends the crooked stem gently, tests its spring, and leaves it pointing where it was.{/n}
"Nor have I discovered what became of Corven. A stolen voice was never news. Some days I remember the sound. Most days I remember something less convenient for a hungry thing to imitate. The way he used to laugh before I reached the end of a complaint, for instance."
"Was he usually right?"
"Frequently enough to be irritating. I miss that too."''', c('[Return toward the upper path with her.]', "path")),
    n("lost", "Soana", '''{n}There are seedlings in the sheltered corner, spaced widely enough that the bare ground remains visible between them. Soana kneels to lift a fallen twig from one.{/n}
"Meret's seed. A little of it came up. I was tempted to count the new shoots every morning. I restricted myself to every other morning and felt exceptionally reasonable."
"You have begun again."
"Yes. The dead stems did not turn green because I decided to be industrious. Those are still there."
{n}She indicates the pale sticks farther up the slope. Nothing is growing against the dry ridge where the thing was contained.{/n}
"I have not opened the bowl. I have not reopened the shrine. A quiet season is not an invitation to poke at the answer."
{n}She rises and brushes soil from her palm.{/n}
"Come. Meret has found something she wants me to see before she leaves. I had begun to suspect that you would arrive only after I had found a satisfactory way to be angry about it. You have interrupted the process."''', c('[Ask what Meret found.]', "path")),
    n("path", "Soana", '''{n}At the upper bend you find Meret waiting with a cut length of wire wrapped around a stick. Her bow is on her back. The worn family mark hangs at her belt.{/n}
"There are snares beyond the hollow," she says. "Not ours. Fresh cuts where someone has taken hazel, and sacks dragged along the ground. I found this one empty. I did not walk through the rest to make sure."
"A welcome survival of good sense," Soana says.
"I have to leave with my camp. That has survived too."
{n}Soana's mouth tightens. Meret turns to you.{/n}
"I said I would look at the eastern paths when I was here. I looked. Now I am telling her what I saw before I go. I am not handing you my place for the rest of your life either."
"I had not offered it," you say.
"Good. We may finish this conversation before the roots grow over us."
{n}Soana examines the wire without unwrapping it. Then she looks toward the route you helped agree upon.{/n}''',
        c('"We kept the carts out of the cleft. This is something else to investigate."', "cleft", requires=("soana.path_cleft",)),
        c('"The flood passage did not authorize snares. We should find who put them there."', "flood", requires=("soana.path_flood",))),
    n("cleft", "Soana", '''"Varn still carries his loads through. He has acquired a more varied vocabulary for the narrowest part. I hear it before I see him."
{n}Meret makes a short, appreciative sound.{/n}
"Someone has been walking beyond the carrying path," Soana continues. "That does not make every person who used it responsible. Nor does it make the cut branches less cut."
"What would you have done before I returned?"
"Followed the trail. Then decided whether the people at its end were more use frightened or listening. I have not forgotten either method."
{n}She hands the wire back to Meret.{/n}
"Leave that outside the cave. I want to recognize another piece of the same work when I see it."''', c('[Agree to inspect the eastern ground in daylight.]', "end")),
    n("flood", "Soana", '''"The families used their permission twice. They left the marker as agreed. The kindling was replaced, though one bundle had more damp twigs than I should have accepted from a child."
"Did you tell Varn?"
"In sufficient detail."
{n}Meret turns her face aside to hide a smile.{/n}
"This wire was beyond the permitted camp," Soana continues. "I want to know whose hands put it there. Then I want it out. That need not wait until I have decided how charming to be about the people attached to those hands."
{n}She gives the wrapped wire back to Meret.{/n}
"Keep it where I can compare it with the rest. No bare fingers on the loop. It was made by somebody who expected resistance."''', c('[Agree to inspect the eastern ground in daylight.]', "end")),
    n("end", "Soana", '''{n}Meret promises to show you the beginning of the trail before her camp leaves. Soana begins to ask for more time, stops, and asks for the place where Meret will leave her last report instead.{/n}
"Here," Meret says. "With you. I can stay for the inspection. After that, you will have to decide without my grandmother standing conveniently behind me."
"Your grandmother knew when to stop enjoying a point."
"No, she didn't."
{n}Soana's answer is a reluctant snort. Back at the cave, she retrieves the scattered roots and puts them in their basket. Then she turns to you.{/n}
"I have something disagreeable to deal with. I am also glad you came. The first fact has not swallowed the second."
{n}She touches your forearm briefly, without making the touch a request for service.{/n}
"Come when we can see the ground. Bring boots you can bear to get muddy. I have had enough of people declaring themselves ready while dressed to be admired."''', c('[Return for the trail, with the welcome remembered.]', flags=("soana.late_returned",))),
], "soana.progression_kept", delay=0)

s("a_track_with_two_ends", "A track with two ends", '"Show me where Meret found the wire."', [
    n("start", "Soana", '''{n}Meret leads you from the cave to a patch of churned earth beyond the upper bend. Soana follows with a short hooked stick. She has wrapped cloth around its lower end so that it will not slide in a tightened loop.{/n}
"For lifting what we have seen," she says. "Not for waving about until something happens."
{n}The dragged sacks have left two shallow furrows. Hoofprints cross them. A narrower trail turns under a hazel whose lowest branches have been cut away. At the edge of it, a tuft of coarse gray hair clings to a thorn.{/n}
"I heard something beyond there," Meret says. "It stopped when I stopped. I thought it might be a wolf."
{n}Soana examines the thorn without touching the hair.{/n}
"It might. The ground is willing to tell us more, if we refrain from putting our feet over its mouth."
{n}Farther in, something scrapes once against a root.{/n}''',
        c('[Lore Nature DC 26] [Separate the animal trail from the people who laid the traps.]', check=dict(Skill="SkillLoreNature", DC=26, Success="read", Failure="mistake", CommanderOnly=True)),
        c('[Have Meret watch the movement while you and Soana inspect the ground one strip at a time.]', "slow"),
        c('"We should return when we can give the ground our attention."', abort=True)),
    n("read", "Narrator", '''{n}The gray hair is caught below the level of the hoofprints' owner. The narrow trail belongs to a dog, not a wolf: a dragged tether has brushed the wet earth beside it, leaving a repeated line between the paw marks. Beyond the cut hazel the prints bunch together and stop.{/n}
{n}You point out the tether before anyone moves. Meret goes around the hazel on bare stone. From there she can see the animal lying with one hind foot held by a low wire loop.{/n}
"Alive," she says. "And making an effort to convince me it has plenty of teeth."
{n}Soana crouches where the dog can see her without dragging itself around. She speaks to it in a low, unadorned voice. It growls. She tells it that its opinion has been received.{/n}
{n}You follow the wire to the peg and show Meret where to release its tension. Soana lifts the loop with the padded stick. The dog snaps at the cloth, frees its leg, and crawls under the hazel before trying to stand.{/n}
"Keep back," she says. "It has just learned how much strangers improve an afternoon. Give it time to reconsider."
{n}With the animal clear, you can see the little knots of wire continuing in a line toward the camp. Several have been set in the paths used by smaller animals. One already holds a dead hare.{/n}''', c('[Mark the other loops before following the tether toward its owner.]', "found_end")),
    n("found_end", "Soana", '''{n}The tether leads to a woman carrying two empty sacks. When the dog limps out to meet her she drops both sacks and kneels beside it.{/n}
"Tarn! You were tied."
{n}She sees the bitten end of the tether, then the wrapped wire in Meret's hand.{/n}
"That was mine," she says. "The snare. I did not mean it for him."
"I had suspected you were not running short of dogs," Soana replies. "Whom did you mean it for?"
"Hares. There are people to feed."
{n}The woman gives her name as Hessa. She keeps a hand on the dog's back while he tries the injured foot. Soana waits until he can stand before asking Hessa to show her every trap, including the empty ones.{/n}
"Now?"
"We have daylight, and you have seen what happens when only the person who set them knows where they are."
{n}Hessa leads the inspection. The dog stays beside her. You find the whole short line before the light fades, gather the hare, and dismantle the wire. She takes the food but does not attempt to reset anything.{/n}
{n}At the last peg, Soana asks her to come to the cave when she has settled the dog at camp. Hessa agrees to bring someone who can speak for their stores.{/n}''', c('[Return knowing who set the snares and where they ran.]', flags=("soana.late_track_read", "soana.late_trail_known"))),
    n("mistake", "Narrator", '''{n}You take the narrow track for the approach of an animal still moving through the scrub. The nearest dry patch appears safe. When you step onto it, wire tightens against a branch and a hoarse yelp answers from beneath the hazel.{/n}
{n}You stop. Soana pulls your sleeve back, hard enough to make you take the same step in reverse.{/n}
"There is another line. Look at it before you look for somewhere to stand."
{n}The sound comes again. Now you can see a dog caught by a hind foot. It has dragged a loose tether into a second snare while struggling against the first. Your step disturbed that line and frightened it into pulling harder.{/n}
{n}Meret reaches the dry stone beyond the hazel and calls to the dog. It keeps struggling. A woman answers from farther down the slope and comes running, stopping only when Soana orders her to look at the ground.{/n}
"Tarn. Stay, you foolish thing. Stay."
{n}The dog recognizes her voice. She reaches him from the stony side, gets a hand beneath his chest, and holds him while Soana lifts the wire. He tries to stand afterwards but will not put weight on the trapped foot.{/n}
{n}You acknowledge your mistake. The woman nods once and begins examining the foot instead of reassuring you. Soana puts the loosened wire around the stick.{/n}
"We inspect the rest slowly," she says. "Being wrong has not made the ground less crowded."''', c('[Help carry the dog clear, then inspect with Hessa rather than guessing again.]', "late_end")),
    n("slow", "Soana", '''{n}Meret finds a place above the hazel and stays there. She calls out when she can see the movement clearly: a dog, low to the ground, trying to reach a tether caught against a root.{/n}
"There is wire at the foot," she adds. "I cannot see where it goes."
{n}You and Soana begin at the last patch of undisturbed earth. She points out each place worth examining; you follow the line with your eyes before easing aside a leaf or fallen twig. It is slow work. The dog complains whenever a branch moves.{/n}
"I agree," Soana tells it. "Complaining is appropriate. Moving about is not helping."
{n}The first loop is empty. The second holds the tether, which leads to a third around the dog's hind foot. You call the pattern to Meret. She repeats it before moving down from her stone.{/n}
{n}A woman from the camp hears the voices and arrives while you are loosening the first peg. She identifies herself as Hessa and admits the snares are hers before anyone asks. At Soana's direction she reaches the dog from the stony side and holds it still while the wire comes away.{/n}
{n}He is shaken and tender-footed, but can walk to the edge of the scrub. You have used the clear part of the afternoon finding a safe approach. There is not enough light to check the entire trap line.{/n}
"No one goes through it tonight," Soana says. "Not even someone who is certain she remembers every peg. Especially not her."''', c('[Mark the closed approach and arrange to finish the inspection in daylight.]', "slow_end")),
    n("late_end", "Soana", '''{n}Hessa carries Tarn to a dry place near the camp and settles him on an old cloak. She says she will keep him off the foot until she can see whether it improves. There is no quick cure offered by anyone present.{/n}
{n}The three of you then follow her as she points out the traps she can remember. You remove those and mark the approach to the remaining section. When the light begins to fail, Soana insists on stopping.{/n}
"You will forget something because you are frightened for him," she tells Hessa. "I would prefer to find it with morning light instead of my ankle."
{n}You return at dawn. Hessa meets you without the dog, which she has left with someone at camp. The inspection finds two more loops hidden under fallen leaves. All the snares come up. Hessa takes the hare from the one that caught it, then wraps the empty wire around a piece of wood.{/n}
"I will bring our stores keeper to hear what you want," she tells Soana.
"You are capable of hearing it yourself. Bring the person who can answer for what you have already taken."
{n}Hessa agrees. Meret has delayed her departure to finish the search. She will leave after the meeting, even if the conversation remains unpleasant.{/n}''', c('[Return after the full inspection, with its cost remembered.]', flags=("soana.late_track_missed", "soana.late_trail_known"))),
    n("slow_end", "Soana", '''{n}Hessa takes Tarn back to camp and leaves the closed approach marked. In the morning she meets you with the empty sacks, walks the trap line from its beginning, and shows you each loop before anyone crosses it.{/n}
{n}The dog follows a little way before she sends him back. His foot is sore, and for once he accepts an instruction without testing its length.{/n}
{n}You dismantle the whole line. One snare holds a hare; Hessa takes it after checking with Soana that she does not mean to have food wasted as part of the argument.{/n}
"Eat it," Soana says. "Then come to the cave with whoever can speak for your stores. I want to know what else you intended to carry away."
{n}Hessa ties the bundle of wire and agrees. Meret has stayed to see the search through, postponing her departure until after the meeting. She reminds Soana that this is a delay she chose, not an extension of her grandmother's promise.{/n}
"I heard you the first time," Soana says.
"Then the second should require very little effort."
{n}Soana looks at the bundle of snares and does not quite succeed in hiding a smile.{/n}''', c('[Return after the careful search has established the whole line.]', flags=("soana.late_track_slow", "soana.late_trail_known"))),
], "soana.late_returned")

s("what_the_hollow_costs", "What the hollow costs", '"Hessa said she would bring someone to answer for the stores."', [
    n("start", "Soana", '''{n}Hessa has brought a narrow sack and a woman with a bandaged palm. They wait beyond the cave mouth rather than setting their belongings in it. Meret stands beside the path with her pack already fastened.{/n}
"Mava," the newcomer says. "I count what we have left to eat. I also count what people insist they cannot part with before admitting it is food."
{n}Hessa opens the sack. Inside are hazelnuts, loose husks, and a small bundle of thin branches cut for smoking meat.{/n}
"We can return the nuts," Mava says. "The hare has been eaten. I will not offer to return that."
"How many sacks?" Soana asks.
"Two. This is what remains of the second."
{n}Soana reaches toward the nuts, then stops short of taking any.{/n}
"And the branches?"
"From where the hazel crowded the trail."
"It was not crowding its own ground."
{n}Mava looks at the cut ends. She does not try that explanation again.{/n}''',
        c('[Let Soana ask about the intended harvest before offering a judgment.]', "stores"),
        c('"I need time to hear everyone. Let us arrange another meeting."', abort=True)),
    n("stores", "Soana", '''"Three days," Mava says. "Enough gathering to buy meal for the journey. The small nuts we keep. The good ones sell. Hessa can smoke what she catches, if she is allowed to catch anything."
"Not in that hollow," Soana says.
"We did not find a notice saying who owned it."
"You found a forest in a country being devoured. I should have thought the demand for caution might occur to you without a notice."
{n}Hessa closes the sack. Mava watches her hands for a moment before answering.{/n}
"We are not passing through for amusement. Our first store was taken on the road. The next village will sell, but not on our promise of what we might earn. I can leave these nuts and go there with less. I will do it if that is your answer. I want you to know what you are telling us to carry."
{n}Soana looks toward Meret. Meret shakes her head before a request can form.{/n}
"I cannot feed both camps. I can show them the road when we leave. That is what I can give."
"I had not asked."
"I know the expression."
{n}Soana's nostrils flare, then she lets the interrupted request fall.{/n}
"The hollow holds food for creatures that cannot buy elsewhere," she tells Mava. "Strip it because you are frightened, and the next hungry people will find an empty place. They will ask why I did nothing while there was still something to keep."''', c('"What can the ground bear? Show us that much before we decide."', "ground")),
    n("ground", "Soana", '''{n}You walk to the hazel edge together. Meret waits where she can see both the camp's approach and the path home. Mava opens the sack again, comparing the gathered nuts with what remains overhead.{/n}
{n}Soana shows her branches already stripped clean and the small heaps of husks below them. Farther south there is a heavier crop on rougher ground. Reaching it with full sacks would take longer. It would also put the gatherers beyond the deer hollow.{/n}
"Three daylight visits there," she says. "No snares. No branches cut. You carry your empty sacks in where I can see them and your full sacks out the same way. I will have to spend those days watching people pick through what I would rather leave."
"Would it be enough?" you ask Mava.
"For less meal. Enough to make the bargaining possible."
"And the other answer?" you ask Soana.
"They leave the sack and go with Meret. I keep this edge closed while the animals need it. I will spend time watching that boundary instead. Keeping people out is not an occupation performed by pronouncing a sentence."
{n}She studies the low branches, then looks at you.{/n}
"I can make an approach unpleasant enough that a person thinks before returning. I cannot make a whole forest invulnerable, and I cannot be here in every weather. You have heard enough of my plans to understand the size of those omissions."
"Tell them what unpleasant means."
"I was going to. They will see where the line is before they meet it."''', c('[Hear the working and its limits.]', "thorn")),
    n("thorn", "Soana", '''"A turning thorn. Three cuts in dead wood, ash from the same branch, and a name for the piece of ground I mean to keep. Whoever steps over the marked approach hears footsteps coming after them. The nearer they press, the nearer the steps. Turn back, and it stops."
"Whose feet?" Hessa asks.
"Nobody's. A remembered sound given a little reach. There is no creature tied inside it. It cannot bite, and it cannot stop someone determined to pass. It can make a frightened person run badly. That is why you are hearing about it before I set it."
{n}Hessa folds her arms.{/n}
"You intend to frighten us."
"I intend to discourage people from emptying this place while I am elsewhere. You are not exempt from the difficulty merely because you have explained it well."
{n}Soana draws a short line in the dirt with her stick.{/n}
"It will keep only the approach I mark. Beyond it the forest remains a forest. Rain spoils the ash. I renew it or leave it. A person who knows the sign can break it with a wet cloth. There is no life knotted to its life."
{n}She says the last words without looking away from you.{/n}
"You may compare it with the other thing I did. You may not call them the same because both offend you."
"And if we permit the three days?"
"The line goes beyond the southern gathering ground. They can collect what we agreed without crossing it. More of the edge is left open. I shall dislike every sack that leaves, and count them all."''',
        c('"Close the hollow. They have a road out, and taking its last food will leave others hungry."', "reserve"),
        c('"Allow the three days on the southern ground. Keep the inner approach marked and leave them a harvest they can sell."', "harvest")),
    n("reserve", "Soana", '''"Then that is my answer," Soana says. "Leave the sack. Take the road Meret showed you. I will not accuse you of stealing the hare back out of your own stomachs."
{n}Mava looks down at the nuts. Hessa asks whether they may have enough for the morning's walk. Soana measures a portion into Hessa's empty hands before taking the rest.{/n}
"You have names now," Mava says. "If we arrive hungry, you may use them while explaining why the animals needed the food."
"I will remember them," Soana answers. "I would remember an empty hollow too."
{n}There is no gratitude between them. Mava ties the mouth of the nearly empty sack and asks Meret how far they can travel before dark. Meret tells her. They begin discussing which loads must be made lighter. Hessa agrees to stay long enough to see the marked boundary before they leave. Meret gives her the directions once more, then goes to join her own camp.{/n}
{n}Soana waits until they move away before speaking to you.{/n}
"I wanted that answer. It would be a relief to pretend I only endured it because you advised me. I shall spare you the privilege."
"You heard what it costs them."
"Yes. Stay long enough to see what keeping my side costs me. The thorn must be tested. A warning I have not listened to myself is merely a threat I find convenient."''', c('[Agree to test the closed approach with her.]', flags=("soana.late_reserve", "soana.late_boundary_agreed"))),
    n("harvest", "Soana", '''{n}Soana looks at the southern hazel for a long time. Then she names the three visits, ending each at midday so she can inspect the ground while there is still light. Mava repeats them. Hessa repeats the part about snares without waiting to be asked.{/n}
"The sack we brought?" Mava asks.
"Counts toward what leaves. You are not beginning with empty hands merely because you brought one back."
{n}Mava weighs that, then nods. She will stay with Hessa for the gathering and take a later road than Meret's camp. Waiting costs them company on the journey. She chooses it anyway.{/n}
{n}Meret describes the safer fork twice, makes Hessa point it out from the bend, and shoulders her own pack again.{/n}
"I can leave without someone deciding that means I have ceased to care," she says.
"Go," Soana tells her. "Before I find a reason to detain you that we both recognize."
{n}Meret gives the wrapped wire to Hessa. The traps leave with their owner, dismantled. The deer hollow remains beyond the allowed ground.{/n}
{n}Soana watches the hunters part.{/n}
"I would have preferred the quiet edge. I can choose to give some of it and still know what I preferred. We shall test the inner line before I let anyone gather near it. I will not have a running person trample the roots because I was careless about where a sound could reach."''', c('[Agree to test the boundary before the gathering begins.]', flags=("soana.late_harvest", "soana.late_boundary_agreed"))),
], "soana.late_trail_known")

s("where_the_steps_end", "Where the steps end", '"I am ready to hear the thorn before anyone has to trust it."', [
    n("start", "Soana", '''{n}Soana has laid three pieces of dead thorn beside a shallow dish of ash. She has cut a different notch in each. There is no bowl from the old shrine among her tools.{/n}
"That one stays buried," she says when she sees where your eyes go. "I can dislike beginning again without reusing everything that once hurt me."
{n}She puts a wet cloth in your hand.{/n}
"Across all three cuts. That ends this working. If the sound follows someone beyond the place I showed you, use it. Do not wait for a more elegant failure."
"And if it remains inside?"
"We see whether it gives enough warning to be worth the trouble. I am not asking for an act of faith."
{n}She leaves the cloth with you while picking up the marked wood. Her fingers move confidently over the cuts, finding each by touch.{/n}''',
        c('[Ask where she wants you to stand, remembering the interrupted voice-working.]', "changed_role", requires=("soana.voice_interrupted",)),
        c('[Ask which part of the test she wants you to undertake.]', "role", forbids=("soana.voice_interrupted",)),
        c('"I cannot give the test its attention now. Leave the marks unlit until I can."', abort=True)),
    n("changed_role", "Soana", '''"At the approach. You cross after I have spoken, then return by the same way. The cloth is for a sound that will not stay where I put it."
"You said you would ask someone else to close the next bowl."
"I remember what I said. This is not a bowl, and I am not putting my voice within reach of something that can take it. If you dislike the sound, you step back. You need not decide how much pain I ought to endure."
{n}She turns the middle thorn in her hand.{/n}
"I have chosen a task whose limit either of us can enforce. That is not the same as forgetting what happened in the nursery."
"No."
"Nor is remembering it a promise never to put anything useful in your hands again. I have a forest to tend. I cannot afford such an elaborate grudge."
{n}Her glance takes some of the sting from the words. She waits until you have understood the new task, then leads you toward the marked ground.{/n}''', c('[Take the role she has actually offered.]', "placing")),
    n("role", "Soana", '''"Walk the approach when I tell you. Listen. Turn back before you are tempted to invent an enemy for the sound. I shall watch from beside the marker."
"Have you used this before?"
"A smaller sign, around a store people would not leave alone. It frightened a person I disliked and a person I wanted to welcome. I learned to show people where it began."
{n}She picks up the last thorn.{/n}
"I have not used it here. The slope may carry the sound where I do not want it. That is why I asked for someone who could tell me what happened instead of telling me how wise I must have been."
"An exacting qualification."
"You have managed it. Sometimes with enthusiasm I found excessive."
{n}She touches your elbow as she passes. The cloth remains in your hand. You follow her toward the ground she means to mark.{/n}''', c('[Walk with her to the chosen boundary.]', "placing")),
    n("placing", "Narrator", '''{n}The first thorn goes into a crack in dead wood beside the path. Soana sets the second where bare earth meets the roots, the third where a person returning would be able to see it. She lays ash in the cuts and speaks to the ground in a low voice.{/n}
{n}No answering voice comes. A leaf turns on its stem and stops. Soana steps clear of the approach.{/n}
"Now. Slowly."
{n}You cross the first mark. A footstep sounds behind you, heavy enough to press grit into the earth. You know that nobody followed. Knowing does not prevent your shoulders tightening.{/n}
{n}Another step answers your next. When you stop, it stops a fraction later. The little difference makes it harder to dismiss.{/n}
"Come back," Soana says.
{n}You turn. At the first thorn the sound ends. Then a loose pebble falls from the bank, making you look behind once more. Soana sees the movement and does not laugh.{/n}
"That part was a pebble. Sit if you need to. I know what the rest can do to the breath."''',
        c('"Keep the sound this strong. The end is clear, and a warning must make someone stop."', "strong"),
        c('"Make it softer. Someone running from that could be hurt before they understand the way out."', "soft")),
    n("strong", "Soana", '''"Then we test the end again," she says. "Knowing where it is helped you. Hessa will not be allowed to mistake that for everybody's experience."
{n}She approaches the first thorn herself. You take her place beside the marker. The steps sound as she crosses, and her grip tightens on the stick before she can conceal it. She walks back deliberately, stopping just outside the sign.{/n}
"There. I dislike hearing myself followed. I still want a stranger to know that this is not unclaimed ground."
{n}You walk the outer edge together. From one place below the bank the sound can be heard as a distant scrape, though neither of you has crossed. Soana moves the second thorn closer to the first and repeats the working. On the next circuit, the sound remains within the marked approach.{/n}
"Less ground," she says. "A price I can see."
{n}She asks you to stay while she shows Hessa and Mava the marker. They approach only as far as they choose. Mava hears enough to stop, then studies the route back instead of pretending she was not frightened.{/n}
"Put the warning where someone arriving late can see it," she says.
{n}Soana agrees to leave pale stones on either side of the first thorn. The sound keeps its strength. The approach now advertises where it begins.{/n}''', c('[Stay until the visible warning and the tested boundary agree.]', "strong_end")),
    n("soft", "Soana", '''{n}Soana studies you, then the uneven ground beyond the first thorn.{/n}
"A useful objection. I had been imagining a trespasser with the courtesy to fall somewhere less inconvenient."
{n}She rubs some ash from the middle cut and renews the words. On the next crossing, the sound is a tread on dry leaves rather than a heavy foot on earth. It is still near enough to make you look around. It no longer seems about to reach you.{/n}
"Some will ignore it," she says.
"They could ignore the stronger one."
"More will ignore this. You need not make the cost disappear in order to prefer it."
{n}You walk the outer edge together. At one point beneath the bank you hear a faint scrape without entering the marked ground. Soana moves the second thorn inward, surrendering a little reach. The next test holds the sound inside.{/n}
{n}When Hessa and Mava come to see the boundary, Soana lets them choose how far to approach. Hessa crosses one step, hears the tread, and withdraws without being hurried.{/n}
"I would have thought something was in the bushes," she says.
"That is the intention. These stones show where the thought begins. Tell anyone you bring with you."
{n}Mava says she would prefer a simple request. Soana answers that she has made one and is making this as well. They leave the disagreement where the pale stones stand.{/n}''', c('[Stay until the gentler warning has been tested from both sides.]', "soft_end")),
    n("strong_end", "Soana", '''{n}Back outside the cave, Soana takes the unused wet cloth from you and lays it over the rim of a pot. She looks tired, but there is satisfaction in the way she sets the marked stick within reach.{/n}
"I shall inspect it after rain. Until then, that approach can speak without waiting for me to hear it first."
"And the rest of the forest?"
"Remains larger than my intentions."
{n}She holds up one finger before you answer.{/n}
"Let me enjoy one small success before we list everything it has not done. Hessa has seen the line. Mava knows the terms. I have kept the strength I wanted and made the beginning visible. Those are things that happened."
{n}She sits, leaves a place beside her, and asks you to tell her exactly what the first step sounded like.{/n}''', c('[Keep the tested, stronger warning and return to hear how the terms were kept.]', flags=("soana.late_thorn_strong", "soana.late_thorn_tested"))),
    n("soft_end", "Soana", '''{n}At the cave Soana takes the unused cloth and drapes it over the rim of a pot. She puts the marked stick within reach, then sits before finding another task.{/n}
"I will go out to look more often," she says. "A softer warning buys us something and asks something in return. I shall remember that when I find myself resenting the walk."
"Will you regret it?"
"I expect I shall regret many things briefly. I would prefer not to be required to change them all before supper."
{n}She gestures to the place beside her.{/n}
"Tell me about the second crossing. Where did you begin to believe you could stop?"
{n}You describe the sound on the leaves, and the moment when your breath ceased trying to outrun your feet. She listens without improving the account.{/n}''', c('[Keep the gentler warning and return to hear how the terms were kept.]', flags=("soana.late_thorn_soft", "soana.late_thorn_tested"))),
], "soana.late_boundary_agreed", delay=0)

s("the_days_she_counted", "The days she counted", '"What became of the terms we left with Hessa and Mava?"', [
    n("start", "Soana", '''{n}Soana is sitting outside the cave with the marked thorn across her knees. One of the cuts has been washed clean. She turns it so you can see the pale wood.{/n}
"Rain. Entirely unimpressed by my intentions. I checked the approach afterwards. It was silent, as it should have been."
"Will you renew it?"
"When I need that ground kept. I will not keep a warning alive merely because I went to the trouble of inventing one."
{n}She sets it beside the walking stick and makes room for you.{/n}
"There is an account you should hear first. The people did not disappear because we finished deciding what to tell them."''',
        c('[Ask about the families who left without the harvest.]', "reserve", requires=("soana.late_reserve",)),
        c('[Ask about the three days of gathering.]', "harvest", requires=("soana.late_harvest",)),
        c('"I want to hear it when I can stay."', abort=True)),
    n("reserve", "Soana", '''"They left the remaining nuts. Hessa took the wire, wound tight enough that nothing could put a foot through it. Mava asked for the name of the village that would sell meal. I gave her the road as well."
{n}Soana looks toward the upper bend.{/n}
"Tarn could walk a little way before Hessa carried him. She had made a sling from one of the empty sacks. I watched them go until I could no longer see whether she was resting or arguing with him."
"Did they say anything else?"
"Mava said I would find the hollow very quiet. She was right."
{n}For a moment Soana lets that answer stand without protecting it.{/n}
"I put the nuts back in small heaps under the hazel, away from the path. Some were gone by the next morning. I cannot tell you which mouth took every one. I can tell you the food remained where I meant it to."
"Was it worth sending them away with less?"
"I think so. I dislike knowing their names because it prevents me from making the answer comfortable. I am keeping the answer anyway."
{n}She turns toward you.{/n}
"If you come here only when I can tell a pleasing story about myself, we shall have very irregular visits. I would rather you knew what I was willing to defend."''', c('[Hear the rest without requiring her to make the choice painless.]', "meret")),
    n("harvest", "Soana", '''"Three mornings. I inspected six sacks, heard seven complaints about the climb, and found one cut branch that was old enough for Hessa to enjoy proving I had accused her too quickly."
"Did you acknowledge it?"
"With admirable brevity."
{n}Her mouth moves at one corner.{/n}
"They kept to the southern ground. On the last morning Mava wanted another hour. I refused. The nuts were still overhead, and she could see them. That made ending the agreement less pleasant than beginning it."
"Did she stop?"
"Yes. She asked whether I understood how much meal the last sack would buy. I asked whether she understood how often a last sack can be followed by one more. We both understood. She tied the sacks."
{n}Soana brushes a flake of ash from her sleeve.{/n}
"I found fewer tracks along that edge the next day. The gatherers disturbed it. I do not know which animals will return, and I have resisted pretending that I counted them all before we began. The inner hollow was not cut. The camp is empty."
"And the warning?"
"They left it alone. Hessa took the dismantled wire away. Tarn walked beside her for part of the road and rode in a sack for the rest. I hope he learned to dislike the smell of his owner's handiwork."
{n}She looks at the thorn by her stick.{/n}
"I gave three mornings and part of a harvest. I did not give the right to take the next one. That distinction survived having people stand in front of me wanting more."''', c('[Ask about Meret after the camp departed.]', "meret")),
    n("meret", "Soana", '''"She went with her own people. Before Hessa finished preparing to leave. I began suggesting another thing she might inspect on the way, and she asked whether I was giving directions or finding a reason to keep her."
"Which was it?"
"Both. I provided the directions. She left."
{n}Soana folds her hands around one knee.{/n}
"Her grandmother's mark is still hers. The report she gave me is mine to use. I dislike how much smaller that makes my claim, until I remember how much easier it was to believe the report when she could have chosen not to bring it."
"Will you ask her again?"
"If she comes this way. I will also look for other eyes. I have spent too much time treating one useful person as though finding her meant I would never need another."
{n}She looks directly at you, without exempting herself from the difficulty of what she has said.{/n}
"That includes you. I would be glad of your help again. I will not keep inventing an unfinished task each time you begin to stand."
"You might simply ask me to sit."
"I was preparing to. Your habit of anticipating the sensible part remains tiresome."
{n}She moves a little nearer, leaving you room to decide whether to close the rest of the distance.{/n}''', c('[Ask what she wants kept when you have to leave again.]', "guardian")),
    n("guardian", "Soana", '''"The account," she says. "What the warning did, where it stopped, and what I asked of the people who passed. Put no grand title on it. I have enough trouble with people mistaking an old woman for every answer the forest ought to have."
{n}She rests a hand against the hollow at the base of her throat, then lowers it.{/n}
"And write the thing it did not do. The clay medallion and the brand on Orso belonged to another working. I do not want a tale about three thorns to grow until someone thinks we undid that life knot with a wet cloth."''',
        c('"The thorn did not release Orso. The binding and its cost remain."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
        c('"The thorn did not bring Orso back, or supply a replacement guardian."', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"Yes. You still object. I still fear what would come through if I broke what holds him. I do not have an answer that makes those two things cease to matter."
{n}Her jaw tightens, but she stays beside you.{/n}
"I have made a protection here that I can end without killing what carries it. I intend to use that knowledge. I will not tell you it has already become strong enough to take his place."
"I will not tell you affection has settled my objection."
"Then I know who is sitting beside me. I would rather endure that than discover later that you had spent every pleasant evening preparing to forgive something you never meant to question again."
{n}She takes a folded piece of bark from beside the water pot. You recognize the smear where an old beginning was rubbed away.{/n}
"I have finished another account. This one is not for the forest."''', c('[Let her show you what became of the letter to Corven.]', "letter")),
    n("dead", "Soana", '''"No. He remains absent. I have not found another creature whose life I can persuade myself is a convenient answer."
{n}She looks at the path for a moment, listening out of habit.{/n}
"That sentence is not a promise that I have become incapable of doing harm. It is what happened. I have made one smaller protection and learned its limits before relying on it. I mean to keep doing that work."
"Without pretending the forest is safe?"
"Without pretending you need another task from me before you are permitted to leave. Those are different matters, and I have been making excellent use of confusing them."
{n}She gives you a wry look, then takes a folded piece of bark from beside the water pot. The dark smear from her earlier attempt remains on its outer face.{/n}
"I finished this. An argument I could end even without receiving an answer."''', c('[Hear what she chose to write to Corven.]', "letter")),
    n("letter", "Soana", '''"I told him about the spring as it is," she says. "About work I was proud of, and work I would rather have described differently. I wrote your name. I crossed out the sentence that began by explaining what a difficult woman he had married. He knew."
{n}She turns the bark over without offering it to you.{/n}
"I have no address for it. No newly discovered grave. No witness with a tale that changes what I told you before. I will keep it here. If there is ever a person to receive it, he will receive my words, not a stranger's kind explanation of what I must have meant."
"May I ask what you wrote about me?"
"That you came back. That I wanted you to. That I have had a life while I did not know where he was, and I will not call every part of it an apology."
{n}She puts the bark away. The act is plain and complete, with no ceremony to make a message travel where she cannot send it.{/n}
"There. I have said what I had to say to him, as far as I can. Now I would like to finish deciding what I am asking of you."''',
        c('"I want to talk about the life we could keep making together."', "future", requires=("soana.later_courting",)),
        c('"I am here as your friend. Tell me what you want our friendship to keep."', "friend", requires=("soana.later_friends",))),
    n("future", "Soana", '''"I want a place in your plans that is not reserved for the occasions when you need a witch. I want to know when you hope to come, to be allowed to miss you when you cannot, and to hear the reason from you when you can give it."
{n}She looks at the cave, then back at you.{/n}
"I will not leave this place merely because other people would find our arrangement easier to name. Nor will I ask you to put every other love, duty, and desire on the wrong side of its entrance. I want us to arrange time we actually mean to share."
"What would you offer?"
"Time I have stopped promising to the forest before I look to see whether it needs me. A place for your things if you want one. My company, including the days when I have no intention of being instructive."
{n}Her smile grows a little bolder.{/n}
"I can think of several uses for those days. I would enjoy discovering whether you can."
{n}Then she lets the smile settle.{/n}
"I have not become unmarried by writing on bark. I cannot promise what Corven would say. I can promise that I will not hide you behind a more convenient word when speaking of my own choices. What are you willing to promise me?"''',
        c('"A shared life, with time we choose and room for the people we both love. I want to be your partner."', "commit"),
        c('"I want this courtship and the next visit. I am not ready to promise a shared life."', "open"),
        c('"I want to keep you in my life as a friend. I cannot promise the romance we have been trying."', "part_as_friends")),
    n("commit", "Soana", '''{n}She takes your hand and brings it to her cheek. For a moment her eyes close. When she opens them again, she looks pleased enough to be irritated by how much you can see.{/n}
"Yes. That is what I wanted to hear."
"You could leave it there."
"I am considering the possibility."
{n}She kisses your palm, a quick, deliberate touch, then keeps your hand against her face.{/n}
"Beloved will do, when I want a word. Your name will do when I want you to look at me. I do not require a second wedding to know what I have agreed to."
{n}You settle the small practical beginning: a place kept clear beside the blanket, and a longer visit when the fighting allows it. If either of you must change it, the other will hear the change before a stranger is sent to explain it.{/n}
"Come before you go to the final fighting," she says. "Not because there will be one last service to perform. I have spent enough of our time finding those. I want an evening I can remember without inventorying what we repaired."''', c('[Keep the partnership and the farewell she has asked for.]', flags=("soana.committed", "soana.late_future_chosen"))),
    n("open", "Soana", '''{n}She draws a slow breath. Her hand remains beside yours instead of retreating into her sleeve.{/n}
"Less than I hoped. More than an answer made large because you expect me to be hurt."
"I do want to return."
"Then return when you can mean it. I will decide what I want when you ask, with everything we have already done remembered. We need not promise to feel the same forever in order to be honest about wanting one another now."
{n}She brushes one finger along your knuckles.{/n}
"I would still like the evening before you leave for the final fighting. I am not keeping it as a trap in which to obtain a better promise. I would like to be wanted for it without first winning an argument."
"You are."
"Good. I have been remarkably patient while arriving at that simple piece of information."''', c('[Keep the courtship and an evening freely wanted.]', flags=("soana.late_open", "soana.late_future_chosen"))),
    n("part_as_friends", "Soana", '''{n}Her fingers close against her own palm. She looks past you, letting the first response pass before choosing words.{/n}
"Then we are stopping a romance. I will not have our earlier evenings renamed as though we were both merely being polite."
"Neither will I."
"I want the friendship. I will need room to find its comfortable places again. Do not become excessively helpful while I am doing it. I shall resent being treated as a project immediately after being kissed."
{n}She looks at you again. The attempt at sharpness has steadied her.{/n}
"Come before the fighting, if you want to. We can sit. I may not wish to hear how relieved you are that we managed the conversation well."
"I will remember."
"See that you do. It would improve the evening considerably."''', c('[Accept friendship without erasing the courtship.]', flags=("soana.late_friends", "soana.late_romance_ended", "soana.late_future_chosen"))),
    n("friend", "Soana", '''"The visits in which nobody is in danger. They seem to be the first ones everyone postpones."
{n}She takes a scrap of the old proposal from beneath a weight and turns it over. There are corrections on both sides now, none leaving enough room for another beginning.{/n}
"You have spent quite enough time hearing why your methods were inadequate. Come before the final fighting with something foolish you want to tell me. I shall attempt to hear it without making a lesson of it."
"An ambitious undertaking."
"I have not promised success. I have promised an attempt."
{n}She gives you the worn page to read once more, then takes it back before you can mistake the gesture for surrendering her copy.{/n}
"I will keep this. I like remembering that you brought something and remained willing to discover where it failed. I also like remembering the goat in the song. Both are legitimate occupations for a mind that has endured enough solemnity."
{n}You agree on another evening. She keeps the place beside her clear while you finish the one you are in.{/n}''', c('[Keep the friendship and the promised evening.]', flags=("soana.late_friends", "soana.late_future_chosen"))),
], "soana.late_thorn_tested", delay=72)

s("before_the_far_road", "Before the far road", '"I came for the evening, before I have to leave."', [
    n("start", "Soana", '''{n}There is no experiment laid out at the cave mouth. The water pot stands in its cradle, the tools are put away, and a clean cloth covers the place where you usually sit. Soana has left her walking stick within reach rather than leaning it across the entrance.{/n}
"I considered taking you to the bend," she says. "Then I considered how much of an evening we might spend discussing whether the stone was damp. I have chosen dry shelter. You may admire my courage."
{n}She closes the clasp of her shawl, discovers that she has fastened it crookedly, and corrects it with an impatient little breath.{/n}
"You have time?"
"For this."
"Then come in. If you have a speech prepared, allow it to suffer in silence while you sit down."''',
        c('[Sit beside the woman with whom you chose a shared life.]', "beloved", requires=("soana.committed",)),
        c('[Join her for the courtship you are both still choosing.]', "courtship", requires=("soana.late_open",)),
        c('[Keep the evening as her friend.]', "friend", requires=("soana.late_friends",)),
        c('"I cannot give you the evening yet. Let me return when I can keep it."', abort=True)),
    n("beloved", "Soana", '''{n}She leans against you as soon as you are settled. No accidental errand brings her nearer. Her hand finds yours beneath the edge of the shawl.{/n}
"I have been trying to decide what a person ought to say before someone she loves goes to fight a terrible thing. All the excellent answers appear to have been worn smooth by other people's use."
"You could tell me something you want."
"I want you to come back. I want the long visit we discussed. I want to be cross because you have put your belongings in the wrong place, and to discover that I moved them there myself."
{n}She lifts her head to look at you.{/n}
"I know wanting does not arrange it. You need not protect me from the knowledge. It is what I want."
"It is what I want too."
{n}She presses your hand once, satisfied with an answer that does not attempt more than it can carry.{/n}
"Then let us have an evening worth bringing back to. I have done enough rehearsing how gracefully to lose one."''', c('[Turn toward her.]', "desire")),
    n("courtship", "Soana", '''"You remembered which invitation I gave you."
"Did you expect me not to?"
"I expected to spend part of the evening being offered a larger promise because it seemed unkind to leave without one. I had several replies ready."
"You can save them."
"An unusual gift. I shall enjoy the room they leave."
{n}She moves close enough for your shoulders to meet and asks for your hand. When you offer it, she traces the line of your thumb with hers.{/n}
"I still want you. I still wish we could know more about what follows. I am going to enjoy this evening without making either admission apologize for the other."
"May I do the same?"
"I should prefer it. I did not invite a witness to my self-control."
{n}She looks at your mouth, then meets your eyes, smiling with an impatience she no longer needs to hide.{/n}''', c('[Let the evening belong to what you both want now.]', "desire")),
    n("desire", "Soana", '''{n}Soana lifts a hand to your cheek. The pad of her thumb is rough from work; the touch is careful until you lean into it. Then she stops being tentative.{/n}
"There you are," she says softly.
{n}She moves close enough that you can feel her breath, then waits. One loose strand of hair catches against her lip. You move it clear. Her hand closes gently around yours before you can lower it.{/n}
"I would like to kiss you. I would like to keep you here until the daylight makes us admit there is work beyond the entrance. I had a cleverer way of asking."
"You can save it."
"No. This one was good. I shall recover it when you are least prepared."
{n}Her laughter is low and close. The shawl has slipped from one shoulder; she lets it fall into her lap and asks how much of the night you can give her.{/n}''',
        c('"I want to stay with you. Tell me when you want anything slower."', "night"),
        c('"I want the evening and your kisses. I need to leave before the night is over."', "kiss"),
        c('"Hold me for a while. That is what I want most tonight."', "hold")),
    n("night", "Narrator", '''{n}She pulls you close by the hand you have left in hers. You kiss her, and she answers with an eagerness that makes the careful waiting seem far away. The kiss is interrupted only because she laughs when her shawl catches beneath your knee. You free it together. She spreads it over the unused tools rather than returning it to its peg.{/n}
{n}"Let them endure a little inconvenience," she says. "I have been unusually considerate of useful things."{/n}
{n}Then she does not let you be careful. Her hands are rough and sure and impatient with buckles; she pushes the shirt off your shoulders, bites the join of your neck, and pulls you down into the blanket and the smell of smoke and pine, her grey braid coming loose across your chest as she climbs over you.{/n}
{n}Later, a branch brushes the rock outside. Soana lifts her head, listens once, and settles against you again. Her hand returns to the place it had found at your shoulder. She asks whether you remember the first reed she made you pull out of the carrier. You tell her you have had considerable practice remembering her corrections. She laughs against your neck.{/n}
{n}In the morning she is watching the light at the entrance when you wake. She turns immediately when you move.{/n}
{n}"I recovered the clever remark," she says. "It was not as good as I remembered. We may keep what happened instead."{/n}
{n}You kiss her before getting up. She answers without hurrying the moment toward goodbye.{/n}''', c('[Rise together when it is time to leave.]', "leave_night")),
    n("leave_night", "Soana", '''{n}At the entrance she catches your hand once more. Her expression is steady until you turn toward the path, then briefly much less so.{/n}
"Go carefully. I am allowed one ordinary request after all the trouble I took to avoid an ordinary speech."
"You are."
"Then hear it."
{n}You do. She lets go when you are ready, not because she has ceased wanting the hand.{/n}''', c('[Carry the night with you, without calling it a guarantee.]', flags=("soana.lovers", "soana.late_farewell_night", "soana.late_campaign_kept"))),
    n("kiss", "Narrator", '''{n}She accepts the time you name, then leans into the kiss you offer. The pleasure has lost none of its urgency merely because you have agreed when to stop.{/n}
{n}Afterwards she rests against you and begins the song about the goat. You remember enough to anticipate its most undignified turn. She changes the verse and catches you trying to sing the wrong words.{/n}
{n}"An older version," she says solemnly. "The goat has acquired further experience."{/n}
{n}You laugh against her hair. She tells you the new ending, which appears to have been invented for the pleasure of making you laugh exactly there.{/n}
{n}When the time comes, she does not begin another verse. She walks with you to the entrance and asks for one last kiss. It is long enough that you have to adjust the way you stand to keep it comfortable. Neither of you apologizes for the difficulty.{/n}
{n}"Go carefully," she says. "I would like to hear you get the words wrong again."{/n}''', c('[Leave at the time you chose, with the farewell kept.]', flags=("soana.late_farewell_kiss", "soana.late_campaign_kept"))),
    n("hold", "Narrator", '''{n}She opens her arms. You settle against her, adjusting the blanket until the stone no longer presses where you do not want it. She rests one hand at the back of your neck and leaves it still.{/n}
{n}For a while you listen to the small sounds outside: a bird settling, leaves brushing rock, water farther down the slope. Nothing asks to be interpreted. When you begin to speak, the words come less neatly than you intended.{/n}
{n}Soana listens to the unfinished thought. Once she asks a question, then waits while you discover that the first answer was not quite what you meant. She does not turn uncertainty into a reason you ought to have kept silent.{/n}
{n}"Stay here a little longer," she says when you stop. "You have brought enough of tomorrow into the room."{/n}
{n}When you leave, she walks to the entrance with you. She touches her forehead briefly to yours and says your name. For this goodbye, she lets that be enough.{/n}''', c('[Leave with the closeness you chose.]', flags=("soana.late_farewell_held", "soana.late_campaign_kept"))),
    n("friend", "Soana", '''{n}She passes you a small wooden clapper from the warning experiment. Its edges are smooth where it has been handled.{/n}
"Useful wood," she says. "I have spent an unreasonable amount of time deciding what it should become."
"Perhaps it has finished being something."
"Then we are agreed. It may rest. I wanted to show you that I kept it, not appoint you to find its next occupation."
{n}She sets it beside the pot and settles back. You tell the foolish story you brought, about an argument on the road in which both people had been defending the same direction while pointing different ways. Soana asks whether either admitted it. You explain the elaborate compromise by which both managed to remain right.{/n}
"A pity they did not consult the road. It might have had an opinion."
{n}She answers with a story about the festival, a misplaced cloak, and the indignation of a man who found it on the person he had spent the evening trying to impress. The story is not instructive. She looks pleased when you notice.{/n}
{n}At the entrance, later, she rests a hand on your arm.{/n}
"I am glad we had this. Whatever the next road does with you, it has not undone an evening already spent. Come back if you can. Bring yourself before you bring a problem."
{n}She squeezes your arm, then releases it and leaves the path clear.{/n}''', c('[Take leave of the friend who asked for your company.]', flags=("soana.late_farewell_friend", "soana.late_campaign_kept"))),
], "soana.late_future_chosen", delay=24)


def ending(id, title, text, requires=(), forbids=(), any_flags=(), owner="Epilogue"):
    SCENES.append(scene("soana.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Soana")],
        Relationship="soana", last=99, requires=requires, forbids=forbids,
        RequiresAny=list(any_flags)))


ORDINARY = (*LOSS, "soana.closed", "inhuman", "ascended", "sacrifice")
ending("kept_life", "A life with an open path", '''{n}The Commander returned to Soana with time to stay, not merely another question about what the forest could endure. The place beside her blanket acquired belongings she occasionally moved before complaining that they had been misplaced. Some visits were interrupted. Others survived an entire afternoon without improving anything.{/n}
{n}They had chosen a shared life that did not pretend the war was over. It required messages, changed plans and the occasional difficult answer. Soana kept her forest and her temper. She also kept time that she had once given away before anyone asked for it.{/n}
{n}Corven's unanswered place in her history was never tidied into a convenient tale. The bark she had written remained among her belongings. When she called the Commander beloved, she meant the choice she had actually made.{/n}
{n}At the cave, the warning thorn was renewed when needed and allowed to wash quiet when it was not. Visitors learned to look for the pale stones. The Commander learned that a familiar path could still lead to an evening neither had planned, and that Soana's laughter was worth coming home to hear.{/n}''',
    requires=("soana.late_campaign_kept", "soana.committed"), forbids=ORDINARY)
ending("chosen_visits", "The next invitation", '''{n}Soana and the Commander kept the courtship they had chosen without improving its last farewell into a promise of a household. They asked for visits, found time for some, and spoke plainly when an answer disappointed them. The affection in the asking mattered even when the road prevented the answer they wanted.{/n}
{n}She remained capable of wanting more. The Commander remained free to answer. Neither found an honest life made easier by pretending those questions had been settled in advance.{/n}
{n}The forest still occupied much of her attention. Yet there were evenings when she left a useful task unfinished because she wanted to hear a voice at the entrance. She did not ask a spirit to preserve those evenings. She remembered them, and sometimes began planning another before the last had ended.{/n}''',
    requires=("soana.late_campaign_kept", "soana.late_open"), forbids=(*ORDINARY, "soana.committed"))
ending("familiar_company", "Company without a debt", '''{n}The Commander remained welcome at Soana's cave as a friend. She did not disguise the friendship as a romance denied its proper ending, or reduce it to the services each could perform. Sometimes the visit involved a difficult question. Sometimes the most pressing dispute concerned the correct words of a song.{/n}
{n}Meret's old family mark never became an order binding her descendants. Soana remembered the help it had once stood for and asked living people for the help they could choose to give. She was often impatient with the answer. Those who returned generally knew that before setting out.{/n}
{n}The worn proposal stayed beneath its weight. On the back, where there was finally no room for another correction, Soana wrote the date of an evening in which she and the Commander had done nothing especially useful. She found it worth keeping.{/n}''',
    requires=("soana.late_campaign_kept", "soana.late_friends"), forbids=(*ORDINARY, "soana.committed", "soana.late_open"))
ending("sacrifice", "The visit that did not follow", '''{n}Soana heard what the Commander had done to close the Worldwound. For a while she found the praise surrounding the sacrifice impossible to bear. She understood the need the great accounts described. She also remembered the person who had sat beside her and wanted another evening.{/n}
{n}She kept the last visit as it had been: the company actually offered, the promises actually spoken, the pauses nobody had needed to fill. Grief did not entitle her to enlarge them. Nor did the world's relief require her to call the loss small.{/n}
{n}The thorn washed quiet in the next hard rain. She went out afterwards, examined the ground and chose what needed doing that day. It was work she knew how to begin. Returning to the empty place beside the blanket was harder.{/n}''',
    requires=("soana.late_campaign_kept", "sacrifice"), forbids=(*LOSS, "soana.closed", "inhuman", "ascended"))
ending("beyond_the_forest", "An invitation without a summons", '''{n}The Commander's ascent gave Soana no reason to withdraw what she had chosen, and no certainty about how a god might answer it. She addressed the absence with familiar impatience. A new grandeur did not turn an unanswered invitation into an afternoon together.{/n}
{n}She neither knotted the Commander's name into a charm nor offered the forest as payment for a return. Once she had made a terrible binding because she could not bear to lose protection. Whatever power now existed beyond her reach, it would receive a request rather than another tether.{/n}
{n}The last mortal visit remained hers to remember. In the cave she sometimes began an account of the day aloud before deciding whether she meant to finish it. She made no claim to have received an answer merely because she wanted one.{/n}''',
    requires=("soana.late_campaign_kept", "ascended"), forbids=(*LOSS, "soana.closed", "inhuman"))
ending("unrecognizable_return", "What the invitation did not permit", '''{n}What the Commander became could not be welcomed by reciting an earlier invitation. Soana knew the temptation to call a dangerous power necessary and then require everyone near it to accept the cost. Recognition did not make her willing to surrender her own door.{/n}
{n}She remembered the visits that had been freely chosen. They gave the new being no ownership of her, no right to obedience, and no power to turn fear into the affection she had once offered. Those evenings remained part of her life. They did not bind the rest of it.{/n}''',
    requires=("soana.late_campaign_kept", "inhuman"), forbids=(*LOSS, "soana.closed"))
SCENES.append(scene("soana.ending_native_loss", "The path that could not be kept", "Epilogue", 0, "", [
    n("start", "Narrator", '''{n}What followed at Wintersun ended the future imagined during the Commander's visits. The work already done had not been worthless. The warmth or friendship freely offered had not been a lie. Neither had protected the forest against everything that could come afterwards.{/n}''',
        c("[Remember Soana's death at Camellia's hand.]", "camellia", requires=("soana.killed_by_camellia",)),
        c('[Remember the woman who died.]', "dead", requires=("soana.dead",), forbids=("soana.killed_by_camellia",)),
        c('[Remember the forest that was lost.]', "forest", requires=("soana.forest_dead",), forbids=("soana.dead", "soana.killed_by_camellia",)), portrait="Soana"),
    n("camellia", "Narrator", '''{n}Camellia killed Soana. The last evening at the cave could not be remembered honestly without also remembering that ending. A woman who had defended her own right to choose, argued fiercely and offered affection in her own terms had not been preserved by having once been loved.{/n}
{n}The familiar path no longer led to her impatient welcome. No retelling of the earlier visits could make her death into a willing farewell, or turn the interrupted life into something already complete.{/n}''', portrait="Soana"),
    n("dead", "Narrator", '''{n}Soana died, and the practical objects she had handled outlasted her: a carrier with a repaired handle, a stick worn smooth where she gripped it, words crowded onto a page that had been corrected too often. They were evidence of a life, not a method of returning it.{/n}
{n}She had been difficult company and had known it. She had also made room beside her. Both belonged in any account of the woman whose voice would no longer answer from the cave.{/n}''', portrait="Soana"),
    n("forest", "Narrator", '''{n}The forest's loss broke the arrangement the visitors had worked to keep. The limited harvest, the marked approach and the young trees had depended on a place that could still sustain them. Its destruction was not undone by remembering how carefully a smaller danger had once been contained.{/n}
{n}The future imagined beside that cave could no longer be claimed as something already secured. What remained certain was the time actually shared there, and the person Soana had been when she chose to share it.{/n}''', portrait="Soana"),
], Relationship="soana", last=99, requires=("soana.late_campaign_kept",), RequiresAny=list(LOSS)))
ending("aeon", "A path outside the remembered world", '''{n}In the history remade without the Worldwound, the private road the Commander had taken to Soana's cave had no cause to unfold as it once had. No trapped fox led to the same water carrier, no borrowed voice brought the same three people to a sealed bowl, and no last evening could compel the new world to preserve the choices of the old.{/n}
{n}Whatever Soana's life became in that history, it was not a reward owed to the vanished Commander. Corven's place in it could not be decided by a memory the new world did not share. Neither love nor friendship entitled the erased visitor to summon her out of the life that remained her own.{/n}''',
    requires=("soana.progression_kept",), owner="AeonEpilogue")

# Preserve completed late endings; these acknowledge a history interrupted earlier.
ending("unfinished_sacrifice", "The conversation left unfinished", '''{n}The Commander's sacrifice ended a conversation Soana had expected to continue. She had not been given a completed farewell to treasure in place of the next visit. There were questions she had saved, an answer she meant to dispute, and ordinary company she had begun to want without inventing work for it.{/n}
{n}She heard the accounts of what the sacrifice had achieved. They could be true without telling her how to endure the person it had taken. She kept the worn proposal, the blanket, and her own memory of the visits. She remembered exactly what had been promised, including the things both had left for another day.{/n}
{n}At times she began the foolish festival song and stopped before its ending. On other days she finished it. Neither was a measure of how well she understood what the Commander had done.{/n}''',
    requires=("soana.progression_kept", "sacrifice"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept", "inhuman", "ascended"))
ending("unfinished_ascent", "A question beyond its former reach", '''{n}The Commander's ascent carried their interrupted visits beyond the terms Soana had known how to discuss. She had wanted another visit from a particular person. Godhood was a considerable event and a poor substitute for that answer.{/n}
{n}She remembered the shared work, the closed shrine and the evening she had offered without demanding a service in return. Nothing in those memories established what a god would now choose. She would not supply the missing answer by calling her wishes a revelation.{/n}
{n}When she spoke the Commander's name, she used the voice with which she had once invited the traveler to sit. There was no charm around it, no bargain by which the invitation acquired a claim. She had learned enough about binding a needed presence to know that she could want something fiercely without making it hers.{/n}''',
    requires=("soana.progression_kept", "ascended"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept", "inhuman"))
ending("unfinished_change", "An invitation withdrawn", '''{n}The being the Commander became was not entitled to claim every part of the private future Soana had once been willing to discuss. Soana's earlier welcome had been offered to someone she could argue with, refuse and choose to see again. It did not consent in advance to every use of the power that followed.{/n}
{n}She kept her account of the visits without making it an excuse to open her door. The work at the shrine had happened. So had the laughter, the difficult admissions and the company she had wanted. Those things belonged to her life even when she no longer wanted what stood beyond it to come nearer.{/n}
{n}She had once called a terrible binding necessary. She recognized the danger of a familiar argument returning with a different face. Recognition gave it no further right to her.{/n}''',
    requires=("soana.progression_kept", "inhuman"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept"))

# These loss pages concern only earlier shared objects, never an unplayed late rite.
unfinished_loss = deepcopy(next(s for s in SCENES if s["Id"] == "soana.ending_native_loss"))
unfinished_loss["Id"] = "soana.ending_unfinished_loss"
unfinished_loss["Title"] = "The earlier path that ended"
unfinished_loss["Requires"] = ["soana.progression_kept"]
unfinished_loss["Forbids"] = ["soana.late_campaign_kept"]
unfinished_loss["Nodes"][0]["Text"] = '''{n}What followed at Wintersun ended the private future before the visits could reach their later farewell. A place had been made beside Soana, and time had been shared there. The unfinished part could not be recovered by describing the earlier evenings as though they had already settled everything.{/n}'''
unfinished_loss["Nodes"][-1]["Text"] = '''{n}The forest's loss destroyed the place in which Soana and the Commander had begun imagining further visits. The warning line and the sealed shrine had dealt with particular dangers. They had not preserved the whole forest against what followed.{/n}
{n}Their interrupted visits could not be given a completed future merely because that would make the account easier to end. What remained certain was the work and company actually shared, and Soana's own choice to welcome them.{/n}'''
SCENES.append(unfinished_loss)
