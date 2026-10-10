"""Compare every field of two UTF-8 story exports, reporting JSON addresses."""
import argparse
import json
from pathlib import Path


def differences(left, right, address='$'):
    """Yield every differing leaf, including missing fields and ordered items."""
    if type(left) is not type(right):
        yield f'{address}: type {type(left).__name__} != {type(right).__name__}'
    elif isinstance(left, dict):
        for key in sorted(left.keys() | right.keys()):
            child = address + '[' + json.dumps(key, ensure_ascii=False) + ']'
            if key not in left:
                yield f'{child}: missing from first export'
            elif key not in right:
                yield f'{child}: missing from second export'
            else:
                yield from differences(left[key], right[key], child)
    elif isinstance(left, list):
        for index in range(max(len(left), len(right))):
            child = f'{address}[{index}]'
            if index >= len(left):
                yield f'{child}: missing from first export'
            elif index >= len(right):
                yield f'{child}: missing from second export'
            else:
                yield from differences(left[index], right[index], child)
    elif left != right:
        yield f'{address}: {left!r} != {right!r}'


def read_export(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result
    def invalid_constant(value):
        raise ValueError(f'non-finite JSON number: {value}')
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique_pairs,
                      parse_constant=invalid_constant)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before')
    parser.add_argument('after')
    args = parser.parse_args(argv)
    try:
        changes = list(differences(read_export(args.before), read_export(args.after)))
    except (OSError, ValueError) as error:
        print(f'Export comparison failed: {error}')
        return 2
    for change in changes:
        print(change)
    print(f'Export equivalence: {len(changes)} differences')
    return 1 if changes else 0


if __name__ == '__main__':
    raise SystemExit(main())
