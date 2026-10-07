"""ER-H3 uses the full roster fixture and shares allowance contention with both S02 paths."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from tools import harem_rest_sim as sim, rrt_verify as e9

ROOT = Path(__file__).resolve().parents[1]


class FullRosterBudget(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.data = json.loads(sim.SCHEDULE.read_text(encoding='utf-8'))
        cls.route_run = e9.simulate_rest_budget(e9.Model(copy.deepcopy(cls.story)))

    def test_every_row_has_instantiated_outcome_paragraphs_on_epilogue_only(self):
        fixture = sim.roster_fixture(self.story, self.data)
        model = e9.Model(fixture)
        self.assertEqual(e9.validate(model), [])
        page = model.by_id['harem.sim.outcomes']
        self.assertEqual(len(page['Nodes'][0]['Paragraphs']), 2 * len(self.data['schedule']))
        for row in self.data['schedule']:
            self.assertIn('harem.sim.' + row['ref'].lower(), model.by_id)
            for outcome in ('resolved', 'unsettled'):
                flag = 'household.protected.' + row['ref'].lower() + '.' + outcome
                self.assertEqual(sum(p['Requires'] == [flag] for p in page['Nodes'][0]['Paragraphs']), 1)
        for packet in self.data['packets']:
            nodes = model.by_id['harem.sim.packet.' + packet['id'].lower()]['Nodes']
            self.assertEqual([node['Id'] for node in nodes], [ref.lower() for ref in packet['children']])
            self.assertTrue(all(not node['Paragraphs'] for node in nodes))

    def test_both_success_paths_finish_with_full_ch5_docket_and_optional_reservations(self):
        for rematch in (False, True):
            with self.subTest(rematch=rematch):
                result = sim.simulate(self.story, self.data, self.route_run, conditional=True, rematch=rematch)
                self.assertTrue(result['pair_complete'])
                self.assertEqual(result['blocked'], [])
                start5 = sum(self.route_run['chapter_days'].get(ch, 0) * 24 for ch in range(5))
                self.assertEqual(result['pair_eligibility'], start5 + 24 * 24)
                self.assertEqual(result['chapters'][1]['deadline_misses'], [])
                self.assertEqual(result['chapters'][1]['optional'], 22)
                self.assertEqual(result['chapters'][1]['reserved_pair'], 22)
                # eng7-f3: three flavour beats are unkeyed, not protected dockets.
                self.assertEqual(result['chapters'][1]['protected'], 38 + int(rematch))
                self.assertEqual(result['chapters'][1]['dynamic'], 3)
                for chapter in result['chapters']:
                    self.assertLessEqual(chapter['load'], 1.0)
                    by_hour = {}
                    for hour, allowance, ref in chapter['slots']:
                        by_hour[hour, allowance] = by_hour.get((hour, allowance), 0) + 1
                    self.assertTrue(all(count <= (1 if key in ('household.pair', None) else 2)
                                        for (_, key), count in by_hour.items()))

    def test_missing_native_walk_cannot_be_reported_as_a_reachability_proof(self):
        result = sim.simulate(self.story, self.data, self.route_run)
        self.assertFalse(result['conditional'])
        self.assertTrue(result['blocked'])
        self.assertFalse(result['pair_complete'])

    def test_walk_eligibility_times_and_named_gates_control_deadlines(self):
        arrivals = {rel: 0 for rel in self.story['Relationships']}
        arrivals.update({woman: 0 for woman in self.data['seat_women']})
        start5 = sum(self.route_run['chapter_days'].get(ch, 0) * 24 for ch in range(5))
        arrivals['wenduag'] = start5 + 24 * 39
        gates = {flag: 0 for row in self.data['schedule'] for flag in row.get('reads', [])}
        result = sim.simulate(self.story, self.data, self.route_run, arrivals=arrivals, gate_hours=gates)
        self.assertEqual(result['pair_eligibility'], arrivals['wenduag'])
        self.assertFalse(result['pair_complete'])
        self.assertNotIn('S02.morning', result['completed'])

    def test_packet_fallback_and_late_s06_are_counted_without_retired_s46(self):
        result = sim.simulate(self.story, self.data, self.route_run, conditional=True, fallback=True, late_s06=True)
        self.assertIn('S06.ack', result['completed'])
        self.assertNotIn('S46', result['completed'])
        self.assertGreater(result['chapters'][1]['protected'], 41)

    def test_corrupted_roster_uses_its_own_docket_on_both_s02_paths(self):
        for rematch in (False, True):
            with self.subTest(rematch=rematch):
                result = sim.simulate(self.story, self.data, self.route_run, conditional=True,
                                      rematch=rematch, arueshalae_state='corrupted')
                self.assertTrue(result['pair_complete'])
                self.assertEqual(result['arueshalae_state'], 'corrupted')
                self.assertIn('S03b', result['completed'])
                self.assertEqual(result['chapters'][1]['protected'], 39 + int(rematch))
                self.assertEqual(result['blocked'], [])
                for chapter in result['chapters']:
                    self.assertEqual(chapter['deadline_misses'], [])
                    self.assertLessEqual(chapter['load'], 1.0)
