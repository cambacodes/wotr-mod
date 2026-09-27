"""Load reviewed parent-mod binding evidence, pinned to the installed assembly.

This is a source-evidence manifest, not execution of the parent mod's initializer.
"""
import hashlib
import json
from pathlib import Path
import re


def load_parent_bindings(path):
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    assembly = Path(manifest["AssemblyPath"])
    actual = hashlib.sha256(assembly.read_bytes()).hexdigest()
    if actual.lower() != manifest["AssemblySha256"].lower():
        raise ValueError("Parent assembly differs from reviewed binding evidence")
    allowed = {"BlueprintEtude", "BlueprintCue", "BlueprintDialog", "BlueprintAnswer",
               "BlueprintAnswersList", "BlueprintQuest", "BlueprintUnit", "BlueprintCueSequence", "BlueprintBookPage"}
    result = {}
    for item in manifest["Bindings"]:
        guid = item["Guid"]
        kind = item["Type"]
        if not re.fullmatch(r"[0-9a-f]{32}", guid) or kind not in allowed:
            raise ValueError("Invalid parent binding identity or type: " + guid)
        if guid in result or not item["Source"].strip():
            raise ValueError("Duplicate or unattributed parent binding: " + guid)
        creator = kind.removeprefix("Blueprint") + "Configurator.New("
        if guid not in item["Evidence"] or (kind not in item["Evidence"] and creator not in item["Evidence"]):
            raise ValueError("Parent creation excerpt lacks the requested identity/type: " + guid)
        result[guid] = {"type": kind, "path": item["Source"],
                        "provenance": "reviewed-parent-source", "assembly_sha256": actual}
    return result
