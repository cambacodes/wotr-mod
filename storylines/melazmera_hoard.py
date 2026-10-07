"""Melazmera between the beats of her route (11-ROSTER-PLAN-2 §2 build sheet; melazmera_trickster holds the device chain,
the commit, the heap and the pages).

She writes in stone. Every letter she sends is a flat grey rock with small square letters scored into one face by a claw,
dropped through a tent roof in the Abyss or left on a windowsill in Drezen; in Chapter 5 each one carries the Commander's
old seal pressed into a smear of clay. Her visits come at night, in the woman her illusions make (the craft that wraps rocks
in crowns), or in her own shape on the roof of the keep. Every beat is optional and Trickster-only (T in PATH_FIT); none of
them is a partner-to-partner scene, and none states exclusivity as fact.
"""
from story_format import c, n, scene
from storylines.melazmera_trickster import DREZEN
from storylines.melazmera_trickster import (ATE, CLOSED, COMMITTED, DEAD, DECLINED, FED, FED_CULTISTS, FED_DEMONS, FED_HERD,
                                             GREY_CARRIED, GREY_HAND, HARPOONED, CREVICE, SCREAM, CAPTURED, HEAP, LEFT_FREE, M, MESSAGE, PROMISED,
                                             QUEEN_MET, QUEEN_TURNED, FIST, REL, RETURNED, SALTED, SEAL, STONE_KEPT, mz, nar, tag)

SCENES = []

FIRST_READ = M + "stone.first_read"
SECOND_READ = M + "stone.second_read"
REPLY_HONEST = M + "stone.reply_honest"
REPLY_BOAST = M + "stone.reply_boast"
REPLY_QUESTION = M + "stone.reply_question"
FLIGHT = M + "beat.flight"
LET_GO = M + "beat.flight_let_go"
CREW = M + "beat.crew"
CREW_PAID = M + "beat.crew_paid"            # legacy: she was told to pay the dead sailors' kin (now: she paid, in illusion-gold)
CREW_ILLUSION = M + "beat.crew_illusion_gold"  # she paid in illusion-gold under the Commander's seal; it turned to rock past the quay
CREW_DEBT_STANDS = M + "beat.crew_debt_stands"  # ...and the Commander let the debt stand in the Commander's name
CREW_DEBT_SETTLED = M + "beat.crew_debt_settled"  # ...and the Commander made it good in true gold from the crusade chest
CAPTAIN_SPARED = M + "beat.captain_spared"  # the harpooner is under the Commander's protection
QUEEN = M + "beat.queen"
ILLUSION = M + "beat.illusion"
SOULS = M + "beat.souls"
SOUL_REFUSED = M + "beat.soul_refused"
SOUL_LIED = M + "beat.soul_lied"
SEAL_ASKED = M + "beat.seal_asked"          # the Commander asked for the old seal back (she said no)
SEAL_LEFT = M + "beat.seal_left"
AXE = M + "beat.greybor_heard"
DINNER = M + "beat.dinner"
DINNER_EATEN = M + "beat.dinner_eaten"
SHIELD = M + "stone.shield"
COUNTED = M + "beat.counted"
WAR = M + "beat.war"
SHIRT = M + "stone.shirt"


def letter(id, title, nodes, requires, forbids=(), delay=48, chapter=5):
    """A stone with her words scored into it, dropped through a roof or left on a sill."""
    SCENES.append(scene(id, title, "Melazmera", chapter, "", nodes, requires=("trickster.ever", RETURNED, *requires),
                        forbids=(DEAD, CLOSED, LEFT_FREE, DECLINED, *forbids), delay=delay, last=chapter, optional=True,
                        Relationship=REL, Remote=True, Kind="letter", Chapters=[chapter],
                        ForbidOverrides={DECLINED: COMMITTED}, **(dict(Areas=[DREZEN]) if chapter == 5 else {})))
    tag(id)


def visit(id, title, nodes, requires, forbids=(), delay=24):
    """A night visit in Chapter 5: the window, or the roof of the keep."""
    SCENES.append(scene(id, title, "Melazmera", 5, "", nodes, requires=("trickster.ever", MESSAGE, *requires),
                        forbids=(DEAD, CLOSED, LEFT_FREE, DECLINED, *forbids), delay=delay, last=5, optional=True,
                        Relationship=REL, Remote=True, Kind="visit", Chapters=[5], Areas=[DREZEN],
                        ForbidOverrides={DECLINED: COMMITTED}))
    tag(id)


# --- Chapter 4, after Colyphyr: stones through the roof. ------------------------------------------------------------------

letter(M + "stone.first", "A stone through the roof", [
    nar("start", '''{n}It comes through the roof of your tent a little after midnight, through canvas and ridge-pole both, and lands on your table hard enough to split the lamp. By the time you have beaten out the oil and your sentries have come running with their swords out, there is nothing overhead but the red sky of the Abyss, and nothing on the table but a stone.{/n}
{n}It is flat and grey and the size of a psalter. One face of it is covered, edge to edge, in small square letters, scored into the rock by something very hard and very sharp, one careful stroke at a time.{/n}''',
        c("[Read it.]", "words")),
    mz("words", '''"THIEF.
TODAY I ATE: ONE GOAT. ONE HARPY, OLD. A THING FROM THE BOTTOM OF THE SEA WITH TOO MANY LEGS. HALF A DEMON I DID NOT LIKE. THE OTHER HALF IS STILL ON THE CLIFF IF YOU WANT IT.
WHAT DID YOU EAT?
YOUR RING HAS A MARK ON IT. WHAT DOES THE MARK MEAN?
LEAVE YOUR ANSWER ON THE HIGHEST ROCK NEAR YOUR FIRE. I WILL KNOW WHICH ROCK.
M."''',
        c("Continue", "reply")),
    nar("reply", '''{n}Your sentries are still standing in the torn doorway of the tent, looking at the hole in the roof, and then at you, and then at the stone. One of them asks, very carefully, whether he should double the watch.{/n}
{n}You find a flat stone of your own outside, and a knife.{/n}''',
        c('[Scratch an honest answer] "Salt pork. Hard bread. It means every order I give is mine."', "done",
          flags=(FIRST_READ, REPLY_HONEST)),
        c('[Scratch a boast] "Nothing as good as a harpy. It means the whole crusade does what I say."', "done",
          flags=(FIRST_READ, REPLY_BOAST)),
        c('[Scratch a question back] "Why do you count your stones?"', "done", flags=(FIRST_READ, REPLY_QUESTION)),
        c("[Leave no answer.]", "none", flags=(FIRST_READ,))),
    nar("done", '''{n}It takes a long time to scratch even a few words into stone with a knife. By the time you have finished, your hand aches and the knife has lost its edge, and you have a new respect for whatever did all the rest. You carry your stone up to the highest rock beyond the firelight and leave it there, face up.{/n}
{n}In the morning it is gone, and there is a long scorched streak across the rock where something landed, and took off again.{/n}''',
        c("Continue")),
    nar("none", '''{n}You leave the stone where it landed and go back to your blankets. Your sentries double the watch without being told.{/n}
{n}Twice before morning you wake, sure that something very large has settled on the highest rock beyond the firelight and is waiting there, patiently, for a reply that does not come.{/n}''',
        c("Continue"))],
    requires=(), forbids=(FIRST_READ,), delay=24, chapter=4)

letter(M + "stone.second", "A stone in the porridge", [
    nar("start", '''{n}The second one arrives at breakfast. It comes down out of a clear red sky into the cook's porridge pot, and the cook, who has been with the crusade since Kenabres and has seen a great many things fall out of the sky of the Abyss, fishes it out with a ladle and brings it to your table without a word, and goes back to making more porridge.{/n}''',
        c("Continue", "honest", requires=(REPLY_HONEST,)),
        c("Continue", "boast", requires=(REPLY_BOAST,)),
        c("Continue", "question", requires=(REPLY_QUESTION,)),
        c("Continue", "silent", forbids=(REPLY_HONEST, REPLY_BOAST, REPLY_QUESTION))),
    mz("honest", '''{n}"THIEF.{/n}
SALT PORK IS WHAT A PIG IS WHEN IT HAS GIVEN UP. YOU SHOULD EAT BETTER THINGS. I WILL BRING YOU BETTER THINGS.
EVERY ORDER YOU GIVE IS YOURS. THEN I HAVE ALL YOUR ORDERS ON MY CLAW. I GAVE ONE. I TOLD A VROCK TO BE DINNER. IT DID AS IT WAS TOLD.''',
        c("Continue", "tail")),
    mz("boast", '''{n}"THIEF.{/n}
NOTHING IS AS GOOD AS A HARPY. YOU ARE RIGHT. I AM GLAD YOU KNOW IT.
THE WHOLE CRUSADE DOES WHAT YOUR MARK SAYS. I FLEW OVER IT AND TOLD IT TO BE QUIET. IT SHOUTED AND SHOT ARROWS. YOUR CRUSADE IS BADLY TRAINED.''',
        c("Continue", "tail")),
    mz("question", '''"THIEF.
A KOBOLD TOOK THE BLUE STONE ONCE. HE HID IT UNDER HIS TONGUE. I FOUND IT WHEN I ATE HIM.
FORTY-ONE STONES. ONE SEAL. I COUNT BEFORE I SLEEP.
I COUNT AGAIN WHEN I WAKE."''',
        c("Continue", "tail")),
    mz("silent", '''{n}"THIEF.{/n}
YOU DID NOT ANSWER. I WAITED ON THE HIGH ROCK. A HARPY SAT ON IT WITH ME. I ATE THE HARPY. IT WAS NOT AN ANSWER.
I WILL ASK AGAIN WHEN I CAN SEE YOUR FACE. YOU WILL NOT LIKE IT BETTER.''',
        c("Continue", "tail")),
    mz("tail", '''"I FLEW OVER THE CITY OF THE LADY IN SHADOW. IT SMELLS OF PERFUME POURED ON TOP OF PISS. NOTHING THERE IS WORTH EATING EXCEPT THE THINGS THAT WOULD DISAGREE WITH ME.
THERE IS A HOLE IN YOUR WORLD. I HAVE LOOKED DOWN IT FROM THIS SIDE. THINGS COME UP OUT OF IT WARM. I AM THINKING ABOUT IT.
M."''',
        c("[Put it with the first stone.]", flags=(SECOND_READ,)),
        c("[Give it back to the cook, for the soup.]", flags=(SECOND_READ,)))],
    requires=(FIRST_READ,), forbids=(SECOND_READ,), delay=48, chapter=4)


