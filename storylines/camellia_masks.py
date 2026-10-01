"""Camellia: the masks. The arc around the Trickster device (camellia_trickster).

Before the kill, a liar courts a liar on her own companion hub. Nothing here states her murders as fact: she never
confesses in these scenes, and the Commander never accuses. It is the Trickster's ear for a lie, set against hers, and the
double meanings are hers to enjoy. Each scene engages a canon anchor:
- her Varisian teacher, the barred windows and the puppy (Camelia/Cue_0089, Cue_0090, Cue_0094, Cue_0096);
- Mireya, the spirit she names because she "doesn't know her name" (Cue_0107 1b515274, Cue_0108, Cue_0112);
- the spirits of Sarkoris that "endlessly thirst" (Cue_0077 3c75f9fe) and her "unexpected and overwhelming" moods (FinalTruth
  Cue_0054 4f1a912b; Cue_0080);
- her taste for anticipation (Cue_0064), the fencing masters of her girlhood (Cue_0090), "kindred souls are those with which
  we choose to entwine ourselves" (Cue_0170);
- what she watches for in a friend's eyes (FinalTruth Cue_0042 f53d2eeb), and what she does with a heart (Cue_0079).
After the return: her grave, her lesson, her price (camellia_trickster), her test, and the life after her answer. She stays
what she is. The romance does not cure her; it gives her a reason to wait.
"""
from story_format import c, scene
from storylines.camellia_trickster import (BY_ORDER, CLOSED, COMMITTED, DANCED, DREZEN, DUE, FED, FLINCHED, FUNERAL, GAME, GONE,
                                           GRAVE, HUB_LIST, INVENTED, KILLED, KNIFE_NOTICED, LATE, LESSON, LIST_BURNED,
                                           LIST_KEPT, NAME_LEFT, NAMED, NOT_TODAY, OUT_LIED, OUTLIVE, OWED, P, PRESENCE, QUIET,
                                           REL, RET, ROMANCE, SCENES, SHE_WON, SHELF, STARTED, STEADY, UNIT, WITNESS_HERS,
                                           WITNESS_LIED, cam, lead, met, nar)

M = P + "masks."
# PP2 early beats (camellia_early: path-neutral, set in the Prologue and Chapter 2), read here only.
EARLY_ASKED = "camellia.early.blood.asked"
EARLY_KEPT = "camellia.early.blood.kept"
EARLY_SHIELD = "camellia.early.cart.shield"
EARLY_WATCH = "camellia.early.cart.watch"

TWO_LIES = M + "two_lies"
MIREYA = M + "mireya"
FLIES = M + "flies_at_a_window"
FUNERAL_SCENE = M + "the_funeral_i_would_like"
DANCE = M + "a_dance_with_a_knife_in_it"


def living(id, title, entry, nodes, requires=(), forbids=(), delay=48, chapter=3, last=5, chapters=None):
    """A scene with the living Camellia, on her own companion hub, while the Trickster's ear is live."""
    extra = dict(Chapters=list(chapters)) if chapters else {}
    SCENES.append(scene(id, title, "Camellia", chapter, entry, nodes, requires=("trickster", *requires),
                        forbids=(*GONE, CLOSED, *forbids), delay=delay, last=last, optional=True, Relationship=REL,
                        AnswerLists=[HUB_LIST], ContactUnit=UNIT, **extra))


# === Before the kill: a liar's courtship ===================================================================================

# --- 1. Two lies and a truth (Chapter 3 onward). ---------------------------------------------------------------------

