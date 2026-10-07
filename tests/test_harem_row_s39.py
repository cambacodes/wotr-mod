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
        return next(n for n in body['Nodes'] if n['Id'] == node)['Choices'][index]

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
            self.assertEqual(len(choices), 4 if step == 'undertaking' else 3)
            self.assertTrue(choices[-1]['Abort'])
            self.assertEqual(choices[-1]['Set'], [])
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
            self.assertEqual(len(paragraphs), 2 * (len(pair.RECORDS) + len(pair.COSTS) + 1))
            for i in range(0, len(paragraphs), 2):
                normal, returned = paragraphs[i:i + 2]
                self.assertIn('sacrifice', normal['Forbids'])
                self.assertIn('sacrifice', returned['Requires'])
                self.assertIn('trickster.commander_back', returned['Requires'])
                self.assertIn(pair.PREFIX + 'reader.' + woman + '.open', normal['Requires'])
        before = pair.PREFIX + 'reader.nocticula.before_council'
        self.assertIn('noct.acq.council_fight', self.story['DerivedForbids'][before])
        entries = [e for e in self.story['Books']['trickster.ledger']['Entries'] if e['Id'].startswith(pair.PREFIX)]
        self.assertEqual(len(entries), 2)
        for entry in entries:
            self.assertEqual(len(entry['Lines']), len(pair.RECORDS) + len(pair.COSTS))
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
            self.assertEqual(len(histories), 5 if step == "undertaking" else 3)
            aborts = [s for s in histories if pair.PREFIX + step + ".seen" not in s.flags]
            self.assertEqual(len(aborts), 1)
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


if __name__ == '__main__':
    unittest.main()
