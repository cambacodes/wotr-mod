"""Route-local residue: dispatched mail and performed defense histories."""
import unittest
from tests.story_fixture import fresh_story
from tools import rrt_verify as rv

class KaylessaRoundFourTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rv.Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def test_late_supplement_cannot_enter_original_acknowledgment(self):
        sid = 'kaylessa.clearing.avennara'
        for original_reply_read in (False, True):
            state = rv.SimState(5, 1000)
            state.flags.update(self.scenes[sid]['Requires'])
            state.flags.update({'kaylessa.trickster.returned', 'kaylessa.trickster.knife_held'})
            state.times.update({f: 0 for f in state.flags})
            if original_reply_read:
                state.flags.add(sid)
            ordered_answer_1, *_ = self.node('kaylessa.wasps.the_girls_face', 'courier_followup')['Choices']
            dispatch = ordered_answer_1
            for flag in dispatch['Set']:
                state.flags.add(flag)
                state.times[flag] = state.hour
            choices = self.node(sid, 'receipt')['Choices']
            available = [c for c in choices if rv.sim_choice_available(c, state)]
            self.assertTrue(available)
            self.assertEqual({c['Next'] for c in available}, {'end'})
            supplement = self.model.by_id['kaylessa.clearing.courier_reply']
            for elapsed in (0, 719, 720):
                state.hour = 1000 + elapsed
                self.assertEqual(rv.sim_available(self.model, supplement, state), elapsed >= 720)
            ordered_answer_2, *_ = self.node(supplement['Id'], 'open')['Choices']
            ack = ordered_answer_2['Set']
            self.assertEqual(ack, ['kaylessa.wasps.courier_acknowledged'])
            state.flags.update(ack)
            self.assertFalse(rv.sim_available(self.model, supplement, state))

    def test_account_in_original_letter_keeps_original_receipt(self):
        sid = 'kaylessa.clearing.avennara'
        state = rv.SimState(5, 1000)
        state.flags.update({'kaylessa.wasps.remembered_the_courier', 'kaylessa.wasps.courier_in_first_letter'})
        choices = self.node(sid, 'receipt')['Choices']
        available = [c for c in choices if rv.sim_choice_available(c, state)]
        self.assertEqual([c['Next'] for c in available], ['courier'])
        ordered_answer_3, *_ = self.node(sid, 'courier')['Choices']
        self.assertIn('kaylessa.wasps.courier_acknowledged', ordered_answer_3['Set'])
        supplement = self.model.by_id['kaylessa.clearing.courier_reply']
        state = rv.SimState(5, 1000)
        state.flags.update(supplement['Requires'])
        state.flags.remove('kaylessa.wasps.courier_supplement_sent')
        self.assertFalse(rv.sim_available(self.model, supplement, state))

    def test_epilogue_does_not_certify_undelivered_account(self):
        paragraphs = [p for s in self.story['Scenes'] if s['Id'].startswith('kaylessa.') for n in s['Nodes'] for p in n.get('Paragraphs', []) if p.get('Requires', []) == ['kaylessa.wasps.courier_acknowledged'] and p.get('Forbids', []) == [] and (p.get('AnyGroups', []) == [])]
        self.assertTrue(paragraphs)
        self.assertTrue(paragraphs)
        for p in paragraphs:
            self.assertEqual(p['Requires'], ['kaylessa.wasps.courier_acknowledged'])

    def test_both_name_histories_perform_defense_before_aftermath(self):
        sid = 'kaylessa.clearing.once_when_it_counts'
        for name in ('name', 'name_fresh'):
            ordered_answer_4, *_ = self.node(sid, name)['Choices']
            self.assertEqual(ordered_answer_4['Next'], 'wall')
        choices = self.node(sid, 'wall')['Choices']
        self.assertEqual([c['Next'] for c in choices], ['shields', 'flank'])
        for choice in choices:
            self.assertFalse(choice['Requires'])
            self.assertFalse(choice['Check'])
            action = self.node(sid, choice['Next'])
            ordered_answer_5, *_ = action['Choices']
            self.assertEqual(ordered_answer_5['Next'], 'after')
if __name__ == '__main__':
    unittest.main()
