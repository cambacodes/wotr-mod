"""Exercise divergent settlements, receipt delivery and epilogue claims."""
import unittest
from tests.story_fixture import fresh_story
from tools import rrt_verify as verify
K = 'konomi.trickster.'

class KonomiRound3Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = verify.Model(cls.story)

    def node(self, sid, nid):
        return next(n for n in self.by["konomi." + sid]["Nodes"] if n["Id"] == nid)

    @staticmethod
    def selectable(choice, flags):
        return set(choice.get("Requires", [])) <= flags and not set(choice.get("Forbids", [])) & flags

    def test_each_political_settlement_reaches_its_own_breakfast(self):
        cut = self.node('trickster.dismissed.private', 'konomi.trickster.dismissed.private.explicit.1')
        for bargain, expected in (('paid', 'morning'), ('paid_envoy', 'morning'), ('favour', 'morning_favour')):
            ordered_answer_1, *_ = self.node('trickster.dismissed.terms', bargain)['Choices']
            flags = set(ordered_answer_1['Set'])
            choices = [ch for ch in cut['Choices'] if self.selectable(ch, flags)]
            self.assertEqual([expected], [ch['Next'] for ch in choices])
            breakfast = self.node('trickster.dismissed.private', expected)
            self.assertTrue(breakfast['Choices'])

    def test_whole_return_histories_leave_one_letter_or_two_with_fallback(self):
        prefix = 'konomi.trickster.'
        chains = ((5, ['dead.recalled', 'dismissed.late', 'dismissed.arrival'], 1), (5, ['never_arrived.accredited', 'never_arrived.arrival', 'never_arrived.audience_letter'], 1), (3, ['never_arrived.accredited', 'never_arrived.arrival', 'dead.recalled'], 1), (3, ['never_arrived.accredited', 'never_arrived.arrival', 'never_arrived.audience_letter', 'dead.recalled'], 2))
        for chapter, chain, letters in chains:
            hosts = [self.by[prefix + sid] for sid in chain]
            self.assertTrue(all((chapter in s['Chapters'] for s in hosts)))
            self.assertEqual([s['Id'] for s in hosts if s.get('Remote')], [prefix + part for part in chain if part in ('never_arrived.audience_letter', 'dead.recalled')])
            for s in hosts:
                if not s.get('Remote'):
                    self.assertEqual('b5e867e13503c6f41bb1316705efb4a2', s['ContactUnit'])
                    self.assertEqual(['33960c7f7af40cd43b7f801a76c87a0b'], s['AnswerLists'])
                    self.assertNotIn('konomi.present_now', s['Requires'])

    def test_paid_and_favour_histories_cannot_invent_an_envoy_appointment(self):
        readers = set()
        for s in self.story['Scenes']:
            if s.get('Relationship') != 'konomi' or s.get('Owner') != 'Epilogue':
                continue
            for n in s['Nodes']:
                paras = n.get('Paragraphs', [])
                for para in paras:
                    if not (para.get('Requires', []) == ['konomi.trickster.recessed', 'konomi.trickster.cost.outfoxed', 'konomi.trickster.envoy'] and para.get('Forbids', []) == [] and (para.get('AnyGroups', []) == [])):
                        continue
                    readers.add((s['Id'], n['Id']))
                    for settlement in ('paid_envoy', 'favour'):
                        flags = {K + 'recessed', K + 'cost.outfoxed'}
                        ordered_answer_2, *_ = self.node('trickster.dismissed.terms', settlement)['Choices']
                        flags.update(ordered_answer_2['Set'])
                        self.assertFalse(self.selectable(para, flags))
                        gossip = [p for p in paras if p.get('Requires', []) == ['konomi.trickster.recessed', 'konomi.trickster.cost.outfoxed'] and p.get('Forbids', []) == ['konomi.trickster.envoy'] and (p.get('AnyGroups', []) == [])]
                        self.assertTrue(self.selectable(next(iter(gossip)), flags))
                        ordered_answer_3, *_ = self.node('trickster.dismissed.private', 'envoy')['Choices']
                        flags.update(ordered_answer_3['Set'])
                        self.assertTrue(self.selectable(para, flags))
                        self.assertFalse(self.selectable(next(iter(gossip)), flags))
        self.assertLessEqual({
            ('konomi.ending_ascended', 'start'),
            ('konomi.ending_changed', 'start'),
            ('konomi.ending_distance', 'start'),
            ('konomi.ending_distance_lived', 'exclusive'),
            ('konomi.ending_distance_lived', 'portfolio'),
            ('konomi.ending_distance_open', 'start'),
            ('konomi.ending_distance_open_lived', 'exclusive'),
            ('konomi.ending_distance_open_lived', 'portfolio'),
            ('konomi.ending_private', 'start'),
            ('konomi.ending_public', 'start'),
            ('konomi.ending_public_buried', 'start'),
            ('konomi.trickster.epilogue.commit', 'dinner'),
            ('konomi.trickster.epilogue.commit', 'signed'),
            ('konomi.trickster.epilogue.commit', 'terms'),
            ('konomi.trickster.epilogue.envoy', 'start'),
            ('konomi.trickster.epilogue.refused', 'postwar_open'),
            ('konomi.trickster.epilogue.refused', 'postwar_visit'),
            ('konomi.trickster.epilogue.refused', 'start'),
        }, readers)

    def test_all_register_copies_keep_the_signed_correction(self):
        copies = [p for s in self.story['Scenes'] if s.get('Relationship') == 'konomi' for n in s['Nodes'] for p in n.get('Paragraphs', []) if p.get('Requires', []) == ['konomi.trickster.returned', 'konomi.trickster.cost.accredited'] and p.get('Forbids', []) == [] and (p.get('AnyGroups', []) == [])]
        self.assertTrue(copies)
        for para in copies:
            self.assertIn('konomi.trickster.returned', para['Requires'])
            self.assertIn('konomi.trickster.cost.accredited', para['Requires'])

    def test_new_lastcall_obligation_requires_an_actual_acceptance(self):
        page = self.by['konomi.lastcall.page']
        accepted = next((p for p in page['Nodes'][0]['Paragraphs'] if p.get('Requires', []) == ['konomi.lastcall.terms_accepted'] and p.get('Forbids', []) == [] and (p.get('AnyGroups', []) == [])))
        call = self.by['konomi.lastcall.call']
        terms = next((n for n in call['Nodes'] if n['Id'] == 'terms'))
        accept, refuse, defer = terms['Choices']
        self.assertEqual([a['Next'] for a in terms['Choices']], ['accepted', None, None])
        flags = {'konomi.lastcall.called'}
        self.assertFalse(self.selectable(accepted, flags))
        for choice in terms['Choices'][1:]:
            self.assertFalse(self.selectable(accepted, flags | set(choice['Set'])))
        acceptance = next((n for n in call['Nodes'] if n['Id'] == accept['Next']))
        ordered_answer_4, *_ = acceptance['Choices']
        self.assertTrue(self.selectable(accepted, flags | set(ordered_answer_4['Set'])))
        collections = [p for s in self.story['Scenes'] if s.get('Relationship') == 'konomi' for n in s['Nodes'] for p in n.get('Paragraphs', []) if p.get('Requires', []) == ['konomi.trickster.favour_owed', 'konomi.lastcall.terms_accepted'] and p.get('Forbids', []) == [] and (p.get('AnyGroups', []) == [])]
        self.assertTrue(collections)
        for para in collections:
            outstanding = flags | {K + 'favour_owed'}
            self.assertFalse(self.selectable(para, outstanding))
            self.assertTrue(self.selectable(para, outstanding | {'konomi.lastcall.terms_accepted'}))

    def test_actual_settlement_receipts_control_the_lastcall_account(self):
        for sid, nid, history, due in (('trickster.dismissed.terms', 'paid', K + 'cost.debt_owed', False), ('trickster.dismissed.terms', 'paid_envoy', K + 'cost.debt_owed', False), ('trickster.dismissed.terms', 'favour', K + 'cost.debt_owed', True), ('trickster.dead.consultation', 'paid', K + 'cost.consult_fee', False)):
            state = verify.SimState(5, 100)
            state.flags.update({'trickster', 'trickster.ever', 'trickster.lastcall.open', history})
            ordered_answer_5, *_ = self.node(sid, nid)['Choices']
            state.flags.update(ordered_answer_5['Set'])
            verify.sim_complete(self.model, state)
            self.assertEqual(due, 'konomi.lastcall.favour_due' in state.flags, nid)
            self.assertEqual(due, 'konomi.lastcall.account_due' in state.flags, nid)
if __name__ == '__main__':
    unittest.main()