living(TWO_LIES, "Two lies and a truth", '"You look bored, Camellia. That seems dangerous."', [
    nar("open", '''{n}Camellia is sitting on her bedroll with a lap full of dried flowers, sorting them by some system known only to her: stems to the left, heads to the right, the ones with insects in them into a small silk bag that she ties very tightly.{/n}''',
        c("Continue", "bored", forbids=(EARLY_ASKED, EARLY_KEPT, EARLY_SHIELD, EARLY_WATCH)),
        # PP2 (13 section 2b): what she kept of the Prologue caves and the Chapter 2 cart, before she picks her game.
        c("Continue", "early_asked", requires=(EARLY_ASKED,)),
        c("Continue", "early_kept", requires=(EARLY_KEPT,), forbids=(EARLY_ASKED,)),
        c("Continue", "early_shield", requires=(EARLY_SHIELD,), forbids=(EARLY_ASKED, EARLY_KEPT)),
        c("Continue", "early_watch", requires=(EARLY_WATCH,), forbids=(EARLY_ASKED, EARLY_KEPT, EARLY_SHIELD))),
    cam("early_asked", '''"You asked me about my skirts, once." {n}She does not look up from the flowers.{/n} "In the caves under Kenabres, with a dead man at my feet and you and your companions deciding whether I was worth the trouble of rescuing. You were the one who asked. I have been meaning to repay the attention."''',
        c("Continue", "early_shield", requires=(EARLY_SHIELD,)),
        c("Continue", "early_watch", requires=(EARLY_WATCH,), forbids=(EARLY_SHIELD,)),
        c("Continue", "bored", forbids=(EARLY_SHIELD, EARLY_WATCH))),
    cam("early_kept", '''"In the caves under Kenabres you looked at my skirts, and then at my face, and said nothing at all." {n}She drops a stem to the left.{/n} "I decided you had missed it. I have since revised my opinion of you, my friend. Upwards. I so rarely have to."''',
        c("Continue", "early_shield", requires=(EARLY_SHIELD,)),
        c("Continue", "early_watch", requires=(EARLY_WATCH,), forbids=(EARLY_SHIELD,)),
        c("Continue", "bored", forbids=(EARLY_SHIELD, EARLY_WATCH))),
    cam("early_shield", '''"At the camp, when the gargoyles came, you stood in front of me as though I were something that might break." {n}A dried poppy turns between her fingers.{/n} "People usually stand in front of me to get a better view of what is coming. You put your back to me. I have not decided yet whether that was brave or merely careless."''',
        c("Continue", "bored")),
    cam("early_watch", '''"At the camp, when the gargoyles came, you stood by the cart and watched me be frightened, to see what I would do instead." {n}A dried poppy turns between her fingers.{/n} "You saw what I did instead. You haven't asked me about it since. I find that I mind."''',
        c("Continue", "bored")),
    cam("bored", '''"Dangerous? Ha ha! You flatter me." {n}She does not look up.{/n} "I am never bored, my friend. I am waiting. Bored women yawn. I am deciding which of you to watch."
{n}She holds a dried poppy up to the lamp, turns it, and drops it into the silk bag.{/n} "But since you are here, and since you are looking at me in that clever way, would you like to play a game? My teacher taught it to me when I was small. The old Varisian woman my father paid to live with us. She said it was how she learned when the spirits were lying."''',
        c('"What game?"', "rules"),
        c('"Do spirits lie?"', "spirits")),
    cam("spirits", '''"Constantly." {n}She says it with deep affection.{/n} "They are like children, or courtiers. They tell you what they think will please you, and what they want, and very occasionally what is true, all in the same breath. One learns to listen for the seam." {n}She runs a manicured nail along the edge of a pressed leaf, very slowly.{/n} "Everyone has a seam."''',
        c('"And the game?"', "rules")),
    cam("rules", '''"Two lies and a truth. I tell you three things. You tell me which one is true. Then you do the same to me, and we see who is better at it." {n}At last she looks up. Her eyes are very bright.{/n} "I warn you, I was a lonely child, and I practised a great deal. I had very little else to do behind those windows."''',
        c('"Go on, then."', "hers")),
    cam("hers", '''{n}She folds her hands in her lap, over the flowers, like a girl at a recital.{/n}
"One. When I was small I had a puppy, a little barking ball of happiness, and I loved him very much.
Two. My father put bars on the windows of our house to keep the world out.
Three." {n}She smiles.{/n} "I have never told you a single lie."''',
        c('"The puppy. Nobody makes up a puppy."', "puppy"),
        c('"The bars. That one\'s true."', "bars"),
        c('[Trickster] "Three is a lie. It\'s the only one you\'d bother to tell."', "three")),
    cam("puppy", '''"Oh, the puppy was true." {n}Her smile softens into something almost wistful, and then it is gone.{/n} "So was the next one, very nearly. The bars were real. But they were not to keep the world out, my friend. Father was a practical man. They were there to keep me in."
{n}She lets that sit a moment, then brightens.{/n} "So you see, I only told you one lie. And you let it walk straight past you."''',
        c("Continue", "yours")),
    cam("bars", '''"The bars were real." {n}She nods, pleased, as at a promising pupil.{/n} "But you missed the twist. They were not to keep the world out. They were to keep me in. Father was always so protective." {n}A pause, delicate as a dropped glove.{/n} "Of the world."
"So that one was a lie with a true thing inside it. Those are my favourites. They are the only kind anyone ever believes."''',
        c("Continue", "yours")),
    cam("three", '''{n}For a heartbeat something in her face goes perfectly still, the way a cat goes still at the sound of a mouse behind the wainscot. Then she laughs, delighted, and claps her hands once.{/n}
"Ha ha! How rude. And how correct." {n}She leans forward.{/n} "The puppy was real, the bars were real, and of course I have lied to you. I lie to everyone. It would be terribly unfriendly to make an exception." {n}She tilts her head.{/n} "But you didn't guess. You knew. How?"''',
        c('"You said it last. People save the lie for last."', "yours"),
        c('[Trickster] "It\'s the only one you smiled at."', "yours")),
    cam("yours", '''"Now you. Three things. And do make them good. I shall be very insulted if you insult me with easy ones."''',
        c('[Tell three truths that sound like lies] "I don\'t sleep well. I cheat at cards. I like you."', "out_lied"),
        c('[Play fairly] "I was born in a barn. I once outran a horse. I\'ve never been to Absalom."', "fair"),
        c('[Tell her three lies] "I\'m afraid of you. I\'m tired of this crusade. I\'m not enjoying myself."', "three_lies")),
    cam("out_lied", '''{n}She studies you for a long time, head on one side, one finger tapping her chin.{/n}
"The cards are a lie. You do not need to cheat; you simply make the other person think you have. The sleep is true, I have heard you walk at night. And the last one..." {n}She stops. Her finger stops.{/n}
"You're waiting for me to say the last one is a lie." {n}Her voice has dropped.{/n} "You said them all in exactly the same voice. All three. I cannot find the seam."''',
        c('"They\'re all true."', "confess"),
        c('[Say nothing, and smile]', "confess_silent")),
    cam("confess", '''"All true." {n}She repeats it, and a faint colour comes up in her cheeks, which she does nothing to hide, and which you suspect she could hide perfectly well if she wanted to.{/n} "That is cheating, you know. Telling the truth in a game about lies. It is the most underhanded thing anyone has ever done to me, and I have met my father."''',
        c("Continue", "close_won", flags=(GAME, OUT_LIED, STARTED))),
    cam("confess_silent", '''{n}She waits. You wait. The lamp gutters. At last she laughs, softly, and looks down at the flowers in her lap as if they had said something indiscreet.{/n}
"You are not going to tell me. Of course you're not. You are going to leave me wondering which part of you likes me." {n}She plucks a dried rose and hands it to you, stem first.{/n} "I shall wonder very thoroughly."''',
        c("Continue", "close_won", flags=(GAME, OUT_LIED, STARTED))),
    cam("fair", '''"Absalom." {n}No hesitation at all.{/n} "You've been to Absalom. Everyone who has been to Absalom says 'Absalom' as if it owed them money." {n}She beams.{/n} "One point to me. Don't sulk. I did warn you. I have been listening for seams since I was six years old."''',
        c("Continue", "close_lost", flags=(GAME, SHE_WON, STARTED))),
    cam("three_lies", '''"Oh, all three are lies. You aren't afraid of me, which is very foolish of you. You aren't tired of the crusade, you're far too entertained by it. And you are enjoying yourself enormously." {n}She tips her head back and laughs.{/n} "You broke the rules, my friend. There was supposed to be one true thing. I shall have to assume it's hiding somewhere else."''',
        c("Continue", "close_lost", flags=(GAME, SHE_WON, STARTED))),
    cam("close_won", '''"We shall play again. You owe me a chance to win." {n}She goes back to her flowers. Stems to the left. Heads to the right. The silk bag, very tightly tied.{/n} "I always win eventually. I am patient in a way that frightens people, when they notice it."''',
        c("[Leave her to her flowers]")),
    cam("close_lost", '''"We shall play again, when you are better at it." {n}She goes back to her flowers.{/n} "Don't worry. I shall teach you. I always teach the people I like the things I know. It's only fair that someone should understand me."''',
        c("[Leave her to her flowers]")),
], delay=0)


# --- 2. Mireya's name. -------------------------------------------------------------------------------------------------

