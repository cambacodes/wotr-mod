"""E-Q7-29: reviewed inheritance of native reactions by returned visitor hubs."""
import json
from pathlib import Path

NENIO_LIST = '1ab909cc3a6194840b1475b99547c263'
REACTIONS = (
    'nocticula.trickster.reaction.nenio',
    'eritrice.trickster.react.nenio_motion',
    'eritrice.trickster.react.nenio_tabled',
    'areelu.trickster.react.nenio_two_drafts',
    'melazmera.trickster.react.nenio_specimen',
)
HUBS = ('nenio.presence', 'nenio.presence.arcade')
# eng7-f3: the siege-camp visitor offers only the earned Ch6 shadow reaction.
CH6_HUB = 'nenio.presence.threshold'
HUB_REACTIONS = {**dict.fromkeys(HUBS, REACTIONS), CH6_HUB: REACTIONS[:1]}
# end eng7-f3


# eng8-q8f: manual reading is never an in-world entry witness.
def gameplay_entry_lint(story):
    contract = json.loads((Path(__file__).with_name('gameplay_entry_inventory_contracts.json')).read_text())
    scenes = {s['Id']: s for s in story['Scenes']}
    if (contract['scope'] not in story.get('Relationships', {})
            and not any(s.get('Relationship') == contract['scope'] for s in scenes.values())):
        return []  # Other-route unit fixtures carry no Terendelev inventory.
    errors = []
    for row in contract['entries']:
        for suffix, hub in zip(('', '_awning'), contract['hubs']):
            sid = row['scene'] + suffix
            scene = scenes.get(sid, {})
            presence = story.get('Presences', {}).get(hub, {})
            other = row['scene'] + ('_awning' if not suffix else '')
            if (not scene.get('Entry') or scene.get('ManualOnly') or scene.get('Remote')
                    or scene.get('ContactUnit') != contract['unit']
                    or scene.get('InteractionHub') != hub or scene.get('Areas') != [contract['area']]
                    or scene.get('Chapters') != [5]
                    or contract['return'] not in scene.get('Requires', [])
                    or other not in scene.get('Forbids', [])
                    or presence.get('Dialog') != 'hub' or presence.get('Unit') != contract['unit']
                    or contract['return'] not in presence.get('Requires', [])
                    or (suffix and 'terendelev.presence.failed' not in scene.get('Requires', []))):
                errors.append('missing earned gameplay entry: ' + sid + ' (' + ','.join(row['findings']) + ')')
    for scene in scenes.values():
        # Chapter contradictions are save-safe retired manuscripts, not live delivery debt.
        retired = ('chapter_later' in scene.get('Forbids', []) and scene.get('MinChapter', 1) >= 2)
        native_entry = bool(scene.get('Entry') and scene.get('AnswerLists') and not scene.get('Remote'))
        hub = story.get('Presences', {}).get(scene.get('InteractionHub'), {})
        contact_entry = bool(scene.get('Entry') and not scene.get('Remote')
                             and scene.get('ContactUnit') and hub.get('Dialog') == 'hub'
                             and hub.get('Unit') == scene.get('ContactUnit'))
        if (scene.get('Relationship') == contract['scope'] and scene.get('ManualOnly') and not retired
                and not scene.get('Owner', '').endswith('Epilogue')
                and not native_entry and not contact_entry):
            errors.append('substantive ManualOnly scene has no gameplay entry: ' + scene['Id'])
    return errors
# end eng8-q8f


def integrate(story):
    """Authored attachment only: preserve scene identity, native lists and all route gates."""
    # eng7-f3
    for key, reactions in HUB_REACTIONS.items():
        story['Presences'][key]['ReactionScenes'] = list(reactions)
    # end eng7-f3
    errors = lint(story)
    if errors:
        raise ValueError('; '.join(errors))


def lint(story):
    scenes = {s['Id']: s for s in story['Scenes']}
    errors = gameplay_entry_lint(story)  # eng8-q8f: build and CLI enforce nominated delivery rows.
    for key, presence in story.get('Presences', {}).items():
        entries = presence.get('ReactionScenes', [])
        if entries and key not in HUB_REACTIONS:  # eng7-f3
            errors.append('unreviewed reaction hub: ' + key)
        if key in HUB_REACTIONS and entries != list(HUB_REACTIONS[key]):  # eng7-f3
            errors.append('missing, reordered or duplicate reactions: ' + key)
        for sid in entries:
            scene = scenes.get(sid, {})
            if (sid not in REACTIONS or not scene.get('Reaction') or scene.get('Owner') != 'Nenio'
                    or scene.get('AnswerLists') != [NENIO_LIST] or scene.get('InteractionHub')
                    or scene.get('Remote') or scene.get('ContactUnit')):
                errors.append('invalid native reaction attachment: ' + key + '/' + sid)
        if entries and (presence.get('Dialog') != 'hub'
                        or 'nenio.trickster.visitor' not in presence.get('Requires', [])
                        or 'trickster.ever' not in presence.get('Requires', [])):
            errors.append('unearned visitor hub: ' + key)
    # eng7-f3: reject a free, misplaced or broadened Chapter 6 delivery.
    presence = story.get('Presences', {}).get(CH6_HUB, {})
    reaction = scenes.get(REACTIONS[0], {})
    required = {'trickster.ever', 'nenio.trickster.visitor', 'nenio.trickster.returned', *(f for f in reaction.get('Requires', []) if f != 'nocticula.present_now')}
    # The Nenio hub can remain while Nocticula's optional reaction is unavailable.
    if (not required <= set(presence.get('Requires', []))
            or not {'nenio.closed', 'nenio.dissolved', REACTIONS[0], 'sacrifice'} <= set(presence.get('Forbids', []))
            or presence.get('MinChapter') != 6 or presence.get('MaxChapter') != 6
            or presence.get('Area') != '10c4b0e2af186ba46ab4d238d00a40a8'
            or presence.get('Unit') != '49e6676f68337114985a22bd548a8a4d'
            or presence.get('At') != dict(NearUnit='a609ed9b2205d034bb3bb04d2a255681', Side='right', Distance=2.5)):
        errors.append('invalid earned Ch6 visitor window: ' + CH6_HUB)
    # end eng7-f3
    for key in HUB_REACTIONS:
        if key not in story.get('Presences', {}):
            errors.append('missing visitor: ' + key)
    return errors


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--story', default=str(Path(__file__).resolve().parents[1] / 'development/Story.json'))
    args = parser.parse_args()
    errors = lint(json.loads(Path(args.story).read_text(encoding='utf-8-sig')))
    for error in errors:
        print('HARD ' + error)
    print('hub attachment lint: %d hard' % len(errors))
    raise SystemExit(bool(errors))
