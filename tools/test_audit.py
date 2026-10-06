"""Measure tests/lints without writing artifacts in the worktree.

Usage: python tools/test_audit.py python --json /tmp/python-times.json
       python tools/test_audit.py lints --json /tmp/lint-times.json
RulesTests emits per-suite measurements when RRT_TEST_TIMINGS points into /tmp.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]

# Relative module costs from the audit receipts. These affect scheduling only;
# unknown/new modules still run, and all selected methods retain their assertions.
PYTHON_COSTS = {'test_delivery_inventory2': 20, 'test_foresight_echo': 65,
                'test_presence_dependency_lint': 35, 'test_return_safety': 35,
                'test_native_world_reconciliation': 25, 'test_player_text_lint': 20}


class TimedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = []
        self.fixtures = []
        self.outcomes = {}

    def addSuccess(self, test):
        self.outcomes[test.id()] = 'passed'
        super().addSuccess(test)

    def addSkip(self, test, reason):
        self.outcomes[test.id()] = 'skipped: ' + reason
        super().addSkip(test, reason)

    def addFailure(self, test, error):
        self.outcomes[test.id()] = 'failed'
        super().addFailure(test, error)

    def addError(self, test, error):
        self.outcomes[test.id()] = 'error'
        super().addError(test, error)

    def startTest(self, test):
        self.started = time.perf_counter()
        super().startTest(test)

    def stopTest(self, test):
        self.rows.append(dict(test=test.id(), seconds=time.perf_counter() - self.started,
                             status=self.outcomes.get(test.id(), 'subtests; see aggregate result')))
        super().stopTest(test)


class TimedSuite(unittest.TestSuite):
    def _handleClassSetUp(self, test, result):
        current = test.__class__
        changed = getattr(result, '_previousTestClass', None) != current
        started = time.perf_counter()
        super()._handleClassSetUp(test, result)
        if changed:
            result.fixtures.append(dict(fixture=current.__module__ + '.' + current.__qualname__ + '.setUpClass',
                                        seconds=time.perf_counter() - started))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['python', 'lints'])
    parser.add_argument('--json', type=Path, required=True)
    parser.add_argument('--tests', nargs='+', help='profile these Python test names instead of full discovery')
    parser.add_argument('--jobs', type=int, choices=range(1, 5), default=1,
                        help='isolate independent selected Python modules in worker processes')
    args = parser.parse_args()
    # Audit output must be external, even when a caller supplies a path.
    if args.json.resolve().is_relative_to(ROOT):
        parser.error('--json must point outside the repository')
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    os.environ.update(PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1')
    started = time.perf_counter()
    if args.jobs > 1 and (args.kind != 'python' or not args.tests):
        parser.error('--jobs requires python --tests')
    if args.kind == 'python' and args.jobs > 1:
        # Balance measured expensive modules instead of placing all generators
        # in one worker. Each worker still owns its imports and mutable fixtures.
        groups = {}
        for name in args.tests:
            module = next((part for part in name.split('.') if part.startswith('test_')), name)
            groups.setdefault(module, []).append(name)
        count = min(args.jobs, len(groups))
        batches, costs = [[] for _ in range(count)], [0] * count
        for module in sorted(groups, key=lambda n: (-PYTHON_COSTS.get(n, 1), n)):
            worker = min(range(count), key=lambda i: (costs[i], i))
            batches[worker].extend(sorted(groups[module])); costs[worker] += PYTHON_COSTS.get(module, 1)
        with tempfile.TemporaryDirectory(prefix='rrt-python-audit-') as scratch:
            def run_batch(pair):
                i, names = pair
                output = Path(scratch) / (str(i) + '.json')
                run = subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), 'python',
                    '--json', str(output), '--tests', *names], capture_output=True, text=True)
                return run, json.loads(output.read_text(encoding="utf-8")) if output.exists() else None
            with ThreadPoolExecutor(max_workers=count) as pool:
                results = list(pool.map(run_batch, enumerate(batches)))
            for run, result in results:
                sys.stdout.write(run.stdout); sys.stderr.write(run.stderr)
            if any(result is None for run, result in results):
                return 1
            data = dict(seconds=time.perf_counter() - started,
                passed=all(run.returncode == 0 and result['passed'] for run, result in results),
                tests=sum(result['tests'] for run, result in results),
                skipped=sum(result['skipped'] for run, result in results),
                rows=sorted([row for run, result in results for row in result['rows']], key=lambda r: r['test']),
                fixtures=[row for run, result in results for row in result['fixtures']])
            code = 0 if data['passed'] else 1
    elif args.kind == 'python':
        loader = unittest.TestLoader()
        loader.suiteClass = TimedSuite
        suite = loader.loadTestsFromNames(args.tests) if args.tests else loader.discover('tests', pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=1, resultclass=TimedResult).run(suite)
        data = dict(seconds=time.perf_counter() - started, passed=result.wasSuccessful(),
                    tests=result.testsRun, skipped=len(result.skipped), rows=result.rows, fixtures=result.fixtures)
        code = 0 if result.wasSuccessful() else 1
    else:
        rows = []
        with tempfile.TemporaryDirectory(prefix='rrt-lint-audit-') as scratch:
            for path in sorted((ROOT / 'tools').glob('*_lint.py')):
                text = path.read_text(encoding='utf-8-sig')
                command = [sys.executable, '-m', 'tools.' + path.stem]
                # Several lints intentionally expose only check(story). Running
                # them with -m imports a module and measures no protection.
                if not re.search(r'^if __name__\s*==', text, re.M):
                    command = [sys.executable, '-c',
                        'import importlib,json; from pathlib import Path; '
                        'm=importlib.import_module(' + repr('tools.' + path.stem) + '); '
                        's=json.loads(Path("development/Story.json").read_text()); '
                        'r=m.check(s); print("checked", len(r))']
                # Use the actual default contract for non-story metadata lints.
                elif '"--story"' in text or "'--story'" in text:
                    command += ['--story', str(ROOT / 'development/Story.json')]
                elif path.stem == 'native_gate_contract_lint':
                    command += [str(ROOT / 'development/Story.json')]
                begin = time.perf_counter()
                log = Path(scratch) / (path.stem + '.log')
                with log.open('w') as out:
                    run = subprocess.run(command, cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
                rows.append(dict(lint=path.name, seconds=time.perf_counter() - begin,
                                 exit=run.returncode, tail=log.read_text(errors='replace', encoding="utf-8").splitlines()[-4:]))
                print(f'{path.name}: {rows[-1]["seconds"]:.3f}s (exit {run.returncode})', flush=True)
        data = dict(seconds=time.perf_counter() - started, rows=rows)
        code = 0  # an inventory records existing advisory debt; gate policies are unchanged
    args.json.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    return code


if __name__ == '__main__':
    sys.exit(main())
