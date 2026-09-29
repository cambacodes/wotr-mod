"""Extract native capital objects for both wives; run with the UnityPy interpreter."""
import hashlib
import json
from pathlib import Path
import zipfile

import UnityPy


def main():
    bundle = Path("C:/Program Files (x86)/Steam/steamapps/common/Pathfinder Second Adventure/Bundles/drezencapital_default_mechanics.scenes")
    env = UnityPy.load(str(bundle))
    objects = list(env.objects)
    result = {"bundle": str(bundle), "sha256": hashlib.sha256(bundle.read_bytes()).hexdigest().upper(), "objects": []}
    for obj in objects:
        if obj.type.name != "GameObject":
            continue
        data = obj.read_typetree()
        if not any(name in data.get("m_Name", "").lower() for name in ("anevia", "irabeth")):
            continue
        local = {item.path_id: item for item in objects if item.assets_file == obj.assets_file}
        components = []
        for pointer in data["m_Component"]:
            item = local[pointer["component"]["m_PathID"]]
            components.append({"path_id": item.path_id, "type": item.type.name, "data": item.read_typetree()})
        result["objects"].append({"path_id": obj.path_id, "data": data, "components": components})
        print(data["m_Name"], [(c["data"].get("UniqueId"), c["data"].get("m_Blueprint"), c["data"].get("m_Dialog")) for c in components if c["data"].get("m_Blueprint") or c["data"].get("m_Dialog")])
    ids = {"33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276"}
    for obj in result["objects"]:
        for component in obj["components"]:
            for field in ("m_Blueprint", "m_Dialog"):
                reference = component["data"].get(field)
                if reference:
                    ids.add(reference["guid"])
    result["blueprints"] = {}
    with zipfile.ZipFile(bundle.parent.parent / "blueprints.zip") as archive:
        for path in archive.namelist():
            if not path.endswith(".jbp") or not any(name in path.lower() for name in ("anevia", "irabeth")):
                continue
            raw = archive.read(path)
            if any(identity.encode() in raw[:150] for identity in ids):
                record = json.loads(raw)
                result["blueprints"][path] = {"sha256": hashlib.sha256(raw).hexdigest().upper(), "record": record}
                print(record["AssetId"], path)
    found = {value["record"]["AssetId"] for value in result["blueprints"].values()}
    assert found == ids, f"Unresolved typed targets: {ids - found}"
    output = Path("reference/canon-review/tirabade-capital-contact-records.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Recorded {len(result['objects'])} matching objects; loaded actor availability is not established.")


if __name__ == "__main__":
    main()
