"""Arueshalae, the living courtship: "The treatment" (Trickster path; arueshalae.md F18, the sneaky quack).

A Trickster Commander decides that a succubus's hunger is a medical condition and appoints themself her physician.
Every session is on her own companion hub (her unit is in the party), from Chapter 3 to Chapter 5, and every one of them
turns on something canon says about her: she watches mortals to understand them (hub Cue_0048ad6e, "I'm watching... I'm
trying to understand what they truly are"); "Any caress, of any kind, sucks the life from mortals" (Cue_0083 0cb8bb69);
she wants to kiss someone "only as a mortal. Not as a demon" (dfe62398); she grew up in Lady Vellexia's house in
Alushinyrra (f5160086); Nocticula told her to her face that she follows the Commander only by the queen's leave
(Nocticula_main/Cue_0523 b84ef61b).

Device redesign (2026-10-01, Option A): the quack's protection is a real spell, not a trick. Death Ward 0413915f makes its
subject "immune to energy drain" (enGB 952800ab); the Commander finds it in the shrine library (Lore (Religion); the
Trickster's own Lore (Religion) rank 1, TricksterLoreReligionTier1Feature 04177c4d, read as trickster.religion_tier1,
only lowers the DC) and buys it as a Scroll of Death Ward 89e10c3f from the scroll merchants (native Chapter 3 and 5 vendor
tables). Each protected touch spends one scroll (RemoveItemFromPlayer, gated on arueshalae.ward_held); with no scroll
there is no touch, and the scene says why. The ward lasts minutes (caster level 7), and the scenes are timed to it. That
her caress is "energy drain" is the Commander's inference from the crusade's primer, labelled as such on the page. Her
native romance runs beside all of this and is never started, completed or contradicted; where it has already happened
(the Ch4 dream, the release from the Abyss) the sessions read it.
"""
from story_format import c, n, scene
from storylines.arueshalae_trickster import (AFTERTASTE, CHAPLAIN, CLAIMED, CLOSED, COMMITTED, DEAD, DECLINED, EVIL_DEAD,
                                             FAILED, HUB, RECRUITED, REFUSED, RETIRED_TEXT, RETURNED, SAINT_ONLY, SCROLL,
                                             STARTED, UNIT, WARD_HELD)

SCENES = []
T = "arueshalae.treatment."
CURE = "trickster.religion_tier1"          # MainCharacterFacts: the chosen Lore (Religion) rank 1 (lowers the reading's DC only)
LAB = "arueshalae.lab_seen"                # SelectedAnswers After_Lab/Answer_0022 (the supportive answer), variant read
DREAM = "arueshalae.dream_woken"           # SelectedAnswers Nightmares/Answer_0006 (the dream kiss itself), variant read
ELYSIUM = "arueshalae.changed"             # Derived (Q11): native redemption seen (Q3/BackToReality Cue_0018) or the Ch5 best ending

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
CURED = T + "cure_works"                   # the ward has been proven on her hand at the procedure (no longer a lore trick)
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
DREZEN_AREA = "2570015799edf594daf2f076f2f975d8"   # DrezenCapital: the tower above the citadel
# PP2 early beat (arueshalae_early, the Chapter 2 prison; path-neutral), read in "Night reading" only.
EARLY_KEPT = "arueshalae.early.desna.kept"
EARLY_DOUBTED = "arueshalae.early.desna.doubted"
EARLY_PLAIN = "arueshalae.early.desna.plain"

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
    a("start", '''"I watch everyone. You know that." {n}She is standing at your elbow, looking at the books you have not put away, all borrowed from the shrine: a Desnan breviary with a cracked spine, open at the blessing for travellers; the crusade's drill-primer on demons, open at the succubus; and a chaplain's handbook of wards, open at a page with a skull drawn in the margin.{/n}
"My goddess's mercy. My own kind, in a sergeant's handwriting. And the wards the priests lay against death." {n}Her voice changes.{/n} "Why are you reading all three of those at the second bell, Commander?"''',
        c("Continue", "why", forbids=(EARLY_KEPT, EARLY_DOUBTED, EARLY_PLAIN)),
        c("Continue", "prison_kept", requires=(EARLY_KEPT,)),
        c("Continue", "prison_doubted", requires=(EARLY_DOUBTED,), forbids=(EARLY_KEPT,)),
        c("Continue", "prison_plain", requires=(EARLY_PLAIN,), forbids=(EARLY_KEPT, EARLY_DOUBTED))),
    a("prison_kept", '''{n}She touches the open page, the travellers' blessing, without quite letting her finger rest on it.{/n} "You made me a prayer like this through the bars in Drezen, in your own words. A star, a road, one night." {n}She takes her hand back.{/n} "And now you've found the priests' version, and you're reading it at the second bell as if you meant to find something in it that isn't there. I'm afraid to ask what."''',
        c("Continue", "why")),
    a("prison_doubted", '''"In the cells under Drezen you promised me her pardon, and I told you that was the Dawnflower's promise, not hers." {n}A small, wry tilt of her head toward the breviary.{/n} "You've been doing your reading since. I can see the page from here. It's the right goddess, this time."''',
        c("Continue", "why")),
    a("prison_plain", '''"In the cells under Drezen you told me you didn't know the first thing about her, and that my warning wasn't enough. You didn't pretend it was." {n}She looks at the three books, all open at the same page.{/n} "You know something about her now. Why?"''',
        c("Continue", "why")),
    nar("why", '''{n}You lay the books side by side. Desna's blessing promises nothing about demons. The crusade's primer calls a succubus's touch a drain. The chaplain's handbook offers protection against energy drain: Death Ward. None of the three mentions the other two.{/n}
{n}The ward cannot mend what has already been drained. A Scroll of Death Ward from Drezen's market costs as much as a good horse, lasts seven minutes, and is spent in one reading. The shrine's chaplain will read it over whoever brings it. When it runs out, you will need another.{/n}
{n}She bends over the books. Your calculation of the price per minute is still wet in the margin. Whether the handbook's ward will stop what her skin takes remains a guess.{/n}''',
        c('[Lay the books side by side; the lore you chose on the Trickster\'s road tells you where to look] "The primer names it. The handbook stops it."',
          requires=(CURE,), check={"Skill": "SkillLoreReligion", "DC": 10, "Success": "fit", "Failure": "not_yet"}),
        c('[Work it out the hard way, from the handbook and the primer]', forbids=(CURE,),
          check={"Skill": "SkillLoreReligion", "DC": 15, "Success": "fit", "Failure": "not_yet"})),
    a("fit", '''{n}She reads over your shoulder for a long time, her lips moving on the handbook's dry chaplain's phrases.{/n}
"Immune to energy drain." {n}She sounds as though she is afraid to breathe on it.{/n} "Not a cure. A ward you buy by the scroll, and it's gone before a candle's burned down a finger." {n}Her finger stops on your margin note, where you have worked the price out per minute.{/n} "You've written it down as if it were a dosage. You've worked out what it costs to hold my hand." {n}She straightens, and then does not seem to know what to do with her hands.{/n} "I don't trust it. Nobody's ever offered me something so small and so dear at the same time. I keep looking for the hook. And you haven't even tried it yet; you only think my touch is what that sergeant meant."''',
        c("[Close the books.]", flags=(STUDIED,))),
    a("not_yet", '''{n}She watches you turn back three pages, then five, then the whole handbook, and lose the thread each time.{/n}
"You'll get there," {n}she says.{/n} "Or you won't, and you'll have burned a lot of the shrine's lamp oil on a demon." {n}She almost smiles.{/n} "Come back to it. I'll be here. I'm always watching."''', c(abort=True)),
], ("trickster",), forbids=(STUDIED,), chapters=(3, 5), Areas=[DREZEN_AREA])   # the shrine library


