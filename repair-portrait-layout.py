"""Repair named NPC overrides; leave companion portraits and original backups in place."""
import hashlib
import json
import shutil
import struct
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
MOD = Path(r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure\Mods\CustomNpcPortraits")
USER = Path.home() / "AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous"
SIZES = {"Fulllength.png": (692, 1024), "Medium.png": (330, 432), "Small.png": (185, 242)}
MISPLACED_NPCS = ("Horgus Gwerm", "Hulrun", "Queen Galfrey", "Storyteller", "Terendelev", "Staunton Vhane")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    backup = ROOT / "backups" / ("portrait-layout-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
    changes, audit = [], []

    def copy(source, target):
        if target.exists() and digest(source) == digest(target):
            return
        saved = None
        if target.exists():
            backup.mkdir(parents=True, exist_ok=True)
            saved = backup / f"{len(changes)}-{target.name}"
            shutil.copy2(target, saved)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        changes.append(dict(target=str(target), backup=str(saved) if saved else None, sha256=digest(target)))

    # These are NPCs, despite having been placed in the companion portrait directory.
    for name in MISPLACED_NPCS:
        source = USER / "Portraits" / ("CustomNpcPortraits - " + name)
        if not source.is_dir():
            continue
        for size in SIZES:
            if (source / size).is_file():
                copy(source / size, MOD / "Portraits - Npc" / name / size)

    for directory in sorted((MOD / "Portraits - Npc").iterdir()):
        if not directory.is_dir():
            continue
        files = {}
        for size in SIZES:
            source = directory / size
            # One installed pack has an unnecessary second Minagho directory.
            if not source.is_file() and (directory / directory.name / size).is_file():
                source = directory / directory.name / size
            if source.is_file():
                files[size] = source
        if "Medium.png" not in files:
            audit.append(dict(name=directory.name, status="incomplete NPC pack; no Medium.png", files=list(files)))
            continue
        for size, source in files.items():
            copy(source, USER / "Portraits - Npc" / directory.name / size)
        audit.append(dict(name=directory.name, status="NPC runtime override installed", files=list(files)))

    for directory in sorted((USER / "Portraits").glob("CustomNpcPortraits - *")):
        images = []
        for name, expected in SIZES.items():
            image = directory / name
            if not image.is_file():
                continue
            header = image.read_bytes()[:24]
            if header[:8] != b"\x89PNG\r\n\x1a\n":
                raise ValueError(f"Invalid PNG: {image}")
            dimensions = struct.unpack(">II", header[16:24])
            images.append(dict(file=name, dimensions=dimensions, standard_size=dimensions == expected))
        audit.append(dict(name=directory.name, status="companion-layout source preserved", files=images))

    backup.mkdir(parents=True, exist_ok=True)
    (backup / "manifest.json").write_text(json.dumps(changes, indent=2) + "\n", encoding="utf8")
    (ROOT / "portrait-audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf8")
    print(f"Installed {len(changes)} portrait files with backups. Audited {len(audit)} named packs.")
    for entry in audit:
        if entry["status"].startswith("incomplete"):
            print(entry["name"], entry["status"])


if __name__ == "__main__":
    main()
