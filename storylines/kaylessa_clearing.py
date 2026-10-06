"""Kaylessa: after the knife (kaylessa_trickster's commit).

Every scene here Requires the commit (the late yes of "Put down somewhere" counts). Canon anchors:
- the place she was meant to die: the Forn ambush clearing (Kaylessa_FornAmbush 37a6331a) and the tomb Kyonin's
  marksmen raise there when her letter goes (KaylessaTomb 78fb64bf, started by the Kaylessa_Letter project 472666a0);
  in the living world, the ravine where Forn fell by Kyonin's arrows;
- her first words to the Commander, "What are you looking at, soldier? Like what you see?" (Kaylessa_main/Cue_0001 2d7d6df4);
- light hurts her: Forn's flash powder "and she cried out as if I had stabbed her" (Forn_main/Cue_0048 e5f50b58);
- the Dark Fate as a state of the soul that "detests the light" (Kaylessa_Reveal/Cue_0041 d5010739);
- Avennara, "the leader of the border defenders", her real friends in Kyonin (Kaylessa_Reveal/Cue_0028 f252350f);
- the Sunset Wasps' goddess, Calistria, the Savored Sting (Cue_0039 b60a1979).
Intimacy (Directive 12): the clearing, by starlight she can see by and the Commander cannot; the cut lands at the start.
"""
from story_format import c, scene
from storylines.kaylessa_wasps import SOLDIER
from storylines.kaylessa_trickster import (FIRST_WORDS, AMULET, ARROW, BEAST_FED, BEGGED, CLOSED, COMMITTED, COUNCIL_KNOWS, DEAD_L,
                                           DREZEN, HER_ARROW, KNIFE_BACK, KNIFE_HELD, LEFT, MET, PRESENCE, REL, SHYKA_RAISED,
                                           STALLED, SWAP_CLEAN, SWAP_FUMBLED, TOMB, UNIT, WASP_SENT, kay, nar)

SCENES = []
N = "kaylessa.clearing."
NIGHT = N + "where_i_was_meant_to_die"
MORNING = N + "grey_light"
STIRS = N + "the_beast_stirs"
NAME = N + "once_when_it_counts"
CLOAK = N + "a_cloak_that_isnt_grey"
AFTER = N + "after_the_war"
AVENNARA = N + "avennara"
LETTER_SENT = "kaylessa.wasps.letter_sent"         # kaylessa_wasps/kyonin: her letter went under the crusade's seal

NIGHT_FLAG = N + "night"
HELD_HER = N + "held_her"
SPOKE_WASP = N + "spoke_the_sting"
MADE_HER_LAUGH = N + "made_her_laugh"
RED_CLOAK = N + "red_cloak"


def here(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5), any_groups=()):
    """A physical scene at her presence under the tailor's awning, after the commit."""
    # Every commit leaves the knife in one pair of hands or the other (kaylessa_trickster KNIFE_HELD / KNIFE_BACK).
    extra = dict(RequiresAnyGroups=[[KNIFE_HELD, KNIFE_BACK]] + [list(g) for g in any_groups])
    SCENES.append(scene(id, title, "Kaylessa", min(chapters), entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", COMMITTED, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, id, *forbids))), delay=delay, last=max(chapters),
                        optional=True, Relationship=REL, Chapters=list(chapters), ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, **extra))


def away(id, title, nodes, requires, forbids=(), delay=24, owner="Kaylessa", kind="visit", any_groups=()):
    """A rest-delivered scene: she comes for the Commander at night, or they are out past the walls together."""
    SCENES.append(scene(id, title, owner, 3, "", nodes, requires=tuple(dict.fromkeys(("trickster.ever", COMMITTED, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, id, *forbids))), delay=delay, last=5, optional=True,
                        Relationship=REL, Remote=True, Kind=kind, Chapters=[3, 5], **(dict(Areas=[DREZEN]) if kind == "visit" else {}),
                        RequiresAnyGroups=[[KNIFE_HELD, KNIFE_BACK]] + [list(g) for g in any_groups]))


# --- The night: where she was meant to die (heat up to the cut). ------------------------------------------------------

