"""Seelah's situation continuity and current Last Call custody contract."""
import unittest

from tests.test_seelah_round2 import Walk, route_story
from storylines import lastcall, lastcall_partners as partners, seelah_round2 as r


class SeelahRound3Tests(unittest.TestCase):
    def test_suppers_do_not_share_mutable_pages(self):
        story = route_story()
        by = {s["Id"]: s for s in story["Scenes"]}
        promise = r.node(by["seelah.promise"], "supper")
        kept = r.node(by["seelah.kept"], "supper")
        self.assertIsNot(promise, kept)
        self.assertNotIn("The whole evening", promise["Text"])
        self.assertIn("The whole evening", kept["Text"])
        promise["Choices"][0]["Text"] = "changed in the interrupted situation"
        self.assertNotEqual(promise["Choices"][0]["Text"], kept["Choices"][0]["Text"])

    def test_closure_uses_the_actual_posting_history(self):
        story = route_story()
        by = {s["Id"]: s for s in story["Scenes"]}
        paragraphs = r.node(by[r.PREFIX + "epilogue.pickpocket"], "end")["Paragraphs"]
        outside = next(p for p in paragraphs if "left for her posting with her papers" in p["Text"])
        companion = next(p for p in paragraphs if "kept her place among the companions" in p["Text"])
        for posted in (False, True):
            flags = ["seelah.closed"] + ([r.PREFIX + "stay_decided"] if posted else [])
            w = Walk(story, flags)
            self.assertEqual(posted, w.available(outside))
            self.assertEqual(not posted, w.available(companion))

    def test_every_settlement_withholds_the_list_call(self):
        # Use the current shared producers and the actual call scene. Do not
        # restore the superseded thief's-promise/anonymous-coin implementation.
        derived = partners.derived()
        forbids = partners.derived_forbids()
        account = "seelah.lastcall.account_due"
        groups, _, exclusions = partners.call_guards()[account]
        derived[account] = groups
        forbids[account] = exclusions
        story = {"Derived": derived, "DerivedForbids": forbids}
        call = next(s for s in partners.call_in_scenes(lastcall.at_the_rift_scene)
                    if s["Id"] == "seelah.lastcall.call")
        earned = ["trickster", "trickster.ever", "trickster.lastcall.open",
                  "seelah.lastcall.callable", r.HOLDS, r.KEEPS]
        self.assertTrue(Walk(story, earned).available(call))
        for receipt in (r.GIVEN, r.ROBBED, r.SETTLED, "seelah.lastcall.list_returned"):
            with self.subTest(receipt=receipt):
                self.assertFalse(Walk(story, earned + [receipt]).available(call))
        self.assertFalse(Walk(story, earned[:-2]).available(call))

    def test_epilogue_reclaims_only_an_outstanding_list_and_game_is_earned(self):
        story = route_story()
        ending = next(s for s in story["Scenes"] if s["Id"] == r.PREFIX + "epilogue.pickpocket")
        paragraphs = r.node(ending, "end")["Paragraphs"]
        reclaim = next(p for p in paragraphs if "Seelah recovered her list" in p["Text"])
        game = next(p for p in paragraphs if "game belonged to them both" in p["Text"])
        for receipt in (None, r.GIVEN, r.ROBBED, r.SETTLED, "seelah.lastcall.list_returned"):
            flags = [r.HOLDS, r.KEEPS] + ([receipt] if receipt else [])
            with self.subTest(receipt=receipt):
                self.assertEqual(receipt is None, Walk(story, flags).available(reclaim))
        self.assertFalse(Walk(story, [r.ROBBED]).available(game))
        self.assertTrue(Walk(story, [r.ROBBED, r.GAME]).available(game))
        self.assertFalse(any("never stopped trying" in p["Text"] for p in paragraphs))

    def test_paid_receipt_preserves_the_visit_twins_later_yes(self):
        story = route_story()
        by = {s["Id"]: s for s in story["Scenes"]}
        flags = ["trickster.ever", r.PREFIX + "returned", r.PREFIX + "declined",
                 r.COIN_NO, r.HOLDS, r.GIVEN, "seelah.kissed", "seelah.presence.failed"]
        w = Walk(story, flags)
        paid = by[r.PREFIX + "dismissed.second_ask_paid"]
        w.take(paid, "start", 0)
        w.take(paid, "yes", 0)
        self.assertIn(r.COIN_PAID, w.flags)
        self.assertNotIn("seelah.committed", w.flags)
        visit = by[r.PREFIX + "dismissed.second_ask_visit"]
        self.assertTrue(w.available(visit))
        self.assertEqual("offer", w.take(visit, "coin_answer", 0))
        self.assertTrue(w.available(r.node(visit, "offer")["Choices"][0]))
        w.take(visit, "offer", 0)
        self.assertIn("seelah.committed", w.flags)
        self.assertIn(r.PREFIX + "reconciled", w.flags)


if __name__ == "__main__":
    unittest.main()
