"""S12 reservation safety; these checks do not certify an emitted encounter."""
import copy
import unittest

from storylines.harem_rows import s12


class S12ContractTests(unittest.TestCase):
    def test_registration_is_inert_until_sheet_blockers_are_resolved(self):
        payload = {"Scenes": [{"Id": "existing"}], "Derived": {"existing": [["flag"]]}}
        scenes = payload["Scenes"]
        refs = {"native": "a" * 32}
        original = copy.deepcopy((payload, refs))
        self.assertIsNone(s12.register(payload, scenes, refs))
        self.assertEqual((payload, refs), original)
        self.assertIs(payload["Scenes"], scenes)
        self.assertEqual(len(s12.BLOCKERS), 3)

    def test_ordered_reservations_and_only_one_delayed_retry(self):
        settle, retry = s12.STEPS
        self.assertEqual([s["id"] for s in s12.STEPS],
                         [s12.P("settle"), s12.P("retry")])
        self.assertEqual(settle["start"], ("lesson", "spoiled", "refused", "later"))
        self.assertEqual(retry["start"], ("lesson", "refused", "later"))
        self.assertEqual((settle["delay"], retry["delay"]), (0, 48))
        self.assertEqual(retry["requires"], (s12.P("settle.failed"),))
        for step in s12.STEPS:
            self.assertEqual(step["chapters"], (5,))
            self.assertEqual(step["allowance"], "household.protected")
            self.assertEqual(step["category"], "protected")
            self.assertIn(step["witness"], step["forbids"])
            self.assertNotIn("later", step["terminals"])

    def test_success_requires_both_deeds_and_preserves_asymmetric_ceiling(self):
        respect = s12.LADDER["nenio.harem.attitude.camellia.respect"][0]
        for step in s12.STEPS:
            self.assertTrue(set(respect) <= set(step["terminals"]["lesson"]))
        self.assertEqual([key for key in s12.LADDER if key.startswith("camellia.")],
                         ["camellia.harem.attitude.nenio.rival"])
        self.assertFalse(any(key.endswith((".friend", ".lover")) for key in s12.LADDER))
        all_flags = {flag for s in s12.STEPS for flags in s["terminals"].values() for flag in flags}
        self.assertTrue(all(flag.startswith(s12.PREFIX) for flag in all_flags))
        self.assertFalse(any(any(part in flag for part in
                                (".harem.attitude.", ".enmity.", ".closed", ".committed"))
                             for flag in all_flags))

    def test_first_failure_is_pending_and_refusals_are_final(self):
        settle, retry = s12.STEPS
        self.assertNotIn(s12.P("unsettled"), settle["terminals"]["spoiled"])
        for step in s12.STEPS:
            self.assertIn(s12.P("unsettled"), step["terminals"]["refused"])
            self.assertNotIn(s12.P("settle.done"), step["terminals"]["refused"])
        self.assertIn(s12.P("unsettled"), retry["forbids"])

    def test_presence_is_current_and_paid_page_is_only_consumed(self):
        for rel in s12.PAIR:
            self.assertIn(rel + ".harem.eligible", s12.COMMON_REQUIRES)
            self.assertIn(rel + ".present_now", s12.COMMON_REQUIRES)
            self.assertIn(rel + ".closed", s12.COMMON_FORBIDS)
        self.assertIn("trickster", s12.COMMON_REQUIRES)
        self.assertIn("foresight.page_taken", s12.COMMON_REQUIRES)
        self.assertEqual(len(s12.ENMITY_OVERRIDES), 2)
        for step in s12.STEPS:
            for flags in step["terminals"].values():
                self.assertNotIn("foresight.page_taken", flags)


if __name__ == "__main__":
    unittest.main()
