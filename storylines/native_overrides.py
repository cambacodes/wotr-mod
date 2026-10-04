"""Shared native reconciliation registry (authored Trickster changes).

README
======
declare(payload, source=__name__, target=GUID, target_type="cue", action="REPLACE",
        spec=dict(Parent=GUID, Dialog=GUID, Key=localization_key,
                  Replacement=scene_id, When=[["trickster.now", "route.recovered"]]))
compiles to the existing E14i runtime contract. Use "slide"/"SLIDE-SWAP" with
Page/Sequence instead of Parent/Dialog, or "HIDE" with a reviewed NativeGate id
and Relationship (pass key="arsinoe.souls_search_answer" for that reviewed gate).
HIDE on a slide uses the E14d suppression contract. Ordered
Variants retain the E14d scene-availability check and original cue save names.

When is an OR of AND groups; !flag is allowed by E14d. Every group needs the
appropriate trickster.now/ever predicate and an existing state, not a new gate.
Do not infer rescued from committed or returned from survived. The existing
earned_presence T6 check decides whether historical Trickster evidence suffices.

register_legacy migrates reviewed route dictionaries without changing their
runtime representation. finalize validates GUIDs/types against blueprints.zip,
state names and the runtime whitelist. Unsupported actions/targets fail at build
time with a safe alternative. In particular answer text and journal text cannot
be safely replaced by this runtime; journal reconciliation currently supports
only the existing E19 SETTLE-FAILED contract, which grants no completion or XP.

Runtime safety stays in NativeEpilogueEdit/NativeGate: complementary original
conditions, the same snapshot, preserved reviewed OnShow/OnStop/continuations,
and refusal on drift. The archive alone cannot establish parent-mod compatibility
(Arueshalae Cue_0461). Add a reviewed runtime contract before declaring a new
target. Registry metadata is build/report evidence, not a second runtime path.
"""
import copy
from functools import lru_cache
from pathlib import Path
import re

from tools.game_blueprints import find_bindings, game_dir, text_key

ROOT = Path(__file__).resolve().parents[1]
TYPES = dict(cue="BlueprintCue", slide="BlueprintCue", answer="BlueprintAnswer",
             objective="BlueprintQuestObjective", dialog="BlueprintDialog", etude="BlueprintEtude")
FIELDS = ("NativeEpilogueEdits", "NativeEpilogueSuppressions", "NativeGates", "NativeObjectiveSettlements")


@lru_cache(maxsize=1)
def contracts():
    """Read the actual runtime whitelists; never maintain a divergent Python list."""
    cue_source = (ROOT / "src/NativeEpilogueEdit.cs").read_text(encoding="utf-8-sig")
    cues = set(re.findall(r'\["([a-f0-9]{32})"\]\s*=\s*new Evidence', cue_source))
    rules = (ROOT / "src/Story.cs").read_text(encoding="utf-8-sig")
    def table(name):
        body = rules.split(" " + name + " =", 1)[1].split("};", 1)[0]
        return dict(re.findall(r'\["([^"]+)"\]\s*=\s*"([a-f0-9]{32})"', body))
    return cues, table("ReviewedNativeGates"), table("ReviewedNativeObjectives")


