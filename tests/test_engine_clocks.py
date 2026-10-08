"""Shared delay/timestamp behavior, independent of route prose and assembly."""
import copy
import unittest

from tools import rrt_verify as rules
from tools.harem_schedule_lint import delayed_clock_errors


class SharedClocksTests(unittest.TestCase):
    def setUp(self):
        scene = dict(Id='clock.scene', Relationship='clock', Owner='Narrator',
                     DelayHours=48, DelayClocks=['deed'], Requires=['deed', 'form'],
                     Nodes=[dict(Id='start', Text='Test', Choices=[
                         dict(Set=['deed', 'prior'], RefreshTimes=['deed'], Next='leave')]),
                            dict(Id='leave', Text='Test', Choices=[dict(Abort=True)])])
        self.model = rules.Model(dict(Scenes=[scene], Relationships={'clock': dict(
            StartedFlag='clock.started', ClosedFlag='clock.closed', CommittedFlag='clock.committed')}))
        self.scene = self.model.by_id['clock.scene']
        self.state = rules.SimState(5, 100)
        self.state.flags.update(['deed', 'form', 'prior', 'clock.started'])
        self.state.times.update(deed=52, form=99, prior=12)

    def test_declared_clock_ignores_newer_body_requirement(self):
        self.assertTrue(rules.sim_available(self.model, self.scene, self.state))
        self.state.hour = 99
        self.assertFalse(rules.sim_available(self.model, self.scene, self.state))

    def test_missing_saved_clock_cannot_grant_the_wait(self):
        del self.state.times['deed']
        self.state.times['form'] = 0
        self.assertFalse(rules.sim_available(self.model, self.scene, self.state))

    def test_declared_clocks_must_name_saved_deeds(self):
        self.scene['DelayClocks'] = ['form']
        self.assertTrue(delayed_clock_errors(self.scene, self.model.story))
        self.scene['DelayClocks'] = ['deed']
        self.assertFalse(delayed_clock_errors(self.scene, self.model.story))

    def test_only_explicit_chosen_clock_refreshes_across_reload(self):
        choice = self.scene['Nodes'][0]['Choices'][0]
        leave = self.scene['Nodes'][1]['Choices'][0]
        for hour in (100, 124):
            self.state.hour = hour
            self.assertFalse(rules.sim_play(self.model, self.scene, self.state, {}, plan=(0, [choice, leave])))
            self.assertEqual(self.state.times['deed'], hour)
            self.assertEqual(self.state.times['prior'], 12)
            self.assertNotIn(self.scene['Id'], self.state.flags)
            self.state = copy.deepcopy(self.state)

    def test_legacy_delay_still_uses_latest_requirement(self):
        self.scene.pop('DelayClocks')
        self.assertFalse(rules.sim_available(self.model, self.scene, self.state))
        self.state.hour = 147
        self.assertTrue(rules.sim_available(self.model, self.scene, self.state))
