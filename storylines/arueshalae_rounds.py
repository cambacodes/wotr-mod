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
                                             SCROLL, SOSIEL_HUB, UNIT, RECRUITED, WARD_HELD)
from storylines.arueshalae_treatment import (DREZEN_AREA, SERGEANT_STORY, COME_TO_ME, CURE, CURED, DRAINED, ELYSIUM, INTAKE, KITCHEN, MEALTIMES,
                                             MORNING, NIGHT, RELAPSE, RX_WANT, RX_WATCH, T, TOUCHED, ACQ, ACQ_CLAWS, ACQ_LEASH,
                                             ACQ_VOICE)

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

session(CAT, "A sleeping cat", 3, '"You look pleased with yourself."', [
    a("start", '{n}She has straw in her hair. Her hand stays open, palm up, even while the smith calls his apprentices back to work.{/n} "The cat. The one on the smithy roof. It came to me. I\'ve tried sitting under that roof, again and again, being very still. This morning it climbed into my lap."',
        c("Continue", "want", requires=(RX_WANT,)),
        c("Continue", "watch", forbids=(RX_WANT,))),
    a("want", '"It was on my list. Number two. I told you, and then wished I hadn\'t." {n}She studies her empty palm.{/n} "Today I stopped offering it things. I sat down. It put its head under my hand as if I were very slow at my work."',
        c("Continue", "science")),
    a("watch", '"I noticed it while I was watching the smiths eat. Two of us, watching them." {n}She turns her empty hand over.{/n} "This morning it came down and sat on my knee. I hadn\'t brought a fish. Apparently I was wanted anyway."',
        c("Continue", "science")),
    a("science", '"It pushed against my fingers. Hard. Then it went to sleep." {n}She lowers her voice.{/n} "The apprentice said I was to keep stroking it until it woke. She had horseshoes to finish. I sat there until the muster bell."\n{n}Her mouth twitches.{/n} "I was late. For a cat. Write that down; nobody in Alushinyrra would believe it."',
        c('"Congratulations. The demon has a pet."', "pet"),
        c('"Let me see this famous hand, then."', "examine")),
    a("pet", '"It isn\'t mine. The apprentice was quite firm about that." {n}She looks toward the smithy.{/n} "But it wanted my hand. I\'m going to buy it a fish. I know, that will spoil the experiment."',
        c("[Let her go and buy it a fish.]", flags=(CAT,))),
    a("examine", '{n}She holds her palm up for inspection, smiling.{/n} "Nothing there, Commander. It liked me and left nothing to prove it. You\'ll have to take my word, and I lie beautifully."',
        c("[Let her go and buy it a fish.]", flags=(CAT,))),
], (MEALTIMES,), delay=24, chapters=(3, 5))   # Drezen-set (the smithy roof): not in the Abyss (R2-5)


# --- The net-menders' song (Drezen: Chapters 3 and 5) ------------------------------------------------------------

session(SONG, "The net-menders", 3, '"They stopped singing again."', [
    a("start", '''{n}She is standing at the corner of the refugee quarter with her arms wrapped round herself, watching the Kenabres women mend nets they will never use on a lake they will never see again. They are singing. As soon as she takes a step closer, they stop.{/n}
"Every time." {n}She doesn't sound angry. She sounds as if she has been handed a verdict.{/n} "I've been coming here every evening. I stay at the corner. I don't go near. And every time I take one step, one, they stop. It's as if the song knows."''',
        c("Continue", "why")),
    a("why", '''"I want to learn it. That's all. It's the one thing in Drezen I want to learn and can't steal." {n}She hugs herself tighter.{/n} "It's about a lake. I've worked out that much from the corner. A lake that holds the moon so still you could fish it out with a net. And the men who went out in the boats and didn't come back, and the women who mended the nets anyway."
"I think it's the most beautiful thing I've ever heard. And I'm the thing that makes them stop."''',
        c('[Walk into the circle and sing the first verse, badly] "Somebody start me off, I only know the tune."', "sing",
          mythic="Trickster"),
        c('[Offer her your arm, sleeve and all, and walk her in] "Come on. They stop because they don\'t know you. Let them."', "walk")),
    nar("sing", '''{n}You do not know the words. You sing them anyway, loudly and wrongly, in the voice of a Commander who has shouted orders over three battles. The women stare at you in appalled silence. Then an old woman with a net in her lap begins to laugh, and corrects you, and sings the line properly, and another woman joins her to drown you out, and then they are all singing, at you, to make you stop.{/n}
{n}Arueshalae comes in from the corner under cover of the noise, and sits on an upturned basket at the edge of the circle, and nobody notices. By the third verse she is singing too, very softly, on the tune alone.{/n}''',
        c("Continue", "after")),
    nar("walk", '''{n}She lets you. She walks into the circle at your shoulder the way she must once have walked into a room full of strangers in the Upper City: reading every face, finding the door, counting the steps to it. The song stops. The women look at her. You see her decide, very deliberately, to stay where she is.{/n}
{n}You tell them she is the one who warned Kenabres before the attack, the one who was jailed for it; that she has been standing at their corner every night because she wants to learn their song.{/n}
{n}There is a long silence. Then the old woman with a net in her lap shifts over on her bench, just enough, and starts the verse again from the top, slowly, for a beginner.{/n}''',
        c("Continue", "after")),
    a("after", '''{n}Later, walking back through the dark, she hums it under her breath, over and over, and gets the second line wrong every time, and starts again.{/n}
"I only have the first verse. The old woman says I sing it like a sergeant." {n}She stops in the middle of the street.{/n} "They made room for me on the bench, Commander. They didn't know what I am, or they knew and didn't care, and I don't know which is more frightening. I'm going to go back tomorrow. And the day after. Until I know every verse."''',
        c("[Walk her home.]", flags=(SONG,))),
], (MEALTIMES,), delay=24, chapters=(3, 5))


