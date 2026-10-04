"""E-Q7-10 native evidence acceptance, using the q6b registry (not L1-L6).

Checks cited producer types, recorded answers, chapter/path provenance and exact
exported reader contracts. The JSON also supplies native observations to the
required C# acceptance suite. No desired composite facts are fixture inputs.
"""
import json
from pathlib import Path
from zipfile import ZipFile

from tools.game_blueprints import blueprint_type, game_dir

EXPECTATIONS = Path(__file__).with_name('native_fact_inventory_expectations.json')


def verify_inventory(payload, archive=None, expectations=None):
    spec = expectations or json.loads(EXPECTATIONS.read_text())
    for witness in spec['witnesses']:
        name, reader, expected = witness['flag'], witness['reader'], witness['value']
        if payload.get(reader, {}).get(name) != expected:
            raise ValueError('Native fact inventory reader drift: ' + name)
        if witness.get('historical') and name not in payload.get('PermanentEtudes', []) and not name.startswith('ascend_'):
            raise ValueError('Native fact inventory lost completed history: ' + name)
        if not (1 <= witness['first_chapter'] <= witness['last_chapter'] <= 6):
            raise ValueError('Native fact inventory invalid producer window: ' + name)
    with ZipFile(archive or game_dir() / 'blueprints.zip') as z:
        for witness in spec['witnesses']:
            name = witness['flag']
            for source in witness['sources']:
                record = json.loads(z.read(source['path']))
                if record['AssetId'] != source['guid'] or blueprint_type(record['Data']) != source['type']:
                    raise ValueError('Native fact inventory producer drift: ' + name)
                for token in source.get('required_tokens', []):
                    if token not in json.dumps(record['Data']):
                        raise ValueError('Native fact inventory producer condition/action drift: ' + name)
    scenes = {s['Id']: s for s in payload['Scenes']}
    for finding in spec['findings']:
        if finding['scene'] not in scenes and finding['status'] != 'no_change_needed':
            raise ValueError('Native fact inventory missing consumer: ' + finding['id'])
    # Only the nominated continuation: L1-L6 and general route checks remain q6a-owned.
    for scene in scenes.values():
        if scene['Id'].startswith('minachiv.') and 'chivarro.searching' in scene.get('Requires', []):
            raise ValueError('Native fact inventory: Azata-only searching is mandatory in ' + scene['Id'])
    if payload['Derived'].get('minachiv.reunion_history') != [
            ['chivarro.searching'], ['minagho_chivarro.trickster.reunited']]:
        raise ValueError('Native fact inventory: missing earned Trickster reunion alternative')
    # Chapter constraints concern the production of history, not its later recall.
    for consumer in spec['producer_requirements']:
        if consumer['first_chapter'] > scenes[consumer['scene']]['MaxChapter']:
            raise ValueError('Native fact inventory: producer occurs after consumer window: ' + consumer['scene'])
        if consumer['current_path'] not in consumer['producer_paths']:
            if consumer.get('earned_alternative') not in {
                    f for group in payload['Derived'].get(consumer['predicate'], []) for f in group}:
                raise ValueError('Native fact inventory: incompatible native path: ' + consumer['scene'])
    return spec
