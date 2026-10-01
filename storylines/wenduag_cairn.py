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
from storylines.wenduag_trickster import (ABYSS_CAIRN, BARE, BOTH, BOUGHT, BRASK_KNOWS, BRASK_MET, CAIRN, CLOSED, COMMITTED,
                                          DEEP, DREZEN, GATE_SEEN, IN_PARTY, KILLED, LANN_GONE, LANN_HUB, LANN_IN, LANN_KNOWS,
                                          LANN_LIED_AGAIN, LANN_OWED, LANN_PAID, LANN_PAID_LATE, LATE, LIED, MARK, NATIVE,
                                          PROVED, Q3_BETRAYED, Q3_LOYAL, Q3_SPARED, REDEEMED, REL, RETURNED, SAVA_DEAD,
                                          SCENES as _DEVICE_SCENES, STARTED, STREET_CAIRN, W, WATCH, WATER, WITH_YOU,
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
    wd("her", '''"Weak things die in their sleep." {n}Wenduag's voice is very soft, and very close. She smells of the cellars and of raw meat.{/n} "Hosilla used to say that, in the Maze, to the ones who came to her hungry. Then she'd come round in the night and prove it. I learned to sleep with one eye open. The ones who didn't, Savamelekh ate." {n}The knee presses a little harder.{/n}''',
        c("Continue", "which_back", requires=(RETURNED,)),
        c("Continue", "which_kept", forbids=(RETURNED,))),
    wd("which_back", '''"You put me under stones, {mf|master|mistress}, and I dug. Now it's your turn. Are you a weak thing?"''',
        c("Continue", "which")),
    wd("which_kept", '''{n}She shifts her weight, and the knife slides a finger's width along your neck without cutting.{/n} "You kept me. You looked Savamelekh's offer in the eye and made a better one, or you stood over me when I'd earned my death and didn't give it to me. Everybody in this citadel thinks that makes you soft." {n}Her breath is warm on your ear.{/n} "I want to know if they're right. Show me."''',
        c("Continue", "which")),
    nar("which", '''{n}Her weight is on your breastbone and her knife is on your throat, and she is waiting, perfectly still, to see what you do.{/n}''',
        c('[Heave her off you and roll clear.]', check=dict(Skill="SkillAthletics", DC=26, Success="won", Failure="lost")),
        c('"Get off me, or finish it. You won\'t get a second try."', check=dict(Skill="CheckIntimidate", DC=26, Success="won_word", Failure="lost")),
        c('"Wait. You\'ve got a stain on your cuff."', "stain", mythic="Trickster")),
    nar("won", '''{n}You surge up under her with everything you have, hips and shoulders and both hands, and she goes over sideways off the map table, taking half the Worldwound with her, and hits the floor with a sound like a sack of kindling. By the time she is up on her haunches you are standing, with your own knife out.{/n}''',
        c("Continue", "won_her")),
    wd("won_her", '''{n}She stays crouched on the floor among the scattered maps and laughs up at you, with blood on her teeth where she bit her lip.{/n}
"Good. Good! You didn't think about it. You just moved." {n}She wipes her mouth with the back of her wrist and looks at the red on it with satisfaction.{/n} "The ones who think about it die. They lie there working out whether I mean it, and I do." {n}She springs up.{/n} "Again, one day. When you're not expecting it. That's the only kind of again there is."''',
        c("Continue", flags=(PROVED, WON, STARTED))),
    wd("won_word", '''{n}There is a long silence. The knife does not move. Then, very slowly, the weight comes off your chest, and she sits back on her heels on the edge of the table, and looks at you with her head on one side.{/n}
"You meant that." {n}She sounds pleased and a little surprised, the way a hunter sounds when a deer turns and lowers its antlers.{/n} "You'd have let me cut, and killed me with the blood still coming out of you. I could hear it in your voice." {n}She sheathes the knife.{/n} "Most people beg, with a knife on their throat. Or they pray. You threatened me." {n}She grins.{/n} "Good."''',
        c("Continue", flags=(PROVED, WON, STARTED))),
    nar("stain", '''{n}She looks.{/n}
{n}She doesn't look. She laughs, low, delighted, right against your ear.{/n} "The stain on the cuff. Hosilla tried that on me when I was seven. I took two of her fingers for it."
{n}She is so pleased with the old trick that she leans back to grin at you, half a finger's width, and lifts the knife a hair off your throat to do it. That is all you needed. Since your first night in this citadel you have slept over these maps with your own dagger under the Worldwound, a hand's breadth from your fingers; Commanders who sleep without one do not stay Commanders long. While she laughed at the cuff, your hand found it. When her grin comes back down, the point is resting under her breastbone.{/n}''',
        c("Continue", "stain_her")),
    wd("stain_her", '''"...Cheat." {n}She goes very still on top of you, with her knife at your throat and yours under her heart. Her eyes are wide.{/n} "You said the stupid thing so I'd laugh at it." {n}And then she is grinning, all her teeth.{/n} "Filthy, clever cheat. You knew I'd know it. You wanted me to know it." {n}She laughs, and the laugh pushes her chest against your point, and she does not seem to care.{/n} "Hosilla would say that's not a fight. Hosilla is dead. Fighting is the meaning of life, {mf|master|mistress}. Cheating is how you win it."''',
        c("[Put your dagger back under the maps.]", flags=(PROVED, TRICKED, STARTED))),
    nar("lost", '''{n}You heave, or you snarl, and it is not enough. She rides the heave the way you would ride a bucking mule, and her knee sinks into your chest until the ribs creak, and the edge of the knife turns, and draws.{/n}
{n}Not your throat. Your forearm, which you have thrown up without thinking: a long, shallow, deliberate cut from the wrist toward the elbow, neat as a tailor's seam.{/n}''',
        c("Continue", "lost_her")),
    wd("lost_her", '''{n}She watches it bleed with great interest.{/n} "You bleed well." {n}Her voice is thoughtful.{/n} "Lots of uplanders don't. They go white and fall over. You just looked at it." {n}She lifts the knife away and sits back on her heels, and licks the edge, once, the way you might taste a sauce.{/n} "Not strong enough tonight. But you didn't beg, and you didn't call for your guards." {n}She slides off the table.{/n} "That's something. Fine. You'll do." {n}At the door she looks back.{/n} "Get somebody to sew that. I'd do it, but I'd enjoy it too much."''',
        c("Continue", flags=(PROVED, BLED, STARTED))),
], forbids=(PROVED,), delay=24)


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
    nar("struck", '''{n}You walk up behind Sergeant Brask and tap him on the shoulder, and when he turns round, surprised, with the grin still half on his face, you break his nose with your fist.{/n}
{n}It makes a sound like a green stick. He sits down hard in the road in his new coat, with blood running over his mouth, and stares up at you. None of his men moves. None of them is going to.{/n}
{n}Behind you, very softly, Wenduag laughs.{/n}''',
        c("Continue", "after_struck")),
    wd("after_struck", '''{n}She walks through the postern past the sitting sergeant, and on the far side she stops and looks at your hand, at the split knuckles.{/n}
"You did it yourself." {n}She takes your hand in both of hers and turns it over, and looks at the blood on it, his blood, and then at you.{/n} "Not a guard. Not an order. Your own hand." {n}Her thumb goes over the split skin, not gently.{/n} "In the caves, that's what a chief does when someone bites one of hers. He doesn't send somebody. He goes." {n}She lets go.{/n} "His men will all be afraid of you now. And they'll hate me for it." {n}She grins.{/n} "Good. I like being hated for good reasons."''',
        c("Continue", flags=(GATE_SEEN, GATE_STRUCK))),
    nar("rebuked", '''{n}Brask's grin widens. He steps aside for you with a flourish, and bows, and his men snigger.{/n}
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
        c("Continue", "promised", requires=(BOUGHT,)),
        c("Continue", "plain", forbids=(BOUGHT,))),
    wd("promised", '''"You promised me." {n}She looks up, and her eyes are hard as flint.{/n} "His death, at my hand. His stinger in my fist, cut off, not given. That was the bargain. That's what I fell down in front of his gang for." {n}She jabs a finger at the sacking.{/n} "And somebody else cut it."''',
        c('"And now it\'s in your fist. Take it. Nobody else in the world will ever hold it."', "take"),
        c('"I owe you his death. I don\'t have it to give. I\'m not going to pretend otherwise."', "owed")),
    wd("take", '''{n}She takes it. She holds it by the cut end, where it is safe, and turns it so the lamplight runs along it, and her face does something you have never seen it do: it goes very young, and very old, at the same time.{/n}
"My father ate this." {n}She says it to the stinger, not to you.{/n} "Every night for years. It made him strong, and then it made him his." {n}She wraps it back in its sacking with great care.{/n} "I'll keep it. When I'm old, if I'm ever old, I'll show it to the young ones and tell them what it is. That's better than killing him. Nearly."''',
        c("Continue", flags=(STINGER_GIVEN,))),
    wd("owed", '''"No. You don't." {n}She looks at you for a long time. Then, surprisingly, she nods.{/n}
"You didn't lie. You could have. You could have told me you held him down for me and I missed it." {n}She takes the stinger, sacking and all, and tucks it under her arm.{/n} "You owe me a death, {mf|master|mistress}. A good one. Something as big as him. I'll tell you when I've picked it." {n}Her teeth show.{/n} "Don't worry. It won't be anyone you like. Probably."''',
        c("Continue", flags=(STINGER_GIVEN, PROMISE_OWED))),
    wd("plain", '''"He's dead." {n}She lets out a long breath, and something in her shoulders comes down that you did not know was up.{/n} "I should have been there. It should have been my hand." {n}She looks at the stinger again.{/n} "But I was under your stones, or in your cellars, being dead. That's the price of dying, I suppose. You miss things."''',
        c('"It\'s yours. Take it."', "take"),
        c('[Throw it on the brazier.]', "burn")),
    wd("burn", '''{n}She does not stop you. She watches it go into the coals, and hiss, and blacken, and the smell that comes off it makes her gag and put her sleeve over her mouth. The black bead at the tip bursts with a small wet sound.{/n}
{n}When it is only a curl of ash she takes her sleeve away.{/n} "Good." {n}Her voice is rough.{/n} "Nobody should have that. Not even me. Especially not me." {n}She wipes her eyes, which are running from the smoke.{/n} "Don't tell anyone I said that."''',
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
    wd("why_knows", '''"He's been telling people he saw me breathing in the street. The captain laughed at him. The next one might not." {n}She nudges Brask with her toe, not hard, the way you nudge a sleeping dog.{/n} "So he's your problem too. But that's not why I brought him."''',
        c("Continue", "why")),
    wd("why", '''{n}She crouches beside him, easy on her heels, and looks up at you across his body.{/n}
"In the tunnels, when a hunter wants somebody, she doesn't bring them flowers. What would you do with flowers, underground? She brings them what she caught. The best thing she caught. And she puts it at their feet, and she waits to see what they do with it." {n}She puts a hand flat on Brask's heaving back.{/n} "If they eat it, they're hers. If they give it back to her, they're hers. If they kick it away, well." {n}She shrugs.{/n} "Then she knows."''',
        c("Continue", "want")),
    wd("want", '''"He called me mongrel bitch at your gate. He laughed at me with his men. He'd have put my head on a pole and brushed his coat under it." {n}Her voice is very steady.{/n} "And he's yours. One of your soldiers, in your city, under your law." {n}She stands.{/n} "So he's the best thing I could catch. Something of mine, that's also something of yours." {n}She folds her arms and waits.{/n} "Well. There he is."''',
        c('[Nudge him toward her with your boot.] "He\'s yours."', "given", alignment=("Evil", 1)),
        c('[Pull out his gag.] "On your knees, sergeant. Ask her pardon. Use her name."', "knelt", alignment=("Chaotic", 1)),
        c('[Take her knife off her belt, and do it yourself.]', "struck"),
        c('[Cut his bonds and set him on his feet.] "Get up, sergeant. Back to your gate."', "no")),
    wd("given", '''{n}She looks at you for a moment, very still. Then she smiles, slow and wide, until every one of her teeth is showing.{/n}
"Mine." {n}She hauls Brask up by the back of his collar, one-handed, as if he weighed nothing, and he makes a thin noise through his gag.{/n} "Don't worry, sergeant. I'm not going to kill you. Dead men forget. I want you to remember." {n}She drags him to the door and out, and it swings shut behind them.{/n}
{n}Whatever happens on the wall walk behind the south gate that night, the watch does not hear it, or says it did not. In the morning Brask is in the infirmary with two fingers of his sword hand broken and every button cut off his shirt, and he tells the chaplain he fell down the stairs, and he never, afterwards, says the word *mongrel* in anyone's hearing again.{/n}''',
        c("Continue", "after_given")),
    wd("after_given", '''{n}She comes back before midnight, with his blood under her nails and his last button in her fist, and drops it on your table.{/n}
"You gave him to me." {n}She sits on the table beside it.{/n} "You didn't pretend it was justice. You didn't tell me to be merciful. You just gave him to me, because I wanted him." {n}She looks at you.{/n} "That's how I know. Savamelekh fed me too, in the Maze. Good meat, more than the tribe ever gave me, and I was glad of it. But he fed me so I'd be his: every bite had his poison on it and a hook in it." {n}She rolls the button between her fingers.{/n} "You gave me one of yours and didn't tell me what to do with him. No hook. That's either very stupid or very strong." {n}She reaches out and puts her hand flat on your chest, over the heart, and presses, the way she pressed her knee there in the dark.{/n} "Now you're mine. I'm not asking."''',
        c("Continue", flags=YES + (GIVEN,))),
    n("knelt", "Sergeant Brask", '''{n}Brask spits out the rag and draws breath to shout, and sees your face, and does not. He gets his knees under him, awkwardly, with his hands still tied behind his back, and kneels there in his shirt on your floor with his nose dripping.{/n}
"I..." {n}He swallows.{/n} "I ask your pardon. Wenduag." {n}He looks at you.{/n} "Of Neathholm."''',
        c("Continue", "after_knelt")),
    wd("after_knelt", '''{n}She stares down at him. Then she begins to laugh, a helpless, whooping laugh that doubles her over and makes her hold on to the wall.{/n}
"Of Neathholm!" {n}She wipes her eyes.{/n} "Oh, that's worse than killing him. That's so much worse. He'll have to live with having said it." {n}She hauls him up by the collar and throws him out of the door, still tied, and you hear him go down the stairs on his knees.{/n}
{n}Then she turns to you, still grinning, with tears of laughter on her face.{/n} "You made him say my name. The whole name." {n}She comes close.{/n} "Nobody on the surface ever says it right. They say *the mongrel*, or *the Commander's dog*. You made one of them say it on his knees." {n}She takes your face in both hands, rough, and looks at it as if she had caught it.{/n} "You're mine now. I'm not asking."''',
        c("Continue", flags=YES + (KNELT,))),
    nar("struck", '''{n}She lets you take it. She watches you do it with her lips parted.{/n}
{n}You pull Brask's head back by the hair, and lay the flat of her knife along his cheek so that he can feel the cold of it, and then turn it and draw the point once across the back of his hand, the one he points with, where everyone who salutes him will see the line every day of his life. Not deep. Deep enough.{/n}
{n}Then you cut his bonds with the same knife, and open the door, and he goes, without a word, clutching his hand.{/n}''',
        c("Continue", "after_struck")),
    wd("after_struck", '''{n}She takes her knife back from you, and looks at the blood on it, and wipes it, slowly, on her own sleeve.{/n}
"You did it yourself. Again." {n}Her voice is thick.{/n} "With my knife. In front of me." {n}She sheathes it, and puts her hand over the hilt, as if it were warm.{/n} "In the caves, when a chief takes a hunter's kill and finishes it with the hunter's own blade, it means: *what's yours is mine, and what's mine is yours, and anybody who touches either answers to both*." {n}She steps close, very close, and puts her teeth, not gently, against the side of your neck, and then takes them away.{/n} "You didn't know that. You did it anyway. You're mine now. I'm not asking."''',
        c("Continue", flags=YES + (STRUCK,))),
    wd("no", '''{n}Brask scrambles up, rubbing his wrists, and does not wait to be told twice. The door bangs behind him.{/n}
{n}Wenduag has not moved. She is looking at you as if you had turned into a stranger in front of her eyes.{/n}
"Back to your gate." {n}She repeats it slowly.{/n} "I brought you the best thing I could catch, and you let it go." {n}She is not angry. That is the worst of it.{/n} "Then you're not mine. And I'm not yours. That's what it means, where I come from. That's all it means." {n}She pulls her hood up.{/n} "I'll still fight your war. I'm not stupid. But don't come down the cellar stair any more, {mf|master|mistress}. The neathers won't let you through."''',
        c("Continue", flags=(CLOSED,))),
], requires=(PROVED, GATE_SEEN), forbids=(COMMITTED, IN_PARTY), delay=24)

