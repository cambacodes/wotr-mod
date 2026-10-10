"""Inventory mutations must fail the required verifier's own-life/provenance checks."""
from tests.story_fixture import fresh_story
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import earned_presence_lint, own_life_lint, return_provenance_lint

ROOT = Path(__file__).resolve().parents[1]



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class InventoryContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = fresh_story()

    def test_clean_required_checks(self):
        self.assertEqual(own_life_lint.check(self.story), [])
        self.assertEqual(return_provenance_lint.check(self.story), [])
        self.assertEqual(earned_presence_lint.check(self.story)[0], [])

    def test_each_registered_own_consumer_mutation_fails(self):
        baseline = set(own_life_lint.check(self.story))
        for site in own_life_lint.contracts()['sites']:
            for field in ('Requires', 'Forbids'):
                for guard in site.get(field, []):
                    with self.subTest(scene=site['scene'], node=site.get('node'), paragraph=site.get('paragraph'), guard=guard):
                        story = copy.deepcopy(self.story)
                        target = own_life_lint.targets(story, site)[0]
                        target[field].remove(guard)
                        self.assertTrue(set(own_life_lint.check(story)) - baseline)
                        self.assertTrue(any(e.startswith('OL ') and e not in baseline
                                            for e in earned_presence_lint.check(story)[0]))

    def test_life_loss_and_return_reader_mutations_fail(self):
        baseline = set(own_life_lint.check(self.story))
        for spec in own_life_lint.contracts()['people'].values():
            for loss in spec['losses']:
                with self.subTest(loss=loss):
                    story = copy.deepcopy(self.story)
                    story['DerivedForbids'][spec['key']].remove(spec['key'] + '.blocked.' + loss)
                    self.assertTrue(set(own_life_lint.check(story)) - baseline)

    def test_return_overrides_and_every_completion_producer(self):
        data = return_provenance_lint.contracts()
        for sid in data['producers']:
            self.assertTrue(any(data["completed"] in c["Set"] for s in self.story["Scenes"] if s["Id"] == sid
                                for n in s["Nodes"] for c in n["Choices"]), sid)
        for loss in data['overrides']:
            story = copy.deepcopy(self.story)
            story['Relationships']['camellia']['UnavailableOverrides'][loss] = data['generic']
            self.assertTrue(return_provenance_lint.check(story))
        for sid in data['producers']:
            choices = [(n['Id'], i) for s in self.story['Scenes'] if s['Id'] == sid for n in s['Nodes']
                       for i, c in enumerate(n['Choices']) if data['completed'] in c['Set']]
            self.assertTrue(any(data["completed"] in c["Set"] for s in self.story["Scenes"] if s["Id"] == sid
                                for n in s["Nodes"] for c in n["Choices"]))
            for node, i in choices:
                story = copy.deepcopy(self.story)
                scene = next(s for s in story['Scenes'] if s['Id'] == sid)
                saved_answer(next(n for n in scene['Nodes'] if n['Id'] == node)['Choices'], i)['Set'].remove(data['completed'])
                self.assertTrue(return_provenance_lint.check(story))
        story = copy.deepcopy(self.story)
        story['Derived'][data['completed']] = [[data['generic']]]
        self.assertTrue(return_provenance_lint.check(story))
        for sid in data['producers']:
            for flag in data['producer_inputs']:
                story = copy.deepcopy(self.story)
                next(s for s in story['Scenes'] if s['Id'] == sid)['Requires'].remove(flag)
                self.assertTrue(return_provenance_lint.check(story))

    def test_veiled_cards_and_complementary_dispatch_mutations(self):
        data = return_provenance_lint.contracts()
        for sid in data['veiled_scenes']:
            story = copy.deepcopy(self.story)
            next(s for s in story['Scenes'] if s['Id'] == sid)['Requires'].remove(data['available'])
            self.assertTrue(return_provenance_lint.check(story))
        for sid in data['dispatch_scenes']:
            scene = next(s for s in self.story['Scenes'] if s['Id'] == sid)
            for node in scene['Nodes']:
                for i, choice in enumerate(node['Choices']):
                    for field in ('Requires', 'Forbids'):
                        if data['available'] not in choice[field]:
                            continue
                        story = copy.deepcopy(self.story)
                        changed = next(s for s in story['Scenes'] if s['Id'] == sid)
                        target = saved_answer(next(n for n in changed['Nodes'] if n['Id'] == node['Id'])['Choices'], i)
                        target[field] = [data['generic'] if k == data['available'] else k for k in target[field]]
                        self.assertTrue(return_provenance_lint.check(story))

    def test_current_acts_consume_t7_and_keep_independent_or_gate(self):
        data = json.loads((ROOT / 'tools/current_act_inventory_contracts.json').read_text(encoding="utf-8"))
        for sid in data['new_acts']:
            scene = next(s for s in self.story['Scenes'] if s['Id'] == sid)
            self.assertTrue(earned_presence_lint.live_context(self.story, scene), sid)
        scene = next(s for s in self.story['Scenes'] if s['Id'] == 'wenduag.trickster.street.fall')
        mutated = copy.deepcopy(self.story)
        target = next(s for s in mutated['Scenes'] if s['Id'] == scene['Id'])
        target['Requires'].remove('trickster.now')
        self.assertTrue(any(e.startswith('T7 ' + scene['Id']) for e in earned_presence_lint.check(mutated)[0]))
        self.assertIn('wenduag.trickster.fall_agreed', scene['RequiresAnyGroups'][0])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        data = return_provenance_lint.contracts()
        scene = next(s for s in self.story['Scenes'] if s['Id'] == data['producers'][0])
        from contextlib import ExitStack
        with ExitStack() as changes:
            for node in scene['Nodes']:
                for choice in node['Choices']:
                    if data['completed'] in choice['Set']:
                        changes.enter_context(patch.dict(choice, Set=[f for f in choice['Set'] if f != data['completed']]))
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_return_overrides_and_every_completion_producer()


if __name__ == '__main__':
    unittest.main()