# --- Intake (Chapter 3): the pulse ----------------------------------------------------------------------------------

session(INTAKE, "Intake", 3, '[Hold out your hand, palm up] "You look pale. Let me take your pulse. When did you last eat?"', [
    nar("start", '''{n}She looks at your open hand the way a cat looks at a hand held out to it: as a question, and possibly a trap.{/n}
"You know what touching me costs." {n}It is not a warning so much as a fact she has been asked to confirm.{/n} "In the Abyss I learned to look for what a held-out hand wants. What do you want?" {n}You tell her: her pulse. Only that. She considers it for a long breath, tilting her head, interested in spite of herself. Then she pulls her sleeve down over her hand, all the way to the knuckles, and lays her wrist in your palm, cuff and all, lightly, ready to take it back.{/n}
{n}Her pulse, through the cloth, if a succubus has a pulse, is slow and faint and far too even, like a clock somebody forgot to wind. She watches your fingers on her sleeve, and then your face, and her ruby eyes are enormous.{/n}''',
        c("Continue", "laugh")),
    a("laugh", '''"When did I last..." {n}A laugh startles out of her, and she clamps her free hand over her mouth, appalled at herself.{/n} "Commander, I don't eat. Not the way you mean. I can taste your bread and your wine, and they are lovely, and they are like... like looking at a painting of a fire when you're cold."
{n}She tries to take her wrist back. You don't let her, yet.{/n} "I'm taking it back now. You shouldn't hold on so long. The cloth slips. If it slips, you won't feel what it costs you until it's already gone."''',
        c('"Answer the question. When did you last eat?"', "answer"),
        c('[Let go] "Sorry. Occupational habit."', "released")),
    a("released", '''{n}You open your hand. She takes her wrist back at once and holds it against her chest, and for a moment neither of you says anything.{/n}
"Thank you." {n}She sounds surprised to be saying it. Then she looks at your empty palm, still held out, and something in her face argues with itself and loses.{/n} "No. Here. Finish counting. You let go when I asked, so you can have it for as long as it takes to count." {n}She tugs the cuff straight and lays her wrist back in your hand herself, and this time she does not watch your fingers. She watches you.{/n}''',
        c("[Count, and nothing more.]", "answer")),
    a("answer", '''{n}She rubs the place where your fingers were, through the sleeve, as if it were her skin that had been hurt.{/n}
"Properly? Before the goddess. Before Desna caught me in the priestess's dream and made me look at what I was." {n}Her voice drops.{/n} "Since then I don't touch anyone. I keep my hands behind my back in a crowd, and when somebody brushes against me anyway I feel the edge of them go, a little, and I walk away fast. I tell myself every day that I'm not hungry, and every day it's a lie."''',
        c("Continue", "diagnosis")),
    nar("diagnosis", '''{n}You make the face that the Kenabres field surgeons made when they had bad news and no time: a short nod, a click of the tongue, a hand on the hip.{/n}
"Starvation," {n}you tell her.{/n} "I'd write it on the chart, if you had a chart."
{n}Her mouth twists.{/n} "Starvation. That's a mortal word. You starve because there's no bread. I'm not short of bread, Commander. I'm surrounded by it every hour, and it talks to me, and thanks me for my prayers." {n}She looks at the hand that held her wrist.{/n} "I'll tell you what it is. I want to be touched and not count what I took. I want to kiss someone the way a mortal does, and have them still there afterwards. Once. That's the whole illness."
"Then I've spent three nights in the shrine library finding out what that would take," {n}you tell her.{/n} "Somebody has to be the doctor. I've read the texts. I'm the nearest thing you've got."''',
        c("Continue", "her")),
    a("her", '''{n}For a moment you think you have hurt her. Then she sits down, very suddenly, on an ammunition crate, and laughs until she has to wipe her eyes on her sleeve, and the laugh is the most unguarded sound you have ever heard her make.{/n}
"A doctor. For a succubus. Oh, gods, they'd hang you in Alushinyrra, and then they'd hire you." {n}She sobers, a little.{/n} "You should know before you start that if this goes wrong, it won't be the patient on the floor. It'll be the doctor. So don't lose the doctor, doctor." {n}She says it lightly, and it is not light.{/n} "Very well. What do you prescribe? I warn you, any physician in Alushinyrra would have reached for chains."''',
        c('"Watch people eat. Three times a day. Take notes."', "watch", flags=(INTAKE, RX_WATCH, STARTED)),
        c('"Every day, tell me one thing you want that isn\'t a person."', "want", flags=(INTAKE, RX_WANT, STARTED)),
        c('"Actually, I\'ll need a second visit to decide. Doctors always do."', abort=True)),
    a("watch", '''"Watch people eat." {n}She says it slowly, testing it for the trick.{/n} "I already watch them. I watch them all the time, it's what I do instead of... I've told you. Watching them is how I learn what they are."
"Not like this, though. Not on purpose, three times a day, as medicine." {n}She almost smiles.{/n} "All right. I'll take notes. You'll regret asking to read them."''', c()),
    a("want", '''"One thing I want that isn't a person." {n}She looks genuinely frightened, which you did not expect.{/n} "I don't know if I have any. That's the whole... that's the problem, Commander. I used to turn every want I had toward someone I could have."
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
    a("want", '''"I kept the list. Number one: nothing. I told you I would come and say so, and then I didn't, because I was ashamed. Number two: I want the cat that sleeps on the smithy roof to like me. It doesn't. Number three: I want the smell of the bakery on Tanner's Row at dawn. Not the bread. The smell."
{n}She turns a page, and her cheeks colour.{/n} "Number four I've crossed out. Number five: I want to know what the Kenabres refugees sing when they're mending nets. They stop when I come close."''',
        c("Continue", "evening")),
    a("evening", '''"And then, in the evening, I sat at the back of Fye's, where nobody looks, and I watched them eat together, and talk with their mouths full, and pass bread with their dirty hands, and I realised something." {n}She closes the book.{/n}
"I know how a table works. I've sat at more of them than you have, and watched what everyone wanted. And then a pikeman with no teeth pushed his bread across to a stranger and didn't look up to see what he'd bought with it. Nothing. He bought nothing. I watched him for an hour, waiting for the price." {n}She looks at you with something almost like accusation.{/n} "Why do you call it a treatment? What's getting treated?"''',
        c('"You\'re getting better. That\'s what treatment is for."', "better", flags=(MEALTIMES, SAID_BETTER)),
        c('"Because I\'m a quack, and quacks need patients."', "quack", flags=(MEALTIMES, SAID_QUACK))),
    a("better", '''"Better." {n}She says the word as if it were in a language she had studied but never heard spoken.{/n} "I wish I knew what Desna saw in me. I used to think my kind only ever got killed." {n}She tucks the book into her belt.{/n} "But you've written it down now. So I suppose it's official. The Commander of the crusade says I'm getting better." {n}A pause.{/n} "Don't tell anyone. They'll want a second opinion."''', c()),
    a("quack", '''{n}She laughs, the startled laugh again, and this time she doesn't cover it.{/n} "A quack. Yes. That's much more honest." {n}She tucks the book into her belt.{/n}
"You know what's strange? I trust that more. The priests sound so certain when they talk about mercy. You're the first one who's admitted they're making it up." {n}She considers.{/n} "I'll keep taking the medicine, quack. But I want it noted that I'm doing it out of spite."''', c()),
], (INTAKE, "trickster.ever"), forbids=(MEALTIMES,), delay=24, chapters=(3, 5))   # Drezen-set: not in the Abyss (R2-5)


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
"He's alive. I went back to look. He was laughing with his friends. I stopped before it was more than a breath, and I don't know what a breath of me costs a man, and I can never ask him." {n}She lifts her chin, bracing for the verdict.{/n} "So. Desna's priests would give me a road to walk and a star to walk it by. What do you give me?"''',
        c('"Next time, come to me. Whatever hour. I\'ll be the one who notices first."', "come", flags=(RELAPSE, COME_TO_ME)),
        c('"Then stay out of Fye\'s for a while. Out of taverns, out of crowds."', "stay_out", flags=(RELAPSE, STAY_OUT)),
        c('[Straight-faced] "I\'ll tell the sergeant he was blessed by a Desnan saint in disguise. He\'ll dine out on it for years."',
          "saint_story", flags=(RELAPSE, SERGEANT_STORY))),
    a("come", '''"Come to you." {n}She says it as if you had told her to walk into a fire to warm up.{/n} "Commander, you are the last person I should come to when I'm hungry. You're the one I..." {n}She stops herself.{/n}
"No. I understand. You'd rather I came to you than to a stranger. Because you know what I am, and he didn't." {n}Something in her face eases, and something else tightens.{/n} "All right. I'll come to you. And you'll send me away. Promise me you'll send me away."''', c()),
    a("stay_out", '''"Out of taverns." {n}She nods too quickly.{/n} "Yes. That's sensible. That's what a real doctor would say." {n}She is quiet for a moment.{/n}
"The only thing is... that's where they are. The mortals. That's where they laugh and sing and hold each other's hands. If I stay out of the places where they're happy, I'll learn everything about them except the one thing I want to understand." {n}She squares her shoulders.{/n} "But I'll do it. For a while. I've walked worse roads in worse company."''', c()),
    a("saint_story", '''{n}She opens her mouth to protest, and nothing comes out. Then she laughs, helplessly, and slides down the stable wall until she is sitting in the straw.{/n}
"A saint. In disguise." {n}She is laughing and crying at the same time.{/n} "You're horrible. Tender of Dreams forgive me, you're horrible. I nearly ate a man and you're going to tell him he was blessed." {n}She wipes her face.{/n} "He'll believe you. That's the worst of it. He'll light a candle at the shrine every week for the rest of his life, and I'll have to walk past it."''', c()),
], (MEALTIMES, "trickster.ever"), forbids=(RELAPSE,), delay=48, chapters=(3, 5))   # Drezen-set: not in the Abyss (R2-5)


