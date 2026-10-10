"""Chadali: the small hours of the hall - her power, her bad days, the first session, and the wait for the question.

Every scene is in the Council hall, on her own private list (Council_Chadali/AnswersList_0003). Canon anchors:
- "I heal some, make some stronger... But truth be told, I can't compete with the gods!" (Council_Chadali/Cue_0007 0d35409a);
- the first sessions: "Right! Of course! No one knows how it will turn out - but we must always believe in our good
  fortune." (Council_1/Cue_0016 9f006d71); "Don't be so tough on our new friend! They're our lucky charm and will bring us
  good fortune!" (Council_2/Cue_0013 bd0307cf); "And I would be happy to help, even without the votes. I'm sorry that I
  can't." (Council_2/Cue_0031 30f2736d);
- Socothbenoth, who brought the Commander to the Council (Council_1/Cue_0007 b5aa61e8) and introduced her as "the
  patron of serendipity" (Council_1/Cue_0033 c3cc0d39);
- the bracelets, earrings, white flowers and white-gold ring (Cue_0001 f674c7cf, Cue_0018 51c885e2, Cue_0019 054852ef).
Her gifts and her bad days are her own telling in her own voice.
"""
from story_format import c, scene
from storylines.chadali_trickster import CLOSED, COMMITTED, DECLINED, LIST, LOST, STARTED, ch, nar
from storylines.chadali_wagers import BORN, CHARM, REAL_WAGER
from storylines.chadali_fortunes import NIGHT

SCENES = []
H = "chadali.hours."

BLESSING = H + "make_some_stronger"
EARRING = H + "an_unlucky_day"
FIRST = H + "our_new_friend"
SOCOTH = H + "who_brought_you"
PRISONER = H + "a_cookie_for_the_enemy"
WAITING = H + "not_today"
SCAR = H + "for_luck"

# Outcomes the epilogue reads.
BLESSED = H + "blessed"
REFUSED_BLESSING = H + "refused_blessing"
EARRING_FOUND = H + "earring_found_openly"
FIRST_SIGHT = H + "first_sight"
PRISONER_FED = H + "prisoner_fed"
PRISONER_REFUSED = H + "prisoner_refused"
SCAR_KEPT = H + "scar_kept"


