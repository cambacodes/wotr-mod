"""Delamere: the beats around the fire (delamere_woods holds the spine; delamere_trickster the device).

- The white stag (required, between the feasting table and "Red"): the device told in her own voice. The stag hunt is
  Kyado's canon (Kyado_main_dialogue/Cue_0039) and her own (DelamereInTomb/Cue_0034: "Three daysss we vied with each other
  in ssstealth and ssspeed... I did not eat the meat"); her death at full draw on an unfinished hunt is authored, and is
  the reading the tomb's invisible archer gives (TombOfDelamere_BookEvent/Cue_0052, Cue_0054).
- Her glory (optional): "Can it be that my glory hasss faded?" (DelamereInTomb/Cue_0020); "I wasss known... Feared...
  Ressspected... Loved..." (Cue_0032).
- The jester (optional, Chapter 5): her reaction to the Trickster the Commander has become, through Kyado's own reading of
  the path: "anyone who treats everything seriously finds themselves defenseless before you, like a child"
  (Kyado_main_dialogue/Cue_0109 509eac82).
- A demon in her woods (optional, Chapter 5): the Worldwound's things in the valleys she guarded.
- The prior's lessons (optional, physical on Kyado's list in Chapter 3): Kyado, who is afraid, and the woman who is not.
"""
from story_format import c
from storylines.delamere_trickster import (BOW_RETURNED, CLOSED, COMMITTED, KYADO_JUDGED, KYADO_SPOKEN, KEPT_QUIET, LIMP, P,
                                           PROCLAIMED, RETURNED, STAG_TOLD, YEW_BOW, dl, kyado, nar)
from storylines.delamere_trickster import temple as _temple, visit as _visit
from storylines.delamere_woods import COUNTED, FIRST_MEAT, TABLE

SCENES = []


def temple(*args, **kw):
    _temple(*args, into=SCENES, **kw)


def visit(*args, **kw):
    _visit(*args, into=SCENES, **kw)


JESTER_SEEN = P + "jester_seen"
KNIFE_LIFTED = P + "knife_lifted"
DEMON_HUNTED = P + "demon_hunted"
BAIT_CLEAN = P + "bait_clean"
LESSONS = P + "prior_lessons"


# --- The white stag (the device, in her own voice) -------------------------------------------------------------------

