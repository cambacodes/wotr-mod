"""Authored S04 vigil: suspicion is not discovery, and a prayer is not absolution.

Source: hs-A/S04 and harem-lore-check/S04. The reviewed sheet explicitly
withholds the Religion DC, confession producer and retry contract. Reserve
their answer positions without fabricating checks, evidence or resolution.
PendingHooks below are authoring blockers, never new player-earned gates.
"""
import copy

from story_format import c, n
from storylines import household, foresight

P = "household.pair.seelah_camellia."
BLOCKERS = (P + "contract.religion", P + "contract.confession", P + "contract.resolution")


def build_scene():
    # _table_scene has no ENTRIES side effect: make_story can be called twice.
    # Participants supplies route openness; present_now supplies current epochs.
    # life.available keeps Camellia's narrowly paid body overrides, rather than
    # treating her generic returned history as permission to attend.
    return household._table_scene(
        P + "settle", "An unfinished prayer", "Seelah",
        '[Seelah and Camellia: the prayer for the dead.]', [
            n("start", "Seelah", '''{n}Seelah clears the cups from the corner table. A crusader's cracked shield rests against her chair; she sets a candle beside it. Camellia reaches past her to straighten the cloth.{/n}
"You can leave that. I want to finish the prayer before we go back to the walls."
{n}Camellia folds her hands and inclines her head. Seelah stops with her fingers on the candle.{/n}
"And don't make that curtsy at me. I can fight beside you. That doesn't mean I like what I sense in you."''',
              c('[Lore (Religion): distinguish mercy from a blessing.]', "awaiting",
                requires=(BLOCKERS[0],)),
              c('[Present the confession you kept.]', "awaiting",
                requires=(BLOCKERS[1],)),
              household.word_made_true('[Word Made True.]', "word", use="seelah_camellia"),
              c('"Then leave the blessing unsaid."', "refused"),
              c('[Later.]', abort=True), portrait="Seelah"),
            n("awaiting", "Seelah", '''"No. Not on that argument."
{n}Seelah keeps her hand on the unlit candle.{/n}''',
              c('[Later.]', abort=True), portrait="Seelah"),
            n("word", "Seelah", '''{n}The candle catches without a flame touching its wick. Seelah looks sharply at you, then turns the shield toward the light.{/n}
"I heard that. You can stop an argument with your tricks. You can't put a blessing in my mouth."
{n}Camellia lets her curtsy deepen, then rises without waiting for Seelah's hand.{/n}
"How fortunate. I had not asked for one. Shall we get back to killing demons, or must I disappoint you further?"
"Demons," {n}Seelah says.{/n} "And the prayer is for the people they killed."''',
              c('[Leave the blessing withheld.]', flags=(
                  P + "settle.seen", P + "resolved", P + "seelah_blessing_withheld",
                  P + "camellia_cover_limited", P + "cost.seelah_company_kept",
                  P + "cost.camellia_public_cover", P + "method.word")), portrait="Seelah"),
            n("refused", "Camellia", '''"Such solemnity over a little courtesy. Perhaps I should have brought flowers."
{n}Camellia draws her hand back from the cloth. Her smile holds; her fingers close hard enough to whiten the knuckles.{/n}
"Leave them for the dead," {n}Seelah says. She takes the shield and stands.{/n} "Come on. There's still a wall to hold."
{n}Camellia lifts her wine before the candle can spill into it. The prayer remains unfinished.{/n}''',
              c('Continue', flags=(P + "settle.seen", P + "permanent_refusal", P + "unsettled")),
              portrait="Camellia"),
        ], requires=("trickster", household.KEPT, household.eligible("seelah"),
                     household.eligible("camellia"), "seelah.present_now", "camellia.present_now",
                     "camellia.life.available", P + "seelah_body", P + "camellia_body"),
        forbids=(household.KING_GONE, "trickster.failed", P + "settle.seen",
                 "seelah.closed", "camellia.closed",
                 household.enmity("seelah", "camellia"), household.enmity("camellia", "seelah")),
        chapters=(5,), Pair=["seelah", "camellia"], Participants=["seelah", "camellia"],
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=P + "settle.seen", ForbidOverrides={
            household.enmity("seelah", "camellia"): "seelah.harem.reconciled.camellia",
            household.enmity("camellia", "seelah"): "camellia.harem.reconciled.seelah",
        })


def register(payload, scenes, refs):
    """Register only this row; attitude and first-wins writes belong to the owner."""
    body = build_scene()
    # A failed returned-copy placement cannot stand in for a body. It does not
    # veto an independently living native companion in the capital, however.
    for woman, losses, returned in (
            ("seelah", ["seelah_dead", "seelah_gone"], "seelah.trickster.returned"),
            ("camellia", ["camellia.killed", "camellia.dead", "camellia.kicked_out"],
             "camellia.trickster.veiled_available")):
        key = P + woman + "_native_body"
        payload.setdefault("Derived", {})[key] = [[woman + ".present_now"]]
        payload.setdefault("DerivedForbids", {})[key] = losses
        back = P + woman + "_returned_body"
        payload["Derived"][back] = [[woman + ".present_now", returned]]
        payload["DerivedForbids"][back] = [woman + ".presence.failed"]
        payload["Derived"][P + woman + "_body"] = [[key], [back]]
    # The lore audit requires reviewed discovery/DC/retry authority before any
    # resolution is emitted, including the otherwise contracted Word approach.
    body["Nodes"][0]["Choices"][2]["Requires"].append(BLOCKERS[2])
    if not any(s["Id"] == body["Id"] for s in payload["Scenes"]):
        payload["Scenes"].append(copy.deepcopy(body))
    pending = payload.setdefault("PendingHooks", [])
    # The first helper consumer also declares its existing read-only runtime
    # symbol to the export's known-condition inventory. Rules.Complete supplies
    # its counted value; no choice produces it and no limit is changed.
    for key in BLOCKERS + (household.WMT_AVAILABLE,):
        if key not in pending:
            pending.append(key)
    foresight.CONSUMERS[body["Id"]] = household.PAGE_TAKEN
