"""Wenduag on the Trickster path: "The Mongrel cairn" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, Wenduag block, binding; the
build sheet is in Writer/handoffs/trickster/wenduag.md, "Implementation notes (R6)". It supersedes the spec's lie, rear-guard
order, rehearsal, chaplain's book, bed and cell locators, Every-dawn terms and priced second ask; the canon table stays).

Canon (blueprints.zip / enGB; full GUIDs in the build sheet):
- Her creed: "You... you are stronger than me, yes... this is the right of the strong... Your strength gives you the right to
  decide... only your strength!" (WenduagDefeated/Cue_0010 d6fd4094); "Fighting is the meaning of life, Lann." (Cue_0044
  ef2e3eb8); "I want to live, even if that means you have to die." (WenduTraitor_DrezensStreet/Cue_0012 cb9aa76c); "being
  weak is shameful. The weak get eaten... I'd rather be dead than a coward or a fool." (WenduDubious/Cue_0017 607e8ed0);
  "Survival is the only thing that matters." (FinalSava/Cue_0025 7578c524).
- The kill at Lann's Q1 is the Commander's own blow: [Kill her without a word] -> Cue_0049 fbf606cb ("Maybe you will say
  something, Lann?") -> Cue_0042 fa23e079 (Lann's eulogy, StartEtude WenduagKilled, UnitAttackAndKill by PlayerCharacter).
- Savamelekh's claim: his crystal in his Alushinyrra house, "the poison from my stinger... my children will be graced with a
  true queen" (SavaAndWendu/Cue_0023 b97fe0d7); in Lann's Q2 he calls her "the best of all my daughters" and she answers
  "Yes, master" (SavamelekhAbyss/Cue_0054 06e378ba); Lann's own blow kills her afterwards (LannQ2_WenduagAttackAndDie, Kill
  by Lann_Companion). The street, Ch5: "If you wanted to buy my loyalty, you should have done it before now." (Cue_0011
  b06703f6).
- Mongrel hardiness, his words and hers: "My poison doesn't kill mongrels — it gives them life. A long, long life."
  (SavamelekhAbyss/Cue_0036); "Yes, we are not easily destroyed. You made us tough and strong, creator." (FinalSava/Cue_0009).
  She tracks by scent (SavaIsDeadNow/Cue_0150).

The device (the Commander's plan and nerve, never a mythic power): the Commander's own blow is pulled into a wound that looks
mortal (Mobility, under Lann's eye); the burial is taken alone, under stones, with her knife back in her hand (burying hunters armed is
Lann's word; the loose head end and the dressing are the Commander's own work); she wakes under stones and digs. In the traitor and exile worlds
the Commander buys her before Savamelekh can: she falls in front of his gang, and a Mongrel he believes dead is a Mongrel he
stops sending for: his call stays in her blood until he dies, but nobody comes looking for a corpse. She was never dead:
no raise, no word made true, no document. The engine side, named: the native Kill actions run unchanged, and her native unit
stays dead or gone. RRT revives and recruits nothing. After the return she exists only in RRT's rest-delivered scenes (no
party slot, no presence), the way Galfrey's Kitrane does after the native death at Iz; every later scene reads the authored
return flag, which the relationship's UnavailableOverrides honour. The native death record is the trick's cover story: to
Drezen, to Savamelekh and to every native system she is dead, and the device needs exactly that. Her living self is the spawned
presence copy in Drezen (wenduag_cairn.PRESENCES) and the rest-delivered scenes.

Cost: Lann's trust (he spoke his real eulogy over her, or believed his own blow killed her). The Commander can pay it first
(lann.truth) or when Lann names what he is owed (lann.found_out). Damaged, never ended.

The native romance comes first: every romance scene Forbids wenduag.trickster.native (WenduagRomance_Active playing, or
_Finished seen). RRT starts and completes no native etude.

Path fit (ROUTE-BRIEF-R v1): the early.* hub beats are N-all (no Trickster gate, no romance promise); everything else is T.
"""
from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "wenduag"
W = "wenduag.trickster."

# --- Hosts (every pair retchecked 2026-09-30; see the build sheet B6) --------------------------------------------------------
HUB = "ced27e744d2dded40bbb5adf17816dbb"            # CompanionDialogues/Wenduag/AnswersList_0003 (W path)
HUB_BACK = "a75d1c112c133734f96ae1f25fe17c05"       # Wenduag/Cue_0002, her servile greeting
EXILE_LIST = "0f4612672dd4d3e4d84575b23ffdddb3"     # Wenduag/AnswersList_0017 (the exile answer)
EXILE_BACK = "f436e2adfafcc6541849a828790416ca"     # Wenduag/Cue_0016 "Why? Did I do something wrong...?"
EXILE_CUE = "fa010a1b9f738964782d313580c1c0d1"      # Wenduag/Cue_0020 (Unrecruit + KickedOut)
KILL_LIST = "71ec232384eb5d349aff0b7d60f092ed"      # WenduagDefeated/AnswersList_0045 (the kill list)
KILL_BACK = "1d3ea8f8fe724a841b509dcab0961436"      # WenduagDefeated/Cue_0019 (Lann: "Tell her what she wants to hear...")
KILL_ASK = "fbf606cbf933aa04691bc7cfbe23292a"       # WenduagDefeated/Cue_0049 -> Cue_0042 (the eulogy, then the blow)
TRAITOR_HUB = "9bad7ea452d30254997b153473954cc1"    # WenduagTraitorCompanion/AnswersList_0003 (L path)
TRAITOR_BACK = "daeb0e0796521c042bdd6baebbce7ade"   # WenduagTraitorCompanion/Cue_0002 "How can I be of service?"
TRAITOR_EXILE = "25a503735f9dd5448b84649add442029"  # WenduagTraitorCompanion/AnswersList_0026
TRAITOR_EXILE_BACK = "62fb54095bcb8364fa834213c4283256"  # Cue_0025 "what did I do to draw your ire?"
TRAITOR_EXILE_CUE = "d07647bcdf0e2dc47b9534a3ca4cb048"   # Cue_0029 (Unrecruit + KickedOut)
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"       # CompanionDialogues/Lann/AnswersList_0003
LANN_UNIT = "cb29621d99b902e4da6f5d232352fbda"      # Lann_Companion
DREZEN = "2570015799edf594daf2f076f2f975d8"         # DrezenCapital

# --- Relationship flags ---------------------------------------------------------------------------------------------------
STARTED = "wenduag.started"
CLOSED = "wenduag.closed"
COMMITTED = "wenduag.committed"

# Native reads (trickster_world binds the existing ones on demand; the new ones are in BINDINGS below).
KILLED = "wenduag.killed"                  # WenduagKilled (Lann's Q1, Cue_0042/0044)
DEAD = "wenduag.dead_any"                  # WenduagNotInParty_Dead (in party or ex, and killed or dead)
KICKED = "wenduag.kicked_out"              # WenduagNotInParty_KickedOut (also started by the street's combat)
KICKED_LATCH = "wenduag.kicked_out.latched"
TRAITOR = "wenduag.traitor"                # WenduagTraitor (the L path's recruit)
IN_PARTY = "wenduag.in_party"              # WenduagInParty
ROMANCE = "wenduag.romance_active"         # WenduagRomance_Active (read only)
FINISHED = "wenduag.romance_finished"      # WenduagRomance_Finished (read only)
FINISHED_LATCH = FINISHED + ".latched"
CHOSEN = "wenduag.chosen"                  # Venduag_Chosen (the Prologue: she was chosen over Lann)
REDEEMED = "wenduag.redeemed"              # WenduagRedeemed (the L path's lesson, Cue_0058)
STREET = "wenduag.street_confronted"       # WenduTraitor_DrezensStreet/Cue_0025
HEARD = "wenduag.heard_savamelekh"         # SavaAndWendu/Cue_0023: his promise, overheard
DREW = "wenduag.drew_on_you"               # SavaAndWendu/Cue_0011: caught at the crystal, she drew
FELL = "wenduag.abyss_fell"                # MongrelsDefeated/Cue_0001: "You will never win... Die!" (Lann's blow follows)
Q3_LOYAL = "wenduag.q3_turned_on_him"      # FinalSava/Cue_0035
Q3_BETRAYED = "wenduag.q3_betrayed_you"    # FinalSava/Cue_0025
Q3_SPARED = "wenduag.q3_spared"            # SavaIsDeadNow/Cue_0137
Q3_SENT = "wenduag.q3_sent_away"           # SavaIsDeadNow/Cue_0138 (the Commander's own closure)
Q3_KILLED = "wenduag.q3_killed"            # SavaIsDeadNow/Cue_0139 (the Commander's own kill)
HELLO_SENT = "wenduag.hello_sent_away"     # WenduagHelloAgain/Cue_0016
HELLO_ATTACKED = "wenduag.hello_attacked"  # WenduagHelloAgain/Cue_0033
SAVA_DEAD = "savamelekh.dead"              # Derived: either Q3 completed
YANIEL_FREED = "yaniel.freed"
YANIEL_KILLED = "yaniel.killed"
YANIEL_ASKED = "wenduag.yaniel_death"      # WenduRom_YanielsDeath started (the native romance's own question)
LANN_IN = "lann.in_party"
LANN_GONE = ("lann.dead", "lann.kicked_out", "lann.plot_absent")

# Authored: the route.
NATIVE = W + "native"                      # Derived: the native romance owns her
WITH_YOU = W + "with_you"                  # Derived: she is the Commander's on RRT terms (returned, or kept and earned)
PRIMED = W + "primed"                      # a plan exists to bring her back (the staged blow, or the bid)
STAGED = W + "staged"                      # the Commander chose where the blow would land
CLEAN = W + "stroke_clean"
DEEP = W + "cost.stroke_deep"              # the stroke went deeper than meant: she carries the Commander's scar
CUSTOM = W + "custom_read"                 # the Commander read the Mongrel burial custom
CAIRN = W + "cairn_built"                  # the Neathholm cairn
ABYSS_CAIRN = W + "abyss_cairn"            # the cairn in the rubble of Savamelekh's house
STREET_CAIRN = W + "street_cairn"          # the cairn in the catacombs under the citadel
LIED = W + "cost.lied_to_lann"             # the cost: Lann believes her dead
LANN_ALONE = W + "lann.alone"              # Lann left the burial to the Commander
LANN_WATCHING = W + "lann.watching"        # Lann stayed and watched the stones go on
LANN_KNOWS = W + "lann.knows"              # Lann saw her breathing and walked away (Alushinyrra, a failed Bluff)
LANN_PAID = W + "lann.paid"                # the Commander told Lann first
LANN_PAID_LATE = W + "lann.paid_late"      # the Commander told Lann when he asked
LANN_OWED = W + "lann.owed"                # the Commander refused him the truth
LANN_LIED_AGAIN = W + "lann.lied_again"    # the Commander lied to him a second time
LANN_FOUND = W + "lann.found_out"          # the scene id doubles as the record
WATER = W + "cairn.water"                  # a waterskin left in the cairn
BARE = W + "cairn.bare"                    # nothing but the knife: the Mongrel way
MARK = W + "cairn.mark"                    # the Commander's mark scratched on the underside of the top stone
BOUGHT = W + "bought"                      # the Commander outbid Savamelekh (her allegiance)
FALL_AGREED = W + "fall_agreed"            # she agreed to fall in front of his gang (the bid with the plan)
DEATH_PROMISED = W + "death_promised"      # the Commander promised her Savamelekh's death at her hand
EXILE_AGREED = W + "exile_agreed"          # the dismissal itself was the plan (or the late bid made it one)
UNPLANNED = W + "cost.unplanned"           # a rescue nobody prepared: decided on the spot, and paid for
PASSAGE = W + "abyss_passage"              # the smuggler paid to carry her out of the Abyss when she wakes
STAY_DEAD = W + "stay_dead_ordered"        # the Commander told her, at her return, to stay dead
STREET_LANN = "wenduag.street_lann"        # Lann at the street ambush (his native lines there)
BID_FAILED = W + "bid_failed"
SCORNED = W + "exile_scorned"              # she took the exile for a real one
LATE_FAILED = W + "late_bid_failed"
LATE = W + "cost.late"                     # the bid came late, or the fall was unbought
CHAMPION = W + "champion_seen"
CRYSTAL_DONE = W + "crystal_done"
BOTH = W + "crystal_both"                  # she kept both bids open (survival)
WATCH = W + "cost.watch"                   # the watch was paid off with the Commander's rank (Favors)
BRASK_KNOWS = W + "brask_knows"            # Sergeant Brask saw her breathing in the street
BRASK_MET = W + "brask.met"
RETURNED = W + "returned"
DECLINED = W + "declined"                  # reserved for Last Call's declined slot: never set (her no is the Commander's)
LATE_COMMITTED = W + "late_committed"
SECRET = "trickster.secret.wenduag_cairn"
# Read from the courtship module (wenduag_cairn), declared here for the pages.
PROVED = W + "proved"
GATE_SEEN = W + "gate_seen"

BINDINGS = {
    "Etudes": {CHOSEN: "285ae03094c379045b7cb3106e3f8abf", REDEEMED: "52576309e24d8024fbc08c2ff7016c2f",
               FINISHED: "c3a5748e4a44a1649a75e0968c15a0c1"},
    "SeenCues": {HEARD: ["b97fe0d7003556b4d806c3db9bc15ecf"], DREW: ["f91a06c798cb4394ca80c5f4e927f4d9"],
                 FELL: ["c3ca34383f9ee3a4e9908ce68a2e828b"], Q3_LOYAL: ["c309b3bad07c0cd4aa586a5291da1e2c"],
                 Q3_BETRAYED: ["7578c524612750e4588c8af8dae52f44"], Q3_SPARED: ["121cc01414b509c4098239378424c81c"],
                 Q3_SENT: ["e0a0bc80863383a4cb2e7ded6adc4541"], Q3_KILLED: ["94f483f833d6c9243b539112dbf707d2"],
                 HELLO_SENT: ["0b113d240e700dd4a8dc738452b29613"], HELLO_ATTACKED: ["d84337e5fbe54c1428ac6cdf3f6603ec"],
                 # WenduTraitor_DrezensStreet Cue_0021/Cue_0022: Lann's own lines at the ambush (he is there, active).
                 STREET_LANN: ["bfb97b63903554b4a80cc9a55384c17c", "c724c5e9ac9b0e64e9b24dd77eb00523"]},
    "CompletedQuests": {SAVA_DEAD + ".w": "5ba83bd1a6b1c884794fbb4858480e7f",   # Q3_TraitorsBlood (her Q3)
                        SAVA_DEAD + ".l": "df19bef39c8aa6a4b9dcaf40450b94dc"},  # Q3TheLastResort (Lann's Q3)
}
FELL_LATCH = FELL + ".latched"
STREET_LATCH = "wenduag.street.latched"     # trickster_world LATCHES: <- wenduag.street_confronted
LATCHES = {FINISHED_LATCH: [FINISHED], FELL_LATCH: [FELL]}
DERIVED = {
    NATIVE: [[ROMANCE], [FINISHED_LATCH]],
    WITH_YOU: [[RETURNED], [IN_PARTY, BOUGHT], [IN_PARTY, Q3_LOYAL], [IN_PARTY, Q3_SPARED], [IN_PARTY, REDEEMED]],
    SAVA_DEAD: [[SAVA_DEAD + ".w"], [SAVA_DEAD + ".l"]],
    # No late romance (the Elyanka precedent): eligibility and Last Call read a yes she actually gave.
    LATE_COMMITTED: [["trickster.ever", COMMITTED]],
    # 05 §2.5 voice note: she joins a household as a pack joins, by who is strongest, and says so.
    "wenduag.harem.voice.pack": [[COMMITTED]],
}

