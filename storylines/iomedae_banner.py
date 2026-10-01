"""Iomedae, the courtship around her banner (Trickster; 11-ROSTER-PLAN-2 §2, veiled until the finale; spec Build sheet R6).

Chapter 3: the Sword of Valor remembers the woman who carried it (a relic's memory, never her message: before the Summit she
"observed you without intervening", Goddesses_Summit/Cue_0087), and her herald prays the Commander's questions and gets no
answer (Herald_Drezen_c3, AnswersList_0017 797452ab, return Cue_0076 2ea22fac). The Commander tests it with a word sealed in
the foot of the pole. Chapter 4: in the Abyss there is no banner; the herald tells the Acts (Nexus Herald_Camp AnswersList_0022
d1abc904, return Cue_0010 50ab8449). Chapter 5: the Summit (AnswersList_0136 7f18896f, E14b), the bare platform where the
wager is conceived, and her first words to the Commander in her own voice, after her herald's fate. After her concession: the
dream in which she chooses to look as she did. Chapter 6: the night before Threshold.

The device, the disputation, the Threshold, the reactions and the pages live in iomedae_trickster. Path fit: all T (v1).
"""
from story_format import c, n, p, scene
from storylines.iomedae_trickster import (
    E, REL, CLOSED, STARTED, COMMITTED, DREZEN, IOMEDAE_UNIT, SUMMIT_LIST, KEY_DIES, KEY_LATCH, IZ_DONE, BANNER_HELD,
    ORDER_BANNER, HERALD_SAVED, HERALD_FELL, HERALD_FOUGHT, NENIO, DREAM_BANNER, SENT_AWAY, QUESTION_SENT, ASKED_WHOSE, ASKED_MIND,
    ASKED_BACK, HERALD_ANSWERED, BRIDGE_SEEN, TESTED, WORD_ARODEN, WORD_LIAR, WORD_PLEASE, TEST_DONE, SLIP_BURNED,
    BRIDGE_TOLD, DREAMS_TOLD, ABYSS_SILENCE, SUMMIT_ASKED, PLAN, HERALD_DREAM, SPOKEN, DISPUTED, DECLINED, MORTAL_SEEN,
    EVE_SEEN, BRIDGE_KNOWN, FALSE_FACE, QUEEN_SAW, io, nar, remote, tag)

SCENES = []

HERALD3_LIST = "797452ab97defe74487c091e59379224"   # c3/Drezen_C3/Herald/AnswersList_0017 (the herald's questions)
HERALD3_BACK = "2ea22fac3bb0ed04ba643748d1c2bf8e"   # Herald/Cue_0076 "I am here to illuminate you, Champion."
HERALD4_LIST = "d1abc9044634dec45a396755380c8623"   # c4/Nexus_Camp/Herald_Camp/AnswersList_0022 (personal questions)
HERALD4_BACK = "50ab84494d3f15341bf5f87d712f3030"   # Herald_Camp/Cue_0010 "There shouldn't be any secrets between us..."
SUMMIT_RETURN = "{n}The goddess waits for your decision. So, with rather more amusement, does the Lady in Shadow.{/n}"


def herald(id, text, *choices):
    return n(id, "conversant", text, *choices)


def at_herald(id, title, chapter, entry, nodes, requires, forbids, lists, back, delay=0):
    """Inline on the Hand of the Inheritor's own list, returning to his clean cue."""
    SCENES.append(scene(id, title, "Hand of the Inheritor", chapter, entry, nodes, requires=("trickster", *requires),
                        forbids=(CLOSED, *forbids), delay=delay, last=chapter, optional=True, Relationship=REL,
                        Chapters=[chapter], AnswerLists=[lists], NativeReturnCue=back))
    tag(id)


# --- Chapter 3, 1. The banner's first memory (a relic's memory, not her message). ------------------------------------------

