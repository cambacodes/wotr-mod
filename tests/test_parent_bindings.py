"""Evidence pinning must fail closed when parent code or binding identity changes."""
import hashlib
import json
from pathlib import Path
import sys
from tests.writable_temp import writable_temp
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from parent_bindings import load_parent_bindings


class ParentBindingTests(unittest.TestCase):
    def test_evidence_pin_and_identity(self):
        with writable_temp() as directory:
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
