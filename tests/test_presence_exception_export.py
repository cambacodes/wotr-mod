import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from tools.presence_exception_schema import errors
from tools.presence_failure_lint import check as receipt_errors

ROOT = Path(__file__).resolve().parents[1]


class PresenceExceptionExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8"))

    def test_fresh_process_parity(self):
        with tempfile.TemporaryDirectory(prefix="eng7-l06-") as scratch:
            story = Path(scratch) / "Story.json"
            story.write_text(json.dumps(self.story), encoding="utf-8")
            run = subprocess.run([sys.executable, str(ROOT / "tools/earned_presence_lint.py"), "--story", str(story)],
                                 cwd=scratch, text=True, capture_output=True)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        for name in ("aranka.presence", "nenio.presence", "nenio.presence.arcade"):
            self.assertIn(name, self.story["PresenceExceptions"])

    def test_undeclared_and_arbitrary_bypass(self):
        self.assertEqual([], errors(self.story))
        bad = copy.deepcopy(self.story)
        bad["PresenceExceptions"].pop("nenio.presence")
        self.assertTrue(errors(bad))
        bad = copy.deepcopy(self.story)
        bad["DerivedForbids"]["nenio.presence.route_open"].remove("nenio.closed")
        self.assertTrue(errors(bad))
        for loss in ("nenio.dead", "nenio.dissolved", "nenio.killed_by_commander"):
            bad = copy.deepcopy(self.story)
            bad["PresenceExceptions"]["nenio.presence"]["AbsentLosses"][loss] = "Arbitrary loss bypass"
            self.assertTrue(errors(bad))

    def test_receipt_lint_and_mutations(self):
        self.assertEqual([], receipt_errors(self.story))
        bad = copy.deepcopy(self.story)
        bad["PresenceFailureReceipts"]["gesmerha.presence"]["Requires"] = []
        self.assertTrue(receipt_errors(bad))
        for suffix in ("commit", "commit_mourned", "unvisited"):
            bad = copy.deepcopy(self.story)
            scene = next(s for s in bad["Scenes"] if s["Id"] == "gesmerha.trickster.epilogue." + suffix)
            scene.setdefault("Requires", []).append("gesmerha.presence.failed")
            self.assertTrue(receipt_errors(bad), suffix)
        bad = copy.deepcopy(self.story)
        bad["Derived"]["gesmerha.trickster.late_committed"][-1][-1] = "gesmerha.presence.failed"
        self.assertTrue(receipt_errors(bad))
