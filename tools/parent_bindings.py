"""Load reviewed parent-mod binding evidence, pinned to the installed assembly.

This is a source-evidence manifest, not execution of the parent mod's initializer.
"""
import hashlib
import json
import os
from pathlib import Path
import re


# Manifests pin the absolute path the evidence was reviewed at. If the game has since moved, re-root that path
# onto the current game folder; the SHA-256 check below still requires the identical assembly.
OLD_GAME_ROOTS = (r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure",)
GAME_DIR = os.environ.get("RRT_GAME_DIR") or r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure"


def _resolve_assembly(assembly):
    if assembly.exists():
        return assembly
    text = str(assembly)
    for root in OLD_GAME_ROOTS:
        if text.lower().startswith(root.lower() + "\\"):
            relative = text[len(root) + 1:]
            if os.name != "nt":
                relative = relative.replace("\\", "/")
            return Path(GAME_DIR) / relative
    return assembly


def load_parent_bindings(path):
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    assembly = _resolve_assembly(Path(manifest["AssemblyPath"]))
    actual = hashlib.sha256(assembly.read_bytes()).hexdigest()
    if actual.lower() != manifest["AssemblySha256"].lower():
        raise ValueError("Parent assembly differs from reviewed binding evidence")
    allowed = {"BlueprintEtude", "BlueprintCue", "BlueprintDialog", "BlueprintAnswer",
               "BlueprintAnswersList", "BlueprintQuest", "BlueprintUnit", "BlueprintCueSequence",
               "BlueprintBookPage", "BlueprintQuestObjective", "BlueprintUnlockableFlag"}
    result = {}
    for item in manifest["Bindings"]:
        guid = item["Guid"]
        kind = item["Type"]
        if not re.fullmatch(r"[0-9a-f]{32}", guid) or kind not in allowed:
            raise ValueError("Invalid parent binding identity or type: " + guid)
        if guid in result or not item["Source"].strip():
            raise ValueError("Duplicate or unattributed parent binding: " + guid)
        creator = kind.removeprefix("Blueprint") + "Configurator.New("
        declaration = item.get("GuidDeclaration") or ""
        if (guid not in item["Evidence"] and guid not in declaration) \
                or (kind not in item["Evidence"] and creator not in item["Evidence"]):
            raise ValueError("Parent creation excerpt lacks the requested identity/type: " + guid)
        result[guid] = {"type": kind, "path": item["Source"],
                        "provenance": "reviewed-parent-source", "assembly_sha256": actual}
    return result
