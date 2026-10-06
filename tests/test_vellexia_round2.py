"""Route-local regressions for paid returns, separate stances and closing history."""
import copy
import unittest

from expansion import make_expansion


def visible(paragraph, flags):
    return (set(paragraph.get("Requires", ())) <= flags
            and not set(paragraph.get("Forbids", ())) & flags
            and all(set(group) & flags for group in paragraph.get("AnyGroups", ())))


class VellexiaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = make_expansion()
        cls.scenes = {s["Id"]: s for s in cls.payload["Scenes"] if s["Id"].startswith("vellexia.")}

    def text(self, ending, flags):
        page = self.scenes["vellexia." + ending]["Nodes"][0]
        return page["Text"] + "\n" + "\n".join(p["Text"] for p in page.get("Paragraphs", ()) if visible(p, flags))

    def test_opening_does_not_depend_on_jerribeth_availability(self):
        answer = self.scenes["vellexia.unfinished_likeness"]["Nodes"][0]["Choices"][0]
        self.assertEqual("warning", answer["Next"])
        self.assertFalse(any("jerribeth" in f for f in answer["Requires"] + answer["Forbids"]))

    def test_night_delay_starts_with_lovers_farewell(self):
        night = self.scenes["vellexia.trickster.after.night"]
        flags = {"trickster.ever", "vellexia.committed", "vellexia.invited"}
        self.assertFalse(set(night["Requires"]) <= flags)
        # Rules.Available anchors delays to the latest held requirement.
        flags.add("vellexia.farewell_lovers")
        times = {"vellexia.committed": 0, "vellexia.invited": 24, "vellexia.farewell_lovers": 72}
        anchor = max(times[f] for f in night["Requires"] if f in times)
        self.assertFalse(83 - anchor >= night["DelayHours"])
        self.assertTrue(84 - anchor >= night["DelayHours"])

    def test_both_physical_hosts_collect_cost_before_stance(self):
        for host in ("after.visit", "after.visit_quarters"):
            nodes = {n["Id"]: n for n in self.scenes["vellexia.trickster." + host]["Nodes"]}
            self.assertIn("memorial feasts", nodes["unmirrored"]["Text"])
            self.assertIn("thrown down the stairs", nodes["diminished"]["Text"])
            self.assertIn("will not cast", nodes["diminished"]["Text"])
            self.assertIn("I shall decide each time", nodes["want"]["Text"])
            self.assertIn("vellexia.closed", nodes["collect"]["Choices"][0]["Set"])

    def test_rescue_only_endings_do_not_invent_a_shell_or_private_contact(self):
        flags = {"vellexia.prediction_known", "vellexia.trickster.returned", "vellexia.trickster.cost.diminished"}
        for ending in ("ending_interrupted", "ending_ascent", "ending_sacrifice"):
            text = self.text(ending, flags)
            self.assertNotIn("take them off", text)
            self.assertNotIn("shell stayed closed", text)
            self.assertNotIn("silver cover kept", text)
        mirror = self.text("ending_mirror", flags | {"vellexia.trickster.kept_as_mirror"})
        self.assertNotIn("shell she had offered", mirror)

    def test_closed_return_has_no_unplayed_play(self):
        flags = {"vellexia.closed", "vellexia.trickster.returned", "vellexia.trickster.visited"}
        self.assertNotIn("old play", self.text("ending_closed", flags))
        self.assertIn("old play", self.text("ending_closed", flags | {"vellexia.hour_kept"}))

    def test_returned_commander_keeps_exactly_one_earned_cost_copy(self):
        flags = {"vellexia.farewell_lovers", "vellexia.trickster.cost.diminished",
                 "vellexia.trickster.cost.bored_once"}
        for ending in ("ending_lovers", "trickster.epilogue.commit"):
            for extra in (set(), {"sacrifice", "trickster.commander_back"}):
                text = self.text(ending, flags | extra)
                self.assertEqual(1, text.count("take them off"))
                self.assertEqual(1, text.count("one dull sentence"))
            text = self.text(ending, flags | {"sacrifice"})
            self.assertNotIn("take them off", text)
            self.assertNotIn("one dull sentence", text)

    def test_interrupted_contact_never_repeats_private_costs(self):
        flags = {"vellexia.prediction_known", "vellexia.trickster.cost.diminished",
                 "vellexia.trickster.cost.bored_once", "vellexia.trickster.late_committed"}
        text = self.text("ending_interrupted", flags)
        self.assertNotIn("take them off", text)
        self.assertNotIn("one dull sentence", text)
        self.assertIn("hands were never finished", text)

    def test_final_company_and_delay_exclude_late_romance(self):
        forbidden = self.payload["DerivedForbids"]["vellexia.trickster.late_committed"]
        for stance in ("vellexia.farewell_friends", "vellexia.farewell_slow"):
            self.assertIn(stance, forbidden)
            self.assertIn(stance, self.scenes["vellexia.trickster.epilogue.commit"]["Forbids"])
        self.assertIn("vellexia.trickster.night_kept", self.scenes["vellexia.trickster.epilogue.commit"]["Forbids"])

    def test_daeran_cameo_requires_positive_presence(self):
        page = self.scenes["vellexia.trickster.epilogue.commit"]["Nodes"][0]
        cameo = next(p for p in page["Paragraphs"] if p["Text"].startswith("{n}Daeran,"))
        self.assertFalse(visible(cameo, set()))
        self.assertTrue(visible(cameo, {"daeran.in_party"}))
        self.assertFalse(visible(cameo, {"daeran.in_party", "daeran.dead"}))

    def test_explicit_cut_is_on_night_path_without_new_effects(self):
        nodes = {n["Id"]: n for n in self.scenes["vellexia.trickster.after.night"]["Nodes"]}
        slot = "vellexia.trickster.after.night.explicit.1"
        self.assertEqual(slot, nodes["threshold"]["Choices"][0]["Next"])
        self.assertEqual("morning", nodes[slot]["Choices"][0]["Next"])
        self.assertEqual([], nodes[slot]["Choices"][0]["Set"])
        self.assertTrue(nodes[slot]["Text"])


if __name__ == "__main__":
    unittest.main()
