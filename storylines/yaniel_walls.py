"""Yaniel's courtship on the Trickster path (11-ROSTER-PLAN-2 §2, Yaniel build sheet): her letter from Nerosyan (Chapter 3),
the Commander alone with her iron in the Abyss (Chapter 4), and her Chapter 5 visits in Drezen, all rest-delivered because
no chapel or presence anchor is free for her (10 §5.2). The device, the verdict, the commit, the niche, the pages and the
reactions live in yaniel_trickster.

Canon anchors used here: the Half Measure's roast and the old tree by the town hall in Nerosyan (TrueYaniel/Cue_0035
efb1ee54); the statue (Cue_0044 7c1becd8, and Seelah's "the hands of the Yaniel statue"); Staunton Vhane and his brother
Joran, who made Radiance, going over to Minagho and dying for it (Cue_0030 5a28c5c2, Answer_0029 09d9caa5; Joran's brand on
the blade); Areelu, who gave her to Minagho "tired of my obstinacy" (Cue_0023 e8756562) and wore her face in the Drezen
citadel (FakeYaniel_First/Cue_0032 1ed1497d, FakeYaniel_ToAreelu/Cue_0001 7418d421); Minagho's collection (Cue_0021
7db27044). The Minagho scene reads the merged minagho_chivarro route (a started flag and presence facts, never a Forbids).
"""
from story_format import c, n
from storylines import yaniel_trickster as yt
from storylines.yaniel_trickster import (B_AREELU, B_BOUT, B_CHURCH, B_NIGHT, B_PRAYER, B_RAID, B_REFUGEE, B_ROAST,
                                         B_STATUE, B_STAUNTON, B_WALLS, HUSK_BOUGHT, HUSK_FREED, HUSK_LEFT, NICHE, CARRIES, CLOSED,
                                         COMMITTED, CUFF_PACKED, CUFF_WORN, JUDGES, KILLED, MINAGHO_SECRET, MINAGHO_SEEN,
                                         MINAGHO_TOLD, RETURNED, STATUE_LIED, SWAPPED, TOLD_STATUE, TOLD_STAUNTON, UNMASKED,
                                         FAKE_FREED, FAKE_REFUSED, WHY_BACK, WHY_CANT, Y, nar, visit, yn)

SCENES = yt.SCENES   # appended in order: the route's rest delivery keeps authored order within a relationship

CH3_READ = Y + "ch3_read"
CH4_SEEN = Y + "ch4_seen"
BOUT_DIRTY = Y + "bout_dirty"
MC = "minagho_chivarro.trickster."
MINAGHO_HERE = Y + "minagho_here"     # Derived (yaniel_trickster.DERIVED is extended below): Minagho sits in Drezen
AREELU_COURTED = "areelu.started"      # node variant only: the Commander is keeping Areelu's company


# --- Chapter 3 (T): a letter from Nerosyan -------------------------------------------------------------------------------

visit(Y + "ch3.nerosyan", "The Half Measure", [
    nar("start", '''{n}A letter finds you three days after the Fane, carried up from the south by a Mendevian courier who says the woman who gave it to him paid him in advance, in old coin, and told him the Commander would know her by her hand. The hand is square and upright, pressed hard into the paper, as if its owner did not trust ink to stay where it was put.{/n}''',
        c("[Read it.]", "one")),
    yn("one", '''"Commander,
"The Hand of the Inheritor knew me. I did not expect that. I thought, after seventy years, that a herald would have to be told. He looked at me the way you look at a letter you have been waiting a long time for, and then he put his hand on my head, and I am not going to write down what I did then.
"They brought me up out of the Fane and put me on a cart for Nerosyan with the wounded, because I would not stay in a bed. I have been in Nerosyan four days."''',
       c("Continue", "carries", requires=(CARRIES,)),
       c("Continue", "judges", requires=(JUDGES,), forbids=(CARRIES,)),
       c("Continue", "refused", forbids=(CARRIES, JUDGES))),
    yn("carries", '''"I carried Radiance through the gate on my hip. You should have seen the guards' faces. A priest stopped me in the street and asked me, very kindly, where I had stolen it. I told him I had it from a thief. He did not know what to do with that at all.
"Three more priests have been to my lodging since, each more senior than the last, to explain to me that the sword belongs to the Church and ought to go back to a reliquary. I told the last of them that the Church had seventy years to come and fetch it off me and did not, and that now it was mine again by gift of the Commander of the crusade, and he could take it up with you. So he may write to you. I apologise in advance. I do not apologise very much."''',
       c("Continue", "half")),
    yn("judges", '''"I went through the gate with nothing on my hip. I bought a sword in the market, a plain one, too light, with a grip made for a man's hand. It will do until something better tries to kill me.
"Every night I think of the other one on your hip, and the oath on it, and I find I sleep better than I have any right to. That is a strange thing to be able to say about a stranger who robbed me."''',
       c("Continue", "half")),
    yn("refused", '''"I still have my iron. I have tried to leave it off three nights running, and three nights running I have got up in the dark and put it back in my belt. I am telling you this because you are the only person in the world who would understand why it is funny, and because I do not know anybody else's address.
"You kept your sword. I hope you keep it well. I should have liked, I think, to watch you do it."''',
       c("Continue", "half")),
    yn("half", '''"The Half Measure is still there. I stood in the street outside it for most of an afternoon before I could go in. The board over the door is new and the stairs are the same. They do not serve the roast any more. The cook who made it died forty years ago, and her daughter after her, and the girl behind the counter now had never heard of it. I told her how it was done, as near as I remembered, and she wrote it down on a slate, and made a face.
"The old tree by the town hall is in leaf, and not in bloom. I stood under it anyway. It is a great deal bigger than it was. So, I suppose, am I, in the wrong direction."''',
       c("Continue", "statue")),
    yn("statue", '''"They have a statue of me in the cathedral square. You did not tell me that. Stone, twice my height, with Radiance held up at the sky and a face on it like a girl who has never been hungry. The pilgrims leave candles at its feet. I went and stood among them one evening with my hood up. An old woman next to me was praying for her grandson at the front, to me, and I stood there beside her and did not know what to do with my hands.
"The chaplains are taking it down next week and sending it up to Drezen on an ox-cart, because Drezen is ours again and the martyr ought to go home. I am going to Drezen too. I would like to get there before my statue does. I would like, if you are anywhere near the city, to see what you have done with my iron.
"Y."''',
       c("[Fold the letter away.]", flags=(CH3_READ,))),
], requires=("trickster.ever",), forbids=(CH3_READ,), delay=72, kind="letter", chapters=(3,), areas=(),
    RequiresAnyGroups=[[SWAPPED, yt.FANE_REFUSED]])


# --- Chapter 4 (T): the Commander alone in the Abyss with her iron ---------------------------------------------------------

visit(Y + "ch4.shackle", "Husk-iron", [
    nar("start", '''{n}Somewhere in Alushinyrra a bell is ringing that has never rung for anything good. You cannot sleep. You have been lying on a stranger's bed in a city that sells people by the pound, listening to it, and at some point your hand went into your pack of its own accord and came out with her iron.{/n}
{n}It is heavier than it looks. Minagho's smiths did not waste craft on it; it was hammered out of a bar and bent round a wrist while it was hot, and you can see, on the inside, where the metal has been worn bright and thin by seventy years of the same bone moving against it. The sheared link hangs from the eye and knocks against your knuckles when you turn it.{/n}''',
        c("Continue", "city")),
    nar("city", '''{n}Minagho is somewhere in this city. You have heard her name in two taverns and a slave market since you came through the rift. Everybody in Alushinyrra knows the lilitu who collects things. Some of the things she collected are hanging in her lairs still, and some are on hooks in places nobody will tell you about, and one of them is standing a watch on the walls of Drezen because you took this off her wrist.{/n}''',
        c("Continue", "why_cant", requires=(WHY_CANT,)),
        c("Continue", "why_back", requires=(WHY_BACK,), forbids=(WHY_CANT,)),
        c("Continue", "choose", forbids=(WHY_CANT, WHY_BACK))),
    nar("why_cant", '''{n}"So you can't put it back on," you told her. It was a good line. It was even true. It has not, until now, occurred to you that the iron would have to go somewhere once it was off her, and that somewhere would be you.{/n}''',
        c("Continue", "choose")),
    nar("why_back", '''{n}"So you have to come back for it," you told her. A hostage, she called it. You thought it was a clever move at the time, the kind that puts a piece on the board where the other player has to come and take it. Lying here, you are no longer certain which of you is the piece.{/n}''',
        c("Continue", "choose")),
    nar("choose", '''{n}The bell stops. In the quiet you can hear the city breathing through the walls: a laugh, a cry, somebody bargaining in a language that sounds like knives being sharpened. The cuff is warm now from your hand.{/n}''',
        c("[Close it on your own wrist.]", "worn"),
        c("[Wrap it in a clean cloth and put it back at the bottom of the pack.]", "packed")),
    nar("worn", '''{n}It goes round your wrist the way it went round hers: badly. The edge bites. The pin will not go all the way in, because she hammered it too many nights, and in the end you bend the soft end over with the pommel of your knife and leave it like that.{/n}
{n}In the morning your companions look at it, and at you, and one by one decide not to ask. In the market that afternoon a slaver with a jackal's head takes one look at your wrist and marks you up, loudly, as somebody's escaped property, and three of his cousins spend the rest of the day finding out that you are not.{/n}''',
        c("[Leave it on.]", flags=(CUFF_WORN, CH4_SEEN))),
    nar("packed", '''{n}You fold it into a strip of clean linen, the way a chaplain folds a relic, and put it at the very bottom of your pack, under the maps and the spare boots, where you will know it is there every time you lift the pack and not otherwise.{/n}
{n}It is a small thing to carry through the Abyss. It weighs more than you want it to. You have been given worse loads by better people, and none of them was ever warm from the hand.{/n}''',
        c("[Sleep, if you can.]", flags=(CUFF_PACKED, CH4_SEEN))),
], requires=("trickster.ever", SWAPPED), forbids=(CH4_SEEN,), delay=48, kind="memory", chapters=(4,), areas=())


