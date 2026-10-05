"""E-Q7-11: registered loss-specific returns and their consumer class sweep."""
import json
from pathlib import Path

CONTRACT = Path(__file__).with_name('return_provenance_contracts.json')


def contracts():
    return json.loads(CONTRACT.read_text(encoding='utf-8'))


def integrate(story):
    if 'camellia' not in story['Relationships']:
        return
    data = contracts()
    rel = story['Relationships']['camellia']
    rel['UnavailableOverrides'].update(data['overrides'])
    rel['TricksterAccess']['killed_by_commander']['Returned'] = data['completed']
    story.setdefault('Derived', {}).update(data['derived'])
    from storylines import earned_presence
    # eng7-integ: refresh the serialized acquisition exception with the new
    # loss-specific returns; a full RouteOpen guard would block the paid actor
    # before she can complete the physical reckoning.
    for name in story.get('Presences', {}):
        if earned_presence.presence_relationship(name) != 'camellia':
            continue
        declaration = story.get('PresenceExceptions', {}).get(name)
        for field, entries in earned_presence.presence_guard_fields('camellia', rel, declaration).items():
            story.setdefault(field, {}).update(entries)
    # A retained-death resurrection clears current DEAD. Its historical return
    # never lifts a later DEAD; the coffin copy answers only the native execution.
    for scene in story['Scenes']:
        for loss, returned in data['overrides'].items():
            if loss in scene.get('ForbidOverrides', {}):
                scene['ForbidOverrides'] = {**scene['ForbidOverrides'], loss: returned}
        if scene.get('Owner', '').endswith('Epilogue') and scene.get('Relationship') == 'camellia' and 'camellia.committed' in scene.get('Requires', []):
            for loss, returned in data['overrides'].items():
                if loss not in scene.get('Forbids', []):
                    scene['Forbids'] = [*scene.get('Forbids', []), loss]
                scene['ForbidOverrides'] = {**scene.get('ForbidOverrides', {}), loss: returned}
        for node in scene['Nodes']:
            for choice in node['Choices']:
                if scene['Id'] in data['producers'] and data['generic'] in choice.get('Set', []):
                    choice['Set'] = list(dict.fromkeys([*choice['Set'], data['completed']]))
        if scene['Id'] in data['veiled_scenes']:
            scene['Requires'] = list(dict.fromkeys([*scene['Requires'], data['available']]))
        if scene['Id'] in data['dispatch_scenes']:
            for node in scene['Nodes']:
                for choice in node['Choices']:
                    # Correct both positive dispatches and complementary fallbacks.
                    for field in ('Requires', 'Forbids'):
                        choice[field] = [data['available'] if k == data['generic'] else k for k in choice.get(field, [])]
    for key in data['due_keys']:
        if key in story.get('Derived', {}):
            story['Derived'][key] = [[data['available'] if k == data['generic'] else k for k in g] for g in story['Derived'][key]]


def check(story):
    if 'camellia' not in story.get('Relationships', {}):
        return []
    data, errors = contracts(), []
    rel = story['Relationships']['camellia']
    for loss, returned in data['overrides'].items():
        if rel.get('UnavailableOverrides', {}).get(loss) != returned:
            errors.append('RP camellia: %s needs %s' % (loss, returned))
    if rel.get('TricksterAccess', {}).get('killed_by_commander', {}).get('Returned') != data['completed']:
        errors.append('RP killed access conflates return histories')
    for key, value in data['derived'].items():
        if story.get('Derived', {}).get(key) != value:
            errors.append('RP incorrect provenance reader ' + key)
    by = {s['Id']: s for s in story['Scenes']}
    # eng8-q8d: registration is node-scoped; the ritual must still establish
    # its native execution and paid breath before the folded agreement.
    folded = data.get('eng8-q8d', {}).get('coffin_completion_nodes', {})
    for sid, nodes in folded.items():
        scene = by.get(sid, {})
        if (data['producer_inputs'][0] not in scene.get('Requires', [])
                or not any(data['producer_inputs'][1] in c.get('Set', [])
                           for n in scene.get('Nodes', []) for c in n['Choices'])
                or not set(nodes) <= {n['Id'] for n in scene.get('Nodes', [])}):
            errors.append('RP folded coffin lacks matching ritual: ' + sid)
    # end eng8-q8d
    if data['completed'] in story.get('Derived', {}) or data['completed'] in story.get('Latches', {}):
        errors.append('RP completed coffin return must be authored by its own producer')
    for sid in data['producers'] + data['veiled_scenes'] + data['dispatch_scenes']:
        if sid not in by:
            errors.append('RP missing consumer/producer ' + sid)
    for sid in data['producers']:
        if sid in by and not set(data['producer_inputs']) <= set(by[sid].get('Requires', [])):
            errors.append('RP coffin completion lacks matching loss/ritual: ' + sid)
    for scene in story['Scenes']:
        for loss, returned in data['overrides'].items():
            lift = scene.get('ForbidOverrides', {}).get(loss)
            if lift and lift != returned:
                errors.append('RP stale loss override %s/%s' % (scene['Id'], loss))
        if scene['Id'] in data['veiled_scenes'] and data['available'] not in scene['Requires']:
            errors.append('RP veiled consumer lacks current completed return: ' + scene['Id'])
        for node in scene['Nodes']:
            for i, choice in enumerate(node['Choices']):
                loc = '%s/%s[%d]' % (scene['Id'], node['Id'], i)
                if scene['Id'] in data['producers'] and data['generic'] in choice.get('Set', []) and data['completed'] not in choice['Set']:
                    errors.append('RP missing completion producer ' + loc)
                # eng8-q8d: only the registered folded agreement can complete a return.
                if (scene['Id'] not in data['producers'] and node['Id'] not in folded.get(scene['Id'], [])
                        and data['completed'] in choice.get('Set', [])):
                    errors.append('RP unauthorized coffin completion producer ' + loc)
                if scene['Id'] in data['dispatch_scenes'] and data['generic'] in choice.get('Requires', []) + choice.get('Forbids', []):
                    errors.append('RP stale dispatch/fallback ' + loc)
    for key in data['due_keys']:
        groups = story.get('Derived', {}).get(key, [])
        if not groups or any(data['available'] not in g or data['generic'] in g for g in groups):
            errors.append('RP stale card reader ' + key)
    return errors


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--story', default=str(CONTRACT.parents[1] / 'development/Story.json'))
    args = parser.parse_args()
    errors = check(json.loads(Path(args.story).read_text(encoding='utf-8')))
    for error in errors:
        print(error)
    print('return provenance: %d hard' % len(errors))
    raise SystemExit(bool(errors))
