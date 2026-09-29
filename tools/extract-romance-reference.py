"""Extract local dialogue evidence for writing and integration; never ship game text."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    "konomi": ("World/Crusade/RankUps/Diplomacy/",),
    "jerribeth": ("World/Dialogs/c3/Wintersun/JerribethReveal/", "World/Dialogs/c3/IvorySanctum/Jerribeth", "World/Dialogs/c4/RaptureOfRupture/Jerribeth_"),
    "vellexia": ("World/Dialogs/c4/RaptureOfRupture/", "World/Dialogs/c5/Mythic_Demon/Conspirators/Vellexia_", "World/Dialogs/c5/Mythic_Demon/Demons_InTheDrezen/Vellexia_"),
    "kiana": ("World/Dialogs/Companions/CompanionQuests/Seelah/Q2_", "World/Dialogs/Companions/CompanionQuests/Seelah/Q3_"),
    "seelah": ("World/Dialogs/Companions/CompanionDialogues/Seelah/", "World/Dialogs/Companions/CompanionQuests/Seelah/"),
    "arsinoe": ("World/Dialogs/NPC_Common/VendorArsinoe/", "World/Dialogs/Companions/CompanionRomances/Lann/Event3/ArsinoeWedding/"),
    "gesmerha": ("World/Dialogs/c3/Wintersun/BlindCarver/", "World/Dialogs/c3/Wintersun/PeacefulWintersun/PeacefulWoodCarver/", "World/Dialogs/c5/KTC_WintersunHelp/"),
    "chivarro": ("World/Dialogs/c4/TenThousandDelights/Chivarro_dialogue/", "World/Dialogs/c4/Minagho_Desperation/MinaghoAfterCombat/"),
    "wenduag": ("World/Dialogs/Companions/CompanionDialogues/Wenduag/", "World/Dialogs/Companions/CompanionRomances/Wenduag/ThatIsFinal/"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure"))
    args = parser.parse_args()
    destination = ROOT / "reference/expansion"
    destination.mkdir(parents=True, exist_ok=True)
    strings = json.loads((args.game / "Wrath_Data/StreamingAssets/Localization/enGB.json").read_text(encoding="utf-8-sig"))["strings"]
    with ZipFile(args.game / "blueprints.zip") as archive:
        records = {}
        etudes = {}
        for name in archive.namelist():
            if not name.endswith(".jbp"):
                continue
            if name.startswith("World/Etudes/Common/WrathOfTheRighteous/"):
                obj = json.loads(archive.read(name))
                etudes[name] = obj["AssetId"]
            if any(name.startswith(prefix) for prefixes in GROUPS.values() for prefix in prefixes):
                obj = json.loads(archive.read(name))
                data = obj["Data"]
                key = (data.get("Text") or {}).get("m_Key", "")
                records[name] = {"guid": obj["AssetId"], "type": data.get("$type", "").split(", ")[-1], "text": strings.get(key, ""), "data": data}
        (destination / "blueprints.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        (destination / "etudes.json").write_text(json.dumps(etudes, indent=2), encoding="utf-8")
        for character, prefixes in GROUPS.items():
            blocks = [f"{path}\nGUID: {record['guid']}\n{record['text']}\n" for path, record in records.items() if path.startswith(prefixes) and record["text"]]
            (destination / f"{character}.txt").write_text("\n".join(blocks), encoding="utf-8")
            print(f"{character}: {len(blocks)} localized dialogue entries")
        print(f"Extracted {len(records)} blueprints and {len(etudes)} etude references to {destination}")


if __name__ == "__main__":
    main()
