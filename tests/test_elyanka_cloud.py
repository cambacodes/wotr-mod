"""villain-route-elyanka (cloud): structure and reader acceptance for the design-first pass."""
import unittest

from tests.story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete

E = 'elyanka.trickster.'


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
        check = stag[2]['Check']
        self.assertEqual(('SkillAthletics', 'held', 'gored'), (check['Skill'], check['Success'], check['Failure']))
        self.assertGreater(check['DC'], 0)
        for outcome, flag in (('held', E + 'hunt.held'), ('gored', E + 'hunt.gored')):
            answer = self.node('beat.hunt', outcome)['Choices']
            self.assertEqual([('fire', [flag])], [(c['Next'], c['Set']) for c in answer])
        self.assertNotIn('antlers and your arms', self.node('beat.hunt', 'kill_quick')['Text'])

    def test_both_hunt_histories_have_their_own_reader(self):
        base = (E + 'owned', E + 'tested', 'elyanka.committed', E + 'bier_seen', E + 'hunt.ate')
        held = self.shown('epilogue.claim', 'page', self.flags(*base, E + 'hunt.held'))
        gored = self.shown('epilogue.claim', 'page', self.flags(*base, E + 'hunt.gored'))
        self.assertIn('by the antlers', held)
        self.assertNotIn("tine left", held)
        self.assertIn("tine left", gored)
        self.assertNotIn('by the antlers', gored)
        scar = self.shown('ch6.collateral', 'inspect', self.flags(*base, E + 'hunt.gored'))
        self.assertIn("hart's tine", scar)
        self.assertEqual('', self.shown('ch6.collateral', 'inspect', self.flags(*base, E + 'hunt.held')))

    def test_chapter5_promises_are_read_in_her_epilogue(self):
        base = (E + 'owned', E + 'tested', 'elyanka.committed', E + 'bier_seen')
        for flag, phrase in ((E + 'table.left', 'would not sit, and would not tell'),
                             (E + 'tyrant.told_her', 'No knight of Lastwall'),
                             (E + 'anatomy.left', '"Burn it, then,"'),
                             (E + 'ustalav.woods', 'black circle'),
                             (E + 'ustalav.refused', 'never went to Ustalav alive'),
                             (E + 'fitting.refused', 'planed the shoulders')):
            with self.subTest(flag=flag):
                self.assertIn(phrase, self.shown('epilogue.claim', 'page', self.flags(*base, flag)))
                self.assertNotIn(phrase, self.shown('epilogue.claim', 'page', self.flags(*base)))

    def test_master_dies_on_screen_not_in_a_report(self):
        # Behaviour, not wording: the killing is a shown node in a scene the Commander attends in person
        # (a visit or event), never a letter, sending or memory that reports it afterwards.
        scene = self.scenes[E + 'beat.master']
        self.assertIn(scene.get('Kind'), ('visit', 'event'))
        kill = self.node('beat.master', 'kill2')
        self.assertTrue(kill['Text'].strip())
        self.assertEqual([E + 'master.killed'], kill['Choices'][0]['Set'])

    def test_no_paperwork_collector(self):
        texts = []
        for sid in ('trickster.lastcall.page.collectors', 'elyanka.lastcall.page', E + 'epilogue.claim', E + 'epilogue.debt'):
            for n in self.scenes[sid]['Nodes']:
                texts += [p['Text'] for p in n.get('Paragraphs', [])]
        joined = ' '.join(texts)
        for phrase in ('on file', 'possession was refused', 'refused possession', 'He returned to Caliphas',
                       'presented her bequest', 'took their names to the chaplains'):
            self.assertNotIn(phrase, joined)

    def test_hanging_reveals_the_carts_to_seelah_in_the_ledger(self):
        entry = next(e for e in self.story['Books']['trickster.ledger']['Entries'] if e['Id'] == 'secret.elyanka_siege_dead')
        self.assertIn(E + 'inquiry.misled', entry['Lines'][0]['Forbids'])
        self.assertIn('trickster.secret.elyanka_siege_dead.known.seelah', entry['Lines'][0]['Forbids'])


if __name__ == '__main__':
    unittest.main()
