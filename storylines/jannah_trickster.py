"""Jannah Aldori on the Trickster path: "First blood" (Writer/handoffs/trickster/jannah.md for the canon research; the binding
plan is 11-ROSTER-PLAN-2 §2 with the coordinator's correction: duel law she honours, never a word made true).

Canon: a half-elf recruit of the Eagle Watch from Mivon, "an apprentice of a famous fencing master" (Seelah Q1 3f001f86)
who "won every encounter, I always won" (Deserter/Cue_0018 fb323aad) and signed up "four days before the demon attack! Am
I lucky, or what?" (52169bb4). Seelah: "She couldn't have become an Aldori otherwise" (a955505e). She ran at the
Houndheart camp ambush, north toward Numeria (e2c02200, 78c0efc7), and the vrocks caged her in the Molten Scar: "It was my
first real battle against actual demons" (Deserter/Cue_0015 423ff883). The [Attack] answer (Answer_0026 3dce20ad) plays
Cue_0027 199d4dbf: "Her fencer's instincts allow Jannah to react to the danger, but the cage is too small and she cannot
evade your weapon. Jannah falls to the floor dead, her eyes wide and unseeing." Alive, she returns in Seelah's Q3 "calm
and collected... a scar on her right temple, jagged and fresh" (ktc_DeserterJoins/Cue_0001 7f36934a), afraid of being
"written out of my own life story" (Cue_0022 cfcafcf2); refused, she goes back to the Condemned (Cue_0030 7fc6b68e).

Devices, earned in play:
- killed worlds: "Aldori terms". At the cage a Knowledge (World) check names the Aldori forms to her (to the first blood;
  the one who bleeds lays down her blade and lies where she falls, eyes open, until the victor quits the circle); then,
  before the native [Attack], the Commander issues the formal Mivon challenge and passes her own sword through the bars.
  Her pride accepts. The native blow ("Death to deserters!", shouted for the onlookers) lands as first blood along her
  right temple. A scalp cut sheets her face in blood, and a yielded Aldori lying still with open eyes is a corpse to anyone
  who does not know the forms. She yielded; the Commander walks away knowing it. In Chapter 5 she turns herself in at the
  Drezen cells (her canon JannaInPrison_Locator) to have the unclaimed yield claimed.
- living worlds: "a duel of stories". She has put herself in those cells to wait for the Condemned wagon and will take no
  pardon. Her master's wine-hour game, blood and tale: each tells the other's part of the Houndheart ambush, and the first
  lie caught is first blood. The Commander wins by catching the lie she tells against herself (or cheats a false catch, a
  Ledger secret), or loses, and she serves the posting and comes back on her own word.
Cost: her unbeaten record (the cage, or the story) and the scar; the Commander's public yield if she draws first blood at
the muster. The commit is hers: a public Aldori rematch at the muster, for the only stake the forms allow (her record, answered
or standing); the bout decides only that. Afterwards she chooses, and her yes is her own act. Her no is always the
Commander's doing: a bout thrown to her, her record mocked before the muster, the forms refused after losing, or the false
catch kept. A circle left chalked in the yard is the later yes, unpriced.
The spine between return and commit is jannah_circle (the forms, Houndheart, the wall).
"""
from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "jannah"
P = "jannah.trickster."
C = "jannah.circle."
UNIT = "4880d0b16ca74fa46a167914e2b44bcc"          # CR4_DeserterJanna (the cage, the Drezen cell, Seelah's Q3)
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
LOCATOR = "e595a2a6-e8ca-4d13-9010-f482088a4a27"   # JannaInPrison_Locator (JannaInPrison_Drezen 478931ef, Janna_Prison 1e069277)
PRESENCE = "jannah.presence"
# Q6 follow-up (INT/COX): the cell before her return (the letter's world, waiting on the wagon) and the cell after the wagon,
# so blood and tale and the wagon's return are met in person, not delivered at a rest. Each is exclusive with the others.
CELLS_PRESENCE = "jannah.presence.cells"
BACK_PRESENCE = "jannah.presence.back"
FIRST_LIST = "b2b77a591c8808f409aa2083bd1b318a"    # c3/MoltenScar/Deserter/AnswersList_0003 (her first questions)
FIRST_CUE = "8c909dc650b9dff408a0d144da24b920"     # Deserter/Cue_0059 "Yes... that's right. You know everything..." (a clean cue on it)
CAGE_LIST = "170fd7a11f66c88428bc27bfba3a569f"     # Deserter/AnswersList_0021 ([Open the cage] x2, [Attack] Answer_0026 -> Cue_0027);
                                                   # reached only without Seelah in the group (her branch breaks the lock)
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"   # NPC_Common/Irabeth/AnswersList_0009
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"    # CompanionDialogues/Seelah/AnswersList_0003
KING_C5 = household.KING_C5                        # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_RETURN = household.KING_C5_RETURN          # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"

STARTED = "jannah.started"
CLOSED = "jannah.closed"
COMMITTED = "jannah.committed"
# Native state (trickster_world BINDINGS).
DEAD = "jannah.dead"                              # JannaDead_SeelahDoesntKnow f8129442 (Cue_0027)
DEAD_KNOWN = "jannah.dead_known"                  # JannaDead_SeelahKnows 699b1ad8 (Seelah told, Cue_0105 166223b5)
DEAD_L = "jannah.dead.latched"
FREE = "jannah.free"                              # JannaFree d99770b1
PRISON = "jannah.prison"                          # JannaInPrison 59632e17
CONDEMNED = "jannah.condemned"                    # JannaInCondemned 46f4524c
JOINED = "jannah.joined"                          # ktc_DeserterJoins/Cue_0019 651ecf0c (Seelah's Q3)
REFUSED = "jannah.refused_q3"                     # ktc_DeserterJoins/Answer_0017 e66c11e6 "You need to leave Drezen."
Q3_STARTED = "seelah.q3_started"                  # WeightOfMySword_SeelahQ3_quest 5a5a533c (started)
SOULS = "seelah.souls_returned"                   # the same quest, completed
ELAN_DEAD = "seelah.elan_dead"
# Q6 r5 (CAN): the Commander was at the Houndheart camp with her (Seelah Q1 KnightCamp: Elan's chest, Cue_0011 2100f41a;
# "Jannah and I will look around the northern side", Cue_0012 f75430d6). The duel of stories tells that day, so it needs it.
HH_SEEN = "seelah.houndheart_seen"
HH_SEEN_CUES = ["2100f41ae724734418dc74b15719543e", "f75430d6f83e9864ca9b16db1a170bd1"]
# Q6 r6 (CAN): she handed her sword through the bars (Deserter Cue_2 / Cue_5, AddItemToPlayer); the Commander cut Seelah
# down at the cage after Seelah broke the lock (Deserter Answer_0057 [Kill Seelah]).
SWORD_GIVEN = "jannah.sword_given"
# Q6 follow-up (CAN): the Commander saw her creep up on the quasit alone (KnightCamp Cue_0017 "sneaks up on it while the
# others talk"); the shared catch remembers it only then, and otherwise reads her tell.
QUASIT_SEEN = "jannah.quasit_seen"
QUASIT_SEEN_CUES = ["da671fced713af6419502ca50bdeb94c"]
SWORD_GIVEN_CUES = ["decaff681a6646ea8102a1860fcbd172", "5ddbadee4a3b4d169ad9fbe7a7f62253"]
SEELAH_KILLED_AT_CAGE = "jannah.seelah_killed_at_cage"
SEELAH_KILLED_ANSWER = "b1cf64a1c5af84c46b578fa82f865d66"
SEELAH_DEAD = "seelah_dead"
SEELAH_GONE = "seelah_gone"
SEELAH_BACK = "seelah.trickster.returned"

# The device, killed worlds.
NAMED = P + "primed.forms_named"                  # the Commander named the Aldori forms to her (Knowledge (World))
PRIMED = P + "primed"                             # the challenge made and accepted, her sword passed, before the native [Attack]
BOTCHED = P + "cage.botched"                      # the forms garbled; the cage is only an execution now
ASH_SILENT = P + "ash.said_nothing"
ASH_SAID = P + "ash.said_sentence"
COST_ASH = P + "cost.left_in_ash"
CLAIMED = P + "yield.claimed"
RELEASED = P + "yield.released"
NAMELESS = P + "cost.nameless"                    # dead on the rolls, kept so (the Evil claim)
SCAR = P + "cost.temple_scar"
# The device, living worlds.
IN_CELLS = P + "alive.in_cells"
Q3_SETTLED = P + "alive.q3_settled"
POSTED = P + "alive.posted"                       # she won the story; the Condemned wagon took her north
CAUGHT = P + "alive.caught_her"                   # the Commander caught the lie she told against herself
LIED = P + "alive.false_blood"                    # a false catch, bluffed: the Ledger secret below
SECRET = "trickster.secret.jannah_false_blood"
SECRET_KNOWN = SECRET + ".known.jannah"
STORY_LOST = P + "cost.story_lost"                # the Commander lost the story; she came back on her own word
STRANGER = P + "alive.visitors_way"               # Q6 follow-up (INT): no shared Houndheart; each told her own bout
POSTING = P + "cost.posting"
# Both worlds.
RETURNED = P + "returned"
FIRST_LOSS = P + "cost.first_loss"                # her unbeaten record, gone
GONE = P + "gone"
DECLINED = P + "declined"                         # she threw the bout
CONFESSED = P + "confessed"
HELD_LIE = P + "held_the_lie"
YOU_FIRST = P + "bout.commander_first"
SHE_FIRST = P + "bout.her_first"
PUBLIC_YIELD = P + "cost.public_yield"            # the Commander lay down in the sand before the muster
REFUSED_YIELD = P + "refused_the_yield"
LATE_YES = P + "chalk_circle.walked_in"
THREW = P + "threw_the_bout"                    # the Commander handed her the bout (her no)
SHAMED = P + "shamed_her"                        # the Commander mocked her record before the muster (her no)
LATE_YIELD = P + "cost.late_yield"               # the yield owed from the muster, given in the empty yard
PUBLIC_REPAIR = P + "public_repair_promised"
RECKONED = C + "seelah.cage_reckoned"
LATE_CLEAR = P + "late_committed.without.unpaid_debts"
LATE_COMMITTED = P + "late_committed"
PRESENCE_ON = P + "presence_on"
# The spine (jannah_circle); scene ids double as flags once the scene completes.
FORMS = C + "forms"
HOUNDHEART = C + "houndheart"
WALLS = C + "walls"
NIGHT = P + "circle_night"
MORNING = P + "morning"
HH_HONEST = C + "hh.honest"
HH_LUCKY = C + "hh.lucky"
HH_STAND = C + "hh.stand"
WALL_SALUTE = C + "walls.saluted"
WALL_SHIELD = C + "walls.shielded"
WALL_WATCHED = C + "walls.watched"
SEELAH_HERSELF = C + "seelah.herself"
SEELAH_FOR_HER = C + "seelah.told_for_her"
SEELAH_KEPT = C + "seelah.kept"
MIVON_TRUTH = C + "mivon.truth"
MIVON_LEGEND = C + "mivon.legend"

RELATIONSHIP = dict(
    Title="First blood",
    Description=("Jannah Aldori, a half-elf duellist of Mivon who never lost a bout and ran from one battle. She keeps "
                 "the Aldori forms the way other people keep a faith. I have had to learn them."),
    Objective="Answer Jannah Aldori",
    Guidance=("On the Trickster path. At the Molten Scar, do not strike the deserter in the cage: a blow there kills her. "
              "If she lives, look for her in Chapter 5 in the old cells under the Drezen citadel, where she has put "
              "herself. She fights her own duels, and she may throw one."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, DEAD_KNOWN, GONE], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED, DEAD_KNOWN: RETURNED},
    TricksterAccess={
        "killed": dict(detect=[DEAD], device=P + "killed.yield", returned=RETURNED),
        "killed_known": dict(detect=[DEAD_KNOWN], device=P + "killed.yield", returned=RETURNED),
        "alive": dict(detect=["!" + DEAD, "!" + DEAD_KNOWN], device=P + "alive.stories", returned=RETURNED),
    },
)

PRESENCES = {
    # A copy of her own unit at her own canon Drezen mark: the last cell of the old gaol, where Janna_Prison translocates
    # her in Chapter 3 (that native placement runs in Chapter 3 only; this one is Chapter 5 only). No other presence uses
    # this locator; a later route that does must stand at least 2 m off it.
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", ManageNative=True, At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                   Requires=["trickster.ever", PRESENCE_ON], Forbids=[CLOSED, GONE], MinChapter=5, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   Greeting="{n}In the last cell of the old gaol, with its door standing open, a half-elf in a patched "
                            "gambeson sits on the bunk with a practice sword across her knees. She has "
                            "scratched a circle into the floor stones with its point, three paces across, and she keeps "
                            "her boots out of it.{/n}"),
    # Living worlds, after her letter and before blood and tale is settled. Off while she rides the wagon.
    CELLS_PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", ManageNative=True, At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                         Requires=["trickster.ever", IN_CELLS], Forbids=[CLOSED, GONE, POSTED, PRESENCE_ON], MinChapter=5, MaxChapter=5,
                         AnswerLists=[], Dialog="hub", DelayHours=12,
                         Greeting="{n}The last cell of the old gaol has its door standing open; the turnkey has given up on the "
                                  "lock. A half-elf in a patched gambeson sits on the bunk with her back to the wall and her boots "
                                  "on the blanket, and does not get up.{/n}"),
    # The lost tale: back from the Condemned wagon's ford (36 hours after it left), in the same cell.
    BACK_PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", ManageNative=True, At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                        Requires=["trickster.ever", POSTED], Forbids=[CLOSED, GONE, PRESENCE_ON], MinChapter=5, MaxChapter=5,
                        AnswerLists=[], Dialog="hub", DelayHours=36,
                        Greeting="{n}The last cell of the old gaol is occupied again. Its occupant is grey with road dust, and "
                                 "one sleeve of her gambeson has been sewn shut with black surgeon's thread.{/n}"),
}

