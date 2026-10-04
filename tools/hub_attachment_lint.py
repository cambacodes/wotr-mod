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


def integrate(story):
    """Authored attachment only: preserve scene identity, native lists and all route gates."""
    for key in HUBS:
        story['Presences'][key]['ReactionScenes'] = list(REACTIONS)
    errors = lint(story)
    if errors:
        raise ValueError('; '.join(errors))


def lint(story):
    scenes = {s['Id']: s for s in story['Scenes']}
    errors = []
    for key, presence in story.get('Presences', {}).items():
        entries = presence.get('ReactionScenes', [])
        if entries and key not in HUBS:
            errors.append('unreviewed reaction hub: ' + key)
        if key in HUBS and entries != list(REACTIONS):
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
    for key in HUBS:
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