living(MIREYA, "A name for a spirit", '"Who are you talking to?"', [
    nar("open", '''{n}Camellia sits apart from the fire with the bone snake of her amulet cupped in both hands, very close to her mouth, murmuring. When she hears you she does not startle. She finishes her sentence, whatever it was, and only then looks up.{/n}''',
        c("Continue", "who")),
    cam("who", '''"Mireya." {n}She holds up the amulet so that the firelight catches the little snake's eyes.{/n} "The spirit in here. I found her when she was hardly anything, a shred of rage and madness blowing about the ruins like a scrap of paper. I locked her in, and I've taken care of her ever since."
"I talk to her in the evenings. She doesn't answer yet. She needs a great deal more before she can." {n}She licks her lips, a small, absent movement.{/n} "But she listens. I am sure she listens."''',
        c('"Mireya. Is that her name?"', "name"),
        c('"What does she need?"', "needs")),
    cam("needs", '''"Blood, mostly." {n}She says it as another woman might say "rest, mostly", with a small apologetic shrug.{/n} "Every time I give her some, the shroud over her lifts a little. Soon I will be able to ask her what happened to this land, and how to heal it. Isn't that a lovely thing to want?"
{n}She strokes the snake's head with one fingertip.{/n} "You needn't look at me like that. Demon blood, mostly. The Worldwound is generous."''',
        c('"Mostly."', "mostly"),
        c('"And her name?"', "name")),
    cam("mostly", '''"Mostly." {n}She agrees, pleasantly, and says nothing else at all, and the silence goes on just long enough to be a reply of its own.{/n}''',
        c('"And her name?"', "name")),
    cam("name", '''"I don't know her real name. She was too broken to tell me. So I call her Mireya. It was the name of a girl in a book I liked, when I was small. She was very beautiful and very sad and she drowned herself in the third chapter, and I read that chapter every night for a year." {n}Camellia smiles fondly.{/n}
"Do you think she minds? Being named by a stranger? I've always wondered. Names are such intimate things to give. Like a collar."''',
        c('[Offer a name] "Call her Toilday. Nobody\'s afraid of a Toilday."', "tuesday"),
        c('[Trickster] "I had a friend like that once. Sergeant Barnaby Quill. He never answered me either."', "barnaby"),
        c('"Keep the one you gave her. It\'s yours."', "keep")),
    cam("tuesday", '''"Toilday!" {n}She laughs so suddenly that the amulet swings on its cord.{/n} "Oh, that's dreadful. Toilday. She would never forgive me."
{n}She holds the snake up to her ear, as if listening, and her face goes grave.{/n} "No. She says she is Mireya, and she would like you to know that she is taking it very personally." {n}Her eyes glitter.{/n} "Now you've done it. Now she knows your voice."''',
        c("Continue", "after", flags=(NAMED,))),
    cam("barnaby", '''"Sergeant Barnaby Quill," {n}she repeats, slowly, testing the weight of it.{/n} "Tell me about him."
{n}So you do. He was from Mendev. He had a limp from a vrock, a wife in Nerosyan he wrote to every week, and a laugh like a mule falling downstairs. You make up the mule on the spot. You make up the wife's name too. Camellia listens with her chin on her hands and her eyes never leaving your mouth.{/n}''',
        c("Continue", "made_up")),
    cam("made_up", '''"You made him up." {n}Very softly. Not a question.{/n} "Just now. All of him. The limp and the wife and the mule. You made him up and put him in my head, and now he's in there, and I shall never get him out."
{n}She is quiet for a moment, turning the amulet in her fingers.{/n} "How did it feel? To make a person up, and have someone believe in them?"''',
        c('"Lonely."', "lonely"),
        c('"Wonderful."', "wonderful")),
    cam("lonely", '''"Yes." {n}She says it at once, and then looks as though she wishes she hadn't.{/n} "Yes, that's exactly it. You make them up so that you have someone to talk to, and then you have to keep them alive all by yourself, and nobody else can ever really see them." {n}She laughs, lightly, and it doesn't quite work.{/n} "How silly. We are being very silly tonight."''',
        c("Continue", "after", flags=(INVENTED,))),
    cam("wonderful", '''"Wonderful," {n}she agrees, and her smile is the widest you have seen it.{/n} "It is, isn't it? Like having a secret door in a house nobody knows you live in." {n}She presses the amulet to her lips.{/n} "I think we could be very good friends, you and I. Better than anyone I've ever had. I have had a great many friends."''',
        c("Continue", "after", flags=(INVENTED,))),
    cam("keep", '''"Mine." {n}She considers the word, and you can see her decide she likes it.{/n} "Yes. She is mine, isn't she. I made her what she is." {n}She tucks the snake back into the lace at her throat, carefully.{/n} "You're very generous, my friend. Most people want to take things away from me. You keep telling me to keep them."''',
        c("Continue", "after", flags=(NAME_LEFT,))),
    cam("after", '''"Go to bed. You look like something the spirits would enjoy." {n}She turns back to the fire and lifts the amulet to her mouth again.{/n} "Mireya and I have a great deal to discuss. Most of it is about you."''',
        c("[Leave her to her conversation]")),
], requires=(GAME,), delay=48)


# --- 3. Flies at a window (Chapter 4, the Abyss). ----------------------------------------------------------------------

living(FLIES, "Flies at a window", '"You\'ve gone pale. Is it the spirits?"', [
    nar("open", '''{n}In the Abyss Camellia sleeps badly, when she sleeps at all. Tonight she sits with her back against a rock that is faintly warm, like a sleeping animal, and presses the heels of her hands against her ears. Her lips are moving. When you come closer you hear that she is counting.{/n}''',
        c("Continue", "none")),
    cam("none", '''"There are no spirits here." {n}Her voice is thin and very polite, the voice of a hostess apologising for a draught.{/n} "That's the trouble. At home, in the Wound, the spirits are mad, but they are spirits. They have a land, they have a grief. They want something I can give them."
"Here there is no land. There's only appetite. Nothing that ever lived here wants anything but more." {n}She lowers her hands and smiles, horribly, beautifully.{/n} "It sounds like flies at a window, my friend. Thousands of them. Beating and beating at the glass, and I am the glass."''',
        c('"What can I do?"', "do"),
        c('"How long have you heard them?"', "long")),
    cam("long", '''"Since I was a little girl. My father brought doctors, and priests, and exorcists, and they all said something was wrong with me, and they all went away." {n}She shrugs.{/n} "Then my teacher came and said nothing was wrong with me at all. I was simply listening to something no one else could hear. She was very useful, for a while. Then she became tiresome."
{n}She looks at her hands.{/n} "It is quieter, usually. There are ways to make it quieter."''',
        c('"What can I do?"', "do")),
    cam("do", '''"Entertain me, my friend." {n}She says it the way she would order a footman to fetch a shawl.{/n} "Anything. Everything. Make it loud and long and stupid. I would rather be entertained while I wait than listen to them."''',
        c('[Trickster] Tell her the longest, most outrageous lie you know, and don\'t stop until she laughs.', "story"),
        c("[Sit beside her and take her hands off her ears]", "hands"),
        c('"There\'s a demon camp an hour east. Go and bleed some of them. Quiet it the usual way."', "fed")),
    cam("story", '''{n}So you tell her how you once sold a vrock its own left wing and charged it rent on the right. You tell her about the court of the Tyrant of Toildays, and the war of the three spoons. It gets worse. It gets much worse. Somewhere around the ambassador made entirely of cheese she snorts, very unbecomingly, and puts a hand over her mouth.{/n}
"Stop. Stop, that's not fair, I was trying to be tragic." {n}She is shaking with laughter now, and when it passes, her shoulders have come down.{/n} "That was dreadful. Do tell me another."''',
        c("Continue", "quiet", flags=(QUIET,))),
    cam("hands", '''{n}Her hands are cold and damp and very strong. She lets you take them. She lets you hold them in her lap. For a long time neither of you says anything, and the warm rock breathes against your backs.{/n}
"You're lying to me with your hands," {n}she says at last.{/n} "You are telling me everything will be well. A comforting lie. You should offer your services to the chaplains." {n}She does not take her hands back.{/n}''',
        c("Continue", "quiet", flags=(QUIET,))),
    cam("fed", '''{n}She is on her feet before you have finished the sentence, and already smoothing her hair.{/n}
"You are the best of friends. The very best." {n}She kisses your cheek, quickly, like a girl leaving for a ball.{/n} "Don't wait up. And don't look for me, please. I am never at my prettiest afterwards."
{n}She is back before dawn, washed, and not humming. Her sleeves are wet to the elbow. She lies down with her back to the camp and her hands pressed flat over her ears, and does not sleep. In the morning she tells everyone it was a lovely walk, and is short with the cook, and will not look at you until noon.{/n}''',
        c("[Let her sleep]", flags=(FED,))),
    cam("quiet", '''"You know what you are?" {n}She rests her head against your shoulder, as if she had always done it.{/n} "Your conversation is preferable to theirs. At present. Do not let it go to your head."
{n}She does not sleep. She sits with her head on your shoulder and her fingers closed round your sleeve, counting under her breath, and she does not let go until morning.{/n}''',
        c("[Stay until morning]")),
], requires=(GAME,), delay=48, chapter=4, last=4, chapters=(4,))


