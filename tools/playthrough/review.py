"""Run and admit pinned checkpoint reviews. Provider invocation is confined to run_call."""
import argparse
import concurrent.futures
import hashlib
import json
import os
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

from admission import HERE, admit, atomic_json, digest, load, parse_json, uncertain

ROOT = HERE.parents[1]


def pin_inputs(paths, prompt, model, reviewer):
    files = {str(Path(p).resolve()): digest(p) for p in sorted(set(paths))}
    payload = dict(files=files, prompt=prompt, model=model, reviewer=reviewer, effort='medium', sandbox='read-only')
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest(), files


def usage_from_log(log):
    usage, actual_model = 'unknown', 'unknown'
    for line in log.splitlines():
        try: event = json.loads(line)
        except ValueError: continue
        if isinstance(event, dict):
            if isinstance(event.get('usage'), dict): usage = event['usage']
            if event.get('model'): actual_model = event['model']
    return usage, actual_model


def run_call(entry, reviewer, paths, prompt, model, runs, submitted=None):
    key, files = pin_inputs(paths, prompt, model, reviewer)
    name = Path(entry['dossier']).stem + '.' + reviewer
    out = runs / entry['policy'] / 'review' / key / (name + '.json')
    receipt_path = out.with_suffix('.receipt.json')
    identity = {k: entry[k] for k in ('dossier', 'policy', 'chapter', 'part')}
    if reviewer == 'luna': identity['scope'] = entry['scope']
    result = dict(reviewer=reviewer, status='failed', input_digest=key,
                  output=out.relative_to(runs).as_posix(), receipt=receipt_path.relative_to(runs).as_posix())
    if out.exists() and receipt_path.exists():
        try:
            receipt = load(receipt_path)
            obj = admit(load(out), reviewer, submitted, identity)
            if receipt['input_digest'] == key and receipt['exit'] == 0 and receipt['status'] == 'admitted' and receipt['output_digest'] == digest(out):
                return dict(result, status='admitted', output_digest=digest(out), cached=True), obj
        except (ValueError, KeyError): pass
    attempt = uuid.uuid4().hex
    log_path = out.parent / (name + '.' + attempt + '.log')
    raw_path = out.parent / (name + '.' + attempt + '.raw')
    start = time.monotonic()
    exit_code, log, raw, obj, error = None, '', '', None, None
    with tempfile.TemporaryDirectory(prefix='rrt-review-') as tmp:
        response = Path(tmp) / 'response.json'
        argv = ['codex', 'exec', '-m', model, '-s', 'read-only', '-C', str(ROOT),
                '--skip-git-repo-check', '--ephemeral', '--json',
                '-c', 'model_reasoning_effort="medium"', '-o', str(response), '-']
        try:
            process = subprocess.run(argv, input=prompt, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     encoding='utf-8', errors='replace', timeout=900, check=False)
            exit_code, log = process.returncode, process.stdout
            raw = response.read_text(encoding='utf-8') if response.exists() else ''
            if exit_code: raise ValueError('provider exited ' + str(exit_code))
            obj = admit(parse_json(raw), reviewer, submitted, identity)
            # Refuse a call whose supplied files changed while the provider ran.
            if any(digest(p) != h for p, h in files.items()): raise ValueError('inputs changed during review')
        except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
            error = str(exc)
            obj = None
            if isinstance(exc, subprocess.TimeoutExpired):
                log = exc.stdout or ''
                if isinstance(log, bytes): log = log.decode('utf-8', errors='replace')
        if response.exists(): raw = response.read_text(encoding='utf-8', errors='replace')
        out.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(log, encoding='utf-8', newline='\n')
        raw_path.write_text(raw, encoding='utf-8', newline='\n')
    usage, actual_model = usage_from_log(log)
    receipt = dict(input_digest=key, inputs=files, prompt_digest=hashlib.sha256(prompt.encode('utf-8')).hexdigest(),
                   reviewer=reviewer, requested_model=model, actual_model=actual_model, effort='medium',
                   argv=argv, exit=exit_code, elapsed_seconds=round(time.monotonic() - start, 3), usage=usage,
                   status='admitted' if obj is not None else 'failed', error=error,
                   log=log_path.relative_to(runs).as_posix(), raw=raw_path.relative_to(runs).as_posix())
    if obj is not None:
        atomic_json(out, obj)
        receipt['output_digest'] = digest(out)
        result.update(status='admitted', output_digest=receipt['output_digest'], cached=False)
        print(reviewer + ' ok ' + entry['dossier'], flush=True)
    else:
        print(reviewer + ' FAILED ' + entry['dossier'] + ': ' + str(error), flush=True)
    atomic_json(receipt_path, receipt)
    return result, obj


def confined(runs, relative):
    path = (runs / relative).resolve()
    if not path.is_relative_to(runs.resolve()): raise ValueError('output outside run root: ' + relative)
    return path


