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
time with a safe alternative. eng7-f6b retains F1 state-scoped answer DisplayText
replacements and eng7-l04 reviewed object/action/journal targets. JOURNAL selects
localized fields at read time and never changes progression or XP.

Runtime safety stays in NativeEpilogueEdit/NativeGate/NativeWorldReconciliation: complementary original
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
# eng7-f1: the runtime answer policy is the sole whitelist.
from tools.native_answer_policy import contracts as answer_contracts, check as check_answer
from tools import native_q3_policy
# end eng7-f1

ROOT = Path(__file__).resolve().parents[1]
TYPES = dict(cue="BlueprintCue", slide="BlueprintCue", answer="BlueprintAnswer",
             objective="BlueprintQuestObjective", dialog="BlueprintDialog", etude="BlueprintEtude")
# eng7-f1: answer presentation is registered alongside existing native reconciliations.
FIELDS = ("NativeEpilogueEdits", "NativeEpilogueSuppressions", "NativeGates", "NativeObjectiveSettlements", "NativeAnswerEdits")
# end eng7-f1

# eng7-l04: extend the q6b registry with reviewed world/journal target types.
TYPES.update(quest="BlueprintQuest", **{"script-zone": "BlueprintScriptZone"})
FIELDS += ("NativeWorldReconciliations",)


@lru_cache(maxsize=1)
def world_contracts():
    rules = (ROOT / "src/Story.cs").read_text(encoding="utf-8-sig")
    body = rules.split(" ReviewedNativeWorldTargets =", 1)[1].split("};", 1)[0]
    return dict(re.findall(r'\["([a-f0-9]{32})"\]\s*=\s*"([^"\n]+)"', body))