# --- 4. The funeral I would like (Chapter 5, Drezen). ------------------------------------------------------------------

living(FUNERAL_SCENE, "The funeral I would like", '"You\'re watching the procession."', [
    nar("open", '''{n}A crusader's funeral goes down the street below the citadel wall: four bearers, a chaplain with a book, a widow walking behind with her hand on the coffin, and a cart of white lilies that someone has tied up with a blue ribbon. Camellia watches it from the parapet with the absorbed attention of a woman at a play.{/n}''',
        c("Continue", "critic")),
    cam("critic", '''"The lilies are wrong." {n}She says it the way a dressmaker says "the hem is wrong".{/n} "White lilies are for weddings. No one has told them. And the blue ribbon, with that widow's coat? Dreadful."
"And look at her. She keeps touching the coffin. As if he might knock." {n}She tilts her head.{/n} "Everyone at a funeral is waiting for the same thing, you know. They are waiting for the dead to prove them wrong. They never do. It's the one performance nobody can stop giving."''',
        c('"What would you want at yours?"', "hers"),
        c('"You enjoy funerals."', "enjoy")),
    cam("enjoy", '''"I enjoy honesty." {n}She smiles down at the widow.{/n} "A funeral is the only place where people stop pretending that the person they're looking at is going to be there tomorrow. Everywhere else, everyone lies about that all day long. You. Me. That chaplain." {n}A pause.{/n} "Him especially."''',
        c('"What would you want at yours?"', "hers")),
    cam("hers", '''"Mine?" {n}She lights up like a child asked about her birthday.{/n} "Oh, I've planned it for years. A small chapel. Rain, if it can be arranged. Very good music. And the wrong flowers, on purpose. White lilies, the wedding kind, heaps of them, so that no one knows whether they ought to weep or congratulate me."
{n}She leans her elbows on the parapet.{/n} "And at the very back, one person who doesn't believe a word of it. Who stands there with their arms folded and waits for me to sit up. I have always wanted someone like that."''',
        c('[Promise the wrong flowers] "White lilies. The wedding kind. I\'ll order them myself."', "promise"),
        c('"I\'d rather you didn\'t need one."', "outlive"),
        c('"You\'re being morbid."', "morbid")),
    cam("promise", '''"You would, wouldn't you." {n}She turns to look at you properly, and for a moment she is not smiling at all.{/n} "You'd stand at the back with your arms folded. You'd be the one who didn't believe it."
{n}Then the smile comes back, brighter than before.{/n} "Then that's settled. You'll bring the lilies, and I shall do the rest. I've always been very good at lying still."''',
        c("Continue", "close", flags=(FUNERAL,))),
    cam("outlive", '''"Rather I didn't need one?" {n}She laughs, but it's a small laugh.{/n} "My friend, everybody needs one eventually. Even you. Even me. The only question is whether anyone interesting comes." {n}She hesitates.{/n} "Would you? Come, I mean. At the back. Arms folded."''',
        c('"Always."', "close", flags=(OUTLIVE,)),
        c('[Trickster] "I\'ll come. I won\'t believe a word of it."', "promise")),
    cam("morbid", '''"I'm being practical." {n}She sniffs, and turns back to the procession.{/n} "We're at war with the Abyss, my friend. Half the people in this city will be lying in a box by midwinter. The least one can do is choose one's flowers." {n}The cart turns the corner. The lilies nod in the wind.{/n} "Somebody always gets them wrong."''',
        c("Continue", "close")),
    cam("close", '''{n}Below, the widow stops at the gate, takes one lily from the cart, and puts it in her coat. Camellia watches her do it with great interest.{/n}
"There," {n}she murmurs.{/n} "Now she's begun to believe it."''',
        c("[Watch the procession go]")),
], requires=(GAME,), delay=48, chapter=5, last=5, chapters=(5,))


# --- 5. A dance with a knife in it (Chapter 4 onward). -----------------------------------------------------------------

