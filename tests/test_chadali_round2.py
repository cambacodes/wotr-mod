"""Exact-choice route histories: a payment, contact and a yes are different acts."""
import unittest
from storylines import chadali_trickster as t
from storylines import chadali_wagers as w
from storylines import chadali_fortunes as f
from storylines import chadali_sessions as s
from storylines import chadali_hours as h
SCENES = {sc['Id']: sc for module in (t, w, f, s, h) for sc in module.SCENES}

def play(scene_id, via, flags=(), finances=1000):
    """Walk named answers, rejecting unavailable choices and unaffordable debits.

    This is a route-local choice walk, not a substitute for the production
    Rules/progression gate. Scene availability is tested by that gate.
    """
    sc = SCENES[scene_id]
    nodes = {nd['Id']: nd for nd in sc['Nodes']}
    flags = set(flags)
    seen = []
    current = sc['Nodes'][0]['Id']
    while current is not None:
        if current in seen:
            raise AssertionError('cycle: ' + current)
        seen.append(current)
        nd = nodes[current]
        flags.update(nd.get('EnterSet', []))
        available = [i for i, c in enumerate(nd['Choices']) if set(c['Requires']) <= flags and (not set(c['Forbids']) & flags) and (not c.get('Crusade') or c['Crusade']['Resource'] != 'Finances' or finances + c['Crusade']['Amount'] >= 0)]
        index = via.get(current, available[0] if available else -1)
        if index not in available:
            raise AssertionError((scene_id, current, index, available))
        choice = nd['Choices'][index]
        flags.update(choice['Set'])
        if choice.get('Crusade', {}).get('Resource') == 'Finances':
            finances += choice['Crusade']['Amount']
        if choice['Abort']:
            return (flags, finances, seen, False)
        current = choice['Next']
    flags.add(scene_id)
    return (flags, finances, seen, True)

