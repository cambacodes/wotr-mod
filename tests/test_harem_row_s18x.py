"""S18.x claimant independence, blocked remedy and bodily wrapper contracts."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s18x
from storylines import foresight
from tools import rrt_verify

ROOT = Path(__file__).resolve().parents[1]


class CaptivityAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.consumers_before = dict(foresight.CONSUMERS)
        cls.payload = fresh_story(include_harem=False)
        s18x.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rrt_verify.Model(cls.payload)
        cls.private = cls.model.by_id[s18x.P + "account"]
        cls.table = cls.model.by_id[s18x.P + "account_table"]

    @classmethod
    def tearDownClass(cls):
        foresight.CONSUMERS.clear()
        foresight.CONSUMERS.update(cls.consumers_before)

    def state(self, scene):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(scene["Requires"])
        # Rules.Complete latches this from the current Trickster before a hub
        # is opened; fixture states supply the historical latch explicitly.
        state.flags.add("trickster.ever")
        return state

    def test_claimant_can_object_when_respondent_is_dead_closed_unromanced_or_a_ghost(self):
        for respondent_state in ((), ("hepzamirah.closed",), ("hepzamirah.dead_observed",),
                                 ("hepzamirah.epoch_unavailable",), ("hepzamirah.ghost_dispersed",)):
            with self.subTest(respondent=respondent_state):
                state = self.state(self.private)
                state.flags.update(respondent_state)
                self.assertTrue(rrt_verify.sim_available(self.model, self.private, state))
                self.assertFalse(rrt_verify.sim_available(self.model, self.table, state))
        self.assertEqual(self.private["ContactUnit"], s18x.claimant.UNIT)
        self.assertFalse(self.private["AdditionalContactUnits"])
        self.assertFalse(self.private["Participants"])

    def test_current_claimant_loss_and_page_path_and_chapter_are_required(self):
        for loss in ("horzalah.closed", "horzalah.dead", "horzalah.trickster.left_free",
                     "horzalah.epoch_unavailable", "horzalah.presence.failed", "trickster.failed"):
            state = self.state(self.private)
            state.flags.update([loss, "horzalah.trickster.returned"])
            self.assertFalse(rrt_verify.sim_available(self.model, self.private, state), loss)
        for gate in ("trickster", "foresight.page_taken", "horzalah.present_now"):
            state = self.state(self.private)
            state.flags.remove(gate)
            self.assertFalse(rrt_verify.sim_available(self.model, self.private, state), gate)
        for chapter in (3, 4, 6):
            state = self.state(self.private)
            state.chapter = chapter
            self.assertFalse(rrt_verify.sim_available(self.model, self.private, state))

    def test_body_wrapper_blocks_ghost_confinement_and_later_loss(self):
        self.assertEqual(self.table["AdditionalContactUnits"], [s18x.respondent.BODY_UNIT])
        self.assertTrue(rrt_verify.household_presence_attachment(self.payload, self.table))
        state = self.state(self.table)
        self.assertTrue(rrt_verify.sim_available(self.model, self.table, state))
        state.flags.add(s18x.respondent.CONFINED)
        self.assertFalse(rrt_verify.sim_available(self.model, self.table, state))
        state.flags.add(s18x.respondent.RELEASED)
        state.times[s18x.respondent.CONFINED] = state.hour - 72
        self.assertTrue(rrt_verify.sim_available(self.model, self.table, state))
        for loss in ("hepzamirah.closed", "hepzamirah.epoch_unavailable", "hepzamirah.presence.failed"):
            lost = copy.deepcopy(state)
            lost.flags.add(loss)
            self.assertFalse(rrt_verify.sim_available(self.model, self.table, lost), loss)
        state.flags.remove(s18x.respondent.RET)
        state.flags.add(s18x.respondent.DISPERSED)
        self.assertFalse(rrt_verify.sim_available(self.model, self.table, state))
        # Both the runtime and simulation read the contacts' presence windows.
        windows = self.payload["Presences"][s18x.respondent.PRESENCE]["ContactWindows"]
        self.assertIn({"Flag": "hepzamirah.trickster.bond.the_hunt", "MinAgeHours": 120}, windows)
        state = self.state(self.table)
        hunt = "hepzamirah.trickster.bond.the_hunt"
        state.flags.add(hunt)
        for age, available in ((119, False), (120, True)):
            state.times[hunt] = state.hour - age
            self.assertEqual(rrt_verify.sim_available(self.model, self.table, state), available)

    def test_truce_and_prior_native_hearing_never_pay_the_atrocity(self):
        for histories in ((), ("horzalah.trickster.beat.sister_heard",),
                          ("household.pair.horzalah_hepzamirah.truce.seen", "household.packet.k3.seen")):
            state = self.state(self.private)
            state.flags.update(histories)
            rrt_verify.sim_complete(self.model, state)
            self.assertNotIn(s18x.REMEDY_READY, state.flags)
            root = next(n for n in self.private["Nodes"] if n["Id"] == "start")
            self.assertFalse(rrt_verify.sim_choice_available(select_answer(root["Choices"],
                    (('remedy',
                      False,
                      None,
                      None,
                      ('household.docket.horzalah_hepzamirah.captivity_remedy_ready',
                       'household.docket.horzalah_hepzamirah.instructions.carried',
                       'household.docket.horzalah_hepzamirah.cost.hepzamirah_trap_knowledge'),
                      ()),), expected_position=0), state))
            self.assertTrue(rrt_verify.sim_choice_available(select_answer(root["Choices"], (('unresolved', False, None, None, (), ()),), expected_position=1), state))
            self.assertTrue(rrt_verify.sim_choice_available(select_answer(root["Choices"], ((None, True, None, None, (), ()),), expected_position=2), state))

    def test_completion_exhausts_both_wrappers_and_survives_reload(self):
        for scene in (self.private, self.table):
            terminal = next(n for n in scene["Nodes"] if n["Id"] == ("named" if scene is self.table else "unresolved"))
            saved = json.loads(json.dumps(select_answer(terminal["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"]))
            for wrapper in (self.private, self.table):
                state = self.state(wrapper)
                state.flags.update(saved)
                self.assertFalse(rrt_verify.sim_available(self.model, wrapper, state))
            self.assertEqual(scene["RestAllowance"], "household.protected")
            self.assertFalse(scene["Optional"])
        for scene in (self.private, self.table):
            abort = select_answer(next(n for n in scene["Nodes"] if n["Id"] == "start")["Choices"], ((None, True, None, None, (), ()),), expected_position=2)
            self.assertTrue(abort["Abort"])
            self.assertFalse(abort["Set"])
            self.assertIsNone(abort["Next"])
            for node in scene["Nodes"]:
                for choice in node["Choices"]:
                    self.assertTrue(all(flag in s18x.WRITES for flag in choice["Set"]))
        state = self.state(self.private)
        state.rest_spent["household.protected"] = 2
        self.assertFalse(rrt_verify.sim_available(self.model, self.private, state))

    def test_registration_is_idempotent_and_prose_has_no_spectral_body_or_epilogue_paragraphs(self):
        self.assertEqual(rrt_verify.validate(self.model), [])
        payload = copy.deepcopy(self.payload)
        ids = [s["Id"] for s in payload["Scenes"]]
        s18x.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(ids, [s["Id"] for s in payload["Scenes"]])
        for scene in (self.private, self.table):
            ids = {node["Id"] for node in scene["Nodes"]}
            for node in scene["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                for choice in node["Choices"]:
                    self.assertTrue(choice["Next"] is None or choice["Next"] in ids)




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
