"""The blocked S22 incident must not be manufactured from other history."""
import copy
import unittest

from storylines.harem_rows import s22
from tests.story_fixture import fresh_story


PREFIX = "household.pair.wenduag_irabeth."


class S22BlockedIncidentTests(unittest.TestCase):
    def test_registration_preserves_payload_scenes_and_native_refs(self):
        payload = fresh_story()
        scenes = payload["Scenes"]
        refs = payload["Etudes"]
        before = copy.deepcopy(payload)
        s22.register(payload, scenes, refs)
        s22.register(payload, scenes, refs)
        self.assertEqual(payload, before)
        self.assertIs(payload["Scenes"], scenes)
        self.assertIs(payload["Etudes"], refs)

    def test_page_commitments_bodies_and_native_complaint_cannot_unlock_vigil(self):
        from tools import rrt_verify

        payload = fresh_story()
        s22.register(payload, payload["Scenes"], payload["Etudes"])
        model = rrt_verify.Model(payload)
        for extra in (
            [],
            ["household.native.wenduag_complaint_seen"],
            ["s22.test.tavern_murder_seen", "s22.test.regular_soldiers_seen"],
            ["wenduag.trickster.echo.abyss.returned_available"],
            ["tirabade.harem.eligible", "anevia.epoch_unavailable"],
            ["irabeth.epoch_unavailable"],
            ["wenduag.closed"],
        ):
            with self.subTest(extra=extra):
                state = rrt_verify.SimState(5, 1000)
                state.flags.update([
                    "trickster", "trickster.now", "foresight.page_taken",
                    "trickster.foresight.accepted", "wenduag.committed",
                    "irabeth.committed", "wenduag.harem.eligible",
                    "irabeth.harem.eligible", "wenduag.present_now",
                    "irabeth.present_now", *extra,
                ])
                rrt_verify.sim_complete(model, state)
                self.assertFalse(any(key.startswith(PREFIX) for key in state.flags))
                self.assertFalse(any(scene["Id"].startswith(PREFIX)
                                     for scene in payload["Scenes"]))

    def test_export_has_no_vigil_producers_readers_or_intimate_slots(self):
        payload = fresh_story()
        self.assertFalse(any(scene["Id"].startswith(PREFIX)
                             for scene in payload["Scenes"]))
        for field in ("Derived", "DerivedOpenRoutes", "SeenCues", "SelectedAnswers"):
            self.assertFalse(any(key.startswith(PREFIX) for key in payload.get(field, {})))
        for scene in payload["Scenes"]:
            for node in scene["Nodes"]:
                for choice in node["Choices"]:
                    self.assertFalse(any(key.startswith(PREFIX) for key in choice.get("Set", [])))


if __name__ == "__main__":
    unittest.main()
