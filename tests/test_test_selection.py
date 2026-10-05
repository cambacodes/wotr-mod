"""Gate selection must include guards, route consumers and shared systems."""
import unittest
from tools.test_selection import select, catalog


class SelectionTests(unittest.TestCase):
    def test_engine_and_unknown_changes_run_native_and_live_regressions(self):
        for path in ('src/Story.cs', 'tools/new_contract.json', 'unrecognized/file.py'):
            plan = select([path])
            self.assertTrue(plan['shared'])
            self.assertLessEqual({'NativeContradictionInventoryTests', 'PresenceRuntimeF9Tests',
                                  'TerendelevNativeDependencyTests', 'Inventory2WalkerMutationTests'},
                                 set(plan['suites']))
            self.assertIn('tests.test_crossroute_lint', plan['python'])

    def test_route_edit_includes_shared_fixtures_and_all_named_consumers(self):
        plan = select(['storylines/wenduag_echo.py'])
        self.assertFalse(plan['shared'])
        self.assertIn('WenduagTricksterTests', plan['suites'])
        self.assertIn('WenduagEchoRulesTests', plan['suites'])
        self.assertIn('ContactDisambiguationTests', plan['suites'])
        self.assertIn('tests.test_wenduag_echo', plan['python'])
        self.assertNotIn('NocticulaAcquiredHarborTests', plan['suites'])

    def test_coupled_routes_and_shared_story_edits(self):
        plan = select(['storylines/anevia.py'])
        self.assertEqual(set(plan['routes']), {'anevia', 'irabeth', 'tirabade'})
        self.assertIn('TirabadeCombinedHistoryTests', plan['suites'])
        for name in ('household', 'lastcall', 'trickster_world', 'scene_kinds'):
            self.assertTrue(select(['storylines/' + name + '.py'])['shared'])

    def test_mixed_engine_and_route_changes_keep_route_consumers(self):
        plan = select(['src/Story.cs', 'storylines/eritrice_trickster.py'])
        self.assertTrue(plan['shared'])
        self.assertIn('EritriceTricksterTests', plan['suites'])
        self.assertIn('PresenceRuntimeF9Tests', plan['suites'])

    def test_empty_tree_and_new_suite_do_not_create_an_empty_gate(self):
        plan = select([])
        self.assertTrue(plan['shared'])
        self.assertTrue(plan['suites'])
        self.assertEqual([], catalog()['ContactDisambiguationTests'])


if __name__ == '__main__':
    unittest.main()