DERIVED = {
    # Killed worlds: she is in the cell from Chapter 5 once the forms were kept at the cage; living worlds: once she is out
    # of the story duel (or back from the wagon). The posting keeps her off the locator until she walks back in.
    PRESENCE_ON: [[DEAD_L, PRIMED], [RETURNED]],
    # A Seelah's Q3 in progress is left to finish before she writes from the cells.
    Q3_SETTLED: [[REFUSED], [SOULS]],      # quality pass Q6 (INT): joining Q3 is not finishing it; the souls must be home
    # R2-6: the war can end between the wall and the muster; her page answers it after the Threshold.
    LATE_COMMITTED: [["trickster.ever", WALLS, LATE_CLEAR]],
    LATE_CLEAR: [["trickster.ever", P + "truth_clear", P + "repairs_clear", P + "cage_reckoning_clear"]],
    P + "truth_clear": [[P + "no_false_blood"], [CONFESSED]],
    P + "no_false_blood": [["trickster.ever"]],
    P + "repairs_clear": [[P + "not_declined"], [LATE_YES]],
    P + "not_declined": [["trickster.ever"]],
    P + "cage_reckoning_clear": [[P + "no_cage_killing"], [P + "seelah_not_back"], [RECKONED]],
    P + "no_cage_killing": [["trickster.ever"]],
    P + "seelah_not_back": [["trickster.ever"]],
    # 05 §2.5 voice note (morning after): she joins, but she will have it remembered who chalked the circle first.
    "jannah.harem.voice.first_blood": [[COMMITTED]],
}


def jan(id, text, *choices, **kw):
    return n(id, "Jannah", text, *choices, portrait="Jannah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Jannah", **kw)


def meet(id, title, entry, nodes, requires, forbids=(), delay=24, optional=False, hub=PRESENCE, **extra):
    """A physical scene at her cell (Chapter 5; the gaol is under the capital's citadel)."""
    SCENES.append(scene(id, title, "Jannah", 5, entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, *forbids))), delay=delay, last=5,
                        optional=optional, Relationship=REL, Chapters=[5], ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=hub, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, kind="visit", chapter=5, optional=False, **extra):
    """A rest-delivered scene: a letter from her, or a night in which she is there in person."""
    SCENES.append(scene(id, title, "Jannah", chapter, "", nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))) if "trickster" not in requires
                        else tuple(dict.fromkeys(requires)),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, *forbids))), delay=delay, last=chapter,
                        optional=optional, Relationship=REL, Remote=True, Kind=kind, Chapters=[chapter],
                        # Q6 r2 (COX): her Chapter 5 visits are manual reads (her book, "choose Read"); only the letter from the
                        # cells arrives at a rest, which keeps her inside the ledger's Chapter 5 allocation.
                        **({"ManualOnly": True} if kind == "visit" and chapter == 5 and not extra.get("TricksterDevice") else {}), **extra))   # Q6 r6 (INT): the device pages (stories, wagon) arrive at a rest


# --- Killed worlds, Chapter 3: the forms at the cage (inline, before the native [Attack]). -----------------------------
# Quality pass Q6 r3: RETIRED BY GATING (both primers forbid chapter_later, held by the runtime in every chapter from 2 on;
# ids, nodes and choice indices kept). The native [Attack] (Answer_0026 -> Cue_0027 199d4dbf) narrates her death and plays
# KillJanna (103de7bd), whose CommandAction 3d7d10a2 executes a real Kill and whose CommandAction 1 opens the cage. A
# staged survival needs a primed substitution of that outcome, which the engine does not have (contract, for a later E-item:
# a primed-only authored cue ahead of Cue_0027 in Answer_0026.NextCue, running StartEtude JannaDead_SeelahDoesntKnow
# f8129442 without PlayCutscene, plus a native-unit hide on leaving the area; verified in the harness in both branches).
# Until it exists the cage is the Commander's own choice of a non-partner's death, and canon stands (11-ROSTER-PLAN-2
# section 5, ruling #2). Her Trickster route is the living worlds: the duel of stories.

SCENES.append(scene(P + "cage.forms", "The forms", "Jannah", 3,
    '"In Kenabres you boasted of a fencing master in Mivon. Did he teach you the forms?"',
    [jan("start", '''{n}The word reaches her somewhere under the fear. Her chin comes up a finger's breadth, the way a fencer's does when she sees a salute begin.{/n}
"He taught me everything. The salute, the measure, the forms. Seven years in his salle above the dyers' yards." {n}Her voice cracks on the last word. You watch her hate that it cracked.{/n}
"Why? Nobody gives the forms to a deserter. You give a deserter a rope."''',
         c('[Knowledge (World)] "Mivon was built by Aldori who fled Rostland. Anyone who wants to stay there fights for the right, bout after bout. So tell me how a bout to the first blood ends, in his salle."',
           check=dict(Skill="SkillKnowledgeWorld", DC=22, Success="named", Failure="garbled")),
         c("[Let it go.]", abort=True)),
     nar("named", '''{n}You have it right: the Aldori who fled Rostland, the city they made on the river, the duels a stranger must win to stay, the Aldori way of taking a blade out of a hand rather than a life out of a body. She hears it as if you were reading her own name off a wall.{/n}''',
         c("Continue", "named_her")),
     jan("named_her", '''"In his salle?" {n}Something in her face, which the vrocks spent weeks emptying out, fills back up. It isn't hope. It's older than hope, and it stands up straighter.{/n}
"Not Mivon's way. His. The salute, the chalk circle, and nobody steps out of it unbloodied. To the first blood and no further. The one who bleeds lays down her blade and lies where she falls, eyes open, not moving, until the victor has left the yard. He said a fencer who can't lose properly will one day lose her life improperly. He made us practise it for an hour at a time." {n}She says it the way a novice recites a verse she hated learning.{/n}
"And whatever the victor says over you, that's the end of it. Whatever they leave unsaid, you owe until it's said. He was a hard old man." {n}She looks at you through the bars.{/n} "Why does the Commander of the crusade want to know how an old man in Mivon ended his bouts?"''',
         c('"So that when I decide what to do with you, I can offer them to you."', flags=(NAMED,)),
         c('"Keep them close. You may need them before this cage is open."', flags=(NAMED,))),
     nar("garbled", '''{n}You get Mivon wrong: you make it a Brevic city, and the Aldori a school of cavalry sabres. Jannah listens the way a master listens to a first-year student murder a verse.{/n}''',
         c("Continue", "garbled_her")),
     jan("garbled_her", '''"No. You've never been anywhere near Mivon." {n}The pride goes back wherever it was hiding, and what is left is a frightened girl in a cage.{/n}
"If you mean to kill me, Commander, kill me. Just don't pretend you know where I come from."''',
         c("[Step back from the cage.]", flags=(BOTCHED,)))],
    requires=("trickster",), forbids=(NAMED, BOTCHED, "chapter_later"), last=3, Relationship=REL, Chapters=[3],   # retired (Q6 r3)
    AnswerLists=[FIRST_LIST], NativeReturnCue=FIRST_CUE, EntryMythic="PlayerIsTrickster", TricksterDevice=True))

# The challenge itself, invoked before the native [Attack] (on the sentence list she reaches only when Seelah is not there
# to break the lock): her pride accepts, she takes her own sword through the bars, and the native answers come back. The
# Commander's [Attack] ("Death to deserters!") is then the cut, and first blood (see the ash for what the Commander meant by
# shouting it).
SCENES.append(scene(P + "cage.terms", "To the first blood", "Jannah", 3,
    '[Take her sword from the ash beyond the bars] "Then I challenge you by your master\'s forms, Jannah Aldori. To the first blood, and the one who bleeds yields."',
    [jan("accept", '''{n}She looks at the long Aldori blade in your hand, slightly curved, its grip wound in leather gone black with handling. She knows it better than her own face.{/n}
"In a cage a pace and a half across, where I can't take one step." {n}She laughs, short and ugly.{/n} "They'll call it an execution with a bow in front of it."
"That's what you're counting on, isn't it? That I'd rather lose a bout than be butchered. That I'm still that proud." {n}She wipes her face with the back of a filthy wrist and gets up off the floor of the cage, one hand on the bars.{/n} "You're right. Give me my blade."''',
         c("[Pass her sword through the bars, hilt first, with a healing draught and a roll of linen wound under the grip where only her hand will find them.]", "guard"),
         c('"No. Not like this."', abort=True)),
     nar("guard", '''{n}She takes the hilt the way other women take a hand at a dance. The cage leaves her no footwork at all, so she sets her rear heel against the bars, sinks her weight, and brings the long blade up into a high guard, the only line the bars allow. Then she salutes you through the gap, flat of the blade to her brow, and her eyes above it are perfectly dry.{/n}
"Jannah Aldori. Of Mivon." {n}Her fingers have found what is under the grip. Her face does not change at all; seven years in a salle teach you that too.{/n} "Ready."''',
         c("[Take your guard, and choose your line: high, for the temple and first blood, not the throat.]", flags=(PRIMED,)),
         c("[Lower your blade, and take her sword back through the bars.]", abort=True))],
    requires=("trickster", NAMED), forbids=(PRIMED, "chapter_later"), last=3, Relationship=REL, Chapters=[3],   # retired (Q6 r3)
    AnswerLists=[CAGE_LIST], ReturnToList=True,
    ReturnText="{n}She is on her feet in the cramped cage, blade high in the Aldori guard, eyes on you, waiting for your move.{/n}",
    EntryMythic="PlayerIsTrickster", TricksterDevice=True))


# The same night, alone: where the blade went (a memory; the Commander knows what the companions saw, and what they didn't).
visit(P + "cage.ash", "Where the blade went", [
    nar("open", '''{n}That night, by the light of a camp lamp at the edge of the Scar, you clean her blood off your blade and go over the bout the way she would have: cut by cut, in order.{/n}
{n}You shouted the old sentence as you cut, "Death to deserters!", loud enough for everyone behind you to hear. The forms let the victor say whatever they like before the blood. You needed your companions to hear an execution.{/n}''',
        c("Continue", "cut")),
    nar("cut", '''{n}Her guard came up where the forms put it and the bars allowed it, high and forward. Your cut rode down the flat of her sword to the hilt, turned off the crossguard, and opened her right temple from the brow to above the ear. Not deep. Scalp wounds never need to be deep. They bleed as if the whole head were emptying.{/n}''',
        c("Continue", "fall")),
    nar("fall", '''{n}She went down on her back with her face a red mask and her eyes wide open, fixed on the roof of the cage. Her master's rule, the one she had recited to you through the bars: a fencer who has yielded does not close her eyes, does not wipe away the blood, does not move a finger until the victor has gone. She kept it. She had chosen to. She breathed through her teeth, shallow and slow, the way the old man taught his students to breathe while they lay in the chalk; with that much blood on her face, nobody looking from outside the bars could have told breath from the heat-shimmer of the Scar.{/n}
{n}Your companions saw an execution, because you had shouted one. Nobody went into the cage to be sure: you were already out of it and giving the order to move, and nobody wanted to be the one to kneel in a deserter's blood.{/n}
{n}Everything else she needed you had put in her hand. A sword, and the cage's lock was vrock iron gone rotten in the heat; Seelah had once broken one like it with a single blow. A healing draught and a roll of linen, wound under the grip. And the dark, which the vrocks spend over their ritual pits on the far side of the Scar. What she needed from herself was only not to blink. You chose to trust her with that, because the only other way to leave her alive was to leave her in front of witnesses who would ask why.{/n}''',
        c("[Remember that you said nothing over her, and walked out of the circle.]", "silent", flags=(ASH_SILENT, COST_ASH)),
        c('[Remember what you said over her] "Sentence carried out."', "sentence", flags=(ASH_SAID, COST_ASH))),
    nar("silent", '''{n}Under the forms, a yield the victor leaves unspoken is owed until it is spoken. You left hers lying in the ash with her. Whether she ever comes to collect it is hers to decide.{/n}
{n}Out in the dark the vrocks are circling back to their cages and their ritual. You hope she remembers to be dead for them too.{/n}''',
        c("[Put out the lamp.]")),
    nar("sentence", '''{n}You said it loud enough for everyone to hear, and she heard it too. By her master's rule, whatever the victor says over the yield is the end of the matter. The sentence was death to deserters, and it has been carried out: Jannah Aldori, recruit of the Eagle Watch, is dead. What the woman lying in the ash does with that is hers to decide.{/n}
{n}Out in the dark the vrocks are circling back to their cages and their ritual. You hope she remembers to be dead for them too.{/n}''',
        c("[Put out the lamp.]")),
], requires=("trickster.ever", DEAD_L, PRIMED), forbids=(RETURNED,), delay=6, kind="memory", chapter=3, optional=True,
    TricksterDevice=True)


# --- Killed worlds, Chapter 5: the unclaimed yield, in her own cell. -------------------------------------------------

