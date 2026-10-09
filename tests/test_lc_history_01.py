"""Dorgelinda Last Call admission and history variants through the export."""
import unittest

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_available, sim_complete

D = 'dorgelinda.trickster.'


class LastCallHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = Model(fresh_story())
        cls.scenes = {s['Id']: s for s in cls.model.scenes}

    def state(self, *history):
        state = SimState(6, 1000)
        state.flags.update(('trickster.ever', 'trickster', 'chapter_later',
                            'trickster.lastcall.taken', 'ending.trickster',
                            'lastcall.commander_returned', *history))
        sim_complete(self.model, state)
        return state

    def test_retained_carts_remain_callable_after_settlement(self):
        state = self.state('dorgelinda.committed', D + 'cost.carts_signed', D + 'cost.told_all')
        self.assertIn('dorgelinda.lastcall.callable', state.flags)
        state.flags.add('dorgelinda.lastcall.resolved')
        sim_complete(self.model, state)
        self.assertNotIn('dorgelinda.lastcall.callable', state.flags)

    def test_commitment_overrides_historical_decline_for_page_admission(self):
        for committed, expected in ((False, False), (True, True)):
            with self.subTest(committed=committed):
                history = [D + 'declined', D + 'cost.carts_signed', D + 'cost.told_all']
                if committed:
                    history.append('dorgelinda.committed')
                self.assertEqual(expected, sim_available(
                    self.model, self.scenes['dorgelinda.lastcall.page'], self.state(*history)))
