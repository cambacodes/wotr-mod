"""Shamira after the waking: her city, her visit, the game she proposes, and the throne she still wants
(shamira_trickster holds the device; shamira_mind the nights behind the Commander's eyes and the waking).

The commit (11 §2): "think of anything but me". In the room where she first read the Commander (the Harem of Ardent Dream,
Shamira_dialogue: the mind-duel of Cue_0039 0a75cdac to Cue_0058 0e929c72), she proposes a game of her own trade, and the
Commander loses it on purpose. Nothing is spoken: every answer in the game is a thought. Winning it is the soft no (she
stays an ally); throwing her out of the Commander's head, as a Commander once did in public (Cue_0055 b15365b6), is the
hard no. The cut comes as she opens the Commander's mind and the body follows.

Her way between worlds is canon: from Socothbenoth's house in the city, any arch in Alushinyrra "will teleport you to my
palace" for one who bears her mark (Cue_0180 8d19d6a4); she walks the closets back to Drezen. Her throne-hunger is canon
(Nocticula/Cue_0015 7cad8bc1, Cue_0021 84df3b22; Epilogues/Cue_0296 354a799d). The evil demand of this half is hers: help
her to her lady's throne. The Commander may stand where she can see, refuse her Nocticula, or lie to a mind-reader.
Nothing here harms Nocticula; the throne is a wish, and the epilogue keeps it one.
"""
from story_format import c
from storylines.shamira_trickster import (ALLY, BARRACKS, CAST_OUT, CITY, CLOSED, COMMITTED, EMBODIED, GAME, GROWER_DEAD,
                                           KEPT, LIED_HER, LOST_GAME, NOCT_HIDING, NOT_NOCT, P, READ, SOCOTH_GONE, STAND,
                                           THREW_OUT, THRONE, TORN, VISITED, WHISPER, nar, sh)
from storylines.shamira_trickster import page as _page
from storylines.shamira_mind import LAST_HER, LAST_HOME, LAST_PEACE, WANT_STEWARD

SCENES = []


def page(*args, **kw):
    _page(*args, into=SCENES, **kw)


NOCT_WILL_ATTEND = "noct.will_attend"      # read in node text only (Nocticula/Answer_0011 started it)
ARCH = P + "arch"                          # she took the Commander through the arch to her palace
HELD = P + "morning.held"
LEFT = P + "morning.left"
AS_FOOL = P + "court.fool"
AS_GUEST = P + "court.guest"
AS_EQUAL = P + "court.equal"

LIVE = (CLOSED, KEPT, CAST_OUT)


# --- The first night of company: the cost, in play ---------------------------------------------------------------------

FIRST_COMPANY = P + "first_company"

page(P + "after.first_company", "Company", [
    nar("start", '''{n}The first night after she walked out of your wardrobe, you are almost afraid to sleep. You lie a long time listening to the camp, and then, without deciding to, you are dreaming.{/n}''',
        c("Continue", "home", requires=(LAST_HOME,)),
        c("Continue", "peace", requires=(LAST_PEACE,)),
        c("Continue", "her", requires=(LAST_HER,)),
        c("Continue", "plain", forbids=(LAST_HOME, LAST_PEACE, LAST_HER))),
    nar("home", '''{n}The kitchen again: the door you knew the sound of, the bread, the stair. You are alone in it for as long as it takes to notice that you are waiting.{/n}
{n}Then the door opens without a knock, and she comes in out of a dark that is not in your dream, shaking cold off her shoulders like snow, and sits down at your table as if she has sat there all her life.{/n}''',
        c("Continue", "sits")),
    nar("peace", '''{n}The green road again, north of Drezen, the crusade going home in no order. You walk it alone for as long as it takes to notice that you keep looking back.{/n}
{n}Then she is on the road behind you, coming out of a dark that is not in your dream, shaking cold off her shoulders like snow, and falls into step beside you as if she has walked it all her life.{/n}''',
        c("Continue", "sits")),
    nar("her", '''{n}The Harem again, the throne, the light: the dream of her you gave her on the wardrobe floor. You are alone in it, with a dreamed woman on a dreamed throne, for as long as it takes to notice that the dreamed one is not looking at you.{/n}
{n}Then the real one comes in at the great doors, out of a dark that is not in your dream, shaking cold off her shoulders like snow, and walks straight past her own image without a glance, and stops in front of you.{/n}''',
        c("Continue", "sits")),
    nar("plain", '''{n}Kenabres, the square, the smoke. You are alone in it for as long as it takes to notice that you are looking at the fountain.{/n}
{n}Then she is sitting on it, come out of a dark that is not in your dream, shaking cold off her shoulders like snow.{/n}''',
        c("Continue", "sits")),
    sh("sits", '''"Don't get up." {n}She holds her hands out, not to you: to the dream itself, the way a traveller holds them out to a hearth. The colour comes back into her fingers while you watch.{/n}
"This is how it will be. Every night. I will come in out of the cold, and I will sit down in whatever you are dreaming, and I will warm my hands, and I will take one coal home with me. You will not always see me. You will always know." {n}She looks at you sidelong.{/n} "Is it very terrible?"''',
        c('"Yes."', "yes", flags=(FIRST_COMPANY,)),
        c('"No."', "no", flags=(FIRST_COMPANY,)),
        c("[Say nothing. Hold your hands out beside hers.]", "hands", flags=(FIRST_COMPANY,))),
    sh("yes", '''"Good." {n}Without heat.{/n} "It should be. I took something from you that nobody gets back. If you told me it was nothing, I would know you were lying, and I would have to think less of you." {n}She warms her hands a while longer. Then, not looking at you:{/n} "I will try to be quiet. Some nights."''',
        c("Continue", "coal")),
    sh("no", '''"Liar." {n}But she does not sound as if she minds.{/n} "You'll tell me the truth one night when you're tired, and I will already know it, and we'll both pretend it's news." {n}She warms her hands a while longer.{/n} "Until then, say no. It's a nice sound. Nobody has said no to me in that voice before."''',
        c("Continue", "coal")),
    sh("hands", '''{n}You hold your hands out beside hers, to a fire that is only a dream of a fire, and it is warm.{/n}
{n}She glances at your hands, and then at your face, and for a moment she has nothing clever to say at all. She shifts along, a little, to make room.{/n}''',
        c("Continue", "coal")),
    nar("coal", '''{n}When she goes, she takes something with her: you feel it go, a warmth lifted out of the dream in two cupped hands, the way you would carry a coal from one hearth to another on a cold morning. The dream goes on without it. It is a little dimmer. It is still yours.{/n}
{n}You wake before the sentries change, and lie there, and are not alone, and do not know what to do about it.{/n}''',
        c("[Get up.]")),
], requires=("trickster.ever", EMBODIED), forbids=(FIRST_COMPANY,) + LIVE, delay=12)


