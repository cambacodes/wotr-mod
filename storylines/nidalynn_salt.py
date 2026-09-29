"""Nidalynn, from her own face to the snowfield: the chosen form, the first flight, the salt and the ridge.

11 §2: she proposes when the hatchling first flies; bread and salt, Reudger's rite, is the yes (no test before it, no
second ask, no price). Eating is the Commander's yes; the heel of the loaf left on the kiln shelf is the Commander's
not-yet, and it keeps; "No" closes. Nothing romantic or physical is ever staged while she wears the widow: the chosen
form comes first (door.own_form), and every scene after it is hers. The intimacy is a snowfield under the north peak
above Drezen, under the stars; she flies the Commander up as a silver dragon and takes her own form in the snow.

Must acknowledge (11 §2): Devarra (the bill, in her voice, never on the page with her), Ulbrig (who knew the Windstep),
the druids (she was one), the clutch.
"""
from story_format import c, scene
from storylines.nidalynn_trickster import (
    CLAIMED, CLOSED, COMMITTED, DV_BILL, DV_HUNTING, DV_RETURNED, FED_DEMONS, FED_GOATS, FED_RATS, FIRST_DEMON, FORM,
    HAND_SET, HATCHED, KISSED, LEFT_WITH_IT, LIE_KEPT, MET, NAME_NONE, NAME_PEBBLE, NAME_SOOT, P, PROPOSED, BREAD_KEPT, REFUSED, RENOUNCED,
    SALT, SNOW, nar, nd)
from storylines.nidalynn_trickster import steps as _steps, visit as _visit
from storylines.nidalynn_kiln import CLAIM_KEPT, TORCS

SCENES = []


def steps(*args, **kw):
    _steps(*args, into=SCENES, **kw)


def visit(*args, **kw):
    _visit(*args, into=SCENES, **kw)


OWN_FORM = P + "door.own_form"
WOMEN = P + "steps.the_widows_time"
WINGS = P + "wall.wings"
FLIGHT = P + "ridge.first_flight"
HEEL = P + "kiln.the_heel"
SNOWFIELD = P + "ridge.snowfield"
BACK = P + "door.home_from_the_dark"
LONG_NIGHT = P + "kiln.long_night"


# --- 1. Her own face (she comes to the Commander's door): the widow is put off -----------------------------------------

visit(OWN_FORM, "Her own face", [
    nar("door", '''{n}Your steward comes in to say there is a woman at the door who will not give her name, and that she has brought soup.{/n}
{n}You do not know her. She is tall, taller than you, and straight-backed, and somewhere past thirty in the way that a good blade is somewhere past new. Her hair is white, not grey, the white of salt or snow, in a thick braid over one shoulder. She wears a plain blue wool dress with the sleeves rolled, and a sheepskin over it, and she is holding a covered pot against her hip. There is no belly.{/n}
{n}Then she looks at you, and her eyes are pale grey with no brown in them at all.{/n}''',
        c("Continue", "soup")),
    nd("soup", '''"Well, don't stand there with your mouth open; take the pot. It's hot, and I've carried it up four flights." {n}It is the same voice. It is not the widow's voice at all: lower, easier, with a laugh folded up inside it somewhere.{/n} "Barley and mutton. The little one ate the rest of the mutton, so it's mostly barley."''',
        c('"Nidalynn?"', "yes"),
        c('"Where\'s the belly?"', "belly")),
    nd("yes", '''"Who else brings you soup?" {n}She comes in past you and puts the pot on your map table, on top of the map, without asking.{/n} "Don't answer that either. I know who brings you soup. I've been sitting on a step opposite your door for a season."''',
        c("Continue", "why")),
    nd("belly", '''"Retired." {n}She comes in past you and puts the pot on your map table, on top of the map, without asking.{/n} "It had a long and honourable career. The women on the step are very upset; they'd knitted it a blanket. I told Old Anka the truth, the eldest of them, and she said she'd known since the autumn, because nobody carries that high for four months, and then she gave me the blanket anyway."''',
        c("Continue", "why")),
    nd("why", '''{n}She turns round, with her back to your map table and her hands braced on its edge, and lets you look at her. She does not make it easy, and she does not make it hard. She simply stands there, as herself, and lets it happen.{/n}
"I said you'd know when I wanted to be looked at as myself. That you wouldn't have to ask." {n}Her chin comes up a little.{/n} "This is the shape I'd choose, if nobody needed me to be anything. I've worn it before, now and then, when I was somewhere I meant to stay. I wore it at Reudger's fire."''',
        c('"You\'re beautiful."', "beautiful"),
        c('"Why now?"', "now"),
        c("[Say nothing. Look at her.]", "look")),
    nd("beautiful", '''"I know." {n}It is not vanity. It is the tone of a woman agreeing that the soup is hot.{/n} "I made it, didn't I? I'd be a poor sort of dragon if I made myself a face I didn't like." {n}Then, lower, and not quite as easily:{/n} "But thank you. It's a different thing to hear it said."''',
        c("Continue", "now")),
    nd("look", '''{n}You look. She lets you. After a while the corner of her mouth goes up.{/n} "Thorough. That's a trickster for you. Checking the seams." {n}She holds out one arm, turning it over, as she did in your quarters that first night. It stays an arm.{/n} "No scales. No belly. Only me."''',
        c("Continue", "now")),
    nd("now", '''"Now?" {n}She considers it, chewing.{/n} "Now I go back to my kiln, and the little one goes back to eating the undercroft, and you go back to your war. I'm not going to sit in your citadel and be looked at by your generals. I'll keep my kiln and my step. Come when you like, and come hungry; I'll know if you've eaten in the citadel first, and I'll be offended."
{n}She looks at you sidelong, over the bread.{/n} "And don't ever lie to me about anything you love. The salt won't stand for it. Neither will I."''',
        c("Continue", "mother", requires=(DV_RETURNED,)),
        c("Continue", "eat", forbids=(DV_RETURNED,))),
    nd("mother", '''"And there's a grey dragon on the ridge above your city who comes down at night and lies on the east wall and looks at my kiln." {n}Her voice does not change.{/n} "She hasn't come closer. She won't, while I'm in it. I'm not afraid of her; I'm older than she is, and I'm not the one who stole from her. But I thought you should hear it from me, in this face, and not from your sentries."''',
        c("Continue", "eat")),
    nd("eat", '''"Now eat the soup, before it goes cold and I have to be the widow again to make you." {n}She sits down in your chair, the good one, and crosses her legs, and looks, now, very slightly unsure of herself, as if she had rehearsed everything up to this point and nothing after it.{/n}''',
        c("[Eat the soup, and let her watch you do it.]", "end"),
        c("[Put the soup down and go to her.]", "near")),
    nd("near", '''{n}She puts up one hand, flat against your chest, before you are quite close enough, and holds you there. Not pushing. Holding.{/n} "Soup first." {n}Her eyes are laughing, and not only laughing.{/n} "I've waited a season on a step. I can wait for you to eat. So can you."''',
        c("[Eat the soup.]", "end")),
    nd("end", '''{n}You eat. She watches you do it with the deep satisfaction of a woman who has fed somebody properly, and when you have finished she takes the pot back and tucks it under her arm.{/n}
"There. The step, tomorrow, if you want me. It's the same step. It's a different woman on it." {n}At the door she stops.{/n} "And if the sergeant with the squint calls me 'mother', I shall bite him."''',
        c("[Watch her go.]", flags=(FORM,))),
], requires=(RENOUNCED, HATCHED), forbids=(FORM,), delay=24)


