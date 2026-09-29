"""Arueshalae, the treatment's other sessions and the life after the yes (Trickster path; arueshalae.md F18).

Canon touched here (blueprints.zip / enGB, hub CompanionDialogues/Arueshalae): she studies mortals the way a scholar
studies a text ("They love cats!", 98597b65, said as if sharing a scientific discovery); "You mortals aren't liars.
You're dreamers" (5ae7fdea); her last victim was a priestess of Desna, who died "of my kiss" (6f76ee9e, 0ab59621); in
the Abyss she dreads meeting "old acquaintances" at the Ten Thousand Delights (BestEnding 3edf6ac1 recalls it); "You
cannot have dreams without nightmares" is a line the Commander can say to her in her final dream (Q3/FinalDream).
Authored and labelled: the smithy cat, the net-menders' song, the temple letter, the dance, the race.
"""
from story_format import c, n, p, reaction, scene
from storylines.arueshalae_trickster import (CLOSED, COMMITTED, DEAD, EVIL_DEAD, HUB, LANN_HUB, RETURNED, SAINT_ONLY,
                                             SOSIEL_HUB, UNIT, RECRUITED)
from storylines.arueshalae_treatment import (SERGEANT_STORY, COME_TO_ME, CURE, CURED, DRAINED, ELYSIUM, INTAKE, KITCHEN, MEALTIMES,
                                             MORNING, NIGHT, RELAPSE, RX_WANT, RX_WATCH, T, TOUCHED)

SCENES = []
CAT = T + "the_cat"
SONG = T + "the_song"
PRIESTESS = T + "the_priestess"
CARRY = T + "carries_her"
WRITE = T + "writes_the_temple"
TEMPLE_LETTER = T + "temple_letter"
OLD_NAME = T + "old_name"
WOUND = T + "the_wound"
DANCE = T + "the_dance"
AFTER_WAR = T + "after_the_war"
RACE = T + "the_race"
NIGHTMARE = T + "nightmare"
EVE = T + "the_eve"
GUARD = (CLOSED, DEAD, EVIL_DEAD, RECRUITED)
BACK = dict(ForbidOverrides={DEAD: RETURNED})


