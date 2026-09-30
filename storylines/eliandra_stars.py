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
    CHARTS, CLOSED, COMMITTED, DEAD, DECLINED, DREZEN, E, FLIRTED, HEALING_SEEN, HEART_SEEN, LEAVE, LETTER_ANSWERED,
    LIED_ABOUT_HAND, LIGHTS_GIVEN, LIGHTS_SEEN, MET, NO_LEAVE, PATH_FIT, REFUSED_FOR_HER, REL, REWARD_RETURNED, TABLET,
    TRIED_TO_CHEAT, UNIT)
from storylines.eliandra_trickster import FLIRTED, LOVERS_SPOKEN, OBSERVED, REMEMBRANCE, SARKORIS_TOLD
from storylines.eliandra_trickster import SCENES as SCENES_MAIN

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
              Requires=["trickster.ever", MET], Forbids=[CLOSED, DEAD, HUB_FAILED, KING_GONE], MinChapter=5,
              MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # Fallback, when the King is gone or cannot be found: her own Drezen mark from the Angel path.
    HUB_ALT: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(Locator=MARK, Offset=[0.0, 0.0]),
                  Requires=["trickster.ever", MET], Forbids=[CLOSED, DEAD], MinChapter=5, MaxChapter=5,
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


def drezen(id, title, entry, nodes, requires, forbids=(), delay=0, places=PLACES, heart=True, **fields):
    """A beat on her presence (the King's tavern, or her Drezen mark): the same scene on each, each forbidding the other."""
    ids = [id + suffix for _, suffix, _ in places]
    for hub, suffix, extra in places:
        sid = id + suffix
        PATH_FIT[sid] = "T"
        SCENES.append(scene(sid, title, "Eliandra", 5, entry, copy.deepcopy(nodes),
                            requires=("trickster.ever", *((HEART_SEEN,) if heart else (MET,)), *requires),
                            forbids=(CLOSED, DEAD, *[o for o in ids if o != sid], *forbids), delay=delay, last=5,
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
    """Twins of a shrine scene on her presence (tavern and mark): same nodes, each twin forbidding the others."""
    original = next(s for s in SCENES_MAIN if s["Id"] == scene_id)
    ids = [scene_id] + [scene_id + "_drezen" + suffix for _, suffix, _ in PLACES]
    for hub, suffix, extra in PLACES:
        sid = scene_id + "_drezen" + suffix
        PATH_FIT[sid] = "T"
        twin = copy.deepcopy(original)
        twin.pop("AnswerLists", None)
        twin.pop("NativeReturnCue", None)
        twin.update(Id=sid, Entry=entry, Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=hub,
                    Forbids=list(dict.fromkeys(original["Forbids"] + [o for o in ids if o != sid])),
                    RequiresAnyGroups=[list(g) for g in original.get("RequiresAnyGroups") or []]
                    + [list(g) for g in extra.get("RequiresAnyGroups", [])])
        SCENES.append(twin)
    original["Forbids"] = list(dict.fromkeys(original["Forbids"] + ids[1:]))


also_in_drezen(E + "ch5.terms", '"What does your Lady take, in return for what she gives?"')
also_in_drezen(E + "ch5.last_rite", '"Will you hold one last rite at the star-heart? For yourself, this time."')


def drezen_pre(id, title, entry, nodes, requires, forbids=(), delay=0, **fields):
    """A device or commit beat on her presence, before the star-heart."""
    drezen(id, title, entry, nodes, requires, forbids=forbids, delay=delay, heart=False, **fields)


drezen_pre(E + "ch5.self_offering", "Her own offering", '"You sent for me?"', [
    el("start", '''"I did. Come up to the north wall tonight." {n}Eliandra has the stargazers' crates stacked round her, roped and labelled in her small exact hand, and she does not look at any of them.{/n} "I have had the basin carried up there. My Lady's rite is made under the open stars, and the wall is the nearest open sky in this city that nobody will walk across."''',
       c("[Go up to the north wall at nightfall.]", "heart")),
    nar("heart", '''{n}The north wall of Drezen is black and bitter and nearly empty. The great bronze basin from the star-heart stands in the angle of a tower, brimming, with the true sky lying in it, and the Wound's red glare low on the horizon beyond.{/n}
{n}She kneels at it without a word. From the look of her knees, she has been kneeling at it, one way or another, for much of the last two days.{/n}''',
        c("Continue", "refused", requires=(REFUSED_FOR_HER,)),
        c("Continue", "cheated", requires=(TRIED_TO_CHEAT,), forbids=(REFUSED_FOR_HER,)),
        c("Continue", "walked", forbids=(REFUSED_FOR_HER, TRIED_TO_CHEAT))),
    el("refused", '''"You refused it for me," she says, without turning round. "You meant it kindly, and it was not yours to refuse. I have thought about that for two days. It is exactly what I did to Vestari and Cristry for a hundred years, and I did not see it until someone did it to me."''',
       c("Continue", "mine")),
    el("cheated", '''"You tried to cheat her," she says, without turning. "In the heart of my shrine, with your hand behind your back." {n}She is quiet.{/n} "I do not know why, and I am not going to guess on your behalf. That is between you and her, and between you and me, and neither of those is finished."
"This is not for you. It is my vow, and I will not have my release bought with a lie. So I will pay for it myself, honestly, and you will stand at the stair and watch it done properly."''',
       c("[Stand at the stair.]", "kneel")),
    el("walked", '''"You walked away from the basin," she says, without turning. "At first I thought your nerve had failed. Then I thought that you had understood what you were about to give, and could not give it lightly. I have decided that I prefer the second."''',
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
"She let me go," she says. "Just like that. For the giving, and a little light." {n}She looks at her empty hand.{/n} "Katair will say I have made a terrible bargain. He will be right about the bargain. He will be wrong about everything else."''',
       c("[Help her up.]", flags=(LEAVE, REWARD_RETURNED)),
       c("[Sit down on the cold stone beside her instead.]", flags=(LEAVE, REWARD_RETURNED))),
], requires=(NO_LEAVE,), forbids=(LEAVE,), delay=48, TricksterDevice=True, TricksterState="no_leave")


drezen_pre(E + "ch5.evening", "Two people on a wall", '"You look as if you haven\'t slept since the basin."', [
    el("start", '''"I have not." {n}Eliandra is sitting on the stargazers' crates with her cloak pulled round her, watching Drezen's lamps go out one by one.{/n} "Odden says I am too old to sit up all night. Odden has been saying that for eighty years, and he has been sitting up with me for most of them." {n}She moves over on the crate without being asked.{/n} "Sit. I have been wanting to ask you something that is not a rite, and not a vow, and not anything a high priestess ought to ask."''',
       c("[Sit beside her.]", "ask")),
    el("ask", '''"Why did you come to my shrine at all? Not the demons; the demons brought everyone. Why did you stay, and ask about my dead, or my Lady, or whatever it was you asked, when you had a war to be at?"''',
       c('"Because nobody had asked you anything in a hundred years. I wanted to be the first."', "first"),
       c('[Flirt] "Because I wanted to find out what you look like when you forget to be the high priestess."', "forget"),
       c('"I don\'t know. I kept finding reasons to come back."', "reasons")),
    el("first", '''"The first." {n}She turns the word over.{/n} "You were. You still are. It is a strange thing to be to someone, after a century. I am not sure whether it is a gift or a burden, and I have decided not to decide tonight."''',
       c("Continue", "close")),
    el("forget", '''{n}She laughs, very quietly, so as not to wake the street.{/n} "Tired," she says. "I look tired. You are looking at it now." {n}She holds your eyes, and does not move away either.{/n} "It is not very impressive."''',
       c('"It is to me."', "close")),
    el("reasons", '''"So did I." {n}She says it simply, and then seems surprised at herself.{/n} "I kept finding reasons to be where you would come. I told myself it was hospitality. I have been a priestess for a very long time, Commander. I know what I tell myself."''',
       c("Continue", "close")),
    nar("close", '''{n}You sit on the crates until the last lamp on the street goes out. At some point her head comes to rest against your shoulder, and neither of you mentions it, and when the sky begins to grey she straightens, and stands, and looks down at you with an expression you have not seen on her before: not the priestess measuring a portent, but a woman deciding something.{/n}
{n}"Tomorrow," she says. "Walk with me in the morning. I will ask you then."{/n}''',
        c("[Promise to walk with her.]", flags=(E + "drezen.evening",))),
], requires=(LEAVE,), forbids=(COMMITTED, DECLINED, E + "drezen.evening"), delay=6)

drezen_pre(E + "ch5.first_mile", "The first mile", '"Walk with you? Where?"', [
    el("start", '''"Out of the north gate, at first light. A mile along the old road, and back." {n}Eliandra is already in a grey travelling cloak, her hair pinned up under the hood; she looks like any priestess on any road.{/n} "The stargazers will winter here, and in the spring I mean to take them on, into whatever is left of Sarkoris. I want to see the first mile of it before I lead anyone down it."''',
       c("[Walk out of the gate with her at first light.]", "gate")),
    nar("gate", '''{n}The road north out of Drezen is ash and old ruts and frost, and she walks it as if the open road were a floor that might give way under her; she had not left her valley in a hundred years until the carts brought her here. The gate guards watch her go with frank curiosity. She does not notice.{/n}''',
        c("Continue", "lights", requires=(LIGHTS_GIVEN,)),
        c("Continue", "tired", requires=(REWARD_RETURNED,), forbids=(LIGHTS_GIVEN,)),
        c("Continue", "road", forbids=(LIGHTS_GIVEN, REWARD_RETURNED))),
    el("lights", '''{n}She keeps glancing up. The sky is barely grey, and low in the north, over the Wound, there is a smear you cannot quite look at: your eyes slide off it to a cloud, a crow, a cart-rut.{/n}
"They are still out," she says. "The last of them. Green, very pale, going rose at the edges where the sun is coming. They are always brightest just before they go." {n}She glances at you, and away.{/n} "I said I would be tiresome about it."''',
       c("Continue", "tired_too", requires=(REWARD_RETURNED,)),
       c("Continue", "road", forbids=(REWARD_RETURNED,))),
    nar("tired_too", '''{n}She stumbles once on a frozen rut, and catches herself, and does not look at you. Last night she sat up with a stargazer's fever, and it took her until the small hours, and it would not have a week ago. Nobody said anything about it at breakfast. All of them noticed.{/n}''',
        c("Continue", "road")),
    nar("tired", '''{n}She walks slowly. Last night she sat up with a stargazer's fever, and it took her until the small hours, which it would not have a week ago; Odden said nothing about it at breakfast, loudly.{/n}
{n}Low in the north, over the Wound, the last of the night's lights are fading. You can see them, pale green going rose. She looks at them once, and then at you, as if to be sure you still can.{/n}''',
        c("Continue", "hand", requires=(TRIED_TO_CHEAT,)),
        c("Continue", "road", forbids=(TRIED_TO_CHEAT,))),
    el("hand", '''{n}Half a mile out she speaks without turning her head.{/n} "Before I ask you anything, you will answer me one thing, and you will answer it plainly, or I will ask you nothing at all." {n}Her voice is quite even.{/n}
"In the heart of my shrine you knelt across the basin from me with your hand behind your back. What did you mean to do with it?"''',
       c('[Tell her the truth] "Take the leave, then find a loophole later and get the lights back."', "owned"),
       c('[Lie] "Nothing. A cramp. You read too much into it."', "lied", flags=(DECLINED, LIED_ABOUT_HAND))),
    el("owned", '''{n}She walks on for a while.{/n} "Thank you," she says at last. "That is an ugly answer, and it is the true one. I would rather have the ugly true thing than a pretty lie, from you, every morning for the rest of my life." {n}She does not smile.{/n} "I have not forgiven it. I may. Walk with me to the milestone."''',
       c("Continue", "road")),
    el("lied", '''{n}She stops in the road.{/n}
"My Lady saw your hand," she says. "I saw your hand. And you stand in the open road with her lights still in the sky and tell me it was a cramp." {n}She looks at you with no anger at all, which is worse.{/n} "I was going to ask you something. I will not, today. Go back to your war, Commander. We leave for the fords in a few days. If I ever know what to do with you, I will write."''',
       c("[Let her walk back alone.]")),
    el("road", '''{n}The first mile is not a long way. At a milestone half-buried in ash Eliandra stops, and looks north along the road, and then back at the walls of Drezen, and then at you.{/n}
"I have never asked anyone for anything for myself," she says. "I have asked for help for my people, often; that is different. For myself, I asked my Lady for nothing in a hundred years." {n}She takes a breath.{/n} "So I am out of practice. Forgive me if I do it badly."''',
       c("Continue", "ask")),
    el("ask", '''"Drezen," she says, "or the road?" {n}She holds your eyes.{/n} "When your war is done. Will you have me in Drezen, in your city, with walls around us? Or will you walk the road with me into whatever is left of Sarkoris, and help me find out what it is?"
"I am asking you, Commander. I want to be told."''',
       c('[Either. Ask me every morning.] "Either. Both. Ask me every morning, and I\'ll give you a different answer every day."', "yes",
         flags=(COMMITTED,)),
       c('[Tell her to leave the stargazers] "Drezen. Just you. Let Odden take them on."', "no", flags=(DECLINED,)),
       c('[Wish her well] "The road is yours, Eliandra. Go well."', "farewell", flags=(CLOSED,))),
    el("yes", '''{n}She laughs: short, startled and entirely unguarded, not a sound the high priestess of Pulura has made in public in a century. A carter on the road turns round to look.{/n}
"Every morning," she says. "You will regret that. I have a hundred years of questions saved up." {n}She reaches out and takes your hand, deliberately, the way she would set a lens to her eye. Her fingers are cold from the road. She does not let go.{/n}
"The heart of the shrine is still open," she says, more quietly. "I left it for last. Ride back with me to the dry fall, Commander, and help me close it."''',
       c("[Walk back to the gate with her.]")),
    el("no", '''{n}She takes it like a blow she saw coming.{/n}
"You ask me to abandon the only people I have," she says. "The ones who are left. Odden, who has no one. The girl with the sling, who does not know how to be anywhere but a cave." {n}She is not angry. That would be easier.{/n} "I cannot. I will not. If that is the only way you will have me, then you will not have me, and I will have asked for nothing after all."
"Go back to your war, Commander. We leave for the fords in a few days. I will write, when I know where we are."''',
       c("[Let her walk back alone.]")),
    el("farewell", '''{n}Something moves across her face and is put away, neatly, the way she rolls a chart.{/n}
"Thank you," she says. "For the rite. For everything you gave that you did not have to." {n}She lays her hand on her heart and bows: the full bow of a high priestess to an honoured guest.{/n} "Farewell, Commander. Pulura's children will remember you."''',
       c("[Watch her walk back to the gate.]")),
], requires=(LEAVE,), forbids=(COMMITTED, DECLINED), delay=24,
    RequiresAnyGroups=[[LOVERS_SPOKEN, OBSERVED, FLIRTED, E + "eyes_kissed", E + "vow_told", REMEMBRANCE, SARKORIS_TOLD, E + "drezen.evening"]])


drezen_pre(E + "visit.star_heart", "The shrine's last night", '"Is the heart still open?"', [
    nar("start", '''{n}Pulura's Fall, after dark.{/n}''',
        c("Continue", "walk_back", forbids=(LETTER_ANSWERED,)),
        c("Continue", "ride_back", requires=(LETTER_ANSWERED,))),
    nar("walk_back", '''{n}It is a long day's ride from Drezen to the dry fall, and she does not speak much on the way. The hidden door still opens for her. The shrine is very quiet with everyone gone; your boots echo in corridors that heard nothing but soft slippers for a hundred years. She walks ahead of you with a lamp, touching the walls as she passes, the way one touches the shoulders of friends at a funeral.{/n}''',
        c("Continue", "heart")),
    nar("ride_back", '''{n}She walked back from the fords alone, two days on the old road, and asked you by a note left at the gate to meet her at the dry fall. She is waiting at the foot of it with a lamp and her hood down. At the hidden door she stops and does not seem to know what to do with her other hand. Then she gives it to you, and leads you in.{/n}''',
        c("Continue", "heart")),
    nar("heart", '''{n}The star-heart is bare to the rock. The basin went with the carts; the long table did not, being too heavy to move, and her last charts lie on it half rolled, weighted with river stones. Overhead the sky burns, black and enormous, as it has burned for a century and will burn when there is nobody under it at all.{/n}
{n}Eliandra sets the lamp down and blows it out. There is enough light without it.{/n}''',
        c("Continue", "her")),
    el("her", '''"I used to take the evening's reading here," she says. "Every evening, for a hundred years. I knew every star over this room. I never once looked at a living soul the way I looked at them." {n}She turns to face you.{/n}''',
       c("Continue", "look", requires=(LIGHTS_GIVEN,)),
       c("Continue", "look_up", forbids=(LIGHTS_GIVEN,))),
    el("look", '''"There are lights over the north tonight. You cannot see them. I can." {n}She steps closer, close enough that you can smell the road on her cloak, and cedar, and ink.{/n} "Look at me, then," she says. "I will look up for both of us."''',
       c("Continue", "want", requires=(E + "dead_named",)),
       c("Continue", "want_rite", forbids=(E + "dead_named",))),
    el("look_up", '''"You still have your eyes, and I have nothing of my Lady's left but her leave." {n}She steps closer, close enough that you can smell the road on her cloak, and cedar, and ink.{/n} "Look up, then, while I look at you. I have looked at the sky long enough."''',
       c("Continue", "want", requires=(E + "dead_named",)),
       c("Continue", "want_rite", forbids=(E + "dead_named",))),
    el("want_rite", '''"I have wanted things before," she says. "I gave all of it to her before I knew what it was, and I did not miss it, because I did not know what I was missing." {n}Her hand comes up, slowly, and rests flat on your chest, the way she rests it on her own heart when she bows.{/n}
"I know now. I want you, Commander. I have wanted you since you came to me with a question nobody had asked me in a hundred years: what my Lady takes, and what I might ask her for. I have no idea at all what to do about it. I am told that is usual."''',
       c("[Kiss her.]", "robes"),
       c('[Flirt] "I\'ll show you. Slowly. We have all night."', "robes"),
       c('"I told you I wasn\'t watching the stars."', "robes", requires=(FLIRTED,))),
    el("want", '''"I have wanted things before," she says. "I gave all of it to her before I knew what it was, and I did not miss it, because I did not know what I was missing." {n}Her hand comes up, slowly, and rests flat on your chest, the way she rests it on her own heart when she bows.{/n}
"I know now. I want you, Commander. I have wanted you since the day you walked into my broken shrine with blood on your sleeves and asked me who I had lost. I have no idea at all what to do about it. I am told that is usual."''',
       c("[Kiss her.]", "robes"),
       c('[Flirt] "I\'ll show you. Slowly. We have all night."', "robes"),
       c('"I told you I wasn\'t watching the stars."', "robes", requires=(FLIRTED,))),
    nar("robes", '''{n}She kisses like someone learning a language by immersion: clumsy for a breath, then with a sudden fierce aptitude that takes you both by surprise. Her hands are in your hair. Yours are at her waist, on the grey cloak, on the pin at her throat that will not come undone.{/n}
{n}She takes your hands away from it. For a heartbeat you think she has changed her mind. Then she unpins it herself and lets the cloak fall, and beneath it the white robes of her office, and she loosens those too, tie by tie, with the same steady fingers that never once shook at the lens, looking at you the whole while.{/n}''',
        c("Continue", "wrist")),
    nar("wrist", '''{n}Her skin is paler where the robes have always covered it, and there is a scar on her shoulder you did not know about, old and white, from some fight a century gone. You put your mouth to it. She makes a sound nobody in this shrine has ever heard from her.{/n}
{n}You find her wrist, and the pulse beneath it, quick and hard: a heart that kept its steady time through a hundred years of evenings and is keeping no time at all now. You press your lips there and feel it race. Eliandra says your name, and then says it again, as if she were checking an observation, and pulls you close.{/n}''',
        c("Continue", "learn")),
    nar("learn", '''{n}Then she stops being careful. Your shirt goes, and she spreads her hands flat on your ribs and moves them slowly, north to south, the way she once moved a lens across a sky she meant to know by heart, and you feel her breath catch each time she finds something new: a scar, a pulse, the place where your breath goes ragged.{/n}
{n}"I have watched things move for a hundred years," she says against your throat. "I want to feel something move." Her teeth close, lightly, on your shoulder. Her thigh is between yours. The white robes are round her hips now and she does not trouble to push them further; her hands are busy, and her mouth, and there is nothing of the high priestess left in either.{/n}''',
        c("Continue", "charts")),
    nar("charts", '''{n}The table is behind her. The charts are on the table. Neither fact turns out to matter. The river stones go over with a clatter, and the half-rolled charts slide off the edge in a slow white landslide, a hundred years of the northern sky spilling across the floor of the star-heart, and Eliandra, flat on her back on the bare wood with her hair loose over the Maiden's own constellations, laughs aloud and draws you down onto her.{/n}
{n}Overhead, the stars go on burning. For once, nobody in this room is looking at them.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}You wake on the floor of the star-heart under her cloak, with a star chart stuck to your back and the sky overhead gone pale with morning. Eliandra is already up and dressed, kneeling among the fallen charts, rolling them one by one and tying them with a concentration that suggests she has decided not to think about anything else just yet.{/n}
{n}Boots in the corridor. A man stops in the doorway: a military bearing, a face covered in old scars, a bow across his back. He looks at the empty shrine. He looks at the charts. He looks at you, and at her, and at the cloak, and at the obvious.{/n}''',
        c("Continue", "katair")),
    kt("katair", '''"I was beyond the walls," says Katair. "Days. I came back to a sacked shrine and an empty valley, and found the carts' tracks going to Drezen, and Odden in Drezen, who told me you had come back here and would not tell me why." {n}His voice is perfectly level. His hands are not, quite.{/n} "Regnard. Taeriell. The lovers."
{n}It is not a question. Eliandra nods.{/n}
"I was not here," he says.''',
       c('"She was. She held the rest of them together."', "answer"),
       c("[Say nothing. Let her answer him.]", "answer")),
    el("answer", '''"No," says Eliandra, "you were not, and you will carry that, and I cannot stop you." {n}She stands, with the charts in her arms.{/n}''',
       c("Continue", "answer_given", requires=(LIGHTS_GIVEN,)),
       c("Continue", "answer_self", forbids=(LIGHTS_GIVEN,))),
    el("answer_given", '''"I have let my Lady go, Katair. Or she has let me go. The Commander made an offering in my place, and I have made my choice." {n}She lifts her chin.{/n} "I am not going to be ashamed of it in front of you."''',
       c("Continue", "wrong")),
    el("answer_self", '''"I gave my Lady back her gift, Katair. Myself, at the basin, with nobody's hand but mine. She let me go. And then I made my choice." {n}She lifts her chin.{/n} "I am not the strongest of her servants any more, and I am not going to be ashamed of any of it in front of you."''',
       c("Continue", "wrong")),
    kt("wrong", '''{n}Katair is silent. Then he crosses the room, takes the charts out of her arms, and looks at them.{/n}
"You have rolled these wrong," he says. "Every one. The north is on the outside." {n}He hands them back.{/n} "In a hundred years I never once saw you roll a chart wrong."
{n}Then, to you, with no change of tone:{/n} "If you are careless with her, Commander, I will know. Taeriell used to chart where I went, every time I left the walls. Seventy years of it. He thought I did not know." {n}He stops, as if he has walked into a wall.{/n} "He will not chart anything now."''',
       c('"I\'ll take care of her."', "end"),
       c('"She doesn\'t need taking care of. She needs asking."', "end")),
    nar("end", '''{n}Katair goes out to see to the horses. Eliandra stands in the middle of the star-heart with an armful of wrongly rolled charts, looking at the doorway where he went.{/n}
{n}"He will forgive me," she says. "Not today. He has other things to forgive himself first." She looks down at the charts and, astonishingly, smiles. "I am not going to reroll them."{/n}''',
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
    el("brave", '''"Ordinary." {n}She does not like the word, and does not argue with it either.{/n} "The boy will walk. That is what matters, and I will not pretend otherwise because it took me an hour." {n}Her jaw sets, the high priestess for a breath.{/n} "But I will be quicker next time. My Lady took back her gift; she did not take back a century of knowing where the blood runs and how a wound wants to close. That is mine. I learned it at a thousand pallets." {n}A breath, not quite steady.{/n} "I resent the hour, Commander. I will go on resenting it. I would pay it again."''',
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
    kt("her", '''"She gave her whole life to my Lady at thirteen. She never once asked for any of it back, and she held the rest of us together for a century while I went out to stand over my own grave. She deserves one thing that is hers."
{n}He looks at you directly now, and holds it.{/n}''',
       c("Continue", "gave_it", requires=(LIGHTS_GIVEN,)),
       c("Continue", "chose_you", forbids=(LIGHTS_GIVEN,))),
    kt("gave_it", '''"You gave her that. I do not like the way you did it, and I do not understand you, and I am grateful. Do not make me regret it."''',
       c('"I won\'t."', "end"),
       c('[Offer your hand] "Come and drink with us at the Stone Tree, when the war\'s over."', "tree")),
    kt("chose_you", '''"She gave that up herself, and then she chose you. I did not choose you, and I do not understand why she did, and I will not stand between her and the first thing she has ever taken for her own. Do not make me regret it."''',
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
    el("going", '''"You will go there. Everyone knows it. The crusade will end at Threshold, one way or another." {n}She lays her hand flat on the chart in front of her.{/n} "Before we lost the shrine, we meant to finish a working: my Lady's power and the memory of Sarkoris's priests, put into one thing, to clear the sky above that fortress and set the northern stars burning over it. Odden says we can still do it, from what is left of our work."''',
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
    el("irony", '''"And the north is where my Lady hangs her lights. You can still count every star there; you will never see the lights among them." {n}She says it gently, without pity.{/n} "So I have drawn it for you instead. It is not the same. It is what I can give you, and I am very good at it." {n}She rolls the chart, ties it, and holds it out.{/n} "Keep it. Correct it, if I have made mistakes. Do not cross anything out."''',
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
"Then you came."''',
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
    el("her_turn", '''"You may ask me one back. That is only fair. I have been taking an answer from you every morning and giving you none." {n}She folds her hands.{/n} "Go on. I will answer anything."''',
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
    el("miss_slow", '''"The strength, every time someone bleeds and I am slow. The vow..." {n}A pause.{/n} "The certainty. For a century I never once had to choose what I was for; my Lady had chosen, and I had agreed, and a hundred people are alive because I never wavered. I would make that vow again. But now I choose every morning, and it frightens me, and I have told no one that but you."''',
       c("Continue", "end")),
    el("miss_strong", '''"Not the strength. My Lady left me that, and I use it every day, and every day it is heavier, because now I choose each time whom to spend it on. The vow chose for me. The vow..." {n}A pause.{/n} "The certainty. For a century I never once had to choose what I was for; my Lady had chosen, and I had agreed, and a hundred people are alive because I never wavered. I would make that vow again. But now I choose every morning, and it frightens me, and I have told no one that but you."''',
       c("Continue", "end")),
    el("end", '''{n}She adds one more line to the paper and turns it so that you can read it: today's date, and beside it, "asked and answered, both ways".{/n}
"Tomorrow," she says, "I am going to ask you something easy, as a rest. I have not decided what. Something about horses, perhaps. I know nothing whatever about horses."''',
       c("[Promise to be an expert on horses by tomorrow.]", flags=(QUESTIONS,))),
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
