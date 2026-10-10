"""Private repair: honest bout outcomes, learned strain, attendance and caps."""
import copy
import unittest
from unittest.mock import patch
from tests.structure import without_prose

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from storylines import harem_caps, household
from storylines.harem_rows import z_household_mend as mend
from tools import departure_lint, payoff_lint, rrt_verify as rules



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class HouseholdMendTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.first, cls.later = (cls.model.by_id[sid] for sid in mend.SCENE_IDS)

    def state(self, extra=(), omit=(), chapter=5, hour=1000):
        state = rules.SimState(chapter, hour)
        state.flags.update({"trickster", "trickster.foresight.accepted",
                            "trickster.foresight.cost.promise", household.KEPT,
                            "camellia.committed", "camellia.trickster.terms_named", mend.STRAIN})
        state.flags.update(extra)
        state.flags.difference_update(omit)
        rules.sim_complete(self.model, state)
        return state

    def test_only_learned_unmended_strain_and_paid_current_path_admit(self):
        self.assertTrue(rules.sim_available(self.model, self.first, self.state()))
        for flag in (mend.STRAIN, "trickster", "trickster.foresight.accepted",
                     household.KEPT, "camellia.trickster.terms_named"):
            with self.subTest(flag=flag):
                self.assertFalse(rules.sim_available(self.model, self.first, self.state(omit=(flag,))))
        for flag in (mend.MEND, "trickster.failed", "fool_king.gone", "sacrifice"):
            self.assertFalse(rules.sim_available(self.model, self.first, self.state(extra=(flag,))))
        self.assertTrue(rules.sim_available(self.model, self.first,
                        self.state(extra=("sacrifice", "trickster.ever", "ending.trickster"))))
        self.assertIn(mend.STRAIN, self.story["PendingHooks"])
        produced = {f for s in self.story['Scenes'] for n in s['Nodes'] for c in n['Choices'] for f in c['Set']}
        self.assertNotIn(mend.STRAIN, produced)

    def test_absence_and_closure_withdraw_both_opportunities(self):
        for flag in ("camellia.closed", "camellia.killed", "camellia.dead",
                     "camellia.kicked_out", "camellia.epoch_unavailable",
                     "camellia.returned_actor_lost", "camellia.presence.failed"):
            with self.subTest(flag=flag):
                state = self.state(extra=(flag, mend.SCENE_IDS[0] + ".attempted"))
                self.assertFalse(rules.sim_available(self.model, self.first, state))
                self.assertFalse(rules.sim_available(self.model, self.later, state))
        # Historical return alone cannot lift deliberate closure or later loss.
        for flag in ("camellia.closed", "camellia.returned_actor_lost", "camellia.epoch_unavailable"):
            self.assertFalse(rules.sim_available(self.model, self.first,
                self.state(extra=(flag, "camellia.trickster.coffin_life"))))

    def test_other_woman_and_enmity_never_hide_private_repair(self):
        state = self.state(extra=("galfrey.closed", "galfrey.dead", "galfrey.epoch_unavailable",
                                 "camellia.harem.enmity.galfrey", "galfrey.harem.enmity.camellia"))
        self.assertTrue(rules.sim_available(self.model, self.first, state))
        for scene in (self.first, self.later):
            self.assertEqual(scene["Participants"], ["camellia"])
            self.assertEqual(scene["Pair"], [])
            self.assertFalse(any("enmity" in f for f in scene["Forbids"]))

    def test_earned_coffin_return_lifts_only_its_declared_absence(self):
        earned = ("camellia.killed", "camellia.dead",
                  "camellia.trickster.cost.knows_you_tried",
                  "camellia.trickster.death_observed")
        self.assertTrue(rules.sim_available(self.model, self.first, self.state(extra=earned)))
        # The existing staged death also overrides its own unrecruitment;
        # deliberate closure and a subsequent loss remain final.
        for loss in ("camellia.closed", "camellia.returned_actor_lost", "camellia.epoch_unavailable"):
            self.assertFalse(rules.sim_available(self.model, self.first,
                self.state(extra=(*earned, loss))))

    def test_every_answer_remains_selectable_and_records_the_honest_result(self):
        for scene in (self.first, self.later):
            attempted = scene["Id"] + ".attempted"
            outcomes = walk(self, self.model, scene, self.state())
            first, second, third, fourth = outcomes
            self.assertTrue(all(o is not None for o in (first, second, third, fourth)))
            won, nick, refused, abort = outcomes
            self.assertIn(scene["Id"] + ".commander_won", won.flags)
            self.assertNotIn(mend.MEND, won.flags)
            self.assertIn(mend.MEND, nick.flags)
            self.assertIn(scene["Id"] + ".cost.nick", nick.flags)
            self.assertIn(scene["Id"] + ".cost.unmarked_boast_lost", nick.flags)
            self.assertNotIn(mend.MEND, refused.flags)
            for outcome in (won, nick, refused):
                self.assertIn(attempted, outcome.flags)
                self.assertEqual(outcome.rest_spent["household.pair"], 1)
            self.assertNotIn(attempted, abort.flags)
            self.assertFalse(abort.rest_spent)
            self.assertEqual(saved_answer(scene["Nodes"][0]["Choices"], 0)["Check"]["Success"], "commander_touch")
            self.assertEqual(saved_answer(scene["Nodes"][0]["Choices"], 0)["Check"]["Failure"], "camellia_touch")

    def test_failed_or_refused_opportunity_leaves_delayed_later_mend(self):
        self.assertFalse(rules.sim_available(self.model, self.later, self.state()))
        for outcome in walk(self, self.model, self.first, self.state()):
            attempted = mend.SCENE_IDS[0] + ".attempted"
            if attempted not in outcome.flags or mend.MEND in outcome.flags:
                continue
            # Successful rest restores the existing shared optional allowance.
            outcome.rest_spent.clear()
            outcome.hour += 47
            rules.sim_complete(self.model, outcome)
            self.assertFalse(rules.sim_available(self.model, self.later, outcome))
            outcome.hour += 1
            self.assertTrue(rules.sim_available(self.model, self.later, outcome))
            later_outcomes = walk(self, self.model, self.later, outcome)
            self.assertIn(mend.MEND, later_outcomes[1].flags)
            self.assertIn(attempted, later_outcomes[1].flags)
            for done in later_outcomes[:3]:
                done.rest_spent.clear()
                self.assertFalse(rules.sim_available(self.model, self.first, done))
                self.assertFalse(rules.sim_available(self.model, self.later, done))

    def test_table_chapters_and_shared_optional_allowance(self):
        for chapter in (1, 2, 4, 6):
            self.assertFalse(rules.sim_available(self.model, self.first, self.state(chapter=chapter)))
        self.assertTrue(rules.sim_available(self.model, self.first, self.state(chapter=3)))
        state = self.state()
        state.rest_spent["household.pair"] = 1
        self.assertFalse(rules.sim_available(self.model, self.first, state))
        # The existing cap collects this slice when other reviewed slices arrive.
        payload = dict(Scenes=copy.deepcopy([self.first, self.later]), Counts={})
        for i in range(3):
            scene = copy.deepcopy(self.first)
            scene.update(Id="test.mend.%d" % i, HouseholdWitness="test.attempt.%d" % i)
            payload["Scenes"].append(scene)
        harem_caps.apply(payload)
        self.assertEqual(payload["Counts"]["household.cap.ch5.mend"]["Min"], 4)
        self.assertIn(self.first["HouseholdWitness"], payload["Counts"]["household.cap.ch5.mend"]["Of"])
        self.assertIn("household.cap.ch5.mend", payload["Scenes"][0]["Forbids"])

    def test_surface_classification_and_no_other_state_writes(self):
        registered = {s["scene"] for s in departure_lint.contracts()["women"]["camellia"]["surfaces"]}
        self.assertTrue(set(mend.SCENE_IDS) <= registered)
        for scene in (self.first, self.later):
            self.assertEqual(scene["Relationship"], "household")
            self.assertEqual(scene["HouseholdCategory"], "mend")
            for node in scene["Nodes"]:
                self.assertFalse(node["Paragraphs"])
                for choice in node["Choices"]:
                    self.assertTrue(all(f == mend.MEND or f.startswith(scene["Id"] + ".") for f in choice["Set"]))
        self.assertEqual(departure_lint.check(self.story), [])
        self.assertEqual(payoff_lint.check(self.story), [])

    def test_registration_is_append_only_and_idempotent(self):
        payload = copy.deepcopy(self.story)
        before = copy.deepcopy(payload)
        mend.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(without_prose(payload), without_prose(before))
        # Later shared finalizers can append their own scenes. Our registrar
        # preserves all incoming scene positions and appends only this slice.
        prefix = copy.deepcopy(self.story)
        prefix['Scenes'] = [s for s in prefix['Scenes'] if s['Id'] not in mend.SCENE_IDS]
        old_ids = [s['Id'] for s in prefix['Scenes']]
        mend.register(prefix, prefix['Scenes'], prefix['Etudes'])
        self.assertEqual([s['Id'] for s in prefix['Scenes']], old_ids + list(mend.SCENE_IDS))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        check = self.first['Nodes'][0]['Choices'][0]['Check']
        with patch.dict(check, Success='camellia_touch'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_every_answer_remains_selectable_and_records_the_honest_result()


if __name__ == "__main__":
    unittest.main()
