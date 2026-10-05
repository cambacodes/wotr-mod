"""eng8-q8b: L6 must see non-producer consumers and every native twin."""
import copy
import json
from pathlib import Path
import unittest

from tools import earned_presence_lint
from tools.crossroute_checks import left_trickster
from tools.crossroute_checks.common import Proof, blocks, verify

ROOT = Path(__file__).resolve().parents[1]


class LeftTricksterConsumerLintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))
        cls.contract = json.loads((ROOT / "tools/left_trickster_consumer_contracts.json").read_text())

    def test_all_registered_consumers_and_native_twins_are_guarded(self):
        self.assertEqual(earned_presence_lint.left_trickster_consumers(self.story), [])
        ids = {s["Id"] for s in self.story["Scenes"]}
        for name in ("trial", "gate", "stinger", "cairn", "morning", "vellexia", "yaniel", "neathers", "hunt", "gongs"):
            self.assertIn("wenduag.trickster.court." + name + ".native_visit", ids)

    def test_inherited_l13_choice_indices_survive_stronger_entry_guards(self):
        for sid in ("wenduag.trickster.court.claim", "wenduag.trickster.court.claim_in_person"):
            scene = next(s for s in self.story["Scenes"] if s["Id"] == sid)
            for node in scene["Nodes"]:
                if node["Id"] in ("after_given", "after_knelt", "after_struck"):
                    self.assertEqual(len(node["Choices"]), 2)
                    yes, leave = node["Choices"]
                    self.assertIn("wenduag.committed", yes["Set"])
                    self.assertIn("trickster.now", yes["Requires"])
                    self.assertEqual(leave["Text"], "[Leave.]")
                    self.assertTrue(leave["Abort"])
                    self.assertEqual(leave["Set"], [])
                    self.assertEqual(leave["Forbids"], ["trickster.now"])

    def test_removing_each_entry_guard_is_l6_even_without_a_reward_setter(self):
        targets = [s for s in self.story["Scenes"] if s["Id"] in self.contract["scenes"]
                   or s["Id"].startswith(self.contract["court_prefix"])]
        self.assertGreaterEqual(len(targets), 30)
        # Small complete contract fixture isolates T6c from unrelated debt and
        # avoids repeatedly solving the entire campaign for each mutation.
        for scene in targets:
            with self.subTest(scene=scene["Id"]):
                story = {"Relationships": {"wenduag": {"StartedFlag": "wenduag.started", "ClosedFlag": "wenduag.closed", "CommittedFlag": "wenduag.committed"}}, "Scenes": [copy.deepcopy(scene)],
                         "Derived": {self.contract["return_reader"]: self.contract["return_groups"]},
                         "DerivedForbids": {self.contract["return_reader"]: self.contract["return_forbids"]}}
                target = story["Scenes"][0]
                target["Requires"].remove("trickster.now")
                # The test specifically removes producer evidence: prose alone
                # still requires current power under the nominated contract.
                for node in target["Nodes"]:
                    for choice in node["Choices"]:
                        choice["Set"] = []
                model = verify.Model(story)
                findings = left_trickster.check(model, list(blocks(model)), Proof(model))
                self.assertTrue(any(f["scene"] == scene["Id"] and "T6c" in f["missing_condition"] for f in findings))

    def test_survival_reader_rejects_historical_only_or_latched_live_power(self):
        for groups in ([["wenduag.trickster.returned"]], [["wenduag.trickster.returned", "past_power"]]):
            story = copy.deepcopy(self.story)
            story["Derived"][self.contract["return_reader"]] = groups
            story.setdefault("Latches", {})["past_power"] = ["trickster.now"]
            self.assertTrue(any(self.contract["return_reader"] in e
                                for e in earned_presence_lint.left_trickster_consumers(story)))

    def test_missing_consumer_fails_instead_of_silently_reducing_coverage(self):
        story = copy.deepcopy(self.story)
        story["Scenes"] = [s for s in story["Scenes"] if s["Id"] != self.contract["scenes"][0]]
        self.assertTrue(any("missing registered" in e for e in earned_presence_lint.left_trickster_consumers(story)))


if __name__ == "__main__":
    unittest.main()