away(NIGHT, "Where I was meant to die", [
    nar("open", '''{n}She comes for you after the last bell, wrapped to the eyes, with no lantern. She doesn't say where you're going. She carries no light and wants none. She takes your wrist and leads you.{/n}''',
        c("Continue", "tomb", requires=(TOMB,)),
        c("Continue", "bare", requires=(BEGGED,), forbids=(TOMB,)),
        c("Continue", "branch", requires=(DEAD_L,), forbids=(BEGGED,)),
        c("Continue", "ravine", forbids=(DEAD_L,))),
    nar("tomb", '''{n}An hour's ride out of the gate, over ground you remember, to the clearing where Forn sprang his trap. There is a tomb in it now, white stone, raised by Kyonin marksmen who were told she was dead. Her name is cut into the lintel in Elven, very fine. Somebody has left dried flowers on the step.{/n}
{n}She stands in front of it with her hands behind her back, like an officer inspecting a sentry.{/n}''',
        c("Continue", "why")),
    nar("bare", '''{n}An hour's ride out of the gate, over ground you remember, to the clearing where Forn sprang his trap. There is no stone. The crusade's burial detail left a long, low mound at the edge of the trees, already green, and no name on it.{/n}
{n}She stands in front of it with her hands behind her back, like an officer inspecting a sentry.{/n}''',
        c("Continue", "why")),
    nar("branch", '''{n}An hour's ride out of the gate brings you to a clearing among dead trees. Kaylessa points toward a gap in the trunks. "That's where I came out in the branch Shyka took me from. Forn's archers were on the other side." She touches her collarbone. "I remember their arrow. I remember walking away, too."{/n}''',
        c("Continue", "why_branch")),
    nar("ravine", '''{n}Not far. Out of the south gate and down into the ravine below the wall, where the stones are still stained dark in places and someone has swept away the lantern glass. It's black as the bottom of a well with the moon down, and she knows every stone of it.{/n}
{n}She walks you to the stone where the hunter lay and stops there, with your wrist still in her hand.{/n}''',
        c("Continue", "why_ravine")),
    kay("why", '''"This is where I'm supposed to be, soldier. Under that." {n}She nods at the ground as if it had insulted her.{/n}
"I asked you for it. I got it, for a night. And then I got this instead, all of it, the market and the tea and you." {n}She turns round.{/n} "I wanted to do something here that isn't dying."''',
        c("Continue", "desire")),
    kay("why_branch", '''"I used to look at these trees and see his archers." {n}She looks back toward the horses.{/n}
"I've spent enough nights with that hunter in my head. I brought you here because I want to remember something else when I look at these trees."''',
        c("Continue", "desire")),
    kay("why_ravine", '''"He meant this to be my grave. Kyonin's arrows, a courier's face, and nobody left to say otherwise." {n}Her thumb moves on the inside of your wrist.{/n}
"It's his instead. I wanted to see it with you. I wanted to do something down here that isn't dying."''',
        c("Continue", "desire")),
    nar("desire", '''{n}She pulls the shawl down, and then the hood, and then, with quick soldier's fingers, the buckles of the courier's cloak. It drops round her boots. She kicks it flat onto the grass with one foot and stands on it, looking at you, chin up.{/n}''',
        c("Continue", "like_met", requires=(FIRST_WORDS,)),
        c("Continue", "like_stranger", forbids=(FIRST_WORDS,))),
    kay("like_met", '''"Anemora made this body to prove a point." {n}Her voice is low and rough and not quite steady.{/n} "Kyonin wants it in the ground to hide the point. I've been hiding it under rags since the Worldwound. Tonight it's mine, and I want you to have it, and I want you to look at it while you do."
"When we met, I asked you something. What are you looking at, soldier?" {n}Her mouth moves.{/n} "Like what you see?"''',
        c('[Flirt] "Very much. Show me the rest."', "rest"),
        c('"I can\'t see a thing."', "see"),
        c("[Kiss her.]", "kiss")),
    kay("like_stranger", '''"Anemora made this body to prove a point." {n}Her voice is low and rough and not quite steady.{/n} "Kyonin wants it in the ground to hide the point. I've been hiding it under rags since the Worldwound. Tonight it's mine, and I want you to have it, and I want you to look at it while you do."
"In Kenabres, when soldiers stared, I used to ask them something. What are you looking at, soldier?" {n}Her mouth moves.{/n} "Like what you see?"''',
        c('[Flirt] "Very much. Show me the rest."', "rest"),
        c('"I can\'t see a thing."', "see"),
        c("[Kiss her.]", "kiss")),
    kay("see", '''"Not the way I can." {n}She laughs under her breath, pleased with herself, the way a hunter is pleased with a good wind.{/n} "I can see every hair on your arms standing up, soldier. It's only fair one of us gets to."
{n}She takes your hands and puts them on the laces of her leathers.{/n} "Then find it the other way."''',
        c("Continue", "kiss")),
    kay("rest", '''"Greedy." {n}She says it with deep approval.{/n} "Good."
{n}She unlaces her leathers herself, without hurry, watching your face the whole time the way she watches a treeline, and lets the stars do what little they can. Grey scars cross her ribs and the tops of her arms, the Worldwound's handwriting. She doesn't cover any of them.{/n}''',
        c("Continue", "kiss")),
    nar("kiss", '''{n}Her mouth is cool and then it isn't. She kisses the way she fights, forward, all at once, one hand hard at the back of your neck and the other already working at your belt. When the point of a fang finds the side of your neck she goes still against you, and breathes there once, and moves on, and you both know what she chose not to do.{/n}''',
        c("Continue", "knife_held", requires=(KNIFE_HELD,)),
        c("Continue", "knife_back", requires=(KNIFE_BACK,))),
    nar("knife_held", '''{n}When she finds the Kyonin dagger at your belt she draws it, looks at it in the starlight, and lays it on the grass beside the cloak, within reach of your hand and not hers. She does it without looking, the way she'd lay down a bow.{/n}''',
        c("Continue", "down")),
    nar("knife_back", '''{n}She pulls the Kyonin dagger out of her boot and lays it on the grass beside the cloak, within reach of her own hand, and then she pushes it an inch toward yours. She does it without looking, the way she'd lay down a bow.{/n}''',
        c("Continue", "down")),
    kay("down", '''"There. Now nobody's holding anything." {n}She is breathing hard, and her skin under your hands is cool as river stone and getting warmer, and every muscle Anemora's work put in her is moving at once.{/n}
"Don't you dare be gentle with me, soldier. I've had enough careful hands for one life. I want yours."''',
        c("[Pull her down onto the cloak.]", "cut", flags=(NIGHT_FLAG,))),
    nar("cut", '''{n}She lands on the cloak and catches you by the hair. Her leathers slip from one shoulder; she presses your hand against the bare skin and bites a laugh off against your mouth. "Here, soldier." She draws you over her, kissing hard, the courier's grey bunching beneath you.{/n}''',
        c("[...]")),
], requires=(), delay=12)


