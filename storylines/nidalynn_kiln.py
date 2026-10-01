"""Nidalynn, from the hearth to the hatching: the egg, the kiln and the confession (nidalynn_trickster holds the device).

Every beat engages her canon: sincerity and kindness as a silver dragon's first law, and the body fed before the soul
(DragonsKenabres Cue_0015); deeds over words (Cue_0009); the widow's part and what it was for (Cue_0016); the Windstep,
Reudger the White and his riddle about Golarion's salt (NidalynnQuest1 Cue_0012, Cue_0017, Cue_0018, Cue_0023);
"Warriors are not the only ones worth remembering" (Cue_0024); the metallic dragons who wanted Devarra's clutch raised
well (Cue_0058). The riddle is told as a memory, never as a test.

Pivotal choices, and nowhere else: what the Commander says at the kiln when the crowd comes with torches (the confession,
the lie, or the hatchling given to the fire), and whose the hatchling is afterwards (the claim given up, or kept).
"""
from story_format import c, n, p, scene
from storylines.nidalynn_trickster import (
    CHOSEN_UNIT, CLAIMED, CLERK, FORM, CLOSED, CONFESSED, DV_BILL, DV_HUNTING, DV_RETURNED, FED_DEMONS, FED_GOATS, FED_RATS,
    GIVEN_UP, GOAT_CORRECTED, GOAT_STANDS, GOLEM, HAND, HAND_SET, HATCHED, KILN, KILN_AGREED, LEFT_WITH_IT, LIE_KEPT, LIED, MET, NAME_NONE, NAME_PEBBLE,
    NAME_SOOT, P, PALMS, REL, RENOUNCED, REVEALED, ROCK_JOKE, TOLD_EGG, TOLD_NOTHING, TOLD_ROCK, TORC_BOUGHT, TORC_LEFT,
    TORC_LIFTED, VAULT, WHY_COULD, WHY_DUNNO, WHY_SMALL, WHY_USE, nar, nd)
from storylines.nidalynn_trickster import QUARTERMASTER, SLATE, STORYTELLER_SUPPLIES, STRAW   # PP10: the egg the druids left in the straw
from storylines.nidalynn_trickster import steps as _steps, visit as _visit

SCENES = []


def steps(*args, **kw):
    _steps(*args, into=SCENES, **kw)


def visit(*args, **kw):
    _visit(*args, into=SCENES, **kw)


CLAIM_KEPT = P + "claim_kept"
TORCS = P + "steps.torcs"
BELLY = P + "steps.belly"
FEEDING = P + "kiln.feeding"
ABYSS_LETTER = P + "letter.from_the_kiln"
WHOSE = P + "kiln.whose"
RIDDLE_SNOW = P + "riddle.snow"
RIDDLE_FOLK = P + "riddle.common_folk"
RIDDLE_NONE = P + "riddle.unanswered"
SPEAR_PROVOST = P + "spear.provost"
SPEAR_FREED = P + "spear.freed"
SPEAR_SEEN = P + "spear.seen"
DRUIDS_DEFENDED = P + "druids.defended"
DRUIDS_REGRETTED = P + "druids.regretted"
ULBRIG_MET = P + "ulbrig_met"
GOAT_PAID = P + "goat.paid"
GOAT_ASKED = P + "goat.asked"
GOAT_WOLVES = P + "goat.wolves"
WAKE_SAID = P + "wake.name_said"
CHAPLAIN = P + "chaplain_prayed"


# --- 1. The hearth (she comes to the Commander's quarters): the egg, the reveal, the kiln ---------------------------------

visit(P + "hearth.listening", "Nobody's widow", [
    nar("door", '''{n}The sergeant with the squint lets her up the stair at the second bell and calls her "mother", and she thanks him, and pats his arm, and does not look back to see him blush. She comes into your rooms without knocking, as a woman comes into a sickroom.{/n}
{n}She does not look at you, or at the maps, or at anything you own. She goes straight to the hearth, kneels in front of it with a grunt for the belly, wraps both hands in the ends of her shawl, and reaches into the fire.{/n}''',
        c("Continue", "listen")),
    nar("listen", '''{n}She lifts the grey thing out of the coals and holds it against her ear, the way a child holds a shell to hear the sea. Her eyes close.{/n}
{n}Then she begins to hum. It is not a tune; it goes too low for a tune, and it does not end where a breath should end. The cup on your mantel starts to buzz against the stone. The window-glass answers it.{/n}
{n}Inside the egg, something knocks. Once. Twice. Then again, faster, like a fist on a door.{/n}''',
        c("Continue", "cold")),
    nd("cold", '''{n}She opens her eyes.{/n} "It's alone, and it's cold, and it's stopped expecting anybody to turn it." {n}She lays it back in the coals, very carefully, and rakes the embers up around it with your poker.{/n} "It's the smallest, and it's had the worst of the heat; you can feel it in the shell. Runts often do."
"Your hearth is a good hearth, Commander. It isn't a dragon. By the feel of it, it won't last the week."''',
        c('"And you know that how, widow?"', "how"),
        c('"How do you know what it thinks?"', "how")),
    nd("how", '''{n}She sits back on her heels, and puts one hand on the small of her back, and sighs the long sigh of a woman who has been standing on a market step all day.{/n} "Oh, very well. It's late, and your chairs look comfortable, and I did promise I'd tell you in your own house."
"I'm not a widow. I've never been married; nobody ever asked me in a way I liked. I'm not carrying." {n}She pats the belly, almost fondly.{/n} "And I'm not, if we're being honest about it, a woman."''',
        c("Continue", "sleeve")),
    nar("sleeve", '''{n}She pushes up the sleeve of her dress to the elbow and holds out her forearm to the firelight, and you watch it change.{/n}
{n}It happens the way frost comes on a window: from the wrist upward, fine and fast. Scales, silver and small as the links of a good hauberk, laid over one another so neatly that the fire runs along them like water. Her nails darken and lengthen and curve. Her breath, when she lets it out, is cold. The ash on the hearthstone in front of her grows a little fern of frost.{/n}
{n}Then she shakes her wrist, the way you shake water off a hand, and it is a woman's arm again, a little red at the knuckles from washing.{/n}''',
        c("Continue", "name")),
    nd("name", '''"Nidalynn." {n}She pulls the sleeve back down.{/n} "Of the silver. I'd bow, but there's the belly, and I'd never get up again." {n}She looks at you with those pale, grey, no-brown eyes, perfectly steady.{/n} "There. Now we're both liars who've told the truth once tonight. It's a good start. Most people never manage it."''',
        c('"A dragon. On my hearthstone."', "dragon", flags=(REVEALED,)),
        c('"I knew there was something wrong with the belly."', "belly", flags=(REVEALED,)),
        c('"You\'re the second-best liar in this room."', "second", flags=(REVEALED,))),
    nd("dragon", '''"On your hearthstone, in your good chair, drinking your wine, presently." {n}She is already reaching for the jug.{/n} "Don't look like that. We've been walking among you since before your crusades had names. Somebody has to keep an eye on you. You're so short-lived; you get into such trouble."''',
        c("Continue", "why", forbids=(VAULT, STRAW)),
        c("Continue", "why_vault", requires=(VAULT,)),
        c("Continue", "why_straw", requires=(STRAW,))),
    nd("belly", '''"Did you." {n}She looks down at it with something like pride.{/n} "It's a good belly. It's got me through three sieges and a plague year. Soldiers step round it, and the women feed it, and nobody asks it hard questions." {n}She pours herself your wine.{/n} "Tell me what was wrong with it, so I can fix it. No; don't. You'll only say it's too round, and it isn't."''',
        c("Continue", "why", forbids=(VAULT, STRAW)),
        c("Continue", "why_vault", requires=(VAULT,)),
        c("Continue", "why_straw", requires=(STRAW,))),
    nd("second", '''{n}She laughs, a real laugh, big and warm and a little too loud for the room, and it fills your quarters and does not quite fit in them.{/n} "Second! You've got a Sanctum egg in your fire and the whole citadel calling it a rock, and you say second." {n}She wipes her eyes.{/n} "Well. Maybe. I've had longer to practise."''',
        c("Continue", "why", forbids=(VAULT, STRAW)),
        c("Continue", "why_vault", requires=(VAULT,)),
        c("Continue", "why_straw", requires=(STRAW,))),
    nd("why", '''{n}She settles into your chair, with a hand under the belly, pours herself a cup of your wine, and turns it without drinking.{/n} "Now you. I've told you what I am. You tell me why you did it."
"You stood in that chamber with Xanthir Vang's golems over you, and you went in under their fists for the smallest egg of a dragon who tried to burn your army out of the sky. Why?"''',
        c('"It was the smallest. The golems had already given up on it."', "small", flags=(WHY_SMALL,)),
        c('"Because they were going to smash it, and I could stop them."', "could", flags=(WHY_COULD,)),
        c('"A dragon on the crusade\'s side could be useful."', "useful", flags=(WHY_USE,)),
        c('"I don\'t know. I still don\'t."', "dunno", flags=(WHY_DUNNO,))),
    nd("why_vault", '''{n}She settles into your chair, with a hand under the belly, pours herself a cup of your wine, and turns it without drinking.{/n} "Now you. I've told you what I am. You tell me why you did it."
"The clutch was crated in your own vault. The druids wanted it, and your cooks wanted it, and you'd only to wait and let somebody else decide. Instead you went down at night with a coal bucket, past your own clerk, and carried the smallest egg of a dragon who tried to burn your army out of the sky up four flights in your bare hands. Why?"''',
        c('"It was the smallest. Nobody was going to miss it."', "small", flags=(WHY_SMALL,)),
        c('"Because the cooks or the druids were going to have it, and I could stop them."', "could", flags=(WHY_COULD,)),
        c('"A dragon on the crusade\'s side could be useful."', "useful", flags=(WHY_USE,)),
        c('"I don\'t know. I still don\'t."', "dunno", flags=(WHY_DUNNO,))),
    # PP10: the straw's Commander kept what four "druids" gave up for dead, and signed it off the stores in chalk.
    nd("why_straw", '''{n}She settles into your chair, with a hand under the belly, pours herself a cup of your wine, and turns it without drinking.{/n} "Now you. I've told you what I am. You tell me why you did it."
"We let our eldest call it dead, and I should have stayed with it. Your quartermaster wanted it out with the bedding, and every soldier in this city would have cheered the cart. You had only to nod. Instead you signed a lie on your own stores' slate, and carried the smallest egg of a dragon who tried to burn your army out of the sky up to your own fire, cold, with nothing in it anybody could hear. Why?"''',
        c('"It was the smallest. Nobody was going to miss it."', "small", flags=(WHY_SMALL,)),
        c('"Because everybody said it was finished, and I could still try."', "could", flags=(WHY_COULD,)),
        c('"A dragon on the crusade\'s side could be useful."', "useful", flags=(WHY_USE,)),
        c('"I don\'t know. I still don\'t."', "dunno", flags=(WHY_DUNNO,))),
    nd("small", '''"Yes." {n}She nods slowly, as though you have handed her something she was expecting and is glad to have.{/n} "My grandfather used to say the runt of any litter is the one that remembers who fed it. He was talking about foals. He was usually right about foals."''',
        c("Continue", "hand_check")),
    nd("could", '''"Because you could." {n}She considers it, the way she might consider a bolt of cloth.{/n} "That's a trickster's answer. I don't like it as much as I'd like to. But it's honest, and most people who do a good thing say it was for a better reason than that, and they're lying."''',
        c("Continue", "hand_check")),
    nd("useful", '''{n}She sets the wine down.{/n} "Useful." {n}She says it without heat.{/n} "Well, you're a Commander. I suppose it's your trade to see what things are useful for." {n}Her eyes go to the hearth.{/n} "It won't be useful. It'll be hungry and bad-tempered and it'll bite. Most children are useful the way a fire in winter is useful: you don't get to choose what it burns. We'll talk about that again, you and I."''',
        c("Continue", "hand_check")),
    nd("dunno", '''"No. You don't." {n}She seems, of all things, pleased.{/n} "Good. The ones with a fine speech ready usually wrote it before they did the kind thing. You haven't one. I like that better." {n}She lifts the cup to you, at last, and drinks.{/n}''',
        c("Continue", "hand_check")),
    nar("hand_check", '''{n}She puts the cup down and holds out her hand, palm up, and waits.{/n}''',
        c("Continue", "hand", requires=(HAND,)),
        c("Continue", "palms", requires=(PALMS,)),
        c("Continue", "kiln", forbids=(HAND, PALMS))),
    nd("hand", '''"Give me that hand. The one you've been hiding in your sleeve since I came in." {n}When you do, she turns it over in both of hers and clicks her tongue.{/n} "Who set this? A crusade chirurgeon, with a stick and a prayer? It'll knit crooked, and you'll never close it on a sword again."
{n}She takes the two broken fingers between her thumbs. You are expecting it to hurt. It hurts more than you are expecting. Something grates, and something else clicks into a place it had forgotten, and she is binding them to a spill of kindling from your own wood-basket before you have finished swearing.{/n}
"There. The Windstep had a bonesetter for the horses, and he taught me on the foals. You've better bones than a foal. Worse manners."''',
        c("Continue", "kiln", flags=(HAND_SET,))),
    nd("palms", '''"Give me those hands. Both of them." {n}She turns them palm up to the firelight and looks at the blisters for a while without saying anything.{/n} "You carried it up the stairs against your chest. Didn't you. The whole way, with the skin coming off." {n}She takes a little pot out of her mending basket, something that smells of goose-fat and yarrow, and works it into your palms with her thumbs, slowly, not gently.{/n} "Idiot. You should have wrapped it in wet sacking. Any shepherd's child could have told you. The Windstep children carried coals from camp to camp in wet sacking, in their bare hands, and sang while they did it."''',
        c("Continue", "kiln", flags=(HAND_SET,))),
    nd("kiln", '''"Now. It's cold, and your fire isn't enough, and I'm not going to sit on it in your quarters; your steward would have a seizure." {n}She thinks.{/n} "There's an old lime-kiln under the east wall, below the tanners' stair. The crusade hasn't used it since they finished the new curtain. The bricks are sound. If I fire it right, the heart of it gets as hot as a dragon's belly and stays hot all night."
"Tomorrow night. Bring the egg. Wrap it in your coat, not your arms." {n}She gets up, belly first, with a hand on the chair.{/n} "And have your cook make you a proper supper before you come. I won't have you fainting on my kiln."''',
        c('"Tomorrow night."', flags=(KILN_AGREED,)),
        c('"Why are you helping it? It\'s a woundwyrm. It\'s the Wound\'s get."', "wound")),
    nd("wound", '''{n}At the door she stops.{/n} "It's an egg. Eggs aren't anything yet. That's the whole point of them."
"What hatches is what it's fed, and what it's taught, and who it's afraid of. Its mother was raised in the Wound and chained to golems. I'll try to do better by it." {n}She shrugs.{/n} "It may grow up wicked anyway. They do, sometimes. So do children. We still don't leave them in the snow."''',
        c('"Tomorrow night, then."', flags=(KILN_AGREED,))),
], requires=(MET,), forbids=(KILN_AGREED,), delay=24)


