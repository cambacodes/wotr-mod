"""Conservative dependency selection for the per-round rules/Python gate."""
from pathlib import Path
import ast
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ROUTES = {
    'aivu', 'anevia', 'aranka', 'areelu', 'arsinoe', 'arueshalae', 'camellia',
    'chadali', 'chivarro', 'delamere', 'devarra', 'dorgelinda', 'eliandra',
    'elyanka', 'ember', 'eritrice', 'galfrey', 'gesmerha', 'hepzamirah', 'herrax',
    'horzalah', 'iomedae', 'irabeth', 'jannah', 'jerribeth', 'kaylessa', 'kiana',
    'konomi', 'melazmera', 'mielarah', 'minagho', 'minagho_chivarro', 'nenio',
    'nidalynn', 'nocticula', 'nurah', 'seelah', 'shamira', 'soana', 'targona',
    'terendelev', 'tirabade', 'vellexia', 'wenduag', 'yaniel',
}
# One source scan replaces one full-file regex search per route.
FLAG_ROUTES = re.compile(r'["\'](' + '|'.join(sorted(ROUTES)) + r')(?=[."\'])')
FILE_ROUTES = {r: re.compile(r'(?i)(?<![a-z])' + re.escape(r)) for r in ROUTES}

SHARED_STORIES = {'household', 'lastcall', 'longcon', 'trickster_world',
                  'scene_kinds', 'foresight', 'nm1_fold', 'earned_presence'}
# Exhaustive campaign interleavings remain in FULL. FAST always runs the small
# engine fixtures and the integrated inventories below, then the directly
# touched route suites. This list is a tier boundary, never a test retirement.
FAST_INVENTORIES = {
    'LatestStateInventoryTests', 'ImplicitParticipantInventoryTests',
    'NativeEndingInventory2Tests', 'NativeGateContractParityTests',
    'NativeWorldReconciliationInventoryTests', 'NativeContradictionInventoryTests',
    'NativeVariantCoverageInventoryTests', 'EngineF6cNativeTests',
    'TerendelevNativeDependencyTests', 'KianaNativeReconciliationTests',
    'NativeAnswerEditsTests', 'PresenceRuntimeF9Tests', 'PresenceTransitionInventoryTests',
    'PresenceBootstrapInventoryTests', 'Inventory2WalkerMutationTests',
    'GameplayEntryInventoryTests', 'EarnedPresenceTests', 'LeftTricksterConsumerTests',
    'EarnedOutcomeInventoryTests', 'ParticipantInventoryTests', 'WenduagEchoRulesTests',
    'LastCallHistoryInventoryTests', 'NativeFactInventoryTests',
    'EngineQ5Tests', 'ContactInventoryOracleTests', 'ReturnProvenanceInventoryTests',
    'PresenceFailureReceiptTests', 'LocationInventoryTests', 'WorldFactInventoryTests',
}
FAST_PYTHON = {
    'test_return_safety', 'test_gate_lint', 'test_rrt_validate', 'test_crossroute_lint',
    'test_etude_lifecycle', 'test_chapter_zero', 'test_harem_engine',
    'test_presence_dependency_lint', 'test_native_world_reconciliation',
    'test_draft_contract_lint', 'test_earned_presence', 'test_player_text_lint',
    'test_text_structure_lint', 'test_parent_bindings', 'test_test_selection', 'test_verifier_tiers',
    'test_foresight_echo',
    'test_test_gate', 'test_harness_evidence',
    'test_voice_authority', 'test_voice_lock_lint', 'test_prose_integration',
}


def mentioned_routes(path):
    # Over-selecting cross-route assertions is intentional. Literal flags and
    # suite names both contribute; no unrecognized file gets an empty gate.
    text = path.read_text(encoding='utf-8-sig')
    names = set(FLAG_ROUTES.findall(text))
    names.update(r for r, pattern in FILE_ROUTES.items() if pattern.search(path.stem))
    if names & {'anevia', 'irabeth', 'tirabade'}:
        names |= {'anevia', 'irabeth', 'tirabade'}
    if names & {'minagho', 'chivarro', 'minagho_chivarro'}:
        names |= {'minagho', 'chivarro', 'minagho_chivarro'}
    return names


def filename_routes(path):
    return {r for r, pattern in FILE_ROUTES.items() if pattern.search(path.stem)}