def hour(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5)):
    """A physical sitting on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Chadali", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="chadali", Chapters=list(chapters), AnswerLists=[LIST]))


# --- 1. Make some stronger: her own power. ------------------------------------------------------------------------

hour(BLESSING, "Make some stronger", '"You said you heal some, make some stronger."', [
    ch("start", '''"I do!" {n}She holds up her hands, palms out, as if showing that there is nothing in them.{/n} "Not very much. Not like the gods. Iomedae can make a whole army stand up straight. I can make one person feel like it's a good morning."
"Let me do it for you. Before the next battle. It won't stop a sword." {n}She wiggles her fingers.{/n} "It'll just make you believe, for a moment, that the sword might miss. That's all luck ever is, really. That moment."''',
      c('[Hold out your hands.] "Do it."', "bless"),
      c('"I don\'t want to believe the sword might miss. I want to make sure it does."', "refuse"),
      c('"Why don\'t you do it for the whole army?"', "army")),
    ch("army", '''"Because it's not a spell. It's a... it's a me." {n}She frowns, looking for the words.{/n}
"When I do it for someone, a little of me goes into them. Not much. It comes back. But if I did it for the whole army, there'd be none of me left for a while, and I'd just be a lady in a yellow dress, sitting in a hall, very tired." {n}She smiles.{/n} "I'm allowed to choose who. That's the one selfish thing about being chance."''',
      c('[Hold out your hands.] "Then choose me."', "bless"),
      c('"Then keep it. Save it for someone who needs it more."', "refuse")),
    ch("bless", '''{n}She takes your hands in both of hers. Her palms are warm and a little floury, and she closes her eyes, and for a moment nothing happens at all.{/n}
{n}Then something does. It is not light and it is not warmth. It is the feeling of walking into a room and knowing, without any reason, that everyone in it is glad you came.{/n}
"There." {n}She opens her eyes, a little breathless.{/n} "That's the whole of it. It's not much. It's not nothing."''',
      c('"It\'s not nothing."', "after", flags=(BLESSED,))),
    ch("refuse", '''{n}Her hands stay out a moment longer, and then she folds them in her lap.{/n}
"You're very strange." {n}Without offence.{/n} "Everyone else in the world wants to feel lucky. You want to feel ready." {n}She thinks about it.{/n}
"All right. I won't push it on you. It doesn't work if you push it, anyway; it just slides off." {n}A small, stubborn smile.{/n} "I'll just stand very near you before battles. It leaks. You can't stop it leaking."''',
      c("Continue", "after", flags=(REFUSED_BLESSING,))),
    ch("after", '''"Go on. Go and win something." {n}She waves you off with both hands.{/n} "And when the sword misses, don't tell me it was you. I know it was you. Let me think it was me, just this once."''',
      c("[Go.]")),
], requires=(BORN,), forbids=(BLESSING,))


# --- 2. An unlucky day. ------------------------------------------------------------------------------------------

hour(EARRING, "An unlucky day", '"Are you... crawling under the table?"', [
    nar("open", '''{n}There is a pair of feet in yellow silk slippers sticking out from under the Council table, and a great deal of muttering. A tray of cookies lies upside down on the floor. A cup has been knocked over, and its contents have run across Alichino's side of the table, which you suspect is the only good thing that has happened today.{/n}''',
        c("Continue", "start")),
    ch("start", '''"I lost an earring." {n}Muffled, from under the table.{/n} "The white-gold one. The one that clinks. I dropped the tray, and then I knocked the cup, and then I bent down and it just... went."
{n}She wriggles out backwards, flushed and dusty, and sits on the floor.{/n} "I'm having an unlucky day. Me! I'm chance! It's the most humiliating thing that's ever happened to anyone."''',
      c('[Get down on the floor and look for it with her.]', "search"),
      c('[Trickster] [Palm a coin, "find" the earring behind her ear.] "Here it is."', "trick"),
      c('"How can chance have an unlucky day?"', "how")),
    ch("how", '''"Easily!" {n}Indignant.{/n} "Chance goes both ways. Nobody remembers that. They think I'm only the nice way. I'm both. Heads and tails."
"Usually I stand on the heads side. Today I slipped." {n}She sniffs.{/n} "It happens every few centuries. It's always on a day when I've baked something nice."''',
      c('[Get down on the floor and look for it with her.]', "search"),
      c('[Trickster] [Palm a coin, "find" the earring behind her ear.] "Here it is."', "trick")),
    ch("search", '''{n}You get down on the flagstones beside her. It takes half an hour, and involves a great deal of dust, three spiders, a cookie from what must be the Council's first session, and one of Eritrice's quills.{/n}
{n}You find it at last in a crack between two stones under Cobblehoof's chair, and hold it up. It clinks.{/n}
{n}Chadali stares at it, and then at you, dusty and on your knees, and her face does something complicated.{/n} "You didn't trick it. You just looked."''',
      c('"Sometimes that\'s all it takes."', "found", flags=(EARRING_FOUND,))),
    ch("trick", '''{n}You reach behind her ear and bring back your hand with something white-gold in it, glinting.{/n}
{n}She reaches for it, and stops. She looks at it closely. It is a coin, not an earring; you have had to improvise.{/n}
"That's not my earring." {n}Flatly. Then, despite herself, her mouth twitches.{/n} "That's a very good trick and a very bad earring."''',
      c("[Put the coin away. Get down on the floor and look properly.]", "search")),
    ch("found", '''{n}She takes the earring and puts it back in, and shakes her head so it clinks, and the sound seems to put something right.{/n}
"There. Heads side again." {n}She leans against you on the floor, dusty and relieved.{/n}
"I'm going to remember this. The day I was unlucky, and you got down on the floor." {n}A small laugh.{/n} "That's much better than being lucky. Don't tell anyone I said that; I'll lose my job."''',
      c("[Help her up.]")),
], requires=(STARTED,), forbids=(EARRING,))


# --- 3. Our new friend: the first sessions. ------------------------------------------------------------------------

hour(FIRST, "Our new friend", '"Do you remember the first session?"', [
    ch("start", '"Of course I do! I remember everything that makes me happy, and it made me very happy." {n}She settles in, like someone about to tell a favourite story.{/n}\n"Socothbenoth brought you in, and everyone looked at you as if you were a new kind of beetle. I remember Eritrice asking you questions. Shyka laughed at something nobody else could see. Cobblehoof said \'Phrr\'."\n"And I looked at you and said, just look how cute they are! They\'ll be our lucky charm!" {n}Her eyes gleam.{/n} "And everyone laughed. And I was right."',
      c('"Why did you defend me? You\'d never met me."', "why"),
      c('"You decided that fast?"', "fast")),
    ch("fast", '''"Faster!" {n}She claps.{/n} "I decided before you'd sat down. You came through the door and stood there looking at all of us, a demon lord and a devil and a hippogriff and the Eldest and two empyreal lords, and you weren't frightened at all. You were counting the exits."
{n}She laughs.{/n} "Everybody who's frightened of us counts the exits. You were counting them the way a general does. To see which one we'd come in by."''',
      c('"And that made me lucky?"', "why")),
    ch("why", '''{n}She is quiet for a moment, turning her bracelet.{/n}
"You looked like someone who'd been unlucky for a very long time and had decided to do something about it." {n}Softly.{/n}
"I know that look. I see it on the faces of the people who pray to me the hardest. The ones who don't expect anything, and pray anyway." {n}She looks up.{/n} "I've never been able to help most of them. I thought, maybe this one I can. So I called you our lucky charm. It's the best thing I know how to call anyone."''',
      c('"You did help. You still do."', "helped", flags=(FIRST_SIGHT,)),
      c('"You couldn\'t even give me votes, in the second session."', "votes", requires=("chadali.aid_regretted",))),
    ch("votes", '''"I know!" {n}She covers her face.{/n} "You asked for material aid and I said I'd be happy to help even without the votes, and I was sorry I couldn't. I was so sorry. I sent you good wishes instead." {n}Through her fingers:{/n} "That's a terrible thing to send an army."
{n}She lowers her hands.{/n} "But I meant them. Every one. That's all I had that day. Now I have cookies, and you." {n}She beams.{/n} "I'm much better equipped."''',
      c("Continue", "helped", flags=(FIRST_SIGHT,))),
    ch("helped", '"Good." {n}She says it very firmly, as if settling an old account.{/n} "Then I was right, and everybody who laughed at me in the first session was wrong, and I\'m going to remind them at the next one."\n"I\'ll put the little squiggle on my own copy. They\'ll hate that."',
      c("[Leave her pleased with herself.]")),
], requires=(CHARM,), forbids=(FIRST,))


TELL = (
    c('"It\'s about his sister. He means to bring her down, and he wants you to be the coin he tosses."', "truth", flags=("chadali.hours.refused_socothbenoth",)),
    c('[Trickster] "Do it. Let him owe you. Let him owe us."', "use", flags=("chadali.hours.obliged_socothbenoth",)),
)


# --- 4. Who brought you: Socothbenoth asks her for a favour. ---------------------------------------------------

SOCOTH_REFUSED = H + "refused_socothbenoth"
SOCOTH_OBLIGED = H + "obliged_socothbenoth"

hour(SOCOTH, "Who brought you", '"Socothbenoth was here. I passed him on the stair."', [
    ch("start", """"He was." {n}She is sitting very straight, turning her ring, and she has not offered a cookie.{/n} "He brought me flowers. Real ones, from somewhere warm. He called me darling eleven times. I counted."