class ChadaliRound2Tests(unittest.TestCase):

    def test_two_stakes_each_collected_by_both_refusals(self):
        for stake_index, stake in ((0, 'stake_luck'), (1, 'stake_coin')):
            base, _, _, _ = play(w.REAL_WAGER, {'bet': stake_index})
            self.assertIn(w.W + stake, base)
            other = 'stake_coin' if stake == 'stake_luck' else 'stake_luck'
            self.assertNotIn(w.W + other, base)
            for refusal in ({'start': 1}, {'start': 0, 'her_test': 1}):
                flags, _, seen, _ = play(t.P + 'council.second_cookie', refusal, base)
                self.assertIn('collect_luck' if stake_index == 0 else 'collect_coin', seen)
                self.assertIn(w.W + 'stake_collected', flags)
                self.assertNotIn(t.COMMITTED, flags)
                self.assertNotIn(w.W + 'stake_released', flags)

    def test_yes_releases_and_postponement_does_not_complete_wager(self):
        base, _, _, _ = play(w.REAL_WAGER, {'bet': 1})
        flags, _, _, _ = play(t.P + 'council.second_cookie', {'her_test': 0}, base)
        self.assertIn(t.COMMITTED, flags)
        self.assertIn(w.W + 'stake_released', flags)
        self.assertNotIn(w.W + 'stake_collected', flags)
        flags, _, _, completed = play(w.REAL_WAGER, {'bet': 2, 'people': 1})
        self.assertFalse(completed)
        self.assertNotIn(w.REAL_WAGER, flags)
        self.assertNotIn(w.BET_ON_HER, flags)

    def test_loan_transfer_is_not_the_investment_visit(self):
        for answer in (0, 1):
            flags, _, _, _ = play(f.REPAID, {'owed': answer}, (t.LUCK_OWED,))
            self.assertIn(f.LOAN_RETURNED, flags)
        flags, _, _, _ = play(f.REPAID, {}, (t.LUCK_LENT,))
        self.assertNotIn(f.LOAN_RETURNED, flags)

    def test_coin_custody_waits_for_arrival_and_preserves_old_exits(self):
        scene = SCENES[s.LAST_EVENING]
        nodes = {nd['Id']: nd for nd in scene['Nodes']}
        self.assertIn('chadali.wagers.coin_lost', scene['Forbids'])
        for nid in ('start', 'keep', 'walk', 'together'):
            self.assertTrue(all((s.COIN_TAKEN not in answer['Set'] for answer in nodes[nid]['Choices'])))
        for choice in (0, 1):
            flags, _, seen, done = play(s.LAST_EVENING, {'carry': choice})
            self.assertTrue(done)
            self.assertIn(s.COIN_TAKEN, flags)
            self.assertIn('together_home' if choice == 0 else 'walk_home', seen)
        for nid in ('walk', 'together'):
            ordered_answer_1, *ordered_answer_1_rest = nodes[nid]['Choices']
            self.assertIsNone(ordered_answer_1['Next'])
            ordered_answer_2, *ordered_answer_2_rest = nodes[nid]['Choices']
            self.assertEqual([], ordered_answer_2['Set'])

    def test_market_contact_flour_and_courtship_are_separate(self):
        self.assertIn('trickster.now', t.PRESENCES[t.MARKET]['Requires'])
        self.assertIn('chadali.present_now', t.PRESENCES[t.MARKET]['Requires'])
        for name in ('after.market_wager', 'after.market_wager_visit'):
            self.assertIn('trickster.now', SCENES[t.P + name]['Requires'])
            self.assertIn('chadali.present_now', SCENES[t.P + name]['Requires'])
        self.assertIn('chadali.present_now', SCENES[t.P + 'epilogue.company']['Requires'])
        self.assertIn('chadali.reachable_by_letter', SCENES[t.P + 'react.ember_penny']['Requires'])
        flags, money, _, _ = play(t.P + 'after.market_wager', {'start': 1})
        self.assertEqual(1000, money)
        self.assertNotIn(t.RETURN_READY, flags)
        flags, money, _, _ = play(t.P + 'after.market_wager', {'carried': 1})
        self.assertEqual(950, money)
        self.assertNotIn(t.RETURN_READY, flags)
        flags, money, seen, _ = play(t.P + 'after.market_wager', {'carried': 0})
        self.assertEqual(950, money)
        self.assertIn('invite', seen)
        self.assertIn(t.RETURN_READY, flags)
        self.assertIn(t.LATE_INTENT, flags)
        for sc in (t.P + 'after.market_wager', t.P + 'after.market_wager_visit'):
            flags, _, _, completed = play(sc, {}, finances=0)
            self.assertTrue(completed)
            self.assertNotIn(t.RETURN_READY, flags)

    def test_donated_post_is_not_an_accepted_invitation(self):
        flags, money, seen, _ = play(t.P + 'council.late_wager', {'reply': 1})
        self.assertEqual(900, money)
        self.assertIn(t.P + 'post_sent', flags)
        self.assertNotIn(t.LATE_INTENT, flags)
        self.assertNotIn('personal_reply', seen)
        flags, _, seen, _ = play(t.P + 'council.late_wager', {'reply': 0})
        self.assertIn('personal_reply', seen)
        self.assertIn(t.LATE_INTENT, flags)
        flags, money, _, completed = play(t.P + 'council.late_wager', {'start': 1})
        self.assertFalse(completed)
        self.assertEqual(1000, money)
        self.assertNotIn(t.P + 'post_sent', flags)

    def test_three_signatures_names_and_refusal_cost(self):
        for index in range(3):
            flags, _, _, _ = play(s.BETTING_LIVES, {'start': index})
            self.assertIn(s.S + 'feint_signed', flags)
            self.assertIn(s.S + 'names_recounted', flags)
            self.assertNotIn(s.S + 'feint_refused', flags)
        flags, _, _, _ = play(s.BETTING_LIVES, {'command': 1})
        self.assertNotIn(s.S + 'names_recounted', flags)
        flags, money, _, _ = play(s.BETTING_LIVES, {'start': 3})
        self.assertEqual(900, money)
        self.assertIn(s.S + 'feint_refused', flags)
        self.assertNotIn(s.S + 'feint_signed', flags)
        flags, _, _, completed = play(s.BETTING_LIVES, {'start': 4}, finances=0)
        self.assertFalse(completed)

    def test_scar_and_reporter_provenance(self):
        _, _, ordinary, _ = play(h.SCAR, {})
        flags, _, scar, _ = play(h.SCAR, {'start': 1})
        self.assertNotIn('heal_scar', ordinary)
        self.assertIn('heal_scar', scar)
        self.assertIn('close_scar', scar)
        self.assertIn(h.SCAR_KEPT, flags)
        for source in (s.SAID_BABBLING, s.SAID_CRAZY):
            for answer in range(3):
                flags, _, seen, _ = play(s.OVERHEARD, {'question': answer}, (source,))
                written = source == s.SAID_BABBLING
                self.assertEqual(written, s.S + 'notebook_returned' in flags)
                self.assertEqual(not written, s.S + 'oral_reply' in flags)
                self.assertEqual(written, 'close' in seen)

    def test_slots_and_legacy_ending_exits(self):
        for scene_id in (f.NIGHT, s.WISH, t.P + 'epilogue.commit'):
            sc = SCENES[scene_id]
            slot = next((nd for nd in sc['Nodes'] if nd['Id'] == scene_id + '.explicit.1'))
            ordered_answer_3, *ordered_answer_3_rest = slot['Choices']
            self.assertFalse(ordered_answer_3['Set'])
        ending = SCENES[t.P + 'epilogue.commit']
        page = ending['Nodes'][0]
        ordered_answer_4, *ordered_answer_4_rest = page['Choices']
        self.assertIn(t.P + 'late_invited', ordered_answer_4['Requires'])
        *answer_in_order_1_preceding, answer_in_order_1 = page['Choices']
        self.assertEqual('friend', answer_in_order_1['Next'])
        for node_id in ('stay', 'half', 'coin', 'penny'):
            nd = next((nd for nd in ending['Nodes'] if nd['Id'] == node_id))
            ordered_answer_5, *ordered_answer_5_rest = nd['Choices']
            self.assertIsNone(ordered_answer_5['Next'])
            ordered_answer_6, *ordered_answer_6_rest = nd['Choices']
            self.assertFalse(ordered_answer_6['Set'])

    def test_extraction_letter_preserves_coin_custody_and_forfeiture(self):
        for history, expected, absent in (((), 'hurt', 'coin'), ((t.PRIMED,), 'coin', 'coin_home'), ((t.PRIMED, t.WAGERED), 'coin', 'coin_home'), ((t.PRIMED, 'chadali.wagers.coin_lost'), 'coin_collected', 'coin'), ((t.PRIMED, s.COIN_TAKEN), 'coin_home', 'coin')):
            flags, _, seen, completed = play(t.P + 'fought.lucky', {'refusal': 1}, history)
            self.assertTrue(completed)
            self.assertIn(expected, seen)
            self.assertNotIn(absent, seen)
            self.assertIn(t.NEEDLE_OWED, flags)
            self.assertEqual(s.COIN_TAKEN in history, s.COIN_TAKEN in flags)
            self.assertNotIn('chadali.lastcall.luck_returned', flags)

    def test_epilogue_slot_brief_uses_past_tense(self):
        import json
        from pathlib import Path
        path = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/chadali/chadali.trickster.epilogue.commit.explicit.1.json'
        self.assertEqual('third-past', json.loads(path.read_text(encoding='utf-8'))['narration'])
if __name__ == '__main__':
    unittest.main()
