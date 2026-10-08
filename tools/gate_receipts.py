"""Bounded stage execution and durable evidence for the existing gate entry point."""
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import threading
import time


# Independent required inventory: removing a command from a profile fails preflight.
REQUIRED_LINTS = frozenset({'verify', 'crossroute', 'pacing', 'schedule', 'smoothing',
                            'slot', 'payoff', 'departure', 'voice'})
LINT_COMMANDS = {
    'verify': ('tools/rrt_verify.py', '--strict'),
    'crossroute': ('tools/crossroute_lint.py',),
    'pacing': ('tools/pacing_lint.py',),
    'schedule': ('tools/harem_schedule_lint.py',),
    'smoothing': ('tools/harem_smoothing_lint.py', '--strict-forms'),
    'slot': ('tools/slot_brief_lint.py', '--strict', '--known-rebuilds'),
    'payoff': ('tools/payoff_lint.py', '--strict'),
    'departure': ('tools/departure_lint.py', '--strict'),
    'voice': ('tools/voice_lock_lint.py', '--strict'),
}


def lint_commands(python, story, game, scratch, full=False):
    commands = []
    for label, argv in LINT_COMMANDS.items():
        command = [python, *argv, '--story', str(story)]
        if label == 'verify':
            command += ['--quiet', '--game', game, '--json', str(scratch / 'verify.json'),
                        '--text', str(scratch / 'verify.txt')]
            if not full:
                command += ['--gate-only']
        if label == 'pacing':
            command += ['--availability', 'tools/pacing-availability.json']
        commands.append((label, command))
    validate_coverage(commands)
    return commands


def validate_coverage(commands):
    actual = {label: list(argv) for label, argv in commands}
    missing = [label for label in sorted(REQUIRED_LINTS)
               if label not in actual or not all(token in actual[label] for token in LINT_COMMANDS[label])]
    if missing:
        raise ValueError('Required lint coverage missing: ' + ', '.join(missing))
    return {label: {'command': command} for label, command in actual.items()}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_hash(root):
    """Hash source/config bytes, including untracked inputs; exclude generated output."""
    digest = hashlib.sha256()
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if any(p in {'.git', '__pycache__', 'obj', 'bin', '.runs', 'dist'} for p in relative.parts):
            continue
        if not path.is_file() or path.suffix in {'.pyc', '.log'} or relative.parts[0] == 'development':
            continue
        digest.update(str(relative).replace(os.sep, '/').encode() + b'\0')
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def identity(root, story, policies):
    policy_files = {str(path.relative_to(root)) if path.is_relative_to(root) else str(path):
                    sha256(path) if path.is_file() else None for path in policies}
    return {'source_hash': source_hash(root), 'export_hash': sha256(story) if story.is_file() else None,
            'policy_hash': hashlib.sha256(json.dumps(policy_files, sort_keys=True).encode()).hexdigest(),
            'policy_files': policy_files,
            'scene_count': len(json.loads(story.read_text(encoding='utf-8-sig'))['Scenes']) if story.is_file() else None}


def hard_count(output):
    counts = re.findall(r'(?:HARD FAILURES:\s*(\d+)|(\d+)\s+hard failures\b)', output, re.I)
    return sum(int(a or b) for a, b in counts) if counts else None


def observations(output, exit_code, root, scratch):
    # Failed commands remain failed, even when also reproducing baseline debt.
    if exit_code == 0:
        return []
    output = output.replace(str(root), '<repo>').replace(str(scratch), '<scratch>')
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    return sorted(set(line for line in lines if not re.search(r'\b\d+(?:\.\d+)?\s*(?:seconds|s|ms)\b', line))) or ['nonzero exit: ' + str(exit_code)]


def load_baseline(path, pin, profile, policy_hash):
    if sha256(path) != pin:
        raise ValueError('Baseline receipt does not match the pinned SHA256')
    baseline = json.loads(path.read_text(encoding='utf-8'))
    if baseline.get('mode') != profile or baseline.get('policy_hash') != policy_hash or not baseline.get('source_hash'):
        raise ValueError('Baseline profile/policy/source identity mismatch')
    if not baseline.get('complete') or not baseline.get('stages') or any(not s.get('complete') for s in baseline['stages']):
        raise ValueError('Baseline evidence is incomplete')
    baseline['_receipt_pin'] = pin
    baseline['_receipt_path'] = str(path)
    return baseline


def compare(stage, baseline):
    if baseline is None:
        return {'status': 'unclassified', 'baseline': [], 'new': [], 'observed': stage['findings']}
    old = next((s for s in baseline['stages'] if s['stage'] == stage['stage']), None)
    if old is None or old.get('check_command') != stage['check_command']:
        return {'status': 'unclassified', 'baseline': [], 'new': [], 'observed': stage['findings']}
    before, after = set(old['findings']), set(stage['findings'])
    return {'status': 'compared', 'baseline': sorted(before & after), 'new': sorted(after - before),
            'resolved': sorted(before - after)}


