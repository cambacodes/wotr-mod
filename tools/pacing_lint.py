"""Pacing lint (handoff 13 section 6): per-woman beat counts by chapter, plus the pacing pass's hard rules.

Reads the generated story (development/Story.json) and the availability map (tools/pacing-availability.json).

Findings:
  REVIEW  she is present in a chapter (availability map) where her built route starts no beat, and the chapter has
          no coordinator exception. A warning for the route owner; it never fails the build.
  WARN    she is in person in Chapter 4, and every beat her route starts there is remote.
  HARD    (fails, exit 1)
          H1  a Ch1-2 scene reads `trickster`/`trickster.ever` or carries Trickster content (device, Trickster state,
              Trickster mythic entry or choice).
          H2  a Ch1-2 scene sets a CommittedFlag, or the StartedFlag of a Trickster route (a relationship whose
              StartedFlag no Ch3+ path-neutral scene sets). When the availability map is given, the StartedFlag rule
              covers the roster's routes only: a framework relationship outside the roster (the Long Con, doc 15 section 7,
              which starts at Chaleb's pyre in Ch1 and is no romance) is not a Trickster route.
          H3  a Ch1-2 scene sets a native key (an etude, quest, cue, answer, dialog or native flag binding), or any
              scene sets a key bound to a native or parent-mod romance etude (13 section 0).
          H4  a Ch1-2 scene reads or sets another relationship's CommittedFlag or a harem flag (`<rel>.harem...`).
  SCHEMA  the availability map is malformed or does not match the roster (exit 2).

A "Ch1-2 scene" is a non-epilogue scene whose chapter window opens at Chapter 2 or earlier (a Prologue scene,
chapter 0, counts as Chapter 1). A beat counts in the chapter where its window opens ("starts"); the chapters where
it is still open are reported alongside. Chapter windows follow Rules.Available (src/Story.cs): the Chapters list
when present, otherwise MinChapter..MaxChapter.

The roster source of truth is Writer/handoffs/trickster-matrix.json (43 characters). The availability map carries
a `_roster` snapshot of it so the lint still runs where the Writer folder is absent; when the matrix is found, the
snapshot must match it.
"""
import argparse
import collections
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORY = ROOT / "development" / "Story.json"
DEFAULT_AVAILABILITY = ROOT / "tools" / "pacing-availability.json"
DEFAULT_MATRIX = ROOT.parent / "Writer" / "handoffs" / "trickster-matrix.json"

CHAPTERS = ("1", "2", "3", "4", "5", "6")
MODES = ("ip", "remote")
TRICKSTER_KEYS = {"trickster", "trickster.ever"}
GUID = re.compile(r"\b[0-9a-f]{32}\b")
HAREM = re.compile(r"(^|\.)harem(\.|$)")

# 13 section 0: native romance etudes (Camellia, Arueshalae, Wenduag, Galfrey) and the parent mod's romance states.
ROMANCE_ETUDES = {
    "89f8c2f1a7a8ea24794bf4af231e89a1": "CamelliaRomance",
    "fe6ee37b2aa394e4eaa51208cf7d7f86": "CamelliaRomance_PreStart",
    "e49702f590611644580f09c8f9ef0e5b": "CamelliaRomance_Start",
    "d6a90c0f6536331498cafa1f3195d886": "ArueshalaeRomance",
    "6a3fdd0758fe78d4aa2c3b26d7614fbc": "ArueshalaeRomance_Active",
    "543a6e475aeb9bf4eafb43903e3e186b": "ArueshalaeRomance_Fail",
    "39c388b5f2ab0f14b90030bab1b676b9": "WenduagRomance",
    "33c4c2f66f2461e4993df21566252079": "WenduagRomance_Active",
    "133842cc9812fc74f88a21e12ec2c6f8": "GalfreyRomance",
    "c9358d866e0b3844b8d72536ca60e4b4": "GalfreyRomance_Active",
    "2e98dbe685f045cdabf88b66e4cde9ff": "parent Aranka romance",
    "9f655e252d334f04884f10188b0d8928": "parent Nurah romance",
    "b5c19cd01e364df99f6c946c7da14751": "parent Minagho romance",
    "80cb9c6f466b4eaaaa9561ca56c5f348": "parent Targona romance",
    "18affced672d4c56a52bf6ffc00601b9": "parent Nocticula romance",
}
# Story.json maps whose keys are native bindings (Rules.IsNativeFlag plus the permanent etudes).
NATIVE_MAPS = ("Etudes", "CompletedEtudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs",
               "UnlockableFlags", "QuestObjectives", "StartedQuests", "InventoryItems")