# --- 2. The widow's time (optional, her own step): what she told the women --------------------------------------------

steps(WOMEN, "The widow's time", '"The women on the next step are staring at you."', [
    nd("start", '''"They're staring at you." {n}She takes another bite of her apple.{/n} "They've decided you're the reason the widow went away. Old Anka's put it about that the widow's man came back from the dead, and was a crusader, and took her off to Mendev to have the child in a proper bed. They've half convinced themselves it was you."
"I didn't tell them that. I told Anka the truth. Anka told the rest of them a better story, because she's a Kellid and a Kellid would rather die than tell a story straight."''',
        c('"Does it bother you?"', "bother"),
        c('"Am I supposed to be the dead crusader?"', "crusader")),
    nd("crusader", '''"You're supposed to be a great many things, to hear them tell it. Tall. Handsome. Unfaithful. Very bad at writing letters." {n}She smiles at the apple.{/n} "I'd say they've got one of those right."''',
        c("Continue", "bother")),
    nd("bother", '''"No." {n}She thinks about it properly before she says it.{/n} "It's their story now. They made it out of what they had, the way the Windstep made cheese out of mare's milk because that's what there was. It's a kind story. Nobody in it is a fool, and nobody's left on a step."
"And they still feed me. They feed me more, now. They say I'm too thin since the widow went." {n}She holds up the apple, which she did not buy.{/n} "You see? A costume isn't the only way to be looked after. It's only the quickest."''',
        c("Continue", "torc", requires=(TORCS,)),
        c("Continue", "end", forbids=(TORCS,))),
    nd("torc", '''{n}She nods across the square. The Kellid girl from the jeweller's is there, at a water-trough, and she is wearing the hare torc, or she is not, and either way she lifts her chin at the white-haired woman on the step, the way you greet somebody from your own fell.{/n}
"She doesn't know who I am. She knows I'm the one who knew her great-great-grandmother's name. That's enough, for a girl with no clan left. It's a great deal."''',
        c("Continue", "end")),
    nd("end", '''"Sit a while. The women want to look at you, and I want them to have a good look, so they'll stop asking me." {n}She moves over on the step, and it is not a wide step, and she does not move over very far.{/n}''',
        c("[Sit down beside her.]")),
], requires=(FORM,), forbids=(WOMEN,), delay=24, chosen=True, optional=True)


# --- 3. Wings (the east wall above the kiln): the hatchling tries the air; the first kiss --------------------------------

visit(WINGS, "Wings", [
    nar("wall", '''{n}She is on the east wall above the kiln, at dusk, sitting on the parapet with her legs over the drop and a sheepskin round her shoulders. Below, on the kiln roof, the young dragon is learning her wings.{/n}
{n}She is the size of a pony now. She runs the length of the roof-ridge with her wings out and her neck stretched, and at the end of the ridge she jumps, and for one moment she is in the air, and then she is not, and there is a crash in the lane below and a great deal of furious hissing, and a soldier somewhere laughs, and stops laughing.{/n}''',
        c("Continue", "watch")),
    nd("watch", '''"Eleven times today." {n}Nidalynn does not take her eyes off the lane.{/n} "She won't let me help. She bit me for trying. She's right; you have to do it yourself or it doesn't count, the first time." {n}The young dragon climbs back up the kiln wall by her claws, dragging one wing, and goes to the end of the ridge again.{/n} "Sit down. You'll make her nervous. She thinks you're going to take her away. She still thinks that, you know. Children remember."''',
        c("[Sit beside her on the parapet.]", "sit")),
    nar("sit", '''{n}You sit. The stone is cold. She is not; you can feel it through the sheepskin where her shoulder is against yours, a steady warmth like a banked hearth, far more than the evening should allow.{/n}
{n}Down on the roof the young dragon spreads her wings, and folds them, and spreads them.{/n}''',
        c("Continue", "run")),
    nd("run", '''"I remember the first time I flew." {n}She says it quietly, as if to herself.{/n} "Off a cliff over the sea, a long way from here, with my mother shouting at me from the rocks. I didn't know how. I only knew that I'd rather fall than stand on that cliff another day." {n}She laughs under her breath.{/n} "I fell. A long way. Then I didn't."''',
        c('"Were you afraid?"', "afraid"),
        c('"Your mother pushed you?"', "mother")),
    nd("mother", '''"Silver mothers don't push. They shout. It's worse." {n}Her mouth twitches.{/n} "She'd have liked you. She liked anyone who could make her laugh when she was angry. There weren't many."''',
        c("Continue", "afraid")),
    nd("afraid", '''"Terrified." {n}She turns her head and looks at you, and her face is very close, and very still.{/n} "It's the same now. I'm old, and I've flown over half the world, and I'm sitting on a wall with my heart going like that little one's, because I've decided something and I haven't said it yet."''',
        c('"Then say it."', "say"),
        c("[Kiss her.]", "kiss")),
    nd("say", '''"No." {n}She says it softly.{/n} "Some things you say. Some things you do." {n}And she leans the last little distance, and does.{/n}''',
        c("Continue", "kissed")),
    nar("kiss", '''{n}She meets you halfway. She does not hurry. She has never hurried anything in her life, you think, and she does not start now: it is a slow kiss, and a thorough one, and it tastes of cold air and the apple she was eating on the step, and when her hand comes up to the back of your neck it is warm, and it stays.{/n}''',
        c("Continue", "kissed")),
    nar("kissed", '''{n}There is a crash below, and a shriek, and a sound that neither of you has heard before: a great ragged beating, like a sail in a gale.{/n}
{n}You both look down. The young dragon is not in the lane. She is above it, for three heartbeats, four, five, labouring and lopsided and furious, a hand's breadth off the cobbles; and then she comes down again on the kiln roof, hard, and sits there with her wings half open, astonished.{/n}''',
        c("Continue", "almost")),
    nd("almost", '''{n}Nidalynn has hold of your arm hard enough to bruise.{/n} "Five. That was five. She held it for five." {n}She is laughing, and her eyes are wet.{/n} "She'll do it properly soon. A day, a week. When she does, I've something to say to you. Something I'll do. Not before."
{n}She lets go of your arm, and then, after a moment's thought, takes your hand instead, and keeps it, and goes back to watching the roof.{/n}''',
        c("[Watch the roof with her until it's too dark to see.]", flags=(KISSED,))),
], requires=(FORM,), forbids=(KISSED,), delay=24)


