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
        self.assertEqual([s["Id"] for s in first["Scenes"] if s["Id"] in {v["Id"] for v in scenes}],
                         [s["Id"] for s in scenes])
        self.assertEqual([s["Id"] for s in first["Scenes"]],
                         [s["Id"] for s in second["Scenes"]])
        self.assertIn(contract_identities([s for s in self.payload['Scenes'] if s['Id'] == pair.ID]), {1: (('household.pair.anevia_irabeth.ack',),)}[1])

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
            answer = ordered_answer(pages["start"]["Choices"], index, ((('wives', False, None, None, (), ()), ('dispatch', False, None, None, (), ()), (None, True, None, None, (), ())),))
            visited = set()
            while answer["Next"]:
                self.assertNotIn(answer["Next"], visited)
                visited.add(answer["Next"])
                answer = select_answer(pages[answer["Next"]]["Choices"], (('wives', False, None, None, (), ()), (None, False, None, None, (), ())), expected_position=0)
            self.assertEqual(answer["Set"], [pair.ID + ".marriage_acknowledged"])
            self.assertFalse(answer["Abort"])
        later = select_answer(pages["start"]["Choices"], ((None, True, None, None, (), ()),), expected_position=2)
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




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)




def ordered_answer(answers, ordinal, expected_orders):
    """Protect answer order, then select its declared structural destination."""
    actual = tuple(answer_key(answer) for answer in answers)
    if actual not in expected_orders:
        raise AssertionError(('answer order/gates changed', actual, expected_orders))
    for order in expected_orders:
        if order == actual:
            key = next(key for order_index, key in enumerate(order) if order_index == ordinal)
            return select_answer(answers, (key,))
    raise AssertionError('missing declared answer order')

if __name__ == "__main__":
    unittest.main()
