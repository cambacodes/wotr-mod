"""S02 registration, before household copies its entries."""


def register(payload, scenes, refs):
    from storylines import harem_s02, household_pair_seelah_wenduag as sw
    harem_s02.register()
    payload.setdefault("PendingHooks", []).extend(sw.RESERVED_READS)
    # Controller-owned stages read enacted deeds; pair prose writes no attitudes.
    for a, other in (sw.PAIR, sw.PAIR[::-1]):
        # The reviewed pair is separate from the generic friction roster.
        payload["PendingHooks"].extend([a + ".harem.enmity." + other,
                                        a + ".harem.reconciled." + other])
        blocked = sw.P(a + ".enmity_unreconciled")
        payload["Derived"][blocked] = [[a + ".harem.enmity." + other]]
        payload["DerivedForbids"][blocked] = [a + ".harem.reconciled." + other]
        for stage in sw.STAGES:
            key = sw.att(a, other, stage)
            if stage == "rival":
                groups = [["seelah.harem.eligible", "wenduag.harem.eligible"]]
            else:
                rung = next(r for r in sw.LADDER if r["edge"] == (a, other) and r["to"] == stage)
                groups = [[flag] for flag in rung["reads"]]
            payload["Derived"][key] = groups
            payload["DerivedForbids"][key] = [blocked] + list(sw._above(a, other, stage))
