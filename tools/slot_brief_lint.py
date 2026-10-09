"""Validate Gemory briefs against the current exported scene graph (read-only).

The boundary is the first complete beat of each selectable next node, converted
to Gemory's tags without rewriting its words. Terminal slots have no next beat;
their boundaries require editorial review. Short runtime IDs and inline source
mappings use host_scene/host_node and optional paragraph_index/after_text.
last_lines maps branch targets to exact boundaries when they differ. Missing
slots are failures unless the slot index records an evidenced editorial drop.
--known-rebuilds reports the routes with remaining rebuild debt separately;
it never suppresses their findings or exempts another route.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("voice", "scene", "last_line", "speakers", "example", "facts")
# Routes that still carry slot-brief rebuild debt (see
# tools/route_packs/explicit_slots/REBUILD-REPORT.md). Remove a route once its
# briefs and the harem pairs attributed to it lint clean.
# Only reserved harem pairs remain (they need host scenes from structure owners).
REBUILDING = frozenset(("nocticula", "jerribeth", "arueshalae", "camellia"))
ALIASES = {"areelu-vorlesh": "areelu", "elyanka-camilary": "elyanka",
           "dorgelinda-stranglehold": "dorgelinda"}
MALE_NAMES = re.compile(r"\b(Elan|Daeran|Sosiel|Lann|Woljif|Regill|Greybor|"
                        r"Rokhorn|Marhevok|Horgus|Camellius|Galfrey's husband)\b", re.I)
MALE_ROLE = re.compile(r"\b(?:another man|other man|male (?:lover|partner|participant|guard|servant)|"
                       r"man|husband|boyfriend|men|manservant|prince|king|duke|baron|father|brother)\b", re.I)
MALE_PRONOUN = re.compile(r"\b(?:he|him|his|himself)\b", re.I)
ANATOMY = re.compile(r"\b(?:anatomy|anatomical|genital\w*|penis|vagina|cock|clitoris|"
                     r"intercourse|penetrat\w*|oral sex|pleasures? you with her mouth)\b", re.I)


def route_name(path):
    name = ALIASES.get(path.parent.name, path.parent.name)
    if "harem" in path.parts:
        pair = path.stem.removeprefix("household.pair.").split(".")[0].split("_")
        return next((r for r in sorted(REBUILDING) if r in pair), name)
    # A paired route containing a rebuilding character is owned by that rebuild.
    return next((r for r in sorted(REBUILDING) if name.startswith(r + "_")), name)


def first_beat(node, speakers):
    """Exact first Owlcat beat, with only the markup converted for Gemory."""
    text = node.get("Text", "").strip()
    if text.startswith("{n}"):
        end = text.find("{/n}")
        return "N: " + text[3:end] if end >= 0 else None
    if text.startswith('"'):
        end = text.find('"', 1)
        tag = next((t for t, name in speakers.items() if name == node.get("Speaker")), None)
        return tag + ": " + text[1:end] if tag and end >= 0 else None
    if node.get("Speaker") == "Narrator" and text:
        return "N: " + text.splitlines()[0]
    return None


YOU = re.compile(r"\b(?:you|your|yours|yourself)\b", re.I)
THEY = re.compile(r"\bthe Commander(?:'s)?\b")
THEM = re.compile(r"\b(?:them|their|themselves)\b", re.I)
PAST = re.compile(r"\b(?:was|were|had|did|said|went|came|took|kept|drew|left|made|found|"
                  r"stood|lay|sat|knew|felt|held|gave|got|began|\w{3,}ed)\b", re.I)
PRESENT = re.compile(r"\b(?:is|are|has|does|says|goes|comes|takes|keeps|draws|leaves|makes|finds|"
                     r"stands|lies|sits|knows|feels|holds|gives|gets|begins)\b", re.I)


def narration_text(node):
    """Narrator prose of a node and its paragraphs (quoted dialogue excluded)."""
    texts = [node.get("Text", "")] + [p.get("Text", "") for p in node.get("Paragraphs", [])]
    out = []
    for text in texts:
        tagged = re.findall(r"\{n\}(.*?)\{/n\}", text, re.S)
        if tagged:
            out += tagged
        elif node.get("Speaker") == "Narrator":
            out.append(re.sub(r'"[^"]*"', " ", text))
    return " ".join(out)


def host_narration(nodes):
    """(person, tense) of the host prose: 'second'/'third'/None, 'past'/'present'/None."""
    text = " ".join(narration_text(n) for n in nodes)
    second, third = len(YOU.findall(text)), len(THEY.findall(text))
    if not second and not third:
        # Unnamed third-person Commander ("kissed them", "their shoulders").
        them = len(THEM.findall(text))
        third = them if them >= 2 else 0
    person = "second" if second > third else "third" if third > second else None
    past, present = len(PAST.findall(text)), len(PRESENT.findall(text))
    tense = "past" if past > 2 * present else "present" if present > past else None
    return person, tense


def gate_possible(value, chapter=None):
    """Reject demonstrably contradictory gates, not legitimate earned gates."""
    required = set(value.get("Requires", []))
    forbidden = set(value.get("Forbids", [])) - set(value.get("ForbidOverrides", {}))
    if chapter is not None:
        required |= {"chapter_one"} if chapter == 1 else {"chapter_later"} if chapter > 1 else set()
    if required & forbidden:
        return False
    any_flags = value.get("RequiresAny", [])
    if any_flags and not set(any_flags) - forbidden:
        return False
    return all(set(group) - forbidden for group in value.get("RequiresAnyGroups", value.get("AnyGroups", [])))


def host_active(scene, slot):
    chapters = scene.get("Chapters") or range(scene.get("MinChapter", 0), scene.get("MaxChapter", 6) + 1)
    if scene.get("Retired") or scene.get("Disabled") or not any(gate_possible(scene, c) for c in chapters):
        return False
    nodes = {n["Id"]: n for n in scene.get("Nodes", [])}
    if not nodes:
        return False
    pending, seen = [scene.get("Start", scene["Nodes"][0]["Id"])], set()
    while pending:
        current = pending.pop()
        if current in seen or current not in nodes:
            continue
        seen.add(current)
        node = nodes[current]
        if not gate_possible(node):
            continue
        if current == slot:
            return True
        for choice in node.get("Choices", []):
            if gate_possible(choice):
                check = choice.get("Check") or {}
                pending.extend(t for t in (choice.get("Next"), check.get("Success"), check.get("Failure")) if t)
    return False


def following_paragraphs(scene, node, index):
    """Possible next paragraphs, preserving the slot's existing gate context."""
    slot = node["Paragraphs"][index]
    required, forbidden = set(), set()
    for value in (scene, node, slot):
        required.update(value.get("Requires", []))
        forbidden.update(set(value.get("Forbids", [])) - set(value.get("ForbidOverrides", {})))
    for i, paragraph in enumerate(node["Paragraphs"][index + 1:], index + 1):
        groups = paragraph.get("AnyGroups", [])
        combined = dict(Requires=list(required | set(paragraph.get("Requires", []))),
                        Forbids=list(forbidden | set(paragraph.get("Forbids", []))), AnyGroups=groups)
        if not gate_possible(combined):
            continue
        yield i, paragraph
        if (set(paragraph.get("Requires", [])).issubset(required)
                and set(paragraph.get("Forbids", [])).issubset(forbidden)
                and all(set(group) & required for group in groups)):
            break