# --- 2. The kiln (the first night): moving the egg, and what she remembers ---------------------------------------------

visit(P + "kiln.fire", "The lime-kiln", [
    nar("walk", '''{n}The egg goes down through the lower town inside your coat, and you go down with it, past the tanners' stair and the shuttered stalls, with the snow she promised coming in slantwise off the Worldwound. It is heavier than it was. It knocks, now and then, against your ribs.{/n}
{n}The kiln is an old stone bottle as tall as two men, built into the foot of the east wall, with a mouth at the bottom and a chimney at the top where the snow comes in. She has been at it since noon. The heart of it is white. You can feel it on your face from the lane.{/n}''',
        c("Continue", "set")),
    nd("set", '''"Give it here." {n}Her sleeves are rolled to the shoulder and she has pinned the widow's skirts up out of the way, and her forearms are sooty to the elbow.{/n} "Mind the step. Mind the lip. Mind my belly, for pity's sake, I'm very attached to it."
{n}She takes the egg in her shawl and lays it on a baker's peel as long as a pike, and runs it into the kiln's mouth to the bricks at the very back, with her face turned from the heat. When she straightens her hair is steaming and she is laughing.{/n} "There. Now it's somewhere it can believe in."''',
        c("Continue", "night")),
    nar("night", '''{n}The rest of the night is fire. The kiln eats wood the way a siege eats men, and it is the two of you who feed it: splitting, carrying, stoking, sitting back on a sack of lime against the wall with your eyes stinging, then up again.{/n}
{n}She works the way old farm women work, without hurry and without ever stopping, and she talks the whole time. Not to you, at first. To the kiln, to the wood, to the egg: "Come on, then. There's a good fire. There's a good, hot fire for a little one."{/n}''',
        c("Continue", "sit")),
    nd("sit", '''{n}Near midnight she sits down beside you on the lime sack, close, because it is the only dry seat, and hands you half a loaf out of her basket and a knife.{/n} "Eat. You've been feeding that fire for three hours and you haven't fed yourself once. A body is not a kiln, Commander. It needs more than wood."''',
        c('"Tell me about the Windstep."', "windstep"),
        c('"How old are you?"', "old"),
        c("[Eat, and say nothing.]", "quiet")),
    nd("quiet", '''{n}She watches you eat, and approves of it, and tells you anyway, the way people tell things by a fire at midnight, to fill the dark.{/n}''',
        c("Continue", "windstep")),
    nd("old", '''"Old enough that it's rude to ask." {n}She takes the knife back and cuts herself a piece of the bread.{/n} "Old enough that I was a girl at a fire in Sarkoris before the Wound. Old enough that it doesn't feel very long ago." {n}She chews.{/n} "Not as old as all that. Dragons live a long time. I'm not halfway."''',
        c("Continue", "windstep")),
    nd("windstep", '''"The Windstep were horse-folk, on the grass, north of the Moutray." {n}She stares into the kiln's mouth, and something in her face goes a long way off.{/n} "Mares, and mare's milk, and skies that went on for ever. The brand was a mare galloping under the stars."
"Reudger the White was their cheesemaker. Not a lord, not a warrior. I came to his fire when I was young and still clumsy in this shape, and he never once asked me where from. I called him grandfather. Half the grass did."''',
        c("Continue", "reudger")),
    nd("reudger", '''"It was his habit, not the clan's: a heel of bread with salt on it for anyone who came to his fire. 'There. Now you're of my fire, and I'll hear no more about where you're from.'" {n}She almost smiles.{/n} "He'd sit on the step of his summer house with his pipe, watching the mares, and when I sat down by him he'd pass me a piece of cheese and ask me a riddle."''',
        c("Continue", "riddle")),
    nd("riddle", '''"Always the same riddle. 'You need salt to make cheese, girl. It keeps it and gives it its taste. So what's Golarion's salt? What lets us live here, and makes it worth the living?'" {n}She says it in a deep, slow voice, a man's voice with a pipe in it, and then she laughs at herself.{/n}
"And I'd say 'snow', every time, because I loved the snow. And every time he'd laugh at me and say snow was as white as salt but half the world had never seen it. Year after year."''',
        c('"And the answer?"', "answer"),
        c('"The common folk."', "folk", flags=(RIDDLE_FOLK,)),
        c('"Snow. You were right."', "snow", flags=(RIDDLE_SNOW,))),
    nd("answer", '''"The common folk." {n}She says it simply, as a thing she has known a long time and only lately understood.{/n} "Farmers and weavers and cheesemakers and woodcutters. Wars come and go. The ploughing doesn't. I didn't understand it until they were all dead. You don't, usually."''',
        c("Continue", "remember", flags=(RIDDLE_NONE,))),
    nd("folk", '''{n}She turns her head and looks at you, surprised, and then not surprised at all.{/n} "Yes. Of course you'd know it. You've got a city of them behind that wall and you're the one feeding them." {n}She looks back at the fire.{/n} "I didn't understand it until they were all dead. You don't, usually."''',
        c("Continue", "remember")),
    nd("snow", '''{n}She laughs, delighted, loud enough that the snow on the kiln's lip shivers.{/n} "Year after year I said that, and nobody ever agreed with me. Not once." {n}She wipes her eyes with a sooty wrist and leaves a streak.{/n} "It's wrong. The answer's the common folk. Farmers and weavers and cheesemakers; wars come and go and the ploughing doesn't. But I've always liked the snow better, and I'll not be told I'm wrong about it twice in one night."''',
        c("Continue", "remember")),
    nd("remember", '''"When the Wound opened, I was a long way north. By the time I came back there was nothing on the grass but ash, and things walking in the ash that should not walk." {n}The kiln roars softly.{/n} "I couldn't even find his grave. None of their graves. So I sit on steps in refugee quarters and listen to them sell their grandmothers' torcs, and I remember the names on the brands. Somebody has to. Warriors are not the only ones worth remembering."''',
        c('"You\'re still grieving them."', "grieve"),
        c("[Feed the kiln.]", "feed")),
    nd("grieve", '''"A hundred years isn't very long, for grieving." {n}She takes a log from the pile and hands it to you, as though that were the natural end of the sentence.{/n} "Feed the fire. I'll grieve, you stoke, and we'll both be useful."''',
        c("Continue", "feed")),
    nar("feed", '''{n}Toward morning the snow stops. The kiln's heart has gone from white to the deep orange of a forge, and it ticks as it settles. She puts her ear to the brick of its flank, the way she put her ear to the egg, and listens.{/n}''',
        c("Continue", "knocking")),
    nd("knocking", '''"Listen." {n}She takes your wrist and puts your palm flat against the hot stone beside her own. Under it, very faint, through two feet of brick, something is knocking. Not the way it knocked in your hearth. Steadily. Like a heart.{/n}
"It believes us." {n}She lets go of your wrist and sits back on her heels, and wipes her face with a sooty sleeve.{/n} "Go home and sleep, Commander. I'll keep it tonight. Come back when it's ready. You'll know. The whole lower town will know."''',
        c("[Go home and sleep.]", flags=(KILN,))),
], requires=(KILN_AGREED,), forbids=(KILN,), delay=24)


# --- 3. The torcs (optional, the widow's step): what Sarkoris sells for bread ------------------------------------------

