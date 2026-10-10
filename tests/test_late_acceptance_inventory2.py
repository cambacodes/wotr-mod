"""eng8-q8h: false-acceptance and infeasible-consumer mutations are hard L4 findings."""
from tests.story_fixture import fresh_story

import copy
import json
from pathlib import Path
import unittest
from tools import rrt_verify as V
from tools.crossroute_checks import late_commitment
from tools.crossroute_checks.common import Proof, blocks
ROOT = Path(__file__).resolve().parents[1]

class LateAcceptanceInventory2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.inventory = json.loads((ROOT / 'tools/late_acceptance_inventory2_contracts.json').read_text(encoding="utf-8"))

    def errors(self, story):
        model = V.Model(story)
        selected = [b for b in blocks(model) if b.route in {'arsinoe', 'nenio', 'terendelev', 'kiana'}]
        return [f for f in late_commitment.acceptance_inventory_check(model, selected, Proof(model))
                if f['subject'] in {'late-acceptance', 'permanent-acceptance', 'producer-consumer'}]

    def test_generated_acceptance_inventory(self):
        self.assertEqual(len(self.inventory['finding_ids']), 13)
        self.assertEqual(self.errors(self.story), [])

    def test_refusal_keeps_saved_generic_continue_identity(self):
        scene = next((s for s in self.story['Scenes'] if s['Id'] == 'kiana.trickster.epilogue.commit'))
        blank = next((n for n in scene['Nodes'] if n['Id'] == 'blank'))
        self.assertIn('kiana.trickster.late_no', blank['EnterSet'])
        legacy_answer, = blank['Choices']
        self.assertIsNone(legacy_answer['Next'])
        ordered_answer_1, *_ = blank['Choices']
        answer = ordered_answer_1
        self.assertIsNone(answer['Next'])
        self.assertEqual(answer['Set'], [])
        self.assertEqual(answer['Requires'], [])
        self.assertEqual(answer['Forbids'], [])
        self.assertFalse(answer['Abort'])
        self.assertIsNone(answer.get('Check'))
        self.assertIsNone(answer.get('Revive'))

    def test_each_readiness_shortcut_is_rejected(self):
        for route, shortcut in [('arsinoe', 'arsinoe.trickster.stays_to_collect'),
                                ('nenio', 'nenio.started'),
                                ('terendelev', 'terendelev.trickster.first_night_seen')]:
            with self.subTest(route=route):
                broken = copy.deepcopy(self.story)
                key = route + '.trickster.late_committed'
                broken['Derived'][key] = [['trickster.ever', shortcut, route + '.outcome.route_open']]
                self.assertTrue(self.errors(broken))

    def test_both_hubs_and_release_require_documented_development(self):
        for sid in self.inventory['commit_consumers']:
            with self.subTest(scene=sid):
                broken = copy.deepcopy(self.story)
                scene = next(s for s in broken['Scenes'] if s['Id'] == sid)
                scene['Requires'].remove('terendelev.trickster.watch.proof_seen')
                self.assertTrue(self.errors(broken))

    def test_affirmative_consumer_cannot_require_its_own_yes_or_set_blocker(self):
        for index in (3, 4):
            for mutation in ('requires_yes', 'joint_commit', 'contradiction', 'missing_receipt'):
                with self.subTest(index=index, mutation=mutation):
                    broken = copy.deepcopy(self.story)
                    scene = next(s for s in broken['Scenes'] if s['Id'] == 'kiana.trickster.epilogue.commit')
                    choice = scene['Nodes'][0]['Choices'][index]
                    if mutation == 'requires_yes':
                        choice['Requires'].append('kiana.trickster.late_yes')
                    elif mutation == 'joint_commit':
                        choice['Set'].append('kiana.committed')
                    elif mutation == 'contradiction':
                        choice['Requires'].append('kiana.committed')
                    else:
                        choice['Set'].remove('kiana.trickster.late_yes')
                    self.assertTrue(self.errors(broken))
