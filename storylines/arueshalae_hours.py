"""Arueshalae, further hours: the treatment's harder sessions, the chaplain's wedding, the hundredth day, and the fallen
succubus's side of the queen's bill (arueshalae.md F18).

Canon: in the Abyss the hunger is worse (her own words at the Ten Thousand Delights, Brothel_Inside 399c6614, and "Evil
calls me back. Every day", hub 34c8f44a); Nocticula "enjoys killing, but her favorite tools are seduction and deception"
and "the worst mistake anyone can make is to underestimate her" (hub 61862e9d, 39f32845); evil Arueshalae's "boys", her
balor-led gang, die with her at the lair (MeetEvilArusha/Cue_0006 f95980a8, Cue_0013 speaker CR28M_BalorMythicFighter).
Authored and labelled: the Tanner's Row bakery, the wedding, the queen's token, the balor's name (Rakkoth; the native unit
is the unnamed CR28M_BalorMythicFighter).
"""
from story_format import c, n, scene
from storylines.arueshalae_trickster import (AFTERTASTE, ALLY, CHAPLAIN, CLOSED, COMMITTED, DEAD, DEBT, DREZEN, EVIL_DEAD,
                                             EVIL_UNIT, FAVOUR, HUB, P, RECRUITED, RETURNED, REUNITED, TAVERN_FAILED, DREZEN_PLACES,
                                             TAVERN_PRESENCE, UNANSWERED, UNIT, YARD_PRESENCE)
from storylines.arueshalae_chapel import CENSER, COUNTING
from storylines.arueshalae_treatment import CURE, CURED, ELYSIUM, INTAKE, MORNING, RELAPSE, RX_WANT, T, TOUCHED

SCENES = []
BAKERY = T + "the_bakery"
ABYSS_TOUCH = T + "abyss_dose"
BAD_DAY = T + "bad_day"
SNAPPED_BACK = T + "snapped_back"
QUARREL = T + "first_quarrel"
WEDDING = P + "chaplain.wedding"
HUNDRED = P + "returned.hundred"
TOKEN = P + "evil.token"
BOYS = P + "evil.the_boys"
GUARD = (CLOSED, DEAD, EVIL_DEAD, RECRUITED)
BACK = dict(ForbidOverrides={DEAD: RETURNED})


