"""Check the C# engine's requested external bindings against the installed export.

This does not start Unity, execute Main.Build, or test a real game save.
Build tests/RulesTests.csproj before running this command.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
from zipfile import ZipFile
from parent_bindings import load_parent_bindings

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "development/game-bindings-report.json")
    parser.add_argument("--parent-bindings", help="Reviewed parent-mod evidence manifest(s), pinned to the installed assembly; "
                        "several paths may be joined with os.pathsep, as in RRT_PARENT_BINDINGS")
    parser.add_argument("--game", type=Path, default=Path(r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure"))
    args = parser.parse_args()
    dotnet = Path(os.environ["LOCALAPPDATA"]) / "RanRomanceTools/dotnet/dotnet.exe"
    runner = ROOT / "tests/bin/Release/net8.0/RulesTests.dll"
    output = subprocess.run([str(dotnet) if dotnet.is_file() else "dotnet", str(runner), "--bindings", str(args.story.resolve())], check=True, capture_output=True, text=True)
    bindings = json.loads(output.stdout)
    pending = {b["Guid"] for b in bindings}
    found = {}
    with ZipFile(args.game / "blueprints.zip") as archive:
        for name in archive.namelist():
            # E10 readers bind flags, objectives and items that live anywhere in the archive (Items/, Equipment/, World/...).
            if not name.endswith(".jbp"):
                continue
            with archive.open(name) as stream:
                header = stream.read(160)
                if not any(guid.encode("ascii") in header for guid in pending):
                    continue
                record = json.loads(header + stream.read())
            guid = record["AssetId"]
            if guid in pending:
                found[guid] = {"path": name, "type": record["Data"]["$type"].split(", ")[-1]}
                pending.remove(guid)
            if not pending:
                break
    failures = []
    if args.parent_bindings:
        for manifest in filter(None, args.parent_bindings.split(os.pathsep)):
            for guid, record in load_parent_bindings(manifest).items():
                if guid in pending:
                    found[guid] = record
                    pending.remove(guid)
    for binding in bindings:
        target = found.get(binding["Guid"])
        expected = binding["ExpectedType"]
        matches = target is not None and (target["type"].startswith(expected[:-1]) if expected.endswith("*") else target["type"] == expected)
        if not matches:
            failures.append({**binding, "Actual": target})
    report = {
        "scope": "Offline external GUID/type bindings requested by the actual C# story rules; no Unity execution or save round trip",
        "story": str(args.story.resolve()), "game": str(args.game),
        "binding_uses": len(bindings), "unique_targets": len(found),
        "failures": failures, "targets": found,
    }
    report_path = args.output
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit(f"FAIL: {len(failures)} unresolved or mistyped bindings; {report_path}")
    parent_count = sum(record.get("provenance") == "reviewed-parent-source" for record in found.values())
    print(f"PASS: {len(bindings)} binding uses; {len(found) - parent_count} archive targets and {parent_count} reviewed parent-source targets. Report: {report_path}")


if __name__ == "__main__":
    main()
