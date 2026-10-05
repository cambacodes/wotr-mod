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

# eng8-q8d: the Chapter 6 exception is the explicit Horzalah coordinator ruling.
BINDING_LIMITS.update({name: {"3": 2, "4": 0, "5": tier, "6": six}
                      for name, tier, six in (("Camellia", 1, 0), ("Galfrey", 1, 0),
                          ("Horzalah", 2, 1), ("Nenio", 1, 0), ("Terendelev", 1, 0))})
DELIVERY_INVENTORY = DEFAULT.with_name("delivery_inventory2_contracts.json")


def delivery_inventory(story, contracts=None):
    """Structural coverage; executed positive histories are mandatory C# tests.

    Mutation/diagnostic fixtures cannot bless a known production overrun.
    Scene metadata alone never claims to have delivered a page.
    """
    contracts = contracts or json.loads(DELIVERY_INVENTORY.read_text(encoding="utf-8"))
    scenes = {s["Id"]: s for s in story["Scenes"]}
    failures = []
    for row in contracts["sites"]:
        scene = scenes.get(row["scene"])
        if scene is None:
            failures.append("missing delivery site " + row["scene"])
            continue
        if row.get("physical") and (remote(scene) or not scene.get("ContactUnit")
                or not (scene.get("InteractionHub") or scene.get("AnswerLists"))
                or scene.get("ManualOnly")):
            failures.append("physical delivery drift " + scene["Id"])
        if "chapters" in row and scene.get("Chapters") != row["chapters"]:
            failures.append("chapter allocation drift " + scene["Id"])
    for row in contracts["retired_reactors"]:
        scene = scenes.get(row)
        if scene is None or "trickster.ever" not in scene.get("Forbids", []):
            failures.append("unretired reactor " + row)
    active = {s["Owner"] for s in story["Scenes"]
              if s["Id"].startswith("galfrey.trickster.react.")
              and "trickster.ever" not in s.get("Forbids", [])}
    if active != set(contracts["reactors"]):
        failures.append("Galfrey reactor allocation drift: " + ",".join(sorted(active)))
    # eng-final Q8-07/Q8-13: explicit retirements have negative coverage;
    # no active production history may use them or be relabelled to hide a failure.
    retired_offers = set(json.loads(DEFAULT.with_name("rescue_endpoint_inventory_contracts.json").read_text(encoding="utf-8"))["retired_offers"])
    retired_histories = contracts.get("retired_histories", [])
    if {h["name"] for h in retired_histories} != {"wenduag-champion", "wenduag-late-bid"}:
        failures.append("retired delivery history coverage drift")
    for history in retired_histories:
        ids = [step["scene"] for step in history["steps"] if step.get("scene")]
        if not ids or any(sid not in retired_offers for sid in ids):
            failures.append("unauthorized retired delivery history: " + history["name"])
        for sid in ids:
            scene = scenes.get(sid, {})
            if "trickster.ever" not in set(scene.get("Requires", [])) & set(scene.get("Forbids", [])):
                failures.append("live retired delivery offer: " + sid)
    for history in contracts["histories"]:
        if any(step.get("scene") in retired_offers for step in history["steps"]):
            failures.append("retired offer in production delivery history: " + history["name"])
        if history.get("expectedFailure") or history.get("diagnostic"):
            failures.append("production history expects failure: " + history["name"])
        if any(set(step) & {"flags", "checkpoint", "pre_age"}
               for step in history["steps"]):
            failures.append("fabricated production history: " + history["name"])
    return failures
# end eng8-q8d


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
    # eng8-q8d: synthetic unit-test stories keep their own fixture contracts.
    if any(s["Id"] == "galfrey.trickster.iz.offer" for s in story["Scenes"]):
        result["hard"].extend(delivery_inventory(story))
    # end eng8-q8d
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