# --- The morning after (a rest later): grey light at the clearing. -----------------------------------------------------

away(MORNING, "Grey light", [
    nar("open", '''{n}You wake to cold grass and a grey sky and the sound of Drezen's horns a long way off, calling the morning watch. She's already up, sitting on a stone a few feet away, dressed again, with the shawl wound over her eyes against a light you'd hardly call light.{/n}''',
        c("Continue", "held", requires=(KNIFE_HELD,)),
        c("Continue", "back", requires=(KNIFE_BACK,))),
    nar("held", '''{n}The Kyonin dagger is back at your belt. She must have buckled it on you while you slept. You didn't feel her do it. You aren't sure you'd have felt anything she chose to do.{/n}''',
        c("Continue", "check")),
    nar("back", '''{n}The Kyonin dagger is back in her left boot, sheathed. Her fingers keep going to the hilt where it sticks up past the leather, round and round the worn wood, a habit she hasn't noticed she has.{/n}''',
        c("Continue", "check")),
    kay("check", '''"I checked." {n}She doesn't turn her head.{/n} "First thing, before I even opened my eyes. Same as every morning."''',
        c("Continue", "stalled", requires=(STALLED,), forbids=(BEAST_FED,)),
        c("Continue", "fed", requires=(BEAST_FED,)),
        c("Continue", "clean", requires=(SWAP_CLEAN,), forbids=(BEAST_FED,)),
        c("Continue", "fumbled", requires=(SWAP_FUMBLED,), forbids=(BEAST_FED,))),
    kay("stalled", '''"Still there. Same place. The thumb didn't slip." {n}She breathes out slowly.{/n} "I half thought it would. I thought something like last night was exactly the kind of thing that feeds it. It didn't. It just sat there, like a dog that's been told."''',
        c("Continue", "now")),
    kay("fed", '''"It's quiet." {n}She says it as if it were bad news.{/n} "It's been hungry since your cells, soldier. Every night I can feel it at the back of my teeth. Last night it was quiet. I don't know if that's because of you or in spite of you, and I don't trust it either way."''',
        c("Continue", "now")),
    kay("clean", '''"Same place as yesterday." {n}She finally looks at you, over the shawl.{/n} "I thought a night like that would feed it. It didn't get a crumb. It'll move again next week; it always does, a little, like water through a boot. But not for you. Not for last night." {n}She rubs her thumb over the knots.{/n} "I'm not going to say anything more about it in case it hears."''',
        c("Continue", "now")),
    kay("fumbled", '''"It's where it was after the ravine. No further." {n}She rubs her hands together, hard, as if they were cold.{/n} "I was afraid it would come for you. Last night. When I stopped thinking. It didn't. I don't know what that means, and I'm not going to ask."''',
        c("Continue", "now")),
    kay("now", '''"They'll be missing you on the walls. There's a war on, apparently." {n}She stands, and holds out a hand to pull you up, and doesn't let go straight away once you're standing.{/n}
"Rule one still stands, soldier. Not your drow. But last night I was yours, and I chose it, and I'll choose it again if I feel like it. Mind you remember the difference."''',
        c('"I\'ll remember."', "ride"),
        c('"Stay a little longer. The war can wait an hour."', "longer", flags=(HELD_HER,))),
    kay("ride", '''"Good." {n}She's already walking toward the horses, and over her shoulder:{/n} "You snore, by the way. I'm putting it in my report."''',
        c("[Ride back to Drezen.]")),
    kay("longer", '''"It can't. That's the whole trouble with wars." {n}But she sits back down on the stone, and after a moment she leans against you, shoulder to shoulder, and lets the horns call twice more before she moves.{/n}
"One hour, soldier. And then you go and be a Commander, and I go and sit under my awning, and nobody in Drezen knows a thing."''',
        c("[Ride back to Drezen.]")),
], requires=(NIGHT_FLAG,), delay=1, any_groups=((STALLED, SWAP_CLEAN, SWAP_FUMBLED),))