# --- Her city: the first whisper from Alushinyrra ---------------------------------------------------------------------

page(P + "after.city", "Who sat in my chair", [
    nar("start", '''{n}You dream of the war tables, the way you do: maps, lamps, the same argument about the same river crossing. At the edge of the dream, where the lamplight gives out, a red-haired woman is sitting on a map chest with her legs crossed, warming her hands at your lamp.{/n}
{n}She has come for her coal, as she comes every night now. She takes it without asking. Then she talks.{/n}''',
        c("Continue", "home")),
    sh("home", WHISPER + '''"I am home." {n}The voice is hers, and it is rich with a satisfaction so deep it is almost sleepy.{/n} "I came out of a wardrobe in Socothbenoth's house, naked except for your coat, and walked through my own city at the hour when the demons are drunkest, and nobody knew me. Nobody. They were all too busy wearing black for me."''',
        c("Continue", "chair")),
    sh("chair", '''"My Harem was dark. My court had split in three. And in my chair, on my throne, in my light that withers fools, sat a glabrezu I once made kneel for a whole year because he looked at me without asking." {n}She sounds delighted.{/n} "He had my crown on. He had had it cut down to fit his horns."
"I let him talk for a while, in his head, about how he'd always known I'd fall. Then I went in and took his dreams too. He is sitting in the Lower City now, beside Ziforian, and he cannot remember his own name. It suits him."''',
        c('"You were meant to be dead. People will talk."', "talk"),
        c('"You\'re cruel, Shamira."', "cruel")),
    sh("talk", '''"People will talk to me. That is a different thing." {n}A soft laugh.{/n} "I have not told anyone my name. I am simply sitting in my Harem again, in a face they know, and letting them wonder. Nobody in Alushinyrra will ask a woman on that throne who she is. It's much too dangerous to know."''',
        c("Continue", "grower", requires=(GROWER_DEAD,)),
        c("Continue", "lady", forbids=(GROWER_DEAD,))),
    sh("grower", '''"And the Street of Vats is in an uproar. Somebody killed Oshkuvar in his own cellar and nobody can find out who, and in the Fleshmarkets a murder nobody can sell is the most frightening thing there is." {n}She is purring.{/n} "Sarzaksys has put a price on the killer's head. It is a very flattering price. I thought about claiming it, just to see his face."''',
        c("Continue", "lady")),
    sh("cruel", '''"Yes." {n}No shame at all, only amusement that you felt the need to say so.{/n} "I was cruel before you killed me, and I am cruel now, and in between I spent a week behind your eyes, being kind to you, because you were the only thing in there with me. Don't mistake a week for a nature, Golarian."''',
        c("Continue", "grower", requires=(GROWER_DEAD,)),
        c("Continue", "lady", forbids=(GROWER_DEAD,))),
    sh("lady", '''"And she knows." {n}The voice changes, as it always does when she comes to this.{/n} "My lady. She has not come. She has not sent. But the glabrezu's guards stepped aside for me as if they had been told to, and on the first night a black silk pillow was on my throne that I did not put there." {n}Silence.{/n} "She is letting me. As she always did. She is letting me want her chair and sit in mine, and she is watching to see what I do."''',
        c("Continue", "hiding", requires=(NOCT_HIDING,)),
        c("Continue", "attends", requires=(NOCT_WILL_ATTEND,), forbids=(NOCT_HIDING,)),
        c("Continue", "cold", forbids=(NOCT_HIDING, NOCT_WILL_ATTEND))),
    sh("hiding", '''"They say her throne is empty. They say she went into the Council and did not come out, and that she is hiding." {n}The voice goes very quiet.{/n} "I have walked past the doors of her palace three times tonight. They are open. There is nobody on the other side of them." {n}A breath.{/n} "I have not gone in. I wanted to tell someone first. Isn't that absurd?"''',
        c("Continue", "cold")),
    sh("attends", '''"You told her about her brother's little plot, didn't you. I found it in you, while I was living in your head, and forgot it until tonight." {n}Something almost like amusement.{/n} "You sold her brother to her and me to him. You are a very busy clown. She will be grateful for about a century, which is a long time, for her."''',
        c("Continue", "cold")),
    sh("cold", '''"I'm cold again." {n}It comes out abruptly, as if she did not mean to say it.{/n} "Not like before. Only at the edges. Your coal burns well, Golarian, but it burns down by dusk, and my Harem has a great many rooms." {n}A pause, and then, lightly, much too lightly:{/n} "I'm coming to Drezen. I want to see what you look like asleep, from the outside, with me in there. I have never looked from the outside before."''',
        c("[Sleep on. She is still there.]", flags=(CITY,))),
], requires=("trickster.ever", EMBODIED), forbids=(CITY,) + LIVE, delay=48)


# --- Her visit: out of the Commander's wardrobe -------------------------------------------------------------------------