meet(P + "killed.yield", "An unclaimed yield", '"The turnkey says there\'s a dead woman in my cells."', [
    nar("open", '''{n}The turnkey swears she walked in off the street at the change of the watch, gave a name that is on the Eagle Watch's roll of the dead, and asked for a cell. He gave her the last one because it was empty and because, he says, she had the look of someone who would take one anyway.{/n}
{n}She is standing when you come down the steps, in a patched gambeson with a long Aldori blade at her hip. A scar runs from her right brow to above the ear, pink and badly knitted: your blade's work, and nobody's healing.{/n}''',
        c("Continue", "salute")),
    jan("salute", '''{n}She salutes you, flat of the blade to the brow, and sheathes again before you can decide whether to return it.{/n}
"Commander. Jannah Aldori, of Mivon. I yielded to you in the Molten Scar."''',
        c("Continue", "unsaid", forbids=(ASH_SAID,)),
        c("Continue", "said", requires=(ASH_SAID,))),
    jan("unsaid", '''"You shouted your sentence as you cut, for the others to hear. That was before the blood. Over me, after it, you said nothing, and quit the circle. By the old man's rule, a yield nobody claims is owed until somebody does. I've been owing you since the Scar." {n}She says it like a debt to a moneylender.{/n}
"I don't like owing. So I came to hear what you'd say."''',
        c("Continue", "how")),
    jan("said", '''"You said the sentence was carried out, and quit the circle. So it was. Jannah Aldori of the Eagle Watch is on the rolls of the dead. I read her name on the board by the chapel on my way in. They spelled it wrong."
{n}Something dry happens at the corner of her mouth.{/n} "So I came to ask who that leaves standing in your cells."''',
        c("Continue", "how")),
    jan("how", '''"You'll want to know how. I lay in the ash until your boots were out of hearing. Then I counted to a thousand, because my master used to say a victor's field is exactly as big as a victor's pride, and I didn't know how proud you were."
"Then I found what you'd wound under my grip. I drank the draught first. It closed the cut to a seam, enough that I stopped leaving a trail. Then I packed the linen over the seam and tied it with my belt, and broke the lock with my pommel. Three blows. Seelah would have done it in one." {n}A dry twist of the mouth.{/n}
"I went down into the lava channels, where the air is too hot for wings, and walked south by night until the Scar was behind me. After that it was only walking."''',
        c('"And after that?"', "after"),
        c('"You could have kept walking."', "after")),
    jan("after", '''"I hired on with a salt caravan to Nerosyan under a name I made up and was bad at answering to. I guarded salt all winter. Nobody asked me a single thing." {n}She touches the scar, not the way people touch a wound: the way a fencer checks her guard.{/n}
"Then word came up the road that the Commander was back out of the Abyss, and I found I couldn't go on being a salt guard called nothing while I still owed you a yield."''',
        c("Continue", "record")),
    jan("record", '''"Seven years in the circles of Mivon, and I never once bled first. Not in a tournament, not in a quarrel, not against the bandits on the river roads. You were the first."
"I want you to know I haven't forgiven you for it. I'm not sure I want to."''',
        c("Continue", "seelah_known", requires=(DEAD_KNOWN,)),
        c("Continue", "claim", forbids=(DEAD_KNOWN,))),
    jan("seelah_known", '''"The turnkey says Seelah came down to the gaol after the Scar, asking whether anybody had brought in a body. Nobody had." {n}Her jaw sets.{/n}
"Don't tell her. Not yet. I'll do it myself, when I can look at her without being sick."''',
        c("Continue", "claim")),
    jan("claim", '''"So. Say it now. Whatever you say over me is the end of the matter, and I'll keep it. I'm an Aldori. That's all the Scar left me."''',
        c('[Claim the yield] "Then here it is. You live, under your own name, and you stay where I can find you."', "claimed",
          flags=(CLAIMED, RETURNED, STARTED, FIRST_LOSS, SCAR)),
        c('[Release the yield] "I release it. You owe me nothing. Go wherever you like."', "released",
          flags=(RELEASED, RETURNED, STARTED, FIRST_LOSS, SCAR)),
        c('[Claim it for yourself] "You\'re dead on the rolls. Stay dead. You\'ll fight where I send you, under no name at all."',
          "nameless", flags=(NAMELESS, CLAIMED, RETURNED, STARTED, FIRST_LOSS, SCAR), alignment=("Evil", 1)),
        c('[Dismiss her] "You\'re nothing to me. Get out of my gaol."', "dismissed", flags=(CLOSED, GONE))),
    jan("claimed", '''"Under my own name." {n}She repeats it the way you'd test an edge on a thumbnail.{/n}
"The Watch has me dead. Irabeth will have views. You'll have to tell her, because I'm not going to." {n}She sits down on the bunk, and only then does she look tired.{/n}
"All right. I'll stay where you can find me. I thought that would be harder to say."''',
        c("[Leave her to the cell.]")),
    jan("released", '''"Released." {n}She takes it like a blow she had been warned about.{/n}
"In the old man's salle that's an honour. The victor saying the loser owes nothing; he'd chalk it on the wall. Here it just means you're done with me."
{n}She doesn't move toward the steps.{/n} "I'm staying anyway. Not because I owe you. Because I chose it, and that's the first thing I've done since the Houndheart camp that my legs didn't choose for me."''',
        c("[Leave her to the cell.]")),
    jan("nameless", '''{n}It lands. You watch it land. Then she straightens, heels together, the way a recruit stands for a sentence.{/n}
"As you say. No name." {n}Her voice is perfectly even.{/n}
"I'll keep it. Under the forms I have to. Don't expect me to like you for it, Commander."''',
        c("[Leave her to the cell.]")),
    nar("dismissed", '''{n}You turn your back on her and climb the steps. Behind you there is no sound at all: she does not move until you have gone. She never has.{/n}
{n}In the morning the last cell is empty. On its floor someone has scratched a circle into the stones with a sword's point, and in the middle of it one word: PAID.{/n}''',
        c("[Let her go.]")),
], requires=(DEAD_L, PRIMED), forbids=(RETURNED,), delay=24, TricksterDevice=True)


# --- Living worlds, Chapter 5: the letter from the cells, and the duel of stories. -----------------------------------

visit(P + "alive.letter", "From the last cell", [
    nar("open", '''{n}The letter is folded small and sealed with candle wax, no signet. The hand is upright and exact, every stroke finished, like someone who was taught to write by the same master who taught her to cut.{/n}''',
        c("Continue", "joined", requires=(JOINED, CONDEMNED)),
        c("Continue", "refused", requires=(REFUSED,), forbids=(JOINED,)),
        c("Continue", "condemned", requires=(CONDEMNED,), forbids=(JOINED, REFUSED)),
        c("Continue", "prison", requires=(PRISON,), forbids=(JOINED, REFUSED, CONDEMNED)),
        c("Continue", "free", requires=(FREE,), forbids=(JOINED, REFUSED, CONDEMNED, PRISON)),
        c("Continue", "unmet", forbids=(JOINED, REFUSED, CONDEMNED, PRISON, FREE)),
        c("Continue", "joined_free", requires=(JOINED,), forbids=(CONDEMNED,))),
    jan("joined_free", '''"Commander. The jeweller is dead and we got the souls back. I came to you on my own feet, nobody's prisoner, and I held the mouth of that hole for Seelah because I chose to. Now it's done I've chosen again. I've asked the Condemned for a place. The sergeant said yes before I'd finished asking, which I'm choosing to take as a compliment."
"I didn't run. Not once, at the mouth of that hole. I'd like that written down somewhere, and you're the only one who writes things down who might believe it."''',
        c("Continue", "wagon")),
    jan("joined", '''"Commander. The jeweller is dead and we got the souls back. The Condemned only let me go to find you in Drezen; if you'd turned me away I'd have gone straight back to them. You didn't turn me away. I'm going back anyway. The hunt's over, and a deserter who stays on only because nobody sent her back hasn't settled anything."
"I didn't run. Not once, at the mouth of that hole. I'd like that written down somewhere, and you're the only one who writes things down who might believe it."''',
        c("Continue", "wagon")),
    jan("refused", '''"Commander. You told me to leave Drezen. I went as far as the north gate and came back, and I've put myself in the old cells under the citadel."
"I've put myself where you can find me, and I'll go when the crusade sends me, not before. I was never going to run twice."''',
        c("Continue", "wagon")),
    jan("condemned", '''"Commander. My Condemned company came through Drezen on its way to the north gate. The sergeant lets us sleep in the gaol when we're in a town, so he can count us in the morning. I'm writing from the last cell."
"He says I'm the only one of his who ever asked to be counted."''',
        c("Continue", "wagon")),
    jan("prison", '''"Commander. You sent me to these cells after the Molten Scar. I'm in them again, and this time I asked."
"I've asked for the Condemned. This time I mean to be sent."''',
        c("Continue", "wagon")),
    jan("free", '''"Commander. I walked out of the Molten Scar with the cage open behind me and no chain on me. I went to Kenabres and tried to be nobody. It didn't take. I'm bad at being nobody; I was raised to be looked at."
"So I came back and gave the gaol my name, and they didn't know what to do with it, so they gave me a cell."''',
        c("Continue", "wagon")),
    jan("unmet", '''"Commander. You may not know my face. Jannah Aldori, of Mivon. I ran at Houndheart. The vrocks caged me in the Molten Scar. I slipped out under their beaks. Very neat. No. It wasn't neat. I worked a fastening loose for nights with a sliver of bone. When they went to feed, I squeezed through. Left skin off my hand on the iron. I hid in the ash till they stopped looking. Then I walked here and asked the gaol for a cell. This one I can open."''',
        c("Continue", "wagon")),
    jan("wagon", '''"The Condemned wagon goes north at the ninth bell of Oathday, and I mean to be on it. I'm writing so you'll hear it from me and not from a turnkey, and not think I ran again."''',
        c("Continue", "sign")),
    nar("sign", '''{n}It is signed "J. Aldori, of Mivon", and under the name, very small, a circle with one stroke through it: her old salle's mark, the kind of thing a student draws in the margins for years after she has left.{/n}''',
        c("[Fold the letter.]", flags=(IN_CELLS,))),
], requires=("trickster",), forbids=(DEAD, DEAD_KNOWN, RETURNED, IN_CELLS, Q3_STARTED), delay=24, kind="letter",
    ForbidOverrides={Q3_STARTED: Q3_SETTLED}, RequiresAnyGroups=[[JOINED, REFUSED, "coronation.seen"]])


