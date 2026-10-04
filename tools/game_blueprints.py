"""Offline blueprint GUID/type evidence, shared by native registries and binding checks.

README: find_bindings(zip_path, {guid: expected_type}) returns archive records with
path/type/data, or raises ValueError naming every missing/mistyped GUID. No parent
manifest may substitute for a native target. This uses verify-game-bindings' small
header scan; no Unity load, extraction directory, or persistent cache is needed.
"""
import json
import os
from pathlib import Path
import re
from zipfile import ZipFile


def game_dir():
    configured = os.environ.get("RRT_GAME_DIR")
    if configured:
        return Path(configured)
    if Path("/wrath/blueprints.zip").is_file():
        return Path("/wrath")
    return Path(r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")


def blueprint_type(data):
    return data["$type"].split(", ")[-1]


def text_key(value):
    """Owlcat LocalizedString.Key, falling back to Shared.String.Key (E14d)."""
    if not isinstance(value, dict):
        return None
    if value.get("m_Key"):
        return value["m_Key"]
    shared = value.get("Shared")
    return shared.get("stringkey") if isinstance(shared, dict) else shared


def iter_records(archive, prefixes=()):
    for path in archive.namelist():
        if path.endswith(".jbp") and (not prefixes or path.startswith(prefixes)):
            yield path, json.loads(archive.read(path))


def find_bindings(zip_path, expected):
    pending = set(expected)
    found = {}
    with ZipFile(zip_path) as archive:
        for path in archive.namelist():
            if not pending:
                break
            if not path.endswith(".jbp"):
                continue
            with archive.open(path) as stream:
                header = stream.read(160)
                # AssetId is in the header in Owlcat's export (same contract as
                # verify-game-bindings.py). Confirm equality after parsing.
                asset = re.search(rb'"AssetId"\s*:\s*"([a-f0-9]{32})"', header)
                if asset is None or asset.group(1).decode("ascii") not in pending:
                    continue
                record = json.loads(header + stream.read())
            guid = record["AssetId"]
            if guid in pending:
                found[guid] = dict(path=path, type=blueprint_type(record["Data"]), data=record["Data"])
                pending.remove(guid)
    failures = [f"{guid}: expected {expected[guid]}, missing from {zip_path}" for guid in sorted(pending)]
    for guid, record in found.items():
        want = expected[guid]
        actual = record["type"]
        matches = actual.startswith(want[:-1]) if want.endswith("*") else actual == want
        if want == "BlueprintCueBase":
            matches = actual in {"BlueprintCue", "BlueprintBookPage", "BlueprintCueSequence", "BlueprintCheck"}
        if not matches:
            failures.append(f"{guid}: expected {want}, found {actual} at {record['path']}")
    if failures:
        raise ValueError("Native blueprint binding verification failed:\n" + "\n".join(failures))
    return found
