"""ER-A1-RETURN: a played, voluntary debate after the completed sitting."""
from story_format import c, n, p, scene


OPENING = "eritrice.trickster.reconciled_debate"


def integrate(payload):
    from storylines import eritrice_trickster as route
    if any(s["Id"] == OPENING for s in payload["Scenes"]):
        return
    payload["Scenes"].append(scene(OPENING, "", "Eritrice", 5, "Continue", [
        n("open", "Eritrice", "[PROSE PENDING: voluntary new private debate after completed reconciliation]",
          c("[PROSE PENDING: accept the private debate]", "exchange"),
          c("[PROSE PENDING: refuse the private debate]", abort=True),
          paragraphs=(p("[PROSE PENDING: read the standing extraction grudge before the new debate]",
                        requires=(route.ON_AGENDA,)),)),
        n("exchange", "Eritrice", "[PROSE PENDING: play the first honest objection and her counterargument; preparation only]",
          c("Continue", "record", flags=(route.STARTED, route.MINUTES_READ, route.STRAIGHT))),
        n("record", "Eritrice", "[PROSE PENDING: enter the new private debate in the minutes; no commitment yet]"),
    ], requires=("trickster.now", route.RETURNED, route.VISIT),
       forbids=(route.CLOSED, route.MINUTES_READ, route.DECLINED, OPENING),
       last=5, Relationship="eritrice", Areas=[route.DREZEN],
       ContactUnit=route.UNIT, InteractionHub="eritrice.presence", optional=True))
    # Book presentation may auto-start a relationship on entry. The performed
    # exchange, rather than that presentation side effect, unlocks this reading.
    point = next(s for s in payload["Scenes"] if s["Id"] == "eritrice.minutes.point_one.drezen")
    point["Requires"].append(route.MINUTES_READ)