def a(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Arueshalae", **kw)


def session(id, title, chapter, entry, nodes, requires, forbids=(), delay=0, last=5, chapters=None, optional=True, **extra):
    SCENES.append(scene(id, title, "Arueshalae", chapter, entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(*GUARD, id, *forbids), delay=delay, last=last, optional=optional,
                        Relationship="arueshalae", AnswerLists=[HUB], ContactUnit=UNIT,
                        Chapters=list(chapters or range(chapter, last + 1)), **{**BACK, **extra}))


# --- The cat on the smithy roof ---------------------------------------------------------------------------------

session(CAT, "Field observations", 3, '"You look pleased with yourself."', [
    a("start", '''{n}She has straw in her hair and a long red scratch across the back of one hand, and she is so happy she is almost vibrating.{/n}
"The cat. The one on the smithy roof. It came to me." {n}She says it the way you would announce the fall of a fortress.{/n} "I've been trying for weeks. I've been sitting under that roof every morning, being very still and very uninteresting, and it just looked at me. They know, you see. Animals always know what we are."''',
        c("Continue", "want", requires=(RX_WANT,)),
        c("Continue", "watch", forbids=(RX_WANT,))),
    a("want", '''"It was on my list. Day two. I want the cat to like me. I told you, and I was ashamed of it, because it's such a small, stupid thing to want." {n}She turns the scratched hand over, admiring the scratch.{/n} "And then this morning I stopped trying. I just sat there and thought about the bakery on Tanner's Row, and the refugees, and your burnt onions, and it came down and sat on my knee as if I were furniture."''',
        c("Continue", "science")),
    a("watch", '''"I only noticed it because of your prescription. I was watching the smiths eat their bread at the forge door, and there it was on the roof, watching them too. Two of us, taking notes." {n}She turns the scratched hand over, admiring the scratch.{/n} "And this morning it came down and sat on my knee as if I were furniture. I didn't do anything. I think that's why."''',
        c("Continue", "science")),
    a("science", '''{n}She lowers her voice, very serious, as if sharing a scientific discovery.{/n} "Then it scratched me and ran off. I think that means it likes me. I asked the smith's apprentice and she said that's how cats say it. Mortals love cats, you know. I've been studying it. It's one of the few things I'm sure of."
{n}She holds the scratch up for you to see.{/n} "It bled. It healed. Nothing was taken. It's the first time something has hurt me for a reason that wasn't hunger."''',
        c('"Congratulations. The patient has a pet."', "pet"),
        c('"I\'m going to need to examine that scratch. Very thoroughly."', "examine")),
    a("pet", '''"It isn't mine. Nobody owns a cat. That's the other thing I've learned about mortals: they love the things they can't own, and they're very happy about it, and they complain about it all the time." {n}She beams.{/n} "I'm going to buy it a fish."''',
        c("[Let her go and buy it a fish.]", flags=(CAT,))),
    a("examine", '''{n}She laughs and hides the hand behind her back.{/n} "You are the worst doctor in the Worldwound. The scratch is fine. The scratch is perfect. I'm keeping it until it scars." {n}She pauses.{/n} "Do succubi scar? I don't know. I'll find out. That can go in the notes too."''',
        c("[Let her go and buy it a fish.]", flags=(CAT,))),
], (MEALTIMES,), delay=24, chapters=(3, 4, 5))


# --- The net-menders' song (Drezen: Chapters 3 and 5) ------------------------------------------------------------

session(SONG, "The net-menders", 3, '"They stopped singing again."', [
    a("start", '''{n}She is standing at the corner of the refugee quarter with her arms wrapped round herself, watching the Kenabres women mend nets they will never use on a lake they will never see again. They are singing. As soon as she takes a step closer, they stop.{/n}
"Every time." {n}She doesn't sound angry. She sounds as if she has been handed a verdict.{/n} "I've been coming here every evening. I stay at the corner. I don't go near. And every time I take one step, one, they stop. It's as if the song knows."''',
        c("Continue", "why")),
    a("why", '''"I want to learn it. That's all. It was on my list, the day I crossed the fourth one out." {n}She hugs herself tighter.{/n} "It's about a lake. I've worked out that much from the corner. A lake that holds the moon so still you could fish it out with a net. And the men who went out in the boats and didn't come back, and the women who mended the nets anyway."
"I think it's the most beautiful thing I've ever heard. And I'm the thing that makes them stop."''',
        c('[Walk into the circle and sing the first verse, badly] "Somebody start me off, I only know the tune."', "sing",
          mythic="Trickster"),
        c('[Take her hand and walk her in] "Come on. They stop because they don\'t know you. Let them."', "walk")),
    nar("sing", '''{n}You do not know the words. You sing them anyway, loudly and wrongly, in the voice of a Commander who has shouted orders over three battles. The women stare at you in appalled silence. Then an old woman with a net in her lap begins to laugh, and corrects you, and sings the line properly, and another woman joins her to drown you out, and then they are all singing, at you, to make you stop.{/n}
{n}Arueshalae comes in from the corner under cover of the noise, and sits on an upturned basket at the edge of the circle, and nobody notices. By the third verse she is singing too, very softly, on the tune alone.{/n}''',
        c("Continue", "after")),
    nar("walk", '''{n}She lets you. She walks into the circle behind you like a child being taken to a school it is afraid of. The song stops. The women look at her. You tell them she is the one who warned Kenabres before the attack, the one who was jailed for it; that she has been standing at their corner every night because she wants to learn their song.{/n}
{n}There is a long silence. Then the old woman with a net in her lap shifts over on her bench, just enough, and starts the verse again from the top, slowly, for a beginner.{/n}''',
        c("Continue", "after")),
    a("after", '''{n}Later, walking back through the dark, she hums it under her breath, over and over, as if afraid it will fall out of her.{/n}
"It isn't about the lake at all. It's about mending the nets anyway." {n}She stops in the middle of the street.{/n} "They made room for me on the bench, Commander. They didn't know what I am, or they knew and didn't care, and I don't know which is more frightening. I'm going to go back tomorrow. And the day after. Until I know every verse."''',
        c("[Walk her home.]", flags=(SONG,))),
], (MEALTIMES,), delay=24, chapters=(3, 5))


# --- The priestess she killed ----------------------------------------------------------------------------------

session(PRIESTESS, "The last one", 3, '"You\'ve been reading the Desnan prayer book again."', [
    a("start", '''{n}She has, and she closes it when she sees you, and then, with an effort, opens it again.{/n}
"I want to tell you about her. The priestess. I told you once, when you asked about the goddess, but I told it like a story, the way I tell everything. I want to tell it the way you'd tell a priest, if priests didn't flinch. With the parts that matter." {n}She takes a breath she does not need.{/n} "May I?"''',
        c('"Tell me."', "tell")),
    a("tell", '''"She was a priestess of Desna in a little shrine above a river. I don't remember the town. I never knew her name. I spent a month in her dreams and I never once asked it; it wasn't a thing I needed." {n}Her voice is very steady.{/n}
"I found her through her dreams. I spent a month in them before I went to her in the flesh, so she would already love me when I arrived. That was how I did it. That was how we all did it. She lay in my arms, and she died of my kiss. I remember every smallest detail. The cold sweat. Her weak whisper. And I went into her mind to see what dreaming was, and the goddess was waiting there."''',
        c("Continue", "question")),
    a("question", '''"Everything since has been because of her. The mercy. The memories of the ones I was made from. The years as a spy. This." {n}She gestures at herself, at the crusade, at you.{/n}
"So I want to ask you something. Your treatment, the watching, the list, the hand. Does any of it make up for her? Is that what it's for? Because if it is, I'll do it forever. And if it isn't, I need to know what it's for."''',
        c('"No. Nothing makes up for her. You carry her. That\'s all."', "carry", flags=(PRIESTESS, CARRY)),
        c('"No. But she had a name. Somebody could write to her shrine and ask it."',
          "write", flags=(PRIESTESS, WRITE))),
    a("carry", '''{n}She closes her eyes, and you think you have done her harm. Then she nods.{/n}
"Thank you. Everyone else says something kind. The priests say the goddess has forgiven me, and I think, then the goddess is wrong, and I'm not allowed to think that." {n}She puts her hand flat on the prayer book.{/n} "You carry her. Yes. That's right. I'll carry her, and I'll carry the watching and the list and your terrible onions, all at once. They don't cancel. They just have to fit."''', c()),
    a("write", '''{n}She stares at you as if you had suggested she fly to the moon.{/n} "Write to them. To the Desnans. And say what? 'Dear Mother of the shrine, I am the succubus who killed your priestess, please tell me her name so I can...'" {n}She stops.{/n} "So I can what?"
{n}You tell her: so she can stop calling her "the priestess". So the one person in the world who remembers every smallest detail of her death can remember the one detail that was hers.{/n}
"That's insane," she whispers. "That's the most insane thing you've ever prescribed. I'm going to do it."''', c()),
], (RELAPSE,), delay=24, chapters=(3, 4, 5))

session(TEMPLE_LETTER, "Reply from the river", 5, '"They wrote back."', [
    a("start", '''{n}She has the letter in both hands, and she has been crying, and she has been doing it for some time.{/n}
"The Mother of the shrine wrote back. She knew. She'd always known it was a demon; the goddess told her, in a dream, the night it happened." {n}She holds the letter out, and then pulls it back, as if it might hurt you to read.{/n} "Her name was Ilvanne. Ilvanne. She's buried under the shrine's apple tree, and the tree has done very well." {n}She reads on, and her voice catches.{/n} "The Mother says Ilvanne always wanted to see the sea. She never went. There was always someone who needed her at the shrine."''',
        c("Continue", "sea")),
    a("sea", '''"And she sent this." {n}From the fold of the letter she takes a small flat river stone, grey, with a white band round it.{/n}
"She says: 'The goddess told me the one who took our sister would one day ask where she lies. I have kept this for that day. Take her to the sea, and then you may stop asking.'" {n}Arueshalae turns the stone over and over.{/n} "She knew. For years. She kept a stone for me. Commander, how do mortals do that? How do you keep a stone for the thing that killed your sister?"''',
        c('"I don\'t know. But when the Wound is closed, we\'re going to the sea."', "promise", flags=(TEMPLE_LETTER,)),
        c('"Maybe that\'s what dreaming is."', "dream", flags=(TEMPLE_LETTER,))),
    a("promise", '''"We." {n}She presses the stone to her lips, very lightly, as if it were a person she might drain.{/n} "Yes. When the Wound is closed. I'm going to hold you to that, doctor. I'm going to hold you to it so hard."''', c()),
    a("dream", '''{n}She is quiet for a long time.{/n} "Desna asked me what I dream of. I've never had an answer." {n}She closes her fist round the stone.{/n} "I think I might have part of one now. It's grey, with a white band round it. And it wants to see the sea."''', c()),
], (WRITE,), delay=72, chapters=(5,))


# --- The Abyss (Chapter 4): her old name ------------------------------------------------------------------------

session(OLD_NAME, "What they called me", 5, '"The woman in the Alushinyrra market. Who was she?"', [
    a("start", '''{n}She is sitting with her back to the fire, which she never does, and her wings are wrapped round her like a cloak.{/n}
"Somebody I knew. Somebody from the Ten Thousand Delights. She recognised me across the whole market and she called me by my old name, loud, so everyone would turn, and they all did." {n}She is holding herself very still.{/n} "It isn't Arueshalae. You don't need to know what it is. It's a name that means something you'd do to a person, and it was mine for a very long time."''',
        c("Continue", "offer")),
    a("offer", '''"She asked if I was hungry. She said there was a party in the Upper City and plenty of mortals at it who'd paid to be eaten, and she'd get me in, for old times' sake. She said it kindly. That's the worst of it. In the Delights they say those things kindly."
{n}Her hands are clenched in the fabric of her wings.{/n} "And I was hungry. I am. The Abyss made it worse, Commander. It was like trying not to drink when you're standing in the sea. Some nights it still is, even here. I stood there with her hand on my arm and I thought about saying yes for as long as it takes to say it."''',
        c('"You didn\'t say it."', "didnt"),
        c('[Hold out your hand] "Then take this instead. Right now."', "hand", requires=(TOUCHED,))),
    a("didnt", '''"No. I didn't. I said..." {n}She laughs, cracked.{/n} "I said I was seeing a doctor. She didn't understand. She thought it was a new kind of client."
{n}She finally turns to face the fire, and you.{/n} "But I nearly did. You should know that. Your patient nearly went to a party in the Upper City. You should write it in the notes, with a very black line under it."''', c(flags=(OLD_NAME,))),
    nar("hand", '''{n}She looks at your hand as if it were a door she is not sure she is allowed through. Then she takes it, here in the chapel yard, with the Delights still on her like a smell she cannot wash out, and holds on.{/n}''',
        c("Continue", "held_cure", requires=(CURED,)),
        c("Continue", "held_paid", forbids=(CURED,))),
    a("held_cure", '''{n}You lit the star-candle at dusk. The first cold comes and the rite takes it, and the second you let come, and slowly her shoulders come down from round her ears.{/n}
"That's the difference," she says at last, very quietly. "Her party would have been more. Much more. And I'd have hated myself before dawn. This is less, and I don't." {n}She does not let go.{/n} "Don't tell her about the doctor. She'll want one."''', c(flags=(OLD_NAME,))),
    a("held_paid", '''{n}The cold comes, and you let it, and she feels you let it, and after two breaths she pulls away and holds your hand between her wrists instead, the careful way.{/n}
"Two," she says. "Only two. I could have had a whole party. I'd rather have two of yours." {n}She is shaking.{/n} "If we ever go back down there, don't do that. Everybody in the Abyss can smell it when someone gives."''', c(flags=(OLD_NAME,))),
], (INTAKE,), delay=24, chapters=(5,))


# --- The Commander wounded (Chapter 5): the doctor is the patient ---------------------------------------------

session(WOUND, "The doctor is out", 5, '"You\'re sitting up. Good."', [
    nar("start", '''{n}The wound is not serious, the chaplains say, which is what they say about wounds that nearly were. You are propped up in the field hospital with your side strapped and a taste of healing potion in your mouth like old pennies, and she is sitting on the stool beside the cot where she has been sitting, the orderlies tell you, for eleven hours.{/n}''',
        c("Continue", "helpless")),
    a("helpless", '''"I couldn't do anything." {n}She is holding her own hands in her lap, as if they were a pair of animals that might get loose.{/n} "They carried you in and there was so much of you on the stretcher, and every healer in the tent went to work, and I just stood there. I know a thousand ways to take a life out of someone and not one to put it back."
"Sosiel had to ask me to move. Twice. The second time he took my arm and walked me out, and he was very kind about it, and I wanted to kill him for being able to help."''',
        c("Continue", "stitch")),
    a("stitch", '''{n}She picks up a needle and a reel of gut from the orderly's tray, holding them as if they were contraband.{/n}
"So I asked the surgeon to teach me this. While you were asleep. I practised on a pig's belly from the kitchens." {n}She is blushing furiously.{/n} "It turns out I have very steady hands. It turns out that's what all those centuries were good for. The surgeon says I'm a natural. I didn't tell her why."
"Your stitches are coming loose at the bottom. May I? I won't touch you. Only the thread."''',
        c('"Doctor\'s orders. Go ahead."', "go", flags=(WOUND,)),
        c('[Hold out your bare hand for her to hold, instead] "Stitch later. Sit with me."', "sit", requires=(TOUCHED,),
          flags=(WOUND,))),
    nar("go", '''{n}She does it without once touching your skin, only the thread and the needle and the steel of the forceps, her face an inch from the wound, her breath held. It is the neatest suture you have ever had. She ties it off and cuts it and sits back, and her hands are shaking now that it is done.{/n}
"There," she says. "Now you've got a little bit of me in you that didn't take anything. Just a knot."''', c()),
    a("sit", '''{n}She looks at the hand, and at the strapping on your side, and at the hand again.{/n} "You're hurt. You can't spare it." {n}Then she takes it anyway, lightly, and holds it without holding it, and keeps it for the rest of the night.{/n}
"Doctor's orders," she says, when the orderly comes to shoo her away, and the orderly, to everyone's surprise, goes.''', c()),
], (KITCHEN,), delay=24, chapters=(5,))


# --- The dance (Chapter 5) --------------------------------------------------------------------------------------

session(DANCE, "Recommended exercise", 5, '"There\'s music in the square."', [
    a("start", '''{n}There is. Someone has won something, or thinks they have, and the Drezen square is full of lanterns and bad fiddlers and soldiers dancing with anybody who will have them.{/n}
"I've been watching them from the steps. I've watched mortals dance for years. At weddings, in taverns, in the camps at Kenabres before..." {n}She stops.{/n} "In the Upper City we danced, of course. It was a kind of hunting. Here it seems to be a kind of falling over while holding on to someone."''',
        c('[Hold out your hand] "Recommended exercise. Twice a week."', "dance")),
    nar("dance", '''{n}She takes it before she can think better of it, and you pull her down the steps into the crowd, and for a moment she is rigid with terror in the middle of the square, a demon in a crowd of mortals with her hand in a mortal's hand, everyone within reach.{/n}
{n}Then a fiddler hits a wrong note, and a sergeant treads on your foot, and somebody's child runs between your legs, and she laughs, and the rigidity goes out of her.{/n}''',
        c("Continue", "cure", requires=(CURED,)),
        c("Continue", "glove", forbids=(CURED,))),
    nar("cure", '''{n}You dance badly, and she dances beautifully, and between you it comes out as something the fiddlers can live with. The first cold comes up through your joined hands and the candle you lit at dusk takes it; after that she keeps a hand's breadth of air between your palms, and you dance with that air between you, which the fiddlers think is very courtly.{/n}
"You're counting," she says into your ear. "Not the steps. The other thing." You are. So is she.''',
        c("Continue", "after")),
    nar("glove", '''{n}She has put a glove on, a long silk one from somewhere, and she holds your hand through it, and even so you can feel the faint cold at the edges, the way you feel a draught through a closed shutter. You dance anyway. You dance badly, and she dances beautifully, and nobody in the square notices that the Commander is a little grey by the end of it.{/n}''',
        c("Continue", "after")),
    a("after", '''{n}She pulls you out of the crowd before the last dance, breathless, and leans on the wall of the grain store with her head tipped back to the lanterns.{/n}
"It isn't hunting." {n}She sounds astonished.{/n} "It's just... being in the same place as everyone at once, and nobody's trying to get anything. How did I watch it for years and not see that?" {n}She looks at you.{/n} "Twice a week, you said. I'm going to hold you to it."''',
        c("[Promise twice a week.]", flags=(DANCE,))),
], (TOUCHED,), delay=24, chapters=(5,))


# --- After the yes ---------------------------------------------------------------------------------------------

session(AFTER_WAR, "Prognosis", 5, '"What will you do, after?"', [
    a("start", '''{n}She has clearly been waiting for someone to ask, because she has an answer ready, and she gives it in a rush, as if afraid of losing her nerve.{/n}
"A kitchen. I want a kitchen. Not a big one. With a window, and a table that's too small, and a place on the shelf for the cat's fish. I want to learn to cook, badly, like you, and burn things for somebody, and have them eat it anyway." {n}She stops for breath.{/n} "And the song. I want to know every verse by then. And the stone, the sea. I told you all of it, didn't I? I tell you everything now. It's very inconvenient."''',
        c("Continue", "you")),
    a("you", '''"And you. I want you there, when you're there. I'm not a fool, I know what you are. You'll be off doing impossible things for the rest of your life, and I'll be the one at the window, waiting to find out which ones." {n}She says it lightly, and means it lightly, and her eyes are very steady.{/n}
"I've been in a house with a thousand guests at the table, Commander. The table was never the problem. The empty chair was. So come back to the kitchen. That's all. That's the whole prognosis.''',
        c('"I\'ll come back to the kitchen. Burn something for me."', "burn", flags=(AFTER_WAR,)),
        c('"The prognosis is excellent. Doctor\'s verdict."', "verdict", flags=(AFTER_WAR,))),
    a("burn", '''"Oh, I will." {n}She grins, all teeth, and for a moment she looks exactly like what she is, and it is wonderful.{/n} "I'm going to burn things for you that nobody has ever burned before. I've got centuries of practice at making mortals suffer. It's time it was good for something."''', c()),
    a("verdict", '''"Excellent." {n}She tastes the word.{/n} "Nobody has ever said that about my future. They said 'damned', and 'doomed', and once, in the Delights, 'profitable'." {n}She laughs.{/n} "Excellent. I'll write that in the notes. On the front page. In red."''', c()),
], (MORNING,), delay=24, chapters=(5,))

session(RACE, "A race over the roofs", 5, '"I challenge you."', [
    a("start", '''{n}She is standing on the parapet of the citadel wall in the last of the light, with her wings half open and a look you have seen on soldiers before a charge they expect to win.{/n}
"A race. From here to the smithy roof, where the cat sleeps. You on your feet, me on my wings." {n}She grins.{/n} "I've watched the children do it along the market roofs. They scream the whole way. It looks like the best thing in the world. I want to scream the whole way."''',
        c("Continue", "stakes", requires=(SERGEANT_STORY,)),
        c("Continue", "rules", forbids=(SERGEANT_STORY,))),
    a("stakes", '''"And if I win, you go to the red-bearded sergeant and tell him the saint wasn't a saint. He lit a candle for me again yesterday. I can't bear it." {n}She considers.{/n} "No. Don't. Let him keep his saint. If I win, you carry my notes for a week. If you win..." {n}She shrugs, delighted.{/n} "You won't."''',
        c("Continue", "rules")),
    a("rules", '''"No flying for you, obviously. No walking for me. No tricks." {n}She narrows her eyes.{/n} "I know that face. That's your trick face. I said no tricks."''',
        c('[Race her fair, and lose]', "fair", flags=(RACE,)),
        c('[Agree to "no tricks", then take the shortcut through the chapel bell-rope loft]', "cheat", mythic="Trickster",
          flags=(RACE,))),
    nar("fair", '''{n}You run. She flies. It is not close. You go over the barracks roof and down a drainpipe and across two washing lines and up the woodpile, and she is sitting on the smithy ridge with the cat in her lap long before you get there, screaming with laughter the whole way, exactly as promised.{/n}
"I won! I won by a mile! You fell off a washing line!" {n}She is radiant.{/n} "That was the best thing in the world. The children were right. Do it again tomorrow."''', c()),
    nar("cheat", '''{n}She launches. You do not follow. You go straight down the stair inside the wall, through the chapel, up the bell-rope ladder into the loft, along the beam that runs out over the lane, and drop onto the smithy roof from above, where the cat looks up at you with total contempt. She lands a breath later, and stares.{/n}
"You cheated." {n}She is laughing so hard she has to sit down on the ridge.{/n} "You said no tricks and you cheated and I didn't see how. I was flying over you the whole time." {n}She wipes her eyes.{/n} "Rematch. Tomorrow. And I'm watching the chapel."''', c()),
], (MORNING,), delay=24, chapters=(5,))

session(NIGHTMARE, "The other kind of dream", 5, '"I\'m sorry I woke you."', [
    nar("start", '''{n}She has woken you by screaming, which she has never done, not once in all the months of the crusade. When you get to her she is sitting bolt upright on her bedroll with her wings half open and her nails dug into her own arms.{/n}''',
        c("Continue", "dream")),
    a("dream", '''"I dreamed. I don't dream, Commander. Demons don't. I was so proud, when it started, when the goddess showed me how... and now it's this." {n}She is shaking.{/n}
"It was the priestess. And the sergeant. And everyone. A table, a long table, like Lady Vellexia's, and all of them sitting at it, and me at the head, and they were all very polite and very grey, and nobody would eat." {n}She presses her palms against her eyes.{/n} "They were waiting for me to eat first."''',
        c('"You cannot have dreams without nightmares. They\'re the price of being a person."', "price", flags=(NIGHTMARE,)),
        c('[Sit with her till dawn, and say nothing.]', "sit", flags=(NIGHTMARE,))),
    a("price", '''{n}She lowers her hands and looks at you, and something in her face shifts, as if you had said a word in a language she had been trying to remember.{/n}
"The price of being a person." {n}She breathes out.{/n} "Then I'll pay it. I'll pay it every night. Only... will you be there some of the nights? Not all. I know you can't be there all. Some."''', c()),
    nar("sit", '''{n}You sit on the end of the bedroll with your back against the tent pole, and after a while she leans against your shoulder, not touching skin, only cloth, and after a longer while she falls asleep again. You stay until the window goes grey. She doesn't dream again, or if she does, she doesn't scream.{/n}''', c()),
], (MORNING,), delay=48, chapters=(5,))

session(EVE, "Before Threshold", 5, '"Tomorrow, then."', [
    a("start", '''{n}The camp before the last march is very quiet. Everybody who has anything to say is saying it, in low voices, in the dark, and she has found you on the edge of the lines with a lantern and the daybook, which is nearly full now.{/n}
"I've been reading it back. From the beginning. 'Watch people eat. Three times a day.'" {n}She laughs softly.{/n} "It seems a very long time ago. I was so sure it was a joke."''',
        c("Continue", "fear")),
    a("fear", '''"I'm afraid of tomorrow." {n}She says it simply, as a clinical observation.{/n} "Not of dying. I've died. Of what's at the bottom of the Wound. Of the Abyss seeing me come back and remembering what I am, and calling, and me answering." {n}She closes the book.{/n}
"So I want to ask you something, doctor. If it calls me, tomorrow, and I start to go, what's the treatment?"''',
        c('"Look for me. I\'ll be the one making a bad joke."', "joke", flags=(EVE,)),
        c('"Burnt onions. A cat. A song about a lake. A stone that wants to see the sea."', "list", flags=(EVE,))),
    a("joke", '''"Of course you will." {n}She laughs, and it catches in her throat.{/n} "In the middle of the end of the world, you'll be making a joke, and I'll hear it, and I'll be so annoyed I'll forget to fall." {n}She puts the book in your hands.{/n} "Keep this for me until after. I'll want to write the ending."''', c()),
    a("list", '''{n}She goes very still, listening to her own list said back to her in your voice.{/n}
"Yes," she whispers. "That's the treatment. That's all of it." {n}She puts the book in your hands.{/n} "Keep this for me until after. If I start to go, read it to me. Out loud. Even the diagram."''', c()),
], (MORNING,), delay=24, chapters=(5,))


# --- The epilogue page of the treatment (a committed Arueshalae; no system effects) ------------------------------

SCENES.append(scene(T + "epilogue.together", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}After the Worldwound was closed, Arueshalae kept a daybook for the rest of a very long life, and its first page, in a hand that had only just learned to be careful, read: "Watch people eat. Three times a day."{/n}''',
        paragraphs=(
            p('''{n}She took a river stone with a white band round it to the sea, and let it go, and came back and said that was the first dream she was certain was hers.{/n}''',
              requires=(TEMPLE_LETTER,)),
            p('''{n}She learned every verse of the net-menders' song, and the Kenabres women taught it to their granddaughters with a line in it that had not been there before, about a stranger at the corner of the square.{/n}''',
              requires=(SONG,)),
            p('''{n}She kept a kitchen with a window and a table too small for it, and burned things in it for the Commander, and nobody who sat at it was ever the one being eaten.{/n}''',
              requires=(AFTER_WAR,)),
            p('''{n}She kept the wanting out of the Commander's sight, as she had promised. She was very good at it. Only the cat on the smithy roof ever saw all of her at once, and the cat did not care.{/n}''',
              requires=(SAINT_ONLY,)),
            p('''{n}The Commander never quite stopped being a quack, and she never quite stopped being a patient, and the treatment was never completed, because, as she told anyone who asked, the best treatments never are.{/n}''',
              forbids=(SAINT_ONLY,)),
        ))],
    requires=("trickster.ever", COMMITTED, INTAKE), forbids=(CLOSED, EVIL_DEAD), last=6, Relationship="arueshalae"))


