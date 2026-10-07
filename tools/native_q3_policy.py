"""eng7-f1: build-time mirror of the specialized Q3 action-list runtime contract."""
from pathlib import Path
import re
from tools.game_blueprints import blueprint_type

FINAL = "2b4a5c01a192d1f4aa8c9d32aa149727"
VERDICT = "aeccec94d6e3246488d7f13577a8380d"
COMPLETION = "dd2a29da89d7abe47a7342470f56b275"
SETUP = "559deab3edca4764a8475948397113a7"
KIANA_REVIVE = "0d8253caf33f7474799c2130fbe15907"
DOG_REVIVE = "4008e4f363bf551498c3a99a12a60cc3"
TYPES = {SETUP: "CommandAction", KIANA_REVIVE: "CommandAction", DOG_REVIVE: "CommandAction", FINAL: "BlueprintEtude", VERDICT: "BlueprintCue", COMPLETION: "CommandAction"}


def boolean(value):
    return "True" if value is True else "False"


def checker(data):
    def condition(item):
        kind = blueprint_type(item)
        if kind == "EtudeStatus":
            return "E:" + item["m_Etude"].removeprefix("!bp_") + ":" + ":".join(boolean(item[f]) for f in
                ("Not", "NotStarted", "Started", "Playing", "CompletionInProgress", "Completed"))
        if kind == "OrAndLogic":
            return "L:" + boolean(item["Not"]) + ":" + checker(item["ConditionsChecker"])
        return "unreviewed"
    return data["Operation"] + "[" + ";".join(condition(c) for c in data["Conditions"]) + "]"


def unit_shape(unit):
    if unit and blueprint_type(unit) == "UnitFromSpawner":
        return unit["Spawner"]["_entity_id"] + "@" + unit["Spawner"]["SceneAssetGuid"]
    return "unreviewed"


def shape(data):
    def action(item):
        kind = blueprint_type(item)
        if kind == "Conditional":
            return "C:" + checker(item["ConditionsChecker"]) + "{" + shape(item["IfTrue"]) + "}{" + shape(item["IfFalse"]) + "}"
        if kind == "Spawn":
            return "S:" + ",".join(s["_entity_id"] + "@" + s["SceneAssetGuid"] for s in item["Spawners"]) + "{" + shape(item["ActionsOnSpawn"]) + "}"
        if kind == "PlayCutscene":
            return kind + ":" + item["m_Cutscene"].removeprefix("!bp_") + ":" + boolean(item["PutInQueue"]) + ":" + boolean(item["CheckExistence"]) + ":" + str(len(item["Parameters"]["Parameters"])) + "".join(
                ":" + p["Name"] + ":" + p["Type"] + ":" + unit_shape(p["Evaluator"]) for p in item["Parameters"]["Parameters"])
        if kind == "StopCutscene":
            return kind + ":" + item["m_Cutscene"].removeprefix("!bp_") + ":" + unit_shape(item["WithUnit"])
        if kind in {"StartEtude", "CompleteEtude"}:
            return kind + ":" + item["Etude"].removeprefix("!bp_") + ":" + boolean(item["Evaluate"]) + ":" + boolean(item["EtudeEvaluator"] is None)
        return "unreviewed"
    return ";".join(action(a) for a in data["Actions"])


def check(spec, found):
    source = (Path(__file__).resolve().parents[1] / "src/NativeQ3Recovery.cs").read_text(encoding="utf-8-sig")
    signatures = dict(re.findall(r'const string (\w+Shape) = "([^"]+)"', source))
    etude, cue, complete = (found[g]["data"] for g in (FINAL, VERDICT, COMPLETION))
    triggers = [c for c in etude["Components"] if blueprint_type(c) == "EtudePlayTrigger"]
    empty = dict(Operation="And", Conditions=[])
    if (spec.get("Target") != FINAL or spec.get("Relationship") != "kiana"
        or not spec.get("When") or any("trickster.now" not in g or not
            ({"kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back"}.intersection(g)
             or len(g) == 3 and set(g) == {"trickster.now", "kiana.trickster.returned", "kiana.trickster.cost.guests_robbed"}) for g in spec["When"])
        or len(triggers) != 1 or triggers[0]["Conditions"] != empty
        or shape(triggers[0]["Actions"]) != signatures["TriggerShape"]
        or shape(cue["OnStop"]) != signatures["VerdictShape"]
        or shape(complete["Action"]) != signatures["CompletionShape"] or complete["EntryCondition"] != empty
        or etude["m_StartsOnComplete"] != ["!bp_6d3fb96f9b60c0449a01add4be5c4a49"]):
        raise ValueError("NativeOverride kiana.q3_recovery: declaration/action sites differ from reviewed runtime policy")

    setup, kiana, dog = (found[g]["data"] for g in (SETUP, KIANA_REVIVE, DOG_REVIVE))
    bad = "C:And[E:d983621f7b887b043acb0c43186bf824:False:False:False:True:False:False]"
    victim = "5c8fbdc4-67d2-439f-9507-5214166213bf@96778946654e0694da9678eff26d097f"
    girl = "d08b7760-eafc-43d6-901d-2b1298ebb0fe@96778946654e0694da9678eff26d097f"
    wife = "935cd45a-387a-46ab-bc8a-42a209657f3f@96778946654e0694da9678eff26d097f"
    dog_id = "3a8f7f55-8a41-4987-8825-addaed6e0ab7@96778946654e0694da9678eff26d097f"
    def revival(unit):
        return "StopCutscene:03346ed57a7462443a6be887591150ca:" + unit + ";PlayCutscene:3644cee8047af074b9f67299adf8e0fb:False:True:1:Unit:Unit:" + unit
    if (len(setup["Action"]["Actions"]) != 5 or shape(dict(Actions=setup["Action"]["Actions"][:1])) != bad + "{S:" + victim + "{}}{S:" + wife + "," + girl + "{}}"
            or shape(kiana["Action"]) != bad + "{" + revival(victim) + "}{" + revival(girl) + "}"
            or shape(dog["Action"]) != revival(dog_id)
            or any(c["EntryCondition"] != empty for c in (setup, kiana, dog))):
        raise ValueError("NativeOverride kiana.q3_recovery: individual action sites differ from reviewed runtime policy")
