"""S23's permitted historical branch and blocked settlement boundary."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s23
from tools import rrt_verify


class S23Registration(unittest.TestCase):
    def setUp(self):
        self.old_scene = {"Id": "existing", "Nodes": [{"Id": "old", "Choices": []}]}
        self.payload = {"Scenes": [copy.deepcopy(self.old_scene)]}
        self.refs = {"existing": "unchanged"}
        s23.register(self.payload, self.payload["Scenes"], self.refs)
        self.body = self.payload["Scenes"][-1]

    def test_append_only_and_duplicate_registration_rejected(self):
        self.assertEqual(self.payload["Scenes"][0], self.old_scene)
        self.assertEqual(self.refs, {"existing": "unchanged"})
        with self.assertRaises(ValueError):
            s23.register(self.payload, self.payload["Scenes"], self.refs)

    def test_current_qualified_claimant_and_paid_page(self):
        self.assertEqual(self.body["Participants"], ["minagho_chivarro"])
        self.assertEqual(self.body["ParticipantWomen"], ["chivarro"])
        self.assertTrue({"participant.chivarro.available", "chivarro.present_now",
                         "trickster", "foresight.page_taken", "herrax.asked_kill_chivarro"}
                        <= set(self.body["Requires"]))
        self.assertNotIn("minagho_chivarro.harem.eligible", self.body["Requires"])
        self.assertFalse(any("minagho.present" in key or "herrax.committed" in key
                             for key in self.body["Requires"]))
        self.assertEqual(self.body["ForbidOverrides"], {"sacrifice": "trickster.commander_back"})

    def test_no_settlement_or_remote_body_is_fabricated(self):
        writes = [flag for node in self.body["Nodes"] for choice in node["Choices"]
                  for flag in choice["Set"]]
        self.assertEqual(writes, [s23.PREFIX + "turf.seen", s23.PREFIX + "historical"])
        self.assertTrue(all(node["Speaker"] == "Chivarro" for node in self.body["Nodes"]))
        self.assertNotIn("Paragraphs", self.body["Nodes"][0])
        self.assertNotIn("Derived", self.payload)

    def test_protected_ch5_completion_and_clean_abort(self):
        self.assertEqual(self.body["Chapters"], [5])
        self.assertEqual(self.body["MaxChapter"], 5)
        self.assertEqual(self.body["RestAllowance"], "household.protected")
        self.assertIn(self.body["HouseholdWitness"], self.body["Forbids"])
        choices = self.body["Nodes"][0]["Choices"]
        self.assertEqual(select_answer(choices, (('historical', False, None, None, (), ()),), expected_position=0)["Next"], "historical")
        self.assertTrue(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1)["Abort"])
        self.assertEqual(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1)["Set"], [])
        self.assertIsNone(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1)["Next"])


class S23CurrentAttendance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = fresh_story(include_harem=False)
        s23.register(payload, payload["Scenes"], payload["Etudes"])
        cls.model = rrt_verify.Model(payload)
        cls.body = next(body for body in cls.model.scenes if body["Id"] == s23.PREFIX + "turf")
        cls.closed = payload["Relationships"]["minagho_chivarro"]["ClosedFlag"]

    def available(self, add=(), remove=()):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update({"availability.observed", "trickster", "trickster.foresight.accepted",
                            "household.table.kept", "herrax.asked_kill_chivarro",
                            "minachiv.complete", "minachiv.before_the_last_road",
                            "minachiv.future_chivarro", "minagho_chivarro.trickster.chivarro_in",
                            "minagho.dead"})
        state.flags.update(add)
        state.flags.difference_update(remove)
        rrt_verify.sim_complete(self.model, state)
        return rrt_verify.sim_available(self.model, self.body, state)

    def test_solo_chivarro_does_not_need_minagho_or_herrax_romance(self):
        self.assertTrue(self.available())
        self.assertTrue(self.available(add=("herrax.closed",)))

    def test_later_loss_and_closure_defeat_an_old_return(self):
        returned = "minagho_chivarro.trickster.returned_chivarro"
        self.assertTrue(self.available(add=("chivarro.dead", returned)))
        for loss in (self.closed, "chivarro.epoch_unavailable",
                     "minagho_chivarro.trickster.chivarro_sent_back",
                     "minagho_chivarro.trickster.chivarro_walked",
                     "minagho_chivarro.trickster.chivarro_declined"):
            with self.subTest(loss=loss):
                self.assertFalse(self.available(add=(returned, loss)))

    def test_no_unearned_page_arrival_or_living_commander(self):
        for missing in ("trickster.foresight.accepted", "trickster",
                        "minagho_chivarro.trickster.chivarro_in", "herrax.asked_kill_chivarro"):
            with self.subTest(missing=missing):
                self.assertFalse(self.available(remove=(missing,)))
        self.assertFalse(self.available(add=("sacrifice",)))
        self.assertTrue(self.available(add=("sacrifice", "ending.trickster")))




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

if __name__ == "__main__":
    unittest.main()