def world_group_supported(target, relationship, group):
    from tools.native_gate_contract_lint import requirements
    if not isinstance(group, list) or not all(isinstance(flag, str) for flag in group):
        return False
    contract = world_contracts().get(target, "")
    if contract.endswith(":JOURNAL"):
        return relationship == "kiana" and "trickster.now" in group and any(flag in group for flag in requirements()[0])
    if contract == "etude:HIDE-OBJECTS":
        return relationship == "eliandra" and {"trickster.now", "eliandra.trickster.buried"}.issubset(group)
    return contract in {"etude:RETIRE-PRISONER", "script-zone:RETIRE-ESCAPE"} and relationship == "minagho_chivarro" and {
        "trickster.now", "minagho_chivarro.trickster.minagho_in"}.issubset(group)


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
    # eng7-l04: only an exact reviewed type/action pair may reach the new adapter.
    if action in {"HIDE-OBJECTS", "RETIRE-PRISONER", "RETIRE-ESCAPE", "JOURNAL"}:
        if world_contracts().get(target) != target_type + ":" + action or spec.get("Target") != target:
            raise ValueError(f"NativeOverride {target}: no reviewed world target contract")
        return "NativeWorldReconciliations", target
    # eng7-f1: text-only native answer identity is retained by DisplayText, with no authored actions.
    if action == "REPLACE" and target_type == "answer":
        policy = answer_contracts().get(target)
        if policy is None:
            raise ValueError(f"NativeOverride {target}: no reviewed safe native answer-policy contract")
        if spec.get("AnswerList") != policy["AnswerList"] or spec.get("Key") != policy["Key"]:
            raise ValueError(f"NativeOverride {target}: answer list/key differs from runtime contract")
        if set(spec) != {"AnswerList", "Key", "Relationship", "Text", "When"}:
            raise ValueError(f"NativeOverride {target}: text-only answer contract forbids behavior fields")
        return "NativeAnswerEdits", target
    # end eng7-f1
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
    # eng-final / E-Q8-01 + E-Q8-06: native ending guards read the same
    # finite live-body inputs as Rules.Validate, never arbitrary authored keys.
    latest = rules.split("LatestStateRuntime =", 1)[1].split("}", 1)[0]
    known.update(re.findall(r'"([^"\n]+)"', latest))
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
    # eng7-l04: reject unsupported Q3 declarations before publication.
    from tools.native_gate_contract_lint import validate
    from tools import kiana_native_policy  # eng7-f6b
    validate(payload)
    registered = {(row["Field"], row["RuntimeKey"]) for row in payload.get("NativeOverrides", [])}
    missing = [(field, key) for field in FIELDS for key in payload.get(field, {}) if (field, key) not in registered]
    if missing:
        raise ValueError(f"NativeOverrides: unregistered native edits {missing}; use register_legacy/declare")
    known = _known(payload)
    scenes = {s["Id"]: s for s in payload.get("Scenes", [])}
    expected = kiana_native_policy.expected()  # eng7-f6b: include every inspected parent
    for row in payload.get("NativeOverrides", []):
        target = row["Target"]
        spec = payload[row["Field"]][row["RuntimeKey"]]
        _delivery(target, row["TargetType"], row["Action"], row["RuntimeKey"], spec)
        expected[target] = TYPES[row["TargetType"]]
        # eng7-f1: validate both Q3 action attachment sites and the native completion command.
        if row["RuntimeKey"] == "kiana.q3_recovery":
            expected.update(native_q3_policy.TYPES)
        # end eng7-f1
        # eng7-f1: the only earned histories reviewed for these Kiana answer rewrites.
        if row["Field"] == "NativeAnswerEdits":
            if (spec.get("Relationship") != "kiana" or "kiana" not in payload.get("Relationships", {})
                or not isinstance(spec.get("Text"), str) or not spec["Text"].strip()
                or any("trickster.now" not in g or not {"kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back"}.intersection(g)
                       for g in spec.get("When", []))):
                raise ValueError(f"NativeOverride {target}: answer replacement requires current Trickster and paid guest recovery")
            policy = answer_contracts()[target]
            expected[policy["AnswerList"]] = "BlueprintAnswersList"
            expected[policy["NextCue"]] = "BlueprintCue"
            if policy["SeenCue"]:
                expected[policy["SeenCue"]] = "BlueprintCue"
        # end eng7-f1
        variants = [spec] + spec.get("Variants", [])
        for variant in variants:
            groups = variant.get("When", [])
            if not groups or any(not group or not {"trickster.now", "trickster.ever"}.intersection(group) for group in groups):
                raise ValueError(f"NativeOverride {target}: every When group requires trickster.now/ever")
            # eng7-l04: journal changes require full payment; burial/recruitment use only existing earned states.
            if row["Field"] == "NativeWorldReconciliations" and any(
                    not world_group_supported(target, spec.get("Relationship"), group) for group in groups):
                raise ValueError(f"NativeOverride {target}: unsupported earned world state")
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
    # eng7-l04: native-action/object evidence and localization fields must match as well as GUID/type.
    verify_world_targets(payload, found)
    for row in payload.get("NativeOverrides", []):
        spec = payload[row["Field"]][row["RuntimeKey"]]
        # eng7-f1
        if row["RuntimeKey"] == "kiana.q3_recovery":
            native_q3_policy.check(spec, found)
        # end eng7-f1
        # eng7-f1: reject behavior drift at export as well as at runtime.
        if row["Field"] == "NativeAnswerEdits":
            check_answer(row["Target"], spec, found)
        # end eng7-f1
        # eng7-f6b: sequence membership is supported only for reviewed in-place text delivery.
        if row["Target"] in kiana_native_policy.contracts():
            kiana_native_policy.check(row["Target"], spec, found)
        allowed_parents = {"BlueprintCue", "BlueprintAnswer", "BlueprintDialog"}
        if row["Target"] in kiana_native_policy.contracts():
            allowed_parents.update({"BlueprintCueSequence", "BlueprintSequenceExit"})
        if spec.get("Parent") and found[spec["Parent"]]["type"] not in allowed_parents:
            raise ValueError(f"NativeOverride {row['Target']}: unsafe parent type {found[spec['Parent']]['type']}")
        if spec.get("Key") and text_key(found[row["Target"]]["data"].get("Text")) != spec["Key"]:
            raise ValueError(f"NativeOverride {row['Target']}: localization key differs from archive")
        row["Evidence"] = found[row["Target"]]["path"]
        row["When"] = copy.deepcopy(spec["When"])
        row["Relationships"] = sorted({scenes[v["Replacement"]]["Relationship"] for v in [spec] + spec.get("Variants", [])}
                                      if row["Field"] == "NativeEpilogueEdits" else {spec["Relationship"]})
    return found


