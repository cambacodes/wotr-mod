"""Terendelev, Chapter 5: the watch (the courtship on her presence in Drezen; 11-ROSTER-PLAN-2 §2 build sheet).

She comes back from Iz in a borrowed cloak, in the one shape she has left, and sits where the lower town is busiest: beside
the tiefling trader's stall (or under the tailor's awning when he is not in the capital), watching the street the way she
watched Kenabres. Every beat opens from there.

The beats: her first night (what she owes: the Commander's "nothing", or "your life", which is the player's soft no);
the proof (her own Kenabres words mend her own cut: she is living); the wings (she cannot take her dragon shape); Kenabres
(who lived; her oath to the Wardstone); Deskari (the grudge, and whether the Commander will take her if he is faced again);
the Queen (Galfrey came to Iz to give her rest; or her own body killed Galfrey); the keepsakes (her claw handed back, her
scale refused); the commit (she asks to guard the wound, as she guarded Kenabres); the release of a debt held over her; and
the north turret, her watch-post, where the courtship ends in the one night she leaves her post unwatched.
"""
import copy

from story_format import c, n, reaction, scene
from storylines import foresight
from storylines.terendelev_trickster import (
    AEON, AREELU_TOLD, PARENT_EMBODIED, CLAW, CLAW_HELD, CLOSED, COMMITTED, DREZEN, GROUNDED, HUB, HUB_FAILED, HUB_FB, HUMAN, LATE, P,
    QUEEN_FELL, REL, RETURNED, SCALE_HELD, TAILOR, TIEFLING, WOUND_OPEN)

SCENES = []

FIRST_NIGHT = P + "first_night_seen"
OWED = P + "owed"
DECLINED = P + "declined"
DRESSING = P + "dressing"
GUARDIAN = P + "guardian"
PROOF = P + "watch.proof_seen"
AREELU_NAMED = P + "watch.areelu_named"
WINGS = P + "watch.wings_tried"
KENABRES_TOLD = P + "watch.kenabres_told"
DESKARI_VOW = P + "watch.deskari_vow"
DESKARI_LET_GO = P + "watch.deskari_let_go"
GALFREY_SPOKEN = P + "watch.galfrey_spoken"
GALFREY_BACK = "galfrey.trickster.returned"         # Q6 (COX): the Queen brought back on her own Trickster route (read only)
MANUSCRIPTS = "iz.manuscripts"                       # latched GalfreyGoesToManuscripts: the priestess's sorcery killed her (Cue_0072)
QUEEN_KILLED = "galfrey.killed_by_commander"
LEFT_EARLY_W = "iz.left_early"
DESKARI_KILLED = "iz.deskari_killed"                  # latched DeskariKilledInIz 047d71e3 (terendelev_trickster BINDINGS)
SCALE_KEPT = P + "watch.scale_kept"
CLAW_RETURNED = P + "watch.claw_returned"
NIGHT = P + "night.seen"                 # set on the night watch (either hub twin): the reactions and pages read it
# The unregistered continuation draft's delivered flag (terendelev.continuation.returned_actor_confirmed) has no producer in
# the registered story, so nothing here may name it; the draft forbids this route's return instead (terendelev_continuation).

GREETING = ("{n}Beside the tiefling trader's stall in the lower town, a tall woman with silver hair sits on an upturned crate, a "
            "crusader's cloak around her shoulders that was cut for someone broader. She is watching the street the way a "
            "sentry watches a road. Children keep drifting close to stare at her, and she keeps letting them.{/n}")
PRESENCES = {
    # Front of the tiefling trader; Mielarah stands behind him at 2.5 m, so the two copies are 5 m apart.
    HUB: dict(Unit=HUMAN, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TIEFLING, Side="front", Distance=4.5),
              Requires=["trickster.ever", RETURNED], Forbids=[CLOSED, HUB_FAILED, *PARENT_EMBODIED], MinChapter=5, MaxChapter=5,
              AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # Fallback: right of the tailor (Kaylessa stands left 2.5, Arueshalae's evil copy front 2.0: 5 m and 3.2 m apart).
    HUB_FB: dict(Unit=HUMAN, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TAILOR, Side="right", Distance=2.5),
                 Requires=["trickster.ever", RETURNED, HUB_FAILED], Forbids=[CLOSED, *PARENT_EMBODIED], MinChapter=5,
                 MaxChapter=5, AnswerLists=[], Dialog="hub",
                 Greeting=("{n}Under the tailor's awning, out of the wind, a tall silver-haired woman in a borrowed crusader's "
                           "cloak sits on a bale of cloth and watches the street go by. The tailor has stopped asking her to "
                           "move. He has started bringing her tea.{/n}")),
}


