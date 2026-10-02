"""Doc 16 §8c.6: the Seelah x Wenduag prerequisite sheet (storylines/household_pair_seelah_wenduag.py) lints clean, and the
lint catches the defects the reviewed handoff rules out."""
import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from storylines import household  # noqa: E402
from storylines import household_pair_seelah_wenduag as sw  # noqa: E402

P = sw.P


def mutated(fn):
    steps = copy.deepcopy(sw.STEPS)
    fn({s["id"]: s for s in steps})
    return steps


class SheetTests(unittest.TestCase):
    def test_sheet_is_clean(self):
        self.assertTrue(sw.validate(set(household.PARTNERS)))

    def test_no_shipped_pair_ids(self):
        for name in ("development/Story.json", "package/Story.json"):
            path = ROOT / name
            if path.exists():
                self.assertNotIn(sw.PREFIX, path.read_text(encoding="utf-8"), name)

    def test_debt_and_custody_outcomes(self):
        produced = sw._produced(sw.STEPS)
        for flag in (sw.DEBT["owed"], sw.DEBT["paid"], sw.DEBT["cost"], sw.BOUNDARY["flag"],
                     sw.CAPTIVE["custody_flag"]) + sw.COSTS:
            self.assertIn(flag, produced)
        self.assertEqual(sw.DEBT["outstanding_reader"]["forbids"], (sw.DEBT["paid"],))

    def assertRejects(self, fn, needle):
        with self.assertRaises(ValueError) as err:
            sw.validate(set(household.PARTNERS), mutated(fn))
        self.assertIn(needle, str(err.exception))

    def test_rejects_attitude_writer(self):
        self.assertRejects(lambda s: s[P("watch")]["outcomes"][0].__setitem__(
            "flags", (P("watch.seen"), P("watch.done"), "seelah.harem.attitude.wenduag.friend")), "only pair outcome")

    def test_rejects_short_delay(self):
        self.assertRejects(lambda s: s[P("debt_repayment")].__setitem__("delay", 47), "delay 47")

    def test_rejects_debt_on_failure(self):
        self.assertRejects(lambda s: s[P("stood")].__setitem__("failure", (P("stood.seen"), P("stood.debt_owed"))),
                           "failure writes")

    def test_rejects_wrapper_drift(self):
        self.assertRejects(lambda s: s[P("stood.after_restraint")].__setitem__("success", (P("stood.seen"),)),
                           "same outcomes")

    def test_rejects_same_timestamp_order(self):
        self.assertRejects(lambda s: s[P("restraint")].__setitem__("forbids", (P("restraint.seen"),)),
                           "must forbid " + P("stood.seen"))

    def test_rejects_unpaid_choice(self):
        self.assertRejects(lambda s: s[P("choice")].__setitem__(
            "requires", tuple(f for f in s[P("choice")]["requires"] if f != sw.DEBT["paid"])), "choice must require")

    def test_rejects_hang_with_custody(self):
        def fn(s):
            s[P("restraint")]["outcomes"][1]["flags"] += (sw.CAPTIVE["custody_flag"],)
        self.assertRejects(fn, '"Hang him" must not')

    def test_rejects_unproduced_read(self):
        self.assertRejects(lambda s: s[P("morning")].__setitem__("requires", (P("choice.never"),)), "no step produces")

    def test_rejects_reordered_indices(self):
        self.assertRejects(lambda s: s[P("choice")].__setitem__(
            "outcomes", {1: s[P("choice")]["outcomes"][0], 2: s[P("choice")]["outcomes"][1]}), "0..n-1")


if __name__ == "__main__":
    unittest.main()