class SchemaError(Exception):
    pass


def load_json(path):
    with open(path, encoding="utf-8-sig") as handle:
        return json.load(handle)


def is_epilogue(scene):
    return scene["Owner"].endswith("Epilogue")


def is_remote(scene):
    return bool(scene.get("Remote")) or scene["Owner"] == "Memory"


def relationship_of(scene):
    return scene.get("Relationship") or "tirabade"   # Story.cs Scene.Relationship default


def window(scene):
    """The chapters in which Rules.Available can pass; the Prologue (0) folds into Chapter 1."""
    if scene.get("Chapters"):
        chapters = scene["Chapters"]
    else:
        chapters = range(scene["MinChapter"], min(scene["MaxChapter"], 6) + 1)
    return sorted({max(1, c) for c in chapters if c <= 6})


def is_early(scene):
    chapters = window(scene)
    return not is_epilogue(scene) and bool(chapters) and chapters[0] <= 2


def choices(scene):
    return [choice for node in scene["Nodes"] for choice in node.get("Choices", [])]


def reads(scene):
    keys = set(scene.get("Requires", [])) | set(scene.get("Forbids", [])) | set(scene.get("RequiresAny", []))
    keys |= {key for group in scene.get("RequiresAnyGroups", []) for key in group}
    overrides = scene.get("ForbidOverrides") or {}
    keys |= set(overrides) | set(overrides.values())
    for choice in choices(scene):
        keys |= set(choice.get("Requires", [])) | set(choice.get("Forbids", []))
    for node in scene["Nodes"]:
        for paragraph in node.get("Paragraphs") or []:
            keys |= set(paragraph.get("Requires") or []) | set(paragraph.get("Forbids") or [])
    return keys


def sets(scene):
    return {key for choice in choices(scene) for key in choice.get("Set", [])}


def trickster_gated(scene):
    requires_any = set(scene.get("RequiresAny", []))
    return (bool(TRICKSTER_KEYS & set(scene.get("Requires", [])))
            or bool(requires_any) and requires_any <= TRICKSTER_KEYS
            or any(group and set(group) <= TRICKSTER_KEYS for group in scene.get("RequiresAnyGroups", []))
            or bool(scene.get("TricksterDevice")))


def trickster_content(scene):
    why = sorted(TRICKSTER_KEYS & reads(scene))
    if scene.get("TricksterDevice"): why.append("TricksterDevice")
    if scene.get("TricksterState"): why.append("TricksterState " + scene["TricksterState"])
    if scene.get("EntryMythic") == "Trickster": why.append("EntryMythic Trickster")
    if any(choice.get("Mythic") == "Trickster" for choice in choices(scene)): why.append("choice Mythic Trickster")
    return why


# ---------------------------------------------------------------- availability schema and roster

def roster_from_matrix(matrix):
    return [{"character": row["character"], "relationship": row.get("relationship_id")} for row in matrix["characters"]]