# --- Chapter 5: night visits and stones, before and after the heap. ------------------------------------------------------

visit(M + "beat.flight", "Over the Wound", [
    nar("start", '''{n}The keep goes quiet under you a little after the second bell, every horse and every dog at once. When you climb out onto the leads she is along the ridge of the roof in her own shape, with the old seal glittering on her claw, and she puts her head down beside the chimney for you.{/n}
"Get on," {n}she says.{/n} "I am going to show you your war from where I see it. Nobody else in your castle has ever seen it from there. They would all be sick."''',
        c("[Climb up behind her head.]", "up")),
    nar("up", '''{n}She does not fly the way a bird flies. She falls off the keep, and goes on falling long enough that you are certain she has misjudged it, and then the wings open with a crack like a sail in a gale and the whole of Drezen swings away beneath you, and she is climbing, and climbing, and the cold comes up through her plates and through your clothes and into your teeth.{/n}
{n}Then she levels out, and you see it.{/n}''',
        c("Continue", "see")),
    nar("see", '''{n}The Worldwound from above, at night, is a burn on the skin of the world that has not scabbed. The rifts glow along it in rows, like the cracks in a loaf of bread gone black in the oven, and round every one of them there is a ring of dark where the land has died. South, very small, are the crusade's fires: Drezen's walls, the camps on the road, a thin gold chain of pickets strung along the Wound's edge, each link a man with a torch who does not know that anything is overhead.{/n}
"There," {n}she says, and her voice comes up through her whole body and into yours.{/n} "That is you. That little string of lights. And that is the thing you are fighting." {n}Her head swings north, at the dark.{/n} "It is bigger."''',
        c('"What do you see, when you look at it?"', "sees"),
        c('"It won\'t be, when I\'m done."', "boast")),
    mz("sees", '''"Doors." {n}She banks, slowly, and the rifts turn beneath you like the spokes of a wheel.{/n} "Every one of those is a door, and something is always coming up through it. I can taste them. The air above the Wound is full of things going up and things going down. Most of what goes down is yours. Soldiers. They go down very fast, with a sound like a coin dropped in a well." {n}She sounds pleased with the comparison.{/n} "I have been eating the ones that come up. Nobody is eating the ones that go down. That is a waste."''',
        c("Continue", "dive")),
    mz("boast", '''{n}She laughs, and it goes out across the Wound like thunder, and far below a picket-torch stops moving.{/n}
"You are standing on the back of a dragon in the middle of the sky with nothing under you but a mile of air," {n}she says,{/n} "and you are boasting. You are the stupidest thing I have ever carried." {n}She sounds delighted.{/n} "Hold on, then, conqueror. I am going to show you how small you are."''',
        c("Continue", "dive")),
    nar("dive", '''{n}She folds her wings and drops. The wind tears at you. Your eyes stream, the spines under your hands are slick with cold, and the ground comes up out of the dark, a rift the size of a river, glowing, rushing at you, until you can see the stones on its lips and the steam coming off them and something moving in the steam, and at the last moment she opens her wings and the world slams into your spine and you are skimming along the Wound's edge so low that her claws trail through the smoke.{/n}''',
        c("[Hold on with both hands and every muscle you have.]", "hold"),
        c("[Let go of her spines and spread your arms.]", "letgo")),
    mz("hold", '''{n}You hold on. She climbs out of the dive, and out of the smoke, and up into the clean cold air, and when she speaks again she is giggling.{/n}
"You are holding on so hard I can feel it through my plates," {n}she says.{/n} "Good. Things I carry should hold on." {n}She turns south, towards the little string of lights.{/n} "I will take you home now, before you freeze and I have to explain to your priests why their Commander is blue."''',
        c("Continue", "home")),
    mz("letgo", '''{n}You let go. For one heartbeat there is nothing holding you to her at all but speed and the wind; then her whole body rolls under you, a slow smooth half-turn that keeps you pressed to her neck as if you were glued there, and she comes up out of the smoke with you still on her back and your arms still out.{/n}
"You let go," {n}she says. She sounds scandalised, and something else.{/n} "Nobody lets go. Everything I have ever carried held on until I ate it." {n}She flies on a while in silence.{/n} "Do not do that again. I did not like it. Do it again."''',
        c("Continue", "home", flags=(LET_GO,))),
    nar("home", '''{n}She puts you down on the roof of the keep with your legs numb and your hands raw and your face stiff with frost. The sentry on the gate-tower is staring at the sky, where she is already going, and when you pass him on the stair he opens his mouth and shuts it again and salutes, very correctly, to the air slightly to the left of you.{/n}''',
        c("[Go down to bed.]", flags=(FLIGHT,)))],
    requires=(FED,), forbids=(FLIGHT,))

visit(M + "beat.crew", "Salt", [
    nar("start", '''{n}She is sitting on your windowsill when you come up from the war council, in the woman she wears, with her knees drawn up and a stone in her hand, turning it over and over. She does not look round.{/n}
"Your sky-ship," {n}she says.{/n} "The one that brought you to my island. You have been thinking about it. I can see it on your face whenever you look at my claw."''',
        c("Continue", "ate", requires=(ATE,)),
        c("Continue", "harpoon", requires=(HARPOONED,), forbids=(ATE,)),
        c("Continue", "missed", requires=(CREVICE,), forbids=(ATE, HARPOONED)),
        c("Continue", "scream", requires=(SCREAM,), forbids=(ATE, HARPOONED, CREVICE)),
        c("Continue", "arrival", forbids=(ATE, HARPOONED, CREVICE, SCREAM))),
    mz("ate", '''"You want me to be sorry about the sailors." {n}She tilts her head, considering it, as she might consider an unfamiliar fruit.{/n} "I was hungry, and they were there, and they were salty. I told you when we met: be angry quickly. You were not angry quickly. You have been angry slowly, all this time, and saying nothing." {n}She sounds curious, not guilty.{/n}
"So say it now. What do you want for them? I do not know what people want for sailors. Nobody ever asked me for anything for the ones I ate."''',
        c('"They had families. You paid Greybor in gold. Pay them."', "pay", requires=(GREY_CARRIED,)),
        c('"They had families. You have gold. Pay them."', "pay", forbids=(GREY_CARRIED,)),
        c('"They were sailors. Sailors die. I only wanted you to know I remember them."', "remember"),
        c('"Nothing. But if you ever touch a ship of mine again, I will come to your cave with a harpoon myself."', "threat")),
    mz("pay", '''"Pay." {n}She laughs until she has to hold the frame, and then she holds out her hand, and the old seal glitters on the smallest finger.{/n} "Pay! Gold! I have a sack of it from the drowned country, and nobody on your side of the hole has ever seen it. It is heavy, and it shines, and it is mine." {n}She taps the ring against the sill.{/n}
"Press your name in the clay and they will take it from me. People take anything with your name on it. I have watched them do it with a crown." {n}Her eyes are very bright, and one corner of her mouth is not quite straight.{/n} "I will carry it to the Alushinyrra quay myself, to the ones whose men I salted. You said pay them. I am going to pay them."''',
        c("Continue", "paid")),
    nar("paid", '''{n}She is gone three nights. On the fourth morning the sack is back on your war map, empty and damp, with the old seal pressed into its clay, and beside it lies a heap of rocks: grey, lumpy, ordinary, the kind a child could throw. Under them is a message from the Alushinyrra quay, in a docker's cramped hand, with the Knight Commander's seal pressed into the wax. It says that gold came off the quay stairs in the dragon's claws, and under the sun on the quay it was gold, and it was counted into the hands of the dead men's kin, one by one, and at the first bell of the morning every coin of it was a rock. The kin know whose seal was on the sack. They want what was promised them, and they have named the one who promised it.{/n}
"They would not let me land." {n}She is on the sill, in the woman she wears, delighted, picking at a rock on her thumbnail.{/n} "They screamed and they threw things. So I let go of the sack from the sky." {n}She giggles.{/n} "You said pay them. You did not say in what."
{n}The empty leather smells of salt. Her claw has scored SALTY across it.{/n}''',
        c("[Keep the sack. Let the debt stand in your name.]", flags=(CREW, CREW_PAID, CREW_ILLUSION, CREW_DEBT_STANDS)),
        c("[Make it good in true gold from the crusade chest.]", flags=(CREW, CREW_PAID, CREW_ILLUSION, CREW_DEBT_SETTLED),
          crusade=("Finances", -100))),
    mz("remember", '''"You remember them." {n}She says it slowly, testing it.{/n} "I do not remember the things I eat. I remember that I ate them. That is different." {n}She looks down at the stone in her hand.{/n}
"Then you keep them, and I will keep you keeping them. Say their names to me when I ask, thief. I will ask when I am bored, and I am bored a great deal." {n}She sets the stone down on the sill, carefully, as though putting something back where it belongs.{/n} "That is more than most sailors get. It is also a debt, and it is yours."''',
        c("[Leave the stone where she put it.]", flags=(CREW,))),
    mz("threat", '''{n}She turns round on the sill and looks at you properly for the first time, and her eyes are two coals blown bright.{/n}
"A harpoon," {n}she says.{/n} "You." {n}She laughs so hard she nearly falls off the sill, and catches herself on the frame with a hand that for one heartbeat is a claw, and leaves four white scores in the wood.{/n}
"Yes. Come to my cave with a harpoon. I would like that very much. I will leave your ships alone until you do, so that you have a reason."''',
        c("[Look at the marks in the window frame.]", flags=(CREW,))),
    mz("harpoon", '''"Your captain." {n}She touches the welt beneath her ribs.{/n} "I went back to my island. He was drinking in the Midnight Isles, telling his harpoon story. Every time he told it I was bigger."
"I left a stone on his roof. He will be there when I go back." {n}She sets another stone beside your hand.{/n} "I can carry your answer. Write it large. I will be reading it from above his window."''',
        c('"He was following my order. He\'s under my protection."', "spare"),
        c('"Then eat him last. Last is a long way off."', "last")),
    mz("spare", '''{n}You score the order into her stone: the captain acted at your command; he is under your protection. She reads it, with her lip lifted.{/n}
"I have his roof. You have him." {n}She bares her teeth.{/n} "I will take the hook that was in my side. That is mine, and I will have it off his wall."
{n}When she returns from the Isles she brings the stone back, with a fresh line beneath yours: STILL ALIVE. She smells of tar and spilled beer, and the harpoon is over her shoulder, point and rope and all.{/n} "He shut the shutters. I listened anyway. He kept his arm, thief. He did not keep his hook. He made me smaller at the end, and I took the hook for it."''',
        c("[Let her have that.]", flags=(CREW, CAPTAIN_SPARED))),
    mz("last", '''"Last." {n}She smiles with every tooth.{/n} "Yes. I can leave a meal for later. Let him tell it while I hunt your rifts. When I go back to the Isles I want to hear how much bigger I have grown."''',
        c("Continue", flags=(CREW,))),
    mz("missed", '''"It got away from me." {n}She sounds aggrieved still.{/n} "Your sky-ship. Nothing gets away from me. I have been going over it and over it, every night: the clouds, the cliffs, the wind. It went down into the rocks where I do not fit, as if whoever was steering it knew exactly how big I am."
"Who was steering it, thief? I want to know. I want to go and look at them."''',
        c('"I landed it in the crevice."', "me"),
        c('"A captain who knows the Midnight Isles. That\'s all you\'re getting."', "secret")),
    mz("me", '''"You." {n}She stares at you, and then she giggles, high and delighted.{/n} "You made me go hungry, then came back with a gift. I did not even know it was the same thief." {n}She puts her chin on her knees.{/n} "I should eat you. I keep saying that. It keeps not happening."''',
        c("Continue", flags=(CREW,))),
    mz("secret", '''"That is all I am getting." {n}She scowls.{/n} "You keep things from me. Nobody keeps things from me. They are all inside me, eventually, and then I know everything they knew." {n}She stands up on the sill.{/n}
"Keep your captain, then. I will find him. I always find out. A man who can put a ship down in the one crevice I do not fit has a ship, and I will take the ship, hull and sail and all, and sleep on it. Or his arm, if he is slow about it." {n}She grins.{/n} "You said keep him. You did not say keep him whole."''',
        c("Continue", flags=(CREW,)))],
    requires=(), forbids=(CREW,))