def review_entry(entry, args, common, chapter_parts=None):
    paths = common + [confined(args.runs, entry['dossier'])]
    paths += [confined(args.runs, entry['timeline']), confined(args.runs, entry['trace']), confined(args.runs, entry['states'])]
    identity = {k: entry[k] for k in ('dossier', 'policy', 'chapter', 'part', 'scope')}
    prompt = (HERE / 'reviewer-contract.md').read_text(encoding='utf-8')
    prompt += '\nTASK: Review ' + json.dumps(identity) + '.\n'
    prompt += 'Read the dossier, chapter timeline, trace, export and knowledge files below. Output strict JSON only.\n'
    if chapter_parts is not None:
        paths += [confined(args.runs, p['dossier']) for p in chapter_parts]
        paths += [confined(args.runs, p['luna']['output']) for p in chapter_parts]
        paths += [confined(args.runs, p['terra']['output']) for p in chapter_parts if p['terra']['status'] == 'admitted']
        prompt += 'Synthesize ONE whole chapter; part scores are not chapter scores. Reopen full excerpts for cross-part claims.\n'
    prompt += '\n'.join(str(p) for p in paths) + '\n'
    prompt += 'Knowledge (read only): ' + str(args.knowledge) + '\n'
    luna, obj = run_call(entry, 'luna', paths, prompt, args.luna, args.runs)
    result = dict(entry, luna=luna, terra=dict(status='unrun', exit=None))
    if obj is None: return result
    submitted = uncertain(obj)
    if not submitted:
        result['terra'] = dict(status='not_required', exit=None)
        return result
    paths += [confined(args.runs, luna['output'])]
    prompt += '\nTASK (Terra): Recheck ONLY these submitted ids; dispose of each exactly once using the Terra variant.\n'
    prompt += json.dumps(submitted, ensure_ascii=False) + '\n'
    result['terra'], _ = run_call(entry, 'terra', paths, prompt, args.terra, args.runs, submitted)
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('policy', nargs='?', default='all')
    ap.add_argument('parallel', nargs='?', type=int, default=4)
    ap.add_argument('--runs', type=Path, default=HERE / 'runs')
    ap.add_argument('--manifest', type=Path)
    ap.add_argument('--export', type=Path, default=ROOT / 'development/Story.json')
    ap.add_argument('--knowledge', type=Path, default=os.environ.get('RRT_KNOWLEDGE', 'C:/Users/Z/Documents/Projects/Writer/knowledge'))
    ap.add_argument('--luna', default=os.environ.get('RRT_LUNA', 'gpt-6-luna'))
    ap.add_argument('--terra', default=os.environ.get('RRT_TERRA', 'gpt-5.6-terra'))
    args = ap.parse_args()
    args.runs = args.runs.resolve(); args.knowledge = args.knowledge.resolve()
    if args.parallel < 1: ap.error('parallel must be positive')
    if not args.knowledge.is_dir(): ap.error('knowledge directory missing')
    policies = ['trickster_all_romance', 'trickster_villain', 'nontrickster_good', 'hostile'] if args.policy == 'all' else [args.policy]
    entries, chapters = [], []
    common = [args.export.resolve(), HERE / 'reviewer-contract.md', HERE / 'reviewer-schema.json',
              HERE / 'admission.py', HERE / 'review.py', HERE / 'dossier.py', HERE / 'walker.py', HERE / 'policies.json']
    common += sorted(p for p in args.knowledge.rglob('*') if p.is_file())
    for policy in policies:
        path = confined(args.runs, policy + '/dossier-manifest.json')
        manifest = load(path); common.append(path)
        if manifest['policy'] != policy: raise ValueError('policy manifest mismatch')
        for ch in manifest['chapters']:
            base = dict(policy=policy, chapter=ch['chapter'], timeline=ch['timeline'], trace=manifest['trace'], states=manifest['states'])
            for part, dossier in enumerate(ch['parts'], 1): entries.append(dict(base, dossier=dossier, part=part, scope='part'))
            chapters.append(dict(base, dossier=ch['timeline'], part=1, scope='chapter'))
    target = args.manifest or args.runs / 'review-manifest.json'
    # Declare coverage before invoking a provider. Interrupted work stays visible as unrun.
    manifest = dict(schema='rrt-review-run/2', runs_root=os.path.relpath(args.runs, target.parent),
                    entries=[dict(e, luna={'status':'unrun', 'exit':None}, terra={'status':'unrun', 'exit':None}) for e in entries + chapters])
    atomic_json(target, manifest)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        for result in pool.map(lambda e: review_entry(e, args, common), entries):
            results.append(result)
            manifest['entries'] = results + manifest['entries'][len(results):]
            atomic_json(target, manifest)
    for entry in chapters:
        parts = [r for r in results if r['policy'] == entry['policy'] and r['chapter'] == entry['chapter'] and r['scope'] == 'part']
        if all(p['luna']['status'] == 'admitted' and p['terra']['status'] in ('admitted', 'not_required') for p in parts):
            results.append(review_entry(entry, args, common, parts))
        else: results.append(dict(entry, luna={'status':'unrun', 'exit':None}, terra={'status':'unrun', 'exit':None}))
        manifest['entries'] = results + manifest['entries'][len(results):]
        atomic_json(target, manifest)
    success = bool(results) and all(r['luna']['status'] == 'admitted' and r['terra']['status'] in ('admitted', 'not_required') for r in results)
    print('review done' if success else 'review FAILED')
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