# --- The beast stirs: the knife's first bad night. ----------------------------------------------------------------

here(STIRS, "The knife in the dark", '"You look like you haven\'t slept."', [
    nar("open", '''{n}She's under the awning at dusk with the shawl down and her eyes shut, and her hands are wrapped tight round a cup of cold tea as if it were the only thing holding her to the crate. When you sit down beside her she flinches, and then she doesn't.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Bad night." {n}She doesn't open her eyes.{/n} "There was a fight in the lower city, some deserter with a knife and a woman who owed him money. I heard it through two walls. I heard her scream." {n}Her jaw tightens.{/n} "And the thing in me sat up and licked its lips, soldier. It wanted to go and watch."''',
        c("Continue", "held", requires=(KNIFE_HELD,)),
        c("Continue", "back", requires=(KNIFE_BACK,))),
    kay("held", '''"I came to your door at the second bell. You were asleep. I stood there with my hand on the latch and I thought: the knife's in there, on that belt, and I gave it away, and if it comes the rest of the way tonight I'll have to wake you and ask." {n}She opens her eyes.{/n} "And that stopped it. Having to ask. It doesn't know how to ask for anything."''',
        c("Continue", "what")),
    kay("back", '''"I had the knife out. In my own hand, all night, in the dark, because you gave it back to me and said it was mine." {n}She opens her eyes.{/n} "And every time the thing in me leaned on it, I thought of you pushing my fingers closed round the hilt, as if it were mine to decide. It hates that. It wants me to think I've got no choice."''',
        c("Continue", "what")),
    kay("what", '''"It passed. It always passes, until the night it doesn't." {n}She puts the cup down.{/n} "I'm not telling you so you'll fix it. You can't. I'm telling you because rule three cuts both ways."''',
        c("[Put your arm round her and say nothing.]", "held_her", flags=(HELD_HER,)),
        c('"Calistria doesn\'t forgive and doesn\'t forget. Neither should you. Hate it right back."', "sting",
          flags=(SPOKE_WASP,)),
        c('"Next time it sits up, send it to me. I\'ll tell it a joke so bad it goes back to sleep out of embarrassment."',
          "joke", flags=(MADE_HER_LAUGH,))),
    kay("held_her", '''{n}She goes stiff for a moment under your arm, the way she does when anyone touches her without warning. Then she lets her head fall against your shoulder, heavily, like a soldier who has stopped marching.{/n}
"This," {n}she says, to nobody in particular.{/n} "This is the stupidest thing that works."''',
        c("[Stay until the lamps are lit.]")),
    kay("sting", '''{n}She stares at you. Then a laugh gets out of her, low and startled, and it seems to surprise her more than you.{/n}
"You've been reading about my goddess. Somebody's been in the chaplain's shelves." {n}She shakes her head, and she's still smiling when she stops.{/n} "Hate it right back. Yes. The Sting would like that. She never did like anything that crept up on a woman in the dark."''',
        c("[Stay until the lamps are lit.]")),
    kay("joke", '''"You'd bore it to death. You'd bore a curse to death." {n}She's trying not to laugh, and failing, with her hand over her mouth.{/n}
"Gods. Fine. Tell me one now, then. The worst one you've got. I'll test it on the beast later."
{n}You tell her one. It is truly terrible. She laughs until she has to put her head down on her knees, and when she lifts it again her eyes are wet and she looks ten years younger.{/n}''',
        c("[Stay until the lamps are lit.]")),
], requires=(MORNING,), delay=48)


# --- A cloak that isn't grey. -----------------------------------------------------------------------------------------

