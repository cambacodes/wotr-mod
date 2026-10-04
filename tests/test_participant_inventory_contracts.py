"""eng7-l05: inventory/binding evidence only; cross-route L1 remains q6a-owned."""
import json
from pathlib import Path
import unittest
from zipfile import ZipFile

from tools.game_blueprints import game_dir, blueprint_type

ROOT = Path(__file__).resolve().parents[1]


class ParticipantInventoryContractTests(unittest.TestCase):
    def test_mapped_finding_review_is_complete(self):
        contract = json.loads((ROOT / "tools/participant_inventory_contracts.json").read_text())
        backlog = json.loads((ROOT / "tools/engine_backlog.json").read_text())
        item = next(i for i in backlog["items"] if i["id"] == "E-Q7-04")
        self.assertEqual({row["id"] for row in contract["finding_review"]}, set(item["finding_ids"]))
        self.assertTrue(all(row["evidence"] for row in contract["finding_review"]))
        payload = json.loads((ROOT / "development/Story.json").read_text())
        ids = {scene["Id"] for scene in payload["Scenes"]}
        for row in contract["finding_review"]:
            if row["status"] == "no_change_needed":
                self.assertNotIn(row["scene"], ids)

    def test_native_current_readers_have_archive_evidence(self):
        contract = json.loads((ROOT / "tools/participant_inventory_contracts.json").read_text())
        payload = json.loads((ROOT / "development/Story.json").read_text())
        with ZipFile(game_dir() / "blueprints.zip") as archive:
            for key, evidence in contract["binding_evidence"].items():
                data = json.loads(archive.read(evidence["path"]))
                self.assertEqual(data["AssetId"], evidence["guid"], key)
                self.assertEqual(blueprint_type(data["Data"]), "BlueprintEtude", key)
                self.assertEqual(payload["Etudes"][key], evidence["guid"], key)
                self.assertNotIn(key, payload["PermanentEtudes"], "Current party readers must not latch past absence")


if __name__ == "__main__":
    unittest.main()
