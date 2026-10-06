"""Wenduag on the Trickster path, the courtship (wenduag_trickster holds the device, the returns and Lann's price; the build
sheet is in Writer/handoffs/trickster/wenduag.md, "Implementation notes (R6)").

Every scene here Requires wenduag.trickster.with_you (she came back from her cairn, or she stayed at the Commander's side and
earned it: bought before Savamelekh could buy her, loyal to the Commander at his end, spared after betraying the Commander, or
redeemed and recruited at Lann's Q3) and Forbids wenduag.trickster.native: where her native romance lives or has finished, it
owns her, and nothing here plays. Every beat is Chapter 5, at a rest in Drezen (the native Chapter 3 window is never touched).

The commit (11 §2): she drags Sergeant Brask of the south gate in by the collar and drops him at the Commander's feet. What
the Commander does with him is the yes. The Commander's only no is to set him on his feet. The test before it is her trial
(the stain on the cuff, kept from the spec) and the gate, where Brask speaks first. Intimacy: her cairn, in the dark under
the citadel, where the strong one decides.

Must acknowledge (from her side, in her voice, no pair scene): Lann (wenduag_trickster), Yaniel, Savamelekh, Vellexia.
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines.wenduag_trickster import (ABYSS_CAIRN, BARE, BOTH, BOUGHT, BRASK_KNOWS, BRASK_MET, CAIRN, CLOSED, COMMITTED, DEATH_PROMISED,
                                          DEEP, DREZEN, GATE_SEEN, IN_PARTY, KILLED, LANN_GONE, LANN_HUB, LANN_IN, LANN_KNOWS,
                                          LANN_LIED_AGAIN, LANN_OWED, LANN_PAID, LANN_PAID_LATE, LATE, LIED, MARK, NATIVE,
                                          PROVED, Q3_BETRAYED, Q3_KILLED, Q3_LOYAL, Q3_SENT, Q3_SPARED, REDEEMED, REL, RETURNED, SAVA_DEAD,
                                          SCENES as _DEVICE_SCENES, STARTED, STAY_DEAD, STREET_CAIRN, W, WATCH, WATER, WITH_YOU, HELLO_SENT, HELLO_ATTACKED,
                                          YANIEL_ASKED, YANIEL_FREED, YANIEL_KILLED, nar, page, tag, wd)

SCENES = []
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"      # NPC_Common/Irabeth/AnswersList_0009
IRABETH_GUARD = dict(forbids=("irabeth_dead", CLOSED), ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"})
VELLEXIA_SEEN = "wenduag.vellexia_conflict"          # Derived over the four "blond bitch" cues (trickster_world)
VELLEXIA_HERE = "vellexia.trickster.in_person"       # Derived: Vellexia walks Drezen in her own body (her route)

WON = W + "trial.won"
TRICKED = W + "trial.tricked"
BLED = W + "cost.bled"
GATE_HERS = W + "gate.hers"            # the Commander let her answer Brask
GATE_STRUCK = W + "gate.struck"        # the Commander broke Brask's nose
GATE_REBUKED = W + "gate.rebuked"      # the Commander sent her back to the cellars
STINGER_GIVEN = W + "stinger.given"
STINGER_BURNED = W + "stinger.burned"
PROMISE_OWED = W + "promise.owed"      # his death at her hand was promised, and somebody else got it
GIVEN = W + "claim.given"              # [He's yours]
KNELT = W + "claim.knelt"              # [On your knees, sergeant]
STRUCK = W + "claim.struck"            # [Do it yourself]
CAIRN_SEEN = W + "court.cairn"
KNIFE = W + "cairn.knife_held"
UNDER = W + "cairn.rolled"
STONE = W + "morning.stone"
PARTNER = W + "partner"                # Derived (Last Call, the Ledger): committed here, or her native romance kept to the end
_DERIVED_EXTRA = {PARTNER: [[COMMITTED], ["wenduag.romance_finished.latched"]]}

VISIT = dict(requires=("trickster.ever", WITH_YOU), forbids=(NATIVE, CLOSED))


def visit(id, title, nodes, requires=(), forbids=(), delay=24, optional=False, kind="visit", **extra):
    page(id, title, nodes, requires=VISIT["requires"] + tuple(requires), forbids=VISIT["forbids"] + tuple(forbids),
         delay=delay, chapters=(5,), kind=kind, optional=optional, **extra)
    SCENES.append(_DEVICE_SCENES.pop())


# --- 1. Weak things die in their sleep (the test before the yes; a failed check bleeds, and never blocks). -------------------

visit(W + "court.trial", "Weak things die in their sleep", [
    nar("start", '''{n}You fall asleep over the maps, which you have been doing too often, with your cheek on the Worldwound and a candle burning down beside your elbow.{/n}
{n}You wake because you cannot breathe. There is a knee on your chest, and a weight behind it that is all bone and wire, and a knife laid flat along the side of your throat, cold, the edge just touching. The candle has gone out. Somewhere above you in the dark, someone is grinning; you can hear it in her breathing.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Weak things die in their sleep." {n}Wenduag's voice is very soft, and very close. She smells of the cellars and of raw meat.{/n} "My rule. I learned it in the Maze, where the ones who slept soundly didn't last. I sleep with one eye open. I always have." {n}The knee presses a little harder.{/n}''',
        c("Continue", "which_back", requires=(RETURNED,)),
        c("Continue", "which_kept", forbids=(RETURNED,))),
    wd("which_back", '''"You put me under stones, {mf|master|mistress}, and I dug. Now it's your turn. Are you a weak thing?"''',
        c("Continue", "which")),
    wd("which_kept", '''{n}She shifts her weight, and the knife slides a finger's width along your neck without cutting.{/n} "You kept me at your side. Your soldiers watch me pass and look at you as if you had let a wolf through the gate." {n}Her breath is warm on your ear.{/n} "I want to know if they're right. Show me."''',
        c("Continue", "which")),
    nar("which", '''{n}Her weight is on your breastbone and her knife is on your throat, and she is waiting, perfectly still, to see what you do.{/n}''',
        c('[Heave her off you and roll clear.]', check=dict(Skill="SkillAthletics", DC=26, Success="won", Failure="lost")),
        c('"Get off me, or finish it. You won\'t get a second try."', check=dict(Skill="CheckIntimidate", DC=26, Success="won_word", Failure="lost")),
        c('"Wait. You\'ve got a stain on your cuff."', "stain", mythic="Trickster")),
    nar("won", '''{n}You surge up under her with everything you have, hips and shoulders and both hands, and she goes over sideways off the map table, taking half the Worldwound with her, and hits the floor with a sound like a sack of kindling. By the time she is up on her haunches you are standing, with your own knife out.{/n}''',
        c("Continue", "won_her")),
    wd("won_her", '''{n}She stays crouched on the floor among the scattered maps and laughs up at you, with blood on her teeth where she bit her lip.{/n}
"Good. Good! You didn't think about it. You just moved." {n}She wipes her mouth with the back of her wrist and looks at the red on it with satisfaction.{/n} {n}She rubs her bitten lip.{/n} "You put me on the floor. I\'ll want another try when that knee stops aching."''',
        c("Continue", flags=(PROVED, WON, STARTED))),
    wd("won_word", '''{n}There is a long silence. The knife does not move. Then, very slowly, the weight comes off your chest, and she sits back on her heels on the edge of the table, and looks at you with her head on one side.{/n}
"You meant that." {n}She sounds pleased and a little surprised, the way a hunter sounds when a deer turns and lowers its antlers.{/n} "You'd have let me cut, and killed me with the blood still coming out of you. I could hear it in your voice." {n}She sheathes the knife.{/n} "Most people beg, with a knife on their throat. Or they pray. You threatened me." {n}She grins.{/n} "Good."''',
        c("Continue", flags=(PROVED, WON, STARTED))),
    nar("stain", '''{n}She doesn't look. She laughs, low, delighted, right against your ear.{/n} "The stain on the cuff. The oldest trick there is. I've seen it a hundred times."
{n}She is so pleased with the old trick that she leans back to grin at you, half a finger's width, and lifts the knife a hair off your throat to do it. That is all you needed. Since your first night in this citadel you have slept over these maps with your own dagger under the Worldwound, a hand's breadth from your fingers; Commanders who sleep without one do not stay Commanders long. While she laughed at the cuff, your hand found it. When her grin comes back down, the point is resting under her breastbone.{/n}''',
        c("Continue", "stain_her")),
    wd("stain_her", '''"...Cheat." {n}She goes very still on top of you, with her knife at your throat and yours under her heart. Her eyes are wide.{/n} "You said the stupid thing so I'd laugh at it." {n}And then she is grinning, all her teeth.{/n} "Filthy, clever cheat. You knew I'd know it. You wanted me to know it." {n}She laughs, and the laugh pushes her chest against your point, and she does not seem to care.{/n} "I\'ll try that on the next knight who comes down the cellar stair. He\'ll hate you for teaching me."''',
        c("[Put your dagger back under the maps.]", flags=(PROVED, TRICKED, STARTED))),
    nar("lost", '''{n}You heave, or you snarl, and it is not enough. She rides the heave the way you would ride a bucking mule, and her knee sinks into your chest until the ribs creak, and the edge of the knife turns, and draws.{/n}
{n}Not your throat. Your forearm, which you have thrown up without thinking: a long, shallow, deliberate cut from the wrist toward the elbow, neat as a tailor's seam.{/n}''',
        c("Continue", "lost_her")),
    wd("lost_her", '''{n}She watches it bleed with great interest.{/n} "You bleed well." {n}Her voice is thoughtful.{/n} "Lots of uplanders don't. They go white and fall over. You just looked at it." {n}She lifts the knife away and sits back on her heels, and licks the edge, once, the way you might taste a sauce.{/n} "Not strong enough tonight. But you didn't beg, and you didn't call for your guards." {n}She slides off the table.{/n} "That's something. Fine. You'll do." {n}At the door she looks back.{/n} "Get somebody to sew that. I'd do it, but I'd enjoy it too much."''',
        c("Continue", flags=(PROVED, BLED, STARTED))),
], forbids=(PROVED,), delay=24,
   # the delay counts from the stamped event that earned her (her return, or the bid); a native key carries no stamp
   RequiresAnyGroups=[[RETURNED, BOUGHT, Q3_LOYAL, Q3_SPARED, REDEEMED]])


# --- 2. The gate (the Commander's pivotal choice before the claim). -------------------------------------------------------

visit(W + "court.gate", "Sergeant Brask", [
    nar("start", '''{n}You are coming back from the lower town at dusk, with the last of the light going red over the walls, when you hear the south gate before you see it: a man laughing, loud and deliberate, the way men laugh when they want to be heard, and his watch laughing with him.{/n}''',
        c("Continue", "gate", forbids=(BRASK_KNOWS,)),
        c("Continue", "gate_knows", requires=(BRASK_KNOWS,))),
    n("gate", "Sergeant Brask", '''{n}Sergeant Brask has his back to you: a big man with a red neck and a new coat, brushed. He is standing in the postern with his arms folded, blocking it, and in front of him in the road, hooded, with a hunting spear over her shoulder and a brace of hares at her belt, is a Mongrel woman who has stopped walking.{/n}
"Back to your kennel, mongrel bitch. Gate's shut to your kind after dark. Captain's orders." {n}He grins over his shoulder at his men.{/n} "Or you can ask nicely. Go on. Beg."
{n}Under the hood, you see the gleam of her eyes. She has not moved. She has not looked at you. She knows you are there; she knew before you turned the corner. She is waiting to see what you do.{/n}''',
        c("Continue", "choose")),
    n("gate_knows", "Sergeant Brask", '''{n}Sergeant Brask is standing in the postern with his arms folded, blocking it, in his new coat. In front of him in the road, hooded, with a hunting spear over her shoulder, is a Mongrel woman who has stopped walking. He is not laughing at her. He is staring, and his red face has gone patchy.{/n}
"I know you." {n}He says it too loudly, for his men.{/n} "I saw you breathing in the street. I told the captain and he laughed at me. Traitor's head on the pole, that's the law." {n}He sees you, then, over her shoulder, and his jaw sets.{/n} "Commander. I'll have her taken in. Unless you want to tell me again I didn't see what I saw."
{n}Under the hood, she has not moved. She is waiting to see what you do.{/n}''',
        c("Continue", "choose")),
    nar("choose", '''{n}Every man of the watch is looking at you. So, from the dark of the hood, is she.{/n}''',
        c('[Say nothing. Let her answer him.]', "hers"),
        c('[Walk up to Brask and break his nose.]', "struck", alignment=("Evil", 1)),
        c('"Back to the cellars, Wenduag. Sergeant, stand aside for the Commander."', "rebuked")),
    nar("hers", '''{n}You stop where you are, and fold your arms, and wait.{/n}
{n}She understands at once. You see it go through her, a kind of shiver, like a hound slipped off a leash. She lets the hares fall at her feet. She puts back her hood, very slowly, so that he can see her face and her teeth, and she walks up to him until her nose is a finger's width from his chin, and she breathes in, long and deep, through her nose, the way a hunter smells a carcass to see if it is still good.{/n}
{n}Then she says, conversationally, "You've been drinking. And you're afraid. It's coming out of your skin." She licks her lips. "Uplanders always smell best afraid."{/n}
{n}Brask takes a step back. It is only one step. Every man on the gate sees it. She walks past him through the postern without hurrying, and his watch parts in front of her like water, and nobody laughs.{/n}''',
        c("Continue", "after_hers")),
    wd("after_hers", '''{n}She is waiting in the shadow of the gatehouse on the far side, spear on her shoulder, hares forgotten in the road.{/n}
"You let me." {n}There is something almost shy in it.{/n} "In front of all of them, you let me. You didn't fight it for me and you didn't tell me to walk past." {n}She looks back at the gate, where Brask is shouting at his men about nothing.{/n} "He'll hate me more now. That's good. Hate you can use." {n}Her eyes come back to you, bright in the dusk.{/n} "I'm going to remember this, {mf|master|mistress}. You'll see how."''',
        c("Continue", flags=(GATE_SEEN, GATE_HERS))),
    nar("struck", '''{n}You walk up behind Sergeant Brask and tap him on the shoulder, and when he turns round, surprised, you break his nose with your fist.{/n}
{n}It makes a sound like a green stick. He sits down hard in the road in his new coat, with blood running over his mouth, and stares up at you. None of his men moves. None of them is going to.{/n}
{n}Behind you, very softly, Wenduag laughs.{/n}''',
        c("Continue", "after_struck")),
    wd("after_struck", '''{n}She walks through the postern past the sitting sergeant, and on the far side she stops and looks at your hand, at the split knuckles.{/n}
"You did it yourself." {n}She takes your hand in both of hers and turns it over, and looks at the blood on it, his blood, and then at you.{/n} "Not a guard. Not an order. Your own hand." {n}Her thumb goes over the split skin, not gently.{/n} "Settling my quarrel for me would have shamed me. That wasn't settling it. That was you, answering someone who bit what's yours. A chief who sends somebody else is a chief nobody fears. You went." {n}She lets go.{/n} "His men will all be afraid of you now. And they'll hate me for it." {n}She grins.{/n} "Good. I like being hated for good reasons."''',
        c("Continue", flags=(GATE_SEEN, GATE_STRUCK))),
    nar("rebuked", '''{n}Brask steps aside for you, stiffly, and his men watch to see what the mongrel will do.{/n}
{n}She does not argue. She picks up her hares, and pulls the hood back down, and turns and walks back the way she came, toward the cellar stair, without a word. She does not look at you once. That is how you know how much it cost her.{/n}''',
        c("Continue", "after_rebuked")),
    wd("after_rebuked", '''{n}She is waiting for you at the bottom of the cellar stair, in the dark, with the hares at her feet.{/n}
"Back to the cellars." {n}She says it without heat, which is worse.{/n} "In front of him. In front of his men." {n}She studies you, as if you were a trail that has doubled back on itself.{/n} "I know why. You don't want the whole gate asking why the Commander protects a mongrel. You're thinking about your city." {n}She picks up a hare and weighs it in her hand.{/n} "That's what a chief does, too. Sometimes. I don't have to like it." {n}Then, very quietly:{/n} "He's going to pay for that, and not to you. You should know that now."''',
        c("Continue", flags=(GATE_SEEN, GATE_REBUKED))),
], requires=(PROVED,), forbids=(GATE_SEEN,), delay=24)


# --- 3. The stinger (optional): Savamelekh is dead, and someone else killed him. ------------------------------------------

visit(W + "court.stinger", "The stinger", [
    nar("start", '''{n}You bring it down to her in the cellars wrapped in sacking, because nobody should have to carry it in their bare hands: a curved black spike as long as your forearm, still sticky at the base where it was cut from his tail, and at the tip a clouded bead of something that the lamplight will not quite pass through.{/n}
{n}Savamelekh is dead. Whatever he fed the neathers of Neathholm for all those years, this is where it came from.{/n}''',
        c("Continue", "her")),
    wd("her", '''{n}Wenduag looks at it for a long time without touching it. Her nostrils flare.{/n}
"That's him." {n}Her voice is flat.{/n} "That's the smell. That's what was in the meat, every night, in his house. That's what called." {n}She reaches out one finger toward the black bead at the tip, and stops a hair's breadth from it, and draws her hand back.{/n}''',
        c("Continue", "promised", requires=(DEATH_PROMISED,)),
        c("Continue", "plain", forbids=(DEATH_PROMISED,))),
    wd("promised", '''"You offered me his death. My hand on the knife. His stinger cut off." {n}She looks from the spike to you.{/n} "Somebody else got the killing. Don\'t hand me the tail and tell me it\'s the same."''',
        c('"And now it\'s in your fist. Take it. Nobody else in the world will ever hold it."', "take"),
        c('"I owe you his death. I don\'t have it to give. I\'m not going to pretend otherwise."', "owed")),
    wd("take", '''{n}She takes it. She holds it by the cut end, where it is safe, and turns it so the lamplight runs along it, and her face does something you have never seen it do: it goes very young, and very old, at the same time.{/n}
"This kept my father alive." {n}She says it to the stinger, not to you.{/n} "Alive, and strong, and serving. Years of it. He was still standing among Savamelekh\'s children when I found him." {n}She wraps it back in its sacking with great care.{/n} "I\'ll keep it. Let the young ones smell what he fed their parents. If another bastard offers them meat that smells like this, they\'ll know what they\'re eating."''',
        c("Continue", flags=(STINGER_GIVEN,))),
    wd("owed", '''"No. You don't." {n}She looks at you for a long time. Then, surprisingly, she nods.{/n}
"You didn't lie. You could have. You could have told me you held him down for me and I missed it." {n}She takes the stinger, sacking and all, and tucks it under her arm.{/n} "You owe me a death, {mf|master|mistress}. A good one. Something as big as him. I'll tell you when I've picked it." {n}Her teeth show.{/n} "Don't worry. It won't be anyone you like. Probably."''',
        c("Continue", flags=(STINGER_GIVEN, PROMISE_OWED))),
    wd("plain", '''"He\'s dead." {n}Her shoulders loosen, then tighten again.{/n} "I wanted to see him fall. Now I\'ve got the part he meant to feed me with." {n}She reaches toward the spike, stops, and bares her teeth.{/n} "Put it down."''',
        c('"It\'s yours. Take it."', "take"),
        c('[Throw it on the brazier.]', "burn")),
    wd("burn", '''{n}She does not stop you. She watches it go into the coals, and hiss, and blacken, and the smell that comes off it makes her gag and put her sleeve over her mouth. The black bead at the tip bursts with a small wet sound.{/n}
{n}When it is only a curl of ash she takes her sleeve away.{/n} "Good." {n}Her voice is rough.{/n} "He doesn't get to leave anything behind with a hook in it. Not in my people. Not in me." {n}She wipes her eyes, which are running from the smoke.{/n} "Don't tell anyone I said that."''',
        c("Continue", flags=(STINGER_BURNED,))),
], requires=(RETURNED, SAVA_DEAD), forbids=(W + "court.stinger",), optional=True)


# --- 4. The claim (COMMIT): she drops Brask at the Commander's feet. -------------------------------------------------------

YES = (COMMITTED, STARTED)

visit(W + "court.claim", "What she caught", [
    nar("start", '''{n}The door of your quarters bangs open without a knock, and something heavy hits the floor at your feet and grunts.{/n}
{n}It is Sergeant Brask. His wrists are bound behind him with his own belt and his ankles with a strip torn from his own coat, and there is a gag in his mouth that is also, unless you are mistaken, a piece of his own coat. The rest of the coat is gone. His nose is bleeding. His eyes are enormous.{/n}
{n}Wenduag steps in over him and shuts the door with her heel.{/n}''',
        c("Continue", "her")),
    wd("her", '''"I caught him on the wall walk behind the south gate. Alone, for once. He was brushing his coat." {n}She pushes back her hood. She is flushed and bright-eyed and very pleased with herself, and there is a scratch down one cheek that she has not bothered to wipe.{/n} "He fought. Not well. I didn't hurt him much. I wanted him to be able to see."''',
        c("Continue", "why_knows", requires=(BRASK_KNOWS,)),
        c("Continue", "why", forbids=(BRASK_KNOWS,))),
    wd("why_knows", '''"He tried to have me taken at your gate. He's been telling people he saw me breathing in the street. The captain laughed at him. The next one might not." {n}She nudges Brask with her toe, not hard, the way you nudge a sleeping dog.{/n} "So he's your problem too. But that's not why I brought him."''',
        c("Continue", "why")),
    wd("why", '''{n}She crouches beside him, easy on her heels, and looks up at you across his body.{/n}
"I don't bring flowers. What would I do with flowers? I bring what I caught. The best thing I caught. And I put it at your feet, and I watch what you do with it." {n}She puts a hand flat on Brask's heaving back.{/n} "That's how I ask. I've never asked anybody before, so it's the only way I know. If you take it, you're mine. If you kick it away, well." {n}She shrugs.{/n} "Then I know."''',
        c("Continue", "want")),
    wd("want", '''"He's had his mouth on me at your gate, in front of his men, more than once. He laughed while he did it. He'd have put my head on a pole and brushed his coat under it." {n}Her voice is very steady.{/n} "And he's yours. One of your soldiers, in your city, under your law." {n}She stands.{/n} "So he's the best thing I could catch. Something of mine, that's also something of yours." {n}She folds her arms and waits.{/n} "Well. There he is."''',
        c('[Nudge him toward her with your boot.] "He\'s yours."', "given", alignment=("Evil", 1)),
        c('[Pull out his gag.] "On your knees, sergeant. Ask her pardon. Use her name."', "knelt", alignment=("Chaotic", 1)),
        c('[Take her knife off her belt, and do it yourself.]', "struck"),
        c('[Cut his bonds and set him on his feet.] "Get up, sergeant. Back to your gate."', "no")),
    wd("given", '''{n}She looks at you for a moment, very still. Then she smiles, slow and wide, until every one of her teeth is showing.{/n}
"Mine." {n}She hauls Brask up by the back of his collar, one-handed, as if he weighed nothing, and he makes a thin noise through his gag.{/n} "Don't worry, sergeant. I'm not going to kill you. Dead men forget. I want you to remember." {n}She drags him to the door and out, and it swings shut behind them.{/n}
{n}Whatever happens on the wall walk behind the south gate that night, the watch does not hear it, or says it did not. In the morning Brask is in the infirmary with two fingers of his sword hand broken and every button cut off his shirt, and he tells the chaplain he fell down the stairs, and he never, afterwards, says the word *mongrel* in anyone's hearing again.{/n}''',
        c("Continue", "after_given")),
    wd("after_given", '''{n}She returns before midnight and drops Brask\'s last button on your map. His blood is drying under her nails.{/n} "Two fingers broken. He\'ll remember which hand pointed at me." {n}She rolls the button toward you.{/n} "Savamelekh always put something in the meat. You gave me this one and let me choose what to break." {n}She sits on the table and traps your hand against her thigh.{/n} "Keep the button. I want to see you touch it when he salutes."''',
        c("Continue", flags=YES + (GIVEN,))),
    n("knelt", "Sergeant Brask", '''{n}Brask spits out the rag and draws breath to shout, and sees your face, and does not. He gets his knees under him, awkwardly, with his hands still tied behind his back, and kneels there in his shirt on your floor with his nose dripping.{/n}
"I..." {n}He swallows.{/n} "I ask your pardon. Wenduag." {n}He looks at you.{/n} "Of Neathholm."''',
        c("Continue", "after_knelt")),
    wd("after_knelt", '''{n}She cuts Brask's bonds and lets him stumble out, then laughs until her shoulders shake.{/n} "Wenduag of Neathholm. He got every bit out. On his knees." {n}She catches your face between her hands; her thumbs are rough against your jaw.{/n} "Tomorrow he\'ll have to open the gate for me. I\'ll make him look at my face while he does it." {n}She brings her mouth close to yours.{/n} "Say it. I want to hear how it sounds from you."''',
        c("Continue", flags=YES + (KNELT,))),
    nar("struck", '''{n}She lets you take it. She watches you do it with her lips parted.{/n}
{n}You pull Brask's head back by the hair, and lay the flat of her knife along his cheek so that he can feel the cold of it, and then turn it and draw the point once across the back of his hand, the one he points with, where everyone who salutes him will see the line every day of his life. Not deep. Deep enough.{/n}
{n}Then you cut his bonds with the same knife, and open the door, and he goes, without a word, clutching his hand.{/n}''',
        c("Continue", "after_struck")),
    wd("after_struck", '''{n}She takes back the knife and draws one finger along its flat, through Brask\'s blood.{/n} "My blade. Your hand." {n}She wipes it on her sleeve and puts it away.{/n} "He\'ll show that line every time he salutes." {n}Her teeth press against your neck, then release. She keeps her mouth there when she speaks.{/n} "I\'ve left you something to show him, too. Wear your collar low tomorrow."''',
        c("Continue", flags=YES + (STRUCK,))),
    wd("no", '''{n}Brask scrambles up, rubbing his wrists, and does not wait to be told twice. The door bangs behind him.{/n}
{n}Wenduag has not moved. She is looking at you as if you had turned into a stranger in front of her eyes.{/n}
"Back to your gate." {n}She repeats it slowly.{/n} "I brought you the best thing I could catch, and you let it go." {n}She is not angry. That is the worst of it.{/n} "Then you're not mine. And I'm not yours. That's what it means, the way I ask. That's all it means." {n}She pulls her hood up.{/n} "I'll still fight your war. I'm not stupid. But don't come down the cellar stair any more, {mf|master|mistress}. The neathers won't let you through."''',
        c("Continue", flags=(CLOSED, W + "court.claim_refused"))),
], requires=(PROVED, GATE_SEEN), forbids=(COMMITTED, IN_PARTY), delay=24)

# Kept at the Commander's side, she is a living companion: the claim is played in person, on her own native list (R2-3).
# The twin opens on the walk to the Commander's quarters; the rest is the same scene. Mutually exclusive by IN_PARTY.
HUB_LISTS = ["ced27e744d2dded40bbb5adf17816dbb",    # CompanionDialogues/Wenduag/AnswersList_0003 (W path)
             "9bad7ea452d30254997b153473954cc1",    # WenduagTraitorCompanion/AnswersList_0003 (L path, recruited)
             "b14654863485b734aa0fb5ec16d2846a"]    # WenduDubious_Companion/AnswersList_0003 (redeemed, recruited at Lann's Q3)
_claim = copy.deepcopy(SCENES[-1])
_claim["Id"] = W + "court.claim_in_person"
_claim["Entry"] = '"You look pleased with yourself."'
_claim.pop("Remote", None); _claim.pop("Kind", None)   # Areas stays [Drezen]: the scene is the Commander's quarters
_claim["Requires"] = ["trickster.ever", WITH_YOU, IN_PARTY, PROVED, GATE_SEEN]
_claim["Forbids"] = [NATIVE, CLOSED, COMMITTED, _claim["Id"]]
_claim["AnswerLists"] = HUB_LISTS
_claim["ReturnToList"] = True
_claim["ReturnText"] = "{n}Wenduag is sitting on your map table, eating, as if nothing at all had happened tonight.{/n}"
_claim["Nodes"][0] = n("start", "conversant", '''{n}She does not answer. She jerks her head toward the stair to your quarters and walks, and you follow her up, and when she opens your door something heavy lies on the floor inside, bound hand and foot, and grunts.{/n}
{n}It is Sergeant Brask. His wrists are tied behind him with his own belt and his ankles with a strip torn from his own coat, and the gag in his mouth is, unless you are mistaken, also a piece of his own coat. The rest of the coat is gone. His nose is bleeding. His eyes are enormous.{/n}
{n}Wenduag steps in over him and shuts the door with her heel.{/n}''', c("Continue", "her"))
for _node in _claim["Nodes"][1:]:
    if _node["Speaker"] == "Wenduag":
        _node["Speaker"] = "conversant"
        _node["Portrait"] = ""
SCENES.append(_claim)
tag(_claim["Id"], "T")

# Returned from her cairn, she is played in person too: a spawned copy of her unit at the place in Drezen where her native
# exile walks her out (LannWenduGoAwayLocator, DrezenCapital main scene; no other presence uses it). The native unit stays
# dead or gone; this copy is RRT's living Wenduag. The claim moves onto it.
UNIT = "ae766624c03058440a036de90a7f2009"              # Wenduag_Companion
PRESENCE = "wenduag.presence"
PRESENCES = {
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy",
                   At=dict(Locator="f8cfa132-6536-4fc5-a2be-1c49b0165202", Offset=[0.0, 0.0]),
                   Requires=["trickster.ever", RETURNED], Forbids=[CLOSED, IN_PARTY, COMMITTED], MinChapter=5, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   Greeting=("{n}A neather woman in a hunter's hood is crouched against the wall where the street from the south "
                             "gate comes up toward the citadel, a spear across her knees, watching the gate. Soldiers going "
                             "past give her a wide berth without knowing why. Under the hood, her teeth show.{/n}")),
}
_remote = next(x for x in SCENES if x["Id"] == W + "court.claim")
_remote.pop("Remote", None)
_remote.pop("Kind", None)
_remote["ContactUnit"] = UNIT
_remote["InteractionHub"] = PRESENCE
_remote["Entry"] = '"What have you got there?"'
_remote["Nodes"][0] = n("start", "Narrator", '''{n}Boots scrape the postern steps. Wenduag drags a bound man into the wall angle by his collar and drops him at your feet. The watch above cannot see him, but his muffled curses carry.{/n}
{n}It is Sergeant Brask. His wrists are tied behind him with his own belt and his ankles with a strip torn from his own coat, and the gag in his mouth is, unless you are mistaken, also a piece of his own coat. The rest of the coat is gone. His nose is bleeding. His eyes are enormous.{/n}
{n}Wenduag puts her foot on his back, the way a hunter rests a foot on a kill, and pushes back her hood.{/n} "Not out here. Take his feet."
{n}Between you, you carry him up the back stair of the citadel like a rolled carpet, past a sentry who finds something very interesting in the ceiling, and into your quarters, and she drops him on your floor and shuts the door with her heel.{/n}''', c("Continue", "her"))


# --- 5. Her cairn (intimacy; Directive 12: heat up to the cut, cut at the start of the act). --------------------------------

visit(W + "court.cairn", "In the dark, the strong one decides", [
    nar("start", '''{n}She comes for you after midnight, and takes you down: past the storerooms, past the cellars where the neathers sleep in their heaps and lift their heads as you go by, down the oldest stair to the catacombs, where Drezen's dead lay in their niches before there were too many dead to bother.{/n}
{n}At the bottom she stops, and takes the lamp out of your hand, and blows it out.{/n}''',
        c("Continue", "dark")),
    wd("dark", '''"You don't know this place. I do." {n}Her voice is right beside your ear, and then it is not; she moves without a sound on the old stone.{/n} "Down here you're the weak one. You don't know where the walls are, or which stones move, or where I am." {n}Her hand closes round your wrist, hard, calloused, very warm.{/n} "So you'll have to let me lead."''',
        c("Continue", "stones")),
    wd("stones", '''{n}She walks you through the dark by the wrist, twenty steps, thirty, turning twice, until you have no idea where you are. Then she puts your hand on something cold and rough: stones, piled, waist high, dry to the touch.{/n}
"My cairn." {n}She says it the way another woman might say *my bed*.{/n}''',
        c("Continue", "own_street", requires=(STREET_CAIRN,)),
        c("Continue", "own_built", requires=(RETURNED,), forbids=(STREET_CAIRN,)),
        c("Continue", "own_kept", forbids=(RETURNED,))),
    wd("own_street", '''"The one you built. Down here, at the bottom of the stair. I put it back together after I dug out of it, stone for stone. It's the only thing an uplander ever made for me that I didn't have to take."''',
        c("Continue", "top")),
    wd("own_built", '''"The one you built is a long way from here. So I built it again, down here, stone for stone, the way you did it. The head end loose." {n}A breath of a laugh in the dark.{/n} "A hunter ought to know where she's going to lie."''',
        c("Continue", "top")),
    wd("own_kept", '''"I built this one myself, before I needed it. So I'd know where I was going, and nobody would get it wrong." {n}A breath of a laugh in the dark.{/n} "I wasn't going to let an uplander get it wrong."''',
        c("Continue", "top")),
    wd("top", '''{n}You hear her draw her knife. You feel her lay it, flat, on the topmost stone, under your hand, so that your fingers rest on the bone of the grip.{/n}
"There. Now you've got a knife and I haven't." {n}She is behind you. Her breath is on the back of your neck.{/n} "I put every stone here. I know where you can stand. You don\'t." {n}Her hands come round and find the buckle of your belt, and stop there.{/n} "You can pick it up, if you like. Hold it on me. See how far it gets you, when you can't see where I am."''',
        c('[Leave the knife where it is. Let her decide.]', "decide"),
        c('[Pick up the knife and turn round, blade first.]', "knife"),
        c('[Take her wrists instead, and turn her against the stones.]', "roll")),
    nar("decide", '''{n}You take your hand off the knife.{/n}
{n}She makes a sound in her throat that is not a word. Then the buckle is open and your belt is gone, somewhere into the dark, and her hands are everywhere, rough and quick and certain, and not in the least gentle: she undresses you the way she skins a hare, with no wasted movement and no hesitation at all, and the cold of the catacomb comes onto your skin all at once and then her heat after it.{/n}
{n}She shrugs off her leathers and pushes you back against the cairn. The stones are cold and uneven against your spine. Her tail comes round your thigh, and tightens, and holds.{/n}''',
        c("Continue", "cut")),
    nar("knife", '''{n}You pick it up and turn, and there is nothing there. Only dark, and cold stone, and the smell of her somewhere very close.{/n}
{n}Then her hand closes over yours on the grip, and guides the point, unhurried, until it rests in the hollow of her own throat, and she presses forward into it until you feel her pulse through the blade. You cannot see her. You can hear that she is smiling.{/n}
"Good," {n}she says, against the edge.{/n} "Keep it there." {n}And with her other hand, one-handed, without looking, she begins to unlace her own leathers.{/n}''',
        c("Continue", "cut", flags=(W + "cairn.knife_held",))),
    nar("roll", '''{n}You find her wrists in the dark, both of them, and she lets you, for exactly as long as it takes you to turn her against the cairn, and then she laughs and twists and it is you against the stones again, with her forearm across your collarbones and her whole weight leaning on it.{/n}
"Nice try." {n}Her teeth close on the side of your throat, hard enough to mark, and let go.{/n} "Again." {n}You try again. This time it takes her longer. By the third time your clothes lie in a heap beside the lamp, and you are not sure any longer who is winning, and neither, from the sound of her, is she.{/n}''',
        c("Continue", "cut", flags=(W + "cairn.rolled",))),
    wd("cut", '''{n}Her bare skin is hot against yours. She kisses you hard, one hand gripping the back of your neck. When she pulls away, her teeth drag over your lower lip.{/n} "Still want to see?" {n}You catch her hips and draw her closer. Her knee presses between your thighs; she laughs against your mouth, breathless.{/n} "Now, uplander. Put those hands to work." {n}High above the catacombs, a bell begins to strike.{/n}''',
        c("Continue", flags=(CAIRN_SEEN,))),
], requires=(COMMITTED,), forbids=(CAIRN_SEEN,), delay=24)


# --- 6. The morning (the consequence). --------------------------------------------------------------------------------------

visit(W + "court.morning", "Grit in your hair", [
    nar("start", '''{n}You wake alone, in the dark, on cold stone, with your coat thrown over you and grit in your hair and a dull ache in every part of you that has ever been leaned on.{/n}
{n}Somebody has left the lamp beside your hand, lit, turned low. By its light you can see the cairn, and your belt draped over the top of it, and the gap in the topmost row where one of the flat stones used to be.{/n}''',
        c("Continue", "stone")),
    nar("stone", '''{n}It is not gone. It is in your coat pocket: a flat grey stone a little bigger than your palm, with a single line scratched across it by a knife point, still sharp-edged and fresh.{/n}
{n}The cut is fresh. You run your thumb along it and find grit beneath the nail.{/n}''',
        c("Continue", "stairs")),
    nar("stairs", '''{n}When you come up the cellar stair the neathers are awake, squatting over their breakfast fires, and every one of them looks up at you, and sniffs, and looks away again, grinning. An old one-eyed woman cackles out loud and slaps her knee. By noon, you suspect, every neather in the city will know exactly where the Commander spent the night, and by nightfall the whole citadel will know that the neathers know something, and nobody will dare to ask them what.{/n}''',
        c("Continue", "given", requires=(GIVEN,)),
        c("Continue", "knelt", requires=(KNELT,), forbids=(GIVEN,)),
        c("Continue", "struck", forbids=(GIVEN, KNELT))),
    nar("given", '''{n}At the south gate, a new sergeant has the watch, a quiet woman from Nerosyan who salutes you without meeting your eyes. Brask, they tell you, has asked to be transferred to the wall at the far end of the lower town, as far from the cellar stair as it is possible to be inside Drezen. Nobody asks why. Everybody knows.{/n}''',
        c("Continue", "end")),
    nar("knelt", '''{n}At the south gate, Brask has the watch as usual. He salutes you with great care, and when a cellar neather comes through the postern with a brace of hares he stands aside for her without a word, and his men, who have all heard by now what he said on his knees, and to whom, do not laugh at anything all morning.{/n}''',
        c("Continue", "end")),
    nar("struck", '''{n}At the south gate, Brask has the watch as usual, with a bandage on the back of his right hand. He salutes you with it. It is a very careful salute, and he does not take his eyes off your face while he gives it, and neither do any of his men.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}Wenduag is gone all day. At nightfall she is in your quarters again, eating supper from the pot. A fresh hare hangs from her belt.{/n}''',
        c('[Put the stone on the table beside her.]', flags=(STONE,)),
        c('[Keep the stone in your pocket, and say nothing about it.]', flags=(STONE, W + "morning.pocket"))),
], requires=(CAIRN_SEEN,), forbids=(STONE,), delay=8)


# --- 7. Must acknowledge: Vellexia and Yaniel (optional, from her side, node variants on their own native flags). ----------

visit(W + "court.vellexia", "The blond one", [
    nar("start", '''{n}Wenduag has found a new sport. She sits on the parapet above the citadel yard for an hour at a time, very still, and watches one particular window.{/n}''',
        c("Continue", "promised", requires=(VELLEXIA_SEEN,)),
        c("Continue", "here", forbids=(VELLEXIA_SEEN,))),
    wd("promised", '''"The blond one." {n}She does not take her eyes off the window.{/n} "The succubus from the Midnight Isles. I promised her something, the night we met. I told her I'd make her scream." {n}Her lips peel back.{/n} "With pleasure, I said. I meant it, too, that night. Don't mistake that for liking the bitch. I keep my promises, {mf|master|mistress}. The fun ones. I'm deciding which kind this one is."''',
        c("Continue", "what")),
    wd("here", '''"There's a succubus in your citadel." {n}She does not take her eyes off the window.{/n} "Walking about in the day like a lady, with that yellow hair and that smile, and your whole court pretending not to notice what she smells like." {n}She sniffs, deliberately.{/n} "I noticed. I notice everything that's hungry."''',
        c("Continue", "what")),
    wd("what", '''{n}She turns her head at last and looks at you, and there is a question in her face that she is not going to ask aloud.{/n}
"A demon took my father and made him his. Demons fed me, and made me grateful." {n}Her voice is flat.{/n} "I'm not going to pretend I like a demon in your house because she's got nice manners. So tell me what she is to you, {mf|master|mistress}, and I'll tell you what I'm going to do about it."''',
        c('"Leave her be. She\'s under my roof, and nobody in it gets hunted."', "leave"),
        c('"Hunt her, if you want. Frighten her. Nobody dies."', "hunt")),
    wd("leave", '''"Under your roof." {n}She weighs it, and does not like it, and puts it down.{/n} "All right. I'll leave her be. Under your roof." {n}She turns back to the window.{/n} "Outside it, she's meat, like everybody else. Tell her that, when you see her. Tell her the neather said so. She'll know what it means; her kind always do."''',
        c("Continue", flags=(W + "vellexia.left",))),
    wd("hunt", '''{n}Her face lights up like a child's.{/n} "Nobody dies." {n}She says it the way she said it at the gate, like the terms of a bad bargain she has every intention of enjoying.{/n} "You're no fun. But all right. Nobody dies." {n}She slides off the parapet.{/n} "She'll hear me coming, though. Every night, somewhere in the dark, just behind her. A hare's head on her pillow. My knife in her door. Her own scent on my hands when I pass her in the hall. She'll never see me. She'll never know when." {n}Her grin is terrible.{/n} "And one night she'll turn round and I'll be close enough to bite, and I'll let her feel my teeth on her throat, and I'll let her live. That's the scream I promised. The fun ones are the ones they remember."''',
        c("Continue", flags=(W + "vellexia.hunted",))),
], requires=(GATE_SEEN, VELLEXIA_HERE), optional=True)   # only while Vellexia walks Drezen in her own body

visit(W + "court.yaniel", "The paladin in the cage", [
    nar("start", '''{n}Wenduag has heard the story at last. The neathers in the cellars tell it among themselves: the paladin taken when Drezen fell, who spent seventy years a prisoner, first on Areelu's tables and then in Minagho's Fane, fighting every guard she could reach until they made her a husk.{/n}''',
        c("Continue", "freed", requires=(YANIEL_FREED,)),
        c("Continue", "killed", forbids=(YANIEL_FREED,))),
    wd("freed", '''"And you brought her out of it." {n}She sounds almost resentful.{/n} "Seventy years, and she came out of it holding a sword." {n}She is quiet for a while.{/n} "The crusaders follow a legend before they follow the living. Legends don't make mistakes. That one isn't dead, and she isn't a legend yet either. She's the one to watch, {mf|master|mistress}. Not the demons. Her." {n}She shrugs.{/n} "I'm not saying do anything. I'm saying watch. Uplanders never learn the difference till the knife's already in."''',
        c('"She\'s no threat to either of us."', "threat"),
        c('"You sound jealous."', "jealous")),
    wd("threat", '''"Everybody who's still breathing is a threat to somebody." {n}She shrugs.{/n} "But fine. I'll watch her for you. I watch everybody anyway."''',
        c("Continue", flags=(W + "yaniel.watched",))),
    wd("jealous", '''{n}She bares her teeth, which is not a no.{/n} "Of what they'll sing about her, maybe. Nobody sings about neathers. We don't last long enough."''',
        c("Continue", flags=(W + "yaniel.jealous",))),
    wd("killed", '''"And you killed her. In the Fane." {n}She turns her head and looks at you, curious, careful, as if she were testing ice.{/n} "Seventy years a prisoner and a husk, and a legend of the crusades, and you put her down. I've been trying to work out why. If you were afraid of her, that's cunning. If you did it for no reason at all, that's a sickness, and I'd like to know which one I've tied myself to."''',
        c('"She\'d have been a rival. Better now than later."', "rival"),
        c('"It was a mistake."', "mistake")),
    wd("rival", '''{n}She is quiet for a long while. Then a slow, pleased smile.{/n} "Now or later. Yes. That's how it's done in the tunnels, when two hunters want the same place by the fire." {n}She nods, satisfied.{/n} "The lesson of cunning. I'll remember that you know it."''',
        c("Continue", flags=(W + "yaniel.rival",))),
    wd("mistake", '''{n}Her disappointment is sharper than anger would have been.{/n} "A mistake." {n}She looks away.{/n} "The strong are allowed to kill. They're not allowed to be stupid about it. That's how they stop being strong."''',
        c("Continue", flags=(W + "yaniel.mistake",))),
], requires=(GATE_SEEN,), RequiresAnyGroups=[[YANIEL_FREED, YANIEL_KILLED]],
    forbids=(W + "early.yaniel", YANIEL_ASKED), optional=True)


# --- 7b. More of her (optional beats; each is her canon: the tunnels, the tribe, the hunt, the Maze). ------------------------

page(W + "killed.cellar", "Among the cellar neathers", [
    nar("start", '''{n}The neathers who came up from Neathholm after Lann's reckoning live in the cellars under the citadel: Sull's people, and the ones who followed them, in heaps of hides and straw between the old storerooms, where it is dark and damp and smells like home to them. They watch you come down the stair with their yellow eyes and say nothing, and nobody stops you.{/n}
{n}She is in the furthest cellar, lying on her back on a hide with her shirt pulled up and an old neather woman packing something grey and foul-smelling into the seam in her side. She does not look round.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Moss, spit, and something she won\'t name." {n}Wenduag hisses as the old woman presses the dressing into place.{/n} "Getting this closed is taking longer than I\'d like. A chaplain sees my face, he\'ll ask why the dead woman needs a bottle." {n}She looks up at you.{/n} "Bring him down here and he\'ll bring questions back up."''',
        c('"How long before you can fight?"', "fight"),
        c('"What was it like, under the stones?"', "under")),
    wd("fight", '''"I can fight now. I can't win." {n}She says it as if it were an obvious distinction, which to her it is.{/n} "Ten days, or near it. Then I'll be what I was. More, maybe. The dark does that, if it doesn't eat you." {n}She lets her head fall back on the hide.{/n} "I\'m hungrier than I was before your knife. Once this closes, you can find out how much."''',
        c("Continue", "sull")),
    wd("under", '''{n}She is quiet for a while, and the old woman packs the wound, and hums.{/n}
"Quiet." {n}She sounds surprised by her own answer.{/n} "That's what I remember most. Not the dark. Neathholm's dark; I was born in it. The quiet. No gongs, no tribe, no Lann, nobody telling me what I was. Just the stone on my face and my heart going, and the knife." {n}She flexes her right hand.{/n} "I lay there a long time before I pushed. Longer than I needed to. I wanted to know what it was like to be nobody's anything." {n}Then she snorts.{/n} "It was boring. So I dug."''',
        c("Continue", "sull")),
    wd("sull", '''{n}She jerks her chin toward the other cellars, where the neathers are.{/n}
"The old ones down here know. They smelled it on me. If Lann hasn\'t heard yet, it isn\'t because they went looking for him." {n}Her lip curls.{/n} "That's what old ones are for." {n}She closes her eyes.{/n} "Go away now, {mf|master|mistress}. I'm going to sleep, and I don't let anyone watch me do that. Not even you. Especially not you."''',
        c("Continue", flags=(W + "cellar.seen",))),
], requires=("trickster.ever", RETURNED, KILLED), delay=24, chapters=(3,), optional=True)

SCENES.append(_DEVICE_SCENES.pop())

SCENES.append(scene(W + "traitor.nerves", "The call", "Wenduag", 4, '"You haven\'t eaten since we came to the Midnight Isles."', [
    n("start", "conversant", '''{n}Wenduag is sitting on her heels at the edge of the camp, facing the city, the way a dog sits facing a door it is not allowed through. There are dark, oily streaks on her cheeks, dried, as if she has been crying tar and wiped it away with her sleeve.{/n}
"I can't eat. It's all wrong here. The meat tastes of him." {n}She does not turn round. Her voice is flat and very low, with none of the servant in it.{/n} "He's here, {mf|master|mistress}. Somewhere in this city. I can feel him in my blood, like a hook in a fish. He isn't calling yet. He's letting me feel how easy it would be."''',
        c('"And when he calls?"', "calls"),
        c('"Your face. What is that?"', "tears")),
    n("tears", "conversant", '''{n}She touches her cheek, looks at the black on her fingertip, and wipes it off on the ground with disgust.{/n}
"His poison. It comes out when he's near. Any of us with his blood in us weeps it; even Lann can't hide from it." {n}Her mouth twists.{/n} "Last time I cried it was salt, and it was for my father. Now he gets to make me cry tar. Isn't that funny?"''',
        c('"And when he calls?"', "calls")),
    n("calls", "conversant", '''"When he calls, I go. You know that. That was the bargain." {n}She finally turns her head and looks at you, and her eyes are bloodshot and very steady.{/n} "I'll go to him and kneel and say *yes, master*, and I'll mean it, a little, because of what's in my blood. And I'll fight you, because he'll tell me to. And I'll try to kill Lann, because that's what he'll believe." {n}She swallows.{/n} "And then I'll fall down. That's the part I keep thinking about. That's the part I have to get right."''',
        c('"I\'ll be there when you fall."', "there"),
        c('"If you get it wrong, you die. You knew that when you agreed."', "knew")),
    n("there", "conversant", '''"You'd better be." {n}She turns back to the city.{/n} "I've never trusted anyone to be where they said they'd be. Not Hosilla. Not him. Not the tribe." {n}A long breath.{/n} "I'm not going to start now. I'm just going to fall, and see."''',
        c("Continue", flags=(W + "nerves.promised",))),
    n("knew", "conversant", '''{n}She laughs, raw and short, and there is real relief in it.{/n}
"Yes. Good. That's what I needed to hear. Not a promise; uplanders make promises the way they make water." {n}She stands, and stretches, and wipes the last of the black off her face.{/n} "If I get it wrong I die, and it was my mistake, and nobody owes me anything. That I can do. That's just hunting."''',
        c("Continue", flags=(W + "nerves.hunting",))),
], requires=("trickster", "wenduag.traitor", BOUGHT), forbids=(W + "traitor.nerves", "wenduag.abyss_fell"), last=4,
    Relationship=REL, Chapters=[4], AnswerLists=["9bad7ea452d30254997b153473954cc1"], NativeReturnCue="daeb0e0796521c042bdd6baebbce7ade"))
tag(W + "traitor.nerves", "T")

visit(W + "court.neathers", "The weak get eaten", [
    nar("start", '''{n}She takes you down to the cellars in the middle of the afternoon and stops at the mouth of the furthest one without going in.{/n}
{n}There is an old neather lying on a pile of straw inside: a man with a grey muzzle and milky eyes and a cough that shakes his whole body. His ribs show. Beside him somebody has left a bowl of broth and a wooden cup of water, both untouched, and a spear with a cracked shaft that he will never throw again.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Old Tuhk. He was the best trapper in Neathholm when I was small. He taught me to set a snare." {n}Her voice is quite matter-of-fact.{/n} "Lung rot. He eats nothing and coughs on the little ones. Your chaplain says he can drive the sickness out. He wants Tuhk upstairs, away from the children, with a bed and someone to feed him. While the soldiers wait for those same beds." {n}She folds her arms.{/n} "Sull would keep handing him broth until we were all hungry. I know what a winter does to a hunter who cannot hunt." {n}Her lip curls.{/n} "I'd walk him down to the deep tunnels tonight and leave him there with his spear. Then the little ones eat his share. Your priest wants to spend soldiers' prayers on him instead. I\'ve carried his share down this stair every day. Tonight I\'d carry him down instead."''',
        c("Continue", "ask")),
    wd("ask", '''{n}She looks at you sideways.{/n} "The hunters down here do what I say now. I made them; it took three fights and a bitten ear. But they're in your city, under your roof, and your chaplains come down here sometimes with their bread and their prayers." {n}Her yellow eyes are steady.{/n} "So I'm asking. I'm asking you, because I'm yours. Tonight I walk him down the oldest stair, past my cairn, and leave him in the dark with his spear. Or I don't. Say which."''',
        c('"Do it. It\'s your tribe, and your arithmetic."', "cull", alignment=("Evil", 1)),
        c('"No. Nobody gets left in the dark to die in my city."', "forbid"),
        c('"Take him up to the chaplains\' infirmary. Tonight. I\'ll pay for his bed."', "infirmary", alignment=("Good", 1),
          crusade=("Finances", -100))),
    wd("cull", '''{n}She nods, as if you had confirmed a sum.{/n}
"Yes." {n}Then, lower:{/n} "Nobody ever said *do it* to me out loud before, so that somebody else carried half." {n}She goes into the cellar and crouches beside him, and says something in the neather tongue that makes him stop coughing and turn his milky eyes toward her, and she puts the cracked spear in his hands, and helps him up.{/n}
{n}You do not go down the oldest stair with them that night. In the morning the straw in the furthest cellar is gone, and the bowl and the cup are washed and put away, and nobody in the cellars says anything about it, to you or to each other.{/n}''',
        c("Continue", flags=(W + "neathers.culled",))),
    wd("forbid", '''"Then you come down here when he coughs. You don't get to say no and forget him." {n}Her fingers tighten around the cracked spear.{/n} "I'll move the children to the next cellar. Your chaplain can try his prayer down here when he comes with the bread. But I'm not carrying Tuhk up past your soldiers while you stand here giving orders." {n}She thrusts the spear back into the straw.{/n} "Your city. He stays."''',
        c("Continue", flags=(W + "neathers.forbidden",))),
    wd("infirmary", '''"A bed from the war chest. For him." {n}Wenduag looks from Tuhk\'s cracked spear to the stair.{/n} "Your chaplains will scrub him and pray over him. He\'ll hate that." {n}She crouches beside the straw.{/n} "Let the priest drive the rot out first. A dry bed won't do that. I'll watch him try." {n}She lifts him; he coughs against her shoulder.{/n} "I\'ll carry him. Tell the priest to save his sermon."''',
        c("Continue", flags=(W + "neathers.infirmary",))),
], requires=(COMMITTED,), optional=True)

visit(W + "court.hunt", "Outside the south postern", [
    nar("start", '''{n}"Leave your boots," she says, at the south postern, an hour after midnight. "And the sword. And that." She taps the badge of rank on your chest. "Hares can't read, but they can hear it jingle."{/n}
{n}Outside the walls the land is black and silver under a thin moon, broken hills and the burnt stumps of old orchards and, far off to the north, the dull red smear on the clouds where the Worldwound lies. She goes ahead of you with a spear and no light at all, and you follow her by the pale of her shirt, barefoot on cold ground.{/n}''',
        c("Continue", "quiet")),
    wd("quiet", '''{n}She stops so suddenly that you nearly walk into her, and puts a hand flat on your chest without looking round.{/n}
"You breathe like a smith's bellows." {n}Her whisper barely carries.{/n} "In through the nose. Slow. Let it out through your teeth. Put your heel down first, then roll. Don't look at the hare. Look next to it. Things know when they're looked at."''',
        c('[Do exactly as she says, and move with her.]', check=dict(Skill="SkillStealth", DC=20, Success="kill", Failure="blunder")),
        c('[Read the ground instead: the runs, the droppings, the wind.]', check=dict(Skill="SkillLoreNature", DC=20, Success="kill", Failure="blunder"))),
    nar("kill", '''{n}For a long stretch of the night you are nothing but feet and breath, and the ground under you, and her shape ahead. Then her arm comes up. Ten paces off, at the edge of a stand of thorn, something the size of a small dog lifts its head: not a hare. A deer, a young one, thin from a hard year.{/n}
{n}She does not throw. She looks at you, and holds out the spear.{/n}''',
        c('[Take the spear, and throw.]', "thrown"),
        c('[Push it back into her hands.]', "hers")),
    nar("blunder", '''{n}You do everything she says. Your heel still comes down on a dry stick with a crack like a snapped bone, and forty paces off, at the edge of a stand of thorn, a young deer you had not even seen goes bounding away into the dark.{/n}
{n}She turns her head and looks at you. You cannot see her face, but you can feel her grin.{/n}''',
        c("Continue", "blunder_her")),
    wd("blunder_her", '''"I heard that stick from here. So did supper." {n}She catches your wrist and draws you onward.{/n} "Step where I step. Unless you want me dragging you through the thorn."''',
        c("Continue", "hers")),
    nar("thrown", '''{n}The throw is not a good one. It goes in behind the shoulder, too far back, and the deer screams and runs, and she is already gone after it, flat out, low to the ground, faster than you have ever seen anything on two legs move. By the time you catch up she has it down in the thorn with her knife in its throat and her knee on its neck, and she is laughing.{/n}''',
        c("Continue", "eat")),
    nar("hers", '''{n}She throws from where she stands, without seeming to aim. The spear takes the deer through the heart and it drops where it stood, without a sound, and does not kick.{/n}
{n}She walks up to it unhurried, and kneels, and pulls the spear free, and opens its chest with her knife in three strokes.{/n}''',
        c("Continue", "eat")),
    wd("eat", '''{n}She cuts the heart out while it is still warm and holds it in both hands, steaming in the cold, and bites into it, and holds it out to you, with blood running down her chin.{/n}
"I made the kill. I get the first bite. Here. You were there." {n}Her teeth are black in the moonlight.{/n} "Go on. You were there."''',
        c('[Eat.]', "ate"),
        c('"Not raw."', "not_raw")),
    wd("ate", '''{n}It is hot and slick and tastes of iron and something wild, and it is not like anything you have eaten before. She watches you eat it with an expression you have never seen on her: not triumph, not mockery. Something closer to peace.{/n}
"There." {n}She sits back on her heels in the thorn with the deer between you and the red smear of the Wound behind her.{/n} "Now you've eaten with a neather. In the tunnels, that means something. Up here it just means you've got blood on your face." {n}She reaches over and wipes it off your chin with her thumb, and licks the thumb.{/n} "I like it better in the tunnels."''',
        c("Continue", flags=(W + "hunt.ate",))),
    wd("not_raw", '''"Uplanders." {n}She rolls her eyes and eats the rest herself, in four bites, and wipes her mouth on her sleeve.{/n} "All right. We'll cook the rest. There's a stupid little fire you can make that the demons won't see; I'll show you. You'll burn it, and I'll laugh." {n}She looks at you across the carcass, and her grin is very white.{/n} "You came, though. Barefoot, in the dark, without your sword. That's more than any of the others would have done."''',
        c("Continue", flags=(W + "hunt.cooked",))),
], requires=(GATE_SEEN,), optional=True)

visit(W + "court.gongs", "Counted in gongs", [
    nar("start", '''{n}You find her on the top of the citadel wall at the dead end of the night, sitting with her back to a merlon, listening. Down in the lower town a temple bell is telling the hour.{/n}''',
        c("Continue", "her")),
    wd("her", '''"In Neathholm there's a gong. The gong keeper strikes it twice a day, once to start the day and once to end it, because in the tunnels there's no sun to do it for him." {n}She tilts her head toward the bell.{/n} "That's the only thing I miss. Isn't that stupid? Not the tribe. Not the dark. The gong. I used to count my life in it. Thousands of gongs since my father went hunting and didn't come back."''',
        c("Continue", "father")),
    wd("father", '''"Rullo. Old Gorom. My father." {n}She counts them on her fingers.{/n} "The tribe said the tunnels took them. Savamelekh had them." {n}She tucks her hands beneath her knees.{/n} "You know about his children now. The little ones in Neathholm still wait for a hunter who isn\'t coming home. I used to sit by the gong and listen for my father\'s step behind it."''',
        c("Continue", "maze_chosen", requires=("wenduag.chosen",)),
        c("Continue", "maze_lann", forbids=("wenduag.chosen",))),
    wd("maze_chosen", '''"You know what I thought, in the Maze, the first time I saw you?" {n}She turns her head.{/n} "Lann was there, and me, and you had to choose. And I thought: *this one will choose Lann. Everyone chooses Lann. Lann is nice.*" {n}She laughs, softly.{/n} "And you chose me. The one who'd sold people to a demon for a piece of meat. You looked at both of us and you chose the one who bit." {n}She is not laughing now.{/n} "I've been trying to work out why ever since. I think I know, now. I think you saw what I'd do with it."''',
        c('"I did."', "saw"),
        c('"I chose the stronger one."', "stronger")),
    wd("maze_lann", '''"In the Maze, the first time, you had to choose between me and Lann." {n}She turns her head.{/n} "You chose Lann. Of course you did. Everyone chooses Lann. Lann is nice." {n}No bitterness in it; she says it the way she might say that water is wet.{/n} "And then, later, when you had the choice again, with my life in your hand, you chose me. Not the way anyone would think." {n}She looks at you for a long while.{/n} "I think that's the only choice that counted. The first one was just manners."''',
        c('"It was the only one that counted."', "saw"),
        c('"I chose the stronger one, the second time."', "stronger")),
    wd("saw", '''"Hosilla found a use for my teeth. Savamelekh found one for my blood." {n}She looks down toward the cellar stair.{/n} "Your sergeant found a word for all of me. He doesn\'t say it where I can hear him now." {n}She stands and catches your hand.{/n} "Come down. I want that mouth of yours busy before another bell starts."''',
        c("Continue", flags=(W + "gongs.saw",))),
    wd("stronger", '''{n}That pleases her. It pleases her enough that she laughs out loud, and a sentry further along the wall looks round and then pretends he hasn't.{/n}
"The stronger one. Yes. That's an honest answer. You chose the one who'd be useful to you, and you were right." {n}Her eyes narrow.{/n} "Are you still? Or am I only strong while I'm pointed at your enemies?" {n}She gets up.{/n} {n}She pulls you up by the hand and keeps hold of it.{/n} "Come down. You\'ve had enough watchmen listening to you tonight."''',
        c("Continue", flags=(W + "gongs.stronger",))),
], requires=(COMMITTED,), optional=True)


# --- 8. Reactions (named companions with a stake: Lann above all; Irabeth for the traitor in her city). ---------------------

SCENES.append(reaction("Lann", W + "react.lann_morning", ("trickster.ever", CAIRN_SEEN, LANN_IN),
    '''{n}Lann is waiting for you at the top of the cellar stair, leaning on the wall with his arms folded, the way you have seen him wait outside a tavern for a friend who is taking too long.{/n}
"You smell like her." {n}He says it without heat.{/n} "Every neather in the cellars can smell it. So can I." {n}He looks at you for a while, and his mouth works, and he gives up on whatever he was going to say and says something else.{/n} "I grew up with her. She was the best hunter in Neathholm and the worst friend, and she'd sell you to a demon for a leg of mutton and tell you about it afterwards so she could watch your face." {n}He pushes off the wall.{/n} "Just... when she does it to you, Commander, and she will, don't come and tell me. I already know how the story goes."''',
    answer_list=LANN_HUB, relationship=REL, entry='"You\'ve been waiting for me, Lann."', chapter=5, last=5, portrait="Lann",
    forbids=LANN_GONE + (CLOSED,), RequiresAnyGroups=[[LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN]],
    Chapters=[5]))
tag(W + "react.lann_morning", "T")

SCENES.append(reaction("Irabeth", W + "react.irabeth_traitor", ("trickster.ever", RETURNED, STREET_CAIRN, BRASK_KNOWS),
    '''{n}Irabeth closes the door of her office behind you before she says anything, which is how you know it is bad.{/n}
"The watch on the south gate is talking. A sergeant says he saw the traitor from the street breathing, and that the Commander buried her quiet. His captain laughed at him. I didn't." {n}She sits down.{/n} "And now my people tell me there's a neather woman hunting hares at night outside the south postern, who comes and goes through a gate that's supposed to be shut to her kind after dark." {n}Her voice is very even.{/n} "I'm the head of your security, Commander. I've seen what one traitor can do to an army. I'm not going to ask you what you've done. I'm going to tell you that if she so much as looks at one of my soldiers the wrong way, I'll hang her myself, and you can bury her properly the second time."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You wanted to see me, Irabeth?"', chapter=5, last=5, portrait="Irabeth",
    Chapters=[5], **IRABETH_GUARD))
tag(W + "react.irabeth_traitor", "T")
SCENES.append(reaction("Irabeth", W + "react.irabeth_suspicion", ("trickster.ever", RETURNED, STREET_CAIRN),
    '''{n}Irabeth closes the door of her office behind you before she says anything.{/n}
"The traitor from the street. You buried her yourself, the neather way, and nobody saw the body go into the ground but you." {n}She sits down.{/n} "And now my people tell me there's a neather woman hunting hares outside the south postern at night, who comes and goes through a gate that's shut to her kind after dark. Nobody can tell me her name. Nobody can tell me which cellar she sleeps in." {n}Her voice is very even.{/n} "I've seen what one traitor can do to an army, Commander. I'm noticing things nobody can explain. If that woman so much as looks at one of my soldiers the wrong way, I'll hang her, whoever she is."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You wanted to see me, Irabeth?"', chapter=5, last=5, portrait="Irabeth",
    Chapters=[5], forbids=("irabeth_dead", CLOSED, BRASK_KNOWS), ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"}))
tag(W + "react.irabeth_suspicion", "T")

SCENES.append(reaction("Regill", W + "react.regill_watch", ("trickster.ever", RETURNED, "regill.in_party"),
    '''{n}Regill does not look up from his ledger of punishments.{/n} "A traitor fell in your street, or in a demon's house, or in a Neathholm tunnel; I have not troubled to learn which. A traitor was buried by the Commander's own hand, without a tribunal. And there is now a neather in the cellars who eats raw hare, answers to no muster roll and comes and goes through gates that are shut to her kind." {n}He turns a page.{/n} "I do not ask whether these facts are connected. Asking would oblige me to act. I note, Commander, that a crusade which buries its traitors privately has a Commander who has decided the law is a private matter. I will be keeping my own account of where that leads. Its entries are short."''',
    answer_list="2366a8db6481070439fee222c0c52e45", relationship=REL, entry='"You have something to say, Regill."', chapter=5, last=5,
    portrait="Regill", forbids=("regill.dead", "regill.kicked_out", "regill.plot_absent", CLOSED), Chapters=[5]))
tag(W + "react.regill_watch", "T")


# --- 9. Epilogue pages (Owner WenduagEpilogue, Chapter 6; no effects; no page Requires another). ---------------------------

EPI = "WenduagEpilogue"
SAC = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})

COMMON = (
    p("{n}The Commander told Lann the truth before anyone in the cellars could. Lann stayed through the war and after. The confession kept this quarrel from swallowing their friendship. His people and the war still needed him. Lann never quite forgave the Commander.{/n}", requires=(LANN_PAID,), forbids=LANN_GONE),
    p("{n}A woman in the cellars told Lann that Wenduag lived. Lann asked the Commander and got the truth, late. Lann stayed through the war and after, but every doubtful answer brought another question. The Commander had to meet Lann's eyes while answering.{/n}", requires=(LANN_PAID_LATE,), forbids=LANN_GONE),
    p("{n}The Commander refused to tell Lann the truth about the cairn. Lann stayed and fought, but stopped making jokes in the Commander's hearing.{/n}", requires=(LANN_OWED,), forbids=LANN_GONE),
    p("{n}Lann asked the Commander for the truth about Wenduag. The Commander lied again, and Lann accepted the answer. Wenduag called it the Commander's lie, and refused to carry it.{/n}", requires=(LANN_LIED_AGAIN,), forbids=(W + "lann.disbelieved",) + LANN_GONE),
    p("{n}Lann asked the Commander for the truth about Wenduag. The Commander lied. Lann already knew Wenduag was alive. Lann stayed through the war, but never again believed the Commander about anything that mattered, and said so once, to the Commander's face.{/n}", requires=(W + "lann.disbelieved",), forbids=LANN_GONE),
    p("{n}Lann never learned that Wenduag lived. Whatever he believed about the cellar neathers' dead hunter, he kept it to himself, and did not go down to look.{/n}", requires=(LIED,), forbids=(LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, LANN_KNOWS, W + "lann.found_out", W + "lann.disbelieved") + LANN_GONE),
    p("{n}She carried the Commander's stroke in her side for the rest of her life: a long pale seam, low on the left, a finger's width from the place that would have ended her. She showed it to people she wanted to frighten. She never said who had put it there. She said she was saving the answer for the day she paid it back.{/n}", requires=(DEEP,)),
    p("{n}She kept the Commander's waterskin, the one that had been under her hand in the dark. She never drank from it again, and she never threw it away, and she never explained either.{/n}", requires=(WATER,)),
    p("{n}The flat stone with the Commander's mark scratched into its underside hung on a thong round her neck for the rest of the war. She called it a claim. Uplanders called it a necklace, and she said that was why uplanders were stupid.{/n}", requires=(MARK,)),
    p("{n}Savamelekh's stinger stayed with her, wrapped in sacking, for the rest of her life. She showed it to the young neathers of the cellars when they were old enough to understand, and told them what it was, and what it had cost, and what it had called, and that it did not call any more.{/n}", requires=(STINGER_GIVEN,)),
    p("{n}The Commander still owed her a death, a big one, as big as Savamelekh. She said she had picked it, and never said what it was. When the Commander asked which creature she meant, she smiled and sharpened her spear.{/n}", requires=(PROMISE_OWED,)),
    p("{n}Savamelekh's stinger went into a brazier in a Drezen cellar, and the smell of it hung about the place for a month. With its owner dead, nothing called the neathers who lived there in the night any more; she said the burning was only to make sure he left nothing behind.{/n}", requires=(STINGER_BURNED,)),
    p("{n}Whatever had become of Savamelekh, nobody had brought her his body. She went looking the spring after the Threshold, alone, with a spear and a knife and the Commander's promise, and came back in the autumn, and would not say what she had found.{/n}", requires=(DEATH_PROMISED,), forbids=(SAVA_DEAD,)),
    p("{n}Whatever had become of Savamelekh, nobody had brought her his body. She went looking the spring after the Threshold, alone, with a spear and a knife, and came back in the autumn, and would not say what she had found.{/n}", forbids=(SAVA_DEAD, DEATH_PROMISED)),
)

COMMON = COMMON + (
    p("{n}Lann did not see the end of the war at the Commander's side. Whatever had passed between them about the cairn went with him, and Wenduag never spoke of it.{/n}", requires=("lann.dead",), any_groups=((LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, LIED),)),
    p("{n}Lann did not see the end of the war at the Commander's side. Whatever had passed between them about the cairn went with him, and Wenduag never spoke of it.{/n}", requires=("lann.kicked_out",), forbids=("lann.dead",), any_groups=((LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN, LIED),)),
)

COMMITTED_PARAS = (
    p("{n}Sergeant Brask served out the war on the far wall of the lower town, as far from the cellar stair as Drezen allowed, and never again used the word *mongrel*. His hand healed crooked. He learned to salute with the other one.{/n}", requires=(GIVEN,)),
    p("{n}Sergeant Brask kept the south gate until the end of the war, and every neather who came through the postern after dark was let through with a nod. He never said her name again after that one time on his knees, but everyone who had heard him say it remembered, and so did he.{/n}", requires=(KNELT,)),
    p("{n}Sergeant Brask kept the south gate until the end of the war, with a thin white line across the back of his sword hand where every man who saluted him could see it. He never told anyone how he got it. He did not have to.{/n}", requires=(STRUCK,)),
    p("{n}Old Tuhk went down the oldest stair one night with his cracked spear in his hands, and did not come back up, and his share fed the cellars through the winter. The chaplain came looking for Tuhk the next day. Wenduag told him where she had left him; he went down with a lamp and returned without him. She never spoke of it again, but she never again asked the Commander for anything she could decide herself, either.{/n}", requires=(W + "neathers.culled",)),
    p("{n}The first prayer failed to lift Tuhk's sickness. Wenduag carried his cracked spear to the infirmary the next morning and stood beside the bed until the chaplain tried again. The cough broke. By spring he was setting snares in the citadel yard. She took half his catch and told him his bed had been expensive.{/n}", requires=(W + "neathers.infirmary",)),
    p("{n}Wenduag moved the children away from Tuhk's straw. The visiting chaplain drove out his sickness, but hunger had left him too weak to rise. The Commander came down with broth; Wenduag made sure of it. By spring he could sit beside a snare. She complained about every hare he failed to catch.{/n}", requires=(W + "neathers.forbidden",)),
    p("{n}Wenduag left a hare's head on Vellexia's pillow and a knife in her door. Vellexia returned both, pinning the head to Wenduag's bed. The next time the huntress followed her into a dark corridor, the succubus caught her wrist and pulled her close. \"You brought the knife. Must I do everything else?\" Wenduag laughed, drew the blade with her free hand and cut the clasp from Vellexia's gown. Vellexia caught that hand too. \"Better. Now put it away.\" Wenduag put the blade away and caught Vellexia by the waist. The succubus pulled her into the alcove, her open gown brushing the huntress's hands. Wenduag answered her kiss and drew her closer. Before dawn, the huntress returned to her den with the red ribbon between her teeth.{/n}", requires=(W + "vellexia.hunted", "participant.vellexia.available"), forbids=("vellexia.dead",)),
    p("{n}Under the Commander's roof, Wenduag kept her knife away from Vellexia. The succubus made a point of asking whether she had grown tame. Wenduag showed her the knife whenever the Commander was out of earshot.{/n}", requires=(W + "vellexia.left", "participant.vellexia.available"), forbids=("vellexia.dead",)),
    p("{n}Some nights, when the war let them, she took the Commander out through the south postern barefoot with a spear and no light, and they came back before dawn with blood on their chins and nothing to say to anyone.{/n}", any_groups=((W + "hunt.ate", W + "hunt.cooked"),)),
    p("{n}She never once used the Commander's name where anyone could hear, and she stopped saying *master* altogether. When she needed to call the Commander she whistled, her own whistle, one note up and one down, and the Commander came, and everybody who saw it pretended not to have.{/n}"),
    p("{n}Every so often she woke the Commander in the night with a knife at the throat and her knee on the breastbone, to see. The Commander never once lay there working out whether she meant it. She said that was how she knew.{/n}", any_groups=((W + "trial.won", W + "trial.tricked"),)),
    p("{n}Every so often she woke the Commander in the night with a knife at the throat and her knee on the breastbone, to see. The first time, the Commander had bled for it. The old white line on the Commander's forearm was the only scar she ever said she was proud of that she had not given herself.{/n}", requires=(BLED,)),
)

SCENES.append(scene(W + "epilogue.pack", "", EPI, 6, "", [
    nar("page", '''{n}Wenduag gathered a band among the cellar neathers. They followed her after three fights and a bitten ear. She fought where the fighting was worst, took what she could carry, and never pretended the crusade had made her merciful.{/n}
{n}She did not become a crusader. She did not learn to pray. She learned the names of the Commander\'s enemies, all of them, and wrote them nowhere, and forgot none.{/n}''',
        paragraphs=COMMITTED_PARAS + COMMON + (p("{n}Down at the bottom of the oldest stair, in the dark, there was a cairn with the head end loose. It was hers. The Commander was the only uplander who ever knew where it was, and the only one she ever took there.{/n}", requires=(CAIRN_SEEN,)),))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice", Q3_KILLED, Q3_SENT, HELLO_SENT, HELLO_ATTACKED), last=6, Relationship=REL, **SAC))
tag(W + "epilogue.pack", "T")

SCENES.append(scene(W + "epilogue.unclaimed", "", EPI, 6, "", [
    nar("page", '''{n}The war ended before Wenduag had caught anything worth laying at the Commander's feet. She said so herself, sourly, to anyone who asked: the good prey had all been killed by other people.{/n}
{n}She stayed in the cellars under the citadel with the neathers, all the same. She hunted outside the south postern at night and came back with hares and once with a deer, and fought in the Commander's war where the fighting was worst, and was the Commander's in every way that mattered to her except the one she had not yet decided to ask for.{/n}
{n}The spring after the Threshold, she caught something. What it was, and whose feet she dropped it at, and what they did with it, belongs to the years after the war.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", STARTED), forbids=(COMMITTED, CLOSED, "sacrifice", Q3_KILLED, Q3_SENT, HELLO_SENT, HELLO_ATTACKED),
    last=6, Relationship=REL, **SAC))
tag(W + "epilogue.unclaimed", "T")

SCENES.append(scene(W + "epilogue.dead", "", EPI, 6, "", [
    nar("page", '''{n}Wenduag of Neathholm stayed dead. The Commander had said so, once, in the dark, and she had taken the Commander at the word.{/n}
{n}The neathers in the cellars of Drezen told a story for years afterwards about a dead hunter who lived at the bottom of the oldest stair, and ate raw hare, and came out on moonless nights to walk the walls of the city that had buried her. Children were told that if they were very weak, or very stupid, she would come for them. The children of the neathers grew up very strong, and not at all stupid.{/n}
{n}Nobody ever found her cairn. The Commander never looked.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", CLOSED, STAY_DEAD), RequiresAnyGroups=[[CAIRN, ABYSS_CAIRN, STREET_CAIRN]], forbids=(COMMITTED, "sacrifice"),
    last=6, Relationship=REL, **SAC))
tag(W + "epilogue.dead", "T")

SCENES.append(scene(W + "epilogue.refused", "", EPI, 6, "", [
    nar("page", '''{n}Wenduag brought the Commander the best thing she had caught, once, and the Commander set it on its feet and sent it back to its gate. She did not ask again. She had never asked anybody before; she said afterwards that she now understood why.{/n}
{n}She fought the rest of the war where the fighting was worst, because she was not stupid, and she kept to the cellars and the dark between battles, and the neathers there learned not to say the Commander's name in her hearing. When the war ended she was gone before the banners came down, with a band of her own, east, toward the edge of the Wound, where there was still something worth hunting.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", CLOSED, W + "court.claim_refused"), forbids=(COMMITTED, STAY_DEAD, "sacrifice"), last=6, Relationship=REL, **SAC))
tag(W + "epilogue.refused", "T")


# Reviewed polish P06/P08/P12 and HEAT: authored history selectors, before native-visit cloning.
# These receipts distinguish performed acts; they add no eligibility, payment or check.
ORCHARD = W + "orchard_return"

def _polish_scene(suffix):
    return next(item for item in SCENES if item["Id"] == W + suffix)

def _polish_node(item, id):
    return next(node for node in item["Nodes"] if node["Id"] == id)

def _polish_origin(item, source, target, text):
    original = _polish_node(item, source)
    variant = copy.deepcopy(original)
    variant.update(Id=target, Text=text)
    item["Nodes"].append(variant)
    for node in item["Nodes"][:-1]:
        for answer in list(node["Choices"]):
            if answer.get("Next") == source:
                alternate = copy.deepcopy(answer)
                answer.setdefault("Forbids", []).append(ORCHARD)
                alternate["Next"] = target
                alternate.setdefault("Requires", []).append(ORCHARD)
                node["Choices"].append(alternate)

_polish_origin(_polish_scene("court.trial"), "which_back", "which_orchard", '"You came into my orchards alone. No guards. No sword at my back." {n}Her knee presses harder against your chest.{/n} "Tonight you\'re inside your walls. Let\'s see if that makes you careless."')
_polish_origin(_polish_scene("court.cairn"), "own_built", "own_orchard", '"I carried these down after I came back through your gate. Every one." {n}She presses your hand against a rough edge.{/n} "If I ever need a grave, I won\'t have your sergeant choosing it."')
_polish_origin(_polish_scene("court.stinger"), "plain", "plain_orchard", '"He\'s dead." {n}She smells the spike without touching it.{/n} "I spent long enough hunting hares outside your walls. I wanted him." {n}Her fingers tighten on the sacking.{/n} "You could have brought me something with a throat left to cut."')

_trial = _polish_scene("court.trial")
_start = _polish_node(_trial, "start")
_start["Choices"][0].setdefault("Forbids", []).append(Q3_BETRAYED)
_start["Choices"].extend([
    c("Continue", "her", requires=(Q3_BETRAYED,), forbids=(Q3_SPARED,)),
    c("Continue", "reckoning_select", requires=(Q3_BETRAYED, Q3_SPARED)),
])
_trial["Nodes"].extend([
    nar("reckoning_select", "{n}Her knife stays flat against your throat. She watches your eyes.{/n}",
        c("Continue", "reckoning_bought", requires=(BOUGHT,)),
        c("Continue", "reckoning", forbids=(BOUGHT,))),
    wd("reckoning_bought", '"You made your offer. I took it. Then I took his, too." {n}She shows her teeth.{/n} "Don\'t call it a misunderstanding. I thought he would win."', c("Continue", "reckoning")),
    wd("reckoning", '"In his house, I chose him." {n}Her knife stays against your throat.{/n} "He looked stronger. I was wrong. You left me breathing after I tried to put you in the ground." {n}She leans closer.{/n} "I haven\'t forgotten that. Have you?"', c("Continue", "her")),
])

_cairn = _polish_scene("court.cairn")
_polish_node(_cairn, "knife")["Choices"][0]["Next"] = "knife_down"
_cairn["Nodes"].append(nar("knife_down", '{n}You lay the knife on the top stone. Her hands close over yours and pull them against her bare waist. Together you strip off the remaining clothes, dropping them beside the lamp. She catches your lower lip between her teeth as you draw her closer.{/n}', c("Continue", "cut")))

_regill = _polish_scene("react.regill_watch")
# E6 reactions are one-node only. This existing host uses the standard native dialogue contract.
_regill.pop("Reaction", None)
_start = _polish_node(_regill, "start")
_exit = copy.deepcopy(_start["Choices"][0])
_start["Text"] = "{n}Regill closes his ledger. Three witness statements lie beside it.{/n}"
_start["Choices"][0].update(Next="neathholm", Requires=[CAIRN])
_start["Choices"].extend([
    c("Continue", "abyss", requires=(ABYSS_CAIRN,), forbids=(CAIRN,)),
    c("Continue", "street", requires=(STREET_CAIRN,), forbids=(CAIRN, ABYSS_CAIRN)),
])
for _id, _location in (
    ("neathholm", "Lann reported Wenduag dead in Neathholm. You undertook the burial."),
    ("abyss", "Wenduag was reported dead in Savamelekh's house. You disposed of the body."),
    ("street", "Wenduag fell in the Drezen ambush. You took the body into the catacombs."),
):
    _regill["Nodes"].append(n(_id, "Regill", '"' + _location + '" ' + '"The grave was not inspected. A neather answering her description now passes through the south gate without appearing on the muster roll." {n}He rests one finger on the ledger.{/n} "I have witnesses. I have not accepted their conclusion. If she turns your soldiers against you, I will act. A private burial will not settle the matter twice."',
        copy.deepcopy(_exit), portrait="Regill"))
# E-Q8-02 appends the existing burial group below. Echo integration removes that group only.

# Paid/witness outcomes are exclusive in the ending even in overlapping saved histories.
_lann_priority = (W + "lann.disbelieved", LANN_LIED_AGAIN, LANN_OWED, LANN_PAID_LATE, LANN_PAID)
for _paragraph in COMMON:
    for _rank, _receipt in enumerate(_lann_priority):
        if _receipt in _paragraph["Requires"]:
            _paragraph["Forbids"] = list(dict.fromkeys(_paragraph["Forbids"] + list(_lann_priority[:_rank])))
            break


# Round 2 situation work precedes native-hub cloning; saved nodes/answers remain.
_reckoning = _polish_node(_trial, "reckoning")
_reckoning["Choices"][0].update(Text='"I spared you to fight him, not to pretend you kept your word. Show me what you choose now."', Next="reckoning_answer")
_trial["Nodes"].append(wd("reckoning_answer", '"Then watch. I took his offer because I wanted what he fed me. '
    'You left me alive after I lost. I want to know what you do when I come at you with my own knife." '
    '{n}She shifts her knee off your ribs, leaving you room to move.{/n}', c("Continue", "her")))

_stinger = _polish_scene("court.stinger")
_take = _polish_node(_stinger, "take")
_take["Choices"][0]["Forbids"].append(DEATH_PROMISED)
_take["Choices"].append(c("Continue", "tail_debt", requires=(DEATH_PROMISED,), flags=(STINGER_GIVEN,)))
_stinger["Nodes"].append(wd("tail_debt",
    '"The tail is mine now. You still owe me what you promised. I wanted my knife in him." '
    '{n}She tucks the wrapped stinger beneath her arm.{/n} "I will pick something else. Something big."',
    c("Continue", flags=(PROMISE_OWED,))))

_morning = _polish_scene("court.morning")
for _index, _target in enumerate(("stone_shown", "stone_kept")):
    _polish_node(_morning, "end")["Choices"][_index]["Next"] = _target
_morning["Nodes"].extend([
    wd("stone_shown", '{n}She pushes the pot toward you, then turns the stone under one finger.{/n} '
       '"From my cairn. I cut it while you slept." {n}She puts it back in your palm and closes your fingers over it.{/n} '
       '"Keep it. I came back with supper, not to ask for it. Eat before I finish yours too."', c("Continue")),
    wd("stone_kept", '{n}Her hand slips into your pocket and finds the stone. She leaves it there.{/n} '
       '"Good. You haven\'t traded it for another medal." {n}She pulls you down beside her and pushes the pot between you.{/n} '
       '"A hare. No sergeant tonight. Eat."', c("Continue")),
])

_yaniel = _polish_scene("court.yaniel")
for _answer in _polish_node(_yaniel, "start")["Choices"]:
    _answer["Forbids"].append("yaniel.trickster.returned")
_polish_node(_yaniel, "start")["Choices"].append(c("Continue", "returned_yaniel", requires=("yaniel.trickster.returned",)))
_yaniel["Nodes"].extend([
    wd("returned_yaniel", '"The paladin lives again. You killed her and then brought her back." '
       '{n}She tilts her head.{/n} "Even after what we said about her. She could still take your knights from you. '
       'You must want her sword very badly."',
       c('"We need her against the demons. I answered for what I did."', "returned_answer"),
       c('"I can stand having someone strong beside me."', "returned_answer")),
    wd("returned_answer", '"Beside you. Until she chooses differently." {n}Her fingers close on your sleeve.{/n} '
       '"I\'ll watch her. If she bites you, I want to see."', c("Continue", flags=(W + "yaniel.watched",))),
])
# A prior early discussion may suppress its repeat, but must not suppress changed news.
_yaniel["ForbidOverrides"] = {W + "early.yaniel": "yaniel.trickster.returned"}
_polish_node(_polish_scene("court.vellexia"), "hunt")["Text"] = (
    '"Nobody dies. You\'re no fun." {n}She slides off the parapet, watching the window.{/n} '
    '"A hare\'s head on her pillow. My knife in her door. Let\'s see what she sends back." '
    '{n}Up above, Vellexia opens the shutters. She drops a red ribbon; Wenduag catches it.{/n} '
    '"If you insist on skulking beneath my window, huntress, bring something better than vermin." '
    '{n}Wenduag winds the ribbon around her fist.{/n} "She saw. Good."')
_polish_node(_polish_scene("epilogue.pack"), "page")["Text"] += (
    '\n{n}After a long hunt she came back through the south postern with food over her shoulder. '
    'She found the Commander at the maps, took the chair beside them and put her bloody hand on the table. '
    '"Move the Wound. Supper goes here."{/n}')

# --- Registration -------------------------------------------------------------------------------------------------------------

def integrate(payload):
    """The Last Call partner key (committed here, or the native romance kept to the end) and her presence; wenduag_trickster
    binds the rest."""
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)
    for key, groups in _DERIVED_EXTRA.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    from storylines import wenduag_echo
    wenduag_echo.integrate(payload)
    _round2_slots(payload)

# eng7-l08: E-Q7-17 / wenduag:048,053. The cited visits use the
# existing Wenduag actor and hub instead of consuming more rest pages.
# Her copy stays at that same place for the post-commit visits, and is also
# available in Chapter 3 for the already-earned cellar visit. No return,
# payment, refusal, native-romance or commitment conditions change.
_delivery_visits = {
    W + "court." + name for name in
    ("trial", "gate", "stinger", "cairn", "morning", "vellexia", "yaniel",
     "neathers", "hunt", "gongs")
}
for _delivery_scene in SCENES:
    if _delivery_scene["Id"] in _delivery_visits or _delivery_scene["Id"] == W + "killed.cellar":
        _delivery_scene.pop("Remote", None)
        _delivery_scene.pop("Kind", None)
        _delivery_scene["ContactUnit"] = UNIT
        _delivery_scene["InteractionHub"] = PRESENCE
        _delivery_scene["AnswerLists"] = []
        _delivery_scene["Entry"] = _delivery_scene["Title"]
PRESENCES[PRESENCE]["MinChapter"] = 3
PRESENCES[PRESENCE]["Forbids"] = [f for f in PRESENCES[PRESENCE]["Forbids"] if f != COMMITTED]
# end eng7-l08

# eng7-l08: the same visits on a recruited native Wenduag use her verified three native
# hubs. Keep the presence and native-list contracts separate (Rules validates
# them separately); both variants record the original completion ID.
for _delivery_source in list(SCENES):
    if _delivery_source["Id"] not in _delivery_visits:
        continue
    _native_visit = copy.deepcopy(_delivery_source)
    _native_visit["Id"] = _delivery_source["Id"] + ".native_visit"
    _native_visit.pop("ContactUnit", None)
    _native_visit.pop("InteractionHub", None)
    _native_visit["AnswerLists"] = list(HUB_LISTS)
    _native_visit["Requires"].append(IN_PARTY)
    if _delivery_source["Id"] not in _native_visit["Forbids"]:
        _native_visit["Forbids"].append(_delivery_source["Id"])
    for _delivery_node in _native_visit["Nodes"]:
        for _delivery_answer in _delivery_node["Choices"]:
            if not _delivery_answer.get("Next") and not _delivery_answer.get("Check") and not _delivery_answer.get("Abort"):
                if _delivery_source["Id"] not in _delivery_answer.setdefault("Set", []):
                    _delivery_answer["Set"].append(_delivery_source["Id"])
    SCENES.append(_native_visit)
# end eng7-l08

# eng8-q8b begin: E-Q8-02 applies at entry, including every native hub twin.
_current_survival = {W + name for name in (
    "killed.cellar", "epilogue.pack", "epilogue.unclaimed", "epilogue.dead", "epilogue.refused",
    "react.regill_watch", "react.lann_morning",
    "react.irabeth_traitor", "react.irabeth_suspicion")}
for _consumer in SCENES:
    if _consumer["Id"].startswith(W + "court.") or _consumer["Id"] in _current_survival:
        _consumer["Requires"] = list(dict.fromkeys([*_consumer.get("Requires", []), "trickster.now"]))
    if _consumer["Id"] == W + "react.lann_morning":
        _consumer["Requires"] = list(dict.fromkeys([*_consumer["Requires"], WITH_YOU]))
    if _consumer["Id"] == W + "react.regill_watch":
        _consumer.setdefault("RequiresAnyGroups", []).append([CAIRN, ABYSS_CAIRN, STREET_CAIRN])
    # L13 already serialized these answer indices. Entry power must not make
    # its generator omit the old off-path leave answers on a regenerated save.
    if _consumer["Id"] in (W + "court.claim", W + "court.claim_in_person"):
        for _node in _consumer["Nodes"]:
            if _node["Id"] in ("after_given", "after_knelt", "after_struck"):
                _answer = _node["Choices"][0]
                _answer["Requires"] = list(dict.fromkeys([*_answer.get("Requires", []), "trickster.now"]))
                _node["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
# eng8-q8b end


def _round2_slots(payload):
    """Authored reserved passages; legacy terminal answers still own completion."""
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    # These old native-hub answers used to terminate before the new stone reply.
    # Keep their original primary-completion effects at the same saved indices.
    morning = scenes[W + "court.morning.native_visit"]
    for answer in _polish_node(morning, "end")["Choices"][:2]:
        if W + "court.morning" not in answer["Set"]:
            answer["Set"].append(W + "court.morning")
    for twin in ("", ".native_visit"):
        cairn = scenes[W + "court.cairn" + twin]
        slot = cairn["Id"] + ".explicit.1"
        for node in cairn["Nodes"]:
            for answer in node["Choices"]:
                if answer.get("Next") in ("cut", "cut_echo"):
                    answer["Next"] = slot
        # EXPLICIT SLOT: chosen first night on her cairn; knife down, lamp out.
        cairn["Nodes"].append(wd(slot,
            '{n}She drags you close by the hips. You kiss her back; her breath catches and she bears you down against the stones. '
            'Your hands find her bare hips. She draws you between her knees and pulls you into another kiss. '
            'Above the stair, the watch bell sounds.{/n}',
            c("Continue", "cut", forbids=(W + "echo.abyss.returned",)),
            *([c("Continue", "cut_echo", requires=(W + "echo.abyss.returned",))]
              if any(node["Id"] == "cut_echo" for node in cairn["Nodes"]) else [])))
        _polish_node(cairn, "cut")["Text"] = ('{n}Afterward she lies against you on the cold stone, your coat over both of you. '
            'When you shift, her fingers tighten on your wrist.{/n} "Not yet. The maps can wait."')
        if any(node["Id"] == "cut_echo" for node in cairn["Nodes"]):
            _polish_node(cairn, "cut_echo")["Text"] = ('{n}Afterward her hand finds yours in the dark and holds it against the stones.{/n} '
            '"Caught." {n}She laughs into your neck and stays there.{/n}')
        gongs = scenes[W + "court.gongs" + twin]
        slot = gongs["Id"] + ".explicit.1"
        for id in ("saw", "stronger"):
            terminal = _polish_node(gongs, id)["Choices"][0]
            terminal["Forbids"].append(CAIRN_SEEN)
            successor = copy.deepcopy(terminal)
            successor["Forbids"].remove(CAIRN_SEEN)
            successor["Requires"].append(CAIRN_SEEN)
            successor["Next"] = slot
            # Completion is still delivered by the slot's outgoing answer.
            successor["Set"] = [flag for flag in successor["Set"] if flag != W + "court.gongs"]
            _polish_node(gongs, id)["Choices"].append(successor)
        # EXPLICIT SLOT: later return down the stair; no repeated first night.
        completion = (W + "court.gongs",) if twin else ()
        gongs["Nodes"].append(wd(slot,
            '{n}She leads you off the wall, past the sentry carrying fresh arrows, and down the back stair. '
            'At its foot she pushes you against the stone and kisses you. Your hands find her waist; she catches them and pulls you onward.{/n} '
            '"You know the way now. Hurry." {n}When the watch changes, she is still beside you.{/n}',
            c("Continue", flags=completion)))
