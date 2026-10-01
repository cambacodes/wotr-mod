"""Arueshalae, the last case notes: the list, the watcher watched, the ward she cannot learn but can spend, the
chaplain's sermon, and the second chair (Trickster path; arueshalae.md F18). The glover and the fallen wager are retired
by gating (2026-10-01; ids and indices kept).

Canon: "I'm watching... I'm listening to their conversations, studying their faces" (hub 48ad6e04); "I used to talk a
lot before, and all of it was a lie... I like silence more now" (b6c4b7ad); "It's a great temptation. I don't know if I
should be trusted with such power" (63d51120). Authored and labelled: the sermon's text, the chairs.
"""
from story_format import c, n, scene
from storylines.arueshalae_trickster import (AFTERTASTE, ALLY, CHAPLAIN, CLOSED, COMMITTED, DEAD, DREZEN, EVIL_DEAD,
                                             EVIL_UNIT, HUB, P, RECRUITED, RETIRED_TEXT, RETURNED, REUNITED, SCROLL,
                                             TAVERN_FAILED, DREZEN_PLACES, TAVERN_PRESENCE, UNIT, WARD_HELD, YARD_PRESENCE)
from storylines.arueshalae_rounds import CAT, TEMPLE_LETTER
from storylines.arueshalae_chapel import CENSER
from storylines.arueshalae_treatment import (CURED, DRAINED, DREZEN_AREA, ELYSIUM, KITCHEN, MEALTIMES, MORNING, RX_WANT, RX_WATCH, T,
                                             TOUCHED)

SCENES = []
FORTY = T + "day_forty"
WATCHED = T + "watched_you_eat"
TEACH = T + "teach_me"
HER_BOX = T + "her_scroll"                 # she spent one of the Commander's scrolls on someone of her own choosing
GLOVES = T + "the_glover"
SERMON = P + "chaplain.sermon"
CHAIR = T + "the_second_chair"
NOVICE = T + "the_novice"
RAIN = T + "rainy_day"
SEA_MAP = T + "sea_map"
SOSIEL_OFFER = P + "returned.sosiel"
OTHER_ONE = P + "evil.the_other_one"
SCAR = T + "the_scar"
PRAYER = P + "chaplain.prayer"
BET = P + "evil.wager"
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


# --- The list, day forty -------------------------------------------------------------------------------------

hub(FORTY, "Number forty", 3, '"How\'s the list?"', [
    a("start", '''{n}She produces it at once, as if she had been carrying it in her hand in case you asked. It is several pages now, the early ones creased soft from being unfolded and folded again.{/n}
"Number thirty-one: I want it to rain on a day when I don't have to go anywhere. Number thirty-three: I want to know what the novice who sweeps the chapel is humming. Number thirty-six, and I'm very proud of this one: I want to be bored."
{n}She looks up.{/n} "Do you understand? Bored. Nothing happening, and nobody wanting anything, and no danger, and no hunger, just a long afternoon with nothing in it. Mortals complain about it constantly. I've never once had it."''',
        c("Continue", "forty")),
    a("forty", '''"And number forty." {n}She hesitates, and turns the page so you can't see it.{/n} "Number forty I'm not going to read to you. It's about you. It isn't what you're thinking; I checked, I was very careful. But I'm not ready to say it out loud."
"No. I'm keeping that page. Don't look at me like that."''',
        c('"Of course. Every patient\'s allowed one secret from their doctor."', "secret", flags=(FORTY,)),
        c('[Straight-faced] "Absolutely not. Hand it over. Medical necessity."', "tease", flags=(FORTY,))),
    a("secret", '''"One secret." {n}She folds the list up very small and tucks it inside her bodice, against her skin.{/n} "I've kept a great many secrets for other people, and sold some. This one isn't intelligence for anyone. It's mine." {n}She pats the place where the paper is.{/n} "Thank you. I'll tell you on number four hundred. Maybe."''', c()),
    a("tease", '''{n}She snatches the list out of reach and holds it behind her back, laughing.{/n} "No! Absolutely not! Medical necessity, the doctor says." {n}She backs away, still laughing.{/n} "You'll hear number forty when I'm good and ready, doctor, and not a moment before. That's my prescription for you. It's called patience. You've never taken it."''', c()),
], (MEALTIMES, RX_WANT), delay=48, chapters=(3, 4, 5))


