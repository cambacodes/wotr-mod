"""Counterexample histories for struct2-01's paid fallback and timed journey."""
import hashlib
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_available, sim_complete, sim_choice_available
from storylines import camellia_trickster as ct


class Struct2ContinuityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def state(self, hour=0, *flags):
        state = SimState(5, hour)
        state.flags.update(('trickster.ever', 'chapter_later', 'elyanka.trickster.bier_seen', *flags))
        state.times.update({flag: 0 for flag in state.flags})
        sim_complete(self.model, state)
        return state

    def test_prepared_fallback_delivers_stones_before_terminal_completion(self):
        sid = ct.P + 'killed.late_curtain_prepared'
        price = self.node(sid, 'eng8.price')
        unpaid = self.state()
        for original in price['Choices'][:2]:
            self.assertIsNone(original['Next'])
            self.assertFalse(sim_choice_available(original, unpaid))
        for acceptance in price['Choices'][3:5]:
            self.assertTrue(sim_choice_available(acceptance, unpaid))
            self.assertEqual('r2.stones', acceptance['Next'])
            self.assertIn(ct.TERMS, acceptance['Set'])
            ending = self.node(sid, acceptance['Next'])['Choices'][0]
            self.assertIn(ct.FILLED, ending['Set'])
            self.assertIsNone(ending['Next'])
        # Approved sibling delivery is reused without new Camellia voice.
        self.assertEqual(self.node(ct.P + 'killed.late_curtain', 'r2.stones')['Text'],
                         self.node(sid, 'r2.stones')['Text'])
        for suffix in ('killed.late_curtain', 'killed.third_night'):
            for acceptance in self.node(ct.P + suffix, 'eng8.price')['Choices'][:2]:
                self.assertEqual('r2.stones', acceptance['Next'])
                self.assertIn(ct.FILLED, self.node(ct.P + suffix, acceptance['Next'])['Choices'][0]['Set'])
        kept = self.node(ct.P + 'epilogue.kept', 'page')['Paragraphs']
        self.assertTrue(any(ct.FILLED in p['Requires'] for p in kept))
        committed = self.node(ct.P + 'epilogue.commit', 'page')['Paragraphs']
        for price_flag in (ct.BLED, ct.MARKED):
            self.assertTrue(any(price_flag in p['Requires'] for p in committed))
        # Refusal keeps its old position and receives no payment.
        self.assertNotIn(ct.FILLED, price['Choices'][2]['Set'])

    def test_dialogue_dispatch_cannot_advance_time_or_restore_presence(self):
        sid = 'elyanka.trickster.beat.courier'
        returned = 'elyanka.trickster.courier.returned'
        away = 'elyanka.trickster.courier.away'
        message = self.node(sid, 'message2')
        answers = ('come_back_hungry', 'ripening', 'silent')
        for index, branch in enumerate(answers):
            state = self.state(72, away)
            state.times[away] = 72
            self.assertEqual(('hungry', 'ripening', 'silent')[index], message['Choices'][index]['Next'])
            self.assertFalse(sim_choice_available(message['Choices'][index], state))
            dispatch = message['Choices'][index + 3]
            self.assertTrue(sim_choice_available(dispatch, state))
            terminal = self.node(sid, dispatch['Next'])['Choices'][0]
            self.assertIsNone(terminal['Next'])
            state.flags.update(terminal['Set'])
            state.times.update({f: state.hour for f in terminal['Set']})
            sim_complete(self.model, state)
            self.assertNotIn(returned, state.flags)
            self.assertNotIn('elyanka.present_now', state.flags)
            delivery = self.model.by_id['elyanka.trickster.beat.courier_return']
            for elapsed in (0, 48, 95):
                state.hour = 72 + elapsed
                self.assertFalse(sim_available(self.model, delivery, state), (branch, elapsed))
                self.assertFalse(sim_available(self.model, self.model.by_id['elyanka.trickster.beat.anatomy'], state))
            state.hour = 168
            self.assertTrue(sim_available(self.model, delivery, state), branch)
            state.chapter = 6
            self.assertTrue(sim_available(self.model, delivery, state), 'return survives chapter transition')
            state.chapter = 5
            start = self.node(delivery['Id'], 'start')
            enabled = [c for c in start['Choices'] if sim_choice_available(c, state)]
            self.assertEqual(1, len(enabled))
            result = self.node(delivery['Id'], enabled[0]['Next'])['Choices'][0]
            self.assertEqual([returned], result['Set'])
            state.flags.update(result['Set'])
            state.times[returned] = state.hour
            sim_complete(self.model, state)
            self.assertIn('elyanka.present_now', state.flags)
            # A later independent loss cannot be lifted by this courier return.
            state.flags.add('elyanka.returned_actor_lost')
            sim_complete(self.model, state)
            self.assertNotIn('elyanka.present_now', state.flags)

    def test_master_is_optional_and_anchors_to_latest_answer(self):
        master = self.model.by_id['elyanka.trickster.beat.master']
        state = self.state(119)
        self.assertFalse(sim_available(self.model, master, state))
        state.hour = 120
        self.assertTrue(sim_available(self.model, master, state))
        for answer in ('come_back_hungry', 'ripening', 'silent'):
            state = self.state(191, 'elyanka.trickster.courier.' + answer)
            state.times['elyanka.trickster.courier.' + answer] = 72
            self.assertFalse(sim_available(self.model, master, state))
            state.hour = 192
            self.assertTrue(sim_available(self.model, master, state))

if __name__ == '__main__':
    unittest.main()
