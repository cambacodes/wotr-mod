"""Eliandra, Chapter 5 in Drezen: after the star-heart (the courtship on her presence; 11-ROSTER-PLAN-2 §2 build sheet).

The stargazers come to Drezen with the high priestess who has let her Lady go. F10 authored staging moves her primary
table to the ordinary tailor's frontage (8 m; live proof 20261005-100808), preserving the King's-gone fallback gates.
F11 authored staging puts the fallback beside the jeweller, about four metres left and four metres forward.
The old Angel-path mark was off the walkmesh beside Yaniel; the offset leaves Nidalynn her steps. Every beat is Trickster-only (T): it follows the device and the yes.

The beats: the city (her first morning question); the stone (the King's tavern only); the lights she can see and the
Commander cannot; the healing that tires her now; Katair and his own grave at the Stone Tree (Ranger_main Cue_0016-0023);
Threshold and the woman she saw there; the chart of the Commander's sky; the road into Sarkoris.
"""
import copy

from story_format import c, n, scene
from storylines.eliandra_trickster import (
    CHARTS, CLOSED, COMMITTED, DEAD, DECLINED, DREZEN, E, FLIRTED, HEALING_SEEN, HEART_SEEN, LEAVE, LETTER_ANSWERED,
    LIED_ABOUT_HAND, LIGHTS_GIVEN, LIGHTS_SEEN, MET, NO_LEAVE, PATH_FIT, REFUSED_FOR_HER, REL, REWARD_RETURNED, TABLET,
    TRIED_TO_CHEAT, UNIT)
from storylines.eliandra_trickster import FLIRTED, LOVERS_SPOKEN, OBSERVED, REMEMBRANCE, SARKORIS_TOLD, TERMS_READ
from storylines.eliandra_trickster import SCENES as SCENES_MAIN

SCENES = []

TAILOR = "253cdb8f434e5a6469b75e18428316e3"  # F10: front 8 m. Live proof 20261005-100808.
FOOL_KING = "cc50a88bbd8dd3e4da066d33d14fdfc8"       # FoolKing (MythicTrickster_Ch3), in his tavern in DrezenCapital
JEWELLER = "bc1093231b1577a4485a730c29595195"  # JewelerCapitalTrader; ordinary Ch3/Ch5 capital trader
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

GREETING = ("{n}At a table in the open ground between the tailor's and the jeweller's stalls, out of the worst of the street noise, a woman in a grey travelling cloak sits with a cup "
            "of water in front of her and a star chart spread under her hands. The passers-by give her table a wide, respectful "
            "berth, as though it were an altar.{/n}")
PRESENCES = {
    # Front of the ordinary tailor, 8 m: 4.5 m from the evil Arueshalae fallback; pending live.
    # The existing King-gone and failure gates still select the fallback.
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TAILOR, Side="front", Distance=8.0),
              Requires=["trickster.ever", MET], Forbids=[CLOSED, DEAD, "eliandra.attacked", "eliandra.trickster.away", HUB_FAILED, KING_GONE], MinChapter=5,
              MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # F11 authored fallback: street left/front of the jeweller, away from Nidalynn at left 2.5 m.
    # World offset (merchant faces about -15 degrees): about 4.2 m left / 4.4 m front. Pending Ground-only live proof.
    HUB_ALT: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=JEWELLER, Offset=[-5.2, 3.2]),
                  Requires=["trickster.ever", MET], Forbids=[CLOSED, DEAD, "eliandra.attacked", "eliandra.trickster.away"], MinChapter=5, MaxChapter=5,
                  RequiresAnyGroups=[[HUB_FAILED, KING_GONE]], AnswerLists=[], Dialog="hub",
                  Greeting=("{n}To the left of the jeweller's stall, a little way into the street, a woman in a grey travelling cloak sits with a star chart across "
                            "her knees, watching the street as though it were a sky she had not learned yet.{/n}")),
}