def _delivery(target, target_type, action, key, spec):
    cues, gates, objectives = contracts()
    alternative = ("use a reviewed E14i cue replacement preserving OnShow/OnStop and continuation, "
                   "or an E18 answer ShowConditions gate; add its runtime policy first")
    if target_type not in TYPES:
        raise ValueError(f"NativeOverride {target}: unsupported type {target_type}; {alternative}")
    if action in {"REPLACE", "SLIDE-SWAP"}:
        if target_type not in {"cue", "slide"} or (action == "SLIDE-SWAP" and target_type != "slide"):
            raise ValueError(f"NativeOverride {target}: {action} cannot safely alter {target_type}; {alternative}. "
                             "For journals use a reviewed E19 failed-objective settlement or an authored objective.")
        if target not in cues:
            raise ValueError(f"NativeOverride {target}: no reviewed E14d/E14i cue-policy contract; {alternative}")
        if (target_type == "slide") != bool(spec.get("Page")):
            raise ValueError(f"NativeOverride {target}: slide requires Page; dialogue cue requires Parent/Dialog")
        return "NativeEpilogueEdits", target
    if action == "HIDE":
        if target_type == "slide" and target in cues and spec.get("Page"):
            return "NativeEpilogueSuppressions", target
        if gates.get(key) == target:
            return "NativeGates", key
        raise ValueError(f"NativeOverride {target}: cannot safely HIDE without a reviewed E18 gate or E14d slide suppression; {alternative}. "
                         "Journal objectives use a reviewed E19 settlement, never silent removal.")
    if action == "SETTLE-FAILED" and target_type == "objective" and objectives.get(key) == target:
        return "NativeObjectiveSettlements", key
    raise ValueError(f"NativeOverride {target}: unsupported action {action}; {alternative}")


def declare(payload, *, source, target, target_type, action, spec, key=None):
    """Append a declaration and compile to an existing runtime field atomically."""
    if not re.fullmatch(r"[a-f0-9]{32}", target):
        raise ValueError(f"NativeOverride {source}: target must be a native GUID: {target}")
    field, runtime_key = _delivery(target, target_type, action, key, spec)
    if runtime_key in payload.get(field, {}):
        raise ValueError(f"NativeOverride {source}: conflicting {field} {runtime_key}")
    if any(row["Target"] == target for row in payload.get("NativeOverrides", [])):
        raise ValueError(f"NativeOverride {source}: duplicate target {target}; append ordered Variants instead")
    built = copy.deepcopy(spec)
    payload.setdefault(field, {})[runtime_key] = built
    payload.setdefault("NativeOverrides", []).append(dict(Source=source, Target=target, TargetType=target_type,
        Action=action, Field=field, RuntimeKey=runtime_key, Authored=True))


def register_legacy(payload, source, *, edits=None, suppressions=None, gates=None, settlements=None):
    """Save-compatible migration adapter; all spec bytes/ordering are retained."""
    for target, spec in (edits or {}).items():
        slide = bool(spec.get("Page"))
        declare(payload, source=source, target=target, target_type="slide" if slide else "cue",
                action="SLIDE-SWAP" if slide else "REPLACE", spec=spec)
    for target, spec in (suppressions or {}).items():
        declare(payload, source=source, target=target, target_type="slide", action="HIDE", spec=spec)
    for key, spec in (gates or {}).items():
        # The reviewed gates include specialised spawn and quest control. They
        # stay on their existing runtime path, not a generic type-wide mutation.
        kind = {"ivory_sanctum.red_dragon_spawn": "etude", "golems_dragon_eggs.over_body": "cue",
                "arsinoe.souls_search_answer": "answer", "dragon_eggs.dialog": "dialog",
                "kiana.q3_recovery": "etude"}.get(key)
        declare(payload, source=source, target=spec["Target"], target_type=kind, action="HIDE", spec=spec, key=key)
    for key, spec in (settlements or {}).items():
        declare(payload, source=source, target=spec["Target"], target_type="objective", action="SETTLE-FAILED", spec=spec, key=key)