DANCE_ROMANCE = '''"You needn't look so hopeful, darling. This is a lesson, not an assignation. Assignations don't require one to count."'''
living(DANCE, "A dance with a knife in it", '"Camellia? You wanted to see me?"', [
    nar("open", '''{n}Camellia has cleared her tent, or her room, or whatever corner of the world the crusade has lent her this week, down to the boards, and pushed everything against the walls. She is barefoot, with her skirts pinned up to the ankle and a candle in each corner of the floor.{/n}''',
        c("Continue", "teach")),
    cam("teach", '''"I want to teach you to dance." {n}She sounds entirely serious.{/n} "A proper Taldan court dance. My father had the finest masters in Kenabres come to the house, a fencing master in the mornings and a dancing master in the afternoons. I could never tell the difference. Both of them were always telling me where to put my feet so that I could reach someone's heart."''',
        c("Continue", "romance", requires=(ROMANCE,)),
        c("Continue", "start", forbids=(ROMANCE,))),
    cam("romance", DANCE_ROMANCE, c("Continue", "start")),
    cam("start", '''"Give me your hand. No, the left. Your right goes here." {n}She places it at her waist with a small, precise tug, as if hanging a picture.{/n} "Now we walk. Three steps and a turn. Three and a turn. Don't look at your feet. If you look at your feet, you have already lost."''',
        c("Continue", "dancing")),
    nar("dancing", '''{n}Three steps and a turn. She is light and very quick, and she counts under her breath, one-two-three, one-two-three, and she smells of dried roses and something metallic underneath. On the fourth turn, your hand at her waist slides lower, and under the pinned-up skirt, strapped high on her thigh, you feel the hard shape of a knife.{/n}''',
        c("[Say nothing, and keep dancing]", "silent"),
        c('"You\'re armed."', "armed"),
        c('[Trickster] Keep dancing, and on the next turn, lift it neatly from the strap.', "lifted")),
    cam("silent", '''{n}She notices that you noticed. You can tell because she stops counting aloud, and because her eyes, which have been on your collar all this time as a good pupil's should, lift to yours and stay there.{/n}
"You didn't look down," {n}she says, very softly, not missing a step.{/n} "Everybody looks down."''',
        c("Continue", "anticipation", flags=(DANCED,))),
    cam("armed", '''"Of course I'm armed." {n}She laughs, delighted, and turns under your arm.{/n} "A lady should always be armed at a dance. You never know who will ask you." {n}She comes back into your hands.{/n} "My dancing master said the only difference between a waltz and a duel is who knows it's happening. I have always thought he was being modest."''',
        c("Continue", "anticipation", flags=(KNIFE_NOTICED,))),
    cam("lifted", '''{n}On the next turn the knife is in your hand and her strap is empty, and she does not notice for a full three steps. Then she does. She stops dead.{/n}
"Give that back," {n}she says, in a completely different voice.{/n}
{n}You hold it out, hilt first. She looks at it, and then at you, and then she takes it and slides it home without looking down, and the other voice is gone as though it had never been.{/n} "Well. Now I know where your hands go when I'm not watching. How very instructive."''',
        c("Continue", "anticipation", flags=(KNIFE_NOTICED,))),
    cam("anticipation", '''{n}The candles have burned down by a finger's width. She is close enough that her breath stirs your collar, and her hand is flat on your chest, over the place a fencing master would call the heart.{/n}
"That's enough for tonight." {n}She does not move away.{/n} "Have patience. Imagine the rest. Anticipation quickens the imagination, my friend. I know this from experience." {n}She steps back and blows out the nearest candle.{/n} "Three steps and a turn. Practise."''',
        c("[Go]")),
], requires=(GAME, MIREYA), delay=72, chapter=4, last=5)


# === After the return: the days before her price ============================================================================

# --- The grave (killed): she takes the Commander to her own grave. --------------------------------------------------

GRAVE_LEADS = [
    ("late", nar, '''{n}The sexton is there, by the gate, with his lantern. He sees the Commander, and then he sees the veiled woman on the Commander's arm, and he sets the lantern down very carefully on the path and walks away into the dark without once looking back.{/n}''', LATE),
    ("order", cam, '''"Your Mendevian sergeant came here, you know. The morning after. She stood exactly where you are standing and said, to the stone, 'Nothing personal.' I thought that was very sweet of her. I am going to remember it for a long time."''', BY_ORDER),
]
SCENES.append(scene(P + "beat.her_own_grave", "Her own grave", "Camellia", 3,
    '"You look like a woman with somewhere to be."', [
    cam("open", '''"I have. We have. Come with me, my friend. I want to show you where I live now." {n}She lowers her veil and takes your arm, lightly, like a lady on a promenade.{/n}''',
        c("Continue", "walk")),
    *lead([("walk", nar, '''{n}She takes you to the cemetery at dusk, by the long way, past the chapel and the stonemason's yard. Her grave is at the edge, under a hawthorn: a plain stone, already weathering, and a jar of lilies, the white wedding kind, gone brown at the edges. She stoops and straightens them.{/n}''', None),
           *GRAVE_LEADS], "stone"),
    cam("stone", '''"'Camellia Gwerm. A daughter of Kenabres. She gave her life in the service of the crusade.'" {n}She reads it aloud in a clear, carrying voice, like a governess.{/n} "Two errors in eleven words. I did not give it, it was taken, and I did not give it in anyone's service. And no one has ever called me a daughter of Kenabres who wasn't hoping to be paid."
{n}She crouches, and brushes a snail from the stone with one gloved finger.{/n} "Still. It's a nice stone. My father never bought me anything so honest."''',
        c('"Why bring me here?"', "why"),
        c('[Trickster] Read the eulogy you would have given.', "eulogy"),
        c("[Lie down in the grass on her grave]", "lie_down")),
    cam("why", '''"Because nobody else can come with me." {n}She says it quite simply.{/n} "It's a very lonely thing, to have a grave. One stands in front of it and there is no one to say, 'Do you remember when she did such and such?' Only strangers who didn't know me, and friends who did, and I am rather short of friends who did, as you know."''',
        c("Continue", "last")),
    cam("eulogy", '''{n}You clear your throat. You tell the stone that Camellia Gwerm was a liar of the first water, a spirit talker of great appetite and poor table manners, that she was cruel to waiters and kind to insects in the most suspicious way, and that anyone who believed she was dead deserved what was coming to them.{/n}
{n}She listens with her hands clasped under her chin. When you have finished she is crying, very prettily, without a sound, and you cannot for your life tell if it is real.{/n} "That," {n}she says,{/n} "I'm going to have carved on the back. Nobody will ever believe it's about me."''',
        c("Continue", "last")),
    cam("lie_down", '''{n}She looks at you as if you had suggested something shocking at a dinner party. Then she laughs, gathers up her skirts, and lies down beside you in the long grass, on top of herself, with her hands folded on her breast.{/n}
"So this is what it looked like," {n}she says to the hawthorn.{/n} "From the outside. I always wondered." {n}Her hand finds yours in the grass and holds it, hard.{/n} "It's very peaceful. I don't care for it at all."''',
        c("Continue", "last")),
    cam("last", '''{n}The cemetery bell rings the hour. She gets up, and shakes out her skirt, and puts the veil down again.{/n}
{n}She looks back once, from the gate, at the plain stone under the hawthorn and the brown lilies in their jar.{/n} "I shall come here every year," {n}she says.{/n} "It's the only place in the world where I'm exactly what everyone thinks I am."
"Come to me soon. Not here. Somewhere with a lock on the door. There's something I want to teach you, and I don't think it should be done in front of me."''',
        c("[Walk her back through the dark]", flags=(GRAVE,))),
    ], requires=("trickster.ever", RET, KILLED), forbids=(CLOSED, GRAVE), delay=24, last=5, Relationship=REL,
    Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN], InteractionHub=PRESENCE))


