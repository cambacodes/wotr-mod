"""S12's reviewed craft contract, held at its build sheet's emission stop.

DATA ONLY. The lesson is an authored addition, not a native event. No dialogue,
stage producer or encounter is emitted until the coordinator resolves BLOCKERS.
See tools/route_packs/harem/S12.md for evidence and integration requirements.
"""

PREFIX = "household.pair.nenio_camellia."
PAIR = ("nenio", "camellia")
BLOCKERS = (
    "The approved second tool approach is unallocated.",
    "The integrator's final-failure owner mapping is absent.",
    "The pending/final retry policy is not reconciled for S12.",
)


def P(suffix):
    return PREFIX + suffix


# Native voice evidence only: a BarkBanter is not a SeenCue or a dialogue hook.
EVIDENCE = dict(
    path="World/Dialogs/Barkobanters/Banter/NenioCamelia/Banter_NenioCamelia_banter1.jbp",
    guid="58822bc7c77c2784d8ddec8c89be1423",
    keys=("d8e3cc90-795b-499c-9acb-a35ba1ead16d",
          "6d2431cf-e504-4336-a470-ff9cf2d57e3c"),
)

# Prospective adapter input, not a flag producer or a substitute for RouteOpen.
READY_GROUP = tuple(rel + suffix for rel in PAIR
                    for suffix in (".harem.eligible", ".present_now"))
COMMON_REQUIRES = ("trickster", "foresight.page_taken",
                   "household.stance_eligible", "household.table.kept") + READY_GROUP
COMMON_FORBIDS = ("fool_king.gone", "trickster.failed", "sacrifice") + tuple(
    rel + suffix for rel in PAIR
    for suffix in (".closed", ".epoch_unavailable", ".returned_actor_lost"))
ENMITY_OVERRIDES = {
    a + ".harem.enmity." + b: a + ".harem.reconciled." + b
    for a, b in (PAIR, PAIR[::-1])
}

DEED_COSTS = tuple(P(suffix) for suffix in (
    "deed.camellia_correction", "deed.nenio_revision",
    "cost.camellia_method_shown", "cost.nenio_first_classification_yielded",
    "cost.commander_bench_labour"))

# Ordered node/choice reservations from sheet B, fields 3-5. No live answers.
STEPS = (
    dict(id=P("settle"), delay=0, requires=(P("ready"),),
         forbids=(P("settle.seen"),), witness=P("settle.seen"),
         category="protected", allowance="household.protected", chapters=(5,),
         start=("lesson", "spoiled", "refused", "later"),
         terminals={
             "lesson": (P("settle.seen"), P("settle.done")) + DEED_COSTS,
             "spoiled": (P("settle.seen"), P("settle.failed"),
                         P("cost.commander_lesson_spoiled")),
             "refused": (P("settle.seen"), P("settle.refused"), P("unsettled")),
         }),
    dict(id=P("retry"), delay=48, requires=(P("settle.failed"),),
         forbids=(P("retry.seen"), P("settle.done"), P("unsettled")),
         witness=P("retry.seen"), category="protected",
         allowance="household.protected", chapters=(5,),
         start=("lesson", "refused", "later"),
         terminals={
             "lesson": (P("retry.seen"), P("retry.done"), P("settle.done")) + DEED_COSTS,
             "refused": (P("retry.seen"), P("retry.refused"), P("unsettled")),
         }),
)

# Reader proposals only. The shared integrator owns attitude and enmity writes.
LADDER = {
    "nenio.harem.attitude.camellia.rival": ((P("settle.seen"),),),
    "camellia.harem.attitude.nenio.rival": ((P("settle.seen"),),),
    "nenio.harem.attitude.camellia.respect": (DEED_COSTS[:4],),
}
LEDGER = {
    "kept": (P("settle.done"), "Nenio revised the sample's classification. Camellia kept the rest to herself."),
    "pending": (P("settle.failed"), "The lesson was replaced by an accusation."),
    "final": (P("unsettled"), "The lesson was refused."),
}


def register(payload, scenes, refs):
    """Intentionally inert: the sheet explicitly stops emission at BLOCKERS.

    Do not turn a reservation into a playable, single-approach settlement or
    silently choose a tolerated woman. This also leaves all shared state intact.
    """
    return None
