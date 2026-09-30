"""Eliandra, Chapter 5 in Drezen: after the star-heart (the courtship on her presence; 11-ROSTER-PLAN-2 §2 build sheet).

The stargazers come to Drezen with the high priestess who has let her Lady go. She keeps a table by the Fool King's bar,
where the stone from her chiefs' ground sits under its cloth (left of Thaberdine, 2.5 m; no other presence uses him), or,
when the King is gone or cannot be found, the Drezen mark where she stands on the Angel path (the native spawner that
Eliandra_DefaultActor 64c5a760 hides everywhere else). Every beat is Trickster-only (T): it follows the device and the yes.

The beats: the city (her first morning question); the stone (the King's tavern only); the lights she can see and the
Commander cannot; the healing that tires her now; Katair and his own grave at the Stone Tree (Ranger_main Cue_0016-0023);
Threshold and the woman she saw there; the chart of the Commander's sky; the road into Sarkoris.
"""
import copy

from story_format import c, n, scene
from storylines.eliandra_trickster import (
    CLOSED, COMMITTED, DEAD, DREZEN, E, HEALING_SEEN, HEART_SEEN, LIGHTS_GIVEN, LIGHTS_SEEN, PATH_FIT, REL,
    REWARD_RETURNED, TABLET, UNIT)

SCENES = []

FOOL_KING = "cc50a88bbd8dd3e4da066d33d14fdfc8"       # FoolKing (MythicTrickster_Ch3), in his tavern in DrezenCapital
MARK = "9a41b047-9314-4719-a915-9c24aedf3e95"        # her native DrezenCapital spawner (scene 3e2b5ea0; Eliandra_DefaultActor)
HUB = "eliandra.presence"
HUB_ALT = "eliandra.presence.mark"
HUB_FAILED = HUB + ".failed"
KING_GONE = "fool_king.gone"

FIRST_QUESTION = E + "drezen.first_question"
STONE_SEEN = E + "drezen.stone_seen"
STONE_HOME = E + "drezen.stone_home"      # the Commander promised to carry the stone back to the chiefs' ground
DARK_SKY = E + "drezen.dark_sky"
ORDINARY = E + "drezen.ordinary"
KATAIR_GRAVE = E + "drezen.katair_grave"
THRESHOLD_TOLD = E + "drezen.threshold"
CHART = E + "drezen.chart"
ROAD = E + "drezen.road_promised"

GREETING = ("{n}At a table by the King's bar, out of the worst of the noise, a woman in a grey travelling cloak sits with a cup "
            "of water in front of her and a star chart spread under her hands. The regulars give her table a wide, respectful "
            "berth, as though it were an altar.{/n}")
PRESENCES = {
    # Left of the Fool King, 2.5 m; no other presence is anchored to him (10 §2 (i): the Table spawns no units).
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FOOL_KING, Side="left", Distance=2.5),
              Requires=["trickster.ever", HEART_SEEN], Forbids=[CLOSED, DEAD, HUB_FAILED, KING_GONE], MinChapter=5,
              MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # Fallback, when the King is gone or cannot be found: her own Drezen mark from the Angel path.
    HUB_ALT: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(Locator=MARK, Offset=[0.0, 0.0]),
                  Requires=["trickster.ever", HEART_SEEN], Forbids=[CLOSED, DEAD], MinChapter=5, MaxChapter=5,
                  RequiresAnyGroups=[[HUB_FAILED, KING_GONE]], AnswerLists=[], Dialog="hub",
                  Greeting=("{n}A woman in a grey travelling cloak sits in a quiet corner of the city with a star chart across "
                            "her knees, watching the street as though it were a sky she had not learned yet.{/n}")),
}


