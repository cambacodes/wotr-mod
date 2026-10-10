"""C2 behavioral validation/report regression suite against the managed runner."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class CompleteValidationReportTests(unittest.TestCase):
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