# --- The touch: the quack's cure ---------------------------------------------------------------------------------

session(TOUCHED, "The procedure", 3, '"I want to try something. Give me your hand."', [
    a("start", '''{n}She puts both hands behind her back at once, the old habit of a woman who puts her hands away before a temptation can find them.{/n}
"No. You know I can't. You know what happens." {n}She eyes your outstretched hand as if it were a drawn sword.{/n} "Any caress, Commander. Any caress of any kind. That's not a manner of speaking. It's what I am."''',
        c("Continue", "dream", requires=(DREAM,)),
        c("Continue", "explain", forbids=(DREAM,))),
    a("dream", '''"I know what you're thinking. In the dream you bent down to kiss me, where it couldn't have hurt you, and I screamed and threw you off." {n}Her cheeks go dark.{/n} "I've been ashamed of that every day since. That was the one place in all the worlds where my kiss isn't death, and I still couldn't bear it. Out here I'm still what I was built to be. I won't risk you out here."''',
        c("Continue", "explain")),
    nar("explain", '''"It's a procedure," {n}you tell her.{/n} "The ward from the handbook, read over me. While it holds, your hand takes nothing. That's what the books say. Tonight we find out whether the books know what you are."
{n}She searches your face for the joke. For once, you aren't making one. It frightens her more than the hand does.{/n}
"And if they don't? If it doesn't hold?"
"Then I'll have spent a fortune to learn something, and so will you. That's what procedures are for."''',
        c('[Light the star-candle, say the travellers\' blessing, then hold out your hand] "One star, one night."', "cure_try",
          requires=(CURE,), forbids=(CURE,), mythic="Trickster"),   # retired 2026-10-01 (no lore trick protects her)
        c('[Light the star-candle and say the blessing from the chaplain\'s commentary, word for word]', requires=(CURE,),
          forbids=(CURE,), check={"Skill": "SkillLoreReligion", "DC": 20, "Success": "cure_try", "Failure": "pay_try"}),   # retired
        c('"You\'re right. Not yet."', abort=True),
        c('[Spend a Scroll of Death Ward: have the shrine\'s chaplain read it over you, then hold out your hand] "Seven minutes. Let\'s not waste them."',
          "ward_try", requires=(WARD_HELD,), remove_item=SCROLL),
        c("[Not yet: there is no ward read on you.]", "no_scroll")),
    nar("ward_try", '''{n}You walk her across the yard to the chapel. The shrine's chaplain breaks the seal for you at the altar rail and reads the scroll over you, every word, without asking why, and you feel it settle on your skin like a coat of cold water, and then like nothing at all. The parchment goes to ash in his fingers. She watches it fall from the doorway, and does not come in.{/n}
{n}Then she takes your hand. Her fingers are cool and very light. You wait for the draught under the door, the cold in the middle of you that every soldier in the crusade has heard about. It does not come. She is waiting for it too; you can see her waiting, braced, the way a woman braces on ice.{/n}''',
        c("Continue", "cured")),
    a("cured", '''{n}She is staring at your joined hands. She has stopped breathing, if she breathes.{/n}
"Nothing." {n}Her voice is tiny.{/n} "It isn't taking anything. Commander, it isn't taking anything." {n}Her thumb moves, once, over your knuckles, testing.{/n} "I can feel your pulse. I can feel it, and I'm not... It's only a pulse."
"Seven minutes," {n}you tell her.{/n} "Then the ward's spent, and so is the scroll. Every time, a new one. That's the treatment."
{n}She holds on while you count. At the sixth minute she lets go herself, carefully, before the ward can let go of you, and holds the hand you held against her chest, and begins to cry, silently.{/n} "I've never held anyone's hand before without killing a little of them. Not once." {n}A wet, startled laugh.{/n} "Seven minutes, at the price of a horse. Gods help your purse, doctor. I'll take it."''',
        c("[Keep your hand where she can see it.]", flags=(TOUCHED, CURED))),
    nar("no_scroll", '''{n}She looks at your bare hand, and then at your face, and sees the answer before you give it; she sees everything before you do.{/n}
"No ward." {n}She puts her hands behind her back, quite gently, the way she puts them away in a crowd.{/n} "Then no hand. Not tonight, and not on a promise. Buy it, and have it read, and come back, and I'll be braver than this. I swear by the road I will."''',
        c("[Go and find the scroll-sellers.]", abort=True)),
    nar("cure_try", RETIRED_TEXT, c("Continue", "cured")),   # retired with its answers (2026-10-01): the candle and the lore
    nar("pay_try", RETIRED_TEXT, c("Continue", "paid")),   # retired with its answer (2026-10-01): no unwarded touch
    a("paid", RETIRED_TEXT, c("[Catch your breath.]", flags=(TOUCHED, DRAINED))),
], (RELAPSE, "trickster.ever"), forbids=(TOUCHED,), delay=48, chapters=(3, 5), Areas=[DREZEN_AREA])   # the shrine and its yard


