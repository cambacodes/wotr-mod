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
                options = {k: profile[k] for k in ('conditional', 'rematch', 'fallback', 'late_s06', 'arueshalae_state') if k in profile}
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
                        if allowance is not None:  # eng7-f3: dynamic flavour is unkeyed.
                            self.assertLessEqual(count, self.story['RestAllowances'][allowance])
                ch5 = result['chapters'][1]
                self.assertGreaterEqual(ch5['rests_needed'], 20)
                counted = ch5['household_beats'] + (30 if profile.get('fallback') else 0)
                budget_profile = profile.get('budget_profile', 'worst' if profile.get('fallback') or profile.get('rematch') else 'ideal')
                ceiling = self.scenarios['chapter_ceilings']['5'][budget_profile]
                self.assertLessEqual(counted, ceiling)

    # eng7-f3
    def test_data_inventory_names_every_missing_scene_and_enmity_reader(self):
        result = sim.inventory_acceptance(self.story, self.schedule, self.scenarios)
        missing = result['missing_data']
        active = [r['ref'] for r in self.schedule['schedule'] if r.get('count') and r.get('status') != 'retired']
        self.assertEqual(missing['schedule_scene_refs'], active)
        self.assertEqual(missing['packet_scene_refs'], ['K1', 'K2', 'K3'])
        readers = sorted({f for k, groups in self.story['Derived'].items() if k.endswith('.harem.enmity_any')
                          for group in groups for f in group} | {
                              'minagho_chivarro.harem.enmity.minagho.hepzamirah',
                              'minagho_chivarro.harem.enmity.chivarro.hepzamirah'})
        self.assertEqual(missing['enmity_producer_flags'], readers)
        self.assertEqual(len(readers), 12)
        self.assertFalse(result['enmity_producers'])
        self.assertTrue(missing['native_walk'])

    def test_data_inventory_drift_and_partial_enmity_production_are_visible(self):
        expected = copy.deepcopy(self.scenarios)
        expected['missing_data']['schedule_scene_refs'].remove('S02')
        self.assertTrue(sim.inventory_acceptance(self.story, self.schedule, expected)['errors'])
        story = copy.deepcopy(self.story)
        flag = expected['missing_data']['enmity_producer_flags'][0]
        producer = story['Scenes'][0]
        producer['Nodes'][0]['Choices'][0]['Set'].append(flag)
        result = sim.inventory_acceptance(story, self.schedule, self.scenarios)
        self.assertIn(flag, result['enmity_producers'])
        self.assertNotIn(flag, result['missing_data']['enmity_producer_flags'])
        self.assertEqual(len(result['missing_data']['enmity_producer_flags']), 11)
        self.assertTrue(result['errors'])
        self.assertFalse(result['certified'])

    def test_conditional_cli_runs_every_available_profile_and_passes(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(sim.main(['--conditional']), 0)
        for profile in self.scenarios['scenarios']:
            if profile['conditional']:
                self.assertIn('Scenario: ' + profile['id'], output.getvalue())
        self.assertIn('does not certify native reachability', output.getvalue())

    def test_unkeyed_flavour_never_consumes_protected_slots_or_hides_a_miss(self):
        for rematch in (False, True):
            result = sim.simulate(self.story, self.schedule, self.route_run, conditional=True,
                                  fallback=True, late_s06=True, rematch=rematch)
            ch5 = result['chapters'][1]
            dynamic = [(hour, allowance, ref) for hour, allowance, ref in ch5['slots'] if ref.startswith('reserved.dynamic.')]
            self.assertEqual([ref for _, _, ref in dynamic], ['reserved.dynamic.0', 'reserved.dynamic.1', 'reserved.dynamic.2'])
            self.assertTrue(all(allowance is None for _, allowance, _ in dynamic))
            self.assertEqual(ch5['dynamic'], 3)
            self.assertEqual(ch5['protected'], 48 + int(rematch))
            self.assertEqual(ch5['household_beats'], ch5['protected'] + ch5['optional'] + ch5['letters'] + ch5['dynamic'])
            self.assertEqual(ch5['deadline_misses'], [])
        # A real shortage still fails; the simulator must not simply ignore reserved.dynamic.2.
        run = copy.deepcopy(self.route_run)
        run['chapter_days'][5] = 25
        result = sim.simulate(self.story, self.schedule, run, conditional=True, fallback=True, rematch=True)
        self.assertTrue(result['chapters'][1]['deadline_misses'])
        self.assertFalse(result['pair_complete'])
    # end eng7-f3

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
        state.flags.update(['trickster', 'seelah.committed', 'seelah.chosen_future', 'seelah.short_future_chosen'])
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