# --- The priestess she killed ----------------------------------------------------------------------------------

session(PRIESTESS, "The last one", 3, '"You\'ve been reading the Desnan prayer book again."', [
    a("start", '{n}She closes the Desnan prayer book when she sees you, then opens it again.{/n} "I want to tell you about the priestess I killed. About what I did to her. I can say it without hiding behind the goddess this time."',
        c('"Tell me."', "tell")),
    a("tell", '''"She was a priestess of Desna. I can't remember the town, only the road out of it. I can't remember her name. I remember what I did." {n}Her voice is very steady.{/n}
"I went to her the way we went to all of them, and made her love me, and it didn't take long; it never did. That was how we all did it. She lay in my arms, and she died of my kiss. I remember every smallest detail. The cold sweat. Her weak whisper. And while she was dying I went into her mind, to find out what mortal dreams were like, and the goddess was waiting there."''',
        c("Continue", "question")),
    a("question", '"Everything since began in her dream. The mercy. The memories. The years as a spy." {n}Her thumb presses into the prayer book.{/n} "And now I come to you, and try what you ask of me, and sometimes I laugh. Does any of this make up for what I did to her?"',
        c('"No. Nothing makes up for her. You carry her. That\'s all."', "carry", flags=(PRIESTESS, CARRY)),
        c('"No. But she had a name. Somebody could write to her shrine and ask it."',
          "write", flags=(PRIESTESS, WRITE))),
    a("carry", '''{n}She closes her eyes, and you think you have done her harm. Then she nods.{/n}
"Thank you. Everyone else says something kind. The priests say the goddess has forgiven me, and I think, then the goddess is wrong, and I'm not allowed to think that." {n}She puts her hand flat on the prayer book.{/n} "You carry her. Yes." {n}She looks at the book under her hand.{/n} "I won't forget her. Not even on a day when I laugh."''', c()),
    a("write", '''{n}She stares at you as if you had suggested she fly to the moon.{/n} "Write to them. To the Desnans. And say what? 'Dear Mother of the shrine, I am the succubus who killed your priestess, please tell me her name so I can...'" {n}She stops.{/n} "So I can what?"
{n}You tell her: so she can stop calling her "the priestess". So the one person in the world who remembers every smallest detail of her death can remember the one detail that was hers.{/n}
"That's insane," {n}she whispers.{/n} "That's the most insane thing anyone has asked of me, and I have been asked for things in Alushinyrra that would curl your hair. I'm going to do it."''', c()),
], (RELAPSE,), delay=24, chapters=(3, 4, 5))