visit(P + "woken.white_stag", "The white stag", [
    nar("fire", '''{n}She has made a fire on the ridge above Drezen, in a fold of the hill where she can see the city's lamps and not smell its gutters, and there is a hare on a green stick over it. When you come limping up out of the dark she does not turn round. She moves over on her log to make room.{/n}''',
        c("[Sit.]", "owe")),
    dl("owe", '''"Eat." {n}She tears the hare in two and gives you the bigger half, which from her is a speech.{/n} "The boy says you asked him what I was aiming at, before you blew that horn. You should hear it from the one who was doing the aiming. I owe you that, I think. For the leg."''',
        c('"Tell me about the white stag."', "stag"),
        c('"You don\'t owe me anything."', "debt")),
    dl("debt", '''"Do not tell me what I owe. I have been keeping my own accounts since before your grandmother's grandmother was born." {n}She pokes the fire.{/n} "Listen, and eat, and do not interrupt me. I have not told this in a very long time, and I do not know how much of it is still where I left it."''',
        c("Continue", "stag")),
    dl("stag", '''"I was nineteen. The snow came early that year. And one morning a white stag walked out of the trees below where my temple stands now, and stood in the open, where no stag ever stands, and looked at me."
{n}Her voice has changed. It is lower, and slower, as if she were reading the words off the inside of her own eyelids.{/n} "It spoke. It had a man's voice. An old man's, dry, like my grandfather's. It said: 'Hunt me, daughter. Hunt me well, and I will be your bow.'"''',
        c("Continue", "three")),
    dl("three", '''"Three days and three nights. We vied with each other in stealth and in speed, the stag and I. I did not sleep. I ate snow. I lost it in a whiteout on the second night and found it again by the smell, the way you find a friend in the dark." {n}She almost smiles.{/n} "A noble fight. The best I ever had. It was faster than me and cleverer than me, and it wanted to be caught. That is a hard thing to hunt, stag. A beast that wants you to win, and will not let you."''',
        c('"How did it end?"', "lake")),
    dl("lake", '''"At a frozen lake, on the third dawn. It walked out onto the ice and turned and waited for me. I drew. It did not run. It looked at me the way you looked at me in the leaves: surprised that it was over."
{n}She is quiet.{/n} "I did not eat the meat. I gave all of it to Old Deadeye, every scrap, and went three more days hungry after the three days of chasing. The antlers I made into my bow over that winter. The hide I made into this." {n}She touches the breastplate.{/n}''',
        c("Continue", "vow")),
    dl("vow", '''"And I knelt in its blood on the ice and I swore. When the stag calls, I answer. Wherever I am. Whatever I am doing. I did not know it would hold past death." {n}She turns the hare bone in her fingers.{/n} "Nobody tells you which of your vows are the ones that hold. You find out."''',
        c('"And the hunt you died on?"', "death")),
    dl("death", '''"I was thirty-eight winters. Old, for a hunter on the roads." {n}She throws the bone into the fire.{/n} "A wolf came down out of the north in a hungry winter. White, as the stag had been, and too big, and wrong somehow in the way it moved. It took children out of the byres. I tracked it eleven days into the passes. On the eleventh I had it below me in a gully, on the ice. I drew."
{n}She stops.{/n} "And then there is nothing. A rock came down, or the ice gave way under me, or my heart burst in my chest. I remember the draw. I remember the wolf's eyes. And then the dark."''',
        c("Continue", "draw")),
    dl("draw", '''"I died at full draw, with the arrow on the string and the beast in front of me. I never loosed." {n}She holds up her right hand, the fingers curled as if around a bowstring, and looks at it.{/n} "That is what I was doing, stag. All that time, in the dark. Holding. Waiting for my fingers to open. The pilgrims felt it, the boy says, when they touched my bow. An arrow that was not there, pointing at their hearts. It was not pointing at them. It was pointing at a wolf."''',
        c('"What happened to the wolf?"', "wolf"),
        c('"That\'s the saddest thing I\'ve ever heard."', "sad"),
        c('"Well. At least you held your form."', "form")),
    dl("wolf", '''"Dead of old age these many lifetimes, I should think. Or it went north into the Wound when the Wound came, and became something worse." {n}A short, cracked laugh.{/n} "I held a bow on a dead wolf for longer than your city has stood. If you ever wonder whether I am stubborn, stag, remember that."''',
        c("Continue", "opened")),
    dl("sad", '''"It is not sad. It is only long." {n}She says it firmly, as if the matter had been settled by a village council long ago.{/n} "Sad is the Stone Hares' girl who could track a fox across a frozen river. Sad is a boy on my grave with his fingers in the drain. I was a hunter who died hunting. There are worse ends. Most of them happen in beds."''',
        c("Continue", "opened")),
    dl("form", '''{n}She stares at you. Then something breaks in her face and she laughs, really laughs, head back, a sound that sends a roosting bird clattering out of the next tree.{/n} "My form." {n}She wipes her eyes with a greasy thumb.{/n} "Four walls of stone and a Kellid seal and a witch eating off my belly, and the jester says: at least you held your form. Erastil help me. I did. Not one finger moved."''',
        c("Continue", "opened")),
    dl("opened", '''"So now you know what you did with your horn." {n}She looks at you across the fire.{/n} "You did not raise me. I am not one of the lich-things; no god bought me back and no sorcerer tied me to his will. The stag called, and I answered, because I swore I would. And when I answered, my fingers opened at last."
{n}She reaches over and lays her hand flat on your thigh, over the place where the arrow went in.{/n} "Your leg is where it went. It had been waiting a very long time."''',
        c('"You kept a promise for centuries. I\'ve never kept one for a week."', "week"),
        c('"I\'m glad it was my leg."', "glad")),
    dl("week", '''"Then you had better start." {n}She takes her hand back and throws another stick on the fire.{/n} "Start with a small one. Promise me you will come back to this fire tomorrow night and eat another hare." {n}She waits.{/n} "Come. It is a very small promise. Even a jester can keep a small one."''',
        c('"I promise."', "promised", flags=(STAG_TOLD,))),
    dl("glad", '''"Liar." {n}But she does not take the hand away.{/n} "A kind one. I will allow it, tonight." {n}She looks into the fire for a while, and so do you, and neither of you says anything, and the city's lamps go out one by one below the hill.{/n}''',
        c("[Stay until the fire burns down.]", flags=(STAG_TOLD,))),
    nar("promised", '''{n}You come back the next night. She has two hares, and pretends she caught the second one by accident.{/n}''',
        c("[Eat.]")),
], requires=("trickster.ever", TABLE), forbids=(CLOSED, STAG_TOLD), delay=24)


