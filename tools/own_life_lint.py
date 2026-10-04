"""E-Q7-06: explicit own-life contracts, independent of romance eligibility.

These contracts cover nominated own-route consumers; q6a owns cross-route L1/L4.
No loss is waived except by its registered return. Closed living women retain
independent consequences; only continuing romance reads closure.
"""
import json
from pathlib import Path

CONTRACT = Path(__file__).with_name('own_life_contracts.json')


def contracts():
    return json.loads(CONTRACT.read_text(encoding='utf-8'))


def life_fields(person, spec):
    key = spec['key']
    derived = {key: [['chapter_one'], ['chapter_later']]}
    forbids = {key: []}
    for loss, returned in spec['losses'].items():
        blocked = key + '.blocked.' + loss
        derived[blocked] = [[loss]]
        forbids[key].append(blocked)
        if returned:
            forbids[blocked] = [returned]
    return derived, forbids


def targets(story, site):
    scene = next((s for s in story.get('Scenes', []) if s['Id'] == site['scene']), None)
    if scene is None:
        return []
    if 'node' not in site:
        return [scene]
    node = next((n for n in scene['Nodes'] if n['Id'] == site['node']), None)
    if node is None:
        return []
    if 'paragraph' in site:
        i = site['paragraph']
        return node.get('Paragraphs', [])[i:i + 1]
    if 'choices' in site:
        return [node['Choices'][i] for i in site['choices']]
    return [node]


def integrate(story):
    data = contracts()
    if 'minagho_chivarro' in story['Relationships']:
        story.setdefault('Derived', {}).update(data['derived'])
    for person, spec in data['people'].items():
        if spec['relationship'] not in story['Relationships']:
            continue
        derived, forbids = life_fields(person, spec)
        story.setdefault('Derived', {}).update(derived)
        story.setdefault('DerivedForbids', {}).update(forbids)
    for site in data['sites']:
        for target in targets(story, site):
            for field in ('Requires', 'Forbids'):
                target[field] = list(dict.fromkeys([*target.get(field, []), *site.get(field, [])]))
    # Stale arrival must select the existing alone/loss variant, never stage a corpse.
    for site in data['rewires']:
        for target in targets(story, site):
            for field in ('Requires', 'Forbids'):
                target[field] = [site['to'] if k == site['from'] else k for k in target.get(field, [])]


def check(story):
    data, errors = contracts(), []
    if 'minagho_chivarro' in story.get('Relationships', {}):
        for key, value in data['derived'].items():
            if story.get('Derived', {}).get(key) != value:
                errors.append('OL stale arrival reader ' + key)
    for person, spec in data['people'].items():
        if spec['relationship'] not in story.get('Relationships', {}):
            continue
        derived, forbids = life_fields(person, spec)
        for field, expected in (('Derived', derived), ('DerivedForbids', forbids)):
            for key, value in expected.items():
                if story.get(field, {}).get(key) != value:
                    errors.append('OL life reader %s: incorrect %s' % (key, field))
    for site in data['sites'] + data['rewires']:
        if site['relationship'] not in story.get('Relationships', {}):
            continue
        found = targets(story, site)
        if not found:
            errors.append('OL missing consumer ' + site['scene'])
        for target in found:
            if 'to' in site:
                if site['from'] in target.get('Requires', []) + target.get('Forbids', []) or site['to'] not in target.get('Requires', []) + target.get('Forbids', []):
                    errors.append('OL stale arrival consumer ' + site['scene'])
            for field in ('Requires', 'Forbids'):
                if not set(site.get(field, [])) <= set(target.get(field, [])):
                    errors.append('OL %s: missing %s %s' % (site['scene'], field, site[field]))
    return errors


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--story', default=str(CONTRACT.parents[1] / 'development/Story.json'))
    args = parser.parse_args()
    errors = check(json.loads(Path(args.story).read_text(encoding='utf-8')))
    for error in errors:
        print(error)
    print('own life: %d hard' % len(errors))
    raise SystemExit(bool(errors))
