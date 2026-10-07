"""An incomplete S18.f contract must not grant an unearned truce."""
import copy
import unittest

from storylines.harem_rows import s18f


class S18fBlockedRegistration(unittest.TestCase):
    def test_registration_preserves_existing_state_and_captivity_docket(self):
        scenes = [{"Id": "household.docket.horzalah_hepzamirah.account"}]
        refs = {"trickster": "existing-binding"}
        payload = {
            "Scenes": scenes,
            "Etudes": refs,
            "Derived": {
                "horzalah.harem.enmity.hepzamirah": [["existing.enmity"]],
                "household.docket.horzalah_hepzamirah.unresolved": [["existing.account"]],
            },
        }
        before = copy.deepcopy(payload)
        s18f.register(payload, scenes, refs)
        s18f.register(payload, scenes, refs)
        self.assertEqual(payload, before)
        self.assertIs(payload["Scenes"], scenes)
        self.assertIs(payload["Etudes"], refs)


if __name__ == "__main__":
    unittest.main()