def _known(payload):
    fields = ("Etudes", "CompletedEtudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs",
              "UnlockableFlags", "QuestObjectives", "InventoryItems", "PartyItems", "StartedQuests", "MainCharacterFacts", "Derived", "Latches")
    known = set().union(*(payload.get(field, {}) for field in fields))
    known.update(payload.get("PendingHooks", []))
    known.update("revive." + name + ".available" for name in payload.get("Revivals", {}))
    known.update(name + ".failed" for name in payload.get("Presences", {}))
    # Same finite runtime inputs as Story.cs Rules.Validate (not arbitrary flags
    # accepted because they happen to appear in authored Requires).
    rules = (ROOT / "src/Story.cs").read_text(encoding="utf-8-sig")
    runtime = rules.split("var derivedFlags =", 1)[1].split("var contactEvidence", 1)[0]
    known.update(re.findall(r'"([^"\n]+)"', runtime))
    echo = rules.split("WenduagEchoRuntime = new[]", 1)[1].split("}", 1)[0]
    known.update("wenduag.trickster.echo.abyss." + suffix for suffix in re.findall(r'"([^"\n]+)"', echo))
    for relationship in payload.get("Relationships", {}).values():
        known.update(relationship.get(field) for field in ("StartedFlag", "ClosedFlag", "CommittedFlag"))
    for scene in payload.get("Scenes", []):
        known.add(scene["Id"])
        for node in scene.get("Nodes", []):
            for choice in node.get("Choices", []):
                known.update(choice.get("Set", []))
    return known


def finalize(payload, archive=None):
    """Build gate: no unregistered legacy edits, invalid states or unsafe GUIDs."""
    registered = {(row["Field"], row["RuntimeKey"]) for row in payload.get("NativeOverrides", [])}
    missing = [(field, key) for field in FIELDS for key in payload.get(field, {}) if (field, key) not in registered]
    if missing:
        raise ValueError(f"NativeOverrides: unregistered native edits {missing}; use register_legacy/declare")
    known = _known(payload)
    scenes = {s["Id"]: s for s in payload.get("Scenes", [])}
    expected = {}
    for row in payload.get("NativeOverrides", []):
        target = row["Target"]
        spec = payload[row["Field"]][row["RuntimeKey"]]
        _delivery(target, row["TargetType"], row["Action"], row["RuntimeKey"], spec)
        expected[target] = TYPES[row["TargetType"]]
        variants = [spec] + spec.get("Variants", [])
        for variant in variants:
            groups = variant.get("When", [])
            if not groups or any(not group or not {"trickster.now", "trickster.ever"}.intersection(group) for group in groups):
                raise ValueError(f"NativeOverride {target}: every When group requires trickster.now/ever")
            for group in groups:
                for state in group:
                    if not isinstance(state, str) or state.removeprefix("!") not in known:
                        raise ValueError(f"NativeOverride {target}: unknown state {state!r}")
            if row["Field"] == "NativeEpilogueEdits":
                replacement = scenes.get(variant.get("Replacement"))
                if replacement is None or len(replacement.get("Nodes", [])) != 1:
                    raise ValueError(f"NativeOverride {target}: replacement must name an existing one-node scene")
        for field, kind in (("Page", "BlueprintBookPage"), ("Sequence", "BlueprintCueSequence"), ("Dialog", "BlueprintDialog")):
            if spec.get(field):
                expected[spec[field]] = kind
        # E14i accepts cue, answer or dialog parents. Verify their concrete type
        # after reading the record, using Blueprint* only for this union.
        if spec.get("Parent"):
            expected.setdefault(spec["Parent"], "Blueprint*")
    found = find_bindings(archive or game_dir() / "blueprints.zip", expected)
    for row in payload.get("NativeOverrides", []):
        spec = payload[row["Field"]][row["RuntimeKey"]]
        if spec.get("Parent") and found[spec["Parent"]]["type"] not in {"BlueprintCue", "BlueprintAnswer", "BlueprintDialog"}:
            raise ValueError(f"NativeOverride {row['Target']}: unsafe parent type {found[spec['Parent']]['type']}")
        if spec.get("Key") and text_key(found[row["Target"]]["data"].get("Text")) != spec["Key"]:
            raise ValueError(f"NativeOverride {row['Target']}: localization key differs from archive")
        row["Evidence"] = found[row["Target"]]["path"]
        row["When"] = copy.deepcopy(spec["When"])
        row["Relationships"] = sorted({scenes[v["Replacement"]]["Relationship"] for v in [spec] + spec.get("Variants", [])}
                                      if row["Field"] == "NativeEpilogueEdits" else {spec["Relationship"]})
    return found