# --- The spirits' due (dead otherwise): she has chosen. ---------------------------------------------------------------

SCENES.append(scene(P + "beat.spirits_due", "The spirits' due", "Camellia", 3,
    '"You\'re up. You\'re well. You\'re frightening the quartermaster."', [
    cam("open", '''"I am well, thank you, my friend. I am better than well." {n}She is sitting at the edge of camp with her feet in the grass and her face turned up to the sun, like a woman at a spa.{/n} "Do you know what dying is like? It's like the moment after a very long concert, when the music stops and nobody has begun to clap. I lay in that silence for a day and a half. I've never heard anything so beautiful."''',
        c("Continue", "chosen")),
    cam("chosen", '''"And then you called me back, and you made me a promise, and the spirits heard it." {n}She turns her head and looks at you, still smiling, and lifts the silver bowl from the grass beside her.{/n} "The new moon is tonight. I thought you ought to know. I thought you ought to have the afternoon to decide how brave you mean to be."''',
        c('"How much will they want?"', "who"),
        c("[Say nothing, and hold out your wrist]", "silent"),
        c('"What if I stop you?"', "not")),
    cam("who", '''"As much as I decide." {n}Quite gently.{/n} "That was the bargain. You don't ask, and I don't tell you. I promise I'll stop before you faint. Probably." {n}She pats your hand.{/n} "Most people would have bargained harder for their own blood. You didn't bargain at all. You'll have to decide tonight what kind of person that makes you, which I think you've been putting off."''',
        c("Continue", "unmissed")),
    cam("silent", '''{n}She looks at your wrist in the sunlight, and then up at you. Her smile changes, very slightly, into something warmer and much more alarming.{/n}
"Oh, you're good. Not tonight, darling. Put it away. Anticipation quickens the imagination." {n}She takes a long breath of the morning air.{/n} "I'm so glad I didn't stay dead."''',
        c("Continue", "unmissed")),
    cam("not", '''"Then you stop me." {n}She shrugs.{/n} "And the spirits remember that you promised and didn't pay, and so do I, and I lie back down, and this time nobody calls me overacting." {n}She considers.{/n} "But you won't. I've watched you. You keep your promises when they're expensive. It's the only thing about you I don't understand."''',
        c("Continue", "unmissed")),
    cam("unmissed", '''"It's a strange thing, you know. I've spent my whole life taking. I had a list of people I would take from, and I took. And now I'm sitting in the sun waiting for someone to come to me and give." {n}She sounds genuinely thoughtful.{/n}
"I don't know what the flies will make of it. They've never been fed anything freely given. They may not like the taste." {n}She smiles.{/n} "Or they may never want anything else."''',
        c("Continue", "after")),
    cam("after", '''{n}She stands, and brushes the grass from her skirt, and puts her hand flat on your chest for a moment, just over the heart, as if checking a clock.{/n}
"Come to me soon. Somewhere with a lock on the door. There's something I want to teach you, now that I know what it feels like from the other side."''',
        c("[Watch her walk back into camp]", flags=(DUE,))),
    ], requires=("trickster.ever", RET, OWED), forbids=(CLOSED, KILLED, DUE), delay=24, last=5, Relationship=REL,
    AnswerLists=[HUB_LIST], ContactUnit=UNIT))


# --- The lesson: where a friend would stand. -------------------------------------------------------------------------

met(P + "beat.lesson", "Where a friend would stand", '"You said you wanted to teach me something."', [
    cam("open", '''"I did. Lock the door." {n}She waits until you have. Then she draws the small clean knife, not from her sleeve, but from yours; you did not feel her put it there.{/n} "You've been carrying it since breakfast, and wrong. Everybody does. They carry it as if they might need it. You should carry it as if you've already decided."''',
        c("Continue", "where")),
    cam("where", '''{n}She takes your hand and closes it round the hilt, and then she moves your hand, slowly, the way the dancing master moved her feet.{/n}
"Not here. Everybody goes for here. It's a soldier's mistake. The ribs are in the way." {n}She moves it an inch to the side, under her own breastbone.{/n} "Here. Up and in. And you must be close. As close as a friend. Close enough that they don't see it coming, because they're looking at your face."''',
        c("Continue", "heart")),
    cam("heart", '''"Did you know that blood only flows while the heart is still beating? I didn't, until I watched. Beat. Beat. Beat. And then nothing, and it simply lies there, like a dropped glove." {n}She says it dreamily, as if describing a sunset.{/n}
"I should know. I have looked. People do insist on looking at one's face instead, which is so convenient."''',
        c("Continue", "throat")),
    cam("throat", '''{n}She lifts your hand, and the knife in it, and lays the edge against her own throat, just under the jaw where the pulse is. Then she lets go.{/n}
"Now," {n}she says, and her eyes are very wide, and very bright, and fixed on yours.{/n} "Tell me what you feel. Don't lie. I'll know."''',
        c("[Hold it perfectly still, and look back at her]", "steady"),
        c("[Take the knife away]", "flinched"),
        c('[Trickster] "I feel like you\'ve done this before, from the other side."', "other_side")),
    cam("steady", '''{n}The knife does not move. Her pulse jumps against the steel, once, twice, and then settles, and then, very slowly, speeds up again, and it has nothing to do with fear.{/n}
"Oh," {n}she breathes.{/n} "Oh, there it is. There it is. Interest. How flattering. Most people are far less courteous with a knife in their hand. They look frightened, or angry, or sick." {n}She puts two fingers on your wrist and takes the knife back, very gently.{/n} "You just look interested."''',
        c("Continue", "done", flags=(LESSON, STEADY))),
    cam("other_side", '''{n}For one moment, all the brightness goes out of her face, and what is left underneath is very still and very old.{/n}
"Yes," {n}she says.{/n} "Many times. Never from this side."
{n}The knife has not moved. Her pulse is going like a bird's under it. She looks at the edge, and at your hand, and then at you, and she smiles, slowly, as if she had just been given a present she had not dared to ask for.{/n} "It's much more frightening from this side. I like it."''',
        c("Continue", "done", flags=(LESSON, STEADY))),
    cam("flinched", '''{n}You take the knife away. She watches it go with an expression you cannot read, then takes it from your hand and tucks it back into your sleeve herself.{/n}
"There. That's what most people do." {n}She doesn't sound disappointed. She sounds as though she has learned something she will think about later.{/n} "It's all right, my friend. It isn't a test. Not yet. That comes afterwards, and it's much harder."''',
        c("Continue", "done", flags=(LESSON, FLINCHED))),
    cam("done", '''"Go now. I have to think about my price." {n}She is at the door before you, unlocking it.{/n} "I have yet to decide how troublesome you are worth making."''',
        c("[Go]")),
], requires=("trickster.ever", RET), forbids=(LESSON,), delay=24, any_groups=[[GRAVE, DUE]],
   living=(DANCE,), living_groups=())


