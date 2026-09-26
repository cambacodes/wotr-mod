"""Generate a separate mechanical test story; never replace the development export."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from story_format import c, n, scene

payload = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
skills = ["SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery",
          "SkillKnowledgeArcana", "SkillKnowledgeWorld", "SkillLoreNature",
          "SkillLoreReligion", "SkillPerception", "SkillUseMagicDevice",
          "CheckDiplomacy", "CheckBluff", "CheckIntimidate"]
choices = []
for skill in skills:
    for commander_only in (True, False):
        choice = c("Attempt " + skill)
        choice["Check"] = dict(Skill=skill, DC=25, Success="success", Failure="failure",
                               CommanderOnly=commander_only)
        choices.append(choice)
payload["Scenes"].append(scene("mechanics_check_fixture", "Native check fixture", "Memory", 3, "", [
    n("start", "Narrator", "Choose a native skill check.", *choices),
    n("success", "Narrator", "The check succeeds.", c(flags=("fixture.success",))),
    n("failure", "Narrator", "The check fails; the story continues.", c(flags=("fixture.failure",))),
], Relationship="tirabade", Remote=True, optional=True,
    ContactUnit="b5e867e13503c6f41bb1316705efb4a2",
    AdditionalContactUnits=["280d4712dceb37f4a88e98f1f4c6e64f"]))
destination = ROOT / "development/native-check-fixture.json"
destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote isolated native-check fixture: {destination}")
