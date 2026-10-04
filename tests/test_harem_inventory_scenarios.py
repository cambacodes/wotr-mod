"""E-Q7-36: approved inventory and negative delivery cases, without inventing build sheets."""
import contextlib
import copy
import io
import json
from pathlib import Path
import unittest
from tools import harem_rest_sim as sim, rrt_verify as e9, harem_schedule_lint as schedule_lint

ROOT = Path(__file__).resolve().parents[1]


class HaremInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))
        cls.schedule = json.loads(sim.SCHEDULE.read_text(encoding="utf-8"))
        cls.scenarios = json.loads((ROOT / 'tools/harem_inventory_scenarios.json').read_text(encoding="utf-8"))
        cls.route_run = e9.simulate_rest_budget(e9.Model(cls.story))

    def test_missing_build_sheets_and_native_walk_block_certification(self):
        result = sim.inventory_acceptance(self.story, self.schedule, self.scenarios)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['status'], 'data_blocked')
        self.assertFalse(result['certified'])
        self.assertTrue(any('native eligibility/gate-hour' in b for b in result['blockers']))
        self.assertTrue(any('build-sheet scene missing' in b for b in result['blockers']))
        self.assertTrue(any('enmity producers' in b for b in result['blockers']))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sim.main(['--inventory']), 1)

    def test_census_allowance_and_binding_mutations_are_rejected(self):
        for mutation in ('counts', 'ceiling', 'allowance', 'scene'):
            with self.subTest(mutation=mutation):
                story, data, expected = copy.deepcopy((self.story, self.schedule, self.scenarios))
                if mutation == 'counts': data['expected_counts']['ch5_primary'] += 1
                if mutation == 'ceiling': expected['campaign_ceilings']['ideal'] += 1
                if mutation == 'allowance': story['RestAllowances']['household.pair'] = 2
                if mutation == 'scene': expected['row_scene_ids']['S02'] = ['missing.scene']
                self.assertTrue(sim.inventory_acceptance(story, data, expected)['errors'])

    def test_conditional_profiles_share_rests_and_do_not_certify_native_delivery(self):
        for profile in self.scenarios['scenarios']:
            with self.subTest(profile=profile['id']):
                options = {k: profile[k] for k in ('conditional', 'rematch', 'fallback', 'late_s06') if k in profile}
                result = sim.simulate(self.story, self.schedule, self.route_run, **options)
                if not profile['conditional']:
                    self.assertTrue(result['blocked'])
                    self.assertFalse(result['pair_complete'])
                    continue
                self.assertFalse(result['blocked'])
                self.assertTrue(result['pair_complete'])
                self.assertNotIn('S46', result['completed'])
                for chapter in result['chapters']:
                    self.assertEqual(chapter['deadline_misses'], profile.get('expected_deadline_misses', {}).get(str(chapter['chapter']), []))
                    self.assertLessEqual(chapter['load'], 1)
                    usage = {}
                    for hour, allowance, ref in chapter['slots']:
                        usage[hour, allowance] = usage.get((hour, allowance), 0) + 1
                    for (_, allowance), count in usage.items():
                        self.assertLessEqual(count, self.story['RestAllowances'][allowance])
                ch5 = result['chapters'][1]
                self.assertGreaterEqual(ch5['rests_needed'], 20)
                counted = ch5['household_beats'] + (30 if profile.get('fallback') else 0)
                ceiling = self.scenarios['chapter_ceilings']['5']['worst' if profile.get('fallback') else 'ideal']
                self.assertLessEqual(counted, ceiling)

    def test_participant_absence_keeps_outcome_withheld_in_walk_timed_model(self):
        arrivals = {rel: 0 for rel in self.story['Relationships']}
        arrivals.update({woman: 0 for woman in self.schedule['seat_women']})
        arrivals.pop('wenduag')
        gates = {key: 0 for row in self.schedule['schedule'] for key in row.get('reads', [])}
        result = sim.simulate(self.story, self.schedule, self.route_run, arrivals=arrivals, gate_hours=gates)
        self.assertFalse(result['pair_complete'])
        self.assertNotIn('S02.morning', result['completed'])
        self.assertTrue(any('wenduag' in b['missing'] for b in result['blocked']))

    def test_paid_page_offer_uses_existing_real_producers(self):
        model = e9.Model(self.story)
        state = e9.SimState(3, 1000)
        state.flags.update(['trickster', 'seelah.committed'])
        offer = model.by_id['household.table.offered']
        e9.sim_complete(model, state)
        self.assertFalse(e9.sim_available(model, offer, state))
        # This is the existing acceptance/cost pair, not the desired public composite.
        state.flags.update(['trickster.foresight.accepted', 'trickster.foresight.cost.promise'])
        e9.sim_complete(model, state)
        self.assertTrue(e9.sim_available(model, offer, state))
        state.flags.add(self.story['Relationships']['seelah']['ClosedFlag'])
        e9.sim_complete(model, state)
        self.assertFalse(e9.sim_available(model, offer, state))

    def test_branch_clock_negative_uses_existing_w0c_validator(self):
        fixture = {'Scenes': [{'Id': 'clock.producer', 'Nodes': [{'Choices': [{'Set': ['a.seen', 'b.seen']}]}]}]}
        delayed = {'Id': 'delayed.fixture', 'DelayHours': 48, 'Requires': [],
                   'RequiresAnyGroups': [['a.seen', 'b.seen']]}
        self.assertEqual(schedule_lint.delayed_clock_errors(delayed, fixture), [])
        delayed['RequiresAnyGroups'][0][1] = 'untimed.derived'
        self.assertTrue(schedule_lint.delayed_clock_errors(delayed, fixture))
