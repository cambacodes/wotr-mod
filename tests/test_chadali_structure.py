"""Chadali ending and account behavior through the assembled story."""
import copy
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools import prose_pending_lint, rrt_verify as verify


class ChadaliStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {scene["Id"]: scene for scene in cls.story["Scenes"]}
        cls.model = verify.Model(copy.deepcopy(cls.story))

    def test_fair_variants_follow_the_world_and_earned_history(self):
        paragraphs = self.by["chadali.trickster.epilogue.lucky_night"]["Nodes"][0]["Paragraphs"]
        closed, unresolved = paragraphs[18], paragraphs[56]
        for earned in (False, True):
            for wound_closed in (False, True):
                for convened in (False, True):
                    with self.subTest(earned=earned, closed=wound_closed, convened=convened):
                        state = verify.SimState(6, 0)
                        if earned:
                            state.flags.add("chadali.fortunes.saw_the_fair_plainly")
                        if wound_closed:
                            state.flags.add("ending.wound_closed")
                        if convened:
                            state.flags.add("council.epilogue_convened")
                        self.assertEqual(earned and wound_closed,
                                         verify.sim_choice_available(closed, state))
                        self.assertEqual(earned and convened and not wound_closed,
                                         verify.sim_choice_available(unresolved, state))

    def test_unresolved_placeholder_has_an_exact_registration(self):
        root = Path(__file__).resolve().parents[1]
        registry = json.loads((root / "tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        self.assertEqual([], prose_pending_lint.check(self.story, registry, integration=True))

    def test_lost_wager_does_not_discharge_either_old_loan(self):
        choice = self.by["chadali.lastcall.call"]["Nodes"][0]["Choices"][0]
        for old_loan in ("luck_lent", "luck_owed"):
            for lost_wager in (False, True):
                for repaid in (False, True):
                    with self.subTest(loan=old_loan, lost=lost_wager, repaid=repaid):
                        state = verify.SimState(5, 0)
                        state.flags.add("chadali.trickster.cost." + old_loan)
                        if lost_wager:
                            state.flags.add("chadali.wagers.luck_lost")
                        if repaid:
                            state.flags.add("chadali.fortunes.loan_returned")
                        verify.sim_complete(self.model, state)
                        self.assertEqual(not repaid, "chadali.lastcall.luck_due" in state.flags)
                        self.assertEqual(not repaid, verify.sim_choice_available(choice, state))

    def test_lost_wager_alone_creates_no_old_loan(self):
        state = verify.SimState(5, 0)
        state.flags.add("chadali.wagers.luck_lost")
        verify.sim_complete(self.model, state)
        self.assertNotIn("chadali.lastcall.luck_due", state.flags)


if __name__ == "__main__":
    unittest.main()