# --- Her glory (Drezen market; optional) ---------------------------------------------------------------------------

visit(P + "woken.glory", "Her glory", [
    nar("market", '''{n}There is a crowd around the fountain in the Drezen market, and a minstrel on its rim with a lute, and when you push through to see what the laughter is about, the tall Kellid woman at the front of the crowd has her hand around his lute's neck and the minstrel has gone the colour of whey.{/n}''',
        c("Continue", "song")),
    dl("song", '''"Sing it again," she says, very pleasantly. "The part about the Blessed Delamere who wept over every deer she slew, and fed the orphans of the wood with honey from her own hands."
{n}The minstrel does not sing it again. She lets go of the lute. He clutches it to his chest like a baby.{/n}''',
        c('"Delamere. What did he do?"', "wrong")),
    dl("wrong", '''"He sang me wrong." {n}She turns on you, and there is real outrage in her face, and under it something stranger and more naked: hunger.{/n} "Weeping over deer. Honey. Orphans. I never wept over a deer in my life; I ate them. I had no honey; bees hate me. And I did not feed orphans, I put them to work, which is better for an orphan than honey."
{n}She looks back at the minstrel.{/n} "But he knew my name. They all know my name. He sang it in a market in a city, and people who have never seen a Kellid hill clapped."''',
        c("Continue", "crowd")),
    nar("crowd", '''{n}The crowd has gone quiet. At the back, an old Sarkorian woman with a basket of turnips has put the basket down. She is staring at the stag-hide breastplate, and at the bow, and at the face above them, and her lips are moving.{/n}
{n}Beyond her, by the steps of Iomedae's cathedral, a young priest in a white tabard has stopped to watch, frowning, with the look of a man about to say that there is no Saint Delamere in the calendar.{/n}''',
        c("Continue", "glory")),
    dl("glory", '''{n}She has seen the old woman too. Her voice drops so that only you can hear it.{/n} "When I was alive, they knew me in every valley between the river and the passes. Feared me. Respected me. Some of them loved me. I did not ask for it; I was hard on them, and they came to me anyway." {n}Her jaw sets.{/n} "In the dark I thought: my glory has faded. They have forgotten me. And now I find they have not forgotten me. They have only made me soft."''',
        c('[Proclaim her] "Drezen! This is Delamere the Blessed, priestess of Erastil, who guarded these valleys before the Wound. She\'s back, and she doesn\'t weep over deer."', "proclaim",
          flags=(PROCLAIMED,)),
        c('[Take her arm] "Let them sing it wrong. Walk with me."', "quiet", flags=(KEPT_QUIET,))),
    nar("proclaim", '''{n}Your voice carries across the whole market. For a heartbeat there is silence. Then the old Sarkorian woman at the back sinks to her knees in the dung and the cabbage leaves, and a man beside her, and then half a dozen more, all of them Kellid faces from the refugee camp, all of them with their hands pressed to their hearts in the old way.{/n}
{n}The young priest opens his mouth, and looks at the kneeling Sarkorians, and closes it again.{/n}''',
        c("Continue", "proclaimed")),
    dl("proclaimed", '''{n}She stands among them as if she has been struck. Then she walks to the old woman and takes her by both elbows and hauls her up out of the dung, not gently.{/n} "Get up. Get up. I am not a god. Erastil is the god; I only carried his bow." {n}She holds the woman's face in her hands.{/n} "What clan?"
{n}The woman tells her, weeping. Delamere nods, and repeats the name, and lets her go, and turns back to you, and her eyes are blazing.{/n} "You did that on purpose."''',
        c('"Of course I did."', "purpose")),
    dl("purpose", '''"I will never be rid of them now. They will come to my woods. They will bring me their quarrels and their sick goats and their daughters who will not marry." {n}She takes a breath that shakes.{/n} "I am going to be very busy, stag. I have not been busy in a very long time." {n}She walks out of the market with her back straight as a spear, and does not look round, and the Sarkorians part for her like water.{/n}''',
        c("[Watch her go.]")),
    nar("quiet", '''{n}She lets you take her arm, which surprises both of you, and you walk her out of the market past the frowning priest and the staring old woman and out through the Tanners' Gate, and behind you the minstrel, very cautiously, begins to play something else.{/n}''',
        c("Continue", "quieted")),
    dl("quieted", '''"Let them sing it wrong." {n}She tries the words as if they were a new kind of bread.{/n} "In my day I would have had his lute off him and broken it over the fountain." {n}She walks a while.{/n} "The old woman knew me. Did you see? She knew me." {n}Her grip tightens on your arm.{/n} "That is enough. One is enough. I do not need a city to kneel. I have been knelt to. It is uncomfortable for everyone."''',
        c("[Walk her to the gate.]")),
], requires=("trickster.ever", COUNTED), forbids=(CLOSED, PROCLAIMED, KEPT_QUIET), delay=48, optional=True)