session(TEMPLE_LETTER, "Reply from the river", 5, '"They wrote back."', [
    a("start", '''{n}She has the letter in both hands. It is short, and she has read it enough times that the fold has gone soft.{/n}
"The Mother of the shrine wrote back." {n}Her voice is careful, as if the words might break.{/n} "I told them what I did, and where I buried her, outside Greengates. I wrote it plainly, the way you said." {n}She holds the letter out, and then pulls it back, as if it might hurt you to read.{/n} "The Mother thinks she knows who it was. A priestess of theirs called Ilvanne went north on the Greengates road the year I describe, and never wrote again. She thinks. She isn't sure. Neither am I." {n}She reads on, and her voice catches.{/n} "She says Ilvanne used to talk about the sea. There was always someone who needed her first."''',
        c("Continue", "sea")),
    a("sea", '''"And she sent this." {n}From the fold of the letter she takes a small flat river stone, grey, with a white band round it.{/n}
"She says: 'This is from the river below our shrine. Ilvanne used to stand in the shallows and call it the nearest she would get, if it was Ilvanne. If you are what you say you are, take her to the sea. Then do not write to us again. I will pray for her. I will not pray for you.'" {n}Arueshalae turns the stone over and over.{/n} "She hates me. Good. Somebody should, who knew her." {n}Her hand closes on it until the knuckles go pale.{/n} "And she still sent it. Commander, I know what to do with hate. I don't know what to do with a stone."''',
        c('"I don\'t know. But when the Wound is closed, we\'re going to the sea."', "promise", flags=(TEMPLE_LETTER,)),
        c('"Maybe that\'s what dreaming is."', "dream", flags=(TEMPLE_LETTER,))),
    a("promise", '''"We." {n}She presses the stone to her lips, very lightly, as if it were a person she might drain.{/n} "Yes. When the Wound is closed. I'm going to hold you to that. I'm going to hold you to it so hard."''', c()),
    a("dream", '''{n}She is quiet for a long time.{/n} "Desna asked me what I dream of. I keep finding things I want to tell her." {n}She closes her fist around the stone.{/n} "This one is grey, with a white band around it. The Mother asked me to take it to the sea. I want to."''', c()),
], (WRITE,), delay=72, chapters=(5,))


# --- The Abyss (Chapter 4): her old name ------------------------------------------------------------------------

session(OLD_NAME, "What they called me", 5, '"The woman in the Alushinyrra market. Who was she?"', [
    a("start", '''{n}She is sitting with her back to the fire, which she never does, and her wings are wrapped round her like a cloak.{/n}
"Somebody I knew. Somebody from the Ten Thousand Delights." {n}She is holding herself very still.{/n}''',
        c("Continue", "offer", forbids=(ACQ,)),
        c("Continue", "seen_voice", requires=(ACQ_VOICE,)),
        c("Continue", "seen_claws", requires=(ACQ_CLAWS,)),
        c("Continue", "seen_leash", requires=(ACQ_LEASH,))),
    a("offer", '''"She recognised me across the whole market and called me by the old word, loud, so everyone would turn, and they all did. What she used to call all of us. A word for what we did to people." {n}Her mouth twists.{/n} "It isn't my name. It never was. It was only true."
"She asked if I was hungry. She said there was a party in the Upper City and plenty of mortals at it who'd paid to be eaten, and she'd get me in, for old times' sake. She said it kindly. That's the worst of it. In the Delights they say those things kindly."
{n}Her hands are clenched in the fabric of her wings.{/n} "And I was hungry. I am. The Abyss made it worse, Commander. It was like trying not to drink when you're standing in the sea. Some nights it still is, even here. I stood there with her hand on my arm and I thought about saying yes for as long as it takes to say it."''',
        c('"You didn\'t say it."', "didnt"),
        c('[Hold out your hand] "Then take this instead. Right now."', "hand", requires=(TOUCHED,), forbids=(TOUCHED,)),   # retired
        c('[Spend a Scroll of Death Ward: call the chaplain out into the yard to read it over you, then hold out your hand] "Then take this instead. Right now."',
          "hand", requires=(TOUCHED, WARD_HELD), remove_item=SCROLL)),
    a("didnt", '"No. I didn\'t." {n}She turns toward the fire.{/n} "She laughed at me. She knew I\'d wanted to say yes. So do you, now." {n}Her mouth twists.{/n} "Write it in your little book, Commander. Your succubus nearly went to a party in the Upper City, and the only thing that stopped her was that she\'d have had to tell you afterwards."', c(flags=(OLD_NAME,))),
    nar("hand", '''{n}The shrine's chaplain comes out into the yard at your call, breaks the seal and reads the ward over you, and goes back in without a word. She watches the parchment burn down to nothing in his fingers. She looks at your hand as if it were a door she is not sure she is allowed through. Then she takes it, here in the chapel yard, with the Delights still on her like a smell she cannot wash out, and holds on.{/n}''',
        c("Continue", "held_cure", requires=(CURED,)),
        c("Continue", "held_paid", forbids=(CURED,))),
    a("held_cure", '''{n}Nothing comes out of you. She holds on anyway, harder than she needs to, and slowly her shoulders come down from round her ears.{/n}
"That's the difference," {n}she says at last, very quietly.{/n} "Her party would have been more. Much more. And I'd have hated myself before dawn. This is less, and I don't." {n}At the sixth minute she lets go, before the ward can.{/n} "Don't tell her about the scrolls. She'd want you to buy her some, and she'd make you watch what she did with them."''', c(flags=(OLD_NAME,))),
    # arue12: the Chapter 4 beat was played; she does not retell what the Commander saw. Each callback reads its cost.
    a("seen_voice", '''"You were there. You heard what came out of my mouth." {n}Her hands are clenched in the fabric of her wings.{/n} "'This one's mine.' I've said it in my head every night since. Not to you. To her. She'd have had me upstairs within the hour if you'd said one word, and I'd have gone, and told myself it was to get away from you."
{n}She stares into the dark past the fire.{/n} "The Abyss made it worse, Commander. It was like trying not to drink when you're standing in the sea. Some nights it still is, even here. Some nights I'm still standing in that street with her hand on my arm."''',
        c('"You didn\'t say yes."', "didnt"),
        c('[Spend a Scroll of Death Ward: call the chaplain out into the yard to read it over you, then hold out your hand] "Then take this instead. Right now."',
          "hand", requires=(TOUCHED, WARD_HELD), remove_item=SCROLL)),
    a("seen_claws", '''"She's telling them all, you know. Every girl in the Delights." {n}She turns her hand over in the firelight; the nails are short and clean again.{/n} "I can still feel her cheek come apart. I lie down on it at night. I don't sleep; I lie down on it, and it's warm." {n}A breath.{/n}
"And under how good that was, the thing I can't put down. She offered me the room, and before you opened your mouth I was going to say yes. I cut her for the reaching. I'd have gone upstairs for the room."''',
        c('"You didn\'t say yes."', "didnt"),
        c('[Spend a Scroll of Death Ward: call the chaplain out into the yard to read it over you, then hold out your hand] "Then take this instead. Right now."',
          "hand", requires=(TOUCHED, WARD_HELD), remove_item=SCROLL)),
    a("seen_leash", '''"I'm still angry with you." {n}She does not look round.{/n} "I want you to know that before anything else. You put him in my hand."
{n}Her wings tighten round her.{/n} "And I've been honest with myself since, which you'd hate. If she'd offered me the room first, and not the leash, I'd have gone up the stairs. The leash I could cut. The stairs I'd have climbed, and been glad, and come back down and lied to you about it beautifully."''',
        c('"You didn\'t say yes."', "didnt"),
        c('[Spend a Scroll of Death Ward: call the chaplain out into the yard to read it over you, then hold out your hand] "Then take this instead. Right now."',
          "hand", requires=(TOUCHED, WARD_HELD), remove_item=SCROLL)),
    a("held_paid", '''{n}Nothing comes out of you. She holds your hand between her wrists instead of her palms anyway, the careful way, as if she did not quite believe the ward.{/n}
"Seven minutes," {n}she says.{/n} "I could have had a whole party. I'd rather have seven of yours." {n}She is shaking.{/n} "If we ever go back down there, don't do that. Everybody in the Abyss can smell it when someone gives."''', c(flags=(OLD_NAME,))),
], (INTAKE,), delay=24, chapters=(5,))