SCENES[-1]["Nodes"].extend([
    mz("scream", '"That scream from your ship. I remembered it when I found the seal." {n}She leans close, grinning.{/n} "You have a very large throat for such a small thing. I have stopped wondering what it tastes like. For tonight."', c("Continue", flags=(CREW,))),
    mz("arrival", '"The island brought you to my cave. You could have taken my stones. Instead, I have your seal." {n}She holds it up beside your face.{/n} "I got the better cargo."', c("Continue", flags=(CREW,))),
])

visit(M + "beat.queen", "The thing in the swamp", [
    nar("start", '''{n}You come back to your quarters and find her sitting on your desk eating your candles, one after another, like sticks of sugar, in the dark she has made by eating them.{/n}
"I had news from my island," {n}she says, around a mouthful of tallow.{/n} "A harpy came through the hole. I ate it, and it told me everything first. Harpies always talk."''',
        c("Continue", "turned", requires=("melazmera.fq_betrayed",)),
        c("Continue", "fought", requires=("melazmera.queen_fought",), forbids=("melazmera.fq_betrayed",)),
        c("Continue", "withdrew", requires=("melazmera.queen_withdrew",), forbids=("melazmera.fq_betrayed", "melazmera.queen_fought")),
        c("Continue", "crowned", requires=(M + "queen_crowned",), forbids=(QUEEN_TURNED,)),
        c("Continue", "denied", requires=(M + "queen_refused_crown",), forbids=(QUEEN_TURNED, M + "queen_crowned", M + "queen_withheld")),
        c("Continue", "promised", requires=(PROMISED,), forbids=(QUEEN_TURNED, M + "queen_crowned", M + "queen_refused_crown")),
        c("Continue", "plain", forbids=(QUEEN_TURNED, PROMISED, M + "queen_crowned", M + "queen_refused_crown")),
        c("Continue", "withheld", requires=(M + "queen_withheld",), forbids=(QUEEN_TURNED, M + "queen_crowned"))),
    mz("crowned", '''"The thing in the swamp is wearing a rock on her head," {n}she says, delighted.{/n} "A grey rock, from your path. The harpy says it has sunk an inch into her and she will not let anyone near it, and she tells the whole island that the Knight Commander brought her a crown and that it shines." {n}She crunches another candle.{/n}
"You gave her a rock and called it a crown. I give thieves rocks and call them crowns. The difference is that she thanked you." {n}Her eyes gleam in the dark.{/n} "You are very cruel, thief. I did not know."''',
        c('"She was happy with it."', "happy"),
        c('"I learned it from you."', "learned")),
    mz("denied", '''"The thing in the swamp says you would not bring her my crown," {n}she says.{/n} "She says you told her it was a rock, to her face, and she sank to the bottom of her pool and sulked, and she is going to remember it when the island is hers." {n}She crunches another candle.{/n}
"You told the puddle the truth. Nobody tells the puddle the truth; it is not worth the breath." {n}She looks at you in the dark she has made.{/n} "Now she has two enemies on her island and one of them is in my hoard. She will not sleep for a hundred years."''',
        c('"She\'s back in her swamp. Let her keep it."', "dismiss"),
        c('"Take me with you when you go and look."', "ask")),
    mz("turned", '''"The thing in the swamp turned on you." {n}She sounds delighted.{/n} "She promised you her love and her affection and then she tried to drown you in her whirlpool, because she is too good for the likes of you. The harpy told me all of it. The harpy did the voice." {n}She does the voice too, wetly, and it is very good.{/n}
"Love and affection, and then a whirlpool. She should have offered you the whirlpool first. At least she owns one."''',
        c('"Leave the swamp out of it."', "dismiss"),
        c('"Next time, I\'ll ask you."', "ask")),
    mz("fought", '''"You fought the thing in the swamp." {n}She grins around a mouthful of tallow.{/n} "The harpy heard her screaming about her powafulness. It did the voice."

{n}She repeats the word in a wet, shrill gurgle.{/n} "I would have liked to hear it myself. I have never heard her say it while somebody was hitting her."''',
        c('"Leave the swamp out of it."', "dismiss"),
        c('"Next time, I\'ll ask you."', "ask")),
    mz("withdrew", '''"The thing in the swamp waved you off her island like a queen," {n}she says, delighted,{/n} "and then went down one of her holes and has not come up since. The harpy says she is sulking in a plague pit and telling the flies that you were her very best knight." {n}She does the voice, wetly, and it is very good.{/n}
"When she comes up again, she will find my cave empty and think she has won. I want to be there for her face. She does not really have one. I want to be there for the place where it would be."''',
        c('"She\'s back in her swamp. Let her keep it."', "dismiss"),
        c('"Take me with you when you go and look."', "ask")),
    mz("promised", '''"You promised the thing in the swamp my crown." {n}She sounds delighted.{/n} "The little one on the ledge. The harpy says she has been telling the whole island that the Knight Commander is bringing her a crown, and she has been practising wearing it with a pebble on her head." {n}She giggles.{/n} "It keeps sliding off. She does not have a head, really. She has a place where a head would go."
"You lied to her. To get into my cave." {n}The scarlet eyes gleam at you in the dark.{/n} "Good. She deserves lies. She has never told the truth in her life except by accident."''',
        c('"Maybe I\'ll send her a rock. She won\'t know the difference."', "rock"),
        c('"I\'d have lied to anyone to get into that cave."', "anyone")),
    mz("plain", '''"The thing in the swamp is telling everyone that the Knight Commander was her knight," {n}she says.{/n} "That the Knight Commander came to her in her cave and did everything she said and went away grateful, and that she is going to be queen of the whole island now that the fat lizard has gone." {n}She crunches another candle.{/n}
"I am the fat lizard." {n}She sounds more amused than offended.{/n} "She has been calling me that for years. When I am finished with your war, I am going to go back and sit on her swamp until it is dry."''',
        c('"Take me with you when you do."', "ask"),
        c('"Leave her be. She\'s harmless."', "keep")),
    mz("keep", '''"Harmless." {n}She licks tallow from her fingers.{/n} "She sent knights to be my supper for years and called it a present to herself. You can keep your pity. I have a cave on your side now."''',
        c("Continue", flags=(QUEEN,))),
    mz("ask", '''"Bring your steel, then." {n}She crunches the last candle.{/n} "I will bring my mouth. We can find something worth using both on. Not tonight. Your pickets have left me a warm trail."''',
        c("Continue", flags=(QUEEN,))),
    mz("rock", '''"A rock." {n}Her eyes light up like two coals blown on.{/n} "Yes. Send her a rock. Wrap it in something shiny. I will make it shine for you; I know how. She will wear it for a hundred years and tell everyone it is a crown, and everyone will see it is a rock, and nobody will tell her." {n}She sighs happily.{/n} "You are very cruel, thief. I did not know."''',
        c("Continue", flags=(QUEEN,))),
    mz("anyone", '''"To anyone," {n}she repeats.{/n} "To get into my cave." {n}She puts down the last candle and looks at you in the dark, and her eyes are the only light left.{/n} "Then you are a liar and a thief, and you went into a dragon's cave on a puddle's word, and you did not even take the crown." {n}She licks tallow off her thumb.{/n} "I am going to keep a very close watch on you."''',
        c("Continue", flags=(QUEEN,)))],
    requires=(QUEEN_MET,), forbids=(QUEEN,))