def validate_availability(availability, roster):
    """Raise SchemaError listing every problem; returns the entries (key -> entry)."""
    problems = []
    if not isinstance(availability, dict):
        raise SchemaError("availability map must be a JSON object")
    entries = {key: value for key, value in availability.items() if not key.startswith("_")}
    by_name = collections.defaultdict(list)
    for key, entry in entries.items():
        if not isinstance(entry, dict):
            problems.append("%s: entry must be an object" % key)
            continue
        by_name[entry.get("character")].append(key)
    wanted = {row["character"]: row.get("relationship") for row in roster}
    for name in wanted:
        if name not in by_name:
            problems.append("missing entry for roster character %r" % name)
        elif len(by_name[name]) > 1:
            problems.append("roster character %r has %d entries: %s" % (name, len(by_name[name]), sorted(by_name[name])))
    for name, keys in by_name.items():
        if name not in wanted:
            problems.append("extra entry %s: %r is not a roster character" % (sorted(keys), name))
    for key, entry in entries.items():
        if not isinstance(entry, dict):
            continue
        where = key
        present = entry.get("present")
        if not isinstance(present, dict):
            problems.append("%s: 'present' must be an object of chapter -> mode" % where)
            present = {}
        for chapter, mode in present.items():
            if chapter not in CHAPTERS:
                problems.append("%s: bad chapter key %r (only \"1\"..\"6\")" % (where, chapter))
            if mode not in MODES:
                problems.append("%s: bad mode %r in chapter %s (only ip or remote)" % (where, mode, chapter))
        exceptions = entry.get("exceptions", {})
        if not isinstance(exceptions, dict):
            problems.append("%s: 'exceptions' must be an object" % where)
            exceptions = {}
        for chapter, reason in exceptions.items():
            if chapter not in present:
                problems.append("%s: exception for chapter %r where she is not present" % (where, chapter))
            if not isinstance(reason, str) or not reason.startswith("none: ") or len(reason) <= len("none: "):
                problems.append("%s: exception for chapter %s must read \"none: <reason>\"" % (where, chapter))
        evidence = entry.get("evidence")
        if not isinstance(evidence, dict):
            problems.append("%s: 'evidence' must be an object" % where)
            evidence = {}
        if present and not GUID.search(str(evidence.get("first_met", ""))):
            problems.append("%s: evidence.first_met must cite a native GUID" % where)
        for chapter in present:
            if chapter in CHAPTERS and not GUID.search(str(evidence.get(chapter, ""))):
                problems.append("%s: present in chapter %s without evidence (a native GUID) in evidence.%s" % (where, chapter, chapter))
        if not isinstance(entry.get("verify", False), bool):
            problems.append("%s: 'verify' must be true or false" % where)
        verify_chapters = entry.get("verify_chapters", [])
        if not isinstance(verify_chapters, list) or any(c not in present for c in verify_chapters):
            problems.append("%s: 'verify_chapters' must list present chapters" % where)
        elif verify_chapters and entry.get("verify") is not True:
            problems.append("%s: verify_chapters set but verify is not true" % where)
        routes = entry.get("routes")
        if not isinstance(routes, list) or not all(isinstance(r, dict) and isinstance(r.get("relationship"), str) for r in routes):
            problems.append("%s: 'routes' must be a list of {relationship, owners?}" % where)
        else:
            expected = wanted.get(entry.get("character"))
            if expected and expected not in {r["relationship"] for r in routes}:
                problems.append("%s: routes do not include the roster relationship %r" % (where, expected))
            for route in routes:
                owners = route.get("owners")
                if owners is not None and (not isinstance(owners, list) or not all(isinstance(o, str) for o in owners)):
                    problems.append("%s: route %s owners must be a list of names" % (where, route["relationship"]))
    if problems:
        raise SchemaError("\n".join(problems))
    return entries


def resolve_roster(availability, matrix_path, notes):
    snapshot = availability.get("_roster") if isinstance(availability, dict) else None
    if matrix_path and Path(matrix_path).is_file():
        roster = roster_from_matrix(load_json(matrix_path))
        if len(roster) != len({row["character"] for row in roster}):
            raise SchemaError("roster source %s repeats a character" % matrix_path)
        if snapshot is not None and sorted(map(json.dumps, snapshot)) != sorted(map(json.dumps, roster)):
            raise SchemaError("availability _roster snapshot differs from %s; refresh the snapshot" % matrix_path)
        notes.append("roster: %d characters from %s" % (len(roster), matrix_path))
        return roster
    if not isinstance(snapshot, list):
        raise SchemaError("no roster: trickster-matrix.json not found and the availability map has no _roster snapshot")
    notes.append("roster: %d characters from the availability _roster snapshot (trickster-matrix.json not found)" % len(snapshot))
    return snapshot


