"""S40 deed traversal, current channels, costs and survival readers."""
from tests.story_fixture import fresh_story
import json
import unittest

from storylines import household_pair_iomedae_nocticula as row
from tools import rrt_verify as verify

class CaptiveDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = verify.Model(cls.story)

    def state(self):
        state = verify.SimState(5, 1000)
        state.flags.update(['trickster', 'trickster.ever', 'trickster.foresight.accepted',
                            'trickster.foresight.cost.promise', 'household.table.kept',
                            'iomedae.committed', 'iomedae.trickster.first_spoken',
                            'iomedae.trickster.order_banner', 'noct.complete',
                            'iomedae.trickster.disputation.called', 'iomedae.trickster.disputed',
                            'nocticula.trickster.said_yes'])
        verify.sim_complete(self.model, state)
        return state

    def body(self, step):
        return self.model.by_id[row.P + step]

    def walk(self, step, choice, result=None):
        body = next(s for s in self.story['Scenes'] if s['Id'] == row.P + step)
        nodes = {n['Id']: n for n in body['Nodes']}
        answer = ordered_answer(nodes['start']['Choices'], choice,
                ((('complete', False, None, None, (), ()),
                  ('declined', False, None, None, (), ()),
                  (None, True, None, None, (), ())),
                 ((None, False, 'six', 'short', (), ()),
                  ('paid', False, None, None, (), ()),
                  ('falsified', False, None, None, (), ()),
                  (None, True, None, None, (), ())),
                 (('commissioned', False, None, None, (), ()),
                  ('refused', False, None, None, (), ()),
                  (None, True, None, None, (), ()))))
        self.assertFalse(answer['Set'])
        if answer['Abort']:
            return set(), None
        destination = answer.get('Next') or answer['Check'][result]
        terminal = nodes[destination]['Choices']
        _single_result, = terminal
        self.assertFalse(select_answer(terminal, ((None, False, None, None, (), ()),), expected_position=0)['Abort'])
        return set(select_answer(terminal, ((None, False, None, None, (), ()),), expected_position=0)['Set']), select_answer(terminal, ((None, False, None, None, (), ()),), expected_position=0).get('Crusade')

    def test_all_deeds_refusals_checks_costs_and_aborts(self):
        cases = [('open', 0, None, 'open.ready', -200),
                 ('open', 1, None, 'permanent_refusal', None),
                 ('delivery', 0, 'Success', 'delivery.held', None),
                 ('delivery', 0, 'Failure', 'delivery.failed', None),
                 ('delivery', 1, None, 'delivery.held', -500),
                 ('delivery', 2, None, 'permanent_refusal', None),
                 ('ransom', 0, None, 'ransom.held', -700),
                 ('ransom', 1, None, 'permanent_refusal', None)]
        for step, choice, result, witness, expense in cases:
            with self.subTest(step=step, choice=choice, result=result):
                flags, cost = self.walk(step, choice, result)
                self.assertIn(row.P + step + '.seen', flags)
                self.assertIn(row.P + witness, flags)
                self.assertEqual(cost, dict(Resource='Finances', Amount=expense) if expense else None)
                self.assertTrue(all(f.startswith(row.P) for f in flags))
                self.assertFalse(any('.harem.' in f for f in flags))
                if witness in ('delivery.held', 'ransom.held'):
                    self.assertIn(row.P + 'proof.six_alive', flags)
                else:
                    self.assertNotIn(row.P + 'proof.six_alive', flags)
        for step, index in [('open', 2), ('delivery', 3), ('ransom', 2)]:
            self.assertEqual(self.walk(step, index), (set(), None))

    def test_paid_page_current_path_and_banner_are_required(self):
        self.assertTrue(verify.sim_available(self.model, self.body('open'), self.state()))
        for missing in ['trickster', 'trickster.foresight.accepted',
                        'iomedae.trickster.first_spoken', 'iomedae.trickster.order_banner']:
            state = self.state()
            state.flags.discard(missing)
            verify.sim_complete(self.model, state)
            self.assertFalse(verify.sim_available(self.model, self.body('open'), state), missing)
        state = self.state()
        state.flags.discard('iomedae.trickster.order_banner')
        state.flags.add('iomedae.banner_in_hand')
        verify.sim_complete(self.model, state)
        self.assertTrue(verify.sim_available(self.model, self.body('open'), state))

    def test_closure_and_council_silence_even_with_historical_commit(self):
        for flag in ['iomedae.closed', 'noct.closed', 'noct.dead', 'noct.acq.council_fight']:
            state = self.state()
            state.flags.add(flag)
            verify.sim_complete(self.model, state)
            self.assertFalse(verify.sim_available(self.model, self.body('open'), state), flag)
        state = self.state()
        state.flags.update(['noct.dead', 'noct.defeated_not_dead', 'noct.acq.council_fight'])
        verify.sim_complete(self.model, state)
        self.assertFalse(verify.sim_available(self.model, self.body('open'), state))
        state.flags.add('nocticula.trickster.returned')
        verify.sim_complete(self.model, state)
        self.assertTrue(verify.sim_available(self.model, self.body('open'), state))
        state.flags.add('noct.closed')
        verify.sim_complete(self.model, state)
        self.assertFalse(verify.sim_available(self.model, self.body('open'), state))

    def test_deed_witnesses_supply_clocks_and_recovery_exclusions(self):
        for step, witness in [('delivery', 'open.ready'), ('ransom', 'delivery.failed')]:
            state = self.state()
            body = self.body(step)
            self.assertFalse(verify.sim_available(self.model, body, state))
            state.flags.add(row.P + witness)
            state.times[row.P + witness] = 1000
            verify.sim_complete(self.model, state)
            self.assertFalse(verify.sim_available(self.model, body, state))
            state.hour = 1048
            self.assertTrue(verify.sim_available(self.model, body, state))
        for flag in ['resolved', 'permanent_refusal', 'ransom.seen']:
            state.flags.add(row.P + flag)
            self.assertFalse(verify.sim_available(self.model, self.body('ransom'), state))
            state.flags.remove(row.P + flag)

    def test_living_reader_variants_and_historical_costs(self):
        def visible(paragraph, state):
            return (all(f in state.flags for f in paragraph['Requires'])
                    and not any(f in state.flags for f in paragraph['Forbids'])
                    and all(any(f in state.flags for f in g) for g in paragraph['AnyGroups']))
        for woman in row.PAIR:
            paras = row.living_paragraphs(woman)[:2]
            for sacrificed, returned, expected in [(False, False, 1), (True, False, 0), (True, True, 1)]:
                state = self.state()
                state.flags.add(row.P + 'resolved')
                if sacrificed:
                    state.flags.add('sacrifice')
                if returned:
                    state.flags.add('ending.trickster')
                verify.sim_complete(self.model, state)
                self.assertIn(contract_identities([p for p in paras if visible(p, state)]),
                        {1: (((None,
                               None,
                               None,
                               False,
                               ('household.pair.iomedae_nocticula.resolved',
                                'household.pair.iomedae_nocticula.reader.nocticula.open',
                                'sacrifice',
                                'trickster.commander_back'),
                               ()),),
                             ((None,
                               None,
                               None,
                               False,
                               ('household.pair.iomedae_nocticula.resolved',
                                'household.pair.iomedae_nocticula.reader.nocticula.open'),
                               ('sacrifice',)),),
                             ((None,
                               None,
                               None,
                               False,
                               ('household.pair.iomedae_nocticula.resolved',
                                'household.pair.iomedae_nocticula.reader.iomedae.open'),
                               ('iomedae.trickster.buried_alive', 'sacrifice')),),
                             ((None,
                               None,
                               None,
                               False,
                               ('household.pair.iomedae_nocticula.resolved',
                                'household.pair.iomedae_nocticula.reader.iomedae.open',
                                'sacrifice',
                                'trickster.commander_back'),
                               ('iomedae.trickster.buried_alive',)),)),
                         0: ((),)}[expected])
                state.flags.add('iomedae.closed' if woman == 'iomedae' else 'noct.closed')
                verify.sim_complete(self.model, state)
                self.assertIn(contract_identities([p for p in paras if visible(p, state)]), {0: ((),)}[0])
        ledger = self.story['Books']['trickster.ledger']['Entries']
        for suffix in ['ledger', 'seating']:
            entry = next(e for e in ledger if e['Id'] == row.P + 'reader.' + suffix)
            for cost in row.COSTS:
                self.assertTrue(any(row.P + 'cost.' + cost in line['Requires'] for line in entry['Lines']))

    def test_failed_delivery_reload_paid_remedy_and_saved_allowance(self):
        state = self.state()
        state.crusade_resources = {'Finances': 1200}

        def play(step, choice, result=None):
            body = self.body(step)
            nodes = {n['Id']: n for n in body['Nodes']}
            first = ordered_answer(nodes['start']['Choices'], choice,
                    ((('complete', False, None, None, (), ()),
                      ('declined', False, None, None, (), ()),
                      (None, True, None, None, (), ())),
                     ((None, False, 'six', 'short', (), ()),
                      ('paid', False, None, None, (), ()),
                      ('falsified', False, None, None, (), ()),
                      (None, True, None, None, (), ())),
                     (('commissioned', False, None, None, (), ()),
                      ('refused', False, None, None, (), ()),
                      (None, True, None, None, (), ()))))
            destination = first.get('Next') or first['Check'][result]
            last = select_answer(nodes[destination]['Choices'], ((None, False, None, None, (), ()),), expected_position=0)
            return verify.sim_play(self.model, body, state, set(), plan=(0, [first, last]))

        self.assertTrue(play('open', 0))
        self.assertEqual(state.crusade_resources['Finances'], 1000)
        self.assertEqual(state.rest_spent['household.protected'], 1)
        state.hour += 48
        state.rest_spent.clear()
        self.assertTrue(play('delivery', 0, 'Failure'))
        self.assertNotIn(row.P + 'proof.six_alive', state.flags)
        saved = json.loads(json.dumps(dict(flags=sorted(state.flags), times=state.times,
                                         hour=state.hour, spent=state.rest_spent,
                                         resources=state.crusade_resources)))
        state = verify.SimState(5, saved['hour'])
        state.flags.update(saved['flags'])
        state.times.update(saved['times'])
        state.rest_spent.update(saved['spent'])
        state.crusade_resources = saved['resources']
        verify.sim_complete(self.model, state)
        self.assertFalse(verify.sim_available(self.model, self.body('delivery'), state))
        self.assertFalse(verify.sim_available(self.model, self.body('ransom'), state))
        state.hour += 48
        state.rest_spent.clear()
        self.assertTrue(verify.sim_available(self.model, self.body('ransom'), state))
        self.assertTrue(play('ransom', 0))
        self.assertEqual(state.crusade_resources['Finances'], 300)
        self.assertIn(row.P + 'ransom.held', state.flags)
        self.assertIn(row.P + 'proof.six_alive', state.flags)
        self.assertIn(row.P + 'delivery.failed', state.flags)
        self.assertEqual(state.rest_spent['household.protected'], 1)
        self.assertFalse(verify.sim_available(self.model, self.body('ransom'), state))

    def test_all_living_sublines_obey_channel_silence_and_current_presence(self):
        for woman in row.PAIR:
            paragraphs = row.living_paragraphs(woman)
            rescue = [p for p in paragraphs if "iomedae.trickster.buried_alive" in p["Requires"]]
            paragraphs = [p for p in paragraphs if p not in rescue]
            for paragraph in rescue:
                self.assertTrue({row.P + "resolved", row.reader_key(woman), "sacrifice",
                                 "trickster.commander_back", "iomedae.trickster.buried_alive"}
                                <= set(paragraph["Requires"]))
                self.assertEqual(paragraph["AnyGroups"], [])
            for index in range(0, len(paragraphs), 2):
                living, returned = paragraphs[index:index + 2]
                self.assertEqual(living['Forbids'], [*returned['Forbids'], 'sacrifice'])
                self.assertEqual(returned['Requires'], [*living['Requires'], 'sacrifice', 'trickster.commander_back'])
                self.assertIn(row.reader_key(woman), living['Requires'])
                if woman == 'iomedae':
                    self.assertEqual(living['AnyGroups'], [list(row.BANNERS)])
        state = self.state()
        key = row.reader_key('nocticula')
        self.assertIn(key, state.flags)
        state.flags.update(['noct.acq.council_fight', 'noct.dead', 'noct.defeated_not_dead'])
        verify.sim_complete(self.model, state)
        self.assertNotIn(key, state.flags)
        state.flags.add('nocticula.trickster.returned')
        verify.sim_complete(self.model, state)
        self.assertIn(key, state.flags)
        state.flags.add('noct.closed')
        verify.sim_complete(self.model, state)
        self.assertNotIn(key, state.flags)

    def test_unaffordable_terminal_payment_grants_no_witness_or_allowance(self):
        for step, node_id, price, witness in [('open', 'commissioned', 200, None),
                                              ('delivery', 'paid', 500, 'open.ready'),
                                              ('ransom', 'complete', 700, 'delivery.failed')]:
            body = self.body(step)
            answer = select_answer(next(n for n in body['Nodes'] if n['Id'] == node_id)['Choices'], ((None, False, None, None, (), ()),), expected_position=0)
            for funds in (None, 0, price - 1):
                state = self.state()
                if witness:
                    state.flags.add(row.P + witness)
                    state.times[row.P + witness] = state.hour - 48
                state.crusade_resources = None if funds is None else {'Finances': funds}
                before = (set(state.flags), dict(state.times), dict(state.rest_spent))
                self.assertFalse(verify.sim_choice_available(answer, state))
                self.assertFalse(verify.sim_paid_choice(self.model, body, answer, state,
                                                       lambda: self.fail('unaffordable deed published')))
                self.assertEqual((state.flags, state.times, state.rest_spent), before)




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)




def ordered_answer(answers, ordinal, expected_orders):
    """Protect answer order, then select its declared structural destination."""
    actual = tuple(answer_key(answer) for answer in answers)
    if actual not in expected_orders:
        raise AssertionError(('answer order/gates changed', actual, expected_orders))
    for order in expected_orders:
        if order == actual:
            key = next(key for order_index, key in enumerate(order) if order_index == ordinal)
            return select_answer(answers, (key,))
    raise AssertionError('missing declared answer order')

if __name__ == '__main__':
    unittest.main()