def te(id, text, *choices, **kw):
    return n(id, "Terendelev", text, *choices, portrait="Terendelev", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Terendelev", **kw)


PLACES = ((HUB, "", ()), (HUB_FB, "_awning", (HUB_FAILED,)))


def watch(id, title, entry, nodes, requires, forbids=(), delay=0, **fields):
    """A beat opened from her presence (the tiefling's stall, or the tailor's awning): the same scene on each hub, each
    forbidding the other's completion."""
    for hub, suffix, extra in PLACES:
        twin = id + ("_awning" if not suffix else "")
        SCENES.append(scene(id + suffix, title, "Terendelev", 5, entry, copy.deepcopy(nodes),
                            requires=("trickster.ever", RETURNED, *requires, *extra),
                            forbids=(CLOSED, AEON, twin, *forbids), delay=delay, last=5, Relationship=REL,
                            Chapters=[5], Areas=[DREZEN], ContactUnit=HUMAN, InteractionHub=hub, **copy.deepcopy(fields)))


# --- 1. The first night: what she owes -----------------------------------------------------------------------------------

watch(P + "after.first_night", "The first night", '"You look as though you haven\'t slept."', [
    te("start", '''"Sleep." {n}She turns the word over as though it belonged to somebody else.{/n} "I tried. Your quartermaster found me a room with a real bed in it and a window that shuts. I lay down, and closed my eyes, and it was dark, and I was back in the bones." {n}Her hands tighten on the edge of the cloak.{/n} "So I came down here, where there are lanterns, and people, and two men who have been arguing since the second bell about the price of turnips."''',
       c('"What was it like? Both times."', "deaths"),
       c('"Who won the turnip argument?"', "turnips")),
    te("turnips", '''"Neither. That is the beauty of it." {n}Something that is almost her old laugh, the one from the square.{/n} "They will be back tomorrow, and the turnips will be worse, and they will both be alive to be angry about it. I sat here all night listening to that. I cannot tell you how beautiful it was."''',
       c('"And the rest of it? The dying?"', "deaths")),
    te("deaths", '''"Kenabres I remember in pieces. The sky tearing. Going up because somebody had to be between him and the Wardstone, and nobody else in the city had wings. His scythe. Falling." {n}She says it very evenly, the way soldiers learn to.{/n} "Iz I remember whole. That was worse. I was inside the thing he made of me, and I saw everything it did, and I could not stop one claw."''',
       c("Continue", "iz", forbids=("iz.left_early",)),
       c("Continue", "iz_queen", requires=("iz.left_early",))),
    te("iz_queen", '{n}She turns on the crate and looks at you properly.{/n} "The second death was the Queen\'s. Her knights, her lances, her chaplains singing. I remember every one of their faces. Not yours; you were not there." {n}A pause.{/n} "Yours I saw afterwards, through the smoke over what was left of me, with a knife in your hand. You came close when everyone else kept away." {n}Her hands tighten on the cloak.{/n} "And between the two deaths it was not dark, exactly. It was being used. I would take the dark."',
       c("Continue", "sums")),
    te("iz", '''{n}She turns on the crate and looks at you properly.{/n} "The second death was yours. I remember your face through the fire. It was a kinder death than the first, and I want you to know that I know it." {n}A pause.{/n} "And between them it was not dark, exactly. It was being used. I would take the dark."''',
       c("Continue", "sums")),
    te("sums", '''"I have been sitting here all night doing sums, which is a very silver thing to do. You gave me a body out of your own. The wound it came from is still open in you. I felt it all night, like a door left ajar at the bottom of a stair." {n}She folds her hands.{/n} "Silver dragons pay what they owe, crusader. It is very nearly the whole of our religion. So tell me plainly. What do I owe you?"''',
       c('[Nothing] "Nothing. You healed me first. We\'re square."', "nothing", flags=(FIRST_NIGHT,)),
       c('[Flirt] "Breakfast would be a start."', "breakfast", flags=(FIRST_NIGHT, P + "watch.breakfast")),
       c('[You owe me] "You owe me your life."', "owed", flags=(FIRST_NIGHT, OWED))),
    te("nothing", '''"Square." {n}She laughs, and this time it is the laugh from the square, bright as a bell in cold air; two children by the stall turn round to look.{/n} "I dulled your pain for a night and you made me a body out of your own blood. That is a very generous kind of arithmetic." {n}Her eyes stay on your face.{/n} "I only ever saw your face in pain before. It is a better face without it. I will not insist on the sums, then. I will only remember them."''',
       c("[Leave her to her street.]")),
    te("breakfast", '''"Breakfast." {n}Her brows go up.{/n} "I owe you a life and you want fried bread." {n}And then she is laughing, the laugh from the square, bright as a bell in cold air, so that the turnip men stop to stare.{/n} "There is a woman two streets over who fries it the way they did at the festival, with honey. I smelled it at the fourth bell and nearly wept. Very well, crusader. Breakfast. It is a start, and I shall decide later what it is the start of."''',
       c("[Go and find the woman with the honey.]")),
    te("owed", '''{n}She is quiet. The turnip men go on arguing. A child tugs at the hem of the borrowed cloak, and she puts a hand on his head without looking, and he goes away satisfied.{/n}
"Yes," {n}she says at last.{/n} "I do. I will pay it." {n}She stands and settles the cloak on her shoulders like armour.{/n} "A life is a large sum, and I would not like to pay it badly. Give me a little time to think how."''',
       c("[Leave her to her sums.]")),
], requires=(), forbids=(FIRST_NIGHT,), delay=24)


# --- 2. The proof: what she is made of ------------------------------------------------------------------------------------

watch(P + "watch.proof", "Pry loose the grip", '"You sent a boy to find me."', [
    te("start", '''"I did. I need to know what I am, and I did not want to find out alone." {n}She holds out her hand, palm up.{/n} "Your knife, please."''',
       c("[Give her the knife.]", "cut"),
       c('"What are you going to do with it?"', "why")),
    te("why", '''"Something I have done a thousand times to other people and never once to myself." {n}Her hand stays out.{/n} "I have healed ghouls by mistake, crusader, in the dark, in a hurry. I know what happens to dead flesh under a healer's words. It smokes. It splits. If I smoke, I would rather know it now, from my own mouth, than from a priest's."''',
       c("[Give her the knife.]", "cut")),
    nar("cut", '''{n}She draws the blade across the heel of her own palm, quickly, the way a cook bleeds a fowl. The blood comes up in a line, red. She gives you back the knife hilt-first and holds the hand where you can both see it.{/n}
{n}"Pry loose the grudging grip of pain," says Terendelev, the old words from the festival square. "Cast off the veil of suffering flesh. Let light and life go forth in triumph to repel the skulking shade of death."{/n}''',
        c("Continue", "healed")),
    nar("healed", '''{n}The cut closes. Not all at once: the way a cut closes on a child who has been told to be brave, the edges drawing together and going pink and then pale. There is no smoke. There is no smell of burning meat. There is a thin white line, and then not even that.{/n}''',
        c("Continue", "living")),
    te("living", '''{n}She lets out a breath she seems to have been holding since Iz.{/n} "Living. The dead do not mend under those words; they come apart." {n}She flexes the hand.{/n} "That is one question answered. The other is what I am living as. Your blood, out of a wound the Abyss made. I can feel it in me, crusader, the way an old break feels the rain. I know what weather the Worldwound is having."''',
       c('"Areelu Vorlesh put a crystal in me, in the caves under Kenabres. The wound is her work."', "areelu",
         requires=(AREELU_TOLD,), flags=(AREELU_NAMED,)),
       c('"Does it frighten you?"', "fear")),
    te("areelu", '''{n}Her face does not change. Her hand does: it closes, slowly, into a fist.{/n} "Areelu Vorlesh. The Wound's mother." {n}She says the name as if it were a stone she had found in her bread.{/n} "So I am made from the work of the woman who made the Wound, that made the war, that killed Kenabres and me in it." {n}She opens her hand again, deliberately.{/n} "I will think about that when I am stronger. I will not think about it today."''',
       c("Continue", "fear")),
    te("fear", '''"A little. Less than I expected." {n}She tilts her head, listening to something inside herself.{/n} "It does not feel like his. It feels like yours. That is the strangest thing I have ever said aloud, and I have lived a long time among very strange people." {n}She reaches for you.{/n} "Now. Your turn. Stay where you are, and let me try."''',
       c("[Let her put her hand on the wound.]", "try")),
    nar("try", '''{n}She speaks the words again, low, with her palm flat over the dressing. The pain goes quiet. It goes quiet the way it went on the square: at once, completely, like a dog called to heel.{/n}
{n}The bleeding does not stop. Under her hand the dressing darkens, slowly, as it always does.{/n}''',
        c("Continue", "promise")),
    te("promise", '''{n}She takes her hand away and looks at it.{/n} "I promised you on the square that you would recover. I have now failed to keep that promise twice." {n}Her mouth tightens.{/n} "I do not like that at all. Silver dragons are not supposed to fail at promises. It is very bad for the reputation."''',
       c('"You kept the part that mattered."', "end", flags=(PROOF,)),
       c('"Third time lucky."', "end", flags=(PROOF,)),
       c('"Leave it. It\'s as much yours now as mine."', "end", flags=(PROOF,))),
    te("end", '''{n}She looks at you for the space of a breath, and something in her face eases.{/n} "Perhaps." {n}She tucks the knife back into your belt herself, neatly, as though she were putting away someone else's tools.{/n} "I am going to keep trying. Every morning, if you will let me. It will not work, and I will do it anyway, because that is what I am for."''',
       c("[Leave her with her hand still warm from yours.]")),
], requires=(FIRST_NIGHT,), delay=12)


# --- 3. The wings: what she cannot do ------------------------------------------------------------------------------------

watch(P + "watch.wings", "The shape she cannot take", '"The sentries say you were on the wall at midnight."', [
    te("start", '''"The sentries talk too much. They will make fine sergeants." {n}She does not smile.{/n} "Come up with me tonight. I want to try something, and I would rather have somebody there who will not tell me afterwards that it was a very brave attempt."''',
       c("[Go up with her after dark.]", "wall")),
    nar("wall", '''{n}The outer wall above the lower town, after the last bell. The wind comes off the hills with the smell of snow in it. She walks out to where the parapet is broken and the drop is long, takes off the borrowed cloak, folds it, and hands it to you.{/n}
{n}Then she stands in the wind in her shirtsleeves with her arms a little way from her sides, and breathes in, long and slow, the way a dragon does before it becomes itself.{/n}''',
        c("Continue", "fail")),
    nar("fail", '''{n}Nothing comes of it. For an instant something seems to gather along her shoulders, like the air before lightning, and your ears pop, and then it is gone and she is on her knees on the wall-walk with her hands flat on the stones, gasping as though she had been struck in the stomach.{/n}''',
        c("[Kneel beside her.]", "after"),
        c("[Wait. Let her get up on her own.]", "after")),
    te("after", '''"Nothing." {n}She sits back on her heels. There is blood at one nostril; she wipes it away with the back of her hand and looks at it.{/n} "In Kenabres I kept this shape so that I would not crush your cute little houses. I chose it every morning. I never once thought I might have to live in it." {n}She laughs, not well.{/n} "I am the only silver dragon in the world who has to take the stairs."''',
       c('"Try again."', "again", flags=(WINGS,)),
       c('"You don\'t need wings to be what you are."', "kind", flags=(WINGS,)),
       c('[Flirt] "For what it\'s worth, I like you at this size."', "size", flags=(WINGS,))),
    nar("again", '''{n}She does. She gets to her feet and breathes in and gathers herself, and the air shivers, and she goes down again, harder, and this time she stays down with her forehead on the cold stone until the shaking stops.{/n}''',
        c("Continue", "again_end")),
    te("again_end", '''"No." {n}Muffled, against the stone.{/n} "Not today. Perhaps not this year." {n}She rolls onto her back and looks up at the stars.{/n} "Thank you for making me try twice. Anyone else would have said it was very brave, and I would have had to be polite to them."''',
       c("[Sit down beside her on the wall-walk.]")),
    te("kind", '"That is kind. It will not put me back in the air." {n}She takes the cloak back and holds it between her hands.{/n} "I miss flying. I miss my breath, and sleeping on the mountain. I do not yet know what I can do without them. Stay a while. I do not want to walk down those stairs yet."',
       c("[Stay a while.]")),
    te("size", '''{n}She stares at you. Then she laughs, properly, helplessly, sitting on the wall-walk with blood on her lip and the wind in her hair.{/n} "Oh, you would. You would, and you would say it to my face, on a wall, at midnight, the night I find out I am a cripple." {n}She wipes her eyes.{/n} "I have been flattered by kings, crusader. None of them ever managed to make me laugh while they did it. Help me up."''',
       c("[Help her up.]")),
], requires=(FIRST_NIGHT,), delay=24)


# --- 4. Kenabres: who lived --------------------------------------------------------------------------------------------

watch(P + "watch.kenabres", "Who lived", '"You were asking the sergeants about Kenabres."', [
    te("start", '''"I was. They were very kind, and they knew nothing; they are Mendevians from the southern levies, and to them Kenabres is a name on a map with a black line through it." {n}She looks at her hands.{/n} "I kept that city for longer than your grandmother's grandmother lived, crusader. I do not know who is alive in it. Who lived?"''',
       c('"More than you\'d think. Most of them are here, in Drezen."', "names"),
       c('"Not enough."', "names")),
    te("names", '''"Tell me, then, and I will tell you whether I knew them." {n}She begins to count on her fingers, and it is clear she has been making this list all night.{/n} "The Tirabade girl with the bad leg, who went over the roofs faster than the watch could run on the streets. The half-orc knight on the east wall who sang to her sword when she thought nobody could hear. The young paladin of the Inheritor with a thief's quick hands, who laughed out loud in the cathedral and was forgiven for it." {n}Her fingers stop.{/n} "Hulrun. The old goat."''',
       c('"Ask them yourself. They\'d want to see you."', "ask"),
       c('"Some of them are still fighting. Some of them aren\'t."', "ask")),
    te("ask", '"I knew them. I knew who would argue with the watch, who would feed a stray, who would leave a lamp burning for a late son. I do not know where they are now. That is what I was asking you."',
       c("Continue", "wardstone")),
    te("wardstone", '''"I swore an oath to the Wardstone, the day I came down from the mountains to live among them. That no demon would ever touch it while I lived." {n}Her voice does not waver, which is worse than if it had.{/n} "It fell while I was dying in the sky above it. I kept my oath exactly, you see. I simply did not live long enough for it to matter."''',
       c('"It wasn\'t yours to hold alone."', "home", flags=(KENABRES_TOLD,)),
       c('"You kept it better than anyone could have. The city stood for decades because of you."', "home", flags=(KENABRES_TOLD,)),
       c('"Then swear a better one next time."', "home", flags=(KENABRES_TOLD,))),
    te("home", '{n}She turns toward the south road, beyond Drezen\'s walls.{/n} "Some part of me is already walking back there. It will be a long walk. I have no wings." {n}Then, more lightly, because she is Terendelev and will not be pitied in a public street:{/n} "They will have built something ugly in the square to remember me by. They always do. I should like to go and see it, one day, and stand beside it until somebody notices."',
       c("[Leave her to her list.]")),
], requires=(FIRST_NIGHT,), delay=12)


# --- 5. Deskari: the grudge ---------------------------------------------------------------------------------------------

watch(P + "watch.deskari", "An orderly grudge", '"Something is on your mind."', [
    te("start", '''"The Lord of Locusts." {n}She says it without heat.{/n} "They say in the barracks that you killed him. At Iz, the same day you brought me out of the fire. They say it the way men talk about the weather, and then they go and drink to it." {n}She turns to face you squarely.{/n} "Is it true?"''',
       c('"It\'s true. He fell at Iz."', "true"),
       c('"True enough. He\'ll come back in the Abyss, though. They always do."', "true")),
    te("true", '''"Good." {n}A single word, with the whole weight of a dragon behind it.{/n} "I have heard it said, too, that a demon lord killed twice within the year does not come back from the second time. The Abyss has a graveyard for its lords, and keeps them there." {n}She looks down at her hands.{/n} "I do not know if that is true. I hope it is. I have never hoped a thing so hard."''',
       c('"What did he do to you? In the dark."', "dark"),
       c("Continue", "ask")),
    te("dark", '''"He did not keep me in a place. He kept me in a purpose." {n}She is very still.{/n} "Guard Iz. Kill whoever comes. When it is done, peace. He said it every time I tried to be something other than his, and every time I believed him a little more, because it is the only thing a bone can want." {n}Her jaw sets.{/n} "He made me want peace from him. That is the thing I will not forgive. Not the dying. The wanting."''',
       c("Continue", "ask")),
    te("ask", '''"So I will ask you something, and you may say no." {n}She stands straighter, as though at a parade.{/n} "If you ever face him again within the year, in his Rifts or at the heart of the Wound or anywhere else, take me. I have no wings and no breath, but I have a grudge, and a silver dragon's grudge is a very orderly thing. It keeps accounts."''',
       c('"I\'ll take you. You have my word."', "vow", flags=(DESKARI_VOW,)),
       c('"No. You\'ve given him enough of you already."', "no", flags=(DESKARI_LET_GO,)),
       c('"If it comes to that, you\'ll hear it from me first."', "vow", flags=(DESKARI_VOW,))),
    te("vow", '''{n}She inclines her head, formally, the way the old silvers are said to take an oath from one another on the mountain.{/n} "Then it is agreed, and I will hold you to it, and you will not like how tidily." {n}Something eases in her shoulders.{/n} "Thank you. I do not expect it to come. I only wanted to know that if it did, I would not be sitting on a crate in the lower town, watching it happen from a very long way off."''',
       c("[Leave her with it.]")),
    te("no", '''{n}She is silent for a breath, and you think she will argue. She does not.{/n} "That is the answer a friend gives, and I asked a commander." {n}Then, more quietly:{/n} "It may also be the right one. I will not thank you for it. Not this month. Ask me again in a year, and I may."''',
       c("[Leave her with it.]")),
], requires=(FIRST_NIGHT, DESKARI_KILLED), forbids=(LATE,), delay=24)


# --- 6. The Queen: rest granted, and undone ----------------------------------------------------------------------------

watch(P + "watch.galfrey", "The Queen", '"The chaplain says you\'ve been in the chapel every night."', [
    te("start", '''"The chaplain is right, and should mind his chaplaincy." {n}She rubs her eyes.{/n} "I go to think about the Queen. Somebody should."''',
       c("Continue", "alive", forbids=(QUEEN_FELL, "galfrey.dead", QUEEN_KILLED)),
       c("Continue", "dead", requires=(QUEEN_FELL,), forbids=(GALFREY_BACK, QUEEN_KILLED, MANUSCRIPTS)),
       c("Continue", "dead_late", requires=("galfrey.dead", LEFT_EARLY_W), forbids=(QUEEN_FELL, GALFREY_BACK, MANUSCRIPTS, QUEEN_KILLED)),
       c("Continue", "queen_back", requires=(GALFREY_BACK,), forbids=(MANUSCRIPTS, QUEEN_KILLED)),
       c("Continue", "dead_priestess", requires=("galfrey.dead", MANUSCRIPTS), forbids=(GALFREY_BACK, QUEEN_KILLED)),
       c("Continue", "dead_by_you", requires=(QUEEN_KILLED,), forbids=(GALFREY_BACK,)),
       c("Continue", "dead_unknown", requires=("galfrey.dead",), forbids=(QUEEN_FELL, GALFREY_BACK, MANUSCRIPTS, QUEEN_KILLED, LEFT_EARLY_W)),
       c("Continue", "queen_back_priestess", requires=(GALFREY_BACK, MANUSCRIPTS), forbids=(QUEEN_KILLED,)),
       # Q6 r3 (CAN/COX): the Commander's own kill, then the Queen's return on her route (GalfreyOnTheEdge/Answer_0023).
       c("Continue", "queen_back_by_you", requires=(GALFREY_BACK, QUEEN_KILLED))),
    te("queen_back_by_you", '"She died at Iz by your hand. Not mine, not his. Yours." {n}She says it to the chapel door, not to you.{/n} "And now she is alive, and walks in the chapel yard alone, and you did both of those things. I do not know what that makes you, crusader. I have stopped trying to work it out before breakfast."\n"One day I shall speak to her in private. What she says is hers to say."',
       c("[Leave her to it.]", flags=(GALFREY_SPOKEN,)),
       c("[Go with her as far as the chapel yard.]", flags=(GALFREY_SPOKEN,))),
    te("dead_priestess", '''"She died at Iz. Not by my claws: the priestess's sorcery tore her out of her body while her knights were busy with what was left of me." {n}No tremor at all, which is how you know.{/n} "I have asked every knight who was there. They all say the same, and I believe them, and it does not help. I was the reason she was on that field."
"So I go and I kneel, and I tell the Inheritor about her Queen. Somebody who was there should."''',
       c("[Go with her to the chapel.]", flags=(GALFREY_SPOKEN,)),
       c("[Leave her to it.]", flags=(GALFREY_SPOKEN,))),
    te("dead_by_you", '"You killed her." {n}Terendelev keeps her hands flat on her knees.{/n} "I have heard your soldiers speak of it. I want to hear you. We shall talk before I make you any promise."',
       c("[Leave her to it.]", flags=(GALFREY_SPOKEN,))),
    te("dead_unknown", '''"She is dead, and her knights will not tell me how, and I have stopped asking them." {n}She rubs her eyes again.{/n} "I was her friend for a hundred years. Somebody who was her friend should go and tell the Inheritor about her, every night, until it stops hurting or I stop going."''',
       c("[Go with her to the chapel.]", flags=(GALFREY_SPOKEN,)),
       c("[Leave her to it.]", flags=(GALFREY_SPOKEN,))),
    te("queen_back_priestess", '"She died at Iz. Not by my claws; the priestess\'s sorcery did it, while her knights were busy with my bones." {n}Then, very carefully:{/n} "And now she is alive. You would not let that stand either. I saw her cross the chapel yard last night, and she did not see me, and I stood behind a pillar like a thief."\n"I was the reason she was on that field. That much I will carry. The rest belongs to her." {n}The ghost of a smile.{/n} "One day I shall speak to her in private. What she says is hers to say."',
       c('"She\'ll forgive you. She\'s been dead too; she knows."', flags=(GALFREY_SPOKEN,)),
       c("[Go with her as far as the chapel yard.]", flags=(GALFREY_SPOKEN,))),
    te("queen_back", '"She died at Iz, fighting the thing he made of me. My claws. My sorcery. I felt her go, the way you feel a candle go out in the next room." {n}Then, very carefully, as if the words might break:{/n} "And now she is alive. You would not let that stand either. I saw her cross the chapel yard last night, alone, and she did not see me, and I stood behind a pillar like a thief."\n"It does not unmake it. She lives, and I still killed her. I will carry that, and you will not tell me it was his and not mine." {n}She looks toward the chapel.{/n} "One day I shall speak to her in private. What she says is hers to say."',
       c('"She\'ll forgive you. She\'s been dead too; she knows."', flags=(GALFREY_SPOKEN,)),
       c("[Go with her as far as the chapel yard.]", flags=(GALFREY_SPOKEN,))),
    te("alive", '''"Galfrey came to Iz to put me down. To grant rest to my soul and my body. I heard her say it, before the charge, through the thing he had made of me." {n}Her voice is steady.{/n} "She was right. I would have done the same for her. And then you undid it, in front of her knights, with a knife." {n}A breath.{/n} "I asked to see her. She sent a page to say she would pray on it. I think she is afraid I am a blasphemy. I think she is more afraid that I am not."''',
       c('"She\'ll come round. She\'s been wrong about me before."', "alive_end", flags=(GALFREY_SPOKEN,)),
       c('"Give her time. She buried you once already."', "alive_end", flags=(GALFREY_SPOKEN,))),
    te("alive_end", '''"She has been queen for a hundred years, crusader. She does not come round. She arrives, eventually, with an army." {n}The ghost of a smile.{/n} "I will wait. I am good at it now. When she comes, I will kneel to her, because she deserves it, and because it will make her so very uncomfortable."''',
       c("[Leave her to her chapel.]")),
    te("dead", '''"She died at Iz, fighting the thing he made of me." {n}No tremor at all, which is how you know.{/n} "My claws. My sorcery. I was inside it, and I felt her go, the way you feel a candle go out in the next room. A hundred years she held the Wound back, and it was my body that finished her."''',
       c('"That was Deskari\'s weapon. Not you."', "carry", flags=(GALFREY_SPOKEN,)),
       c('"Yes. It was."', "carry", flags=(GALFREY_SPOKEN,))),
    te("dead_late", '''"She died at Iz, fighting the thing he made of me, while you were elsewhere." {n}No tremor at all, which is how you know.{/n} "Her knights say it was the dragon's sorcery. It was. It was my sorcery, in my bones, and I was inside it and could not stop it. A hundred years she held the Wound back, and it was my body that finished her."''',
       c('"That was Deskari\'s weapon. Not you."', "carry", flags=(GALFREY_SPOKEN,)),
       c('"Yes. It was."', "carry", flags=(GALFREY_SPOKEN,))),
    te("carry", '''{n}She shakes her head, once, very firmly.{/n} "No. Listen to me. I will carry that. You will not carry it for me, and you will not tell me it was his and not mine. It was both, and I am the one who is still alive to hold it." {n}She looks toward the chapel.{/n} "So I go and I kneel, and I tell the Inheritor about her Queen, every night. Somebody who was there should."''',
       c("[Go with her to the chapel.]"),
       c("[Leave her to it.]")),
], requires=(FIRST_NIGHT,), delay=24)


# --- 7. The keepsakes: her claw, and her scale --------------------------------------------------------------------------

watch(P + "watch.keepsakes", "Keepsakes", '"I\'ve been carrying something of yours."', [
    te("start", '''"Of mine? I did not know I had anything left." {n}She holds out her hand, curious as a cat.{/n}''',
       c("[Show her the piece of her claw.]", "claw", requires=(CLAW_HELD,)),
       c("[Show her the scale.]", "scale", requires=(SCALE_HELD,))),
    te("claw", '{n}She goes still, looking at the hooked shard across your palm.{/n} "Where did you find it?" {n}You describe the cave at Leper\'s Smile and the swarm above it.{/n} "Leper\'s Smile. I cannot tell you how it came there. I remember another cave, beside Sarkorian ruins and a spreading tree. That was where I fought the foulness out of myself. This brings it back rather sharply."',
       c('[Give it to her] "Then it\'s yours to do something with."', "claw_given", requires=(CLAW_HELD,), remove_item=CLAW,
         flags=(CLAW_RETURNED,)),
       c('"I\'ll keep it, if you don\'t mind. It\'s the only proof I had that you\'d done this before."', "claw_kept")),
    te("claw_given", '{n}She takes it, carefully, as though it might still be hot.{/n} "I will put it back where it belongs. There is a tree beside my old refuge. I used to look at it to remind myself that something outside the cave was still growing." {n}She closes her hand over it.{/n} "Thank you for returning it. I shall decide where to lay it."',
       c("Continue", "scale", requires=(SCALE_HELD,)),
       c("[Leave her with it.]", forbids=(SCALE_HELD,))),
    te("claw_kept", '''"Proof." {n}She seems surprised, and then oddly pleased.{/n} "Yes. I suppose it was. Keep it, then. Only do not show it to the Storyteller again; he looks at it the way a hungry man looks at bread."''',
       c("Continue", "scale", requires=(SCALE_HELD,)),
       c("[Put it away.]", forbids=(SCALE_HELD,))),
    te("scale", '{n}The scale lies on your palm, silver, untarnished. She touches it with one fingertip and draws her hand back as if it had spoken.{/n} "It is warm. It was never warm, all the years it hung on me. Something of you has got into it." {n}She shakes her head.{/n} "No. That one you keep. It still has the strength to raise someone. Save it for that. I have no use for a keepsake while a crusader may have use for a life."',
       c('"It\'s yours."', "scale_end", flags=(SCALE_KEPT,)),
       c("[Put it back in your pack.]", "scale_end", flags=(SCALE_KEPT,))),
    te("scale_end", '''"It was mine. I gave it to Kenabres, and you are what came out of Kenabres." {n}She closes your fingers over it with her own.{/n} "There. That is settled. Silver dragons like things settled."''',
       c("[Leave her to her street.]")),
], requires=(FIRST_NIGHT,), delay=12, RequiresAnyGroups=[[CLAW_HELD, SCALE_HELD]])


# --- 8. The commit: she asks to guard the wound ------------------------------------------------------------------------

watch(P + "commit", "The watch", '"You said you had something to ask me."', [
    nar("start", '''{n}She does not ask it in the street. She takes you up through the citadel at dusk, past the barracks and the chapel and the Commander's own door, to the north turret above your windows, where the wall is highest and the wind is always blowing.{/n}
{n}She has made it hers. There is a brazier, a borrowed pike leaning against the parapet, a folded blanket and a tin cup. The sentries who used to stand this post salute her on the stair now, and do not seem to know why.{/n}''',
        c("Continue", "flogged", requires=(P + "watch.infirmary_flogged",)),
        c("Continue", "ask", forbids=(P + "watch.infirmary_flogged",))),
    te("flogged", '''"Before I ask you anything: the knight from the infirmary." {n}She does not turn from the parapet.{/n} "I have been to see him every day. His back has healed clean; I made sure of it. He still will not look at me, and now he will not look at you either." {n}A breath.{/n} "I have not forgotten who gave that order. I am asking you anyway. That is what it costs you, crusader: to be asked by someone who remembers."''',
       c("Continue", "ask")),
    te("ask", '"I put my hand on that wound in Kenabres and promised you would recover. It is still open." {n}She rests her hands on the parapet.{/n} "I cannot close it. I will not promise again what I cannot do. But I can keep it clean, and I can stand between you and what comes for it. I want to do that."',
       c("Continue", "oath")),
    te("oath", '''"I would like to guard it." {n}Simply, as a soldier asks for a post.{/n} "The way I guarded Kenabres. Stand the night watch over it, and keep the dressing clean, and be between it and whatever comes. Silver dragons swear oaths, crusader; it is what we do instead of prayers. Let me swear one to this."''',
       c("Continue", "debt", requires=(OWED,)),
       c("Continue", "choose", forbids=(OWED,))),
    te("debt", '''{n}She turns to look at you.{/n} "You told me I owe you my life. I have thought about it every night since. And I find I will not stand this watch as a debtor, crusader. A debtor's watch ends when the debt is paid, and I do not want this one to end." {n}Her voice is quite steady.{/n} "So I am asking you, not paying you. Do you understand the difference?"''',
       c('[Hold her to the debt] "You owe me. Pay it however you like."', "declined", flags=(DECLINED,)),
       c('[Ask if she wants to go home] "Is this what you want? Or do you want to go home to Kenabres?"', "kenabres")),
    te("choose", '"I have asked." {n}She lifts her chin.{/n} "A post for myself, this time. Not for a Wardstone or a city. You may find that I take it rather personally."',
       c('[Let her keep watch] "Keep it, then. For as long as you like."', "yes"),
       c('[Ask if she wants to go home] "Is this what you want? Or do you want to go home to Kenabres?"', "kenabres")),
    te("kenabres", '{n}She looks south, over the dark.{/n} "Kenabres is still my home. They will need stubborn people while they rebuild, and I shall help them. But I have decided to stay here with you. I want this watch." {n}She turns back.{/n} "If you do not want me here, say so. I can bear an honest answer."',
       c('[Let her go] "Then go home. Kenabres needs its dragon more than I need a guard."', "go", flags=(CLOSED, GUARDIAN)),
       c('[Ask her to stay] "Then stay. I want you here."', "yes", forbids=(OWED,)),
       c('[Hold her to the debt] "You owe me. Pay it however you like."', "declined", requires=(OWED,), flags=(DECLINED,))),
    te("go", '{n}She is quiet for the space of three breaths. Then she inclines her head, the way the old silvers are said to take leave of one another on the mountain.{/n} "Then I will go home. On foot, since I must. It will be a long walk." {n}She takes the pike from the parapet and hands it to you, hilt-first.{/n} "Somebody will have to stand this watch. Pick a good one." {n}At the head of the stair she stops.{/n} "Keep the wound clean. I will write and ask."',
       c("[Watch her go down the stair.]")),
    te("declined", '''{n}Something in her face closes, gently, like a book.{/n} "Then I will pay it." {n}She takes up the pike.{/n} "I will guard you, crusader, as a debtor guards what she owes. I will be between you and whatever comes, and I will keep the dressing clean, and I will never once be late." {n}She turns back to the dark beyond the parapet.{/n} "But I will not love you as a debtor. You will have to do without that part."''',
       c("[Leave her to her watch.]")),
    te("yes", '''{n}She lets out a breath, and it smokes in the cold air a little longer than a breath should.{/n} "Then hear it." {n}She kneels on the stones of the turret, not as a supplicant, but as a knight kneels to take a post.{/n} "By the Wardstone I failed to keep, and the city I could not hold, and the blood I am made of: I will stand watch over this wound until one of us is dust. So I swear, Terendelev, once protector of Kenabres."''',
       c("Continue", "dressing")),
    nar("dressing", '''{n}Then she gets up, and unbuckles your coat without asking, and unpins the old dressing, and replaces it with a fresh one from her own pocket: clean linen, boiled, folded in a very exact square. Her fingers are warm and quite steady.{/n}''',
        c("Continue", "invite")),
    te("invite", '''"Every morning. At the same hour." {n}She pins it.{/n} "Tonight I stand the first watch. Come up after the second bell, if you would like company." {n}The corner of her mouth moves.{/n} "I will not leave my post, you understand. So you will have to be the one who comes to me."''',
       c('"I\'ll be here."', flags=(COMMITTED, DRESSING)),
       c('[Flirt] "Is that an order, protector?"', flags=(COMMITTED, DRESSING))),
], requires=(FIRST_NIGHT,), forbids=(COMMITTED, DECLINED, *PARENT_EMBODIED), delay=48)


# --- 9. The release: a debt forgiven -------------------------------------------------------------------------------------

watch(P + "commit.release", "A debt forgiven", '"We need to talk about the debt."', [
    nar("start", '{n}She keeps the turret watch and brings clean linen at the appointed hour. Her reports are exact; her manner is reserved. Today she finishes the knot in your dressing before looking up.{/n}',
        c("Continue", "talk")),
    te("talk", '''"There is nothing to talk about, crusader. The terms are clear. I am paying them." {n}She finishes pinning the dressing and steps back, correct as a sentry.{/n} "Unless you have thought of a better way I might pay. I am open to it. I am very good at settling accounts."''',
       c('[Release the debt] "You owe me nothing. You never did. I said it to make you stay."', "release"),
       c('"No. Carry on."', abort=True)),
    te("release", '''{n}She is very still.{/n} "To make me stay." {n}Something moves behind her eyes that is not quite anger.{/n} "You put a debt on a silver dragon to keep her by you. Do you know how many people have ever thought of doing that?" {n}A long breath.{/n} "None. Nobody was ever that foolish, or that frightened of being left."''',
       c('"It was stupid. I\'m taking it back."', "sworn"),
       c('"Frightened, yes. Of you walking to Kenabres."', "sworn")),
    te("sworn", '''"Then it is taken back, and I am not in your debt, and we will never speak of it again unless I want to tease you." {n}She almost smiles.{/n} "Now. Ask me properly. Not as your debtor. I want to hear it asked."''',
       c('[Ask her to stay] "Stand your watch over me. Because you want to."', "yes")),
    te("yes", '{n}She kneels on the cold stones, as a knight kneels to take a post.{/n} "By the Wardstone I failed to keep, and the city I could not hold, and the blood I am made of: I will stand watch over this wound until one of us is dust." {n}She rises. Her mouth curves.{/n} "Those were a debtor\'s terms before. This is my oath. Come up after the second bell. I shall be waiting."',
       c('"I\'ll be there."', flags=(COMMITTED, DRESSING))),
], requires=(DECLINED,), forbids=(COMMITTED, *PARENT_EMBODIED), delay=48)


# --- 10. The north turret: the night watch ------------------------------------------------------------------------------

watch(P + "night.watch", "The north turret", "[Climb to the north turret after the second bell.]", [
    nar("start", '''{n}The stair is dark, and the wind meets you halfway up it with snow on its breath. At the top the brazier has burned down to a red eye. She is at the parapet with the pike in the crook of her arm and the borrowed cloak around her, looking out at the dark where the Worldwound is.{/n}
{n}She does not turn round.{/n} "You are late. The second bell was a quarter of an hour ago."''',
        c('"I stopped to argue with a sentry about the proper way to hold a pike."', "want"),
        c("[Come and stand beside her.]", "want")),
    te("want", '"I have spent this war being careful. Of cities, of your little houses, of everyone who needed me to be stronger than they were." {n}She sets the pike against the parapet.{/n} "Tonight I want you. Come here."',
       c("[Go to her.]", "wound"),
       c('[Flirt] "On duty, protector?"', "duty")),
    te("duty", '''"On duty. Always." {n}She takes hold of the front of your coat and walks you backwards into the lee of the parapet, out of the wind, until your shoulders meet stone.{/n} "I told you I would not leave my post. I did not say I would neglect it."''',
       c("Continue", "wound")),
    nar("wound", '{n}Her hand goes first to the wound: under your coat, under the dressing, her palm flat on the place where you are open. It is hot under her hand, and her hand is hotter; heat answers heat, and the ache in you that has not stopped since Kenabres goes quiet and then turns into something else entirely.{/n}\n{n}She kisses you. Her mouth tastes of ozone and snow, like the air before a storm on a mountain, and her breath is so warm it fogs white between you in the cold.{/n}',
        c("Continue", "hoard")),
    nar("hoard", '''{n}She undresses you the way a dragon counts a hoard: one fastening at a time, slowly, turning each one over as if to learn its worth before she sets it aside. Buckle. Collar. Every lace of your shirt. She takes her time and makes very sure you know that she is taking it, and she laughs low in her throat when you try to hurry her.{/n}
{n}Your hands find the hem of her shirt and the long line of her back under it. Where they go, the human shape slips at its edges: silver surfaces along her collarbone like frost on a blade, and runs down her spine under your palms in a ridge of small, cool, perfect scales.{/n}''',
        c("Continue", "throat")),
    nar("throat", '''{n}She breathes in sharply at that, and her teeth, at your throat, are for an instant much too sharp. She stops. You feel her decide not to stop.{/n}
{n}Her shirt goes over her head and away into the dark. In the red of the brazier she is all long pale lines and heat, the silver running down her spine and gathering at the small of her back where your hands have gone, and when you pull her against you her skin is so warm that the snow melts on her shoulders before it can settle.{/n}''',
        c("Continue", "cloak")),
    nar("cloak", '''{n}The cloak goes down on the stones by the brazier. She lies back on it and draws you down over her by the waist of your breeches, unhurried, the way she might draw a blade she has decided to use; her knees rise on either side of your hips and her heels lock behind you, and her breath comes quick and white against your mouth.{/n}''',
        c("Continue", "cut")),
    nar("cut", '''{n}"Careless," she says, like an order, with her hands spread flat on your back to hold you to her against the wind, and pulls you down the last inch.{/n}
{n}The last thing the north turret sees of its watch is the cloak, the brazier's one red eye, and the pike leaning forgotten against the parapet.{/n}''',
        c("Continue", "grey")),
    te("grey", '''{n}In the grey hour before the sixth bell she lies with her head on your chest and the cloak over you both, listening to the wound under her ear as if it were a heartbeat.{/n} "I have kept a great many watches," {n}she says, very low.{/n} "I have never once been glad of the dark before. I was glad of this one." {n}Her fingers trace the edge of the dressing.{/n} "Do not tell the sentries. They would never respect me again."''',
       c('"Your secret\'s safe."', "morning"),
       c("[Pull the cloak up over her shoulders.]", "morning")),
    nar("morning", '''{n}The relief sentry comes up the stair at the sixth bell, coughing loudly and at length from the third step down.{/n}
{n}By the time his helmet clears the top of the stair she is sitting against the parapet in her breeches and the borrowed cloak, and nothing else. Her shirt is gone. It is wound round your middle in long, very neat strips, knotted over the wound with a knot a sailor would envy.{/n}''',
        c("Continue", "sentry")),
    te("sentry", '''"Nothing to report," {n}Terendelev tells the sentry gravely.{/n} "A quiet night. Carry on." {n}He salutes, and turns to the dark, and keeps his eyes very firmly on it. She leans her head back against the stone and closes her eyes.{/n} "Every morning," {n}she says to you, low.{/n} "At this hour. With my own hands. Do not argue; it is in the oath."''',
       c('"I wasn\'t going to argue."', "end"),
       c('"You\'ve run out of shirts."', "end")),
    te("end", '''{n}She opens one eye.{/n} "Then you will have to find me more. It is the least a Commander can do for the watch." {n}And she laughs, the bell of it carrying out over the cold roofs of Drezen, so that the sentry has to bite the inside of his cheek, and somewhere below in the lower town the two turnip men stop arguing to listen.{/n}''',
       c("[Go down and find her a shirt.]", flags=(NIGHT,))),
], requires=(COMMITTED,), delay=6)


# --- 11. The infirmary: a man with a knife (the pivotal node) ----------------------------------------------------------
# One of the knights who fought her ravener at Iz comes for her with a knife. What the Commander does in her name matters:
# she will not be defended with cruelty, and she remembers who stood aside.

INFIRMARY = P + "watch.infirmary_seen"
FLOGGED = P + "watch.infirmary_flogged"        # the order to flog him was given and left to stand (Evil)
REVOKED = P + "watch.infirmary_revoked"        # given, and taken back at her word
STOOD = P + "watch.infirmary_stood_between"
LET_HER = P + "watch.infirmary_let_her_answer"

watch(P + "watch.infirmary", "The man with the knife", '"There was trouble in the infirmary, they tell me."', [
    nar("start", '''{n}The infirmary is the long vaulted hall under the chapel, where the wounded from Iz lie in rows and the air smells of vinegar and old blood. She has been coming here every afternoon. You find her kneeling by a cot at the far end with her sleeves rolled to the elbow, one hand on a boy's splinted leg, speaking the old words under her breath.{/n}
{n}You are not the only one who has come to find her. A knight of the Queen's host stands in the doorway with his left arm strapped across his chest and a long knife in his right hand, and the whole hall has gone quiet around him.{/n}''',
        c("Continue", "knight")),
    nar("knight", '''{n}"That's it," he says. His voice is perfectly steady; it is his hand that shakes. "That's the thing from Iz. I was in the first lance. I watched it take Ser Hallen's horse out from under him and then take Ser Hallen. I watched it breathe on the second rank." He comes a step down the hall. "They say it's a lady now. They say the Commander bled on it. I don't care what it is now. It was that."{/n}
{n}Terendelev takes her hand off the boy's leg and stands up. She does not step back. She does not say anything at all.{/n}''',
        c('[Have him dragged out] "Guards. Take that man to the yard. Twenty lashes, for drawing steel in a house of healing."', "flog",
          alignment=("Evil", 1)),
        c('[Step between them] "If you want her, knight, you come through me first."', "between", flags=(STOOD,)),
        c("[Say nothing. This is hers to answer.]", "hers", flags=(LET_HER,))),
    te("flog", '''{n}The guards take him by both arms. The knife goes clattering down the aisle between the cots. And Terendelev's voice, which you have only ever heard low, fills the whole vault like a bell.{/n} "No."
{n}The guards stop. Everyone stops. She walks down the aisle, picks up the knife, and holds it out to the knight hilt-first, with his arms still pinned.{/n} "Commander. You will not do that in my name. Not ever. He has earned the right to hate me in a way that you have not earned the right to punish."''',
       c('[Revoke the order] "Let him go."', "answer", flags=(REVOKED,)),
       c('"The order stands. He drew steel on the wounded. Take him out."', "stands", flags=(FLOGGED,))),
    te("stands", '''{n}She looks at you, and there is nothing in her face at all, which is worse than anger. Then she lets the guards take him, and she walks out behind them into the yard, and she stands at the post the whole time with her hands folded, and keeps her eyes on him the whole time.{/n}
{n}When it is done she cuts him down herself and carries him back in, as easily as a child, and sets his shoulder, and heals his back with the old words. Then she goes out, and does not speak to you again that day.{/n}''',
       c("[Let her go.]")),
    te("between", '''{n}The knight stops with the point of the knife a yard from your chest. Behind you Terendelev puts one hand, very lightly, on your shoulder.{/n} "Thank you, crusader. That was well done. Now stand aside, please." {n}When you do not move at once, she steps round you, and goes down the aisle to him with her empty hands open at her sides.{/n}''',
       c("Continue", "answer")),
    te("hers", '''{n}She waits until she is quite sure you are not going to speak for her. Then she goes down the aisle to him, between the cots, with her empty hands open at her sides, until the point of the knife is almost touching her breastbone.{/n}''',
       c("Continue", "answer")),
    te("answer", '''"Ser Hallen had a red plume and a grey mare with one white stocking. He got under my wing with a lance and very nearly reached my heart." {n}She says it quietly, so that only the knight and the nearest cots can hear.{/n} "I remember all of you. That is the part that you will not believe, and it is true. I will not ask you to forgive me. I would not forgive it, in your place."''',
       c("Continue", "arm")),
    te("arm", '''"I will ask you something else." {n}She tilts her head at his strapped arm.{/n} "That bone was set badly in the field, and I can hear it grinding from here every time you breathe. Let me set it again. You may keep the knife in your other hand while I do, if it helps."''',
       c("Continue", "after")),
    nar("after", '''{n}He does not let her. He looks at her for a long breath, and then at you, and then he sheathes the knife with a hand that will not stop shaking and walks out of the infirmary without a word.{/n}
{n}He comes back the next afternoon, and sits on the end of an empty cot with his arm held out, and does not look at her while she sets it. Nobody in the hall says anything about that either.{/n}''',
        c("Continue", "end")),
    te("end", '{n}Later, washing her hands in the basin by the door, she says without turning round:{/n} "He will come back every day until he can look at me. That is the right way round. It should cost him nothing and me a great deal." {n}She dries her hands.{/n} "You let him keep his anger. He has lost enough already. Thank you for leaving me to answer it."',
       c("[Leave the infirmary with her.]", flags=(INFIRMARY,))),
], requires=(FIRST_NIGHT,), delay=24)


# --- 12. The market: honey and fried bread ------------------------------------------------------------------------------

MARKET = P + "watch.market_seen"
KISSED = P + "watch.kissed_in_the_market"
BREAKFAST = P + "watch.breakfast"

watch(P + "watch.market", "Honey and fried bread", '"You look like someone who wants to go somewhere."', [
    te("start", '''"I want to go to the market. The evening one, by the lower gate, where they fry bread in the street and a man with one leg plays the fiddle for coppers." {n}She stands, and brushes off the borrowed cloak.{/n} "Merriment is one of the best medicines, crusader. I told you so on the square. I was talking about your wound. I have lately begun to suspect I was also talking about mine."''',
       c('"Lead on."', "market"),
       c('[Flirt] "Is this an invitation, protector?"', "invite")),
    te("invite", '''"It is a prescription." {n}Her mouth twitches.{/n} "Dragons do not issue invitations; we are too large for the doorways. We issue prescriptions, and the patient is expected to follow them. Come along."''',
       c("Continue", "market")),
    nar("market", '''{n}The evening market by the lower gate is small and loud and smells of smoke, onions and hot fat. There is a fiddler, one-legged, exactly where she said. There is a woman with a pan of oil and a bowl of dough and a crock of honey that she guards with her elbow.{/n}
{n}Terendelev buys two pieces of fried bread with honey and gives you one, and eats hers standing in the street with her eyes shut, the way a person drinks water after a long march.{/n}''',
        c("Continue", "breakfast", requires=(BREAKFAST,)),
        c("Continue", "coat", forbids=(BREAKFAST,))),
    te("breakfast", '''"This is the same woman." {n}She opens her eyes.{/n} "From the morning you asked for breakfast instead of a life. I have been coming every day since. She thinks I am a widow from Kenabres with a very large appetite and nobody to cook for, and she gives me the burnt pieces for nothing." {n}A sidelong look.{/n} "I have not corrected her. It is the first lie I have told in two hundred years, and it is entirely your fault."''',
       c("Continue", "coat")),
    te("coat", '''"Now." {n}She licks honey off her thumb with great dignity.{/n} "Clothes. This cloak belonged to a sergeant who is twice my width and smells of a horse, and everything else I own was borrowed off a line in the barracks yard, which I suspect makes it stolen." {n}She considers.{/n} "I should like one thing that fits. You may choose it. I have no idea what humans wear now; the last time I bought a coat, sleeves were a great deal more exciting."''',
       c('"Something grey. The colour of your scale."', "grey"),
       c('"Something blue, like the sky over Kenabres on a festival morning."', "blue"),
       c('[Flirt] "I\'m not sure I\'m the one to ask. I like the borrowed shirts."', "shirts")),
    te("grey", '''{n}She holds a long grey coat up against herself in the stall-keeper's lamplight, turning it.{/n} "The colour of my scale. Or of rain on the roofs of Kenabres, which is what I will think of every time I put it on." {n}She pays for it without haggling, which appals the stall-keeper.{/n} "Yes. That will do very well."''',
       c("Continue", "child")),
    te("blue", '{n}She holds a long blue coat up against herself in the stall-keeper\'s lamplight, and her face does something you did not expect.{/n} "The festival square. Yes. The sky was this colour when I knelt beside you. You were in a very poor state to admire it." {n}She pays without haggling.{/n} "I shall wear it. There were good things in Kenabres that morning. I mean to remember them."',
       c("Continue", "child")),
    te("shirts", '''"The borrowed shirts." {n}She gives you a long, level look over the stall-keeper's table, and a slow colour comes up her throat that has nothing to do with the cold.{/n} "Then I shall buy a coat, and wear it over the borrowed shirts, and you will have to wonder which of them I have on underneath." {n}She pays for something long and grey without haggling, which appals the stall-keeper.{/n}''',
       c("Continue", "child")),
    nar("child", '''{n}A girl of about seven has been following you both since the fried bread, with the fixed stare of a child who has been told something by an older brother and does not believe it. At last she plants herself in front of Terendelev in the middle of the street.{/n}
{n}"Are you really a dragon?"{/n}''',
        c("Continue", "ice")),
    te("ice", '''{n}Terendelev looks down at her with perfect gravity.{/n} "You do not believe me? Perhaps I should retake my true form and cover this whole market in ice, to win your trust." {n}The girl's eyes go very wide. Then Terendelev laughs, the bright, melodious laugh from the square, and crouches down to the girl's height.{/n} "I am teasing you. I cannot, just now. I left my wings somewhere, and I am waiting for them to find their way back. Will you believe me anyway?"''',
       c("Continue", "believe")),
    nar("believe", '''{n}The girl considers this with enormous seriousness, decides that it is the sort of thing a real dragon would say, and runs off to tell her brother he was right.{/n}
{n}Terendelev stays crouched in the street for a moment longer than she needs to. When she straightens there is honey on her chin and something in her face you have not seen there since Iz: not grief, and not courage. She looks, very simply, happy.{/n}''',
        c('[Kiss her, there in the street.]', "kiss", flags=(MARKET, KISSED), forbids=(OWED,)),
        c('[Wipe the honey off her chin with your thumb.]', "honey", flags=(MARKET,), forbids=(OWED,)),
        c('"You\'re good with children."', "children", flags=(MARKET,)),
        c('[Kiss her, there in the street.]', "kiss", flags=(MARKET, KISSED), requires=(OWED, COMMITTED)),
        c('[Wipe the honey off her chin with your thumb.]', "honey", flags=(MARKET,), requires=(OWED, COMMITTED)),
        c('[Kiss her, there in the street.]', "kiss_debt", flags=(MARKET,), requires=(OWED,), forbids=(COMMITTED,)),
        c('[Wipe the honey off her chin with your thumb.]', "honey_debt", flags=(MARKET,), requires=(OWED,), forbids=(COMMITTED,))),
    te("kiss", '''{n}She is startled; you feel it go through her, and then she is not startled at all. She kisses you back in the middle of the lower market with the fiddler sawing away and the whole street pretending not to look, and her mouth tastes of honey and hot fat and, underneath, something sharp and clean, like the air on a mountain before snow.{/n}
{n}When she draws back she is laughing under her breath.{/n} "In the street. In front of the woman with the honey. She will think me a very forward widow." {n}She does not let go of your coat.{/n} "Good."''',
       c("[Walk her back through the market.]")),
    te("honey", '''{n}She holds very still while you do it. Your thumb comes away sticky; she catches your wrist before you can wipe it on your coat, looks at you, and licks the honey off your thumb herself, unhurried, with her eyes on yours the whole time.{/n}
"Waste not," {n}says Terendelev, and lets go, and walks on through the market as though nothing whatever has happened, and does not look back to see whether you are following. She knows you are.{/n}''',
       c("[Follow her.]")),
    te("children", '''"I was, once." {n}She watches the girl vanish into the crowd.{/n} "Kenabres had a great many of them, and they all wanted to ride on my back, and the prelate thought it undignified, so of course I let them." {n}Her smile fades a little and does not go.{/n} "I would like to be good with them again. It seems I still can be. I was not sure."''',
       c("[Walk her back through the market.]")),
    te('kiss_debt', '{n}She turns her cheek. Your mouth brushes it; she steps back and straightens the borrowed cloak.{/n} "Not while I owe you." {n}She picks up the parcel of bread.{/n} "Come. It is getting cold."', c("[Walk back with her.]")),
    te('honey_debt', '{n}She lets you wipe the honey away, then offers you a clean corner of the cloth wrapped round the bread.{/n} "Here. You will make your sleeve filthy." {n}She folds the cloth again and turns toward the citadel.{/n}', c("[Walk back with her.]")),
], requires=(FIRST_NIGHT,), delay=24)


# --- 13. What the Commander is --------------------------------------------------------------------------------------------

WHAT = P + "watch.what_you_are"

watch(P + "watch.what_are_you", "What you are", '"You\'ve been watching me all afternoon."', [
    te("start", '''"I have. I have been trying to decide what you are." {n}She says it the way a scholar names a problem.{/n} "I have met angels, crusader. I have met aeons, who made my teeth ache, and one very rude azata who sang at me for an hour. You are not any of them. Every one of them has a shape to their power, like a river has banks. Yours has no banks at all."''',
       c("Continue", "cheat")),
    te("cheat", '"And I am made of it. That is what troubles me." {n}She folds her arms.{/n} "Last night I played cards with the sentries on the north turret. I have played cards with crusade sentries for years, and never cheated them. Last night I cheated. I did it without thinking, the way you reach for a cup, and I won eleven coppers and a very fine knife." {n}Her voice drops.{/n} "Silver dragons do not cheat. It is very nearly the second article of our religion. Is that you, in me?"',
       c('"Areelu put a crystal in me, in the caves under Kenabres. Everything I can do grew out of that wound. I didn\'t choose what it became."', "areelu", requires=(AREELU_TOLD,)),
       c('"I\'m someone who doesn\'t take the world\'s rules on trust. Apparently that\'s catching."', "rules"),
       c('"I don\'t know what I am. Neither does anyone else. That\'s rather the point."', "point")),
    te("areelu", '"Areelu\'s work." {n}She looks at the dressing at your side.{/n} "You have given me rather more to think about than eleven coppers. I shall watch myself. You need not look so solemn; I have not decided to blame you for the cards."',
       c("Continue", "cards")),
    te("rules", '"Catching." {n}She laughs despite herself.{/n} "Silver dragons live by rules, crusader. Old ones. Customs so old that the other dragons laugh at us for keeping them. I keep my oaths even when they are inconvenient. Now I must be careful not to cheat at cards. I did not expect to need that precaution." {n}She shakes her head.{/n} "You do not stand behind walls. You walk up to them and look for the loose stone. And I am made of you."',
       c("Continue", "cards")),
    te("point", '''"That is not an answer, that is a dodge." {n}Her eyes narrow, and then something like delight comes into them.{/n} "Oh. It is also an answer, is it not? You are whatever the question was not expecting. Deskari did not expect you. Nor did I, lying in that fire. Nor did the Wound, I think." {n}She turns this over.{/n} "It is a very lawless way to be alive, crusader. I am not sure I approve of it. I am quite sure I would not be alive without it."''',
       c("Continue", "cards")),
    te("cards", '''"So." {n}She unfolds her arms.{/n} "I will give the sentries their eleven coppers back. I will keep the knife, because I won it fairly in the end, when I noticed what I was doing and started again." {n}A small, wry smile.{/n} "And I shall watch myself. If I start telling jokes at funerals, crusader, I expect you to tell me."''',
       c('"I\'ll tell you. I\'ll probably laugh first."', flags=(WHAT,)),
       c('"Keep the coppers. You earned them."', flags=(WHAT,))),
], requires=(FIRST_NIGHT,), delay=48)


# --- 14. A letter to the mountains ----------------------------------------------------------------------------------------

LETTER = P + "watch.letter_written"

watch(P + "watch.letter", "A letter to the mountains", '"Who are you writing to?"', [
    te("start", '''{n}She has borrowed a lap desk from somewhere and is writing on it on her knees, in a large, square, careful hand, with a great many crossings-out.{/n} "My teacher. Halaseliax, who came to the cave, long ago, when the Wound had me black to the heart, and sat at the mouth of it for a year until I could look at him without wanting to tear his throat out." {n}She blots a line.{/n} "I do not know whether he still lives. Letters to dragons are very patient things. They wait on a ledge until someone comes by."''',
       c('"What are you telling him?"', "tell")),
    te("tell", '''"That is the difficulty." {n}She holds the page out so you can see: three lines, all struck through.{/n} "I began, 'Teacher, I have died.' That seemed abrupt. Then, 'Teacher, I have been raised by a demon lord and used against the crusade.' That seemed worse. Then, 'Teacher, I am made of a mortal's blood and I cannot fly, and I am happier than I have been in a hundred years.'" {n}She looks at the last line.{/n} "That one is true. I cannot send it. He would come."''',
       c('"Would that be so bad?"', "come"),
       c('"Tell him the true one. He sat at a cave for a year for you. He\'s earned it."', "true")),
    te("come", '''"He would come, and he would look at you, and he would look at me, and he would know exactly what you did at Iz and what it cost you." {n}She smiles, crookedly.{/n} "And then he would thank you. Formally. For an entire afternoon. Gold dragons are very thorough about gratitude; it is one of their worst qualities."''',
       c("Continue", "true")),
    te("true", '''"The true one, then." {n}She dips the pen, and writes, slowly, saying it aloud as she goes.{/n} "'Teacher. I died at Kenabres, and I was used after, and I am not going to tell you how. A mortal came to the fire and asked me to come back, and opened a wound for it that will not close. I am made partly of that mortal now. I cannot fly. I play cards with sentries. I am happier than I have been in a hundred years.'" {n}She stops.{/n} "What else should I tell him?"''',
       c('"Tell him you\'re keeping a watch again."', "watchline", flags=(LETTER,)),
       c('"Tell him thank you. From me. For the year at the cave."', "thanks", flags=(LETTER,)),
       c('"Tell him nothing else. Let him come and find out."', "nothing", flags=(LETTER,))),
    te("watchline", '"\'I am keeping a watch again,\'" {n}she writes.{/n} "\'Over a wound, this time, not a stone. A smaller watch than a city. I find I am no less stubborn about it.\'" {n}She sands the page.{/n} "He will understand that. He was always telling me I guarded the Wardstone as though I were its mother."',
       c("Continue", "seal")),
    te("thanks", '''{n}She looks at you for the space of a breath, and then writes it, word for word, and adds underneath, in the same square hand:{/n} "'The mortal says thank you for the year at the cave. The mortal does not know what that year was like, and I have not told it, and I do not intend to. But the mortal is right.'"''',
       c("Continue", "seal")),
    te("nothing", '''"Let him come and find out." {n}She laughs, and writes nothing more, and folds the page.{/n} "You are a cruel creature. He will fly for a week with that letter in his claws and nothing in it but a riddle. He will be furious." {n}She seals it.{/n} "He will love it. He always said I had no sense of humour."''',
       c("Continue", "seal")),
    te("seal", '''{n}She seals the letter with a blob of candle wax and presses her thumb into it, since she has no seal, and turns it over in her hands.{/n} "There is a pass north of Drezen where the caravans go. I will give it to a driver and ask him to leave it on the highest rock he passes. Somebody will find it, in a year, or ten." {n}She tucks it into her coat.{/n} "It is a very dragon way of sending a letter. I find I have missed it."''',
       c("[Leave her to her ink.]")),
], requires=(FIRST_NIGHT,), delay=36)


# --- 15. The Storyteller: someone was listening -------------------------------------------------------------------------

LISTENED = P + "watch.storyteller_thanked"

watch(P + "watch.listener", "Someone was listening", '"The Storyteller asked me to tell you something."', [
    te("start", '''"The blind elf with the stories? I have seen him on the citadel steps. He turns his head when I pass, the way dogs do when they hear their name in another room." {n}She waits.{/n} "What did he ask you to tell me?"''',
       c('"That while you were in the dark, someone was listening. He heard your voice in his visions, while you were in the dark."', "heard")),
    te("heard", '''{n}She does not say anything at all for a while. The street goes by.{/n} "I thought I was alone," {n}she says at last.{/n} "In the bones. I thought nobody could hear it. That was the worst of it, crusader, worse than the killing: that I was screaming and the world was going on as if I were not." {n}She stands.{/n} "Take me to him. Now, please, before I decide that it is undignified."''',
       c("[Take her to the Storyteller's shelves.]", "shelves")),
    nar("shelves", '''{n}The old elf is sitting where he always sits, among his books, with a cup gone cold at his elbow. He turns his head before either of you speaks, and his face changes, and he puts the cup down very carefully, as though he had been holding it for a long time.{/n}
{n}Terendelev kneels down on the floor in front of him, in the dust, in her borrowed cloak, and takes both his hands in hers.{/n}''',
        c("Continue", "thanks")),
    te("thanks", '''"You heard me." {n}Her voice is very low.{/n} "All that time. I did not know. I thought I was screaming into a sack." {n}She bows her head over his hands.{/n} "Thank you. It was a poor comfort, you told the Commander. It was the only one there was, and I did not even know I had it, and I am grateful for it now, which is the wrong way round, but it is the way I have."''',
       c("Continue", "elf")),
    nar("elf", '''{n}The Storyteller does not say anything for a moment. Then he frees one hand, and lays it on her head, lightly, the way you would lay a hand on a child's head at a blessing, and says in a voice that is not quite steady: "I have told a great many stories that ended at a pyre, my lady. I am so very glad to have one that did not."{/n}
{n}Terendelev laughs, and wipes her eyes on the back of her wrist, and gets up off the floor, and there is dust on her knees, and she does not brush it off.{/n}''',
        c("[Leave them to talk.]", flags=(LISTENED,))),
], requires=(FIRST_NIGHT, P + "voice.asked"), forbids=("storyteller.dead",), delay=24)


# --- 16. The dressing: the morning after, and the day the Wound closes ---------------------------------------------------

FINALE_ASKED = P + "finale.asked"
FINALE_PLAN = P + "finale.plan"

watch(P + "watch.morning", "The dressing", '"You\'re early."', [
    nar("start", '''{n}She comes to your rooms at the same hour every morning with clean linen folded in a square, knocks once, and does not wait to be told to come in. This morning she is early, and there is a line between her brows.{/n}
{n}She unpins the old dressing, looks at the wound with the frank attention of a surgeon, puts her palm flat on it, says the words, and watches it go on bleeding. Then she binds it again, very neatly. Her hands are warm and steady. She does not let go when the knot is tied.{/n}''',
        c('"What is it?"', "ask")),
    te("ask", '''"The Wound." {n}Not yours; the other one. She says it without looking up.{/n} "I can feel its weather, you know. In my blood. Your blood. Some mornings it is loud, and some mornings it is quiet, and this morning it is very quiet indeed, the way the sea goes quiet before a storm." {n}Her hands tighten on the knot.{/n} "You are going to try to close it. Everyone says so. The whole citadel is packing for it."''',
       c("Continue", "fear")),
    te("fear", '''"And I lay awake last night and thought: I am made out of your wound, and your wound knows the Worldwound's weather the way a child knows its mother's voice. If the Worldwound closes, what happens to a body made out of its echo?" {n}She says it very evenly.{/n} "Perhaps nothing. Perhaps I go on exactly as I am. Perhaps I go out like the fire in the skull at Iz. I do not know. Nobody knows. There is no book."''',
       c('"Then we\'ll find out together."', "together", flags=(FINALE_ASKED,)),
       c('"I\'ll find a way. I always do. Give me time to plan."', "plan", flags=(FINALE_ASKED, FINALE_PLAN)),
       c('"Would you rather I didn\'t close it?"', "rather", flags=(FINALE_ASKED,))),
    te("together", '''"Together." {n}She considers it, and something in her shoulders comes down.{/n} "That is not a plan, crusader. That is what people say when they have no plan." {n}She smooths the dressing flat with her palm.{/n} "It is also, I find, the only thing I wanted to hear. How very undignified."''',
       c("Continue", "end")),
    te("plan", '''"You will find a way." {n}She looks up at you then, and her eyes are the grey of her scale in the morning light.{/n} "Yes. I think you probably will. You found one in a fire at Iz, with a knife and a guess, and I was the only one who did not think you were mad." {n}A pause.{/n} "That is not true. I thought you were mad. I simply did not mind."''',
       c("Continue", "end")),
    te("rather", '''{n}Her head comes up sharply.{/n} "Do not even say it." {n}And then, more gently, because you meant it, and she can see that you did:{/n} "I kept a city against that thing for longer than you have been alive. If it closes and takes me with it, I will count that a very good bargain, and so will you, eventually. Close it. That is an order, from the watch."''',
       c("Continue", "end")),
    te("end", '''{n}She pins the dressing, and gathers up the old linen, and at the door she stops.{/n} "If the dressing opens on the march, send a messenger. Do not wait for it to soak your coat." {n}Then she goes, and you hear her on the stair, humming something under her breath that sounds very much like a Kenabres festival song.{/n}''',
       c("[Finish dressing.]")),
], requires=(NIGHT,), delay=24)

# --- 17. Letters while the Commander is away (Chapter 5 marches) ---------------------------------------------------------

def letter(id, title, nodes, requires, forbids=(), delay=72, **extra):
    SCENES.append(scene(id, title, "Terendelev", 5, "", nodes, requires=("trickster.ever", RETURNED, *requires),
                        forbids=(CLOSED, AEON, *forbids), delay=delay, last=5, Relationship=REL, Chapters=[5], Remote=True,
                        Kind="letter", **extra))


letter(P + "letter.watch_report", "The north turret: a report", [
    te("start", '{n}Terendelev passes you the watch report, written in a large, square, careful hand and headed: REPORT OF THE NORTH TURRET WATCH.{/n}\n"From the watch log: four nights, no alarms, one sentry reprimanded twice. Dressings changed at the appointed hour. The wound continues to complain."',
       c("Continue", "more")),
    te("more", '''"Otherwise: the woman who fries bread by the lower gate asks after you. I have told her you are busy with crusade business, and she has decided that you are my {mf|husband|wife}, and gives me the burnt pieces out of pity. I have not corrected her.
"The Worldwound's weather is loud this week. I feel it in my wrists. Keep the dressing clean. Change it at the proper hour, not whenever you remember. I will know.
"The watch is very dull between dressings. T."''',
       c("[Fold the letter into your coat.]")),
], requires=(NIGHT,), delay=96, ManualOnly=True)

letter(P + "letter.debtor", "A report, correctly made", [
    te("start", '{n}The folded report is written in a large, square, careful hand.{/n}\n"Commander. I have taken the turret watch. The linen is boiled and folded and waits in your rooms. The debt remains unpaid. I have not forgotten it. Terendelev."',
       c("[Read it again, looking for anything else in it.]", "nothing")),
    nar("nothing", '''{n}There is nothing else in it. There is a small blot of ink at the foot of the page where the pen rested for a long while before she signed, as though she had been going to write something more and decided against it.{/n}''',
       c("[Put it away.]")),
], requires=(DECLINED,), forbids=(COMMITTED,), delay=72)


# --- 18. The third bell: she cannot sleep in the dark (a visit, before the watch is agreed) ------------------------------

SAT_UP = P + "watch.sat_up"

SCENES.append(scene(P + "watch.third_bell", "The third bell", "Terendelev", 5, "", [
    nar("start", '''{n}Someone knocks at your door at the third bell of the night: once, very quietly, the knock of someone who will go away again if nobody answers.{/n}
{n}It is Terendelev, in her shirtsleeves and the borrowed cloak, barefoot on the cold stone of the corridor, with a candle in her hand that she has shielded so carefully from the draughts that it has burned down to the holder.{/n}''',
        c("[Let her in.]", "in")),
    te("in", '''"I am sorry. I know the hour." {n}She does not come further in than the doorway.{/n} "I put out my candle to sleep and it was dark, and in the dark I was back in the bones, and I could feel his purpose pulling at me like a hook in the mouth. Guard Iz. Kill whoever comes." {n}Her hand is shaking; the candle-flame shakes with it.{/n} "I lit the candle again. It burned down. I did not know where else to go that had a light in it."''',
       c('"Come in. Sit by the fire. I\'ll sit up with you."', "fire"),
       c('[Take the candle from her and light a fresh one from it.]', "fire")),
    nar("fire", '''{n}She sits on the floor by your hearth with her back against the side of the chair and her knees drawn up, as close to the fire as she can get without being in it. You sit in the chair. She sets the candle on the hearthstone. After a while she leans her head against your knee and closes her eyes.{/n}
{n}Neither of you says anything for a long time. The fire mutters. The sentries call the fourth bell along the walls.{/n}''',
        c("Continue", "talk")),
    te("talk", '''"In Kenabres I slept on the cathedral roof, most nights, in my true shape, curled round the bell-tower like a cat round a milk jug. The bell used to wake me every hour. I liked it. It meant the city was still there to ring it." {n}Her voice is drowsy now.{/n} "I have not slept a whole night since Iz. Talk to me, crusader. About anything. I do not care what. Only let there be a voice in the room that is not his."''',
       c('[Tell her about the Abyss: the red sky, the demons in good coats, the worst meal you ever ate.]', "abyss"),
       c('[Tell her about the festival square after she dulled your pain.]', "gate"),
       c('[Tell her nothing. Hum instead, badly, the tune the fiddler played at the market.]', "hum", requires=(MARKET,)),
       c('[Tell her nothing. Hum instead, badly, a festival tune from Kenabres.]', "hum", forbids=(MARKET,))),
    nar("abyss", '''{n}You tell her about the Abyss: the red that never becomes night, the demons who dress for dinner, a stew in a tavern in Alushinyrra whose ingredients you still refuse to guess. She laughs, once or twice, sleepily, at the right places. At the stew she laughs properly, into your knee.{/n}''',
        c("Continue", "sleep")),
    nar("gate", '{n}You tell her about the square after the pain eased: bunting overhead, festival stalls, people going about their day. She listens with her head against your knee. Beyond the window a sentry calls the hour.{/n} "The bunting," {n}she murmurs.{/n} "I helped hang it. They could never reach the top of the gate."',
        c("Continue", "sleep")),
    nar("hum", '''{n}You hum. It is very bad. She lifts her head to look at you in outraged disbelief, and then puts it back down on your knee and starts, very softly, to hum it with you, correctly, until you give up and let her have it.{/n}''',
        c("Continue", "sleep")),
    nar("sleep", '''{n}Somewhere after the fifth bell she falls asleep, with her head on your knee and one hand closed round your ankle, as though she were holding a post. Her breathing is slow and even and warm through the cloth. The fire burns low. You do not move.{/n}
{n}In the grey before morning she wakes, sees where she is, and does not move either.{/n} "That was a whole night," {n}she says, astonished, into your knee.{/n} "A whole night, and no hook."''',
        c('"Any time you need a light."', "end", flags=(SAT_UP,)),
        c('[Flirt] "You\'re welcome in here any time. With or without the candle."', "end_flirt", flags=(SAT_UP,))),
    te("end", '''{n}She gets up, stiffly, and looks down at you in the chair.{/n} "That is a dangerous offer to make a dragon, crusader. We take things literally, and we come back." {n}At the door she stops.{/n} "Thank you. I will try the dark again tonight. Knowing where the light is may be enough."''',
       c("[Let her go.]")),
    te("end_flirt", '''{n}She gets up, stiffly, and looks down at you in the chair with an expression that is not in the least drowsy any more.{/n} "With or without the candle." {n}She lets the words sit in the cold air between you.{/n} "I will remember you said that. I remember everything anyone says to me after midnight. It is very inconvenient, mostly for me." {n}And she goes, and you hear her laughing on the stair.{/n}''',
       c("[Let her go.]")),
], requires=("trickster.ever", RETURNED, FIRST_NIGHT), forbids=(CLOSED, AEON, COMMITTED, DECLINED), delay=36, last=5,
    Relationship=REL, Chapters=[5], Areas=[DREZEN], Remote=True, Kind="visit", ManualOnly=True))


# --- 19. The war table: the Wound's weather ------------------------------------------------------------------------------
# The Commander is a meticulous and sometimes callous planner; her blood knows the Wound's weather. Using it costs her.

COMPASS = P + "watch.compass"          # the Commander used her as the crusade's compass; it hurts her every time
NOT_A_MAP = P + "watch.not_a_map"

watch(P + "watch.war_table", "The Wound's weather", '"You wanted to see the war table."', [
    nar("start", '''{n}The war room in the citadel is cold, and the great table is covered with the crusade's map of the Worldwound, weighted at the corners with daggers and a boot. Terendelev stands at its edge with her hands behind her back, the way a knight stands at a briefing, and looks at the red-inked blot of the Wound for a long while before she speaks.{/n}''',
        c("Continue", "feel")),
    te("feel", '''"I told you I can feel its weather. I have not told you how well." {n}She points without looking, at a place on the map where your scouts have marked nothing at all.{/n} "There. It is loud there tonight, like a wasps' nest under a floor. Something is gathering. And there, by the ford, it is quiet; the kind of quiet a room has when somebody is holding their breath behind the door." {n}Her finger comes down.{/n} "I could be wrong. I do not think I am."''',
       c('"How does it feel, when you do that?"', "cost")),
    te("cost", '''"Like putting my hand on a stove to learn if it is hot." {n}She takes her hand off the map and looks at it.{/n} "It is your blood in me that knows. Whatever the Abyss put into your wound knows its own kind. When I listen to it, it listens back, and for a little while afterwards I am not entirely sure which of us is doing the listening." {n}A small, wry shrug.{/n} "But it would save lives. I have always been good at that sum."''',
       c('[Use her] "Then read it for me. Every night, before the scouts go out. Tell me where it\'s loud and where it\'s holding its breath."', "use",
         flags=(COMPASS,)),
       c('[Trust your intuition] "Tell me only where it\'s quietest. That\'s where they\'re waiting, and that\'s where I\'ll send nobody."', "quiet",
         flags=(COMPASS,), mythic="Trickster"),
       c('"No. You\'re not a map, and I won\'t use you as one."', "no", flags=(NOT_A_MAP,))),
    te("use", '''"Every night." {n}She nods once, like a soldier taking an order she had expected.{/n} "Very well. I will come down at the second bell and put my hand on this map and tell you what I hear." {n}Then, lower:{/n} "You did not hesitate, crusader. I noticed. It is the right choice, and you made it the way a good commander makes the right choice: at once, and at someone else's expense." {n}She almost smiles.{/n} "I do not hold it against you. I only noticed."''',
       c("Continue", "blood")),
    te("quiet", '{n}She follows the line of the river with her finger.{/n} "I have spent this war looking for ambushes. The scouts can find hidden bodies. This may find the thing hiding behind them." {n}She sets her palm on the map again.{/n} "Very well. I shall listen for the places that are too quiet. Second bell, before the scouts leave. Have a cloth ready. It will make my nose bleed."',
       c("Continue", "blood")),
    nar("blood", '''{n}When she takes her hand off the map there is a single drop of blood on the parchment beside the ford, from her nose. She wipes her lip with the back of her wrist and looks at the drop with a kind of detached interest.{/n} "Your colour," {n}she says.{/n} "I keep forgetting it is not mine."''',
        c("[Give her your handkerchief.]")),
    te("no", '{n}She looks at you across the map for the space of a breath, and something in her face you cannot read.{/n} "No. Not a map." {n}She takes her hand back.{/n} "Kenabres used me for one, you know. Night after night: where are the demons, Terendelev, how many, how soon. I never minded. I was their dragon." {n}A pause.{/n} "It is a strange thing, to be told I am not something. I think I like it. I will tell the scouts what I felt tonight, all the same. Once. As a gift, not a duty."',
       c("[Walk her out of the war room.]")),
], requires=(FIRST_NIGHT, PROOF), delay=24)


# --- 20. The Kenabres refugees: the ribbon-seller ------------------------------------------------------------------------

KNOWN = P + "watch.known_to_kenabres"   # she let the Kenabres refugees know who she is
HIDDEN = P + "watch.hidden_from_kenabres"

watch(P + "watch.refugees", "The ribbon-seller", '"There\'s a crowd round your crate."', [
    nar("start", '''{n}There is. Most of them are the Kenabres refugees who came north with the crusade after the fall and live now in the lower town, in lean-tos against the old wall. In the middle of them an old woman is sitting on the cobbles in front of Terendelev's crate, crying without making any noise, with a tray of faded festival ribbons in her lap.{/n}
{n}Terendelev looks up at you over the old woman's head with the expression of a sentry who has just been asked for a password she has forgotten.{/n}''',
        c("Continue", "old")),
    nar("old", '''{n}"I sold ribbons on the square," the old woman says to you, because you are the Commander and she has decided you should know. "Forty festivals. Every year the silver lady bought a blue one and tied it on the gate, up where nobody could reach. Every year." She wipes her face. "I'd know that hand anywhere. The way she holds her money. I'd know it. She's dead. We all saw her die. And she's sitting on a crate in Drezen buying my ribbons."{/n}''',
        c("Continue", "choice")),
    te("choice", '''{n}Terendelev speaks low, to you, under the old woman's weeping.{/n} "They are all listening. Half of them are from Kenabres. If I tell them who I am, it will be all over the lower town by nightfall, and all over the crusade by morning, and they will want me to be what I was. Their dragon. I cannot fly, crusader. I cannot be that." {n}Her hands are clenched in the cloak.{/n} "If I tell them she is mistaken, she will go home and think she is going mad. Tell me what to do. No; do not. I will decide. Only stay here while I do."''',
       c("[Stay beside her. Say nothing.]", "decide"),
       c('[Quietly] "They lost everything. You\'re the one thing they could get back."', "decide"),
       c('[Quietly] "You don\'t owe them the dragon. You\'ve already died for them once."', "decide")),
    te("decide", '''{n}She is silent a moment. Then she gets down off the crate, and kneels on the cobbles in front of the old woman so that their faces are level, and takes the tray of ribbons gently out of her lap, and chooses one. Blue.{/n} "You gave me the long end, every year, and charged me for the short one." {n}Her voice carries, a little, whether she means it to or not.{/n} "I always knew. I never said. It was worth the difference, to see you cheat a dragon."''',
       c("Continue", "crowd")),
    nar("crowd", '''{n}The old woman makes a sound you will remember for a long time. And the whole crowd moves, not closer, but lower: one after another, the people of Kenabres going down on their knees on the cobbles of Drezen, the way people used to kneel in the square when a silver shape went over the Wardstone at evening.{/n}
{n}Terendelev looks at them all, and her face does something terrible and then steadies.{/n} "Get up," {n}she says.{/n} "Get up, all of you. I am not your dragon any more. I am a woman on a crate who owes you a great deal, and I would like to start paying it. Who here has a roof that leaks?"''',
        c("Continue", "after")),
    te("after", '''{n}Afterwards, when the crowd has gone off arguing about roofs, she sits back down on the crate with the blue ribbon wound round and round her fingers.{/n} "That was either very brave or very foolish. I told them. It is done." {n}She looks at the ribbon.{/n} "They will want too much of me, and I will give it to them anyway, and in a month I will be more tired than I was in the bones. And every one of them will have a dry roof." {n}She ties the ribbon round her wrist.{/n} "I think I was lonely, crusader. I did not know it until she said my hand."''',
       c("[Sit down on the cobbles beside her crate.]", flags=(KNOWN,))),
], requires=(FIRST_NIGHT, KENABRES_TOLD), delay=24)


# --- 21. A second report, while the Commander is away ------------------------------------------------------------------

letter(P + "letter.second_report", "The north turret: a second report", [
    te("start", '''{n}Another page torn from the quartermaster's ledger, in the same large square hand. This one is not headed at all.{/n}
"The Wound was loud last night, loud as I have ever felt it, and then very suddenly quiet, and I stood at the parapet until the sixth bell waiting for it to be loud again. It was not. I do not know what that means. I do not like not knowing.
"I folded a fresh dressing this morning, at the proper hour, and tied the knot round my own bare wrist and untied it again, so that my hands would not forget it."''',
       c("Continue", "end")),
    te("end", '''"The woman with the honey has given me a whole loaf for you, which is on your table and going stale, and the ribbon-seller has given me a ribbon for you, which is blue, and which I am to tie on you personally the next time I see you, she says, for luck. I have agreed to do this. You will not fidget. That is an order from the watch.
"I have been careful for three hundred years and it has not once felt like this. Come up to the turret. T."''',
       c("[Read it again.]")),
], requires=(NIGHT,), delay=192, ManualOnly=True)


# --- Reactions: two more who were at Iz --------------------------------------------------------------------------------

SCENES.append(reaction("Daeran", P + "react.daeran.cousin", (RETURNED,),
    '''{n}Daeran is lounging in his chair with a glass, and he looks you over with his most delighted expression, the one that usually means somebody else is about to have a very bad day.{/n} "My dear Commander. You raised a dragon from a pyre with your own blood, in front of my cousin's knights, without so much as a chant. I have spent a small fortune on necromancers who could not raise a cat." {n}He swirls the glass.{/n} "And not a necromancer at all, apparently. She bleeds. She blushes. I checked, discreetly." {n}His smile thins.{/n} "My cousin came a very long way to give that creature rest. Do take care, my friend. Galfrey forgives nothing she has knelt over."''',
    answer_list="4d978cbd2aa780d46874255282039f3f", relationship=REL, forbids=("daeran.dead", "daeran.kicked_out", "galfrey.dead", CLOSED, "chapter_later"),   # retired (Q6 r2, COX)
    entry='"You look amused, Daeran."', chapter=5, last=5, delay=24, portrait="Daeran"))

SCENES.append(reaction("Regill", P + "react.regill.unsanctioned", (RETURNED,),
    '''{n}Regill slides the marked sentry reports across the desk.{/n} "An undead abomination of the Abyss, destroyed by crusade forces at Iz. And then restored, in the field, by the Commander, by an unsanctioned rite of the Commander's own devising, using the Commander's own blood." {n}He sets the pen down.{/n} "There is no article of any code I know that covers it. I have looked. The Order would call it imprudence bordering on criminality." {n}He turns the page over.{/n} "She stood the night watch on the north wall three times this week and reported two lapses among the sentries, both correct. I have noted it. That is all."''',
    answer_list="2366a8db6481070439fee222c0c52e45", relationship=REL, forbids=("regill.dead", "regill.kicked_out", "regill.left_plot", CLOSED, "chapter_later"),   # retired (Q6 r2, COX)
    entry='"You have something to say, Regill."', chapter=5, last=5, delay=48, portrait="Regill"))

# --- 22. The mountains: why she came down ------------------------------------------------------------------------------

MOUNTAINS = P + "watch.mountains"

watch(P + "watch.mountains", "Why she came down", '"Where did you live, before Kenabres?"', [
    te("start", '''"In the mountains, with my kin, the way silver dragons do. A cave the size of this citadel, with a floor of old snow and older gold, and a view of three valleys and a river that went silver at sunset." {n}She smiles at something a long way off.{/n} "We are a very orderly people, crusader. We keep customs so old that the other dragons laugh at us. The elders live such pure, exact lives that you could set a water-clock by their breathing. I meant to be one of them, when I was a thousand."''',
       c('"What happened?"', "wound")),
    te("wound", '''"The Worldwound opened." {n}Simply.{/n} "We are long-lived, and we live apart, and to us your lives go by like sparks off a fire. It is very easy, from a mountain, to watch sparks go out and call it the way of things." {n}She looks down at her hands.{/n} "I could not. I went down to see. I saw the refugees on the roads from Sarkoris, and the crusade's first dead, and I stayed. My elders thought it very young of me. I suppose it was."''',
       c('"Do you regret it?"', "regret"),
       c('"And the foulness? The cave?"', "cave")),
    te("regret", '''"Never once." {n}At once, without heat.{/n} "I chose to be a champion of the meek, and I have been one, and I have never been sorry. Even in the bones I was not sorry that I came down; I was only sorry that I had been made to hurt the people I came down for." {n}A pause.{/n} "I am sorry I cannot go back up, now, to tell them I was right. That is vanity. Silver dragons are allowed a very little."''',
       c("Continue", "kenabres")),
    te("cave", '''"You have heard that part." {n}She is quiet.{/n} "My unit was ambushed near the Wound, early, and I was infected with its filth, and my scales went black from the chest outward. I hated everyone who had not been touched. My friends. My friends most of all." {n}Her jaw sets.{/n} "They carried me to a cave and left me, and I thought they were glad to be rid of me, and I was wrong. I was wrong about everything, that year. It took me the whole of it, and my teacher at the mouth of the cave, to find that out."''',
       c("Continue", "kenabres")),
    te("kenabres", '''"And after that, Kenabres." {n}Her voice warms.{/n} "At first it was only the place where the Wardstone was: a post, a duty. And then one day I was flying over it at evening and I saw that the baker on the east street had painted his shutters blue, and I was so pleased about it that I circled twice. That was when I knew. It was not a post any more. It was mine, and I was its."''',
       c('"And now?"', "now")),
    te("now", '''"And now I am on a crate in the lower town of Drezen, with no wings, made partly of a mortal." {n}She laughs, softly.{/n} "The elders would say that I have come down further than any silver dragon in the history of our kind, and they would be right." {n}She looks at you sidelong.{/n} "I find I do not mind the height as much as I expected. The view from down here has certain compensations."''',
       c('[Flirt] "Such as?"', "such", flags=(MOUNTAINS,)),
       c('"Your elders would be proud of you. Whatever they say."', "proud", flags=(MOUNTAINS,))),
    te("such", '''"Such as a mortal who asks 'such as' in that tone of voice, on a public street, in front of the tiefling who sells lamp-oil." {n}She holds your eyes, and she does not blush, quite.{/n} "I am three hundred years old, crusader. I know exactly what I meant. I am waiting to see whether you do."''',
       c("[Hold her gaze.]")),
    te("proud", '''"Proud." {n}She considers it gravely.{/n} "No. They would be appalled, and they would write me a very long letter explaining why. But under it, in the part they would not write down..." {n}She smiles.{/n} "Perhaps. My teacher, at least. He always said I would come down to the world one day and never be able to climb back up. I think he meant it as a warning. I think he was also a little envious."''',
       c("[Leave her to her street.]")),
], requires=(FIRST_NIGHT,), delay=36)


# --- 23. After the fight: waiting at the gate (a visit) -----------------------------------------------------------------

QUARRELLED = P + "watch.quarrel"

SCENES.append(scene(P + "watch.at_the_gate", "At the gate", "Terendelev", 5, "", [
    nar("start", '''{n}You come down into the citadel yard at dusk after a day of councils and drill, and some time in the afternoon the old wound in your side, the one she keeps dressed, opened under your coat without your noticing. You notice now: the shirt is stuck to it.{/n}
{n}She is standing at the foot of the stair. She has been standing there, the stair-sentry tells you later, since a clerk mentioned on the turret that the Commander had been seen at the council table with a hand pressed to one side, which was the middle of the afternoon.{/n}''',
        c("Continue", "look")),
    te("look", '''{n}She looks at your arm. She looks at the dark wet patch spreading over your side where the dressing has given up. She takes one very long breath, and it smokes in the torchlight.{/n} "Sit down on that step," {n}says Terendelev,{/n} "before you fall down it, and then I will decide whether to heal you or to kill you."''',
       c('"It\'s a scratch."', "scratch"),
       c("[Sit down on the step.]", "down")),
    te("scratch", '''"It is not a scratch. I can smell it from here, and so can every dog in the lower town." {n}She takes hold of your belt and sits you down on the step herself, not gently, and catches you when your knees go.{/n} "You have a hole in you that I made a promise over, crusader. You do not get to carry it into a council and sit on it all afternoon like this."''',
       c("Continue", "down")),
    nar("down", '''{n}She cuts the dressing away with your own knife, there on the stair, in front of the whole yard, and says the old words over the wound with her palm flat on it and her other hand gripping your wrist so hard it hurts. The pain goes quiet. The bleeding slows, and does not stop. It never does, for her; it only slows.{/n}''',
        c("Continue", "angry")),
    te("angry", '"The clerk told me you were bleeding. Then he went back inside and said nothing to the council." {n}She pulls the new dressing tight.{/n} "Nobody called me. Nobody called a surgeon. You sat there until your shirt stuck to the wound. I cannot fly to a window now, crusader. Send a messenger before you fall out of your chair."',
       c('"I can\'t promise that. It\'s a war."', "war", flags=(QUARRELLED,)),
       c('"I\'m sorry. I didn\'t think."', "sorry", forbids=(FLOGGED,)),
       c('[Take her hand, the one on the knot.]', "hand"),
       c('"I\'m sorry. I didn\'t think."', "sorry_flogged", requires=(FLOGGED,))),
    te("sorry_flogged", '''"You did not think. No." {n}The anger goes out of her, and something colder comes in behind it.{/n} "You think a great deal about some skins. You thought long enough about that boy's back in the infirmary to leave the order standing." {n}She pins the dressing.{/n} "You are careful with the people you have decided to be careful with, crusader. I have not yet worked out how you decide. I am not sure I want to."''',
       c("[Let her help you up.]")),
    te("war", '{n}She stops with both hands on the knot. The yard is noisy with soldiers coming off drill.{/n} "Yes. A war. I know what a wound costs when you leave it unattended." {n}She finishes the knot.{/n} "When it opens, tell someone. I have no wish to hear of it from a clerk who thinks it is council business."',
       c("[Let her help you up.]")),
    te("sorry", '''"You did not think. No." {n}The anger goes out of her all at once, like a held breath.{/n} "You never do, when it is your own skin. You thought a great deal at Iz, with a knife in your hand and my bones in the fire. You are very careful with everyone but yourself." {n}She pins the dressing.{/n} "I know that kind of creature. I was one. Somebody had to stand at the mouth of a cave for a year before I learned better."''',
       c("[Let her help you up.]")),
    te("hand", '''{n}She lets you. Her hand is shaking; you did not know dragons' hands could shake. She stands on the stair with your hand around hers and the whole yard crossing past pretending not to see, and does not say anything at all until the last of them has gone in.{/n}
"Three hours," {n}she says finally, very low.{/n} "Come inside. You are getting blood on the only coat that fits me."''',
       c("[Go inside with her.]")),
], requires=("trickster.ever", RETURNED, FIRST_NIGHT, DRESSING), forbids=(CLOSED, AEON), delay=60, last=5, Relationship=REL, Chapters=[5],
    Remote=True, Kind="visit", ManualOnly=True, Areas=[DREZEN]))

# --- 24. Faith: the prayer that will not come ---------------------------------------------------------------------------

FAITH = P + "watch.faith"

watch(P + "watch.faith", "The prayer that will not come", '"You were in the chapel again last night."', [
    te("start", '''"I was. I go every night." {n}She is turning the blue-grey stone of a sling-bullet over and over in her fingers, a thing she must have picked up in the street.{/n} "I served the Inheritor for longer than your crusade has had a name. I fought under her banner at the edge of the Wound when the first crusaders were still arguing about whose banner to fight under." {n}The stone stops.{/n} "And I kneel in her chapel every night now, and I cannot pray. The words will not come."''',
       c('"Your healing words come."', "healing"),
       c('"Why not?"', "why")),
    te("healing", '''"Those are not prayers. Those are mine; I made them, a long time ago, the way a smith makes a tool." {n}She shakes her head.{/n} "A prayer is a different thing. You open a door and say: here I am, as I am. And I cannot say it, crusader, because I do not know what I am, and I will not lie to her."''',
       c("Continue", "why")),
    te("why", '''"Because the last voice I answered in the dark was his." {n}Very low.{/n} "I knelt to him, in the bones. Not with my knees; I had none that were mine. But I knelt. I wanted his peace so much that I did everything he asked for it. And now I kneel in her chapel and open my mouth and the only words that want to come out are his: guard, kill, wait." {n}Her hand closes on the stone.{/n} "I will not give her those. I would rather give her nothing."''',
       c('"Then give her nothing. Kneel there anyway. She\'ll know what it means."', "nothing", flags=(FAITH,)),
       c('"Say something else, then. Anything true. Tell her about the ribbon-seller, or the turnip men."', "true", flags=(FAITH,)),
       c('"Maybe she isn\'t the one you need to say it to yet."', "yet", flags=(FAITH,))),
    te("nothing", '''"Kneel there anyway." {n}She considers it the way she considers everything, gravely, from all sides.{/n} "A sentry does not stop standing his post because nobody comes to relieve him. He stands it until they do." {n}Slowly, she nods.{/n} "Yes. I can do that. I am very good at standing a post and saying nothing. It is the one thing Deskari did not take out of me; he only pointed it the wrong way."''',
       c("[Leave her with it.]")),
    te("true", '''{n}She stares at you. Then she laughs, and it surprises her; you can see it surprise her.{/n} "Tell the Inheritor about the turnip men." {n}She wipes her eyes.{/n} "She will think I have gone mad. She will be right." {n}The laugh fades into something quieter.{/n} "But it is true, and it is small, and it is mine and not his. I will try it tonight. If the goddess of valour wishes to hear about the price of turnips in the lower town of Drezen, she shall."''',
       c("[Leave her with it.]")),
    te("yet", '''{n}She looks at you for a while without answering.{/n} "You mean that I should say it to you first. Here I am, as I am." {n}She turns the stone over once more and then puts it in your hand and closes your fingers over it.{/n} "Here I am, then. As I am. Made of you, and his, and three hundred years of my own. It is not a prayer. It will do to be going on with."''',
       c("[Keep the stone.]")),
], requires=(FIRST_NIGHT,), delay=48)


# --- 25. The silver on her collarbone: the morning the scales stay -------------------------------------------------------

SCALES = P + "watch.scales_stayed"

watch(P + "watch.scales", "The silver that stayed", '"You\'re wearing your shirt open at the throat."', [
    te("start", '''"I am. Look." {n}She draws the neck of her shirt aside with one finger, frankly, in the middle of the street, as she might show a healed cut.{/n} "Here."
{n}Along her collarbone, where your hands were on the turret, there is a line of small silver scales, cool and perfect, catching the light. It was there that night and gone by morning. It is here now, in the daylight, and it has not gone.{/n}''',
       c('"Does it hurt?"', "hurt"),
       c("[Touch it.]", "touch")),
    te("hurt", '''"No. It itches, rather, the way new skin itches." {n}She lets the shirt fall back.{/n} "It came up again this morning, while I was changing your dressing, and it stayed. There is a little down my spine as well, I think; I cannot see it. The sentries on the north turret have been very careful not to look."''',
       c("Continue", "hope")),
    nar("touch", '''{n}The scales are cool under your fingertips, and smooth, and you feel her pulse jump underneath them. She does not move away. After a moment she puts her own hand over yours and holds it there, flat against the silver.{/n} "It came up while I was changing your dressing this morning," {n}she says,{/n} "and it stayed."''',
        c("Continue", "hope")),
    te("hope", '''"I do not know what it means." {n}She says it carefully, like a woman stepping onto ice.{/n} "I tried the shape again, afterwards, on the turret. Nothing, as always. But something is coming back, crusader, a little at a time, from wherever it went. Or something new is growing where the old thing was. I cannot tell which." {n}Her mouth quirks.{/n} "I have decided not to hope about it. I am hoping about it very much."''',
       c('"Then I\'ll hope for both of us, so you don\'t have to."', "end", flags=(SCALES,)),
       c('[Flirt] "It seems to come up when I touch you. We should keep testing that."', "flirt", flags=(SCALES,))),
    te("end", '''"That is a very generous offer, and a very foolish one, and I accept it." {n}She buttons the shirt to the throat, and then, after a moment, unbuttons the top button again, so that the silver shows.{/n} "There. Let the lower town look. It is about time something about me was worth looking at again."''',
       c("[Leave her to her street.]")),
    te("flirt", '''"We should keep testing it." {n}She repeats it with enormous gravity, as though you had proposed a course of study.{/n} "Yes. Rigorously. Every night, I think, for a very long time, to be sure of the result." {n}The gravity lasts until the tiefling trader drops a lamp, and then she is laughing, the old bell of it, in the middle of the lower town, with the silver showing at her throat.{/n}''',
       c("[Leave her laughing.]")),
], requires=(NIGHT,), delay=48)


# --- Reaction: Seelah, when she comes back ------------------------------------------------------------------------------

SCENES.append(reaction("Seelah", P + "react.seelah.alive", (RETURNED,),
    '{n}Seelah is sitting very still, which is not like her.{/n} "I went down to the lower town to see for myself. She was in the lower town, watching the street. She looked up and said my name the way the old sisters at the chapel used to, and asked me if I\'d kept my oath." {n}She laughs, and it cracks in the middle.{/n} "I watched her die over Kenabres from a roof, Commander. I prayed so hard my knees bled through my hose. And she asked me if I\'d kept my oath." {n}She wipes her face on her sleeve, fiercely.{/n} "I said yes. It\'s true. I\'m going to go back tomorrow and tell her properly."',
    answer_list="417fa384f3250634bb71859fbc913453", relationship=REL, forbids=("seelah_dead", "seelah_gone", CLOSED),
    ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"},
    entry='"You look like you\'ve seen a ghost, Seelah."', chapter=5, last=5, delay=24, portrait="Seelah"))

# --- 26. A message for the knight: Irabeth -------------------------------------------------------------------------------
# Her own acknowledgment of Irabeth (no scene with Irabeth present): the knight from the walls of Kenabres, who saw her come
# out of the fire, and, where the Queen fell at Iz, the knight whose Queen her body killed.

IRABETH_MESSAGE = P + "watch.irabeth_message"

watch(P + "watch.irabeth", "A message for the knight", '"You keep looking at the barracks."', [
    te("start", '''"The half-orc knight. Tirabade. The one who sang to her sword on the east wall at Kenabres." {n}Her eyes are on the barracks door.{/n}''',
       c("Continue", "passes", forbids=("irabeth_dead",)),
       c("Continue", "passes", requires=("irabeth_dead", "irabeth.trickster.returned")),
       c("Continue", "fallen", requires=("irabeth_dead",), forbids=("irabeth.trickster.returned",))),
    te("passes", '''"She walks past this crate twice a day and salutes me, very correctly, and does not stop. I think she does not know what to say to me. I know I do not know what to say to her."''',
       c("Continue", "queen", requires=(QUEEN_FELL,)),
       c("Continue", "walls", forbids=(QUEEN_FELL,))),
    te("fallen", '"They told me in the barracks that she fell at Iz, before I was brought out. We were not close. I knew her voice before I knew her name, and I had hoped to hear it again." {n}Her hands are still in her lap.{/n} "I went to the chapel and asked where she lies. The chaplain did not know. Nobody seems to know where anyone lies, after Iz."',
       c('"I\'ll find out for you."', "fallen_end", flags=(P + "watch.irabeth_grave_inquiry",)),
       c("[Say nothing. Sit with her.]", "fallen_end")),
    te("fallen_end", '''"Thank you." {n}She looks at the barracks door a while longer, as though somebody might still come out of it singing.{/n} "When I know, I will go and stand a watch there. One night. It is what we do, on the mountain, for someone whose song we knew."''',
       c("[Leave her watching the door.]")),
    te("queen", '''"She was there when I came out of the fire. She had her sword drawn over her Queen's body, and I was the thing that had made it a body." {n}Her hands are still in her lap.{/n} "And she found me a cloak and a horse because you told her to, and she rode beside me all the way out of Iz, and never once looked at me. I have been thinking about that ride every night. It was the bravest thing I have ever seen a mortal do, and she did it for an order."''',
       c("Continue", "ask")),
    te("walls", '''"She served on the walls of Kenabres for years. I knew her voice before I knew her name; there are not many knights who sing to their swords, and fewer who sing in tune." {n}A faint smile.{/n} "She saw me die over the city, as they all did. Now she sees me on a crate, eating fried bread. I think it offends her sense of order. It would offend mine."''',
       c("Continue", "ask")),
    te("ask", '''"I will not go to her. It is not my place to make her talk to me; she has had enough made of her by dragons this year." {n}She turns to you at last.{/n} "Will you carry something to her for me? Not a letter. Only this: that the dragon remembers the song, and the sword, and the east wall, and would be glad to hear it again, one day, if the knight should ever wish to sing it. And that the dragon asks nothing else of her. Nothing at all."''',
       c('"I\'ll tell her. Word for word."', "yes", flags=(IRABETH_MESSAGE,)),
       c('"Tell her yourself, when you\'re both ready. She\'ll come round."', "self")),
    te("yes", '''"Word for word." {n}She nods.{/n} "Silver dragons are particular about messages. If you change a word, I will know, and I will be very polite to you about it for a week." {n}She looks back at the barracks door, and at last her shoulders come down a little.{/n} "Thank you, crusader."''',
       c("[Leave her watching the door.]")),
    te("self", '''"When we are both ready." {n}She weighs it.{/n} "That may be a long time, for her. It may be a longer time for me." {n}Then, drily:{/n} "Very well. I am three hundred years old. I can outwait a knight. It is one of the few things I am still certainly better at than your people."''',
       c("[Leave her watching the door.]")),
], requires=(FIRST_NIGHT,), delay=36)

# --- 27. The road out of Iz (a visit, on the march back) ------------------------------------------------------------------

ROAD = P + "watch.road_from_iz"

SCENES.append(scene(P + "watch.road", "The road out of Iz", "Terendelev", 5, "", [
    nar("start", '{n}On the road out of Iz the column moved at a walk, because the wounded could go no faster. You remember Terendelev beside you on a borrowed horse, sitting bolt upright with both fists on the reins. The mare kept turning her head to inspect her rider. Terendelev refused to notice.{/n}',
        c('"You\'ve never ridden a horse before, have you?"', "horse"),
        c("[Ride on beside her and say nothing. Try not to laugh.]", "laugh")),
    te("horse", '''"I have been a horse's natural predator for three hundred years, crusader. It has not come up." {n}The mare shies at a rock; Terendelev grips harder and says something to it in Draconic that makes it flatten its ears.{/n} "In Kenabres I walked everywhere, in this shape, or I flew. Nobody offered me a horse. I think they were afraid I would eat it."''',
       c("Continue", "look")),
    te("laugh", '''"You are laughing." {n}She does not turn her head; turning her head appears to be beyond her.{/n} "I can hear you not laughing, and it is very loud. Go on, then. I have been a horse's natural predator for three hundred years. It is only fair that one of them should have its revenge on me in front of the whole crusade."''',
       c("Continue", "look")),
    nar("look", '''{n}And the whole crusade is looking, in its way: the knights and the sergeants and the walking wounded, turning in their saddles or on their crutches to see the silver-haired woman who came out of the fire. Some of them make the sign of the Inheritor as she passes. One spits. Most only look, the way people look at a comet, as though she might be a sign of something and they have not decided what.{/n}
{n}She sees it all. She sits her horse badly and very straight, and looks back at every one of them.{/n}''',
        c("Continue", "sky")),
    te("sky", '''{n}Later, when the column halts to water the horses and she has got down, with some difficulty and more dignity, she stands at the edge of the road looking back at Iz and the sky over it.{/n} "I used to fly over this," {n}she says.{/n} "Not here; further east, at the edge of the Wound, when I was young and the crusades were new. From up there it looked like a burn on the world. From down here it looks like the whole world." {n}She is quiet.{/n} "I did not know that. I should have. It would have made me humbler."''',
       c('"You were kind enough. You knelt on the cobbles for a stranger."', "kind"),
       c('"You\'ll get used to it. We all do."', "used")),
    te("kind", '"I knelt for strangers throughout this war. I do not regret it." {n}She looks along the column, at the wounded keeping pace with the horses.{/n} "I knew the streets of Kenabres. I did not know these roads from a saddle. At present I am learning rather more than I wanted about this mare. Help me up before she notices."',
       c("[Help her back up onto the mare.]", flags=(ROAD,))),
    te("used", '''"I hope not." {n}She shakes her head.{/n} "I do not want to get used to it. I want to remember, every day, how big it looks from down here, and how small everyone is who has to walk under it." {n}She looks at the mare, and sighs.{/n} "Now help me back up onto this creature before she decides I am a coward, and tells the others."''',
       c("[Help her back up onto the mare.]", flags=(ROAD,))),
], requires=("trickster.ever", RETURNED), forbids=(CLOSED, AEON, LATE, FIRST_NIGHT), delay=4, last=5, Relationship=REL, Chapters=[5],
    Remote=True, Kind="visit", ManualOnly=True))


# eng8-q8f: authored handovers and invitations through the existing two contacts.
_GAMEPLAY_ENTRIES = {
    "letter.watch_report": '"Let me read your watch report."',
    "letter.second_report": '"You have another report for me?"',
    "watch.third_bell": '"Come by my room after your watch."',
    "watch.at_the_gate": '"Walk with me to the citadel."',
    "watch.road": '"Tell me about the ride back from Iz."',
}
for _key, _entry in _GAMEPLAY_ENTRIES.items():
    _host = next(s for s in SCENES if s["Id"] == P + _key)
    _host.update(Entry=_entry, ContactUnit=HUMAN, InteractionHub=HUB,
                 Areas=[DREZEN], Remote=False, ManualOnly=False)
    if _key == "watch.road":
        # The existing completed-Iz reader witnesses the trip; the late return stays excluded.
        _host["Requires"] = list(dict.fromkeys([*_host["Requires"], "iz.done"]))
        _host["Nodes"][0]["Text"] = ('{n}Beside the trader\'s stall, Terendelev shakes her head at a passing horse. '
            'The ride back from Iz is still fresh in her memory.{/n}\n' + _host["Nodes"][0]["Text"])
    _host.pop("Kind", None)
    _twin = copy.deepcopy(_host)
    _twin["Id"] += "_awning"
    _twin["InteractionHub"] = HUB_FB
    if _key == "watch.road":
        _twin["Nodes"][0]["Text"] = _twin["Nodes"][0]["Text"].replace("Beside the trader's stall", "Under the tailor's awning", 1)
    _twin["Requires"] = list(dict.fromkeys([*_twin["Requires"], HUB_FAILED]))
    _host["Forbids"] = list(dict.fromkeys([*_host["Forbids"], _twin["Id"]]))
    _twin["Forbids"] = list(dict.fromkeys([*_twin["Forbids"], _host["Id"]]))
    SCENES.append(_twin)
# end eng8-q8f


# Both presence hubs use the same sold-memory variants; old answers keep their indices.
for suffix in ("", "_awning"):
    foresight.gap(REL, P + "watch.proof" + suffix, (("fear", 0),), "try",
        """{n}She speaks the words again, low, with her palm flat over the dressing. The pain goes quiet, at once, completely, like a dog called to heel.{/n}
{n}The bleeding does not stop. Under her hand the dressing darkens, slowly, as it always does.{/n}""",
        foresight.GONE_SQUARE)
    foresight.gap(REL, P + "after.first_night" + suffix, (("start", 1),), "turnips",
        '''"Neither. That is the beauty of it." {n}She almost laughs.{/n} "They will be back tomorrow, and the turnips will be worse, and they will both be alive to be angry about it. I sat here all night listening to that. I cannot tell you how beautiful it was."''',
        foresight.GONE_SQUARE)


# The remaining laugh comparisons also describe the Commander's senses, rather than Terendelev's own memory.
for _beat, _node, _via, _old, _new in (
    ("after.first_night", "nothing", ("sums", 0),
     "She laughs, and this time it is the laugh from the square, bright as a bell in cold air;",
     "She laughs, bright as a bell in cold air;"),
    ("after.first_night", "breakfast", ("sums", 1),
     "And then she is laughing, the laugh from the square, bright as a bell in cold air,",
     "And then she is laughing, bright as a bell in cold air,"),
    ("watch.market", "ice", ("child", 0),
     "Then Terendelev laughs, the bright, melodious laugh from the square,",
     "Then Terendelev laughs, bright and melodious,"),
):
    for _suffix in ("", "_awning"):
        _host = P + _beat + _suffix
        _scene = next(s for s in SCENES if s["Id"] == _host)
        _text = next(nd["Text"] for nd in _scene["Nodes"] if nd["Id"] == _node)
        foresight.gap(REL, _host, (_via,), _node, _text.replace(_old, _new), foresight.GONE_SQUARE)


def integrate(payload):
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)