steps(TORCS, "What they carried out", '"You were watching the jeweller again."', [
    nd("start", '''"I'm always watching the jeweller." {n}She does not take her eyes off the stall across the square.{/n} "He buys Sarkorian torcs by the weight of the copper. He sells them to crusaders from Mendev by the weight of the story. It's very good business. Watch."
{n}A Kellid girl of perhaps fourteen is at the counter with a copper torc in both hands, the kind that is made to be worn for a lifetime and never taken off. The jeweller weighs it on his little scale and names a price. The girl's face does not move. She has been told prices before.{/n}''',
        c("Continue", "brand")),
    nd("brand", '''"See the hare, on the terminal? Running, with its ears back." {n}Her voice drops.{/n} "That's the Hollowmoor mark. They were goat-herders on the fells south of the Windstep. I knew her great-great-grandmother. She was a terrible singer and she made the best goat-butter on the grass." {n}The girl has taken the jeweller's coins. The torc is going into a tray with a dozen others.{/n} "That's the last Hollowmoor torc in the world, most like, and it's going to a Mendevian knight who'll tell his friends he took it off a dead cultist."''',
        c('[Cross the square and buy it back at his price, and give it to the girl.]', "bought", flags=(TORC_BOUGHT,), crusade=("Finances", -50)),
        c('[Trickery: lean on the jeweller\'s counter, and lift the torc off the tray while he\'s counting]',
          check=dict(Skill="SkillThievery", DC=20, Success="lifted", Failure="caught", CommanderOnly=True)),
        c('"It was hers to sell."', "left", flags=(TORC_LEFT,))),
    nar("bought", '''{n}The jeweller is very surprised to be asked for it back, and more surprised when you pay the price he names without a word of haggling, and most surprised of all when you walk the torc across the square and hold it out to the girl, who looks at it, and at you, and at the widow on the step behind you, and does not take it until the widow nods.{/n}''',
        c("Continue", "after_bought")),
    nd("after_bought", '''"She'll sell it again next winter," {n}Nidalynn says, when you sit back down.{/n} "When she's hungry enough. You know that." {n}She nods to you, once, the way she would to a horse that has done well.{/n} "But she'll know somebody bought it back once. That's not nothing. That's a story she'll tell her own children, and she'll get it wrong, and it'll be better for it."''',
        c("[Stay on the step a while.]", "end")),
    nar("lifted", '''{n}It is easier than it should be. The jeweller is counting silver and talking about the weather, and his tray is at your elbow, and then it is at your elbow with one torc fewer. You walk across the square with a hare running in your sleeve and drop it into the girl's lap as you pass, and do not stop.{/n}
{n}Behind you, the jeweller goes on counting.{/n}''',
        c("Continue", "after_lifted", flags=(TORC_LIFTED,))),
    nd("after_lifted", '''{n}When you sit back down on the step she is looking at you with an expression you have not seen on her before, somewhere between a scolding and a laugh, and neither one quite winning.{/n} "You stole it."
"From a thief, for a child, in front of a silver dragon." {n}She shakes her head slowly.{/n} "I ought to march you back over there and make you pay him. I'm not going to. I want you to know I thought about it, and I want you to know it was close."''',
        c("[Stay on the step a while.]", "end")),
    nar("caught", '''{n}The jeweller is a jeweller. His hand comes down on the tray a heartbeat before yours does, and he looks up at you, at the Commander of the crusade with a hand in his tray, and a great many expressions go across his face and settle on a very polite one.{/n} "Commander. A fine piece. For you, a special price."''',
        c('[Pay the special price, and give it to the girl anyway.]', "bought", flags=(TORC_BOUGHT,), crusade=("Finances", -100)),
        c('"Keep it."', "left", flags=(TORC_LEFT,))),
    nd("left", '''"Yes. It was." {n}She does not argue.{/n} "She sold it to eat. That's her right, and it's better sense than a lot of people in this city have." {n}She watches the torc go into the jeweller's back room.{/n} "I'll remember it for her. That's what I'm for. You go and win your war, Commander; that's what you're for. Somebody has to do both."''',
        c("[Stay on the step a while.]", "end")),
    nar("end", '''{n}You sit on the step with her until the light goes, and she tells you, one by one, whose torc is whose in the jeweller's tray, clan by clan, mark by mark, until the jeweller closes his shutters with a bang as if he could hear her.{/n}''',
        c("[Say goodnight.]")),
], requires=(MET,), forbids=(TORCS,), delay=24, optional=True)


# --- 4. The belly (optional, the widow's step, after the kiln): what the part is for ------------------------------------

steps(BELLY, "The widow's part", '"Your belly hasn\'t grown."', [
    nd("start", '''{n}She looks down at it, and then up at you, with enormous dignity.{/n} "It's a very good belly. It's the same size it was in Kenabres four years ago, and the same size it was in Nerosyan before that, and it'll be the same size when you're old. It's a belly of great constancy."
{n}Then she laughs, low, so the women on the next step don't hear.{/n} "You noticed. Good. Nobody else in this city has, and I've been sitting here a good while."''',
        c('"Why a pregnant widow?"', "why"),
        c('"Is it a lie, if it doesn\'t hurt anyone?"', "lie")),
    nd("why", '''"Because people are kind to a woman carrying." {n}She says it without a trace of irony.{/n} "Kinder than they are to anyone else. Soldiers step round me. Old women sit with me and feed me and tell me what their sons are doing. Children bring me things. A widow on her own is someone to be cheated; a widow with a child coming is someone to be looked after."
"And I sit here and I'm looked after, and I hear everything." {n}She nods at the square.{/n} "I know which of your sergeants is selling the grain ration. I know whose boy is sick. I know more about this city than your spies do, Commander, and it costs me nothing but a cushion."''',
        c("Continue", "test")),
    nd("lie", '''"It's a lie." {n}She doesn't hesitate.{/n} "I don't like it. I've never liked it. Silver dragons are supposed to be sincere, and I am; I'm sincere about the soup and the gossip and the children." {n}She smooths the dress over the belly.{/n} "But a costume isn't a lie in the way that matters. It's a question. I dress up as something people ought to be kind to, and I watch who is."''',
        c("Continue", "test")),
    nd("test", '''"People think a foolish request from a pregnant woman is beneath them. The ones who help anyway, without laughing, without asking what's in it for them, those are the ones worth knowing." {n}She glances sideways at you.{/n} "You never laughed at the widow. You sat down on the step. You'd be surprised how rare that is."''',
        c('"And when you don\'t need anyone to be kind to you?"', "when"),
        c('"I sat down because you were watching my door."', "watching")),
    nd("watching", '''"And you could have sent a sergeant." {n}She pats your hand.{/n} "Don't spoil it. Let an old woman think well of you."''',
        c("Continue", "when")),
    nd("when", '''{n}She is quiet a little while.{/n} "Then I take it off. And I'm myself, and people look at me as I am." {n}Her fingers stop moving on the dress.{/n} "I don't do that often. It's harder than you'd think. The belly's a shield, Commander. It keeps hands off. Nobody reaches for a widow with a child coming."
"When I want to be looked at as myself, you'll know. You won't have to ask." {n}She says it lightly, and does not look at you while she says it, and her ears have gone faintly pink, which on a woman of her apparent years is a remarkable thing to see.{/n}''',
        c("[Leave it there.]")),
], requires=(KILN,), forbids=(BELLY, HATCHED), delay=24, optional=True)


# --- 5. The hatching (the kiln): the crowd, and what the Commander says to it (pivotal) --------------------------------

