"""Round-four rendered custody, audience and relocation counterexamples."""
import unittest
from unittest.mock import patch

from tests import test_eritrice_round3 as r3
from storylines import eritrice_minutes as minutes
from storylines import eritrice_council as council
from storylines import eritrice_trickster as route
from tools import player_text_lint



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EritriceRoundFourTests(unittest.TestCase):
    setUp = r3.EritriceRoundThreeTests.setUp
    walk = r3.EritriceRoundThreeTests.walk

    def text(self, scene, node):
        return next(n['Text'] for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_essence_advice_keeps_alternatives_and_danger(self):
        flags = {'trickster.ever', route.STARTED, minutes.CONVENING, 'council.cauldron_given'}
        for answer, receipt in [('urged', minutes.URGED), ('warned', minutes.WARNED),
                                ('promised', minutes.PROMISED)]:
            state, visited = self.walk(minutes.ESSENCE, flags,
                                     {'start': 'pays', 'choice': answer})
            self.assertIn(receipt, state)
            self.assertNotIn(minutes.EXTRACTED, state)
            self.assertNotIn(minutes.ESSENCE_GIVEN, state)
        reviews = player_text_lint.check({'Scenes': [self.scenes[minutes.ESSENCE]]})['review']
        self.assertFalse([r for r in reviews if r['code'] == 'speaker-attribution-review'])

    def test_no_lexicon_possession_needed_for_copies(self):
        state, visited = self.walk(minutes.CIPHERED,
            {'trickster.ever', route.STARTED, minutes.POINT_ONE, minutes.CIPHER},
            {'start': 'lie', 'humbled': 'teach'})
        self.assertIn('teach', visited)
        self.assertIn(minutes.CIPHERED, state)
        self.assertFalse(any('lexicon' in flag.lower() for flag in self.scenes[minutes.CIPHERED]['Requires']))

    def test_apology_offer_matches_performed_and_consumed_audience(self):
        for branch in ('ruling', 'ruling_betrayal'):
            node = next(n for n in self.scenes[route.P + 'fought.tabled']['Nodes']
                        if n['Id'] == branch)
            answer = saved_answer(node['Choices'], 0)
            self.assertIn(route.P + 'apology_arranged', answer['Set'])
            self.assertEqual(answer['Crusade'], {'Resource': 'Favors', 'Amount': -200})
        state, _ = self.walk(route.VISIT,
                             {'trickster.ever', route.P + 'apology_arranged'}, {'open': 'apology'})
        self.assertIn(route.APOLOGISED, state)
        page = self.scenes[route.P + 'epilogue.commit']['Nodes'][0]
        apology = next(p for p in page['Paragraphs'] if route.APOLOGISED in p['Requires'])
        self.assertNotIn(route.P + 'apology_arranged', apology['Requires'])
        self.assertTrue(set(apology['Requires']) <= {route.APOLOGISED})

    def test_drezen_speech_and_articles_are_local(self):
        for sid in (minutes.STANDING, council.K + 'personal_privilege', minutes.RECORD,
                    council.TWICE, council.K + 'second_morning'):
            scene = self.scenes[sid + '.drezen']
            self.assertEqual(scene['InteractionHub'], 'eritrice.presence')
            self.assertEqual(scene['ContactUnit'], route.UNIT)
            self.assertFalse(scene.get('Remote'))

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

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.scenes[minutes.ESSENCE]
        choice = next(c for n in scene['Nodes'] if n['Id'] == 'choice'
                      for c in n['Choices'] if c['Next'] == 'urged')
        with patch.dict(choice, Set=[]):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_essence_advice_keeps_alternatives_and_danger()


if __name__ == '__main__':
    unittest.main()