# --- 4. The first flight (Chapter 5): she proposes; bread and salt is the yes (the commit) --------------------------------

visit(FLIGHT, "Salt on bread", [
    nar("boy", '''{n}It is the sergeant with the squint who comes for you this time, not a refugee boy, and he does not knock; he comes straight in, out of breath and grinning like a fool.{/n} "Commander. The little mother. She's up. She's up, and she's not coming down."
{n}From the citadel steps you can see her: a red-black shape over the lower town, very high, turning in long uneven circles against a hard blue winter sky, and every face in Drezen turned up to watch.{/n}''',
        c("Continue", "kiln")),
    nar("kiln", '''{n}By the time you reach the kiln the young dragon has come down again, onto the roof, where she is stalking up and down the ridge with her wings still half open, too proud to fold them. The sergeant's men are cheering from the lane. Somebody has brought a drum.{/n}
{n}Nidalynn is not cheering. She is standing in the kiln's mouth in her own shape, with her sleeves rolled and her braid pinned up, looking up at the roof, and she has the face of a woman watching a ship come home.{/n}''',
        c("Continue", "table")),
    nar("table", '''{n}When she sees you she goes inside without a word, and you follow her.{/n}
{n}Inside, in the heat, on the bricks by the kiln's mouth, she has laid out a cloth. On the cloth is a round loaf, dark, still warm, and a knife, and a small cake of something greyish-white, rough, the size of a child's fist, worn smooth on one side, as if something had licked it for a long time.{/n}''',
        c("Continue", "salt")),
    nd("salt", '''"It's salt. From the lick-stone at Reudger's summer pasture, where his mares came to lick it." {n}She sits down on her heels by the cloth and touches it with one finger.{/n} "The last piece. I took it the year the Wound opened, when I came back and there was nothing on the grass. I've carried it a hundred years. I never found anyone to break it for."
"Reudger gave me bread and salt the first night I came to his fire. It was his way of saying 'of my fire'. Not the clan's; his. You don't say it with your mouth. You say it with salt, and the other one says yes by eating it."''',
        c("Continue", "ask")),
    nd("ask", '''{n}She picks up the knife and cuts the heel off the loaf, and holds the salt over it, and breaks a piece off the edge of the cake between her thumb and forefinger. It takes some doing. It has been a stone for a long time.{/n}
"I'm not asking you to be anybody's husband, or wife, or to swear anything to a priest. I'm too old for priests." {n}She crumbles the salt over the bread.{/n} "I'm asking you to be of my fire. Mine, and hers, as long as the salt's in your blood. And it doesn't go out. So."''',
        c("Continue", "held", requires=(HAND_SET,)),
        c("Continue", "offer", forbids=(HAND_SET,))),
    nd("held", '''{n}She takes your hand, the one she mended, and turns it palm up and puts the bread in it.{/n} "I set that hand. I'd like to see it close on something worth holding."''',
        c("Continue", "offer")),
    nd("offer", '''{n}She holds it out to you, the heel of the dark loaf with the old salt on it, on her open palm, and waits.{/n}
{n}She is not smiling now. Her face is quite calm, and her hand is quite steady, and on the kiln roof above you the young dragon has started to sing, badly, the way young dragons sing, a long rising shriek at the sky that makes the lane's dogs howl.{/n}''',
        c("[Take the bread and salt, and eat.]", "yes", flags=(COMMITTED, SALT, PROPOSED)),
        c('"Not yet. Keep it for me. I\'ll come back for it."', "not_yet", flags=(BREAD_KEPT, PROPOSED)),
        c('"No. I can\'t be of anyone\'s fire."', "no", flags=(REFUSED, PROPOSED, CLOSED))),
    nar("yes", '''{n}It is hard and dark and sour, the way rye bread is, and the salt is very old and very sharp and tastes of nothing but salt, and of stone, and faintly, underneath, of grass. You eat all of it.{/n}
{n}She watches you do it. When you have swallowed the last of it she lets out a breath that she seems to have been holding for a hundred years, and it frosts the air between you, even here in the heat of the kiln.{/n}''',
        c("Continue", "yes2")),
    nd("yes2", '''"There." {n}She breaks a second piece off the cake, puts it on the heel of her own bread, and eats it, slowly, with her eyes shut.{/n} "Now we're both of the same fire. Reudger would laugh himself sick. A trickster and a silver, at a lime-kiln."
{n}She opens her eyes. There is nothing calm in them any more.{/n} "Tonight, when the moon's down. Come to the lane with nothing in your hands. I want to show you where I go when I want to be alone. I've never taken anyone."''',
        c('"Tonight."')),
    nd("not_yet", '''{n}She does not close her hand. She looks at the bread on her palm for a while, and then she wraps it in a corner of the cloth, carefully, the way she wraps everything, and puts it on the shelf above the kiln's mouth where the heat will keep it dry.{/n}
"It keeps. Salt keeps; that's what it's for." {n}Her voice is quite even.{/n} "It'll be on that shelf. I won't ask you again; that's not how it's done. You'll come and eat it, or you won't, and either way I'll know what you meant." {n}She looks up at the roof, where the young dragon is still singing.{/n} "Go on. Go and cheer her. She'll want you to have seen."''',
        c("[Go out and cheer.]")),
    nd("no", '''{n}She closes her hand on the bread, slowly, until the crust cracks.{/n}
"Then you can't." {n}There is no anger in it at all, which is worse than anger.{/n} "That's an answer, and you gave it to my face, in my own fire. I'd rather that than a kind lie." {n}She stands up, and puts the salt back in the fold of her sleeve.{/n} "She'll fly north with me at the thaw. There's snow in the north, and nobody to tell stories about her." {n}At the kiln's mouth she stops, with her back to you.{/n} "Thank you for her. I mean it. I'll always mean it."''',
        c("[Leave her to the fire.]")),
], requires=(KISSED, RENOUNCED, HATCHED), forbids=(PROPOSED, COMMITTED), delay=48, chapters=(5, 5))


