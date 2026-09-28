"""Camellia: the cards, the bowl, the knife shop and the amulet (camellia_trickster, camellia_masks, camellia_evenings).

Her Varisian teacher left her a painted deck (her teacher: Camelia/Cue_0094, Cue_0096; the cards are authored, and named only
by their pictures). She feeds Mireya demon blood in a bowl (Cue_0108, Cue_0112). The amulet's spirit was her own invention
(FinalTruth Cue_0012 6aa5270c: "There is no Mireya. I made her up."); a Commander who turned on her before Q3 hears it from her
here, after the answer, in her own time. Two lies and a truth is played a second time, when the stakes have changed.
"""
from story_format import c
from storylines.camellia_trickster import (AMULET_KEPT, BARGAIN_COST, BARGAINED, BOWL_HELD, COMMITTED, DUE, GAME, GRAVE, OUT_LIED, P,
                                           SHE_WON, UNMASKED,
                                           cam, met, nar)
from storylines.camellia_masks import MIREYA, TWO_LIES, living

K = P + "cards."
DECK = K + "the_old_womans_deck"
BOWL = K + "a_bowl_for_mireya"
CUTLER = K + "the_cutler"
DECK_AGAIN = K + "the_deck_again"
SECOND_GAME = K + "two_lies_again"
AMULET = K + "the_amulet"

READ_BACK = P + "cards.read_back"         # the Commander turned her own reading back on her


# --- Before the kill: the old woman's deck. ----------------------------------------------------------------------------

living(DECK, "The old woman's deck", '"Are those cards?"', [
    cam("open", '''"My teacher's." {n}Camellia is laying them out on a camp stool in a cross, face down, with the care of a woman arranging a table for guests.{/n} "The old Varisian woman who came to live with us when I was small. When she died, they were the only thing of hers I asked for. Father thought I would want her jewellery. I didn't. The jewellery never told me anything."
{n}She squares the last card with one fingertip.{/n} "Sit. I shall read you. Everyone should be read at least once by someone who means it."''',
        c('"Do you believe in it?"', "believe"),
        c('"Go on, then."', "read")),
    cam("believe", '''"In the cards?" {n}She considers it seriously.{/n} "No. In the person turning them over? Always. My teacher used to say the cards don't tell the future. They tell you what the reader wants you to be afraid of. That's much more useful."''',
        c('"Go on, then."', "read")),
    cam("read", '''{n}She turns the first card. It shows a man in an apron with a cleaver, painted in faded reds.{/n}
"The butcher. Your past. You've killed a great many things to get where you are, and you have never once lost sleep over it." {n}Her eyes flick up.{/n} "Well. Not over the killing."
{n}She turns the second. Two women in one gown, back to back.{/n} "The twins. Your present. Someone near you has two faces." {n}She smiles, very sweetly.{/n} "I wonder who."''',
        c("Continue", "third")),
    cam("third", '''{n}She lays her hand flat on the third card, the future, and does not turn it.{/n}
"And now the future." {n}Her voice drops.{/n} "My teacher taught me to look at the person's face while I turn the last one. That's the real reading. The card is only the excuse." {n}She turns it, not looking at it, looking at you. It shows a woman with a veil over her face and a knife behind her back.{/n}''',
        c("[Keep your face perfectly still]", "still"),
        c('[Trickster] Reach across and turn the card back over. "Read it again. This time, look at the card."', "back"),
        c('"That\'s a pretty picture. Who is she?"', "who")),
    cam("still", '''{n}She watches your face for a long time. You give her nothing. At last she looks down at the card herself, and laughs, a little breathlessly.{/n}
"Oh. The widow. A woman in a veil with a knife behind her back." {n}She taps it.{/n} "And you didn't blink. You looked at me as if I had turned over a picture of a nice supper." {n}She gathers up the cards.{/n} "My teacher would have hated you. She hated people she couldn't read. So do I, usually."''',
        c("Continue", "close")),
    cam("back", '''{n}You turn the card face down. She stares at your hand on it, then at you. Then she turns it over again, and this time she looks at the picture herself: the veiled woman, the hidden knife. The colour goes out of her cheeks and comes back all at once.{/n}
"You made me read my own card," {n}she says softly.{/n} "That's cheating. That's the worst cheating there is." {n}She sits back.{/n} "My teacher said the cards always tell the truth to the one who turns them. I've never turned one for myself. I've never dared."''',
        c("Continue", "close", flags=(READ_BACK,))),
    cam("who", '''"Who is she?" {n}Camellia tilts her head at the veiled figure as though at an old acquaintance glimpsed across a ballroom.{/n} "My teacher called her the widow. She said the widow is the one who is already dressed for your funeral, before you know you're going to have one." {n}She smiles.{/n} "She always came up in my readings. Always. Every single time. My teacher used to laugh about it."''',
        c("Continue", "close")),
    cam("close", '''{n}She wraps the deck in a square of black silk, and ties it with a ribbon, and tucks it into her bodice, over her heart.{/n}
"Don't take it too seriously," {n}she says lightly.{/n} "They're only pictures. Painted by an old woman who liked to frighten little girls." {n}She pats the place where the cards are.{/n} "She was very good at it."''',
        c("[Leave her to her cards]")),
], requires=(MIREYA,), delay=48)


