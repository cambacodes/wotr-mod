"""eng7-f6b: archive parity for the reviewed Kiana text-only cue contracts.

The runtime validates these exact parents, continuations, lists and action
shapes. Presentation keeps the original cue, including native history readers.
No condition, outcome, sequence entry, or native quest action is rewritten.
"""
import json
from functools import lru_cache
from pathlib import Path
import re
from zipfile import ZipFile

from tools.game_blueprints import find_bindings, game_dir, text_key

ROOT = Path(__file__).resolve().parents[1]


def contracts():
    return json.loads((ROOT / "tools/kiana_native_contracts.json").read_text(encoding="utf-8"))


def parent_type(target, spec):
    """Verifier union stays narrow: only the two reviewed sequence parents qualify."""
    default = 'BlueprintCue|BlueprintAnswer|BlueprintDialog'
    policy = contracts().get(target)
    if policy and spec.get('Parent') == policy['Parent'] and policy.get('ParentType') == 'BlueprintCueSequence':
        return default + '|BlueprintCueSequence'
    return default


def runtime_declaration(target, policy):
    def array(values):
        return 'new[] { ' + ', '.join('"' + v + '"' for v in values) + ' }' if values else 'Array.Empty<string>()'
    args = ['degradeOnRefusal: false', 'parent: "' + policy['Parent'] + '"',
            'dialog: "' + policy['Dialog'] + '"', 'alsoParents: ' + array(policy['AlsoParents']), 'textOnly: true']
    for field, option in [('Continue', 'continueTo'), ('Answers', 'answers'), ('OnShow', 'onShow'), ('OnStop', 'onStop')]:
        if policy[field]:
            args.append(option + ': ' + array(policy[field]))
    return '["' + target + '"] = new Evidence("", "", "' + policy['Key'] + '", ' + ', '.join(args) + ')'


def expected():
    result = {}
    source = (ROOT / 'src/NativeEpilogueEdit.cs').read_text(encoding='utf-8-sig')
    policies = contracts()
    runtime_targets = set(re.findall(r'\["([a-f0-9]{32})"\] = new Evidence\([^\n]*textOnly: true', source))
    if runtime_targets != set(policies):
        raise ValueError('eng7-f6b: text-only runtime inventory differs from archive contracts')
    for target, policy in policies.items():
        if runtime_declaration(target, policy) not in source:
            raise ValueError('eng7-f6b: runtime cue policy differs: ' + target)
        result[target] = 'BlueprintCue'
        result[policy['Dialog']] = 'BlueprintDialog'
        if policy.get('SpeakerSource'):
            result[policy['SpeakerSource']] = 'BlueprintCue'
        for parent, kind in zip([policy['Parent'], *policy['AlsoParents']], [policy['ParentType'], *policy['AlsoParentTypes']]):
            result.setdefault(parent, kind)
    return result


def action_shape(action):
    kind = action['$type'].split(', ')[-1]
    guid = next((v.removeprefix('!bp_') for v in action.values() if isinstance(v, str) and v.startswith('!bp_')), None)
    return kind + (':' + guid if guid else '')


def check(target, spec, found):
    policy = contracts()[target]
    data = found[target]['data']
    error = 'eng7-f6b: native cue behavior differs from reviewed runtime policy: ' + target
    if (spec.get('Parent') != policy['Parent'] or spec.get('Dialog') != policy['Dialog']
            or spec.get('Key') != policy['Key'] or text_key(data.get('Text')) != policy['Key']
            or data.get('Components') != [] or data.get('ShowOnce') is not False
            or data.get('ShowOnceCurrentDialog') is not False or not isinstance(data.get('Conditions'), dict)
            or data.get('Continue') != dict(Cues=['!bp_' + g for g in policy['Continue']], Strategy='First')
            or data.get('Answers') != ['!bp_' + g for g in policy['Answers']]
            or [action_shape(a) for a in data.get('OnShow', {}).get('Actions', [])] != policy['OnShow']
            or [action_shape(a) for a in data.get('OnStop', {}).get('Actions', [])] != policy['OnStop']):
        raise ValueError(error)
    if policy.get('SpeakerSource'):
        source = found[policy['SpeakerSource']]
        if (source['path'].rsplit('/', 1)[0] != found[target]['path'].rsplit('/', 1)[0]
                or source['data']['Speaker'].get('m_Blueprint') != '!bp_' + policy['InheritedSpeaker']):
            raise ValueError(error)
    for parent in [policy['Parent'], *policy['AlsoParents']]:
        record = found[parent]
        original = record['data']
        if record['type'] in {'BlueprintCue', 'BlueprintSequenceExit'}:
            cues = original.get('Continue', {}).get('Cues', [])
        elif record['type'] == 'BlueprintAnswer':
            cues = original.get('NextCue', {}).get('Cues', [])
        elif record['type'] == 'BlueprintDialog':
            cues = original.get('FirstCue', {}).get('Cues', [])
        elif record['type'] == 'BlueprintCueSequence':
            cues = original.get('Cues', [])
        else:
            raise ValueError(error)
        if cues.count('!bp_' + target) != 1:
            raise ValueError(error)


@lru_cache(maxsize=1)
def native_context():
    """Native conversation evidence for L1; romance closure does not silence NPC dialogue.

    Only the reviewed text-only targets qualify. Native speakers keep their
    physical appearance; other mentions remain subject to the staging check.
    New women absent from the original conversation receive no exemption.
    """
    policies = contracts()
    found = find_bindings(game_dir() / 'blueprints.zip', expected())
    units = {(found[g]['data']['Speaker'].get('m_Blueprint') or '').removeprefix('!bp_') for g in policies} - {''}
    actors = find_bindings(game_dir() / 'blueprints.zip', {g: 'BlueprintUnit' for g in units})
    strings = json.loads((game_dir() / 'Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings']
    def localized(value):
        key = text_key(value) or (value or {}).get('stringkey')
        text = strings.get(key, '')
        return text.get('Text', '') if isinstance(text, dict) else text
    names = {g: localized(r['data']['m_DisplayName']) or localized(r['data']['LocalizedName']) for g, r in actors.items()}
    directories = {r['path'].rsplit('/', 1)[0] + '/' for g, r in found.items() if g in policies}
    conversations = {d: [] for d in directories}
    with ZipFile(game_dir() / 'blueprints.zip') as archive:
        for path in archive.namelist():
            directory = path.rsplit('/', 1)[0] + '/'
            if directory not in directories or not path.endswith('.jbp'):
                continue
            data = json.loads(archive.read(path))['Data']
            conversations[directory].append(localized(data.get('Text')))
    def speaker(target):
        unit = found[target]['data']['Speaker'].get('m_Blueprint')
        if not unit and policies[target].get('SpeakerSource'):
            # These four native null-speaker cues use the dialog's initiating
            # Seelah. Cue_0029 explicitly confirms her identity in the same
            # conversation; Arsinoe's later speech confers no staging exemption.
            check(target, policies[target], found)
            unit = found[policies[target]['SpeakerSource']]['data']['Speaker']['m_Blueprint']
        name = names.get((unit or '').removeprefix('!bp_'))
        return {name} if name else set()
    return {g: dict(Found=found, Mentions=' '.join(conversations[found[g]['path'].rsplit('/', 1)[0] + '/']),
                    Speakers=speaker(g))
            for g in policies}
