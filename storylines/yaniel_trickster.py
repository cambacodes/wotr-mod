"""Yaniel on the Trickster path: "The swap: sword for shackle" (Writer/handoffs/trickster/yaniel.md for the canon research;
the binding plan is 11-ROSTER-PLAN-2 §2, Yaniel block and build sheet, rewritten 2026-09-30 (R5). It supersedes the spec's
palm-back, husk state, stockade theft, bout and chapel oath; YAN-01 is retired to reference/retired-drafts).

Canon (TrueYaniel_MidnightFane_dialog 009a448c, Chapter 3):
- a half-elf paladin of Iomedae, Areelu's prisoner and then one of Minagho's "collector's items" (Cue_0021 7db27044);
  "not a day went by that I didn't try to escape or kill one of my guards" (Cue_0023 e8756562);
- handed Radiance, she takes it (Cue_0008 cbf1a11c). With RadiancePlus2 in the pack her touch remakes it as the +4 Holy
  Avenger (Cue_0017 9f7b77ac) and she gives it back with a charge: "its journey must end in the black heart of Deskari...
  Radiance will fulfill its destiny in your hands" (Cue_0035 efb1ee54, the hope branch). Otherwise: "I doubt I'll be able
  to raise this sword again" (Cue_0027 536ceec8, the doubt branch). Both reopen AnswersList_0010 8b4733e3;
- she leaves for the Hand of the Inheritor (Cue_0012 2e27a01b) and Yaniel_Freed 7c552641 starts. Off the Angel path she
  has no later native unit or line, so her Trickster future is wholly authored;
- the kill is the player's own choice (Answer_0031, Answer_0009, Answer_7; Cue_0013 "the light departs them forever",
  Yaniel_Killed d6579be8). It stands (coordinator ruling: canon death stays only where the player chose it), and
  `yaniel.killed.latched` closes every scene here. Never freeing her is an entry condition (matrix user_decision);
- Radiance sings at Deskari's voice at Iz if a form she remade is in the pack (DeskariFight/Cue_0036 221a9592).

Device (a burden swap, no mythic power): she hands the sword back; the Commander closes her fingers on the hilt again and,
with the other hand, works the pin out of the cut manacle still on her wrist and keeps it. The argument is Diplomacy DC 20,
made against her own words. Success: she keeps Radiance, removed from the Commander for real by a whitelisted RemoveItem
of the form held (`carries`). Failure: she will not take the sword, and lets the Commander keep the iron on an oath sworn on
Radiance to carry it to Deskari's heart (`judges`, `cost.oath_deskari`). A Chapter 5 remote visit on the walls does the same
swap if the Fane passed without it (`late.wall`, `cost.late`), before or after Iz. Cost: the shackle for good
(`cost.shackle_kept`), plus Radiance itself or the oath. Commit: she proposes the trade-back; the yes is that neither
trades. Recovery from a no is a joint act: the night vigil at her niche.

Authored, and labelled as such on the page: the statue's journey from Nerosyan to Drezen and its niche in the old east gate
tower, her watches on the east wall, her ride to Iz with the crusade, the sexton.

Path fit (ROUTE-BRIEF-R, v1): every scene is T (11 §2 "v1: every scene is T"); the v2 N-fit paths are Angel, Aeon, Azata,
Legend and Gold Dragon, written later (14-PATH-FIT.md). The courtship beats live in yaniel_walls.
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "yaniel"
Y = "yaniel.trickster."

UNIT = "d914111e83e44194db99ab91d8c04632"            # Units/.../MidnightFane/Yaniel (the true Yaniel; the Fane unit)
PORTRAIT_GUID = "c745f6e4994645f7873fca8ae902c13e"   # BCT_TrueYaniel (the unit's m_Portrait; fallback until custom art ships)
DREZEN = "2570015799edf594daf2f076f2f975d8"
TALK = "8b4733e32e9112a479f8af49c39e3c49"            # TrueYaniel/AnswersList_0010 (the talk hub after the handover)
DOUBT_CUE = "536ceec8863161f489ef28ddd9c51845"       # Cue_0027 "I doubt I'll be able to raise this sword again" (clean)
HOPE_CUE = "efb1ee540ea049743bd146397641bb9b"        # Cue_0035 "...the black heart of Deskari..." (clean)
TO_HAND = "2e27a01bb56b6ea4587a46d30a0f9ccc"         # Cue_0012 "Our golden-winged angel is here!... I will go to him now."
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"      # CompanionDialogues/Seelah/AnswersList_0003

STARTED = "yaniel.started"
CLOSED = "yaniel.closed"
COMMITTED = "yaniel.committed"

# Native reads (bound in integrate(); the Radiance forms and the latches come from trickster_world).
FREED = "yaniel.freed.latched"
KILLED = "yaniel.killed.latched"
CH5 = "yaniel.ch5.latched"
DOUBT = "yaniel.fane_doubt"
HOPE = "yaniel.fane_hope"
SANG = "yaniel.radiance_sang"
HELD = "yaniel.radiance_held"                        # Derived over every form (trickster_world)
MW, P1, P2 = "yaniel.radiance_masterwork", "yaniel.radiance_plus1", "yaniel.radiance_plus2"
HA4, HA6 = "yaniel.radiance_ha4", "yaniel.radiance_ha6"
ITEMS = {MW: "3b2df06a731030d49a1240b763cb6069", P1: "de1fc233ad934a0a93a17ebed3ec0cfb",
         P2: "6a80e629e9a5ca74da1dabc2984bba3b", HA4: "0ff011d62af77e9428e12ac08f63709e",
         HA6: "cf5c1a507825f184dacbc3abe14b9db1"}
IZ = "iz.done"
TOLD_STAUNTON = "yaniel.told_staunton"               # Answer_0029: the Commander told her Staunton and Joran went over and died
TOLD_STATUE = "yaniel.told_statue"                   # Answer_0043: "...your cold, stone statue"
SEELAH_SISTER = "yaniel.seelah_sister"               # Cue_0003: Seelah's "Sister!" at the Fane
UNMASKED = "yaniel.areelu_unmasked"                  # FakeYaniel_ToAreelu/Cue_0001 "Forgive me this little masquerade."
FAKE_FREED = "yaniel.fake_freed"                     # FakeYaniel_ToAreelu/Cue_0006 "The 'Yaniel' you freed from the dungeon..."
FAKE_REFUSED = "yaniel.fake_refused"                 # FakeYaniel_ToAreelu/Cue_0014 "...why did you refuse to set the poor prisoner free?"
SEELAH_DEAD, SEELAH_GONE, SEELAH_BACK = "seelah_dead", "seelah_gone", "seelah.trickster.returned"

# The route.
SWAPPED = Y + "swapped"               # the Commander holds her shackle (every device outcome)
CARRIES = Y + "carries"               # she keeps Radiance; the Commander's form was removed
HANDED_LATE = Y + "handed_after_iz"   # the late swap on the walls was made after Iz: she never carried it there
HOLY = Y + "carries_holy"             # she keeps the Holy Avenger her touch made (Cue_0017): only it can sing at Iz
JUDGES = Y + "judges"                 # she would not take it: the Commander carries it, under oath
OATH = Y + "cost.oath_deskari"        # the oath sworn on Radiance: Deskari's heart (Iz, or the Threshold rift after Iz)
LATE = Y + "cost.late"                # the swap was made on the walls of Drezen in Chapter 5, not in the Fane
SHACKLE = Y + "cost.shackle_kept"     # the iron stays with the Commander for good (the commit and the vigil)
FANE_REFUSED = Y + "fane_refused"     # at the Fane the Commander gave the iron back rather than swear
SWORD_LOST = Y + "sword_lost"         # the late oath was sworn with no Radiance in the pack: find it, then carry it
WHY_CANT = Y + "why.cannot_put_back"  # "So you can't put it back on."
WHY_BACK = Y + "why.come_back"        # "So you have to come back for it."
RETURNED = Y + "returned"             # she came to Drezen and stayed
CUFF_WORN = Y + "cuff_worn"           # Chapter 4: the Commander closed the iron on the Commander's own wrist
CUFF_PACKED = Y + "cuff_packed"
VERDICT = Y + "verdict"
OATH_BROKEN = Y + "oath_broken"
OATH_BELIEVED = Y + "oath_believed"   # nothing in the pack and no song, and she took the Commander's word for Iz
OATH_THRESHOLD = Y + "oath_threshold"  # the late oath sworn after Iz: the Threshold, judged there, not at the verdict
OATH_PENDING = Y + "oath_pending"      # the verdict found the Threshold oath not yet due
OATH_UNPROVEN = Y + "oath_unproven"    # the sword is on the hip but she could not believe it went to Iz
OATH_STANDS = Y + "oath_stands"       # the verdict: a form in the pack, the song heard at Iz, or her taking the Commander's word
DECLINED = Y + "declined"             # the Commander gave her back the shackle
LEFT_FREE = Y + "left_free"           # the Commander left her to her vigil (sets the ClosedFlag)
VIGIL = Y + "vigil_stood"
NICHE = Y + "niche_seen"
MORNING = Y + "morning_seen"
SEELAH_BLESSED = Y + "seelah_blessed"
MINAGHO_SEEN = Y + "minagho_seen"
MINAGHO_TOLD = Y + "minagho_told"
MINAGHO_SECRET = "trickster.secret.yaniel_minagho"
# Courtship beats (yaniel_walls), read by the pages and the Last Call coda.
B_WALLS, B_STATUE, B_STAUNTON = Y + "beat.walls", Y + "beat.statue", Y + "beat.staunton"
B_AREELU, B_BOUT, B_ROAST = Y + "beat.areelu", Y + "beat.bout", Y + "beat.roast"
B_NIGHT, B_CHURCH, B_REFUGEE = Y + "beat.night", Y + "beat.church", Y + "beat.refugee"
B_RAID, B_PRAYER = Y + "beat.raid", Y + "beat.prayer"
HUSK_FREED, HUSK_BOUGHT, HUSK_LEFT = Y + "husk_freed", Y + "husk_bought", Y + "husk_left"   # Chapter 4, the block in Alushinyrra
STATUE_LIED = Y + "statue_lied"       # "It's a good likeness."
# The Commander's own reciprocal choices in the courtship; the yes needs one of them (review r2 BEL).
DRAWN_WALLS, DRAWN_BITE, DRAWN_TREE = Y + "drawn.walls", Y + "drawn.bite", Y + "drawn.tree"
DRAWN = Y + "drawn"                   # Derived: any of them

RELATIONSHIP = dict(
    Title="Sword for Shackle",
    Description=("Yaniel, the paladin of Drezen, spent the better part of a century on a hook in Minagho's fane. I freed her "
                 "and handed her back her sword. Then I took the one thing she had left from the pit, and now one of us is "
                 "carrying the other's burden."),
    Objective="See what Yaniel does with the trade",
    Guidance=("On the Trickster path, when Yaniel gives Radiance back to you in the Midnight Fane, do not take it. Keep her "
              "cut manacle instead, and make her keep the sword. If the Fane passes without it, she will come to the walls of "
              "Drezen in Chapter 5. Killing her in the Fane ends this for good."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[KILLED], FailureFlags=[], UnavailableOverrides={},
    TricksterAccess={
        "doubt": dict(detect=["!" + KILLED], device=Y + "fane.swap", returned=SWAPPED),
        "hope": dict(detect=["!" + KILLED], device=Y + "fane.swap_hope", returned=SWAPPED),
        "late": dict(detect=["!" + KILLED], device=Y + "late.wall", returned=SWAPPED),
    },
)

DERIVED = {
    DRAWN: [[DRAWN_WALLS], [DRAWN_BITE], [DRAWN_TREE], [Y + "raid_kiss"], [Y + "statue_scars"], [Y + "night_stayed"]],
    # 05 §2.5 voice note: she joins the table as a soldier who keeps her own watch; she stands where she chooses.
    "yaniel.harem.voice.keeps_her_own_watch": [[COMMITTED]],
}
LATCHES = {CH5: ["irabeth.chapter_five"]}             # the Chapter05 etude (5b01aa69), bound by irabeth_independent
SEEN_CUES = {DOUBT: [DOUBT_CUE], HOPE: [HOPE_CUE], SANG: ["221a9592527d8b5498346c55549dd2be"],
             SEELAH_SISTER: ["fd994112dc80453a954e9486f4668d36"], UNMASKED: ["7418d421e3af812439ea312991c37147"],
             FAKE_FREED: ["b618fff15d921894e84b9b2fe9efaa39"], FAKE_REFUSED: ["f1a82798065c27b45aa1d17d9db80dc6"]}
SELECTED = {TOLD_STAUNTON: "09d9caa56d1dd4743bb04f8e39ae7459", TOLD_STATUE: "8f635c7b16eadd44b8a28aac5e937e37"}

# Path fit (ROUTE-BRIEF-R 2026-09-29, v1): T = device or Trickster-only; N-all = any path; N-fit = the fitting paths.
PATH_FIT = {}


def tag(scene_id, fit="T"):
    PATH_FIT[scene_id] = fit


def yi(id, text, *choices, **kw):
    """Yaniel inside the Fane dialog: the Fane unit's own name and portrait (E14f)."""
    return n(id, "Yaniel", text, *choices, speaker_unit=UNIT, **kw)


