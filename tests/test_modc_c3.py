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
            {'Id': 'start', 'Text': '''α
β''', 'Paragraphs': [
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
        node['Text'] += '''
'''
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
        retired = {'arueshalae_heat', 'camellia_heat', 'chadali_heat',
                   'nocticula_heat', 'heat_g4', 'heat_cal_b',
                   'heat_cal_g', 'zzz_shamira_pairs', 'zzz_vellexia_pairs',
                   'zzz_nocticula_pairs'}
        paths = [ROOT / 'expansion.py', *(ROOT / 'storylines').rglob('*.py')]
        for path in paths:
            tree = ast.parse(path.read_text(encoding='utf-8-sig'))
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    names = {alias.name.rsplit('.', 1)[-1] for alias in node.names}
                    if isinstance(node, ast.ImportFrom) and node.module:
                        names.add(node.module.rsplit('.', 1)[-1])
                    self.assertFalse(names & retired, str(path))
        for name in ('herrax_cloud', 'nurah_cloud', 'arueshalae_cloud'):
            path = ROOT / 'storylines' / (name + '.py')
            tree = ast.parse(path.read_text(encoding='utf-8'))
            replacing_calls = [node for node in ast.walk(tree)
                               if isinstance(node, ast.Call)
                               and isinstance(node.func, ast.Attribute)
                               and node.func.attr in {'replace', 'sub', 'subn'}]
            self.assertFalse(replacing_calls, str(path))
        for name in retired:
            self.assertFalse(list((ROOT / 'storylines').rglob(name + '.py')))



if __name__ == '__main__':
    unittest.main()