# --- The Commander wounded (Chapter 5): she sits beside the cot --------------------------------------------------

session(WOUND, "Beside your bed", 5, '"You\'re sitting up. Good."', [
    nar("start", '''{n}The wound is not serious, the chaplains say, which is what they say about wounds that nearly were. You are propped up in the field hospital with your side strapped and a taste of healing potion in your mouth like old pennies, and she is sitting on the stool beside the cot where she has been sitting, the orderlies tell you, for eleven hours.{/n}''',
        c("Continue", "helpless")),
    a("helpless", '''"I couldn't do anything." {n}She is holding her own hands in her lap, as if they were a pair of animals that might get loose.{/n} "They carried you in and there was so much of you on the stretcher, and every healer in the tent went to work, and I just stood there. I knew exactly where it would hurt you, and not one thing to do about it."
"The orderly had to ask me to move. Twice. The second time she took me by the sleeve and walked me out, and she was very kind about it, and I wanted to kill her for being able to help."''',
        c("Continue", "stitch")),
    a("stitch", '''{n}She picks up a needle and a reel of gut from the orderly's tray, holding them as if they were contraband.{/n}
"So I asked the surgeon to teach me this. While you were asleep. I practised on a pig's belly from the kitchens." {n}She is blushing furiously.{/n} "It turns out I have very steady hands. It turns out that's what all those centuries were good for. The surgeon says I'm a natural. I didn't tell her why."
"Your stitches are coming loose at the bottom. May I? I won't touch you. Only the thread."''',
        c('"Go ahead. Steady hands."', "go", flags=(WOUND,)),
        c('[Hold out your hand for her to hold, instead] "Stitch later. Sit with me."', "sit", requires=(TOUCHED,),
          flags=(WOUND,))),
    nar("go", '''{n}She does it without once touching your skin, only the thread and the needle and the steel of the forceps, her face an inch from the wound, her breath held. It is the neatest suture you have ever had. She ties it off and cuts it and sits back, and her hands are shaking now that it is done.{/n}
"There," {n}she says.{/n} "Now you've got a little bit of me in you that didn't take anything. Just a knot."''', c()),
    a("sit", '''{n}She looks at the hand, and at the strapping on your side, and at the hand again.{/n} "You're hurt, and there's no ward on you, and you smell of blood, and I won't." {n}Then she lays her own hand on the blanket over yours, so that only the wool is between them, and keeps it there for the rest of the night.{/n}
"Commander's orders," {n}she says, when the orderly comes to shoo her away, and smiles at her with every one of her teeth, and the orderly, to everyone's surprise, goes.{/n}''', c()),
], (KITCHEN,), delay=24, chapters=(5,))