RELATIONSHIP = dict(
    Title="The Mongrel cairn",
    Description=("Wenduag of Neathholm believes that only strength gives anyone the right to anything, including the right "
                 "to decide who lives. I have decided that she does, more than once, and not always in the way anyone "
                 "watching believed."),
    Objective="Find out what Wenduag does with what I gave her",
    Guidance=("On the Trickster path, when Wenduag's life is in your hands (at Lann's reckoning in Neathholm, in "
              "Savamelekh's house, or when she has gone over to him), a blow can be chosen, a burial can be taken alone, "
              "and a Mongrel can be bought before her master buys her. What she does after that is her own affair."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[KILLED, DEAD, KICKED, Q3_SENT, Q3_KILLED, HELLO_SENT, HELLO_ATTACKED],
    FailureFlags=[],
    UnavailableOverrides={KILLED: RETURNED, DEAD: RETURNED, KICKED: RETURNED},
    TricksterAccess={
        # WenduagNotInParty_Dead can join WenduagKilled (its activation reads WenduagKilled for an eligible companion):
        # the killed world's device pages ignore both.
        "killed": dict(detect=[KILLED, DEAD], device=W + "killed.back", returned=RETURNED),
        "abyss": dict(detect=[DEAD, "!" + KICKED], device=W + "abyss.back", returned=RETURNED),
        "exiled": dict(detect=[KICKED, "!" + DEAD], device=W + "exile.late_bid", returned=RETURNED),
        "street": dict(detect=[KICKED, DEAD], device=W + "street.back", returned=RETURNED),
    },
)

# Path fit tags (ROUTE-BRIEF-R v1): T = Trickster only; N-all = any path, no gate.
PATH_FIT = {}


def tag(scene_id, fit):
    PATH_FIT[scene_id] = fit


def conv(id, text, *choices, **kw):
    """Wenduag inside her own native dialog (the conversant)."""
    return n(id, "conversant", text, *choices, **kw)


def lann(id, text, *choices, **kw):
    """Lann speaking inside a native dialog he shares (E14f native speaker)."""
    return n(id, "Lann", text, *choices, speaker_unit=LANN_UNIT, **kw)


def wd(id, text, *choices, **kw):
    """Wenduag on a rest-delivered page."""
    return n(id, "Wenduag", text, *choices, portrait="Wenduag", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def inline(id, title, chapters, entry, nodes, lists, back, requires=(), forbids=(), fit="T", **extra):
    SCENES.append(scene(id, title, "Wenduag", min(chapters), entry, nodes, requires=requires, forbids=(id,) + tuple(forbids),
                        last=max(chapters), Relationship=REL, Chapters=list(chapters), AnswerLists=list(lists),
                        NativeReturnCue=back, **extra))
    tag(id, fit)


def page(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="visit", areas=(DREZEN,), optional=False,
         owner="Wenduag", **extra):
    """A rest-delivered page. Drezen visits wait for a rest in the capital, where she keeps to the cellars."""
    body = scene(id, title, owner, min(chapters), "", nodes, requires=tuple(dict.fromkeys(requires)),
                 forbids=tuple(dict.fromkeys((id,) + tuple(forbids))), delay=delay, last=max(chapters), optional=optional,
                 Relationship=REL, Chapters=list(chapters), Remote=True, Kind=kind, **extra)
    if areas:
        body["Areas"] = list(areas)
    SCENES.append(body)
    tag(id, "T")


def device(state):
    return dict(TricksterDevice=True, TricksterState=state)


# --- 1. Early beats (N-all, W path, inline on her hub): Chapters 1-3. No Trickster gate, no romance promise. -----------------

inline(W + "early.teeth", "Counting teeth", (1,), '"The uplanders keep staring at you."', [
    conv("start", '''{n}Wenduag is crouched on an overturned cart at the edge of the street, knees up, chewing a strip of dried meat she has found in somebody's ruined larder. Two crusaders go past with a stretcher between them and look at her the way people look at a dog that has slipped its rope. She watches them all the way to the corner, still chewing.{/n}
"Staring? They're counting my teeth, {mf|master|mistress}. Every uplander in this city does it. They look at my mouth, then at my hands, then at my mouth again, as if I might have more teeth than they do and they want to know how many before I use them." {n}She tears off another strip with her canines, slowly, for the benefit of a woman hurrying past with a bucket.{/n} "I don't mind. In the caves, a stare is a question. I'm only waiting for one of them to ask it properly."''',
        c('"Then smile at them. Let them count."', "smile"),
        c('"They watched demons eat their neighbours last night. Let them stare."', "afraid"),
        c('"Stare back. See who looks away first."', "stare")),
    conv("smile", '''{n}Wenduag considers this, then turns on the cart and smiles at the next passer-by: a clerk in a torn surcoat with a sheaf of lists under his arm. It is a very complete smile. It goes all the way back.{/n}
{n}The clerk walks into a lamp post, apologises to it, and walks faster.{/n}
"Ha!" {n}She slaps her knee.{/n} "You see? He'll count them in his sleep tonight. That's better than a knife, sometimes. A knife you have to clean." {n}She settles back on her heels, pleased with the world for a moment, and then the moment passes.{/n} "But it only works on the soft ones. Show your teeth to something hungrier than you and it takes it as an invitation."''',
        c('"And what do you do then?"', "then")),
    conv("then", '''"Then you find out which of you is stronger. Quickly." {n}She shrugs, as if it were a question of weather.{/n} "Down in Neathholm you learn it before you learn to talk. The strong eat, the weak get eaten, and the ones in the middle spend their whole lives pretending to be one or the other. I stopped pretending when I was small. It saves time."
{n}She looks at you, a long measuring look, from boots to eyes.{/n} "You don't pretend either. That's why I'm on your side of the street, and not theirs."''',
        c("Continue", flags=(W + "early.teeth.smile",))),
    conv("afraid", '''"Their neighbours were slow." {n}She says it without cruelty, the way she might say that their neighbours were tall.{/n} "Fear is honest, {mf|master|mistress}. I like fear. A man who is afraid of you tells you the truth about where he'll run. But these ones are afraid of the wrong thing. They look at me and see a demon's dog. The demon's dogs ate their neighbours. I only ate their bread."''',
        c('"And if you had been slow?"', "slow"),
        c('"Nobody here thinks you\'re a demon\'s dog."', "dog")),
    conv("slow", '''"Then I'd be meat, and I wouldn't complain about it." {n}She finishes the strip and licks her fingers clean, one at a time.{/n} "Meat doesn't complain. That's the whole difference between meat and a hunter. The hunter has something to say about it."''',
        c("Continue", flags=(W + "early.teeth.afraid",))),
    conv("dog", '''{n}Wenduag laughs at you, not unkindly, the way you laugh at a child who has told you the sea is small.{/n} "Everyone here thinks it, {mf|master|mistress}. The ones who don't say it are the ones who are afraid of you. When you're gone, they'll say it. That's all right. When you're gone, I'll have something to say too."''',
        c("Continue", flags=(W + "early.teeth.afraid",))),
    conv("stare", '''{n}That pleases her. It pleases her so much that for a moment she looks almost young.{/n}
"Yes. That's it. That's the whole of it." {n}She hops down from the cart and plants herself in the middle of the street, feet apart, and fixes her yellow eyes on a burly sergeant coming the other way with a crate on his shoulder. He meets the stare. He holds it for three steps. On the fourth he finds something very interesting in the gutter.{/n}
{n}She turns back to you with her chin up.{/n} "Three steps. An uplander. Not bad. In Neathholm that one would have been something, maybe a hunter's second." {n}Her voice drops, and the play goes out of it.{/n} "The ones who look at their boots, {mf|master|mistress}, you can walk past. The ones who hold your eye, you watch. And the ones who hold it and smile, you kill first, before they decide to do it to you."''',
        c('"Which kind am I?"', "which")),
    conv("which", '''{n}Wenduag holds your eyes, the way she held the sergeant's, and neither of you looks down. Somewhere behind her a cart goes by, and a bell rings for the dead, and neither of you looks at that either.{/n}
"The kind I follow." {n}She breaks it first, which she clearly did not expect to do, and covers it with a grin.{/n} "For now. The strong have the right to lead. When you stop being strong, I'll tell you. I'll be the first to."''',
        c("Continue", flags=(W + "early.teeth.stare",))),
], [HUB], HUB_BACK, fit="N-all")

inline(W + "early.walls", "Men in rows", (2,), '"You\'ve been watching the knights drill all morning."', [
    conv("start", '''{n}Wenduag sits on a crate of arrows at the edge of the drill field, with her elbows on her knees and her chin on her fists. Out on the trampled grass a company of crusaders is practising a pike wall, three ranks deep, stepping and bracing and stepping again to a sergeant's bellow.{/n}
"All morning, {mf|master|mistress}. I can't stop. It's like watching beetles build a nest." {n}She points with her chin.{/n} "They stand in rows so the demons can count them faster. They wear the same colours so the demons know which ones to eat. They shout before they charge, so nobody is surprised. Uplanders make a war the way they make a bed: neat, and to be slept in."''',
        c('"A line doesn\'t break when one man is afraid. That\'s the point of it."', "line"),
        c('"How would a Mongrel take Drezen, then?"', "take"),
        c('"You don\'t have to fight in their rows. You fight in mine."', "mine")),
    conv("line", '''{n}She chews on that, and does not like the taste.{/n} "No. It breaks when all of them are afraid at once. Which is worse." {n}She nods at the third rank, where a boy is leaning on his pike to rest.{/n} "That one will die first. He knows it. His friends know it. They keep him in the middle so he can't run, and they call it courage." {n}Her lip curls.{/n} "Sull would do the same, back home. Share the last of the food with the ones who can't hunt, and starve together, and call it the tribe. That's why my people are still living in a hole." {n}She spits.{/n} "If I were chief, the ones who couldn't stand alone wouldn't eat the ones who could. Your way is kinder. It's also why your city is full of demons."''',
        c('"And yet the city is still ours."', "ours")),
    conv("ours", '''"Yours." {n}She says it carefully, as if tasting it.{/n} "Because you're strong, not because they stand in rows. Every one of those men is here because you walked into a demon's army and came out with his head. They follow you because you're strong. The day you aren't, they'll follow somebody else." {n}She shrugs.{/n} "So would I. That's not an insult, {mf|master|mistress}. It's the only honest thing anybody here will ever tell you."''',
        c("Continue", flags=(W + "early.walls.line",))),
    conv("take", '''{n}Her whole face changes. You have never before seen her look at the city walls as a problem instead of a view.{/n}
"Not from the front. Only fools and uplanders go in the front." {n}She sketches in the dirt with the point of an arrow: the wall, the gate, the old river culvert at the west corner, the sewer grates in the lower town.{/n} "There's always a hole. The demons came in through one. Rats come in through the same ones. You send your quiet people down in the night, ten or twelve, with knives and no armour, and you cut the throats on the gate from the inside while the fools are still shouting at the front. By morning it's your gate." {n}She sits back.{/n} "And you don't lose the boy in the third rank. You lose the ten who went down the hole, and they're the ones who knew the risk."''',
        c('"That\'s not how crusaders fight."', "crusaders"),
        c('"Ten who knew the risk. I\'ll remember that."', "remember")),
    conv("crusaders", '''"No. That's why they lose so often." {n}She scuffs the map out with her heel.{/n} "I'm not a crusader, {mf|master|mistress}. I'm a hunter who happens to be standing in your camp. Hunters don't care if the deer thinks it was fair."''',
        c("Continue", flags=(W + "early.walls.take",))),
    conv("remember", '''{n}She looks at you sideways, a slow, delighted look, as if you had just dropped your guard in a fight and shown her something she was not supposed to see.{/n}
"You will, won't you. You'll remember it the night you need it and pretend it was your idea." {n}She laughs.{/n} "Good. I don't care whose idea it was, as long as I'm one of the ten."''',
        c("Continue", flags=(W + "early.walls.take",))),
    conv("mine", '''{n}She turns her head and studies you, chin still on her fists.{/n} "Yours. And what do yours look like, {mf|master|mistress}? A deserter's daughter, a thief who prays, a man who talks to his sword. And me." {n}She seems to find this funny for a while.{/n} "No rows. No colours. Everybody bites. I like it."
{n}Then, lower, watching the pike wall step and brace and step:{/n} "But don't make the mistake the uplanders make with their rows, and think I'll stand where you put me because you put me there. I stand next to you because you're the strongest thing on this field. That's a better leash than a row. And easier to slip."''',
        c("Continue", flags=(W + "early.walls.mine",))),
], [HUB], HUB_BACK, fit="N-all")

inline(W + "early.gate", "The south gate", (3,), '"Something happened at the south gate. The whole citadel is talking."', [
    conv("start", '''{n}Wenduag is in a foul, quiet temper, which is worse than a loud one. She is sitting with her back to the wall, whetting a knife that is already sharp, and she does not look up.{/n}
"Talking. Of course they are." {n}The stone scrapes along the edge, once, twice.{/n} "I went out through the south gate before sunrise to hunt. There's a sergeant there, a big man with a red neck and a new coat. Brask, they call him. He made me stand in the road while the carts went through. All the carts. Then all the men. Then a goat." {n}Scrape.{/n} "Then he let me through, and when my back was to him he said to his men, *there goes the Commander's mongrel bitch, back to her kennel*. They laughed. He thought I didn't hear." {n}She finally looks up. Her eyes are very flat.{/n} "I can hear a rat cough through three walls, {mf|master|mistress}. I heard every one of them laugh."''',
        c('"I\'ll have him on latrine duty until the war is over."', "latrine"),
        c('"Then answer him yourself. Nobody dies."', "answer"),
        c('"He\'s a crusader and you\'re a guest in his city. Walk past."', "guest")),
    conv("latrine", '''{n}The whetstone stops.{/n} "You'll fight my fights for me? In front of his men?" {n}She shakes her head, slowly, like someone correcting a child who means well.{/n} "Then every one of them learns that the mongrel bitch has to run to her {mf|master|mistress} when a sergeant bites her. And the next one bites harder, because now he knows I won't bite back." {n}She starts on the knife again.{/n} "If anybody settles my quarrel for me, everyone knows I couldn't. I might as well lie down in the road and let them walk over me."''',
        c('"Then what do you want?"', "want")),
    conv("want", '''"What I want is to open him from the belt to the chin." {n}She says it pleasantly.{/n} "What I'll do is nothing, because you'd have to hang me, and I'm not stupid. So I'll wait. He'll forget. Uplanders always forget." {n}The knife catches the lamplight.{/n} "I never do."''',
        c("Continue", flags=(BRASK_MET, W + "gate_early.fought_for"))),
    conv("answer", '''{n}She sets the whetstone down very carefully, as if it were something that might break.{/n} "Nobody dies." {n}She repeats it the way you would repeat the terms of a bad bargain.{/n} "You're no fun, {mf|master|mistress}." {n}But she is smiling, and it is the real smile, the one with no play in it.{/n} "Nobody dies. But he'll wish he had. He likes his new coat so much. He brushes it. I've watched him brush it." {n}She tests the edge of the knife against her thumb, and a bead of blood comes up, and she licks it off.{/n} "Let's see how he likes it with the sleeves off. In front of the same men. Nobody dies."''',
        c('"Nobody. I mean it."', "mean")),
    conv("mean", '''"I heard you the first time." {n}She stands, stretches until her joints crack, and slides the knife away.{/n} "A hunter who kills everything that insults her starves in a month, {mf|master|mistress}. There's no meat left. You have to leave some of them walking, so they remember." {n}At the door she looks back.{/n} "He'll remember."''',
        c("Continue", flags=(BRASK_MET, W + "gate_early.let_her"))),
    conv("guest", '''{n}For a heartbeat the whole of her goes still, the stillness of something that has decided whether to spring and chosen not to, yet.{/n}
"A guest." {n}She tastes the word and spits it out.{/n} "Yes, {mf|master|mistress}. A guest. I'll walk past. I'll walk past him every morning with my eyes on my boots like a good dog, and he'll laugh every morning, and I'll remember every one." {n}She bows. It is a perfectly servile bow, and there is nothing servile in it at all.{/n} "I'll remember whose guest I am, too."''',
        c("Continue", flags=(BRASK_MET, W + "gate_early.rebuked"))),
], [HUB], HUB_BACK, fit="N-all", Areas=[DREZEN])

inline(W + "early.yaniel", "A legend of the crusades", (3, 4, 5), '"You\'ve been watching me since the Midnight Fane."', [
    conv("start", '''{n}Wenduag does not deny it. She has been walking a pace behind you and a little to the left since the Fane, where she can see your hands.{/n}
"I've been thinking about the paladin in the cage." {n}She waits to see what your face does.{/n}''',
        c("Continue", "freed", requires=(YANIEL_FREED,)),
        c("Continue", "killed", forbids=(YANIEL_FREED,))),
    conv("freed", '''"Seventy years a prisoner, first on Areelu's tables and then in Minagho's Fane, {mf|master|mistress}, until they made her a husk, and she still walks out of it straighter than your knights walk out of their beds." {n}There is no mockery in it. It is the respect one predator gives another across a clearing.{/n} "They say she fought them the whole first stretch of it, every guard she could reach. I'd have done the same, and lost the same." {n}She rolls her shoulders.{/n} "Your crusaders will follow a legend before they follow a living {mf|man|woman}. The legends don't make mistakes. They're dead, or they might as well be. That one's neither. I'd watch her."''',
        c('"She\'s an ally. We need every one we can get."', "ally"),
        c('"You sound jealous."', "jealous")),
    conv("ally", '''"Allies are what you call people who haven't decided yet." {n}She shrugs.{/n} "I'm not saying kill her. I'm saying watch her. There's a difference, and uplanders never learn it until the knife's already in."''',
        c("Continue", flags=(W + "yaniel.watched",))),
    conv("jealous", '''{n}She bares her teeth, which is not a no.{/n} "Of a woman a demon turned into a husk? No. Nobody ever turned me into anything I didn't choose." {n}Then, more quietly:{/n} "Of what they'll say about her when this is over, maybe. Nobody will ever write songs about a neather. We don't last long enough to be legends."''',
        c("Continue", flags=(W + "yaniel.jealous",))),
    conv("killed", '''"You killed her." {n}She says it the way she might say you had eaten the last of the bread: an observation, filed for later.{/n} "The legend of the crusades, seventy years a prisoner and a husk in Minagho's Fane, and you put her down there, in the Fane. I've been trying to work out why." {n}She tilts her head.{/n} "If you were afraid of her, that's cunning. If you were bored, that's a sickness. I want to know which one I'm following."''',
        c('"She\'d have been a rival. Better now than later."', "rival"),
        c('"It was a mistake."', "mistake"),
        c('"That\'s mine to know."', "mine")),
    conv("rival", '''{n}She is quiet for a while. Then a slow smile.{/n} "Now or later. Yes. That's how we do it in the tunnels too, when two hunters want the same place by the fire." {n}She nods, satisfied, as if a knot has been untied.{/n} "I'll remember that you know how. And that you don't warn anyone first."''',
        c("Continue", flags=(W + "yaniel.rival",))),
    conv("mistake", '''{n}Her disappointment is sharper than anger would have been.{/n} "A mistake." {n}She looks away.{/n} "I was hoping for something clever. The strong are allowed to kill. They're not allowed to be stupid about it. That's how you stop being strong."''',
        c("Continue", flags=(W + "yaniel.mistake",))),
    conv("mine", '''"Is it." {n}She gives you a long, flat look, the look she gives a trail that goes into rock and stops.{/n} "Fine. Keep it. I'll find out on my own. I always do."''',
        c("Continue", flags=(W + "yaniel.kept",))),
], [HUB], HUB_BACK, fit="N-all", RequiresAnyGroups=[[YANIEL_FREED, YANIEL_KILLED]], forbids=(YANIEL_ASKED,))


# --- 2. The staged blow (T, L path, Chapter 3): inline on the kill list, before Cue_0049 and the Commander's own blow. ------

SCENES.append(scene(W + "killed.stage", "Where the blow lands", "Wenduag", 3,
    '[Strike the blow yourself, and choose where it lands] "Say your piece to her, Lann. I\'ll be the one to finish it."', [
    nar("start", '''{n}She is on her knees in the muck of the cave floor with one hand clamped over the hole in her side, and she is grinning at you through her own blood. Behind her the tunnel goes down into the dark. Beside you Lann has turned half away, the way a man turns from a fire he does not want to see go out. He will watch the end, because he is Lann. He will not watch closely.{/n}
{n}You have killed enough to know how it looks. There is a place low on the left side, under the last rib, where a blade can go in to the hilt and bring out more blood than anyone should have in them, and miss everything that stops a heart. It looks like a death. It bleeds like a death. Done right, it is a very long sleep and a very bad morning.{/n}
{n}You came down these tunnels knowing how Lann's reckoning was likely to end, and you came ready for it: a field dressing and a stoppered vial of healer's draught in your belt pouch, where nobody looks.{/n}
{n}Done wrong, it is a death. And if Lann sees the edge turn, he will ask you why, and you will have to answer him.{/n}''',
        c('[Strike low, under the ribs, and turn the edge at the last moment.]',
          check=dict(Skill="SkillMobility", DC=24, Success="clean", Failure="deep")),
        c('"Wait."', abort=True)),
    nar("clean", '''{n}Your hand is steady. You settle your weight, measure the distance with your eyes, and put the whole of the killing in your face and none of it in your wrist. Lann sees a Commander about to end it. Wenduag, who has seen more killing blows coming than anyone alive, sees the same.{/n}
{n}Good. Let them both believe it.{/n}''',
        c("[Let her have her last word.]", native_next=KILL_ASK, flags=(STAGED, PRIMED, CLEAN))),
    nar("deep", '''{n}Your grip is slick with her blood, and the angle is wrong: she has shifted on her knees, the way the dying do, and the place under the rib is not where it was. You know it before you move. It is going to go deeper than you want. It is going to go very close.{/n}
{n}You do not stop. Stopping now would be the one thing Lann would never forget.{/n}''',
        c("[Let her have her last word.]", native_next=KILL_ASK, flags=(STAGED, PRIMED, DEEP))),
], requires=("trickster",), forbids=(STAGED,), last=3, Relationship=REL, Chapters=[3], AnswerLists=[KILL_LIST],
    NativeReturnCue=KILL_BACK, EntryMythic="PlayerIsTrickster", **device("killed")))
tag(W + "killed.stage", "T")


def cairn_close(extra=()):
    """The last choice at every cairn: what the Commander leaves with her besides the knife."""
    return (
        c('[Leave the knife and nothing else.]', flags=(BARE,) + tuple(extra)),
        c('[Leave the knife, and your own waterskin under her other hand.]', flags=(WATER,) + tuple(extra)),
        c('[Leave the knife, and scratch your mark into the underside of the top stone with it first.]', flags=(MARK,) + tuple(extra)),
    )


CAIRN_SET = (CAIRN, LIED, SECRET, PRIMED)

page(W + "killed.cairn", "The Mongrel cairn", [
    nar("start", '''{n}The first night you rest after Neathholm you do not sleep. You lie with your eyes open and go over it again, every stone, the way you went over it at the time, in the tunnel, after the others had gone.{/n}
{n}Lann said his words over her. You heard every one of them: that her soul might find peace wherever it ended up, since it had clearly not found it here. He meant them. Then your blade came down, low on the left side, and she folded over it with a look of pure satisfaction, as if you had finally done something she approved of, and lay still in the muck.{/n}
{n}Now the others have gone back up the passage toward the light, and there is only Lann, standing over her with his arms hanging, and you, kneeling. You put two fingers under the angle of her jaw as a matter of form, the way anyone would.{/n}''',
        c("Continue", "pulse")),
    nar("pulse", '''{n}There it is. Faint, and slow, and very far down, like somebody knocking on a door at the bottom of a well.{/n}''',
        c("Continue", "tunnel", forbids=(DEEP,)),
        c("Continue", "tunnel_deep", requires=(DEEP,))),
    nar("tunnel", '''{n}The wound under her rib is ugly and bleeding freely, which is what you wanted: a lot of blood makes a death, for anyone who is not looking closely. It will close. You have watched neathers in these tunnels take wounds that would have dropped a crusader where he stood, and get up, and bite; tonight you are counting on it.{/n}
{n}Now you have to put her somewhere nobody will look, and where she can get out.{/n}''',
        c("Continue", "read")),
    nar("tunnel_deep", '''{n}Barely. The blade went in closer than you meant, and the blood that comes is darker than it should be. She may not wake. If she does, she will carry your stroke in her side for the rest of her life, and she will know exactly how close you came, because she will have felt it.{/n}
{n}Now you have to put her somewhere nobody will look, and where she can get out, if she can get out.{/n}''',
        c("Continue", "read")),
    nar("read", '''{n}A little way back up the tunnel there is a side passage you passed on the way down, low and choked with fallen rock. You remember it because of the stones: piled deliberately, in heaps as long as a body, some old and furred with grey mould, some new.{/n}''',
        c('[Look at the heaps properly, the way a hunter reads a trail.]',
          check=dict(Skill="SkillLoreNature", DC=18, Success="custom", Failure="guess")),
        c('[Think back over what you have heard of neather customs.]',
          check=dict(Skill="SkillKnowledgeWorld", DC=18, Success="custom", Failure="guess"))),
    nar("custom", '''{n}They are graves. Every heap is the length of a body, and at the foot of the newest one the hilt of a knife shows between two rocks, where the dead man's hand still holds it. Somebody buried a hunter here and sent him into the dark armed.{/n}''',
        c('"Lann. Those heaps in the side tunnel. Is that how your people bury their own?"', "lann_custom", flags=(CUSTOM,))),
    lann("lann_custom", '''{n}Lann looks at the side passage, and then at her, and his face does something complicated.{/n} "Hunters, yes. Under stones, so the rats don't get them, and armed. You don't send a hunter anywhere without a knife." {n}He rubs his eyes with the heel of his hand.{/n} "She should go armed. Whatever she did. She should go armed."''',
        c('"Then I\'ll do it for her. Alone. She was my kill, and she\'d have wanted it done by the one who beat her."',
          check=dict(Skill="CheckBluff", DC=18, Success="alone", Failure="watching"))),
    nar("guess", '''{n}You cannot make sense of them. Rockfall, maybe, or old Mongrel middens, or somebody's idea of a wall.{/n}''',
        c("Continue", "lann_guess")),
    lann("lann_guess", '''{n}Lann follows your look to the side passage.{/n} "Graves. Hunters' graves." {n}He sounds very tired.{/n} "We put our dead under stones, so the rats don't get them, and the hunters with their knives. I suppose I ought to do that for her. After everything." {n}He does not move.{/n} "Or we burn her. Or we leave her for the rats. She'd have left me for the rats and been proud of it."''',
        c('"No. Stones. And I\'ll do it alone. She was my kill; it should be the one who beat her."',
          check=dict(Skill="CheckBluff", DC=24, Success="alone", Failure="watching"))),
    lann("alone", '''{n}He looks at you for a while, and something in his face gives way, relief or shame, and you cannot tell which and neither can he.{/n}
"Yeah. Yeah, that's... that's right. She'd have wanted it to be you. She never gave a damn what I thought." {n}He takes a step toward her, and stops.{/n} "Put her knife in her right hand. She's right-handed. Always was." {n}Then he goes back up the passage toward the others and the light, and does not look back, and you are alone with her in the dark.{/n}''',
        c("Continue", "build")),
    lann("watching", '''"Alone?" {n}Lann frowns.{/n} "No. No, I'll stay. I'm not leaving you down here by yourself with... I'll stay." {n}He goes to the mouth of the side passage and leans on the rock there with his arms folded, where he can see everything and help with nothing, and watches you work.{/n}''',
        c("Continue", "build_watched")),
    nar("build", '''{n}You carry her into the side passage yourself. She is heavier than she looks, all wire and gristle, and her blood soaks your sleeves to the elbow. You lay her on her back in the space beside the newest grave, and before anything else you open her shirt, pack the wound with the dressing from your pouch, bind it tight, and tip the healer's draught between her teeth, stroking her throat until she swallows. Then you build.{/n}
{n}Flat stones first, over her legs and body, set on edge against each other so that they roof her rather than press on her. Nothing she could not shift from underneath with her knees and her back. At the head end, which no grave you saw had, you leave a gap for air, packed loosely with fist-sized rocks that one push would send rolling. It takes a long time. It is the most careful thing you have done since you came to Drezen.{/n}
{n}Her knife is in the muck of the cave where it fell when your blade went in. You fetch it, and wipe it on your own knee, and open her right hand, and close her fingers round the grip.{/n}''',
        *cairn_close((LANN_ALONE,))),
    nar("build_watched", '''{n}You carry her into the side passage, with Lann's eyes on your back the whole way. "So she doesn't leak through the stones," you tell him, binding her side tight with the dressing from your pouch, and he looks away, because it is the kind of thing a soldier does for a corpse and he cannot bear to watch it. While he is looking away, the vial goes between her teeth.{/n}
{n}You lay her beside the newest grave and you build the way you would build if you meant it: flat stones on edge, and at the head end loose rock. Whether the loose rock is for air or for want of better stones, Lann does not ask. He knows hunters' graves. He does not know you.{/n}
{n}When you go back for her knife he says, "Right hand," before you can ask, and his voice cracks on it. You close her fingers round the grip while he watches. From where he stands it is a mercy. From where you kneel you can feel her pulse knock against your thumb through the hilt.{/n}''',
        *cairn_close((LANN_WATCHING,))),
], requires=("trickster.ever", KILLED, STAGED), forbids=(CAIRN,), delay=2, chapters=(3,), kind="event", areas=(),
    **device("killed"))

# The page's closing choices each record the cairn and the lie together.
for _node in SCENES[-1]["Nodes"]:
    for _choice in _node["Choices"]:
        if any(f in (BARE, WATER, MARK) for f in _choice["Set"]):
            _choice["Set"] = list(dict.fromkeys(list(_choice["Set"]) + list(CAIRN_SET)))


# --- 3. She digs (T): the killed world's return, in Drezen. ------------------------------------------------------------------

# The Commander's own no at a return: she goes back to the dark on her own feet, and the route closes.
CLOSING_NO = c('[Let the dark keep her] "Go back under your stones, Wenduag. Stay dead."', "stay_dead")


RETURN_SET = (RETURNED, STARTED)

page(W + "killed.back", "A dead woman at the south gate", [
    nar("start", '''{n}The sentries at your door have not seen anyone go in. The shutters are fastened from the inside. And yet there is somebody sitting on your map table in the dark, with her feet on your chair, eating your supper out of the pot with her fingers.{/n}
{n}She smells of wet stone and old blood and the deep places under Kenabres. Her hair is full of grit. There is a dark crust down her left side from the ribs to the hip, where the shirt is torn, and under the crust a raw pink seam where the stroke went in. Across her knees lies a knife, a long hunter's knife with a bone grip, the one you closed her fingers round in the dark.{/n}''',
        c("Continue", "her")),
    wd("her", '''"You're late." {n}Wenduag licks gravy off her thumb.{/n} "Your sergeant at the south gate nearly wet himself. Brask, they call him. Big red neck. He watched a dead woman walk in through his gate with her own grave on her, and he crossed himself, and then he pretended he hadn't seen anything, because what would he tell his captain?" {n}She laughs, and then winces, and puts a hand to her side.{/n} "Uplanders. They'd rather be blind than stupid."''',
        c("Continue", "dark")),
    wd("dark", '''{n}She sets down the pot.{/n} "Do you know what it's like, waking up under stones? No. Nobody does. The dead don't tell, and I'm the only one who ever came back to say." {n}She says it lightly. Her hand has gone to the knife.{/n} "It's black. Blacker than anything in Neathholm. There's a stone on your face, and one on your chest, and your side is full of fire, and you think: *so this is where the weak go*. And then you notice there's a knife in your hand."
{n}Her fingers close round the bone grip, and open, and close, as they must have done in the dark.{/n} "My own knife. In my right hand. And a dressing on my side, tied tight, and the taste of some uplander healer's muck in my mouth. Somebody wanted me to have it all."''',
        c("Continue", "water", requires=(WATER,)),
        c("Continue", "mark", requires=(MARK,), forbids=(WATER,)),
        c("Continue", "bare", forbids=(WATER, MARK))),
    wd("water", '''"And there was water, under my other hand. An uplander's waterskin. It had your smell on it." {n}She makes a face.{/n} "That's not how it's done. A hunter goes to the dark with a knife, and that's all. The water was soft. But I drank it, the second day, when my tongue was stuck to my teeth." {n}A pause.{/n} "It was good water."''',
        c("Continue", "why")),
    wd("mark", '''"And when I pushed the top stone off, there were scratches on the underside of it. Your mark. Cut with my own knife, before you put it back in my hand." {n}She reaches into her shirt and sets a flat grey stone on the table between you, scratched side up.{/n} "I brought it. I didn't know if it was a curse or a signature. In the tunnels we'd call it a claim."''',
        c("Continue", "why")),
    wd("bare", '''"Nothing else. No water, no light, nothing soft." {n}She sounds almost proud of you.{/n} "Just the knife, the way it's done for a hunter. Whoever built that cairn knew the old way, or asked someone who did. I dug for two days with nothing in my belly and I thought about that the whole time: who knew enough to do it right, and wrong enough to leave the head end loose."''',
        c("Continue", "why")),
    wd("why", '''{n}She slides off the table and stands, slowly, favouring the side. She is shorter than you remember. She is also between you and the door.{/n}
"So. You struck me down in front of Lann, and you put me under stones with my knife, and you left the head end loose. You wanted me dead to everybody but you." {n}The knife comes up, easily, point first, not quite at your throat.{/n} "Give me one reason I shouldn't open your throat for it. The strong have the right to decide. You decided. Now I'm deciding."''',
        c("Continue", "deep", requires=(DEEP,)),
        c("Continue", "lann", forbids=(DEEP,))),
    wd("deep", '''{n}She lifts the torn shirt with her free hand. The pink seam runs far closer to the middle of her than it should, and the flesh round it is still angry and swollen.{/n} "You nearly did it for real. Another finger's width and there'd have been nobody to wake up. I felt it go in. I felt you know." {n}She lets the shirt fall.{/n} "I'll owe you that. One day I'll put it back where it came from."''',
        c("Continue", "lann")),
    wd("lann", '''"Lann said words over me." {n}Something ugly crosses her face, and it is not anger.{/n} "I heard him. I was still awake, just. *May your soul find peace wherever it ends up.* Little Lann, with his soft heart, wishing me peace." {n}She spits on your floor.{/n} "You let him say it. You let him mean it. You knew the whole time." {n}The knife steadies.{/n} "That's the only part I don't understand. And it's the part I like best."''',
        c('"Because you dug."', "dug"),
        c('"Try it. You\'ve been in the ground for days, and I haven\'t."', "try"),
        CLOSING_NO),
    wd("dug", '''{n}She stares at you. Then she begins to laugh, a hoarse, delighted, painful laugh, bent over her wound.{/n}
"Because I dug." {n}The knife drops to her side.{/n} "Yes. That's it. That's exactly it. You didn't save me. You gave me a knife and a heap of stones and let me find out if I was strong enough to get out. The weak would have died down there. I didn't." {n}She wipes her eyes with the back of her wrist.{/n} "You're the first uplander who ever understood a thing about us."''',
        c("Continue", "now")),
    wd("try", '''{n}For a heartbeat you think she will. Her weight goes onto the balls of her feet and the point of the knife lifts a finger's width.{/n}
{n}Then she grins, all her teeth.{/n} "Days. You counted them." {n}She lowers the knife.{/n} "Good. You're right. I'd lose, today. And I don't fight to lose." {n}She sheathes it without looking.{/n} "Another day, when I'm whole. You'll know it when it comes. I won't send word."''',
        c("Continue", "now")),
    wd("now", '''{n}She sits down again, on your table, and pulls the pot back into her lap.{/n}
"Here's how it will be. I'm dead. Lann says so, and Lann doesn't lie; that's his whole trouble. So I stay dead, up here. Down in the cellars under your citadel there are neathers now, some of Sull's, some strays, a few who ran from Savamelekh, and they'll hide a dead hunter for a while without asking why. I've already been down there. Nobody asked." {n}She eats.{/n} "When you want me, come down. Come alone. Uplanders who come with guards don't get to see where I sleep."''',
        c('"And Lann?"', "and_lann")),
    wd("and_lann", '''"Lann is your problem." {n}She shrugs, but it is a stiff shrug.{/n} "You told the lie. You keep it, or you don't. I'm not going to go up to him and say *surprise*. I'd like to see his face, but I'd like to keep mine more." {n}She looks at you over the rim of the pot.{/n} "He'll find out. He's slow, but he isn't stupid, and he has a nose. When he does, he'll come to you, not me. He always went to somebody else when I hurt him."''',
        c("Continue", flags=RETURN_SET)),
    wd("stay_dead", '''{n}She looks at you for a while, over the point of her knife, as if she were deciding whether to be angry. Then she laughs, softly, and puts it away.{/n}
"Stay dead." {n}She slides her knife into her belt and goes to the shutters.{/n} "All right. The dead go where they like, {name}. You'll never know where that is. That's what you bought." {n}The shutters were fastened from the inside. They are still fastened when you look. She is gone anyway.{/n}''',
        c("Continue", flags=(CLOSED, STAY_DEAD))),
], requires=("trickster.ever", KILLED, CAIRN), forbids=(RETURNED,), delay=72, chapters=(3, 5), **device("killed"))

page(W + "ch4.stone", "A stone in the pack", [
    nar("start", '''{n}Somewhere on the Midnight Isles, between one nightmare and the next, you go through your pack for a whetstone and your hand closes on something that is not one.{/n}''',
        c("Continue", "stone", requires=(RETURNED,)),
        c("Continue", "none", forbids=(RETURNED,))),
    nar("stone", '''{n}It is a flat grey stone, a little bigger than your palm, cold even here. One edge is chipped where it was levered off something heavier. Someone has scratched three lines across one face with a knife point, deep enough to feel with your thumb: the marks the neathers cut on a tunnel wall to say *this way is mine*.{/n}
{n}She put it in your pack in Drezen, the night before you left. You never saw her do it. That was, you suppose, the point: a dead woman does not say goodbye. She leaves a stone from her own grave where you will find it in the dark, and lets you work out what it means.{/n}''',
        c('[Put it back at the bottom of the pack.]', flags=(W + "stone.kept", PRIMED)),
        c('[Keep it in your pocket from now on.]', flags=(W + "stone.pocket", PRIMED))),
    nar("none", '''{n}There is nothing in there but the whetstone after all. But for a moment, in the stink of the Abyss, you smelled wet rock and old blood, and you were back in the side tunnel under Kenabres with your hands full of stones, packing the head end loose.{/n}
{n}You do not know whether she dug. The Abyss does not care. There is nobody here you can ask.{/n}''',
        c("[Go back to the whetstone.]", flags=(W + "stone.doubt", PRIMED))),
], requires=("trickster.ever", KILLED, CAIRN), delay=24, chapters=(4,), kind="memory", areas=(), **device("killed"))


# --- 4. The bid (T): outbid Savamelekh before he can buy her. -----------------------------------------------------------------

PLAN = ('''"He will call you. He has called every neather he ever fed, and his poison is in you. So go when he calls. Fight us, if he asks it. And when it's time, fall down in front of his gang where I can reach you, and stay down. Let them carry it home. Nobody sends for a corpse."''')
PLAN_TOLD = ('''{n}Savamelekh will call her; he has called every neather he ever fed, and his poison is in her. So she is to go when he calls, and fight you if he asks it, and when the time comes, fall down in front of his gang where you can reach her, and stay down, and let them carry it home. Nobody sends for a corpse.{/n}''')

inline(W + "traitor.bid", "The better offer", (3, 4), '"Let\'s talk about Savamelekh, Wenduag. Just the two of us."', [
    conv("start", '''{n}Wenduag's face does everything a loyal servant's face should do: surprise, a flicker of fear, then eager, earnest devotion. It is a beautiful performance. You watched her give it to Lann in Neathholm with the blood still wet on her side.{/n}
"Savamelekh, {mf|master|mistress}? He's nothing. A worm. I only served him because I didn't know what real strength looked like. Now I do." {n}She puts a hand on her heart.{/n} "If he ever shows his face, I'll tear it off for you."''',
        c('"Lann told me you\'d betray me the moment I turned my back. I believe him."', "lann", requires=("wenduag.lann_warned",)),
        c('"You\'re a good liar. Lie to someone who isn\'t better at it."', "liar")),
    conv("lann", '''"Lann." {n}The eager face slips, just a little, at the corner of the mouth.{/n} "Lann believes everything is exactly what it looks like. That's why he's still a boy." {n}She spreads her hands.{/n} "If you think I'll betray you, {mf|master|mistress}, why keep me? Send me away. Kill me. You had your chance in the caves."''',
        c("Continue", "offer")),
    conv("liar", '''{n}She holds the servile face for a breath too long, and then something behind it shrugs and sets it down, the way you set down a pack at the end of a march.{/n}
"Better at it." {n}Her real voice is lower, flatter, amused.{/n} "Maybe. You've been watching me eat your bread and call you master for days, and you never once believed it. I could see you not believing it." {n}She tilts her head.{/n} "So what do you want, liar? You didn't bring me out here to tell me I'm a bad girl."''',
        c("Continue", "offer")),
    conv("offer", '''{n}You tell her what Savamelekh wants, as near as you can guess it: a neather who knows the Commander's habits and tricks, standing at the Commander's back, and a knife in it at the right moment. And what he'll pay: his poison, his favour, a crown on a heap of Mongrels.{/n}
{n}She listens without a flicker, which is how you know you have guessed well.{/n}
"And what's your price, {mf|master|mistress}?" {n}She makes the word sound like an insult.{/n} "Do I get a better crown? A bigger heap?"''',
        c('"You get him. His death, at your hand. His stinger in your fist."',
          check=dict(Skill="CheckDiplomacy", DC=26, Success="yes", Failure="no")),
        c('"You get to live. That\'s more than he\'s offering, whatever he tells you."',
          check=dict(Skill="CheckIntimidate", DC=26, Success="yes_fear", Failure="no"))),
    conv("yes", '''{n}Something happens in her yellow eyes that has nothing servile in it at all. It is hunger.{/n}
"His death." {n}She says it the way other women say a lover's name.{/n} "He fed me. In the Maze. He tore a piece off a priestess and put it in my hand and I ate it and I was grateful." {n}Her lip curls back from her teeth.{/n} "Nobody feeds me and walks away. Nobody." {n}Then, sharp:{/n} "How? He'll feel me the moment I go near him. He feels everything his poison touches."''',
        c(PLAN, "plan", flags=(DEATH_PROMISED,))),
    conv("yes_fear", '''{n}She looks at you, really looks, as she has not since Neathholm: the way she looked at you over her own blood in the cave, weighing what you are.{/n}
"You'd do it, too." {n}It is not a question, and it is not fear. It is respect, which in her is worse.{/n} "He'd do it slower. But you'd do it first." {n}She wets her lips.{/n} "All right. I'm listening. What does a {mf|master|mistress} who'd do it first want with me? He'll feel me the moment I go near him; he feels all of us."''',
        c(PLAN, "plan")),
    conv("plan", '''{n}She is silent for a long while. Then she begins, very softly, to laugh.{/n}
"Die for him. So he stops sending for me." {n}Her eyes are wet with it.{/n} "Oh, that's filthy. That's the filthiest thing I've ever heard an uplander say. And after, when he thinks his best daughter bled out on his floor for him?"''',
        c('"After, you come and find me. And then we go and find him."', "after")),
    conv("after", '''"And then we go and find him." {n}She savours it.{/n} "Fine. I'll answer when he calls. I'll fight you, if he asks it; I'll even try to kill Lann, because he'll believe that. And when it's time I'll fall down where you can reach me, and I'll lie there, and you'll do the rest." {n}She leans close, close enough that you can smell her: leather, iron, and something rank underneath, his poison in her sweat.{/n} "If you're not there, {mf|master|mistress}, I'll be dead for real, and I'll come back and haunt you. Neathers don't, usually. I'd make the effort."
{n}Then she steps back, and bows, and the eager servant's face is on again as if it had never come off.{/n}''',
        c("Continue", flags=(BOUGHT, PRIMED, FALL_AGREED))),
    conv("no", '''{n}Her face does not change at all. That is the answer.{/n}
"I don't understand, {mf|master|mistress}." {n}Sweet, eager, blank.{/n} "Savamelekh is nothing to me. I only want to serve you. Please don't listen to Lann." {n}She bows.{/n} "May I go? I should practise. I want to be strong for you."
{n}She goes. You watch her go, and you know two things: that she heard every word, and that you have not bought her. Whatever Savamelekh is offering, tonight it still sounds better.{/n}''',
        c("Continue", flags=(BID_FAILED,))),
], [TRAITOR_HUB], TRAITOR_BACK, requires=("trickster", TRAITOR), forbids=(BOUGHT, BID_FAILED, FELL, KICKED))

inline(W + "exile.bid_hub", "Dismissed", (3, 4),
    '[Make the dismissal a bid] "You\'re leaving, Wenduag. Listen carefully to where you\'re going."', [
    conv("start", '''{n}The word lands on her like a slap. For an instant she forgets to be servile, and her whole face goes hard and grey as tunnel rock.{/n}
"Leaving." {n}Then she remembers, and bows lower than usual, and her voice goes sweet.{/n} "Of course, {mf|master|mistress}. Wherever you send me." {n}Her knuckles are white on her belt.{/n}''',
        c('"Savamelekh will want you back. He\'s wanted you since the Maze. Go to him."', "go")),
    conv("go", '''"Savamelekh." {n}She says it without inflection, the way a hunter says the name of an animal she has been tracking for a long time.{/n} "You're throwing me to him."''',
        c("Continue", "plan")),
    conv("plan", '''{n}You tell her how it will go, low, for her alone. She is dismissed, and she is bitter about it, and every soldier in the camp will see that she is bitter. She goes to her old patron with her pride in pieces, and he believes her, because it is true. He makes her his champion; he has always wanted one. And when you come home from whatever the war throws at you next, she brings his gang to meet you.{/n}
''' + PLAN_TOLD,
        c('"When he\'s dead, you won\'t be his. You\'ll be mine, and the neathers in Drezen will be yours to lead."',
          check=dict(Skill="CheckDiplomacy", DC=22, Success="yes", Failure="no")),
        c('"Forget it. Stay."', abort=True)),
    conv("yes", '''{n}She stares at you. Then, slowly, her lips peel back from her teeth in something that is almost a smile and almost a snarl.{/n}
"You're sending me into his house to lie to him with the truth." {n}She shakes her head.{/n} "Oh, that's cruel. That's so cruel. Every word I tell him will be real. How much I hate you. How you threw me out." {n}She breathes in, hard, through her nose.{/n} "I'll do it. I'll hate you properly, so he can smell it." {n}She steps back, and straightens, and makes her face ugly with humiliation, and raises her voice so that it carries across the whole camp.{/n}''',
        c("[Say it again, loudly, for everyone to hear.]", native_next=EXILE_CUE, flags=(BOUGHT, PRIMED, FALL_AGREED, EXILE_AGREED, DEATH_PROMISED))),
    conv("no", '''{n}She hears the words. You can see her hear them. And you can see her decide that they are the kind of thing an uplander says when he is throwing out a dog and wants to feel kind about it.{/n}
"Of course, {mf|master|mistress}." {n}She does not believe a word. Her eyes have gone flat and dry.{/n} "A plan. Very clever. I'll remember it." {n}She is not going to remember it. She is going to remember being thrown out.{/n}''',
        c("[Dismiss her anyway.]", native_next=EXILE_CUE, flags=(SCORNED,)),
        c('"Forget it. Stay."', abort=True)),
], [EXILE_LIST], EXILE_BACK, requires=("trickster",), forbids=(BOUGHT, SCORNED), EntryMythic="PlayerIsTrickster")

inline(W + "exile.bid_traitor", "You heard me", (3, 4),
    '[Make the dismissal a bid] "You heard me. Now hear the rest of it, quietly."', [
    conv("start", '''{n}She is on her knees at your feet, where she dropped, one hand reaching for your boot. At the word *quietly* the hand stops.{/n}
"The rest of it, {mf|master|mistress}?" {n}The servile whine is still in her voice, but her eyes have come up, and they are not servile at all.{/n}''',
        c("Continue", "plan")),
    conv("plan", '''{n}You keep your voice low, for her alone. You know where she will go when she leaves: to the demon who fed her in the Maze, who has been waiting for his spy to report. Let her go to him thrown out and humiliated, and let him have her. And when you come home from the Abyss, let her bring him the Commander's head, or try.{/n}
''' + PLAN_TOLD,
        c('"You were his spy. Now be mine. And when he\'s dead, the neathers in Drezen are yours."',
          check=dict(Skill="CheckDiplomacy", DC=22, Success="yes", Failure="no")),
        c('"Forget it. Get up."', abort=True)),
    conv("yes", '''{n}Wenduag stays on her knees. It is the safest place to hide a face, and she needs to hide hers: it has gone quite still with delight.{/n}
"A spy's spy." {n}The whisper barely reaches you.{/n} "Lann will be so happy to see me go. Let him be." {n}Then she lets her face fall apart, the humiliation and the bitterness, all of it real, all of it borrowed from the day before, and looks up at you with murder in her eyes for anyone who is watching.{/n}''',
        c("[Turn your back on her.]", native_next=TRAITOR_EXILE_CUE, flags=(BOUGHT, PRIMED, FALL_AGREED, EXILE_AGREED, DEATH_PROMISED))),
    conv("no", '''{n}Her eyes go flat. Whatever she hears in your voice, it is not a plan. It is a master who is tired of his dog and wants to feel clever about it.{/n}
"Yes, {mf|master|mistress}." {n}She does not believe you.{/n} "Very clever."''',
        c("[Turn your back on her anyway.]", native_next=TRAITOR_EXILE_CUE, flags=(SCORNED,)),
        c('"Forget it. Get up."', abort=True)),
], [TRAITOR_EXILE], TRAITOR_EXILE_BACK, requires=("trickster",), forbids=(BOUGHT, SCORNED), EntryMythic="PlayerIsTrickster")

page(W + "exile.champion", "Savamelekh's champion", [
    nar("start", '''{n}The camp is asleep. The Abyss is not; somewhere past the pickets a thing with too many voices is singing to itself, the way it has sung every night since you came to these islands.{/n}
{n}You wake because the singing has stopped. There is a shape crouched at the foot of your bedroll, knees up, perfectly still, and the smell of it is leather and iron and something rank and sweet underneath.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Don't shout. Your sentries are asleep, and I'd hate to make it permanent." {n}Wenduag's teeth show in the dark.{/n} "Hello, {mf|master|mistress}. I've come to report. That's what a spy does, isn't it?"
{n}She is leaner than when she left, and there are new scars on her forearms, neat and parallel, like marks on a tally stick. Her eyes have a sick yellow shine that was not in them before.{/n}''',
        c('"What has he done to you?"', "done"),
        c('"Report, then."', "report")),
    wd("done", '''"Fed me." {n}She says it with a kind of disgust that is also longing.{/n} "Every night. Meat with his poison on it. It's good, {mf|master|mistress}. You have no idea how good. It makes the whole world sharp." {n}She holds up her scarred forearm.{/n} "And when I'm too sharp, I cut. So I remember whose I am." {n}She lets the arm fall.{/n} "It isn't his."''',
        c("Continue", "report")),
    wd("report", '''"He believes me. He believed me the moment I came crawling in, because I came crawling in: I was so angry at you I could hardly see. You did that well." {n}She grins.{/n} "I'm his champion now. First of his children. He has a house here, high up, full of neathers he stole over the years, old ones, ones we thought the tunnels ate. He sits over them like a spider over flies." {n}She lowers her voice.{/n} "He's going to Drezen, when it suits him. He wants to be waiting for you when you come home, with his children around him, and me in front. He's given me the honour of your head. He was very specific: I'm to take it myself."''',
        c('"Then it\'s going as planned."', "planned")),
    wd("planned", '''"It's going as planned." {n}She rocks on her heels.{/n} "When you come home, I'll be in your street with his gang, and I'll do everything he told me, very loudly, and then I'll fall down. And you'll do the rest." {n}She leans in.{/n} "You'd better be there, {mf|master|mistress}. And you'd better kill him afterwards, like you said. With me watching. I'm not dying for him twice."''',
        c('"His stinger, in your fist. I keep my bargains."', "bargain", requires=(DEATH_PROMISED,)),
        c('"Go back before you\'re missed."', "go")),
    wd("bargain", '''"You keep your bargains." {n}She laughs silently.{/n} "You keep your bargains with the people you've already decided to keep. I watched you. That's all right. I'm one of them now." {n}She is gone between one breath and the next, and the singing past the pickets starts again as if nothing had interrupted it.{/n}''',
        c("Continue", flags=(CHAMPION, PRIMED))),
    wd("go", '''"Missed." {n}She seems to find the word funny.{/n} "Nobody misses a dog, {mf|master|mistress}. They notice when it's back." {n}She is gone between one breath and the next.{/n}''',
        c("Continue", flags=(CHAMPION, PRIMED))),
], requires=("trickster.ever", KICKED, EXILE_AGREED), forbids=(DEAD,), delay=24, chapters=(4,), areas=(), **device("exiled"))

page(W + "exile.late_bid", "A new master", [
    nar("start", '''{n}She finds you on the edge of the camp, in the thin grey hour that passes for morning on the Midnight Isles. You do not hear her come. You smell her first: leather, iron, and something rank and sweet that was never on her before.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Look at you, {mf|master|mistress}. Still alive. I was hoping to do that myself." {n}Wenduag is sitting on a rock above you with one knee drawn up, and she has never looked healthier: sleek and quick and bright-eyed, with a sick yellow shine in her eyes.{/n} "I have a new master now. The great Savamelekh. He feeds me every night. He tells me I'm his favourite." {n}She smiles.{/n} "He's given me the honour of your head. I came to have a look at it first, to make sure it's worth carrying."''',
        c('"You came a long way to gloat."', "gloat")),
    wd("gloat", '''"I came a long way because he called, and I came." {n}For a moment something moves behind the bright eyes, and is put away.{/n} "You threw me out. He took me in. That's all the explanation a neather needs." {n}She tilts her head.{/n} "Well? Aren't you going to beg? Offer me something? Uplanders always offer something when it's too late."''',
        c('"He\'ll make you his queen and keep you on a leash. I\'ll give you his head, and no leash at all."',
          check=dict(Skill="CheckDiplomacy", DC=28, Success="yes", Failure="no")),
        c('"If you walk into my city with his gang, I will kill you. You know I will. Or you can walk in with them and fall down, and live."',
          check=dict(Skill="CheckIntimidate", DC=28, Success="yes", Failure="no"))),
    wd("yes", '''{n}She stops smiling. She stays very still on her rock for a long time, and the grey light gets a little less grey.{/n}
"You're serious." {n}She looks down at her own hands, at the neat tally marks on her forearms that were not there before.{/n} "Fall down in the street, and live. And he stops sending for a dead woman." {n}Her voice is very quiet.{/n} "Do you know what his call is like? It's like hunger. It's worse. I can't stop answering it. I tried. If he thinks I'm dead, he'll stop calling me by name. The rest of it I can bear."
{n}She looks up.{/n} "If I fall down, you'll pick me up. You'll bury me yourself. You won't let your people put my head on a pole." {n}She is not asking. She is telling you what you are going to do.{/n}''',
        c('"I\'ll bury you myself. The neather way."', "deal")),
    wd("deal", '''"The neather way." {n}She laughs, a short raw sound.{/n} "What would an uplander know about the neather way?" {n}She stands.{/n} "Fine. It's a worse bargain than the one I'd have taken if you'd offered it before you threw me out. You'll pay for that, one day. But it's better than his." {n}She drops off the rock and is gone into the grey, and the sweet rank smell goes with her.{/n}''',
        c("Continue", flags=(BOUGHT, PRIMED, LATE, FALL_AGREED, EXILE_AGREED))),
    wd("no", '''{n}She laughs at you: a real laugh, delighted, from the belly.{/n}
"Oh, that's good. That's very good. You'd almost have had me, a year ago." {n}She stands on her rock, black against the grey.{/n} "But he feeds me, {mf|master|mistress}, and you threw me out. I know which of those is strength." {n}She is gone, and the smell with her, and you are left with the certainty that the next time you see her she will be trying to kill you.{/n}''',
        c("Continue", flags=(LATE_FAILED,))),
], requires=("trickster", KICKED, KICKED_LATCH), forbids=(BOUGHT, LATE_FAILED, DEAD), delay=24, chapters=(4,), areas=(),
    **device("exiled"))

inline(W + "crystal.bid", "Two masters", (4,), '"I was in Savamelekh\'s house, Wenduag. I heard everything."', [
    conv("start", '''{n}Wenduag goes very still, the way a hunting animal goes still when a branch cracks.{/n}''',
        c("Continue", "drew", requires=(DREW,)),
        c("Continue", "heard", forbids=(DREW,))),
    conv("drew", '''"I know you were. I pulled a knife on you in front of him." {n}She does not apologise. She looks at you with open, hostile curiosity.{/n} "And he took me back and told me to stay by your side and wait. And you let me. You haven't said a word since. I've been waiting for you to kill me in my sleep." {n}Her mouth twists.{/n} "Is this it? You want to do it awake?"''',
        c("Continue", "what")),
    conv("heard", '''"Everything." {n}She tests the word.{/n} "Then you heard me call you a worm. You heard me say I'd cut your throat." {n}She lifts her chin.{/n} "And you let me walk back into your camp and eat your food and sleep ten paces from you. Why?"''',
        c("Continue", "what")),
    conv("what", '''{n}She is not frightened. She is waiting, the way she waits at a trail's end for whatever comes out of the brush, knife loose in her hand.{/n}
"He's promised me the poison from his stinger. The whole of it, not the scraps he gives his children in their meat. It will make me perfect, he says. And my people will have a queen." {n}She watches your face.{/n} "Well, {mf|master|mistress}? What does the strongest thing I ever followed have to say to that?"''',
        c('"He\'s offering you his poison. I\'m offering you him. His death, at your hand, and his stinger cut off, not given."',
          check=dict(Skill="CheckDiplomacy", DC=26, Success="yes", Failure="both")),
        c('"He\'ll make you his queen on a leash. Try to take my head, and you won\'t be anybody\'s anything."',
          check=dict(Skill="CheckIntimidate", DC=26, Success="yes_fear", Failure="both")),
        c('"Nothing. You\'ll choose, when it comes to it."', "nothing")),
    conv("yes", '''{n}She draws a breath through her teeth, slow, like someone smelling meat on a fire.{/n}
"Cut off." {n}She repeats it, relishing it.{/n} "Not given. Taken." {n}Her eyes have gone bright.{/n} "He talks about my father, you know. How good his blood was. How good mine is. As if he'd made it." {n}She bares her teeth.{/n} "All right. I'll go on being his good girl. I'll stand by your side and wait for his signal like he told me. And when he gives it, I'll stab someone in the back, {mf|master|mistress}." {n}She grins.{/n} "Just not yours."''',
        c("Continue", flags=(BOUGHT, CRYSTAL_DONE, DEATH_PROMISED))),
    conv("yes_fear", '''{n}She looks at you for a long time, and for once there is no performance in it at all.{/n}
"You would, too." {n}She lets out a breath.{/n} "He talks. He promises. He's been promising neathers things for longer than there have been neathers. You don't promise. You'd just do it." {n}She nods, slowly, as if agreeing with something she has known for a while.{/n} "The strong have the right. All right. I'll wait for his signal, like a good girl. And when it comes, I'll know which one of you to stab."''',
        c("Continue", flags=(BOUGHT, CRYSTAL_DONE))),
    conv("both", '''{n}She hears you out. Then she smiles, and it is the smile of somebody who has been offered two meals and sees no reason to choose.{/n}
"That's a good offer. His was good too." {n}She stretches, easy and insolent.{/n} "I'm a neather, {mf|master|mistress}. We live because we take every chance and wait to see which one holds. When the time comes, I'll see which of you is standing, and I'll be on that side." {n}She bows.{/n} "You'd do the same. Don't pretend you wouldn't."''',
        c("Continue", flags=(BOTH, CRYSTAL_DONE))),
    conv("nothing", '''"Nothing." {n}She stares at you as if you had grown a second head.{/n} "You heard all that, and you're going to let me choose." {n}Then, slowly, she laughs.{/n} "That's either the stupidest thing I've ever heard, or you already know what I'll pick." {n}She shakes her head.{/n} "I hate it when I can't tell."''',
        c("Continue", flags=(BOTH, CRYSTAL_DONE))),
], [HUB], HUB_BACK, requires=("trickster", HEARD), forbids=(BOUGHT, CRYSTAL_DONE, NATIVE))


page(W + "exile.ch5_hunt", "Outside the walls", [
    nar("start", '''{n}Nobody has seen her since you sent her away. The gate watch saw a hooded neather go out through the south postern that night and not come back; the cellar neathers say nothing, which in the cellars means something. Somewhere out in the burnt orchards beyond the walls, a hunter who was thrown out of your service is living off hares and her own temper.{/n}
{n}If you want her back, nobody is going to bring her. You will have to go out and find her yourself, tonight, before she decides you are prey.{/n}''',
        c('[Go out through the postern alone, and read the ground the way she would.]',
          check=dict(Skill="SkillLoreNature", DC=22, Success="found", Failure="found_you")),
        c('[Go out through the postern alone, and let her find you.]', "found_you"),
        c('[Leave her to the orchards.]', abort=True)),
    nar("found", '''{n}It takes most of the night. A snare in a hedge, set low and mean, the way she sets them. A hare\'s skin pegged out on a stump to dry. The smell of a fire put out with dirt, not water. You find her at the end of it, crouched on a stone wall above a dry ditch, watching you come with a spear across her knees. She has known you were coming for an hour. She let you keep going, to see if you would.{/n}''',
        c("Continue", "her")),
    nar("found_you", '''{n}You walk the dark orchards for an hour, and then the dark walks into you: a weight on your back, a forearm across your throat, and the cold of a knife under your ear before you hear a thing. It cuts as she settles it, a short shallow line, so that you will remember it.{/n}''',
        c("Continue", "her", flags=(W + "cost.bled_outside",))),
    wd("her", '''"Look who came out of {mf|his|her} walls." {n}Wenduag\'s voice is flat and bright at once.{/n} "You threw me out. In front of everybody. And now you come out alone, at night, into my orchards, where the strong one decides." {n}She tilts her head.{/n} "Savamelekh never sent for me, after. Nobody did." {n}Her teeth show.{/n} "So. You came."''',
        c("Continue", "bought_before", requires=(BOUGHT,)),
        c("Continue", "laughed_before", requires=(LATE_FAILED,), forbids=(BOUGHT,)),
        c("Continue", "nobody", forbids=(BOUGHT, LATE_FAILED))),
    wd("bought_before", '''"You bought me once. Remember? Better than his offer, you said. And then you threw me out anyway, like a dog that bit the wrong hand." {n}Her eyes glint.{/n} "So I know what your offers are worth. Make me a new one. Make it better."''',
        c("Continue", "offer")),
    wd("laughed_before", '''"You came to me once already, in the Abyss, with an offer. I laughed at it. I went back to him." {n}Her teeth show.{/n} "He never sent for me again after that. Not once. So here I am in your orchards, laughing at nobody. Make me another offer. Make it better than the last."''',
        c("Continue", "offer")),
    wd("nobody", '''"I waited for somebody to come and make me an offer, and nobody came, and I hated you for that more than for the throwing out." {n}Her teeth show.{/n} "So. You came. What are you offering?"''',
        c("Continue", "offer")),
    nar("offer", '''{n}She waits on the wall with the spear across her knees, and the orchards wait with her.{/n}''',
        c('"Nothing. I came because I want you back. On your terms."', "terms"),
        c('"Savamelekh is still alive. Come back and hunt him with me."', "sava", forbids=(SAVA_DEAD,)),
        c('"I came to tell you that you were right, and I was wrong to throw you out."', "wrong"),
        c('"I came to tell you not to come back."', "stay_dead")),
    wd("terms", '''"My terms." {n}She considers you along the spear.{/n} "You don\'t know what you\'re saying. My terms are that I don\'t come back as your dog. I come back to the cellars, and I go out through your gate when I please, and nobody stops me, and nobody counts me on a roll, and when you want me you come down the stair, alone, like tonight." {n}She stands up on the wall.{/n} "And the first time you throw me out again, I\'ll be the one who comes looking."''',
        c("Continue", "back")),
    wd("sava", '''{n}Her whole body goes tight, like a bowstring pulled.{/n} "Alive. Out there, still calling his children." {n}She is quiet for a while.{/n} "You\'re offering me him. Not his poison. Him." {n}She grins, slow and ugly.{/n} "That\'s a better offer than the one I was waiting for. You\'re late with it. You\'ll pay for that, one day."''',
        c("Continue", "back", flags=(W + "death_promised",))),
    wd("wrong", '''{n}She stares at you as if you had spoken in a language she has only heard about.{/n} "Wrong." {n}She tastes it.{/n} "A {mf|master|mistress} who says *I was wrong* to a neather on a wall in the dark." {n}Then she laughs, and there is something unsteady in it.{/n} "That\'s either the weakest thing I\'ve ever heard or the strongest. I don\'t know which. I hate not knowing."''',
        c("Continue", "back")),
    wd("back", '''{n}She drops off the wall and lands in front of you, close, and looks at you from boots to eyes, the long measuring look she gave you the first day.{/n}
"All right. I\'ll come back. Not tonight. Tomorrow, through the postern, when your sergeant has the watch, so he can see me walk in." {n}She turns away into the dark, and then stops.{/n} "Go home, {mf|master|mistress}. You\'re out of your walls, and I\'m not the only thing out here that bites."''',
        c("Continue", flags=(RETURNED, STARTED, PRIMED, LATE))),
    wd("stay_dead", '''{n}She looks at you over the spear for a while.{/n} "Then why did you come out?" {n}She does not wait for the answer. She is gone into the orchards, and you walk back to your walls alone, and nobody at the postern asks where you have been.{/n}''',
        c("Continue", flags=(CLOSED,))),
], requires=("trickster", KICKED, KICKED_LATCH), forbids=(DEAD, STREET, RETURNED), delay=24, chapters=(5,),
   kind="event", **device("exiled"))


# --- 5. The falls (T): in Savamelekh's house (Lann's blow), and in the Drezen street. ---------------------------------------

page(W + "abyss.fall", "The best of his daughters", [
    nar("start", '''{n}You have washed his cellar's dust out of your hair twice since you left his house, and it is still in the creases of your knuckles. When you finally rest, it all comes back, in order, the way you did it.{/n}
{n}Savamelekh called her "the best of all my daughters", and she went to him. She fought beside his children in his house with his poison making her quick and terrible, and nothing you could do would put her down. Then the others lay dead, and he was gone through his own door, and she stood breathing hard in the wreck of his hall and screamed at Lann that he would never win, and went for his throat.{/n}
{n}Lann's blow took her in the side. She dropped like a cut rope.{/n}''',
        c("Continue", "bought", requires=(FALL_AGREED,)),
        c("Continue", "unbought", forbids=(FALL_AGREED,))),
    nar("bought", '''{n}She dropped exactly where she had told you she would: in front of what was left of his gang, where any of them who crawled away could carry it home. You saw her turn into Lann's blow in the last instant so that it went in low on the left side instead of the middle. Nobody else did. Lann did not. And you saw her bite down, as she fell, on the vial of healer's draught you gave her for exactly this, and swallow.{/n}
{n}He is standing over her now with blood on his hands and his face grey under the black streaks that Savamelekh's call wrung out of him, and he is not going to move until someone moves him.{/n}''',
        c('[Kneel beside her, and put yourself between him and her face.] "Go and see to the others, Lann. I\'ll take care of her."',
          check=dict(Skill="CheckBluff", DC=22, Success="alone", Failure="knows"))),
    nar("unbought", '''{n}She was trying to kill him. She would have, if he had been a heartbeat slower. There was no plan in it and nothing held back; she went down the way a hunter goes down, all at once and hard.{/n}
{n}Lann is standing over her with blood on his hands and his face grey under the black streaks Savamelekh's call wrung out of him. You go down on one knee beside her, as a Commander does after a fight, to be sure.{/n}''',
        c('[Look closely at her mouth and throat.]', check=dict(Skill="SkillPerception", DC=22, Success="breath", Failure="cough"))),
    nar("breath", '''{n}There: a bubble of blood at the corner of her lips that swells, very slowly, and shrinks. Somewhere far down she is still breathing. You have heard her say it yourself, in the Maze, the first time you met: her people's lives are short, but they are hardier than humans.{/n}
{n}Lann has not seen it. Lann is looking at his own hands.{/n}''',
        c('"She\'s gone, Lann. Go and see to the others. I\'ll take care of her."',
          check=dict(Skill="CheckBluff", DC=26, Success="alone", Failure="knows"))),
    nar("cough", '''{n}You see nothing. Then she coughs, a wet, tearing sound, and a spray of blood spatters your boot, and Lann flinches as if someone had struck him.{/n}
"She's..." {n}He does not finish it.{/n}''',
        c('"That\'s the last of it. The body does that. Go and see to the others, Lann; I\'ll take care of her."',
          check=dict(Skill="CheckBluff", DC=26, Success="alone", Failure="knows"))),
    lann("alone", '''{n}Lann looks down at her. His mouth works.{/n}
"I never wanted it to be me," he says, to nobody. "I always thought, if anyone, it would be you." {n}He wipes his hands on his coat, carefully, all the way to the wrists, and goes to see to the others, and does not look back.{/n}''',
        c("Continue", "cairn", forbids=(UNPLANNED,)),
        c("Continue", "price", requires=(UNPLANNED,))),
    nar("price", '''{n}Nobody bought this. There was no plan and no bargain: an hour ago she was trying to tear Lann's throat out for Savamelekh, and now you are on your knees in his hall choosing to bury her breathing. There is a price for deciding it here, now, with nothing prepared, and you pay it in front of everyone.{/n}
{n}Your crusaders wait at the door of his house, in the Abyss, with the Wound's sky burning over them, while their Commander builds a cairn for the traitor who tried to kill one of their own. Every one of them will tell it in every camp from here to Drezen. Not one of them will tell it kindly.{/n}''',
        c("[Build it anyway.]", "cairn", crusade=("Favors", -100))),
    lann("knows", '''{n}Lann looks from your face to hers, and you watch him understand. It happens slowly, the way ice goes on a pond.{/n}
"She's breathing." {n}His voice is flat.{/n} "You were going to let me think I'd killed her." {n}His hand goes to his knife, and stays there, and does not draw it.{/n} "She tried to rip my throat out, Commander. Just now. You saw." {n}He stares at you. Then he takes his hand off the knife.{/n} "Do what you want. You always do." {n}He walks away. He does not look back either, but it is a different kind of not looking.{/n}''',
        c("Continue", "cairn_known", forbids=(UNPLANNED,)),
        c("Continue", "price_known", requires=(UNPLANNED,))),
    nar("price_known", '''{n}Lann is gone up the stair. Your crusaders are not. They wait at the door of the demon's house, in the Abyss, under a burning sky, and they watch their Commander carry the traitor who tried to tear Lann's throat out down into the cellar, still breathing. Nobody bought this, and nothing was prepared; you are deciding it now, in front of all of them, and they will tell it in every camp from here to Drezen.{/n}''',
        c("[Build it anyway.]", "cairn_known", crusade=("Favors", -100))),
    nar("cairn", '''{n}Savamelekh's house is falling down around you: his children's blood on the floors, his hall half open to the burning sky of the Abyss. There is rubble enough for a hundred cairns. You carry her down into what was once a cellar, where the light does not reach, and lay her on the stone floor, and build.{/n}
{n}Flat pieces of his own walls, set on edge so that they roof her rather than press on her. The head end packed loose. Her knife from the floor of his hall, wiped on your knee, closed into her right hand. Above you somewhere, his gang's survivors are dragging themselves away to tell whoever is left that the Commander's crusaders killed his favourite daughter, and that she died fighting for him.{/n}
{n}Let him hear it, and stop sending for her.{/n}
{n}Before the first stone you bind her side with the dressing from your pouch and get your own draught between her teeth. Then, when it is built, you go up into the burning street and find the one thing the Midnight Isles never run short of: someone who will carry anything anywhere for money. A tiefling with a barge and no questions takes a purse from the war chest, a sketch of the cellar, and your instructions: in two nights, a woman will push her way out of a heap of stones down there. Feed her, and take her through to Drezen by whatever doors your trade uses, and there will be the same again at the other end.{/n}''',
        *cairn_close((LANN_ALONE,))),
    nar("cairn_known", '''{n}You build it anyway, in the cellar of Savamelekh's burning house, out of the pieces of his own walls: flat stones on edge, the head end loose, her knife closed into her right hand. Lann does not come to watch. He knows what you are doing, and he knows why, and he will not help you and he will not stop you.{/n}
{n}Above you, his gang's survivors are dragging themselves away to tell whoever is left that his favourite daughter died fighting for him. Let him hear it, and stop sending for her.{/n}
{n}Before the first stone you bind her side with the dressing from your pouch and get your own draught between her teeth. Then, when it is built, you go up into the burning street and find the one thing the Midnight Isles never run short of: someone who will carry anything anywhere for money. A tiefling with a barge and no questions takes a purse from the war chest, a sketch of the cellar, and your instructions: in two nights, a woman will push her way out of a heap of stones down there. Feed her, and take her through to Drezen by whatever doors your trade uses, and there will be the same again at the other end.{/n}''',
        *cairn_close((LANN_KNOWS,))),
], requires=("trickster.ever", DEAD, FELL, FELL_LATCH), forbids=(ABYSS_CAIRN,), delay=2, chapters=(4,), kind="event", areas=(),
    RequiresAnyGroups=[[FALL_AGREED, "trickster"]],   # an unprepared rescue is a live Trickster act (ledger R2-2)
    **device("abyss"))

# The abyss cairn records the cairn and the cost. A known Lann was not lied to: his cost is what he watched you do.
for _node in SCENES[-1]["Nodes"]:
    for _choice in _node["Choices"]:
        if any(f in (BARE, WATER, MARK) for f in _choice["Set"]):
            extra = [ABYSS_CAIRN, SECRET, PRIMED, PASSAGE] + ([LIED] if LANN_ALONE in _choice["Set"] else [])
            _choice["Set"] = list(dict.fromkeys(list(_choice["Set"]) + extra))
            _choice["Crusade"] = dict(Resource="Finances", Amount=-150)   # the smuggler's purse, paid from the war chest
_abyss = SCENES[-1]
_abyss_late = [c_ for n_ in _abyss["Nodes"] if n_["Id"] in ("breath", "cough") for c_ in n_["Choices"]]
for _choice in _abyss_late:
    _choice["Set"] = list(dict.fromkeys(list(_choice["Set"]) + [UNPLANNED]))

page(W + "abyss.back", "She followed his smell home", [
    nar("start", '''{n}The neathers in the cellars under the citadel send for you, which they have never done. A boy with a hare-lip and a spear taller than he is waits at the top of the stair until you come, and then leads you down without a word, past the old storerooms, past the place where the Mongrels sleep in heaps for warmth, to a cistern nobody has used in fifty years.{/n}
{n}She is sitting on the lip of the cistern with her legs dangling over the dark, eating a raw hare. She is thinner than you have ever seen her, and there is stone dust ground into every line of her face, and a pink seam in her side where Lann's blow went in.{/n}''',
        c("Continue", "her")),
    wd("her", '''"Your tiefling earned his money." {n}Wenduag does not turn round.{/n} "He was sitting on the cellar stair when I pushed the last stone off, eating an apple, with a sack of bread and a skin of wine for me and a face like a man who has seen worse things climb out of the ground. He took me through doors I won't describe to you, because you'd have nightmares, and you have enough." {n}She tears off a strip of hare.{/n} "I didn't need him for the last of it. Savamelekh came here, to your city, to call his children in your cellars. I could smell him from the Drezen side of the last door. He taught us to find him by it. He never thought about what else it could lead to."''',
        c("Continue", "lann")),
    wd("lann", '''{n}She turns, at last, and looks at you.{/n}''',
        c("Continue", "lann_alone", forbids=(LANN_KNOWS, UNPLANNED)),
        c("Continue", "lann_unbought", requires=(UNPLANNED,), forbids=(LANN_KNOWS,)),
        c("Continue", "lann_knows", requires=(LANN_KNOWS,))),
    wd("lann_unbought", '''"Little Lann hit me." {n}She says it with a kind of wonder.{/n} "I was trying to tear his throat out, and he hit me, and I went down. No plan. No bargain." {n}Her mouth twists.{/n} "I joined you to be his eyes, and when he called me in his house, I went, the way I always knew I would."''',
        c("Continue", "unbought_refused", requires=(BID_FAILED,)),
        c("Continue", "unbought_never", forbids=(BID_FAILED,))),
    wd("unbought_refused", '''"You even made me an offer, once. I laughed at it." {n}She stares at you.{/n} "And you knelt in his filth anyway and found me breathing, and lied to Lann, and built me a cairn. For a woman who had turned you down." {n}She shakes her head slowly.{/n} "I don't understand it. I've been trying all the way home. I hate not understanding things."''',
        c("Continue", "calls", forbids=(SAVA_DEAD,)),
        c("Continue", "silent", requires=(SAVA_DEAD,))),
    wd("unbought_never", '''"You never even tried to buy me. You let me walk into his house with his poison in my blood and his name in my mouth." {n}She stares at you.{/n} "And then you knelt in his filth and found me breathing, and lied to Lann, and built me a cairn anyway. For nothing." {n}She shakes her head slowly.{/n} "I don't understand it. I've been trying all the way home. I hate not understanding things."''',
        c("Continue", "calls", forbids=(SAVA_DEAD,)),
        c("Continue", "silent", requires=(SAVA_DEAD,))),
    wd("lann_alone", '''"Little Lann hit me." {n}There is something almost fond in it, and something that is not fond at all.{/n} "I turned into it, like I said I would, and he put it exactly where I needed it. I didn't think he had it in him. He thinks he killed me, doesn't he? He thinks his old friend Wendu died with his steel in her, trying to tear his throat out." {n}She licks her fingers.{/n} "Let him. It'll make a man of him. Or it'll break him. Either way it's not my problem. It's yours. You told him."''',
        c("Continue", "calls", forbids=(SAVA_DEAD,)),
        c("Continue", "silent", requires=(SAVA_DEAD,))),
    wd("lann_knows", '''"Lann knows." {n}She says it before you can.{/n} "I heard him. I was down, but I wasn't gone. *She's breathing. You were going to let me think I'd killed her.*" {n}Her imitation of his voice is merciless and exact.{/n} "And you built my cairn anyway, with him standing at the top of the stairs hating you for it." {n}She shakes her head, wondering.{/n} "Do you know what that cost you? No. You'll find out. He's the only one of them who ever liked you for nothing."''',
        c("Continue", "calls", forbids=(SAVA_DEAD,)),
        c("Continue", "silent", requires=(SAVA_DEAD,))),
    wd("calls", '''{n}She puts the hare down and wipes her knife on the stone.{/n}
"So. I died for him in his own house, and his children ran home and told him so, and he believed it. Nobody comes looking for me now." {n}She touches her temple.{/n} "He still calls, at night. It's in the blood. But he calls the way you call a dog that's dead: out of habit, not expecting it to come."''',
        c("Continue", "decide")),
    wd("silent", '''{n}She puts the hare down and wipes her knife on the stone.{/n}
"So. I died for him in his own house, and his children ran home and told him so. And while I was crawling home through his doors, somebody killed him. The cellar neathers told me, the night I came down the stair." {n}She touches her temple.{/n} "It's quiet in here. All the way down. I hate that it wasn't my hand."''',
        c("Continue", "decide")),
    wd("decide", '''{n}The knife comes up, easily, point first.{/n} "Now tell me why I shouldn't open your throat for putting me under stones. The strong have the right to decide. You decided. It's my turn."''',
        c('"Because you dug."', "dug"),
        c('"Because he isn\'t dead yet, and you want to be there when he is."', "sava", forbids=(SAVA_DEAD,)),
        c('"Because he\'s dead, and you want to be alive to spit where they burned him."', "spit", requires=(SAVA_DEAD,)),
        CLOSING_NO),
    wd("dug", '''{n}She stares at you, and then laughs until she has to hold her side.{/n}
"Because I dug." {n}The knife comes down.{/n} "Yes. You gave me stones and a knife and let me find out. The weak would have stayed under. I didn't." {n}She wipes her eyes.{/n} "You're a filthy, clever uplander and I'm going to follow you until one of us is dead for real."''',
        c("Continue", "stay")),
    wd("sava", '''{n}Her whole body goes tight, like a bowstring pulled.{/n} "He isn't dead yet." {n}She lowers the knife, slowly.{/n} "No. He isn't. And he thinks I am." {n}She sheathes it.{/n} "All right. That's a reason. I'll keep you alive for it."''',
        c("Continue", "stay")),
    wd("spit", '''{n}That surprises a laugh out of her.{/n} "Spit where they burned him." {n}She lowers the knife.{/n} "Yes. I'd like that. I'd like to stand on whatever's left of him and spit, and know he never got me back." {n}She sheathes it.{/n} "All right. That's a reason."''',
        c("Continue", "stay")),
    wd("stay", '''"I'll stay down here. I'm dead; the neathers in your cellars know how to keep a dead woman quiet, and they don't ask questions a hunter doesn't want answered." {n}She picks the hare back up.{/n} "When you want me, come down. Alone. And bring food. The dead get hungry." {n}She jerks her chin at the stair.{/n} "Your tiefling is waiting up there for the rest of his money. I told him you keep your bargains. Don't make a liar of me."''',
        c("[Pay the smuggler his balance.]", flags=RETURN_SET, crusade=("Finances", -150))),
    wd("stay_dead", '''{n}She looks at you over the point of her knife for a long time.{/n}
"Stay dead." {n}She almost smiles.{/n} "All right. I've practised." {n}She drops backwards into the dark of the cistern. You hear her land, far down, and then nothing, not even footsteps. The boy with the spear takes you back up the stair, and when you ask the neathers about her afterwards, they look at you as if you had asked about a ghost.{/n}''',
        c("Continue", flags=(CLOSED, STAY_DEAD))),
], requires=("trickster.ever", DEAD, ABYSS_CAIRN, PASSAGE), forbids=(RETURNED,), delay=48, chapters=(5,), **device("abyss"))

BRASK_PULL = dict(crusade=("Favors", -100))

page(W + "street.fall", "The traitor in the street", [
    nar("start", '''{n}By the time you rest, the street has been sluiced and the bodies carted off and the song about it is already being sung in the barracks. You go over it anyway, every step, the way you did it this morning.{/n}
{n}They were waiting for you in the lower town, in the stink of smoke and old blood, the way Savamelekh had promised: a gang of his demons, and at their head the neather who had given them everything they knew about you. She called you worm. She told them that the honour of your head was hers alone. Then they came at you, and she came with them, and the street was very loud for a while.{/n}
{n}Now it is quiet, and she is lying on her back on the cobbles among his dead with her knife still in her hand and a great deal of blood under her.{/n}''',
        c("Continue", "bought", requires=(FALL_AGREED,)),
        c("Continue", "unbought", forbids=(FALL_AGREED,))),
    nar("bought", '''{n}She fell where she told you she would, at the edge of the fight, in plain sight of the last of his demons as they broke and ran. You saw her take the blow on the side, low, and go down all at once, like a puppet with the strings cut. You also saw her tuck her chin as she fell, so that her head did not strike the stones, and bite down on the vial of healer's draught she had carried in her cheek since the morning.{/n}''',
        c("Continue", "brask")),
    nar("unbought", '''{n}She fought to kill. There was no plan in it, and no fall held back; she was trying for your throat when she went down, and she went down hard.{/n}''',
        c('[Kneel beside her, and look closely.]', check=dict(Skill="SkillPerception", DC=22, Success="breath", Failure="brask_sees"))),
    nar("breath", '''{n}A bubble of blood at the corner of her lips, swelling and shrinking, very slowly. She is still breathing. Neathers, she told you once, have short lives, but they are hardier than humans. Nobody else has seen it yet.{/n}''',
        c("Continue", "brask_late")),
    n("brask", "Sergeant Brask", '''{n}The sergeant of the south gate comes picking his way through the bodies with a dozen of his watch behind him: a big man with a red neck and a new coat, spattered now to the elbows. He looks down at her with enormous satisfaction.{/n}
"The Commander's mongrel bitch." {n}He nudges her hip with his boot.{/n} "I knew it. I told them all she'd turn. Traitor's head goes on a pole over the south gate, Commander, that's the law, and I'd take it kindly if I could be the one to put it there. I've been wanting to since the day she walked through my gate."''',
        c("Continue", "lann_there", requires=(STREET_LANN,)),
        c("Continue", "claim", forbids=(STREET_LANN,))),
    lann("lann_there", '''{n}Lann is standing a few paces off with his bow still in his hand. He has not moved since she fell. He looks at her the way you look at a house you grew up in, burning.{/n}
"Wendu," he says, very quietly, and nothing else.''',
        c("Continue", "claim_lann")),
    nar("claim", '''{n}The watch is looking at you. So is half the lower town, from its doorways. A traitor's head on the south gate is exactly what Drezen needs to see this morning, and exactly what you cannot give them.{/n}''',
        c('"She\'s mine. My kill, my prisoner, my traitor. Her people bury their own under stones, and I\'ll do it myself. Nobody touches her."',
          check=dict(Skill="CheckBluff", DC=22, Success="yields", Failure="pull_rank"))),
    nar("claim_lann", '''{n}The watch is looking at you. So is Lann. So is half the lower town, from its doorways. A traitor's head on the south gate is exactly what Drezen needs to see this morning, and exactly what you cannot give them.{/n}''',
        c('"She\'s mine. My kill, my prisoner, my traitor. Her people bury their own under stones, and I\'ll do it myself. Nobody touches her."',
          check=dict(Skill="CheckBluff", DC=22, Success="yields_lann", Failure="pull_rank_lann"))),
    n("brask_sees", "Sergeant Brask", '''{n}You see nothing, only blood. Then boots crunch on the stones beside you and the sergeant of the south gate squats down with a grunt: a big man with a red neck and a new coat, spattered to the elbows.{/n}
"Well, would you look at that." {n}He points with his dagger at the corner of her mouth, where a bubble of blood swells and shrinks.{/n} "Still breathing, the bitch. Tough as old boots, these mongrels." {n}He shifts his grip on the dagger.{/n} "Want me to finish her, Commander? Traitor's head goes on a pole over the south gate. That's the law. I'd take it kindly if I could be the one to put it there."''',
        c('"That\'s the death rattle, sergeant. Put your knife away. Her people bury their own, and I\'ll do it myself."',
          check=dict(Skill="CheckBluff", DC=26, Success="yields_late", Failure="pull_rank_hard"))),
    n("brask_late", "Sergeant Brask", '''{n}Boots crunch on the stones behind you. The sergeant of the south gate comes picking his way through the bodies: a big man with a red neck and a new coat, spattered to the elbows. He looks down at her with enormous satisfaction.{/n}
"Traitor's head goes on a pole over the south gate, Commander. That's the law. I'd take it kindly if I could be the one to put it there. I told them all she'd turn."''',
        c('"She\'s mine. My kill, my traitor. Her people bury their own under stones, and I\'ll do it myself. Nobody touches her."',
          check=dict(Skill="CheckBluff", DC=26, Success="yields_late", Failure="pull_rank_hard"))),
    n("yields_late", "Sergeant Brask", '''{n}Brask looks at your face, and at hers, and puts his knife away. He does not like it.{/n} "Your kill, Commander." {n}He spits on the stones a hand's breadth from her head.{/n}
{n}Nobody bought this; she was trying to kill you an hour ago, and you are claiming her body from your own watch with nothing prepared. That has a price, and you pay it on the spot: a cask for the gate, three days' leave for the men who saw, and your word, in front of half the lower town, that the Commander will answer for the traitor's grave. Before noon every barracks in Drezen knows what the Commander bought this morning, and for whom.{/n}''',
        c("Continue", "catacomb", crusade=("Favors", -50), forbids=(STREET_LANN,)),
        c("Continue", "lann_eyes", crusade=("Favors", -50), requires=(STREET_LANN,))),
    n("yields", "Sergeant Brask", '''{n}Brask opens his mouth, and looks at your face, and shuts it.{/n} "Your kill, Commander." {n}He does not like it. He steps back and spits on the stones, a hand's breadth from her head.{/n} "As you say. Mongrels bury mongrels."''',
        c("Continue", "catacomb")),
    n("yields_lann", "Sergeant Brask", '''{n}Brask opens his mouth, and looks at your face, and shuts it.{/n} "Your kill, Commander." {n}He steps back and spits on the stones.{/n}
{n}Lann says nothing at all. He walks over and closes her eyes with two fingers, gently, the way you close a book, and walks away down the street without looking back. He believes it. Of course he does. He has no reason not to.{/n}''',
        c("Continue", "catacomb_lann")),
    n("pull_rank", "Sergeant Brask", '''"With respect, Commander, it's the law." {n}Brask plants his feet. His men shuffle behind him.{/n} "The whole town saw her turn. They'll want to see her head."
{n}They will. You tell him, in front of his men, exactly how many of the town's soldiers you have kept alive this year and how many of his you could stop keeping alive, and what the crusade will do for the lower town's wells and granaries if you are pleased this morning. It costs you. Every word of it will be repeated in every barracks before noon.{/n}
"...Your kill, Commander," {n}Brask says at last, very stiffly.{/n}''',
        c("Continue", "catacomb", **BRASK_PULL, flags=(WATCH,))),
    n("pull_rank_lann", "Sergeant Brask", '''"With respect, Commander, it's the law." {n}Brask plants his feet. His men shuffle behind him.{/n} "The whole town saw her turn."
{n}So you buy her body from him in front of his men, with favours the lower town will count and remember. Before noon every barracks in Drezen knows the Commander paid good goodwill for a traitor's corpse.{/n}
{n}Lann says nothing at all. He closes her eyes with two fingers, gently, and walks away down the street. He believes she is dead. He has no reason not to.{/n}''',
        c("Continue", "catacomb_lann", **BRASK_PULL, flags=(WATCH,))),
    n("pull_rank_hard", "Sergeant Brask", '''"Death rattle?" {n}Brask looks at you, and at her, and at you again, and something ugly and knowing comes into his red face.{/n} "Begging your pardon, Commander, but I've heard a death rattle. That's a live woman." {n}He stands up.{/n} "A live traitor. And you want her buried quiet."
{n}He is right, and his men heard him say it. So you settle it the only way left: in front of all of them, with your rank and the crusade's goodwill in the lower town, piece by piece, until he takes his hand off his dagger. It costs you more than you like. He knows exactly what he has seen.{/n}
"...Your kill, Commander," {n}he says at last.{/n} "Mongrels bury mongrels."''',
        c("Continue", "catacomb", crusade=("Favors", -150), flags=(WATCH, BRASK_KNOWS), forbids=(STREET_LANN,)),
        c("Continue", "lann_eyes", crusade=("Favors", -150), flags=(WATCH, BRASK_KNOWS), requires=(STREET_LANN,))),
    lann("lann_eyes", '''{n}Lann has been standing a few paces off with his bow still in his hand since she fell, looking at her the way you look at a house you grew up in, burning. He did not hear what Brask said to you, or he did not understand it. He walks over and closes her eyes with two fingers, gently, the way you close a book.{/n}
"Wendu," he says, very quietly, and walks away down the street without looking back.''',
        c("Continue", "catacomb_lann")),
    nar("catacomb", '''{n}There are catacombs under the citadel, old ones, from before the demons came, where Drezen's dead lay in niches until there were too many dead to bother. You carry her down yourself. The neathers who live in the cellars above them watch you go past with their yellow eyes and say nothing at all.{/n}
{n}You build it in an empty niche at the bottom of the oldest stair, out of the fallen stones of the vault: flat pieces set on edge so that they roof her rather than press on her, the head end packed loose, her knife wiped on your knee and closed into her right hand.{/n}
{n}Before the first stone you open her shirt, pack the wound, bind it tight, and get a healer's draught between her teeth. In the dark of the vault nobody sees you do it.{/n}''',
        *cairn_close(())),
    nar("catacomb_lann", '''{n}There are catacombs under the citadel, old ones, from before the demons came. You carry her down yourself. The neathers in the cellars above watch you go past with their yellow eyes and say nothing.{/n}
{n}You build it in an empty niche at the bottom of the oldest stair: flat stones set on edge, the head end packed loose, her knife closed into her right hand. Lann does not come. Lann is somewhere up in the citadel, grieving for a woman who is breathing under your hands.{/n}
{n}Before the first stone you open her shirt, pack the wound, bind it tight, and get a healer's draught between her teeth. In the dark of the vault nobody sees you do it.{/n}''',
        *cairn_close((LIED,))),
], requires=("trickster.ever", KICKED, DEAD, STREET, STREET_LATCH), forbids=(STREET_CAIRN,), delay=2, chapters=(5,), kind="event",
    RequiresAnyGroups=[[FALL_AGREED, "trickster"]],   # an unprepared rescue is a live Trickster act (ledger R2-2)
    areas=(), **device("street"))

for _node in SCENES[-1]["Nodes"]:
    for _choice in _node["Choices"]:
        if any(f in (BARE, WATER, MARK) for f in _choice["Set"]):
            _choice["Set"] = list(dict.fromkeys(list(_choice["Set"]) + [STREET_CAIRN, SECRET, PRIMED]))
for _node in SCENES[-1]["Nodes"]:
    if _node["Id"] == "unbought":
        for _choice in _node["Choices"]:
            _choice["Set"] = list(dict.fromkeys(list(_choice["Set"]) + [UNPLANNED]))

page(W + "street.back", "Up from the catacombs", [
    nar("start", '''{n}Three nights after the street, one of the cellar neathers finds you on the citadel wall: an old woman with one eye and no teeth, who has never spoken to you. She takes your sleeve in a hand like a bundle of sticks and pulls, and does not let go until you follow.{/n}
{n}Down past the storerooms. Down past the cellars where the Mongrels sleep in heaps. Down the oldest stair into the catacombs, where the air is cold and wet and smells of lime, to the niche at the bottom where you built a cairn.{/n}
{n}The cairn has been pushed apart from the inside. The stones lie scattered across the floor. On the top step of the stair, just out of the reach of the lamplight, someone is sitting with her knees drawn up and a knife across them.{/n}''',
        c("Continue", "her")),
    wd("her", '''"I heard them singing." {n}Wenduag's voice is hoarse and cracked, as if she has been shouting for a long time.{/n} "Up there, in your city. Your soldiers, drinking. Singing about the Commander who beat Savamelekh's traitor in the street." {n}She laughs, and it turns into a cough.{/n} "I lay under your stones and listened to my own funeral. It was a bad song. The rhymes were terrible."''',
        c("Continue", "brask", requires=(BRASK_KNOWS,)),
        c("Continue", "quiet", forbids=(BRASK_KNOWS, SAVA_DEAD)),
        c("Continue", "quiet_dead", requires=(SAVA_DEAD,), forbids=(BRASK_KNOWS,))),
    wd("brask", '''"And I heard your sergeant, too, before you carried me off. *That's a live woman.*" {n}She does his accent perfectly, the flat southern vowels of the Mendevian levies.{/n} "Brask. The one with the coat. He knows. He's up there right now drinking to my death and knowing it's a lie." {n}She turns the knife over in her hands.{/n} "I'm going to have to do something about Brask."''',
        c("Continue", "quiet", forbids=(SAVA_DEAD,)),
        c("Continue", "quiet_dead", requires=(SAVA_DEAD,))),
    wd("quiet", '''{n}She stops, and tilts her head, as if listening.{/n}
"Nobody's looking for me." {n}She touches her temple.{/n} "He's still in here. Savamelekh. He calls at night; it's in the blood, he made sure of that. But he isn't calling *me* any more. His best daughter died in the street, fighting for him, and his demons ran home and told him so. You don't send for a corpse." {n}She lets her hand fall.{/n} "You were right about that much."''',
        c("Continue", "late", requires=(UNPLANNED,)),
        c("Continue", "decide", forbids=(UNPLANNED,))),
    wd("quiet_dead", '''{n}She stops, and tilts her head, as if listening.{/n}
"Nobody's looking for me. Nobody's calling, either." {n}She touches her temple.{/n} "He's dead. Savamelekh. The cellar neathers say somebody finished him while I was under your stones, and the call stopped like a gong cut off in the middle of a stroke." {n}She lets her hand fall.{/n} "It should have been my hand. I'll never forgive you for that, either. Add it to the list."''',
        c("Continue", "late", requires=(UNPLANNED,)),
        c("Continue", "decide", forbids=(UNPLANNED,))),
    wd("late", '''"You didn't buy me, though." {n}Her eyes glint in the dark.{/n} "Not before. You didn't come and find me and make me an offer. I was trying to kill you in that street, {mf|master|mistress}. I meant it." {n}She holds up the knife.{/n} "And you still knelt down in the blood and saw me breathing and lied to your own sergeant for me. For a traitor who was trying to kill you." {n}She shakes her head, slowly.{/n} "I don't understand you. I hate not understanding things."''',
        c("Continue", "decide")),
    wd("decide", '''{n}She gets to her feet, carefully, one hand on the wall.{/n} "So. Here's the thing I have to decide. You put me under stones. You chose where I'd lie and what I'd have in my hand. The strong have the right to decide who lives. You decided." {n}The knife comes up, easily, point first.{/n} "Now it's my turn. Why shouldn't I open your throat?"''',
        c('"Because you dug."', "dug"),
        c('"Because Savamelekh is still out there, and you want to be the one who ends him."', "sava", forbids=(SAVA_DEAD,)),
        c('"Because you\'re alive, and he isn\'t. That\'s all the winning there is."', "won", requires=(SAVA_DEAD,)),
        CLOSING_NO),
    wd("dug", '''{n}She stares at you, and then she laughs, a raw, delighted, painful laugh that echoes off the vault.{/n}
"Because I dug. Yes." {n}The knife drops.{/n} "Stones and a knife and the dark, and see if I'm strong enough. The weak would still be down there." {n}She wipes her mouth.{/n} "You're the only uplander I ever met who understood a thing about us. It's disgusting."''',
        c("Continue", "stay")),
    wd("sava", '''"He's still out there." {n}She goes very still.{/n} "Yes. And he thinks I'm dead. He'll never see me coming." {n}Slowly, she sheathes the knife.{/n} "All right. That's a reason. I'll keep you alive for it."''',
        c("Continue", "stay")),
    wd("won", '''{n}She looks at you for a while over the knife.{/n} "Alive, and he isn't." {n}She tastes it.{/n} "That's the creed, isn't it. That's the whole creed, and you said it better than the old ones ever did." {n}She sheathes the knife.{/n} "All right."''',
        c("Continue", "stay")),
    wd("stay", '''"I'll stay down here with the cellar neathers. They'll hide a dead woman; they've hidden worse." {n}She glances at the old one-eyed woman, who has sat down on the bottom step and appears to be asleep.{/n} "When you want me, come down. Alone. Uplanders who come with guards don't get to see where I sleep."''',
        c("Continue", flags=RETURN_SET)),
    wd("stay_dead", '''{n}She looks at you over the knife for a long while.{/n}
"Stay dead." {n}She nods.{/n} "Your city already sang the song. It would be a shame to spoil it." {n}She steps back past the lamplight, into the catacombs, and you hear her go, and then you don't. The one-eyed woman takes you back up the stair, and never speaks to you again.{/n}''',
        c("Continue", flags=(CLOSED, STAY_DEAD))),
], requires=("trickster.ever", KICKED, DEAD, STREET_CAIRN), forbids=(RETURNED,), delay=48, chapters=(5,), **device("street"))


# --- 6. Lann's trust (T): the cost, and paying it. -------------------------------------------------------------------------

LANN_GUARD = (LANN_IN,)

SCENES.append(scene(W + "lann.truth", "What Lann is owed", "Lann", 3,
    '"Walk with me, Lann. There\'s something you need to hear from me before you hear it anywhere else."', [
    lann("start", '''{n}Lann falls into step beside you, grinning, and then looks at your face and stops grinning.{/n}
"Uh-oh. That's your bad-news face. The last time I saw it we were about to walk into a room full of demons." {n}He keeps his voice light, but his shoulders have come up.{/n} "Who died?"''',
        c('"Nobody. That\'s the problem. Wenduag is alive."', "alive"),
        c('"Never mind. It can wait."', abort=True)),
    lann("alive", '''{n}He laughs. It is an automatic, polite laugh, the kind you give a joke you have not understood, and it dies halfway.{/n}
"No." {n}He looks at you.{/n} "No, she's... I saw..."''',
        c("Continue", "saw_killed", requires=(KILLED,)),
        c("Continue", "saw_abyss", requires=(ABYSS_CAIRN,), forbids=(KILLED,)),
        c("Continue", "saw_street", forbids=(KILLED, ABYSS_CAIRN))),
    lann("saw_killed", '''"I saw you do it. In the caves. I said the words over her." {n}His voice has gone thin.{/n} "I told her soul to find peace. I meant it. I stood there and meant it."''',
        c('"I turned the blade. I buried her with her knife and left the head end loose. She dug."', "how")),
    lann("saw_abyss", '''"I killed her. In his house. My own hands. I've been..." {n}He looks at his hands as if they belonged to someone else.{/n} "I've been dreaming about it every night since."''',
        c('"She turned into your blow, and I buried her with her knife and left the head end loose. She dug."', "how", requires=(FALL_AGREED,)),
        c('"Your blow didn\'t finish her. I found her breathing, and I buried her with her knife and left the head end loose. She dug."', "how", forbids=(FALL_AGREED,))),
    lann("saw_street", '''"I saw her in the street. I closed her eyes. I closed her eyes, Commander."''',
        c('"And I buried her with her knife and left the head end loose. She dug."', "how")),
    lann("how", '''{n}Lann sits down on the nearest thing, which is a water butt, and does not seem to notice that it is wet.{/n}
"Under stones. With her knife." {n}He almost laughs.{/n} "The way we bury hunters. You used the... you used our own..." {n}He puts his face in his hands, and when he takes them away he is angry, properly angry, in a way you have never seen him.{/n} "Why me? Why did I have to be the one who believed it? You could have told me. I'd have... I don't know what I'd have done. Helped. Or tried to stop you. But I'd have known."''',
        c('"You don\'t lie well, Lann. It had to be true for you, or it wasn\'t true for anyone."', "why"),
        c('"I didn\'t trust you to let her live."', "trust")),
    lann("why", '''"I don't lie well." {n}He repeats it, bitterly.{/n} "No. I don't. It's the one thing she always said was wrong with me." {n}He wipes his face.{/n} "So you used that. You used the one honest thing about me to sell her death." {n}He is quiet for a while.{/n} "And you're telling me now. Before I found out. Why?"''',
        c('"Because you\'re owed it. And because I\'d rather you hit me than find her in the cellars and think I was laughing at you."', "owed")),
    lann("trust", '''{n}That lands. You see it land.{/n} "You thought I'd kill her." {n}He stares at you.{/n} "Maybe I would've. In the caves. I don't know." {n}He looks away.{/n} "That's the worst part. You're probably right." {n}Then, after a while:{/n} "So why are you telling me now?"''',
        c('"Because you\'re owed it. And because I\'d rather you hit me than find her in the cellars and think I was laughing at you."', "owed")),
    lann("owed", '''{n}Lann stands up. For a moment you think he is going to do it. His fists are clenched. Then he lets out a long breath through his nose, and unclenches them, one finger at a time.{/n}
"I'm not going to hit you. You'd let me, and then I'd feel bad about it, and then you'd have won twice." {n}He manages something that is nearly his old grin, and isn't.{/n} "Here's what I'm owed, Commander, since you're asking. Next time you lie to me, do it to my face. Tell me you're lying, even if you can't tell me what about. So I can decide whether to believe you." {n}He looks toward the stair down to the cellars.{/n} "And don't ask me to be happy about her. I'm not. She tried to kill me, and she'll try again, and you'll be standing there. I don't know what that makes you." {n}He goes. At the corner he stops.{/n} "Thanks for telling me. I mean it. I think."''',
        c("Continue", flags=(LANN_PAID,))),
], requires=("trickster.ever", RETURNED, LIED, *LANN_GUARD), forbids=(LANN_PAID, LANN_FOUND, LANN_KNOWS, CLOSED) + LANN_GONE,
    last=5, Relationship=REL, Chapters=[3, 5], AnswerLists=[LANN_HUB], ReturnToList=True,
    ReturnText='{n}Lann is looking at the cellar stair. When he looks back at you, he does it carefully.{/n}'))
tag(W + "lann.truth", "T")

SCENES.append(scene(W + "lann.found_out", "Lann names the price", "Lann", 3, '"Something on your mind, Lann?"', [
    lann("start", '''{n}Lann is sitting on the wall with his bow across his knees, not stringing it, not doing anything with it.{/n}
"Yeah." {n}He does not look at you.{/n} "I went down to the cellars last night. To the neathers. I go sometimes; they're the closest thing to home I've got up here." {n}He runs his thumb along the bow.{/n} "One of the old women told me there's a dead hunter living down at the bottom. A woman. Eats raw hare. Nobody's supposed to say her name." {n}Now he looks at you.{/n} "I didn't need her to say it. I could smell her from the top of the stair. I grew up with that smell."''',
        c("Continue", "lied", forbids=(LANN_KNOWS,)),
        c("Continue", "knew", requires=(LANN_KNOWS,))),
    lann("lied", '''"She's alive." {n}His voice is very even, which is how you know how hard he is holding it.{/n}
"I mourned her. I lay awake working out what I should have said to her instead, back when there was still time. I'm a grown man, Commander, and I lay awake over Wendu." {n}He swallows.{/n} "And you knew. The whole time. You were standing right there and you knew."''',
        c("Continue", "price")),
    lann("knew", '''"I knew she was breathing. I told you so, standing over her. You built her a cairn anyway." {n}He shakes his head.{/n} "I've been telling myself she'd have died down there anyway. That you were just being... I don't know. Kind to a corpse. Neather-kind." {n}He laughs without humour.{/n} "And she's been down in the cellars eating hare. You let me tell myself that."''',
        c("Continue", "price")),
    lann("price", '''{n}He stands up and faces you properly.{/n}
"Here's what I'm owed. The truth. All of it. How you did it and why, and I want it from you, not from her, and not from some old woman in the cellars. I've earned that much. I've earned it a dozen times over, following you." {n}His jaw is tight.{/n} "And then I'll decide what I think of you. Not before."''',
        c('[Tell him everything: the blow, the stones, the knife, why.]', "truth"),
        c('"It\'s done, Lann. Leave it."', "refuse"),
        c('[Lie] "She crawled out on her own. I didn\'t know until she turned up."', "lie", alignment=("Evil", 1), forbids=(LANN_KNOWS,)),
        c('[Lie] "She was dying when I buried her. I didn\'t know she\'d live."', "lie_known", alignment=("Evil", 1), requires=(LANN_KNOWS,))),
    lann("truth", '''{n}So you tell him. All of it: where the blade went and why, the loose stones at the head end, the knife in her right hand, the reason you let him believe. He listens with his arms folded and his eyes on the ground, and does not interrupt once.{/n}
{n}When you have finished, he is quiet for a long time.{/n}
"Our own burial. You used our own way of burying hunters to cheat." {n}It is not quite an accusation.{/n} "She'd love that. She'd think it was the cleverest thing she ever heard." {n}He picks up his bow.{/n} "All right. I've got the truth. Late, but I've got it." {n}He looks at you.{/n} "Don't make me dig for it next time. I'm not a neather in a cairn. I shouldn't have to."''',
        c("Continue", flags=(LANN_PAID_LATE,))),
    lann("refuse", '''"Leave it." {n}He nods slowly, as if you had confirmed something he was afraid of.{/n}
"Right. Leave it. The Commander has decided, so it's decided." {n}He picks up his bow.{/n} "That's her whole creed, you know. The strong decide. I spent my whole life trying to prove there was another way." {n}He turns away.{/n} "I'll still follow you. I'm not going anywhere. But I'm going to be listening for the lies now. I never used to."''',
        c("Continue", flags=(LANN_OWED,))),
    lann("lie_known", '''{n}Lann stares at you.{/n} "You didn't know." {n}He says it flatly, the way you repeat a price you are not going to pay.{/n} "I stood at the top of that stair and told you she was breathing, and you looked at me and built the cairn with the head end loose. I've built cairns, Commander. I know what a loose head end is for." {n}He picks up his bow.{/n} "Fine. That's your story. I'll know it's a story every time you tell it. I'm still with you. I just don't believe you any more, about anything that matters."''',
        c("Continue", flags=(LANN_LIED_AGAIN, W + "lann.disbelieved"))),
    lann("lie", '''{n}He looks at you for a long time. You watch him decide whether to believe it, and you watch him decide that he does, because the alternative is too much to carry.{/n}
"On her own." {n}He lets out a breath.{/n} "Of course she did. She always did everything on her own." {n}He almost smiles.{/n} "Sorry, Commander. I thought... it doesn't matter what I thought." {n}He shoulders his bow and goes, and you are left with the knowledge that you have just lied to the most honest man in your army twice, and that the second time was easier.{/n}''',
        c("Continue", flags=(LANN_LIED_AGAIN,))),
], requires=("trickster.ever", RETURNED, *LANN_GUARD), forbids=(LANN_PAID, CLOSED) + LANN_GONE, delay=72,
    RequiresAnyGroups=[[LIED, LANN_KNOWS]], last=5, Relationship=REL, Chapters=[3, 5], AnswerLists=[LANN_HUB], ReturnToList=True,
    ReturnText='{n}Lann has gone back to his bow. He does not look up again.{/n}'))
tag(W + "lann.found_out", "T")


# --- 7. The Ledger's secret. -------------------------------------------------------------------------------------------------

household.secret(
    "wenduag_cairn", "Under stones",
    "I built a cairn for a woman who was still breathing, the way her people bury hunters, and put her own knife back in her "
    "hand. Everyone who saw her fall believes she is dead: the ones who mourned her and the ones who were glad. Lann said "
    "words over her, or struck the blow himself, or closed her eyes. If he learns it from anyone but me, I will have lied "
    "to the most honest man in my army about the one thing he could not forgive.",
    portrait="Wenduag", witnesses=("lann",), risk="high")


# --- Registration -------------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        want = list(value) if isinstance(value, list) else value
        if have is not None and have != want:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = want


def integrate(payload):
    """Register the new native reads, the latch and the Derived keys; the verified world keys (wenduag.*, lann.*, yaniel.*,
    irabeth_dead, vellexia.*, coronation.*) bind on demand in trickster_world."""
    for kind, table in BINDINGS.items():
        _bind(payload, kind, table)
    _bind(payload, "Latches", LATCHES)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    from storylines import trickster_world
    wanted = {KILLED, DEAD, KICKED, KICKED_LATCH, STREET_LATCH, TRAITOR, IN_PARTY, ROMANCE, STREET, YANIEL_FREED, YANIEL_KILLED, YANIEL_ASKED,
              LANN_IN, *LANN_GONE, "irabeth_dead"}
    for key in sorted(wanted):
        if key in trickster_world.BINDINGS and not trickster_world._bound(payload, key):
            kind, guid, _ = trickster_world.BINDINGS[key]
            payload.setdefault(kind, {})[key] = [guid] if kind in trickster_world.LIST_KINDS and isinstance(guid, str) else guid


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'wenduag.trickster.abyss.back',
    'wenduag.trickster.abyss.fall',
    'wenduag.trickster.ch4.stone',
    'wenduag.trickster.exile.champion',
    'wenduag.trickster.killed.back',
    'wenduag.trickster.killed.cairn',
    'wenduag.trickster.street.back',
    'wenduag.trickster.street.fall',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