def yn(id, text, *choices, **kw):
    """Yaniel on a rest-delivered page (her portrait)."""
    return n(id, "Yaniel", text, *choices, portrait="Yaniel", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def visit(id, title, nodes, requires, forbids=(), delay=24, kind="visit", chapters=(5,), areas=(DREZEN,), **extra):
    """A rest-delivered scene: she is there (visit), or her letter is (letter). Drezen visits need the Commander in Drezen."""
    extra = dict(extra)
    if areas:
        extra["Areas"] = list(areas)
    SCENES.append(scene(id, title, "Yaniel", min(chapters), "", nodes, requires=tuple(dict.fromkeys(requires)),
                        forbids=tuple(dict.fromkeys((KILLED, CLOSED) + tuple(forbids))), delay=delay, last=max(chapters),
                        Relationship=REL, Chapters=list(chapters), Remote=True, Kind=kind, **extra))
    tag(id)


def removal(text, flags, forms, fallback=None, requires=(), forbids=(), **kw):
    """One terminal sibling per Radiance form she can be holding: each removes exactly that form (whitelisted RemoveItem),
    and each gates on its own InventoryItems key; the later siblings forbid the earlier forms."""
    out = []
    for i, form in enumerate(forms):
        extra = (HOLY,) if form in (HA4, HA6) else ()   # only the forms her touch remade sing at Deskari's voice
        out.append(c(text, flags=tuple(flags) + extra, requires=(form,) + tuple(requires), forbids=tuple(forms[:i]) + tuple(forbids),
                     remove_item=ITEMS[form], **kw))
    if fallback:
        # No form of hers in the pack (a state the native dialog cannot produce here): nothing to hand over, so her refusal.
        out.append(c(text, fallback, forbids=tuple(forms)))
    return out


# --- 1. The Midnight Fane (T): the swap, inline on her talk hub ------------------------------------------------------------

GO_TO_HAND = '"The Hand of the Inheritor is holding the far end of the fane. Go to him."'


def _fane(sid, title, cue, seen, forms, entry, opening, argument, kept_nodes, oath_opening):
    """Both Fane branches share the shape: the swap, the argument, and three endings, all into her native farewell."""
    nodes = [
        nar("start", opening,
            c("[Work the pin out of the cuff.]", "cuff"),
            c("[Let go, and take the sword.]", abort=True)),
        yi("cuff", '''{n}The pin comes on the third twist. The cuff opens with a sound like a knuckle cracking, and then it is in your fist: two fingers of rough iron, one sheared link of chain still hanging from its eye, warm from her. Her wrist is bare. Under the place where it sat the skin is white and hard as a heel.{/n}
{n}She stares at the white band. Then at your hand.{/n} "That is mine." {n}Her voice has gone very quiet, the way a soldier's does before she hits someone.{/n} "The only thing in this pit that was ever mine. Give it back."''',
            c(argument, check=dict(Skill="CheckDiplomacy", DC=20, Success="kept", Failure="oath")),
            c("[Give her the cuff, and take the sword.]", abort=True)),
        *kept_nodes,
        yi("kept_why", '''{n}She turns the sword a little, so the light of the rift runs down the fuller, and looks at you along the blade.{/n}
"You understand what you are doing? This is not a sword a person lends. The Church will want it back. Every chaplain in Mendev will want it back, and so will half the knights, and some of them will ask nicely." {n}Her eyes go to the iron in your fist.{/n} "And you take a husk's cuff in trade. That is a thief's bargain, stranger. What do you want with it?"''',
            c('"So you can\'t put it back on."', "kept_cannot", flags=(WHY_CANT,)),
            c('"So you have to come back for it."', "kept_back", flags=(WHY_BACK,))),
        yi("kept_cannot", '''"Put it back on." {n}She says it slowly, as if you had named a sin she had not known she had.{/n}
"Every night in this place I told myself I would not miss it. And the Hand of the Inheritor will take it off me, and some kind sister in a white apron will throw it in the midden, and some night in a good bed I will wake with my wrist cold and go looking for it." {n}Her mouth twists.{/n} "You have seen that before, have you? Someone who went back for their chain?"
{n}She does not wait for an answer. She shifts the sword to her shoulder, where it sits as if it had never been anywhere else.{/n} "Keep it, then. Keep it well away from me."''',
            *removal(GO_TO_HAND, (SWAPPED, CARRIES), forms, fallback="oath", native_next=TO_HAND)),
        yi("kept_back", '''{n}She barks, once, like a sergeant hearing a recruit's excuse. It might be a laugh.{/n}
"A hostage. You took a hostage off a woman you just cut down from a hook." {n}She weighs the sword in her hand, then weighs you.{/n} "You are a very peculiar sort of crusader, whoever you are. Minagho kept me for a trophy. Areelu kept me for a specimen. Nobody ever kept a piece of me so that I would have to come and fetch it."
"Very well. I will come and fetch it. And when I do, I will want to see what else you have been keeping, and how."''',
            *removal(GO_TO_HAND, (SWAPPED, CARRIES), forms, fallback="oath", native_next=TO_HAND)),
        yi("oath", oath_opening,
            c('[Lay your hand flat on the blade.] "I swear it on Radiance. Deskari\'s heart, and nowhere short of it."', "sworn"),
            c("[Give her back the cuff.]", "refused")),
        yi("sworn", '''{n}Her hand comes down over yours on the steel, callus on callus. Radiance is cold under both of them.{/n}
"Then it is sworn, and I heard it, and so did She." {n}She lets go.{/n} "Carry it, stranger. Carry it where it has to go. I will be watching your hands. I have nothing else left to watch."
{n}She looks at the iron in your other fist a long while, the way you might look at a house you grew up in, burning. Then she turns her face away from it.{/n}''',
            c(GO_TO_HAND, flags=(SWAPPED, JUDGES, OATH), native_next=TO_HAND)),
        yi("refused", '''{n}She takes it without a word and does not put it back on. She hooks it through her belt instead, beside a knife she took off a dead husk-keeper an hour ago, and pats it once, as if to be sure it is there.{/n}
"There," {n}she says, without heat.{/n} "Now we both know what we will and will not carry."''',
            c(GO_TO_HAND, flags=(FANE_REFUSED,), native_next=TO_HAND)),
    ]
    SCENES.append(scene(sid, title, "Yaniel", 3, entry, nodes, requires=("trickster", seen),
                        forbids=(KILLED, SWAPPED, FANE_REFUSED, CLOSED), last=3, Relationship=REL, AnswerLists=[TALK],
                        NativeReturnCue=cue, EntryMythic="PlayerIsTrickster", TricksterDevice=True,
                        TricksterState="doubt" if cue == DOUBT_CUE else "hope"))
    tag(sid)


_fane(Y + "fane.swap", "Sword for shackle", DOUBT_CUE, DOUBT, [MW, P1],
      "[Close her fingers back around the hilt.]",
      '''{n}She holds the sword out to you, hilt first. You do not take it. You put your hand over hers instead and fold her fingers back around the grip, one at a time, the way a surgeon folds a dying man's hand around his own sword so that he will be found holding it. She lets you. She is too surprised to do anything else.{/n}
{n}Her other wrist is still in iron: a husk's manacle, crude and thick, one link of the chain that held her to the hook still hanging from its eye where somebody sheared it. The pin is a lump of soft metal hammered flat. Minagho never needed a good lock. Nobody who hung here was ever meant to leave.{/n}
{n}Her eyes are on the sword. Your free hand is on the pin.{/n}''',
      '[Diplomacy] "No. You keep the sword, and I keep this. You said you couldn\'t raise it. You just raised it."',
      [
          yi("kept", '''{n}She looks down at Radiance in her own two hands. Her knuckles have gone white on the grip. The blade does not glow, not the way the songs say it did; it does not need to.{/n}
"I did," {n}she says.{/n} "I did, didn't I."
{n}A dry sound comes out of her that is nearly a laugh.{/n} "Seventy-odd years in this pit, and the first thing I do with my hands is lie with them. I said I would never lift it again, and I was holding it up at your face like a torch." {n}She draws a long breath through her nose.{/n} "Iomedae forgive me. I am out of practice at telling the truth. Nobody down here ever wanted it."''',
             c("Continue", "kept_why")),
      ],
      '''{n}She does not move for the space of three breaths. Then, very carefully, as though it were made of thin glass, she lays the sword across your forearms and takes her hands away.{/n}
"No. You are very quick, stranger, and very kind, and you are wrong. Hands that have been a demon's plaything do not get to hold that. Not yet. Perhaps not ever."
{n}Her eyes drop to the iron in your fist, and something moves under her face and is put away again.{/n} "But you want that so badly, keep it. On one condition. Swear to me, here, on Radiance, that you will carry this sword to the black heart of Deskari, and not sell it on the way, and not hang it on a wall. Then the iron is yours. Otherwise give it back, and let me carry my own."''')

_fane(Y + "fane.swap_hope", "Worthy hands", HOPE_CUE, HOPE, [HA4, P2],
      "[Put the shining sword back into her hands.]",
      '''{n}The light has not gone out of the blade. It still breathes, soft and gold, as if it had woken and did not yet trust the room. She holds it out to you hilt first, as she said she would, and you do not take it. You fold her fingers back around the grip instead, one at a time, and the glow brightens under both your hands and then settles, like a dog that has found the right lap.{/n}
{n}Her other wrist is still in iron: a husk's manacle, crude and thick, one link of the chain that held her to the hook still hanging from its eye where somebody sheared it. The pin is a lump of soft metal hammered flat. Minagho never needed a good lock. Nobody who hung here was ever meant to leave.{/n}
{n}Her eyes are on the sword. Your free hand is on the pin.{/n}''',
      '[Diplomacy] "You said it belongs in worthy hands. Yours were first. I\'ll keep this instead."',
      [
          yi("kept", '''{n}She looks at the sword in her hands for a long breath, and Radiance looks back, if a sword can: the glow gathers along the edge and lies there, warm and content.{/n}
"Mine were first," {n}she says.{/n} "Mine were first, and then they were Minagho's, and then they were nothing's for seventy years." {n}She turns the blade so the light runs along it.{/n} "It knew me. I told you it was an instinct that it would go to Deskari in your hands. It was an old woman's instinct, from a pit. The sword has a better one."
{n}She swallows.{/n} "Iomedae forgive me. I was giving it away because I was afraid to be the one who failed it twice."''',
             c("Continue", "kept_why")),
      ],
      '''{n}She does not move for the space of three breaths. The glow along the blade dims, as if the sword were listening. Then, very carefully, she lays it across your forearms and takes her hands away.{/n}
"No. I said what I said, and I meant it. It is going to Deskari's heart, and it is going in hands that have not hung on a hook. Yours, stranger. Not mine. Not yet."
{n}Her eyes drop to the iron in your fist, and something moves under her face and is put away again.{/n} "But you want that so badly, keep it. On one condition. Swear to me, here, on Radiance, that you will carry it to the black heart of Deskari, and not sell it on the way, and not hang it on a wall. Then the iron is yours. Otherwise give it back, and let me carry my own."''')

# The hope branch's own reply to the swap: the sword has just woken for her.
for _node in SCENES[-1]["Nodes"]:
    if _node["Id"] == "kept_why":
        _node["Text"] = ("{n}The glow runs up the blade and back down, as if the sword were stretching after a long sleep.{/n} "
                         "\"You understand what you are doing? It knew me. It lit for me the way it has not lit for anybody in seventy "
                         "years, and you are telling me that makes it mine. The Church will want it back. Every chaplain in Mendev will "
                         "want it back, and half the knights, and some of them will ask nicely.\" {n}Her eyes go to the iron in your "
                         "fist.{/n} \"And you take a husk's cuff in trade for a holy sword that has just woken up. That is a thief's "
                         "bargain, stranger. I know a thief's bargain when I see one. What do you want with it?\"")

# --- 2. The walls of Drezen (T): the late swap, Chapter 5, if the Fane passed without it ---------------------------------------

LATE_FORMS = [HA6, HA4, P2, P1, MW]
SWAP_LATE = '[Diplomacy] "You came up here to look at the city you held. Hold it again."'

late_nodes = [
    nar("start", '''{n}The sentry on the east tower tells you, a little too loudly, that there is a woman on his wall who is not on his roster, and that she has been there since the bell before dawn and will not come down. She is standing at the old gate tower where the parapet is broken, looking out over the ash toward the Wound: a lean, gray-headed half-elf in a borrowed crusader's cloak, bareheaded in the wind, with a husk's iron cuff still on her left wrist and one sheared link of chain swinging from it.{/n}''',
        c("Continue", "tried", requires=(FANE_REFUSED,)),
        c("Continue", "fresh", forbids=(FANE_REFUSED,))),
    yn("tried", '''{n}She hears your boots on the stair and does not turn around.{/n} "The quick hands from the Fane," {n}she says.{/n} "You tried to rob me once, in the dark, with an angel watching. Don't look like that; I know a robbery when one is done to me. I have had a great deal of practice."
{n}She rattles the cuff against the stone.{/n} "I kept it. You were right about that much, whatever else you were playing at. I have tried to leave it off three times since, and three times I have gone back for it. That is a thing I would not say to a priest."''',
       c("Continue", "wall")),
    yn("fresh", '''{n}She hears your boots on the stair and turns her head, not her body, the way a sentry does who has decided you are not worth turning around for.{/n} "Commander," {n}she says.{/n} "They told me in the square that is what you are now. The one who cut me down in the Fane and gave me back my sword, and then took it back again, very politely, and pointed me at an angel." {n}Her mouth twitches.{/n} "I have been walking for a long time to come and look at you."''',
       c("Continue", "wall")),
    yn("wall", '''{n}She lays her palm flat on the broken parapet.{/n} "This gate. The day the city fell I stood here with a hundred refugees behind me and a demon for every one of them coming up the road. I held it until the last cart was through. Then I held it a little longer, because I was young and stupid and thought someone might come back for me."
"Nobody came. Minagho came." {n}She takes her hand off the stone and looks at the cuff on her wrist, and then, deliberately, at your hands.{/n} "I came up here to see whether I could stand on it without being sick. I can. I am not sure it is the victory I hoped."''',
       c("[Take her wrist and work the pin out of the cuff.]", "cuff_sword", requires=(HELD,)),
       c("[Take her wrist and work the pin out of the cuff.]", "cuff_empty", forbids=(HELD,)),
       c('"Then stand on it a while longer. I\'ll come back."', abort=True)),
    yn("cuff_sword", '''{n}She lets you take her wrist. She even holds it still. The pin fights you longer than it would have in the Fane; she has been hammering it back in every night, you realise, and the soft metal is mushroomed flat. It comes. The cuff drops into your palm, warm, with the link swinging.{/n}
{n}Before she can say anything you draw Radiance and put the hilt in the hand you have just emptied.{/n}
"What is this?" {n}Her fingers have closed on the grip by reflex. She looks at them as if they belonged to somebody else.{/n} "Commander. What is this?"''',
       c(SWAP_LATE, check=dict(Skill="CheckDiplomacy", DC=20, Success="late_kept", Failure="late_oath")),
       c("[Take the sword back, and give her the cuff.]", abort=True)),
    yn("late_kept", '''{n}She looks down the length of the blade, along the parapet, over the ash to the Wound, and back again. Her grip shifts on the hilt, once, the way a hand settles on a tool it knows. The wind catches her cloak.{/n}
"Hold it again." {n}Her voice has gone hoarse.{/n} "Seventy years they told me this city was a demon pen, and they were right, and now it is not, and you want me to stand on its wall with its sword as though none of it happened in between."
{n}She laughs, a short, cracked sound.{/n} "All right. Iomedae help me, all right. Keep my iron, then, you thief. Keep it well. I will be up here every night making sure you have not sold it."''',
       *removal("[Let go of the hilt.]", (SWAPPED, CARRIES, LATE), LATE_FORMS, forbids=(IZ,)),
       *removal("[Let go of the hilt.]", (SWAPPED, CARRIES, LATE, HANDED_LATE), LATE_FORMS, fallback="late_oath", requires=(IZ,))),
    yn("late_oath", '''{n}She holds it for the space of three breaths. Then she turns it, carefully, and puts it back across your hands.{/n}
"No. That is a sword for someone who has not spent seventy years on a hook, and I will not have it said that the first thing Yaniel did on the walls of Drezen was take the crusade's best blade off its Commander." {n}Her eyes go to the cuff in your fist.{/n} "But keep that, since you are so fond of it. On one condition."''',
       c("Continue", "late_iz", forbids=(IZ,)),
       c("Continue", "late_rift", requires=(IZ,))),
    yn("late_iz", '''"Swear to me on Radiance that you will carry it to the black heart of Deskari. They say in the square the crusade marches for Iz; they say he is there. Take it there. Do not sell it on the way. Do not hang it on a wall. Then the iron is yours."''',
       c('[Lay your hand flat on the blade.] "I swear it. Iz, and Deskari\'s heart."', "late_sworn", flags=(SWAPPED, JUDGES, OATH, LATE)),
       c("[Give her back the cuff.]", abort=True)),
    yn("late_rift", '''"They tell me in the square you have already been to Iz, and that the demon lord there will not be bothering anyone for a while. Good. I was not there to see it, so I will not swear to what I did not see." {n}Her jaw sets.{/n} "But the hole he tore in the world is still open, and his filth still comes up out of it. Swear to me on Radiance that you will carry it to the Threshold, to the heart of his Wound, and not stop short of it. Then the iron is yours."''',
       c('[Lay your hand flat on the blade.] "I swear it. The Threshold, and the heart of his Wound."', "late_sworn", flags=(SWAPPED, JUDGES, OATH, LATE, OATH_THRESHOLD)),
       c("[Give her back the cuff.]", abort=True)),
    yn("late_sworn", '''{n}Her hand comes down over yours on the steel. It is a hard hand, and cold from the wall.{/n}
"Sworn," {n}she says,{/n} "and I heard it, and so did She. I am going to stay in this city a while, Commander, and I am going to watch your hands."''',
       c("[Let her go back to her watch.]")),
    yn("cuff_empty", '''{n}She lets you take her wrist. The pin fights you longer than it would have in the Fane; she has been hammering it back in every night, you realise, and the soft metal is mushroomed flat. It comes. The cuff drops into your palm, warm, with the link swinging.{/n}
{n}She looks at your belt, where a sword ought to be, and at your back, and at your hands.{/n} "You are not carrying it." {n}Her voice is quite level.{/n} "Radiance. The sword I put in your hands. Where is it, Commander?"''',
       c('"Not here. It\'s safe."', "empty_oath"),
       c('"Gone. It\'s gone."', "empty_oath")),
    yn("empty_oath", '''{n}Something goes out of her shoulders. She looks out at the ash for a while.{/n}
"Then here is what you will do, since you want my iron so much." {n}She turns back.{/n} "You will find it. Wherever it is, whoever has it, whatever you have to pay. You will put it back on your own hip. And then you will carry it where it has to go: the black heart of Deskari, or the heart of the Wound he made if he is past carrying it to. Swear that on my iron, since I cannot make you swear on my sword. Then keep the iron."''',
       c('[Close your fist on the cuff.] "I swear it. I\'ll find it, and I\'ll carry it."', "late_sworn",
         flags=(SWAPPED, JUDGES, OATH, LATE, SWORD_LOST), forbids=(IZ,)),
       c('[Close your fist on the cuff.] "I swear it. I\'ll find it, and I\'ll carry it."', "late_sworn",
         flags=(SWAPPED, JUDGES, OATH, LATE, SWORD_LOST, OATH_THRESHOLD), requires=(IZ,)),
       c("[Give her back the cuff.]", abort=True)),
]
SCENES.append(scene(Y + "late.wall", "The gate she held", "Yaniel", 5, "", late_nodes,
                    requires=("trickster", FREED, CH5), forbids=(KILLED, SWAPPED, CLOSED), delay=24, last=5,
                    Relationship=REL, Remote=True, Kind="visit", Chapters=[5], Areas=[DREZEN],
                    TricksterDevice=True, TricksterState="late"))
tag(Y + "late.wall")


# --- 3. Chapter 5 (T): she comes to stay -------------------------------------------------------------------------------------

visit(Y + "ch5.found", "I held your wall", [
    nar("start", '''{n}She is waiting in the corridor outside your rooms when you come back from the day's business, sitting on the bench where petitioners sit, with her back straight against the wall and her boots flat on the floor, as if the bench were a post she had been ordered to hold.{/n}''',
        c("Continue", "carries", requires=(CARRIES,)),
        c("Continue", "judges", requires=(HELD,), forbids=(CARRIES,)),
        c("Continue", "judges_empty", forbids=(CARRIES, HELD))),
    yn("judges_empty", '''{n}She stands when she sees you, and her eyes go straight to your hip, and find nothing there, and come up to your face.{/n}
"Commander." {n}A nod, very correct, and cold.{/n} "I came to watch your hands. I told you I would. They are empty. I have been watching every sword the smiths here sell, in case yours turned up on a table. It has not, yet."
"You swore. The oath is not due. I will be here when it is."''',
       c("Continue", "cuff_seen", requires=(CUFF_WORN,)),
       c("Continue", "why_back", requires=(WHY_BACK,), forbids=(CUFF_WORN,)),
       c("Continue", "stay", forbids=(CUFF_WORN, WHY_BACK))),
    yn("carries", '''{n}Radiance is across her knees, in a plain scabbard somebody has sewn for it out of an old saddle. She stands when she sees you, and the sword comes up with her as if it were part of her arm.{/n}
"Commander." {n}A nod, very correct.{/n} "I held your wall with your sword while you were in the Abyss. The east wall, the night watches, the old gate. Twice things came over it that the sentries did not have names for. Radiance had names for them."
"I thought you should know where your sword was. And I wanted to see if your hands had grown back empty."''',
       c("Continue", "cuff_seen", requires=(CUFF_WORN,)),
       c("Continue", "why_back", requires=(WHY_BACK,), forbids=(CUFF_WORN,)),
       c("Continue", "stay", forbids=(CUFF_WORN, WHY_BACK))),
    yn("judges", '''{n}She stands when she sees you, and her eyes go straight to your hip, and stay there until she has found the hilt.{/n}
"Commander." {n}A nod, very correct.{/n} "I came to watch your hands. I told you I would. I have been watching the walls of this city while you were in the Abyss, which was less interesting, and I have been watching every sword the smiths here sell, in case yours turned up on a table. It did not."
"So. You still have it. That is one day of the oath kept. I will be here for the others."''',
       c("Continue", "cuff_seen", requires=(CUFF_WORN,)),
       c("Continue", "why_back", requires=(WHY_BACK,), forbids=(CUFF_WORN,)),
       c("Continue", "stay", forbids=(CUFF_WORN, WHY_BACK))),
    yn("cuff_seen", '''{n}Then she sees your wrist.{/n}
{n}She goes very still. The iron is where you closed it in the Abyss, crude and heavy, the sheared link lying against the back of your hand. She reaches out as if to touch it and stops a finger short.{/n}
"You wear it." {n}Her voice has gone odd.{/n} "In the Abyss. You walked around the Abyss with a husk's iron on." {n}She lets her hand fall.{/n} "Take it off in front of me one day, Commander, and let me see your wrist. I want to know if it leaves the same mark on a free person as it did on me."''',
       c("Continue", "stay")),
    yn("why_back", '''{n}Her eyes go to your belt pouch, the way a woman's go to a purse she has seen a pickpocket touch.{/n}
"You told me in the Fane you kept it so that I would have to come and fetch it. Here I am. Fetching." {n}She does not hold out her hand.{/n} "Don't give it to me yet. I have not decided whether I want it."''',
       c("Continue", "stay")),
    yn("stay", '''"I have taken a room in the old east gate tower. Nobody wanted it; it floods. The chaplains here tried to put me in the cathedral close with the widows, to wait for my own statue." {n}Her lip curls.{/n} "They are bringing it up from Nerosyan, did you know? Carved in stone, sword in hand, eyes on heaven. It is on the same road I came up, a week behind me, on an ox-cart. I am being followed into Drezen by my own grave."
"I will be on the east wall most nights. If you want me, that is where I am. If you do not, that is also where I am."''',
       c('"I\'ll come up."', flags=(RETURNED, STARTED)),
       c('"Try to sleep sometimes."', "sleep"),
       c("[Show her the second iron, from the block in Alushinyrra.]", "husk", requires=(HUSK_FREED,)),
       c("[Show her the second iron, from the block in Alushinyrra.]", "husk", requires=(HUSK_BOUGHT,), forbids=(HUSK_FREED,))),
    yn("husk", '''{n}You take it out of the pack and put it on the bench beside her: a second cuff, crude husk-iron, the pin hammered flat, not hers. She looks at it without touching it, the way she looked at her own wrist in the Fane.{/n}
"Where?" {n}Her voice is very quiet.{/n}
{n}You tell her. The Fleshmarkets of the Middle City, a block, a crier with a painted smile, genuine Fane stock broken up this season. A woman on a hook by one wrist, with a face that did not fit her.{/n}''',
       c("Continue", "husk2")),
    yn("husk2", '''"Minagho's racks, sold off by the piece." {n}She picks the cuff up at last, and turns it, and finds the worn bright place on the inside where a wrist moved against it for years.{/n} "I knew some of them. We could not speak, most nights. We tapped on the hooks. I do not know which one this was. I never knew their names; Minagho named them all herself, like dogs."
{n}She puts it back in your hand.{/n} "Keep it with mine. Do not tell me you did it for me. Tell me you did it because you know how the pin goes now, and could not walk past."''',
       c('"I couldn\'t walk past."', flags=(RETURNED, STARTED, Y + "husk_told"))),
    yn("sleep", '''"Sleep." {n}She considers the word.{/n} "I slept on a hook for seventy years, Commander. It was never restful. I will try a bed when I have made sure nothing is coming over the wall to take it off me." {n}She turns to go, and stops.{/n} "Come up anyway."''',
       c("[Let her go.]", flags=(RETURNED, STARTED))),
], requires=("trickster.ever", SWAPPED, CH5), forbids=(RETURNED, LATE))

visit(Y + "ch5.found_late", "A room that floods", [
    nar("start", '''{n}Two days after the wall, a boy from the gate guard brings you a message he has plainly been made to repeat until he could say it without looking at his feet.{/n}''',
        c("Continue", "msg")),
    yn("msg", '''"The paladin says," {n}the boy recites,{/n} "that she has taken the room in the old east gate tower, the one that floods, and that nobody is to try to move her to the cathedral close with the widows, and that she is not anybody's relic, and that if the Commander wants to see the iron she gave away, the Commander knows which wall she is on."
{n}He takes a breath.{/n} "And she said to say she has not been sick yet. She said you would know what that meant."
{n}He hesitates.{/n} "She also said, if the Commander asked how she was, to say she was standing up. I don't know what that means, my lord. She said you would."''',
       c("Continue", "carries", requires=(CARRIES,)),
       c("Continue", "judges", forbids=(CARRIES,))),
    nar("carries", '''{n}That night you see her from the citadel: a lean shape against the stars on the broken parapet of the east gate, and every so often, when something moves out in the ash, a thin line of gold where she lifts the sword to look at it.{/n}''',
        c('"Tell her I know which wall."', flags=(RETURNED, STARTED))),
    nar("judges", '''{n}That night you see her from the citadel: a lean shape against the stars on the broken parapet of the east gate, standing her watch with a borrowed spear. Once, when you cross the courtyard with Radiance on your hip, the shape on the wall turns to follow you until you are through the door.{/n}''',
        c('"Tell her I know which wall."', flags=(RETURNED, STARTED))),
], requires=("trickster.ever", LATE), forbids=(RETURNED,), delay=24)


# --- 4. After Iz (T): the verdict ---------------------------------------------------------------------------------------

visit(Y + "verdict.letter", "What Iz was like", [
    nar("start", '''{n}The letter comes down from Iz with the wounded, in the satchel of a Mendevian sergeant who has plainly been told what she would do to him if he lost it. The hand is square and upright and old-fashioned, the hand of a woman who learned her letters before anyone now living in Drezen was born.{/n}''',
        c("[Read it.]", "letter")),
    yn("letter", '''"Commander,
"I did not tell you I was going. You would have made a face about it, or made a plan about it, and I have had enough plans made about me. I went up with the Mendevian foot on the second day, in the rank behind the shields, where an old woman with a good sword is most use.
"You will have heard that Deskari spoke over Iz. I heard it too. It was like having a hive poured into your ears."''',
       c("Continue", "sang", requires=(HOLY,)),
       c("Continue", "quiet", forbids=(HOLY,))),
    yn("sang", '''"And Radiance sang. There is no other word for it, Commander, and I have tried to find one all night. It grew bright, and then it grew hot, and then it was singing in my hands, and I could not have let go of it if Minagho herself had come up behind me and asked me to."''',
       c("Continue", "letter_iz")),
    yn("quiet", '''"Radiance did not sing. The old songs say it used to light up every time I raised it; the songs are liars, like the statue. His voice went over it like wind over a stone. It was a good sword, and it did good work, and I was glad of that. I did not want it to do anything I could not do myself."''',
       c("Continue", "letter_iz")),
    yn("letter_iz", '''"I should tell you what Iz was like, since you were somewhere at the front of it and will have seen only the front. At the back it was dust and flies and orders nobody could hear. The foot went in through what used to be a gate and is now a hole, over stones that were somebody's house when Sarkoris was a country. There were dead in the streets older than I am. Some of them got up.
"I fought beside a boy from Vyre who had never held a spear before the spring and a Mendevian sergeant who had held one for thirty years, and neither of them knew who I was, and neither of them asked. It was the best day I have had since the siege. I would not have believed that possible. I am writing it down so that I do not lie to myself about it later."''',
       c("Continue", "end_sang", requires=(HOLY,)),
       c("Continue", "end_quiet", forbids=(HOLY,))),
    yn("end_sang", '''"Seventy years I told myself that sword was a thing I used to have. You put it back in my hands and it glowed for me, and I thought that was the most it would ever do. Over Iz it sang. I do not know what that makes it, or what that makes me.
"I know what it makes you. It makes you the one who heard nothing. It would have sung for you. It sang for me instead, because you gave it away.
"We are not square. I am coming back to Drezen to settle it. Keep my iron where I can find it.
"Y."''',
       c("[Fold the letter away.]", flags=(VERDICT,))),
    yn("end_quiet", '''"Seventy years I told myself that sword was a thing I used to have. You put it back in my hands and it was only a sword. At Iz it was only a sword still, and I was only a soldier in a rank, and that was the best of it. Nobody was looking at the sword. Nobody was looking at me.
"You gave me that. I do not know yet what I gave you, except a lump of husk-iron and a great deal of trouble.
"We are not square. I am coming back to Drezen to settle it. Keep my iron where I can find it.
"Y."''',
       c("[Fold the letter away.]", flags=(VERDICT,))),
], requires=("trickster.ever", RETURNED, IZ, CARRIES), forbids=(VERDICT, HANDED_LATE), kind="letter", areas=())

visit(Y + "verdict.wall", "After Iz", [
    nar("start", '''{n}She is on the east wall when you come up, with the sword you put in her hands after Iz across her knees and a whetstone going along it in long, slow strokes. She does not look up.{/n}''',
        c("Continue", "talk")),
    yn("talk", '''"You gave me this after the demon lord was already beaten," {n}she says.{/n} "I noticed. I am not a fool. Whatever it was going to do at Iz, it did not do it for me, and it did not do it for you either. It hung on your hip in a wagon, or it stayed in Drezen, and the war went on without it."
"So I have been taking it out on the ash every night. The things that come up out of the Wound do not know it was late." {n}The whetstone stops.{/n} "We are not square, Commander. Come up to my room tomorrow. I want to settle it."''',
       c('"Tomorrow."', flags=(VERDICT,))),
], requires=("trickster.ever", RETURNED, IZ, CARRIES, HANDED_LATE), forbids=(VERDICT,), delay=24)

visit(Y + "verdict.hands", "Show me your hands", [
    nar("start", '''{n}She is on the stair of the citadel when you come back from Iz, sitting on the top step with the east-wall spear across her knees. She does not get up. She looks at your face, and then at your hip, and then at your hands, in that order, the way a quartermaster looks at a returned wagon.{/n}''',
        c("Continue", "pending_held", requires=(OATH_THRESHOLD, HELD)),
        c("Continue", "pending_empty", requires=(OATH_THRESHOLD,), forbids=(HELD,)),
        c("Continue", "held", requires=(HELD,), forbids=(OATH_THRESHOLD,)),
        c("Continue", "sang_gone", requires=(SANG,), forbids=(HELD, OATH_THRESHOLD)),
        c("Continue", "empty", forbids=(HELD, SANG, OATH_THRESHOLD))),
    yn("pending_held", '''"Still on your hip." {n}She nods at the hilt.{/n} "Good. You swore me the Threshold on my wall, and the Threshold is still ahead of you. I cannot judge an oath that is not due. I can only look, and I have looked."
"Keep it there. When you walk into his Wound I want it in your hand, not in a quartermaster's wagon. That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_PENDING))),
    yn("pending_empty", '''"Not on your hip." {n}She looks at the place where it should be.{/n} "You swore me the Threshold on my wall, and the Threshold is still ahead of you. So I will not call it broken yet. I will only tell you that you had better find it before you walk into his Wound, because I will be asking."
"That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_PENDING))),
    yn("held", '''"Show me."
{n}You draw Radiance and lay it across your palms. She does not touch it. She leans close and looks at the edge, the way a smith would, and at the grip, and at the black stains in the fuller that no amount of oil has quite got out.{/n}''',
       c("Continue", "held_sang", requires=(SANG,)),
       c("Continue", "held_word", forbids=(SANG,))),
    yn("held_sang", '''"It sang," {n}she says, not a question.{/n} "The foot coming back down the road are telling it in every village. Deskari opened his mouth over Iz, and the Commander's sword lit up like a church window and started to sing." {n}She sits back.{/n} "I wanted to be there to hear it. I was up on your wall, watching for you. That was my choice, and I would make it again, and I will be sorry about it for the rest of my life."
"You carried it where you swore. The oath stands." {n}She stands, and puts her hand flat over yours on the blade, the way she did when you swore it.{/n} "That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_STANDS))),
    yn("held_word", '''"It did not sing, they say. The foot coming back down the road say the Commander went up into the ruins and came out again, and the thing that spoke over the city is not speaking any more, and not one of them mentions a sword that shone." {n}She looks up from the blade.{/n}
"This on your hip tells me you have it now. It does not tell me where it has been. Did it go to Iz, Commander?"''',
       c('[Diplomacy] "It went into Iz on my hip, and it came out again."',
         check=dict(Skill="CheckDiplomacy", DC=15, Success="held_believed", Failure="held_unproven"))),
    yn("held_believed", '''{n}She studies your face the way she studied the edge. Whatever she is looking for, she finds enough of it.{/n}
"Perhaps it only sings for the hands that were first. Perhaps it only sings in stories. It went where you swore it would go. The oath stands." {n}She stands, and puts her hand flat over yours on the blade, the way she did when you swore it.{/n} "That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_STANDS))),
    yn("held_unproven", '''{n}She studies your face the way she studied the edge, and shakes her head, slowly.{/n}
"I cannot tell. Seventy years of liars, Commander, and I cannot tell with you. I will not condemn you on nothing, and I will not say the oath stands either." {n}She stands.{/n} "Carry it to the Threshold. I will believe it there. That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_UNPROVEN))),
    yn("sang_gone", '''"The foot coming back down the road say your sword sang at Iz." {n}She says it very evenly.{/n} "Lit up like a church window when he opened his mouth, and sang. So it was there, on your hip, where you swore it would be." {n}She looks at your hip, where it is not.{/n} "And now it is not. Somewhere between Iz and this step you put it down."
"I swore you to Deskari's heart. You took it there. What you do with a sword after it has been where it has to go is your affair, Commander, and I am trying very hard to believe that." {n}She stands.{/n} "The oath stands. That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_STANDS))),
    yn("empty", '''"Where is it?"
{n}Your hip is bare. There is nothing in your hands but your hands.{/n}''',
       c('[Diplomacy] "I carried it into Iz. It\'s gone since. You\'ll have to take my word."', "empty_word_lost",
         requires=(SWORD_LOST,)),
       c('[Diplomacy] "I carried it into Iz. It\'s gone since. You\'ll have to take my word."',
         check=dict(Skill="CheckDiplomacy", DC=20, Success="believed", Failure="doubted"), forbids=(SWORD_LOST,)),
       c('"It\'s not on me. It hasn\'t been for a while."', "broken")),
    yn("empty_word_lost", '''"Your word." {n}She says it without heat.{/n} "You swore on my iron to find it and carry it, because you had already lost it once. And here you are with your hands empty again." {n}She looks at them for a while.{/n}''',
       c("Continue", "broken")),
    yn("believed", '''{n}She studies your face the way she studied your hands. You hold still for it. Whatever she is looking for, she seems to find something near enough.{/n}
"Seventy years with liars, Commander. You are either telling the truth or you are the best of them." {n}She lets out a breath.{/n} "I will take it. I have decided to take it. What you do with a sword after it has been where it has to go is your affair. The oath stands."
"That is one thing. There is another thing, and it is not about the sword."''',
       c("Continue", "done", flags=(VERDICT, OATH_BELIEVED, OATH_STANDS))),
    yn("doubted", '''{n}She studies your face the way she studied your hands, and whatever she is looking for, she does not find it.{/n}''',
       c("Continue", "broken")),
    yn("broken", '''"You swore." {n}Not loud. She stands up, and the spear stands up with her.{/n} "On that blade, with my hand on yours, in a pit under the ground where I had not heard anyone swear anything true in seventy years. And you had it in your pack when you went to Iz, or you did not, and either way it is not on your hip now, and you cannot show me where it went."
{n}She looks away, down the stair, over the courtyard.{/n} "I am not going to curse you. I have not got the heart for it. But I am going to say it plainly, once, so that it has been said: the oath is broken, and I heard it break."''',
       c("Continue", "done", flags=(VERDICT, OATH_BROKEN))),
    nar("done", '''{n}She goes down the stair without looking back. Halfway down, she stops, and says over her shoulder, not loudly:{/n} "Come and find me tomorrow. There is a thing we have to settle, you and I, and I want to do it on my own wall."''',
        c("Continue", "tail_kept", forbids=(OATH_BROKEN,)),
        c("Continue", "tail_broken", requires=(OATH_BROKEN,))),
    nar("tail_kept", '''{n}She is gone into the crowd at the bottom of the stair before you can answer.{/n}''', c("[Let her go.]")),
    nar("tail_broken", '''{n}She is gone into the crowd at the bottom of the stair before you can answer. It is not, you think, a summons to be forgiven.{/n}''',
        c("[Let her go.]")),
], requires=("trickster.ever", RETURNED, IZ, JUDGES), forbids=(VERDICT, CARRIES))


# --- 5. The commit (T): she proposes the trade-back; the yes is that neither trades ----------------------------------------
# In person (ledger R2-3): on her presence at her own Drezen mark, the spawner the Angel path uses for her (Yaniel_DefaultActor,
# scene 3e2b5ea0), and up the stair to her room. The room twin is the remote fallback when the presence cannot be placed.

PRESENCE = "yaniel.presence"
PRESENCE_FAILED = "yaniel.presence.failed"
MARK = "0e8a0488-bd46-4115-be7a-6674b9358a71"        # her native DrezenCapital spawner (Yaniel_DefaultActor / Drezen_Yaniel_Ch5)
GREETING = ("{n}Yaniel stands off the street with her back to a wall and her cloak pulled round her, the way a sentry stands "
            "between watches. People passing give her room without knowing why. She watches their hands.{/n}")
PRESENCES = {
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(Locator=MARK, Offset=[0.0, 0.0]),
                   Requires=["trickster.ever", RETURNED], Forbids=[CLOSED, LEFT_FREE, KILLED], MinChapter=5, MaxChapter=5,
                   AnswerLists=[], Dialog="hub", Greeting=GREETING),
}

TRADE_ROOM = '''{n}The room in the old east gate tower is exactly as bad as she said. There is a camp bed that the damp has warped, a brazier, a pail under the place where the roof leaks, and one good thing: a window cut in the thickness of the wall that looks straight down the road the refugees took the day the city fell.{/n}'''

TRADE_BODY = [
    yn("carries", '''{n}She unbuckles the saddle-leather scabbard from her hip, and holds Radiance out to you across the room, hilt first, the way she did in the Fane.{/n}
"Your sword for my shackle," {n}she says,{/n} "and we are square."''',
       c("Continue", "carries_sang", requires=(HOLY,)),
       c("Continue", "carries_quiet", forbids=(HOLY,))),
    yn("carries_sang", '''"It sang for me at Iz. I have thought about that every night since. You gave me that, and it cost you the only song that sword will ever sing for you. I cannot give it back. I can give you the sword. Take it, and give me my iron, and we are two soldiers who did each other a good turn in a bad place, and nobody owes anybody."''',
       c("Continue", "told", requires=(MINAGHO_TOLD,)),
       c("Continue", "hid", requires=(MINAGHO_SECRET,), forbids=(MINAGHO_TOLD,)),
       c("Continue", "ask", forbids=(MINAGHO_TOLD, MINAGHO_SECRET))),
    yn("carries_quiet", '''"It did not sing at Iz. It did not need to. It went into the city in a rank of soldiers, in the hand of a soldier, and it came out again, and nobody made a song of it. You gave me that. Take it back now, and give me my iron, and we are two soldiers who did each other a good turn in a bad place, and nobody owes anybody."''',
       c("Continue", "told", requires=(MINAGHO_TOLD,)),
       c("Continue", "hid", requires=(MINAGHO_SECRET,), forbids=(MINAGHO_TOLD,)),
       c("Continue", "ask", forbids=(MINAGHO_TOLD, MINAGHO_SECRET))),
    yn("judges", '''{n}She looks at the hilt on your hip, and then at the pouch where you keep her iron.{/n}
"Your sword for my shackle," {n}she says,{/n} "and we are square."
"You carried it where you swore. I watched your hands all the way to Iz and back, and they did not drop it. The oath is done; the sword is yours, free and clear, and I will say so to any priest who asks. Give me my iron, and we are two soldiers who did each other a good turn in a bad place, and nobody owes anybody."''',
       c("Continue", "told", requires=(MINAGHO_TOLD,)),
       c("Continue", "hid", requires=(MINAGHO_SECRET,), forbids=(MINAGHO_TOLD,)),
       c("Continue", "ask", forbids=(MINAGHO_TOLD, MINAGHO_SECRET))),
    yn("judges_empty", '''{n}She looks at your bare hip, and then at the pouch where you keep her iron.{/n}
"Your sword for my shackle," {n}she says,{/n} "and we are square. It does not matter that you have not got it on you. It went where it had to go; what it does now is its own business, and yours."
"The oath is done. Give me my iron, and we are two soldiers who did each other a good turn in a bad place, and nobody owes anybody."''',
       c("Continue", "told", requires=(MINAGHO_TOLD,)),
       c("Continue", "hid", requires=(MINAGHO_SECRET,), forbids=(MINAGHO_TOLD,)),
       c("Continue", "ask", forbids=(MINAGHO_TOLD, MINAGHO_SECRET))),
    yn("judges_open", '''{n}She looks at your hip, and then at the pouch where you keep her iron.{/n}
"Your sword for my shackle," {n}she says,{/n} "and we are square. Not the oath. The oath waits for the Threshold, and it will wait whatever we do here. The rest of it."
"Give me my iron, and we are two soldiers who did each other a good turn in a bad place, and nobody owes anybody anything but that one walk into the Wound."''',
       c("Continue", "told", requires=(MINAGHO_TOLD,)),
       c("Continue", "hid", requires=(MINAGHO_SECRET,), forbids=(MINAGHO_TOLD,)),
       c("Continue", "ask", forbids=(MINAGHO_TOLD, MINAGHO_SECRET))),
    yn("told", '''{n}She glances, without meaning to, out of the window and down into the city.{/n}
"And do not think I have forgotten your lilitu. I have not. Every morning when I come down off the wall I think about her, and about the knife in my boot." {n}Her jaw sets.{/n} "You told me the truth about her. That is why I am standing here offering you a fair trade instead of throwing your iron out of the window. Do not make me regret it."''',
       c("Continue", "ask")),
    yn("hid", '''{n}She glances, without meaning to, out of the window and down into the city.{/n}
"There is still a lilitu in your city's business, and you still have not told me why. I have stopped asking. I have not stopped watching your hands." {n}Her jaw sets.{/n} "This is a fair trade, Commander. It is fair because it asks nothing about her. Take it, and neither of us has to find out what the other one is hiding."''',
       c("Continue", "ask")),
    yn("ask", '''{n}She holds out her hand, palm up. It is steady. Her voice is not, quite.{/n}
"Well, Commander? It is a fair trade. It is the fairest one anybody has offered me in seventy years."''',
       c('[Keep the shackle] "No. You keep what I gave you. I keep what I took. Nobody\'s square."', "yes",
         flags=(COMMITTED, SHACKLE)),
       c("[Give her the shackle back.]", "given")),
    yn("yes", '''{n}She stares at you. Her hand stays out a moment longer, empty, and then she lets it drop.{/n}
"Nobody's square," {n}she repeats.{/n} "That is not a trade. That is a debt. Two debts, going the wrong way." {n}She crosses the room. Up close she smells of the wall, of cold stone and wind and the oil she uses on the sword.{/n} "Do you know what Minagho used to say to me? That a thing you owe is a thing that owns you. She said it the way other people say good night."
{n}She takes your face in both her hands. They are hard hands, callused in all the places a sword calluses a hand, and they are shaking.{/n} "I would like very much to owe you something, and be owned by nothing," {n}she says, and kisses you.{/n}''',
       c("Continue", "yes2")),
    yn("yes2", '''{n}It is not a gentle kiss. It is the kiss of somebody who has been told she is dead for seventy years and has decided to argue. When she lets you go she does not step back; she leans her forehead on yours and breathes, hard, like a woman at the top of a stair.{/n}
"Tomorrow night," {n}she says.{/n} "Not here. The pail is full, and I will not do this with a pail listening. I know a better place. Keep my iron, Commander. Keep it close."''',
       c('"Close."')),
    yn("given", '''{n}You put the iron in her palm. Her fingers close on it. For a moment she only holds it, weighing it, as she weighed the sword.{/n}
"There," {n}she says.{/n} "Square." {n}She turns it over. The sheared link swings.{/n} "It is lighter than I remembered. Or I am stronger. One of us has changed."
{n}She does not put it on. She hangs it from a nail by the window, where it can see the road, and stands looking at it with her back to you.{/n} "Thank you, Commander. You had better go. I have a watch to stand."''',
       c("[Go.]", flags=(DECLINED,))),
]
TRADE_BRANCH = (
    c("Continue", "carries", requires=(CARRIES,)),
    c("Continue", "judges", requires=(OATH_STANDS, HELD), forbids=(CARRIES,)),
    c("Continue", "judges_empty", requires=(OATH_STANDS,), forbids=(CARRIES, HELD)),
    c("Continue", "judges_open", forbids=(CARRIES, OATH_STANDS)),
)

SCENES.append(scene(Y + "commit.trade", "Your sword for my shackle", "Yaniel", 5, '"You said we had a thing to settle."', [
    yn("start", '''{n}She pushes herself off the wall as you come up.{/n} "Not here," {n}she says.{/n} "Walk with me. Up to my wall."
{n}She takes you through the east gate and up the tower stair without another word, two steps ahead, not looking back to see whether you follow.{/n}''',
       c("Continue", "room")),
    nar("room", TRADE_ROOM + '''
{n}She goes to the window and stands at it with her back to you for a while, looking down the road. Then she turns round.{/n}''', *TRADE_BRANCH),
    *copy.deepcopy(TRADE_BODY)],
    requires=("trickster.ever", VERDICT, DRAWN), forbids=(KILLED, CLOSED, COMMITTED, DECLINED, OATH_BROKEN, Y + "commit.trade_room"),
    delay=24, last=5, Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=PRESENCE))
tag(Y + "commit.trade")

visit(Y + "commit.trade_room", "Your sword for my shackle", [
    nar("start", '''{n}A boy from the gate guard brings the word: the paladin is in her room in the gate tower, and would the Commander come up.{/n}
''' + TRADE_ROOM + '''
{n}She is standing at the window with her back to you when you come up the stair. She turns round.{/n}''', *TRADE_BRANCH),
    *copy.deepcopy(TRADE_BODY)],
    requires=("trickster.ever", VERDICT, DRAWN, PRESENCE_FAILED), forbids=(COMMITTED, DECLINED, OATH_BROKEN, Y + "commit.trade"), delay=24)

VIGIL_NODES = [
    nar("start", '''{n}A note under your door, in the square old-fashioned hand: "Tonight. The niche under the east gate tower, where they have put the statue. Bring nothing. You will kneel on stone until the morning bell. I have not kept a vigil since the Fane. I would not like to keep this one alone."{/n}
{n}The niche is at the foot of the gate tower, a hollow in the old wall where the chaplains have set up their ox-cart saint until the cathedral is ready for her: Yaniel of Drezen, the Holy Martyr, in painted stone, sword raised, eyes on heaven. The real one is already kneeling in front of her with a lamp at her knee. She does not look round.{/n}''',
        c("Continue", "broken", requires=(OATH_BROKEN,)),
        c("Continue", "declined", requires=(DECLINED,), forbids=(OATH_BROKEN,))),
    yn("broken", '''"You broke an oath on my sword." {n}She says it to the statue.{/n} "A paladin who breaks an oath kneels a night for it. You are not a paladin, and I am not your confessor, and I do not know what this is. But I know what a vigil is for. It is for finding out what is left when everything you were going to say has been said to the dark."''',
       c("Continue", "choose")),
    yn("declined", '''"You gave it back." {n}She says it to the statue.{/n} "I have had it on a nail by my window for three nights now, and every night I have taken it down and held it, and put it back. I thought it would feel like having my wrist back. It feels like having something taken away from me twice."
"I do not know what that means. When I do not know what a thing means I kneel a night on it. That is what a vigil is for."''',
       c("Continue", "choose")),
    yn("choose", '''"Kneel with me until the bell. Or do not. There is no shame in going to bed, Commander. The crusade needs you awake more than it needs you on your knees in front of a statue that does not look like me."''',
       c("[Kneel beside her.]", "kneel"),
       c('[Leave her to it] "Keep your vigil, Yaniel. It\'s yours."', "leave")),
    nar("kneel", '''{n}You kneel. The flags are wet and colder than anything has a right to be in summer. The lamp throws the statue's shadow up the wall, sword and all, three times the height of the woman beside you.{/n}
{n}She does not pray aloud. After the first hour, neither do you. The watch changes on the wall above; a cart goes by in the dark; somewhere out in the ash something howls and is answered and falls quiet. Your knees stop hurting sometime after midnight, which is worse than when they hurt.{/n}
{n}Toward the end of the night she reaches over without looking and takes your hand, and holds it on the stone between you, and does not let go.{/n}''',
        c("Continue", "bell")),
    yn("bell", '''{n}The morning bell goes in the cathedral. She stands, stiffly, and pulls you up after her, and then she holds out her other hand. The iron is in it: her cuff, the sheared link swinging.{/n}
"Take it back," {n}she says.{/n} "Not because I cannot carry it. I carried it on a nail for three nights and it did not kill me. Because I would rather you had it. Because every time I look at your hands I want to know what they are holding, and I have decided I want it to be this."
{n}She puts it in your palm and closes your fingers over it, one at a time, the way you closed hers over the sword in the Fane.{/n} "There. Now it is my trick."''',
       c("[Keep the shackle.]", "bell_yes", flags=(COMMITTED, SHACKLE, VIGIL))),
    yn("bell_yes", '''{n}She kisses you in the gray light at the foot of her own statue, briefly and hard, with the lamp guttering out at her knee.{/n}
"Tonight," {n}she says against your mouth.{/n} "Here. I want her to watch."''',
       c('"Tonight."')),
    yn("leave", '''{n}She nods, as if you had answered a question about the weather.{/n}
"It is," {n}she says.{/n} "It always was. Go on, Commander. Sleep. One of us should."
{n}When you look back from the corner she has not moved: a gray head bowed in front of a painted one, and the lamp, and the long shadow of a raised stone sword going up the wall into the dark.{/n}''',
       c("[Go.]", flags=(LEFT_FREE, CLOSED))),
]
visit(Y + "commit.vigil", "A vigil at the niche", VIGIL_NODES, requires=("trickster.ever", DRAWN),
      forbids=(COMMITTED, LEFT_FREE), delay=24, RequiresAnyGroups=[[DECLINED, OATH_BROKEN]])


# --- 6. The niche (T): the intimacy, the morning, the lamp ----------------------------------------------------------------

NICHE_NODES = [
    nar("start", '''{n}She is waiting at the foot of the gate tower when the watch changes, with a lamp in one hand and her cloak over her arm, and she does not say anything. She takes your wrist, as you took hers on the wall, and leads you into the niche.{/n}
{n}The painted Yaniel of Drezen stands over the two of you with her stone sword raised and her stone eyes on heaven. The carver gave her the face of a girl of twenty with no scars and a mouth that has never said anything rude.{/n}''',
        c("Continue", "statue", requires=(STATUE_LIED,)),
        c("Continue", "statue_true", requires=(Y + "statue_truth",), forbids=(STATUE_LIED,)),
        c("Continue", "statue_scars", requires=(Y + "statue_scars",), forbids=(STATUE_LIED, Y + "statue_truth")),
        c("Continue", "vigil", requires=(VIGIL,), forbids=(STATUE_LIED, Y + "statue_truth", Y + "statue_scars")),
        c("Continue", "lamp", forbids=(STATUE_LIED, Y + "statue_truth", Y + "statue_scars", VIGIL))),
    yn("statue", '''"You told me it was a good likeness." {n}She looks up at it.{/n} "You are a liar, Commander, and a very kind one, and I have been thinking about that lie for days."''',
       c("Continue", "lamp")),
    yn("statue_true", '''"You told me it looked nothing like me." {n}She looks up at it.{/n} "You are the first person in Drezen who has. The chaplains keep telling me how moving it is. I keep wanting to take a hammer to its nose."''',
       c("Continue", "lamp")),
    yn("statue_scars", '''"You told me the scars were the best part." {n}She looks up at the smooth stone face above her.{/n} "She has none. Look at her. Not one. I have been waiting days to show you exactly how many she is missing."''',
       c("Continue", "lamp")),
    yn("vigil", '''"We knelt on these stones all night." {n}She looks down at the flags, and then up at the statue.{/n} "She watched us do it. She watched us all night with that face on, as if we were very holy and very dull."''',
       c("Continue", "lamp")),
    nar("lamp", '''{n}She sets the lamp at the statue's feet, so that the stone woman is lit from below and watches the two of you with her painted eyes, and laughs at her: a real laugh, low and delighted and a little cruel.{/n}
"Look at her," {n}she says.{/n} "The Holy Martyr. Seventy years they prayed to her, and she never once wanted anything." {n}She turns to you.{/n} "I have wanted things every day of my life. Even on the hook. Especially on the hook."''',
        c("Continue", "want")),
    yn("want", '''{n}She takes your face in two sword-callused hands and kisses you like someone breaking out of somewhere: hard, and then harder, with her teeth, as if the kiss were a wall and she meant to be on the other side of it by morning.{/n}
"I spent seventy years with things that wanted me," {n}she says, against your mouth.{/n} "Minagho wanted me on a shelf. Areelu wanted me on a table. I do not want to be wanted, Commander. I want."''',
        c("[Pull her in.]", "threshold"),
        c('"Then take."', "threshold")),
    nar("threshold", '''{n}Her fingers find your buckles faster than your own could, as fast as they ever found a strap on a shield, and your belt goes on the flags, and the pouch with her iron in it with it; she kicks the pouch against the statue's plinth without looking, as if to say: there, you, hold that. Your shirt comes open under her hands. She puts her palm flat on your chest over your heart and holds it there, feeling it go, and her own breath goes ragged.{/n}
{n}You get her out of the borrowed crusader's tunic, and the shirt under it. She is lean and hard and scarred all over, a hundred old white lines across her ribs and shoulders, the marks of the hooks in a neat row under her collarbones, and she does not hide any of it. She catches your hand when it slows over the hook-scars and presses it down harder, into them.{/n}''',
        c("Continue", "threshold2")),
    nar("threshold2", '''"Not gently," {n}she says.{/n} "Gently is for relics."
{n}She shakes her cloak out onto the flags at the statue's feet, in the lamplight, and pulls you down onto it with her knee already across you. She drags your shirt the rest of the way off your shoulders and plants her hands on your chest, her gray hair falling in her eyes, her breath hissing through her teeth, and she begins to lower herself onto you, and above her the painted martyr gazes at heaven and sees nothing at all.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}Afterwards the lamp has burned down to a blue bead. She sits on the cloak with her back against the plinth of her own statue, one knee drawn up, your shirt around her shoulders because it was nearer than hers, and the iron cuff in her hand. She is turning it over and over, and she is not wearing it.{/n}''',
        c("Continue", "morning2")),
    yn("morning2", '''"Seventy years," {n}she says,{/n} "I thought about every door in the Fane. Which ones had guards and which had wards, which demon slept, which husk could be trusted to scream. Not a day went by that I did not try to get out."
"And now I keep walking back to one door." {n}She puts the iron in your hand and closes your fingers on it.{/n} "Explain that to me, Commander. No. Do not. You will make a joke of it, and it will be a good joke, and I will laugh, and it will still not be explained."''',
        c("Continue", "sexton_seelah", forbids=(SEELAH_DEAD, SEELAH_GONE)),
        c("Continue", "sexton_seelah", requires=(SEELAH_BACK, SEELAH_DEAD)),
        c("Continue", "sexton_seelah", requires=(SEELAH_BACK, SEELAH_GONE), forbids=(SEELAH_DEAD,)),
        c("Continue", "sexton", requires=(SEELAH_DEAD,), forbids=(SEELAH_BACK,)),
        c("Continue", "sexton", requires=(SEELAH_GONE,), forbids=(SEELAH_DEAD, SEELAH_BACK))),
    nar("sexton_seelah", '''{n}At the first bell there are boots on the gate stair: somebody coming down early for the dawn office at the niche. They stop. You hear a sharp little breath, and then nothing, and then the boots going very quietly back up the stair the way they came.{/n}
{n}When you come out of the niche an hour later, Yaniel's lamp is gone from the statue's feet. It is standing on the bottom step of the stair, filled with fresh oil and trimmed, and beside it, in the dust, somebody has drawn Iomedae's sword with a fingertip, and under it, very small, a street thief's mark for "safe house".{/n}
{n}Yaniel looks at it for a while.{/n} "Sister," {n}she says, very dry, and picks up the lamp.{/n}''',
        c("[Go up into the day.]", flags=(NICHE, MORNING))),
    nar("sexton", '''{n}At the first bell the chaplains' sexton comes down the gate stair with his broom for the dawn office at the niche, and finds the lamp burnt out at the martyr's feet, and a woman's boot print in the soot beside it, and, hanging from the martyr's raised stone sword, a borrowed crusader's cloak that somebody has left there to dry.{/n}
{n}He looks at it through three strokes of the broom. Then he takes the cloak down, folds it, lays it on the bottom step, and sweeps round it. He never says a word to anyone. Yaniel says afterwards that it was the most Iomedaean thing she has seen a churchman do since she came up out of the pit.{/n}''',
        c("[Go up into the day.]", flags=(NICHE, MORNING))),
]
visit(Y + "visit.niche", "In front of her", NICHE_NODES, requires=("trickster.ever", COMMITTED), forbids=(NICHE,), delay=24)


# --- 7. Reactions (Seelah: a paladin of Iomedae, a thief before that, and the one who called her "Sister" in the Fane) --------

SEELAH_GUARD = dict(forbids=(SEELAH_DEAD, SEELAH_GONE, CLOSED, KILLED),
                    ForbidOverrides={SEELAH_DEAD: SEELAH_BACK, SEELAH_GONE: SEELAH_BACK})

SCENES.append(reaction("Seelah", Y + "react.seelah_fane", ("trickster.ever", SWAPPED, SEELAH_SISTER),
    '''{n}Seelah waits until nobody else is in earshot, and then a little longer.{/n} "In the Fane. When you gave Yaniel back her sword." {n}She lowers her voice.{/n} "Yaniel. Radiance. I've seen that sword a hundred times, Commander, in paintings and in the hands of her statue, and you stood in front of the woman herself and picked her cuff while she was looking straight at you, with an angel down the hall."
{n}She glances at your belt pouch, then away.{/n} "I was a thief before I was a paladin. I know that twist of the wrist. I just never thought I'd see anyone use it to take something off a saint." {n}A breath.{/n} "I'm not going to ask why. I'm going to pray you had a good reason, and I'm going to keep an eye on that pouch."''',
    answer_list=SEELAH_HUB, entry='"You\'ve been looking at me oddly since the Fane."', chapter=3, last=5, portrait="Seelah",
    **SEELAH_GUARD))
tag(Y + "react.seelah_fane")

SCENES.append(reaction("Seelah", Y + "react.seelah_after", ("trickster.ever", NICHE),
    '''{n}Seelah does not look at you for a while. She is polishing her shield with great care, round and round the same boss.{/n} "I filled her lamp," {n}she says at last.{/n} "At the niche. Yesterday morning. It had burnt out."
"When the sergeants had been shouting at me all day, back when I was a novice nobody wanted, I used to go and sit under the Yaniel statue and tell her about it. She never said anything. Statues don't." {n}The cloth stops.{/n} "I heard her laughing yesterday. Down there. At the statue. I never once thought of her laughing."
{n}She looks up at last.{/n} "She was laughing. I've prayed in front of that statue for years and I never once imagined her laughing. Give her more reasons, Commander."''',
    answer_list=SEELAH_HUB, entry='"Something on your mind, Seelah?"', chapter=5, last=5, portrait="Seelah",
    flags=(SEELAH_BLESSED,), **SEELAH_GUARD))
tag(Y + "react.seelah_after")


SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"      # CompanionDialogues/Sosiel/AnswersList_0002
SCENES.append(reaction("Sosiel", Y + "react.sosiel_iron", ("trickster.ever", SWAPPED),
    '''{n}Sosiel has a sketch half-finished on his knee: a woman's wrist, bare, with a pale band across it where something used to be.{/n} "I promised her in the Fane we would heal her wounds," {n}he says, without looking up.{/n} "I thought I meant the ones you could put a salve on."
"She let me look at her wrist on the road up out of the pit. The skin is healing. The rest of it..." {n}He turns the charcoal in his fingers.{/n} "You took the iron off her, and she let you keep it. Shelyn teaches that the ugliest thing a person carries can be the thing that makes them beautiful to someone else, if the someone else is willing to hold it for a while. I never thought I would see it done with a manacle." {n}He looks at your belt pouch.{/n} "Hold it gently, Commander. It was the only thing she had."''',
    answer_list=SOSIEL_HUB, entry='"What are you drawing?"', chapter=3, last=5, portrait="Sosiel",
    forbids=("sosiel.dead", "sosiel.kicked_out", CLOSED, KILLED)))
tag(Y + "react.sosiel_iron")


# --- 8. Epilogue pages (Owner YanielEpilogue, Chapter 6; no effects) ------------------------------------------------------

EP = dict(last=6, Relationship=REL)
SAC = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})
COMMON = (
    p("{n}The Commander carried a husk's iron cuff for the rest of a long life, crude and heavy, with one sheared link of chain still hanging from its eye. Nobody was ever allowed to clean it.{/n}", requires=(SHACKLE,)),
    p("{n}Radiance stayed in Yaniel's hands. The Church of Iomedae asked for it back four times in the first year of the peace, politely, and then stopped asking. It never sang again, so far as anyone knew; she said once had been enough, and that she had heard it for both of them.{/n}", requires=(CARRIES, HOLY)),
    p("{n}Radiance stayed in Yaniel's hands. The Church of Iomedae asked for it back four times in the first year of the peace, politely, and then stopped asking. It never sang for her, and she never asked it to; she said it was a sword, and she was a soldier, and that was enough for both of them.{/n}", requires=(CARRIES,), forbids=(HOLY,)),
    p("{n}Radiance hung in the Commander's hall afterwards, not on the wall, where Yaniel had said it must never hang, but on a peg by the door at the height of a hand, so that it could be taken down in a hurry. It was, twice.{/n}", requires=(JUDGES,), forbids=(OATH_BROKEN,)),
    p("{n}The painted martyr went into the cathedral of Drezen at midsummer, as the chaplains had planned. The chaplains never did find out why the Commander's household laughed every time the procession went by it.{/n}", requires=(NICHE,)),
    p("{n}The Half Measure in Nerosyan put her roast back on its board, on the old recipe, and wrote her name beside it in chalk. She ate there every spring, under the old tree by the town hall, when it was in bloom.{/n}", requires=(B_ROAST,)),
    p("{n}An old merchant of Nerosyan with a crutch and a cloudy eye was carried up to Drezen once more before he died, to see the gate. She held his hand on the parapet for an afternoon, and afterwards she would never say what they talked about, except that it was mostly turnips.{/n}", requires=(B_REFUGEE,)),
    p("{n}When the war was over she went to the place where Staunton Vhane was buried, as she had said she would, and shouted at the ground for most of an hour. Then she sat down on it and wept, which she had not done since the Fane, and the Commander stood between her and the road so that nobody would see.{/n}", requires=(B_STAUNTON,)),
    p("{n}The Church of Iomedae never did examine her. The chaplain who had come to the Commander's door with the seal of Nerosyan wrote to his superiors that the relic was in the hands it was meant for, and that he would not be the one to take it out of them, and after that nobody else volunteered.{/n}", requires=(B_CHURCH, CARRIES)),
    p("{n}She stopped praying for things. She told her goddess about her days instead, out loud, on the wall, in the tone of a sergeant making a report, and she swore that on some nights the report was received.{/n}", requires=(B_PRAYER,)),
    p("{n}Somewhere in the Midnight Isles a woman with a face that did not quite fit her lived out her years as nobody's collector's item, and the Commander kept her iron at the bottom of a pack beside the other, and never told anyone why there were two.{/n}", any_groups=((HUSK_FREED, HUSK_BOUGHT),)),
)

SCENES.append(scene(Y + "epilogue.together", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Yaniel of Drezen, the Holy Martyr, came back from the dead and would not stay holy. She took the flooded room in the old east gate tower and kept it for the rest of her life, though she could have had any house in the city, and she stood the night watch on the east wall whenever she pleased, which was often, and nobody ever again put her name on a roster without asking her first.{/n}
{n}She never took the Commander's name and never gave her own away. What there was between them had no word in the Church's books and she did not look for one. She said she had spent seventy years being called things, and that the Commander was the only person who had ever called her nothing at all and simply held out a hand.{/n}
{n}Every year, on the night the Fane fell, she knelt a vigil in front of her own statue in the cathedral, and at the morning bell she got up and went home, and on the way she laughed.{/n}''',
        paragraphs=(*COMMON,
                    p("{n}The Commander never took the iron off. Yaniel said it looked ridiculous on a free wrist and was the only piece of jewellery she had ever given anyone, and that she would break the arm of whoever tried to remove it.{/n}", requires=(CUFF_WORN,)),
                    p("{n}She told the Commander once, in the dark, that the oath had been the first true thing anyone had sworn to her since the siege, and that the Commander had kept it, and that she had no idea what to do with a person who kept things. She was learning.{/n}", requires=(JUDGES,), forbids=(OATH_BROKEN,)),
                    p("{n}The broken oath was never mentioned between them after the night of the vigil. She said a vigil was for leaving something at the foot of a statue, and she had left it there.{/n}", requires=(OATH_BROKEN,)),
                    p("{n}On the night before the Threshold she came to the Commander's tent with Radiance in its saddle-leather scabbard and a lamp. She did not say anything. She set the lamp down, put the Commander's hand on the hilt beside her own, and held it there until the lamp went out.{/n}", requires=(CARRIES,)),
                    p("{n}A paladin of Iomedae who had once been a thief in Kenabres kept the lamp at the niche filled, every morning, for as long as the statue stood at the gate. Nobody asked her to. Yaniel called her Sister, and meant it, and Seelah pretended not to hear.{/n}", requires=(SEELAH_BLESSED,)),
                    p("{n}The sentries of the east wall told for years how the Commander once kissed the paladin on the parapet in front of the whole watch, with ichor to the elbows, and how she pushed the Commander off and said 'Not yet', and how everybody on the wall knew exactly what 'yet' meant.{/n}", requires=(Y + "raid_kiss",)),
                    p("{n}She never learned to sleep through the night. But on the nights the Commander stayed, she slept past the second bell, and she said that was worth more than a bed.{/n}", requires=(Y + "night_stayed",)),
                    p("{n}She fought dirty from then on, when it mattered, and never once admitted where she had learned it.{/n}", requires=(Y + "bout_dirty",)),
                    p("{n}The Commander never told her the truth about the lilitu. Whether she ever learned it, and from whom, and what she did about it, is a matter for the years after the war.{/n}", requires=(MINAGHO_SECRET,)),
                    p("{n}She never forgave the Commander for the lilitu, and she never stopped coming home. She said the two were not the same thing, and that anyone who thought they were had not lived long enough.{/n}", requires=(MINAGHO_TOLD,))))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.together")

SCENES.append(scene(Y + "epilogue.commit", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Yaniel and the Commander had finished what they had to settle. She rode to the Threshold with the Mendevian foot, in the rank behind the shields, and came back down the road on a cart with a broken leg and the whole of her temper.{/n}
{n}In the spring she came up the stair of the Commander's tower on crutches, with the iron cuff in one hand. She put it on the table between them. "Your sword for my shackle," she said, "and we are square. Or not. I have spent the winter on my back deciding which I would rather, and I will not tell you until you have told me."{/n}
{n}The Commander pushed the cuff back across the table. She looked at it, and at the Commander, and laughed, and threw the crutches on the floor.{/n}
{n}Afterwards she kept the flooded room in the gate tower, out of stubbornness, and slept there perhaps one night in three. The other nights she did not explain, and nobody in Drezen was fool enough to ask her.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", VERDICT, DRAWN), forbids=(COMMITTED, DECLINED, LEFT_FREE, CLOSED, OATH_BROKEN, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.commit")

SCENES.append(scene(Y + "epilogue.broken", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}The oath stayed broken. Yaniel never spoke of it again, and she never let the Commander speak of it either. She stood the night watch on the east wall of Drezen until the war was over, and when the Commander came up the stair she would move over on the parapet to make room, and hand across a cup, and that was all.{/n}
{n}She kept the flooded room in the gate tower. She never asked for her iron back. Once, years after the Threshold, she said to a young sentry who asked about the Commander that some people break their word and some people break their word and keep coming up the stair anyway, and that she had not yet decided which was worse. The sentry did not understand. She did not explain.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", OATH_BROKEN), forbids=(COMMITTED, LEFT_FREE, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.broken")

SCENES.append(scene(Y + "epilogue.unasked", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Yaniel and the Commander settled the matter of the sword after Iz, and never got as far as the other matter. The war did not leave time, and neither of them was the sort to take it when the war did not give it.{/n}
{n}She stood the night watch on the east wall of Drezen until the war ended and the watch was no longer needed, and then she stood it anyway. Once a year, on the night the Fane fell, the Commander found her on the wall, and they stood there together and watched the ash, and on one of those nights, many years later, she said that she had been waiting a long time for somebody to ask her something, and that she had got out of the habit of waiting. The Commander did not answer. The ash did not either.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", VERDICT), forbids=(DRAWN, COMMITTED, DECLINED, LEFT_FREE, OATH_BROKEN, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.unasked")

SCENES.append(scene(Y + "epilogue.unsettled", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Yaniel stood the night watch on the east wall of Drezen until the war ended and the watch was no longer needed, and then she stood it anyway. She kept the flooded room in the gate tower. She never did learn to sleep in a bed.{/n}
{n}What she and the Commander might have been was never settled, because the war did not leave them the time; she said afterwards that it had been the same for everybody she ever loved, and that at least this time nobody had died of it. Once a year, on the night the Fane fell, the Commander found her on the wall, and they stood there together without saying very much, and watched the ash.{/n}
{n}Once, years later, she said that the Commander had given her the one thing Minagho never could: a question left open. She said it the way other people say thank you.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", RETURNED), forbids=(VERDICT, COMMITTED, LEFT_FREE, CLOSED, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.unsettled")

SCENES.append(scene(Y + "epilogue.declined", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Yaniel hung her iron from a nail by the window of the gate tower, where it could see the road the refugees took, and there it stayed. She never wore it again. She never threw it away.{/n}
{n}She and the Commander were square, as she had asked, and she was scrupulous about it: she never owed the Commander so much as a cup of wine, and she never let the Commander owe her one. They were friends, of a sort, the careful sort. Some evenings, when the Commander came up the stair, she would be standing at the window with the iron in her hand, and she would put it back on its nail before she turned round.{/n}
{n}She lived a long time, as half-elves do when nothing kills them. When she died the iron was found in her hand, and the priest who laid her out did not know what it was, and put it in the coffin with her anyway, because she would not let go of it.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, LEFT_FREE, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.declined")

SCENES.append(scene(Y + "epilogue.left_free", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Yaniel finished her vigil alone, and in the morning she took her spear and went down the Drezen road, and did not come back. She was seen in the Wound for years afterwards, hunting alone, as the old paladin Berenguer was said to do; some said with him, and some said she had never met him in her life and did not need to.{/n}
{n}The painted martyr went into the cathedral of Drezen at midsummer. The real one never came to look at it. The Commander went, once, and stood in front of it for a while, and could not find anything in its face at all.{/n}''',
        paragraphs=(p("{n}Radiance went with her. It was never seen in Drezen again.{/n}", requires=(CARRIES,)),
                    p("{n}She took her iron with her, the one the Commander had given back. The sentries on the east gate said she had it in her fist when she went through, not on her wrist.{/n}", requires=(DECLINED,)),
                    p("{n}Once a year a letter came to Drezen with no name on it, in a square old-fashioned hand, from somewhere in the Wound. It never said much: the weather, a demon killed, a cart got through. It always ended the same way: keep my iron where I can find it.{/n}", forbids=(DECLINED,))))],
    requires=("trickster.ever", LEFT_FREE), forbids=(COMMITTED, "sacrifice"), **SAC, **EP))