def _terminate_tree(process):
    if os.name == 'posix':
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    else:
        subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                       capture_output=True, timeout=10, check=False)
    process.wait(timeout=10)


class StageRunner:
    def __init__(self, root, scratch, env, timeout, snapshot, baseline=None):
        self.root, self.scratch, self.env = root, scratch, env
        self.timeout, self.snapshot, self.baseline = timeout, snapshot, baseline
        self.stages = []
        self._processes = set()
        self._lock = threading.Lock()
        self._cancelled = False

    def cancel(self):
        with self._lock:
            self._cancelled = True
            for process in self._processes:
                _terminate_tree(process)

    def run(self, label, command, env=None):
        begin = time.monotonic()
        log = self.scratch / (label + '.log')
        code, reason = 125, None
        print('RUN ' + label, flush=True)
        try:
            with log.open('w', encoding='utf-8') as out:
                with self._lock:
                    if self._cancelled:
                        reason, code = 'cancelled', 130
                        raise subprocess.CalledProcessError(code, command)
                    process = subprocess.Popen(command, cwd=self.root, env=env or self.env, stdout=out,
                        stderr=subprocess.STDOUT, start_new_session=os.name == 'posix',
                        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0)
                    self._processes.add(process)
                try:
                    code = process.wait(timeout=self.timeout)
                    _terminate_tree(process)
                    if code < 0 or code in {124, 137, 143}:
                        reason = 'killed or timed out'
                except subprocess.TimeoutExpired:
                    reason, code = 'timeout', 124
                    _terminate_tree(process)
                except BaseException:
                    reason, code = 'cancelled', 130
                    _terminate_tree(process)
                    raise
                finally:
                    with self._lock:
                        self._processes.discard(process)
        except OSError as error:
            reason = str(error)
        finally:
            output = log.read_text(errors='replace', encoding='utf-8') if log.exists() else ''
            check_command = [str(c).replace(str(self.root), '<repo>').replace(str(self.scratch), '<scratch>') for c in command]
            stage = dict(self.snapshot, stage=label, command=command, check_command=check_command,
                         exit=code, complete=reason is None, incomplete_reason=reason,
                         seconds=time.monotonic() - begin, receipt=output.splitlines()[-4:],
                         output=output, hard_failures=hard_count(output),
                         evidence_kind='managed construction' if label == 'managed' else 'synthetic fixture',
                         check_kind='C# progression' if label == 'rules' else 'Python tests' if label == 'python' else label,
                         findings=observations(output, code, self.root, self.scratch))
            stage['defects'] = compare(stage, self.baseline)
            self.stages.append(stage)
        if code:
            print(output, flush=True)
            raise subprocess.CalledProcessError(code if code > 0 else 128 - code, command)
        print(f'PASS {label}: {stage["seconds"]:.2f}s', flush=True)

    def write(self, path, mode, selection, coverage, expected, elapsed, exit_code):
        stages = list(self.stages)
        ran = {s['stage'] for s in stages}
        for label in expected:
            if label not in ran:
                stages.append(dict(self.snapshot, stage=label, exit=None, complete=False,
                                   incomplete_reason='skipped after failed prerequisite', command=None))
        complete = all(s['complete'] for s in stages)
        if exit_code == 0:
            exit_code = next((s['exit'] for s in stages if s.get('exit')), 0)
        if not complete and exit_code == 0:
            exit_code = 125
        actual_coverage = {label: dict(check, complete=any(s['stage'] == label and s['complete'] for s in stages),
                                      passed=any(s['stage'] == label and s['complete'] and s['exit'] == 0 for s in stages))
                           for label, check in coverage.items()}
        receipt = dict(self.snapshot, schema=1, mode=mode, selection=selection, coverage=actual_coverage,
                       seconds=elapsed, exit=exit_code, complete=complete,
                       passed=complete and exit_code == 0, stages=stages)
        receipt['baseline'] = {key: self.baseline.get(key) for key in
            ('source_hash', 'export_hash', 'policy_hash', '_receipt_pin', '_receipt_path')} if self.baseline else None
        for name, filename in [('rules', 'rules-times.json'), ('python', 'python-times.json')]:
            measurement = self.scratch / filename
            try:
                receipt[name] = json.loads(measurement.read_text(encoding='utf-8'))
            except (OSError, ValueError):
                receipt[name] = None
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(path.suffix + '.tmp')
            temporary.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
            temporary.replace(path)
        return receipt
