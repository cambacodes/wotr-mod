"""Print installed native contact/storage evidence without changing game assets."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path("D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure"))
    args = parser.parse_args()
    assembly = args.game / "Wrath_Data/Managed/Assembly-CSharp.dll"
    print("Assembly SHA256", hashlib.sha256(assembly.read_bytes()).hexdigest().upper())
    env = dict(os.environ, DOTNET_ROOT="C:/Users/Z/AppData/Local/RanRomanceTools/dotnet")
    types = {
        "Kingmaker.EntitySystem.EntityPool`1": ("HandleAdded",),
        "Kingmaker.EntitySystem.EntityPoolEnumerator`1": ("MoveNext",),
        "Kingmaker.EntitySystem.EntityDataBase": ("ShouldBeEnumeratedByEntityPoolEnumerator", "DetachView", "AttachView"),
        "Kingmaker.EntitySystem.SceneEntitiesState": ("IsSceneLoaded =>", "AddEntityData"),
        "Kingmaker.EntitySystem.AreaPersistentState": ("AllEntityData",),
        "Kingmaker.UnitLogic.FactLogic.AddPet": ("SpawnUnit(", "SetMaster(", "IsInGame ="),
        "Kingmaker.View.Spawners.CompanionSpawner": ("GetMyCompanion", "PlaceCompanion", "ShouldShowUnit"),
        "Kingmaker.View.EntityViewBase": ("AttachToData(", "DetachFromData(", "UpdateViewActive()"),
        "Kingmaker.EntitySystem.Persistence.Scenes.SceneLoader": ("CrossSceneState, Enumerable", "CrossSceneRoot : DynamicRoot", "allCrossSceneUnit.IsInGame =", "UnloadEntitiesCoroutine("),
    }
    for name, needles in types.items():
        result = subprocess.run(["tools/ilspycmd.exe", "-t", name, str(assembly)], env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
        lines = result.stdout.splitlines()
        indices = set()
        for i, line in enumerate(lines):
            if any(needle in line for needle in needles):
                indices.update(range(max(0, i - 2), min(len(lines), i + 24)))
        assert indices, f"No requested evidence in {name}"
        print("\nTYPE", name)
        for i in sorted(indices):
            print(f"{i + 1}: {lines[i]}")


if __name__ == "__main__":
    main()
