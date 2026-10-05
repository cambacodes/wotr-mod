"""Measure tests/lints without writing artifacts in the worktree.

Usage: python tools/test_audit.py python --json /tmp/python-times.json
       python tools/test_audit.py lints --json /tmp/lint-times.json
RulesTests emits per-suite measurements when RRT_TEST_TIMINGS points into /tmp.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TimedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = []

    def startTest(self, test):
        self.started = time.perf_counter()
        super().startTest(test)

    def stopTest(self, test):
        self.rows.append(dict(test=test.id(), seconds=time.perf_counter() - self.started))
        super().stopTest(test)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['python', 'lints'])
    parser.add_argument('--json', type=Path, required=True)
    args = parser.parse_args()
    # Audit output must be external, even when a caller supplies a path.
    if args.json.resolve().is_relative_to(ROOT):
        parser.error('--json must point outside the repository')
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    os.environ.update(PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1')
    started = time.perf_counter()
    if args.kind == 'python':
        suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=1, resultclass=TimedResult).run(suite)
        data = dict(seconds=time.perf_counter() - started, passed=result.wasSuccessful(),
                    tests=result.testsRun, skipped=len(result.skipped), rows=result.rows)
        code = 0 if result.wasSuccessful() else 1
    else:
        rows = []
        with tempfile.TemporaryDirectory(prefix='rrt-lint-audit-') as scratch:
            for path in sorted((ROOT / 'tools').glob('*_lint.py')):
                text = path.read_text(encoding='utf-8-sig')
                command = [sys.executable, '-m', 'tools.' + path.stem]
                # Use the actual default contract for non-story metadata lints.
                if '"--story"' in text or "'--story'" in text:
                    command += ['--story', str(ROOT / 'development/Story.json')]
                elif path.stem == 'native_gate_contract_lint':
                    command += [str(ROOT / 'development/Story.json')]
                begin = time.perf_counter()
                log = Path(scratch) / (path.stem + '.log')
                with log.open('w') as out:
                    run = subprocess.run(command, cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
                rows.append(dict(lint=path.name, seconds=time.perf_counter() - begin,
                                 exit=run.returncode, tail=log.read_text(errors='replace').splitlines()[-4:]))
                print(f'{path.name}: {rows[-1]["seconds"]:.3f}s (exit {run.returncode})', flush=True)
        data = dict(seconds=time.perf_counter() - started, rows=rows)
        code = 0  # an inventory records existing advisory debt; gate policies are unchanged
    args.json.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    return code


if __name__ == '__main__':
    sys.exit(main())
