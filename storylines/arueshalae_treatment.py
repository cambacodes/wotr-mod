"""Arueshalae, the living courtship: "The treatment" (Trickster path; arueshalae.md F18, the sneaky quack).

A Trickster Commander decides that a succubus's hunger is a medical condition and appoints themself her physician.
Every session is on her own companion hub (her unit is in the party), from Chapter 3 to Chapter 5, and every one of them
turns on something canon says about her: she watches mortals to understand them (hub Cue_0048ad6e, "I'm watching... I'm
trying to understand what they truly are"); "Any caress, of any kind, sucks the life from mortals" (Cue_0083 0cb8bb69);
she wants to kiss someone "only as a mortal. Not as a demon" (dfe62398); she grew up in Lady Vellexia's house in
Alushinyrra (f5160086); Nocticula told her to her face that she follows the Commander only by the queen's leave
(Nocticula_main/Cue_0523 b84ef61b).

The quack's one real power is the Trickster's own Lore (Religion) rank 1 (TricksterLoreReligionTier1Feature 04177c4d:
treat affliction "removes... any negative conditions"), bound as MainCharacterFacts trickster.religion_tier1. A
Commander who took that trick can name her drain a negative condition and treat it as fast as it lands. A Commander who
did not has no trick for it: they touch her anyway and pay in their own strength. Her native romance runs beside all of
this and is never started, completed or contradicted; where it has already happened (the Ch4 dream, the Ch5 flowers of
Elysium) the sessions read it.
"""
from story_format import c, n, scene
from storylines.arueshalae_trickster import (AFTERTASTE, CHAPLAIN, CLAIMED, CLOSED, COMMITTED, DEAD, DECLINED, EVIL_DEAD,
                                             FAILED, HUB, RECRUITED, RETURNED, SAINT_ONLY, STARTED, UNIT)

SCENES = []
T = "arueshalae.treatment."
CURE = "trickster.religion_tier1"          # MainCharacterFacts: the chosen Lore (Religion) rank 1 trick
LAB = "arueshalae.lab_seen"                # StartedDialogs: After_Lab (her desires shown to everyone), variant read
DREAM = "arueshalae.dream_woken"           # StartedDialogs: the native Ch4 dream (her kiss not deadly there), variant read
ELYSIUM = "arueshalae.elysium"             # StartedDialogs: the native Ch5 best ending (her touch no longer harms)

INTAKE = T + "intake"
STUDIED = T + "studied"
SLIPPED = T + "rite_slipped"
VOW_RITE = T + "vow_rite"
CANDLE_BEARER = T + "candle_bearer"
DISTANCE_KEPT = T + "distance_kept"
RX_WATCH = T + "rx_watch"
RX_WANT = T + "rx_want"
MEALTIMES = T + "mealtimes"
SAID_BETTER = T + "said_better"
SAID_QUACK = T + "said_quack"
RELAPSE = T + "relapse"
COME_TO_ME = T + "come_to_me"
STAY_OUT = T + "stay_out"
SERGEANT_STORY = T + "sergeant_story"
FORTY = T + "day_forty"
TOUCHED = T + "touched"
CURED = T + "cure_works"
DRAINED = "arueshalae.trickster.cost.drained"
ALUSHINYRRA = T + "alushinyrra"
WANTS_MEAL = T + "wants_a_meal"
QUEEN = T + "queen"
NO_DEALS = T + "promised_no_deals"
DEALS = T + "refused_to_promise"
KITCHEN = T + "kitchen"
RELAPSE_TWO = T + "relapse_two"
FAST = T + "fast"
NO_FAST = T + "no_fast"
HER_CALL = T + "her_call"
NIGHT = T + "night"
MORNING = T + "morning"

# Every treatment session is hers, on her hub, with her alive (or back) and not fallen.
GUARD = (CLOSED, DEAD, EVIL_DEAD, RECRUITED)
BACK = dict(ForbidOverrides={DEAD: RETURNED})


