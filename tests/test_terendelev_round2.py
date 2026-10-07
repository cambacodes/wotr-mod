"""Route-local traversal checks for the R2 restoration/watch situations."""
import unittest

from storylines import terendelev_trickster as route, terendelev_watch as watch


class TerendelevRound2Tests(unittest.TestCase):
    def scene(self, scenes, name):
        return next(s for s in scenes if s["Id"] == route.P + name)

    def node(self, scene, name):
        return next(n for n in scene["Nodes"] if n["Id"] == name)

    def test_cut_traverses_slot_to_existing_dawn_on_both_hosts(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "night.watch" + suffix)
            slot = s["Id"] + ".explicit.1"
            self.assertEqual(self.node(s, "cut")["Choices"][0]["Next"], slot)
            self.assertEqual(self.node(s, slot)["Choices"][0]["Next"], "grey")
            self.assertFalse(self.node(s, slot)["Choices"][0]["Set"])
            self.assertEqual(self.node(s, "end")["Choices"][0]["Set"], [watch.NIGHT])
            # Choosing company does not complete the consummation or close the route.
            choice = self.node(s, "want")["Choices"][-1]
            self.assertEqual(choice["Next"], "company")
            terminal = self.node(s, "company")["Choices"][0]
            self.assertTrue(terminal["Abort"])
            self.assertFalse(terminal["Set"])

    def test_notice_keeps_personal_eligibility_without_an_escort(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "watch.deskari" + suffix)
            answers = self.node(s, "ask")["Choices"]
            self.assertEqual(answers[0]["Next"], "vow")
            self.assertEqual(answers[0]["Set"], [watch.DESKARI_VOW])
            self.assertEqual(answers[2]["Next"], "notice")
            self.assertEqual(answers[2]["Set"], [watch.DESKARI_VOW, route.DESKARI_NOTICE])
            release = self.scene(watch.SCENES, "watch.war_table" + suffix)
            for node in ("blood", "no"):
                self.assertIn(route.DESKARI_NOTICE, self.node(release, node)["Choices"][-1]["Forbids"])
                self.assertIsNone(self.node(release, node)["Choices"][0]["Next"])
            self.assertEqual(self.node(release, "departure_stay")["Choices"][0]["Set"], [route.DESKARI_SETTLED])

    def test_known_hal_appends_destination_without_granting_an_arrival(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "watch.letter" + suffix)
            answers = self.node(s, "start")["Choices"]
            self.assertEqual(answers[0]["Next"], "tell")
            self.assertEqual(answers[-1]["Requires"], [route.HAL_MET])
            self.assertEqual(self.node(s, "hal")["Choices"][0]["Set"], [route.HAL_LETTER])
            seal = self.node(s, "seal")["Choices"]
            self.assertIn(route.HAL_LETTER, seal[0]["Forbids"])
            self.assertEqual(seal[-1]["Requires"], [route.HAL_LETTER])
            self.assertFalse(self.node(s, "refuge")["Choices"][0]["Set"])
        self.assertEqual(route.BINDINGS["SeenCues"][route.HAL_MET], ["195ef1a822c1c144f80f3cd6d5669d63"])

    def test_reactors_use_existing_earned_return_receipts(self):
        for scenes, name, actor in ((route.SCENES, "react.seelah.watch", "seelah"),
                                    (watch.SCENES, "react.seelah.alive", "seelah"),
                                    (route.SCENES, "react.anevia.kenabres", "anevia")):
            s = self.scene(scenes, name)
            for loss in (actor + "_dead", actor + "_gone"):
                self.assertIn(loss, s["Forbids"])
                self.assertEqual(s["ForbidOverrides"][loss], actor + ".trickster.returned")

    def test_late_return_starts_after_completed_iz_in_drezen(self):
        s = self.scene(route.SCENES, "late.the_wound_calls")
        self.assertIn("iz.done", s["Requires"])
        self.assertEqual(s["Areas"], [route.DREZEN])
        self.assertEqual(s["DelayHours"], 24)
        self.assertIn(route.RETURNED, s["Forbids"])
        self.assertIn(route.CLOSED, s["Forbids"])

    def test_earned_ending_callbacks_distinguish_delivery_and_settled_vow(self):
        for name in ("watch", "late", "debt", "guardian"):
            s = self.scene(route.SCENES, "epilogue." + name)
            paragraphs = self.node(s, "page")["Paragraphs"]
            self.assertIn(route.HAL_LETTER, paragraphs[9]["Forbids"])
            self.assertIn(route.DESKARI_SETTLED, paragraphs[24]["Requires"])
            known = [p for p in paragraphs if route.HAL_LETTER in p["Requires"]]
            self.assertEqual(len(known), 1)
            self.assertIn(watch.LETTER, known[0]["Requires"])
        # Late love retains the existing release/proof/personal gates.
        for arm in route.DERIVED[route.P + "late_committed"]:
            self.assertIn(watch.DEBT_FREE, arm)
            self.assertIn(watch.PROOF, arm)


if __name__ == "__main__":
    unittest.main()
