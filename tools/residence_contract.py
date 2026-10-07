"""W5 residence seating reference for review; never imported by the game/export.

Inputs are already qualified current bodies and first-wins enmity pairs.
This does not grant attendance, stance, ownership, or a return.
"""
from math import dist, inf


CHAMBER = "28a49e115795ed44397b5a1503cef4f0"
# 10b section 4, in this fixed contract order. Scene-transform evidence,
# not a navmesh or live-placement certificate. Exclude the Commander's seat.
SEATS = (
    ("ChadaliLocAfterFight", (-7.23, 0, 1.94)),
    ("EritriceLocAfterFight", (-7.05, 0, 5.50)),
    ("CobblehoofLocAfterFight", (-9.57, 0, 5.87)),
    ("AlichinoLocAfterFight", (-9.01, 0, 1.98)),
    ("SocotLocAfterFight", (-10.14, 0, 3.70)),
    ("CouncilLoc3", (0, 0, 3.92)),
    ("ShykaLocPlayer", (10.22, 0, 1.32)),
    ("EritriceLoc6", (10.01, 0, 8.01)),
    ("EritriceLoc1", (4.08, 0, 12.66)),
)
NATIVE_SPOTS = {
    "chadali": (-12.15, 0, 4.24),
    "eritrice": (5.68, 0, 13.82),
    "shyka": (11.62, 0, 1.73),
    "socothbenoth": (3.02, 0, 6.77),
    "alichino": (-2.41, 0, 15.49),
    "cobblehoof": (-8.90, 0, 9.18),
}


def assign_seats(picker_order, enmities=(), *, seats=SEATS,
                 native_positions=(), fixed_positions=None, capacity=6):
    """Return positions atomically, or refuse the selected set with a reason.

    Fixed positions represent qualified living native Chadali/Eritrice, count
    toward capacity and participate in distance checks. No copies are assigned
    for them. Other native occupants are exclusion positions only.
    """
    selected = tuple(picker_order)
    if capacity not in (4, 6):
        raise ValueError("Use the approved quarters (4) or Chamber (6) capacity")
    if len(set(selected)) != len(selected):
        raise ValueError("A woman cannot occupy two seats")
    if len(selected) > capacity:
        raise ValueError("Too many residents selected")
    fixed = dict(fixed_positions or {})
    if not set(fixed) <= set(selected) or not set(fixed) <= {"chadali", "eritrice"}:
        raise ValueError("Only selected native Chadali/Eritrice retain fixed spots")
    enemies = {frozenset(pair) for pair in enmities}
    if any(len(pair) != 2 for pair in enemies):
        raise ValueError("Enmity requires two distinct women")
    occupied = [*native_positions, *fixed.values()]
    free = [(index, position) for index, (_, position) in enumerate(seats)
            if all(dist(position, other) >= 1.5 for other in occupied)]
    assigned = {}
    for woman in selected:
        hostile = [position for other, position in assigned.items()
                   if frozenset((woman, other)) in enemies]
        if woman in fixed:
            position = fixed[woman]
        else:
            candidates = [(index, position) for index, position in free
                          if all(dist(position, other) >= 1.0 for other in assigned.values())]
            if not candidates:
                raise ValueError("No unoccupied seat remains")
            index, position = min(candidates, key=lambda seat: (
                -min((dist(seat[1], other) for other in hostile), default=inf), seat[0]))
            free = [seat for seat in free if seat[0] != index]
        if any(dist(position, other) < 1.0 for other in assigned.values()):
            raise ValueError("Residents would share a seat")
        if any(dist(position, other) < 8.0 for other in hostile):
            raise ValueError("These two residents need seats at least eight metres apart")
        assigned[woman] = position
    return assigned