# --- The watcher watched -------------------------------------------------------------------------------------

hub(WATCHED, "Observations of a Commander eating", 3, '"You\'ve been watching me at meals."', [
    a("start", '''"Of course I have. You told me to watch people eat three times a day. You eat three times a day. Sometimes." {n}She has the daybook open, and she is completely unrepentant.{/n}
"You're my most interesting subject. Everyone else eats as if they're at a meal. You eat as if you expect to be ambushed in the next four minutes. You keep your back to the wall. You never finish. Last night you gave half your bread to whoever was next to you, and didn't look to see who it was."''',
        c("Continue", "notes")),
    a("notes", '''{n}She turns a page, reading aloud in a clinical voice.{/n} "'Subject laughed with mouth full, twice. Subject told the quartermaster a joke about a goat that was not funny. Quartermaster laughed anyway. Conclusion: subject is loved.'" {n}She looks up, suddenly shy.{/n}
"I didn't understand that, at first. Why the quartermaster laughed. And then I understood it, and I had to stop watching for a day." {n}She closes the book.{/n} "I watched you hand that bread away, and I wanted to be the one sitting next to you. That's all. That's the whole entry."''',
        c('"And what are you going to do about it?"', "do", flags=(WATCHED,)),
        c('"Tell the quartermaster the goat joke was very funny."', "goat", flags=(WATCHED,))),
    a("do", '''"Keep watching." {n}She smiles, very small.{/n} "For now. Watching is what I do instead of taking. One day I'll put the book down and sit beside you at the mess table instead. I almost did today." {n}She tucks the book into her belt.{/n} "I'll let you know. Probably by accident."''', c()),
    a("goat", '''{n}She laughs so suddenly she snorts, and claps her hand over her face, horrified.{/n} "That was undignified. You made me undignified." {n}She peeks over her fingers.{/n} "It wasn't funny. It was a terrible joke. I laughed at it for an hour afterwards, alone, on the wall, and I don't know why."''', c()),
], (MEALTIMES, RX_WATCH), delay=48, chapters=(3, 4, 5))


# --- "Teach me the trick" --------------------------------------------------------------------------------------

