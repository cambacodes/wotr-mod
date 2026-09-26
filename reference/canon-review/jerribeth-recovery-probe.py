"""Read exact installed Jerribeth references; never modify the archive or game state."""
import hashlib
import json
from pathlib import Path
import zipfile
import sys

GAME = Path(r"D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure")
TARGETS = {
    "native_unavailable": "cd8666952065ce74d94d960a23482133",
    "act4_unit": "417ce3dcf3a9707488f2b9b2a790814b",
    "sanctum_unit": "bb9fe2c12d6941a43bfd5d5090ac97b9",
    "patron_dead": "72e423c719ed9d44fa432a6b9629babd",
    "sanctum_location": "669220945fa20fa4a9317dea3618a19c",
    "sanctum_plaque": "61a1f58e-a948-4cd7-80f8-96b16dac28df",
    "demon_brain": "f8ff8935f7859494fb18e056657d30ff",
    "base_faction": "0f539babafb47fe4586b719d02aff7c4",
    "sanctum_faction": "d64258e86eeb1d8479f35a9b16f6590a",
}


def keys(value):
    if isinstance(value, dict):
        if value.get("m_Key"):
            yield value["m_Key"]
        if value.get("stringkey"):
            yield value["stringkey"]
        for child in value.values():
            yield from keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from keys(child)


def main():
    localization = json.loads((GAME / "Wrath_Data/StreamingAssets/Localization/enGB.json").read_text(encoding="utf-8-sig"))["strings"]
    records = []
    hits = {name: [] for name in TARGETS}
    examined = 0
    with zipfile.ZipFile(GAME / "blueprints.zip") as archive:
        for path in archive.namelist():
            if not path.endswith(".jbp"):
                continue
            examined += 1
            raw = archive.read(path)
            matched = [name for name, guid in TARGETS.items() if guid.encode() in raw]
            definitions = {"demon_brain", "base_faction", "sanctum_faction"}
            if any(name in definitions for name in matched):
                asset_id = json.loads(raw).get("AssetId")
                matched = [name for name in matched if name not in definitions or TARGETS[name] == asset_id]
            named = "jerribeth" in path.lower() or "jerribetn" in path.lower()
            if not matched and not named:
                continue
            record = json.loads(raw)
            for name in matched:
                hits[name].append(path)
            records.append({"path": path, "sha256": hashlib.sha256(raw).hexdigest().upper(),
                            "targets": matched, "record": record,
                            "localized": {key: localization[key] for key in set(keys(record)) if key in localization}})
    output = Path(__file__).with_name("jerribeth-recovery-records.json")
    output.write_text(json.dumps({"archive": str(GAME / "blueprints.zip"),
                                 "blueprints_examined": examined, "targets": TARGETS,
                                 "hits": hits, "records": records}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Read {examined} blueprint records; retained {len(records)} exact references.")
    for name, paths in hits.items():
        print(name, len(paths))


def delivery_records():
    """Run with the existing UnityPy environment; append exact delivery evidence."""
    import UnityPy

    output = Path(__file__).with_name("jerribeth-recovery-records.json")
    records = json.loads(output.read_text(encoding="utf-8"))
    delivery = {}
    for bundle, selected in (
        ("f8acb79bcccd0fb4a93db8e50a0d7c82.unit", None),
        ("drezencapital_default_mechanics.scenes", {468}),
    ):
        path = GAME / "Bundles" / bundle
        env = UnityPy.load(str(path))
        chosen = []
        for obj in env.objects:
            if obj.type.name != "GameObject" or selected is not None and obj.path_id not in selected:
                continue
            data = obj.read_typetree()
            local = {item.path_id: item for item in env.objects if item.assets_file == obj.assets_file}
            components = []
            for component in data["m_Component"]:
                item = local[component["component"]["m_PathID"]]
                components.append({"path_id": item.path_id, "type": item.type.name, "data": item.read_typetree()})
            if selected is None and not any("m_Corpulence" in c["data"] for c in components):
                continue
            parents = []
            transform = next(c["data"] for c in components if c["type"] == "Transform")
            parent = transform["m_Father"]["m_PathID"]
            while parent:
                value = local[parent].read_typetree()
                parents.append({"path_id": parent, "data": value})
                parent = value["m_Father"]["m_PathID"]
            chosen.append({"path_id": obj.path_id, "data": data, "components": components, "parents": parents})
        delivery[bundle] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest().upper(), "objects": chosen}
    # Retain prior parsed navigation evidence only if its original bundle still matches.
    prior = json.loads(output.with_name("terendelev-actor-blueprint-records.json").read_text())
    nav = GAME / "Bundles/drezencapital.nav"
    current_hash = hashlib.sha256(nav.read_bytes()).hexdigest().upper()
    assert current_hash == prior["sha256"]["drezencapital.nav"].upper()
    delivery["navigation_prior_verified_bundle"] = {"sha256": current_hash, "triangles": prior["navigation_triangle_audit"],
        "source": "terendelev-actor-blueprint-records.json", "note": "Existing parsed triangle evidence, bundle hash rechecked; not a live obstruction test."}
    records["delivery"] = delivery
    output.write_text(json.dumps(records, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print("Recorded native Jerribeth collider, capital anchor and parent transforms; navigation bundle hash matches prior parsed evidence.")


if __name__ == "__main__":
    delivery_records() if "--delivery" in sys.argv else main()
