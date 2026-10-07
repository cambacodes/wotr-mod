"""S29: authored ward visit, hs-D §8d; friend/friend ceiling, no intimacy.

Native anchors verified in blueprints.zip/enGB, 2026-10-07:
KianaAloneAftermath/Cue_0010 e0abe01a6531ec6499f21e44cc81afe6,
80ed53ab-565b-4c0f-bac5-632b286dcde0 (alone, not universal);
ElandKianaAftermath/Cue_0006 a819e8c85ef23324bb0d8117bb9d7df3,
1aef0e95-dc1e-49fa-9852-3fba13bd5e20 (married, not universal).
Both under World/Dialogs/Companions/CompanionQuests/Seelah/Q3_WeightOfMySword.
No native fact changes, echoes, new return or partner agreement. Controller
and later Ledger/Last Call reader attachments remain integrator-owned.
"""
import copy

from story_format import c, n, scene
from storylines import harem_caps, household
from storylines.kiana_trickster import DREZEN

PREFIX = "household.pair.seelah_kiana."
PAIR = ("seelah", "kiana")


def P(key):
    return PREFIX + key


HELPED = tuple(P(key) for key in (
    "ward.seen", "ward.helped", "deed.kiana_named_patient",
    "deed.seelah_followed_healer", "cost.kiana_delayed_private_talk",
    "cost.seelah_worked_ward"))

# Current partner readings have precedence over earlier marriage history.
# These are read-only wrappers, never negotiations or attendance for Elan.
ACCOUNTS = (
    ("exposed", "kiana.partner_secret_exposed", '"Elan knows. I have enough to answer for without having you two look at me over this poor man\'s head."'),
    ("separated", "kiana.separated", '"Elan and I have parted. I told him myself. Please don\'t make me explain it while I\'m trying to stop somebody bleeding."'),
    ("bereaved", "kiana.elan.death_known", '"I miss Elan. Some days I want to talk about him. Today I want this man to get home."'),
    ("share", "kiana.partner_stance.share", '"Elan and I have our own letters to write. Our own evenings, too. Elan\'s terms still stand, Commander. No officers sent to fetch me."'),
    ("secret", "kiana.partner_stance.secret", '"I haven\'t told Elan about us, Commander. Don\'t turn a visit with Seelah into something I can pretend he agreed to."'),
    ("exclusive", "kiana.partner_stance.exclusive", '"What I promised you belongs in our own conversation, Commander. Seelah came to see me, too."'),
    ("reconciled", "kiana.stayed_married", '"Elan and I are still married. I\'ll tell him about this visit myself. He\'ll be delighted to hear Seelah lost an argument to a bandage."'),
    ("elan_current", "kiana.elan.present", '"Elan has his own duties. You can ask me about him without sending somebody to fetch him. Leave the poor man out of this performance."'),
    ("married", "kiana.history_married", '"I was married, Seelah. I haven\'t brought news of Elan today. Please don\'t make up a happier ending because you want to comfort me."'),
)


