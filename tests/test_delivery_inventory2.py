"""E-Q8-07: coverage and mutation checks for shipped delivery contracts."""
from tests.story_fixture import fresh_story
import copy
import json
from pathlib import Path
import unittest
from tools import remote_allocation_lint as allocation
from tools import timeline_contract_lint as timeline

class DeliveryInventory2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from expansion import make_expansion
        cls.story = fresh_story()
        cls.contracts = json.loads(allocation.DELIVERY_INVENTORY.read_text(encoding='utf-8'))

    def scene_variant(self, scene_id):
        story = dict(self.story, Scenes=list(self.story['Scenes']))
        index = next((i for i, s in enumerate(story['Scenes']) if s['Id'] == scene_id))
        changed = copy.deepcopy(story['Scenes'][index])
        story['Scenes'][index] = changed
        return (story, changed)

    def test_scene_variants_cannot_poison_later_mutations(self):
        physical = next((row['scene'] for row in self.contracts['sites'] if row.get('physical')))
        changed, scene = self.scene_variant(physical)
        scene['ContactUnit'] = None
        self.assertTrue(allocation.delivery_inventory(changed))
        self.assertEqual(allocation.delivery_inventory(self.story), [])
        from tools import return_provenance_lint as provenance
        sid = next(iter(provenance.contracts()['eng8-q8d']['coffin_completion_nodes']))
        changed, scene = self.scene_variant(sid)
        ordered_answer_1, *ordered_answer_1_rest = scene['Nodes'][0]['Choices']
        ordered_answer_1['Set'].append(provenance.contracts()['completed'])
        self.assertTrue(provenance.check(changed))
        self.assertEqual(provenance.check(self.story), [])

    def test_every_mapped_finding_has_a_positive_delivered_history(self):
        findings = self.contracts['findings']
        expected = {'camellia': [72, 73], 'galfrey': list(range(13, 24)) + [89, 90], 'horzalah': [21, 22, 23, 24, 31], 'nenio': [23], 'terendelev': [88, 89], 'wenduag': [42, 43, 44, 65]}
        self.assertCountEqual([f'{route}:{index:03}' for route, indices in expected.items() for index in indices], [row['finding'] for row in findings])
        self.assertEqual(allocation.delivery_inventory(self.story), [])
        self.assertEqual({h['character'].lower() for h in self.contracts['histories']}, set(expected))
        for h in self.contracts['histories']:
            self.assertFalse(h['expectedFailure'], h['name'])
            self.assertTrue(h['steps'], h['name'])
            for step in h['steps']:
                self.assertFalse(set(step) & {'flags', 'checkpoint', 'pre_age'}, h['name'])

    def test_retired_delivery_histories_cannot_hide_an_active_failure(self):
        contracts = copy.deepcopy(self.contracts)
        retired = contracts['retired_histories']
        self.assertEqual({h['name'] for h in retired}, {'wenduag-champion', 'wenduag-late-bid'})
        self.assertEqual(allocation.delivery_inventory(self.story, contracts), [])
        contracts['retired_histories'].append(contracts['histories'].pop(0))
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))
        contracts = copy.deepcopy(self.contracts)
        contracts['histories'].append(contracts['retired_histories'].pop(0))
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))
        story, scene = self.scene_variant('wenduag.trickster.exile.champion')
        scene['Forbids'].remove('trickster.ever')
        self.assertTrue(allocation.delivery_inventory(story))

    def test_physical_remote_manual_and_contact_mutations_fail(self):
        for row in self.contracts['sites']:
            if not row.get('physical'):
                continue
            for mutation in ('Remote', 'ManualOnly', 'ContactUnit'):
                story, scene = self.scene_variant(row['scene'])
                scene[mutation] = None if mutation == 'ContactUnit' else True
                self.assertTrue(allocation.delivery_inventory(story), (row['scene'], mutation))

    def test_unallocated_reactor_and_production_expected_failure_rejected(self):
        for sid in self.contracts['retired_reactors']:
            story, scene = self.scene_variant(sid)
            scene['Forbids'].remove('trickster.ever')
            self.assertTrue(allocation.delivery_inventory(story), sid)
        contracts = copy.deepcopy(self.contracts)
        contracts['histories'][0]['expectedFailure'] = True
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))
        contracts['histories'][0]['expectedFailure'] = False
        contracts['histories'][0]['steps'][0]['pre_age'] = 200
        self.assertTrue(allocation.delivery_inventory(self.story, contracts))

    def test_folded_coffin_provenance_is_scoped_and_requires_paid_ritual(self):
        from tools import return_provenance_lint as provenance
        self.assertEqual(provenance.check(self.story), [])
        for sid in provenance.contracts()['eng8-q8d']['coffin_completion_nodes']:
            story, scene = self.scene_variant(sid)
            scene['Requires'].remove('camellia.killed')
            self.assertTrue(provenance.check(story), sid)
            story, scene = self.scene_variant(sid)
            ordered_answer_2, *ordered_answer_2_rest = scene['Nodes'][0]['Choices']
            ordered_answer_2['Set'].append(provenance.contracts()['completed'])
            self.assertTrue(provenance.check(story), sid)

    def test_all_eight_character_limits_are_binding(self):
        contracts = json.loads(allocation.DEFAULT.read_text(encoding='utf-8'))
        for character in ('Camellia', 'Galfrey', 'Horzalah', 'Nenio', 'Terendelev', 'Wenduag'):
            changed = copy.deepcopy(contracts)
            row = next((a for a in changed['allocations'] if a['character'] == character))
            row['limits']['5'] += 1
            self.assertTrue(allocation.lint({'Scenes': []}, changed, [])['hard'], character)

    def test_cumulative_clock_rejects_missing_origin_reordering_and_overrun(self):
        history = dict(origin='coronation', maximum_hours=168, steps=[dict(hour=0, set=['coronation']), dict(hour=168, set=['yes'])])
        self.assertIsNone(timeline.delivered_timeline(history))
        history['steps'][-1]['hour'] = 174
        self.assertIn('exceeds', timeline.delivered_timeline(history))
        history['steps'][0]['set'] = []
        self.assertIn('missing', timeline.delivered_timeline(history))
        history['steps'][-1]['hour'] = -1
        self.assertIn('nonchronological', timeline.delivered_timeline(history))

    def test_entrance_fold_preserves_saved_choices_and_earned_gift(self):
        scenes = {s['Id']: s for s in self.story['Scenes']}
        for suffix, terminal in (('unmet.knife', 'exit'), ('late.at_night', 'no_priest')):
            scene = scenes['horzalah.trickster.' + suffix]
            end = next((n for n in scene['Nodes'] if n['Id'] == terminal))
            ordered_answer_3, *ordered_answer_3_rest = end['Choices']
            self.assertIn('chapter.six', ordered_answer_3['Forbids'])
            *answer_in_order_1_preceding, answer_in_order_1 = end['Choices']
            self.assertIn('chapter.six', answer_in_order_1['Requires'])
            *answer_in_order_2_preceding, answer_in_order_2 = end['Choices']
            self.assertTrue(answer_in_order_2['Next'].startswith('eng8.guild.'))
            self.assertTrue(any(('horzalah.trickster.tested' in c['Set'] for n in scene['Nodes'] if n['Id'].startswith('eng8.guild.') for c in n['Choices'])))
        self.assertEqual(scenes['horzalah.trickster.visit.chamber']['MaxChapter'], 5)
        self.assertEqual(scenes['terendelev.trickster.wound.weeps']['Chapters'], [3])
if __name__ == '__main__':
    unittest.main()
