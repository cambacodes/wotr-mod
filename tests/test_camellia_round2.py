"""Camellia situation continuity and legacy-save regression checks."""
import copy
import json
from pathlib import Path
import unittest
from storylines import camellia_trickster as ct, camellia_masks, camellia_evenings, camellia_cards, camellia_days, camellia_last, camellia_native, camellia_intimate_aftermath
from tools import savecompat

class CamelliaRound2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.before = {'Scenes': copy.deepcopy(ct.SCENES + camellia_native.SCENES), 'Derived': {}}
        cls.after = copy.deepcopy(cls.before)
        camellia_intimate_aftermath.integrate(cls.after)
        cls.scenes = {s['Id']: s for s in cls.after['Scenes']}

    def node(self, sid, nid):
        return next((n for n in self.scenes[ct.P + sid]['Nodes'] if n['Id'] == nid))

    def test_all_legacy_references_and_ending_exit_effects_survive(self):
        self.assertEqual([], savecompat.check(self.after, savecompat.inventory(self.before)))
        for old in self.before['Scenes']:
            if old['Owner'].endswith('Epilogue'):
                new = self.scenes[old['Id']]
                for original, current in zip(old['Nodes'], new['Nodes']):
                    self.assertEqual(original['Choices'], current['Choices'])

    def test_slots_are_reachable_and_keep_each_branch_successor(self):
        from tests.story_fixture import fresh_story
        from tests.fix16b_structure import declared_host, reachable_nodes
        scenes = {s['Id']: s for s in fresh_story()['Scenes']}
        root = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/camellia'
        for path in root.glob('*.json'):
            brief = json.loads(path.read_text(encoding='utf-8'))
            sid, nid = declared_host(path.stem, brief, scenes)
            with self.subTest(slot=brief['slot_id'], host=nid):
                host = scenes[sid]
                pages = {n['Id']: n for n in host['Nodes']}
                self.assertIn(nid, reachable_nodes(host))
                if 'insertion' not in brief:
                    continue
                slot = pages[nid]
                self.assertEqual([[]], [c['Set'] for c in slot['Choices']])
                successor = brief['insertion']['retained_successor'].split(' -> ')[-1]
                self.assertEqual(['end' if 'the_second_dance' in sid else successor], [c['Next'] for c in slot['Choices']])
                anchor = brief['insertion']['after_node']
                if 'the_second_dance' in sid:
                    anchor = 'strap' if brief['slot_id'].endswith('.1') else 'leave'
                    ordered_answer_1, *ordered_answer_1_rest = pages[anchor]['Choices']
                    flags = set(ordered_answer_1['Set'])
                    self.assertEqual([successor], [c['Next'] for c in pages['morning.dance']['Choices'] if set(c['Requires']) <= flags and (not set(c['Forbids']) & flags)])
                self.assertIn(nid, [c['Next'] for c in pages[anchor]['Choices']])
                if 'the_deck_again' in sid:
                    self.assertEqual([None], [c['Next'] for c in pages['wont_close']['Choices']])

    def test_first_coffin_delivery_does_not_need_placement_failure(self):
        for sid, terminal in (('killed.third_night', 'home'), ('killed.late_curtain', 'walk')):
            answers = self.node(sid, terminal)['Choices']
            self.assertTrue(any((c.get('Next') == 'eng8.reunion' and ct.PRESENCE_FAILED not in c['Requires'] for c in answers)))
            for answer in self.node(sid, 'eng8.price')['Choices'][:2]:
                self.assertEqual('r2.stones', answer['Next'])
                self.assertIn(ct.TERMS, answer['Set'])
            ordered_answer_2, *ordered_answer_2_rest = self.node(sid, 'r2.stones')['Choices']
            self.assertIn(ct.FILLED, ordered_answer_2['Set'])

    def test_existing_charges_precede_irreversible_consequences(self):
        ordered_answer_3, *ordered_answer_3_rest = self.node('killed.third_night', 'start')['Choices']
        self.assertEqual(-100, ordered_answer_3['Crusade']['Amount'])
        for suffix in ('', '_camp', '_alive'):
            host = self.scenes[ct.P + 'day.a_new_friend' + suffix]
            for page in host['Nodes']:
                for answer in page['Choices']:
                    if answer.get('Next') == 'warn':
                        self.assertEqual({'Resource': 'Favors', 'Amount': -100}, answer['Crusade'])
            ordered_answer_4, *ordered_answer_4_rest = self.node('day.a_new_friend' + suffix, 'warn')['Choices']
            self.assertNotIn('Crusade', ordered_answer_4)

    def test_prices_and_confessions_are_collected_not_inferred_from_a_kiss(self):
        for suffix in ('', '_camp', '_alive'):
            self.assertEqual([ct.P + 'mireya_disclosed'], self.node('cards.the_amulet' + suffix, 'tell')['EnterSet'])
            ordered_answer_5, *ordered_answer_5_rest = self.node('evening.breakfast' + suffix, 'r2.public_paid')['Choices']
            self.assertIn(ct.P + 'encounter.all.public_paid', ordered_answer_5['Set'])
            ordered_answer_6, *ordered_answer_6_rest = self.node('bond.witness' + suffix, 'r2.public_after')['Choices']
            self.assertIn(ct.P + 'bond.witness_public', ordered_answer_6['Set'])
            ordered_answer_7, *ordered_answer_7_rest = self.node('bond.witness' + suffix, 'hers')['Choices']
            self.assertIn(ct.WITNESS_HERS, ordered_answer_7['Set'])
        paragraphs = self.node('epilogue.commit', 'page')['Paragraphs']
        for flag in (ct.BLED, ct.MARKED):
            accounts = [p for p in paragraphs if flag in p.get('Requires', ())]
            self.assertTrue(accounts)
            self.assertTrue(all(flag in p['Requires'] for p in accounts))

    def test_geography_current_path_and_refusal(self):
        for sid in ('cards.a_bowl_for_mireya', 'beat.spirits_due'):
            self.assertEqual([3, 5], self.scenes[ct.P + sid]['Chapters'])
        for sid in ('epilogue.kept', 'epilogue.kept_on_record', 'epilogue.commit', 'epilogue.commit_on_record'):
            self.assertIn('trickster.now', self.scenes[ct.P + sid]['Requires'])
        self.assertNotIn(ct.RET, self.scenes[ct.P + 'epilogue.refused']['Requires'])
        self.assertIn('sacrifice', self.scenes[ct.P + 'epilogue.refused']['Forbids'])

    def test_either_resurrection_debt_reads_without_requiring_both(self):
        for sid in ('epilogue.kept', 'epilogue.kept_on_record', 'epilogue.commit', 'epilogue.commit_on_record'):
            paragraphs = self.node(sid, 'page')['Paragraphs']
            self.assertTrue(any((p.get('AnyGroups') == [[ct.OWED, ct.BARGAIN_COST]] for p in paragraphs)))

    def test_one_current_victim_suffices_for_oath_without_summoning_departed_women(self):
        key = ct.P + 'kills_answered.present_victim'
        groups = self.after['Derived'][key]
        self.assertEqual({'nurah.present_now', 'soana.present_now', 'kaylessa.present_now'}, {g[0] for g in groups})
        for group in groups:
            self.assertTrue(any((all((flag in set(group) for flag in candidate)) for candidate in groups)))
            self.assertFalse(any((all((flag in {group[1]} for flag in candidate)) for candidate in groups)))
        for suffix in ('', '_camp'):
            self.assertIn(key, self.scenes[ct.P + 'kills_answered.oath' + suffix]['Requires'])
            self.assertFalse(self.scenes[ct.P + 'kills_answered.oath' + suffix].get('RequiresAnyGroups'))
if __name__ == '__main__':
    unittest.main()
