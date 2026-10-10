import copy
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'tools'))
from storylines.kiana_native import NATIVE_TEXT_EDITS
from rrt_verify import Model, validate

class KianaNativeTextTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from tests.story_fixture import fresh_story
        cls.story = fresh_story()

    def test_reviewed_fields_match_canon_evidence(self):
        evidence = json.loads((ROOT / 'tests/KianaQ3TextEvidence.json').read_text(encoding='utf-8'))
        self.assertEqual(set(NATIVE_TEXT_EDITS), set(evidence))
        for field, edit in NATIVE_TEXT_EDITS.items():
            self.assertEqual((edit['Type'], edit['Key']), (evidence[field]['Type'], evidence[field]['Key']), field)
            for variant in edit['Variants']:
                self.assertTrue(all(('trickster.now' in group for group in variant['When'])), field)
                self.assertTrue(variant['When'], field)

    def test_validator_mirror_rejects_unearned_partial_recovery(self):
        story = copy.deepcopy(self.story)
        self.assertFalse(validate(Model(story)))
        for group in [['trickster.now', 'kiana.trickster.returned'], ['trickster.now', 'kiana.trickster.cost.guests_robbed'], ['trickster.ever', 'kiana.trickster.returned', 'kiana.trickster.cost.guests_robbed'], ['trickster.now', 'kiana.trickster.returned', 'kiana.trickster.cost.guests_robbed', 'kiana.trickster.dog_saved']]:
            invalid = copy.deepcopy(story)
            invalid['NativeGates']['kiana.q3_recovery']['When'] = [group]
            self.assertIn('Invalid reviewed Q3 recovery gate: kiana.q3_recovery', validate(Model(invalid)))

    def test_validator_mirror_rejects_text_contract_drift(self):
        story = copy.deepcopy(self.story)
        field = next(iter(story['NativeTextEdits']))
        story['NativeTextEdits'][field]['Key'] = 'drift'
        self.assertIn('Invalid reviewed native text field: ' + field, validate(Model(story)))
if __name__ == '__main__':
    unittest.main()
