"""S0 byte-preserving guard. Baselines and results must live in system temp.

capture --source CLEAN_PREDECESSOR --out BASELINE [--game GAME]
check --baseline BASELINE --source CANDIDATE --out RESULTS
      [--allow-source EXACT_CODE_PATH ...]

No acceptance override or baseline refresh exists. Existing gate debt is evidence,
never permission to accept a failing candidate. S0 freezes the default expansion;
other profiles and same-process compiler isolation belong to S1.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tempfile

FORMAT = 1
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
PARENTS = tuple('reference/canon-review/' + name + '.json' for name in (
    'expansion-parent-bindings', 'nurah-parent-bindings',
    'nurah-parent-runtime-cue-bindings', 'terendelev-parent-bindings'))
EXPORTS = {'development/Story.json', 'package/Story.json'}
NAMESPACE = 'RanRomance.Tirabade.v1/'
TIMEOUT = 1800


class GuardError(ValueError):
    pass


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(',', ':')) + '\n').encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_hash(path):
    sha = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            sha.update(block)
    return sha.hexdigest()


def git(source, *args):
    return subprocess.check_output(['git', '-C', str(source), *args],
                                   stderr=subprocess.PIPE).decode('utf-8').strip()


def source_files(source):
    """Pin every tracked/nonignored file, plus ignored executable/data inputs.

    A new contract, discovered row or ignored Python module must not silently
    escape the inventory. Only known outputs/build caches are excluded.
    """
    names = set(git(source, 'ls-files', '-z', '--cached', '--others',
                    '--exclude-standard').split('\0')) - {''}
    for area in ('storylines', 'tools', 'reference', 'data', 'src', 'tests', 'authoring'):
        for path in (source / area).rglob('*'):
            if path.suffix in {'.py', '.json', '.cs', '.csproj', '.props'}:
                names.add(path.relative_to(source).as_posix())
    result = {}
    for name in sorted(names - EXPORTS):
        path = source / name
        if any(part in {'.git', '__pycache__', 'obj', 'bin'} for part in Path(name).parts):
            continue
        if path.is_symlink():
            raise GuardError('Unpinned symlink input: ' + name)
        if path.is_file():
            result[name] = dict(sha256=file_hash(path), bytes=path.stat().st_size,
                                executable=bool(path.stat().st_mode & 0o111))
    return result


def external_inputs(source, game):
    """Hash native archives/localization and every reviewed parent assembly."""
    paths = {'blueprints.zip': game / 'blueprints.zip',
             'enGB.json': game / 'Wrath_Data/StreamingAssets/Localization/enGB.json'}
    # Parent evidence outside the build's four manifests is also a reference input.
    for manifest in sorted((source / 'reference/canon-review').glob('*parent*bindings*.json')):
        data = json.loads(manifest.read_text(encoding='utf-8-sig'))
        if 'AssemblyPath' not in data:
            continue
        original = data['AssemblyPath']
        assembly = Path(original)
        if not assembly.is_file():
            match = re.search(r'(?i)[\\/]Mods[\\/](.*)', original)
            if match:
                assembly = game / 'Mods' / match[1].replace('\\', '/')
        actual = file_hash(assembly)
        if actual.lower() != data['AssemblySha256'].lower():
            raise GuardError('Parent assembly differs: ' + manifest.name)
        paths['parent/' + manifest.name] = assembly
    evidence = {name: dict(sha256=file_hash(path), bytes=path.stat().st_size)
                for name, path in sorted(paths.items())}
    return evidence, paths


def runtime_inputs(source):
    script = (source / 'build-expansion.ps1').read_text(encoding='utf-8-sig')
    block = script.split('$env:RRT_PARENT_BINDINGS = (@(', 1)[1].split(')', 1)[0]
    declared = tuple(re.findall(r"'(reference/[^']+\.json)'", block))
    if declared != PARENTS:
        raise GuardError('Build-script parent order changed: ' + repr(declared))
    return dict(python=sys.version, python_executable_sha256=file_hash(Path(sys.executable)),
                dotnet=subprocess.check_output(['dotnet', '--version']).decode().strip(),
                platform=sys.platform, parent_order=[p for p in PARENTS if (source / p).is_file()],
                profile='default-expansion/independent_tirabade=True',
                hashseed='0', utf8='1', destination_seeds=['LF', 'CRLF'],
                serializer='expansion.py CLI; raw bytes; no normalization',
                required_suites=['python-discovery', 'strict-verifier', 'rules-progression'])


def temporary_output(path, source):
    path = path.resolve()
    temp = Path(tempfile.gettempdir()).resolve()
    if not path.is_relative_to(temp) or path == temp or path.is_relative_to(source.resolve()):
        raise GuardError('Output must be a new directory in system temp, outside source')
    if path.exists():
        raise GuardError('Refusing to overwrite immutable output: ' + str(path))
    return path


def clean_environment(snapshot, scratch, game):
    # Preserve only host infrastructure. Inherited test fixtures, story output,
    # PYTHONPATH and route flags must not influence compilation or checks.
    env = {key: value for key, value in os.environ.items()
           if not key.startswith(('RRT_', 'PYTHON', 'GIT_'))}
    env.update(PYTHONHASHSEED='0', PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               RRT_ROOT=str(snapshot), RRT_GAME_DIR=str(game), RRT_PYTHON=sys.executable,
               RRT_PARENT_BINDINGS=os.pathsep.join(str(snapshot / p) for p in PARENTS
                                                  if (snapshot / p).is_file()),
               RRT_TEST_BUILD_ROOT=str(scratch / 'rules-build'),
               RRT_TEST_TIMINGS=str(scratch / 'rules-times.json'),
               RRT_NATIVE_COVERAGE_OUTPUT=str(scratch / 'native-coverage.json'),
               TMPDIR=str(scratch), TMP=str(scratch), TEMP=str(scratch),
               GIT_OPTIONAL_LOCKS='0')
    return env


def execute(command, cwd, env, log, timeout=TIMEOUT):
    """Bound the whole process group, including children left by failed parents.

    H2's executor is a proposal in this checkout; no callable executor exists.
    Keep this private until its coordinator-owned implementation is available.
    """
    started = datetime.now(timezone.utc).isoformat()
    timed_out = False
    with log.open('wb') as output:
        process = subprocess.Popen(command, cwd=cwd, env=env, stdout=output,
                                   stderr=subprocess.STDOUT, start_new_session=os.name != 'nt')
        try:
            code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            code = None
        finally:
            if os.name == 'nt':
                if timed_out:
                    subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            process.wait()
    return dict(exit=code, timed_out=timed_out, started=started,
                finished=datetime.now(timezone.utc).isoformat(), log_sha256=file_hash(log))


def first_difference(before, after, path='$'):
    """Ordered diagnostic only; it never decides byte acceptance."""
    if type(before) is not type(after):
        return path + ': type changed'
    if isinstance(before, dict):
        if list(before) != list(after):
            return path + ': dictionary key order/keys changed'
        for key in before:
            difference = first_difference(before[key], after[key], path + '.' + key)
            if difference:
                return difference
    elif isinstance(before, list):
        if len(before) != len(after):
            return path + ': count %d -> %d' % (len(before), len(after))
        for index, (old, new) in enumerate(zip(before, after)):
            difference = first_difference(old, new, '%s[%d]' % (path, index))
            if difference:
                return difference
    elif before != after:
        return path + ': %r -> %r' % (str(before)[:100], str(after)[:100])
    return None


def byte_difference(before, after):
    if before == after:
        return None
    offset = next((i for i, (a, b) in enumerate(zip(before, after)) if a != b),
                  min(len(before), len(after)))
    try:
        detail = first_difference(json.loads(before), json.loads(after)) or '$: serialization/newline/BOM changed'
    except (ValueError, UnicodeError):
        detail = 'invalid JSON/encoding'
    return dict(first_byte=offset, before_bytes=len(before), after_bytes=len(after),
                before_sha256=digest(before), after_sha256=digest(after), path=detail,
                before_neighborhood=repr(before[max(0, offset - 40):offset + 80]),
                after_neighborhood=repr(after[max(0, offset - 40):offset + 80]))


def predecessor_inventory(story):
    from tools import savecompat
    return dict(scene_order=[s['Id'] for s in story['Scenes']],
                relationship_order=list(story.get('Relationships', {})),
                nodes=[dict(scene=s['Id'], order=[n['Id'] for n in s['Nodes']],
                            choices=[dict(node=n['Id'], identities=savecompat.choice_identities(s, n),
                                          targets=[{k: c.get(k) for k in ('Next', 'NativeNext', 'Check')}
                                                   for c in n['Choices']]) for n in s['Nodes']])
                       for s in story['Scenes']])


def ownership_failures(before, after, allowed):
    changed = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
    failures = []
    for path in changed:
        # References, contracts, runtime/gate tools are pinned even if named.
        code = (path in {'expansion.py', 'story.py', 'story_format.py'}
                or path.startswith(('storylines/', 'authoring/', 'tests/')) and path.endswith(('.py', '.cs'))
                or path == 'tools/refactor_guard.py')
        if path not in allowed or not code:
            failures.append('Unaccounted input/source change: ' + path)
    return changed, failures


def snapshot_source(source, target, files):
    target.mkdir()
    for name, entry in files.items():
        destination = target / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / name, destination)
        if file_hash(destination) != entry['sha256']:
            raise GuardError('Input changed while copying: ' + name)
    for name in EXPORTS:
        if (source / name).is_file():
            (target / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source / name, target / name)
    # Immutable revision context for existing HEAD-relative tests, without an
    # attached index/worktree or writes to the original Git metadata.
    metadata = target / '.git'
    metadata.mkdir()
    (metadata / 'objects/info').mkdir(parents=True)
    common = Path(git(source, 'rev-parse', '--git-common-dir'))
    if not common.is_absolute():
        common = source / common
    (metadata / 'objects/info/alternates').write_text(str(common.resolve() / 'objects') + '\n')
    (metadata / 'refs').mkdir()
    (metadata / 'HEAD').write_text(git(source, 'rev-parse', 'HEAD') + '\n')
    (metadata / 'config').write_text('[core]\n\trepositoryformatversion = 0\n\tbare = false\n')
    subprocess.run(['git', '-C', str(target), 'read-tree', 'HEAD'], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def worker(snapshot, inputs_path, reads_path):
    """Run the real CLI, auditing data reads after interpreter startup."""
    import runpy
    inputs = json.loads(inputs_path.read_text())
    allowed = set(inputs['files'])
    external = {str(Path(p).resolve()) for p in inputs['external']}
    libraries = {Path(sys.base_prefix).resolve(), Path(sys.prefix).resolve()}
    reads = set()

    def audit(event, args):
        if event != 'open' or isinstance(args[0], int):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        mode, flags = args[1], args[2]
        writing = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        if not writing and path.suffix == '.pyc' and not path.exists():
            return  # Importlib probes absent caches even with -B.
        if path.is_relative_to(snapshot):
            name = path.relative_to(snapshot).as_posix()
            if writing:
                if name != 'development/Story.json':
                    raise GuardError('Generator wrote unaccounted output: ' + name)
            elif name not in allowed and name != 'development/Story.json':
                raise GuardError('Generator read unaccounted input: ' + name)
            elif name in allowed:
                reads.add(name)
        elif str(path) in external:
            if writing:
                raise GuardError('Generator wrote external input: ' + str(path))
            reads.add('external:' + str(path))
        elif not any(path.is_relative_to(lib) for lib in libraries):
            raise GuardError('Generator read unaccounted external input: ' + str(path))

    sys.addaudithook(audit)
    sys.path.insert(0, str(snapshot))
    os.chdir(snapshot)
    sys.argv = ['expansion.py']
    try:
        runpy.run_path(str(snapshot / 'expansion.py'), run_name='__main__')
    finally:
        # This output is outside the audited source; write through a descriptor
        # opened before installing the audit hook by the command entry point.
        os.write(inputs['reads_fd'], canonical(sorted(reads)))


def generation(source, files, game, externals, scratch, observations, failures):
    outputs = {}
    read_sets = {}
    jobs = []
    for seed in ('LF', 'CRLF'):
        for repeat in range(2):
            label = '%s-%d' % (seed, repeat)
            work = scratch / label
            snapshot_source(source, work, files)
            output = work / 'development/Story.json'
            output.parent.mkdir(exist_ok=True)
            output.write_bytes(b'\r\n' if seed == 'CRLF' else b'\n')
            inputs = scratch / (label + '-inputs.json')
            reads = scratch / (label + '-reads.json')
            inputs.write_bytes(canonical(dict(files=files, external=[str(p.resolve()) for p in externals.values()])))
            log = scratch / (label + '.log')
            command = [sys.executable, '-B', str(Path(__file__).resolve()), '_worker',
                       '--source', str(work), '--inputs', str(inputs), '--reads', str(reads)]
            jobs.append((label, command, work, log, output, reads))
    # Fresh processes/snapshots are independent. Collect in fixed seed/repeat
    # order so completion order cannot affect the receipt.
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(execute, command, work, clean_environment(work, scratch, game), log)
                   for _, command, work, log, _, _ in jobs]
        attempts = {seed: [] for seed in ('LF', 'CRLF')}
        for (label, _, _, log, output, reads), future in zip(jobs, futures):
            result = future.result()
            observations.append(dict(stage='generate-' + label, **result))
            if result['exit'] != 0 or result['timed_out']:
                failures.append('Generation failed: ' + label + ': ' + log.read_text(errors='replace')[-2000:])
                continue
            attempts[label.split('-')[0]].append(output.read_bytes())
            read_sets[label] = json.loads(reads.read_bytes())
    if any(len(values) != 2 for values in attempts.values()):
        return {}, read_sets, None
    for seed, values in attempts.items():
        difference = byte_difference(*values)
        if difference:
            failures.append(dict(nondeterministic=seed, difference=difference))
        outputs[seed] = values[0]
    return outputs, read_sets, scratch / 'LF-0'


def gate_commands(scratch):
    return [('python-discovery', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-q']),
            ('strict-verifier', [sys.executable, 'tools/rrt_verify.py', '--strict', '--json', str(scratch / 'verify.json'),
                                 '--text', str(scratch / 'verify.txt')]),
            ('rules-progression', ['dotnet', 'run', '--project', 'tests/RulesTests.csproj', '-c', 'Release', '--',
                                   'development/Story.json'])]


def gates(snapshot, scratch, game, observations):
    env = clean_environment(snapshot, scratch, game)
    env['RRT_TEST_STORY'] = str(snapshot / 'development/Story.json')
    results = []
    for name, command in gate_commands(scratch):
        log = scratch / (name + '.log')
        print('RUN ' + name, flush=True)
        observed = execute(command, snapshot, env, log)
        observations.append(dict(stage=name, **observed))
        text = log.read_text(encoding='utf-8', errors='replace')
        result = dict(stage=name, command=[x.replace(str(scratch), '<temp>').replace(sys.executable, '<python>')
                                          for x in command], exit=observed['exit'], timed_out=observed['timed_out'])
        if name == 'strict-verifier':
            match = re.search(r'HARD FAILURES: (\d+)', text)
            result['hard_failures'] = int(match[1]) if match else None
            report_path = scratch / 'verify.json'
            if report_path.is_file():
                report = json.loads(report_path.read_bytes())
                result['player_text_hard'] = report.get('player_text', {}).get('hard', [])
        result['passed'] = observed['exit'] == 0 and not observed['timed_out']
        if name == 'strict-verifier' and result['hard_failures'] != 0:
            result['passed'] = False
        results.append(result)
        print(name + ': exit=' + str(observed['exit']), flush=True)
    return results


def receipt(evidence, observations):
    return dict(format=FORMAT, identity=digest(canonical(evidence)), evidence=evidence,
                observations=observations)


def load_baseline(path):
    data = json.loads((path / 'receipt.json').read_bytes())
    if data.get('format') != FORMAT or data.get('identity') != digest(canonical(data['evidence'])):
        raise GuardError('Malformed baseline receipt or identity')
    evidence = data['evidence']
    if evidence.get('source_digest') != digest(canonical(evidence.get('source_files'))):
        raise GuardError('Malformed source inventory digest')
    if evidence.get('operation') != 'capture' or not evidence.get('structural_passed'):
        raise GuardError('Baseline is stale/failed/incomplete')
    if [g['stage'] for g in evidence.get('gates', [])] != ['python-discovery', 'strict-verifier', 'rules-progression']:
        raise GuardError('Missing required gate receipts')
    if set(evidence.get('exports', {})) != {'LF', 'CRLF'}:
        raise GuardError('Missing required frozen export')
    for gate in evidence['gates']:
        if (not isinstance(gate.get('command'), list) or not gate['command']
                or type(gate.get('timed_out')) is not bool
                or gate.get('exit') is not None and type(gate['exit']) is not int
                or gate.get('passed') != (gate.get('exit') == 0 and not gate['timed_out'])):
            raise GuardError('Malformed required gate result: ' + gate['stage'])
    if evidence.get('gate_debt') != [g for g in evidence['gates'] if not g['passed']]:
        raise GuardError('Gate debt differs from required results')
    observed = data.get('observations', [])
    required = {'generate-LF-0', 'generate-LF-1', 'generate-CRLF-0', 'generate-CRLF-1',
                'frozen-savecompat', 'python-discovery', 'strict-verifier', 'rules-progression'}
    if {item.get('stage') for item in observed} != required or len(observed) != len(required):
        raise GuardError('Missing/duplicate required execution observations')
    for item in observed:
        try:
            begin = datetime.fromisoformat(item['started'])
            end = datetime.fromisoformat(item['finished'])
            if not begin.tzinfo or not end.tzinfo or end < begin:
                raise ValueError('invalid execution interval')
        except (KeyError, ValueError, TypeError):
            raise GuardError('Malformed execution timestamps: ' + item.get('stage', '?'))
        if not re.fullmatch(r'[0-9a-f]{64}', item.get('log_sha256', '')):
            raise GuardError('Missing execution log digest: ' + item['stage'])
    for gate in evidence['gates']:
        item = next(item for item in observed if item['stage'] == gate['stage'])
        if (item.get('exit'), item.get('timed_out')) != (gate['exit'], gate['timed_out']):
            raise GuardError('Execution observation differs from gate result: ' + gate['stage'])
    for seed, entry in evidence['exports'].items():
        raw = (path / (seed + '-Story.json')).read_bytes()
        if len(raw) != entry['bytes'] or digest(raw) != entry['sha256']:
            raise GuardError('Baseline export corrupted: ' + seed)
    return evidence


def perform(operation, source, out, game, baseline=None, allowed=()):
    source, game = source.resolve(), game.resolve()
    out = temporary_output(out, source)
    if operation == 'capture' and git(source, 'status', '--porcelain'):
        raise GuardError('Capture requires a clean predecessor; dirty source is not blessed')
    old = load_baseline(baseline.resolve()) if baseline else None
    files = source_files(source)
    runtime = runtime_inputs(source)
    native, externals = external_inputs(source, game)
    revision = git(source, 'rev-parse', 'HEAD')
    guard_hash = file_hash(Path(__file__).resolve())
    failures, observations = [], []
    changed = []
    if old:
        if runtime != old['runtime'] or native != old['native_inputs'] or guard_hash != old.get('guard_sha256'):
            failures.append('Pinned runtime/native/parent inputs changed')
        changed, ownership = ownership_failures(old['source_files'], files, set(allowed))
        failures.extend(ownership)
    tracked = (source / 'development/Story.json').read_bytes()
    with tempfile.TemporaryDirectory(prefix='rrt-refactor-') as temporary:
        scratch = Path(temporary)
        outputs, reads, snapshot = generation(source, files, game, externals, scratch, observations, failures)
        evidence = dict(operation=operation, revision=revision, source_files=files,
                        source_digest=digest(canonical(files)), runtime=runtime, native_inputs=native,
                        guard_sha256=guard_hash,
                        changed_sources=changed, authorized_sources=sorted(allowed), generator_reads=reads,
                        tracked_export_sha256=digest(tracked), exports={}, failures=failures)
        if outputs:
            from tools import savecompat
            story = json.loads(outputs['LF'])
            difference = byte_difference(tracked, outputs['CRLF' if b'\r\n' in tracked else 'LF'])
            evidence['tracked_export_stale'] = difference is not None
            if difference:
                failures.append(dict(stale_tracked_export=difference))
            frozen = savecompat.check(story)
            evidence['frozen_savecompat'] = frozen
            failures.extend(frozen)
            inventory = predecessor_inventory(story)
            # Reuse the verifier's existing registration inventory, without an
            # independent runtime name derivation.
            sys.path.insert(0, str(ROOT))
            from tools import rrt_verify
            names, _ = rrt_verify.build_names(rrt_verify.Model(story))
            evidence['registration_sha256'] = digest(canonical(names))
            namespace = re.findall(r'Encoding.UTF8.GetBytes\("([^"]+)" \+ name\)',
                                   (source / 'src/Main.cs').read_text(encoding='utf-8-sig'))
            evidence['guid_namespace'] = namespace
            if namespace != [NAMESPACE]:
                failures.append('GuidFor namespace changed')
            evidence['predecessor_inventory'] = inventory
            evidence['scene_count'] = len(story['Scenes'])
            for seed, raw in outputs.items():
                evidence['exports'][seed] = dict(bytes=len(raw), sha256=digest(raw))
                if old:
                    diff = byte_difference((baseline / (seed + '-Story.json')).read_bytes(), raw)
                    if diff:
                        failures.append(dict(export=seed, difference=diff,
                                             action='ESCALATE; preserve predecessor order/adapter'))
            if old:
                if old['predecessor_inventory'] != inventory:
                    failures.append('Predecessor scene/node/relationship/choice identities or targets changed: ' +
                                    first_difference(old['predecessor_inventory'], inventory))
                if old['registration_sha256'] != evidence['registration_sha256']:
                    failures.append('Registration-name inventory changed')
            # Candidate and baseline use the same unmodified released inventory.
            command = [sys.executable, 'tools/savecompat.py', '--story', 'development/Story.json']
            observed = execute(command, snapshot, clean_environment(snapshot, scratch, game), scratch / 'savecompat.log')
            observations.append(dict(stage='frozen-savecompat', **observed))
            if observed['exit'] != 0 or observed['timed_out']:
                failures.append('Frozen savecompat CLI failed')
            evidence['gates'] = gates(snapshot, scratch, game, observations)
            if (snapshot / 'development/Story.json').read_bytes() != outputs['LF']:
                failures.append('Frozen gate export changed during checks')
        else:
            evidence['gates'] = []
        if source_files(source) != files or git(source, 'rev-parse', 'HEAD') != revision:
            failures.append('Source changed during guard execution')
        if external_inputs(source, game)[0] != native:
            failures.append('Native inputs changed during guard execution')
        if file_hash(Path(__file__).resolve()) != guard_hash:
            failures.append('Guard implementation changed during execution')
        evidence['structural_passed'] = not failures
        evidence['gate_passed'] = bool(evidence['gates']) and all(g['passed'] for g in evidence['gates'])
        evidence['gate_debt'] = [g for g in evidence['gates'] if not g['passed']]
        evidence['accepted'] = evidence['structural_passed'] and evidence['gate_passed']
        if old:
            evidence['baseline_identity'] = digest(canonical(old))
            evidence['predecessor_gate_debt'] = old['gate_debt']
        result = receipt(evidence, observations)
        out.mkdir(parents=True)
        for seed, raw in outputs.items():
            (out / (seed + '-Story.json')).write_bytes(raw)
        (out / 'receipt.json').write_bytes(canonical(result))
        # Logs/reports are retained only in this explicitly requested result
        # bundle. Private source snapshots/build/cache trees are always removed.
        for log in scratch.glob('*.log'):
            shutil.copyfile(log, out / log.name)
        if (scratch / 'verify.json').is_file():
            shutil.copyfile(scratch / 'verify.json', out / 'verify.json')
        print(json.dumps(dict(receipt=str(out / 'receipt.json'), identity=result['identity'],
                              structural_passed=evidence['structural_passed'],
                              gate_passed=evidence['gate_passed'], accepted=evidence['accepted'])))
        # Capture may preserve an honest baseline with existing gate debt, but
        # both commands return failure while any mandatory gate is red.
        return 0 if evidence['accepted'] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='operation', required=True)
    for name in ('capture', 'check'):
        command = sub.add_parser(name)
        command.add_argument('--source', type=Path, required=True)
        command.add_argument('--out', type=Path, required=True)
        command.add_argument('--game', type=Path, default=Path(os.environ.get('RRT_GAME_DIR', '/wrath')))
        if name == 'check':
            command.add_argument('--baseline', type=Path, required=True)
            command.add_argument('--allow-source', action='append', default=[], metavar='EXACT_CODE_PATH')
    command = sub.add_parser('_worker', help=argparse.SUPPRESS)
    command.add_argument('--source', type=Path, required=True)
    command.add_argument('--inputs', type=Path, required=True)
    command.add_argument('--reads', type=Path, required=True)
    args = parser.parse_args()
    if args.operation == '_worker':
        # Open private audit output before enforcing generator I/O policy.
        with args.reads.open('wb') as stream:
            inputs = json.loads(args.inputs.read_bytes())
            inputs['reads_fd'] = stream.fileno()
            args.inputs.write_bytes(canonical(inputs))
            worker(args.source.resolve(), args.inputs, args.reads)
        return 0
    try:
        return perform(args.operation, args.source, args.out, args.game,
                       getattr(args, 'baseline', None), getattr(args, 'allow_source', ()))
    except (GuardError, OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print('REFACTOR GUARD FAIL: ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
