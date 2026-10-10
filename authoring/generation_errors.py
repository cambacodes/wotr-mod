"""One collector for expected assembly errors and the expansion CLI report."""
from contextlib import contextmanager
import inspect
import json
import os
from pathlib import Path
import sys


errors = []
_depth = 0


@contextmanager
def collecting():
    global _depth
    if not _depth:
        errors.clear()
    _depth += 1
    try:
        yield
    finally:
        _depth -= 1


def record(code, *, scene=None, node=None, source=None, detail=None):
    if source is None:
        # Attribute helpers to the authoring caller, rather than the collector.
        frame = inspect.currentframe().f_back
        while frame and frame.f_globals.get("__name__") in (__name__, "storylines.heat_text"):
            frame = frame.f_back
        if frame:
            path = Path(frame.f_code.co_filename).resolve()
            root = Path(__file__).resolve().parents[1]
            source = path.relative_to(root).as_posix() if path.is_relative_to(root) else path.name
        del frame
    entry = {"code": code}
    for key, value in (("scene", scene), ("node", node), ("source", source), ("detail", detail)):
        if value is not None:
            entry[key] = value
    errors.append(entry)


class GenerationErrors(ValueError):
    """Assembly finished, but its collected errors prohibit publication."""


def expansion_main():
    complete = False
    export_written = False
    with collecting():
        try:
            from .compiler import CompilationInputs, compile_story
            from ._serialization import write_story
            root = Path(__file__).resolve().parents[1]
            output = Path(os.environ.get("RRT_STORY_OUTPUT", root / "development/Story.json"))
            compiled = compile_story("expansion", CompilationInputs(destination=output))
            complete = True
            if not errors:
                print(f"INCOMPLETE DEVELOPMENT EXPORT: {len(compiled.payload['Scenes'])} scenes -> {output}")
                output.parent.mkdir(exist_ok=True)
                previous = output.read_bytes() if output.exists() else None
                try:
                    write_story(output, compiled)
                except BaseException:
                    # A failed writer must leave neither a partial new export
                    # nor a truncated replacement of the prior export.
                    if previous is None:
                        output.unlink(missing_ok=True)
                    else:
                        output.write_bytes(previous)
                    raise
                export_written = True
        except GenerationErrors:
            complete = True
        except BaseException as exc:
            complete = False
            record("generation.exception", detail=f"{type(exc).__name__}: {exc}")
        finally:
            report = os.environ.get("RRT_GENERATION_REPORT")
            if report:
                Path(report).write_text(json.dumps({"version": 1, "complete": complete,
                    "export_written": export_written, "errors": errors}, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="\n")
        if errors:
            print(json.dumps(errors, ensure_ascii=False), file=sys.stderr)
        return 0 if not errors and export_written else 1


class OverlayMismatch(Exception):
    """An explicitly diagnosed overlay failure, already entered in the collector."""
    def __init__(self, code, **address):
        record(code, **address)
        super().__init__(code)


@contextmanager
def overlay_item():
    """Skip one invalid overlay target while processing its independent siblings."""
    try:
        yield
    except OverlayMismatch:
        pass


def overlay_node(scenes, scene, node, *, scene_address=None):
    event = scenes.get(scene)
    scene = scene if scene_address is None else scene_address
    if event is None:
        raise OverlayMismatch("overlay.scene_resolution", scene=scene, node=node)
    matches = [item for item in event["Nodes"] if item["Id"] == node]
    if len(matches) != 1:
        raise OverlayMismatch("overlay.node_resolution", scene=scene, node=node, detail=str(len(matches)))
    return matches[0]


def overlay_index(node, field, index, scene):
    items = node.get(field) or []
    if not -len(items) <= index < len(items):
        raise OverlayMismatch("overlay.index_resolution", scene=scene, node=node.get("Id"),
                              detail=f"{field}[{index}]")
    return items[index]