hub(TEACH, "The one trick", 5, '"Teach me how you do it."', [
    a("start", '''"The ward. The scroll. The way you read it, and the cold simply doesn't come." {n}She is standing very straight, as she does when she has rehearsed something.{/n}
"Teach me to do it. Then I could touch anyone, not just you. The baker's girl, the pikeman in the hospital, the Kenabres women on the bench." {n}Her voice wavers.{/n} "Please. I learned so many cruel things so easily. Why should this be the one that's hard?"''',
        c("Continue", "try")),
    nar("try", '''{n}You try. You put a spent scroll case in her hands and show her how the words run, and she follows them with one finger, line by line, the way she follows a stranger's face in the market. Then you tell her the plain thing the shrine's chaplain told you, the thing you should have told her first: the ward goes on the one who is touched, not on the one who touches. She could have every scroll in Drezen read over herself, and her hand would take exactly what it always took.{/n}
{n}She sits with that for a long time, turning the empty case over and over.{/n}''',
        c("Continue", "cant")),
    a("cant", '''"So reading it over myself wouldn't help. I'd have to ward someone else, every time, and pay for every hand." {n}She laughs, and it is not a good laugh.{/n}
"For one moment I thought I could take the baker's girl by the hand, and walk out of here with nobody holding mine. Instead I'd have to ask her father to let a demon have a scroll read over his daughter, at the price of a horse, so that I could show her how to fold dough."''',
        c('"Good. A ward you could carry for anyone, you\'d spend on the baker\'s girl."', "need", flags=(TEACH,)),
        c('"Then I\'ll hold the hands you can\'t. You point, I hold."', "point", flags=(TEACH,)),
        c('[Take one of your own scrolls out of the case and put it in her hand] "Then buy it. This one\'s yours. Spend it on whoever you like."',
          "hers", flags=(TEACH, HER_BOX), requires=(WARD_HELD,), remove_item=SCROLL)),
    a("need", '''{n}She stares at you, and then she hears the joke, and then the thing under it that you did not make a joke of.{/n} "You're jealous. Of the baker's girl. Of a pikeman with one leg." {n}Her mouth twists.{/n} "Lady Vellexia kept the good wine locked in a cabinet only she could open, so the guests would come back for it. Every one of them came back. I poured." {n}She looks at the scroll case on your belt.{/n} "And here's the doctor, keeping the only key in {mf|his|her} own satchel. I ought to hate that. Tender of Dreams forgive me, I'm going to come back for it every night."''', c()),
    a("point", '''"I point, and you hold." {n}Her mouth twitches.{/n} "The Commander of the crusade, going round the field hospital holding the hands of everyone a succubus points at." {n}Then she stops smiling.{/n} "You'd do it, wouldn't you. You'd actually do it." {n}She takes a fold of your sleeve, and doesn't try anything, and just holds it.{/n} "All right. I'll point. Carefully."''', c()),
    a("hers", '''{n}She looks at the sealed scroll in her palm as if it were a live coal, or a ring.{/n} "Mine. To spend on whoever I like." {n}Her fingers close on it.{/n} "You know who it's going to be. You knew before you took it out."
"The baker's girl. Tomorrow, before dawn. The shrine's chaplain will read it over her for me; he won't ask why, he'll only ask whether she's had breakfast. And for seven minutes I'll stand at the trough beside her and let her lean on me, and show her how to fold the dough with my hands on hers, and nothing will go out of her at all." {n}She tucks the scroll inside her bodice, against her skin, the way she keeps her list.{/n} "It's the most extravagant thing anyone has ever let me do. I'm going to remember this."''', c()),
], (KITCHEN, CURED), delay=48, chapters=(5,))


# --- The glover: RETIRED by gating (2026-10-01; ids and indices kept). Any caress drains; no glove stops it. ---------

hub(GLOVES, "A pair of gloves", 3, '"New gloves?"', [
    a("start", RETIRED_TEXT, c("Continue", "test")),
    a("test", RETIRED_TEXT, c("[Take the gloved hand]", "take")),
    nar("take", RETIRED_TEXT, c("Continue", "after")),
    a("after", RETIRED_TEXT, c("[Keep holding on.]", flags=(GLOVES,))),
], (TOUCHED, DRAINED), delay=48, chapters=(3, 5))


# --- The chaplain's first sermon ------------------------------------------------------------------------------

hub(SERMON, "On temptation", 3, '"You\'re preaching on Sunday?"', [
    a("start", '''"Tomorrow. The acolyte with the cloak asked me. He said the second company would come to hear me who would never come to hear him, and I said that was a terrible reason to preach, and he said most reasons for preaching are." {n}She has a wax tablet covered in crossed-out lines.{/n}
"I'm going to preach on temptation. It's the only subject I know anything about." {n}She reads.{/n} "'The Abyss does not tempt you with what is evil. It tempts you with what is sweet, and then it tells you that sweet and evil are the same thing. They are not. That is the lie. Everything else it says is true.'"''',
        c("Continue", "doubt")),
    a("doubt", '''{n}She lowers the tablet.{/n} "Is that too much? Is it dangerous, to tell soldiers the Abyss tells the truth about most things? The Iomedaeans say you must never grant the enemy anything." {n}She bites her lip.{/n}
"But I was the enemy. And the worst thing about the enemy is that it isn't stupid. If I tell them it's stupid, they'll believe me, and then the first time a succubus says something clever to them in a dark tent, they'll think, but I was told they were stupid, and they'll be lost."''',
        c('"Preach it exactly like that. The truth is the only thing that works."', "preach", flags=(SERMON,)),
        c('"Add a joke. Soldiers listen to anything with a joke in it."', "joke", flags=(SERMON,))),
    a("preach", '''"Exactly like that." {n}She nods, slowly, and picks up the stylus.{/n} "Then I'll have to say how I know. Not all of it. But enough." {n}She looks frightened, and certain.{/n} "Come and sit at the back. If I stop in the middle, cough. I'll know it's you."''', c()),
    a("joke", '''{n}She stares at you, and then, grimly, writes something at the bottom of the tablet.{/n} "'A succubus, a paladin and a Trickster walk into a tavern.'" {n}She looks up.{/n} "I don't know how it ends. You'll have to tell me. Come and sit at the front, and if I stop in the middle, you can finish it for me."''', c()),
], (CHAPLAIN, CENSER), delay=48, chapters=(3, 5))


