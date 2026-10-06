"""eng7-f2: reject new reviews without hiding unresolved editorial findings.

The F2 task permits markup repairs and asks strict mode to reject *new*
findings. Its existing editorial reviews remain visible in player_text.review;
the baseline follows diagnostic identity and rejects additional occurrences.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

BASELINE = Path(__file__).with_suffix('.json')


def fingerprint(row, text):
    identity = [row[key] for key in ('scene', 'location', 'code')]
    return hashlib.sha256(json.dumps(identity, ensure_ascii=False).encode('utf-8')).hexdigest()


def new_findings(story, rows, policy=None, therapy_counts=None):
    from tools.player_text_lint import surfaces
    policy = json.loads(BASELINE.read_text(encoding='utf-8')) if policy is None else policy
    text = {(sid, location): value for sid, location, value, _, _ in surfaces(story)}
    remaining = Counter(policy.get('findings', {}))
    hard = []
    for row in rows:
        key = fingerprint(row, text[row['scene'], row['location']])
        if remaining[key] > 0:
            remaining[key] -= 1
        else:
            hard.append({**row, 'severity': 'hard'})
    # Counts remain a request for human review, not an automatic voice verdict.
    # Strict mode nevertheless rejects an increase in the registered baseline.
    for route, count in sorted((therapy_counts or {}).items()):
        budget = policy.get('therapy_counts', {}).get(route, 0)
        if count > budget:
            hard.append(dict(scene='therapy/' + route, location='budget',
                             code='therapy-budget-increase', start=0, end=0,
                             match=route, count=count, budget=budget, severity='hard'))
    return hard