# eng7-l09 / E-Q7-26: her memory remains hers; the Commander supplies no sold senses.
for _suffix in ("", "_awning"):
    if not any(s["Id"] == P + "watch.third_bell" + _suffix for s in SCENES):
        continue  # The remote third-bell host currently has no awning twin.
    foresight.gap(REL, P + "watch.third_bell" + _suffix, (("talk", 1),), "gate",
        '{n}You repeat the survivors\' accounts of the festival square. Your own morning is gone. Terendelev listens with her head against your knee.{/n} "The bunting," {n}she murmurs.{/n} "I helped hang it. They could never reach the top of the gate."',
        foresight.GONE_SQUARE)
# end eng7-l09
# eng8-q8d: her debtor report is handed over on either earned presence hub.
_eng8_report = next(s for s in SCENES if s['Id'] == P + 'letter.debtor')
_eng8_report.pop('Kind', None)
_eng8_report.update(Remote=False, Entry='[Take her report.]', ContactUnit=HUMAN,
                     InteractionHub=HUB, Areas=[DREZEN])
_eng8_report['Nodes'][0]['Text'] = ('{n}Terendelev hands you a folded report. Her writing is large, square and very careful.{/n}\n'
                                     + _eng8_report['Nodes'][0]['Text'].split('\n', 1)[1])