# --- 5. The heel (Chapter 5, after "not yet"): the loaf keeps; the Commander comes back for it ------------------------

visit(HEEL, "The heel of the loaf", [
    nar("shelf", '''{n}The loaf on the shelf above the kiln's mouth has gone hard as a brick, and the cloth round it has gone grey with lime-dust. Nobody has moved it. You can tell nobody has moved it; the dust lies the same way on the shelf all round.{/n}
{n}She is at the fire, feeding it, in her own shape, with her braid down her back. She knows you have come in. She does not turn round.{/n}''',
        c("Continue", "wait")),
    nd("wait", '''"The little one caught a hare in the fells yesterday. Her first. She brought it back and dropped it at the kiln door and sat there until I'd said how clever she was three times." {n}She puts another log on.{/n} "Then she ate it in front of me, very slowly, so I'd know it wasn't for me."''',
        c("[Take the heel down from the shelf, and unwrap it, and eat it.]", "eat", flags=(COMMITTED, SALT)),
        c("[Sit by the fire with her, and leave the shelf alone tonight.]", "sit")),
    nar("eat", '''{n}It is stone-hard, and you have to break it with the heel of your hand on the brick, and the salt on it has crusted into the crumb. It hurts your teeth. You eat all of it anyway.{/n}
{n}She has stopped feeding the fire. She is standing very still, with a log in her hands, listening to you chew.{/n}''',
        c("Continue", "turned")),
    nd("turned", '''{n}She puts the log down and turns round, and she is smiling and weeping at once, which you would not have thought a dragon's face could do.{/n} "You broke a tooth on it. I heard." {n}She comes and takes your face in both hands and turns it to the firelight, to look.{/n} "Idiot. You could have soaked it. Any child of the grass could have told you." {n}Then she stops looking at your teeth.{/n}
"Tonight, when the moon's down. Come to the lane with nothing in your hands."''',
        c('"Tonight."')),
    nd("sit", '''{n}You sit on the lime sack. After a while she sits down beside you, close, because it is still the only dry seat, and hands you half a loaf out of her basket: new bread, soft, with nothing on it.{/n}
"Eat. That's only bread." {n}She watches you eat it, and the loaf on the shelf stays where it is, and neither of you looks at it.{/n}''',
        c("[Stay until the fire's low.]", abort=True)),
], requires=(BREAD_KEPT,), forbids=(COMMITTED,), delay=72, chapters=(5, 5))


# --- 6. The snowfield (after the yes): she flies the Commander to the north peak, in her own form -----------------------

