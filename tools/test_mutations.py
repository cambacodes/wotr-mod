"""Reproduce the streamlining audit on a disposable system-temp scratch branch.

Only test/tools/source copies are mutated. The working export is read once;
mutated exports, logs, assemblies and the scratch worktree are removed on exit.
The optional evidence JSON must live outside the repository.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

from test_selection import ROOT, select


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    parser.add_argument('--only', choices=('all', 'world-cache', 'draft-cache', 'scene-fixture', 'selector', 'consumer', 'bindings-timing'), default='all')
    args = parser.parse_args()
    if args.json.resolve().is_relative_to(ROOT):
        parser.error('--json must point outside the repository')
    evidence = []
    with tempfile.TemporaryDirectory(prefix='rrt-mutations-') as directory:
        temp = Path(directory)
        scratch = temp / 'checkout'
        branch = 'audit/eng-tests-' + uuid.uuid4().hex
        subprocess.run(['git', 'worktree', 'add', '-q', '-b', branch, str(scratch), 'HEAD'], cwd=ROOT, check=True)
        # The coordinator may prune worktrees from a host that cannot see this
        # container's /tmp. A lock keeps this registered until our own cleanup.
        subprocess.run(['git', 'worktree', 'lock', '--reason', 'temporary test mutation audit', str(scratch)], cwd=ROOT, check=True)
        try:
            # Include the pending implementation, without committing it.
            for name in ('tests', 'tools'):
                shutil.copytree(ROOT / name, scratch / name, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('bin', 'obj', '__pycache__'))
            env = dict(os.environ, PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1',
                       RRT_GAME_DIR='/wrath', RRT_TEST_BUILD_ROOT=str(temp / 'build'),
                       RRT_TEST_STORY=str(ROOT / 'development/Story.json'))
            story_path = temp / 'Story.json'
            story = json.loads((ROOT / 'development/Story.json').read_text(encoding="utf-8"))
            story_path.write_text(json.dumps(story), encoding="utf-8")

            def command(cmd):
                start = time.perf_counter()
                run = subprocess.run(cmd, cwd=scratch, env=env, capture_output=True, text=True)
                output = run.stdout + run.stderr
                failure = next((line for line in output.splitlines() if line.startswith('FAIL:')), '')
                return dict(exit=run.returncode, seconds=round(time.perf_counter()-start, 4),
                            receipt=failure + '\n' + output[-1600:])

            def record(name, results, expected, scope, detector):
                assert detector in select(scope)['suites'] or detector in select(scope)['python'], detector
                for label, failed in expected.items():
                    assert bool(results[label]['exit']) == failed, (name, label, results[label])
                    receipt = results[label]['receipt']
                    if failed and 'Ran ' in receipt and 'FAILED (' in receipt:
                        assert 'FAIL:' in receipt or 'AssertionError' in receipt, (name, 'infrastructure error', receipt)
                evidence.append(dict(mutation=name, results=results, scope=scope, fast_detector=detector))
                args.json.write_text(json.dumps(evidence, indent=2) + '\n', encoding="utf-8")
                print(name + ': expected outcomes confirmed', flush=True)

            def python_case(module, method, setup):
                code = setup + '\nimport unittest\nfrom ' + module + ' import *\n' + \
                    's=unittest.defaultTestLoader.loadTestsFromName(' + repr(module + '.' + method) + ')\n' + \
                    'r=unittest.TextTestRunner(verbosity=2).run(s)\nraise SystemExit(not r.wasSuccessful())'
                return command([sys.executable, '-B', '-c', code])

            def build():
                result = command(['dotnet','build','tests/RulesTests.csproj','-c','Release','--nologo','-v','quiet'])
                if result['exit']: raise RuntimeError(result['receipt'])
            def rules(suite):
                return command(['dotnet', str(temp/'build/bin/Release/net8.0/RulesTests.dll'),
                                '--suites='+suite, str(story_path)])
            def world_cache_mutations():
                path = scratch / 'tests/WorldBuildCache.cs'
                original = path.read_bytes()
                for name, old, new in (
                    ('world cache: merge earned and unearned flags', 'JsonSerializer.Serialize(state, options)', 'state.Chapter.ToString()'),
                    ('world cache: retain mutable caller result', 'Program.Copy(state)', 'state'),
                    ('world cache: project away money and timestamps', 'JsonSerializer.Serialize(state, options)', 'JsonSerializer.Serialize(new { state.Chapter, state.Flags }, options)'),
                ):
                    assert original.count(old.encode()) == 1
                    path.write_bytes(original.replace(old.encode(), new.encode()))
                    build()
                    record(name, dict(retained=rules('WorldBuildCacheTests')), dict(retained=True),
                           ['tests/WorldBuildCache.cs'], 'WorldBuildCacheTests')
                path.write_bytes(original)
            if args.only == 'world-cache':
                world_cache_mutations()
                return 0

            if args.only in ('all', 'bindings-timing'):
                path = scratch / 'tools/test_gate.py'
                original = path.read_bytes()
                guard = b"if label != 'bindings':"
                assert original.count(guard) == 1
                path.write_bytes(original.replace(guard, b'if True:'))
                result = python_case('tests.test_test_selection',
                    'SelectionTests.test_bindings_cannot_overwrite_completed_rules_receipts', '')
                record('gate receipts: bindings reuses campaign output paths',
                       dict(retained=result), dict(retained=True),
                       ['tools/test_gate.py'], 'tests.test_test_selection')
                path.write_bytes(original)
                if args.only == 'bindings-timing':
                    return 0

            if args.only in ('all', 'consumer'):
                path = scratch / 'tests/test_foresight_echo.py'
                original = path.read_bytes()
                old_test = subprocess.check_output(['git','show','HEAD:tests/test_foresight_echo.py'], cwd=ROOT)
                for sid in ('household.table.offered', 'household.table.offered_c5', 'wenduag.trickster.echo.abyss.prepare'):
                    changed = json.loads(json.dumps(story))
                    scene = next(s for s in changed['Scenes'] if s['Id'] == sid)
                    if sid.startswith('household.'):
                        scene['Requires'].remove('foresight.page_taken')
                        changed['ForesightConsumers'].pop(sid)
                        name = 'consumer: omit gate and registry for ' + sid
                    else:
                        scene['Id'] = sid + '.wrong'
                        changed['ForesightConsumers'][scene['Id']] = changed['ForesightConsumers'].pop(sid)
                        name = 'consumer: rename scene and registry together'
                    story_path.write_text(json.dumps(changed), encoding="utf-8")
                    setup = ('import copy,json; from pathlib import Path; from tests import test_foresight_echo as t; '
                        'consumer_fixture=json.loads(Path(' + repr(str(story_path)) + ').read_text(encoding="utf-8")); '
                        't.fresh_story=lambda:copy.deepcopy(consumer_fixture); '
                        't.foresight.CONSUMERS.clear(); t.foresight.CONSUMERS.update(consumer_fixture["ForesightConsumers"])')
                    method = 'ForesightSurfaceTests.test_registered_consumer_contract_matches_export'
                    path.write_bytes(old_test)
                    old = python_case('tests.test_foresight_echo', method, setup)
                    path.write_bytes(original)
                    new = python_case('tests.test_foresight_echo', method, setup)
                    record(name, dict(generator_oracle=old, independent_contract=new),
                           dict(generator_oracle=False, independent_contract=True),
                           ['storylines/foresight.py'], 'tests.test_foresight_echo')
                path.write_bytes(original); story_path.write_text(json.dumps(story), encoding="utf-8")
                if args.only == 'consumer':
                    return 0

            if args.only in ('all', 'selector'):
                path = scratch / 'tools/test_selection.py'
                original = path.read_bytes()
                for name, old, new in (
                    ('selector: ignore generator changes', 'or set(files) & {', 'or set() & {'),
                    ('selector: ignore edited serialization witness', 'if body(current) != body(old):', 'if False:'),
                ):
                    assert original.count(old.encode()) == 1
                    path.write_bytes(original.replace(old.encode(), new.encode()))
                    result = python_case('tests.test_test_selection',
                        'SelectionTests.test_generator_serialization_witness_runs_when_its_source_changes', '')
                    record(name, dict(retained=result), dict(retained=True),
                           ['tools/test_selection.py'], 'tests.test_test_selection')
                path.write_bytes(original)
                if args.only == 'selector':
                    return 0

            if args.only in ('all', 'scene-fixture'):
                path = scratch / 'tests/test_delivery_inventory2.py'
                original = path.read_bytes()
                for name, old, new in (
                    ('scene fixture: reuse mutable scene list', "Scenes=list(self.story['Scenes'])", "Scenes=self.story['Scenes']"),
                    ('scene fixture: shallow-copy nested answers', "copy.deepcopy(story['Scenes'][index])", "dict(story['Scenes'][index])"),
                ):
                    assert original.count(old.encode()) == 1
                    path.write_bytes(original.replace(old.encode(), new.encode()))
                    result = python_case('tests.test_delivery_inventory2',
                        'DeliveryInventory2Tests.test_scene_variants_cannot_poison_later_mutations', '')
                    record(name, dict(retained=result), dict(retained=True),
                           ['tests/test_delivery_inventory2.py'], 'tests.test_delivery_inventory2')
                path.write_bytes(original)
                if args.only == 'scene-fixture':
                    return 0

            draft_lint = scratch / 'tools/draft_contract_lint.py'
            original_draft = draft_lint.read_bytes()
            guard = b"if data['root'] == str(Path(root).resolve()):"
            assert original_draft.count(guard) == 1
            draft_lint.write_bytes(original_draft.replace(guard, b'if True:'))
            result = python_case('tests.test_draft_contract_lint',
                'DraftContractTests.test_shared_gate_fixture_does_not_hide_defects_or_other_sources',
                'from tests.test_draft_contract_lint import DraftContractTests; '
                'DraftContractTests.setUpClass=classmethod(lambda cls: None)')
            record('draft fixture: reuse another source root', dict(retained=result), dict(retained=True),
                   ['tools/draft_contract_lint.py'], 'tests.test_draft_contract_lint')
            draft_lint.write_bytes(original_draft)
            if args.only == 'draft-cache':
                return 0

            old_speech = subprocess.check_output(['git','show','claude/eng-final:tests/test_player_text_lint.py'], cwd=ROOT)
            new_speech = (scratch / 'tests/test_player_text_lint.py').read_bytes()
            for name, setup in (
                ('speech: omit tell attribution', 'from tools import player_text_lint as l; import re; p=l.PATTERNS["embedded-commander-speech"]; l.PATTERNS["embedded-commander-speech"]=re.compile(p.pattern.replace("say|tell|ask", "say|ask"),re.I)'),
                ('speech: omit straight quoted attribution', 'from tools import player_text_lint as l; import re; p=l.PATTERNS["embedded-commander-speech"]; l.PATTERNS["embedded-commander-speech"]=re.compile(p.pattern.replace(\'["”]\',\'[”]\'),re.I)'),
                ('speech: corrupt finding span', 'from tools import player_text_lint as l; original=l.check\ndef bad(*a,**k):\n r=original(*a,**k)\n for row in r["review"]:\n  if row["code"]=="embedded-commander-speech": row["start"]=-1\n return r\nl.check=bad'),
            ):
                (scratch / 'tests/test_player_text_lint.py').write_bytes(old_speech)
                old = python_case('tests.test_player_text_lint', 'PlayerTextTests.test_explicit_speech_and_review_span', setup)
                (scratch / 'tests/test_player_text_lint.py').write_bytes(new_speech)
                new = python_case('tests.test_player_text_lint', 'PlayerTextTests.test_npc_questions_and_demands_are_not_commander_attributions', setup)
                record(name, dict(removed=old, retained=new), dict(removed=True,retained=True),
                       ['tools/player_text_lint.py'], 'tests.test_player_text_lint')
            result = python_case('tests.test_harem_smoothing', 'ShippedData.test_doc16_parser',
                                 'from tests.test_harem_smoothing import lint as l; l.parse_doc16_tags=lambda text: {}')
            record('doc16: parser discards table', dict(retained=result), dict(retained=True),
                   ['tools/harem_smoothing_lint.py'], 'tests.test_harem_smoothing')

            build()
            native_test = scratch / 'tests/test_native_answer_edits.py'
            native_test.write_bytes(subprocess.check_output(['git','show','claude/eng-final:tests/test_native_answer_edits.py'],cwd=ROOT))
            for name, groups in (
                ('native answer: remove current Trickster guard', [['kiana.trickster.guests_home']]),
                ('native answer: remove paid guest history', [['trickster.now']]),
                ('native answer: substitute individual return', [['trickster.now','kiana.trickster.returned']]),
            ):
                old = python_case('tests.test_native_answer_edits', 'NativeAnswerContractTests.test_shipped_answers_match_runtime_whitelist',
                    'from storylines import kiana_native as k; k.HOME_WORLDS[:]='+repr(groups))
                changed = json.loads(json.dumps(story))
                for edit in changed['NativeAnswerEdits'].values():
                    if edit['Relationship']=='kiana': edit['When']=groups
                story_path.write_text(json.dumps(changed), encoding="utf-8")
                record(name, dict(self_reference=old, runtime=rules('KianaNativeReconciliationTests')),
                       dict(self_reference=False,runtime=True), ['storylines/kiana_native.py'], 'KianaNativeReconciliationTests')
            story_path.write_text(json.dumps(story), encoding="utf-8")
            source = scratch / 'src/Story.cs'
            source_bytes = source.read_bytes()
            for name, old, new in (
                ('contacts: omit ambiguity guard', 'if (found != null) return null;', 'if (false) return null;'),
                ('contacts: ignore living unusable twin', 'else if (!ignorable(candidate)) return null;', 'else if (false) return null;'),
                ('contacts: reject dead original beside copy', 'else if (!ignorable(candidate)) return null;', 'else return null;'),
            ):
                assert source_bytes.count(old.encode()) == 1
                source.write_bytes(source_bytes.replace(old.encode(), new.encode()))
                build()
                record(name, dict(fixture=rules('ContactDisambiguationTests'), inventory=rules('PresenceTransitionInventoryTests')),
                       dict(fixture=True,inventory=True), ['src/Story.cs'], 'ContactDisambiguationTests')
            source.write_bytes(source_bytes)
            cache = scratch / 'tests/ReachabilityCache.cs'
            original = cache.read_bytes()
            for name, old, new in (
                ('cache: merge resources and timestamps', 'JsonSerializer.Serialize(start, options)', 'string.Join(",", start.Flags)'),
                ('cache: discard earlier branch outcomes', 'else Flags.UnionWith(Walk.Current.Flags);', 'else { Flags.Clear(); Flags.UnionWith(Walk.Current.Flags); }'),
                ('cache: merge area partitions', 'JsonSerializer.Serialize(partition)', '"shared"'),
            ):
                assert old.encode() in original
                cache.write_bytes(original.replace(old.encode(), new.encode()))
                build()
                record(name, dict(retained=rules('ReachabilityCacheTests')), dict(retained=True),
                       ['tests/ReachabilityCache.cs'], 'ReachabilityCacheTests')
            cache.write_bytes(original)
            world_cache_mutations()
            build()
            for route in ('arueshalae','chadali','delamere','devarra','dorgelinda','eritrice','jannah','kaylessa','mielarah','nenio'):
                suite = route.capitalize() + 'TricksterTests'
                for field in ('ClosedFlag','CommittedFlag'):
                    changed = json.loads(json.dumps(story))
                    rel = changed['Relationships'][route]
                    rel['StartedFlag'],rel[field] = rel[field],rel['StartedFlag']
                    story_path.write_text(json.dumps(changed), encoding="utf-8")
                    record(route+': swap StartedFlag/'+field, dict(retained=rules(suite)), dict(retained=True),
                           ['storylines/'+route+'_trickster.py'], suite)
        finally:
            try:
                subprocess.run(['git','worktree','remove','--force','--force',str(scratch)],cwd=ROOT,check=True)
            finally:
                subprocess.run(['git','branch','-D',branch],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