# --- The jester (Chapter 5; optional): what the Commander has become ---------------------------------------------------

visit(P + "woken.jester", "Defenceless", [
    nar("yard", '''{n}She is waiting in the yard of your quarters when you come back from the war council, sitting on the mounting block with her bow across her knees and a look on her face that you have learned means she has been thinking about something for a long time and has reached the end of it.{/n}''',
        c("Continue", "rumour")),
    dl("rumour", '''"While you were in the Abyss, people talked about you. They always talk about you; in a city nobody has anything better to do." {n}She turns the bow over.{/n} "They say you walked into places no one comes out of, and came out laughing. They say demons who were meant to eat you ended up arguing among themselves about the recipe. They say it the way children talk about the fox in the old stories. Half afraid. Half on the fox's side."''',
        c("Continue", "kyado")),
    dl("kyado", '''"The boy said something to me once, about you, before I knew you. He said anyone who treats everything seriously is defenceless before you, like a child." {n}She looks up.{/n} "I treat everything seriously, stag. I have never made a joke in my life that I know of. So I have been sitting on this block since the bell, asking myself whether I am defenceless before you."''',
        c('"Yes."', "yes"),
        c('"No. You\'re the only one I can\'t fool."', "no"),
        c('[Thievery: while she talks, lift the skinning knife from her belt]', check=dict(Skill="SkillThievery", DC=26, Success="lifted", Failure="caught", CommanderOnly=True))),
    dl("yes", '''"Yes." {n}She considers that, frowning, as though you had told her the depth of a ford.{/n} "Honest, at least. I was defenceless the night you blew the horn. My own vow opened my hand for you. I did not choose it."
{n}She stands.{/n} "But I chose the rest. The fire, the woods, the wall. Mark that, fox. You caught me by a trick once. Everything after that, I walked into on my own feet, looking where I was going."''',
        c("Continue", "end", flags=(JESTER_SEEN,))),
    dl("no", '''"Liar." {n}But she looks pleased, which she hides badly, as always.{/n} "You fooled me with a horn. You would fool me again tomorrow if it would make you laugh." {n}She stands.{/n} "But you tell me when you have done it. That is the thing I did not expect. The fox in the stories never tells."''',
        c("Continue", "end", flags=(JESTER_SEEN,))),
    nar("lifted", '''{n}It comes away from her belt as if it were glad to go. She is still talking. You wait until she stops, and then you hold it up between two fingers, handle first, the way you would return a dropped glove.{/n}''',
        c("Continue", "lifted2")),
    dl("lifted2", '''{n}She looks at the knife. She looks at her belt. She looks at you.{/n} "Yes," she says at last, in a voice you have not heard from her before. "Defenceless. Like a child." {n}She takes the knife back, very carefully, as if it might have learned tricks while it was away.{/n} "Do that to the Horned One's people and I will kiss you in front of the whole war council. Do it to me again and I will put you over my knee."''',
        c("Continue", "end", flags=(JESTER_SEEN, KNIFE_LIFTED))),
    dl("caught", '''{n}Her hand closes on your wrist before your fingers have found the hilt, hard enough to grind the bones.{/n} "No." {n}She does not let go.{/n} "Not defenceless, then. Not with a knife." {n}She holds your wrist a moment longer than she needs to, and her thumb moves, once, over the pulse.{/n} "Try again next winter. You will be slower then; I have seen to that."''',
        c("Continue", "end", flags=(JESTER_SEEN,))),
    dl("end", '''"Here is what I have decided, sitting on this block." {n}She slings her bow.{/n} "In the old stories the fox always wins, and the village always pays for it afterward. I have been the village. I will not be the village again." {n}She looks at you, long and level.{/n} "So play your tricks on demons, stag. Play them on the Horned One and his witches and the things in the Wound. And when you play one on my people, I will know, and I will come for my day early."''',
        c("[Nod.]")),
], requires=("trickster.ever", FIRST_MEAT), forbids=(CLOSED, JESTER_SEEN), delay=48, chapters=(5, 5), optional=True)


