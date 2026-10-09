"""Strict review admission shared by the runner and manifest-only aggregation."""
import hashlib
import json
import os
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
METRICS = ('flow_pacing', 'appetite_character_truth', 'gameplay_seam')
PENDING = {'pending_verification', 'needs_live', 'design_required'}


def parse_json(text):
    def pairs(items):
        obj = {}
        for key, value in items:
            if key in obj: raise ValueError('duplicate JSON key: ' + key)
            obj[key] = value
        return obj
    def constant(value):
        raise ValueError('invalid JSON constant: ' + value)
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)


def load(path):
    return parse_json(Path(path).read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # System temp, then a unique destination-side staging file for cross-device atomic replace.
    with tempfile.TemporaryFile(mode='w+', encoding='utf-8', newline='\n') as tmp:
        json.dump(obj, tmp, ensure_ascii=False, indent=2)
        tmp.write('\n'); tmp.seek(0)
        fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
        try:
            with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as out:
                out.write(tmp.read()); out.flush(); os.fsync(out.fileno())
            os.replace(name, path)
        finally:
            if os.path.exists(name): os.unlink(name)


def validate(value, schema, root=None, address='$'):
    """The small JSON Schema subset used by reviewer-schema.json, without dependencies."""
    root = root or schema
    if '$ref' in schema:
        target = root
        for key in schema['$ref'].split('/')[1:]: target = target[key]
        return validate(value, target, root, address)
    if 'oneOf' in schema:
        matches = 0
        for variant in schema['oneOf']:
            try: validate(value, variant, root, address)
            except ValueError: continue
            matches += 1
        if matches != 1: raise ValueError(address + ': expected exactly one output variant')
        return
    types = schema.get('type')
    if types:
        types = [types] if isinstance(types, str) else types
        checks = {'object': isinstance(value, dict), 'array': isinstance(value, list),
                  'string': isinstance(value, str), 'integer': type(value) is int,
                  'null': value is None}
        if not any(checks[t] for t in types): raise ValueError(address + ': invalid type')
    if 'const' in schema and value != schema['const']: raise ValueError(address + ': wrong constant')
    if 'enum' in schema and value not in schema['enum']: raise ValueError(address + ': invalid enum')
    if type(value) is int:
        if value < schema.get('minimum', value) or value > schema.get('maximum', value):
            raise ValueError(address + ': out of range')
    if isinstance(value, str) and len(value) < schema.get('minLength', 0): raise ValueError(address + ': empty string')
    if isinstance(value, dict):
        if not set(schema.get('required', [])) <= value.keys(): raise ValueError(address + ': missing fields')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and value.keys() - props.keys():
            raise ValueError(address + ': extra fields')
        for key in value.keys() & props.keys(): validate(value[key], props[key], root, address + '.' + key)
    if isinstance(value, list):
        for i, item in enumerate(value): validate(item, schema.get('items', {}), root, address + '[' + str(i) + ']')
    if 'if' in schema:
        try: validate(value, schema['if'], root, address)
        except ValueError: pass
        else: validate(value, schema['then'], root, address)


def status(findings):
    active = [f for f in findings if f['disposition'] not in ('dropped', 'artifact')]
    counts = {s: sum(f['severity'] == s for f in active) for s in ('hard', 'major', 'minor')}
    pending = sum(f['disposition'] in PENDING for f in active)
    state = ('blocking' if any(f['severity'] == 'hard' and f['disposition'] == 'confirmed' for f in active)
             else 'pending' if pending else 'needs_fixes' if counts['hard'] or counts['major']
             else 'pass_with_minor' if counts['minor'] else 'pass')
    return dict(counts, pending=pending, chapter_status=state)


def admit(obj, reviewer, submitted=None, identity=None):
    validate(obj, load(HERE / 'reviewer-schema.json'))
    if obj['reviewer'] != reviewer: raise ValueError('wrong reviewer')
    if identity:
        for key, val in identity.items():
            if obj.get(key) != val: raise ValueError('identity mismatch: ' + key)
    if reviewer == 'luna':
        ids = [f['id'] for f in obj['findings']]
        if len(set(ids)) != len(ids): raise ValueError('duplicate Luna id')
        for f in obj['findings']:
            expected = 'confirmed' if f['certainty'] == 'certain' else 'pending_verification'
            if f['disposition'] != expected or f['chapter'] != obj['chapter']: raise ValueError('finding disposition/chapter mismatch')
        counts = status(obj['findings'])
        for key in ('hard', 'major', 'minor'):
            if obj['verdict'][key] != counts[key]: raise ValueError('incorrect verdict count')
        # Legacy status vocabulary permits uncertain hard items as needs_fixes.
        expected = counts['chapter_status']
        if expected == 'pending': expected = 'needs_fixes' if counts['hard'] or counts['major'] else 'pass_with_minor'
        if obj['verdict']['chapter_status'] != expected: raise ValueError('incorrect verdict status')
        for metric in obj['chapter_metrics'].values():
            if obj['scope'] == 'part' and metric['score'] is not None: raise ValueError('part cannot assign chapter score')
            if metric['score'] is None:
                if metric['evidence_level'] != 'unmeasured': raise ValueError('null score must be unmeasured')
            elif not metric['evidence'] or metric['evidence_level'] == 'unmeasured': raise ValueError('score requires addressed evidence')
        if obj['chapter_disposition'] == 'no_mod_content' and (obj['findings'] or any(m['score'] is not None for m in obj['chapter_metrics'].values())):
            raise ValueError('empty chapter cannot invent scores or findings')
    else:
        if submitted is None: raise ValueError('Terra requires submitted items')
        expected = {f['id'] for f in submitted}
        ids = [d['id'] for d in obj['dispositions']]
        if len(ids) != len(set(ids)) or set(ids) != expected: raise ValueError('Terra ids must cover submitted items exactly once')
        for d in obj['dispositions']:
            f = d['finding']
            if d['disposition'] in ('confirmed', 'revised'):
                if f is None or f['id'] != d['id'] or f['certainty'] != 'certain' or f['disposition'] != 'confirmed' or f['chapter'] != obj['chapter']:
                    raise ValueError('invalid Terra replacement')
            elif f is not None: raise ValueError('nonconfirmed disposition cannot replace evidence')
    return obj


def uncertain(luna):
    return [f for f in luna['findings'] if f['disposition'] == 'pending_verification']


def resolve(luna, terra=None):
    decisions = {d['id']: d for d in terra['dispositions']} if terra else {}
    records = []
    for original in luna['findings']:
        d = decisions.get(original['id'])
        f = dict(d['finding'] if d and d['finding'] else original)
        if d: f['disposition'] = 'confirmed' if d['disposition'] == 'revised' else d['disposition']
        records.append(dict(f, raw_luna=original, adjudication=d))
    return records