page(P + "after.visit", "Out of the wardrobe", [
    nar("start", '''{n}You wake from a dream of Kenabres in which a red-haired woman was sitting on the fountain, as she does every night now, and for a moment you do not know what woke you. Then you see that the wardrobe door is open, and that there is a woman sitting on the end of your bed with her legs crossed, watching you.{/n}
{n}She has dressed properly this time: a gown the colour of the inside of a fire, cut low and slit high, and her red hair piled up with pins of black glass. She looks as if she has been sitting there for some time.{/n}''',
        c("Continue", "watching")),
    sh("watching", '''"You smile in your sleep when I come in." {n}She says it the way a scholar notes something odd in a specimen.{/n} "I have watched ten thousand sleepers from the inside. I have never watched one from the outside while I was in there too. You turn towards the door before I open it. You make room on the fountain." {n}She leans forward and puts one long finger on your forehead, exactly where she used to push her way in.{/n} "It is very strange to be expected."''',
        c('"You\'re always there now."', "did"),
        c('"I like the company."', "restful")),
    sh("did", '''"I am." {n}She does not take her finger away.{/n} "I have been in thousands of heads. I have never once gone back to the same one twice. Nobody told me it would feel like..." {n}She stops. She takes the finger away and looks at it.{/n} "Like coming home. It feels like coming home. I am furious about it, and I do not know with whom."''',
        c("Continue", "torn", requires=(TORN,)),
        c("Continue", "body", forbids=(TORN,))),
    sh("restful", '''"Liar." {n}Fondly, for her.{/n} "You miss being alone in there. I can feel you missing it, some nights; it moves through your dreams like a draught under a door." {n}She takes her finger away.{/n} "I know that draught. I have had it for six thousand years. I did not think I would ever be the thing that caused it."''',
        c("Continue", "torn", requires=(TORN,)),
        c("Continue", "body", forbids=(TORN,))),
    sh("torn", '''{n}She sees you looking at the seam across her collarbone, white against the fire-coloured silk, and does not cover it.{/n}
"My court thinks it's a duelling scar. I've let them. I've had three challenges already, from fools who thought it meant someone once beat me." {n}She smiles, slowly.{/n} "None of them will challenge anyone again."''',
        c("Continue", "body")),
    sh("body", '''"The body is good." {n}She stretches, the way a cat stretches, to show you.{/n} "It's slow in the mornings. It gets hungry, which I had forgotten was a thing bodies did. It likes wine too much. And it is always, always a little cold." {n}She draws her feet up onto the bed.{/n} "Your coal is the only warm thing in it. I can feel it in here, burning down, every day, by dusk. Then I come and sit in your dragon, or your bread, or your stupid barley, until I'm warm again."''',
        c("Continue", "barracks", requires=(BARRACKS,)),
        c("Continue", "arueshalae", forbids=(BARRACKS,))),
    sh("barracks", '''"And the barracks." {n}Her eyes go bright.{/n} "I felt it the moment I came into your city. They're still in there, the men I walked through: I can taste them, flat and grey, like bread left out. A sergeant of theirs hanged himself last week. Did they tell you? No. They put it down to the war." {n}She considers.{/n} "Two more of them will desert before the spring. One will paint something magnificent. I left a spark in him, by accident. I was in a hurry."''',
        c('"You said nobody would know."', "know"),
        c("[Say nothing.]", "arueshalae")),
    sh("know", '''"Nobody does know." {n}Reasonably.{/n} "Except you. And now the Ledger in your head, which I can read upside down. You wrote it down under 'secrets', with a little mark beside it." {n}She laughs.{/n} "You keep accounts of your sins. How very Golarian. Hide that page, clown. There are people in your camp who'd read it."''',
        c("Continue", "arueshalae")),
    sh("arueshalae", '''{n}She tilts her head, listening to something far off.{/n} "Your succubus is two rooms away. Arueshalae. She's awake; she's always awake. She knows I'm here." {n}A dry little pause.{/n} "She's praying. To Desna. For you, I think, not for herself. She has learned to dream of flowers and to pray for other people." {n}The contempt in her voice does not quite cover the other thing.{/n} "I cannot stand to listen to it. Close your door when I come, next time."''',
        c("Continue", "next")),
    sh("next", '''{n}She gets up off your bed and walks to the wardrobe, and stops in its door with her hand on the frame, exactly where she stood the morning she woke.{/n}
"Next time, I am taking you to the Harem. To the room where I first reached into your head." {n}She looks back at you over her shoulder.{/n} "I have a game I want to play with you. I have never played it with anyone. I'll tell you the rules there."''',
        c('"What kind of game?"', "kind"),
        c('"I\'ll come."', "come")),
    sh("kind", '''"The kind I'm good at." {n}And that is all she will say. The wardrobe door closes on her, and when you open it again your coats are hanging there, and they smell of cinnamon.{/n}''',
        c("[Close the wardrobe.]", flags=(VISITED, GAME))),
    sh("come", '''"I know you will. I've read it." {n}She smiles, and for once there is nothing in it but the smile.{/n} "I read it before I asked. I only asked because I wanted to hear you say it with your mouth. It's a much stupider instrument than your head. I find I like it."
{n}The wardrobe door closes on her. When you open it again, your coats smell of cinnamon.{/n}''',
        c("[Close the wardrobe.]", flags=(VISITED, GAME))),
], requires=("trickster.ever", CITY), forbids=(VISITED,) + LIVE, delay=48, kind="visit")


# --- The commit: think of anything but me, in the Harem of Ardent Dream --------------------------------------------------

