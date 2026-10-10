import copy
import importlib
import json
import hashlib
import os
import zipfile
from pathlib import Path
import unittest
from unittest.mock import patch

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
        # F11: the mark keeps its saved ID and earned gates, on the jeweller street instead of Yaniel's mark.
        fallback = self.story["Presences"]["eliandra.presence.mark"]
        self.assertEqual({"NearUnit": "bc1093231b1577a4485a730c29595195", "Offset": [-5.2, 3.2]}, fallback["At"])
        self.assertEqual([["eliandra.presence.failed", "fool_king.gone"]], fallback["RequiresAnyGroups"])

    def test_f11_fallbacks_have_independent_anchors_and_keep_spacing(self):
        presences = self.story["Presences"]
        for primary, fallback in (("eliandra.presence", "eliandra.presence.mark"),
                                  ("shamira.presence", "shamira.presence.awning")):
            self.assertNotEqual(presences[primary]["At"]["NearUnit"], presences[fallback]["At"]["NearUnit"])
            bad = copy.deepcopy(self.story)
            bad["Presences"][fallback]["At"] = copy.deepcopy(presences[primary]["At"])
            self.assertTrue(any(fallback in e and "F11" in e for e in check(bad)))
        self.assertEqual({"NearUnit": "15f754455d1d87c42a4e14df456d5415", "Side": "left", "Distance": 6.5},
                         presences["shamira.presence.awning"]["At"])
        bad = copy.deepcopy(self.story)
        bad["Presences"]["eliandra.presence.mark"]["At"] = {
            "NearUnit": "bc1093231b1577a4485a730c29595195", "Side": "left", "Distance": 4.0}
        self.assertTrue(any("eliandra.presence.mark" in e and "spacing" in e for e in check(bad)))

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
        with zipfile.ZipFile(archive_path) as archive:
            sources = list(table["evidence"])
            for area in table["areas"]:
                sources.append(area)
                for unit in area["units"]:
                    sources.extend((unit, unit["membership"], unit["scene_owner"]))
            for source in sources:
                raw = archive.read(source["path"])
                record = json.loads(raw)
                self.assertEqual(source["guid"], record["AssetId"])
                if "pointer" in source:
                    value = record
                    for part in source["pointer"].strip("/").split("/"):
                        value = value[int(part)] if isinstance(value, list) else value[part]
                    self.assertEqual(source["value"], value, source["path"])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        table = json.loads((ROOT / 'tools/drezen_area_chapters.json').read_text(encoding='utf-8'))
        target = table['evidence'][0]['path']
        read = zipfile.ZipFile.read
        def altered(archive, name, *args, **kwargs):
            raw = read(archive, name, *args, **kwargs)
            if name == target:
                record = json.loads(raw)
                record['AssetId'] = '0' * 32
                return json.dumps(record).encode('utf-8')
            return raw
        with patch.object(zipfile.ZipFile, 'read', altered):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_pinned_native_area_and_spawner_evidence()


if __name__ == "__main__":
    unittest.main()
