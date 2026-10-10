"""S20 reuses earned account history; it never manufactures a joint scene."""
import copy
import unittest
from tests.structure import without_prose

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
        scene = next(item for item in without_prose(self.before["Scenes"]) if item["Id"] == s20.ACCOUNT)
        decide = next(node for node in scene["Nodes"] if node["Id"] == "decide")
        self.assertEqual(["go", "for_her", "kept"], [choice["Next"] for choice in decide["Choices"]])
        for index, outcome in enumerate(s20.OUTCOMES):
            with self.subTest(outcome=outcome):
                self.assertIn(outcome, ordered_answer(decide["Choices"], index, ((('go', False, None, None, (), ()), ('for_her', False, None, None, (), ()), ('kept', False, None, None, (), ())),))["Set"])
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
        by_id = {scene["Id"]: scene for scene in without_prose(self.before["Scenes"])}
        self.assertIn("jannah.trickster.challenge", by_id)
        yielding = by_id["jannah.circle.yielding_the_circle"]
        explain = next(node for node in yielding["Nodes"] if node["Id"] == "explain")
        self.assertIn("jannah.circle.yielded_the_circle", select_answer(explain["Choices"], (('yielded', False, None, None, (), ()),), expected_position=0)["Set"])
        flags = {*self.entry["Requires"], s20.OUTCOMES[0], "jannah.circle.yielded_the_circle"}
        self.assertFalse(visible(self.entry["Lines"][4], flags), "yield selection is not its aftermath")
        flags.add(yielding["Id"])
        self.assertTrue(visible(self.entry["Lines"][4], flags))

    def test_history_survives_loss_without_creating_attendance(self):
        flags = {*self.entry["Requires"], s20.OUTCOMES[0], "seelah_dead", "seelah.closed",
                 "jannah.dead", "jannah.closed", "jannah.epoch_unavailable", "seelah.epoch_unavailable"}
        self.assertTrue(visible(self.entry, flags))
        self.assertEqual(without_prose(self.before["Scenes"]), without_prose(self.after["Scenes"]))
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