here(CLOAK, "Not grey", '"Is that... a new cloak?"', [
    nar("open", '''{n}The tailor is actually smiling. You've never seen him smile at her before. She's standing under his awning in a cloak that is not grey: a deep, dark red, the colour of old wine, cut long for riding, with a hood that comes well down over the eyes. She's holding it closed at the throat with both hands, as though it might run away.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Don't." {n}She points a finger at you before you can open your mouth.{/n} "Don't say anything. I bought it. With money. He's been trying to sell me something for weeks and I finally let him, and now he's going to be unbearable."
"The grey was a courier's colour. It was for hiding." {n}Her fingers tighten on the edge of the hood.{/n}''',
        c("Continue", "amulet", requires=(AMULET,)),
        c("Continue", "no_amulet", forbids=(AMULET,))),
    kay("amulet", '''"And I've got nothing left to hide under. No elf face, not any more. It burnt out in the ravine. So I thought, if I'm going to walk round your city looking like what I am, I might as well be seen doing it." {n}She lifts her chin.{/n} "The Wasps wore red under the grey, in Kyonin. Where nobody could see it."''',
        c("Continue", "ask")),
    kay("no_amulet", '''"I'm still hiding. I'll be hiding till the day Kyonin forgets my name, which will be never. But I'm tired of hiding in a colour that means I'm running." {n}She lifts her chin.{/n} "The Wasps wore red under the grey, in Kyonin. Where nobody could see it."''',
        c("Continue", "ask")),
    kay("ask", '''"So. Say it. Whatever you were going to say."''',
        c('[Flirt] "It suits you. It\'ll suit the floor of my quarters even better."', "flirt", flags=(RED_CLOAK,)),
        c('"It suits you."', "suits", flags=(RED_CLOAK,)),
        c('"People will see you coming a mile off."', "seen", flags=(RED_CLOAK,))),
    kay("flirt", '''{n}She hits you in the chest with the back of her hand, not gently, and doesn't take the hand away.{/n} "In the middle of the market. With him listening." {n}The tailor is very carefully folding a bolt of linen with his back to you.{/n}
"We'll see about the floor, soldier. I paid good money for this. If it ends up on anybody's floor, I'll be the one who drops it there, and the floor will have been swept."''',
        c("[Leave her to argue with the tailor about the hem.]")),
    kay("suits", '''"It does." {n}She says it as a fact, not a question, and then looks faintly shocked at herself.{/n}
"It does," {n}she says again, quieter, looking down at the red over her arm.{/n} "I'd forgotten I was allowed to like the look of something."''',
        c("[Leave her to argue with the tailor about the hem.]")),
    kay("seen", '''"Let them." {n}Her teeth show, all of them.{/n} "Let them see me coming a mile off, soldier, and let them run the whole mile. I've spent two years being the one who runs. It's somebody else's turn."''',
        c("[Leave her to argue with the tailor about the hem.]")),
], requires=(MORNING,), delay=24)


# --- Once, when it counts: she says the Commander's name. ---------------------------------------------------------

here(NAME, "Once, when it counts", '"The bells..."', [
    nar("open", '''{n}The alarm bells start on the east wall while you're under the awning: three strokes and a pause, three and a pause, the signal for flyers. Over the rooftops something with too many wings is circling the citadel, and more are coming up out of the smoke over the Worldwound behind it.{/n}
{n}She's on her feet with the bow strung before the second set of strokes.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Vescavors. A swarm. They go for the eyes and the soft places." {n}She checks the arrows in her quiver with one pass of her fingers, counting by touch.{/n}
"Your people need you on the wall, and I'll be better off on a roof where nobody's standing on my feet." {n}She's already moving. At the edge of the awning she stops, and turns, and looks at you.{/n}''',
        c("Continue", "name", requires=(SOLDIER,)),
        c("Continue", "name_fresh", forbids=(SOLDIER,))),
    kay("name_fresh", '''"{name}."
{n}She says it once, quite clearly, as if she were laying a coin on a table where you would find it later.{/n}
"There. You never asked, so I never used it. Now I have. Don't get used to it, soldier." {n}And she's gone, up a drainpipe and over a gutter onto the roofs, fast as a thrown knife.{/n}''',
        c("[Go to the wall.]", "after")),
    kay("name", '''"{name}."
{n}She says it once, quite clearly, as if she were laying a coin on a table where you would find it later.{/n}
"There. I said I'd use it once, when it counted. Don't get used to it, soldier." {n}And she's gone, up a drainpipe and over a gutter onto the roofs, fast as a thrown knife.{/n}''',
        c("[Go to the wall.]", "after")),
    nar("after", '''{n}Afterwards, when the swarm is broken and the wall is being cleared of what's left of it, you find a dozen vescavors on the rooftops round the market square with an arrow through each of their heads, all at the same angle, all from the same roof. She's sitting on the ridge of it with her bow across her knees, looking entirely pleased with herself.{/n}''',
        c("Continue", "roof")),
    kay("roof", '''"Twelve." {n}She holds up the empty quiver.{/n} "I'd have had thirteen if your crossbowmen hadn't taken the last one. It was mine. I'd been watching it for a whole minute."
{n}She holds out her hand for you to help her down, and when you've got her down she doesn't let go of it.{/n} "You were good on the wall. I watched you too. From up there you look like someone who isn't going to die today. Keep looking like that."''',
        c("[Keep hold of her hand.]")),
], requires=(MORNING,), delay=24)


