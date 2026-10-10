"""Overlay consolidation regressions through the export comparison CLI."""
import ast
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.export_equivalence import differences


ROOT = Path(__file__).resolve().parents[1]


class ExportEquivalenceTests(unittest.TestCase):
    def setUp(self):
        self.fixture = {'Scenes': [{'Id': 'scene', 'Nodes': [
            {'Id': 'start', 'Text': 'α\nβ', 'Paragraphs': [
                {'Text': 'γ', 'Requires': ['earned']}], 'Choices': [
                    {'Text': 'δ', 'Next': 'end', 'Set': ['paid']},
                    {'Text': 'ε', 'Next': None}]}]}],
            'Books': {'ledger': {'Text': 'ζ'}}}

    def compare(self, before, after):
        with tempfile.TemporaryDirectory(prefix='modc-c3-') as temporary:
            paths = [Path(temporary) / name for name in ('before.json', 'after.json')]
            for path, payload in zip(paths, (before, after)):
                path.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
            return subprocess.run([sys.executable, str(ROOT / 'tools/export_equivalence.py'),
                                   *map(str, paths)], capture_output=True, text=True, encoding='utf-8')

    def test_equal_exports(self):
        result = self.compare(self.fixture, copy.deepcopy(self.fixture))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('0 differences', result.stdout)

    def test_reports_all_mutated_fields(self):
        changed = copy.deepcopy(self.fixture)
        node = changed['Scenes'][0]['Nodes'][0]
        node['Text'] += '\n'
        node['Paragraphs'][0]['Text'] += '!'
        node['Choices'][0]['Set'].append('extra')
        changed['Books']['ledger']['Text'] += '!'
        result = self.compare(self.fixture, changed)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for address in ('["Text"]', '["Paragraphs"][0]["Text"]',
                        '["Choices"][0]["Set"][1]', '["Books"]["ledger"]["Text"]'):
            self.assertIn(address, result.stdout)
        self.assertIn('4 differences', result.stdout)

    def test_order_types_and_missing_fields(self):
        changed = copy.deepcopy(self.fixture)
        changed['Scenes'][0]['Nodes'][0]['Choices'].reverse()
        self.assertTrue(list(differences(self.fixture, changed)))
        self.assertTrue(list(differences({'value': True}, {'value': 1})))
        self.assertEqual(len(list(differences({'a': 1}, {'b': 2}))), 2)

    def test_invalid_export_is_failure(self):
        with tempfile.TemporaryDirectory(prefix='modc-c3-') as temporary:
            path = Path(temporary) / 'invalid.json'
            path.write_text('{"Text":"a","Text":"b"}', encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'tools/export_equivalence.py'),
                                     str(path), str(path)], capture_output=True,
                                    text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 2)


class RetiredOverlayTests(unittest.TestCase):
    def test_retired_overlays_are_absent_from_build_imports(self):
        retired = {'arueshalae_heat', 'camellia_heat', 'chadali_heat'}
        paths = [ROOT / 'expansion.py', *(ROOT / 'storylines').rglob('*.py')]
        for path in paths:
            tree = ast.parse(path.read_text(encoding='utf-8-sig'))
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    names = {alias.name.rsplit('.', 1)[-1] for alias in node.names}
                    if isinstance(node, ast.ImportFrom) and node.module:
                        names.add(node.module.rsplit('.', 1)[-1])
                    self.assertFalse(names & retired, str(path))
        for name in retired:
            self.assertFalse((ROOT / 'storylines' / (name + '.py')).exists())


if __name__ == '__main__':
    unittest.main()