# --- Before the kill: a bowl for Mireya. -------------------------------------------------------------------------------

living(BOWL, "A bowl for Mireya", '"You look pleased with yourself. It\'s never a good sign."', [
    nar("open", '''{n}After the fighting, Camellia is kneeling among the demon dead at the edge of the field, with a shallow silver bowl in her lap. She has gathered something into it from a hulking corpse with too many joints. It is dark and thick and faintly steaming in the cold. She is humming.{/n}''',
        c("Continue", "her")),
    cam("her", '''"Mireya's supper." {n}She looks up, flushed and bright, as if you had caught her picking flowers.{/n} "Demon blood is very rich. It clears her head wonderfully. A few more bowls, my teacher would have said, and she'll be able to tell me her real name." {n}She holds the bowl out to you.{/n} "Would you hold it? My hands are cold, and the amulet likes to be held with both."''',
        c("[Hold the bowl]", "hold"),
        c('"I\'d rather not."', "refuse"),
        c('[Trickster] "Only if I get to say grace."', "grace")),
    cam("hold", '''{n}The bowl is heavier than it looks, and warm, horribly warm, through the silver. She takes the amulet from her throat and lowers the little bone snake into the blood, very slowly, the way one dips a spoon into soup to cool it. The blood moves, though nothing touches it.{/n}
"There," {n}she murmurs to the snake.{/n} "There, darling. Drink."''',
        c("Continue", "drink", flags=(BOWL_HELD,))),
    cam("grace", '''"Grace?" {n}Camellia's lips part in delighted shock.{/n} "Oh, do. Nobody has ever said grace for her."
{n}So you say it, over the steaming bowl, in the solemn singsong of a chaplain at a crusader's table: for what we are about to receive, may the Lord of Whatever-It-Was be truly sorry. She has to bite her lip to keep from laughing, and then she lowers the amulet into the blood with shaking hands.{/n} "That was blasphemous in at least three directions," {n}she whispers.{/n} "She loved it."''',
        c("Continue", "drink", flags=(BOWL_HELD,))),
    cam("refuse", '''"Rather not." {n}She takes the bowl back without offence, and balances it on her knees, and dips the amulet herself.{/n} "That's all right. Most people would rather not. My father's servants used to leave the room." {n}She glances up.{/n} "You haven't left, though. You're still standing there. I noticed."''',
        c("Continue", "drink")),
    nar("drink", '''{n}The blood goes down in the bowl. It goes down steadily, as though something small and patient were drinking it through a straw, until there is only a dark ring left on the silver. Camellia lifts the amulet and wipes it clean on her skirt with great tenderness.{/n}''',
        c("Continue", "after")),
    cam("after", '''"She's quieter now. Much quieter." {n}She fastens the amulet back at her throat.{/n} "She'll sleep for days. And then she'll be hungry again, and I'll find her something. There's always something, out here."
{n}She stands, brushing off her knees.{/n} "Thank you for staying. It's a very private thing. I've never let anyone watch before." {n}She considers you.{/n} "I wonder why I let you."''',
        c("[Walk back with her]"),
        c("[Trickster] While she fastens the amulet, cut your palm over the empty bowl, and speak to what stands at her back",
          "bargain", forbids=(BARGAINED,))),
    nar("bargain", '''{n}She has told you herself: a shaman goes to war with spirits at her side, always, and in a fight they grow loud. You speak to those, not to the snake in the amulet. You let your blood run into the silver while her head is bent over the clasp, and you say it very quietly: if she dies, by my hand or on my word, keep her three nights, and give her back to me.{/n}
{n}The blood in the bowl moves, though nothing touches it. It goes down in a slow ring until the silver is clean. Somewhere very close, something with no breath lets one out.{/n}''',
        c("Continue", "paid")),
    cam("paid", '''{n}She looks up from the clasp and sees your hand.{/n} "You've cut yourself." {n}She takes your wrist and turns the palm to the light, and her nostrils flare, very slightly.{/n} "And my bowl is clean. How strange. I only fed her half." {n}She wraps your palm in a strip torn from her own hem, very neatly.{/n} "Be more careful. The spirits out here will take anything that's offered, and they always come back for more."''',
        c("[Let her bind it]", flags=(BARGAINED, BARGAIN_COST))),
], requires=(TWO_LIES,), delay=48)


