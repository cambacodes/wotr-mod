"""Route-local traversal checks for the R2 restoration/watch situations."""
import unittest

from storylines import terendelev_trickster as route, terendelev_watch as watch



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

class TerendelevRound2Tests(unittest.TestCase):
    def scene(self, scenes, name):
        return next(s for s in scenes if s["Id"] == route.P + name)

    def node(self, scene, name):
        return next(n for n in scene["Nodes"] if n["Id"] == name)

    def test_cut_traverses_slot_to_existing_dawn_on_both_hosts(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "night.watch" + suffix)
            slot = s["Id"] + ".explicit.1"
            self.assertEqual(by_contract(self.node(s, 'cut')['Choices'], [{'Next': 'terendelev.trickster.night.watch.explicit.1', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'terendelev.trickster.night.watch_awning.explicit.1', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"], slot)
            self.assertEqual(by_contract(self.node(s, slot)['Choices'], [{'Next': 'grey', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"], "grey")
            self.assertFalse(by_contract(self.node(s, slot)['Choices'], [{'Next': 'grey', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Set"])
            self.assertEqual(by_contract(self.node(s, 'end')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.night.seen'], 'Abort': False}])["Set"], [watch.NIGHT])
            # Choosing company does not complete the consummation or close the route.
            choice = by_contract(self.node(s, 'want')['Choices'], [{'Next': 'company', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])
            self.assertEqual(choice["Next"], "company")
            terminal = by_contract(self.node(s, 'company')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': True}])
            self.assertTrue(terminal["Abort"])
            self.assertFalse(terminal["Set"])

    def test_notice_keeps_personal_eligibility_without_an_escort(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "watch.deskari" + suffix)
            answers = self.node(s, "ask")["Choices"]
            self.assertEqual(by_contract(answers, [{'Next': 'vow', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.deskari_vow'], 'Abort': False}])["Next"], "vow")
            self.assertEqual(by_contract(answers, [{'Next': 'vow', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.deskari_vow'], 'Abort': False}])["Set"], [watch.DESKARI_VOW])
            self.assertEqual(by_contract(answers, [{'Next': 'notice', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.deskari_vow', 'terendelev.trickster.watch.deskari_notice'], 'Abort': False}])["Next"], "notice")
            self.assertEqual(by_contract(answers, [{'Next': 'notice', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.deskari_vow', 'terendelev.trickster.watch.deskari_notice'], 'Abort': False}])["Set"], [watch.DESKARI_VOW, route.DESKARI_NOTICE])
            release = self.scene(watch.SCENES, "watch.war_table" + suffix)
            for node in ("blood", "no"):
                self.assertIn(route.DESKARI_NOTICE, by_contract(self.node(release, node)['Choices'], [{'Next': 'departure', 'Requires': ['terendelev.trickster.watch.deskari_vow'], 'Forbids': ['terendelev.trickster.watch.deskari_notice', 'terendelev.trickster.watch.deskari_settled'], 'Set': [], 'Abort': False}])["Forbids"])
                self.assertIsNone(by_contract(self.node(release, node)['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"])
            self.assertEqual(by_contract(self.node(release, 'departure_stay')['Choices'], [{'Next': 'departure_end', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.deskari_settled'], 'Abort': False}])["Set"], [route.DESKARI_SETTLED])

    def test_known_hal_appends_destination_without_granting_an_arrival(self):
        for suffix in ("", "_awning"):
            s = self.scene(watch.SCENES, "watch.letter" + suffix)
            answers = self.node(s, "start")["Choices"]
            self.assertEqual(by_contract(answers, [{'Next': 'tell', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"], "tell")
            self.assertEqual(by_contract(answers, [{'Next': 'hal', 'Requires': ['terendelev.trickster.hal_met'], 'Forbids': [], 'Set': [], 'Abort': False}])["Requires"], [route.HAL_MET])
            self.assertEqual(by_contract(self.node(s, 'hal')['Choices'], [{'Next': 'tell', 'Requires': [], 'Forbids': [], 'Set': ['terendelev.trickster.watch.hal_refuge_delivery'], 'Abort': False}])["Set"], [route.HAL_LETTER])
            seal = self.node(s, "seal")["Choices"]
            self.assertIn(route.HAL_LETTER, by_contract(seal, [{'Next': 'pass', 'Requires': [], 'Forbids': ['terendelev.trickster.watch.hal_refuge_delivery'], 'Set': [], 'Abort': False}])["Forbids"])
            self.assertEqual(by_contract(seal, [{'Next': 'refuge', 'Requires': ['terendelev.trickster.watch.hal_refuge_delivery'], 'Forbids': [], 'Set': [], 'Abort': False}])["Requires"], [route.HAL_LETTER])
            self.assertFalse(by_contract(self.node(s, 'refuge')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Set"])
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
            self.assertIn(route.HAL_LETTER, by_contract(paragraphs, [{'Requires': ['terendelev.trickster.watch.letter_written'], 'Forbids': ['terendelev.trickster.watch.hal_refuge_delivery', 'terendelev.trickster.watch.hal_refuge_delivery', 'terendelev.trickster.watch.hal_refuge_delivery'], 'AnyGroups': []}, {'Requires': ['terendelev.trickster.watch.letter_written'], 'Forbids': ['terendelev.trickster.watch.hal_refuge_delivery'], 'AnyGroups': []}])["Forbids"])
            self.assertIn(route.DESKARI_SETTLED, by_contract(paragraphs, [{'Requires': ['terendelev.trickster.watch.deskari_vow', 'terendelev.trickster.watch.deskari_settled', 'terendelev.trickster.watch.deskari_settled', 'terendelev.trickster.watch.deskari_settled'], 'Forbids': ['terendelev.trickster.watch.deskari_notice', 'terendelev.trickster.watch.deskari_notice', 'terendelev.trickster.watch.deskari_notice'], 'AnyGroups': []}, {'Requires': ['terendelev.trickster.watch.deskari_vow', 'terendelev.trickster.watch.deskari_settled'], 'Forbids': ['terendelev.trickster.watch.deskari_notice'], 'AnyGroups': []}])["Requires"])
            known = [p for p in paragraphs if route.HAL_LETTER in p["Requires"]]
            self.assertIsNotNone(only(known))
            self.assertIn(watch.LETTER, by_contract(known, [{'Requires': ['terendelev.trickster.watch.letter_written', 'terendelev.trickster.watch.hal_refuge_delivery'], 'Forbids': [], 'AnyGroups': []}])["Requires"])
        # Late love retains the existing release/proof/personal gates.
        for arm in route.DERIVED[route.P + "late_committed"]:
            self.assertIn(watch.DEBT_FREE, arm)
            self.assertIn(watch.PROOF, arm)


if __name__ == "__main__":
    unittest.main()
