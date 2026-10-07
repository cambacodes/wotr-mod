"""S18.x: authored captivity account; the unspecified remedy remains blocked.

The private claimant channel needs no respondent romance or Table membership.
The optional household wrapper has two bodily participants, never a prison ghost.
Both exhaust one incident. No truce, affection, enmity or pardon is produced.
See tools/route_packs/harem/s18x.md for verified canon and integration limits.
"""
from story_format import c, n, scene
from storylines import horzalah_trickster as claimant
from storylines import hepzamirah_trickster as respondent

P = "household.docket.horzalah_hepzamirah."
SEEN = P + "account.seen"
# A producerless pending hook reserves choice [0] without inventing a remedy.
REMEDY_READY = P + "captivity_remedy_ready"
WRITES = (SEEN, P + "unsettled", P + "horzalah_captivity_named")


def _nodes(joint=False):
    nodes = [
        n("start", "Horzalah", '''{n}Horzalah catches the edge of the sheet beneath one nail. The scar around her throat tightens as she turns her head.{/n}
"You want to hear about Baphomet's daughters? Write down what one of them did to the other. Hepzamirah lured me into a trap. Locked me in the Ivory Labyrinth. Me!"
{n}Her nail punches through the sheet.{/n}
"If you ever ask me to work with that bitch, remember who locked the door. Write her name."''',
          c('[Present the existing captivity remedy.]', "remedy", requires=(REMEDY_READY,)),
          c('"Your sister\'s name stays on the account. I have not paid it."', "unresolved"),
          c('[Later.]', abort=True)),
        # Kept as a destination for the reserved answer. No delivery witness or
        # effect can appear until the owner specifies a concrete remedy.
        n("remedy", "Horzalah", '"A bargain is not payment for the Ivory Labyrinth. Put that away."',
          c('[Continue.]', "unresolved")),
        n("unresolved", "Horzalah", '''"Good. And if she tells you I escaped, ask her whose trap it was."
{n}Horzalah tears the punctured edge free and leaves the rest beneath your hand.{/n}
"I have enemies to kill. I won't spend the rest of my life rattling her bars for your amusement. Don't offer me business with her and call it forgiveness."''',
          c('[Continue.]', "reply" if joint else None, flags=() if joint else WRITES)),
    ]
    if joint:
        nodes.extend([
            n("reply", "Hepzamirah", '''{n}Hepzamirah looks at the torn sheet, then at her sister's throat.{/n}
"You found a way out. Don't mistake it for a victory over me."
{n}She pushes the scrap back toward Horzalah with one finger.{/n}
"Your precious guild was no use to you in there. Here, your knife is still sharp and the Commander has a war. Use it. I have no intention of kneeling to you."''',
              c('[Continue.]', "named")),
            n("named", "Horzalah", '''"You were always quicker with a lock than a blade."
{n}Horzalah leaves the scrap where it lies. Neither sister reaches for the other's hand.{/n}
"Her name stays. Whatever else you ask us to do against the demons."''',
              c('[Continue.]', flags=WRITES)),
        ])
    return nodes


def register(payload, scenes, refs):
    """Append the row once; shared integration must call this before finalizers."""
    if any(s["Id"] == P + "account" for s in scenes):
        return
    pending = payload.setdefault("PendingHooks", [])
    if REMEDY_READY not in pending:
        pending.append(REMEDY_READY)
    common_requires = ("trickster", "foresight.page_taken", "horzalah.present_now",
                       claimant.WANTS, "horzalah.presence.route_open")
    common_forbids = ("trickster.failed", claimant.CLOSED, claimant.DEAD,
                      claimant.LEFT_FREE, claimant.PRESENCE_FAILED,
                      "horzalah.epoch_unavailable", SEEN)
    private = scene(
        P + "account", "The jailer named", "Horzalah", 5,
        '"What did Hepzamirah do to you?"', _nodes(),
        requires=common_requires, forbids=common_forbids, last=5,
        Relationship="horzalah", Chapters=[5], Areas=[claimant.DREZEN],
        ContactUnit=claimant.UNIT, InteractionHub=claimant.PRESENCE,
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=SEEN)
    table = scene(
        P + "account_table", "The jailer named", "Horzalah", 5,
        '[Horzalah and Hepzamirah: the imprisonment]', _nodes(joint=True),
        requires=common_requires + (
            "household.table.kept", "household.stance_eligible",
            "horzalah.harem.eligible", "hepzamirah.harem.eligible",
            "hepzamirah.present_now", respondent.RET),
        forbids=common_forbids + ("fool_king.gone", respondent.CLOSED,
                                  "hepzamirah.presence.failed", respondent.CONFINED,
                                  "hepzamirah.epoch_unavailable"),
        last=5, Relationship="household", Chapters=[5], Areas=[claimant.DREZEN],
        InteractionHub=claimant.PRESENCE, ContactUnit=claimant.UNIT,
        AdditionalContactUnits=[respondent.BODY_UNIT],
        ForbidOverrides={respondent.CONFINED: respondent.RELEASED},
        Participants=["horzalah", "hepzamirah"], Pair=["horzalah", "hepzamirah"],
        ParticipantWomen=[], RestAllowance="household.protected",
        HouseholdCategory="protected", HouseholdWitness=SEEN)
    scenes.extend([private, table])
    from storylines import foresight
    foresight.CONSUMERS.update({s["Id"]: "foresight.page_taken" for s in (private, table)})
