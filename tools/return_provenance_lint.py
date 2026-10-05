"""E-Q7-11: registered loss-specific returns and their consumer class sweep."""
import json
from pathlib import Path
# eng8-q8a: standalone CLI uses the same route presence declarations as the exporter.
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
# end eng8-q8a

CONTRACT = Path(__file__).with_name('return_provenance_contracts.json')


def contracts():
    return json.loads(CONTRACT.read_text(encoding='utf-8'))


# eng8-q8a: extend the existing strict provenance gate, not a second lifecycle system.
LATEST = CONTRACT.with_name('latest_state_inventory_contracts.json')


def latest_contracts():
    return json.loads(LATEST.read_text(encoding='utf-8'))


def registered_closing_departure(rel, scene, node, index, choice, flag):
    """The sole nominated departure already closes romance on the same answer."""
    p = latest_contracts()['wenduag']['departure_producer']
    return (rel == 'wenduag' and scene == p['scene'] and node == p['node']
            and index == p['choice'] and flag == p['receipt']
            and {'wenduag.closed', p['receipt']} <= set(choice.get('Set', [])))


def integrate_latest_state(story):
    data = latest_contracts()['nenio']
    rel = story.get('Relationships', {}).get('nenio')
    if rel is None:
        return
    rel['UnavailableOverrides'].update(data['overrides'])
    rel['UnavailableFlags'] = list(dict.fromkeys([*rel['UnavailableFlags'], data['runtime_loss']]))
    for key, groups in data['derived'].items():
        story.setdefault('Derived', {})[key] = groups
        story.setdefault('DerivedForbids', {})[key] = [data['runtime_loss']]
    for scene in story.get('Scenes', []):
        for loss, returned in data['overrides'].items():
            if loss in scene.get('ForbidOverrides', {}):
                scene['ForbidOverrides'][loss] = returned
        if scene.get('Relationship') == 'nenio' and scene.get('Owner', '').endswith('Epilogue'):
            scene['Forbids'] = list(dict.fromkeys([*scene.get('Forbids', []), data['runtime_loss']]))
    # Presence predicates were assembled before these loss-specific overrides.
    from storylines import earned_presence
    for name in story.get('Presences', {}):
        if earned_presence.presence_relationship(name) != 'nenio':
            continue
        declaration = story.get('PresenceExceptions', {}).get(name)
        for field, entries in earned_presence.presence_guard_fields('nenio', rel, declaration).items():
            story.setdefault(field, {}).update(entries)