SCENES[-1]["Nodes"].extend([
    mz("happy", '"She thanked you for my bait." {n}Melazmera giggles, licking tallow off her thumb.{/n} "Next time she sends a knight, I shall ask him to bow to it."', c("Continue", flags=(QUEEN,))),
    mz("learned", '"You learned badly. I get a meal when somebody takes my crown. You got thanked." {n}She presses your seal into the candlewax on the desk.{/n} "Still. Her face. I wish I had seen her face."', c("Continue", flags=(QUEEN,))),
    mz("dismiss", '{n}She crunches the last candle, then drops its blackened wick onto your report.{/n} "Fine. I will not talk about your swamp. I did not say I would not sit on it. What is for supper?"', c("Continue", flags=(QUEEN,))),
    mz("withheld", '"You kept the crown where it belonged." {n}She laughs.{/n} "She sent a knight to rob me, and he defended my ledge. She will send a stupider one next time."', c("Continue", flags=(QUEEN,))),
])

visit(M + "beat.illusion", "The woman she wears", [
    nar("start", '''{n}She comes in over the sill in the woman she wears and sits down in your chair as if it were hers, and you sit on the end of your bed because it is the only other place, and look at her.{/n}
{n}Close to, in lamplight, the woman is very good. There is a pulse in her throat. There is a small scar on her chin. Her hair is black and heavy and moves when she moves. Only her shadow, going up the wall behind her and across the ceiling, gives the lie to her: it has a neck as long as a ladder.{/n}''',
        c('"Why this shape?"', "why"),
        c('"Why a rock, for a crown?"', "rock")),
    mz("why", '''"Because you are small. Your window is small. Your door is small. I could take the roof off, but then your priests would start ringing things." {n}She turns her hands over in her lap.{/n}

"I learned to fold myself down to enter the drowned king's hall. His doors were narrow. His crown was worth going in for. But a small dragon still looks like a dragon. So I wrap a woman round myself, as I wrap a crown round a rock."

{n}She smiles, showing the points of her teeth.{/n} "I wore her when I came to find you. The first time I stood on Drezen's walls, a sentry said good evening to me. He kept his spear on his shoulder. I could have eaten him before he lowered it."''',
        c("Continue", "edge")),
    mz("rock", '''"Because it is a rock." {n}She touches it, where it sits pressed into her hair, grey and pitted and ordinary.{/n} "I make rocks look like crowns so that thieves will take them. Everyone takes them. Everyone. So I wear a crown that looks like a rock, so that everyone who looks at me can see what I think of crowns." {n}She smiles.{/n}
"The thing in the swamp wanted my little crown more than anything in the world. I wanted her to see me wearing a rock and know that I could have worn anything." {n}She shrugs.{/n} "She hated it. I enjoyed that."''',
        c("Continue", "edge")),
    mz("edge", '''"Do you want to see the edge?" {n}She holds out her hand, palm up, across the space between the chair and the bed.{/n} "Here. Along the wrist."
{n}You take her hand. It is warm and dry and a little rough, a woman's hand, and then as your fingers move towards her wrist there is a place where the warmth stops, abruptly, as if you had put your hand out of a window into winter, and under your fingertips the skin is not skin but plate, hard and smooth and cold, a patch of it the size of a coin.{/n}
"That is me," {n}she says.{/n} "Folded small, but me. The picture stops there. It always stops somewhere; I can never find where until somebody touches it."''',
        c('"Show me the rest of you. Here."', "show"),
        c("[Keep your hand where it is.]", "stay")),
    mz("show", '''{n}She looks at you for a heartbeat. Then she lets go of the woman's face, and only the face.{/n}
{n}It does not change so much as stop pretending. What sits in your chair is still folded small, but it is not a woman: a long dark head on a long neck, purple plate, a jaw that hangs over your desk, scarlet eyes level with yours and lit from inside, and the breath that comes out of her smells of cold iron and old fire. The candle leans away from her until it goes out. Her horns scrape the ceiling, and plaster sifts down onto your maps.{/n}
"This is me," {n}she says, with a voice that makes the window rattle.{/n} "Look properly. People usually only see this once."''',
        c("[Look properly.]", "after_shown"),
        c("[Put your hand on her jaw.]", "after_shown")),
    mz("stay", '''{n}She leaves her hand in yours, the woman's hand, and the cold claw under your fingertips, and does not take either away. After a while she turns her hand over so that your fingers lie along the inside of the wrist that is not there, and closes her eyes.{/n}
"There. Keep your fingers on the plate," {n}she says.{/n} "The skin is warm. Under it, that cold plate is mine. Move them further, and you will feel the claw." {n}She opens her eyes, and they are all red, with no white in them at all, and very close.{/n} "Be careful with that. People who find where I stop lying usually find out what I am, and then they are over."''',
        c("Continue", "after_held")),
    nar("after_shown", '''{n}When she has gone, back out of the window with a sound like a sail filling, you find a long pale scar in the plaster of the ceiling where her horns went, and a fine dust of it over your maps, and on the arm of your chair four white scores in the wood where something with claws held on while it was not being a woman.{/n}
{n}You do not have the chair mended.{/n}''',
        c("Continue", flags=(ILLUSION,))),
    nar("after_held", '''{n}When she has gone, back out of the window with a sound like a sail filling, there is a mark on the palm of your hand the size of a coin, red and tight, like a burn from something very cold. It is gone by morning.{/n}
{n}The arm of your chair, where her wrist lay, is rimed with frost until noon.{/n}''',
        c("Continue", flags=(ILLUSION,)))],
    requires=(FED,), forbids=(ILLUSION,))
next(x for x in SCENES[-1]["Nodes"] if x["Id"] == "after_shown")["EnterSet"] = [M + "cost.chair_scores"]

visit(M + "beat.souls", "Even dead souls", [
    nar("start", '''{n}She is lying along the ridge of the roof in her own shape when you climb out onto the leads, with her chin on the chimney stack and her eyes half closed, and she does not move when you come up beside her.{/n}
"Somebody died," {n}she says.{/n} "Down there, in your hospital. Just now. I felt it go past." {n}Her nostrils flare.{/n} "A soldier. Young. He was frightened and then he was not. He is going somewhere a long way off, very fast, and he tastes of salt and wet wool, and a girl he did not tell."''',
        c('"You sound as if you\'ve eaten souls. Even dead ones."', "boast"),
        c('"Leave him alone."', "leave")),
    mz("leave", '''"I am leaving him alone." {n}She sounds offended.{/n} "He is not mine. He is going to your grey lady at the end of the long line. She is very strict about her line. You take one out of it and she notices, and she sends things." {n}One eye opens and looks at you.{/n} "I have taken from the end of her line where she was not looking. Not in your city. Not him."''',
        c("Continue", "boast")),
    mz("boast", '''"It is not boasting if it is true." {n}She rolls onto her side along the ridge, and the slates crack under her.{/n} "I was hatched where the light goes thin, on the far side of the dark, where the dead go past like fish in a river. Everything there eats a little of the dead; it is the only food. When I came to the Abyss I found the dead there were bigger, and angrier, and they did not go past; they stayed and turned into demons. So I ate the demons."
"A soul tastes of whatever it was most. A paladin tastes of salt and lightning. A demon tastes of ash and the thing it wanted. The thing in the swamp tasted of nothing at all. That is why I spat her out."''',
        c('"What would mine taste of?"', "mine"),
        c('"You won\'t touch the dead of this crusade. Not one."', "forbid")),
    mz("mine", '''{n}She lifts her head off the chimney and brings it round until one eye is a foot from your face, and looks into you for a long, slow breath. You can feel her looking; it is like standing too near a cold oven.{/n}
"Burnt sugar," {n}she says at last.{/n} "And iron. And a joke nobody laughed at." {n}She puts her head back on the chimney.{/n} "When you die, thief, give it to me. Do not send it down the long line to the grey lady. I will keep it on the heap, with the seal, and the stones, and count it every night."''',
        c('"No. It goes where everyone\'s goes."', "no"),
        c('[Lie] "It\'s yours."', "lie"),
        c('"Ask me when the war is over."', "later")),
    mz("forbid", '''{n}She is quiet for so long that you think she has gone to sleep. Then she says, without opening her eyes:{/n} "Not one."
"They go down very fast, your soldiers, and nobody is eating them, and it is a waste. But not one." {n}The tip of her tail moves on the slates, once, like a cat's.{/n} "If I eat your dead, your priests will come for me with their bells, and you will have to choose between us, and you might choose badly. You are worth more to me than a soldier. Even a young one." {n}One eye opens.{/n} "Yours, thief. The ones that come up out of the hole already dead are not yours, and I will take those without asking."''',
        c("Continue", "mine")),
    mz("no", '''"Where everyone's goes." {n}She snorts, and smoke curls up past the chimney.{/n} "To be weighed by a grey lady and sent to a place you did not choose. You would rather that than my heap." {n}She sounds more puzzled than hurt.{/n} "Then keep it. But I will be at the end of her line when you get there, thief, and I will watch you go past, and I will be very rude to her about it."''',
        c("Continue", flags=(SOULS, SOUL_REFUSED))),
    mz("lie", '''{n}She opens both eyes, and looks at you, and then she laughs, low and long, until the roof trembles.{/n}
"That was a lie," {n}she says, pleased.{/n} "I can taste lies. They taste of copper. Everyone lies to me to stop me eating them. You lied to me so that I would be pleased." {n}She puts her head back down.{/n} "I am going to keep that lie on the heap. That one cost you nothing. I will keep it anyway."''',
        c("Continue", flags=(SOULS, SOUL_LIED))),
    mz("later", '''"When the war is over." {n}She considers the Wound, glowing along the north like the cracks in a black loaf.{/n} "Your war will be over when you are at the bottom of that hole. You will be very busy. You will not remember to answer." {n}One eye rolls towards you.{/n} "I will remember for you. Dragons are good at waiting. We are the best in the world at it."''',
        c("Continue", flags=(SOULS,)))],
    requires=(FED,), forbids=(SOULS,))

