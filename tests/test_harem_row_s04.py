"""S04: earned attendance, parked missing contracts, refusal and saved allowance."""
import copy
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s04
from tools import rrt_verify as verify


class S04Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = verify.Model(cls.story)
        cls.scene = cls.model.by_id[s04.P + "settle"]

    def state(self):
        state = verify.SimState(5, 1000)
        state.flags.update(self.scene["Requires"])
        for woman in self.scene["ParticipantWomen"]:
            state.flags.update(self.story["SeatWomen"][woman]["Requires"])
            state.flags.update(self.model.composites[woman + ".harem.eligible"][0])
        state.available_contacts = {
            contact["Options"][0]["Units"][0]
            for contact in self.scene["ParticipantContacts"].values()}
        return state

    def test_earned_page_path_table_and_both_current_bodies(self):
        self.assertIsNone(self.scene["ContactUnit"])
        self.assertTrue(verify.sim_available(self.model, self.scene, self.state()))
        for gate in ("trickster", "foresight.page_taken", "household.table.kept",
                     "seelah.harem.eligible", "camellia.harem.eligible",
                     "seelah.present_now", "camellia.present_now", "camellia.life.available"):
            with self.subTest(gate=gate):
                state = self.state()
                state.flags.remove(gate)
                self.assertFalse(verify.sim_available(self.model, self.scene, state))
        for chapter in (3, 4, 6):
            state = self.state()
            state.chapter = chapter
            self.assertFalse(verify.sim_available(self.model, self.scene, state))

    def test_return_history_cannot_override_closure_or_later_body_loss(self):
        for woman, loss in (("seelah", "seelah_dead"), ("camellia", "camellia.dead")):
            state = self.state()
            state.flags.add(loss)
            self.assertFalse(verify.sim_available(self.model, self.scene, state))
            state.flags.update([woman + ".trickster.returned", woman + ".closed"])
            self.assertFalse(verify.sim_available(self.model, self.scene, state))
            state.flags.remove(woman + ".closed")
            state.flags.remove(woman + ".present_now")
            state.flags.add(woman + ".returned_actor_lost")
            self.assertFalse(verify.sim_available(self.model, self.scene, state))

    def test_directed_enmity_keeps_matching_reconciliation_override(self):
        for woman, other in (("seelah", "camellia"), ("camellia", "seelah")):
            state = self.state()
            state.flags.add(woman + ".harem.enmity." + other)
            self.assertFalse(verify.sim_available(self.model, self.scene, state))
            state.flags.add(woman + ".harem.reconciled." + other)
            self.assertTrue(verify.sim_available(self.model, self.scene, state))

    def test_failed_copy_placement_never_supplies_a_returned_body(self):
        body_model = verify.Model(dict(Scenes=[], Derived={k: v for k, v in self.story["Derived"].items()
                                      if k.startswith(s04.P)},
                                      DerivedForbids={k: v for k, v in self.story["DerivedForbids"].items()
                                                      if k.startswith(s04.P)}))
        for woman, lost, returned in (("seelah", "seelah_gone", "seelah.trickster.returned"),
                                     ("camellia", "camellia.killed", "camellia.trickster.veiled_available")):
            state = verify.SimState(5, 1000)
            state.flags.update([woman + ".present_now", returned, lost])
            verify.sim_complete(body_model, state)
            self.assertIn(s04.P + woman + "_body", state.flags)
            state.flags.add(woman + ".presence.failed")
            verify.sim_complete(body_model, state)
            self.assertNotIn(s04.P + woman + "_body", state.flags)
            # An independently living native body can still attend.
            state.flags.remove(lost)
            verify.sim_complete(body_model, state)
            self.assertIn(s04.P + woman + "_body", state.flags)

    def test_unknown_crime_cannot_become_a_confession_or_resolution(self):
        state = self.state()
        state.flags.update(["camellia.mireya_unmasked", "trickster.wmt.available",
                            "camellia.trickster.returned"])
        choices = self.scene["Nodes"][0]["Choices"]
        self.assertEqual(len(choices), 5)
        self.assertEqual([i for i, c in enumerate(choices)
                          if verify.sim_choice_available(c, state)], [3, 4])
        producers = {flag for scene in self.story["Scenes"] for node in scene["Nodes"]
                     for choice in node["Choices"] for flag in choice["Set"]}
        self.assertFalse(set(s04.BLOCKERS) & producers)
        self.assertTrue(set(s04.BLOCKERS) <= set(self.story["PendingHooks"]))
        self.assertNotIn(s04.P + "retry", self.model.by_id)

    def test_abort_does_not_spend_and_refusal_exhausts_only_this_incident(self):
        state = self.state()
        abort = self.scene["Nodes"][0]["Choices"][4]
        self.assertTrue(abort["Abort"])
        self.assertFalse(abort["Set"])
        self.assertIsNone(abort["Next"])
        self.assertEqual(state.rest_spent, {})
        refusal = next(n for n in self.scene["Nodes"] if n["Id"] == "refused")["Choices"][0]
        self.assertEqual(set(refusal["Set"]), {s04.P + "settle.seen",
                                              s04.P + "permanent_refusal", s04.P + "unsettled",
                                              "seelah.harem.enmity.camellia",
                                              "seelah.harem.stance.tolerated"})
        state.flags.update(refusal["Set"])
        self.assertFalse(verify.sim_available(self.model, self.scene, state))
        self.assertFalse(any(f.endswith(".closed") for f in refusal["Set"]))
        state = self.state()
        state.rest_spent["household.protected"] = 2
        self.assertFalse(verify.sim_available(self.model, self.scene, state))

    def test_word_reservation_retains_use_limit_and_debt(self):
        choice = self.scene["Nodes"][0]["Choices"][2]
        self.assertIn("trickster.wmt.available", choice["Requires"])
        self.assertEqual(set(choice["Set"]), {"trickster.wmt.use.seelah_camellia",
                                             "household.wmt.debt.seelah_camellia"})
        self.assertIn(s04.BLOCKERS[2], choice["Requires"])
        self.assertEqual(self.story["ForesightConsumers"][self.scene["Id"]], "foresight.page_taken")

    def test_repeated_registration_never_duplicates_or_mutates_original_scenes(self):
        originals = []
        payload = dict(Scenes=list(originals))
        s04.register(payload, originals, {})
        once = copy.deepcopy(payload)
        s04.register(payload, originals, {})
        self.assertEqual(payload, once)
        self.assertEqual(originals, [])


if __name__ == "__main__":
    unittest.main()