# --- Alushinyrra (Chapters 4-5): the house she grew up in ---------------------------------------------------------

session(ALUSHINYRRA, "Where I grew up", 4, '"Tell me about the house you grew up in."', [
    a("start", '''{n}She is quiet for so long you think she will not answer. In the Abyss she rests less and watches more. Even here, she keeps one eye on the dark beyond the camp.{/n}
"Lady Vellexia's house. In Alushinyrra." {n}She hugs her knees.{/n} "It was beautiful. Everything in it was beautiful. The guests were beautiful, until they weren't. When I see a long table now, I remember them around hers, trying so hard to amuse her."''',
        c("Continue", "table")),
    a("table", '''"That's what I remember about meals. The long table, the candles, the silver. The guests in their best clothes, trying so hard to entertain her. And the food on the plates, which nobody touched, because the food was never the point. That's how I remember it, anyway: everyone waiting to see which of them she would keep."
{n}She looks at you.{/n} "At a mortal table I still wait for someone to die. They pass the bread, and I watch the hands. I know what a hand across a table used to mean."''',
        c("Continue", "question")),
    nar("question", '''{n}You ask her the only question a doctor could ask: if she could eat anything, anything at all, a meal that would really feed her and cost nobody, what would it be?{/n}
{n}She thinks about it for a long time. She takes it seriously, the way she takes all your prescriptions seriously, even the ones that are jokes.{/n}''',
        c("Continue", "meal")),
    a("meal", '''"A meal someone made for me." {n}She says it so quietly you almost miss it, and then she flushes, as if she had said something indecent.{/n}
"Not bought. Not stolen. Not... served, the way Lady Vellexia served. Made. By someone who didn't know how to cook, who got it wrong, and gave it to me anyway because they wanted me to have it." {n}She laughs at herself.{/n} "That's ridiculous. It wouldn't feed me. I'd taste it and it would be a painting of a fire again. But I'd eat every crumb."''',
        c('"Noted. That\'s going in the treatment plan."', "noted", flags=(ALUSHINYRRA, WANTS_MEAL)),
        c('''"That's not ridiculous. You want someone to give you something."''', "first",
          flags=(ALUSHINYRRA, WANTS_MEAL))),
    a("noted", '''"The treatment plan." {n}She rests her chin on her knees and smiles at the dark.{/n} "You haven't got a treatment plan. You've got a pocket full of jokes and a very straight face." {n}A pause.{/n} "Write it down anyway. I want to see what it looks like in your handwriting."''', c()),
    a("first", '''{n}She goes still.{/n} "They could burn it, and I'd still want it." {n}She presses her hand to her mouth.{/n} "I want to sit beside them while they eat theirs."
"I'm going to cry in the Abyss, in front of the whole camp, and it's your fault."''', c()),
], (INTAKE, "trickster.ever"), forbids=(ALUSHINYRRA,), delay=24, chapters=(4,))

# Q11: the telling is staged in the Abyss, so it stays in Chapter 4; a Chapter 5 player who missed it hears it in Drezen.
import copy as _copy
_twin = _copy.deepcopy(SCENES[-1])
_twin.update(Id=T + "alushinyrra_drezen", MinChapter=5, MaxChapter=5, Chapters=[5])
_twin["Forbids"] = _twin["Forbids"] + [T + "alushinyrra_drezen"]
for _node in _twin["Nodes"]:
    _node["Text"] = (_node["Text"]
        .replace('''In the Abyss she rests less and watches more. Even here, she keeps one eye on the dark beyond the camp.''',
                 '''Since the Abyss she rests less and watches more. Even here, her gaze keeps straying to the dark beyond the torchlight.''')
        .replace('''I'm going to cry in the Abyss, in front of the whole camp, and it's your fault.''',
                 '''I'm going to cry on the citadel wall, in front of the whole watch, and it's your fault.'''))
SCENES.append(_twin)


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
], (CLAIMED, INTAKE, "trickster.ever"), forbids=(QUEEN,), delay=24, chapters=(4,), optional=True)   # Sol r1 CAN: told in the Isles


# --- The kitchen (Chapter 5): the meal someone made -----------------------------------------------------------------

KITCHEN_OPEN = '''{n}You requisition the officers' kitchen in the citadel for an evening, which the cook allows only after you promise not to touch the good knives. You touch the good knives. You burn the onions. You make something that is meant to be a Mendevian farmhouse stew and is, generously, brown.{/n}
{n}She comes in because you sent a page with a note that said only "Doctor's orders. Seventh bell. Kitchens." She stops in the doorway and looks at the table, at the two bowls, the heel of bread, the wine you have not stolen, and her hand goes to her mouth.{/n}'''
session(KITCHEN, "A meal someone made", 5, '"Seventh bell. You said kitchens."', [
    nar("start", KITCHEN_OPEN, c("Continue", "sit")),
    a("sit", '''"You remembered." {n}She sits down as if the bench might give way under her.{/n} "I told you once, and I thought you'd forgotten it."
{n}She picks up the spoon. She eats. She eats slowly, all of it, every burnt piece of onion, and you can see on her face that it is exactly what she said it would be: a painting of a fire. She eats it anyway, as if it were a fire.{/n}''',
        c("Continue", "taste")),
    a("taste", '''"It's terrible." {n}She wipes the bowl with the bread.{/n} "It's truly terrible, Commander. In Lady Vellexia's house the cook who sent this up would have spent the night waiting to be sent for." {n}She puts the bread in her mouth, and chews, and swallows, and her eyes are wet.{/n}
"It's the best thing anyone has ever given me. And it didn't feed me at all. And I'm not hungry. How am I not hungry?"''',
        c("[Spend a Scroll of Death Ward: slip across the yard and have the chaplain read it over you while she wipes the bowl]", "hand_cure",
          requires=(WARD_HELD,), remove_item=SCROLL),
        c("[Keep your hands on the table.]", "hand_paid")),
    nar("hand_cure", '''{n}You are back from the chapel before the bowl is dry, with the ward cold on your skin, and she knows the look of you now; she puts the bowl down. Then she reaches across the table and takes your hand, the one with the onion burn on the knuckle, and turns it over, and presses her lips to the burn.{/n}
{n}Nothing comes out of you. Nothing at all. She lifts her mouth away slowly, deliberately, watching your face over your knuckles, and then she does it again, because she can.{/n}
"Still working," {n}she says.{/n} "Seven minutes, and the walk across the yard had two of them. I counted. Good."''',
        c("Continue", "after")),
    nar("hand_paid", '''{n}She reaches across the table for your hand, the one with the onion burn on the knuckle, and stops an inch short of it. She knows the sound of a seal breaking by now, and she has not heard one tonight.{/n}
{n}She bends her head instead and kisses the air above the burn, so close that you feel her breath on it and nothing else.{/n}
"One," {n}she says, shakily.{/n} "For the cook. That's all I'm allowed tonight, and I've never meant one more. Don't you dare laugh."''',
        c("Continue", "after")),
    a("after", '''{n}She stays until the candles are low, helping you wash the bowls in a basin of cold water with the concentration of someone performing surgery.{/n}
"I've been asking what I dream of. Since the goddess. I still don't know." {n}She dries the last bowl.{/n} "But I think I know what I want to remember, when I'm very old, if demons get old. I want to remember that somebody burned the onions for me."''',
        c("[Leave the bowls to dry.]", flags=(KITCHEN,))),
], (TOUCHED, ALUSHINYRRA, "trickster.ever"), forbids=(KITCHEN,), delay=48, chapters=(5,), Areas=[DREZEN_AREA])   # the citadel kitchens