# --- After the war: what she wants, now that she might live to see it. ---------------------------------------------

here(AFTER, "After", '"Do you ever think about after?"', [
    nar("open", '''{n}The market is closing. The tailor is lowering his shutters round her, leaving her the corner under the awning as if it were a rented room. She's watching the last carts go, with her knees drawn up and her boots on the crate.{/n}''',
        c("Continue", "start")),
    kay("start", '''"I don't. I never did. There was no after, not for me. There was Kyonin, and then there was the Worldwound, and then there was running, and at the end of the running there was a knife." {n}She glances at the dagger, wherever it is today.{/n}
"Now there's this. And people keep talking about when the Wound is closed, as if it were a thing that happens. And I keep catching myself listening."''',
        c('"What would you do?"', "what"),
        c('"Where would you go?"', "where")),
    kay("what", '''"Hunt." {n}At once, without thinking.{/n} "Not demons. Men. The ones the law misses, the way I used to in Kyonin before Anemora spoiled it. Only this time I'd check the names myself. Every one of them. Twice." {n}Her mouth twists.{/n} "Calistria's work, done properly. Is that a terrible thing to want, soldier?"''',
        c("Continue", "kyonin")),
    kay("where", '''"Anywhere the sun doesn't come straight down." {n}She almost smiles.{/n} "Somewhere with forests. Somewhere a woman in a red cloak can walk into an inn and sit with her back to the wall and nobody asks her anything. There must be one of those somewhere in the world."''',
        c("Continue", "kyonin")),
    kay("kyonin", '''"And one day I'll go to Kyonin. Not to live. Just to walk in through the gate with my own face on and let them look." {n}She turns her head.{/n}''',
        c("Continue", "sent", requires=(WASP_SENT,)),
        c("Continue", "letter", requires=(LETTER_SENT,), forbids=(WASP_SENT,)),
        c("Continue", "plain", forbids=(WASP_SENT, LETTER_SENT))),
    kay("sent", '''"Tessariel will have got there first. She'll have told them. They'll know what I am before I even open my mouth." {n}A breath.{/n} "Good. Let them know. It'll save time."''',
        c("Continue", "you")),
    kay("letter", '''"Avennara has my letter by now. The border knows. The Council will deny it, but the border knows." {n}A breath.{/n} "When I walk in, the sentries will have heard of me. That's more than Forn ever meant them to."''',
        c("Continue", "you")),
    kay("plain", '''"They'll try to kill me, of course. The Council will. Let them try it in daylight, in front of everyone, with me standing in the gate saying my name." {n}A breath.{/n} "That's the only kind of fight I've ever wanted."''',
        c("Continue", "you")),
    kay("you", '''"And you." {n}She says it as if she were adding a line to a list she'd been keeping for some time.{/n}
"I don't know what you'll be, after. Whatever your Council turns you into, whatever Shyka or your war costs you, whatever mess you make of the Wound. I don't know, and I don't care. Mind the rules, and you can come with me to Kyonin and watch them look."''',
        c('"I\'ll mind the rules."', "rules"),
        c('"Rule four. I\'m breaking one right now."', "four")),
    kay("rules", '''"Good soldier." {n}She puts her boots down off the crate, and leans over, and kisses you once, briefly, on the mouth, in the open, with the tailor's shutter half down and anybody in the square to see.{/n} "Now go and win your war. I'd like there to be an after."''',
        c("[Go and win the war.]")),
    kay("four", '''"Which one?" {n}She's delighted and furious at once.{/n} "Which one, soldier? You can't just..." {n}And then she sees your face, and she stops, and puts her hand flat on your chest.{/n}
"You're not going to tell me. You're never going to tell me." {n}She leans in until her forehead is against yours.{/n} "You absolute bastard. Go and win your war. I'll be here, working it out."''',
        c("[Go and win the war.]")),
], requires=(NAME,), delay=48, chapters=(5,))


# --- Avennara's answer (only when her letter went under the crusade's seal). -------------------------------------------

