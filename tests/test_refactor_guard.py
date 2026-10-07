"""Falsify S0's public capture/check boundary using tiny real CLI generators.

The fixture gates are explicit stubs: these tests prove guard behavior, not that
the production route has passed its existing Python/static/progression gates.
"""
import copy
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from story_format import c, n, scene
from tools import refactor_guard as guard, savecompat


def story():
    return dict(Scenes=[scene('route.one', 'One', 'Woman', 1, 'Enter', [
        n('start', 'Woman', 'Original words', dict(c('Stay', 'end'), Id='stay'), c('Leave')),
        n('end', 'Woman', 'Goodbye', c('Leave'))]),
        scene('route.two', 'Two', 'Woman', 2, 'Enter', [n('start', 'Woman', 'Second', c('Leave'))])],
        Relationships={'route': dict(StartedFlag='begun', ClosedFlag='closed', CommittedFlag='committed')},
        Etudes={}, Derived={}, DerivedForbids={}, PendingHooks=[])


GENERATOR = '''import json
from pathlib import Path
root = Path(__file__).parent
payload = json.loads((root / "data/payload.json").read_bytes())
output = root / "development/Story.json"
newline = "\\r\\n" if output.exists() and b"\\r\\n" in output.read_bytes() else "\\n"
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8", newline=newline)
'''


class GuardIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='rrt-guard-test-')
        self.addCleanup(self.temp.cleanup)
        self.scratch = Path(self.temp.name)
        self.source = self.scratch / 'source'
        self.source.mkdir()
        for name, data in {
            'expansion.py': GENERATOR.encode(),
            'data/payload.json': json.dumps(story(), ensure_ascii=False).encode(),
            'development/Story.json': (json.dumps(story(), ensure_ascii=False, indent=2) + '\n').encode(),
            'src/Main.cs': ('Encoding.UTF8.GetBytes("%s" + name)' % guard.NAMESPACE).encode(),
            'tools/savecompat_baseline.json': guard.canonical(savecompat.inventory(story())),
            'tools/savecompat.py': savecompat.BASELINE_PATH.with_name('savecompat.py').read_bytes(),
            'tools/__init__.py': b'',
            'build-expansion.ps1': ("$env:RRT_PARENT_BINDINGS = (@(" +
                                    ''.join("'%s'\n" % p for p in guard.PARENTS) + ')').encode(),
        }.items():
            path = self.source / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        common = guard.git(guard.ROOT, 'rev-parse', '--git-common-dir')
        revision = guard.git(guard.ROOT, 'rev-parse', 'HEAD')

        def fixture_git(source, *args):
            if args == ('status', '--porcelain'):
                return ''
            if args == ('rev-parse', 'HEAD'):
                return revision
            if args == ('rev-parse', '--git-common-dir'):
                return str((guard.ROOT / common).resolve())
            if args[0] == 'ls-files':
                return '\0'.join(p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file())
            raise AssertionError(args)

        self.addCleanup(patch.stopall)
        patch('sys.stdout', new_callable=io.StringIO).start()
        patch.object(guard, 'git', side_effect=fixture_git).start()
        patch.object(guard, 'external_inputs', return_value=({'fixture-native': {'sha256': '0' * 64, 'bytes': 0}}, {})).start()
        patch.object(savecompat, 'BASELINE_PATH', self.source / 'tools/savecompat_baseline.json').start()
        self.gates = patch.object(guard, 'gates').start()
        self.gates.return_value = [dict(stage=name, command=guard.recorded_command(command, self.scratch),
            exit=0, timed_out=False, passed=True, **({'hard_failures': 0} if name == 'strict-verifier' else {}))
            for name, command in guard.gate_commands(self.scratch)]
        def fixture_gates(snapshot, scratch, game, observations):
            for result in self.gates.return_value:
                observations.append(dict(stage=result['stage'], exit=result['exit'], timed_out=result['timed_out'],
                    started='2026-10-07T00:00:00+00:00', finished='2026-10-07T00:00:01+00:00',
                    log_sha256='0' * 64))
            return self.gates.return_value
        self.gates.side_effect = fixture_gates
        self.baseline = self.scratch / 'baseline'
        self.assertEqual(0, guard.perform('capture', self.source, self.baseline, self.scratch))

    def check(self, name='result', allowed=()):
        output = self.scratch / name
        code = guard.perform('check', self.source, output, self.scratch, self.baseline, allowed)
        return code, json.loads((output / 'receipt.json').read_bytes())['evidence']

    def test_unchanged_default_and_both_newline_seeds_pass(self):
        code, evidence = self.check()
        self.assertEqual(0, code)
        self.assertTrue(evidence['accepted'])
        self.assertEqual(2, evidence['scene_count'])
        self.assertEqual([], evidence['frozen_savecompat'])
        self.assertIn('data/payload.json', evidence['generator_reads']['LF-0'])
        self.assertIn(b'\r\n', (self.baseline / 'CRLF-Story.json').read_bytes())
        self.assertNotIn(b'\r\n', (self.baseline / 'LF-Story.json').read_bytes())

    def test_public_check_identity_is_stable_across_temp_paths_and_times(self):
        for name in ('first', 'second'):
            self.assertEqual(0, self.check(name)[0])
        first = json.loads((self.scratch / 'first/receipt.json').read_bytes())
        second = json.loads((self.scratch / 'second/receipt.json').read_bytes())
        self.assertEqual(first['identity'], second['identity'])
        self.assertEqual(first['evidence'], second['evidence'])
        self.assertNotEqual(first['observations'], second['observations'])

    def test_stale_equal_count_export_rejected(self):
        export = self.source / 'development/Story.json'
        export.write_bytes(export.read_bytes().replace(b'Original words', b'Stale words'))
        code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertTrue(evidence['tracked_export_stale'])
        self.assertTrue(any('stale_tracked_export' in f for f in evidence['failures'] if isinstance(f, dict)))

    def test_tracked_newline_profile_change_and_bom_fail(self):
        export = self.source / 'development/Story.json'
        original = export.read_bytes()
        export.write_bytes(original.replace(b'\n', b'\r\n'))
        code, evidence = self.check('newline')
        self.assertEqual(1, code)
        # Both isolated seed profiles still match. The candidate changed the
        # default tracked destination seed, which must also remain frozen.
        self.assertFalse(evidence['tracked_export_stale'])
        self.assertIn('Tracked export bytes/newline seed differ from predecessor', evidence['failures'])
        export.write_bytes(b'\xef\xbb\xbf' + original)
        code, evidence = self.check('bom')
        self.assertEqual(1, code)
        self.assertTrue(evidence['tracked_export_stale'])

    def test_different_count_and_same_count_wrong_fresh_export_rejected(self):
        original = (self.source / 'expansion.py').read_text(encoding='utf-8')
        for name, mutation in (
            ('count', 'payload["Scenes"].pop()'),
            ('text', 'payload["Scenes"][0]["Nodes"][0]["Text"] = "Wrong words"'),
            ('guard', 'payload["Scenes"][0]["Requires"] = ["unearned"]'),
            ('scene-order', 'payload["Scenes"].reverse()'),
            ('node-order', 'payload["Scenes"][0]["Nodes"].reverse()'),
            ('choice-order', 'payload["Scenes"][0]["Nodes"][0]["Choices"].reverse()'),
            ('choice-id', 'payload["Scenes"][0]["Nodes"][0]["Choices"][0]["Id"] = "replacement"'),
            ('target', 'payload["Scenes"][0]["Nodes"][0]["Choices"][0]["Next"] = "missing"'),
            ('dictionary-order', 'payload = dict(reversed(list(payload.items())))'),
            ('lost-node', 'payload["Scenes"][0]["Nodes"].pop()'),
            ('native-target', 'payload["Scenes"][0]["NativeReturnCue"] = "wrong-guid"'),
            ('relationship-id', 'payload["Relationships"]["replacement"] = payload["Relationships"].pop("route")'),
        ):
            with self.subTest(name=name):
                (self.source / 'expansion.py').write_text(original.replace('output = root', mutation + '\noutput = root'), encoding='utf-8')
                # Make the tracked file genuinely fresh. The golden still must
                # reject it even when its scene count/IDs match the predecessor.
                subprocess.run([sys.executable, '-B', 'expansion.py'], cwd=self.source, check=True)
                code, evidence = self.check(name, allowed=['expansion.py'])
                self.assertEqual(1, code)
                self.assertFalse(evidence['tracked_export_stale'])
                self.assertTrue(any('export' in f for f in evidence['failures'] if isinstance(f, dict)))

    def test_new_and_changed_reference_inputs_cannot_be_authorized_as_code(self):
        path = self.source / 'reference/new.json'
        path.parent.mkdir()
        path.write_text('{}', encoding='utf-8')
        code, evidence = self.check(allowed=['reference/new.json'])
        self.assertEqual(1, code)
        self.assertIn('Unaccounted input/source change: reference/new.json', evidence['failures'])

    def test_dead_source_edit_is_rejected_despite_identical_export(self):
        path = self.source / 'storylines/unregistered.py'
        path.parent.mkdir()
        path.write_text('text = "Unregistered prose"\n', encoding='utf-8')
        code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertFalse(evidence['tracked_export_stale'])
        self.assertIn('Unaccounted input/source change: storylines/unregistered.py', evidence['failures'])

    def test_ignored_input_is_pinned_even_when_only_its_existence_is_read(self):
        path = self.source / '.env'
        path.write_text('fixture=changed\n', encoding='utf-8')
        # Simulate git ignoring .env, as the production checkout does. The
        # complete filesystem inventory must still catch the newly added input.
        old_git = guard.git
        def ignored(source, *args):
            value = old_git(source, *args)
            return '\0'.join(p for p in value.split('\0') if p != '.env') if args[0] == 'ls-files' else value
        with patch.object(guard, 'git', side_effect=ignored):
            code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertIn('Unaccounted input/source change: .env', evidence['failures'])

    def test_shared_collector_leak_rejected_with_producer_attribution(self):
        module = self.source / 'storylines/collector.py'
        module.parent.mkdir()
        module.write_text('ROWS = []\ndef collect(row):\n    ROWS.append(row)\n    return ROWS\n', encoding='utf-8')
        generator = self.source / 'expansion.py'
        generator.write_text(generator.read_text(encoding='utf-8').replace('output = root',
            'from storylines.collector import collect\n'
            'payload["Scenes"].extend(collect(payload["Scenes"][0]))\noutput = root'), encoding='utf-8')
        status, evidence = self.check(allowed=['expansion.py', 'storylines/collector.py'])
        self.assertEqual(1, status)
        self.assertIn('storylines/collector.py', evidence['generator_reads']['LF-0'])
        self.assertTrue(any(isinstance(row, dict) and row.get('export') == 'LF' and
                            '$.Scenes: count 2 -> 3' in row['difference']['path']
                            for row in evidence['failures']))

    def test_existing_reference_drift_and_deleted_input_fail(self):
        reference = self.source / 'data/payload.json'
        reference.write_bytes(reference.read_bytes() + b' ')
        status, evidence = self.check('reference', allowed=['data/payload.json'])
        self.assertEqual(1, status)
        self.assertFalse(evidence['tracked_export_stale'])
        self.assertIn('Unaccounted input/source change: data/payload.json', evidence['failures'])
        reference.unlink()
        self.assertEqual(1, self.check('deleted')[0])

    def test_parent_native_and_tool_drift_fail(self):
        with patch.object(guard, 'external_inputs', return_value=({'fixture-native': {'sha256': '1' * 64, 'bytes': 0}}, {})):
            self.assertEqual(1, self.check('native')[0])
        source = self.source / 'tools/savecompat.py'
        source.write_bytes(source.read_bytes() + b'\n# changed verifier\n')
        self.assertEqual(1, self.check('tool', allowed=['tools/savecompat.py'])[0])

    def test_runtime_drift_fails_despite_unchanged_export(self):
        original = guard.runtime_inputs
        def drift(source):
            value = original(source)
            value['python'] = 'changed-runtime'
            return value
        with patch.object(guard, 'runtime_inputs', side_effect=drift):
            code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertFalse(evidence['tracked_export_stale'])
        self.assertIn('Pinned runtime/native/parent inputs changed', evidence['failures'])

    def test_wrong_namespace_fails_with_unchanged_story(self):
        (self.source / 'src/Main.cs').write_text('Encoding.UTF8.GetBytes("Wrong/" + name)', encoding='utf-8')
        code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertIn('GuidFor namespace changed', evidence['failures'])

    def test_external_read_and_extra_write_fail_in_worker(self):
        secret = self.scratch / 'unaccounted.json'
        secret.write_text('{}', encoding='utf-8')
        original = (self.source / 'expansion.py').read_text(encoding='utf-8')
        for name, statement in (
            ('read', 'Path(%r).read_bytes()' % str(secret)),
            ('write', '(root / "unaccounted.json").write_text("{}")'),
            ('delete', '(root / "data/payload.json").unlink()'),
            ('rename', '(root / "data/payload.json").rename(root / "stolen.json")'),
            ('subprocess', 'import subprocess; subprocess.run(["true"])'),
            ('caught-read', 'try:\n    Path(%r).read_bytes()\nexcept Exception:\n    pass' % str(secret)),
            ('caught-write', 'try:\n    (root / "unaccounted.json").write_text("{}")\nexcept Exception:\n    pass'),
        ):
            with self.subTest(name=name):
                (self.source / 'expansion.py').write_text(original + statement + '\n', encoding='utf-8')
                code, evidence = self.check(name, allowed=['expansion.py'])
                self.assertEqual(1, code)
                self.assertTrue(any('Generation failed:' in f and 'unaccounted' in f
                                    for f in evidence['failures'] if isinstance(f, str)))

    def test_nondeterministic_generator_rejected(self):
        code = (self.source / 'expansion.py').read_text(encoding='utf-8').replace('output = root',
            'import os\npayload["Nonce"] = os.getpid()\noutput = root')
        (self.source / 'expansion.py').write_text(code, encoding='utf-8')
        status, evidence = self.check(allowed=['expansion.py'])
        self.assertEqual(1, status)
        self.assertTrue(any('nondeterministic' in f for f in evidence['failures'] if isinstance(f, dict)))

    def test_red_and_timeout_gates_are_debt_never_acceptance(self):
        failed = copy.deepcopy(self.gates.return_value)
        failed[0].update(exit=143, passed=False)
        failed[1].update(exit=1, hard_failures=13, passed=False)
        failed[2].update(exit=None, timed_out=True, passed=False)
        self.gates.return_value = failed
        code, evidence = self.check()
        self.assertEqual(1, code)
        self.assertTrue(evidence['structural_passed'])
        self.assertFalse(evidence['accepted'])
        self.assertEqual(failed, evidence['gate_debt'])
        capture = self.scratch / 'debt-baseline'
        self.assertEqual(1, guard.perform('capture', self.source, capture, self.scratch))
        self.assertEqual(failed, guard.load_baseline(capture)['gate_debt'])

    def test_corrupt_export_missing_receipt_and_overwrite_fail(self):
        (self.baseline / 'LF-Story.json').write_bytes(b'{}')
        with self.assertRaisesRegex(guard.GuardError, 'corrupted'):
            guard.load_baseline(self.baseline)
        with self.assertRaises(OSError):
            guard.load_baseline(self.scratch / 'missing')
        with self.assertRaisesRegex(guard.GuardError, 'overwrite'):
            guard.perform('capture', self.source, self.baseline, self.scratch)

    def test_missing_or_malformed_gate_receipts_fail_even_with_rehashed_identity(self):
        original = json.loads((self.baseline / 'receipt.json').read_bytes())
        for mutation in ('missing', 'malformed', 'missing-export', 'missing-source', 'missing-timestamp',
                         'failed-generation', 'failed-savecompat', 'changed-command', 'false-acceptance',
                         'wrong-inventory', 'missing-runtime', 'unaccounted-read', 'boolean-format',
                         'string-status', 'numeric-acceptance', 'float-count', 'null-failures',
                         'null-savecompat', 'float-length', 'missing-revision', 'bad-revision', 'capture-authorization'):
            with self.subTest(mutation=mutation):
                value = copy.deepcopy(original)
                evidence = value['evidence']
                if mutation == 'missing':
                    evidence['gates'].pop()
                elif mutation == 'malformed':
                    evidence['gates'][0]['exit'] = '0'
                elif mutation == 'missing-export':
                    evidence['exports'].pop('CRLF')
                elif mutation == 'missing-source':
                    evidence['source_files'].pop('expansion.py')
                elif mutation == 'missing-timestamp':
                    value['observations'][0].pop('started')
                elif mutation == 'failed-generation':
                    value['observations'][0]['exit'] = 1
                elif mutation == 'failed-savecompat':
                    next(row for row in value['observations'] if row['stage'] == 'frozen-savecompat')['timed_out'] = True
                elif mutation == 'changed-command':
                    evidence['gates'][0]['command'] = ['true']
                elif mutation == 'false-acceptance':
                    evidence['accepted'] = False
                elif mutation == 'wrong-inventory':
                    evidence['predecessor_inventory']['scene_order'].reverse()
                elif mutation == 'missing-runtime':
                    evidence.pop('runtime')
                elif mutation == 'unaccounted-read':
                    evidence['generator_reads']['LF-0'].append('external:unaccounted')
                elif mutation == 'boolean-format':
                    value['format'] = True
                elif mutation == 'string-status':
                    evidence['structural_passed'] = 'true'
                elif mutation == 'numeric-acceptance':
                    evidence['accepted'] = 1
                elif mutation == 'float-count':
                    evidence['scene_count'] = float(evidence['scene_count'])
                elif mutation == 'null-failures':
                    evidence['failures'] = None
                elif mutation == 'null-savecompat':
                    evidence['frozen_savecompat'] = None
                elif mutation == 'float-length':
                    evidence['exports']['LF']['bytes'] = float(evidence['exports']['LF']['bytes'])
                elif mutation == 'missing-revision':
                    evidence.pop('revision')
                elif mutation == 'bad-revision':
                    evidence['revision'] = 'not-an-immutable-revision'
                else:
                    evidence['authorized_sources'] = ['expansion.py']
                value['identity'] = guard.digest(guard.canonical(evidence))
                (self.baseline / 'receipt.json').write_bytes(guard.canonical(value))
                with self.assertRaises(guard.GuardError):
                    guard.load_baseline(self.baseline)

    def test_dirty_capture_does_not_create_a_baseline(self):
        old_git = guard.git
        def dirty(source, *args):
            return ' M expansion.py' if args == ('status', '--porcelain') else old_git(source, *args)
        output = self.scratch / 'dirty'
        with patch.object(guard, 'git', side_effect=dirty):
            with self.assertRaisesRegex(guard.GuardError, 'clean predecessor'):
                guard.perform('capture', self.source, output, self.scratch)
        self.assertFalse(output.exists())


