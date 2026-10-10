"""Route histories from the generated payload, including derived availability."""
import unittest
from unittest.mock import patch

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete, sim_available



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class ElyankaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def flags(self, *history):
        state = SimState(5, 1000)
        state.flags.update(('trickster', 'chapter_later', *history))
        sim_complete(self.model, state)
        return state.flags

    @staticmethod
    def enabled(item, flags):
        return (all(f in flags for f in item.get('Requires', []))
                and not any(f in flags for f in item.get('Forbids', []))
                and all(any(f in flags for f in g) for g in item.get('RequiresAnyGroups', []))
                and all(any(f in flags for f in g) for g in item.get('AnyGroups', [])))

    def node(self, scene, node):
        return next(n for n in self.scenes['elyanka.trickster.' + scene]['Nodes'] if n['Id'] == node)

    def test_funeral_recollection_does_not_require_living_tirabades(self):
        scene = self.scenes['elyanka.trickster.door.hearse']
        for funeral in ('king', 'partisans_a', 'partisans_b', 'fye'):
            for returned in ((), ('anevia.trickster.returned', 'irabeth.trickster.returned')):
                flags = self.flags('iz.done', 'anevia_gone', 'irabeth_dead',
                                   'elyanka.funeral.' + funeral, *returned)
                self.assertTrue(self.enabled(scene, flags), (funeral, returned))

    def test_goddess_romance_refusal_does_not_block_corpse_test(self):
        scene = self.scenes['elyanka.trickster.test.the_dead']
        for seelah in ((), ('seelah.in_party',), ('seelah_dead',)):
            self.assertTrue(self.enabled(scene, self.flags(
                'elyanka.trickster.owned', 'iomedae.closed', *seelah)))

    def test_both_morning_answers_and_horse_receipts_after_daeran_loss(self):
        cord = self.node('visit.hearse', 'cord')
        for loss in ('daeran.dead', 'daeran.kicked_out', 'daeran.plot_absent', 'daeran.in_party'):
            flags = self.flags(loss, 'elyanka.committed')
            for index in (2, 3):
                answer = saved_answer(cord['Choices'], index)
                self.assertTrue(self.enabled(answer, flags))
                reply = self.node('visit.hearse', answer['Next'])
                self.assertIn('elyanka.trickster.bier_seen', saved_answer(reply['Choices'], 0)['Set'])
                continuation = self.node('visit.hearse', saved_answer(reply['Choices'], 0)['Next'])
                exits = [c for c in continuation['Choices'] if self.enabled(c, flags)]
                self.assertEqual(['horses'], [c['Next'] for c in exits])
            self.assertIn('elyanka.trickster.horses_balked',
                          saved_answer(self.node('visit.hearse', 'horses2')['Choices'], 0)['Set'])

    def test_targona_recollection_requires_current_presence(self):
        choices = self.node('beat.table', 'welcome')['Choices']
        for history in ((), ('targona.trickster.returned',),
                        ('targona.trickster.returned', 'targona.returned_actor_lost'),
                        ('targona.trickster.returned', 'targona.epoch_unavailable')):
            # Loss occurred long before yesterday; a historical return cannot date a visit.
            flags = self.flags(*history)
            enabled = [c['Next'] for c in choices if self.enabled(c, flags)]
            self.assertEqual(['targona'] if 'targona.present_now' in flags
                             and 'targona.trickster.in_drezen' in flags else ['choose'], enabled)

    def test_dismissed_creditor_gets_only_distant_sacrifice_ending(self):
        flags = self.flags('elyanka.trickster.left_free', 'elyanka.trickster.owned',
                           'elyanka.closed', 'sacrifice')
        scene = self.scenes['elyanka.trickster.epilogue.left_free_mourned']
        self.assertTrue(self.enabled(scene, flags))
        text = scene['Nodes'][0]['Text'] + ' '.join(
            p['Text'] for p in scene['Nodes'][0]['Paragraphs'] if self.enabled(p, flags))
        self.assertFalse(self.enabled(self.scenes['elyanka.trickster.epilogue.eaten'], flags))
        for blocker in ('trickster.commander_back', 'lastcall.active'):
            self.assertFalse(self.enabled(scene, flags | {blocker}))

    def test_minimum_and_delayed_delivery_have_consistent_accounts(self):
        for delay in (24, 24 * 21):
            state = SimState(5, delay)
            state.flags.update(('trickster', 'elyanka.trickster.executor',
                                'elyanka.trickster.door_seen'))
            sim_complete(self.model, state)
            state.times.update({f: 0 for f in state.flags})
            scene = self.model.by_id['elyanka.trickster.executor.haggle']
            self.assertTrue(sim_available(self.model, scene, state))
            state.hour = 23
            self.assertFalse(sim_available(self.model, scene, state))
        for delay in (48, 24 * 21):
            state = SimState(5, delay)
            state.flags.update(('trickster', 'elyanka.trickster.declined',
                                'elyanka.trickster.owned', 'elyanka.trickster.tested'))
            sim_complete(self.model, state)
            state.times.update({f: 0 for f in state.flags})
            scene = self.model.by_id['elyanka.trickster.commit.her_move']
            self.assertTrue(sim_available(self.model, scene, state))
            state.hour = 47
            self.assertFalse(sim_available(self.model, scene, state))

    def test_horse_and_warning_consequences_follow_their_causes(self):
        for receipt in ('horses_balked', 'tyrant.lastwall_warned', 'master.killed'):
            flag = 'elyanka.trickster.' + receipt
            readers = [p for p in self.node('epilogue.claim', 'page')['Paragraphs'] if flag in p['Requires']]
            self.assertTrue(readers, flag)
            self.assertTrue(all(self.enabled(p, self.flags(flag)) for p in readers))
            self.assertTrue(all(not self.enabled(p, self.flags()) for p in readers))
        self.assertIn('elyanka.trickster.horses_balked', saved_answer(self.node('visit.hearse', 'horses2')['Choices'], 0)['Set'])

    def test_nidalynn_flight_removes_only_the_question(self):
        flags = self.flags('nidalynn.started', 'nidalynn.closed', 'nidalynn.trickster.left_with_it')
        choices = self.node('beat.table', 'choose')['Choices']
        self.assertFalse(self.enabled(saved_answer(choices, 3), flags))
        self.assertFalse(self.enabled(saved_answer(choices, 3), self.flags('nidalynn.started', 'nidalynn.closed')))
        self.assertTrue(all(self.enabled(c, flags) for c in choices[:3]))

    def test_dispatched_wine_survives_sender_loss_without_annual_visits(self):
        delivery = self.scenes['elyanka.trickster.beat.daeran_bottle']
        receipt = 'elyanka.trickster.daeran.bottle_tasted'
        readers = [p for p in self.node('epilogue.claim', 'page')['Paragraphs'] if receipt in p['Requires']]
        self.assertTrue(readers)
        for loss in ('daeran.dead', 'daeran.kicked_out', 'daeran.plot_absent'):
            self.assertTrue(self.enabled(delivery, self.flags('elyanka.trickster.daeran_ally', loss)))
            selected, = [p for p in readers if self.enabled(p, self.flags('elyanka.trickster.daeran_ally', receipt, loss))]
            self.assertEqual(selected['Forbids'], [])
            self.assertEqual(selected['AnyGroups'], [['daeran.dead', 'daeran.kicked_out', 'daeran.plot_absent']])
            self.assertTrue(all(not self.enabled(p, self.flags('elyanka.trickster.daeran_ally', loss)) for p in readers))

    def test_final_camp_location_and_single_slot_continuity(self):
        self.assertEqual("d80bdee55139ac24583f337a53878021", self.story["Etudes"]["daeran.plot_absent"])
        self.assertEqual(['10c4b0e2af186ba46ab4d238d00a40a8'],
                         self.scenes['elyanka.trickster.ch6.collateral']['Areas'])
        slot = self.node('visit.hearse', 'elyanka.trickster.visit.hearse.explicit.1')
        self.assertEqual(slot['Id'], saved_answer(self.node('visit.hearse', 'threshold')['Choices'], 0)['Next'])
        self.assertEqual('morning', saved_answer(slot['Choices'], 0)['Next'])
        self.assertFalse(saved_answer(slot['Choices'], 0)['Set'])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.model.by_id['elyanka.trickster.executor.haggle']
        with patch.dict(scene, DelayHours=0):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_minimum_and_delayed_delivery_have_consistent_accounts()


if __name__ == '__main__':
    unittest.main()