visit(M + "beat.seal", "The new seal", [
    nar("start", '''{n}The engraver has finished your new seal, and it lies on your desk in the morning in a little box lined with red cloth: heavier than the old one, a little too big for your finger, with the device of the crusade cut into it deep and sharp. Your clerks are pleased with it. The chancellery will need three weeks to send out word of the change to every commander on the Wound.{/n}
{n}That night there is a stone on your windowsill, and in the clay on its corner, sharp and clean, the old seal, pressed in so hard the clay has cracked.{/n}''',
        c("Continue", "stone")),
    mz("stone", '''"THIEF.
YOUR CLERKS HAVE CUT YOU A NEW RING. I WATCHED THEM THROUGH THE WINDOW. IT IS UGLY AND TOO BIG. THE OLD ONE IS BETTER. THE OLD ONE IS MINE.
WHAT ORDERS DID THE OLD ONE GIVE? TELL ME ALL OF THEM. I WANT TO KNOW WHAT IS ON MY CLAW.
M."''',
        c("Continue", "visit")),
    nar("visit", '''{n}She comes for the answer herself, the next night, in the woman she wears, and sits on your windowsill with her legs hanging down outside over three storeys of air, and holds out her hand so that the old ring glitters in the lamplight.{/n}''',
        c('"It gave a lot of orders. Some of them killed people. Most of them saved more."', "orders"),
        c('"I want it back."', "back"),
        c('"Keep it. The new one\'s only for the clerks."', "keep")),
    mz("orders", '''"Some of them killed people." {n}She turns the ring on her finger, looking at it with new interest.{/n} "That is the most interesting thing you have ever told me about it." {n}She holds it to her ear, as though it might speak.{/n}
"I thought it was jewellery. It is a claw. You wore a claw on your hand and every time you pressed it into wax, somebody went and died on it somewhere." {n}Her eyes gleam.{/n} "And you gave it to me. You gave me your claw. Oh, thief. I did not know it was that kind of present."''',
        c("Continue", flags=(SEAL_LEFT,))),
    mz("back", '''{n}She pulls her hand back against her chest so fast that the window frame creaks, and for a heartbeat her fingers are claws and her eyes are all red, with no white in them at all.{/n}
"No." {n}She says it very softly.{/n} "Things in my hoard do not leave. I told you when we met. You brought it into my cave. I kept it. It stays with me."
{n}Then, slowly, the claws are fingers again, and she looks at you with something like delight.{/n} "You asked, though. You wanted it back and you asked, in my hearing, with my claw a foot from your throat." {n}She holds the ring up to the lamp.{/n} "Ask again whenever you like. I enjoy saying no to you."''',
        c("Continue", flags=(SEAL_ASKED,))),
    mz("keep", '''"Only for the clerks." {n}She considers the ring on her finger, and then you.{/n} "So the new one says what you tell it, and the old one says what I tell it." {n}She smiles, slowly.{/n} "I have been pressing it into every stone I send you. I have been pressing it into the goats before I eat them. I pressed it into a vrock on the Wound's edge. He did not like it."''',
        c("Continue", flags=(SEAL_LEFT,)))],
    requires=(SEAL,), forbids=(SEAL_ASKED, SEAL_LEFT))

visit(M + "beat.greybor", "The little man with the axe", [
    nar("start", '''"The little man with the axe," {n}she says as she comes over the sill and sits on your desk.{/n} "Grey beard. Very cross."''',
        c("Continue", "him")),
    mz("him", '''"He bit my coin." {n}She says it with enormous satisfaction.{/n} "Everyone else in your city looked at my crown, or at my face, or at the ground. He looked at my shadow first, then my hands, then my coin, and then he bit it. He is the only person in your whole city who looked at the right things in the right order."
"How much does he cost? I want him. Not to eat. To keep. He could stand at the mouth of my cave and look at thieves in the right order, and bite their coins, and tell me which ones to eat."''',
        c('"He\'s not for sale. He\'s mine."', "mine", flags=(M + "beat.greybor_claimed",)),
        c('"Ask him yourself. Bring more coin."', "ask"),
        c('"He\'d charge you by the thief."', "charge")),
    mz("mine", '''"Yours." {n}Her eyes narrow, and she looks at you, and then out of the window towards the gate, as though weighing something.{/n} "You keep him, then. The way I keep things." {n}She sniffs.{/n} "Fine. I will not take him. But I will know where he is, all the time, and when you are not using him, I will borrow him to look at thieves."''',
        c("Continue", flags=(AXE,))),
    mz("ask", '''"More coin." {n}She considers it, frowning.{/n} "I have a great deal of coin, from the drowned country, but it is square and nobody can spend it. He did not mind. He bit it and put it in his boot." {n}She laughs.{/n} "Yes. I will bring him a whole sack, and ask him properly, the way you ask. He will say no. I know he will say no. I want to hear how he says it."''',
        c("Continue", flags=(AXE,))),
    mz("charge", '''"By the thief." {n}She repeats it with the air of a scholar learning a new word in an old language.{/n} "A coin for each thief he looks at. And I eat the thief, and I keep the coin, and so the thief pays for the looking." {n}She claps her hands together.{/n} "That is the best idea anyone in your city has had. I am going to tell him it was mine."''',
        c("Continue", flags=(AXE,)))],
    requires=(GREY_CARRIED, FED), forbids=(AXE,))

visit(M + "beat.dinner", "What giving is", [
    nar("start", '''{n}There is something on your desk when you come up from the war council, on your best map, steaming. It is roughly the size of a cartwheel and roughly the shape of a heart, and it is dark red going on black, and it is still moving, slowly, like a bellows somebody has stopped working.{/n}
{n}She is sitting in your chair in the woman she wears, with one boot up on the edge of your desk beside it, cleaning a claw that is only half a fingernail, and she watches you find it the way a cat watches you find the bird on the step.{/n}''',
        c("Continue", "gift")),
    mz("gift", '''"It is a heart," {n}she says.{/n} "From a thing with six arms and a crown of bone that came up out of the hole last night and wanted to eat your pickets. I ate it instead. I kept you the best part."
"You gave me a ring. A ring is a very small thing, thief, a thing a clerk could carry. This is a gift." {n}She lets the word sit there, pleased with the size of it.{/n} "It is still warm. It will be warm for days. Things like that do not know when to stop. Eat it, and let me watch what you are made of. Or do not, and let me watch that."''',
        c("[Cut a slice and eat it.]", "eat"),
        c('"Thank you. I\'ll... have the cook do something with it."', "cook"),
        c('"People don\'t give each other hearts. Not like this."', "teach")),
    nar("eat", '''{n}You take your knife and cut a slice off the edge, where it is least alive, and put it in your mouth, and chew.{/n}
{n}It tastes of iron and pepper and burning hair, and it fights you all the way down, and when it gets where it is going it sits there like a coal. For the rest of the night you are very warm, and very awake, and every sound in the citadel is much too loud, and you can see in the dark rather better than you ought to.{/n}''',
        c("Continue", "ate")),
    mz("ate", '''{n}She watches your throat as you swallow. Then she comes round the desk and catches your chin between fingers that have not quite stopped being claws.{/n}

"Open your mouth." {n}She smells your breath and grins.{/n} "There. Iron. Better than your salt pork."

{n}She bites a piece from the heart without letting go of your chin.{/n} "Next time I will bring you something that fights harder."''',
        c("Continue", flags=(DINNER, DINNER_EATEN))),
    mz("cook", '''"The cook." {n}She looks at the heart and then at you, and for a heartbeat the woman's face is not quite a woman's, and the lamp gutters.{/n} "I gave it to you. Not to the cook."
{n}Then she laughs.{/n} "No. You are right, and I hate it. When you left your ring with me, it was mine, to eat or wear or sleep on. This is yours, to feed to a cook if you like." {n}She works it through like a sum she does not care for.{/n} "Fine. Tell the cook it will bite. I will be listening, and I will want to know which finger."''',
        c("Continue", "cook_after")),
    nar("cook_after", '''{n}It does bite. The cook loses the end of a finger to it before he gets it into the pot, and the stew he makes of it is so hot that the men who eat it do not sleep for two nights, and fight a skirmish on the north road on the third that the sergeants still talk about. Nobody asks where the meat came from. Several of them ask for more.{/n}''',
        c("Continue", flags=(DINNER,))),
    mz("teach", '''"Not like this." {n}She looks at the heart, puzzled.{/n} "How, then? What do people give each other?"
{n}You try to tell her. Flowers; she has eaten flowers. Rings; she has one of yours. Letters; she has been sending you stones. Bread, a coat, a night's watch, a promise. She listens to all of it with her head on one side, frowning, as if you were describing the customs of a country under the sea.{/n}
"Those are very small things," {n}she says at last, with contempt.{/n} "Things that fit in a hand. Things that can be taken back. Your people give each other small things so that they can take them back." {n}She pats the heart, which shudders.{/n} "This one is dragon-size. Nobody takes it back. You will grow into it, or you will not, and either way I will know something about you."''',
        c("Continue", flags=(DINNER,)))],
    requires=(FED,), forbids=(DINNER,))

letter(M + "stone.shield", "A stone and a shield", [
    nar("start", '''{n}In the morning there is a shield propped against the wall under your window, three storeys down in the yard, as though somebody had leaned it there to go for a drink. It is round and black and scorched, and painted on its face is Deskari's locust, and the arm-straps on the back are still buckled round what is left of an arm.{/n}
{n}On your windowsill is a stone.{/n}''',
        c("Continue", "words")),
    mz("words", '''"THIEF.
A MAN CAME UP OUT OF THE HOLE LAST NIGHT WITH A FLY ON HIS SHIELD AND FORTY MORE BEHIND HIM. THEY WERE GOING TO YOUR PICKETS ON THE NORTH ROAD. THEY WERE FAT.
THEY ARE NOT GOING TO YOUR PICKETS NOW.
I KEPT YOU THE SHIELD. I DO NOT KNOW WHAT YOU DO WITH SHIELDS. PUT IT IN YOUR HOARD.
M."''',
        c("[Have the shield hung in the hall.]", flags=(SHIELD,)),
        c("[Have it burned, and the arm buried.]", flags=(SHIELD,)))],
    requires=(FED,), forbids=(SHIELD,), delay=36)

