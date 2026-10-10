"""Independent in-memory contracts and mutation probes for AST classification."""
import textwrap
import unittest
from unittest.mock import patch

from tools import test_classifier as classifier


class TestClassifierTests(unittest.TestCase):
    def classify(self, body):
        source = 'class Example:\n    def test_contract(self):\n' + textwrap.indent(textwrap.dedent(body).strip() + '\n', '        ')
        return classifier.classify_source(source)[0]

    def test_prose_literal_membership(self):
        row = self.classify('self.assertIn("She opens the door.", rendered)')
        self.assertEqual(row['classification'], 'pinned')
        self.assertEqual(row['pinned_assertions'], [{'line': 3, 'reason': classifier.PROSE}])

    def test_requires_set(self):
        row = self.classify('self.assertEqual(set(choice["Requires"]), {"trickster.now"})')
        self.assertEqual(row['classification'], 'behavioural')
        self.assertEqual(row['pinned_assertions'], [])

    def test_registry_count(self):
        row = self.classify('self.assertEqual(len(registry), 19)')
        self.assertEqual(row['classification'], 'pinned')
        self.assertEqual(row['pinned_assertions'], [{'line': 3, 'reason': classifier.COUNT}])

    def test_mixed_lists_only_pinned_lines(self):
        row = self.classify('''
            self.assertIn("She opens the door.", node["Text"])
            self.assertEqual(set(node["Requires"]), {"trickster.now"})
        ''')
        self.assertEqual(row['classification'], 'mixed')
        self.assertEqual([p['line'] for p in row['pinned_assertions']], [3])

    def test_choice_and_paragraph_position_siblings(self):
        for field in ('Choices', 'Paragraphs'):
            row = self.classify(f'self.assertEqual(node["{field}"][2]["Next"], "end")')
            self.assertEqual(row['classification'], 'mixed')
            self.assertEqual(row['pinned_assertions'][0]['reason'], classifier.POSITION)

    def test_enumerated_choice_identity_and_registry_siblings(self):
        row = self.classify('''
            for index, choice in enumerate(node["Choices"]):
                self.assertEqual(index, 0)
        ''')
        self.assertEqual(row['pinned_assertions'][0]['reason'], classifier.POSITION)
        for body in ('self.assertEqual(len(model.by_id), 19)',
                     'self.assertEqual(text.count("Hello"), 2)',
                     'self.assertIn("Hello", rendered)'):
            self.assertEqual(self.classify(body)['classification'], 'pinned', body)

    def test_source_comparison_and_alias(self):
        row = self.classify('source = path.read_text(encoding="utf-8")\nself.assertIn("def integrate", source)')
        self.assertEqual(row['classification'], 'pinned')
        self.assertIn(classifier.SOURCE, [p['reason'] for p in row['pinned_assertions']])

    def test_alias_choice_index_and_helper_return(self):
        source = '''
            def answers(node):
                return node["Choices"]
            def test_contract():
                choices = answers(node)
                chosen = choices[1]
                assert chosen["Set"] == ["earned"]
        '''
        row = classifier.classify_source(textwrap.dedent(source))[0]
        self.assertEqual(row['classification'], 'mixed')
        self.assertEqual(row['pinned_assertions'][0]['line'], 7)

    def test_diagnostics_messages_ids_and_uniqueness_are_behavioural(self):
        for body in (
            'self.assertIn("missing target", errors)',
            'self.assertEqual(result.returncode, 1, "She opens the door.")',
            'self.assertEqual(node["Id"], "the old room")',
            'ids = [s["Id"] for s in story["Scenes"]]\nself.assertEqual(len(ids), len(set(ids)))',
            'self.assertEqual(check_scene({"Text": "She opens the door."}), [])',
        ):
            self.assertEqual(self.classify(body)['classification'], 'behavioural', body)

    def test_local_bindings_do_not_leak_between_tests(self):
        rows = classifier.classify_source('''
def test_first():
    actual = node["Text"]
    assert actual == "Hello"
def test_second():
    actual = node["Requires"]
    assert actual == ["earned"]
''')
        self.assertEqual([r['classification'] for r in rows], ['pinned', 'behavioural'])

    def test_helper_local_alias_and_assertion_helper(self):
        rows = classifier.classify_source('''
class Example:
    def answers(self, node):
        result = node["Choices"]
        return result
    def assert_text(self, node):
        self.assertEqual(node["Text"], "Hello")
    def test_contract(self):
        selected = self.answers(node)[2]
        self.assertEqual(selected["Next"], "end")
        self.assert_text(node)
''')
        self.assertEqual(rows[0]['classification'], 'mixed')
        self.assertEqual({p['line'] for p in rows[0]['pinned_assertions']}, {7, 10})
        self.assertEqual(rows[0]['pinned_assertions'][0]['helper'], 'assert_text')

    def test_setup_alias_and_class_scopes(self):
        rows = classifier.classify_source('''
class First:
    def setUp(self):
        self.actual = node["Text"]
    def test_contract(self):
        self.assertEqual(self.actual, "Hello")
class Second:
    def setUp(self):
        self.actual = node["Requires"]
    def test_contract(self):
        self.assertEqual(self.actual, ["earned"])
''')
        self.assertEqual([r['classification'] for r in rows], ['pinned', 'behavioural'])

    def test_builtin_assert_and_async_discovery(self):
        row = classifier.classify_source('async def test_contract():\n    assert len(story["Scenes"]) == 9\n')[0]
        self.assertEqual(row['classification'], 'pinned')
        self.assertIsNone(row['class'])

    def test_mutation_probe_kills_missing_registry_rule(self):
        # Disable precisely the registry recognition rule, then run the unchanged
        # public-seam contract. Its assertion must fail (not merely raise a crash).
        with patch.object(classifier, 'COLLECTIONS', classifier.COLLECTIONS - {'registry'}):
            original = classifier.Analyzer.tags
            def broken_tags(analyzer, node, seen=frozenset()):
                return original(analyzer, node, seen) - {'hint:registry'}
            with patch.object(classifier.Analyzer, 'tags', broken_tags):
                result = unittest.TestResult()
                TestClassifierTests('test_registry_count').run(result)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(len(result.failures), 1)
        self.assertEqual(result.errors, [])
        self.assertIn("'behavioural' != 'pinned'", result.failures[0][1])


if __name__ == '__main__':
    unittest.main()