page(P + "harem", "Think of anything but me", [
    nar("start", '''{n}She comes for you at the dead of night, out of the wardrobe, in black this time, and takes you by the wrist without a word. You go back the way you went for her body: the wardrobe, the empty Council with its candles burning for nobody, Socothbenoth's purple door, the house full of listening closets.{/n}
{n}In the street outside his house there is an arch of black stone. She walks you under it, and the city folds.{/n}''',
        c("Continue", "harem")),
    nar("harem", '''{n}The Harem of Ardent Dream. You remember it full: courtiers, music, the smell of a hundred perfumes and a hundred sins, the crowd that watched her reach into your head. Tonight it is empty. The couches are bare. The fountains still run, and the sound of them fills the great room the way a held breath fills a chest.{/n}
{n}At the far end, on its dais, the throne. The light around it is low, a glow like coals under ash.{/n}''',
        c("Continue", "light_back", requires=(BARRACKS,)),
        c("Continue", "sits", forbids=(BARRACKS,))),
    nar("light_back", '''{n}Brighter than that, when she steps up onto the dais: the light catches from her, and flares, and for a moment it is the old light, the throne-light, and it makes your skin burn with fever where you stand. Two hundred men's dreams went into that light. It suits her terribly.{/n}''',
        c("Continue", "sits")),
    nar("sits", '''{n}She sits on her throne, and crosses her legs, and looks down at you exactly as she looked down at you the first time, a lifetime ago, when you came to her court as a wanderer seeking patronage.{/n}''',
        c("Continue", "where_duel", requires=(THREW_OUT,)),
        c("Continue", "where_read", requires=(READ,), forbids=(THREW_OUT,)),
        c("Continue", "where_crystals", forbids=(THREW_OUT, READ))),
    sh("where_duel", '''"Here. This is where you threw me out of your head." {n}Her voice fills the empty room.{/n} "In front of my whole court. I had not been beaten in public for centuries, and a Golarian did it with {mf|his|her} eyes shut, and the demons cheered. I have thought about that day more than I have thought about my own death." {n}A thin smile.{/n} "Stand where you stood then."''',
        c("[Stand where you stood.]", "rules")),
    sh("where_read", '''"Here. This is where I first had you in my head." {n}Her voice fills the empty room.{/n} "The whole court watched. You let me in because you thought it would amuse me, and it did. You hid something under the barley, or you didn't; either way I have been looking for it ever since. Stand where you stood then."''',
        c("[Stand where you stood.]", "rules")),
    sh("where_crystals", '''"Here. This is where I first went into your head, for my crystals." {n}Her voice fills the empty room.{/n} "I wanted to know what you knew, and I took it, the way I took everything in those days: all at once, with the court watching. I did not look at anything else in there. I was not interested." {n}A small pause.{/n} "More fool me. Stand where you stood then."''',
        c("[Stand where you stood.]", "rules")),
    sh("rules", '''"Here is the game." {n}She leans forward.{/n} "Think of anything but me. Anything at all: your war, your dragon, your bread, your Wound. I will go into that crowded house of yours and look in every room. If I find myself in any of them, anywhere, I win."
"If I don't, you win, and I will never ask you anything again, and we will be what we are. Allies. A clown and the woman he murdered and put back together." {n}A pause.{/n} "And no words. Words are for liars and I will not have them in my Harem tonight. Only what you think."''',
        c("Continue", "begin")),
    nar("begin", '''{n}The heat gathers behind your forehead, the old fever, exactly as it did the first time. But it is not a hand in a drawer tonight. It is slow, and careful, the way you would walk through a house you had once burned down, looking for anything that was left.{/n}
{n}You have to think of something. The game has begun.{/n}''',
        c("[Think of the Wound.]", "wound"),
        c("[Think of Drezen, and the war tables, and every face you owe something to.]", "drezen"),
        c("[Think of moonshine recipes, loudly, the way you did the first time.]", "barley")),
    nar("wound", '''{n}You think of the Wound: the violet sky over the north, the rift in the earth that pulls at the scar under your ribs. It is enormous. It fills the house. She walks all the way round it, slowly, and you can feel her looking.{/n}
{n}And there, at the very edge of it, where the rift's light falls on the ground, is a red-haired woman sitting on a stone with her back to the rift, holding her hands out to it as if it were a hearth.{/n}''',
        c("Continue", "search")),
    nar("drezen", '''{n}You think of Drezen: the walls, the maps, the lamps in the war room, your officers' faces, the dead you carried home. She walks among them, touching nothing.{/n}
{n}And there, in your quarters, you can feel her find it: a wardrobe with its door a little open, and a smell of cinnamon coming out of it.{/n}''',
        c("Continue", "search")),
    nar("barley", '''{n}You think of barley. Mash and yeast and wormwood and copper, the long argument about seals. She laughs out loud in the empty Harem, and the fountains carry it.{/n}
{n}Then she goes looking under the barley, as she promised the first time she would. And under it, where you hid it that first day in her court, the small thing you would not let her have: her, on her throne, burning.{/n}''',
        c("Continue", "search")),
    sh("search", '''{n}She says nothing. Her hands are tight on the arms of the throne. You can feel her, very still, in the middle of your head, deciding whether what she has found counts.{/n}
{n}You can still win. It would be easy. Think of the Wound, only the Wound, the whole violet weight of it, and bury the rest, and she will not look under it twice. She has told you so. She has never lied to you about anything that mattered.{/n}''',
        c("[Stop hiding her. Let her find herself in every room.]", "lost", flags=(COMMITTED, LOST_GAME, ARCH)),
        c("[Think of the Wound. Only the Wound. Until she stops looking.]", "won", flags=(ALLY, ARCH)),
        c("[Throw her out of your head.]", "thrown", flags=(CLOSED, ARCH))),
    nar("lost", '''{n}You stop.{/n}
{n}You stop holding the Wound up in front of everything, and let the house be what it is, and she walks into it. She finds herself behind your eyes, where she lived for a week. She finds herself on the lip of the fountain in Kenabres, where nobody sat before her. She finds herself in the square under the burning spire, and in the barracks' silence, and in the wardrobe, and in the dark on the floor of it among your boots. She finds herself at the edge of every dream you have had since, warming her hands.{/n}
{n}Neither of you says anything. There is nothing to say. She has already heard it.{/n}''',
        c("Continue", "rise")),
    nar("rise", '''{n}She stands up from her throne.{/n}
{n}The light flares with her, low and red, and the heat behind your forehead changes. It is not a search any more. It is her, opening you the way you would open a letter you have waited a long time for, slowly, with the tip of a finger, and every place she touches in your head lights up and stays lit. You hear your own breath catch. You do not remember deciding to breathe that way.{/n}''',
        c("Continue", "steps", requires=(TORN,)),
        c("Continue", "steps_plain", forbids=(TORN,))),
    nar("steps", '''{n}She comes down the steps of the dais, one at a time, and the black gown comes down with her, a pin at a time: from her hair first, the black glass ringing on the stone, and then the rest, falling about her like smoke going the wrong way. Under it she is long and pale and made exactly as she wanted to be made, except for one thin white seam across the collarbone. She puts your hand on it.{/n}
"Yours," {n}she says aloud, and it is the only word spoken in the Harem that night.{/n}''',
        c("Continue", "cut")),
    nar("steps_plain", '''{n}She comes down the steps of the dais, one at a time, and the black gown comes down with her, a pin at a time: from her hair first, the black glass ringing on the stone, and then the rest, falling about her like smoke going the wrong way. Under it she is long and pale and made exactly as she wanted to be made, and she is shaking, very slightly, the way a flame shakes.{/n}
{n}She does not say anything. She takes your face in her long cold hands, and her mouth tastes of cinders.{/n}''',
        c("Continue", "cut")),
    nar("cut", '''{n}The last thing she opens in your head is the thing you had not known was shut: and the fever there becomes something else entirely, and your body follows your mind down onto the steps of her throne, into the heat of her, as if it had only been waiting to be told.{/n}
{n}Above you both, the light around the empty throne burns higher than it has burned since she came home, and the fountains go on running in the dark, and nobody in Alushinyrra is watching.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}There is no morning in the Abyss. There is only the purple light through the high windows changing its mind about how bright to be.{/n}
{n}You wake on the steps of the dais, under her gown, with a dream of her still warm behind your eyes, as always now. She is sitting on the top step with her knees drawn up, awake, watching you, the way she watched you sleep in Drezen. Demons do not sleep. She has been watching the whole night.{/n}''',
        c("Continue", "watch")),
    sh("watch", '''"You dreamed of me all night." {n}Softly.{/n} "I was in there; I'm always in there. But you were dreaming of me before I came in, and in six thousand years I have never once walked into a dream that was already about me and been made welcome in it." {n}She puts one finger on your forehead, the old place.{/n} "It was like a house after a party. Everyone else gone, and the lamps still warm."
"I sit in your sleep every night. You will never be alone in there again. That is the arrangement, and it is not fair, and I will never give you your solitude back."''',
        c("Continue", "last_home", requires=(LAST_HOME,)),
        c("Continue", "last_peace", requires=(LAST_PEACE,)),
        c("Continue", "last_her", requires=(LAST_HER,)),
        c("Continue", "want", forbids=(LAST_HOME, LAST_PEACE, LAST_HER))),
    sh("last_home", '''"The last dream you had alone. The kitchen. The bread and the stair and the voice calling you in." {n}She looks away.{/n} "I go and sit in it sometimes, when the court is loud. You let me. I have never had a kitchen."''',
        c("Continue", "want")),
    sh("last_peace", '''"The last dream you had alone. The green fields. The crusade going home in no order, singing." {n}She looks away.{/n} "It's the dullest dream anyone has ever given me. I walk that road every night. I don't know why."''',
        c("Continue", "want")),
    sh("last_her", '''"The last dream you had alone was me. On the throne, burning." {n}She looks away.{/n} "Nobody in six thousand years has ever dreamed me as I wanted to be. I go back and stand in it, some nights. It's the warmest room you have."''',
        c("Continue", "want")),
    sh("want", '''"Now, listen." {n}The throne-room voice comes back, not all the way.{/n} "You will not shut me in the back of your head again, or anywhere else. Not in a promise, not in a Ledger. You will not ask me to be kind; I tried it for a week and it did not take. And when you want a night alone, just one, you will come here, through that wardrobe, and ask me for it to my face." {n}A slow smile.{/n} "I will make you work for it. I will give it to you in the end. Those are not terms, Golarian. That is simply how it is going to be."''',
        c('"Agreed."', "go", flags=(HELD,)),
        c("[Say nothing. Let her read it.]", "go", flags=(HELD,))),
    sh("go", '''"Good." {n}She stands, and looks down at you on her steps, and for a moment she is exactly as she was the first time, contemptuous and radiant and bored.{/n} "Then get dressed, Commander. You're lying on my floor in my throne room with nothing on, and my court comes back at the third bell, which is now."
{n}She holds out her hand. It is still a little cold.{/n}''',
        c("[Take her hand.]", "bell")),
    nar("bell", '''{n}You do not get dressed in time. She meant you not to.{/n}
{n}The third bell goes somewhere in the palace, deep and slow, and the great doors of the Harem open, and the court comes back in the order it always comes: the servants with the lamps, the musicians, the lesser demons in a crowd, and then the great ones, slowly, so as to be seen. They see you. The Golarian, half in a travelling coat, on the steps of the dais. The music stops before it has started.{/n}''',
        c("Continue", "bell_silence")),
    sh("bell_silence", '''{n}She is already on her throne, dressed, as if she had been there for hours. She does not look at you. She looks at her court, and lets the silence go on until it is unbearable, and then a little longer.{/n}
{n}In your head, very fast:{/n} "They will talk about this for a century whatever I do, so we will decide what they say. What are you, in my Harem? Choose. Quickly. The glabrezu at the back is already working out how to kill you."''',
        c("[Bow low, and play her fool.]", "fool", flags=(AS_FOOL,)),
        c("[Pour yourself a cup of her wine, and sit down on the steps like a guest.]", "guest", flags=(AS_GUEST,)),
        c("[Stand beside her throne, where she can see you.]", "equal", flags=(AS_EQUAL,))),
    sh("fool", '''{n}You bow like a court jester, with a flourish, all the way to the floor.{/n}
"My fool," {n}she says to the room, bored.{/n} "Nocticula's favourite, as some of you will remember. I keep him for the laughs." {n}The court relaxes, a little, the way a dog relaxes when the stick is put down.{/n}
{n}In your head:{/n} "Clever. They'll leave you alone now. Nobody in the Abyss assassinates a joke; it looks bad. You will, of course, have to be funny every time you come here, for the rest of your life."''',
        c("Continue", "bell_end")),
    sh("guest", '''{n}You pour a cup from the jug on the step and sit down with it, in front of all of them, as if the throne room were a tavern.{/n}
{n}Nobody breathes. Then she laughs, low and delighted, and the court, not knowing what else to do, laughs with her.{/n} "My guest," {n}she says.{/n} "Who drinks my wine without asking, and whom I have not yet killed. You may all speculate why." {n}In your head:{/n} "They will. Oh, they will. I will hear nothing else for a year. It will be delicious."''',
        c("Continue", "bell_end")),
    sh("equal", '''{n}You get up and stand beside her throne, at her right hand, where a steward stands, where a lover stands. The court stares.{/n}
{n}She lets them stare. Then she lifts one hand, without looking at you, and lets it rest on your wrist, lightly, for the space of one breath, in front of everyone.{/n}
"Well," {n}says the Ardent Dream to her court.{/n} "Now you know." {n}In your head, much quieter:{/n} "That was either the bravest or the stupidest thing I have ever seen a mortal do in this room. I haven't decided. Don't move."''',
        c("Continue", "steward", requires=(WANT_STEWARD,)),
        c("Continue", "bell_end", forbids=(WANT_STEWARD,))),
    sh("steward", '''"You wanted a steward for Alushinyrra who owed you her life, the first night. I remember." {n}Very dry, in your head.{/n} "Now you are standing where a steward stands. Look at the pair of us. Nocticula would be sick with laughter."''',
        c("Continue", "bell_end")),
    nar("bell_end", '''{n}The music starts again. The court flows back to its couches and its quarrels, and pretends not to look at you, and looks at nothing else.{/n}
{n}When you leave, through the black arch, a demon in a silver mask falls into step beside you for a few paces and murmurs, without turning his head, that he has always admired the Lady Shamira and would be very glad to be of service to her friends. You recognise him. He dreamed of her chair, once, in front of you, with his hands pressed to his temples.{/n}''',
        c("[Go home through the arch.]")),
    sh("won", '''{n}You think of the Wound. Only the Wound. You hold it up in front of everything, the whole violet weight of it, the pull on your scar, the rift, the fire, and you keep it there, and keep it there.{/n}
{n}She looks for a long time. Then the heat goes out of your head, all at once, like a hand out of cold water.{/n}
"You won." {n}Her voice is perfectly level.{/n} "I have never lost this game. I invented it."''',
        c("Continue", "ally")),
    sh("ally", '''"I meant it. I will not ask again." {n}She sits back on her throne, and the low light settles around her, and she looks down at you with the old, vast boredom.{/n} "Allies, then. I owe you a life, and you owe me nothing, and I will pay every favour of it exactly, and not one more." {n}A slight movement of her hand toward the arch.{/n} "Go home, Golarian. My court comes back at the third bell, and I would rather they did not see me having lost."''',
        c("[Go home through the arch.]")),
    nar("thrown", '''{n}You throw her out: with everything you have, all at once, a door slammed on a hand.{/n}
{n}She reels back on the throne as if she has been struck. For a moment her face is naked with shock. Then it closes.{/n}''',
        c("Continue", "out_twice", requires=(THREW_OUT,)),
        c("Continue", "out", forbids=(THREW_OUT,))),
    sh("out_twice", '''"In my own Harem." {n}Very quietly.{/n} "Twice. Once for the court, when you were a stranger and it was a game. And once now, for no one, when it was not."''',
        c("Continue", "out")),
    sh("out", '''"You shut a door on me. In my own house." {n}She stands.{/n}
"You cretin. Get out of my Harem." {n}Her voice does not rise. It does not need to.{/n} "I will still come into your sleep, since this body dies without it. I will sit with my back to you at the far edge of every dream you have, and I will never speak, and you will never see me again."''',
        c("[Go home through the arch, alone.]")),
], requires=("trickster.ever", VISITED, GAME), forbids=(COMMITTED, ALLY) + LIVE, delay=24, kind="visit")




