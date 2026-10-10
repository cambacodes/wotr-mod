"""S10 indexed walks and fail-closed integration contract.

The bodily channel flags below are test inputs, not authored route producers.
They exercise loss of current attendance independently of historical commitment.
"""
import copy
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from tests.story_fixture import fresh_story

from storylines.harem_rows import s10
from tools import rrt_verify as verify, savecompat

ROOT = Path(__file__).resolve().parents[1]


class SeelahNenioRow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)

    def setUp(self):
        self.payload = copy.deepcopy(self.base)
        for woman in ("seelah", "nenio"):
            relationship = self.payload["Relationships"][woman]
            self.payload.setdefault("SeatWomen", {})[woman] = dict(
                Relationship=woman,
                Requires=[woman + ".present_now", "test.body." + woman],
                UnavailableFlags=list(relationship["UnavailableFlags"]),
                UnavailableOverrides=dict(relationship.get("UnavailableOverrides", {})))
        s10.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        # Only this graph is under test; the global verifier checks the assembled export.
        self.model = verify.Model(copy.deepcopy(dict(self.payload, Scenes=[self.payload["Scenes"][-1]])))
        self.scene = self.model.by_id[s10.QUESTION]
        self.state = verify.SimState(3, 1000)
        self.state.flags.update(self.scene["Requires"])
        for woman in ("seelah", "nenio"):
            self.state.flags.update(self.payload["SeatWomen"][woman]["Requires"])
            self.state.flags.add(self.model.composites[woman + ".harem.eligible"][0][0])

    def walk(self, indices):
        node = self.scene["Nodes"][0]
        before = set(self.state.flags)
        for index in indices:
            choice = node["Choices"][index]
            self.assertTrue(verify.sim_choice_available(choice, self.state))
            if choice["Abort"]:
                self.assertEqual(self.state.flags, before)
                return
            self.state.flags.update(choice["Set"])
            if choice["Next"] is None:
                self.state.flags.add(self.scene["Id"])
                return
            node = next(n for n in self.scene["Nodes"] if n["Id"] == choice["Next"])
        self.fail("Walk did not finish")

    def test_register_rejects_missing_attendance_without_partial_writes(self):
        payload = copy.deepcopy(self.base)
        before = copy.deepcopy(payload)
        with self.assertRaisesRegex(ValueError, "bodily SeatWomen"):
            s10.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, before)

    def test_answer_writes_only_deeds_and_keeps_friend_ceiling(self):
        self.walk([0, 0, 0])
        self.assertTrue(set(s10.ANSWERED) <= self.state.flags)
        self.assertTrue(all(".attitude." not in f and ".committed" not in f and ".enmity." not in f
                            for node in self.scene["Nodes"] for c in node["Choices"] for f in c["Set"]))
        self.assertFalse(verify.sim_available(self.model, self.scene, self.state))
        self.state.chapter = 5
        self.assertFalse(verify.sim_available(self.model, self.scene, self.state))
        self.assertEqual(self.payload["Derived"][s10.PREFIX + "alliance.kept"], [list(s10.ANSWERED[1:])])

    def test_decline_records_no_answer_or_deed(self):
        self.walk([1, 0])
        self.assertIn(s10.PREFIX + "question.declined", self.state.flags)
        self.assertFalse(set(s10.ANSWERED[1:]) & self.state.flags)
        self.assertFalse(verify.sim_available(self.model, self.scene, self.state))

    def test_abort_has_no_writes_and_remains_available(self):
        self.walk([2])
        self.assertTrue(verify.sim_available(self.model, self.scene, self.state))
        choice = select_answer(self.scene["Nodes"][0]["Choices"], ((None, True, None, None, (), ()),), expected_position=2)
        self.assertEqual(choice["Set"], [])
        self.assertIsNone(choice.get("NativeNext"))

    def test_page_path_friendship_body_and_closure_are_independent(self):
        self.assertTrue(verify.sim_available(self.model, self.scene, self.state))
        for missing in ("foresight.page_taken", "trickster", *s10.FRIENDS,
                        "test.body.seelah", "test.body.nenio", "seelah.present_now", "nenio.present_now"):
            with self.subTest(missing=missing):
                state = copy.deepcopy(self.state)
                state.flags.remove(missing)
                self.assertFalse(verify.sim_available(self.model, self.scene, state))
        for loss in ("seelah.closed", "nenio.closed", "seelah.plot_departed",
                     "nenio.dissolved", "seelah.epoch_unavailable", "nenio.epoch_unavailable",
                     "trickster.failed", "fool_king.gone"):
            with self.subTest(loss=loss):
                state = copy.deepcopy(self.state)
                state.flags.update([loss, "seelah.trickster.returned", "nenio.life.recreated"])
                self.assertFalse(verify.sim_available(self.model, self.scene, state))
        for chapter in (2, 4, 6):
            self.state.chapter = chapter
            self.assertFalse(verify.sim_available(self.model, self.scene, self.state))

    def test_enmity_overrides_are_directional_and_do_not_write_state(self):
        for source, other in (("seelah", "nenio"), ("nenio", "seelah")):
            state = copy.deepcopy(self.state)
            state.flags.add(source + ".harem.enmity." + other)
            self.assertFalse(verify.sim_available(self.model, self.scene, state))
            state.flags.add(other + ".harem.reconciled." + source)
            self.assertFalse(verify.sim_available(self.model, self.scene, state))
            state.flags.add(source + ".harem.reconciled." + other)
            self.assertTrue(verify.sim_available(self.model, self.scene, state))

    def test_allowance_and_dynamic_cap_apply_without_extra_arc(self):
        self.state.rest_spent["household.pair"] = 1
        self.assertFalse(verify.sim_available(self.model, self.scene, self.state))
        self.assertFalse(self.scene.get("HouseholdArcStart", False))
        self.assertEqual(self.scene["HouseholdCategory"], "dynamic")

    def test_third_ch5_dynamic_witness_caps_flavour_but_not_protected_dockets(self):
        from storylines import harem_caps
        payload = dict(Scenes=[s10.question()])
        for index in range(2):
            payload["Scenes"].append(dict(Id="test.dynamic.%d" % index,
                MinChapter=5, MaxChapter=5, Chapters=[5], HouseholdCategory="dynamic",
                HouseholdWitness="test.dynamic.%d.seen" % index, Forbids=[]))
        protected = dict(Id="test.protected", MinChapter=5, MaxChapter=5, Chapters=[5],
            HouseholdCategory="protected", HouseholdWitness="test.protected.seen", Forbids=[])
        payload["Scenes"].append(protected)
        harem_caps.apply(payload)
        key = "household.cap.ch5.dynamic"
        self.assertEqual(payload["Counts"][key]["Min"], 3)
        self.assertIn(key, payload["Scenes"][0]["Forbids"])
        self.assertEqual(protected["Forbids"], [])

    def test_ledger_keeps_historical_deeds_without_fabricating_living_speech(self):
        entry = self.payload["Books"]["trickster.ledger"]["Entries"][-1]
        self.assertEqual(entry["Requires"], [s10.PREFIX + "question.seen"])
        self.assertEqual([line["Requires"] for line in entry["Lines"]],
            [[s10.PREFIX + "alliance.kept"], [s10.PREFIX + "question.declined"]])
        self.assertFalse(any("explicit" in node["Id"] for node in self.scene["Nodes"]))

    def test_registration_is_append_only_idempotent_and_save_compatible(self):
        self.assertEqual(without_prose(self.base["Scenes"]), without_prose(self.payload["Scenes"][:-1]))
        before = copy.deepcopy(self.payload)
        s10.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.assertEqual(before, self.payload)
        self.assertEqual(savecompat.check(self.payload), [])
        self.assertEqual([n["Id"] for n in self.scene["Nodes"]], ["start", "account", "revised", "declined"])
        self.assertTrue(all(not n.get("Paragraphs") and n["Choices"] for n in self.scene["Nodes"]))


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
