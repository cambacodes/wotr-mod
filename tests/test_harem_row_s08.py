"""S08 review safety: blocked contracts must never enter a playable export."""
import copy
import unittest

from storylines.harem_rows import register_all, s08
from storylines import household


class HaremRowS08(unittest.TestCase):
    def test_unresolved_contract_is_inert_even_with_all_success_history(self):
        payload = {"Scenes": [], "Derived": {"existing": [["history"]]},
                   "Relationships": {"household": {"ClosedFlag": "household.closed"}}}
        before = copy.deepcopy(payload)
        s08.register(payload, payload["Scenes"], dict.fromkeys(s08.COMMON_REQUIRES, True))
        self.assertEqual(payload, before)
        self.assertEqual(len(s08.BLOCKERS), 4)

    def test_discovery_has_no_draft_side_effects(self):
        payload = {"Scenes": []}
        register_all(payload, payload["Scenes"], {})
        self.assertEqual(payload, {"Scenes": []})

    def test_review_does_not_register_consumers_or_entries(self):
        consumers = dict(household.CONSUMERS)
        entries = copy.deepcopy(household.ENTRIES)
        s08.draft_scenes()
        self.assertEqual(household.CONSUMERS, consumers)
        self.assertEqual(household.ENTRIES, entries)

    def test_chapter_body_channel_and_later_loss_guards_on_every_wrapper(self):
        for scene in s08.draft_scenes():
            with self.subTest(scene=scene["Id"]):
                self.assertEqual(scene["Chapters"], [5])
                self.assertEqual(scene["Participants"], ["arueshalae"])
                self.assertEqual(scene["RestAllowance"], "household.protected")
                self.assertIn("arueshalae.present_now", scene["Requires"])
                self.assertIn("nocticula.reachable_by_letter", scene["Requires"])
                self.assertIn("noct.acq.seal_received", scene["Requires"])
                self.assertIn("noct.acq.renewed_agreement", scene["Requires"])
                for loss in ("noct.acq.council_fight", "noct.closed", "noct.acq.closed",
                             "arueshalae.closed", "arueshalae.epoch_unavailable",
                             "nocticula.epoch_unavailable"):
                    self.assertIn(loss, scene["Forbids"])
                    self.assertNotIn(loss, scene["ForbidOverrides"])
                for a, b in (("arueshalae", "nocticula"), ("nocticula", "arueshalae")):
                    self.assertEqual(scene["ForbidOverrides"][household.enmity(a, b)],
                                     a + ".harem.reconciled." + b)

    def test_unknown_personality_offers_neither_and_corruption_has_precedence(self):
        for scene in s08.draft_scenes():
            if scene["Id"].endswith("redeemed"):
                self.assertIn("arueshalae.redeemed", scene["Requires"])
                self.assertIn("arueshalae.corrupted", scene["Forbids"])
            else:
                self.assertIn("arueshalae.corrupted", scene["Requires"])

    def test_retry_uses_failure_clock_and_wrappers_share_exhaustion(self):
        for scene in s08.draft_scenes():
            retry = ".retry." in scene["Id"]
            step = "retry" if retry else "settle"
            self.assertEqual(scene["DelayHours"], 48 if retry else 0)
            self.assertEqual(scene["HouseholdWitness"], s08.P(step + ".seen"))
            self.assertIn(s08.P(step + ".seen"), scene["Forbids"])
            self.assertIn(s08.P("resolved"), scene["Forbids"])
            self.assertIn(s08.P("permanent_refusal"), scene["Forbids"])
            if retry:
                self.assertIn(s08.P("settle.failed"), scene["Requires"])

    def test_reserved_answers_abort_and_destination_safety(self):
        for scene in s08.draft_scenes():
            nodes = {node["Id"]: node for node in scene["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertEqual(len(root), 3 if ".retry." in scene["Id"] else 4)
            self.assertTrue(root[-1]["Abort"])
            self.assertFalse(root[-1]["Set"])
            self.assertIsNone(root[-1]["Next"])
            for node in nodes.values():
                for choice in node["Choices"]:
                    if choice["Next"]:
                        self.assertIn(choice["Next"], nodes)
                    if choice.get("Check"):
                        self.assertIsNone(choice["Check"]["DC"])
                        self.assertIn(choice["Check"]["Success"], nodes)
                        self.assertIn(choice["Check"]["Failure"], nodes)
                    for flag in choice["Set"]:
                        self.assertTrue(flag.startswith(s08.PREFIX), flag)
                        self.assertFalse(any(token in flag for token in
                                             (".harem.attitude.", ".enmity.", ".stance.",
                                              ".closed", ".committed", ".returned", ".changed")))
                    if node["Id"] != "start":
                        self.assertFalse(choice["Abort"])

    def test_scene_drafts_have_no_conditional_paragraphs_or_intimate_slots(self):
        for scene in s08.draft_scenes():
            for node in scene["Nodes"]:
                self.assertNotIn("Paragraphs", node)
                self.assertNotIn("explicit", node["Id"])


if __name__ == "__main__":
    unittest.main()