visit(P + "kiln.hatching", "What came out of the rock", [
    nar("boy", '''{n}A refugee boy hammers on the citadel door at dusk, and will not give his message to the guard, and will not give it to your steward. He gives it to you with his hands on his knees and no breath left:{/n} "The widow says. Come now. She says you'll know."
{n}You know. You can hear it from the citadel steps: a sound out of the lower town like a kettle left on the fire too long, rising and rising and not stopping, and under it every dog in Drezen barking at once.{/n}''',
        c("Continue", "kiln")),
    nar("kiln", '''{n}The kiln's mouth is open and the heat comes out of it in a wall. She is on her knees at the mouth, in the glare, with her sleeves rolled and her shawl over her hands, and in front of her on the white bricks the egg is breaking.{/n}
{n}Not the way a hen's egg breaks. It splits along a seam, like a log in a fire, and the grime it was hidden in flakes off in scabs, and what pushes out through the split is a claw the size of your thumb, black-red, wet, and furious.{/n}''',
        c("Continue", "out")),
    nar("out", '''{n}Then a snout. Then the whole of it, all at once, the way a thing is born that has been waiting too long: a newborn dragon the size of a cat, slick and red-black and steaming, with a pale seam down its spine like a scar where the Wound's taint touched it in the egg, and a mouth that is almost all teeth.{/n}
{n}It screams. That is the sound the dogs were barking at.{/n}
{n}Nidalynn laughs, delighted, with tears running down her sooty face, and holds out her shawled hand to it, and it bites her.{/n}''',
        c("Continue", "bite")),
    nd("bite", '''"Oh, you little..." {n}She does not pull her hand away. The hatchling hangs off the shawl by its teeth, growling, its tail lashing.{/n} "There. There. Bite, then. Bite, you've every right, you've been in the dark without your mother." {n}She looks back at you over her shoulder, blazing, laughing, ridiculous with soot.{/n} "It's a girl. Look at her. Look at the temper on her. Her mother all over."''',
        c("Continue", "torches")),
    nar("torches", '''{n}You do not get long to look.{/n}
{n}A scream like that does not stay in a kiln. By the time the hatchling has let go of the shawl there are people in the lane: refugees from the quarter, soldiers off the east wall with their spears, a chaplain of Iomedae with a torch held up and his mouth set. More are coming down the tanners' stair. Somebody has seen what is on the bricks.{/n}
{n}"Woundwyrm," a soldier says, and the word goes back through the lane faster than a man could run it.{/n}''',
        c("Continue", "crowd")),
    nar("crowd", '''{n}The sergeant with the squint pushes to the front and stands there, spear grounded, looking from the kiln to you, very unhappy.{/n} "Commander." {n}He wets his lips.{/n} "They're saying it came out of your rock."
{n}Behind him a woman in a Kenabres shawl says, not loudly, that a woundwyrm burned her husband's wagon on the Kenabres road with him in it. A soldier with a burn-scarred jaw says the mother came down on his company at the ford. The chaplain says that he has burned Wound-spawn before and will burn this, and the torch in his fist says he means now.{/n}''',
        c("Continue", "clerk", requires=(CLERK,)),
        c("Continue", "her", forbids=(CLERK, QUARTERMASTER)),
        c("Continue", "quartermaster", requires=(QUARTERMASTER,))),
    nar("quartermaster", '''{n}And at the back, still in his stores apron, the quartermaster is telling anyone who will listen that the druids left that egg in his straw for dead, and the Commander said it would be buried, and signed it off his slate as disposed of; and that he knew it for a lie when he chalked it, and chalked it anyway, and he'll not pretend otherwise now.{/n}''',
        c("Continue", "her")),
    nar("clerk", '''{n}And at the back, a young man with ink on his cuffs, the vault clerk, is saying to anyone who will listen that he saw the Commander in the vault at night with a bucket of coal, and that he counted eleven and wrote twelve, and that he has been sick about it ever since.{/n}''',
        c("Continue", "her")),
    nar("her", '''{n}Nidalynn has got to her feet. She has the hatchling bundled against her, under the shawl, over the swell of the widow's belly, and it is still growling. She stands in the kiln's mouth with the heat at her back, between the fire and the torches, and she does not say anything.{/n}
{n}She is looking at you. Not pleading. Waiting. Whatever is said to this lane tonight, she is not going to be the one to say it.{/n}''',
        c('[Tell them the truth] "It did. I took it out of the Ivory Sanctum from under the golems, and brought it into this city in my pack, and called it a rock. I lied to every one of you. It\'s mine to answer for."',
          "confess", flags=(CONFESSED,), crusade=("Favors", -100), forbids=(VAULT, STRAW)),
        c('[Lie] "Nonsense. It came down out of the hills in the snow. I\'ll have it caged and sent north."', "lied", flags=(LIED,)),
        c('[Give it to them] "Then burn it."', "given", flags=(GIVEN_UP, CLOSED)),
        c('[Tell them the truth] "It did. I took it out of the citadel vault in a coal bucket, past my own clerk, and carried it up the stairs in my hands, and called it a rock. I lied to every one of you. It\'s mine to answer for."',
          "confess_vault", flags=(CONFESSED,), crusade=("Favors", -100), requires=(VAULT,)),
        # PP10: the egg the druids left in the straw.
        c('[Tell them the truth] "It did. The druids left it in my vault for dead, and I signed it off the stores\' slate as disposed of, and carried it up to my own fire, and called it a rock. I lied to every one of you. It\'s mine to answer for."',
          "confess_straw", flags=(CONFESSED,), crusade=("Favors", -100), requires=(SLATE,))),
    nar("confess_straw", '''{n}The lane goes quiet in a way that is worse than shouting.{/n}
{n}You tell them the rest of it, because once you have started there is no sense stopping. The druids and their handcart. The twelfth egg on the straw heap, cold, that four of them gave up for dead. The slate, and the lie on it with your mark beside it. The hearth. The "rock". You tell them your steward did not know, and the sergeant did not know, and the widow is a widow who knows eggs. You tell them that if it ever burns a wagon or a barn or a man, they are to bring the bill to the citadel, and it will be paid, by you, in whatever coin is owed.{/n}''',
        c("Continue", "chaplain")),
    nar("confess_vault", '''{n}The lane goes quiet in a way that is worse than shouting.{/n}
{n}You tell them the rest of it, because once you have started there is no sense stopping. The vault. The soot. The lump of coal in the straw where the egg had been, and the clerk who wrote down twelve. The stairs, and your palms. The hearth. The "rock". You tell them your steward did not know, and the sergeant did not know, and the widow is a widow who knows eggs. You tell them that if it ever burns a wagon or a barn or a man, they are to bring the bill to the citadel, and it will be paid, by you, in whatever coin is owed.{/n}''',
        c("Continue", "chaplain")),
    nar("confess", '''{n}The lane goes quiet in a way that is worse than shouting.{/n}
{n}You tell them the rest of it, because once you have started there is no sense stopping. The golems. The ash. The hearth. The "rock". You tell them your steward did not know, and the sergeant did not know, and the widow is a widow who knows eggs. You tell them that if it ever burns a wagon or a barn or a man, they are to bring the bill to the citadel, and it will be paid, by you, in whatever coin is owed.{/n}''',
        c("Continue", "chaplain")),
    nar("chaplain", '''{n}The chaplain lowers his torch a little.{/n} "Then the sin of it is on your head, Commander."
{n}Somebody spits. The woman in the Kenabres shawl turns away and goes back up the stair without a word, and that is worse than the spitting. The soldier with the burned jaw says he will remember this. He says it to you, not to the crowd, and you believe him.{/n}
{n}It takes a long time for the lane to empty. It does, in the end, because you are still standing there, and because nobody wants to be the first to put a torch to the Commander's confession. The sergeant with the squint stays by the kiln door when the rest have gone, spear grounded, and says he's taking the watch here tonight, on his own time, if it's all the same to you.{/n}''',
        c("Continue", "sky", requires=(DV_RETURNED,)),
        c("Continue", "said", forbids=(DV_RETURNED,))),
    nar("sky", '''{n}High on the ridge above Drezen, where the old watchtower stands, something grey that has been lying very still for a long time lifts its head toward the lower town, and listens, and does not lie down again.{/n}''',
        c("Continue", "said")),
    nd("said", '''{n}When the lane is empty she sits down on the kiln step, all at once, as if her knees have gone. The hatchling has fallen asleep inside the shawl with a corner of it in its mouth.{/n}
"I've always said it's what you do that matters. Not what you say." {n}She looks up at you.{/n} "I was wrong about tonight. Tonight what you said was the thing you did. You said it out loud, to all of them, with a torch in your face." {n}She wipes her cheek with the back of her wrist, and leaves another streak.{/n} "Sit down. You're shaking. So am I."''',
        c("[Sit down beside her.]", flags=(HATCHED,))),
    nar("lied", '''{n}Your voice carries. You have had a great deal of practice making it carry. You tell them about the storms in the north, and the wild things that come down out of the hills in a hard winter, and how the widow found it by the kiln looking for warmth, and that you will have it in an iron cage by morning and on a cart to the Worldwound's edge by noon.{/n}
{n}They believe you. They want to. It is a better story than the Commander's rock, and nobody has to feel a fool at the end of it.{/n}''',
        c("Continue", "lied2")),
    nar("lied2", '''{n}The lane empties. The chaplain goes last, and makes the sign of Iomedae's sword at the kiln's mouth as he goes.{/n}
{n}Nidalynn has not moved. She stands in the kiln's mouth with the hatchling asleep against her, and she looks at you for as long as it takes the last torch to go up the tanners' stair, and she does not say one word. Then she sits down on the kiln step with her back to you, and stays there.{/n}''',
        c("[Go home.]", flags=(HATCHED,))),
    nar("given", '''{n}The chaplain comes forward with his torch. The soldiers come after him. Nobody hurries; they are doing a thing they have been told to do by the Commander of the crusade, and there is no shame in it, and no need to run.{/n}
{n}Nidalynn does not move out of the kiln's mouth. She looks at you, once, over the chaplain's shoulder, and you see her understand.{/n}''',
        c("Continue", "silver")),
    nar("silver", '''{n}Then the kiln's roof comes off.{/n}
{n}It does not burst; it lifts, all of a piece, bricks and slates and the old iron bands, the way a lid lifts off a pot, and falls back into the lane in a long rattle. And out of the smoke, out of the white heart of the kiln, something goes up into the dark that is silver from end to end, huge, too huge for the lane, too huge for the sky over the lower town, with a small furious red-black thing held against its breast in one great claw.{/n}
{n}Every torch in the lane goes out at once in the cold of its passing. Then it is gone, over the east wall, north, into the snow.{/n}''',
        c("[Stand in the dark lane.]")),
], requires=(KILN,), forbids=(HATCHED, GIVEN_UP), delay=48)


# --- 6. The truth owed (after the lie): she will not eat at a liar's table, and says so --------------------------------

visit(P + "kiln.truth_owed", "Hills in the north", [
    nar("kiln", '''{n}She sends for you two days later. The note is in a big, round, old-fashioned hand on the back of a refugee's ration list, and it says only: "The kiln. Tonight. Bring nothing."{/n}
{n}There is no cage. There never was going to be a cage. The hatchling is asleep on a folded blanket in the kiln's warm mouth, and she is sitting beside it on the step, mending, and she does not get up.{/n}''',
        c("Continue", "hills")),
    nd("hills", '''"It came down out of the hills in the snow." {n}She does not look up from the mending.{/n} "That was a good story. You told it well. Everybody went home happy and nobody had to be ashamed of anything, and in the morning the chaplain told the whole lower town that the Commander had the matter in hand."
"I've been sitting here two days listening to people say how wise you were."''',
        c('"It kept the torches away from her."', "kept"),
        c('"You didn\'t say anything either."', "silent")),
    nd("kept", '''"It did." {n}She puts the mending down.{/n} "And the truth would have too, if you'd stood there long enough. I watched their faces. They were ready to be ashamed of themselves. You didn't give them the chance."''',
        c("Continue", "salt")),
    nd("silent", '''"No. I didn't." {n}She meets your eyes.{/n} "It wasn't mine to say. You hid her; I'd only have been telling on you. And you'd have let me, I think. You'd have let an old widow take the torches for you, and felt clever about it after."''',
        c("Continue", "salt")),
    nd("salt", '''"I'm not going to bargain with you, Commander. I'm too old, and it's beneath us both." {n}She folds her hands on the belly.{/n} "I'll tell you how it is with me, and you'll do what you like."
"Reudger wouldn't eat salt with a man who lied to him about what he loved. It wasn't a rule. He said it only wouldn't go down. I've found he was right." {n}She looks at the hatchling.{/n} "You love this ugly little thing. I've seen you look at her. And you stood in that lane and told the whole city she was a stray from the hills. I can't eat at your fire while that's the story. The salt won't go down."''',
        c('[Go to the morning muster and tell the garrison the truth] "Tomorrow. At muster, in front of all of them."', "muster",
          flags=(CONFESSED,), crusade=("Favors", -150)),
        c('"The story stays. It\'s safer for her."', "stays", flags=(LIE_KEPT, CLOSED))),
    nar("muster", '''{n}You do it in the citadel yard the next morning, from the steps, to three companies standing in the frost. It is harder than the lane would have been; they are not frightened now, only puzzled, and then angry, and a lie told once and then confessed is worse than a lie confessed at once. You can see them working out what else you might have called a rock.{/n}
{n}The chaplain is at the back. He does not say anything this time. He makes the sign of the sword, looking at you, and walks out of the yard before the companies are dismissed.{/n}''',
        c("Continue", "after")),
    nd("after", '''{n}She is at the kiln that evening, and she gets up when you come, which she did not do before.{/n} "I heard. The whole lower town heard." {n}She takes your hand, turns it palm up, puts a piece of bread in it.{/n} "That was harder than doing it in the lane. You know that. You'll have them looking at you sideways for a month."
"Eat that. It's not the salt. I'm not ready for the salt. It's only bread; you look like you've been sick."''',
        c("[Eat.]", flags=(HATCHED,))),
    nd("stays", '''"Then it stays." {n}She nods, slowly, as if she had known.{/n} "I'll keep her here through the winter; she needs the kiln. At the thaw I'll take her north, where there's snow and nobody to tell stories about her, and she can grow up whatever she's going to be." {n}She picks up the mending again.{/n} "You were very kind to her, Commander. You were kind to me. I'll remember it. I remember everything; it's my trade." {n}The needle goes in and out.{/n} "Go home. Mind the ice on the tanners' stair."''',
        c("[Go.]")),
], requires=(LIED,), forbids=(CONFESSED, LIE_KEPT), delay=48)


# --- 7. Whose is she (the kiln, after the confession): the claim, given up or kept (pivotal) ---------------------------