visit(SNOWFIELD, "Where the snow stays", [
    nar("lane", '''{n}The moon is down. The lane below the kiln is black, and the kiln's mouth is a red eye in it, and she is standing in the middle of the cobbles in her own shape with her braid undone and her feet bare on the frost.{/n}
{n}"Stand back," she says. "Further. Further than that. I'm bigger than you'd think."{/n}''',
        c("Continue", "change")),
    nar("change", '''{n}It is not like the arm in your quarters. It is not fine or fast. It is like watching weather come in over a mountain: the dark filling, and filling, and going on filling long after you think it must stop.{/n}
{n}When it stops, the lane is full of her. Silver from end to end, scale on scale like the links of a hauberk made for a giant, with a crest of horns laid back along her skull and a wing folded against the kiln wall that would roof half the lower town. Her breath comes out of her in a long cold plume and hangs in the air, and the frost on the cobbles thickens where it falls.{/n}
{n}The eyes are the same. Pale grey. No brown at all. They look down at you from a great height, and they are laughing.{/n}''',
        c("Continue", "climb")),
    nd("climb", '''{n}Her voice is the same too, only bigger, as if it were coming up out of a well.{/n} "Well, go on. Up the foreleg, and sit where the neck meets the shoulders, and hold on to the crest. Don't kick. I'm not a horse. The Windstep children never kicked."''',
        c("[Climb up.]", "fly")),
    nar("fly", '''{n}You climb. She is cold under your hands, cold as a mail shirt left out overnight, and under the cold, a long way down, something vast and warm is beating.{/n}
{n}She does not warn you. The wings open, and the lane drops away beneath you so fast that your stomach stays in it, and Drezen is below you, a spill of lamps and smoke and walls, and then it is small, and then it is behind you, and there is nothing in front of you but the dark and the white shoulders of the mountains and more stars than you have ever seen in your life.{/n}
{n}It is so cold that you stop being able to feel your face. You do not care. You do not care about anything. You are laughing, and the wind takes the laughter and throws it away.{/n}''',
        c("Continue", "field")),
    nar("field", '''{n}She comes down on a snowfield high under the north peak, higher than the old watchtower's ridge, higher than anything you can see; a long white slope that has not had a footprint on it all winter. Far below, Drezen is a smudge of orange in the dark. The Worldwound is a stain along the northern sky. Up here it is very small.{/n}
{n}You slide off her shoulder into snow to the knee, and when you turn round she is already a woman again, standing barefoot in the snow in the blue dress, with her white hair loose to her waist and the snow not melting under her feet.{/n}''',
        c("Continue", "cold")),
    nd("cold", '''"This is where I come when I want to be alone." {n}Her breath does not steam. Yours does, in great ragged clouds; your teeth are going like a drum.{/n} "I've never brought anyone. I've never wanted anyone here." {n}She looks at you shaking, and her face does something soft and wicked at once.{/n} "Oh. Oh, you poor warmblood. You're freezing."''',
        c('"You could have mentioned the cold."', "mention"),
        c("[Go to her.]", "go")),
    nd("mention", '''"I could." {n}She is already coming toward you through the snow, which parts round her ankles and does not seem to touch her.{/n} "I wanted to see if you'd come anyway. You did."''',
        c("Continue", "go")),
    nar("go", '''{n}She opens the sheepskin she has carried up in one claw, and puts it round you both, and pulls you in against her, and she is warm. Not a little warm. Warm like a hearth, like a banked kiln, like the heart of the thing that flew you here; the heat comes off her through the thin wool of the dress and into you, and your teeth stop.{/n}
{n}She holds you like that for a while, with her chin on your hair, and does nothing else at all. She is in no hurry. She has never been in a hurry. Your hands, when they can feel again, find the laces at the back of the blue dress, and she goes still.{/n}''',
        c("Continue", "slow")),
    nd("slow", '''"Slowly." {n}It is barely a word. Her mouth is at your temple.{/n} "I've waited a very long time to be hungry for anything, and I mean to take my time over it." {n}She tips her head back to look at you, and her eyes are not calm now, not any of the long patience in them, only want, plain and bright and nowhere near old.{/n} "Slowly. And be grateful."''',
        c("[Undo the laces, one at a time.]", "laces")),
    nar("laces", '''{n}One at a time. She lets you. The dress comes off her shoulders and down, and she steps out of it into the snow as if it were a warm floor, and stands there under more stars than there are names for, in nothing but her white hair, and lets you look, as she did in your quarters: without shame, without hurry, as herself.{/n}
{n}There is no scale on her now. There is a long body, strong through the shoulder and the thigh, pale as the snowfield, warm as the kiln, with a little silver at the hollows of her collarbones where the light catches, like frost that has decided to stay.{/n}
{n}Then she is undoing your coat, and she is less patient about your laces than you were about hers.{/n}''',
        c("Continue", "down")),
    nar("down", '''{n}The cold comes in where your clothes go, and she follows it with her hands, and wherever her hands go the cold stops. She laughs into your mouth when you gasp at the snow on your back; she does not let you up. She is heavier than she looks, and very much stronger, and she presses you down into the snowfield with the sheepskin under you and her hair falling round both your faces like a tent of white silk.{/n}
{n}Her mouth is slow. Her hands are slow. The snow under you is soft, and the stars over her shoulder go on and on, and her breath, which never steams, is the only warm thing on the whole mountain, and it is on your throat.{/n}''',
        c('"Nidalynn."', "want"),
        c("[Pull her closer.]", "want")),
    nd("want", '''{n}She lifts her head. Her hair falls round your face, and her eyes in the starlight are not grey at all now; they have silver in them, all the way through.{/n} "Four hundred winters I've watched you warm-blooded things want each other, and wondered what the fuss was." {n}Her voice is low and rough and perfectly unashamed.{/n} "I know now. I want you. All of you, here, in my snow, and I'm not going to be quick about it, and I'm not going to be polite."''',
        c('"Then don\'t be."', "cut"),
        c("[Answer her with your hands.]", "cut")),
    nar("cut", '''{n}She laughs, low in her chest, and comes over you in one long movement, a knee in the snow on either side of you and the sheepskin sliding off her shoulders, her weight settling onto you, warm as a banked kiln. Her hands take your wrists and press them down into the snow above your head, not hard, only so that you know who is holding whom. She looks down at you, all of her, white hair and starlight and want.{/n}
{n}Then she bends down to you, slowly, the way she does everything, and her mouth finds yours, and the snowfield takes you both.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}Grey light on the snowfield. Your eyelashes have frozen together, and when you get them open the first thing you see is a red-black face, upside down, with a great many teeth in it, a hand's breadth from your own.{/n}
{n}The young dragon has found you. She is standing on your chest, which hurts, looking down at you with an expression of enormous disapproval, and every time you breathe she rises and falls.{/n}''',
        c("Continue", "found")),
    nd("found", '''"She followed us." {n}Nidalynn's voice is lazy and warm and somewhere behind your head, and you realise that you are lying against her, under the sheepskin, and that she has not put the dress back on.{/n} "All the way up. In the dark. On her third real flight." {n}She sounds indecently proud.{/n} "She's been sitting on the snow over there since the stars went, sulking. She doesn't approve of you."''',
        c('"She\'s standing on me."', "standing"),
        c("[Scratch the young dragon under the jaw.]", "scratch")),
    nd("standing", '''"She is. It's a great honour." {n}She reaches up past your head and taps the young dragon on the snout, once.{/n} "Off. Off, madam. You'll crack a rib and then who'll feed you?" {n}The young dragon considers this, and gets off, slowly, making it clear that it was her own idea.{/n}''',
        c("Continue", "breakfast")),
    nd("scratch", '''{n}The young dragon goes rigid with outrage. Then, very slowly, her eyes half close, and she leans her jaw into your fingers, and a sound comes out of her like a kettle beginning to think about boiling.{/n}
{n}Behind you, Nidalynn laughs so hard the sheepskin shakes.{/n} "Traitor. Seven weeks I've been scratching her. One night on a mountain and she's anybody's."''',
        c("Continue", "breakfast")),
    nd("breakfast", '''{n}She sits up, and the cold comes back into the sheepskin where she was, and she pulls her dress over her head without hurry and reaches for the bag she brought up in her other claw. Bread. The cake of old salt, wrapped in its cloth. A flask of something that turns out to be hot, and tastes of honey and pine.{/n}
"Eat. You're half frozen, and you'll need your strength for the walk down; I'm not flying you home in daylight in front of the whole city." {n}She breaks the bread, and puts a crumb of the salt on your piece, and a crumb on hers.{/n} "There. Every morning, as long as there's any left. Then we'll find more."''',
        c('"What happens now?"', "now")),
    nd("now", '''"Now?" {n}She considers it, chewing.{/n} "Now I go back to my kiln, and the little one goes back to eating the undercroft, and you go back to your war. I'm not going to sit in your citadel and be looked at by your generals. I'll keep my kiln and my step. Come when you like. Bring whoever's hungry; I've never turned anyone from my fire who came to it hungry, and I'm not going to start for you."
{n}She looks at you sidelong, over the bread.{/n} "And don't ever lie to me about anything you love. The salt won't stand for it. Neither will I."''',
        c("Continue", "down_the_hill")),
    nar("down_the_hill", '''{n}You walk down. It takes half the morning, with the young dragon flying ahead and coming back to shriek at you for being slow, and Nidalynn walking barefoot beside you through the snow in her blue dress, and your hand in hers. By the time you reach the tanners' stair half of Drezen has seen you, and the other half has heard.{/n}
{n}The sergeant with the squint is on the kiln door. He looks at you, and at her, and at the frost still in your hair, and says, "Commander," with the most perfectly straight face you have ever seen on a soldier, and opens the door.{/n}''',
        c("[Go in out of the cold.]", flags=(SNOW,))),
], requires=(COMMITTED,), forbids=(SNOW,), delay=12, chapters=(5, 5))