_eng8_twin = copy.deepcopy(_eng8_report)
_eng8_twin['Id'] += '_awning'
_eng8_twin['InteractionHub'] = HUB_FB
_eng8_twin['Requires'].append(HUB_FAILED)
_eng8_twin['Forbids'].append(_eng8_report['Id'])
_eng8_report['Forbids'].extend([_eng8_twin['Id'], HUB_FAILED])
SCENES.append(_eng8_twin)
# end eng8-q8d
# eng8-q8h begin: the documented proof and personal receipts govern both hubs.
DEBT_FREE = P + "debt_free"
PERSONAL_BEATS = (WINGS, KENABRES_TOLD, DESKARI_VOW, DESKARI_LET_GO,
    GALFREY_SPOKEN, INFIRMARY, FLOGGED, LETTER, LISTENED, SAT_UP, FAITH)
for _scene in SCENES:
    if _scene["Id"] in (P + "after.first_night", P + "after.first_night_awning"):
        _sums = next(nd for nd in _scene["Nodes"] if nd["Id"] == "sums")
        for _choice in _sums["Choices"][:2]:
            _choice["Set"].append(DEBT_FREE)
    if _scene["Id"] in (P + "commit", P + "commit_awning", P + "commit.release", P + "commit.release_awning"):
        _scene["Requires"].append(PROOF)
        _scene.setdefault("RequiresAnyGroups", []).append(list(PERSONAL_BEATS))
    if _scene["Id"] in (P + "commit.release", P + "commit.release_awning"):
        _release = next(nd for nd in _scene["Nodes"] if nd["Id"] == "yes")
        for _choice in _release["Choices"]:
            _choice["Set"].append(DEBT_FREE)
