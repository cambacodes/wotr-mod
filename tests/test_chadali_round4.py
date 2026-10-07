"""Narrative provenance across Chadali's existing alternative histories."""
import json
from pathlib import Path
import unittest

from tests.test_chadali_round2 import SCENES, play, t, w, f, h


def nodes(scene_id):
    return {node['Id']: node for node in SCENES[scene_id]['Nodes']}


class ChadaliRound4Tests(unittest.TestCase):
    def test_injury_introduced_before_both_charm_replies(self):
        scene = nodes(w.CHARM)
        for history in ((), (w.W + 'her_worshippers',)):
            for choices in ({'start': 0, 'person': 1}, {'start': 1, 'ornament': 0}):
                _, _, seen, done = play(w.CHARM, choices, history)
                self.assertTrue(done)
                self.assertIn('think', seen)
                injury = [nid for nid in seen if 'crushed hand' in scene[nid]['Text']]
                self.assertEqual(['start'], injury)
                self.assertLess(seen.index(injury[0]), seen.index('think'))
        self.assertNotIn("crossbowman", scene['person']['Text'])

    def test_needle_correspondence_does_not_require_apology(self):
        flags, _, _, _ = play(t.P + 'fought.lucky', {'refusal': 1})
        self.assertIn(t.NEEDLE_OWED, flags)
        self.assertNotIn(t.APOLOGISED, flags)
        paragraph = next(p for p in t.ROUND2_PARAGRAPHS if t.NEEDLE_OWED in p['Requires'])
        self.assertIn('correspondence', paragraph['Text'])
        self.assertNotIn('apology', paragraph['Text'])

    def test_honey_reservation_returns_to_an_aftermath(self):
        _, _, seen, done = play(f.NIGHT, {})
        self.assertTrue(done)
        self.assertLess(seen.index(f.NIGHT + '.explicit.1'), seen.index('cut'))
        scene = nodes(f.NIGHT)
        self.assertIn('pulls the loosened silk away', scene[f.NIGHT + '.explicit.1']['Text'])
        self.assertIn('silk still beside your armour', scene['cut']['Text'])
        self.assertIsNone(scene['cut']['Choices'][0]['Next'])
        self.assertEqual([], scene['cut']['Choices'][0]['Set'])
        path = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/chadali/chadali.fortunes.honey.explicit.1.json'
        brief = json.loads(path.read_text(encoding='utf-8'))
        from tools.slot_brief_lint import first_beat
        self.assertEqual(first_beat(scene['cut'], brief['speakers']), brief['last_line'])

    def test_allocation_choices_keep_the_existing_outcomes(self):
        for choice, receipt in ((0, h.LUCK_GIVEN_BACK), (1, h.LUCK_GIVEN_BACK), (2, h.LUCK_KEPT_GIVING)):
            flags, _, _, done = play(h.NUMBER, {'zero': choice})
            self.assertTrue(done)
            self.assertIn(receipt, flags)


if __name__ == '__main__':
    unittest.main()
