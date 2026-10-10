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
from types import SimpleNamespace
from unittest.mock import patch

from story_format import c, n, scene
from tools import refactor_guard as guard, savecompat

check_guard = guard.perform
check_baseline = guard.load_baseline
check_process = guard.execute
check_inventory = guard.predecessor_inventory


def newline_seed(path):
    with path.open('rb') as stream:
        raw = stream.read()
    if b'\r\n' in raw:
        return 'CRLF'
    return 'LF'


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
            if args == ('for-each-ref', '--format=%(refname)'):
                return 'refs/rrt/ownership-reviewed'
            if args == ('rev-parse', 'refs/rrt/ownership-reviewed'):
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
        self.assertEqual(0, check_guard('capture', self.source, self.baseline, self.scratch))

    def check(self, name='result', allowed=()):
        output = self.scratch / name
        code = check_guard('check', self.source, output, self.scratch, self.baseline, allowed)
        return code, json.loads((output / 'receipt.json').read_bytes())['evidence']

    def test_unchanged_default_and_both_newline_seeds_pass(self):
        code, diagnostics = self.check()
        self.assertEqual(0, code)
        self.assertTrue(diagnostics['accepted'])
        self.assertEqual(2, diagnostics['scene_count'])
        self.assertEqual([], diagnostics['frozen_savecompat'])
        self.assertIn('data/payload.json', diagnostics['generator_reads']['LF-0'])
        self.assertEqual(newline_seed(self.baseline / 'CRLF-Story.json'), 'CRLF')
        self.assertEqual(newline_seed(self.baseline / 'LF-Story.json'), 'LF')

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
        code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertTrue(diagnostics['tracked_export_stale'])
        self.assertTrue(any('stale_tracked_export' in f for f in diagnostics['failures'] if isinstance(f, dict)))

    def test_tracked_newline_profile_change_and_bom_fail(self):
        export = self.source / 'development/Story.json'
        original = export.read_bytes()
        export.write_bytes(original.replace(b'\n', b'\r\n'))
        code, diagnostics = self.check('newline')
        self.assertEqual(1, code)
        # Both isolated seed profiles still match. The candidate changed the
        # default tracked destination seed, which must also remain frozen.
        self.assertFalse(diagnostics['tracked_export_stale'])
        self.assertIn('Tracked export bytes/newline seed differ from predecessor', diagnostics['failures'])
        export.write_bytes(b'\xef\xbb\xbf' + original)
        code, diagnostics = self.check('bom')
        self.assertEqual(1, code)
        self.assertTrue(diagnostics['tracked_export_stale'])

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
                code, diagnostics = self.check(name, allowed=['expansion.py'])
                self.assertEqual(1, code)
                self.assertFalse(diagnostics['tracked_export_stale'])
                self.assertTrue(any('export' in f for f in diagnostics['failures'] if isinstance(f, dict)))

    def test_new_and_changed_reference_inputs_cannot_be_authorized_as_code(self):
        path = self.source / 'reference/new.json'
        path.parent.mkdir()
        path.write_text('{}', encoding='utf-8')
        code, diagnostics = self.check(allowed=['reference/new.json'])
        self.assertEqual(1, code)
        self.assertIn('Unaccounted input/source change: reference/new.json', diagnostics['failures'])

    def test_dead_source_edit_is_rejected_despite_identical_export(self):
        path = self.source / 'storylines/unregistered.py'
        path.parent.mkdir()
        path.write_text('text = "Unregistered prose"\n', encoding='utf-8')
        code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertFalse(diagnostics['tracked_export_stale'])
        self.assertIn('Unaccounted input/source change: storylines/unregistered.py', diagnostics['failures'])

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
            code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertIn('Unaccounted input/source change: .env', diagnostics['failures'])

    def test_shared_collector_leak_rejected_with_producer_attribution(self):
        module = self.source / 'storylines/collector.py'
        module.parent.mkdir()
        module.write_text('ROWS = []\ndef collect(row):\n    ROWS.append(row)\n    return ROWS\n', encoding='utf-8')
        generator = self.source / 'expansion.py'
        generator.write_text(generator.read_text(encoding='utf-8').replace('output = root',
            'from storylines.collector import collect\n'
            'payload["Scenes"].extend(collect(payload["Scenes"][0]))\noutput = root'), encoding='utf-8')
        status, diagnostics = self.check(allowed=['expansion.py', 'storylines/collector.py'])
        self.assertEqual(1, status)
        self.assertIn('storylines/collector.py', diagnostics['generator_reads']['LF-0'])
        self.assertTrue(any(isinstance(row, dict) and row.get('export') == 'LF' and
                            '$.Scenes: count 2 -> 3' in row['difference']['path']
                            for row in diagnostics['failures']))

    def test_existing_reference_drift_and_deleted_input_fail(self):
        reference = self.source / 'data/payload.json'
        reference.write_bytes(reference.read_bytes() + b' ')
        status, diagnostics = self.check('reference', allowed=['data/payload.json'])
        self.assertEqual(1, status)
        self.assertFalse(diagnostics['tracked_export_stale'])
        self.assertIn('Unaccounted input/source change: data/payload.json', diagnostics['failures'])
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
            code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertFalse(diagnostics['tracked_export_stale'])
        self.assertIn('Pinned runtime/native/parent inputs changed', diagnostics['failures'])

    def test_wrong_namespace_fails_with_unchanged_story(self):
        (self.source / 'src/Main.cs').write_text('Encoding.UTF8.GetBytes("Wrong/" + name)', encoding='utf-8')
        code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertIn('GuidFor namespace changed', diagnostics['failures'])

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
                code, diagnostics = self.check(name, allowed=['expansion.py'])
                self.assertEqual(1, code)
                self.assertTrue(any('Generation failed:' in f and 'unaccounted' in f
                                    for f in diagnostics['failures'] if isinstance(f, str)))

    def test_nondeterministic_generator_rejected(self):
        code = (self.source / 'expansion.py').read_text(encoding='utf-8').replace('output = root',
            'import os\npayload["Nonce"] = os.getpid()\noutput = root')
        (self.source / 'expansion.py').write_text(code, encoding='utf-8')
        status, diagnostics = self.check(allowed=['expansion.py'])
        self.assertEqual(1, status)
        self.assertTrue(any('nondeterministic' in f for f in diagnostics['failures'] if isinstance(f, dict)))

    def test_red_and_timeout_gates_are_debt_never_acceptance(self):
        failed = json.loads(json.dumps(self.gates.return_value))
        failed[0].update(exit=143, passed=False)
        failed[1].update(exit=1, hard_failures=13, passed=False)
        failed[2].update(exit=None, timed_out=True, passed=False)
        self.gates.return_value = failed
        code, diagnostics = self.check()
        self.assertEqual(1, code)
        self.assertTrue(diagnostics['structural_passed'])
        self.assertFalse(diagnostics['accepted'])
        self.assertEqual(failed, diagnostics['gate_debt'])
        capture = self.scratch / 'debt-baseline'
        self.assertEqual(1, check_guard('capture', self.source, capture, self.scratch))
        self.assertEqual(failed, check_baseline(capture)['gate_debt'])

    def test_corrupt_export_missing_receipt_and_overwrite_fail(self):
        (self.baseline / 'LF-Story.json').write_bytes(b'{}')
        with self.assertRaisesRegex(guard.GuardError, 'corrupted'):
            check_baseline(self.baseline)
        with self.assertRaises(OSError):
            check_baseline(self.scratch / 'missing')
        with self.assertRaisesRegex(guard.GuardError, 'overwrite'):
            check_guard('capture', self.source, self.baseline, self.scratch)

    def test_missing_or_malformed_gate_receipts_fail_even_with_rehashed_identity(self):
        original = json.loads((self.baseline / 'receipt.json').read_bytes())
        for mutation in ('missing', 'malformed', 'missing-export', 'missing-source', 'missing-timestamp',
                         'failed-generation', 'failed-savecompat', 'changed-command', 'false-acceptance',
                         'wrong-inventory', 'missing-runtime', 'unaccounted-read', 'boolean-format',
                         'string-status', 'numeric-acceptance', 'float-count', 'null-failures',
                         'null-savecompat', 'float-length', 'missing-revision', 'bad-revision', 'capture-authorization'):
            with self.subTest(mutation=mutation):
                value = copy.deepcopy(original)
                diagnostics = value['evidence']
                if mutation == 'missing':
                    diagnostics['gates'].pop()
                elif mutation == 'malformed':
                    diagnostics['gates'][0]['exit'] = '0'
                elif mutation == 'missing-export':
                    diagnostics['exports'].pop('CRLF')
                elif mutation == 'missing-source':
                    diagnostics['source_files'].pop('expansion.py')
                elif mutation == 'missing-timestamp':
                    value['observations'][0].pop('started')
                elif mutation == 'failed-generation':
                    value['observations'][0]['exit'] = 1
                elif mutation == 'failed-savecompat':
                    next(row for row in value['observations'] if row['stage'] == 'frozen-savecompat')['timed_out'] = True
                elif mutation == 'changed-command':
                    diagnostics['gates'][0]['command'] = ['true']
                elif mutation == 'false-acceptance':
                    diagnostics['accepted'] = False
                elif mutation == 'wrong-inventory':
                    diagnostics['predecessor_inventory']['scene_order'].reverse()
                elif mutation == 'missing-runtime':
                    diagnostics.pop('runtime')
                elif mutation == 'unaccounted-read':
                    diagnostics['generator_reads']['LF-0'].append('external:unaccounted')
                elif mutation == 'boolean-format':
                    value['format'] = True
                elif mutation == 'string-status':
                    diagnostics['structural_passed'] = 'true'
                elif mutation == 'numeric-acceptance':
                    diagnostics['accepted'] = 1
                elif mutation == 'float-count':
                    diagnostics['scene_count'] = float(diagnostics['scene_count'])
                elif mutation == 'null-failures':
                    diagnostics['failures'] = None
                elif mutation == 'null-savecompat':
                    diagnostics['frozen_savecompat'] = None
                elif mutation == 'float-length':
                    diagnostics['exports']['LF']['bytes'] = float(diagnostics['exports']['LF']['bytes'])
                elif mutation == 'missing-revision':
                    diagnostics.pop('revision')
                elif mutation == 'bad-revision':
                    diagnostics['revision'] = 'not-an-immutable-revision'
                else:
                    diagnostics['authorized_sources'] = ['expansion.py']
                value['identity'] = guard.digest(guard.canonical(diagnostics))
                (self.baseline / 'receipt.json').write_bytes(guard.canonical(value))
                with self.assertRaises(guard.GuardError):
                    check_baseline(self.baseline)

    def test_dirty_capture_does_not_create_a_baseline(self):
        old_git = guard.git
        def dirty(source, *args):
            return ' M expansion.py' if args == ('status', '--porcelain') else old_git(source, *args)
        output = self.scratch / 'dirty'
        with patch.object(guard, 'git', side_effect=dirty):
            with self.assertRaisesRegex(guard.GuardError, 'clean predecessor'):
                check_guard('capture', self.source, output, self.scratch)
        self.assertFalse(output.exists())