# ---------------------------------------------------------------- beats and findings

def route_scenes(story, routes):
    for scene in story["Scenes"]:
        if is_epilogue(scene):
            continue
        for route in routes:
            owners = route.get("owners")
            if relationship_of(scene) == route["relationship"] and (owners is None or scene["Owner"] in owners):
                yield scene
                break


def count_beats(story, routes):
    starts = {c: collections.Counter() for c in CHAPTERS}
    opens = {c: collections.Counter() for c in CHAPTERS}
    for scene in route_scenes(story, routes):
        chapters = window(scene)
        if not chapters:
            continue
        mode = "remote" if is_remote(scene) else "ip"
        starts[str(chapters[0])][mode] += 1
        for chapter in chapters:
            opens[str(chapter)][mode] += 1
    return starts, opens


def hard_violations(story, paced=None):
    """paced: the roster's relationship ids (from the availability map); None applies H2's StartedFlag rule to all."""
    relationships = story["Relationships"]
    committed = {r["CommittedFlag"]: key for key, r in relationships.items()}
    started = {r["StartedFlag"]: key for key, r in relationships.items()}
    base_started = set()
    for scene in story["Scenes"]:
        if not is_epilogue(scene) and not is_early(scene) and not trickster_gated(scene):
            base_started |= {key for key in sets(scene) if key in started}
    native = {}
    for section in NATIVE_MAPS:
        values = story.get(section) or {}
        for key in (values if isinstance(values, (dict, list)) else []):
            if isinstance(key, str):
                native[key] = section
    romance_keys = {}
    for section in NATIVE_MAPS + ("PermanentEtudes",):
        values = story.get(section) or {}
        if isinstance(values, dict):
            for key, value in values.items():
                guid = value if isinstance(value, str) else json.dumps(value)
                for romance in ROMANCE_ETUDES:
                    if romance in guid:
                        romance_keys[key] = ROMANCE_ETUDES[romance]
    found = []
    for scene in story["Scenes"]:
        sid = scene["Id"]
        own = relationship_of(scene)
        written = sets(scene)
        for key in sorted(written):
            if key in romance_keys:
                found.append(("H3", sid, "sets %s, bound to %s" % (key, romance_keys[key])))
            elif key in ROMANCE_ETUDES:
                found.append(("H3", sid, "sets %s (%s)" % (key, ROMANCE_ETUDES[key])))
        if not is_early(scene):
            continue
        why = trickster_content(scene)
        if why:
            found.append(("H1", sid, "Ch1-2 scene carries Trickster content: " + ", ".join(why)))
        for key in sorted(written):
            if key in committed:
                found.append(("H2", sid, "Ch1-2 scene sets CommittedFlag %s (%s)" % (key, committed[key])))
            elif key in started and key not in base_started and (paced is None or started[key] in paced):
                found.append(("H2", sid, "Ch1-2 scene sets StartedFlag %s of Trickster route %s" % (key, started[key])))
            if key in native and key not in romance_keys:
                found.append(("H3", sid, "Ch1-2 scene sets native key %s (%s)" % (key, native[key])))
        for key in sorted(reads(scene) | written):
            if key in committed and committed[key] != own:
                found.append(("H4", sid, "Ch1-2 scene touches another partner's CommittedFlag %s (%s)" % (key, committed[key])))
            if HAREM.search(key):
                found.append(("H4", sid, "Ch1-2 scene touches harem flag %s" % key))
    return found


