"""F2 native return safety (tools/return_safety.py): the Main.cs:226-239 contract on synthetic fixtures, the allowlist
rules, and (when blueprints.zip is present) the real Areelu reveal pair that the contract rejects."""
import copy
import io
import json
import os
from pathlib import Path
import sys
from tests.temp_directory import temporary_directory
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import return_safety  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "return-safety-fixtures"
CUE, LIST = "c" * 32, "a" * 32


def load(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def reader(blueprints):
    return lambda guid: blueprints.get(guid)


def scene(cue=CUE, lists=(LIST,), sid="x.inline"):
    return {"Id": sid, "NativeReturnCue": cue, "AnswerLists": list(lists)}


class ReturnSafetyRuleTests(unittest.TestCase):
    def test_pass_fixture(self):
        self.assertEqual(return_safety.scene_problems(scene(), reader(load("pass.json"))), [])

    def test_fail_fixture_reports_every_rule(self):
        bad = return_safety.scene_problems(scene(), reader(load("fail.json")))
        self.assertEqual(sorted(bad), sorted([
            "cue.ShowOnce", "cue.ShowOnceCurrentDialog", "cue.Conditions", "cue.OnShow", "cue.OnStop", "cue.Continue",
            "cue.Experience=Normal", "cue.AlignmentShift", "cue.Answers=2", "list.ShowOnce", "list.Conditions",
            "list.MythicRequirement=Trickster", "list.AlignmentRequirement=Good"]))

    def test_each_rule_alone(self):
        base = load("pass.json")
        cases = [(CUE, "ShowOnce", True, "cue.ShowOnce"),
                 (CUE, "Conditions", {"Operation": "And", "Conditions": [{"$type": "x, FlagUnlocked"}]}, "cue.Conditions"),
                 (CUE, "OnStop", {"Actions": [{"$type": "x, StartEtude"}]}, "cue.OnStop"),
                 (CUE, "Continue", {"Cues": ["!bp_" + "d" * 32], "Strategy": "First"}, "cue.Continue"),
                 (CUE, "Answers", ["!bp_" + "b" * 32], "cue.Answers[0]=%s is not the scene's answer list" % ("b" * 32)),
                 (CUE, "PrototypeLink", "!bp_" + "e" * 32, "cue.PrototypeLink (inherited fields cannot be checked)"),
                 (LIST, "ShowOnce", True, "list.ShowOnce"),
                 (LIST, "AlignmentRequirement", "Evil", "list.AlignmentRequirement=Evil")]
        for guid, key, value, reason in cases:
            with self.subTest(reason=reason):
                bps = copy.deepcopy(base)
                bps[guid][key] = value
                self.assertEqual(return_safety.scene_problems(scene(), reader(bps)), [reason])

    def test_resolution_failures(self):
        bps = load("pass.json")
        self.assertEqual(return_safety.scene_problems(scene(cue="f" * 32), reader(bps)), ["cue not found in blueprints.zip"])
        self.assertEqual(return_safety.scene_problems(scene(cue=LIST), reader(bps)), ["cue is a BlueprintAnswersList, not a BlueprintCue"])
        self.assertEqual(return_safety.scene_problems(scene(lists=(LIST, CUE)), reader(bps)),
                         ["scene has 2 AnswerLists (Main.cs:229 calls AnswerLists.Single())"])

    def test_scenes_without_a_return_are_ignored(self):
        failures, allowed = return_safety.check([{"Id": "plain", "NativeReturnCue": None}], reader({}), {})
        self.assertEqual((failures, allowed), ([], []))


class ReturnSafetyAllowlistTests(unittest.TestCase):
    def entry(self, **kw):
        e = {"cue": CUE, "reasons": ["cue.ShowOnce"], "reason": "native cue shows once", "todo": "decide the return"}
        e.update(kw)
        return e

    def bps(self):
        bps = load("pass.json")
        bps[CUE]["ShowOnce"] = True
        return reader(bps)

    def test_unlisted_violation_is_hard(self):
        failures, allowed = return_safety.check([scene()], self.bps(), {})
        self.assertEqual(len(failures), 1)
        self.assertEqual((failures[0]["scene"], failures[0]["cue"], failures[0]["reasons"]), ("x.inline", CUE, ["cue.ShowOnce"]))
        self.assertEqual(allowed, [])

    def test_exact_entry_is_known_not_hard(self):
        failures, allowed = return_safety.check([scene()], self.bps(), {"x.inline": self.entry()})
        self.assertEqual(failures, [])
        self.assertEqual(allowed[0]["todo"], "decide the return")

    def test_stale_or_widened_entries_are_hard(self):
        for name, allow, bps in [("fixed", {"x.inline": self.entry()}, reader(load("pass.json"))),
                                 ("other reasons", {"x.inline": self.entry(reasons=["cue.OnShow"])}, self.bps()),
                                 ("other cue", {"x.inline": self.entry(cue="f" * 32)}, self.bps()),
                                 ("missing scene", {"x.inline": self.entry(), "gone": self.entry()}, self.bps())]:
            with self.subTest(name=name):
                failures, _ = return_safety.check([scene()], bps, allow)
                self.assertEqual(len(failures), 1, failures)

    def test_allowlist_entries_need_reason_and_todo(self):
        with temporary_directory() as tmp:
            path = Path(tmp) / "allow.json"
            path.write_text(json.dumps({"x.inline": self.entry(todo="")}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "lacks todo"):
                return_safety.load_allowlist(path)

    def test_repository_allowlist_is_valid(self):
        return_safety.load_allowlist(return_safety.ALLOWLIST)


GAME = Path(os.environ.get("RRT_GAME_DIR") or r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")


@unittest.skipUnless((GAME / "blueprints.zip").exists(), "blueprints.zip not installed")
class ReturnSafetyGameTests(unittest.TestCase):
    """FakeYaniel_ToAreelu/AnswersList_0002 is returned to by Cue_0006 (Conditions: FakeYanielFreed) and Cue_0014."""
    REVEAL_LIST = "4ab7a78f96a994446a56a9bc27ac2bfb"

    @classmethod
    def setUpClass(cls):
        cls.read = return_safety.ZipReader(GAME)

    def test_areelu_reveal_cue_0006_fails_on_its_conditions(self):
        bad = return_safety.scene_problems(scene(cue="b618fff15d921894e84b9b2fe9efaa39", lists=(self.REVEAL_LIST,)), self.read)
        self.assertIn("cue.Conditions", bad)

    def test_story_fixture_through_the_cli(self):
        with temporary_directory() as tmp:
            story = Path(tmp) / "Story.json"
            story.write_text(json.dumps({"Scenes": [scene(cue="b618fff15d921894e84b9b2fe9efaa39", lists=(self.REVEAL_LIST,),
                                                          sid="areelu.reveal")]}), encoding="utf-8")
            out = io.StringIO()
            saved, sys.stdout = sys.stdout, out
            try:
                code = return_safety.main(["--story", str(story), "--game", str(GAME), "--allowlist", ""])
            finally:
                sys.stdout = saved
            self.assertEqual(code, 1, out.getvalue())
            self.assertIn("HARD areelu.reveal cue b618fff15d921894e84b9b2fe9efaa39: cue.Conditions", out.getvalue())


if __name__ == "__main__":
    unittest.main()
