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
        from tests.story_fixture import fresh_story
        cls.story = fresh_story()
        cls.contract = json.loads((ROOT / 'tools/gameplay_entry_inventory_contracts.json').read_text(encoding="utf-8"))

    def test_r5_inventory_covers_all_served_findings_without_claiming_delivery(self):
        diagnostics = hub_attachment_lint.gameplay_entry_diagnostics(self.story)
        expected = {
            'aranka': range(8, 12), 'delamere': range(1, 6),
            'chadali': range(13, 19), 'devarra': range(2, 7),
            'gesmerha': range(9, 18), 'elyanka-and-camilary': [8],
            'nenio': range(11, 14), 'nurah': range(6, 12),
            'iomedae': range(1, 3), 'konomi': range(3, 6), 'seelah': [10],
        }
        self.assertEqual({f'{route}:D{n:02d}' for route, ns in expected.items() for n in ns},
                         {f for row in diagnostics for f in row['findings']})
        for row in diagnostics:
            with self.subTest(scene=row['scene']):
                if row['status'] != 'fixed':
                    self.assertTrue(row['blockers'])
                    self.assertTrue(row['requirement'])

    def test_r5_flag_only_delivery_cannot_be_certified(self):
        for row in self.contract['route_entries']:
            if not row.get('requires_world_action'):
                continue
            with self.subTest(finding=row['findings']):
                contract = copy.deepcopy(self.contract)
                candidate = next(r for r in contract['route_entries'] if r['findings'] == row['findings'])
                candidate.update(status='fixed', blockers=[])
                candidate['delivery']['completion_action'] = {'kind': 'flag', 'target': 'accepted'}
                result = next(r for r in hub_attachment_lint.gameplay_entry_diagnostics(self.story, contract)
                              if r['findings'] == row['findings'])
                self.assertTrue(result['errors'])
                self.assertIn('no supported completion-producing world action; authored flags are not proof',
                              result['deficits'])

    def test_r5_missing_action_and_empty_body_remain_explicit_debts(self):
        diagnostics = hub_attachment_lint.gameplay_entry_diagnostics(self.story)
        arrows = next(r for r in diagnostics if r['findings'] == ['delamere:D05'])
        self.assertEqual([], arrows['deficits'])
        self.assertEqual('fixed', arrows['status'])
        for row in diagnostics:
            if row['status'] == 'blocked':
                self.assertTrue(row['deficits'], row['findings'])

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
            original = program.read_text(encoding="utf-8")
            for witness in ('Rules.EnterNode(node, state)', 'Rules.ChoiceAvailable(c, state)',
                            'Rules.PaymentExitAvailable(node, state)',
                            'next.CrusadeResources[cost.Resource] = balance + cost.Amount'):
                program.write_text(original.replace(witness, 'REMOVED', 1), encoding="utf-8")
                self.assertTrue(acceptance_walker_inventory.lint(temp), witness)
            program.write_text(original, encoding="utf-8")
            for route in acceptance_walker_inventory.ROUTES:
                path = dest / (route + 'TricksterTests.cs')
                source = path.read_text(encoding="utf-8")
                path.write_text(source.replace('Program.WalkVia(scene, w, node, index)', 'Program.Walk(scene, w)'), encoding="utf-8")
                self.assertTrue(acceptance_walker_inventory.lint(temp), route)
                path.write_text(source, encoding="utf-8")
