"""Aggregate Luna + Terra checkpoint reviews into one report (runs/REVIEW-SUMMARY.md + review-findings.json).
Terra's verdict replaces Luna's uncertain findings for the same dossier (kept/revised findings in, dropped out)."""
import collections, glob, json, os, re, sys
rows, per_ch, kinds, forms, chars = [], [], collections.Counter(), collections.Counter(), collections.defaultdict(list)
for f in sorted(glob.glob('runs/*/review/*.luna.json')):
    luna = json.load(open(f, encoding='utf-8'))
    terra_path = f.replace('.luna.json', '.terra.json')
    findings = [x for x in luna.get('findings', []) if x.get('certainty') != 'uncertain']
    if os.path.exists(terra_path):
        findings += json.load(open(terra_path, encoding='utf-8')).get('findings', [])
    policy = f.split(os.sep)[0].split('/')[1] if '/' in f else f.split(os.sep)[1]
    dossier = os.path.basename(f).replace('.luna.json', '')
    v = luna.get('verdict', {})
    per_ch.append((policy, dossier, (v.get('fun') or {}).get('score'), (v.get('feels_like_part_of_the_game') or {}).get('score'), v.get('chapter_status')))
    for x in findings:
        x = dict(x, policy=policy, dossier=dossier); rows.append(x)
        kinds[(x.get('kind'), x.get('severity'))] += 1
        if x.get('kind') == 'gameplay_integration': forms[x.get('recommended_form')] += 1
    for c in luna.get('characters', []) or []:
        name = c.get('character') or c.get('id') or c.get('name')
        if name: chars[name].append((policy, dossier, c))
json.dump(rows, open('runs/review-findings.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
avg = lambda xs: round(sum(xs) / len(xs), 1) if xs else None
out = ['# Playthrough review summary (Luna gpt-6-luna medium + Terra gpt-5.6-terra medium)', '']
out.append('| Policy | Dossiers | Avg fun | Avg feels-like-game | Hard | Major | Minor |'); out.append('|---|---|---|---|---|---|---|')
for p in sorted({r[0] for r in per_ch}):
    pr = [r for r in per_ch if r[0] == p]; pf = [x for x in rows if x['policy'] == p]
    out.append(f"| {p} | {len(pr)} | {avg([r[2] for r in pr if r[2]])} | {avg([r[3] for r in pr if r[3]])} | "
               f"{sum(1 for x in pf if x.get('severity')=='hard')} | {sum(1 for x in pf if x.get('severity')=='major')} | {sum(1 for x in pf if x.get('severity')=='minor')} |")
out += ['', '## Findings by kind and severity', '']
for (k, s), n in sorted(kinds.items(), key=lambda t: -t[1]): out.append(f'- {k} / {s}: {n}')
out += ['', '## Gameplay integration: recommended forms', '']
for k, n in forms.most_common(): out.append(f'- {k}: {n}')
out += ['', '## Lowest-scoring checkpoints (feels like part of the game)', '']
for r in sorted([r for r in per_ch if r[3]], key=lambda r: r[3])[:12]: out.append(f'- {r[0]}/{r[1]}: feel {r[3]}, fun {r[2]}, {r[4]}')
out += ['', '## Hard findings', '']
for x in [x for x in rows if x.get('severity') == 'hard'][:60]:
    out.append(f"- [{x['policy']}/{x['dossier']}] {x.get('kind')} {x.get('scene')}/{x.get('node')}: {str(x.get('claim'))[:220]}")
open('runs/REVIEW-SUMMARY.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('\n'.join(out[:40]))