"And then he asked me for a favour." {n}She looks at the flowers, not at you.{/n} "One night, he wouldn't say which, he wants all of my luck. Every morning's worth, all at once, sent to him and nobody else. He said it was for family. He said it would make someone very, very surprised." """,
      c('"And the crusade? That night, it gets nothing."', "crusade"),
      c('"Do you want to do it?"', "want")),
    ch("crusade", '"Nothing. That\'s why I haven\'t agreed." {n}She picks a fallen petal off the table.{/n} "My worshippers need it too. Eleven darlings and a bunch of flowers don\'t settle that."\n"He wouldn\'t name the night. You know him better than I do. What\'s he hiding?"',
      *TELL),
    ch("want", '"I want to know what he\'s buying." {n}Her ring turns once.{/n} "He asked for everything, and wouldn\'t tell me why. That\'s a very bad bet."\n"My priests ask for healing. The crusade asks for strength. His flowers are lovely. They still haven\'t answered my question."',
      *TELL),
    ch("truth", '{n}She puts the flowers in the bin, stem first.{/n} "His sister. Of course. She\'s dangerous enough without my helping him spring something on her."\n"I\'ll tell him no. He can call me darling twelve times if he likes." {n}She pulls a sheet of paper towards her.{/n} "Stay. I want you to hear what I actually write."',
      c("[Stay while she writes her no.]")),
    ch("use", '"Let him owe us? First he tells me the night and what he means to do." {n}She plucks one flower out of the bunch.{/n} "He can have one morning\'s share if I like the answer. The rest goes where I send it."\n"And he owes help to my worshippers, not another bouquet. You may take a favour for the introduction. You don\'t get to promise my luck."',
      c("[Leave her with the flowers.]")),
], requires=(STARTED,), forbids=(SOCOTH,))


# --- 5. A cookie for the enemy. ---------------------------------------------------------------------------------------

hour(PRISONER, "A cookie for the enemy", '"You\'ve wrapped a parcel for someone else."', [
    ch("start", '''"For a prisoner." {n}She says it as if it were the most natural thing in the world.{/n} "There's a cultist in your dungeons in Drezen. One of Deskari's. They caught him last week. He hasn't eaten. He says he'd rather die than take bread from the crusade."
"But I'm not the crusade." {n}She pats the parcel.{/n} "I'm just a lady with cookies. Will you take it down to him?"''',
      c('"He\'s a murderer. He burned villages."', "murderer"),
      c('"Why? He\'d kill you if he could."', "why"),
      c('"All right."', "fed", flags=(PRISONER_FED,))),
    ch("murderer", '''"I know." {n}Very quietly.{/n} "I know what he did. I felt some of them go. The villages."
{n}She does not take the parcel back.{/n} "He's still going to be hanged, probably. I'm not asking you to let him go. I'm asking you to let him eat a cookie first. It doesn't make what he did smaller. It just makes the world a tiny bit less like what he wanted it to be."''',
      c('"All right. I\'ll take it down."', "fed", flags=(PRISONER_FED,)),
      c('"No. He doesn\'t get kindness. Not from you, not from me."', "refused", flags=(PRISONER_REFUSED,))),
    ch("why", '''"He would." {n}She nods.{/n} "He'd kill me, and then he'd kill you, and then he'd go to sleep and dream about the Abyss. I know."
"That's why." {n}Simply.{/n} "The Abyss told him nobody would ever be kind to him again. I'd like the Abyss to be wrong about something. Just once. Just one cookie's worth."''',
      c('"All right. I\'ll take it down."', "fed", flags=(PRISONER_FED,)),
      c('"No. He doesn\'t get kindness. Not from you, not from me."', "refused", flags=(PRISONER_REFUSED,))),
    ch("fed", '''"Thank you." {n}She beams, and then her face grows serious.{/n}
"Don't tell him it's from me. Tell him it's from someone who thinks he's wrong about everything." {n}She tucks a white flower into the knot of the parcel.{/n}
"He won't eat it, probably. Or he will, and hate himself. Either way, he'll have to think about it. That's all I want. One thought that isn't the Abyss's."''',
      c("[Take the parcel.]")),
    ch("refused", '''{n}She takes the parcel back and holds it in her lap for a long time.{/n}
"All right. It's your prison. It's your war." {n}Her voice is steady and not at all sulky, which is worse.{/n}
"I think you're wrong. I think you're wrong and I think you know why you're wrong, and you're doing it anyway because you're tired and angry and people you love died in those villages." {n}She looks up.{/n} "That's allowed. I'll eat it myself. I'll think about him while I do."''',
      c("[Let her.]")),
], requires=(BORN,), forbids=(PRISONER,))


# --- 6. Not today: waiting for the question. ------------------------------------------------------------------------

hour(WAITING, "Not today", '"You\'re very quiet."', [
    nar("open", '''{n}She is baking. There is no oven in the hall, and she is baking anyway, in a way that involves a great deal of kneading, some very pointed looks at a bowl, and no heat of any kind. Flour is in her hair. Flour is on the Council table. Some of it is on Alichino's chair, in the shape of a small rude word.{/n}''',
        c("Continue", "start")),
    ch("start", '''"I'm not quiet. I'm concentrating." {n}She kneads harder.{/n} "I'm going to bake the best batch I've ever baked, and I'm not going to burn a single one."
"And you're not allowed to ask me today." {n}Very fast, without looking up.{/n} "Not the question. The bet's still on. It's just that I've got flour everywhere and I look like a ghost and I want to be wearing the yellow when you ask. The good yellow."''',
      c('"You look perfect."', "perfect"),
      c('"Are you nervous?"', "nervous"),
      c('[Tease] "What question?"', "tease")),
    ch("tease", '''{n}She throws a handful of flour at you. It is a remarkably accurate throw.{/n}
"You know exactly what question. You're the one who has to ask it! You're doing it on purpose. You're making me say it so I'll go red." {n}She has gone red.{/n} "Not today. Go away. Come back when I'm yellow."''',
      c('"Are you nervous?"', "nervous")),
    ch("perfect", '''"I look like a sack of flour." {n}She stops kneading, though, and pushes a strand of floury hair out of her face with her wrist.{/n}
"...You really think so?" {n}And then, before you can answer:{/n} "No, don't answer. If you answer I'll believe you, and then I'll want you to ask, and I've got dough under my nails."''',
      c('"Are you nervous?"', "nervous")),
    ch("nervous", '''{n}She is quiet, her floury hands gone still in the bowl.{/n}
"I don't get nervous," {n}she says at last.{/n} "I'm getting nervous. I don't care for it. I can give you the odds on an army. I can't give you the odds on this, and I'm chance. It's insulting."
{n}She looks up at you.{/n} "I'm chance, and I don't know what I'll say. Isn't that silly? I know what I'll say. I don't know if I'll be brave enough to say it."''',
      c('"I\'ll ask when you\'re ready. Not before."', "ready"),
      c('"You\'ll be brave enough. You were born in a meteor shower."', "brave")),
    ch("ready", '''"When I'm yellow." {n}She nods, and goes back to kneading, more gently.{/n} "And when I've stopped shaking. Probably not at the same time. You'll have to pick one."''',
      c("[Leave her to her dough.]")),
    ch("brave", '''{n}She laughs, a little shakily.{/n} "That wasn't brave. That was just arriving. Anybody can arrive." {n}She thinks about it.{/n}
"I'm brave all the time. This is different. This is being brave where you can watch me do it, and I hate it." {n}She shoos you with a floury hand.{/n} "Go on. Not today. Soon."''',
      c("[Leave her to her dough.]")),
], requires=(REAL_WAGER,), forbids=(WAITING, COMMITTED, DECLINED))


# --- 7. For luck: after the commit, a wound and a scar. -----------------------------------------------------------

hour(SCAR, "For luck", '"It\'s only a scratch."', [
    nar("open", '''{n}It is not only a scratch. You came to the hall straight from the field without stopping at the healers, and somewhere on the way the bandage bled through, and she saw it before you had finished coming through the door.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Sit down." {n}The flat voice, the raised finger with its ring. There is no arguing with it. She kneels in front of you and undoes the bandage with quick, steady hands, far steadier than her voice.{/n}
"I said I heal some. You're some." {n}She lays both palms over the wound.{/n} "This will feel strange. Don't make a joke. If you make a joke I'll laugh and it'll go crooked."''',
      c("[Don't make a joke.]", "heal"),
      c('"Leave a scar."', "scar")),
    ch("scar", '"A scar?" {n}She looks up from the wound.{/n} "Well. A little one, then. It won\'t make you proof against the next blade. Hold still."',
      c("Continue", "heal", flags=(SCAR_KEPT,))),
    ch("heal", '{n}The pulling pain eases under her palms. When Chadali lifts them, the wound has closed. She lets out the breath she was holding.{/n} "There. Try moving. Slowly!"',
      c("Continue", "after")),
    ch("after", '"Warn me next time. I nearly dropped a tray." {n}Her hand rests beside the healed wound.{/n} "And if you\'re bleeding like this, go to the nearest healer. Even if it isn\'t me. I\'ll be cross about that later, when you\'re alive to hear it."',
      c('"First. Before the healers."', "close")),
    ch("close", '{n}She kisses the healed skin, then looks up and catches your eye. Her fingers tighten briefly on your knee before she gathers the bandage.{/n} "For luck. Now let me get rid of this dreadful thing."',
      c("[Let her fuss.]")),
], requires=(NIGHT,), forbids=(SCAR,))


# --- 8. Zero: the number beside her own name, and why she had an unlucky day. ----------------------------------

NUMBER = H + "a_lucky_number"
LUCK_GIVEN_BACK = H + "luck_given_back"
LUCK_KEPT_GIVING = H + "luck_kept_giving"

hour(NUMBER, "Zero", '"What are you writing?"', [
    ch("start", '"A list." {n}She turns the paper round. A column copied from earlier sessions: she remembers Eritrice choosing one, Cobblehoof twelve, Alichino six hundred and sixty-six, "which he chose himself, which is cheating". Your name, and beside it, underlined three times, a two.{/n}\n{n}At the very bottom, in the same round hand, is her own name. Beside it is a nought.{/n}',
      c('"Why is yours zero?"', "zero")),
    ch("zero", '"Because I sent it to you!" {n}She holds the list where you can see it, tapping the nought beside her name.{/n} "My share, not the Council\'s. You\'re going out against demons. I wanted you lucky." {n}She rubs her bare earlobe.{/n} "But I want my earring back, too. And I\'m sick of picking up broken trays. Don\'t look pleased about this."',
      c('"Stop. Take it back. All of it."', "back"),
      c('"Half. You keep half, or I\'ll find a way to send it back myself."', "half", flags=(LUCK_GIVEN_BACK,)),
      c("[Say nothing. Let her keep giving it.]", "keep", flags=(LUCK_KEPT_GIVING,))),
    ch("back", '"All of it? No!" {n}She plants her finger on the list.{/n} "I chose where it went. I\'ll keep half now. I want a decent morning, and you can manage with the other half. Don\'t argue."',
      c("[Don't argue.]", "half", flags=(LUCK_GIVEN_BACK,))),
    ch("half", '{n}She scratches out the nought and writes a firm one beside her name.{/n} "Half for me. There! I want my luck doing something about those trays." {n}She folds the list into her sleeve.{/n} "If you come back with both your ears, you can help me find what belongs in mine."',
      c("[Leave her with her one.]")),
    ch("keep", '{n}Chadali waits for an answer, then folds the list sharply.{/n} "Oh, you like this arrangement! Of course you do." {n}She kneels and peers beneath the Council table.{/n} "I\'ll keep sending it. I want you back from the front. But get down here and help me find my earring. I\'m not losing that as well."',
      c("[Go.]")),
], requires=(EARRING,), forbids=(NUMBER,))


# --- 9. The seat beside her (after the commit): a session, under the table. ----------------------------------------

SEAT = H + "the_seat_beside_her"

hour(SEAT, "The seat beside her", '"You saved me a seat."', [
    nar("open", '{n}The session is over. Chadali pushes an empty chair beside hers and puts a cookie on the seat. The war reports remain spread across the table.{/n}',
        c("Continue", "start")),
    ch("start", '"I\'ve saved you a seat. Move the cookie before you sit on it." {n}She holds out her hand beside the chair.{/n} "And this. If you\'re staying."',
      c('"What were you thinking of?"', "thinking"),
      c('"Should we be more careful?"', "careful")),
    ch("thinking", '"Your thumb." {n}She answers at once, then covers her mouth with her free hand.{/n} "I was going to say the Worldwound. But you\'re doing that with your thumb, and I\'m trying very hard to think about something else."',
      c("Continue", "close")),
    ch("careful", '"Careful?" {n}She squeezes your fingers.{/n} "The session\'s over. Let the others think what they like when they come back. I won\'t let go just because somebody wants this chair."',
      c("Continue", "close")),
    ch("close", '"Next session, come here." {n}She points at the chair beside hers.{/n} "If they argue, I\'ll argue back. You\'ll have to help with the Worldwound. I can\'t hold your hand and do everything."',
      c("[Take the cookie, and the seat.]")),
], requires=(COMMITTED,), forbids=(SEAT,))


# --- 10. Pretend we never met (Chapter 5): the Council's ending, foreseen. -------------------------------------------

NEVER_MET = H + "pretend_we_never_met"
REMEMBERED = H + "promised_to_remember"

hour(NEVER_MET, "Pretend we never met", '"You look worried."', [
    ch("start", '"I\'m not worried. I\'m thinking about the end." {n}She is sitting very still, looking at the long table and its seven chairs.{/n}\n"The Council\'s nearly done. One way or another. And when it\'s done, I know what they\'ll do. I\'ve seen councils end before." {n}Quietly.{/n} "They\'ll pretend it never happened. All of them. Alichino because it\'s convenient, and Cobblehoof because it\'s embarrassing, and Socothbenoth because he\'ll be busy, and Shyka because they\'ll find a better story."\n"I remember Eritrice keeping every scrap of minutes. I hope she keeps those too, whatever she says in public."',
      c('"And you?"', "you"),
      c('"I won\'t pretend."', "promise", flags=(REMEMBERED,))),
    ch("you", '"I\'ll deny it too, if anybody asks." {n}She rubs a crumb off the table.{/n} "But at home, on the anniversary, I want cookies and somebody who remembers why there are seven chairs. Will you come?"',
      c('"You won\'t be. I won\'t pretend."', "promise", flags=(REMEMBERED,)),
      c('"I can\'t promise what the war will leave of me."', "war")),
    ch("war", '"No. You can\'t promise that." {n}She offers her hand.{/n} "I\'ll keep the date anyway. If you come back, there\'ll be a chair. If you don\'t, I\'ll be cross with an empty one."',
      c("[Let her hold your hand.]")),
    ch("promise", '{n}She holds out her little finger. When you link it, she grips hard.{/n} "Then two of us remember. Privately. No speeches in the square. You come to my table and eat."',
      c("[Hold on.]")),
], requires=(STARTED, "council.cauldron_given"), forbids=(NEVER_MET,), chapters=(5,))


# --- Epilogue paragraphs on the committed page (chadali.trickster.epilogue.lucky_night). ------------------------------

EPILOGUE_PARAGRAPHS = [
    (BLESSED, "{n}Before every battle that remained, she took the Commander's hands for a moment and closed her eyes. The swords did not always miss. The Commander always walked out feeling that everyone in the room had been glad to see them.{/n}"),
    (REFUSED_BLESSING, "{n}She never blessed the Commander. She stood very near before every battle instead, and it leaked, as she had said it would.{/n}"),
    (EARRING_FOUND, "{n}She told the story of the lost earring to everyone, for years, and it always ended the same way: \"And then my lucky charm got down on the floor.\" She told it as if it were the best part of the war.{/n}"),
    (FIRST_SIGHT, "{n}She never stopped reminding the Council members who had laughed in the first session that she had been right. Eritrice minuted it every time, with the little squiggle.{/n}"),
    (PRISONER_FED, "{n}The cultist in the Drezen dungeon ate the cookie, the night before he was hanged. He never said a word about it. The white flower was found pressed in his prayer book, in the page about the Abyss.{/n}"),
    (LUCK_GIVEN_BACK, "{n}Her list of lucky numbers survived the Council. She kept the one beside her own name, and complained whenever a tray broke anyway. The Commander still heard about the lost earring.{/n}"),
    (LUCK_KEPT_GIVING, "{n}She kept sending her share of luck to the Commander. When she lost an earring or broke a tray, she came to their quarters and demanded help finding it or gathering the pieces. Her complaints often lasted longer than the search.{/n}"),
    (SOCOTH_REFUSED, "{n}Socothbenoth never asked her for a favour again. He sent flowers every year anyway, from somewhere warm, with a note that said only \"No hard feelings, darling.\" She put them in the bin, stem first, every year, and smiled.{/n}"),
    (SOCOTH_OBLIGED, "{n}Chadali kept her counteroffer to Socothbenoth: one morning's share only if he named the night and its purpose, and help for her worshippers in return. No agreement or delivery had followed. The Commander had no favour to collect.{/n}"),
    (REMEMBERED, "{n}When the Council's members publicly pretended they had never met, Chadali joined in. In private, she kept the date. Every year, on the anniversary of the first session, the Commander and Chadali ate cookies at a table with seven chairs, and remembered all of it, and made it sound much better than it was.{/n}"),
    (SCAR_KEPT, "{n}The Commander carried a thin pale scar for the rest of their life, curved at one end like the edge of a coin. She touched it for luck, every time, without asking.{/n}"),
]


def integrate(payload):
    """Give the committed page the small hours' consequences."""
    from story_format import p
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["chadali.trickster.epilogue.lucky_night"]["Nodes"][0]
    # Sol (PP6 audit): Socothbenoth's later favours only while he is still about; he vanishes in the Nocticula ending
    # (SocotGone, Epilogues/Cue_0570), and the absent variants say so.
    gone = ("socot.gone", "chadali.socoth_never_seen")
    page.setdefault("Paragraphs", []).extend(
        p(text, requires=(flag, "council.epilogue_ceased") if flag == REMEMBERED else (flag,),
          forbids=gone if flag in (SOCOTH_REFUSED, SOCOTH_OBLIGED) else ()) for flag, text in EPILOGUE_PARAGRAPHS)
    page["Paragraphs"].extend([
        p("{n}Socothbenoth never asked her for a favour again. Nobody saw him again at all. Chadali said she did not miss him, and baked his favourite anyway, once, and ate it herself.{/n}",
          requires=(SOCOTH_REFUSED,), any_groups=[list(gone)]),
        p("{n}Socothbenoth vanished without answering her counteroffer. Chadali threw out his flowers. Her worshippers had kept their morning luck; the Commander had no favour to collect.{/n}",
          requires=(SOCOTH_OBLIGED,), any_groups=[list(gone)]),
    ])