# --- 7. The first demon (Chapter 5, after the snowfield): what she hunts, and what the household will be to her ----------

visit(FIRST_DEMON, "What she hunts", [
    nar("wall", '''{n}A dretch came over the east wall in the night, one of the stragglers that still come down out of the Wound on the wind. The sentries did not see it until it was on the walk. The young dragon did.{/n}
{n}What is left of it is lying in the lane below the kiln, in several pieces, and the young dragon is sitting beside the pieces with her tail curled round her feet, not eating them. She is waiting for somebody to come and see.{/n}''',
        c("Continue", "her")),
    nd("her", '''{n}Nidalynn is on the kiln step with her arms folded and her braid down her back, and she has the face of a woman who is proud of her child and does not intend to show it until the child is out of earshot.{/n} "She won't eat it. She killed it, and then she spat it out, and then she sat down and waited for you." {n}Her mouth twitches.{/n} "Go on. She won't budge until you've said something."''',
        c("[Tell the young dragon she did well.]", "well"),
        c("[Crouch down, and look at the dretch, and then at her.]", "look")),
    nar("well", '''{n}The young dragon looks at you. Then she picks up the dretch's head in her jaws, very carefully, walks across the lane, and drops it on your boot.{/n}''',
        c("Continue", "fed")),
    nar("look", '''{n}The young dragon watches you look. When you look up at her she lifts her head, very high, the way the chaplain lifts his when he is about to say something about Iomedae, and makes a small, satisfied noise.{/n}''',
        c("Continue", "fed")),
    nd("fed", '''"That's for you." {n}Nidalynn is laughing silently on the step.{/n} "A dragon's first kill goes to the one she thinks is the head of the house. I rather thought it'd be me."''',
        c("Continue", "demons", requires=(FED_DEMONS,)),
        c("Continue", "goats", requires=(FED_GOATS,)),
        c("Continue", "rats", requires=(FED_RATS,)),
        c("Continue", "house", forbids=(FED_DEMONS, FED_GOATS, FED_RATS))),
    nd("demons", '''"She's been eating what the provosts bring back from the rift since she was the size of a cat, and she hates it, and she eats it anyway." {n}She looks at the pieces in the lane.{/n} "And now she won't eat one she killed herself. She knows what it is. You did that, when you chose. I didn't like it, and it was right."''',
        c("Continue", "house")),
    nd("goats", '''"She's been raised on your goats, and now she won't eat a demon. She doesn't think it's food." {n}She looks at the pieces in the lane with satisfaction.{/n} "She thinks it's vermin. That's the right thing for a dragon of this city to think."''',
        c("Continue", "house")),
    nd("rats", '''"She's been clearing your undercroft since she hatched. She thinks this is just a big rat." {n}She looks at the pieces in the lane.{/n} "She's not wrong. She's a housekeeper, Commander. You made a housekeeper out of a woundwyrm. I've been alive a long time and I've never seen anything like it."''',
        c("Continue", "house")),
    nd("house", '''"The head of the house." {n}She says it again, as if testing it for weight.{/n} "I've been thinking about that. About what a house is, with you in it." {n}She makes room for you on the step.{/n}
"I'll tell you how it is with me, since you'll want to know. I'm of your fire. That's salt; it doesn't go out, and I'll not pretend it does when it's inconvenient. What I ask of you is the same as I asked on the snow: don't lie to me about anything you love. That's all. It's more than most people manage."''',
        c("Continue", "bill", requires=(DV_BILL,)),
        c("Continue", "druids", requires=(DV_HUNTING,), forbids=(DV_BILL,)),
        c("Continue", "end", forbids=(DV_BILL, DV_HUNTING))),
    nd("bill", '''"And the grey one's bill." {n}She does not look at the ridge, but her voice is careful.{/n} "I heard what she asked of you. A life, owed, to be named when she likes. That's a dragon's bill; I'd have written it the same." {n}She puts her hand on yours.{/n} "When she names it, you come to me first. Not to argue it. To tell me. I'll not have her collect in the dark from somebody who's eaten my salt."''',
        c("Continue", "end")),
    nd("druids", '''"And the grey one's still following the druids." {n}Her mouth thins.{/n} "My people. You pointed her at them. They're further north than she'll ever find, and they're patient, and one of them is a good deal bigger than she is." {n}She looks at you.{/n} "I haven't forgiven that. I'm not going to. I've only decided it's a smaller thing than the rest of you. Don't make me decide again."''',
        c("Continue", "end")),
    nd("end", '''{n}The young dragon has come up the lane and put her head in Nidalynn's lap, heavily, and gone to sleep there, with the dretch's blood still on her chin. Nidalynn wipes it off with a corner of her sleeve without looking, as if she has done it a thousand times, and will do it a thousand more.{/n}''',
        c("[Sit on the step with them.]", flags=(FIRST_DEMON,))),
], requires=(SNOW,), forbids=(FIRST_DEMON,), delay=48, chapters=(5, 5))


