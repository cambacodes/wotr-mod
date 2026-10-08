"""Disclosure histories: individual receipts and repeated later additions."""
import copy
import unittest
from unittest.mock import patch

from storylines import dorgelinda_ledger as ledger, dorgelinda_trickster as trickster
from tests.test_dorgelinda_polish import visible

L = ledger.L


class RoundThreeTests(unittest.TestCase):
    def setUp(self):
        self.payload = {'Scenes': copy.deepcopy(trickster.SCENES + ledger.SCENES)}
        trickster.integrate(self.payload)
        ledger.integrate(self.payload)
        self.by = {s['Id']: s for s in self.payload['Scenes']}

    def complete(self, flags):
        flags = {f for f in flags if not f.startswith((L + 'undisclosed.', L + 'disclosure_dispatch.',
                 L + 'disclosure_prefix.', L + 'next_disclosure.')) and f != L + 'new_columns'}
        for key, groups in self.payload['Derived'].items():
            if key.startswith(L + 'undisclosed.'):
                if any(set(g) <= flags for g in groups) and not set(self.payload['DerivedForbids'].get(key, [])) & flags:
                    flags.add(key)
        for key, groups in self.payload['Derived'].items():
            if key.startswith((L + 'disclosure_prefix.', L + 'next_disclosure.')):
                if any(set(g) <= flags for g in groups) and not set(self.payload['DerivedForbids'].get(key, [])) & flags:
                    flags.add(key)
        for key, spec in self.payload.get('Counts', {}).items():
            if sum(source in flags for source in spec['Of']) >= spec['Min']:
                flags.add(key)
        return flags

    def disclose(self, sid, flags):
        flags = self.complete(flags)
        self.disclosure_answers = []
        nodes = {n['Id']: n for n in self.by[sid]['Nodes']}
        current, named, pages = 'disclosure.0', [], []
        while current != 'shaken':
            self.assertNotIn(current, pages)
            pages.append(current)
            choices = [a for a in nodes[current]['Choices'] if visible(a, flags)]
            self.assertEqual(len(choices), 1, (sid, current, sorted(flags)))
            answer = choices[0]
            self.disclosure_answers.append(answer['Text'])
            named.extend(f[len(L + 'disclosed.'):] for f in answer['Set'] if f.startswith(L + 'disclosed.'))
            flags.update(answer['Set'])
            flags = self.complete(flags)
            current = answer['Next']
            if current == 'disclosure.cold':
                cold = next(a for a in nodes[current]['Choices'] if visible(a, flags))
                flags.update(cold['Set'])
                return flags, named, pages, cold['Abort']
        last = next(a for a in nodes[current]['Choices'] if visible(a, flags))
        flags.update(last['Set'])
        if not last['Abort']:
            flags.add(sid)
        return flags, named, pages, last['Abort']

    def test_pair_and_individual_entitlements_name_each_woman_once(self):
        flags = {'trickster.ever'} | {L + 'current_other.' + r for r in ('tirabade', 'anevia', 'irabeth')}
        _, named, _, _ = self.disclose(ledger.OTHERS, flags)
        self.assertEqual(named, ['tirabade', 'anevia', 'irabeth'])
        spoken = ' '.join(self.disclosure_answers)
        self.assertEqual(spoken.count('Anevia'), 1)
        self.assertEqual(spoken.count('Irabeth'), 1)

    def test_every_partner_has_one_receipt_and_a_distinct_judgment(self):
        from storylines.dorgelinda_round3 import REACTIONS
        flags = {'trickster.ever'} | {L + 'current_other.' + r for r in REACTIONS}
        for sid in (ledger.OTHERS, L + 'changed_columns'):
            _, named, pages, _ = self.disclose(sid, flags)
            self.assertEqual(set(named), set(REACTIONS))
            self.assertEqual(len(named), len(set(named)))
            self.assertEqual(len(pages), len(REACTIONS))  # pair suppresses two individual replies
            replies = [node['Text'] for node in self.by[sid]['Nodes'] if node['Id'].startswith('named.')]
            self.assertEqual(len(replies), len(set(replies)))
            self.assertFalse(any('Your time with her is yours to arrange' in text for text in replies))

    def test_routine_names_have_individual_answers_without_invented_receipts(self):
        from storylines.dorgelinda_round3 import EXPLANATIONS
        actual = ('anevia', 'irabeth', 'seelah', 'konomi')
        flags = {'trickster.ever'} | {L + 'current_other.' + r for r in actual}
        final, named, pages, _ = self.disclose(ledger.OTHERS, flags)
        self.assertEqual(set(named), set(actual))
        self.assertEqual(len(pages), len(actual) + 2)  # entry and final judgment
        self.assertEqual(len([a for a in self.disclosure_answers if a.startswith('[Explain')]), len(actual))
        self.assertFalse(any(L + 'disclosed.' + r in final for r in EXPLANATIONS))

    def test_two_additions_after_solo_and_initial_shared_arrangements(self):
        for initial in ('sole_line', 'terms_kept'):
            flags = {'trickster.ever', 'dorgelinda.present_now', trickster.COMMITTED,
                     L + initial, L + 'current_other.seelah'}
            if initial == 'terms_kept':
                flags.add(L + 'disclosed.seelah')
                flags.add(L + 'current_other.kiana')
            flags, named, _, _ = self.disclose(L + 'changed_columns', flags)
            self.assertEqual(named, ['seelah'] if initial == 'sole_line' else ['kiana'])
            for rel in ('galfrey', 'areelu'):
                flags.add(L + 'current_other.' + rel)
                self.assertTrue(visible(self.by[L + 'changed_columns'], self.complete(flags)))
                flags, named, _, abort = self.disclose(L + 'changed_columns', flags)
                self.assertEqual(named, [rel])
                self.assertTrue(abort)
                self.assertNotIn(L + 'changed_columns', flags)
                self.assertNotIn(L + 'new_columns', self.complete(flags))

    def test_cold_disclosure_keeps_the_existing_quarrel(self):
        for cold in ({L + 'quarrel_cold'}, {L + 'quarrel_unmended'}):
            flags = {'trickster.ever', L + 'current_other.areelu'} | cold
            after, _, pages, _ = self.disclose(L + 'changed_columns', flags)
            self.assertNotIn('shaken', pages)
            self.assertNotIn(L + 'quarrel_mended', after)
            self.assertTrue(cold <= after)

    def test_extraordinary_explanations_and_judgments_differ_on_return(self):
        from storylines.dorgelinda_round3 import EXPLANATIONS
        for rel, explanation in EXPLANATIONS.items():
            texts = []
            for sid in (ledger.OTHERS, L + 'changed_columns'):
                nodes = {n['Id']: n for n in self.by[sid]['Nodes']}
                flags = self.complete({'trickster.ever', L + 'current_other.' + rel})
                choice = [a for a in nodes['disclosure.0']['Choices'] if visible(a, flags)][0]
                self.assertEqual(choice['Text'], explanation)
                texts.append(nodes[choice['Next']]['Text'])
                self.assertNotEqual(nodes['named.' + rel]['Text'], '"Aye."')
            self.assertNotEqual(*texts)

    def test_generated_capitalization(self):
        page = next(n for n in self.by[L + 'carried_forward']['Nodes'] if n['Id'] == 'paid')
        self.assertIn("and they're not", page['Text'])
        self.assertNotIn("and They're", page['Text'])

    def test_disclosure_predicates_are_linear_and_have_no_dispatch_counts(self):
        from storylines.dorgelinda_round3 import REACTIONS
        readers = [k for k in self.payload['Derived'] if k.startswith(L + 'undisclosed.')]
        self.assertEqual(len(readers), len(REACTIONS))
        for field in ('Derived', 'DerivedForbids', 'Counts'):
            self.assertFalse(any(k.startswith(L + 'disclosure_dispatch.') for k in self.payload[field]))
        prefixes = {k: groups for k, groups in self.payload['Derived'].items()
                    if k.startswith(L + 'disclosure_prefix.')}
        selectors = {k: groups for k, groups in self.payload['Derived'].items()
                     if k.startswith(L + 'next_disclosure.')}
        self.assertEqual(len(prefixes), len(REACTIONS))
        self.assertEqual(len(selectors), len(REACTIONS) + 1)
        self.assertTrue(all(len(groups) <= 2 and all(len(g) == 1 for g in groups) for groups in prefixes.values()))
        self.assertTrue(all(len(groups) == 1 and len(groups[0]) == 1 for groups in selectors.values()))
        self.assertTrue(all(len(self.payload['DerivedForbids'].get(k, [])) <= 1 for k in selectors))
        for sid in (ledger.OTHERS, L + 'changed_columns'):
            entry = next(n for n in self.by[sid]['Nodes'] if n['Id'] == 'disclosure.0')
            retained = [a for a in entry['Choices'] if (a.get('Next') or '').startswith('disclosure.batch.')]
            self.assertEqual(len(retained), 7)
            self.assertTrue(all('trickster.ever' in a['Forbids'] for a in retained))

    def test_pre_round_three_nodes_and_choice_references_stay_in_place(self):
        before = {'Scenes': copy.deepcopy(trickster.SCENES + ledger.SCENES)}
        with patch('storylines.dorgelinda_round3.integrate'):
            trickster.integrate(before)
            ledger.integrate(before)
        for old_scene in before['Scenes']:
            if old_scene['Id'] not in (ledger.OTHERS, L + 'changed_columns'):
                continue
            new_nodes = self.by[old_scene['Id']]['Nodes']
            old_ids = [node['Id'] for node in old_scene['Nodes']]
            self.assertEqual([node['Id'] for node in new_nodes if node['Id'] in old_ids], old_ids)
            by = {node['Id']: node for node in new_nodes}
            for old in old_scene['Nodes']:
                new = by[old['Id']]
                self.assertGreaterEqual(len(new['Choices']), len(old['Choices']))
                for index, answer in enumerate(old['Choices']):
                    self.assertEqual(new['Choices'][index]['Next'], answer['Next'])
                    self.assertEqual(new['Choices'][index]['Set'], answer['Set'])

    def test_sparse_histories_always_have_exactly_one_next_answer(self):
        import random
        from storylines.dorgelinda_round3 import REACTIONS
        rng = random.Random(731)
        for _ in range(80):
            current = {r for r in REACTIONS if rng.randrange(2)}
            disclosed = {r for r in REACTIONS if rng.randrange(2)}
            flags = {'trickster.ever'} | {L + 'current_other.' + r for r in current}
            flags |= {L + 'disclosed.' + r for r in disclosed}
            _, named, _, _ = self.disclose(ledger.OTHERS, flags)
            expected = current - disclosed
            if 'tirabade' in current or 'tirabade' in disclosed:
                expected -= {'anevia', 'irabeth'}
            if 'tirabade' in expected:
                expected |= {'anevia', 'irabeth'}
            self.assertEqual(set(named), expected)


if __name__ == '__main__':
    unittest.main()
