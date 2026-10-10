"""S39 deed walks, channels, save layout and guarded consequence readers."""
import unittest

from tests.story_fixture import fresh_story
from storylines import household_pair_galfrey_nocticula as pair
from tools import rrt_verify as verify


class GalfreyNocticulaUndertaking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s['Id']: s for s in cls.story['Scenes']}
        cls.scenes = [s for s in cls.story['Scenes'] if s['Id'].startswith(pair.PREFIX)]
        cls.model = verify.Model(cls.story)

    def choice(self, step, node, index=0, kitrane=False):
        body = self.by[pair.PREFIX + step + ('.kitrane' if kitrane else '')]
        return ordered_answer(next(n for n in body['Nodes'] if n['Id'] == node)['Choices'], index,
                (((None, False, None, None, (), ()),),
                 ((None, False, 'kept', 'mistranslated', (), ()),
                  ('interpreted', False, None, None, (), ()),
                  ('exposed', False, None, None, (), ()),
                  (None, True, None, None, (), ()))))

    def state(self, step='open', kitrane=False):
        state = verify.SimState(5, 1000)
        state.flags.update(['trickster', 'foresight.page_taken', 'household.table.kept',
                            'galfrey.harem.eligible', 'nocticula.harem.eligible'])
        if kitrane:
            state.flags.update(['galfrey.dead', pair.RETURNED])
        if step != 'open':
            state.flags.update(pair.f('open.ready', 'survey.acquired', 'sortie.mustered'))
        if step == 'last_litter':
            state.flags.update(pair.f('undertaking.failed'))
        return state

    def available(self, state, step='open', kitrane=False):
        body = self.by[pair.PREFIX + step + ('.kitrane' if kitrane else '')]
        return verify.sim_available(self.model, verify.norm_scene(body), state)

    def test_exact_terminal_writes_and_prices(self):
        expected = {
            ('open', 'sent'): ('open.seen', 'open.ready', 'survey.acquired', 'sortie.mustered',
                               'cost.courier_fares', 'cost.commander_guarantor_promised'),
            ('open', 'insult'): ('open.seen', 'open.insult_sent', 'permanent_refusal'),
            ('undertaking', 'kept'): pair.SUCCESS,
            ('undertaking', 'interpreted'): (*pair.SUCCESS, 'cost.interpreter_paid'),
            ('undertaking', 'mistranslated'): ('undertaking.seen', 'undertaking.failed', 'unsettled', 'cost.commander_delay'),
            ('undertaking', 'exposed'): ('undertaking.seen', 'undertaking.scout_exposed', 'permanent_refusal', 'cost.commander_cover_lost'),
            ('last_litter', 'home'): pair.REPAIR,
            ('last_litter', 'declined'): ('last_litter.seen', 'last_litter.declined', 'permanent_refusal'),
        }
        for kitrane in (False, True):
            for (step, node), flags in expected.items():
                choice = self.choice(step, node, kitrane=kitrane)
                self.assertEqual(choice['Set'], pair.f(*flags))
                self.assertIsNone(choice['Next'])
            for step, node, amount in [('open', 'sent', -200), ('undertaking', 'interpreted', -300),
                                        ('last_litter', 'home', -400)]:
                self.assertEqual(self.choice(step, node, kitrane=kitrane)['Crusade'],
                                 {'Resource': 'Finances', 'Amount': amount})
            self.assertEqual(self.choice('undertaking', 'start', kitrane=kitrane)['Check'],
                             dict(Skill='CheckDiplomacy', DC=24, Success='kept', Failure='mistranslated', CommanderOnly=True))

    def test_gate_attendance_and_identity_variants(self):
        for kitrane in (False, True):
            state = self.state(kitrane=kitrane)
            self.assertTrue(self.available(state, kitrane=kitrane))
            self.assertFalse(self.available(state, kitrane=not kitrane))
            for gate in ['trickster', 'foresight.page_taken', 'household.table.kept',
                         'galfrey.harem.eligible', 'nocticula.harem.eligible']:
                changed = self.state(kitrane=kitrane)
                changed.flags.remove(gate)
                changed.flags.update(['trickster.ever', 'foresight.met'])
                self.assertFalse(self.available(changed, kitrane=kitrane), gate)
            for block in ['galfrey.closed', 'galfrey.killed_by_commander', 'noct.closed',
                          'noct.acq.council_fight', 'galfrey.epoch_unavailable', 'nocticula.epoch_unavailable']:
                changed = self.state(kitrane=kitrane)
                changed.flags.add(block)
                self.assertFalse(self.available(changed, kitrane=kitrane), block)
            changed = self.state(kitrane=kitrane)
            changed.flags.update(['noct.acq.council_fight', 'nocticula.trickster.returned'])
            self.assertTrue(self.available(changed, kitrane=kitrane))
            changed.flags.update(['galfrey.harem.stance.own_house', 'galfrey.harem.enmity.nocticula'])
            self.assertTrue(self.available(changed, kitrane=kitrane))  # separately carried, never a joint meeting

    def test_delays_use_deed_clocks_not_respect_and_retry_is_once(self):
        for step, clock in [('undertaking', 'open.ready'), ('last_litter', 'undertaking.failed')]:
            state = self.state(step)
            state.times[pair.f(clock)[0]] = state.hour - 47
            self.assertFalse(self.available(state, step))
            state.times[pair.f(clock)[0]] = state.hour - 48
            self.assertTrue(self.available(state, step))
            state.flags.add(pair.f(step + '.seen')[0])
            self.assertFalse(self.available(state, step))
        state = self.state('undertaking')
        state.flags.remove(pair.f('survey.acquired')[0])
        self.assertFalse(self.available(state, 'undertaking'))
        state = self.state('last_litter')
        for flag in pair.f('resolved', 'permanent_refusal'):
            state.flags.add(flag)
            self.assertFalse(self.available(state, 'last_litter'))
        state = self.state()
        state.chapter = 6
        self.assertFalse(self.available(state))

    def test_append_only_choices_abort_and_no_policy_writes(self):
        for body in self.scenes:
            step = body['Id'][len(pair.PREFIX):].split('.')[0]
            choices = body['Nodes'][0]['Choices']
            self.assertIn(contract_identities(choices),
                    {3: ((('sent', None, None, False, (), ()),
                          ('insult', None, None, False, (), ()),
                          (None, None, None, True, (), ())),
                         (('home', None, None, False, (), ()),
                          ('declined', None, None, False, (), ()),
                          (None, None, None, True, (), ()))),
                     4: (((None, 'kept', 'mistranslated', False, (), ()),
                          ('interpreted', None, None, False, (), ()),
                          ('exposed', None, None, False, (), ()),
                          (None, None, None, True, (), ())),)}[4 if step == 'undertaking' else 3])
            self.assertTrue(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=-1)['Abort'])
            self.assertEqual(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=-1)['Set'], [])
            self.assertEqual(body['RestAllowance'], 'household.protected')
            self.assertTrue(body['ManualOnly'])
            self.assertEqual(body['Participants'], list(pair.PAIR))
            self.assertEqual(self.story['ForesightConsumers'][body['Id']], 'foresight.page_taken')
            for node in body['Nodes']:
                self.assertFalse(node.get('Paragraphs'))
                for choice in node['Choices']:
                    self.assertTrue(all(flag.startswith(pair.PREFIX) for flag in choice['Set']))
                    self.assertFalse(any(word in flag for flag in choice['Set']
                                         for word in ('.respect', '.enmity', '.reconciled', '.committed', '.closed')))
                    if node['Id'] != 'start':
                        self.assertFalse(choice['Abort'])

    def test_lastcall_readers_have_survival_and_current_channel_guards(self):
        for woman in pair.PAIR:
            page = self.by[woman + '.lastcall.page']['Nodes'][0]
            paragraphs = [p for p in page['Paragraphs']
                          if any(flag.startswith(pair.PREFIX) for flag in p['Requires'])]
            keys = ('resolved', 'failed', 'repaired', 'insult', 'scout', 'declined', 'cost.courier_fares', 'cost.commander_guarantor_promised', 'cost.galfrey_sponsorship_withdrawn', 'cost.nocticula_factor_overruled', 'cost.commander_guarantor_kept', 'cost.reconnaissance_forgone', 'cost.commander_delay', 'cost.commander_cover_lost', 'cost.interpreter_paid', 'cost.corrected_demand_carried', 'reaction')
            self.assertEqual([p["Id"] for p in paragraphs],
                             [pair.PREFIX + "reader.lastcall." + woman + "." + key + "." + channel
                              for key in keys for channel in ("living", "returned")])
            for i in range(0, len(paragraphs), 2):
                normal, returned = paragraphs[i:i + 2]
                self.assertIn('sacrifice', normal['Forbids'])
                self.assertIn('sacrifice', returned['Requires'])
                self.assertIn('trickster.commander_back', returned['Requires'])
                self.assertIn(pair.PREFIX + 'reader.' + woman + '.open', normal['Requires'])
        before = pair.PREFIX + 'reader.nocticula.before_council'
        self.assertIn('noct.acq.council_fight', self.story['DerivedForbids'][before])
        entries = [e for e in self.story['Books']['trickster.ledger']['Entries'] if e['Id'].startswith(pair.PREFIX)]
        self.assertIn(contract_identities(entries), {2: (('household.pair.galfrey_nocticula.reader.ledger', 'household.pair.galfrey_nocticula.reader.seating'),)}[2])
        for entry in entries:
            self.assertEqual([line["Id"] for line in entry["Lines"]],
                             [pair.PREFIX + "reader." + key for key in ('resolved', 'failed', 'repaired', 'insult', 'scout', 'declined', 'cost.courier_fares', 'cost.commander_guarantor_promised', 'cost.galfrey_sponsorship_withdrawn', 'cost.nocticula_factor_overruled', 'cost.commander_guarantor_kept', 'cost.reconnaissance_forgone', 'cost.commander_delay', 'cost.commander_cover_lost', 'cost.interpreter_paid', 'cost.corrected_demand_carried')])
            self.assertFalse(any('sacrifice' in line['Forbids'] for line in entry['Lines']))

    def test_every_answer_check_and_terminal_debit(self):
        from tests.harem_row_walk import walk
        # These fixtures start at each scene's earned entry; gate histories are
        # independently covered above, without synthesizing route commitments.
        model = verify.Model(dict(self.story, Scenes=self.scenes))
        for body in model.scenes:
            state = verify.SimState(5, 1000)
            state.flags.update(body["Requires"])
            state.times.update({flag: 900 for flag in body["Requires"]})
            state.crusade_resources = {"Finances": 2000}
            histories = walk(self, model, body, state)
            step = body["Id"][len(pair.PREFIX):].split('.')[0]
            self.assertIn(contract_identities(histories),
                    {3: ((('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.corrected_demand_carried',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.last_litter',
                           'household.pair.galfrey_nocticula.last_litter.held',
                           'household.pair.galfrey_nocticula.last_litter.seen',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.last_litter',
                           'household.pair.galfrey_nocticula.last_litter.declined',
                           'household.pair.galfrey_nocticula.last_litter.seen',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept')),
                         (('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.corrected_demand_carried',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.last_litter.held',
                           'household.pair.galfrey_nocticula.last_litter.kitrane',
                           'household.pair.galfrey_nocticula.last_litter.seen',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.last_litter.declined',
                           'household.pair.galfrey_nocticula.last_litter.kitrane',
                           'household.pair.galfrey_nocticula.last_litter.seen',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.table.kept')),
                         (('household.pair.galfrey_nocticula.cost.commander_guarantor_promised',
                           'household.pair.galfrey_nocticula.cost.courier_fares',
                           'household.pair.galfrey_nocticula.open',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.open.seen',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.open',
                           'household.pair.galfrey_nocticula.open.insult_sent',
                           'household.pair.galfrey_nocticula.open.seen',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.table.kept'),
                          ('household.table.kept',)),
                         (('household.pair.galfrey_nocticula.cost.commander_guarantor_promised',
                           'household.pair.galfrey_nocticula.cost.courier_fares',
                           'household.pair.galfrey_nocticula.open.kitrane',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.open.seen',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.open.insult_sent',
                           'household.pair.galfrey_nocticula.open.kitrane',
                           'household.pair.galfrey_nocticula.open.seen',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.table.kept'),
                          ('household.table.kept',))),
                     5: ((('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking',
                           'household.pair.galfrey_nocticula.undertaking.held',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_delay',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.pair.galfrey_nocticula.unsettled',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.interpreter_paid',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking',
                           'household.pair.galfrey_nocticula.undertaking.held',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_cover_lost',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking',
                           'household.pair.galfrey_nocticula.undertaking.scout_exposed',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.table.kept')),
                         (('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.held',
                           'household.pair.galfrey_nocticula.undertaking.kitrane',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_delay',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.failed',
                           'household.pair.galfrey_nocticula.undertaking.kitrane',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.pair.galfrey_nocticula.unsettled',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_guarantor_kept',
                           'household.pair.galfrey_nocticula.cost.galfrey_sponsorship_withdrawn',
                           'household.pair.galfrey_nocticula.cost.interpreter_paid',
                           'household.pair.galfrey_nocticula.cost.nocticula_factor_overruled',
                           'household.pair.galfrey_nocticula.cost.reconnaissance_forgone',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.resolved',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.held',
                           'household.pair.galfrey_nocticula.undertaking.kitrane',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.cost.commander_cover_lost',
                           'household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.permanent_refusal',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.pair.galfrey_nocticula.undertaking.kitrane',
                           'household.pair.galfrey_nocticula.undertaking.scout_exposed',
                           'household.pair.galfrey_nocticula.undertaking.seen',
                           'household.table.kept'),
                          ('household.pair.galfrey_nocticula.open.ready',
                           'household.pair.galfrey_nocticula.sortie.mustered',
                           'household.pair.galfrey_nocticula.survey.acquired',
                           'household.table.kept')))}[5 if step == 'undertaking' else 3])
            aborts = [s for s in histories if pair.PREFIX + step + ".seen" not in s.flags]
            _single_result, = aborts
            self.assertEqual(aborts[0].crusade_resources["Finances"], 2000)
            for result in histories:
                self.assertFalse(result.flags & {"galfrey.closed", "noct.closed"})
                if pair.PREFIX + step + ".seen" in result.flags:
                    self.assertEqual(result.times[pair.PREFIX + step + ".seen"], 1000)
                if pair.PREFIX + "resolved" in result.flags:
                    self.assertTrue({pair.PREFIX + "cost." + c for c in
                                     ("galfrey_sponsorship_withdrawn", "nocticula_factor_overruled",
                                      "commander_guarantor_kept", "reconnaissance_forgone")} <= result.flags)
            balances = {flag: end.crusade_resources["Finances"] for end in histories for flag in end.flags}
            if step == "open":
                self.assertEqual(balances[pair.PREFIX + "open.ready"], 1800)
            elif step == "undertaking":
                self.assertEqual(balances[pair.PREFIX + "undertaking.failed"], 2000)
                self.assertEqual(balances[pair.PREFIX + "cost.interpreter_paid"], 1700)
            else:
                self.assertEqual(balances[pair.PREFIX + "last_litter.held"], 1600)




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
