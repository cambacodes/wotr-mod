"""R4 local declaration and history-dispatch regressions."""
import itertools
import copy
import unittest
from unittest.mock import patch

from storylines import galfrey_trickster as g, galfrey_kitrane as k
from tests import test_galfrey_round2 as round2



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class GalfreyRound4Tests(unittest.TestCase):
    def test_all_saved_selectors_remain_but_have_no_live_incoming_answers(self):
        saved_selectors = set()
        oracle = round2.GalfreyRound2Tests()
        for scene in g.SCENES + k.SCENES:
            selectors = {n['Id']: n for n in scene['Nodes'] if '.select.' in n['Id']}
            saved_selectors.update((scene["Id"], key) for key in selectors)
            if not selectors:
                continue
            flags = sorted({flag for node in selectors.values() for c in node['Choices']
                            for field in ('Requires', 'Forbids') for flag in c[field]})
            for node in scene['Nodes']:
                if node['Id'] in selectors:
                    continue
                for choice in node['Choices']:
                    if scene['Id'] in choice['Requires']:
                        continue  # Retired structural links require completion.
                    self.assertNotIn(choice.get('Next'), selectors, (scene['Id'], node['Id']))
                # Every history has a path with selectable answers, including
                # the nested King/crown variants and the stall copies.
            histories = [set()]
            for flag in flags:
                histories += [history | {flag} for history in histories]
            for history in histories:
                state = {g.KEPT} | history
                reached = oracle.traverse(scene, state)
                self.assertFalse({key for key in reached if ".select." in key})
        self.assertTrue(saved_selectors)

    def test_cousin_diversion_rejoins_the_unheard_declaration(self):
        for suffix in ('', '_stall'):
            scene = next(s for s in k.SCENES if s['Id'] == k.CONVERSATION + suffix)
            nodes = {n['Id']: n for n in scene['Nodes']}
            answer = saved_answer(nodes['eng8.cousin']['Choices'], 0)
            self.assertNotIn(k.CONVERSATION, answer['Set'])
            self.assertNotIn('.select.', answer['Next'])
            self.assertEqual('said', saved_answer(nodes[answer['Next']]['Choices'], 0)['Next'])
            self.assertEqual([c['Next'] for c in nodes['said']['Choices']], ['now'])
            self.assertTrue(all(k.CONVERSATION in c['Set'] for c in nodes['now']['Choices']))

    def test_postponed_answer_is_declared_before_the_commanders_reply(self):
        for name in ('alive.after_no', 'commit.answer_again', 'commit.answer_again_stall'):
            scene = next(s for s in k.SCENES if s['Id'] == g.P + name)
            nodes = {n['Id']: n for n in scene['Nodes']}
            self.assertEqual('yes', saved_answer(nodes['start']['Choices'], 2)['Next'])
            self.assertEqual('ally', saved_answer(nodes['start']['Choices'], 1)['Next'])
            self.assertTrue(all(g.COMMITTED not in c['Set'] for c in nodes['ally']['Choices']))
            self.assertEqual('refused', saved_answer(nodes['start']['Choices'], 3)['Next'])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scenes = copy.deepcopy(k.SCENES)
        scene = next(s for s in scenes if s['Id'] == k.CONVERSATION)
        choice = next(n for n in scene['Nodes'] if n['Id'] == 'eng8.cousin')['Choices'][0]
        choice['Set'] = [k.CONVERSATION]
        with patch.object(k, 'SCENES', scenes):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_cousin_diversion_rejoins_the_unheard_declaration()


if __name__ == '__main__':
    unittest.main()