# Q6 follow-up (INT/COX): met in person on her cell hub, not delivered at a rest (her letter is her one Chapter 5 rest delivery).
meet(P + "alive.stories", "Blood and tale", '"About the Condemned wagon."', [
    nar("open", '''{n}The old gaol under the citadel smells of wet straw and lamp oil. The last cell's door stands open; the turnkey has given up on the lock. Jannah sits on the bunk in a patched gambeson with her back to the wall, her boots on the blanket and a borrowed practice sword across her knees. She has scratched a circle into the floor stones with its point.{/n}''',
        c("Continue", "start")),
    jan("start", '''"You got my letter." {n}She doesn't get up.{/n} "Then you know what I'll say to a pardon, so don't waste the ink."''',
        c('[Offer her a pardon] "Signed and sealed. You walk out of here tonight."', "pardon"),
        c('[Order her out] "You\'re not getting on that wagon. That\'s an order."', "order"),
        c('"Why the Condemned? You could simply leave."', "why")),
    jan("pardon", '''"No. I don't want a pardon. I want people to see me do something, and a pardon's a piece of paper that says they don't have to look." {n}She turns the practice sword over on her knees, and her ears have gone pink.{/n}
"Thank you. No."''',
        c("Continue", "choose")),
    jan("order", '''"You can order me out of a cell. You can't order me into your crusade and have it mean anything." {n}She shrugs one shoulder.{/n}
"I've asked for the posting, and the sergeant's agreed. If you want to stop it, you'll have to do it in front of him."''',
        c("Continue", "choose")),
    jan("why", '''"Because I ran. Because the Condemned go wherever it's worst, and I want to stand somewhere bad and not run, where somebody who doesn't like me can see it."
{n}She looks at the scratched circle, not at you.{/n} "And because Seelah would come down here and tell me I'd done enough, and I'd believe her, because I want to. I haven't. I want it done in front of people who don't like me and have to write it down anyway."''',
        c("Continue", "choose")),
    jan("choose", '''{n}She waits, with the patience of a woman who has already decided and is only being polite.{/n}''',
        c('[Challenge her] "Then fight me for it. If I win, you stay."', "challenge", requires=(HH_SEEN,)),
        c('[Let her go to the wagon] "Then go. Good luck, Jannah."', "let_go"),
        # Q6 follow-up (INT): a Commander who was never at Houndheart challenges her too (the visitors' way, below).
        c('[Challenge her] "Then fight me for it. If I win, you stay."', "challenge", forbids=(HH_SEEN,))),
    jan("challenge", '''"Fight you. In here?" {n}She looks round the cell: the bunk, the bucket, the circle she scratched.{/n}
"With what? They took my blade when I came down here, and a stick against the Commander of the crusade is a joke I'm too tired to tell."
{n}Then something changes in her face, all at once, like a fencer seeing an opening.{/n} "Wait. There's a game."''',
        c("Continue", "rules", requires=(HH_SEEN,)),
        c("Continue", "rules_visitor", forbids=(HH_SEEN,))),
    jan("rules_visitor", '''"My master's salle played it after fencing on wet nights. Blood and tale. Two fencers tell the same bout between them, and the first one caught in a lie has bled first. You weren't at Houndheart, so we can't play it his way."
"There's the visitors' way. When a sword came to the salle from somewhere else, nobody knew her bouts, so one told her own and the other hunted the lie, with one chance to name it. Name none, and the teller wins. It's harder. You've nothing to go on but the teller: her hands, her feet, where she looks when she says it."''',
        c("Continue", "stake_visitor")),
    jan("stake_visitor", '''{n}She lays the practice sword down inside the scratched circle, carefully, as if it were a real one.{/n}
"Same stakes. If I draw first blood, I'm on the wagon at the ninth bell, and you send nobody after it. If you do, I walk out of this cell, and you can say what comes next. I'll tell mine first. I've had the practice. You're a witness to this telling, Commander. Not to the cage."''',
        c('"Agreed. Tell it."', "own_tale"),
        c('[Let her go to the wagon] "No. Go, if you have to."', "let_go")),
    jan("own_tale", '''"Houndheart. Three of us out of Kenabres after a ring: Seelah, Elan and me. Curl begged off with an old wound. A quasit came out of Elan's travelling chest with the ring in its paws, and its colours put Elan and me face-down in the dirt." {n}She tells it fast and flat, like a report, and watches you the whole time.{/n}
"When I came round the others were chasing it all over the camp. I never went near it. I stayed back by the chest with my sword out and let them run. Then Curl was there with the ring, calling things up out of the ground, and Elan swung at him, and Seelah got between them, and I turned and ran."''',
        c("[Perception] Watch her, not the story: her hands, her feet, where her eyes go.",
          check=dict(Skill="SkillPerception", DC=22, Success="own_caught", Failure="own_missed")),
        c('[Let her finish] "No blood. I believe you."', "drawn", flags=(STRANGER,))),
    nar("own_caught", '''{n}It is in her sword hand. When she says she never went near it, the hand on her knee turns over and the wrist rolls forward: the small, exact start of a lunge, the way a fencer's body remembers a pass the mouth is busy denying. Her eyes go to the corner of the cell, twenty paces off across a camp you have never seen.{/n}''',
        c('"Your hand moved when you said you never went near it. You tried to get at it, didn\'t you."', "own_yield")),
    jan("own_yield", '''{n}She looks down at her hand as if it belonged to somebody else, and shuts it.{/n}
"...Alone. While the others were talking. Sword out, creeping up on it like a cat on a pigeon, and the filthy thing blinked away twenty paces with a clap just as I got there." {n}Her mouth twists.{/n} "First blood. To you. Seven years in the circles of Mivon and I never bled first, and I lose my record in a cell to a stranger who read my wrist."
{n}She leaves the practice sword where it lies inside the circle.{/n} "Say it, then. What comes next."''',
        c('"You walk out of this cell. The wagon goes without you; I\'ll square it with your sergeant."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS, STRANGER)),
        c('"You stay in Drezen, where I can watch you not running."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS, STRANGER))),
    nar("own_missed", '''{n}You watch her hands, her feet, her eyes, and they tell you nothing. She has told it so many times, to so many bars, that it has worn smooth.{/n}''',
        c('[Let her finish] "No blood. I believe you."', "drawn", flags=(STRANGER,))),
    jan("rules", '''"My master's salle played it after fencing on wet nights. Blood and tale. Two fencers tell the same bout between them, each her turn, and either can catch the other in a lie. The first one caught has bled first, and yields. Nobody caught, the tale's drawn, and a drawn bout goes to the one who was challenged. He used to say a fencer who lies about a bout will lie with a blade, so you might as well find out over wine."
"We'll tell Houndheart. You were there. Back my telling, and they'll ask you about it. Don't improve it for me."''',
        c("Continue", "stake")),
    jan("stake", '''{n}She lays the practice sword down inside the scratched circle, carefully, as if it were a real one.{/n}
"If I draw first blood, I'm on the wagon at the ninth bell, and you send nobody after it. If you do, I walk out of this cell, and you can say what comes next. That's the forms."''',
        c('"Agreed. I\'ll tell yours first."', "your_tale"),
        c('[Let her go to the wagon] "No. Go, if you have to."', "let_go")),
    nar("your_tale", '''{n}She settles against the wall, cross-legged, and waits the way a judge waits.{/n}
{n}You tell her part of Houndheart: the quasit out of Elan's chest, the colours that put Elan and her face-down in the dirt, the chase across the runes, Curl out of nowhere with the ring and the things he called up out of the ground, Seelah between him and Elan's sword. And then her.{/n}''',
        c('[Tell it true] "You ran. Before it was over, you ran north, and you didn\'t come back for any of us."', "true"),
        c('[Tell it kinder] "You went for help, and got lost in the scrub."', "kind_lie")),
    jan("kind_lie", '''"No." {n}She says it before you've finished.{/n}
"That's a kind lie, and it's the worst sort. First blood to me."''',
        c("Continue", "won")),
    jan("true", '''{n}She nods once, as if you had touched her on the guard and not the body. No blood.{/n}
"My turn. Your part." {n}She tells it fast and flat, like a report.{/n} "You were in it from the chest to the end. When Curl's things came up out of the ground you didn't go anywhere. I remember thinking you looked like somebody painted on a temple wall, and hating you a little for it."''',
        c("Continue", "her_tale")),
    jan("her_tale", '''"Me? I never went near that quasit. I lay in the dirt where its colours dropped me and let the rest of you chase it. Then Curl's things came, and you turned to meet them, and I turned and ran."
{n}She stops, and waits for you to find the lie, if there is one.{/n}''',
        c("[Perception] Go back over the camp, stroke by stroke, and look for the lie in her telling.",
          check=dict(Skill="SkillPerception", DC=20, Success="caught", Failure="missed")),
        c('[Let her finish] "No blood. It\'s true."', "drawn")),
    nar("caught", '''{n}You go back over the camp, stroke by stroke: the chest, the colours, the chase across the runes. And while you do, you watch her. When she says she never went near it, the hand on her knee turns over, the way a fencer's hand does when it remembers a pass.{/n}''',
        c('"You never went near it? You crept up on that quasit alone, sword out, while the rest of us were talking, and it blinked away with a clap. You ran later. You\'ve been telling it worse than it was."', "yield", requires=(QUASIT_SEEN,)),
        c('"You never went near it? Your hand just moved when you said that. You went after it, didn\'t you. You\'ve been telling it worse than it was."', "yield", forbids=(QUASIT_SEEN,))),
    jan("yield", '''{n}She opens her mouth to say no, and nothing comes out. You watch her go back through it herself: the quasit, the clap, her own feet.{/n}
"...First blood." {n}She says it very quietly.{/n} "To you. Seven years in the circles of Mivon and I never bled first, and I lose my record in a cell, to a story, on a lie I told against myself."
{n}She leaves the practice sword where it lies inside the circle.{/n} "Say it, then. What comes next."''',
        c('"You walk out of this cell. The wagon goes without you; I\'ll square it with your sergeant."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS)),
        c('"You stay in Drezen, where I can watch you not running."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS))),
    jan("stay", '''"The wagon goes without me." {n}She gets off the bunk and stands, and doesn't seem to know what to do with her hands.{/n}
"All right. By the forms. Don't expect me to be grateful. The forms don't say anything about grateful."''',
        c("[Leave her the cell for the night.]")),
    nar("missed", '''{n}You go back over it and find nothing. The chest, the chase, Curl's things: it all sits where she put it. If there is a lie in her telling, it is buried deeper than your memory reaches.{/n}''',
        c('[Bluff] {n}Name a lie anyway:{/n} "Elan\'s chest was on your left, not your right. You weren\'t where you say you were."',
          check=dict(Skill="CheckBluff", DC=26, Success="false_blood", Failure="false_caught")),
        c('[Let her finish] "No blood. It\'s true."', "drawn")),
    jan("false_blood", '''{n}She frowns. You watch her go back over the camp, looking for the chest, and not be sure.{/n}
"...Maybe. Maybe it was on the left. I've told it to myself so many ways I can't find the edges any more." {n}Her mouth twists.{/n}
"Then that's first blood. To you. My record, gone in a cell, over a travelling chest."''',
        c('"You walk out of this cell. The wagon goes without you."', "stay_false", flags=(LIED, SECRET, RETURNED, STARTED, FIRST_LOSS))),
    jan("stay_false", '''"The wagon goes without me." {n}She sits there a while longer, frowning at the circle as if it had cheated her and she can't work out how.{/n}
"By the forms, then. I'll stay. And I'll think about that chest."''',
        c("[Leave her the cell for the night.]")),
    jan("false_caught", '''{n}Her eyes come up off the floor and fix on you, and for a heartbeat she looks exactly like what she is: a duellist who has seen a feint.{/n}
"No. The chest was on my right. The quasit came out of it in my face." {n}She almost smiles.{/n} "That's a lie, Commander. First blood to me."''',
        c("Continue", "won")),
    jan("drawn", '''"No blood?" {n}She looks at you with something close to pity.{/n}
"Then the tale's drawn, and a drawn bout goes to the one who was challenged. That's me."''',
        c("Continue", "won")),
    jan("won", '''"So. The wagon." {n}She picks the practice sword up out of the circle and lays it across her knees again.{/n}
"You fought fair enough. You just lost. It happens. It happened to me at Houndheart, only there I didn't stay to lose properly."''',
        c("[Let the forms stand.]", flags=(POSTED,))),
    jan("let_go", '''{n}She nods, the small nod of a fencer acknowledging a touch she saw coming.{/n}
"Thank you. I mean it." {n}She leans her head back against the wall.{/n} "Go on, Commander. Somebody up there needs you more than a deserter in a cell does."''',
        c("[Leave her to the wagon.]", flags=(CLOSED, GONE))),
], requires=(IN_CELLS,), forbids=(DEAD, DEAD_KNOWN, RETURNED, POSTED), delay=12, hub=CELLS_PRESENCE,
    TricksterDevice=True, TricksterState="alive")


# Q6 follow-up (INT/COX): she is met in her cell again once she is back (a presence 36 hours after the wagon left), not at a rest.
meet(P + "alive.wagon", "The ninth bell, and after", '"You came back."', [
    nar("open", '''{n}The gate sergeant sent up word that a soldier from the north-road company had come back and gone straight down to the old gaol.{/n}
{n}She is grey with road dust, her gambeson slit along one sleeve and sewn shut again with a Condemned surgeon's black thread. She gets up off the bunk when you come in.{/n}''',
        c("Continue", "old_scar", requires=(JOINED,)),
        c("Continue", "old_scar", requires=(REFUSED,), forbids=(JOINED,)),
        c("Continue", "new_scar", forbids=(JOINED, REFUSED))),
    nar("old_scar", '''{n}The old scar on her right temple has a new one across it now, still angry, badly knitted. She stands in the middle of the cell and waits to be looked at.{/n}''',
        c("Continue", "ford")),
    nar("new_scar", '''{n}There is a cut on her right temple from the brow to above the ear, still angry and badly knitted. She stands in the middle of the cell and waits to be looked at.{/n}''',
        c("Continue", "ford")),
    jan("ford", '''"Half the wagon came back. They put us on a ford a morning's march up the north road, and in the night things with too many legs came over the water, and we held it till the relief came at noon. The wounded crawled back across behind us. Nobody in my file ran. I didn't either." {n}She touches the stitches at her temple, briefly, like a fencer touching the button on a foil.{/n}
"I'd like that written down too."''',
        c("Continue", "said")),
    jan("said", '''"I won in your cell. You yielded. By the old man's rule the winner says the end of the matter, and I didn't say it before the wagon left, because I didn't know it yet."
"I do now. I'm staying. Not because you won; you didn't. Because I did, and it's mine to say. The sergeant will sign me over to Drezen if you countersign it."''',
        c('"Then stay."', "stay", flags=(RETURNED, STARTED, STORY_LOST, POSTING)),
        c('"Good. I was about to send somebody after the wagon."', "cheat", flags=(RETURNED, STARTED, STORY_LOST, POSTING)),
        c('[Refuse her] "You won. You went. That was the end of it."', "refused", flags=(CLOSED, GONE))),
    jan("stay", '''"Good." {n}She sits back down on the bunk and puts her boots on the blanket, as if she has been sitting there for years.{/n}
"I'll keep the old cell. Nobody else wants it, and I've got used to the way the turnkey snores."''',
        c("[Let her have the cell.]")),
    jan("cheat", '''"Then you'd have lost twice, and cheated once, and I'd have had to challenge you properly." {n}The corner of her mouth goes up.{/n}
"I'll keep the old cell. Nobody else wants it."''',
        c("[Let her have the cell.]")),
    jan("refused", '''{n}She takes it standing, the way she took the wagon: heels together, chin up.{/n}
"All right. That's a fair reading of the forms. Not the only one." {n}She salutes you, flat of the blade to the brow, picks up her pack, and walks out past you and up the gaol steps, not running.{/n}''',
        c("[Let her go.]")),
], requires=(POSTED,), forbids=(RETURNED,), delay=36, hub=BACK_PRESENCE, TricksterDevice=True, TricksterState="alive")   # Q6 r3 (COX): 36 h keeps the lost-story chain inside 168 h


# --- The commit: her public rematch at the muster (the bout decides only her record); then she chooses. -----------------------------------------------

meet(P + "challenge", "The rematch", '"You look like someone about to do something in public."', [
    nar("open", '''{n}She is on the bunk with her sword across her knees, rolling a stick of fencer's chalk between her fingers. The blade has been cleaned and oiled and the grip rewound in new leather. Her hair is freshly dressed and pinned back hard, the way you'd pin it for a bout.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Muster's at the fourth bell. The whole yard: your sergeants, the Eagle Watch, the smith's boys on the smithy roof, anyone with a reason to be late for drill." {n}She tosses the chalk and catches it.{/n}
"I'm going to challenge you. There, in front of all of them. By the old man's forms, out in the open, where everybody can see who asked and who answered."''',
        c("Continue", "lie", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "why", forbids=(LIED,)),
        c("Continue", "why", requires=(LIED, CONFESSED))),
    jan("lie", '''"One thing first, before I chalk a circle with you in it." {n}She stops rolling the chalk.{/n}
"In my cell you caught me in a lie about Elan's chest at Houndheart. I've gone over it every night since. The chest was on my right. The quasit came out of it in my face. You caught me in a lie I never told, and I gave you my record for it."
"I'm not asking you anything. I'm telling you I know. You can say so now, or you can say nothing, and I'll still walk out to that muster."''',
        c('[Confess] "Yes. I lied. I missed the real one, and I wanted you out of that cell more than I wanted to win clean."',
          "confessed", flags=(CONFESSED, SECRET_KNOWN)),
        c('"The chest was on your left."', "held", flags=(HELD_LIE, SECRET_KNOWN))),
    jan("confessed", '''"There." {n}She lets out a breath she seems to have been holding since the cell.{/n}
"That's what it looks like when somebody's caught in a lie and says so. My master called it the only honest yield there is. I'll take it." {n}She points the chalk at you.{/n} "The real one was mine, by the way. I found it. I'm not telling you where."''',
        c("Continue", "why")),
    jan("held", '''{n}She looks at you exactly as long as it takes a fencer to decide a feint isn't worth answering.{/n}
"All right. I'll still fight you. The forms don't care what you are. They only care what you do inside the chalk."''',
        c("Continue", "why")),
    jan("why", '''"You want to know why." {n}She doesn't wait for you to say it.{/n}''',
        c("Continue", "why_cage", requires=(SCAR,)),
        c("Continue", "why_cell", requires=(FIRST_LOSS,), forbids=(SCAR,)),
        c("Continue", "why_won", forbids=(FIRST_LOSS,))),
    jan("why_cage", '''"Because you beat me in a cage and quit the circle, and I've been owed a rematch ever since. In the old man's salle the loser could always ask for one, and a victor worth anything granted it. You never gave me the chance to ask. So I'm asking where you can't pretend you didn't hear."
"And because everybody who saw the Scar thinks they watched an execution. Nobody in Drezen has seen Jannah Aldori claim a proper rematch. They've only heard about her running, and then about her dying."''',
        c("Continue", "stake")),
    jan("why_cell", '''"Because you beat me in a cell with a story, and a story isn't steel. In the old man's salle the loser could always ask for a rematch, and a victor worth anything granted it. I'm asking where you can't pretend you didn't hear."
"And because nobody in Drezen has seen Jannah Aldori claim a proper rematch. They've only heard about her running."''',
        c("Continue", "stake")),
    jan("why_won", '''"Because I beat you in a cell with a story, and the only one who saw it was a turnkey. A story isn't steel. I want the rematch you'd have asked for if you'd been raised in Mivon, and I want it where everybody can see."
"Nobody in Drezen has seen Jannah Aldori claim a proper rematch. They've only heard about her running."''',
        c("Continue", "stake_won")),
    jan("stake", '''{n}She puts the chalk in your hand and closes your fingers over it.{/n}
"My stake, and I'm setting it, not the old man. If I draw first blood, the old loss is answered, and my record is mine again to keep. If you do, it stands, and I carry it, and I cut a second notch the wrong way."
"That's the stake. Don't get ideas about the rest."''',
        c('"Fourth bell. I\'ll be there."', "yard"),
        c('[Flirt] "And the rest of it? When do you decide that?"', "rather"),
        c('"Not in front of the muster. Ask me somewhere else."', "not_there")),
    jan("stake_won", '''{n}She puts the chalk in your hand and closes your fingers over it.{/n}
"My stake, and I'm setting it. If I draw first blood, I've beaten you twice, and everybody saw the second time. If you do, we're square, and I'll say so to anyone who asks."
"That's the stake. Don't get ideas about the rest."''',
        c('"Fourth bell. I\'ll be there."', "yard"),
        c('[Flirt] "And the rest of it? When do you decide that?"', "rather"),
        c('"Not in front of the muster. Ask me somewhere else."', "not_there")),
    jan("rather", '''"When I've got my breath back." {n}She takes the chalk out of your hand again.{/n}
"And don't you dare make it easy for me. If you throw a bout of mine in front of four hundred soldiers, Commander, I'll never forgive you, and I'll know. I always know."''',
        c("Continue", "yard")),
    jan("not_there", '''"No. Somewhere else is where I ran." {n}She takes the chalk back.{/n}
"It's the muster or nothing. Come and find me when you've got the nerve for it. I'll be here. Obviously."''',
        c("[Leave her with the chalk.]", abort=True)),
    nar("yard", '''{n}The yard at the fourth bell is full the way only a yard with a rumour in it gets full. Sergeants who should be drilling. The Eagle Watch in their blue, who know exactly which recruit ran at the Houndheart camp. The smith's boys on the smithy roof with their legs dangling.{/n}
{n}Jannah walks into the middle of it and draws a circle on the sand, three paces across, in one stroke, without looking down. The yard goes quiet.{/n}''',
        c("Continue", "challenge")),
    jan("challenge", '''{n}She steps into the circle and draws. The long blade comes up to her brow in the salute, and she says it loud enough for the gate guards to hear:{/n}
"Jannah Aldori, of Mivon, once a recruit of the Eagle Watch, who ran at the Houndheart camp. I claim my rematch from the Commander of the crusade. To the first blood."
{n}On the smithy roof somebody drops a hammer. Nobody laughs.{/n}''',
        c("[Step into the circle and salute.]", "bout")),
    nar("bout", '''{n}She comes at you the way she must have come at everyone in Mivon for seven years: on the balls of her feet, the blade low and quick and never where you are looking. She isn't trying to hit you. She's trying to take the sword out of your hand, the Aldori way, and twice she very nearly does.{/n}''',
        c("[Mobility] Stay out of her measure and wait for her to overreach.",
          check=dict(Skill="SkillMobility", DC=28, Success="you_first", Failure="her_first")),
        c("[Athletics] Bind her blade and drive through it.",
          check=dict(Skill="SkillAthletics", DC=28, Success="you_first", Failure="her_first")),
        c("[Leave a line open and let her take it.]", "no_gift")),
    jan("no_gift", '''{n}She sees the opening, and doesn't take it. She steps back out of measure and lowers her blade, and the whole yard hears her:{/n}
"Don't you dare. Fight me, or get out of my circle."''',
        c("[Take your guard again.]", "bout_again")),
    nar("bout_again", '''{n}She comes in again, faster and angrier, and now she is trying to hit you.{/n}''',
        c("[Mobility] Stay out of her measure and wait for her to overreach.",
          check=dict(Skill="SkillMobility", DC=28, Success="you_first", Failure="her_first")),
        c("[Athletics] Bind her blade and drive through it.",
          check=dict(Skill="SkillAthletics", DC=28, Success="you_first", Failure="her_first")),
        c("[Open the line again.]", "thrown", flags=(THREW, DECLINED))),
    nar("thrown", '''{n}She sees the second open line, and this time she doesn't step back. She stops. She lowers her blade until its point rests on the sand.{/n}
{n}Four hundred soldiers watch Jannah Aldori stand in her own circle and refuse an opening a child could have taken.{/n}''',
        c("Continue", "thrown_her")),
    jan("thrown_her", '''"You'd hand it to me." {n}Her voice is quite even, and it carries.{/n}
"In front of all of them. As if I were a girl at a fair who has to be let win." {n}She salutes you, flat of the blade to the brow, and sheathes, and steps out of the chalk.{/n}
"The bout's void. Nobody bled. Nothing's answered." {n}She walks out of the yard without looking back, and the muster parts to let her through.{/n}''',
        c("[Let her go.]")),
    nar("you_first", '''{n}She overreaches by a hand's breadth. It's enough. Your point takes her high on the sword arm, through the gambeson, and a line of red opens on the sleeve. First blood.{/n}
{n}She lays her blade down on the sand, lies back inside the chalk, and fixes her eyes on the sky. By her master's rule the victor may say something over her before leaving the circle. The whole yard waits to hear what.{/n}''',
        c('"It stands. You fought like an Aldori."', "you_honour", flags=(YOU_FIRST, FIRST_LOSS)),
        c('"Nothing I could say over you is worth more than how you fought."', "you_honour", flags=(YOU_FIRST, FIRST_LOSS)),
        c('[Mock her before the muster] "Four hundred witnesses, and you still lost. Run along, deserter."', "shamed",
          flags=(YOU_FIRST, FIRST_LOSS, SHAMED, DECLINED), alignment=("Evil", 1))),
    jan("you_honour", '''{n}Flat on the sand, eyes on the sky, Jannah Aldori laughs: the old laugh from the tavern in Kenabres, much too loud for a yard full of soldiers.{/n}
"It stands, then." {n}She doesn't move a finger.{/n} "Quit the circle, Commander. I'm not allowed to get up until you do, and my arm hurts."''',
        c("[Quit the circle.]", "you_up")),
    jan("you_up", '''{n}You step over the chalk. She gets up, sheathes, and stands in the circle bleeding through her sleeve while the yard stares at her.{/n}
"The wrong way, and in front of everybody," {n}she says, to you, not to them.{/n} "Good. Nobody can say it was an accident."''',
        c("Continue", "after")),
    jan("shamed", '''{n}The yard goes very still. Jannah gets up, which she has never once done before the victor left the circle, and she does it slowly, deliberately, so that every one of them sees her break the forms rather than lie there under that.{/n}
"The bout was fair," {n}she says, to the yard.{/n} "What the Commander said after it wasn't. Write that down, anybody here who writes things down." {n}She walks out without sheathing.{/n}''',
        c("[Watch her go.]")),
    nar("her_first", '''{n}You never see it coming. A turn of her wrist, a flicker of steel inside your guard, and a sting along your jaw; when you touch it your fingers come away red. First blood.{/n}
{n}Jannah stands inside the chalk with her blade lowered, breathing hard, and waits to see what the Commander of the crusade does with the forms in front of the whole muster.{/n}''',
        c("[Lay down your weapon, lie back inside the circle, and keep your eyes on the sky.]", "her_yield",
          flags=(SHE_FIRST, PUBLIC_YIELD), crusade=("Favors", -100)),
        c("[Wipe the blood off your jaw and walk out of the circle.]", "walked_off", flags=(SHE_FIRST, REFUSED_YIELD, DECLINED))),
    jan("her_yield", '''{n}Four hundred soldiers watch their Commander lie down on {mf|his|her} back in the sand inside a deserter's chalk circle, eyes open, not moving. It is so quiet you can hear the smith's forge breathing.{/n}
"Answered," {n}Jannah says, to you. Then, louder, to the whole yard:{/n} "First blood! Does anybody here want to argue with me about it?"
{n}Some of them do. You can see it in the Mendevian knights by the barracks door: a Commander who lies down in the sand for a deserter is a Commander who can be made to lie down. By evening the officers will be writing home to Nerosyan about it, and the knights' donations will be slower to come.{/n}
{n}Nobody on the smithy roof wants to. She steps out of the chalk, as the old man's rule would have it, so that you're allowed to move. Then she steps straight back in and pulls you up by both hands.{/n}''',
        c("Continue", "after")),
    jan("walked_off", '''{n}The yard watches you walk out of the chalk with blood on your jaw, as if her rules were a game she had made up to pass the time in a cell.{/n}
{n}Jannah doesn't follow. She stands in the middle of the circle with her blade lowered and says, quite clearly, so that everyone hears it: "Then it wasn't a bout. It was a brawl, and I don't give anything to brawlers."{/n}''',
        c("[Keep walking.]")),
    jan("after", '''{n}Later, when the muster has been dismissed three times and still hasn't gone anywhere, she walks you round behind the barracks to the practice yard. There's nobody in it: sand, a trough, a rack of blunted blades.{/n}
"That was the bout." {n}She stops at the edge of the sand and turns to face you. Her ears have gone pink at the points, and she is scowling about it.{/n}
"And this is me wanting you. I've wanted you since the cell. I'm sick of fencing round it."''',
        c("Continue", "yes", forbids=(HELD_LIE,)),
        c("Continue", "no_lie", requires=(HELD_LIE,))),
    jan("yes", '''{n}She takes your face in both hands, in the open yard, where anybody coming round the barracks could see, and kisses you: not quick, not careful, and not in any of the forms.{/n}
"Tonight. Here. Bring your sword, and leave your rank in the barracks." {n}Her ears have gone pink at the points.{/n} "I'll bring the chalk."''',
        c('"I\'ll be here."', flags=(COMMITTED,)),
        c("[Kiss her back, and let the barracks look.]", flags=(COMMITTED,)),
        c('[Refuse her] "No. It was a bout. That\'s all it was."', "refuse", flags=(CLOSED, GONE))),
    jan("refuse", '''{n}She takes her hands back as if from a hot blade.{/n}
"A bout. Yes. I heard you." {n}She tries to settle her mouth into a smile and gives it up. Her salute is quick; she leaves before you can return it.{/n}''',
        c("[Let her go.]")),
    jan("no_lie", '''"And I've decided no." {n}She says it quietly, without heat.{/n}
"You caught me in a lie I never told, and you let me give you my record for it, and when I asked you for the truth you looked me in the eye and moved the chest again." {n}She steps back out of measure.{/n}
"I fought you anyway, because the forms don't care what you are. I do."''',
        c("[Let her go.]", flags=(DECLINED,))),
], requires=(WALLS,), forbids=(COMMITTED, DECLINED), delay=24)


# The intimacy: the chalked duelling circle in the practice yard at night, the swords on the sand.
# Q6 follow-up (INT): her appointment is kept from her cell hub (the yard, that night), not from the mod's book.
meet(P + "circle_night", "Inside the chalk", '[Go to the practice yard tonight, with your sword.]', [
    nar("open", '''{n}At night the practice yard behind the barracks is sand, a water trough, a rack of blunted blades and a sky stained by the Worldwound's wrong-coloured light. The circle is already chalked when you come in. Three paces across, one stroke.{/n}
{n}Jannah is standing in the middle of it in her shirt and breeches, barefoot on the cold sand, with her sword drawn and its point resting between her feet.{/n}''',
        c("Continue", "salute_or")),
    jan("salute_or", '''"Salute, or leave the circle." {n}It is not entirely a joke.{/n}''',
        c("[Draw, and salute her.]", "saluted"),
        c("[Lay your sword on the sand at her feet.]", "laid")),
    nar("saluted", '''{n}She returns it, flat of the blade to the brow, and then lays her sword on the sand. After a moment you lay yours across it, and the two blades lie there crossed, catching the red light.{/n}''',
        c("Continue", "close")),
    jan("laid", '''"No salute?" {n}She looks at your blade lying at her feet, and something in her face gives way.{/n}
"That's a salute too. The old man gave it once, to a student who'd beaten him. You just don't know it." {n}She lays her own sword across yours.{/n}''',
        c("Continue", "close")),
    jan("close", '''{n}She steps in, inside measure, where the old man taught her never to stand unless she meant to finish something.{/n}
"In Mivon I never let anyone this close. You don't, if you want to stay unbeaten." {n}Her breath is quick and she isn't hiding it.{/n}''',
        c("Continue", "mark_jaw", requires=(SHE_FIRST,), forbids=(COMMITTED,)),      # retired by gating (Q6; index kept)
        c("Continue", "mark_arm", requires=(YOU_FIRST,), forbids=(COMMITTED,)),      # retired (Q6)
        c("Continue", "mark_late", forbids=(SHE_FIRST, YOU_FIRST, COMMITTED)),       # retired (Q6)
        c("Continue", "record_lost", requires=(FIRST_LOSS,)),
        c("Continue", "record_kept", forbids=(FIRST_LOSS,))),
    jan("record_lost", '''"I'm not unbeaten any more. I find I don't mind."''',
        c("Continue", "mark_jaw", requires=(SHE_FIRST,)),
        c("Continue", "mark_arm", requires=(YOU_FIRST,)),
        c("Continue", "mark_late", forbids=(SHE_FIRST, YOU_FIRST))),
    jan("record_kept", '''"I still am. Nobody's had my blood first, not the Scar, not you." {n}She takes one more step, so there is no measure left at all.{/n} "I'm letting you in anyway. Don't make me regret it."''',
        c("Continue", "mark_jaw", requires=(SHE_FIRST,)),
        c("Continue", "mark_arm", requires=(YOU_FIRST,)),
        c("Continue", "mark_late", forbids=(SHE_FIRST, YOU_FIRST))),
    nar("mark_jaw", '''{n}Her thumb finds the cut she gave you at the muster, along the line of your jaw, and follows it all the way, slowly, the way you'd follow the edge of a blade you were proud of.{/n}
"I did that," {n}she says against your mouth, as if she still can't quite believe it.{/n} "In front of everyone."''',
        c("Continue", "kiss")),
    nar("mark_arm", '''{n}She takes your hand and puts it on her sword arm, on the bandage over the cut you gave her at the muster, and holds it there, clear of the wound. Her eyes stay on your mouth.{/n}
"You did that. In front of everyone. Nobody ever did that in front of everyone." {n}Her voice has gone low.{/n} "Do it again. Not with the sword."''',
        c("Continue", "kiss")),
    nar("mark_late", '''{n}She takes your hand and lays it flat over her heart, where it is beating hard enough to feel through the shirt, and holds it there.{/n}
"The last time you stood in a circle of mine, it went wrong. This time you walked in knowing what you were doing. So did I." {n}Her voice has gone low.{/n}''',
        c("Continue", "kiss")),
    nar("kiss", '''{n}She kisses you hard and without finesse, then again, slower, testing the angle until she gets the kiss she wants. Her palms are rough and they find your buckles without looking. Your belt goes. Your coat goes, onto the sand outside the chalk, because she won't have anything in the circle that doesn't belong there.{/n}
{n}You pull her shirt over her head. The Worldwound's light lies red along her ribs. She has a fencer's marks, old nicks on her forearms from practice blades, and newer ones the Wound gave her, and she guides your mouth to the new ones first.{/n}''',
        c("Continue", "learn")),
    jan("learn", '''{n}She is not patient and she is not shy.{/n} "Take that off. All of it. I want to look at you." {n}When she has looked, her breath goes ragged and she doesn't try to steady it.{/n}
{n}She walks you backwards across the circle a step at a time until your heels are at the chalk, and holds you there on its edge with her mouth at your throat and her hands learning you the way she'd learn a new blade: the weight, the balance, the places it wants to move.{/n}
"Seven years I only wanted to win," {n}she says against your skin.{/n} "Tonight I want this more."''',
        c("Continue", "down")),
    jan("down", '''"This is where I'd take your sword," {n}she says, breathing hard, her forehead against yours,{/n} "if you'd brought it into measure." {n}She works at your belt with one hand and doesn't let go of you with the other.{/n}
"You did. So I will."''',
        c("[Let her.]", "cut"),
        c("[Take hers first.]", "cut")),
    nar("cut", '''{n}She hooks your heel with hers, the oldest trick in any salle, and takes you down onto the cold sand inside the chalk. The circle smears under your shoulder. Neither of you cares about the forms after that.{/n}''',
        c("[Go down with her.]")),
], requires=(COMMITTED,), forbids=(NIGHT,), delay=0)   # hub: her cell presence


meet(MORNING, "A scuffed circle", '"You\'ve got sand in your hair."', [
    nar("open", '''{n}She is back in the last cell, rewinding her sword's grip with a strip of new leather and humming something from Mivon under her breath. She stops humming the moment she sees you. There is sand in her hair and she knows it.{/n}''',
        c("Continue", "talk_yielded", requires=(PUBLIC_YIELD,)),
        c("Continue", "talk_won", requires=(YOU_FIRST,)),
        c("Continue", "talk_late", forbids=(PUBLIC_YIELD, YOU_FIRST))),
    jan("talk_yielded", '''"The whole garrison knows. The sergeants are calling it the Commander's Yield. The Eagle Watch have a song about it already. It rhymes 'Aldori' with 'sorry', and it's terrible, and I've heard it four times since breakfast."''',
        c("Continue", "told")),
    jan("talk_won", '''"The whole garrison knows. They're saying the Commander put the deserter on her back in front of the muster." {n}She pulls the leather tight.{/n} "They're not wrong. They're only talking about the wrong time of day."''',
        c("Continue", "told")),
    jan("talk_late", '''"Half the garrison still thinks the muster was the end of it, one way or the other. None of them has any idea what happened in the yard last night, and I intend to keep it that way for at least a week."''',
        c("Continue", "told")),
    jan("told", '''"I've been told three times this morning that you could do better than a deserter. Once by a sergeant, once by a priest, and once by a woman selling pies. I told all three the same thing: the forms don't care what they think."
{n}She tests the grip in her palm.{/n} "Whoever else you've got, Commander, and I've heard things, none of them chalked a circle in front of your muster. I did. You'll remember that."''',
        c('"I\'ll remember."', "houndheart"),
        c('[Flirt] "You hum when you\'re happy."', "hum"),
        c('"Irabeth is going to want a word with me."', "irabeth", forbids=("irabeth_dead",)),
        c('"Irabeth is going to want a word with me."', "irabeth", requires=("irabeth_dead", "irabeth.trickster.returned"))),
    jan("hum", '''"I do not." {n}She does, and she knows it, and the points of her ears go pink.{/n} "It's a drinking song from the river docks. It's about a boatman's wife. You wouldn't like the third verse."''',
        c("Continue", "houndheart")),
    jan("irabeth", '''"Irabeth has already had a word with me. She wanted to know what exactly the Eagle Watch would be vouching for, if anybody asked it." {n}Jannah shrugs, and her ears go pink.{/n}
"I told her: a fencer. She didn't laugh. I think that means she was satisfied."''',
        c("Continue", "houndheart")),
    jan("houndheart", '''{n}She stops working the grip.{/n}
"I didn't think about Houndheart once, last night. Not once. Do you know how long it's been since I went a whole night without it? Since before the cage." {n}She looks at the scratched circle on the cell floor.{/n}
"It'll come back. It always does. But it's got competition now."''',
        c("[Leave her to her grip.]")),
], requires=(NIGHT,), delay=6)


# Her no, answered: a circle left chalked in the yard (no price, no second ask; the truth, said inside it).
# Q6 follow-up (INT): reached from her cell hub (a word about the yard), not from the mod's book.
meet(P + "chalk_circle", "A circle in the yard", '"Somebody has chalked a circle in the practice yard."', [
    nar("open", '''{n}She doesn't look up from the bunk. "Has somebody," she says, and turns over to face the wall.{/n}
{n}That night, the practice yard behind the barracks has a circle on its sand, three paces across, in one stroke. Her sword lies across the middle. She sits on the yard wall with her knees drawn up, watching. She doesn't call down.{/n}''',
        c('[Step into the circle] "I lied to you in your cell. I named a lie you never told, because I missed the one you did, and I wanted you out of that cell more than I wanted to win clean."',
          "walked_in", requires=(HELD_LIE,), flags=(CONFESSED, COMMITTED, LATE_YES)),
        c("[Step into the circle, draw, and salute her properly.]", "saluted_in", requires=(THREW,), forbids=(HELD_LIE,),
          flags=(COMMITTED, LATE_YES)),
        c('[Step into the circle] "What I said over you at the muster was a lie, and a cheap one. You fought like an Aldori. I\'ll say so at the next muster, to the same four hundred."',
          "unsaid_in", requires=(SHAMED,), forbids=(HELD_LIE,), flags=(COMMITTED, LATE_YES)),
        c("[Step into the circle, lay down your weapon, and lie back on the sand with your eyes on the sky.]", "yield_in",
          requires=(REFUSED_YIELD,), forbids=(HELD_LIE,), flags=(COMMITTED, LATE_YES, LATE_YIELD)),
        c("[Leave the circle as it is.]", "left", flags=(CLOSED, GONE))),
    jan("walked_in", '''{n}She comes down off the wall and walks into the chalk, and stops inside measure.{/n}
"That's all I wanted. Not sorry. Just the truth, said out loud, inside the circle, where it counts." {n}She picks up her sword and lays it across your feet.{/n}
"I decided the rest a while ago. I was only waiting for you to be somebody I could say it to."''',
        c("[Let her say it.]")),
    jan("saluted_in", '''{n}She comes down off the wall, picks her sword up out of the chalk and returns the salute, flat of the blade to the brow, and holds it.{/n}
"That's all I wanted. Not an apology. A salute that means it." {n}She lowers the blade.{/n} "We're not going to fight. Not tonight. I've already decided what tonight is."''',
        c("[Let her decide.]")),
    jan("unsaid_in", '''{n}She comes down off the wall and stands at the edge of the chalk, not in it, until the silence starts to hurt.{/n}
"You'd say that at the muster. Out loud. To the same four hundred." {n}She steps into the chalk.{/n}
"Then you'll say it, and I'll stand there and hear it. And tonight doesn't have to wait for that. I decided about tonight a long time ago."''',
        c("[Let her decide.]")),
    jan("yield_in", '''{n}She comes down off the wall and walks slowly round the circle, once, the way a victor does. You don't move. Your eyes stay on the Wound-light.{/n}
"Nobody's watching," {n}she says.{/n} "It doesn't count the same without the muster." {n}She kneels at the edge of the chalk.{/n}
"It counts enough. Quit lying there, Commander. I've decided, and I'd like you on your feet for it."''',
        c("[Get up.]")),
    nar("left", '''{n}You leave it. In the morning the circle has been scuffed out and the sword is gone, and so is she. The gate sergeant saw a half-elf walk out on the south road at first light, alone.{/n}
{n}Not running, he says. He's quite sure. He watched her until she was out of sight.{/n}''',
        c("[Let her go.]")),
], requires=(DECLINED,), forbids=(COMMITTED,), delay=72)


# --- Epilogue pages (Owner JannahEpilogue; appended in authored order; no effects). --------------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}She kept the scar on her temple where it could be seen, and let the Commander trace it exactly once a year, on the anniversary of the Molten Scar, and never on any other day.{/n}", requires=(SCAR,)),
    p("{n}The Eagle Watch never did correct its roll of the dead. Jannah Aldori, recruit, is listed there still, killed in the Molten Scar. She went to look at it sometimes, when she was in a bad mood, and came away cheerful.{/n}", requires=(SCAR,), forbids=(NAMELESS,)),
    p("{n}She fought the rest of the war under no name, as she had been told to, and after the war the Commander offered to give her own back. She said she would think about it. She was still thinking about it years later, and making the Commander ask.{/n}", requires=(NAMELESS,)),
    p("{n}She liked to tell people that the Commander had released her from a yield once, which in her old salle was the highest honour one fencer could pay another, and that she had stayed anyway, which her old master would have called being a fool.{/n}", requires=(RELEASED,)),
    p("{n}Of the Condemned company she rode north with, half came home. She kept their names on a strip of leather wound under her sword's grip, and rewound it every spring.{/n}", requires=(POSTING,)),
    p("{n}She never let the Commander forget that she had won blood and tale in a gaol cell. When they argued, she would say, \"Drawn bouts go to the one who was challenged,\" and the argument would be over, whether or not anybody had been challenged.{/n}", requires=(STORY_LOST,)),
    p("{n}Every year at the muster she challenged the Commander again, in front of whoever was watching, for no stake at all but the pleasure of it. The Commander fought every one of them in earnest, because she would have known otherwise and never forgiven it, and lost most of them, and won a few, and she kept the tally of both on the inside of her scabbard.{/n}", requires=(PUBLIC_YIELD,)),
    p("{n}Every year at the muster she challenged the Commander again, in front of whoever was watching, for no stake at all but the pleasure of it, and lost more often than she won, and demanded another pass whenever she lost. Afterwards she went home with the Commander, still arguing about the last touch.{/n}", requires=(YOU_FIRST,), forbids=(PUBLIC_YIELD,)),
    p("{n}The Commander said it at the next muster, out loud, to the same four hundred: that Jannah Aldori had fought like an Aldori, and that what had been said over her was a lie. She stood in the front rank and heard it with her chin up. Afterwards she said it was the second-best thing anyone had ever said to her in public.{/n}", requires=(SHAMED, LATE_YES, PUBLIC_REPAIR)),
    p("{n}She wrote her father the truth about Houndheart. He wrote back that fate had brought her to Mendev, and she wrote back that fate had nothing to do with it. They kept up that argument by letter for the rest of his life, and neither of them ever gave an inch.{/n}", requires=(MIVON_TRUTH,)),
    p("{n}Her father in Mivon had the Watch's notice and her bright letter both, and he chose to repeat the bright one to everyone on his street for the rest of his life. She let him.{/n}", requires=(MIVON_LEGEND,)),
    p("{n}She and Seelah stayed friends, the kind who argue about everything and turn up for each other anyway. Seelah hit her twice, the day Jannah walked across the square to find her, and never mentioned either one again.{/n}", requires=(SEELAH_HERSELF,)),
    p("{n}Seelah learned that Jannah was in the Commander's gaol, and why, from the Commander, not from Jannah. It took the two of them a long time to find their way back to the tavern table, and they did it without any help from the Commander.{/n}", requires=(SEELAH_FOR_HER,)),
    p("{n}She told the Commander once that on the wall, with the vrocks coming, she had heard the salute called and remembered who she was. She never said whose voice it had been. She didn't have to.{/n}", requires=(WALL_SALUTE,)),
    p("{n}She never quite forgave the Commander for standing on the wall and watching to see whether she would run. She did not run. She said that was the only thing about that night that mattered, and that the watching was the Commander's own business, to carry.{/n}", requires=(WALL_WATCHED,)),
    p("{n}She kept the question of the chest at Houndheart to herself for the rest of her life. Once, very late at night, she told the Commander where her own lie had been in that telling. She made the Commander swear never to repeat it, and the Commander never has.{/n}", requires=(CONFESSED,)),
)
SCENES.append(scene(P + "epilogue.first_blood", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Jannah Aldori, of Mivon, stayed at the Commander's side through the Threshold and after it. She kept teaching the Eagle Watch recruits, whether or not she wore their blue herself.{/n}
{n}After the war she chalked a circle in a yard and taught the forms to anyone who would stand in it: soldiers, orphans, a one-armed priest, the children of people who had run. She taught the salute, the measure and the yield. She did not teach anyone to stay unbeaten. She said it was a bad habit.{/n}
{n}Some nights she woke thinking she was back at the camp, and lay still with her eyes open until she wasn't, until the room came back. On mornings after, she sought the Commander out and sat close, her cup against her knee.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.commit", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Jannah Aldori got her rematch. She had the chalk in her pocket on the day of the Threshold, and she was angry about it for a month.{/n}
{n}In the first spring after, she walked into the yard of the Commander's house at the hour when the household was up and about, drew a circle on the gravel in one stroke, and claimed the rematch the war had cheated her of, loud enough for the neighbours.{/n}
{n}They fought in earnest. Afterwards she sheathed her sword and caught the Commander's hand before it could leave hers.{/n}
"That's the record settled. I want you. Still. Come inside with me." {n}She waited for the answer, then went through the door with the Commander, shoulder to shoulder.{/n}''',
        paragraphs=(
            p("{n}She kept the scar on her temple where it could be seen.{/n}", requires=(SCAR,)),
            p("{n}Of the Condemned company she rode north with, she kept the names under her sword's grip.{/n}", requires=(POSTING,)),
        ))],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.declined", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Jannah Aldori stayed in Drezen until the war was over, in the last cell of the old gaol, with its door open. She trained with the Eagle Watch, fought where she was sent and never ran, and never once crossed blades with the Commander again.{/n}
{n}When the crusade broke up she went home to Mivon. People who knew her there said she had come back quieter, and a better fencer than when she left, and that there was one bout in Drezen she would not talk about.{/n}''',
        paragraphs=(
            p("{n}It was the Commander she would not talk about, and the lie the Commander had held to in her cell before the muster. She said a blade could be forgiven anything but that.{/n}", requires=(HELD_LIE,)),
            p("{n}When someone in Mivon asked her once how she had come to lose her only bout in Mendev, she said the bout was void. The Commander had offered her an opening twice, like alms; she had refused it twice. Nobody bled. Nothing was answered.{/n}", requires=(THREW,)),
            p("{n}She never repeated what the Commander had said over her in the sand, before four hundred soldiers. The soldiers repeated it for her, for years.{/n}", requires=(SHAMED,)),
            p("{n}She had drawn first blood on the Commander at the muster, fairly, and the Commander would not lie down in the sand for it. She said a victor who has to beg for her yield has not won anything, and she did not ask twice.{/n}", requires=(REFUSED_YIELD,)),
        ))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), **EP))

SCENES.append(scene(P + "epilogue.gone", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Nobody in Drezen saw Jannah Aldori again. A half-elf fencer from Mivon was said to be teaching the forms in a river town far to the south, in a salle above a dye-works, and to be very hard on students who ran from a bout.{/n}
{n}She was said to be unbeaten, too, though the people who said so had never seen her lose, which is not the same thing.{/n}''')],
    requires=("trickster.ever", GONE), forbids=(COMMITTED,), **EP))


# --- Reactions: Irabeth and King Thaberdine (ledger 05 §3.1 row 24), and Seelah (coordinator, 2026-09-29: a named stake). ------------------

IRABETH_GONE = ("irabeth_dead",)
IRABETH_BACK = {"irabeth_dead": "irabeth.trickster.returned"}
KING = dict(answer_list=KING_C5, speaker="conversant", NativeReturnCue=KING_C5_RETURN, forbids=("fool_king.gone",),
            chapter=5, last=5, Chapters=[5])

SCENES.append(reaction("Irabeth", P + "react.irabeth_rolls", (RETURNED, DEAD_L),
    '''{n}Irabeth has a ledger open in front of her and has not turned a page since you came in.{/n}
"The Eagle Watch struck Jannah Aldori from its rolls in the winter. Dead in the Molten Scar, by your hand. I signed it. Now there's a half-elf in your gaol giving that name and wearing a scar I'd know anywhere, because I've seen your blade work."
"I'll need to know what to write, Commander. 'Came back' isn't a column."''',
    answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=5, last=5, Chapters=[5], entry='"About the deserter in the gaol..."',
    portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Irabeth", P + "react.irabeth_wagon", (RETURNED, CONDEMNED),   # Q6 r5 (CAN): the appeal is the Condemned history (ktc_DeserterJoins/Cue_0013-0014)
    '''{n}Irabeth doesn't look up from her dispatches.{/n}
"The Condemned sergeant came to me this morning, about the half-elf sitting in your gaol on your leave. I spoke for that girl once, when she appealed to the Queen. I thought she'd earned a chance to die usefully."
{n}She sets down the pen.{/n} "Now she's earned a chance to live usefully, apparently. See that she does."''',
    answer_list=IRABETH_HUB, forbids=(*IRABETH_GONE, DEAD_L), chapter=5, last=5, Chapters=[5],
    entry='"About the deserter in the gaol..."', portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Irabeth", P + "react.irabeth_wagon_free", (RETURNED,),
    '''{n}Irabeth doesn't look up from her dispatches.{/n}
"The Condemned sergeant came to me this morning. He'd had a half-elf down for his north wagon, and she's sitting in your gaol now, on your leave."
{n}She sets down the pen.{/n} "She ran from my Watch once. See that she doesn't run from yours."''',
    answer_list=IRABETH_HUB, forbids=(*IRABETH_GONE, DEAD_L, CONDEMNED), chapter=5, last=5, Chapters=[5],
    entry='"About the deserter in the gaol..."', portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Irabeth", P + "react.irabeth_sand", (PUBLIC_YIELD, SHE_FIRST),
    '''"You lay down in the sand in front of my sergeants." {n}Irabeth says it the way she would read out a charge.{/n}
"The whole muster. Flat on your back inside a deserter's chalk, with your eyes on the sky, because she cut your jaw and some rule of her old master's said you had to."
{n}She is quiet a moment.{/n} "I've never seen anything like it. Half of them think less of you for it. The other half would walk into the Worldwound behind you tomorrow. I haven't decided which half I'm in."''',
    answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=5, last=5, Chapters=[5], entry='"You heard about the muster."',
    portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

# Q6 r3 (INT): the voluntary yield (yielding_the_circle) has its own account; nobody cut the Commander for it.
SCENES.append(reaction("Irabeth", P + "react.irabeth_yielded", (PUBLIC_YIELD, C + "yielded_the_circle"),
    '''"You lay down in the sand in front of my sergeants." {n}Irabeth says it the way she would read out a charge.{/n}
"Before a blade was lifted. You'd beaten her in front of all of them, and then you walked into her chalk and lay down anyway, and she lay down next to you, and four hundred soldiers stood there with their mouths open."
{n}She is quiet a moment.{/n} "I asked her what it meant. She said it was her old master's, from his salle and nobody else's, and then she wouldn't say another word. I haven't decided whether that's a good sign."''',
    answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=5, last=5, Chapters=[5], entry='"You heard about the muster."',
    portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))


# Seelah: the friend she failed, who grieved her or lost her, and whose Q3 may have returned her (a named stake, per the
# coordinator's brief update; she speaks on her own companion hub, and only once Jannah has faced her or been told of).
SEELAH_GUARD = dict(forbids=("seelah_dead", "seelah_gone"),
                    ForbidOverrides={"seelah_dead": SEELAH_BACK, "seelah_gone": SEELAH_BACK})
SEELAH_AT = dict(answer_list=SEELAH_HUB, chapter=5, last=5, Chapters=[5], portrait="Seelah", **SEELAH_GUARD)

SCENES.append(reaction("Seelah", P + "react.seelah_known", (RETURNED, DEAD_KNOWN, SEELAH_HERSELF),
    '''{n}Seelah's knuckles are skinned across one hand, and she keeps rubbing them as if it would come off.{/n}
"You told me she was dead. You stood there and told me, and I said it wasn't justice, and you let me say it." {n}Her voice is shaking.{/n}
"She's alive. She let me hit her, and then she told me all of it: the forms, the blood, lying in the ash with her eyes open while you walked away. She says it was her choice as much as yours, and I'm to leave you alone about it."
"I'm trying, Commander. I'm a paladin. I'm meant to be good at forgiving people. Give me a little while to be bad at it first."''',
    entry='"You\'ve seen Jannah."', **SEELAH_AT))

SCENES.append(reaction("Seelah", P + "react.seelah_unknown", (RETURNED, DEAD, SEELAH_HERSELF),
    '''{n}Seelah comes straight at you, stops a pace short, and doesn't seem to know what to do with her hands.{/n}
"Jannah was in the Molten Scar. In a cage. And you... and she..." {n}She takes a breath and starts again.{/n} "She told me all of it. The forms, and the blood, and the ash. I didn't even know she'd been caught. I thought she'd just run, and kept running."
"She's alive, and she's here, and she's got your mark on her face, and she's happier than I've seen her since Kenabres. I don't know whether to thank you or hit you. I hit her. That felt like enough for one day."''',
    entry='"You\'ve seen Jannah."', **dict(SEELAH_AT, forbids=("seelah_dead", "seelah_gone", DEAD_KNOWN))))

SCENES.append(reaction("Seelah", P + "react.seelah_cells", (RETURNED, SEELAH_HERSELF),
    '''"Jannah's in the gaol." {n}Seelah says it like an accusation, and then like good news, both in the same breath.{/n}
"And she won't leave it! She won't take a pardon! And you knew, and you went down and played some sort of game with her over the Houndheart camp, and now she's staying in Drezen." {n}She shakes her head.{/n}
"I'd have gone down there myself if anyone had told me. She came and found me instead. She's different. She stands like somebody who's stopped waiting to be hit."''',
    entry='"You\'ve seen Jannah."', **dict(SEELAH_AT, forbids=("seelah_dead", "seelah_gone", DEAD_L))))

SCENES.append(reaction("Seelah", P + "react.seelah_told", (RETURNED, SEELAH_FOR_HER),
    '''"Jannah. In your gaol. And it's you telling me." {n}Seelah turns her gauntlet over in her hands.{/n}
"I'm glad it was you and not a letter. I'm less glad it wasn't her. She's a coward about exactly one thing, and apparently it's me." {n}A crooked smile.{/n}
"So I'm going to go down to that gaol and stand outside the cell until she runs out of reasons. It's the only trick I've ever had that works on her."''',
    entry='"About Jannah..."', **SEELAH_AT))

SCENES.append(reaction("Seelah", P + "react.seelah_muster", (COMMITTED,),
    '''{n}Seelah is grinning before you've reached her.{/n}
"I was on the barracks steps. I saw the whole thing: the chalk, the salute, all of it. 'Jannah Aldori, who ran at the Houndheart camp.' She said it herself, out loud, in front of everyone!" {n}She laughs.{/n}
"No glory without risk. She used to shout it louder than I did. I never thought I'd hear her mean it."''',
    entry='"You were at the muster."', **SEELAH_AT))

SCENES.append(reaction("Thaberdine", P + "react.king_gaol", (RETURNED, "fool_king.available"),
    '''"Commander! Is it true? There's a woman in the gaol who won't be let out?" {n}The King is appalled.{/n}
"In my kingdom people ask to be let out of them. Usually through me. Usually drunk. I've issued a decree: the half-elf in the last cell is to have the good blanket, on account of she's the only honest prisoner in the realm and it's making the others look bad."''',
    entry='"Your Majesty. Heard any news from the gaol?"', **KING))

SCENES.append(reaction("Thaberdine", P + "react.king_muster", (COMMITTED, "fool_king.available"),
    '''"I saw it! From the roof of the tavern, with a glass! Well. A bottle. Pointed the right way." {n}The King waves his mug at the ceiling.{/n}
"A circle in the sand! Swords! A challenge called out loud in front of the whole garrison! That's how it should be done, Commander. None of this whispering in corridors. I'd knight her, if I remembered how, and if she wouldn't cut me for it."''',
    entry='"You were at the muster, Your Majesty?"', **KING))


# --- Registration helpers ------------------------------------------------------------------------------------------------

household.secret("jannah_false_blood", "The chest at Houndheart",
                 "In the gaol, playing her master's game, I missed the lie she told against herself and named one she "
                 "never told: Elan's chest, left or right. She believed me, and gave me her record for it. She is in Drezen "
                 "on the strength of a travelling chest I moved.", portrait="Jannah", witnesses=("jannah",), risk="high")


def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the relationship's own derived keys, its presence and its portrait fallback. Scenes are added by
    expansion.py; world keys the matrix already verified (jannah.dead, joined, seelah.q3_started...) bind on demand."""
    payload.setdefault("DerivedForbids", {}).update({
        P + "no_false_blood": [LIED], P + "not_declined": [DECLINED],
        P + "not_confessed": [CONFESSED],
        P + "no_cage_killing": [SEELAH_KILLED_AT_CAGE], P + "seelah_not_back": [SEELAH_BACK],
    })
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    seen = payload.setdefault("SeenCues", {})
    if seen.get(HH_SEEN, HH_SEEN_CUES) != HH_SEEN_CUES:
        raise ValueError("Conflicting binding: " + HH_SEEN)
    seen[HH_SEEN] = list(HH_SEEN_CUES)
    if seen.get(SWORD_GIVEN, SWORD_GIVEN_CUES) != SWORD_GIVEN_CUES:
        raise ValueError("Conflicting binding: " + SWORD_GIVEN)
    seen[SWORD_GIVEN] = list(SWORD_GIVEN_CUES)
    if seen.get(QUASIT_SEEN, QUASIT_SEEN_CUES) != QUASIT_SEEN_CUES:
        raise ValueError("Conflicting binding: " + QUASIT_SEEN)
    seen[QUASIT_SEEN] = list(QUASIT_SEEN_CUES)
    answers = payload.setdefault("SelectedAnswers", {})
    if answers.get(SEELAH_KILLED_AT_CAGE, SEELAH_KILLED_ANSWER) != SEELAH_KILLED_ANSWER:
        raise ValueError("Conflicting binding: " + SEELAH_KILLED_AT_CAGE)
    answers[SEELAH_KILLED_AT_CAGE] = SEELAH_KILLED_ANSWER
    # The unit's own BlueprintPortrait (CR4_DeserterJanna m_Portrait) until custom art ships; a custom PNG always wins.
    payload.setdefault("PortraitFallbacks", {}).setdefault("Jannah", "550a859fc62244ceadeb40d79ca4d261")


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'jannah.trickster.alive.stories',
    'jannah.trickster.alive.wagon',
    'jannah.trickster.cage.ash',
    'jannah.trickster.killed.yield',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]


# Round 2 authored continuation: the existing repair owes truth AND the
# specific refused act. Keep original nodes/answer positions; append the yes.
_r2_by = {s["Id"]: s for s in SCENES}
_r2_chalk = _r2_by[P + "chalk_circle"]
_r2_nodes = {n["Id"]: n for n in _r2_chalk["Nodes"]}
_r2_open = _r2_nodes["open"]["Choices"]
_r2_open[0]["Set"] = [CONFESSED, SECRET_KNOWN]
_r2_open[0]["Forbids"] = [CONFESSED]
_r2_open[1]["Set"] = []
_r2_open[1]["Forbids"] = []
_r2_open[1]["Requires"].append(P + "truth_clear")
_r2_open[2]["Set"] = [PUBLIC_REPAIR]
_r2_open[2]["Forbids"] = []
_r2_open[2]["Requires"].append(P + "truth_clear")
_r2_open[3]["Set"] = [LATE_YIELD]
_r2_open[3]["Forbids"] = []
_r2_open[3]["Requires"].append(P + "truth_clear")
_r2_nodes["walked_in"]["Text"] = (
    '{n}She lets out a breath, but stays on the wall.{/n} "The chest stays on the right, then. '
    'Good. Now the yard. We haven\'t finished there."')
_r2_nodes["walked_in"]["Choices"][0].update(Next="repair_due", Text="Continue")
for _r2_id in ("saluted_in", "unsaid_in", "yield_in"):
    _r2_nodes[_r2_id]["Choices"][0]["Next"] = "repair_yes"
# A reload already inside the confession node must still collect its debt.
_r2_nodes["walked_in"]["Choices"][0]["Set"] = [CONFESSED, SECRET_KNOWN]
_r2_open.append(c("[Stand inside the chalk with her.]", "repair_yes",
    requires=(HELD_LIE, CONFESSED), forbids=(THREW, SHAMED, REFUSED_YIELD)))
_r2_chalk["Nodes"].extend([
    jan("repair_due", '"You wanted me out of that cell. I heard you. What happened at the muster is still yours to answer."',
        c("[Draw and give her an earnest salute.]", "saluted_in", requires=(THREW,)),
        c('"The insult was a lie. I\'ll correct it at the next muster, before the same four hundred."',
          "unsaid_in", requires=(SHAMED,), flags=(PUBLIC_REPAIR,)),
        c("[Lay down your blade and hold the yield you owe her.]", "yield_in", requires=(REFUSED_YIELD,), flags=(LATE_YIELD,)),
        c("[Stay inside the chalk.]", "repair_yes", forbids=(THREW, SHAMED, REFUSED_YIELD)),
        c("[Leave the circle.]", "left", flags=(CLOSED, GONE))),
    jan("repair_yes", '{n}She steps close, takes your wrist and draws your hand to her waist.{/n} '
        '"No more bout tonight. I want you here. With me. That\'s my answer."',
        c("[Stay with her.]", flags=(COMMITTED, LATE_YES)),
        c("[Leave her.]", "left", flags=(CLOSED, GONE))),
])
_r2_chalk["DelayHours"] = 36
_r2_by[P + "challenge"]["DelayHours"] = 12
for _r2_sid in (NIGHT, MORNING, P + "epilogue.first_blood"):
    _r2_by[_r2_sid]["Requires"].append(P + "truth_clear")
for _r2_sid in (P + "challenge", P + "chalk_circle", NIGHT):
    _r2_by[_r2_sid]["Requires"].append(P + "cage_reckoning_clear")

# JAN-03: the yard can witness this telling and this bout, never the cage.
_r2_challenge = _r2_by[P + "challenge"]
_r2_cn = {n["Id"]: n for n in _r2_challenge["Nodes"]}
_r2_cn["yard"]["Choices"][0]["Next"] = "account"
_r2_challenge["Nodes"].extend([
    jan("account", '{n}A recruit by the trough calls out, "She slipped past the vrocks! Didn\'t even bleed!" '
        'Jannah turns on him, her sword still lowered.{/n} '
        '"Who told you that? I waited in their cage. Ran at Houndheart before that. '
        'You want a story to carry? Watch what I do here."',
        c('"I can vouch for what you told me in the cell. Nothing before it."', "account_heard", forbids=(HH_SEEN,)),
        c('"I saw you try for the quasit. And I saw you run."', "account_saw", requires=(QUASIT_SEEN,)),
        c('"I saw you run at Houndheart. Today the yard can see you fight."', "account_saw", requires=(HH_SEEN,), forbids=(QUASIT_SEEN,))),
    jan("account_heard", '"Then don\'t let them put you outside a cage you never saw. I\'ll tell my part." '
        '{n}She turns back to the waiting ranks.{/n}', c("Continue", "challenge")),
    jan("account_saw", '"Both. Don\'t leave either out." {n}She lifts her sword to her brow.{/n}',
        c("Continue", "challenge")),
])

# The default slots stop at the start of the act. Both original approach
# answers and the cut's original terminal answer retain their positions.
_r2_night = _r2_by[NIGHT]
_r2_cut = next(n for n in _r2_night["Nodes"] if n["Id"] == "cut")
_r2_cut["Text"] = ('{n}She hooks your heel with hers and takes you down onto the cold sand. '
                   'Her mouth finds yours before you can catch your breath, the sand grinding cold under your shoulders and her skin burning above it, the red light of the Wound running along her ribs. '
                   'There is no pretence of measure left, and she is shaking and not ashamed of it.{/n} '
                   '"Look at me," {n}she says.{/n} "No. Do not look at the light. Me."')
_r2_cut["Choices"][0]["Next"] = NIGHT + ".explicit.1"
# Brief: mutually chosen first yard night; crossed blades stay aside.
_r2_night["Nodes"].append(nar(NIGHT + ".explicit.1",
    '{n}The chalk smears beneath your shoulder and the circle stops meaning anything. Her breath comes ragged against your ear, her nails find your back, and all her fencer\'s discipline goes the way of the forms; there is only heat, cold sand and the sound she makes when she stops holding it in. '
    'The watch bell sounds beyond the barracks, and neither of you answers it.{/n}',
    c("[Stay with her.]")))


# The existing companion hook carries the game/posting alternatives. Its
# original node and answer keep their identities; this is now a short dialogue.
_r2_cells = _r2_by[P + "react.seelah_cells"]
_r2_cells.pop("Reaction", None)
_r2_start = _r2_cells["Nodes"][0]
_r2_start["Text"] = ('"Jannah\'s in the gaol." {n}Seelah says it like an accusation, then like good news.{/n} '
    '"She came and found me herself. Had to put the tankard down before she could talk."')
_r2_start["Choices"][0].update(Next="cell_game", Forbids=[POSTING])
_r2_start["Choices"].append(c("Continue", "cell_posting", requires=(POSTING,)))
_r2_cells["Nodes"].extend([
    n("cell_game", "Seelah", '"You played that game with her, and now she\'s staying. I\'d have gone down myself '
      'if anyone had told me." {n}Seelah shakes her head.{/n} "She\'s different. Still arguing, thank the gods. '
      'I\'m going to drag her out for a drink when the watch changes."', c("Continue"), portrait="Seelah"),
    n("cell_posting", "Seelah", '"She won your game, left on the wagon, held the ford. Half her company dead. '
      'Then she chose to come back." {n}Seelah rubs her brow.{/n} "Let her say it in that order. '
      'I\'ve had to hear all of it twice. Now I\'m going to get her a drink."', c("Continue"), portrait="Seelah"),
])
_r2_muster = _r2_by[P + "react.seelah_muster"]["Nodes"][0]
_r2_muster["Text"] = ('{n}Seelah grins before you reach her.{/n} "Jannah told me she said it herself in the yard. '
    'Her name, Houndheart, all of it. Then she tried to skip the part behind the barracks." '
    '{n}She laughs.{/n} "I\'ve never seen her so bad at hiding anything. Give her a reason to keep grinning, Commander."')

# Unresolved false blood belongs to the existing service/refusal ending,
# whose legacy Continue stays effect-free. No new registry surface is needed.
_r2_declined = _r2_by[P + "epilogue.declined"]
_r2_declined["Requires"].remove(DECLINED)
_r2_declined["RequiresAnyGroups"] = [["trickster.ever", DECLINED], [WALLS, LIED, P + "not_confessed"]]
DERIVED[P + "not_confessed"] = [["trickster.ever"]]
_r2_declined["Nodes"][0]["Text"] = (
    '{n}Jannah Aldori stayed in Drezen until the war was over. She trained with the Eagle Watch and fought '
    'where she was sent. The Commander remained outside her chalk.{/n} '
    '{n}When the crusade broke up she went home to Mivon. People there said she had come back quieter, '
    'and a better fencer than when she left. She would not talk about the Commander.{/n}')
_r2_declined["Nodes"][0].setdefault("Paragraphs", []).append(p(
    '{n}The travelling chest remained on the right in every telling she gave. She never chalked another circle '
    'for the Commander. When she returned to Mivon, she took the record with her, unsettled.{/n}',
    requires=(WALLS, LIED, P + "not_confessed")))

import copy as _r2_copy
_r2_letter = _r2_by[P + "alive.letter"]
for _r2_id in ("joined", "joined_free"):
    _r2_original = next(n for n in _r2_letter["Nodes"] if n["Id"] == _r2_id)
    _r2_variant = _r2_copy.deepcopy(_r2_original)
    _r2_variant["Id"] = _r2_id + "_paid"
    _r2_variant["Text"] = _r2_variant["Text"].replace(
        "The jeweller is dead and we got the souls back.",
        "The jeweller is dead. The souls were already free in Drezen, thanks to you and Arsinoe. We brought back empty settings.")
    for _r2_source in list(_r2_letter["Nodes"]):
        for _r2_choice in list(_r2_source["Choices"]):
            if _r2_choice.get("Next") == _r2_id:
                _r2_alt = _r2_copy.deepcopy(_r2_choice)
                _r2_alt["Next"] = _r2_variant["Id"]
                _r2_alt["Requires"].append(P + "guests_home")
                _r2_choice["Forbids"].append(P + "guests_home")
                _r2_source["Choices"].append(_r2_alt)
    _r2_letter["Nodes"].append(_r2_variant)
