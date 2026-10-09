"""Iomedae on the Trickster path: "Her own bridge" (Writer/handoffs/trickster/iomedae.md, Build sheet R6; the binding plan is
11-ROSTER-PLAN-2 §2, Iomedae block, and the user's decisions of 2026-09-28: she is veiled until the finale, and the device is
her banner. The spec's Pharasma petition, Storyteller hub and fine-print joke are withdrawn; its canon table and register
stay).

Canon (blueprints.zip / enGB):
- The banner is hers from before the Starstone: "An ancient relic - the banner that Iomedae once carried into battle"
  (Items/Artefacts/VS/SworOfValorBanner 3a5ffb2f, removed from the player when it is raised over the citadel in Chapter 2,
  SwordOfValorScene/CommandAction 4 0bdfd8f3); "the Sword of Valor was Iomedae's banner before she passed the Test of the
  Starstone" (TrueEnding/Suggest/Cue_0025 9ce46e4f); "Such artifacts are almost like living creatures... It seems to see
  something kindred in you" (FakeYaniel_ToAreelu/Cue_0013); it changed under the Commander's blood (Herald Cue_0080 77e2e9cb).
- At Iz it is put back in the Commander's hands (c5/Iz/Banner/Cue_0011 1a0b602d), or lost (Cue_0014 710ed961), and on this
  path a sock may fly in its place (Cue_0071 445c1729, TricksterBanner b99cec06).
- Her mortal legend: "turned her cloak into a bridge... and even talked some undead into throwing himself upon his sword"
  (Nenio Cue_0215 cdbc3902); "The Acts of Iomedae": "...the sixth of her eleven feats of greatness" (ActsOfIomedae 75b3f367).
- Her law and her truth: "Gods must not interfere directly in the affairs of mortals" (Goddesses_Summit/Cue_0016 2e46d7fc);
  "the one who closes the Worldwound will die along with it!" (Cue_0045 909f6c75); "At first, I did not know who you were...
  Until that point, I had observed you without intervening" (Cue_0087 16c4d5d6); "I am no demon - I do not lie and cheat"
  (Cue_0026); "I do not blame them, I blame myself" (Cue_0093); the Trickster's power "can break the laws of reality itself.
  It is dangerous." (Cue_0101); her bow at the Wound, "I bow my head before your bravery" (GrandFinal/Cue_0085 7d25dae9).

So the courtship keeps canon's order: before the Summit she only observes. What reaches the Commander in Chapter 3 is the
banner's memory of the woman who carried it (labelled on the page as a relic's memory, never her message), and her herald,
who prays the Commander's questions and gets no answer. After the herald's dying prayer and the Summit she knows who the
Commander is, and from then on she answers, still veiled: in dreams, and through her banner. She appears in person only at
Threshold, and after.

Device ("Her own bridge", a labelled wager): the Commander carries her banner into the Wound in imitation of her mortal
cloak-bridge. At Threshold she chooses whether to answer it. Nothing obliges her; no mythic power, no document, no raise.
Commit: a formal disputation (thesis, objections, answers); her yes is conceding the argument aloud.
Cost: the Commander stays buried to the world (their own concession in the disputation) and owes her a miracle she chose to
grant; Drezen loses the Sword of Valor to the Wound. Fallback, when the banner was lost at Iz: the cathedral's processional
banner of the Inheritor, bearing her sign (a cheaper imitation), got by an oath or by theft; that bridge costs the banner hand.

Path fit (ROUTE-BRIEF-R, v1): every scene is T. She is veiled on every other path (user decision); v2 may give Angel a
reverence thread without romance (spec, Build sheet B8).
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
REL = "iomedae"
E = "iomedae.trickster."

DREZEN = "2570015799edf594daf2f076f2f975d8"            # DrezenCapital: the citadel, its banner platform, the cathedral
IOMEDAE_UNIT = "9a1443603c9353d4194a583a31228c8b"      # Units/NPC/Unique/.../Goddesses_Summit/Iomedae (the Summit speaker)
PORTRAIT_GUID = "438135f5553f4a0cb5635c5ac2caaeea"     # Units/Portraits/Player/IomedaeGoddessFemale_Portrait (her unit's)
SUMMIT_LIST = "7f18896facfbd614c96e2e4ea2d6c0d5"       # Goddesses_Summit/AnswersList_0136 (keep the power or not; E14b)
FINAL_LISTS = ["294126e3264796e488ce19bfb1851355",     # c6/SecondFloor/GrandFinal/AnswersList_0005 (the final decision)
               "16994192cfa484744bd10852b8dc806f"]     # GrandFinal/AnswersList_0127 (after her bow, Cue_0085)
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"        # CompanionDialogues/Seelah/AnswersList_0003
SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"        # CompanionDialogues/Sosiel/AnswersList_0002
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"        # CompanionDialogues/Daeran/AnswersList_0003

STARTED = "iomedae.started"
CLOSED = "iomedae.closed"
COMMITTED = "iomedae.committed"

# Native reads (B2). SeenCues only: no etude is bound, so the etude lifecycle is untouched.
BANNER_HELD = "iomedae.banner_in_hand"         # c5/Iz/Banner/Cue_0011: "Your banner... is back in your hands."
BANNER_LOST = "iz.banner_lost"                 # c5/Iz/Banner/Cue_0014: the empty flagpole
SOCK = "iz.sock_raised"                        # TricksterBanner: the Sock of Valor flies in its place
IZ_DONE = "iz.done"
KEY_DIES = "iomedae.key_dies_revealed"         # Goddesses_Summit/Cue_0045
KEY_LATCH = "iomedae.key_dies_revealed.latched"
REPROACHED = "iomedae.reproached"              # Goddesses_Summit/Cue_0422: the Trickster ultimate drove Drezen mad
WITNESSED = "iomedae.witnessed_sacrifice"      # GrandFinal/Cue_0085: she bowed
COERCED = "iomedae.sacrifice_coerced"          # GrandFinal/Answer_0026 [Submit]
HERALD_SAVED = "iomedae.herald_saved"          # LabyrinthOfBaphometh/Herald/Cue_0021: his heart given back
HERALD_FELL = "iomedae.herald_fell"            # the same dialog: he died there (Cue_0020, Cue_0026)
HERALD_HEAVEN = "iomedae.herald_heaven"        # Herald/Cue_0028: he chooses Heaven
HERALD_EXILED = "iomedae.herald_exiled"        # Herald/Cue_0031: he leaves in exile
HERALD_SPITE = "iomedae.herald_spite"          # Herald/Answer_0006: deliberate execution
HERALD_ACCOUNTED = E + "herald_accounted"      # owns cruelty; no invented absolution
PERSONAL = E + "personal_exchange"            # completed questions, never a war-talk tally
POSTPONED = E + "concession.postponed"
EVE_PERSONAL = E + "eve.reason"
HERALD_FOUGHT = "iomedae.herald_fought"        # the same dialog: he chose the fight (Cue_0011, Cue_0012, Cue_0017)
NENIO = "iomedae.nenio_acts"                   # Nenio/Cue_0215: "turned her cloak into a bridge"
QUEEN_SAW = "iomedae.queen_saw_banner"         # GalfreyArrives/Cue_0052: "...only to discover that it was no longer her banner"
SILENCED = "iomedae.silenced_nocticula"        # NocticulaThreshold/Cue_0022: "Enough, Nocticula. You have lost the battle for this mortal soul"
SIGHED = "iomedae.threshold_sigh"             # NocticulaThreshold/Cue_0028: "...a noise like a soft sigh. Is that Iomedae?"
SACRIFICE = "sacrifice"
WOUND_CLOSED = "ending.wound_closed"
BACK = "trickster.commander_back"
H2 = "lastcall.h2"
ACTIVE = "lastcall.active"

# The route (authored flags; every scene id is also a flag once played).
DREAM_BANNER = E + "dream.banner"              # scene: the banner's first memory (Chapter 3)
SENT_AWAY = E + "sent_away"                    # the Commander moved out from under the banner (also sets the ClosedFlag)
QUESTION_SENT = E + "question_sent"            # the herald prays the Commander's question
ASKED_WHOSE = E + "asked.whose"
ASKED_MIND = E + "asked.mind"
ASKED_BACK = E + "asked.back"
HERALD_ANSWERED = E + "herald_answered"        # the herald reports: no answer; she observes
BRIDGE_SEEN = E + "bridge_seen"                # the chasm memory: the cloak laid across the gorge
TESTED = E + "tested"                          # the slip sealed in the socket of the pole
WORD_ARODEN = E + "test.aroden"
WORD_LIAR = E + "test.liar"
WORD_PLEASE = E + "test.please"
TEST_DONE = E + "test_answered"                # the memory never said the word
SLIP_BURNED = E + "slip_burned"
BRIDGE_TOLD = E + "bridge_told"                # the herald told the Acts, in the Abyss
DREAMS_TOLD = E + "dreams_told"                # ... and was told about the dreams
ABYSS_SILENCE = E + "abyss_silence"
SUMMIT_ASKED = E + "summit_asked"              # at the Summit: "did you ask anyone's leave?" "No."
PLAN = E + "plan.wager"                        # the wager conceived on the bare platform
HERALD_DREAM = E + "herald_dream"
SPOKEN = E + "first_spoken"                    # she has spoken to the Commander herself (after the Summit)
IZ_NIGHT = E + "iz_night"
CALLED = E + "disputation.called"
ORDER_BANNER = E + "order_banner"              # the fallback: the cathedral's banner of the Inheritor
COST_OATH = E + "cost.oath_sworn"
COST_STOLEN = E + "cost.banner_stolen"
DISPUTED = E + "disputed"
DECLINED = E + "declined"
COST_BOASTED = E + "cost.boasted"
COST_BURIED = E + "cost.buried_to_the_world"
COST_LIED = E + "cost.lied"
COST_MOCKED = E + "cost.madness_mocked"
ARGUED_OLD = E + "argued.old_form"
ARGUED_PLAIN = E + "argued.plain"
OWNED_MADNESS = E + "answered.madness"
OWNED_THEFT = E + "answered.theft"
MORTAL_SEEN = E + "mortal_seen"
EVE_SEEN = E + "eve_seen"
CARRIED = E + "banner_carried"                 # the device act at Threshold (the Commander's; answering is hers)
CONCEDED_AT_WOUND = E + "conceded_at_wound"
KISSED_AT_WOUND = E + "kissed_at_wound"
RESCUE_ONLY = E + "rescue_only"               # she conceded the argument at the Wound, and nothing else
ARGUMENT_ONLY = E + "argument_only"           # the disputation held; the Commander took the argument and declined the rest
DEAD_TO_WORLD = E + "dead_to_world"           # Derived: the world buried the Commander (her bridge, or Last Call's empty coffin)
VERDICT = E + "afterlogue.verdict_heard"      # the E14e line in Pharasma's court was shown
APPEALS = (E + "afterlogue.appeal_mercy", E + "afterlogue.appeal_iomedae", E + "afterlogue.appeal_justice",
           E + "afterlogue.appeal_balance")   # SelectedAnswers: the Commander intervened at Areelu's trial (Cue_26's own condition)
PHARASMA_UNIT = "db064cafc234498ca83a702c472c1a7b"
APPEAL_ANSWERS = ("dfe36dafa2aa423badcfc58845521a30", "b310f96f6a3149f1ad439d5cfe285f25", "c8e8d245e469495fa43bc3cefbb759b9",
                  "52eeccb144a04ff79650f08eacff9a17")  # afterlogue Answer_0023/0025/0024/0028
VERDICT_CUE = "b4602032fbbd4c4c9c04493f5fe6ddcb"  # Epilogues_afterlogues/Cue_26: "You have earned your peace."
VERDICT_PARENTS = ["da7646b4ce8e4e658ee92aa02877ec17", "abafa9f923204d5a96cb13bec9ab7771", "d7c1d87165af414ebffbd4f50151af49",
                   "9377e7d23348467ab12a3de0a94246fc", "f8b124e1f6584f54a9a3f80e85973a0c"]  # Cue_0017/0018/0019/12/19, Continue First
COURTED = E + "courted"                       # Derived: her completed personal exchange, or the postponed eve exchange
FALSE_FACE = E + "false_face_seen"             # Chapter 4: something in Alushinyrra wore her face in a dream
STUDIED = E + "canons_studied"               # the cathedral's canons read before the disputation (Lore DC 20, not 24)
AFTER_ROAD = E + "after.road"                 # the respondent's question: what the Commander will do with the life left
AFTER_NEAR = E + "after.near"
AFTER_WAR = E + "after.war"
AFTER_OPEN = E + "after.open"
POWER_ANSWERED = E + "answered.power"         # "the power in you... can break the laws of reality" (Cue_0101), answered

# Derived (B5).
BRIDGE_KNOWN = E + "bridge_known"
KEPT = "iomedae.appointment_kept"              # the bridge world (ledger rows 6 and 16): she answered
RESCUED = E + "rescued"                       # she answered the banner for the argument alone (no romance)
BURIED_ALIVE = E + "buried_alive"             # either: the Commander lives, dead to the world
MIRACLE = E + "cost.miracle_owed"
LATE_COMMITTED = E + "late_committed"

RELATIONSHIP = dict(
    Title="Her Own Bridge",
    Description=("The Sword of Valor was hers before it was mine, before she was a goddess. It remembers her. Lately it has "
                 "been showing me what it remembers, and I have not been able to stop looking."),
    Objective="Carry her banner where it is needed",
    Guidance=("On the Trickster path, sleep under the Sword of Valor in Drezen and ask her herald what the banner remembers. "
              "After the goddess has come to Drezen, hold her banner again, raise it where it flew and argue your case. "
              "At the Wound, before the final choice, unfurl it."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[], FailureFlags=[], UnavailableOverrides={},
)

SEEN_CUES = {
    BANNER_HELD: ["1a0b602da28e56f4badf9406964e4244"],
    HERALD_SAVED: ["55ab2d8561d68ad4aae145e4798b43d4"],
    HERALD_HEAVEN: ["6a9482523b5ac1646823a4866485f0ab"],
    HERALD_EXILED: ["58565f5d678283e4b94874f5a07bdbc2"],
    HERALD_FELL: ["c241ccdbc3b178b41b7161d17ff43b17", "1f0fef1fbc666cc42a213671d6b171a2"],
    HERALD_FOUGHT: ["4a056226dce658f4da30d99d851537ec", "7dbd09bed7138984c994631e35722a4e", "9d391c75a04e30946aee2fa377d65ede"],
    NENIO: ["cdbc3902b0a3ea742b44922dedeee61b"],
    QUEEN_SAW: ["d383267ee2a7b8141835f106f40bf28e"],
    SILENCED: ["05c37f9556af62c4ba275d57afdc91a8"],
    SIGHED: ["900c45dc39736cf4487017e2b096e107"],
}
DERIVED = {
    BRIDGE_KNOWN: [[BRIDGE_SEEN], [BRIDGE_TOLD], [NENIO], [SUMMIT_ASKED]],
    # The bridge world: the Commander closed the Wound with the banner carried, and she had conceded. She answered.
    KEPT: [[SACRIFICE, WOUND_CLOSED, "trickster.ever", CARRIED, COMMITTED]],
    RESCUED: [[SACRIFICE, WOUND_CLOSED, "trickster.ever", CARRIED, RESCUE_ONLY]],
    BURIED_ALIVE: [[KEPT], [RESCUED]],
    DEAD_TO_WORLD: [[KEPT], [RESCUED], ["lastcall.dead_on_record"]],
    COURTED: [[PERSONAL], [POSTPONED, EVE_PERSONAL]],
    MIRACLE: [[KEPT], [RESCUED]],
    # No late romance: eligibility, the Table and Last Call read a concession she actually made.
    LATE_COMMITTED: [["trickster.ever", COMMITTED]],
    # 05 §2.5 voice note: she comes when her war allows, and she does not compete for the hours.
    "iomedae.harem.voice.duty_first": [[COMMITTED]],
}

# Path fit (ROUTE-BRIEF-R 2026-09-29, v1): T = device or Trickster-only; N-all = any path; N-fit = the fitting paths.
PATH_FIT = {}


def tag(scene_id, fit="T"):
    PATH_FIT[scene_id] = fit


def io(id, text, *choices, **kw):
    """Iomedae on a rest-delivered page (her portrait)."""
    return n(id, "Iomedae", text, *choices, portrait="Iomedae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def remote(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="sending", drezen=False, last=None,
           owner="Iomedae", **extra):
    """A rest-delivered page of her route. drezen=True: only at a rest in the capital (the platform, the cathedral)."""
    chapters = tuple(chapters)
    SCENES.append(scene(id, title, owner, min(chapters), "", nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, *forbids), delay=delay, last=last or max(chapters), optional=True,
                        Relationship=REL, Remote=True, Kind=kind, Chapters=list(chapters),
                        **(dict(Areas=[DREZEN]) if drezen else {}), **extra))
    tag(id)


# --- Her answer to the word in the socket (read wherever she first speaks through a banner). --------------------------------

def word_nodes(prefix, then):
    """The payoff of the Chapter 3 test: she read the word, and did not answer, because she was observing."""
    return [
        io(prefix + "aroden", '''"You wrote my god's name in the foot of my banner, to see whether it would sting." {n}A pause.{/n} "It did. I did not answer. I was observing, and I will not break my own rule to win a test set by a Trickster with a candle."''',
           c("Continue", prefix + "burned", requires=(SLIP_BURNED,)), c("Continue", then, forbids=(SLIP_BURNED,))),
        io(prefix + "liar", '''"You wrote 'Liar' on a strip of paper and pushed it into the foot of my banner." {n}There is no heat in it; there is something drier than heat.{/n} "I read it. I did not answer. I was observing, and I do not break a rule to win an argument with a strip of paper."''',
           c("Continue", prefix + "burned", requires=(SLIP_BURNED,)), c("Continue", then, forbids=(SLIP_BURNED,))),
        io(prefix + "please", '''"You wrote 'Please' in the foot of my banner and sealed it with your thumb." {n}The voice is quieter.{/n} "I read it. I did not answer; I was observing. I have thought about that word more often than a goddess ought to think about anything written in wax."''',
           c("Continue", prefix + "burned", requires=(SLIP_BURNED,)), c("Continue", then, forbids=(SLIP_BURNED,))),
        io(prefix + "burned", '''"And then you dug it out with a knife and burned it in a candle, as though that would unwrite it. I had already read it, Commander. Burning a thing only tells me you wish you had not written it."''',
           c("Continue", then)),
    ]


def word_gate(prefix, then):
    """Continue choices into the word payoff (or straight on, if the Commander never set the test)."""
    return (c("Continue", prefix + "aroden", requires=(WORD_ARODEN,)),
            c("Continue", prefix + "liar", requires=(WORD_LIAR,)),
            c("Continue", prefix + "please", requires=(TESTED,), forbids=(WORD_ARODEN, WORD_LIAR)),
            c("Continue", then, forbids=(TESTED,)))


# --- Chapter 5, after Iz: the banner in hand, and her voice in it. The disputation is called. -------------------------------

CALL = (
    c('"I\'m going to carry it into the Wound."', "plan"),
    c('"Will you answer it, if I do?"', "plan"),
)

remote(E + "iz.night", "Back in your hands", [
    nar("start", '''{n}At your rest, the recovered Sword of Valor leans where you set it, its cloth still stiff with blood. You look at it for a while, then put your hand against the staff. The war has left few quiet moments for this.{/n}''',
        c('"You can stop observing now. I know you\'re there."', "stirs"),
        c('"She isn\'t going to answer. You\'re a flag."', "stirs"),
        c("[Say nothing. Put your hand on the staff.]", "stirs")),
    nar("stirs", '''{n}The cloth moves against your hand. There is no wind.{/n}''',
        c("Continue", "first", forbids=(SPOKEN,)),
        c("Continue", "again", requires=(SPOKEN,))),
    io("first", '''"Commander." {n}Her voice comes from the cloth, exact and pitched for you alone.{/n} "My herald's dying prayer told me what had been done to you. Until then, I watched without intervening." {n}The cloth settles.{/n} "The Queen carried my banner to Iz. You brought it back. I have something to say to you."''',
       *word_gate("first.", "plan_q")),
    io("again", '''"Commander. You are holding my banner again." {n}The voice is the one from the white dream: older, exact, pitched for you alone.{/n} "The Queen carried it to Iz and left it in a camp. She meant well. Many people who have lost my banner meant well."''',
       *word_gate("again.", "plan_q")),
    *word_nodes("first.", "plan_q"),
    *word_nodes("again.", "plan_q"),
    io("plan_q", '''"You have my banner in your hands. Tell me what you mean to do with it." {n}The cloth hangs still.{/n}''',
       *CALL),
    io("plan", '''"I know what you intend. Raise my banner where it flew, and bring the case there. You propose; I object; you answer. Do not lie. Flattery will not help you either." {n}Her voice carries like an order.{/n} "I will hear you on the platform."''',
       c('"A disputation."', "form"),
       c('"And if I win?"', "win")),
    io("form", '''"A disputation. You have heard of them, I think, in the way you have heard of most things that require patience."''',
       c('"I\'ll be there."', flags=(IZ_NIGHT, CALLED, SPOKEN))),
    io("win", '''"Then I will say so, aloud. That is what winning a disputation means. It does not mean that I will do anything."''',
       c('"I\'ll be there."', flags=(IZ_NIGHT, CALLED, SPOKEN))),
], requires=(STARTED, BANNER_HELD, BRIDGE_KNOWN, KEY_LATCH), forbids=(IZ_NIGHT,), delay=0, chapters=(5,))


# --- Chapter 5, the fallback: the banner was lost at Iz. The cathedral's banner of the Inheritor, by oath or by theft. -------

OATH = E + "oath"

remote(E + "order.banner", "A banner of her order", [
    nar("start", '''{n}The Sword of Valor is gone. You saw its empty pole at Iz, among the dead who tried to hold it, and whatever the demons wanted it for, they have it now.{/n}''',
        c("Continue", "sock", requires=(SOCK,)),
        c("Continue", "cathedral", forbids=(SOCK,))),
    nar("sock", '''{n}Over the citadel of Drezen, in its place, flies a sock. Your sock. You were very pleased with it at the time, and the city has taken it to its heart, and a sock is not going to carry anyone anywhere.{/n}''',
        c("Continue", "cathedral")),
    nar("cathedral", '''{n}The cathedral of Drezen, whose great window the goddess stepped out of on the day of the Summit, keeps a processional banner of the Inheritor on a stand beside the altar: good white cloth with her sign worked on it in gold thread, carried through the streets on her feast days. It is not a relic. It has been nowhere but this church and the street outside. It is hers only in the way every banner of her order is hers.{/n}
{n}It will have to do. It is a worse bridge than the one she carried, and you know it, and you are going to ask anyway.{/n}
{n}The canon who keeps the altar is an old man with a soldier's shoulders gone soft. He hears you out without interrupting.{/n}''',
        c("Continue", "canon")),
    n("canon", "Canon of the cathedral", '''"You want to borrow the Inheritor's banner." {n}He looks from you to the banner and back.{/n} "It is not lent, Commander. It is carried, by those sworn to her, where she would have it go." {n}A pause.{/n} "Where would she have it go?"''',
      c('[Tell him the truth] "Into the Worldwound."', "truth"),
      c('"Somewhere it will be seen."', "vague")),
    n("vague", "Canon of the cathedral", '''"Everywhere it goes, it is seen. That is the point of a banner." {n}He does not smile.{/n} "I asked where."''',
      c('[Tell him the truth] "Into the Worldwound."', "truth")),
    n("truth", "Canon of the cathedral", '''{n}The old man is silent. Then he goes to the altar rail and kneels at it, stiffly, knee by knee, and stays there for as long as it takes to say whatever he says. When he gets up he does not look at you.{/n}
"Then swear for it. On her sign, in the old form, as a knight of her order swears. A Trickster's oath, on the Inheritor's sign." {n}His mouth twists.{/n} "I will have to hear it to believe it."''',
      c("[Swear on her sign.]", "swear"),
      c("[Thank him, and come back tonight to take it.]", "night")),
    nar("night", '''{n}Past midnight the cathedral is dark but for the lamp over the altar. The banner stands on its stand where it stood by day. Between it and you are forty feet of floor that echoes, a sacristan asleep in the choir stalls, and a door with a bolt that was put on after the last time somebody tried this.{/n}''',
      c("[Thievery] Lift it.", check=dict(Skill="SkillThievery", DC=22, Success="stolen", Failure="caught", CommanderOnly=True))),
    nar("stolen", '''{n}The bolt gives to a bent nail. The floor, walked on the sides of your feet along the wall, echoes nothing. The banner comes off its stand with a sigh of cloth, and you have it wound round its staff and under your coat before the lamp has finished guttering. The sacristan sleeps on. In the morning the canon will find the empty stand, and know exactly who, and have no way to prove it.{/n}''',
      c("Continue", "raise", flags=(ORDER_BANNER, COST_STOLEN))),
    nar("caught", '''{n}The bolt gives. The floor does not. Your third step rings off the vault like a dropped pan, and the sacristan in the choir is not asleep after all; he is the canon, in a blanket, with a lantern he has been keeping shuttered on his knee.{/n}''',
      c("Continue", "caught2")),
    n("caught2", "Canon of the cathedral", '''"I thought you might." {n}He opens the lantern. He does not call the watch.{/n} "Thieves have been stealing from her house since before there was a house. She has never once sent them to me for punishment. She sends them to me to finish what they started honestly."
"Swear, then. Here, now, with your hand still on it. Then take it, and nobody will ever say you stole it, because you will not have."''',
      c("[Swear on her sign.]", "swear")),
    nar("swear", '''{n}He sets her sign in your hand. It is heavier than it looks.{/n}
{n}He gives you the words, and you say them after him, in the old form: to carry her banner where it is needed, and not bring it back for your own glory; to answer for what is done under it; to lie to no one while it is in your keeping. They are not words you would have chosen. You find, once they are in your mouth, that you mean them, which is worse.{/n}
"Well sworn," {n}says the canon, grudgingly, like a man paying a debt he had hoped to dispute.{/n} "Take it. And if she does not want it where you are taking it, she will let you know."''',
      c("Continue", "raise", flags=(ORDER_BANNER, COST_OATH), alignment=("Lawful", 1))),
    nar("raise", '''{n}That night you climb to the platform of the citadel.{/n}''',
      c("Continue", "raise_sock", requires=(SOCK,)),
      c("Continue", "raise_bare", forbids=(SOCK,))),
    nar("raise_sock", '''{n}You haul down the Sock of Valor, which comes down reluctantly and heavy with rain, and fold it, because it seems to deserve that much. Then you run the cathedral's banner up the pole in its place. The white cloth takes the wind off the Wound and stands out square and gold-stitched over the city, and looks, you have to admit, a good deal more like the right idea.{/n}''',
      c("Continue", "voice")),
    nar("raise_bare", '''{n}You run the cathedral's banner up the bare pole. The white cloth takes the wind off the Wound and stands out square and gold-stitched over the city, where the Sword of Valor used to fly.{/n}''',
      c("Continue", "voice")),
    nar("voice", '''{n}The cloth stirs against the wind, not with it.{/n}''',
      c("Continue", "o.first", forbids=(SPOKEN,)),
      c("Continue", "o.again", requires=(SPOKEN,))),
    io("o.first", '''"That is not my banner." {n}Her voice reaches you and no one on the walls.{/n} "It bears my sign. Until my herald's dying prayer, I watched without intervening. Now you have brought this cloth to my banner's pole. I will hear what you have to say."''',
      *word_gate("of.", "o.judge")),
    io("o.again", '''"That is not my banner." {n}The voice from the white dream, older and exact.{/n} "It bears my sign. It has been carried in far more processions than battles."''',
      *word_gate("oa.", "o.judge")),
    *word_nodes("of.", "o.judge"),
    *word_nodes("oa.", "o.judge"),
    io("o.judge", '''"Mine was lost at Iz, in the camp where the Queen left it."''',
       c("Continue", "o.sock", requires=(SOCK,)),
       c("Continue", "o.how", forbids=(SOCK,))),
    io("o.sock", '''"And then you flew a stocking over my crusade." {n}A pause.{/n} "I noticed."''',
       c("Continue", "o.how")),
    io("o.how", '''"And now you have brought me my own church's banner, and I know how you came by it."''',
       c("Continue", "o.stolen", requires=(COST_STOLEN,)),
       c("Continue", "o.sworn", requires=(COST_OATH,))),
    io("o.stolen", '''"You stole it from my house. I will remember that." {n}The cloth stills.{/n} "You have raised my sign here. I will hear your case tomorrow night. I have not excused the theft."''',
       c('"I\'ll be here."', flags=(CALLED, SPOKEN))),
    io("o.sworn", '''"You swore for it on my sign, in the old form. I heard every word." {n}Something moves in the voice.{/n} "A Trickster's oath. I did not think I would live to hear one. Tomorrow night, here, I will hear you out. Bring that oath with you."''',
       c('"I\'ll be here."', flags=(CALLED, SPOKEN))),
], requires=("trickster", STARTED, IZ_DONE, BRIDGE_KNOWN, KEY_LATCH), forbids=(BANNER_HELD, ORDER_BANNER), delay=12, chapters=(5,),
    kind="visit", drezen=True, RequiresAnyGroups=[[BANNER_LOST, SOCK]])


# --- Chapter 5, optional preparation: the canons (an earned option; the disputation's Lore check drops from DC 24 to 20). ---

remote(E + "canons", "The canons", [
    nar("start", '''{n}The cathedral of Drezen keeps its books in a long room over the south aisle, up a stair so narrow that anyone climbing it has time to reconsider. Most of the books burned when the city fell. What is left has been brought back from Nerosyan a crate at a time, and smells of the road.{/n}
{n}You have a disputation to win, against the one person in the world who cannot be lied to, on a subject she has had longer to think about than your city has stood. It seems reasonable to read something first.{/n}''',
        c("Continue", "canon_known", requires=(ORDER_BANNER,)),
        c("Continue", "canon_new", forbids=(ORDER_BANNER,))),
    n("canon_known", "Canon of the cathedral", '''{n}The old canon who keeps the altar is at a reading desk with a lamp. He looks up, sees who it is, and looks down again at his page with the expression of a man who has decided to be patient because the alternative is a sin.{/n}
"You have her banner. Now you want her books." {n}He turns a page.{/n} "What else of hers will you be needing, Commander? The candlesticks?"''',
      c('"The rules of a disputation. I\'ve been called to one."', "rules"),
      c('"Just the books. I\'ll bring the candlesticks back."', "rules")),
    n("canon_new", "Canon of the cathedral", '''{n}An old canon with a soldier's shoulders gone soft is at a reading desk with a lamp. He looks up at the Knight Commander in his library at an hour when Knight Commanders are asleep or drunk, and does not seem to think either would have been an improvement.{/n}
"You want something," {n}he says.{/n} "People only climb that stair when they want something."''',
      c('"The rules of a disputation. I\'ve been called to one."', "rules")),
    n("rules", "Canon of the cathedral", '''"Called." {n}He sets down his pen.{/n} "By whom?"''',
      c("[Tell him.]", "told"),
      c('"Somebody who doesn\'t lose many."', "vague")),
    n("vague", "Canon of the cathedral", '''"Then you will lose." {n}He says it without malice, as a man says it will rain.{/n} "But you may lose well, which in a disputation is worth something. Sit down."''',
      c("Continue", "lesson")),
    n("told", "Canon of the cathedral", '''{n}He does not say anything at all. He looks at you for as long as it takes the lamp to gutter and steady. Then he gets up, goes to the far end of the room, and comes back with a book bound in boards so old the leather has gone to horn.{/n}
"The canons of her church were written by people arguing with her," {n}he says,{/n} "which is to say, by people losing to her. Sit down. You have a great deal to learn and, I suspect, very little time."''',
      c("Continue", "lesson")),
    n("lesson", "Canon of the cathedral", '''{n}He teaches the way old soldiers teach recruits, without flattery. The proposition is stated once and not amended. Each objection is answered in turn, and an objection left unanswered is conceded. Never claim more than you can prove; she will make you prove it. Never appeal to feeling; she will grant the feeling and deny the point.{/n}
"And the dead," {n}he says, tapping a page.{/n} "If your case touches the dead, you will have the Lady of Graves in the room whether you invite her or not. The canons are clear: what Pharasma has received, no one takes. What she has not yet received is not hers. Learn the difference. Learn to say it in fewer than ten words."''',
      c('"And if I win?"', "win"),
      c('"And if I lie?"', "lie")),
    n("win", "Canon of the cathedral", '''"Then she will say so aloud, and it will be the only thing anyone remembers about you, including you." {n}He closes the book and pushes it across the desk.{/n} "Take it. Bring it back. If you do not, I will know where to look for it."''',
      c("[Take the book, and read it through the night.]", flags=(STUDIED,))),
    n("lie", "Canon of the cathedral", '''"Then it ends, and you will have been the kind of fool the canons have a word for, and the word is not kind." {n}He closes the book and pushes it across the desk.{/n} "Read it. All of it. The part about lying is short, because it does not need to be long."''',
      c("[Take the book, and read it through the night.]", flags=(STUDIED,))),
], requires=(STARTED, CALLED), forbids=(STUDIED, DISPUTED), delay=0, chapters=(5,), kind="visit", drezen=True)


# --- Chapter 5: the disputation (the commit). Her yes is conceding the argument aloud. ---------------------------------------

LORE = dict(Skill="SkillLoreReligion", DC=24, Success="old_form", Failure="tangled", CommanderOnly=True)
LORE_STUDIED = dict(Skill="SkillLoreReligion", DC=20, Success="old_form", Failure="tangled", CommanderOnly=True)
PROPOSE = (
    c('[State it in the old form] "I propose that the key may carry your banner into the lock; and that you may answer it, and break no law of yours in doing so."', "obj1"),
    c('[State it plainly] "I\'m going into the Wound with your banner, and I\'m betting you\'ll answer it the way you answered your cloak. Tell me why you won\'t."', "obj1"),
)
ANSWER1 = (
    c('"It is a wager. I can lose it. You may not answer, and then I die in the lock the way the witch built me to. The dying is real either way. All I\'ve arranged is a chance."', "obj1_ok"),
    c('"It isn\'t a wager. You\'ll answer. I know you. It\'s a sure thing."', "refuse"),
)
ANSWER2 = (
    c('"Then the world gets its death. The Commander of the Fifth Crusade dies in the Wound: no crown, no command, no name. Whatever walks back across your banner is nobody the world ever has to meet."', "obj2_ok", flags=(COST_BURIED,)),
    c('"The world won\'t notice the difference."', "notice"),
    c('"I\'ll step down afterwards. Somebody else can have the crown."', "step_down"),
)
ANSWER3 = (
    c("[Lore (Religion)] Put it to her in the old form, the way the canons put it.", check=LORE_STUDIED, requires=(STUDIED,)),
    c("[Lore (Religion)] Put it to her in the old form.", check=LORE, forbids=(STUDIED,)),
    c('"I don\'t know the canons. I know you did it once."', "plain"),
    c('"Break the rule. You\'re a goddess."', "break"),
)
AFTER3 = (
    c("Continue", "madness", requires=(REPROACHED,)),
    c("Continue", "theft", requires=(COST_STOLEN,), forbids=(REPROACHED,)),
    c("Continue", "concede", forbids=(REPROACHED, COST_STOLEN)),
)
DECIDED = (DISPUTED, COMMITTED)

remote(E + "disputation", "Disputation", [
    nar("start", '''{n}Midnight on the platform of the citadel. You sent the sentries down an hour ago with orders to hear nothing, and they went with the faces of men who intend to hear everything.{/n}''',
        c("Continue", "sword", requires=(BANNER_HELD,)),
        c("Continue", "order", forbids=(BANNER_HELD,))),
    nar("sword", '''{n}The Sword of Valor flies over Drezen again, cleaned of Iz as well as you could clean it, cracking in the wind off the Wound. You raised it yourself at dusk, where the Queen took it down, where you first raised it with your blood on it.{/n}''',
        c("Continue", "open")),
    nar("order", '''{n}The cathedral's white banner flies over Drezen where the Sword of Valor used to, its gold thread catching the torchlight from the walls, snapping in the wind off the Wound. It is a lesser thing. It is what you have.{/n}''',
        c("Continue", "open")),
    nar("open", '''{n}A disputation is opened by the one who calls it. You have read enough, since Iz, to know that much; you have not had time to learn much more.{/n}''',
        c('[Open it properly] "I call the Inheritor to disputation."', "arrive"),
        c('[Open it your way] "It\'s up. You\'re called. Let\'s argue."', "arrive")),
    nar("arrive", '''{n}You do not see her; you were told you would not. But the banner's shadow lies across the stones at your feet in the shape of a woman standing, although the torches are behind the banner and its shadow falls the wrong way, and the voice comes out of the shadow.{/n}''',
        c("Continue", "called")),
    io("called", '''"I am called, and I am here." {n}The voice has the flat, carrying precision of a court.{/n} "The respondent will object. The proponent will answer. The proponent will not lie. State your proposition."''',
       *PROPOSE),
    io("obj1", '''"First objection. A sacrifice that has arranged its way back is not a sacrifice. It is a wager, and a wager on a death is a kind of theft: you would take the price the world pays for its heroes, and keep the goods."''',
       *ANSWER1,
       c('"Then call it theft. I\'m a Trickster. What did you expect?"', "shrug")),
    io("shrug", '''"I expected an answer. That was a shrug."''',
       *ANSWER1),
    io("obj1_ok", '''{n}The shadow is still.{/n} "The point stands. I will not object that you are gambling. I object to what you are gambling with."''',
       c("Continue", "obj2")),
    io("obj2", '''"Second objection. The world is owed what it has been promised. Drezen has buried you once already. It will bury you again, and mean it this time, and build on your grave. If you walk back out of the Wound and take up your crown, you have sold the world a death and delivered it a hero on horseback."''',
       *ANSWER2),
    io("notice", '''"I will."''',
       ANSWER2[0]),
    io("step_down", '''"Stepping down is not dying. The world was promised a grave, not a resignation."''',
       ANSWER2[0]),
    io("obj2_ok", '''"Then you give up more than your life. You give up the use of it." {n}The voice slows, as if she were reading a clause back to be certain of it.{/n} "You would let Drezen mourn you, and walk past your own grave, and never be thanked for any of it. Never command again. Never be known by the people you saved."''',
       c('"Yes."', "obj_power"),
       c('"I\'ve been thanked. It\'s overrated."', "obj_power")),
    io("obj_power", '''"The power in you can break the laws of reality. How am I to know you will not go into the lock and joke your way out, then call it my miracle?"''',
       c('"Because I won\'t use it. That\'s the point. What the witch put in me goes into the seam; that\'s what a lock is for. I\'m walking in with a flag. If I come out, you carried me. If I cheat, you\'ll know, and you won\'t have."', "power_ok", flags=(POWER_ANSWERED,)),
       c('"You don\'t know. You\'ll have to trust me."', "power_trust"),
       c('[Trickster] "If I meant to cheat you, I wouldn\'t have told you where I was going."', "power_trick", mythic="Trickster")),
    io("power_trust", '''"I asked what you will do with that power. Answer me."''',
       c('"Then here\'s the answer. I won\'t use it. What the witch put in me goes into the seam; I\'m walking in with a flag. If I come out, you carried me. If I cheat, you\'ll know, and you won\'t have."', "power_ok", flags=(POWER_ANSWERED,))),
    io("power_trick", '''"That is true." {n}The shadow tilts.{/n} "It is also the most Trickster thing you have said tonight, and I find it persuasive, which I resent. Granted, narrowly. Do not make me regret the narrowness."''',
       c("Continue", "obj3", flags=(POWER_ANSWERED,))),
    io("power_ok", '''"Then the power burns in the lock, as it was built to, and whatever walks out is only you." {n}The voice is very level.{/n} "Granted. I will hold you to it."''',
       c("Continue", "obj3")),
    io("obj3", '''"Third objection. Gods must not interfere directly in mortal affairs. Nor are the dead mine. When the lock takes the key, its soul goes to the Lady of Graves. I will not take from Pharasma what the Wound gives her."''',
       *ANSWER3),
    io("break", '''"No." {n}Just that, and then, because she is scrupulous:{/n} "Try again."''',
       *ANSWER3[:3]),
    io("old_form", '''{n}You give it to her the way the canons would: a banner is not an affair of mortals, but hers, from before she was a god, so to answer it is to keep faith with her own act, not to meddle in yours; and the Lady of Graves loses nothing, because a soul that walks back across before the lock closes on it was never hers to collect. Nobody dies who comes back over.{/n}
{n}The shadow is quiet.{/n} "That is a canon lawyer's argument, Commander."''',
       c('"Is it a bad one?"', "good")),
    io("good", '''"No. It is a good one. I dislike it for that reason." {n}A pause.{/n} "Granted. The Lady of Graves will notice nonetheless. If she has anything to say about it, I will answer to her myself. That is mine to carry, not yours."''',
       c("Continue", "after3", flags=(E + "argued.old_form",))),
    io("tangled", '''{n}You tangle it. You cite a council you have half heard of, and a canon that turns out, when she asks you which, not to say what you said it says.{/n}
"That is not the canon, Commander."''',
       c('"No. It isn\'t. I don\'t know the canons."', "plain")),
    io("plain", '''{n}You tell her what you do know: that she did it once, for people who were going to die anyway, with no one's leave; that you are asking her to do it once more; that if you are already dead when she gets there, you are the Lady of Graves', and she takes nothing from anybody.{/n}
"That is not theology." {n}The shadow tilts, a little, the way a head tilts.{/n} "It is an honest {mf|man's|woman's} wager. It will do. Granted." {n}A pause.{/n} "The Lady of Graves will notice nonetheless. If she has anything to say about it, I will answer to her myself. That is mine to carry, not yours."''',
       c("Continue", "after3", flags=(E + "argued.plain",))),
    nar("after3", '''{n}The banner cracks over your head. Below, on the walls, a sentry who was ordered to hear nothing coughs, and is shushed.{/n}''',
        *AFTER3),
    io("madness", '''"There is another answer owed. Your victory cost your followers their minds. Some have not recovered. Answer for them before asking me for anything."''',
       c('[Own it] "I did it. It won, and it cost people their minds, and some of them haven\'t come back. I\'d think hard before I did it again. I won\'t pretend it was nothing."', "madness_ok", flags=(OWNED_MADNESS,)),
       c('[Joke] "They were due a holiday."', "mocked")),
    io("madness_ok", '''"No. It was not nothing." {n}The shadow does not soften, but it does not withdraw.{/n} "It is answered. It is not forgiven; it is not mine to forgive. It is answered."''',
       c("Continue", "theft", requires=(COST_STOLEN,)),
       c("Continue", "concede", forbids=(COST_STOLEN,))),
    io("theft", '''"And the banner you raised tonight to call me, you stole from my own house."''',
       c('"I did. I\'d do it again, and I\'d tell you so."', "concede", flags=(OWNED_THEFT,)),
       c('[Lie] "I borrowed it. The canon said I could."', "lied")),
    io("concede", '''{n}The banner snaps overhead. The shadow remains beside you.{/n} "The respondent has heard the proposition and the answers. The Inheritor concedes the argument."''',
       c('"That\'s all?"', "privilege"),
       c("[Wait.]", "privilege")),
    io("privilege", '''"Not yet. The respondent has one question, by right, when she concedes." {n}The shadow on the stones has not moved, but it seems nearer.{/n} "If I answer my banner, and you walk back across it, and the world keeps its grave: what will you do with the life that is left?"''',
       c('"Walk. There are roads in Mendev nobody\'s ever walked for the pleasure of it."', "other", requires=(COURTED,), flags=(AFTER_ROAD,)),
       c('"Stay near Drezen. Somebody should watch it who doesn\'t need thanking."', "other", requires=(COURTED,), flags=(AFTER_NEAR,)),
       c('"Go where you\'re fighting. You\'ll need somebody who doesn\'t mind losing arguments."', "other", requires=(COURTED,), flags=(AFTER_WAR,)),
       c('"I don\'t know. I\'ve never had a life I didn\'t owe somebody."', "other", requires=(COURTED,), flags=(AFTER_OPEN,)),
       c("[Leave the personal question for another night.]", "concession.postponed", forbids=(COURTED,))),
    io("other", '''{n}The banner cracks overhead. Her voice loses its court pitch.{/n} "The questions I brought to you in private were not for the crusade. I wanted your answers. I want more than that now." {n}Her shadow reaches the staff beneath your hand.{/n} "That is my answer, not part of the proposition."''',
       c('"Will you answer it, at the Wound?"', "will"),
       c('"I\'ve wanted you since the rain."', "rain", requires=(DREAM_BANNER,)),
       c('"I\'ve wanted you since the square."', "square_want", forbids=(DREAM_BANNER,)),
       c("[Put your hand on the staff.]", "staff"),
       c('"Then I\'ll take the argument, and leave the other thing where you set it down. You have a war. I won\'t make you carry me as well."', "argument_only")),
    io("argument_only", '''{n}The shadow on the stones goes still. When she speaks the formality is back in every syllable, and you have the impression that she put it on the way a knight puts a helm on: quickly, and because something needed covering.{/n}
"Noted." {n}A pause.{/n} "The argument stands. What I conceded after it stands as well; I do not take a thing back because it was declined. You will have the banner at the Wound, and I will decide there whether to answer it, as I would have decided in any case."
{n}Another pause, shorter.{/n} "That was courteously done. I had not expected courtesy from you." {n}She does not say what she means to do with it.{/n}''',
       c("[Stay until the torches burn down, and say nothing more.]", flags=(DISPUTED, ARGUMENT_ONLY))),
    io("square_want", '''"Since the square." {n}Something in the voice might, in a mortal woman, have been a laugh held behind the teeth.{/n} "I told you in front of a demon lord that you were going to die, and that was when. You have poor taste, Commander." {n}A pause.{/n} "So, it seems, have I."''',
       c("[Stay on the platform until the torches burn down.]", "torches")),
    io("will", '''"I conceded that I may. I did not say that I will." {n}The voice does not waver.{/n} "You will learn it at the Wound, when I do. I will not promise you a miracle to make you braver. You are brave enough, and it would be a lie, because I have not decided."''',
       c('"Then I\'ll see you at the Wound."', "torches")),
    io("rain", '''"Since the rain." {n}Something in the voice might, in a mortal woman, have been a laugh held behind the teeth.{/n} "A banner's memory of a tired girl in the mud. You have poor taste, Commander." {n}A pause.{/n} "So, it seems, have I."''',
       c("[Stay on the platform until the torches burn down.]", "torches")),
    io("staff", '''{n}Something passes down the staff under your palm, warm, like a hand closing over yours from above.{/n}
"Yes," {n}she says,{/n} "there."''',
       c("[Stay until the torches burn down.]", "torches")),
    nar("torches", '''{n}You stay while the torches burn down. Her shadow remains close to the staff, and once her voice answers a small remark you had not thought she would hear. Below you, the watch changes. Neither of you moves to end the night.{/n}''',
        c("[Go down, and let the city talk.]", flags=DECIDED)),
    io("refuse", '''{n}The shadow goes still in a different way.{/n}
"A sure thing." {n}She repeats it the way one repeats a sum that has come out wrong.{/n} "Then it is not a sacrifice. It is a transaction."
"I bow my head to sacrifices, Commander. I do not bow to bargains. If you mean it, show me at the Wound."''',
       c("[Let her go.]", flags=(DISPUTED, DECLINED, COST_BOASTED))),
    io("mocked", '''"A holiday." {n}The shadow on the stones is suddenly only a shadow, falling the right way.{/n} {n}From very far off:{/n} "Then we are finished here. I will be at the Wound. If you have anything better to say by then, say it there."''',
       c("[Stand alone under the banner.]", flags=(DISPUTED, DECLINED, COST_MOCKED))),
    io("lied", '''"I do not lie, Commander, and I know when I am lied to. I told you what would happen." {n}The shadow on the stones is suddenly only a shadow, falling the right way.{/n} {n}From very far off:{/n} "I will be at the Wound. Bring the truth, if you have any left."''',
       c("[Stand alone under the banner.]", flags=(DISPUTED, DECLINED, COST_LIED))),
    io("concession.postponed", '''"The argument stands. The rest does not follow from it." {n}The shadow draws back from the staff.{/n} "You have asked whether I may save you. You have not told me why you want me beside you afterwards. We may speak of that another night."''',
       c("[Leave the banner raised.]", flags=(DISPUTED, ARGUMENT_ONLY, POSTPONED))),
], requires=(STARTED, BRIDGE_KNOWN, CALLED, IZ_DONE), forbids=(COMMITTED, DECLINED, ARGUMENT_ONLY, HERALD_SPITE), delay=24, chapters=(5,), drezen=True,
    ForbidOverrides={HERALD_SPITE: HERALD_ACCOUNTED})


# --- Chapter 6, Threshold: the device act (E14b on the final lists; no clean return cue fits). -------------------------------
# She is unveiled here. The native Answer_0017 / Answer_0035 stay the sacrifice; whether she answers is hers.

THRESHOLD_RETURN = "{n}The banner stands at the lip of the Wound, stretched flat toward the rift by the hot wind. The Worldwound waits.{/n}"
def state(extra=()):
    return (c("Continue", "committed", requires=(COMMITTED,), forbids=tuple(extra)),
            c("Continue", "declined", requires=(DECLINED,), forbids=(COMMITTED, *extra)),
            c("Continue", "unargued", forbids=(COMMITTED, DECLINED, ARGUMENT_ONLY, *extra)),
            c("Continue", "argued", requires=(ARGUMENT_ONLY,), forbids=(COMMITTED, DECLINED, *extra)))


HALL = (c("Continue", "silenced", requires=(SILENCED,)),
        c("Continue", "sighed", requires=(SIGHED,), forbids=(SILENCED,)),
        *state((SILENCED, SIGHED)))
STATE = state()
GO = (CARRIED,)

# Only a present witness speaks; neither cameo is needed to carry the banner.
_NOCT_WITNESS = "crossroute.nocticula.available"
_AREELU_WITNESS = "crossroute.areelu.available"
_WITNESSES = tuple(dict(answer, Forbids=[*answer.get("Forbids", []), _NOCT_WITNESS, _AREELU_WITNESS]) for answer in HALL) + (
    c("Continue", "nocticula_objection", requires=(_NOCT_WITNESS,)),
    c("Continue", "areelu_objection", requires=(_AREELU_WITNESS,), forbids=(_NOCT_WITNESS,)),
)

SCENES.append(scene(E + "threshold.banner", "Her own bridge", "Iomedae", 6,
    '[Unfurl the banner] "Before anyone goes in: I\'m carrying something."', [
    nar("plant", '''{n}You drive the staff into the scorched rock at the edge, where the ground is hot through your boots, and let the cloth go. The wind out of the Wound takes it at once and stretches it flat toward the rift, the way the wind in the gorge once stretched a cloak.{/n}''',
        c("Continue", "here", requires=(WITNESSED,)),
        c("Continue", "comes", forbids=(WITNESSED,)),
        c("[Furl it again. Not yet.]", abort=True)),
    nar("comes", '''{n}The light at the edge changes. It does not brighten; it steadies, the way light does in a church when the doors swing shut behind you. Iomedae stands beside her banner at the lip of the Worldwound, in her own shape, and you are looking at her, not at her shadow on the stones.{/n}
{n}She plants her feet beside the staff. The cloth strains toward the fire between you.{/n}''',
        *_WITNESSES),
    nar("here", '''{n}She has only just bowed her head to you. She lifts it when she sees what is in your hand, and for the space of a breath the goddess of valour looks at her banner at the edge of the Wound as a woman looks at a letter in her own hand that she does not remember sending.{/n}
"The Lady in Shadow wanted you in there for her reasons," {n}says Iomedae.{/n} "Go in for yours."''',
        *_WITNESSES),
    nar("silenced", '''{n}Before the ascent, in the hall below, she silenced the Lady in Shadow for you with one sentence: you have lost the battle for this mortal soul. She does not mention it now. Neither do you. It is enough that you both remember who was in the hall.{/n}''',
        *STATE),
    nar("sighed", '''{n}Before the ascent, in the hall below, when the Lady in Shadow's voice had faded, something lingered there and sighed. You did not know then whose sigh it was. You know now.{/n}''',
        *STATE),
    nar("committed", '''"The argument stands," {n}says Iomedae.{/n} "I conceded it, and I do not take back what I have said aloud." {n}The violet fire of the Wound is in her eyes. It does not seem to trouble her.{/n} "I have not decided. I told you I would decide here. I am deciding."''',
        c('"Then decide quickly. I\'m going in."', "go"),
        c("[Kiss her.]", "kiss"),
        c('"If you don\'t, it was still worth it."', "worth"),
        c('"The Lady in Shadow wanted me in there. So did the witch. Doesn\'t that bother you?"', "wanted")),
    nar("wanted", '''"It bothers me that they will say afterwards that they were right." {n}She does not look toward either of them, wherever they are.{/n} "Let them. The lock does not care who wanted you in it. I care who you went in for." {n}She steps back half a pace from the edge, beside her banner, and waits.{/n}''',
        c("[Turn to the Wound.]", flags=GO)),
    nar("go", '''{n}She nods, once, the way a commander nods to a runner who has his orders and does not need them repeated. Her eyes go to the staff in the rock, and to your hand, and back to your face, as if she were memorizing the order they come in. Then she steps back half a pace from the edge, beside her banner, and waits.{/n}''',
        c("[Turn to the Wound.]", flags=GO)),
    nar("kiss", '''{n}Her armoured hand closes at the back of your neck. She kisses you hard, holding you against her while the Wound's heat beats on your face. When she releases you her hand stays for one breath longer.{/n}''',
        c("[Turn to the Wound.]", flags=GO + (KISSED_AT_WOUND,))),
    nar("worth", '''"I know." {n}She says it quietly, as she said the bow.{/n} "That is why I am still deciding, and not decided." {n}She steps back half a pace, beside her banner, and waits.{/n}''',
        c("[Turn to the Wound.]", flags=GO)),
    nar("declined", '''{n}She walked off your roof, the last time you argued. She has not forgotten why, and she does not pretend to.{/n}''',
        c("Continue", "d_boast", requires=(COST_BOASTED,)),
        c("Continue", "d_mock", requires=(COST_MOCKED,), forbids=(COST_BOASTED,)),
        c("Continue", "d_lie", forbids=(COST_BOASTED, COST_MOCKED))),
    nar("d_mock", '''"You called Drezen's madness a holiday, on my roof, under my banner," {n}says Iomedae. She does not raise her voice at the edge of the Wound. She does not need to.{/n} "Answer for it now. Not to me. To them."''',
        c('[Own it] "I did it. It won, and it cost them their minds, and some never came back. I owe them more than a joke. I\'m going in anyway, and it isn\'t a sure thing."', "u_check", flags=(OWNED_MADNESS,)),
        c('[Make a joke of it] "They\'re still on holiday."', "turned")),
    nar("d_lie", '''"You lied to me about my own house," {n}says Iomedae. She does not raise her voice at the edge of the Wound. She does not need to.{/n} "Tell me the truth now, at the edge, where it costs you something."''',
        c('[The truth] "I stole it. The canon never said I could. I\'m going in anyway, and it isn\'t a sure thing."', "u_check", flags=(OWNED_THEFT,)),
        c('[Hold to the lie] "Borrowed. I told you."', "turned")),
    nar("d_boast", '''"You told me it was a sure thing," {n}says Iomedae. She does not raise her voice at the edge of the Wound. She does not need to.{/n} "Is it?"''',
        c('[The truth] "No. It isn\'t. I\'m going anyway."', "u_check"),
        c('[Make a joke of it] "Sure as anything."', "turned")),
    nar("unargued", '''"You have not made your case," {n}says Iomedae.{/n} "Make it here. Briefly. The Wound is waiting."''',
        c('"I might die in there. You might not answer. The world gets its grave either way: the Commander dies in the Wound and stays dead. I\'m asking anyway."', "u_check"),
        c('"It\'s a sure thing. You\'ll answer."', "refused")),
    nar("u_check", '''{n}She studies your face without answering. The banner strains toward the rift.{/n}''',
        c("Continue", "u_madness", requires=(REPROACHED,), forbids=(OWNED_MADNESS,)),
        c("Continue", "u_theft", requires=(COST_STOLEN,), forbids=(OWNED_THEFT, REPROACHED)),
        c("Continue", "u_theft", requires=(COST_STOLEN, OWNED_MADNESS), forbids=(OWNED_THEFT,)),
        c("Continue", "conceded", forbids=(REPROACHED, COST_STOLEN)),
        c("Continue", "conceded", requires=(OWNED_MADNESS,), forbids=(COST_STOLEN,)),
        c("Continue", "conceded", requires=(OWNED_THEFT,), forbids=(REPROACHED,)),
        c("Continue", "conceded", requires=(OWNED_MADNESS, OWNED_THEFT))),
    nar("u_madness", '''"Your victory cost your followers their minds," {n}says Iomedae.{/n} "Some have not recovered. Answer for them before you ask me for anything."''',
        c('[Own it] "I did it. It won, and it cost people their minds, and some of them haven\'t come back. I won\'t pretend it was nothing."', "u_after_m", flags=(OWNED_MADNESS,)),
        c('[Joke] "They were due a holiday."', "turned")),
    nar("u_after_m", '''"It was not nothing." {n}She does not soften.{/n} "It is answered. It is not forgiven; it is not mine to forgive."''',
        c("Continue", "u_theft", requires=(COST_STOLEN,), forbids=(OWNED_THEFT,)),
        c("Continue", "conceded", forbids=(COST_STOLEN,)),
        c("Continue", "conceded", requires=(OWNED_THEFT,))),
    nar("u_theft", '''"And the banner in the rock beside you came out of my own house," {n}says Iomedae.{/n} "You did not ask for it. Say so."''',
        c('[The truth] "I stole it. I\'d do it again, and I\'m telling you so."', "conceded", flags=(OWNED_THEFT,)),
        c('[Lie] "I borrowed it. The canon said I could."', "turned")),
    nar("conceded", '''{n}Iomedae looks at you for one breath of the Wound's hot wind.{/n} "Then the Inheritor concedes the argument. Aloud, at the edge, where anyone may hear." {n}Her voice does not change, but her hand comes to rest on the staff of her banner, beside yours.{/n} "And the world keeps its grave."''',
        c('"It keeps it."', "boast", requires=(COST_BOASTED,)),
        c('"It keeps it."', "other_q", forbids=(COST_BOASTED,))),
    nar("other_q", '''"That is the argument," {n}says Iomedae.{/n} "It is all I have conceded."''',
        c('"And the other thing? The one we never argued."', "other_yes", requires=(COURTED,)),
        c('"And the other thing? The one we never argued."', "other_no", forbids=(COURTED,)),
        c('"That\'s all I need."', "rescue")),
    nar("other_yes", '''{n}She looks directly at you while the fire leans toward her banner.{/n} "I chose to come to you in private. I wanted to hear you when neither of us was giving orders. I want you still." {n}Her hand closes beside yours on the staff.{/n} "That answer is mine."''',
        c("Continue", "decide")),
    nar("other_no", '''"I have heard your case. That is not the same as knowing you." {n}Her hand stays on the banner.{/n} "I may answer this without giving you the answer you want about me."''',
        c("Continue", "rescue")),
    nar("rescue", '''"I have not decided whether I will answer your banner when you call from inside the fire. I will decide that when you are in it, and not before." {n}She steps back half a pace, beside her banner, and waits.{/n}''',
        c("[Turn to the Wound.]", flags=GO + (RESCUE_ONLY, COST_BURIED))),
    nar("boast", '''"You called it a sure thing. Now you stand at the fire and admit that it is not." {n}Her hand stays on the staff.{/n} "I accept the correction. Keep it when you turn toward the Wound."''',
        c("Continue", "other_q")),
    nar("decide", '''"What I have said to you stands, and I do not take it back." {n}Her hand stays on the staff.{/n} "What I have not decided is whether I will answer your banner when you call from inside the fire. I will decide that when you are in it, and not before." {n}She steps back half a pace, beside her banner, and waits.{/n}''',
        c("[Turn to the Wound.]", flags=GO + (COMMITTED, CONCEDED_AT_WOUND, COST_BURIED))),
    nar("argued", '''"The argument stands," {n}says Iomedae.{/n} "I conceded it on your roof. You left the personal question there." {n}The fire leans toward her banner.{/n} "I have not decided whether I will answer your banner when you call from inside the fire. I will decide that when you are in it."''',
        c("[Turn to the Wound.]", flags=GO + (RESCUE_ONLY, COST_BURIED)),
        c('"I set it down on the roof. I\'d like to pick it up again, here, if you\'ll let me."', "other_yes", requires=(COURTED,)),
        c("[Leave it at the argument.]", "rescue", forbids=(COURTED,))),
    nar("turned", '''"Then go." {n}She turns her face toward the rift, and away from you.{/n} "I have nothing more to say to you."''',
        c("[Leave the banner where it stands.]", flags=GO + (CLOSED,))),
    nar("refused", '''"Then it is not a sacrifice. It is a transaction." {n}She does not turn away. That would be kinder.{/n} "I bow my head to sacrifices. Go in, Commander, and we will see which of us was right."''',
        c("[Leave the banner where it stands.]", flags=GO + (DECLINED, COST_BOASTED))),
], requires=("trickster", "trickster.ever", STARTED), forbids=(CARRIED, CLOSED, HERALD_SPITE), last=6, optional=True, Relationship=REL,
    ForbidOverrides={HERALD_SPITE: HERALD_ACCOUNTED},
    Chapters=[6], AnswerLists=list(FINAL_LISTS), ReturnToList=True, ReturnText=THRESHOLD_RETURN,
    RequiresAnyGroups=[[BANNER_HELD, ORDER_BANNER]]))
tag(E + "threshold.banner")

# Append witness branches after the retained finale nodes. Her answer does
# not guarantee rescue, settle Pharasma's terms, or grant the personal yes.
SCENES[-1]["Nodes"].extend([
    nar("nocticula_objection", '''{n}The Lady in Shadow watches the cloth stretch toward the rift.{/n} "A touching gesture. Are you going to close it with a banner, Inheritor? Or will your champion still have to do the unpleasant part?"
"The key must still close the Wound," {n}Iomedae answers.{/n} "You will not choose what I do afterwards."''',
        c("Continue", "areelu_objection", requires=(_AREELU_WITNESS,)),
        *(dict(answer, Forbids=[*answer.get("Forbids", []), _AREELU_WITNESS]) for answer in HALL)),
    nar("areelu_objection", '''{n}Areelu studies the staff, then the place where the cloth meets the fire.{/n} "The connection runs through the soul. Your relic cannot make another key."
"I am not making one," {n}says Iomedae. Her hand stays on the staff.{/n} "You have explained what the lock demands. The Commander will answer for the choice. So will I."''', *HALL),
])


# --- The afterlogue (E14e): at Areelu's trial, when the Commander intervened, Pharasma's closing line to a sacrificed Commander
# (Cue_26, "You have earned your peace") is replaced in the bridge world by the terms she set on the bridge page. Cue_25 (the
# living Commander) and Cue_27 (the demon) come first in every parent's Continue(First) list and do not hold here.

SCENES.append(scene(E + "afterlogue.verdict", "The terms", "Iomedae", 6, "", [
    n("verdict", "Pharasma", '''"Now you, {name}, the mortal who walked back over a bridge that was not yours to cross. You have done the impossible, and I have written it down as it happened: you died closing the Worldwound, and your death stands in my book. The Inheritor has answered to me for the rest. Go back to your grave and live beside it. When you come to this hall again there will be no bridge, and no one will be permitted to argue for you."''',
      c("Continue", flags=(VERDICT,)), speaker_unit=PHARASMA_UNIT),
], requires=("trickster.ever", BURIED_ALIVE), forbids=(VERDICT,), last=99, optional=True, Relationship=REL,
    ContinueBefore=dict(Cue=VERDICT_CUE, Parents=list(VERDICT_PARENTS)), RequiresAnyGroups=[list(APPEALS)]))
tag(E + "afterlogue.verdict")


# --- Reactions (named companions with a stake: Seelah, her paladin; Sosiel, Shelyn's priest; Daeran, her mocker). -----------

SCENES.append(reaction("Seelah", E + "react.seelah", ("trickster.ever", DISPUTED, "seelah.in_party"),
    '''"You were up on the platform half the night shouting at the banner. The sentries think you've lost your mind. I told them you always talk to yourself before a big fight." {n}Seelah folds her arms.{/n} "Then they said the banner talked back. In a woman's voice. Very formal."
{n}She looks at you, then up, as if someone might be listening from the roof.{/n} "I've prayed to Her every day since I was a kid picking pockets, and She has never once argued with me. Not once! You get a whole disputation." {n}She scrubs a hand over her face.{/n} "I'm not jealous. I'm a little jealous. I'm mostly scared for you."
"If you're taking Her banner into the Wound... no, don't tell me. If you come back, I'm hitting you. If you don't, I'm praying for you. I'm doing both."''',
    answer_list=SEELAH_HUB, chapter=5, last=6, entry='"About last night, on the citadel."', portrait="Seelah",
    forbids=("seelah_dead", "seelah_gone")))
SCENES[-1]["ForbidOverrides"] = {"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"}
tag(E + "react.seelah")

SCENES.append(reaction("Sosiel", E + "react.sosiel", ("trickster.ever", COMMITTED, DISPUTED),
    '''{n}Sosiel does not look up from the canvas. There is a banner on it, roughed in, and a figure beneath it that is only an outline yet.{/n}
"When I began this portrait, I expected to paint the Commander beneath a banner. Now the banner has become the difficult part." {n}A careful stroke.{/n} "How do I paint the Inheritor conceding an argument? I suppose I begin with the person who made her listen."
"I have started your portrait, my friend. In case she does not answer, at the Wound. It has a black frame." {n}He sets the brush down.{/n} "If she does, I will paint over the frame. Either way, it will be the first true thing I have painted in a long time."''',
    answer_list=SOSIEL_HUB, chapter=5, last=6, entry='"What are you painting?"', portrait="Sosiel",
    forbids=("sosiel.dead", "sosiel.kicked_out")))
tag(E + "react.sosiel")

SCENES.append(reaction("Daeran", E + "react.daeran", ("trickster.ever", COMMITTED, DISPUTED),
    '''"'Your pride will destroy you!'" {n}Daeran does it in her voice, beautifully, and then, with a flourish, in yours.{/n} "'Only if I lose the argument.'"
{n}He lowers himself onto a chair with the air of a man settling in for a play.{/n} "You argued canon law with the Inheritor on a roof at midnight, and she conceded. The whole city is talking about it and none of them believe it. Do you know how many of her priests would have you burned for half of what you said up there? And she conceded. To you. The cathedral will be rewriting its catechism for a decade, and nobody will be allowed to say why."
"Do write down what you said to her. I want to use it on a bishop."''',
    answer_list=DAERAN_HUB, chapter=5, last=6, entry='"You look pleased with yourself."', portrait="Daeran",
    forbids=("daeran.dead", "daeran.kicked_out")))
tag(E + "react.daeran")

SCENES.append(reaction("Daeran", E + "react.daeran_lost", ("trickster.ever", DECLINED),
    '''"I hear the goddess of valour walked out on you." {n}Daeran is delighted, and does not trouble to hide it.{/n} "In the middle of a disputation. On your own roof. A goddess walked out on you, Commander. Do you know how many people can say that? None. Everyone else she simply ignores."
{n}He sobers, fractionally, which for Daeran is a great deal.{/n} "Whatever you said, don't say it again at the Wound. She is the sort who gives exactly one more chance and then carves the refusal over a door."''',
    answer_list=DAERAN_HUB, chapter=5, last=6, entry='"You look pleased with yourself."', portrait="Daeran",
    forbids=("daeran.dead", "daeran.kicked_out", COMMITTED)))
tag(E + "react.daeran_lost")

SCENES.append(reaction("Seelah", E + "react.seelah_eve", ("trickster.ever", COMMITTED, "seelah.in_party"),
    '''{n}Seelah is sitting on an upturned crate by the banner, polishing a buckle that does not need it.{/n}
"She'll be there tomorrow, won't she. At the Wound." {n}It is not quite a question.{/n} "I keep thinking I should tell you something to tell Her. Something a paladin would say. I've been sitting here an hour and all I've got is 'hello' and 'sorry about the pockets'."
{n}She sets the buckle down.{/n} "Don't tell Her anything from me. If I ever see Her, I'll tell Her myself. And you..." {n}She points the polishing rag at you like a sword.{/n} "You come back. That's an order. I know I can't give you orders. I'm giving it anyway."''',
    answer_list=SEELAH_HUB, chapter=6, last=6, entry='"You look like you want to say something."', portrait="Seelah",
    forbids=("seelah_dead", "seelah_gone")))
SCENES[-1]["ForbidOverrides"] = {"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"}
tag(E + "react.seelah_eve")

SCENES.append(reaction("Sosiel", E + "react.sosiel_frame", ("trickster.ever", COMMITTED, E + "react.sosiel"),
    '''{n}Sosiel has the portrait with him, wrapped in oilcloth. He does not unwrap it.{/n}
"It is finished, all but the frame. The black is mixed." {n}He rests the canvas across his knees.{/n} "I kept thinking that if I finished it, you would have to live long enough to see it."
{n}He looks up.{/n} "Come back and let me paint over the black, my friend. I would much rather waste the paint."''',
    answer_list=SOSIEL_HUB, chapter=6, last=6, entry='"You brought the portrait."', portrait="Sosiel",
    forbids=("sosiel.dead", "sosiel.kicked_out")))
tag(E + "react.sosiel_frame")


# --- Epilogue pages (Owner IomedaeEpilogue, Chapter 6; read-only: no page sets a flag). -----------------------------------
# The bridge world is iomedae.appointment_kept (it joins trickster.commander_back). Pages that play while the Commander lives
# Forbid `sacrifice` unless trickster.commander_back holds; only the grieving page Requires `sacrifice` (Last Call's L6 quiets
# it on a Last Call run, where the Commander walked out of the rift).

EPI = "IomedaeEpilogue"
ALIVE = dict(ForbidOverrides={SACRIFICE: BACK})


def page(id, title, nodes, requires, forbids=(), **extra):
    SCENES.append(scene(E + "epilogue." + id, title, EPI, 6, "", nodes, requires=("trickster.ever", *requires),
                        forbids=tuple(forbids), last=6, Relationship=REL, **extra))
    tag(E + "epilogue." + id)


# Every other account of these years is told by the few who were let in on it: the world's Commander is a grave.
HOUSE_FRAME = ("{n}The people who mattered were told, one at a time, behind a shut door, by a stranger with a hood up who knew things only "
               "the Commander could know. Most of them hit the stranger. All of them kept it. Whatever they made of their lives "
               "afterwards they made beside someone the world called by another name, or by none, and the old title they kept for "
               "indoors. When they told it later, among themselves, they said{/n} \"the Commander\" {n}anyway, and nobody outside the door "
               "ever understood whom they meant.{/n}")


page("bridge", "The Bridge", [
    nar("fire", '''{n}The Wound opens through your chest. You walk into it. Your blood boils; the seam draws tight and closes on its key. The power sewn into you burns in the lock, holding it shut. You left the banner planted at the edge. You cannot see it now, or feel your hands.{/n}''',
        c("[Say her name.]", "name"),
        c("[Think of the gorge.]", "gorge", requires=(BRIDGE_SEEN,)),
        c("[Think of nothing. Hold on.]", "hold")),
    nar("name", '''{n}You say it into the fire, or you think you do; there is no air in here to carry it. Whatever you have prayed in your life, this is not a prayer. It is the name of the woman who heard your case, said as though she stood within reach.{/n}''',
        c("[Wait.]", "sword", requires=(BANNER_HELD,)),
        c("[Wait.]", "order", forbids=(BANNER_HELD,))),
    nar("gorge", '''{n}Pins in the rock. The smell of burned rope. Forty people who were going to die, and a tired girl with a wet braid taking off her cloak. She did not know it would hold; you were the banner in her other hand, and you felt her not know. She cast it anyway. You have nothing left to cast. You left it at the edge.{/n}''',
        c("[Wait.]", "sword", requires=(BANNER_HELD,)),
        c("[Wait.]", "order", forbids=(BANNER_HELD,))),
    nar("hold", '''{n}You hold on to the last of yourself, which is not much: a name, a few faces, the voice that heard your case. The fire pulls at it the way it pulls at everything, and for one breath you are not sure whether you are holding on or being held.{/n}''',
        c("Continue", "sword", requires=(BANNER_HELD,)),
        c("Continue", "order", forbids=(BANNER_HELD,))),
    nar("sword", '''{n}Behind you, at the edge, a hand pulls a staff out of scorched rock. You do not see it. You feel it, the way you feel a door open in a house you thought was empty.{/n}
{n}The Sword of Valor comes out over the fire the way a cast net goes out over water, and lies there, flat and taut, from the edge to where you are, no wider than a plank. It does not burn. The fire goes around it.{/n}''',
        c("Continue", "her")),
    nar("order", '''{n}Behind you, at the edge, a hand pulls a staff out of scorched rock. You do not see it. You feel it, the way you feel a door open in a house you thought was empty.{/n}
{n}The cathedral's white banner comes out over the fire the way a cast net goes out over water, and lies there, flat and taut, from the edge to where you are, no wider than a plank. It is a lesser thing than the one she carried, and the fire knows it: it scorches along the edges as it lies there, and the gold thread smokes.{/n}''',
        c("Continue", "her")),
    nar("her", '''{n}At the far end of it, where the fire stops, a woman in plain steel stands with one hand on the staff and her whole weight against it.{/n}
{n}It is Iomedae. You recognize her from Threshold before she takes your hand. The face gives you something to hold on to; it does not make her mortal. At the Summit she said the Worldwound was no longer the concern of mortals alone. Here she has chosen to act, and she will answer for this crossing before Pharasma.{/n}
"I told you I would decide here," {n}she says.{/n} "I have decided. Walk."''',
        c("[Walk.]", "walk"),
        c('"You came."', "came"),
        c('"Why?"', "why"),
        paragraphs=(
            p("{n}It is the face the banner showed you at the gorge, the tired woman bracing herself while her company crossed.{/n}", requires=(BRIDGE_SEEN,)),
            p("{n}You remember her forehead against yours in the dream at the gorge, before she sent you back to the war.{/n}", requires=(MORTAL_SEEN,), forbids=(BRIDGE_SEEN,)),
        )),
    nar("came", '''"I came." {n}Her arm is shaking. Her face is not.{/n} "Walk, Commander. Do not look down. Do not look at me."''',
        c("[Walk.]", "walk")),
    nar("why", '''"Because you argued well, and because you meant it, and because I wanted to." {n}The fire leans at her and she does not lean back.{/n} "The last is not a reason a goddess gives. I am giving it anyway, here, where nobody but you and the Wound can hear me, and the Wound is closing. Walk."''',
        c("[Walk.]", "walk")),
    nar("walk", '''{n}You walk. It gives under you like a wet plank, and you feel her feel it. Behind you the lock finishes closing on the key; you hear it, a sound like a great door shutting in a house you have lived in all your life. Whatever the Wound was pulling on in your chest, there is nothing left there for it to pull. Halfway across, something reaches after you out of the seam, patient and many, and you do not look back.{/n}''',
        c("Continue", "sword_end", requires=(BANNER_HELD,)),
        c("Continue", "order_end", forbids=(BANNER_HELD,))),
    nar("sword_end", '''{n}At the far end she reaches out and takes your wrist and pulls, and you are standing on rock that does not burn. Then she lets the banner go behind you, into the fire, so that nothing can follow. The Sword of Valor drops into the seam and the seam closes over it, and where the Worldwound was there is a scar in the ground, smoking, and her banner is part of the scar.{/n}''',
        c("Continue", "grey")),
    nar("order_end", '''{n}The cathedral's banner holds, and burns. By the far end it is burning under your hand where you grip its edge to keep your feet, and you do not let go, because she does not. When you step off onto rock that does not burn, your palm is burned to the bone and the banner is ash behind you, falling into a seam that closes over it, and where the Worldwound was there is a scar in the ground, smoking.{/n}''',
        c("Continue", "grey")),
    nar("grey", '''{n}Then there is no rock, and no fire, and no scar. There is a grey place, very large and very quiet, and a woman on a throne of bone who has been waiting for you longer than you have been alive. You know her the way you know the ground under you when you fall on it.{/n}
"The key that walked out of its lock," {n}says the Lady of Graves.{/n} "You died in the Wound. I watched the thread cut. Standing on the Inheritor's banner did not keep you from my judgment."''',
        c('"Then why am I talking to you?"', "terms"),
        c("[Say nothing.]", "terms")),
    nar("terms", '''"Because the Inheritor is standing behind you, and she has asked." {n}You do not turn. You can feel her there the way you felt her at the far end of the banner.{/n}
"Hear my terms, then. Your death stays in my book, written as it happened: the Commander of the Fifth Crusade died closing the Worldwound. The world keeps its grave, and you will not contradict it, in word or in face. When you come to this hall again there will be no bridge, and no one will be permitted to argue for you: not she, and not your own tongue. And the Inheritor answers to me for this one, in whatever coin I name, whenever I name it."''',
        c('"Why would you agree to that?"', "why_terms"),
        c("[Look back at Iomedae.]", "liable")),
    nar("why_terms", '''"The Worldwound is closed. Its key belongs among my dead. You will remain there in my reckoning, whatever road you walk." {n}Pharasma's gaze passes to the Inheritor.{/n} "And I will have a goddess answer for the exception. That is worth more than your remaining years."''',
        c("[Look back at Iomedae.]", "liable")),
    nar("liable", '''{n}Iomedae is in plain steel, with one hand still closed as if on a staff that is not there.{/n} "I accept them," {n}she says.{/n} "All of them. Write my name beside the debt."
"It is written," {n}says the Lady of Graves.{/n} "Go back, mortal. Do not thank either of us."''',
        c("Continue", "grave")),
    nar("grave", '''"The Commander of the Fifth Crusade died in the Wound," {n}says Iomedae.{/n} "I saw it. So did the world. You will not contradict us."''',
        c('"And what am I?"', "what"),
        c('"Thank you."', "thanks"),
        c('"Stay."', "stay_here")),
    nar("stay_here", '''"Not tonight." {n}She does not let go of your wrist.{/n} "There is a door in Heaven I have kept waiting for an hour, and a Lady of Graves who will want to hear from me before she hears about me, and a war in the east that did not stop because the Wound did." {n}A pause.{/n} "I have granted you a miracle, Commander. I chose to. One day I will tell you what I choose to ask for it. Until then, you are dead, and I am busy, and we will both have to learn to live with it."''',
        c("Continue", "sleep")),
    nar("what", '''"Somebody I owe an argument." {n}She lets go of your wrist.{/n} "And somebody who owes me a miracle, since I have just granted you one. I chose to. I will tell you, one day, what I choose to ask for it."''',
        c("Continue", "sleep")),
    nar("thanks", '''"Do not thank me. You will not like the bill." {n}She lets go of your wrist.{/n} "I have granted you a miracle, Commander. I chose to. One day I will tell you what I choose to ask for it."''',
        c("Continue", "sleep")),
    nar("sleep", '''{n}She is gone before you can answer, and you lie down on the hot rock at the edge of what was the Worldwound and sleep as you have not slept since Kenabres.{/n}''',
        paragraphs=(
            p('''{n}A sentry found a stranger at the edge of the scorched earth with a corked flask. The burial parties carried you back with the wounded. You left before anyone recognized your face, and Drezen held its rites over an empty coffin. The flask was empty too; your death had been entered in the Lady of Graves' book.{/n}''',
              requires=(H2,)),
            p('''{n}When you woke there was nobody at the edge but the dead and the crows. You walked away from the scar before the burial parties reached it, and Drezen buried the Commander of the Fifth Crusade with honours in the citadel yard. The grave is remarkably unoccupied.{/n}''',
              forbids=(H2,)),
            p('''{n}It had not been your choice to go in; the Lady in Shadow made it for you. Iomedae answered the banner anyway. The coercion did not erase the death, or the terms of your return.{/n}''',
              requires=(COERCED,)),
            p('''{n}She had bowed her head to you at the edge. She did not bow at the bridge. She held the staff.{/n}''',
              requires=(WITNESSED,)),
            p('''{n}She had conceded at the edge, aloud, with the fire at her back, a breath before you went in. She said afterwards that it was the shortest disputation she had ever lost, and the only one she had enjoyed.{/n}''',
              requires=(CONCEDED_AT_WOUND,)),
            p('''{n}You had told her once that it was a sure thing. It was not, and you went anyway. That was the part she kept.{/n}''',
              requires=(COST_BOASTED,)),
            p('''{n}You remembered the grey place when you woke, every word of it, and the terms. You have kept them since. So has she.{/n}'''),
            p('''{n}Drezen woke to find the Sword of Valor gone from the world with its Commander. The chaplains said the Commander had carried it into the Wound as the Inheritor once carried it into battle, and they were right, and never knew how right. The invasions ended with the Wound, but the city's walls had to be watched the old way again, with wards and patrols and a priest at every gate, because every demon lord in the Abyss knew that the banner was gone.{/n}''',
              requires=(BANNER_HELD,)),
            p('''{n}The hand that held the cathedral's banner over the fire never closed properly again.{/n}''',
              requires=(ORDER_BANNER,)),
            p(HOUSE_FRAME),
        )),
], requires=(KEPT,), forbids=(CLOSED,))


page("lived", "The Argument, Continued", [
    nar("page", '''{n}After Threshold she found you, in plain steel and on foot. She set her helm down within reach and looked you in the face.{/n}''',
        c("Continue", "closed", requires=(WOUND_CLOSED,), forbids=(SACRIFICE,)),
        c("Continue", "flask", requires=(H2,), forbids=(CARRIED,)),
        c("Continue", "open", forbids=(WOUND_CLOSED,))),
    nar("closed", '''"You did not go in. Something else was the key." {n}She sits heavily, like a soldier after a march.{/n} "I am relieved. I had prepared to lose you. I have not yet stopped being angry about that."''',
        c('"Sorry to waste your decision."', "wasted"),
        c("[Kiss her.]", "kissed"), paragraphs=(
            p('''{n}She glances at your hand, which held the banner staff at the edge while she waited for the fire to take you.{/n}''', requires=(CARRIED,)),
            p('''{n}Her banner never reached the edge. She had watched your choice with nothing to cast across the fire.{/n}''', forbids=(CARRIED,)))),
    nar("wasted", '''"It was not wasted. I know what I would have done." {n}She looks at you sidelong.{/n} "So, I think, do you. That is enough. I do not need to have been tested to know what I am."''',
        c("Continue", "end")),
    nar("kissed", '''{n}She lets you, and then some. When she draws back her hand stays on the back of your neck.{/n} "Where it flew," {n}she says.{/n} "Tonight."''',
        c("Continue", "end")),
    nar("flask", '''"A bottle," {n}says Iomedae, before anything else.{/n} "You went into the Wound with your death corked in a bottle, and not with my banner." {n}She does not sit.{/n} "I stood at the edge with nothing to answer, and you walked out anyway, by a Trickster's answer to a question I had asked you honestly."''',
        c('"You\'d have preferred mine."', "preferred"),
        c('"I didn\'t want to make you choose."', "choose")),
    nar("preferred", '''"I would." {n}A pause.{/n} "I also prefer you alive. I did not expect the two preferences to disagree, and I do not enjoy it." {n}Then, at last, she sits.{/n}''',
        c("Continue", "end")),
    nar("choose", '''"You decided for me." {n}Her voice does not rise. It goes flat, the way it went flat in the square.{/n} "The one choice at that Wound that was mine, and you took it out of my hands and called it kindness. Do not do that again. Not to me."
{n}Then she sits down, all at once, and puts her hand over yours on the table, and leaves it there.{/n}''',
        c("Continue", "end")),
    nar("open", '''"You left it open," {n}says Iomedae. No greeting.{/n} "Every soul it eats from now on, it eats because you chose a joke over a lock."''',
        c("Continue", "open_banner", requires=(CARRIED,)),
        c("Continue", "open_plain", forbids=(CARRIED,))),
    nar("open_banner", '''"You raised my banner at the edge, and I stood beside it deciding, and then you told a joke instead of going in. My banner is still standing there, stretched toward a Wound that stayed open. I have not taken it back. I want it there, where I can see what it failed to cross."''',
        c("Continue", "open_stay")),
    nar("open_plain", '''"I stood at the edge with nothing to answer while you did it. I grieve every one of them, as I told you I would."''',
        c("Continue", "open_stay")),
    nar("open_stay", '''{n}She does not leave.{/n} "I conceded that I may love a Trickster. I did not concede that I would like everything a Trickster does. I came. Now help me close it."''',
        c('"How?"', "how"),
        c('"I\'m sorry."', "sorry")),
    nar("how", '''"With soldiers. Scouts. People who know where the next demons will come through. We have work to do."''',
        c("Continue", "end")),
    nar("sorry", '''"Good. Stay sorry. It will make you useful." {n}Something in her face eases, very slightly.{/n} "Not too sorry. I have seen what that does to people, and I would rather have you."''',
        c("Continue", "end")),
    nar("end", '''{n}She keeps her hand against yours a moment longer, then reaches for her helm.{/n} "The platform where my banner flew. I want to see you there." {n}She leaves on foot, with the remaining orders still spread across your table.{/n}'''),
], requires=(COMMITTED,), forbids=(KEPT, SACRIFICE, CLOSED), **ALIVE)


SEELAH_OPEN = '{n}Seelah found you at breakfast. She sat down across from you with her porridge and did not eat it.{/n} "The east-wall sentry says a knight came down your stair before dawn," {n}she said.{/n} "Plain steel. Braid. Wished him good morning like she\'d known him all his life." {n}She looked at you for a long moment, and whatever she saw made her put the spoon down.{/n} "Was that Her?" {n}Seelah rubs her face with both hands.{/n} "No. Don\'t answer that. I need to think. And you\'d better think too. Whatever happened up there, the people who follow Her still need us downstairs."'
SEELAH_BURIED = '{n}Seelah heard it from the sergeant at the postern, who had told nobody else. She found the stranger that evening in the back room of an inn outside the walls, shut the door, and sat down without taking off her gauntlets.{/n} "You and her," {n}she said. It was not a question. She looked at the stranger for a long time, the way she used to look at the Commander before a charge.{/n} "Was that Her?" {n}Seelah rubs her face with both hands.{/n} "No. Don\'t answer that. I need to think. And you\'d better think too. Whatever happened up there, the people who follow Her still need us downstairs."'


page("platform", "Where It Flew", [
    nar("night", '''{n}The platform on top of the citadel of Drezen, at night.{/n}''',
        c("Continue", "buried", requires=(DEAD_TO_WORLD,)),
        c("Continue", "open", forbids=(DEAD_TO_WORLD,))),
    nar("buried", '''{n}Drezen still wears black for its Commander. You come into the city after dark in a borrowed coat with the hood up, by the postern under the east wall. The sergeant who keeps it served under you at the citadel gate; she saw your face under the hood the first night, and went white, and opened the door, and has opened it every night since without a word, and climbs to the platform stair ahead of you to send the watch on an errand. Nobody else looks at you twice. You are nobody; there is a grave in the citadel yard to prove it.{/n}''',
        c("Continue", "bare_kept", requires=(KEPT,)),
        c("Continue", "bare_flask", forbids=(KEPT,))),
    nar("bare_kept", '''{n}The platform is bare. The pole stands in its iron socket with the halyard slapping against it, and nothing at the top tonight. Her banner is in the seam of the world, and whatever Drezen hangs there next will be something else.{/n}''',
        c("Continue", "her")),
    nar("bare_flask", '''{n}The pole is bare tonight. Whatever flew there at dusk has been taken down and folded on the parapet, squared at the corners the way a soldier folds a thing, and you know who asked for it.{/n}''',
        c("Continue", "her")),
    nar("open", '''{n}You climb the stair to the citadel's platform, past a sentry who salutes and asks nothing.{/n}''',
        c("Continue", "open_left", requires=(CARRIED,)),
        c("Continue", "open_down", forbids=(CARRIED,))),
    nar("open_left", '''{n}The pole has been bare since Threshold. Her banner is still standing at the edge of the Wound where you planted it, and she has never asked for it back. The halyard slaps against the empty pole in the wind, and there is nothing at the top.{/n}''',
        c("Continue", "her")),
    nar("open_down", '''{n}She asked for it bare. You took the banner down yourself at dusk, folded it, and left it on the table in your quarters. The halyard slaps against the empty pole in the wind, and there is nothing at the top.{/n}''',
        c("Continue", "her")),
    nar("her", '''{n}She sits on the parapet, her helm beside her. Plain steel, a plain cloak, a braid loosened by the wind. She sets a hand over yours as you come within reach.{/n} "The war has had enough of this night. I came for you."''',
        c('"Understood. Then why are you here?"', "why"),
        c('"The pole looks wrong without it."', "pole"),
        c('"Your banner showed me things. Did you mind?"', "mind", requires=(DREAM_BANNER,)),
        c("[Go to her.]", "close"), paragraphs=(
            p('''"The Wound is still open. At dawn I go back to the people your joke left fighting it." {n}Her hand stays over yours.{/n}''', forbids=(WOUND_CLOSED,)),
            p('''"I have not forgotten the people whose minds your victory broke." {n}She presses your knuckles once.{/n} "Nor have you. Keep it that way."''', requires=(OWNED_MADNESS,)),
            p('''"The canon still wants his cloth back. Wanting you has not persuaded me that he is wrong."''', requires=(COST_STOLEN,)),
            p('''"Neither of us knew whether I would answer the fire." {n}She turns your hand palm-up.{/n} "I know why I came here tonight."''', requires=(KEPT,), forbids=(OWNED_MADNESS, COST_STOLEN,)))),
    nar("mind", '''"I minded a great deal." {n}She does not sound as though she minds now.{/n} "It showed you a girl in the rain who did not know what she was doing, and pretended well, and whatever else it thought you should see. I was more frightened in some of it than I have ever admitted to a priest." {n}She looks at the empty pole.{/n} "Which did you like best?"''',
        c('"The rain. You told a banner things you wouldn\'t tell a person."', "liked"),
        c('"The gorge. You burned the cloak behind you."', "liked", requires=(E + "dream.chasm",)),
        c('"The knight. You argued a dead man into his grave."', "liked", requires=(E + "dream.test",))),
    nar("liked", '''"You would choose that." {n}Her mouth curves briefly.{/n} "Come here."''',
        c("[Go to her.]", "close")),
    nar("why", '''"Because I wanted to touch you awake." {n}She stands close enough that her breastplate presses against your coat.{/n} "And I intend to stay until morning."''',
        c("[Go to her.]", "close")),
    nar("pole", '''"Bare," {n}she agrees.{/n}''',
        c("Continue", "pole_kept", requires=(KEPT,)),
        c("Continue", "pole_open", forbids=(KEPT,))),
    nar("pole_kept", '''"I brought you back across it." {n}She looks at the empty pole.{/n} "We left it in the Wound. I did not leave you there."''',
        c("[Go to her.]", "close")),
    nar("pole_open", '''"The Sword of Valor was mine before the Starstone." {n}Her gaze leaves the pole and settles on you.{/n} "Tonight I want you here, under the sky."''',
        c("[Go to her.]", "close")),
    nar("close", '''{n}She smells of cold iron and woodsmoke. Her hands close at your jaw, rough palms against your skin. She draws you close enough that you feel her breath.{/n} "I wanted to hear you again. Now I want your mouth. You may save your next argument until morning."''',
        c("[Kiss her.]", "kiss"),
        c('"Then stop pretending."', "kiss"),
        c("[Start on the buckles at her side.]", "buckles"),
        c("[Stay beside her without going further.]", "night_quiet")),
    nar("kiss", '''{n}Her mouth meets yours hard. Her hand tightens at the back of your neck; when you catch her waist she presses closer. She works a vambrace strap loose without breaking the kiss, then pulls your hand to the buckles at her side.{/n}''',
        c("Continue", "steel")),
    nar("buckles", '''{n}Your fingers find the first buckle at her side. She does not stop you. She sets her own hands to the other side and works the straps with a soldier's speed, and you meet at the last buckle, and she laughs against your mouth, low and short, as if it had surprised her.{/n}''',
        c("Continue", "steel")),
    nar("steel", '''{n}She lowers the breastplate onto the stones herself. She will want it again in the morning. The gambeson follows; she loosens the linen at her throat and pulls it away. There are old scars on the skin she has chosen to show you, one pale line along her ribs.{/n} "Look at me." {n}She takes your hand and places it against her bare side.{/n}''',
        c("[Put your mouth to the scar along her ribs.]", "ribs"),
        c('"They\'re beautiful."', "liar")),
    nar("ribs", '''{n}Her breath goes out of her short and hard, and her hand closes in your hair and holds you there. She lets it go on until she is shaking, the way an arm shakes that has held a weight too long.{/n}''',
        c("Continue", "cloak")),
    nar("liar", '''{n}Her thumb traces your mouth. She does not cover herself.{/n} "Then come closer."''',
        c("Continue", "cloak")),
    nar("cloak", '''{n}She unclasps her cloak and spreads it across the bare stones beneath the pole. The wool settles against your boots. She reaches for you.{/n}
"Come here."''',
        c("Continue", "down")),
    nar("down", '''{n}She pulls you onto the spread cloak and bends over you. The braid falls across her bare shoulder; cold stone presses through the wool. Her hands hold your wrists for a moment, then release them. She bends to your throat and catches the laces of your shirt between her fingers.{/n} "Stay with me." {n}The laces give. The shirt goes over your head and onto the stones, and she lays herself down against you, her heat against the cold of the night, and the want in her is not a petition, it is a decision already made. Her breath leaves her in a sound she does not trouble to hide. She is a goddess on a roof under open sky and she is shaking with how badly she wants to be had.{/n}''',
        c("Continue", E + "epilogue.platform.explicit.1", requires=(KEPT,)),
        c("Continue", E + "epilogue.platform.explicit.1", forbids=(KEPT, DEAD_TO_WORLD)),
        c("Continue", E + "epilogue.platform.explicit.1", requires=(DEAD_TO_WORLD,), forbids=(KEPT,)),
        c("[Draw back and sit up.]", "night_quiet")),
    nar("morning_dead", '''{n}You wake cold beneath her cloak. Your shirt lies tangled with her linen; she pulls it free and hands it to you. Before fastening her breastplate she leans down and kisses you again, slowly enough to make the morning watch inconvenient.{/n}
"I have a war," {n}she says.{/n} "So do you, though the world has buried you and it will be harder to wage."
{n}Below, on the stair, boots: the sentry coming up on the morning round. You are the late Commander of the Fifth Crusade, and there is an empty coffin in the yard below with your name on it; you roll off the cloak into the shadow of the parapet and stay there, and she passes you your coat, holding the hood open until you have pulled it over your face.{/n}
"I will come back. Not often. Do not wait on the platform; I will find you." {n}She tucks her cloak round you where you crouch. The boots are halfway up the stair. She does not hurry.{/n} "One thing more. The Commander of the Fifth Crusade is buried in the yard below. What am I to call what is left?"''',
        c("[Tell her a name you make up on the spot.]", "name_new"),
        c("[Tell her your own name, the one from before the crusade.]", "name_old"),
        c('"You choose."', "name_hers")),
    nar("morning_kept", '''{n}You wake cold beneath her cloak. Your shirt lies tangled with her linen; she pulls it free and hands it to you. Before fastening her breastplate she leans down and kisses you again, slowly enough to make the morning watch inconvenient.{/n}
"I have a war," {n}she says.{/n} "So do you, though you are dead and it will be harder to wage."
{n}Below, on the stair, boots: the sentry coming up on the morning round. You are the late Commander of the Fifth Crusade, and your grave is in the yard below; you roll off the cloak into the shadow of the parapet and stay there, and she passes you your coat, holding the hood open until you have pulled it over your face.{/n}
"I will come back. Not often. Do not wait on the platform; I will find you." {n}She tucks her cloak round you where you crouch.{/n} "And the miracle: I have not decided what I will ask for it. When I have, you will not like it, and you will do it anyway."
{n}The boots are halfway up the stair. She does not hurry.{/n} "One thing more. The Commander of the Fifth Crusade is buried in the yard below. What am I to call what is left?"''',
        c("[Tell her a name you make up on the spot.]", "name_new"),
        c("[Tell her your own name, the one from before the crusade.]", "name_old"),
        c('"You choose."', "name_hers")),
    nar("name_new", '''{n}She repeats it once, to see how it sits in her mouth, and her eyebrows go up very slightly.{/n} "That is a terrible name. It sounds like a pedlar's." {n}A pause.{/n} "It will do. Nobody will look twice at a pedlar."''',
        c("Continue", "sentry")),
    nar("name_old", '''"That name was yours before the crusade," {n}she says. She repeats it under her breath.{/n} "Good. I will use it."''',
        c("Continue", "sentry")),
    nar("name_hers", '''"No." {n}She answers at once.{/n} "I will not choose it for you. Tell me your choice when I come back."''',
        c("Continue", "sentry")),
    nar("sentry", '''{n}The sentry reaches the top of the stair and finds a bare pole, an empty platform, and a knight of some small order in plain steel coming down past him, who wishes him a good morning in a voice that makes him stand straighter for the rest of the day.{/n}''',
        c("Continue"), paragraphs=(p(SEELAH_BURIED, requires=("seelah.in_party",)),)),
    nar("morning_open", '''{n}You wake cold beneath her cloak. Your shirt lies tangled with her linen; she pulls it free and hands it to you. Before fastening her breastplate she leans down and kisses you again, slowly enough to make the morning watch inconvenient.{/n}
"I have a war," {n}she says,{/n} "and so do you, and you are still its Commander."
"I will come back. Not often. Do not wait on the platform; I will find you." {n}At the head of the stair she turns.{/n} "Your sentries will talk. Let them. I have been talked about by better."
{n}The sentry on the morning round salutes a knight of some small order in plain steel coming down the citadel stair before dawn, and watches her pass. By breakfast the sergeant has heard about her.{/n}''',
        c("Continue"), paragraphs=(p(SEELAH_OPEN, requires=("seelah.in_party",)),)),
    # Slot A: mutual waking first night on the cloak; heated-cut default, brief supplies future prose.
    nar(E + "epilogue.platform.explicit.1", '''{n}She draws you against her on the spread cloak. Your shirt falls beside the steel; her hand closes at the back of your neck, and she kisses you until you are both breathing hard. The cold, the stone and the watch below go out of the world; there is her skin, her breath at your ear, and a sound she makes against your throat that she makes no effort to hide. Afterwards she keeps you close.{/n} "Stay." {n}The halyard strikes the pole once in the dark.{/n}''',
        c("Continue", "morning_kept", requires=(KEPT,)),
        c("Continue", "morning_open", forbids=(KEPT, DEAD_TO_WORLD)),
        c("Continue", "morning_dead", requires=(DEAD_TO_WORLD,), forbids=(KEPT,))),
    nar("night_quiet", '''{n}She releases you, takes up her linen and sits beside you with the cloak over both your shoulders. Below, a watchman calls the change. She remains until the sky pales, then takes up her steel.{/n} "I will find you again. My duties will decide when."''',
        c("[Leave before the morning watch.]"), paragraphs=(
            p('''{n}You pull your hood low before descending. Drezen still mourns the name carved on your empty grave.{/n}''', requires=(DEAD_TO_WORLD,)),
            p('''{n}The sentry salutes you. There are orders waiting downstairs for the Commander.{/n}''', forbids=(DEAD_TO_WORLD,)))),
], requires=(COMMITTED,), forbids=(SACRIFICE, CLOSED), **ALIVE)


page("gate", "A Stranger", [
    nar("start", '''{n}Some years later.{/n}''',
        c("Continue", "road", requires=(AFTER_ROAD,)),
        c("Continue", "near", requires=(AFTER_NEAR,)),
        c("Continue", "war", requires=(AFTER_WAR,)),
        c("Continue", "fence", forbids=(AFTER_ROAD, AFTER_NEAR, AFTER_WAR))),
    nar("road", '''{n}The stranger has walked a great many roads in Mendev, most of them for the pleasure of it, as promised, and is sitting on a milestone outside a village whose name is not worth learning, eating an apple, when a woman in plain steel comes up the road from the south. The stranger knows her first. The stranger always does.{/n}''',
        c("Continue", "speech")),
    nar("near", '''{n}The stranger keeps the lamps at a waystation on the Drezen road, two days south of the city, where the carters stop and nobody asks a lamp-keeper anything but the price of oats. At dusk a woman in plain steel comes in off the road and sits down at the end of the bench. The stranger knows her first. The stranger always does.{/n}''',
        c("Continue", "speech")),
    nar("war", '''{n}The stranger is behind a barricade at the edge of somebody else's battle, a long way from Drezen, with a borrowed crossbow and no name anyone here would recognize, when the fighting slackens and a woman in plain steel drops down behind the same barricade to catch her breath. The stranger knows her first. The stranger always does.{/n}''',
        c("Continue", "speech")),
    nar("fence", '''{n}The stranger is mending a fence outside a Mendevian village when a woman in plain steel stops at the gate. The stranger knows her first. The stranger always does.{/n}''',
        c("Continue", "speech")),
    nar("speech", '''"You were buried with honours," {n}says Iomedae.{/n} "I attended."''',
        c('"I heard. Nice speech. Too long."', "long"),
        c('"Did they cry?"', "cry"),
        c("[Say nothing. Move over and make room.]", "room")),
    nar("long", '''"It was exactly as long as you deserved." {n}She does not smile. She does not leave, either.{/n}''',
        c("Continue", "stay")),
    nar("cry", '''"Some of your companions did. One of them struck the coffin with her fist and hurt her hand, and would not say why she was laughing." {n}She considers.{/n} "I did not cry. I have not the habit. I stood at the back and was very angry with you for not being in it, which I understand is a mortal custom."''',
        c("Continue", "stay")),
    nar("room", '''{n}She sits. Road dust clings to the seams of her steel. You shift to make room; she catches your hand before it can withdraw and settles it against her knee. For a while she says nothing. Hooves pass on the road beyond the gate.{/n}''',
        c("Continue", "stay")),
    nar("stay", '''"I cannot stay long," {n}she says, which is what she always says.{/n} "There is a war in the east. There is always a war in the east."''',
        c('"Have you decided about the miracle?"', "miracle"),
        c('"Stay for supper, at least."', "supper"),
        c("[Take her hand, the one with the notch in it.]", "hand"),
        c('"What did the Lady of Graves say, when you told her?"', "graves")),
    nar("graves", '''"That she had noticed." {n}Iomedae is quiet for a moment.{/n} "She does not waste words. Nor do I, usually. I put your argument to her, and then mine. She agreed with neither. A soul that stands on a goddess's banner is on nobody's road, she said, and she would not have it argued over twice. She let you go on her terms: you are dead in her book, there is no appeal at the next appointment, and I answer to her for this one. I do. Then she told me that next time there will be nothing to cross back over, and that she will be waiting at the other end of it herself."
{n}She looks at the road.{/n} "I accepted her terms. She has my answer. So do you."''',
        c("Continue", "leave")),
    nar("miracle", '''"No." {n}Then, because you go on looking at her:{/n} "Yes. I have decided a hundred times, and each time I have decided that it can wait, because once I ask for it I will have asked, and you will do it, and then it will be done." {n}She looks at the road.{/n} "I would rather be owed."''',
        c("Continue", "leave")),
    nar("supper", '''"Supper." {n}She says it as if the word amused her more than it should.{/n} "Very well. Supper. Then the war."
{n}She eats what the stranger eats, which is bread and whatever there is, and she eats it the way soldiers eat, quickly and without looking at it, and when she has finished she takes the last onion off the board without asking and eats that too, raw, and does not explain.{/n}''',
        c("Continue", "leave")),
    nar("hand", '''{n}She turns her hand in yours and threads her fingers through it. You know the pressure; she knows where your thumb will rest.{/n} "I had to ride through the night to find you here. Keep hold a little longer."''',
        c("Continue", "leave")),
    nar("leave", '''{n}At the gate she comes back for one more kiss, catching your coat as you turn. Then she takes her sword and goes down the road toward the fighting. You return to the place she left warm beside you.{/n}''',
        c("Continue")),
], requires=(KEPT,), forbids=(CLOSED,))


page("after", "Here and There", [
    nar("page", '''{n}Iomedae kept her war. Her visits were brief and irregular; she arrived in plain steel, found the Commander wherever the fighting or the road had taken them, and reached for their hand before asking for news.{/n}''',
        dict(c("Continue"), Id="continue"),
        c("[Stay beside her after the vigil.]", E + "epilogue.after.explicit.1", requires=(KEPT,)),
        paragraphs=(
            p('''{n}The Commander of the Fifth Crusade was buried at Drezen with honours, and the grave is remarkably unoccupied. Travellers still cross paths with a stranger here and there, on the roads of Mendev and further off. Among those who keep finding the stranger is a woman in plain steel, whom the stranger always recognizes first.{/n}''',
              requires=(KEPT,)),
            p('''{n}In the ninth year she called in the debt. One of her knights lay dying in a hospice in Mendev, asking whether his company had held a ford. She could not leave the line she was holding. The stranger found her with blood drying on her gauntlets.{/n} "Go to him. Tell him what happened," {n}she said.{/n} "He has earned the truth."
{n}The stranger sat beside the knight through the night. The ford had fallen. It had held one hour longer than anyone expected, and in that hour the village behind it had emptied onto the road. He heard the names of the people who escaped. He died before dawn, knowing whom that hour had saved.{/n}
{n}When the stranger returned, she took off the bloodied gauntlets and listened to the names, the account of the ford, and the knight's last answer. "The debt is paid," she said. She moved her sword from the other chair and drew it up beside hers.{/n}
{n}She did not sit. She stood in the middle of the room with the lamp behind her, a woman who had held a line for nine days without once being afraid of it, and looked at the stranger the way she looked at ground she meant to take.{/n} "I have spent the night picturing this, and not the ford. That is a failing. I intend to indulge it." {n}Her fist closed in the front of the stranger's coat and pulled them across the room. The kiss tasted of iron and cold water; there was dried blood in the creases of her knuckles and she did not care who wore it. She unbuckled the breastplate herself, fast, a soldier's hands, and slapped the stranger's fingers away from the straps at her hip.{/n} "Mine. Yours I will do slowly." {n}She did it slowly. The coat went, the shirt, the belt; her palms went over ribs and hip and the long muscle of the thigh like an inventory of something she had feared lost, and her breath thickened when the stranger's mouth found the pulse beneath her jaw. The sword went down on the floor within reach of the bed. It was the last thing she put down. She drew them under the blankets, skin to skin, her bare thigh sliding between theirs, and held them there with her whole weight while the heat climbed between them and neither pretended to patience. Her mouth was at their ear; her hand travelled down their belly and stopped, deliberately, at the edge of what came next.{/n}''',
              requires=(KEPT,)),
            p('''{n}The Commander lived on in the open, with a name and a war and a great many people who wanted things. She came anyway, rarely, and waited at the back of the hall in plain steel until the petitioners had gone.{/n}''',
              forbids=(KEPT, "lastcall.dead_on_record")),
            p('''{n}The world buried the Commander of the Fifth Crusade in an empty coffin, as the Commander had arranged it with a flask, and without her banner. She came anyway, to wherever the stranger was, and never once asked about the bottle.{/n}''',
              requires=("lastcall.dead_on_record",), forbids=(KEPT,)),
            p('''{n}She said the argument on the platform was the best she had lost in an age. She had it by heart, and quoted it back whenever the stranger was being unreasonable.{/n}''',
              requires=(ARGUED_OLD,)),
            p('''{n}She said the argument on the platform was the worst she had ever lost, and that she had lost it anyway. She said it fondly, which was worse.{/n}''',
              requires=(ARGUED_PLAIN,)),
            p('''{n}She did not let Drezen's madness rest because it had been answered. Every winter she sent the stranger to the houses where the ones who never came back from it were kept, to sit with them, carry water, and be cursed at by people who did not know whom they were cursing, and the stranger went. She never called it a penance. She called it the rest of the answer.{/n}''',
              requires=(OWNED_MADNESS,)),
            p('''{n}The cathedral of Drezen never saw its banner of the Inheritor again. The old canon blamed demons in public and the late Commander in private, and in his prayers he told Her so, and was, he believed, heard.{/n}''',
              requires=(COST_STOLEN, DEAD_TO_WORLD)),
            p('''{n}The canon blamed the Commander for the missing banner in person. Iomedae heard the accusation without excusing the theft. You had admitted it to her; the admission did not give the church its cloth back.{/n}''', requires=(COST_STOLEN,), forbids=(DEAD_TO_WORLD,)),
            p('''{n}The oath sworn on her sign in the cathedral held. She never once had to remind anybody of it. That, she said, was the first miracle she had ever seen a Trickster perform.{/n}''',
              requires=(COST_OATH,)),
            p('''{n}The hand that held the cathedral's banner over the fire never closed properly again. She held it sometimes, the burned one, and never healed it.{/n} "You paid that," {n}she said.{/n} "I will not take it from you."''',
              requires=(ORDER_BANNER, KEPT)),
            p('''{n}Drezen flew a sock over the citadel for a year afterwards, in its Commander's memory. She never said a word about it. She did not need to.{/n}''',
              requires=(SOCK, DEAD_TO_WORLD)),
            p('''{n}Drezen flew the sock until proper cloth was raised again. Its living Commander was made to hear every complaint from the cathedral. Iomedae did not intervene.{/n}''', requires=(SOCK,), forbids=(DEAD_TO_WORLD,)),
            p('''{n}The Hand of the Inheritor never learned where his lady went on certain nights. He suspected, and prayed for the stranger by name, and was too good an angel to ask.{/n}''',
              requires=(HERALD_HEAVEN,)),
            p('''{n}Some nights she came and said nothing at all, and the stranger learned that those were the nights she was thinking of her herald.{/n}''',
              requires=(HERALD_FELL,), forbids=(HERALD_SAVED,)),
            p('''{n}The flask never sloshed. Once she laid her hand over the pocket, as she had over the banner staff at the edge. After the crossing the flask was empty; Pharasma kept the death.{/n}''',
              requires=(BURIED_ALIVE, H2, "trickster.lastcall.primed.bottle")),
            p('''{n}Once she set her palm against the pocket that held the flask. No banner had reached the Wound, and the bottle still held its death. She withdrew her hand without asking to take it.{/n}''', requires=("lastcall.bottled_held",), forbids=(BURIED_ALIVE, CARRIED)),
            p('''{n}The stranger walked the roads of Mendev for the pleasure of it, as promised, and she said that of all the terms of the disputation it was the only one she had not expected to enjoy enforcing.{/n}''',
              requires=(AFTER_ROAD, KEPT)),
            p('''{n}The stranger kept a lamp on the Drezen road, two days south of the city, and watched over it without being thanked, as promised. The carters say the lamp-keeper has a visitor sometimes, a knight of some small order, and that on those nights the lamp burns until morning.{/n}''',
              requires=(AFTER_NEAR, KEPT)),
            p('''{n}The stranger went where she was fighting, as promised, and lost a great many arguments in a great many camps, and won the ones that mattered.{/n}''',
              requires=(AFTER_WAR, KEPT)),
            p('''{n}The stranger had told her on the platform that there had never been a life that was not owed to somebody. She took that as a challenge. It was some years before the stranger noticed that the life had become their own, and she did not point it out, because she does not gloat, quite.{/n}''',
              requires=(AFTER_OPEN, KEPT)),
            p('''{n}The embodied power burned in the seam. What remained belonged to the soul, enough to speak at the Lady of Graves' trial. The returned body could not wield it. The stranger walked Mendev without that strength, as promised.{/n}''',
              requires=(KEPT,)),
            p('''{n}She never spoke of the kiss at the edge of the Wound. Neither did anyone else who saw it, and a great many people saw it, not all of them friendly. Iomedae did not apologize for it when her priests asked.{/n}''',
              requires=(KISSED_AT_WOUND,)),
            p('''{n}The word in the socket stayed where it had been sealed, under a thumbprint in the wax, at the foot of the bare pole over Drezen. Nobody else ever read it. She said she had read it enough for everyone.{/n}''',
              requires=(TESTED,), forbids=(SLIP_BURNED,)),
            p('''{n}When veterans praised the fight in Baphomet's prison, you told them how you had killed the Herald out of spite. Iomedae never called that admission absolution. Neither did you.{/n}''', requires=(HERALD_ACCOUNTED,)),
            p('''{n}When the second appointment comes there will be no appeal; she has said so. She comes anyway.{/n}''', requires=(KEPT,)),
            p('''{n}Her banner had stood at the edge, but the Commander walked away with the Wound still open. No crossing emptied the flask. Once she rested her hand over the cork through the coat, then withdrew it. The death stayed in the bottle.{/n}''',
              requires=("lastcall.h1", "lastcall.bottled_held", CARRIED), forbids=(BURIED_ALIVE,)),
        )),
    # Slot B: established lovers after the paid vigil; undressing and reunion on the bed, then the heated cut.
    nar(E + "epilogue.after.explicit.1", '''{n}She set her sword beside the bed and caught the stranger by the coat. She kissed them hard, then pushed the coat from their shoulders. The gauntlets were already off; she unbuckled her breastplate and laid it beside the sword. They helped each other out of the remaining straps and clothes, as they had on other brief nights together.{/n} "Stay. I rode through the night for this." {n}She drew them down beside her, bare skin warm beneath the blankets. Her hand settled at their hip; she kissed them again and pulled them closer. She turned beneath them, and her hand tightened at their back, and the long ride, the sword and the war were forgotten for a while. Beyond the shutter, a watchman called the hour.{/n}''',
        c("Continue", "vigil_morning")),
    nar("vigil_morning", '''{n}At dawn she sits on the bed's edge, tugging her boots on. You catch her loose braid and she turns back for a kiss, one knee against the blankets. Outside, the wounded are being brought in.{/n} "I must go." {n}She presses your hand once before reaching for her sword.{/n}''',
        c("Continue")),
], requires=(COMMITTED,), forbids=(SACRIFICE, CLOSED), **ALIVE)


page("unanswered", "Bowed", [
    nar("page", '''{n}The Worldwound closed on its key, as the witch had designed it, and the key did not come back.{/n}''',
        paragraphs=(
            p('''{n}Her banner stood at the edge when you went in. She had said she bowed to sacrifices and not to bargains, and you had offered her a bargain. She did not answer it. She bowed her head at the edge, as she had said she would, and meant it, and the banner burned where it stood.{/n}''',
              requires=(CARRIED, DECLINED, COST_BOASTED), forbids=(COMMITTED,)),
            p('''{n}Her banner stood at the edge when you went in. You had refused to give her an honest answer, and had not corrected it. She did not answer the banner. She bowed her head at the edge, and meant it, and the banner burned where it stood.{/n}''',
              requires=(CARRIED, DECLINED), forbids=(COMMITTED, COST_BOASTED)),
            p('''{n}Her banner stood at the edge when you went in, and she had turned her face from you. It burned where it stood.{/n}''',
              requires=(CARRIED, CLOSED)),
            p('''{n}She had made her personal concession. She was at the edge. You never raised her banner there, and she could not answer what was never raised. She stood at the lip of the Wound a long time after it closed, and said nothing to anyone.{/n}''',
              requires=(COMMITTED,), forbids=(CARRIED,)),
            p('''{n}She had watched you choose. She bowed her head at the edge, and meant it, and came once to the grave in Drezen, and did not come again.{/n}''',
              forbids=(COMMITTED, CARRIED)),
            p('''{n}Drezen buried its Commander with honours. The chaplains said afterwards that a knight in plain steel stood at the back of the crowd through every speech and left before the last one, and that nobody knew her order.{/n}'''),
            p('''{n}She had been at the edge, in her own shape, beside nothing. When the Wound closed on its key she stood where the banner would have stood, and waited, as if a bridge might yet be laid from the other side by someone who had never learned how. None was.{/n}''',
              requires=(COMMITTED,), forbids=(CARRIED,)),
            p('''{n}She came back once more, alone, on a night when the citadel yard was empty, and stood at the grave, and said the words over it herself. They were short.{/n} "You argued well. You meant it. You did not raise it." {n}Then, after a while, as if it had been pried out of her:{/n} "I would have answered." {n}Nobody heard her. She had made sure of that.{/n}''',
              requires=(COMMITTED,), forbids=(CARRIED,)),
            p('''{n}She kept one thing from the Wound: a scorched strip of gold-threaded cloth that the fire had spat out at the edge, all that was left of her banner. She did not say what she kept it for. She folded it carefully before taking it away.{/n}''',
              requires=(CARRIED,)),
        )),
], requires=(STARTED, SACRIFICE), forbids=(BACK,))


page("respect", "Watched", [
    nar("page", '''{n}Iomedae kept her word: she did not intervene, and she watched.{/n}''',
        paragraphs=(
            p('''{n}You moved your bed out from under her banner, and the dreams stopped, and nothing else ever began.{/n}''',
              requires=(SENT_AWAY,)),
            p('''{n}She had said she did not bow to bargains, and you had offered her one on the platform. She did not come. Once, on a road in Mendev, a knight in plain steel passed you going the other way, and nodded, and did not stop.{/n}''',
              requires=(DECLINED, COST_BOASTED, DISPUTED)),
            p('''{n}She had walked off your roof over a thing you had said there, and you had not unsaid it. She did not come. Once, on a road in Mendev, a knight in plain steel passed you going the other way, and nodded, and did not stop.{/n}''',
              requires=(DECLINED, DISPUTED), forbids=(COST_BOASTED,)),
            p('''{n}At the Wound you asked for certainty instead of risking the wager. She refused the bargain there. Later, on a Mendev road, she nodded as she passed you and did not stop.{/n}''', requires=(DECLINED,), forbids=(DISPUTED,)),
            p('''{n}On that road in Mendev you thought of asking what she would have done at the Wound. She was already past you. You let her go.{/n}''',
              requires=(DECLINED,)),
            p('''{n}You had turned her away at the edge of the Wound. She did not come back.{/n}''',
              requires=(CLOSED,), forbids=(SENT_AWAY,)),
            p('''{n}Whatever might have been argued on the platform, under her banner, went unargued. The war took the nights, and then the war was over.{/n}''',
              forbids=(DISPUTED, SENT_AWAY, CLOSED)),
            p('''{n}The Worldwound stayed open. She fought it, as she had always fought it, and you did not see her do it.{/n}''',
              forbids=(WOUND_CLOSED,)),
            p('''{n}The Worldwound closed without you in it. On the night the crusade feasted the victory, a knight of some small order stood at the back of the hall in plain steel, drank nothing, and left before the toasts. Nobody knew her. You did, and did not go after her, and were never sure afterwards whether she had wanted you to.{/n}''',
              requires=(WOUND_CLOSED,), forbids=(SACRIFICE, SENT_AWAY)),
            p('''{n}Her banner stayed at the edge of the Wound where you had planted it, unanswered and unburned, stretched toward a rift you did not enter. She never took it back, and nobody else dared to.{/n}''',
              requires=(CARRIED,), forbids=(SENT_AWAY, WOUND_CLOSED)),
            p('''{n}Her unanswered banner stayed planted beside the closed scar. She had not cast it, and no fire had consumed it.{/n}''', requires=(CARRIED, WOUND_CLOSED), forbids=(SENT_AWAY,)),
            p('''{n}The Sword of Valor flew over Drezen for the rest of your life. Some nights you slept two floors under it, out of habit, and woke with your hand curled round nothing. It showed you nothing more.{/n}''',
              requires=(SENT_AWAY, BANNER_HELD)),
            p('''{n}The Sword of Valor was lost at Iz, and a sock flew in its place over the citadel, because you had put it there. Some nights you slept two floors under it, out of habit, and woke with your hand curled round nothing. A sock remembers nothing.{/n}''',
              requires=(SENT_AWAY, SOCK), forbids=(BANNER_HELD,)),
            p('''{n}The Sword of Valor was lost at Iz, and the pole on the citadel stood empty for the rest of your life. Some nights you climbed up to it, out of habit, and stood under nothing. It showed you nothing more.{/n}''',
              requires=(SENT_AWAY, BANNER_LOST), forbids=(BANNER_HELD, SOCK)),
            p('''{n}You never slept under her banner again, wherever it flew. It showed you nothing more.{/n}''',
              requires=(SENT_AWAY,), forbids=(BANNER_HELD, SOCK, BANNER_LOST)),
            p('''{n}You kept your undertaking about the Herald. When soldiers praised the prison's fall, you named the spite in his execution. She heard the account without returning to your side.{/n}''', requires=(HERALD_ACCOUNTED,)),
        )),
], requires=(), forbids=(COMMITTED, SACRIFICE, RESCUED), RequiresAnyGroups=[[STARTED, SENT_AWAY]], **ALIVE)


page("rescued", "Answered", [
    nar("page", '''{n}You died in the closing Wound. Her banner carried you out to the Lady of Graves' judgment. The death remained in her book; Iomedae accepted liability for the exception. Drezen buried the Commander in an empty coffin.{/n}
{n}Afterwards a knight in plain steel found you on a Mendev road.{/n} "The argument brought me to the edge. I chose to cast the banner. That was not a personal concession." {n}She stopped at the fork.{/n} "You owe me a miracle. I will come when I have decided what to ask."''',
        paragraphs=(
            p('''{n}The Sword of Valor fell into the seam behind you so that nothing could follow. Drezen had to keep its walls with patrols, wards and priests again.{/n}''', requires=(BANNER_HELD,)),
            p('''{n}The cathedral's banner burned beneath your hand. Your palm never closed properly again; the cloth became ash in the closing seam.{/n}''', requires=(ORDER_BANNER,)),
            p('''{n}The power sewn into your body burned in the seam. The soul kept enough to speak in the Lady of Graves' court. The returned body could not wield it.{/n}'''),
            p('''{n}In the ninth year she found you with blood drying on her gauntlets. One of her knights was dying in a Mendev hospice, asking whether his company had held a ford. She could not leave her line.{/n} "Go to him. Tell him what happened. He has earned the truth."
{n}You sat beside him through the night. The ford had fallen after holding an hour longer than expected. In that hour the village emptied onto the road. He heard the names of those who escaped and died before dawn. You brought her his last words. She took off her gauntlets to listen.{/n} "The debt is paid."
{n}She went back to the fighting. You went home by the Mendev road, with the miracle paid and the final appointment still ahead.{/n}'''),
            p('''{n}Every winter she sent you to the houses where those who never recovered from Drezen's madness were kept. You carried water, sat with them and heard their anger. Your admission at the banner had not ended your responsibility.{/n}''', requires=(OWNED_MADNESS,)),
            p('''{n}The cathedral never recovered its stolen cloth. In prayer the canon still blamed the late Commander. Iomedae did not excuse the theft merely because she had heard the case.{/n}''', requires=(COST_STOLEN,)),
            p('''{n}The oath sworn in the cathedral still held. Returning alive had not released you from it.{/n}''', requires=(COST_OATH,)),
            p('''{n}The Lady of Graves had let the stranger go back over on her own terms: the death stands in her book, and there is no appeal at the next appointment. Iomedae answers to her for it.{/n}'''),
            p('''{n}When veterans praised the fight in Baphomet's prison, you told them how you had killed the Herald out of spite. Iomedae never called that admission absolution. Neither did you.{/n}''', requires=(HERALD_ACCOUNTED,)),
            p(HOUSE_FRAME),
        )),
], requires=(RESCUED,), forbids=(CLOSED, COMMITTED))

# --- Registration ------------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the banner and herald reads (SeenCues), the Derived keys and the portrait fallback. Scenes are added by
    expansion.py; the world keys (iz.*, iomedae.key_dies_revealed, seelah.*, sosiel.*, daeran.*, sacrifice, ending.*)
    bind on demand in trickster_world, whose trickster.commander_back carries the bridge world."""
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "SelectedAnswers", {**dict(zip(APPEALS, APPEAL_ANSWERS)), HERALD_SPITE: "e299c81b99cc41d43bfdbc3359810679"})
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("PortraitFallbacks", {}).setdefault("Iomedae", PORTRAIT_GUID)
    # These Iomedae-owned encounters are supplied before this route's hook.
    # E6 reactions require Remote or a native answer list; their local banner
    # meetings are ordinary area encounters, retaining all participant gates.
    for host in payload["Scenes"]:
        if host["Id"] in (E + "react.ix_a.targona", E + "react.ix_a.yaniel"):
            pass  # A100: stays a remote reaction until a hub conversion lands


