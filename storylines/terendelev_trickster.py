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
the Commander on a dead vrock outside Drezen), so it should burn only what is Deskari's; her spirit once remade her out of
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
    nar("scale", "{n}Among the rations and maps lies a silver scale the size of your palm. Terendelev's. You lift it into the candlelight. It has not tarnished. The silver is cold against your fingers.{/n}",
        c("[Turn it over in your fingers.]", "square")),
    nar("no_scale", '{n}There is no silver scale among the rations and maps. Your hand pauses over the open pack. You think of Terendelev, protector of Kenabres.{/n}',
        c('[Close the pack.]', "square")),
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


# --- Chapter 3 (Drezen): what the wound weeps --------------------------------------------------------------
# The planted preparation: the Commander tests what the wound's blood does before trusting it with anything that matters.

page(P + "wound.weeps", "What the wound weeps", [
    nar("start", '{n}Drezen is quiet beyond your shutters. You wake with your shirt stuck to your side. The old wound has opened again. A drop of blood has fallen on the hearthstone and left a bright scorch mark.{/n}',
        c("Continue", "areelu", requires=(AREELU_TOLD,)),
        c("Continue", "plain", forbids=(AREELU_TOLD,))),
    nar("areelu", "{n}Areelu said Terendelev had only dulled your pain. She said she implanted the crystal in the caves, and that each drop from the unhealed wound burns your enemies. You look at the scorch mark beside the bed.{/n}",
        c("Continue", "test")),
    nar("plain", '{n}The healers have tried prayers and salves. None has closed the wound. You strip away the wet dressing and look at the mark on the stone.{/n}',
        c("Continue", "test")),
    nar("test", '{n}A vrock came over the north wall during the last watch. The sentries killed it. Its carcass lies outside the gate, feathers stiff with filth. You take your knife and a scrap of clean linen.{/n}',
        c("[Catch a drop on your knife and lay it on the vrock's hide.]", "vrock", flags=(BLOOD_TESTED,)),
        c("[Bind the wound and go back to sleep.]", "sleep")),
    nar("vrock", "{n}The drop hisses. It eats through the hide and the meat beneath it. You slide the clean blade under the burning scrap. The hissing stops at the steel; red blood pools there without scorching it. On a second scrap the same thing happens. The smell is appalling.{/n}\n{n}You try it on the flat of your own blade: nothing. On a strip of clean linen: only blood.{/n}\n{n}It burns what belongs to the enemy, then, and leaves alone what does not. You try it on a camp rat the dogs killed: the rat stays a dead rat. It does not mend, or make, or raise. Whatever the wound's blood is for, it is for taking things away.{/n}\n{n}You write down what the blood touched and what it burned. One dead demon is a poor foundation for a theory. It is what you have.{/n}",
        c("Continue", "scale_choice", requires=(SCALE_HELD,)),
        c("Continue", "sleep", forbids=(SCALE_HELD,))),
    nar("scale_choice", "{n}Terendelev's scale is in your pack. You unwrap it beside the bloodstained knife.{/n}",
        c("[Touch a drop of the blood to her scale.]", "scale", flags=(SCALE_WARMED,)),
        c("[Leave the scale where it is.]", "sleep")),
    nar("scale", '{n}The scale stays cold. Then warmth spreads beneath your thumb, faint and brief. By the time you lift it to the lantern it is cold again. You wipe away the brown smear.{/n}',
        c('"Terendelev?"', "silence")),
    nar("silence", '{n}Nothing answers. Beyond the wall a sentry calls to his relief. You wrap the scale and put it away.{/n}',
        c("[Bind the wound.]")),
    nar("sleep", "{n}You bind the wound. By morning the bleeding has stopped. Outside, soldiers are hauling the vrock's carcass away.{/n}",
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
        watch='''{n}Galfrey follows your gaze. She has not sheathed her sword; she leans on it, as she leaned on it through the fight.{/n} "She stood beside us through this war. Kenabres was her home. We gave her the only mercy we had to give." {n}Her jaw sets.{/n} "Let it burn, Commander. It is her pyre now."''',
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
        fire("pitch_vrock", "{n}You know what it does, because you tested it outside Drezen's gate before you trusted it with anything: a coin-sized pit eaten through a dead vrock's hide; your own blade and a strip of clean linen left untouched. It burns what is the enemy's. It makes nothing. Whatever it leaves, something else has to shape.{/n}",
             c("Continue", "pitch_scale", requires=(SCALE_WARMED,)),
             c("Continue", "pitch_plan", forbids=(SCALE_WARMED,))),
        fire("pitch_scale", '{n}A drop warmed her scale once, for a breath. You do not know what that proved. The small warmth stays in your thoughts as you look into the fire.{/n}',
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
        fire("measured", "{n}Outside Drezen, the hissing stopped where the vrock\'s filth met clean steel. You watch for that edge now. White fire eats the black marrow; then its hiss dies and the blood runs red over clean bone. You press the dressing against your side. The cleansing is done. Whether she can make flesh of what remains is still her gamble.{/n}",
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
        voice("warm", '''{n}She is warm under your hands: not the dry heat of the fire, but the warmth of a body with blood moving in it. Some of it is yours. Her eyes go to your side, where the wound is still running freely and has no intention of stopping.{/n} "You are still open. You opened it for me and it has not shut." {n}Her fingers find it, and she says the old words from the square, and the pain goes quiet. The bleeding slows. It does not stop.{/n} "It will not close," {n}she says softly.{/n} "I can feel that it never will. What have you done to yourself?"''',
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
    nar("start", '{n}The wound opens by itself, after your return from Iz. There is no knife in it and no blow; you wake with the bed soaked and the bleeding running faster than it has since Kenabres, and it does not slow for bandages or prayers until nearly morning.{/n}\n{n}You lie in the grey light and think about the fire.{/n}',
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
    nar("failed", '{n}You looked into the fire until the heat drove you back. You found nothing. Now the wound has opened again, and the bones were still burning when you left. You remember how carefully the knights kept away from them.{/n}',
        c("Continue", "ride")),
    nar("claimed", '''{n}She told you she had been owned once and would not be owned again, and then she hid from you in her own fire. She was right. You have been composing a better sentence ever since.{/n}''',
        c("Continue", "ride")),
    nar("flinched", '''{n}You held the knife over the wound and could not do it. She did not blame you. That was the worst of it.{/n}''',
        c("Continue", "ride")),
    nar("passed", '''{n}You walked past that fire at Iz with the rest of the column. You told yourself it was a pyre. You have been walking past it every night since.{/n}''',
        c("Continue", "ride")),
    nar("ride", '{n}You ride back to Iz with a handful of soldiers. They have learned not to ask why you keep a hand pressed to your side. Wind carries ash between the ruined walls.{/n} {n}The bones still burn: a low bed of white cinders, the skull half buried, and a small flame at its heart.{/n}',
        c("[Go to the skull.]", "voice")),
    te("voice", '''{n}This time you do not need to look. Whatever breathes in the skull breathes very slowly, and it has been listening for hoofbeats.{/n} "Someone came." {n}The voice is thinner than smoke.{/n} "Nobody comes to a pyre once it is lit. It is not done. Who are you, and what do you want?"''',
        c('"The wounded one from the festival square. You healed me, the day Kenabres fell. I\'ve come to ask you to come back."', "ask",
          requires=(LEFT_EARLY,)),
        c('"The one who tried to claim you. I\'ve come to ask properly, this time."', "ask", requires=(REFUSED_CLAIM,), forbids=(LEFT_EARLY,)),
        c('"The one who lost nerve. I\'ve come to finish it, if you\'ll still have it."', "ask", requires=(FLINCHED,),
          forbids=(LEFT_EARLY, REFUSED_CLAIM)),
        c('"The wounded one from the square. I walked away from this fire once. I\'ve come back to ask you to come back."', "ask",
          forbids=(LEFT_EARLY, REFUSED_CLAIM, FLINCHED))),
    te("ask", '"Come back." {n}A breath that might have been a laugh, once.{/n} "Into what? The body he made is ash. I have been made foul before, long ago; I shut myself in a cave and burned the Wound out of my own spirit until I could look at the sun again. I have nothing left to burn with now, and less of me left in this fire. The fire takes a little every hour."',
        c('"Then take something from me instead."', "gamble")),
    nar("gamble", '''{n}You tell her what you have. A wound that has never closed, and is open now. Blood that burns what belongs to the Abyss and leaves other things alone. Her own spirit, which has done this once already with nothing to work in but itself. It is a guess, and you tell her it is a guess.{/n}''',
        c("Continue", "risk")),
    te("risk", '''"And if it makes me another thing like the one you killed? Or burns me with the rest of his?" {n}The flame is very small.{/n} "And there is less of me than there was. Whatever comes out of this fire now will be less than what went in. I think the wings are gone already. I felt them go while I waited in the ash."''',
        c('"Less of you is still you. I\'m asking."', "choose"),
        c('[Let her rest] "Then rest. I won\'t make you."', "rest", flags=(RESTED, CLOSED))),
    te("choose", '"Asking. Yes. You are." {n}The flame gathers itself.{/n} "Very well, wounded one. I have been cold, listening for you. Open it."',
        c("[Open the wound over the ash.]", "cut", mythic="Trickster")),
    nar("cut", '''{n}The wound is already open. You open it further, and kneel over the ash with the cut side down, and the blood runs out from under your ribs onto it, and where it finds what is left of the ravener it burns white, and where it finds the small flame at the heart of the skull, the flame drinks.{/n}
{n}It takes longer than you would have liked. You are on your knees in the ash by the end of it, and a woman is on her knees in front of you, naked and grey with cinders, holding your hand in both of hers as though it were the only warm thing in the world.{/n}''',
        c("Continue", "after")),
    te("after", '''"Cold," {n}she says, amazed, and then, looking at the blood on her own palm where the ash has cut it:{/n} "Red." {n}She tries to gather herself inward, the way a dragon does, and nothing comes; she does not seem surprised. She only looks at the ash where the wings would have been.{/n} "They are gone. I knew they would be. It does not matter. I have hands. Give me your cloak, and let us leave this place before it remembers us."''',
        c('[Wrap her in your cloak.] "Let\'s go home."', flags=(RETURNED, STARTED, WOUND_OPEN, GROUNDED, LATE))),
    te("rest", '''"Thank you." {n}The flame gutters.{/n} "You came back. That will do. Tell no one in Kenabres; let them remember the square."''',
        c("[Stay until it goes out.]")),
], requires=("trickster", MONSTER_DEAD, MONSTER_LATCH, "iz.done"), Areas=[DREZEN], forbids=(RETURNED, CLOSED, *PARENT_EMBODIED), delay=24,
    TricksterDevice=True, TricksterState="late")


# --- Reactions: companions and NPCs with a real stake in her ------------------------------------------------------------

SCENES.append(reaction("Seelah", P + "react.seelah.watch", (P + "night.seen",),
    '{n}Seelah is sitting on the edge of the practice ring with a whetstone she is not using.{/n} "So. The north turret." {n}She grins, then doesn\'t.{/n} "My first festival in Kenabres, when I was still new to the order. Old habits: I caught my own hand halfway into a merchant\'s purse, and when I looked round she was standing right behind me in her human shape. She didn\'t call the watch. She asked whether the Inheritor paid her paladins so badly, and when I said yes, she laughed like bells and bought me a pie." {n}She turns the stone over.{/n} "The sentries say she came down off that turret this morning laughing like that again. I knew that laugh. Hearing it here was something else." {n}Her voice roughens.{/n} "Be good to her, Commander. She\'s been somebody\'s weapon. Don\'t let her be anybody\'s again. Not even yours."',
    answer_list=SEELAH_HUB, relationship=REL, forbids=("seelah_dead", "seelah_gone", CLOSED),
    ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"},
    entry='"You look like you\'ve heard something, Seelah."', chapter=5, last=5, delay=12, portrait="Seelah"))

SCENES.append(reaction("Irabeth", P + "react.irabeth.dressing", (P + "dressing",),
    '''{n}Irabeth does not look up from the duty roster.{/n} "The dragon was in the laundry at the fourth bell, cutting her own shirt into strips with my second-best knife. She asked the washerwoman how long linen takes to boil clean. The washerwoman told her. She wrote it down." {n}She turns a page.{/n} "I served on the walls at Kenabres. I have seen her stand between a vrock and a children's ward. I never thought I would see her ask a washerwoman anything." {n}Now she looks up.{/n} "Whatever you are to each other, Commander, she changes that dressing every morning at the same hour, like a watch relieved. I'd not keep her waiting."''',
    answer_list=IRABETH_HUB, relationship=REL, forbids=("irabeth_dead", CLOSED),
    ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"},
    entry='"Anything to report, knight?"', chapter=5, last=5, delay=24))

SCENES.append(reaction("Anevia", P + "react.anevia.kenabres", (RETURNED, P + "watch.kenabres_told"),
    '{n}Anevia is sitting with her bad leg up on a crate.{/n} "So the silver lady asked after me. By name. Nice of her." {n}She picks at a splinter.{/n} "Half of Kenabres used to go up on the roofs to watch her fly over the Wardstone of an evening. I went up for the view and stayed for the pickpocketing. Everyone\'s looking up, see." {n}She stops smiling.{/n} "I watched her come down, too. The day the city fell. For a long while I couldn\'t look up without seeing that scythe again." {n}She shrugs, badly.{/n} "Tell her I said hello. And tell her if she ever wants to go and see what\'s left of the old square, I know the way over the roofs. Bad leg or no."',
    answer_list=ANEVIA_HUB, relationship=REL, forbids=("anevia_gone", "anevia_dead", CLOSED),
    ForbidOverrides={"anevia_dead": "anevia.trickster.returned", "anevia_gone": "anevia.trickster.returned"},
    entry='"Terendelev asked after you."', chapter=5, last=5, delay=24))

SCENES.append(reaction("Storyteller", P + "react.storyteller.quiet", (RETURNED, VOICE),
    '''{n}The Storyteller hears your step and smiles before you speak.{/n} "It has gone quiet, Commander. The voice in the dark. I reached for her last night out of habit, and there was nothing to reach for, and I lay awake for an hour thinking the worst." {n}He shakes his head slowly.{/n} "Then a knight came by the shelves this morning, telling everyone who would stop and listen that a silver-haired woman had been seen on the walls at midnight, arguing with a sentry about the proper way to hold a pike. I have told a great many stories that ended at a pyre. I have never been so glad to have one end in an argument."''',
    answer_list=ST_HUB, relationship=REL, forbids=(ST_DEAD, CLOSED),
    entry='"You look rested, old man."', chapter=5, last=5, delay=24, portrait="Storyteller"))

SCENES.append(reaction("Galfrey", P + "react.galfrey.letter", (RETURNED,),
    '{n}Terendelev passes you a sealed letter.{/n}',
    remote=True, relationship=REL, forbids=("galfrey.dead", "galfrey.killed_by_commander", CLOSED),
    ForbidOverrides={"galfrey.dead": "galfrey.trickster.returned"},     # Q6 (COX): a Queen brought back writes too
    title="A letter for the dragon", chapter=5, last=5, delay=48, portrait="Galfrey", Kind="letter",
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
    p("{n}She did not fly again for a long time. In the spring after the war, on an ordinary morning, she walked out onto the north turret, took a long breath as a dragon does, and was a dragon: smaller than she had been, and duller silver, with a rust-red seam down the length of her breast where the Commander's blood had made her. She flew once round Drezen, badly, and landed on the barracks roof, and broke it. She said it was the best morning of her life, and paid for the roof.{/n}", requires=('terendelev.committed',), forbids=('terendelev.trickster.cost.late',)),
    p("{n}She never flew again. She said the wings had stayed in the fire at Iz, and that it was a fair price, and that she had seen enough of the sky from above to know it looked better from a wall. On clear nights she took the north turret's watch anyway, and stood with her face into the wind.{/n}", requires=('terendelev.trickster.cost.late',), forbids=()),
    p("{n}Whatever became of the Worldwound, the Commander's wound did not close. The physicians said it should have. Terendelev said it had been opened for someone else, and would stay open as long as she did, and changed the dressing every morning at the same hour, for the rest of the Commander's life.{/n}", requires=('terendelev.trickster.cost.wound_open', 'terendelev.trickster.dressing'), forbids=()),
    p("{n}Whatever became of the Worldwound, the Commander's wound did not close. It wept a little every morning, and burned what it touched if what it touched was an enemy's, and never once burned her.{/n}", requires=('terendelev.trickster.cost.wound_open',), forbids=('terendelev.trickster.dressing',)),
    p('{n}She went back to Kenabres only once, to stand in the cathedral site as the streets were rebuilt where she had told a wounded stranger to come the next day. She said the Commander was late, but had come in the end, and that she counted that as a promise kept on both sides.{/n}', requires=('terendelev.trickster.watch.kenabres_told', 'engine.l12.kenabres_rebuilding'), forbids=()),
    p("{n}When Queen Galfrey's name was spoken in her hearing she went quiet, and stayed quiet, and later, alone, she would go and stand a watch in the chapel of the Inheritor for as long as it took. It was her body that had killed the Queen at Iz. She never let anyone tell her otherwise.{/n}", requires=('terendelev.trickster.saw_the_queen_fall',), forbids=('iz.manuscripts', 'galfrey.killed_by_commander')),
    p("{n}The claw the Commander found at Leper's Smile she buried under the tree by the Sarkorian ruins where she had once burned the Wound out of herself. She did not say what she said over it. She came back with dirt under her nails, and smiling.{/n}", requires=('terendelev.trickster.watch.claw_returned',), forbids=()),
    p('{n}The knight of the first lance from the infirmary carried the lash-marks on his back for the rest of his life. Terendelev had healed them clean and they scarred anyway, the way some things do. She never spoke of it to the Commander again, and never once, in all the years after, let the Commander give an order in her name.{/n}', requires=('terendelev.trickster.watch.infirmary_flogged',), forbids=()),
    p('{n}The knight of the first lance from the infirmary came up to the north turret every year on the anniversary of Iz and stood the night watch beside her. Neither of them said much. In the morning he would nod to her, the way one sentry nods to another, and go down.{/n}', requires=('terendelev.trickster.watch.infirmary_seen',), forbids=('terendelev.trickster.watch.infirmary_flogged',)),
    p("{n}Nobody in Drezen ever learned whether the letter left on the highest rock of the northern pass was found. The spring after the war it was gone, and in its place, weighted down with a stone, lay a single gold scale the size of a shield. She hung it over the Commander's hearth and would not say a word about it, and polished it every week.{/n}", requires=('terendelev.trickster.watch.letter_written',), forbids=()),
    p('{n}She swore she never cheated at cards again. The sentries of the north turret, who went on losing to her for years, said otherwise, but never to her face.{/n}', requires=('terendelev.trickster.watch.what_you_are',), forbids=()),
    p('{n}Whatever the Worldwound did at the end, she did not go out with it. She was on the north turret at the hour of the dressing with the linen folded in its square, and when the Commander came up the stair she said, very drily, that she had known she would be, and then sat down rather suddenly on the stones and did not get up for some time.{/n}', requires=('terendelev.trickster.finale.asked', 'terendelev.committed'), forbids=()),
    p("{n}Every night of the war she came down to the war room at the second bell and put her hand on the map, and told the Commander where the Wound was loud and where it was holding its breath. She was right more often than the scouts. Every night it cost her a nosebleed, and every night she wiped it on the Commander's handkerchief and said it was a fair trade for a life, and it was.{/n}", requires=('terendelev.trickster.watch.compass',), forbids=()),
    p("{n}She never read the Wound's weather for the crusade again after that one night, and the Commander never asked. Once, years later, she said it was the first time anyone had ever refused to use her, and that she had not known until then how tired she was of being useful.{/n}", requires=('terendelev.trickster.watch.not_a_map',), forbids=()),
    p('{n}The people of Kenabres who had knelt to her in the lower town went home, in time, to rebuild. Every festival after that, somebody climbed the new gate of Kenabres and tied a blue ribbon at the top of it, up where nobody could reach, and nobody would ever say who.{/n}', requires=('terendelev.trickster.watch.known_to_kenabres',), forbids=()),
    p("{n}She never slept in the dark again. There was always a candle, and on the bad nights there was the Commander's hearth, and the Commander's knee to put her head on, and the sentries learned not to knock at that door between the third bell and the sixth.{/n}", requires=('terendelev.trickster.watch.sat_up',), forbids=()),
    p('{n}The woman who fried bread by the lower gate went to her grave believing that the silver-haired widow from Kenabres had married the Commander of the crusade in the middle of her market, over a crock of honey. It was not strictly true. Nobody who had been there that evening ever corrected her.{/n}', requires=('terendelev.trickster.watch.kissed_in_the_market',), forbids=()),
    p('{n}Whenever the Commander rode out, she stood in the gate of Drezen until the last horse was home, however long it took. She never once asked the Commander not to go. She only counted.{/n}', requires=('terendelev.trickster.watch.quarrel',), forbids=()),
    p('{n}She never did climb back up to the mountains. She said the view from the lower town had certain compensations, and when asked what they were, looked at the Commander, and did not answer.{/n}', requires=('terendelev.trickster.watch.mountains', 'terendelev.committed'), forbids=()),
    p('{n}She found her prayers again in the second winter after the war. Nobody ever learned what she said to the Inheritor on her knees in the chapel of Drezen, night after night. The chaplain would say only that it went on a long time, and that he had once, passing, distinctly heard the word "turnips".{/n}', requires=('terendelev.trickster.watch.faith',), forbids=()),
    p("{n}The silver along her collarbone never went away. In the lower town they said it was a mark of the Inheritor's favour; in the barracks they said it was something else, and grinned; she let both stories stand, and wore her shirts open at the throat.{/n}", requires=('terendelev.trickster.watch.scales_stayed',), forbids=()),
    p("{n}Terendelev still remembered the knight's song from Kenabres. In Drezen, when she heard Irabeth singing on the wall, she stopped at the foot of the stair and listened. She waited until the last note before climbing to the watch.{/n}", requires=('terendelev.trickster.watch.irabeth_message', 'crossroute.irabeth.available'), forbids=('irabeth_dead',)),
    p('{n}The Storyteller told of the dragon who died twice and came back beside her pyre at Iz. He remembered her kneeling among his books in a borrowed cloak, and the laugh that followed her thanks.{/n}', requires=('terendelev.trickster.watch.storyteller_thanked',), forbids=('storyteller.dead', 'storyteller.dead_delayed')),
    p("{n}The fire at Iz had taken more of the Commander's blood than it needed, and some of it never came back. The Commander's hands were cold every winter after, whatever the fire. Every winter Terendelev took them between her own, which were always too warm, and held them until they were not, and said it was a debt the fire owed and she was collecting it.{/n}", requires=('terendelev.trickster.cost.bled_white',), forbids=()),
    p('{n}She never forgave the Lord of Locusts, and never pretended to. If the day came when he was cut down again, she said, she meant to be there, in whatever shape she had, and she meant it to be the last day.{/n}', requires=('terendelev.trickster.watch.deskari_vow',), forbids=()),
    p("{n}She went back to Kenabres only once, to stand in the cathedral's old site where she had told a wounded stranger to come the next day. She said the Commander was late, but had come in the end, and that she counted that as a promise kept on both sides.{/n}", requires=('terendelev.trickster.watch.kenabres_told',), forbids=('engine.l12.kenabres_rebuilding',)),
    p("{n}When the Storyteller left his mortal body to serve the Lady of Graves, he took the memory of Terendelev's voice with him: her thanks, her laughter, and the rustle of her cloak as she rose from the dust beside his books.{/n}", requires=('terendelev.trickster.watch.storyteller_thanked', 'storyteller.dead_delayed'), forbids=('storyteller.dead',)),
    p("{n}When the Storyteller left his mortal body to serve the Lady of Graves, he took the memory of Terendelev's voice with him: her thanks, her laughter, and the rustle of her cloak as she rose from the dust beside his books.{/n}", requires=('terendelev.trickster.watch.storyteller_thanked', 'storyteller.dead_main'), forbids=('storyteller.dead_dlc',)),
    p("{n}After Irabeth's return, Terendelev heard her singing on Drezen's wall. She stopped at the foot of the stair. When the song ended, she called the knight's name and went up to greet her.{/n}", requires=('terendelev.trickster.watch.irabeth_message', 'irabeth_dead', 'irabeth.trickster.returned', 'crossroute.irabeth.available'), forbids=()),
    p("{n}In Drezen she kept a candle for the knight whose grave she had asked the Commander to find. She said the knight's name before the evening watch.{/n}", requires=('terendelev.trickster.watch.irabeth_grave_inquiry', 'irabeth_dead'), forbids=('irabeth.trickster.returned',)),
)

epilogue("watch", '''{n}Terendelev stayed in Drezen. She kept the north turret's night watch for the rest of the war, and for a long time after it, and the garrison learned to salute her on the stair. She never asked to be called anything but Terendelev; the city called her its dragon anyway, the way Kenabres once had, and she said that a city which insists on having a dragon should at least keep its gutters clean, and made sure it did.{/n}
{n}She healed whoever came to her. She never healed the Commander, because she could not, and she never stopped trying.{/n}''',
         requires=(COMMITTED,), forbids=(CLOSED, "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS, **SURVIVED)

epilogue("late", '''{n}The evening after the Commander returned from Threshold, Terendelev climbed the stair with clean linen under her arm. She laid it beside the bed. "You told me nothing was owed. I have not forgotten." She took the Commander's hand. "I want to stay. Not until an account is settled. With you." The linen waited while she drew the Commander close. At dawn she opened the bundle and changed the dressing; afterward she went down to relieve the turret watch.{/n}''',
         requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED, P + "declined", "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS,
         **SURVIVED)

epilogue("debt", '''{n}Terendelev paid her debt. She tended the wounded who remained in Drezen while the army went to Threshold, and never once let it be said that a silver dragon had failed to settle what she owed. She stood watch on the north turret every night of the war, and never once let the Commander join her there.{/n}
{n}It was a very correct arrangement. Everyone in Drezen said so, and some of them said it kindly.{/n}
{n}On the last night of the war she was seen on the north turret, alone, with the linen folded in its square in her lap, looking at the Commander's lit window for a long while. Then she put the linen down on the parapet and went down the stair, and in the morning the dressing was changed at the proper hour, correctly, and she did not speak.{/n}''',
         requires=(P + "declined",), forbids=(COMMITTED, CLOSED, "sacrifice"), paragraphs=EPILOGUE_PARAGRAPHS, **SURVIVED)

epilogue("sacrifice", '''{n}The Commander did not come back from the Threshold. Terendelev heard it on the north turret, from a runner who could not look at her, and thanked him, and sent him down.{/n}
{n}She kept the watch that night anyway, and the next, and every night after, with the linen folded in its square on the parapet beside her while the hour of the dressing came and went. The garrison learned not to speak to her between the second bell and the dawn. In the spring she walked out of Drezen with a pike and a borrowed cloak, and the sentries on the north road said she did not look back, which in a dragon, one of them said, is a kind of looking back.{/n}''',
         requires=(RETURNED, "sacrifice"), forbids=("trickster.commander_back", CLOSED),
         RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED, P + "declined"]])

# Authored M24: departure has its own Kenabres callbacks.
GUARDIAN_PARAGRAPHS = (
    p("{n}She did not fly again for a long time. In the spring after the war, on an ordinary morning, she walked out onto the north turret, took a long breath as a dragon does, and was a dragon: smaller than she had been, and duller silver, with a rust-red seam down the length of her breast where the Commander's blood had made her. She flew once round Drezen, badly, and landed on the barracks roof, and broke it. She said it was the best morning of her life, and paid for the roof.{/n}", requires=('terendelev.committed',), forbids=('terendelev.trickster.cost.late', 'terendelev.trickster.guardian')),
    p("{n}She never flew again. On clear nights she stood the watch at Kenabres's east gate with her face into the wind. When the sentries offered her the sheltered post, she told them she had spent quite enough time out of the sky.{/n}", requires=('terendelev.trickster.cost.late',), forbids=()),
    p('{n}The wound she had tended in Drezen remained open. From Kenabres she sent clean linen and exact instructions. The Commander had to find other hands to tie the knots.{/n}', requires=('terendelev.trickster.cost.wound_open', 'terendelev.trickster.dressing'), forbids=()),
    p("{n}Whatever became of the Worldwound, the Commander's wound did not close. It wept a little every morning, and burned what it touched if what it touched was an enemy's, and had not burned Terendelev at Iz.{/n}", requires=('terendelev.trickster.cost.wound_open',), forbids=('terendelev.trickster.dressing',)),
    p('{n}She helped the people of Kenabres rebuild, carrying stone, setting broken bones and quarrelling over the strength of the new walls. At the cathedral site she remembered the wounded stranger she had expected the next morning. Much had delayed them both.{/n}', requires=('terendelev.trickster.watch.kenabres_told', 'engine.l12.kenabres_rebuilding'), forbids=()),
    p("{n}In Kenabres she stood a watch in the Inheritor's chapel for the crusaders killed by her body at Iz. She remembered Galfrey among them. She would not let the Commander call them strangers.{/n}", requires=('terendelev.trickster.saw_the_queen_fall',), forbids=('iz.manuscripts', 'galfrey.killed_by_commander')),
    p("{n}The claw the Commander found at Leper's Smile she buried under the tree by the Sarkorian ruins where she had once burned the Wound out of herself. She did not say what she said over it. She came back with dirt under her nails, and smiling.{/n}", requires=('terendelev.trickster.watch.claw_returned',), forbids=()),
    p('{n}The knight of the first lance carried the lash-marks for the rest of his life. She remembered who had ordered the lashes. In Kenabres she did not let the Commander lend orders the authority of her name.{/n}', requires=('terendelev.trickster.watch.infirmary_flogged',), forbids=()),
    p('{n}The knight of the first lance came to Kenabres on the anniversary of Iz and stood the east-gate watch beside her. At dawn he nodded to her and went down. Neither had asked the other to forget.{/n}', requires=('terendelev.trickster.watch.infirmary_seen',), forbids=('terendelev.trickster.watch.infirmary_flogged',)),
    p('{n}A driver brought a gold scale to Kenabres, wrapped in cloth. He had found it where her letter was left on the northern pass. She hung it in her guardroom and polished it herself. When asked who had sent it, she told the sentries to mind their post.{/n}', requires=('terendelev.trickster.watch.letter_written',), forbids=()),
    p("{n}Kenabres's east-gate sentries learned that Terendelev played cards. They lost steadily. She insisted she no longer cheated, and made them count the coppers whenever she won.{/n}", requires=('terendelev.trickster.watch.what_you_are',), forbids=()),
    p('{n}Whatever the Worldwound did at the end, she did not go out with it. She was on the north turret at the hour of the dressing with the linen folded in its square, and when the Commander came up the stair she said, very drily, that she had known she would be, and then sat down rather suddenly on the stones and did not get up for some time.{/n}', requires=('terendelev.trickster.finale.asked', 'terendelev.committed'), forbids=('terendelev.trickster.guardian',)),
    p("{n}Before she left Drezen she had read the Wound's weather at the war table, wiping the blood from her nose afterward. From Kenabres she sent what warnings she could. The scouts still had to ride out and find what waited on the roads.{/n}", requires=('terendelev.trickster.watch.compass',), forbids=()),
    p("{n}She remembered that the Commander had refused her offered nightly readings. In Kenabres she watched the roads with her own eyes and listened for the sentries' reports.{/n}", requires=('terendelev.trickster.watch.not_a_map',), forbids=()),
    p('{n}The people of Kenabres who had knelt to her in the lower town went home, in time, to rebuild. Every festival after that, somebody climbed the new gate of Kenabres and tied a blue ribbon at the top of it, up where nobody could reach, and nobody would ever say who.{/n}', requires=('terendelev.trickster.watch.known_to_kenabres', 'engine.l12.kenabres_rebuilding'), forbids=()),
    p('{n}There was always a candle in her guardroom. On bad nights she went down to the east gate and sat with the watch until dawn. They argued about turnips and dice, and made room for her by the fire.{/n}', requires=('terendelev.trickster.watch.sat_up',), forbids=()),
    p('{n}The woman who fried bread by the lower gate went to her grave believing that the silver-haired widow from Kenabres had married the Commander of the crusade in the middle of her market, over a crock of honey. It was not strictly true. Nobody who had been there that evening ever corrected her.{/n}', requires=('terendelev.trickster.watch.kissed_in_the_market',), forbids=()),
    p("{n}Her letters from Kenabres asked about the wound and about who had been called when it bled. She still disliked hearing of the Commander's health from a stranger.{/n}", requires=('terendelev.trickster.watch.quarrel',), forbids=()),
    p('{n}She never did climb back up to the mountains. She said the view from the lower town had certain compensations, and when asked what they were, looked at the Commander, and did not answer.{/n}', requires=('terendelev.trickster.watch.mountains', 'terendelev.committed'), forbids=('terendelev.trickster.guardian',)),
    p('{n}In the second winter after the war she began to pray again, in Kenabres. The priest who passed her in the chapel heard the names of townsfolk, living and dead, and once, distinctly, a complaint about turnips.{/n}', requires=('terendelev.trickster.watch.faith',), forbids=()),
    p("{n}The silver at her collarbone stayed. Kenabres's gate watch learned to recognise her in the dark by the glint above her shirt.{/n}", requires=('terendelev.trickster.watch.scales_stayed',), forbids=()),
    p('{n}A traveller from Drezen brought Terendelev news of Irabeth: the knight had been heard singing on the wall again. Terendelev made him repeat the tune as well as he could. The east-gate sentries heard her humming it that night.{/n}', requires=('terendelev.trickster.watch.irabeth_message', 'crossroute.irabeth.available'), forbids=('irabeth_dead',)),
    p('{n}The Storyteller told of the dragon who died twice and came back beside her pyre at Iz. He remembered her kneeling among his books in a borrowed cloak, and the laugh that followed her thanks.{/n}', requires=('terendelev.trickster.watch.storyteller_thanked',), forbids=('storyteller.dead', 'storyteller.dead_delayed')),
    p('{n}Every winter she sent the Commander thick gloves from Kenabres. Her letters asked whether the cold had reached the fingers yet, and instructed that the gloves were to be worn, not admired. She remembered what the fire had taken.{/n}', requires=('terendelev.trickster.cost.bled_white',), forbids=()),
    p('{n}She never forgave the Lord of Locusts, and never pretended to. If the day came when he was cut down again, she said, she meant to be there, in whatever shape she had, and she meant it to be the last day.{/n}', requires=('terendelev.trickster.watch.deskari_vow',), forbids=()),
    p("{n}She often passed the cathedral's old site on her way to the gate. Once she stood there until the evening watch called her name, remembering the stranger she had told to come back tomorrow.{/n}", requires=('terendelev.trickster.watch.kenabres_told',), forbids=('engine.l12.kenabres_rebuilding',)),
    p("{n}When the Storyteller left his mortal body to serve the Lady of Graves, he took the memory of Terendelev's voice with him: her thanks, her laughter, and the rustle of her cloak as she rose from the dust beside his books.{/n}", requires=('terendelev.trickster.watch.storyteller_thanked', 'storyteller.dead_delayed'), forbids=('storyteller.dead',)),
    p("{n}When the Storyteller left his mortal body to serve the Lady of Graves, he took the memory of Terendelev's voice with him: her thanks, her laughter, and the rustle of her cloak as she rose from the dust beside his books.{/n}", requires=('terendelev.trickster.watch.storyteller_thanked', 'storyteller.dead_main'), forbids=('storyteller.dead_dlc',)),
    p('{n}A traveller from Drezen brought Terendelev news of Irabeth: the knight had been heard singing on the wall again. Terendelev made him repeat the tune as well as he could. The east-gate sentries heard her humming it that night.{/n}', requires=('terendelev.trickster.watch.irabeth_message', 'irabeth_dead', 'irabeth.trickster.returned', 'crossroute.irabeth.available'), forbids=()),
    p("{n}In Kenabres she kept a candle for the knight whose grave she had asked the Commander to find. She said the knight's name before the evening watch.{/n}", requires=('terendelev.trickster.watch.irabeth_grave_inquiry', 'irabeth_dead'), forbids=('irabeth.trickster.returned',)),
)

epilogue("guardian", '{n}Terendelev walked home to Kenabres in a borrowed cloak, with her boots worn through. A baker who had known her for forty years recognised her at the gate and brought her indoors before asking a single question.{/n} {n}She took a room by the east gate and kept its night watch with a pike. She healed whoever came to her. Among the changed streets she found familiar faces and learned the names of their children. The city had lost its dragon, and now its guardian was home.{/n} {n}Once a year the Commander received a short letter. It always ended: "The wound. Is it still open? Tell me the truth."{/n}',
         requires=(RETURNED, P + "guardian"), forbids=("sacrifice",), paragraphs=GUARDIAN_PARAGRAPHS, **SURVIVED)

epilogue("rest", '{n}The fire at Iz burned out. The crusaders raised a cairn over the bones. Travellers said the stones were warm in winter; scholars blamed the sun. None of them had stood beside the pyre.{/n}',
         requires=(RESTED,), forbids=(RETURNED,), paragraphs=(
    p('{n}Queen Galfrey gave leave for the cairn. Her knights laid the first stones.{/n}', forbids=("galfrey.dead", "galfrey.killed_by_commander", "galfrey.trickster.returned")),
    p('{n}The knights who had served Galfrey laid the first stones without waiting for a royal command.{/n}', any_groups=(("galfrey.dead", "galfrey.killed_by_commander", "galfrey.trickster.returned"),)),
))


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


# --- Shyka's page: the echo and the memory gap (Writer/handoffs/12-TRICKSTER-FORESIGHT.md §2.4a, §2.9) -----------------
# The echo (06 "Echo slots": proposed) is gated on the page and appended last at the ash of the late return: heat on the
# hand from someone else's branch, water carried to the wrong end of the fire. The gamble that follows is untouched.
# The gap is not optional: a Commander who sold the morning in the square to Shyka knows it only as told (12 §2.3), so the
# memory page reaches her words through that, and rejoins at her promise. The original choices are gated off, never removed.
from storylines import foresight as _foresight  # noqa: E402

_foresight.echo(REL, P + "late.the_wound_calls", "ride",
    "[Send the riders to the skull's jaw with the water skins.]",
    _foresight.variant('''{n}Heat on the back of your hand, before you are near enough to feel any: the dry, even heat of a hearth, not a pyre. It comes off a crumb from the back of Shyka's page, one that belongs to some other Commander: a dragon's skull burning in a square hung with bunting, gold bones, and the warm end of it at the jaw.{/n}
{n}So you send the riders to the jaw first, with every water skin you have, to cool a way in. The jaw end is cold ash and nothing. The water goes into it with a hiss like somebody laughing, and half of what the riders carried for the road home is gone before you understand that you are quenching the wrong end of the wrong fire.{/n}
{n}The warmth was never at the jaw. It is at the heart of the skull, where the small flame has not gone out.{/n}''',
        forbids=(_foresight.GONE_SQUARE,)),
    _foresight.variant('''{n}Heat on the back of your hand, before you are near enough to feel any: the dry, even heat of a hearth. A crumb from the back of Shyka's page: a dragon's skull burning in a square hung with bunting, gold bones, the warm end at the jaw. You sold that square to Shyka, or a piece of it, to pay for the page. The bunting is the only part you are sure of, and it is wrong.{/n}
{n}You send the riders to the jaw first anyway, with every water skin you have. The jaw end is cold ash and nothing, and half of what they carried for the road home hisses away into it before you call them off.{/n}
{n}The warmth was never at the jaw. It is at the heart of the skull, where the small flame has not gone out.{/n}''',
        requires=(_foresight.GONE_SQUARE,)),
    sense="touch", wrong="gold bones in a square hung with bunting; the warm end at the jaw",
    misstep="a wrong preparation spent: water carried to quench a fire that had to be reached", cost=("Materials", -50))

_foresight.gap(REL, P + "memory.square", (("scale", 0), ("no_scale", 0)), "square",
    '''{n}You know the festival square in Kenabres the way you know a story you have been told too often: bunting, fried dough, a crusader bleeding on the cobbles, an old prelate praying over the crusader and failing. Other people put it there for you afterwards. Where your own morning was there is a neat line of Shyka's handwriting, and you cannot get behind it.{/n}
{n}But you know what she said. Half of Kenabres heard her say it, and the half that lived has told it to you, word for word, as if it were still yours to keep.{/n}''',
    _foresight.GONE_SQUARE, choices=[c("[Say her words over to yourself.]", "promise")])


# eng7-l09 / E-Q7-26: sold-square callbacks on both earned restitution hosts.
for _host in (P + "bones.restitution", P + "bones.restitution_irabeth"):
    _foresight.gap(REL, _host, (("call", 0), ("call", 1)), "voice",
        '{n}The fire leans toward you. A voice comes out of it that has no throat to come from, hoarse with smoke and very tired.{/n} "Who calls me that? There is no Kenabres. There is only this place, and the task, and the dark between."',
        _foresight.GONE_SQUARE)
    _foresight.gap(REL, _host, (("shift", 0),), "wings",
        '{n}She looks down at the bones she came out of.{/n} "My wings are in that fire." {n}Her voice steadies.{/n} "Well. I came out of it, and they did not. I will take that bargain for now."',
        _foresight.GONE_SQUARE)
# end eng7-l09
# eng8-q8d: authored blood test in Chapter 3 Drezen, before the descent.
_eng8_test = next(s for s in SCENES if s['Id'] == P + 'wound.weeps')
_eng8_test.update(MinChapter=3, MaxChapter=3, Chapters=[3], Areas=[DREZEN])
for _eng8_node in _eng8_test['Nodes']:
    if _eng8_node['Id'] == 'areelu':
        # Keep the saved node; Chapter 3 has no future audience-hall memory.
        pass  # The saved node retains its Cue_0095-gated recollection.
    _eng8_node['Text'] = (_eng8_node['Text']
        .replace('The Abyss has no night, only a dimmer red. You wake in it', 'Drezen\'s bells wake you before dawn')
        .replace('On the dust of the Abyss itself', 'On a scrap of a cultist\'s Abyssal hide')
        .replace('The priests in the Abyss do not try.', 'The citadel\'s priests can only bind it.')
        .replace('lying in the red half-dark', 'lying in the first grey light')
        .replace('The Abyss mutters to itself beyond the pickets.', 'The watch changes beyond the citadel door.')
        .replace('you ride on into the red.', 'you return to the crusade\'s dispatches.'))
# end eng8-q8d

# eng8-q8f: authored royal-letter handover at either existing Terendelev contact.
# Her earned return and the Queen's existing availability guards remain mandatory.
import copy as _entry_copy
_royal_letter = next(s for s in SCENES if s["Id"] == P + "react.galfrey.letter")
_royal_letter.update(Entry='"You have a letter for me?"', ContactUnit=HUMAN,
                     InteractionHub=HUB, Areas=[DREZEN], Chapters=[5], Remote=False, ManualOnly=False)
_royal_letter.pop("Kind", None)
_royal_letter["Reaction"] = False  # A physical handover uses the existing hub-scene contract.
_royal_letter["Nodes"][0]["Speaker"] = "Narrator"  # Read her writing; do not summon the Queen as a speaker.
_royal_start = _royal_letter["Nodes"][0]
_royal_terminal = _entry_copy.deepcopy(_royal_start["Choices"][0])
_royal_start["Choices"][0]["Next"] = "royal"
_royal_start["Choices"][0]["Forbids"].append("galfrey.trickster.returned")
_royal_start["Choices"].append(c("Continue", "private", requires=("galfrey.trickster.returned",)))
_royal_letter["Nodes"].extend([
    nar("royal", '{n}The letter is sealed with the royal arms of Mendev, and written in a firm, old-fashioned hand.{/n}\n"Commander. I took my knights to Iz to grant rest to her soul and her body. It was my duty and I would do it again. You have undone it. I have asked the Inheritor whether I ought to be glad.\n"She has not answered. I have decided I am glad regardless, which is either faith or its opposite, and at my age I am no longer sure there is a difference.\n"She was our protector and our friend. See that you are hers."\n{n}It is signed with the one word, Galfrey, and nothing else: no title.{/n}', _entry_copy.deepcopy(_royal_terminal)),
    nar("private", '{n}Terendelev passes you a letter sealed with green wax. The hand is familiar.{/n} "I went to Iz with the crusade. To grant our friend rest was my duty. I did not expect to learn afterward that she lived. I have prayed over it, and I am glad. Give her my thanks for every watch she has stood. Deliver them quietly." {n}Beneath the last line is one name: Kitrane.{/n}', c("[Fold the letter and put it away.]")),
])
_royal_awning = _entry_copy.deepcopy(_royal_letter)
_royal_awning["Id"] += "_awning"
_royal_awning["InteractionHub"] = HUB_FB
_royal_awning["Requires"] = list(dict.fromkeys([*_royal_awning["Requires"], HUB_FAILED]))
_royal_letter["Forbids"] = list(dict.fromkeys([*_royal_letter["Forbids"], _royal_awning["Id"]]))
_royal_awning["Forbids"] = list(dict.fromkeys([*_royal_awning["Forbids"], _royal_letter["Id"]]))
SCENES.append(_royal_awning)
# end eng8-q8f


# Authored M26: a departed guardian mourns an unreturned Commander at home.
epilogue("guardian_sacrifice", '{n}The news reached Terendelev in Kenabres. She read the letter in her room by the east gate, then went down to relieve the sentry. She kept the whole night watch.{/n} {n}Afterward she put away the linen she had meant to send to Drezen. She still lit a candle before sleeping. When a child asked whom it was for, she answered, "Someone who came back for me."{/n} {n}She stayed in Kenabres. There were people there who needed her, and she had not finished keeping them.{/n}',
    requires=(RETURNED, P + "guardian", "sacrifice"), forbids=("trickster.commander_back",),
    paragraphs=(p("{n}She never regained her wings. She did not call that loss a debt the dead could pay.{/n}", requires=(LATE,)),))


# Round 2 authored receipts: disposal is performed, not merely promised.
HAL_MET = P + "hal_met"
BINDINGS.setdefault("SeenCues", {})[HAL_MET] = ["195ef1a822c1c144f80f3cd6d5669d63"]
HAL_LETTER = P + "watch.hal_refuge_delivery"
DESKARI_NOTICE = P + "watch.deskari_notice"
DESKARI_SETTLED = P + "watch.deskari_settled"
for _s in SCENES:
    if _s["Id"] in (P + "bones.restitution", P + "bones.restitution_irabeth"):
        _answer = next(nd for nd in _s["Nodes"] if nd["Id"] == "answer")
        _answer["Text"] += (' {n}Before the column leaves, the knights rake the last ribs into the fire. '
            'Terendelev watches until they crumble. She takes a handful of ash and scatters it across the rubble; '
            'the knights scatter the rest. Nothing is taken for a reliquary.{/n}')
    if _s["Id"] == P + "late.the_wound_calls":
        _after = next(nd for nd in _s["Nodes"] if nd["Id"] == "after")
        _after["Text"] += (' {n}Wrapped in your cloak, she waits while your soldiers break the last bones into the embers. '
            'She scatters the first handful of ash herself. They empty the skull and leave it to burn.{/n}')
    if _s["Id"] == P + "react.seelah.watch":
        _s["Nodes"][0]["Text"] = ('{n}Seelah catches your arm as you pass the practice ring.{/n} '
            '"The sentry at the sixth bell has been trying to tell me something without saying it. The north turret, eh?" '
            '{n}She grins.{/n} "At the festival in Kenabres I bought a pie for a hungry child. Terendelev caught me '
            'looking at it and asked whether the Inheritor starved her paladins. Then she bought another and laughed '
            'when I ate it before the child finished his." {n}Seelah glances up at the turret.{/n} '
            '"I heard that laugh again this morning. Tell her to come down for supper. There is room at our table."')
    if _s["Id"] == P + "react.irabeth.dressing":
        _s["Nodes"][0]["Text"] = ('{n}Irabeth intercepts the relief sentry at the stair, checks his bandaged wrist, '
            'and sends another knight up in his place.{/n} "Terendelev took his watch as well as her own. '
            'I have told her to eat before she takes a third." {n}She turns to you.{/n} '
            '"She borrowed my knife to cut a shirt into dressings. I want the knife back. And if you keep her on that '
            'turret until dawn again, send word to the officer of the watch. He needs a relief, not the details."')
    if _s["Id"] in (P + "epilogue.watch", P + "epilogue.late", P + "epilogue.debt", P + "epilogue.guardian"):
        _pars = _s["Nodes"][0]["Paragraphs"]
        # Existing letter receipt remains sufficient; knowledge only changes the destination.
        _mountain = _pars[9]
        _mountain["Forbids"].append(HAL_LETTER)
        _home = _s["Id"] == P + "epilogue.guardian"
        _pars.append(p('{n}The courier left her letter at the old refuge. Months later a traveller brought back '
            'a gold scale wrapped in the same sheet, with every crossing-out carefully preserved. '
            + ('Terendelev hung it in her room by the east gate of Kenabres.' if _home else
               'Terendelev hung it beside the hearth in Drezen.') +
            ' She laughed when she unfolded the sheet, and would not explain why.{/n}',
            requires=(P + "watch.letter_written", HAL_LETTER)))
        _pars[24]["Text"] = ('{n}She had asked to face Deskari again. Before the army left, she counted the '
            'wounded who could not march and chose to remain with them. She released the Commander from the escort '
            'promise herself. His name still made her fingers tighten on her pike.{/n}')
        _pars[24]["Requires"].append(DESKARI_SETTLED)
        _pars.append(p('{n}The Commander had promised word if Deskari appeared again. She watched for the dispatches '
            'with the other sentries; no place in the marching column had been promised.{/n}',
            requires=(DESKARI_NOTICE,)))
        if _s["Id"] == P + "epilogue.watch":
            _s["Nodes"][0]["Text"] += (' {n}After her visit to Kenabres, she came back to Drezen with worn boots '
                'and a parcel of fried bread. She left the pike by the door and caught the Commander by the collar. '
                '"The east gate has its watch. Tonight you have me."{/n}')
        if not _home:
            _pars[18]["Text"] = ('{n}She still spoke of the mountain winds. Then she would come down from the '
                'turret, unfasten her cloak beside the Commander, and draw their chair nearer the fire with her foot.{/n}')
            # The shirt is a consequence of the night actually played, never of rescue or an oath alone.
            _pars.append(p('{n}The sixth-bell sentry remembered the missing shirt long after the war. '
                'When the relief found them on the turret again, Terendelev held up a roll of linen. '
                '"Provisioned this time," she said. The sentry went down. She caught the Commander by the collar and kissed them.{/n}',
                requires=(P + "night.seen", COMMITTED)))


# A skipped farewell does not silently collect the escort debt in an ending.
for _s in SCENES:
    if _s["Id"] in (P + "epilogue.watch", P + "epilogue.late", P + "epilogue.debt", P + "epilogue.guardian"):
        _pars = _s["Nodes"][0]["Paragraphs"]
        _pars[24]["Forbids"].append(DESKARI_NOTICE)
        _pars.append(p('{n}The army marched without settling her request to face Deskari. '
            'When the Commander next spoke of Iz, she asked why the promised horse had never come. '
            'She heard the answer standing, with her hand closed on the pike.{/n}',
            requires=(P + "watch.deskari_vow",), forbids=(DESKARI_NOTICE, DESKARI_SETTLED)))
    if _s["Id"] == P + "epilogue.guardian":
        _s["Nodes"][0]["Text"] += (' {n}At dusk she returned from the healing room to the east gate. '
            'The ribbon-seller had left a blue length on the sill. Terendelev took it up to the watch, '
            'tied it where the street could see it, and called the relief sentry by name.{/n}')
