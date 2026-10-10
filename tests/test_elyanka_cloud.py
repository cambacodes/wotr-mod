"""villain-route-elyanka (cloud): structure and reader acceptance for the design-first pass."""
import unittest
from unittest.mock import patch

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete

E = 'elyanka.trickster.'



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class ElyankaCloudTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def flags(self, *history):
        state = SimState(6, 1000)
        state.flags.update(('trickster', 'trickster.ever', 'chapter_later', *history))
        sim_complete(self.model, state)
        return state.flags

    @staticmethod
    def enabled(item, flags):
        return (all(f in flags for f in item.get('Requires', []))
                and not any(f in flags for f in item.get('Forbids', []))
                and all(any(f in flags for f in g) for g in item.get('RequiresAnyGroups', []))
                and all(any(f in flags for f in g) for g in item.get('AnyGroups', [])))

    def node(self, scene, node):
        return next(n for n in self.scenes[E + scene]['Nodes'] if n['Id'] == node)

    def shown(self, scene, node, flags):
        n = self.node(scene, node)
        return ' '.join(p['Text'] for p in n.get('Paragraphs', []) if self.enabled(p, flags))

    def test_hunt_interception_is_a_checked_answer_with_two_outcomes(self):
        stag = self.node('beat.hunt', 'stag')['Choices']
        self.assertEqual(['kill', 'kill_quick'], [c['Next'] for c in stag[:2]])
        check = saved_answer(stag, 2)['Check']
        self.assertEqual(('SkillAthletics', 'held', 'gored'), (check['Skill'], check['Success'], check['Failure']))
        self.assertGreater(check['DC'], 0)
        for outcome, flag in (('held', E + 'hunt.held'), ('gored', E + 'hunt.gored')):
            answer = self.node('beat.hunt', outcome)['Choices']
            self.assertEqual([('fire', [flag])], [(c['Next'], c['Set']) for c in answer])

    def test_both_hunt_histories_have_their_own_reader(self):
        for suffix in ('held', 'gored'):
            receipt = E + 'hunt.' + suffix
            readers = [p for p in self.node('epilogue.claim', 'page')['Paragraphs'] if receipt in p['Requires']]
            self.assertTrue(readers)
            self.assertTrue(all(self.enabled(p, self.flags(receipt)) for p in readers))
            self.assertTrue(all(not self.enabled(p, self.flags()) for p in readers))
        scar = [p for p in self.node('ch6.collateral', 'inspect')['Paragraphs'] if E + 'hunt.gored' in p['Requires']]
        self.assertTrue(scar)
        self.assertTrue(all(self.enabled(p, self.flags(E + 'hunt.gored')) for p in scar))
        self.assertTrue(all(not self.enabled(p, self.flags(E + 'hunt.held')) for p in scar))

    def test_chapter5_promises_are_read_in_her_epilogue(self):
        for suffix in ('table.left', 'tyrant.told_her', 'anatomy.left', 'ustalav.woods', 'ustalav.refused', 'fitting.refused'):
            flag = E + suffix
            readers = [p for p in self.node('epilogue.claim', 'page')['Paragraphs'] if flag in p['Requires']]
            self.assertTrue(readers, flag)
            self.assertTrue(all(self.enabled(p, self.flags(flag)) for p in readers))
            self.assertTrue(all(not self.enabled(p, self.flags()) for p in readers))

    def test_master_dies_on_screen_not_in_a_report(self):
        # Behaviour, not wording: the killing is a shown node in a scene the Commander attends in person
        # (a visit or event), never a letter, sending or memory that reports it afterwards.
        scene = self.scenes[E + 'beat.master']
        self.assertIn(scene.get('Kind'), ('visit', 'event'))
        kill = self.node('beat.master', 'kill2')
        self.assertEqual([c['Next'] for c in self.node('beat.master', 'kill')['Choices']], ['kill2'])
        self.assertEqual([E + 'master.killed'], saved_answer(kill['Choices'], 0)['Set'])


    def test_hanging_reveals_the_carts_to_seelah_in_the_ledger(self):
        entry = next(e for e in self.story['Books']['trickster.ledger']['Entries'] if e['Id'] == 'secret.elyanka_siege_dead')
        self.assertIn(E + 'inquiry.misled', entry['Lines'][0]['Forbids'])
        self.assertIn('trickster.secret.elyanka_siege_dead.known.seelah', entry['Lines'][0]['Forbids'])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        check = next(c['Check'] for c in self.node('beat.hunt', 'stag')['Choices'] if c.get('Check'))
        with patch.dict(check, Success='gored'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_hunt_interception_is_a_checked_answer_with_two_outcomes()


if __name__ == '__main__':
    unittest.main()
