"""Every text read/write must name its encoding: Windows defaults to cp1252 and the data is UTF-8."""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ["tests", "tools", "storylines", "story.py", "expansion.py"]


def _files():
    for name in SOURCES:
        path = ROOT / name
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from (p for p in path.rglob("*.py") if "scratch" not in p.parts)


def _text_mode(call):
    mode = call.args[1] if len(call.args) > 1 else next((k.value for k in call.keywords if k.arg == "mode"), None)
    if mode is None:
        return True
    return not (isinstance(mode, ast.Constant) and isinstance(mode.value, str) and "b" in mode.value)


def offenders():
    found = []
    for path in _files():
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or any(k.arg == "encoding" or k.arg is None for k in node.keywords):
                continue
            func = node.func
            name = func.attr if isinstance(func, ast.Attribute) else func.id if isinstance(func, ast.Name) else ""
            bare = (name in ("read_text", "write_text")
                    or (name == "open" and isinstance(func, ast.Name) and _text_mode(node))
                    or (name == "open" and isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id == "io" and _text_mode(node)))
            if bare:
                found.append(f"{path.relative_to(ROOT)}:{node.lineno}: {name}() without encoding=")
    return found


class Utf8IoTests(unittest.TestCase):
    def test_text_io_names_its_encoding(self):
        self.assertEqual([], offenders(), "pass encoding='utf-8' (Windows defaults to cp1252)")


if __name__ == "__main__":
    unittest.main()
