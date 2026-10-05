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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--base', help='include committed changes since this git ref')
    parser.add_argument('--files', nargs='+', help='explicit changed-file list; replaces git detection')
    parser.add_argument('--plan', action='store_true', help='print selection without running commands')
    parser.add_argument('--game', default=os.environ.get('RRT_GAME_DIR', '/wrath'))
    args = parser.parse_args()
    plan = select(args.files if args.files is not None else changed_files(args.base))
    if args.plan:
        print(json.dumps(plan, indent=2))
        return 0
    started = time.perf_counter()
    env = dict(os.environ, PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1', RRT_PYTHON=sys.executable,
               RRT_GAME_DIR=str(Path(args.game).resolve()))
    env['RRT_PARENT_BINDINGS'] = os.pathsep.join(str(ROOT / 'reference/canon-review' / (name + '.json'))
        for name in ('expansion-parent-bindings', 'nurah-parent-bindings', 'nurah-parent-runtime-cue-bindings',
                     'terendelev-parent-bindings') if (ROOT / 'reference/canon-review' / (name + '.json')).is_file())
    with tempfile.TemporaryDirectory(prefix='rrt-gate-') as scratch:
        scratch = Path(scratch)
        env['RRT_TEST_BUILD_ROOT'] = str(scratch / 'rules-build')
        env['RRT_TEST_TIMINGS'] = str(scratch / 'rules-times.json')
        env['RRT_NATIVE_COVERAGE_OUTPUT'] = str(scratch / 'native-coverage.json')
        def run(label, command):
            begin = time.perf_counter()
            log = scratch / (label + '.log')
            print('RUN ' + label, flush=True)
            with log.open('w') as out:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=out, stderr=subprocess.STDOUT)
            elapsed = time.perf_counter() - begin
            if result.returncode:
                print(log.read_text(errors='replace'), file=sys.stderr)
                raise subprocess.CalledProcessError(result.returncode, command)
            print(f'PASS {label}: {elapsed:.2f}s', flush=True)
        run('expansion', [sys.executable, 'expansion.py'])
        # Reuse exactly the data generated in this gate. No authoring test may
        # mutate it, and differential generator tests still build their variants.
        shutil.copyfile(ROOT / 'development/Story.json', scratch / 'Story.json')
        env['RRT_TEST_STORY'] = str(scratch / 'Story.json')
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
            run('verify', verifier)
            # The verifier already executes earned_presence_lint.check and fails
            # on its hard findings. Re-running that same traversal adds no guard.
            for label, command in lints:
                run(label, [sys.executable, *command])
        # These processes read the same immutable export and use disjoint logs.
        # Python tests have private fixtures; no harness or game is started.
        with ThreadPoolExecutor(max_workers=2) as pool:
            checks = pool.submit(static_checks)
            python = pool.submit(run, 'python',
                [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-q']
                if args.full else [sys.executable, '-m', 'unittest', '-q', *plan['python']])
            checks.result(); python.result()
        command = ['dotnet', 'run', '--project', 'tests/RulesTests.csproj', '-c', 'Release', '--',
                   'development/Story.json']
        if not args.full:
            command += ['--suites=' + ','.join(plan['suites']), '--jobs=2']
            # Keep story last for the retained legacy command-line modes.
            command.remove('development/Story.json'); command.append('development/Story.json')
        run('rules', command)
        if args.full:
            run('bindings', [sys.executable, 'tools/verify-game-bindings.py', 'development/Story.json',
                             '--game', args.game, '--parent-bindings', env['RRT_PARENT_BINDINGS']])
            run('managed', ['bash', 'tools/managed_tests_linux.sh', args.game, 'development/Story.json'])
    print(f'PASS {"FULL" if args.full else "FAST"}: {time.perf_counter() - started:.2f}s')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