# --- After the yes: the second chair ------------------------------------------------------------------------------------

hub(CHAIR, "The second chair", 5, '"You bought furniture?"', [
    a("start", '''{n}She has. There is a chair in her room by the chapel that was not there yesterday: a plain Drezen kitchen chair, ash wood, with a rush seat, standing across the little table from her own. She is standing behind it with both hands on its back, as if introducing it.{/n}
"You know I grew up in Lady Vellexia's house. All those chairs at her table, and nobody eating." {n}She pats the chair.{/n} "So I bought one, from the joiner on Coppersmith Lane, with my own coin, for one particular person to sit in. It's for you. It's yours. Nobody else sits in it unless you bring them."''',
        c("Continue", "why")),
    a("why", '''"In the Upper City a chair at the table meant you might be dinner." {n}She runs her thumb along the rush seat, where the joiner's chalk mark still shows.{/n} "Here it means you're expected. I bought it for you, and I'm already sorry I showed it to you." {n}She lets go of it.{/n} "Sit down. Let's see if it works."''',
        c("[Sit in the chair.]", "sit", flags=(CHAIR,)),
        c("[Turn the chair round and sit astride it, arms on the back, like a soldier in a mess tent.]", "astride", flags=(CHAIR,))),
    nar("sit", '''{n}You sit. The rush seat creaks. She sits down opposite you in her own chair, very carefully, and puts her hands flat on the table, and looks at you across it the way you have seen her look at the net-menders' bench, and the bakery, and the cat.{/n}
"It works," she says, very quietly. "Nobody at this table is the one being eaten. It works."''', c()),
    a("astride", '''{n}She stares at you, then laughs so hard she has to hold on to the table.{/n} "You're impossible. I buy you a chair, the first chair I have ever bought anyone, and you sit on it backwards." {n}She turns her own chair round and sits on it the same way, facing you over its back, chin on her folded arms.{/n} "There. Now it's a proper table. A barracks table. I've always wanted one of those."''', c()),
], (COMMITTED, MORNING), delay=48, chapters=(5,))


# --- The novice's hymn (day thirty-three on her list) -----------------------------------------------------------

hub(NOVICE, "What the novice hums", 3, '"You were in the chapel before dawn again."', [
    a("start", '''"Sweeping. With the novice. He hums while he sweeps, the same four bars, over and over, and I put it on my list as number thirty-three, and this morning I asked him what it was." {n}She is still holding a broom, and does not seem to have noticed.{/n}
"He didn't know. His grandmother hummed it. He doesn't know the words or where it comes from or what it's for. He just hums it while he sweeps, because she did." {n}She looks at the broom.{/n} "So now I hum it too. I don't know the words. I don't know what it's for either, and I can't stop."''',
        c("Continue", "hum")),
    a("hum", '''{n}She hums it for you, the four bars, badly, twice through. It is nothing: a scrap of a lullaby, or a work song, or a hymn that lost its words somewhere between a grandmother and a boy.{/n}
"In the Abyss, nothing is kept unless it's useful. You keep a slave for his hands, a spy for her tongue, a song for what it makes people do." {n}She leans on the broom.{/n} "This isn't useful. It doesn't make anyone do anything. He hums it because she did. That's all. I think that might be the most mortal thing I've found yet."''',
        c('"It\'s allowed. That\'s what most of what people keep is for."', "keep", flags=(NOVICE,)),
        c("[Hum it back to her, worse.]", "worse", flags=(NOVICE,))),
    a("keep", '''"For nothing." {n}She smiles slowly.{/n} "For remembering the person who hummed it first." {n}She props the broom against the wall, very carefully, as if it too were a thing to be kept.{/n} "Then I'll keep it for the novice. And his grandmother. And whoever taught her. A whole line of people I'll never meet, humming while they sweep."''', c()),
    nar("worse", '''{n}You hum it back. You are tone-deaf and you get the third bar wrong. She winces, visibly, and then laughs, and hums it again, correctly, pointedly, and you hum it wrong again on purpose, and by the end the novice is standing in the chapel door with his broom, staring at the Commander of the crusade and the chaplain's demon humming at each other like two cats on a wall.{/n}''', c()),
], (MEALTIMES, RX_WANT), delay=48, chapters=(3, 5))