# --- After: the throne she still wants -----------------------------------------------------------------------------------

page(P + "after.throne", "The chair she wants", [
    nar("start", '''{n}She comes out of the wardrobe at dusk this time, in something plain and dark that does not suit her, and sits in your chair at your table, among your maps, and drinks your wine without asking.{/n}
{n}She has a look you know from the Harem: the look of a woman who has decided to say something dangerous and is enjoying the moment before she says it.{/n}''',
        c("Continue", "chair")),
    sh("chair", '''"I have been thinking about my lady's chair." {n}She turns your cup in her long fingers.{/n} "I have been thinking about it for three hundred years; I thought about it the night she came out across the water for me. You know that. You caught me at it, in my own Harem, the day I told you about the birds."
"Now I have your fire and a body nobody grew for a queen, and I am thinking about it again."''',
        c("Continue", "hiding", requires=(NOCT_HIDING,)),
        c("Continue", "not_hiding", forbids=(NOCT_HIDING,))),
    sh("hiding", '''"She is gone into the shadows. Her doors stand open. Her throne is empty, and all of Alushinyrra is waiting to see who is stupid enough to sit in it." {n}Her eyes glitter.{/n} "Somebody will. If it is not me, it will be a glabrezu with his horns through my crown. You would not want that. Think of the city."''',
        c("Continue", "ask")),
    sh("not_hiding", '''"She is on her throne. She knows exactly where I am, and what I want, and she sends me black silk pillows." {n}Her eyes glitter.{/n} "One day she will be bored, or careless, or looking the other way, the way she looked the other way when you carried me out of her bedroom behind your eyes. And on that day I want to know where you are standing."''',
        c("Continue", "ask")),
    sh("ask", '''"So I am asking. Plainly, since you like plain things." {n}She sets the cup down.{/n} "When I go for her chair, whenever that is, will you help me take it? Your crusade, your tricks, your ridiculous luck. Your Council friends, if any of them are still breathing."
{n}Then, as you open your mouth, she smiles.{/n} "Careful. I am in your head. I will hear the answer before you say it."''',
        c('"No. Not against Nocticula. Anyone else, but not her."', "not_her", flags=(THRONE, NOT_NOCT)),
        c('"I won\'t help you and I won\'t stop you. I\'ll stand where you can see me. That\'s all."', "stand", flags=(THRONE, STAND)),
        c('[Lie] "Of course I will."', "lie", flags=(THRONE, LIED_HER))),
    sh("not_her", '''{n}She does not answer for a while. She reads it: all of it, whatever it is in you that says no, and why.{/n}
"You mean it." {n}Flatly.{/n} "You would help me take any throne in the Abyss but hers." {n}A long breath.{/n} "I should hate you for that. I find I only hate that you have a reason, and that I can see it, and that it is not a bad one."
"Very well. Keep your reason. I will keep wanting. We will see which of us gets tired first."''',
        c("Continue", "socoth")),
    sh("stand", '''"Stand where I can see you." {n}She tastes it.{/n} "Neither for me nor against me. Only there, where I can see you, when I go." {n}Something softens, and then she makes it hard again.{/n} "That is what she did for me, you know. My lady. Three hundred years of standing where I could see her. It was the cruellest kindness anyone ever did me, and I loved her for it." {n}She drinks.{/n} "Fine. Stand there. I'll look."''',
        c("Continue", "socoth")),
    sh("lie", '''{n}She laughs until she has to put the cup down.{/n}
"Oh, you thought 'never' so loudly I nearly went deaf. You thought it in capitals. And you said 'of course' with your mouth, like a man selling a lame horse to a blind woman." {n}She wipes her eyes.{/n} "Nobody in the Abyss has ever lied to me so badly. They wouldn't dare. You lie to me the way other people bring flowers."
"Keep doing it. Never once get better at it."''',
        c("Continue", "socoth")),
    sh("socoth", '''"And his Council?" {n}She waves a hand at your maps, at the war, at everything.{/n} "Socothbenoth wanted my essence for his great joke. He has it; it's in that diamond of yours, with the Nirvana and the Abyss and all the rest. He'll pour it into the Wound for you." {n}A pause.{/n}''',
        c("Continue", "socoth_gone", requires=(SOCOTH_GONE,)),
        c("Continue", "socoth_here", forbids=(SOCOTH_GONE,))),
    sh("socoth_gone", '''"Where is he now, I wonder? Not in his house; I've been there. His wardrobes are all shut." {n}She smiles, very slowly.{/n} "I hope he is somebody's guest, somewhere very dark, for a very long time. I hope his hostess has hideous carpets."''',
        c("Continue", "end")),
    sh("socoth_here", '''"He sent me a present, you know. In my Harem. A silk scarf in exactly my colour, and a card: 'For the leftovers.' Nothing else." {n}Her lip curls.{/n} "I am going to strangle him with it one day. Not soon. He'd enjoy it too much, now."''',
        c("Continue", "end")),
    sh("end", '''{n}She finishes your wine and stands, and stops by the wardrobe with her hand on the frame, as she always does now.{/n}
"You dreamed of the war tables again last night. I sat in the corner and was bored." {n}It is not a complaint.{/n} "I'll be there tonight. Dream of something with wine in it." {n}She opens the door.{/n} "Goodnight, Commander. Sleep. I'll be along."''',
        c("[Close the wardrobe behind her.]")),
], requires=("trickster.ever", COMMITTED), forbids=(THRONE,) + LIVE, delay=72, kind="visit")


