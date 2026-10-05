"""E-Q8-07: coverage and mutation checks for shipped delivery contracts."""
import copy
import json
from pathlib import Path
import unittest

from tools import remote_allocation_lint as allocation
from tools import timeline_contract_lint as timeline


class DeliveryInventory2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from expansion import make_expansion
        cls.story = make_expansion()
        cls.contracts = json.loads(allocation.DELIVERY_INVENTORY.read_text(encoding="utf-8"))

    def test_every_mapped_finding_has_a_positive_delivered_history(self):
        findings = self.contracts["findings"]
        expected = {"camellia": [72, 73], "galfrey": list(range(13, 24)) + [89, 90],
                    "horzalah": [21, 22, 23, 24, 31], "nenio": [23],
                    "terendelev": [88, 89], "wenduag": [42, 43, 44, 65]}
        self.assertCountEqual([f"{route}:{index:03}" for route, indices in expected.items() for index in indices],
                              [row["finding"] for row in findings])
        self.assertEqual(allocation.delivery_inventory(self.story), [])
        self.assertEqual({h["character"].lower() for h in self.contracts["histories"]}, set(expected))
        for h in self.contracts["histories"]:
            self.assertFalse(h["expectedFailure"], h["name"])
            self.assertTrue(h["steps"], h["name"])
            for step in h["steps"]:
                self.assertFalse(set(step) & {"flags", "checkpoint", "pre_age"}, h["name"])

    def test_physical_remote_manual_and_contact_mutations_fail(self):
        for row in self.contracts["sites"]:
            if not row.get("physical"):
                continue
            for mutation in ("Remote", "ManualOnly", "ContactUnit"):
                story = copy.deepcopy(self.story)
                scene = next(s for s in story["Scenes"] if s["Id"] == row["scene"])
                scene[mutation] = None if mutation == "ContactUnit" else True
                self.assertTrue(allocation.delivery_inventory(story), (row["scene"], mutation))

    def test_unallocated_reactor_and_production_expected_failure_rejected(self):
        for sid in self.contracts["retired_reactors"]:
            story = copy.deepcopy(self.story)
            scene = next(s for s in story["Scenes"] if s["Id"] == sid)
            scene["Forbids"].remove("trickster.ever")
            self.assertTrue(allocation.delivery_inventory(story), sid)
        contracts = copy.deepcopy(self.contracts)
        contracts["histories"][0]["expectedFailure"] = True
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))
        contracts["histories"][0]["expectedFailure"] = False
        contracts["histories"][0]["steps"][0]["pre_age"] = 200
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))

    def test_folded_coffin_provenance_is_scoped_and_requires_paid_ritual(self):
        from tools import return_provenance_lint as provenance
        self.assertEqual(provenance.check(self.story), [])
        for sid in provenance.contracts()['eng8-q8d']['coffin_completion_nodes']:
            story = copy.deepcopy(self.story)
            scene = next(s for s in story['Scenes'] if s['Id'] == sid)
            scene['Requires'].remove('camellia.killed')
            self.assertTrue(provenance.check(story), sid)
            story = copy.deepcopy(self.story)
            scene = next(s for s in story['Scenes'] if s['Id'] == sid)
            scene['Nodes'][0]['Choices'][0]['Set'].append(provenance.contracts()['completed'])
            self.assertTrue(provenance.check(story), sid)

    def test_all_eight_character_limits_are_binding(self):
        contracts = json.loads(allocation.DEFAULT.read_text(encoding="utf-8"))
        for character in ("Camellia", "Galfrey", "Horzalah", "Nenio", "Terendelev", "Wenduag"):
            changed = copy.deepcopy(contracts)
            row = next(a for a in changed["allocations"] if a["character"] == character)
            row["limits"]["5"] += 1
            self.assertTrue(allocation.lint({"Scenes": []}, changed, [])["hard"], character)

    def test_cumulative_clock_rejects_missing_origin_reordering_and_overrun(self):
        history = dict(origin="coronation", maximum_hours=168,
                       steps=[dict(hour=0, set=["coronation"]), dict(hour=168, set=["yes"])])
        self.assertIsNone(timeline.delivered_timeline(history))
        history["steps"][-1]["hour"] = 174
        self.assertIn("exceeds", timeline.delivered_timeline(history))
        history["steps"][0]["set"] = []
        self.assertIn("missing", timeline.delivered_timeline(history))
        history["steps"][-1]["hour"] = -1
        self.assertIn("nonchronological", timeline.delivered_timeline(history))

    def test_entrance_fold_preserves_saved_choices_and_earned_gift(self):
        scenes = {s["Id"]: s for s in self.story["Scenes"]}
        for suffix, terminal in (("unmet.knife", "exit"), ("late.at_night", "no_priest")):
            scene = scenes["horzalah.trickster." + suffix]
            end = next(n for n in scene["Nodes"] if n["Id"] == terminal)
            self.assertIn("chapter.six", end["Choices"][0]["Forbids"])
            self.assertIn("chapter.six", end["Choices"][-1]["Requires"])
            self.assertTrue(end["Choices"][-1]["Next"].startswith("eng8.guild."))
            self.assertTrue(any("horzalah.trickster.tested" in c["Set"]
                                for n in scene["Nodes"] if n["Id"].startswith("eng8.guild.") for c in n["Choices"]))
        self.assertEqual(scenes["horzalah.trickster.visit.chamber"]["MaxChapter"], 5)
        self.assertEqual(scenes["terendelev.trickster.wound.weeps"]["Chapters"], [3])
        self.assertNotIn("The Abyss has no night", scenes["terendelev.trickster.wound.weeps"]["Nodes"][0]["Text"])
        for node in scenes["terendelev.trickster.wound.weeps"]["Nodes"]:
            self.assertNotIn("priests in the Abyss", node["Text"])
            self.assertNotIn("red half-dark", node["Text"])
            self.assertNotIn("Nocticula's audience hall", node["Text"])


if __name__ == "__main__":
    unittest.main()
