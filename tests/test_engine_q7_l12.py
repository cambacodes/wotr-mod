"""eng7-l12: contract mutations and save-layout regression, no repo artifacts."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from expansion import make_expansion
from storylines import engine_q7_l12 as lane
from tools.crossroute_checks import commander_alive, location_staging, world_facts
from tools.crossroute_checks.common import Proof, blocks, verify
from tools import earned_presence_lint


def findings(check, story):
    model = verify.Model(story)
    return check.check(model, list(blocks(model)), Proof(model))


class Lane12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch.object(lane, "integrate"):
            cls.before = make_expansion()
        cls.after = copy.deepcopy(cls.before)
        lane.integrate(cls.after)

    def test_saved_scene_node_relationship_and_choice_positions(self):
        self.assertEqual(list(self.before["Relationships"]), list(self.after["Relationships"]))
        self.assertEqual([s["Id"] for s in self.before["Scenes"]], [s["Id"] for s in self.after["Scenes"]])
        for old, new in zip(self.before["Scenes"], self.after["Scenes"]):
            self.assertEqual([n["Id"] for n in old["Nodes"]], [n["Id"] for n in new["Nodes"]])
            for a, b in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(a["Choices"], b["Choices"], old["Id"] + "/" + a["Id"])

    def test_world_claims_and_staging_are_clean(self):
        self.assertEqual(findings(world_facts, self.after), [])
        self.assertEqual(findings(location_staging, self.after), [])

    def test_commander_mourning_mutation_is_rejected(self):
        story = copy.deepcopy(self.after)
        page = next(s for s in story["Scenes"] if s["Id"] == "anevia.ending_sacrifice")
        p = next(p for n in page["Nodes"] for p in n["Paragraphs"] if lane.narration_free(p["Text"]).startswith("The spring after Threshold, somebody knocked"))
        p["Forbids"].remove(lane.DEAD)
        self.assertTrue(any(f["scene"] == page["Id"] for f in findings(commander_alive, story)))
        self.assertTrue(any("living continuation" in error for error in earned_presence_lint.check(story)[0]))

    def test_world_fact_guard_removal_is_rejected(self):
        story = copy.deepcopy(self.after)
        page = next(s for s in story["Scenes"] if s["Id"] == "chadali.trickster.epilogue.lucky_night")
        p = next(p for n in page["Nodes"] for p in n["Paragraphs"] if "night the Wound closed" in p["Text"])
        p["Requires"].remove("ending.wound_closed")
        self.assertTrue(any(f["scene"] == page["Id"] for f in findings(world_facts, story)))

    def test_all_bereavement_siblings_are_disjoint(self):
        contracts = lane.inventory("commander_block_contracts.json")["continuations"]
        count = 0
        for scene in self.after["Scenes"]:
            if not scene.get("Owner", "").endswith("Epilogue"):
                continue
            for node in scene["Nodes"]:
                for p in node.get("Paragraphs") or []:
                    if any(lane.narration_free(p["Text"]).startswith(c["prefix"]) for c in contracts):
                        self.assertIn(lane.DEAD, p["Forbids"])
                        count += 1
        self.assertGreater(count, 50)  # sweep includes both Tirabade routes

    def test_off_island_and_physical_contracts_include_manual_reads(self):
        scenes = {s["Id"]: s for s in self.after["Scenes"]}
        for contract in lane.inventory("location_inventory_contracts.json")["venues"]:
            self.assertEqual(scenes[contract["scene"]]["Areas"], contract["areas"])
        self.assertNotIn("c876d5303f4a19f4a80b0cc9b313db6f", scenes["melazmera.trickster.ch4.hunt_found"]["Areas"])

    def test_existing_finale_variants_are_preserved_without_contradictory_appendices(self):
        old = next(s for s in self.before["Scenes"] if s["Id"] == "melazmera.trickster.epilogue.left_free")
        new = next(s for s in self.after["Scenes"] if s["Id"] == old["Id"])
        self.assertEqual(old["Nodes"][0]["Paragraphs"], new["Nodes"][0]["Paragraphs"])
        for a, b in zip(self.before["Scenes"], self.after["Scenes"]):
            for original, changed in zip(a["Nodes"], b["Nodes"]):
                for paragraph in changed.get("Paragraphs", [])[len(original.get("Paragraphs", [])):]:
                    self.assertFalse(set(paragraph.get("Requires", [])) & set(paragraph.get("Forbids", [])), a["Id"])

    def test_lint_does_not_excuse_same_block_unrelated_staging(self):
        story = copy.deepcopy(self.after)
        scene = next(s for s in story["Scenes"] if s["Id"] == "galfrey.trickster.ch4.letter")
        scene["Nodes"][0]["Text"] += " {n}You stand in Drezen's citadel.{/n}"
        self.assertTrue(any(f["scene"] == scene["Id"] for f in findings(location_staging, story)))


if __name__ == "__main__":
    unittest.main()
