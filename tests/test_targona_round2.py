"""Targona's earned branches, slot continuations and unavailable endings."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools.crossroute_checks.common import Proof, fields, lit, verify


class TargonaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.proof = Proof(verify.Model(cls.story))

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]["Nodes"] if n["Id"] == node)

    def test_all_continuing_endings_reject_incompatible_departure(self):
        for suffix in ("commit", "colleague", "colleague_lost", "ally", "declined",
                       "refused_promise", "furlough", "sacrifice"):
            scene = self.scenes["targona.trickster.epilogue." + suffix]
            gate = fields(scene, overrides=True)
            for loss in ("swarm", "demon", "lich", "devil", "targona.condemned",
                         "targona.dead_lair", "targona.returned_actor_lost"):
                with self.subTest(ending=suffix, loss=loss):
                    self.assertTrue(self.proof.implies(gate, lit(loss, False)))

    def test_refused_promise_remains_a_closed_farewell(self):
        scene = self.scenes["targona.trickster.epilogue.refused_promise"]
        self.assertIn("targona.closed", scene["Requires"])
        self.assertNotIn("targona.outcome.route_open", scene["Requires"])
        self.assertEqual("targona.trickster.returned",
                         scene["ForbidOverrides"]["targona.dead_lab"])

    def test_slots_do_not_create_acceptance_or_night_receipts(self):
        for scene_id, target in (("targona.trickster.after.ward", "morning"),
                                 ("targona.trickster.after.quiet_ward", "morning"),
                                 ("targona.ward_evening", "bell")):
            node = self.node(scene_id, scene_id + ".explicit.1")
            self.assertEqual(1, len(node["Choices"]))
            answer = node["Choices"][0]
            self.assertEqual(target, answer["Next"])
            self.assertEqual([], answer["Set"])
            self.assertEqual([], answer["Requires"])
            self.assertEqual([], answer["Forbids"])
            self.assertFalse(answer["Abort"])
        for scene_id in ("targona.trickster.after.ward", "targona.trickster.after.quiet_ward"):
            self.assertEqual(["targona.trickster.night_kept"],
                             self.node(scene_id, "morning")["Choices"][0]["Set"])

    def test_first_nights_are_alternatives_and_costs_stay_distinct(self):
        ward = self.scenes["targona.trickster.after.ward"]
        quiet = self.scenes["targona.trickster.after.quiet_ward"]
        self.assertIn("targona.trickster.declined", ward["Forbids"])
        self.assertIn("targona.trickster.declined", quiet["Requires"])
        for scene in (ward, quiet):
            self.assertIn("targona.committed", scene["Forbids"])
        self.assertEqual(["targona.committed"], self.node(ward["Id"], "dawn")["Choices"][2]["Set"])
        self.assertEqual(["targona.committed", "targona.trickster.cost.light_sealed"],
                         self.node(quiet["Id"], "start")["Choices"][0]["Set"])
        self.assertEqual(["targona.closed"], self.node(quiet["Id"], "start")["Choices"][1]["Set"])
        spent = self.node("targona.trickster.free.spent_light", "start")["Choices"]
        self.assertEqual(("Favors", -300), (spent[0]["Crusade"]["Resource"], spent[0]["Crusade"]["Amount"]))
        self.assertEqual(("Finances", -500), (spent[1]["Crusade"]["Resource"], spent[1]["Crusade"]["Amount"]))
        self.assertTrue(spent[2]["Abort"])
        self.assertEqual([], spent[2]["Set"])

    def test_text_paragraph_slots_preserve_legacy_exit_mechanics(self):
        from storylines import targona_opening, targona_trickster
        for module, sid, nid in ((targona_opening, "targona.the_open_threshold", "buckles"),
                                  (targona_trickster, "targona.trickster.epilogue.commit", "end")):
            node = self.node(sid, nid)
            self.assertIn(module.EXPLICIT_PARAGRAPHS[sid + ".explicit.1"], node["Text"])
            self.assertEqual(1, len(node["Choices"]))
            self.assertIsNone(node["Choices"][0]["Next"])
            self.assertEqual([], node["Choices"][0]["Set"])
            self.assertFalse(node["Choices"][0]["Abort"])
            self.assertEqual([], node["Choices"][0]["Requires"])

    def test_five_briefs_match_the_production_addresses(self):
        root = Path(__file__).resolve().parents[1] / "tools/route_packs"
        addresses = json.loads((root / "plans/targona-slot-addresses.json").read_text(encoding="utf-8"))
        briefs = [json.loads(p.read_text(encoding="utf-8"))
                  for p in (root / "explicit_slots/targona").glob("*.json")]
        self.assertEqual(set(addresses), {b["slot_id"] for b in briefs})
        self.assertEqual(5, len(briefs))
        for brief in briefs:
            address = addresses[brief["slot_id"]]
            node = self.node(address["scene"], address["node"])
            anchor = brief["last_line"].removeprefix("N: ")
            self.assertIn(anchor, node["Text"])

    @unittest.expectedFailure
    def test_shared_classifier_does_not_gate_history_on_other_romances(self):
        """Pending shared-owner repair: P1 8-15 / F1 7-14, not prose evasions."""
        cases = (("targona.unasked_question", "start", 0, "areelu.closed"),
                 ("targona.the_folded_room", "study", 0, "crossroute.irabeth.unavailable"),
                 ("targona.trickster.free.spent_light", "start", 1, "iomedae.closed"),
                 ("targona.trickster.after.ward", "dawn", 1, "iomedae.closed"),
                 ("targona.trickster.free.the_names", "start", 1, "iomedae.closed"),
                 ("targona.trickster.free.the_names", "start", 2, "iomedae.closed"))
        violations = [(sid, nid, i, flag) for sid, nid, i, flag in cases
                      if flag in self.node(sid, nid)["Choices"][i]["Forbids"]]
        violations.extend(("targona.an_unpromised_future", flag)
                          for flag in ("crossroute.areelu.unavailable", "crossroute.irabeth.unavailable")
                          if flag in self.scenes["targona.an_unpromised_future"]["Forbids"])
        self.assertEqual([], violations)


if __name__ == "__main__":
    unittest.main()
