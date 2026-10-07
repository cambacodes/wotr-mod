"""S30: authored Eliandra/Targona alliance; hs-D's friend/friend ceiling.

The Angel Wardens report is voice evidence, never a Trickster history input.
Registration owns only this row's Table entry, local witnesses and Ledger recall.
Attitude production belongs to the shared household layer.
"""
from story_format import c, n
from storylines import household, lastcall_ledger, eliandra_trickster
from storylines import targona_opening, targona_trickster


PREFIX = "household.pair.eliandra_targona."
SCENE_ID = PREFIX + "charges"
FRIENDS = ("eliandra.harem.attitude.targona.friend",
           "targona.harem.attitude.eliandra.friend")
ANSWERED = tuple(PREFIX + suffix for suffix in (
    "charges.seen", "charges.answered", "deed.eliandra_named_charges",
    "deed.targona_answered_duty", "cost.eliandra_spent_audience",
    "cost.targona_heard_delay"))
DECLINED = (PREFIX + "charges.seen", PREFIX + "charges.declined")


def nodes():
    return [
        n("start", "Targona", '''{n}Targona has drawn a straight line across the road map. Eliandra sets her cup on it. Outside, a wagon rattles toward the infirmary.{/n}
"Eliandra, I have heard you ask for more time. What will that time change? The demons will not wait while we settle everyone comfortably."
{n}She moves the cup off the line, but leaves the map between them.{/n} "Who is left without a guard? Name them."''',
          c('"Hear who the pursuit leaves behind."', "people"),
          c('"Keep your own tasks."', "declined"),
          c("[Later.]", abort=True), portrait="Targona"),
        n("people", "Eliandra", '''"Odden. The stargazers carrying what we could save from the sanctuary. The wounded who cannot keep pace with a cart. Those are the people I still have to bring home."
{n}Eliandra shifts the map toward Targona and lays a finger across the road.{/n} "Odden can lead them. He cannot fight off demons and get the carts through at the same time. I came here to speak of Pulura's work, and I am spending that audience on this. Hear me before you fly."''',
          c("[Hear Targona's answer.]", "answered"), portrait="Eliandra"),
        n("answered", "Targona", '''{n}Targona looks from Eliandra's finger to the infirmary road outside. She rubs out the end of her line and draws it beside the carts.{/n}
"Then I will watch that road while they pass. I will not send you ahead with people I could have guarded."
{n}She taps the remaining line.{/n} "But once they are through, I want your help finding where I can strike. My brother's light was given to the fight. I will not spend mine waiting without a purpose."
{n}Eliandra takes her cup off the map altogether.{/n} "Bring them through. Then we will look together."''',
          c("[Leave them the map.]", flags=ANSWERED), portrait="Targona"),
        n("declined", "Eliandra", '''{n}Eliandra rolls up the road map. Targona leaves her hand on the table until it has passed beneath her fingers.{/n}
"Very well. I will go back to the stargazers. They still need me."
{n}Targona rises.{/n} "And the wounded need me at the cots. Eliandra, we have not answered each other."
"No. We have not." {n}Eliandra takes the map with her.{/n}''',
          c("[Let them return to their tasks.]", flags=DECLINED), portrait="Eliandra"),
    ]


def register(payload, scenes, refs):
    # make_story is also called repeatedly by save-compatibility tests. Replace
    # only our registrations, so each expansion receives exactly one copy.
    household.ENTRIES[:] = [s for s in household.ENTRIES if s["Id"] != SCENE_ID]
    lastcall_ledger.EXTRA_ENTRIES[:] = [e for e in lastcall_ledger.EXTRA_ENTRIES
                                       if e["Id"] != PREFIX + "seating"]
    # The shared registry defines qualified records for composite seats only.
    # These named single-seat records reuse each route's existing absence terms.
    seats = payload.setdefault("SeatWomen", {})
    for woman, route, overrides in (
        ("eliandra", eliandra_trickster.RELATIONSHIP, {}),
        ("targona", targona_opening.RELATIONSHIP,
         targona_trickster.RELATIONSHIP_PATCH["UnavailableOverrides"]),
    ):
        seats[woman] = dict(Relationship=woman,
                           Requires=[woman + ".present_now"],
                           UnavailableFlags=list(route["UnavailableFlags"]),
                           UnavailableOverrides=dict(overrides))
    payload.setdefault("Derived", {})[PREFIX + "ready"] = [[
        "eliandra.harem.eligible", "targona.harem.eligible", household.KEPT]]
    pending = payload.setdefault("PendingHooks", [])
    reads = (*FRIENDS, "eliandra.harem.enmity.targona", "targona.harem.enmity.eliandra",
             "eliandra.harem.reconciled.targona", "targona.harem.reconciled.eliandra")
    for key in reads:
        if key not in pending:
            pending.append(key)
    household.table_entry(
        SCENE_ID, "The people behind the arrow", "[Eliandra and Targona: the road map]",
        nodes(), ("eliandra", "targona"), PREFIX + "ready",
        requires=(*FRIENDS, "eliandra.met_ch5", "targona.trickster.in_drezen",
                  "eliandra.present_now", "targona.present_now"),
        forbids=(PREFIX + "charges.seen", "trickster.failed", "fool_king.gone",
                 "eliandra.trickster.away", "sacrifice"),
        chapters=(5,), ParticipantWomen=["eliandra", "targona"],
        HouseholdCategory="dynamic", HouseholdWitness=PREFIX + "charges.seen",
        ForbidOverrides={"sacrifice": "trickster.commander_back"})
    lastcall_ledger.EXTRA_ENTRIES.append(dict(
        Id=PREFIX + "seating", Section="Seating Notes", Portrait="Eliandra",
        Title="Eliandra and Targona", Text="{n}The road map at the Table.{/n}",
        Requires=[PREFIX + "charges.seen"], Forbids=[], AnyGroups=[],
        Lines=[
            dict(Text="{n}Eliandra named the stargazers and wounded who needed a guard. Targona heard her and answered before returning to the pursuit. They agreed to look at the map together once the carts were through.{/n}",
                 Requires=list(ANSWERED), Forbids=[], AnyGroups=[]),
            dict(Text="{n}They kept separate tasks.{/n}", Requires=[DECLINED[1]],
                 Forbids=[], AnyGroups=[]),
        ]))
