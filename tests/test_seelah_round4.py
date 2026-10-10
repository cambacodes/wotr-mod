"""R4 D09-D12: refusal direction and earned invitation callbacks."""
import unittest

from tests.test_seelah_round2 import Walk, route_story
from storylines import seelah_round2 as r
from tools.savecompat import choice_identities


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


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
        invitations = [ref["GuidFor"].removeprefix(f"answer.{scene['Id']}.start.")
                       for answer, ref in zip(answers, choice_identities(scene, r.node(scene, "start")))
                       if ref["GuidFor"] != f"answer.{scene['Id']}.start.0" and walk.available(answer)]
        dest = walk.take(scene, "start", only(invitations))
        self.assertTrue(walk.has(r.CUSTODY))
        self.assertNotIn("seelah.committed", walk.flags)
        return scene, dest

    def successful_lift(self, walk, scene):
        # Play the untaught lift and resolve its actual success destination.
        # Timing/native adapter observations are covered by the C# suites.
        walk.take(scene, "stall", 1)
        dest = next(a for a in r.node(scene, "stall")["Choices"] if a.get("Check", {}).get("Skill") == "SkillThievery")["Check"]["Success"]
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
                    w.take(scene, dest, 1)
                    self.assertNotIn(r.GAME, w.flags)

    def test_let_her_go_does_not_supply_a_return_or_a_romantic_callback(self):
        w = Walk(self.story, ["trickster", "trickster.ever"])
        w.take(self.by[r.PREFIX + "dismissed.late"], "start", 2)
        self.assertNotIn(r.PREFIX + "returned", w.flags)
        page = r.node(self.by[r.PREFIX + "epilogue.refused"], "end")
        self.assertFalse(w.available(next(p for p in page["Paragraphs"] if r.PREFIX + "returned" in p["Requires"])))
        self.assertTrue(w.available(next(p for p in page["Paragraphs"] if r.PREFIX + "returned" in p["Forbids"])))


if __name__ == "__main__":
    unittest.main()