# Treatment provenance: keep the old healing destinations and branch on the actual scar request.
_scar = next(s for s in SCENES if s["Id"] == SCAR)
_hn = {nd["Id"]: nd for nd in _scar["Nodes"]}
_hn["scar"]["Choices"][0]["Next"] = "heal_scar"
_scar["Nodes"].extend([
    ch("heal_scar", '{n}A thin pale line remains, curving at one end like the edge of a coin. Chadali runs one finger beside it.{/n} "The little one you asked for. No more collecting them!"', c("Continue", "after_scar")),
    ch("after_scar", '{n}Her palm rests beside the new scar.{/n} "That mark is enough. Next time, the nearest healer. I want you alive when you come through this door."', c("Continue", "close_scar")),
    ch("close_scar", '{n}She kisses the scar, catches your eye and smiles before gathering the bloody bandage.{/n} "For luck."', c("[Let her fuss.]")),
])
_seat = next(s for s in SCENES if s["Id"] == H + "the_seat_beside_her")
_sn = {nd["Id"]: nd for nd in _seat["Nodes"]}
for _choice in _sn["start"]["Choices"]:
    _choice["Text"] = '[Take the seat and her hand.] ' + _choice["Text"]
_sn["start"]["Choices"].append(c('"Another time. The reports need me."', abort=True))
_hn["after"]["Choices"][0]["Text"] = '"The nearest healer. I promise."'