def catalog():
    suites = {}
    for path in sorted((ROOT / 'tests').glob('*Tests.cs')):
        text = path.read_text(encoding='utf-8-sig')
        if re.search(r'(?:internal|public) static void Run\((?:Story \w+, )?Action<bool,\s*string> \w+\)', text):
            fixture = re.search(r'(?:internal|public) static void Run\(Action<bool,\s*string> \w+\)', text)
            suites[path.stem] = [] if fixture else sorted(mentioned_routes(path))
    return suites


def changed_files(base=None):
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=ROOT, timeout=30).decode().splitlines()
    files = git('diff', '--name-only', 'HEAD') + git('ls-files', '--others', '--exclude-standard')
    if base:
        files += git('diff', '--name-only', base + '...HEAD')
    return sorted(set(files))


def python_names(path, files):
    module = 'tests.' + path.stem
    expensive = 'test_late_consumer_registration_is_serialized'
    if path.stem != 'test_foresight_echo' or set(files) & {
            'expansion.py', 'story.py', 'storylines/foresight.py'}:
        return [module]
    current = ast.parse(path.read_text(encoding='utf-8-sig'))
    try:
        old = ast.parse(subprocess.check_output(['git', 'show', 'HEAD:tests/test_foresight_echo.py'],
                                               cwd=ROOT, stderr=subprocess.DEVNULL, timeout=30).decode('utf-8-sig'))
        body = lambda tree: next(ast.dump(n) for n in ast.walk(tree)
                                 if isinstance(n, ast.FunctionDef) and n.name == expensive)
        if body(current) != body(old):
            return [module]
    except (subprocess.CalledProcessError, StopIteration):
        return [module]
    # Its production factory and test body are unchanged. Keep every other
    # foresight test here; FULL discovery always runs the serialization witness.
    return [module + '.' + cls.name + '.' + method.name
            for cls in current.body if isinstance(cls, ast.ClassDef)
            for method in cls.body if isinstance(method, ast.FunctionDef)
            and method.name.startswith('test_') and method.name != expensive]


def select(files):
    suites = catalog()
    routes, shared = set(), not files
    touched_suites, touched_python = set(), set()
    for name in files:
        path = Path(name)
        if path.parts and path.parts[0] == 'tests':
            if path.stem in suites:
                touched_suites.add(path.stem)
            if path.name.startswith('test_') and path.suffix == '.py':
                touched_python.add(path.stem)
        if path.parts and path.parts[0] == 'tools':
            # A lint/selector regression must run even if neither file contains
            # a literal route name. Unknown systems keep the shared core too.
            stem = path.stem.replace('-', '_')
            candidates = {'test_' + stem, 'test_' + stem.removesuffix('_lint')}
            touched_python.update(candidate for candidate in candidates
                                  if (ROOT / 'tests' / (candidate + '.py')).is_file())
        if path.parts and path.parts[0] == 'storylines':
            match = {r for r in ROUTES if path.stem == r or path.stem.startswith(r + '_')}
            if match and path.stem not in SHARED_STORIES:
                routes |= match
                continue
        # Route-only test edits still need the shared engine regressions.
        if path.parts and path.parts[0] == 'tests' and path.name != 'Program.cs':
            actual = ROOT / path
            if actual.is_file() and actual.suffix in {'.py', '.cs'}:
                # A selector/cache/inventory fixture's example flags are not
                # ownership declarations for every route used in its examples.
                match = filename_routes(actual)
                if match and len(match) <= 3:
                    routes |= match
                    continue
        shared = True
    if routes & {'anevia', 'irabeth', 'tirabade'}:
        routes |= {'anevia', 'irabeth', 'tirabade'}
    if routes & {'minagho', 'chivarro', 'minagho_chivarro'}:
        routes |= {'minagho', 'chivarro', 'minagho_chivarro'}
    selected = [name for name, owners in suites.items()
                if not owners or name in FAST_INVENTORIES or name in touched_suites or routes.intersection(owners)]
    python = []
    for path in sorted((ROOT / 'tests').glob('test_*.py')):
        if path.stem == 'test_ideal_run_regression' and path.stem not in touched_python:
            continue  # always in FULL, which runs discovery
        owners = mentioned_routes(path)
        if path.stem in FAST_PYTHON or path.stem in touched_python or routes.intersection(owners):
            python.extend(python_names(path, files))
    return dict(files=files, shared=shared, routes=sorted(routes), suites=selected, python=python)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base')
    parser.add_argument('--files', nargs='+')
    parser.add_argument('--catalog', action='store_true')
    args = parser.parse_args()
    print(json.dumps(catalog() if args.catalog else select(args.files if args.files is not None
                                                        else changed_files(args.base)), indent=2))