visit(WHOSE, "Whose she is", [
    nar("kiln", '''{n}The hatchling has already doubled in size, faster than any hatchling Nidalynn says she has known; the Wound in her, she thinks. She is the size of a hunting dog now, all neck and elbows and appetite, and she has learned to climb out of the kiln's mouth and sit on the step in the thin sun, and hiss at the sergeant with the squint, who has started bringing her pigs' ears in his pocket.{/n}
{n}Nidalynn is on the step beside her, with the widow's belly and a bowl of something that smells of barley, and she gives you the bowl before she says anything else.{/n}''',
        c("Continue", "eat")),
    nd("eat", '''"Eat first. Then I'm going to ask you something, and I'd rather you weren't hungry when I do. Hungry people say whatever gets them to the next meal." {n}She waits until you have eaten half of it.{/n}
"Whose is she?"''',
        c("Continue", "whose", forbids=(STRAW,)),
        c("Continue", "whose_straw", requires=(STRAW,))),
    # PP10: the straw's Commander kept what everybody else, Nidalynn included, had given up.
    nd("whose_straw", '''"I'm not being clever. It's a real question, and I don't know the answer." {n}The hatchling butts her head against Nidalynn's knee and is ignored.{/n} "You kept her fair, if there's such a thing. Everybody else had given her up, me with them, and you put your mark to a lie on your own stores' slate to keep her. The crusade could say she's its own, a war-prize out of the Sanctum that the druids left behind, and there's not a court in Mendev would argue. A dragon on your side of the Wound. There are generals who'd sell their mothers for that."
"I'm only an old woman with a kiln. I can't take what isn't given me. So I'm asking."''',
        c("Continue", "mother", requires=(DV_RETURNED,)),
        c("Continue", "choose", forbids=(DV_RETURNED,))),
    nd("whose", '''"I'm not being clever. It's a real question, and I don't know the answer." {n}The hatchling butts her head against Nidalynn's knee and is ignored.{/n} "You stole her fair, if there's such a thing. You took her when nobody else would have, and paid for it. The crusade could say she's its own, a war-prize out of the Sanctum, and there's not a court in Mendev would argue. A dragon on your side of the Wound. There are generals who'd sell their mothers for that."
"I'm only an old woman with a kiln. I can't take what isn't given me. So I'm asking."''',
        c("Continue", "mother", requires=(DV_RETURNED,)),
        c("Continue", "choose", forbids=(DV_RETURNED,))),
    nd("mother", '''"And her mother's alive. She'll come for her. Not tomorrow, maybe, but dragons have long memories and she has a long reason." {n}She says it without fear, as she might say that the river floods in spring.{/n} "When she comes, she'll be told the truth, by me. That you took her child, and I kept it. And she'll send the bill for it to you, Commander, not to me. That's only fair. I'd do the same."''',
        c("Continue", "choose")),
    nd("choose", '''{n}The hatchling has found your boot and is chewing the lace with great concentration.{/n}''',
        c('"She\'s yours to raise. I\'ve no claim on her, and I won\'t make one."', "given", flags=(RENOUNCED,)),
        c('"She\'s the crusade\'s. A dragon on our side of the Wound is worth an army."', "crusade", flags=(CLAIMED,)),
        c('"She\'s mine. I stole her fair."', "mine", flags=(CLAIMED,), forbids=(STRAW,)),
        c('"She\'s mine. I kept her fair, when nobody else would."', "mine", flags=(CLAIMED,), requires=(STRAW,))),
    nd("given", '''{n}She lets out a breath.{/n} "Just like that."
"You know what you're giving away? At the rate she's growing she'll be the size of a barn before long, and one day a thing that could take a city. You could have had her at your heel." {n}She puts her hand on the hatchling's back, and the hatchling, for once, allows it.{/n} "And you'd have been a worse Commander for it, and she'd have been a worse dragon."
"Thank you. I don't say it for show. I'm grateful, and I'll stay grateful, and you'll find that's a heavy thing to have a dragon feel toward you."''',
        c("Continue", "bill", requires=(DV_RETURNED,)),
        c("[Scratch the hatchling behind the horn-buds, carefully.]", "end", forbids=(DV_RETURNED,))),
    nd("bill", '''"And her mother's bill still comes to you." {n}She says it gently.{/n} "Giving her to me doesn't change who took her. You know that."''',
        c('"I know."', "end")),
    nd("end", '''{n}The hatchling bites you. Not hard. As an experiment.{/n}
{n}Nidalynn laughs.{/n} "She likes you. That's how they say it, at this age. Wait till she's bigger; she'll say it with fire."''',
        c("[Stay on the step with them.]")),
    nd("crusade", '''"An army." {n}She repeats it without any tone at all.{/n} "Then the crusade will feed her. Twice a day, meat, and not rotten, and a warm place, and somebody to be bitten by. I'll show your people how." {n}She takes the bowl back from you and sets it down.{/n} "And when she can fly, she'll go where she likes, Commander, and she won't like the crusade. They never do. You can't keep a dragon by owning her. You can only keep one by being worth coming back to."''',
        c("[Leave her on the step.]")),
    nd("mine", '''"Fair." {n}She turns the word over.{/n} "It's a trickster's word, that one. Everything's fair if you were clever enough." {n}She stands up, belly first.{/n} "Then feed her. She's yours. Twice a day, and not rotten, and I'll show you how, because I'm not going to let her starve for your pride."
"But she isn't a thing, Commander. She's a child. And I don't eat at a fire where children are property."''',
        c("[Leave her on the step.]")),
], requires=(CONFESSED, HATCHED), forbids=(RENOUNCED, CLAIMED), delay=24)


# --- 8. The claim, again (after a claim): she asks nothing; the Commander watches ----------------------------------------

visit(P + "kiln.claim_again", "Yours", [
    nar("bill", '''{n}The quartermaster sends up a bill: four goats, a pig, a side of salt beef, a sack of lime, a new kiln door, and two days' wages for a stablehand who was bitten through the calf and would like it known that he was not paid to be bitten. The bottom line has been underlined twice.{/n}
{n}The crusade's dragon is growing.{/n}''',
        c("Continue", "kiln")),
    nar("kiln", '''{n}You go down to the kiln at dusk. The hatchling is on the roof, where she is not supposed to be, spreading wings that are not yet wide enough to hold her and folding them again, and spreading them, and folding them, the way a child tries a word it does not know yet.{/n}
{n}Nidalynn is below, on the step, watching. Every time the wings open her whole body leans a little toward them. She does not call up. She does not ask you anything. She has said she will not, and she does not.{/n}''',
        c("Continue", "look")),
    nar("look", '''{n}The hatchling sees you, and hisses, and looks down at Nidalynn, and hops along the roof-ridge toward her end of it and settles there, as close to her as the roof allows.{/n}
{n}Nobody has to tell you which way she will fly.{/n}''',
        c('"Nidalynn. She\'s yours. I was wrong to call her anything else."', "let_go", flags=(RENOUNCED,)),
        c("[Keep your claim, and say nothing.]", "keep", flags=(CLAIM_KEPT,))),
    nd("let_go", '''{n}She does not turn round at once. When she does, her face is wet.{/n} "You didn't have to. You know that? The quartermaster's bill would have got to you in the end, and you'd have been a fool, and then she'd have flown, and you'd have been a fool with an empty kiln. You'd have got there."
"You got there before she flew. That's the part that counts." {n}She holds out her hand to the roof, and the hatchling comes down onto her arm, heavily, all claws, and she does not flinch.{/n} "Thank you. Sit down. I've soup."''',
        c("[Sit down.]")),
    nd("keep", '''{n}She does not turn round.{/n} "Mind the ice on the tanners' stair," {n}she says, to the roof.{/n}''',
        c("[Go.]")),
], requires=(CLAIMED, HATCHED), forbids=(RENOUNCED, CLAIM_KEPT), delay=72)


# --- 9. Feeding (optional, after the hatching): what she eats, and what she's called -----------------------------------

visit(FEEDING, "What she eats", [
    nar("kiln", '''{n}She has eaten a kiln-cat. Nidalynn tells you this at the door as if it were news of a death in the family, and then adds, in a lower voice, that the cat started it.{/n}
{n}The hatchling is on the warm step with her tail around her feet, looking pleased with herself. She is bigger every time you see her, and hungrier.{/n}''',
        c("Continue", "meat")),
    nd("meat", '''"She needs meat. A great deal of it, and often, and alive when she can get it; she has to learn to kill or she'll never learn to hunt." {n}Nidalynn sits down with a grunt.{/n} "And what she learns to hunt now is what she'll go looking for when she's grown, if I've any say in it. Her mother learned on whatever came through the Wound, and look what she hunted: your army."
"So. You took her. You'll help me choose."''',
        c('[Have the provosts send her what they kill at the rift] "Demons. Let her grow up hating the taste of them."', "demons", flags=(FED_DEMONS,)),
        c('[Send down goats from the crusade\'s stores] "Goats. A dragon that hunts goats is somebody\'s problem, not everybody\'s."', "goats",
          flags=(FED_GOATS,), crusade=("Materials", -50)),
        c('"The undercroft\'s full of rats. Let her work for it."', "rats", flags=(FED_RATS,))),
    nd("demons", '''{n}She is quiet a moment.{/n} "That's a hard way to raise a child. On the thing that ruined her." {n}She looks at the pale seam down the hatchling's spine.{/n} "It might be the right one. She'll never be free of the Wound; it's in her. Better she learns to hate it than to crave it." {n}She nods, once.{/n} "Demons, then. I'll tell the provosts to bring them dead. I'll not have her fighting a vrock at this size."''',
        c("Continue", "name")),
    nd("goats", '''"Goats." {n}Something eases in her face.{/n} "Yes. That's a farmer's answer. A dragon that thinks of goats as dinner thinks of goatherds as the people who keep her dinner. That's a start." {n}She scratches the hatchling under the jaw; it allows it.{/n} "The old folk on the grass used to say a well-fed dragon is a good neighbour. They mostly meant wolves. It holds."''',
        c("Continue", "name")),
    nd("rats", '''"The undercroft." {n}She laughs, surprised.{/n} "You're cheaper than the Windstep, and they counted every copper." {n}She thinks about it.{/n} "It's not wrong. Let her hunt what's under her feet. She'll learn patience, and the cooks will love her, and she'll grow up thinking that what a dragon is for is keeping a house clean." {n}A pause.{/n} "There are worse lessons."''',
        c("Continue", "name")),
    nd("name", '''"The soldiers want to know her name. The sergeant with the squint has been calling her 'little mother', which I won't have." {n}She glances at you sidelong.{/n} "I mean to let her name herself, when she's old enough. But she'll need something to be called until then."''',
        c('"Soot. For the ash she came out in."', "soot", flags=(NAME_SOOT,)),
        c('"Pebble. She was a rock, once."', "pebble", flags=(NAME_PEBBLE,)),
        c('"Let her choose her own."', "none", flags=(NAME_NONE,))),
    nd("soot", '''"Soot." {n}She tries it on the hatchling, who ignores it with the whole of her body.{/n} "She won't answer to it. She'll know it's hers, all the same. Every time someone says it she'll remember she was hidden once, and got out."''',
        c("[Leave them on the step.]")),
    nd("pebble", '''{n}She laughs until she has to hold her ribs.{/n} "Pebble. A woundwyrm called Pebble. Her mother would eat you." {n}She wipes her eyes.{/n} "Yes. Pebble. So nobody ever forgets you told the whole city she was a rock, and so she never does either."''',
        c("[Leave them on the step.]")),
    nd("none", '''"Good." {n}She says it quietly.{/n} "That's a thing people never think of. What she's called is the first thing anybody ever gives her, and she didn't choose it." {n}She puts her hand on the hatchling's back.{/n} "'Little one', then, until she tells us otherwise. It'll do for both of us."''',
        c("[Leave them on the step.]")),
], requires=(HATCHED,), forbids=(FEEDING, LIE_KEPT), delay=24, optional=True)