here(AVENNARA, "From the border", '"You\'ve got a letter."', [
    nar("open", '''{n}The letter comes by an elven courier who will not stay for an answer, in a leather case sealed with a leaf pressed into green wax. It is addressed in a clear, upright hand to Kaylessa of the Sunset Wasps, in care of the Commander of the Fifth Crusade. It has been opened once already on the road and resealed, not very well. You carry it down to the market yourself.{/n}''',
        c("Continue", "letter")),
    nar("letter", '''{n}She reads it under the awning with her shoulder against yours, so you read it too.{/n}
{n}"Kaylessa. We had been told you were dead. Some of us believed it. I did not, because you were always too stubborn to die where anyone told you to."{/n}
{n}"We have read what you wrote. The Council says it is a drow's lie and forbids it to be copied. It has been copied eleven times that I know of. It is read aloud in the guardrooms of the border forts, at night, with the doors shut. Nobody who hears it looks at the forest in quite the same way afterwards."{/n}''',
        c("Continue", "tessariel", requires=(WASP_SENT,)),
        c("Continue", "tomb", requires=(TOMB,), forbids=(WASP_SENT,)),
        c("Continue", "end", forbids=(WASP_SENT, TOMB))),
    nar("tessariel", '''{n}"A drow woman came to one of our forts in the spring with her own face uncovered and asked to be taken before the Council. She said your name. They took her away. They could not take away the forty soldiers who heard her in the gate."{/n}''',
        c("Continue", "end")),
    nar("tomb", '''{n}"The marksmen who went to Mendev in your name raised you a stone. It seems they were hasty. Tell them I said so, if they are still in the Commander's service. Tell them to leave it standing anyway."{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}"Stay alive. That is an order, and I know you have never once obeyed one. The border remembers. A."{/n}
{n}Kaylessa reads it twice, the second time with her lips moving. Then she folds it very small and puts it inside her shirt, over her heart, and does not say anything at all for the rest of the afternoon, and does not let go of your hand.{/n}''',
        c("[Leave her with it.]")),
], requires=(LETTER_SENT,), delay=72)


# --- World-specific aftermath: Shyka's question, the Council's next hunter, the arrow's scar. -------------------------

SHYKA_NOTE = "kaylessa.trickster.react.shyka_note"   # the Eldest's note (a reaction letter); completing it is the cue
SHYKA_ANSWER = N + "how_it_ends"
HUNTER = N + "the_next_hunter"
SCAR = N + "the_arrow"
TOLD_SHYKA_TRUE = N + "told_shyka_the_truth"
TOLD_SHYKA_JOKE = N + "told_shyka_a_joke"
HUNTER_TURNED = N + "hunter_turned_back"
HUNTER_HERS = N + "hunter_hers"


here(SHYKA_ANSWER, "How it ends", '"Is that from Shyka?"', [
    nar("open", '''{n}She has Shyka's note on her knee, the one in three handwritings, and a stub of charcoal, and a scrap of courier's paper with nothing on it yet. The note has changed shape again since you last saw it. She has weighted it down with her cup so it can't get any ideas.{/n}''',
        c("Continue", "start")),
    kay("start", '''"It wants to know how it ends. That thing. It asked you, and it asked me, and it'll forget both of us asked." {n}She taps the charcoal against the paper.{/n}
"I've been trying to write it an answer since it arrived. I keep writing 'badly' and crossing it out. It isn't true yet. I don't like writing things that aren't true."''',
        c("Continue", "raised", requires=(SHYKA_RAISED,)),
        c("Continue", "plain", forbids=(SHYKA_RAISED,))),
    kay("raised", '''"And somewhere in its keeping there's a you who said yes and meant it. Every word, you said. No fingers crossed." {n}She doesn't look up.{/n} "I think about that one sometimes. Whether that you is happy, being Shyka. Whether it remembers me."''',
        c("Continue", "ask")),
    kay("plain", '''"And somewhere in its keeping there's a you who said yes to it. A you that's one of the Many now, with a hundred faces and none of them yours." {n}She doesn't look up.{/n} "I think about that one sometimes. Whether it remembers me."''',
        c("Continue", "ask")),
    kay("ask", '''"You write it, soldier. You paid. It's your answer to give."''',
        c('[Write the truth] "It hasn\'t ended. She still says soldier. Ask again later."', "truth", flags=(TOLD_SHYKA_TRUE,)),
        c('[Write a joke] "Slightly used. As promised. No refunds."', "joke", flags=(TOLD_SHYKA_JOKE,))),
    kay("truth", '''{n}She reads it over your shoulder, and her breath goes out through her nose, short.{/n}
"'She still says soldier.'" {n}She takes the paper and folds it into a shape that is almost a wasp, and then, frowning, into one that isn't.{/n} "It'll lose it. It'll find it again in a hundred years and not know what it means. Good. Let it wonder."''',
        c("[Give her the folded note.]")),
    kay("joke", '''"'No refunds.'" {n}She stares at it. Then she puts her face in her hands, and her shoulders shake, and it takes you a moment to be sure she's laughing.{/n}
"You're telling the thing that bought your future it can't have me back. In writing." {n}She wipes her eyes with the heel of her hand.{/n} "Send it. Gods. Send it before I think better of it."''',
        c("[Give her the folded note.]")),
], requires=(SHYKA_NOTE,), forbids=("shyka.gone",), delay=24)


