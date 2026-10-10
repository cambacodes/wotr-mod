"""Narrative provenance across Chadali's existing alternative histories."""
import json
from pathlib import Path
import unittest
from tests.test_chadali_round2 import SCENES, play, t, w, f, h

def nodes(scene_id):
    return {node['Id']: node for node in SCENES[scene_id]['Nodes']}

class ChadaliRound4Tests(unittest.TestCase):

    def test_injury_introduced_before_both_charm_replies(self):
        for history in ((), (w.W + 'her_worshippers',)):
            for choices in ({'start': 0, 'person': 1}, {'start': 1, 'ornament': 0}):
                _, _, seen, done = play(w.CHARM, choices, history)
                self.assertTrue(done)
                self.assertIn('think', seen)
                self.assertLess(seen.index('start'), seen.index('think'))

    def test_needle_correspondence_does_not_require_apology(self):
        flags, _, _, _ = play(t.P + 'fought.lucky', {'refusal': 1})
        self.assertIn(t.NEEDLE_OWED, flags)
        self.assertNotIn(t.APOLOGISED, flags)
        paragraph = next((p for p in t.ROUND2_PARAGRAPHS if t.NEEDLE_OWED in p['Requires']))
        self.assertNotIn(t.APOLOGISED, paragraph['Requires'])
        self.assertNotIn(t.APOLOGISED, paragraph['Forbids'])

    def test_honey_reservation_returns_to_an_aftermath(self):
        _, _, seen, done = play(f.NIGHT, {})
        self.assertTrue(done)
        self.assertLess(seen.index(f.NIGHT + '.explicit.1'), seen.index('cut'))
        scene = nodes(f.NIGHT)
        ordered_answer_1, *ordered_answer_1_rest = scene['cut']['Choices']
        self.assertIsNone(ordered_answer_1['Next'])
        ordered_answer_2, *ordered_answer_2_rest = scene['cut']['Choices']
        self.assertEqual([], ordered_answer_2['Set'])
        path = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/chadali/chadali.fortunes.honey.explicit.1.json'
        brief = json.loads(path.read_text(encoding='utf-8'))
        from tools.slot_brief_lint import first_beat

    def test_allocation_choices_keep_the_existing_outcomes(self):
        for choice, receipt in ((0, h.LUCK_GIVEN_BACK), (1, h.LUCK_GIVEN_BACK), (2, h.LUCK_KEPT_GIVING)):
            flags, _, _, done = play(h.NUMBER, {'zero': choice})
            self.assertTrue(done)
            self.assertIn(receipt, flags)
if __name__ == '__main__':
    unittest.main()
