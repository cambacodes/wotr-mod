"""FAST/FULL gates. Outputs, logs and build intermediates live in system temp."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

from test_selection import ROOT, changed_files, select


def stage_environment(env, label, scratch):
    # Bindings invokes RulesTests too, but its receipts describe a different
    # mode. Never overwrite the completed campaign's measurements or coverage.
    if label != 'bindings':
        return env
    private = dict(env)
    private['RRT_TEST_TIMINGS'] = str(scratch / 'bindings-times.json')
    private['RRT_NATIVE_COVERAGE_OUTPUT'] = str(scratch / 'bindings-coverage.json')
    return private


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--base', help='include committed changes since this git ref')
    parser.add_argument('--files', nargs='+', help='explicit changed-file list; replaces git detection')
    parser.add_argument('--plan', action='store_true', help='print selection without running commands')
    parser.add_argument('--game', default=os.environ.get('RRT_GAME_DIR', '/wrath'))
    parser.add_argument('--json', type=Path, help='retain timing and pass receipts outside the repository')
    args = parser.parse_args()
    if args.json and args.json.resolve().is_relative_to(ROOT):
        parser.error('--json must point outside the repository')
    args.game = str(Path(args.game).expanduser().resolve())
    plan = select(args.files if args.files is not None else changed_files(args.base))
    if args.plan:
        print(json.dumps(plan, indent=2))
        return 0
    started = time.perf_counter()
    stages = []
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
        def run(label, command):
            begin = time.perf_counter()
            log = scratch / (label + '.log')
            print('RUN ' + label, flush=True)
            with log.open('w') as out:
                result = subprocess.run(command, cwd=ROOT, env=stage_environment(env, label, scratch),
                                        stdout=out, stderr=subprocess.STDOUT)
            elapsed = time.perf_counter() - begin
            stages.append(dict(stage=label, seconds=elapsed, exit=result.returncode,
                               receipt=log.read_text(errors='replace', encoding="utf-8").splitlines()[-4:]))
            if result.returncode:
                print(log.read_text(errors='replace', encoding="utf-8"), file=sys.stderr)
                raise subprocess.CalledProcessError(result.returncode, command)
            print(f'PASS {label}: {elapsed:.2f}s', flush=True)
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
        env['RRT_TEST_STORY'] = str(scratch / 'Story.json')
        env['RRT_GATE_DRAFT_INVENTORY'] = str(draft_fixture)
        # Preserve advisory baselines: these CLIs enforce their existing hard
        # policies only. Do not turn known writing debt into a new gate.
        lints = [('crossroute', ['tools/crossroute_lint.py', '--story', 'development/Story.json']),
                 ('pacing', ['tools/pacing_lint.py', '--story', 'development/Story.json', '--availability', 'tools/pacing-availability.json']),
                 ('schedule', ['tools/harem_schedule_lint.py', '--story', 'development/Story.json']),
                 ('smoothing', ['tools/harem_smoothing_lint.py', '--story', 'development/Story.json', '--strict-forms'])]
        def static_checks():
            verifier = [sys.executable, 'tools/rrt_verify.py', '--strict', '--quiet', '--game', args.game,
                        '--json', str(scratch / 'verify.json'), '--text', str(scratch / 'verify.txt')]
            if not args.full:
                verifier += ['--gate-only']
            # The verifier already executes earned_presence_lint.check and fails
            # on its hard findings. Re-running that same traversal adds no guard.
            # All commands read the frozen export; their reports and logs are
            # private. Do not serialize the two expensive independent scans.
            with ThreadPoolExecutor(max_workers=2) as static_pool:
                futures = [static_pool.submit(run, 'verify', verifier)]
                futures.extend(static_pool.submit(run, label, [sys.executable, *command])
                               for label, command in lints)
                for future in futures:
                    future.result()
        # These processes read the same immutable export and use disjoint logs.
        # Python tests have private fixtures; no harness or game is started.
        command = ['dotnet', 'run', '--project', 'tests/RulesTests.csproj', '-c', 'Release', '--',
                   'development/Story.json']
        if not args.full:
            command.insert(command.index('--'), '--no-build')
            command += ['--suites=' + ','.join(plan['suites']), '--jobs=2']
            command.remove('development/Story.json'); command.append('development/Story.json')
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
            run('bindings', [sys.executable, 'tools/verify-game-bindings.py', 'development/Story.json',
                             '--runner', str(scratch / 'rules-build/bin/Release/net8.0/RulesTests.dll'),
                             '--output', str(scratch / 'bindings.json'),
                             '--game', args.game, '--parent-bindings', env['RRT_PARENT_BINDINGS']])
            run('narrator', ['dotnet', 'build', 'narrator/Narrator.csproj', '-c', 'Release', '--nologo', '-v', 'quiet',
                            '-p:BaseIntermediateOutputPath=' + str(scratch / 'narrator-obj') + '/',
                            '-p:OutputPath=' + str(scratch / 'narrator-bin') + '/'])
            run('managed', ['bash', 'tools/managed_tests_linux.sh', args.game, 'development/Story.json'])
        elapsed = time.perf_counter() - started
        if args.json:
            args.json.write_text(json.dumps(dict(mode='FULL' if args.full else 'FAST', seconds=elapsed,
                selection=plan, stages=stages, rules=json.loads((scratch / 'rules-times.json').read_text(encoding="utf-8")),
                python=json.loads((scratch / 'python-times.json').read_text(encoding="utf-8")) if not args.full else None), indent=2) + '\n', encoding="utf-8")
    print(f'PASS {"FULL" if args.full else "FAST"}: {elapsed:.2f}s')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