# Append new paragraphs after all old route paragraphs; existing consumer
# inventories keep their positions. No historical guess summons its speaker.
_integrate_hours = integrate
def integrate(payload):
    _integrate_hours(payload)
    from story_format import p
    from storylines import chadali_trickster as spine, chadali_sessions as sessions
    page = next(sc for sc in payload["Scenes"] if sc["Id"] == "chadali.trickster.epilogue.lucky_night")["Nodes"][0]
    page["Paragraphs"].extend(spine.ROUND2_PARAGRAPHS)
    page["Paragraphs"].extend(p(text, requires=(flag,)) for flag,text in sessions.ROUND2_PARAGRAPHS)
    for para in page["Paragraphs"]:
        if "chadali.wagers.hoped_aloud" in para["Requires"]:
            para["Requires"] = ["chadali.wagers.commander_hoped_aloud", "ending.wound_closed"]
    page["Paragraphs"].extend([
        p('{n}After the fighting at Threshold ended, Chadali repeated the hopeful words the Commander had spoken in the dark hall. "You said it before you knew how. I kept it."{/n}', requires=("chadali.wagers.commander_hoped_aloud",), forbids=("ending.wound_closed",)),
        p('{n}The night the Wound closed, Chadali repeated the hope she had spoken when the Commander could not: they would win, though she did not yet know how. "That one was mine," she said. "You stayed to hear it."{/n}', requires=("chadali.wagers.chadali_hoped_aloud", "ending.wound_closed")),
        p('{n}After the fighting at Threshold ended, Chadali repeated her own words from the dark hall. The Commander had stayed when she said them. She remembered that too.{/n}', requires=("chadali.wagers.chadali_hoped_aloud",), forbids=("ending.wound_closed",)),
    ])

    # Append after the existing paragraph inventory to preserve saved positions.
    from storylines.chadali_fortunes import SAW_THE_FAIR
    page["Paragraphs"].append(p(
        "{n}Her fair was never built on ground the Wound had let go, because the Wound did not let go, and the Council sat on arguing over it. She built it anyway, small and loud, in the lee of the walls where the ground was held and the lamps could be seen from the front: acrobats on spliced rope, lollipops, and a three-headed puppy that ate nobody. Soldiers on leave came with their helmets under their arms and went back to the line with sticky fingers. There was a devil's stall. It sold lollipops. Chadali watched it herself, every day, with a very big one, and the Commander never once saw her look at the glow on the horizon.{/n}",
        requires=(SAW_THE_FAIR, "council.epilogue_convened"),
        forbids=("ending.wound_closed",),
    ))


