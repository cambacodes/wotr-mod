"""eng7-l12: contract mutations and save-layout regression, no repo artifacts."""
import copy
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from tests.story_fixture import fresh_story
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
        cls.final = fresh_story()

    def test_saved_scene_node_relationship_and_choice_positions(self):
        self.assertEqual(list(self.before["Relationships"]), list(self.after["Relationships"]))
        self.assertEqual([s["Id"] for s in self.before["Scenes"]], [s["Id"] for s in self.after["Scenes"]])
        for old, new in zip(self.before["Scenes"], self.after["Scenes"]):
            self.assertEqual([n["Id"] for n in old["Nodes"]], [n["Id"] for n in new["Nodes"]])
            for a, b in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(without_prose(a["Choices"]), without_prose(b["Choices"]), old["Id"] + "/" + a["Id"])

    def test_world_claims_and_staging_are_clean(self):
        self.assertEqual(findings(world_facts, self.after), [])
        self.assertEqual(findings(location_staging, self.after), [])

    def test_commander_mourning_mutation_is_rejected(self):
        story = copy.deepcopy(self.final)
        page = next(s for s in story["Scenes"] if s["Id"] == "anevia.ending_sacrifice")
        p = next(n for n in page["Nodes"] if n["Id"] == "end")["Paragraphs"][7]
        p["Forbids"].remove(lane.DEAD)
        self.assertTrue(any(f["scene"] == page["Id"] for f in findings(commander_alive, story)))
        self.assertTrue(any("living continuation" in error for error in earned_presence_lint.check(story)[0]))

    def test_world_fact_guard_removal_is_rejected(self):
        story = copy.deepcopy(self.final)
        page = next(s for s in story["Scenes"] if s["Id"] == "chadali.trickster.epilogue.lucky_night")
        p = next(n for n in page["Nodes"] if n["Id"] == "page")["Paragraphs"][15]
        p["Requires"].remove("ending.wound_closed")
        self.assertTrue(any(f["scene"] == page["Id"] for f in findings(world_facts, story)))

    def test_all_bereavement_siblings_are_disjoint(self):
        contracts = json.loads((Path(__file__).resolve().parents[1] / "tools/commander_continuation_surfaces.json").read_text())
        scenes = {s["Id"]: s for s in self.final["Scenes"]}
        for scene_id, node_id, slot in contracts:
            node = next(n for n in scenes[scene_id]["Nodes"] if n["Id"] == node_id)
            paragraph = node["Paragraphs"][int(slot[10:-1])]
            self.assertIn(lane.DEAD, paragraph["Forbids"])
        count = len(contracts)
        self.assertGreater(count, 50)  # sweep includes both Tirabade routes

    def test_off_island_and_physical_contracts_include_manual_reads(self):
        scenes = {s["Id"]: s for s in self.after["Scenes"]}
        for contract in lane.inventory("location_inventory_contracts.json")["venues"]:
            self.assertEqual(scenes[contract["scene"]]["Areas"], contract["areas"])
        self.assertNotIn("c876d5303f4a19f4a80b0cc9b313db6f", scenes["melazmera.trickster.ch4.hunt_found"]["Areas"])

    def test_existing_finale_variants_are_preserved_without_contradictory_appendices(self):
        old = next(s for s in self.before["Scenes"] if s["Id"] == "melazmera.trickster.epilogue.left_free")
        new = next(s for s in self.after["Scenes"] if s["Id"] == old["Id"])
        self.assertEqual(without_prose(old["Nodes"][0]["Paragraphs"]), without_prose(new["Nodes"][0]["Paragraphs"]))
        for a, b in zip(self.before["Scenes"], self.after["Scenes"]):
            for original, changed in zip(a["Nodes"], b["Nodes"]):
                for paragraph in changed.get("Paragraphs", [])[len(original.get("Paragraphs", [])):]:
                    self.assertFalse(set(paragraph.get("Requires", [])) & set(paragraph.get("Forbids", [])), a["Id"])

    def test_lint_does_not_excuse_same_block_unrelated_staging(self):
        story = copy.deepcopy(self.final)
        scene = next(s for s in story["Scenes"] if s["Id"] == "galfrey.trickster.ch4.letter")
        scene["Nodes"][0]["Text"] += " {n}You stand in Drezen's citadel.{/n}"
        self.assertTrue(any(f["scene"] == scene["Id"] for f in findings(location_staging, story)))


if __name__ == "__main__":
    unittest.main()
