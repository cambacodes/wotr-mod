"""Camellia: four days (camellia_trickster, camellia_masks, camellia_evenings, camellia_cards).

The market, where a dead woman buys flowers; the day of her funeral, a year on, or of her fall; the second dance, which
finishes the first; and a new friend, which is the most dangerous thing she can have. The last is the villain's day: she
does not change. She waits, and the Commander learns what waiting costs other people.
"""
from story_format import c, scene
from storylines.camellia_trickster import (CLOSED, COMMITTED, DANCED, DREZEN, FRIEND_WARNED, FRIEND_WATCHED, GRAVE, KILLED,
                                           KNIFE_NOTICED, NOT_TODAY, P, PRESENCE, REL, RET, SCENES, SHELF, UNIT, cam, met, nar)

D = P + "day."
MARKET = D + "the_flower_market"
ANNIVERSARY = D + "the_anniversary"
SECOND_DANCE = D + "the_second_dance"
NEW_FRIEND = D + "a_new_friend"


# --- The flower market (killed): a dead woman buys flowers. ----------------------------------------------------------

SCENES.append(scene(MARKET, "The flower market", "Camellia", 3, '"You look like you\'re going out."', [
    cam("open", '''"I am. We are. It's market day, and I've been dead for weeks, and I want flowers." {n}She pins the veil in place and offers you her arm.{/n} "Don't look at me like that. Dead women have every right to flowers. We're practically their best customers."''',
        c("Continue", "market")),
    nar("market", '''{n}The flower market is in the square below the cathedral, a dozen barrows under striped awnings, most of the stock gone brown at the edges from the cold. Camellia walks among them like a duchess at a fair. The sellers call out to the Commander. None of them call out to the veiled woman on the Commander's arm. Their eyes slide off her as rain slides off glass.{/n}''',
        c("Continue", "choose")),
    cam("choose", '''"Look at them," {n}she murmurs, delighted.{/n} "They can't see me at all. I could take anything I liked." {n}She stops at a barrow of hothouse roses, very expensive, very red.{/n} "When I was alive, sellers used to follow me round the stalls. They could tell I had money. Now they can tell I'm nothing at all."
"It's so restful, being nothing. You have no idea."''',
        c('"Buy what you like. I\'ll pay."', "pay"),
        c('[Trickster] "Take what you like. I\'ll distract them."', "take"),
        c('"You\'re not nothing."', "not")),
    cam("pay", '''"You'll pay." {n}She laughs softly.{/n} "The Commander of the crusade, paying for a dead woman's roses. The seller will tell his wife about it tonight. 'The Commander bought an armful of roses and walked off with nobody.'"
{n}She chooses, very carefully, one white rose, one red, and a sprig of something dark with berries on it that the seller warns her is poisonous. She thanks him and takes it anyway.{/n}''',
        c("Continue", "home")),
    cam("take", '''{n}You ask the rose-seller a very long question about the provenance of his soil. You ask him about his brother-in-law. You ask him whether the rumours about the Nerosyan tulip blight are true. By the time you have finished, Camellia is at the far end of the square with a whole barrow's worth of roses in her arms and the look of a girl who has stolen the moon.{/n}
"That was vulgar," {n}she whispers, when you catch up.{/n} "That was completely vulgar, and I've never been so happy in my life."''',
        c("Continue", "home")),
    cam("not", '''{n}She turns her veiled face to you and says nothing, while a flower-seller shouts about tulips and a cart goes by with a broken wheel.{/n}
"No," {n}she says at last, very quietly.{/n} "Not to you. That's the trouble, isn't it. I've found a way to be nothing to everyone in the world, and there's one person who won't let me." {n}She squeezes your arm.{/n} "Buy me a rose. A red one. Before I say something I mean."''',
        c("Continue", "home")),
    cam("home", '''{n}On the way back she stops at the cemetery gate, and goes in alone, and comes back without the flowers. When you ask, she says she left them on a grave she liked the look of.{/n}
"Mine," {n}she adds, after a moment.{/n} "It seemed rude not to. Everyone else had forgotten."''',
        c("[Walk her home]")),
    ], requires=("trickster.ever", RET, KILLED, GRAVE), forbids=(CLOSED,), delay=48, last=5, optional=True, Relationship=REL,
    Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN], InteractionHub=PRESENCE))


# --- The anniversary. --------------------------------------------------------------------------------------------------