# --- Chapter 5 (T): Minagho (the pivotal moral node: tell her, or keep it) ---------------------------------------------------

visit(Y + "ch5.minagho", "The lilitu on the crate", [
    nar("start", '''{n}Yaniel does not come up to your rooms. She sends a boy to ask you to the east wall, and when you get there she is standing at the broken parapet of the gate tower with her back to the city, the way a sentry stands when she does not trust what is behind her.{/n}''',
        c("Continue", "here", requires=(MINAGHO_HERE,)),
        c("Continue", "heard", forbids=(MINAGHO_HERE,))),
    yn("here", '''"There is a lilitu sitting on a crate by your quartermaster's stores." {n}Her voice is perfectly flat.{/n} "Eyeless. Pretty, if you like knives. I walked past her this morning on my way to the wall. She was turning one of the crusade's daggers over in her fingers, and she heard my boots, and she lifted her face the way she used to when she came into the room with the hooks, and she smiled."
"She knew my step, Commander. After seventy years she knew my step. And nobody in this city will tell me why she is sitting in the middle of it, untouched, with a crusade dagger in her hand, except that it is the Commander's business."''',
       c("Continue", "ask")),
    yn("heard", '''"There is a madam from Alushinyrra on your quartermaster's bench," {n}she says,{/n} "and every sentry in the gate tower knows why. She asks after a lilitu by name. Minagho. And your people run her errands, and your quartermaster does not look round when she talks, and nobody in this city will tell me what the Commander of the crusade wants with the creature who kept me on a hook, except that it is the Commander's business."''',
       c("Continue", "ask")),
    yn("ask", '''{n}She turns round at last. Her face is quite calm. Her hand is on the parapet, and the knuckles are white.{/n}
"She took Staunton. She took Drezen. She took me, and hung me up in her collection between a Sarkorian witch and a boy from Kenabres who screamed for his mother for eleven years. Minagho liked to wake me and tell me things. That everyone had forgotten me. That my goddess had given me up."
"So I am asking you, Commander, since you are the one person in this city who has not lied to me yet. What is she to you?"''',
       c('[Tell her the truth] "She\'s in my bed, Yaniel. And in my debt. That\'s what she is to me."', "truth"),
       c('[Keep it from her] "Nothing you need to carry. Leave her to me."', "hide", alignment=("Chaotic", 1))),
    yn("truth", '''{n}She does not move. For a while the only thing that moves is the wind, pulling at her cloak.{/n}
"In your bed." {n}She tastes it the way you might taste something to find out whether it has been poisoned.{/n} "And in your debt. So she is yours, the way I was hers." {n}A short, ugly laugh.{/n} "No. I do not believe that. Nobody owns Minagho. She owns things. I would know."
"I will not ask you to choose. I watched a better soldier than me try to make someone choose between Minagho and everything else, and he chose her, and Drezen burned." {n}Her voice does not change.{/n} "I am telling you what I will do. I will stand my watch. I will not cross that courtyard by the quartermaster's stores. And if she ever touches me again, in any way, for any reason, I will kill her, Commander, and I will not ask your leave, and I will not be sorry."''',
       c('"That\'s fair."', "truth_end"),
       c('"She won\'t touch you."', "truth_end")),
    yn("truth_end", '''{n}She looks at you for a while, the way she looks at the ash from the wall: as if something might come out of it, and she means to be ready.{/n}
"Thank you for not lying," {n}she says at last.{/n} "It is the worst thing anyone has told me since I came up out of the pit, and you told it to my face. That counts for something. I am not yet sure what."''',
       c("[Leave her to her watch.]", flags=(MINAGHO_SEEN, MINAGHO_TOLD))),
    yn("hide", '''{n}Her eyes stay on yours for a long time. You hold them. Whatever she is looking for, you do not give it to her.{/n}
"Leave her to you." {n}She repeats it slowly.{/n} "That is what they told me in the Fane, the ones who came to feed us. 'Leave it to the mistress.' It is a thing people say when they know something they do not mean to tell you."
{n}She turns back to the parapet.{/n} "Very well, Commander. I will leave her to you. I will not cross that courtyard. I will stand my watch, and I will watch your hands, and one day I will find out what they have been holding. Go on. I have work."''',
       c("[Go.]", flags=(MINAGHO_SEEN, MINAGHO_SECRET))),
], requires=("trickster.ever", RETURNED, "minachiv.started", Y + "minagho_known"), forbids=(MINAGHO_SEEN,))


# --- Chapter 5 (T): the courtship, before the commit ------------------------------------------------------------------------

BEAT = dict(forbids=(COMMITTED,), optional=True)

visit(Y + "beat.walls", "The city as it was", [
    nar("start", '''{n}She is waiting for you at the foot of the gate tower after the second bell, and she walks you along the east wall in the dark without saying where you are going. Every so often she stops, and puts her hand on the parapet, and looks down into the city.{/n}''',
        c("Continue", "one")),
    yn("one", '''"There." {n}She points down at a roofless shell where the soldiers now keep their mules.{/n} "That was a bakery. Brown bread and poppy-seed rolls. The baker had a daughter who threw flour at the garrison when we came off watch, and her father let her, because he said the men needed to be told they were not heroes at least once a day."
"And there. A chapel of Torag. Staunton prayed there before he went on watch. Very loudly. You could hear him up here." {n}Her hand moves along the stone.{/n} "And there, where the demons have been burning their rubbish, there was a fountain. Somebody painted me by it once, the summer before the city fell. I was vain about it for a month."''',
       c('"What was it like, on the last day?"', "last"),
       c('"Were you happy here?"', "happy")),
    yn("last", '''"Loud." {n}She says it at once, as if she had been waiting for somebody to ask.{/n} "People think it was screaming. It was bells. Every bell in the city going at once, and nobody ringing them in time, so it sounded like the whole of Drezen falling down a stair. We had carts in the east road three deep. I had forty knights at this gate at dawn and eleven by noon."
"I kept thinking, when the last cart is through, I will turn round and look at the city properly one more time. I never did. There was always one more cart." {n}She looks down at the mule pens.{/n} "I am looking now. It is not as good as I remembered."''',
       c("Continue", "you")),
    yn("happy", '''"Happy." {n}She considers it.{/n} "I was young, I was good at my work, I was vain about my hair, and I was fairly sure the goddess was pleased with me. Everyone I loved was inside these walls. I thought that was what happy felt like, and that it would go on, and that the crusade would be won by the time I was fifty."
"So yes. I was happy. I was a fool, and I was happy, and I would not trade either one back for anything Minagho ever offered me, and she offered me a great deal."''',
       c("Continue", "you")),
    yn("you", '''{n}She turns from the city and leans back against the parapet, and looks at you instead.{/n}
"And you? Nobody on this wall knows anything about you that did not come out of a song. The sentries say you fell into a hole under Kenabres and came out something more than mortal, and that you laugh at gods. That is two facts and a rumour. I want a fourth thing."''',
       c('"I laughed at a god once. I\'m not sure it was a good idea."', "laugh"),
       c('"I don\'t know what I am. I\'m finding out on the way."', "way"),
       c('[Flirt] "The fourth thing is that I\'ve been thinking about you since the Fane."', "flirt")),
    yn("laugh", '''"Once." {n}Her eyebrows go up.{/n} "Only once? The sentries have you down for three a week." {n}She shakes her head.{/n} "I prayed to mine every day on that hook, Commander, even the days I hated her. Especially those. I never once laughed at her. I think I would have liked to. I think she might have liked it too."''',
       c("Continue", "end")),
    yn("way", '''{n}She nods slowly, as though you had given the right answer in a drill.{/n}
"That is how I found out what I was. On the way. Minagho found out on the way too; she found out I would not break, and it annoyed her very much." {n}Her mouth twitches.{/n} "Do not let anyone finish finding you out before you do, Commander. It is a great waste of a person."''',
       c("Continue", "end")),
    yn("flirt", '''{n}She looks at you for a moment as if you had spoken in the tongue of the Abyss. Then she laughs, low, surprised, and puts her hand over her mouth, like a girl caught laughing in chapel.{/n}
"Since the Fane." {n}The hand comes down.{/n} "You saw me on a hook, gray as a rat, stinking, with seventy years of Minagho on me, and you have been thinking about me since." {n}She shakes her head.{/n} "Either you are a liar, Commander, or you have very strange taste. I have not decided which I would prefer."''',
       c("Continue", "end")),
    nar("end", '''{n}She walks you back to the gate tower. At the foot of the stair she stops, and for a moment you think she is going to say something else. Instead she reaches out and touches your wrist, where the iron sits, or where your pack strap crosses it, with two fingers, the way you might touch a door to see if the fire behind it has gone out. Then she goes up the stair to her watch.{/n}''',
        c("[Go down into the city.]", flags=(B_WALLS,))),
], requires=("trickster.ever", RETURNED), **BEAT)

