"""Yaniel's courtship on the Trickster path (11-ROSTER-PLAN-2 §2, Yaniel build sheet): her letter from Nerosyan (Chapter 3),
the Commander alone with her iron in the Abyss (Chapter 4, one Memory page), and her Chapter 5 visits in Drezen, all in
person on her presence at her own Drezen mark (ledger 05 §4.2; since audit r9 even the verdict from Iz is told in person). The device,
the verdict, the commit, the niche, the pages and the reactions live in yaniel_trickster.

Canon anchors used here: the Half Measure's roast and the old tree by the town hall in Nerosyan (TrueYaniel/Cue_0035
efb1ee54); the statue (Cue_0044 7c1becd8, and Seelah's "the hands of the Yaniel statue"); Staunton Vhane and his brother
Joran, who made Radiance, going over to Minagho and dying for it (Cue_0030 5a28c5c2, Answer_0029 09d9caa5; Joran's brand on
the blade); Areelu, who gave her to Minagho "tired of my obstinacy" (Cue_0023 e8756562) and wore her face in the Drezen
citadel (FakeYaniel_First/Cue_0032 1ed1497d, FakeYaniel_ToAreelu/Cue_0001 7418d421); Minagho's collection (Cue_0021
7db27044). The Minagho scene reads the merged minagho_chivarro route (a started flag and presence facts, never a Forbids).
"""
from story_format import c, n
from storylines import yaniel_trickster as yt
from storylines.yaniel_trickster import hub  # noqa: E402 (the presence hub helper)
from storylines.yaniel_trickster import (B_AREELU, B_BOUT, B_CHURCH, B_NIGHT, B_PRAYER, B_RAID, B_REFUGEE, B_ROAST,
                                         B_STATUE, B_STAUNTON, B_WALLS, DRAWN_BITE, DRAWN_TREE, DRAWN_WALLS, HELD, HOLY, HUSK_BOUGHT, HUSK_FREED, HUSK_LEFT, NICHE, CARRIES, CLOSED,
                                         COMMITTED, CUFF_PACKED, CUFF_WORN, JUDGES, KILLED, MINAGHO_SECRET, MINAGHO_SEEN,
                                         MINAGHO_TOLD, RETURNED, STATUE_LIED, SWAPPED, TOLD_STATUE, TOLD_STAUNTON, UNMASKED,
                                         FAKE_FREED, FAKE_REFUSED, LATE, SWORD_LOST, OATH_BROKEN, OATH_STANDS, OATH_UNPROVEN, STRUCK, TRUSTED, WHY_BACK, WHY_CANT, Y, nar, visit, yn)

SCENES = yt.SCENES   # appended in order: the route's rest delivery keeps authored order within a relationship

CH3_READ = Y + "ch3_read"
CH4_SEEN = Y + "ch4_seen"
BOUT_DIRTY = Y + "bout_dirty"
MC = "minagho_chivarro.trickster."
MINAGHO_HERE = Y + "minagho_here"     # Derived (yaniel_trickster.DERIVED is extended below): Minagho sits in Drezen
AREELU_COURTED = "areelu.started"      # node variant only: the Commander is keeping Areelu's company


# --- Chapter 3 (T): a letter from Nerosyan -------------------------------------------------------------------------------

visit(Y + "ch3.nerosyan", "The tree by the town hall", [
    nar("start", '''{n}A letter finds you, travel-stained and much handled, carried by the crusade's couriers from Nerosyan. The last of them, a Mendevian sergeant, says the woman who gave it to him paid him in advance, in old coin, and told him the Commander would know her by her hand. The hand is square and upright, pressed hard into the paper, as if its owner did not trust ink to stay where it was put.{/n}''',
        c("[Read it.]", "one")),
    yn("one", '''"Commander,
"The Hand of the Inheritor knew me. I did not expect that. I thought, after so long, that a herald would have to be told. He looked at me the way you look at a letter you have been waiting a long time for, and then he put his hand on my head, and I am not going to write down what I did then.
"They brought me up out of the Fane and put me on a cart for Nerosyan with the wounded, because I would not stay in a bed. I have been in Nerosyan since."''',
       c("Continue", "carries", requires=(CARRIES,)),
       c("Continue", "judges", requires=(JUDGES,), forbids=(CARRIES,)),
       c("Continue", "refused", forbids=(CARRIES, JUDGES))),
    yn("carries", '''"I carried Radiance through the gate on my hip. You should have seen the guards' faces. A priest stopped me in the street and asked me, very kindly, where I had stolen it. I told him I had it from a thief. He did not know what to do with that at all.
"Three more priests have been to my lodging since, each more senior than the last, to explain to me that the sword belongs to the Church and ought to go back to a reliquary. I told the last of them that the Church had kept it in a tower and lost it, and had no business lecturing me about safekeeping, and that now it was mine again by gift of the Commander of the crusade, and the priest could take it up with you. So he may write to you. I apologise in advance. I do not apologise very much."''',
       c("Continue", "half")),
    yn("judges", '''"I went through the gate with nothing on my hip. I bought a sword in the market, a plain one, too light, with a grip made for a man's hand. It will do until something better tries to kill me.
"Every night I think of the other one on your hip, and the oath on it, and I find I sleep better than I have any right to. That is a strange thing to be able to say about a stranger who robbed me."''',
       c("Continue", "half")),
    yn("refused", '''"I still have my iron. I have tried to leave it off three nights running, and three nights running I have got up in the dark and put it back in my belt. I am telling you this because you are the only person in the world who would understand why it is funny, and because I do not know anybody else's address.
"You kept your sword. I hope you keep it well. I should have liked, I think, to watch you do it."''',
       c("Continue", "half")),
    yn("half", '''"They tell me the Half Measure is open again, in Drezen, on its old street, with a new keeper. I do not believe it. I will believe it when I am standing at the counter and they have never heard of my roast."
"The old tree by the town hall is in leaf, and not in bloom. I stood under it anyway. It is a great deal bigger than it was. So, I suppose, am I, in the wrong direction."''',
       c("Continue", "statue_told", requires=(TOLD_STATUE,)),
       c("Continue", "statue", forbids=(TOLD_STATUE,))),
    yn("statue_told", '''"You told me in the Fane there was a statue of me. You did not tell me it was twice my height, in the middle of the cathedral square, with Radiance held up at the sky and a smooth, unmarked face. The pilgrims leave candles at its feet. I went and stood among them one evening with my hood up. An old woman next to me was praying for her grandson at the front, to me, and I stood there beside her and did not know what to do with my hands."''',
       c("Continue", "statue_end")),
    yn("statue", '''"They have a statue of me in the cathedral square. You did not tell me that. Stone, twice my height, with Radiance held up at the sky and a smooth, unmarked face. The pilgrims leave candles at its feet. I went and stood among them one evening with my hood up. An old woman next to me was praying for her grandson at the front, to me, and I stood there beside her and did not know what to do with my hands."''',
       c("Continue", "statue_end")),
    yn("statue_end", '''"The chaplains want to send the statue to Drezen on an ox-cart. They have been arguing about the escort for a week. I am going too. I intend to get there before it does. Come and find me, Commander, if you are anywhere near the city. I should like to see what you have done with Drezen.
"Y."''',
       c("[Fold the letter away.]", flags=(CH3_READ,))),
], requires=("trickster.ever",), forbids=(CH3_READ,), delay=48, kind="letter", chapters=(3,), areas=(),
    RequiresAnyGroups=[[SWAPPED, yt.FANE_REFUSED]])


# --- Chapter 4 (T): the Commander alone in the Abyss with her iron ---------------------------------------------------------