def el(id, text, *choices, **kw):
    return n(id, "Eliandra", text, *choices, portrait="Eliandra", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Eliandra", **kw)


def kt(id, text, *choices, **kw):
    return n(id, "Katair", text, *choices, portrait="Katair", **kw)


PLACES = ((HUB, "", {}), (HUB_ALT, "_mark", dict(RequiresAnyGroups=[[HUB_FAILED, KING_GONE]])))


def drezen(id, title, entry, nodes, requires, forbids=(), delay=0, places=PLACES):
    """A beat on her presence (the King's tavern, or her Drezen mark): the same scene on each, each forbidding the other."""
    ids = [id + suffix for _, suffix, _ in places]
    for hub, suffix, extra in places:
        sid = id + suffix
        PATH_FIT[sid] = "T"
        SCENES.append(scene(sid, title, "Eliandra", 5, entry, copy.deepcopy(nodes),
                            requires=("trickster.ever", HEART_SEEN, *requires),
                            forbids=(CLOSED, DEAD, *[o for o in ids if o != sid], *forbids), delay=delay, last=5,
                            Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=hub,
                            **copy.deepcopy(extra)))


# --- 1. The city: her first morning question --------------------------------------------------------------------------------

drezen(E + "drezen.city", "A city with walls", '"How are you finding Drezen?"', [
    el("start", '''"Loud." {n}Eliandra says it with a kind of wonder.{/n} "I had forgotten that a city is loud all night. In the shrine the loudest thing after dark was Odden snoring, and we moved him to the far cell in the forty-third year." {n}She turns her cup of water in her hands.{/n}
"There are children everywhere. There were no children in Pulura's Fall. I had forgotten that too. A little boy asked me this morning whether I was a ghost, because I was so pale, and I told him I was only old, and he said that was worse."''',
       c('"Are the others settled?"', "others"),
       c('"You don\'t look old."', "old")),
    el("others", '''"Odden found us rooms above a cooper's, near the citadel. The cooper is a widower, and Odden has already told him about his daughter Ranhild, twice, and been told about the cooper's son, three times, and they are now inseparable." {n}A small smile.{/n} "The wardens have gone to your quartermaster to ask for work. The girl with the sling is learning to be a scullion somewhere with windows. They are frightened, all of them, and none of them has asked to go back."''',
       c("Continue", "ask")),
    el("old", '''"I was old enough to lead a shrine before your grandmother was born, Commander, and I look it in the mornings." {n}She does not seem displeased.{/n} "My Lady kept us as we were for as long as the work lasted. The work is over. I do not know what time will do with me now that she has let me go, and I find that I do not mind. I spent a century with nothing changing. I should like to see what I look like when something does."''',
       c("Continue", "ask")),
    el("ask", '''{n}She sets the cup down and folds her hands on the chart, the way a priestess folds them before a reading.{/n}
"You said I might ask you every morning. I have been saving the first one since the road." {n}She takes a breath.{/n} "What do you do in the mornings, Commander? When you are not being a commander. I want to know what I am asking you away from."''',
       c('"Read dispatches. Curse at them. Burn the worst ones."', "dispatches", flags=(FIRST_QUESTION,)),
       c('[Flirt] "Until now? Nothing worth asking me away from."', "flirt", flags=(FIRST_QUESTION,)),
       c('"Nothing. I don\'t have mornings. I have the next thing."', "nothing", flags=(FIRST_QUESTION,))),
    el("dispatches", '''"Burn them." {n}She seems delighted.{/n} "We had no dispatches. We had observations, and every one was kept, even the wrong ones. I think I should like to burn something, once. Will you save me a very bad one?"''',
       c('"I\'ll save you the Council\'s next letter."', "end")),
    el("flirt", '''{n}Colour comes into her face, which, in someone that pale, is very visible.{/n} "You say things like that as if they cost you nothing," she says. "I have watched you. I do not think they are free. I think you have simply decided to pay for them." {n}She looks down at the chart.{/n} "Say it again tomorrow. I will pretend to be less surprised."''',
       c("Continue", "end")),
    el("nothing", '''"The next thing." {n}She considers that as she would a star that had stopped where it should not.{/n} "Then I shall be the next thing, some mornings. I am told I am very good at being in the way. Katair has said so for a hundred years."''',
       c("Continue", "end")),
    el("end", '''"Thank you. That is one." {n}She picks up her cup again.{/n} "I have a hundred years of questions, and you have agreed to all of them. You should have read the terms more carefully, Commander."''',
       c("[Leave her to her chart.]")),
], requires=(), forbids=(FIRST_QUESTION,))


# --- 2. The stone (the King's tavern only) ----------------------------------------------------------------------------

drezen(E + "drezen.stone", "The stone under the cloth", '"You\'ve been looking at the King\'s stone."', [
    el("start", '''"I came to see it." {n}Eliandra does not pretend otherwise. Behind the bar, under its cloth, the stone tablet from the chiefs' ground sits between a keg and a jar of pickled eggs.{/n}
"I watched you carry it away from behind my Lady's veil, and I have wondered ever since what a crusader wanted with a chief's stone. And here it is, in a tavern, holding up a king." {n}She is quiet.{/n} "He asked me whether his ancestors were buried under it. I said probably. I thought it kinder than the truth."''',
       c('"What is the truth?"', "truth"),
       c('"He needed it more than the dead did."', "needed")),
    el("truth", '''"That nobody knows whose it is." {n}She looks at the cloth.{/n} "The chiefs of the clans went to their rest on barges, down the river and over our falls, and the stones were set up afterwards by whoever loved them. Most had no names. Sarkoris did not believe a chief belonged to a stone, or a stone to a chief. It believed in the arguing afterwards." {n}She almost smiles.{/n} "In a way, your King is very Sarkorian. He has a stone, and a great many opinions about what it means, and no evidence at all."''',
       c("Continue", "choice")),
    el("needed", '''"Perhaps." {n}She does not argue.{/n} "The dead are patient. They have been lying under that slope for a hundred years while cultists walked them about on strings, and nobody gave them anything but the edge of a sword. A king who drinks to them every night may be the best thing that has happened to them in a century." {n}A pause.{/n} "I did not say it was a good king."''',
       c("Continue", "choice")),
    el("choice", '''"I will not ask for it back. It is not mine to ask for; it belonged to the chiefs, and they are past asking. But I will tell you what I would do, if it were mine."
"I would take it home when the war is done. Set it up again where it stood, below the dry fall, with the others. And then I would let your King come and visit it, and drink to whoever he likes."''',
       c('"When the war\'s done, I\'ll carry it back myself. The King can come and drink at the cairn."', "home", flags=(STONE_SEEN, STONE_HOME)),
       c('"It stays with the King. He\'d fall apart without it, and the city would follow."', "stays", flags=(STONE_SEEN,))),
    el("home", '''{n}She looks at you with a directness that is almost uncomfortable.{/n} "You would do that." {n}It is not a question.{/n} "Then I will hold you to it, the way my Lady holds her servants: gently, and forever." {n}She lays her hand flat on the cloth, over the stone, and takes it away again.{/n} "He will want to make a speech. Let him. The dead have heard worse."''',
       c("[Leave the stone to its cloth.]")),
    el("stays", '''"Then it stays." {n}She says it without resentment.{/n} "You know your city, and I know nothing about kings. Perhaps a stone that holds up a drunkard and a drunkard who holds up a city is a better use for the dead than standing on a hillside." {n}She glances at the cloth.{/n} "I will come and look at it sometimes. Tell him I will pay for my water."''',
       c("[Leave the stone to its cloth.]")),
], requires=(TABLET,), forbids=(STONE_SEEN,), places=PLACES[:1])


# --- 3. The lights over Drezen (the cost, seen from the wall) ---------------------------------------------------------

drezen(E + "drezen.dark_sky", "Lights over the north wall", '"You sent for me. It\'s the middle of the night."', [
    el("start", '''"It is. Come up to the wall with me. Bring a cloak; the wind comes straight off the Wound." {n}She is already on her feet, her own cloak pinned to the throat, her face bright in a way you have not seen it in Drezen before.{/n} "They are out, Commander. Over the north. The first night of the winter."''',
       c("[Go up to the north wall with her.]", "wall")),
    nar("wall", '''{n}The north wall of Drezen is black and bitter and nearly empty. A sentry stamps his feet in the angle of a tower, his face turned up, his mouth open. Two crusaders further along have stopped mid-round to stare. Eliandra stands at the parapet and looks north.{/n}
{n}You look north too. There is the Wound's red smear on the horizon, as always, and above it a dark, clear sky with a great many stars. And there is something else, a place in the sky your eyes will not stay on. They slide off it to a star, to a cloud, to the sentry's upturned face. You try three times. The third time you understand that you will be trying for the rest of your life.{/n}''',
        c("Continue", "cost", requires=(LIGHTS_SEEN,)),
        c("Continue", "cost_plain", forbids=(LIGHTS_SEEN,))),
    nar("cost", '''{n}You remember the chiefs' ground: the colours over the dry fall, the cairn, the sword across your knees. You remember them exactly, and you will go on remembering them exactly, and that is all you will have. The veil that hid a whole shrine for a century lies over one pair of eyes now, and it is very good work.{/n}''',
        c("Continue", "her")),
    nar("cost_plain", '''{n}It is a strange loss, when you finally feel its edges. You had not looked at the northern lights more than a handful of times in your life. You had not known you meant to look at them again. The veil that hid a whole shrine for a century lies over one pair of eyes now, and it is very good work.{/n}''',
        c("Continue", "her")),
    el("her", '''{n}Eliandra is not looking at the sky. She is looking at you.{/n}
"I thought I should see your face the first time," she says. "So that I would know how to tell you about them, all the other times. Whether to be kind, or to be exact." {n}Her hand finds yours on the cold stone of the parapet.{/n} "Which would you like?"''',
       c('"Exact."', "exact"),
       c('"Kind."', "kind"),
       c("[Watch her face instead of the sky.]", "face")),
    el("exact", '''"Exact." {n}She turns to the north, and her voice changes: it is the voice she uses for the evening reading, slow and plain.{/n} "Three curtains, north-north-east, the lowest touching the Wound's glare. Green at the hem, very bright. Folds of rose above, moving westward, perhaps a hand's breadth in the time it takes to breathe twice. At the height of the middle curtain a white band, where it is brightest, pulsing, the way a heart does when one has been running." {n}She stops.{/n} "The sentry has started to cry. He is trying to hide it. There. That is exact."''',
       c("Continue", "end")),
    el("kind", '''"Kind." {n}She considers the sky.{/n} "They are the most beautiful I have seen them in a hundred years, and I have seen them every winter of those hundred years through a hole in a rock. I think my Lady has put them out for us. I think she likes to be looked at, and she knows you cannot, and she has sent them anyway, so that I will have to tell you." {n}Her fingers tighten.{/n} "That is kind, and I think it is also true. I would not tell you a kind thing that was not."''',
       c("Continue", "end")),
    nar("face", '''{n}So you watch her face. It is easy; she is standing very close. The lights you cannot see are in it: green on one cheekbone, rose moving in her eyes, and a white that comes and goes along the line of her jaw as the sky above her breathes. She knows what you are doing. She lets you, and does not speak, and after a while she leans her head against your shoulder and goes on looking up for both of you.{/n}''',
        c("Continue", "end")),
    el("end", '''"They will be back tomorrow night, if the wind holds," she says at last. "And I will tell you again. You have promised to put up with it."
{n}She does not say that she is sorry. You notice that, and you are grateful for it, and she seems to know you are.{/n}''',
       c("[Stay on the wall until the sentry is relieved.]", flags=(DARK_SKY,))),
], requires=(LIGHTS_GIVEN,), forbids=(DARK_SKY,), delay=24)


# --- 4. Ordinary (the reward returned): a healing that takes everything ------------------------------------------------

drezen(E + "drezen.ordinary", "One wound at a time", '"You look exhausted. What happened?"', [
    el("start", '''"A boy from the Wintersun road with an axe-cut to the thigh. The chaplain was at the walls; someone remembered the priestess from the dry fall." {n}Eliandra's hands are clean, but there is blood dried under her nails, and she is sitting very straight in the way of someone who does not trust herself to sit any other way.{/n}
"He will keep the leg. It took me the better part of an hour. Once it would have taken me ten breaths, and I would have gone on to the next."''',
       c("Continue", "shrine", requires=(HEALING_SEEN,)),
       c("Continue", "no_shrine", forbids=(HEALING_SEEN,))),
    el("shrine", '''"You saw me, in the shrine. After the raid. One wounded after another, one hand on the hurt and one on the head, and my Lady's light taking each of them." {n}She turns her hands over and looks at the backs of them.{/n} "That is gone. I gave it back. I knew what I was giving; I did not know what it would feel like, afterwards, to reach for it out of habit and find only my own two hands."''',
       c("Continue", "choice")),
    el("no_shrine", '''"You never saw what it was, before. It would have been something to see. One wounded after another, and my Lady's light taking each of them, and I could have gone on all night." {n}She turns her hands over and looks at the backs of them.{/n} "I gave it back. I knew what I was giving; I did not know what it would feel like, afterwards, to reach for it out of habit and find only my own two hands."''',
       c("Continue", "choice")),
    el("choice", '''"Odden watched me do it. He said nothing at all, which from Odden is a sermon." {n}A tired smile.{/n} "He thinks I have made a terrible bargain. So does Katair. So, I think, do you, a little, in the part of you that likes to count."''',
       c('"Do you regret it?"', "regret"),
       c('"I think you did a very ordinary, very brave thing, and a boy kept his leg."', "brave"),
       c("[Take her hands and look at the blood under the nails.]", "hands")),
    el("regret", '''"No." {n}She answers at once, and then, being who she is, checks the answer.{/n} "No. I regret that the boy waited an hour in pain. I regret that the next one will wait longer. I do not regret the bargain." {n}She looks at you.{/n} "I was the strongest of my Lady's priestesses because I gave her everything and kept nothing. Now I keep something. It is a smaller strength. It is mine."''',
       c("Continue", "end")),
    el("brave", '''"Ordinary." {n}She repeats it as though it were a word in a language she is learning, and a pleasant one.{/n} "Priestesses all over Golarion do exactly what I did today, every day, and go to bed exhausted, and nobody thinks them saints. I have been a saint for a hundred years, Commander. It was lonely. This is better."''',
       c("Continue", "end")),
    nar("hands", '''{n}Her hands are cold and not quite steady. You turn them palm up. The blood under the nails is the boy's, and the ink stain on the second finger of the right hand is a hundred years old, and there is no shimmer on either palm, none at all, only the lines anyone has.{/n}
{n}Eliandra lets you look. Then she closes her fingers round yours. "They will learn," she says. "They learned to hold a lens. They can learn to be tired."{/n}''',
        c("Continue", "end")),
    el("end", '''"Go and see to your war. I am going to sit here with a cup of water and watch the street go by, and I am going to enjoy being useless for an hour." {n}She almost laughs.{/n} "I have never been useless for an hour in my life. I should like to find out whether I am any good at it."''',
       c("[Leave her to her hour.]", flags=(ORDINARY,))),
], requires=(REWARD_RETURNED,), forbids=(ORDINARY,), delay=24)


# --- 5. Katair: his own grave at the Stone Tree (Ranger_main Cue_0016-0023) ------------------------------------------------

drezen(E + "drezen.katair", "A name on a tombstone", '"Katair wants a word with me?"', [
    nar("start", '''{n}Katair is not sitting down. He stands beside her table with his arms folded and his bow across his back, as he stood at the shrine's door, and when Eliandra gets up and goes off on some errand that is plainly invented, he watches her go and waits until she is out of earshot.{/n}''',
        c("Continue", "stone_tree")),
    kt("stone_tree", '''"The others think I went to the Stone Tree to see my wife," says Katair. "Taeriell thought it for seventy years. He died thinking it." {n}His scarred face does not move.{/n}
"I was married under that tree the spring before the Wound opened. When my Lady hid the shrine we could send no word to our families. None. And I knew Ymris would come looking for me. So I built a grave there, in the first place she would look, and carved my name on the stone, and let her find it."''',
       c('"So she would stop looking."', "stop"),
       c("[Say nothing.]", "stop")),
    kt("stop", '''"So she would grieve, and stop, and go to Mendev, and live." {n}He says it flatly, the way a sergeant reads a casualty list.{/n} "She did. I watched her find it, from behind the veil. I have been going back to that stone for a hundred years because it is the last place I was happy and the first place I did something I could not undo."
"I tell you this because you have been kneeling at our basin, Commander, and giving away things you cannot get back, and I think you ought to know what it looks like a hundred years later."''',
       c('"What does it look like?"', "looks"),
       c('"Are you warning me off her?"', "warn")),
    kt("looks", '''"It looks like a stone with my name on it, and a woman in Mendev I will never see again, and a mission that ended with a demon walking in through the door." {n}He unfolds his arms.{/n} "It looks like it was worth it. That is the worst of it. It was worth it, and I would do it again, and it is still a grave."''',
       c("Continue", "her")),
    kt("warn", '''"No." {n}Something almost like humour crosses his face and is gone.{/n} "She has not been warned off anything since she was thirteen, and it has done her no good at all. I am not going to start now." {n}He glances the way she went.{/n} "I am telling you what a sacrifice weighs, because she will never tell you what hers weighed. She will say it was nothing. It was not nothing."''',
       c("Continue", "her")),
    kt("her", '''"She gave her whole life to my Lady at thirteen. She never once asked for any of it back, and she held the rest of us together for a century while I went out to stand over my own grave. She deserves one thing that is hers."
{n}He looks at you directly now, and holds it.{/n} "You gave her that. I do not like the way you did it, and I do not understand you, and I am grateful. Do not make me regret it."''',
       c('"I won\'t."', "end"),
       c('[Offer your hand] "Come and drink with us at the Stone Tree, when the war\'s over."', "tree")),
    kt("tree", '''{n}Katair looks at your hand as if it were a strange animal. Then he takes it, briefly, hard.{/n}
"Perhaps," he says. "Someone should tell the stone it can stop pretending. It has been lying for me for a hundred years. It has earned a drink."''',
       c("Continue", "end")),
    nar("end", '''{n}Eliandra comes back with three cups of water, sets one in front of each of you, and looks from Katair to you and back with the air of a woman who knows exactly what she has missed and has decided not to ask. Katair drinks his water in one swallow, like brandy, nods to her, and goes.{/n}''',
        c("[Stay with her.]", flags=(KATAIR_GRAVE,))),
], requires=(), forbids=(KATAIR_GRAVE,), delay=48)


# --- 6. Threshold: the woman she saw there ---------------------------------------------------------------------------------

drezen(E + "drezen.threshold", "What she saw at Threshold", '"You\'ve been to Threshold, haven\'t you? Before the Wound."', [
    el("start", '''{n}Eliandra puts down her pen.{/n} "Once. It was a fortress for spellcasters the clans had outlawed, and I went with a delegation of priests to see that the prisoners were fed. I saw the witch there. Areelu." {n}She says the name without heat, the way one names a disease.{/n}
"She was nothing, when I saw her. A pale shadow in a cell. They told me her spirit was broken before they brought her in, and she gave the guards no trouble at all." {n}Her mouth tightens.{/n} "I think now that it was a ruse. The most patient deception I have ever seen, and I did not see it."''',
       c('"Nobody saw it."', "nobody"),
       c('"What else do you remember?"', "remember")),
    el("nobody", '''"That is a comfort to the crowd. It is none to me. I was a priestess of the goddess who hides things from the eye, Commander. I should have known a veil when I stood in front of one." {n}She shakes her head.{/n} "Instead I blessed her bread."''',
       c("Continue", "going")),
    el("remember", '''"That the cell was cold, and that she thanked me for the bread, and that her eyes followed the priests who had brought it and not the bread at all. I thought it was hunger." {n}A pause.{/n} "I have had a hundred years to remember those eyes. They were counting us."''',
       c("Continue", "going")),
    el("going", '''"You will go there. Everyone knows it. The crusade will end at Threshold, one way or another." {n}She lays her hand flat on the chart in front of her.{/n} "Before we lost the shrine, we meant to finish a working: my Lady's power and the memory of Sarkoris's priests, put into one thing, to clear the sky above that fortress and set the northern stars burning over it. Odden says we can still do it, from what the demon did not take."''',
       c("Continue", "blind", requires=(LIGHTS_GIVEN,)),
       c("Continue", "sighted", forbids=(LIGHTS_GIVEN,))),
    el("blind", '''{n}She looks at you, and you both know the next thing before she says it.{/n}
"If we do it, the whole crusade will look up at Threshold and see my Lady's lights over the Wound. And you will not." {n}Neither of you pretends otherwise.{/n} "I will be there, if I can. Not in the breach. In the camp, with the healers. When they light, find me. I will tell you what they look like. I will tell you exactly."''',
       c('"Then I\'ll find you."', "end"),
       c('"Tell me kindly, that time."', "end")),
    el("sighted", '''"If we do it, the whole crusade will look up at Threshold and see my Lady's lights over the Wound." {n}She smiles, a little crookedly.{/n} "You will see them. I made sure of that when I paid her myself. It is the one thing I have done in a hundred years that was entirely selfish, and I am very pleased with it."
"When they light, look up. And then look for me, in the camp with the healers. I want to see your face."''',
       c('"I\'ll look."', "end")),
    el("end", '''"And, Commander." {n}She catches your wrist as you rise, lightly.{/n} "If you meet her there, and she seems broken, do not believe it. I did, once. I have been sorry for a hundred years."''',
       c("[Promise her.]", flags=(THRESHOLD_TOLD,))),
], requires=(), forbids=(THRESHOLD_TOLD,), delay=24)


# --- 7. The chart of the Commander's sky -------------------------------------------------------------------------------------

drezen(E + "drezen.chart", "Your lights sit low in the north", '"What are you drawing?"', [
    el("start", '''"You." {n}Eliandra turns the chart so that you can see it: a circle of the sky, carefully inked, with the stars of the north crowded into its lower edge and a great many corrections in the margin.{/n}
"This morning's question. I asked Odden what a person's stars were for, in the south, and he said fortune-telling, and I said nonsense, and he said I should try it. So." {n}She taps the chart.{/n} "When were you born, Commander? Under what sky?"''',
       c("[Tell her the truth.]", "truth"),
       c('[Lie] "Midwinter, at midnight, during an eclipse. Obviously."', "lie"),
       c('"I don\'t know. Nobody wrote it down."', "unknown")),
    el("truth", '''{n}She listens gravely, and writes it in the margin, and corrects the chart in three places without crossing anything out.{/n}
"Then I had it nearly right," she says. "I guessed from your face. You have a northern face, whatever your mother thought."''',
       c("Continue", "reading")),
    el("lie", '''"Obviously." {n}She writes it down with perfect seriousness, underneath it writes "a lie, probably", and underneath that "the Commander's", and underlines it twice.{/n}
"An observation that was wrong is still an observation," she says. "It tells you where the eye goes astray. In your case, whenever you are asked a simple question."''',
       c("Continue", "reading")),
    el("unknown", '''"Then I shall choose for you." {n}She says it as though it were the most natural thing in the world.{/n} "I have spent a century choosing things for other people. I am going to allow myself this one." {n}She makes a small mark at the edge of the circle.{/n} "There. Late autumn. The first cold night. The night the lights come back."''',
       c("Continue", "reading")),
    el("reading", '''"Here is your sky." {n}Her finger moves along the lower edge of the circle, where the northern stars are crowded thickest.{/n} "Most of your lights sit low, in the north. Not overhead, where a king's would be, or a saint's. Low, near the edge of what can be seen, where they are easy to miss unless one is sitting down and looking on purpose."''',
       c("Continue", "irony", requires=(LIGHTS_GIVEN,)),
       c("Continue", "plain", forbids=(LIGHTS_GIVEN,))),
    el("irony", '''"And the north is the one part of the sky you cannot look at any more." {n}She says it gently, without pity.{/n} "So I have drawn it for you instead. It is not the same. It is what I can give you, and I am very good at it." {n}She rolls the chart, ties it, and holds it out.{/n} "Keep it. Correct it, if I have made mistakes. Do not cross anything out."''',
       c("[Take the chart.]", "end")),
    el("plain", '''"It suits you. Things are always hiding at the edge of the sky, near the ground, where people have stopped looking up." {n}She rolls the chart, ties it, and holds it out.{/n} "Keep it. Correct it, if I have made mistakes. Do not cross anything out."''',
       c("[Take the chart.]", "end")),
    el("end", '''"That is today's," she says. "Tomorrow's will be harder. I have been working up to the hard ones." {n}For a moment she loses the thread of her own calculation, and does not seem to mind.{/n} "Go away now. I want to watch you carry it."''',
       c("[Carry the chart away where she can see it.]", flags=(CHART,))),
], requires=(FIRST_QUESTION,), forbids=(CHART,), delay=24)


# --- 8. The road: a spring promised --------------------------------------------------------------------------------------------

drezen(E + "drezen.road", "The road into Sarkoris", '"Planning the route already?"', [
    el("start", '''"Planning the first spring." {n}There is a map on the table now, not a chart: old, Sarkorian, the lake below Iz drawn in blue that no longer exists.{/n}
"When your war is done, the clans' land will need everything. Healers, and wells, and priests who remember what the temples were for. I will start at Iz, where the elders used to meet and argue. I intend to reopen a temple of my Lady there, and let it argue with the others." {n}She looks up.{/n} "And I want you on the road with me, the first spring. Only the first. After that you can be in Drezen as much as you like."''',
       c('"The first spring. I\'ll be there."', "yes", flags=(ROAD,)),
       c('"Why the first?"', "why")),
    el("why", '''"Because the first spring after a century is the one I am afraid of." {n}She says it simply.{/n} "I have not been outside a cave in a hundred years without a reason and a sword at my back. I do not know what the land will look like, or what I will feel when I see it. Odden will cry, and the girl with the sling will ask questions, and I would like, for once, to have somebody beside me who is not waiting for me to tell them what to do."''',
       c('"Then the first spring is mine."', "yes", flags=(ROAD,)),
       c('"I can\'t promise it. The war decides where I am."', "war")),
    el("yes", '''{n}She writes something small in the corner of the map, and turns it so you can read it: your name, and "first spring", and underneath, in the same exact hand, "asked, and answered".{/n}
"There," she says. "That is not a vow. I am done with vows. It is a thing I asked for and was given, which is much better, and much more frightening."''',
       c("[Leave her to her map.]")),
    el("war", '''"No. It does." {n}She does not seem hurt.{/n} "Then I will ask again in the spring, when the war has decided. I am allowed to ask every morning. You agreed to it on the ford road, and I have a very good memory." {n}She rolls the map, carefully.{/n} "But I will leave a place on the road beside me, all the same, and I will not let Odden put the mule in it."''',
       c("[Leave her to her map.]", flags=(E + "drezen.road_open",))),
], requires=(CHART,), forbids=(ROAD,), delay=24)


# --- 9. Odden, in a city with wine in it -----------------------------------------------------------------------------------

ODDEN_SPOKE = E + "drezen.odden"


def od(id, text, *choices, **kw):
    return n(id, "Odden", text, *choices, portrait="Odden", **kw)


drezen(E + "drezen.odden", "The dwarf and the cooper", '"Odden looks happier than I\'ve ever seen him."', [
    el("start", '''"He has discovered that in Drezen one may buy wine without hiding it in a boot-chest." {n}Eliandra looks across the room, where the old dwarf is explaining something at great length to a cooper who has plainly heard it before and is listening anyway.{/n} "He came to find me this morning to tell me he had something to say to you, and he has been working up to it ever since. I think he has now had enough wine to be brave. Brace yourself."''',
       c("[Let him come.]", "odden")),
    od("odden", '''{n}Odden arrives at the table with his beard freshly braided and his cup held very carefully level.{/n}
"Commander. A word. Stargazer to commander." {n}He clears his throat.{/n} "I've watched her for a hundred years. Hundred and some. Every evening, the reading. Every morning, the rounds. Never a day off, never a cup of wine, never a word for herself. I thought she was made that way, like a lens is. Ground to it."
"Then you came, and she took a cup at my table, and now she's sitting in Drezen with her feet very nearly up, asking people questions." {n}His eyes are wet.{/n} "I don't know what you did at that basin. She won't say. I don't need to know."''',
       c('"She did most of it herself."', "herself"),
       c('"What did you want to say, Odden?"', "say")),
    od("herself", '''"She did. She does everything herself. That's the trouble with her." {n}He glares at you with enormous affection.{/n} "But she didn't do this one alone. So."''',
       c("Continue", "say")),
    od("say", '''"If you hurt her, I'll tell every tavern in Drezen that you cheat at cards." {n}He holds up a thick finger.{/n} "Every one. And I'll be believed, because I'm very old and I have an honest face."
"That's all. That's the whole speech. I had a longer one, but the wine ate it." {n}He raises his cup to her, and then, after a moment's thought, to you, and drinks, and goes back to the cooper with the air of a dwarf who has discharged a great duty.{/n}''',
       c("Continue", "after")),
    el("after", '''{n}Eliandra has her hand over her mouth. When she takes it away she is trying very hard not to laugh.{/n}
"He practised that," she says. "On me. Twice. The first version had a verse in it." {n}She watches the old dwarf settle back beside the cooper.{/n} "He had a daughter, you know. Ranhild. We never learned what became of her. I think he has decided that since he cannot fuss over her, he will fuss over me. I have decided to let him."''',
       c('"For the record, it\'s a fair question. Whether I cheat at cards."', "cards"),
       c("[Raise your cup to Odden across the room.]", "cup")),
    el("cards", '''"Do you?" {n}Her eyes narrow, with interest rather than disapproval.{/n} "No. Do not answer. I should like there to be one thing about you that I find out for myself. I am told that is how it is done."''',
       c("[Leave the question unanswered.]", flags=(ODDEN_SPOKE,))),
    nar("cup", '''{n}Odden sees you raise it, and raises his back, and the cooper, not knowing why, raises his too, and then half the room is drinking to something none of them could name. Eliandra watches all of it with her hand on her heart, as though this, too, were an observation, and one she means to keep.{/n}''',
        c("[Drink.]", flags=(ODDEN_SPOKE,))),
], requires=(FIRST_QUESTION,), forbids=(ODDEN_SPOKE,), delay=24)


# --- 10. The morning questions ----------------------------------------------------------------------------------------------

QUESTIONS = E + "drezen.questions"

drezen(E + "drezen.questions", "Every morning", '"What is it today?"', [
    el("start", '''{n}Eliandra has a sheet of paper in front of her with a list on it. Several lines are marked through, which is so unlike her that you look twice: not crossed out, you realise, but ticked, each with the day's date beside it in her small exact hand.{/n}
"Today's question," she says, "is a hard one. I have been saving it. I have asked you what you do in the mornings. I have asked you when you were born. I asked you whether you prefer the sea or the mountains, which you did not answer, and whether you have ever been in love before, which you answered badly." {n}She sets the paper down.{/n} "Today I want to know what you are afraid of."''',
       c('"Losing. Anything. Anyone."', "losing"),
       c('"Being stuck. Things that don\'t change."', "stuck"),
       c('[Lie] "Nothing."', "nothing")),
    el("losing", '''"Losing." {n}She writes it down.{/n} "I thought so. You plan like a person who has lost a great deal and does not mean to do it again. Every move three moves ahead, and a door left open behind you in case." {n}She looks up.{/n} "I lost a whole country, Commander, and a hundred years, and a shrine. I am still here. You may find that encouraging, or not."''',
       c("Continue", "her_turn")),
    el("stuck", '''"Things that do not change." {n}She puts the pen down entirely.{/n} "Then you should have been very frightened of me. I kept a shrine exactly as it was for a hundred years. I kept myself exactly as I was." {n}A small, wry smile.{/n} "Regnard was afraid of the same thing. He told me so, and I told him his talent was needed. I will not tell you that. Your talent is needed everywhere; that is the trouble with it."''',
       c("Continue", "her_turn")),
    el("nothing", '''"Nothing." {n}She writes it down, and beside it, carefully, "a lie", and beside that, "a kind one, probably, for my sake".{/n} "An observation that was wrong is still an observation, Commander. I will ask again in a month. The answer will be more interesting then."''',
       c("Continue", "her_turn")),
    el("her_turn", '''"You may ask me one back. That is only fair. I have been taking answers from you for weeks and giving you none." {n}She folds her hands.{/n} "Go on. I will answer anything."''',
       c('"What are you afraid of?"', "afraid"),
       c('"What did you want, at thirteen, before the vow?"', "thirteen", flags=(E + "drezen.sea",)),
       c('"Do you miss any of it? The strength, the vow, the shrine?"', "miss")),
    el("afraid", '''"That I will be very good at this," she says at once, "and then you will die in some breach somewhere, and I will have learned it for nothing, and it will be too late to go back to not knowing." {n}She holds your eyes as she says it, and does not soften it.{/n} "There. You asked."''',
       c("Continue", "end")),
    el("thirteen", '''"To see the sea." {n}She laughs, surprised at herself.{/n} "I had never seen it. Nobody in my clan had. A trader told us it was a lake with no other side, and I did not believe him, and I meant to go and see for myself when I was grown. Then I found my gift, and there was the vow, and there was always something more important than the sea."''',
       c("Continue", "end")),
    el("miss", '''"The shrine, every evening at the hour of the reading." {n}She considers it honestly, the way she considers everything.{/n}''',
       c("Continue", "miss_slow", requires=(REWARD_RETURNED,)),
       c("Continue", "miss_strong", forbids=(REWARD_RETURNED,))),
    el("miss_slow", '''"The strength, every time someone bleeds and I am slow. The vow..." {n}A pause.{/n} "No. I thought I would. I thought it was holding me up. It turns out it was only holding me still."''',
       c("Continue", "end")),
    el("miss_strong", '''"Not the strength. My Lady left me that, and I use it every day, and every day it is heavier, because now I choose each time whom to spend it on. The vow chose for me. The vow..." {n}A pause.{/n} "No. I thought I would miss it. I thought it was holding me up. It turns out it was only holding me still."''',
       c("Continue", "end")),
    el("end", '''{n}She adds one more line to the paper and turns it so that you can read it: today's date, and beside it, "asked and answered, both ways".{/n}
"Tomorrow," she says, "I am going to ask you something easy, as a rest. I have not decided what. Something about horses, perhaps. I know nothing whatever about horses."''',
       c("[Promise to be an expert on horses by tomorrow.]", flags=(QUESTIONS,))),
], requires=(CHART,), forbids=(QUESTIONS,), delay=24)


# --- 11. Lann's question (after his word on the veil) ----------------------------------------------------------------------

LANN_ANSWERED = E + "drezen.lann_answered"

drezen(E + "drezen.lann", "Somebody looking at the sky", '"Lann asked me to ask you something."', [
    el("start", '''"Lann." {n}Eliandra sets down her pen.{/n} "The young archer with the Wound in his bones. He watches me across the yard as though I owed him money." {n}She folds her hands.{/n} "Ask."''',
       c('"Whether anyone behind the veil ever looked out and thought about his people. The ones in the caves."', "ask")),
    el("ask", '''{n}She does not answer quickly. When she does, it is in the voice of the evening reading, slow and exact.{/n}
"Yes. Every winter, at the solstice, Odden set a lamp in the east window of the library, where it could not be seen through the veil but could be seen from inside by anyone who looked east. It was for the ones outside. All of them. The clans who would not run, the crusaders who came too late, and the children in the caves who were born into the Wound and never knew there had been anything else."
"It did them no good at all. We knew that. We lit it anyway, for a hundred years."''',
       c('"I\'ll tell him."', "tell"),
       c('"Tell him yourself."', "yourself")),
    el("tell", '''"Tell him also that I am sorry, and that I know it is not enough, and that I do not expect him to forgive a veil for doing what veils do." {n}She pauses.{/n} "And tell him that there is a lamp in my window in Drezen now, at the east side. It is not for anyone in particular. He may take it personally, if he likes."''',
       c("[Take her message to Lann.]", flags=(LANN_ANSWERED,))),
    el("yourself", '''{n}Something shifts in her face: fear, very briefly, and then a decision.{/n} "Yes," she says. "You are right. I have sent other people to say hard things for me for a hundred years." {n}She stands, and smooths her robe, and looks across the room towards the door as though it were a long way off.{/n} "Where does he keep himself? I will find him before the evening reading, and I will say it to his face, and he may be as angry with me as he likes. I have earned it."''',
       c("[Tell her where to find him.]", flags=(LANN_ANSWERED,))),
], requires=(E + "react.lann_veil",), forbids=(LANN_ANSWERED,), delay=12)


# --- 12. Ramien's dream (read only if the Desnan saw his dream come true at Pulura's Fall) --------------------------------

RAMIEN_DREAM = "eliandra.ramien_dream"   # SeenCues RamienPulura/Cue_0007 cb298915: the northern lights and a priestess
RAMIEN_TALKED = E + "drezen.ramien"

drezen(E + "drezen.ramien", "The priest who dreamed of the waterfall", '"I hear Ramien has been to see you."', [
    el("start", '''"Three times." {n}Eliandra looks faintly beleaguered.{/n} "The priest of the Song of the Spheres. He is very kind, and very young, and he says he dreamed of me. The northern lights over our valley, the waterfall parting, and a woman dressed as a priestess who pointed him towards the demons and said a single name." {n}She turns her cup of water round.{/n} "He came to Pulura's Fall because of it. He says it saved us."''',
       c('"Did it?"', "saved"),
       c('"Was it you?"', "you")),
    el("saved", '''"It brought him, and he brought you, or you brought him; the order is disputed and I have stopped asking." {n}She almost smiles.{/n} "Desna sends dreams, and my Lady sends lights, and they have always been friends, in the way of goddesses: at a great distance, and with a great deal of mutual approval. If one of them lent the other a waterfall for a night, I will not complain."''',
       c('"Was it you in the dream?"', "you")),
    el("you", '''"No." {n}Then, more honestly:{/n} "I do not know. I did not dream it. I was asleep in my cell, and I dreamed about what I always dreamed about, which was the lake below Iz before the Wound." {n}She looks at her hands.{/n}
"He says the woman in his dream had my face. I told him it was my Lady, and that she often borrows her servants' faces when she wants to be looked at kindly. He said that was the most beautiful thing he had ever heard, and wrote it down, and I suspect it will be in a sermon by the end of the week."''',
       c('"Is it true?"', "true"),
       c('[Flirt] "I\'d believe it. She has good taste in faces."', "flirt")),
    el("true", '''"I have no idea." {n}Serenely.{/n} "It is the kind of thing that ought to be true. After a hundred years of vigil I have learned that the gods rarely correct a kind story, and never correct a sermon." {n}She sips her water.{/n} "He also asked whether I would bless the new window in his chapel. I said yes. I have never blessed a window. I expect it will go perfectly well."''',
       c("[Leave her to her windows.]", flags=(RAMIEN_TALKED,))),
    el("flirt", '''{n}Eliandra looks at you over the rim of her cup with an expression that, on any other woman, you would call smug.{/n}
"You say that," she says, "to a woman who has just been told by a priest of Desna that she appears in divine visions. You will have to do better than that, Commander. Try again tomorrow. I will be insufferable until then."''',
       c("[Leave her to be insufferable.]", flags=(RAMIEN_TALKED,))),
], requires=(RAMIEN_DREAM,), forbids=(RAMIEN_TALKED,), delay=24)


def integrate(payload):
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = copy.deepcopy(value)