visit(M + "beat.count", "The Commander's hoard", [
    nar("start", '''{n}She comes in over the sill and does not sit down. She walks round your quarters instead, slowly, in the woman she wears, touching things: the sword on its hooks, the maps on the desk, the stones she has sent you in a row along the shelf, the arm of your chair, the bed.{/n}
"I am counting your hoard," {n}she says, when you ask.{/n} "You counted mine. You know what is real in it. It is only fair."''',
        c("Continue", "count")),
    mz("count", '''"One sword. Real. It has killed things." {n}She touches it with one finger and takes the finger away quickly, as if it were hot.{/n} "Maps. Not real. They are pictures of places that are not there any more; the war has eaten them. Your stones: real. All of them are mine, so they are real." {n}She stops at the bed and looks at it for a long breath.{/n}
"And letters. From other people." {n}She sniffs them, a whole drawer of them, without opening a single one.{/n} "They are real too. I do not like them. I am not going to eat them." {n}She shuts the drawer, very gently.{/n} "Your hoard is badly kept, thief. Everything in it is from somebody else."''',
        c('"Everything in yours is from somebody you ate."', "ate"),
        c('[Take the sapphire out of your pocket and put it on the shelf with her stones.]', "sapphire", requires=(STONE_KEPT,))),
    mz("ate", '''"Yes. And none of them came back to ask for it." {n}She sits on the edge of your bed and looks at the sapphire in your pocket.{/n} "Forty stones on the heap. One there. One seal. One Commander."

{n}Her hand closes over the stone through the cloth.{/n} "You were still there when I woke. I counted twice."''',
        c("Continue", flags=(COUNTED,))),
    mz("sapphire", '''{n}You put the grey stone on the shelf, at the end of the row of her letters, where it looks like one more of them.{/n}
{n}She stares at it. Then she comes and picks it up, and weighs it in her palm, and puts it back into your pocket herself, and pats it flat.{/n} "No. That one does not go on the shelf. That one goes where it goes. That is the one you took." {n}Her hand stays flat against you.{/n}
"The others are things I gave you. That one is a thing you stole, and I let you." {n}She sounds very serious.{/n} "It is the most important thing in your hoard. Do not put it with the letters."''',
        c("Continue", flags=(COUNTED,)))],
    requires=(HEAP,), forbids=(COUNTED,))

visit(M + "beat.war", "Not in anybody's lines", [
    nar("start", '''{n}The crusade is making ready for the last push. You can hear it all over the citadel even at night: carts in the yard, hammering in the smithies, sergeants shouting at men who already know what they are doing. When you climb out onto the roof to get away from it she is there, along the ridge, watching the Wound with her chin on the chimney.{/n}
"You are going down the hole," {n}she says, without looking round.{/n} "All of you. I can smell it on the whole castle. Iron and fear and prayers."''',
        c("Continue", "lines")),
    mz("lines", '''"I will not come." {n}She says it flatly, as a fact about the weather.{/n} "I do not fight in anybody's war. I do not stand in lines, and I do not go where I am told, and I do not get into holes where there is no room to turn round. I am a dragon. Dragons who go to wars end up on the walls of castles, stuffed, with a little brass plate."
{n}Then her eye rolls round to you.{/n} "But I will be at the edge. All of it. Everything that comes up out of the hole behind you, while you are going down it, will find me there first. I am not fighting for you, thief. I am eating near you. It is different."''',
        c('"It\'s enough."', "enough"),
        c('"Come down the hole with me."', "come"),
        c('"If I don\'t come back up..."', "if")),
    mz("enough", '''{n}She lowers her head beside you. Cold breath works beneath your collar.{/n} "Come back with your talking still in you. I want it in my cave. I want your hands on me, thief, and the stone where I can find it."''',
        c("Continue", flags=(WAR,))),
    mz("come", '''{n}She laughs, very softly for her, so that only the slates shake.{/n} "No." {n}She says it almost gently.{/n} "You asked, and I said no, and you are still standing there. That is something. Everything else I ever said no to, I ate."
"Go down your hole. Do what you do. Come back up with your talking still in you." {n}Her eye closes and opens.{/n} "I will be counting."''',
        c("Continue", flags=(WAR,))),
    mz("if", '''"Then I will come and get what is left and put it on the heap." {n}She does not even pause.{/n} "I told you that already. On the heap, in my cave, under my crown. I do not say things twice unless I want them to be true twice." {n}Her tail moves on the slates.{/n}
"Do not make me do it, thief. I would do it. I would not like it. I would never forgive you, and I have a very long time not to forgive in."''',
        c("Continue", flags=(WAR,)))],
    requires=(COMMITTED, HEAP), forbids=(WAR,), delay=36)


# --- Chapter 4, on Colyphyr: the Queen asks, and the old cave by daylight. ------------------------------------------------

QUEEN_HUB = "a39dd7d45c635304f9e8404c78a340c3"   # FulsomeQueen/AnswersList_0003 (her hub before Hepzamirah falls)


def queen(id, text, *choices):
    return n(id, "conversant", text, *choices)


SCENES.append(scene(M + "ch4.queen_after", "Where is my crown?", "Melazmera", 4,
    '"I went into the dragon\'s cave."', [
    queen("start", '''{n}The Fulsome Queen rears up out of her filth so fast that a wave of it slops over the lip of her pool.{/n}
"I know! I know you did! The whole island knows! The fat lizard came home and she did not roar, and she did not spit, and she did not come and chew anybody!" {n}Her borrowed face is working with something between terror and greed.{/n} "And you are not dead! Why are you not dead? Everybody who goes into that cave is dead!"''',
        c('"I didn\'t take anything. That\'s the trick."', "trick"),
        c('"She came to my fire and ate my supper. We talked."', "talked", requires=(RETURNED,))),
    queen("trick", '''"You did not take anything." {n}She repeats it slowly, the way she might repeat a word in a language she has decided not to learn.{/n} "Then what was the point of going in?"
{n}She thinks about it. You watch her think about it; it takes a while, and it bubbles.{/n} "Oh! Oh, you are so cunning! You did not take anything yet. You are waiting until she trusts you. And then you will take everything, and she will not even come home, because she will think it is a present!" {n}She hugs herself, wetly.{/n} "That is almost as clever as me. Almost."''',
        c("Continue", "crown")),
    queen("talked", '''"Talked." {n}The Queen goes so still that the flies land on her.{/n} "She does not talk. She eats. She ate my knights. She ate my slaves. She chewed me." {n}Her voice climbs to a wail.{/n} "She only ever talked to me about eating me! She never sat and listened! I am the Queen! I am much more interesting than you!"
{n}Then, abruptly, she is sly again.{/n} "Did she say anything about me? She did. She said I was beautiful. She said she was sorry she chewed me." {n}She does not wait for an answer.{/n} "I knew it. Everybody is sorry, in the end."''',
        c("Continue", "crown")),
    queen("crown", '''"So." {n}She sways towards you, and the smell comes with her.{/n} "Where is my crown?"''',
        c('[Hand her a rock from the path] "Here. It only looks like a rock. That\'s the illusion."', "rock",
          requires=(PROMISED,)),
        c('"It was a rock, your majesty. Everything in that cave that shines is a rock. You said so yourself."', "truth"),
        c('"The crown stays with the dragon."', "withhold", forbids=(PROMISED,)),
        c('"I promised. I am keeping it with the dragon anyway."', "withhold", requires=(PROMISED,))),
    queen("rock", '''{n}She takes the rock in both hands, with enormous reverence, and holds it up to her face and peers at it, and then, very slowly, puts it on her head, where it sinks an inch into her and stays there.{/n}
"It is very heavy," {n}she whispers.{/n} "Crowns are heavy. Nocticula says so. I heard her say so." {n}She turns her head carefully from side to side to show you.{/n} "Is it shining? I cannot see it. Tell me it is shining."''',
        c('"It\'s shining."', "shining"),
        c('"Like the Lady in Shadow herself."', "shining")),
    queen("shining", '''{n}She shivers all over with joy, and a smell of rotting lilies goes up from her like steam.{/n}
"I knew it. I knew you were my knight." {n}She settles back into her pool, very carefully, holding her head still so the rock will not fall off.{/n} "Go away now, knight. The Queen is going to sit here and be beautiful for a while. Do not tell the fat lizard. She will want it back."''',
        c("[Leave her with her crown.]", flags=(M + "queen_crowned",))),
    queen("truth", '''"A rock." {n}Her face crumples. For a moment she looks like nothing so much as a child whose sweet has been dropped in the mud, and then, horribly, like a child who has decided whose fault that was.{/n}
"Everybody takes and nobody brings," {n}she says, in the small drowning voice.{/n} "I will remember that you did not bring. Queens remember. I will remember it when the horned bitch is dead and the island is mine, and you are standing where I can reach you." {n}She sinks down until only her eyes are above the filth.{/n} "Go away."''',
        c("[Go away.]", flags=(M + "queen_refused_crown", M + "queen_truth_told")))],
    requires=("trickster.ever", SALTED), forbids=(DEAD, QUEEN_TURNED, M + "queen_crowned", M + "queen_refused_crown",
                                                  CLOSED),
    last=4, Relationship=REL, Chapters=[4], optional=True, AnswerLists=[QUEEN_HUB], ReturnToList=True,
    ReturnText="{n}The Fulsome Queen wobbles in her pool, watching you with small wet eyes.{/n}"))
tag(M + "ch4.queen_after")
SCENES[-1]["Nodes"].append(queen("withhold", '"With the lizard! My knight leaves the crown with the lizard!" {n}The Queen splashes filth over the rim of her pool.{/n} "Go away! I shall find a knight who knows whom to rob!"', c("[Go away.]", flags=(M + "queen_refused_crown", M + "queen_withheld"))))


