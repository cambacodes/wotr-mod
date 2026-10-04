"""E-Q7-17: binding per-woman remote ledger, independent of rotation keys.

Count completed deliveries in one traversed history, never a union of alternate
worlds. Static audit sequences are reported separately until a route walker
supplies a trace. Memory/Table allocations must name their actual serialized
owner; changing a title or relationship is not an exemption.
"""
import argparse
import json
from pathlib import Path

DEFAULT = Path(__file__).with_name("remote_allocation_contracts.json")
# Binding ledger values: changing a contract cannot grant a larger allocation.
BINDING_LIMITS = {"Irabeth": {"3": 2, "4": 0, "5": 1, "6": 0},
                  "Shamira": {"3": 2, "4": 0, "5": 2, "6": 0},
                  "Wenduag": {"3": 2, "4": 0, "5": 1, "6": 0}}


def remote(scene):
    return bool(scene.get("Remote")) or scene.get("Owner") == "Memory"


def belongs(scene, allocation):
    return (scene.get("Relationship") in allocation["relationships"]
            or scene.get("Owner") in allocation["owners"]
            or any(scene["Id"].startswith(p) for p in allocation.get("prefixes", [])))


def count_history(story, allocation, chapter, deliveries):
    """The caller records each delivered scene ID and its chapter at execution.

    Abort/revisit displays are not additional completed pages. Repeated complete
    IDs are invalid (Rules.Available prevents them), not silently deduplicated.
    Mutually exclusive twins naturally count once in a valid history.
    """
    scenes = {s["Id"]: s for s in story["Scenes"]}
    pages, invalid = [], []
    for sid in deliveries:
        scene = scenes.get(sid)
        if scene is None:
            invalid.append("unknown delivery " + sid)
            continue
        if not belongs(scene, allocation) or not remote(scene):
            continue
        if sid in pages:
            invalid.append("repeated completion " + sid)
            continue
        if (not scene.get("MinChapter", 1) <= chapter <= scene.get("MaxChapter", 5)
                or scene.get("Chapters") and chapter not in scene["Chapters"]):
            invalid.append("delivery outside chapter window " + sid)
        pages.append(sid)
    limit = allocation["limits"][str(chapter)]
    result = {"character": allocation["character"], "chapter": chapter,
              "pages": pages, "count": len(pages), "limit": limit,
              "ledger_row": allocation["ledger_row"], "invalid": invalid}
    result["failure"] = bool(invalid or len(pages) > limit)
    return result


def lint(story, contracts=None, histories=None):
    contracts = contracts or json.loads(DEFAULT.read_text(encoding="utf-8"))
    result = {"hard": [], "review": [], "histories": [], "findings": []}
    allocations = {a["character"]: a for a in contracts["allocations"]}
    for name, a in allocations.items():
        if any(type(x) is not int or x < 0 for x in a["limits"].values()) or not a["ledger_row"]:
            result["hard"].append(name + ": malformed binding allocation")
        if name in BINDING_LIMITS and a["limits"] != BINDING_LIMITS[name]:
            result["hard"].append(name + ": allocation differs from binding ledger " + a["ledger_row"])
    # Passed traces are acceptance evidence; catalog sequences are diagnostic
    # witnesses only, because the linter cannot certify native event delivery.
    for h in histories if histories is not None else contracts.get("audit_sequences", []):
        row = count_history(story, allocations[h["character"]], h["chapter"], h["deliveries"])
        row.update(history=h["name"], evidence="executed_trace" if histories is not None else "audit_sequence")
        result["histories"].append(row)
        if row["failure"]:
            (result["hard"] if histories is not None else result["review"]).append(row)
    ids = {s["Id"] for s in story["Scenes"]}
    for c in contracts["findings"]:
        row = dict(c)
        row["status"] = "not_in_export" if c["scene"] not in ids else "checked_by_character_ledger"
        result["findings"].append(row)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--story", default=str(DEFAULT.parents[1] / "development/Story.json"))
    ap.add_argument("--histories", type=Path, help="completed delivery traces from route walkers")
    args = ap.parse_args(argv)
    histories = json.loads(args.histories.read_text(encoding="utf-8")) if args.histories else None
    report = lint(json.loads(Path(args.story).read_text(encoding="utf-8")), histories=histories)
    print(json.dumps(report, indent=2))
    return bool(report["hard"])


if __name__ == "__main__":
    raise SystemExit(main())