# --- The second relapse (Chapter 5): wanting the wrong thing ------------------------------------------------------

session(RELAPSE_TWO, "Contraindications", 5, '''"You look as though you haven't rested."''', [
    a("start", '''"I don't need sleep. I do need my thoughts to leave me alone for a while. They haven't." {n}She sits on the edge of her bedroll, the daybook open on her knees. The page is blank.{/n}
"I have to tell you something. You're not going to like it, and I'm not going to be able to say it twice."''',
        c("Continue", "want")),
    a("want", '''"Since the kitchens, since your hand... I've started to watch the ward the wrong way. Not you. It. I count the minutes the way you taught me, and somewhere about the fifth I start wanting the seventh. I want it to run out while I'm still holding on. I want the moment when it stops being safe." {n}She is gripping the book so hard the cover bends.{/n}
"I lie here and I count the hours until I can see you, and I don't know if I'm counting them because I love your company or because I'm hungry and you're the only food in all the world I'm allowed near. I can't tell the difference any more. I used to be able to tell. That was the one thing I was proud of."''',
        c("Continue", "ask")),
    a("ask", '''{n}She closes the book.{/n} "So I want to stop. The treatment. The hand. Just for a while. I want to go back to crumbs and see whether I still want to see you when there's nothing in it for the hunger."
{n}She looks at you, defiant and terrified.{/n} "Or you can tell me that's stupid, and that I'm being dramatic, and that you know what you're doing. You usually do. Even when you're joking."''',
        c('"Then we stop. A week. No hands. I\'ll still come and see you."', "fast", flags=(RELAPSE_TWO, FAST)),
        c('"No. You\'re not a danger to me. We keep going."', "no_fast", flags=(RELAPSE_TWO, NO_FAST)),
        c('"You\'re the patient. You decide. I\'ll follow the prescription you write."', "her_call",
          flags=(RELAPSE_TWO, HER_CALL))),
    a("fast", '''"A week." {n}She nods, and nods again.{/n} "And you'll still come. Even when there's nothing to give me." {n}She tries to smile.{/n} "Come anyway. I want to hear you laugh, even if I keep my hands to myself the whole week." {n}She tries to smile.{/n} "And if I'm not glad to see you by the seventh day, you'll know what I am before I do."''', c()),
    a("no_fast", '''"You're very sure." {n}She studies your face, the way she studies strangers in the market.{/n} "That's what frightens me. You're very sure, and you've never been a succubus, and I have." {n}She closes her eyes.{/n}
"All right. We keep going. But if I ever take more than you mean to give, you tell me. At once. Out loud. Don't be kind about it. Kindness is how they die."''', c()),
    a("her_call", '''{n}She stares at you. Then she gets up, crosses the room, and bends to your ear, and says a word into it that is not Arueshalae: a name made of sounds a throat was not built for, that stings the ear like smoke.{/n}
"That's what they called me, before. It isn't magic. It's just the name of the thing I was." {n}She straightens, very pale.{/n} "If I ever start to take more than you're giving, say it. I'll hear it. I swear by the road I'll stop when I hear it." {n}She sits back down on the bedroll, shaking.{/n} "I've never given it to anyone. Don't lose it. Don't ever use it for anything else."''', c()),
], (KITCHEN, SLIPPED, "trickster.ever"), forbids=(RELAPSE_TWO,), delay=48, chapters=(5,))


# --- The rite slips (Chapter 5): the cost, and her distance ---------------------------------------------------------

