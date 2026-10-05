"""F7: native Drezen reachability, anchor membership and shared-anchor spacing.

An area guard and a chapter window are conjunctive: a 3..5 window does not
make Drezen accessible during the intervening Abyss chapter. Only reachable
pairs are instantiated; a window with no reachable pair is an error. Explicit
scene Chapters must each be reachable. Native references establish possible
anchor membership, not live visibility, mesh clearance or a successful click.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPITAL = "2570015799edf594daf2f076f2f975d8"
RETURN = "83a099db95e0e6e4485a20b10ce7c28d"
SIDES = {"left": (-1, 0), "right": (1, 0), "front": (0, 1), "behind": (0, -1)}


def exclusive(a, b):
    """Same flag/window proof as Rules.PresencesExclusive; no invented gates."""
    af, bf = set(a.get("Forbids", [])), set(b.get("Forbids", []))
    return (a.get("MaxChapter", 6) < b.get("MinChapter", 1)
            or b.get("MaxChapter", 6) < a.get("MinChapter", 1)
            or bool(set(a.get("Requires", [])) & bf)
            or bool(set(b.get("Requires", [])) & af)
            or any(set(g) <= bf for g in a.get("RequiresAnyGroups", []))
            or any(set(g) <= af for g in b.get("RequiresAnyGroups", [])))


def offset(at):
    x, z = SIDES[at.get("Side", "left")]
    return x * at["Distance"], z * at["Distance"]


def check(story, table=None):
    table = table or json.loads((ROOT / "tools/drezen_area_chapters.json").read_text())
    areas = {a["guid"]: a for a in table["areas"]}
    errors = []
    presences = story.get("Presences", {})
    for key, presence in presences.items():
        area = areas.get(presence.get("Area"))
        if area is None:
            errors.append(f"{key}: area absent from reachability inventory")
            continue
        pairs = [c for c in area["reachable_chapters"]
                 if presence.get("MinChapter", 1) <= c <= presence.get("MaxChapter", 6)]
        if not pairs:
            errors.append(f"{key}: no reachable (area, chapter) pair")
        anchor = (presence.get("At") or {}).get("NearUnit")
        if anchor and anchor not in {u["guid"] for u in area["units"]}:
            errors.append(f"{key}: NearUnit {anchor} absent from {area['name']} native unit list")
    for scene in story.get("Scenes", []):
        if scene.get("Remote") or scene.get("Owner") == "Memory" or scene.get("Owner", "").endswith("Epilogue"):
            continue
        for guid in scene.get("Areas", []):
            if guid not in (CAPITAL, RETURN):
                continue
            reachable = areas[guid]["reachable_chapters"]
            chapters = scene.get("Chapters") or range(scene.get("MinChapter", 1), scene.get("MaxChapter", 5) + 1)
            if not set(chapters) & set(reachable) or scene.get("Chapters") and set(chapters) - set(reachable):
                errors.append(f"{scene['Id']}: unreachable Drezen scene chapter(s)")
    for (ak, a), (bk, b) in itertools.combinations(presences.items(), 2):
        aa, ba = (a.get("At") or {}), (b.get("At") or {})
        if (a.get("Area") != CAPITAL or b.get("Area") != CAPITAL
                or not aa.get("NearUnit") or aa.get("NearUnit") != ba.get("NearUnit")
                or exclusive(a, b)):
            continue
        gap = math.dist(offset(aa), offset(ba))
        if gap < 4 - 1e-6:
            errors.append(f"{ak} / {bk}: shared-anchor spacing {gap:.2f} m < 4 m")
    return sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    failures = check(json.loads(args.story.read_text(encoding="utf-8")))
    print(f"Drezen placement: {len(failures)} hard failures")
    for failure in failures:
        print(failure)
    return int(args.strict and bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