tag(Y + "epilogue.left_free")

SCENES.append(scene(Y + "epilogue.mourned", "", "YanielEpilogue", 6, "", [
    nar("page", '''{n}Word came down to Drezen that the Commander had given everything at the Threshold and had not come back. Yaniel was on the east wall when the riders came in. She heard them out, and nodded, and went back to her watch.{/n}
{n}In the morning the sentries found her kneeling in front of her own statue at the foot of the gate tower, with a lamp burnt out beside her, and she did not get up for them.{/n}''',
        paragraphs=(
            p("{n}She had a husk's iron cuff in her hands. The Commander had carried it to the end; the riders had brought it back with the rest. She put it on the statue's stone wrist, where it did not fit, and left it there, and nobody in the Church dared take it off.{/n}", requires=(SHACKLE,)),
            p("{n}She stood the vigil for three nights, as a paladin does for a broken oath, and on the fourth morning she went back up on the wall.{/n}", requires=(OATH_BROKEN,)),
            p("{n}She had been owed a trade that was never made. She said, to nobody, that she supposed that meant she would have to keep owing, and she did, for the rest of her life, to anyone on the east wall who needed it.{/n}", forbids=(COMMITTED,)),
        ))],
    requires=("trickster.ever", STARTED, "sacrifice"), forbids=("trickster.commander_back",), **EP))