# --- After the return: the cutler. -------------------------------------------------------------------------------------

met(CUTLER, "The cutler", '"Where are we going?"', [
    cam("open", '''"Shopping." {n}She says it with the pleased air of a woman announcing a picnic.{/n} "There's a cutler in the lower city, an old dwarf who used to make knives for Hellknights before he lost his thumb. He has the best steel in Drezen and the worst manners. We shall get on beautifully."''',
        c("Continue", "shop")),
    nar("shop", '''{n}The shop is a hole in a wall under the old aqueduct, lit by one lamp and a forge the size of a bread oven. Blades hang from every beam like smoked hams. The dwarf behind the counter looks at Camellia, and then at you, and then back at Camellia, and says nothing at all, which in the lower city is a kind of welcome.{/n}''',
        c("Continue", "choose")),
    cam("choose", '''{n}She walks along the wall with her hands clasped behind her back, like a lady at an exhibition.{/n}
"You see, a knife is like a friend. Everyone thinks they want the biggest one. They don't. They want the one that fits." {n}She takes down a long, wicked thing with a serrated back.{/n} "This one is for people who want to be seen with a knife." {n}She puts it back. She takes down a plain little blade no longer than her hand.{/n} "This one is for people who want to use one."''',
        c('"Which one would you choose for me?"', "for_me"),
        c('"Which one did you use on me? At the end, I mean."', "used")),
    cam("used", '''"None of these." {n}She says it without a flicker.{/n} "You never saw the one I used, my friend. You were looking at my face. Everybody always is." {n}She smiles.{/n} "It's why I come to shops like this. To look at them properly, for once. I so rarely get to."''',
        c("Continue", "for_me")),
    cam("for_me", '''{n}She takes her time. She holds three different blades up against your hand, frowning, as a dressmaker holds up ribbons. At last she settles on one: short, heavy in the spine, with a grip wrapped in plain black cord. Nothing about it is beautiful. It fits your palm as if it had been made there.{/n}
"This one." {n}She closes your fingers round it.{/n} "It's honest. It won't pretend to be anything it isn't. I think you should have at least one honest thing about you."''',
        c('"I\'ll buy it."', "buy"),
        c('[Trickster] "Steal it for me. I want to see you do it."', "steal")),
    cam("buy", '''{n}The dwarf names a price that would make a quartermaster weep, and you pay it. Camellia watches the coins go down on the counter with an expression of great approval.{/n}
"You didn't haggle. Good. One should never haggle over a knife. It gives the knife ideas about what it's worth."''',
        c("Continue", "close")),
    cam("steal", '''{n}Camellia's eyes go very wide. Then she smiles, and turns to the dwarf, and asks him in a small, anxious voice whether he has anything in a lady's size, with mother-of-pearl, for a wedding present. By the time he has fetched down three trays and explained all of them, the black-corded knife is no longer on the counter, and she is thanking him warmly and promising to return with her husband.{/n}
{n}Outside, under the aqueduct, she presses it into your hand, and her fingers are shaking with laughter.{/n} "Don't ever let me do that again. I liked it far too much."''',
        c("Continue", "close")),
    cam("close", '''"There. Now we match." {n}She holds up her own small clean knife beside yours, blade to blade, in the grey light.{/n} "Mine is for ending things. Yours is for keeping them." {n}She sheathes hers.{/n} "Do try not to confuse the two. I shall be very cross if you do."''',
        c("[Walk back through the lower city]")),
], requires=("trickster.ever",), any_groups=[[GRAVE, DUE]], delay=24, optional=True)


