"""E2 gate lints (tools/gate_lint.py, handoff 17): one-flag groups and scenes relying on the tirabade default."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import gate_lint  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "gate-lint-fixtures" / "story.json"


def story():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class GateLintTests(unittest.TestCase):
    def test_pass_fixture(self):
        self.assertEqual(gate_lint.check(story(), {"a_cup"}), dict(singleton_groups=[], implicit_relationship=[]))

    def test_all_singleton_groups_fail_everywhere(self):
        s = story()
        groups = [["x.one"], ["x.two"]]
        s["Scenes"][1]["RequiresAnyGroups"] = groups
        s["Scenes"][1]["Nodes"][0]["Paragraphs"][0]["AnyGroups"] = groups
        s["Presences"]["x.presence"]["RequiresAnyGroups"] = groups
        s["Books"]["x.book"]["Entries"][0]["AnyGroups"] = groups
        s["Books"]["x.book"]["Entries"][0]["Lines"][0]["AnyGroups"] = groups
        bad = gate_lint.check(s, {"a_cup"})["singleton_groups"]
        self.assertEqual([x.split(":")[0] for x in bad], ["scene x.scene", "paragraph x.scene/n/0", "presence x.presence",
                                                         "book entry x.book/e1", "book line x.book/e1/0"])
        self.assertTrue(all("use Requires or one OR-group" in x for x in bad))

    def test_one_singleton_among_groups_fails(self):
        s = story()
        s["Scenes"][1]["RequiresAnyGroups"] = [["x.one", "x.two"], ["x.three"]]
        bad = gate_lint.check(s, {"a_cup"})["singleton_groups"]
        self.assertEqual(len(bad), 1)
        self.assertIn("['x.three'] among 2 groups are plain requirements; move them to Requires", bad[0])

    def test_single_group_and_real_cnf_pass(self):
        s = story()
        for groups in ([["x.one"]], [["x.one", "x.two"]], [["x.one", "x.two"], ["x.three", "x.two"]]):
            with self.subTest(groups=groups):
                s["Scenes"][1]["RequiresAnyGroups"] = groups
                self.assertEqual(gate_lint.check(s, {"a_cup"})["singleton_groups"], [])

    def test_implicit_relationship(self):
        s = story()
        del s["Scenes"][1]["Relationship"]
        bad = gate_lint.check(s, {"a_cup"})["implicit_relationship"]
        self.assertEqual(bad, ["scene x.scene: declare Relationship explicitly; the loader defaults it to tirabade (Story.cs:254)"])

    def test_legacy_list_may_only_name_scenes(self):
        bad = gate_lint.check(story(), {"a_cup", "gone"})["implicit_relationship"]
        self.assertEqual(len(bad), 1)
        self.assertIn("names gone", bad[0])

    def test_frozen_trio_list(self):
        legacy = gate_lint.load_trio_legacy()
        self.assertEqual(len(legacy), 40)
        self.assertTrue({"a_cup", "parting", "abyss_dream", "tirabade.negotiated_ending_aeon"} <= legacy)

    def test_repository_story_passes(self):
        path = ROOT / "development" / "Story.json"
        res = gate_lint.check(json.loads(path.read_text(encoding="utf-8")))
        self.assertEqual(res, dict(singleton_groups=[], implicit_relationship=[]))


if __name__ == "__main__":
    unittest.main()
