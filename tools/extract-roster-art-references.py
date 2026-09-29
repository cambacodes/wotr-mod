"""Decode native unit-linked portrait references without editing the images.

Run with the isolated RanRomanceTools/unitypy Python environment.
"""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import UnityPy


UNITS = {
    "AneviaCapital": "Act_3_DemonsHerecy/Drezen/AneviaTirabade_DrezenCapital",
    "IrabethCapital": "Act_3_DemonsHerecy/Drezen/IrabethTirabade_DrezenCapital",
    "VellexiaDefault": "Act_4_MidnightIsles/RaptureOfRupture/Vellexia_Default",
    "VellexiaFirstDate": "Act_4_MidnightIsles/RaptureOfRupture/VellexiaFirstDate",
    "VellexiaSecondDate": "Act_4_MidnightIsles/RaptureOfRupture/VellexiaSecondDate",
    "VellexiaThirdDate": "Act_4_MidnightIsles/RaptureOfRupture/VellexiaThirdDate",
    "Shamira": "Act_4_MidnightIsles/HaremOfArdentDream/Shamira",
    "Herrax": "Act_4_MidnightIsles/TenThousandDelights/Herraxa",
    "Eliandra": "Act_3_DemonsHerecy/PuluraFall/PuluraFall_Eliandra",
    "YanielRescued": "Act_2_SwordOfValor/DrezenCitadelLevel2/Yaniel_DrezenCitadelLevel2",
    "YanielFane": "Act_3_DemonsHerecy/MidnightFane/Yaniel",
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path("C:/Program Files (x86)/Steam/steamapps/common/Pathfinder Second Adventure"))
    parser.add_argument("--output", type=Path, default=Path("reference/art-review/roster-native"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    bundle = args.game / "Bundles/portraits"
    env = UnityPy.load(str(bundle))
    textures = {key: obj for key, obj in env.container.items()
                if obj.m_PathID and obj.type.name == "Texture2D"}
    records = []
    with ZipFile(args.game / "blueprints.zip") as archive:
        portraits = {}
        for name in archive.namelist():
            if name.startswith(("Units/Portraits/", "Units/PortraitsGenerated/")) and name.endswith(".jbp"):
                raw = archive.read(name)
                data = json.loads(raw)
                portraits[data["AssetId"]] = (name, raw, data["Data"])
        for label, suffix in UNITS.items():
            path = "Units/NPC/Unique/" + suffix + ".jbp"
            raw = archive.read(path)
            unit = json.loads(raw)
            portrait_id = unit["Data"]["m_Portrait"].removeprefix("!bp_")
            portrait_path, portrait_raw, portrait = portraits[portrait_id]
            (args.output / (label + "-unit.jbp")).write_bytes(raw)
            (args.output / (label + "-portrait.jbp")).write_bytes(portrait_raw)
            record = {"label": label, "unit_path": path, "unit_id": unit["AssetId"],
                      "unit_sha256": digest(raw), "prefab": unit["Data"].get("Prefab"),
                      "portrait_path": portrait_path, "portrait_id": portrait_id,
                      "portrait_sha256": digest(portrait_raw), "images": []}
            for field in ("m_PortraitImage", "m_HalfLengthImage", "m_FullLengthImage"):
                asset = portrait["Data"].get(field)
                image_id = asset.get("AssetId") if asset else None
                entry = {"field": field, "asset_id": image_id}
                obj = textures.get(image_id)
                if obj is None:
                    entry["status"] = "not_in_portraits_bundle"
                else:
                    texture = obj.read()
                    output = args.output / (label + "-" + field + ".png")
                    texture.image.save(output)
                    entry.update(status="decoded", file=output.name, name=texture.m_Name,
                                 path_id=obj.path_id, width=texture.m_Width, height=texture.m_Height,
                                 sha256=digest(output.read_bytes()))
                record["images"].append(entry)
            records.append(record)
    result = {"bundle": str(bundle), "bundle_sha256": digest(bundle.read_bytes()),
              "method": "UnityPy native texture decode at original dimensions, without image editing; no prefab render",
              "units": records}
    (args.output / "provenance.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for record in records:
        print(record["label"] + ": " + ", ".join(f"{i['field']}={i['status']}" for i in record["images"]))
    assert len(records) == len(UNITS)
    assert all(i["status"] == "decoded" for record in records for i in record["images"]), "Unresolved native image links"


if __name__ == "__main__":
    main()