tag(Y + "epilogue.mourned")


# A page never plays for a woman the Commander killed in the Fane (the kill stands).
for _page in SCENES:
    if _page["Owner"] == "YanielEpilogue" and KILLED not in _page["Forbids"]:
        _page["Forbids"].append(KILLED)


# --- The secret (08 §3): the Commander kept the lilitu from her ---------------------------------------------------------------

household.secret(
    "yaniel_minagho", "What Minagho is to me",
    "Yaniel asked me what Minagho is to me, and I told her to leave the lilitu to me. "
    "It is very much her affair. Minagho kept her on a hook for seventy years, and ruined Staunton, and gave Drezen to the "
    "demons, and I keep her close. Minagho knows exactly who Yaniel is. She has not said anything yet.",
    portrait="Yaniel", witnesses=("yaniel", "minagho_chivarro"), risk="medium")


# --- Registration -------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        value = list(value) if isinstance(value, list) else value
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = value


def integrate(payload):
    """Her native reads (the Fane cues, the Iz song, the Fane answers, the Ch2 unmasking), the Radiance removal whitelist,
    her Chapter 5 latch, her Derived keys and the portrait fallback. The Radiance forms and the Fane latches bind on demand
    in trickster_world."""
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "SelectedAnswers", SELECTED)
    _bind(payload, "Latches", LATCHES)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    items = payload.setdefault("RemovableItems", [])
    for guid in ITEMS.values():
        if guid not in items:
            items.append(guid)
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)
    payload.setdefault("PortraitFallbacks", {}).setdefault("Yaniel", PORTRAIT_GUID)