# --- 8. The claimed flight (Chapter 5): the claim kept, she flies to Nidalynn, and they go ------------------------------

visit(P + "ridge.claimed_flight", "Where she flew", [
    nar("sky", '''{n}The crusade's dragon flies on a bright hard morning, off the kiln roof, with half the garrison watching and the quartermaster's latest bill for goats still on your table.{/n}
{n}She goes up in long uneven circles over the lower town, red-black against the blue, higher and higher, and every face in Drezen is turned up to her, and yours is among them. Then she comes down.{/n}''',
        c("Continue", "down")),
    nar("down", '''{n}She comes down on the kiln step, where a woman in a widow's dress is standing with a sheepskin over her arm, and puts her head against the woman's belly, the way she has since she was the size of a cat.{/n}
{n}Nidalynn puts the sheepskin over her shoulders and looks across the lane at you. She does not look angry. She looks as though she has been expecting this for a long time and is sorry, now that it has come, that she was right.{/n}''',
        c("Continue", "go")),
    nd("go", '''"She's flown, Commander. I said she would." {n}She puts her hand on the young dragon's neck.{/n} "She's yours in every court in Mendev. I'll not argue it. I'm only going where she's going, because somebody has to feed her, and she won't let it be you."
"Thank you for the egg. I mean it. I'll always mean it." {n}The young dragon unfolds her wings.{/n} "Mind the ice on the tanners' stair."''',
        c("[Watch them go north.]", flags=(LEFT_WITH_IT, CLOSED))),
], requires=(CLAIM_KEPT,), forbids=(RENOUNCED,), delay=48, chapters=(5, 5))


# --- 9. Back from the Abyss (Chapter 5): the first night home -----------------------------------------------------------

visit(BACK, "Home from the dark", [
    nar("door", '''{n}You have been back in Drezen for half a day. You have seen the council, and the quartermaster, and a great many people who wanted to shake your hand, and you have not eaten, and you have not slept, and there is a smell of the Abyss in your clothes that no washing has touched.{/n}
{n}At dusk there is a knock at your door that is not your steward's.{/n}''',
        c("Continue", "own", requires=(FORM,)),
        c("Continue", "widow", forbids=(FORM,))),
    nar("own", '''{n}She is on the landing with a covered basket on her arm and snow on her sheepskin, tall and white-braided in her own face, and she does not wait to be asked in. She puts the basket on your table and takes your face in both hands and turns it to the lamp, the way she looked at your teeth, the way she looks at everything she means to mend.{/n}''',
        c("Continue", "look")),
    nar("widow", '''{n}She is on the landing in the widow's dress, with a covered basket on her arm and snow on her shawl, and she does not wait to be asked in. She puts the basket on your table and walks all the way round you once, slowly, the way a horse-trader walks round a horse, looking for what's lame.{/n}''',
        c("Continue", "look")),
    nd("look", '''"Thinner. Greyer. There's something wrong with your eyes; they don't sit still." {n}She lets out a breath.{/n} "But all there. I counted. I've been counting every night since you went, and I was afraid I'd lose count."
"Sit down. Eat. Don't tell me anything until you've eaten."''',
        c("[Sit, and eat.]", "eat")),
    nar("eat", '''{n}It is barley and mutton again, and black bread, and a pot of something sharp and green that she says is for the blood. She sits across from you and watches every spoonful go down with the fierce attention of a woman who has seen too many people not come back.{/n}
{n}When you have finished she takes the bowl away, and then she sits down again, and folds her hands, and waits.{/n}''',
        c("Continue", "tell")),
    nd("tell", '''"Now. What was it like?" {n}She holds up a hand.{/n} "Not the war. I'll hear the war from your generals, and they'll lie. What was it like for you, in the dark?"''',
        c('"Like a nightmare that kept its promises."', "nightmare"),
        c('"The demons laughed at my jokes. That was the worst part."', "laughed"),
        c('"I don\'t want to talk about it."', "quiet")),
    nd("nightmare", '''{n}She nods slowly, as if you had said something she recognised.{/n} "I've never been down. I've stood at the edge of it and smelled it, and that was enough to put me off my food, and nothing puts me off my food." {n}She reaches across and puts her hand over yours on the table, briefly.{/n} "You went all the way down. And you came back up and asked for soup. That's a kind of courage nobody sings about."''',
        c("Continue", "news")),
    nd("laughed", '''{n}She stares at you, and then she laughs, a real laugh, big and startled.{/n} "Oh, they would. They would." {n}She wipes her eyes.{/n} "A trickster in the Abyss. They must have thought you were one of theirs, until you weren't." {n}The laugh goes out of her face slowly.{/n} "Don't let them be the only ones who laugh at your jokes. That's how it starts. Come and tell them to me instead. I'll laugh at the bad ones too."''',
        c("Continue", "news")),
    nd("quiet", '''"Then don't." {n}She says it at once, without offence.{/n} "Some things you carry by yourself for a while before you can put them down in front of anybody. I know about that." {n}She pushes the bread across to you again.{/n} "When you want to, there's a kiln, and a step, and me. It's not going anywhere. Neither am I."''',
        c("Continue", "news")),
    nd("news", '''"Well. My news." {n}She settles back.{/n}''',
        c("Continue", "news_hatched", requires=(HATCHED,)),
        c("Continue", "news_egg", forbids=(HATCHED,))),
    nd("news_hatched", '''"She's the size of a calf, and she can't fly yet, and she thinks she can. She's been off the kiln roof nineteen times while you were gone. The sergeant's started keeping a tally on the wall in charcoal." {n}Her face softens.{/n} "She looked for you every dusk. I told her you'd come back. She didn't believe me. She's a very sensible child."''',
        c("Continue", "end")),
    nd("news_egg", '''"The egg's well. It's grown. It's not stopped knocking all winter, and the whole lower town's heard it sing." {n}She frowns.{/n} "It's waiting for something. I don't know what. They do that, sometimes, the wise ones. They wait till the house is whole."''',
        c("Continue", "end")),
    nd("end", '''{n}She gets up, and picks up her basket, and at the door she stops.{/n} "Sleep tonight. Properly. In a bed, not a chair." {n}She looks back at you.{/n} "I'll know if you don't. The laundress on the second floor tells me everything."''',
        c("[Sleep.]", flags=(BACK,))),
], requires=(MET,), forbids=(BACK, LIE_KEPT), delay=12, chapters=(5, 5))


