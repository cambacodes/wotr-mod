"""E-Q7-17: count actual histories by woman, including auxiliary owners."""
import copy
import json
from pathlib import Path
import unittest

from tools import remote_allocation_lint as lint


class RemoteAllocationTests(unittest.TestCase):
    def setUp(self):
        self.contracts = json.loads(lint.DEFAULT.read_text(encoding="utf-8"))
        self.allocations = {a["character"]: a for a in self.contracts["allocations"]}

    def scene(self, sid, who="Wenduag", chapter=5, relationship=None, remote=True, owner=None):
        return dict(Id=sid, Owner=owner or who, Relationship=relationship or who.lower(),
                    MinChapter=chapter, MaxChapter=chapter, Chapters=[chapter], Remote=remote)

    def count(self, scenes, deliveries, who="Wenduag", chapter=5):
        return lint.count_history({"Scenes": scenes}, self.allocations[who], chapter, deliveries)

    def test_chapter_three_third_page_and_zero_allocation(self):
        for chapter, count in [(3, 3), (4, 1), (5, 2), (6, 1)]:
            scenes = [self.scene("page" + str(i), chapter=chapter) for i in range(count)]
            result = self.count(scenes, [s["Id"] for s in scenes], chapter=chapter)
            self.assertTrue(result["failure"], result)
            self.assertIn("§4.2", result["ledger_row"])
            self.assertIn("R2-5", result["ledger_row"])

    def test_alias_and_refusal_after_closure_do_not_hide_third_page(self):
        scenes = [self.scene("first", who="Shamira"), self.scene("dream", who="Shamira"),
                  self.scene("inquiry", who="Shamira", relationship="shamira_barracks", owner="Surgeon")]
        result = self.count(scenes, ["first", "dream", "inquiry"], who="Shamira")
        self.assertEqual(result["count"], 3)
        self.assertTrue(result["failure"])
        mutated = copy.deepcopy(scenes)
        mutated[-1]["Relationship"] = "unrelated"
        mutated[-1]["Owner"] = "Shamira"
        self.assertTrue(self.count(mutated, ["first", "dream", "inquiry"], who="Shamira")["failure"])

    def test_alternative_twins_count_per_run(self):
        scenes = [self.scene("letter"), self.scene("letter-fallback")]
        for ids in [["letter"], ["letter-fallback"]]:
            self.assertFalse(self.count(scenes, ids)["failure"])
        self.assertTrue(self.count(scenes, ["letter", "letter-fallback"])["failure"])

    def test_physical_folded_and_framework_pages(self):
        scenes = [self.scene("return"), self.scene("folded", remote=False),
                  self.scene("memory", who="Memory", relationship="memory", chapter=4),
                  self.scene("table", who="Table", relationship="household", chapter=5)]
        result = self.count(scenes, ["return", "folded", "table"])
        self.assertFalse(result["failure"])
        self.assertEqual(result["pages"], ["return"])
        self.assertFalse(self.count(scenes, ["memory"], chapter=4)["failure"])
        # A woman's page called Memory still belongs to her allocation.
        scenes[-2]["Relationship"] = "wenduag"
        self.assertTrue(self.count(scenes, ["memory"], chapter=4)["failure"])

    def test_mutations_fail_executed_acceptance_trace(self):
        story = {"Scenes": [self.scene("return"), self.scene("trial", remote=False)]}
        trace = [dict(name="street-courtship", character="Wenduag", chapter=5,
                      deliveries=["return", "trial"])]
        self.assertEqual(lint.lint(story, self.contracts, trace)["hard"], [])
        story["Scenes"][1]["Remote"] = True
        self.assertTrue(lint.lint(story, self.contracts, trace)["hard"])
        story["Scenes"][1]["Remote"] = False
        trace[0]["deliveries"].append("missing")
        self.assertTrue(lint.lint(story, self.contracts, trace)["hard"])
        self.assertTrue(self.count(story["Scenes"], ["return", "return"])["failure"])

    def test_mapped_findings_and_every_audited_road_registered(self):
        root = Path(__file__).resolve().parents[1]
        backlog = json.loads((root / "tools/engine_backlog.json").read_text(encoding="utf-8"))
        expected = next(i["finding_ids"] for i in backlog["items"] if i["id"] == "E-Q7-17")
        self.assertCountEqual(expected, [c["finding"] for c in self.contracts["findings"]])
        sequences = self.contracts["audit_sequences"]
        self.assertEqual(sum(h["character"] == "Shamira" for h in sequences), 16)
        self.assertEqual(sum(h["character"] == "Wenduag" for h in sequences), 9)
        self.assertTrue(any(h["name"] == "departure" for h in sequences))

    def test_cannot_raise_limits_or_rename_auxiliary_relationship_to_pass(self):
        mutated = copy.deepcopy(self.contracts)
        mutated["allocations"][2]["limits"]["5"] = 20
        self.assertTrue(lint.lint({"Scenes": []}, mutated, [])["hard"])

    def test_current_mapped_visits_use_physical_delivery_and_stable_hubs(self):
        from expansion import make_expansion
        story = make_expansion()
        scenes = {s["Id"]: s for s in story["Scenes"]}
        for suffix in ["trial", "gate", "stinger", "cairn", "morning", "vellexia", "yaniel", "neathers", "hunt", "gongs"]:
            sid = "wenduag.trickster.court." + suffix
            self.assertFalse(lint.remote(scenes[sid]), sid)
            self.assertEqual(scenes[sid]["InteractionHub"], "wenduag.presence")
            self.assertFalse(lint.remote(scenes[sid + ".native_visit"]), sid)
            self.assertEqual(len(scenes[sid + ".native_visit"]["AnswerLists"]), 3)
        self.assertFalse(lint.remote(scenes["wenduag.trickster.killed.cellar"]))
        report = lint.lint(story)
        # Remaining failures are retained, never silently given a new allocation.
        self.assertEqual({h["history"] for h in report["review"]},
                         {"abyss", "stone", "champion", "late-bid", "street-courtship", "departure"})


if __name__ == "__main__":
    unittest.main()
