"""S0 byte-preserving guard. Baselines and results must live in system temp.

capture --source CLEAN_PREDECESSOR --out BASELINE [--game GAME]
check --baseline BASELINE --source CANDIDATE --out RESULTS
      [--allow-source EXACT_CODE_PATH ...]

No acceptance override or baseline refresh exists. Existing gate debt is evidence,
never permission to accept a failing candidate. S0 freezes the default expansion;
Use --gate-profile arch-s1 for the S1 command/serialization slice: base and
both Tirabade profiles, with only its named Python and voice-lock gates.
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
import sysconfig
import tempfile
import time

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
REQUIRED_GATES = ('python-discovery', 'strict-verifier', 'rules-progression')
S1_GATES = ('python-targeted', 'voice-lock')


def required_gates(profile):
    return S1_GATES if profile == 'arch-s1' else REQUIRED_GATES


def ownership_reference(source):
    # Reuse the voice authority's exact ref preference; never substitute HEAD
    # for the coordinator's independent reviewed ownership context.
    from tools.voice_authority import reviewed_revision
    revision = reviewed_revision(source)
    refs = git(source, 'for-each-ref', '--format=%(refname)').splitlines()
    ref = next(name for name in ('refs/rrt/ownership-reviewed',
                                'refs/remotes/origin/claude/trickster-expansion') if name in refs)
    return dict(ref=ref, revision=revision)


def host_environment():
    # Keep interpreter/build discovery, not arbitrary inherited generator knobs.
    keys = ('PATH', 'HOME', 'USERPROFILE', 'SYSTEMROOT', 'WINDIR', 'COMSPEC',
            'PATHEXT', 'DOTNET_ROOT', 'LD_LIBRARY_PATH', 'SSL_CERT_FILE', 'SSL_CERT_DIR')
    return {key: os.environ[key] for key in keys if key in os.environ}


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
    """Pin tracked files and ignored inputs, excluding explicit output caches.

    A new contract, discovered row or ignored Python module must not silently
    escape the inventory. Only known outputs/build caches are excluded.
    """
    names = set(git(source, 'ls-files', '-z', '--cached', '--others',
                    '--exclude-standard').split('\0')) - {''}
    excluded_dirs = {'tools/.store', 'tools/scratch', 'reference/asset-extraction-env',
                     'harness/.runs', 'harness/probes', 'backups', 'dist'}
    for directory, dirs, entries in os.walk(source):
        parent = Path(directory).relative_to(source)
        dirs[:] = [name for name in dirs if name not in {'.git', '__pycache__', 'obj', 'bin'}
                   and (parent / name).as_posix() not in excluded_dirs]
        for name in dirs:
            if (Path(directory) / name).is_symlink():
                raise GuardError('Unpinned symlink input directory: ' + (parent / name).as_posix())
        for name in entries:
            if not name.endswith(('.pyc', '.log')):
                names.add((parent / name).as_posix())
    result = {}
    for name in sorted(names - EXPORTS):
        path = source / name
        if any(part in {'.git', '__pycache__', 'obj', 'bin'} for part in Path(name).parts):
            continue
        if (name.startswith('tools/rrt_verify_report.') or name.endswith(('.pyc', '.log'))
                or any(name.startswith(area + '/') for area in excluded_dirs)
                or name.startswith('package/') and Path(name).suffix in {'.dll', '.exe', '.config'}):
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


def runtime_inputs(source, gate_profile='s0'):
    script = (source / 'build-expansion.ps1').read_text(encoding='utf-8-sig')
    block = script.split('$env:RRT_PARENT_BINDINGS = (@(', 1)[1].split(')', 1)[0]
    declared = tuple(re.findall(r"'(reference/[^']+\.json)'", block))
    if declared != PARENTS:
        raise GuardError('Build-script parent order changed: ' + repr(declared))
    # Python source, bytecode and extensions are executable inputs too. Third-
    # party packages are excluded and the worker refuses reads from them.
    library = Path(sysconfig.get_path('stdlib')).resolve()
    libraries = {}
    for directory, dirs, names in os.walk(library):
        dirs[:] = sorted(set(dirs) - {'site-packages', 'dist-packages'})
        for name in sorted(names):
            p = Path(directory) / name
            if p.suffix in {'.py', '.pyc', '.so', '.pyd', '.dll'}:
                libraries[p.relative_to(library).as_posix()] = file_hash(p)
    result = dict(python=sys.version, python_executable_sha256=file_hash(Path(sys.executable)),
                python_library_digest=digest(canonical(libraries)),
                dotnet=subprocess.check_output(['dotnet', '--version']).decode().strip(),
                dotnet_executable_sha256=file_hash(Path(shutil.which('dotnet')).resolve()),
                host_environment_sha256=digest(canonical(host_environment())),
                platform=sys.platform, parent_order=[p for p in PARENTS if (source / p).is_file()],
                profile='default-expansion/independent_tirabade=True',
                generator_site='disabled (-S); stdlib and pinned source only',
                hashseed='0', utf8='1', destination_seeds=['LF', 'CRLF'],
                serializer='expansion.py CLI; raw bytes; no normalization',
                required_suites=list(required_gates(gate_profile)), timeout_seconds=TIMEOUT,
                gate_profile=gate_profile)
    if gate_profile == 'arch-s1':
        result['ownership_reference'] = ownership_reference(source)
    return result


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
    env = host_environment()
    env.update(PYTHONHASHSEED='0', PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               RRT_ROOT=str(snapshot), RRT_GAME_DIR=str(game), RRT_PYTHON=sys.executable,
               RRT_PARENT_BINDINGS=os.pathsep.join(str(snapshot / p) for p in PARENTS
                                                  if (snapshot / p).is_file()),
               RRT_TEST_BUILD_ROOT=str(scratch / 'rules-build'),
               RRT_TEST_TIMINGS=str(scratch / 'rules-times.json'),
               RRT_NATIVE_COVERAGE_OUTPUT=str(scratch / 'native-coverage.json'),
               TMPDIR=str(scratch), TMP=str(scratch), TEMP=str(scratch),
               GIT_OPTIONAL_LOCKS='0', LC_ALL='C.UTF-8', TZ='UTC',
               DOTNET_CLI_TELEMETRY_OPTOUT='1', DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1')
    return env


def execute(command, cwd, env, log, timeout=TIMEOUT):
    """Bound a tree in a private supervisor, including detached Linux children.

    Writer's H2 job executor requires a coordinator-owned immutable JobSpec and
    launch grant. This standalone CLI has no such adapter; do not synthesize a
    grant or import its mutable job state. Keep execution private to the guard.
    """
    started = datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory(prefix='rrt-supervisor-', dir=log.parent) as temporary:
        config = Path(temporary) / 'command.json'
        status = Path(temporary) / 'status.json'
        config.write_bytes(canonical(dict(command=command, cwd=str(cwd), env=env,
                                         log=str(log), timeout=timeout)))
        supervisor = subprocess.Popen([sys.executable, '-S', '-B', str(Path(__file__).resolve()),
                                       '_supervise', '--config', str(config), '--status', str(status)],
                                      env=env, start_new_session=True,
                                      stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        try:
            _, error = supervisor.communicate(timeout=timeout + 10)
        except subprocess.TimeoutExpired:
            os.killpg(supervisor.pid, signal.SIGTERM)
            try:
                _, error = supervisor.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(supervisor.pid, signal.SIGKILL)
                _, error = supervisor.communicate()
        if supervisor.returncode != 0 or not status.is_file():
            # Unsupported supervision fails closed; never silently use a
            # process-group-only fallback that can strand setsid descendants.
            log.write_bytes(error or b'Whole-process-tree supervisor failed\n')
            result = dict(exit=126, timed_out=False)
        else:
            result = json.loads(status.read_bytes())
    return dict(**result, started=started, finished=datetime.now(timezone.utc).isoformat(),
                log_sha256=file_hash(log))


def supervise(config, status):
    if sys.platform != 'linux':
        raise GuardError('Whole-process-tree supervision requires Linux')
    import ctypes
    # A separate subreaper owns one command tree. This also keeps concurrent
    # attempts from reaping one another's children.
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0):
        raise GuardError('Linux subreaper unavailable')
    cancelled = [False]
    for signum in (signal.SIGTERM, signal.SIGINT):
        signal.signal(signum, lambda *_: cancelled.__setitem__(0, True))
    spec = json.loads(config.read_bytes())
    timed_out = False
    with Path(spec['log']).open('wb') as output:
        process = subprocess.Popen(spec['command'], cwd=spec['cwd'], env=spec['env'], stdout=output,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        deadline = time.monotonic() + spec['timeout']
        try:
            while process.poll() is None and not cancelled[0] and time.monotonic() < deadline:
                time.sleep(0.02)
            timed_out = process.poll() is None
            code = None if timed_out else process.returncode
        finally:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.kill() if process.poll() is None else None
            process.wait()
            # Detached or double-forked children are adopted by this supervisor
            # as their parents die. Kill/reap successive generations to empty.
            children_path = Path('/proc/self/task/%d/children' % os.getpid())
            cleanup_deadline = time.monotonic() + 3
            unfinished = False
            while True:
                children = [int(p) for p in children_path.read_text(encoding='utf-8').split()]
                if not children:
                    break
                unfinished = True
                for child in children:
                    try:
                        os.kill(child, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                while True:
                    try:
                        pid, _ = os.waitpid(-1, os.WNOHANG)
                    except ChildProcessError:
                        break
                    if not pid:
                        break
                if time.monotonic() >= cleanup_deadline:
                    raise GuardError('Could not verify descendant cleanup')
                time.sleep(0.01)
            if unfinished and code == 0:
                code = 125
                output.write(b'Unfinished command descendants were terminated; stage failed\n')
    status.write_bytes(canonical(dict(exit=code, timed_out=timed_out)))


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


def snapshot_source(source, target, files, ownership=None):
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
    (metadata / 'objects/info/alternates').write_text(str(common.resolve() / 'objects') + '\n', encoding='utf-8')
    (metadata / 'refs').mkdir()
    if ownership:
        ref = metadata / ownership['ref']
        ref.parent.mkdir(parents=True, exist_ok=True)
        ref.write_text(ownership['revision'] + '\n', encoding='utf-8')
    (metadata / 'HEAD').write_text(git(source, 'rev-parse', 'HEAD') + '\n', encoding='utf-8')
    (metadata / 'config').write_text('[core]\n\trepositoryformatversion = 0\n\tbare = false\n', encoding='utf-8')
    subprocess.run(['git', '-C', str(target), 'read-tree', 'HEAD'], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def worker(snapshot, inputs_path, reads_path):
    """Run the real CLI, auditing data reads after interpreter startup."""
    import runpy
    inputs = json.loads(inputs_path.read_text(encoding='utf-8'))
    allowed = set(inputs['files'])
    external = {str(Path(p).resolve()): name for name, p in inputs['external'].items()}
    library = Path(sysconfig.get_path('stdlib')).resolve()
    reads = set()
    violations = []
    destination = inputs.get('destination', 'development/Story.json')

    def reject(message):
        violations.append(message)
        raise GuardError(message)

    def audit(event, args):
        if event in {'subprocess.Popen', 'os.system', 'os.exec', 'os.posix_spawn',
                     'os.fork', 'socket.__new__', 'ctypes.dlopen'}:
            reject('Generator attempted unaccounted execution: ' + event)
        if event in {'os.remove', 'os.rename', 'os.rmdir', 'os.symlink', 'os.link',
                     'os.chmod', 'os.truncate', 'os.utime'}:
            reject('Generator attempted unaccounted filesystem mutation: ' + event)
        if event == 'os.mkdir' and Path(os.fsdecode(args[0])).resolve() != (snapshot / destination).parent:
            reject('Generator created unaccounted directory: ' + str(args[0]))
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
                if name != destination:
                    reject('Generator wrote unaccounted output: ' + name)
            elif name not in allowed and name != destination:
                reject('Generator read unaccounted input: ' + name)
            elif name in allowed:
                reads.add(name)
        elif str(path) in external:
            if writing:
                reject('Generator wrote external input: ' + str(path))
            reads.add('external:' + external[str(path)])
        elif (writing or not path.is_relative_to(library)
              or {'site-packages', 'dist-packages'} & set(path.parts)
              or path.suffix not in {'.py', '.pyc', '.so', '.pyd', '.dll'}):
            reject('Generator read unaccounted external input: ' + str(path))

    sys.addaudithook(audit)
    sys.path[:] = [str(snapshot)] + [p for p in sys.path if p and Path(p).resolve().is_relative_to(library)]
    os.chdir(snapshot)
    profile = inputs.get('profile', 'default')
    sys.argv = ['story.py' if profile == 'base' else 'expansion.py']
    try:
        if profile == 'joint':
            # The legacy CLI has no false-mode switch. Freeze its factory with
            # the same historical expansion serialization, in a fresh process.
            output = snapshot / destination
            if 'authoring/compiler.py' in allowed:
                from authoring.compiler import CompilationInputs, compile_story
                from authoring._serialization import write_story
                compiled = compile_story('expansion', CompilationInputs(output), independent_tirabade=False)
                write_story(output, compiled)
                if output.read_bytes() != compiled.export_bytes:
                    reject('Compiler bytes differ from the joint destination write')
            else:
                from expansion import make_expansion
                payload = make_expansion(independent_tirabade=False)
                newline = '\r\n' if output.exists() and b'\r\n' in output.read_bytes() else '\n'
                output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n',
                                  encoding='utf-8', newline=newline)
        else:
            command = runpy.run_path(str(snapshot / sys.argv[0]), run_name='__main__')
            if 'compiled' in command and (snapshot / destination).read_bytes() != command['compiled'].export_bytes:
                reject('Compiler bytes differ from the CLI destination write')
        if violations:
            raise GuardError('Generator caught an input-policy violation: ' + violations[0])
    finally:
        # This output is outside the audited source; write through a descriptor
        # opened before installing the audit hook by the command entry point.
        os.write(inputs['reads_fd'], canonical(sorted(reads)))


def generation(source, files, game, externals, scratch, observations, failures, profile='default', ownership=None):
    outputs = {}
    read_sets = {}
    jobs = []
    for seed in ('LF', 'CRLF'):
        for repeat in range(2):
            label = '%s-%d' % (seed, repeat)
            work = scratch / label
            snapshot_source(source, work, files, ownership)
            destination = 'package/Story.json' if profile == 'base' else 'development/Story.json'
            output = work / destination
            output.parent.mkdir(exist_ok=True)
            output.write_bytes(b'\r\n' if seed == 'CRLF' else b'\n')
            inputs = scratch / (label + '-inputs.json')
            reads = scratch / (label + '-reads.json')
            inputs.write_bytes(canonical(dict(files=files, profile=profile, destination=destination,
                                             external={name: str(p.resolve())
                                                                    for name, p in externals.items()})))
            log = scratch / (label + '.log')
            command = [sys.executable, '-S', '-B', str(Path(__file__).resolve()), '_worker',
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
            prefix = '' if profile == 'default' else profile + '-'
            observations.append(dict(stage='generate-' + prefix + label, **result))
            if result['exit'] != 0 or result['timed_out']:
                diagnostic = log.read_text(errors='replace', encoding='utf-8')[-2000:].replace(str(scratch), '<temp>')
                failures.append('Generation failed: ' + prefix + label + ': ' + diagnostic)
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


def gate_commands(scratch, gate_profile='s0'):
    if gate_profile == 'arch-s1':
        return [('python-targeted', [sys.executable, '-m', 'unittest', 'tests.test_refactor_guard',
                                    'tests.test_savecompat_baseline', 'tests.test_utf8_io', '-q']),
                ('voice-lock', [sys.executable, 'tools/voice_lock_lint.py', '--strict'])]
    return [('python-discovery', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-q']),
            ('strict-verifier', [sys.executable, 'tools/rrt_verify.py', '--strict', '--json', str(scratch / 'verify.json'),
                                 '--text', str(scratch / 'verify.txt')]),
            ('rules-progression', ['dotnet', 'run', '--project', 'tests/RulesTests.csproj', '-c', 'Release', '--',
                                   'development/Story.json'])]


def recorded_command(command, scratch):
    return [word.replace(str(scratch), '<temp>').replace(sys.executable, '<python>') for word in command]


def gates(snapshot, scratch, game, observations, gate_profile='s0'):
    env = clean_environment(snapshot, scratch, game)
    env['RRT_TEST_STORY'] = str(snapshot / 'development/Story.json')
    results = []
    for name, command in gate_commands(scratch, gate_profile):
        log = scratch / (name + '.log')
        print('RUN ' + name, flush=True)
        observed = execute(command, snapshot, env, log)
        observations.append(dict(stage=name, **observed))
        text = log.read_text(encoding='utf-8', errors='replace')
        result = dict(stage=name, command=recorded_command(command, scratch),
                      exit=observed['exit'], timed_out=observed['timed_out'])
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
    try:
        return validate_baseline(path)
    except (KeyError, TypeError, AttributeError, ValueError) as error:
        raise GuardError('Malformed baseline receipt: ' + str(error)) from error


def validate_baseline(path):
    data = json.loads((path / 'receipt.json').read_bytes())
    if (type(data.get('format')) is not int or data['format'] != FORMAT
            or data.get('identity') != digest(canonical(data['evidence']))):
        raise GuardError('Malformed baseline receipt or identity')
    evidence = data['evidence']
    gate_profile = evidence.get('runtime', {}).get('gate_profile', 's0')
    if gate_profile not in ('s0', 'arch-s1'):
        raise GuardError('Unknown pinned gate profile')
    required_suites = required_gates(gate_profile)
    if (any(type(evidence.get(key)) is not bool for key in
            ('structural_passed', 'gate_passed', 'accepted', 'tracked_export_stale'))
            or type(evidence.get('scene_count')) is not int or evidence['scene_count'] < 0
            or not isinstance(evidence.get('revision'), str)
            or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', evidence['revision'])
            or evidence.get('changed_sources') != [] or evidence.get('authorized_sources') != []):
        raise GuardError('Malformed capture status, count, revision or ownership scope')
    if evidence.get('source_digest') != digest(canonical(evidence.get('source_files'))):
        raise GuardError('Malformed source inventory digest')
    if evidence.get('operation') != 'capture' or not evidence.get('structural_passed'):
        raise GuardError('Baseline is stale/failed/incomplete')
    if [g['stage'] for g in evidence.get('gates', [])] != list(required_suites):
        raise GuardError('Missing required gate receipts')
    if set(evidence.get('exports', {})) != {'LF', 'CRLF'}:
        raise GuardError('Missing required frozen export')
    for gate in evidence['gates']:
        expected = dict(gate_commands(Path('<temp>'), gate_profile))[gate['stage']]
        if (not isinstance(gate.get('command'), list) or not gate['command']
                or gate['command'] != recorded_command(expected, Path('<temp>'))
                or type(gate.get('timed_out')) is not bool
                or gate.get('exit') is not None and type(gate['exit']) is not int
                or type(gate.get('passed')) is not bool
                or gate.get('passed') != (gate.get('exit') == 0 and not gate['timed_out']
                    and (gate['stage'] != 'strict-verifier' or gate.get('hard_failures') == 0))):
            raise GuardError('Malformed required gate result: ' + gate['stage'])
    if canonical(evidence.get('gate_debt')) != canonical([g for g in evidence['gates'] if not g['passed']]):
        raise GuardError('Gate debt differs from required results')
    observed = data.get('observations', [])
    required = {'generate-LF-0', 'generate-LF-1', 'generate-CRLF-0', 'generate-CRLF-1',
                'frozen-savecompat', *required_suites}
    if gate_profile == 'arch-s1':
        required.update('generate-' + profile + '-' + seed + '-' + str(repeat)
                        for profile in ('base', 'joint') for seed in ('LF', 'CRLF') for repeat in range(2))
    if {item.get('stage') for item in observed} != required or len(observed) != len(required):
        raise GuardError('Missing/duplicate required execution observations')
    for item in observed:
        if (type(item.get('timed_out')) is not bool
                or item.get('exit') is not None and type(item['exit']) is not int):
            raise GuardError('Malformed execution status: ' + item['stage'])
        if item['stage'] not in required_suites and (item['exit'] != 0 or item['timed_out']):
            raise GuardError('Failed required structural execution: ' + item['stage'])
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
    if (evidence['failures'] != [] or evidence['tracked_export_stale']
            or evidence['frozen_savecompat'] != [] or evidence['guid_namespace'] != [NAMESPACE]
            or evidence['gate_passed'] != all(g['passed'] for g in evidence['gates'])
            or evidence['accepted'] != evidence['gate_passed']):
        raise GuardError('Inconsistent acceptance/structural evidence')
    if evidence['tracked_export_sha256'] not in {entry['sha256'] for entry in evidence['exports'].values()}:
        raise GuardError('Tracked export does not match a frozen newline profile')
    from tools import savecompat
    if (evidence['frozen_baseline_revision'] != savecompat.BASELINE_REVISION
            or evidence['frozen_baseline_sha256'] != evidence['source_files']['tools/savecompat_baseline.json']['sha256']):
        raise GuardError('Missing or inconsistent released savecompat pin')
    for seed, entry in evidence['exports'].items():
        raw = (path / (seed + '-Story.json')).read_bytes()
        if type(entry['bytes']) is not int or len(raw) != entry['bytes'] or digest(raw) != entry['sha256']:
            raise GuardError('Baseline export corrupted: ' + seed)
        story = json.loads(raw)
        if (len(story['Scenes']) != evidence['scene_count']
                or canonical(predecessor_inventory(story)) != canonical(evidence['predecessor_inventory'])):
            raise GuardError('Frozen export differs from predecessor inventory: ' + seed)
    for name, entry in evidence['source_files'].items():
        if (Path(name).is_absolute() or '..' in Path(name).parts
                or type(entry['bytes']) is not int or entry['bytes'] < 0
                or type(entry['executable']) is not bool
                or not re.fullmatch(r'[0-9a-f]{64}', entry['sha256'])):
            raise GuardError('Malformed source inventory entry: ' + name)
    if not {'expansion.py', 'src/Main.cs', 'tools/savecompat.py',
            'tools/savecompat_baseline.json', 'build-expansion.ps1'} <= evidence['source_files'].keys():
        raise GuardError('Missing required pinned source inputs')
    if not evidence['native_inputs'] or evidence['runtime']['required_suites'] != list(required_suites):
        raise GuardError('Missing pinned native/runtime inputs')
    for name, entry in evidence['native_inputs'].items():
        if (type(entry['bytes']) is not int or entry['bytes'] < 0
                or not re.fullmatch(r'[0-9a-f]{64}', entry['sha256'])):
            raise GuardError('Malformed native input hash: ' + name)
    runtime_keys = {'python', 'python_executable_sha256', 'python_library_digest', 'dotnet',
                    'dotnet_executable_sha256', 'host_environment_sha256', 'platform', 'parent_order',
                    'profile', 'generator_site', 'hashseed', 'utf8', 'destination_seeds', 'serializer',
                    'required_suites', 'timeout_seconds'}
    if not runtime_keys <= evidence['runtime'].keys():
        raise GuardError('Incomplete pinned runtime inputs')
    if set(evidence['generator_reads']) != {'LF-0', 'LF-1', 'CRLF-0', 'CRLF-1'}:
        raise GuardError('Missing required generator read inventory')
    for reads in evidence['generator_reads'].values():
        if (not isinstance(reads, list) or reads != sorted(set(reads))
                or any(name not in evidence['source_files'] and
                       (not name.startswith('external:') or name[9:] not in evidence['native_inputs'])
                       for name in reads)):
            raise GuardError('Unaccounted frozen generator read')
    if gate_profile == 'arch-s1':
        ownership = evidence['runtime'].get('ownership_reference', {})
        if (ownership.get('ref') not in ('refs/rrt/ownership-reviewed', 'refs/remotes/origin/claude/trickster-expansion')
                or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', ownership.get('revision', ''))):
            raise GuardError('Missing pinned reviewed ownership context')
        profiles = evidence.get('profiles', {})
        if set(profiles) != {'base', 'joint'}:
            raise GuardError('Missing required S1 profile')
        for profile, entry in profiles.items():
            if set(entry.get('exports', {})) != {'LF', 'CRLF'}:
                raise GuardError('Missing required profile newline export: ' + profile)
            if set(entry.get('reads', {})) != {'LF-0', 'LF-1', 'CRLF-0', 'CRLF-1'}:
                raise GuardError('Missing required profile read inventory: ' + profile)
            for reads in entry['reads'].values():
                if (not isinstance(reads, list) or reads != sorted(set(reads))
                        or any(name not in evidence['source_files'] and
                               (not name.startswith('external:') or name[9:] not in evidence['native_inputs'])
                               for name in reads)):
                    raise GuardError('Unaccounted profile generator read: ' + profile)
            for seed, export in entry['exports'].items():
                raw = (path / (profile + '-' + seed + '-Story.json')).read_bytes()
                if (type(export.get('bytes')) is not int or len(raw) != export['bytes']
                        or digest(raw) != export['sha256']):
                    raise GuardError('Baseline profile export corrupted: ' + profile + '-' + seed)
                if predecessor_inventory(json.loads(raw)) != entry.get('predecessor_inventory'):
                    raise GuardError('Profile predecessor inventory differs: ' + profile)
    return evidence


def perform(operation, source, out, game, baseline=None, allowed=(), gate_profile='s0'):
    source, game = source.resolve(), game.resolve()
    out = temporary_output(out, source)
    if operation == 'capture' and git(source, 'status', '--porcelain'):
        raise GuardError('Capture requires a clean predecessor; dirty source is not blessed')
    old = load_baseline(baseline.resolve()) if baseline else None
    files = source_files(source)
    runtime = runtime_inputs(source) if gate_profile == 's0' else runtime_inputs(source, gate_profile)
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
    if old and digest(tracked) != old['tracked_export_sha256']:
        failures.append('Tracked export bytes/newline seed differ from predecessor')
    with tempfile.TemporaryDirectory(prefix='rrt-refactor-') as temporary:
        scratch = Path(temporary)
        outputs, reads, snapshot = generation(source, files, game, externals, scratch, observations, failures,
                                             ownership=runtime.get('ownership_reference'))
        profile_outputs = {}
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
            # The frozen inventory belongs to the captured revision, rather than
            # whichever checkout happens to be hosting this guard invocation.
            frozen = savecompat.check(story, json.loads((source / 'tools/savecompat_baseline.json').read_bytes()))
            evidence['frozen_baseline_revision'] = savecompat.BASELINE_REVISION
            evidence['frozen_baseline_sha256'] = files['tools/savecompat_baseline.json']['sha256']
            if evidence['frozen_baseline_sha256'] != file_hash(savecompat.BASELINE_PATH):
                failures.append('Released savecompat baseline differs from the guard checkout')
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
            if gate_profile == 'arch-s1':
                evidence['profiles'] = {}
                for profile in ('base', 'joint'):
                    profile_scratch = scratch / profile
                    profile_scratch.mkdir()
                    raw_exports, profile_reads, _ = generation(source, files, game, externals,
                        profile_scratch, observations, failures, profile=profile,
                        ownership=runtime.get('ownership_reference'))
                    profile_outputs[profile] = raw_exports
                    if not raw_exports:
                        continue
                    profile_story = json.loads(raw_exports['LF'])
                    profile_inventory = predecessor_inventory(profile_story)
                    entry = dict(exports={seed: dict(bytes=len(raw), sha256=digest(raw))
                                          for seed, raw in raw_exports.items()},
                                 reads=profile_reads, predecessor_inventory=profile_inventory)
                    evidence['profiles'][profile] = entry
                    if old:
                        for seed, raw in raw_exports.items():
                            diff = byte_difference((baseline / (profile + '-' + seed + '-Story.json')).read_bytes(), raw)
                            if diff:
                                failures.append(dict(export=profile + '-' + seed, difference=diff))
                        if old['profiles'][profile]['predecessor_inventory'] != profile_inventory:
                            failures.append('Profile predecessor identities or targets changed: ' + profile)
                        # Use the exact predecessor's full profile inventory.
                        predecessor = json.loads((baseline / (profile + '-LF-Story.json')).read_bytes())
                        profile_failures = savecompat.check(profile_story, savecompat.inventory(predecessor))
                        failures.extend(profile + ': ' + failure for failure in profile_failures)
                evidence['gates'] = gates(snapshot, scratch, game, observations, gate_profile)
            else:
                evidence['gates'] = gates(snapshot, scratch, game, observations)
            if (snapshot / 'development/Story.json').read_bytes() != outputs['LF']:
                failures.append('Frozen gate export changed during checks')
        else:
            evidence['gates'] = []
        if source_files(source) != files or git(source, 'rev-parse', 'HEAD') != revision:
            failures.append('Source changed during guard execution')
        if (source / 'development/Story.json').read_bytes() != tracked:
            failures.append('Tracked export changed during guard execution')
        final_runtime = runtime_inputs(source) if gate_profile == 's0' else runtime_inputs(source, gate_profile)
        if final_runtime != runtime:
            failures.append('Runtime inputs changed during guard execution')
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
        for profile, exports in profile_outputs.items():
            for seed, raw in exports.items():
                (out / (profile + '-' + seed + '-Story.json')).write_bytes(raw)
        (out / 'receipt.json').write_bytes(canonical(result))
        # Logs/reports are retained only in this explicitly requested result
        # bundle. Private source snapshots/build/cache trees are always removed.
        for log in scratch.rglob('*.log'):
            shutil.copyfile(log, out / '-'.join(log.relative_to(scratch).parts))
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
        command.add_argument('--gate-profile', choices=('s0', 'arch-s1'), default='s0')
        if name == 'check':
            command.add_argument('--baseline', type=Path, required=True)
            command.add_argument('--allow-source', action='append', default=[], metavar='EXACT_CODE_PATH')
    command = sub.add_parser('_worker', help=argparse.SUPPRESS)
    command.add_argument('--source', type=Path, required=True)
    command.add_argument('--inputs', type=Path, required=True)
    command.add_argument('--reads', type=Path, required=True)
    command = sub.add_parser('_supervise', help=argparse.SUPPRESS)
    command.add_argument('--config', type=Path, required=True)
    command.add_argument('--status', type=Path, required=True)
    args = parser.parse_args()
    if args.operation == '_supervise':
        supervise(args.config, args.status)
        return 0
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
                       getattr(args, 'baseline', None), getattr(args, 'allow_source', ()), args.gate_profile)
    except (GuardError, OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print('REFACTOR GUARD FAIL: ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