# --- One night alone: the arrangement, tested --------------------------------------------------------------------------

ASKED_ALONE = P + "night_alone.asked"
TOOK_NIGHT = P + "night_alone.taken"
GAVE_BACK = P + "night_alone.given_back"
COLD_NIGHT = P + "cost.cold_night"

page(P + "after.night_alone", "One night alone", [
    nar("start", '''{n}You go the way she showed you: into the wardrobe, through the empty Council, through Socothbenoth's purple door and his house of listening closets, out under the black arch in the street.{/n}
{n}The Harem is full tonight. Music, perfume, a hundred demons on the couches, a fight going on quietly in one corner that nobody is watching. The court sees you come in, a Golarian in a travelling coat, and goes silent in waves, from the door to the dais.{/n}''',
        c("Continue", "court")),
    sh("court", '''{n}She is on her throne, in red, with the low light around her. She watches you walk the whole length of the room, between the couches, and she does not help.{/n}
"The Golarian." {n}She says it to the court, in her throne-room voice, bored and carrying.{/n} "The one who argued with me in my own Harem, once. Come to beg a favour, I suppose. They always come back to beg." {n}And in your head, at the same moment, much quieter:{/n} "Play along, clown. They're watching. They have to see you ask."''',
        c('[Kneel at the foot of the dais] "Lady Shamira. I\'ve come for something of mine."', "kneel"),
        c('[Stand] "I came for what you owe me."', "stand")),
    sh("kneel", '''{n}The court sighs, a long delighted sound, like an audience at the good part of a play.{/n}
"How charming. On your knees, in my Harem, in front of everyone." {n}Her face gives nothing. In your head she is laughing so hard she can barely speak.{/n} "They will talk about this for a century. You have made me more powerful in this city tonight than a year of murders would. Get up. No, stay down one more breath. There. Now get up, and follow me."''',
        c("Continue", "private", flags=(ASKED_ALONE,))),
    sh("stand", '''{n}The court draws its breath in, all at once. Nobody speaks to her like that on her own dais. The last one who did it is sitting in the Lower City beside Ziforian, trying to remember his name.{/n}
"Owe you." {n}She rises, slowly, and the light rises with her, and for a moment every demon in the room is afraid.{/n} "Clear the Harem," {n}she says, not loudly, and they go, all of them, fast, without looking back. When the last door closes she sits down on the top step of the dais and puts her face in her hands and laughs.{/n}''',
        c("Continue", "private", flags=(ASKED_ALONE,))),
    sh("private", '''"Well, then." {n}She is sitting on the steps of her throne with her knees up, the way she sat the morning after the game.{/n} "One night alone. I promised you could ask. Ask."
{n}She is not smiling. She touches her own chest, where the coal of you sits, and you can see her know exactly how long it will last.{/n} "Understand what you're asking. If I don't come tonight, this body goes cold by morning. Not dead. Cold. I don't know what cold costs a body that was never anyone. Neither do you."''',
        c('"One night. I want to know what it\'s like again."', "take", flags=(TOOK_NIGHT, COLD_NIGHT)),
        c('"No. I only wanted to hear you offer it."', "offered", flags=(GAVE_BACK,))),
    sh("offered", '''{n}She stares at you. Then something in her face goes very soft and very dangerous at once.{/n}
"You came all the way through Socothbenoth's closets and knelt in front of my court to hear me offer." {n}She shakes her head, slowly.{/n} "You are the stupidest creature in the Abyss, and I have met the whole Abyss." {n}She pulls you down beside her on the step, and puts her forehead against yours, the old place.{/n} "I'll be there tonight. Dream of the kitchen. I like the kitchen."''',
        c("[Stay on the steps with her a while.]")),
    sh("take", '''{n}She is quiet for a while. Then she nods, once, like a merchant accepting a bad price.{/n}
"Go home, then. Sleep. I won't come." {n}Her voice is perfectly level.{/n} "Don't look for me in it. If you look for me, it isn't alone, and you'll have wasted it."''',
        c("Continue", "alone")),
    nar("alone", '''{n}You sleep in your own bed in Drezen, and you dream, and for the first night since the wardrobe floor, nobody comes.{/n}
{n}It is Kenabres. It is always Kenabres. The square, the smoke, the dragon coming down with her wings on fire, and your legs rooted to the stones. Nobody on the fountain. Nobody to tell you the sky is too red. You stand there for the whole of the dream and the dragon falls and falls, as slowly as she always fell, and you find you have been looking at the fountain the entire time.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}She is sitting on the end of your bed when you wake, in the red dress from the Harem, with your blanket round her shoulders. Her lips are grey. Her long hands, when she lifts one to push her hair back, move slowly, like a cold woman's in a winter street, and the fingertips are white.{/n}
{n}She does not come closer. She looks at your face, and reads it, and whatever she finds there makes her close her eyes.{/n}''',
        c("Continue", "read")),
    sh("read", '''"You looked at the fountain." {n}Her voice is hoarse.{/n} "The whole night. You were alone, and you looked at the fountain." {n}She opens her eyes.{/n} "My hands are cold. They'll stay a little cold now, I think, at the tips. I don't mind. I wanted to know if you would miss me." {n}A ragged breath.{/n} "Tonight I'm coming back in. Try and stop me."''',
        c("[Lift the blanket.]")),
], requires=("trickster.ever", COMMITTED, THRONE), forbids=(ASKED_ALONE,) + LIVE, delay=72, kind="visit")