def el(id, text, *choices, **kw):
    return n(id, "Eliandra", text, *choices, portrait="Eliandra", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Eliandra", **kw)


def kt(id, text, *choices, **kw):
    return n(id, "Katair", text, *choices, portrait="Katair", **kw)


PLACES = ((HUB, "", {}), (HUB_ALT, "_mark", dict(RequiresAnyGroups=[[HUB_FAILED, KING_GONE]])))


def drezen(id, title, entry, nodes, requires, forbids=(), delay=0, places=PLACES, heart=True, **fields):
    """A beat on her presence (the tailor's frontage, or the jeweller's street): the same scene on each, each forbidding the other."""
    ids = [id + suffix for _, suffix, _ in places]
    for hub, suffix, extra in places:
        sid = id + suffix
        PATH_FIT[sid] = "T"
        SCENES.append(scene(sid, title, "Eliandra", 5, entry, copy.deepcopy(nodes),
                            requires=("trickster.ever", *((HEART_SEEN,) if heart else (MET,)), *requires),
                            forbids=(CLOSED, DEAD, "eliandra.attacked", "eliandra.trickster.away", *[o for o in ids if o != sid], *forbids), delay=delay, last=5,
                            Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=hub,
                            RequiresAnyGroups=[list(g) for g in fields.get("RequiresAnyGroups", [])]
                            + [list(g) for g in extra.get("RequiresAnyGroups", [])],
                            **{k: copy.deepcopy(v) for k, v in fields.items() if k != "RequiresAnyGroups"}))


# --- 0. The persistent host (audit r4). Her native unit belongs to the captive pool that Pulura_Chapter05_Mechanics destroys
# once C5_MutasafenFall_quest completes (the greeting completes it), so she cannot be found at the shrine on a later visit. The
# stargazers come to Drezen ("I will lead the survivors somewhere safe", Cue_0030), and her presence stands there from the
# meeting on. The terms and the rite are also offered there (twins of the shrine scenes); her own offering, the first mile and
# the shrine's last night are hosted only there.

def also_in_drezen(scene_id, entry):
    """Twins of a shrine scene on her presence (tailor and jeweller): same nodes, each twin forbidding the others."""
    original = next(s for s in SCENES_MAIN if s["Id"] == scene_id)
    ids = [scene_id] + [scene_id + "_drezen" + suffix for _, suffix, _ in PLACES]
    for hub, suffix, extra in PLACES:
        sid = scene_id + "_drezen" + suffix
        PATH_FIT[sid] = "T"
        twin = copy.deepcopy(original)
        twin.pop("AnswerLists", None)
        twin.pop("NativeReturnCue", None)
        twin.update(Id=sid, Entry=entry, Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=hub,
                    Forbids=list(dict.fromkeys(original["Forbids"] + ["eliandra.trickster.away"] + [o for o in ids if o != sid])),
                    RequiresAnyGroups=[list(g) for g in original.get("RequiresAnyGroups") or []]
                    + [list(g) for g in extra.get("RequiresAnyGroups", [])])
        if scene_id == E + "ch5.last_rite":
            # R4 D02/D03: authored travel from either capital host, not a
            # restored sanctuary. The evacuation and offering remain intact.
            nodes = {node["Id"]: node for node in twin["Nodes"]}
            nodes["start"]["Text"] = nodes["start"]["Text"].replace(
                "My people are packing.", "My people are preparing for the road north.")
            nodes["leave"]["Text"] = nodes["leave"]["Text"].replace(
                "Someone nearby is nailing a stargazer's crate shut.",
                "Across the street, a stargazer is nailing a supply crate shut.")
            for ident in ("heart_new", "heart_known"):
                nodes[ident]["Text"] = (
                    "{n}You leave Drezen with Eliandra and a small crusader escort. "
                    "At Pulura's Fall, the soldiers search the approach and the empty corridors "
                    "before taking watch outside the star-heart. The demons know this place; "
                    "the stargazers' evacuation stands. This visit is for the rite alone.{/n}\n"
                    + nodes[ident]["Text"])
        SCENES.append(twin)
    original["Forbids"] = list(dict.fromkeys(original["Forbids"] + ids[1:]))


also_in_drezen(E + "ch5.terms", '"What does your Lady take, in return for what she gives?"')
also_in_drezen(E + "ch5.last_rite", '"Will you hold one last rite at the star-heart? For yourself, this time."')


def drezen_pre(id, title, entry, nodes, requires, forbids=(), delay=0, **fields):
    """A device or commit beat on her presence, before the star-heart."""
    drezen(id, title, entry, nodes, requires, forbids=forbids, delay=delay, heart=False, **fields)


drezen_pre(E + "ch5.observe_drezen", "The reading on the wall", '"Will you take your evening reading tonight? I\'d like to watch."', [
    el("start", '''"On the north wall, at dusk. The shrine is gone; the sky is not." {n}Eliandra considers you, as she considers a question that is not quite the one being asked.{/n} "Come, then. Say nothing unless I ask, and touch nothing made of brass. I have carried every lens I own up those stairs, and I will not carry them down again in pieces."''',
       c("[Go up to the north wall at dusk.]", "wall")),
    nar("wall", '''{n}She sets out her lenses on the parapet in the angle of a tower, out of the wind, with a chart pinned flat under four river stones she has carried all the way from the dry fall. The sky over Drezen is not the sky of the star-heart: there is smoke in it, and the Wound's red glare low in the north. She reads it anyway. Her lips move. Her pen moves. When she makes an error she writes the correction beside it and leaves the error where it is.{/n}
{n}Once, low over the Wound, there is a flicker at the edge of your sight: green, gone before you can look at it. She glances at you, sees that you saw it, and says nothing.{/n}''',
        c("Continue", "done")),
    el("done", '''{n}At last she lowers the lens.{/n} "That is what my Lady is," {n}she says.{/n} "Not gold. Not temples. The patience to look, every evening, and the lights at the edge of it. If you still mean to make her an offering, now you know what she will be weighing it against."''',
       c("[Thank her, and go down.]", flags=(OBSERVED,))),
], requires=(), forbids=(OBSERVED, TERMS_READ, LEAVE, NO_LEAVE), delay=0)

drezen_pre(E + "ch5.self_offering", "Her own offering", '"You sent for me?"', [
    el("start", '''"I did. Come up to the north wall tonight." {n}Eliandra has the stargazers' crates stacked round her, roped and labelled in her small exact hand, and she does not look at any of them.{/n} "I have had the basin carried up there. My Lady's rite is made under the open stars, and the wall is the nearest open sky in this city that nobody will walk across."''',
       c("[Go up to the north wall at nightfall.]", "heart")),
    nar("heart", '''{n}The north wall of Drezen is black and bitter and nearly empty. The great bronze basin from the star-heart stands in the angle of a tower, brimming, with the true sky lying in it, and the Wound's red glare low on the horizon beyond.{/n}
{n}She kneels at it without a word. From the look of her knees, she has been kneeling at it, one way or another, for much of the last two days.{/n}''',
        c("Continue", "refused", requires=(REFUSED_FOR_HER,)),
        c("Continue", "cheated", requires=(TRIED_TO_CHEAT,), forbids=(REFUSED_FOR_HER,)),
        c("Continue", "walked", forbids=(REFUSED_FOR_HER, TRIED_TO_CHEAT))),
    el("refused", '''"You refused it for me," {n}she says, without turning round.{/n} "You meant it kindly, and it was not yours to refuse. I have thought about that for two days. It is exactly what I did to Vestari and Cristry for a hundred years, and I did not see it until someone did it to me."''',
       c("Continue", "mine")),
    el("cheated", '''"You tried to cheat her," {n}she says, without turning.{/n} "In the heart of my shrine, with your hand behind your back." {n}She is quiet.{/n} "I do not know why, and I am not going to guess on your behalf. That is between you and her, and between you and me, and neither of those is finished."
"This is not for you. It is my vow, and I will not have my release bought with a lie. So I will pay for it myself, honestly, and you will stand at the stair and watch it done properly."''',
       c("[Stand at the stair.]", "kneel")),
    el("walked", '''"You walked away from the basin," {n}she says, without turning.{/n} "At first I thought your nerve had failed. Then I thought that you had understood what you were about to give, and could not give it lightly. I have decided that I prefer the second."''',
       c("Continue", "mine")),
    el("mine", '''"So I will do it myself. Properly. Under the open stars, aloud, something I love, from her own domain." {n}She holds her right hand out over the water, palm down. The green shimmer lies on it, faint as breath.{/n} "She gave me this for what I gave her. I will give it back, and ask for nothing in return, and see what she does. It is the only offering I have that is truly mine."''',
       c("[Kneel beside her.]", "kneel"),
       c('"Eliandra, don\'t. Let me try again."', "again")),
    el("again", '''"No." {n}Very gentle, and not open to argument.{/n} "It is my vow. It should be my offering. I have let other people pay for my rules for a hundred years, Commander. Not this time."''',
       c("[Kneel beside her.]", "kneel")),
    nar("kneel", '''{n}She speaks to the water. You do not hear all of it; some of it is in no language you know, and some of it is only her name for her Lady, said over and over the way a child says a parent's name in the dark. Then, in plain words: "I give it back. Keep it. I am not the strongest of your servants any more. I am only yours."{/n}
{n}The shimmer leaves her hand. It goes down into the basin like a coin into a well, slowly, turning, and the water closes over it. For a while nothing happens at all.{/n}
{n}Then the stars in the basin move. Not a heartbeat behind the sky, as they always have: with it. Exactly with it, as though the water had stopped remembering and begun to see.{/n}''',
        c("Continue", "free")),
    el("free", '''{n}Eliandra lets out a breath that goes on and on. She sits back on her heels and puts both hands over her face, and when she takes them away she is laughing and crying at once, and does not seem to know which.{/n}
"She let me go," {n}she says.{/n} "Just like that. For the giving, and a little light." {n}She looks at her empty hand.{/n} "Katair will say I have made a terrible bargain. He will be right about the bargain. He will be wrong about everything else."''',
       c("[Help her up.]", flags=(LEAVE, REWARD_RETURNED)),
       c("[Sit down on the cold stone beside her instead.]", flags=(LEAVE, REWARD_RETURNED))),
], requires=(NO_LEAVE,), forbids=(LEAVE,), delay=48, TricksterDevice=True, TricksterState="no_leave")


drezen_pre(E + "ch5.evening", "Two people on a wall", '"You look as if you haven\'t slept since the basin."', [
    el("start", '"No, I have not slept." {n}She shifts along the crate and lifts the edge of her cloak for you. The stargazers\' last cases stand roped beside her; beyond them the night watch crosses the street.{/n} "Sit here. Odden will inspect the knots at dawn. Until then I need neither a report nor a prayer."',
       c("[Sit beside her.]", "ask")),
    el("ask", '''"You came to help us against the demons. You stayed to ask about my Lady. The crusade must have needed you elsewhere. Why stay?"''',
       c('"I wanted to ask about you, for once."', "first"),
       c('[Flirt] "Because I wanted to find out what you look like when you forget to be the high priestess."', "forget", flags=(FLIRTED,)),
       c('"I don\'t know. I kept finding reasons to come back."', "reasons")),
    el("first", '"About me?" {n}She takes your hand beneath the cloak.{/n} "Then stay. I should like to be asked while I have no hammering to shout over."',
       c("Continue", "close")),
    el("forget", '"Tired. Irritable. Quite capable of wanting you here." {n}She looks directly at you, her knee touching yours beneath the cloak.{/n} "Keep looking. I have put the charts away."',
       c('"It is to me."', "close")),
    el("reasons", '"So did I. I nearly sent a warden with a question about the road." {n}She moves closer.{/n} "You saved him a cold walk. Sit here."',
       c("Continue", "close")),
    nar("close", '{n}She rests against your shoulder and keeps your hand beneath her cloak. When the last street lamp goes dark she turns towards you; her mouth brushes your cheek. She stays there until the watch changes.{/n}\n{n}At the first grey light she straightens. A carter is already checking the wheels.{/n} "The morning after this one. Walk with me from the north gate. I have something to ask you before we take the carts out."',
        c("[Promise to walk with her.]", flags=(E + "drezen.evening",))),
], requires=(LEAVE,), forbids=(COMMITTED, DECLINED, E + "drezen.evening"), delay=6)

drezen_pre(E + "ch5.first_mile", "The first mile", '"Walk with you? Where?"', [
    el("start", '''"Out of the north gate, at first light. A mile along the old road, and back." {n}Eliandra is already in a grey travelling cloak, her hair pinned up under the hood; she looks like any priestess on any road.{/n} "The carts are nearly ready. I mean to lead them into what is left of Sarkoris. I want to see the first mile of it before I lead anyone down it."''',
       c("[Walk out of the gate with her at first light.]", "gate")),
    nar("gate", '''{n}The road north out of Drezen is ash and old ruts and frost, and she walks it as if the open road were a floor that might give way under her; she had not left her valley in a hundred years until the carts brought her here. The gate guards watch her go with frank curiosity. She does not notice.{/n}''',
        c("Continue", "lights", requires=(LIGHTS_GIVEN,)),
        c("Continue", "tired", requires=(REWARD_RETURNED,), forbids=(LIGHTS_GIVEN,)),
        c("Continue", "road", forbids=(LIGHTS_GIVEN, REWARD_RETURNED))),
    el("lights", '''{n}She keeps glancing up. The sky is barely grey, and low in the north, over the Wound, there is a smear you cannot quite look at: your eyes slide off it to a cloud, a crow, a cart-rut.{/n}
"They are still out," {n}she says.{/n} "The last of them. Green, very pale, going rose at the edges where the sun is coming. They are always brightest just before they go." {n}She glances at you, and away.{/n} "I shall describe them whenever you ask. You may regret asking."''',
       c("Continue", "tired_too", requires=(REWARD_RETURNED,)),
       c("Continue", "road", forbids=(REWARD_RETURNED,))),
    nar("tired_too", '''{n}She stumbles once on a frozen rut, and catches herself, and does not look at you. Last night she sat up with a stargazer's fever, and it took her until the small hours, and it would not have before she gave the gift back. Nobody said anything about it at breakfast. All of them noticed.{/n}''',
        c("Continue", "road")),
    nar("tired", '''{n}She walks slowly. Last night she sat up with a stargazer's fever, and it took her until the small hours, which it would not have before she gave the gift back; Odden said nothing about it at breakfast, loudly.{/n}
{n}Low in the north, over the Wound, the last of the night's lights are fading. You can see them, pale green going rose. She looks at them once, and then at you, as if to be sure you still can.{/n}''',
        c("Continue", "hand", requires=(TRIED_TO_CHEAT,)),
        c("Continue", "road", forbids=(TRIED_TO_CHEAT,))),
    el("hand", '''{n}Half a mile out she speaks without turning her head.{/n} "Before I ask you anything, you will answer me one thing, and you will answer it plainly, or I will ask you nothing at all." {n}Her voice is quite even.{/n}
"In the heart of my shrine you knelt across the basin from me with your hand behind your back. What did you mean to do with it?"''',
       c('[Tell her the truth] "Take the leave, then find a loophole later and get the lights back."', "owned"),
       c('[Lie] "Nothing. A cramp. You read too much into it."', "lied", flags=(DECLINED, LIED_ABOUT_HAND))),
    el("owned", '''{n}She walks on for a while.{/n} "Thank you," {n}she says at last.{/n} "That is an ugly answer, and it is the true one. I would rather have the ugly true thing than a pretty lie, from you, every morning for the rest of my life." {n}She does not smile.{/n} "I have not forgiven it. I may. Walk with me to the milestone."''',
       c("Continue", "road")),
    el("lied", '''{n}She stops in the road.{/n}
"My Lady saw your hand," {n}she says.{/n} "I saw your hand. And you stand in the open road with her lights still in the sky and tell me it was a cramp." {n}She looks at you with no anger at all, which is worse.{/n} "I was going to ask you something. I will not, today. Go back to your war, Commander. We leave for the fords in a few days. If I ever know what to do with you, I will write."''',
       c("[Let her walk back alone.]")),
    el("road", '''{n}The first mile is not a long way. At a milestone half-buried in ash Eliandra stops, and looks north along the road, and then back at the walls of Drezen, and then at you.{/n}
"The carts will be ready soon. I want your answer before we leave." {n}She turns away from the road to face you.{/n} "For me, this time."''',
       c("Continue", "ask")),
    el("ask", '''"Drezen," {n}she says,{/n} "or the road?" {n}She holds your eyes.{/n} "When your war is done. Will you have me in Drezen, in your city, with walls around us? Or will you walk the road with me into whatever is left of Sarkoris, and help me find out what it is?"
"I am asking you, Commander. I want to be told."''',
       c('[Either. Ask me every morning.] "Either. Both. Ask me every morning, and I\'ll give you a different answer every day."', "yes",
         flags=(COMMITTED,)),
       c('[Tell her to leave the stargazers] "Drezen. Just you. Let Odden take them on."', "no", flags=(DECLINED,)),
       c('[Wish her well] "The road is yours, Eliandra. Go well."', "farewell", flags=(CLOSED,))),
    el("yes", '''{n}She laughs: short, startled and entirely unguarded. A carter on the road turns round to look.{/n}
"Every morning," {n}she says.{/n} "You will regret that. I have a hundred years of questions saved up." {n}She reaches out and takes your hand, deliberately, the way she would set a lens to her eye. Her fingers are cold from the road. She does not let go.{/n}
"The heart of the shrine is still open," {n}she says, more quietly.{/n} "I left it for last. Ride back with me to the dry fall, Commander, and help me close it."''',
       c("[Walk back to the gate with her.]")),
    el("no", '''{n}Eliandra looks north along the road. The carts are still waiting at the gate.{/n}
"You ask me to abandon the only people I have," {n}she says.{/n} "The ones who are left. Odden, who has no one. The girl with the sling, who does not know how to be anywhere but a cave." {n}She is not angry. That would be easier.{/n} "I cannot. I will not. If that is the only way you will have me, then you will not have me, and I will have asked for nothing after all."
"Go back to your war, Commander. We leave for the fords in a few days. I will write, when I know where we are."''',
       c("[Let her walk back alone.]")),
    el("farewell", '''{n}Something moves across her face and is put away, neatly, the way she rolls a chart.{/n}
"Thank you," {n}she says.{/n} "For the rite. For everything you gave that you did not have to." {n}She lays her hand on her heart and bows: the full bow of a high priestess to an honoured guest.{/n} "Farewell, Commander. Pulura's children will remember you."''',
       c("[Watch her walk back to the gate.]")),
], requires=(LEAVE,), forbids=(COMMITTED, DECLINED), delay=24,
    RequiresAnyGroups=[[LOVERS_SPOKEN, OBSERVED, FLIRTED, E + "eyes_kissed", E + "vow_told", REMEMBRANCE, SARKORIS_TOLD, E + "drezen.evening"]])


drezen_pre(E + "visit.star_heart", "The shrine's last night", '"Is the heart still open?"', [
    nar("start", '''{n}In Drezen, Eliandra rolls her last chart and reaches for her travelling cloak.{/n}''',
        c("Continue", "walk_back", forbids=(LETTER_ANSWERED,)),
        c("Continue", "ride_back", requires=(LETTER_ANSWERED,))),
    nar("walk_back", '''{n}You ride from Drezen together with a small crusader escort. At the dry fall the soldiers search the approach and the empty shrine, then take turns watching the entrance through the night. The demons know where the temple stands; one guarded visit will not make it a refuge again. Inside, Eliandra carries the lamp past the empty cells and stops at each door before leading you to the star-heart.{/n}''',
        c("Continue", "heart")),
    nar("ride_back", '''{n}Since your meeting beside the tailor's, she has kept the last chart for this journey. Odden still has the column at the fords. You leave Drezen together with a small crusader escort. At the dry fall the soldiers search the approach and the empty shrine, then take turns watching the entrance through the night. The temple's secrecy is lost; they can guard this visit, not settle her people here. Eliandra takes your hand at the hidden door and leads you to the star-heart.{/n}''',
        c("Continue", "heart")),
    nar("heart", '''{n}The star-heart is bare to the rock. The basin went with the carts; the long table did not, being too heavy to move, and her last charts lie on it half rolled, weighted with river stones. Overhead the sky burns, black and enormous, as it has burned for a century and will burn when there is nobody under it at all.{/n}
{n}Eliandra sets the lamp down and blows it out. There is enough light without it.{/n}''',
        c("Continue", "her")),
    el("her", '"The last reading is packed. The door can wait until morning." {n}Eliandra sets her palm on the bare table, then turns to you.{/n} "I asked you here because I want you to stay with me tonight."',
       c("Continue", "look", requires=(LIGHTS_GIVEN,)),
       c("Continue", "look_up", forbids=(LIGHTS_GIVEN,))),
    el("look", '''"There are lights over the north tonight. You cannot see them. I can." {n}She steps closer, close enough that you can smell the road on her cloak, and cedar, and ink.{/n} "Look at me, then," {n}she says.{/n} "I will look up for both of us."''',
       c("Continue", "want", requires=(E + "dead_named",)),
       c("Continue", "want_rite", forbids=(E + "dead_named",))),
    el("look_up", '''"You kept your sight. I gave her the strength back. I am still her priestess." {n}She steps closer, close enough that you can smell the road on her cloak, and cedar, and ink.{/n} "Look up, then, while I look at you. I have looked at the sky long enough."''',
       c("Continue", "want", requires=(E + "dead_named",)),
       c("Continue", "want_rite", forbids=(E + "dead_named",))),
    el("want_rite", '"You asked what my Lady would take, and what I might ask of her. I remembered that on the road." {n}She lays her hand against your chest and comes closer.{/n} "The offering is done. This is what I want now. Kiss me, Commander."',
       c("[Kiss her.]", "robes"),
       c('[Flirt] "I\'ll show you. Slowly. We have all night."', "robes"),
       c('[Flirt] "The stars can wait."', "robes", requires=(FLIRTED,))),
    el("want", '"You asked who I had lost when there were bodies waiting to be carried out. I remembered that on the road." {n}She lays her hand against your chest and comes closer.{/n} "The offering is done. This is what I want now. Kiss me, Commander."',
       c("[Kiss her.]", "robes"),
       c('[Flirt] "I\'ll show you. Slowly. We have all night."', "robes"),
       c('[Flirt] "The stars can wait."', "robes", requires=(FLIRTED,))),
    nar("robes", '{n}Her first kiss misses the corner of your mouth. She catches your face between her hands and tries again, firmly enough to leave you breathless. Your fingers catch on the pin at her throat.{/n}\n{n}She pushes them aside, unpins her cloak herself, and loosens the ties of her white robes while looking straight at you. When you reach for her again, she pulls you in.{/n}',
        c("Continue", "wrist")),
    nar("wrist", '{n}The loosened robes slip from her shoulder. You kiss the exposed skin; her fingers tighten in your hair. When your mouth reaches her wrist, she turns her hand to hold your cheek.{/n} "Closer." {n}She says your name against your mouth and pulls you to her.{/n}',
        c("Continue", "learn")),
    nar("learn", '''{n}She pulls your shirt free and lays both hands against your ribs. Her fingers pause over a scar; her breath catches against your throat. She takes your hand and presses it to her bare waist.{/n} "Here. I want your hands here." {n}Her teeth close lightly on your shoulder. Her thigh presses between yours; the loosened white robes gather at her hips. She pulls you closer, then backs against the table without letting go.{/n}''',
        c("Continue", "charts")),
    nar("charts", '{n}She catches a chart beneath her elbow and pushes it clear. The river stones clatter to the floor. The remaining rolls slide after them, still tied; she watches them fall, then draws you in against her at the edge of the bare table.{/n} "They can be picked up. Come here."\n{n}Her hands go to your belt before you have finished obeying, exact and unembarrassed, the way she handles every difficult task. The white robes are bunched at her hips; she hauls them higher, and the lamp finds her bare skin, pale against the dark wood. She takes your hand from her waist and lays it flat against her ribs, over the hammering of her heart, and watches your face while you feel it.{/n}\n"Not so careful," {n}she says, a little breathless, and bites at your lower lip.{/n} "I have spent a hundred years being careful. Harder. There."\n{n}She arches with her head tipped back and the lights of the dead shrine going over her throat. When she cannot stand any more of it she drags your clothes open and pulls you in against her until nothing is left between you but the next breath, and she says your name like a woman reading a star she has finally found.{/n}',
        c("Continue", "morning")),
    nar("morning", '{n}You wake beneath her cloak with a star chart stuck to your back. Eliandra is pressed along your side, her hair caught under your shoulder. She frees it with an irritated tug and kisses you before getting up.{/n}\n{n}By the time boots sound in the corridor she is dressed and kneeling among the charts. A scarred man with a bow stops in the doorway. Katair looks from the empty shrine to the cloak and your bare shoulder, then to Eliandra. She keeps hold of the roll she has tied wrong.{/n}',
        c("Continue", "katair")),
    kt("katair", '''"I was beyond the walls," {n}says Katair.{/n} "Days. I came back to a sacked shrine and an empty valley, and found the carts' tracks going to Drezen, and Odden in Drezen, who told me you had come back here and would not tell me why." {n}His voice is perfectly level. His hands are not, quite.{/n} "Regnard. Taeriell. The lovers."
{n}It is not a question. Eliandra nods.{/n}
"I was not here," {n}he says.{/n}''',
       c('"She was. She held the rest of them together."', "answer"),
       c("[Say nothing. Let her answer him.]", "answer")),
    el("answer", '''"No," {n}says Eliandra,{/n} "you were not, and you will carry that, and I cannot stop you." {n}She stands, with the charts in her arms.{/n}''',
       c("Continue", "answer_given", requires=(LIGHTS_GIVEN,)),
       c("Continue", "answer_self", forbids=(LIGHTS_GIVEN,))),
    el("answer_given", '''"My Lady has released me, Katair. The Commander made an offering in my place, and I have made my choice." {n}She lifts her chin.{/n} "I am not going to be ashamed of it in front of you."''',
       c("Continue", "wrong")),
    el("answer_self", '''"I gave my Lady back her gift, Katair. Myself, at the basin, with nobody's hand but mine. She let me go. And then I made my choice." {n}She lifts her chin.{/n} "I am not the strongest of her servants any more, and I am not going to be ashamed of any of it in front of you."''',
       c("Continue", "wrong")),
    kt("wrong", '{n}Katair takes the charts from her arms and examines their ties.{/n} "The north is on the outside. Every one." {n}He looks towards the discarded cloak, then back at her.{/n} "The column leaves soon. Who is tending the wounded?"\n"I am," {n}Eliandra answers.{/n} "As I was yesterday. I will be at the carts when they leave."\n{n}Katair loosens one tie and checks the observations. His hand stops at Taeriell\'s name in the margin.{/n} "I should have been here."',
       c('"The column still has its priestess."', "end"),
       c('"Ask her. I am staying out of this."', "end")),
    nar("end", '{n}Katair goes to see to the horses. Eliandra watches him leave, then puts the charts in your arms and retrieves her cloak.{/n} "He will have questions for the column. I will answer those too." {n}She catches your mouth in a brief kiss before pinning the cloak.{/n} "I wanted you here. I still do. Now help me carry these out before he brings the horses through the door."',
        c("[Help her carry them out.]", flags=(HEART_SEEN, CHARTS))),
], requires=(COMMITTED,), forbids=(HEART_SEEN,), delay=12)


# --- 1. The city: her first morning question --------------------------------------------------------------------------------

drezen(E + "drezen.city", "A city with walls", '"How are you finding Drezen?"', [
    el("start", '''"Loud." {n}Eliandra says it with a kind of wonder.{/n} "I had forgotten that a city is loud all night. In the shrine the loudest thing after dark was Odden snoring, and we moved him to the far cell in the forty-third year." {n}She turns her cup of water in her hands.{/n}
"There are children everywhere. There were no children in Pulura's Fall. I had forgotten that too. A little boy asked me this morning whether I was a ghost, because I was so pale, and I told him I was only old, and he said that was worse."''',
       c('"Are the others settled?"', "others"),
       c('"You don\'t look old."', "old")),
    el("others", '''"Odden found us rooms above a cooper's, near the citadel. The cooper is a widower, and Odden has already told him about his daughter Ranhild, twice, and been told about the cooper's son, three times, and they are now inseparable." {n}A small smile.{/n} "The wardens have gone to your quartermaster to ask for work. The girl with the sling is learning to be a scullion somewhere with windows. They are frightened, all of them, and none of them has asked to go back."''',
       c("Continue", "ask")),
    el("old", '''"I led that shrine for a hundred years, Commander. I look it in the mornings." {n}She does not seem displeased.{/n} "My Lady kept us as we were while the work lasted. Now I have a city full of strangers and a road into Sarkoris to consider. I shall have to look up from the charts occasionally."''',
       c("Continue", "ask")),
    el("ask", '''{n}She sets the cup down and folds her hands on the chart, the way a priestess folds them before a reading.{/n}
"You said I might ask you every morning. I have been saving the first one since the road." {n}She takes a breath.{/n} "What do you do in the mornings, Commander? When you are not being a commander. I want to know what I am asking you away from."''',
       c('"Read dispatches. Curse at them. Burn the worst ones."', "dispatches", flags=(FIRST_QUESTION,)),
       c('[Flirt] "Until now? Nothing worth asking me away from."', "flirt", flags=(FIRST_QUESTION,)),
       c('"Nothing. I don\'t have mornings. I have the next thing."', "nothing", flags=(FIRST_QUESTION,))),
    el("dispatches", '''"Burn them." {n}She seems delighted.{/n} "We had no dispatches. We had observations, and every one was kept, even the wrong ones. I think I should like to burn something, once. Will you save me a very bad one?"''',
       c('"I\'ll save you the Council\'s next letter."', "end")),
    el("flirt", '{n}She looks frankly at your mouth, then hooks her fingers beneath yours on the table.{/n} "Then leave the dispatches unopened for a little while tomorrow. Come to me first. I should like to find out how long I can delay a Commander."',
       c("Continue", "end")),
    el("nothing", '"You could have breakfast. With me." {n}She turns your hand over and runs her thumb across the palm.{/n} "There will still be a war when the bread is gone. I am going to ask you again tomorrow."',
       c("Continue", "end")),
    el("end", '{n}She returns to the chart, keeping your hand until the edge of the table pulls it from hers.{/n} "Go, Commander. I have had my answer. Tomorrow I want more of your morning."',
       c("[Leave her to her chart.]")),
], requires=(), forbids=(FIRST_QUESTION,))


# --- 2. The stone (the King's tavern only) ----------------------------------------------------------------------------

drezen(E + "drezen.stone", "The stone under the cloth", '"You\'ve been looking at the King\'s stone."', [
    el("start", '"Come. I want to look at it again." {n}Eliandra rolls her chart and leads you from the tailor\'s frontage to Thaberdine\'s tavern. The King waves you past his drinkers. Behind the bar, his stone tablet sits beneath a cloth between a keg and a jar of pickled eggs.{/n}\n"I watched you carry it away from behind my Lady\'s veil. I wondered what a crusader wanted with a chief\'s stone. He asked whether his ancestors were buried under it. I said probably."',
       c('"What is the truth?"', "truth"),
       c('"He needed it more than the dead did."', "needed")),
    el("truth", '''"I read it. He lifted the cloth for me, and I read it twice." {n}She looks at the cloth.{/n} "The letters are older than the fall of Sarkoris. The moss is older than that. It says what he says it says, word for word, and it bears his crest. I do not know how, and I will not pretend it is a forgery. It is not."
"But I remember that ground. The chiefs went to their rest on barges, down the river and over our falls, and the stones were set up afterwards by whoever loved them. Most had no names. Sarkoris did not believe a chief belonged to a stone, or a stone to a chief." {n}She almost smiles.{/n} "So there are two histories under that cloth now: the one I remember, and the one your trickery made true. I have decided to keep both. Sarkoris always did like an argument."''',
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
    el("start", '''"It is. Come up to the wall with me. Bring a cloak; the wind comes straight off the Wound." {n}She is already on her feet, her own cloak pinned to the throat, her face bright in a way you have not seen it in Drezen before.{/n} "They are out, Commander. Over the north. Come and see what they have done to the sentries."''',
       c("[Go up to the north wall with her.]", "wall")),
    nar("wall", '''{n}The north wall of Drezen is black and bitter and nearly empty. A sentry stamps his feet in the angle of a tower, his face turned up, his mouth open. Two crusaders further along have stopped mid-round to stare. Eliandra stands at the parapet and looks north.{/n}
{n}You look north too. There is the Wound's red smear on the horizon, as always, and above it a dark, clear sky with a great many stars. And there is something else, a place in the sky your eyes will not stay on. They slide off it to the sentry's upturned face. You recognize the pull from the first-mile road. This time you stop trying to force your eyes back and stand beside her.{/n}''',
        c("Continue", "cost", requires=(LIGHTS_SEEN,)),
        c("Continue", "cost_plain", forbids=(LIGHTS_SEEN,))),
    nar("cost", '''{n}You remember the chiefs' ground: the colours over the dry fall, the cairn, the sword across your knees. You remember them exactly, and you will go on remembering them exactly, and that is all you will have. The veil that hid a whole shrine for a century lies over one pair of eyes now, and it is very good work.{/n}''',
        c("Continue", "her")),
    nar("cost_plain", '''{n}Your eyes find every star. Between them is a space they will not stay on, no matter how carefully you try. The veil that hid a whole shrine now turns one person's gaze aside.{/n}''',
        c("Continue", "her")),
    el("her", '''{n}Eliandra is watching your face.{/n} "They were pale on the road. Tonight the whole sky is moving." {n}Her hand finds yours on the parapet.{/n} "I wanted to be here when you looked. Shall I tell you exactly what I see, or make it sound kinder?"''',
       c('"Exact."', "exact"),
       c('"Kind."', "kind"),
       c("[Watch her face instead of the sky.]", "face")),
    el("exact", '''"Exact." {n}She turns to the north, and her voice changes: it is the voice she uses for the evening reading, slow and plain.{/n} "Three curtains, north-north-east, the lowest touching the Wound's glare. Green at the hem, very bright. Folds of rose above, moving westward, perhaps a hand's breadth in the time it takes to breathe twice. At the height of the middle curtain a white band, where it is brightest, pulsing, the way a heart does when one has been running." {n}She stops.{/n} "The sentry has started to cry. He is trying to hide it. There. That is exact."''',
       c("Continue", "end")),
    el("kind", '"Kind, then. They are bright enough to make the sentries forget the cold." {n}She looks north, her fingers tightening around yours.{/n} "I have watched them from the shrine all my life. I like having you beside me under them. I will describe the part your eyes cannot keep."',
       c("Continue", "end")),
    nar("face", '{n}You watch her instead. When she notices, she leans against you and turns her cheek towards your mouth. Your kiss lands just below her ear; she draws a sharp breath, then catches your wandering hand against the parapet.{/n} "The sentry is still here." {n}She does not move away. She holds your fingers while he makes his round.{/n}',
        c("Continue", "end")),
    el("end", '"Tomorrow, if the wind holds. I shall bring another cloak." {n}She stays against your shoulder, one hand over yours. When the sentry passes again she points out the lowest green fold for him, then resumes the description quietly for you.{/n}',
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
    el("regret", '"No. I regret that the boy waited an hour in pain, and that the next will wait longer." {n}She flexes her tired fingers.{/n} "I will need another priestess at that table tomorrow. I should have asked sooner. I would still make the offering."',
       c("Continue", "end")),
    el("brave", '''"Ordinary." {n}She does not like the word, and does not argue with it either.{/n} "The boy will walk. That is what matters, and I will not pretend otherwise because it took me an hour." {n}Her jaw sets, the high priestess for a breath.{/n} "But I will be quicker next time. My Lady took back her gift; she did not take back a century of knowing where the blood runs and how a wound wants to close. That is mine. I learned it at a thousand pallets." {n}A breath, not quite steady.{/n} "I resent the hour, Commander. I will go on resenting it. I would pay it again."''',
       c("Continue", "end")),
    nar("hands", '''{n}Her hands are cold and not quite steady. You turn them palm up. The blood under the nails is the boy's, and fresh ink stains the second finger of the right hand, and there is no shimmer on either palm, none at all, only the lines anyone has.{/n}
{n}Eliandra lets you look. Then she closes her fingers round yours. "They will learn," she says. "They learned to hold a lens. They can learn to be tired."{/n}''',
        c("Continue", "end")),
    el("end", '''"Go and see to your war. I am going to sit here with a cup of water and watch the street go by, and I am going to enjoy being useless for an hour." {n}She almost laughs.{/n} "I have never been useless for an hour in my life. I should like to find out whether I am any good at it."''',
       c("[Leave her to her hour.]", flags=(ORDINARY,))),
], requires=(REWARD_RETURNED,), forbids=(ORDINARY,), delay=24)


# --- 5. Katair: his own grave at the Stone Tree (Ranger_main Cue_0016-0023) ------------------------------------------------

drezen(E + "drezen.katair", "A name on a tombstone", '"Katair wants a word with me?"', [
    nar("start", '''{n}Katair is not sitting down. He stands beside her table with his arms folded and his bow across his back, as he stood at the shrine's door, and when Eliandra gets up and goes off on some errand that is plainly invented, he watches her go and waits until she is out of earshot.{/n}''',
        c("Continue", "stone_tree")),
    kt("stone_tree", '''"The others think I went to the Stone Tree to see my wife," {n}says Katair.{/n} "Taeriell thought it for seventy years. He died thinking it." {n}His scarred face does not move.{/n}
"I was married under that tree the spring before the Wound opened. When my Lady hid the shrine we could send no word to our families. None. And I knew Ymris would come looking for me. So I built a grave there, in the first place she would look, and carved my name on the stone, and let her find it."''',
       c('"So she would stop looking."', "stop"),
       c("[Say nothing.]", "stop")),
    kt("stop", '''"So she would grieve, and stop, and go to Mendev, and live." {n}He says it flatly, the way a sergeant reads a casualty list.{/n} "She did. I watched her find it, from behind the veil. I have been going back to that stone for a hundred years because it is the last place I was happy and the first place I did something I could not undo."
"I tell you this because of what was given at our basin, Commander."''',
       c("Continue", "given", requires=(LIGHTS_GIVEN,)),
       c("Continue", "hers", forbids=(LIGHTS_GIVEN,))),
    kt("given", '''"You knelt there and gave away something you cannot get back, and I think you ought to know what that looks like a hundred years later."''',
       c('"What does it look like?"', "looks"),
       c('"Are you warning me off her?"', "warn")),
    kt("hers", '''"She knelt there and gave back the strength she had carried since she was thirteen, and she did it with you watching, and I think you ought to know what a thing like that looks like a hundred years later, since you will be the one living beside it."''',
       c('"What does it look like?"', "looks"),
       c('"Are you warning me off her?"', "warn")),
    kt("looks", '''"It looks like a stone with my name on it, and a woman in Mendev I will never see again, and a mission that ended with a demon walking in through the door." {n}He unfolds his arms.{/n} "It looks like it was worth it. That is the worst of it. It was worth it, and I would do it again, and it is still a grave."''',
       c("Continue", "her")),
    kt("warn", '''"No." {n}Something almost like humour crosses his face and is gone.{/n} "She has not been warned off anything since she was thirteen, and it has done her no good at all. I am not going to start now." {n}He glances the way she went.{/n} "I am telling you what a sacrifice weighs, because she will never tell you what hers weighed. She will say it was nothing. It was not nothing."''',
       c("Continue", "her")),
    kt("her", '"The column still looks to her. I have watched her go from the wounded to your table and back again without sitting down." {n}He unfolds his arms.{/n} "When she says she will walk to Iz, believe her. Help with the horses. Do not make her argue for the road as well."',
       c("Continue", "gave_it", requires=(LIGHTS_GIVEN,)),
       c("Continue", "chose_you", forbids=(LIGHTS_GIVEN,))),
    kt("gave_it", '"You paid for her release. I am grateful. That does not put her people in your debt." {n}He glances towards the road.{/n} "We will need good horses in spring. Remember that when she brings you the map."',
       c('"I\'ll remember."', "end"),
       c('[Offer your hand] "Come and drink with us at the Stone Tree, when the war\'s over."', "tree")),
    kt("chose_you", '''"She gave that up herself, and then she chose you. I did not choose you, and I do not understand why she did, and I will not stand between her and the first thing she has ever taken for her own. Do not make me regret it."''',
       c('"I won\'t."', "end"),
       c('[Offer your hand] "Come and drink with us at the Stone Tree, when the war\'s over."', "tree")),
    kt("tree", '''{n}Katair looks at your hand as if it were a strange animal. Then he takes it, briefly, hard.{/n}
"Perhaps," {n}he says.{/n} "Someone should tell the stone it can stop pretending. It has been lying for me for a hundred years. It has earned a drink."''',
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
    el("going", '''"You will go there. Everyone knows it. The crusade will end at Threshold, one way or another." {n}She lays her hand flat on the chart in front of her.{/n} "Before we lost the shrine, we meant to finish a working: my Lady's power and the memory of Sarkoris's priests, put into one thing, to clear the sky above that fortress and set the northern stars burning over it. Odden says we can still do it, from what is left of our work."''',
       c("Continue", "blind", requires=(LIGHTS_GIVEN,)),
       c("Continue", "sighted", forbids=(LIGHTS_GIVEN,))),
    el("blind", '''{n}She looks at you, and you both know the next thing before she says it.{/n}
"If we do it, the whole crusade will look up at Threshold and see the northern stars burning, and my Lady's lights among them. You will see the stars. Not the lights." {n}Neither of you pretends otherwise.{/n} "I will be there, if I can. Not in the breach. In the camp, with the healers. When they light, find me. I will tell you what they look like. I will tell you exactly."''',
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
    el("truth", '''{n}She listens and corrects the chart in three places, leaving the old marks in the margin.{/n} "There. Your account is better than my guess. Odden shall not hear that his fortune-telling needed corrections."''',
       c("Continue", "reading")),
    el("lie", '''"Obviously." {n}She writes it down with perfect seriousness, underneath it writes "a lie, probably", and underneath that "the Commander's", and underlines it twice.{/n}
"An observation that was wrong is still an observation," {n}she says.{/n} "It tells you where the eye goes astray. In your case, whenever you are asked a simple question."''',
       c("Continue", "reading")),
    el("unknown", '''"Then I shall choose for you." {n}She says it as though it were the most natural thing in the world.{/n} "I have spent a century choosing things for other people. I am going to allow myself this one." {n}She makes a small mark at the edge of the circle.{/n} "There. Late autumn. The first cold night. The night the lights come back."''',
       c("Continue", "reading")),
    el("reading", '''"Here is your sky." {n}Her finger moves along the lower edge of the circle, where the northern stars are crowded thickest.{/n} "Most of your lights sit low, in the north. Not overhead, where a king's would be, or a saint's. Low, near the edge of what can be seen, where they are easy to miss unless one is sitting down and looking on purpose."''',
       c("Continue", "irony", requires=(LIGHTS_GIVEN,)),
       c("Continue", "plain", forbids=(LIGHTS_GIVEN,))),
    el("irony", '''"And the north is where my Lady hangs her lights. You can still count every star there; you will never see the lights among them." {n}She says it gently, without pity.{/n} "So I have drawn it for you instead. It is not the same. It is what I can give you, and I am very good at it." {n}She rolls the chart, ties it, and holds it out.{/n} "Keep it. Correct it, if I have made mistakes. Do not cross anything out."''',
       c("[Take the chart.]", "end")),
    el("plain", '''"It suits you. Things are always hiding at the edge of the sky, near the ground, where people have stopped looking up." {n}She rolls the chart, ties it, and holds it out.{/n} "Keep it. Correct it, if I have made mistakes. Do not cross anything out."''',
       c("[Take the chart.]", "end")),
    el("end", '{n}She gives you the chart, then catches your sleeve as you turn to leave.{/n} "Keep it dry. And come back before the night watch. I want to see you without a table between us."',
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
    el("yes", '{n}She writes your name beside the road to Iz, and beneath it, "first spring". Then she turns the map for you to see.{/n} "I will ask the quartermaster for two mounts. You can explain why one must carry the Commander."',
       c("[Leave her to her map.]")),
    el("war", '''"No. It does." {n}She does not seem hurt.{/n} "Then I will ask again in the spring, when the war has decided. I am allowed to ask every morning. You agreed to it on the ford road, and I have a very good memory." {n}She rolls the map, carefully.{/n} "But I will leave a place on the road beside me, all the same, and I will not let Odden put the mule in it."''',
       c("[Leave her to her map.]", flags=(E + "drezen.road_open",))),
], requires=(CHART,), forbids=(ROAD,), delay=24)


# --- 9. Odden, in a city with wine in it -----------------------------------------------------------------------------------

ODDEN_SPOKE = E + "drezen.odden"


def od(id, text, *choices, **kw):
    return n(id, "Odden", text, *choices, portrait="Odden", **kw)


drezen(E + "drezen.odden", "The dwarf and the cooper", '"Odden looks happier than I\'ve ever seen him."', [
    el("start", '''"He has discovered that in Drezen one may buy wine without hiding it in a boot-chest." {n}Odden has come down from the refugees' rooms with the cooper. Across the street, the old dwarf is explaining something at great length to a cooper who has plainly heard it before and is listening anyway.{/n} "He came to find me this morning to tell me he had something to say to you, and he has been working up to it ever since. I think he has now had enough wine to be brave. Brace yourself."''',
       c("[Let him come.]", "odden")),
    od("odden", '{n}Odden approaches with his beard freshly braided and a full cup held level.{/n} "Commander. A word." {n}He glances at Eliandra.{/n} "She had bandages to change all morning. The wardens have work, and she is still doing their lifting. If you mean to sit with her, make her sit too."',
       c("Continue", "remembered", requires=(E + "remembrance",)),
       c("Continue", "departed", forbids=(E + "remembrance",))),
    od("remembered", '''"She took a cup at my table, on the day of the dead. The whole room saw it. And now she's sitting in Drezen with her feet very nearly up, asking people questions." {n}His eyes are wet.{/n} "I don't know what you did at that basin. She won't say. I don't need to know."''',
       c('"She did most of it herself."', "herself"),
       c('"What did you want to say, Odden?"', "say")),
    od("departed", '''"She walked out of the valley in a travelling cloak, like anybody, and now she's sitting in Drezen with her feet very nearly up, asking people questions." {n}His eyes are wet.{/n} "I don't know what you did at that basin. She won't say. I don't need to know."''',
       c('"She did most of it herself."', "herself"),
       c('"What did you want to say, Odden?"', "say")),
    od("herself", '''"She did. She does everything herself. That's the trouble with her." {n}He glares at you with enormous affection.{/n} "But she didn't do this one alone. So."''',
       c("Continue", "say")),
    od("say", '"If you hurt her, every tavern in Drezen hears that you cheat at cards. From me." {n}He raises a thick finger.{/n} "I have an honest face. You have yours. Decide who they will believe." {n}He drinks to her, drinks to you, then goes back to the cooper with his speech delivered.{/n}',
       c("Continue", "after")),
    el("after", '{n}Eliandra watches Odden return to the cooper, struggling not to laugh.{/n} "He practised that on me twice. The first version had a verse." {n}She takes your hand openly on the table.{/n} "His daughter Ranhild never came back. We do not know what became of her. Let him fuss. I will tell him when he goes too far."',
       c('"For the record, it\'s a fair question. Whether I cheat at cards."', "cards"),
       c("[Raise your cup to Odden across the street.]", "cup")),
    el("cards", '"Do you?" {n}Her eyes narrow with interest.{/n} "No. Save your answer. I shall play against you, and Odden may watch. We will see whether his honest face survives losing."',
       c("[Leave the question unanswered.]", flags=(ODDEN_SPOKE,))),
    nar("cup", '''{n}Odden sees you raise it, and raises his back, and the cooper, not knowing why, raises his too, and then the drinkers at the outdoor tables are drinking to something none of them could name. Eliandra watches all of it with her hand on her heart, as though this, too, were an observation, and one she means to keep.{/n}''',
        c("[Drink.]", flags=(ODDEN_SPOKE,))),
], requires=(FIRST_QUESTION,), forbids=(ODDEN_SPOKE,), delay=24)


# --- 10. The morning questions ----------------------------------------------------------------------------------------------

QUESTIONS = E + "drezen.questions"

drezen(E + "drezen.questions", "Every morning", '"What is it today?"', [
    el("start", '''{n}Eliandra has a list before her. Beside two questions she has written dates: mornings, and the sky of your birth. The next line is still blank.{/n} "Today I want to know what you are afraid of." {n}She sets the pen down.{/n} "The soldiers talk about the next breach. I want your answer, Commander."''',
       c('"Losing. Anything. Anyone."', "losing"),
       c('"Being stuck. Things that don\'t change."', "stuck"),
       c('[Lie] "Nothing."', "nothing")),
    el("losing", '''"Losing." {n}She writes it down.{/n} "I thought so. You plan like a person who has lost a great deal and does not mean to do it again. Every move three moves ahead, and a door left open behind you in case." {n}She looks up.{/n} "I lost a whole country, Commander, and a hundred years, and a shrine. I am still here. You may find that encouraging, or not."''',
       c("Continue", "her_turn")),
    el("stuck", '''"Things that do not change." {n}She puts the pen down entirely.{/n} "Then you should have been very frightened of me. I kept a shrine exactly as it was for a hundred years. I kept myself exactly as I was." {n}A small, wry smile.{/n} "Regnard was afraid of the same thing. He told me so, and I told him his talent was needed. I will not tell you that. Your talent is needed everywhere; that is the trouble with it."''',
       c("Continue", "her_turn")),
    el("nothing", '''"Nothing." {n}She writes it down, and beside it, carefully, "a lie", and beside that, "a kind one, probably, for my sake".{/n} "An observation that was wrong is still an observation, Commander. I will ask again in a month. The answer will be more interesting then."''',
       c("Continue", "her_turn")),
    el("her_turn", '''"Now ask me one." {n}She folds her hands.{/n} "You have answered mine. I shall answer yours."''',
       c('"What are you afraid of?"', "afraid"),
       c('"What did you want, at thirteen, before the vow?"', "thirteen", flags=(E + "drezen.sea",)),
       c('"Do you miss any of it? The strength, the vow, the shrine?"', "miss")),
    el("afraid", '"Of reaching for you in bed and finding an empty pillow. Of a messenger at the door with your cloak and no one inside it." {n}She meets your eyes.{/n} "I have learned how you breathe when you sleep. I want more time to learn the rest. Your next breach may give me none."',
       c("Continue", "end")),
    el("thirteen", '''"To see the sea." {n}She laughs, surprised at herself.{/n} "I had never seen it. Nobody in my clan had. A trader told us it was a lake with no other side, and I did not believe him, and I meant to go and see for myself when I was grown. Then I found my gift, and there was the vow, and there was always something more important than the sea."''',
       c("Continue", "end")),
    el("miss", '''"The shrine, every evening at the hour of the reading." {n}She considers it honestly, the way she considers everything.{/n}''',
       c("Continue", "miss_slow", requires=(REWARD_RETURNED,)),
       c("Continue", "miss_strong", forbids=(REWARD_RETURNED,))),
    el("miss_slow", '''"The strength, every time someone bleeds and I am slow. The vow..." {n}A pause.{/n} "The certainty. For a century I never once had to choose what I was for; my Lady had chosen, and I had agreed, and a hundred people are alive because I never wavered. I would make that vow again. But now I choose every morning, and it frightens me, and I have told no one that but you."''',
       c("Continue", "end")),
    el("miss_strong", '''"Not the strength. My Lady left me that, and I use it every day, and every day it is heavier, because now I choose each time whom to spend it on. The vow chose for me. The vow..." {n}A pause.{/n} "The certainty. For a century I never once had to choose what I was for; my Lady had chosen, and I had agreed, and a hundred people are alive because I never wavered. I would make that vow again. But now I choose every morning, and it frightens me, and I have told no one that but you."''',
       c("Continue", "end")),
    el("end", '{n}She puts the pen away and catches your hand before you rise.{/n} "Tomorrow you will have more orders. Come before you read them. I want a little of the morning."',
       c("[Promise to come before the morning orders.]", flags=(QUESTIONS,))),
], requires=(CHART,), forbids=(QUESTIONS,), delay=24)


# --- 11. Ramien's dream (read only if the Desnan saw his dream come true at Pulura's Fall) --------------------------------

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
    el("flirt", '{n}She lowers her cup, looking pleased with herself.{/n} "Good taste, certainly. A very imprecise compliment. Try again tomorrow, Commander. I shall expect you."',
       c("[Leave her to be insufferable.]", flags=(RAMIEN_TALKED,))),
], requires=(RAMIEN_DREAM,), forbids=(RAMIEN_TALKED,), delay=24)


def integrate(payload):
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = copy.deepcopy(value)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'eliandra.trickster.ch5.self_offering',
    'eliandra.trickster.ch5.self_offering_mark',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]


# Round 2: authored continuity at both physical hosts. Old indices and effects remain;
# only append fallback nodes/answers. Release, proposal and sex are separate decisions.
for _scene in SCENES:
    # These twins also use the first-visit cast; retain historical Angel acquaintance.
    _scene["Forbids"] = list(dict.fromkeys([*_scene["Forbids"], "eliandra.met_ch3"]))
    _by = {nd["Id"]: nd for nd in _scene["Nodes"]}
    if _scene["Id"] in (E + "visit.star_heart", E + "visit.star_heart_mark"):
        for _id in ("look", "look_up"):
            _answers = _by[_id]["Choices"]
            _answers[1]["Requires"].append(E + "terms_known")
            _answers.append(c("Continue", "want_observation", forbids=(E + "dead_named", E + "terms_known")))
        _scene["Nodes"].append(el("want_observation",
            '"You stayed for the reading. Tonight I want you to stay for me." {n}She rests her hand on your chest and comes close enough for her breath to touch your mouth.{/n} "Kiss me, Commander."',
            c("[Kiss her.]", "robes"), c('[Flirt] "The stars can wait."', "robes")))
        _slot = _scene["Id"] + ".explicit.1"
        _by["charts"]["Choices"][0]["Next"] = _slot
        # Explicit brief: first chosen night at the bare chart table; no interruption.
        _scene["Nodes"].append(nar(_slot,
            '{n}Eliandra holds you there with both legs locked behind you, her breath hard against your mouth. The last chart slips from the table.{/n}',
            c("Continue", "morning")))
    if _scene["Id"] in (E + "drezen.city", E + "drezen.city_mark"):
        _by["ask"]["Text"] = _by["ask"]["Text"].replace("since the road", "until we could sit together")
    if _scene["Id"] in (E + "drezen.road", E + "drezen.road_mark"):
        _by["why"]["Choices"][1]["Forbids"].append(LETTER_ANSWERED)
        _written = copy.deepcopy(_by["why"]["Choices"][1])
        _written.update(Next="war_letter", Requires=[LETTER_ANSWERED], Forbids=[])
        _by["why"]["Choices"].append(_written)
        _scene["Nodes"].append(el("war_letter",
            '"Then I will ask again when it is done. You wrote that I could ask every morning." {n}She folds the map.{/n} "Keep that letter in mind when you think the spring too far away to discuss."',
            c("[Leave the spring open.]", flags=(E + "drezen.road_open",))))


# Round 3: the one road letter is followed by a physical caravan arrival.
# Authored staging at the established capital frontage, independent of the
# ordinary host that remains absent until the player greets her here.
from storylines.eliandra_trickster import AWAY, RETURNED
ARRIVAL = "eliandra.presence.arrival"
PRESENCES[ARRIVAL] = dict(
    Unit=UNIT, Area=DREZEN, Mode="spawn-copy",
    At=dict(NearUnit=TAILOR, Side="front", Distance=8.0),
    Requires=["trickster.ever", MET, COMMITTED, LETTER_ANSWERED, AWAY],
    Forbids=[CLOSED, DEAD, "eliandra.attacked", RETURNED],
    MinChapter=5, MaxChapter=5, DelayHours=48, AnswerLists=[], Dialog="hub",
    Greeting="{n}A dusty pack rests beside the tailor's frontage. Eliandra waits beside it, still wearing her travelling cloak.{/n}")
_arrival = next(s for s in SCENES_MAIN if s["Id"] == E + "ch5.return_from_fords")
_arrival.pop("Remote", None)
_arrival.pop("Kind", None)
_arrival.update(InteractionHub=ARRIVAL, Areas=[DREZEN], ContactUnit=UNIT, Entry='"Eliandra. You came back."')
_arrival_nodes = {node["Id"]: node for node in _arrival["Nodes"]}
_arrival_nodes["start"]["Text"] = '{n}Two days after your reply, you find Eliandra beside the tailor\'s frontage, dust on her cloak and her pack at her feet.{/n} "Odden has the column. I have come for your answer in person."'
_arrival_nodes["start"]["Choices"][0]["Text"] = "[Tell her what you meant.]"
_arrival_nodes["start"]["Choices"][1]["Text"] = "[Welcome her.]"
_arrival_nodes["truth"]["Text"] = '"You meant to take my release and recover your offering afterwards. Then you called it a cramp. I have read your answer twice. I believe this one. I have not forgiven the other."'
_arrival_nodes["truth"]["Choices"][0]["Text"] = "[Listen.]"
_arrival_nodes["answer"]["Text"] = '"I still mean to ask you. Odden will keep the column at the fords while I am here. We have wounded waiting, Commander. I cannot stay long."'
_arrival_nodes["answer"]["Choices"][0]["Text"] = "[Take her hand.]"
_arrival_nodes["return"]["Text"] = '{n}She takes your hand and leaves it there.{/n} "Either, then. I have brought no carts today. They are waiting for me, and I mean to go back."'