remote(DREAM_BANNER, "What the banner remembers", [
    nar("start", '''{n}You sleep in the citadel, two floors under the platform where the Sword of Valor flies. You have slept there for weeks. Tonight you do not dream of the war.{/n}
{n}It is raining, and you are heavy with it: rain in your cloth, rain running the length of you, rain soaking into the grain of the wood that is somehow also you. A hand closes around you low down, where you are thickest, and lifts. The grip is a swordsman's, callused at the root of every finger. It is cold, and it does not let go.{/n}''',
        c("Continue", "line")),
    nar("line", '''{n}She carries you along a line of soldiers in the last grey of evening. You see her in pieces, the way a banner sees whoever carries it: the edge of a jaw under a dented helm, a wet braid, a gauntlet with the leather worn through at the knuckles. She is young. She is tired in a way that has nothing to do with the day.{/n}
{n}Beyond the soldiers, across a field of black stubble, something waits in ranks that do not shift or cough or stamp against the cold, because nothing in them is alive to mind it.{/n}
{n}A boy at the end of the line is shaking. He is too young for his mail. She stops in front of him and drives your staff into the mud at his feet, and the jolt runs all the way up into your cloth.{/n}
"Look at this, not at them," she says. Her voice is hoarse from shouting and low from not wanting the others to hear. "When the line breaks, and it will, you will not be able to find me. Find this. Where it stands, I am standing. Do you understand me?"
{n}He nods. He is looking up at you. So, you realize, is she, as if she needed telling too.{/n}''',
        c("Continue", "alone")),
    nar("alone", '''{n}Later the line has sunk into the sleep soldiers sleep before a dawn attack, and she sits alone in the mud with her back against your staff. She takes her helm off. You cannot see her face from where you are. You can feel the back of her head against the wood.{/n}
"Tomorrow they will come across that field," she tells you, "and I will be the only one of us who has ever seen them come, and I will have to look as if I have done it a hundred times." {n}A long breath, let out slowly, so nobody will hear it.{/n} "Hold. I will do the rest."
{n}She says it to a banner on a pole in the rain. She says it the way people say the things they would never say to another person.{/n}
{n}Then she puts her helm back on, and gets up, and walks the line again in the dark, stopping at each sleeper long enough to check a strap or tuck in a cloak, and says nothing to any of them, and comes back, and sits down against your staff again, and does not sleep.{/n}''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake with your hand curled around nothing, the fingers bent as if round a staff.{/n}
{n}Above you the Sword of Valor snaps in the wind off the Worldwound, wearing the colours your blood gave it the day you raised it. Nobody told you it could do this. Nobody told you it could do anything but keep demons from stepping out of the air into your streets.{/n}
{n}The herald of Iomedae is in the city. He might know what a relic of hers remembers, and why it would show it to you.{/n}''',
        c("[Go up to the platform and look at it.]", "platform"),
        c("[Turn over and go back to sleep. It was a dream.]", flags=(STARTED,)),
        c('[Have your bed moved to the far tower] "Dreams are for people with less to do."', "moved")),
    nar("platform", '''{n}The stair is cold. The sentry at the top salutes and does an admirable job of not looking surprised.{/n}
{n}The banner is only a banner: heavy cloth, its old device drowned under the colours it took from you. The staff is not the staff from the dream. Staves rot and are replaced. The cloth is what is left of her, if anything is, and in this wind it is trying to get away from the pole and go somewhere.{/n}
{n}You put your hand on the staff, low down, where it is thickest. The wood is dry. Nobody is holding the other end.{/n}''',
        c("[Say goodnight to it, since there is nobody to hear.]", flags=(STARTED,)),
        c("[Go back down without a word.]", flags=(STARTED,))),
    nar("moved", '''{n}By noon your cot, your maps and your armour stand in a round room at the far end of the citadel, where the wind comes in through arrow slits and nothing flies overhead. The quartermaster does not ask why. That is what quartermasters are for.{/n}
{n}You sleep badly there, and dream of nothing but work. It is, you tell yourself, an improvement.{/n}''',
        c("Continue", flags=(CLOSED, SENT_AWAY))),
], requires=("trickster",), delay=0, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 3, 2. The herald prays the question (inline on his list). -------------------------------------------------------

ASK = (
    c('"Ask her whose dream it was: hers, or the banner\'s."', flags=(QUESTION_SENT, ASKED_WHOSE)),
    c('"Ask her if she minds. It was her banner. I bled on it."', flags=(QUESTION_SENT, ASKED_MIND)),
    c('"Ask her if she wants it back."', flags=(QUESTION_SENT, ASKED_BACK)),
    c('"Don\'t. I\'ll work it out for myself."', abort=True),
)

at_herald(E + "herald.question", "What the banner remembers", 3,
    '"A question about the Sword of Valor. Does it remember the hands that carried it?"', [
    herald("start", '''{n}The Hand of the Inheritor turns his golden head toward the citadel, as if he could see the banner through the stone.{/n} "Remember? It is a relic of my lady's mortal days, Champion. Such things are not dead cloth. They keep the shape of what was done with them, as a blade keeps the edge it was given."
{n}He looks back at you more closely.{/n} "Why do you ask?"''',
        c('[Tell him the truth] "Because last night I was the banner. In the rain, in someone\'s hand, the night before a battle."', "truth"),
        c('"Call it a hypothesis. I\'d like to know what I\'m sleeping under."', "hypothesis"),
        c('[Joke] "It snores. I wanted to know whose habit that is."', "joke")),
    herald("truth", '''{n}The herald is silent for the space of several breaths, and when he speaks again his voice has dropped the way voices drop in temples.{/n} "Then it showed you her. Before the Starstone, before any of us served her: a woman with a banner and a war."
{n}His hand closes on the hilt of his sword. It is not a threat. It is something to hold.{/n} "It changed under your hand when you raised it. Perhaps it has decided you should know whose it was. Perhaps she is pleased that her chosen should see her as she was."''',
        c("Continue", "ask")),
    herald("hypothesis", '''"A careful answer. You give a great many of those." {n}He does not press it.{/n} "It is said in the Heavens that the relics of the mortal saints keep their memories, and that sometimes, under the right hand, they share them. I have never known this one to do it. It has flown over Drezen, and over the demons who held Drezen, and it showed none of them anything at all."''',
        c("Continue", "ask")),
    herald("joke", '''{n}The herald's face does something complicated and settles on patience.{/n} "It does not snore, Champion. It is the banner my lady carried when she was mortal, before she passed the Test of the Starstone. It has kept demons out of your streets since the day you raised it."
{n}He studies you.{/n} "But you did not ask idly. I have learned that much about you. When you joke, it is because the true answer embarrasses you."''',
        c("Continue", "ask")),
    herald("ask", '''"I can pray your question to her tonight. I pray every night, and she hears." {n}He hesitates, the scrupulous hesitation of a being who will not overpromise.{/n} "I will not promise you an answer. My lady answers deeds more readily than questions. What shall I ask her?"''',
        *ASK),
], requires=(DREAM_BANNER,), forbids=(QUESTION_SENT,), lists=HERALD3_LIST, back=HERALD3_BACK)


# --- Chapter 3, 3. No answer: she observes (Cue_0087). ----------------------------------------------------------------------

THANK = (
    c('"Then I\'ll keep sleeping under it."', flags=(HERALD_ANSWERED,)),
    c('"Thank you for asking her anyway."', "thanked"),
)

at_herald(E + "herald.answer", "No answer", 3, '"Did she answer?"', [
    herald("start", '''{n}The herald does not answer at once. He has the look of someone who has been awake all night and is not used to it.{/n} "No."
{n}He says it as though it cost him.{/n} "I prayed it as you asked it, word for word. I have prayed to her for longer than your city has stood, Champion, and she has always answered me, even when the answer was to wait. Last night there was no answer. There was only..." {n}He searches for the word.{/n} "Attention. As though she had turned her head toward something, and was watching it, and did not wish to be interrupted."''',
        c("Continue", "whose", requires=(ASKED_WHOSE,)),
        c("Continue", "mind", requires=(ASKED_MIND,)),
        c("Continue", "back", forbids=(ASKED_WHOSE, ASKED_MIND))),
    herald("whose", '''"You asked whose dream it was. If it were hers, I think I would know. She does not send dreams to anyone lightly, and she has never sent one without telling her herald first." {n}A pause.{/n} "It is the banner, Champion. I am almost certain it is the banner."''',
        c('"Almost."', "warn")),
    herald("mind", '''"You asked whether she minds what your blood did to her banner. I told you in the first days that I do not call it blasphemy. I will tell you something else now." {n}He lowers his voice.{/n} "I do not think she minds. I think she is curious. I have not seen her curious about a mortal in a very long time."''',
        c('"Is that good?"', "warn")),
    herald("back", '''"You asked whether she wants it back." {n}Almost a smile.{/n} "She gave it to the world long before either of us was thinking of Drezen. I do not think gods ask for things back. But she heard the question, Champion. She did not dismiss it. She only watched."''',
        c('"Watched what?"', "warn")),
    herald("warn", '''"You, I think." {n}He does not seem to find that comforting.{/n} "She watches over the crusade, and over you. How could she not? But this was not the way she watches a battle."
{n}He steps closer, and for once the grandeur goes out of his voice.{/n} "Champion. A relic shows what was. It cannot show you what she is now. Do not mistake the one for the other. Mortals who fall in love with a saint's memory generally end in a cloister, or a ballad, and neither suits you."''',
        *THANK),
    herald("thanked", '''"It is what I am for." {n}He bows, and then, straightening, seems to hear what he has just said, and looks faintly troubled by it.{/n} "Though I confess I have never before been thanked for carrying a question that was not answered. Most people thank me for the answers."''',
        c("Continue", flags=(HERALD_ANSWERED,))),
], requires=(QUESTION_SENT,), forbids=(HERALD_ANSWERED,), lists=HERALD3_LIST, back=HERALD3_BACK, delay=24)


# --- Chapter 3, 4. The gorge: the cloak laid across (the root of the wager). -------------------------------------------------

remote(E + "dream.chasm", "The gorge", [
    nar("start", '''{n}The banner dreams again, and you are in it.{/n}
{n}Night, and running. She is not carrying you upright now; you are over her shoulder like a pike, your cloth wound tight round your staff so it will not catch the wind and slow her. There are perhaps forty of them left behind her, and behind them a sound that is not quite footsteps.{/n}
{n}Then the ground stops.{/n}''',
        c("Continue", "gorge")),
    nar("gorge", '''{n}It is a gorge, or a crack in the world; the dark in it goes further down than dark ought to. There was a bridge. You can see where it was: two iron pins in the rock at her feet, two more on the far side, and nothing between them but the smell of burned rope. Across the gap, twenty strides off, a torch somebody wedged into the far pins is still burning, as if to taunt the people it was meant to guide.{/n}
{n}Behind the forty, the sound gets nearer: patient, and many.{/n}
{n}Someone says her name and asks what they do now. She does not answer him. She drives your staff into a crack in the rock, hard, and her hands go to the clasp at her throat.{/n}''',
        c("Continue", "cloak")),
    nar("cloak", '''{n}It is only a cloak: wool, sodden with the road, the hem black with ash. She takes it off and holds it, and says something you cannot hear over the wind in the gorge. It is too short to be a prayer, or it is a very short prayer. Then she casts it out over the gap the way a fisherman casts a net.{/n}
{n}It should fall. You watch it not fall. It lies across the dark from pin to pin, flat and taut, no wider than a plank, and the wind that should lift its edges goes around it.{/n}
"Walk," she says. "Do not look down. Do not look at me. Walk."
{n}They walk: forty of them, one at a time, on a cloak, over nothing. The boy from the rain is the ninth. She stands at the near end the whole while with one hand on your staff. Her arm is shaking. Her face is not.{/n}''',
        c("Continue", "last")),
    nar("last", '''{n}When the last of them is over she pulls you out of the rock, sets you on her shoulder and steps out onto the cloth herself. You feel it give under her like a wet plank. You feel her feel it. Halfway across, the sound behind reaches the edge, and something reaches after her, and she does not look back.{/n}
{n}On the far side she turns, takes the torch from the pins and throws it down onto her cloak. It burns the way wool burns, quickly and ordinarily, and drops into the dark in pieces, and the things on the other side are left looking at a gap.{/n}
{n}She sits down on the rock without a word, with her back against your staff, as she did in the rain. Somebody brings her another man's cloak. She does not put it on. She sits in the cold in her shirt and mail and watches the far side of the gorge until the dead have given up and gone, which is nearly morning, and only then does she let anyone see her shake.{/n}''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake cold, though the room is not.{/n}
{n}They say of her that she turned her cloak into a bridge. It is a handsome line, and it fits in a hymn. It does not say that she held the thing there with a shaking arm and her own weight, and burned it behind her so nothing could follow. Whether it happened so, or only so in the keeping of a banner that was jammed into a rock and watching, you have no way to know.{/n}
{n}Above you the Sword of Valor goes on snapping in the wind off the Wound.{/n}''',
        c("[Lie awake and think about the gorge.]", flags=(BRIDGE_SEEN,)),
        c("[Get up and write down what you saw while you still have it.]", flags=(BRIDGE_SEEN,)),
        c('[Climb to the platform in your shirt and tell the banner] "You could have warned me."', flags=(BRIDGE_SEEN,))),
], requires=(QUESTION_SENT,), forbids=(BRIDGE_SEEN,), delay=24, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 3, 5. A word in the socket: the Trickster tests whether anyone is sending the dreams. ---------------------------

remote(E + "platform.test", "A word in the socket", [
    nar("start", '''{n}Two dreams, and one herald who swears his goddess did not answer. You have run enough confidence tricks to know how you would test this if somebody else were the mark.{/n}
{n}Near midnight you climb to the platform with the stub of a candle, a strip of paper and a stick of sealing wax. The banner's pole stands in an iron socket set into the stone and packed round with lead, and where the lead has shrunk from the iron there is a crack as wide as a fingernail. You will write one word, small, where no light but yours will ever find it, roll it tight, push it down into the crack and seal it over with wax and the ball of your thumb.{/n}
{n}If the dreams are only the banner remembering, they will never say it. If someone is sending them, she will know what is sitting in the foot of her own banner. A goddess who does not lie ought to have no trouble with one word.{/n}''',
        c('[Write "Aroden." Her god, before she was one; the one who died.]', "sealed", flags=(TESTED, WORD_ARODEN)),
        c('[Write "Liar." If anyone is listening, that will bring her.]', "sealed", flags=(TESTED, WORD_LIAR)),
        c('[Write "Please." Nobody would expect it of you.]', "sealed", flags=(TESTED, WORD_PLEASE))),
    nar("sealed", '''{n}The wax takes your thumbprint. On the stair down you meet the sentry coming up with his lantern, who stops and raises it.{/n}
"Commander? Anything wrong up there?"''',
        c('"Checking the mortar. Carry on."'),
        c('"Nothing that won\'t keep till morning."')),
], requires=(BRIDGE_SEEN, HERALD_ANSWERED), forbids=(TESTED,), delay=12, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 3, 6. The dead knight: the memory never says the word. ----------------------------------------------------------

remote(E + "dream.test", "The oath over the door", [
    nar("start", '''{n}The banner dreams. You go into it listening for your word.{/n}
{n}Stone this time, and cold, and quiet: a hall with a broken roof and snow coming through it. She carries you upright and walks slowly, the way one walks toward something one does not want to startle.{/n}
{n}At the far end of the hall a knight sits on the steps of a dais. His armour is very old and very good, and there is nothing inside it that ought to be moving. Frost lies on his shoulders like epaulettes. When she stops ten paces off he lifts his head, and whatever looks out of the helm is patient, and is not alive.{/n}''',
        c("Continue", "oath")),
    nar("oath", '''"You swore an oath once," she says. "I read it on the way in. It is carved over the door, and your name is under it."
{n}The thing on the steps makes a sound that is not a word.{/n}
"You swore to hold this hall for the living. There are no living here. There have not been for a long while. You are holding it against them." {n}She plants you in the snow between herself and him, takes her hand from your staff, and shows him her empty hands.{/n} "I will not fight you. I think you know that I would win, and I think you know you would not mind. So I will only ask you: whose oath are you keeping?"''',
        c("Continue", "argued")),
    nar("argued", '''{n}It takes a long time. She waits it out standing, with snow gathering on her shoulders and on your cloth. She argues him down the way water argues down a stone: without raising her voice, without leaving, without letting a single one of his answers go unanswered.{/n}
{n}He says the hall is his charge. She says a charge is given for a purpose, and asks him for the purpose. He says the living will return. She asks him how long he has waited, and when he cannot say, she tells him: longer than the living he swore to live. He says that if he lays down the charge he will be nothing. She says that he has been nothing for a long time, and that she is offering him the chance to have been something instead.{/n}
{n}By the end he is only listening.{/n}
{n}Then he stands and draws his sword, sets the pommel against the step and the point in the gap under his breastplate, looks at her, and leans.{/n}
{n}She goes to him afterwards, closes the visor over the empty helm, and sits beside him until the snow has covered the rest.{/n}''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake listening, as you went to sleep listening, for one word. It was not in the dream. It was not in the hall or the snow or anything she said to a dead knight who needed arguing into his rest.{/n}
{n}So it is the banner, remembering, and nobody behind it. You tell yourself that is the answer you wanted. It is certainly the safer one.{/n}''',
        c("Continue", "aroden", requires=(WORD_ARODEN,)),
        c("Continue", "liar", requires=(WORD_LIAR,)),
        c("Continue", "please", forbids=(WORD_ARODEN, WORD_LIAR))),
    nar("aroden", '''{n}You wrote the name of her dead god and pushed it into the foot of her banner, to see if it would sting. The woman in the dream spent the night making a dead man keep his oath. You find you would rather she had not been so busy.{/n}''',
        c("Continue", "slip")),
    nar("liar", '''{n}You wrote "Liar" on a strip of paper and shoved it into the foot of her banner. The woman in the dream spent the night talking a dead man into his grave with nothing but the truth. You find you are not proud of the word.{/n}''',
        c("Continue", "slip")),
    nar("please", '''{n}You wrote "Please" and sealed it under your thumb, because nobody would expect it of you. Nobody did. The woman in the dream was busy being asked for nothing by a dead knight, and giving it to him anyway.{/n}''',
        c("Continue", "slip")),
    nar("slip", '''{n}In the morning the wax on the socket is whole, your thumbprint still in it.{/n}''',
        c("[Leave the slip where it is.]", flags=(TEST_DONE,)),
        c("[Dig it out of the crack with a knife and burn it in the candle.]", flags=(TEST_DONE, SLIP_BURNED))),
], requires=(TESTED,), forbids=(TEST_DONE,), delay=24, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 3, the Queen at the relic: "it was no longer her banner" (GalfreyArrives/Cue_0052). ---------------------------

remote(E + "platform.queen", "No longer hers", [
    nar("start", '''{n}The Queen came to Drezen and went, before anything else, to pray before her goddess's banner, and found, she told you, that it was no longer her goddess's banner. She said it lightly, and then went on to more pressing matters. You have not been able to go on to more pressing matters.{/n}
{n}That night you go up to the platform.{/n}''',
        c("Continue", "night")),
    nar("night", '''{n}From the foot of the pole the banner looks as the Queen saw it: your colours, not hers, snapping over a city you took back with your blood on your hands and some of it on the cloth. A pilgrim would see a relic defaced. A priest would see an omen. The Queen saw a loss, and was too well-bred to say so twice.{/n}
{n}You have been inside it. You have been the thing her hand closed on in the rain, and felt her lean her head against you in the dark, when she thought nobody could hear. The colours are yours. Nothing underneath them has changed its mind.{/n}''',
        c('[Tell the banner] "She\'s wrong. You\'re still hers."', "still"),
        c('[Tell the banner] "Maybe it\'s for the best. Hers or mine, you\'re going to be busy."', "busy"),
        c("[Say nothing. Stand your watch under it until the sentry comes.]", "watch")),
    nar("still", '''{n}The cloth cracks in the wind off the Wound, as it has cracked every night for months. It does not agree with you, or disagree. It is a banner. But you feel better for having said it to something that was there.{/n}''',
        c("[Go down.]")),
    nar("busy", '''{n}It is the kind of thing you say to a horse before a long ride, and you are aware of that, and say it anyway. The banner goes on snapping in the wind. Somewhere under the colours a woman in the rain is telling a frightened boy where to look.{/n}''',
        c("[Go down.]")),
    nar("watch", '''{n}The sentry comes at the change of the watch and finds his Knight Commander standing at attention under the Sword of Valor, alone, in the small hours, like a squire at a vigil. He opens his mouth, and thinks better of it, and takes his post on the other side of the pole, and the two of you stand watch together until morning without a word.{/n}''',
        c("[Go down at morning.]")),
], requires=(DREAM_BANNER, QUEEN_SAW), forbids=(), delay=12, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 3, 7. The herald on Aroden: her god died the year the Wound opened (glossary; Aroden's death in 4606). ----------

at_herald(E + "herald.aroden", "The Last Azlanti", 3, '"Tell me about Aroden. And about her, when he died."', [
    herald("start", '''{n}The Hand of the Inheritor is quiet for a moment, which in him is a long time.{/n}
"The Last Azlanti. The god of humanity. She served him as his herald before she served anyone as a goddess, and when he died she inherited his faithful, the way a daughter inherits a house with the mourners still in it."
"He died in the year the Worldwound opened. The same year. Heaven was in upheaval; there were councils, and speeches, and a great deal of waiting to see. She did not wait. She went to his people and told them the truth, which they did not want, and then she stayed with them, which they wanted less."''',
        c('"You make it sound like grief."', "grief"),
        c('"And the Wound?"', "wound"),
        c('"Why does the banner never dream of him?"', "him")),
    herald("grief", '''"It was grief. She does not call it that. She calls it duty, which is what grief becomes when one cannot afford it."''',
        c("Continue", "why")),
    herald("wound", '''"She has fought it every year it has been open. That it opened when her god died is not a thing she speaks of." {n}He hesitates.{/n} "Some of us think she has been holding a door shut on her own mourning ever since." {n}He catches himself.{/n} "That is not a thing I should say to a mortal."''',
        c("Continue", "why")),
    herald("him", '''"Perhaps because it never saw him. A banner sees the one who carries it. He was a god, and she was a knight on foot in the mud. He never needed carrying."''',
        c("Continue", "why")),
    herald("why", '''"Why do you ask, Champion? You asked me about the banner before. You are asking me about her now."''',
        c('"Because I keep meeting her in the dark, and she keeps being somebody I\'d follow."'),
        c('"I wanted to know what she lost."'),
        c('"No reason."')),
], requires=(E + "dream.chasm",), forbids=(), lists=HERALD3_LIST, back=HERALD3_BACK)


# --- Chapter 3, 8. The morning after the rain (the line breaks; she is where the banner stands). ----------------------------

remote(E + "dream.rain_end", "Where it stands", [
    nar("start", '''{n}The banner dreams, and it is the rain again: the same line of soldiers, the same black stubble, the same boy too young for his mail. But it is morning now, and the things across the field have begun to walk.{/n}
{n}She does not make a speech. She lifts you out of the mud and holds you up, high, with both hands on your staff, and the line sees you and steadies, and that is the speech.{/n}''',
        c("Continue", "break")),
    nar("break", '''{n}The line breaks, as she said it would. It breaks on the left, where the ground is soft, and the dead come through the gap without hurry, the way water comes through a sluice. You feel her hands change on your staff: one hand only now, the other on her sword. You feel her run.{/n}
{n}She plants you in the gap. She plants you so hard the staff jars in her grip and you feel it up to your finial, and then she stands in front of you with her back to your cloth, and the soldiers who ran look back and see where you are standing, and she is standing there.{/n}
{n}They come back. Not all of them. Enough.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}It ends by noon. The rain has stopped. She walks the field with you over her shoulder, and she does not look at the dead the way commanders look at the dead in paintings. She looks at their faces, one after another, as if she were being careful not to miss anyone.{/n}
{n}The boy is alive. He is sitting on a stone with his helmet off and his hands shaking and somebody else's blood down the front of him, and when he sees her he stands up, badly.{/n}
"You found it," {n}she says.{/n}
"You said to." {n}His voice cracks on it.{/n}
{n}She considers him, and considers you, and then she holds your staff out to him.{/n} "Carry it tomorrow. You know where it goes."''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake with the weight of the staff going out of your hands into someone else's.{/n}
{n}There are hymns to her that call her the Light of the Sword. You have heard them sung in Drezen by people who have never seen a sword used in earnest. They do not say that she looked at every face on the field, or that she gave her banner to a frightened boy to carry because he had come back to it, and that this was the whole of her theory of command.{/n}''',
        c("[Lie still, and remember the gap on the left.]"),
        c("[Get up, and walk the walls before the watch changes.]")),
], requires=(E + "herald_answered",), forbids=(), delay=48, chapters=(3,), kind="memory", drezen=True)


# --- Chapter 4, 1. In the Abyss, the herald tells the Acts. ------------------------------------------------------------------

at_herald(E + "herald.legend", "The Acts", 4, '"Tell me about your lady. Before she was a goddess."', [
    herald("start", '''{n}The Hand of the Inheritor has been watching the lights of Alushinyrra with an expression you have learned to read as disgust held under discipline. At your question it changes into something else.{/n} "Here, of all places?"
{n}He considers it.{/n} "Perhaps here most of all. This city is full of creatures who were made into what they are. She made herself."''',
        c("Continue", "acts")),
    herald("acts", '''"The Acts count eleven feats before the Starstone. The chroniclers quarrel over the order, and she does not settle it, because she will not discuss them. I will tell you what every novice is told." {n}He counts on gauntleted fingers.{/n}
"She broke her sword against the Whispering Tyrant's sorceries, and prayed over the pieces, and made it whole with her own hand, and that was the sixth. She talked a dead knight into his rest with no weapon drawn. She laid her cloak across a gorge, and her company crossed over on it, with the bridge burned and the dead behind them."''',
        c('"And then she burned the cloak behind her."', "burned"),
        c('"Did she ever say how she did it?"', "how"),
        c('"Thank you. That\'s all I wanted."', flags=(BRIDGE_TOLD,))),
    herald("burned", '''"That is not in the Acts." {n}He looks at you as if you had quoted to him a letter he had written and never sent.{/n} "Where did you hear it?"''',
        c("[Tell him about the dreams.]", "dreams"),
        c('"Somebody in a tavern."', "tavern")),
    herald("tavern", '''"Then it was a very well-read tavern." {n}He lets it go, though you can see what it costs him to let anything go in this city.{/n} "Keep your secrets, Champion. The Abyss will try to have them out of you soon enough."''',
        c("Continue", flags=(BRIDGE_TOLD,))),
    herald("dreams", '''{n}You tell him what the banner has shown you, all of it, in the order it came. He hears you out with his wings folded close against his back.{/n}
"I have prayed before that banner," he says at last, quietly. "It has never shown me anything." {n}There is no envy in it. There is something nearer to fear.{/n} "Forgive me. In this place I am afraid of everything that shows us what we want to see. And yet a relic of hers would not lie."
{n}He sets his hand on your shoulder, heavily, the way knights do it.{/n} "When we are home, and she can hear you, ask her yourself. Not through me."''',
        c("Continue", flags=(BRIDGE_TOLD, DREAMS_TOLD))),
    herald("how", '''"She has never said. The priests say faith, and they are right." {n}He lifts his chin, the way he does when he speaks of her in front of demons.{/n} "Her company was going to die on that bank, and she would not allow it. She asked nothing of heaven that night that she had not already given it. My lady did not wait to be a goddess to do what was right, Champion. That is why she became one."''',
        c("Continue", flags=(BRIDGE_TOLD,))),
], requires=(DREAM_BANNER,), forbids=(BRIDGE_TOLD,), lists=HERALD4_LIST, back=HERALD4_BACK)


# --- Chapter 4, 1b. The herald's doubt (canon: in the Abyss he begins to watch the Commander with trepidation). -------------

at_herald(E + "herald.doubt", "A fortress", 4, '"You\'ve been watching me differently since the city."', [
    herald("start", '''{n}The Hand of the Inheritor does not deny it. That is one of the things that makes him poor company in Alushinyrra, where everyone denies everything.{/n}
"I have. Forgive me." {n}He folds his hands on the pommel of his sword.{/n} "You asked me about my lady's Acts as a scholar asks. Then you told me her banner shows you her life, and I was glad, because a relic of hers would not show its secrets to someone unworthy. And then I watched you ask about her again, in this city, and I did not know what I was watching."''',
        c('"What did it look like?"', "looked")),
    herald("looked", '''"It looked like a general asking about a fortress." {n}He says it without heat.{/n} "Where the gate is weak. Which wall was built in a hurry. You asked me how she did the thing at the gorge the way a sapper asks how a wall was raised, and you already knew more of it than the Acts do. I have heard siege engineers ask gentler questions."
"So I will ask you plainly, Champion, because in this place I have nothing left but plainness. Do you love my lady, or do you mean to use her?"''',
        c('[Tell the truth] "Both. I don\'t know yet which is winning."', "both"),
        c('"I\'m not using her. I\'m trying to understand her."', "understand"),
        c('[Joke] "Can\'t it be both? She\'s very well fortified."', "joke")),
    herald("both", '''{n}The herald closes his eyes, briefly, like a man who has been struck and has decided not to acknowledge it.{/n} "That is the most honest answer I have had in this city, and I wish you had lied." {n}He opens them.{/n} "She will not be used, Champion. Better generals than you have tried, and gods besides. But she may be loved. I have seen it happen once or twice, to mortals who did not deserve it either."''',
        c("Continue", "pray")),
    herald("understand", '''"Understanding is a kind of siege, when it is done by someone like you." {n}He keeps his eyes on the city, and his voice is gentle.{/n} "I do not say that to wound you. I say it because it is what I would have said of myself, once, before she taught me better."''',
        c("Continue", "pray")),
    herald("joke", '''{n}He does not laugh. He does not reproach you either; he only waits, with a patience that is worse than either, until the joke has finished dying in the perfumed air.{/n} "When you joke, it is because the true answer embarrasses you. I told you that in Drezen. I do not think you have ever been embarrassed by a fortress."''',
        c("Continue", "pray")),
    herald("pray", '''"I will pray for you tonight, as I pray every night. I will not tell her what you said. You will tell her yourself, one day, or you will not." {n}He hesitates.{/n} "And Champion. If I do not come back from this city, and it may be that I do not, do not let anyone tell you she sent me after you. I came because I chose to. She will want you to know that, and I will not be there to say it."''',
        c('"You\'ll come back."'),
        c('"I\'ll tell her."'),
        c("[Clasp his arm, the way knights do it.]")),
], requires=(E + "dreams_told",), forbids=(), lists=HERALD4_LIST, back=HERALD4_BACK, delay=48)


# --- Chapter 4, 2. No banner in the Abyss. -----------------------------------------------------------------------------------

remote(E + "abyss.silence", "No banner here", [
    nar("start", '''{n}In the Abyss you sleep in snatches, in a borrowed room that smells of perfume laid over something going bad, and the dreams that come are the city's: sweet and heavy, and every one of them wants something from you.{/n}
{n}None of them is hers. The banner is a world away on its pole over Drezen, and whatever it remembers, it is remembering to empty stone. You had not known you were used to it until you woke three nights running with your hand closed on nothing, reaching for a staff that was not there.{/n}''',
        c("Continue", "cold")),
    nar("cold", '''{n}You make yourself think it through the way you would think through anybody's weakness, your own included. It is what you would do to an enemy commander who had started writing letters to a woman across the lines: find the letters, read them, and decide whether the man was compromised.{/n}
{n}A relic of a goddess has been showing you her life. Her herald says she watches you, and she has not answered a single question. Her banner has taken more interest in you than she has. And here you are in the Abyss, being lied to by experts, and the one thing in your life that has never lied to you is a flag's memory of a woman in the rain.{/n}
{n}The verdict, if you were writing it about someone else, would be short: compromised. You would recommend that the officer be watched, and kept away from the enemy's letters. You find you do not care to recommend it.{/n}''',
        c("[Count the days back to Drezen.]", flags=(ABYSS_SILENCE,)),
        c("[Put it out of your mind. There is a demon queen to deal with.]", flags=(ABYSS_SILENCE,))),
], requires=(DREAM_BANNER,), forbids=(ABYSS_SILENCE,), delay=48, chapters=(4,), kind="memory")


# --- Chapter 4, 3. A face in the Abyss: something in Alushinyrra puts on hers, and gives itself away by asking. ------------

remote(E + "abyss.face", "A borrowed face", [
    nar("start", '''{n}On the fifth night in Alushinyrra a dream comes that is almost right.{/n}
{n}Rain, and a field of black stubble, and a woman with a wet braid and a dented helm sitting with her back against a banner's staff. You know the scene; you have been the banner in it. Tonight you are not the banner. Tonight you are standing in the mud in front of her, and she looks up at you and smiles.{/n}''',
        c("Continue", "smile")),
    nar("smile", '''{n}It is the smile that is wrong. You have watched her face from the height of a banner a dozen times, in rain and snow and the dark over a gorge, and you have never once seen it do that: warm, slow and entirely for you.{/n}
"There you are," {n}says the woman with her face.{/n} "I have waited so long. Come and sit with me. Leave all that out there; the war can keep. Come here, and I will tell you everything you want to hear."''',
        c("[Test it with the word you sealed in the socket.]", "word", requires=(E + "tested",)),
        c('"She doesn\'t lie. So tell me you\'ve never lied."', "lie"),
        c("[Sit down beside her. It is a dream; what harm can it do?]", "sit")),
    nar("word", '''"What did I write in the foot of your banner?"
{n}The woman with her face does not hesitate, which is the second mistake.{/n} "Your name," {n}she says tenderly.{/n} "What else would you write there?"''',
        c("Continue", "seen")),
    nar("lie", '''"I have never lied to you," {n}says the woman with her face, at once and warmly, as if it cost nothing.{/n}
{n}The woman in the banner's memories never said anything about herself that was not dragged out of her, and never once said it warmly.{/n}''',
        c("Continue", "seen")),
    nar("sit", '''{n}You sit. The mud is warm, which mud in that field never was. She leans her head on your shoulder, which she never would, and her hand finds your knee, and it is only when she begins to tell you how the war will end, and how kindly, and how soon, that you understand what she is: the Abyss, trying on a shape it found in your sleep.{/n}''',
        c("Continue", "seen")),
    nar("seen", '''{n}The rain stops in mid-air. The field goes on for a while without anybody in it. Then the thing wearing her face laughs, a light, pleased, not unkind laugh, as a hostess laughs when a guest finds the joke under the tablecloth, and the dream folds up like a fan.{/n}
{n}You wake in a room in Alushinyrra with the taste of rain in your mouth, and a clear, cold certainty you did not have before: you would know the real one anywhere, because the real one would never ask you to come to her. She would tell you where she was going, and let you decide whether to follow.{/n}''',
        c("[Sleep with a knife under the pillow for the rest of the week.]", flags=(FALSE_FACE,)),
        c("[Go to the window and look at the city until morning.]", flags=(FALSE_FACE,))),
], requires=(DREAM_BANNER,), forbids=(FALSE_FACE,), delay=96, chapters=(4,), kind="event")


# --- Chapter 5, 1. The Summit: did you ask anyone's leave? (E14b beside Answer_0214; no clean cue on the list.) --------------

SCENES.append(scene(E + "summit.precedent", "Leave", "Iomedae", 5,
    '[Before you answer] "One question first, about when you were mortal."', [
    n("ask", "Iomedae", '''{n}The goddess inclines her head a fraction: the leave a judge gives a petitioner. Behind her the Lady in Shadow smiles at nothing, and waits to see what the question costs you.{/n}''',
      c('"When your people were at the edge of a gorge, with the bridge burned and the dead behind them, did you ask anyone\'s leave?"',
        "answer", requires=(BRIDGE_KNOWN,)),
      c('"They say you once made a bridge out of your cloak. Did you ask anyone\'s leave first?"', "answer",
        forbids=(BRIDGE_KNOWN,)),
      speaker_unit=IOMEDAE_UNIT),
    n("answer", "Iomedae", '''"No."
{n}She does not elaborate. Then, because you asked it of the girl at the gorge and not of the goddess in the square, she does.{/n} "There was no one to ask, and no time to ask them. I did what was in front of me, and answered for it afterwards. I have been answering for it since, to people who were not there, in books that get the width of the gorge wrong."''',
      c("Continue", "banner", requires=(DREAM_BANNER,)),
      c("Continue", "why", forbids=(DREAM_BANNER,)),
      speaker_unit=IOMEDAE_UNIT),
    n("banner", "Iomedae", '''{n}Her eyes stay on you a little longer than on anyone else in the square.{/n} "But you knew the answer. You have been sleeping under my banner, and it has been indiscreet."
{n}She does not turn her head toward the demon lord.{/n} "We will not discuss my banner in front of the Lady in Shadow, nor while the woman who built you to die is still loose with her plans for you. Make your decision, Commander. I will not make it for you."''',
      c("[Nod, and turn back to the matter at hand.]", flags=(SUMMIT_ASKED, STARTED)),
      speaker_unit=IOMEDAE_UNIT),
    n("why", "Iomedae", '''"Why do you ask it now?"''',
      c('"Because I\'m about to not ask yours."', "understand"),
      speaker_unit=IOMEDAE_UNIT),
    n("understand", "Iomedae", '''{n}Something moves at the corner of her mouth, and is put away.{/n} "Then we understand each other better than I would like. I have known a great many people who would not ask. Very few of them told me so to my face, in front of a demon lord. Make your decision, Commander."''',
      c("[Nod, and turn back to the matter at hand.]", flags=(SUMMIT_ASKED, STARTED)),
      speaker_unit=IOMEDAE_UNIT),
], requires=("trickster", "trickster.ever", KEY_DIES), forbids=(SUMMIT_ASKED, CLOSED), last=5, optional=True, Relationship=REL,
    Chapters=[5], AnswerLists=[SUMMIT_LIST], ReturnToList=True, ReturnText=SUMMIT_RETURN, EntryMythic="PlayerIsTrickster"))
tag(E + "summit.precedent")


# --- Chapter 5, 2. The bare platform: the wager is conceived (the Queen took the banner to Iz). ------------------------------

remote(E + "platform.bare", "The empty pole", [
    nar("start", '''{n}While you were in the Abyss, Drezen buried you, feasted you and went to war without you, and the Queen took the Sword of Valor with her to Iz. The platform on top of the citadel is bare. The pole stands in its iron socket with the halyard slapping against it in the wind, and nothing at the top.{/n}''',
        c("Continue", "wax", requires=(E + "test_answered",), forbids=(E + "slip_burned",)),
        c("Continue", "think", forbids=(E + "test_answered",)),
        c("Continue", "think", requires=(E + "slip_burned",))),
    nar("wax", '''{n}The wax is still on the crack at its foot, with your thumbprint in it and your word underneath.{/n}''',
        c("Continue", "think")),
    nar("think", '''{n}You stand where the banner stood and do what you do best, which is to look at a thing from the side nobody else is standing on.{/n}
{n}The goddess told the whole square the truth: the lock will destroy the key, and you are the key. The witch built you for it. The Lady in Shadow wanted you ignorant of it. And the goddess who told you would not lie to spare you, and would not interfere to save you.{/n}
{n}But once, when she was mortal and there was nobody to ask, she laid something of hers across a gap and told her people to walk.{/n}''',
        c("Continue", "wager")),
    nar("wager", '''{n}Her banner. It was hers before it was a relic, before she was a goddess; it was in her hand at the gorge. If the key goes into the lock carrying it, into the fire, meaning to die there, will she answer it? Nothing obliges her to. Nothing in any book says she can.{/n}
{n}It is not a plan. It is a wager on a woman you have met once and dreamed of a dozen times, and the odds are atrocious. You have made worse bets for less.{/n}
{n}And you can already see the cost. The Queen said it herself, in the war camp before Drezen: demons cannot step out of the air where the banner of the goddess flies. Carry it into the Wound and the city keeps nothing.{/n}
{n}You do the sums anyway, because that is what you are for. The lower town, packed to the walls with the people who came back after the siege. The cathedral whose window she stepped out of. The yard where they buried you. Every one of them sleeps easier under that cloth than they know. If the Wound closes, it will not matter. If it does not, the city will pay for your wager in the only coin demons take.{/n}''',
        c('[Say it aloud to the empty pole] "I\'m going to need your banner back."', flags=(PLAN,)),
        c("[Keep it to yourself. First get the banner back from Iz.]", flags=(PLAN,)),
        c('[Shrug] "Drezen managed seventy years without it. It can manage again."', flags=(PLAN,))),
], requires=(STARTED, KEY_LATCH, BRIDGE_KNOWN), forbids=(PLAN, IZ_DONE), delay=12, chapters=(5,), kind="memory", drezen=True)


# --- Chapter 5, 3. After the Summit: she stops observing (her own voice, in a dream, not through the banner). --------------

remote(E + "dream.summit", "The truth in the square", [
    nar("start", '''{n}It is not the banner dreaming. You know it at once, the way you know a face from a portrait of it.{/n}
{n}There is no rain, no gorge, nobody's hands. There is a white space like the inside of a cloud, and a voice in it, and the voice is speaking to you.{/n}''',
        c("Continue", "asked", requires=(SUMMIT_ASKED,)),
        c("Continue", "square", forbids=(SUMMIT_ASKED,))),
    io("asked", '''"You asked me in the square whether I asked anyone's leave." {n}Iomedae does not appear. The voice is enough; it fills the white the way light fills a room.{/n} "I answered you in front of the Lady in Shadow, briefly, because she did not deserve more. You did."''',
       c("Continue", "truth")),
    io("square", '''"You stood in the square before the cathedral and heard what I came to say." {n}Iomedae does not appear. The voice is enough; it fills the white the way light fills a room.{/n} "I said it in front of the Lady in Shadow, because she deserved to hear it said. You deserved to hear it differently."''',
       c("Continue", "truth")),
    io("truth", '''"I told you that the lock will destroy the key. I did not tell you gently. Gentleness would have been a lie of emphasis, and the Lady in Shadow had already left you ignorant; I would not leave you comforted instead." {n}A pause.{/n} "Until my herald's prayer I did not know who you were, and I observed you without intervening. I have stopped observing. I do not know yet what I have started."''',
       c("Continue", "face", requires=(FALSE_FACE,)),
       c("Continue", "ask", forbids=(FALSE_FACE,))),
    io("face", '''"Something in the Lady in Shadow's city put on my face for you once, in a dream, and asked you to come to it." {n}The voice cools by a degree.{/n} "You knew it for a forgery by what it asked. I observed that. I did not intervene. I would like you to know that I noticed."''',
       c("Continue", "ask")),
    io("ask", '''"So I will ask you now what I could not ask in front of her. You know what you are, and what closing the Wound will cost. What will you do?"''',
       c('"Close it."', "close"),
       c('"I don\'t know yet."', "unknown"),
       c('"Something you won\'t like."', "wont")),
    io("close", '''"Yes." {n}No approval in it, and no grief; only the sound of a thing being entered in a record.{/n} "I thought you would. You have the look of somebody who has already decided, and is only waiting to be told it is foolish."''',
       c('"Is it?"', "foolish")),
    io("foolish", '''"It is brave. The two are not always different." {n}The white begins to thin.{/n} "Sleep, Commander. I will come again. I have not decided whether that is wise, either."''',
       c("[Sleep.]", flags=(SPOKEN,))),
    io("unknown", '''"That is honest. Keep it; you will not be able to afford it for long." {n}The white begins to thin.{/n} "When you know, I will know. I have stopped observing, but I have not stopped seeing."''',
       c("[Sleep.]", flags=(SPOKEN,))),
    io("wont", '''"Very probably." {n}Something dry moves through the voice, and is put away.{/n} "I have watched you since Drezen. I would be astonished if it were anything else. Tell me when it has a shape, and I will tell you why it is wrong."''',
       c('"And if it isn\'t?"', "isnt")),
    io("isnt", '''"Then I will tell you that instead. I do not lie, Commander. It makes me poor company for a Trickster, and a very good judge of one."''',
       c("[Sleep.]", flags=(SPOKEN,))),
], requires=(STARTED, KEY_LATCH), forbids=(SPOKEN,), delay=12, chapters=(5,))


# --- Chapter 5, 4. Her herald: his fate, answered in her own voice. -----------------------------------------------------------

remote(E + "dream.herald", "Her herald", [
    nar("start", '''{n}It is not the banner dreaming. You know it at once, the way you know a face from a portrait of it.{/n}
{n}There is no rain, no gorge, nobody's hands. There is a white space like the inside of a cloud, and a voice in it, and the voice is speaking to you.{/n}''',
        c("Continue", "saved", requires=(HERALD_SAVED,)),
        c("Continue", "fell", requires=(HERALD_FELL,), forbids=(HERALD_SAVED,)),
        c("Continue", "fought", requires=(HERALD_FOUGHT,), forbids=(HERALD_SAVED, HERALD_FELL))),
    io("fought", '''"You fought him."
{n}Iomedae does not appear. The voice is enough; it fills the white the way light fills a room.{/n} "In Baphomet's prison, at the end, what was left of him wanted the fight more than it wanted saving, and he told you so, and you gave it to him. I heard him ask. I will not pretend I would have answered him the same way."
{n}A silence, long for a goddess.{/n} "I do not blame you. I blame myself. He followed you of his own will, and I let him go believing what he wished to believe about you, because it served, and I did not correct him."''',
       c("Continue", "stopped", forbids=(SPOKEN,)),
       c("Continue", "known", requires=(SPOKEN,))),
    io("saved", '''"You gave him back his heart."
{n}Iomedae does not appear. The voice is enough; it fills the white the way light fills a room.{/n} "He came before me with the wound still open and knelt, and told me how wrong he had been about you. I told him he had been wrong in the other direction first, and that the fault was mine, not his. I let him believe you were my chosen. I do not lie. I let him mistake me, which is not so much better as I used to think."
"You went into Baphomet's prison for a servant of mine whom I could not openly ask you to save. I did not ask. That is why it counts."''',
       c("Continue", "stopped", forbids=(SPOKEN,)),
       c("Continue", "known", requires=(SPOKEN,))),
    io("fell", '''"He is gone."
{n}Iomedae does not appear. The voice is enough; it fills the white the way light fills a room.{/n} "I told you in Drezen that I could not say whether he could be saved. You went where I could not go, and decided what I could not decide. I will not pretend I would have decided the same."
{n}A silence, long for a goddess.{/n} "I do not blame you. I blame myself. He followed you of his own will, and I let him go believing what he wished to believe about you, because it served, and I did not correct him."''',
       c("Continue", "stopped", forbids=(SPOKEN,)),
       c("Continue", "known", requires=(SPOKEN,))),
    io("known", '''"I came to tell you that myself, and not through a banner, because it is not a thing to be told through cloth." {n}The white does not waver.{/n} "He served me faithfully, and at the end badly, which was my fault. I will not have his ending carried to you by a flag. That is all. I have a war, and so, still, do you."''',
       c('"Thank you for telling me."', flags=(HERALD_DREAM,)),
       c("[Say nothing, and let her go.]", flags=(HERALD_DREAM,))),
    io("stopped", '''"Until my herald's prayer I did not know who you were, and I observed you without intervening. You know that; I said it in front of the Lady in Shadow." {n}The white grows closer, the way a room grows closer when someone sits down across from you.{/n} "I have stopped observing."''',
       c('"You\'re talking to me."', "precedent"),
       c('"Why now?"', "now"),
       c("[Say nothing, and listen.]", "listen")),
    io("precedent", '''"I am. Do not make me regret the precedent."''',
       c("Continue", flags=(HERALD_DREAM, SPOKEN))),
    io("now", '''"Because now I know what you are, and what was done to you, and what it will cost. I was not willing to speak to a stranger." {n}A pause.{/n} "You are not one. My banner saw to that, without asking me."''',
       c("Continue", flags=(HERALD_DREAM, SPOKEN))),
    io("listen", '''{n}She lets the silence go on, as if she were testing whether you would break it. You do not. When she speaks again there is something in the voice that might be approval, if goddesses approved of such small things.{/n} "Good. Most people talk to fill a silence. You wait to see what is in it."''',
       c("Continue", flags=(HERALD_DREAM, SPOKEN))),
], requires=(STARTED, KEY_LATCH), forbids=(HERALD_DREAM,), delay=24, chapters=(5,),
    RequiresAnyGroups=[[HERALD_SAVED, HERALD_FELL, HERALD_FOUGHT]])


# --- After her concession (Chapter 5-6): the dream she chooses. The heat, and where it will be. -----------------------------

remote(E + "dream.mortal", "What the banner did not see", [
    nar("start", '''{n}She brings you to a gorge.{/n}''',
        c("Continue", "seen", requires=(BRIDGE_SEEN,)),
        c("Continue", "unseen", forbids=(BRIDGE_SEEN,))),
    nar("seen", '''{n}You know it by the pins in the rock and the smell of burned rope. But the dead are not coming, and the torch on the far side has burned down to a coal, and she is sitting on the lip of it with her boots over the drop, the way she sat against the banner's staff in the rain.{/n}
{n}She is not the goddess of the Summit. She has let herself look as she looked then: the dented helm set down beside her, the braid, the gauntlet worn through at the knuckles. Older than the girl in the rain, though not by much.{/n}''',
        c("Continue", "sit")),
    nar("unseen", '''{n}You have never seen it, but you know it from the Acts: two iron pins in the rock on either side, and the smell of burned rope, and nothing in between. The dead are not coming. On the far side a torch has burned down to a coal. She is sitting on the lip of the gorge with her boots over the drop.{/n}
{n}She is not the goddess of the Summit. She has let herself look as she looked then, before the Starstone: a dented helm set down beside her, a braid, a gauntlet worn through at the knuckles. A knight on foot who has marched a long way.{/n}''',
        c("Continue", "sit")),
    io("sit", '''"You have seen what my banner remembers. It remembers what a banner sees: my hands, my shoulders, the back of my head." {n}She moves over on the rock.{/n} "Sit. I will show you the rest."''',
       c("[Sit beside her, with your boots over the drop.]", "hand"),
       c('"Is this you, or a memory of you?"', "which")),
    io("which", '''"It is me, choosing to look as I did. There is a difference, and it is the whole of the difference." {n}She moves over on the rock again, pointedly.{/n}''',
       c("[Sit beside her.]", "hand")),
    io("hand", '''{n}She takes off the gauntlet finger by finger and gives you her hand the way one hands over a weapon for inspection. The knuckles are scarred white. There is a notch out of the heel of the palm where a blade once went through the leather.{/n}
"The Whispering Tyrant's dead did that. I kept it when I kept everything else." {n}Her thumb moves once across the back of your hand. It is a small thing, and she watches it happen as though it were a large one.{/n} "I was mortal a long time before I was not. I remember hunger, and cold, and being so tired that I slept standing. I remember wanting. I did not expect to be reminded of it, at this remove, by a Trickster who argues like a canon lawyer."''',
       c("[Put your mouth to the notch in her palm.]", "palm"),
       c('"Then let me remind you properly."', "properly"),
       c('"What did you want, back then?"', "wanted")),
    io("palm", '''{n}Her breath goes out of her short, as if you had struck her somewhere she had forgotten was undefended. She does not take the hand away. She turns it, slowly, until your mouth is in the hollow of her palm and her fingers are along your cheek.{/n}''',
       c("Continue", "kiss")),
    io("properly", '''"Properly." {n}The word amuses her more than it ought to. It is the most human thing you have seen her do, and she knows it, and does not hide it.{/n} "You have a very high opinion of your abilities, Commander. I have watched you use them on demons, and on queens, and on a king who calls a tavern his throne room. I am not sure I wish to be added to the list."''',
       c('"It\'s been accurate so far."', "kiss")),
    io("wanted", '''"Sleep. Dry boots. That the people behind me would live until morning." {n}She looks at you sidelong.{/n} "And other things, which were no one's business, and are now apparently yours."''',
       c("[Take her face in your hands.]", "kiss")),
    nar("kiss", '''{n}Her fingers come up to your jaw. They are rough, and they read your face the way a scholar reads a carved inscription, letter by letter. When she draws you in, it is with the unhurried certainty of a woman who has never in her life begun a thing she did not mean to finish. Her mouth is warm and tastes of cold air and smoke, and it is the least holy kiss you can imagine, and she does not end it until she has had enough of it.{/n}
{n}Your hand finds the buckle of her breastplate at her side. She covers it with her own and does not move it away. She does not let the buckle open either.{/n}''',
        c("Continue", "not_here")),
    io("not_here", '''"Not in a dream." {n}Her forehead is against yours. Her voice is not quite steady, and she lets you hear that it is not.{/n} "When it happens I will not have it be something you were asleep for. Wake up, Commander. I have a war, and so do you."''',
       c("[Wake.]", flags=(MORTAL_SEEN,)),
       c('"Tell me where."', "where")),
    io("where", '''"Where it flew."''',
       c("[Wake, with the taste of smoke still in your mouth.]", flags=(MORTAL_SEEN,))),
], requires=(COMMITTED,), forbids=(MORTAL_SEEN,), delay=24, chapters=(5, 6))


# --- After a refusal (Chapter 5-6): the silence she keeps. The yes stays reachable at the Wound. ------------------------------

remote(E + "silence", "No answer", [
    nar("start", '''{n}She does not come.{/n}
{n}Not in the white, not in the banner, not in the small hours when you stand on the platform with your hand on the staff and say her name into the wind off the Wound like a sentry calling a password into the dark. The banner cracks and snaps, as banners do. It is only cloth. You had forgotten what that was like.{/n}''',
        c("Continue", "sums")),
    nar("sums", '''{n}You go over it the way you go over a battle you lost: coldly, from the beginning. You had the argument. You had it by the throat. And then you gave her the one answer she had told you, in so many words, that she would not take.{/n}
{n}She did not argue with it. She got up and left.{/n}''',
        c("Continue", "cost", requires=(E + "cost.boasted",)),
        c("Continue", "cost_other", forbids=(E + "cost.boasted",))),
    nar("cost", '''{n}She said she bowed to sacrifices and not to bargains, and that if you meant it you would show her at the Wound. It has taken you two days to understand that she was not being proud. She was telling you exactly what it would take, as she always does, and you were too pleased with yourself to hear it.{/n}''',
        c("[Resolve to tell her the truth at the Wound, if she asks.]"),
        c("[Resolve not to need her. You have been going into the Wound alone since Kenabres.]")),
    nar("cost_other", '''{n}She told you that if you had anything better to say, you should say it at the Wound. It has taken you two days to understand that she meant it literally: she will be there, and she will listen, and she will not come here to be told it first.{/n}''',
        c("[Resolve to tell her the truth at the Wound, if she asks.]"),
        c("[Resolve not to need her. You have been going into the Wound alone since Kenabres.]")),
], requires=(DECLINED,), forbids=(COMMITTED,), delay=24, chapters=(5,), kind="memory")


# --- After her concession (Chapter 5-6): questions that are not about the war. ------------------------------------------------

remote(E + "dream.questions", "Not in any report", [
    nar("start", '''{n}The white again, and her voice in it. Tonight she has brought into the dream something she has never brought before: a question that is not about the war.{/n}''',
        c("Continue", "ask")),
    io("ask", '''"I have watched you since Drezen and argued with you on a roof, and I do not know where you were born." {n}The voice is almost diffident, which is so unlike it that you nearly laugh.{/n} "Tell me something that is in no report."''',
       c('"I was nobody. Then I was the Commander. There wasn\'t much in between."', "nobody"),
       c('"I stole things, before. Never anything that couldn\'t be spared."', "stole"),
       c('"You first."', "first")),
    io("nobody", '''"Nobody is a great deal to have been. I began there too. There are books now that give me a noble house and a vision in the cradle. I had a borrowed sword, and a sergeant who told me to stop dropping it."''',
       c("Continue", "hers")),
    io("stole", '''"Everything can be spared, by someone who is not the one losing it." {n}There is no reproach in it tonight, only interest.{/n} "Tell me the best thing you ever stole."''',
       c('"A horse, from a man who beat it."', "horse"),
       c('"A kiss. Not from you. Yet."', "kiss")),
    io("horse", '''"Good." {n}Just that, and then, after a moment, as if it had been pried out of her:{/n} "That was a good thing to steal."''',
       c("Continue", "hers")),
    io("kiss", '''"Yet." {n}The white seems to warm by a degree, like a room in which somebody has decided not to be offended.{/n} "You are very sure of your abilities, Commander. I have said so before. I will probably say it again."''',
       c("Continue", "hers")),
    io("first", '''"I asked first." {n}A pause.{/n} "Very well. You asked a fair question. I will answer it."''',
       c("Continue", "hers")),
    io("hers", '''"Then here is one of mine, which is in no report either." {n}The white warms, very slightly.{/n}
"Before a battle I ate bread and a raw onion, like a carter, because an old sergeant told me that a knight who could keep food down before a fight could do anything. I have not eaten an onion since the Starstone." {n}The voice considers this with apparent surprise.{/n} "I miss them. That is the kind of thing I do not say to my herald."''',
       c('"What else do you miss?"', "miss"),
       c('"I\'ll bring you one. Afterwards."', "onion")),
    io("miss", '''"Being tired in the ordinary way. Being wrong about small things, where it did not matter. Rain." {n}A pause.{/n} "Being touched without its meaning anything to anyone but the two people concerned. Gods do not get that. Everything we touch becomes a relic, or a scandal."''',
       c('"Then I\'ll try to be a scandal."', "fear")),
    io("onion", '''"Afterwards." {n}She repeats the word as if weighing it on a scale.{/n} "You say it as though you expect there to be one. I have not decided that, and neither, I think, have you."''',
       c('"No. But I\'m planning for it."', "fear")),
    io("fear", '''"Then answer me one more, and I will let you sleep." {n}The white draws in close.{/n} "What are you afraid of? Not the Wound; everyone is afraid of the Wound. You."''',
       c('"That you won\'t come, and I\'ll have been right to go anyway."', "right"),
       c('"That you will, and I won\'t know what to do with it."', "will"),
       c('"Being forgotten wouldn\'t be so bad. Being remembered wrong would."', "wrong")),
    io("right", '''"That is a soldier's fear, and an honest one." {n}The voice is very quiet.{/n} "I have had it. It does not go away. It only stops mattering, at the edge."''',
       c("[Sleep.]")),
    io("will", '''"Then we will have the same problem, and we will argue about it." {n}Something that is nearly a laugh.{/n} "I find I am looking forward to that more than I should."''',
       c("[Sleep.]")),
    io("wrong", '''"You will be remembered wrong. Everyone is. I am remembered as a woman who never doubted and never ate onions." {n}The white begins to thin.{/n} "The ones who matter will remember you right. I intend to be one of them."''',
       c("[Sleep.]")),
], requires=(COMMITTED,), forbids=(), delay=48, chapters=(5,))


# --- Chapter 6. The night before Threshold: she has not decided; neither has the Commander. ---------------------------------

remote(E + "dream.eve", "The night before", [
    nar("open", '''{n}The last camp before Threshold.{/n}''',
        c("Continue", "o_start", requires=(COMMITTED, E + "cost.buried_to_the_world")),
        c("Continue", "start", forbids=(COMMITTED,)),
        c("Continue", "start", requires=(COMMITTED,), forbids=(E + "cost.buried_to_the_world",))),
    nar("o_start", '''{n}You conceded, on the platform, that the world would keep its grave. Tonight, in the last camp before Threshold, you find out what that costs in ink.{/n}
{n}A Commander going into the Wound leaves orders: who commands after, what is to be done with the army, who is to be told. Every Commander in the history of the crusades who has written such orders has hoped, while writing them, that they would be burned unread. You are writing them knowing that they will be read, and obeyed, and that you will have to stand somewhere at the back of a crowd and watch them obeyed, and say nothing.{/n}''',
        c("Continue", "o_write")),
    nar("o_write", '''{n}You write the ordinary things first. The dispositions of the army. The debts the crusade owes to merchants who were paid in promises. The names of soldiers who deserve better than they have had. None of it is hard. You have always been good at telling other people what to do.{/n}
{n}Then you come to the part where a Commander writes something for the people who will mourn, and your pen stops.{/n}''',
        c("[Write something true that does not give you away.]", "o_true"),
        c("[Write something grand, for the chaplains to read out.]", "o_grand"),
        c("[Write nothing. Leave the space blank.]", "o_blank")),
    nar("o_true", '''{n}It takes you most of the night. In the end it is three lines: that you did this on purpose, that nobody made you, and that the people you are leaving are to stop saluting the empty chair and get on with their lives, which you paid rather a lot for. It does not say goodbye. You cannot quite bring yourself to lie in a letter she might read over someone's shoulder.{/n}''',
        c("Continue", "o_seal")),
    nar("o_grand", '''{n}It comes easily, which should worry you. Fire and sacrifice and the dawn of a new age; the Wound closed by the one it was opened to destroy. The chaplains will weep. It is magnificent, and it is a lie by emphasis, and you think of a goddess who will not lie even by emphasis, and you tear it up, and write three lines instead, and they are true.{/n}''',
        c("Continue", "o_seal")),
    nar("o_blank", '''{n}You leave it blank. Let them fill it with whatever they need; people always do. The dead are not consulted about their eulogies, and you are, in every way that the world will ever be told about, going to be dead.{/n}''',
        c("Continue", "o_seal")),
    nar("o_seal", '''{n}You seal it and give it to the quartermaster, to be opened if the Commander does not come back from the Wound. He takes it the way a man takes something hot. You do not tell him that he will open it either way.{/n}''',
        c("[Go to bed. The banner is beside the cot, rolled on its staff.]", "start")),
    nar("start", '''{n}You took the banner down from the citadel yourself on the morning the crusade marched, and Drezen watched you do it and did not ask why. Now the whole crusade is awake pretending to sleep. You lie down with the banner rolled on its staff beside you, close enough to touch, and shut your eyes, and she is there before the dark has finished arriving.{/n}''',
        c("Continue", "committed", requires=(COMMITTED,)),
        c("Continue", "declined", requires=(DECLINED,), forbids=(COMMITTED,)),
        c("Continue", "unargued", forbids=(COMMITTED, DECLINED, E + "argument_only")),
        c("Continue", "argued", requires=(E + "argument_only",), forbids=(COMMITTED, DECLINED))),
    io("argued", '''"Tomorrow." {n}The white is very still tonight.{/n}
"You took the argument and left the rest on the roof, and I have let it lie there. Hear me exactly: the argument stands. I conceded that I may answer my banner. I did not promise that I will. I will decide at the Wound, as you will."''',
       c("Continue", "others")),
    io("committed", '''"Tomorrow." {n}The white is smaller tonight, as if she were keeping it close.{/n}
"I conceded the argument, and it stands. But hear me exactly, because tomorrow there will be no time for it. I conceded that I may answer my banner. I did not promise that I will. I will decide at the Wound, with the fire in front of me, as you will."''',
       c("Continue", "others")),
    io("declined", '''"You know why I left your roof." {n}There is no anger in it. It is worse than anger: it is a fact, set down where you will have to step over it.{/n}
"Tomorrow you will stand at the Wound with my banner, and I will be there. Show me. That is all I have left to say to you, and it is not little."''',
       c("Continue", "others")),
    io("unargued", '''"You never raised it where it flew. The war took the nights, and I do not reproach you for that; it is a war." {n}A pause.{/n} "Tomorrow, at the Wound, raise it, and argue. Briefly. The Worldwound does not wait on disputations."''',
       c("Continue", "others")),
    io("others", '''"The Architect built you to die in her lock. She is not wrong about the lock. She is wrong about what she is owed for it."
"And the Lady in Shadow wants you in the Wound as well, for reasons she will call kind. Do not go in for hers. Go in for yours, or do not go."''',
       c('"And if you don\'t answer?"', "if_not"),
       c('"I\'ll see you there."', "there"),
       c('"You could just tell me now."', "now"),
       c('"What did you do, the night before the Starstone?"', "starstone")),
    io("starstone", '''"I do not speak of the Test." {n}At once, and not unkindly: a door closed by someone who has closed it many times.{/n} "Not to my herald, not to my priests, and not to you. What happens there is between the one who goes in and the Stone."
{n}A pause.{/n} "I will tell you what I did the night before the gorge, which is the nearest thing I have. I ate an onion. I checked the straps on forty sets of armour that were not mine. I slept for an hour, sitting up. And I did not decide anything, because I had already decided, and there was no use in doing it twice."''',
       c('"Then I\'ll do the same."', "same")),
    io("same", '''"Check your straps," {n}she says.{/n} "And sleep. I will be there in the morning. That much I have decided."''',
       c("[Sleep.]", flags=(EVE_SEEN,))),
    io("if_not", '''"Then you will have died closing the Worldwound, and I will bow my head to it, and mean it." {n}The white does not waver.{/n} "I will not tell you tonight that I would grieve less than I would."''',
       c("[Sleep.]", flags=(EVE_SEEN,))),
    io("there", '''"You will. That much I can promise, and I do."''',
       c("[Sleep.]", flags=(EVE_SEEN,))),
    io("now", '''"I could. I will not. If I decided tonight, I would be deciding about a Commander who has not yet walked up to the edge." {n}Dry as dust:{/n} "I have met a great many people who were brave the night before."''',
       c("[Sleep.]", flags=(EVE_SEEN,))),
], requires=(STARTED, KEY_LATCH), forbids=(EVE_SEEN,), delay=0, chapters=(6,),
    RequiresAnyGroups=[[BANNER_HELD, ORDER_BANNER]])