met(ANNIVERSARY, "The anniversary", '"You\'re dressed in black."', [
    cam("open", '''"I am in mourning." {n}She smooths the black silk at her waist with both hands.{/n} "It's the anniversary. Well, not a year. I couldn't wait a year. It's the monthly anniversary. I've decided to keep them. I've never had an anniversary of anything before, except my birthday, and nobody ever came to that."''',
        c("Continue", "killed_a", requires=(KILLED,)),
        c("Continue", "dead_a", forbids=(KILLED,))),
    cam("killed_a", '''"One month since I died convincingly. One month since they put me under that plain little stone with the wedding lilies." {n}She lifts a glass of wine she will not drink.{/n} "To the dead. To me. To the only woman in Drezen who has read her own eulogy and found it wanting."''',
        c("Continue", "toast")),
    cam("dead_a", '''"One month since I fell by the wagons, and lay there, and heard nothing at all for a day and a half. One month since you told me I was overacting." {n}She lifts a glass of wine she will not drink.{/n} "To the dead. To me. To the silence, which I miss, and to the rude voice that ended it, which I don't."''',
        c("Continue", "toast")),
    cam("toast", '''"You're supposed to drink to the dead, you know. It's the custom." {n}She holds the glass out to you.{/n} "I never drink in company. Drink for me. Tell me what you remember about me. The way people do at a wake. I want to hear what they'd have said, if they'd known me."''',
        c('"I remember that you cheated at cards."', "cards"),
        c('"I remember your face when I told you to die."', "face"),
        c('[Trickster] "I remember that you were a terrible person and a wonderful liar, and nobody has missed you at all."', "missed")),
    cam("cards", '''"I never cheated at cards." {n}She is outraged.{/n} "I cheated at everything else, but never at cards. Cards are sacred. My teacher taught me that." {n}Then she stops.{/n} "You're lying. You're lying at my wake. That's..." {n}She begins to laugh.{/n} "That's exactly what I would have wanted. Say another one."''',
        c("Continue", "close")),
    cam("face", '''{n}She goes very still.{/n} "What did it look like? My face. I've always wondered. I've never seen it from the outside, at that moment. Nobody who has ever seen it has been in any condition to tell me."
{n}You tell her. You tell her it looked surprised, and then, just before the end, pleased. As if someone had finally told a joke she hadn't heard before.{/n}
{n}She listens to the end, and when you are done she puts down the glass very carefully.{/n} "Thank you," {n}she says.{/n} "That's the only thing I ever wanted anyone to tell me."''',
        c("Continue", "close")),
    cam("missed", '''"Nobody has missed me at all." {n}She repeats it slowly, savouring each word.{/n} "Oh, that's a beautiful eulogy. That's honest and cruel and entirely correct. The crusade has gone on as if I'd never existed." {n}She drinks, one small sip. You have never once seen her drink.{/n} "Except for one person. Whom I shall not name. At my own wake."''',
        c("Continue", "close")),
    cam("close", '''"Next month," {n}she says,{/n} "we'll do it again. And the month after. Until one of us is dead properly, and then the other one can do it alone." {n}She sets down the glass.{/n} "I'd prefer it to be me who does it alone. I'd do it so much better. But I won't insist."''',
        c("[Stay with her until the candle burns out]")),
], requires=("trickster.ever", COMMITTED, SHELF), delay=96, optional=True)


# --- The second dance: the lesson, finished. ---------------------------------------------------------------------------

met(SECOND_DANCE, "The second dance", '"Three steps and a turn?"', [
    cam("open", '''"You remembered." {n}She has already cleared the floor. The candles are in the corners again, as they were the first time, and she is barefoot, and her skirt is pinned up to the ankle.{/n} "I promised myself, the first time, that I would finish the lesson one day. I never finish lessons. I get bored halfway, or the other person dies. You're the first one who's still here for the second half."''',
        c("Continue", "danced_d", requires=(DANCED,)),
        c("Continue", "noticed_d", requires=(KNIFE_NOTICED,), forbids=(DANCED,)),
        c("Continue", "new_d", forbids=(DANCED, KNIFE_NOTICED))),
    cam("danced_d", '''"And last time you didn't look down. You felt the knife and you went on dancing." {n}She takes your left hand, and puts your right at her waist.{/n} "It's still there. It's always there. Tonight you may look, if you like."''',
        c("Continue", "dance")),
    cam("noticed_d", '''"And last time you found the knife, and said so, and I was very cross with you, and I have forgiven you entirely." {n}She takes your left hand, and puts your right at her waist.{/n} "It's still there. Tonight I shan't be cross."''',
        c("Continue", "dance")),
    cam("new_d", '''"We never had a first half, did we? I was dead too soon. So I shall teach you the whole thing at once, which is how I prefer to learn things, and people." {n}She takes your left hand and puts your right at her waist, a little lower than a dancing master would.{/n} "Three steps and a turn. Don't look at your feet."''',
        c("Continue", "dance")),
    nar("dance", '''{n}Three steps and a turn. She counts under her breath, one-two-three, one-two-three, and the candles go round the walls. She is closer than the dance requires, and then closer still. Your hand at her waist finds the knife strapped high on her thigh, and this time she stops, and puts her own hand over yours, and holds it there.{/n}''',
        c("[Unbuckle the strap]", "strap"),
        c("[Leave it where it is]", "leave")),
    cam("strap", '''{n}She watches your face while you do it. The buckle is stiff; she does not help. When it gives, the knife slides down into your palm, warm from her skin, and she lets out a long, shaky breath.{/n}
"There," {n}she whispers.{/n} "Now you're holding the only thing I've never let anyone hold. Put it somewhere I can see it."
{n}You lay it on the floor between two of the candles. She looks at it for a moment, and then she does not look at it again.{/n}''',
        c("Continue", "end")),
    cam("leave", '''"Leave it?" {n}Her breath catches, and her eyes go dark and bright at once.{/n} "You'd dance with me armed. You'd lie down with me armed." {n}She presses closer, until you can feel the hilt between you both.{/n} "Nobody has ever wanted me with the knife. They always want me to take it off first. As if that made any difference."''',
        c("Continue", "end")),
    nar("end", '''{n}The dance stops somewhere in the middle of a turn, and neither of you notices. She kisses you as she fences, close and quick and always coming in, and she is laughing against your mouth, and her fingers are in your collar, then under it. One of the candles goes out, and then another. She pulls you down onto the bare boards in the middle of the cleared floor, one-two-three, and the last thing she says before she stops counting altogether is that this, at last, is the end of the lesson.{/n}''',
        c("[Let the last candle burn down.]")),
], requires=("trickster.ever", COMMITTED, SHELF), delay=72, optional=True, living=())