def check_latest_state(story):
    data, errors = latest_contracts(), []
    by = {s['Id']: s for s in story.get('Scenes', [])}
    n = data['nenio']
    rel = story.get('Relationships', {}).get('nenio')
    if rel is not None:
        for loss, returned in n['overrides'].items():
            if rel.get('UnavailableOverrides', {}).get(loss) != returned:
                errors.append('LS nenio: stale loss override ' + loss)
        if n['runtime_loss'] not in rel.get('UnavailableFlags', []):
            errors.append('LS nenio: missing current-body loss')
        for key, groups in n['derived'].items():
            if story.get('Derived', {}).get(key) != groups or story.get('DerivedForbids', {}).get(key) != [n['runtime_loss']]:
                errors.append('LS nenio: incorrect matching return ' + key)
        producer = by.get(n['producer'], {})
        node = next((x for x in producer.get('Nodes', []) if x['Id'] == n['producer_node']), {})
        choices = node.get('Choices', [])
        if len(choices) <= n['producer_choice'] or choices[n['producer_choice']].get('Revive') != n['producer_action']:
            errors.append('LS nenio: paid return must restore the retained original')
        if 'nenio.trickster.returned' not in producer.get('Forbids', []):
            errors.append('LS nenio: historical return must retire the one-shot bargain')
        for sid in n['consumers']:
            if sid not in by:
                errors.append('LS nenio: missing consumer ' + sid)
        for scene in story.get('Scenes', []):
            for loss, returned in n['overrides'].items():
                lift = scene.get('ForbidOverrides', {}).get(loss)
                if lift is not None and lift != returned:
                    errors.append('LS stale loss override ' + scene['Id'] + '/' + loss)
            if scene.get('Relationship') == 'nenio' and scene.get('Owner', '').endswith('Epilogue'):
                if n['runtime_loss'] not in scene.get('Forbids', []):
                    errors.append('LS nenio: ending lacks current-body guard ' + scene['Id'])
                if 'nenio.dead' not in scene.get('Forbids', []):
                    errors.append('LS nenio: ending lacks current native death ' + scene['Id'])
        from storylines import earned_presence
        for name in story.get('Presences', {}):
            if earned_presence.presence_relationship(name) != 'nenio':
                continue
            declaration = story.get('PresenceExceptions', {}).get(name)
            for field, entries in earned_presence.presence_guard_fields('nenio', rel, declaration).items():
                for key, value in entries.items():
                    if story.get(field, {}).get(key) != value:
                        errors.append('LS nenio: stale presence predicate ' + key)
        guest = next((e for book in story.get('Books', {}).values() for e in book.get('Entries', []) if e['Id'] == n['guest']), {})
        route_keys = story.get('DerivedOpenRoutes', {})
        if not any('nenio' in route_keys.get(key, []) for key in guest.get('Requires', [])):
            # The guarded eligibility key can delegate RouteOpen transitively.
            def guarded(key, seen=()):
                if key in seen:
                    return False
                if 'nenio' in route_keys.get(key, []):
                    return True
                groups = story.get('Derived', {}).get(key, [])
                return bool(groups) and all(any(guarded(k, (*seen, key)) for k in g) for g in groups)
            if not any(guarded(k) for k in guest.get('Requires', [])):
                errors.append('LS nenio: Guest List lacks current route availability')
    if 'wenduag' in story.get('Relationships', {}):
        w, e = data['wenduag'], data['wenduag']['prefix']
        if story.get('Derived', {}).get(w['life_return']) != w['life_groups']:
            errors.append('LS wenduag: bodily departure is missing or conflated with romance')
        if story.get('DerivedForbids', {}).get(w['life_return']) != [e + 'unavailable']:
            errors.append('LS wenduag: missing invalid-actor exclusion')
        for key in w['romance_readers']:
            if not {e + 'unavailable', 'wenduag.closed'} <= set(story.get('DerivedForbids', {}).get(key, [])):
                errors.append('LS wenduag: closure retains romance ' + key)
        for sid in (w['refusal'], w['departure']):
            scene = by.get(sid, {})
            if not {'wenduag.closed', 'wenduag.life.available'} <= set(scene.get('Requires', [])) or e + 'unavailable' not in scene.get('Forbids', []):
                errors.append('LS wenduag: missing living closure ending ' + sid)
        p = w['departure_producer']
        node = next((n for n in by.get(p['scene'], {}).get('Nodes', []) if n['Id'] == p['node']), {})
        choices = node.get('Choices', [])
        if len(choices) <= p['choice'] or not {'wenduag.closed', p['receipt']} <= set(choices[p['choice']].get('Set', [])):
            errors.append('LS wenduag: departure lacks its explicit receipt')
        elif any(k in choices[p['choice']].get('Set', []) for k in ('wenduag.committed', 'wenduag.trickster.returned', e + 'returned')):
            errors.append('LS wenduag: departure grants a romantic return')
    return errors
# end eng8-q8a


def integrate(story):
    # eng8-q8a: assembled consumers and the existing presence declaration share one repair.
    integrate_latest_state(story)
    # end eng8-q8a
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
        return check_latest_state(story)  # eng8-q8a: partial route exports still enforce their own inventory.
    # eng8-q8a: the normal strict gate must enforce the new inventory as well.
    data, errors = contracts(), check_latest_state(story)
    # end eng8-q8a
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
                if scene['Id'] not in data['producers'] and data['completed'] in choice.get('Set', []):
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