# --- The dance (Chapter 5) --------------------------------------------------------------------------------------

session(DANCE, "Music in the square", 5, '"There\'s music in the square."', [
    a("start", '''{n}There is. Someone has won something, or thinks they have, and the Drezen square is full of lanterns and bad fiddlers and soldiers dancing with anybody who will have them.{/n}
"I've been watching them from the steps. I've watched mortals dance for years, at weddings, in taverns, wherever I could stand at the back and not be noticed." {n}She stops.{/n} "In the Upper City we danced, of course. It was a kind of hunting. Here it seems to be a kind of falling over while holding on to someone."''',
        c('[Hold out your hand] "Dance with me. Twice a week, while the fiddlers last."', "dance", requires=(TOUCHED,), forbids=(TOUCHED,)),   # retired
        c('[Spend a Scroll of Death Ward: have the chaplain read it over you on the chapel steps, then hold out your hand] "Dance with me. Twice a week, while the fiddlers last."',
          "dance", requires=(WARD_HELD,), remove_item=SCROLL),
        c('[Offer her your sleeve] "Dance with me. Twice a week. The sleeve\'s free."', "dance_sleeve")),
    nar("dance", '{n}The ward is on you when she takes your hand. The chapel steps and the walk into the square have used two minutes already. She mouths the count against your ear as you dance. Before the fifth remaining minute ends, she moves her fingers to your sleeve.{/n} "There. Cloth now. I want the next dance too." {n}She pulls you back toward the fiddlers.{/n}',
        c("Continue", "cure", requires=(CURED,)),
        c("Continue", "glove", forbids=(CURED,))),
    nar("cure", '''{n}You dance badly, and she dances beautifully, and between you it comes out as something the fiddlers can live with. One reel is seven minutes, near enough; you both know it, and you both pretend not to. When the fiddlers start the second, she moves her hand from yours to your sleeve without missing a step, and you dance the rest with the cloth between you, which the fiddlers think is very courtly.{/n}
"You're counting," {n}she says into your ear.{/n} "Not the steps. The other thing." {n}You are. So is she.{/n}''',
        c("Continue", "after")),
    nar("glove", '''{n}She holds your sleeve, not your hand, and dances with the cloth between you. You dance anyway. You dance badly, and she dances beautifully, and nobody in the square notices that the Commander's partner never once touches the Commander's skin.{/n}''',
        c("Continue", "after")),
    nar("dance_sleeve", '''{n}She looks at your sleeve, and then at you, and laughs, and takes it, a fistful of good Mendevian wool, and lets you pull her down the steps into the crowd. For a moment she is rigid with terror in the middle of the square, a demon in a crowd of mortals with everyone within reach.{/n}
{n}Then a fiddler hits a wrong note, and a sergeant treads on your foot, and somebody's child runs between your legs, and she laughs, and the rigidity goes out of her. You dance badly, and she dances beautifully, holding your sleeve as if it were your hand, and nobody in the square notices that she never once touches your skin.{/n}''',
        c("Continue", "after")),
    a("after", '''{n}She pulls you out of the crowd before the last dance, breathless, and leans on the wall of the grain store with her head tipped back to the lanterns.{/n}
"It isn't hunting." {n}She sounds astonished.{/n} "It's just... being in the same place as everyone at once, and nobody's trying to get anything. How did I watch it for years and not see that?" {n}She looks at you.{/n} "Twice a week, you said. I'm going to hold you to it."''',
        c("[Promise twice a week.]", flags=(DANCE,))),
], (TOUCHED,), delay=24, chapters=(5,))


# --- After the yes ---------------------------------------------------------------------------------------------

