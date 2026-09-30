"""Terendelev on the Trickster path: "Restitution in the Wound's blood" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, rewritten
2026-09-29 after the Astra design review r3; it supersedes the scale raise, the Storyteller price and the thief framing of
Writer/handoffs/trickster/terendelev.md, whose canon research and hooks stay valid).

Canon (blueprints.zip / enGB):
- The silver dragon who kept Kenabres. She met the Commander in human shape on the festival square: "My name is
  Terendelev. I am the protector of this city." (WelcomeDialogue/Cue_0039 f5651757; TerendelevHuman 9e8401e7). Her words
  over the wound: "Pry loose the grudging grip of pain..." (Cue_0033 b5032780); "I have not healed you fully. Alas, sooner
  or later your pain will return" (Cue_0058 2e06a430); "You will recover, I promise you that. Tomorrow, come to the
  cathedral..." and "merriment is one of the best medicines" (Cue_0042 92456eff); her dry wit, "Perhaps I should retake my
  true form and engulf this square with my ice breath to win your trust?" (Cue_0056 51db8a3f).
- Areelu: "The dragon was only able to temporarily dull the pain... your wound weeps blood from time to time, every drop
  of which burns your enemies" (Audience_Areelu/Cue_0095 af5d0b6b); "a reflection of the Worldwound... It cannot fully be
  healed until the Worldwound is healed" (Cue_0097 c3cdce20).
- The Storyteller's vision of her corruption and self-purification: black scales (Cue_0769-0772), the cave and her mentor
  Halaseliax (Cue_0779-0782), "her soul... was able to purify herself. For dragons are truly powerful not only in body but
  in spirit" (Cue_0778 71fbdd5c); her voice "in darkness which she cannot escape" (Cue_0785 ca71b79b).
- Iz: "An undead monster created from Terendelev's remains has made its lair nearby" (GalfreyOnTheEdge/Cue_0030 87fdbffb);
  "To grant rest to her soul and her body... is our duty" (Cue_0005 c37c6235); the Queen can fall to "the dragon's
  sorcery" (Cue_0073 a3167386). Her Dragon-path lines (never shown to a Trickster, TerendelevSoul_Actions 601429c7) are
  lore only; here she tells the Deskari part herself, in her own words.
- Silver dragons keep oaths and customs (TerendelevCompanion); she swore to guard the Wardstone (Aeon companion lines).

The device, and what is authored (labelled on the page as the Commander's gamble, never as lore): at the burning bones the
Commander looks for her (Perception; the Storyteller's vision and the claw story, or the Trickster's sight, make it easier).
Found, she asks to be let go. The Commander offers the wound's blood: it burns what belongs to the Abyss (canon, and seen by
the Commander on a dead vrock in the Abyss), so it should burn only what is Deskari's; her spirit once remade her out of
corruption (the Storyteller's vision, or her own telling), and what it lacks now is substance. Nobody knows whether it
makes flesh or another unlife. She is told, and she chooses; claimed, she refuses. The cost stays: the wound, cut open over
her bones, never closes again; she remembers both deaths and cannot take her dragon shape.

Delivery: inline on whichever post-battle dialog plays (Galfrey's, or Irabeth's when the Queen has fallen), a late page for
a Commander who missed, failed or claimed, and her presence in Drezen for the courtship (terendelev_watch).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
REL = "terendelev"
P = "terendelev.trickster."

HUMAN = "9e8401e7703907e4d94189d5992dd13e"         # TerendelevHuman (Prologue): her voice and her body
PORTRAIT_GUID = "d9d0098309a546c6bd8fe825874e50ae"  # BCT_TerendelevHuman, the book-picture fallback
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
TIEFLING = "23eabf5b6364d4a4e86202dc5d27600b"      # Vendor_Tiefling, the lower town (Mielarah stands behind him at 2.5)
TAILOR = "253cdb8f434e5a6469b75e18428316e3"        # TailorCapitalTrader, the fallback (Kaylessa left 2.5, Arueshalae front 2.0)
GALFREY_LIST = "c132e5e4fabc68d49aad76af3f447eb6"   # c5/Iz/GalfreyAfter/AnswersList_0002
GALFREY_RETURN = "4323895e05091eb40a206bcfb1394b6f" # GalfreyAfter/Cue_0028 "...you will have to tolerate me for a little longer."
IRABETH_LIST = "d0905746a5a015949ac39891ab4e5339"   # c5/Iz/IrabethSurvives/AnswersList_0003
IRABETH_RETURN = "2a2a1beb1f22986499798b8e094d46f6" # IrabethSurvives/Cue_0010 "Understood, Commander."
ST_HUB = "2f5b7e0b76d3c5a42a431e1e33a8db09"        # NPC_Common/StoryTeller_MainDialogue/AnswersList_0004
ST_RETURN = "34a0d078b4ac51547a8f5e0e1c8e1e2c"     # StoryTeller_MainDialogue/Cue_0880 "The Storyteller nods, saying nothing."
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"    # CompanionDialogues/Seelah/AnswersList_0003
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"   # NPC_Common/Irabeth/AnswersList_0009
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"    # NPC_Common/Anevia/AnswersList_0003
SCALE = "816f244523b5455a85ae06db452d4330"          # TerendelevScaleItem (never consumed here)
CLAW = "66afc74ef27c7244eac8f8d376cd7947"           # TerendelevClaw (can be handed back, as hers)

STARTED = "terendelev.started"
CLOSED = "terendelev.closed"
COMMITTED = "terendelev.committed"
# Native reads.
IZ_BATTLE = "iz.terendelev_battle"        # SeenCues GalfreyOnTheEdge/Cue_0005: the crusade attacked her ravener with the Commander
LEFT_EARLY = "iz.left_early"              # DidntVisitedEvents: the Queen fought it without the Commander
MONSTER_DEAD = "iz.monster_dead"          # Iz_Default/MonsterDead
MONSTER_LATCH = "iz.monster_dead.latched"
VOICE = "terendelev.voice_heard"          # SeenCues StoryTeller Cue_0785: her voice "in darkness which she cannot escape"
CLAW_STORY = "terendelev.claw_story"      # SeenCues Cue_0778 / Cue_0779: the vision of her self-purification
AREELU_TOLD = "terendelev.areelu_told"    # SeenCues Audience_Areelu/Cue_0095: "only able to temporarily dull the pain"
AEON = "terendelev.aeon_spared"           # TerendelevWasNotKilled (never on Trickster; forbidden everywhere as a guard)
SCALE_HELD = "terendelev.scale_held"
CLAW_HELD = "terendelev.claw_held"
SIGHT = "trickster.perception_tier1"      # TricksterPerceptionTier1Feature: "You see more than other people."
ST_DEAD = "storyteller.dead"
# The parent romance (RanRomance) has already brought her back: its returned-person finale (TereBook05End terminal cues,
# reference/canon-review/terendelev-parent-bindings.json) or the Lich binding that embodies her in service. Only these gate
# the Trickster return; meeting or courting her on the parent route (RanRomTereRom, the oath, the scale) does not.
PARENT_RETURNED = "terendelev.continuation.returned_finale_seen"
PARENT_LICH = "terendelev.parent_lich_bind"
PARENT_EMBODIED = (PARENT_RETURNED, PARENT_LICH)
# Authored.
EYES = P + "eyes"                         # Derived: the claw story heard, or the Trickster's sight
STORY_KNOWN = P + "story_known"           # Derived: the Storyteller's vision of her corruption heard (scale or claw)
DEBT = P + "memory.debt"
VOICE_ASKED = P + "voice.asked"
BLOOD_TESTED = P + "blood_tested"         # the Commander watched the wound's blood burn a dead vrock (Chapter 4)
SCALE_WARMED = P + "scale_warmed"         # ...and a drop of it warm her scale, for a breath
SEARCH_FAILED = P + "search_failed"
REFUSED_CLAIM = P + "refused_claim"
FLINCHED = P + "flinched"
RESTED = P + "rested"                     # the Commander let her go to Pharasma (closes)
RETURNED = P + "returned"
WOUND_OPEN = P + "cost.wound_open"        # the Commander's wound, cut open over her bones, never closes again
GROUNDED = P + "grounded"                 # no dragon shape (lifted on the epilogue page unless cost.late)
BLED_WHITE = P + "cost.bled_white"          # unprepared, the Commander bled past sense into the fire: cold hands for life
LATE = P + "cost.late"                    # the late return: grounded for good
QUEEN_FELL = P + "saw_the_queen_fall"     # she came back in the Irabeth twin, knowing her body killed Galfrey
HUB = "terendelev.presence"
HUB_FB = "terendelev.presence.awning"
HUB_FAILED = HUB + ".failed"
LATE_COMMITTED = P + "late_committed"

BINDINGS = {
    "SeenCues": {IZ_BATTLE: ["c37c6235f1748b144903529f78462c50"],
                 CLAW_STORY: ["71fbdd5c766802f4eac6dfe0612a2d46", "fabb0f4a300ac7b4389c7bee48b07c77"],
                 AREELU_TOLD: ["af5d0b6be337672478f086357442cd15"]},
    "SeenCues_parent": {PARENT_RETURNED: ["8bf0fdc74bae4ef79dcfe04036e813ab", "4791f49d19624dafa2ea1ae6dd18c588",
                                          "30b3341acced4fa793dcc92dfe3587a9", "10fe0c7bd80d441c8688c37babc19f66"]},
    "Etudes": {PARENT_LICH: "bbe7d7dbb92a4923a1ca4433e626a5ec",
               # Q6 r3 (CAN): DeskariKilledInIz (Chapter05_Outcomes); read as a latch source only, recorded below.
               "iz.deskari_killed.live": "047d71e3e928d454bbd168497ee7c17f"},
    "InventoryItems": {CLAW_HELD: CLAW},
    "MainCharacterFacts": {SIGHT: "8bc2f9b88a0cf704ea72d86c2a3e2aef"},
    "Latches": {MONSTER_LATCH: [MONSTER_DEAD + ".live"], "iz.deskari_killed": ["iz.deskari_killed.live"]},   # the raw Iz reader; MONSTER_DEAD is its Derived record (trickster_world)
}

DERIVED = {
    EYES: [[CLAW_STORY], [SIGHT]],
    STORY_KNOWN: [[CLAW_STORY], [VOICE]],
    # R2-6: she has asked what she owes; if the war ends before her watch is agreed, the epilogue carries it.
    LATE_COMMITTED: [["trickster.ever", P + "first_night_seen"]],
    # 05 §2.5 voice note: she joins a household the way she joined Kenabres, by standing a watch over it.
    "terendelev.harem.voice.keeps_the_watch": [[COMMITTED], [LATE_COMMITTED]],
}

RELATIONSHIP = dict(
    Title="Restitution",
    Description=("Terendelev healed me on the festival square in Kenabres, on the day the city fell, and promised "
                 "I would recover. She died before the day was out. Deskari raised what was left of her and set it to guard Iz. The "
                 "crusade came to Iz to give her rest. I mean to find out whether rest is all she has left."),
    Objective="Find out what is left of Terendelev",
    Guidance=("On the Trickster path, after the crusade puts down the monster made from her remains at Iz, go to the "
              "burning bones before you leave the Queen's camp. Hearing the Storyteller's vision of her, or his story of "
              "her corruption, will help you see what is there. If you miss it, the wound will not let you forget."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[AEON], FailureFlags=[],
    TricksterAccess={
        "bones": dict(detect=[IZ_BATTLE], device=P + "bones.restitution", returned=RETURNED),
        "late": dict(detect=[MONSTER_DEAD], device=P + "late.the_wound_calls", returned=RETURNED),
    },
)


def te(id, text, *choices, **kw):
    return n(id, "Terendelev", text, *choices, portrait="Terendelev", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Terendelev", **kw)


def voice(id, text, *choices):
    """Her voice inside a native dialog (E14f: the TerendelevHuman unit's portrait and name)."""
    return n(id, "Terendelev", text, *choices, speaker_unit=HUMAN)


def fire(id, text, *choices):
    """Narration inside a native dialog."""
    return n(id, "Narrator", text, *choices)


def conv(id, text, *choices):
    return n(id, "conversant", text, *choices)


def page(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="visit", owner="Terendelev", **extra):
    SCENES.append(scene(id, title, owner, min(chapters), "", nodes,
                        requires=tuple(dict.fromkeys(requires)), forbids=tuple(dict.fromkeys((AEON, *forbids))),
                        delay=delay, last=max(chapters), Relationship=REL, Chapters=list(chapters), Remote=True, Kind=kind,
                        **extra))


# --- Chapter 3 (a memory): what she promised on the square --------------------------------------------------------------

page(P + "memory.square", "What she promised", [
    nar("start", '''{n}Drezen after midnight: the sentries calling the hour along the walls, a dog barking somewhere in the lower town, and in your quarters a single candle burned down almost to the dish. You have tipped your pack out onto the table to find a whetstone.{/n}''',
        c("Continue", "scale", requires=(SCALE_HELD,)),
        c("Continue", "no_scale", forbids=(SCALE_HELD,))),
    nar("scale", '''{n}Among the rations and the maps lies a silver scale the size of your palm. Terendelev's. It has ridden at the bottom of your pack since Kenabres, through the caves and the siege and everything since. It has never tarnished. It has never once been warm, however long you hold it.{/n}''',
        c("[Turn it over in your fingers.]", "square")),
    nar("no_scale", '''{n}At the bottom of the pack, among the rations and the maps, there is a flat clean space the shape of something that used to ride there. Terendelev's scale. It was spent, the way such things are meant to be spent, on someone who needed it more than a keepsake. The pack has not quite forgotten it.{/n}''',
        c("[Put your hand in the empty place.]", "square")),
    nar("square", '''{n}You remember the festival square in Kenabres: bunting, the smell of fried dough, cobbles hard under your back and a hole in you that would not stop. An old prelate praying over you, and failing. Then a woman bending into your sight, silver-haired and unlined, with a sadness in her eyes older than the city around her.{/n}
{n}"Pry loose the grudging grip of pain," she said, and the pain went where it was told.{/n}''',
        c("[Remember what she said after.]", "promise")),
    nar("promise", '''{n}"You will recover, I promise you that. Tomorrow, come to the cathedral and say that you are expected by Terendelev, protector of Kenabres."{/n}
{n}There was no tomorrow in Kenabres. Later that same day the ground opened and Deskari came up out of it, and she went up to meet him, and she did not come down. You never went to the cathedral. There was nobody left there to expect you.{/n}''',
        c('"I still haven\'t been to the cathedral."', "end", flags=(DEBT,)),
        c('[Raise the candle to her, like a cup] "Merriment is one of the best medicines. You said so."', "end", flags=(DEBT,)),
        c("[Say nothing. Pack the bag again.]", "end")),
    nar("end", '''{n}The candle gutters and goes out. In the dark the wound aches, dull and patient, the way it has ached every night since the square: the pain she pried loose, come back, exactly as she warned you it would.{/n}
{n}She kept every other promise she made that day. She kept the city until it killed her.{/n}''',
        c("[Lie down. Sleep, if it comes.]")),
], requires=("trickster",), forbids=(P + "memory.square", MONSTER_DEAD), delay=24, chapters=(3,), kind="memory", Areas=[DREZEN],
    owner="Memory")


# --- Chapters 3 to 5 (the Storyteller's hub): where the voice is kept ---------------------------------------------------
# After his native vision (Cue_0785). Only a conversation: he is no party to anything, and nothing is bought.

SCENES.append(scene(P + "voice.where", "Somewhere she cannot leave", "Storyteller", 3,
    '"You said you hear Terendelev\'s voice in your visions. Tell me about that darkness."', [
    conv("start", '''{n}The Storyteller's blind eyes drift toward your voice and past it, as though you were standing a little to one side of yourself.{/n} "Darkness is the wrong word, and it is the only one I have. When I tell a story, I stand where the teller stood. When I reach for her, there is nowhere to stand. There is only the voice. And it is... kept. The way a thing is kept in a box."''',
        c('"Kept where?"', "where"),
        c('"Is she in pain?"', "pain")),
    conv("where", '''"I do not know, child. I am not a finder of lost things; I am a teller of them." {n}He turns his cup a quarter-turn on the table, the way a man adjusts a lamp.{/n} "But I know this much. The Lady of Graves keeps very tidy books. A soul that has not come before her to be judged is a soul that something is holding on to. The dead do not linger by accident. Somebody wants them where they are."''',
        c("Continue", "ask")),
    conv("pain", '''"Yes." {n}He says it simply.{/n} "And under the pain something I like less. Shame. She sounds like someone who has been made to do a thing she would have died rather than do, except that she has already died, and so she was not given the choice." {n}His hand tightens on the cup.{/n} "I have heard a great many dead people, Commander. I have not often heard one ashamed."''',
        c("Continue", "ask")),
    conv("ask", '''"You ask like someone who means to do something about it. May I ask why? Terendelev had a great many admirers. I do not recall that you were one of them."''',
        c('"She healed me in the festival square, the day Kenabres fell. She promised I\'d recover."', "square", flags=(VOICE_ASKED,)),
        c('[Trust your intuition] "If someone is holding on to her, then she can be taken off them."', "held", flags=(VOICE_ASKED,),
          mythic="Trickster"),
        c('"No reason. Curiosity."', "curious")),
    conv("square", '''"Ah." {n}Something eases in his face.{/n} "Then you are the wounded crusader. I heard of it, afterwards: the dragon who stopped in the middle of the festival to kneel on the cobbles over a stranger. People told it as a small kindness before a great horror. The small kindnesses are always the first thing to be forgotten." {n}He smiles, crookedly.{/n} "I should not have guessed you were the sort to remember them."''',
        c("Continue", "end")),
    conv("held", '''{n}The old elf is quiet. Then he laughs, low, and has to put the cup down.{/n} "Taken off them. Of all the people in this citadel, you are the only one who would hear a soul in torment and think of it as a lock rather than a grave." {n}The laugh fades.{/n} "Be careful. Whoever holds her will not want to let her go, and she may not want to be carried."''',
        c("Continue", "end")),
    conv("curious", '''"Curiosity." {n}He tilts his head, listening to something that is not your voice.{/n} "I have lived a long time on other people's curiosity, Commander. I know what it sounds like. That was not it."''',
        c("Continue", "end")),
    conv("end", '''"If I hear her more clearly, I will tell you. And if you find her before I do..." {n}He hesitates, which the Storyteller rarely does.{/n} "Tell her someone was listening. It is a poor comfort. It is the one I have."''',
        c("[Leave him to his cup.]")),
], requires=("trickster", VOICE), forbids=(VOICE_ASKED, RETURNED, MONSTER_DEAD, ST_DEAD, AEON), last=5, Relationship=REL,
    Chapters=[3, 4, 5], AnswerLists=[ST_HUB], NativeReturnCue=ST_RETURN))


# --- Chapter 4 (a page, in the Abyss): what the wound weeps --------------------------------------------------------------
# The planted preparation: the Commander tests what the wound's blood does before trusting it with anything that matters.

page(P + "wound.weeps", "What the wound weeps", [
    nar("start", '''{n}The Abyss has no night, only a dimmer red. You wake in it with your shirt stuck to your side. The wound is weeping again.{/n}
{n}It has done this since Kenabres: a thin, slow bleed that comes and goes for no reason any healer has found, and stops when it pleases. Tonight there is more of it than usual. Where it has dripped onto the stone beside your bedroll there are small bright scorch marks, as if someone had flicked coals.{/n}''',
        c("Continue", "areelu", requires=(AREELU_TOLD,)),
        c("Continue", "plain", forbids=(AREELU_TOLD,))),
    nar("areelu", '''{n}You remember Areelu in Nocticula's audience hall, calm as a lecturer. The dragon was only able to temporarily dull the pain. Your wound weeps blood from time to time, every drop of which burns your enemies. It cannot fully be healed until the Worldwound is healed.{/n}
{n}So that is what Terendelev gave you on the square: not a cure. A few good nights, and her best try. She knelt on the cobbles and did everything she had, and it was not enough, and she promised you anyway.{/n}''',
        c("Continue", "test")),
    nar("plain", '''{n}The healers in Drezen gave up on it in the first month. The priests in the Abyss do not try. You have learned to live with the wound the way you live with the weather, and it occurs to you, lying in the red half-dark, that you have never once asked it what it actually does.{/n}''',
        c("Continue", "test")),
    nar("test", '''{n}You are not a physician. You are, however, someone who likes to know exactly what a tool will do before trusting it with anything that matters. At the edge of the camp lies the vrock your sentries killed at the last watch, its feathers already going to slime.{/n}''',
        c("[Catch a drop on your knife and lay it on the vrock's hide.]", "vrock", flags=(BLOOD_TESTED,)),
        c("[Bind the wound and go back to sleep.]", "sleep")),
    nar("vrock", '''{n}The drop hisses. It eats a hole the size of a coin through the hide and goes on eating, down into the meat, until there is a smoking pit you could put your thumb in. The smell is appalling.{/n}
{n}You try it on the flat of your own blade: nothing. On a strip of clean linen: only blood. On the dust of the Abyss itself, it smokes, faintly, like a candle just blown out.{/n}
{n}It burns what belongs to the enemy, then, and leaves alone what does not. You try it on a camp rat the dogs killed: the rat stays a dead rat. It does not mend, or make, or raise. Whatever the wound's blood is for, it is for taking things away.{/n}
{n}One dead vrock, one rat, one knife and a scrap of linen. A careful person would want more than that. A careful person also writes it down.{/n}''',
        c("Continue", "scale_choice", requires=(SCALE_HELD,)),
        c("Continue", "sleep", forbids=(SCALE_HELD,))),
    nar("scale_choice", '''{n}Her scale is in the bottom of your pack, where it always is. You could not say why you think of it now. Perhaps only because it is the one thing you carry that came from someone who tried to heal you.{/n}''',
        c("[Touch a drop of the blood to her scale.]", "scale", flags=(SCALE_WARMED,)),
        c("[Leave the scale where it is.]", "sleep")),
    nar("scale", '''{n}Nothing happens.{/n}
{n}Then, and you will swear to this afterwards, while also admitting that you had been awake for thirty hours, the scale is warm. Not hot. Warm, the way a hand is warm when it has just come out of a glove. It lasts as long as a breath. Then it is only a scale again, cold as it has been since Kenabres, with a rust-brown smear on it that you wipe away with your thumb.{/n}''',
        c('"Terendelev?"', "silence")),
    nar("silence", '''{n}Nothing answers. The Abyss mutters to itself beyond the pickets. Somewhere a sentry coughs.{/n}
{n}You wrap the scale again and put it back at the bottom of the pack, and you lie awake a long while afterwards, not thinking about it with great care.{/n}''',
        c("[Bind the wound.]")),
    nar("sleep", '''{n}You bind the wound. By morning the bleeding has stopped of its own accord, as it always does, and you ride on into the red.{/n}''',
        c("[Break camp.]")),
], requires=("trickster",), forbids=(P + "wound.weeps", RETURNED, MONSTER_DEAD), delay=24, chapters=(4,), kind="event",
    owner="Commander")


# --- Chapter 5 (the device, inline at Iz): restitution in the Wound's blood ----------------------------------------------
# Exactly one of the two post-battle dialogs plays: GalfreyAfter if the Queen lives, IrabethSurvives if she fell. The same
# scene is hosted on each; each twin forbids the other. The host speaks as the dialog's conversant.

PERCEPTION = (
    c("[Perception DC 20] Look into the fire the way you have looked at things since the path took you: for what is there, "
      "not for what is burning.", requires=(EYES,),
      check=dict(Skill="SkillPerception", DC=20, Success="found", Failure="failed", CommanderOnly=True)),
    c("[Perception DC 24] Look for her in the fire. The Storyteller said she was somewhere she could not leave.",
      requires=(VOICE,), forbids=(EYES,),
      check=dict(Skill="SkillPerception", DC=24, Success="found", Failure="failed", CommanderOnly=True)),
    c("[Perception DC 30] Look for her in the fire.", forbids=(EYES, VOICE),
      check=dict(Skill="SkillPerception", DC=30, Success="found", Failure="failed", CommanderOnly=True)),
    c("[Leave the fire to burn.]", abort=True),
)

HOSTS = {
    "galfrey": dict(
        list=GALFREY_LIST, back=GALFREY_RETURN, suffix="",
        watch='''{n}Galfrey follows your gaze. She has not sheathed her sword; she leans on it, as she leaned on it through the fight.{/n} "She sheltered Kenabres for longer than I have worn a crown. We gave her the only mercy we had to give." {n}Her jaw sets.{/n} "Let it burn, Commander. It is her pyre now."''',
        fail_line='''{n}Galfrey's hand comes to rest on your shoulder, briefly, the way a commander touches a soldier who has stood too long at a grave.{/n} "There is nothing of her left in that. Come away."''',
        fail_exit='"She deserved better than this, Your Majesty. So did all of Kenabres."',
        claim_line='''{n}Galfrey has been watching you, not the fire. Whatever she heard, she keeps it behind her face.{/n} "Commander. Whatever you were speaking to, I pray it was only grief."''',
        claim_exit='"Only grief, Your Majesty."',
        rest_line='''{n}When you turn from the fire at last, Galfrey is still there, bareheaded. She does not ask what you were saying to the bones. She only inclines her head to them, the way a queen salutes a fallen ally.{/n}''',
        rest_exit='"She\'s gone, Your Majesty. For good, this time."',
        see='''{n}Galfrey has come as near as the heat allows, her sword up and not quite raised. She looks at the blood on the ash, and at you, and then at the woman in the ribcage, and her voice goes very quiet.{/n} "Goddess preserve us. Commander, I came to this city to give her rest. Tell me that was not a blasphemy." {n}And then, differently:{/n} "...Lady Terendelev?"''',
        answer='''"Your Majesty." {n}Terendelev's voice is hoarse, but it is hers.{/n} "You came to put me down. You were right to. Thank you for it."''',
        exit='"She\'s alive, Your Majesty. Take it up with me, not with her."',
        queen=False),
    "irabeth": dict(
        list=IRABETH_LIST, back=IRABETH_RETURN, suffix="_irabeth",
        watch='''{n}Irabeth comes to stand at your shoulder. Her eyes go to the fire and away, and come back to it against her will.{/n} "I served on the walls of Kenabres. When she flew over, the whole garrison went quiet." {n}Her voice drops.{/n} "The Queen went at it first. She would not let anyone else take the front."''',
        fail_line='''{n}Irabeth says your name, then your rank, the way she would call a sentry who has stopped answering.{/n} "Commander. There's nothing in there. We should go."''',
        fail_exit='"Mark this place, knight. I may come back to it."',
        claim_line='''{n}Irabeth has not taken her eyes off you. Whatever she heard, she does not want to have heard it.{/n} "Commander... who were you talking to?"''',
        claim_exit='"No one, knight. Get the column ready to move."',
        rest_line='''{n}When you turn from the fire at last, Irabeth is standing a few paces off with her helm under her arm. She makes the sign of the Inheritor toward the bones, stiffly, and then does not seem to know what to do with her hand.{/n}''',
        rest_exit='"Get the column ready, knight. We\'re done here."',
        see='''{n}Irabeth has her blade out and no idea where to point it. She looks at the blood on the ash, and at you, and at the woman in the ribcage.{/n} "That's... Commander, that's her voice. I heard it from the walls every festival." {n}She swallows hard, and then, because she is Irabeth, she finds her feet.{/n} "What are your orders?"''',
        answer='''{n}Terendelev looks at the knight, and past her at the field, where the Queen's banner lies on the stones, and she knows. You watch her know it.{/n} "The Queen." {n}Her voice cracks.{/n} "I felt her fall. My claws. My sorcery. I am so sorry, child. I do not ask you to forgive it."''',
        exit='"Find her a cloak and a horse, knight. And not a word to anyone until we\'re clear of Iz."',
        queen=True),
}


def bones(host):
    h = HOSTS[host]
    sid = P + "bones.restitution" + h["suffix"]
    twin = P + "bones.restitution" + ("_irabeth" if host == "galfrey" else "")
    returned = (RETURNED, STARTED, WOUND_OPEN, GROUNDED) + ((QUEEN_FELL,) if h["queen"] else ())
    nodes = [
        fire("start", '''{n}What is left of the ravener lies where it fell across the rubble of a Sarkorian square: a dragon's skeleton, long as a street, burning. It is not an ordinary fire. It has nothing to feed on but the bones, and it does not spread, and it does not die down. The knights give it a wide berth and pretend not to look at it.{/n}
{n}It was Terendelev. Your arms still ache from the putting down of it.{/n}''',
             c("Continue", "host")),
        conv("host", h["watch"], *PERCEPTION),
        fire("failed", '''{n}You look until your eyes run and the heat drives you back a step, and then another. It is fire and bone and nothing else. If anything of her is still in there, it does not know you, or you do not know how to see it.{/n}''',
             c("Continue", "failed_host")),
        conv("failed_host", h["fail_line"], c(h["fail_exit"], flags=(SEARCH_FAILED,))),
        fire("found", '''{n}You look until the heat makes your eyes run, and then you keep looking.{/n}
{n}There. Not in the flames: between them. The fire moves the way fire moves, except in one place, at the heart of the skull, where it moves the way a sleeper breathes. Slow. Stubborn. Something in there has not gone where the dead go.{/n}''',
             c("Continue", "scale", requires=(SCALE_HELD,)),
             c("Continue", "call", forbids=(SCALE_HELD,))),
        fire("scale", '''{n}In your pack, against your spine, something has gone warm.{/n}''',
             c("Continue", "call")),
        fire("call", '''{n}You go to the edge of the fire, close enough that the hair on your forearms crisps.{/n}''',
             c('"Terendelev. I know you\'re still in there."', "voice"),
             c('[Say it the way she said it on the square, as a title] "Terendelev. Protector of Kenabres."', "voice")),
        voice("voice", '''{n}The fire leans toward you. A voice comes out of it that has no throat to come from, hoarse with smoke and very tired, and you know it at once.{/n} "Who calls me that? There is no Kenabres. There is only this place, and the task, and the dark between."''',
              c('"The crusader from the festival square. The one you healed."', "knows"),
              c('"The one who just put you down. Again."', "knows_hard")),
        voice("knows_hard", '''"Yes. I felt you. I felt every one of you, and I could not stop." {n}The fire shudders the whole length of the spine.{/n} "You fought like the wounded one from the square. The stranger on the cobbles. Is it you?"''',
              c('"It\'s me."', "knows")),
        voice("knows", '''{n}A long, rasping silence.{/n} "The wounded one. I told you to come to the cathedral." {n}Something in the fire almost laughs.{/n} "You did not come. I suppose I cannot hold that against you. There was no cathedral by morning."''',
              c("Continue", "task")),
        voice("task", '''"He raised me. The Lord of Locusts. He took what was left of me off the stones of Kenabres and made it walk, and made it hunt, and set it here to keep your kind out of his city. He promised me peace when the task was done." {n}The voice hardens, and breaks.{/n} "I killed crusaders for that promise. I think I killed friends. He is in this city still, or his stink is. I could feel him the way you feel a draught."''',
              c('"That wasn\'t you. That was his thing, wearing your bones."', "want"),
              c('"You did. And now it\'s over."', "want")),
        voice("want", '''"Then let me go. Leave me, or end it; I no longer care which. I am so tired of the dark." {n}The slow breathing at the heart of the skull falters.{/n} "Why are you still standing there, wounded one? What can you want with a heap of burning bones?"''',
              c('"I want you to come back."', "offer"),
              c('[Tell her she\'s yours now] "I killed what held you. That makes you mine."', "claimed", flags=(REFUSED_CLAIM,)),
              c('[Let her rest] "Nothing. Go where you\'re going. You\'ve earned it."', "rest", flags=(RESTED, CLOSED))),
        voice("claimed", '''"Yours." {n}The fire goes flat and blue for an instant, like a coal under a bellows run backwards.{/n} "He called me his, too. He said it very often. I have been owned, crusader, and I have had enough of it for any life I might be given." {n}The breathing in the skull slows until you cannot find it.{/n} "Whatever you are, you will not be that. Go away."''',
              c("Continue", "claimed_host")),
        conv("claimed_host", h["claim_line"], c(h["claim_exit"])),
        voice("rest", '''"Thank you." {n}It is hardly a voice any more.{/n} "Do not tell Kenabres. Let them remember the square, and the flying, and not this." {n}The fire at the heart of the skull stops breathing, and is only fire.{/n}''',
              c("[Stand with the bones until the fire burns low.]", "rest_host")),
        conv("rest_host", h["rest_line"], c(h["rest_exit"])),
        voice("offer", '''"Come back." {n}Something that might once have been a laugh.{/n} "Into what? That body is the thing you have just killed, and I would not wear it again if the Inheritor herself held the door. I have been made foul before, wounded one. Long ago the Wound had me black to the heart, and I shut myself in a cave and burned it out of my own spirit until I could look at the sun. It very nearly finished me. I have nothing left to burn with. I have no body at all."''',
              c('"You remade yourself once, out of nothing but your own spirit. The spirit\'s still here. What\'s missing is the rest of you."', "pitch"),
              c('"The Storyteller saw that cave. He says a dragon is as strong in spirit as in body. I\'m counting on it."', "pitch",
                requires=(STORY_KNOWN,))),
        fire("pitch", '''{n}You crouch at the edge of the fire, close enough that your brows singe, and you tell her what you have. A wound that has never closed. Blood that burns what belongs to the Abyss.{/n}''',
             c("Continue", "pitch_vrock", requires=(BLOOD_TESTED,)),
             c("Continue", "pitch_guess", forbids=(BLOOD_TESTED,))),
        fire("pitch_vrock", '''{n}You know what it does, because you tested it in the Abyss before you trusted it with anything: a coin-sized pit eaten through a dead vrock's hide; your own blade and a strip of clean linen left untouched. It burns what is the enemy's. It makes nothing. Whatever it leaves, something else has to shape.{/n}''',
             c("Continue", "pitch_scale", requires=(SCALE_WARMED,)),
             c("Continue", "pitch_plan", forbids=(SCALE_WARMED,))),
        fire("pitch_scale", '''{n}And a drop of it on her scale, once, made the scale warm for the length of a breath. You told yourself you had been awake too long. You have carried that scale against your spine every day since, and it is warm now.{/n}''',
             c("Continue", "pitch_plan")),
        fire("pitch_plan", '''{n}No priest would bless it. But it is a plan and not a hope: a burn that knows its enemy, a spirit that has remade itself once, and the one thing she lacks, which you have in you.{/n}''',
             c("Continue", "hook")),
        fire("pitch_guess", '''{n}So say the scorch marks on your sheets, and the healers in Drezen, who stopped touching your dressings bare-handed. You never tested it. You do not know how fast it burns, or how much of it a fire would take. It is a guess, and you know it is a guess.{/n}''',
             c("Continue", "hook")),
        voice("hook", '''"And what would you do with it?" {n}The voice is flat with exhaustion.{/n} "Bleed on a pyre, and hope?"''',
              c('[Trust your intuition] "He holds you by what he put into you: his purpose, grown into your bones. That is his, and my blood burns what\'s his. Burn the hook out of you, and what\'s left of you can do the rest."', "risk",
                mythic="Trickster"),
              c('"My blood for a body. If it burns what\'s his, whatever it leaves is yours. Make something of it."', "risk")),
        voice("risk", '''"And if it does not stop at what is his?" {n}The fire is very still.{/n} "If it burns me too, then I was his all through, and I would rather know it. And if it does not, you would be giving me flesh out of a wound the Abyss put in you. I might come out of that fire living. I might come out of it as another thing like the one you killed, with your blood in it instead of his."''',
              c('"I can\'t know. I\'m asking anyway."', "choose"),
              c('"I would rather gamble with you than leave you here."', "choose")),
        voice("choose", '''"Asking." {n}She turns the word over.{/n} "He never asked. He took." {n}The breathing at the heart of the skull quickens, a little.{/n} "Very well. Open your wound, crusader. I will do the rest, or I will not."''',
              c("[Open the wound over the bones.]", "cut", mythic="Trickster"),
              c('[Lower the knife] "...Not like this. Not today."', "flinch", flags=(FLINCHED,))),
        voice("flinch", '''"No." {n}There is no anger in it; only something very tired, and very gentle.{/n} "No, I did not think so. It is a great deal to ask of anyone, and you have asked it of yourself." {n}The breathing slows.{/n} "Go on, then. I have waited in the dark before."''',
              c("Continue", "flinch_host")),
        conv("flinch_host", h["fail_line"], c(h["fail_exit"])),
        fire("cut", '''{n}You take out your knife. The wound has never closed; it has only ever been persuaded to stop. You unpersuade it. The blade goes in along the old seam, and the pain that Terendelev once pried loose comes back all at once, as though it had been waiting at the door.{/n}
{n}You go down on your knees at the edge of the pyre and lean out over it, the cut side down, and let the blood run out from under your ribs into the fire.{/n}''',
             c("Continue", "measured", requires=(BLOOD_TESTED,)),
             c("Continue", "unmeasured", forbids=(BLOOD_TESTED,))),
        fire("measured", '''{n}You watched the vrock's hide in the Abyss and you know how fast it burns. So you count. You give the bones what they need to burn clean and not a drop more, and you keep your other hand pressed hard below the cut, the way a field surgeon taught you, so the blood goes where you send it.{/n}''',
             c("Continue", "burn")),
        fire("unmeasured", '''{n}You have no idea how much it will take. The fire drinks and drinks. Your sight begins to grey at the edges, and the knights behind you have started to shout.{/n}''',
             c("[Knowledge (Arcana) DC 24] Watch the flames and stop at the moment the fire has what it needs.",
               check=dict(Skill="SkillKnowledgeArcana", DC=24, Success="burn", Failure="too_long", CommanderOnly=True)),
             c("[Athletics DC 24] Stay on your feet and keep bleeding until it is done, whatever it takes.",
               check=dict(Skill="SkillAthletics", DC=24, Success="burn", Failure="too_long", CommanderOnly=True))),
        fire("too_long", '''{n}You bleed past sense. The fire takes more than it needs, a great deal more, and you do not know it until your knees hit the rubble and the stones come up to meet your cheek. Somebody is holding your arm up out of the flames. Somebody is swearing. The last thing you see before the grey closes is the fire at the heart of the skull, drinking.{/n}
{n}You never quite get that blood back. For the rest of your life your hands are cold in winter, whatever the fire.{/n}''',
             c("Continue", "burn", flags=(BLED_WHITE,))),
        fire("burn", '''{n}Where it strikes the bones, it burns: white and furious, the way it burns everything that belongs to the Abyss. The ravener's blackened ribs crack and blister. Something shrieks in the marrow that is not her, and burns, and is gone.{/n}
{n}Where it strikes the slow breathing at the heart of the skull, it does not burn. It is taken.{/n}''',
             c("Continue", "shape")),
        fire("shape", '''{n}You bleed for longer than is sensible. Your sight goes grey at the edges. The fire gathers the blood the way a hand gathers water, and draws it inward, and then the fire is no longer burning the bones. It is burning around something.{/n}
{n}Inside the ribcage of the dragon she used to be, a shape sits up in the ash. Long limbs. Hair dark with blood to the scalp, and silver under it. A woman's back, bent double, coughing.{/n}''',
             c("Continue", "born")),
        voice("born", '''{n}She turns her head. Her eyes are the grey of her scale. She is naked and filthy and shaking, and there is a cut along the heel of her hand where she pushed herself up off a splintered rib. It is bleeding. Red. Ordinary red.{/n} "I am cold," {n}Terendelev says, in pure astonishment.{/n} "Wounded one. I am cold. I am bleeding."''',
              c("[Put your cloak around her.]", "warm"),
              c("[Take her bleeding hand.]", "warm")),
        voice("warm", '''{n}She is warm under your hands: not the dry heat of the fire, but the warmth of a body with blood moving in it. Some of it is yours. Her eyes go to your side, where the wound is still running freely and has no intention of stopping.{/n} "You are still open. You opened it for me and it has not shut." {n}Her fingers find it, and she says the old words from the square, and the pain goes quiet. The bleeding slows. It does not stop.{/n} "It will not close," she says softly. "I can feel that it never will. What have you done to yourself?"''',
              c('"Made a trade. A good one."', "bones_left"),
              c('"Don\'t. It was worth it."', "bones_left")),
        voice("bones_left", '''{n}She looks past you at the ribcage she sat up in, at the blackened skull, at the long spine going away across the rubble with the white fire still crawling along it.{/n} "Do not let them make relics of those. The crusade loves a relic. They will want a rib for a cathedral and a claw for the Queen's chapel and a tooth for every knight who fought here." {n}Her voice hardens.{/n} "He wore those. Let them burn down to nothing, and scatter what is left, and let nobody pray over it."''',
              c('"They\'ll burn. I\'ll see to it."', "shift"),
              c('"Nobody will touch them. You have my word."', "shift")),
        fire("shift", '''{n}Then she tries. You see her do it: the long breath, the gathering inward, the thing every dragon does without thinking. Nothing comes of it. She is a woman sitting in the ash, and a woman she stays.{/n}''',
             c("Continue", "wings")),
        voice("wings", '''{n}She looks down at the bones she came out of.{/n} "My wings are in that fire." {n}Then, with a ghost of the voice that once offered to breathe ice across a festival square to win a stranger's trust:{/n} "Well. I came out of it, and they did not. I will take that bargain for now."''',
              c("Continue", "see")),
        conv("see", h["see"], c("Continue", "answer")),
        voice("answer", h["answer"], c(h["exit"], flags=returned)),
    ]
    SCENES.append(scene(sid, "Restitution", "Terendelev", 5, "[Walk over to the burning bones.]", nodes,
                        requires=("trickster", IZ_BATTLE),
                        forbids=(RETURNED, SEARCH_FAILED, REFUSED_CLAIM, FLINCHED, CLOSED, AEON, twin, *PARENT_EMBODIED),
                        last=5, Relationship=REL, Chapters=[5], AnswerLists=[h["list"]], NativeReturnCue=h["back"],
                        TricksterDevice=True, TricksterState="bones"))


bones("galfrey")
bones("irabeth")


# --- Chapter 5 (a page): the late return -------------------------------------------------------------------------------
# For a Commander who was not at the bones (the Queen fought it alone), missed her in the fire, claimed her, lost nerve, or
# simply walked past. Dearer: the fire has burned lower while she waited, and what it took with it does not come back.

page(P + "late.the_wound_calls", "The fire at Iz", [
    nar("start", '''{n}The wound opens by itself, three nights after Iz. There is no knife in it and no blow; you wake with the bed soaked and the bleeding running faster than it has since Kenabres, and it does not slow for bandages or prayers until nearly morning.{/n}
{n}You lie in the grey light and think about the fire.{/n}''',
        c("Continue", "absent", requires=(LEFT_EARLY,)),
        c("Continue", "failed", requires=(SEARCH_FAILED,), forbids=(LEFT_EARLY,)),
        c("Continue", "claimed", requires=(REFUSED_CLAIM,), forbids=(LEFT_EARLY, SEARCH_FAILED)),
        c("Continue", "flinched", requires=(FLINCHED,), forbids=(LEFT_EARLY, SEARCH_FAILED, REFUSED_CLAIM)),
        c("Continue", "passed", forbids=(LEFT_EARLY, SEARCH_FAILED, REFUSED_CLAIM, FLINCHED))),
    nar("absent", '''{n}You were not there. The Queen's knights put the ravener down without you, and the report that came back said only that the bones were still burning when the column marched, and that nobody had liked to go near them.{/n}
{n}Nobody had gone near them. Nobody had looked.{/n}''',
        c("Continue", "absent_queen", requires=("galfrey.dead",)),
        c("Continue", "ride", forbids=("galfrey.dead",))),
    nar("absent_queen", '''{n}And the Queen had died there. Her knights went back to Mendev with her body on a cart and would not say how, not to you. You have been thinking about that, too: about what it would mean to bring back the dragon whose bones were burning on the field where Galfrey fell, and whether you have the right, and whether you have the right not to.{/n}''',
        c("Continue", "ride")),
    nar("failed", '''{n}You looked into that fire and saw nothing, and turned away. You have been seeing it every night since: the one place at the heart of the skull where the flames did not move quite like flames. You did not see it then. You have not been able to stop seeing it now.{/n}''',
        c("Continue", "ride")),
    nar("claimed", '''{n}She told you she had been owned once and would not be owned again, and then she hid from you in her own fire. She was right. You have been composing a better sentence ever since.{/n}''',
        c("Continue", "ride")),
    nar("flinched", '''{n}You held the knife over the wound and could not do it. She did not blame you. That was the worst of it.{/n}''',
        c("Continue", "ride")),
    nar("passed", '''{n}You walked past that fire at Iz with the rest of the column. You told yourself it was a pyre. You have been walking past it every night since.{/n}''',
        c("Continue", "ride")),
    nar("ride", '''{n}It is days back to Iz with a handful of riders who have learned not to ask you questions. The city is quieter now; the thing that ruled it is gone, and what it left behind is only ruins and flies.{/n}
{n}The bones are still burning. Lower now: a long bed of white ash with the skull lying in it like a stone in a stream, and a small, stubborn flame at the heart of it that has not gone out.{/n}''',
        c("[Go to the skull.]", "voice")),
    te("voice", '''{n}This time you do not need to look. Whatever breathes in the skull breathes very slowly, and it has been listening for hoofbeats.{/n} "Someone came." {n}The voice is thinner than smoke.{/n} "Nobody comes to a pyre once it is lit. It is not done. Who are you, and what do you want?"''',
        c('"The wounded one from the festival square. You healed me, the day Kenabres fell. I\'ve come to ask you to come back."', "ask",
          requires=(LEFT_EARLY,)),
        c('"The one who tried to claim you. I\'ve come to ask properly, this time."', "ask", requires=(REFUSED_CLAIM,), forbids=(LEFT_EARLY,)),
        c('"The one who lost nerve. I\'ve come to finish it, if you\'ll still have it."', "ask", requires=(FLINCHED,),
          forbids=(LEFT_EARLY, REFUSED_CLAIM)),
        c('"The wounded one from the square. I walked away from this fire once. I\'ve come back to ask you to come back."', "ask",
          forbids=(LEFT_EARLY, REFUSED_CLAIM, FLINCHED))),
    te("ask", '''"Come back." {n}A breath that might have been a laugh, once.{/n} "Into what? The body he made is ash. I have been made foul before, long ago; I shut myself in a cave and burned the Wound out of my own spirit until I could look at the sun again. I have nothing left to burn with now, and less of me to burn than there was three days ago. The fire takes a little every hour."''',
        c('"Then take something from me instead."', "gamble")),
    nar("gamble", '''{n}You tell her what you have. A wound that has never closed, and is open now. Blood that burns what belongs to the Abyss and leaves other things alone. Her own spirit, which has done this once already with nothing to work in but itself. It is a guess, and you tell her it is a guess.{/n}''',
        c("Continue", "risk")),
    te("risk", '''"And if it makes me another thing like the one you killed? Or burns me with the rest of his?" {n}The flame is very small.{/n} "And there is less of me than there was. Whatever comes out of this fire now will be less than what went in. I think the wings are gone already. I felt them go, the second night."''',
        c('"Less of you is still you. I\'m asking."', "choose"),
        c('[Let her rest] "Then rest. I won\'t make you."', "rest", flags=(RESTED, CLOSED))),
    te("choose", '''"Asking. Yes. You are." {n}The flame gathers itself.{/n} "Very well, wounded one. I have been cold for three days, listening for you. Open it."''',
        c("[Open the wound over the ash.]", "cut", mythic="Trickster")),
    nar("cut", '''{n}The wound is already open. You open it further, and kneel over the ash with the cut side down, and the blood runs out from under your ribs onto it, and where it finds what is left of the ravener it burns white, and where it finds the small flame at the heart of the skull, the flame drinks.{/n}
{n}It takes longer than you would have liked. You are on your knees in the ash by the end of it, and a woman is on her knees in front of you, naked and grey with cinders, holding your hand in both of hers as though it were the only warm thing in the world.{/n}''',
        c("Continue", "after")),
    te("after", '''"Cold," {n}she says, amazed, and then, looking at the blood on her own palm where the ash has cut it:{/n} "Red." {n}She tries to gather herself inward, the way a dragon does, and nothing comes; she does not seem surprised. She only looks at the ash where the wings would have been.{/n} "They are gone. I knew they would be. It does not matter. I have hands. Give me your cloak, and let us leave this place before it remembers us."''',
        c('[Wrap her in your cloak.] "Let\'s go home."', flags=(RETURNED, STARTED, WOUND_OPEN, GROUNDED, LATE))),
    te("rest", '''"Thank you." {n}The flame gutters.{/n} "You came back. That will do. Tell no one in Kenabres; let them remember the square."''',
        c("[Stay until it goes out.]")),
], requires=("trickster", MONSTER_DEAD, MONSTER_LATCH), forbids=(RETURNED, CLOSED, *PARENT_EMBODIED), delay=24,
    TricksterDevice=True, TricksterState="late")


# --- Reactions: companions and NPCs with a real stake in her ------------------------------------------------------------

SCENES.append(reaction("Seelah", P + "react.seelah.watch", (P + "night.seen",),
    '''{n}Seelah is sitting on the edge of the practice ring with a whetstone she is not using.{/n} "So. The north turret." {n}She grins, then doesn't.{/n} "My first festival in Kenabres, when I was still new to the order. Old habits: I caught my own hand halfway into a merchant's purse, and when I looked round she was standing right behind me in her human shape. She didn't call the watch. She asked whether the Inheritor paid her paladins so badly, and when I said yes, she laughed like bells and bought me a pie." {n}She turns the stone over.{/n} "The sentries say she came down off that turret this morning laughing like that again. Nobody else in Drezen had ever heard it. I had." {n}Her voice roughens.{/n} "Be good to her, Commander. She's been somebody's weapon. Don't let her be anybody's again. Not even yours."''',
    answer_list=SEELAH_HUB, relationship=REL, forbids=("seelah_dead", "seelah_gone", CLOSED),
    entry='"You look like you\'ve heard something, Seelah."', chapter=5, last=5, delay=12, portrait="Seelah"))

SCENES.append(reaction("Irabeth", P + "react.irabeth.dressing", (P + "dressing",),
    '''{n}Irabeth does not look up from the duty roster.{/n} "The dragon was in the laundry at the fourth bell, cutting her own shirt into strips with my second-best knife. She asked the washerwoman how long linen takes to boil clean. The washerwoman told her. She wrote it down." {n}She turns a page.{/n} "I served on the walls at Kenabres. I have seen her stand between a vrock and a children's ward. I never thought I would see her ask a washerwoman anything." {n}Now she looks up.{/n} "Whatever you are to each other, Commander, she changes that dressing every morning at the same hour, like a watch relieved. I'd not keep her waiting."''',
    answer_list=IRABETH_HUB, relationship=REL, forbids=("irabeth_dead", CLOSED),
    ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"},
    entry='"Anything to report, knight?"', chapter=5, last=5, delay=24))

SCENES.append(reaction("Anevia", P + "react.anevia.kenabres", (RETURNED, P + "watch.kenabres_told"),
    '''{n}Anevia is sitting with her bad leg up on a crate.{/n} "So the silver lady asked after me. By name. Nice of her." {n}She picks at a splinter.{/n} "Half of Kenabres used to go up on the roofs to watch her fly over the Wardstone of an evening. I went up for the view and stayed for the pickpocketing. Everyone's looking up, see." {n}She stops smiling.{/n} "I watched her come down, too. The night it all went. Took me a year to be able to look at the sky." {n}She shrugs, badly.{/n} "Tell her I said hello. And tell her if she ever wants to go and see what's left of the old square, I know the way over the roofs. Bad leg or no."''',
    answer_list=ANEVIA_HUB, relationship=REL, forbids=("anevia_gone", "anevia_dead", CLOSED),
    entry='"Terendelev asked after you."', chapter=5, last=5, delay=24))

SCENES.append(reaction("Storyteller", P + "react.storyteller.quiet", (RETURNED, VOICE),
    '''{n}The Storyteller hears your step and smiles before you speak.{/n} "It has gone quiet, Commander. The voice in the dark. I reached for her last night out of habit, and there was nothing to reach for, and I lay awake for an hour thinking the worst." {n}He shakes his head slowly.{/n} "Then a knight came by the shelves this morning, telling everyone who would stop and listen that a silver-haired woman had been seen on the walls at midnight, arguing with a sentry about the proper way to hold a pike. I have told a great many stories that ended at a pyre. I have never been so glad to have one end in an argument."''',
    answer_list=ST_HUB, relationship=REL, forbids=(ST_DEAD, CLOSED),
    entry='"You look rested, old man."', chapter=5, last=5, delay=24, portrait="Storyteller"))

SCENES.append(reaction("Galfrey", P + "react.galfrey.letter", (RETURNED,),
    '''{n}The letter is sealed with the royal arms of Mendev, and written in a firm, old-fashioned hand.{/n}
"Commander. I took my knights to Iz to grant rest to her soul and her body. It was my duty and I would do it again. You have undone it. I have spent three nights on my knees asking the Inheritor whether I ought to be glad.
"She has not answered. I have decided I am glad regardless, which is either faith or its opposite, and at my age I am no longer sure there is a difference.
"She was our protector and our friend. See that you are hers."
{n}It is signed with the one word, Galfrey, and nothing else: no title.{/n}''',
    remote=True, relationship=REL, forbids=("galfrey.dead", "galfrey.killed_by_commander", CLOSED),
    ForbidOverrides={"galfrey.dead": "galfrey.trickster.returned"},     # Q6 (COX): a Queen brought back writes too
    title="A letter under the royal seal", chapter=5, last=5, delay=48, portrait="Galfrey", Kind="letter",
    ManualOnly=True))                                                    # Q6 (COX): a manual read, not a rest delivery


# --- Epilogue pages (ordered siblings; read-only) ------------------------------------------------------------------------

EPI = "TerendelevEpilogue"
WATCH = P + "watch."


def epilogue(id, text, requires, forbids=(), paragraphs=(), **extra):
    SCENES.append(scene(P + "epilogue." + id, "", EPI, 6, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=forbids, last=6, Relationship=REL, **extra))


# Q6 r3 (INT, ledger row 16): the living-Commander pages never follow an unsurvived sacrifice; `sacrifice` is lifted only
# by trickster.commander_back (Last Call's kept Appointment or the Commander's own return).
SURVIVED = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})


