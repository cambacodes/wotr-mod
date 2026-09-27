"""Read requested native records without rewriting the game's blueprint archive."""
import json
import os
from pathlib import Path
import re
import sys
from zipfile import ZipFile

# Decode JSON's wire encoding, not the Windows console encoding inherited by Python.
pending = set(json.load(sys.stdin.buffer))
found = {}
asset_id = re.compile(rb'"AssetId"\s*:\s*"([0-9a-fA-F]{32})"')
with ZipFile(sys.argv[1]) as archive:
    for name in archive.namelist():
        if not name.startswith(("World/", "Units/", "Mythic/")) or not name.endswith(".jbp"):
            continue
        with archive.open(name) as stream:
            header = stream.read(200)
            match = asset_id.search(header)
            if match is None or match[1].decode("ascii").lower() not in pending:
                continue
            record = json.loads(header + stream.read())
        guid = record["AssetId"]
        if guid in pending:
            found[guid] = record["Data"]
            pending.remove(guid)
        if not pending:
            break
manifest = os.environ.get("RRT_PARENT_BINDINGS")
if pending and manifest:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
    from parent_bindings import load_parent_bindings
    for manifest_path in manifest.split(os.pathsep):
        if not manifest_path:
            continue
        for guid, record in load_parent_bindings(manifest_path).items():
            if guid in pending:
                # Explicit typed fixtures only; no native fields or parent behavior invented.
                found[guid] = {"$type": "ReviewedParentFixture, " + record["type"],
                               "FixtureProvenance": record}
                pending.remove(guid)
                print("Parent source fixture: " + guid + " " + record["type"], file=sys.stderr)
if pending:
    raise RuntimeError("Missing native blueprints: " + ", ".join(sorted(pending)))
json.dump(found, sys.stdout)