# eng7-l04 begin: declarations for E-Q7-32, preserving every native ID and quest action.
BURIAL = "a6e26159152a54c47a70ec91495499cf"
PRISON = "0544675ba14e81e48bb0965823c33efe"
ESCAPE = "067bd492b3a377d4e9112d929ec62fdb"
CORPSE_IDS = ("36388267-9dfb-410c-ac7c-e6a96538ce7b", "8ea39933-3fd6-43fa-9d82-b1dbe03ccadf",
              "6cacdba8-376e-41ff-9728-5eeff69e5021", "61dd594e-2a0e-47f5-86b5-937dccccce52")
BURIAL_SCENE = "42332f3087ee8e34b8fd90aa34d64614"
PRISON_SCENE = "1c9b1a8d692860647848123dc61f3baa"

# Authored journal variants describe only the paid release already made in kiana_trickster.
# The original quest/objective IDs, completion actions, unrecovered histories and XP remain native.
JOURNALS = {
    "5a5a533c9ce630a48b877f9a194840cb": (
        "b46d5fa9-4ea9-4e7a-9997-b95c458bd095", "", "",
        "The wedding guests are home. Arsinoe broke the ransomed soul stones in Drezen, but Sunhammer is still at large. "
        "Seelah means to find the jeweler who sold her friends to the demons and make him answer for it."),
    "7ac73c0b5de939b4b824a0aac54ba5f2": (
        "ef5f2b7e-8e8c-4338-a8c1-acce1e65618f", "e4e4c32c-68d4-4542-93bb-2ea6fc09e4b8", "Find Sunhammer's hideout",
        "Arsinoe's vision points to a cave beneath a cliff in the southern Worldwound, on the edge of the Winged Wood. "
        "The guests' souls have already been returned, but the cave may lead Seelah and the Commander to Sunhammer."),
    "83527eddea019674cb123a6a52bdf169": (
        "e07e3559-8973-46ee-8c3f-85326d63c8aa", "8f8bb69c-77fb-4b1a-af7a-589fa79bcb17", "Confront Sunhammer and recover the stolen jewelry",
        "The cave is a Baphomite hideout. Sunhammer kept the wedding jewelry after selling the soul stones back to Drezen. "
        "Seelah intends to retrieve the empty settings and settle accounts with the jeweler."),
    "5b1e04caadc42114281d29db76c19c4f": (
        "884bf99f-bd1e-42ea-ac54-996fe4e8dddb", "fe6c829a-52b3-489e-814f-b9cbe22a8cd6", "Return the jewelry to Drezen",
        "Seelah has the empty settings. The souls they held were freed in Drezen after the Commander paid for their return. "
        "Bring the jewelry to the infirmary and meet the families whose wedding Sunhammer ruined."),
    "ba857f1c903988f47a70a9d6a2d861fa": (
        "247343ee-0c87-4495-9857-310cc31fa663", "", "",
        "Jannah, the convicted deserter, wants to join her friends in pursuing Sunhammer. The wedding guests have been "
        "freed, but the jeweler who stole their souls has yet to answer for it."),
}


