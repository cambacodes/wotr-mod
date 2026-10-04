"""Doc 16 section 4 caps for authored household registrations, without producing pair content."""

CAPS = {3: dict(arcs=3, optional=6, mend=6), 5: dict(arcs=4, optional=16, mend=4, dynamic=3)}


def apply(payload):
    """Only arc starts, optional dynamic flavour and mend attempts read Counts caps.
    Protected dockets and later steps of an already begun arc stay uncapped by Counts.
    Scene metadata names the actual timestamped witness; no synthetic outcome producer is added.
    """
    scenes = [s for s in payload["Scenes"] if s.get("HouseholdCategory")]
    counts = payload.setdefault("Counts", {})
    for chapter, limits in CAPS.items():
        for kind in ("arcs", "mend", "dynamic"):
            if kind not in limits:
                continue
            selected = [s for s in scenes if chapter in s.get("Chapters", range(s["MinChapter"], s["MaxChapter"] + 1))
                        and (s.get("HouseholdArcStart") if kind == "arcs" else s["HouseholdCategory"] == kind)]
            sources = list(dict.fromkeys(s["HouseholdWitness"] for s in selected))
            if len(sources) < limits[kind]:
                continue
            key = "household.cap.ch%d.%s" % (chapter, kind)
            value = dict(Of=sources, Min=limits[kind], Chapters=[chapter])
            if key in counts and counts[key] != value:
                raise ValueError("Conflicting household cap: " + key)
            counts[key] = value
            for scene in selected:
                if key not in scene["Forbids"]:
                    scene["Forbids"].append(key)