# --- After her answer: the deck again. --------------------------------------------------------------------------------

met(DECK_AGAIN, "The deck, again", '"You brought the cards."', [
    cam("open", '''"I brought the cards." {n}She is sitting on the floor of your room with the black silk unfolded in front of her and the deck in her hands, shuffling, over and over.{/n} "I thought I would read us. Both of us, together. My teacher said you should never read a couple. She said the cards get jealous. I've always wanted to find out whether that's true."''',
        c("Continue", "read_back", requires=(READ_BACK,)),
        c("Continue", "cards", forbids=(READ_BACK,))),
    cam("read_back", '''"And last time you made me read my own card. The widow. I've been thinking about her ever since." {n}She stops shuffling.{/n} "I'm not afraid of her any more. I've been her. It was quite comfortable."''',
        c("Continue", "cards")),
    cam("cards", '''{n}She lays down two cards, side by side, face down. She puts one of your hands on the left one and her own on the right.{/n}
"Yours, and mine. We turn them together. And whatever they say, we don't argue with it. That's the rule." {n}Her fingers tighten on the back of her card.{/n} "Ready?"''',
        c("[Turn it over]", "turned")),
    nar("turned", '''{n}Your card shows a man with a mask held up in front of his face, laughing behind it. Hers shows the veiled widow, as it always does, with the knife behind her back. The two pictures lie side by side on the black silk. The laughing man's free hand is reaching towards the widow's knife. The widow's free hand is reaching towards his mask.{/n}''',
        c("Continue", "meaning")),
    cam("meaning", '''{n}Camellia is very quiet. Then she laughs, softly, disbelievingly.{/n}
"The fool, and the widow. She's reaching for his mask and he's reaching for her knife." {n}She touches the painted hands.{/n} "My teacher had a name for this. Two cards that reach for each other. She called it a marriage. She said it was the most dangerous spread there is, because neither card ever lets go first."''',
        c('"Then we won\'t let go."', "wont"),
        c('[Trickster] "I stacked the deck while you weren\'t looking."', "stacked")),
    cam("wont", '''"No." {n}She gathers up the two cards and holds them together, face to face, as though they were kissing.{/n} "No, I don't think we shall. I think we're far too stubborn." {n}She tucks them into her bodice together, apart from the rest of the deck.{/n} "I shall keep these two. The others can be jealous."''',
        c("Continue", "close")),
    cam("stacked", '''{n}She stares at you. Then at the cards. Then at you.{/n}
"You did not." {n}She searches your face, and you watch her fail to find the seam. It is not a thing you have seen before.{/n} "You couldn't have. I was watching your hands the whole time. I always watch hands." {n}Her voice drops.{/n} "Did you?"
{n}You don't answer. She begins to laugh, helplessly, and pulls you down onto the silk with her, scattering the rest of the deck across the floor.{/n}''',
        c("Continue", "close")),
    cam("close", '''"Whatever the truth is," {n}she says, some time later, from somewhere near your collar,{/n} "I'm not going to find out. I'm going to leave it exactly where it is. It's the first thing in my life I've ever wanted to leave alone."''',
        c("[Leave the cards where they fell]")),
], requires=("trickster.ever", COMMITTED), delay=72, optional=True)


