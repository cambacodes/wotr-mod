"""S20 reuses earned account history; it never manufactures a joint scene."""
import copy
import unittest

from storylines.harem_rows import s20
from tests.story_fixture import fresh_story
from tools import savecompat


def visible(record, flags):
    return (all(key in flags for key in record.get("Requires", []))
            and not any(key in flags for key in record.get("Forbids", []))
            and all(any(key in flags for key in group) for group in record.get("AnyGroups", [])))


class S20ReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = fresh_story(include_harem=False)
        cls.after = copy.deepcopy(cls.before)
        s20.register(cls.after, cls.after["Scenes"], cls.after["Etudes"])
        cls.entry = next(item for item in cls.after["Books"]["trickster.ledger"]["Entries"]
                         if item["Id"] == s20.ENTRY_ID)

    def test_registration_changes_only_one_historical_entry(self):
        reverted = copy.deepcopy(self.after)
        reverted["Books"]["trickster.ledger"]["Entries"].remove(self.entry)
        self.assertEqual(self.before, reverted)
        self.assertEqual([], savecompat.check(self.after))

    def test_discovery_and_repeat_registration_are_safe(self):
        payload = copy.deepcopy(self.before)
        s20.register(payload, payload["Scenes"], payload["Etudes"])
        once = copy.deepcopy(payload)
        s20.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(once, payload)
        self.assertEqual(self.entry, next(item for item in payload["Books"]["trickster.ledger"]["Entries"]
                                          if item["Id"] == s20.ENTRY_ID))

    def test_three_outcomes_have_real_unchanged_producers(self):
        scene = next(item for item in self.before["Scenes"] if item["Id"] == s20.ACCOUNT)
        decide = next(node for node in scene["Nodes"] if node["Id"] == "decide")
        self.assertEqual(["go", "for_her", "kept"], [choice["Next"] for choice in decide["Choices"]])
        for index, outcome in enumerate(s20.OUTCOMES):
            with self.subTest(outcome=outcome):
                self.assertIn(outcome, decide["Choices"][index]["Set"])
                flags = {*self.entry["Requires"], outcome}
                self.assertTrue(visible(self.entry, flags))
                lines = [line for line in self.entry["Lines"][:3] if visible(line, flags)]
                self.assertEqual([self.entry["Lines"][index]], lines)
                flags.remove(s20.ACCOUNT)
                self.assertFalse(visible(self.entry, flags), "selected answer is not completed account")

    def test_paid_page_current_path_and_table_are_required(self):
        flags = {*self.entry["Requires"], s20.OUTCOMES[0]}
        for missing in ("trickster.now", "foresight.page_taken", "household.table.kept"):
            with self.subTest(missing=missing):
                self.assertFalse(visible(self.entry, (flags - {missing}) | {"shyka.met", "trickster.ever"}))
        self.assertFalse(visible(self.entry, set(self.entry["Requires"])), "no account result inferred")

    def test_offer_and_deferral_do_not_invent_a_reply_or_duel(self):
        for outcome in s20.OUTCOMES:
            flags = {*self.entry["Requires"], outcome}
            self.assertFalse(visible(self.entry["Lines"][3], flags))
            self.assertFalse(visible(self.entry["Lines"][4], flags))
        self.assertIn("whether they have spoken", self.entry["Lines"][1]["Text"])
        self.assertIn("postponed", self.entry["Lines"][2]["Text"])
        by_id = {scene["Id"]: scene for scene in self.before["Scenes"]}
        self.assertIn("jannah.trickster.challenge", by_id)
        yielding = by_id["jannah.circle.yielding_the_circle"]
        explain = next(node for node in yielding["Nodes"] if node["Id"] == "explain")
        self.assertIn("jannah.circle.yielded_the_circle", explain["Choices"][0]["Set"])
        flags = {*self.entry["Requires"], s20.OUTCOMES[0], "jannah.circle.yielded_the_circle"}
        self.assertFalse(visible(self.entry["Lines"][4], flags), "yield selection is not its aftermath")
        flags.add(yielding["Id"])
        self.assertTrue(visible(self.entry["Lines"][4], flags))

    def test_history_survives_loss_without_creating_attendance(self):
        flags = {*self.entry["Requires"], s20.OUTCOMES[0], "seelah_dead", "seelah.closed",
                 "jannah.dead", "jannah.closed", "jannah.epoch_unavailable", "seelah.epoch_unavailable"}
        self.assertTrue(visible(self.entry, flags))
        self.assertEqual(self.before["Scenes"], self.after["Scenes"])
        for field in ("DepartureEpochs", "Relationships", "Presences", "SeatWomen", "Counts", "RestAllowances"):
            self.assertEqual(self.before.get(field), self.after.get(field))

    def test_registration_order_and_conflicts_fail_clearly(self):
        with self.assertRaisesRegex(ValueError, "assembled Trickster Ledger"):
            s20.register({}, [], {})
        payload = copy.deepcopy(self.after)
        next(item for item in payload["Books"]["trickster.ledger"]["Entries"]
             if item["Id"] == s20.ENTRY_ID)["Text"] = "Incompatible earlier registration"
        with self.assertRaisesRegex(ValueError, "Conflicting S20"):
            s20.register(payload, payload["Scenes"], payload["Etudes"])