here(HUNTER, "The next one", '"You\'ve got blood on your sleeve."', [
    nar("open", '''{n}She's cleaning an arrowhead with a rag, very thoroughly, under the awning. There is blood on her sleeve that isn't hers and blood on the rag, and the tailor has gone round the other side of his stall to be busy.{/n}''',
        c("Continue", "start")),
    kay("start", '''"They sent another one." {n}She doesn't stop cleaning.{/n} "The Council. Your marksmen on the ridge ran home and told them I'm alive, and they sent another hunter. Younger than the last one. Worse manners. He came over the east wall last night with a blade he'd rubbed with ash."
"I've got him in the old cooper's cellar by the tannery. He's alive. For now."''',
        c("Continue", "ask")),
    kay("ask", '''"I'm asking you, because rule three cuts both ways and because the last time I didn't ask anybody, you saw what I did in that ravine." {n}She puts the arrowhead down.{/n}
"What do we do with him?"''',
        c('"Send him home with a message: every hunter they send comes back like this, or doesn\'t come back."', "turned",
          flags=(HUNTER_TURNED,)),
        c('"He came to kill you. He\'s yours. Do what you want with him."', "hers", flags=(HUNTER_HERS,))),
    kay("turned", '''"A message." {n}She considers it the way a quartermaster considers a bill.{/n} "Yes. Broken fingers, both hands, so he can't draw a bow again. And a letter pinned to his coat in my own hand, in Elven, saying who I am and what I know, for every guard between here and the border to read on his way."
{n}She stands.{/n} "It's crueller than killing him. The Council will have to decide whether to hide him too."''',
        c("[Let her go to the cellar.]")),
    kay("hers", '''"Mine." {n}She turns the arrowhead between her fingers.{/n} "You know what I'd enjoy doing to him in that cellar. Don't pretend you don't."
"I'll break his fingers and pin the letter to his coat. Let the Council see what their duty bought. I want him alive when he tells them who did it."''',
        c("[Let her go to the cellar.]")),
], requires=(COUNCIL_KNOWS,), delay=48, chapters=(5,))


here(SCAR, "The arrow", '"Let me see that."', [
    nar("open", '''{n}She's waiting under the awning with a pot of salve from the chaplain's stores, a roll of clean linen and an expression that forbids argument.{/n}''',
        c("Continue", "yours", requires=(ARROW,)),
        c("Continue", "hers", forbids=(ARROW,))),
    kay("yours", '''"Sit. Shirt off. Your shoulder." {n}She's already unwinding the old bandage.{/n} "The arrow that was meant for me. You said they'd hit you first, and they did, because you're the kind of fool who means things."
{n}Her fingers are cool on the healing wound, careful the way her hands aren't careful with anything else. She works the salve in slowly.{/n} "It'll scar. A white one, here. Every time I see it, I'll know whose face they were aiming at."''',
        c('"Good. Something to remember me by."', "remember"),
        c("[Say nothing. Let her work.]", "quiet")),
    kay("hers", '''"Sit. And hold this." {n}She pulls the collar of her tunic aside and hands you the linen. Under it, low on her collarbone, the arrow wound from the ravine has closed into an angry, puckered star.{/n}
"I can't see it properly to salve it myself. I hate asking. I'm asking." {n}She tips her head back and looks at the underside of the awning while your hands do the work.{/n} "Gently. No, not that gently. I'm not made of paper."''',
        c('"Does it hurt?"', "remember"),
        c("[Say nothing. Let her feel your hands.]", "quiet")),
    kay("remember", '''"Everything hurts. That's how you know you're still in it." {n}A pause.{/n} "This hurts less than most things. Don't let it go to your head, soldier."''',
        c("Continue", "end")),
    kay("quiet", '''{n}Neither of you says anything for a while. The market goes on round the awning: a cart, a dog, a sergeant calling the names of men who are not coming back from the Worldwound. Her breath slows. So does yours.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}When it's done she ties off the linen with a knot you've seen her tie on a bowstring, and then she leaves her hand where it is, flat over the bandage, a moment longer than the work needed.{/n}''',
        c("[Stay there.]")),
], requires=(), delay=24, any_groups=((ARROW, HER_ARROW),))
