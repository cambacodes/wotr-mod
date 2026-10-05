"""Canon partner coherence inventory. Advisory by default; --strict is opt-in.

Reads exported scenes, including conditional paragraphs and EVERY incoming
choice path. It proves state guards using the verifier's existing SAT helper.
Names/relationship words are discovery heuristics, not a prose-quality verdict:
the accompanying report reviews arrangement, reaction, and native resolutions.
No game flags, story conditions, or relationship requirements are authored here.
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path(__file__).with_name("canon_partners.json")


def verify_evidence(registry, blueprints, localization):
    """Verify every nested citation against the supplied game files, read-only."""
    localized = json.loads(Path(localization).read_text(encoding="utf-8-sig"))["strings"]
    citations = {}

    def visit(value):
        if isinstance(value, dict):
            if "path" in value and "guid" in value:
                citations[(value["path"], value["guid"], value.get("key"), value.get("text"))] = value
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(registry)
    errors = []
    with zipfile.ZipFile(blueprints) as archive:
        for (path, guid, key, text), citation in sorted(citations.items()):
            try:
                record = json.loads(archive.read(path))
            except KeyError:
                errors.append(f"{path}: missing blueprint")
                continue
            if record.get("AssetId") != guid:
                errors.append(f"{path}: GUID mismatch")
            if key:
                if localized.get(key) != text:
                    errors.append(f"{path}: localized line mismatch ({key})")
                # A quoted line must belong to THIS blueprint, not a similarly
                # named cue or a string found elsewhere in localization.
                if key not in json.dumps(record.get("Data", {})):
                    errors.append(f"{path}: localized key absent from blueprint")
    return dict(citations=len(citations), errors=errors)


def _names(partner):
    return [partner["name"], *partner.get("aliases", [])]


def _mentions(text, partner):
    if partner.get("mention_patterns"):
        return any(re.search(pattern, text, re.I) for pattern in partner["mention_patterns"])
    return any(re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text, re.I)
               for name in _names(partner))


def _end_kind(scene):
    # NativeReturnCue overrides also use Owner=*Epilogue; those are dialogue,
    # not ending-book pages. Do not credit them as postwar coverage.
    if scene.get("NativeReturnCue"):
        return None
    # The Last Call conversation is a farewell, not a separate postwar page
    # for every dialogue node. The ending-book page owns state coverage.
    if not scene.get("Owner", "").endswith("Epilogue"):
        return None
    if "lastcall" in scene.get("Id", "").lower():
        return "lastcall"
    return "epilogue"


def _chapter_start(scene):
    chapters = scene.get("Chapters") or []
    return min(chapters) if chapters else scene.get("MinChapter", 1)


def _dialogue_replacements(story):
    """Some native dialogue replacements use Epilogue owners for injection.

    Read the declared native target type/evidence, including every variant;
    an Owner label alone cannot turn Seelah's aftermath into a postwar page.
    """
    targets = {row["Target"] for row in story.get("NativeOverrides", [])
               if row.get("TargetType") == "cue"
               and "/Epilogues/" not in row.get("Evidence", "")}
    replacements = set()
    for target, edit in story.get("NativeEpilogueEdits", {}).items():
        if target in targets:
            replacements.update(v["Replacement"] for v in [edit, *edit.get("Variants", [])]
                                if v.get("Replacement"))
    return replacements


def _asserts_absence(text, partner):
    """Conservative claim discovery; report exact text for human review.

    Do not flag a promise to tell a partner, a denial of death, or the bare
    word 'alone'. Unmatched paraphrases remain a manual whole-path obligation.
    """
    names = "|".join(re.escape(n) for n in _names(partner))
    patterns = list(partner.get("absence_patterns") or [
        rf"\b(?:{names})\s+(?:is|was|has|had)\s+(?:already\s+)?(?:dead|died|gone|left|departed)\b",
        rf"\b(?:{names})\s+died\b",
        rf"\b(?:I|we)\s+(?:have\s+|had\s+)?left\s+(?:{names})\b",
    ])
    if partner.get("relationship_type") in ("wife", "husband") or "husband" in partner.get("relationship_type", ""):
        patterns += [r"\bmy (?:wife|husband) (?:is dead|died|is gone)\b",
                     r"\b(?:our|my|the) marriage (?:is|was) over\b"]
    return any(re.search(pattern, text, re.I) for pattern in patterns)


def check(story, registry=None):
    """Return findings/evidence; never turn route writing debt into hard errors.

    Acknowledgement is counted only in an accessible pre-commit context (or a
    node dominating a commitment choice). Merely mentioning the name in a
    later ending cannot pass it. Ending coverage must mention the partner and
    prove a declared current state; historical latches alone are insufficient.
    Separate epilogue and Last Call families are required where exported.
    """
    # Lazy imports avoid a cycle when rrt_verify invokes this module.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools import rrt_verify
    from tools.crossroute_checks.common import AND, NOT, OR, Proof, blocks, lit, when

    registry = registry if registry is not None else json.loads(REGISTRY.read_text(encoding="utf-8"))
    dialogue_ids = _dialogue_replacements(story)

    def end_kind(scene):
        return None if scene["Id"] in dialogue_ids else _end_kind(scene)

    roster = registry.get("roster", [])
    relevant = {e["relationship"] for e in roster if e.get("partners")}
    relevant |= {r for e in roster for r in e.get("additional_relationships", [])}
    shared_ids = {sid for e in roster for sid in e.get("shared_scene_ids", [])}
    # Partner-containing shared scenes are inspected too, but cannot satisfy a
    # woman's own ending/Last Call obligation merely by mentioning her spouse.
    scenes = [s for s in story.get("Scenes", []) if s.get("Relationship") in relevant or s.get("Id") in shared_ids]
    model = rrt_verify.Model({**story, "Scenes": scenes})
    proof = Proof(model)
    surfaces = list(blocks(model))
    by_scene = {}
    for block in surfaces:
        by_scene.setdefault(block.scene["Id"], []).append(block)
    findings, rows = [], []

    def reachable(context):
        return not proof.implies(context, NOT(context))

    def address(block):
        return {"scene": block.scene["Id"], "node": block.node["Id"], "slot": block.slot}

    def finding(entry, partner, code, detail, block=None):
        result = dict(woman=entry["woman"], relationship=entry["relationship"], partner=partner["name"],
                      code=code, detail=detail)
        if block:
            result.update(address(block), excerpt=re.sub(r"\s+", " ", block.text).strip()[:320])
        findings.append(result)

    for entry in roster:
        route = entry["relationship"]
        routes = {route, *entry.get("additional_relationships", [])}
        own = [s for s in model.scenes if s["Relationship"] in routes or s["Id"] in entry.get("shared_scene_ids", [])]
        config = story.get("Relationships", {}).get(route, {})
        committed = config.get("CommittedFlag")
        commit_flags = {f for f in [committed, *entry.get("commitment_flags", [])] if f}
        commits = []
        for scene in own:
            for block in by_scene.get(scene["Id"], []):
                if block.slot.startswith("choice[") and commit_flags.intersection(block.spec.get("Set", [])):
                    if reachable(block.context):
                        commits.append(block)
        for partner in entry.get("partners", []):
            row = dict(woman=entry["woman"], partner=partner["name"], acknowledgements=[],
                       commitments=[address(b) for b in commits], ending_coverage={}, absence_claims=[])
            rows.append(row)
            scope = partner.get("scope", "campaign")
            if scope in ("coercion", "dlc1_anomaly"):
                # Not a silent success: explicitly record why no ordinary
                # campaign romance obligation is inferred from these records.
                row["scope_review"] = scope
                continue
            if not own or not config:
                finding(entry, partner, "missing_route", "Registry route is absent from the supplied export.")
                continue
            if not commits:
                finding(entry, partner, "missing_commitment_inventory", "No reachable commitment producer found; inspect late/derived commitment contracts.")

            mentioned = [b for s in own for b in by_scene.get(s["Id"], [])
                         if _mentions(b.text, partner) and reachable(b.context)]
            for block in mentioned:
                if end_kind(block.scene) or block.slot in ("Entry", "ReturnText"):
                    continue
                if not commits:
                    continue
                can_precede = committed and reachable(AND(block.context, lit(committed, False)))
                earlier = can_precede and any(_chapter_start(block.scene) < _chapter_start(c.scene) for c in commits)
                precommit = can_precede and proof.implies(block.context, lit(committed, False))
                dominates = any(c.scene["Id"] == block.scene["Id"] and
                                (block.node["Id"] == c.node["Id"] or block.node["Id"] in c.ancestors)
                                and proof.implies(c.context, block.context) for c in commits)
                # A declared receipt can connect an ack scene to a later
                # commitment within the same chapter. It is checked against
                # actual producers and never inferred from an arbitrary name.
                receipts = set(partner.get("acknowledgement_receipts", []))
                produced = {flag for n in block.scene["Nodes"] for c in n["Choices"] for flag in c.get("Set", [])}
                witnessed = any(proof.implies(c.context, OR(*(lit(f) for f in receipts & produced)))
                                  for c in commits) if receipts & produced else False
                if earlier or precommit or dominates or witnessed:
                    row["acknowledgements"].append(address(block))
            if not row["acknowledgements"]:
                finding(entry, partner, "acknowledgement_before_commitment", "No reachable acknowledgement proven before commitment (chapter, guard, same-scene dominance, or declared receipt).")

            # Historical native ends remain visible, without requiring an
            # already dead suitor or an abandoned former lover to reappear.
            resolved = partner.get("native_resolution")
            if resolved:
                row["native_resolution"] = partner["native_resolution"]

            declared = [(f["state"], when(f["when"])) for f in partner.get("native_fates", []) if f.get("when")]
            ending_scenes = [] if resolved else [s for s in own if end_kind(s)]
            for kind in sorted({end_kind(s) for s in ending_scenes}):
                covered = []
                for block in mentioned:
                    if end_kind(block.scene) != kind or not (block.slot == "text" or block.slot.startswith("paragraph[")):
                        continue
                    valid = [state for state, condition in declared if proof.implies(block.context, condition)]
                    if valid:
                        covered.append({**address(block), "states": valid})
                row["ending_coverage"][kind] = covered
                if not covered:
                    finding(entry, partner, "partner_state_ending_coverage", f"No {kind} surface both acknowledges the partner and proves a native/current state; unknown fates need explicit reviewed uncertainty.")
                elif declared:
                    for state, condition in declared:
                        possible = any(reachable(AND(b.context, condition)) for s in ending_scenes
                                       if end_kind(s) == kind for b in by_scene.get(s["Id"], [])
                                       if b.slot == "text")
                        # Mentioning someone in a living-only paragraph does
                        # not cover their dead/departed state elsewhere.
                        state_coverage = OR(*(b.context for b in mentioned if end_kind(b.scene) == kind
                                              and proof.implies(b.context, condition)))
                        if possible and not reachable(state_coverage):
                            finding(entry, partner, "missing_partner_state", f"{kind} has reachable {state} histories but no acknowledgement gated to that state.")
                # A covered happy ending cannot discharge a different page's
                # obligation. Inspect each actual page and all its incoming
                # histories, including conditional paragraph alternatives.
                for scene in ending_scenes:
                    if end_kind(scene) != kind:
                        continue
                    for page in by_scene.get(scene["Id"], []):
                        if page.slot != "text" or not reachable(page.context):
                            continue
                        local = [b for b in mentioned if b.scene["Id"] == scene["Id"]
                                 and b.node["Id"] == page.node["Id"]
                                 and (b.slot == "text" or b.slot.startswith("paragraph["))]
                        missing = []
                        for state, condition in declared:
                            histories = AND(page.context, condition)
                            coverage = OR(*(b.context for b in local if proof.implies(b.context, condition)))
                            if reachable(histories) and not proof.implies(histories, coverage):
                                missing.append(state)
                        if missing:
                            finding(entry, partner, "partner_state_page_gap",
                                    f"{kind} page has uncovered current-state histories: {', '.join(missing)}.", page)
            if not ending_scenes and not resolved:
                finding(entry, partner, "partner_state_ending_coverage", "No epilogue or Last Call family exported.")

            absent = OR(*(condition for state, condition in declared if any(t in state for t in ("dead", "killed", "departed", "absent", "former", "exiled", "dismissed"))),
                        *(lit(flag) for flag in partner.get("dramatized_separation_flags", [])))
            for scene_id in sorted({b.scene["Id"] for b in commits}):
                for block in by_scene.get(scene_id, []):
                    if not _asserts_absence(block.text, partner) or not reachable(block.context):
                        continue
                    row["absence_claims"].append(address(block))
                    if not proof.implies(block.context, absent):
                        finding(entry, partner, "ungated_commitment_absence", "Commitment-time absence/separation assertion is not entailed by a matching native fate or reviewed dramatized separation.", block)
    return dict(mode="report", findings=findings, entries=rows,
                roster_count=len(roster), partner_count=len(rows), hard=[])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--json", type=Path, help="Optional report destination (use system temp for audit artifacts)")
    parser.add_argument("--strict", action="store_true", help="Fail on advisory findings; never enabled by rrt_verify")
    parser.add_argument("--verify-canon", type=Path, metavar="GAME_DIR", help="Verify registry citations against GAME_DIR/blueprints.zip and enGB.json")
    args = parser.parse_args(argv)
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    result = check(json.loads(args.story.read_text(encoding="utf-8-sig")), registry)
    if args.verify_canon:
        result["canon_evidence"] = verify_evidence(registry, args.verify_canon / "blueprints.zip",
                                                  args.verify_canon / "Wrath_Data/StreamingAssets/Localization/enGB.json")
        for error in result["canon_evidence"]["errors"]:
            print("  CANON", error)
        print(f"Canon evidence: {result['canon_evidence']['citations']} citations, {len(result['canon_evidence']['errors'])} errors")
    print(f"Canon partners: {result['roster_count']} women, {result['partner_count']} partner records, {len(result['findings'])} advisory findings")
    for row in result["findings"]:
        print(f"  {row['woman']} / {row['partner']}: {row['code']} {row.get('scene', '')} {row['detail']}")
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return int(bool(result.get("canon_evidence", {}).get("errors")) or args.strict and bool(result["findings"]))


if __name__ == "__main__":
    raise SystemExit(main())