SCENES.append(scene(M + "ch4.old_hoard", "The cave with the hole in its roof", "Melazmera", 4, "", [
    nar("start", '''{n}She comes for you at the next rest on the island, not to the fire but to the edge of the camp, in the woman she wears, with rain running off the rock on her head, and crooks one finger. You follow her. Your sentries watch you go, and nobody tries to stop you, and one of them makes the sign of Iomedae behind your back.{/n}
{n}She takes you to the cave. She walks in by the front, between the bait's shelves, without looking at any of them.{/n}''',
        c("Continue", "crown")),
    mz("crown", '''{n}She takes the bait from its ledge and holds it up. A crown shines between her fingers. She rolls it over, and it is a plain rock. Another turn, and the crown shines again.{/n}

"My rock. My trick." {n}She sets it at the far end of the ledge, away from the heap.{/n} "There. Keep your sleeve clear of it. I would hate to eat you for a careless sleeve."''',
        c("Continue", "rain")),
    mz("rain", '''{n}She walks to the middle of the cave, where the rain comes down through the hole in the roof in its grey column, and stands in it with her face turned up, and lets it run over her.{/n}
"This is why I took this cave," {n}she says, with her eyes shut.{/n} "The thing in the swamp had it first. She tells everyone I threw her out because I would not fit in the other caves. That is true. But it is not why." {n}She opens her mouth and lets the rain fill it and swallows.{/n} "Where I was hatched, there is no rain. Only the dark, and things going past in it. The first time I felt this on my face, I ate everything on the island that was standing between me and it. Including her, a little."''',
        c('"Show me the real treasure."', "heap"),
        c("[Step into the rain beside her.]", "beside")),
    mz("beside", '''{n}You step into the column of rain. It is cold and heavy and it hits the top of your head like a flat hand. She opens one eye and looks at you standing in it, soaked in a breath, blinking.{/n}
"That is my rain," {n}she says.{/n} "You are standing in it." {n}She shuts the eye again.{/n} "Stay there. I have not decided if I mind."''',
        c("Continue", "heap")),
    mz("heap", '''{n}She takes you to the heap at the back and kneels by it, and begins to take stones off it, one at a time, and lay them on the floor in front of you in a row.{/n}
"The eye of a statue from a temple that fell in the sea. A ruby that a lord in the Isles swallowed to keep it from his brother; I ate the lord. A lump of star." {n}She holds up something grey and pitted that is heavier than it should be; you can see it weigh down her hand.{/n} "It came down in the sea and a fisherman brought it up in his net, and I ate the net, and the fisherman, and then I had it."
"Forty-one. I know every one of them. A kobold tried to keep the blue one under his tongue. I got it back." {n}She holds her hand out flat over the row, as if warming it.{/n} "You are looking at them without a blade in your hand. Look. Remember them."''',
        c("[Look at them one by one, and remember.]", "ring"),
        c('"Where\'s my ring?"', "ring")),
    mz("ring", '''{n}She lifts her left hand, where the seal rattles on her smallest finger.{/n}
"Here," {n}she says.{/n} "Not on the heap. I tried it on the heap, for a night, and I could not sleep. It kept being warm. The others are warm from me. That one was warm from you, from inside your hand, and it would not stop." {n}She makes a fist round it.{/n} "So I wear it. It does not fit. I do not care."
{n}She puts the stones back on the heap one by one, in exactly the places they came from, and you realise she knows every one of those places the way you know the rooms of a house you grew up in.{/n}''',
        c("Continue", "out")),
    nar("out", '''{n}She walks you back to the edge of camp before the rain stops. At the last rock she stops, and turns, and puts out her hand and touches your wet face with two fingers, once, the way she touched the stones on the heap, as if to see what was real.{/n}
"There is a hole in your world," {n}she says.{/n} "I can smell it from here. Things come up out of it warm." {n}She takes her fingers away.{/n} "I am thinking about it, thief. Go to sleep."''',
        c("[Go to sleep.]", flags=(M + "old_hoard_seen",)))],
    requires=("trickster.ever", RETURNED), forbids=(DEAD, CLOSED, M + "old_hoard_seen"), last=4, optional=True,
    Relationship=REL, Remote=True, Kind="visit", Chapters=[4], Areas=["c876d5303f4a19f4a80b0cc9b313db6f"]))
tag(M + "ch4.old_hoard")


# --- Chapter 5: the rain, the joke, the drowned king. --------------------------------------------------------------------

visit(M + "beat.rain", "Rain over Drezen", [
    nar("start", '''{n}A hard cold rain falls over Drezen, and at midnight there is a sound on your roof like a cart being unloaded, and then nothing.{/n}
{n}You find her on the leads in the woman she wears, standing in the downpour with her face turned up and her arms held a little out from her sides, soaked through, with the rain running off the rock on her head and down her neck and into her gown, which does not get wet, because it is not there.{/n}''',
        c("Continue", "rain")),
    mz("rain", '''"There is no rain in my new cave," {n}she says, without looking at you.{/n} "There is no hole in the roof. There is a crack in the world with fire at the bottom, and it is warm, and things come up out of it, and I eat them. It is a very good cave. But nothing ever falls into it from the sky."
{n}She wipes her face with both hands, and laughs, and the rain runs into her mouth.{/n} "I heard it on your roof. I was on the Wound's edge, and I heard it start, and I came."''',
        c('"You could have stayed on Colyphyr. It rains there every night."', "stayed"),
        c("[Stand in it with her.]", "stand")),
    mz("stayed", '''"I could have." {n}She catches your collar and draws you into the downpour.{/n} "But my seal was here. So was the hand I took it from."
{n}She rubs rain from your cheek with her thumb, then pushes your head back beneath the falling water.{/n} "You are shivering already. Stay until I am finished."''',
        c("Continue", "stand")),
    nar("stand", '''{n}You stand in the rain with her on the roof of the keep until you are wet to the skin and your teeth are chattering, and she does not seem to feel it at all. Below you the yard fills with puddles. A sentry on the gate-tower has put his cloak over his head and is pretending very hard that there is nobody on the roof.{/n}
{n}After a while she takes your hand, the woman's hand round yours, cold and wet, and does not say anything, and holds it up to the sky, palm up, as if to see how much it will hold.{/n}''',
        c('"It doesn\'t hold much."', "hold"),
        c("[Let her hold it.]", "hold")),
    mz("hold", '''"No," {n}she agrees.{/n} "Your hand is very small. It holds almost nothing." {n}She tips it, and the rain runs off it, and she watches it go.{/n} "It brought a ring into my cave. I still have that ring. Let your hand be small; it did well enough."
{n}She lets go, and goes to the edge of the roof, and steps off it, and a moment later something enormous goes up past the gate-tower in the rain, and the sentry drops his cloak.{/n}''',
        c("Continue", flags=(M + "beat.rain_stood",)))],
    requires=(FED,), forbids=(M + "beat.rain_stood",))

visit(M + "beat.joke", "The one who makes jokes", [
    nar("start", '''{n}She is sitting in your chair when you come in, with her feet up on your desk and one of your reports in her hand, upside down. She is not reading it. She is looking at the seal on it, the new one, with the expression of a woman who has found a hair in her soup.{/n}
"Your soldiers say you are the one who makes jokes," {n}she says.{/n} "In the barracks. I listened at the window. They say the Knight Commander makes jokes in the worst places: on the walls, at the head of a charge, over a grave. They are all very frightened of you, and they laugh about it a great deal." {n}She puts the report down.{/n} "Tell me one."''',
        c('"What do you call a dragon who gives things away?"', "riddle"),
        c('"I\'m not the one who laughs. Other people do that."', "laughs")),
    mz("laughs", '''"Other people." {n}She tilts her head.{/n} "I do not laugh at jokes either. I laugh when things are funny. A goat running the wrong way, into my mouth. A paladin who says foul beast and then touches my crown. The thing in the swamp trying to be beautiful."
"You are the one your soldiers say makes jokes. So make one. If it is bad I will eat your candles."''',
        c('"What do you call a dragon who gives things away?"', "riddle")),
    mz("riddle", '''"I do not know." {n}She frowns at you, as if it were a riddle with a prize at the end and she meant to have the prize.{/n} "A dragon who gives things away is not a dragon. So it is nothing. You call it nothing." {n}She folds her arms.{/n} "That is not funny. What do you call it?"''',
        c('"A lizard. A very fat lizard."', "joke")),
    mz("joke", '''{n}She stares at you with her mouth open. The fat lizard: the thing in the swamp's word for her, whined across a whole island for years.{/n}
"That is not a joke," {n}she says.{/n} "That is a slander. That is the puddle's word." {n}And then she laughs, so hard she has to hold on to the arm of your chair, and four white scores appear in it that were not there before.{/n}
"I am going to keep it," {n}she says, when she can.{/n} "The next knight the puddle sends into my cave, I am going to let him get his hand on the crown, and then I am going to come home and put my head down beside him and ask him what you call a dragon who gives things away. He will not know. I will tell him. And then I will eat him, and he will die not understanding it, and that will be the funniest thing that has ever happened on my island."''',
        c("Continue", flags=(M + "beat.joke_told",)))],
    requires=(FED,), forbids=(M + "beat.joke_told",))
next(x for x in SCENES[-1]["Nodes"] if x["Id"] == "joke")["EnterSet"] = [M + "cost.chair_scores"]

