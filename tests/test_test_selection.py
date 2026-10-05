"""Gate selection must include guards, route consumers and shared systems."""
import unittest
from tools.test_selection import select, catalog


class SelectionTests(unittest.TestCase):
    def test_bindings_cannot_overwrite_completed_rules_receipts(self):
        import json, os, subprocess, sys, tempfile
        from pathlib import Path
        from unittest.mock import patch
        from tools.test_selection import ROOT
        with patch.object(sys, 'path', [str(ROOT / 'tools'), *sys.path]):
            from test_gate import stage_environment
        with tempfile.TemporaryDirectory(prefix='rrt-stage-receipts-') as directory:
            scratch = Path(directory)
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
            build = Path(env.get('RRT_TEST_BUILD_ROOT', str(scratch / 'build')))
            runner = build / 'bin/Release/net8.0/RulesTests.dll'
            if not runner.is_file():
                env['RRT_TEST_BUILD_ROOT'] = str(scratch / 'build')
                subprocess.run(['dotnet', 'build', 'tests/RulesTests.csproj', '-c', 'Release',
                                '--nologo', '-v', 'quiet'], cwd=ROOT, env=env, check=True,
                               capture_output=True, text=True)
                runner = scratch / 'build/bin/Release/net8.0/RulesTests.dll'
            story = env.get('RRT_TEST_STORY', str(ROOT / 'development/Story.json'))
            timings = scratch / 'rules-times.json'
            env['RRT_TEST_TIMINGS'] = str(timings)
            env['RRT_NATIVE_COVERAGE_OUTPUT'] = str(scratch / 'native-coverage.json')
            subprocess.run(['dotnet', str(runner), '--suites=WorldBuildCacheTests,ReachabilityCacheTests',
                            story], cwd=ROOT, env=env, check=True, capture_output=True, text=True)
            completed = timings.read_bytes()
            self.assertTrue(json.loads(completed), 'The completed rules run emitted no measurements')
            bindings = subprocess.run(['dotnet', str(runner), '--bindings', story], cwd=ROOT,
                env=stage_environment(env, 'bindings', scratch), check=True, capture_output=True, text=True)
            self.assertIsInstance(json.loads(bindings.stdout), list)
            self.assertEqual(timings.read_bytes(), completed)
            self.assertTrue((scratch / 'bindings-times.json').is_file())

    def test_changed_tests_and_lints_select_their_own_regressions(self):
        for file in ('tests/test_intimacy_contract_lint.py', 'tools/intimacy_contract_lint.py'):
            self.assertIn('tests.test_intimacy_contract_lint', select([file])['python'])
        self.assertIn('ArsinoeCampaignTests', select(['tests/ArsinoeCampaignTests.cs'])['suites'])
        self.assertIn('tests.test_ideal_run_regression', select(['tests/test_ideal_run_regression.py'])['python'])
        for file in ('tools/harem_smoothing_lint.py', 'tools/harem-smoothing.json'):
            self.assertIn('tests.test_harem_smoothing', select([file])['python'])

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

    def test_shared_fixture_examples_do_not_select_unrelated_campaigns(self):
        plan = select(['tests/test_test_selection.py', 'tests/WorldBuildCacheTests.cs'])
        self.assertEqual([], plan['routes'])
        self.assertNotIn('KaylessaTricksterTests', plan['suites'])
        self.assertIn('WorldBuildCacheTests', plan['suites'])

    def test_generator_serialization_witness_runs_when_its_source_changes(self):
        from unittest.mock import patch
        from tools import test_selection as selection
        plan = select(['tests/test_foresight_echo.py'])
        self.assertTrue(any('ForesightCanonTests' in name for name in plan['python']))
        self.assertFalse(any('late_consumer_registration' in name for name in plan['python']))
        for file in ('expansion.py', 'story.py', 'storylines/foresight.py'):
            self.assertIn('tests.test_foresight_echo', select([file])['python'])
        with patch.object(selection.subprocess, 'check_output',
                          return_value=b'def test_late_consumer_registration_is_serialized(): pass'):
            self.assertIn('tests.test_foresight_echo', select([])['python'])


if __name__ == '__main__':
    unittest.main()
