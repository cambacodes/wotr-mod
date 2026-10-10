"""Round-2 debt, branch-exit and append-only checks on the authored route."""
import copy
import json
import unittest
from storylines import chivarro_setpieces as polish
from storylines import minagho_chivarro_continuation as continuation
from storylines import minagho_chivarro_stance as stance
from storylines import minagho_chivarro_trickster as trickster

class ChivarroSetpieceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': copy.deepcopy(continuation.SCENES + trickster.SCENES)}
        stance.integrate(payload)
        cls.before = copy.deepcopy(payload)
        polish.integrate(payload)
        cls.pages = {page['Id']: page for page in payload['Scenes']}

    def nodes(self, suffix):
        return {node['Id']: node for node in self.pages[polish.P + suffix]['Nodes']}

    def test_merged_rounds_preserve_inserts_and_public_reckoning(self):
        from storylines import minagho_round2
        from storylines import lastcall_partners
        saved = copy.deepcopy(lastcall_partners.PARTNERS)
        try:
            payload = {'Scenes': copy.deepcopy(continuation.SCENES + trickster.SCENES)}
            stance.integrate(payload)
            minagho_round2.integrate(payload)
            before = copy.deepcopy(payload['Scenes'])
            polish.integrate(payload)
            pages = {page['Id']: page for page in payload['Scenes']}
            for original in before:
                revised = pages[original['Id']]
                ids = [node['Id'] for node in revised['Nodes']]
                self.assertEqual(len(ids), len(set(ids)))
                self.assertEqual([node['Id'] for node in original['Nodes']], [new_id for old_node, new_id in zip(original['Nodes'], ids)])
            page = pages[polish.P + 'after.the_price_of_her_name_letter']
            nodes = {node['Id']: node for node in page['Nodes']}
            ordered_answer_1, *ordered_answer_1_rest = nodes['start']['Choices']
            self.assertEqual(ordered_answer_1['Next'], 'reckoning_receipt')
            ordered_answer_2, *ordered_answer_2_rest = nodes['reckoning_receipt']['Choices']
            self.assertEqual(ordered_answer_2['Next'], 'verdict_paid')
            ordered_answer_3, *ordered_answer_3_rest = nodes['start']['Choices']
            self.assertEqual(ordered_answer_3['Set'], [])
            ordered_answer_4, *ordered_answer_4_rest = nodes['verdict_paid']['Choices']
            self.assertEqual(set(ordered_answer_4['Set']), {trickster.T_NAME, trickster.PALM_TABLE})
            clean = pages[polish.P + 'alone.chivarro']
            clean_nodes = {node['Id']: node for node in clean['Nodes']}
            ordered_answer_5, *ordered_answer_5_rest = clean_nodes['threshold_clean']['Choices']
            insert = clean_nodes[ordered_answer_5['Next']]
            self.assertIn('.explicit.', insert['Id'])
            ordered_answer_6, *ordered_answer_6_rest = insert['Choices']
            self.assertEqual(ordered_answer_6['Set'], [])
            ordered_answer_7, *ordered_answer_7_rest = insert['Choices']
            self.assertIsNone(ordered_answer_7['Next'])
            wardrobe = pages[polish.P + 'reunion.wardrobe']
            wardrobe_nodes = {node['Id']: node for node in wardrobe['Nodes']}
            for identity in ('which', 'which_debt'):
                for answer in wardrobe_nodes[identity]['Choices']:
                    if polish.P + 'chivarro_sent_back' in answer['Set']:
                        self.assertEqual(answer['Next'], 'departure_answer')
                    elif polish.P + 'chivarro_in' in answer['Set']:
                        self.assertNotIn(answer['Next'], ('departure_answer', 'chivarro_leaves'))
            ordered_answer_8, *ordered_answer_8_rest = wardrobe_nodes['departure_answer']['Choices']
            self.assertEqual(ordered_answer_8['Next'], 'chivarro_leaves')
        finally:
            lastcall_partners.PARTNERS[:] = saved

    def terminal(self, page, answer):
        nodes = {node['Id']: node for node in page['Nodes']}
        target = answer['Next']
        seen = set()
        while target and '.explicit.' in target:
            if target in seen:
                raise AssertionError('Invalid replay traversal')
            seen.add(target)
            choices = nodes[target]['Choices']
            dispatch_9, = choices
            answer_in_order_1, *answer_in_order_1_following = choices
            target = answer_in_order_1['Next']
        return target

    def test_saved_scene_node_order_and_choice_effects(self):
        for before in self.before['Scenes']:
            after = self.pages[before['Id']]
            self.assertEqual([x['Id'] for x in before['Nodes']], [x['Id'] for x in [new_node for old_node, new_node in zip(before['Nodes'], after['Nodes'])]])
            for old, new in zip(before['Nodes'], after['Nodes']):
                self.assertEqual([a.get('Abort') for a in old['Choices']], [b.get('Abort') for a, b in zip(old['Choices'], new['Choices'])])
                for index, (answer, revised) in enumerate(zip(old['Choices'], new['Choices'])):
                    if (before['Id'], old['Id'], index) == (polish.P + 'after.the_price_of_her_name_letter', 'start', 0):
                        self.assertEqual(revised['Set'], [])
                        ordered_answer_10, *ordered_answer_10_rest = self.nodes('after.the_price_of_her_name_letter')['verdict_paid']['Choices']
                        self.assertEqual(ordered_answer_10['Set'], answer['Set'])
                    elif answer['Next'] is None and '.explicit.' in (revised['Next'] or ''):
                        self.assertEqual(revised['Set'], [])
                        reached = {x['Id']: x for x in after['Nodes']}[revised['Next']]
                        ordered_answer_11, *ordered_answer_11_rest = reached['Choices']
                        ordered_answer_12, *ordered_answer_12_rest = reached['Choices']
                        if ordered_answer_11['Next'] and ordered_answer_12['Next'].endswith('.after'):
                            ordered_answer_13, *ordered_answer_13_rest = reached['Choices']
                            reached = {x['Id']: x for x in after['Nodes']}[ordered_answer_13['Next']]
                        ordered_answer_14, *ordered_answer_14_rest = reached['Choices']
                        self.assertEqual(ordered_answer_14['Set'], answer['Set'])
                    else:
                        self.assertEqual(answer['Set'], revised['Set'])
                    for key in ('Abort', 'Revive', 'Alignment', 'StartEtude', 'RemoveItem'):
                        self.assertEqual(answer.get(key), revised.get(key))

    def test_slots_do_not_merge_secret_discovery_exits_or_pay_twice(self):
        installed = 0
        for before in self.before['Scenes']:
            after = self.pages[before['Id']]
            for old, new in zip(before['Nodes'], after['Nodes']):
                if not any(('.explicit.' in (a['Next'] or '') for a in new['Choices'])):
                    continue
                for answer, revised in zip(old['Choices'], new['Choices']):
                    if len(new['Choices']) == 1:
                        self.assertEqual(self.terminal(after, revised), answer['Next'])
                installed += 1
            for node in after['Nodes']:
                if '.explicit.' in node['Id']:
                    for answer in node['Choices']:
                        if answer['Next'] is not None:
                            self.assertEqual(answer['Set'], [])
                        self.assertNotIn('Crusade', answer)
        self.assertGreater(installed, 15)

    def test_epilogue_contract_paragraph_ordinals_stay_in_place(self):
        for before in self.before['Scenes']:
            after = self.pages[before['Id']]
            for old, new in zip(before['Nodes'], after['Nodes']):
                original = old.get('Paragraphs', [])
                revised = new.get('Paragraphs', [])
                fields = ('Requires', 'Forbids', 'AnyGroups')
                self.assertEqual([[p.get(k) for k in fields] for p in original], [[current.get(k) for k in fields] for prior, current in zip(original, revised)])

    def test_earned_commitment_locks_out_conflicting_second_chain(self):
        continuation_pages = [page for page in self.pages.values() if page['Id'].startswith('minachiv.') and (not page['Owner'].endswith('Epilogue'))]
        self.assertTrue(continuation_pages)
        self.assertTrue(all((trickster.CHAIN in page['Forbids'] for page in continuation_pages)))
        for suffix in ('after.before_the_last_road', 'alone.chivarro', 'alone.chivarro_letter'):
            self.assertIn(trickster.COMPLETE, self.pages[polish.P + suffix]['Forbids'])

    def test_letter_and_secret_dawn_pay_same_housing_rent_once(self):
        for suffix in ('alone.chivarro_letter', 'alone.chivarro_morning'):
            nodes = self.nodes(suffix)
            paying = [a for node in nodes.values() if node['Id'] != 'haggle' for a in node['Choices'] if stance.P + 'cost.morning_after' in a['Set']]
            self.assertTrue(paying)
            self.assertTrue(all((a['Crusade'] == {'Resource': 'Finances', 'Amount': -100} for a in paying)))
        nodes = self.nodes('alone.chivarro_when_it_scars')
        ordered_answer_15, *ordered_answer_15_rest = nodes['start']['Choices']
        ordered_answer_16_prior_0, ordered_answer_16, *ordered_answer_16_rest = nodes['chv']['Choices']
        self.assertEqual(ordered_answer_15['Crusade']['Amount'] + ordered_answer_16['Crusade']['Amount'], 0)
        ordered_answer_17_prior_0, ordered_answer_17, *ordered_answer_17_rest = nodes['start']['Choices']
        self.assertNotIn('Crusade', ordered_answer_17)

    def test_letter_rebuke_collects_actual_meeting_not_palm_print(self):
        nodes = self.nodes('after.the_price_of_her_name_letter')
        ordered_answer_18, *ordered_answer_18_rest = nodes['start']['Choices']
        self.assertEqual(ordered_answer_18['Next'], 'verdict_paid')
        ordered_answer_19, *ordered_answer_19_rest = nodes['start']['Choices']
        self.assertEqual(ordered_answer_19['Set'], [])
        ordered_answer_20, *ordered_answer_20_rest = nodes['verdict_paid']['Choices']
        self.assertEqual(set(ordered_answer_20['Set']), {trickster.T_NAME, trickster.PALM_TABLE})

    def test_installed_defaults_match_briefs_and_minagho_only_stays_owned(self):
        for path in polish.BRIEFS.glob('*.json'):
            brief = json.loads(path.read_text(encoding='utf-8'))
            sid = brief['slot_id'].split('.explicit.')[0]
            ids = {node['Id']: node for node in self.pages[sid]['Nodes']}
            ids.update({para['Id']: para for node in self.pages[sid]['Nodes'] for para in node.get('Paragraphs', []) if 'Id' in para})
            sources = brief.get('source_nodes') or [brief['source']['node']]
            held = '.alone.minagho' in sid or all(('minagho' in x for x in sources))
            if held:
                self.assertNotIn(brief['slot_id'], ids)
if __name__ == '__main__':
    unittest.main()
