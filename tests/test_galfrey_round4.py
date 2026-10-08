"""R4 local declaration and history-dispatch regressions."""
import itertools
import unittest

from storylines import galfrey_trickster as g, galfrey_kitrane as k
from tests import test_galfrey_round2 as round2


class GalfreyRound4Tests(unittest.TestCase):
    def test_all_saved_selectors_remain_but_have_no_live_incoming_answers(self):
        count = 0
        oracle = round2.GalfreyRound2Tests()
        for scene in g.SCENES + k.SCENES:
            selectors = {n['Id']: n for n in scene['Nodes'] if '.select.' in n['Id']}
            count += len(selectors)
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
            for bits in itertools.product((False, True), repeat=len(flags)):
                state = {g.KEPT} | {flag for flag, on in zip(flags, bits) if on}
                text = oracle.traverse(scene, state)
                self.assertNotIn('There is a brief silence.', text, scene['Id'])
        self.assertEqual(34, count)

    def test_cousin_diversion_rejoins_the_unheard_declaration(self):
        for suffix in ('', '_stall'):
            scene = next(s for s in k.SCENES if s['Id'] == k.CONVERSATION + suffix)
            nodes = {n['Id']: n for n in scene['Nodes']}
            answer = nodes['eng8.cousin']['Choices'][0]
            self.assertNotIn(k.CONVERSATION, answer['Set'])
            self.assertNotIn('.select.', answer['Next'])
            self.assertEqual('said', nodes[answer['Next']]['Choices'][0]['Next'])
            self.assertIn('I wanted you', nodes['said']['Text'])
            self.assertTrue(all(k.CONVERSATION in c['Set'] for c in nodes['now']['Choices']))

    def test_postponed_answer_is_declared_before_the_commanders_reply(self):
        for name in ('alive.after_no', 'commit.answer_again', 'commit.answer_again_stall'):
            scene = next(s for s in k.SCENES if s['Id'] == g.P + name)
            nodes = {n['Id']: n for n in scene['Nodes']}
            self.assertIn('Stay tonight' if name == 'alive.after_no' else 'I want you',
                          nodes['start']['Text'])
            self.assertEqual('yes', nodes['start']['Choices'][2]['Next'])
            self.assertEqual('ally', nodes['start']['Choices'][1]['Next'])
            self.assertIn('I would rather', nodes['start']['Choices'][1]['Text'])
            self.assertNotIn('I would.', nodes['ally']['Text'])
            self.assertEqual('refused', nodes['start']['Choices'][3]['Next'])


if __name__ == '__main__':
    unittest.main()