# --- A new friend: the villain's day. ----------------------------------------------------------------------------------

met(NEW_FRIEND, "A new friend", '"Who was that you were laughing with?"', [
    cam("open", '''"Oh, that was Ilse." {n}Camellia is cutting flowers for a vase, her back to you, with neat, precise snips.{/n} "A quartermaster's girl. She mends the banners. She has the loveliest laugh, like a wren. We've been taking walks together in the evenings. She tells me all about her sweetheart in the Third Company and her mother in Tabor and the ribbons she means to buy for her wedding."
{n}Snip.{/n} "She says I'm the best friend she's ever had."''',
        c("Continue", "list")),
    nar("list", '''{n}Something in the way she says it makes you look at the shelf over your bed. The list is there, where it has always been, or the ash of it, or the memory. You think of the names on it that are not yet crossed out. You think of the names that are. You find that you know, without being told, whose name will be written at the bottom of the list tonight.{/n}''',
        c("Continue", "ask")),
    cam("ask", '''"You're looking at me the way you look at demons." {n}She puts the scissors down.{/n} "Say it. You'll feel better. I shan't be offended. I'm never offended by the truth. It's so rare."''',
        c('"She\'s going on the list."', "list_ask"),
        c('[Trickster] Tell Ilse, tomorrow, that Camellia has consumption and must be allowed to rest. Alone. For months.', "warn"),
        c('"She\'s your friend. That\'s your business."', "watch")),
    cam("list_ask", '''"She's going on the list." {n}Camellia agrees serenely, and picks the scissors up again.{/n} "She went on the list the first evening, when she laughed at my joke about the chaplain's hat. She doesn't know. That's what makes it lovely. She gets to be happy for such a long time first."
{n}Snip.{/n} "You're wondering whether I'll do it. So am I. That's the most exciting part. I honestly don't know. I haven't decided. You've made me so very indecisive."''',
        c('[Trickster] Tell Ilse, tomorrow, that Camellia has consumption and must be allowed to rest. Alone. For months.', "warn"),
        c('"Then I\'ll be watching."', "watch")),
    cam("warn", '''{n}It takes you a morning. You find Ilse in the banner loft with a mouthful of pins, and you tell her, gravely, as a Commander tells a soldier bad news, that the lady Camellia is ill, very ill, with a coughing sickness that is most catching, and that the kindest thing a friend can do is to stay away until the physicians say otherwise.{/n}
{n}Ilse cries a little. She sends a ribbon. She does not come back.{/n}''',
        c("Continue", "warned")),
    cam("warned", '''"Consumption." {n}Camellia holds up the ribbon, blue, with a little bow.{/n} "You gave me consumption. Ilse sent me this and a very sweet note, and now she crosses the yard when she sees me coming, with her hand over her mouth."
{n}She winds the ribbon round her finger, and unwinds it.{/n} "You took my friend away. You lied to her to do it. You made her afraid of me, for no reason she'll ever understand." {n}She smiles, slowly.{/n} "You lied to a girl to take my plaything away. How very possessive of you." {n}She ties the ribbon round her wrist, tight enough to mark.{/n} "I shall keep this. It's evidence of what you'll do when something of mine is in the way."''',
        c("[Take her hand]", flags=(FRIEND_WARNED,))),
    cam("watch", '''"You'll be watching." {n}She turns round at last, and looks at you as if you were a card she had not expected to turn up.{/n}
"You could have lied to her. You could have told her I was ill, or mad, or married. You're so good at it." {n}Her voice is perfectly pleasant.{/n} "You didn't. You decided that a girl who mends banners is worth less to you than finding out what I'll do. I shall remember that about you. I'm writing it down somewhere you'll never find."''',
        c("Continue", "cost")),
    nar("cost", '''{n}Down in the yard, Ilse is laughing, like a wren. She sees you at the window and waves, and holds up a blue ribbon for you to admire: for her wedding, she calls up. For the Third Company's sergeant. The lady Camellia helped her choose it.{/n}
{n}Camellia waves back, very prettily, and does not take her eyes off your face while she does it.{/n}''',
        c("[Wave back]", flags=(FRIEND_WATCHED,), alignment=("Evil", 1))),
], requires=("trickster.ever", COMMITTED, NOT_TODAY), delay=96, optional=True, living=())
