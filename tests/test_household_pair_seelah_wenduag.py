"""Doc 16 §8c.6: the Seelah x Wenduag prerequisite sheet (storylines/household_pair_seelah_wenduag.py) lints clean, and the
lint catches the defects the reviewed handoff rules out."""
import copy
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from storylines import household
from storylines import household_pair_seelah_wenduag as sw
P = sw.P

def mutated(fn):
    steps = copy.deepcopy(sw.STEPS)
    fn({s["id"]: s for s in steps})
    return steps

class SheetTests(unittest.TestCase):

    def test_sheet_is_clean(self):
        self.assertTrue(sw.validate(set(household.PARTNERS)))

    def test_implementation_keeps_reviewed_step_ids(self):
        from storylines import harem_s02
        harem_s02.register()
        actual = [s['Id'] for s in household.ENTRIES + household.INVITATIONS
                  if s['Id'].startswith(sw.PREFIX)]
        self.assertEqual(actual, [s['id'] for s in sw.STEPS if s.get('kind') != 'derived'])

    def test_debt_and_custody_outcomes(self):
        produced = sw._produced(sw.STEPS)
        for flag in (sw.DEBT["owed"], sw.DEBT["paid"], sw.DEBT["cost"], sw.BOUNDARY["flag"],
                     sw.CAPTIVE["custody_flag"]) + sw.COSTS:
            self.assertIn(flag, produced)
        self.assertEqual(sw.DEBT["outstanding_reader"]["forbids"], (sw.DEBT["paid"],))

    def assertRejects(self, fn, needle):
        with self.assertRaises(ValueError) as err:
            sw.validate(set(household.PARTNERS), mutated(fn))
        self.assertIsInstance(err.exception, ValueError)

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

    def test_amended_steps_keep_existing_ids_and_append_invitation(self):
        self.assertEqual([step['id'] for step in sw.STEPS], [P(name) for name in (
            'init', 'spar', 'rematch', 'watch', 'restraint', 'restraint.after_stood', 'stood',
            'stood.after_restraint', 'debt_repayment', 'choice', 'morning', 'invite')])
        steps = {step['id']: step for step in sw.STEPS}
        self.assertEqual(steps[P('invite')]['delay'], 0)
        self.assertEqual(steps[P('invite')]['rest_allowance'], None)
        self.assertEqual(steps[P('rematch')]['outcomes'][1]['flags'], (P('rematch.seen'), P('rematch.declined')))
        self.assertEqual(steps[P('debt_repayment')]['outcomes'][2]['flags'],
                         (P('debt_repayment.seen'), P('captive.rusk_dead'), P('debt.betrayed')))
        self.assertIn(P('choice.watch_taken'), steps[P('choice')]['outcomes'][0]['flags'])
        self.assertNotIn(P('choice.back_room'), sw._produced(sw.STEPS))
        self.assertNotIn(P('boundary.breached'), sw._produced(sw.STEPS))

    def test_rejects_missing_participant_and_wrong_allowance(self):
        self.assertRejects(lambda s: s[P('stood.after_restraint')].__setitem__('participants', ('wenduag',)), 'both participants')
        self.assertRejects(lambda s: s[P('rematch')].__setitem__('rest_allowance', 'household.pair'), 'wrong rest allowance')

    def test_rejects_missing_clock_or_invented_invitation_delay(self):
        self.assertRejects(lambda s: s[P('watch')].__setitem__('any_groups', ()), 'alternative respect clocks')
        self.assertRejects(lambda s: s[P('invite')].__setitem__('delay', 48), 'invalid invitation delay')

    def test_rejects_abort_writer_and_outcomeless_terminal(self):
        self.assertRejects(lambda s: s[P('choice')]['outcomes'][2].__setitem__('flags', (P('choice.seen'),)), 'Abort writes nothing')
        self.assertRejects(lambda s: s[P('morning')]['outcomes'][0].__setitem__('flags', (P('morning.seen'),)), 'seen and an outcome')

    def test_rejects_missing_wound_cost_on_either_terminal_or_wrapper(self):
        for name in ('stood', 'stood.after_restraint'):
            for terminal in ('success', 'failure'):
                self.assertRejects(lambda s, name=name, terminal=terminal: s[P(name)].__setitem__(
                    terminal, tuple(flag for flag in s[P(name)][terminal] if flag != P('cost.seelah_wounded'))), 'record Seelah wounded')

    def test_rejects_missing_betrayal_or_breach_gate(self):
        for flag in (P('debt.betrayed'), P('captive.rusk_dead'), P('boundary.breached')):
            self.assertRejects(lambda s, flag=flag: s[P('choice')].__setitem__(
                'forbids', tuple(value for value in s[P('choice')]['forbids'] if value != flag)), 'choice must forbid')
if __name__ == '__main__':
    unittest.main()