# --- 10. A letter to the Abyss (Chapter 4, optional): from the kiln ------------------------------------------------------

visit(ABYSS_LETTER, "From the kiln", [
    nd("letter", '''{n}The letter is on the back of a quartermaster's requisition for lamp oil, folded small, in a big, round, old-fashioned hand. It smells of woodsmoke. It came through the Storyteller's portal with the supplies he fetches from Golarion: a Sarkorian woman was waiting at his door in Drezen with it, he says, and would not go away until he had put it in his satchel.{/n}
"Commander. I hope you are eating. I don't know what grows where you are. Whatever it is, don't eat that. Eat what you brought."''',
        c("Continue", "hatched", requires=(HATCHED,)),
        c("Continue", "egg", forbids=(HATCHED,))),
    nd("egg", '''"The egg is well. It knocks all day now and sings at night, and the kiln's never been hotter. I sleep beside it. The sergeant with the squint brings me wood and pretends he's only passing."
"It is snowing here. I have had to put a stone on this letter to write it; the wind wants it."''',
        c("Continue", "end")),
    nd("hatched", '''"She is well. She is twice the size she was and three times as rude. She has been on the kiln roof twice and fallen off it twice, and the second time she bit the sergeant for laughing. He has forgiven her. He hasn't forgiven me for laughing too."
"She looks for you. I don't know how she knows you're gone. She sits on the step at dusk and faces the citadel, and when you don't come she eats something out of spite."''',
        c("Continue", "end", forbids=(FORM,)),
        c("Continue", "own", requires=(FORM,))),
    nd("own", '''"The women on the step have stopped asking about the widow. They ask about you instead. Old Anka wants to know whether you are eating. I told her I had no idea, and that it was a scandal."
"Come back whole. I have been setting other people's bones since you left, and I am tired of it."
{n}At the bottom, in the same hand, smaller, as if written afterwards and nearly scratched out:{/n} "N. Of the kiln. Mind you come home."''',
        c("[Fold the letter away.]")),
    nd("end", '''"The refugee women are asking about the widow's time. I tell them it will come when it comes. They cluck at me and bring me soup. I will tell you a secret: I am enjoying it very much."
"Come back whole. I have been setting other people's bones since you left, and I am tired of it."
{n}At the bottom, in the same hand, smaller, as if written afterwards and nearly scratched out:{/n} "N. Of the kiln."''',
        c("[Fold the letter away.]")),
], requires=(KILN, STORYTELLER_SUPPLIES), forbids=(ABYSS_LETTER, LIE_KEPT), delay=24, chapters=(4, 4), kind="letter",
    optional=True)   # PP10 (Sol COX): carried by the Storyteller's portal supplies, once he has offered them


# --- 11. The spear (after the confession): the man whose company her mother burned (pivotal) ---------------------------

visit(P + "kiln.the_spear", "The man from the ford", [
    nar("night", '''{n}The sergeant with the squint wakes you himself, in the small hours, with a lantern and a face like a funeral.{/n} "Commander. The kiln. You'd best come. Nobody's hurt. Not yet."
{n}There is a man on his knees in the lane below the kiln with his hands behind his head and a boar-spear lying in the frost in front of him. You know the burned jaw before you see the face. The soldier from the ford.{/n}''',
        c("Continue", "held")),
    nar("held", '''{n}Nidalynn is standing over him in the widow's dress with a lantern in one hand and nothing in the other. She did not need anything in the other. The kiln door behind her is barred, and from inside it comes a low, furious, bubbling hiss, like a pot about to boil over.{/n}
{n}"He came over the wall by the tanners' stair," she says, very quietly. "He'd have been at the door in another minute. I heard him on the stair. I hear everything on that stair."{/n}''',
        c("Continue", "him")),
    nar("him", '''{n}He does not look at you. He looks at the frost.{/n} "Sixty men at the ford, Commander. The mother came down out of the smoke on us before we'd got the carts across. I had my brother in the second cart." {n}His voice is perfectly flat.{/n} "You said to bring the bill to you. I'm bringing it. I'm not sorry. You can hang me; I'll still not be sorry."''',
        c("Continue", "choice")),
    nd("choice", '''{n}Nidalynn does not look at you. She is looking at the man on his knees, and her face is not angry. It is something older and sadder than angry.{/n} "He's yours to judge, Commander. He's your soldier, and it's your city, and it's your confession he came to answer." {n}A pause.{/n} "Only remember I'm standing here when you do it."''',
        c('[Hand him to the provost] "Deserting his post and drawing a weapon in the city. The provost will deal with it."', "provost", flags=(SPEAR_PROVOST,)),
        c('[Let him go] "Go home. Go to bed. We\'ll say you were drunk."', "freed", flags=(SPEAR_FREED,)),
        c('"Unbar the door, Nidalynn. Let him see what he came to kill."', "see", flags=(SPEAR_SEEN,))),
    nd("provost", '''{n}She nods slowly. She does not argue.{/n} "That's the law. You'll need your law, with a war on." {n}The sergeant takes the man by the arm and hauls him up, not roughly.{/n}
"He'll get twenty lashes and a month in the cells, and he'll come out hating her more than he went in." {n}She watches them go up the stair.{/n} "It was a fair judgment. I'd have made a different one. I'm not a Commander."''',
        c("[Go home.]")),
    nd("freed", '''{n}The man looks up at you at last, and you watch him not believe it.{/n} "Commander?"
"Go on," {n}Nidalynn says, before you can.{/n} "Go on up the stair before the Commander remembers the law. And leave the spear." {n}He goes. He does not run, which is something.{/n} "You were kind to him." {n}She picks up the boar-spear, weighs it, leans it against the kiln wall.{/n} "He'll try again, maybe. Or he'll lie awake and think about it. Kindness is a gamble, Commander. It's the only kind I've ever liked."''',
        c("[Go home.]")),
    nar("see", '''{n}She looks at you for a heartbeat. Then she lifts the bar, and pulls the kiln door open, and the heat comes out into the frost in a great slow breath.{/n}
{n}The hatchling is on the bricks at the back with every scale on end, hissing at the lane, red-black and no bigger than a dog, with the pale Wound-seam down her back and her little wings mantled over her like a cloak two sizes too big. She is shaking. She has never heard a man come up a stair with a spear before.{/n}''',
        c("Continue", "see2")),
    nar("see2", '''{n}The soldier looks at her from his knees, and keeps looking.{/n}
{n}"That's it," he says at last. "That's all it is." He sounds as if somebody has cheated him. Then he puts his face in his hands, the burned side and the whole side, and stays like that.{/n}''',
        c("Continue", "see3")),
    nd("see3", '''{n}Nidalynn goes and sits down beside him on the frozen step, with a grunt for the belly, and takes a heel of bread out of her apron pocket, and breaks it in half, and puts half in his hand.{/n} "Eat that. You've been awake all night hating something the size of a dog. It's hungry work." {n}She looks up at you over his bent head.{/n} "Go home, Commander. I'll send him up the stair when he's fed. Nobody's going to the provost tonight."''',
        c("[Leave them on the step.]")),
], requires=(CONFESSED, HATCHED), forbids=(SPEAR_PROVOST, SPEAR_FREED, SPEAR_SEEN, LIE_KEPT, FORM), delay=48, optional=True)


# --- 12. The druids (optional, in the druids' world): where the eleven went ---------------------------------------------

visit(P + "kiln.the_druids", "Four druids and a handcart", [
    nar("kiln", '''{n}She is at the kiln with a letter on thick paper, its seal broken, a blob of wax with no mark in it at all, and she has been turning it over in her hands since before you came down the stair.{/n}''',
        c("Continue", "letter")),
    nd("letter", '''"From the others. The druids." {n}She puts it down on the step between you.{/n} "They're three rivers east, in a valley with a white stone on top of the hill, and your eleven are there. Hatched, all of them. Fat and furious. The gold one says they bite everyone equally and that he's proud of them."
"They want to know why I'm still here. With one. In a kiln, in a city, beside a trickster."''',
        c('"What will you tell them?"', "tell"),
        c('"Why are you still here?"', "tell")),
    nd("tell", '''"That she's the smallest, and she was the coldest, and she'd not have lived the road." {n}She looks at the kiln.{/n} "That's true. It's not all of it. I'll tell them the rest when I know what the rest is." {n}She glances at you.{/n} "They'll laugh. Dragons are terrible gossips. The gold one will fly over one night to have a look at you, pretending to be a stork."''',
        c("Continue", "hunted", requires=(DV_HUNTING,)),
        c("Continue", "end", forbids=(DV_HUNTING,))),
    nd("hunted", '''{n}She picks up the letter again.{/n} "And there's this. They say a grey woundwyrm has been working along the rivers, looking for the valley. She found the white stone. She stood off. The gold one stood in front of the nest and she stood off." {n}Her mouth thins.{/n} "You sent her, Commander. I know you did. You'd your reasons, and she's their mother, and I've been trying to decide what I think of it ever since."''',
        c('"She had a right to know where her children were."', "right", flags=(DRUIDS_DEFENDED,)),
        c('"I was wrong to send her."', "wrong", flags=(DRUIDS_REGRETTED,))),
    nd("right", '''"She had." {n}She says it with difficulty.{/n} "I'll give you that, because it's true, and I don't like it. A mother's got a right. So have eleven hatchlings who've never met her and would be her dinner if she were hungry enough." {n}She tucks the letter into her apron.{/n} "We'll not agree on this. I've decided I can bear that."''',
        c("Continue", "end")),
    nd("wrong", '''{n}She is quiet a while.{/n} "You don't say that often. I've been listening. You'll say it was a joke, and it worked, didn't it, and you'd do it again. You don't often say 'wrong'." {n}She tucks the letter into her apron.{/n} "Well. It's said. That'll do."''',
        c("Continue", "end")),
    nd("end", '''"I'll write back tonight. I'll tell them the little one's well, and that the Commander of the crusade feeds my kiln with wood at midnight and eats my bread." {n}Her ears have gone pink again.{/n} "That'll give them something to talk about for a century."''',
        c("[Leave her to her letter.]")),
], requires=(KILN, "eggs.druids"), forbids=(LIE_KEPT,), delay=48, optional=True)


# --- 13. Ulbrig at the kiln (optional, Ulbrig in the company): the white-haired girl at Reudger's fire -----------------