class GuardPrimitiveTests(unittest.TestCase):
    def test_byte_order_line_endings_and_bom_are_failures(self):
        for before, after in ((b'{"a":1,"b":2}\n', b'{"b":2,"a":1}\n'),
                              (b'{}\n', b'{}\r\n'), (b'{}\n', b'\xef\xbb\xbf{}\n')):
            with self.subTest(after=after):
                self.assertIsNotNone(guard.byte_difference(before, after))

    def test_receipt_identity_is_deterministic_without_wall_clock_or_temp_path(self):
        diagnostics = dict(source_digest='source', exports={'LF': {'sha256': 'story'}}, failures=[])
        first = guard.receipt(diagnostics, [{'started': 'yesterday', 'log_sha256': 'one'}])
        second = guard.receipt(copy.deepcopy(diagnostics), [{'started': 'today', 'log_sha256': 'two'}])
        self.assertEqual(first['identity'], second['identity'])
        self.assertEqual(guard.canonical(first['evidence']), guard.canonical(second['evidence']))

    def test_identity_edge_cases_use_existing_savecompat_rules(self):
        data = story()
        s = data['Scenes'][0]
        s['ReturnToList'] = True
        s['AnswerLists'] = ['host.a', 'host.b']
        inventory = check_inventory(data)
        self.assertEqual(['answer.route.one.host.a.start.0', 'answer.route.one.host.b.start.0'],
                         next(ref['GuidFor'] for event in inventory['nodes'] if event['scene'] == 'route.one'
                              for node in event['choices'] if node['node'] == 'start' for ref in node['identities']
                              if ref['GuidFor'] == ['answer.route.one.host.a.start.0', 'answer.route.one.host.b.start.0']))
        s['ContinueBefore'] = {'Cue': 'native'}
        self.assertEqual([], next(ref['GuidFor'] for event in check_inventory(data)['nodes'] if event['scene'] == 'route.one'
                              for node in event['choices'] if node['node'] == 'start' for ref in node['identities']))
        s.pop('ContinueBefore')
        s['ReturnToList'] = False
        s['Owner'] = 'Epilogue'
        s['Nodes'][0]['Choices'] = [c('Continue')]
        self.assertEqual('answer.route.one.start.continue',
                         next(ref['GuidFor'] for event in check_inventory(data)['nodes'] if event['scene'] == 'route.one'
                              for node in event['choices'] if node['node'] == 'start' for ref in node['identities']))

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
            result = check_process([sys.executable, '-c', script], scratch, dict(os.environ),
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
                result = check_process([sys.executable, '-c', parent], scratch, dict(os.environ), scratch / 'log', timeout=3)
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


class S1ProfileTests(unittest.TestCase):
    """Real tiny generators falsify the extra command-profile boundaries."""

    def setUp(self):
        GuardIntegrationTests.setUp(self)
        patch('tools.voice_authority.git', side_effect=lambda source, *args: guard.git(source, *args).encode('utf-8')).start()
        generator = self.source / 'expansion.py'
        generator.write_text(generator.read_text(encoding='utf-8') +
            '\ndef make_expansion(*, independent_tirabade=True):\n'
            '    result = json.loads((root / "data/payload.json").read_bytes())\n'
            '    result["Scenes"][0]["Nodes"][0]["Text"] = "Joint words"\n'
            '    return result\n', encoding='utf-8')
        (self.source / 'story.py').write_text(GENERATOR.replace('development/Story.json', 'package/Story.json')
            .replace('newline=newline', 'newline=None'), encoding='utf-8')
        def fixture_gates(snapshot, scratch, game, observations, gate_profile='s0'):
            results = []
            for name, command in guard.gate_commands(scratch, gate_profile):
                observations.append(dict(stage=name, exit=0, timed_out=False,
                    started='2026-10-07T00:00:00+00:00', finished='2026-10-07T00:00:01+00:00',
                    log_sha256='0' * 64))
                results.append(dict(stage=name, command=guard.recorded_command(command, scratch),
                    exit=0, timed_out=False, passed=True))
            return results
        self.gates.side_effect = fixture_gates
        self.baseline = self.scratch / 's1-baseline'
        status = check_guard('capture', self.source, self.baseline, self.scratch, gate_profile='arch-s1')
        diagnostics = json.loads((self.baseline / 'receipt.json').read_bytes())['evidence']
        self.assertEqual(0, status, diagnostics['failures'])

    def test_all_profiles_and_receipt_identity_survive_destination_seeds(self):
        for name in ('first', 'second'):
            self.assertEqual(0, check_guard('check', self.source, self.scratch / name, self.scratch,
                self.baseline, gate_profile='arch-s1'))
        first = check_baseline(self.baseline)
        self.assertEqual({'base', 'joint'}, set(first['profiles']))
        self.assertNotEqual(first['exports']['LF'], first['profiles']['joint']['exports']['LF'])
        self.assertEqual(first['profiles']['base']['exports']['LF'], first['profiles']['base']['exports']['CRLF'])
        self.assertEqual(json.loads((self.scratch / 'first/receipt.json').read_bytes())['identity'],
                         json.loads((self.scratch / 'second/receipt.json').read_bytes())['identity'])

    def test_joint_only_delta_fails_even_when_default_export_matches(self):
        generator = self.source / 'expansion.py'
        generator.write_text(generator.read_text(encoding='utf-8').replace('Joint words', 'Wrong joint words'),
                             encoding='utf-8')
        out = self.scratch / 'changed-joint'
        self.assertEqual(1, check_guard('check', self.source, out, self.scratch, self.baseline,
            allowed=['expansion.py'], gate_profile='arch-s1'))
        diagnostics = json.loads((out / 'receipt.json').read_bytes())['evidence']
        self.assertTrue(any(isinstance(row, dict) and row.get('export') == 'joint-LF'
                            for row in diagnostics['failures']))
        self.assertEqual([], [row for row in diagnostics['failures']
                             if isinstance(row, dict) and row.get('export') == 'LF'])

    def test_missing_corrupt_or_unaccounted_profile_evidence_fails(self):
        original = json.loads((self.baseline / 'receipt.json').read_bytes())
        for mutation in ('missing-profile', 'missing-seed', 'unaccounted-read', 'wrong-inventory', 'missing-observation', 'missing-ownership'):
            with self.subTest(mutation=mutation):
                value = copy.deepcopy(original)
                diagnostics = value['evidence']
                if mutation == 'missing-profile':
                    diagnostics['profiles'].pop('base')
                elif mutation == 'missing-seed':
                    diagnostics['profiles']['joint']['exports'].pop('CRLF')
                elif mutation == 'unaccounted-read':
                    diagnostics['profiles']['base']['reads']['LF-0'].append('unaccounted')
                elif mutation == 'wrong-inventory':
                    diagnostics['profiles']['joint']['predecessor_inventory']['scene_order'].reverse()
                elif mutation == 'missing-observation':
                    value['observations'] = [row for row in value['observations']
                                             if row['stage'] != 'generate-base-LF-0']
                else:
                    diagnostics['runtime'].pop('ownership_reference')
                value['identity'] = guard.digest(guard.canonical(diagnostics))
                (self.baseline / 'receipt.json').write_bytes(guard.canonical(value))
                with self.assertRaises(guard.GuardError):
                    check_baseline(self.baseline)
        (self.baseline / 'receipt.json').write_bytes(guard.canonical(original))
        (self.baseline / 'base-LF-Story.json').write_bytes(b'{}')
        with self.assertRaisesRegex(guard.GuardError, 'corrupted'):
            check_baseline(self.baseline)


class CompilerCommandTests(unittest.TestCase):
    def test_exact_serialization_and_legacy_copy_policy(self):
        from authoring.compiler import CompilationInputs, compile_story
        from authoring._serialization import write_story
        # Intentionally unsorted keys, UTF-8 and embedded CRLF in player text.
        payload = {'z': 'é\r\n', 'a': [2, 1]}
        module = SimpleNamespace(_make_story=lambda: payload,
                                 _make_expansion=lambda **kwargs: payload)
        with tempfile.TemporaryDirectory(prefix='rrt-compiler-') as temporary:
            output = Path(temporary) / 'Story.json'
            for profile, seed, newline in (
                ('expansion', None, '\n'), ('expansion', b'\n', '\n'), ('expansion', b'\r\n', '\r\n'),
                ('base', None, os.linesep), ('base', b'\n', os.linesep), ('base', b'\r\n', os.linesep)):
                with self.subTest(profile=profile, seed=seed):
                    if seed is None:
                        output.unlink(missing_ok=True)
                    else:
                        output.write_bytes(seed)
                    with patch('authoring.compiler._legacy_module', return_value=module):
                        compiled = compile_story(profile, CompilationInputs(output))
                    self.assertIs(payload, compiled.payload)
                    expected = (json.dumps(payload, ensure_ascii=False, indent=2) + '\n').replace('\n', newline).encode('utf-8')
                    self.assertEqual(expected, compiled.export_bytes)
                    write_story(output, compiled)
                    self.assertEqual(json.loads(output.read_text(encoding="utf-8")), payload)
                    self.assertEqual(newline_seed(output), "CRLF" if newline == "\r\n" else "LF")

    def test_factory_delegates_preserve_profile_argument_and_exception(self):
        import expansion
        import story as base_story
        sentinel = ValueError()
        with patch('authoring.compiler.compile_story', return_value=SimpleNamespace(payload={'sentinel': True})) as compile:
            self.assertEqual({'sentinel': True}, expansion.make_expansion(independent_tirabade=False))
            compile.assert_called_once_with('expansion', independent_tirabade=False)
            compile.reset_mock()
            self.assertEqual({'sentinel': True}, base_story.make_story())
            compile.assert_called_once_with('base')
        with patch.object(expansion, '_make_expansion', side_effect=sentinel):
            with self.assertRaises(ValueError) as caught:
                expansion.make_expansion()
            self.assertIs(sentinel, caught.exception)

    def test_destination_read_error_precedes_json_serialization_error(self):
        from authoring.compiler import CompilationInputs, compile_story
        sentinel = PermissionError()
        destination = SimpleNamespace(exists=lambda: True)
        destination.read_bytes = lambda: (_ for _ in ()).throw(sentinel)
        module = SimpleNamespace(_make_expansion=lambda **kwargs: {'unserializable': object()})
        with patch('authoring.compiler._legacy_module', return_value=module):
            with self.assertRaises(PermissionError) as caught:
                compile_story('expansion', CompilationInputs(destination))
        self.assertIs(sentinel, caught.exception)

    def test_compiler_reuses_executing_cli_module(self):
        from authoring.compiler import _legacy_module
        for name in ('story', 'expansion'):
            command = SimpleNamespace(__file__=str(guard.ROOT / (name + '.py')),
                                      **{'_make_' + name: lambda: {}})
            with patch.dict(sys.modules, {'__main__': command}), patch('importlib.import_module') as load:
                self.assertIs(command, _legacy_module(name))
                load.assert_not_called()

    def test_cli_error_message_status_and_destination(self):
        with tempfile.TemporaryDirectory(prefix='rrt-command-error-') as temporary:
            parent = Path(temporary) / 'file'
            parent.write_text('existing file', encoding='utf-8')
            before = parent.stat()
            # Freeze the old Path.mkdir failure on this host (including the
            # Windows WinError spelling), rather than hardcoding Linux errno.
            with self.assertRaises(FileExistsError) as original_error:
                parent.mkdir(exist_ok=True)
            output = parent / 'Story.json'
            env = guard.clean_environment(guard.ROOT, Path(temporary), Path('/wrath'))
            env['RRT_STORY_OUTPUT'] = str(output)
            result = subprocess.run([sys.executable, '-B', 'expansion.py'], cwd=guard.ROOT,
                                    env=env, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(1, result.returncode)
            self.assertEqual('', result.stdout)
            self.assertEqual("FileExistsError: " + str(original_error.exception),
                             result.stderr.splitlines()[-1])
            self.assertEqual(parent.stat(), before)


if __name__ == '__main__':
    unittest.main()