def lint(paths, story, known_rebuilds=False, slot_index=None):
    findings, counts, identities = [], Counter(), {}
    scenes = story.get("Scenes", [])
    nodes = {}
    for scene in scenes:
        for node in scene.get("Nodes", []):
            nodes.setdefault(node["Id"], []).append((scene, node, None))
            for index, paragraph in enumerate(node.get("Paragraphs", [])):
                if paragraph.get("Id"):
                    nodes.setdefault(paragraph["Id"], []).append((scene, node, index))

    def add(path, code, message, warning=False):
        severity = "warning" if warning else "known" if known_rebuilds and route_name(path) in REBUILDING else "hard"
        findings.append(dict(path=str(path), route=route_name(path), severity=severity, code=code, message=message))

    for path in sorted(paths):
        counts[route_name(path)] += 1
        try:
            brief = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            add(path, "parse", str(exc))
            continue
        if not isinstance(brief, dict):
            add(path, "schema", "Brief must be an object")
            continue
        for field in REQUIRED:
            if not brief.get(field):
                add(path, "required", "Missing/empty " + field)
        for field in ("voice", "scene", "last_line", "example"):
            if field in brief and not isinstance(brief[field], str):
                add(path, "schema", field + " must be text")
        facts = brief.get("facts")
        if facts is not None and not isinstance(facts, str):
            add(path, "schema", "facts must be text: Gemory concatenates this field")
        speakers = brief.get("speakers", {})
        if not isinstance(speakers, dict) or any(not isinstance(t, str) or not re.fullmatch(r"[A-Z]", t)
                                               or not isinstance(n, str) or not n for t, n in speakers.items()):
            add(path, "schema", "speakers must map single uppercase tags to names")
            speakers = {}
        boundaries = brief.get("last_lines", {})
        if not isinstance(boundaries, dict) or any(not isinstance(k, str) or not isinstance(v, str) or not v
                                                   for k, v in boundaries.items()):
            add(path, "schema", "last_lines must map target addresses to nonempty text")
            boundaries = {}
        slot = brief.get("slot_id", path.stem)
        if not isinstance(slot, str) or not slot:
            add(path, "schema", "slot_id must be nonempty text")
            continue
        disposition = (slot_index or {}).get(slot, {})
        if disposition.get("status") == "dropped":
            if not disposition.get("reason") or not disposition.get("evidence"):
                add(path, "index", "Dropped slot needs a reason and evidence")
            elif any(host_active(s, n["Id"]) for s, n, _ in nodes.get(slot, [])):
                add(path, "index", "Dropped slot still has an active runtime host")
            continue
        signature = json.dumps(brief, sort_keys=True, ensure_ascii=False)
        if slot in identities and signature != identities[slot][0]:
            add(path, "duplicate", "Divergent slot id also in " + str(identities[slot][1]))
            add(identities[slot][1], "duplicate", "Divergent slot id also in " + str(path))
        identities.setdefault(slot, (signature, path))
        matches = nodes.get(slot, [])
        declared = brief.get("host_scene") or (brief.get("insertion", {}).get("scene") if isinstance(brief.get("insertion"), dict) else None)
        if brief.get("host_node") and not declared:
            add(path, "schema", "host_node requires host_scene")
        if ("paragraph_index" in brief or "after_text" in brief) and not brief.get("host_node"):
            add(path, "schema", "Inline/paragraph addresses require host_node")
        if brief.get("host_node") and declared:
            matches = [(s, n, brief.get("paragraph_index")) for s in scenes if s["Id"] == declared
                       for n in s.get("Nodes", []) if n["Id"] == brief["host_node"]]
        if declared:
            matches = [(s, n, i) for s, n, i in matches if s["Id"] == declared]
        elif len(matches) > 1:
            inferred = slot.rsplit(".explicit.", 1)[0]
            original = [(s, n, i) for s, n, i in matches if s["Id"] == inferred]
            if len(original) == 1:
                matches = original
        if not matches:
            add(path, "host", "No active slot node for " + slot + (" in " + declared if declared else ""))
        elif len(matches) != 1:
            add(path, "host", "Ambiguous slot host: " + slot)
        else:
            scene, node, paragraph_index = matches[0]
            if paragraph_index is not None and (type(paragraph_index) is not int or
                    not 0 <= paragraph_index < len(node.get("Paragraphs", []))):
                add(path, "host", "paragraph_index is outside the declared host")
                continue
            if not host_active(scene, node["Id"]):
                add(path, "retired", "Host/slot is retired, disconnected or gated off: " + scene["Id"])
            if paragraph_index is not None and not gate_possible(node["Paragraphs"][paragraph_index]):
                add(path, "retired", "Slot paragraph is gated off")
            by_id = {n["Id"]: n for n in scene["Nodes"]}
            if brief.get("after_text"):
                anchor = brief["after_text"]
                text = node.get("Text", "") if paragraph_index is None else node.get("Paragraphs", [])[paragraph_index].get("Text", "")
                if not isinstance(anchor, str) or text.count(anchor) != 1:
                    add(path, "host", "Inline anchor must occur exactly once in the declared host")
                    targets = set()
                else:
                    tail = text.split(anchor, 1)[1].strip()
                    if not tail:
                        add(path, "host", "Inline anchor has no following beat")
                        targets = set()
                    else:
                        prefix = text[:text.index(anchor) + len(anchor)]
                        if not tail.startswith(("{n}", '"')) and prefix.count("{n}") > prefix.count("{/n}"):
                            tail = "{n}" + tail
                        by_id["inline"] = dict(Text=tail, Speaker=node.get("Speaker"))
                        targets = {"inline"}
            elif paragraph_index is None:
                targets = {c.get("Next") for c in node.get("Choices", []) if gate_possible(c) and c.get("Next")}
            else:
                paragraph = node["Paragraphs"][paragraph_index]
                targets = set()
                # Each conditional paragraph before the first unconditional
                # paragraph can be the next displayed beat on some history.
                for index, following in following_paragraphs(scene, node, paragraph_index):
                    key = node["Id"] + "/paragraph#" + str(index)
                    by_id[key] = dict(following, Speaker=node.get("Speaker"))
                    targets.add(key)
                if not targets:
                    targets = {c.get("Next") for c in node.get("Choices", []) if gate_possible(c) and c.get("Next")}
            if not targets:
                add(path, "terminal", "Terminal slot has no next-node boundary; review last_line manually", warning=True)
            mismatches = []
            for target in sorted(targets):
                following = by_id.get(target)
                if not following:
                    add(path, "next", "Missing next node " + target)
                elif (boundaries.get(target, brief.get("last_line"))
                      not in (following.get("Text"), first_beat(following, speakers))):
                    mismatches.append(target + ": " + repr(first_beat(following, speakers)))
            if mismatches:
                add(path, "last_line", "Boundary differs in " + scene["Id"] + "; expected next beats: " + " | ".join(mismatches))
            if boundaries and set(boundaries) != targets:
                add(path, "last_line", "last_lines must cover exactly the current next-beat addresses")
            if boundaries and brief.get("last_line") not in boundaries.values():
                add(path, "last_line", "last_line must match one of the declared branch boundaries")
            # Narration follows the host prose, not scene ownership.
            # The slot's own host prose decides the person; when it has no
            # person marker, the beats it flows into, then the build-up, decide.
            own = node if paragraph_index is None else dict(node["Paragraphs"][paragraph_index], Speaker=node.get("Speaker"))
            if brief.get("after_text"):
                own = dict(node, Text=text.split(brief["after_text"], 1)[0]) if isinstance(brief["after_text"], str) else node
            following = [by_id[t] for t in sorted(targets) if t in by_id]
            build_up = [n for n in scene["Nodes"] if any(node["Id"] in (c.get("Next"),
                        (c.get("Check") or {}).get("Success"), (c.get("Check") or {}).get("Failure"))
                        for c in n.get("Choices", []))]
            person, tense = None, None
            for context in ([own], following, build_up):
                person, tense = host_narration(context)
                if person:
                    break
            mode = brief.get("narration", "second-present")
            # Person is the Commander's: an absent Commander sets no requirement.
            wanted = None if brief.get("commander") == "absent" else {
                "second": "second-present", "third": "third-past"}.get(person)
            if wanted and mode != wanted:
                add(path, "narration", "Host prose is %s-person %s; brief needs narration=%s" % (person, tense or "tense-unclear", wanted))
            elif wanted == "third-past" and tense == "present":
                add(path, "narration_tense", "Host is third-person present; Gemory writes third-past", warning=True)
        content = " ".join(str(brief.get(k, "")) for k in ("voice", "scene", "facts", "example", "participants", "required_beats"))
        males = sorted(set(MALE_NAMES.findall(content) + MALE_ROLE.findall(content)))
        male_speakers = [n for n in speakers.values() if MALE_NAMES.search(n) or MALE_ROLE.search(n)]
        participants = brief.get("participants", [])
        if not isinstance(participants, list):
            add(path, "schema", "participants must be a list")
            participants = []
        male_participants = [n for n in participants if MALE_NAMES.search(str(n)) or MALE_ROLE.search(str(n))]
        cuckold = bool(re.search(r"\bcuckold\w*\b", str(brief.get("scene", "")), re.I))
        scene_text = str(brief.get("scene", ""))
        absent = brief.get("commander") == "absent" or bool(re.search(
            r"\bCommander (?:is |has |will be )?(?:absent|away|left|departed|not present)\b|\bwithout (?:the )?Commander\b",
            scene_text, re.I))
        commander_present = not absent and bool(re.search(r"\bCommander\b|\byou\b", scene_text, re.I))
        # A male speaker can interrupt from outside (Elan), without joining the
        # act. Named sexual participants are different from arrival dialogue.
        sexual_males = [name for name in male_speakers if re.search(
            re.escape(name) + r"[^.!?]{0,70}\b(?:joins? (?:the sex|them in bed)|has sex|penetrates|fucks)\b",
            str(brief.get("scene", "")), re.I)]
        anonymous_act = re.search(r"\b(?:has sex|intercourse|sleeps) with (?:a |the |another )?(?:man|husband|boyfriend)\b",
                                  str(brief.get("scene", "")), re.I)
        if anonymous_act and not re.search(r"\b(?:no|never|not)\b", str(brief.get("scene", ""))[:anonymous_act.start()].split(".")[-1], re.I):
            sexual_males.append(anonymous_act.group())
        if (sexual_males or male_participants) and not (cuckold and commander_present):
            add(path, "scope", "Another male participant/speaker requires a cuckold scene with Commander present: "
                + ", ".join(sexual_males + male_participants))
        if males:
            add(path, "male_mention", "Review male mentions for participation (background mentions alone are allowed): " + ", ".join(males), warning=True)
        elif MALE_PRONOUN.search(content):
            add(path, "male_mention", "Review male pronouns for an unnamed male participant or fixed Commander anatomy", warning=True)
        names = [n for n in speakers.values() if n not in ("Commander", "Narrator")]
        women = [str(n) for n in names + participants if n not in ("Commander", "Narrator")
                 and not MALE_NAMES.search(str(n)) and not MALE_ROLE.search(str(n))]
        if not women:
            add(path, "scope", "No woman identified in speakers or participants")
        if any(re.search(r"\b(?:Ember|Aivu)\b", str(n), re.I) for n in names + participants):
            add(path, "scope", "Friendship-only character in an explicit slot")
        if commander_present and (ANATOMY.search(content) or brief.get("commander") in ("a man", "a woman")):
            variants = brief.get("commander_variants", [])
            if not isinstance(variants, list) or not all(isinstance(v, str) for v in variants) or not {"a man", "a woman"}.issubset(variants):
                add(path, "variants", "Anatomy-sensitive Commander slot needs both commander_variants")
    return findings, dict(sorted(counts.items()))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--briefs", type=Path, default=ROOT / "tools/route_packs/explicit_slots")
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--known-rebuilds", action="store_true")
    parser.add_argument("--index", type=Path, default=ROOT / "tools/route_packs/plans/slot-brief-index.json")
    args = parser.parse_args(argv)
    try:
        story = json.loads(args.story.read_text(encoding="utf-8-sig"))
        paths = list(args.briefs.rglob("*.json"))
        if not paths or not isinstance(story, dict) or not isinstance(story.get("Scenes"), list):
            raise ValueError("No briefs or invalid story Scenes")
        slot_index = json.loads(args.index.read_text(encoding="utf-8-sig")) if args.index.exists() else {}
        findings, counts = lint(paths, story, args.known_rebuilds, slot_index)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print("Slot brief lint: input failure: " + str(exc))
        return 1
    for finding in findings:
        print("{severity}: {path}: {code}: {message}".format(**finding))
    totals = Counter(f["severity"] for f in findings)
    print("Brief counts: " + ", ".join(f"{r}={n}" for r, n in counts.items()))
    print(f"Slot brief lint: {sum(counts.values())} briefs; {totals['hard']} hard; {totals['known']} known rebuild; {totals['warning']} warnings")
    return int(args.strict and totals["hard"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
