"""S07 stays a pre-page acknowledgment, with current physical attendance."""
import unittest

from story import make_story, scenes
from storylines import household_pair_anevia_irabeth as pair
from tests.story_fixture import fresh_story


class FixedMarriageAcknowledgment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        cls.book = next(s for s in cls.payload["Scenes"] if s["Id"] == pair.ID)

    def test_registered_once_without_reordering_original_scenes(self):
        first, second = make_story(), make_story()
        self.assertEqual([s["Id"] for s in first["Scenes"][:len(scenes)]],
                         [s["Id"] for s in scenes])
        self.assertEqual([s["Id"] for s in first["Scenes"]],
                         [s["Id"] for s in second["Scenes"]])
        self.assertEqual(sum(s["Id"] == pair.ID for s in self.payload["Scenes"]), 1)

    def test_attendance_does_not_require_page_or_committed_household_seats(self):
        book = self.book
        self.assertEqual(book["Chapters"], [2])
        self.assertEqual(book["Areas"], [pair.CAMP])
        self.assertEqual(book["AnswerLists"], [pair.HUB])
        # Ch2 bodies differ from the capital actors used by later routes.
        self.assertEqual(pair.IRABETH, "d1e567736abf23943b9f041ba7a0bc23")
        self.assertEqual(pair.ANEVIA, "ea562adea1736874c9c5616d140fe773")
        self.assertEqual(book["ContactUnit"], pair.IRABETH)
        self.assertEqual(book["AdditionalContactUnits"], [pair.ANEVIA])
        self.assertFalse(book.get("Participants"))
        self.assertFalse(any("foresight" in f or "eligible" in f or "committed" in f
                             for f in book["Requires"]))
        for woman in ("anevia", "irabeth"):
            for suffix in (".closed", "_dead", "_gone"):
                self.assertIn(woman + suffix, book["Forbids"])
        # Capital-specific absence readers cannot supply current camp attendance.
        for woman in ("anevia", "irabeth"):
            self.assertNotIn(woman + "_away", book["Forbids"])
        self.assertFalse(book.get("ForbidOverrides"))

    def test_both_answers_finish_but_later_spends_nothing(self):
        pages = {p["Id"]: p for p in self.book["Nodes"]}
        for index in (0, 1):
            answer = pages["start"]["Choices"][index]
            visited = set()
            while answer["Next"]:
                self.assertNotIn(answer["Next"], visited)
                visited.add(answer["Next"])
                answer = pages[answer["Next"]]["Choices"][0]
            self.assertEqual(answer["Set"], [pair.ID + ".marriage_acknowledged"])
            self.assertFalse(answer["Abort"])
        later = pages["start"]["Choices"][2]
        self.assertTrue(later["Abort"])
        self.assertEqual(later["Set"], [])
        self.assertIsNone(later["Next"])
        self.assertEqual(self.book["RestAllowance"], "household.protected")
        self.assertEqual(self.book["HouseholdWitness"], pair.ID)

    def test_no_ladder_stance_or_truth_invented(self):
        writes = [f for p in self.book["Nodes"] for c in p["Choices"] for f in c["Set"]]
        self.assertEqual(writes, [pair.ID + ".marriage_acknowledged"])
        self.assertFalse(any(s["Id"].startswith("household.pair.anevia_irabeth.")
                             and s["Id"] != pair.ID for s in self.payload["Scenes"]))
        self.assertFalse(any(p.get("Paragraphs") for p in self.book["Nodes"]))


if __name__ == "__main__":
    unittest.main()