# fix14-a: the earlier earring scene always completes its recovery.
_number = next(s for s in SCENES if s['Id'] == NUMBER)
_NUMBER_TEXT = {
    'zero': '"Because I sent it to you!" {n}She holds the list where you can see it, tapping the nought beside her name. The white-gold earring clinks against her jaw.{/n} "My share, not the Council\'s. You\'re going out against demons. I wanted you lucky. Nobody asked me to, and nobody gets to tell me to stop."\n{n}She touches the earring, and her mouth goes sour.{/n} "And yes, before you say it, that\'s why the tray went over, and the cup, and why I was under that table in the first place. You got down on the floor and found it. It was very sweet. I\'m still cross, and I\'m still not taking it back. Don\'t look pleased about this."',
    'half': '{n}She scratches out the nought and writes a firm one beside her name, pressing so hard the quill spits.{/n} "Half for me. There! Half is a decent morning and a tray that stays on its feet, and the other half is yours whether you like it or not." {n}She folds the list into her sleeve, and the earring clinks as she shakes her head.{/n} "I\'m not doing it for gratitude. I\'m doing it because the alternative is you dead, and then I\'d have to bake for the funeral."',
    'keep': '{n}Chadali waits for an answer, then folds the list sharply.{/n} "Oh, you like this arrangement! Of course you do." {n}She flicks the earring as though it had insulted her.{/n} "Fine. The nought stays. Every morning, all of it, to you. You\'ll have a charmed life and I\'ll have a clumsy one, and when I drop the next tray you can pick up the pieces." {n}Her voice drops.{/n} "Come back from the front. That is the whole of the bet."',
}
for _node in _number['Nodes']:
    if _node['Id'] in _NUMBER_TEXT:
        _node['Text'] = _NUMBER_TEXT[_node['Id']]
