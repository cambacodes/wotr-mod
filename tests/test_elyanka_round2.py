"""Route histories from the generated payload, including derived availability."""
import unittest

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete


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
        for loss in ('daeran.dead', 'daeran.kicked_out', 'daeran.plot_absent'):
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
