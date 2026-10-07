"""R4 D09-D12: refusal direction and earned invitation callbacks."""
import unittest

from test_seelah_round2 import Walk, route_story
from storylines import seelah_round2 as r


class SeelahRound4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = route_story()
        # The route fixture omits expansion's shared current-path definition.
        cls.story["Derived"]["trickster.now"] = [["trickster"]]
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}

    def reclaim(self, walk, suffix):
        scene = self.by[r.PREFIX + suffix + ".list_reclaimed"]
        self.assertTrue(walk.available(scene))
        answers = r.node(scene, "start")["Choices"]
        invitations = [i for i in range(1, len(answers)) if walk.available(answers[i])]
        self.assertEqual(1, len(invitations))
        dest = walk.take(scene, "start", invitations[0])
        self.assertTrue(walk.has(r.CUSTODY))
        self.assertNotIn("seelah.committed", walk.flags)
        return scene, dest

    def successful_lift(self, walk, scene):
        # Play the untaught lift and resolve its actual success destination.
        # Timing/native adapter observations are covered by the C# suites.
        walk.take(scene, "stall", 1)
        dest = r.node(scene, "stall")["Choices"][1]["Check"]["Success"]
        self.assertEqual("lifted", dest)
        return walk.take(scene, dest, 0)

    def test_retained_body_return_before_any_courtship_gets_first_invitation(self):
        w = Walk(self.story, ["trickster.ever", "trickster", "seelah.diamond_held",
                              "seelah_dead", "seelah.dead.latched", "revive.seelah.available"])
        # Pay the existing resurrection, wake her, and keep the list. Neither
        # returning her body nor keeping her property invents a romantic past.
        pick = self.by[r.PREFIX + "dead.pickpocket"]
        self.assertTrue(w.available(pick))
        w.take(pick, "bier", 1)
        w.take(pick, "fumble", 0)
        w.take(pick, "coin", 0)
        self.assertEqual("pocketed", self.successful_lift(w, pick))
        w.take(pick, "pocketed", 0)
        # Observe the native body alive after the Revive action.
        w.flags.discard("seelah_dead")
        wakes = self.by[r.PREFIX + "dead.wakes"]
        self.assertTrue(w.available(wakes))
        w.take(wakes, "start", 0)
        w.take(wakes, "coin", 1)
        w.take(wakes, "kept", 0)
        scene, dest = self.reclaim(w, "dead")
        self.assertEqual("offer_first", dest)
        text = r.node(scene, dest)["Text"]
        self.assertIn("An evening with you?", text)
        self.assertNotIn("another evening", text)
        self.assertNotIn("I still do", text)
        w.take(scene, dest, 0)
        self.assertIn(r.GAME, w.flags)
        self.assertFalse(w.has("seelah.romance"))

    def test_fresh_courier_return_reclaims_before_courtship(self):
        w = Walk(self.story, ["trickster.ever", "trickster", "seelah.diamond_held",
                              "seelah_dead", "seelah.dead.latched"])
        effects = self.by[r.PREFIX + "dead.pickpocket_effects"]
        self.assertTrue(w.available(effects))
        w.take(effects, "start", 0)
        w.take(effects, "purse", 0)
        self.assertEqual("rider", self.successful_lift(w, effects))
        w.take(effects, "rider", 0)
        self.assertNotIn("seelah.diamond_held", w.flags)
        reply = self.by[r.PREFIX + "dead.effects_reply"]
        self.assertTrue(w.available(reply))
        w.take(reply, "start", 0)
        w.take(reply, "note", 0)
        arrival = self.by[r.PREFIX + "dead.effects_arrival"]
        self.assertTrue(w.available(arrival))
        w.take(arrival, "start", 0)
        scene, dest = self.reclaim(w, "after")
        self.assertEqual("offer_first", dest)
        self.assertNotIn("another evening", r.node(scene, dest)["Text"])
        w.take(scene, dest, 1)
        self.assertNotIn(r.GAME, w.flags)
        self.assertFalse(w.has("seelah.romance"))
        self.assertNotIn(r.PREFIX + "courted", w.flags)

    def test_existing_courtship_gets_only_the_repeat_invitation_in_both_twins(self):
        # COURTED also records the played market evening without a kiss.
        for suffix in ("dead", "after"):
            for history in (["seelah.kissed"], [r.PREFIX + "courted"],
                            [r.PREFIX + "courted", r.PREFIX + "tavern_kissed"]):
                with self.subTest(suffix=suffix, history=history):
                    flags = ["trickster.ever", r.PREFIX + "returned", r.HOLDS] + history
                    if suffix == "dead":
                        flags += ["seelah.revived", r.PREFIX + "woke", r.KEEPS]
                    w = Walk(self.story, flags)
                    scene, dest = self.reclaim(w, suffix)
                    self.assertEqual("offer", dest)
                    self.assertIn("another evening", r.node(scene, dest)["Text"])
                    w.take(scene, dest, 1)
                    self.assertNotIn(r.GAME, w.flags)

    def test_each_returned_refusal_preserves_her_no_and_the_existing_retry(self):
        for suffix in ("commit", "commit_visit"):
            for nid, receipt in (("no", r.FREEDOM_NO), ("no_death", r.LIST_NO),
                                 ("no_stones", r.COIN_NO)):
                with self.subTest(suffix=suffix, refusal=nid):
                    w = Walk(self.story, ["trickster.ever", r.PREFIX + "returned", "seelah.kissed"])
                    if suffix.endswith("_visit"):
                        w.flags.add("seelah.presence.failed")
                    w.take(self.by[r.PREFIX + "dismissed." + suffix], nid, 0)
                    self.assertIn(receipt, w.flags)
                    self.assertIn(r.PREFIX + "declined", w.flags)
                    ending = self.by[r.PREFIX + "epilogue.refused"]
                    self.assertTrue(w.available(ending))
                    page = r.node(ending, "end")
                    self.assertIn("Seelah had refused the Commander's request", page["Text"])
                    romantic = page["Paragraphs"][0]
                    self.assertTrue(w.available(romantic))
                    self.assertIn("She had not taken back her no", romantic["Text"])
                    self.assertIn("what to put right before asking again", romantic["Text"])
                    self.assertFalse(w.available(page["Paragraphs"][1]))
                    retry = self.by[r.PREFIX + "dismissed.second_ask" +
                                    ("_visit" if suffix.endswith("_visit") else "")]
                    self.assertEqual(receipt != r.COIN_NO, w.available(retry))
                    w.flags.add("seelah.committed")
                    self.assertFalse(w.available(ending))

    def test_let_her_go_does_not_supply_a_return_or_a_romantic_callback(self):
        w = Walk(self.story, ["trickster", "trickster.ever"])
        w.take(self.by[r.PREFIX + "dismissed.late"], "start", 2)
        self.assertNotIn(r.PREFIX + "returned", w.flags)
        page = r.node(self.by[r.PREFIX + "epilogue.refused"], "end")
        self.assertFalse(w.available(page["Paragraphs"][0]))
        self.assertTrue(w.available(page["Paragraphs"][1]))


if __name__ == "__main__":
    unittest.main()