def integrate_world(payload):
    """Wire every mapped E-Q7-32 site through the existing native registry."""
    rows = [(BURIAL, "eliandra", "HIDE-OBJECTS", [["trickster.now", "eliandra.trickster.buried"]]),
            (PRISON, "minagho_chivarro", "RETIRE-PRISONER", [["trickster.now", "minagho_chivarro.trickster.minagho_in"]]),
            (ESCAPE, "minagho_chivarro", "RETIRE-ESCAPE", [["trickster.now", "minagho_chivarro.trickster.minagho_in"]])]
    for target, relationship, action, when in rows:
        declare(payload, source=__name__ + ".eng7_l04", target=target, target_type="script-zone" if target == ESCAPE else "etude",
                action=action, spec=dict(Target=target, Relationship=relationship, When=when))
    for target, (description_key, title_key, title, description) in JOURNALS.items():
        declare(payload, source=__name__ + ".eng7_l04", target=target,
                target_type="quest" if target == "5a5a533c9ce630a48b877f9a194840cb" else "objective", action="JOURNAL",
                spec=dict(Target=target, Relationship="kiana", When=[["trickster.now", "kiana.trickster.guests_ransomed"],
                          ["trickster.now", "kiana.trickster.guests_bought_back"]], DescriptionKey=description_key,
                          Description=description, TitleKey=title_key, Title=title))


def _walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def verify_world_targets(payload, found):
    for target, spec in payload.get("NativeWorldReconciliations", {}).items():
        data = found[target]["data"]
        error = f"NativeOverride {target}: native world evidence differs from reviewed contract"
        if target == BURIAL:
            displays = [row for row in _walk(data.get("Components")) if row.get("$type", "").endswith(", HideMapObject")
                        and row.get("MapObject", {}).get("MapObject", {}).get("_entity_id") in CORPSE_IDS]
            if (data.get("m_LinkedAreaPart") != "!bp_72672fb14139b1443a6700473cce04d7" or len(displays) != 4
                    or {row["MapObject"]["MapObject"]["_entity_id"] for row in displays} != set(CORPSE_IDS)
                    or any(row.get("Unhide") is not True or row["MapObject"].get("$type", "").split(", ")[-1] != "MapObjectFromScene"
                           or row["MapObject"]["MapObject"].get("SceneAssetGuid") != BURIAL_SCENE for row in displays)):
                raise ValueError(error)
        elif target == PRISON:
            triggers = [row for row in data.get("Components", []) if row.get("$type", "").endswith(", EtudePlayTrigger")
                        and any(s.get("_entity_id") == "9bf297f2-559f-4823-8471-c9761999538a" for a in row.get("Actions", {}).get("Actions", [])
                                for s in a.get("Spawners", []))]
            if len(triggers) != 1:
                raise ValueError(error)
            trigger = triggers[0]
            actions = trigger["Actions"]["Actions"]
            conditions = trigger.get("Conditions", {})
            status = conditions.get("Conditions", [{}])[0]
            if (len(actions) != 2 or conditions.get("Operation") != "And" or len(conditions.get("Conditions", [])) != 1
                    or status.get("$type", "").split(", ")[-1] != "EtudeStatus" or status.get("m_Etude") != "!bp_eff0ca2318f96c049b5c9e6785eac196"
                    or not status.get("Playing") or any(status.get(k) for k in ("Not", "NotStarted", "Started", "Completed", "CompletionInProgress"))
                    or actions[0].get("$type", "").split(", ")[-1] != "Spawn" or actions[0].get("RespawnIfDead") is not False
                    or actions[0].get("ActionsOnSpawn", {}).get("Actions") != [] or len(actions[0].get("Spawners", [])) != 1
                    or actions[0]["Spawners"][0].get("SceneAssetGuid") != PRISON_SCENE
                    or actions[1].get("$type", "").split(", ")[-1] != "ScriptZoneActivate" or actions[1].get("UseEvaluator") is not False
                    or actions[1].get("ScriptZoneEvaluator") is not None
                    or actions[1].get("ScriptZone", {}).get("_entity_id") != "b8efebdc-2c24-40e6-b189-04fc39ad52a8"
                    or actions[1]["ScriptZone"].get("SceneAssetGuid") != PRISON_SCENE):
                raise ValueError(error)
        elif target == ESCAPE:
            actions = data.get("EnterActions", {}).get("Actions", [])
            if (data.get("TriggerConditions") != dict(Operation="And", Conditions=[]) or data.get("ExitActions", {}).get("Actions") != []
                    or len(actions) != 1 or actions[0].get("$type", "").split(", ")[-1] != "PlayCutscene"
                    or actions[0].get("m_Cutscene") != "!bp_ee638b3fc29d95848aee5bdb74821aaf"
                    or actions[0].get("PutInQueue") is not False or actions[0].get("CheckExistence") is not True
                    or actions[0].get("Parameters", {}).get("Parameters") != []):
                raise ValueError(error)
        else:
            if (text_key(data.get("Description")) != spec.get("DescriptionKey") or not spec.get("Description")
                    or bool(spec.get("TitleKey")) != bool(spec.get("Title"))
                    or spec.get("TitleKey") and text_key(data.get("Title")) != spec["TitleKey"]):
                raise ValueError(error)
