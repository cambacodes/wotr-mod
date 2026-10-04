"""Temporal presence and contact rules must match the managed runtime."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import rrt_verify as rv


class ContactWindowTests(unittest.TestCase):
    def test_age_boundaries_and_superseded_witness(self):
        window = dict(Flag="produced", MinAgeHours=12, MaxAgeHours=48, SupersededBy=["superseded"])
        state = rv.SimState(5, 100)
        self.assertTrue(rv.contact_windows_available([window], state))
        state.flags.add("produced")
        self.assertFalse(rv.contact_windows_available([window], state))
        for at, expected in [(-1, False), (101, False), (100, False), (89, False), (88, True), (52, True), (51, False)]:
            state.times["produced"] = at
            self.assertEqual(rv.contact_windows_available([window], state), expected, at)
        state.times["produced"] = 80
        state.flags.add("superseded")
        self.assertFalse(rv.contact_windows_available([window], state))

    def test_validation(self):
        known = {"produced", "superseded"}
        good = dict(Flag="produced", MinAgeHours=12, MaxAgeHours=48, SupersededBy=["superseded"])
        self.assertTrue(rv.contact_windows_valid([good], known))
        for changes in [dict(Flag="unknown"), dict(MinAgeHours=-1), dict(MaxAgeHours=11), dict(MaxAgeHours="48"),
                        dict(SupersededBy=["unknown"]), dict(SupersededBy=["produced"]),
                        dict(SupersededBy=["superseded", "superseded"])]:
            bad = dict(good, **changes)
            self.assertFalse(rv.contact_windows_valid([bad], known), changes)
        self.assertFalse(rv.contact_windows_valid([good, good], known))
        self.assertFalse(rv.contact_windows_valid(None, known))

    def test_hepzamirah_hunt_window_and_stale_body(self):
        story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))
        model = rv.Model(story)
        presence = story["Presences"]["hepzamirah.presence"]
        hunt = "hepzamirah.trickster.bond.the_hunt"
        self.assertEqual(presence["ContactWindows"], [dict(Flag=hunt, MinAgeHours=120)])
        visits = [s for s in model.scenes if s["ContactUnit"] == presence["Unit"] and presence["Area"] in s["Areas"]]
        self.assertTrue(visits)
        state = rv.SimState(5, 1000)
        state.flags.update(presence["Requires"] + [hunt])
        state.times[hunt] = state.hour
        for hours in [0, 24, 119, 120, 121]:
            at = copy.deepcopy(state)
            at.hour += hours
            expected = hours >= 120
            self.assertEqual(rv.presence_wanted(presence, at, presence["Area"]), expected, hours)
            for scene in visits:
                self.assertEqual(rv.contact_windows_for_scene(model, scene, at, presence["Area"]), expected, scene["Id"])
        state.times.pop(hunt)
        self.assertFalse(rv.presence_wanted(presence, state, presence["Area"]))
        self.assertTrue(all(not rv.contact_windows_for_scene(model, s, state) for s in visits))


if __name__ == "__main__":
    unittest.main()
