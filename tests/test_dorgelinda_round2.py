"""Situation histories and earned receipts for Dorgelinda's second polish round."""
import copy
import json
from pathlib import Path
import unittest
from storylines import dorgelinda_ledger as l, dorgelinda_trickster as t
from tests.test_dorgelinda_polish import visible

class RoundTwoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payload = {'Scenes': copy.deepcopy(t.SCENES + l.SCENES)}
        t.integrate(cls.payload)
        l.integrate(cls.payload)
        cls.scenes = {s['Id']: s for s in cls.payload['Scenes']}

    def node(self, scene, node):
        return next((n for n in self.scenes[scene]['Nodes'] if n['Id'] == node))

    def answers(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices'] if visible(c, flags)]

    def test_professional_progress_cannot_be_late_acceptance(self):
        self.assertEqual(t.DERIVED[t.P + 'late_committed'], [['trickster.ever', t.COMMITTED, 'dorgelinda.outcome.accepted']])
        self.assertEqual(t.DERIVED['dorgelinda.outcome.accepted'], [[t.COMMITTED]])
        for nid in ('clean', 'dirty'):
            ordered_answer_1, *ordered_answer_1_rest = self.node(t.P + 'after.fellows_methods', nid)['Choices']
            self.assertNotIn(t.COMMITTED, ordered_answer_1['Set'])

    def test_disclosure_pays_before_renewed_request_and_she_answers(self):
        sid = t.P + 'after.second_ask'
        ordered_answer_2, *ordered_answer_2_rest = self.node(sid, 'price')['Choices']
        payment = ordered_answer_2
        self.assertEqual(payment['Crusade']['Amount'], -100)
        self.assertEqual(payment['Set'], [t.TOLD_ALL])
        ordered_answer_3, *ordered_answer_3_rest = self.node(sid, 'told')['Choices']
        request = ordered_answer_3
        self.assertFalse(request['Set'])
        self.assertEqual(request['Next'], 'accepted')
        answer = self.node(sid, 'accepted')
        ordered_answer_4, *ordered_answer_4_rest = answer['Choices']
        self.assertEqual(ordered_answer_4['Set'], [t.COMMITTED, t.TOLD_ALL])

    def test_recovery_precedes_actual_requisition_and_crisis(self):
        sid = t.P + 'after.fellows_methods'
        flags = {l.REQUISITIONS, t.CONSCIENCE}
        answers = self.answers(sid, 'door', flags)
        self.assertEqual([a['Next'] for a in answers], ['conscience'])
        self.assertEqual(self.payload['SeenCues'][l.REQUISITIONS], ['1576c91c20be9064083a3181abb354a9'])
        for flags in ({t.CONSCIENCE}, {t.CONSCIENCE, l.RATIONS_EQUAL, l.RATIONS_LIE}):
            self.assertEqual([a['Next'] for a in self.answers(l.RATIONS, 'start', flags)], ['provisioned'])

    def test_delivery_awards_stock_once_and_sealing_awards_none(self):
        ordered_answer_5, *ordered_answer_5_rest = self.node(l.DEBTS, 'forge')['Choices']
        self.assertNotIn('Crusade', ordered_answer_5)
        for nid, amount in (('twice', 100), ('honest', 75), ('fence', 100)):
            fresh = self.answers(l.HELMETS, nid, set())
            received = self.answers(l.HELMETS, nid, {l.L + 'helmets_received'})
            dispatch_6, = fresh
            answer_in_order_1, *answer_in_order_1_following = fresh
            self.assertEqual(answer_in_order_1['Crusade']['Amount'], amount)
            dispatch_7, = received
            answer_in_order_2, *answer_in_order_2_following = received
            self.assertNotIn('Crusade', answer_in_order_2)

    def test_all_quarrel_exits_inherit_loss_and_repairs_cannot_mint_stock(self):
        loss = self.answers(l.QUARREL_SCENE, 'start', set())
        dispatch_8, = loss
        answer_in_order_3, *answer_in_order_3_following = loss
        self.assertEqual(answer_in_order_3['Crusade']['Amount'], -150)
        answer_in_order_4, *answer_in_order_4_following = loss
        self.assertIn(l.ALLOTMENT_LOST, answer_in_order_4['Set'])
        answer_in_order_5, *answer_in_order_5_following = self.answers(l.QUARREL_SCENE, 'start', {l.ALLOTMENT_LOST})
        self.assertNotIn('Crusade', answer_in_order_5)
        ordered_answer_9, *ordered_answer_9_rest = self.node(l.QUARREL_SCENE, 'grain_receipt')['Choices']
        self.assertEqual(ordered_answer_9['Crusade']['Amount'], -50)
        for sid, nid in ((l.QUARREL_SCENE, 'written'), (l.COLD_COUNTS, 'letter')):
            for flags, expected in ((set(), 0), ({l.ALLOTMENT_LOST}, 50), ({l.ALLOTMENT_LOST, l.POWDER_RESTORED}, 0)):
                answers = self.answers(sid, nid, flags)
                dispatch_10, = answers
                answer_in_order_6, *answer_in_order_6_following = answers
                self.assertEqual(answer_in_order_6.get('Crusade', {}).get('Amount', 0), expected)

    def test_bill_checks_keep_a_real_debt_and_payment_is_separate(self):
        for nid, flag, amount in (('jest_won', l.WINE_OWED, 50), ('jest_lost', l.BILL_OWED, 200)):
            answers = self.node(l.REVELS, nid)['Choices']
            answer_in_order_7, *answer_in_order_7_following = answers
            self.assertIn(flag, answer_in_order_7['Set'])
            answer_in_order_8, *answer_in_order_8_following = answers
            self.assertNotIn('Crusade', answer_in_order_8)
            answer_in_order_9_before_0, answer_in_order_9, *answer_in_order_9_following = answers
            self.assertEqual(answer_in_order_9['Crusade']['Amount'], -amount)
            answer_in_order_10_before_0, answer_in_order_10, *answer_in_order_10_following = answers
            self.assertIn(l.CELLAR_PAID, answer_in_order_10['Set'])
            answer_in_order_11_before_0, answer_in_order_11, *answer_in_order_11_following = answers
            self.assertNotIn(t.COMMITTED, answer_in_order_11['Set'])
        *answer_in_order_12_preceding, answer_in_order_12 = self.node(l.L + 'cellar_settlement', 'bill')['Choices']
        self.assertTrue(answer_in_order_12['Abort'])

    def test_solo_denials_and_poly_denial_follow_real_state(self):
        sid = l.OTHERS
        solo = [a for a in self.answers(sid, 'says', {'trickster.ever'}) if a['Next'] in ('lie', 'nobody')]
        poly = [a for a in self.answers(sid, 'says', {'trickster.ever', l.OTHER_LOVER}) if a['Next'] in ('lie', 'nobody')]
        dispatch_11, = solo
        dispatch_12, = poly
        self.assertEqual({a['Next'] for a in solo}, {'nobody'})
        self.assertEqual({a['Next'] for a in poly}, {'lie'})
        self.assertNotIn(['ember.harem.eligible'], self.payload['Derived'][l.OTHER_LOVER])
        self.assertNotIn(['aivu.harem.eligible'], self.payload['Derived'][l.OTHER_LOVER])

    def test_names_are_disclosed_before_terms_and_new_relationship_has_followup(self):
        sid = l.OTHERS
        answers = self.answers(sid, 'names.0', {l.L + 'undisclosed.nocticula'})
        self.assertEqual([a['Next'] for a in answers], ['named.nocticula'])
        ordered_answer_13, *ordered_answer_13_rest = self.node(sid, 'named.nocticula')['Choices']
        answer = ordered_answer_13
        self.assertFalse(answer['Set'])
        self.assertEqual(self.payload['DerivedOpenRoutes'][l.L + 'current_other.nocticula'], ['nocticula'])
        *answer_in_order_13_preceding, answer_in_order_13 = self.answers(sid, 'names.0', set())
        self.assertEqual(answer_in_order_13['Next'], 'names_done')
        follow = self.scenes[l.L + 'changed_columns']
        self.assertEqual(follow['RequiresAnyGroups'], [[l.L + 'sole_line', l.L + 'terms_kept']])
        self.assertIn(l.L + 'new_columns', follow['Requires'])
        self.assertIn(t.CLOSED, follow['Forbids'])
        nodes = {n['Id']: n for n in follow['Nodes']}
        reached, pending = (set(), [follow['Nodes'][0]['Id']])
        while pending:
            nid = pending.pop()
            if nid in reached:
                continue
            reached.add(nid)
            pending.extend((a['Next'] for a in nodes[nid]['Choices'] if a.get('Next')))
        self.assertEqual(reached, set(nodes))

    def test_disclosure_is_acyclic_and_names_only_each_actual_relationship(self):
        from storylines.household import PARTNERS
        partners = [r for r in PARTNERS if r != 'dorgelinda']
        for actual in ([], ['nocticula'], ['anevia', 'galfrey'], partners):
            flags = {l.L + 'undisclosed.' + r for r in actual if not (r in ('anevia', 'irabeth') and 'tirabade' in actual)}
            current, visited, named = ('names.0', set(), [])
            while current != 'names_done':
                self.assertNotIn(current, visited)
                visited.add(current)
                if current.startswith('named.'):
                    named.append(current[6:])
                choices = self.answers(l.OTHERS, current, flags)
                dispatch_14, = choices
                answer_in_order_14, *answer_in_order_14_following = choices
                flags.update(answer_in_order_14['Set'])
                answer_in_order_15, *answer_in_order_15_following = choices
                current = answer_in_order_15['Next']
            self.assertEqual(named, [r for r in partners if r in actual and (not (r in ('anevia', 'irabeth') and 'tirabade' in actual))])
        for rel, native in (('arueshalae', l.L + 'native_arueshalae_open'), ('camellia', 'camellia.romance'), ('galfrey', 'galfrey.romance_active'), ('wenduag', 'wenduag.romance_active')):
            key = l.L + 'current_other.' + rel
            self.assertIn([native], self.payload['Derived'][key])
            self.assertEqual(self.payload['DerivedOpenRoutes'][key], [rel])
        self.assertEqual(self.payload['Etudes'][l.L + 'native_arueshalae'], 'd6a90c0f6536331498cafa1f3195d886')
        self.assertEqual(self.payload['Derived'][l.L + 'native_arueshalae_open'], [[l.L + 'native_arueshalae']])
        self.assertNotIn(l.L + 'native_arueshalae_failed', self.payload['Etudes'])

    def test_first_night_slot_and_brief_have_matching_cut(self):
        slot = 'dorgelinda.ledger.after_hours.explicit.1'
        ordered_answer_15, *ordered_answer_15_rest = self.node(l.NIGHT, 'threshold')['Choices']
        old = ordered_answer_15
        self.assertEqual(old['Next'], slot)
        self.assertFalse(old['Set'])
        ordered_answer_16, *ordered_answer_16_rest = self.node(l.NIGHT, slot)['Choices']
        self.assertEqual(ordered_answer_16['Set'], [l.NIGHT_KEPT])
        brief = json.loads((Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/dorgelinda-stranglehold' / (slot + '.json')).read_text(encoding='utf-8'))
if __name__ == '__main__':
    unittest.main()
