"""eng7-f1: archive mirror of NativeAnswerEdit.Check; policies come from Story.cs.

This is deliberately narrow: text presentation only, with every behavior field
of the three reviewed Kiana answers checked. New native policies need a runtime
review. A matching GUID/type/localization key alone is insufficient evidence.
"""
from functools import lru_cache
from pathlib import Path
import re

from tools.game_blueprints import blueprint_type, text_key


@lru_cache(maxsize=1)
def contracts():
    source = (Path(__file__).resolve().parents[1] / "src/Story.cs").read_text(encoding="utf-8-sig")
    return {target: dict(zip(("AnswerList", "Key", "NextCue", "SeenCue"), fields))
            for target, *fields in re.findall(
                r'\["([a-f0-9]{32})"\] = new NativeAnswerPolicy\("([a-f0-9]{32})", "([^"]+)", "([a-f0-9]{32})", "([a-f0-9]*)"\)', source)}


def check(target, spec, found):
    policy = contracts()[target]
    data = found[target]["data"]
    parent = found[policy["AnswerList"]]["data"]
    empty = dict(Operation="And", Conditions=[])
    shown = data.get("ShowConditions", {})
    conditions = shown.get("Conditions", [])
    seen = policy["SeenCue"]
    show = shown == empty if not seen else (shown.get("Operation") == "And" and len(conditions) == 1
        and blueprint_type(conditions[0]) == "CueSeen" and conditions[0].get("Not") is False
        and conditions[0].get("CurrentDialog") is False and conditions[0].get("m_Cue") == "!bp_" + seen)
    defaults = dict(Components=[], ShowOnce=False, ShowOnceCurrentDialog=False, DebugMode=False,
        MythicRequirement="None", AlignmentRequirement="None", Experience="NoExperience", RequireValidCue=False,
        AddToHistory=True, ShowCheck=dict(Type="Unknown", DC=0), FakeChecks=[],
        CharacterSelection=dict(SelectionType="Clear", ComparisonStats=[]), SelectConditions=empty,
        OnSelect=dict(Actions=[]), NextCue=dict(Cues=["!bp_" + policy["NextCue"]], Strategy="First"))
    if (spec.get("AnswerList") != policy["AnswerList"] or spec.get("Key") != policy["Key"]
        or text_key(data.get("Text")) != policy["Key"] or not show
        or parent.get("Answers", []).count("!bp_" + target) != 1
        or any(data.get(key) != value for key, value in defaults.items())
        or data.get("AlignmentShift", {}).get("Value") != 0
        or data.get("AlignmentShift", {}).get("Direction") != "TrueNeutral"):
        raise ValueError(f"NativeOverride {target}: answer behavior differs from the reviewed runtime policy")
