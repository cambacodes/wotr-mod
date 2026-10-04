"""Report native death/departure language beside authored Trickster returns.

README: python tools/native_contradictions.py [--story development/Story.json]
[--game /wrath] [--output tools/native_contradictions_report.md]. Report only:
never edits story content or fails a route for a search hit. Joins native GUIDs
and localization keys, including shared localization, then lists uncovered
cues/answers/slides per route with its existing return predicates. Name context
from sibling cues catches pronoun-only slides. Historical deaths, hypotheticals,
other women on shared pages and unreachable native branches can be false positives;
the report is a review queue, not proof of contradiction or runtime safety.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.game_blueprints import blueprint_type, game_dir, iter_records, text_key  # noqa: E402

LOSS = re.compile(r"\b(?:dead|died|dies|death|killed|slain|mourn\w*|buried|funeral|widow\w*|"
                  r"vanish\w*|disappear\w*|depart\w*|abandon\w*|wander\w*|absent|gone|left|lonely|alone)\b|"
                  r"never\s+(?:saw|seen|returned)|no one ever saw|won['’]t\s+(?:come|return)|"
                  r"(?:life|story)\s+(?:has\s+)?ended|never\s+see\b.{0,80}\bagain", re.I)
RETURN = re.compile(r"(?:returned|rescued|recovered|survived|revived|restored|flown|ransomed|bought_back)", re.I)
ALIASES = {"minagho_chivarro": ("Minagho", "Chivarro"), "camellia": ("Camellia", "Camelia", "Mireya"),
           "devarra": ("Devarra",), "mielarah": ("Mielarah", "Tumberd"),
           "dorgelinda": ("Dorgelinda", "Stranglehold"), "elyanka": ("Elyanka", "Camilary"),
           "areelu": ("Areelu", "Vorlesh")}


def localization_text(strings, value):
    if isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return ""
    entry = strings.get(text_key(value), "")
    return entry.get("Text", "") if isinstance(entry, dict) else entry


def return_routes(payload):
    """Only existing declared return/outcome evidence; invent no rescue predicate."""
    result = {}
    for route, relationship in payload.get("Relationships", {}).items():
        keys = set(relationship.get("UnavailableOverrides", {}).values())
        for state in relationship.get("TricksterAccess", {}).values():
            returned = state.get("Returned", state.get("returned"))
            if returned:
                keys.add(returned)
        for scene in payload.get("Scenes", []):
            if scene.get("Relationship") == route:
                keys.update(flag for node in scene.get("Nodes", []) for choice in node.get("Choices", [])
                            for flag in choice.get("Set", []) if flag.startswith(route + ".") and RETURN.search(flag))
        keys = {k for k in keys if isinstance(k, str) and RETURN.search(k)}
        if keys:
            result[route] = sorted(keys)
    return result


def scan(payload, records, strings):
    routes = return_routes(payload)
    covered = {row["Target"] for row in payload.get("NativeOverrides", [])}
    names = {route: re.compile(r"\b(?:" + "|".join(re.escape(n) for n in ALIASES.get(route, (route.replace('_', ' '),))) + r")\b", re.I)
             for route in routes}
    entries = []
    page_members = {}
    cue_pages = defaultdict(set)
    for path, record in records:
        data = record["Data"]
        kind = blueprint_type(data)
        if kind == "BlueprintBookPage":
            page_members[record["AssetId"]] = {ref.removeprefix("!bp_") for ref in data.get("Cues", [])}
            continue
        if kind not in {"BlueprintCue", "BlueprintAnswer"}:
            continue
        text = localization_text(strings, data.get("Text"))
        if not text:
            continue
        # A book page or dialog directory supplies a woman's name to later
        # pronoun-only slides. Carry scope, not a guessed antecedent.
        scope = path.rsplit("/", 1)[0]
        entries.append((path, record["AssetId"], kind, text, scope))
    by_guid = {entry[1]: entry for entry in entries}
    page_names = {}
    for page, members in page_members.items():
        page_names[page] = {route for guid in members if guid in by_guid for route, pattern in names.items()
                            if pattern.search(by_guid[guid][3])}
        for guid in members:
            cue_pages[guid].add(page)
    candidates = defaultdict(list)
    coverage = defaultdict(int)
    for path, guid, kind, text, scope in entries:
        if not LOSS.search(text):
            continue
        named = {route for route, pattern in names.items() if pattern.search(text)}
        # Context search is intentionally restricted to epilogue slides and the
        # route's own named dialogue directory, avoiding whole-hub contamination.
        contextual = set().union(*(page_names[page] for page in cue_pages[guid])) if cue_pages[guid] else set()
        # A companion hub often mentions other women. Its unnamed lines belong
        # to the directory's woman, not to every name mentioned anywhere in it.
        contextual.update(route for route, pattern in names.items() if pattern.search(scope))
        for route in named | contextual:
            if guid in covered:
                coverage[route] += 1
                continue
            candidates[route].append(dict(guid=guid, path=path, kind="slide" if "/Epilogues/" in path else kind,
                                          text=text, match="name" if route in named else "sibling context"))
    return routes, candidates, coverage


def render(payload, records, strings):
    routes, candidates, coverage = scan(payload, records, strings)
    lines = ["# Native contradiction candidates", "", "Generated by `python tools/native_contradictions.py`.", "",
             "Report only. These are lexical candidates, not proven contradictions. Check native conditions, timing, "
             "death provenance, current/ever Trickster policy, and original/replacement scene availability before editing. "
             "Registry coverage means the GUID is declared; it does not prove coverage of every history.", "",
             "| Route | Uncovered candidates | Declared candidate GUIDs |", "|---|---:|---:|"]
    for route in sorted(routes):
        lines.append(f"| {route} | {len(candidates[route])} | {coverage[route]} |")
    for route in sorted(routes):
        lines += ["", f"## {route}", "", "Authored return/rescue predicates: " + ", ".join(f"`{k}`" for k in routes[route]) + ".", ""]
        if not candidates[route]:
            lines.append("No uncovered lexical candidates found. This does not establish native-history consistency.")
        for candidate in sorted(candidates[route], key=lambda c: (c["path"], c["guid"])):
            snippet = re.sub(r"\s+", " ", candidate["text"]).strip()
            if len(snippet) > 420:
                match = LOSS.search(snippet)
                offset = max(0, match.start() - 130)
                snippet = ("…" if offset else "") + snippet[offset:offset + 420] + "…"
            lines += [f"- `{candidate['guid']}` — {candidate['kind']}; {candidate['match']}; `{candidate['path']}`",
                      "  > " + snippet.replace("\n", " ")]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--game", type=Path, default=game_dir())
    parser.add_argument("--output", type=Path, default=ROOT / "tools/native_contradictions_report.md")
    args = parser.parse_args()
    payload = json.loads(args.story.read_text(encoding="utf-8-sig"))
    strings = json.loads((args.game / "Wrath_Data/StreamingAssets/Localization/enGB.json").read_text(encoding="utf-8-sig"))["strings"]
    with ZipFile(args.game / "blueprints.zip") as archive:
        report = render(payload, iter_records(archive, ("World/Dialogs/",)), strings)
    args.output.write_text(report, encoding="utf-8")
    print(f"REPORT ONLY: native contradiction candidates -> {args.output}")


if __name__ == "__main__":
    main()
