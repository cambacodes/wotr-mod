"""E-Q7-23: producer/reader diagnostics, including nested and draft gates."""
import copy
import json
from pathlib import Path
import unittest

from tools import obligation_flow_lint as lint


class ObligationFlowTests(unittest.TestCase):
    def setUp(self):
        self.contracts = {"obligations": [dict(finding="route:001", flag="promise", scene="offer", source=["fixture"])],
                          "negative_exemptions": {}}
        self.story = {"Scenes": [dict(Id="offer", Nodes=[dict(Id="start", Choices=[dict(Set=["promise"])])])]}

    def status(self, story=None):
        return lint.lint(story or self.story, self.contracts)["findings"][0]["status"]

    def test_dead_promise_not_mistaken_for_consumer(self):
        self.assertEqual(self.status(), "dead_obligation")
        self.story["Description"] = "promise"
        self.assertEqual(self.status(), "dead_obligation")

    def test_scene_node_choice_paragraph_book_journal_and_derived_readers(self):
        fixtures = [dict(Requires=["promise"]), dict(RequiresAnyGroups=[["promise", "other"]]),
                    dict(Nodes=[dict(Id="later", Requires=["promise"])]),
                    dict(Nodes=[dict(Id="later", Choices=[dict(Forbids=["promise"])])]),
                    dict(Nodes=[dict(Id="later", Paragraphs=[dict(Requires=["promise"], Text="resolution")])])]
        for fixture in fixtures:
            with self.subTest(fixture=fixture):
                story = copy.deepcopy(self.story)
                story["Scenes"].append(dict(Id="resolution", **fixture))
                self.assertEqual(self.status(story), "consumer_review")
        for table, value in [("Books", {"book": {"Pages": [{"Requires": ["promise"]}]}}),
                             ("Relationships", {"route": {"Journal": [{"Requires": ["promise"]}]}}),
                             ("Derived", {"resolved": [["promise"]]})]:
            story = copy.deepcopy(self.story); story[table] = value
            self.assertEqual(self.status(story), "consumer_review")

    def test_negative_only_missing_producer_and_real_native_binding(self):
        self.story["Scenes"].append(dict(Id="next", Forbids=["known.lann"], Nodes=[]))
        report = lint.lint(self.story, self.contracts)
        self.assertEqual(report["unbound_forbids"][0]["flag"], "known.lann")
        for table in ["SeenCues", "SelectedAnswers", "QuestObjectives", "CompletedQuests", "CompletedEtudes", "StartedQuests", "MainCharacterFacts", "Derived", "Latches"]:
            story = copy.deepcopy(self.story); story[table] = {"known.lann": ["witness"]}
            self.assertEqual(lint.lint(story, self.contracts)["unbound_forbids"], [])

    def test_revisit_and_archival_exemptions_are_explicit(self):
        self.story["Scenes"][0]["Nodes"][0]["Choices"][0]["Abort"] = True
        self.assertEqual(self.status(), "revisit")
        c = self.contracts["obligations"][0]; c["archival"] = True
        self.assertTrue(lint.lint(self.story, self.contracts)["hard"])
        c["reason"] = "pure historical choice record; no outstanding work promised"
        self.assertEqual(self.status(), "archival")

    def test_unreachable_stub_is_not_a_completion_producer(self):
        self.story["Scenes"][0]["Nodes"] = [dict(Id="start", Choices=[dict(Abort=True)]),
                                                 dict(Id="retained_stub", Choices=[dict(Set=["stub_flag"])])]
        p, _, _, _ = lint.index(self.story)
        self.assertNotIn("offer", p)
        self.assertNotIn("stub_flag", p)

    def test_retired_scene_and_choice_have_no_producer(self):
        for target in [self.story["Scenes"][0], self.story["Scenes"][0]["Nodes"][0]["Choices"][0]]:
            target.update(Requires=["retired"], Forbids=["retired"])
            producers, _, _, _ = lint.index(self.story)
            self.assertNotIn("offer", producers)
            self.assertNotIn("promise", producers)
            del target["Requires"]; del target["Forbids"]
        # An explicit forbid override keeps the branch live for inventory.
        scene = dict(Id="offer", Requires=["lost"], Forbids=["lost"], ForbidOverrides={"lost": "returned"},
                     Nodes=[dict(Id="start", Choices=[dict(Set=["promise"])])])
        self.assertEqual(self.status({"Scenes": [scene]}), "dead_obligation")

    def test_negative_when_and_settled_journal_readers(self):
        self.story["JournalEntries"] = [{"When": [["!known.lann"]], "SettledWhen": [["promise"]]}]
        report = lint.lint(self.story, self.contracts)
        self.assertEqual(report["findings"][0]["status"], "consumer_review")
        self.assertEqual(report["unbound_forbids"][0]["flag"], "known.lann")

    def test_mutating_away_reader_returns_dead_obligation(self):
        self.story["Books"] = {"book": {"Requires": ["promise"]}}
        self.assertEqual(self.status(), "consumer_review")
        del self.story["Books"]
        self.assertEqual(self.status(), "dead_obligation")

    def test_drafts_are_separate_and_all_mapped_flags_are_registered(self):
        self.contracts["obligations"][0]["draft"] = True
        report = lint.lint({"Scenes": []}, self.contracts, drafts=self.story)
        self.assertEqual(report["findings"][0]["status"], "dead_obligation")
        root = Path(__file__).resolve().parents[1]
        backlog = json.loads((root / "tools/engine_backlog.json").read_text())
        expected = next(i["finding_ids"] for i in backlog["items"] if i["id"] == "E-Q7-23")
        self.assertCountEqual(expected, [c["finding"] for c in json.loads(lint.DEFAULT.read_text())["obligations"]])


if __name__ == "__main__":
    unittest.main()