# The late predicate is owned by the earlier registered restitution module.
from storylines import terendelev_trickster as _q8_terendelev
_q8_terendelev.DERIVED[P + "late_committed"] = [
    ["trickster.ever", FIRST_NIGHT, DEBT_FREE, PROOF, beat] for beat in PERSONAL_BEATS]
# end eng8-q8h


# Reviewed polish M20: fallback scenes retain their actual seat and witness.
for _scene in SCENES:
    if not _scene["Id"].endswith("_awning"):
        continue
    _beat = _scene["Id"][len(P):-len("_awning")]
    if _beat == "watch.refugees":
        _scene["Entry"] = '"There is a crowd under the awning."'
    if _beat in ("after.first_night", "watch.refugees", "watch.mountains", "watch.irabeth"):
        for _node in _scene["Nodes"]:
            _node["Text"] = (_node["Text"].replace("on the crate", "on the bale of cloth")
                .replace("this crate", "this awning").replace("Terendelev's crate", "Terendelev's bale")
                .replace("a crate", "a bale of cloth").replace("the crate", "the bale of cloth")
                .replace("by the stall", "under the awning")
                .replace("sitting on a bale of cloth in Drezen buying", "sitting under an awning in Drezen buying")
                .replace("the tiefling trader pretends to count his stock", "the tailor pretends to count his needles"))
    if _beat == "watch.mountains":
        _such = next(nd for nd in _scene["Nodes"] if nd["Id"] == "such")
        _such["Text"] = '"Such as a mortal who asks that question in that tone, on a public street, while the tailor pretends to count his needles."' + _such["Text"][_such["Text"].index(" {n}"):]
    if _beat == "watch.scales":
        _flirt = next(nd for nd in _scene["Nodes"] if nd["Id"] == "flirt")
        _flirt["Text"] = _flirt["Text"].split(" {n}The gravity lasts")[0] + ' {n}The tailor pricks his finger and swears. Terendelev laughs, with the silver showing at her throat.{/n}'


