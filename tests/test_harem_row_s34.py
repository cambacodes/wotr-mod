"""Row reservations stay stable; J03 explicitly activates only approved contracts."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s34


ROOT = Path(__file__).resolve().parents[1]
PREFIX = "household.pair.hepzamirah_minagho."


class S34ReservationTests(unittest.TestCase):
    def test_registration_does_not_publish_unearned_job_or_change_existing_state(self):
        # A page and old returns cannot stand in for the missing operation.
        for history in ([], ["foresight.page_taken", "trickster.now"],
                        ["hepzamirah.trickster.returned", "minagho.trickster.returned"],
                        ["hepzamirah.closed", "minagho.closed"]):
            with self.subTest(history=history):
                scenes = [{"Id": "existing", "Nodes": [{"Id": "start", "Choices": []}]}]
                refs = {"trickster": "existing-etude"}
                payload = {"Scenes": scenes, "Etudes": refs, "PendingHooks": list(history)}
                before = copy.deepcopy(payload)
                s34.register(payload, scenes, refs)
                self.assertEqual(before, payload)
                self.assertIs(payload["Scenes"], scenes)
                self.assertIs(payload["Etudes"], refs)
                s34.register(payload, scenes, refs)
                self.assertEqual(before, payload)

    def test_schedule_preserves_reserved_primary_and_single_retry(self):
        schedule = json.loads((ROOT / "tools/harem-schedule.json").read_text(encoding="utf-8"))
        def entries(value):
            if isinstance(value, dict):
                yield value
                for child in value.values():
                    yield from entries(child)
            elif isinstance(value, list):
                for child in value:
                    yield from entries(child)
        rows = [entry for entry in entries(schedule) if entry.get("ref") == "S34"]
        self.assertEqual(1, len(rows))
        row = rows[0]
        self.assertEqual("reserved", row["status"])
        self.assertEqual(("5.03", 5, 1, 1),
                         (row["order"], row["chapter"], row["count"], row["retry"]))
        self.assertEqual(["hepzamirah", "minagho"], row["women"])

    def test_current_export_has_no_unsupported_shared_job(self):
        story = fresh_story()
        self.assertTrue({PREFIX + "job", PREFIX + "retry"} <= {scene["Id"] for scene in story["Scenes"]})
        self.assertFalse(any(PREFIX + "favour" in str(v) for v in story.get("Derived", {}).values()))


if __name__ == "__main__":
    unittest.main()
