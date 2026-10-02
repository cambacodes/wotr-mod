"""Harem W0 (16 §8c): table_entry()/_table_scene() take a `delay` (DelayHours), default 0."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from storylines import household  # noqa: E402
from story_format import c, n  # noqa: E402

NODES = [n("start", "Seelah", "Test.", c("Continue"))]


class HouseholdDelayTests(unittest.TestCase):
    def setUp(self):
        self._entries = list(household.ENTRIES)

    def tearDown(self):
        household.ENTRIES[:] = self._entries

    def test_default_delay_is_zero(self):
        body = household.table_entry("test.delay.default", "T", "[T]", NODES, ("seelah", "konomi"), "test.trigger")
        self.assertEqual(body["DelayHours"], 0)

    def test_delay_is_passed_through(self):
        body = household.table_entry("test.delay.48", "T", "[T]", NODES, ("seelah", "konomi"), "test.trigger", delay=48)
        self.assertEqual(body["DelayHours"], 48)
        self.assertIn("test.trigger", body["Requires"])
        self.assertEqual(body["InteractionHub"], household.TABLE_HUB)

    def test_table_scene_delay(self):
        body = household._table_scene("test.delay.ts", "T", "Seelah", "[T]", NODES, ("a",), (), delay=8)
        self.assertEqual(body["DelayHours"], 8)
        self.assertEqual(household._table_scene("test.delay.ts0", "T", "Seelah", "[T]", NODES, ("a",), ())["DelayHours"], 0)


if __name__ == "__main__":
    unittest.main()
