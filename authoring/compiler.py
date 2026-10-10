"""Compile in legacy order, collecting expected defects across nested phases.

The outer compilation rejects the collected defects after validation and
serialization. Reference/contract loading remains in the legacy builders.
"""
from dataclasses import dataclass
import importlib
from pathlib import Path
import sys

from ._serialization import serialize
from . import generation_errors


@dataclass(frozen=True)
class CompilationInputs:
    destination: Path | None = None


@dataclass(frozen=True)
class CompiledStory:
    payload: dict
    export_bytes: bytes
    _text: str
    _newline: str | None


def _legacy_module(name):
    # A direct CLI already executed its top-level imports as __main__. Reuse
    # that module rather than importing the same source a second time. This
    # also handles the guard's runpy execution without aliasing sys.modules.
    command = sys.modules.get("__main__")
    source = Path(__file__).resolve().parents[1] / (name + ".py")
    if (command is not None and getattr(command, "__file__", None)
            and Path(command.__file__).resolve() == source and hasattr(command, "_make_" + name)):
        return command
    return importlib.import_module(name)


SCENE_KINDS = ("letter", "visit", "sending", "memory", "event", "invitation")


def delivery_errors(scene):
    errors = []
    if scene.get("Kind") is not None and scene["Kind"] not in SCENE_KINDS:
        errors.append("Kind must be one of " + "/".join(SCENE_KINDS))
    remote = bool(scene.get("Remote")) or scene.get("Owner") == "Memory"
    if remote:
        physical_only = [k for k in ("EntryMythic", "EntryAlignment", "ContinueBefore", "ReturnToList") if scene.get(k)]
        return errors + [k + " needs a physical scene" for k in physical_only]
    errors += [k + " needs a remote scene" for k in ("Kind", "ManualOnly", "TableHosted") if scene.get(k)]
    attached = (scene.get("InteractionHub") or scene.get("AnswerLists") or scene.get("ContinueBefore")
                or str(scene.get("Owner", "")).endswith("Epilogue")
                or (scene.get("Relationship") or "tirabade") == "tirabade" and scene.get("Owner") in ("Anevia", "Irabeth", "Together"))
    return errors + ([] if attached else ["physical scene needs an InteractionHub or AnswerLists"])


_compilation_depth = 0


def compile_story(profile, inputs=None, *, independent_tirabade=True):
    global _compilation_depth
    with generation_errors.collecting():
        _compilation_depth += 1
        try:
            compiled = _compile_story(profile, inputs, independent_tirabade=independent_tirabade)
            # The base build is a phase of expansion assembly. Its errors must
            # not prevent the independent expansion overlays from running.
            if _compilation_depth == 1 and generation_errors.errors:
                raise generation_errors.GenerationErrors("Generation errors: " + str(len(generation_errors.errors)))
            return compiled
        finally:
            _compilation_depth -= 1


def _compile_story(profile, inputs=None, *, independent_tirabade=True):
    """Compile the base or expansion with its existing order and copy policy.

    No destination means expansion LF bytes or base host-newline bytes. A
    destination is inspected after assembly, exactly as in the old CLI.
    """
    if profile == "base":
        payload = _legacy_module("story")._make_story()
    elif profile == "expansion":
        payload = _legacy_module("expansion")._make_expansion(independent_tirabade=independent_tirabade)
    else:
        raise ValueError("Unknown story profile: " + str(profile))
    # Mirrors Story.Validate's remote/physical field rules, the ones a remote->in-person conversion breaks (A96, A100).
    for scene in payload.get("Scenes", []):
        for rule in delivery_errors(scene):
            entry = {"code": "scene.delivery", "scene": scene.get("Id"),
                     "source": "authoring/compiler.py", "detail": rule}
            # Base scenes are validated again after expansion transformations.
            # A repeated scene/rule is still one diagnosed delivery defect.
            if entry not in generation_errors.errors:
                generation_errors.record("scene.delivery", scene=scene.get("Id"),
                                         source="authoring/compiler.py", detail=rule)
    destination = None if inputs is None else inputs.destination
    text, newline, raw = serialize(payload, profile, destination)
    return CompiledStory(payload, raw, text, newline)