# --- The soft no, kept: one favour, exactly --------------------------------------------------------------------------------

FAVOUR = P + "ally.favour"

page(P + "after.favour", "One favour, exactly", [
    nar("start", '''{n}No wardrobe opens. In your sleep she sits where she always sits now, at the far edge of the dream with her back to you, and says nothing. Instead, one grey morning, there is a folded square of red silk on your map table, weighed down with one of the black glass pins she wore in her hair, and nobody on your staff can say how it got there.{/n}
{n}Written on the silk, in a hand like a row of knives:{/n}''',
        c("Continue", "letter")),
    sh("letter", '''"Commander. You won our game, so I will not ask you anything. I will only pay. I owe you one life, which I cannot pay back, being unable to give you mine. So I will pay it in pieces, as I learn things, and you will get exactly as much as it is worth and not one grain more."
"Here is the first piece. There is a templar of the Ivory Labyrinth in your city wearing the face of a Mendevian quartermaster. I felt him from Alushinyrra; his head is full of mazes and he is very bad at hiding them. He sleeps above the chandler's on the Street of Nails."''',
        c("Continue", "letter2")),
    sh("letter2", '''"You may thank me by not thanking me. You may reply by not replying. If you want to know what I think of you, you already know, because you won, and you only won because you did not want to lose."
{n}There is no signature. There does not need to be. The silk smells of cinnamon.{/n}''',
        c("[Send the watch to the Street of Nails.]", "watch", flags=(FAVOUR,)),
        c("[Burn the silk, and go to the Street of Nails yourself.]", "yourself", flags=(FAVOUR,))),
    nar("watch", '''{n}The watch finds him where she said he would be, in a room above the chandler's with a Mendevian quartermaster's coat hanging on the door and a quartermaster's face on the pillow. When they pull the face off him, there is a goat's skull underneath, and a map of Drezen with every well marked.{/n}
{n}You keep the black glass pin. You are not sure why.{/n}''',
        c("[Put the pin in your coat.]")),
    nar("yourself", '''{n}You go alone, at night, and take the stairs above the chandler's three at a time. He is awake. He is not ready. When it is over there is a goat's skull on the floor where a quartermaster's face was, and a map of Drezen with every well marked, and a smell of cinnamon in the room that was not there when you came in.{/n}
{n}She was watching. Of course she was. She did not say a word.{/n}''',
        c("[Go home.]")),
], requires=("trickster.ever", ALLY), forbids=(FAVOUR, CLOSED), delay=72)


