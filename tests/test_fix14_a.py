"""Round-3 structure acceptance against generated gates and played flags."""
import itertools
import unittest
from unittest.mock import patch

from tests.story_fixture import fresh_story
from tests.test_kiana_partner import walk
from storylines import kiana_partner as kp, kiana_round4 as r4


def visible(block, flags):
    overrides = block.get('ForbidOverrides', {})
    return (set(block.get('Requires', ())) <= flags
            and not any(key in flags and overrides.get(key) not in flags
                        for key in block.get('Forbids', ()))
            and all(set(group) & flags for group in block.get('AnyGroups', block.get('RequiresAnyGroups', ()))))


class Fix14ATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def test_no_roof_accounts_partition_settlement_return_loss_and_grace(self):
        for nid in ('rubric2_cauldron_night', 'rubric2_cauldron_return'):
            parts = {p['Id']: p for p in self.node('arsinoe.trickster.late.commit', nid)['Paragraphs'] if p.get('Id', '').startswith('fix14.account.')}
            for called, burst, lastcall, grace in itertools.product((False, True), repeat=4):
                flags = {key for key, on in (
                    ('arsinoe.lastcall.called', called), ('arsinoe.siphon_burst', burst),
                    ('lastcall.active', lastcall), ('arsinoe.trickster.cost.rent_grace', grace)) if on}
                expected = 0 if called else 1 if burst else 2 if lastcall else 3
                self.assertEqual([i for i in range(4) if visible(parts.get('fix14.account.' + str(i)), flags)], [expected])
                self.assertEqual([i for i in (7, 8) if visible(parts.get('fix14.account.' + str(i)), flags)], [7 if grace else 8])
                for i, collateral in zip((4, 5, 6), ('collateral_still', 'collateral_word', 'lien')):
                    self.assertFalse(visible(parts.get('fix14.account.' + str(i)), flags))
                    self.assertTrue(visible(parts.get('fix14.account.' + str(i)), flags | {'arsinoe.trickster.cost.' + collateral}))

    def test_declined_cookie_ending_selects_the_played_stake(self):
        scene = self.scenes['chadali.trickster.epilogue.declined']
        base = {'trickster.ever', 'chadali.trickster.declined', 'chadali.present_now'}
        for flag, index in (('chadali.wagers.coin_lost', 0), ('chadali.wagers.luck_lost', 1)):
            flags = base | {flag}
            self.assertTrue(visible(scene, flags))
            stakes = [p for p in scene['Nodes'][0]['Paragraphs']
                      if any(f.startswith('chadali.wagers.') for f in p['Requires'])]
            self.assertEqual([p['Requires'] for p in stakes if visible(p, flags)], [[flag]])
            self.assertFalse(visible(scene, flags | {'chadali.trickster.hall_sealed'}))

    def test_recovered_earring_keeps_all_allocation_outcomes(self):
        sid = 'chadali.hours.a_lucky_number'
        self.assertIn('chadali.hours.an_unlucky_day', self.scenes[sid]['Requires'])
        zero = self.node(sid, 'zero')
        self.assertEqual([c['Next'] for c in zero['Choices']], ['back', 'half', 'keep'])
        outcomes = walk(self.scenes[sid]['Nodes'], 'zero', {'chadali.hours.an_unlucky_day', 'chadali.hours.earring_found_openly'})
        self.assertTrue(any('chadali.hours.luck_given_back' in s for s in outcomes))
        self.assertTrue(any('chadali.hours.luck_kept_giving' in s for s in outcomes))

    def test_both_keeper_endings_read_transfer_presence_and_departures(self):
        bill = 'devarra.trickster.cost.egg_withheld'
        kiln, hatched, north, present = ('nidalynn.trickster.kiln', 'nidalynn.trickster.hatched', 'nidalynn.trickster.left_with_it', 'nidalynn.present_now')
        for sid, grown_index, shell_index in (
            ('devarra.trickster.epilogue.woken', 20, 26),
            ('devarra.trickster.epilogue.commit', 17, 22),
        ):
            parts = self.node(sid, 'page')['Paragraphs']
            for hatched_flag in (True, False):
                paragraph, = [p for p in parts if p.get('Requires') ==
                              [bill, hatched, kiln, present] if hatched_flag] if hatched_flag else [p for p in parts if p.get('Requires') == [bill, kiln, present]]
                flags = {bill, kiln, present} | ({hatched} if hatched_flag else set())
                self.assertTrue(visible(paragraph, flags))
                for loss in ('nidalynn.closed', 'nidalynn.trickster.lie_kept', 'nidalynn.trickster.goat.lie_kept', 'nidalynn.trickster.given_to_the_crowd', north):
                    self.assertFalse(visible(paragraph, flags | {loss}), (sid, loss))
                self.assertFalse(visible(paragraph, flags - {present}))
                self.assertFalse(visible(paragraph, flags - {kiln}))
            variants = [p for p in parts if p.get('Id', '').startswith('fix14.keeper.')]
            for flags in ({bill}, {bill, 'nidalynn.trickster.egg_owed'}, {bill, kiln},
                          {bill, kiln, hatched, 'nidalynn.closed'},
                          {bill, kiln, hatched, 'nidalynn.closed', 'nidalynn.trickster.lie_kept'},
                          {bill, kiln, north}):
                selected, = [p for p in variants if visible(p, flags)]
                self.assertTrue(selected['Id'].startswith('fix14.keeper.'))

    def test_morning_dispatch_does_not_earn_a_commitment(self):
        sid = 'kiana.morning'
        flags = {kp.OPEN, 'trickster.ever', 'trickster.now', 'kiana.company', 'kiana.rehearsed'}
        committed = {kp.SHARE, kp.EXCLUSIVE, 'kiana.separated', 'kiana.committed'}
        for entry, pending in (('partner_share', r4.EARLY_SHARE_SENT), ('partner_answer', r4.EARLY_BREAKUP_SENT)):
            outcomes = walk(self.scenes[sid]['Nodes'], entry, flags)
            self.assertTrue(outcomes)
            for state in outcomes:
                self.assertIn(pending, state)
                self.assertFalse(committed & state)
            reply = self.scenes[sid + ('.elan_reply' if pending == r4.EARLY_SHARE_SENT else '.elan_parting')]
            self.assertIn(pending, reply['Requires'])
            self.assertEqual(reply['DelayHours'], 48)
        sent, = walk(self.scenes[sid]['Nodes'], 'partner_share', flags)
        shared = walk(self.scenes[sid + '.elan_reply']['Nodes'], 'partner_elan_terms', sent)
        self.assertTrue(any({kp.SHARE, 'kiana.committed'} <= s for s in shared))
        sent, = walk(self.scenes[sid]['Nodes'], 'partner_answer', flags)
        waiting, = walk(self.scenes[sid + '.elan_parting']['Nodes'], 'partner_breakup', sent)
        self.assertIn(r4.EARLY_DELIVERY_WAIT, waiting)
        self.assertFalse(committed & waiting)
        delivery = self.scenes[sid + '.after_delivery']
        self.assertEqual(delivery['DelayHours'], 24)
        self.assertIn(r4.EARLY_DELIVERY_WAIT, delivery['Requires'])
        settled, = walk(delivery['Nodes'], 'partner_exclusive_yes', waiting)
        self.assertTrue({kp.EXCLUSIVE, 'kiana.separated', 'kiana.committed'} <= settled)
        for followup, pending in ((self.scenes[sid + '.elan_reply'], r4.EARLY_SHARE_SENT),
                                  (delivery, r4.EARLY_DELIVERY_WAIT)):
            self.assertIn('kiana.present_now', followup['Requires'])
            self.assertIn(kp.DEAD, followup['Forbids'])
            earned = flags | {pending, 'kiana.lovers', 'seelah.souls_returned', 'kiana.present_now'}
            self.assertTrue(visible(followup, earned))
            self.assertFalse(visible(followup, earned - {'seelah.souls_returned'}))
            self.assertFalse(visible(followup, earned - {'kiana.present_now'}))
            for loss in (kp.DEAD, 'kiana.closed', 'kiana.committed'):
                self.assertFalse(visible(followup, earned | {loss}))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        paragraph = next(p for p in self.node('arsinoe.trickster.late.commit', 'rubric2_cauldron_night')['Paragraphs']
                         if p.get('Id') == 'fix14.account.0')
        with patch.dict(paragraph, Requires=[]):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_no_roof_accounts_partition_settlement_return_loss_and_grace()


if __name__ == '__main__':
    unittest.main()