visit(Y + "ch4.shackle", "Husk-iron", [
    nar("start", '''{n}Somewhere in Alushinyrra a bell is ringing that has never rung for anything good. You cannot sleep. You have been lying on a stranger's bed in a city that sells people by the pound, listening to it, and at some point your hand went into your pack of its own accord and came out with her iron.{/n}
{n}It is heavier than it looks. Minagho's smiths did not waste craft on it; it was hammered out of a bar and bent round a wrist while it was hot, and you can see, on the inside, where the metal has been worn bright and thin by decades of a wrist moving against it. The sheared link hangs from the eye and knocks against your knuckles when you turn it.{/n}''',
        c("Continue", "city", forbids=("minagho.dead",)),
        c("Continue", "city_dead", requires=("minagho.dead",))),
    nar("city_dead", '''{n}Minagho is dead in this city. You were there when it happened. Her collection is not: some of the things she collected are hanging in her lairs still, and some are on hooks in places nobody will tell you about, and one of them is standing a watch on the walls of Drezen because you took this off her wrist.{/n}''',
        c("Continue", "why_cant", requires=(WHY_CANT,)),
        c("Continue", "why_back", requires=(WHY_BACK,), forbids=(WHY_CANT,)),
        c("Continue", "choose", forbids=(WHY_CANT, WHY_BACK))),
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
        c("[Leave it on.]", "market", flags=(CUFF_WORN, CH4_SEEN))),
    nar("packed", '''{n}You fold it into a strip of clean linen, the way a chaplain folds a relic, and put it at the very bottom of your pack, under the maps and the spare boots, where you will know it is there every time you lift the pack and not otherwise.{/n}
{n}It is a small thing to carry through the Abyss. It weighs more than you want it to. You have been given worse loads by better people, and none of them was ever warm from the hand.{/n}''',
        c("[Sleep, if you can.]", "market", flags=(CUFF_PACKED, CH4_SEEN))),
    nar("market", '''{n}The Fleshmarkets of the Middle City sell by the pound in the morning and by the piece in the afternoon. A few days after that night you are crossing them in the afternoon, on other business, when a lot on the block stops you.{/n}
{n}It is a woman, or it was: gray, bone-thin, hanging from a hook by one wrist with her toes just brushing the boards, the way a side of meat hangs in a butcher's window. Her face does not quite fit her; it sits a little wrong, like a borrowed coat. On the wrist that holds her up is a manacle you would know in the dark: crude husk-iron, two fingers thick, the pin a lump of soft metal hammered flat.{/n}''',
        c("Continue", "crier")),
    nar("crier", '''{n}The crier is a tiefling with a painted smile. "Collector's piece!" he is calling, to a crowd that is mostly not listening. "Genuine Fane stock, from the mistress's own racks, broken up this season! A face that can be any face you like, my lords! A shield that walks! Very obedient; the mistress trained it herself!"{/n}
{n}The husk's eyes are open. They move to you, and to your wrist, and stay there.{/n}''',
        c("Continue", "wrist_worn", requires=(CUFF_WORN,)),
        c("Continue", "offer", forbids=(CUFF_WORN,))),
    nar("wrist_worn", '''{n}Your sleeve has slid back. The iron on your own wrist, the one you closed there at night in this same city, is in plain view: the same crude metal, the same flattened pin, the same sheared link. The husk on the block is staring at it as if it were a word in a language she had forgotten she knew.{/n}''',
        c("Continue", "offer")),
    nar("offer", '''{n}The crier sees you looking and his smile widens.{/n} "Ah! A {mf|gentleman|lady} of discernment! Fifty in gold, my lord, or a crusader's note of hand; we are very modern here. Cheap at the price. The mistress's own work!"''',
        c("[Pay him with a note on the crusade's war chest, and have her cut down.]", "bought", crusade=("Finances", -50)),
        c("[Thievery] [Step up to inspect the lot, and work the pin while the crier talks.]",
          check=dict(Skill="SkillThievery", DC=18, Success="picked", Failure="fumbled", CommanderOnly=True)),
        c("[Walk on. You have a war to win.]", "left")),
    nar("bought", '''{n}He reads the note twice, holds it up to the light, and has his boy cut her down. She drops onto the boards like a sack. When you kneel beside her she does not flinch, and she does not look at your face; she looks at the iron on her wrist, and then at you, as if waiting to be told what she is for now.{/n}
{n}You work the pin out yourself. It takes three twists. You know exactly how, now.{/n}
"Go," {n}you tell her.{/n} {n}She looks at you for a while longer, and then she goes, not quickly, into the crowd, with her bare wrist held against her chest like something newly born. You keep the iron. You do not quite know why.{/n}''',
        c("[Put it in the pack.]", flags=(HUSK_BOUGHT, Y + "ch4_block_seen"))),
    nar("picked", '''{n}You step up onto the block to look at her teeth, as a buyer does, and while the crier is explaining to you at length how very fine they are, your fingers find the pin behind her wrist. Three twists. You know exactly how, now. The cuff opens with a sound like a knuckle cracking, and she drops.{/n}
{n}The crier turns round at the thump, and his painted smile slides, and by then she is off the back of the block and into the crowd of the Middle City, running on legs that have not run in years, and you are shouting "Thief! Stop her!" as loudly as anybody, and pointing the wrong way.{/n}''',
        c("Continue", "picked2")),
    nar("picked2", '''{n}Nobody catches her. The crier tears at his hair. A demon in a litter laughs so hard at him it has to be carried away. You walk off the other side of the market with a second husk's iron in your pocket, still warm, and a feeling in your chest you do not have a word for.{/n}''',
        c("[Put it in the pack.]", flags=(HUSK_FREED, Y + "ch4_block_seen"))),
    nar("fumbled", '''{n}Your fingers find the pin behind her wrist, but the crier is sharper than he looks. He catches your wrist in a grip like a trap, and his painted smile does not move at all.{/n} "Inspection is free, my lord. Liberation is fifty."
{n}Behind him two hulking things with too many teeth have come to the edge of the block. You could fight them. You would win. The whole market would see the Commander of the crusade start a riot in the Fleshmarkets over a husk, and every trader in Alushinyrra would know your face by nightfall.{/n}''',
        c("[Pay him with a note on the crusade's war chest.]", "bought", crusade=("Finances", -50)),
        c("[Walk away.]", "left")),
    nar("left", '''{n}You walk on. The crier's voice follows you across the market, calling the lot again, lower now: forty-five, genuine Fane stock, the mistress's own work.{/n}
{n}That night the iron you carry is heavier than it was in the morning. It is not, of course. It is the same iron. You lie awake a long time anyway.{/n}''',
        c("[Try to sleep.]", flags=(HUSK_LEFT, Y + "ch4_block_seen"))),
], requires=("trickster.ever", SWAPPED), forbids=(CH4_SEEN,), delay=48, kind="memory", chapters=(4,), areas=(), owner="Memory")


# --- Chapter 5 (T): Minagho (the pivotal moral node: tell her, or keep it) ---------------------------------------------------

hub(Y + "ch5.minagho", "The lilitu on the crate", '"You look like you want to hit something."', [
    nar("start", '''{n}She does not answer. She takes you up to the east wall, and at the broken parapet of the gate tower she stops with her back to the city, the way a sentry stands when she does not trust what is behind her.{/n}''',
        c("Continue", "here", requires=(MINAGHO_HERE,)),
        c("Continue", "heard", forbids=(MINAGHO_HERE,))),
    yn("here", '''"There is a lilitu sitting on a crate by your quartermaster's stores." {n}Her voice is perfectly flat.{/n} "Eyeless. Pretty, if you like knives. I walked past her this morning on my way to the wall. She was turning one of the crusade's daggers over in her fingers, and she heard my boots, and she lifted her face the way she used to when she came into the room with the hooks, and she smiled."
"She knew my step, Commander. After all that time she knew my step. And nobody in this city will tell me why she is sitting in the middle of it, untouched, with a crusade dagger in her hand, except that it is the Commander's business."''',
       c("Continue", "ask")),
    yn("heard", '''"There is a madam from Alushinyrra on your quartermaster's bench," {n}she says,{/n} "and every sentry in the gate tower knows why. She asks after a lilitu by name. Minagho. And your people run her errands, and your quartermaster does not look round when she talks, and nobody in this city will tell me what the Commander of the crusade wants with the creature who kept me on a hook, except that it is the Commander's business."''',
       c("Continue", "ask")),
    yn("ask", '''{n}She turns round at last. Her face is quite calm. Her hand is on the parapet, and the knuckles are white.{/n}
"She took Staunton. She took Drezen. She took me, and hung me up in her collection between a Sarkorian witch and a boy from Kenabres who screamed for his mother for eleven years. Minagho liked to wake me and tell me things. That everyone had forgotten me. That my goddess had given me up."
"So tell me, Commander. What is she to you?"''',
       c('[Tell her the truth] "She\'s in my bed, Yaniel. And in my debt. That\'s what she is to me."', "truth",
         requires=("minachiv.complete",)),
       c('[Tell her the truth] "She\'s in my debt, and under my protection. And I mean to keep her close."', "truth_close",
         forbids=("minachiv.complete",)),
       c('[Keep it from her] "Nothing you need to carry. Leave her to me."', "hide", alignment=("Chaotic", 1))),
    yn("truth", '''{n}She does not move. For a while the only thing that moves is the wind, pulling at her cloak.{/n}
"In your bed." {n}She tastes it the way you might taste something to find out whether it has been poisoned.{/n} "And in your debt. So she is yours, the way I was hers." {n}A short, ugly laugh.{/n} "No. I do not believe that. Nobody owns Minagho. She owns things. I would know."
"I will not ask you to choose. Staunton had to choose once, between Minagho and everything else he was, and he chose her, and Drezen burned." {n}Her voice does not change.{/n} "I am telling you what I will do. I will stand my watch. I will not go where she is. And if she ever touches me again, in any way, for any reason, I will kill her, Commander, and I will not ask your leave, and I will not be sorry."''',
       c('"That\'s fair."', "truth_end"),
       c('"She won\'t touch you."', "truth_end")),
    yn("truth_close", '''{n}She does not move. For a while the only thing that moves is the wind, pulling at her cloak.{/n}
"Close." {n}She tastes the word the way you might taste something to find out whether it has been poisoned.{/n} "Under your protection. Minagho." {n}A short, ugly laugh.{/n} "She had me under hers. It had hooks in it."
"I will not ask you to choose. Staunton had to choose once, between Minagho and everything else he was, and he chose her, and Drezen burned. I am telling you what I will do. I will stand my watch. I will not go where she is. And if she ever lays a finger on me again, for any reason, I will kill her, Commander, and I will not ask your leave."''',
       c('"That\'s fair."', "truth_end"),
       c('"She won\'t touch you."', "truth_end")),
    yn("truth_end", '''{n}She looks at you for a while, the way she looks at the ash from the wall: as if something might come out of it, and she means to be ready.{/n}
"Thank you for not lying," {n}she says at last.{/n} "It is the worst thing anyone has told me since I came up out of the pit, and you told it to my face. That counts for something. I am not yet sure what."''',
       c("[Leave her to her watch.]", flags=(MINAGHO_SEEN, MINAGHO_TOLD))),
    yn("hide", '''{n}Her eyes stay on yours. You hold them. Whatever she is looking for, you do not give it to her.{/n}
"Leave her to you." {n}She repeats it slowly.{/n} "That is what they told me in the Fane, the ones who came to feed us. 'Leave it to the mistress.' It is a thing people say when they know something they do not mean to tell you."
{n}She turns back to the parapet.{/n} "Very well, Commander. I will leave her to you. I will not cross that courtyard. I will stand my watch, and I will watch your hands, and one day I will find out what they have been holding. Go on. I have work."''',
       c("[Go.]", flags=(MINAGHO_SEEN, MINAGHO_SECRET))),
], requires=("trickster.ever", RETURNED, "minagho_chivarro.started", Y + "minagho_known"), forbids=(MINAGHO_SEEN,))


# --- Chapter 5 (T): the courtship, before the commit ------------------------------------------------------------------------

BEAT = dict(forbids=(COMMITTED,), optional=True)

hub(Y + "beat.walls", "The city as it was", '"Walk the wall with me?"', [
    nar("start", '''{n}She pushes herself off the wall without a word and walks you up the gate tower stair and along the east wall in the dusk, without saying where you are going. Every so often she stops, and puts her hand on the parapet, and looks down into the city.{/n}''',
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
       c('[Flirt] "The fourth thing is that I\'ve been thinking about you since the Fane."', "flirt", flags=(DRAWN_WALLS,))),
    yn("laugh", '''"Once." {n}Her eyebrows go up.{/n} "Only once? The sentries have you down for three a week." {n}She shakes her head.{/n} "I prayed to mine every day on that hook, Commander, even the days I hated her. Especially those. I never once laughed at her. I think I would have liked to. I think she might have liked it too."''',
       c("Continue", "end")),
    yn("way", '''{n}She nods slowly, as though you had given the right answer in a drill.{/n}
"That is how I found out what I was. On the way. Minagho found out on the way too; she found out I would not break, and it annoyed her very much." {n}Her mouth twitches.{/n} "Do not let anyone finish finding you out before you do, Commander. It is a great waste of a person."''',
       c("Continue", "end")),
    yn("flirt", '''{n}She looks at you for a moment as if you had spoken in the tongue of the Abyss. Then she laughs, low and rough, and catches your sleeve before you can step back.{/n}
"Since the Fane." {n}Her grip stays on your sleeve.{/n} "You saw me on a hook, gray as a rat, stinking, with all of Minagho still on me, and you have been thinking about me since." {n}She shakes her head.{/n} "Then come for the middle watch and think about me from closer. Bring a cloak. It is cold up here, and I am not lending you mine."''',
       c("Continue", "end")),
    nar("end", '''{n}She walks you back to the gate tower. At the foot of the stair she stops, and for a moment you think she is going to say something else. Instead she reaches out and touches your wrist, where the iron sits, or where your pack strap crosses it, with two fingers, the way you might touch a door to see if the fire behind it has gone out. Then she goes up the stair to her watch.{/n}''',
        c("[Go down into the city.]", flags=(B_WALLS,))),
], requires=("trickster.ever", RETURNED), **BEAT)