# --- After her answer: two lies and a truth, again. -------------------------------------------------------------------

AGAIN_LEADS_WON = '''"You beat me the last time we played. I haven't forgiven you. I've been practising."'''
AGAIN_LEADS_LOST = '''"You lost the last time we played. I've let you think about it long enough."'''
met(SECOND_GAME, "Two lies and a truth, again", '"Play a game with me?"', [
    cam("open", '''"I thought you'd never ask." {n}She is already sitting up in bed, cross-legged, with her hair down and her knife on the pillow.{/n} "Two lies and a truth. Like the first time. I've been wanting to play it again for months, but I wanted to wait until the stakes were properly high."''',
        c("Continue", "won", requires=(OUT_LIED,)),
        c("Continue", "lost", requires=(SHE_WON,), forbids=(OUT_LIED,)),
        c("Continue", "hers", forbids=(OUT_LIED, SHE_WON))),
    cam("won", AGAIN_LEADS_WON, c("Continue", "hers")),
    cam("lost", AGAIN_LEADS_LOST, c("Continue", "hers")),
    cam("hers", '''{n}She folds her hands in her lap, like a girl at a recital, exactly as she did the first time.{/n}
"One. I have never been happier in my life than I am in this bed.
Two. I will never want the knife back.
Three." {n}She holds your eyes.{/n} "I love you."''',
        c('"One is the lie."', "one"),
        c('"Two is the lie."', "two"),
        c('"Three is the lie."', "three")),
    cam("one", '''"One?" {n}She laughs, but her eyes are strange.{/n} "No. One is true. I'm very happy. It's the strangest feeling. It's like being full after a meal I didn't eat." {n}She leans towards you.{/n} "Guess again."''',
        c('"Two, then."', "two"),
        c('"Three, then."', "three")),
    cam("three", '''{n}Her face does not change at all, and that is how you know you have said something terrible.{/n}
"No," {n}she says quietly.{/n} "Three is true. Three is the one I was most afraid you'd pick." {n}She looks down at her hands.{/n} "I said it last, the way people save the lie for last. You told me that once. I wanted to see if you'd remember."''',
        c("Continue", "two")),
    cam("two", '''"Two." {n}She lets out a breath she seems to have been holding for a very long time.{/n} "Yes. Two is the lie. Of course it is. I will want the knife back one day, darling. I can't help it. It's the one true thing about me that nobody can ever make untrue."
{n}She picks the knife up off the pillow and turns it in the candlelight.{/n} "But not today. And I'll tell you something else, since you won."''',
        c("Continue", "else")),
    cam("else", '''"I lied the first time too. When we first played. I said I had never lied to you, and you caught it, and I laughed." {n}She puts the knife back down, very carefully, point towards the door.{/n}
"That wasn't the lie. The lie was that I laughed because you were clever. I laughed because you were the first person who ever caught me, and I was so frightened I thought I might die." {n}She smiles.{/n} "Your turn. Three things. Make them good."''',
        c('[Trickster] "I love you. I love you. I love you."', "all"),
        c('"I\'m not afraid of you. I never was. I love you."', "mine")),
    cam("all", '''"That's three truths." {n}Her voice cracks on it, just slightly.{/n} "That's cheating. You always cheat. You cheat with the truth, which is the only thing I can't see through." {n}She pulls you down to her by the collar.{/n} "Don't ever stop."''',
        c("[Don't stop]")),
    cam("mine", '''"The first one's a lie," {n}she says at once, with enormous satisfaction.{/n} "You're a little afraid of me. You always have been. It's the nicest thing about you." {n}She pulls you down to her by the collar.{/n} "And the rest?"
{n}You don't answer. You don't have to. She has already found the seam.{/n}''',
        c("[Put out the candle]")),
], requires=("trickster.ever", COMMITTED, GAME), delay=72, optional=True)