# --- A demon in her woods (Chapter 5; optional) ------------------------------------------------------------------------

visit(P + "woken.demon", "Be the stag again", [
    nar("sign", '''{n}She is waiting at the edge of her woods at dusk with two fresh tracks drawn in the mud at her feet: one a deer's, one something else. The second has three toes, and a spur behind, and it has been pressed down deep, as though whatever made it were much heavier than anything that size should be.{/n}''',
        c("Continue", "babau")),
    dl("babau", '''"It came out of the Wound nine nights ago. It has taken a charcoal-burner and two goats, and the goats it did not bother to eat." {n}She scuffs the track out with her boot.{/n} "I have lost it four times. It goes through shadows the way a fish goes through water, and it is patient. Patient as me." {n}Her mouth tightens.{/n} "I need it to come to me. So I need something it wants more than it wants to stay hidden."''',
        c('"And what does it want?"', "want")),
    dl("want", '''"Wounded meat." {n}She looks, deliberately, at your leg.{/n} "A thing that limps. That cannot run far. That a demon has been smelling on the wind all week from the direction of your camp, stag, because you walk these hills like a cart."
"Be the stag again. Walk out into the clearing below the old Ash-Cutter stones, and let it hear you coming. I will be in the trees. I will not miss."''',
        c('"You want to use me as bait."', "bait"),
        c('"Where do you want me?"', "where")),
    dl("bait", '''"I want to use you as a stag. You were a very good one once." {n}She checks her fletching, one arrow at a time.{/n} "If you would rather, I will go back to losing it in the shadows while it eats the next charcoal-burner. It is your country. You choose what it costs."''',
        c('"Where do you want me?"', "where")),
    nar("where", '''{n}The clearing is grey under a thin moon, ringed with the tumbled stones of a village that was a village before there was a crusade. You walk out into the middle of it and stand among the stones, and then, because standing is not what she asked for, you begin to walk. Slowly. Badly. Favouring the leg.{/n}
{n}The woods around you have gone completely silent.{/n}''',
        c('[Stealth: walk as prey walks, and do not look toward the trees where she is waiting]',
          check=dict(Skill="SkillStealth", DC=22, Success="clean", Failure="scent", CommanderOnly=True))),
    nar("clean", '''{n}You do not look toward her trees. Not once. You limp from stone to stone like a thing too tired and hurt to care who hears it, and the silence thickens, and thickens, and then there is a shape in the moonlight that was not there before, low and long and grey, with too many joints in its arms, coming at you across the clearing without a sound.{/n}
{n}It is ten paces off when the first arrow takes it in the eye.{/n}''',
        c("Continue", "kill", flags=(BAIT_CLEAN,))),
    nar("scent", '''{n}You look toward her trees. Only once, only for a heartbeat, the way you would look toward a friend to make sure she is still there. The thing in the dark sees you do it.{/n}
{n}It does not come from the front. It comes out of the shadow of the stone at your back, and its claws go into your shoulder before you have turned, and you are down, with its weight on you and its breath on your neck, stinking of the Wound.{/n}
{n}The first arrow takes it in the eye an inch from your ear.{/n}''',
        c("Continue", "kill")),
    nar("kill", '''{n}The second takes it in the throat, and the third in the joint of the knee, and by then she is out of the trees and running, and the fourth she does not shoot at all: she drives it into the thing's skull by hand, both fists on the shaft, with all her weight behind it, and holds it there until it stops moving.{/n}''',
        c("Continue", "after_clean", requires=(BAIT_CLEAN,)),
        c("Continue", "after_hurt", forbids=(BAIT_CLEAN,))),
    dl("after_clean", '''{n}She stands over it, breathing hard, and then she looks at you, and her face is fierce and bright.{/n} "You did not look. You walked like meat and you did not look at me once." {n}She wipes her hands on the dead grass.{/n} "Do you know how hard that is? To trust a bow at your back and not look? Grown hunters cannot do it. I could not do it, at your age."''',
        c("Continue", "burn")),
    dl("after_hurt", '''{n}She is on her knees beside you before the thing has finished twitching, pulling your coat back from the shoulder.{/n} "You looked." {n}Her voice is shaking.{/n} "You looked at me. I told you not to look." {n}Her hands, pressing a pad of moss into the wound, are not shaking at all.{/n} "Fool. Fool of a stag. It was a heartbeat from your throat."''',
        c('"You didn\'t miss."', "missed")),
    dl("missed", '''"I never miss." {n}She ties off the pad with a strip of her own shirt, and pulls it tight, and then does not let go of the knot.{/n} "I was not afraid of missing. I was afraid of being a heartbeat slow. I was a heartbeat slow once, in a gully on the ice, and I have had a long time to think about it."''',
        c("Continue", "burn")),
    dl("burn", '''"Help me drag it to the stones. We burn it where it can see the village it did not get." {n}She looks around the ring of tumbled stones, grey in the moonlight.{/n} "The Ash-Cutters built here. Their children played in this clearing. I used to walk through on my rounds and count them." {n}A pause.{/n} "One of them used to follow me for a mile, pretending to be a stag. He was very bad at it. He was better than you."''',
        c("[Help her drag it.]", flags=(DEMON_HUNTED,))),
], requires=("trickster.ever", STAG_TOLD), forbids=(CLOSED, DEMON_HUNTED), delay=48, chapters=(5, 5), optional=True)


