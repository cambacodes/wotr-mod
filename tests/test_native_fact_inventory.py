"""E-Q7-10 real archive evidence, export contract and mutation acceptance."""
from tests.story_fixture import fresh_story
import copy
import json
from pathlib import Path
import unittest
from itertools import zip_longest
from tests.structure import without_prose
from unittest.mock import patch
import expansion
from storylines import native_facts
from tools.native_fact_inventory import EXPECTATIONS, verify_inventory

class NativeFactInventoryTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        cls.spec = json.loads(EXPECTATIONS.read_text(encoding="utf-8"))

    def test_each_mapped_finding_has_current_evidence(self):
        backlog = json.loads(Path('tools/engine_backlog.json').read_text(encoding="utf-8"))
        expected = {f['id'] for f in backlog['findings'] if f.get('item_id') == 'E-Q7-10'}
        self.assertEqual(expected, {f['id'] for f in self.spec['findings']})
        scenes = {s['Id']: s for s in self.payload['Scenes']}
        for row in self.spec['findings']:
            self.assertTrue(row['evidence'])
            if row['id'] in {'nenio:038', 'nenio:039'}:
                self.assertNotIn(row['scene'], scenes)
            elif row['id'] == 'devarra:001':
                scene = scenes[row['scene']]
                self.assertFalse(any(n['Id'] == 'failed' or 'eggs.destroyed' in str(without_prose(n)) for n in scene['Nodes']))
            elif row['id'] == 'eritrice:013':
                handled = next(n for n in scenes[row['scene']]['Nodes'] if n['Id'] == 'handled')
                self.assertFalse(any(c.get('Crusade') for c in handled['Choices']))

    def test_native_producer_and_reader_contract(self):
        verify_inventory(self.payload)
        native_facts.verify()
        for row in self.spec['cases']:
            # Fixtures cannot seed the outcomes they are intended to test.
            self.assertTrue(set(row['observations']) <= {'Etudes', 'CompletedEtudes', 'SeenCues', 'SelectedAnswers', 'StartedDialogs', 'CompletedQuests', 'QuestObjectives'})
            for inputs in row['observations'].values():
                self.assertTrue(all(len(value.split(':')[0]) == 32 for value in inputs))

    def test_missing_or_changed_reader_and_lost_history_fail_acceptance(self):
        for witness in self.spec['witnesses']:
            bad = dict(self.payload)
            bad[witness['reader']] = dict(self.payload[witness['reader']])
            del bad[witness['reader']][witness['flag']]
            with self.subTest(witness=witness['flag']):
                with self.assertRaises(ValueError):
                    verify_inventory(bad)
        bad = copy.deepcopy(self.payload)
        bad['PermanentEtudes'].remove(native_facts.key('kaylessa.letter_sent'))
        with self.assertRaises(ValueError):
            verify_inventory(bad)

    def test_wrong_native_producer_path_or_late_window_fails(self):
        for mutate, message in ((lambda s: s['witnesses'][0]['sources'][0].update(guid='0' * 32), 'producer drift'), (lambda s: s['producer_requirements'][0].update(first_chapter=6), 'after consumer window'), (lambda s: s['producer_requirements'][0].pop('earned_alternative'), 'incompatible native path')):
            spec = copy.deepcopy(self.spec)
            mutate(spec)
            with self.assertRaises(ValueError):
                verify_inventory(self.payload, expectations=spec)
        bad = copy.deepcopy(self.payload)
        next((s for s in bad['Scenes'] if s['Id'] == 'minachiv.two_answers'))['Requires'].append('chivarro.searching')
        with self.assertRaises(ValueError):
            verify_inventory(bad)
        bad = copy.deepcopy(self.payload)
        bad['Derived']['minachiv.reunion_history'] = [['chivarro.searching']]
        with self.assertRaises(ValueError):
            verify_inventory(bad)

    def test_branch_helper_keeps_indices_targets_and_appends_neutral(self):
        original = dict(Id='entry', Text='entry', Choices=[dict(Text='one', Next='remember', Requires=[], Forbids=[], Set=['earned']), dict(Text='two', Next=None)])
        scene = dict(Nodes=[copy.deepcopy(original), dict(Id='remember', Text='memory', Choices=[dict(Text='done', Next=None)])])
        native_facts.history_variant(scene, 'remember', 'observed', 'neutral')
        entry = scene['Nodes'][0]
        self.assertEqual([c.get('Next') for c in entry['Choices'][:2]], ['remember', None])
        ordered_answer_1, *_ = entry['Choices']
        self.assertEqual(ordered_answer_1['Set'], ['earned'])
        ordered_answer_2, *_ = entry['Choices']
        self.assertEqual(ordered_answer_2['Next'], 'remember')
        _, _, ordered_answer_3, *_ = entry['Choices']
        self.assertEqual(ordered_answer_3['Set'], ['earned'])
        self.assertEqual(scene['Nodes'][1]['Id'], 'remember')
        self.assertEqual(scene['Nodes'][2]['Id'], 'remember.history_neutral')

    def test_export_retains_every_old_id_index_and_answer_target(self):
        with patch.object(native_facts, 'inventory_consumers', lambda payload: None), patch('tools.native_fact_inventory.verify_inventory', lambda payload, archive: None):
            before = expansion.make_expansion()
        after = self.payload['Scenes']
        old_ids = [s['Id'] for s in before['Scenes']]
        old_id_set = set(old_ids)
        self.assertEqual(old_ids, [s['Id'] for s in after if s['Id'] in old_id_set])
        after_by_id = {s['Id']: s for s in after}
        for old in before['Scenes']:
            new = after_by_id[old['Id']]
            with self.subTest(scene=old['Id']):
                self.assertEqual(old.get('Relationship'), new.get('Relationship'))
                self.assertTrue(all((new is not None and old['Id'] == new['Id'] for old, new in zip_longest(old['Nodes'], new['Nodes']) if old is not None)))
                for old_node, new_node in zip(old['Nodes'], new['Nodes']):
                    self.assertTrue(all((new is not None for old, new in zip_longest(old_node['Choices'], new_node['Choices']) if old is not None)))
                    for old_choice, new_choice in zip(old_node['Choices'], new_node['Choices']):
                        self.assertEqual(old_choice.get('Next'), new_choice.get('Next'))
                        self.assertEqual(old_choice.get('Set'), new_choice.get('Set'))
if __name__ == '__main__':
    unittest.main()
