"""Evidence pinning must fail closed when parent code or binding identity changes."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from tests.temp_fixtures import temporary_directory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from parent_bindings import load_parent_bindings


class ParentBindingTests(unittest.TestCase):
    @unittest.skipIf(os.name == "nt", "POSIX relocation of reviewed Windows paths")
    def test_relocated_windows_manifest_keeps_assembly_pin(self):
        with tempfile.TemporaryDirectory(prefix="rrt-parent-relocation-") as directory:
            root = Path(directory)
            assembly = root / "Mods" / "RanRomance" / "RanRomance.dll"
            assembly.parent.mkdir(parents=True)
            assembly.write_bytes(b"reviewed parent")
            manifest = {
                "AssemblyPath": r"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure\Mods\RanRomance\RanRomance.dll",
                "AssemblySha256": hashlib.sha256(assembly.read_bytes()).hexdigest(),
                "Bindings": [],
            }
            path = root / "bindings.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with patch("parent_bindings.GAME_DIR", str(root)):
                self.assertEqual(load_parent_bindings(path), {})
                assembly.write_bytes(b"unreviewed parent")
                with self.assertRaisesRegex(ValueError, "assembly differs"):
                    load_parent_bindings(path)

    def test_evidence_pin_and_identity(self):
        with temporary_directory() as directory:
            root = Path(directory)
            assembly = root / "fixture.dll"
            assembly.write_bytes(b"test-only assembly identity")
            guid = "6178470b05c75484085753b821a6a614"
            record = {"Guid": guid, "Type": "BlueprintEtude", "Source": "Fixture.Configure",
                      "Evidence": f'EtudeConfigurator.New("Fixture", "{guid}")'}
            manifest = {"AssemblyPath": str(assembly),
                        "AssemblySha256": hashlib.sha256(assembly.read_bytes()).hexdigest(),
                        "Bindings": [record]}
            path = root / "bindings.json"

            def read():
                path.write_text(json.dumps(manifest), encoding="utf-8")
                return load_parent_bindings(path)

            self.assertEqual(read()[guid]["provenance"], "reviewed-parent-source")
            assembly.write_bytes(b"different version")
            with self.assertRaisesRegex(ValueError, "assembly differs"):
                read()
            assembly.write_bytes(b"test-only assembly identity")
            record["Type"] = "BlueprintQuest"
            with self.assertRaisesRegex(ValueError, "identity/type"):
                read()
            record["Type"] = "BlueprintEtude"
            page = {"Guid": "951e4432cf844a36a8a222b27589fb43", "Type": "BlueprintBookPage",
                    "Source": "Fixture.Page", "Evidence": 'BookPageConfigurator.New("Page", "951e4432cf844a36a8a222b27589fb43")'}
            manifest["Bindings"].append(page)
            self.assertEqual(read()[page["Guid"]]["type"], "BlueprintBookPage")
            page["Evidence"] = page["Evidence"].replace("BookPageConfigurator", "CueConfigurator")
            with self.assertRaisesRegex(ValueError, "identity/type"):
                read()
            manifest["Bindings"].pop()
            manifest["Bindings"].append(dict(record))
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                read()
            manifest["Bindings"].pop()
            record["Evidence"] = 'EtudeConfigurator.New("Other", "00000000000000000000000000000000")'
            with self.assertRaisesRegex(ValueError, "identity/type"):
                read()


if __name__ == "__main__":
    unittest.main()
