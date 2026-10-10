"""Reviewed Dorgelinda polish: retained terms and exhaustive local dispatches."""
import copy
import itertools
import unittest
from storylines import dorgelinda_ledger as ledger
from storylines import dorgelinda_trickster as trickster
L = 'dorgelinda.ledger.'
P = 'dorgelinda.trickster.'
C, M, X, N, U = (L + key for key in ('quarrel_cold', 'quarrel_mended', 'quarrel_unmended', 'narrowed', 'unblessed'))
B = P + 'cost.boots_paid'

def visible(item, flags):
    return all((f in flags for f in item.get('Requires', ()))) and (not any((f in flags for f in item.get('Forbids', ())))) and all((any((f in flags for f in group)) for group in item.get('AnyGroups', ())))

class DorgelindaPolishTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': copy.deepcopy(trickster.SCENES + ledger.SCENES)}
        ledger.integrate(payload)
        cls.scenes = {scene['Id']: scene for scene in payload['Scenes']}

    def node(self, scene, node):
        return next((n for n in self.scenes[scene]['Nodes'] if n['Id'] == node))

    def histories(self, keys):
        for bits in itertools.product((False, True), repeat=len(keys)):
            yield {key for key, bit in zip(keys, bits) if bit}

    def choices(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices'] if visible(c, flags)]

    def cold(self, flags):
        return X in flags or (C in flags and M not in flags)

    def test_march_covers_all_64_histories_without_expanding_private_terms(self):
        scene = L + 'carried_forward'
        for flags in self.histories((B, C, M, X, N, U)):
            with self.subTest(flags=sorted(flags)):
                answers = self.choices(scene, 'boots', flags)
                dispatch_1, = answers
                answer_in_order_1, *answer_in_order_1_following = answers
                target = answer_in_order_1['Next']
                if B in flags:
                    self.assertEqual(target, 'paid')
                    answers = self.choices(scene, 'paid', flags)
                    dispatch_2, = answers
                    answer_in_order_2, *answer_in_order_2_following = answers
                    target = answer_in_order_2['Next']
                expected = 'choose_cold' if self.cold(flags) else 'choose_reserved' if N in flags else 'choose_private' if U in flags else 'choose'
                self.assertEqual(target, expected)
                last = self.choices(scene, target, flags)
                self.assertEqual(['receipt', 'kiss_cold' if self.cold(flags) else 'kiss_reserved' if N in flags else 'kiss_reserved_private' if U in flags else 'kiss', 'salute'], [a['Next'] for a in last])
                self.assertEqual([c['Next'] for c in last][::2], ['receipt', 'salute'])
                answer_in_order_3_before_0, answer_in_order_3, *answer_in_order_3_following = last
                kiss = self.node(scene, answer_in_order_3['Next'])
                ordered_answer_3, *ordered_answer_3_rest = kiss['Choices']
                self.assertEqual(ordered_answer_3['Next'], 'end')
                ordered_answer_4, *ordered_answer_4_rest = kiss['Choices']
                self.assertFalse(ordered_answer_4['Set'])
                self.assertEqual(kiss['Id'], 'kiss_cold' if self.cold(flags) else 'kiss_reserved' if N in flags else 'kiss_reserved_private' if U in flags else 'kiss')

    def test_council_and_postwar_dispatch_keep_cold_priority(self):
        for flags in self.histories((C, M, X, N, U)):
            with self.subTest(flags=sorted(flags)):
                council = self.choices(L + 'after_the_council', 'start', flags)
                self.assertEqual(['council_cold'] if self.cold(flags) else ['think', 'like'], [a['Next'] for a in council])
                self.assertEqual({c['Next'] for c in council}, {'council_cold'} if self.cold(flags) else {'think', 'like'})
                after = self.choices(L + 'after_the_war', 'tin', flags)
                dispatch_5, = after
                answer_in_order_4, *answer_in_order_4_following = after
                self.assertEqual(answer_in_order_4['Next'], 'after_cold' if self.cold(flags) else 'after_narrowed' if N in flags else 'after')
        for scene, node in (('after_the_council', 'council_cold'), ('after_the_war', 'after_cold')):
            ordered_answer_6, *ordered_answer_6_rest = self.node(L + scene, node)['Choices']
            answer = ordered_answer_6
            self.assertIsNone(answer['Next'])
            self.assertFalse(answer['Set'])

    def test_both_ending_families_respect_account_and_relationship(self):
        for flags in self.histories((C, M, X, N, U)):
            for told in (False, True):
                history = flags | {L + 'signed_after'} | ({P + 'cost.told_all'} if told else set())
                committed = self.node(P + 'epilogue.committed', 'page')['Paragraphs']
                after = self.node(P + 'epilogue.after_the_war', 'page')['Paragraphs']
                disclosure = [p for p in committed if P + 'cost.told_all' in p.get('Requires', ()) or P + 'cost.told_all' in p.get('Forbids', ())]
                self.assertEqual([[P + 'cost.told_all']] if told else [[]], [p['Requires'] for p in disclosure if visible(p, history)])
                relationship = [p for p in committed if set(p.get('Requires', ()) + p.get('Forbids', ())) & {C, M, X, N, U}]
                warm = not self.cold(flags) and N not in flags and (U not in flags)
                self.assertEqual([[M]] if warm and M in flags else [[]] if warm else [], [p['Requires'] for p in relationship if visible(p, history)])
                states = [p for p in after if set(p.get('Requires', ()) + p.get('Forbids', ())) & {C, M, X, N, U} and p.get('Requires') != [M]]
                if self.cold(flags):
                    expected = [X] if X in flags else [C]
                elif N in flags:
                    expected = [N, C, M] if C in flags and M in flags else [N]
                elif U in flags:
                    expected = [U, C, M] if C in flags and M in flags else [U]
                else:
                    expected = [L + 'signed_after', C, M] if C in flags and M in flags else [L + 'signed_after']
                self.assertEqual([expected], [p['Requires'] for p in states if visible(p, history)])
        for disposition in (ledger.TRUE_BOOKS, ledger.CLEAN_COPY, ledger.HER_NAME):
            account = [p for p in self.node(P + 'epilogue.committed', 'page')['Paragraphs'] if p.get('Requires') == [disposition] and (not p.get('AnyGroups'))]
            self.assertEqual([True], [visible(p, {disposition}) for p in account])

    def test_order_has_a_private_rebuke_and_other_rations_keep_thanks(self):
        scene = L + 'half_rations'
        for flags, target in ((set(), 'last'), ({ledger.ORDERED}, 'after_ordered')):
            answers = self.choices(scene, 'after', flags)
            dispatch_7, = answers
            answer_in_order_5, *answer_in_order_5_following = answers
            self.assertEqual(answer_in_order_5['Next'], target)
            ordered_answer_8, *ordered_answer_8_rest = self.node(scene, target)['Choices']
            self.assertIsNone(ordered_answer_8['Next'])

    def test_new_forgery_requires_current_path_but_issued_document_is_history(self):
        scene = L + 'old_debts'
        for flags, count in (({'trickster.now'}, 3), ({'trickster.ever', 'trickster.failed'}, 2), ({'trickster.ever', 'legend'}, 2), ({'trickster.ever', 'dragon'}, 2)):
            answers = self.choices(scene, 'stuck', flags)
            self.assertEqual(['forge', 'honest', 'fence'] if count == 3 else ['honest', 'fence'], [a['Next'] for a in answers])
            self.assertEqual(any((c['Next'] == 'forge' for c in answers)), count == 3)
        self.assertNotIn('trickster.now', self.scenes[scene]['Requires'])
        self.assertIn('forged', {c['Next'] for c in self.choices(L + 'three_hundred_helmets', 'start', {ledger.FORGED, 'trickster.failed'})})

    def test_professional_fallback_and_treasury_payment_make_no_extra_promise(self):
        fallback = self.scenes[P + 'epilogue.commit']
        self.assertIn('dorgelinda.committed', fallback['Forbids'])
        ordered_answer_9, *ordered_answer_9_rest = self.node(L + 'the_kings_bill', 'bill')['Choices']
        choice = ordered_answer_9
        self.assertEqual(choice['Crusade'], {'Resource': 'Finances', 'Amount': -200})
        self.assertEqual(choice['Next'], 'mine')
if __name__ == '__main__':
    unittest.main()
