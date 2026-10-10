"""Seelah's situation continuity and current Last Call custody contract."""
import unittest

from tests.test_seelah_round2 import Walk, route_story
from storylines import lastcall, lastcall_partners as partners, seelah_round2 as r


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class SeelahRound3Tests(unittest.TestCase):
    def test_suppers_do_not_share_mutable_pages(self):
        story = route_story()
        by = {s["Id"]: s for s in story["Scenes"]}
        promise = r.node(by["seelah.promise"], "supper")
        kept = r.node(by["seelah.kept"], "supper")
        self.assertIsNot(promise, kept)
        previous = [list(a["Set"]) for a in kept["Choices"]]
        for answer in promise["Choices"]:
            answer["Set"].append("fixture.interrupted")
        self.assertEqual([a["Set"] for a in kept["Choices"]], previous)


    def test_closure_uses_the_actual_posting_history(self):
        story = route_story()
        by = {s["Id"]: s for s in story["Scenes"]}
        paragraphs = r.node(by[r.PREFIX + "epilogue.pickpocket"], "end")["Paragraphs"]
        outside = next(p for p in paragraphs if r.PREFIX + "stay_decided" in p["Requires"])
        companion = next(p for p in paragraphs if "seelah.closed" in p["Requires"] and r.PREFIX + "stay_decided" in p["Forbids"])
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
        reclaim = next(p for p in paragraphs if r.HOLDS in p["Requires"] and r.ROBBED in p["Forbids"])
        game = next(p for p in paragraphs if r.GAME in p["Requires"])
        for receipt in (None, r.GIVEN, r.ROBBED, r.SETTLED, "seelah.lastcall.list_returned"):
            flags = [r.HOLDS, r.KEEPS] + ([receipt] if receipt else [])
            with self.subTest(receipt=receipt):
                self.assertEqual(receipt is None, Walk(story, flags).available(reclaim))
        self.assertFalse(Walk(story, [r.ROBBED]).available(game))
        self.assertTrue(Walk(story, [r.ROBBED, r.GAME]).available(game))

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
        self.assertTrue(w.available(next(a for a in r.node(visit, "offer")["Choices"] if "seelah.committed" in a["Set"])))
        w.take(visit, "offer", 0)
        self.assertIn("seelah.committed", w.flags)
        self.assertIn(r.PREFIX + "reconciled", w.flags)


if __name__ == "__main__":
    unittest.main()
