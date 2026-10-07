"""Replay immediate truth and postponement through the existing hunt and endings."""
import unittest

from tests.story_fixture import fresh_story
from tests.test_DelamerePolish import P, matches, play
from tools.rrt_verify import Model, SimState, sim_complete


class DelamereRound4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = Model(fresh_story())
        cls.scenes = cls.model.by_id
        play.model = cls.model

    def ending_flags(self, flags):
        state = SimState(6, 5000)
        state.flags.update(flags)
        sim_complete(self.model, state)
        return state.flags

    def test_chapel_confession_and_postponement_reach_existing_outcomes(self):
        chapel = self.scenes[P + "woken.old_deadeye"]
        nodes = {n["Id"]: n for n in chapel["Nodes"]}
        self.assertEqual(nodes["not_like"]["Choices"][0]["Next"], "haddo_end")
        self.assertEqual(len(nodes["not_like"]["Choices"]), 2)
        for immediate in (False, True):
            flags, seen = play(chapel, {"trickster.ever", P + "returned", P + "lied_erastil"},
                               choices={"lied": 1, "not_like": int(immediate)})
            self.assertEqual("confessed_here" in seen, immediate)
            self.assertEqual(P + "confessed" in flags, immediate)
            self.assertIn(P + "old_deadeye", flags)
            self.assertNotIn("delamere.closed", flags)
            for suffix in ("woods.second_hunt", "woods.second_hunt_page",
                           "woods.second_hunt_late"):
                with self.subTest(immediate=immediate, hunt=suffix):
                    got, visited = play(self.scenes[P + suffix],
                                        flags | {P + "second_hunt_offered"})
                    self.assertEqual("chapel_oath" in visited, not immediate)
                    self.assertEqual("confess" in visited, not immediate)
                    self.assertIn(P + "confessed", got)
                    self.assertIn("delamere.committed", got)
                    self.assertNotIn("delamere.closed", got)
                    got = self.ending_flags(got)
                    self.assertTrue(matches(self.scenes[P + "epilogue.caught"], got))
                    self.assertFalse(matches(self.scenes[P + "epilogue.apart"], got))
                    self.assertFalse(matches(self.scenes[P + "epilogue.sacrifice"], got))
                    sacrificed = got | {"sacrifice"}
                    self.assertFalse(matches(self.scenes[P + "epilogue.caught"], sacrificed))
                    self.assertTrue(matches(self.scenes[P + "epilogue.sacrifice"], sacrificed))
            got, visited = play(self.scenes[P + "woods.second_hunt"],
                                flags | {P + "second_hunt_offered"},
                                choices={"choice": 2})
            self.assertIn("delamere.closed", got)
            self.assertNotIn("delamere.committed", got)
            got = self.ending_flags(got)
            self.assertFalse(matches(self.scenes[P + "epilogue.caught"], got))
            self.assertTrue(matches(self.scenes[P + "epilogue.apart"], got))


if __name__ == "__main__":
    unittest.main()
