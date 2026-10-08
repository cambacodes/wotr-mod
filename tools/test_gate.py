"""FAST/FULL gates. Outputs, logs and build intermediates live in system temp."""
import argparse
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import uuid
from concurrent.futures import ThreadPoolExecutor

try:
    from .test_selection import ROOT, changed_files, select
    from .gate_receipts import StageRunner, identity, lint_commands, load_baseline, validate_coverage
except ImportError:
    from test_selection import ROOT, changed_files, select
    from gate_receipts import StageRunner, identity, lint_commands, load_baseline, validate_coverage


def stage_environment(env, label, scratch):
    # Bindings invokes RulesTests too, but its receipts describe a different
    # mode. Never overwrite the completed campaign's measurements or coverage.
    if label != 'bindings':
        return env
    private = dict(env)
    private['RRT_TEST_TIMINGS'] = str(scratch / 'bindings-times.json')
    private['RRT_NATIVE_COVERAGE_OUTPUT'] = str(scratch / 'bindings-coverage.json')
    return private


def ownership_commands(commands, args, full):
    """Preserve H04 authority flags within the current receipt gate."""
    result = []
    for label, argv in commands:
        command = list(argv)
        if label == 'voice':
            command.append('--milestone' if full else '--integration')
            if args.voice_job:
                command += ['--job', str(args.voice_job.resolve())]
            if args.append_approvals:
                command += ['--append-approvals', str(args.append_approvals.resolve())]
        result.append((label, command))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--voice-job', type=Path, help='coordinator-reviewed held scaffold job record')
    parser.add_argument('--append-approvals', type=Path, help='coordinator-reviewed pending-choice append records')
    parser.add_argument('--base', help='include committed changes since this git ref')
    parser.add_argument('--files', nargs='+', help='explicit changed-file list; replaces git detection')
    parser.add_argument('--plan', action='store_true', help='print selection without running commands')
    parser.add_argument('--game', default=os.environ.get('RRT_GAME_DIR', '/wrath'))
    parser.add_argument('--json', type=Path, help='retain timing and pass receipts outside the repository')
    parser.add_argument('--timeout', type=float, default=900, help='maximum seconds per subprocess (default 900)')
    parser.add_argument('--baseline', type=Path, help='independently reproduced baseline receipt')
    parser.add_argument('--baseline-sha256', help='required immutable baseline receipt pin')
    parser.add_argument('--policy', type=Path, action='append', default=[], help='additional binding policy/rubric file to hash')
    parser.add_argument('--collect-failures', action='store_true', help='finish independent checks for a complete baseline receipt; still exits nonzero')
    args = parser.parse_args()
    if args.timeout <= 0 or not math.isfinite(args.timeout):
        parser.error('--timeout must be finite and positive')
    if bool(args.baseline) != bool(args.baseline_sha256):
        parser.error('--baseline and --baseline-sha256 must be supplied together')
    if args.json and args.json.resolve().is_relative_to(ROOT):
        parser.error('--json must point outside the repository')
    args.game = str(Path(args.game).expanduser().resolve())
    plan = select(args.files if args.files is not None else changed_files(args.base))
    if args.plan:
        commands = lint_commands(sys.executable, ROOT / 'development/Story.json', args.game, Path('<scratch>'), args.full)
        commands = ownership_commands(commands, args, args.full)
        plan['coverage'] = validate_coverage(commands)
        plan['coverage']['python'] = {'kind': 'Python tests', 'tests': 'full discovery' if args.full else plan['python']}
        plan['coverage']['rules'] = {'kind': 'C# progression', 'suites': 'full discovery' if args.full else plan['suites']}
        plan['mode'] = 'FULL' if args.full else 'FAST'
        plan['stages'] = ['expansion', 'draft-fixture', *plan['coverage'],
                          *(['bindings', 'narrator', 'managed'] if args.full else ['rules-build'])]
        print(json.dumps(plan, indent=2))
        return 0
    if args.json is None:
        args.json = Path(tempfile.gettempdir()) / 'rrt-gate-receipts' / (uuid.uuid4().hex + '.json')
    print('Receipt: ' + str(args.json), flush=True)
    started = time.perf_counter()
    env = dict(os.environ, PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1', RRT_PYTHON=sys.executable,
               RRT_GAME_DIR=str(Path(args.game).resolve()))
    env.pop('RRT_GATE_DRAFT_INVENTORY', None)
    env['RRT_PARENT_BINDINGS'] = os.pathsep.join(str(ROOT / 'reference/canon-review' / (name + '.json'))
        for name in ('expansion-parent-bindings', 'nurah-parent-bindings', 'nurah-parent-runtime-cue-bindings',
                     'terendelev-parent-bindings') if (ROOT / 'reference/canon-review' / (name + '.json')).is_file())
    with tempfile.TemporaryDirectory(prefix='rrt-gate-') as scratch:
        scratch = Path(scratch)
        env['RRT_TEST_BUILD_ROOT'] = str(scratch / 'rules-build')
        env['RRT_TEST_TIMINGS'] = str(scratch / 'rules-times.json')
        env['RRT_NATIVE_COVERAGE_OUTPUT'] = str(scratch / 'native-coverage.json')
        if args.full:
            env.setdefault('RRT_RULES_JOBS', '2')
        env['TMPDIR'] = env['TMP'] = env['TEMP'] = str(scratch)
        mode = 'FULL' if args.full else 'FAST'
        policies = [ROOT / 'tools/gate_receipts.py', ROOT / 'tools/test_selection.py', ROOT / 'build-expansion.ps1', *args.policy]
        writer = Path(os.environ.get('RRT_WRITER_DIR', '/work/Writer'))
        policies += [writer / 'harness/HARNESS-RUBRIC.md', writer / 'TRICKSTER-RUBRIC.md']
        snapshot = identity(ROOT, ROOT / 'development/Story.json', policies)
        baseline = load_baseline(args.baseline, args.baseline_sha256, mode, snapshot['policy_hash']) if args.baseline else None
        runner = StageRunner(ROOT, scratch, env, args.timeout, snapshot, baseline)
        lints = lint_commands(sys.executable, scratch / 'Story.json', args.game, scratch, args.full)
        lints = ownership_commands(lints, args, args.full)
        coverage = validate_coverage(lints)
        coverage['python'] = {'kind': 'Python tests', 'tests': 'full discovery' if args.full else plan['python']}
        coverage['rules'] = {'kind': 'C# progression', 'suites': 'full discovery' if args.full else plan['suites']}
        coverage['verify']['includes'] = ['save compatibility', 'earned presence', 'text structure', 'draft contracts']
        expected = ['expansion', 'draft-fixture', *coverage]
        expected += ['bindings', 'narrator', 'managed'] if args.full else ['rules-build']
        # Persist evidence on both success and failure, before TemporaryDirectory cleanup.
        import contextlib
        @contextlib.contextmanager
        def receipt_scope():
            code = 0
            previous = {}
            def cancelled(signum, frame):
                runner.cancel()
                raise subprocess.CalledProcessError(128 + signum, ['gate cancelled'])
            for signum in (signal.SIGTERM, signal.SIGINT):
                previous[signum] = signal.signal(signum, cancelled)
            try:
                yield
            except subprocess.CalledProcessError as error:
                code = error.returncode
                raise
            except BaseException:
                code = 125
                raise
            finally:
                try:
                    receipt = runner.write(args.json, mode, plan, coverage, expected, time.perf_counter() - started, code)
                    if code == 0 and not receipt['passed']:
                        raise subprocess.CalledProcessError(receipt['exit'], ['gate coverage incomplete'])
                finally:
                    for signum, handler in previous.items():
                        signal.signal(signum, handler)
        def run(label, command):
            try:
                runner.run(label, command, stage_environment(env, label, scratch))
            except subprocess.CalledProcessError as error:
                if not args.collect_failures or error.returncode in {124, 125, 130, 137, 143} or label in {'expansion', 'draft-fixture', 'rules-build'}:
                    raise
        with receipt_scope():
            # Verifier and Python controls inspect the same unintegrated drafts.
            # Keep their assertions, but do not build identical scratch worlds twice.
            draft_fixture = scratch / 'drafts.json'
            draft_command = [sys.executable, '-c',
                'import json,sys; from pathlib import Path; from tools import draft_contract_lint as d; '
                'Path(sys.argv[1]).write_text(json.dumps(dict(root=str(d.ROOT.resolve()), modules=d.inventory())), encoding="utf-8")',
                str(draft_fixture)]
            with ThreadPoolExecutor(max_workers=3) as initial_pool:
                expansion = initial_pool.submit(run, 'expansion', [sys.executable, 'expansion.py'])
                drafts = initial_pool.submit(run, 'draft-fixture', draft_command)
                build = None if args.full else initial_pool.submit(run, 'rules-build',
                    ['dotnet', 'build', 'tests/RulesTests.csproj', '-c', 'Release', '--nologo', '-v', 'quiet'])
                expansion.result(); drafts.result()
                if build is not None:
                    build.result()
            # Reuse exactly this gate's generated data. Differential generator tests
            # still build their own variants; fixture consumers get private copies.
            shutil.copyfile(ROOT / 'development/Story.json', scratch / 'Story.json')
            generated = identity(ROOT, scratch / 'Story.json', policies)
            if generated['source_hash'] != snapshot['source_hash']:
                raise RuntimeError('Source changed during generation')
            snapshot.update(generated)
            # Expansion receipts name the produced export, rather than the old input.
            for stage in runner.stages:
                stage.update(generated)
            env['RRT_TEST_STORY'] = str(scratch / 'Story.json')
            env['RRT_GATE_DRAFT_INVENTORY'] = str(draft_fixture)
            # Preserve advisory baselines: these CLIs enforce their existing hard
            # policies only. Do not turn known writing debt into a new gate.
            def static_checks():
                # The verifier already executes earned_presence_lint.check and fails
                # on its hard findings. Re-running that same traversal adds no guard.
                # All commands read the frozen export; their reports and logs are
                # private. Do not serialize the two expensive independent scans.
                with ThreadPoolExecutor(max_workers=2) as static_pool:
                    futures = [static_pool.submit(run, label, command) for label, command in lints]
                    for future in futures:
                        future.result()
            # These processes read the same immutable export and use disjoint logs.
            # Python tests have private fixtures; no harness or game is started.
            command = ['dotnet', 'run', '--project', 'tests/RulesTests.csproj', '-c', 'Release', '--',
                       str(scratch / 'Story.json')]
            if not args.full:
                command.insert(command.index('--'), '--no-build')
                command += ['--suites=' + ','.join(plan['suites']), '--jobs=2']
                command.remove(str(scratch / 'Story.json')); command.append(str(scratch / 'Story.json'))
            with ThreadPoolExecutor(max_workers=3) as pool:
                checks = pool.submit(static_checks)
                python = pool.submit(run, 'python',
                    [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-q']
                    if args.full else [sys.executable, 'tools/test_audit.py', 'python', '--json',
                                      str(scratch / 'python-times.json'), '--jobs', '2', '--tests', *plan['python']])
                # FULL can overlap its long campaign walks. On this remote, adding
                # those workers to FAST's scans increases contention and wall time.
                rules = pool.submit(run, 'rules', command) if args.full else None
                checks.result(); python.result()
                if rules is not None:
                    rules.result()
            if not args.full:
                run('rules', command)
            if args.full:
                run('bindings', [sys.executable, 'tools/verify-game-bindings.py', str(scratch / 'Story.json'),
                                 '--runner', str(scratch / 'rules-build/bin/Release/net8.0/RulesTests.dll'),
                                 '--output', str(scratch / 'bindings.json'),
                                 '--game', args.game, '--parent-bindings', env['RRT_PARENT_BINDINGS']])
                run('narrator', ['dotnet', 'build', 'narrator/Narrator.csproj', '-c', 'Release', '--nologo', '-v', 'quiet',
                                '-p:BaseIntermediateOutputPath=' + str(scratch / 'narrator-obj') + '/',
                                '-p:OutputPath=' + str(scratch / 'narrator-bin') + '/'])
                run('managed', ['bash', 'tools/managed_tests_linux.sh', args.game, str(scratch / 'Story.json')])
            elapsed = time.perf_counter() - started
            if identity(ROOT, scratch / 'Story.json', policies) != snapshot:
                raise RuntimeError('Source, export or policy changed during validation')
            failed = next((stage for stage in runner.stages if stage['exit']), None)
            if failed:
                raise subprocess.CalledProcessError(failed['exit'], failed['command'])
    print(f'PASS {"FULL" if args.full else "FAST"}: {elapsed:.2f}s')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
