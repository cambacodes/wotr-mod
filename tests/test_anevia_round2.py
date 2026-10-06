"""Played slot landings, spouse evidence and arrival clocks for Anevia."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.test_anevia_partner_stance import walk

ROOT = Path(__file__).resolve().parents[1]


def windows_hold(windows, flags, times, hour):
    return all(window["Flag"] not in flags or
               hour - times[window["Flag"]] >= window.get("MinAgeHours", 0)
               for window in windows)


class AneviaRoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.books = {book["Id"]: book for book in cls.story["Scenes"]}

    def test_slots_bridge_to_saved_pages_without_granting_receipts(self):
        played = []
        for path in (ROOT / "tools/route_packs/explicit_slots/anevia").glob("*.json"):
            brief = json.loads(path.read_text(encoding="utf-8"))
            identity = brief["slot_id"].rsplit(".explicit.", 1)[0]
            if identity.startswith("three_"):
                continue
            book = self.books[identity]
            nodes = {page["Id"]: page for page in book["Nodes"]}
            slot = nodes[brief["slot_id"]]
            self.assertEqual(brief["default_text"], slot["Text"])
            self.assertEqual(slot["Choices"][0]["Next"], brief["source_node"])
            self.assertEqual(slot["Choices"][0]["Set"], [])
            self.assertTrue(any(answer.get("Next") == brief["slot_id"]
                                for page in book["Nodes"] for answer in page["Choices"]))
            self.assertFalse(slot.get("Paragraphs"))
            buildup = nodes["round2.buildup." + brief["source_node"]]
            self.assertEqual(buildup["Choices"][0]["Next"], brief["slot_id"])
            self.assertTrue(buildup["Text"])
            played.append(brief["slot_id"])
        self.assertEqual(len(played), 18)
        sleep = next(page for page in self.books["anevia.the_evening_without_a_case"]["Nodes"]
                     if page["Id"] == "sleep")
        self.assertEqual(sleep["Choices"][0]["Next"], "morning")

    def test_discovery_is_played_only_with_a_present_wife(self):
        book = self.books["anevia.the_last_ordinary_thing"]
        for present in (False, True):
            flags = {"anevia.partner_stance.secret", "anevia.committed"}
            if present:
                flags.add("irabeth.present_now")
            outcomes = walk(book, flags)
            self.assertTrue(outcomes)
            self.assertTrue(all({"anevia.partner_lie_exposed", "anevia.closed", "anevia.parted"} <= state
                                for state in outcomes))
        nodes = {page["Id"]: page for page in book["Nodes"]}
        self.assertIn("watch captain's receipt", nodes["partner_two_reports"]["Text"])
        self.assertIn("Stay away from our house", nodes["partner_how_long"]["Text"])
        self.assertFalse(any("irabeth.closed" in answer.get("Set", ())
                             for page in book["Nodes"] for answer in page["Choices"]))

    def test_physical_return_windows_are_distinct(self):
        windows = self.story["Presences"]["anevia.presence"]["ContactWindows"]
        wardrobe = "anevia.trickster.gone.wardrobe"
        fetched = "anevia.trickster.gone.fetched"
        crate = "anevia.trickster.cost.crated"
        for flags, times, arrival in (({wardrobe}, {wardrobe: 24}, 72),
                                      ({fetched}, {fetched: 96}, 108),
                                      ({wardrobe, crate}, {wardrobe: 72, crate: 0}, 144)):
            self.assertFalse(windows_hold(windows, flags, times, arrival - 1))
            self.assertTrue(windows_hold(windows, flags, times, arrival))
        journey = self.books[wardrobe]["ContactWindows"]
        self.assertFalse(windows_hold(journey, {crate}, {crate: 0}, 71))
        self.assertTrue(windows_hold(journey, {crate}, {crate: 0}, 72))

    def test_native_survival_and_recollection_match_played_history(self):
        bread = self.books["anevia.trickster.native.bread_returned"]
        self.assertIn("trickster.ever", bread["Requires"])
        self.assertNotIn("trickster.now", bread["Requires"])
        self.assertEqual(set(bread["RequiresAnyGroups"][0]), {
            "irabeth.trickster.returned", "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record"})
        for identity, book in self.books.items():
            if identity.startswith("anevia.trickster.epilogue.native_tirabade"):
                self.assertNotIn("no notes or traces", book["Nodes"][0]["Text"])
        aeon = self.books["anevia.ending_aeon"]["Nodes"][0]["Text"]
        self.assertIn("died in the River Kingdoms", aeon)
        self.assertNotIn("ran a tavern", aeon)
        for suffix in ("second_ask", "fetched_second_ask"):
            book = self.books["anevia.trickster.gone." + suffix]
            self.assertFalse(any("since that wardrobe opened" in page["Text"] for page in book["Nodes"]))

    def test_paid_and_kept_closet_widows_reach_their_earned_yes(self):
        from tools.timeline_contract_lint import replay_schedule
        contracts = json.loads((ROOT / "tools/timeline_contracts.json").read_text(encoding="utf-8"))
        for schedule in contracts["schedules"]:
            if schedule["name"] in ("paid-widow", "kept-closet-widow"):
                with self.subTest(history=schedule["name"]):
                    result = replay_schedule(self.story, schedule)
                    self.assertIsNone(result["failure"])
                    self.assertEqual(result["hour"], 168)


if __name__ == "__main__":
    unittest.main()