session(SLIPPED, "A missed night", 5, '"You\'re awake. Don\'t get up."', [
    nar("start", '''{n}The march back from the last sortie ran late, and you fell asleep in your boots with the scroll case still buckled to your belt, unopened. You remember her coming to the tent to see that you had eaten. You remember reaching for her, half-asleep, your bare hand an inch from the back of her neck, and her not pulling away at once.{/n}
{n}Then you remember your own name, very loud, and the tent floor coming up to meet you where she threw you clear. Your shoulder aches from the landing. Her skin never touched yours; she made sure of that, with an inch to spare. She was not in the tent.{/n}''',
        c("Continue", "her", requires=(CURED,)),
        c("Continue", "her_paid", forbids=(CURED,))),
    a("her_paid", '''{n}You find her at first light in the far corner of the baggage lines, as far from your tent as the pickets allow, with her knees drawn up and her wings wrapped round them. Her face is grey.{/n}
"We never found anything that works. We've been touching anyway, and I told myself we were being careful." {n}Her voice is very flat.{/n} "You reached for me and I was hungry and I leaned into it for a breath, and another, before I threw you off."''',
        c("Continue", "distance_paid")),
    a("distance_paid", '''"So I've moved my bedroll. To the chapel crypt, in Drezen. Here, to the baggage lines." {n}She has plainly rehearsed this.{/n} "Somewhere I can't reach you in the night. Either you find a ward that holds, or we stop touching, or you come to me awake and knowing, every time. I won't be the thing that takes you in your sleep."''',
        c('"Then I\'ll find a ward that holds, or I won\'t touch you. I swear it on the road."', "vow", flags=(SLIPPED, DRAINED, VOW_RITE)),
        c('''"Rest where you like. I'll come to you awake, and knowing, every time."''', "come", flags=(SLIPPED, DRAINED, CANDLE_BEARER)),
        c('"You\'re right. Keep your distance for a while. I\'ll earn it back."', "earn", flags=(SLIPPED, DRAINED, DISTANCE_KEPT))),
    a("her", '''{n}You find her at first light in the far corner of the baggage lines, as far from your tent as the pickets allow, with her knees drawn up and her wings wrapped round them. Her face is grey. You have seen that look on the faces of the soldiers who dug out Kenabres.{/n}
"No ward on you. The case was on your belt, still sealed, and you were asleep, and you reached for me, and for one breath I leaned into it. One breath. Two." {n}Her voice is very flat.{/n} "Then I threw you across the tent. I did stop, before your hand landed. And I was sorry I'd stopped, all the way across the tent, and I'm still sorry, sitting here. That's the part I can't carry." {n}She looks at the shoulder you landed on, and away.{/n}''',
        c("Continue", "distance")),
    a("distance", '''"So I've moved my bedroll. To the chapel crypt, in Drezen. Here, to the baggage lines." {n}She has plainly rehearsed this.{/n} "Somewhere I can't reach you in the night. Not until I can trust you to be awake, with the ward read, every single time, march or no march. I won't be the thing you forget about."''',
        c('"Then I\'ll never touch you again without the ward read. I swear it on the road."', "vow", flags=(SLIPPED, DRAINED, VOW_RITE)),
        c('''"Rest where you like. I'll come to you awake, with the ward read, every time."''', "come", flags=(SLIPPED, DRAINED, CANDLE_BEARER)),
        c('"You\'re right. Keep your distance for a while. I\'ll earn it back."', "earn", flags=(SLIPPED, DRAINED, DISTANCE_KEPT))),
    a("vow", '''"On the road." {n}She looks at you for a long time over her knees.{/n} "Desnans don't swear on the road lightly. Travellers die on it." {n}She does not move from the corner.{/n} "Then I'll come back to the tent when I've watched you keep it for a week. Not before."''', c()),
    a("come", '''{n}She laughs, once, badly.{/n} "You'd walk down to a crypt every night with a scroll in your hand, to a demon who nearly ate you." {n}She hugs her knees tighter.{/n} "Yes. Come. Knock first. And if you ever come with the seal still whole, I'll know, and I'll be on the other side of the crypt before you can argue."''', c()),
    a("earn", '''"Earn it back." {n}She nods, and nods again, and her eyes are wet.{/n} "I'll be in the chapel. I can't bear to sit beside you tonight." {n}She gets up, and stops at the tent flap.{/n} "When you come, come with the ward already on you. I want to hear the seal go before I see your face."''', c()),
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
    a("no_fast", '"At the procedure I let go at six. I remember being sorry there was still a minute left." {n}She keeps her hands behind her back.{/n} "You told me we\'d keep going. I still want to. But if I ever start taking more, you must tell me. That part hasn\'t changed."',
        c("Continue", "list", requires=(FORTY,)),
        c("Continue", "risk", forbids=(FORTY,))),
    a("her_call", '"You have my old name. I gave it to you myself." {n}She works a loose thread out of her cuff.{/n} "I still dread needing to hear it. And I still want you here. I can\'t promise there will never be a bad night. Only that I\'ll listen when you call me back. Keep it for that. Nothing else."',
        c("Continue", "list", requires=(FORTY,)),
        c("Continue", "risk", forbids=(FORTY,))),
    a("list", '''"You wanted to know what number forty was, on the list. The one I kept back." {n}She doesn't take it out. She knows it by heart.{/n}
"'Number forty: I want to ask the Commander something, and I want to be the one who asks, for once in my life, instead of the one who's asked.'" {n}She swallows.{/n} "So. That's what this is. I'm doing number forty."''',
        c("Continue", "risk")),
    a("risk", '''"But first you have to hear the thing I'm most afraid of, because I won't ask with it hidden." {n}She does not look at you.{/n} "One night there'll be no scroll in your satchel, or the minutes will run out while neither of us is counting. A march, a siege, a night you forget. I'll be hungry, and you'll be asleep, and I won't stop in time. Not stiff fingers. The rest of you." {n}Her voice drops.{/n} "What happens then?"''',
        c('"Then I\'ll wake, and run, and not come back till you send for me."', "ask"),
        c('"Then I\'ll have known the price every night and paid it. That\'s mine to decide, not yours."', "ask"),
        c('''"On those nights, I'll sleep in another room. That's the rule."''', "ask")),
    a("ask", '''{n}She brings her hands out from behind her back. They are empty. She holds them out to you, palms up, not touching, an inch away.{/n}
"I'm not going to test you. I've tested everyone I ever met and it never once made me happy. I'm just going to ask." {n}Her voice goes very small and very steady.{/n} "Will you have me? I want you. Desna forgive me, I've been trying to say it all evening."''',
        c('"Yes. Both of you."', "both", flags=(COMMITTED,)),
        c('"Yes. But keep the hunger out of my sight."', "saint", flags=(SAINT_ONLY, DECLINED)),
        c('''"Not yet. I need time to think."''', "not_yet", flags=(DECLINED,)),
        c('"No."', "neither", flags=(CLOSED, REFUSED))),
    a("both", '''{n}She closes the inch, and stops with her fingers on your cuff, on the cloth, and holds that instead, and does not seem to know what to do with it now she has it.{/n} "Both." {n}She says it again, as if checking it for a trick.{/n} "Both. I... I had something to say after that. I had a whole... it's gone." {n}Her grip tightens on the cloth.{/n} "I want you so much right now it frightens me. And it's me wanting. There's nobody else in here to blame it on." {n}She laughs, very softly, and it shakes, and she does not let go.{/n} "Don't say anything. I'll get it wrong again. Just stay where you are."''', c()),
    a("saint", '''"Only the parts of me that pray, then." {n}She nods, and something shutters in her face, smoothly, the way it must have in Lady Vellexia's house when a guest said the wrong thing.{/n}
"Out of your sight." {n}She looks down at her hands as if they had done something without her.{/n} "Every single day I keep it down, Commander. For the soldiers at the rail, and the novice who sweeps, and the cat. I thought that with you, just with you, I might stop holding my breath." {n}Her voice goes so soft you barely hear it.{/n} "I can't say yes to that. You'd be kissing a woman with her hand over her own mouth. Desna forgive me, I'd rather you didn't kiss me at all."''', c()),
    a("not_yet", '''{n}She lets her hands fall. She does not look hurt; she looks like someone recalculating a route.{/n} "Not yet." {n}She nods.{/n} "All right. I've waited longer for smaller things." {n}A small, crooked smile.{/n} "But I asked first. That's done. That can't be taken back. The next one's yours."''', c()),
    nar("neither", '''{n}She puts her hands behind her back again, very carefully, as if putting something away in a drawer. Then she goes down the steps and into the city, and the lamps come on behind her one by one.{/n}''', c()),
], (RELAPSE_TWO, "trickster.ever"), forbids=(COMMITTED, DECLINED, AFTERTASTE, CHAPLAIN, FAILED), delay=168, chapters=(5,),
    Areas=[DREZEN_AREA])   # the fast's seven days; the citadel wall

session(T + "prescription_again", "The next one's yours", 5, '"Is the offer still open?"', [
    nar("start", "{n}You find her on the smithy roof at sundown, watching Drezen's sentries light their lamps. A cat sleeps against her hip. She watches you climb over the eaves and shifts her wings to leave room beside her.{/n}",
        c("Continue", "roof")),
    a("roof", '''"You climb like a bear." {n}She makes room on the ridge. The cat does not.{/n} "I've been sitting here every evening since the wall, you know. I told myself it was for the cat."
{n}She waits. She has decided, you realise, not to make it easy, and not to make it hard either. She has simply left the space open, the way you would leave a door ajar.{/n}''',
        c('[Ask her] "Will you have me? Both of you, and whatever I am."', "yes", flags=(COMMITTED,)),
        c('[Tell her no, properly this time, and climb down]', "no", flags=(CLOSED, REFUSED))),
    a("yes", '''{n}She doesn't answer at once. She looks at the city, and the cat, and her own hands, as if checking them all off a list.{/n}
"Yes. Obviously, yes. I asked you first; I was only waiting to see if you'd ever get round to it." {n}Then the composure goes all at once and she is laughing and crying and the cat is complaining and she is holding your sleeve.{/n} "You asked me. On a roof. With a cat. Nobody in the Upper City would believe a word of it."''', c()),
    a("no", '''"Properly this time." {n}She nods, and strokes the cat, and does not look up.{/n} "Thank you for telling me yourself. Mind the loose slate on the way down."''', c()),
], (DECLINED, RELAPSE_TWO, "trickster.ever"), forbids=(COMMITTED, AFTERTASTE, CHAPLAIN, FAILED), delay=48, chapters=(5,),
    Areas=[DREZEN_AREA])   # the smithy roof


# --- The night (Chapter 5, after any redeemed yes): the bell tower under Desna's stars (heat to the cut) -------------