hub(Y + "beat.statue", "Yaniel of Drezen, the Holy Martyr", '"There\'s a crowd at the east gate."', [
    nar("start", '''{n}The ox-cart from Nerosyan comes in at the east gate in the middle of the morning, with a crowd of pilgrims behind it and a crowd of chaplains in front, and in the back, lashed upright under a sheet like a bride under a veil, the Holy Martyr of Drezen. The chaplains mean to set her in the niche at the foot of the gate tower until the cathedral is ready for her. The real one has walked you down to watch, and is standing at the back of the crowd beside you with her hood up.{/n}''',
        c("Continue", "sheet")),
    nar("sheet", '''{n}They take the sheet off. The crowd sighs. The statue is twice the height of a woman, painted, with a gilded sword raised to heaven and a smooth face with none of her scars. The painted hands have no calluses. At its feet the carver has cut, in letters as long as your hand: YANIEL OF DREZEN, THE HOLY MARTYR. SHE HELD THE GATE.{/n}''',
        c("Continue", "told", requires=(TOLD_STATUE,)),
        c("Continue", "look", forbids=(TOLD_STATUE,))),
    yn("told", '''"You told me about this," {n}she says, low, beside you.{/n} "In the Fane. You said it was better to see me in the flesh than to pray in front of a cold stone statue. I thought you were being kind to an old woman on a hook." {n}She looks up at it.{/n} "You were being accurate. It is very cold."''',
       c("Continue", "look")),
    yn("look", '''{n}She stands looking at it while the chaplains bless it and the pilgrims light their candles and a very small boy is lifted up to kiss its stone toe. Her face does not change at all.{/n}
"Tell me the truth, Commander," {n}she says, without turning her head.{/n} "Is it a good likeness?"''',
       c('[Lie] "It\'s a good likeness."', "lie", flags=(STATUE_LIED,)),
       c('"It looks nothing like you."', "truth", flags=(Y + "statue_truth",)),
       c('[Flirt] "It\'s missing the scars. The scars are the best part."', "scars", flags=(Y + "statue_scars",))),
    yn("lie", '''{n}Her mouth twitches. She does not look at you.{/n}
"Liar," {n}she says, very softly, almost fondly.{/n} "You are a terrible liar, Commander, which is strange, because I have been told you are a very good one. Perhaps you only lie badly when it does not matter." {n}She pulls her hood lower.{/n} "Thank you. Nobody has lied to me kindly since the siege. They only ever did it the other way."''',
       c("Continue", "end")),
    yn("truth", '''{n}She lets out a breath she seems to have been holding since the cart came through the gate.{/n}
"No. It does not." {n}She looks up at the smooth stone face.{/n} "That girl never held anything. She would have dropped the gate and run, and she would have been right to. I did not have the sense." {n}A dry sound.{/n} "The chaplains keep telling me how moving it is. You are the first person in Drezen who has said it to my face. I think I could kiss you for it. I think I will not, in front of the chaplains."''',
       c("Continue", "end")),
    yn("scars", '''{n}She turns her head and looks at you properly, under the hood, as she has not since the sheet came off. Her eyes are very pale in the shadow.{/n}
"The best part? Be careful with that." {n}She turns fully toward you.{/n} "I would take every one of them off if I could. But this is the body I have. If it is the one you want to look at, come somewhere with fewer candles. I will show you what the carver left out."''',
       c("Continue", "end")),
    nar("end", '''{n}The chaplains carry the martyr into the niche and set her on her plinth with her stone sword raised toward the gate tower's ceiling, and a lamp at her feet. The real Yaniel watches them do it. When the crowd has gone she walks up to the niche alone, and stands in front of herself for a while, and then, very deliberately, turns her back on the statue and sits down on its plinth, and takes out a whetstone, and starts on her sword.{/n}''',
        c("[Leave her there.]", flags=(B_STATUE,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

hub(Y + "beat.staunton", "Joran's brand", '"You look like you have a question."', [
    nar("start", '''{n}She takes you up to her room in the gate tower and does not sit. She stands by the brazier with her arms folded and her back to the coals, and says, before you have shut the door:{/n}''',
        c("Continue", "told", requires=(TOLD_STAUNTON,)),
        c("Continue", "learned", forbids=(TOLD_STAUNTON,))),
    yn("told", '''"You told me in the Fane. Staunton and Joran, gone over to the demons, and dead for it. I said I knew. I did know; Minagho told me a hundred times. But I did not believe it until I came up here and asked the quartermaster where Joran's forge had been, and he spat."''',
       c("Continue", "brand")),
    yn("learned", '''"I asked the quartermaster where Staunton's brother kept his forge. He spat. Then a sergeant with more tact told me the rest: Staunton gone over to the demons, again, at the end, and Joran with him, and both of them dead for it. Minagho told me that a hundred times in the Fane. I did not believe her. I believe a sergeant."''',
       c("Continue", "brand")),
    yn("brand", '''"Joran made Radiance. Did you know that? He forged it with his own hands and put his brand on it, and he made the scabbard after, and fussed over the fit of it for a month. He was so proud of that sword he could not speak when he gave it to me. Staunton stood behind him and cried into his beard, and pretended it was the smoke."''',
       c("Continue", "carries", requires=(CARRIES,)),
       c("Continue", "judges", requires=(HELD,), forbids=(CARRIES,)),
       c("Continue", "judges_empty", forbids=(CARRIES, HELD))),
    yn("judges_empty", '''{n}She looks at your bare hip, where the sword ought to be, and her mouth tightens, and she lets it go.{/n}
"You have not got it on you. No matter. I know where the brand is; I watched him put it there." {n}She touches the side of her own hand, below the thumb, as if the mark were there.{/n} "When you carry that sword, you carry Joran's work, and I have been carrying Staunton on my wrist, if you think about it. His lilitu's iron. Neither of us asked for it."''',
       c("Continue", "grief")),
    yn("carries", '''{n}She draws the sword and holds it out to the firelight, blade flat, so that you can see the smith's brand near the hilt, worn nearly smooth.{/n}
"I have been looking at it every night on the wall." {n}Her thumb moves over it.{/n} "I keep thinking I ought to have it ground off. I keep not doing it."''',
       c("Continue", "grief")),
    yn("judges", '''"Show me."
{n}You draw Radiance and hold it to the firelight, and she leans close and finds the smith's brand near the hilt without looking for it, worn nearly smooth. She does not touch it.{/n}
"That is Joran's work on your hip," {n}she says,{/n} "and I have been carrying Staunton on my wrist, if you think about it. His lilitu's iron. Neither of us asked for it."''',
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
    yn("lie", '''{n}She turns her head and looks at you, and you know at once that she knows. Decades of being lied to by experts; a Commander's kind lie does not get past her.{/n}
"No, they do not," {n}she says, gently.{/n} "But thank you. That is a kind lie. I am beginning to keep a count." {n}She looks back at the fire.{/n} "Do not make a habit of it. I would like one person in this city to tell me the truth about the dead, even if it is you."''',
       c("Continue", "end")),
    nar("end", '''{n}She goes at last, up the stair to her wall. At the door she stops and says, without turning:{/n} "When the war is done, if I am alive, I am going to find where they buried him, and I am going to shout at him for an hour. Come with me. Somebody should stop me when I start to enjoy it."''',
        c('"I\'ll come."', flags=(B_STAUNTON,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

hub(Y + "beat.areelu", "The masquerade", '"Something\'s wrong."', [
    nar("start", '''{n}She takes you to the gate-tower stair and sits down with her jaw clenched. A chaplain has been telling her about the siege: a prisoner in the citadel who used Yaniel's name and wore her face. The chaplain called it a miracle. Then he told her whose miracle it was.{/n}''',
        c("Continue", "freed", requires=(FAKE_FREED,)),
        c("Continue", "refused", requires=(FAKE_REFUSED,), forbids=(FAKE_FREED,)),
        c("Continue", "plain", forbids=(FAKE_FREED, FAKE_REFUSED))),
    yn("freed", '''"You freed her. She thanked you. Later she showed you the passage to the Sword of Valor." {n}Her mouth tightens.{/n} "My face. My name. She even called herself a trophy. That was what I was, while she was walking about in my skin."
"You could not have known. She was good at it. She was good in the laboratory, too, before she gave me to Minagho. Tired of my obstinacy, she said."''',
       c("Continue", "areelu")),
    yn("refused", '''"You left her chained in the dungeon. She warned you there would be consequences." {n}Yaniel watches your face.{/n} "Did you suspect her? Or would you have left me there too?"
{n}She rubs her cheek with the heel of her hand.{/n} "Never mind. I am angry at the wrong person. She took my face and my name. Years on her tables, and when she had finished with me she found another use for them."''',
       c("Continue", "areelu")),
    yn("plain", '''"Areelu Vorlesh, wearing my face. The chaplain knew that much. He could not tell me what she did with it." {n}She touches her cheek.{/n} "I know what she did with the rest of me. Years in her laboratory, and then Minagho's collection. She said she was tired of my obstinacy. Apparently she liked my face better than my temper."''',
       c("Continue", "areelu")),
    yn("areelu", '''"Areelu Vorlesh." {n}She says the name as if spitting out a tooth.{/n} "Years in her laboratory. I watched her sew demons together and graft their limbs onto crusaders. Some of them lived. I wish I could tell you that was the mercy of it."
"And then she put on my face, and walked into my city, and people cried to see me." {n}Her hand goes to her own cheek, as if to be sure of it.{/n} "How many of them do you suppose she killed, wearing it?"''',
       c('"Some. Not as many as she could have. She wanted something from me."', "wanted"),
       c('"None, that I know of. She was looking at me, not them."', "wanted")),
    yn("wanted", '''"She wanted something from you." {n}She almost laughs.{/n} "Of course she did. She always wants something. That is the worst of her, Commander; she wants things the way a scholar wants things, patiently, and she will take your face off to get them and apologise for the mess."''',
       c("Continue", "courted", requires=(AREELU_COURTED,)),
       c("Continue", "end", forbids=(AREELU_COURTED,), requires=(FAKE_FREED,)),
        c("Continue", "end_refused", requires=(FAKE_REFUSED,), forbids=(FAKE_FREED, AREELU_COURTED)),
        c("Continue", "end_unknown", forbids=(FAKE_FREED, FAKE_REFUSED, AREELU_COURTED))),
    yn("courted", '''{n}She looks at you sidelong.{/n} "They tell me the Architect writes to you. And you write back." {n}Her jaw tightens.{/n} "Then use what she tells you to close the Wound. No more prisoners for her tables, Commander. I have seen enough of her work. Do not ask me to call her a friend."
"And if she puts on my face again, I will take it off her with a knife. You can put that in your next letter."''',
       c("Continue", "end", requires=(FAKE_FREED,)),
        c("Continue", "end_refused", requires=(FAKE_REFUSED,), forbids=(FAKE_FREED,)),
        c("Continue", "end_unknown", forbids=(FAKE_FREED, FAKE_REFUSED))),
    yn("end", '''{n}She leans her head against the stair wall.{/n} "The woman you freed thanked you in my voice. I keep thinking about that. And then you met me: gray, stinking, and ready to snap your fingers off if you put them in the wrong place."
{n}She opens her eyes.{/n} "Were you disappointed?"''',
       c('"No. The first one was a liar. You\'re the one I robbed."', "robbed"),
       c('[Flirt] "I\'d rather risk your teeth than her lies."', "bite", flags=(DRAWN_BITE,))),
    yn("robbed", '''{n}She laughs, a real one, short and startled out of her.{/n} "The one you robbed. Iomedae help me, that is the nicest thing anyone has said to me since I came back from the dead." {n}She gets up off the stair.{/n} "Go away, Commander. I have to stand a watch, and I cannot do it laughing."''',
       c("[Go.]", flags=(B_AREELU,))),
    yn("bite", '''"I did not try to bite you." {n}A pause.{/n} "I considered it." {n}She gets up off the stair and looks down at you from two steps up, which puts her eyes very nearly level with yours.{/n} "I am still considering it. Go away, Commander, before I decide."''',
       c("[Go.]", flags=(B_AREELU,))),

    yn('end_refused', '''{n}She leans her head against the stair wall.{/n} "The woman you left in that dungeon looked at you as if nothing mattered. Not even the chains. She wore my face. I keep wondering what you saw in it."
{n}Her eyes open.{/n} "Then you met me, filthy and furious. Did you look for her in me?"''',
       c('"No. The first one was a liar. You\'re the one I robbed."', "robbed"),
       c('[Flirt] "I\'d rather risk your teeth than her lies."', "bite", flags=(DRAWN_BITE,))),
    yn('end_unknown', '''{n}She leans her head against the stair wall.{/n} "You saw my face on Areelu before you saw it on me. I do not know what she made you expect. A saint? A broken old woman?"
{n}She opens her eyes.{/n} "Then I came out of the pit and started shouting at you. Were you disappointed?"''',
       c('"No. The first one was a liar. You\'re the one I robbed."', "robbed"),
       c('[Flirt] "I\'d rather risk your teeth than her lies."', "bite", flags=(DRAWN_BITE,))),
], requires=("trickster.ever", RETURNED, UNMASKED), **BEAT)

hub(Y + "beat.bout", "Not all enemies", '"Those are practice swords."', [
    nar("start", '''{n}"They are," she says. "The court behind the gate tower. Now. Come alone, or I will know you are afraid of an old woman."{/n}
{n}In the court she drops the two blunt blades from the armoury on the flags and rolls her sleeves to the elbow. Her forearms are ropy and white-scarred. She throws you a sword without warning and it is only luck and a lifetime of bad habits that you catch it by the grip.{/n}''',
        c("Continue", "fight")),
    yn("fight", '''"Seventy years a prisoner," {n}she says, circling,{/n} "and not a day went by that I did not try to escape or kill one of my guards. I got very good at the second one. The trick is that they always think you are finished." {n}She lunges without shifting her feet at all, and you only just get your blade across in time.{/n}
"You are not finished yet. Good. Show me what the Commander of the crusade does when an old woman is trying to put {mf|him|her} on the ground."''',
       c("[Keep a straight guard and answer her cuts.]", "fair"),
       c("[Fight her like a Trickster: feint, kick the dust, and go for the knee.]", "dirty", flags=(BOUT_DIRTY,))),
    nar("fair", '''{n}You keep to the drill. She tests your guard with short, hard blows, then steps back and lowers her practice sword. Your wrist aches from turning them.{/n}''',
        c("Continue", "fair2")),
    yn("fair2", '''"A sound guard," {n}she says.{/n} "Now try it with mud under your boots and something climbing over the parapet. Drezen did not fall in a practice yard."''',
       c("Continue", "end")),
    nar("dirty", '''{n}You hold a straight guard for three passes, and on the fourth you feint high, drop, sweep a boot through the grit of the court so that it sprays up into her face, and go in low for her knee with the flat of the blade.{/n}
{n}She goes down, and takes you with her, and for a few breaths it is not a fencing lesson at all: it is elbows and knees and her forearm across your throat and your practice sword somewhere under both of you. Then she starts to laugh, flat on her back in the dust, and cannot stop.{/n}''',
        c("Continue", "dirty2")),
    yn("dirty2", '''"Grit," {n}she says, when she can breathe.{/n} "In the eyes. Iomedae's teeth, Commander, that is a husk-keeper's trick. They used to throw salt at us so we would rub our eyes and not see them come with the hooks." {n}She wipes her face with the back of her wrist, smearing dust into the scar on her cheek.{/n}
"Some say one must always fight fair. I say not against everyone. And not always." {n}She props herself up on an elbow and looks down at you.{/n} "You would have lived through the siege. I did not think anybody in this crusade would have."''',
       c("Continue", "end")),
    nar("end", '''{n}She gets up, and holds out her hand, and pulls you up by it, and does not let go straight away. Her palm is hard and dry and gritty. She turns your hand over and looks at it, knuckles and calluses and the new scrapes from the flags, as a horse-dealer looks at a hoof.{/n}
"Good hands," {n}she says.{/n} "I told you I would watch them."''',
        c("[Take your hand back, eventually.]", flags=(B_BOUT,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

hub(Y + "beat.roast", "The roast", '"What is that smell?"', [
    nar("start", '''{n}Juniper, burnt fat, something sharp and old-fashioned that nobody in Drezen has cooked in living memory. It is on her cloak and her hands. "The Half Measure's roast," she says. "Fye let me have his kitchen for a day, and a whole side of mutton, and his cook, who wept. Come up to the wall at the third bell. Bring bread. Bring nobody else."{/n}''',
        c("Continue", "wall")),
    yn("wall", '''{n}She has made a table of two barrels and a door on the broken parapet of the gate tower, and a brazier, and the roast is on the door in a pan, black at the edges and very nearly the right shape.{/n}
"The Half Measure's," {n}she says.{/n} "Or near enough. The Half Measure is back on its old street, did you know? Fye Kito keeps it now; a relative of his had it before the siege. Nobody there remembered the roast. I told his cook how it was done, as near as I remembered, and he wrote it on a slate and made a face, and in the end I made most of it myself." {n}She saws off a slab with her belt knife and puts it on your bread.{/n} "Eat. Tell me it is terrible. It is. I want to hear somebody else say it."''',
       c('"It\'s terrible."', "terrible"),
       c('"It\'s the best thing I\'ve eaten in the Worldwound."', "best")),
    yn("terrible", '''{n}She laughs until she has to put her knife down.{/n} "It is. It is dreadful. The juniper is wrong and the mutton is old and I have burnt it on one side." {n}She eats a mouthful anyway, with her eyes shut.{/n} "And it tastes of the Half Measure. Of spring. Of the night before my first watch, when Staunton bought for the whole table and Joran fell asleep in the gravy."''',
       c("Continue", "tree")),
    yn("best", '''"Liar." {n}She points her knife at you.{/n} "I am keeping count." {n}She eats a mouthful herself, with her eyes shut.{/n} "But it is close. It is close enough to taste of the Half Measure. Of spring. Of the night before my first watch, when Staunton bought for the whole table and Joran fell asleep in the gravy."''',
       c("Continue", "tree")),
    yn("tree", '''{n}She looks out over the ash toward the Wound, where the sky is the color of an old bruise.{/n}
"There is a tree by the town hall in Nerosyan. It was a sapling when I was a girl. The spring I took my vows I sat under it with a boy from the tannery and let him kiss me, and I felt very wicked, and he told everybody." {n}A dry sound.{/n} "It was in leaf when I went back. Not in bloom. I stood under it anyway, and it is ten times the height it was, and the boy from the tannery has been dead fifty years."
"I want to see it bloom, Commander. That is what I want. It is a small thing, for a woman who has been a saint, and I want it more than I have wanted anything since the hook."''',
       c('"Then we\'ll go in spring."', "spring"),
       c('[Flirt] "Will you let me kiss you under it? I won\'t tell everybody."', "kiss", flags=(DRAWN_TREE,))),
    yn("spring", '''"We." {n}She turns the word over.{/n} "You say that as if there is going to be a spring. As if there is going to be a we in it." {n}She looks at you, in the red light of the brazier, for a while.{/n} "The Commander of the crusade, eating my terrible roast on a door, making plans for the spring. The sentries will never believe it."''',
       c("Continue", "end")),
    yn("kiss", '''"You would tell everybody." {n}She leans across the door, over the ruins of the roast, until her face is a hand's breadth from yours, and her breath smells of juniper and burnt fat.{/n} "You would tell every sentry on this wall. It would be in the songs by summer." {n}She stays there a moment longer, looking at your mouth, and then sits back.{/n} "Ask me again under the tree. I will decide then. I have waited long enough for that tree; you can wait a season."''',
       c("Continue", "end")),
    nar("end", '''{n}You finish the roast between you, all of it, the burnt side too, and she wipes the pan out with the last of your bread, as a soldier does. When you go down she is scraping the door clean with her knife and humming something under her breath, off-key, that you think might be a drinking song from before the city fell.{/n}''',
        c("[Go down.]", flags=(B_ROAST,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)


NIGHT_STAYED = Y + "night_stayed"
CHURCH_DEFIED = Y + "church_defied"
CHURCH_SENT = Y + "church_sent"

hub(Y + "beat.night", "What Minagho told me", '"You look like you haven\'t slept."', [
    nar("start", '''{n}She has not. It is in her face, gray under the gray, and in the way she holds herself very straight, as a soldier does who knows that if she leans on anything she will be asleep. She looks at you for a while as if deciding something. Then she takes you up the tower stair to the flooded room without a word.{/n}''',
        c("Continue", "room")),
    nar("room", '''{n}The brazier has gone out. There is a husk-keeper's knife on the floor by the wall, where somebody has plainly sat all night with her back to the stone and her knees drawn up. She sits down there again, in the same place, as if it were a post, and picks up the knife, and holds it loosely in one hand.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"The sentry wanted to fetch you last night. Twice. I told him not to." {n}Her voice is hoarse.{/n} "I am not a child. I do not need to be sat with."
{n}She lets you sit anyway. After a while she says, to the window:{/n} "Minagho used to wake me. Not every night. Just often enough that I never learned to sleep through it. She would come in with a lamp and sit on the edge of the hook-rack and talk. Pleasantly. As if we were two old friends."
"She would tell me things. That everyone had forgotten me. That the Church had struck my name from its books for a heretic. That Staunton had given her the city with his own hands. That my goddess had heard every prayer I ever said on that hook and laughed." {n}Her hand tightens on the knife.{/n} "Some of it was lies. Some of it, I have since found out, was not. I never knew which. That was the point."''',
        c("Continue", "dream")),
    yn("dream", '''"Tonight I dreamed she came in with the lamp, and I was so glad to see a light that I thanked her." {n}She says it very flatly.{/n} "That is the part that woke me. Not her. The thanking."
{n}She turns her head and looks at you in the gray light from the window.{/n} "Tell me something true, Commander. Anything. I do not care what. Something nobody in this city has told me, that is not a song about me or a sermon or a lie to make me feel better. I want to hear something true in this room before I try to sleep in it again."''',
        c('"I\'m not sure I\'m still entirely mortal. Nobody knows that but me."', "true_power"),
        c('"When I took your iron in the Fane, I didn\'t know what I\'d do with it. I still don\'t."', "true_iron", forbids=(LATE,)),
        c('"I\'m afraid of the day the war ends. I don\'t know who I\'ll be without it."', "true_war"),
        c('"When I took your iron on the wall, I didn\'t know what I\'d do with it. I still don\'t."', "true_iron_late", requires=(LATE,))),
    yn("true_power", '''{n}She is quiet for a while.{/n} "I wondered. The things you can do... I have seen soldiers come back changed. Not like that."
{n}She puts the knife on the floor between you.{/n} "Minagho made me a shield she could hide behind. I could still feel the blows. They hurt. So does this damned floor. I am here, whatever she made of me. You are here too. Sit a little longer."''',
        c("Continue", "sleep")),
    yn("true_iron", '''{n}A short laugh comes out of her.{/n} "No. I did not think you did. You looked at it in the Fane the way a dog looks at a bone it has stolen off a table: very pleased, and not at all sure it was allowed." {n}She puts the knife down on the floor between you.{/n} "Keep not knowing, Commander. I would rather you did not know what to do with it than that you knew exactly."''',
        c("Continue", "sleep")),
    yn("true_iron_late", '''{n}A short laugh comes out of her.{/n} "No. I did not think you did. You looked at it on my wall the way a dog looks at a bone it has stolen off a table: very pleased, and not at all sure it was allowed." {n}She puts the knife down on the floor between you.{/n} "Keep not knowing, Commander. I would rather you did not know what to do with it than that you knew exactly."''',
        c("Continue", "sleep")),
    yn("true_war", '''"Yes." {n}She lets her head rest against the wall and puts down the knife.{/n} "The day Drezen fell, I knew what to do. Hold the gate. Get the carts through. Then came seventy years in captivity. Areelu's tables first. Minagho's hooks after."
"I got out, and everyone wanted the woman from the songs. I had no idea what to do with her." {n}She looks at you.{/n} "I still do not. But the wall needs a sentry. That helps."''',
        c("Continue", "sleep")),
    nar("sleep", '''{n}Neither of you says anything after that. The sentry's boots go past on the wall above, and past again. Somewhere in the long afternoon her head comes down onto your shoulder, heavily, all at once, the way a soldier's does in a wagon after three days without sleep, and her breathing slows, and she is gone.{/n}
{n}Your arm is going numb. Your back is against wet stone. The knife is on the floor where she put it, within her reach and not yours.{/n}''',
        c("[Stay where you are until she wakes.]", "stayed"),
        c("[Ease her down onto the camp bed and go.]", "went")),
    nar("stayed", '''{n}She wakes when the evening bell goes and does not move at once. Then she sits up, and looks at you, and at the knife on the floor, and at your arm, which you cannot feel.{/n}
"You stayed." {n}She rubs her face.{/n} "On the floor. In the wet. With a knife in reach of a madwoman." {n}She picks up the knife, looks at it, and slides it into her boot.{/n} "I slept. With somebody in the room. Do you know how long it has been since I could do that? Seventy years, Commander. Get out before I say something I will have to take back."''',
        c("[Get out, eventually.]", flags=(B_NIGHT, NIGHT_STAYED))),
    nar("went", '''{n}She does not wake when you lift her. She is lighter than she looks, all hard muscle and bone, and she mutters something as you lay her down that might be a name, or a curse, or an order to a man long dead.{/n}
{n}The next morning there is a note under your door in the square old hand: "I woke in my bed and did not know how I got there. That has not happened to me since I was a child. Do not do it again without asking. Y." And under it, in smaller letters, pressed so hard the pen has torn the paper: "Thank you."{/n}''',
        c("[Keep the note.]", flags=(B_NIGHT,))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

hub(Y + "beat.church", "The Church's sword", '"Who are your visitors?"', [
    nar("start", '''{n}A chaplain has found her before you did: a tall, grave, courteous man with ink on his fingers, two acolytes, and a letter bearing the sunburst seal of the Church of Iomedae in Nerosyan. She is standing with her back to the wall and her arms folded, letting him talk. When he sees you he turns with visible relief. He is very sorry to trouble the Commander with a small matter of church property.{/n}''',
        c("Continue", "carries", requires=(CARRIES,)),
        c("Continue", "judges", forbids=(CARRIES, SWORD_LOST,)),
        c("Continue", "judges_cuff", requires=(SWORD_LOST,), forbids=(CARRIES,))),
    nar("carries", '''"Radiance," {n}the chaplain says,{/n} "was kept with the crusade's relics in the Tower of Estrod. It was stolen. The Church seeks its return to a reliquary." {n}He clears his throat and glances at Yaniel.{/n}
"The lady now carries it on this city's walls. A woman of great holiness, certainly, but she spent decades in a demon's power and has not been examined by the Church. We ask that the relic be placed in safekeeping until that examination is complete."''',
        c("Continue", "choose")),
    nar("judges", '''"Radiance," {n}the chaplain says,{/n} "was kept with the crusade's relics in the Tower of Estrod. It was stolen. The Church seeks its return to a reliquary." {n}He clears his throat and glances at Yaniel.{/n}
"We understand the Commander swore upon the relic before this lady. She is a woman of great holiness, but she has not been examined after her captivity. An oath on a holy relic before such a witness requires review. We ask that the oath be reviewed and Radiance placed in a reliquary."''',
        c("Continue", "choose")),
    nar("choose", '''{n}He waits. The acolytes wait. Yaniel waits too, with her arms folded, and she is not looking at the chaplain. She is looking at you.{/n}''',
        c('"Minagho had her turn at examining Yaniel. Leave her alone. Radiance belongs in the war against the demons. Tell Nerosyan I said so."', "defy"),
        c('"Why ask me? Ask her."', "sent"),
        c('"The crusade will pay for a new reliquary. Leave Radiance out of it. Will that do?"', "bought",
          crusade=("Favors", -50))),
    nar("defy", '''{n}The chaplain goes quite pale, and then quite red, and bows, and says that he will tell Nerosyan exactly that. He does not say it with any pleasure. The acolytes follow him away down the street as if the stones were hot.{/n}
{n}Yaniel watches them go. When she turns back to you her face is doing something complicated.{/n} "The color of a boiled beet," {n}she says.{/n} "Nobody has stood in front of me since the day the city fell. I did not like it." {n}A pause.{/n} "Do it again."''',
        c("[Leave her to her watch.]", flags=(B_CHURCH, CHURCH_DEFIED))),
    nar("sent", '''{n}The chaplain hesitates, and looks at her, and at you, and then turns to her and makes his request again, very courteously, to her face, which you have to respect.{/n}
{n}She hears him out, very courteously. Then she tells him the name of the priest who heard her first confession, and the year, and what that priest said to her about relics and the hands that hold them, and asks whether the Church has changed its mind since. The chaplain is quiet for a while. Then he laughs, a little helplessly, and bows to her, not to you, and goes away to write to Nerosyan. Nobody ever sees what he wrote.{/n}''',
        c("Continue", "sent2")),
    yn("sent2", '''{n}When he has gone she looks at you sidelong.{/n} "You sent him to me," {n}she says.{/n} "You could have thrown him out. You could have agreed with him. You made him ask me himself." {n}She considers you.{/n} "Nobody has let me answer for myself in a very long time, Commander. I had forgotten what it was like. It was like a cold bath."''',
        c("[Leave her to her watch.]", flags=(B_CHURCH, CHURCH_SENT))),
    nar("bought", '''{n}The chaplain blinks. A new reliquary, he says slowly, is a very generous thought. It would of course need to be worthy of the relic it was not going to contain. He will write to Nerosyan. He bows himself away with the air of a man who has just been paid to lose an argument and is trying to work out whether he minds.{/n}
{n}Yaniel watches him go.{/n} "You bought the Church off with an empty box," {n}she says.{/n} "I have known quartermasters with less nerve. I hope the box is very beautiful."''',
        c("[Leave her to her watch.]", flags=(B_CHURCH, CHURCH_DEFIED))),

    nar('judges_cuff', '''"Radiance," {n}the chaplain says,{/n} "was kept with the crusade's relics in the Tower of Estrod. It was stolen. The Church seeks its return to a reliquary." {n}He clears his throat and glances at Yaniel.{/n}
"We understand the Commander swore upon this lady's manacle to find Radiance and carry it against the demons. Minagho kept her in it." {n}He looks at her bare wrist, then away.{/n} "We ask to review that oath. And we seek Radiance for the Church's reliquary, rather than another private undertaking."''',
        c("Continue", "choose")),
], requires=("trickster.ever", RETURNED, B_STATUE), **BEAT)

hub(Y + "beat.refugee", "The last cart", '"Who is your friend?"', [
    nar("start", '''{n}She is not alone today. She is standing with an old man who has come up the road from the east gate on a crutch to find her. He is very old: bent, bald, with a crutch and a cloudy eye and the lace-cuffed coat of a prosperous Mendevian merchant who has not bought a new coat in thirty years. He is holding her hand in both of his and will not let go of it.{/n}''',
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
    yn("wait", '''"Seventy years," {n}she says to the wall.{/n} "Seventy years a prisoner, and every single day I asked Her whether the last cart got through, and She did not answer, and I thought that was the answer." {n}Her shoulders move.{/n} "It got through. He was under the turnips. His mother named his sister after me."
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

hub(Y + "beat.raid", "Over the wall", '"Mind if I stand the watch with you tonight?"', [
    nar("start", '''{n}She looks at your hip.{/n} "Bring a sword," {n}she says.{/n}
{n}A little after the third bell, halfway along the east wall with her, you hear the tower horn go: three short blasts, the call for "over the wall". Something has come up out of the ash in the dark, a dozen gaunt gray shapes with too many joints, the kind of Wound-spawn that climbs, and they have come up at the one place where the old stones are broken.{/n}''',
        c("Continue", "carries", requires=(CARRIES, HOLY)),
        c("Continue", "carries_plain", requires=(CARRIES,), forbids=(HOLY,)),
        c("Continue", "judges", requires=(HELD,), forbids=(CARRIES,)),
        c("Continue", "judges_empty", forbids=(CARRIES, HELD))),
    nar("carries_plain", '''{n}She is into them before you have your sword clear, and she is the only thing on the wall that is not moving backward: her feet braced at the broken parapet, a hook-scar pulling when she raises her arm. Radiance strikes plain and cold in her hand. She does not shout. She fights the way she talks, economically, without wasting anything, and every stroke finishes something.{/n}''',
        c("Continue", "fight")),
    nar("judges_empty", '''{n}She is into them with a borrowed spear, and they are all over her. She is holding the broken place in the parapet alone, the way she held the gate, and as you come up beside her with a plain sword in your hand her eyes go once to your hip, where something else ought to be, and then she shouts, "Left, Commander! Left!"{/n}''',
        c("Continue", "fight")),
    nar("carries", '''{n}She is into them before you have your sword clear, and Radiance is burning in her hand like a torch, and the gray things are going back from the light the way grease goes back from a hot pan. She does not shout. She fights the way she talks, economically, without wasting anything, and every stroke finishes something.{/n}''',
        c("Continue", "fight")),
    nar("judges", '''{n}She is in the middle of them with a borrowed spear, and they are all over her, because she has no light and they have nothing to fear from a spear. She is holding the broken place in the parapet alone, the way she held the gate, and as you draw Radiance she shouts, "Left, Commander! Light them up!"{/n}''',
        c("Continue", "fight")),
    nar("fight", '''{n}It lasts a quarter of an hour and feels like a night. You fight back to back with her at the broken place, because it is the only place on that wall where two people can stand with a stone at each shoulder. Her back is against yours. You can feel her breathing through both your shirts, fast and steady, and every time she moves you move, as if you had drilled it for years.{/n}
{n}When the last of them goes over the parapet into the dark the sentries start cheering, raggedly, and she turns round, streaked with gray ichor to the elbows, and looks at you.{/n}''',
        c("Continue", "after", forbids=(STRUCK,)),
        c("Continue", "after_struck", requires=(STRUCK,))),
    yn("after_struck", '''{n}She looks at you the way she looked at you in the Fane with Seelah's hand on your arm, and then she looks at your hands.{/n}
"In the Fane you drew on me," {n}she says.{/n} "Tonight you had my back for a quarter of an hour on a broken wall, and every one of those things could have had yours. I have been trying all the way through it to decide which of those two was you." {n}She wipes her blade on her cloak.{/n} "I have decided. Do not make me decide again."''',
        c("Continue", "after", flags=(TRUSTED,))),
    yn("after", '''"You fight like a thief," {n}she says, breathless.{/n} "You kept going for their knees." {n}She wipes her mouth with the back of her wrist and smears ichor across her cheek.{/n} "I had forgotten how it feels to stop watching the person at my back. You stop thinking about your back. You just stop. As if somebody had taken a weight off it."
{n}She is very close. The sentries are still cheering. Nobody is looking at the two of you, and everybody is.{/n}''',
        c("[Kiss her, there on the wall, in front of the sentries.]", "kiss"),
        c('"Your back\'s my business now."', "business")),
    nar("kiss", '''{n}She tastes of ichor and ash and the wall. She makes a sound against your mouth that might be outrage and might be a laugh, and her hand closes on your shirt, and for a heartbeat she kisses you back as if the war were over.{/n}
{n}Then she pushes you off, hard, with the flat of her hand, and says, loudly enough for the whole east wall to hear:{/n} "Not in front of the sentries, Commander!" {n}And, much more quietly, with her eyes very bright:{/n} "Not yet."''',
        c("[Go down, grinning like a fool.]", flags=(B_RAID, Y + "raid_kiss"))),
    yn("business", '''"My back." {n}She considers it.{/n} "That is a very forward thing to say to a woman on a wall." {n}She turns away, and bends to wipe her blade on a dead thing's hide, and says over her shoulder:{/n} "Very well. It is your business. Mind it. I have a great deal of back and most of it is scars."''',
        c("[Go down.]", flags=(B_RAID,))),
], requires=("trickster.ever", RETURNED, B_BOUT), **BEAT)

hub(Y + "beat.prayer", "Nothing to ask", '"Where are you going?"', [
    nar("start", '''{n}She takes you down to the niche at the foot of the gate tower, in front of the painted martyr, but she does not pray. She is sitting on the plinth with her back to her own statue, looking at the lamp, with the face of a woman trying to add up a column of figures that will not come out.{/n}''',
        c("Continue", "ask")),
    yn("ask", '''"You laugh at gods," {n}she says, without looking up.{/n} "The sentries say so. They say it as if it were a trick you do at dinner. I want to know how it is done."
"Every day on that hook I prayed. Morning and night and in between. Minagho would sit on the rack and listen and laugh, and tell me there was nobody on the other end, and I said the words anyway, because they were the only thing in that room that belonged to me. And She answered. She sent you." {n}Her hands tighten on her knees.{/n} "And now I kneel, and I open my mouth, and I have nothing to ask Her for. I do not know how to pray to Her without asking. I never learned. On the hook there was always something to ask."''',
        c('"Maybe she\'s tired of being asked for things. Try telling her something."', "tell"),
        c('"I laugh at gods because they can take it. You pray because you can. Both are ways of standing up."', "stand"),
        c('"I got you out. Not her. If you need someone to thank, I\'m here."', "me")),
    yn("tell", '''{n}She looks at you for a while.{/n} "Tell her something." {n}She turns it over.{/n} "Every prayer I said on that hook was an asking. Let the last cart get through. Let Staunton not have done it. Let me die before I break. Let me out." {n}She looks up at the painted face above her.{/n} "I have never once just told Her anything. It would be like telling a sergeant about the weather."
"Very well. I will try it. I will tell Her about the east wall, and the weather, and a thief who steals shackles. If She laughs, She laughs."''',
        c("Continue", "end")),
    yn("stand", '''{n}She is quiet.{/n}
"A way of standing up," {n}she says at last.{/n} "Yes. That is what it was on the hook. It was not a conversation. It was standing up, every day, in a place that wanted me on my knees." {n}She almost smiles.{/n} "Perhaps She is not silent. Perhaps I have been listening for the wrong thing. I was listening for an answer. Perhaps the praying was the answer."''',
        c("Continue", "end")),
    yn("me", '''{n}She laughs, short and sharp.{/n} "You got me out. Yes. I know that, Commander. And who got you through the Wound alive? Who put you in front of my prison instead of another husk-keeper?"
"No. I will thank you. I have thanked you. I will go on thanking you, in ways the chaplains would not approve of. But I am not going to stop saying the words."''',
        c("Continue", "end")),
    nar("end", '''{n}She turns round on the plinth at last, and kneels, facing her own painted face, and folds her hands. You leave her to it. From the stair you hear her voice, low and conversational, not the voice of a prayer at all, telling somebody about the weather on the east wall, and a thief.{/n}''',
        c("[Go.]", flags=(B_PRAYER,))),
], requires=("trickster.ever", RETURNED, B_STATUE), **BEAT)



# --- Chapter 5 (T): after the niche, before the war ends ---------------------------------------------------------------------

AFTER = dict(optional=True)

hub(Y + "after.watch", "The night watch", '"Is that second spear for me?"', [
    nar("start", '''{n}It is. She does not ask you up to the wall any more. She simply hands you the spear, and a second cup, and walks you up the stair after the last bell, and you stand the watch with her.{/n}
{n}Nothing comes over the wall tonight. The ash lies quiet under a dirty moon. Far out toward the Wound something burns, very small, like a candle in a house across a valley.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"When the war is over," {n}she says, after an hour,{/n} "they will want me to be something. The Church will want a saint. The Queen's people will want a banner. The old knights who are left will want a story about how it was in the old days, and they will want me to tell it at dinners, in a clean dress, with that statue in the next room."
{n}She shifts the spear on her shoulder.{/n} "I do not want to be something. I want a wall, and a watch, and a cup of wine that is not very good, and somebody to stand the watch with who does not want me to be anything. Is that a great deal to want, Commander, after the hook?"''',
        c('"It\'s the least you\'re owed."', "owed"),
        c('"It\'s a great deal. I\'ll see you get it anyway."', "anyway"),
        c('[Flirt] "You forgot to want me. I\'m wounded."', "forgot")),
    yn("owed", '''"Owed." {n}She snorts.{/n} "The Church says I am owed a statue. The Queen's people say I am owed a pension. The old knights say I am owed a seat at their dinners." {n}She leans her shoulder against yours, very slightly, on the parapet.{/n} "I will take the wine. You can keep the rest."''',
        c("Continue", "end")),
    yn("anyway", '''{n}She laughs under her breath.{/n} "Anyway. That is a Commander's word. 'It cannot be done; I will see it done anyway.'" {n}She leans her shoulder against yours, very slightly, on the parapet.{/n} "I used to say it myself, on this gate. I was usually wrong. I would like, for once, to be standing next to somebody who says it and is right."''',
        c("Continue", "end")),
    yn("forgot", '''"I did not forget." {n}She does not look at you.{/n} "I left you off because you are standing here. I do not have to want the one who is on the next watch with me. I only have to hand them a cup." {n}She leans her shoulder against yours on the parapet, very slightly, and leaves it there.{/n} "Now be quiet. You are on watch."''',
        c("Continue", "end")),
    nar("end", '''{n}At the change of the watch the sentry who relieves you salutes her first and you second, and she pretends not to notice, and you pretend not to notice her pretending. On the stair she takes your hand. At the bottom, in the torchlight, she stops to kiss you before leading you to her room. Her supper has gone cold; she eats it with your knee between hers.{/n}''',
        c("[Go down.]", flags=(Y + "after.watch_stood",))),
], requires=("trickster.ever", COMMITTED, NICHE), **AFTER)

hub(Y + "after.wrist", "The mark it leaves", '"You want something."', [
    nar("start", '''{n}She takes you up to her room in the gate tower in daylight, and shuts the door behind her, and stands against it with her arms folded.{/n}''',
        c("Continue", "worn", requires=(CUFF_WORN,)),
        c("Continue", "packed", forbids=(CUFF_WORN,), requires=(CUFF_PACKED,)),
        c("Continue", "pouch", forbids=(CUFF_WORN, CUFF_PACKED))),
    yn("worn", '''"You wore it in the Abyss." {n}She holds out her hand.{/n} "Show me your wrist. I want to see what it left on you."''',
        c('[Set the iron aside and show her your wrist.]', "mark")),
    nar("mark", '''{n}You set the cuff beside you and hold out your wrist. A pale band crosses the skin where the iron rubbed against the bone. She takes your wrist in both hands and turns it toward the window. Then she puts her own beside it: the old white band, hard as a heel, worn in over decades.{/n}''',
        c("Continue", "mark2")),
    yn("mark2", '''"It does," {n}she says quietly.{/n} "The same mark. Only shallower." {n}Her thumb moves over the marked skin, very lightly.{/n} "I thought it would not. I thought it only marked people who were owned. I thought that was what the mark meant."
{n}She lifts your wrist and puts her mouth to the marked place, briefly, then longer, her eyes on yours. She draws you nearer by that hand before giving the iron back.{/n} "Put it back on. Or do not. I do not care any more which. I only wanted to know."''',
        c("[Put it back on.]", "end", flags=(Y + "cuff_back_on",)),
        c("[Put it in your pocket.]", "end", flags=(Y + "cuff_pocketed",))),
    yn("packed", '''"You never wore it," {n}she says.{/n} "The iron. I asked the sentries. I asked your quartermaster, who looked at me as if I had asked him to steal it. You keep it in your pack, wrapped in linen, like a relic."
{n}Her mouth twists.{/n} "I do not know whether that makes me glad or angry. I have been trying to decide for a week. Show it to me."''',
        c("[Take it out of the linen and give it to her.]", "unwrapped")),
    nar("unwrapped", '''{n}She takes it from you and turns it over in her hands, the way you have seen her turn a blade to look at an edge. The inside is still bright where her wrist wore it thin. Your pack has not added so much as a scratch.{/n}''',
        c("Continue", "unwrapped2")),
    yn("unwrapped2", '''"You folded it." {n}She opens the linen across her knee, then gives you the cuff.{/n} "Clean, too. I did not think anyone would trouble over that damned thing." {n}She catches your hand as you reach for the cloth and kisses your knuckles.{/n} "Wrap it. Then come here. I have been standing at this window waiting for you."''',
        c("[Wrap it again.]", "end")),
    nar("end", '''{n}She sends down for supper, draws your chair beside hers and puts a hand on your thigh under the table. She eats with her elbows on the table, and tells you about a quartermaster in the old garrison who kept a pig in the armoury, and laughs so hard at her own story that she has to put her cup down.{/n}''',
        c("Continue", flags=(Y + "after.wrist_seen",))),

    yn("pouch", '"Show me the iron." {n}She holds out her hand.{/n} "I know you still have it. I want to see what you have done to it."',
        c("[Put the cuff in her hand.]", "pouch2")),
    yn("pouch2", '{n}She turns the cuff over. The inside still shines where her wrist wore it thin.{/n} "Not a scratch." {n}She puts it back in your hand, then draws that hand to her waist.{/n} "Put it away. I wanted to see it, and now I want you to stop looking at it."',
        c("Continue", "end")),
], requires=("trickster.ever", COMMITTED, NICHE, Y + "after.watch_stood"), **AFTER)

hub(Y + "beat.drill", "Hold it properly", '"You wanted to see the sword."', [
    nar("start", '''{n}"Not here," she says. "The court behind the gate tower." She walks you there with her sleeves rolled and no weapon at all, and when you come through the arch she holds out her empty hand, not for the sword: for your wrist.{/n}''',
        c("Continue", "grip", forbids=(OATH_BROKEN, OATH_STANDS, OATH_UNPROVEN,)),
        c('Continue', "grip_stands", requires=(OATH_STANDS,), forbids=(OATH_BROKEN,)),
        c('Continue', "grip_broken", requires=(OATH_BROKEN,)),
        c('Continue', "grip_unproven", requires=(OATH_UNPROVEN,), forbids=(OATH_BROKEN, OATH_STANDS))),
    yn("grip", '''"You carry it like a quartermaster's stores," {n}she says, turning your hand over.{/n} "Safe in its scabbard. The oath is still before you, Commander. Draw it. I want to see what those hands can do."
{n}You draw Radiance. She steps behind you and puts her hands over yours on the grip, shifting your fingers one at a time. Her breath warms your ear.{/n} "There. Ease the thumb. Joran left room for it. You are holding a sword, not wringing a chicken's neck."''',
        c("Continue", "cut")),
    yn("cut", '''{n}She walks you through the old cuts, the Mendevian ones, the ones they do not teach any more: the gate cut, the stair cut, the one she calls the widow's cut and will not explain. Her voice is quite even. Her hands on yours are not.{/n}
"I used to do this every morning on the east wall," {n}she says, close behind your ear.{/n} "Two hundred cuts before the bell. Staunton said I would wear the sword out. On the hook I did them in my head. Every morning. Two hundred. I did not miss one."''',
        c('"Show me the two hundred."', "two"),
        c('"You still want it back."', "want", forbids=(OATH_BROKEN, OATH_STANDS, OATH_UNPROVEN,)),
        c('"You still want it back."', "want_stands", requires=(OATH_STANDS,), forbids=(OATH_BROKEN,)),
        c('"You still want it back."', "want_broken", requires=(OATH_BROKEN,)),
        c('"You still want it back."', "want_unproven", requires=(OATH_UNPROVEN,), forbids=(OATH_BROKEN, OATH_STANDS))),
    yn("two", '''{n}She lets go of your hands and steps away and does them in the air, empty-handed, the way she did them in her head on the hook: two hundred cuts with a sword that is not there, fast and exact, her feet never moving off the one flagstone, her breath going in and out like a bellows.{/n}
{n}When she stops, the first bell is ringing. She is not even flushed.{/n} "Two hundred," {n}she says.{/n} "Every morning. I kept count in the Fane, on the hook, in my head, and I never lost my place once. Keep your wrist straight. You have done forty."''',
        c("Continue", "end")),
    yn("want", '''{n}Her hands go still on yours.{/n} "Yes. Every day. I see it on your hip and want to snatch it and run. The crusade needs it in a hand that can carry it all the way. I know that. It does not stop me wanting it."
{n}She lets go of your hands.{/n} "Carry it where you swore, Commander. Carry it well. Now put it away. You are making this damned lesson harder than it needs to be."''',
        c("Continue", "end")),
    nar("end", '''{n}She makes you do the gate cut forty times before she lets you go, and at the fortieth she says nothing, which you have learned is the highest praise she gives.{/n}''',
        c("[Sheathe the sword.]", flags=(Y + "beat.drill",))),

    yn('grip_stands', '''"You carried it where you swore. I said the oath stood, and it stands." {n}She turns your hand over.{/n} "Now draw it. I did not bring you here to admire the scabbard."
{n}You draw Radiance. She steps behind you and puts her hands over yours on the grip, shifting your fingers one at a time. Her breath warms your ear.{/n} "There. Ease the thumb. Joran left room for it. You are holding a sword, not wringing a chicken's neck."''',
        c("Continue", "cut")),

    yn('grip_broken', '''"Draw it." {n}She turns your hand over, briskly.{/n} "This is a lesson, Commander. It does not mend the oath. But the things coming out of the Wound will not wait for us to settle that."
{n}You draw Radiance. She steps behind you and puts her hands over yours on the grip, shifting your fingers one at a time. Her breath warms your ear.{/n} "There. Ease the thumb. Joran left room for it. You are holding a sword, not wringing a chicken's neck."''',
        c("Continue", "cut")),

    yn('grip_unproven', '''"I could not judge where it had been. I can judge how you hold it." {n}She turns your hand over.{/n} "Draw it. We can do something useful while the other matter waits."
{n}You draw Radiance. She steps behind you and puts her hands over yours on the grip, shifting your fingers one at a time. Her breath warms your ear.{/n} "There. Ease the thumb. Joran left room for it. You are holding a sword, not wringing a chicken's neck."''',
        c("Continue", "cut")),

    yn('want_stands', '''{n}Her hands go still on yours.{/n} "Yes. Every day. I see it on your hip and want to snatch it and run. The crusade needs it in a hand that can carry it all the way. I know that. It does not stop me wanting it."
{n}She lets go of your hands.{/n} "You took it where you promised. Keep the edge sound. Keep it ready. Now put it away. You are making this damned lesson harder than it needs to be."''',
        c("Continue", "end")),

    yn('want_broken', '''{n}Her hands go still on yours.{/n} "Yes. Every day. I see it on your hip and want to snatch it and run. The crusade needs it in a hand that can carry it all the way. I know that. It does not stop me wanting it."
{n}She lets go of your hands.{/n} "The oath is broken. The sword still has work to do. Use it. Now put it away. You are making this damned lesson harder than it needs to be."''',
        c("Continue", "end")),

    yn('want_unproven', '''{n}Her hands go still on yours.{/n} "Yes. Every day. I see it on your hip and want to snatch it and run. The crusade needs it in a hand that can carry it all the way. I know that. It does not stop me wanting it."
{n}She lets go of your hands.{/n} "Carry it to the Threshold. That is where I told you I would believe it. Now put it away. You are making this damned lesson harder than it needs to be."''',
        c("Continue", "end")),
], requires=("trickster.ever", RETURNED, JUDGES, HELD, B_WALLS), forbids=(COMMITTED, CARRIES), optional=True)

hub(Y + "beat.light", "The light on the ash", '"You look like you want to show me something."', [
    nar("start", '''{n}"The wall," she says. "Now. It is not an alarm." She takes you up to the broken place in the parapet and draws Radiance, and does not turn round.{/n}
"Look," {n}she says.{/n}''',
        c("Continue", "look")),
    nar("look", '''{n}Out on the ash, a long bowshot from the wall, something is moving: low and slow and too many legs, feeling its way toward the city through the dark the way a hand feels along a table for a cup. The sentries have not seen it. The torches on the wall do not reach that far.{/n}
{n}She lifts the sword. It does not flare; it is not the Fane, and nothing is singing. It only brightens, the way a coal brightens when somebody breathes on it, and the light goes out across the ash, thin and gold, and finds the thing.{/n}''',
        c("Continue", "thing")),
    nar("thing", '''{n}It stops. It turns what it has instead of a face toward the wall. For a moment it and the sword look at each other across a quarter-mile of ash. Then it goes back into the dark the way it came, quickly, and does not come again.{/n}
{n}She lowers the blade. The light goes down into the steel.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"That one has been coming close for three nights," {n}she says.{/n} "It has seen what this blade does to the others." {n}She turns the sword so that the last of the gold runs down the fuller.{/n} "I wanted you to see it. You gave this away. I thought you should see what it does in the hands you gave it to."
"Every night I stand here and think: the Commander of the crusade could have this, and does not, because {mf|he|she} took an old woman's iron instead. I think it is the stupidest thing I have ever seen a commander do. I think about it every night anyway."''',
        c('"It was a trade."', "trade"),
        c('"It looks better on you."', "better")),
    yn("trade", '''"A trade." {n}She snorts.{/n} "A trade is when both parties get something they want. I did not want this. I wanted to be left alone to be sorry for myself." {n}She looks out at the ash, where the thing went.{/n} "Perhaps that is what you got, then. Me, not sorry for myself. It is not much of a bargain for a sword like this, Commander. You ought to have haggled."''',
        c("Continue", "end")),
    yn("better", '''{n}She laughs, startled, and then does not.{/n} "It looks better on me." {n}She turns the blade in the torchlight, as if checking.{/n} "Nobody in my whole captivity said anything looked better on me. Minagho used to say I looked best on a hook." {n}She slides the sword home in its saddle-leather scabbard.{/n} "Thank you, Commander. That is a very foolish thing to say to a woman on a wall, and I am going to remember it anyway."''',
        c("Continue", "end")),
    nar("end", '''{n}You stand the rest of her watch with her. Nothing else comes out of the ash that night. Once, near the end, she hands you the sword to hold while she re-ties her boot, and takes it back afterwards without looking, as if she had handed it to you every night of her life.{/n}''',
        c("[Go down at the bell.]", flags=(Y + "beat.light",))),
], requires=("trickster.ever", RETURNED, CARRIES, HOLY, B_WALLS), **BEAT)

hub(Y + "beat.hunter", "A paladin who hunts alone", '"Who is the scout?"', [
    nar("start", '''{n}She takes you into the guardroom at the foot of the gate tower, where a scout of the Eagle Watch who has just come in off the ash is eating at a table, and sits down across from him, and listens to him the way a hound listens at a door.{/n}''',
        c("Continue", "scout")),
    nar("scout", '''{n}The scout is telling a story he has plainly told before. Out past the old Sarkorian cairns, he says, there is a paladin who hunts alone. An old man, gray as a wolf, in armour nobody has made in fifty years. He has been out in the Wound longer than the scout has been alive. He comes and goes by paths nobody else knows, and where he has been the demons are fewer, and he will not come in to any fort, and he will not take a banner. Berenguer, they call him, the ones who have seen him. The ones who have tried to follow him mostly have not come back.{/n}''',
        c("Continue", "her")),
    yn("her", '''{n}When the scout has gone to find his supper she sits looking at the place where he was.{/n}
"Berenguer," {n}she says.{/n} "I never knew him. I should like to see how much of that story he would admit to. A paladin who would not come in to any fort and would not take a banner." {n}Something moves at the corner of her mouth.{/n} "In my day they would have put him on a charge. Now they tell stories about him in guardrooms."
"I have been thinking, Commander, since the scout started talking, that I could do that. Go out past the cairns with a spear and no banner and nobody's name on me but my own. Nobody would build me a statue. Nobody would want me to be anything."''',
        c('"Then go, if you want it. I won\'t hold you."', "go"),
        c('"Stay. I\'d rather have you on my wall than in a scout\'s story."', "stay"),
        c('"When the war\'s done, I\'ll come with you. Find him, and see if he\'s any good."', "both")),
    yn("go", '''{n}She looks at you for a while.{/n}
"You would not hold me." {n}She says it as if testing a rope.{/n} "No. You would not. You would stand at the gate and watch me go down the road and say something clever to the sentry, and then you would go and win your war." {n}She gets up.{/n} "That is why I am not going yet, you understand. Because you would let me. Nobody has ever let me before. I want to find out what else you would let me do before I use that one up."''',
        c("Continue", "end")),
    yn("stay", '''"Your wall." {n}She snorts.{/n} "It is my wall. I held it seventy years before you called it yours." {n}But she does not get up.{/n} "Very well. I will stay on my wall, and you will come up it when you can, and some night when the war is done I will look out at the cairns and think about an old man who would not take a banner, and not go." {n}She looks at you sidelong.{/n} "Do not look so pleased. I have not promised which night."''',
        c("Continue", "end")),
    yn("both", '''{n}She laughs, loud enough that the sentry on the stair looks in.{/n}
"You. In the Wound, past the cairns, with no banner and no army, following an old man nobody can follow." {n}She shakes her head.{/n} "You would talk the demons into fighting each other and steal their boots while they were at it. Berenguer would take one look at you and go back into the ash for another fifty years."
{n}The laugh fades, but not all the way.{/n} "Yes. When the war is done. I would like that. I would like to see his face."''',
        c("Continue", "end")),
    nar("end", '''{n}She walks you to the foot of the stair. On the bottom step she stops, and looks out through the arch at the ash, the way the scout came in, and for a moment her face is the face on the statue, and then it is not.{/n}''',
        c("[Go.]", flags=(Y + "beat.hunter",))),
], requires=("trickster.ever", RETURNED, B_WALLS), **BEAT)

# Round 2 set pieces use the existing situations; additions retain every saved address.
_by = {s["Id"]: s for s in SCENES}
def _node(suffix, nid):
    return next(n for n in _by[Y + suffix]["Nodes"] if n["Id"] == nid)

# YAN-01/02: she decides whether to answer the chaplain's use of her name.
_statue = _by[Y + "beat.statue"]
_node("beat.statue", "sheet")["Text"] += (' {n}The chaplain raises his hands toward the pilgrims.{/n} "Yaniel would have wanted the living to surrender their comforts for the crusade."'
    ' {n}Beside you, Yaniel catches her hood between two fingers. A wounded cart-driver is being pressed to leave his blanket at the plinth.{/n}')
_old = _node("beat.statue", "sheet")["Choices"]
_memorial_exits = [dict(c) for c in _old]
for _choice in _old:
    _choice["Next"] = "appearance"
_statue["Nodes"].extend([
    yn("appearance", '"He has never met me." {n}Her hand tightens on her hood.{/n} "Listen to him. He has already decided what I want. I have a mind to tell him."'
       ' {n}She looks at the driver again.{/n}',
       c('"Then tell him. I am here."', "appears"),
       c('"You can stay here. I will get the driver his blanket."', "quiet")),
    yn("appears", '{n}She steps into the crowd and pulls her hood back.{/n} "Give him his blanket. I held a gate to get people out of the cold. I did not die to make this man colder."'
       ' {n}The chaplain stares. She points toward the wounded driver.{/n} "Well?" {n}He takes the blanket from the offering pile himself. A pilgrim starts to kneel; Yaniel catches his elbow and keeps him on his feet.{/n}', c("Continue", "meal")),
    yn("quiet", '{n}She stays beside you while you take the blanket back to the cart. When the chaplain asks for your name she answers from under her hood.{/n} "Write down Yaniel. She wanted that man warm."'
       ' {n}She turns away before he can see her face.{/n}', c("Continue", "meal")),
    yn("meal", '"Enough speeches. I want a meal. And if you call it a feast in my honor I will eat in the guardroom."'
       ' {n}She takes your arm and stays just long enough to look at the unveiled face.{/n}', *_memorial_exits),
])

# A bounded bout, with her counterstroke; no result repairs the Fane attack.
_bout = _by[Y + "beat.bout"]
_node("beat.bout", "fight")["Text"] = ('"Three passes. Blunt steel. No spells. If a blade lands clean, we stop." {n}She circles you, watching your feet.{/n}'
    ' "I spent years trying to kill guards who thought I was finished. You need to see what comes over Drezen\'s wall before you try to stop it. Show me your guard."')
_node("beat.bout", "fight")["Choices"].extend([
    c("[Lower your blade and concede the pass.]", "yield"),
    c("[Mobility] [Step inside her reach and turn her blade aside.]", check=dict(Skill="SkillMobility", DC=25, Success="mobility_win", Failure="mobility_loss")),
    c('[Bluff] "Behind you!"', check=dict(Skill="CheckBluff", DC=25, Success="bluff_win", Failure="bluff_loss")),
])
_bout["Nodes"].extend([
    yn("yield", '{n}She checks her stroke when you lower the blade.{/n} "A surrendered pass. You had better know why you give ground when the edge is sharp." {n}She offers the practice blade back, hilt first.{/n}', c("Continue", "end")),
    nar("mobility_win", '{n}You step inside the descending blade and turn it past your shoulder. Your flat lands clean across her ribs. She stops, nods and tests the tender place with her fingers.{/n} "Good. Now remember there may be another one behind it."', c("Continue", "end")),
    nar("mobility_loss", '{n}She shifts her grip as you come inside. The blunt pommel stops at your breastbone; you halt before it drives home.{/n} "Too close. Watch both hands."', c("Continue", "end")),
    nar("bluff_win", '{n}She glances toward the gate arch. Your flat catches her raised arm before her eyes return. She lowers the blade and swears.{/n} "Once, Commander. That will work once."', c("Continue", "end")),
    nar("bluff_loss", '{n}Her eyes stay on you. The flat of her blade taps your thigh as you advance.{/n} "I spent seventy years listening to liars. Try your feet next time."', c("Continue", "end")),
])
_node("beat.bout", "end")["Text"] = ('{n}She puts both practice swords against the wall, then turns your hand over to inspect the scrapes.{/n}'
    ' "Useful work. Keep those hands ready. Next time something comes over the parapet it will not stop at a clean touch."')

# Party-only holy forms: the plain branch still uses Radiance, without borrowing its upgrades.
RAID_HOLY = Y + "raid.holy_in_party"
yt.DERIVED[RAID_HOLY] = [["yaniel.radiance_party.ha4"], ["yaniel.radiance_party.ha6"]]
_raid = _by[Y + "beat.raid"]
_node("beat.raid", "start")["Choices"][2]["Requires"].append(RAID_HOLY)
_node("beat.raid", "start")["Choices"].append(c("Continue", "judges_plain", requires=(yt.PARTY,), forbids=(CARRIES, RAID_HOLY)))
_raid["Nodes"].append(nar("judges_plain", '{n}She hooks a climbing claw with her spear and drags the creature across the stones toward your drawn Radiance. Plain cold iron shears through its neck. She braces her spear against the next one.{/n} "Left, Commander! Keep them off the sentry!"', c("Continue", "fight")))

# Current arrivals, not old arrival receipts. The heard road asks after an absent captor.
_node("ch5.minagho", "start")["Choices"][0]["Requires"].append("minagho.present_now")
_node("ch5.minagho", "start")["Choices"][1]["Requires"].append("chivarro.present_now")
_node("ch5.minagho", "start")["Choices"][1]["Forbids"] = [MINAGHO_HERE]
_node("ch5.minagho", "heard")["Text"] = ('"Chivarro was at the quartermaster\'s bench. She asked after Minagho." {n}Yaniel rubs an old scar on her wrist.{/n}'
    ' "The sentry repeated the question to me. I had a few questions of my own. What has been promised about the creature who kept me on a hook? I want your answer, Commander. Not the sentry\'s."')

def integrate(payload):
    """Minagho's presence facts for the scene on the wall (read-only; the merged route's flags are never forbidden)."""
    derived = {
        MINAGHO_HERE: [[MC + "minagho_in", "minagho.present_now"]],
        Y + "minagho_known": [["minagho_chivarro.started", MC + "minagho_in", "minagho.present_now"], ["minagho_chivarro.started", MC + "chivarro_in", "chivarro.present_now"]],
        # The ledger's canonical started key (05 §6 ruling), read-only alias of the merged route's own StartedFlag.
        "minagho_chivarro.started": [["minachiv.started"]],
    }
    for key, groups in derived.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
