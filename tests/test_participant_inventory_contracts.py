"""eng7-l05: inventory/binding evidence only; cross-route L1 remains q6a-owned."""
import json
from pathlib import Path
import unittest
from zipfile import ZipFile

from tests.story_fixture import fresh_story
from tools.game_blueprints import game_dir, blueprint_type

ROOT = Path(__file__).resolve().parents[1]


class ParticipantInventoryContractTests(unittest.TestCase):
    def test_r5_aranka_requires_the_matching_copy(self):
        scenes = {s['Id']: s for s in fresh_story()['Scenes']}
        for variant in ('dreamer', 'fallen'):
            for suffix, unit in (('', '430cba7801b149b4e8494ace6baf4f7c'),
                                 ('.yard', 'bd0c4fe722aeef94b8495ac284b96bc8')):
                with self.subTest(variant=variant, placement=suffix):
                    scene = scenes['aranka.react.arueshalae.' + variant + suffix]
                    self.assertEqual(scene.get('AdditionalContactUnits'), [unit])

    def test_r5_delamere_delivery_areas(self):
        scenes = {s['Id']: s for s in fresh_story()['Scenes']}
        temple = 'bb6d82794aae9d94d9cc94d1a05e5f20'
        capital = '2570015799edf594daf2f076f2f975d8'
        for sid, areas in (
            ('delamere.trickster.crypt.stag_alone', [temple]),
            ('delamere.trickster.crypt.stag_late', [temple]),
            ('delamere.trickster.woods.second_hunt_page', [capital, temple]),
            ('delamere.trickster.woods.second_hunt_late', [capital, temple]),
        ):
            with self.subTest(scene=sid):
                self.assertEqual(scenes[sid].get('Areas'), areas)

    def test_r5_delivery_patch_native_evidence(self):
        contract = json.loads((ROOT / "tools/participant_inventory_contracts.json").read_text(encoding="utf-8"))
        with ZipFile(game_dir() / 'blueprints.zip') as archive:
            for guid, evidence in contract['delivery_evidence'].items():
                data = json.loads(archive.read(evidence['path']))
                self.assertEqual(guid, data['AssetId'])
                self.assertEqual(evidence['type'], blueprint_type(data['Data']))
        for patch in contract['delivery_patches']:
            for field, values in patch['fields'].items():
                self.assertIn(field, ('Areas', 'AdditionalContactUnits'))
                self.assertTrue(all(guid in contract['delivery_evidence'] for guid in values))

    def test_mapped_finding_review_is_complete(self):
        contract = json.loads((ROOT / "tools/participant_inventory_contracts.json").read_text(encoding="utf-8"))
        backlog = json.loads((ROOT / "tools/engine_backlog.json").read_text(encoding="utf-8"))
        item = next(i for i in backlog["items"] if i["id"] == "E-Q7-04")
        self.assertEqual({row["id"] for row in contract["finding_review"]}, set(item["finding_ids"]))
        self.assertTrue(all(row["evidence"] for row in contract["finding_review"]))
        payload = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))
        ids = {scene["Id"] for scene in payload["Scenes"]}
        for row in contract["finding_review"]:
            if row["status"] == "no_change_needed":
                self.assertNotIn(row["scene"], ids)

    def test_native_current_readers_have_archive_evidence(self):
        contract = json.loads((ROOT / "tools/participant_inventory_contracts.json").read_text(encoding="utf-8"))
        payload = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))
        with ZipFile(game_dir() / "blueprints.zip") as archive:
            for key, evidence in contract["binding_evidence"].items():
                data = json.loads(archive.read(evidence["path"]))
                self.assertEqual(data["AssetId"], evidence["guid"], key)
                self.assertEqual(blueprint_type(data["Data"]), "BlueprintEtude", key)
                self.assertEqual(payload["Etudes"][key], evidence["guid"], key)
                self.assertNotIn(key, payload["PermanentEtudes"], "Current party readers must not latch past absence")


if __name__ == "__main__":
    unittest.main()