# === After her answer ===================================================================================================

# --- The shelf. --------------------------------------------------------------------------------------------------------

met(P + "bond.shelf", "The shelf", '"Camellia. What have you done to my room?"', [
    nar("open", '''{n}Your room has been tidied. Not cleaned; tidied, the way a museum is. Your papers are in stacks squared to the edge of the desk. Your spare boots stand at attention. On the shelf above the bed, where you keep nothing in particular, there is now a row of things: a dried rose, a pressed camellia flower in a little frame, the bone snake of an amulet coiled in a saucer, a small clean knife, and a folded sheet of paper.{/n}''',
        c("Continue", "shelf")),
    cam("shelf", '''"I've moved in." {n}She is sitting on your bed with her ankles crossed, eating an apple with a knife, in small precise slices.{/n} "A little. The things I keep are on the shelf. Everything I own that means anything fits on one shelf. Isn't that sad? Isn't that tidy?"
"The rose is from my father's garden, the one I was permitted to walk in, behind a gate. The camellia is pressed. I hate the things. My mother named me for one, and it's the only thing she left me, so I keep it where I can dislike it properly. The knife you know." {n}She points at the paper with the knife, not the apple.{/n} "And that is my list."''',
        c('"What list?"', "list")),
    cam("list", '''{n}You unfold it. It is a list of names in her small, beautiful, schoolroom hand, perhaps thirty of them. Some are crossed out. Beside every crossed-out name is a date. You recognise two: a steward from Kenabres who was found in a canal, and a chaplain in Drezen who fell down a stair. At the very top of the list is your own name. It has been crossed out, very neatly, and written again underneath.{/n}''',
        c("Continue", "what", requires=(KILLED,)),
        c("Continue", "what_d", requires=(RET,), forbids=(KILLED,)),
        c("Continue", "what_a", forbids=(RET,))),
    cam("what_a", '''"Those are my friends." {n}She says it with great tenderness.{/n} "All my friends. The ones with lines through them, I have finished being friends with. The others are still waiting. They don't know that. It's the only kindness I can do them."
{n}She slices the apple.{/n} "I wrote you in after our little game. I crossed you out the night I decided how I'd do it. Then I wrote you in again. I've never kept a name I've crossed out. I thought you ought to have it."''',
        c("[Fold it and put it back on the shelf]", "kept"),
        c("[Hold it to the candle]", "burned"),
        c('"There are names on here that aren\'t crossed out."', "names")),
    cam("what", '''"Those are my friends." {n}She says it with great tenderness.{/n} "All my friends. The ones with lines through them, I have finished being friends with. The others are still waiting. They don't know that. It's the only kindness I can do them."
{n}She slices the apple.{/n} "I crossed you out the night you told me to die convincingly. Then I wrote you in again. I have never done that before. I thought you ought to have it. It's the most romantic thing I own."''',
        c("[Fold it and put it back on the shelf]", "kept"),
        c("[Hold it to the candle]", "burned"),
        c('"There are names on here that aren\'t crossed out."', "names")),
    cam("what_d", '''"Those are my friends." {n}She says it with great tenderness.{/n} "All my friends. The ones with lines through them, I have finished being friends with. The others are still waiting. They don't know that. It's the only kindness I can do them."
{n}She slices the apple.{/n} "I crossed you out the day I died, lying under that cloak by the wagons. It seemed only fair; I was leaving. Then you told my corpse it was overacting, and I wrote you in again. I thought you ought to have it. It's the most romantic thing I own."''',
        c("[Fold it and put it back on the shelf]", "kept"),
        c("[Hold it to the candle]", "burned"),
        c('"There are names on here that aren\'t crossed out."', "names")),
    cam("names", '''"Yes." {n}She doesn't pretend not to understand.{/n} "There are. You're going to ask me to promise. I'll say something charming, and you'll know it's a lie, and we'll both feel very grown up."
{n}She sets the apple down.{/n} "Or you could do something with the paper, and I'll learn what kind of person I'm living with. I'd prefer that. I've had quite enough of promises. I've made a great many of them."''',
        c("[Fold it and put it back on the shelf]", "kept"),
        c("[Hold it to the candle]", "burned")),
    cam("kept", '''{n}You fold it along its old creases and put it back on the shelf, beside the knife. She watches you do it. Her face does something complicated.{/n}
"You're keeping it." {n}Very quietly.{/n} "You're keeping my friends on your shelf. Next to your own name." {n}She laughs, a little unsteadily.{/n} "Now I shall have to be careful. How tiresome. You'll know if one of them changes."''',
        c("[Leave it where it is]", flags=(SHELF, LIST_KEPT))),
    cam("burned", '''{n}The paper catches at the corner and goes up all at once, as old paper does. She watches it burn with her chin on her hand and an expression of great, patient amusement.{/n}
"How gallant. How completely useless." {n}She taps her temple with the point of the knife.{/n} "I have them all by heart, my friend. I wrote them down for you, not for me." {n}She picks up the apple again.{/n} "But you tried. I do like it when you try."''',
        c("[Brush the ash off the shelf]", flags=(SHELF, LIST_BURNED))),
], requires=("trickster.ever", COMMITTED), forbids=(SHELF,), delay=48, living=())


# --- The witness. ------------------------------------------------------------------------------------------------------

