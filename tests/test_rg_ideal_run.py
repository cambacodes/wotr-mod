"""The ideal-run policy earns Dorgelinda's mending without bypassing her costs."""
import copy
import unittest

from tools import rrt_verify as rules, run_guide_check as guide


L = "dorgelinda.ledger."
COLD = {L + "quarrel_cold", L + "quarrel_unmended"}


class IdealRunMendingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = guide.model_from(guide.ROOT / "development/Story.json")
        cls.avoid = set((guide.KIT / "avoid.txt").read_text(encoding="utf-8").split())

    def play(self, sid, extra=(), avoid=None):
        state = rules.SimState(5, 100)
        state.flags.update(("trickster.ever", "dorgelinda.committed",
                            "dorgelinda.trickster.methods_heard", *extra))
        state.crusade_resources = {"Materials": 1000, "Finances": 1000, "Favors": 1000}
        policy = {"committed": {"dorgelinda.committed"},
                  "closed": {"dorgelinda.closed"} | (self.avoid if avoid is None else avoid)}
        scene = self.model.by_id[sid]
        self.assertTrue(rules.sim_play(self.model, scene, state, policy))
        rules.sim_complete(self.model, state)
        return state

    def test_cold_counts_sibling_apologizes_and_restores_current_commitment(self):
        state = self.play(L + "cold_counts", (L + "quarrel_cold", L + "allotment_lost"))
        self.assertIn(L + "quarrel_mended", state.flags)
        self.assertNotIn(L + "quarrel_unmended", state.flags)
        self.assertNotIn(L + "cold_unmended", state.flags)
        self.assertEqual(state.crusade_resources["Materials"], 1050)
        self.assertIn("dorgelinda.trickster.late_committed", state.flags)

class IdealRunLastCallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = guide.model_from(guide.ROOT / "development/Story.json")
        cls.trace = guide.run_kit()
        cls.text = guide.GUIDE.read_text(encoding="utf-8")

    def test_executed_campaign_mends_and_keeps_dorgelinda_at_last_call(self):
        final = set(self.trace["final_flags"])
        self.assertTrue({L + "quarrel_mended", "dorgelinda.trickster.late_committed",
                         "dorgelinda.harem.eligible"} <= final)
        self.assertFalse((COLD | {L + "cold_unmended"}) & final)
        self.assertTrue(any(e["id"] == "dorgelinda.lastcall.call" for e in self.trace["log"]))
        guide.validate(self.text, self.model, self.trace, guide.manifest())

    def test_guide_still_rejects_loss_after_historical_commitment(self):
        trace = copy.deepcopy(self.trace)
        trace["final_flags"].remove("dorgelinda.harem.eligible")
        with self.assertRaisesRegex(ValueError, "no longer eligible/present at Last Call: dorgelinda"):
            guide.validate(self.text, self.model, trace, guide.manifest())


if __name__ == "__main__":
    unittest.main()