def a(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Arueshalae", **kw)


def hub(id, title, chapter, entry, nodes, requires, forbids=(), delay=0, last=5, chapters=None, **extra):
    SCENES.append(scene(id, title, "Arueshalae", chapter, entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(*GUARD, id, *forbids), delay=delay, last=last, optional=True,
                        Relationship="arueshalae", AnswerLists=[HUB], ContactUnit=UNIT,
                        Chapters=list(chapters or range(chapter, last + 1)), **{**BACK, **extra}))


def tavern(id, title, entry, nodes, requires, forbids=(), delay=0):
    for hub_key, suffix, extra, unit in DREZEN_PLACES:
        SCENES.append(scene(id + suffix, title, "Arueshalae", 5, entry, [dict(nd) for nd in nodes],
                            requires=("trickster.ever", RETURNED, EVIL_DEAD, REUNITED, *requires, *extra),
                            forbids=(CLOSED, ALLY, id, id + "_yard", *forbids), delay=delay, last=5, optional=True,
                            Relationship="arueshalae", Areas=[DREZEN], Chapters=[5], ContactUnit=unit,
                            InteractionHub=hub_key))


# --- The bakery on Tanner's Row (Drezen: Chapters 3 and 5) ---------------------------------------------------

hub(BAKERY, "Tanner's Row, at dawn", 3, '"You smell of flour."', [
    a("start", '''"I've been at the bakery on Tanner's Row. Since before dawn." {n}She has flour on her cheek and in her hair and on one wing, and she has no idea.{/n}
"I told you it was on my list. The smell. Not the bread, the smell. So I went and stood outside in the dark, where the ovens vent into the alley, morning after morning. And this morning the baker's daughter came out with the ash bucket and saw me standing there, and asked if I was hungry."''',
        c("Continue", "hungry")),
    a("hungry", '''"Imagine it. A girl of twelve, with an ash bucket, asking a succubus if she's hungry." {n}She laughs, shakily.{/n} "I said yes, because it was true, and because I have stopped lying about that one thing. And she said, 'Well, come in, then,' and she took me into the bakery and gave me a job."
"I knead. I'm very good at it. It's all in the wrists, and my wrists are very strong, and I never get tired. The baker says I'm the best kneader he's had in twenty years. He pays me in rolls. I give them to the refugees."''',
        c("Continue", "girl")),
    a("girl", '''{n}Her face changes.{/n} "The daughter. She stands next to me at the trough. She talks the whole time, about her friends and the siege and a boy who threw a stone at her. She leans on me when she's tired. She put her flour-covered hand on my arm yesterday to show me how to fold the dough."
"And I felt it. Just a little. The edge of her. And I stepped away so fast I knocked the trough over, and she laughed and called me clumsy, and I let her." {n}Her hands are fists.{/n} "I can't go back, can I? I can't stand next to a child for hours knowing that. What if one day I don't step away?"''',
        c('"You stepped away. That\'s the whole treatment. Go back."', "back", flags=(BAKERY,)),
        c('"Go back, but wear gloves, and knead at the other end of the trough."', "gloves", flags=(BAKERY,)),
        c('"You\'re right. Leave it. Some things you can only want from a distance."', "leave", flags=(BAKERY,))),
    a("back", '''"That's the whole treatment." {n}She repeats it, the way she repeats everything you say that she means to keep.{/n} {n}She wipes her face, spreading the flour further.{/n} "I'll go back. With gloves, this time. I promised her I'd help with the trough. Tomorrow before dawn. If I knock the trough over every morning, the baker's going to stop paying me in rolls."''', c()),
    a("gloves", '''"Gloves and the other end of the trough." {n}She nods, too quickly, relieved.{/n} "That's sensible. That's what a real doctor would say. You keep surprising me by being one." {n}She hesitates.{/n} "She'll ask why. She asks why about everything."
"Tell her you're allergic to children," you suggest. She laughs so hard she has to sit down.''', c()),
    a("leave", '''{n}She is quiet for a long time.{/n} "Some things you can only want from a distance." {n}She nods slowly.{/n} "Yes. I know that one. I've known it longer than anything." {n}She brushes flour from her sleeve, and looks at it, and doesn't brush any more.{/n} "I'll still go and stand in the alley. For the smell. Nobody can take a smell."''', c()),
], (INTAKE, RX_WANT), delay=24, chapters=(3, 5))


# --- The dose in the Abyss (Chapter 4) ---------------------------------------------------------------------

hub(ABYSS_TOUCH, "The dose, adjusted", 5, '"You\'re thinking about the Abyss again."', [
    a("start", '''{n}Back in Drezen, she brings it up without warning, and the night comes back whole: the camp at the edge of the Abyss, the pickets, the fire she would not sit near.{/n}
"Everything is worse here." {n}She is sitting as far from the camp's fire as she can and still be inside the pickets.{/n} "The air here tastes of it. Every scream from the dark tastes of it. It's like being a drunk in a city made of wine." {n}She looks at your hand, and away, and back.{/n}
"I haven't asked. I've been very good. I haven't asked for your hand once since we crossed. I didn't think I could stop, here, if I started."''',
        c('[Hold out your hand] "Doctor\'s orders. The dose is adjusted for altitude."', "take"),
        c('"Then don\'t ask. I\'ll sit here instead."', "sit", flags=(ABYSS_TOUCH,))),
    nar("take", '''{n}She stares at the hand. Then she takes it with both of hers, too hard, and the cold comes through you like a river breaking a dam.{/n}''',
        c("Continue", "cure", requires=(CURED,)),
        c("Continue", "paid", forbids=(CURED,))),
    nar("cure", '''{n}It is not the gentle tide of Drezen. It is a flood. The star-candle you lit at dusk takes the first of it and goes out like a pinched wick, and the rest comes on with nothing to stop it, and for two long breaths you pay it straight, and she feels you paying and does not let go.{/n}
{n}Then she does. She drops your hand as if it were a coal and sits there panting.{/n}''',
        c("Continue", "after")),
    nar("paid", '''{n}It is not the gentle cold of Drezen. It is a flood, and you have nothing to stop it with but your own stubbornness, and your vision goes grey at the edges almost at once. You hold on for one breath. For two.{/n}
{n}She lets go before the third, and catches you as you fold, and holds you by the shoulders with her face white as salt.{/n}''',
        c("Continue", "after")),
    a("after", '''"Too much. That was too much. I felt it, I felt how much I could take here, and I wanted all of it." {n}She is shaking.{/n}
"You were right to adjust the dose, doctor. Adjust it down. Down to nothing, until we're home." {n}She sits back.{/n} "Or I'll take you. Here, in the dark, with the Abyss singing in my ears. I'll take you and I'll be glad, and then I'll never be anything else again."''',
        c('"Down to nothing, until we\'re home."', "home", flags=(ABYSS_TOUCH,))),
    a("sit", '''{n}You sit down next to her in the dark, at the edge of the pickets, not touching. After a while she starts to talk, very quietly, about the bakery and the cat and the net-menders' song, as if reciting a list of things to hold on to. You let her. You are what the Abyss cannot give her: someone sitting there who wants nothing.{/n}''', c()),
    a("home", '''"Until we're home." {n}She smiles, and it is the smile of someone very tired.{/n} "Drezen isn't home. Nothing's home. I've never had one." {n}She shrugs.{/n} "But I know which way it is from here. That's new too."''', c()),
], (TOUCHED,), delay=24, chapters=(5,))


# --- A bad day: the demon's temper ---------------------------------------------------------------------------

hub(BAD_DAY, "Symptoms", 3, '"Arueshalae?"', [
    a("start", '''"What?" {n}It comes out as a snarl, and there is something in it that you have not heard from her before: a harmonic under the voice, like a second voice, cold and very old.{/n}
{n}She has her back to the tent pole. Her wings are half open and her nails are out, long and black, and she is breathing as if she has run a long way. When she sees it is you, she does not put any of it away.{/n}''',
        c("Continue", "tirade")),
    a("tirade", '''"Do you know what I did today? Nothing. I watched a squad of your soldiers flog a deserter, and I stood there, and I enjoyed it. I enjoyed every stroke. And then I went and knelt in the chapel and asked the goddess to take the enjoyment away, and she didn't, because she never does, because it's mine."
"I'm tired of your treatment. I'm tired of your jokes. I'm tired of watching people eat soup and pretending it makes me better. It doesn't. I'm a demon who's pretending, and you're a Trickster who's enjoying the pretence, and one day one of us is going to stop."''',
        c('[Snap back] "Then stop. Go on. Nobody\'s holding you here. Not me, not the goddess."', "snap", flags=(BAD_DAY, SNAPPED_BACK)),
        c('[Sit down on the floor, out of reach, and wait.]', "wait", flags=(BAD_DAY,))),
    a("snap", '''{n}For a moment you think she will take you at your word. Her wings open fully, filling the tent. Then she laughs, a horrible, broken laugh, and folds them again.{/n}
"You'd let me. You'd actually let me go." {n}She slides down the pole until she is sitting.{/n} "That's what I can't bear about you. Everyone else tries to keep me or kill me. You just stand there and let me choose. Every time." {n}She wipes her eyes with the back of a clawed hand.{/n} "I'm not going. I'm just... I'm having a bad day. Can demons have bad days? I'm having one."''', c()),
    nar("wait", '''{n}You sit down on the floor of the tent, just out of her reach, and say nothing at all. It takes a long time. The nails go first; then, slowly, the wings; last of all, the second voice under her breath.{/n}
{n}When she speaks again it is only her own voice, small and hoarse.{/n} "I watched them flog him. The deserter. Twelve strokes, and I counted every one, and I was sorry when they stopped." {n}She sits down opposite you, knees to her chest.{/n} "Desna sent me back to learn what dreams were, and I spent this morning wanting a man's back opened. Put it in the notes. 'Patient had a bad day. Doctor sat on the floor.' Don't you dare write down that it helped."''', c()),
], (RELAPSE,), delay=48, chapters=(3, 4, 5))


# --- After the yes: a first quarrel ---------------------------------------------------------------------------

hub(QUARREL, "Second opinion", 5, '"You\'re angry with me."', [
    a("start", '''"Yes. I am. You walked into that arrow as if it were weather, and I had to stand there and smell you bleed." {n}She has her arms folded and her chin up.{/n}
"You went into the siege lines alone yesterday. Without telling anyone. Without telling me. You came back with an arrow in your shoulder and a joke about it." {n}Her voice shakes.{/n} "I have spent this whole war learning how not to take a life from anybody. And you walk out and offer yours to the first demon with a bow, as if it were a cheap thing."''',
        c("Continue", "fear")),
    a("fear", '''"Do you know what I thought, when they brought you in? Not 'will they live'. I thought: if they die, I'll have to learn how to be without them, and I'm so bad at learning, I've been learning for years, I haven't got the time." {n}She is crying now, and furious about it.{/n}
"So yes. I'm angry. I'm going to be angry for at least a day. And you're going to let me, and you're not going to make a joke about it, and tomorrow you're going to tell me before you do something stupid."''',
        c('"I\'ll tell you. Before. Every time."', "promise", flags=(QUARREL,)),
        c('"I can\'t promise that. It\'s a war, and I\'m the Commander."', "cant", flags=(QUARREL,))),
    a("promise", '''"Every time." {n}She glares at you through her tears.{/n} "You say that about everything. Every time. It's the most frightening thing you say." {n}Then she sits down next to you, hard, and leans her head on your good shoulder.{/n} "I'm still angry. This is me being angry. Don't move."''', c()),
    a("cant", '''"No. I know you can't." {n}She wipes her face.{/n} "That's what makes it a real quarrel, I suppose. In the Upper City we never quarrelled. We just waited until someone was asleep." {n}She sits down, not next to you, but not far.{/n} "I'm going to be angry for two days, then. And afterwards I'll still be here. That's new too."''', c()),
], (MORNING,), delay=48, chapters=(5,))


# --- The chaplain: a wedding ----------------------------------------------------------------------------

hub(WEDDING, "Under the stars", 3, '"Somebody asked me to marry them."', [
    a("start", '''{n}She is pink to the tips of her ears.{/n} "Not like that. To perform it. A corporal from the second company and a laundress from the camp. They want a Desnan wedding, under the stars, and I'm the only Desnan in the crusade who'll do it without asking for a donation first."
"I tried to say no. I said I didn't know the words. So the laundress brought me a book with the words in. I said I'm not a priest. The corporal said I'm the chaplain, the Commander said so, out loud, in the shrine, everybody heard." {n}She glares at you.{/n} "This is your fault."''',
        c("Continue", "fear")),
    a("fear", '''"I'm afraid. I know what a bargain sounds like in the Upper City, with music over it. I don't know what a real wedding looks like. What if I get it wrong? What if I stand there with my hand over theirs and the old hunger..." {n}She doesn't finish.{/n}
"The words say I have to bind their hands with a ribbon. Touch both of them. At once. In front of everyone."''',
        c('"Use a long ribbon."', "ribbon", flags=(WEDDING,)),
        c('"I\'ll stand beside you. If you falter, look at me, and I\'ll make a face."', "face", flags=(WEDDING,))),
    a("ribbon", '''{n}She stares at you. Then she laughs, the startled laugh, the one she can't help.{/n} "A long ribbon. Oh, gods. A very long ribbon. I can tie it from a step away." {n}She is already counting on her fingers, measuring.{/n} "Two ells? Three? The laundress will have some. The laundress has everything." {n}She turns at the tent flap.{/n} "Come anyway. Please. I want someone there who knows what I am, and doesn't mind."''', c()),
    a("face", '''"You'll make a face." {n}She looks at you with enormous gravity.{/n} "The Commander of the crusade will stand at a laundress's wedding and pull faces at the chaplain." {n}Her mouth twitches.{/n} "Yes. Do that. If I look at you and you're pulling a face, I'll be too busy not laughing to be hungry. That's a real treatment. I think it's the best one you've prescribed."''', c()),
], (CHAPLAIN, CENSER), delay=24, chapters=(3, 5))


# --- The returned: a hundred days --------------------------------------------------------------------------

hub(HUNDRED, "One hundred", 5, '"You look like you\'ve been counting."', [
    a("start", '''"A hundred." {n}She holds up both hands, all ten fingers, and then does it nine more times in the air, very fast, grinning.{/n} "A hundred times since the chapel I've wanted to be fed, and counted it, and not asked you. A hundred. The forty-first was very close." {n}She sobers.{/n} "I'm sorry. That's a terrible thing to tell you. It's true, though. I've promised to tell you true things."''',
        c("Continue", "reason")),
    a("reason", '''"You said to ask again at a hundred. Whether there's a reason in the world that isn't me being hungry." {n}She takes a breath.{/n}
"There is. There are several. The kitchen boy who saves me the burnt crusts because he thinks I like them. The refugees who leave me a seat at the soup kettle now. The old woman in the chapel who calls me 'dear' and doesn't know why she's afraid of me." {n}She looks at you.{/n} "And you. Mostly you. Not the taste of you. The fact of you, walking into a room and making a bad joke, so I know where you are."''',
        c('"A hundred and one, tomorrow."', "tomorrow", flags=(HUNDRED,)),
        c('"Then you can ask me whatever you like. That was the deal."', "deal", flags=(HUNDRED,))),
    a("tomorrow", '''"A hundred and one." {n}She laughs.{/n} "Yes. That's the right answer. Not 'well done'. Just the next number." {n}She tucks her hands behind her back, not out of fear, now; out of habit, and pleasure in the habit.{/n} "I'll ask you my question soon. On the chapel steps. Wear something nice. I'm going to."''', c()),
    a("deal", '''"I'll ask you on the chapel steps." {n}She says it very seriously, as if booking an appointment.{/n} "Soon. When I've decided exactly what to ask. I've waited a hundred days; I can wait for the right words." {n}A pause.{/n} "They're going to be the most frightening words I've ever said. Make sure you're there."''', c()),
], (COUNTING, AFTERTASTE), delay=72, chapters=(5,))


# --- The fallen: the queen's token and the boys -------------------------------------------------------------

tavern(TOKEN, "The queen's token", '"What\'s that round your neck?"', [
    a("start", '''{n}She lifts it out on its string: a small black pearl, the size of a fingernail, cold even on a warm night.{/n}
"This? My receipt. It was round my neck when I sat up, and nobody in that house would say whose hand had tied it. It means I'm hers, on loan. When she wants me, it'll get warm." {n}She rolls it between finger and thumb.{/n}''',
        c("Continue", "debt", requires=(DEBT,)),
        c("Continue", "favour", forbids=(DEBT,))),
    a("debt", '''"One summons. Once. That's what you bought me with, darling. My one summons." {n}She laughs.{/n} "Do you know what she's likely to want? Nothing much. A dance. A conversation. A night. She'll pick the hour that hurts you most, not me. That's the art of it."''',
        c("Continue", "hiding", requires=(UNANSWERED,)),
        c("Continue", "end", forbids=(UNANSWERED,))),
    a("favour", '''"Your favour. Not mine. You put it in your own name, you gallant idiot." {n}She taps the pearl.{/n} "I think it was given me so I'd feel it when she comes to collect from you. I think she wants me to be there. She wants me to watch you pay." {n}Her smile is all teeth.{/n} "I will. I wouldn't miss it."''',
        c("Continue", "hiding", requires=(UNANSWERED,)),
        c("Continue", "end", forbids=(UNANSWERED,))),
    a("hiding", '''"It's been cold since she went into hiding. Cold as a stone at the bottom of a well." {n}She tucks it away.{/n} "It'll warm up one day. Queens always come back. Remember: the worst mistake anyone can make is to underestimate her. I told you that once, when I was the other one. It's still true."''',
        c("Continue", "end")),
    a("end", '''{n}She lets the pearl drop back inside her dress, next to her skin.{/n} "Don't look so grim. It's only jewellery. Everyone in Alushinyrra wears somebody's." {n}She finishes her drink.{/n} "And now you know something about me that nobody else in your city does. You should feel honoured. I feel sick."''',
        c("[Say nothing.]", flags=(TOKEN,))),
], (), delay=24)
for s in SCENES[-2:]:
    s["RequiresAnyGroups"] = [[DEBT, FAVOUR]]

tavern(BOYS, "The boys", '"Your gang. At the lair."', [
    a("start", '''"Gone. You ruined my gang." {n}She says it lightly, and her fingers stop moving on the cup.{/n}
"Do you know what they were? Some of the worst things in the Worldwound, and they followed me because I was cleverer than they were, and I let them because they were useful, and they worshipped me because demons will worship anything that hurts them well." {n}She drinks.{/n} "I'm not sad. Demons don't get sad. I'm annoyed. I had almost taught them to wipe their feet."''',
        c("Continue", "choice")),
    a("choice", '''{n}She looks at you across the table, and for once there is no smile at all.{/n} "The balor, Rakkoth, the big one. He used to sit outside my door at night so nobody would disturb my sleep. I don't sleep. He knew that. He sat there anyway." {n}She shrugs, one shoulder.{/n} "Don't you dare feel sorry for him. He ate babies. Say something cruel so I can hate you properly."''',
        c('"He ate babies. I\'m not sorry."', "cruel", flags=(BOYS,)),
        c('[Raise your cup] "To Rakkoth, who sat outside the door."', "toast", flags=(BOYS,))),
    a("cruel", '''"Good." {n}She lets out a breath.{/n} "Good. That's the right answer. That's the answer a Commander gives." {n}She pours more wine.{/n} "You know, the other one of me would have wanted you to say something kind. I'm very glad I'm not her."''', c()),
    a("toast", '''{n}She stares at your raised cup. Then she lifts her own and touches it to yours, very softly.{/n}
"To Rakkoth. Who ate babies and sat outside the door." {n}She drinks it all.{/n} "That's the most demonic thing you've ever done, darling. Toasting a monster because it was loyal. You'd have fitted right in, in the Upper City." {n}She doesn't say anything else for a while.{/n}''', c()),
], (), delay=24)


# Q11: after the native Elysium ending (BestEnding; her touch no longer drains) the sessions that stage a drain close.
for _scene in SCENES:
    if _scene["Id"] in (BAKERY, ABYSS_TOUCH) and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world."""