def a(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Arueshalae", **kw)


def session(id, title, chapter, entry, nodes, requires, forbids=(), delay=0, last=5, chapters=None, **extra):
    """One session of the treatment: physical, on her own companion hub."""
    SCENES.append(scene(id, title, "Arueshalae", chapter, entry, nodes, requires=requires, forbids=(*GUARD, *forbids),
                        delay=delay, last=last, Relationship="arueshalae", AnswerLists=[HUB], ContactUnit=UNIT,
                        Chapters=list(chapters or range(chapter, last + 1)), **{**BACK, **extra}))


# --- The reading (Chapter 3): the work before the joke --------------------------------------------------------------

session(STUDIED, "Night reading", 3, '"You were in the shrine library until the second bell."', [
    a("start", '''"I watch everyone. You know that." {n}She is standing at your elbow, looking at the books you have not put away: a Desnan breviary with a cracked spine, a travellers' psalter, a chaplain's commentary on the Song of the Spheres, all borrowed from the shrine, all open at the same page.{/n}
"The Tender of Dreams' blessing for travellers. The star-candle and the words for the road." {n}Her voice changes.{/n} "Why are you reading about my goddess's mercy at the second bell, Commander?"''',
        c("Continue", "why")),
    nar("why", '''{n}You tell her the truth, because she would hear anything else. You remember a thing she said once, quietly, as if confessing it: that she should like to kiss someone again, but only as a mortal. Not as a demon. You have been reading ever since.{/n}
{n}The Desnan rite for travellers asks the goddess to take the road's harm on herself for one night: one star, one night, one safe passage. And the Trickster's own lore can treat a negative condition as a priest treats a poison. You think the two will fit together. You are not sure.{/n}''',
        c('[Lay the two texts side by side: you already know the lore] "The rite points it. The lore does the rest."', "fit",
          requires=(CURE,)),
        c('[Work out the rite the hard way, from the chaplain\'s commentary]', forbids=(CURE,),
          check={"Skill": "SkillLoreReligion", "DC": 18, "Success": "fit", "Failure": "not_yet"})),
    a("fit", '''{n}She reads over your shoulder for a long time, her lips moving on the old Desnan words.{/n}
"One star, one night." {n}She sounds as though she is afraid to breathe on it.{/n} "Not a cure. A lamp you have to light every evening, and it only keeps one wolf off the road." {n}She straightens.{/n} "That's the first honest thing anyone has ever offered me. Everyone else offered me salvation."''',
        c("[Close the books.]", flags=(STUDIED,))),
    a("not_yet", '''{n}She watches you turn back three pages, then five, then the whole commentary, and lose the thread each time.{/n}
"You'll get there," she says. "Or you won't, and you'll have wasted a lot of candles on a demon." {n}She almost smiles.{/n} "Come back to it. I'll be here. I'm always watching."''', c()),
], ("trickster",), forbids=(STUDIED,), chapters=(3, 4, 5))


# --- Intake (Chapter 3): the pulse ----------------------------------------------------------------------------------

session(INTAKE, "Intake", 3, '[Hold out your hand, palm up] "You look pale. Let me take your pulse. When did you last eat?"', [
    nar("start", '''{n}She looks at your open hand the way a cat looks at a hand held out to it: as a question, and possibly a trap.{/n}
"You know what touching me costs." {n}It is not a warning so much as a fact she has been asked to confirm.{/n} "Every mortal who ever offered me their hand wanted something for it, or was paid to. What do you want?" {n}You tell her: her pulse. Only that. She considers it for a long breath, tilting her head, interested in spite of herself. Then she lays her wrist in your palm, lightly, ready to take it back.{/n}
{n}Her pulse, if a succubus has a pulse, is slow and faint and far too even, like a clock somebody forgot to wind. She watches your fingers on her skin, and then your face, and her ruby eyes are enormous.{/n}''',
        c("Continue", "laugh")),
    a("laugh", '''"When did I last..." {n}A laugh startles out of her, and she clamps her free hand over her mouth, appalled at herself.{/n} "Commander, I don't eat. Not the way you mean. I can taste your bread and your wine, and they are lovely, and they are like... like looking at a painting of a fire when you're cold."
{n}She tries to take her wrist back. You don't let her, yet.{/n} "I'm taking it back now. You shouldn't hold on so long. It isn't safe. Even this is costing you something, a little. You just can't feel it yet."''',
        c('"Answer the question. When did you last eat?"', "answer"),
        c('[Let go] "Sorry. Occupational habit."', "answer")),
    a("answer", '''{n}She rubs the place where your fingers were, as if it were her skin that had been hurt.{/n}
"Properly? Before the goddess. Before Desna caught me in the priestess's dream and made me look at what I was." {n}Her voice drops.{/n} "Since then I've taken only what I couldn't help. A brush of hands in a crowd. Someone's breath when they sleep too close to the fire. Crumbs. I've lived on crumbs for years, and I tell myself every day that I'm not hungry, and every day it's a lie."''',
        c("Continue", "diagnosis")),
    nar("diagnosis", '''{n}You make the face that the Kenabres field surgeons made when they had bad news and no time: a short nod, a click of the tongue, a hand on the hip.{/n}
"Starvation," you tell her. "I'd write it on the chart, if you had a chart."
{n}Her mouth twists.{/n} "Starvation. That's a mortal word. You starve because there's no bread. I'm not short of bread, Commander. I'm surrounded by it every hour, and it talks to me, and thanks me for my prayers." {n}She looks at the hand that held her wrist.{/n} "I'll tell you what it is. I want to be touched and not count what I took. I want to kiss someone the way a mortal does, and have them still there afterwards. Once. That's the whole illness."
"Then I've spent three nights in the shrine library finding out what that would take," you tell her. "Somebody has to be the doctor. I've read the texts. I'm the nearest thing you've got."''',
        c("Continue", "her")),
    a("her", '''{n}For a moment you think you have hurt her. Then she sits down, very suddenly, on an ammunition crate, and laughs until she has to wipe her eyes on her sleeve, and the laugh is the most unguarded sound you have ever heard her make.{/n}
"A doctor. For a succubus. Oh, gods, they'd hang you in Alushinyrra, and then they'd hire you." {n}She sobers, a little.{/n} "Very well, doctor. What do you prescribe? I warn you, I've been prescribed things before. Chains, mostly."''',
        c('"Watch people eat. Three times a day. Take notes."', "watch", flags=(INTAKE, RX_WATCH, STARTED)),
        c('"Every day, tell me one thing you want that isn\'t a person."', "want", flags=(INTAKE, RX_WANT, STARTED)),
        c('"Actually, I\'ll need a second visit to decide. Doctors always do."', abort=True)),
    a("watch", '''"Watch people eat." {n}She says it slowly, testing it for the trick.{/n} "I already watch them. I watch them all the time, it's what I do instead of... I've told you. Watching them is how I learn what they are."
"Not like this, though. Not on purpose, three times a day, as medicine." {n}She almost smiles.{/n} "All right. I'll take notes. You'll regret asking to read them."''', c()),
    a("want", '''"One thing I want that isn't a person." {n}She looks genuinely frightened, which you did not expect.{/n} "I don't know if I have any. That's the whole... that's the problem, Commander. Demons don't want things. We want people. Everything else is a way of getting to them."
"But I'll try. Every day. If I can't think of one, I'll come and tell you that instead, and you'll have to live with the disappointment."''', c()),
], ("trickster", STUDIED), forbids=(INTAKE,), chapters=(3, 4, 5), EntryMythic="PlayerIsTrickster")


# --- Mealtimes: the first report ----------------------------------------------------------------------------------

session(MEALTIMES, "Case notes", 3, '"How is the patient?"', [
    a("start", '''{n}She has a little book now, a clerk's daybook bought off a Drezen stationer, and she holds it against her chest as if she expected you to take it.{/n}
"I've done as you said. I don't know if it's helping. I don't know what helping would look like." {n}She opens it, closes it, opens it.{/n} "Do you want to hear, or is this one of those prescriptions where the doctor doesn't care whether the patient takes it?"''',
        c("Continue", "watch", requires=(RX_WATCH,)),
        c("Continue", "want", forbids=(RX_WATCH,))),
    a("watch", '''"Morning, the mess tent of the second company. They eat standing up, with their helmets under their arms. Nobody finishes their porridge. Everybody complains about it. Somebody always gives the last of theirs to the dog." {n}She turns a page.{/n}
"Noon, the market. A woman bought two apples and cut one in half with her teeth and gave half to a man who wasn't her husband, and the husband saw, and laughed, and then he stole the other apple out of her basket, and she hit him with the basket. I watched them for an hour. I think they were happy. I didn't understand one moment of it."''',
        c("Continue", "evening")),
    a("want", '''"I kept the list. Day one: nothing. I told you I would come and say so, and then I didn't, because I was ashamed. Day two: I want the cat that sleeps on the smithy roof to like me. It doesn't. Day three: I want the smell of the bakery on Tanner's Row at dawn. Not the bread. The smell."
{n}She turns a page, and her cheeks colour.{/n} "Day four I've crossed out. Day five: I want to know what the Kenabres refugees sing when they're mending nets. They stop when I come close."''',
        c("Continue", "evening")),
    a("evening", '''"And then, in the evening, I sat at the back of Fye's, where nobody looks, and I watched them eat together, and talk with their mouths full, and pass bread with their dirty hands, and I realised something." {n}She closes the book.{/n}
"In the Abyss, a meal is always one creature eating another. Here, most of the time, it's two creatures eating a third thing, and talking over it. I didn't know that. I've been on this world for years and I didn't know that." {n}She looks at you with something almost like accusation.{/n} "Why do you call it a treatment? What's getting treated?"''',
        c('"You\'re getting better. That\'s what treatment is for."', "better", flags=(MEALTIMES, SAID_BETTER)),
        c('"Because I\'m a quack, and quacks need patients."', "quack", flags=(MEALTIMES, SAID_QUACK))),
    a("better", '''"Better." {n}She says the word as if it were in a language she had studied but never heard spoken.{/n} "I don't think succubi get better. I think we get managed, or we get killed." {n}She tucks the book into her belt.{/n} "But you've written it down now. So I suppose it's official. The Commander of the crusade says I'm getting better." {n}A pause.{/n} "Don't tell anyone. They'll want a second opinion."''', c()),
    a("quack", '''{n}She laughs, the startled laugh again, and this time she doesn't cover it.{/n} "A quack. Yes. That's much more honest." {n}She tucks the book into her belt.{/n}
"You know what's strange? I trust that more. Every holy man who ever tried to save me was certain. You're the first one who's admitted they're making it up." {n}She considers.{/n} "I'll keep taking the medicine, quack. But I want it noted that I'm doing it out of spite."''', c()),
], (INTAKE, "trickster.ever"), forbids=(MEALTIMES,), delay=24, chapters=(3, 4, 5))


# --- The relapse: a sergeant at Fye's ------------------------------------------------------------------------------

session(RELAPSE, "Relapse", 3, '"You haven\'t been to see me."', [
    nar("start", '''{n}She has been avoiding you for two days. When you finally corner her behind the stables, she backs against the wall as if you were the one to be afraid of, and keeps her hands behind her back.{/n}''',
        c("Continue", "lab", requires=(LAB,)),
        c("Continue", "confess", forbids=(LAB,))),
    a("lab", '''"You heard what I want. In Areelu's laboratory, when the demon in the walls pulled it out of my head and shouted it for everyone to hear. You heard every word." {n}She is very pale.{/n} "You said then that thoughts aren't deeds. I held onto that. I held onto it so hard. And then the night before last I nearly made one of them a deed."''',
        c("Continue", "confess")),
    a("confess", '''"There was a sergeant at Fye's. Third company, the one with the red beard. He was drunk, and he was kind in the way drunk men are kind, and he sat down next to me at the back and put his hand on mine and asked me if I was lonely." {n}Her voice has gone flat and precise, like a report.{/n}
"I was. I said yes. I didn't take my hand away. I felt him begin to go, just a little, just at the edges, and it was so good, Commander. It was the best I've felt since the goddess. And I sat there, and I let it go on for as long as it takes to breathe in, and out, and in again."''',
        c("Continue", "stopped")),
    a("stopped", '''"And then I stood up and walked out into the rain without paying for my wine, and I didn't stop walking until I was at the far end of the city wall, and I stayed there till dawn." {n}She looks at her hands, finally, as if they belonged to the sergeant.{/n}
"He's fine. I went back to look. He's fine. He'll have had a headache and thought it was the ale. He won't ever know." {n}She lifts her chin, bracing for the verdict.{/n} "So. Desna's priests would give me a road to walk and a star to walk it by. What do you give me?"''',
        c('"Next time, come to me. Whatever hour. I\'ll be the one who notices first."', "come", flags=(RELAPSE, COME_TO_ME)),
        c('"Then stay out of Fye\'s for a while. Out of taverns, out of crowds."', "stay_out", flags=(RELAPSE, STAY_OUT)),
        c('[Straight-faced] "I\'ll tell the sergeant he was blessed by a Desnan saint in disguise. He\'ll dine out on it for years."',
          "saint_story", flags=(RELAPSE, SERGEANT_STORY))),
    a("come", '''"Come to you." {n}She says it as if you had told her to walk into a fire to warm up.{/n} "Commander, you are the last person I should come to when I'm hungry. You're the one I..." {n}She stops herself.{/n}
"No. I understand. You'd rather I came to you than to a stranger. Because you know what I am, and he didn't." {n}Something in her face eases, and something else tightens.{/n} "All right. I'll come to you. And you'll send me away. Promise me you'll send me away."''', c()),
    a("stay_out", '''"Out of taverns." {n}She nods too quickly.{/n} "Yes. That's sensible. That's what a real doctor would say." {n}She is quiet for a moment.{/n}
"The only thing is... that's where they are. The mortals. That's where they laugh and sing and hold each other's hands. If I stay out of the places where they're happy, I'll learn everything about them except the one thing I want to understand." {n}She squares her shoulders.{/n} "But I'll do it. For a while. I've walked worse roads for worse gods."''', c()),
    a("saint_story", '''{n}She opens her mouth to protest, and nothing comes out. Then she laughs, helplessly, and slides down the stable wall until she is sitting in the straw.{/n}
"A saint. In disguise." {n}She is laughing and crying at the same time.{/n} "You're horrible. Tender of Dreams forgive me, you're horrible. I nearly ate a man and you're going to tell him he was blessed." {n}She wipes her face.{/n} "He'll believe you. That's the worst of it. He'll light a candle at the shrine every week for the rest of his life, and I'll have to walk past it."''', c()),
], (MEALTIMES, "trickster.ever"), forbids=(RELAPSE,), delay=48, chapters=(3, 4, 5))


# --- The touch: the quack's cure ---------------------------------------------------------------------------------

session(TOUCHED, "The procedure", 3, '"I want to try something. Give me your hand."', [
    a("start", '''{n}She puts both hands behind her back at once, like a child hiding a stolen biscuit.{/n}
"No. You know I can't. You know what happens." {n}She eyes your outstretched hand as if it were a drawn sword.{/n} "Any caress, Commander. Any caress of any kind. That's not a manner of speaking. It's what I am."''',
        c("Continue", "dream", requires=(DREAM,)),
        c("Continue", "explain", forbids=(DREAM,))),
    a("dream", '''"I know what you're thinking. In the dream, it didn't hurt. In the dream I could..." {n}Her cheeks go dark.{/n} "But that was the dream. That was the one place in all the worlds where my kiss isn't death. Out here I'm still what I was built to be. I won't risk you out here just because it was lovely in there."''',
        c("Continue", "explain")),
    nar("explain", '''"It's a procedure," you tell her. "I read about it in a book I haven't written yet. You hold my hand. Whatever it costs, I'll know, the moment it happens. And I'll deal with it."
{n}She searches your face for the joke. For once, you aren't making one. It frightens her more than the hand does.{/n}
"And if you can't deal with it?"
"Then I'll have learned something, and so will you. That's what procedures are for."''',
        c('[Light the star-candle, say the travellers\' blessing, then hold out your hand] "One star, one night."', "cure_try",
          requires=(CURE,), mythic="Trickster"),
        c('[Light the star-candle and say the blessing from the chaplain\'s commentary, word for word]',
          forbids=(CURE,), check={"Skill": "SkillLoreReligion", "DC": 20, "Success": "cure_try", "Failure": "pay_try"}),
        c('"You\'re right. Not yet."', abort=True)),
    nar("cure_try", '''{n}She takes it. Her fingers are cool and very light, and for a heartbeat nothing happens, and then the cold begins: not in your hand, in the middle of you, like a draught under a door.{/n}
{n}The candle gutters. You name the drain a negative condition, the way a priest names a poison, and the rite takes it: the cold goes out of the middle of you and into the little star-flame, which burns blue for a breath and then goes out.{/n}
{n}The second drain comes a heartbeat later, and there is nothing to take it. She feels it land and lets go at once.{/n}''',
        c("Continue", "cured")),
    a("cured", '''{n}She is staring at your joined hands. She has stopped breathing, if she breathes.{/n}
"One." {n}Her voice is tiny.{/n} "One whole breath with your hand in mine, and it didn't take anything. The candle took it." {n}She is staring at the dead wick.{/n} "And then it was me again. I felt it. It would have been you the next breath, and the one after."
"One star, one night," you tell her. "Until I sleep. Every evening, if you want it. That's the treatment."
{n}She holds her own hand, the one you held, against her chest, and begins to cry, silently.{/n} "I've never held anyone's hand before without killing a little of them. Not once. One breath. Every evening. I'll take it."''',
        c("[Keep holding her hand.]", flags=(TOUCHED, CURED))),
    nar("pay_try", '''{n}She takes it. Her fingers are cool and very light, and then the cold begins: not in your hand, in the middle of you, like a draught under a door, and it keeps coming. The edges of the room go soft. Your knees tell you they have an opinion about standing.{/n}
{n}You have no trick for this. You have only the choice to keep holding on, and you make it, for three long breaths, and then she makes it for you and tears her hand away.{/n}''',
        c("Continue", "paid")),
    a("paid", '''{n}You are sitting on the ground. She is kneeling in front of you, holding your face between her wrists, not her palms, careful even now.{/n}
"You idiot. You absolute idiot. You could see it happening and you didn't let go." {n}She is furious. She is shaking.{/n} "Three breaths. You gave me three breaths of you, on purpose, knowing. Nobody has ever... they always pull away. Always. They scream, or they pray, or they pull away."
{n}She sits back on her heels.{/n} "Don't do that again. Please. And I'll be thinking about it every hour until you do."''',
        c("[Catch your breath.]", flags=(TOUCHED, DRAINED))),
], (RELAPSE, "trickster.ever"), forbids=(TOUCHED,), delay=48, chapters=(3, 4, 5))


# --- Alushinyrra (Chapters 4-5): the house she grew up in ---------------------------------------------------------

session(ALUSHINYRRA, "Where I grew up", 4, '"Tell me about the house you grew up in."', [
    a("start", '''{n}She is quiet for so long you think she will not answer. The Abyss does that to her: in the camps of the Abyss she sleeps less and watches more, and she stands between you and the dark without seeming to notice she does it.{/n}
"Lady Vellexia's house. In the Upper City, in Alushinyrra. I told you once. I didn't tell you what it was like." {n}She hugs her knees.{/n} "It was beautiful. Everything in it was beautiful. The guests were beautiful, until they weren't. There was a room where they served dinner every night for a thousand years, and nobody who sat at that table was ever the one eating."''',
        c("Continue", "table")),
    a("table", '''"That's what I remember about meals. The long table, the candles, the silver. The guests in their best clothes, trying so hard to entertain her. And the food on the plates, which nobody touched, because the food was never the point. The point was which of them would still be at the table when the candles burned down."
{n}She looks at you.{/n} "You made me sit in Fye's and watch soldiers eat porridge. Do you know what it was like, the first time? I kept waiting for someone at the table to die."''',
        c("Continue", "question")),
    nar("question", '''{n}You ask her the only question a doctor could ask: if she could eat anything, anything at all, a meal that would really feed her and cost nobody, what would it be?{/n}
{n}She thinks about it for a long time. She takes it seriously, the way she takes all your prescriptions seriously, even the ones that are jokes.{/n}''',
        c("Continue", "meal")),
    a("meal", '''"A meal someone made for me." {n}She says it so quietly you almost miss it, and then she flushes, as if she had said something indecent.{/n}
"Not bought. Not stolen. Not... served, the way Lady Vellexia served. Made. By someone who didn't know how to cook, who got it wrong, and gave it to me anyway because they wanted me to have it." {n}She laughs at herself.{/n} "That's ridiculous. It wouldn't feed me. I'd taste it and it would be a painting of a fire again. But I'd eat every crumb."''',
        c('"Noted. That\'s going in the treatment plan."', "noted", flags=(ALUSHINYRRA, WANTS_MEAL)),
        c('"That\'s not ridiculous. That\'s the first thing you\'ve wanted that isn\'t a person."', "first",
          flags=(ALUSHINYRRA, WANTS_MEAL))),
    a("noted", '''"The treatment plan." {n}She rests her chin on her knees and smiles at the dark.{/n} "You haven't got a treatment plan. You've got a pocket full of jokes and a very straight face." {n}A pause.{/n} "Write it down anyway. I want to see what it looks like in your handwriting."''', c()),
    a("first", '''{n}She goes absolutely still. Then she counts on her fingers, silently, going back through days you can't see.{/n}
"It is," she says, astonished. "It is. The cat doesn't count; I wanted the cat to want me. The smell of the bakery was close. But this..." {n}She presses her hand to her mouth.{/n} "That's the first thing. The first thing I've wanted that isn't somebody. Oh. Oh, I'm going to cry in the Abyss, in front of a demon's camp, and it's your fault."''', c()),
], (INTAKE, "trickster.ever"), forbids=(ALUSHINYRRA,), delay=24, chapters=(4, 5))


# --- The queen's claim (optional; after Nocticula_main/Cue_0523) --------------------------------------------------

session(QUEEN, "Only because I allow it", 4, '"You\'ve been quiet since the Midnight Isles."', [
    a("start", '''"She knelt me. Did you see? I didn't decide to. My knees went down on the marble in front of her, and I was already on them before I knew they'd moved." {n}Her hands are fists in her lap.{/n}
"'This demon follows you around only because I allow it.' That's what she said. And the worst thing, Commander, the very worst thing, is that she might be right. I don't know. I have never known where she stops and I start. She made the first of us. She might have made the part of me that thinks it's free."''',
        c("Continue", "ask")),
    a("ask", '''{n}She turns to you, and her face is naked with fear.{/n}
"Promise me something. If I die, if I fall, if anything happens to me, don't bargain with her. Don't write to her, don't ask her, don't let her name a price for me. She'll say yes. She always says yes. And then she'll own a piece of you, and she'll wear it on a string round her neck and show it to her guests."''',
        c('"I promise. No deals with the queen. Not for you."', "promise", flags=(QUEEN, NO_DEALS)),
        c('"I can\'t promise that. I bargain with everyone. It\'s what I\'m for."', "refuse", flags=(QUEEN, DEALS))),
    a("promise", '''"Thank you." {n}She lets out a long breath, and some of the rigidity goes out of her.{/n} "I know it's a lot to ask of a Trickster. Promising not to bargain is like promising not to breathe." {n}She almost smiles.{/n} "Which, now I think of it, is something I'm very good at, so I'll keep you company."''', c()),
    a("refuse", '''{n}She watches you in silence, and then, very slowly, she nods.{/n}
"No. Of course you can't. If you could, you wouldn't be you, and she'd have one less thing to fear in the whole of the Abyss." {n}She looks away, towards the violet horizon of the Midnight Isles.{/n} "Just... if you ever do it, don't tell me what you paid. I don't want to have to carry that as well."''', c()),
], (CLAIMED, INTAKE, "trickster.ever"), forbids=(QUEEN,), delay=24, chapters=(4, 5), optional=True)


# --- The kitchen (Chapter 5): the meal someone made -----------------------------------------------------------------

KITCHEN_OPEN = '''{n}You requisition the officers' kitchen in the citadel for an evening, which the cook allows only after you promise not to touch the good knives. You touch the good knives. You burn the onions. You make something that is meant to be a Mendevian farmhouse stew and is, generously, brown.{/n}
{n}She comes in because you sent a page with a note that said only "Doctor's orders. Seventh bell. Kitchens." She stops in the doorway and looks at the table, at the two bowls, the heel of bread, the wine you have not stolen, and her hand goes to her mouth.{/n}'''
session(KITCHEN, "A meal someone made", 5, '"Seventh bell. You said kitchens."', [
    nar("start", KITCHEN_OPEN, c("Continue", "sit")),
    a("sit", '''"You remembered." {n}She sits down as if the bench might give way under her.{/n} "I told you in the Abyss and I thought you'd forgotten it."
{n}She picks up the spoon. She eats. She eats slowly, all of it, every burnt piece of onion, and you can see on her face that it is exactly what she said it would be: a painting of a fire. She eats it anyway, as if it were a fire.{/n}''',
        c("Continue", "taste")),
    a("taste", '''"It's terrible." {n}She wipes the bowl with the bread.{/n} "It's truly terrible, Commander. Lady Vellexia's cooks would have been flayed for it, and they'd have deserved it." {n}She puts the bread in her mouth, and chews, and swallows, and her eyes are wet.{/n}
"It's the best thing anyone has ever given me. And it didn't feed me at all. And I'm not hungry. How am I not hungry?"''',
        c("Continue", "hand_cure", requires=(CURED,)),
        c("Continue", "hand_paid", forbids=(CURED,))),
    nar("hand_cure", '''{n}She reaches across the table and takes your hand, the one with the onion burn on the knuckle, and turns it over, and presses her lips to the burn.{/n}
{n}You lit the candle at dusk, before the onions burned; it is still going on the windowsill. The cold begins at once, deep and sweet, and the little flame on the sill takes it and goes blue. She lifts her mouth away before the second one can come, deliberately, watching your face over your knuckles.{/n}
"Still working," she says. "One a night. I counted it. Good."''',
        c("Continue", "after")),
    nar("hand_paid", '''{n}She reaches across the table and takes your hand, the one with the onion burn on the knuckle, and turns it over, and looks at it for a long time. Then she presses her lips, very briefly, to the burn.{/n}
{n}The cold comes, sharp and quick. You feel it take something. She feels you feel it, and lets go at once, and holds her own wrist as if she had burned herself.{/n}
"One," she says, shakily. "That's all. One kiss, for the cook. That was worth it. That was worth whatever it cost you, and I'm sorry, and I'm not sorry."''',
        c("Continue", "after")),
    a("after", '''{n}She stays until the candles are low, helping you wash the bowls in a basin of cold water with the concentration of someone performing surgery.{/n}
"I've been asking what I dream of. Since the goddess. I still don't know." {n}She dries the last bowl.{/n} "But I think I know what I want to remember, when I'm very old, if demons get old. I want to remember that somebody burned the onions for me."''',
        c("[Leave the bowls to dry.]", flags=(KITCHEN,))),
], (TOUCHED, ALUSHINYRRA, "trickster.ever"), forbids=(KITCHEN,), delay=48, chapters=(5,))


# --- The second relapse (Chapter 5): wanting the wrong thing ------------------------------------------------------

session(RELAPSE_TWO, "Contraindications", 5, '"You look like you haven\'t slept."', [
    a("start", '''"I haven't. I don't, mostly, but this is different. This is the other kind of not sleeping." {n}She is sitting on the edge of her bedroll with the daybook open on her knees, and she has not written anything in it.{/n}
"I have to tell you something, and you're not going to like it, and I'm not going to be able to say it twice."''',
        c("Continue", "want")),
    a("want", '''"Since the kitchens, since your hand... I've started to want it. Not you. It. The cold going out of you and into me. Whether it stays or whether you lift it off, I don't care, I just want the moment when it starts." {n}She is gripping the book so hard the cover bends.{/n}
"I lie here and I count the hours until I can see you, and I don't know if I'm counting them because I love your company or because I'm hungry and you're the only food in all the world I'm allowed to have. I can't tell the difference any more. I used to be able to tell. That was the one thing I was proud of."''',
        c("Continue", "ask")),
    a("ask", '''{n}She closes the book.{/n} "So I want to stop. The treatment. The hand. Just for a while. I want to go back to crumbs and see whether I still want to see you when there's nothing in it for the hunger."
{n}She looks at you, defiant and terrified.{/n} "Or you can tell me that's stupid, and that I'm being dramatic, and that you know what you're doing. You usually do. Even when you're joking."''',
        c('"Then we stop. A week. No hands. I\'ll still come and see you."', "fast", flags=(RELAPSE_TWO, FAST)),
        c('"No. You\'re not a danger to me. We keep going."', "no_fast", flags=(RELAPSE_TWO, NO_FAST)),
        c('"You\'re the patient. You decide. I\'ll follow the prescription you write."', "her_call",
          flags=(RELAPSE_TWO, HER_CALL))),
    a("fast", '''"A week." {n}She nods, and nods again.{/n} "And you'll still come. Even when there's nothing to give me." {n}She tries to smile.{/n} "That's the experiment, then. If I'm still glad to see you on the seventh day, it's you. If I'm not, it was the hunger all along, and you should find a better class of patient."''', c()),
    a("no_fast", '''"You're very sure." {n}She studies your face, the way she studies strangers in the market.{/n} "That's what frightens me. You're very sure, and you've never been a succubus, and I have." {n}She closes her eyes.{/n}
"All right. We keep going. But if I ever take more than you mean to give, you tell me. At once. Out loud. Don't be kind about it. Kindness is how they die."''', c()),
    a("her_call", '''{n}She stares at you. Then she gets up, crosses the room, and bends to your ear, and says a word into it that is not Arueshalae: a name made of sounds a throat was not built for, that stings the ear like smoke.{/n}
"That's the one they made me with. In the Abyss a demon's name is a leash. Whoever holds it can stop her." {n}She straightens, very pale.{/n} "If I ever start to take more than you're giving, say it. I'll stop. I won't be able not to." {n}She sits back down on the bedroll, shaking.{/n} "Nobody has held that since the Delights. Don't lose it. Don't ever use it for anything else."''', c()),
], (KITCHEN, SLIPPED, "trickster.ever"), forbids=(RELAPSE_TWO,), delay=48, chapters=(5,))


# --- The rite slips (Chapter 5): the cost, and her distance ---------------------------------------------------------

session(SLIPPED, "A missed night", 5, '"You\'re awake. Don\'t get up."', [
    nar("start", '''{n}The march from the Ivory Labyrinth ran late, the candles were in the baggage, and you fell asleep in your boots without saying the blessing. You remember her coming to the tent. You remember reaching for her, half-asleep, and her not pulling away fast enough.{/n}
{n}You wake a day later. A whole day: the council met without you, and the quartermaster signed for you, and nobody could rouse you. Your hands are cold to the wrist and will not warm at the brazier. When you try to stand, the tent tilts.{/n}''',
        c("Continue", "her")),
    a("her", '''{n}She is sitting in the far corner of the tent, as far from the cot as the canvas allows, with her knees drawn up and her wings wrapped round them. Her face is grey. You have seen that look on the faces of the soldiers who dug out Kenabres.{/n}
"You didn't light it." {n}Her voice is very flat.{/n} "You reached for me and I was hungry and I didn't stop, not for a long breath, and you didn't say the words, and I didn't make you. The chaplain says you'll keep the cold in your hands for a month." {n}She looks at the cold hands, and away.{/n}''',
        c("Continue", "distance")),
    a("distance", '''"So I've moved my bedroll. To the chapel crypt, in Drezen. Here, to the baggage lines." {n}She has plainly rehearsed this.{/n} "Somewhere I can't reach you in the night. Not until you can light that candle every single evening, march or no march, without once forgetting. I won't be the thing you forget about."''',
        c('"Then I\'ll never forget it again. Every night. I swear it on the road."', "vow", flags=(SLIPPED, DRAINED, VOW_RITE)),
        c('"Sleep where you like. I\'ll come to you, every night, with the candle lit."', "come", flags=(SLIPPED, DRAINED, CANDLE_BEARER)),
        c('"You\'re right. Keep your distance for a while. I\'ll earn it back."', "earn", flags=(SLIPPED, DRAINED, DISTANCE_KEPT))),
    a("vow", '''"On the road." {n}She looks at you for a long time over her knees.{/n} "Desnans don't swear on the road lightly. Travellers die on it." {n}She does not move from the corner.{/n} "Then I'll come back to the tent when I've watched you keep it for a week. Not before. Rest your hands."''', c()),
    a("come", '''{n}She laughs, once, badly.{/n} "You'd walk down to a crypt every night with a candle, to a demon who nearly ate you." {n}She hugs her knees tighter.{/n} "Yes. Come. Knock first. And if you ever come without the candle lit, I'll know, and I'll put it out of your reach before you can argue."''', c()),
    a("earn", '''"Earn it back." {n}She nods, and nods again, and her eyes are wet.{/n} "Yes. That's fair. That's what mortals say, isn't it, when they've done something that can't be undone? I'll wait. I'm good at waiting. I'm getting better at it every day you give me to practise."''', c()),
], (TOUCHED, KITCHEN, "trickster.ever"), forbids=(SLIPPED,), delay=24, chapters=(5,))


# --- The proposal (Chapter 5): she asks (06-ROUTE-REGISTRY §3: "she proposes"; no test, no price) ---------------------

session(T + "prescription", "The patient proposes", 5, '"You asked me to meet you here."', [
    nar("start", '''{n}The citadel wall at dusk, where she goes to watch the city light its lamps. She sent a page for you, which she has never done. She is standing very straight, with her hands clasped behind her back, like a soldier about to deliver a report she has rehearsed until it stopped making sense.{/n}''',
        c("Continue", "fast", requires=(FAST,)),
        c("Continue", "no_fast", requires=(NO_FAST,)),
        c("Continue", "her_call", forbids=(FAST, NO_FAST))),
    a("fast", '''"Seven days. No hands. I marked them off on the wall of the well-house with a nail, so I couldn't cheat." {n}She smiles, shakily.{/n} "And on the seventh day I was still glad to see you. I was gladder. I was so glad I went and stood in the well-house so nobody would see my face. So. It's you. It isn't only the hunger. It's you."''',
        c("Continue", "list", requires=(FORTY,)),
        c("Continue", "risk", forbids=(FORTY,))),
    a("no_fast", '''"You were right. I hate that you were right." {n}She keeps her hands behind her back.{/n} "You never let me take more than you meant. Not once. And you told me, every time, out loud, and you weren't kind about it. I think that's the kindest thing anyone has ever done for me."''',
        c("Continue", "list", requires=(FORTY,)),
        c("Continue", "risk", forbids=(FORTY,))),
    a("her_call", '''"You have my name. The old one. And you've never said it." {n}She keeps her hands behind her back.{/n} "There was a night I nearly took too much. I felt you draw breath to say it, and you didn't. You said 'Arueshalae' instead, and I stopped anyway, because you'd chosen the name I chose." {n}Her mouth works.{/n} "Every demon in the Upper City would have used that leash by now. You held it for a month and never once pulled."''',
        c("Continue", "list", requires=(FORTY,)),
        c("Continue", "risk", forbids=(FORTY,))),
    a("list", '''"You wanted to know what day forty was, on the list. The one I kept back." {n}She doesn't take it out. She knows it by heart.{/n}
"'Day forty: I want to ask the Commander something, and I want to be the one who asks, for once in my life, instead of the one who's asked.'" {n}She swallows.{/n} "So. That's what this is. I'm doing day forty."''',
        c("Continue", "risk")),
    a("risk", '''"But first you have to hear the thing I'm most afraid of, because I won't ask with it hidden." {n}She does not look at you.{/n} "One night the candle will be out. A march, a siege, a night you forget. I'll be hungry, and you'll be asleep, and I won't stop in time. Not a lost day. The rest of you." {n}Her voice drops.{/n} "What happens then?"''',
        c('"Then I\'ll wake, and run, and not come back till you send for me."', "ask"),
        c('"Then I\'ll have known the price every night and paid it. That\'s mine to decide, not yours."', "ask"),
        c('"Then we don\'t sleep in the same room on those nights. Ever. That\'s the rule, not the risk."', "ask")),
    a("ask", '''{n}She brings her hands out from behind her back. They are empty. She holds them out to you, palms up, not touching, an inch away.{/n}
"I'm not going to test you. I've tested everyone I ever met and it never once made me happy. I'm just going to ask." {n}Her voice goes very small and very steady.{/n} "Will you have me? All of it. The praying and the wanting. The priests hoped those were two things; they never were. It's one knot, and it's mine, and I'm asking you to hold it."''',
        c('"Yes. Both of you."', "both", flags=(COMMITTED,)),
        c('"Yes. But keep the hunger out of my sight."', "saint", flags=(COMMITTED, SAINT_ONLY)),
        c('"Not yet. Ask me again when we\'ve both slept."', "not_yet", flags=(DECLINED,)),
        c('"No."', "neither", flags=(CLOSED,))),
    a("both", '''{n}She closes the inch, and then does not seem to know what to do with your hand now she has it.{/n} "Both." {n}She says it again, as if checking it for a trick.{/n} "Both. I... I had something to say after that. I had a whole... it's gone." {n}Her grip tightens.{/n} "I want you so much right now it frightens me. And it's me wanting. There's nobody else in here to blame it on." {n}She laughs, very softly, and it shakes, and she does not let go.{/n} "Don't say anything. I'll get it wrong again. Just stay where you are."''', c()),
    a("saint", '''"Only the parts of me that pray, then." {n}She nods, and something shutters in her face, smoothly, the way it must have in Lady Vellexia's house when a guest said the wrong thing.{/n}
"There aren't two of me. There never were; that was the Upper City's story, so the guests could feel clean. But I'll keep the wanting out of your sight. I'm very good at that. You won't thank me for it one day. But I asked, and you answered, and that's more than I ever expected to be given."''', c()),
    a("not_yet", '''{n}She lets her hands fall. She does not look hurt; she looks like someone recalculating a route.{/n} "Not yet." {n}She nods.{/n} "All right. I've waited longer for smaller things." {n}A small, crooked smile.{/n} "But I asked first. That's done. That can't be taken back. The next one's yours."''', c()),
    nar("neither", '''{n}She puts her hands behind her back again, very carefully, as if putting something away in a drawer. Then she goes down the steps and into the city, and the lamps come on behind her one by one.{/n}''', c()),
], (RELAPSE_TWO, "trickster.ever"), forbids=(COMMITTED, DECLINED, AFTERTASTE, CHAPLAIN, FAILED), delay=72, chapters=(5,))

session(T + "prescription_again", "The next one's yours", 5, '"Is the offer still open?"', [
    nar("start", '''{n}You find her where she said the next one would be yours to find her: on the smithy roof at sundown, with the cat asleep against her hip and her wings folded round both of them against the wind. She watches you climb up the woodpile and over the eaves with frank professional interest, and does not help.{/n}''',
        c("Continue", "roof")),
    a("roof", '''"You climb like a bear." {n}She makes room on the ridge. The cat does not.{/n} "I've been sitting here every evening since the wall, you know. I told myself it was for the cat."
{n}She waits. She has decided, you realise, not to make it easy, and not to make it hard either. She has simply left the space open, the way you would leave a door ajar.{/n}''',
        c('[Ask her] "Will you have me? Both of you, and whatever I am."', "yes", flags=(COMMITTED,)),
        c('[Tell her no, properly this time, and climb down]', "no", flags=(CLOSED,))),
    a("yes", '''{n}She doesn't answer at once. She looks at the city, and the cat, and her own hands, as if checking them all off a list.{/n}
"Yes. Obviously, yes. I asked you first; I was only waiting to see if you'd ever get round to it." {n}Then the composure goes all at once and she is laughing and crying and the cat is complaining and she is holding your sleeve.{/n} "You asked me. On a roof. With a cat. Nobody in the Upper City would believe a word of it."''', c()),
    a("no", '''"Properly this time." {n}She nods, and strokes the cat, and does not look up.{/n} "Thank you for climbing up to say it. That was a real thing to do. Mind the loose slate on the way down."''', c()),
], (DECLINED, RELAPSE_TWO, "trickster.ever"), forbids=(COMMITTED, AFTERTASTE, CHAPLAIN, FAILED), delay=48, chapters=(5,))


# --- The night (Chapter 5, after any redeemed yes): the bell tower under Desna's stars (heat to the cut) -------------

session(NIGHT, "Under the Tender of Dreams", 5, '"Where are we going?"', [
    a("start", '''"Up." {n}It is she who asks, in the end, and she asks with her wings.{/n} "Hold on to me. Not like that; like you mean it. I've never carried anyone anywhere they wanted to go."''',
        c("Continue", "tower")),
    nar("tower", '''{n}Drezen falls away under you. The lamps, the wall, the long dark scar of the siege lines. She sets you down at the top of the old bell tower above the citadel, where the bells were melted for arrows years ago and nothing is left but a ring of broken stone open to the sky. The stars are very close. Desna's stars; the ones travellers steer by.{/n}
"I come here to be where she can see me," she says. "I don't pray. I just sit where she can see."''',
        c("Continue", "flowers", requires=(ELYSIUM,)),
        c("Continue", "stars", forbids=(ELYSIUM,))),
    a("flowers", '''{n}She has brought one of the white flowers from the study, the ones she says came from Elysium, and she tucks it into a crack in the stone.{/n}
"Your cure hasn't got anything to cure any more. Have you noticed? Since the flowers, my touch doesn't take." {n}She laughs, a little helplessly.{/n} "All those candles. All that reading. And there's nothing left in me to take the cold out of you." {n}She sounds almost cheated.{/n} "Desna help me. I don't know what I'm for, if I'm not dangerous."''',
        c("Continue", "undress")),
    a("stars", '''"I know every way there is. I was taught in the Upper City, by the best, on a thousand guests." {n}She is standing with her back to the stars, and her hands have found each other behind her back again.{/n} "And every one of those ways ends with me counting what I took. I'm afraid that halfway through I'll start counting. I'm afraid I'll be good at this, the way I was good at it then." {n}She swallows.{/n} "So I brought us somewhere I've never done anything at all. Nothing here remembers me being good at it."''',
        c("Continue", "cure", requires=(CURE,)),
        c("Continue", "uncured", forbids=(CURE,))),
    nar("cure", '''{n}You lit the star-candle in a niche of the broken bell-wall before she carried you up; it will take one drain, once, until you sleep. Her first kiss is careful, almost a question, and the cold comes with it like a tide coming in, and the little flame in the niche takes it and goes out.{/n}
{n}The rest is hers to take, and yours to pay, and you both know it. She kisses you again anyway, and you let it cost what it costs, and she watches your face the whole time, counting.{/n}''',
        c("Continue", "undress")),
    nar("uncured", '''{n}Her first kiss is careful, almost a question, and the cold comes with it, and there is nothing you can do about it except not pull away. She feels it take you, and stops, and you pull her back.{/n}
"You'll be weak tomorrow," she says against your mouth. "You'll be grey and useless and the second company will talk." {n}You tell her to let them. She makes a sound you have never heard her make, and does.{/n}''',
        c("Continue", "undress")),
    nar("undress", '''{n}She knows how to undress a person. She was taught in the Upper City, and the teaching is the worst thing in her. Her hands begin that way, quick and certain, and then she hears how quietly the buckles are coming loose, the way they did for the guests who did not wake, and she stops. When she begins again she is slow, and clumsy, and has to try your belt twice, and she does not let herself get better at it. Her wings unfold and curve round you both against the wind off the Worldwound; she apologises for them; you tell her not to.{/n}
{n}She lays you down on her cloak on the old bell-floor, under the whole wheel of the stars, and follows you down, her hair falling round both your faces, her skin cool and then not cool at all. She settles astride your hips, braces one hand on the stone beside your head, and draws one long breath that she does not need.{/n}''',
        c("[Let her.]", "morning_after")),
    a("morning_after", '''{n}Much later, she lies with her head on your chest, listening to your heart with the concentration of someone taking a pulse, while the stars turn overhead.{/n}
"Still beating." {n}She sounds amazed.{/n} "Still going. I'm lying here, and you're still here, and nobody is any less than they were." {n}She presses her ear closer.{/n} "Don't talk. I'm taking notes. Desna's watching. Let her."''',
        c("[Let her listen.]", flags=(NIGHT,))),
], (COMMITTED, "trickster.ever"), forbids=(NIGHT,), delay=24, chapters=(5,))


# --- The morning after: first light on the tower -----------------------------------------------------------------

session(MORNING, "Case notes, continued", 5, '"Good morning, doctor."', [
    a("start", '''{n}The first light comes up grey over the Worldwound. She is sitting cross-legged on the broken stone with the daybook, writing, her wings folded over you like a second blanket. She has put on your shirt, which she wears as if she stole it on purpose, which she did.{/n}
"Don't look. I'm writing up the procedure." {n}She shields the page with her hand.{/n} "It's very technical. There are a great many underlinings. I've drawn a diagram and then crossed it out because it was indecent, and then I drew it again because it was accurate."''',
        c("Continue", "count")),
    a("count", '''{n}She sets the book down.{/n} "I counted. Last night. Out of habit. How much I took, how much you gave, how much came back." {n}She looks at you.{/n}
"It came out even. In my whole life, nothing has ever come out even. Nobody at the table was the one being eaten." {n}Her voice wobbles.{/n} "I'm going to keep that page. I'm going to keep it until the paper falls apart, and then I'm going to remember it."''',
        c('"Put it in the case notes: patient recovering."', "recovering", flags=(MORNING,)),
        c('"Put it in the case notes: doctor recovering."', "doctor", flags=(MORNING,))),
    a("recovering", '''"Recovering." {n}She writes it, and then underlines it twice.{/n} "Not cured. I'm never going to be cured. The hunger's not a disease, it's what I'm made of, and you're a quack." {n}She leans over to kiss your forehead, quickly, lightly, a tax she has decided she can afford.{/n} "But recovering. I'll take recovering. I'll take it every morning, if you'll write it."''', c()),
    a("doctor", '''{n}She laughs so hard she drops the pen, and it rolls to the edge of the tower and over.{/n} "The doctor! Look at you. You're grey. You look like a Kenabres widow." {n}She writes it anyway, with a stick of charcoal from her pocket.{/n}
"Doctor recovering. Patient smug." {n}She kisses your forehead, quickly, lightly.{/n} "Stay here till the sun's up. That's a prescription. I've decided I'm allowed to write them too, now. I'll fly you down when you can stand."''', c()),
], (NIGHT, "trickster.ever"), forbids=(MORNING,), delay=6, chapters=(5,))


def integrate(payload):
    """The treatment adds only scenes; its keys bind on demand through trickster_world."""
