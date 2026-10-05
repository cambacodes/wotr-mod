"""eng7-l09: isolated, deterministic authoring checks; never publish a draft."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

WORKER = '''
import copy, importlib, json, pathlib, sys
import expansion
story = expansion.make_expansion()
registered = set(sys.modules)
out = {}
for path in sorted(pathlib.Path("storylines").glob("*.py")):
    name = "storylines." + path.stem
    if name in registered: continue
    try:
        module = importlib.import_module(name)
        scenes = getattr(module, "SCENES", [])
        if not scenes: continue
        row = dict(scenes=copy.deepcopy(scenes), integration_error=None)
        if hasattr(module, "integrate"):
            try: module.integrate(copy.deepcopy(story))
            except Exception as exc: row["integration_error"] = str(exc)
        out[path.stem] = row
    except Exception as exc:
        out[path.stem] = dict(scenes=[], import_error=str(exc))
pathlib.Path(sys.argv[1]).write_text(json.dumps(out), encoding="utf-8")
'''


def inventory(root=ROOT):
    # A gate constructs this once from the current sources before starting
    # read-only checks. JSON decoding gives every caller a private fixture.
    fixture = os.environ.get('RRT_GATE_DRAFT_INVENTORY')
    if fixture:
        data = json.loads(Path(fixture).read_text(encoding='utf-8'))
        if data['root'] == str(Path(root).resolve()):
            return data['modules']
    return _build_inventory(root)


def _build_inventory(root):
    # Imports (including append-to-SCENES modules) happen in a fresh process in
    # a disposable copy. No sys.modules or source-module state leaks to callers.
    with tempfile.TemporaryDirectory(prefix="rrt-eng7-l09-drafts-") as folder:
        work = Path(folder)
        for path in sorted(Path(root).glob("*.py")):
            shutil.copy2(path, work / path.name)
        for name in ("storylines", "reference", "tools", "data", "src"):
            shutil.copytree(Path(root) / name, work / name,
                            ignore=shutil.ignore_patterns("__pycache__", "scratch", "obj", "bin", "rrt_verify_report*"))
        result = work / "inventory.json"
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "RRT_ROOT": str(work)}
        completed = subprocess.run([sys.executable, "-c", WORKER, str(result)], cwd=work, env=env,
                                   capture_output=True, text=True)
        if completed.returncode:
            raise RuntimeError(completed.stderr)
        return json.loads(result.read_text(encoding="utf-8"))


def targets(choice):
    if choice.get("Check"):
        return [choice["Check"]["Success"], choice["Check"]["Failure"]]
    return [choice["Next"]] if choice.get("Next") else []


def check_scene(scene):
    rows = []
    def add(code, node="entry", **details):
        rows.append(dict(scene=scene["Id"], location=node, code=code, **details))
    nodes = {n["Id"]: n for n in scene.get("Nodes", [])}
    if not nodes:
        add("empty-graph")
        return rows
    reached, pending = set(), [scene["Nodes"][0]["Id"]]
    while pending:
        node = pending.pop()
        if node in reached:
            continue
        if node not in nodes:
            add("missing-target", node)
            continue
        reached.add(node)
        pending.extend(t for c in nodes[node].get("Choices", []) for t in targets(c))
    # Save-referenced stubs need an explicit reason and a gate on every incoming
    # edge. An exemption cannot conceal a completion producer.
    retired = scene.get("RetiredNodes", {})
    for node in sorted(set(nodes) - reached):
        choices = nodes[node].get("Choices", [])
        incoming = [c for n in nodes.values() for c in n.get("Choices", []) if node in targets(c)]
        if retired.get(node) and not any(c.get("Set") for c in choices) and all(c.get("Forbids") for c in incoming):
            continue
        add("unreachable-node", node)
        for c in choices:
            for flag in c.get("Set", []):
                add("unreachable-producer", node, flag=flag)
    if scene.get("Entry") in nodes:
        add("literal-node-entry")
    if not (scene.get("Remote") or scene.get("Owner") == "Epilogue" or scene.get("EpilogueAfter")
            or scene.get("AnswerLists") or scene.get("InteractionHub") or scene.get("ContinueBefore")
            or scene.get("Relationship", "tirabade") == "tirabade" and scene.get("Owner") in {"Anevia", "Irabeth", "Together"}):
        add("no-physical-attachment")
    requested = {f for n in nodes.values() for c in n.get("Choices", []) for f in c.get("Set", []) if f.endswith(".requested")}
    for node in sorted(reached):
        for i, choice in enumerate(nodes[node].get("Choices", [])):
            flags = choice.get("Set", [])
            if (requested and not targets(choice) and not choice.get("Abort") and not requested.intersection(flags)
                    and any(f.endswith((".authorized", ".theory", ".wait", ".pending")) for f in flags)):
                add("deferred-once-completion", node + "/choice/%d" % i, flags=flags)
    return rows


def check(drafts):
    result = []
    for module, data in sorted(drafts.items()):
        for scene in data.get("scenes", []):
            result.extend(dict(module=module, **r) for r in check_scene(scene))
        for key in ("import_error", "integration_error"):
            if data.get(key):
                result.append(dict(module=module, scene="*", location="integration", code=key, error=data[key]))
    return result


def main():
    rows = check(inventory())
    print(json.dumps(rows, indent=2))
    return int(bool(rows))


if __name__ == "__main__":
    raise SystemExit(main())
