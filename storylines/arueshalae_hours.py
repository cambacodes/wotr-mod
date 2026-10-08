"""Arueshalae, further hours: the redeemed courtship's harder sessions, the chaplain's wedding, the hundredth day, and the fallen
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
                                             EVIL_UNIT, FAVOUR, HUB, P, RECRUITED, RETURNED, REUNITED, SCROLL, TAVERN_FAILED,
                                             DREZEN_PLACES, TAVERN_PRESENCE, UNANSWERED, UNIT, WARD_HELD, YARD_PRESENCE)
from storylines.arueshalae_chapel import CENSER, COUNTING
from storylines.arueshalae_treatment import CURE, CURED, DREZEN_AREA, ELYSIUM, INTAKE, MORNING, RELAPSE, RX_WANT, T, TOUCHED

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
    a("start", '"I\'ve been at the bakery on Tanner\'s Row. Since before dawn." {n}There is flour on her cheek and one wing.{/n} "I like the smell when they open the ovens. So I stood outside. This morning the baker\'s daughter found me beside the ash bucket and asked if I was hungry."',
        c("Continue", "hungry")),
    a("hungry", '"I said yes. She took me inside, and her father put a trough in front of me. I started reciting the travellers\' blessing." {n}She scowls at the flour on her sleeve.{/n} "He said, \'Bless it after you\'ve kneaded it. The second company wants its bread before muster.\' I thought he wanted something from a demon. He wanted someone with strong wrists."\n"I kneaded. He paid me in rolls. I gave them to the refugees. Then I went back to finish the next batch."',
        c("Continue", "girl")),
    a("girl", '"His daughter helped. She\'s twelve. She talked about the siege while we worked, and put her flour-covered hand on my arm to show me a fold."\n{n}Her hands close into fists.{/n} "I felt the edge of her. Warm, and sweet as the dough. I stepped away so fast I knocked the trough over. She called me clumsy, and I let her." {n}She looks at her fists.{/n} "I wanted to stay where I was, Commander. For one breath I wanted it more than the bread."',
        c('"You stepped away. That\'s the whole trick. Go back."', "back", flags=(BAKERY,)),
        c('"Go back, but wear gloves, and knead at the other end of the trough."', "gloves", flags=(BAKERY,)),
        c('"You\'re right. Leave it. Some things you can only want from a distance."', "leave", flags=(BAKERY,))),
    a("back", '"Go back." {n}She wipes her face and spreads the flour.{/n} "Yes. But at the other end of the trough. Gloves for the work, and no hands on me. I\'ll tell her father myself. He can decide whether he still wants my help."', c()),
    a("gloves", '"And I\'ll tell her father not to let her lean on me." {n}She nods.{/n} "She\'ll ask why. She asks why about everything. I\'ll have to answer. Flour isn\'t going to stop what my skin does."', c()),
    a("leave", '{n}She brushes flour off her wing.{/n} "Then I\'ll tell them I won\'t be back. They need bread before the troops march. I won\'t leave them expecting me." {n}Her voice drops.{/n} "I can still stand in the alley. For the smell."', c()),
], (INTAKE, RX_WANT), delay=24, chapters=(3, 5))


# --- The Abyss in her ears (Chapter 5, Drezen) -------------------------------------------------------------
# arue12 REBUILD (edge-fix-design §3.6): no dose. Back from the Abyss she is hunting again without meaning to, a sentry on
# the wall picked out and timed; "Evil calls me back. Every day." (dc2f5239). The ward is tested against a real want.

hub(ABYSS_TOUCH, "The Abyss in her ears", 5, '"Who are you watching?"', [
    a("start", '{n}You find her on the citadel steps after dark with her wings drawn in tight, watching the sentries walk the wall above the gate. She is counting them under her breath, and she does not stop when you sit down.{/n}\n"The third one from the gate. The one with the lamp. He hums when he turns at the end of his walk, and he turns slowly, and he\'s alone up there for as long as it takes to say the travellers\' blessing twice." {n}She says it the way a scout reports a ford.{/n} "I worked that out tonight without meaning to. We came back from the Abyss and I brought it home in my ears. Evil calls me back, Commander. Every day. Down there it shouted."\n"I never asked for your hand out there. Not once, from the crossing to the day we came back. I didn\'t think I could stop, there, if I started. I still don\'t know whether I left that down there or carried it home in my skin."',
        c('[Hold out your hand] "Then find out on me. Not on him."', "take", requires=(TOUCHED,), forbids=(TOUCHED,)),   # retired
        c('"Then don\'t find out. I\'ll sit here instead, between you and the wall."', "sit", flags=(ABYSS_TOUCH,)),
        c('[Spend a Scroll of Death Ward: send a page for the chaplain, and hold out your hand once he has read it over you] "Then find out on me. Not on him."',
          "take", requires=(WARD_HELD,), remove_item=SCROLL)),
    nar("take", '''{n}The chaplain comes down to the steps, breaks the seal, reads the ward over you, and goes back up without a word. She watches the sentry with the lamp turn at the end of his walk. Then she takes your hand with both of hers, too hard, the way a drowning woman takes a rope.{/n}''',
        c("Continue", "cure", requires=(CURED,)),
        c("Continue", "paid", forbids=(CURED,))),
    nar("cure", '''{n}Nothing comes out of you. The ward holds. But you can feel what she is doing on the other side of it: pulling, hard, the way she never pulled before the crossing, a tide throwing itself at a sea wall. She feels the wall, and does not let go. She keeps pulling, and her eyes are on the sentry, not on you.{/n}
{n}Then she does let go. She drops your hand as if it were a coal and sits there panting.{/n}''',
        c("Continue", "after")),
    nar("paid", '''{n}Nothing comes out of you. The ward holds. But you can feel her on the other side of it, pulling, a tide against a sea wall, and she feels the wall, and pulls harder, and keeps pulling, for one breath, for two, with her eyes on the lamp above the gate.{/n}
{n}She lets go before the third, and holds you by the shoulders with her face white as salt, as if you were the one who had nearly drowned.{/n}''',
        c("Continue", "after")),
    a("after", '''"Too much. I tried to take too much. There was a ward on you and I knew it, and I tried anyway, and I was looking at him while I did it." {n}She is shaking, and it is not fear; you have seen the same shake in soldiers after a charge they enjoyed.{/n}
"Whatever I was down there came back across the Wound in my skin, and I felt how much I could take, and I wanted all of it. Yours. His. The whole wall." {n}She sits back.{/n} "No more hands until it's gone out of me again. Ward or no ward, I'd find the minute it runs out, and I'd be glad, and then I'd never be anything else."''',
        c('"Then no more hands until it passes."', "home", flags=(ABYSS_TOUCH,))),
    a("sit", '''{n}You sit beside her on the steps, between her and the wall, keeping your hands on your knees. She watches them for a while. Then she watches the sentry with the lamp turn at the end of his walk, and turn back, and you watch her let him go, every time, step by step, all the way to the gate.{/n}
"Talk to me." {n}Her hands are locked together between her knees.{/n} "About anything. The market, the change of watch, your terrible jokes. Keep talking until he's off duty."''', c()),
    a("home", '''"Until it passes." {n}She smiles, and it is the smile of someone very tired.{/n} "You say that as if you knew it would. I don't. But I'll count the days, and one morning I'll tell you it has, and you'll have to decide whether I'm lying." {n}She shrugs.{/n} "Drezen isn't home. Nothing's ever been home. But I know which way it is from the Abyss now. That's new."''', c()),
], (TOUCHED,), delay=24, chapters=(5,))


# --- A bad day: the demon's temper ---------------------------------------------------------------------------

hub(BAD_DAY, "A bad day", 3, '"Arueshalae?"', [
    a("start", '''"What?" {n}It comes out as a snarl, and there is something in it that you have not heard from her before: a harmonic under the voice, like a second voice, cold and very old.{/n}
{n}She has her back to the tent pole. Her wings are half open and her nails are out, long and black, and she is breathing as if she has run a long way. When she sees it is you, she does not put any of it away.{/n}''',
        c("Continue", "tirade")),
    a("tirade", '''"Do you know what I did today? Nothing. I watched a squad of your soldiers flog a deserter, and I stood there, and I enjoyed it. I enjoyed every stroke. And then I went and knelt in the chapel and asked the goddess to take the enjoyment away, and she didn't, because she never does, because it's mine."
"I'm tired of your scrolls. I'm tired of your jokes. I'm tired of watching people eat soup and pretending it makes me better. It doesn't. I'm a demon who's pretending, and you're a Trickster who's enjoying the pretence, and one day one of us is going to stop."''',
        c('[Snap back] "Then stop pretending. Show me the demon. Go on."', "snap", flags=(BAD_DAY, SNAPPED_BACK)),
        c('[Sit down on the floor, out of reach, and wait.]', "wait", flags=(BAD_DAY,))),
    a("snap", '''{n}She does. Her wings open fully, filling the tent, and she is across it before you see her move, with her nails at your collar and her face an inch from yours, and the second voice under hers says your name the way it would say a meal's. You can smell the deserter's blood on her breath; she went close enough to the post to taste the air.{/n}
{n}Then she laughs, a horrible, broken laugh, and lets go of your collar one finger at a time.{/n} "That's what you wanted to see? You've seen it. That's what he'd have got, if they'd untied him and given him to me." {n}She slides down the pole until she is sitting, and does not put the nails away.{/n} "I'm not sorry I frightened you. I'm having a bad day. Can demons have bad days? I'm having one, and I'm enjoying parts of it."''', c()),
    nar("wait", '''{n}You sit down on the floor of the tent, just out of her reach, and say nothing at all. It takes a long time. The nails go first; then, slowly, the wings; last of all, the second voice under her breath.{/n}
{n}When she speaks again it is only her own voice, small and hoarse.{/n} "I watched them flog him. The deserter. Twelve strokes, and I counted every one, and I was sorry when they stopped." {n}She sits down opposite you, knees to her chest.{/n} "Desna sent me back to learn what dreams were, and I spent this morning wanting a man's back opened. Write it in my book for me; my hands aren't steady. 'She had a bad day. The Commander sat on the floor.' Don't you dare write down that it helped."''', c()),
# NM1 (Sol CAN/INT): a Drezen account (the squad, the chapel): Drezen only, never at the Nexus in Chapter 4; and never
# after BackToReality has released her (arueshalae.changed), when the pretence it rails against is over.
], (RELAPSE,), forbids=("arueshalae.changed",), delay=48, chapters=(3, 5), Areas=[DREZEN_AREA])


# --- After the yes: a first quarrel ---------------------------------------------------------------------------

hub(QUARREL, "A quarrel", 5, '"You\'re angry with me."', [
    a("start", '''"Yes. I am." {n}She has her arms folded and her chin up, and the quartermaster's ledger under one of them.{/n}
"I counted the seals. Every seal I've watched the chaplain break over you since the first seven minutes, every one of them so that I could hold your hand for seven minutes. And then I went to the scroll-sellers and asked the price, the way I used to price a mark's jewels." {n}Her voice shakes.{/n} "I have spent this whole war learning how not to take anything from anybody. And you've been paying for me by the minute, and you never once told me the sum."''',
        c("Continue", "fear")),
    a("fear", '''"Do you know what I thought, when I added it up? Not 'how kind'. I thought: that's a sergeant's pay, gone in the time it takes a candle to drip. That's bread for a street of the refugee quarter. That's what Lady Vellexia's guests spent to sit at her table, and she ate them anyway." {n}She is crying now, and furious about it.{/n}
"So yes. I'm angry. I'm going to be angry for at least a day. And you're going to let me, and you're not going to make a joke about it, and from now on you're going to tell me before you buy another, so that I can say no."''',
        c('"I\'ll tell you. Before. Every time."', "promise", flags=(QUARREL,)),
        c('"No. It\'s my coin, and it\'s my hand. I\'ll spend both as I like."', "cant", flags=(QUARREL,))),
    a("promise", '''"Every time." {n}She glares at you through her tears.{/n} "You say that about everything. Every time. It's the most frightening thing you say." {n}Then she sits down next to you, hard, and leans her head on your shoulder, on the cloth, the careful way.{/n} "I'm still angry. This is me being angry. Don't move."''', c()),
    a("cant", '''"No. I know you won't." {n}She wipes her face.{/n} "That's what makes it a real quarrel, I suppose. In the Upper City we never quarrelled. We just waited until someone was asleep." {n}She sits down, not next to you, but not far.{/n} "I'm going to be angry for two days, then. And afterwards I'll still be here, and I'll still take your hand when you've paid for it, and I'll hate that I do. That's new too."''', c()),
], (MORNING, CURED), delay=48, chapters=(5,))   # Sol r1 BEL: the quarrel is over the scrolls the player actually bought


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
    a("face", '''"You'll make a face." {n}She looks at you with enormous gravity.{/n} "The Commander of the crusade will stand at a laundress's wedding and pull faces at the chaplain." {n}Her mouth twitches.{/n} "Yes. Do that. If I look at you and you're pulling a face, I'll be too busy not laughing to be hungry. That's the best idea you've had since you made me a chaplain."''', c()),
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
    a("deal", '''"I'll ask you on the chapel steps." {n}She says it very seriously, as if booking an appointment.{/n} "Soon. When I've decided exactly what to ask. I've counted a hundred of them; I can wait for the right words." {n}A pause.{/n} "They're going to be the most frightening words I've ever said. Make sure you're there."''', c()),
], (COUNTING, AFTERTASTE), delay=72, chapters=(5,))


# --- The fallen: the queen's token and the boys -------------------------------------------------------------

tavern(TOKEN, "The queen's token", '"What\'s that round your neck?"', [
    a("start", '''{n}She lifts it out on its string: a small black pearl, the size of a fingernail, cold even on a warm night.{/n}
"This? My receipt. It was round my neck when I sat up, and nobody in that house would say whose hand had tied it. It means I'm hers, on loan. When she wants me, it'll get warm." {n}She rolls it between finger and thumb.{/n}''',
        c("Continue", "debt", requires=(DEBT,)),
        c("Continue", "favour", forbids=(DEBT, "nocticula.trickster.favour_called.arueshalae")),
        c("Continue", "favour_paid", requires=("nocticula.trickster.favour_called.arueshalae",), forbids=(DEBT,))),
    a("favour_paid", '''"Your favour. She came for it in her own court, and I watched you pay it, and the pearl went cold the moment you had." {n}She taps it.{/n} "I keep it anyway. A receipt is a receipt. And I like remembering your face."''',
        c("Continue", "end")),
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
    if _scene["Id"] in (BAKERY, ABYSS_TOUCH, HUNDRED, WEDDING) and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)
    # Sol verify (2026-10-01): the Abyss is told on the citadel steps, with the chaplain within call: Drezen only.
    if _scene["Id"] == ABYSS_TOUCH:
        _scene["Areas"] = [DREZEN_AREA]


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world."""