# Authored polish M14: restitution to the Queen's men does not absolve her killer.
QUEEN_OWNED = P + "watch.queen_owned"
QUEEN_ANSWERED = P + "watch.queen_answered"
watch(P + "watch.galfrey_why", "The Queen's death", '"You asked why I killed Galfrey."', [
    te("start", '"She held Mendev against the Wound for a hundred years. She went to Iz to give me rest. You killed her." {n}Terendelev looks directly at you.{/n} "Tell me why. I shall hear it once."',
       c('"I chose to kill her. That death is mine."', "owned", flags=(QUEEN_OWNED,)),
       c('"She was in my way. I would do it again."', "leave", flags=(CLOSED, GUARDIAN)),
       c('[Lie] "It was mercy. There was no other choice."', "leave", flags=(CLOSED, GUARDIAN)),
       c('"I will not answer you."', "leave", flags=(CLOSED, GUARDIAN))),
    te("owned", '"Then do not ask me to mourn her while you spend what was hers. Her household knights still carry her banner. I shall speak to them. You will hear what they need before you ask me to stand a watch for you."', c("[Leave her to the knights.]")),
    te("leave", '{n}She stands and gathers her cloak.{/n} "I cannot keep your watch. Kenabres still needs mine." {n}She passes you without offering her hand.{/n}', c("[Let her leave.]")),
], requires=(QUEEN_KILLED,), forbids=(QUEEN_OWNED, QUEEN_ANSWERED))
watch(P + "watch.galfrey_reckoning", "The Queen's household", '"You have spoken to Galfrey\'s knights."', [
    te("start", '"They want their banner, their quarters, and leave to bury their dead. Your quartermaster has kept all three waiting." {n}She lays his account on the table.{/n} "Three hundred from the war chest, under your seal. Pay it. These men went to Iz for their Queen. They did not go to become the spoils of her killer."',
       c('[Order the restitution] "Their banner, their quarters and their leave. See it done."', "paid",
         crusade=("Finances", -300), flags=(QUEEN_ANSWERED,)),
       c('"No. They serve the crusade now."', "leave", flags=(CLOSED, GUARDIAN)),
       c("[Return when the war chest can meet the cost.]", abort=True)),
    te("paid", '"I shall take them the order myself." {n}She folds it under the account.{/n} "Galfrey\'s death is still yours. This settles what you took from her men. It does not settle her death."', c("[Let her carry the order.]")),
    te("leave", '{n}She stands and gathers her cloak.{/n} "I cannot keep your watch. Kenabres still needs mine." {n}She passes you without offering her hand.{/n}', c("[Let her leave.]")),
], requires=(QUEEN_OWNED,), forbids=(QUEEN_ANSWERED,), delay=72)