# --- The night before the rift (Chapter 6): her last word before Threshold --------------------------------------------

EVE = P + "eve"

page(P + "after.eve", "The night before the rift", [
    nar("start", '''{n}Tomorrow you go down into the Wound. The camp knows it; nobody is singing. You lie in the dark with your eyes shut, and she is already there at the edge of it, as always, and then there is a voice.{/n}''',
        c("Continue", "voice")),
    sh("voice", WHISPER + '''"I can feel the rift from here. Even from my throne. It's pulling on something in you, like a hook in a fish." {n}Her voice is lower than usual, as if the Harem were full of sleepers she does not want to wake.{/n} "I have walked through your whole head. I know what that hook is. Areelu put it there, the night she opened you up, and it has been drawing you towards that hole in the world ever since."''',
        c("Continue", "tomorrow")),
    sh("tomorrow", '''"Tomorrow I won't be there. I can't be; I would burn up at the edge of that thing, what's left of me." {n}The voice goes very still.{/n} "I will be on my throne with the court sent away, with tonight's coal of you in me, and if you go into the Wound and don't come out, it will go cold by morning, and there will be no hearth to go back to, and I will know."''',
        c("Continue", "committed", requires=(COMMITTED,)),
        c("Continue", "ally", requires=(ALLY,), forbids=(COMMITTED,)),
        c("Continue", "plain", forbids=(COMMITTED, ALLY))),
    sh("committed", '''"So come out." {n}It is an order. It is the throne-room voice, and under it something that is not.{/n} "Come out of the hole, clown. I have already died of one trick this year. I will not lose you to a hole in the ground. It would be a very poor joke, and you are not allowed to tell poor jokes. Not to me."''',
        c("[Think of her, loudly, and go to sleep.]", flags=(EVE,))),
    sh("ally", '''"You won our game. I said I would never ask you anything again, and I won't." {n}A pause.{/n} "This isn't asking. This is telling. Come back out of the hole, Golarian. I owe you a life, and I pay my debts, and I can't pay a dead man."''',
        c("[Think of her, loudly, and go to sleep.]", flags=(EVE,))),
    sh("plain", '''"We never finished anything, you and I. A murder, a body, a head with two heartbeats in it." {n}The voice goes dry.{/n} "Come back out of the Wound and finish something. I'm told it's what mortals do."''',
        c("[Think of her, loudly, and go to sleep.]", flags=(EVE,))),
], requires=("trickster.ever", EMBODIED), forbids=(EVE,) + LIVE, delay=0, chapters=(6,))


def integrate(payload):
    """Nothing to bind: the native keys read here (Nocticula's hiding, her brother's plot) bind on demand."""
