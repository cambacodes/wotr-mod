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


# eng8-q8e begin: explicit outcome-to-target parity, including native continuations.
def ending_contracts():
    return json.loads((ROOT / "tools/native_ending_inventory2_contracts.json").read_text(encoding="utf-8"))


ENDING_FIELDS = ("Requires", "RequiresAny", "RequiresAnyGroups", "Forbids", "ForbidOverrides")


def ending_when(scene):
    """Compile the existing ending conditions into E14's OR-of-AND representation.

    An override lifts only its own loss. No commitment implies bodily return.
    The live-path condition applies to these native alterations, not to the
    completed return itself. Final engine guards are read after all appenders.
    """
    from itertools import product
    groups = [scene.get("RequiresAny")] if scene.get("RequiresAny") else []
    groups += scene.get("RequiresAnyGroups") or []
    for loss in scene.get("Forbids") or []:
        override = (scene.get("ForbidOverrides") or {}).get(loss)
        groups.append(["!" + loss, override] if override else ["!" + loss])
    return [list(dict.fromkeys(["trickster.now", *scene.get("Requires", []), *parts]))
            for parts in product(*groups)]


def integrate_endings(payload):
    """Align existing registrations with final, save-compatible ending readers."""
    import copy
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    # The native partner needs the same current-body losses as the authored pack.
    # Reuse the final lifecycle reader; a saved return is not a second life.
    for shared in ending_contracts().get("SharedLossGuards", []):
        target, source = scenes[shared["Outcome"]], scenes[shared["Source"]]
        rel = payload["Relationships"][target["Relationship"]]
        for loss in rel.get("UnavailableFlags", []):
            if loss not in target.setdefault("Forbids", []):
                target["Forbids"].append(loss)
            if loss in source.get("ForbidOverrides", {}):
                target.setdefault("ForbidOverrides", {})[loss] = source["ForbidOverrides"][loss]
            else:
                target.setdefault("ForbidOverrides", {}).pop(loss, None)
    for row in ending_contracts()["Rows"]:
        spec = payload[row["Field"]][row["Target"]]
        outcomes = [scenes[id] for id in row["Outcomes"]]
        if row["Field"] == "NativeEpilogueSuppressions":
            spec["When"] = [g for outcome in outcomes for g in ending_when(outcome)]
            continue
        for variant, outcome, replacement in zip([spec, *spec.get("Variants", [])], outcomes, row["Replacements"]):
            variant["When"] = ending_when(outcome)
            target = scenes[replacement]
            if target is not outcome:
                for field in ENDING_FIELDS:
                    target[field] = copy.deepcopy(outcome.get(field, {} if field == "ForbidOverrides" else []))
                target["Requires"] = list(dict.fromkeys([*target["Requires"], "trickster.now"]))


def check_endings(payload, contracts=None):
    """Missing targets, narrowed histories and unavailable replacements fail closed."""
    contracts = contracts or ending_contracts()
    if len(contracts["Rows"]) != 13 or len(contracts["Findings"]) != 12:
        raise ValueError("E-Q8-06: omitted ending inventory row/finding")
    if len(set(contracts.get("IdentityPreservingTargets", []))) != 4:
        raise ValueError("E-Q8-06: omitted native history identity")
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    registered = {r["Target"]: r for r in payload.get("NativeOverrides", [])}
    for shared in contracts.get("SharedLossGuards", []):
        target, source = scenes[shared["Outcome"]], scenes[shared["Source"]]
        for loss in payload["Relationships"][target["Relationship"]].get("UnavailableFlags", []):
            if (loss not in target.get("Forbids", []) or target.get("ForbidOverrides", {}).get(loss)
                    != source.get("ForbidOverrides", {}).get(loss)):
                raise ValueError("E-Q8-06: inconsistent current-body guard " + loss)
    for row in contracts["Rows"]:
        target = row["Target"]
        spec = payload.get(row["Field"], {}).get(target)
        if not spec or target not in registered or registered[target]["Field"] != row["Field"]:
            raise ValueError("E-Q8-06: missing ending target " + target)
        if target not in contracts["Fixtures"]:
            raise ValueError("E-Q8-06: missing original fixture " + target)
        outcomes = [scenes[id] for id in row["Outcomes"]]
        if row["Field"] == "NativeEpilogueSuppressions":
            if spec["When"] != [g for outcome in outcomes for g in ending_when(outcome)]:
                raise ValueError("E-Q8-06: incomplete suppression histories " + target)
        else:
            variants = [spec, *spec.get("Variants", [])]
            if len(variants) != len(outcomes):
                raise ValueError("E-Q8-06: incomplete variants " + target)
            for variant, outcome, replacement in zip(variants, outcomes, row["Replacements"]):
                if variant["Replacement"] != replacement or variant["When"] != ending_when(outcome):
                    raise ValueError("E-Q8-06: incomplete ending histories " + target)
                if scenes[replacement] is not outcome:
                    for field in ENDING_FIELDS:
                        expected = outcome.get(field, {} if field == "ForbidOverrides" else [])
                        if field == "Requires":
                            expected = list(dict.fromkeys([*expected, "trickster.now"]))
                        if scenes[replacement].get(field) != expected:
                            raise ValueError("E-Q8-06: replacement unavailable for ending " + target)
    return len(contracts["Rows"])