# --- 10. The long night (after the kiss): what she's afraid of -----------------------------------------------------------

visit(LONG_NIGHT, "What a silver is afraid of", [
    nar("kiln", '''{n}The kiln is banked low tonight. The young dragon is asleep at the back of it on the warm bricks, curled round herself like a dog, twitching in dreams, now and then letting out a small wet snort of smoke.{/n}
{n}Nidalynn is sitting on the lime sack in her own face with her boots off and her feet to the embers, and she moves over for you without looking, and you sit, and for a while neither of you says anything, which is the most comfortable silence you have had in a year.{/n}''',
        c("Continue", "ask")),
    nd("ask", '''"Can I tell you a thing I've told no one?" {n}She says it to the embers.{/n} "Not a secret. Silvers are no good at secrets. A thing I'm ashamed of."''',
        c('"Tell me."', "tell"),
        c("[Put your arm round her, and wait.]", "arm")),
    nar("arm", '''{n}She leans into it, the whole long warm weight of her, as if she had been waiting for somebody to do exactly that for a very long time and had given up expecting it.{/n}''',
        c("Continue", "tell")),
    nd("tell", '''"When the Wound opened I was a long way north, off on my own business and in no hurry, because I'm never in a hurry." {n}She pokes the embers with a stick, harder than they need.{/n}
"I came back to ash. I'd not said goodbye to him. I thought there was time; there's always time, for us. That's the whole of it." {n}She holds out her hand without looking.{/n} "There. It's said. Pass me the bread."''',
        c('"He knew."', "knew"),
        c("[Say nothing. Hold on.]", "hold")),
    nd("knew", '''"You can't know that." {n}But she is listening.{/n}''',
        c('"He gave a white-haired girl his salt at his fire, and never asked her where from. He knew she\'d come back. People like that always know."', "salt")),
    nd("salt", '''{n}She does not answer for a long time. When she does, her voice has gone thick.{/n} "That's a trickster's trick. Saying the thing somebody needs to hear, and saying it so well they can't argue." {n}She wipes her face with the heel of her hand.{/n} "It's also true. I think. I'm going to decide it's true, and you're not to take it back."''',
        c("Continue", "afraid")),
    nd("hold", '''{n}She lets you. After a while her breathing evens out, and she says, in a different voice:{/n} "Thank you. For not saying something clever. I know you had one ready."''',
        c("Continue", "afraid")),
    nd("afraid", '''"So now you know what a silver's afraid of." {n}She turns her head on your shoulder and looks at you, very close.{/n} "Not demons. Not golems. Not the grey one on the ridge. Leaving somebody for two years in a temper, and coming back to ash."
"You're so short. All of you. You're here and then you're not, and I don't always notice the difference in time." {n}Her hand finds yours.{/n} "I noticed with you. I noticed the whole time you were gone."''',
        c("[Kiss her.]", "kiss"),
        c('"Then don\'t leave in a temper."', "temper")),
    nd("temper", '''{n}She laughs, wet and startled.{/n} "No. No, I'll quarrel with you here, in the kiln, where you can hear it. That's what kilns are for." {n}And then she kisses you, since you did not.{/n}''',
        c("Continue", "kiss")),
    nar("kiss", '''{n}It is not like the kiss on the wall. It is slower, and it goes on, and her hand comes up into your hair and stays there, and the embers tick, and somewhere in it she makes a small low sound that you feel through her ribs more than hear.{/n}
{n}Then she stops, and puts her forehead against yours, and breathes.{/n}''',
        c("Continue", "not_here")),
    nd("not_here", '''"Not here." {n}Her voice is not steady.{/n} "Not in a lime-kiln, on a sack, with a child at the back of it who wakes up if you drop a spoon." {n}She laughs under her breath.{/n} "I've waited longer than your grandmother's been dead, Commander. I'll not have it on a lime sack."
"When she flies. There's somewhere I'll take you. I'll not tell you where. You'd only try to guess, and you'd guess wrong, and be smug about it."''',
        c("[Stay till the embers are grey.]", flags=(LONG_NIGHT,))),
], requires=(KISSED,), forbids=(LONG_NIGHT, PROPOSED), delay=24, optional=True)
