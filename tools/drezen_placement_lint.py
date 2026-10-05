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
# F10: these primaries need ordinary merchants that survived the F9 Ch5 load/reload.
# Membership in the area alone also admits the transient Fool King and Legend quartermaster.
F10_MERCHANTS = {"23eabf5b6364d4a4e86202dc5d27600b", "253cdb8f434e5a6469b75e18428316e3",
                 "bc1093231b1577a4485a730c29595195"}
F10_PRIMARIES = {"herrax.presence.rokhorn", "shamira.presence", "eliandra.presence", "jerribeth.presence"}
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
    if at.get("Offset") is not None:   # world-space [dx, dz], as Rules.AnchorOffset
        return float(at["Offset"][0]), float(at["Offset"][1])
    x, z = SIDES[at.get("Side", "left")]
    return x * at["Distance"], z * at["Distance"]


def check(story, table=None):
    table = table or json.loads((ROOT / "tools/drezen_area_chapters.json").read_text(encoding="utf-8"))
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
        at = presence.get("At") or {}
        anchor = at.get("NearUnit")
        # F11: each alternate must survive a genuinely missing primary merchant. No gate changes.
        if key in ("eliandra.presence.mark", "shamira.presence.awning"):
            primary = presences.get("eliandra.presence" if key == "eliandra.presence.mark" else "shamira.presence")
            if not anchor or primary and anchor == (primary.get("At") or {}).get("NearUnit"):
                errors.append(f"{key}: F11 requires an independent persistent fallback anchor")
            if at.get("Side") == "behind":
                errors.append(f"{key}: F11 fallback must avoid roof-prone rear staging")
        if key in F10_PRIMARIES:
            if anchor not in F10_MERCHANTS:
                errors.append(f"{key}: F10 requires an ordinary persistent Ch5 merchant, away from the exotic stall")
            if at.get("Side") not in ("front", "left", "right") or at.get("Offset") is not None:
                errors.append(f"{key}: F10 requires front/side ground staging, not a roof-prone rear offset")
        if key in ("targona.presence", "aranka.presence.yard") and anchor != "15f754455d1d87c42a4e14df456d5415":
            errors.append(f"{key}: F9 yard requires the ordinary capital blacksmith, not the Legend event quartermaster")
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
