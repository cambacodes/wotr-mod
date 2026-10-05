"""eng8-q8f: mutation acceptance for the gameplay and branch inventories."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from tools import acceptance_walker_inventory, hub_attachment_lint

ROOT = Path(__file__).resolve().parents[1]


class GameplayEntryInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))
        cls.contract = json.loads((ROOT / 'tools/gameplay_entry_inventory_contracts.json').read_text())

    def test_production_entries_and_helpers(self):
        self.assertEqual([], hub_attachment_lint.gameplay_entry_lint(self.story))
        self.assertEqual([], acceptance_walker_inventory.lint())

    def test_every_entry_mutation_fails_despite_manual_readability(self):
        for row in self.contract['entries']:
            for suffix in ('', '_awning'):
                with self.subTest(scene=row['scene'] + suffix):
                    story = copy.deepcopy(self.story)
                    scene = next(s for s in story['Scenes'] if s['Id'] == row['scene'] + suffix)
                    scene.update(ContactUnit=None, InteractionHub=None, AnswerLists=[], ManualOnly=True)
                    self.assertTrue(hub_attachment_lint.gameplay_entry_lint(story))

    def test_unregistered_manual_sibling_is_not_waived(self):
        story = copy.deepcopy(self.story)
        sibling = copy.deepcopy(next(s for s in story['Scenes'] if s['Id'] == self.contract['entries'][0]['scene']))
        sibling.update(Id='terendelev.trickster.letter.unregistered', ManualOnly=True, Remote=True,
                       ContactUnit=None, InteractionHub=None, AnswerLists=[])
        story['Scenes'].append(sibling)
        self.assertTrue(hub_attachment_lint.gameplay_entry_lint(story))
        # A contact field or native-list field on a remote manual page is no entry.
        sibling['ContactUnit'] = self.contract['unit']
        sibling['AnswerLists'] = ['1ab909cc3a6194840b1475b99547c263']
        self.assertTrue(hub_attachment_lint.gameplay_entry_lint(story))

    def test_walker_shortcuts_fail(self):
        # Source inventory is a guard on adoption; executable sentinels judge behavior separately.
        with tempfile.TemporaryDirectory(prefix='eng8-q8f-walker-') as temp:
            dest = Path(temp) / 'tests'
            dest.mkdir()
            for name in ('Program', 'CamelliaTricksterTests', 'NenioTricksterTests', 'HorzalahTricksterTests'):
                (dest / (name + '.cs')).write_bytes((ROOT / 'tests' / (name + '.cs')).read_bytes())
            program = dest / 'Program.cs'
            original = program.read_text()
            for witness in ('Rules.EnterNode(node, state)', 'Rules.ChoiceAvailable(c, state)',
                            'Rules.PaymentExitAvailable(node, state)',
                            'next.CrusadeResources[cost.Resource] = balance + cost.Amount'):
                program.write_text(original.replace(witness, 'REMOVED', 1))
                self.assertTrue(acceptance_walker_inventory.lint(temp), witness)
            program.write_text(original)
            for route in acceptance_walker_inventory.ROUTES:
                path = dest / (route + 'TricksterTests.cs')
                source = path.read_text()
                path.write_text(source.replace('Program.WalkVia(scene, w, node, index)', 'Program.Walk(scene, w)'))
                self.assertTrue(acceptance_walker_inventory.lint(temp), route)
                path.write_text(source)
