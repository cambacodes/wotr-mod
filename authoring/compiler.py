"""One compilation entry, with the legacy assembly schedule left untouched.

S1 owns command dispatch and serialization only. Reference/contract loading
and mutable collectors still belong to the legacy implementations; the guard
pins their actual source/native reads outside the exported story. Build-local
state and contract loading are later slices, not implied by this interface.
"""
from dataclasses import dataclass
import importlib
from pathlib import Path
import sys

from ._serialization import serialize


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
    if command is not None and getattr(command, "__file__", None) and Path(command.__file__).resolve() == source:
        return command
    return importlib.import_module(name)


SCENE_KINDS = ("letter", "visit", "sending", "memory", "event", "invitation")


def delivery_errors(scene):
    if scene.get("Kind") is not None and scene["Kind"] not in SCENE_KINDS:
        return ["Kind must be one of " + "/".join(SCENE_KINDS)]
    remote = bool(scene.get("Remote")) or scene.get("Owner") == "Memory"
    if remote:
        physical_only = [k for k in ("EntryMythic", "EntryAlignment", "ContinueBefore", "ReturnToList") if scene.get(k)]
        return [k + " needs a physical scene" for k in physical_only]
    errors = [k + " needs a remote scene" for k in ("Kind", "ManualOnly", "TableHosted") if scene.get(k)]
    attached = (scene.get("InteractionHub") or scene.get("AnswerLists") or scene.get("ContinueBefore")
                or str(scene.get("Owner", "")).endswith("Epilogue")
                or (scene.get("Relationship") or "tirabade") == "tirabade" and scene.get("Owner") in ("Anevia", "Irabeth", "Together"))
    return errors + ([] if attached else ["physical scene needs an InteractionHub or AnswerLists"])


def compile_story(profile, inputs=None, *, independent_tirabade=True):
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
    bad = [f"{s['Id']} ({rule})" for s in payload.get("Scenes", []) for rule in delivery_errors(s)]
    if bad:
        raise ValueError("Scene delivery fields contradict remote/physical (Story.Validate): " + ", ".join(bad))
    destination = None if inputs is None else inputs.destination
    text, newline, raw = serialize(payload, profile, destination)
    return CompiledStory(payload, raw, text, newline)
