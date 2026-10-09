"""D2: append inline history readers without changing saved answer targets."""
from copy import deepcopy

from story_format import c, n


# Scene, host, appended node, positive history, negative history, Claude beat.
READERS = (
    ("before_the_end", "climb", "rubric2_purchased_battle",
     ("devarra.tower.one_battle_sold", "devarra.tower.battle_price_accepted"), (),
     "purchased battle breached; predatory collection from the generals before Threshold"),
    ("before_the_end", "climb", "rubric2_voluntary_battle",
     ("devarra.tower.battle_offered",), ("devarra.tower.battle_price_accepted",),
     "voluntary battle fulfilled on her own terms; burned demon column before Threshold"),
    ("the_dwarf", "protect", "rubric2_protection_warning",
     ("devarra.tower.warned",), (), "repeated protection claim answers her earlier once-only warning"),
    *(("the_hoard", host, "rubric2_clutch_debt_" + host,
       ("devarra.trickster.debt_claimed",), (),
       "clutch debt claimed by Commander; she chooses unwelcome coin, not obedience")
      for host in ("honest_her", "steal_her", "ask_her")),
)


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    grouped = {}
    for suffix, host, node, requires, forbids, beat in READERS:
        grouped.setdefault((suffix, host), []).append((node, requires, forbids, beat))
    for (suffix, host), readers in grouped.items():
        scene = scenes["devarra.tower." + suffix]
        if any(node["Id"] == readers[0][0] for node in scene["Nodes"]):
            continue
        target = next(node for node in scene["Nodes"] if node["Id"] == host)
        original = deepcopy(target["Choices"])
        keys = []
        for node_id, requires, forbids, beat in readers:
            key = "devarra.rubric2." + node_id
            payload.setdefault("Derived", {})[key] = [list(requires)]
            if forbids:
                payload.setdefault("DerivedForbids", {})[key] = list(forbids)
            keys.append(key)
            # The host's path/presence guards and each saved answer's gates
            # remain authoritative on both sides of this mandatory readback.
            target["Choices"].append(c("Continue", node_id, requires=(key,)))
            scene["Nodes"].append(n(node_id, "Devarra",
                "[PROSE PENDING: " + beat + "]", *deepcopy(original)))
        for choice in target["Choices"][:len(original)]:
            choice["Forbids"].extend(keys)