# Kept at the Commander's side, she is a living companion: the claim is played in person, on her own native list (R2-3).
# The twin opens on the walk to the Commander's quarters; the rest is the same scene. Mutually exclusive by IN_PARTY.
HUB_LISTS = ["ced27e744d2dded40bbb5adf17816dbb",    # CompanionDialogues/Wenduag/AnswersList_0003 (W path)
             "9bad7ea452d30254997b153473954cc1",    # WenduagTraitorCompanion/AnswersList_0003 (L path, recruited)
             "b14654863485b734aa0fb5ec16d2846a"]    # WenduDubious_Companion/AnswersList_0003 (redeemed, recruited at Lann's Q3)
_claim = copy.deepcopy(SCENES[-1])
_claim["Id"] = W + "court.claim_in_person"
_claim["Entry"] = '"You look pleased with yourself."'
_claim.pop("Remote", None); _claim.pop("Kind", None); _claim.pop("Areas", None)
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


# --- 5. Her cairn (intimacy; Directive 12: heat up to the cut, cut at the start of the act). --------------------------------

visit(W + "court.cairn", "In the dark, the strong one decides", [
    nar("start", '''{n}She comes for you after midnight, and takes you down: past the storerooms, past the cellars where the neathers sleep in their heaps and lift their heads as you go by, down the oldest stair to the catacombs, where Drezen's dead lay in their niches before there were too many dead to bother.{/n}
{n}At the bottom she stops, and takes the lamp out of your hand, and blows it out.{/n}''',
        c("Continue", "dark")),
    wd("dark", '''"Uplanders need light. Neathers don't." {n}Her voice is right beside your ear, and then it is not; she moves without a sound on the old stone.{/n} "Down here you're the weak one. You can't see. You can't smell. You don't know where the walls are." {n}Her hand closes round your wrist, hard, calloused, very warm.{/n} "So you'll have to let me lead."''',
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
    wd("own_kept", '''"Every hunter builds her own, before she needs it. So she knows where she's going, and nobody gets it wrong." {n}A breath of a laugh in the dark.{/n} "I wasn't going to let an uplander get it wrong."''',
        c("Continue", "top")),
    wd("top", '''{n}You hear her draw her knife. You feel her lay it, flat, on the topmost stone, under your hand, so that your fingers rest on the bone of the grip.{/n}
"There. Now you've got a knife and I haven't." {n}She is behind you. Her breath is on the back of your neck.{/n} "In the dark, the strong one decides. That's what the old ones said. They meant: the one who doesn't need to see." {n}Her hands come round and find the buckle of your belt, and stop there.{/n} "You can pick it up, if you like. Hold it on me. See how far it gets you, when you can't see where I am."''',
        c('[Leave the knife where it is. Let her decide.]', "decide"),
        c('[Pick up the knife and turn round, blade first.]', "knife"),
        c('[Take her wrists instead, and turn her against the stones.]', "roll")),
    nar("decide", '''{n}You take your hand off the knife.{/n}
{n}She makes a sound in her throat that is not a word. Then the buckle is open and your belt is gone, somewhere into the dark, and her hands are everywhere, rough and quick and certain, and not in the least gentle: she undresses you the way she skins a hare, with no wasted movement and no hesitation at all, and the cold of the catacomb comes onto your skin all at once and then her heat after it.{/n}
{n}She pushes you back against the cairn. The stones are cold and uneven against your spine. Her tail comes round your thigh, and tightens, and holds.{/n}''',
        c("Continue", "cut")),
    nar("knife", '''{n}You pick it up and turn, and there is nothing there. Only dark, and cold stone, and the smell of her somewhere very close.{/n}
{n}Then her hand closes over yours on the grip, and guides the point, unhurried, until it rests in the hollow of her own throat, and she presses forward into it until you feel her pulse through the blade. You cannot see her. You can hear that she is smiling.{/n}
"Good," {n}she says, against the edge.{/n} "Keep it there." {n}And with her other hand, one-handed, without looking, she begins to unlace her own leathers.{/n}''',
        c("Continue", "cut", flags=(W + "cairn.knife_held",))),
    nar("roll", '''{n}You find her wrists in the dark, both of them, and she lets you, for exactly as long as it takes you to turn her against the cairn, and then she laughs and twists and it is you against the stones again, with her forearm across your collarbones and her whole weight leaning on it.{/n}
"Nice try." {n}Her teeth close on the side of your throat, hard enough to mark, and let go.{/n} "Again." {n}You try again. This time it takes her longer. By the third time neither of you has anything left on above the waist, and you are not sure any longer who is winning, and neither, from the sound of her, is she.{/n}''',
        c("Continue", "cut", flags=(W + "cairn.rolled",))),
    wd("cut", '''{n}Somewhere above you, very far up, a bell tells the hour. Neither of you counts it.{/n}
"Uplanders," {n}she breathes against your mouth, straddling you now on the cold floor at the foot of her own grave, her hands already dragging down the last of what is between you,{/n} "always want to see." {n}She settles her weight, and her nails bite into your shoulders, and she lowers herself down.{/n} "Don't look."''',
        c("Continue", flags=(CAIRN_SEEN,))),
], requires=(COMMITTED,), forbids=(CAIRN_SEEN,), delay=24)


# --- 6. The morning (the consequence). --------------------------------------------------------------------------------------

visit(W + "court.morning", "Grit in your hair", [
    nar("start", '''{n}You wake alone, in the dark, on cold stone, with your coat thrown over you and grit in your hair and a dull ache in every part of you that has ever been leaned on.{/n}
{n}Somebody has left the lamp beside your hand, lit, turned low. By its light you can see the cairn, and your belt draped over the top of it, and the gap in the topmost row where one of the flat stones used to be.{/n}''',
        c("Continue", "stone")),
    nar("stone", '''{n}It is not gone. It is in your coat pocket: a flat grey stone a little bigger than your palm, with a single line scratched across it by a knife point, still sharp-edged and fresh.{/n}
{n}The neathers mark the tunnel walls like that, you remember, to say *this way is mine*. One line is one hunter.{/n}''',
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
    nar("end", '''{n}Of Wenduag there is no sign all day. That is the neather way, one of them tells you, when you ask: a hunter who has made her kill goes off alone to eat it, and does not come back until she is hungry again.{/n}
{n}She is back by nightfall. She is waiting in your quarters when you come in, sitting on the map table with her feet on your chair, eating your supper out of the pot with her fingers, as if she had never been anywhere else.{/n}''',
        c('[Put the stone on the table beside her.]', flags=(STONE,)),
        c('[Keep the stone in your pocket, and say nothing about it.]', flags=(STONE, W + "morning.pocket"))),
], requires=(CAIRN_SEEN,), forbids=(STONE,), delay=8)


# --- 7. Must acknowledge: Vellexia and Yaniel (optional, from her side, node variants on their own native flags). ----------

visit(W + "court.vellexia", "The blond one", [
    nar("start", '''{n}Wenduag has found a new sport. She sits on the parapet above the citadel yard for an hour at a time, very still, and watches one particular window.{/n}''',
        c("Continue", "promised", requires=(VELLEXIA_SEEN,)),
        c("Continue", "here", forbids=(VELLEXIA_SEEN,))),
    wd("promised", '''"The blond one." {n}She does not take her eyes off the window.{/n} "The succubus from the Midnight Isles. I promised her something, the night we met. I told her I'd make her scream." {n}Her lips peel back.{/n} "I keep my promises, {mf|master|mistress}. The fun ones."''',
        c("Continue", "what")),
    wd("here", '''"There's a succubus in your citadel." {n}She does not take her eyes off the window.{/n} "Walking about in the day like a lady, with that yellow hair and that smile, and your whole court pretending not to notice what she smells like." {n}She sniffs, deliberately.{/n} "I noticed. I notice everything that's hungry."''',
        c("Continue", "what")),
    wd("what", '''{n}She turns her head at last and looks at you, and there is a question in her face that she is not going to ask aloud.{/n}
"Demons fed my father to death. Demons fed me, and made me grateful." {n}Her voice is flat.{/n} "I'm not going to pretend I like a demon in your house because she's got nice manners. So tell me what she is to you, {mf|master|mistress}, and I'll tell you what I'm going to do about it."''',
        c('"Leave her be. She\'s under my roof, and nobody in it gets hunted."', "leave"),
        c('"Hunt her, if you want. Frighten her. Nobody dies."', "hunt")),
    wd("leave", '''"Under your roof." {n}She weighs it, and does not like it, and puts it down.{/n} "All right. I'll leave her be. Under your roof." {n}She turns back to the window.{/n} "Outside it, she's meat, like everybody else. Tell her that, when you see her. Tell her the neather said so. She'll know what it means; her kind always do."''',
        c("Continue", flags=(W + "vellexia.left",))),
    wd("hunt", '''{n}Her face lights up like a child's.{/n} "Nobody dies." {n}She says it the way she said it at the gate, like the terms of a bad bargain she has every intention of enjoying.{/n} "You're no fun. But all right. Nobody dies." {n}She slides off the parapet.{/n} "She'll hear me coming, though. Every night, somewhere in the dark, just behind her. A hare's head on her pillow. My knife in her door. Her own scent on my hands when I pass her in the hall. She'll never see me. She'll never know when." {n}Her grin is terrible.{/n} "And one night she'll turn round and I'll be close enough to bite, and I'll let her feel my teeth on her throat, and I'll let her live. That's the scream I promised. The fun ones are the ones they remember."''',
        c("Continue", flags=(W + "vellexia.hunted",))),
], requires=(GATE_SEEN, VELLEXIA_HERE), optional=True)   # only while Vellexia walks Drezen in her own body

visit(W + "court.yaniel", "The paladin in the cage", [
    nar("start", '''{n}Wenduag has heard the story at last. The neathers in the cellars tell it among themselves: the paladin who waited eighty years in a demon's cage in the Midnight Fane for somebody to open the door.{/n}''',
        c("Continue", "freed", requires=(YANIEL_FREED,)),
        c("Continue", "killed", forbids=(YANIEL_FREED,))),
    wd("freed", '''"And somebody did. You did." {n}She sounds almost resentful.{/n} "Eighty years. I'd have gnawed through my own arm. She kept hers for her sword." {n}She is quiet for a while.{/n} "The crusaders follow a legend before they follow the living. Legends don't make mistakes. That one isn't dead, and she isn't a legend yet either. She's the one to watch, {mf|master|mistress}. Not the demons. Her." {n}She shrugs.{/n} "I'm not saying do anything. I'm saying watch. Uplanders never learn the difference till the knife's already in."''',
        c('"She\'s no threat to either of us."', "threat"),
        c('"You sound jealous."', "jealous")),
    wd("threat", '''"Everybody who's still breathing is a threat to somebody." {n}She shrugs.{/n} "But fine. I'll watch her for you. I watch everybody anyway."''',
        c("Continue", flags=(W + "yaniel.watched",))),
    wd("jealous", '''{n}She bares her teeth, which is not a no.{/n} "Of what they'll sing about her, maybe. Nobody sings about neathers. We don't last long enough." {n}Then, after a while:{/n} "They sang about me, once. In the street, when they thought I was dead. A bad song. Terrible rhymes." {n}She almost smiles.{/n} "Better than nothing."''',
        c("Continue", flags=(W + "yaniel.jealous",))),
    wd("killed", '''"And you killed her. In the doorway of her cage." {n}She turns her head and looks at you, curious, careful, as if she were testing ice.{/n} "Eighty years a trophy, and a legend of the crusades, and you put her down. I've been trying to work out why. If you were afraid of her, that's cunning. If you did it for no reason at all, that's a sickness, and I'd like to know which one I've tied myself to."''',
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
    wd("her", '''"Cave moss and spit and something from a lizard's gut. Don't ask what." {n}She hisses as the old woman presses down.{/n} "Uplander healers would have given me a potion and a prayer and I'd have been walking in a day. This takes ten. But nobody writes down who they poured their potions into." {n}She turns her head and looks at you.{/n} "Dead women don't go to healers."''',
        c('"How long before you can fight?"', "fight"),
        c('"What was it like, under the stones?"', "under")),
    wd("fight", '''"I can fight now. I can't win." {n}She says it as if it were an obvious distinction, which to her it is.{/n} "Ten days. Then I'll be what I was. More, maybe. The dark does that, if it doesn't eat you." {n}She lets her head fall back on the hide.{/n} "The old ones used to say that every hunter who comes out of the ground comes out hungrier. I thought it was a story for children. It isn't."''',
        c("Continue", "sull")),
    wd("under", '''{n}She is quiet for a while, and the old woman packs the wound, and hums.{/n}
"Quiet." {n}She sounds surprised by her own answer.{/n} "That's what I remember most. Not the dark. Neathholm's dark; I was born in it. The quiet. No gongs, no tribe, no Lann, nobody telling me what I was. Just the stone on my face and my heart going, and the knife." {n}She flexes her right hand.{/n} "I lay there a long time before I pushed. Longer than I needed to. I wanted to know what it was like to be nobody's anything." {n}Then she snorts.{/n} "It was boring. So I dug."''',
        c("Continue", "sull")),
    wd("sull", '''{n}She jerks her chin toward the other cellars, where the neathers are.{/n}
"Sull knows. He knew the moment I came down the stair; he smelled it on me before I got to the bottom. He hasn't told Lann." {n}Her lip curls.{/n} "He thinks he's protecting Lann. He's protecting the tribe, from Lann finding out what Lann would do. That's what old men are for." {n}She closes her eyes.{/n} "Go away now, {mf|master|mistress}. I'm going to sleep, and I don't let anyone watch me do that. Not even you. Especially not you."''',
        c("Continue", flags=(W + "cellar.seen",))),
], requires=("trickster.ever", RETURNED, KILLED), delay=24, chapters=(3,), optional=True)

SCENES.append(_DEVICE_SCENES.pop())

SCENES.append(scene(W + "traitor.nerves", "The call", "Wenduag", 4, '"You haven\'t eaten since we came to the Midnight Isles."', [
    n("start", "conversant", '''{n}Wenduag is sitting on her heels at the edge of the camp, facing the city, the way a dog sits facing a door it is not allowed through. There are dark, oily streaks on her cheeks, dried, as if she has been crying tar and wiped it away with her sleeve.{/n}
"I can't eat. It's all wrong here. The meat tastes of him." {n}She does not turn round. Her voice is flat and very low, with none of the servant in it.{/n} "He's here, {mf|master|mistress}. Somewhere in this city. I can feel him in my blood, like a hook in a fish. He isn't calling yet. He's letting me feel how easy it would be."''',
        c('"And when he calls?"', "calls"),
        c('"Your face. What is that?"', "tears")),
    n("tears", "conversant", '''{n}She touches her cheek, looks at the black on her fingertip, and wipes it off on the ground with disgust.{/n}
"His poison. It comes out when he's near. All the neathers who ever ate from his hand weep it, sooner or later." {n}Her mouth twists.{/n} "It's the only kind of crying I've ever done. Isn't that funny?"''',
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
    nar("start", '''{n}She takes you down to the cellars in the middle of the afternoon, which she has never done, and stops at the mouth of the furthest one without going in.{/n}
{n}There is an old neather lying on a pile of straw inside: a man with a grey muzzle and milky eyes and a cough that shakes his whole body. His ribs show. Beside him somebody has left a bowl of broth and a wooden cup of water, both untouched, and a spear with a cracked shaft that he will never throw again.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Old Tuhk. He was the best trapper in Neathholm when I was small. He taught me to set a snare." {n}Her voice is quite matter-of-fact.{/n} "Lung rot, from the damp down here, or from the tunnels before; it doesn't matter which. He'll die by the spring. Before that he'll eat a winter's food and give it to the rot, and cough on the little ones, and one or two of them will get it, and they'll die in the summer." {n}She folds her arms.{/n} "Sull would feed him to the last crumb and let the cough take three children with him, and call that the tribe. That's why the tribe is still living in a hole." {n}Her lip curls.{/n} "I'd walk him down to the deep tunnels tonight and leave him there with his spear. It's kinder than the cough, and the little ones eat his share. The weak get eaten. That's not cruelty. That's arithmetic."''',
        c("Continue", "ask")),
    wd("ask", '''{n}She looks at you sideways.{/n} "These are my people now. They do what I say. But they're in your city, under your roof, and your chaplains come down here sometimes with their bread and their prayers." {n}Her yellow eyes are steady.{/n} "So I'm asking. I'm asking you, because I'm yours. Tonight I walk him down the oldest stair, past my cairn, and leave him in the dark with his spear. Or I don't. Say which."''',
        c('"Do it. It\'s your tribe, and your arithmetic."', "cull", alignment=("Evil", 1)),
        c('"No. Nobody gets left in the dark to die in my city."', "forbid"),
        c('"Take him up to the chaplains\' infirmary. Tonight. I\'ll pay for his bed."', "infirmary", alignment=("Good", 1),
          crusade=("Finances", -100))),
    wd("cull", '''{n}She nods, as if you had confirmed a sum.{/n}
"Yes." {n}Then, lower:{/n} "I did this once before, in the Maze, for Hosilla. Nobody said anything. I carried all of it. Nobody ever said *do it* out loud before, so that somebody else carried half." {n}She goes into the cellar and crouches beside him, and says something in the neather tongue that makes him stop coughing and turn his milky eyes toward her, and she puts the cracked spear in his hands, and helps him up.{/n}
{n}You do not go down the oldest stair with them that night. In the morning the straw in the furthest cellar is gone, and the bowl and the cup are washed and put away, and nobody in the cellars says anything about it, to you or to each other.{/n}''',
        c("Continue", flags=(W + "neathers.culled",))),
    wd("forbid", '''{n}Her face hardens.{/n} "You'd let him cough to death slowly, instead of quickly. And take the little ones with him." {n}She stares at you as if you had said something in a language she only half speaks.{/n} "That's the uplander way. Keep everyone breathing, however badly, however long. Call it mercy."
{n}She is angry. She holds it for a while, and then, visibly, she puts it down.{/n} "All right. Your city. Your law. He stays." {n}She looks at the old man.{/n} "But when the little ones start coughing, {mf|master|mistress}, you come down here and you look at them. You don't get to say *no* and then not look."''',
        c("Continue", flags=(W + "neathers.forbidden",))),
    wd("infirmary", '''"The chaplains." {n}She says it as if it were a word for a disease.{/n} "They'll pray over him. They'll wash him with holy water and look at his teeth and his claws and wonder what he is." {n}Then she stops, and looks at him, and at you.{/n} "They'll also have a dry bed, and potions, and nobody coughing on the children." {n}She is quiet for a long while.{/n}
"You'd pay for a neather's bed. With your own money, in front of your own priests." {n}She shakes her head slowly.{/n} "I don't understand you. It's not arithmetic. It's not strength." {n}She goes in and picks him up, straw and all, as easily as a sack, and he coughs into her shoulder and she lets him.{/n} "I'll carry him myself. If they want to pray, let them pray at me."''',
        c("Continue", flags=(W + "neathers.infirmary",))),
], requires=(PROVED,), optional=True)

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
    wd("blunder_her", '''"There. Now you know what the tribe felt like when I was five." {n}She is laughing silently, shoulders shaking.{/n} "I scared off every kill for a whole winter. They nearly ate me instead." {n}She takes your wrist and pulls you on.{/n} "Come on. Deer are stupid. It'll stop in a hundred paces and forget why it ran. This time, step where I step."''',
        c("Continue", "hers")),
    nar("thrown", '''{n}The throw is not a good one. It goes in behind the shoulder, too far back, and the deer screams and runs, and she is already gone after it, flat out, low to the ground, faster than you have ever seen anything on two legs move. By the time you catch up she has it down in the thorn with her knife in its throat and her knee on its neck, and she is laughing.{/n}''',
        c("Continue", "eat")),
    nar("hers", '''{n}She throws from where she stands, without seeming to aim. The spear takes the deer through the heart and it drops where it stood, without a sound, and does not kick.{/n}
{n}She walks up to it unhurried, and kneels, and pulls the spear free, and opens its chest with her knife in three strokes.{/n}''',
        c("Continue", "eat")),
    wd("eat", '''{n}She cuts the heart out while it is still warm and holds it in both hands, steaming in the cold, and bites into it, and holds it out to you, with blood running down her chin.{/n}
"The hunter who makes the kill eats first. The one who was there eats second. Everyone else waits." {n}Her teeth are black in the moonlight.{/n} "Go on. You were there."''',
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
    wd("her", '''"In Neathholm there's a gong. A big one, bronze. Nobody knows where it came from; the old ones say a crusader camp, before anyone was born. Someone strikes it at every change of the watch, because in the tunnels there's no day and night, only the gong." {n}She tilts her head toward the bell.{/n} "That's the only thing I miss. Isn't that stupid? Not the tribe. Not the dark. The gong. I used to count my life in it. Thousands of gongs since my father went hunting and didn't come back."''',
        c("Continue", "father")),
    wd("father", '''{n}She is quiet for a while.{/n}
"They said the tunnels ate him. That's what they say when someone doesn't come back. The tunnels ate him." {n}Her voice is flat.{/n} "It wasn't the tunnels. It was him. Savamelekh. He took the strong ones, Rullo, old Gorom, my father, and fed them his poison until they forgot they'd ever had names." {n}She pulls her knees up.{/n} "Every neather child in Neathholm grows up knowing somebody the tunnels ate. None of them knows it was a demon with a skin like a wet drum. I know. I'm the only one who knows and is still alive."''',
        c("Continue", "maze_chosen", requires=("wenduag.chosen",)),
        c("Continue", "maze_lann", forbids=("wenduag.chosen",))),
    wd("maze_chosen", '''"You know what I thought, in the Maze, the first time I saw you?" {n}She turns her head.{/n} "Lann was there, and me, and you had to choose. And I thought: *this one will choose Lann. Everyone chooses Lann. Lann is nice.*" {n}She laughs, softly.{/n} "And you chose me. The one who'd sold people to a demon for a piece of meat. You looked at both of us and you chose the one who bit." {n}She is not laughing now.{/n} "I've been trying to work out why ever since. I think I know, now. I think you saw what I'd do with it."''',
        c('"I did."', "saw"),
        c('"I chose the stronger one."', "stronger")),
    wd("maze_lann", '''"In the Maze, the first time, you had to choose between me and Lann." {n}She turns her head.{/n} "You chose Lann. Of course you did. Everyone chooses Lann. Lann is nice." {n}No bitterness in it; she says it the way she might say that water is wet.{/n} "And then, later, when you had the choice again, with my life in your hand, you chose me. Not the way anyone would think." {n}She looks at you for a long while.{/n} "I think that's the only choice that counted. The first one was just manners."''',
        c('"It was the only one that counted."', "saw"),
        c('"I chose the stronger one, the second time."', "stronger")),
    wd("saw", '''"Yes." {n}She nods, as if something has been settled.{/n} "Nobody ever chose me for what I'd do. They chose me in spite of it, or to use it, or they didn't choose me at all." {n}She stands, and stretches, and the bell down in the lower town stops.{/n} "One more gong, {mf|master|mistress}. Come to bed. It's cold up here, and you're the only uplander I know who's warm."''',
        c("Continue", flags=(W + "gongs.saw",))),
    wd("stronger", '''{n}That pleases her. It pleases her enough that she laughs out loud, and a sentry further along the wall looks round and then pretends he hasn't.{/n}
"The stronger one. Yes. That's the only honest answer anyone's ever given me about anything." {n}She gets up.{/n} "Don't ever tell me it was because you liked me. I'd have to kill you for lying." {n}She holds out her hand, and pulls you to your feet, and does not let go of it.{/n} "One more gong. Come to bed."''',
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

SCENES.append(reaction("Irabeth", W + "react.irabeth_traitor", ("trickster.ever", RETURNED, STREET_CAIRN),
    '''{n}Irabeth closes the door of her office behind you before she says anything, which is how you know it is bad.{/n}
"The watch on the south gate is talking. A sergeant says he saw the traitor from the street breathing, and that the Commander buried her quiet. His captain laughed at him. I didn't." {n}She sits down.{/n} "And now my people tell me there's a neather woman hunting hares at night outside the south postern, who comes and goes through a gate that's supposed to be shut to her kind after dark." {n}Her voice is very even.{/n} "I'm the head of your security, Commander. I found a traitor in this city once before, in my own chapel. I'm not going to ask you what you've done. I'm going to tell you that if she so much as looks at one of my soldiers the wrong way, I'll hang her myself, and you can bury her properly the second time."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You wanted to see me, Irabeth?"', chapter=5, last=5, portrait="Irabeth",
    Chapters=[5], **IRABETH_GUARD))
tag(W + "react.irabeth_traitor", "T")


# --- 9. Epilogue pages (Owner WenduagEpilogue, Chapter 6; no effects; no page Requires another). ---------------------------

EPI = "WenduagEpilogue"
SAC = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})

COMMON = (
    p("{n}Lann never quite forgave the Commander, and never quite stopped following. He had been told the truth before he found it for himself, and he said, years later, that it was the only reason he could still stand to be in the same room. He never went down the cellar stair.{/n}", requires=(LANN_PAID,)),
    p("{n}Lann had to find the truth for himself, in a cellar, by the smell of a woman he had mourned; and then he had to ask for it. He got it, late. He followed the Commander to the end of the war and after, and he listened, every time the Commander spoke, for the lie. He said he never heard another one. He never said he stopped listening.{/n}", requires=(LANN_PAID_LATE,)),
    p("{n}Lann asked the Commander once for the truth about the cairn, and was told to leave it. He left it. He followed the Commander to the end of the war, and he fought as well as he ever had, and he never again made a joke in the Commander's hearing. Some of the soldiers thought he had grown up. The Commander knew better.{/n}", requires=(LANN_OWED,)),
    p("{n}Lann asked the Commander once for the truth, and was lied to, and believed it, because he wanted to. Nobody ever told him otherwise. Wenduag, who could have, never did; she said it was the Commander's lie, and the Commander's to carry, and that she was not a porter.{/n}", requires=(LANN_LIED_AGAIN,)),
    p("{n}Lann never learned that Wenduag lived. Whatever he believed about the cellar neathers' dead hunter, he kept it to himself, and did not go down to look.{/n}", requires=(LIED,), forbids=(LANN_PAID, LANN_PAID_LATE, LANN_OWED, LANN_LIED_AGAIN)),
    p("{n}She carried the Commander's stroke in her side for the rest of her life: a long pale seam, low on the left, a finger's width from the place that would have ended her. She showed it to people she wanted to frighten. She never said who had put it there. She said she was saving the answer for the day she paid it back.{/n}", requires=(DEEP,)),
    p("{n}She kept the Commander's waterskin, the one that had been under her hand in the dark. She never drank from it again, and she never threw it away, and she never explained either.{/n}", requires=(WATER,)),
    p("{n}The flat stone with the Commander's mark scratched into its underside hung on a thong round her neck for the rest of the war. In the tunnels, she said, that was called a claim; up here, it was called a necklace, and uplanders were stupid.{/n}", requires=(MARK,)),
    p("{n}Savamelekh's stinger stayed with her, wrapped in sacking, for the rest of her life. She showed it to the young neathers of the cellars when they were old enough to understand, and told them what it was, and what it had cost, and what it had called, and that it did not call any more.{/n}", requires=(STINGER_GIVEN,)),
    p("{n}The Commander still owed her a death, a big one, as big as Savamelekh. She said she had picked it, and never said what it was. The Commander stopped asking. Some debts are better left in the dark.{/n}", requires=(PROMISE_OWED,)),
    p("{n}Savamelekh's stinger went into a brazier in a Drezen cellar, and the smell of it hung about the place for a month. The neathers who lived there said afterwards that it was the first month of their lives when nothing had called them in the night.{/n}", requires=(STINGER_BURNED,)),
    p("{n}Savamelekh was still alive somewhere, when the war ended, with the smell of his poison in the wind. She went hunting for him the spring after the Threshold, alone, with a spear and a knife and the Commander's promise, and she came back in the autumn, and would not say. She did not smell of him any more. That was the only answer anyone ever had.{/n}", forbids=(SAVA_DEAD,)),
)

COMMITTED_PARAS = (
    p("{n}Sergeant Brask served out the war on the far wall of the lower town, as far from the cellar stair as Drezen allowed, and never again used the word *mongrel*. His hand healed crooked. He learned to salute with the other one.{/n}", requires=(GIVEN,)),
    p("{n}Sergeant Brask kept the south gate until the end of the war, and every neather who came through the postern after dark was let through with a nod. He never said her name again after that one time on his knees, but everyone who had heard him say it remembered, and so did he.{/n}", requires=(KNELT,)),
    p("{n}Sergeant Brask kept the south gate until the end of the war, with a thin white line across the back of his sword hand where every man who saluted him could see it. He never told anyone how he got it. He did not have to.{/n}", requires=(STRUCK,)),
    p("{n}Old Tuhk went down the oldest stair one night with his cracked spear in his hands, and did not come back up, and his share fed the cellars through the winter. Nobody coughed in the furthest cellar that summer. She never spoke of it again, but she never again asked the Commander for anything she could decide herself, either.{/n}", requires=(W + "neathers.culled",)),
    p("{n}Old Tuhk died in a chaplain's bed in the spring, warm and dry, with a priest of Iomedae praying over him in a language he did not understand and Wenduag sitting at the foot of the bed with her arms folded, glaring at the priest. She said afterwards that it was a stupid way to die. She went back every day until it was over.{/n}", requires=(W + "neathers.infirmary",)),
    p("{n}Two of the little ones in the cellars caught the cough that winter. The Commander went down and looked at them, every time she said to, and one of them lived. She counted that as a draw.{/n}", requires=(W + "neathers.forbidden",)),
    p("{n}The succubus in the citadel learned to sleep with a lamp lit and her back to a wall. Hare's heads on her pillow, a knife in her door, and one night teeth at her throat in a dark corridor, and a laugh, and nothing else. She never found out whose. Wenduag said it was the best promise she ever kept.{/n}", requires=(W + "vellexia.hunted",)),
    p("{n}Wenduag left the succubus alone under the Commander's roof, as she had said she would, and passed her in the halls every day of the war without a word, and sniffed, every time, loudly.{/n}", requires=(W + "vellexia.left",)),
    p("{n}Some nights, when the war let them, she took the Commander out through the south postern barefoot with a spear and no light, and they came back before dawn with blood on their chins and nothing to say to anyone.{/n}", any_groups=((W + "hunt.ate", W + "hunt.cooked"),)),
    p("{n}She never once used the Commander's name where anyone could hear, and she stopped saying *master* altogether. When she needed to call the Commander she whistled, the way the neathers whistle in the tunnels, one note up and one down, and the Commander came, and everybody who saw it pretended not to have.{/n}"),
    p("{n}Every so often she woke the Commander in the night with a knife at the throat and her knee on the breastbone, to see. The Commander never once lay there working out whether she meant it. She said that was how she knew.{/n}", any_groups=((W + "trial.won", W + "trial.tricked"),)),
    p("{n}Every so often she woke the Commander in the night with a knife at the throat and her knee on the breastbone, to see. The first time, the Commander had bled for it. The old white line on the Commander's forearm was the only scar she ever said she was proud of that she had not given herself.{/n}", requires=(BLED,)),
)

SCENES.append(scene(W + "epilogue.pack", "", EPI, 6, "", [
    nar("page", '''{n}Wenduag of Neathholm was dead, as far as Drezen knew, or she was the Commander's dog, as far as Drezen said aloud. She was neither. She kept to the cellars under the citadel with the neathers who had come up out of the tunnels to fight the war, and by the end of it they were hers: not because anyone had given them to her, but because she was the strongest thing in the dark, and she let them see it.{/n}
{n}She fought where the fighting was worst and ate what she killed and never once pretended to be sorry for anything. She did not become a crusader. She did not learn to pray. She learned the names of the Commander's enemies, all of them, and wrote them nowhere, and forgot none.{/n}
{n}Down at the bottom of the oldest stair, in the dark, there was a cairn with the head end loose. It was hers. The Commander was the only uplander who ever knew where it was.{/n}''',
        paragraphs=COMMITTED_PARAS + COMMON)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"), last=6, Relationship=REL, **SAC))
tag(W + "epilogue.pack", "T")

SCENES.append(scene(W + "epilogue.unclaimed", "", EPI, 6, "", [
    nar("page", '''{n}The war ended before Wenduag had caught anything worth laying at the Commander's feet. She said so herself, sourly, to anyone who asked: the good prey had all been killed by other people.{/n}
{n}She stayed in the cellars under the citadel with the neathers, all the same. She hunted outside the south postern at night and came back with hares and once with a deer, and fought in the Commander's war where the fighting was worst, and was the Commander's in every way that mattered to her except the one she had not yet decided to ask for.{/n}
{n}The spring after the Threshold, she caught something. What it was, and whose feet she dropped it at, and what they did with it, belongs to the years after the war.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", STARTED), forbids=(COMMITTED, CLOSED, "sacrifice"), last=6, Relationship=REL, **SAC))
tag(W + "epilogue.unclaimed", "T")

SCENES.append(scene(W + "epilogue.dead", "", EPI, 6, "", [
    nar("page", '''{n}Wenduag of Neathholm stayed dead. The Commander had said so, once, in the dark, and she had taken the Commander at the word.{/n}
{n}The neathers in the cellars of Drezen told a story for years afterwards about a dead hunter who lived at the bottom of the oldest stair, and ate raw hare, and came out on moonless nights to walk the walls of the city that had buried her. Children were told that if they were very weak, or very stupid, she would come for them. The children of the neathers grew up very strong, and not at all stupid.{/n}
{n}Nobody ever found her cairn. The Commander never looked.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", CLOSED), RequiresAnyGroups=[[CAIRN, ABYSS_CAIRN, STREET_CAIRN]], forbids=(COMMITTED, "sacrifice"),
    last=6, Relationship=REL, **SAC))
tag(W + "epilogue.dead", "T")


# --- Registration -------------------------------------------------------------------------------------------------------------

def integrate(payload):
    """The Last Call partner key (committed here, or the native romance kept to the end); wenduag_trickster binds the rest."""
    for key, groups in _DERIVED_EXTRA.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
