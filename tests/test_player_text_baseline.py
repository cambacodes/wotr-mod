"""eng7-f2: shipped reviews remain visible; baseline cannot admit new text."""
import unittest
from tools import player_text_baseline as baseline, player_text_lint as lint


class PlayerTextBaselineTests(unittest.TestCase):
    def fixture(self, text):
        return {"Scenes": [{"Id": "fixture", "Nodes": [{"Id": "start", "Text": text}]}]}

    def test_new_text_and_duplicate_findings_fail(self):
        story = self.fixture('"A registered caller waits."')
        rows = lint.check(story)["review"]
        self.assertTrue(rows)
        self.assertEqual(baseline.new_findings(story, rows, {}), [{**r, "severity": "hard"} for r in rows])
        key = baseline.fingerprint(rows[0], story["Scenes"][0]["Nodes"][0]["Text"])
        policy = {"findings": {key: 1}}
        self.assertFalse(baseline.new_findings(story, rows[:1], policy))
        self.assertEqual(len(baseline.new_findings(story, rows[:1] * 2, policy)), 1)
        changed = self.fixture('"A registered caller waits again."')
        self.assertTrue(baseline.new_findings(changed, lint.check(changed)["review"], policy))

    def test_registered_reviews_are_retained(self):
        import subprocess
        import sys
        from pathlib import Path
        # The export CLI builds once; other tests repeatedly mutate module-level
        # authoring objects, so mirror the gate in a fresh authoring process.
        script = '''import expansion
from tools import player_text_lint as lint, player_text_baseline as baseline
story = expansion.make_expansion()
rows = lint.check(story)["review"]
assert rows
assert not baseline.new_findings(story, rows)
'''
        completed = subprocess.run([sys.executable, '-B', '-c', script],
                                   cwd=Path(__file__).resolve().parents[1], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_new_therapy_review_requires_a_budget(self):
        story = self.fixture('"You have my permission."')
        result = lint.check(story)
        self.assertTrue(baseline.new_findings(story, result['review'], {}, result['therapy_counts']))
        self.assertFalse(baseline.new_findings(story, result['review'],
                         {'therapy_counts': result['therapy_counts']}, result['therapy_counts']))