# --- After her answer: the amulet. -------------------------------------------------------------------------------------

met(AMULET, "The amulet", '"You haven\'t fed Mireya in weeks."', [
    cam("open", '''"No." {n}She is sitting by the window with the bone snake of the amulet in her open palm, looking at it as one looks at a letter from a relative one has stopped writing to.{/n} "I don't need to. I've been meaning to tell you why. I kept putting it off, because it's the last thing, and after it there won't be any more secrets, and I don't know what I'll do without them."''',
        c('"Tell me."', "tell", forbids=(UNMASKED,)),
        c('"Tell me."', "known", requires=(UNMASKED,))),
    cam("known", '''"You already know the worst of it. I told you in Kenabres, with my father's house around us and my knife in my hand: there is no Mireya. I made her up." {n}She turns the little snake over.{/n} "What I never told you is why I kept wearing her afterwards. Even after I'd confessed. Even dead."
"Habit, I thought. It isn't habit. She was the only friend I ever had who couldn't look at me. I made her so that someone would always be near me who wasn't afraid."''',
        c('"And now?"', "why")),
    cam("tell", '''{n}She turns the little snake over. Its empty eye sockets catch the light.{/n}
"There is no Mireya. There never was. I made her up." {n}She says it gently, as one tells a child about a pet that has been given away.{/n} "There was no poor broken spirit in the ruins. There was only me, and a pretty bone amulet, and a need for a reason. A reason that would sound holy, or sad, or mad. Anything but what it was. So I invented a spirit who needed blood, and I fed her, and everyone felt so sorry for me."''',
        c('"I knew."', "knew"),
        c('"Why tell me now?"', "why"),
        c("[Say nothing]", "silent")),
    cam("knew", '''"You knew." {n}She looks up sharply, and then, slowly, she starts to smile.{/n} "Of course you knew. You've known what I was since the first time I lied to you, and you went on letting me. You called me back from the dead knowing it." {n}She closes her hand around the amulet.{/n} "You let me keep my imaginary friend." {n}Her eyes narrow, just slightly.{/n} "I wonder what you wanted in return. People always want something."''',
        c("Continue", "close")),
    cam("why", '''"Because I don't need a reason any more." {n}She opens her hand and looks at the snake.{/n} "I needed Mireya so that people would forgive me. So that there would be someone to blame, or pity. And then you came along, and you didn't need me to have a reason. You just... watched. You watched, and you stayed." {n}She shrugs, a small, bewildered movement.{/n} "She's out of work. Poor thing. I made her up and now I've made her redundant."''',
        c("Continue", "close")),
    cam("silent", '''{n}She waits for you to say something. You don't. She nods slowly, as if you had said exactly the right thing, and looks back down at the amulet.{/n}
"Yes. That's what I thought you'd say." {n}Very softly.{/n} "You never needed her. Only I did."''',
        c("Continue", "close")),
    cam("close", '''{n}She holds the amulet out to you, dangling from its cord.{/n}
"Here. You have her. Put her on your shelf, next to my list. Next to your name." {n}She folds your fingers around the little bone snake.{/n} "If anyone ever asks, tell them she was a very old and very beautiful spirit, and that she was mine. It isn't true. But it's the nicest thing I ever made."''',
        c("[Keep it]", flags=(AMULET_KEPT,))),
], requires=("trickster.ever", COMMITTED), delay=72, optional=True)