met(P + "bond.witness", "The witness", '"You\'re worried. You never look worried."', [
    cam("open", '''"I'm not worried. I'm inconvenienced." {n}She is pacing, which you have never seen her do: six steps to the wall, six back, her skirts hissing.{/n} "Someone saw me."''',
        c("Continue", "killed_w", requires=(KILLED,)),
        c("Continue", "dead_w", requires=(RET,), forbids=(KILLED,)),
        c("Continue", "alive_w", forbids=(RET,))),
    cam("alive_w", '''"A lamplighter in the lower city, last week. I was very neat. I always am." {n}She stops pacing.{/n} "He didn't see anything but my face coming out of the alley behind the tannery, and my face is very memorable, and now the porter is dead and there is a man in a tavern by the river telling everyone who will listen that he saw a lady come out of that alley with her sleeves rolled up."''',
        c("Continue", "choice")),
    cam("killed_w", '''"A woman at the chapel, at the service for the Kenabres dead. I went for the music. I sat at the back, and I lifted my veil, just for a moment, because it was very hot. And a woman in the pew in front turned round." {n}She stops pacing.{/n} "She knew me. She used to buy candles from my father's steward. She went white as a sheet and said 'Lady Gwerm' in front of the chaplain, and then she fainted. They carried her out. She's in the infirmary. She's telling everyone who will listen that she saw a dead woman in church."''',
        c("Continue", "choice")),
    cam("dead_w", '''"A night-soil man in the lower city. The night after the wagons." {n}She stops pacing.{/n} "He saw me come out of the alley. He didn't see anything else, he couldn't have, I was very neat. But he saw my face, and my face is very memorable, and now the porter is dead and there is a man in a tavern by the river telling everyone who will listen that he saw a lady come out of that alley with her sleeves rolled up."''',
        c("Continue", "choice")),
    cam("choice", '''"I can take care of it." {n}She says it lightly, reasonably, the way one offers to see to the washing.{/n} "It would be very easy. People like that fall down stairs all the time. It's practically their vocation."
"Or you can take care of it. Your way." {n}She looks at you.{/n} "You are so resourceful. I should like to see your solution before I employ mine."''',
        c('[Trickster] "Leave it to me. By tomorrow, nobody will believe a word the witness says. Including the witness."', "lied"),
        c('"Do it your way."', "hers")),
    cam("lied", '''{n}It takes you one afternoon. You visit the witness with a chaplain in tow and grave concern on your face. You ask, gently, whether the lady they saw had a veil. And a fan. And a small dog. And had she perhaps also been singing? By the time you leave, the witness has seen a veiled lady, a singing ghost, a dog made of mist and a procession of nuns, and the chaplain has recommended rest, and the story has become the sort of thing people tell children at bedtime. The chaplain has the witness moved to the quiet ward, for rest, and nobody asks after them there.{/n}''',
        c("Continue", "lied_after")),
    cam("lied_after", '''"You made them into a ghost story." {n}Camellia is laughing so hard she has to sit down on the edge of the table.{/n} "Oh, that's so much crueller than anything I would have done. They'll spend the rest of their life being the one who saw the ghost."
{n}Then she stops laughing, and looks at you with that terrible, bright tenderness.{/n} "You saved someone from me. And you did it by being worse." {n}She leans in and straightens your collar, very carefully, as though you were something of hers she means to keep clean.{/n} "I shall have to watch you now. All the time. I want to see what else you'll ruin for me."''',
        c("[Let her say it]", flags=(WITNESS_LIED,))),
    cam("hers", '''"Thank you." {n}She says it as sincerely as she has ever said anything. She kisses your cheek, and straightens your collar, and leaves.{/n}
{n}Two days later, the report says the witness slipped on the wet steps by the river in the dark. Everyone agrees it was a terrible accident. The steps are very steep there. Camellia comes to dinner that night in a new dress and is charming to everyone, and she does not look at you once until the dessert, and then she does not stop.{/n}''',
        c("[Hold her gaze]", flags=(WITNESS_HERS,))),
], requires=("trickster.ever", COMMITTED, SHELF), forbids=(WITNESS_LIED, WITNESS_HERS), delay=72, living=())


# --- Not today. --------------------------------------------------------------------------------------------------------

NOT_TODAY_LEADS = [
    ("kept", cam, '''"You still have my list on your shelf. I look at it every night before I sleep. Nobody on it has changed." {n}A small, wry smile.{/n} "You see what you've done to me. I'm keeping accounts."''', LIST_KEPT),
    ("burned", cam, '''"You burned my list. I rewrote it the next morning, from memory, and then I burned it myself. It seemed only polite to finish what you started."''', LIST_BURNED),
    ("ghost", cam, '''"They're still telling the story of the singing ghost in the chapel, you know. I heard it in the market yesterday. The dog has grown wings."''', WITNESS_LIED),
    ("steps", cam, '''"I walked by the river steps last night. Somebody has put up a railing." {n}She says it without any expression at all.{/n}''', WITNESS_HERS),
]
met(P + "bond.not_today", "Not today", '"You\'re very quiet tonight."', [
    nar("open", '''{n}It is late, and raining, and she is sitting at your window with the shutters open, watching the water run off the eaves. The small clean knife is on the sill beside her, point towards the room, as it always is. She does not turn round.{/n}''',
        c("Continue", "lead")),
    *lead([("lead", cam, '''"I'm thinking." {n}She draws a line in the condensation on the glass, and then another across it.{/n} "About after. After the war. After your Wound is closed and your crusade is over and everyone goes home."''', None),
           *NOT_TODAY_LEADS], "after"),
    cam("after", '''"I'll want it back, you know. The knife. One day." {n}Now she turns round.{/n} "Not because I've stopped loving you. Because I will have. That's how it works, with me. The more I love someone, the more I want to see their face when they understand. It's the only thing I've ever wanted, and I have wanted it so very much."
"I'm telling you so you'll know the day. I'll be smiling. I promised you that."''',
        c('"Then I\'ll be smiling back."', "smile"),
        c('[Trickster] "When that day comes, I\'ll die convincingly. You\'ll never know if I meant it."', "convincing"),
        c('"Not today, though."', "today")),
    cam("smile", '''{n}She looks at you for a long time, the rain loud on the shutters.{/n}
"Yes," {n}she says at last.{/n} "Yes, you would. That's why it hasn't been today." {n}She holds out her hand, and you take it, and she pulls you down to the window seat beside her, and does not let go.{/n}''',
        c("Continue", "night", flags=(NOT_TODAY,))),
    cam("convincing", '''"Oh." {n}It is almost a gasp. Then she is laughing, with her forehead against your shoulder.{/n} "Oh, you monster. You'd do it. You'd lie there with my knife in you and I would never, ever know whether you were really dead. You'd ruin it for me forever."
{n}She lifts her head.{/n} "Oh, that's cruel. Say it again."''',
        c("Continue", "night", flags=(NOT_TODAY,))),
    cam("today", '''"Not today." {n}She says it after you, carefully, the way she says the names of flowers.{/n} "No. Not today. Today I'm going to do something very ordinary, and very dull, and I intend to enjoy it enormously."
{n}She closes the shutters on the rain.{/n} "I'm going to go to bed with someone I'm not going to kill."''',
        c("Continue", "night", flags=(NOT_TODAY,))),
    nar("night", '''{n}She takes the knife off the sill and puts it, point first, in the wood of the window frame, where it quivers and is still. Then she takes your face in both hands and kisses you, slowly, thoroughly, with her eyes open, as if she means to remember exactly what your face does.{/n}
{n}Her hands are cold from the window and then they are not. She undoes your shirt one button at a time and counts them under her breath, the way she counted the dance. On the last button she stops counting and pulls you down onto the bed with her, and the rain goes on and on against the shutters, and neither of you hears it.{/n}''',
        c("[Put out the candle.]")),
], requires=("trickster.ever", COMMITTED), any_groups=[[WITNESS_LIED, WITNESS_HERS]], forbids=(NOT_TODAY,), delay=72, living=())

from storylines.camellia_trickster import city  # noqa: E402 (Q8)
city(P + "bond.shelf", P + "bond.witness", P + "bond.not_today")
from storylines.camellia_trickster import in_drezen  # noqa: E402 (Q8)
in_drezen(FUNERAL_SCENE)