session(AFTER_WAR, "After the war", 5, '"What will you do, after?"', [
    a("start", '''{n}She answers in a rush, as if afraid of losing her nerve.{/n}
"A kitchen. I want a kitchen. With a window, and a table that's too small, and a shelf for whatever cat decides to come in. I want to learn to cook. I'll be terrible at it."
{n}She stops for breath.{/n} "When the Wound is closed. Nobody can send me out on patrol while I'm burning the supper. I could burn the whole pot if I liked."''',
        c("Continue", "you")),
    a("you", '"And you. I want you there, when you\'re there. I\'m not a fool, I know what you are. You\'ll be off doing impossible things for the rest of your life, and I\'ll be the one at the window, waiting to find out which ones." {n}She says it lightly, and means it lightly, and her eyes are very steady.{/n}\n"I remember Lady Vellexia\'s guests, Commander. The table was never the problem. The empty chair was. So come back to the kitchen. That\'s all. Come back. I\'ll want to see you."',
        c('"I\'ll come back to the kitchen. Burn something for me."', "burn", flags=(AFTER_WAR,)),
        c('"It sounds like an excellent future."', "verdict", flags=(AFTER_WAR,))),
    a("burn", '''"Oh, I will." {n}She grins, all teeth, and for a moment she looks exactly like what she is, and it is wonderful.{/n} "I'm going to burn things for you that nobody has ever burned before. I've got centuries of practice at making mortals suffer. It's time it was good for something."''', c()),
    a("verdict", '''"Excellent." {n}She tastes the word.{/n} "Nobody has ever said that about my future. They said 'damned', and 'doomed', and in the Delights they would have said 'profitable'." {n}She laughs.{/n} "Excellent. I'll write that in my book. On the front page. In red, which is the only colour I used to write in."''', c()),
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

session(NIGHTMARE, '''Faces in the dark''', 5, '"I\'m sorry I woke you."', [
    nar("start", '''{n}Her cry wakes you. She is sitting on her bedroll with her wings half open, staring into the dark. Her nails have left red marks on her own arms.{/n}''',
        c("Continue", "dream")),
    a("dream", '''"I was thinking about my first dream. How proud I was of it." {n}She is shaking.{/n} "Then I closed my eyes, and there was the priestess. Her skin was cold. She was trying to speak. I didn't stop."
"I wasn't asleep. I knew where I was. I could hear the watch outside." {n}She presses her palms against her eyes.{/n} "I still couldn't stop seeing her."''',
        c('"I heard you. I\'m here."', "price", flags=(NIGHTMARE,)),
        c('[Sit with her till dawn, and say nothing.]', "sit", flags=(NIGHTMARE,))),
    a("price", '''{n}She lowers her hands and looks at you.{/n} "You're here."
"I used to pray for a dream. I've had one. But when I close my eyes, I still see her." {n}She takes a fistful of your shirt, keeping her fingers clear of your skin.{/n} "Stay till it's light. Not every night. This one."''', c()),
    nar("sit", '''{n}You sit at the end of the bedroll. After a while she leans against your shoulder, with your coat between you. Her hands slowly unclench. Outside, the watch changes. She listens until the first birds begin, then lifts her head to look at the pale sky.{/n}
"They're sounding the muster. I'll come down in a moment. Go on; I want to watch you walk away from me once without it costing anything."''', c()),
], (MORNING,), delay=48, chapters=(5,))

session(EVE, "Before Threshold", 5, '"When it comes, then."', [
    a("start", '''{n}The camp is very quiet tonight. Everyone knows the end of this war is out there somewhere ahead of the column, and everybody who has anything to say about it is saying it, in low voices, in the dark. She has found you on the edge of the lines with a lantern and the daybook, which is nearly full now.{/n}
"I've been reading it back. From the beginning. Your dare, on the first page, in my worst hand." {n}She laughs softly.{/n} "It seems a very long time ago. I was so sure it was a joke."''',
        c("Continue", "fear")),
    a("fear", '''"I'm afraid of the end of it." {n}She says it simply, the way she used to name a mark's weakness to her sisters: a fact, laid on the table.{/n} "Not only of dying. Of what's at the bottom of the Wound. Of the Abyss seeing me come back and remembering what I am, and calling, and me answering." {n}She closes the book.{/n}
"So I want to ask you something. If it calls me, when we get there, and I start to go, what do you do?"''',
        c('"Look for me. I\'ll be the one making a bad joke."', "joke", flags=(EVE,)),
        c('"Burnt onions. Your list. The night you walked out of Fye\'s and kept walking."', "list", flags=(EVE,))),
    a("joke", '''"Of course you will." {n}She laughs, and it catches in her throat.{/n} "In the middle of the end of the world, you'll be making a joke, and I'll hear it, and I'll be so annoyed I'll forget to fall." {n}She puts the book in your hands.{/n} "Keep this for me until after. I'll want to write the ending."''', c()),
    a("list", '''{n}She goes very still, listening to her own list said back to her in your voice.{/n}
"Yes," {n}she whispers.{/n} "That's the answer. That's all of it." {n}She puts the book in your hands.{/n} "Keep this for me until after. If I start to go, read it to me. Out loud. Even the diagram."''', c()),
], (MORNING,), delay=24, chapters=(5,))


# --- The epilogue page of the redeemed courtship (a committed Arueshalae; no system effects) ---------------------

SCENES.append(scene(T + "epilogue.together", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}After the Worldwound was closed, Arueshalae kept a daybook for the rest of a very long life, in a hand that had only just learned to be careful.{/n}''',
        paragraphs=(
            # NM1 (Sol BEL): the first page is the prescription the Commander actually wrote at the intake.
            p('''{n}Its first page read: "Watch people eat. Three times a day."{/n}''', requires=(RX_WATCH,)),
            p('''{n}Its first page was the first list: one thing a day that she wanted and that was not a person. Number one was "nothing". Number two was the cat on the smithy roof, which still did not like her.{/n}''',
              requires=(RX_WANT,), forbids=(RX_WATCH,)),
            p('''{n}She took a river stone with a white band round it to the sea, and let it go, and came back and said she had wanted to make that journey herself.{/n}''',
              requires=(TEMPLE_LETTER,)),
            p('''{n}She learned every verse of the net-menders' song, and the Kenabres women taught it to their granddaughters with a line in it that had not been there before, about a stranger at the corner of the square.{/n}''',
              requires=(SONG,)),
            p('''{n}She kept a kitchen with a window and a table too small for it, and burned things in it for the Commander, and nobody who sat at it was ever the one being eaten.{/n}''',
              requires=(AFTER_WAR,)),
            p('''{n}The Commander had once asked her for only the good days, and she had refused, and she never let {mf|him|her} forget it. Only the cat on the smithy roof ever saw all of her at once without being asked to, and the cat did not care.{/n}''',
              requires=(SAINT_ONLY,)),
            # arue12 REBUILD: no clinic. The hunger stays hers until canon lifts it (c1bbe44f); she keeps the scrolls and the want.
            p('''{n}She bought her own scrolls after the war, out of her own pay, and kept the box on a shelf the Commander was not allowed to reach. She decided when a seal was broken. On the nights she decided against it she said so, and lay down beside the Commander anyway, awake, wanting, the old hunger curled between them like a cat that had never once been fed. It was hers. She kept it the way she kept everything else she had refused.{/n}''',
              forbids=(SAINT_ONLY, ELYSIUM)),
            p('''{n}The day the Abyss let go of her she went down into Drezen and put her bare hands on everything she had ever walked away from, one thing after another, the way a thief goes through a house: bread, latches, strangers' sleeves, the hands of soldiers in the street. She still remembered every taste she had ever taken, and said so at table, to guests who had not asked, and watched them decide whether she was joking. She was not.{/n}''',
              requires=(ELYSIUM,), forbids=(SAINT_ONLY,)),
        ))],
    requires=("trickster.ever", COMMITTED, INTAKE), forbids=(CLOSED, EVIL_DEAD, RECRUITED, "sacrifice"), last=6, Relationship="arueshalae",
    ForbidOverrides={"sacrifice": "trickster.commander_back"}))


