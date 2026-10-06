"""Check the player guide against the export, Rules and the executed ideal-run kit.

The rrt-step comments are a machine-readable index of the visible numbered steps.
We check both the index and its rendered choices/gates, then execute the kit in a
system temporary directory and compare its entire ordered history. No game runs.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "tools/ideal-run-kit"
GUIDE = ROOT / "docs/TRICKSTER-RUN-GUIDE.md"
PROFILE = "3:80,5:30"
BEGIN = "<!-- rrt-checked-begin -->"
END = "<!-- rrt-checked-end -->"
CHAPTER3_COMMITS = {"longcon", "household", "foresight", "nenio", "targona", "nurah", "eritrice",
                    "devarra", "delamere", "gesmerha", "aranka", "kaylessa", "arsinoe", "chadali"}
CHAPTER6_COMMITS = {"nocticula", "areelu", "lastcall"}
STEP = re.compile(r"<!-- rrt-step (.+?) -->")
META = re.compile(r"<!-- rrt-guide (.+?) -->")
AREAS = {
    "61fcf2a352daa394ebae399b1348ba62": "Neathholm",
    "31bab5549f7ea384186159a238360c8d": "Azata island",
    "2570015799edf594daf2f076f2f975d8": "Drezen",
    "0a5654e7dc18f074d9356009d55eb51b": "Wintersun",
    "8217b05e37078414981d994151f0ffb1": "Alushinyrra Higher City",
    "c876d5303f4a19f4a80b0cc9b313db6f": "Colyphyr dungeon",
    "7847c3e3537104f4694167af0b9fcd0e": "Nexus",
    "fe9eaf819cf03424a9108aa8b777694d": "Demonic commando lair",
    "3538511f16d45f44f8249ff710777e2d": "Ivory Labyrinth",
    "22c6a99913fe5bb46b2e6011aaf93368": "Threshold interior",
    "10c4b0e2af186ba46ab4d238d00a40a8": "Threshold exterior",
}


def model_from(path: Path):
    from tools import rrt_verify as verifier
    return verifier.Model(json.loads(path.read_text(encoding="utf-8")))


def flags(model):
    return (set(model.by_id) | set(model.rels) | set(model.native) | set(model.derived)
            | set(model.producers) | {v[k] for v in model.rels.values()
                                      for k in ("StartedFlag", "ClosedFlag", "CommittedFlag")}
            | {f for v in model.rels.values() for k in ("UnavailableFlags", "FailureFlags") for f in v.get(k, [])}
            | {s["InteractionHub"] for s in model.scenes if s.get("InteractionHub")})


def manifest(root=ROOT):
    paths = [root / "src/Story.cs", root / "tools/rrt_verify.py"]
    kit = root / "tools/ideal-run-kit"
    paths += [kit / "final_sim.py", kit / "avoid.txt"]
    paths += sorted(p for p in (kit / "natives").glob("*.txt") if not p.name.startswith("_"))
    paths += sorted((kit / "w6").glob("*.extra.txt"))
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def run_kit(root=ROOT):
    with tempfile.TemporaryDirectory(prefix="rrt-run-guide-") as scratch:
        output = Path(scratch) / "run.json"
        env = dict(os.environ, PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1", CHDAYS=PROFILE)
        run = subprocess.run([sys.executable, str(root / "tools/ideal-run-kit/final_sim.py"), str(output)],
                             cwd=scratch, env=env, text=True, encoding="utf-8",
                             capture_output=True, timeout=180)
        if run.returncode:
            raise ValueError("Ideal-run kit failed:\n" + run.stdout + run.stderr)
        return json.loads(output.read_text(encoding="utf-8"))


def records(trace):
    return [{"scene": e["id"], "chapter": e["ch"], "day": e["day"],
             "completed": e["completed"],
             "choices": [[c["node"], c["index"]] for c in e["choices"]]} for e in trace["log"]]


def commit_chapter(rel):
    return 3 if rel in CHAPTER3_COMMITS else 4 if rel == "herrax" else 6 if rel in CHAPTER6_COMMITS else 5


def ticks(values):
    return ", ".join(f"`{v}`" for v in values) or "none"


def gates(obj):
    parts = []
    for key, title in (("Requires", "Need all"), ("Forbids", "Blocked by"),
                       ("RequiresAny", "Need one")):
        if obj.get(key):
            parts.append(title + ": " + ticks(obj[key]))
    for group in obj.get("RequiresAnyGroups", []):
        parts.append("Need one of: " + ticks(group))
    return "; ".join(parts)


def location(model, scene):
    areas = scene.get("Areas") or []
    if areas:
        place = " / ".join(AREAS.get(a, a) for a in areas)
    else:
        # The native list is the host when there is no area guard. A speaker's
        # ordinary hub is not a substitute for that host.
        place = "native dialogue listed below" if scene.get("AnswerLists") else "owner contact / rest"
    if scene.get("Remote") or scene["Owner"] == "Memory":
        place = "rest delivery / Satchel: " + scene.get("Kind", "conversation") + " (" + place + ")"
    if scene.get("InteractionHub"):
        place += "; hub `" + scene["InteractionHub"] + "`"
    return place


def choice_line(model, scene, node, index):
    choice = node["Choices"][index]
    text = " ".join(choice["Text"].split())
    parts = [f"`{scene['Id']}/{node['Id']}/{index}` — {text}"]
    check = choice.get("Check")
    if check:
        parts.append(f"PASS {check['Skill']} DC {check['DC']}" +
                     (" (Commander only)" if check.get("CommanderOnly") else " (party check)"))
        parts.append(f"success → `{check['Success']}`; failure → `{check['Failure']}`")
    if choice.get("Crusade"):
        cost = choice["Crusade"]
        parts.append(f"crusade {cost['Resource']} {cost['Amount']:+d}")
    if choice.get("RemoveItem"):
        item = choice["RemoveItem"]
        keys = [k for k, guid in model.story.get("InventoryItems", {}).items() if guid == item]
        parts.append("consumes 1 item: " + ticks(keys or [item]))
    if choice.get("Set"):
        parts.append("records " + ticks(choice["Set"]))
    if node.get("EnterSet"):
        parts.append("on entering page: " + ticks(node["EnterSet"]))
    if gates(choice):
        parts.append(gates(choice))
    if choice.get("Abort"):
        parts.append("ends without completing scene")
    return "; ".join(parts)


def render_steps(model, steps):
    lines = ["## Checked choice itinerary", "",
             "Use the area walkthrough above for travel. These numbered steps preserve the kit's exact order,",
             "including the timing substitutions explained above. Days are simulation checkpoints, not travel deadlines.",
             "Within each visit choose the answers in the order printed. Indices are zero-based tester references.",
             "PASS means the successful branch used by this run; save before the roll. All gates shown are implemented.",
             "A completed scene also records its scene ID. Read all letters before waiting for their successors.", ""]
    chapter, day = None, None
    for number, step in enumerate(steps, 1):
        scene = model.by_id[step["scene"]]
        if step["chapter"] != chapter:
            chapter = step["chapter"]
            lines += [f"### Chapter {chapter} choice sequence", ""]
        if step["day"] != day:
            day = step["day"]
            lines += [f"#### Checkpoint day {day}", ""]
        tag = json.dumps(step, ensure_ascii=False, separators=(",", ":"))
        lines += [f"{number}. **{scene['Owner']}: {scene['Title']}** — {location(model, scene)}. <!-- rrt-step {tag} -->",
                  f"   Scene `{scene['Id']}`; chapters {scene['MinChapter']}–{scene['MaxChapter']}" +
                  (" (only " + ", ".join(map(str, scene.get("Chapters"))) + ")" if scene.get("Chapters") else "") +
                  f"; wait at least {scene['DelayHours']}h after the latest prerequisite; " +
                  ("complete." if step["completed"] else "this trace does not complete the scene.")]
        if scene.get("Entry"):
            lines.append("   Open: " + " ".join(scene["Entry"].split()))
        if gates(scene):
            lines.append("   " + gates(scene) + ".")
        if scene.get("AnswerLists"):
            lines.append("   Native answer-list host: " + ticks(scene["AnswerLists"]) + ".")
        if scene.get("ContactUnit"):
            lines.append("   Actor must be physically available: `" + scene["ContactUnit"] + "`" +
                         ("; also " + ticks(scene.get("AdditionalContactUnits", [])) if scene.get("AdditionalContactUnits") else "") + ".")
        if scene.get("Participants"):
            lines.append("   Participants must have open, eligible routes: " + ticks(scene["Participants"]) +
                         "; named women: " + ticks(scene.get("ParticipantWomen", [])) + ".")
        if scene.get("RestAllowance"):
            key = scene["RestAllowance"]
            lines.append(f"   Rest allowance `{key}`: {model.story['RestAllowances'][key]} before another successful rest.")
        for nid, index in step["choices"]:
            lines.append("   - " + choice_line(model, scene, model.nodes[scene["Id"]][nid], index))
        lines.append("")
    return "\n".join(lines).rstrip()


def render_routes(model):
    lines = ["## Route loss and recovery reference", "",
             "Check this before leaving an area or changing a native fate. The closed flag is a deliberate refusal",
             "unless a specific recovery below permits it. A death/departure override is earned only by completing its",
             "device, costs and subsequent choices; it does not grant attraction or commitment.",
             "Native kill choices are not covered merely because another death branch has a device. Reload when no",
             "matching, currently selectable device exists. This is a catalogue of implemented branches, not a promise",
             "that every combination of losses can be repaired.", ""]
    for rel, info in model.rels.items():
        lines += [f"### {rel}: {info['Title']}", "", info.get("Guidance", ""), "",
                  "Commitment: " + ticks([info["CommittedFlag"]]) + "; closure: " + ticks([info["ClosedFlag"]]) + ".",
                  "Unavailable states: " + ticks(info.get("UnavailableFlags", [])) +
                  "; failure states: " + ticks(info.get("FailureFlags", [])) + "."]
        for loss, returned in info.get("UnavailableOverrides", {}).items():
            lines.append(f"- `{loss}` is overridden only by earned `{returned}`.")
        for state, access in info.get("TricksterAccess", {}).items():
            sid = access["Device"]
            if sid not in model.by_id:
                alternatives = [s for s in model.scenes if s["Relationship"] == rel
                                and s.get("TricksterDevice") and s.get("TricksterState") == state]
                lines.append(f"- The registry's named device for **{state}** is absent. "
                             "Use the exported sequence below when its gates match; the stale pointer "
                             "alone does not make this return unavailable." if alternatives else
                             f"- Declared recovery for **{state}** has no exported device scene or matching "
                             "return sequence. Reload before that loss.")
                for alternate in alternatives:
                    lines.append(f"  - `{alternate['Id']}` ({alternate['Title']}); "
                                 f"{location(model, alternate)}; chapters {alternate['MinChapter']}–"
                                 f"{alternate['MaxChapter']}; {alternate['DelayHours']}h delay. "
                                 + gates(alternate) + ".")
                    for node in alternate["Nodes"]:
                        for index in range(len(node["Choices"])):
                            lines.append("    - " + choice_line(model, alternate, node, index))
                continue
            scene = model.by_id[sid]
            lines.append(f"- Recovery for **{state}**: `{sid}` ({scene['Title']}); {location(model, scene)}; "
                         f"chapters {scene['MinChapter']}–{scene['MaxChapter']}; {scene['DelayHours']}h delay. " +
                         gates(scene) + ". Return witness: " + ticks([access["Returned"]]) + ".")
        blockers = {f for s in model.scenes if s["Relationship"] == rel for f in s["Forbids"]
                    if re.search(r"(?:^|[._])(closed|declined|refused|failed|killed|dead|gone)(?:[._]|$)", f)}
        blockers.add(info["ClosedFlag"])
        producers = [(s, n, i) for s in model.scenes if s["Relationship"] == rel for n in s["Nodes"]
                     for i, c in enumerate(n["Choices"]) if blockers.intersection(c["Set"])]
        if producers:
            lines.append("Choices recording closure, refusal or failure that blocks later scenes "
                         "(avoid applicable siblings; a listed recovery must match the actual loss):")
            for scene, node, index in producers:
                lines.append("- " + choice_line(model, scene, node, index))
        lines.append("")
    return "\n".join(lines).rstrip()


def render_presences(model):
    lines = ["## Physical presence windows", "",
             "These are the implemented placement windows, including alternative return branches. A letter does not",
             "put its author beside you. Visit the named area while all requirements hold, after the delay. A recorded",
             "departure, closure or failed placement blocks contact until the corresponding earned recovery applies.",
             "For timed contacts the saved timestamp is required; a missing timestamp does not extend the window.", ""]
    for key, p in model.story.get("Presences", {}).items():
        lines += [f"- **{key}** — {AREAS.get(p['Area'], p['Area'])}, chapters {p['MinChapter']}–{p['MaxChapter']}; "
                  f"{p.get('Mode', 'spawn')}; wait {p.get('DelayHours', 0)}h. {gates(p)}."]
        if p.get("At"):
            lines.append("  Placement anchor: " + str(p["At"]) + ".")
        for w in p.get("ContactWindows", []):
            maximum = w.get("MaxAgeHours")
            lines.append("  Contact after " + ticks([w["Flag"]]) + f": age {w.get('MinAgeHours', 0)}h–" +
                         (f"{maximum}h" if maximum is not None else "unbounded") +
                         "; retired by " + ticks(w.get("SupersededBy", [])) + ".")
    return "\n".join(lines).rstrip()


def render_resources(model, steps):
    totals = Counter()
    chapters = {}
    checks = Counter()
    spent = Counter()
    for step in steps:
        for nid, index in step["choices"]:
            choice = model.nodes[step["scene"]][nid]["Choices"][index]
            cost = choice.get("Crusade")
            if cost and cost["Amount"] < 0:
                amount = -cost["Amount"]
                totals[cost["Resource"]] += amount
                chapters.setdefault(step["chapter"], Counter())[cost["Resource"]] += amount
            check = choice.get("Check")
            if check:
                checks[(check["Skill"], bool(check.get("CommanderOnly")))] = max(
                    checks[(check["Skill"], bool(check.get("CommanderOnly")))], check["DC"])
            if choice.get("RemoveItem"):
                spent[choice["RemoveItem"]] += 1
    lines = ["## Commitment checkpoints", "",
             "Finish these records in the listed chapter on this history. The area's native quest work may continue",
             "after an early mod commitment; a historical promise does not protect against later loss. The checker",
             "asserts each earned commitment time against the chapter boundary, as well as current eligibility at Last Call.", "",
             "| Chapter | Records completed before advancing |", "|---|---|"]
    for ch in (3, 4, 5, 6):
        rels = [r for r in model.rels if r not in {"ember", "aivu"} and commit_chapter(r) == ch]
        lines.append(f"| {ch} | {ticks(rels)} |")
    lines += ["", "## Resource and check preparation", "",
             "Crusade resources are separate from party gold. The following is the gross spend of the printed choice",
             "sequence, including optional scenes; it is not a new romance gate. Keep the required balance at each payment.",
             "The simulator assumes funds and successful checks; it cannot prove that your treasury or skill bonuses suffice.", "",
             "| Chapter | Finances | Materials | Favors |", "|---|---:|---:|---:|"]
    for ch, costs in sorted(chapters.items()):
        lines.append(f"| {ch} | {costs['Finances']} | {costs['Materials']} | {costs['Favors']} |")
    lines += [f"| Total | {totals['Finances']} | {totals['Materials']} | {totals['Favors']} |", "",
              "Party gold: reserve **150,000 gp** for Mielarah, or **100,000 gp** after native Diplomacy DC 41.",
              "She must be hired without the Profane Gift. Stock Death Ward scrolls for Arueshalae; keep a Terendelev scale",
              "unused, Herrax's coin until her printed return/payment, the Abyssal Key until Targona's ward,",
              "Radiance +1 for Yaniel's Fane branch, and the Magical Moonshine Flask through Last Call.", "",
              "Highest mod check in this exact sequence (the individual steps include every DC):", "",
              "| Skill | Who rolls | Highest DC |", "|---|---|---:|"]
    for (skill, commander), dc in sorted(checks.items()):
        lines.append(f"| {skill.removeprefix('Skill')} | {'Commander' if commander else 'party'} | {dc} |")
    if spent:
        lines += ["", "Items actually consumed by the printed answers:", ""]
        for guid, count in sorted(spent.items()):
            keys = [k for k, v in model.story.get("InventoryItems", {}).items() if v == guid]
            lines.append(f"- {ticks(keys or [guid])}: {count}.")
    return "\n".join(lines).rstrip()


def render_checked(model, steps):
    return "\n\n".join([render_resources(model, steps), render_steps(model, steps),
                         render_routes(model), render_presences(model), render_native_plan(model)])


def render_native_plan(model):
    lines = ["## Native action receipts and timing", "",
             "The active kit files below record which native actions accompany the walkthrough. Positive numbers are",
             "simulated chapters; `chapter+day` is an intra-chapter simulation offset. The walkthrough explicitly",
             "corrects the late-Ch4/late-Ch5 substitutions. A kept-off flag is a forbidden action in this run;",
             "an after-scene observation must occur after that scene, never be granted by a cheat.", ""]
    for path in sorted((KIT / "natives").glob("*.txt")):
        if path.name.startswith("_"):
            continue
        lines += [f"### {path.stem} native actions", ""]
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith("#@"):
                line = line[2:].strip()
            elif line.startswith("#"):
                # Preserve useful player directions from the implemented kit,
                # including native actions not explicitly scheduled by it.
                lines.append("> " + line[1:].strip())
                continue
            directive, _, comment = line.partition("  #")
            directive = directive.strip()
            if directive.startswith("-choice "):
                lines.append("- Do not take `" + directive.split()[1] + "`. " + comment.strip())
            else:
                flag, _, when = directive.partition(":")
                forbidden = flag.startswith("!")
                flag = flag.lstrip("!").strip()
                if flag not in model.native:
                    raise ValueError("Kit references unknown/non-native flag " + flag)
                section = model.native[flag]
                binding = model.story[section][flag]
                lines.append(f"- {'Keep OFF' if forbidden else 'Observe'} `{flag}`" +
                             (" at " + when.strip() if when else "") + ": " + comment.strip() +
                             f" Native binding ({section}): {json.dumps(binding, ensure_ascii=False)}.")
        lines.append("")
    lines += ["### Ordered exceptions", ""]
    for path in sorted((KIT / "w6").glob("*.extra.txt")):
        lines.append("Source: " + path.name + ".")
        for raw in path.read_text(encoding="utf-8").splitlines():
            if raw.strip() and not raw.lstrip().startswith("#"):
                lines.append("- " + raw.strip())
    return "\n".join(lines).rstrip()


def validate(text, model, trace=None, expected_manifest=None):
    errors = []
    metas = META.findall(text)
    if len(metas) != 1 or text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("Guide needs exactly one metadata record and checked block")
    meta = json.loads(metas[0])
    steps = [json.loads(raw) for raw in STEP.findall(text)]
    if not steps:
        errors.append("Guide has no steps")
    if meta.get("profile") != PROFILE:
        errors.append("Guide profile differs from campaign-length ideal-run profile")
    if expected_manifest is not None and meta.get("sources") != expected_manifest:
        errors.append("Rules/verifier/active kit changed; re-derive and review the guide")
    known = flags(model)
    for step in steps:
        sid = step.get("scene")
        if sid not in model.by_id:
            errors.append(f"Unknown scene {sid}")
            continue
        scene = model.by_id[sid]
        chapter = step.get("chapter", -1)
        if not (scene["MinChapter"] <= chapter <= scene["MaxChapter"]) or (
                scene.get("Chapters") and chapter not in scene["Chapters"]):
            errors.append(f"Scene {sid} is outside its chapter window")
        for nid, index in step.get("choices", []):
            node = model.nodes[sid].get(nid)
            if node is None or type(index) is not int or index < 0 or index >= len(node["Choices"]):
                errors.append(f"Unknown choice {sid}/{nid}/{index}")
    # All inline code references in handwritten prose and checked rows are
    # validated too. Ignore filenames, numeric GUIDs and hub identifiers; their
    # bindings are checked through the scene/presence data and rendered block.
    prefixes = {k.split(".")[0] for k in known if "." in k}
    prose_tokens = set(re.findall(r"`([^`\n]+)`", text.split(BEGIN, 1)[0]))
    prose_literals = {"Rules.Available", "ChoiceAvailable", "ContactAvailable", "ContactWindowsAvailable"}
    for token in re.findall(r"`([^`\n]+)`", text):
        if token in known or token in prose_literals or re.fullmatch(r"[0-9a-f]{32}", token):
            continue
        if "/" in token and token.rsplit("/", 1)[-1].isdigit():
            try:
                sid, nid, raw = token.rsplit("/", 2)
                model.nodes[sid][nid]["Choices"][int(raw)]
            except (ValueError, KeyError, IndexError):
                errors.append("Unknown choice reference " + token)
        elif (token.split(".")[0] in prefixes and "." in token) or (
                token in prose_tokens and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", token)
                and not token.endswith((".py", ".cs", ".json", ".md", ".txt"))):
            if token not in model.story.get("Presences", {}) and token not in model.story.get("RestAllowances", {}):
                errors.append("Unknown flag/scene reference " + token)
    if not errors:
        actual = text.split(BEGIN, 1)[1].split(END, 1)[0].strip()
        if actual != render_checked(model, steps):
            errors.append("Visible choices, checks, costs, gates, route losses or presence windows are stale")
    if trace is not None:
        if steps != records(trace):
            errors.append("Guide's ordered scenes/choices/completions differ from executed ideal-run path")
        committed = {r["relationship"] for r in trace["result"]["relationships"] if r["committed"]}
        if committed != set(model.rels) - {"ember", "aivu"}:
            errors.append("Combined run no longer commits every achievable relationship")
        days = {int(ch): length for ch, length in trace["result"]["chapter_days"].items()}
        for rel in committed:
            ch = commit_chapter(rel)
            start = sum(length for chapter, length in days.items() if chapter < ch) * 24
            at = trace["result"]["commit_hours"].get(rel)
            if at is None or not start <= at < start + days[ch] * 24:
                errors.append(f"{rel} misses its Chapter {ch} commitment checkpoint")
        romance = committed - {"tirabade", "longcon", "lastcall", "foresight", "household", "nocticula.acquisition"}
        final = set(trace["final_flags"])
        if any(rel + ".harem.eligible" not in final or model.rels[rel]["ClosedFlag"] in final for rel in romance):
            errors.append("A committed woman is no longer eligible/present at Last Call")
        if any(not set(woman.get("Requires", [])).issubset(final)
               for woman in model.story.get("SeatWomen", {}).values()):
            errors.append("A named woman's earned presence is missing at Last Call")
        if sum(e["id"].endswith(".lastcall.call") for e in trace["log"]) != 22:
            errors.append("Combined run does not play all 22 Last Call call-ins")
        if any(c["rests_needed"] > c["rests_available"] for c in trace["result"]["chapters"]):
            errors.append("Combined run exceeds chapter rest budget")
    if errors:
        raise ValueError("\n".join(dict.fromkeys(errors)))
    return len(steps)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", type=Path, default=GUIDE)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    args = parser.parse_args()
    # Permit invocation from outside the checkout without relying on cwd.
    sys.path.insert(0, str(ROOT))
    try:
        count = validate(args.guide.read_text(encoding="utf-8"), model_from(args.story),
                         run_kit(), manifest())
    except (ValueError, KeyError, IndexError, TypeError, subprocess.TimeoutExpired) as error:
        print(f"RUN GUIDE FAIL: {error}", file=sys.stderr)
        return 1
    print(f"RUN GUIDE PASS: {count} ordered steps; 46/48 records; all 22 Last Call call-ins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
