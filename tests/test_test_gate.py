"""H07 public gate probes; all commands and mutations run in disposable fixtures."""
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

from tools import test_gate
from tools.gate_receipts import StageRunner, hard_count, sha256, validate_coverage

ROOT = Path(__file__).resolve().parents[1]


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='rrt-h07-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        (self.repo / 'tools').mkdir(parents=True)
        (self.repo / 'development').mkdir()
        (self.repo / 'tests').mkdir()
        for name in ('test_gate.py', 'gate_receipts.py', 'fast_gate.sh'):
            shutil.copyfile(ROOT / 'tools' / name, self.repo / 'tools' / name)
        (self.repo / 'tools/test_selection.py').write_text(
            'from pathlib import Path\nROOT=Path(__file__).resolve().parents[1]\n'
            'def changed_files(base): return []\n'
            'def select(files): return {"python":["tests.one","tests.two"],"suites":["FixtureProgression"]}\n', encoding="utf-8")
        (self.repo / 'tools/draft_contract_lint.py').write_text(
            'from pathlib import Path\nROOT=Path(__file__).resolve().parents[1]\ndef inventory(): return []\n', encoding="utf-8")
        (self.repo / 'expansion.py').write_text(
            'from pathlib import Path\nPath("development/Story.json").write_text(\'{"Scenes":[{"Id":"fixture"}]}\')\n', encoding="utf-8")
        for name in ('rrt_verify', 'crossroute_lint', 'pacing_lint', 'harem_schedule_lint',
                     'harem_smoothing_lint', 'slot_brief_lint', 'payoff_lint', 'departure_lint', 'voice_lock_lint', 'test_audit'):
            (self.repo / 'tools' / (name + '.py')).write_text('print("HARD FAILURES: 0")\n', encoding="utf-8")
        executable = self.base / 'dotnet'
        executable.write_text('#!/usr/bin/env python3\nprint("PASS synthetic C# command fixture")\n', encoding="utf-8")
        executable.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.base) + os.pathsep + os.environ['PATH'],
                        PYTHONDONTWRITEBYTECODE='1')

    def gate(self, receipt='receipt.json', *argv):
        result = subprocess.run(['bash', 'tools/fast_gate.sh', '--json', str(self.base / receipt),
                                 '--timeout', '3', *argv], cwd=self.repo, env=self.env,
                                capture_output=True, text=True, timeout=25)
        return result, json.loads((self.base / receipt).read_text(encoding="utf-8"))

    def test_actual_commands_inventory_and_receipt_identity(self):
        result, receipt = self.gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertTrue(receipt['passed'])
        self.assertEqual(1, receipt['scene_count'])
        for key in ('source_hash', 'export_hash', 'policy_hash'):
            self.assertEqual(64, len(receipt[key]))
        self.assertEqual({'verify', 'crossroute', 'pacing', 'schedule', 'smoothing', 'slot',
                          'payoff', 'departure', 'voice', 'python', 'rules'}, set(receipt['coverage']))
        python = next(s for s in receipt['stages'] if s['stage'] == 'python')
        rules = next(s for s in receipt['stages'] if s['stage'] == 'rules')
        self.assertEqual('Python tests', python['check_kind'])
        self.assertEqual('C# progression', rules['check_kind'])
        self.assertIn('--suites=FixtureProgression', rules['command'])
        self.assertFalse(any('discover' in s['command'] for s in receipt['stages']))

    def test_ownership_modes_and_both_approval_records_survive_merge(self):
        from argparse import Namespace
        from tools.gate_receipts import lint_commands
        commands = lint_commands('python', Path('story'), '/wrath', self.base)
        args = Namespace(voice_job=self.base / 'voice.json', append_approvals=self.base / 'append.json')
        for full in (False, True):
            with self.subTest(full=full):
                actual = test_gate.ownership_commands(commands, args, full)
                voice = dict(actual)['voice']
                self.assertIn('--milestone' if full else '--integration', voice)
                self.assertNotIn('--integration' if full else '--milestone', voice)
                self.assertEqual(str(args.voice_job), voice[voice.index('--job') + 1])
                self.assertEqual(str(args.append_approvals), voice[voice.index('--append-approvals') + 1])
                self.assertEqual([c for c in commands if c[0] != 'voice'], [c for c in actual if c[0] != 'voice'])
        self.assertNotIn('--integration', dict(commands)['voice'])

    def test_required_lint_omission_through_public_plan_fails(self):
        from tools.gate_receipts import lint_commands
        commands = lint_commands('python', Path('story'), '/wrath', Path('/tmp/probe'))
        with patch.object(test_gate, 'select', return_value={'python': [], 'suites': []}), \
             patch.object(test_gate, 'lint_commands', return_value=[c for c in commands if c[0] != 'voice']), \
             patch.object(sys, 'argv', ['test_gate.py', '--plan', '--files', 'tools/test_gate.py']):
            with self.assertRaisesRegex(ValueError, 'voice'):
                test_gate.main()
        for label, command in commands:
            with self.subTest(label=label), self.assertRaises(ValueError):
                validate_coverage([c for c in commands if c[0] != label])

    def test_zero_hard_failures_is_zero(self):
        self.assertEqual(0, hard_count('HARD FAILURES: 0\nDeparture: 0 hard failures'))
        self.assertEqual(3, hard_count('3 hard failures'))

    def test_missing_execution_cannot_leave_a_zero_exit_receipt(self):
        runner = StageRunner(self.repo, self.base, self.env, 1, {})
        receipt = runner.write(self.base / 'omitted.json', 'FAST', {}, {'rules': {'kind': 'C# progression'}},
                               ['rules'], .01, 0)
        self.assertEqual(125, receipt['exit'])
        self.assertFalse(receipt['passed'])
        self.assertFalse(receipt['coverage']['rules']['complete'])
        runner.stages.append({'stage': 'rules', 'exit': 1, 'complete': True})
        receipt = runner.write(None, 'FAST', {}, {'rules': {'kind': 'C# progression'}}, ['rules'], .01, 0)
        self.assertEqual(1, receipt['exit'])
        self.assertFalse(receipt['passed'])
        self.assertFalse(receipt['coverage']['rules']['passed'])

    def test_exit_143_is_incomplete_and_receipt_survives(self):
        (self.repo / 'expansion.py').write_text('raise SystemExit(143)\n', encoding="utf-8")
        result, receipt = self.gate()
        self.assertEqual(143, result.returncode)
        self.assertFalse(receipt['complete'])
        expansion = next(s for s in receipt['stages'] if s['stage'] == 'expansion')
        self.assertEqual(143, expansion['exit'])
        self.assertFalse(expansion['complete'])
        self.assertTrue(any(s.get('incomplete_reason') == 'skipped after failed prerequisite' for s in receipt['stages']))

    def test_baseline_red_and_new_red_are_distinct_without_exemption(self):
        lint = self.repo / 'tools/payoff_lint.py'
        lint.write_text('print("HARD old defect")\nraise SystemExit(1)\n', encoding="utf-8")
        result, baseline = self.gate('baseline.json', '--collect-failures')
        self.assertEqual(1, result.returncode)
        self.assertTrue(baseline['complete'])
        pin = sha256(self.base / 'baseline.json')
        lint.write_text('print("HARD old defect\\nHARD new defect")\nraise SystemExit(1)\n', encoding="utf-8")
        result, current = self.gate('new.json', '--collect-failures', '--baseline', str(self.base / 'baseline.json'),
                                    '--baseline-sha256', pin)
        self.assertEqual(1, result.returncode)
        stage = next(s for s in current['stages'] if s['stage'] == 'payoff')
        self.assertEqual(pin, current['baseline']['_receipt_pin'])
        self.assertEqual(baseline['source_hash'], current['baseline']['source_hash'])
        self.assertEqual(['HARD old defect'], stage['defects']['baseline'])
        self.assertEqual(['HARD new defect'], stage['defects']['new'])
        self.assertFalse(current['passed'])

    def test_baseline_pin_mismatch_fails_closed(self):
        self.gate('baseline.json')
        result = subprocess.run([sys.executable, 'tools/test_gate.py', '--files', 'tools/test_gate.py',
            '--json', str(self.base / 'rejected.json'),
            '--baseline', str(self.base / 'baseline.json'), '--baseline-sha256', '0' * 64],
            cwd=self.repo, env=self.env, capture_output=True, text=True, timeout=10)
        self.assertNotEqual(0, result.returncode)
        self.assertIn('pinned SHA256', result.stderr)

    @unittest.skipUnless(os.name == 'posix', 'POSIX process group probe')
    def test_timeout_kills_sleeping_descendant(self):
        marker = self.base / 'escaped'
        child = 'import time; from pathlib import Path; time.sleep(1); Path(' + repr(str(marker)) + ').touch()'
        command = [sys.executable, '-c', 'import subprocess,sys,time; subprocess.Popen([sys.executable,"-c",'
                   + repr(child) + ']); time.sleep(20)']
        runner = StageRunner(self.repo, self.base, self.env, .2, {})
        with self.assertRaises(subprocess.CalledProcessError) as failure:
            runner.run('sleep', command)
        self.assertEqual(124, failure.exception.returncode)
        self.assertFalse(runner.stages[0]['complete'])
        # Bound observation of the descendant's attempted write.
        subprocess.run([sys.executable, '-c', 'import time; time.sleep(1.1)'], timeout=3, check=True)
        self.assertFalse(marker.exists(), 'descendant survived timeout')

    @unittest.skipUnless(os.name == 'posix', 'POSIX cancellation probe')
    def test_public_gate_cancellation_preserves_incomplete_receipt(self):
        ready, escaped = self.base / 'ready', self.base / 'escaped'
        child = 'import time; from pathlib import Path; time.sleep(1); Path(' + repr(str(escaped)) + ').touch()'
        (self.repo / 'expansion.py').write_text('import subprocess,sys,time\nfrom pathlib import Path\n'
            'subprocess.Popen([sys.executable,"-c",' + repr(child) + '])\nPath(' + repr(str(ready)) + ').touch()\ntime.sleep(20)\n', encoding="utf-8")
        receipt = self.base / 'cancelled.json'
        process = subprocess.Popen(['bash', 'tools/fast_gate.sh', '--json', str(receipt), '--timeout', '5'],
            cwd=self.repo, env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            deadline = time.monotonic() + 5
            while not ready.exists() and process.poll() is None and time.monotonic() < deadline:
                time.sleep(.02)
            self.assertTrue(ready.exists(), 'fixture expansion did not start')
            process.send_signal(signal.SIGTERM)
            out, error = process.communicate(timeout=10)
            self.assertEqual(143, process.returncode, out + error)
            self.assertFalse(json.loads(receipt.read_text(encoding="utf-8"))['complete'])
            time.sleep(1.1)
            self.assertFalse(escaped.exists(), 'cancelled gate left a descendant')
        finally:
            if process.poll() is None:
                process.kill()
                process.wait(timeout=5)


if __name__ == '__main__':
    unittest.main()