session(NIGHT, "Under the Tender of Dreams", 5, '"Where are we going?"', [
    a("start", '''"Up." {n}It is she who asks, in the end, and she asks with her wings.{/n} "Hold on to me. Not like that; like you mean it. I used to carry people where I wanted them. Tell me if this is where you want to be."''',
        c("[Spend a Scroll of Death Ward: have the chaplain read it over you at the foot of the tower stair]", "stair",
          requires=(WARD_HELD,), forbids=(ELYSIUM,), remove_item=SCROLL),
        # 2026-10-01: no scroll, no touch. Released from the Abyss she needs none (her touch no longer drains).
        c("Continue", "tower", requires=(ELYSIUM,)),
        c("[Tell her there is no ward on you tonight.]", "no_ward", forbids=(ELYSIUM,))),
    nar("stair", '''{n}You make her wait at the foot of the old bell tower while the shrine's chaplain comes down the lane with his lantern, breaks the seal and reads the ward over you by its light. He does not ask what it is for. He looks at her once, and at you, and goes back to his bed. The ward settles on your skin like cold water, and then like nothing. She has already started counting under her breath.{/n}''',
        c("Continue", "tower", flags=(T + "night.warded",))),
    a("no_ward", '''{n}Her hands are on your belt, ready to lift, when you tell her. She stops, and looks at your bare wrist, where the chaplain's ink would be.{/n}
"There's no ward in there." {n}She lets go of you, finger by finger.{/n} "Not tonight, then. I won't take you up a tower and spend the whole night counting what I've taken. I've done that, before the goddess. I won't do it to you." {n}She touches your cheek through a fold of her cloak, the only way she trusts herself to.{/n} "Buy it, and have it read. I'll still be here. I'll still want to go."''',
        c("[Go and find the scroll-sellers.]", abort=True)),
    nar("tower", '''{n}Drezen falls away under you. The lamps, the wall, the long dark scar of the siege lines. She sets you down at the top of the old bell tower above the citadel, where the bells were melted for arrows years ago and nothing is left but a ring of broken stone open to the sky. The stars are very close. Desna's stars; the ones travellers steer by.{/n}
"I come here to be where she can see me," {n}she says.{/n} "I don't pray. I just sit where she can see."''',
        c("Continue", "flowers", requires=(ELYSIUM,)),
        c("Continue", "stars", forbids=(ELYSIUM,))),
    a("flowers", '''{n}She turns her bare hands over in the starlight.{/n} "Since the Abyss let go of me, my touch doesn't take. I know that. I keep expecting to feel you grow cold anyway." {n}She laughs unsteadily.{/n} "I used to know exactly what my hands would do. Now I don't know where to put them."''',
        c("Continue", "undress")),
    a("stars", '"I used to bring people somewhere they couldn\'t leave." {n}She glances at the stair opening, then back at you.{/n} "I come here alone. Tonight I wanted you to see it. I wanted you here with me." {n}Her fingers catch your cuff.{/n} "I\'m wasting the minutes talking. Kiss me."',
        c("Continue", "cure", requires=(CURE,), forbids=(CURE,)),   # retired 2026-10-01 (the lore protects nothing)
        c("Continue", "uncured", requires=(CURE, CURED), forbids=(CURE, CURED)),   # retired 2026-10-01 (no unwarded night)
        c("[Take the scroll case out of your coat and break the seal]", "cure", requires=(WARD_HELD, CURE), forbids=(CURE,),
          remove_item=SCROLL),   # retired (2026-10-01): the ward is read at the foot of the stair, before the flight
        c("Continue", "cure", requires=(T + "night.warded",))),
    nar("cure", '''{n}The ward the chaplain read at the foot of the stair is on you still: cold water, and then nothing. The flight took one of its seven minutes. She does not need to be told how many are left. She has been counting under her breath since the lantern went back down the lane.{/n}
{n}Her first kiss is careful, almost a question, and nothing comes out of you with it. Nothing at all. She makes a sound against your mouth that you have never heard from her, half a laugh and half something with no name in Taldane, and kisses you again, and this time it is not a question.{/n}''',
        c("Continue", "undress")),
    nar("uncured", RETIRED_TEXT, c("Continue", "undress")),   # retired with its answer (2026-10-01)
    nar("undress", '{n}Her fingers slip under your collar. She opens the buckles with quick, certain hands, then fumbles your belt and laughs against your mouth. Her wings curve around you against the wind off the Worldwound.{/n}\n{n}She spreads her cloak on the bell-floor and draws you down. When you answer her kiss she grips your shoulder harder. Her hair falls across your face; she pushes it aside impatiently and settles over you, one hand braced beside your head.{/n} "I want you." {n}It comes out rough, loud enough to carry down the stair. She stays close, watching your face.{/n} "Look at me. Here. With you."',
        c("Continue", "morning_after", requires=(ELYSIUM,)),
        c("Continue", "morning_after_paid", forbids=(ELYSIUM,))),
    a("morning_after", '{n}Later she lies with her ear against your chest. The stars turn above the broken tower, and a watchman\'s lantern moves along the wall below.{/n} "Still beating." {n}She lifts her head and kisses you again.{/n} "I can do that whenever I want now. I keep forgetting. Stay here while I remember."',
        c("[Let her listen.]", flags=(NIGHT,))),
    a("morning_after_paid", '{n}She has drawn her cloak between your bodies. Her ear rests on your chest through the cloth; your heart beats under it.{/n} "I stopped before it ended. I wanted another kiss, and I stopped." {n}Her fingers grip a fold of the cloak.{/n} "Don\'t go yet. The ward\'s gone. I can still have you here."',
        c("[Let her listen.]", flags=(NIGHT,))),
], (COMMITTED, "trickster.ever"), forbids=(NIGHT,), delay=24, chapters=(5,), Areas=[DREZEN_AREA])   # PP2 post-cap: the citadel tower


# --- The morning after: first light on the tower -----------------------------------------------------------------

session(MORNING, "Case notes, continued", 5, '"Good morning, doctor."', [
    a("start", '''{n}The first light comes up grey over the Worldwound. She is sitting cross-legged on the broken stone with the daybook, writing, one wing folded over the cloak you are wrapped in like a second blanket. She has put on your shirt, which she wears as if she stole it on purpose, which she did.{/n}
"Don't look. I'm writing up the procedure." {n}She shields the page with her hand.{/n} "It's very technical. There are a great many underlinings. I've drawn a diagram and then crossed it out because it was indecent, and then I drew it again because it was accurate."''',
        c("Continue", "count", forbids=(ELYSIUM,)),
        c("Continue", "count_e", requires=(ELYSIUM,))),
    a("count", '"I counted last night. The flight, the kisses, where I stopped." {n}Her wing settles over your wrapped shoulders.{/n} "You\'ll be yawning at council. That\'s the tower\'s fault. And mine. I took nothing." {n}She smiles shakily.{/n} "I want to remember how you stayed afterwards."',
        c('"Put it in the case notes: patient recovering."', "recovering", flags=(MORNING,)),
        c('"Put it in the case notes: doctor recovering."', "doctor", flags=(MORNING,))),
    a("recovering", '''"Recovering." {n}She writes it, and then underlines it twice.{/n} "Not cured. I'm never going to be cured. The hunger's not a disease, it's what I'm made of, and you're a quack." {n}She leans over and kisses your brow through a fold of the cloak, quickly, lightly.{/n} "But recovering. I'll take recovering. I'll take it every morning, if you'll write it."''', c()),
    a("doctor", '''{n}She laughs so hard she drops the pen, and it rolls to the edge of the tower and over.{/n} "The doctor! Look at you. You're yawning. You look like a sentry after a double watch." {n}She writes it anyway, with a stick of charcoal from her pocket.{/n}
"Doctor recovering. Patient smug." {n}She kisses your brow through a fold of the cloak, quickly, lightly.{/n} "Stay here till the sun's up. That's a prescription. I've decided I'm allowed to write them too, now. I'll fly you down when you can stand."''', c()),
    # After the native Elysium ending her touch no longer drains (BestEnding cues 0c5b3449, f3f59947): nothing was taken.
    a("count_e", '"I kept expecting the cold to start in you." {n}She lays her palm flat over your heart.{/n} "It never did. I was awake beside you when the watch changed, and I wanted to wake you for another kiss." {n}She leans forward.{/n} "Now you\'re awake."',
        c('"Put it in the case notes: patient recovering."', "recovering_e", flags=(MORNING,)),
        c('"Put it in the case notes: doctor recovering."', "doctor_e", flags=(MORNING,))),
    a("recovering_e", '''"Recovering." {n}She writes it, and looks at the word, and crosses it out.{/n} "No. I don't know what this is. The Abyss let go of me, and the hunger went quiet, and I keep listening for it the way you listen for a dog that's stopped barking." {n}She leans over and kisses your mouth, slowly, for no reason at all, and does not count.{/n} "Write 'under observation.' I'm going to watch it for a long time before I believe it."''', c()),
    a("doctor_e", '''{n}She looks you over, frankly, from your hair to your bare feet.{/n} "The doctor isn't recovering from anything. The doctor's pink. The doctor slept like a baby on a bell-floor, and I lay awake all night beside a warm mortal and didn't take one thing." {n}She writes it anyway.{/n}
"Doctor: insufferable. Patient: frightened of how good this is." {n}She kisses your forehead and then, because she can, your mouth.{/n} "Stay till the sun's up. Doctor's orders. Mine."''', c()),
], (NIGHT, "trickster.ever"), forbids=(MORNING,), delay=6, chapters=(5,), Areas=[DREZEN_AREA])   # PP2 post-cap: first light on the tower


