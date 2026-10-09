"""Current Dorgelinda commitment follows the unresolved-quarrel outcome."""
import unittest

from storylines import dorgelinda_trickster as trickster, household
from tools import rrt_verify as rules

L = "dorgelinda.ledger."
READERS = ("dorgelinda.harem.eligible", "dorgelinda.outcome.accepted",
           "dorgelinda.trickster.late_committed")


class DorgelindaCommitmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use the real route registration and household derivation with unrelated routes inert.
        cls.story = {"Scenes": [], "Relationships": {
            rel: {"StartedFlag": rel + ".started", "ClosedFlag": rel + ".closed",
                  "CommittedFlag": rel + ".committed", "UnavailableFlags": []}
            for rel in household.PARTNERS}}
        trickster.integrate(cls.story)
        cls.story["Derived"].update(household.derived(cls.story))
        cls.story["DerivedOpenRoutes"] = household.open_routes(cls.story)
        cls.model = rules.Model(cls.story)

    def complete(self, extra=()):
        state = rules.SimState(5, 100)
        state.flags.update(("trickster.ever", "dorgelinda.committed",
                            "dorgelinda.trickster.methods_heard"))
        state.flags.update(extra)
        rules.sim_complete(self.model, state)
        return state

    def test_unresolved_quarrel_withholds_current_commitment(self):
        for extra in ((L + "quarrel_cold",), (L + "quarrel_unmended",),
                      (L + "quarrel_cold", L + "quarrel_unmended"),
                      (L + "quarrel_mended", L + "quarrel_unmended"),
                      (L + "quarrel_cold", L + "quarrel_mended", L + "quarrel_unmended")):
            with self.subTest(extra=extra):
                state = self.complete(extra)
                self.assertFalse(set(READERS) & state.flags)
                self.assertIn("dorgelinda.committed", state.flags)

    def test_mended_and_undamaged_commitments_remain_current(self):
        for extra in ((), (L + "quarrel_mended",),
                      (L + "quarrel_cold", L + "quarrel_mended"),
                      (L + "narrowed",), (L + "unblessed",)):
            with self.subTest(extra=extra):
                self.assertTrue(set(READERS) <= self.complete(extra).flags)

    def test_recomputing_old_save_readers_then_mending_restores_eligibility(self):
        state = self.complete()
        state.flags.add(L + "quarrel_cold")
        rules.sim_complete(self.model, state)
        self.assertFalse(set(READERS) & state.flags)
        state.flags.add(L + "quarrel_mended")
        rules.sim_complete(self.model, state)
        self.assertTrue(set(READERS) <= state.flags)

    def test_professional_progress_does_not_earn_commitment(self):
        state = rules.SimState(5, 100)
        state.flags.update(("trickster.ever", "dorgelinda.trickster.methods_heard"))
        rules.sim_complete(self.model, state)
        self.assertFalse(set(READERS) & state.flags)

    def test_route_closure_still_withholds_household_eligibility(self):
        self.assertNotIn(READERS[0], self.complete(("dorgelinda.closed",)).flags)

    def test_world_fallback_matches_the_route_commitment_reader(self):
        from storylines import dorgelinda_trickster, trickster_world
        self.assertEqual(dorgelinda_trickster.DERIVED[READERS[2]],
                         trickster_world.DERIVED[READERS[2]])
