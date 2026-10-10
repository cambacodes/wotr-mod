#!/usr/bin/env python3
"""AST inventory of test contracts; never imports or executes inspected tests.

Classification is conservative static evidence, not permission to rewrite tests.
Names select Python test discovery functions and describe protection only; they
never select classification. Use --bundle-manifest to inspect pinned inputs.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

PROSE = 'player-visible text comparison or prose selector'
POSITION = 'paragraph or choice index used as identity'
COUNT = 'registry, scene, entry, paragraph, choice or occurrence count'
SOURCE = 'source-file text comparison'
PINNED = {PROSE, POSITION, COUNT, SOURCE}
TEXT_FIELDS = {'Text', 'Entry', 'ReturnText', 'Label', 'Description', 'text', 'text_sha256'}
COLLECTIONS = {'Scenes', 'SCENES', 'Paragraphs', 'paragraphs', 'Choices', 'choices',
               'Entries', 'entries', 'registry', 'REGISTRY', 'contexts', 'rows', 'ROWS', 'Lines',
               'by_id', 'PARTNERS', 'CONSUMERS', 'Presences', 'Relationships', 'ForesightConsumers'}
GATES = {'Requires', 'Forbids', 'Set', 'Next', 'Check', 'AnyGroups', 'EnterSet',
         'Id', 'id', 'Abort', 'Success', 'Failure', 'DC'}
LIMITS = [
    'Static heuristics do not establish whether a literal is actually player-visible; review prose candidates.',
    'Local aliases, loop targets, same-module helper returns and assertion helpers are traced conservatively; imported helpers and runtime dispatch are opaque.',
    'Bindings are flow-insensitive unions: reassignment or dynamic field keys can over-classify; unknown assertions default to behavioural.',
    'Setup failures are not assertions: module summaries classify discovered tests, not the cause of a setUpClass error.',
    'No tests are executed. Decorator-generated tests, inherited tests defined in other modules and dynamic test factories may be absent.',
]
FAILING_MODULES = (
    'test_nidalynn_partner_claim test_harem_row_s49 test_contract_j01 test_kiana_partner '
    'test_iomedae_round2 test_horzalah_polish test_herrax_round2 test_harem_row_registry '
    'test_engine_q5 test_eng7_l07_contracts test_endings_job4 test_earned_presence '
    'test_crossroute_presence test_arueshalae_round2 test_harem_row_s30 test_chivarro_setpieces '
    'test_harem_row_s42 test_harem_row_s35 test_harem_row_s25 test_harem_row_s24 '
    'test_engine_q7_l12 test_draft_contract_lint'
).split()


def symbol(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return symbol(node.value) + '.' + node.attr
    return ''


def literal(node):
    return node.value if isinstance(node, ast.Constant) else None


def own_walk(node):
    """Walk a function without attributing nested function bodies to its parent."""
    yield node
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            continue
        yield from own_walk(child)


class Analyzer:
    def __init__(self, source):
        self.tree = ast.parse(source)
        self.functions = {n.name: n for n in ast.walk(self.tree)
                          if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.resolving = set()
        self.globals = {}
        self.bindings = {}
        self.resolve(list(own_walk(self.tree)))
        self.globals = {k: set(v) for k, v in self.bindings.items()}

    def resolve(self, nodes):
        for _ in range(6):
            before = {k: set(v) for k, v in self.bindings.items()}
            for node in nodes:
                if isinstance(node, (ast.Assign, ast.AnnAssign, ast.NamedExpr)):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        self.bind(target, self.tags(node.value))
                elif isinstance(node, (ast.For, ast.AsyncFor, ast.comprehension)):
                    tags = self.tags(node.iter)
                    self.bind(node.target, tags)
                    if (isinstance(node.target, (ast.Tuple, ast.List)) and node.target.elts
                            and isinstance(node.iter, ast.Call) and symbol(node.iter.func) == 'enumerate'
                            and tags & {'collection:Choices', 'collection:Paragraphs', 'collection:choices', 'collection:paragraphs'}):
                        self.bind(node.target.elts[0], {POSITION})
            if before == self.bindings:
                break

    def local_bindings(self, fn, arguments=()):
        saved = self.bindings
        self.bindings = {k: set(v) for k, v in self.globals.items()}
        parameters = fn.args.args
        if parameters and parameters[0].arg in {'self', 'cls'}:
            parameters = parameters[1:]
        for parameter, tags in zip(parameters, arguments):
            self.bindings[parameter.arg] = set(tags)
        self.resolving.add(fn.name)
        self.resolve(list(own_walk(fn)))
        self.resolving.discard(fn.name)
        result = self.bindings
        self.bindings = saved
        return result

    def bind(self, target, tags):
        if isinstance(target, (ast.Tuple, ast.List)):
            for element in target.elts:
                self.bind(element, tags)
        else:
            key = symbol(target).replace('cls.', 'self.', 1)
            if key:
                self.bindings.setdefault(key, set()).update(tags)

    def tags(self, node, seen=frozenset()):
        if node is None:
            return set()
        key = symbol(node).replace('cls.', 'self.', 1)
        tags = set(self.bindings.get(key, ()))
        tail = key.split('.')[-1]
        if tail in COLLECTIONS:
            tags.add('collection:' + tail)
        if tail.lower() in {'text', 'prose', 'paragraphs', 'paragraph', 'choice', 'choices', 'registry', 'scenes'}:
            tags.add('hint:' + tail.lower())
        if tail.lower() in {'text', 'prose', 'rendered', 'player_text'}:
            tags.add(PROSE)
        if tail in {'errors', 'diagnostics', 'stderr', 'stdout', 'returncode'}:
            tags.add('diagnostic')
        if isinstance(node, ast.Constant):
            if isinstance(node.value, str) and re.search(r'\s', node.value.strip()):
                tags.add('literal-prose')
            return tags
        if isinstance(node, ast.Subscript):
            base = self.tags(node.value, seen)
            field = literal(node.slice)
            # A structural projection drops unrelated prose in its container.
            if field in TEXT_FIELDS:
                return {PROSE} | (base & {POSITION})
            if field in GATES:
                return {'behaviour:' + field} | (base & {POSITION, PROSE, SOURCE})
            if field in COLLECTIONS:
                return {'collection:' + field} | (base & {POSITION})
            index = not isinstance(node.slice, ast.Slice) and not isinstance(field, str)
            positional = bool(base & {'collection:Paragraphs', 'collection:paragraphs',
                                     'collection:Choices', 'collection:choices',
                                     'hint:paragraphs', 'hint:choices'})
            if index and positional:
                base.add(POSITION)
            return tags | base | self.tags(node.slice, seen)
        if isinstance(node, ast.Call):
            name = symbol(node.func)
            short = name.split('.')[-1]
            args = node.args
            if short == 'get' and args:
                field = literal(args[0])
                if field in TEXT_FIELDS | GATES | COLLECTIONS:
                    return self.tags(ast.Subscript(value=node.func.value, slice=args[0]), seen)
            if short in {'read_text', 'read_bytes', 'read'}:
                return {SOURCE}
            if name in {'json.loads', 'json.load', 'ast.parse'}:
                return set()  # Parsed metadata/AST is not a raw source comparison.
            if short in {'len', 'sum', 'count'}:
                base = set().union(*(self.tags(a, seen) for a in args)) if args else set()
                if short in {'sum', 'count'} or any(t.startswith('collection:') for t in base) or base & {'hint:registry', 'hint:scenes', 'hint:paragraphs', 'hint:choices'}:
                    base.add(COUNT)
                return base
            if short in self.functions and short not in seen and short not in self.resolving:
                fn = self.functions[short]
                arguments = [self.tags(arg, seen) for arg in args]
                saved = self.bindings
                self.bindings = self.local_bindings(fn, arguments)
                returns = [n.value for n in own_walk(fn) if isinstance(n, ast.Return)]
                result = set().union(*(self.tags(n, seen | {short}) for n in returns)) if returns else tags
                self.bindings = saved
                return result
            # Tool outputs are behavioural even when fed prose as a fixture.
            if short.startswith(('sim_', 'check', 'validate', 'lint', 'live_mentions')) or short.endswith(('errors', 'diagnostics')):
                return {'diagnostic'}
            children = list(args) + [k.value for k in node.keywords]
            if isinstance(node.func, ast.Attribute):
                children.append(node.func.value)
            return tags | set().union(*(self.tags(c, seen) for c in children))
        # Comprehensions carry both projected values and selector dependencies.
        return tags | set().union(*(self.tags(c, seen) for c in ast.iter_child_nodes(node)))

    def assertion(self, node):
        if isinstance(node, ast.Assert):
            return [node.test]
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            name = node.func.attr
            if symbol(node.func.value) == 'self' and name.startswith('assert') and name not in self.functions:
                # Ignore messages: their prose is not a tested value.
                arity = 2 if name in {'assertEqual', 'assertNotEqual', 'assertIn', 'assertNotIn',
                                     'assertIs', 'assertIsNot', 'assertGreater', 'assertLess',
                                     'assertGreaterEqual', 'assertLessEqual', 'assertCountEqual',
                                     'assertAlmostEqual', 'assertRegex', 'assertNotRegex',
                                     'assertListEqual', 'assertDictEqual', 'assertSetEqual',
                                     'assertTupleEqual', 'assertSequenceEqual'} else 1
                return node.args[:arity]
        return None

    def evidence(self, fn, seen=frozenset()):
        rows = []
        for node in own_walk(fn):
            values = self.assertion(node)
            if values is not None:
                tags = set().union(*(self.tags(v) for v in values))
                reasons = tags & PINNED
                # Literal prose is a candidate only outside known diagnostics or
                # structural fields (IDs/flags and enum strings are not prose).
                if 'literal-prose' in tags and 'diagnostic' not in tags and not any(t.startswith('behaviour:') for t in tags):
                    reasons.add(PROSE)
                # Equal cardinality to its own deduplicated form checks uniqueness.
                if len(values) == 2 and all(isinstance(v, ast.Call) and symbol(v.func) == 'len' for v in values):
                    left, right = values
                    if right.args and isinstance(right.args[0], ast.Call) and symbol(right.args[0].func) == 'set' and right.args[0].args and ast.dump(left.args[0]) == ast.dump(right.args[0].args[0]):
                        reasons.discard(COUNT)
                rows.append({'line': node.lineno, 'reasons': sorted(reasons),
                             'behavioural': not reasons or any(t.startswith('behaviour:') for t in tags),
                             'helper': fn.name if seen else None})
            elif isinstance(node, ast.Call):
                name = symbol(node.func).split('.')[-1]
                if name in self.functions and name not in seen and name != fn.name:
                    saved = self.bindings
                    arguments = [self.tags(arg) for arg in node.args]
                    self.bindings = self.local_bindings(self.functions[name], arguments)
                    rows.extend(self.evidence(self.functions[name], seen | {fn.name, name}))
                    self.bindings = saved
        return rows

    def records(self, module):
        records = []
        def visit(body, class_name=None):
            for fn in body:
                if isinstance(fn, ast.ClassDef):
                    saved_functions, saved_globals = self.functions, self.globals
                    self.functions = {n.name: n for n in self.tree.body
                                      if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
                    self.functions.update({n.name: n for n in fn.body
                                           if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))})
                    self.globals = {k: set(v) for k, v in saved_globals.items()}
                    for setup in fn.body:
                        if isinstance(setup, (ast.FunctionDef, ast.AsyncFunctionDef)) and setup.name in {'setUp', 'setUpClass', '__init__'}:
                            local = self.local_bindings(setup)
                            self.globals.update({k: v for k, v in local.items() if k.startswith('self.')})
                    visit(fn.body, fn.name)
                    self.functions, self.globals = saved_functions, saved_globals
                elif isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name.startswith('test'):
                    self.bindings = self.local_bindings(fn)
                    evidence = self.evidence(fn)
                    pinned = {(r['line'], reason, r['helper']) for r in evidence for reason in r['reasons']}
                    has_behaviour = any(r['behavioural'] for r in evidence)
                    classification = 'mixed' if pinned and has_behaviour else 'pinned' if pinned else 'behavioural'
                    doc = ast.get_docstring(fn)
                    protection = doc.splitlines()[0] if doc else fn.name.removeprefix('test_').replace('_', ' ')
                    records.append({'module': module, 'class': class_name, 'function': fn.name,
                                    'line': fn.lineno, 'classification': classification,
                                    'pinned_assertions': [dict(line=line, reason=reason, **({'helper': helper} if helper else {}))
                                                          for line, reason, helper in sorted(pinned, key=lambda r: (r[0], r[1], r[2] or ''))],
                                    'protects': protection, 'assertion_count': len(evidence)})
        visit(self.tree.body)
        return records


def classify_source(source, module='<memory>'):
    """Classify conventional test functions in UTF-8 source supplied by the caller."""
    return Analyzer(source).records(module)


def inventory(root, bundle_manifest=None):
    inputs = []
    if bundle_manifest:
        manifest = json.loads(bundle_manifest.read_text(encoding='utf-8'))
        for entry in manifest['inputs']['tests']:
            if entry['path'].endswith('.py'):
                inputs.append((entry['path'], bundle_manifest.parent / entry['bundle_path'], entry['sha256']))
        # Include newly assigned tests absent from the pinned baseline.
        pinned_paths = {p for p, _, _ in inputs}
        inputs.extend((p.relative_to(root).as_posix(), p, None) for p in sorted((root / 'tests').rglob('*.py'))
                      if p.relative_to(root).as_posix() not in pinned_paths)
    else:
        inputs = [(p.relative_to(root).as_posix(), p, None) for p in sorted((root / 'tests').rglob('*.py'))]
    records, sources = [], []
    for module, path, expected in sorted(inputs):
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if expected and digest != expected:
            raise ValueError(f'Pinned input digest mismatch: {module}')
        records.extend(classify_source(raw.decode('utf-8'), module))
        sources.append({'module': module, 'sha256': digest, 'input': 'bundle' if expected else 'workspace'})
    modules = {}
    for module, _, _ in sorted(inputs):
        rows = [r for r in records if r['module'] == module]
        counts = Counter(r['classification'] for r in rows)
        modules[module] = {c: counts[c] for c in ('behavioural', 'pinned', 'mixed')}
        modules[module]['pinned_assertions'] = sum(len({p['line'] for p in r['pinned_assertions']}) for r in rows)
    failures = {name: {'classification': ('mixed' if counts['mixed'] or (counts['pinned'] and counts['behavioural']) else 'pinned' if counts['pinned'] else 'behavioural'), **counts}
                for name in FAILING_MODULES if (counts := modules.get(f'tests/{name}.py')) is not None}
    return {'schema_version': 1,
            'classifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'base_sha': manifest['base'] if bundle_manifest else None,
            'input_manifest_digest': hashlib.sha256(bundle_manifest.read_bytes()).hexdigest() if bundle_manifest else None,
            'method': 'AST assertions with conservative local provenance',
            'sources': sources, 'counts': dict(Counter(r['classification'] for r in records)),
            'modules': modules, 'cand14_failing_modules': failures, 'known_limits': LIMITS, 'tests': records}


def markdown(data):
    lines = ['# Test inventory', '', 'Static assertion inventory; existing tests are unchanged.', '',
             'Regenerate with `python -m tools.test_classifier`; add `--bundle-manifest <manifest.json>` to use exact pinned baseline inputs plus new workspace tests.', '',
             f"Parsed {len(data['sources'])} Python files; discovered {len(data['tests'])} tests.", '',
             '| Classification | Tests |', '| --- | ---: |']
    lines.extend(f'| {kind} | {data["counts"].get(kind, 0)} |' for kind in ('behavioural', 'pinned', 'mixed'))
    lines += ['', '## Modules with most pinned assertions', '', '| Module | Pinned assertions |', '| --- | ---: |']
    top = sorted(data['modules'].items(), key=lambda item: (-item[1]['pinned_assertions'], item[0]))[:20]
    lines.extend(f'| {m} | {c["pinned_assertions"]} |' for m, c in top)
    lines += ['', '## Cand-14 failing modules', '', 'The supplied failing names identify modules, not individual methods. Every discovered method and pinned line is in JSON. Counts below summarize their assertions; setup errors have no assertion classification.', '',
              '| Module | Classification | Behavioural | Pinned | Mixed |', '| --- | --- | ---: | ---: | ---: |']
    lines.extend(f'| {m} | {c["classification"]} | {c["behavioural"]} | {c["pinned"]} | {c["mixed"]} |'
                 for m, c in data['cand14_failing_modules'].items())
    lines += ['', '## Known limits', ''] + ['- ' + limit for limit in data['known_limits']]
    lines += ['', '## Counts by module', '', '| Module | Behavioural | Pinned | Mixed |', '| --- | ---: | ---: | ---: |']
    lines.extend(f'| {m} | {c["behavioural"]} | {c["pinned"]} | {c["mixed"]} |' for m, c in data['modules'].items())
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--bundle-manifest', type=Path)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    output = args.output_dir or args.root / 'tools/route_packs/plans'
    data = inventory(args.root, args.bundle_manifest)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'test-inventory.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    (output / 'test-inventory.md').write_text(markdown(data), encoding='utf-8', newline='\n')
    print(json.dumps({'files': len(data['sources']), 'tests': len(data['tests']), 'counts': data['counts']}))


if __name__ == '__main__':
    main()
