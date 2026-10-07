"""Route histories from the generated payload, including derived availability."""
import unittest

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete, sim_available


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
                answer = cord['Choices'][index]
                self.assertTrue(self.enabled(answer, flags))
                reply = self.node('visit.hearse', answer['Next'])
                self.assertIn('elyanka.trickster.bier_seen', reply['Choices'][0]['Set'])
                continuation = self.node('visit.hearse', reply['Choices'][0]['Next'])
                exits = [c for c in continuation['Choices'] if self.enabled(c, flags)]
                self.assertEqual(['horses'], [c['Next'] for c in exits])
            self.assertIn('elyanka.trickster.horses_balked',
                          self.node('visit.hearse', 'horses2')['Choices'][0]['Set'])

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
        self.assertIn('in Ustalav, months late', text)
        self.assertIn('no flesh to fetch', text)
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
            self.assertIn('these orders stand', self.node('door.hearse', 'plan')['Text'])
            self.assertIn('still not been shown', self.node('executor.haggle', 'why')['Text'])
            self.assertNotIn('a day and a night', self.node('executor.haggle', 'why')['Text'])
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
            self.assertIn('Since that supper', self.node('commit.her_move', 'hair')['Text'])
            self.assertNotIn('Two days', self.node('commit.her_move', 'hair')['Text'])

    def test_full_claim_page_respects_all_inquiry_outcomes(self):
        for inquiry in (None, 'told_seelah', 'misled', 'hers'):
            history = ['elyanka.committed', 'trickster.secret.elyanka_rites']
            if inquiry:
                history.append('elyanka.trickster.inquiry.' + inquiry)
            flags = self.flags(*history)
            text = ' '.join(p['Text'] for p in self.node('epilogue.claim', 'page')['Paragraphs']
                            if self.enabled(p, flags))
            self.assertEqual(inquiry is None, 'nobody in authority ever came' in text)
            self.assertEqual(inquiry is not None, 'counted the guests' in text)

    def test_horse_and_warning_consequences_follow_their_causes(self):
        self.assertIn('door slips from your hand', self.node('visit.hearse', 'horses')['Text'])
        self.assertNotIn('trained to carry the dead', self.node('visit.hearse', 'horses')['Text'])
        flags = self.flags('elyanka.trickster.horses_balked', 'elyanka.trickster.tyrant.lastwall_warned',
                           'elyanka.trickster.master.killed')
        text = ' '.join(p['Text'] for p in self.node('epilogue.claim', 'page')['Paragraphs']
                        if self.enabled(p, flags))
        self.assertIn('glass rattled', text)
        self.assertIn('hopes to investigate', text)
        self.assertIn('next envoy came with armed attendants', text)
        self.assertNotIn('watched more closely', text)
        self.assertNotIn('Way sent no one else', text)

    def test_nidalynn_flight_removes_only_the_question(self):
        flags = self.flags('nidalynn.started', 'nidalynn.closed', 'nidalynn.trickster.left_with_it')
        choices = self.node('beat.table', 'choose')['Choices']
        self.assertFalse(self.enabled(choices[3], flags))
        self.assertFalse(self.enabled(choices[3], self.flags('nidalynn.started', 'nidalynn.closed')))
        self.assertTrue(all(self.enabled(c, flags) for c in choices[:3]))

    def test_dispatched_wine_survives_sender_loss_without_annual_visits(self):
        delivery = self.scenes['elyanka.trickster.beat.daeran_bottle']
        for loss in ('daeran.dead', 'daeran.kicked_out', 'daeran.plot_absent'):
            flags = self.flags('elyanka.trickster.daeran_ally', loss)
            self.assertTrue(self.enabled(delivery, flags), loss)
            self.assertIn('dispatched', self.node('beat.daeran_bottle', 'her')['Text'])
            flags = self.flags('elyanka.trickster.daeran_ally',
                               'elyanka.trickster.daeran.bottle_tasted', loss)
            texts = [p['Text'] for p in self.node('epilogue.claim', 'page')['Paragraphs']
                     if self.enabled(p, flags)]
            self.assertTrue(any('bottle dispatched' in t for t in texts))
            self.assertTrue(any('kept the cork' in t for t in texts))
            self.assertFalse(any('Every year' in t and 'Arendae' in t for t in texts))

    def test_inquiry_receipt_follows_spoken_confession(self):
        truth = self.node('beat.inquiry', 'truth')['Choices'][0]
        self.assertFalse(truth['Set'])
        self.assertEqual('confess', truth['Next'])
        answer = self.node('beat.inquiry', 'confess')['Choices'][0]
        reply = self.node('beat.inquiry', answer['Next'])
        self.assertIn('witness', reply['Text'])
        self.assertIn('elyanka.trickster.inquiry.told_seelah', reply['Choices'][0]['Set'])

    def test_historical_debts_survive_later_witness_loss_in_all_four_endings(self):
        for ending in ('claim', 'debt', 'lock', 'left_free'):
            paragraphs = self.node('epilogue.' + ending, 'page')['Paragraphs']
            for inquiry in ('told_seelah', 'misled', 'hers'):
                for loss in ('seelah_dead', 'seelah_gone'):
                    flags = self.flags('elyanka.trickster.gave_dead', 'elyanka.trickster.seelah_prayed',
                                       'elyanka.trickster.inquiry.' + inquiry, loss)
                    texts = [p['Text'] for p in paragraphs if self.enabled(p, flags)]
                    self.assertEqual(1, sum('They went south to Ustalav' in t for t in texts))
                    self.assertTrue(any('witness' in t for t in texts), (ending, inquiry, loss))

    def test_final_camp_location_and_single_slot_continuity(self):
        self.assertEqual("d80bdee55139ac24583f337a53878021", self.story["Etudes"]["daeran.plot_absent"])
        self.assertEqual(['10c4b0e2af186ba46ab4d238d00a40a8'],
                         self.scenes['elyanka.trickster.ch6.collateral']['Areas'])
        slot = self.node('visit.hearse', 'elyanka.trickster.visit.hearse.explicit.1')
        self.assertEqual(slot['Id'], self.node('visit.hearse', 'threshold')['Choices'][0]['Next'])
        self.assertEqual('morning', slot['Choices'][0]['Next'])
        self.assertFalse(slot['Choices'][0]['Set'])
        self.assertIn('mourning candles burn down to their sockets', slot['Text'])


if __name__ == '__main__':
    unittest.main()