def ward():
    nodes = [
        n("start", "Kiana", '''{n}Before the next deployment, Kiana meets you and Seelah at the Table with her sleeves rolled up. A hospital orderly waits by the door. Seelah sets down the jug she brought.{/n}
"I was going to steal half an hour with you. The ward has stolen it first. A wounded scout keeps tearing his dressing loose. Come and help me hold him?"''',
          c('"The patient first."', "patient"),
          c('"I\'ll come another time."', "declined"),
          c('[Later.]', abort=True), portrait="Kiana"),
        n("patient", "Kiana", '''{n}In the ward, the scout jerks awake as Kiana unwinds the blood-stiff cloth. Seelah reaches for his shoulder; Kiana puts her hand on his forearm instead.{/n}
"Here. Hold this. He needs two hands more than I need an apology."
{n}Seelah bends closer.{/n}
"Two hands I've got. Tell me where."
{n}Seelah braces the arm as directed. Kiana washes the wound and binds it again, talking the man through the pain. He finally lies still.{/n}''',
          c('[Stay beside the bed.]', "wedding", requires=("kiana.wedding_seen",)),
          c('[Stay beside the bed.]', "postponed", requires=("kiana.history_betrothed",), forbids=("kiana.wedding_seen",)),
          c('[Stay beside the bed.]', "unknown", forbids=("kiana.wedding_seen", "kiana.history_betrothed")), portrait="Kiana"),
        n("private", "Kiana", '''{n}Kiana checks the scout's fingers, then draws Seelah away from his bed.{/n}
"You can bring the jug next time. And stay long enough to hear the princess's new scene. She has a paladin in it now. Very handsome. Useless with bandages until somebody tells her what to do."
{n}Seelah snorts.{/n}
"Ha! Give me a sword and I'll improve the part."
{n}Kiana catches her hand.{/n}
"You can improve it by coming back. I've missed you."
{n}Seelah squeezes her hand. Kiana squeezes back, then releases it to lift the next patient's water cup.{/n}''',
          c('[Leave the jug for their next visit.]', flags=HELPED), portrait="Kiana"),
        n("declined", "Seelah", '''"Then I'll take the other side of the bed."
{n}Seelah picks up her jug and follows Kiana. The orderly opens the door for them; the two women are already arguing about how much of a paladin's training ought to concern bandages.{/n}''',
          c('[Return to your duties.]', flags=(P("ward.seen"), P("ward.declined"))), portrait="Seelah"),
        n("wedding", "Seelah", '''"Kiana, about the wedding. I put you in Sunhammer's way. I still—"
{n}Kiana does not look up from the dressing.{/n}
"I know. And you're holding a man's arm for me instead of standing at the door looking miserable. Keep doing that."
{n}Kiana tests the knot. Seelah watches her hands, then loosens her grip when Kiana nods.{/n}''', c('[Let Kiana speak.]', "account"), portrait="Seelah"),
        n("postponed", "Seelah", '''"I thought we'd be drinking at your wedding before we ever got this far."
{n}Kiana rolls the last strip of cloth between her fingers.{/n}
"So did I. Instead the princess has a postponed wedding and a ward full of soldiers who won't wait for her cue."
{n}Kiana tucks the loose end under the dressing.{/n}
"Don't apologize for a wedding we didn't have. Pass me the clean cloth."''', c('[Pass her the cloth.]', "account"), portrait="Seelah"),
        n("unknown", "Kiana", '''"Don't look so guilty, Seelah. You haven't even spilled the jug yet."
{n}Seelah laughs, quietly enough not to wake the scout. Kiana puts the stained cloth aside.{/n}
"Ask me how I am. You used to be rather good at that."''', c('[Give them time together.]', "account"), portrait="Kiana"),
    ]
    choices = []
    prior = []
    for node_id, flag, text in ACCOUNTS:
        choices.append(c('[Hear her answer.]', node_id, requires=(flag,), forbids=tuple(prior)))
        nodes.append(n(node_id, "Kiana", text, c('[Stay until the dressing is finished.]', "private"), portrait="Kiana"))
        prior.append(flag)
    choices.append(c('[Hear her answer.]', "unsettled", forbids=tuple(prior)))
    nodes.extend([
        n("account", "Seelah", '"And Elan?" {n}Seelah lowers her voice. Kiana keeps her eyes on the sleeping scout.{/n}', *choices, portrait="Seelah"),
        n("unsettled", "Kiana", '"I haven\'t an answer for you about Elan today. Don\'t supply one for me. I came to see my friend, and I mean to keep her for a little while."', c('[Stay until the dressing is finished.]', "private"), portrait="Kiana"),
    ])
    return scene(P("ward"), "The next patient", "Seelah", 5,
                 '[Seelah and Kiana: the ward before deployment]', nodes,
                 requires=("trickster", "foresight.page_taken", "household.table.kept",
                           "household.stance_eligible", P("ready"),
                           "seelah.harem.eligible", "kiana.harem.eligible",
                           "seelah.harem.attitude.kiana.friend", "kiana.harem.attitude.seelah.friend",
                           "seelah.present_now", "kiana.present_now", P("conscious"), P("met")),
                 forbids=("fool_king.gone", "trickster.failed", P("ward.seen"),
                          "kiana.presence.failed", "seelah.harem.enmity.kiana", "kiana.harem.enmity.seelah"),
                 last=5, Relationship="household", Areas=[DREZEN], Chapters=[5],
                 InteractionHub="household.table", Participants=list(PAIR), ParticipantWomen=list(PAIR), Pair=list(PAIR),
                 ForbidOverrides={a + ".harem.enmity." + b: a + ".harem.reconciled." + b for a, b in (PAIR, PAIR[::-1])},
                 HouseholdCategory="dynamic", HouseholdWitness=P("ward.seen"), RestAllowance="household.pair")


def register(payload, scenes, refs):
    """Call before household integration/caps; no writes to controller state."""
    derived = payload.setdefault("Derived", {})
    derived.update({
        P("ready"): [["seelah.harem.eligible", "kiana.harem.eligible", "household.table.kept"]],
        P("met"): [["kiana.aftermath_seen"], ["kiana.trickster.met"], ["kiana.trickster.returned"]],
        P("soul_clear"): [["availability.observed"]],
        P("conscious"): [["seelah.souls_returned"], ["kiana.trickster.returned"], [P("soul_clear")]],
    })
    payload.setdefault("DerivedForbids", {})[P("soul_clear")] = ["kiana.possessed", "kiana.soul_lost"]
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (a + ".harem.attitude." + b + ".friend",
                    a + ".harem.enmity." + b, a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    # Single-woman qualified seats copy the existing relationship's narrow
    # overrides and epoch loss. No other woman's presence can veto this row.
    for woman in PAIR:
        if woman not in payload.setdefault("SeatWomen", {}):
            rel = payload["Relationships"][woman]
            payload["SeatWomen"][woman] = dict(
                Relationship=woman, Requires=[woman + ".present_now"],
                UnavailableFlags=list(dict.fromkeys(rel.get("UnavailableFlags", []) + rel.get("EpochUnavailableFlags", []))),
                UnavailableOverrides=copy.deepcopy(rel.get("UnavailableOverrides", {})))
    if not any(s["Id"] == P("ward") for s in scenes):
        scenes.append(ward())
    if scenes is not payload["Scenes"] and not any(s["Id"] == P("ward") for s in payload["Scenes"]):
        payload["Scenes"].append(ward())
    household.CONSUMERS[P("ward")] = household.PAGE_TAKEN
    harem_caps.apply(payload)