# --- The rainy day (day thirty-six: to be bored) ---------------------------------------------------------------

hub(RAIN, "Nothing happening", 5, '"It\'s raining."', [
    a("start", '''"It is." {n}She says it with deep satisfaction. She is lying on her cot with her boots off and her wings spread across the blankets like a second cloak, watching the rain run down the shutters.{/n}
"Number thirty-six. I want to be bored. And today there's no march, no council, no drill, the second company's confined to barracks, and it's raining." {n}She turns her head on the pillow to look at you.{/n} "I've been lying here for three hours doing nothing, and nobody wants anything, and I'm not hungry, and I'm not afraid. Is this it? Is this boredom?"''',
        c("Continue", "stay")),
    a("stay", '''"It's wonderful." {n}She sounds almost frightened by how wonderful it is.{/n} "I keep expecting someone to call for me, and nobody does. In the Abyss, every moment is a move in a game. In the crusade, every moment is a war. This is the first moment that isn't anything." {n}She pats the edge of the cot.{/n} "Stay. Be bored with me. Doctor's orders. Mine, this time."''',
        c("[Lie down beside her and watch the rain.]", "lie", flags=(RAIN,)),
        c("[Sit on the floor with your back to the cot, and report on the rain.]", "floor", flags=(RAIN,))),
    nar("lie", '''{n}You lie down beside her, on top of the blankets, careful of the wings. Neither of you says anything for a very long time. The rain goes on. Somewhere a bell rings the hour, and then the next hour. At some point she takes your hand through a fold of the blanket, the way she has learned to, and neither of you lets go.{/n}
"This," she says eventually, drowsily, "is the best thing I have ever been prescribed."''', c()),
    nar("floor", '''{n}You sit on the floor with your back against the cot and read the rain aloud in the voice of a staff officer delivering a situation report. "Rain, ongoing. Strength, moderate. Enemy intentions, unknown." She laughs into the pillow until she has to wipe her eyes, and then goes quiet, and then, to her own astonishment, falls asleep.{/n}
{n}She does not sleep, as a rule. You sit very still, so as not to wake her, until the rain stops.{/n}''', c()),
], (FORTY, MORNING), delay=24, chapters=(5,))


# --- The sea map (after the temple's stone) --------------------------------------------------------------------

