"""S05: historical acknowledgment of Nocticula and Shamira's existing bond.

Authored RRT addition; native evidence is recorded in harem/s05.md. The
reviewed sheet blocks live replies until channel dispatch is supplied and
coup reconciliation until a real exposure producer is supplied. Neither
affair discovery nor Socothbenoth's exposed plan supplies those contracts.
This module emits only the sheet's history-only branch. It grants no body,
partner agreement, affection, enmity, return or reconciliation.
"""
from story_format import c, n, scene


P = "household.pair.nocticula_shamira."
LOVERS_SEEN = P + "lovers_seen"
LOVERS_CUE = "216d0445992d7f845a9fe32ffdb381d7"
SLOT_ID = P + "return.explicit.1"

# Editorial reservation only. Never inserted into an emitted scene: none of
# the verified Ch5 channels establishes two freely choosing bodies together.
BLOCKED_SLOT = n(
    "return.explicit.1", "Narrator",
    "{n}Their private audience ends. Neither has yielded her claim on the court.{/n}",
    c(),
)


def historical_scene():
    """No current speaker is inferred from a remembered, actually seen cue."""
    return scene(
        P + "precedence", "The place beside the throne", "Narrator", 5,
        '[Recall Shamira\'s account of her place beside Nocticula.]',
        [n("start", "Narrator", """{n}At the corner table, you turn back to your account of the Ardent Dream. Beyond the tavern doors, a patrol hurries toward Drezen's walls. Shamira had named herself Nocticula's chosen lover and described the queen's visits to her Harem, away from the plots of the Midnight Isles.
The account ends there. There is no answer from either court beside it.{/n}""",
           c('[Keep the account of their existing bond.]', "history"),
           c('[Later.]', abort=True)),
         n("history", "Narrator", """{n}You leave both names in the account. Beside them, the space for a reply remains empty.{/n}""",
           c(flags=(P + "precedence.seen", P + "historical")))],
        requires=("trickster", "foresight.page_taken", "household.stance_eligible",
                  "household.table.kept", LOVERS_SEEN),
        forbids=("trickster.failed", "fool_king.gone", P + "precedence.seen"),
        last=5, Chapters=[5], Relationship="household",
        Areas=["2570015799edf594daf2f076f2f975d8"],
        InteractionHub="household.table", Participants=[], ParticipantWomen=[],
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=P + "precedence.seen",
    )


def register(payload, scenes, refs):
    """Append S05 once; leave every existing scene and native binding intact."""
    bindings = payload.setdefault("SeenCues", {})
    if LOVERS_SEEN in bindings and bindings[LOVERS_SEEN] != [LOVERS_CUE]:
        raise ValueError("Conflicting S05 lover-knowledge binding")
    bindings[LOVERS_SEEN] = [LOVERS_CUE]
    if not any(s["Id"] == P + "precedence" for s in scenes):
        scenes.append(historical_scene())
    # The loader normally receives payload['Scenes']; permit an independent
    # construction list without registering duplicate identities.
    if scenes is not payload["Scenes"] and not any(
            s["Id"] == P + "precedence" for s in payload["Scenes"]):
        payload["Scenes"].append(historical_scene())
    from storylines import foresight
    foresight.CONSUMERS[P + "precedence"] = "foresight.page_taken"
