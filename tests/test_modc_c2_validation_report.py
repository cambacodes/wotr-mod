"""C2 behavioral validation/report regression suite against the managed runner."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class CompleteValidationReportTests(unittest.TestCase):
    def test_real_export_reports_independent_violations(self):
        root = Path(__file__).resolve().parents[1]
        game = Path(os.environ.get("RRT_GAME_DIR", "/wrath"))
        story = json.loads((root / "development/Story.json").read_text(encoding="utf-8"))
        first, second = story["Scenes"][:2]
        expected = [("invalid_scene_kind", first["Id"]),
                    ("invalid_chapter_or_timing_constraints", second["Id"])]
        self.assertNotEqual(first["Id"], second["Id"])
        first["Kind"] = "invalid"
        second["DelayHours"] = -1
        with tempfile.TemporaryDirectory(prefix="rrt-c2-export-") as scratch:
            scratch = Path(scratch)
            mutated = scratch / "story.json"
            mutated.write_text(json.dumps(story, ensure_ascii=False), encoding="utf-8")
            control_identities = []
            for input_path in (root / "development/Story.json", mutated):
                report = scratch / "report.json"
                report.write_text("stale", encoding="utf-8")
                env = dict(os.environ, RRT_VALIDATE_ONLY="1", RRT_VALIDATE_REPORT=str(report))
                command = ["bash", "tools/managed_tests_linux.sh", str(game)]
                if input_path == mutated:
                    command.append(str(input_path))
                result = subprocess.run(command, cwd=root, env=env, text=True, encoding="utf-8",
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
                self.assertIn(result.returncode, (0, 1), f"{command}:\n{result.stdout}")
                self.assertTrue(report.exists(), f"{command}:\n{result.stdout}")
                data = json.loads(report.read_text(encoding="utf-8"))
                self.assertEqual(set(data), {"version", "complete", "errors"})
                self.assertEqual(data["version"], 1)
                self.assertIs(data["complete"], True)
                identities = [(error["code"], error["scene"]) for error in data["errors"]]
                if input_path == mutated:
                    self.assertEqual(result.returncode, 1)
                    self.assertCountEqual(identities, control_identities + expected)
                else:
                    # Export defects belong to the engine gate and route owners. This
                    # regression checks collection without freezing unrelated defects.
                    control_identities = identities
                    for identity in expected:
                        self.assertNotIn(identity, control_identities)
                    self.assertEqual(result.returncode, 1 if identities else 0)
                for error in data["errors"]:
                    self.assertEqual(set(error), {"code", "scene", "detail"})
                    self.assertIsInstance(error["detail"], str)

    def test_managed_validation_report_contract(self):
        root = Path(__file__).resolve().parents[1]
        game = Path(os.environ.get("RRT_GAME_DIR", "/wrath"))
        if not (game / "Wrath_Data" / "Managed").is_dir():
            self.fail("C2 validation requires real game assemblies via RRT_GAME_DIR")
        with tempfile.TemporaryDirectory(prefix="rrt-c2-tests-") as scratch:
            scratch = Path(scratch)
            env = dict(os.environ)
            for key in ("RRT_VALIDATE_ONLY", "RRT_VALIDATE_REPORT", "RRT_TEST_LOAD"):
                env.pop(key, None)
            commands = [
                ["dotnet", "build", "managed-tests/C2ValidationTests.csproj", "-c", "Release", "--nologo", "-v", "quiet",
                 f"-p:GameDir={game}/", f"-p:BaseIntermediateOutputPath={scratch}/obj/", f"-p:OutputPath={scratch}/tests/"],
                ["mono", str(scratch / "tests/C2ValidationTests.exe"), str(game)],
            ]
            for command in commands:
                result = subprocess.run(command, cwd=root, env=env, text=True, encoding="utf-8",
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
                self.assertEqual(result.returncode, 0, f"{command}:\n{result.stdout}")


if __name__ == "__main__":
    unittest.main()