hub(SEA_MAP, "Coastlines", 5, '"What are you reading?"', [
    a("start", '''{n}A map, spread across her camp table and held down at the corners with the daybook, a candle, the river stone and one of her boots. It is a chandler's chart of the rivers south out of Mendev, down through Lake Encarthan to the sea, and she has marked it all over in charcoal.{/n}
"I'm planning. For after. When the Wound is closed." {n}She traces a line with her finger.{/n} "Down the river, then the lake, then the long portage, then the river again, all the way down. Four months, the chandler said, if the weather's kind. This is the first journey I've planned simply because I want to go."''',
        c("Continue", "stone")),
    a("stone", '''{n}She picks up the stone and holds it up to the candle, so the white band glows.{/n} "Ilvanne wanted to see the sea. The Mother said to take her there, and never to write again. I've been thinking: she told me to stop writing. She didn't tell me to stop asking. I think asking might be the thing I do now instead of taking."
"But I want to take her. And I want..." {n}She stops, and starts again.{/n} "I want company. On the river. Four months is a long time to be alone with a stone and a list."''',
        c('"I\'ll come. We\'ll argue about the portage the whole way."', "come", flags=(SEA_MAP,)),
        c('"Bring the cat. It\'s the only one of us who won\'t get seasick."', "cat", flags=(SEA_MAP,))),
    a("come", '''"You'll come." {n}She presses the stone against her mouth.{/n} "For some of it. I know you can't come for all of it. There'll be a world to put back together, and you'll be needed." {n}She smiles.{/n} "Some of it. The last bit. When the river opens out and you can smell salt. Be there for that bit. That's all I'm asking."''', c()),
    a("cat", '''{n}She laughs, the startled laugh, and nearly knocks the candle over.{/n} "The cat! The cat would hate it. The cat would sit in the bow and glare at the water for four months and scratch anyone who tried to fish." {n}She is already marking something on the map, a tiny charcoal cat in the bow of a tiny charcoal boat.{/n} "Yes. The cat comes. And you come, for the last bit, when you can smell salt."''', c()),
], (TEMPLE_LETTER, MORNING), delay=24, chapters=(5,))


# --- The returned: Sosiel's offer -----------------------------------------------------------------------------

hub(SOSIEL_OFFER, "A kinder man's offer", 3, '"I went to see Sosiel."', [
    a("start", '''"About his offer. That if I ever need it again, I should come to him first, because he has more to spare." {n}She is sitting very upright, hands folded, like someone who has come to give notice.{/n}
"I went to tell him no. He's the kindest man in this army, and he meant every word, and he'd have held out his arm to me and prayed to Shelyn while I drank. And I sat in his tent and I couldn't say it. So I said it to his lute instead, which was propped in the corner, and he pretended not to hear me, which was kind too."''',
        c("Continue", "why")),
    a("why", '''"Do you know why I said no?" {n}She looks at you, then at her hands.{/n} "Because he'd forgive me. Instantly, before I'd finished the sentence. He'd bandage his own arm and ask if I wanted tea. And I'd take it, every time, because it would be so easy, and one night I'd come to his tent and not bother to knock." {n}She twists her hands together.{/n}
"And you. In the chapel, you looked at me on that bier and you said I was starving, as if it were a..." {n}She stops. Starts again.{/n} "That isn't it. You didn't... I mean, you did, but that isn't why." {n}Her mouth closes on it.{/n} "I had this worked out on the way over. It was about why I came to you and not to him, and it was..." {n}She glares at the door as if the rest of it went out through it.{/n} "Don't make me look for it."''',
        c('"Keep your sentence. I\'ll be insufferable at you until you find it."', "hard", flags=(SOSIEL_OFFER,)),
        c('"Go back and thank him properly. He\'d want to know you chose."', "thank", flags=(SOSIEL_OFFER,))),
    a("hard", '''{n}She laughs, and it breaks something in her shoulders loose.{/n} "Insufferable. Yes. Everybody says so. The quartermaster keeps a list." {n}She stands.{/n} "Be insufferable at me, then. For a long time. And when I go back to Sosiel, it'll be to learn the lute, not to eat."''', c()),
    a("thank", '''"He'd want to know I chose." {n}She nods slowly.{/n} "Yes. He would. He'd rather I walked away from him on my own feet than came crawling to his tent too hungry to say anything at all." {n}She stands.{/n} "I'll go back tomorrow. With a set of strings for his lute; I've heard the third one buzz. I know how to buy a man's cooperation. This isn't that."''', c()),
], (AFTERTASTE,), delay=48, chapters=(3, 5))


# --- The fallen: one sincere question -------------------------------------------------------------------------