# Consume the existing scene override contract at both affirmative oath offers.
for _scene in SCENES:
    if _scene["Id"] in (P + "commit", P + "commit_awning", P + "commit.release", P + "commit.release_awning"):
        _scene["Forbids"].append(QUEEN_KILLED)
        _scene["ForbidOverrides"] = dict(_scene.get("ForbidOverrides", {}))
        _scene["ForbidOverrides"][QUEEN_KILLED] = QUEEN_ANSWERED
for _scene in _q8_terendelev.SCENES:
    if _scene["Id"] == P + "epilogue.late":
        _scene["Forbids"].append(QUEEN_KILLED)
        _scene["ForbidOverrides"] = dict(_scene.get("ForbidOverrides", {}))
        _scene["ForbidOverrides"][QUEEN_KILLED] = QUEEN_ANSWERED


def polish_memory_answers(payload):
    """M3/M26: consume shared gaps and preserve the original Last Call position."""
    for host in (P + "watch.third_bell", P + "watch.third_bell_awning"):
        scene = next(s for s in payload["Scenes"] if s["Id"] == host)
        talk = next(n for n in scene["Nodes"] if n["Id"] == "talk")
        assert talk["Choices"][4]["Next"] == "gap.gate"
        talk["Choices"][4]["Text"] = "[Tell her what the survivors remember of the festival square.]"
    # The shared Last Call placer follows the last epilogue. The appended guardian
    # mourning page must not move this existing saved scene past the old letter twin.
    scenes = payload["Scenes"]
    coda = next(s for s in scenes if s["Id"] == "terendelev.lastcall.page")
    scenes.remove(coda)
    anchor = next(i for i, s in enumerate(scenes) if s["Id"] == P + "epilogue.rest")
    scenes.insert(anchor + 1, coda)


