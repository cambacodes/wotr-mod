"""Interaction attendance and crown-history regressions for phase 4 ix-a."""
import unittest

from storylines import character_interactions_ix_a as interactions
from storylines import galfrey_trickster as gf
from tests.story_fixture import fresh_story
from tools import gate_lint, player_text_lint
from tools.crossroute_checks.common import AND, NOT, Proof, fields, lit, verify


class InteractionAttendanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.proof = Proof(verify.Model(cls.story))

    def test_departure_epochs_block_every_live_participant(self):
        for authored in interactions.SCENES:
            scene = self.scenes[authored["Id"]]
            for gate in scene["Requires"]:
                if gate.endswith((".present_now", ".reachable_by_letter")):
                    woman = gate.split(".")[0]
                    with self.subTest(scene=scene["Id"], woman=woman):
                        self.assertTrue(self.proof.implies(
                            lit(gate), lit(woman + ".epoch_unavailable", False)))

    def test_banner_is_earned_and_never_a_divine_body(self):
        for authored in interactions.SCENES:
            scene = self.scenes[authored["Id"]]
            if scene["Owner"] == "Iomedae":
                self.assertIn("iomedae.trickster.first_spoken", scene["Requires"])
                self.assertIn("iomedae.trickster.disputation.called", scene["Requires"])
                self.assertEqual(["iomedae.banner_in_hand",
                                  "iomedae.trickster.order_banner"],
                                 scene["RequiresAny"])
                self.assertIn("iomedae.reachable_by_letter", scene["Requires"])
                self.assertNotIn("iomedae.present_now", scene["Requires"])
            self.assertTrue(scene["Reaction"])
            self.assertEqual(scene["Owner"].lower(), scene["Relationship"])
            self.assertIn("trickster", scene["Requires"])
            self.assertEqual([5], scene["Chapters"])
            self.assertEqual(1, len(scene["Nodes"]))

    def test_queen_and_knight_variants_do_not_overlap(self):
        for owner in ("iomedae", "yaniel"):
            variants = [s for s in interactions.SCENES
                        if s["Id"].startswith(owner + ".") and ".galfrey." in s["Id"]]
            for history, expected in (({gf.FINAL}, "queen"),
                                      ({gf.FINAL, gf.RETURNED, gf.CROWN}, "crown"),
                                      ({gf.FINAL, gf.RETURNED, gf.FOREVER}, "kitrane")):
                got = []
                for scene in variants:
                    # Supply shared attendance/channel conditions, varying only
                    # the Queen's native/returned/chosen-crown history.
                    flags = history | (set(scene["Requires"]) -
                                       {gf.FINAL, gf.RETURNED, gf.CROWN, gf.FOREVER})
                    if set(scene["Requires"]) <= flags and not set(scene["Forbids"]) & flags:
                        got.append(scene["Id"].rsplit(".", 1)[-1])
                self.assertEqual([expected], got, (owner, history))

    def test_either_earned_banner_suffices_but_neither_blocks(self):
        for scene in interactions.SCENES:
            if scene["Owner"] != "Iomedae":
                continue
            context = fields({"Requires": scene["Requires"], "Forbids": scene["Forbids"]})
            first, second = scene["RequiresAny"]
            for held, absent in ((first, second), (second, first)):
                self.assertTrue(self.proof.implies(
                    AND(context, lit(held), lit(absent, False)), fields(scene)))
            self.assertTrue(self.proof.implies(
                AND(context, lit(first, False), lit(second, False)), NOT(fields(scene))))

    def test_every_dialogue_turn_is_attributed_and_gates_are_normalized(self):
        story = {"Scenes": interactions.SCENES}
        self.assertEqual([], player_text_lint.check(story)["review"])
        self.assertTrue(all(not rows for rows in gate_lint.check(story, legacy=set()).values()))


if __name__ == "__main__":
    unittest.main()
