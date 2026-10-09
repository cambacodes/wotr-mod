"""Counterexample mutations through review, aggregation and dossier public seams.

All provider invocations use a disposable fake codex executable; no provider calls.
"""
import copy
import inspect
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'tools/playthrough'
sys.path.insert(0, str(TOOLS))
import admission
import dossier
import review
import walker
import dossier_evidence


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')


def finding(certainty='uncertain', severity='hard'):
    return dict(id='observation-1', chapter='1', scene='woman.callback', node='start', flag=None,
                kind='continuity', claim='Living appearance after loss.', evidence='woman.callback/start: "She enters."',
                certainty=certainty, disposition='pending_verification' if certainty == 'uncertain' else 'confirmed',
                severity=severity, recommended_form=None, recommendation='Verify the latest physical history.')


def luna(findings=None, scope='part'):
    findings = findings or []
    count = {s: sum(f['severity'] == s for f in findings) for s in ('hard', 'major', 'minor')}
    state = 'blocking' if any(f['severity'] == 'hard' and f['certainty'] == 'certain' for f in findings) else 'needs_fixes' if count['hard'] or count['major'] else 'pass_with_minor' if count['minor'] else 'pass'
    return dict(schema='rrt-checkpoint-review/2', dossier='policy/chapter-1.md', policy='policy', chapter='1', part=1,
                reviewer='luna', scope=scope, chapter_disposition='reviewed', findings=findings,
                characters=[dict(character_id='woman', present_in=['woman.callback'], state='present', voice='on', truth='on', notes='Observed.')],
                verdict=dict(count, chapter_status=state, fun={'score':6,'justification':'woman.callback pressure.'},
                             feels_like_part_of_the_game={'score':7,'justification':'woman.callback entry.'}, summary='Read.'),
                chapter_metrics={m:dict(score=None if scope == 'part' else 8, justification='Full sequence, woman.callback/start.',
                                        evidence=[] if scope == 'part' else ['woman.callback/start'],
                                        evidence_level='unmeasured' if scope == 'part' else 'simulated') for m in admission.METRICS})


def terra(disposition='dropped'):
    return dict(schema='rrt-checkpoint-adjudication/2', reviewer='terra', dossier='policy/chapter-1.md', policy='policy', chapter='1', part=1,
                dispositions=[dict(id='observation-1', disposition=disposition, reason='The earlier message does not imply a current body.', finding=None)])


FAKE_CODEX = '''#!/usr/bin/env python3
import json, os, re, sys
from pathlib import Path
prompt = sys.stdin.read()
model = sys.argv[sys.argv.index('-m') + 1]
response = Path(sys.argv[sys.argv.index('-o') + 1])
identity = json.loads(re.search(r'TASK: Review (\\{[^\\n]+\\})\\.', prompt).group(1))
with open(os.environ['FAKE_CALLS'], 'a', encoding='utf-8') as calls:
    calls.write(json.dumps({'model':model, 'response':str(response), 'identity':identity}) + '\\n')
obj = json.loads(Path(os.environ['FAKE_TERRA'] if model == 'fake-terra' else os.environ['FAKE_LUNA']).read_text(encoding='utf-8'))
if isinstance(obj, dict):
    for key in ('dossier','policy','chapter','part'):
        obj[key] = identity[key]
    if model != 'fake-terra':
        obj['scope'] = identity['scope']
        if identity['scope'] == 'chapter':
            obj['findings'] = []
            obj['verdict'].update(hard=0, major=0, minor=0, chapter_status='pass')
            for metric in obj['chapter_metrics'].values():
                metric.update(score=8, evidence=['woman.callback/start'], evidence_level='simulated')
response.write_text(json.dumps(obj), encoding='utf-8')
print(json.dumps({'type':'turn.completed', 'model':model, 'usage':{'input_tokens':20,'output_tokens':10,'cached_input_tokens':3}}))
exit(int(os.environ.get('FAKE_TERRA_EXIT' if model == 'fake-terra' else 'FAKE_LUNA_EXIT', '0')))
'''


class ReviewLoopTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='rrt-playthrough-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.tools = self.root / 'tools/playthrough'
        self.tools.mkdir(parents=True)
        for p in TOOLS.iterdir():
            if p.is_file(): shutil.copyfile(p, self.tools / p.name)
        self.runs = self.root / 'runs with spaces'
        self.policy = self.runs / 'policy'
        self.policy.mkdir(parents=True)
        self.export = self.root / 'Story.json'; write_json(self.export, {'scenes':[]})
        self.knowledge = self.root / 'knowledge'; self.knowledge.mkdir()
        (self.knowledge / 'canon.md').write_text('canon é\n', encoding='utf-8')
        (self.policy / 'chapter-1.md').write_text('woman.callback/start: She enters.\n', encoding='utf-8')
        (self.policy / 'chapter-1-timeline.md').write_text('Whole chapter.\n', encoding='utf-8')
        write_json(self.policy / 'trace.json', {'events':[]})
        write_json(self.policy / 'states.json', {'events':{}})
        write_json(self.policy / 'dossier-manifest.json', dict(policy='policy', trace='policy/trace.json', states='policy/states.json',
                   chapters=[dict(chapter='1', timeline='policy/chapter-1-timeline.md', parts=['policy/chapter-1.md'])]))
        bin_path = self.root / 'bin'; bin_path.mkdir()
        fake = bin_path / 'codex'; fake.write_text(FAKE_CODEX, encoding='utf-8', newline='\n'); fake.chmod(0o755)
        self.luna_path = self.root / 'luna.json'; self.terra_path = self.root / 'terra.json'
        write_json(self.luna_path, luna([finding()]))
        write_json(self.terra_path, terra())
        self.calls = self.root / 'calls.jsonl'
        self.env = dict(os.environ, PATH=str(bin_path) + os.pathsep + os.environ['PATH'],
                        FAKE_CALLS=str(self.calls), FAKE_LUNA=str(self.luna_path), FAKE_TERRA=str(self.terra_path))

    def review(self):
        return subprocess.run(['bash', str(self.tools / 'review.sh'), 'policy', '2', '--runs', str(self.runs),
                               '--knowledge', str(self.knowledge), '--export', str(self.export),
                               '--luna', 'fake-luna', '--terra', 'fake-terra'], cwd=self.root,
                              env=self.env, capture_output=True, encoding='utf-8', timeout=30)

    def aggregate(self):
        result = subprocess.run([sys.executable, str(self.tools / 'aggregate.py'), '--manifest', str(self.runs / 'review-manifest.json')],
                                cwd=self.root, env=self.env, capture_output=True, encoding='utf-8', timeout=30)
        self.assertTrue((self.runs / 'review-summary.json').exists(), result.stderr)
        return result, admission.load(self.runs / 'review-summary.json')

    def manifest(self):
        return admission.load(self.runs / 'review-manifest.json')

    def call_rows(self):
        return [json.loads(line) for line in self.calls.read_text(encoding='utf-8').splitlines()]

    def assert_review_ok(self):
        result = self.review()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        return result

    def repin_artifact(self, entry, reviewer, obj):
        record = entry[reviewer]
        path = self.runs / record['output']; write_json(path, obj)
        receipt_path = self.runs / record['receipt']; receipt = admission.load(receipt_path)
        receipt['output_digest'] = admission.digest(path); record['output_digest'] = receipt['output_digest']
        write_json(receipt_path, receipt)

    def test_valid_control_usage_unique_temps_and_cache(self):
        self.assert_review_ok()
        first = self.call_rows()
        self.assertEqual(3, len(first))  # part Luna, Terra, one chapter synthesis
        self.assertEqual(3, len({r['response'] for r in first}))
        for entry in self.manifest()['entries']:
            receipt = admission.load(self.runs / entry['luna']['receipt'])
            self.assertEqual(0, receipt['exit'])
            self.assertEqual({'input_tokens':20,'output_tokens':10,'cached_input_tokens':3}, receipt['usage'])
            self.assertEqual('fake-luna', receipt['actual_model'])
        self.assert_review_ok()
        self.assertEqual(first, self.call_rows())
        result, summary = self.aggregate()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(summary['complete'])
        self.assertIn('woman', summary['characters'])
        self.assertEqual(8, summary['overall']['flow_pacing'])

    def test_same_filename_changed_supplied_input_misses_cache(self):
        self.assert_review_ok()
        for path in (self.export, self.tools / 'reviewer-contract.md', self.knowledge / 'canon.md',
                     self.policy / 'trace.json', self.policy / 'states.json'):
            with self.subTest(path=path.name):
                before = len(self.call_rows())
                path.write_text(path.read_text(encoding='utf-8') + '\n', encoding='utf-8')
                self.assert_review_ok()
                self.assertGreater(len(self.call_rows()), before)

    def test_failed_terra_cannot_print_ok_or_reuse_failed_result(self):
        self.env['FAKE_TERRA_EXIT'] = '7'
        result = self.review()
        self.assertNotEqual(0, result.returncode)
        self.assertNotIn('terra ok', result.stdout)
        self.assertNotIn('review done', result.stdout)
        entry = self.manifest()['entries'][0]
        self.assertEqual('failed', entry['terra']['status'])
        receipt = admission.load(self.runs / entry['terra']['receipt'])
        self.assertEqual(7, receipt['exit'])
        self.assertEqual(20, receipt['usage']['input_tokens'])
        self.assertTrue((self.runs / receipt['raw']).exists())
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertEqual('pending_verification', summary['findings'][0]['disposition'])
        self.env.pop('FAKE_TERRA_EXIT')
        self.assert_review_ok()
        self.assertEqual(2, sum(r['model'] == 'fake-terra' for r in self.call_rows()))

    def test_nonzero_luna_exit_never_admits_valid_json(self):
        self.env['FAKE_LUNA_EXIT'] = '9'
        result = self.review()
        self.assertNotEqual(0, result.returncode)
        self.assertNotIn('luna ok', result.stdout)
        self.assertNotIn('review done', result.stdout)
        self.assertEqual('failed', self.manifest()['entries'][0]['luna']['status'])
        self.assertTrue(all(r['model'] == 'fake-luna' for r in self.call_rows()))

    def test_timeout_preserves_partial_raw_and_unknown_usage(self):
        def timeout(argv, **kwargs):
            Path(argv[argv.index('-o') + 1]).write_text('partial JSON', encoding='utf-8')
            raise subprocess.TimeoutExpired(argv, 900, output='partial diagnostic')
        entry = dict(dossier='policy/chapter-1.md', policy='policy', chapter='1', part=1, scope='part')
        with mock.patch.object(review.subprocess, 'run', side_effect=timeout):
            record, obj = review.run_call(entry, 'luna', [self.export], 'Fixture', 'fake-luna', self.runs)
        self.assertIsNone(obj)
        self.assertEqual('failed', record['status'])
        receipt = admission.load(self.runs / record['receipt'])
        self.assertIsNone(receipt['exit'])
        self.assertEqual('unknown', receipt['usage'])
        self.assertEqual('partial JSON', (self.runs / receipt['raw']).read_text(encoding='utf-8'))
        self.assertEqual('partial diagnostic', (self.runs / receipt['log']).read_text(encoding='utf-8'))

    def test_strict_output_variants_reject_malformed_luna(self):
        for mutate in (lambda o: o.update(extra='ignored'), lambda o: o.update(reviewer='terra'),
                       lambda o: o['verdict'].update(hard=True), lambda o: o['verdict'].update(hard=0),
                       lambda o: o['findings'][0].update(disposition='confirmed'),
                       lambda o: o['chapter_metrics']['flow_pacing'].update(score=9)):
            with self.subTest(mutation=mutate):
                obj = luna([finding()]); mutate(obj)
                write_json(self.luna_path, obj)
                result = self.review()
                self.assertNotEqual(0, result.returncode)
                self.assertNotIn('review done', result.stdout)

    def test_duplicate_json_keys_and_nonjson_constants_rejected(self):
        for raw in ('{"reviewer":"luna","reviewer":"terra"}', '{"score":NaN}', '{"score":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError): admission.parse_json(raw)

    def test_raw_prose_and_json_fragments_are_rejected(self):
        obj = luna([finding()])
        with self.assertRaises(ValueError): admission.admit('prose ' + json.dumps(obj), 'luna')
        fake = self.root / 'bin/codex'
        fake.write_text(FAKE_CODEX.replace('json.dumps(obj), encoding', "'prose ' + json.dumps(obj), encoding"), encoding='utf-8')
        result = self.review()
        self.assertNotEqual(0, result.returncode)
        self.assertNotIn('luna ok', result.stdout)

    def test_missing_terra_remains_pending(self):
        self.assert_review_ok()
        manifest = self.manifest(); manifest['entries'][0]['terra'] = {'status':'unrun','exit':None}
        write_json(self.runs / 'review-manifest.json', manifest)
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertFalse(summary['complete'])
        self.assertEqual(1, summary['counts']['pending'])
        self.assertEqual('pending', summary['reviews'][0]['current_verdict']['chapter_status'])
        self.assertEqual('pending_verification', summary['findings'][0]['disposition'])

    def test_invalid_extra_duplicate_omitted_terra_ids_never_clean(self):
        self.assert_review_ok()
        for mutate in (lambda o: o['dispositions'][0].update(id='foreign-id'),
                       lambda o: o['dispositions'].append(copy.deepcopy(o['dispositions'][0])),
                       lambda o: o.update(dispositions=[]),
                       lambda o: o['dispositions'][0].update(disposition='pass'),
                       lambda o: o['dispositions'][0].update(reason=''),
                       lambda o: o.update(findings=[])):
            with self.subTest(mutation=mutate):
                manifest = self.manifest(); obj = terra(); mutate(obj)
                self.repin_artifact(manifest['entries'][0], 'terra', obj)
                write_json(self.runs / 'review-manifest.json', manifest)
                result, summary = self.aggregate()
                self.assertEqual(1, result.returncode)
                self.assertEqual(1, summary['counts']['pending'])
                self.assertEqual('pending_verification', summary['findings'][0]['disposition'])

    def test_dropped_hard_item_changes_counts_preserves_scores_evidence(self):
        self.assert_review_ok()
        result, summary = self.aggregate()
        self.assertEqual(0, result.returncode)
        row = summary['findings'][0]
        self.assertEqual('dropped', row['disposition'])
        self.assertEqual('hard', row['raw_luna']['severity'])
        self.assertEqual('uncertain', row['raw_luna']['certainty'])
        self.assertEqual('pass', summary['reviews'][0]['current_verdict']['chapter_status'])
        self.assertEqual(0, summary['counts']['hard'])
        self.assertEqual('needs_fixes', summary['reviews'][0]['raw_verdict']['chapter_status'])
        self.assertEqual(6, summary['reviews'][0]['raw_verdict']['fun']['score'])
        self.assertEqual('luna', summary['reviews'][0]['score_reviewer'])

    def test_artifact_live_and_design_dispositions_retained(self):
        for disposition, exit_code in (('artifact',0), ('needs_live',1), ('design_required',1), ('pending_verification',1)):
            write_json(self.terra_path, terra(disposition))
            # Fresh chapter synthesis must consume the current adjudication.
            path = self.policy / 'chapter-1.md'
            path.write_text(path.read_text(encoding='utf-8') + '\n', encoding='utf-8')
            self.assert_review_ok()
            result, summary = self.aggregate()
            self.assertEqual(exit_code, result.returncode)
            self.assertEqual(disposition, summary['findings'][0]['disposition'])
            self.assertEqual('Living appearance after loss.', summary['findings'][0]['raw_luna']['claim'])

    def test_changed_adjudication_invalidates_chapter_synthesis(self):
        self.assert_review_ok()
        manifest = self.manifest()
        self.repin_artifact(manifest['entries'][0], 'terra', terra('artifact'))
        write_json(self.runs / 'review-manifest.json', manifest)
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertEqual('artifact', summary['findings'][0]['disposition'])
        self.assertTrue(any(e['error'] == 'luna stale inputs' and 'timeline' in e['dossier'] for e in summary['errors']))
        self.assertIsNone(summary['overall']['flow_pacing'])

    def test_revised_hard_and_invalid_replacement(self):
        self.assert_review_ok()
        manifest = self.manifest(); obj = terra('revised'); obj['dispositions'][0]['finding'] = finding('certain')
        self.repin_artifact(manifest['entries'][0], 'terra', obj); write_json(self.runs / 'review-manifest.json', manifest)
        _, summary = self.aggregate()
        self.assertEqual('blocking', summary['reviews'][0]['current_verdict']['chapter_status'])
        obj['dispositions'][0]['finding']['id'] = 'replacement-id'
        self.repin_artifact(manifest['entries'][0], 'terra', obj); write_json(self.runs / 'review-manifest.json', manifest)
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertEqual(1, summary['counts']['pending'])

    def test_manifest_only_reading_portable_root_and_stale_digest(self):
        self.assert_review_ok()
        (self.policy / 'review/stray.luna.json').write_text('not json', encoding='utf-8')
        (self.policy / 'review/stray.terra.json').write_text('not json', encoding='utf-8')
        result, summary = self.aggregate()
        self.assertEqual(0, result.returncode)
        self.assertEqual(1, len(summary['findings']))
        manifest = self.manifest(); manifest['entries'][0]['luna']['output'] = '../outside.json'
        write_json(self.runs / 'review-manifest.json', manifest)
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertIn('outside run root', summary['errors'][0]['error'])

    def test_changed_output_or_input_receipt_fails_admission(self):
        self.assert_review_ok()
        manifest = self.manifest(); out = self.runs / manifest['entries'][0]['luna']['output']
        out.write_text(out.read_text(encoding='utf-8') + '\n', encoding='utf-8')
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertIn('output digest mismatch', summary['errors'][0]['error'])
        self.assert_review_ok()
        self.export.write_text('{}', encoding='utf-8')
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertIn('stale inputs', summary['errors'][0]['error'])

    def test_repacking_parts_cannot_change_chapter_mean(self):
        self.assert_review_ok()
        _, before = self.aggregate()
        manifest = self.manifest()
        part = copy.deepcopy(manifest['entries'][0]); part['part'] = 2; part['dossier'] = 'policy/chapter-1-part-02.md'
        write_json(self.runs / part['dossier'], {})
        obj = luna([]); obj.update(part=2, dossier=part['dossier']); obj['verdict']['fun']['score'] = 10
        # New valid admitted part receipt; no provider and no dependency on part weighting.
        out = self.policy / 'review/extra.luna.json'; write_json(out, obj)
        receipt_path = self.policy / 'review/extra.receipt.json'
        receipt = dict(status='admitted', exit=0, input_digest='fixture', inputs={}, output_digest=admission.digest(out))
        write_json(receipt_path, receipt)
        part['luna'] = dict(status='admitted', input_digest='fixture', output='policy/review/extra.luna.json', receipt='policy/review/extra.receipt.json', output_digest=receipt['output_digest'])
        part['terra'] = {'status':'not_required','exit':None}
        manifest['entries'].append(part); write_json(self.runs / 'review-manifest.json', manifest)
        result, after = self.aggregate()
        self.assertEqual(0, result.returncode)
        self.assertEqual(before['overall'], after['overall'])
        self.assertEqual(before['chapter_cells'], after['chapter_cells'])

    def test_missing_chapter_score_and_undeclared_synthesis_stay_missing(self):
        self.assert_review_ok()
        manifest = self.manifest(); manifest['entries'] = manifest['entries'][:1]
        write_json(self.runs / 'review-manifest.json', manifest)
        result, summary = self.aggregate()
        self.assertEqual(1, result.returncode)
        self.assertIsNone(summary['overall']['flow_pacing'])
        self.assertTrue(any(e['error'] == 'chapter synthesis undeclared' for e in summary['errors']))

    def test_empty_chapter_and_metric_anchor_validation(self):
        obj = luna([], 'chapter'); obj['chapter_disposition'] = 'no_mod_content'
        with self.assertRaises(ValueError): admission.admit(obj, 'luna')
        for m in obj['chapter_metrics'].values(): m.update(score=None, evidence_level='unmeasured')
        admission.admit(obj, 'luna')
        obj['chapter_disposition'] = 'reviewed'
        for value in (-1,11,True):
            obj['chapter_metrics']['flow_pacing']['score'] = value
            with self.assertRaises(ValueError): admission.admit(obj, 'luna')
        schema = admission.load(TOOLS / 'reviewer-schema.json')
        for field in admission.METRICS:
            description = schema['$defs']['metrics']['properties'][field]['description']
            for score in (0,2,5,7,9,10): self.assertIn(str(score) + ': ', description)

    def test_old_behavior_mutations_are_killed_by_regressions(self):
        probes = [
            ('review.py', "return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest(), files",
             "return '0' * 64, files", 'ReviewLoopTests.test_same_filename_changed_supplied_input_misses_cache'),
            ('aggregate.py', "current = resolve(luna, terra) if luna else []",
             "current = resolve(luna, terra) if luna else []\n        if terra is None: current = [f for f in current if f['disposition'] != 'pending_verification']",
             'ReviewLoopTests.test_missing_terra_remains_pending'),
            ('aggregate.py', "characters[c['character_id']].append", "characters[c.get('character', 'missing')].append",
             'ReviewLoopTests.test_valid_control_usage_unique_temps_and_cache'),
            ('dossier.py', ' - set(part[-1][3].get("unset", []))', '', 'DossierEvidenceTests.test_final_unset_and_node_reference_terminal_entry'),
            ('review.py', "print('review done' if success else 'review FAILED')", "print('review done')",
             'ReviewLoopTests.test_failed_terra_cannot_print_ok_or_reuse_failed_result'),
        ]
        for filename, old, new, target in probes:
            with self.subTest(mutation=filename + ':' + target), tempfile.TemporaryDirectory(prefix='rrt-loop-mutant-') as tmp:
                root = Path(tmp); tools = root / 'tools/playthrough'; tools.mkdir(parents=True)
                for source in TOOLS.iterdir():
                    if source.is_file(): shutil.copyfile(source, tools / source.name)
                file = tools / filename; text = file.read_text(encoding='utf-8')
                self.assertEqual(1, text.count(old), 'mutation must hit the intended implementation once')
                file.write_text(text.replace(old, new), encoding='utf-8', newline='\n')
                tests = root / 'tests'; tests.mkdir(); (tests / '__init__.py').write_text('', encoding='utf-8')
                shutil.copyfile(Path(__file__), tests / 'test_playthrough_loop.py')
                result = subprocess.run([sys.executable, '-m', 'unittest', 'tests.test_playthrough_loop.' + target],
                                        cwd=root, env=self.env, capture_output=True, encoding='utf-8', timeout=60)
                self.assertNotEqual(0, result.returncode, 'surviving mutation: ' + target)
                self.assertIn('FAIL:', result.stderr, result.stdout + result.stderr)
                self.assertNotIn('ERROR:', result.stderr, result.stdout + result.stderr)


class DossierEvidenceTests(unittest.TestCase):
    def context(self):
        rel = dict(StartedFlag='woman.started', CommittedFlag='woman.committed', ClosedFlag='woman.closed',
                   UnavailableFlags=['native.loss'], UnavailableOverrides={'native.loss':'woman.return'})
        choice = dict(Text='Continue', Next=None, Set=['paid'], Requires=[], Forbids=[], Abort=False)
        node = dict(Id='start', Text='She enters.', Speaker='Woman', EnterSet=['node.entered'],
                    Paragraphs=[dict(Text='She remembers the paid return.', Requires=['woman.return'], Forbids=[], AnyGroups=[])], Choices=[choice])
        scene = dict(Id='woman.callback', Title='Callback', Owner='Woman', Relationship='woman', Nodes=[node], NativeReturnCue=None,
                     Entry='Talk', Remote=False, Requires=['woman.return'], Forbids=['later.loss'], ContactUnit='host-guid',
                     ParticipantWomen=['woman'], AnswerLists=['native-list-guid'], Participants=['woman'])
        V = SimpleNamespace(is_epilogue=lambda s: False, is_table_scene=lambda s: False, is_remote=lambda s: s.get('Remote',False))
        model = SimpleNamespace(rels={'woman':rel}, native={'native.loss':'native loss'}, by_id={'woman.callback':scene}, nodes={'woman.callback':{'start':node}})
        ctx = SimpleNamespace(model=model, V=V, G=SimpleNamespace(AREAS={}), names={'woman':'Woman'}, by_rel={'woman':['woman']}, story={}, knowledge=Path('/missing/knowledge'))
        ctx.women_of_scene = lambda s,e: ['woman']; ctx.native_lines = lambda w: []
        return ctx

    def event(self):
        return dict(type='scene', id='woman.callback', title='Callback', owner='Woman', rel='woman', ch=1, day=2, hour=24,
                    completed=True, remote=False, table=False, epilogue=False,
                    steps=[dict(node='start', index=0, paragraphs=[0], set=['paid'])], end_node=None,
                    set=['paid','node.entered'], unset=['woman.return','woman.committed'])

    def build_fixture(self, ctx, events, max_kb=120):
        tmp = tempfile.TemporaryDirectory(prefix='rrt-dossier-test-'); self.addCleanup(tmp.cleanup)
        runs = Path(tmp.name); policy = runs / 'policy'; policy.mkdir()
        summary = dict(description='Fixture', scenes_visited=sum(e['type']=='scene' for e in events), scenes_completed=1,
                       chapters_reached=[1], committed=[], closed=[], unavailable={})
        write_json(policy / 'trace.json', dict(events=events, summary=summary))
        dossier.build(ctx, 'policy', runs, max_kb, '../../reviewer-contract.md')
        return policy

    def test_final_unset_and_node_reference_terminal_entry(self):
        ctx = self.context(); event = self.event()
        ctx.model.nodes['woman.callback']['finish'] = dict(Id='finish', Text='Gone.', Speaker=None, EnterSet=['terminal.entered'], Paragraphs=[], Choices=[])
        event['end_node'] = dict(node='finish', paragraphs=[]); event['set'].append('terminal.entered')
        world = dict(type='world', ch=1, day=1, hour=0, on=['woman.started','woman.committed','woman.return','native.loss'], off=[])
        policy = self.build_fixture(ctx, [world,event])
        body = (policy / 'chapter-1.md').read_text(encoding='utf-8')
        end = body.split('## State at the end of this part')[1].split('## Appendix')[0]
        self.assertNotIn('committed', end)
        self.assertNotIn('(returned)', end)
        self.assertIn('native.loss', end)
        refs = admission.load(policy / 'states.json')['events']['1']
        self.assertNotIn('woman.return', refs['after'])
        self.assertNotIn('woman.committed', refs['after'])
        self.assertIn('terminal.entered', refs['nodes'][-1]['visible'])
        self.assertIn('woman.return', refs['nodes'][0]['visible'])
        self.assertIn('node.entered', refs['nodes'][0]['visible'])
        self.assertIn('states.json#/events/1/nodes/0', body)
        # Counterexample mutation: omitting final unset resurrects the stale return/commitment.
        mutant = self.event(); mutant['unset'] = []
        mutated = self.build_fixture(ctx, [world,mutant])
        end = (mutated / 'chapter-1.md').read_text(encoding='utf-8').split('## State at the end of this part')[1].split('## Appendix')[0]
        self.assertIn('committed', end); self.assertIn('(returned)', end)

    def test_gates_host_presence_authored_and_native_timeline(self):
        ctx = self.context()
        before = dict(type='world', ch=1, day=1, hour=0, on=['native.loss','woman.return'], off=[])
        after = dict(type='world', ch=1, day=9, hour=192, on=['later.loss'], off=['woman.return'])
        policy = self.build_fixture(ctx, [before,self.event(),after])
        body = (policy / 'chapter-1.md').read_text(encoding='utf-8')
        self.assertIn('host-guid', body); self.assertIn('native-list-guid', body)
        self.assertIn('ParticipantWomen', body); self.assertIn('later.loss', body)
        self.assertIn('authored mod scene', body)
        timeline = (policy / 'chapter-1-timeline.md').read_text(encoding='utf-8')
        self.assertIn('trace.json#/events/0', timeline)
        self.assertIn('trace.json#/events/2', timeline)  # whole chapter, beyond the part's 3-day window
        self.assertIn('scheduled native / derived (earning unknown)', timeline)
        self.assertIn('Required route beats: unknown', timeline)
        self.assertIn('woman.return <- trace.json#/events/0', timeline)
        after['off'] = []
        mutated = self.build_fixture(ctx, [before,self.event(),after])
        self.assertNotEqual(timeline, (mutated / 'chapter-1-timeline.md').read_text(encoding='utf-8'))

    def test_repacking_dossier_preserves_whole_chapter_timeline(self):
        ctx = self.context(); events = [self.event(), dict(self.event(), day=3, hour=48)]
        large = self.build_fixture(ctx, events, 120); small = self.build_fixture(ctx, events, 1)
        self.assertEqual((large / 'chapter-1-timeline.md').read_bytes(), (small / 'chapter-1-timeline.md').read_bytes())
        self.assertEqual(1, len(admission.load(large / 'dossier-manifest.json')['chapters'][0]['parts']))
        self.assertEqual(2, len(admission.load(small / 'dossier-manifest.json')['chapters'][0]['parts']))

    def test_no_physical_fate_inferred_from_flag_spelling_or_romance(self):
        ctx = self.context()
        rel = ctx.model.rels['woman']; rel['UnavailableFlags'] = ['native.killed']; rel['UnavailableOverrides'] = {}
        table = dossier.state_table(ctx, {'native.killed','woman.closed'})
        self.assertIn('physical role/history requires verification', table)
        self.assertNotIn('| dead |', table)
        table = dossier.state_table(ctx, {'woman.closed'})
        self.assertIn('| closed |', table)
        self.assertNotIn('absent', table)


class ExecutedTraceTests(unittest.TestCase):
    """Job con4: causal counterexamples at the executed trace/dossier seam.

    These assert observed histories, not registry/ledger semantic verdicts (jobs
    1/5). Each contrast changes what was played or displayed on the same path.
    """
    @classmethod
    def setUpClass(cls):
        global verify
        from tools import rrt_verify as verify

    def fixture(self, choices=None, **scene_fields):
        nodes = [dict(Id='start', Text='Before the choice.', EnterSet=['entry'],
                      Paragraphs=[dict(Text='Earlier rescue.', Requires=['rescued'])],
                      Choices=choices or [dict(Text='Pay', Next='finish', Set=['rescued'],
                                              Crusade=dict(Resource='Finances', Amount=-5))]),
                 dict(Id='finish', Text='She acknowledges it.', EnterSet=['callback.entered'],
                      Choices=[dict(Text='Continue', Set=['acknowledged'])])]
        story = dict(Relationships={'woman':dict(StartedFlag='woman.started', CommittedFlag='woman.committed',
                                                ClosedFlag='woman.closed')},
                     Scenes=[dict(Id='woman.test', Owner='Woman', Relationship='woman', Nodes=nodes, **scene_fields)])
        model = verify.Model(story); scene = model.scenes[0]
        state = verify.SimState(1, 24); state.crusade_resources = {'Finances':10}
        return model, scene, state

    def execute(self, model, scene, state, indices=(0,0), player=None, ordinal=0):
        path = [node['Choices'][i] for node, i in zip(scene['Nodes'], indices)]
        if player is None:
            plain = copy.deepcopy(state)
            plain_result = verify.sim_play(model, scene, plain, {}, ((), path))
        event = walker.executed_scene(verify, model, scene, state, {}, ((), path), ordinal, player)
        if player is None:
            self.assertEqual(plain_result, event['completed'])
            self.assertEqual(verify.sim_observation_state(plain), verify.sim_observation_state(state))
        event.update(id=scene['Id'], ch=state.chapter, hour=state.hour)
        return event

    def assert_prefix(self, event, nodes, choices, reason):
        self.assertEqual(nodes, [o['address']['node'] for o in event['observations'] if o['kind'] == 'display'])
        self.assertEqual(choices, [(s['node'],s['index']) for s in event['steps']])
        self.assertEqual(reason, event['observations'][-1]['reason'])

    def mutant(self, old, new):
        source = inspect.getsource(verify.sim_play)
        self.assertEqual(1, source.count(old), 'mutation must hit its intended site')
        namespace = dict(verify.__dict__)
        exec(compile(source.replace(old,new), '<con4-sim-mutant>', 'exec'), namespace)
        return namespace['sim_play']

    def test_failed_payment_and_contact_expose_only_executed_prefix(self):
        for failure in ('funds', 'contact'):
            with self.subTest(failure=failure):
                model, scene, state = self.fixture(ContactUnit='host')
                if failure == 'funds': state.crusade_resources['Finances'] = 4
                else: state.available_contacts = set()
                event = self.execute(model, scene, state)
                self.assert_prefix(event, ['start'], [], 'payment_or_contact_failed')
                self.assertFalse(event['completed']); self.assertNotIn('rescued', state.flags)
                self.assertNotIn('callback.entered', state.flags)
                self.assertEqual(4 if failure == 'funds' else 10, state.crusade_resources['Finances'])
                self.assertEqual('start', event['end_node']['node'])
                rows = dossier_evidence.node_states(SimpleNamespace(model=model), event, set())
                self.assertEqual([], rows[0]['paragraphs']); self.assertIsNone(rows[0]['choice_index'])
                self.assertEqual('simulator_observed', rows[0]['evidence_level'])
                state = verify.SimState(1,24); state.crusade_resources = {'Finances':10}; state.available_contacts = {'host'}
                sibling = self.execute(model, scene, state)
                self.assert_prefix(sibling, ['start','finish'], [('start',0),('finish',0)], 'completed')
                self.assertEqual(5, state.crusade_resources['Finances'])
                self.assertIn('acknowledged', state.flags)

    def test_transaction_rollback_is_not_a_decision_or_publication(self):
        model, scene, state = self.fixture()
        scene['Nodes'][0]['Choices'][0]['PostPayment'] = 'finish'
        # A real publication loses contact; sim_paid_choice rolls back all writes/debit.
        scene['Nodes'][0]['Choices'][0]['Set'].append('woman.closed')
        event = self.execute(model, scene, state)
        self.assert_prefix(event, ['start'], [], 'payment_or_contact_failed')
        self.assertEqual(10, state.crusade_resources['Finances'])
        self.assertNotIn('woman.closed', state.flags); self.assertNotIn('rescued', state.flags)
        payment = next(o for o in event['observations'] if o['kind'] == 'payment')
        self.assertEqual(event['states'][payment['before_state']], event['states'][payment['after_state']])
        scene['Nodes'][0]['Choices'][0]['Set'].remove('woman.closed')
        sibling = self.execute(model, scene, state)
        self.assertTrue(sibling['completed']); self.assertIn('rescued', state.flags)

    def test_accepted_abort_records_cost_and_effects_without_planned_suffix(self):
        model, scene, state = self.fixture()
        scene['Nodes'][0]['Choices'][0].update(Abort=True)
        event = self.execute(model, scene, state)
        self.assert_prefix(event, ['start'], [('start',0)], 'accepted_abort')
        self.assertEqual(5, state.crusade_resources['Finances'])
        self.assertIn('rescued', event['set']); self.assertNotIn(scene['Id'], state.flags)
        self.assertIsNone(event['end_node'])
        model, scene, state = self.fixture()
        self.assertTrue(self.execute(model, scene, state)['completed'])

    def test_unavailable_answer_and_unentered_target_are_not_execution(self):
        model, scene, state = self.fixture()
        scene['Nodes'][0]['Choices'][0]['Crusade'] = None
        scene['Nodes'][0]['Choices'][0]['Requires'] = ['missing']
        event = self.execute(model, scene, state)
        self.assert_prefix(event, ['start'], [], 'choice_unavailable')
        state.flags.add('missing')
        sibling = self.execute(model, scene, state, (0,))
        self.assert_prefix(sibling, ['start'], [('start',0)], 'path_exhausted')
        self.assertIsNone(sibling['end_node']); self.assertNotIn('callback.entered', state.flags)

    def test_unproduced_event_refusal_and_later_producer_preserve_display_phase(self):
        choices = [dict(Id='refuse', Text='Refuse rescue', Next='finish', Set=['refused']),
                   dict(Id='rescue', Text='Perform rescue', Next='finish', Set=['rescued'])]
        for index, expected in ((0,False),(1,True)):
            model, scene, state = self.fixture(choices=copy.deepcopy(choices))
            scene['Nodes'][1]['Paragraphs'] = [dict(Text='You remember the rescue.', Requires=['rescued'])]
            scene['Nodes'][1]['Choices'][0]['Set'] = ['rescued']  # too late for this paragraph
            event = self.execute(model, scene, state, (index,0))
            rows = dossier_evidence.node_states(SimpleNamespace(model=model), event, set())
            self.assertNotIn('rescued', rows[0]['visible'])
            self.assertEqual([], rows[0]['paragraphs'])
            self.assertEqual(expected, 'rescued' in rows[1]['visible'])
            self.assertEqual([0] if expected else [], rows[1]['paragraphs'])
            self.assertTrue(event['steps'][0]['answer_name'].endswith('.' + ('rescue' if expected else 'refuse')))
            self.assertIn('rescued', rows[1]['after_choice'])

    def test_dead_speaker_latest_loss_and_earlier_letter_have_distinct_states(self):
        # Trace preserves history and individual actors; it does not infer life from commitment.
        for lost in (False,True):
            model, scene, state = self.fixture(choices=[dict(Text='Continue', Next='finish')])
            state.flags.update({'woman.returned','woman.committed','pair.other.alive'})
            state.times['woman.returned'] = 1
            if lost: state.flags.add('woman.later_loss'); state.times['woman.later_loss'] = 23
            scene['Nodes'][0]['Paragraphs'] = [dict(Text='Earlier authored letter.', Requires=['woman.returned'])]
            event = self.execute(model, scene, state)
            rows = dossier_evidence.node_states(SimpleNamespace(model=model), event, set())
            self.assertEqual(lost, 'woman.later_loss' in rows[0]['visible'])
            self.assertIn('pair.other.alive', rows[0]['visible']); self.assertEqual([0], rows[0]['paragraphs'])
            snap = event['states'][event['steps'][0]['visible_state']]
            self.assertEqual(1, snap['times']['woman.returned'])
            if lost: self.assertEqual(23, snap['times']['woman.later_loss'])

    def test_promised_stance_missing_and_opposite_acknowledgment_are_not_fabricated(self):
        for opened, opposite in ((False,False),(True,False),(True,True)):
            model, scene, state = self.fixture(choices=[dict(Id='share', Text='Share', Next='finish', Set=['stance.share'])])
            scene['Nodes'][1]['Paragraphs'] = [dict(Text='Sharing acknowledged.', Requires=['stance.share']),
                                               dict(Text='Exclusive acknowledged.', Requires=['stance.exclusive'])]
            if opposite: scene['Nodes'][0]['Choices'][0]['Set'] = ['stance.exclusive']
            event = self.execute(model, scene, state, (0,0) if opened else (0,))
            self.assertTrue(event['steps'][0]['answer_name'].endswith('.share'))
            if not opened:
                self.assertIsNone(event['end_node']); self.assertEqual(['start'], [s['node'] for s in event['steps']])
            else: self.assertEqual([1] if opposite else [0], event['steps'][1]['paragraphs'])

    def test_unwitnessed_reaction_world_receipt_and_report_do_not_create_witness(self):
        for knowledge, expected in (([],[]),(['B.witness'],[0]),(['B.report'],[1])):
            model, scene, state = self.fixture(choices=[dict(Text='Continue', Next='finish')])
            state.flags.update(['event.happened', 'B.present', *knowledge])
            scene['Nodes'][0]['Paragraphs'] = [dict(Text='I saw it.', Requires=['B.witness']),
                                               dict(Text='I heard about it.', Requires=['B.report'])]
            event = self.execute(model, scene, state)
            self.assertEqual(expected, event['steps'][0]['paragraphs'])
            self.assertEqual('B.witness' in knowledge, 'B.witness' in event['states'][event['after_state']]['flags'])

    def test_repeated_selection_and_refreshed_time_are_occurrences_not_deltas(self):
        model, scene, state = self.fixture(choices=[dict(Id='promise', Text='Promise', Set=['promise'], RefreshTimes=['promise'])])
        state.flags.add('promise'); state.times['promise'] = 1
        event = self.execute(model, scene, state, (0,))
        self.assertNotIn('promise', event['set'])
        self.assertEqual(['promise'], event['steps'][0]['set'])
        selection = next(o for o in event['observations'] if o['kind'] == 'selection')
        self.assertEqual(1, event['states'][selection['before_state']]['times']['promise'])
        self.assertEqual(24, event['states'][selection['after_state']]['times']['promise'])
        state.hour = 48
        second = self.execute(model, scene, state, (0,), ordinal=1)
        self.assertEqual(event['steps'][0]['answer_guid'], second['steps'][0]['answer_guid'])
        self.assertEqual(48, second['states'][second['after_state']]['times']['promise'])
        self.assertEqual(24, event['states'][event['after_state']]['times']['promise'])

    def test_observer_is_optional_and_final_state_disagreement_fails(self):
        model, scene, state = self.fixture()
        plain, observed = copy.deepcopy(state), copy.deepcopy(state)
        path = [n['Choices'][0] for n in scene['Nodes']]
        plain_result = verify.sim_play(model,scene,plain,{},((),path))
        result = self.execute(model,scene,observed)
        self.assertEqual(plain_result, result['completed'])
        self.assertEqual(verify.sim_observation_state(plain), verify.sim_observation_state(observed))
        def divergent(*args, **kwargs):
            ok = verify.sim_play(*args, **kwargs); args[2].flags.add('unobserved.write'); return ok
        with self.assertRaisesRegex(ValueError, 'final state disagrees'):
            self.execute(model,scene,copy.deepcopy(state), player=divergent)
        result['after_state'] = result['before_state']
        with self.assertRaisesRegex(ValueError, 'final state mismatch'):
            dossier_evidence.node_states(SimpleNamespace(model=model),result,set())

    def test_runtime_answer_identity_forms_and_ambiguous_native_hosts(self):
        model, scene, state = self.fixture(choices=[dict(Text='Ordinary'),dict(Id='saved',Text='Named')])
        node = scene['Nodes'][0]
        for index, expected, guid in ((0,'answer.woman.test.start.0','3ce0b116b4e42d3eb627735e74ecbc44'),
                                      (1,'answer.woman.test.start.saved','8844532f8d6fdb423316042bf3bf5703')):
            identity = verify.sim_answer_identity(scene,node,index)
            self.assertEqual(expected, identity['name'])
            self.assertEqual(guid, identity['guid'])
        scene['Owner'] = 'WomanEpilogue'; node['Choices'] = [verify.norm_scene(dict(Nodes=[dict(Choices=[dict(Text='Continue')])]))['Nodes'][0]['Choices'][0]]
        self.assertEqual('answer.woman.test.start.continue', verify.sim_answer_identity(scene,node,0)['name'])
        self.assertEqual('6be29c1f7fd3a1042c76fbc13be78176', verify.sim_answer_identity(scene,node,0)['guid'])
        node['Choices'].append(dict(node['Choices'][0], Id='other', Text='Another exit'))
        node['Choices'][0]['Id'] = 'continue'
        self.assertEqual('answer.woman.test.start.continue', verify.sim_answer_identity(scene,node,0)['name'])
        scene.update(ReturnToList=True,AnswerLists=['native-list-A','native-list-B'])
        unknown = verify.sim_answer_identity(scene,node,0)
        self.assertIsNone(unknown['guid']); self.assertEqual(2,len(unknown['candidates']))
        self.assertEqual('answer.woman.test.native-list-B.start.0', verify.sim_answer_identity(scene,node,0,'native-list-B')['name'])
        self.assertEqual('40b6eea157b28e2497a87403d8eccecb', verify.sim_answer_identity(scene,node,0,'native-list-B')['guid'])
        native_event = walker.executed_scene(verify,model,scene,state,{},((),[node['Choices'][0]]),answer_list='native-list-B')
        self.assertEqual('40b6eea157b28e2497a87403d8eccecb',native_event['steps'][0]['answer_guid'])
        scene['AnswerLists'] = ['native-list-A']
        self.assertEqual('answer.woman.test.native-list-A.start.0', verify.sim_answer_identity(scene,node,0)['name'])

    def test_execution_mutations_are_killed_by_the_prefix_and_history_assertions(self):
        mutations = [
            ('if not accepted: return finish(False, "payment_or_contact_failed")', 'if not accepted: publish()', 'funds'),
            ('if c["Abort"]: return finish(False, "accepted_abort")', 'if False: return finish(False, "accepted_abort")', 'abort'),
            ('emit("selection", before, node=node["Id"]', 'emit("selection", snapshot(), node=node["Id"]', 'future-set'),
            ('writes=list(c["Set"])', 'writes=[]', 'repeat'),
        ]
        for old,new,case in mutations:
            with self.subTest(case=case):
                model,scene,state = self.fixture()
                if case == 'funds': state.crusade_resources['Finances'] = 4
                if case == 'abort': scene['Nodes'][0]['Choices'][0]['Abort'] = True
                mutant = self.mutant(old,new)
                event = self.execute(model,scene,state,player=mutant)
                with self.assertRaises(AssertionError):
                    if case == 'funds': self.assert_prefix(event,['start'],[],'payment_or_contact_failed')
                    elif case == 'abort': self.assert_prefix(event,['start'],[('start',0)],'accepted_abort')
                    elif case == 'future-set':
                        selection = next(o for o in event['observations'] if o['kind']=='selection')
                        self.assertNotIn('rescued',event['states'][selection['before_state']]['flags'])
                    else: self.assertEqual(['rescued'],event['steps'][0]['set'])

    def test_four_causal_history_regressions_kill_evidence_mutations(self):
        probes = [
            (verify, 'sim_play', 'if all(f in st.flags for f in p.get("Requires", []))',
             'if all(f in st.flags | set(c["Set"]) for f in p.get("Requires", []))',
             self.test_unproduced_event_refusal_and_later_producer_preserve_display_phase),
            (verify, 'sim_observation_state', 'flags=sorted(st.flags)',
             'flags=sorted(f for f in st.flags if f != "woman.later_loss")',
             self.test_dead_speaker_latest_loss_and_earlier_letter_have_distinct_states),
            (walker, 'executed_scene', 'if display else None)',
             'if display else dict(node="finish", paragraphs=[0], before_entry_state=0, visible_state=0))',
             self.test_promised_stance_missing_and_opposite_acknowledgment_are_not_fabricated),
            (verify, 'sim_play', 'if all(f in st.flags for f in p.get("Requires", []))',
             'if all(f in st.flags or f == "B.witness" and "B.present" in st.flags for f in p.get("Requires", []))',
             self.test_unwitnessed_reaction_world_receipt_and_report_do_not_create_witness),
        ]
        for module, name, old, new, regression in probes:
            with self.subTest(regression=regression.__name__):
                source = inspect.getsource(getattr(module, name))
                self.assertEqual(1,source.count(old))
                namespace = dict(module.__dict__)
                exec(compile(source.replace(old,new), '<con4-evidence-mutant>', 'exec'),namespace)
                with mock.patch.object(module,name,namespace[name]), self.assertRaises(AssertionError):
                    regression()


if __name__ == '__main__':
    unittest.main()