# Shared flask consumers remain partitioned at their sources. Reconcile
# only this route's named coda, retaining its paragraph positions and exit.
def integrate_joint(payload):
    coda = next(s for s in payload["Scenes"] if s["Id"] == "iomedae.lastcall.page")
    node = coda["Nodes"][0]
    node["Text"] = "{n}Iomedae kept her war. She came to the Commander when it allowed, in plain steel. The flask stayed corked beneath the coat.{/n}"
    crossing = node["Paragraphs"][0]
    crossing["Text"] = "{n}The Commander went into the Wound with a death corked in a flask, and came out across her banner, laid over the fire as her cloak had once lain over a gorge. The flask came out empty. The death stayed in the Lady of Graves' book, as Iomedae had agreed. The stranger carried the empty flask afterwards, corked, out of habit.{/n}"
    node["Paragraphs"].extend([
        p("{n}Her banner stood at the edge of the Worldwound. She stood beside it while the Commander chose what to do.{/n}", requires=(CARRIED,)),
        p("{n}The Commander had never raised her banner at Threshold. There had been no crossing on her cloth, no bargain with the Lady of Graves for a return. Iomedae's visits were her own choice; the flask had its own terms.{/n}", forbids=(CARRIED,)),
        p("{n}Areelu later measured the empty flask and recorded what the Commander had drained from the Wound she created. She had not witnessed the crossing inside the seam or heard its terms from Iomedae.{/n}", requires=(BURIED_ALIVE, H2, "crossroute.areelu.available")),
    ])


# struct2-11: the argument is offered where the Commander raises the banner.
# Iomedae remains its voice; this does not place a divine body in Drezen.


# IOM-A3-02: retain the saved terminal Continue and offer a separate lifetime
# account to every ending eligible for this page, without an intimate gate.
# endings_job4 still moves the reunion's account to its existing morning.
from copy import deepcopy as _struct2_copy
_struct2_after = next(s for s in SCENES if s["Id"] == E + "epilogue.after")
_struct2_page = _struct2_after["Nodes"][0]
_struct2_page["Choices"].append(c("[Read the account of the years that followed, without the vigil.]", "struct2_lifetime_summary"))
_struct2_after["Nodes"].append(nar("struct2_lifetime_summary",
    "{n}The years went on whether or not anyone kept a vigil for them. Iomedae held her line in the east, and what the Commander had answered and carried followed after, as it always does.{/n}",
    paragraphs=_struct2_copy(_struct2_page["Paragraphs"][2:])))
