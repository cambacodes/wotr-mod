"""Read installed Aivu capital scene bindings; never modify game assets.

Run using reference/asset-extraction-env/Scripts/python.exe.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import zipfile

import UnityPy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path("D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure"))
    parser.add_argument("--output", type=Path, default=Path("reference/canon-review/aivu-capital-contact-records.json"))
    args = parser.parse_args()
    game = args.game
    bundle = game / "Bundles/drezencapital_mechanics_mythicazata.scenes"
    assembly = game / "Wrath_Data/Managed/Assembly-CSharp.dll"
    env = UnityPy.load(str(bundle))
    records = {"game": str(game), "bundle": str(bundle), "sha256": {bundle.name: sha(bundle), assembly.name: sha(assembly)}, "scene_objects": [], "blueprints": {}, "decompiled": {}}
    for obj in env.objects:
        if obj.type.name != "GameObject":
            continue
        data = obj.read_typetree()
        if "AzataDragon" not in data.get("m_Name", ""):
            continue
        local = {o.path_id: o for o in env.objects if o.assets_file == obj.assets_file}
        entry = {"path_id": obj.path_id, "data": data, "components": [], "parents": []}
        for component in data["m_Component"]:
            item = local[component["component"]["m_PathID"]]
            value = item.read_typetree()
            entry["components"].append({"path_id": item.path_id, "type": item.type.name, "data": value})
            if item.type.name == "Transform":
                parent = value["m_Father"]["m_PathID"]
                while parent:
                    transform = local[parent].read_typetree()
                    entry["parents"].append({"path_id": parent, "data": transform, "game_object": local[transform["m_GameObject"]["m_PathID"]].read_typetree()})
                    parent = transform["m_Father"]["m_PathID"]
        records["scene_objects"].append(entry)
    records["scripts"] = [{"path_id": o.path_id, "data": o.read_typetree()} for o in env.objects if o.type.name == "MonoScript" and o.read_typetree().get("m_ClassName") in ("CompanionSpawner", "SpawnerInteractionDialog")]
    wanted = {"4391e8b9afbb0cf43aeba700c089f56d", "a55dfc5df40b491d92a873a6e29f6412", "efce31da9b4f2dd46b3f18d985fbf55e", "2570015799edf594daf2f076f2f975d8", "8a076e720870a44438d13b9b939933fd", "69bf5090bc7e2f34f83b73e64972f54b", "e4a1eb7ccc927bb41afbe8b20f00861f", "d995b5fa774299849862a5e3f5d95199", "d3b47e973d65c6c46af1cce815d1f6ce", "de63e66fbc4992e4caf70ed3e9584cbb", "12de733844928794080d3b83ca9d8f82", "f1a65c6d838f58d49ad4ff40544b895b", "cf36f23d60987224696f03be70351928"}
    # Include every Aivu scene show-condition, including the outdoor placement.
    for entry in records["scene_objects"]:
        for component in entry["components"]:
            condition = component["data"].get("ShowCondition", {}).get("guid")
            if condition:
                wanted.add(condition)
    with zipfile.ZipFile(game / "blueprints.zip") as archive:
        wanted.add("32a037e97c3d5c54b85da8f639616c57")
        wanted.update({"40db17008eb1b7e4fbde32f3811324b7", "890805d2200323a408d057f365158a71", "0beabce6f37afd14c9518762a81e13e0", "db13836a3e1c20b4085fe3f0d8990e77", "8758467ee5750a64ca7269955ee49798", "e6f6c08ea1c8d6840a9bc8ae1615336c", "b40989b991fd60b43af50c021884cbdd", "de6ef6f380230794fb7c45d9e21cc72d", "7bd8c70bbc87e3d4cb13effc53dbf981", "d39b1e8067e50d142a326de4dbc38c5a"})
        dialog_path = "World/Dialogs/c3/Mythic_Azata/Island/Dracosha/Dracosha_AzataIsland_dialog.jbp"
        dialog = json.loads(archive.read(dialog_path))
        wanted.update(value.removeprefix("!bp_") for value in dialog["Data"]["FirstCue"]["Cues"])
        for path in archive.namelist():
            if not path.endswith(".jbp"):
                continue
            if not path.startswith(("World/Areas/", "World/Encounters/DrezenCapital/", "World/Etudes/", "World/Dialogs/c3/Mythic_Azata/Island/Dracosha/", "Units/Pregens/StartGame/", "Mythic/Azata/")):
                continue
            raw = archive.read(path)
            matches_id = any(key.encode() in raw[:120] for key in wanted)
            loads_mechanics = path.startswith("World/Etudes/") and b'!bp_69bf5090bc7e2f34f83b73e64972f54b' in raw
            if matches_id or loads_mechanics:
                records["blueprints"][path] = json.loads(raw)
    process_env = dict(os.environ, DOTNET_ROOT="C:/Users/Z/AppData/Local/RanRomanceTools/dotnet")
    for name in ("Kingmaker.View.Spawners.CompanionSpawner", "Kingmaker.View.Spawners.UnitSpawnerBase", "Kingmaker.Enums.PetType", "Kingmaker.UnitLogic.Interaction.SpawnerInteractionDialog", "Kingmaker.UnitLogic.Interaction.SpawnerInteraction", "Kingmaker.UnitLogic.Interaction.SpawnerInteractionPart", "Kingmaker.Designers.EventConditionActionSystem.Conditions.UnitIsInAreaPart"):
        result = subprocess.run(["tools/ilspycmd.exe", "-t", name, str(assembly)], env=process_env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
        records["decompiled"][name] = result.stdout
    args.output.write_text(json.dumps(records, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(records['scene_objects'])} scene objects and {len(records['blueprints'])} native records to {args.output}")


if __name__ == "__main__":
    main()
