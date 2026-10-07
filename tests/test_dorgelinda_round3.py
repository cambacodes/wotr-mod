"""Disclosure histories: people, batched receipts, and two later additions."""
import copy
import unittest

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
        flags = {f for f in flags if not f.startswith((L + 'undisclosed.', L + 'disclosure_dispatch.')) and f != L + 'new_columns'}
        for key, groups in self.payload['Derived'].items():
            if key.startswith(L + 'undisclosed.'):
                if any(set(g) <= flags for g in groups) and not set(self.payload['DerivedForbids'].get(key, [])) & flags:
                    flags.add(key)
        for key, groups in self.payload['Derived'].items():
            if key.startswith(L + 'disclosure_dispatch.'):
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
            self.assertLess(len(pages), len(REACTIONS))
            replies = [node['Text'] for node in self.by[sid]['Nodes'] if node['Id'].startswith('named.')]
            self.assertEqual(len(replies), len(set(replies)))
            self.assertFalse(any('Your time with her is yours to arrange' in text for text in replies))

    def test_routine_names_are_batched_without_invented_receipts(self):
        from storylines.dorgelinda_round3 import EXPLANATIONS
        actual = ('anevia', 'irabeth', 'seelah', 'konomi')
        flags = {'trickster.ever'} | {L + 'current_other.' + r for r in actual}
        final, named, pages, _ = self.disclose(ledger.OTHERS, flags)
        self.assertEqual(set(named), set(actual))
        self.assertLess(len(pages), len(actual))
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


if __name__ == '__main__':
    unittest.main()
