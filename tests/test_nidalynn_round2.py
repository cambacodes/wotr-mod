"""Round-two histories: care, witnesses, consent, and separate ending answers."""
import itertools
import unittest

from storylines import nidalynn_kiln as kiln, nidalynn_salt as salt
from storylines import nidalynn_trickster as route


def nodes(module, suffix):
    scene = next(s for s in module.SCENES if s["Id"] == route.P + suffix)
    return {n["Id"]: n for n in scene["Nodes"]}


def selectable(node, flags):
    return [c for c in node["Choices"]
            if set(c["Requires"]) <= flags and not set(c["Forbids"]) & flags]


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NidalynnRoundTwoTests(unittest.TestCase):
    def test_every_witness_history_has_one_continuation_and_keeps_testimony(self):
        hatching = nodes(kiln, "kiln.hatching")
        reckoning = nodes(kiln, "kiln.truth_owed")
        for clerk, quartermaster in itertools.product((False, True), repeat=2):
            flags = {f for f, held in ((route.CLERK, clerk),
                                      (route.QUARTERMASTER, quartermaster)) if held}
            with self.subTest(clerk=clerk, quartermaster=quartermaster):
                start = selectable(hatching["lied"], flags)
                later = selectable(reckoning["kiln"], flags)
                suffix = "clerk" if clerk else "quartermaster" if quartermaster else None
                self.assertEqual(only(start)["Next"], "lied_" + suffix if suffix else "lied2")
                self.assertEqual(only(later)["Next"], "hills_" + suffix if suffix else "hills")
        debt = reckoning["salt"]["Choices"]
        self.assertEqual(next(c for c in debt if route.CONFESSED in c["Set"])["Set"], [route.CONFESSED])
        self.assertIn(route.CLOSED, next(c for c in debt if route.CLOSED in c["Set"])["Set"])

    def test_reunion_remembers_inspection_without_implying_transfer(self):
        reunion = nodes(salt, "door.home_from_the_dark")
        for inspected, transferred, hatched in itertools.product((False, True), repeat=3):
            flags = {f for f, held in ((route.KILN_AGREED, inspected),
                                      (route.KILN, transferred), (route.HATCHED, hatched)) if held}
            choices = selectable(reunion["news"], flags)
            expected = ("news_hatched" if hatched else "news_egg" if transferred else
                        "news_inspected" if inspected else "news_hearth")
            self.assertEqual(only(choices)["Next"], expected)

    def test_first_night_slot_keeps_the_cut_morning_and_terminal_receipt(self):
        night = nodes(salt, "ridge.snowfield")
        self.assertEqual(only(night["cut"]["Choices"])["Next"], "explicit.1")
        slot = night["explicit.1"]
        self.assertEqual(only(slot["Choices"])["Next"], "morning")
        self.assertEqual(only(slot["Choices"])["Set"], [])
        self.assertEqual(only(night["down_the_hill"]["Choices"])["Set"], [route.SNOW])
        grief = nodes(salt, "kiln.long_night")
        self.assertEqual(only(selectable(grief["kiss"], set()))["Next"], "not_here")
        self.assertEqual(only(selectable(grief["kiss"], {route.SNOW}))["Next"], "not_here_again")

    def test_late_acceptance_does_not_answer_the_kept_heel(self):
        late = nodes(route, "epilogue.late")["page"]
        heel = nodes(route, "epilogue.heel")["page"]
        self.assertEqual(only(late["Choices"])["Set"], [])
        self.assertFalse(only(late["Choices"])["Next"])

    def test_current_mother_branches_are_exhaustive_after_loss(self):
        widow = nodes(route, "steps.widow")
        hatching = nodes(kiln, "kiln.hatching")
        custody = nodes(kiln, "kiln.whose")
        reveal = nodes(salt, "door.own_form")
        after = nodes(salt, "after.first_demon")
        for returned, present, hunting, bill in itertools.product((False, True), repeat=4):
            flags = {f for f, held in ((route.DV_RETURNED, returned),
                                      (route.DV_PRESENT, present),
                                      (route.DV_HUNTING, hunting),
                                      (route.DV_BILL, bill)) if held}
            for node, live in ((widow["mother"], "mother_alive"),
                               (hatching["chaplain"], "sky"),
                               (custody["whose"], "mother"),
                               (custody["whose_straw"], "mother"),
                               (reveal["now"], "mother")):
                choices = selectable(node, flags)
                self.assertEqual(only(choices)["Next"] == live, returned and present)
            for history in ("druids", "straw"):
                choices = selectable(widow[history], flags)
                self.assertEqual(only(choices)["Next"],
                                 "hunted" if hunting and present else
                                 "hunted_absent" if hunting else "mother")
            choices = selectable(after["house"], flags)
            self.assertEqual(only(choices)["Next"],
                             "bill" if bill else "druids" if hunting and present else
                             "druids_absent" if hunting else "end")
        self.assertEqual(only(custody["mother_absent"]["Choices"])["Next"], "choose")
        self.assertEqual(only(after["druids_absent"]["Choices"])["Next"], "end")






if __name__ == "__main__":
    unittest.main()
