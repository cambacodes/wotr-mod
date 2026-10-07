"""Narrative provenance across Chadali's existing alternative histories."""
import json
from pathlib import Path
import unittest

from test_chadali_round2 import SCENES, play, t, w, f, h


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

    def test_forfeited_coin_stays_with_her_through_both_returns(self):
        # A coin stake is collected by her refusal; tree commitment can follow.
        flags, _, _, _ = play(w.REAL_WAGER, {'bet': 1})
        flags, _, _, _ = play(t.P + 'council.second_cookie', {'her_test': 1}, flags)
        self.assertIn(w.W + 'stake_collected', flags)
        self.assertIn(w.W + 'stake_coin', flags)
        # The production derived rule maps those exact receipts to coin_lost.
        self.assertEqual([[w.W + 'stake_coin', w.W + 'stake_collected']],
                         t.DERIVED[w.W + 'coin_lost'])
        flags |= {w.W + 'coin_lost', t.PRIMED}
        flags, _, _, _ = play(t.P + 'after.orange_tree', {}, flags)
        self.assertIn(t.COMMITTED, flags)
        flags.add('council.fought')
        for return_choice in (0, 1):
            returned, _, seen, done = play(t.P + 'fought.lucky', {'refusal': return_choice}, flags)
            self.assertTrue(done)
            self.assertIn(t.RETURNED, returned)
            self.assertIn('coin_collected', seen)
            self.assertNotIn('coin', seen)
            self.assertNotIn('coin_home', seen)
            letter = nodes(t.P + 'fought.lucky')['coin_collected']['Text']
            self.assertIn('no coin in the envelope', letter)
            self.assertIn('flat in my basket', letter)
            # Both consumers remain truthful without a new custody flag.
            from storylines import lastcall_partners
            coda = next(
                scene for _, scene in lastcall_partners.pages() if scene['Id'] == 'chadali.lastcall.page')
            for paragraphs in (t.ROUND2_PARAGRAPHS, coda['Nodes'][0]['Paragraphs']):
                coin = [p for p in paragraphs
                        if w.W + 'coin_lost' in p.get('Requires', [])]
                self.assertTrue(coin)
                self.assertTrue(all('basket' in p['Text'] for p in coin))

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