OTHER_NODES = [
    a("start", '''"I'm thinking. Don't tease; it happens." {n}She is turning her cup round and round on the table, and she has not drunk from it.{/n}
"Your crusade. Your soldiers, your chapel, your ridiculous city with its bakeries and its cats. I was part of it, once. The other one of me." {n}She says 'the other one' as if it were someone she had met at a party and disliked.{/n} "I've been laughing at her. At her little vows and her little prayers and her counting of days."''',
        c("Continue", "question")),
    a("question", '''{n}She stops turning the cup.{/n} "Tell me one thing, and don't lie, because I'll know, I always know." {n}Her voice is flat and careful.{/n} "Was she happy? The other one. The one who said no to everything. At the end, before she fell. Was she ever, once, happy?"''',
        c('"Yes. Sometimes. It was hard, and she was, sometimes."', "yes", flags=(OTHER_ONE,)),
        c('"No. She was starving the whole time."', "no", flags=(OTHER_ONE,))),
    a("yes", '''{n}Something moves in her face, and is gone.{/n} "Sometimes." {n}She drinks, finally, the whole cup.{/n} "Then she was a fool. Being happy sometimes, when you could be satisfied always." {n}She sets the cup down, very precisely.{/n} "Don't ever tell me that again. I'll think about it for a hundred years."''', c()),
    a("no", '''"Good." {n}She says it too quickly.{/n} "Good. Then I did the right thing. I chose to be fed instead of pure, and pure was never going to make me happy anyway." {n}She pours another cup.{/n} "You're lying, of course. You lie prettily. Keep doing it; it amuses me."''', c()),
]
for hub_key, suffix, extra, unit in DREZEN_PLACES:
    SCENES.append(scene(OTHER_ONE + suffix, "The other one", "Arueshalae", 5, '"You\'re quiet tonight."',
                        [dict(nd) for nd in OTHER_NODES],
                        requires=("trickster.ever", RETURNED, EVIL_DEAD, REUNITED, *extra),
                        forbids=(CLOSED, ALLY, OTHER_ONE, OTHER_ONE + "_yard"), delay=24, last=5, optional=True,
                        Relationship="arueshalae", Areas=[DREZEN], Chapters=[5], ContactUnit=unit,
                        InteractionHub=hub_key))


# --- The scar (after the cat) ---------------------------------------------------------------------------------

hub(SCAR, "Do succubi scar?", 3, '"Let me see your hand."', [
    a("start", '''{n}She holds it out at once, back uppermost, as if she had been waiting for weeks for someone to ask. Across the knuckles, where the smithy cat caught her, there is a thin white line.{/n}
"It scarred." {n}She says it the way another woman might say she was with child.{/n} "I asked, remember, whether succubi scar. I didn't know. I expected it to be gone in a day, the way everything else has gone."''',
        c("Continue", "mark")),
    a("mark", '''"And this did." {n}She runs her thumb along it.{/n} "A cat did this, because it liked me, and it stayed. A smithy cat that I bought a fish for, and it leaves a mark on me that I can still find with my thumb a month later."
{n}She looks at you, her eyes very bright.{/n} "I wanted it to stay. Desna help me, I still do."''',
        c('"It isn\'t mad. It\'s the first thing you\'ve kept that nobody gave you a use for."', "keep", flags=(SCAR,)),
        c('[Spend a Scroll of Death Ward: have the chaplain read it over you at the shrine door, come back, and kiss the scar]', "kiss", flags=(SCAR,), forbids=(ELYSIUM,),
          requires=(WARD_HELD,), remove_item=SCROLL),
        c('[Kiss the scar, lightly]', "kiss_e", flags=(SCAR,), requires=(ELYSIUM,))),
    nar("kiss_e", '''{n}You lift her hand and kiss the white line, lightly, once. Nothing comes out of you. Nothing at all. She stares at the place your mouth was as if she had expected to see frost on it.{/n}
"Now it's got two things in it," she says, unsteadily. "The cat, and you. And it didn't cost you anything. I'll never get used to that. I'm not going to try."''', c()),
    a("keep", '''"The first thing I've kept that nobody gave me a use for." {n}She holds the hand against her chest.{/n} "The list is like that, too. I'm collecting them, aren't I? Useless things. I'm going to be the most cluttered demon in the history of the Abyss." {n}She laughs.{/n} "Good."''', c()),
    nar("kiss", '''{n}She watches you walk to the shrine door and back with the ward read over you, seal to last word, for this, and her mouth opens to stop you and does not. Then you lift her hand and kiss the white line, lightly, once. Nothing comes out of you. She goes very still, and then she takes her hand back, slowly, and looks at the scar as if it had changed colour.{/n}
"You spent a horse on a cat scratch." {n}Her voice is unsteady.{/n} "Now it's got two things in it. The cat, and you. It'll never heal now. I won't let it."''', c()),
], (CAT,), delay=48, chapters=(3, 5))


