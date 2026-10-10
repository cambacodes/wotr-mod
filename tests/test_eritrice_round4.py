"""Round-four rendered custody, audience and relocation counterexamples."""
import unittest

from tests import test_eritrice_round3 as r3
from storylines import eritrice_minutes as minutes
from storylines import eritrice_council as council
from storylines import eritrice_trickster as route
from tools import player_text_lint


class EritriceRoundFourTests(unittest.TestCase):
    setUp = r3.EritriceRoundThreeTests.setUp
    walk = r3.EritriceRoundThreeTests.walk

    def text(self, scene, node):
        return next(n['Text'] for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_essence_advice_keeps_alternatives_and_danger(self):
        flags = {'trickster.ever', route.STARTED, minutes.CONVENING, 'council.cauldron_given'}
        for answer, receipt in [('urged', minutes.URGED), ('warned', minutes.WARNED),
                                ('promised', minutes.PROMISED)]:
            state, prose = self.walk(minutes.ESSENCE, flags,
                                     {'start': 'pays', 'choice': answer})
            self.assertIn(receipt, state)
            self.assertNotIn(minutes.EXTRACTED, state)
            self.assertNotIn(minutes.ESSENCE_GIVEN, state)
            self.assertIn('Now it is my essence', prose)
            self.assertNotIn('Everyone else on this Council is hoping', prose)
        self.assertIn('those are my arguments too', self.text(minutes.ESSENCE, 'urged'))
        self.assertIn('Willingly, or by force', self.text(minutes.ESSENCE, 'warned'))
        reviews = player_text_lint.check({'Scenes': [self.scenes[minutes.ESSENCE]]})['review']
        self.assertFalse([r for r in reviews if r['code'] == 'speaker-attribution-review'])

    def test_no_lexicon_possession_needed_for_copies(self):
        # No inventory/possession flag: the Council returned the original.
        _, prose = self.walk(minutes.CIPHERED,
                             {'trickster.ever', route.STARTED, minutes.POINT_ONE, minutes.CIPHER},
                             {'start': 'lie', 'humbled': 'teach'})
        self.assertIn('Her copies of the Lexicon', prose)
        self.assertIn('before returning it to you', prose)
        self.assertNotIn('turns the book', prose)
        for suffix in ('', '.drezen'):
            self.assertNotIn('a Lexicon page', self.text(minutes.BLANK + suffix, 'open'))

    def test_apology_offer_matches_performed_and_consumed_audience(self):
        for branch in ('ruling', 'ruling_betrayal'):
            node = next(n for n in self.scenes[route.P + 'fought.tabled']['Nodes']
                        if n['Id'] == branch)
            self.assertIn('circulated to the Council', node['Text'])
            answer = node['Choices'][0]
            self.assertIn('circulate the apology', answer['Text'])
            self.assertIn(route.P + 'apology_arranged', answer['Set'])
            self.assertEqual(answer['Crusade'], {'Resource': 'Favors', 'Amount': -200})
        state, _ = self.walk(route.VISIT,
                             {'trickster.ever', route.P + 'apology_arranged'}, {'open': 'apology'})
        self.assertIn(route.APOLOGISED, state)
        page = self.scenes[route.P + 'epilogue.commit']['Nodes'][0]
        apology = next(p for p in page['Paragraphs'] if route.APOLOGISED in p['Requires'])
        self.assertIn('spoken to Eritrice at the special sitting', apology['Text'])
        self.assertNotIn('reconvened Council', apology['Text'])

    def test_drezen_speech_and_articles_are_local(self):
        self.assertIn('to the borrowed room', self.text(minutes.STANDING + '.drezen', 'close'))
        for suffix in ('', '.drezen'):
            self.assertNotIn('never seen her do', self.text(minutes.STANDING + suffix, 'close'))
        self.assertIn('my borrowed table', self.text(council.K + 'personal_privilege.drezen', 'both'))
        self.assertIn('under the chair', self.text(minutes.RECORD + '.drezen', 'start'))
        self.assertIn('seat of the chair', self.text(council.TWICE + '.drezen', 'open'))
        self.assertIn('on the empty chair', self.text(council.TWICE + '.drezen', 'start'))
        self.assertIn('under the chair', self.text(council.K + 'second_morning.drezen', 'morning'))

    def test_repeat_night_and_morning_share_position(self):
        from tests.story_fixture import fresh_story
        from tests.fix16b_structure import reachable_nodes
        from tools import rrt_verify as verify
        story = fresh_story()
        model = verify.Model(story)
        receipt = council.TWICE + '_carried'
        for suffix in ('', '.drezen'):
            night = model.by_id[council.TWICE + suffix]
            nodes = {n['Id']: n for n in night['Nodes']}
            slot = council.TWICE + '.explicit.1'
            self.assertIn(slot, reachable_nodes(night))
            self.assertEqual([(slot, [receipt])],
                             [(c['Next'], c['Set']) for c in nodes['carried']['Choices']])
            self.assertEqual([([council.TWICE] if suffix else [])], [c['Set'] for c in nodes[slot]['Choices']])
            morning = model.by_id[council.K + 'second_morning' + suffix]
            self.assertIn(receipt, morning['Requires'])
            state = verify.SimState(5, 100)
            state.flags.update(morning['Requires'])
            self.assertTrue(verify.sim_available(model, morning, state))
            state.flags.discard(receipt)
            self.assertFalse(verify.sim_available(model, morning, state))


if __name__ == '__main__':
    unittest.main()
