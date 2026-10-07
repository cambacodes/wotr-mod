"""S12: approved ruling 03's authored, limited craft demonstration.

No native confession, living subject, romance or remembered bark is inferred.
The J02 controller publishes only the approved final Nenio -> Camellia failure.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.pair.nenio_camellia."
PAIR = ("nenio", "camellia")
BLOCKERS = ()
SHARED_CRAFT_WITNESS = "household.craft.method_witnessed"


def P(suffix):
    return PREFIX + suffix


# Native voice evidence only: a BarkBanter is not a SeenCue or a dialogue hook.
EVIDENCE = dict(
    path="World/Dialogs/Barkobanters/Banter/NenioCamelia/Banter_NenioCamelia_banter1.jbp",
    guid="58822bc7c77c2784d8ddec8c89be1423",
    keys=("d8e3cc90-795b-499c-9acb-a35ba1ead16d",
          "6d2431cf-e504-4336-a470-ff9cf2d57e3c"),
)

# Current readiness view, not a deed producer or a substitute for RouteOpen.
READY_GROUP = tuple(rel + suffix for rel in PAIR
                    for suffix in (".harem.eligible", ".present_now"))
COMMON_REQUIRES = ("trickster", "trickster.now", "foresight.page_taken",
                   "household.stance_eligible", "household.table.kept") + READY_GROUP
COMMON_FORBIDS = ("household.closed", "fool_king.gone", "trickster.failed", "sacrifice",
                  "engine.l12.commander_unreturned", "nenio.life.unavailable") + tuple(
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

# Ordered reservations retained; the manual approach appends after Later.
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

# Read-only stage views; choices write deeds, never affection.
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


def _nodes(step):
    retry = step["id"] == P("retry")
    choices = [c('"The sample first. Let her show the correction."' if retry else
                 '[Give them the bench; keep the lesson to the sample.]', "lesson")]
    if not retry:
        choices.append(c('"The sample proves what its owner is. Finish there."', "spoiled"))
    choices.extend([c('"Leave the lesson."' if retry else '"No lesson."', "refused"),
                    c("[Later.]", abort=True),
                    c('[Do the bench work while Camellia demonstrates the correction.]', "bench_work")])
    nodes = [
        n("start", "Nenio", '''{n}A dry sample lies on the workbench beside the preparations for the Worldwound march. Nenio has divided a sheet into columns. Camellia keeps the remaining samples beside her own hand.{/n}
"This classification is incomplete. Show me the correction, girl. One sample will do to begin with."''', *choices),
        n("lesson", "Camellia", "[PROSE PENDING: Camellia - keep control of her method / correct the inert sample while the Commander assists / reveal only one limited method]",
          c("[Watch Nenio examine the correction.]", "revision")),
        n("refused", "Camellia", "[PROSE PENDING: Camellia - keep her secrets / take away the unfinished lesson / leave Nenio without the correction]",
          c(flags=step["terminals"]["refused"])),
        n("bench_work", "Narrator", '''{n}You take the tools and hold the dry sample beneath the lamp. The troops' preparations wait while you work. Camellia directs the correction; Nenio watches the sample rather than its owner.{/n}''',
          c("[Follow the correction.]", "manual_correction")),
        n("manual_correction", "Camellia", "[PROSE PENDING: Camellia - expose no more than the same limited method / direct the Commander's correction on the inert sample / surrender one technical advantage to Nenio's scrutiny]",
          c("[Let Nenio check the result.]", "revision")),
        n("revision", "Nenio", '''{n}Nenio examines the corrected sample, then strikes out her first heading and writes another. Camellia removes the remaining samples from her reach.{/n}
"Then the solvent belongs in a different column. Your correction is useful. Your attempt to end the inquiry is less so."
{n}Nenio draws the revised sheet toward herself. The tools you have been working with can finally be put away.{/n}''',
          c("[Finish the lesson.]", flags=step["terminals"]["lesson"])),
    ]
    if not retry:
        nodes.append(n("spoiled", "Camellia",
                       "[PROSE PENDING: Camellia - deny an accusation / remove the sample before the demonstration / leave Nenio's classification unfinished]",
                       c(flags=step["terminals"]["spoiled"])))
    return nodes


def _scene(step):
    return scene(step["id"], "A specimen that answers back", "Nenio", 5,
                 "[Nenio and Camellia: the sample]", _nodes(step),
                 requires=COMMON_REQUIRES + step["requires"],
                 forbids=COMMON_FORBIDS + step["forbids"] + tuple(ENMITY_OVERRIDES),
                 delay=step["delay"], last=5, Relationship="household", Chapters=[5],
                 Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
                 Participants=list(PAIR), ParticipantWomen=[], Pair=list(PAIR),
                 RestAllowance=step["allowance"], HouseholdCategory=step["category"],
                 HouseholdWitness=step["witness"], HouseholdSchedule="S12", HouseholdOrder=5.41,
                 ForbidOverrides={**ENMITY_OVERRIDES, "sacrifice": "trickster.commander_back"})


def register(payload, scenes, refs):
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    derived[P("ready")] = [list(READY_GROUP)]
    # Reuse exactly the loss-specific returns owned by the routes. Latest
    # epochs/closed routes and the J01 current contacts remain authoritative.
    additions = [_scene(step) for step in STEPS]
    for body in additions:
        for woman in PAIR:
            route = payload["Relationships"][woman]
            body["Forbids"] = list(dict.fromkeys([
                *body["Forbids"], *route.get("UnavailableFlags", [])]))
            body["ForbidOverrides"].update(route.get("UnavailableOverrides", {}))
    existing = {body["Id"] for body in scenes}
    scenes.extend(body for body in additions if body["Id"] not in existing)
    for key, groups in LADDER.items():
        derived[key] = [list(group) for group in groups]
        payload.setdefault("DerivedOpenRoutes", {})[key] = list(PAIR)
        blocked = []
        for a, b in (PAIR, PAIR[::-1]):
            guard = P("blocked." + a)
            derived[guard] = [[a + ".harem.enmity." + b]]
            forbids[guard] = [a + ".harem.reconciled." + b]
            blocked.append(guard)
        forbids[key] = blocked
    forbids["nenio.harem.attitude.camellia.rival"].append("nenio.harem.attitude.camellia.respect")
    groups = derived.setdefault(SHARED_CRAFT_WITNESS, [])
    if list(DEED_COSTS) not in groups:
        groups.append(list(DEED_COSTS))
    pending = payload.setdefault("PendingHooks", [])
    for key in (*ENMITY_OVERRIDES, *ENMITY_OVERRIDES.values()):
        if key not in pending:
            pending.append(key)
    household.CONSUMERS.update({body["Id"]: household.PAGE_TAKEN for body in additions})
