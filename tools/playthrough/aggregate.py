"""Aggregate only declared, admitted outputs; missing coverage fails the CLI."""
import argparse
import collections
from pathlib import Path

from admission import METRICS, PENDING, admit, atomic_json, digest, load, resolve, status, uncertain
from review import confined


def artifact(runs, record, reviewer, entry, submitted=None):
    if record.get('status') != 'admitted': raise ValueError(reviewer + ' output ' + record.get('status', 'missing'))
    path = confined(runs, record['output']); receipt = load(confined(runs, record['receipt']))
    if receipt['status'] != 'admitted' or receipt['exit'] != 0: raise ValueError(reviewer + ' failed receipt')
    if receipt['input_digest'] != record['input_digest']: raise ValueError(reviewer + ' input digest mismatch')
    if receipt['output_digest'] != digest(path) or record['output_digest'] != digest(path): raise ValueError(reviewer + ' output digest mismatch')
    if any(digest(p) != h for p, h in receipt['inputs'].items()): raise ValueError(reviewer + ' stale inputs')
    identity = {k: entry[k] for k in ('dossier', 'policy', 'chapter', 'part')}
    if reviewer == 'luna': identity['scope'] = entry['scope']
    return admit(load(path), reviewer, submitted, identity)


def mean(values):
    return round(sum(values) / len(values), 3) if values and all(v is not None for v in values) else None


def aggregate(manifest_path):
    manifest_path = Path(manifest_path)
    manifest = load(manifest_path)
    if manifest['schema'] != 'rrt-review-run/2': raise ValueError('unsupported manifest')
    runs = (manifest_path.parent / manifest['runs_root']).resolve()
    records, cells, errors, characters, reviews = [], [], [], collections.defaultdict(list), []
    seen, chapter_keys, part_keys = set(), set(), set()
    for entry in manifest['entries']:
        key = (entry['policy'], entry['chapter'], entry['scope'], entry['part'])
        if key in seen: raise ValueError('duplicate manifest cell/part')
        seen.add(key)
        if entry['scope'] == 'chapter': chapter_keys.add(key[:2])
        elif entry['scope'] == 'part': part_keys.add(key[:2])
        else: raise ValueError('invalid scope')
        luna, terra, issue = None, None, None
        try:
            luna = artifact(runs, entry['luna'], 'luna', entry)
            submitted = uncertain(luna)
            if submitted: terra = artifact(runs, entry.get('terra', {}), 'terra', entry, submitted)
            elif entry.get('terra', {}).get('status') != 'not_required': raise ValueError('unexpected Terra artifact')
        except (ValueError, KeyError, OSError) as exc:
            issue = str(exc)
            errors.append(dict(policy=entry['policy'], chapter=entry['chapter'], dossier=entry['dossier'], error=issue))
        current = resolve(luna, terra) if luna else []
        verdict = status(current)
        if issue and not verdict['pending']: verdict['chapter_status'] = 'missing_coverage'
        reviews.append(dict(policy=entry['policy'], dossier=entry['dossier'], scope=entry['scope'],
                            current_verdict=verdict, raw_verdict=luna['verdict'] if luna else None,
                            score_reviewer='luna', error=issue))
        for f in current:
            records.append(dict(f, chapter=entry['chapter'], policy=entry['policy'], dossier=entry['dossier'], scope=entry['scope'],
                                input_digest=entry['luna'].get('input_digest')))
        if luna:
            for c in luna['characters']:
                characters[c['character_id']].append(dict(c, policy=entry['policy'], dossier=entry['dossier']))
        if entry['scope'] == 'chapter':
            cells.append(dict(policy=entry['policy'], chapter=entry['chapter'],
                              disposition=luna['chapter_disposition'] if luna else 'missing',
                              metrics=luna['chapter_metrics'] if luna else None,
                              fun=luna['verdict']['fun'] if luna else None,
                              feels_like_part_of_the_game=luna['verdict']['feels_like_part_of_the_game'] if luna else None,
                              status=verdict['chapter_status'], score_reviewer='luna'))
    for key in sorted(part_keys - chapter_keys):
        errors.append(dict(policy=key[0], chapter=key[1], error='chapter synthesis undeclared'))
    if not cells: errors.append(dict(error='no declared chapter coverage'))
    for cell in cells:
        cell_records = [f for f in records if f['policy'] == cell['policy'] and f['chapter'] == cell['chapter']]
        current_status = status(cell_records)['chapter_status']
        cell_errors = [e for e in errors if e.get('policy') == cell['policy'] and e.get('chapter') == cell['chapter']]
        cell['status'] = 'missing_coverage' if cell_errors and current_status == 'pass' else current_status
    policies = {}
    for policy in sorted({c['policy'] for c in cells}):
        measured = [c for c in cells if c['policy'] == policy and c['disposition'] != 'no_mod_content']
        policies[policy] = {m: mean([c['metrics'][m]['score'] if c['metrics'] else None for c in measured]) for m in METRICS}
    overall = {m: mean([p[m] for p in policies.values()]) for m in METRICS}
    minimum = {m: min([c['metrics'][m]['score'] for c in cells if c['metrics'] and c['metrics'][m]['score'] is not None], default=None) for m in METRICS}
    counts = status(records)
    complete = not errors and not counts['pending']
    return runs, dict(schema='rrt-review-summary/2', complete=complete, errors=errors, findings=records,
                      counts=counts, characters=dict(characters), reviews=reviews, chapter_cells=cells,
                      policy_means=policies, overall=overall, minimum_chapter=minimum,
                      coverage=dict(expected=len(cells), reviewed=sum(c['disposition'] == 'reviewed' for c in cells),
                                    no_mod_content=sum(c['disposition'] == 'no_mod_content' for c in cells),
                                    missing=sum(c['disposition'] == 'missing' for c in cells)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, default=Path(__file__).resolve().parent / 'runs/review-manifest.json')
    args = ap.parse_args()
    runs, summary = aggregate(args.manifest)
    atomic_json(runs / 'review-findings.json', summary['findings'])
    atomic_json(runs / 'review-summary.json', summary)
    lines = ['# Playthrough review summary', '', 'Coverage: ' + ('complete' if summary['complete'] else 'INCOMPLETE'),
             '', '| Policy | Chapter | Disposition | Current status | Flow | Appetite | Gameplay seam |',
             '|---|---|---|---|---|---|---|']
    for c in summary['chapter_cells']:
        scores = [c['metrics'][m]['score'] if c['metrics'] else None for m in METRICS]
        lines.append('| ' + ' | '.join(str(v) for v in [c['policy'], c['chapter'], c['disposition'], c['status']] + scores) + ' |')
    lines += ['', 'Counts from current dispositions: ' + str(summary['counts']),
              'Equal chapter means within policy, then equal policy means: ' + str(summary['overall']),
              'Minimum chapter scores: ' + str(summary['minimum_chapter']),
              'Scores remain attributed to Luna; Terra changes dispositions, not scores.', '']
    lines += ['- ' + str(e) for e in summary['errors']]
    (runs / 'REVIEW-SUMMARY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    print('\n'.join(lines))
    return 0 if summary['complete'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
