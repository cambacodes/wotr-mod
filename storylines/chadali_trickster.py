"""Chadali on the Trickster path: "The lucky charm" (Writer/handoffs/trickster/chadali.md; family F21).

Canon: the azata empyreal lord of the Trickster's Council, "the patron of serendipity" (Council_Socothbenoth intro
f728646c), a Vudrani woman in yellow silk who bakes cookies for luck (Council_Chadali/Cue_0001 f674c7cf, Cue_0002
ed7a31d6). "I believe in chance... I create chances... I am chance!" (Cue_0012 dc4fa930). She names the Commander the
Council's "lucky charm" (Council_1/Cue_0025 866558d6, Cue_0034 6b4e5052). She guesses that Cobblehoof's bag holds a
magical orange from the top of Axis (Council_5-1/Cue_0001 dfd57a47); the guess never comes true natively (the bag holds
the soul cauldron, Cue_0041 b936cf96), so the device makes the Commander's own joke true by the Commander's own hand.
If the Commander fights the Council she is knocked unconscious and bled of her essence (Shyka_Offer/Cue_0002 c3b8e7f1),
then pretends she never met them (Epilogues/Cue_0568 0ffd4b0b): hostility and a sealed hall, not death.

Her structure is bets, never motions: a coin called in the air, an orange that should not exist, and a question she
will not let the Commander settle with a coin. Her private dialog sits on the hall spawner (Council_Chadali/
AnswersList_0003) and her unit has no dialog component, so every physical scene is a hall scene; once the hall is
sealed she can only write. The courtship that the spine opens is chadali_wagers (Chapters 3 and 5, before the commit)
and chadali_fortunes (the cauldron, the needle and after the commit).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
P = "chadali.trickster."
UNIT = "75fd91d9d6119ea408a981680c659267"          # Chadali (hostile variant ChadaliEnemy 193c5f9b)
LIST = "e649f211c6b002a49a0c633061877927"          # Council_Chadali/AnswersList_0003
COOKIE = "ed7a31d6f063e0c4aa4ec4e08fab57c0"        # Council_Chadali/Cue_0002 "Eat a cookie for luck!" (clean return)
ERITRICE_LIST = "d07bffc320b9127459c40869ab3e8ee4"  # Council_Eritrice/AnswersList_0002
EMBER_LIST = "f2a35965e9bc601449498bd022b04d9d"     # CompanionDialogues/Ember/AnswersList_0003
# Epilogue pages carry no EpilogueAfter, like Eritrice's, Nocticula's and Dorgelinda's: RRT's epilogue sequence appends them
# in authored order. (An anchor on the Council's own page, BookPage_0187, is not in that sequence and was appended with a warning.)

STARTED = "chadali.started"
CLOSED = "chadali.closed"
COMMITTED = "chadali.committed"
LOST = "chadali.lost_at_council"
LATCHED = LOST + ".latched"
PRIMED = P + "primed"
RETURNED = P + "returned"
DECLINED = P + "declined"
COURTED = P + "courted"
LUCK_LENT = P + "cost.luck_lent"
LUCK_OWED = P + "cost.luck_owed"
ORANGE_TREE = P + "cost.orange_tree"
LATE = P + "cost.late"
GRUDGE = P + "cost.grudge"
ESSENCE = P + "cost.essence_taken"
APOLOGISED = P + "cost.apologised"
NEEDLE_OWED = P + "cost.needle_owed"
LATE_COMMITTED = P + "late_committed"
ORANGE_CALLED = "council.orange_called"
# The courtship's last beat before the commit (chadali_wagers): the question is asked only after it.
WAGERED = "chadali.wagers.the_real_wager"

RELATIONSHIP = dict(
    Title="The lucky charm",
    Description=("Chadali, the azata of serendipity, calls me the Council's lucky charm. I called a coin in the air "
                 "for her and it landed on its edge; she kept it. Now she wants to know whether I believe in luck, "
                 "or only in myself."),
    Objective="Win Chadali's wager",
    Guidance=("On the Trickster path, ask Chadali in the Council hall whether she believes in chance, then call a coin "
              "for her. Return to her private audience in Chapters 3 and 5. If the hall is sealed, she writes."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[LOST], FailureFlags=[],
    UnavailableOverrides={LOST: RETURNED},
    TricksterAccess={LOST: dict(detect=[LOST], device=P + "fought.lucky", returned=RETURNED)},
)

HALL_SEALED = P + "hall_sealed"
DERIVED = {LATE_COMMITTED: [["trickster.ever", STARTED], ["trickster.ever", RETURNED]],
           # The hall no longer opens: the Council's debrief closed it, it was fought, or the path was lost.
           HALL_SEALED: [["council.debrief_motion"], ["council.fought"], ["council.fought_nocta_allied"], ["trickster.failed"]]}


def ch(id, text, *choices, **kw):
    return n(id, "Chadali", text, *choices, portrait="Chadali", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Chadali", **kw)


def hall(id, title, entry, nodes, requires, forbids=(), delay=0, chapters=(3, 5), optional=False, **extra):
    """A physical scene on her own private list in the Council hall (while the hall is open)."""
    SCENES.append(scene(id, title, "Chadali", min(chapters), entry, nodes, requires=requires,
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=optional,
                        Relationship="chadali", Chapters=list(chapters), AnswerLists=[LIST], **extra))


def letter(id, title, nodes, requires, forbids=(), delay=0, **extra):
    """A remote scene: the hall no longer opens, so she writes (Chapter 5 only)."""
    SCENES.append(scene(id, title, "Chadali", 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="chadali", Remote=True, **extra))


# --- 4.1 council_active: the coin lands on its edge (primer), inline on her private list. -------------------------

SCENES.append(scene(P + "council.coin", "Heads or tails", "Chadali", 3, '"Before you go. Heads or tails?"', [
    nar("start", '''{n}Chadali has a coin out before you can answer: an old Elysian piece, worn smooth, with a sun on one face and a moon on the other. She flicks it high over the Council table, bracelets clinking, and watches it turn in the lamplight with her lips parted, as if no coin in the multiverse had ever been tossed before.{/n}''',
        c('[Call it in the air] "Heads, I\'m the Council\'s lucky charm. Tails, you\'re mine."', "edge",
          flags=(PRIMED, LUCK_LENT), mythic="Trickster", alignment=("Chaotic", 1)),
        c("Never mind.", abort=True)),
    nar("edge", '''{n}You are already moving as it falls. One knuckle, one breath of air across the table, and the coin comes down, rings once on the wood, and stands on its edge. It stays there. It wobbles, thinks about it, and stays.{/n}''',
        c("Continue", "both")),
    ch("both", '''"Both! It's both!" {n}Chadali claps her plump hands so hard that a white flower falls out of her hair and lands beside the coin.{/n}
"Heads and tails at once! Do you know how lucky that is? I've been flipping coins since before your crusade had a name, and I have never, ever seen one do that for anyone."
{n}She leans in until her nose nearly touches it, and does not breathe on it.{/n} "I'm keeping this. It's mine now. You'll have to come and get it."''',
      c("[Leave the coin standing.]")),
], requires=("trickster", "chadali.chance_asked"), forbids=(PRIMED, LOST), last=5, Relationship="chadali", Chapters=[3, 5],
    AnswerLists=[LIST], NativeReturnCue=COOKIE))


# --- The payoff: the orange (5-1) or the coin still standing (Chapter 3), a day or more later. ---------------------

SCENES.append(scene(P + "council.orange", "An orange! An orange!", "Chadali", 3, '"You kept the coin?"', [
    nar("open", '''{n}Chadali is waiting at the end of the Council table with both hands behind her back and the expression of someone who has been sitting on a secret for exactly as long as she could bear.{/n}''',
        c("[Trickster] [While she fusses with the ribbon on her parcel, drop the market orange from your pocket into Cobblehoof's empty bag.]",
          "start_orange", requires=(ORANGE_CALLED,)),
        c("Continue", "start_edge", forbids=(ORANGE_CALLED,)),
        c("[Leave the bag alone.]", "start_edge", requires=(ORANGE_CALLED,))),
    ch("start_orange", '''{n}Cobblehoof's bag lies on the table where he left it when the cauldron was handed over. Chadali picks it up to fold it, feels the weight, and turns it out: an orange rolls across the wood. Not a magical one. An ordinary orange with a Drezen market stall's chalk mark on the peel, the one you bought for two coppers this morning.{/n}
"An orange! An orange! I knew it!" {n}She holds it up to the light, turning it, delighted. Then she looks at you, and the dimples go away for a moment.{/n} "...You put it there."''',
      c('[Take the orange] "Half each. It\'s only fair: I lied about the bag."', "confession")),
    ch("start_edge", '''{n}The coin you called in the air is still standing on its edge in the middle of the Council table. A ring of cookie crumbs lies around it where someone has tried to knock it down with a biscuit and failed.{/n}
"It's still standing! Alichino tried twice and pretended he hadn't. Socothbenoth blew on it. Cobblehoof said 'Phrr' at it, which I think was a spell." {n}She beams.{/n} "I bet all of them a cookie apiece that it would stay up. Now they all owe me cookies."''',
      c('[Tip the coin over] "Chance had nothing to do with it. I balanced it."', "confession")),
    ch("confession", '''"I know." {n}She says it without any sulking at all, which is somehow worse.{/n} "I'm chance. I know what I did and what I didn't. That one was you."
"And now I have to tell you something, because cleaning up after oneself is mandatory." {n}She turns the coin over in her fingers.{/n} "When it stood up, I felt your luck go into it. A great deal of luck, all at once, just lying there. So I borrowed a little. I spent it on the Council, on believing we'll win. I'll pay it back. I always pay back."
{n}Then she sets the coin back on its edge between you, with one finger, and takes the finger away, and it stays. It stays because she wants it to; you can see her wanting it.{/n}''',
      c('[Let her keep the luck] "Keep it. Bet it on me."', flags=(STARTED, COURTED)),
      c('[Ask for it back] "I\'ll want that back. With interest."', flags=(STARTED, LUCK_OWED))),
], requires=("trickster.ever", PRIMED), forbids=(STARTED, LOST), delay=24, last=5, Relationship="chadali", Chapters=[3, 5],
    AnswerLists=[LIST], NativeReturnCue=COOKIE))


# --- The commit: the second cookie, and a question she will not let a coin answer. --------------------------------

hall(P + "council.second_cookie", "The second cookie", '"You said there would be more cookies."', [
    nar("open", '''{n}She has baked again. The parcel is wrapped in yellow silk and tied with a ribbon, and the smell of it reaches you from the far end of the hall: honey, and something like cardamom, and something that is not like anything at all.{/n}''',
        c("Continue", "start")),
    ch("start", '''{n}She holds the parcel out, then pulls it back before you can take a cookie.{/n}
"No. First a question, and you have to answer without flipping anything. The coin, every lucky thing that's happened since you walked in here." {n}Her bracelets are quite still.{/n} "Was it luck? Or did you make it happen?"''',
      c('[Tell her the truth] "It was me. It was always me."', "her_test"),
      c('[Flatter her] "It was luck. Yours."', "luck")),
    ch("her_test", '''"So you've been cheating chance on my account." {n}She folds her arms. She isn't smiling. You have never once seen her not smiling, and without the dimples she looks every bit the empyreal lord: old, and patient, and not at all soft.{/n}
"Then do it properly. You make things happen. You don't wait for them. Tell me what happens next, and make it true."''',
      c('[Ask her] "Next, you say yes."', "yes", flags=(COMMITTED,)),
      c('[Toss the coin for it] "Let\'s let chance decide."', "refused")),
    ch("refused", '''"No coins! Not for this!" {n}Chadali snatches the coin out of the air before it can land, and closes her fist on it.{/n}
"You're so mean. You'd leave this to chance? I am chance, and I say: not today. Ask me properly, later, when you mean it."''',
      c('[Accept her refusal] "I\'ll wait, then."', flags=(DECLINED,))),
    ch("luck", '''"Liar." {n}She says it quite kindly, and pops a cookie into her own mouth.{/n}
"You don't believe in luck. You believe in you. You've never once in your life waited for a coin to land." {n}She chews, and swallows, and looks at you with great fondness and no mercy at all.{/n} "Ask me again when you're ready to say so."''',
      c('[Leave the question open] "Let it rest."', flags=(DECLINED,))),
    ch("yes", '''"Yes." {n}She says it at once, and then looks astonished at herself, and then laughs, a real laugh, loud enough to echo off the empty chairs.{/n}
"Oh! You did it! You said it and it happened!" {n}She pushes the whole parcel into your hands and holds on to your wrists over it.{/n} "That's the luckiest thing I've ever seen. And it wasn't luck at all. I don't mind. I don't mind in the least."''',
      c("[Hold on to her.]")),
], requires=("trickster.ever", STARTED, WAGERED, "chadali.wagers.bet_her"), forbids=(COMMITTED, DECLINED), delay=48)


# --- The one priced second ask after her soft no. -----------------------------------------------------------------

hall(P + "after.orange_tree", "The seed from Axis", '"You came back."', [
    ch("start", '''{n}She does not offer a cookie. She offers a seed: pale, striped, warm as a coin that has been in a pocket.{/n}
"From the tree at the top of Axis. There is one, you know. Nobody believes me, which is entirely their loss." {n}She presses it into your palm and folds your fingers over it.{/n}
"Plant it in your city. A real one, with a gardener and a wall, not a trick. If it takes, ask me again and I'll say yes. If you won't spend a single stone on it, then it was only ever a game."''',
      c('[Plant the tree] "It gets the best corner of the citadel garden."', "planted", crusade=("Materials", -100),
        flags=(COMMITTED, ORANGE_TREE)),
      c('[Refuse the seed] "I don\'t garden."', "refused", flags=(CLOSED,))),
    ch("planted", '''"The best corner!" {n}She claps once, and then presses her folded hands against her mouth, and her eyes are very bright over them.{/n}
"It will take. I know it will. Not because of me. Because you paid for the wall." {n}She reaches up and tucks a white flower from her own hair behind your ear.{/n} "Yes. There. You don't even have to ask again. I've decided."''',
      c("[Keep the flower.]")),
    ch("refused", '''"Oh." {n}Just that. She takes the seed back out of your hand, carefully, as if it might bruise.{/n}
"Then it was a game. That's all right. I like games." {n}She is smiling, and it does not reach anywhere.{/n} "Go on, lucky charm. Don't forget to look around; you don't want to miss your luck."''',
      c("[Go.]")),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED,), delay=72)


# A live Trickster who never called her coin before the hall sealed peacefully: a wager by post (Sol r3 INT).
LATE_WAGER = P + "cost.late_wager"
letter(P + "council.late_wager", "A penny by post", [
    nar("start", '''{n}The Council's hall is sealed, and you never once called a coin for her in it. So you call one now, by post: a Drezen silver penny, worn smooth, wrapped in a note that names a wager and a stake.{/n}''',
        c('[Send the wager] "Heads, you write back. Tails, you write back anyway. The stake: a hundred crowns to your shrine by the grain market, whichever way it falls."',
          "reply", crusade=("Finances", -100), mythic="Trickster", alignment=("Chaotic", 1)),
        c("[Keep the penny.]", abort=True)),
    ch("reply", '''{n}The answer comes in a round, happy hand with a great many underlinings, and a cookie in the envelope, somewhat broken.{/n} "That's not a bet! Both faces are the same! That's cheating where I can see it, which is allowed, but only just."
"I'm keeping the penny. The shrine is keeping the hundred crowns; its roof leaks. And I'm writing back, which means you win, which I hate." {n}Further down, smaller:{/n} "Next time send me something true instead of something clever. Then I'll decide whether you're lucky."''',
      c('[Write back] "Something true, then. I missed you at the table."', flags=(STARTED, COURTED, LATE_WAGER)),
      c("[Let it rest there.]")),
], requires=("trickster", "trickster.ever", "council.debrief_motion"), forbids=(PRIMED, STARTED, CLOSED, LOST), delay=24)


# --- 4.2 Hall lost before the payoff (primed): the orange by courier. --------------------------------------------

ERITRICE_PS = nar("postscript", '''{n}Folded inside the silk is a second slip, in a stern, upright hand.{/n} "For the record: the chair opened this parcel, as all correspondence of a dissolved Council remains Council business. The chair ate one cookie. The chair regrets nothing. E."''',
                  c("[Fold the slips away.]"))

LETTER_CHOICES = (
    ('[Eat the orange] "It\'s a good orange."', (STARTED, LATE)),
    ('[Write back and send the coin home] "Keep the coin standing. I\'ll come for it."', (STARTED, LATE, COURTED)),
)

letter(P + "council.orange_letter", "The orange by courier", [
    nar("start", '''{n}A parcel comes up from the Drezen gate with the rest of the post: yellow silk, knotted twice. Inside are cookies, one bruised orange, and the coin you called in the air. It is standing on its edge in a nest of crumbs, and it has not fallen over on the road.{/n}''',
        c("Read on.", "letter")),
    ch("letter", '''{n}The note is in a round, happy hand with a great many underlinings.{/n} "The door to the hall doesn't open any more, so the luck had to travel. I'm sorry about the orange. It got bruised on the way; the road is not as lucky as I am. It is an orange, though. A real one. Don't tell Eritrice. C."''',
      *[c(text, "postscript", flags=flags, forbids=("eritrice.lost_at_council",)) for text, flags in LETTER_CHOICES],
      *[c(text, flags=flags, requires=("eritrice.lost_at_council",)) for text, flags in LETTER_CHOICES]),
    ERITRICE_PS,
], requires=("trickster.ever", PRIMED), forbids=(STARTED, LOST), delay=24,
    RequiresAnyGroups=[["council.debrief_motion", "trickster.failed"]])


# --- 4.3 council_fought: "Lucky you", and her price (the ER-2 device). ------------------------------------------

letter(P + "fought.lucky", "Lucky you", [
    nar("start", '''{n}The letter smells of honey and antiseptic. The round hand has pressed so hard that the nib has torn the paper twice.{/n}''',
        c("Continue", "coin", requires=(PRIMED,)),
        c("Continue", "hurt", forbids=(PRIMED,))),
    nar("coin", '''{n}Your coin is in the envelope. It is lying flat, heads up, the way nobody has been allowed to leave it since the day you called it.{/n}''',
        c("Read the letter.", "hurt")),
    ch("hurt", '''"You're so mean. You knocked me down and let them stick me with that needle. It hurt so, so much. Chance doesn't always bring you honey cookies. Sometimes you get sharp needles, and sometimes the needle is your lucky charm's fault."
"I don't want to see you." {n}Three lines further down, smaller:{/n} "...Why did you write?"''',
      c('[Bet on her luck] "Lucky you. I bet the whole fight you\'d walk away. I never lose a bet on you."', "refusal",
        mythic="Trickster", alignment=("Chaotic", 1))),
    ch("refusal", '''{n}The answer comes back fast, with three underlinings.{/n} "A bet? You bet on me while they held the needle? No. No, no, no. You don't get to be lucky about this. Luck is mine, and I'm not lending it to someone who stood by."
"If you want me at your table again, you pay. Not with a joke. Either you say sorry where the whole crusade can hear it, or you promise me that next time there's a needle, it goes into you instead of anyone you love. Pick one. Or don't write again."''',
      c('[Pay the Council\'s grievance: a public apology in Drezen] "Then hear it from the square."', "square",
        crusade=("Favors", -200), flags=(RETURNED, GRUDGE, ESSENCE, APOLOGISED)),
      c('[Promise her the needle] "Next time, the needle is mine."', "needle",
        flags=(RETURNED, GRUDGE, ESSENCE, NEEDLE_OWED)),
      c('[Refuse her terms] "I don\'t apologise for winning."', "shut", flags=(CLOSED,))),
    ch("square", '''{n}A week after the herald reads your apology in Drezen's square, with the whole garrison listening and not a few of them smirking, a parcel arrives. Cookies, a little burnt at the edges, as if someone had been too cross to watch the oven.{/n}
"I heard it. Everyone heard it. That was the point." {n}Underneath:{/n} "I'm still cross. Eat these anyway. They're for luck. You'll need it, now that you've spent so much of your dignity."''',
      c("[Eat one.]")),
    ch("needle", '''{n}The reply is short.{/n} "I'll hold you to that. I never forget a bet, and I never forget a promise, and this is both." {n}And then, in the corner, a small drawing of a needle, and beside it, crossed out several times and written again: a cookie.{/n}''',
      c("[Keep the letter.]")),
    ch("shut", '''{n}No answer comes. A month later a parcel arrives with no note in it at all: a handful of cookies gone hard.{/n}''',
      c("[Look at the bottom of the parcel.]", "shut_coin", requires=(PRIMED,)),
      c("[Put the parcel away.]", forbids=(PRIMED,))),
    ch("shut_coin", '''{n}Under the cookies lies your coin, flat, tails up.{/n}''',
      c("[Put the coin away.]")),
], requires=("trickster", LATCHED), forbids=(RETURNED,), delay=24, TricksterDevice=True, TricksterState=LOST)


# --- 4.4 Epilogue pages (Owner ChadaliEpilogue; after the Council's own page; no effects). -----------------------

EP = dict(last=6, Relationship="chadali")

SCENES.append(scene(P + "epilogue.commit", "", "ChadaliEpilogue", 6, "", [
    nar("page", '''{n}The spring after Threshold, a Vudrani woman in yellow silk came up the road to Drezen with a basket on her arm, and the gate guards afterwards swore that every die in the barracks came up sixes that day. She found the Commander, sat down uninvited, and put the basket between them: cookies, and a single orange.{/n}
"I've finished thinking," said Chadali. "You never did leave anything to chance, and I've decided that's the luckiest thing about you. So. There's a question you were too busy to ask. Ask it."''',
        c('[Ask her.] "Stay."', "stay"),
        c('[Take the orange, and not the question.] "Half each. Then we\'ll see."', "half"),
        c("[Give her back the coin.]", "coin"),
        paragraphs=(
            p("{n}The orange was bruised on one side, the way the first one had been, on the road from the sealed hall.{/n}", requires=(LATE,)),
            p("{n}She wore a Drezen silver penny on a string round her neck, and tapped it, once, as she sat down.{/n}", requires=(LATE_WAGER,)),
            p("{n}She had said no once, in the hall, and had meant it at the time. The hall was sealed now, and the seed she had meant to bring was still in her sleeve. She had come up the road anyway, to find out whether she still meant it.{/n}", requires=(DECLINED,)),
            p("{n}She had felt the coin fall at the rift, the night the Commander called in the luck she had borrowed, and had paid it all back at once, the way she did everything. She had come up the road, she said, to see what it had bought.{/n}", requires=("chadali.lastcall.called",)),
            p("{n}She had kept the apology the herald read in the square; she took it out of the basket, folded very small, and put it on top of the cookies, where the Commander would see it.{/n}", requires=(APOLOGISED,)),
            p("{n}Before anything else she held out a brooch-pin, point first, and then, while the Commander was still reaching for it, put it away again. \"No. The needle you owe me isn't a pin in a kitchen,\" she said. \"It's the next real one, the next time somebody comes for something you love with a needle in their hand. It stays on the books until then. I never forget a bet.\"{/n}", requires=(NEEDLE_OWED,)),
        )),
    nar("stay", '''{n}"Yes," said Chadali, before the word was quite finished. She took off her sandals and set them side by side under the Commander's table, the way a traveller does who means to stay. Then she pulled the white flower out of her hair, unpinned the yellow silk at her shoulder and let it fall to her waist, came round the table, and climbed into the Commander's lap as if she had been planning the route since the hall was sealed. "I bet you," she said against the Commander's mouth, both hands already busy at the Commander's belt, "that nobody comes through that door before morning."{/n}
{n}Nobody did. In the morning the coin stood on its edge on the windowsill, she lay asleep across most of the bed with honey in her hair, and the barracks had lost at dice all night. They went on losing for a month. Nobody could prove anything.{/n}'''),
    nar("half", '''{n}She peeled it with her thumbs, gave the Commander the larger half, and ate hers slowly. When she had finished she wiped her fingers on the yellow silk and said, "That's a yes, you know. You'll have to say it properly one day." The Commander did, in the end. It took most of a summer. She counted every day, and called each one lucky, and on the evening the Commander finally said it she latched the shutters herself, kicked her sandals across the room and pulled the Commander down onto the bed by both wrists, laughing, before the sentence was finished. She said afterwards it was the best bet she had ever won, and would not say what she had staked.{/n}'''),
    nar("coin", '''{n}She looked at the coin in her palm for a long time, turning it, sun and moon. Then she stood it on its edge on the table between them, where it stayed. "Keep it," she said. "I'll come and look at it sometimes." She did, every spring, and stayed a little longer each time, and never once said what she was waiting for.{/n}'''),
],
    requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED, "council.fought", "council.fought_nocta_allied", "sacrifice"),
    RequiresAnyGroups=[[STARTED, RETURNED]],
    # A soft no whose hall sealed before the seed could come keeps its later ask here (R2-1; Sol r3 INT).
    ForbidOverrides={"council.fought": RETURNED, "council.fought_nocta_allied": RETURNED, "sacrifice": "trickster.commander_back",
                     DECLINED: HALL_SEALED}, **EP))

SCENES.append(scene(P + "epilogue.declined", "", "ChadaliEpilogue", 6, "", [
    nar("page", '''{n}Chadali never did get her proper question. Every year, on the anniversary of the Council's first session, a parcel of cookies arrived in Drezen, with a coin in it lying flat, heads up, and no note at all.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, "council.fought", "council.fought_nocta_allied", HALL_SEALED),
    ForbidOverrides={"council.fought": RETURNED, "council.fought_nocta_allied": RETURNED}, **EP))

SCENES.append(scene(P + "epilogue.lucky_night", "", "ChadaliEpilogue", 6, "", [
    nar("page", '''{n}The coin stood on its edge on a shelf in the Commander's quarters for the rest of their life together, and on the nights Chadali stayed, she would flick it with one finger on her way to bed, just to watch it refuse to fall.{/n}''',
        paragraphs=(
            p("{n}It had fallen once, at the rift, the night the Commander called in her luck. She stood it back up herself the next morning, and would never say which face it had shown.{/n}", requires=("chadali.lastcall.called",)),
            p("{n}The Council went on meeting without her for a while, and then stopped. \"They pretend they never met,\" she said. \"I don't. I remember every one of them. I send them all cookies. Cobblehoof sends them back.\"{/n}", requires=("council.epilogue_ceased",)),
            p("{n}The Council never did work out whom it had forgotten to invite to its victory feast. Chadali left before the toasts with a tray of cookies under her arm, and never told them where she went.{/n}", requires=("council.epilogue_feast",)),
            p("{n}The Council went on convening, and she went on bringing cookies to it, and every session she left a chair empty beside her with a coin standing on its edge on the seat.{/n}", requires=("council.epilogue_convened",)),
            p("{n}The tree she swore came from the top of Axis took in the best corner of the citadel garden, and bore fruit in its second year. The gardener swore the oranges were ordinary. Nobody who ate one believed him.{/n}", requires=(ORANGE_TREE,)),
            p("{n}She never paid back the luck she had borrowed on the day of the coin. She said it was invested.{/n}", requires=(LUCK_LENT,), forbids=(LUCK_OWED, "chadali.lastcall.called")),
            p("{n}She paid back the borrowed luck, with interest, a little at a time, for the rest of the Commander's life. The Commander never once rolled lower than a four.{/n}", requires=(LUCK_OWED,), forbids=("chadali.fortunes.paid_back", "chadali.lastcall.called")),
            p("{n}She had paid back the borrowed luck all at once, with interest, in the hall, before the end. The Commander never once rolled lower than a four afterwards, and she said that was only the interest.{/n}", requires=(LUCK_OWED, "chadali.fortunes.paid_back"), forbids=("chadali.lastcall.called",)),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, DECLINED, "sacrifice"),
    ForbidOverrides={DECLINED: COMMITTED, "sacrifice": "trickster.commander_back"}, **EP))


# --- Reactions (exactly two reactors: Eritrice and Ember, each behind its reactor's availability guard). -----------

EMBER_GUARD = ("ember_dead", "ember_gone", "ember.absent")

SCENES.append(reaction("Eritrice", P + "react.eritrice_coin", (PRIMED,),
    '''"The chair notes a coin standing on its edge in the middle of the table. The chair has no procedure for this." {n}Eritrice writes, stops, writes again.{/n}
"Motion: that it be allowed to stand. All in favour? ...Carried. Chadali, stop clapping."''',
    answer_list=ERITRICE_LIST, forbids=("eritrice.lost_at_council", LOST), chapter=3, last=5, Chapters=[3, 5],
    entry='"About the coin on the table..."', portrait="Eritrice"))

SCENES.append(reaction("Ember", P + "react.ember_orange", (STARTED,),
    '''"The lady with the bracelets gave me two cookies and said one was for luck and one was for you. I ate yours. I think that was lucky for me." {n}Ember licks honey off her thumb.{/n}
"She told me you made a coin stand up on its edge and stay. Can you make one stand for me?"''',
    answer_list=EMBER_LIST, forbids=EMBER_GUARD, chapter=3, last=5, Chapters=[3, 5],
    entry='"Did you meet Chadali?"', portrait="Ember"))

SCENES.append(reaction("Ember", P + "react.ember_needle", (RETURNED,),
    '''"She wrote to me too. She said it hurt, and that she was cross with you, and then she drew a cookie at the bottom." {n}Ember folds the letter very small.{/n}
"People who are cross with you don't draw cookies. I think she's only sad she was brave by herself."''',
    answer_list=EMBER_LIST, forbids=EMBER_GUARD, chapter=5, last=5, Chapters=[5],
    entry='"Chadali wrote to you?"', portrait="Ember"))


def integrate(payload):
    """Register the new relationship's own derived keys. Scenes are added by expansion.py; world keys bind on demand."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