# Q11: after the native Elysium ending (BestEnding cues 0c5b3449, f3f59947: her touch no longer drains) every session
# that stages a drain closes; the night and the morning carry Elysium variants; the discharge offers the yes instead.
for _scene in SCENES:
    if _scene["Id"] not in (NIGHT, MORNING) and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)

DISCHARGED = T + "discharged"
session(DISCHARGED, "Discharged", 5, '"You look different. You keep touching things."', [
    a("start", '''"I do, don't I?" {n}She is sitting on the edge of her bedroll with her bare hands in her lap, turning them over, as if they belonged to someone she had just been introduced to.{/n} "The Abyss let go of me, and since then I've touched the quartermaster, a horse, three novices and the cat. On purpose. Nobody went grey. Nobody even noticed."
{n}She looks up at you, and laughs, and it shakes.{/n} "You've lost your only patient, doctor. There's nothing left in me for your scrolls to ward you from."''',
        c("Continue", "ask")),
    a("ask", '''"So I'm going to do the thing on my list I was keeping for when I was cured, because I'm not going to get a better day for it." {n}She stands, and takes your hand, and holds it, and nothing happens except that she holds it.{/n} "Will you have me? Not your patient. Me. The one who's left."''',
        c('"Yes."', "yes", flags=(COMMITTED,)),
        c('"Not yet."', "later", abort=True),
        c('"No."', "no", flags=(CLOSED, REFUSED))),
    a("yes", '''{n}She does not let go of your hand. She puts her other hand flat on your chest, over your heart, and keeps it there, and waits, and the heart goes on beating under it.{/n} "Still there," {n}she says.{/n} "Still there. Desna help me, I'm never going to get used to that."''', c()),
    a("later", '''"Not yet." {n}She squeezes your hand, hard, because she can.{/n} "All right. I've got a great deal of time now, and two hands to fill it. Ask me again when you've worked out what you're waiting for."''', c(abort=True)),
    a("no", '''{n}She lets go of your hand. She looks at her own for a moment, as if surprised it still works.{/n} "Then I'll go and touch something else," {n}she says, and does not cry until she is out of the tent.{/n}''', c()),
], (INTAKE, ELYSIUM, "trickster.ever"), forbids=(COMMITTED, AFTERTASTE, CHAPLAIN, FAILED, DISCHARGED), delay=24,
    chapters=(5,))

# Sol r1 (INT, 2026-10-01): an Arueshalae released from the Abyss before the Commander ever opened the treatment still has
# a way in. Positive evidence only: her release (arueshalae.changed: BackToReality Cue_0018 / Cue_0025, or BestEnding).
FREED = T + "freed_hands"
session(FREED, "Bare hands", 5, '"You keep looking at your hands."', [
    a("start", '''{n}She is turning her bare hands over in the lamplight as if they belonged to someone she had just been introduced to.{/n}
"I do, don't I. You were there when the Abyss let go of me; you heard me say it. I'm not a monster any more." {n}She laughs, unsteadily.{/n} "I keep waiting for somebody to tell me it was a trick. This morning I touched the quartermaster's sleeve, and then his hand, on purpose, and nothing happened to him at all except that he went red and dropped his ledger."''',
        c("Continue", "ask")),
    a("ask", '''"I've been saving something. A thing I wanted to do on the day it was safe, when I didn't believe there would ever be such a day." {n}She holds out her hand, palm up, the way a person offers a hand to be taken, and waits, and does not take it back.{/n} "Take it. And then tell me whether you'd take the rest of me."''',
        c('[Take her hand] "All of you."', "yes", flags=(FREED, COMMITTED)),
        c('"Not yet."', "later", abort=True),
        c('"No."', "no", flags=(FREED, CLOSED, REFUSED))),
    a("yes", '''{n}She closes her fingers on yours and holds on, and nothing happens, except that she holds on.{/n} "Warm," {n}she says, surprised.{/n} "You're warm. I never noticed. I never dared stay long enough to notice." {n}She does not let go.{/n} "All of me. I'll hold you to that. I'll hold you to it with both hands, now I can."''', c()),
    a("later", '''"Not yet." {n}She curls her fingers closed and puts the hand away, but not behind her back.{/n} "All right. I've a great deal of time now, and two hands to fill it. I'll ask again."''', c(abort=True)),
    a("no", '''{n}She lets her hand fall. She looks at it for a moment, as if surprised it still works.{/n} "Then I'll go and hold somebody else's," {n}she says, quite steadily, and does not cry until she is out of the lamplight.{/n}''', c()),
], ("trickster", "trickster.ever", ELYSIUM), forbids=(INTAKE, COMMITTED, AFTERTASTE, CHAPLAIN, FAILED, FREED), delay=24,
    chapters=(5,))


def integrate(payload):
    """The treatment adds only scenes; its keys bind on demand through trickster_world. Q11: her changed state reads both the
    native redemption (BackToReality/Cue_0018 6b24754f: "The Abyss has relinquished its hold on me. I... I am not a monster
    anymore!", key 7b75d992-a3eb-4608-85fe-f6d6b3350dc6) and the later best-ending dialogue."""
    from storylines import trickster_world as _tw
    kind, guid, _ = _tw.BINDINGS["arueshalae.elysium"]
    value = [guid] if kind in _tw.LIST_KINDS else guid
    if (payload.get(kind) or {}).get("arueshalae.elysium") not in (None, value):
        raise ValueError("Conflicting binding: arueshalae.elysium")
    payload.setdefault(kind, {})["arueshalae.elysium"] = value
    # PP2 (Sol r2, INT): BackToReality has two release cues: Cue_0018 6b24754f, and the romance branch's Cue_0025 8ad7c2ba
    # ("Freedom. Finally... the Abyss has released me from its clutches... I am not a monster anymore!").
    payload.setdefault("SeenCues", {})["arueshalae.back_to_reality"] = ["6b24754fcea768342a30a1e18ce91b92",
                                                                        "8ad7c2ba0e060e545b12269cc5ced777"]
    payload.setdefault("Derived", {})[ELYSIUM] = [["arueshalae.elysium"], ["arueshalae.back_to_reality"]]
