"""eng8-q8f: fail branch-certification shortcuts in the nominated route helpers."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ('Camellia', 'Nenio', 'Horzalah')


def lint(root=ROOT):
    errors = []
    for route in ROUTES:
        name = 'tests/' + route + 'TricksterTests.cs'
        text = (Path(root) / name).read_text(encoding="utf-8")
        helper = re.search(r'List<Snapshot> Through\([^\n]+\)\s*\{(.*?)\n        \}', text, re.S)
        if not helper or 'Program.WalkVia(scene, w, node, index)' not in helper[1]:
            errors.append(name + ': claimed edges must use WalkVia')
        if helper and ('chosen.Set' in helper[1] or 'Paths(scene' in helper[1] or 'Program.Walk(scene' in helper[1]):
            errors.append(name + ': final flags cannot establish a claimed edge')
        if 'void Visit(' in text:
            errors.append(name + ': route-local walker bypasses production processing')
    walker = (Path(root) / 'tests/Program.cs').read_text(encoding="utf-8")
    walker = walker[walker.index('private static List<(Snapshot state, bool via)> WalkPaths'):]
    walker = walker[:walker.index('// eng7-l13: the same generic')]
    for witness in ('Rules.EnterNode(node, state)', 'Rules.ChoiceAvailable(c, state)',
                    'Rules.PaymentExitAvailable(node, state)',
                    'next.CrusadeResources[cost.Resource] = balance + cost.Amount',
                    'via.Value.node == id', 'node.Choices.IndexOf(choice) == via.Value.index'):
        if witness not in walker:
            errors.append('tests/Program.cs: missing production walker step: ' + witness)
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = lint(args.root)
    for error in errors:
        print('HARD ' + error)
    print('acceptance walker inventory: %d hard' % len(errors))
    raise SystemExit(bool(errors))