# --- Companion lines for the treatment (exactly Sosiel and Lann, each behind its reactor's guard) ---------------

SCENES.extend([
    reaction("Sosiel", T + "react.sosiel_hand", (TOUCHED,),
             '''"I saw her holding your hand in the mess tent." {n}Sosiel smiles, and then doesn't.{/n} "In all the time I've known her, she's never touched anyone. She flinches from the healers. She flinches from me. Whatever you're doing, Commander, don't stop, and don't be careless about it. You're holding something that has never once been held."''',
             answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=3, last=5,
             entry='"About Arueshalae..."'),
    reaction("Sosiel", T + "react.sosiel_morning", (MORNING,),
             '''"You came down off the old bell tower this morning grey as a Kenabres widow, and she came down after you humming." {n}Sosiel does not smile, quite.{/n} "I've been her friend longer than you've been her doctor, Commander. She's never hummed. Not once, in all the camps." {n}He sets his cup down.{/n} "Whatever it cost you, she knows the price to the copper. Don't ever let her think it was too much. That's the only thing I'll ask."''',
             answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=5, last=5,
             entry='"About Arueshalae..."'),
    reaction("Lann", T + "react.lann_kitchen", (KITCHEN,),
             '''"The cook says you burned her onions and used the good knives." {n}Lann is grinning.{/n} "She also says your demon ate the whole pot and cried. Is that a treatment? Because I've been eating the cook's stew for a year and nobody's calling it medicine."''',
             answer_list=LANN_HUB, forbids=("lann.dead", "lann.kicked_out"), chapter=5, last=5,
             entry='"About Arueshalae..."'),
])


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world."""
