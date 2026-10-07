"""J06 transaction and private-obligation histories on the assembled export.

Expected failures expose engine work prohibited by this job's src restriction.
They are acceptance debt, not proof of a finished J06.
"""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines.harem_rows import s47, s50, s51
from tools import rrt_verify as rules


class J06Histories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.rows = cls.model.by_id

    def paid_state(self, scene, funds):
        state = rules.SimState(5, 100)
        state.flags.update(scene['Requires'])
        state.flags.update((s50.RENOUNCED, s50.N + 'hatched', s50.N + 'egg_owed',
                            'household.closed'))
        for group in scene['RequiresAnyGroups']:
            state.flags.add(group[0])
        state.times.update({flag: 0 for flag in state.flags})
        state.available_contacts = {scene['ContactUnit']}
        state.crusade_resources = {'Materials': funds}
        return state

    def test_affordable_pre_debit_abort_in_each_body_and_payment_host(self):
        for body in s50.BODIES:
            for step, node_id, price in (('custody', 'hire', 100), ('repair', 'start', 150)):
                with self.subTest(body=body, step=step):
                    scene = self.rows[s50.P + step + '.' + body]
                    node = next(n for n in scene['Nodes'] if n['Id'] == node_id)
                    state = self.paid_state(scene, price)
                    state.flags.add('household.started')
                    self.assertTrue(rules.sim_available(self.model, scene, state))
                    self.assertTrue(rules.sim_choice_available(node['Choices'][0], state))
                    abort = next(c for c in node['Choices'] if c['Abort'])
                    before = copy.deepcopy(state.__dict__)
                    self.assertFalse(rules.sim_play(self.model, scene, state, (), plan=(0, [abort])))
                    self.assertEqual(state.__dict__, before)

    def test_failed_paid_publication_restores_balance_receipts_and_allowance(self):
        for body in s50.BODIES:
            for step, node_id, price in (('custody', 'hire', 100), ('repair', 'start', 150)):
                scene = self.rows[s50.P + step + '.' + body]
                choice = next(n for n in scene['Nodes'] if n['Id'] == node_id)['Choices'][0]
                for fault in ('exception', 'incomplete', 'allowance'):
                    with self.subTest(body=body, step=step, fault=fault):
                        state = self.paid_state(scene, price + 73)
                        before = copy.deepcopy(state.__dict__)

                        def publish():
                            self.assertEqual(state.crusade_resources['Materials'], 73)
                            state.flags.update(choice['Set'])
                            state.times.update({flag: state.hour for flag in choice['Set']})
                            if fault == 'exception':
                                raise RuntimeError('Native publication failed')
                            if fault == 'incomplete':
                                return
                            state.flags.add(scene['Id'])
                            # Missing allowance must roll back even with all receipts.

                        self.assertFalse(rules.sim_paid_choice(self.model, scene, choice, state, publish))
                        self.assertEqual(state.__dict__, before)

    def test_paid_reload_exhausts_the_other_body_without_another_debit(self):
        for step, node_id, price in (('custody', 'hire', 100), ('repair', 'start', 150)):
            scene = self.rows[s50.P + step + '.widow']
            choice = next(n for n in scene['Nodes'] if n['Id'] == node_id)['Choices'][0]
            state = self.paid_state(scene, price + 73)
            self.assertTrue(rules.sim_play(self.model, scene, state, (), plan=(0, [choice])))
            self.assertEqual(state.rest_spent['household.protected'], 1)
            loaded = copy.deepcopy(state)
            loaded.flags.add(s50.N + 'form_chosen')
            self.assertFalse(rules.sim_available(self.model, self.rows[s50.P + step + '.chosen'], loaded))
            self.assertFalse(rules.sim_paid_choice(self.model, scene, choice, loaded,
                                                 lambda: self.fail('Reload republished the payment')))
            self.assertEqual(loaded.crusade_resources['Materials'], 73)

    def test_one_discovery_two_completions_and_one_recovery_are_serialized(self):
        for body in ('widow', 'chosen'):
            notice = self.rows[s51.P + 'notice.' + body]
            self.assertTrue(notice['HouseholdDiscovery'])
            self.assertIsNone(notice['RestAllowance'])
            for sid in ('cell', 'receipt.' + body, 'retry.' + body):
                scene = self.rows[s51.P + sid]
                self.assertEqual(scene['RestAllowance'], 'household.protected')
                self.assertIn(s51.P + sid.split('.')[0] + '.seen', scene['Forbids'])
            retry = self.rows[s51.P + 'retry.' + body]
            self.assertEqual(retry['RequiresAnyGroups'][0], list(s51.flags('cell.failed', 'cell.refused')))
            self.assertNotIn(s51.PROJECTOR_BROKEN, retry['Forbids'])
            self.assertNotIn('areelu.closed', retry['Forbids'])

    def test_spent_commission_has_no_second_comparison_cost(self):
        commission = self.rows[s47.P + 'commission']
        for history in ('yaniel.committed', s47.BEAT):
            for index in (0, 1):
                with self.subTest(history=history, choice=index):
                    state = rules.SimState(5, 1000)
                    state.flags.update(('trickster', 'trickster.foresight.accepted',
                                        'trickster.foresight.cost.promise', 'yaniel.freed.latched',
                                        'yaniel.trickster.returned', 'yaniel.areelu_unmasked', history))
                    rules.sim_complete(self.model, state)
                    self.assertTrue(rules.sim_available(self.model, commission, state))
                    choice = commission['Nodes'][0]['Choices'][index]
                    self.assertTrue(rules.sim_play(self.model, commission, state, (), plan=(0, [choice])))
                    loaded = copy.deepcopy(state)
                    self.assertFalse(rules.sim_available(self.model, commission, loaded))
                    self.assertEqual(s47.P + 'cost.yaniel_comparison' in loaded.flags, index == 0)
                    self.assertNotIn('household.protected', loaded.rest_spent)

    @unittest.expectedFailure
    def test_s50_predecessor_clock_survives_a_later_body_choice(self):
        scene = self.rows[s50.P + 'custody.chosen']
        state = self.paid_state(scene, 100)
        state.times[s50.P + 'notice.opened'] = 52
        state.times[s50.N + 'form_chosen'] = 99
        self.assertTrue(rules.sim_available(self.model, scene, state))

    @unittest.expectedFailure
    def test_s50_departure_during_debit_cancels_publication(self):
        scene = self.rows[s50.P + 'custody.widow']
        choice = next(n for n in scene['Nodes'] if n['Id'] == 'hire')['Choices'][0]
        state = self.paid_state(scene, 100)

        def publish():
            # The native actor disappears after the debit, before publication.
            state.available_contacts.clear()
            state.flags.update(choice['Set'] + [scene['Id']])
            state.rest_spent['household.protected'] = 1

        self.assertFalse(rules.sim_paid_choice(self.model, scene, choice, state, publish))
        self.assertEqual(state.crusade_resources['Materials'], 100)
        self.assertNotIn(s50.P + 'feed_delivered', state.flags)
        self.assertFalse(state.rest_spent)

    @unittest.expectedFailure
    def test_s51_receipt_clock_survives_a_later_body_choice(self):
        scene = self.rows[s51.P + 'receipt.chosen']
        state = rules.SimState(5, 100)
        state.flags.update(scene['Requires'])
        for group in scene['RequiresAnyGroups']:
            state.flags.add(group[0])
        state.times.update({flag: 0 for flag in state.flags})
        state.times[s51.P + 'cell.chart_erased'] = 52
        state.times[s50.N + 'form_chosen'] = 99
        state.available_contacts = {scene['ContactUnit']}
        self.assertTrue(rules.sim_available(self.model, scene, state))
