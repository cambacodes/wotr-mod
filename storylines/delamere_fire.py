"""Delamere: the beats around the fire (delamere_woods holds the spine; delamere_trickster the device).

- The white stag (required, between the feasting table and "Red"): the device told in her own voice. The stag hunt is
  Kyado's canon (Kyado_main_dialogue/Cue_0039) and her own (DelamereInTomb/Cue_0042 20f0dfa4: "Three daysss we vied with each other
  in ssstealth and ssspeed... I did not eat the meat"); her death at full draw on an unfinished hunt is authored, and is
  the reading the tomb's invisible archer gives (TombOfDelamere_BookEvent/Cue_0052, Cue_0054).
- Her glory (optional): "Can it be that my glory hasss faded?" (DelamereInTomb/Cue_0020); "I wasss known... Feared...
  Ressspected... Loved..." (Cue_0039 ac70a123).
- The jester (optional, Chapter 5): her reaction to the Trickster the Commander has become, through Kyado's own reading of
  the path: "anyone who treats everything seriously finds themselves defenseless before you, like a child"
  (Kyado_main_dialogue/Cue_0109 509eac82).
- A demon in her woods (optional, Chapter 5): the Worldwound's things in the valleys she guarded.
- The prior's lessons (optional, physical on Kyado's list in Chapter 3): Kyado, who is afraid, and the woman who is not.
- Old Deadeye's house (optional): Erastil answered at her seal with "A stag bellows in the distance"
  (TombOfDelamere_BookEvent/Cue_0067 a58f2095) when the Commander, his worshipper, prayed there (Answer_0066 needs the
  ErastilFeature). That is read natively (SeenCues delamere.erastil_answered) and told only when the Commander heard it;
  otherwise Brother Haddo offers his church's reading of a stag's call, and says he cannot tell a sign from a stag in rut.
  Nothing claims the god answered anyone else. The Drezen chapel of Erastil and Brother Haddo are authored.
- Delivery (NM1, coordinator allocation exception): the optional beats arrive at a rest like every other visit (Q6 had
  made them manual reads from the mod menu, which a beta cannot rely on).
- The names (optional): "I will count them later. All of them." (the waking) paid on the crypt wall where Zanedra's cult
  feasted (TombOfDelamere_BookEvent/Cue_0002; the farm boy, ZanedraInTemple).
- Doe in fawn (optional): crusade poachers in her wood; whose law judges them (the crusade's, hers, or a Trickster's bluff).
- The hide (optional, after the commit): the stag hide from the blind cut into a brace for the leg her arrow broke; her
  household line (05 voice note a_village_not_a_city): she will know every name at the Commander's fire.
"""
from story_format import c
from storylines.delamere_trickster import (BOW_RETURNED, CLOSED, COMMITTED, ERASTIL_ANSWERED, KYADO_JUDGED, KYADO_SPOKEN, KEPT_QUIET, LIMP, P,
                                           NAMES, POACHERS_HERS, POACHERS_PROVOST, POACHERS_TRICKED, PROCLAIMED,
                                           RETURNED, STAG_TOLD, YEW_BOW, dl, kyado, nar)
from storylines.delamere_trickster import temple as _temple, visit as _visit
from storylines.delamere_trickster import KYADO_DEAD   # PP10: the jester's line from Kyado, alive or in his daybook
from storylines.delamere_woods import CONFESSED, COUNTED, FIRST_MEAT, LIED, TABLE
from storylines.delamere_trickster import VILLAGE_CLANS, VILLAGE_FORCED, VILLAGE_GIVEN, VILLAGE_REFUSED   # polish r4: the poachers' sentence

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
DEADEYE = P + "old_deadeye"
HIDE = P + "hide_brace"


# --- The white stag (the device, in her own voice) -------------------------------------------------------------------

