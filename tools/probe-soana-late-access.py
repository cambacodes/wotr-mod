"""Read installed Soana scene and blueprint access records without game writes.

Run with reference/asset-extraction-env/Scripts/python.exe.
Output is evidence, not an actor restoration or runtime availability assertion.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import os
import subprocess
import zipfile

import UnityPy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path("C:/Program Files (x86)/Steam/steamapps/common/Pathfinder Second Adventure"))
    parser.add_argument("--output", type=Path, default=Path("reference/canon-review/soana-late-access-records.json"))
    args = parser.parse_args()
    records = {"game": str(args.game), "bundles": {}, "blueprints": {}, "direct_references": {}, "access_actions": []}
    access_ids = {
        "2d9c51e422e743947bfa0281d0a2db51", "19c0886c9e105ea4a832eec08321ac0f",
        "87839550c801db944b102f61084fd245", "198b62fe2afa9da4cb314f1b4376b0b9",
        "ef2c34c4a052e294cbdb289be35017bb", "245ad0732c0f97b449481fdaa0b85cf7",
    }
    core = {
        "64805abb52739e44280a758f850b300c", "fccdd316924af204da00c99f01c0e222",
        "d4b624463e52e21438da6f4870320fee", "f102a4d0677148f4cab007f901a5ed3c",
        "ff0d7227c56b2b0488b006893b96040e", "c97882cbc65c4c546aed1810627a5b81",
        "bc435ec57d3151c489d760ecfd4c3289", "995f0ac2951bbb041b062806c163fbf1",
        "8f576b8a-4c79-4f42-a575-d0b27b0f5bb1", "966bb0bc-4937-4e6a-b1af-314fa0a4e468",
    }
    wanted = core | access_ids | {
        "15e0048c7daf0ac4999c2313b58df0e3", "d616ce293b89af14e839c846554b2ccb",
        "54b2da306959efd4683087d9841d21fa", "c2be52d761c44874a67c3c0d87d0dff9",
        "831a725b62c18a443a1d00e4266323a2",
    }
    for name in ("wintersunoutdoor_mechanics_default.scenes", "wintersunoutdoor_mechanics_main.scenes", "wintersunforestcave_mechanics.scenes"):
        path = args.game / "Bundles" / name
        env = UnityPy.load(str(path))
        bundle = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest().upper(), "objects": [], "scripts": []}
        for obj in env.objects:
            if obj.type.name == "MonoScript":
                bundle["scripts"].append({"path_id": obj.path_id, "data": obj.read_typetree()})
            if obj.type.name != "GameObject":
                continue
            data = obj.read_typetree()
            if not re.search(r"Soana|ForestQuest|Orso|Exit_to_ForestCave|Exit.*Outdoor|MessageRoana", data.get("m_Name", ""), re.I):
                continue
            local = {o.path_id: o for o in env.objects if o.assets_file == obj.assets_file}
            entry = {"path_id": obj.path_id, "data": data, "components": [], "parents": []}
            for component in data["m_Component"]:
                item = local[component["component"]["m_PathID"]]
                value = item.read_typetree()
                entry["components"].append({"path_id": item.path_id, "type": item.type.name, "data": value})
                wanted.update(re.findall(r"\b[a-f0-9]{32}\b", json.dumps(value)))
                if item.type.name == "Transform":
                    parent = value["m_Father"]["m_PathID"]
                    while parent:
                        transform = local[parent].read_typetree()
                        entry["parents"].append({"path_id": parent, "data": transform, "game_object": local[transform["m_GameObject"]["m_PathID"]].read_typetree()})
                        parent = transform["m_Father"]["m_PathID"]
            bundle["objects"].append(entry)
        records["bundles"][name] = bundle
    def objects(value):
        if isinstance(value, dict):
            yield value
            for child in value.values():
                yield from objects(child)
        elif isinstance(value, list):
            for child in value:
                yield from objects(child)

    records["access_action_scan"] = {"targets": sorted(access_ids), "scope": "All installed .jbp records; direct fields in typed actions; excludes EtudeStatus conditions", "blueprints_examined": 0}
    with zipfile.ZipFile(args.game / "blueprints.zip") as archive:
        index = {}
        for path in archive.namelist():
            if not path.endswith(".jbp"):
                continue
            raw = archive.read(path)
            records["access_action_scan"]["blueprints_examined"] += 1
            match = re.search(rb'"AssetId"\s*:\s*"([a-f0-9]{32})"', raw[:160])
            if match:
                index[match[1].decode()] = path
            refs = sorted(guid for guid in core if guid.encode() in raw)
            if refs:
                records["direct_references"][path] = refs
            named = "soana" in path.lower() or "wintersun_forestquest" in path.lower()
            access = "wintersun" in path.lower() and path.startswith(("World/Areas/", "GlobalMaps/", "World/Etudes/", "World/Encounters/"))
            cutscene = any(part in path for part in ("/ForestQuest_BearLight/", "/ForestQuest_IfKilledSoana_afterBear/", "/CutsceneCamellia_killSoana/"))
            if any(guid.encode() in raw for guid in access_ids):
                for action in objects(json.loads(raw)):
                    kind = action.get("$type", "").split(", ")[-1]
                    direct = {value.removeprefix("!bp_") for value in action.values() if isinstance(value, str)} & access_ids
                    if direct and kind and kind != "EtudeStatus" and not kind.startswith("Blueprint"):
                        records["access_actions"].append({"path": path, "targets": sorted(direct), "action": action})
            if (named or access or refs or cutscene) and not path.startswith("QA/"):
                records["blueprints"][path] = json.loads(raw)
        for path, value in list(records["blueprints"].items()):
            wanted.add(value["AssetId"])
            parent = value["Data"].get("m_Parent", "")
            if isinstance(parent, str):
                wanted.add(parent.removeprefix("!bp_"))
        examined = set()
        while wanted - examined:
            guid = (wanted - examined).pop()
            examined.add(guid)
            if guid not in index:
                continue
            path = index[guid]
            value = records["blueprints"].setdefault(path, json.loads(archive.read(path)))
            parent = value["Data"].get("m_Parent", "")
            if isinstance(parent, str):
                wanted.add(parent.removeprefix("!bp_"))
    assembly = args.game / "Wrath_Data/Managed/Assembly-CSharp.dll"
    records["assembly_sha256"] = hashlib.sha256(assembly.read_bytes()).hexdigest().upper()
    records["decompiled_types"] = {}
    env = dict(os.environ, DOTNET_ROOT=str(Path.home() / "AppData/Local/RanRomanceTools/dotnet"))
    for typename in (
        "Kingmaker.Designers.EventConditionActionSystem.Actions.SwitchChapter",
        "Kingmaker.Designers.EventConditionActionSystem.Actions.HideUnit",
        "Kingmaker.Designers.EventConditionActionSystem.Evaluators.UnitFromSpawner",
        "Kingmaker.AreaLogic.Cutscenes.Commands.CommandReviveUnit",
        "Kingmaker.View.Spawners.UnitSpawnerBase",
        "Kingmaker.AreaLogic.Etudes.EtudesSystem",
    ):
        result = subprocess.run([str(Path("tools/ilspycmd.exe").resolve()), "-t", typename, str(assembly)], env=env, capture_output=True, text=True, encoding="utf-8", check=True)
        records["decompiled_types"][typename] = result.stdout
    args.output.write_text(json.dumps(records, indent=2, ensure_ascii=True, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {sum(len(b['objects']) for b in records['bundles'].values())} scene objects, {len(records['blueprints'])} blueprints and {len(records['direct_references'])} direct-reference records to {args.output}")


if __name__ == "__main__":
    main()
