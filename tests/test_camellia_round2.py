"""Camellia situation continuity and legacy-save regression checks."""
import copy
import json
from pathlib import Path
import unittest

from storylines import (camellia_trickster as ct, camellia_masks, camellia_evenings,
                        camellia_cards, camellia_days, camellia_last, camellia_native,
                        camellia_intimate_aftermath)
from tools import savecompat


class CamelliaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = {"Scenes": copy.deepcopy(ct.SCENES + camellia_native.SCENES), "Derived": {}}
        cls.after = copy.deepcopy(cls.before)
        camellia_intimate_aftermath.integrate(cls.after)
        cls.scenes = {s["Id"]: s for s in cls.after["Scenes"]}

    def node(self, sid, nid):
        return next(n for n in self.scenes[ct.P + sid]["Nodes"] if n["Id"] == nid)

    def test_all_legacy_references_and_ending_exit_effects_survive(self):
        self.assertEqual([], savecompat.check(self.after, savecompat.inventory(self.before)))
        for old in self.before["Scenes"]:
            if old["Owner"].endswith("Epilogue"):
                new = self.scenes[old["Id"]]
                for original, current in zip(old["Nodes"], new["Nodes"]):
                    self.assertEqual(original["Choices"], current["Choices"])

    def test_slots_are_reachable_and_keep_each_branch_successor(self):
        root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/camellia"
        briefs = [json.loads(p.read_text(encoding="utf-8")) for p in root.glob("*.json")]
        self.assertEqual(21, len(briefs))
        for brief in briefs:
            with self.subTest(slot=brief["slot_id"]):
                host = self.scenes[brief["insertion"]["scene_id"]]
                pages = {n["Id"]: n for n in host["Nodes"]}
                slot = pages[brief["slot_id"]]
                self.assertEqual(brief["default_text"], slot["Text"])
                self.assertEqual([], slot["Choices"][0]["Set"])
                self.assertTrue(any(c.get("Next") == slot["Id"] for n in host["Nodes"] for c in n["Choices"]))
                self.assertIn(slot["Choices"][0]["Next"], pages)
                if "the_second_dance" in host["Id"]:
                    anchor = "strap" if "from strap" in brief["insertion"]["branch"] else "leave"
                    self.assertEqual(slot["Id"], pages[anchor]["Choices"][0]["Next"])
                if "the_deck_again" in host["Id"]:
                    self.assertIsNone(pages["wont_close"]["Choices"][0]["Next"])

    def test_first_coffin_delivery_does_not_need_placement_failure(self):
        for sid, terminal in (("killed.third_night", "home"), ("killed.late_curtain", "walk")):
            answers = self.node(sid, terminal)["Choices"]
            self.assertTrue(any(c.get("Next") == "eng8.reunion" and ct.PRESENCE_FAILED not in c["Requires"]
                                for c in answers))
            for answer in self.node(sid, "eng8.price")["Choices"][:2]:
                self.assertEqual("r2.stones", answer["Next"])
                self.assertIn(ct.TERMS, answer["Set"])
            self.assertIn(ct.FILLED, self.node(sid, "r2.stones")["Choices"][0]["Set"])

    def test_existing_charges_precede_irreversible_consequences(self):
        self.assertEqual(-100, self.node("killed.third_night", "start")["Choices"][0]["Crusade"]["Amount"])
        for suffix in ("", "_camp", "_alive"):
            host = self.scenes[ct.P + "day.a_new_friend" + suffix]
            for page in host["Nodes"]:
                for answer in page["Choices"]:
                    if answer.get("Next") == "warn":
                        self.assertEqual({"Resource": "Favors", "Amount": -100}, answer["Crusade"])
            self.assertNotIn("Crusade", self.node("day.a_new_friend" + suffix, "warn")["Choices"][0])

    def test_prices_and_confessions_are_collected_not_inferred_from_a_kiss(self):
        self.assertIn("Blood strikes silver", self.node("beat.spirits_due", "unmissed")["Text"])
        for suffix in ("", "_camp", "_alive"):
            self.assertEqual([ct.P + "mireya_disclosed"], self.node("cards.the_amulet" + suffix, "tell")["EnterSet"])
            self.assertIn(ct.P + "encounter.all.public_paid",
                          self.node("evening.breakfast" + suffix, "r2.public_paid")["Choices"][0]["Set"])
            self.assertIn(ct.P + "bond.witness_public",
                          self.node("bond.witness" + suffix, "r2.public_after")["Choices"][0]["Set"])
            self.assertIn(ct.WITNESS_HERS, self.node("bond.witness" + suffix, "hers")["Choices"][0]["Set"])
        paragraphs = self.node("epilogue.commit", "page")["Paragraphs"]
        self.assertTrue(any(ct.BLED in p["Requires"] and "took the promised blood" in p["Text"] for p in paragraphs))
        self.assertTrue(any(ct.MARKED in p["Requires"] and "withdrew" in p["Text"] for p in paragraphs))

    def test_geography_current_path_and_refusal(self):
        for sid in ("cards.a_bowl_for_mireya", "beat.spirits_due"):
            self.assertEqual([3, 5], self.scenes[ct.P + sid]["Chapters"])
        for sid in ("epilogue.kept", "epilogue.kept_on_record", "epilogue.commit", "epilogue.commit_on_record"):
            self.assertIn("trickster.now", self.scenes[ct.P + sid]["Requires"])
        self.assertNotIn(ct.RET, self.scenes[ct.P + "epilogue.refused"]["Requires"])
        self.assertIn("sacrifice", self.scenes[ct.P + "epilogue.refused"]["Forbids"])

    def test_either_resurrection_debt_reads_without_requiring_both(self):
        for sid in ("epilogue.kept", "epilogue.kept_on_record", "epilogue.commit", "epilogue.commit_on_record"):
            paragraphs = self.node(sid, "page")["Paragraphs"]
            self.assertTrue(any(p.get("AnyGroups") == [[ct.OWED, ct.BARGAIN_COST]] for p in paragraphs))

    def test_one_current_victim_suffices_for_oath_without_summoning_departed_women(self):
        key = ct.P + "kills_answered.present_victim"
        groups = self.after["Derived"][key]
        self.assertEqual(3, len(groups))
        for group in groups:
            self.assertTrue(any(all(flag in set(group) for flag in candidate) for candidate in groups))
            self.assertFalse(any(all(flag in {group[1]} for flag in candidate) for candidate in groups))
        for suffix in ("", "_camp"):
            self.assertIn(key, self.scenes[ct.P + "kills_answered.oath" + suffix]["Requires"])
            self.assertFalse(self.scenes[ct.P + "kills_answered.oath" + suffix].get("RequiresAnyGroups"))


if __name__ == "__main__":
    unittest.main()