# --- The chaplain prays -------------------------------------------------------------------------------------

hub(PRAYER, "Asking", 5, '"You were at the altar a long time."', [
    a("start", '''"I prayed." {n}She says it as if confessing to a theft.{/n} "To Desna. For myself, this time, not for anyone at the rail. I told you once that I try not to trouble her. That she'd done more for me than I deserved and asking more would be impudent."
"But I'm the chaplain now. The second company asks me to pray for them every day. And it seemed very rude to keep asking her for things on their behalf when I'd never once asked her anything on my own."''',
        c("Continue", "what")),
    a("what", '''"So I knelt, and I told her about the censer, and the boy who ran at Kenabres, and the soldiers at the rail. And then I told her about you." {n}Her mouth twists.{/n} "I said, 'Tender of Dreams, the Commander has made me into a chaplain as a joke, and I have been doing it properly, and I think the joke is on both of us.'"
"And then I asked her what I dream of. She asked me first, a long time ago. I thought it was time I asked her back."''',
        c('"What did she say?"', "said")),
    a("said", '''"Nothing." {n}She smiles.{/n} "She never does, not out loud. But I sat there for an hour, and nothing happened, and I wasn't hungry, and I wasn't afraid, and when I got up the second company was waiting at the rail with their swords, and one of them said, 'Chaplain, you look like you've been somewhere nice.'"
{n}She lifts her hands, and drops them.{/n} "So I think she answered. I think the answer was, 'Go and bless their swords.' Which is a very Desnan answer. She likes people to find out for themselves."''',
        c("[Walk her back to the rail.]", flags=(PRAYER,))),
], (CHAPLAIN, CENSER), delay=48, chapters=(5,))


# --- The fallen: a wager. RETIRED by gating (2026-10-01; ids and indices kept): its stakes were never settled. ----

BET_NODES = [
    a("start", RETIRED_TEXT, c("Continue", "stakes")),
    a("stakes", RETIRED_TEXT,
        c("[Accept the wager.]", "dream", flags=(BET,)),
        c("[Refuse the wager.]", "never", flags=(BET,))),
    a("dream", RETIRED_TEXT, c()),
    a("never", RETIRED_TEXT, c()),
]
for hub_key, suffix, extra, unit in DREZEN_PLACES:
    SCENES.append(scene(BET + suffix, "A wager", "Arueshalae", 5, '"You\'re smiling. I don\'t like it."',
                        [dict(nd) for nd in BET_NODES],
                        requires=("trickster.ever", RETURNED, EVIL_DEAD, REUNITED, *extra),
                        forbids=(CLOSED, ALLY, COMMITTED, BET, BET + "_yard"), delay=24, last=5, optional=True,
                        Relationship="arueshalae", Areas=[DREZEN], Chapters=[5], ContactUnit=unit,
                        InteractionHub=hub_key))


# Q11: after the native Elysium ending (BestEnding; her touch no longer drains) the sessions that stage a drain close.
for _scene in SCENES:
    if _scene["Id"] in (TEACH, GLOVES, SOSIEL_OFFER) and ELYSIUM not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM)
    # Sol verify (2026-10-01): staged at a Drezen place (her room by the chapel; the shrine door), so only in Drezen.
    if _scene["Id"] in (CHAIR, SCAR):
        _scene["Areas"] = [DREZEN_AREA]


def integrate(payload):
    """Scenes only; keys bind on demand through trickster_world."""