# eng7-l04 end
# eng7-l03: reviewed inventory joins the existing registry; uncovered evidence
# stays a failing review entry, never an executable declaration or a new selector.
def inventory(payload, expectations, backlog):
    item = next(i for i in backlog["items"] if i["id"] == expectations["Item"])
    rows = expectations["Findings"]
    ids = [r["Id"] for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != set(item["finding_ids"]):
        raise ValueError("Native inventory: missing, duplicate or unexpected mapped finding")
    fixtures = expectations["Fixtures"]
    mapped = {f["id"]: f for f in backlog["findings"]}
    registry = {r["Target"]: r for r in payload.get("NativeOverrides", [])}
    known = _known(payload)
    results = []
    for row in rows:
        finding = mapped[row["Id"]]
        if row["Route"] != finding["route"] or row["Scene"] != finding["scene"]:
            raise ValueError("Native inventory: finding provenance drift " + row["Id"])
        if not row["Targets"] or not set(finding.get("native_target_guids", [])).issubset(row["Targets"]):
            raise ValueError("Native inventory: omitted cited GUID " + row["Id"])
        if not row["Dependency"] or any(not g or not {"trickster.now", "trickster.ever"}.intersection(g)
                                         for g in row["Dependency"]):
            raise ValueError("Native inventory: missing earned Trickster dependency " + row["Id"])
        unknown = {f.removeprefix("!") for g in row["Dependency"] for f in g} - known
        if unknown:
            raise ValueError(f"Native inventory: unknown dependency {row['Id']}: {sorted(unknown)}")
        for guid in row["Targets"]:
            fixture = fixtures.get(guid)
            if fixture is None or not fixture.get("Data") or not fixture.get("Path"):
                raise ValueError("Native inventory: missing serialized fixture " + guid)
            declaration = registry.get(guid)
            spec = payload[declaration["Field"]][declaration["RuntimeKey"]] if declaration else None
            # AnswerLists and Herrax's question are context: the conflicting reply,
            # rather than the legitimate question, requires replacement.
            context = fixture["Type"] == "BlueprintAnswersList" or (
                row["Route"] == "herrax" and fixture["Type"] == "BlueprintAnswer")
            # eng7-f6c begin: Answer_0784 asks about a future, not a posthumous fate.
            # It has no OnSelect effects. Correct Cue_0785, retaining the useful
            # question and never aliasing the new reply to trapped-voice history.
            context = context or (row["Id"] == "terendelev:003"
                                  and guid == "fd39fd84212de2047b6b887c9a9cf28e")
            # eng7-f6c end
            results.append(dict(Finding=row["Id"], Route=row["Route"], Target=guid, Path=fixture["Path"],
                Dependency=row["Dependency"], Status="context" if context else "registered_unevaluated" if spec else "FAIL_UNCOVERED",
                Spec=copy.deepcopy(spec), Source=declaration["Source"] if declaration else None))
    if not set(expectations["Siblings"]).issubset(fixtures):
        raise ValueError("Native inventory: missing sibling fixture")
    return results