# eng8-q8e end


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


# eng7-l03: deterministic mapped inventory supplements the lexical review queue.
# It consumes q6b's registry and C#'s real Available-aware selector evidence.
def render_inventory(payload, expectations, backlog, coverage=None):
    from storylines.native_overrides import inventory
    rows = inventory(payload, expectations, backlog)
    evaluations = {r["Target"]: r for r in (coverage or {}).get("Evaluations", [])}
    lines = ["# Reviewed native dependency inventory (E-Q7-09 / E-Q7-28)", "",
        "Authored contracts; native identifiers, actions and continuations remain unchanged. "
        "FAIL entries are unresolved dependencies, not permission to hide a native outcome. "
        "Route writers own replacement prose. Lexical sibling candidates follow below.", "",
        "| Finding | Native GUID / path | Earned dependency | Evaluation |", "|---|---|---|---|"]
    failures = 0
    for row in rows:
        evaluation = evaluations.get(row["Target"])
        status = row["Status"]
        # An unchanged-native negative case proves preservation, not reconciliation.
        # Never let it turn an unregistered mapped dependency (e.g. morale) green.
        if evaluation and row["Spec"] and status != "context":
            status = "PASS_EVALUATED" if evaluation["Passed"] else "FAIL_SELECTION"
        if status.startswith("FAIL") or status == "registered_unevaluated":
            failures += 1
        dependency = " OR ".join(" + ".join(g) for g in row["Dependency"])
        lines.append(f"| {row['Finding']} | `{row['Target']}` / `{row['Path']}` | {dependency} | {status} |")
    lines += ["", f"Mapped dependency coverage: **{failures} failing/unevaluated entries**.", "",
              "## Registered delivery contracts", ""]
    specs = {r["Target"]: r["Spec"] for r in rows if r["Spec"]}
    for target, spec in sorted(specs.items()):
        lines.append(f"- `{target}`: `{json.dumps(spec, sort_keys=True)}`")
    lines += ["", "## Existing repairs (H-14)", "",
              "These repairs already use q6b's registry; they do not cover the remaining body-state/Q3 siblings. "
              "Serialized native actions/continuations are checked against the archive, and the existing "
              "NativeDialogEdit/AreeluAfterlogue regressions remain in the full rules gate.", ""]
    registered = {r["Target"]: r for r in payload.get("NativeOverrides", [])}
    for target in expectations.get("ExistingRepairs", []):
        row = registered.get(target)
        if row is None:
            failures += 1
            lines.append(f"- `{target}`: FAIL_UNCOVERED existing repair.")
        else:
            spec = payload[row["Field"]][row["RuntimeKey"]]
            lines.append(f"- `{target}` / `{expectations['Fixtures'][target]['Path']}` / `{row['Source']}`: "
                         f"registered unchanged delivery; `{json.dumps(spec, sort_keys=True)}`.")
    lines += ["",
              "## Native selection cases", ""]
    for evaluation in (coverage or {}).get("Evaluations", []):
        for case in evaluation["Cases"]:
            lines.append(f"- `{evaluation['Target']}` / {case['Name']}: original={case['Original']}; "
                         f"selected=`{case['Selected'] or 'native'}`; expected=`{case['Expected'] or 'native'}`; "
                         f"{'PASS' if case['Passed'] else 'FAIL_SELECTION'}.")
    lines += ["", "## Authored outcome consumers (current export)", "",
              "Review every listed ending alongside the native originals; the mapped dependency column alone "
              "is not the full outcome partition. These are actual scene predicates, including late commitment, "
              "refusal, closure, morale and sacrifice. Listing a scene does not declare its native contradiction resolved.", ""]
    for route in sorted({r["Route"] for r in rows}):
        relationship = "minagho_chivarro" if route == "minagho-and-chivarro" else route
        lines += [f"### {route}", ""]
        for scene in payload["Scenes"]:
            if scene.get("Relationship") != relationship or not scene.get("Owner", "").endswith("Epilogue"):
                continue
            gates = {key: scene.get(key, []) for key in ("Requires", "RequiresAny", "RequiresAnyGroups", "Forbids")}
            gates["ForbidOverrides"] = scene.get("ForbidOverrides", {})
            lines.append(f"- `{scene['Id']}`: chapters {scene['MinChapter']}–{scene['MaxChapter']}; "
                         f"`{json.dumps(gates, sort_keys=True)}`.")
    lines += ["", "## Uncovered native siblings and outcomes", "",
              "Every cue/answer in each cited dialogue directory and every cue on the cited epilogue pages is "
              "enumerated, including lines without lexical death terms. Unmapped entries require review; "
              "they are not automatically contradictions.", ""]
    registered = {r["Target"] for r in payload.get("NativeOverrides", [])}
    for guid in expectations["Siblings"]:
        fixture = expectations["Fixtures"][guid]
        status = "registered (see When/availability)" if guid in registered else "UNCOVERED_REVIEW"
        lines.append(f"- `{guid}` — {fixture['Type']}; `{fixture['Path']}`; {status}.")
    lines += ["", "## Route follow-ups", ""]
    failing = {r["Finding"] for r in rows if r["Status"] == "FAIL_UNCOVERED"}
    for finding in expectations["Findings"]:
        if finding["Id"] in failing:
            lines.append(f"- {finding['Id']} / `{finding['Scene']}`: {finding['Fix']}")
        if finding.get("SnapshotStateAbsent"):
            lines.append(f"- {finding['Id']}: snapshot `{finding['SnapshotStateAbsent']}` is absent here; "
                         "contracts use the current paid dig/raise evidence without inventing a reconciliation flag.")
    # eng8-q8e begin: supplemental targets include pronoun-only follow-ons.
    if expectations.get("eng8-q8e"):
        lines += ["", "## E-Q8-06 ending continuation parity", "",
                  "Authored, current-Trickster reconciliations. Structural parity is checked against final "
                  "ending conditions; native eligibility and negative histories are exercised by RulesTests.", ""]
        try:
            check_endings(payload)
            status = "PARITY"
        except ValueError as error:
            failures += 1
            status = "FAIL"
            lines.append(str(error))
        for row in ending_contracts()["Rows"]:
            lines.append(f"- `{row['Target']}` / `{row['Field']}`: {status}; " + ", ".join(row["Outcomes"]))
    # eng8-q8e end
    return "\n".join(lines) + "\n", failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--game", type=Path, default=game_dir())
    parser.add_argument("--output", type=Path, default=ROOT / "tools/native_contradictions_report.md")
    # eng7-l03
    parser.add_argument("--inventory", type=Path, default=ROOT / "tools/native_inventory_expectations.json")
    parser.add_argument("--coverage", type=Path, help="C# RulesTests selector evidence for this exact story export")
    parser.add_argument("--strict-inventory", action="store_true", help="fail on uncovered/unevaluated mapped dependencies")
    args = parser.parse_args()
    payload = json.loads(args.story.read_text(encoding="utf-8-sig"))
    coverage = json.loads(args.coverage.read_text(encoding="utf-8")) if args.coverage else None
    if coverage:
        import hashlib
        if coverage.get("StorySha256") != hashlib.sha256(args.story.read_bytes()).hexdigest():
            raise ValueError("Native inventory: stale selector evidence for another story export")
    inventory, failures = render_inventory(payload, json.loads(args.inventory.read_text(encoding="utf-8")),
                                          json.loads((ROOT / "tools/engine_backlog.json").read_text(encoding="utf-8")), coverage)
    strings = json.loads((args.game / "Wrath_Data/StreamingAssets/Localization/enGB.json").read_text(encoding="utf-8-sig"))["strings"]
    with ZipFile(args.game / "blueprints.zip") as archive:
        report = render(payload, iter_records(archive, ("World/Dialogs/",)), strings)
    args.output.write_text(inventory + "\n---\n\n" + report, encoding="utf-8")
    print(f"REPORT ONLY: native contradiction candidates -> {args.output}")
    print(f"Native dependency coverage: {failures} failing/unevaluated entries")
    return int(args.strict_inventory and failures > 0)


if __name__ == "__main__":
    sys.exit(main())