visit(P + "kiln.ulbrig", "A face from the grass", [
    nar("lane", '''{n}Ulbrig insists on coming down to the kiln with you. He will not say why. He walks down the tanners' stair in silence, which is not like him, with his big hands opening and shutting at his sides.{/n}
{n}Nidalynn is on the step, in the widow's dress, mending. She looks up when you come round the corner of the lane, and sees who is with you, and the needle stops.{/n}''',
        c("Continue", "look")),
    n("look", "Ulbrig", '''{n}Ulbrig stops a good ten feet off and stares at her. Then he pulls off his cap, which you have never seen him do for anyone.{/n} "Mother, you'll forgive me. You were humming, on the stair. That's a Windstep mare-song. Nobody's sung those since before I went to sleep, eh." {n}His voice has gone thick.{/n} "There was a white-haired girl at old Reudger's fire, when I was a lad. She sang it just so. You've the look of her. The eyes."''',
        c("Continue", "dung"), portrait="Ulbrig"),
    nd("dung", '''{n}She puts the mending down very carefully, and looks at him for a while, at the big hands and the cap.{/n} "I've heard of the Olesk. Horse-thieves and bog-riders, the Windstep said, and the best griffon-men on the grass." {n}Her mouth twitches.{/n} "Reudger's fire had a great many strays at it. White-haired girls among them, I shouldn't wonder."''',
        c("Continue", "ulbrig2")),
    n("ulbrig2", "Ulbrig", '''"Aye. Strays." {n}He looks at her a long while, at the pale grey eyes, and his face goes slowly still.{/n} "She'd be old as the hills now, that girl. Older than me, and I slept a hundred years."
{n}He does not ask. You can see him decide not to ask. He is a Sarkorian of the old clans, and there are things you do not ask of a woman who sings the Windstep's songs.{/n}''',
        c("Continue", "reudger"), portrait="Ulbrig"),
    nd("reudger", '''"He asked after every stray who stopped coming to the summer camp." {n}She says it gently.{/n} "Olesk boys too, I shouldn't wonder. He always thought they'd gone off to be warriors. He said it was a waste of good horsemanship."
"I never found his grave, Ulbrig. I've looked."''',
        c("Continue", "ulbrig3")),
    n("ulbrig3", "Ulbrig", '''"No." {n}He turns his cap round in his hands.{/n} "Nobody will. The grass is gone." {n}He is quiet a while.{/n} "But I remember the brand. The mare under the stars. I could cut it in a saddle yet." {n}He looks at the kiln, and the hiss coming out of it, and back at her.{/n} "And you're raising a dragon in a lime-kiln for the warchief, eh. Of course you are. Reudger would've said so. He'd have said the Windstep always did take in strays."''',
        c("Continue", "end"), portrait="Ulbrig"),
    nd("end", '''"He'd have said it about all of us." {n}She holds out her hand, and Ulbrig takes it, and bends over it like a man in an old song.{/n}
"Come to the kiln when you like, Olesk. Bring your own bread; I hear the Olesk ate like wolves." {n}When he lets go she turns her head and looks at you, and does not say anything, and does not need to.{/n}''',
        c("[Leave the two of them to the step.]", flags=(ULBRIG_MET,))),
], requires=(KILN, "ulbrig.in_party"), forbids=(ULBRIG_MET, LIE_KEPT, FORM, "ulbrig.dead", "ulbrig.kicked_out"), delay=24,
    optional=True)


# --- 14. The goat (after the claim is given up): what the child costs, and who pays it --------------------------------

visit(P + "kiln.the_goat", "A goat in the snow", [
    nar("yard", '''{n}The goat belonged to a Kellid widow in the refugee quarter, a real one, with a baby and no milk of her own. It was the only goat in the quarter. Everybody knew it; the children used to take turns walking it on a string.{/n}
{n}What is left of it is in the snow behind the kiln, and the young dragon is sitting beside what is left of it with blood to the eyes and an expression of absolute, untroubled contentment.{/n}''',
        c("Continue", "widow")),
    nar("widow", '''{n}The real widow is standing in the lane with the baby in her shawl, not crying. Two of the women from the jeweller's step are standing with her. Behind them, at a distance, there are more faces at the ends of the lane than there should be for one goat.{/n}
{n}Nidalynn is on her knees in the snow in front of the young dragon, holding her by the jaw, talking to her low and hard in Draconic. The young dragon is not listening. She is licking her teeth.{/n}''',
        c("Continue", "her")),
    nd("her", '''{n}She lets go of the young dragon's jaw and gets up, and looks at you across the snow, and her face is very tired.{/n} "I let her out to hunt. She found the goat's pen instead. It's my fault. I didn't latch the kiln door; I was watching her the way you watch a child learning to walk, and I forgot she can climb."
"The child needs milk, Commander. There isn't any other goat. Whatever you do now, the women at the end of this lane are going to remember it longer than they'll remember the goat."''',
        c('[Send down a milch-goat from the citadel\'s own pens, and a month\'s milk ration] "The crusade owes her a goat. It\'ll pay one."', "paid",
          flags=(GOAT_PAID,), crusade=("Materials", -50)),
        c('[Walk down the lane to the widow yourself, and tell her it was your dragon, and ask what she needs]', "asked", flags=(GOAT_ASKED,)),
        c('[Trickery: tell the lane that wolves came over the wall in the night]', "wolves", flags=(GOAT_WOLVES,))),
    nar("paid", '''{n}The goat comes down the tanners' stair before noon, a brown nanny with a bell and a sour temper, led by a stable-boy who keeps a very long way from the kiln. The widow looks at it, and at the Commander's seal on the ration chit, and at you, and then she nods, once, the way people nod at weather.{/n}''',
        c("Continue", "after_paid")),
    nd("after_paid", '''"That was generous." {n}Nidalynn is watching the women lead the new goat away.{/n} "And quick. They'll remember the quick more than the generous. A goat that comes the same morning means somebody up there is watching." {n}She rubs her face.{/n} "Thank you. It should have been me. I've nothing to pay with but soup."''',
        c("Continue", "end")),
    nar("asked", '''{n}You walk down the lane in front of all of them, past the women and the faces at the end of it, and you stop in front of the widow with the baby, and you tell her it was your dragon, and it was your fault, and you ask her what she needs.{/n}
{n}She looks at you for a while. She is not used to being asked. Then she tells you, in careful Common, with a great deal of Kellid in it: milk for the baby till spring, a place nearer the wall where the wind does not come in, and for the dragon never to come into the quarter again. You say yes to the first two. You do not lie to her about the third.{/n}''',
        c("Continue", "after_asked")),
    nd("after_asked", '''{n}When you come back up the lane Nidalynn is sitting on the kiln step with the young dragon's head in her lap, and she is looking at you in a way she has not looked at you before, as if you had surprised her, and she had not expected to be.{/n} "You told her you couldn't promise the third. To her face. With the whole lane listening." {n}She strokes the dragon's neck.{/n} "Reudger would've liked you. He'd not have said so. He'd have given you the worst horse and watched how you rode it." {n}She looks down at the young dragon.{/n} "I'll fix that latch tonight. And she hunts with me beside her till she's learned whose goats aren't hers."''',
        c("Continue", "end")),
    nar("wolves", '''{n}It is easy. It is always easy. Three wolves over the east wall in the night, grey ones, with the Wound on them; you saw their tracks yourself at first light; the sentries on the wall will be flogged. By the time you have finished the lane is looking at the wall, and not at the kiln.{/n}
{n}The widow with the baby looks at the blood on the young dragon's muzzle, a long time, and then at you. She says nothing. She has lived in a refugee quarter long enough to know what saying something costs.{/n}''',
        c("Continue", "after_wolves")),
    nd("after_wolves", '''{n}Nidalynn does not speak until the lane has emptied. Then she goes into the kiln and comes out with a crock of goat's milk, the last of it, from the widow's goat, which the widow sold her yesterday, and walks down the lane with it herself, and knocks on a door, and goes in.{/n}
{n}When she comes back she does not sit down.{/n} "Wolves." {n}Just that, and then, low:{/n} "I wear a belly and a shawl, and nobody pays for it but me. That's a costume. This is two boys on the east wall to be flogged for a goat my child ate, and a baby with no milk because her mother daren't say what took it." {n}Her hands are shaking. She folds them.{/n}
"You'll go to the provost before the flogging, and to that door in the morning, and you'll put it right. Or you'll not eat at my fire again. I'll not raise her on a lie that somebody else bleeds for."''',
        c("Continue", "end", forbids=(P + "goat.wolves",)),
        c("[Go to the provost before the flogging, and to the widow's door at first light: the dragon took the goat, the sentries are clear, and the child has milk till spring.]",
          "corrected", flags=(GOAT_CORRECTED,), crusade=("Materials", -50)),
        c('"The wolves stand. It\'s kinder to everyone."', "stands")),
    nd("corrected", '''{n}The sergeant with the squint tells her before you can: the provost tore up the order with his own hands and said a few things about Commanders that the sergeant will not repeat. The widow at the end of the lane took the milk ration and looked at you the whole time she took it.{/n}
{n}Nidalynn hears it out on the kiln step with the young dragon's head in her lap.{/n} "Good. The lane thinks less of you this morning, and the east wall thinks more. That's the right way round." {n}She moves over on the step.{/n} "Sit down. You've a goat's worth of shame on you, and it suits you better than the wolves did."''',
        c("Continue", "end")),
    nd("stands", '''{n}She looks at you for a long breath, and then at the young dragon, asleep with blood on her chin.{/n} "Then it stands." {n}No anger in it at all.{/n} "She'll not grow up at a fire where other people are whipped for her suppers. I'll keep her here while the snow lasts. At the thaw we go north." {n}She picks up the young dragon, heavily, and turns for the kiln.{/n} "Mind the ice on the tanners' stair."''',
        c("[Go.]", flags=(GOAT_STANDS, CLOSED))),
    nd("end", '''{n}The young dragon, who has understood none of this, lays her bloody chin on your boot and goes to sleep.{/n}''',
        c("[Let her.]")),
], requires=(RENOUNCED, HATCHED), forbids=(GOAT_PAID, GOAT_ASKED, GOAT_WOLVES, LIE_KEPT), delay=48, optional=True)


# --- 15. The wake (optional, the widow's step or her own): a Sarkorian burial, and her song ----------------------------

visit(P + "steps.the_wake", "Warriors are not the only ones", [
    nar("quarter", '''{n}An old man dies in the refugee quarter of the Wound-fever that comes in off the river every winter. He was a Kellid, a saddler, from a clan whose name nobody in the quarter can remember; he had no family left. The crusade's chaplains will bury him in the common pit outside the north gate with the others this week.{/n}
{n}Nidalynn sends for you. The note says only: "The saddler. Tonight. You should see how it's done."{/n}''',
        c("Continue", "pyre")),
    nar("pyre", '''{n}It is not the common pit. It is a strip of frozen ground under the east wall, behind the kiln, where the refugee women have built a pyre out of what they could find: a broken cart, a doorframe, the kiln's own wood. The saddler is on it in his best coat, with his awl in his hands.{/n}
{n}There are perhaps thirty of them. They are not weeping. They are standing in a ring with their hands at their sides, waiting, and they are all looking at the tall white-haired woman at the head of the pyre.{/n}''',
        c("Continue", "song")),
    nar("song", '''{n}She sings. It is not a hymn; there is no god in it. It goes low and long, a herding-song, the kind that is sung to bring mares home over a great distance in bad weather, and every Kellid in the ring knows it, and one by one they come in under her, until thirty voices are carrying it along the foot of the wall in the dark.{/n}
{n}Then she stops, and they stop, and she says one word into the silence: a name. The saddler's. And the whole ring says it back to her, together, and then the women put their torches to the pyre.{/n}''',
        c("Continue", "after")),
    nd("after", '''{n}She comes and stands beside you while it burns, with the firelight on her face.{/n} "Among the old clans, you say the name at the fire, and everyone who hears it has to keep it. That's all a grave is for, really. A place to keep a name. We've no graves left, so we keep them this way." {n}Her eyes stay on the fire.{/n} "Thirty people know his name now who didn't this morning. He'll last as long as the last of them."''',
        c('[Say the saddler\'s name, as they did.]', "said", flags=(WAKE_SAID,)),
        c('"How many names do you keep?"', "how_many"),
        c("[Stand with her, and say nothing.]", "stand")),
    nd("said", '''{n}The women nearest you turn their heads when you say it. One of them, an old one, nods to you, the way you nod to somebody who has done a thing properly.{/n}
{n}Nidalynn's hand finds yours in the dark, and holds it hard.{/n} "Now you've one too. Mind you keep it. It's not a small thing I've asked you to carry."''',
        c("Continue", "end")),
    nd("how_many", '''"All of them." {n}She says it simply.{/n} "Every one I've heard said at a fire, since the Wound. I've a very good memory; it's a dragon's curse. There are nine thousand, four hundred and some. I say them over, sometimes, when I can't sleep." {n}A small, crooked smile.{/n} "It takes a long time. I don't sleep much."''',
        c("Continue", "end")),
    nar("stand", '''{n}You stand with her. After a while she leans, very slightly, so that her shoulder is against yours, and stays there until the pyre falls in.{/n}''',
        c("Continue", "end")),
    nd("end", '''"Warriors are not the only ones worth remembering." {n}She says it to the fire, like a line of the song.{/n} "If we forget what these people were in peace, we forget what the war's for. I've said that before, to somebody who didn't understand it." {n}She turns her head and looks at you.{/n} "You do. I can see you do. Go home. Thank you for coming. I'll stay till the embers are out; somebody has to."''',
        c("[Go home.]")),
], requires=(KILN, FORM), forbids=(P + "steps.the_wake", LIE_KEPT), delay=48, optional=True)