visit(M + "beat.drowned_king", "The drowned king's stone", [
    nar("start", '''{n}She comes in over the sill and holds out her hand without a word, and you know what she wants. You take the grey stone out of your pocket and put it in her palm. She does not keep it. She turns it over and over, and then gives it back, and sits down on the floor with her back against your bed, in the woman she wears, with her long legs stretched out across half the room.{/n}
"You know which crown it came from," {n}she says.{/n} "But I have not told you what became of the king."''',
        c('"Where did it come from?"', "story"),
        c('"I know what it\'s worth. You told me: it\'s the one I took."', "worth")),
    mz("worth", '''{n}She looks up at you from the floor, and for a moment her eyes are very bright indeed.{/n} "Yes," {n}she says.{/n} "That is what it is worth." {n}Then she pats the floor beside her.{/n} "Sit down. I am going to tell you anyway. It is a good story. Everyone in it dies."''',
        c("Continue", "story")),
    mz("story", '''"There was a country on the edge of the sea, far from my island, with a king who wore a crown with one blue stone in it. The sea came up one year and took the country, all of it, the fields and the towns and the palace, and the king went down with his crown on his head, sitting on his throne, because he said a king does not leave." {n}She says it with approval.{/n}
"I went down after it. It was a long way down and very cold. The king was still on his throne, with fish in his beard. I took the crown off his head." {n}She holds up two fingers, pinched together.{/n} "The gold I did not want. Gold is soft and it tastes of hands. I kept the stone. I wrapped it in a rock, so nobody would ever know, and I slept on it for two hundred years."''',
        c('"And the king?"', "king")),
    mz("king", '''"I ate him. He was very well preserved." {n}She puts her hand over the pocket holding the stone.{/n} "He held on to his crown until the sea took him. You walked out with his best stone while I watched."

{n}Her fingers tighten on the cloth.{/n} "I still want to take it back. Keep your pocket buttoned."''',
        c("Continue", flags=(M + "beat.king_heard",)))],
    requires=(STONE_KEPT,), forbids=(M + "beat.king_heard",))


# --- Chapter 5: the price of the cells, and the lesson in putting things down. --------------------------------------------

visit(M + "beat.inquisitor", "Somebody is asking", [
    nar("start", '''{n}An inquisitor of Iomedae has been in the cellars under the citadel for two days, with a lamp and a notebook and a young acolyte who holds the lamp. He has measured the cells, and the grating, and the cold that will not come out of the stones. This morning he asked to see the gaoler's book. This afternoon he asked to see you, and you were busy, and he said that he would wait.{/n}
{n}That night she comes in over the sill in the woman she wears, and she is smiling.{/n}''',
        c("Continue", "her")),
    mz("her", '''"There is a man in your cellar with a lamp," {n}she says.{/n} "He smells of candle-wax and certainty. He is asking where your prisoners went. He knows they did not escape; he has looked at the locks." {n}She sits on the corner of your desk and swings her foot.{/n} "He is very thin. I do not think he would be worth the trouble. But he is asking, and he will go on asking, and in the end he will ask you."
"I can make him stop asking." {n}She says it lightly, as she said everything on Colyphyr.{/n} "Tonight. He would go down to the cellar with his lamp, and there would be the cold, and then there would not be anything. Your gaoler would write escaped again. He is a sensible man."''',
        c('"No. He\'s mine to deal with."', "mine"),
        c('"Let him ask. He\'ll find nothing he can prove."', "prove"),
        c('[Evil] "Do it."', "do", alignment=("Evil", 1))),
    mz("mine", '''"Yours." {n}She shrugs.{/n} "The prisoners were yours until you gave them to me. This one you are keeping, and he is thin, and he will keep. What will you tell him?"

{n}She watches your face, then smiles.{/n} "Seven cells, and the locks still whole. I want to hear how you explain that."''',
        c("Continue", "after_mine")),
    nar("after_mine", '''{n}The inquisitor waits in the chapter room with his notebook open. His acolyte lays the gaoler's book beside it, open at the seven empty cells.{/n}
"The locks were not forced, Knight Commander. Who ordered the transfer? And where are the prisoners?"''',
        c("Continue", "inquiry_lie", requires=(M + "beat.inquisitor_lied",)),
        c('[Lie] "Transferred under my orders. Their destination is sealed."', "inquiry_lie"),
        c('"I gave them to Melazmera. They are dead. Put my name in your report."', "inquiry_admit"),
        c('"I will not answer. Send your findings to your superiors."', "inquiry_refuse")),
    mz("prove", '''"Nothing he can prove." {n}She repeats it, and giggles.{/n} "Yes. That is the best kind of nothing. I have a whole heap of it." {n}She slides off the desk.{/n}
"I will leave him his lamp. For now. If it goes out in the cellar, it will be the cold that blew it, and the cold goes where it likes. But he will look at you, thief, every day, across your castle, with that face. The face of a man who knows there is a thing he cannot prove." {n}She looks back from the window.{/n} "I know that face. I have seen it on a great many knights, just before they touched my crown."''',
        c("Continue", flags=(M + "beat.inquisitor_watched",))),
    mz("do", '''{n}She smiles at you, slowly, with every tooth she has, and for a moment the woman is not there at all.{/n}
"There," {n}she says softly.{/n} "You are learning what I am for."
{n}She goes out over the sill. In the morning the inquisitor's acolyte comes to the gatehouse alone, white to the lips, and says that his master went down to the cellars before dawn with the lamp and told him to wait on the stairs, and that the lamp went out, and that his master did not come up. The gaoler writes missing in his book, this time, not escaped. He does not look at you when he writes it. That is worse.{/n}''',
        c("Continue", flags=(M + "beat.inquisitor_eaten", M + "cost.inquisitor")))],
    requires=(FED_CULTISTS,), forbids=(M + "beat.inquisitor_lied", M + "beat.inquisitor_watched", M + "beat.inquisitor_eaten", M + "beat.inquisitor_reported"))
SCENES[-1]["Nodes"].extend([
    n("inquiry_lie", "Inquisitor", '"Sealed. I will record that answer beside the condition of the locks." {n}He has the acolyte copy your words. That night Melazmera reads the copy left on your desk and laughs.{/n} "Seven cells. Such a small lie for such a large meal."', c("Continue", flags=(M + "beat.inquisitor_lied", M + "beat.inquisitor_reported"))),
    n("inquiry_admit", "Inquisitor", '"Then I will name you. Not the gaoler." {n}He closes the book and hands his acolyte the report for the next courier. Melazmera finds you at the window that night.{/n} "You told him. He still went away with all his fingers. I shall have to find dinner somewhere else."', c("Continue", flags=(M + "beat.inquisitor_admitted", M + "beat.inquisitor_reported"))),
    n("inquiry_refuse", "Inquisitor", '"Your refusal will accompany the measurements. My superiors can decide what it conceals." {n}The acolyte takes a second copy; the inquisitor keeps the first. That night Melazmera taps the sealed packet on your desk.{/n} "He can send his questions further. You are keeping him alive, not quiet."', c("Continue", flags=(M + "beat.inquisitor_refused", M + "beat.inquisitor_reported"))),
])

visit(M + "beat.putting_down", "A stronger claim", [
    nar("start", '''{n}She comes in over the sill with something on her mind. You can tell because she does not eat your supper; she walks past it, and sits down on the end of your bed, and turns something over and over in her fingers, scowling at it.{/n}
"I did an experiment," {n}she says.{/n} "On one of your people. About claims."''',
        c('"What kind of experiment?"', "happened")),
    mz("happened", '''"You left me a ring, and now you are in my hoard. I did not take you. You gave, and it held better than anything I ever took." {n}She says it like an accusation.{/n} "So I wanted to know if it works for me. If I give a thing to one of your people, is she mine?"
"There is a woman in your lower town who sits by the well with a bowl. I made myself small and plain and old, and took one of my square coins from the drowned country, and walked up to her bowl to put it in." {n}Her hand closes.{/n} "And I could not open my hand. It was mine. I stood in front of her so long that she asked if I was ill. Then she gave me a coin out of her bowl, because she thought I was poorer than she was."''',
        c("Continue", "coin")),
    mz("coin", '''{n}She opens her fist. There is a small copper coin in it, worn nearly smooth, the kind that buys half a loaf.{/n}
"So she gave to me." {n}Her voice is very flat.{/n} "A beggar. With a bowl. She put a thing in my hand and walked off, and now I have a thing of hers, and she has a claim on me, and I did not agree to it." {n}The lamp gutters.{/n} "I have been thinking all day about going back and eating her, so that the claim goes inside me where it belongs."''',
        c('"Don\'t. You lost fairly. Keep the coin."', "keep"),
        c('"Then give her something so large she can never give it back."', "large"),
        c('"If you eat her, you\'ll never know whether it would have worked."', "know")),
    mz("keep", '''"Lost." {n}She looks at you as if you had struck her, and then, slowly, she laughs, and it is not a pleasant sound.{/n} "Yes. I lost. To a woman with a bowl." {n}She closes her hand around the copper and presses it to her teeth.{/n}
"I will keep it. Not on the heap; the heap is for things I chose. I will wear it, where I can bite it, and every time I bite it I will remember that something in this city beat me with half a loaf." {n}She stands.{/n} "I am going to sit on the roof across from her well for a year, thief. She will be the safest beggar in the world, and she will never know why she cannot sleep."''',
        c("Continue", flags=(M + "beat.put_down", M + "beat.copper_kept"))),
    mz("large", '''{n}She goes very still. Then her eyes light up like two coals blown on.{/n}
"So large she can never give it back." {n}She tastes it.{/n} "Then she is mine, and she cannot get out, because she would have to pay first. Oh, thief. That is how you did it to me. A ring was nothing to you. You made it into a thing I could not give back."
{n}She is on her feet and at the window before you can answer.{/n} "I have a sapphire the size of her head. No; that is too good for her. I have a gold cup from a sunken temple. She will drink her soup out of it for the rest of her life, and every time she lifts it she will know whose she is."''',
        c("Continue", flags=(M + "beat.put_down",))),
    mz("know", '''{n}She stops turning the coin.{/n} "No," {n}she agrees, slowly.{/n} "If I eat her it is over, and I know nothing. That is what I always did, and I always knew nothing." {n}She looks at the coin as a scholar looks at a strange beetle.{/n}
"Fine. I will try again. Tomorrow I will open my hand, if I have to hold it open with the other one, and put the coin in her bowl, and see who owns whom at the end of it." {n}She bares her teeth at you.{/n} "If it goes wrong, thief, I am coming back here and eating something of yours. I have not decided what. Something you like."''',
        c("Continue", flags=(M + "beat.put_down",)))],
    requires=(COMMITTED, HEAP), forbids=(M + "beat.put_down",))
