"""eng7-f1: build-time mirror of the specialized Q3 action-list runtime contract."""
from pathlib import Path
import re
from tools.game_blueprints import blueprint_type

FINAL = "2b4a5c01a192d1f4aa8c9d32aa149727"
VERDICT = "aeccec94d6e3246488d7f13577a8380d"
COMPLETION = "dd2a29da89d7abe47a7342470f56b275"
TYPES = {FINAL: "BlueprintEtude", VERDICT: "BlueprintCue", COMPLETION: "CommandAction"}


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


def shape(data):
    def action(item):
        kind = blueprint_type(item)
        if kind == "Conditional":
            return "C:" + checker(item["ConditionsChecker"]) + "{" + shape(item["IfTrue"]) + "}{" + shape(item["IfFalse"]) + "}"
        if kind == "Spawn":
            return "S:" + ",".join(s["_entity_id"] + "@" + s["SceneAssetGuid"] for s in item["Spawners"]) + "{" + shape(item["ActionsOnSpawn"]) + "}"
        if kind == "PlayCutscene":
            return kind + ":" + item["m_Cutscene"].removeprefix("!bp_") + ":" + boolean(item["PutInQueue"]) + ":" + boolean(item["CheckExistence"]) + ":" + str(len(item["Parameters"]["Parameters"]))
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
            {"kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back"}.intersection(g) for g in spec["When"])
        or len(triggers) != 1 or triggers[0]["Conditions"] != empty
        or shape(triggers[0]["Actions"]) != signatures["TriggerShape"]
        or shape(cue["OnStop"]) != signatures["VerdictShape"]
        or shape(complete["Action"]) != signatures["CompletionShape"] or complete["EntryCondition"] != empty
        or etude["m_StartsOnComplete"] != ["!bp_6d3fb96f9b60c0449a01add4be5c4a49"]):
        raise ValueError("NativeOverride kiana.q3_recovery: declaration/action sites differ from reviewed runtime policy")