# Sol r1 (INT): the released-entry commit (treatment.freed_hands) has its own ending; she was never a patient.
SCENES.append(scene(T + "epilogue.freed", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}After the Worldwound was closed, Arueshalae spent a year touching things. Door-latches, horses, bread still hot from the oven, the rough heads of children who ran at her in the street, the Commander's hand under the table at every feast, on purpose, where everyone could see. She kept a daybook of it, in a careful hand, and on the first page she wrote only: "Warm."{/n}''')],
    requires=("trickster.ever", COMMITTED, T + "freed_hands"), forbids=(CLOSED, EVIL_DEAD, RECRUITED, "sacrifice"), last=6,
    Relationship="arueshalae", ForbidOverrides={"sacrifice": "trickster.commander_back"}))


# --- Companion lines for the redeemed courtship (exactly Sosiel and Lann, each behind its reactor's guard) ------

SCENES.extend([
    reaction("Sosiel", T + "react.sosiel_hand", (TOUCHED,),
             '''"I saw her holding your hand in the mess tent." {n}Sosiel smiles, and then doesn't.{/n} "In all the time I've known her, she's never touched anyone. She flinches from the healers. She flinches from me. Whatever you're doing, Commander, don't be careless about it. She looked happy. I was glad to see it."''',
             answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=3, last=5,
             entry='"About Arueshalae..."'),
    reaction("Sosiel", T + "react.sosiel_morning", (MORNING,),
             '''"You came down off the old bell tower this morning yawning like a sentry after a double watch, and she came down after you humming." {n}Sosiel does not smile, quite.{/n} "I've been her friend longer than you've been buying her scrolls, Commander. She hums when she thinks nobody is listening. This morning she didn't care who was." {n}He sets his cup down.{/n} "She told me what those scrolls cost you. She knows the price to the copper. Don't ever let her think it was too much. That's the only thing I'll ask."''',
             answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=5, last=5,
             entry='"About Arueshalae..."'),
    reaction("Lann", T + "react.lann_kitchen", (KITCHEN,),
             '''"The cook says you burned her onions and used the good knives." {n}Lann is grinning.{/n} "She also says your demon ate the whole pot and licked the spoon. Is that how you court a succubus? Because I've been eating the cook's stew for a year and nobody's ever looked at me like that over it."''',
             answer_list=LANN_HUB, forbids=("lann.dead", "lann.kicked_out"), chapter=5, last=5,
             entry='"About Arueshalae..."'),
])