# Round 2: one shared healing watch; no new romance or medical prerequisite.
from storylines.terendelev_trickster import HAL_MET, HAL_LETTER, DESKARI_NOTICE, DESKARI_SETTLED
for _s in SCENES:
    _base = _s["Id"].removesuffix("_awning")
    _nodes = {nd["Id"]: nd for nd in _s["Nodes"]}
    if _base == P + "commit":
        _nodes["start"]["Text"] = ('{n}She takes you up to the north turret at dusk. Below, the infirmary windows '
            'are lit; the men who could not leave Iz on their own feet are still being carried in. A garrison helper '
            'waits by the brazier with boiled linen and a basin. Terendelev has brought a blanket and her pike.{/n}')
        _nodes["dressing"]["Text"] = ('{n}The helper cuts away the old linen while Terendelev steadies your shoulder. '
            'She speaks her healing words; the pain eases, but the wound stays open. Together they bind it. '
            'She checks the knot, sends the basin down to the infirmary, and waits until the helper has gone.{/n}')
        _nodes["invite"]["Text"] = ('"That is the dressing done." {n}She draws your coat closed and keeps her '
            'fingers on its collar.{/n} "I am taking the watch tonight. Come up after the second bell. '
            'I should like you here when there is no basin between us."')
        _nodes["invite"]["Choices"][0]["Text"] = '"Keep me a place by the brazier."'
    if _base == P + "night.watch":
        _nodes["start"]["Text"] = ('{n}At the top of the stair a helper hands you the last bundle of clean linen '
            'and goes down with the empty basin. Terendelev has finished tending the wounded below. She stands '
            'at the parapet, cloak drawn tight, pike under her arm. Snow melts on the rim of the brazier.{/n} '
            '"Put that down. The dressing can wait until dawn."')
        _nodes["want"]["Text"] = ('{n}You lay the linen by the brazier. She watches your hands, then your face. '
            'Below, a stretcher party calls for the infirmary door to be opened. She waits until the door shuts.{/n} '
            '"They have their healer tonight. Now I want you." {n}She sets the pike against the parapet and '
            'holds out her hand.{/n} "Come here."')
        _nodes["want"]["Choices"].append(c('"Let me sit with you tonight. Nothing more."', "company"))
        _s["Nodes"].append(te("company", '{n}She gathers the blanket and makes room beside the brazier.{/n} '
            '"Then sit close. You are taking half the blanket, and I shall take half your warmth." '
            '{n}At the next bell she takes up the pike again.{/n}', c("[Stay beside her.]", abort=True)))
        _nodes["wound"]["Text"] = ('{n}She feels the knot through your shirt, checks that it has held, then '
            'withdraws her hand. Her fingers catch your jaw instead. She kisses you hard enough to press your '
            'shoulders against the stone; when you pull her closer she laughs against your mouth and kisses you again.{/n}')
        _nodes["cut"]["Text"] = ('{n}"Closer," she says, with her hands spread on your back. '
            'She pulls the edge of the cloak over your shoulders.{/n} '
            '{n}Her breeches are gone, and yours, kicked away across the stones in the red light of the brazier. '
            'Under the cloak she is nothing but heat and the cool silver ridge of her spine, bare skin against bare skin, '
            'her breasts crushed to your chest, her thighs open and trembling round your hips. She has kept a thousand watches '
            'and has never once wanted to be relieved of one. Her hand slides between you, closes, guides, and she lifts '
            'her hips to meet you with a low sound in her throat that is half a laugh and half a growl.{/n} '
            '"I have held this post a long time," {n}she says against your mouth.{/n} "Do not make me wait at it."')
        _slot = _s["Id"] + ".explicit.1"
        _nodes["cut"]["Choices"][0]["Next"] = _slot
        # Explicit slot: her chosen night beneath the cloak; continue into the grey hour and shirt dressing.
        _s["Nodes"].append(nar(_slot, '{n}Terendelev draws you into a fierce kiss. '
            'The cloak closes over you both; the pike rests against the parapet.{/n}', c("Continue", "grey")))
        _nodes["sentry"]["Text"] = ('"Nothing to report," {n}Terendelev tells the sentry. He coughs, salutes, '
            'and fixes his eyes on the road. One bare shoulder shows above her cloak. She tucks it out of sight '
            'and presses her palm against the new dressing.{/n} "That will hold. I want breakfast before the next one. '
            'And a shirt."')
    if _base == P + "watch.refugees":
        _nodes["old"]["Text"] += (' {n}Terendelev bends over the tray.{/n} "The blue one. Did you leave me '
            'the extra length for the gate?" {n}The old woman nods through her tears. Terendelev lays a coin '
            'on the tray and takes the ribbon.{/n}')
    if _base == P + "watch.morning":
        _nodes["start"]["Text"] += (' {n}With the knot finished, she puts the linen aside and kisses you. '
            'Her hand stays at your cheek. Then she looks toward the packed saddlebags.{/n}')
    if _base == P + "watch.deskari":
        _notice = _nodes["ask"]["Choices"][2]
        # The legacy receipt remains a personal grudge beat; NOTICE distinguishes word from escort.
        _notice["Set"].append(DESKARI_NOTICE)
        _notice["Next"] = "notice"
        _s["Nodes"].append(te("notice", '"Word, then. I shall expect word." '
            '{n}She folds her hands over the pike.{/n} "I have waited in silence quite long enough."',
            c("[Leave her with it.]")))
    if _base == P + "watch.letter":
        _nodes["start"]["Choices"].append(c('"I met him at your old refuge. He told me how he helped you."',
            "hal", requires=(HAL_MET,)))
        _s["Nodes"].append(te("hal", '"Alive." {n}She sets the pen down.{/n} "And you stood where '
            'he stood when I could not bear to look at him. I am glad." {n}She draws a fresh sheet toward her.{/n} '
            '"He may have flown elsewhere by now. But a courier can leave this at the refuge. '
            'I shall write the address myself."', c('"What will you tell him?"', "tell", flags=(HAL_LETTER,))))
        _nodes["seal"]["Choices"][0]["Forbids"].append(HAL_LETTER)
        _nodes["seal"]["Choices"][0]["Next"] = "pass"
        _s["Nodes"].append(te("pass", '"There is a pass north of Drezen where the caravans go. '
            'I shall ask a driver to leave it on the highest sheltered rock he passes." '
            '{n}She tucks the letter into her coat.{/n} "I shall ask the next driver."',
            c("[Leave her to her ink.]")))
        _nodes["seal"]["Choices"].append(c("[Take the addressed letter for the courier.]", "refuge",
            requires=(HAL_LETTER,)))
        _s["Nodes"].append(te("refuge", '{n}She crosses out the northern pass and writes directions '
            'to her old refuge beneath the seal.{/n} "Leave it out of the rain. That is all. '
            'Do not ask the courier to wait for a dragon." {n}She gives you the folded sheet.{/n}',
            c("[Send it with the next courier.]")))
        _nodes["seal"]["Text"] = ('{n}She presses her thumb into the candle wax and turns the letter over.{/n} '
            '"For a dragon, a sheltered ledge will serve as a letter-box. Somebody may find it in a year, or ten. '
            'I find I have missed sending them."')
    if _base == P + "watch.galfrey":
        for _key in ("queen_back", "queen_back_priestess"):
            _nodes[_key]["Text"] = _nodes[_key]["Text"].replace('I saw her cross the chapel yard last night,',
                'I recognised Kitrane in the chapel yard last night,').replace('One day I shall speak to her in private.',
                'The Queen stays dead to the world. If Kitrane wishes to speak to me, I shall meet her in private.')

# The existing war-table conversation collects the escort debt before departure.
# Original exits stay selectable; the appended question neither gates romance nor forces attendance.
for _s in SCENES:
    if _s["Id"] not in (P + "watch.war_table", P + "watch.war_table_awning"):
        continue
    for _node in _s["Nodes"]:
        if _node["Id"] in ("blood", "no"):
            _node["Choices"].append(c('"About taking you to face Deskari. The army is nearly ready."',
                "departure", requires=(DESKARI_VOW,), forbids=(DESKARI_NOTICE, DESKARI_SETTLED)))
    _s["Nodes"].extend([
        te("departure", '{n}Terendelev lays the infirmary roll beside the map. She taps three names.{/n} '
            '"These cannot walk. Those six can, if someone changes their dressings. You promised me Deskari. '
            'I counted them this morning, and I have changed my mind."',
            c('"You want to stay?"', "departure_stay"),
            c('"My promise stands. There is a horse for you."', "departure_stay")),
        te("departure_stay", '"Give it to a wounded man. I shall keep this watch." {n}She folds the roll.{/n} '
            '"I want his death as much as I did at Iz. But he has had my body march to his purpose once. '
            'He will not set its road again. I release you from the promise. If you face him, finish it."',
            c('"I will send word."', "departure_end", flags=(DESKARI_SETTLED,))),
        te("departure_end", '{n}She gathers the roll and the bloody handkerchief.{/n} '
            '"There. My place in the column is settled. Now go and sleep. You will have enough sleepless '
            'nights ahead." {n}She takes the roll back to the infirmary.{/n}', c("[Let her go.]")),
    ])


# struct2-08: historical returns do not prove current availability. Sweep both hosts.
for _scene in SCENES:
    _base = _scene['Id'].removesuffix('_awning')
    if _base not in (P + 'watch.irabeth', P + 'watch.galfrey'):
        continue
    _start = next(node for node in _scene['Nodes'] if node['Id'] == 'start')
    _woman = 'irabeth' if _base.endswith('irabeth') else 'galfrey'
    _present = _woman + '.present_now'
    _targets = ('passes',) if _woman == 'irabeth' else ('alive', 'queen_back', 'queen_back_priestess', 'queen_back_by_you')
    for _answer in _start['Choices']:
        if _answer.get('Next') in _targets:
            _answer['Requires'] = list(dict.fromkeys([*_answer.get('Requires', []), _present]))
            if _woman == 'irabeth':
                _answer['Requires'].append('crossroute.irabeth.available')
    # Later loss has its own continuation; old choices and targets remain in place.
    _start['Choices'].append(c('Continue', 'absent_now',
        requires=(_woman + '.trickster.returned',), forbids=(_present,)))
    if _woman == 'irabeth':
        _start['Choices'].append(c('Continue', 'absent_now',
            requires=('irabeth_gone',), forbids=(_present, 'irabeth.trickster.returned', 'irabeth_dead')))
    _scene['Nodes'].append(te('absent_now',
        '[PROSE PENDING: ' + _woman + ' currently absent; distinguish any historical return and Iz recollections]',
        c('Continue')))