visit(Y + "beat.statue", "Yaniel of Drezen, the Holy Martyr", [
    nar("start", '''{n}The ox-cart from Nerosyan comes in at the east gate in the middle of the morning, with a crowd of pilgrims behind it and a crowd of chaplains in front, and in the back, lashed upright under a sheet like a bride under a veil, the Holy Martyr of Drezen. The chaplains mean to set her in the niche at the foot of the gate tower until the cathedral is ready for her. The real one has come down off the wall to watch, and has sent for you, and is standing at the back of the crowd with her hood up.{/n}''',
        c("Continue", "sheet")),
    nar("sheet", '''{n}They take the sheet off. The crowd sighs. The statue is twice the height of a woman, painted, with a gilded sword raised to heaven and a face like a girl of twenty who has never been cold or hungry or afraid: smooth, sweet, empty. At its feet the carver has cut, in letters as long as your hand: YANIEL OF DREZEN, THE HOLY MARTYR. SHE HELD THE GATE.{/n}''',
        c("Continue", "told", requires=(TOLD_STATUE,)),
        c("Continue", "look", forbids=(TOLD_STATUE,))),
    yn("told", '''"You told me about this," {n}she says, low, beside you.{/n} "In the Fane. You said it was better to see me in the flesh than to pray in front of a cold stone statue. I thought you were being kind to an old woman on a hook." {n}She looks up at it.{/n} "You were being accurate. It is very cold."''',
       c("Continue", "look")),
    yn("look", '''{n}She stands looking at it while the chaplains bless it and the pilgrims light their candles and a very small boy is lifted up to kiss its stone toe. Her face does not change at all.{/n}
"Tell me the truth, Commander," {n}she says, without turning her head.{/n} "Is it a good likeness?"''',
       c('[Lie] "It\'s a good likeness."', "lie", flags=(STATUE_LIED,)),
       c('"It looks nothing like you."', "truth"),
       c('[Flirt] "It\'s missing the scars. The scars are the best part."', "scars")),
    yn("lie", '''{n}Her mouth twitches. She does not look at you.{/n}
"Liar," {n}she says, very softly, almost fondly.{/n} "You are a terrible liar, Commander, which is strange, because I have been told you are a very good one. Perhaps you only lie badly when it does not matter." {n}She pulls her hood lower.{/n} "Thank you. Nobody has lied to me kindly in seventy years. They only ever did it the other way."''',
       c("Continue", "end")),
    yn("truth", '''{n}She lets out a breath she seems to have been holding since the cart came through the gate.{/n}
"No. It does not." {n}She looks up at the smooth stone face.{/n} "That girl never held anything. She would have dropped the gate and run, and she would have been right to. I did not have the sense." {n}A dry sound.{/n} "The chaplains keep telling me how moving it is. You are the first person in Drezen who has said it to my face. I think I could kiss you for it. I think I will not, in front of the chaplains."''',
       c("Continue", "end")),
    yn("scars", '''{n}She turns her head and looks at you properly, under the hood, for the first time since the sheet came off. Her eyes are very pale in the shadow.{/n}
"The best part." {n}She lets the words sit.{/n} "Minagho gave me most of those. Areelu gave me the rest. You are standing in a crowd of pilgrims, in front of my holy image, telling me the best part of me is the part my torturers made." {n}She draws a long breath.{/n} "That is the most indecent thing anybody has said to me in seventy years, Commander, and I would like you to say it again somewhere with fewer candles."''',
       c("Continue", "end")),
    nar("end", '''{n}The chaplains carry the martyr into the niche and set her on her plinth with her stone sword raised toward the gate tower's ceiling, and a lamp at her feet. The real Yaniel watches them do it. When the crowd has gone she walks up to the niche alone, and stands in front of herself for a while, and then, very deliberately, turns her back on the statue and sits down on its plinth, and takes out a whetstone, and starts on her sword.{/n}''',
        c("[Leave her there.]", flags=(B_STATUE,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

visit(Y + "beat.staunton", "Joran's brand", [
    nar("start", '''{n}She comes down to your rooms after dark, which she has never done, and does not sit. She stands by the hearth with her arms folded and her back to the fire, and says, before you have shut the door:{/n}''',
        c("Continue", "told", requires=(TOLD_STAUNTON,)),
        c("Continue", "learned", forbids=(TOLD_STAUNTON,))),
    yn("told", '''"You told me in the Fane. Staunton and Joran, gone over to the demons, and dead for it. I said I knew. I did know; Minagho told me a hundred times. But I did not believe it until I came up here and asked the quartermaster where Staunton's forge had been, and he spat."''',
       c("Continue", "brand")),
    yn("learned", '''"I asked the quartermaster where Staunton's brother kept his forge. He spat. Then a sergeant with more tact told me the rest: Staunton gone over to the demons, again, at the end, and Joran with him, and both of them dead for it. Minagho told me that a hundred times in the Fane. I did not believe her. I believe a sergeant."''',
       c("Continue", "brand")),
    yn("brand", '''"Joran made Radiance. Did you know that? He put his mark on the ricasso: a hammer inside a sun. He was barely out of his apprenticeship and so proud of it he could not speak. Staunton stood behind him at the presentation and cried into his beard, and pretended it was the smoke."''',
       c("Continue", "carries", requires=(CARRIES,)),
       c("Continue", "judges", forbids=(CARRIES,))),
    yn("carries", '''{n}She draws the sword and holds it out to the firelight, blade flat, so that you can see the mark near the hilt: a small hammer in a small sun, worn nearly smooth.{/n}
"I have been looking at it every night on the wall." {n}Her thumb moves over it.{/n} "I keep thinking I ought to have it ground off. I keep not doing it."''',
       c("Continue", "grief")),
    yn("judges", '''"Show me."
{n}You draw Radiance and hold it to the firelight, and she leans close and finds the mark near the hilt without looking for it: a small hammer in a small sun, worn nearly smooth. She does not touch it.{/n}
"You have been carrying Joran on your hip all this time," {n}she says,{/n} "and I have been carrying Staunton on my wrist, if you think about it. His lilitu's iron. Neither of us asked for it."''',
       c("Continue", "grief")),
    yn("grief", '''"Everyone keeps telling me to mourn him." {n}Her voice is quite level.{/n} "The chaplains. The Hand. Even the sergeant. 'He was your friend; you should grieve.' And I would like to. I would like very much to sit down somewhere and weep for Staunton Vhane the way I wept for my father. But every time I try, I see her. Her hands on his face. Her voice in his ear. And I cannot find him under it."
"She took him first, you see. Before the city. Before me. I am not ready to let what is left of him out yet. I am afraid of what else would come out with it."''',
       c('[Tell her about Staunton] "He was ashamed. Everyone who knew him said so. He never stopped being ashamed."', "ashamed"),
       c('[Say nothing, and stand beside her.]', "silence"),
       c('[Lie] "They say he died fighting her, at the end."', "lie")),
    yn("ashamed", '''{n}She shuts her eyes.{/n} "Ashamed." {n}A long breath.{/n} "Good. No. Not good. But it is him. That is the first thing anyone has told me that sounds like him. Staunton was always ashamed of something; it was how you knew he was paying attention."
{n}She opens her eyes and looks into the fire.{/n} "Thank you. I think I may be able to cry about that one. Not tonight."''',
       c("Continue", "end")),
    nar("silence", '''{n}You say nothing. You stand beside her with your back to the fire, the way she is standing, and look at the dark window, and after a while she leans, very slightly, so that her shoulder is against yours. She does not say anything either. The fire burns down. When she finally moves it is to put her hand on your arm, briefly, the way a soldier touches a comrade's arm in a line before the charge, to know where they are.{/n}''',
        c("Continue", "end")),
    yn("lie", '''{n}She turns her head and looks at you, and you know at once that she knows. Seventy years of being lied to by experts; a Commander's kind lie does not get past her.{/n}
"No, they do not," {n}she says, gently.{/n} "But thank you. That is the second kind lie you have told me. I am beginning to keep a count." {n}She looks back at the fire.{/n} "Do not make a habit of it. I would like one person in this city to tell me the truth about the dead, even if it is you."''',
       c("Continue", "end")),
    nar("end", '''{n}She goes at last, up the stair to her wall. At the door she stops and says, without turning:{/n} "When the war is done, if I am alive, I am going to find where they buried him, and I am going to shout at him for an hour. Come with me. Somebody should stop me when I start to enjoy it."''',
        c('"I\'ll come."', flags=(B_STAUNTON,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

visit(Y + "beat.areelu", "The masquerade", [
    nar("start", '''{n}She is waiting on the gate tower stair with a face like a shut door. A chaplain has been telling her things, she says, in the kind voice chaplains use for bad news. About the siege. About a woman calling herself Yaniel who was found chained in the citadel dungeon when the crusade took Drezen back, and who showed the Commander the way to the Sword of Valor.{/n}''',
        c("Continue", "freed", requires=(FAKE_FREED,)),
        c("Continue", "refused", requires=(FAKE_REFUSED,), forbids=(FAKE_FREED,)),
        c("Continue", "plain", forbids=(FAKE_FREED, FAKE_REFUSED))),
    yn("freed", '''"You freed her. The chaplain said you cut her chains yourself, and she wept, and told you she was a trophy." {n}Her mouth is thin.{/n} "A trophy. That is my word. That was what I was, in the Fane. She took my face and my name and my word, and walked out of a dungeon on your arm with them, and you did not know."
"Of course you did not know. Nobody knew. She is very good. She was very good in the laboratory, too, before she gave me to Minagho because she was tired of my obstinacy."''',
       c("Continue", "areelu")),
    yn("refused", '''"The chaplain said you would not free her. That you left her in her chains and walked on, and the crusade thought you cruel for it, and then it came out who she was." {n}She looks at you with something that is almost respect and almost anger.{/n} "Why? Did you know? Or were you only being careful? Do not answer that. I do not want to find out that you are cleverer than I was."
"She took my face. My name. My word; she told you she was a trophy, the chaplain said. That was what I was, in the Fane. She was very good in the laboratory, too, before she gave me to Minagho because she was tired of my obstinacy."''',
       c("Continue", "areelu")),
    yn("plain", '''"A woman in my face, in my name, telling you she was a trophy. That was my word. That was what I was, in the Fane." {n}Her mouth is thin.{/n} "She was very good in the laboratory, too, before she gave me to Minagho because she was tired of my obstinacy."''',
       c("Continue", "areelu")),
    yn("areelu", '''"Areelu Vorlesh." {n}She says the name the way you might spit out a tooth.{/n} "The Architect. I was on her tables for years before the Fane. I watched her sew demons together and graft demon limbs onto crusaders and call it healing. She never raised her voice once. She would talk to you while she worked about the weather in Sarkoris before the Wound, and her mother's garden."
"And then she put on my face, and walked into my city, and people cried to see me." {n}Her hand goes to her own cheek, as if to be sure of it.{/n} "How many of them do you suppose she killed, wearing it?"''',
       c('"Some. Not as many as she could have. She wanted something from me."', "wanted"),
       c('"None, that I know of. She was looking at me, not them."', "wanted")),
    yn("wanted", '''"She wanted something from you." {n}She almost laughs.{/n} "Of course she did. She always wants something. That is the worst of her, Commander; she wants things the way a scholar wants things, patiently, and she will take your face off to get them and apologise for the mess."''',
       c("Continue", "courted", requires=(AREELU_COURTED,)),
       c("Continue", "end", forbids=(AREELU_COURTED,))),
    yn("courted", '''{n}She looks at you sidelong.{/n} "And they tell me in the square that she has been in your confidence since. That the Architect writes to the Commander, and the Commander writes back." {n}She lifts one hand before you can say anything.{/n} "No. I am not asking. I have had enough of asking about your company for one lifetime. I am telling you that if she ever puts on my face again, anywhere I can see it, I will take it back off her with a knife, and you can tell her that from me."''',
       c("Continue", "end")),
    yn("end", '''{n}She leans her head back against the stones of the stair and shuts her eyes.{/n}
"Do you know what I thought, when I heard it?" {n}Her voice has gone quiet.{/n} "Not about Areelu. About you. I thought: the Commander has already met me once. A Yaniel who wept and was grateful and needed to be led by the hand. And then the real one came up out of the pit, gray and stinking and furious, and would not take her sword back." {n}She opens her eyes.{/n} "I wondered if you were disappointed."''',
       c('"No. The first one was a liar. You\'re the one I robbed."', "robbed"),
       c('[Flirt] "The first one wept. You tried to bite me."', "bite")),
    yn("robbed", '''{n}She laughs, a real one, short and startled out of her.{/n} "The one you robbed. Iomedae help me, that is the nicest thing anyone has said to me since I came back from the dead." {n}She gets up off the stair.{/n} "Go away, Commander. I have to stand a watch, and I cannot do it laughing."''',
       c("[Go.]", flags=(B_AREELU,))),
    yn("bite", '''"I did not try to bite you." {n}A pause.{/n} "I considered it." {n}She gets up off the stair and looks down at you from two steps up, which puts her eyes very nearly level with yours.{/n} "I am still considering it. Go away, Commander, before I decide."''',
       c("[Go.]", flags=(B_AREELU,))),
], requires=("trickster.ever", RETURNED, UNMASKED), **BEAT)

visit(Y + "beat.bout", "Not all enemies", [
    nar("start", '''{n}"Practice swords," says the note under your door. "The court behind the gate tower. First light. Come alone, or I will know you are afraid of an old woman."{/n}
{n}She is there before you with two blunt blades from the armoury and her sleeves rolled to the elbow. Her forearms are ropy and white-scarred. She throws you a sword without warning and it is only luck and a lifetime of bad habits that you catch it by the grip.{/n}''',
        c("Continue", "fight")),
    yn("fight", '''"Seventy years on a hook," {n}she says, circling,{/n} "and not a day went by that I did not try to escape or kill one of my guards. I got very good at the second one. The trick is that they always think you are finished." {n}She lunges without shifting her feet at all, and you only just get your blade across in time.{/n}
"You are not finished yet. Good. Show me what the Commander of the crusade does when an old woman is trying to put {mf|him|her} on the ground."''',
       c("[Fight her fair, the way the drill-masters taught you.]", "fair"),
       c("[Fight her like a Trickster: feint, kick the dust, and go for the knee.]", "dirty", flags=(BOUT_DIRTY,))),
    nar("fair", '''{n}You fight her fair. It lasts longer than you expected and ends exactly as you expected: her blade flat against your throat, your own sword three paces away on the flags, and her breathing no harder than a woman climbing a stair.{/n}''',
        c("Continue", "fair2")),
    yn("fair2", '''"Well drilled," {n}she says.{/n} "Somebody took trouble over you. You fight the way we fought in the Second Crusade: shoulder to shoulder, eyes front, and die in good order." {n}She takes the blade away from your throat.{/n} "We lost Drezen that way, Commander. I would rather you did not lose anything else."''',
       c("Continue", "end")),
    nar("dirty", '''{n}You give her the drill-master's guard for three passes, and on the fourth you feint high, drop, sweep a boot through the grit of the court so that it sprays up into her face, and go in low for her knee with the flat of the blade.{/n}
{n}She goes down, and takes you with her, and for a few breaths it is not a fencing lesson at all: it is elbows and knees and her forearm across your throat and your practice sword somewhere under both of you. Then she starts to laugh, flat on her back in the dust, and cannot stop.{/n}''',
        c("Continue", "dirty2")),
    yn("dirty2", '''"Grit," {n}she says, when she can breathe.{/n} "In the eyes. Iomedae's teeth, Commander, that is a husk-keeper's trick. They used to throw salt at us so we would rub our eyes and not see them come with the hooks." {n}She wipes her face with the back of her wrist, smearing dust into the scar on her cheek.{/n}
"Some say one must always fight fair. I say not against everyone. And not always." {n}She props herself up on an elbow and looks down at you.{/n} "You would have lived through the siege. I did not think anybody in this crusade would have."''',
       c("Continue", "end")),
    nar("end", '''{n}She gets up, and holds out her hand, and pulls you up by it, and does not let go straight away. Her palm is hard and dry and gritty. She turns your hand over and looks at it, knuckles and calluses and the new scrapes from the flags, as a horse-dealer looks at a hoof.{/n}
"Good hands," {n}she says.{/n} "I told you I would watch them."''',
        c("[Take your hand back, eventually.]", flags=(B_BOUT,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

visit(Y + "beat.roast", "The roast", [
    nar("start", '''{n}The smell reaches the citadel before the invitation does: juniper, burnt fat, something sharp and old-fashioned that nobody in Drezen has cooked in living memory. Then a boy comes up with a message. The paladin has taken the citadel's cook hostage, and his kitchen, and a whole side of mutton, and requests the Commander on the east wall at the third bell, and the Commander is to bring bread, and is not to bring anybody else.{/n}''',
        c("Continue", "wall")),
    yn("wall", '''{n}She has made a table of two barrels and a door on the broken parapet of the gate tower, and a brazier, and the roast is on the door in a pan, black at the edges and very nearly the right shape.{/n}
"The Half Measure's," {n}she says.{/n} "Or near enough. I wrote to the girl in Nerosyan for the slate she took down, and I bullied your cook for two days, and he wept, and I think in the end I made most of it myself." {n}She saws off a slab with her belt knife and puts it on your bread.{/n} "Eat. Tell me it is terrible. It is. I want to hear somebody else say it."''',
       c('"It\'s terrible."', "terrible"),
       c('"It\'s the best thing I\'ve eaten in the Worldwound."', "best")),
    yn("terrible", '''{n}She laughs until she has to put her knife down.{/n} "It is. It is dreadful. The juniper is wrong and the mutton is old and I have burnt it on one side." {n}She eats a mouthful anyway, with her eyes shut.{/n} "And it tastes of the Half Measure. Of spring. Of the night before my first watch, when Staunton bought for the whole table and Joran fell asleep in the gravy."''',
       c("Continue", "tree")),
    yn("best", '''"Liar." {n}She points her knife at you.{/n} "That is the third. I am keeping count." {n}She eats a mouthful herself, with her eyes shut.{/n} "But it is close. It is close enough to taste of the Half Measure. Of spring. Of the night before my first watch, when Staunton bought for the whole table and Joran fell asleep in the gravy."''',
       c("Continue", "tree")),
    yn("tree", '''{n}She looks out over the ash toward the Wound, where the sky is the color of an old bruise.{/n}
"There is a tree by the town hall in Nerosyan. It was a sapling when I was a girl. The spring I took my vows I sat under it with a boy from the tannery and let him kiss me, and I felt very wicked, and he told everybody." {n}A dry sound.{/n} "It was in leaf when I went back. Not in bloom. I stood under it anyway, and it is ten times the height it was, and the boy from the tannery has been dead fifty years."
"I want to see it bloom, Commander. That is what I want. It is a small thing, for a woman who has been a saint, and I want it more than I have wanted anything since the hook."''',
       c('"Then we\'ll go in spring."', "spring"),
       c('[Flirt] "Will you let me kiss you under it? I won\'t tell everybody."', "kiss")),
    yn("spring", '''"We." {n}She turns the word over.{/n} "You say that as if there is going to be a spring. As if there is going to be a we in it." {n}She looks at you, in the red light of the brazier, for a while.{/n} "The Commander of the crusade, eating my terrible roast on a door, making plans for the spring. The sentries will never believe it."''',
       c("Continue", "end")),
    yn("kiss", '''"You would tell everybody." {n}She leans across the door, over the ruins of the roast, until her face is a hand's breadth from yours, and her breath smells of juniper and burnt fat.{/n} "You would tell every sentry on this wall. It would be in the songs by summer." {n}She stays there a moment longer, looking at your mouth, and then sits back.{/n} "Ask me again under the tree. I will decide then. I have waited seventy years for that tree; you can wait a season."''',
       c("Continue", "end")),
    nar("end", '''{n}You finish the roast between you, all of it, the burnt side too, and she wipes the pan out with the last of your bread, as a soldier does. When you go down she is scraping the door clean with her knife and humming something under her breath, off-key, that you think might be a drinking song from before the city fell.{/n}''',
        c("[Go down.]", flags=(B_ROAST,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)


NIGHT_STAYED = Y + "night_stayed"
CHURCH_DEFIED = Y + "church_defied"
CHURCH_SENT = Y + "church_sent"

visit(Y + "beat.night", "What Minagho told me", [
    nar("start", '''{n}The sentry from the east tower is at your door an hour past midnight, not quite looking you in the eye. The paladin in the gate tower, he says. She is not hurt. She is sitting up with a knife. She told him to go away, and then she told him to fetch the Commander, and then she told him not to, and he has decided to fetch you anyway, because she frightens him less than the alternative.{/n}''',
        c("Continue", "room")),
    nar("room", '''{n}She is on the floor of the flooded room with her back against the wall and her knees drawn up, in her shirt, with a husk-keeper's knife loose in one hand. The brazier has gone out. When your shadow comes into the doorway the knife comes up, fast, and then goes down again, slowly, as she sees who it is.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"I told him not to." {n}Her voice is hoarse.{/n} "I am not a child. I do not need to be sat with."
{n}She lets you sit anyway. After a while she says, to the dark window:{/n} "Minagho used to wake me. Not every night. Just often enough that I never learned to sleep through it. She would come in with a lamp and sit on the edge of the hook-rack and talk. Pleasantly. As if we were two old friends."
"She would tell me things. That everyone had forgotten me. That the Church had struck my name from its books for a heretic. That Staunton had given her the city with his own hands. That my goddess had heard every prayer I ever said on that hook and laughed." {n}Her hand tightens on the knife.{/n} "Some of it was lies. Some of it, I have since found out, was not. I never knew which. That was the point."''',
        c("Continue", "dream")),
    yn("dream", '''"Tonight I dreamed she came in with the lamp, and I was so glad to see a light that I thanked her." {n}She says it very flatly.{/n} "That is the part that woke me. Not her. The thanking."
{n}She turns her head and looks at you in the dark.{/n} "Tell me something true, Commander. Anything. I do not care what. Something nobody in this city has told me, that is not a song about me or a sermon or a lie to make me feel better. I want to hear something true in this room before it gets light."''',
        c('"I\'m not sure I\'m still entirely human. Nobody knows that but me."', "true_power"),
        c('"When I took your iron in the Fane, I didn\'t know what I\'d do with it. I still don\'t."', "true_iron"),
        c('"I\'m afraid of the day the war ends. I don\'t know who I\'ll be without it."', "true_war")),
    yn("true_power", '''{n}She is quiet for a while.{/n} "No," {n}she says at last.{/n} "I did not think you were. Nobody who is entirely human looks at a gate the way you looked at mine: as if you could see where it was going to break." {n}She puts the knife down on the floor between you.{/n} "I was not entirely human either, when I came out. A husk is not a person. It is a thing a person used to live in. I am still finding out which rooms are mine."''',
        c("Continue", "sleep")),
    yn("true_iron", '''{n}A short laugh comes out of the dark.{/n} "No. I did not think you did. You looked at it in the Fane the way a dog looks at a bone it has stolen off a table: very pleased, and not at all sure it was allowed." {n}She puts the knife down on the floor between you.{/n} "Keep not knowing, Commander. I would rather you did not know what to do with it than that you knew exactly."''',
        c("Continue", "sleep")),
    yn("true_war", '''"Ah." {n}She lets her head go back against the wall.{/n} "Yes. That is true. I can hear that it is true." {n}She puts the knife down on the floor between you.{/n} "I knew who I was on the day Drezen fell. I was the woman on the gate. Then for seventy years I was nobody, on a hook. The war ended for me and I did not have anybody to be. I am still looking." {n}A pause.{/n} "It is not so bad, looking. It is only slow."''',
        c("Continue", "sleep")),
    nar("sleep", '''{n}Neither of you says anything after that. The sentry's boots go past on the wall above, and past again. Somewhere before the first bell her head comes down onto your shoulder, heavily, all at once, the way a soldier's does in a wagon after three days without sleep, and her breathing slows, and she is gone.{/n}
{n}Your arm is going numb. Your back is against wet stone. The knife is on the floor where she put it, within her reach and not yours.{/n}''',
        c("[Stay where you are until she wakes.]", "stayed"),
        c("[Ease her down onto the camp bed and go.]", "went")),
    nar("stayed", '''{n}She wakes at the first gray light and does not move at once. Then she sits up, and looks at you, and at the knife on the floor, and at your arm, which you cannot feel.{/n}
"You stayed." {n}She rubs her face.{/n} "On the floor. In the wet. With a knife in reach of a madwoman." {n}She picks up the knife, looks at it, and slides it into her boot.{/n} "I slept. Do you know how long it has been since I slept past the second bell? Seventy years, Commander. Get out before I say something I will have to take back."''',
        c("[Get out, eventually.]", flags=(B_NIGHT, NIGHT_STAYED))),
    nar("went", '''{n}She does not wake when you lift her. She is lighter than she looks, all hard muscle and bone, and she mutters something as you lay her down that might be a name, or a curse, or an order to a man seventy years dead.{/n}
{n}In the morning there is a note under your door in the square old hand: "I woke in my bed and did not know how I got there. That has not happened to me since I was a child. Do not do it again without asking. Y." And under it, in smaller letters, pressed so hard the pen has torn the paper: "Thank you."{/n}''',
        c("[Keep the note.]", flags=(B_NIGHT,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

visit(Y + "beat.church", "The Church's sword", [
    nar("start", '''{n}The chaplain comes to your rooms in the middle of the morning with two acolytes and a letter bearing the sunburst seal of the Church of Iomedae in Nerosyan. He is a tall, grave, courteous man with ink on his fingers, and he is very sorry to trouble the Commander with a small matter of church property.{/n}''',
        c("Continue", "carries", requires=(CARRIES,)),
        c("Continue", "judges", forbids=(CARRIES,))),
    nar("carries", '''"The sword Radiance," {n}he says,{/n} "is a relic of the Church. It was held in trust in the Tower of Estrod, as the Commander knows, and lost when Kenabres burned, and recovered by the Commander, for which we are all grateful." {n}He clears his throat.{/n} "It is now, we understand, being carried on the walls of this city by a woman of great holiness and uncertain standing, who was for seventy years in the power of a demon, and who has not yet been examined by the Church. The Church asks, with all respect, that the relic be returned to a reliquary until the examination is complete."''',
        c("Continue", "choose")),
    nar("judges", '''"The sword Radiance," {n}he says,{/n} "is a relic of the Church. It was held in trust in the Tower of Estrod, as the Commander knows, and lost when Kenabres burned, and recovered by the Commander, for which we are all grateful." {n}He clears his throat.{/n} "We understand the Commander has sworn an oath upon it, to a woman of great holiness and uncertain standing, who was for seventy years in the power of a demon, and who has not yet been examined by the Church. An oath on a relic, sworn to an unexamined witness, is irregular. The Church asks, with all respect, that the oath be reviewed, and the relic lodged in a reliquary until it is."''',
        c("Continue", "choose")),
    nar("choose", '''{n}He waits. The acolytes wait. Out of the window, very small on the broken parapet of the east gate, a gray head is turned toward the citadel, as if she had seen the Church's seal go in at your door and has a fair idea what it is for.{/n}''',
        c('[Intimidate] "She was examined for seventy years. The sword stays where it is. Tell Nerosyan the Commander said so."', "defy"),
        c('"Take it up with her. She\'s on the east wall. I\'d bring the acolytes."', "sent"),
        c('"The crusade will pay for a new reliquary, and the sword stays out of it. Will that do?"', "bought",
          crusade=("Favors", -50))),
    nar("defy", '''{n}The chaplain goes quite pale, and then quite red, and bows, and says that he will tell Nerosyan exactly that. He does not say it with any pleasure. The acolytes follow him out as if the floor were hot.{/n}
{n}That evening there is a note under your door in the square old hand. It says: "I saw the seal go in and the chaplain come out the color of a boiled beet. I am told the Commander raised {mf|his|her} voice. Nobody has stood in front of me since the day the city fell. I did not like it. Do it again. Y."{/n}''',
        c("[Keep the note.]", flags=(B_CHURCH, CHURCH_DEFIED))),
    nar("sent", '''{n}The chaplain hesitates, and looks at the window, and at the small gray figure on the wall, and then gathers his acolytes and goes to do his duty, which you have to respect.{/n}
{n}What happens on the east wall you hear about only from the sentries, in several versions. In all of them the chaplain climbs the gate tower stair and makes his request, very courteously, and the paladin hears him out, very courteously, and then tells him the name of the priest who heard her first confession, and the year, and what that priest said to her about relics and the hands that hold them, and asks whether the Church has changed its mind since. In most versions the chaplain laughs. In one he kneels. He comes down without the sword and writes to Nerosyan that evening, and nobody ever sees what he wrote.{/n}''',
        c("Continue", "sent2")),
    yn("sent2", '''{n}She finds you on the citadel stair the next day.{/n} "You sent him to me," {n}she says.{/n} "You could have thrown him out. You could have given him the sword. You sent him up my stair to ask me himself." {n}She considers you.{/n} "Nobody has let me answer for myself in a very long time, Commander. I had forgotten what it was like. It was like a cold bath."''',
        c("[Let her go back up.]", flags=(B_CHURCH, CHURCH_SENT))),
    nar("bought", '''{n}The chaplain blinks. A new reliquary, he says slowly, is a very generous thought. It would of course need to be worthy of the relic it was not going to contain. He will write to Nerosyan. He bows himself out with the air of a man who has just been paid to lose an argument and is trying to work out whether he minds.{/n}
{n}That evening a note comes under your door in the square old hand: "You bought the Church off with an empty box. I have known quartermasters with less nerve. I hope the box is very beautiful. Y."{/n}''',
        c("[Keep the note.]", flags=(B_CHURCH, CHURCH_DEFIED))),
], requires=("trickster.ever", RETURNED, B_STATUE), **BEAT)

visit(Y + "beat.refugee", "The last cart", [
    nar("start", '''{n}She sends a boy for you in the afternoon, which she never does, and when you come down to the east gate she is standing in the road outside it with an old man. He is very old: bent, bald, with a crutch and a cloudy eye and the lace-cuffed coat of a prosperous Mendevian merchant who has not bought a new coat in thirty years. He is holding her hand in both of his and will not let go of it.{/n}''',
        c("Continue", "him")),
    nar("him", '''"I was six," {n}the old man tells you, in a thin high voice, before anybody has introduced anybody.{/n} "Six years old. In the last cart. My mother had me under a sack of turnips and told me not to move. I moved. I looked out through the tail of the cart and there was a lady on the gate with a sword that shone, and she was laughing, and there were demons all the way up the road behind her like black water."
"I have told that story every year of my life. My grandchildren think I made it up." {n}He pats her hand.{/n} "I came back to Drezen when they said the crusade had taken it. I wanted to see the gate before I died. And here she is. On the gate. Laughing."''',
        c("Continue", "her")),
    yn("her", '''{n}Yaniel's face is doing something you have never seen it do. She is holding very still, the way a person holds still with a wasp on their hand.{/n}
"I was not laughing," {n}she says carefully, to the old man.{/n} "I was shouting at the drivers to go faster." {n}Her voice cracks on the last word.{/n} "I did not know anyone in the last cart. I did not know if the last cart got through. They took me before I could turn round and look."
"It got through," {n}says the old man.{/n} "It got through, my lady. All the way to Nerosyan. My mother lived to be eighty. She named my sister after you."''',
        c("Continue", "after")),
    nar("after", '''{n}He goes back up the road at last, on his crutch, with a boy of his household holding his other arm, and turns round twice to wave. She waves back both times. Then she walks through the gate and up the tower stair very fast, and you follow her, and at the top, in the flooded room, she stands with her back to you and her hands flat on the wall.{/n}''',
        c("[Wait.]", "wait"),
        c("[Put your hand on her back.]", "touch")),
    yn("wait", '''"Seventy years," {n}she says to the wall.{/n} "Seventy years on a hook, and every single day I asked Her whether the last cart got through, and She did not answer, and I thought that was the answer." {n}Her shoulders move.{/n} "It got through. He was under the turnips. His mother named his sister after me."
{n}She turns round. Her face is wet and she does not wipe it.{/n} "Do not ever tell anyone you saw this, Commander. The sentries think I am made of iron. I would like them to go on thinking it for a while."''',
        c('"Iron doesn\'t cry. You\'re better than iron."', "end"),
        c('"Nobody will hear it from me."', "end")),
    yn("touch", '''{n}She goes rigid under your hand, and then, very slowly, she does not. Her back is hard and hot through the shirt, and shaking.{/n}
"It got through," {n}she says to the wall.{/n} "Seventy years I asked Her every day whether the last cart got through. She never answered. I thought that was the answer." {n}She laughs, badly.{/n} "He was under the turnips. The whole time. Under the turnips."
{n}She turns round inside your hand, so that it is on her arm instead, and puts her forehead against your collarbone, and stays there, and does not say anything else for a while.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}When you go down she is at the window of the flooded room, looking down the road to Nerosyan, where the last cart went.{/n}''',
        c("[Leave her there.]", flags=(B_REFUGEE,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

visit(Y + "beat.raid", "Over the wall", [
    nar("start", '''{n}The alarm goes on the east wall a little after the third bell: the tower horn, three short blasts, the call for "over the wall". By the time you reach the gate tower stair with a sword in your hand the fighting has already moved up onto the parapet. Something came up out of the ash in the dark, a dozen gaunt gray shapes with too many joints, the kind of Wound-spawn that climbs, and they came up at the one place where the old stones are broken.{/n}''',
        c("Continue", "carries", requires=(CARRIES,)),
        c("Continue", "judges", forbids=(CARRIES,))),
    nar("carries", '''{n}She is in the middle of them. You see her before anything else, because Radiance is burning in her hand like a torch, and the gray things are going back from the light the way grease goes back from a hot pan. She does not shout. She fights the way she talks, economically, without wasting anything, and every stroke finishes something.{/n}''',
        c("Continue", "fight")),
    nar("judges", '''{n}She is in the middle of them with a borrowed spear, and they are all over her, because she has no light and they have nothing to fear from a spear. She is holding the broken place in the parapet alone, the way she held the gate, and she sees you come up the stair with Radiance in your hand, and shouts, "Left, Commander! Light them up!"{/n}''',
        c("Continue", "fight")),
    nar("fight", '''{n}It lasts a quarter of an hour and feels like a night. You fight back to back with her at the broken place, because it is the only place on that wall where two people can stand with a stone at each shoulder. Her back is against yours. You can feel her breathing through both your shirts, fast and steady, and every time she moves you move, as if you had drilled it for years.{/n}
{n}When the last of them goes over the parapet into the dark the sentries start cheering, raggedly, and she turns round, streaked with gray ichor to the elbows, and looks at you.{/n}''',
        c("Continue", "after")),
    yn("after", '''"You fight like a thief," {n}she says, breathless.{/n} "You kept going for their knees." {n}She wipes her mouth with the back of her wrist and smears ichor across her cheek.{/n} "I have not fought beside anyone in seventy years. I had forgotten how it goes. You stop thinking about your back. You just stop. As if somebody had taken a weight off it."
{n}She is very close. The sentries are still cheering. Nobody is looking at the two of you, and everybody is.{/n}''',
        c("[Kiss her, there on the wall, in front of the sentries.]", "kiss"),
        c('"Your back\'s my business now."', "business")),
    nar("kiss", '''{n}She tastes of ichor and ash and the wall. She makes a sound against your mouth that might be outrage and might be a laugh, and her hand fists in your shirt, and for a heartbeat she kisses you back as if the war were over.{/n}
{n}Then she pushes you off, hard, with the flat of her hand, and says, loudly enough for the whole east wall to hear:{/n} "Not in front of the sentries, Commander!" {n}And, much more quietly, with her eyes very bright:{/n} "Not yet."''',
        c("[Go down, grinning like a fool.]", flags=(B_RAID, Y + "raid_kiss"))),
    yn("business", '''"My back." {n}She considers it.{/n} "That is a very forward thing to say to a woman on a wall." {n}She turns away, and bends to wipe her blade on a dead thing's hide, and says over her shoulder:{/n} "Very well. It is your business. Mind it. I have a great deal of back and most of it is scars."''',
        c("[Go down.]", flags=(B_RAID,))),
], requires=("trickster.ever", RETURNED, B_BOUT), **BEAT)

visit(Y + "beat.prayer", "A silent goddess", [
    nar("start", '''{n}You find her in the niche at the foot of the gate tower, in front of the painted martyr, but she is not praying. She is sitting on the plinth with her back to her own statue, looking at the lamp, with the face of a woman trying to add up a column of figures that will not come out.{/n}''',
        c("Continue", "ask")),
    yn("ask", '''"You laugh at gods," {n}she says, without looking up.{/n} "The sentries say so. They say it as if it were a trick you do at dinner. I want to know how it is done."
"Every day on that hook I prayed. Morning and night and in between. Minagho would sit on the rack and listen and laugh, and tell me there was nobody on the other end, and I said the words anyway, because they were the only thing in that room that belonged to me." {n}Her hands tighten on her knees.{/n} "And now I am out, and everybody tells me it was Her who got me out, and I kneel and I say the words, and there is nothing on the other end at all. There was more on the other end when I was on the hook."''',
        c('"Maybe she\'s tired of being asked for things. Try telling her something."', "tell"),
        c('"I laugh at gods because they can take it. You pray because you can. Both are ways of standing up."', "stand"),
        c('"I got you out. Not her. If you need someone to thank, I\'m here."', "me")),
    yn("tell", '''{n}She looks at you for a while.{/n} "Tell her something." {n}She turns it over.{/n} "Every prayer I said on that hook was an asking. Let the last cart get through. Let Staunton not have done it. Let me die before I break. Let me out." {n}She looks up at the painted face above her.{/n} "I have never once just told Her anything. It would be like telling a sergeant about the weather."
"Very well. I will try it. I will tell Her about the east wall, and the weather, and a thief who steals shackles. If She laughs, She laughs."''',
        c("Continue", "end")),
    yn("stand", '''{n}She is quiet for a long while.{/n}
"A way of standing up," {n}she says at last.{/n} "Yes. That is what it was on the hook. It was not a conversation. It was standing up, every day, in a place that wanted me on my knees." {n}She almost smiles.{/n} "Perhaps She is not silent. Perhaps I have been listening for the wrong thing. I was listening for an answer. Perhaps the praying was the answer."''',
        c("Continue", "end")),
    yn("me", '''{n}She laughs, short and sharp, the way she laughs at recruits.{/n} "You got me out. Yes. With a sword and a pin and a very poor bargain." {n}She shakes her head.{/n} "And who got you to the Fane, Commander, with that sword on your hip? Who kept that sword safe for seventy years in a tower in Kenabres, so that somebody would find it? Who put a thief in front of my hook and not a butcher?"
"No. I will thank you. I have thanked you. I will go on thanking you, in ways the chaplains would not approve of. But I am not going to stop saying the words."''',
        c("Continue", "end")),
    nar("end", '''{n}She turns round on the plinth at last, and kneels, facing her own painted face, and folds her hands. You leave her to it. From the stair you hear her voice, low and conversational, not the voice of a prayer at all, telling somebody about the weather on the east wall, and a thief.{/n}''',
        c("[Go.]", flags=(B_PRAYER,))),
], requires=("trickster.ever", RETURNED, B_STATUE), **BEAT)



# --- Chapter 4 (T): a husk on a block in Alushinyrra (a real act, done with what her cuff taught the Commander) ----------------

visit(Y + "ch4.block", "Another collector's item", [
    nar("start", '''{n}The slave market in the Lower City sells by the pound in the morning and by the piece in the afternoon. You are crossing it in the afternoon, on other business, when a lot on the block stops you.{/n}
{n}It is a woman, or it was: gray, bone-thin, hanging from a hook by one wrist with her toes just brushing the boards, the way a side of meat hangs in a butcher's window. Her face does not quite fit her; it sits a little wrong, like a borrowed coat. On the wrist that holds her up is a manacle you would know in the dark: crude husk-iron, two fingers thick, the pin a lump of soft metal hammered flat.{/n}''',
        c("Continue", "crier")),
    nar("crier", '''{n}The crier is a tiefling with a painted smile. "Collector's piece!" he is calling, to a crowd that is mostly not listening. "Genuine Fane stock, from the mistress's own racks, broken up this season! A face that can be any face you like, my lords! A shield that walks! Very obedient; the mistress trained it herself!"{/n}
{n}The husk's eyes are open. They move to you, and to your wrist, and stay there.{/n}''',
        c("Continue", "wrist_worn", requires=(CUFF_WORN,)),
        c("Continue", "choose", forbids=(CUFF_WORN,))),
    nar("wrist_worn", '''{n}Your sleeve has slid back. The iron on your own wrist, the one you closed there at night in this same city, is in plain view: the same crude metal, the same flattened pin, the same sheared link. The husk on the block is staring at it as if it were a word in a language she had forgotten she knew.{/n}''',
        c("Continue", "choose")),
    nar("choose", '''{n}The crier sees you looking and his smile widens.{/n} "Ah! A {mf|gentleman|lady} of discernment! Fifty in gold, my lord, or a crusader's note of hand; we are very modern here. Cheap at the price. The mistress's own work!"''',
        c("[Pay him with a note on the crusade's war chest, and have her cut down.]", "bought", crusade=("Finances", -50)),
        c("[Thievery] [Step up to inspect the lot, and work the pin while the crier talks.]",
          check=dict(Skill="SkillThievery", DC=18, Success="picked", Failure="fumbled", CommanderOnly=True)),
        c("[Walk on. You have a war to win.]", "left")),
    nar("bought", '''{n}He reads the note twice, holds it up to the light, and has his boy cut her down. She drops onto the boards like a sack. When you kneel beside her she does not flinch, and she does not look at your face; she looks at the iron on her wrist, and then at you, as if waiting to be told what she is for now.{/n}
{n}You work the pin out yourself. It takes three twists. You know exactly how, now.{/n}
"Go," {n}you tell her.{/n} {n}She looks at you for a while longer, and then she goes, not quickly, into the crowd, with her bare wrist held against her chest like something newly born. You keep the iron. You do not quite know why.{/n}''',
        c("[Put it in the pack with the other.]", flags=(HUSK_BOUGHT, Y + "ch4_block_seen"))),
    nar("picked", '''{n}You step up onto the block to look at her teeth, as a buyer does, and while the crier is explaining to you at length how very fine they are, your fingers find the pin behind her wrist. Three twists. You know exactly how, now. The cuff opens with a sound like a knuckle cracking, and she drops.{/n}
{n}The crier turns round at the thump, and his painted smile slides, and by then she is off the back of the block and into the crowd of the Lower City, running on legs that have not run in years, and you are shouting "Thief! Stop her!" as loudly as anybody, and pointing the wrong way.{/n}''',
        c("Continue", "picked2")),
    nar("picked2", '''{n}Nobody catches her. The crier tears at his hair. A demon in a litter laughs so hard at him it has to be carried away. You walk off the other side of the market with a second husk's iron in your pocket, still warm, and a feeling in your chest you do not have a word for.{/n}''',
        c("[Put it in the pack with the other.]", flags=(HUSK_FREED, Y + "ch4_block_seen"))),
    nar("fumbled", '''{n}Your fingers find the pin behind her wrist, but the crier is sharper than he looks. He catches your wrist in a grip like a trap, and his painted smile does not move at all.{/n} "Inspection is free, my lord. Liberation is fifty."
{n}Behind him two hulking things with too many teeth have come to the edge of the block. You could fight them. You would win. The whole market would see the Commander of the crusade start a riot in the Lower City over a husk, and every trader in Alushinyrra would know your face by nightfall.{/n}''',
        c("[Pay him with a note on the crusade's war chest.]", "bought", crusade=("Finances", -50)),
        c("[Walk away.]", "left")),
    nar("left", '''{n}You walk on. The crier's voice follows you across the market, calling the lot again, lower now: forty-five, genuine Fane stock, the mistress's own work.{/n}
{n}That night, when you take the pack off, the iron at the bottom of it is heavier than it was in the morning. It is not, of course. It is the same iron. You lie awake a long time anyway.{/n}''',
        c("[Try to sleep.]", flags=(HUSK_LEFT, Y + "ch4_block_seen"))),
], requires=("trickster.ever", SWAPPED, CH4_SEEN), forbids=(Y + "ch4_block_seen",), delay=24, chapters=(4,), areas=(),
    kind="memory")


# --- Chapter 5 (T): after the niche, before the war ends ---------------------------------------------------------------------

AFTER = dict(optional=True)

visit(Y + "after.watch", "The night watch", [
    nar("start", '''{n}She does not ask you up to the wall any more. She simply leaves a second spear leaning in the doorway of the gate tower, and a second cup by the brazier, and when you come up the stair after the last bell she hands you the spear without looking round, and you stand the watch with her.{/n}
{n}Nothing comes over the wall tonight. The ash lies quiet under a dirty moon. Far out toward the Wound something burns, very small, like a candle in a house across a valley.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"When the war is over," {n}she says, after an hour,{/n} "they will want me to be something. The Church will want a saint. The Queen's people will want a banner. The old knights who are left will want a story about how it was in the old days, and they will want me to tell it at dinners, in a clean dress, with that statue in the next room."
{n}She shifts the spear on her shoulder.{/n} "I do not want to be something. I want a wall, and a watch, and a cup of wine that is not very good, and somebody to stand the watch with who does not want me to be anything. Is that a great deal to want, Commander, after seventy years?"''',
        c('"It\'s the least you\'re owed."', "owed"),
        c('"It\'s a great deal. I\'ll see you get it anyway."', "anyway"),
        c('[Flirt] "You forgot to want me. I\'m wounded."', "forgot")),
    yn("owed", '''"Owed." {n}She tastes the word.{/n} "Nobody owes me anything, Commander. That was the whole bargain, remember? Nobody is square. I owe you a sword, or you owe me one; I lose count." {n}She leans her shoulder against yours, very slightly, on the parapet.{/n} "I would rather have it given than owed. Owed things get collected. Minagho taught me that."''',
        c("Continue", "end")),
    yn("anyway", '''{n}She laughs under her breath.{/n} "Anyway. That is a Commander's word. 'It cannot be done; I will see it done anyway.'" {n}She leans her shoulder against yours, very slightly, on the parapet.{/n} "I used to say it myself, on this gate. I was usually wrong. I would like, for once, to be standing next to somebody who says it and is right."''',
        c("Continue", "end")),
    yn("forgot", '''"I did not forget." {n}She does not look at you.{/n} "I left it off the list because it is not a thing I want. It is a thing I have. You do not put the things you have on a list of wants; that is how you lose them. Every soldier knows it." {n}She leans her shoulder against yours on the parapet, very slightly, and leaves it there.{/n} "Now be quiet. You are on watch."''',
        c("Continue", "end")),
    nar("end", '''{n}At the change of the watch the sentry who relieves you salutes her first and you second, and she pretends not to notice, and you pretend not to notice her pretending. Going down the stair in the dark she takes your hand for three steps, and lets it go before the bottom, where the torchlight is.{/n}''',
        c("[Go down.]", flags=(Y + "after.watch_stood",))),
], requires=("trickster.ever", COMMITTED, NICHE), **AFTER)

visit(Y + "after.wrist", "The mark it leaves", [
    nar("start", '''{n}She comes to your rooms in daylight, which she almost never does, and shuts the door behind her, and stands against it with her arms folded.{/n}''',
        c("Continue", "worn", requires=(CUFF_WORN,)),
        c("Continue", "packed", forbids=(CUFF_WORN,))),
    yn("worn", '''"You said you would take it off in front of me one day," {n}she says,{/n} "and let me see your wrist. I have been waiting. I am not good at waiting. I had seventy years of it and I used them all up."
{n}She holds out her hand, palm up.{/n} "Now, Commander. I want to know if it leaves the same mark on a free person."''',
        c("[Bend the pin straight and open the cuff for her.]", "mark")),
    nar("mark", '''{n}The pin you bent over in Alushinyrra fights you. She waits. When the cuff comes off, your wrist under it is red and rubbed raw at the bone, and there is a band of skin already paler than the rest, only a few months old.{/n}
{n}She takes your wrist in both her hands and turns it to the light, the way she turned the sword in the Fane, and looks at it for a long time. Then she puts her own wrist beside it: the old white band, hard as a heel, seventy years deep.{/n}''',
        c("Continue", "mark2")),
    yn("mark2", '''"It does," {n}she says quietly.{/n} "The same mark. Only shallower." {n}Her thumb moves over the red skin, very lightly.{/n} "I thought it would not. I thought it only marked people who were owned. I thought that was what the mark meant."
{n}She lifts your wrist and puts her mouth to the raw place, briefly, the way a soldier kisses a medal or a wound, and then gives your hand back to you, and the iron with it.{/n} "Put it back on. Or do not. I do not care any more which. I only wanted to know."''',
        c("[Put it back on.]", "end"),
        c("[Put it in your pocket.]", "end")),
    yn("packed", '''"You never wore it," {n}she says.{/n} "The iron. I asked the sentries. I asked your quartermaster, who looked at me as if I had asked him to steal it. You keep it in your pack, wrapped in linen, like a relic."
{n}Her mouth twists.{/n} "I do not know whether that makes me glad or angry. I have been trying to decide for a week. Show it to me."''',
        c("[Take it out of the linen and give it to her.]", "unwrapped")),
    nar("unwrapped", '''{n}She takes it from you and turns it over in her hands, the way you have seen her turn a blade to look at an edge. The inside is still bright where her wrist wore it thin. Your pack has not added so much as a scratch.{/n}''',
        c("Continue", "unwrapped2")),
    yn("unwrapped2", '''"Linen," {n}she says.{/n} "Clean linen. You folded it." {n}She laughs, very quietly, and it catches halfway.{/n} "Minagho kept me on a hook in a room that stank. You keep the thing that held me there wrapped in linen at the bottom of your pack, where you know it is there every time you lift it, like a... like a letter." {n}She gives it back and closes your fingers over it.{/n} "Glad. I have decided. Glad. Put it back in its linen."''',
        c("[Wrap it again.]", "end")),
    nar("end", '''{n}She stays for supper, which she has also never done, and eats with her elbows on the table, and tells you about a quartermaster in the old garrison who kept a pig in the armoury, and laughs so hard at her own story that she has to put her cup down.{/n}''',
        c("Continue", flags=(Y + "after.wrist_seen",))),
], requires=("trickster.ever", COMMITTED, NICHE, Y + "after.watch_stood"), **AFTER)

def integrate(payload):
    """Minagho's presence facts for the scene on the wall (read-only; the merged route's flags are never forbidden)."""
    derived = {
        MINAGHO_HERE: [[MC + "minagho_in"]],
        Y + "minagho_known": [["minachiv.started", MC + "minagho_in"], ["minachiv.started", MC + "chivarro_in"]],
    }
    for key, groups in derived.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