EPILOGUE_PARAGRAPHS = (
    p('''{n}She did not fly again for a long time. In the spring after the war, on an ordinary morning, she walked out onto the north turret, took a long breath as a dragon does, and was a dragon: smaller than she had been, and duller silver, with a rust-red seam down the length of her breast where the Commander's blood had made her. She flew once round Drezen, badly, and landed on the barracks roof, and broke it. She said it was the best morning of her life, and paid for the roof.{/n}''',
      requires=(COMMITTED,), forbids=(LATE,)),
    p('''{n}She never flew again. She said the wings had stayed in the fire at Iz, and that it was a fair price, and that she had seen enough of the sky from above to know it looked better from a wall. On clear nights she took the north turret's watch anyway, and stood with her face into the wind.{/n}''',
      requires=(LATE,)),
    p('''{n}Whatever became of the Worldwound, the Commander's wound did not close. The physicians said it should have. Terendelev said it had been opened for someone else, and would stay open as long as she did, and changed the dressing every morning at the same hour, for the rest of the Commander's life.{/n}''',
      requires=(WOUND_OPEN, P + "dressing")),
    p('''{n}Whatever became of the Worldwound, the Commander's wound did not close. It wept a little every morning, and burned what it touched if what it touched was an enemy's, and never once burned her.{/n}''',
      requires=(WOUND_OPEN,), forbids=(P + "dressing",)),
    p('''{n}She went back to Kenabres only once, to stand in the rebuilt cathedral where she had told a wounded stranger to come the next day. She said the Commander was late, but had come in the end, and that she counted that as a promise kept on both sides.{/n}''',
      requires=(WATCH + "kenabres_told",)),
    p('''{n}When Queen Galfrey's name was spoken in her hearing she went quiet, and stayed quiet, and later, alone, she would go and stand a watch in the chapel of the Inheritor for as long as it took. It was her body that had killed the Queen at Iz. She never let anyone tell her otherwise.{/n}''',
      requires=(QUEEN_FELL,)),
    p('''{n}The claw the Commander carried out of the cave she buried under the tree by the Sarkorian ruins where she had once burned the Wound out of herself. She did not say what she said over it. She came back with dirt under her nails, and smiling.{/n}''',
      requires=(WATCH + "claw_returned",)),
    p('''{n}The knight of the first lance from the infirmary carried the lash-marks on his back for the rest of his life. Terendelev had healed them clean and they scarred anyway, the way some things do. She never spoke of it to the Commander again, and never once, in all the years after, let the Commander give an order in her name.{/n}''',
      requires=(P + "watch.infirmary_flogged",)),
    p('''{n}The knight of the first lance from the infirmary came up to the north turret every year on the anniversary of Iz and stood the night watch beside her. Neither of them said much. In the morning he would nod to her, the way one sentry nods to another, and go down.{/n}''',
      requires=(P + "watch.infirmary_seen",), forbids=(P + "watch.infirmary_flogged",)),
    p('''{n}Nobody in Drezen ever learned whether the letter left on the highest rock of the northern pass was found. The spring after the war it was gone, and in its place, weighted down with a stone, lay a single gold scale the size of a shield. She hung it over the Commander's hearth and would not say a word about it, and polished it every week.{/n}''',
      requires=(P + "watch.letter_written",)),
    p('''{n}She swore she never cheated at cards again. The sentries of the north turret, who went on losing to her for years, said otherwise, but never to her face.{/n}''',
      requires=(P + "watch.what_you_are",)),
    p('''{n}Whatever the Worldwound did at the end, she did not go out with it. She was on the north turret at the hour of the dressing with the linen folded in its square, and when the Commander came up the stair she said, very drily, that she had known she would be, and then sat down rather suddenly on the stones and did not get up for some time.{/n}''',
      requires=(P + "finale.asked", COMMITTED)),
    p('''{n}Every night of the war she came down to the war room at the second bell and put her hand on the map, and told the Commander where the Wound was loud and where it was holding its breath. She was right more often than the scouts. Every night it cost her a nosebleed, and every night she wiped it on the Commander's handkerchief and said it was a fair trade for a life, and it was.{/n}''',
      requires=(P + "watch.compass",)),
    p('''{n}She never read the Wound's weather for the crusade again after that one night, and the Commander never asked. Once, years later, she said it was the first time anyone had ever refused to use her, and that she had not known until then how tired she was of being useful.{/n}''',
      requires=(P + "watch.not_a_map",)),
    p('''{n}The people of Kenabres who had knelt to her in the lower town went home, in time, to rebuild. Every festival after that, somebody climbed the new gate of Kenabres and tied a blue ribbon at the top of it, up where nobody could reach, and nobody would ever say who.{/n}''',
      requires=(P + "watch.known_to_kenabres",)),
    p('''{n}She never slept in the dark again. There was always a candle, and on the bad nights there was the Commander's hearth, and the Commander's knee to put her head on, and the sentries learned not to knock at that door between the third bell and the sixth.{/n}''',
      requires=(P + "watch.sat_up",)),
    p('''{n}The woman who fried bread by the lower gate went to her grave believing that the silver-haired widow from Kenabres had married the Commander of the crusade in the middle of her market, over a crock of honey. It was not strictly true. Nobody who had been there that evening ever corrected her.{/n}''',
      requires=(P + "watch.kissed_in_the_market",)),
    p('''{n}Whenever the Commander rode out, she stood in the gate of Drezen until the last horse was home, however long it took. She never once asked the Commander not to go. She only counted.{/n}''',
      requires=(P + "watch.quarrel",)),
    p('''{n}She never did climb back up to the mountains. She said the view from the lower town had certain compensations, and when asked what they were, looked at the Commander, and did not answer.{/n}''',
      requires=(P + "watch.mountains", COMMITTED)),
    p('''{n}She found her prayers again in the second winter after the war. Nobody ever learned what she said to the Inheritor on her knees in the chapel of Drezen, night after night. The chaplain would say only that it went on a long time, and that he had once, passing, distinctly heard the word "turnips".{/n}''',
      requires=(P + "watch.faith",)),
    p('''{n}The silver along her collarbone never went away. In the lower town they said it was a mark of the Inheritor's favour; in the barracks they said it was something else, and grinned; she let both stories stand, and wore her shirts open at the throat.{/n}''',
      requires=(P + "watch.scales_stayed",)),
    p('''{n}The dragon never learned whether her message to the knight was welcome. But one evening, a year after the war, somebody on the east wall of Drezen sang to a sword, in tune, loud enough to carry all the way to the north turret, and Terendelev stood at the parapet with her eyes shut until the song was done.{/n}''',
      requires=(P + "watch.irabeth_message",), forbids=("irabeth_dead",)),
    p('''{n}The Storyteller told her story for the rest of his long life, in every tavern and camp between Drezen and Absalom: the dragon who died twice and came back in a borrowed cloak. He always ended it in the same place: a crate in the lower town, a crock of honey, and a woman laughing. He said it was the only ending of his he had ever been allowed to hear.{/n}''',
      requires=(P + "watch.storyteller_thanked",), forbids=("storyteller.dead",)),
    p('''{n}The fire at Iz had taken more of the Commander's blood than it needed, and some of it never came back. The Commander's hands were cold every winter after, whatever the fire. Every winter Terendelev took them between her own, which were always too warm, and held them until they were not, and said it was a debt the fire owed and she was collecting it.{/n}''',
      requires=(BLED_WHITE,)),
    p('''{n}She never forgave the Lord of Locusts, and never pretended to. If the day came when he was cut down again, she said, she meant to be there, in whatever shape she had, and she meant it to be the last day.{/n}''',
      requires=(WATCH + "deskari_vow",)),
)

