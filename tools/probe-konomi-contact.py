"""Record the installed Konomi actor and dialogue link; run with UnityPy Python."""
import hashlib
import json
from pathlib import Path
import zipfile

import UnityPy


def main():
    game = Path("C:/Program Files (x86)/Steam/steamapps/common/Pathfinder Second Adventure")
    bundle = game / "Bundles/drezencapital_default_mechanics.scenes"
    env = UnityPy.load(str(bundle))
    records = {"bundle": str(bundle), "sha256": hashlib.sha256(bundle.read_bytes()).hexdigest().upper(),
               "objects": [], "blueprints": {}}
    for obj in env.objects:
        if obj.type.name != "GameObject":
            continue
        data = obj.read_typetree()
        if data.get("m_Name") not in ("RankUpOfficer_Diplomacy", "DiplomacyOfficer_Position"):
            continue
        local = {item.path_id: item for item in env.objects if item.assets_file == obj.assets_file}
        components = []
        for component in data["m_Component"]:
            item = local[component["component"]["m_PathID"]]
            components.append({"path_id": item.path_id, "type": item.type.name, "data": item.read_typetree()})
        records["objects"].append({"path_id": obj.path_id, "data": data, "components": components})
    ids = {"ca2d58c5c65723945857e04fb85d30ce", "a81655ed97277974e947c1aaf9e33525",
           "0dc8b8604bb33c846a63f3eb62443674", "b5f301fbc4c44535a6309d610d5bd28a"}
    with zipfile.ZipFile(game / "blueprints.zip") as archive:
        for path in archive.namelist():
            if not path.endswith(".jbp") or not path.startswith(("Units/", "World/Crusade/RankUps/Diplomacy/", "World/Etudes/")):
                continue
            raw = archive.read(path)
            if any(guid.encode() in raw[:150] for guid in ids):
                records["blueprints"][path] = json.loads(raw)
    actor = next(o for o in records["objects"] if o["data"]["m_Name"] == "RankUpOfficer_Diplomacy")
    components = [c["data"] for c in actor["components"]]
    assert any(c.get("UniqueId") == "c658c4cf-116e-4b61-9ff9-8905bcf4fd6b"
               and c.get("m_Blueprint", {}).get("guid") == "ca2d58c5c65723945857e04fb85d30ce" for c in components)
    assert any(c.get("m_Dialog", {}).get("guid") == "a81655ed97277974e947c1aaf9e33525" for c in components)
    assert len(records["blueprints"]) == 4, "Expected typed unit, dialogue, answer-list and presence records"
    output = Path("reference/canon-review/konomi-contact-records.json")
    output.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: {len(records['objects'])} scene objects and four native blueprints -> {output}")


if __name__ == "__main__":
    main()
