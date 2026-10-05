import copy
import importlib
import json
import hashlib
import os
import zipfile
from pathlib import Path
import unittest

from tools.drezen_placement_lint import check, CAPITAL, RETURN

ROOT = Path(__file__).resolve().parents[1]


class DrezenPlacementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))

    def test_all_exported_routes_and_mutations(self):
        self.assertEqual([], check(self.story))
        for mutation in ("return_anchor", "chapter_four", "chapter_six", "unknown_area", "overlap"):
            bad = copy.deepcopy(self.story)
            p = bad["Presences"]["mielarah.presence"]
            if mutation == "return_anchor":
                p["Area"] = RETURN  # The trader exists in capital, not in the siege.
            elif mutation == "unknown_area":
                p["Area"] = "missing"
            elif mutation in ("chapter_four", "chapter_six"):
                p["MinChapter"] = p["MaxChapter"] = 4 if mutation == "chapter_four" else 6
            else:
                p["At"] = copy.deepcopy(bad["Presences"]["galfrey.presence.stall"]["At"])
            self.assertTrue(check(bad), mutation)

    def test_f10_transient_anchors_roofs_and_roaming_lane(self):
        for key in ("herrax.presence.rokhorn", "shamira.presence", "eliandra.presence", "jerribeth.presence"):
            for anchor in ("cc50a88bbd8dd3e4da066d33d14fdfc8", "0f12118177d102f428a3b30b15b132eb",
                           "a380d926e92f70e429681eb9654478f9", "bad9f602b81a80047ac470b01ebe65a9"):
                bad = copy.deepcopy(self.story)
                bad["Presences"][key]["At"]["NearUnit"] = anchor
                self.assertTrue(any(key in e and "F10" in e for e in check(bad)), (key, anchor))
            bad = copy.deepcopy(self.story)
            bad["Presences"][key]["At"]["Side"] = "behind"
            self.assertTrue(any(key in e and "roof" in e for e in check(bad)), key)
        # The native-mark fallback is still a locator, with its earned gates untouched.
        fallback = self.story["Presences"]["eliandra.presence.mark"]
        self.assertEqual("9a41b047-9314-4719-a915-9c24aedf3e95", fallback["At"]["Locator"])
        self.assertEqual([["eliandra.presence.failed", "fool_king.gone"]], fallback["RequiresAnyGroups"])

    def test_every_authored_presence_declaration(self):
        # Sweep route modules too, including declarations not currently registered.
        for path in sorted((ROOT / "storylines").glob("*.py")):
            module = importlib.import_module("storylines." + path.stem)
            presences = getattr(module, "PRESENCES", {})
            if presences:
                with self.subTest(module=path.stem):
                    self.assertEqual([], check({"Presences": presences}))

    def test_explicit_scene_chapters_are_not_hidden_by_a_wide_window(self):
        scene = {"Id": "fixture", "Owner": "Wenduag", "Areas": [CAPITAL],
                 "MinChapter": 3, "MaxChapter": 5, "Chapters": [3, 4, 5]}
        self.assertTrue(check({"Scenes": [scene]}))
        scene["Chapters"] = [3, 5]
        self.assertEqual([], check({"Scenes": [scene]}))

    def test_pinned_native_area_and_spawner_evidence(self):
        table = json.loads((ROOT / "tools/drezen_area_chapters.json").read_text(encoding="utf-8"))
        candidates = [Path(os.environ.get("RRT_BLUEPRINTS_ZIP") or "/wrath/blueprints.zip"),
                      Path(os.environ.get("RRT_GAME_DIR") or
                           r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure") / "blueprints.zip"]
        archive_path = next((p for p in candidates if p.exists()), None)
        self.assertIsNotNone(archive_path, "native blueprint archive required (RRT_BLUEPRINTS_ZIP / RRT_GAME_DIR)")
        with zipfile.ZipFile(archive_path) as archive:
            sources = list(table["evidence"])
            for area in table["areas"]:
                sources.append(area)
                for unit in area["units"]:
                    sources.extend((unit, unit["membership"], unit["scene_owner"]))
            for source in sources:
                raw = archive.read(source["path"])
                self.assertEqual(source["sha256"], hashlib.sha256(raw).hexdigest())
                record = json.loads(raw)
                self.assertEqual(source["guid"], record["AssetId"])
                if "pointer" in source:
                    value = record
                    for part in source["pointer"].strip("/").split("/"):
                        value = value[int(part)] if isinstance(value, list) else value[part]
                    self.assertEqual(source["value"], value, source["path"])


if __name__ == "__main__":
    unittest.main()
