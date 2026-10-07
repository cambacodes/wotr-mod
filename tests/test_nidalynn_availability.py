"""Export regressions blocked by the shared mention classifier (round 3).

Expected failures must be removed when that producer is repaired. These
assertions protect ancestry and religious affiliation from live-guest gates.
"""
import json
import unittest
from pathlib import Path


class NidalynnReferenceAvailabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = json.loads(Path(__file__).resolve().parents[1].joinpath(
            "development/Story.json").read_text(encoding="utf-8"))
        cls.scenes = {s["Id"]: s for s in payload["Scenes"]}

    def choice(self, suffix, node, index):
        scene = self.scenes["nidalynn.trickster." + suffix]
        return next(n for n in scene["Nodes"] if n["Id"] == node)["Choices"][index]

    @unittest.expectedFailure
    def test_both_sanctum_checks_ignore_mothers_current_availability(self):
        for index in (0, 1):
            self.assertNotIn("crossroute.devarra.unavailable",
                             self.choice("eggs.lamp_black", "look", index)["Forbids"])

    @unittest.expectedFailure
    def test_straw_acquisition_ignores_mothers_current_availability(self):
        self.assertNotIn("crossroute.devarra.unavailable",
                         self.choice("eggs.straw", "chit", 0)["Forbids"])

    @unittest.expectedFailure
    def test_hatching_ignores_goddess_romance_closure(self):
        self.assertNotIn("crossroute.iomedae.unavailable",
                         self.scenes["nidalynn.trickster.kiln.hatching"]["Forbids"])

    @unittest.expectedFailure
    def test_chaplain_ignores_goddess_romance_closure(self):
        self.assertNotIn("crossroute.iomedae.unavailable",
                         self.scenes["nidalynn.trickster.kiln.the_chaplain"]["Forbids"])
