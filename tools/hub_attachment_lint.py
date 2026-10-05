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
    errors = []
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
    required = {'trickster.ever', 'nenio.trickster.visitor', 'nenio.trickster.returned', *reaction.get('Requires', [])}
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