# Q11: after the native Elysium ending (BestEnding; her touch no longer drains) the sessions that stage a drain close.
for _scene in SCENES:
    if _scene["Id"] in (OLD_NAME, DANCE, WOUND, T + "react.sosiel_morning") and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)
    # Sol verify (2026-10-01): a beat staged at a Drezen place plays only in Drezen (the refugee quarter, the chapel yard, the square, the citadel roofs).
    if _scene["Id"] in (SONG, OLD_NAME, DANCE, RACE):
        _scene["Areas"] = [DREZEN_AREA]


# NM1 (Sol INT): the native companion pages for Arueshalae, reconciled with a committed Arueshalae (E14d). Cue_0462
# (f76713034f4087a4f80495971c47ca7b, the war over and her wandering just begun, Q3 not completed) and Cue_0461
# (78ae1bdc3b0824b4ca2ed618782f1faa, the dream world where her beloved was alive, after the sacrifice) are replaced while
# she is committed (the second only when the Commander came back); outside those states the native page plays. Cue_0458
# (Q3 completed, the cottage) has a continuation, which E14d does not edit.
COMPANIONS = "fec3b6f28610c8a48a239f148ed3ed60"
PAGE = "e83fff8e997db8e439bf12e09225696a"
WANDER = T + "epilogue.native_wander"
SCENES.append(scene(WANDER, "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '{n}After the fighting at Threshold ended, Arueshalae travelled. She wrote to the Commander when she found a place she wanted to stay, and returned for visits with more questions than answers. At the small kitchen table she left a chair for {mf|him|her}.{/n}', c())],
    requires=("trickster.ever", COMMITTED), last=99, Relationship="arueshalae",
    # E14d delivery (engine queue item 5): the live predicate also reads these, so the wander page never plays for a closed or
    # fallen Arueshalae, or after a sacrifice the Commander did not come back from (dead / dismissed: the scene's own forbids).
    forbids=(CLOSED, "arueshalae.corrupted", "sacrifice"), ForbidOverrides={"sacrifice": "trickster.commander_back"}))
# Harness 2026-10-02: the Cue_0461 (78ae1bdc) dream-world edit failed the runtime cue-policy contract (RanRomance's SlideArue
# sets its Continue to Aranka's slide) and degraded the whole relationship in game. Engine queue item 6 restores it: the
# reviewed evidence accepts the parent's continuation and the replacement keeps it (Aranka's slide still follows), and the
# edit is warning-only (a refusal keeps the native dream page; nothing degrades).
DREAMS = T + "epilogue.native_dreams"
SCENES.append(scene(DREAMS, "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}She still went into the dream world, but less each year. The one she would have looked for there was alive, and snored, and stole the blankets, and she found she preferred that to any dream.{/n}''', c())],
    requires=("trickster.ever", COMMITTED, "trickster.commander_back"), last=99, Relationship="arueshalae",
    forbids=(CLOSED, "arueshalae.corrupted")))
NATIVE_EPILOGUE_EDITS = {
    "f76713034f4087a4f80495971c47ca7b": dict(Page=PAGE, Sequence=COMPANIONS, Key="fa1468ba-9679-4805-9dd4-c71997aa4e7f",
                                             Replacement=WANDER, When=[[COMMITTED, "trickster.ever"]]),
    "78ae1bdc3b0824b4ca2ed618782f1faa": dict(Page=PAGE, Sequence=COMPANIONS, Key="411ef2f1-5168-455f-99b0-ca33960678c5",
                                             Replacement=DREAMS, When=[[COMMITTED, "trickster.ever", "trickster.commander_back"]]),
}


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world. NM1: the reconciled native companion pages (E14d)."""
    from storylines.native_overrides import register_legacy
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)
