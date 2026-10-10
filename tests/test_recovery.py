"""Recovery regressions: old saves, paid clocks and political-only decisions."""
import json
from pathlib import Path
import unittest

from tools import savecompat
from tools.player_text_lint import check as check_player_text


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((Path(__file__).resolve().parents[1] /
                                "development/Story.json").read_text(encoding="utf-8-sig"))
        cls.scenes = {scene["Id"]: scene for scene in cls.story["Scenes"]}

    def test_merged_informed_nodes_keep_old_saved_answers_and_unique_ids(self):
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") == "camellia":
                ids = [node["Id"] for node in scene["Nodes"]]
                self.assertEqual(len(ids), len(set(ids)), scene["Id"])
        scene = self.scenes["camellia.trickster.masks.mireya"]
        nodes = {node["Id"]: node for node in scene["Nodes"]}
        self.assertEqual([choice["Next"] for choice in nodes["who_known"]["Choices"]],
                         ["name", "needs", "needs_known", "name_known"])
        self.assertEqual([], savecompat.check(self.story))

    def test_all_timed_coffins_read_the_existing_native_death_timestamp(self):
        receipt = "camellia.trickster.native_death_observed"
        self.assertEqual(["camellia.dead"], self.story["Latches"][receipt])
        for suffix in ("third_night", "late_curtain_prepared"):
            scene = self.scenes["camellia.trickster.killed." + suffix]
            self.assertEqual(72, scene["DelayHours"])
            self.assertIn(receipt, scene["Requires"])
            self.assertIn("camellia.trickster.killed_corpse_observed", scene["Requires"])
        self.assertIn(["camellia.trickster.amulet_kept"],
                      self.story["Derived"]["camellia.trickster.mireya_known"])

    def test_envoy_decision_withholds_romantic_readers_and_keeps_paid_call(self):
        envoy = "konomi.trickster.envoy"
        self.assertIn(envoy, self.story["DerivedForbids"]["konomi.harem.eligible"])
        self.assertIn(envoy, self.scenes["konomi.lastcall.page"]["Forbids"])
        call = self.scenes["konomi.lastcall.call"]
        self.assertNotIn(envoy, call["Forbids"])
        self.assertNotIn(envoy, self.story["Relationships"]["konomi"]["UnavailableFlags"])

    def test_herrax_recollects_only_an_observed_palace_dismissal(self):
        scene = self.scenes["herrax.house.the_glowworm"]
        nodes = {node["Id"]: node for node in scene["Nodes"]}
        receipt = "herrax.trickster.palace_dismissed"
        self.assertEqual(["30469883ce1583743a6b4228d24778bc"],
                         self.story["SeenCues"][receipt])
        self.assertEqual("end", next(c for c in nodes["joke"]["Choices"] if "trickster.ever" in c["Forbids"])["Next"])
        for seen in (False, True):
            flags = {"trickster", "trickster.ever"}
            if seen:
                flags.add(receipt)
            shown = [answer for answer in nodes["joke"]["Choices"]
                     if set(answer["Requires"]) <= flags
                     and not flags.intersection(answer["Forbids"])]
            destination = only(shown)["Next"]
            self.assertEqual(destination, "joke_after_audience" if seen else "joke_before_audience")
            self.assertEqual("end", only(nodes[destination]["Choices"])["Next"])

    def test_wenduag_wound_polish_keeps_the_original_check_and_no_new_fee(self):
        scene = self.scenes["wenduag.trickster.killed.stage"]
        choice = next(c for node in scene["Nodes"] if node["Id"] == "start" for c in node["Choices"] if c.get("Check", {}).get("Skill") == "SkillMobility")
        self.assertEqual({"Skill": "SkillMobility", "DC": 24,
                          "Success": "clean", "Failure": "deep"}, choice["Check"])
        self.assertIsNone(choice.get("Crusade"))
        self.assertNotIn("wenduag.trickster.cost.wound_charm", choice["Set"])

    def test_explicit_male_visitors_do_not_exempt_commander_gender_claims(self):
        report = check_player_text(self.story)
        for row in report["review"]:
            self.assertFalse(row["code"] == "commander-gender" and row["scene"] in {
                "areelu.trickster.report.commission", "areelu.trickster.report.rival"}, row)
        self.assertNotIn("wenduag", {row["route"] for row in report["therapy_warnings"]})
        # Exact diagnostic exceptions must never silence an actual Commander pronoun.
        probe = {"Scenes": [{"Id": "areelu.trickster.report.commission", "Nodes": [
            {"Id": "start", "Text": "The Commander takes his sword.", "Choices": []}]}]}
        self.assertTrue(any(row["code"] == "commander-gender"
                            for row in check_player_text(probe)["review"]))


if __name__ == "__main__":
    unittest.main()