# --- 16. The chaplain (optional, after the confession): what the church made of it -------------------------------------

visit(P + "kiln.the_chaplain", "The chaplain's report", [
    nar("kiln", '''{n}The chaplain of Iomedae who held the torch on the night of the hatching is sitting on the kiln step when you come down the lane, with his hands folded between his knees and his breath smoking. He has no torch today. He has a satchel.{/n}
{n}Nidalynn, in the doorway, has given him a bowl of barley. He has not eaten it. He gets up when he sees you, and bows, stiffly, the bow of a man who has decided on it in advance.{/n}''',
        c("Continue", "report")),
    n("report", "Chaplain", '''"Commander. I have written to the Mendevian see about the night at the kiln. I thought you should hear it from me." {n}He meets your eyes, and you get the impression it costs him something.{/n} "I have written that the Commander of the crusade kept a woundwyrm's egg in this city by deceit, and hid it under a lie, and that a woundwyrm now lives inside our walls."
"And I have written that the Commander told the truth in the end, all of it, in front of the city, and took the sin on {mf|his|her} own head. I have written that it was the only honest thing I have heard out of the citadel since I came here." {n}A pause.{/n} "Both of those things will be read in the see. I do not know which of them they will remember."''',
        c('"Why tell me?"', "why"),
        c('"What do you want?"', "want")),
    n("why", "Chaplain", '''"Because you told us." {n}He says it simply.{/n} "It seemed to me that a man who is told the truth owes it back. I have always held that the truth is a blade that cuts both hands that hold it. I am holding my end."''',
        c("Continue", "want"), portrait=""),
    n("want", "Chaplain", '''{n}He looks past you at the kiln's mouth, where something red-black is watching him from the dark with its head low.{/n} "I want to know whether it can be saved. The Wound's taint is in it; I have seen the seam on its back. I have seen men with that seam, Commander. Most of them I burned. I believed I had to."
"I would like to pray over it. Not to exorcise it. To ask. I do not think the goddess has ever been asked about a woundwyrm, and I would like to know what she says."''',
        c('"Nidalynn? It\'s your kiln."', "hers"),
        c('"Pray, then. It can\'t hurt."', "pray"),
        c('"Leave her be, Father. She\'s had enough fire for one life."', "leave")),
    nd("hers", '''{n}She has been listening from the doorway with her arms folded over the belly. She looks at the chaplain for some time.{/n} "It's your kiln, Commander, whatever I say. But since you ask." {n}She steps aside from the kiln's mouth.{/n} "Pray, Father. Say it out loud, so she hears you. Prayers never did any harm to a thing that was going to grow up good. And if she's going to grow up wicked, she'll need all the asking she can get."''',
        c("Continue", "prayer")),
    nd("pray", '''{n}Nidalynn looks at you, and then at the chaplain, and then she steps aside from the kiln's mouth without a word.{/n}''',
        c("Continue", "prayer")),
    nar("prayer", '''{n}He kneels on the frozen step, in front of the dark, and prays. Not the rite of exorcism; you have heard that, and this is not it. It is short and plain and in Common, the kind of prayer a soldier says over a wounded horse, and at the end of it he asks the goddess, in so many words, what this is, and what it is for.{/n}
{n}Nothing happens. No light. No voice. The young dragon comes to the edge of the kiln's mouth and puts her nose out into the cold and sniffs the chaplain's knee, and sneezes, and goes back in.{/n}''',
        c("Continue", "after_prayer")),
    n("after_prayer", "Chaplain", '''{n}He gets up. His knees crack. He looks, of all things, satisfied.{/n} "No answer. I did not expect one, and I find I am glad of it. I will not burn what I have not been told to burn." {n}He picks up the barley, at last, and eats it standing, quickly, like a man used to eating on a march.{/n} "Thank you, goodwife. That was good barley. I shall write that to the see as well; they will not know what to make of it."''',
        c("Continue", "end"), portrait=""),
    n("leave", "Chaplain", '''{n}He considers you, and then the kiln, and then he nods, once.{/n} "Enough fire for one life. Yes. I held the torch; I know how much." {n}He picks up the barley at last, and eats it standing, quickly, like a man used to eating on a march.{/n} "Thank you, goodwife. That was good barley. I will come back in the spring, if I may, and ask again."''',
        c("Continue", "end"), portrait=""),
    nd("end", '''{n}When he has gone up the stair she comes and stands beside you on the step.{/n} "He's a good man. Stiff as a new saddle, and he'd burn half this city if his goddess told him to, and he'd weep while he did it." {n}She watches the stair.{/n} "Silvers and Iomedae's people get on well enough. We both think the truth matters. We only disagree about what to do with a sword afterwards."''',
        c("[Watch the stair with her.]", flags=(CHAPLAIN,))),
], requires=(CONFESSED, HATCHED), forbids=(CHAPLAIN, LIE_KEPT, FORM), delay=72, optional=True)


# --- 17. A day in charge (optional, after the claim is given up): the Commander minds the child ------------------------

visit(P + "kiln.in_charge", "A day in charge", [
    nar("note", '''{n}The note is pinned to the kiln door with a hairpin: "Gone north for the day. Back by dark. She has eaten. Do NOT feed her again, whatever she tells you. The door latch sticks. N."{/n}
{n}The kiln door is open. The latch has stuck. The young dragon is not in the kiln.{/n}''',
        c("Continue", "trail")),
    nar("trail", '''{n}She is not hard to follow. There are claw-marks up the tanners' stair, and a baker on the upper landing with an empty tray and a look of religious awe, and a trail of flour through the square, past the jeweller, who has shut his shutters, and up the citadel steps, past two guards who have decided, as one man, that they did not see anything.{/n}
{n}She is in your quarters. She is on your map table. She has eaten the northern third of the Worldwound, in vellum, and is starting on the rift.{/n}''',
        c("Continue", "her")),
    nar("her", '''{n}She looks up at you with a strip of the Abyss hanging out of the side of her mouth, and hisses, and hunches over the rest of the map with her wings mantled, the way a cat hunches over a bird.{/n}
{n}She is a good deal too big for the table. She has a great many teeth. She has not been told she may not eat maps, and she can see no reason why she should stop.{/n}''',
        c('[Athletics: pick her up bodily and carry her out]',
          check=dict(Skill="SkillAthletics", DC=18, Success="carried", Failure="bitten", CommanderOnly=True)),
        c('[Trickery: tie a sausage from the kitchens to a string and walk it slowly out of the door]',
          check=dict(Skill="SkillThievery", DC=14, Success="sausage", Failure="sausage_lost", CommanderOnly=True)),
        c("[Sit down on the floor and wait for her to finish.]", "wait")),
    nar("carried", '''{n}She weighs about as much as a sack of wet sand and fights like a sack of wet cats. You get her off the table and under one arm, with her tail round your neck and her claws in your coat, and you carry her down the citadel steps past the guards, who continue not to see anything, and down through the square, hissing all the way.{/n}''',
        c("Continue", "dark")),
    nar("bitten", '''{n}You get your arms round her. She gets her teeth round your forearm. Neither of you lets go. You carry her down the citadel steps like that, past the guards, who continue not to see anything, with blood running into your sleeve and her growling steadily round a mouthful of your arm, all the way to the kiln.{/n}''',
        c("Continue", "dark", flags=(P + "bitten_by_her",))),
    nar("sausage", '''{n}She sees the sausage. She forgets the map. The sausage goes slowly across the floor, and out of the door, and down the stair, one step at a time, and she goes after it, stalking it with enormous seriousness, belly to the flagstones, tail lashing; and you walk backward down the citadel steps and through the square and down the tanners' stair with a string in your hand and a dragon hunting a sausage at the end of it, in front of half of Drezen.{/n}''',
        c("Continue", "dark")),
    nar("sausage_lost", '''{n}She sees the sausage. She considers the sausage. Then she lunges, faster than anything should be able to move at that size, and the sausage is gone, and the string, and very nearly the end of your finger, and she sits back on the map table licking her teeth and waiting to see what else you will produce.{/n}
{n}In the end you carry her, and she lets you, because she is full.{/n}''',
        c("Continue", "dark")),
    nar("wait", '''{n}You sit on the floor with your back to the wall. She eats the rift. She eats the Ivory Sanctum and Drezen and most of Mendev, with great thoroughness, watching you over the edge of the table the whole time, and when there is nothing left but the corners she climbs down, and walks across the floor, and lies down against your leg, heavily, hot as a brick out of an oven, and goes to sleep.{/n}
{n}You stay there until she wakes, hours later, stretches, and lets you carry her home to the kiln without a fight.{/n}''',
        c("Continue", "dark")),
    nd("dark", '''{n}She is back before dark, as she said, with snow on her sheepskin and a brace of hares over her shoulder. She takes in the kiln, and the young dragon asleep in it, and flour, and vellum, and you, and her face does several things one after another.{/n} "She got out."
"She ate your maps. I can see the Worldwound on her chin." {n}She sits down on the step, suddenly, and laughs until she has to hold her ribs.{/n} "Oh, I'm sorry. I'm not sorry. Did she eat the rift? Tell me she ate the rift."''',
        c('"She ate the rift."', "rift"),
        c('"She ate Mendev."', "rift")),
    nd("rift", '''{n}She wipes her eyes.{/n} "Good girl." {n}Then, more quietly, looking at the kiln:{/n} "You didn't go for a sword. You didn't send for a sergeant with a net. You went and fetched her yourself." {n}She turns her head and looks at you, and her face is warm, and a little rueful.{/n} "I'll fix the latch. And I'll pay for the maps. In barley, mostly. It's all I've got."''',
        c("[Accept the barley.]", flags=(P + "in_charge_done",))),
], requires=(RENOUNCED, HATCHED), forbids=(P + "in_charge_done", LIE_KEPT), delay=48, optional=True)