class GuardPrimitiveTests(unittest.TestCase):
    def test_byte_order_line_endings_and_bom_are_failures(self):
        for before, after in ((b'{"a":1,"b":2}\n', b'{"b":2,"a":1}\n'),
                              (b'{}\n', b'{}\r\n'), (b'{}\n', b'\xef\xbb\xbf{}\n')):
            with self.subTest(after=after):
                self.assertIsNotNone(guard.byte_difference(before, after))

    def test_receipt_identity_is_deterministic_without_wall_clock_or_temp_path(self):
        evidence = dict(source_digest='source', exports={'LF': {'sha256': 'story'}}, failures=[])
        first = guard.receipt(evidence, [{'started': 'yesterday', 'log_sha256': 'one'}])
        second = guard.receipt(copy.deepcopy(evidence), [{'started': 'today', 'log_sha256': 'two'}])
        self.assertEqual(first['identity'], second['identity'])
        self.assertEqual(guard.canonical(first['evidence']), guard.canonical(second['evidence']))

    def test_identity_edge_cases_use_existing_savecompat_rules(self):
        data = story()
        s = data['Scenes'][0]
        s['ReturnToList'] = True
        s['AnswerLists'] = ['host.a', 'host.b']
        inventory = guard.predecessor_inventory(data)
        self.assertEqual(['answer.route.one.host.a.start.0', 'answer.route.one.host.b.start.0'],
                         inventory['nodes'][0]['choices'][0]['identities'][0]['GuidFor'])
        s['ContinueBefore'] = {'Cue': 'native'}
        self.assertEqual([], guard.predecessor_inventory(data)['nodes'][0]['choices'][0]['identities'][0]['GuidFor'])
        s.pop('ContinueBefore')
        s['ReturnToList'] = False
        s['Owner'] = 'Epilogue'
        s['Nodes'][0]['Choices'] = [c('Continue')]
        self.assertEqual('answer.route.one.start.continue',
                         guard.predecessor_inventory(data)['nodes'][0]['choices'][0]['identities'][0]['GuidFor'])

    def test_environment_discards_inherited_fixture_and_generator_controls(self):
        with patch.dict(os.environ, {'RRT_TEST_STORY': '/wrong', 'RRT_STORY_OUTPUT': '/wrong',
                                    'PYTHONPATH': '/wrong', 'PYTHONHASHSEED': '123', 'CUSTOM_INPUT': 'wrong'}):
            env = guard.clean_environment(guard.ROOT, Path(tempfile.gettempdir()), Path('/game'))
        self.assertNotIn('RRT_TEST_STORY', env)
        self.assertNotIn('RRT_STORY_OUTPUT', env)
        self.assertNotIn('PYTHONPATH', env)
        self.assertNotIn('CUSTOM_INPUT', env)
        self.assertEqual('0', env['PYTHONHASHSEED'])

    @unittest.skipUnless(sys.platform == 'linux', 'Linux process-tree witness')
    def test_timeout_kills_child_and_returns_failure_observation(self):
        with tempfile.TemporaryDirectory(prefix='rrt-guard-child-') as temporary:
            scratch = Path(temporary)
            marker = scratch / 'child.txt'
            script = ('import subprocess,sys,time; subprocess.Popen([sys.executable,"-c",'
                      '"import time,pathlib; time.sleep(1); pathlib.Path(%r).write_text(\\\"leaked\\\")"]); '
                      'time.sleep(20)' % str(marker))
            result = guard.execute([sys.executable, '-c', script], scratch, dict(os.environ),
                                   scratch / 'log', timeout=0.2)
            self.assertTrue(result['timed_out'])
            self.assertIsNone(result['exit'])
            # Waiting via a process also bounds the witness's own execution.
            subprocess.run([sys.executable, '-c', 'import time; time.sleep(1.2)'], check=True, timeout=3)
            self.assertFalse(marker.exists())

    @unittest.skipUnless(sys.platform == 'linux', 'Linux detached-child witness')
    def test_detached_child_cleaned_after_success_and_failure(self):
        with tempfile.TemporaryDirectory(prefix='rrt-guard-detached-') as temporary:
            scratch = Path(temporary)
            for exit_code in (0, 1):
                marker = scratch / ('child-%d.txt' % exit_code)
                child = 'import time,pathlib; time.sleep(1); pathlib.Path(%r).write_text("leaked")' % str(marker)
                parent = ('import subprocess,sys; subprocess.Popen([sys.executable,"-c",%r],'
                          'start_new_session=True); sys.exit(%d)' % (child, exit_code))
                result = guard.execute([sys.executable, '-c', parent], scratch, dict(os.environ), scratch / 'log', timeout=3)
                self.assertEqual(125 if exit_code == 0 else exit_code, result['exit'])
                self.assertFalse(result['timed_out'])
                subprocess.run([sys.executable, '-c', 'import time; time.sleep(1.2)'], check=True, timeout=3)
                self.assertFalse(marker.exists())

    @unittest.skipUnless(sys.platform == 'linux', 'symlink input witness')
    def test_ignored_symlink_directory_is_not_an_unpinned_input(self):
        with tempfile.TemporaryDirectory(prefix='rrt-guard-symlink-') as temporary:
            source = Path(temporary) / 'source'
            source.mkdir()
            (source / 'ignored-input').symlink_to(Path(temporary), target_is_directory=True)
            with patch.object(guard, 'git', return_value=''):
                with self.assertRaisesRegex(guard.GuardError, 'symlink input directory'):
                    guard.source_files(source)

    def test_cli_dirty_capture_fails_without_writing_a_baseline(self):
        with tempfile.TemporaryDirectory(prefix='rrt-guard-cli-') as temporary:
            scratch = Path(temporary)
            source = scratch / 'source'
            source.mkdir()
            subprocess.run(['git', 'init', '-q', str(source)], check=True)
            (source / 'expansion.py').write_text('raise AssertionError("must not execute")', encoding='utf-8')
            result = subprocess.run([sys.executable, '-B', str(Path(guard.__file__)), 'capture',
                '--source', str(source), '--out', str(scratch / 'baseline')], capture_output=True, text=True)
            self.assertNotEqual(0, result.returncode)
            self.assertIn('clean predecessor', result.stderr)
            self.assertFalse((scratch / 'baseline').exists())

    def test_result_storage_never_overwrites_or_enters_the_source_tree(self):
        with tempfile.TemporaryDirectory(prefix='rrt-guard-location-') as temporary:
            source = Path(temporary) / 'source'
            source.mkdir()
            for path in (source, source / 'results', Path(tempfile.gettempdir())):
                with self.assertRaises(guard.GuardError):
                    guard.temporary_output(path, source)


if __name__ == '__main__':
    unittest.main()