epilogue("watch", '''{n}Terendelev stayed in Drezen. She kept the north turret's night watch for the rest of the war, and for a long time after it, and the garrison learned to salute her on the stair. She never asked to be called anything but Terendelev; the city called her its dragon anyway, the way Kenabres once had, and she said that a city which insists on having a dragon should at least keep its gutters clean, and made sure it did.{/n}
{n}She healed whoever came to her. She never healed the Commander, because she could not, and she never stopped trying.{/n}''',
         requires=(COMMITTED,), forbids=(CLOSED, "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS, **SURVIVED)

epilogue("late", '''{n}The war ended before Terendelev had answered her own question: what she owed, and how to pay it. The evening after Threshold she climbed the stair to the Commander's rooms with a roll of clean linen under her arm, knelt, and changed the dressing on the wound without asking. When it was done she stayed kneeling, and said that she had decided, and that it would take the rest of the Commander's life, and that she hoped that would be long.{/n}''',
         requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED, P + "declined", "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS,
         **SURVIVED)

epilogue("debt", '''{n}Terendelev paid her debt. She stood between the Commander and harm at Threshold and after, and never once let it be said that a silver dragon had failed to settle what she owed. She stood watch on the north turret every night of the war, and never once let the Commander join her there.{/n}
{n}It was a very correct arrangement. Everyone in Drezen said so, and some of them said it kindly.{/n}
{n}On the last night of the war she was seen on the north turret, alone, with the linen folded in its square in her lap, looking at the Commander's lit window for a long while. Then she put the linen down on the parapet and went down the stair, and in the morning the dressing was changed at the proper hour, correctly, and she did not speak.{/n}''',
         requires=(P + "declined",), forbids=(COMMITTED, CLOSED, "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS, **SURVIVED)

epilogue("sacrifice", '''{n}The Commander did not come back from the Threshold. Terendelev heard it on the north turret, from a runner who could not look at her, and thanked him, and sent him down.{/n}
{n}She kept the watch that night anyway, and the next, and every night after, with the linen folded in its square on the parapet beside her while the hour of the dressing came and went. The garrison learned not to speak to her between the second bell and the dawn. In the spring she walked out of Drezen with a pike and a borrowed cloak, and the sentries on the north road said she did not look back, which in a dragon, one of them said, is a kind of looking back.{/n}''',
         requires=(RETURNED, "sacrifice"), forbids=("trickster.commander_back", CLOSED),
         RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED, P + "declined"]])

epilogue("guardian", '''{n}Terendelev went home to Kenabres. She walked the whole way, since she could not fly it, and arrived at the broken gate in a borrowed cloak with her boots worn through, and the first person to recognise her was a baker who had sold her bread for forty years and had never once guessed what she was.{/n}
{n}She did not ask to be its dragon again; she could not have been. She took a room over the rebuilt east gate and stood its night watch in her grey coat with a pike, and healed whoever came up the stair, and was, the city said, a great deal more trouble than the old one had been, and a great deal easier to talk to. She guarded the city for the rest of its long life. Once a year a letter came to the Commander in a hand like claw-marks, always short. The last line was always the same: "The wound. Is it still open? Tell me the truth."{/n}''',
         requires=(RETURNED, P + "guardian"), paragraphs=EPILOGUE_PARAGRAPHS)

epilogue("rest", '''{n}The fire at Iz burned for nine days and then went out on its own. The crusade raised a cairn over the bones, with the Queen's leave, and it is still there. Travellers who pass it say that it is warm to the touch in winter, which the learned say is only the sun on the stones.{/n}''',
         requires=(RESTED,), forbids=(RETURNED,))


def integrate(payload):
    """Her native reads (the Iz battle cue, the claw story, Areelu's audience, the claw item, the Trickster's sight), her
    Derived keys, the monster latch, and the book-picture fallback. Other world keys bind on demand in trickster_world."""
    for kind, source in (("SeenCues", "SeenCues"), ("SeenCues", "SeenCues_parent"), ("Etudes", "Etudes"),
                         ("InventoryItems", "InventoryItems"), ("MainCharacterFacts", "MainCharacterFacts"), ("Latches", "Latches")):
        for key, value in BINDINGS[source].items():
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != value:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = value
    items = payload.setdefault("RemovableItems", [])
    if CLAW not in items:
        items.append(CLAW)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("PortraitFallbacks", {}).setdefault("Terendelev", PORTRAIT_GUID)