def lint(story, availability, roster):
    entries = validate_availability(availability, roster)
    relationships = set(story["Relationships"])
    report = {"characters": [], "review": [], "warn": [], "info": [], "hard": []}
    covered = set()
    for key in sorted(entries):
        entry = entries[key]
        routes = entry["routes"]
        covered |= {r["relationship"] for r in routes}
        built = [r for r in routes if r["relationship"] in relationships]
        present = entry.get("present", {})
        exceptions = entry.get("exceptions", {})
        row = {"key": key, "character": entry["character"], "built": bool(built), "present": present}
        if not built:
            report["characters"].append(row)
            report["info"].append("%s: no route in Story.json yet" % entry["character"])
            continue
        starts, opens = count_beats(story, built)
        row["starts"] = {c: dict(starts[c]) for c in CHAPTERS}
        row["open"] = {c: dict(opens[c]) for c in CHAPTERS}
        report["characters"].append(row)
        for chapter in CHAPTERS:
            if chapter in present and chapter not in exceptions and sum(starts[chapter].values()) == 0:
                carried = sum(opens[chapter].values())
                report["review"].append({"character": entry["character"], "chapter": chapter, "mode": present[chapter],
                                         "open_from_earlier": carried})
        outside = [c for c in CHAPTERS if c not in present and sum(starts[c].values())]
        if outside:
            report["info"].append("%s: beats start in chapters where the map has her absent: %s (check the map or the windows)"
                                  % (entry["character"], ", ".join("Ch" + c for c in outside)))
        if present.get("4") == "ip" and starts["4"]["remote"] and not starts["4"]["ip"]:
            report["warn"].append("%s: Chapter 4 in person, but all %d Ch4 beats are remote"
                                  % (entry["character"], starts["4"]["remote"]))
    others = sorted(relationships - covered)
    if others:
        report["info"].append("relationships outside the roster (not paced): " + ", ".join(others))
    report["hard"] = hard_violations(story, covered)
    return report


def cell(counter):
    ip, remote = counter.get("ip", 0), counter.get("remote", 0)
    return "%d+%d" % (ip, remote)


def render(report, notes, out):
    for note in notes:
        print("pacing: " + note, file=out)
    print("pacing: beats by the chapter they start in (in-person+remote); '*' present, '-' absent, '!' REVIEW", file=out)
    print("  %-24s %s" % ("character", "  ".join("Ch%s   " % c for c in CHAPTERS)), file=out)
    flagged = {(r["character"], r["chapter"]) for r in report["review"]}
    for row in report["characters"]:
        if not row["built"]:
            print("  %-24s (no route yet) present: %s" % (row["character"], ",".join(sorted(row["present"])) or "-"), file=out)
            continue
        cells = []
        for c in CHAPTERS:
            mark = "!" if (row["character"], c) in flagged else "*" if c in row["present"] else "-"
            cells.append("%s%-6s" % (mark, cell(row["starts"][c])))
        print("  %-24s %s" % (row["character"], " ".join(cells)), file=out)
    for item in report["review"]:
        print("REVIEW %s Ch%s (%s): no beat starts here%s" % (
            item["character"], item["chapter"], item["mode"],
            "; %d carried over from earlier chapters" % item["open_from_earlier"] if item["open_from_earlier"] else ""), file=out)
    for item in report["warn"]:
        print("WARN " + item, file=out)
    for item in report["info"]:
        print("INFO " + item, file=out)
    for rule, sid, message in report["hard"]:
        print("HARD %s %s: %s" % (rule, sid, message), file=out)
    print("pacing: %d hard, %d warn, %d review" % (len(report["hard"]), len(report["warn"]), len(report["review"])), file=out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--story", default=str(DEFAULT_STORY))
    parser.add_argument("--availability", default=str(DEFAULT_AVAILABILITY))
    parser.add_argument("--matrix", default=os.environ.get("RRT_TRICKSTER_MATRIX", str(DEFAULT_MATRIX)),
                        help="roster source of truth (trickster-matrix.json)")
    parser.add_argument("--json", help="also write the report as JSON to this path")
    args = parser.parse_args(argv)
    notes = []
    try:
        availability = load_json(args.availability)
        roster = resolve_roster(availability, args.matrix, notes)
        report = lint(load_json(args.story), availability, roster)
    except SchemaError as error:
        for line in str(error).splitlines():
            print("SCHEMA " + line)
        return 2
    render(report, notes, sys.stdout)
    if args.json:
        with open(args.json, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(report, handle, indent=1)
    return 1 if report["hard"] else 0


if __name__ == "__main__":
    sys.exit(main())