visit(P + "woken.white_stag", "The white stag", [
    nar("fire", '''{n}She has made a fire on the ridge above Drezen, in a fold of the hill where she can see the city's lamps and not smell its gutters, and there is a hare on a green stick over it. When you come limping up out of the dark she does not turn round. She moves over on her log to make room.{/n}''',
        c("[Sit.]", "owe")),
    dl("owe", '''"Eat." {n}She tears the hare in two and gives you the bigger half, which from her is a speech.{/n} "You blew that horn over me without knowing what I was aiming at. You should hear it from the one who was doing the aiming. I owe you that, I think. For the leg."''',
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
{n}She is quiet.{/n} "I did not eat the meat. I gave all of it to Old Deadeye, every scrap, and went three more days hungry after the three days of chasing. The antlers I made into my bow over that winter. The hide I made into armour, and wore it forty winters."''',
        c("Continue", "vow")),
    dl("vow", '''"And I knelt in its blood on the ice and I swore. When the stag calls, I answer. Wherever I am. Whatever I am doing. I did not know it would hold past death." {n}She turns the hare bone in her fingers.{/n} "Nobody tells you which of your vows are the ones that hold. You find out."''',
        c('"And the hunt you died on?"', "death")),
    dl("death", '''"I was fifty-nine winters. Old, for a hunter on the roads." {n}She throws the bone into the fire.{/n} "A wolf came down out of the north in a hungry winter. White, as the stag had been, and too big, and wrong somehow in the way it moved. It took children out of the byres. I tracked it eleven days into the passes. On the eleventh I had it below me in a gully, on the ice. I drew."
{n}She stops.{/n} "And then there is nothing. A rock came down, or the ice gave way under me, or my heart burst in my chest. I remember the draw. I remember the wolf's eyes. And then the dark."''',
        c("Continue", "draw")),
    dl("draw", '''"I died at full draw, with the arrow on the string and the beast in front of me. I never loosed." {n}She holds up her right hand, the fingers curled as if around a bowstring, and looks at it.{/n} "That is what I was doing, stag. All that time, in the dark. Holding. Waiting for my fingers to open. The pilgrims felt it, by the boy's daybook, when they touched my bow. An arrow that was not there, pointing at their hearts. It was not pointing at them. It was pointing at a wolf."''',
        c('"What happened to the wolf?"', "wolf"),
        c('"That\'s the saddest thing I\'ve ever heard."', "sad"),
        c('"Well. At least you held your form."', "form")),
    dl("wolf", '''"Dead of old age these many lifetimes, I should think. Or it went north into the Wound when the Wound came, and became something worse." {n}A short, cracked laugh.{/n} "I held a bow on a dead wolf for longer than your city has stood. If you ever wonder whether I am stubborn, stag, remember that."''',
        c("Continue", "opened")),
    dl("sad", '''"It is not sad. It is only long." {n}She says it firmly, as if the matter had been settled by a village council long ago.{/n} "Sad is the Stone Hares' girl who could track a fox across a frozen river. Sad is a boy on my grave with his fingers in the drain. I was a hunter who died hunting. There are worse ends. Most of them happen in beds."''',
        c("Continue", "opened")),
    dl("form", '''{n}She stares at you. Then something breaks in her face and she laughs, really laughs, head back, a sound that sends a roosting bird clattering out of the next tree.{/n} "My form." {n}She wipes her eyes with a greasy thumb.{/n} "Four walls of stone and a Kellid seal and a witch eating off my belly, and the jester says: at least you held your form. Erastil help me. I did. Not one finger moved."''',
        c("Continue", "opened")),
    dl("opened", '''"So now you know what you did with your horn." {n}She looks at you across the fire.{/n} "I do not know all of what I am, stag. I know what I am not. The lich-things are cold, and I see my breath every morning. They do not bleed, and I bleed. They do not dream, and I dream of snow."
{n}She turns her hand palm up in the firelight.{/n} "And I know what I have lost. When I was the Blessed I could lay these hands on a torn hound and feel Old Deadeye come down them like warm water. Since the crypt, nothing. Whether he took it as the price of the waking, or I left it down there in the dark, I cannot tell you. The stag called, and I answered, because I swore I would. When I answered, my fingers opened at last. That much I know."
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
    nar("crowd", '''{n}The crowd has gone quiet. At the back, an old Sarkorian woman with a basket of turnips has put the basket down. She is staring at the old Kellid grave-leathers, and at the bow, and at the face above them, and her lips are moving.{/n}
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
        c("Continue", "kyado", forbids=(KYADO_DEAD,)),
        c("Continue", "kyado_book", requires=(KYADO_DEAD,))),
    # PP10 (Sol CAN): when Kyado is dead she has his words from the prior's daybook, not from his mouth.
    dl("kyado_book", '''"The boy kept a prior's daybook. I read it, after; somebody had to. Under the day you first came to my temple he wrote, in that small frightened hand, that anyone who treats everything seriously is defenceless before you, like a child." {n}She looks up.{/n} "I treat everything seriously, stag. I have never made a joke in my life that I know of. So I have been sitting on this block since the bell, asking myself whether I am defenceless before you."''',
        c('"Yes."', "yes"),
        c('"No. You\'re the only one I can\'t fool."', "no"),
        c('[Thievery: while she talks, lift the skinning knife from her belt]', check=dict(Skill="SkillThievery", DC=26, Success="lifted", Failure="caught", CommanderOnly=True))),
    dl("kyado", '''"The boy said something to me once, about you, before I knew you. He said anyone who treats everything seriously is defenceless before you, like a child." {n}She looks up.{/n} "I treat everything seriously, stag. I have never made a joke in my life that I know of. So I have been sitting on this block since the bell, asking myself whether I am defenceless before you."''',
        c('"Yes."', "yes"),
        c('"No. You\'re the only one I can\'t fool."', "no"),
        c('[Thievery: while she talks, lift the skinning knife from her belt]', check=dict(Skill="SkillThievery", DC=26, Success="lifted", Failure="caught", CommanderOnly=True))),
    dl("yes", '''"Yes." {n}She considers that, frowning, as though you had told her the depth of a ford.{/n} "Honest, at least. I was defenceless the night you blew the horn. My own vow opened my hand for you. I did not choose it."
{n}She stands.{/n} "But I chose the rest. The count, the meat, every day since. Mark that, fox. You caught me by a trick once. Everything after that, I walked into on my own feet, looking where I was going."''',
        c("Continue", "end", flags=(JESTER_SEEN,))),
    dl("no", '''"Liar." {n}But she looks pleased, which she hides badly, as always.{/n} "You fooled me with a horn. You would fool me again tomorrow if it would make you laugh." {n}She stands.{/n} "But you came back afterwards, and stood where I could see you. That is the thing I did not expect. The fox in the stories never comes back to the henhouse by daylight."''',
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
"Luck," says Delamere, and takes her hand from your back, slowly. "Jester's luck. But you did not close your eyes." {n}She looks at the target, and then at you, and the yard goes quiet around the three of you.{/n} "Come again. Both of you. I have not had pupils in a long time. I had forgotten that I liked it."''',
        c("[Promise to come again.]", flags=(LESSONS,))),
], requires=("trickster.ever", FIRST_MEAT), forbids=(CLOSED, LESSONS, KYADO_JUDGED), delay=24, optional=True)


# --- Old Deadeye's house (Drezen's chapel of Erastil; optional): the god who does not answer her -------------------
# The chapel and its priest are authored. The canon under it: at her seal, Erastil answers his faithful with "A stag
# bellows in the distance" (TombOfDelamere_BookEvent/Cue_0067 a58f2095); Kyado keeps the temple's lore.

visit(P + "woken.old_deadeye", "Old Deadeye's house", [
    nar("bell", '''{n}The message comes from a priest you have never met: Brother Haddo, who keeps the crusade's little chapel of Erastil down in the lower town, two rooms and a bell and a bean patch behind a wall. The Blessed, he writes, has been kneeling in his chapel since before first light. His parishioners are soldiers' wives who come to pray for husbands in the Wound, and they will not come in past her. Would the Commander be so kind.{/n}''',
        c("Continue", "inside")),
    nar("inside", '''{n}The chapel smells of beeswax and wet wool. The altar is a plain board painted with a longbow and a single arrow, the way Erastil's churches paint him now, and on the step below it Delamere kneels with her bow across her thighs and her head up, not bowed, the way a hound waits at a door.{/n}
{n}Brother Haddo, a stooped Mendevian with soil under his nails, hovers in the vestry doorway. Three women with shawls over their heads wait in the porch, not quite daring the threshold.{/n}''',
        c("Continue", "silence")),
    dl("silence", '''"Sit, stag. Not there; that bench is for his people." {n}She does not turn.{/n} "Every night since the crypt I have prayed. On my knees, in my woods, the old words, the ones my mother taught me before I could draw a bow. Every night. Nothing. Not a feather. Not a track in the snow."
{n}She jerks her chin at the vestry.{/n} "Yesterday that one put his hands on a sick child in the camp, and asked Old Deadeye for her, and the fever broke before he had finished the words. A bean-grower. In a city."''',
        c('"Maybe Erastil has already said everything he meant to say to you."', "seal"),
        c('"Ask the priest how he does it."', "haddo"),
        c('"He\'s been listening to you for a very long time. Maybe he\'s gone a little deaf."', "deaf")),
    dl("deaf", '''{n}Her head turns, slowly.{/n} "You will joke in his house?"
{n}Then something twitches at the corner of her mouth, and she looks back at the painted bow.{/n} "My mother said the same. When the snows came late and the elk went south without us. 'He is old, girl. Shout.'" {n}The twitch goes.{/n} "I have shouted, stag. Every night. Ask the priest, then. Ask him how a bean-grower gets an answer."''',
        c("Continue", "haddo")),
    nar("haddo", '''{n}Brother Haddo comes forward because there is nothing else he can do, wiping his hands on his habit.{/n} "The prayer isn't mine, Commander. It's the church's. Hearth and field and neighbour. 'The village is the hand, the family is the fingers.' We say it at every wedding." {n}He glances at the woman on the step, and swallows.{/n} "Drezen is a village with ten thousand fingers. That's how I was taught to see it at the seminary in Vyre. He hears me for their sake, not mine."''',
        c("Continue", "vyre")),
    dl("vyre", '''"Ten thousand fingers." {n}She says it the way she said "kindling" at the south gate.{/n} "A hand with ten thousand fingers is not a hand. It is a thing in a jar in a sorcerer's cellar." {n}She rises, and the priest steps back without meaning to.{/n} "Your seminary taught you well enough, bean-grower. You are not a fool, and the child lived. But you pray to a god I do not know. Mine counted."''',
        c('"Maybe yours still does."', "seal")),
    dl("seal", '''{n}She goes still.{/n} "Say that plainly. I am too old for riddles, and you are too fond of them."''',
        c('"Kyado says that when Erastil\'s faithful knelt at your seal, a stag bellowed far off in the woods. Every time. Your god has been calling over your grave for as long as there have been pilgrims to hear it."', "stag",
          forbids=(STAG_TOLD,)),                                                   # retired by gating (Q6; index kept)
        c('"When I knelt at your seal and asked him for help, a stag bellowed somewhere far off. Then the seal broke under my hands. I heard it."', "stag_seen",
          requires=(ERASTIL_ANSWERED,)),
        c('"Brother Haddo. A stag bellowing over a grave. What would your church make of that?"', "stag_haddo",
          forbids=(ERASTIL_ANSWERED,))),
    dl("stag_seen", '''{n}She goes very still.{/n} "You knelt at my stone. You asked him." {n}Her eyes go over your face as if she were reading tracks in it.{/n} "And he answered you. With a stag's voice." {n}It is not a question, and it is not quite a comfort either.{/n} "He never once answered me with a voice, stag. Only with the one he sent."''',
        c("Continue", "stag")),
    nar("stag_haddo", '''{n}Brother Haddo turns his hat round in his soil-black hands.{/n} "The stag is his, Commander. Old Deadeye's own beast. When the old books say a stag called at a holy place, they mean the god was listening." {n}He glances at the woman on the step, and then away.{/n} "Or a stag was in rut, and somebody wanted it to mean something. I have been a priest thirty years and I have never learned to tell the two apart. But a stag called in that crypt, from what I hear, and she came up out of the stone. I would not presume to say which it was."''',
        c("Continue", "stag")),
    dl("stag", '''{n}For a heartbeat she does not breathe. Then she sits down, hard, on the altar step, as if her knees had been cut.{/n} "A stag."
"Over my grave." {n}Her hand goes to her breastbone, where the pilgrims said the arrow went in.{/n} "The only word he ever spoke to me with a mouth, he said with a stag's. 'Hunt me.' If he said anything over the stone while I lay under it, I could not hear it through the seal. I was holding the string."''',
        c("Continue", "lied", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "borrowed", forbids=(LIED,)),
        c("Continue", "borrowed", requires=(CONFESSED,))),
    dl("lied", '''{n}She looks up at you, and her face is so open that it hurts to see.{/n} "Then it is as you told me. He sent you. He called, and at last he found a stag loud enough." {n}She takes your hand and presses it, hard.{/n} "I will not doubt you again. I swear it, here, in his house."
{n}Somewhere in your chest, a small cold weight settles and does not move.{/n}''',
        c("[Say nothing.]", "haddo_end"),
        c('"Delamere... it wasn\'t like that."', "not_like")),
    dl("not_like", '''"No?" {n}She waits. The chapel waits.{/n} "Then tell me what it was like."''',
        c('"...Another time. Not in front of his priest."', "haddo_end")),
    dl("borrowed", '''{n}She looks at you, and there is something new in it: not suspicion, not quite. The look a tracker gives a set of prints she has been following for days, when she understands at last which way they are going.{/n}
"You blew a stag's call on my horn, and I came." {n}Her mouth tightens.{/n} "You borrowed my god's voice, jester. Did you know?"''',
        c('"Not until tonight. I\'m sorry if that spoils it."', "spoils"),
        c('"I\'d like to say it was all my own idea."', "own_idea")),
    dl("spoils", '''"Spoils it." {n}She shakes her head, slowly.{/n} "Nothing is spoiled. A snare is not less true because the hare did not set it. If my lord left his call lying over my grave, then a jester picked it up and blew it. That is how he always worked. He never did a thing himself if a fool would do it for him."''',
        c("Continue", "haddo_end")),
    dl("own_idea", '''"I know you would." {n}She almost laughs.{/n} "You would steal the credit off a god's plate and eat it in front of him. Do not do it in his house. He has a long bow and a longer memory, and I have only just got back on speaking terms with him."''',
        c("Continue", "haddo_end")),
    dl("haddo_end", '''{n}She gets up and turns to the priest, who flinches.{/n} "Bean-grower. Your rows are crooked; I saw them through the wall. Straighten them before the spring or the rain will take the soil down into the street." {n}She unslings the brace of hares at her belt and lays them on the altar, under the painted bow.{/n} "The first for him. The rest for the women in your porch. They have been standing in the cold for my sake since dawn, and I did not see them. That was a sin. Tell them it was mine."''',
        c("Continue", "out")),
    nar("out", '''{n}She walks out past the three women. One of them, the youngest, reaches out without thinking and touches the hem of her grave-leathers as she goes by, the way you would touch a relic. Delamere stops, and looks at her, and puts a hand on her head for the space of a breath, and goes on.{/n}
{n}Out in the street she waits for you to catch up, and matches her step to your limp.{/n} "Tonight I will pray again," she says. "Not louder. He is not deaf. I will only listen harder."''',
        c("[Walk with her as far as the gate.]", flags=(DEADEYE,))),
], requires=("trickster.ever", STAG_TOLD), forbids=(CLOSED, DEADEYE), delay=48, optional=True)


# --- The names (the crypt wall; optional): "I will count them later. All of them." (the waking, gone) ------------------

visit(P + "woken.names", "The names", [
    nar("wall", '''{n}She has taken the lamp from its hook in the crypt and hung it on the carved stag's antler, which Kyado would think was sacrilege and she thinks is what antlers are for. Below it the wall is scored with lines of old Kellid letters, cut small and deep with a chisel she must have borrowed from someone who has not noticed yet. Stone dust lies in drifts along the floor. Her hands are white with it to the wrist.{/n}''',
        c('"What are you carving?"', "names")),
    dl("names", '''"Names." {n}She does not stop.{/n} "I told you I would count them. The ones I can remember. I wake in the night now with a name in my mouth, like a pip, and if I do not cut it before morning it is gone again."
{n}She taps the first line with the chisel.{/n} "The Stone Hares. That is their mark, the hare with its ears back. Under it, everyone of theirs I knew. Old Tsergun, who kept the ford. His wife, who could not keep a secret. Their girl who tracked foxes. She has no name on the wall yet. I cannot find it."''',
        c('"How many so far?"', "how_many"),
        c("[Look along the wall.]", "look")),
    nar("look", '''{n}The lines go on further than the lamp reaches. There is a hare, and a crooked ash tree, and a mark like an otter, and a mark like three stones, and under every mark a column of names. Some are cut clean. Some have been started and scratched through and started again.{/n}''',
        c("Continue", "how_many")),
    dl("how_many", '''"Six hundred and four." {n}She says it at once; she has been counting as she cut.{/n} "Eleven villages. I walked them every season for twenty years, and I knew every soul in them, and I have remembered six hundred and four. There were more. There were always more. The ones I cannot find are the ones who never gave me trouble." {n}Her mouth twists.{/n} "That is a hard thing to learn about yourself, stag. That you remember the thieves and forget the ones who kept the law."''',
        c('"You remember the girl who tracked foxes."', "girl"),
        c('"Why cut them here, in the crypt?"', "why_here")),
    dl("why_here", '''"Because the Horned One's people ate here. They put their bowls where my head lay and sang over a dead boy." {n}She blows the dust out of a letter.{/n} "I have scrubbed this place until my knuckles bled and it still smells of them. So I am giving it better company. Let the next witch who comes down those stairs to feast find six hundred Kellids waiting for her on the wall. Let her eat under that."''',
        c("Continue", "girl")),
    dl("girl", '''"I remember her hands." {n}The chisel stops.{/n} "Small, with bitten nails. She would go down on her belly on the ice and put her cheek to it, and tell you where the fox had crossed by the way the frost had closed. Nine winters old." {n}She presses the heel of her hand into her eye, and leaves a white smear of stone dust.{/n} "Her mother called her something short. A bird's name, I think. Wren? Linnet? I have cut both and scratched both out. Neither is right."''',
        c('"Leave a space for it. It may come back to you."', "space"),
        c('"Cut the hare\'s mark and leave it at that. She\'d know herself."', "mark"),
        c('[Take the chisel] "Show me the letters. I\'ll cut what you can remember of her, and you can tell me if it\'s wrong."', "cut")),
    dl("space", '''"A space." {n}She considers the wall.{/n} "The Stone Hares always left a place at the fire for the ones out hunting. You did not sit in it, even if it was empty all night." {n}She scores a short line under the hare, and leaves the stone after it smooth.{/n} "Very well. Her place at the fire. If her name comes back, she can sit in it."''',
        c("Continue", "boy")),
    dl("mark", '''"She would." {n}She thinks about it, and nods.{/n} "She would have laughed at me for fussing. She was a hard little thing; she had to be, with that mother." {n}She cuts a small hare under the others, ears back, running.{/n} "There. That is what she was. It will do until I remember the rest."''',
        c("Continue", "boy")),
    dl("cut", '''{n}She looks at you, and then, slowly, she gives you the chisel.{/n} "Hold it like this. Not like that; you hold it like a man holding a stolen purse. Like this." {n}She stands behind you and closes her hand over yours, stone-cold and white with dust, and guides the first stroke.{/n} "Nine winters. Tracked foxes. Bitten nails. The Stone Hares' girl, who put her cheek to the ice." {n}Four strokes, five. What you cut is not a name. It is a description, in a stranger's clumsy hand, in a language you cannot read.{/n}
"There," she says, very quietly, into your hair. "That is her. Better than a name."''',
        c("Continue", "boy")),
    dl("boy", '''{n}She takes the chisel back and moves along the wall, to a place a little apart from the villages, low down, where the lamp barely reaches. Four small marks are already cut there, in a row, like the four finger bones she found in the drain.{/n}
"The farm boy. The one they ate." {n}Her voice does not change.{/n} "I never knew him. He was born long after me. But he died on my grave, and so he is mine. I have cut him with my own people, because he has no one else to be with."''',
        c('"What name did you give him?"', "no_name"),
        c("[Say nothing.]", "no_name")),
    dl("no_name", '''"None. I do not know it, and I will not make one up. That would be a lie told to the dead, and the dead have been lied to enough." {n}She sits back on her heels.{/n} "When your war is done, if I live, I will walk three valleys over and find his people, if there are any, and ask. Then I will come back and cut it."
{n}She looks up at you.{/n} "The witch's bowls on my grave, and his bones in my drain. I cannot undo either. I can do this. It is not much. It is what I have."''',
        c('"It\'s a lot more than anyone else did for him."', "more"),
        c("[Sit down beside her in the dust.]", "sit")),
    dl("more", '''"Anyone else was eating him." {n}She says it flatly, and then, after a breath, less flatly.{/n} "Thank you. You say the right thing sometimes, jester, when you are not trying. Sit down. You are blocking my light."''',
        c("Continue", "sit")),
    nar("sit", '''{n}You sit beside her in the stone dust under six hundred and four names. She does not pick the chisel up again. After a while she leans her shoulder against yours, and you can feel through it the slow ache of a woman who has been holding a chisel since before dawn, and does not intend to say so.{/n}
{n}"Tomorrow," she says, to the wall. "Another fifty. Then another. By the new moon I will have them all, or all I am going to get." She lets her head drop onto your shoulder. "Wake me if I sleep. I have done enough of that in this room."{/n}''',
        c("[Stay until the lamp gutters.]", flags=(NAMES,))),
], requires=("trickster.ever", TABLE), forbids=(CLOSED, NAMES), delay=48, optional=True)


# --- The hide (after the commit; optional): the stag hide from the blind, cut to the leg she broke ------------------

visit(P + "woken.hide", "The hide", [
    nar("door", '''{n}She comes in by the door this time, which is how you know it is a formal visit. She has a bundle under her arm, wrapped in sacking, and a length of knotted cord looped over her wrist, and she stops just inside the threshold and looks around your quarters as if she were pricing a horse.{/n}
{n}Outside the window the sky over the north wall is the colour it always is now: bruised, and faintly lit from below. The Wound does not sleep. Neither, it seems, does she.{/n}''',
        c("Continue", "sit")),
    dl("sit", '''"Sit. Boots off. The bad leg." {n}She does not wait to see whether you obey. She kneels, and lays the cord along the outside of your leg from hip to heel, and ties a knot in it at the knee, and another at the ankle, and a third where the old wound is, and all the while her lips move, counting.{/n}''',
        c('"What is this?"', "what"),
        c("[Let her measure.]", "what")),
    dl("what", '''"The stag." {n}She unwraps the bundle. It is the hide from the blind, or a long strip of it, scraped and smoked and worked soft, the pale belly hair turned inward.{/n} "I kept the best of him for this. A hunter does not let a good hide rot, and I could not think of anyone else I wanted to wear it."
"You walk on the outside of that foot now, the way I showed you, and it is too much for the ankle. It rolls. I have watched it roll on your stairs and on my hills. So." {n}She lays the hide against your shin.{/n} "A brace. Lace it tight in the morning, loose at night. It will not make you walk straight; you would not let the priests do that, and I would not have you let them. It will stop you falling on your face in front of your soldiers."''',
        c('"You made this yourself?"', "made", forbids=(KYADO_DEAD,)),
        c('"I thought the limp was the point. So I\'d remember."', "remember"),
        c('"You made this yourself?"', "made_alone", requires=(KYADO_DEAD,))),
    dl("made", '''"Who else? The boy cannot sew. He tried to mend his own habit once and sewed it to his knee." {n}She is lacing as she talks, quick and rough, the way she cut the arrow out.{/n} "Four nights. My eyes are not what they were. A needle is a harder thing to aim than an arrow."''',
        c("Continue", "tight")),
    dl("remember", '''"You will remember." {n}She pulls the first lace tight enough to make you hiss.{/n} "Every stair. Every frost. That is my mark on you and it is not going anywhere. But a mark is not a punishment. I did not break your leg to watch you fall over, jester. I broke it because you ran well and I had to stop you somehow."''',
        c("Continue", "tight")),
    nar("tight", '''{n}When she is done she sits back on her heels and looks at her work. The brace runs from below your knee to the arch of your foot, laced up the outside with gut, to carry the weight the torn thigh above it will not. Over the shin she has stitched a small mark into the hide in red thread: an arrow, flying, with nothing in front of it.{/n}
{n}"Stand," she says. You stand. The ankle holds. She watches you walk to the window and back, and something in her face eases that you did not know was tight.{/n}''',
        c("Continue", "count")),
    dl("count", '''"Good. Now hear me, because there is a thing I have been meaning to say, and I say things badly indoors." {n}She stays on her knees on your floor. It does not make her look any smaller.{/n}
"I have walked this city, stag, the way I used to walk my valleys. I have heard what they say in your yard, and in the King's tavern, and on the walls. There are a great many people who think they have a claim on you: soldiers, priests, petitioners, the whole crowding hive of it. Some of them are right."''',
        c('"Does that bother you?"', "bother"),
        c('"I\'m not going to lie to you about it."', "no_lie")),
    dl("bother", '''"Bother me?" {n}She considers it honestly, as she considers everything.{/n} "In my day a hunter who brought meat to one hearth and not the rest was a thief, whatever he called it. A hunter who fed every hearth in the village was doing his work." {n}She shrugs.{/n} "I will not be a hearth you visit when the others are cold. That is all. I will be fed, or I will go and feed myself. I have done it before."''',
        c("Continue", "names")),
    dl("no_lie", '''"No. You have lied to me once, or you have not, and either way you know what it cost." {n}She looks at you levelly.{/n} "I did not ask for the truth. I told you I have been counting. I know already." {n}A shrug.{/n} "In my day a hunter who fed every hearth in the village was doing his work. I will not be a hearth you visit when the others are cold. That is all."''',
        c("Continue", "names")),
    dl("names", '''"One thing more." {n}She gets up, stiffly, and brushes off her knees.{/n} "When I ask you their names, you tell me. All of them. Every one who sits at your fire. I do not need to like them. I may not. But I will not live in a village where I do not know who is sleeping next door, and what they did in the bad winter." {n}Her mouth twitches.{/n} "That is not jealousy, whatever the bards will say. It is how a village lives."''',
        c('"You\'ll have every name you ask for."', "promise"),
        c('"And if you don\'t like what they did in the bad winter?"', "winter")),
    dl("winter", '''"Then I will tell them so, to their faces, and they will tell me what I did in mine, and we will both be right." {n}She almost smiles.{/n} "That is how a village works, stag. Nobody likes anybody very much. Everybody knows everybody. And when the wolves come down, everybody takes a spear."''',
        c("Continue", "promise")),
    dl("promise", '''"And hear the rest, so you do not mistake me. Knowing them is not sitting down with them. When I have looked each of them in the face, I will decide whether I eat at your fire, or at mine, with you coming to me. That is mine to choose. Not yours, and not theirs." {n}She picks up the knotted cord from the floor, winds it round her hand, and puts it away inside her jerkin, over her heart, where a city woman would keep a letter.{/n} "I will keep the measure. In case you grow." {n}She goes to the door, and stops, and looks at the brace on your leg with the small red arrow on it.{/n}
"You wear my mark on your leg and my hide on your mark. In the old days that would have meant something, in the hills. I will not tell you what. You would only laugh." {n}She goes.{/n}''',
        c("[Lace it looser, for the night.]", flags=(HIDE,))),
    # Authored: a prior who died before her waking cannot have helped with the brace.
    dl("made_alone", '"I cut it. I stitched it. Whose hands did you think these were?" {n}She is lacing as she talks, quick and rough, the way she cut the arrow out.{/n} "Four nights. My eyes are not what they were. A needle is a harder thing to aim than an arrow."',
        c("Continue", "tight")),
], requires=("trickster.ever", COMMITTED), forbids=(CLOSED, HIDE), delay=48, optional=True)


# --- Doe in fawn (optional): crusade poachers in her woods, and whose law judges them ------------------------------------

visit(P + "woken.poachers", "Doe in fawn", [
    nar("trees", '''{n}A charcoal-burner's boy brings you out to the woods below her temple at a run, and will not say why, only that the Blessed "has got three of yours, and she's being very calm about it".{/n}
{n}She has. Three crusaders in Mendevian surcoats sit in the leaf litter with their backs to three oaks and their wrists tied behind the trunks with their own bowstrings. Their bows lie snapped in a neat pile. Between them and her, on the grass, lies a doe, gutted, and beside the doe, on a fold of her own hide, what came out of her: a fawn, unborn, not much bigger than a cat.{/n}''',
        c("Continue", "calm")),
    dl("calm", '''"Stag." {n}She does not look round. She is sitting on a stump with her bow across her knees, and her voice is perfectly pleasant.{/n} "Yours, I think. They told me so, very loudly, when I took their bows. The crusade. The Commander. They told me whose meat they were fetching and whose name would hang me if I touched them."
"I have not touched them. I have been waiting for you. I wanted to hear you say it too."''',
        c('"They\'re hungry, Delamere. The whole army is hungry."', "hungry"),
        c("[Look at the fawn.]", "fawn")),
    nar("fawn", '''{n}It lies curled on the hide as it lay inside its mother, legs folded, eyes shut. Somebody has wiped it clean. It was not one of the soldiers.{/n}''',
        c("Continue", "hungry")),
    dl("hungry", '''"Hunger I forgive. I have been hungry. I have eaten bark." {n}She stands, and walks to the doe, and crouches by the fawn.{/n} "This I do not forgive. A doe in fawn in the spring is two deer next year and four the year after. Every child in the hills knew it. You let her pass. You let her pass even when your belly is cutting you in half, because she is the village's meat for ten winters and you are one hungry man."
{n}The youngest soldier, a boy with a bad moustache, opens his mouth. She looks at him. He shuts it.{/n}''',
        c("Continue", "law")),
    dl("law", '''"In my day, a man who took a doe in fawn from a village wood lost the two fingers he draws with. Here." {n}She holds up her own right hand, first and second fingers together.{/n} "He could still work. He could still hold a spear when the wolves came. He could never again take the village's meat from it."
"These are your men, in my wood. So you choose, stag. Whose law?"''',
        c('"Mine. The crusade has a provost and a whipping post. They answer to me, not to you."', "provost", flags=(POACHERS_PROVOST,)),
        c('"Yours. Your wood, your law. I won\'t stand between you."', "hers", flags=(POACHERS_HERS,)),
        c('[Bluff: turn to the soldiers] "You idiots. Do you know whose doe that was?"',
          check=dict(Skill="CheckBluff", DC=20, Success="bluff", Failure="bluff_fail", CommanderOnly=True))),
    dl("provost", '''{n}She looks at you for the space of two breaths.{/n} "A whipping post." {n}Then she nods, once.{/n} "Your law is softer than mine and it forgets faster. But you said it to my face, in front of them, and you did not pretend it was mercy." {n}She cuts the bowstrings with three flicks of her knife.{/n} "Take them to your post. And tell your provost from me: the next one I find with a doe in fawn, I will not wait for you."''',
        c("Continue", "meat")),
    dl("hers", '''{n}She is quiet. The soldiers are very quiet.{/n} "My law." {n}She walks down the line of them, and stops in front of the boy with the bad moustache, and takes his right hand from behind the tree and holds it up to the light, as if she were looking at a fish.{/n}
"This one shot her. I watched him. The other two carried." {n}She lets the hand drop.{/n} "Hear me, all three. The law says the fingers. But the law was made for villages, and you are not a village; you are a war, and a war needs its fingers. So."''',
        c("Continue", "sentence", forbids=(VILLAGE_REFUSED, VILLAGE_CLANS)),
        # Polish r4 (Sol BEL): no village below her temple unless the count gave her one; then the work is at Drezen's camps.
        c("Continue", "sentence_camp", forbids=(VILLAGE_GIVEN, VILLAGE_FORCED))),
    dl("sentence", '''"You will dig." {n}She points up the hill, to the clearing below the temple where her village's first longhouses are going up.{/n} "Every day for one season, when your captain can spare you, you will come to my village and dig its ditches and fell its timber, and you will eat at its fires, last. When you go back to your war, you will know the name of every child in it, and you will think of their faces every time you see a doe."
{n}She cuts them loose.{/n} "If you do not come, I will come for the fingers. I know where your tents are. I have been in them."''',
        c("Continue", "meat")),
    dl("sentence_camp", '''"You will dig." {n}She points down the valley, to the smoke over Drezen's camps.{/n} "Your Commander keeps my people behind the walls, in the mud by the river, in tents that leak. Every day for one season, when your captain can spare you, you will go to those tents and dig their ditches and cut their firewood, and you will eat at their fires, last. When you go back to your war, you will know the name of every child there, and you will think of their faces every time you see a doe."
{n}She cuts them loose.{/n} "If you do not go, I will come for the fingers. I know where your tents are. I have been in them."''',
        c("Continue", "meat")),
    nar("bluff", '''{n}You walk down the line of them slowly, the way a magistrate walks, and stop in front of the boy with the bad moustache, and let your voice drop to a whisper that carries.{/n} "That is Delamere the Blessed. Erastil's own. And that doe was his. He sends one like her into every wood where his priestess walks, in fawn, to see who will take her." {n}You let that sit.{/n} "The last man who did lost his hands to the frost that winter. Both of them. Nobody could say why."''',
        c("Continue", "bluffed")),
    nar("bluffed", '''{n}The boy goes grey. One of the others starts to pray, in Mendevian, very fast. By the time you have finished your sentence all three of them are offering, without being asked, to carry every stick of her firewood until the thaw, and swearing on their mothers that no man in their company will draw a bow in her woods again.{/n}
{n}Delamere watches this with an expression you have not seen on her before. It takes you a moment to recognise it as the look of a woman trying very hard not to laugh in church.{/n}''',
        c("Continue", "bluff_her", flags=(POACHERS_TRICKED,))),
    dl("bluff_her", '''{n}She cuts them loose and sends them running up the hill for firewood, and only then turns to you, and her face is thunder.{/n} "You put a lie in my lord's mouth. In my wood. Over a dead doe." {n}She jabs a finger into your chest.{/n}
"And it will work better than any law of mine ever did, because by tonight every tent in your army will know it, and by spring there will not be a doe in fawn taken between here and the river." {n}She shakes her head.{/n} "I hate you a little. Carry the fawn."''',
        c("Continue", "meat")),
    # Authored: the soldier recognizes a local doe, undermining the claim that Erastil sent her.
    nar("bluff_fail", '''{n}You try. You get as far as "Erastil's own doe" before the boy with the bad moustache, who is braver than he looks, says, "Beg pardon, Commander, but I know that split ear. We caught her stealing turnips outside camp last week. She ran when we threw stones. Didn't look like a god's beast then."{/n}
{n}Delamere closes her eyes, briefly, as though praying for patience from a god who has given her very little of it.{/n}''',
        c("Continue", "law_again")),
    dl("law_again", '''"You should have asked him about the turnips first." {n}She opens her eyes.{/n} "Do not play your jester's games over a dead mother, stag. Not in my wood. Answer me plainly. Whose law?"''',
        c('"Mine. The crusade has a provost and a whipping post. They answer to me, not to you."', "provost", flags=(POACHERS_PROVOST,)),
        c('"Yours. Your wood, your law. I won\'t stand between you."', "hers", flags=(POACHERS_HERS,))),
    nar("meat", '''{n}When they are gone she kneels by the doe and cuts the first strip of fat from along its spine for Old Deadeye, and says the low Kellid words over it. Then she takes the fawn in her two hands, very gently, and carries it up the hill to a place under an ash tree, and digs, with her knife, until there is a hole deep enough that the foxes will not have it.{/n}
{n}You help, as much as your leg lets you. She does not tell you to stop.{/n}''',
        c("Continue", "grave")),
    dl("grave", '''"The doe goes to your army. They are hungry; I did not lie about that. It would be a worse sin to let her rot." {n}She pats the earth down flat over the fawn, and sits back.{/n}
"I did not ask you out here to judge three boys. I could have judged three boys in my sleep; I did it for twenty years. I asked you out here to see what you would say when your army and my woods wanted different things." {n}She looks at you across the little grave.{/n} "Now I know. Go home, stag. Take your meat."''',
        c("[Shoulder the doe.]")),
], requires=("trickster.ever", FIRST_MEAT), forbids=(CLOSED, POACHERS_PROVOST, POACHERS_HERS, POACHERS_TRICKED), delay=48,
    optional=True)


# --- Path fit (13 directive update 2026-09-29 / ROUTE-BRIEF-R §2; recorded in PP10) ---------------------------------------
# PATH_FIT is each scene's class today: T (a device, or gated on the Trickster), N-all or N-fit. Every Delamere scene is T:
# she is a living woman only because the Commander woke her with the stag's roar (crypt.stag and its twins), and every
# later beat reads that waking. Kyado's horn lore is the device's primer. PATH_FIT_V2 is empty: on every other path canon
# fate stands (destroyed, laid to rest in Drezen, set free, or raised by the Lich as an undead servant), and this romance is
# built on her authored living return, so it has no other-path version (a route design statement, not a canon rule).
from storylines import delamere_trickster as _trickster, delamere_woods as _woods

PATH_FIT = {s["Id"]: "T" for s in _trickster.SCENES + _woods.SCENES + SCENES}
PATH_FIT_V2 = {}