# --- The prior's lessons (physical, Chapter 3, Kyado alive; optional) ----------------------------------------------------

temple(P + "temple.prior_lessons", "The prior's lessons", '"Kyado, what happened to your hands?"', [
    kyado("hands", '''{n}Kyado looks at his fingers. They are wrapped in rags, and the rags are brown at the tips.{/n} "B-bowstring." {n}He says it as a man might say "plague".{/n} "She says a prior of Erastil who can't draw a bow is like a shepherd who can't count sheep. I said Rathimus couldn't draw a bow either, and she said, 'Then Rathimus was a poor prior, and you will be a better one.' She said it very kindly. It was t-terrible."''',
        c("Continue", "yard")),
    nar("yard", '''{n}Through the temple door you can see her in the yard, setting a straw target against the woodpile. She has painted a demon's face on it in charcoal: a surprisingly good demon, with horns, and a very stupid expression.{/n}
{n}Kyado follows your eyes and whimpers.{/n}''',
        c("[Go out into the yard.]", "out")),
    dl("out", '''"Stag." {n}She does not look up from the target.{/n} "You have come to watch the boy fail. Good. He fails better with someone watching; it makes him angry. Anger is the only thing that has ever made that boy's arm straight."
{n}She raises her voice.{/n} "Boy! Out. Bring the bow. Not that one; the one I gave you. The one you are afraid of."''',
        c("Continue", "draw")),
    nar("draw", '''{n}Kyado comes out holding the bow as if it were a live eel. He nocks badly, draws worse, and the arrow goes into the woodpile a yard to the left of the demon, and sticks there, quivering, in a log.{/n}
{n}Delamere watches it stop quivering. Then she walks over to him, and stands behind him, and takes his elbow in one hand and his wrist in the other.{/n}''',
        c("Continue", "fear")),
    dl("fear", '''"You close your eyes when you loose. Why?" {n}Kyado mumbles something. She waits.{/n} "Louder."
"B-because I'm afraid it will hit." {n}He goes scarlet.{/n} "I'm afraid it will hit something and it will be my fault."
{n}She does not laugh. She is quiet a moment.{/n} "That is the only good reason to be afraid of a bow. Keep it. Keep your eyes open anyway. A priest who shoots with his eyes shut hits the wrong thing, and then it is his fault twice."''',
        c("Continue", "again")),
    nar("again", '''{n}He draws again, with her hands on his. His eyes stay open, streaming. The arrow goes into the straw a foot below the demon's chin, and stays there.{/n}
{n}Kyado stares at it. Then he sits down in the dust, very suddenly, as if somebody had cut the strings behind his knees.{/n}''',
        c("Continue", "you")),
    dl("you", '''{n}She lets him sit. She turns to you with the bow still in her hand.{/n} "Now you, stag. You carry a sword like a man carrying a ladder. Let us see what you do with a string."''',
        c("Continue", "yew_given", requires=(YEW_BOW, BOW_RETURNED)),
        c("Continue", "plain", forbids=(YEW_BOW,)),
        c("Continue", "plain", requires=(YEW_BOW,), forbids=(BOW_RETURNED,))),
    nar("yew_given", '''{n}You unsling the plain yew bow she gave you on the hill, which you have been carrying ever since without once admitting it. She sees it, and says nothing, and something at the corner of her mouth says it for her.{/n}''',
        c("Continue", "shot")),
    nar("plain", '''{n}She hands you Kyado's bow. It is still warm from his hands, and slippery.{/n}''',
        c("Continue", "shot")),
    nar("shot", '''{n}You draw. Your bad leg will not take the weight the way a stance wants it to, so you shift onto the good one, and she puts her palm flat in the small of your back and shifts you back again, firmly.{/n}
"On both," she says, very close to your ear. "Even the bad one. Especially the bad one. A leg you do not trust never gets stronger." {n}Her hand does not move from your back while you loose. The arrow goes into the demon's painted eye.{/n}''',
        c("Continue", "eye")),
    dl("eye", '''{n}Kyado, in the dust, applauds, then stops, embarrassed.{/n}
"Luck," says Delamere, and takes her hand from your back, slowly. "Jester's luck. But you did not close your eyes." {n}She looks at the target, and then at you, and for a moment the yard is very quiet.{/n} "Come again. Both of you. I have not had pupils in a long time. I had forgotten that I liked it."''',
        c("[Promise to come again.]", flags=(LESSONS,))),
], requires=("trickster.ever", FIRST_MEAT), forbids=(CLOSED, LESSONS, KYADO_JUDGED), delay=24, optional=True)
