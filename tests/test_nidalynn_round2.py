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
                self.assertEqual(len(start), 1)
                self.assertEqual(len(later), 1)
                suffix = "clerk" if clerk else "quartermaster" if quartermaster else None
                self.assertEqual(start[0]["Next"], "lied_" + suffix if suffix else "lied2")
                self.assertEqual(later[0]["Next"], "hills_" + suffix if suffix else "hills")
                if suffix:
                    self.assertIn(suffix, reckoning[later[0]["Next"]]["Text"])
        debt = reckoning["salt"]["Choices"]
        self.assertEqual(debt[0]["Set"], [route.CONFESSED])
        self.assertIn(route.CLOSED, debt[1]["Set"])

    def test_reunion_remembers_inspection_without_implying_transfer(self):
        reunion = nodes(salt, "door.home_from_the_dark")
        for inspected, transferred, hatched in itertools.product((False, True), repeat=3):
            flags = {f for f, held in ((route.KILN_AGREED, inspected),
                                      (route.KILN, transferred), (route.HATCHED, hatched)) if held}
            choices = selectable(reunion["news"], flags)
            self.assertEqual(len(choices), 1)
            expected = ("news_hatched" if hatched else "news_egg" if transferred else
                        "news_inspected" if inspected else "news_hearth")
            self.assertEqual(choices[0]["Next"], expected)
        self.assertIn("every evening", reunion["news_inspected"]["Text"])
        self.assertIn("I'll come and turn it", nodes(kiln, "hearth.listening")["cold"]["Text"])

    def test_first_night_slot_keeps_the_cut_morning_and_terminal_receipt(self):
        night = nodes(salt, "ridge.snowfield")
        self.assertEqual(night["cut"]["Choices"][0]["Next"], "explicit.1")
        slot = night["explicit.1"]
        self.assertEqual(slot["Choices"][0]["Next"], "morning")
        self.assertEqual(slot["Choices"][0]["Set"], [])
        self.assertNotIn("dragon", slot["Text"])
        self.assertEqual(night["down_the_hill"]["Choices"][0]["Set"], [route.SNOW])
        grief = nodes(salt, "kiln.long_night")
        self.assertEqual(selectable(grief["kiss"], set())[0]["Next"], "not_here")
        self.assertEqual(selectable(grief["kiss"], {route.SNOW})[0]["Next"], "not_here_again")

    def test_late_acceptance_does_not_answer_the_kept_heel(self):
        late = nodes(route, "epilogue.late")["page"]
        heel = nodes(route, "epilogue.heel")["page"]
        self.assertIn("she ate hers", late["Text"])
        self.assertIn("never moved it", heel["Text"])
        self.assertEqual(late["Choices"][0]["Set"], [])
        self.assertFalse(late["Choices"][0]["Next"])

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
                self.assertEqual(len(choices), 1)
                self.assertEqual(choices[0]["Next"] == live, returned and present)
            for history in ("druids", "straw"):
                choices = selectable(widow[history], flags)
                self.assertEqual(len(choices), 1)
                self.assertEqual(choices[0]["Next"],
                                 "hunted" if hunting and present else
                                 "hunted_absent" if hunting else "mother")
            choices = selectable(after["house"], flags)
            self.assertEqual(len(choices), 1)
            self.assertEqual(choices[0]["Next"],
                             "bill" if bill else "druids" if hunting and present else
                             "druids_absent" if hunting else "end")
        self.assertEqual(custody["mother_absent"]["Choices"][0]["Next"], "choose")
        self.assertEqual(after["druids_absent"]["Choices"][0]["Next"], "end")

    def test_snowfield_releases_wrist_and_keeps_loose_hair(self):
        cut = nodes(salt, "ridge.snowfield")["cut"]["Text"]
        self.assertIn("releases one wrist", cut)
        self.assertNotIn("braid has come undone", cut)

    def test_lastcall_helper_wraps_each_appended_paragraph_once(self):
        from storylines import lastcall_partners
        route.integrate({"Presences": {}, "SeenCues": {}})
        partner = next(p for p in lastcall_partners.PARTNERS if p["rel"] == route.REL)
        for paragraph in partner["paragraphs"]:
            text = paragraph["Text"]
            self.assertEqual(text.count("{n}"), text.count("{/n}"))
            self.assertNotIn("{n}{n}", text)
        self.assertEqual(len(partner["paragraphs"]), 12)


if __name__ == "__main__":
    unittest.main()
