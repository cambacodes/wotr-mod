"""Saved outcomes and history-sensitive readers for rubric round 2.

The Last Call regressions intentionally remain red until its shared owner lands
LC-HISTORY-01. These structural tests do not award prose/voice acceptance.
"""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools.prose_pending_lint import check as pending_check
from tools.rrt_verify import Model, SimState, sim_complete

ROOT = Path(__file__).resolve().parents[1]
D = 'dorgelinda.trickster.'
L = 'dorgelinda.ledger.'
E = 'elyanka.trickster.'


def enabled(item, flags):
    return (set(item.get('Requires', ())) <= flags
            and not set(item.get('Forbids', ())) & flags
            and all(set(group) & flags for key in ('AnyGroups', 'RequiresAnyGroups')
                    for group in item.get(key, ())))



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class Structure3DTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}
        cls.model = Model(cls.story)

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def flags(self, *history):
        state = SimState(6, 1000)
        state.flags.update(('trickster.ever', 'trickster', 'chapter_later',
                            'lastcall.commander_returned', *history))
        sim_complete(self.model, state)
        return state.flags

    def test_pending_surfaces_if_present_are_exactly_registered(self):
        data = json.loads((ROOT / 'tools/route_packs/plans/prose-pending.json').read_text(encoding='utf-8'))
        self.assertEqual([], pending_check(self.story, data, integration=True))

    def test_elyanka_choices_keep_distinct_terminal_outcomes_and_readers(self):
        sid = E + 'beat.master'
        self.assertEqual(['kill', 'escort', 'hers'],
                         [c['Next'] for c in self.node(sid, 'choice')['Choices']])
        self.assertEqual('kill2', by_contract(self.node(sid, 'kill')['Choices'], [{'Next': 'kill2', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])
        outcomes = {'kill2': E + 'master.killed', 'escort': E + 'master.escorted',
                    'hers': E + 'master.hers'}
        for nid, flag in outcomes.items():
            with self.subTest(nid=nid):
                choice = by_contract(self.node(sid, nid)['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['elyanka.trickster.master.killed'], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['elyanka.trickster.master.escorted'], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['elyanka.trickster.master.hers'], 'Check': None, 'Abort': False, 'Crusade': None}])
                self.assertIsNone(choice['Next'])
                self.assertEqual([flag], choice['Set'])
                paras = self.node(E + 'epilogue.claim', 'page')['Paragraphs']
                readers = [p for p in paras if flag in p.get('Requires', ())]
                self.assertTrue(readers)
                for other in outcomes.values():
                    self.assertEqual(flag == other,
                                     any(enabled(p, self.flags(other)) for p in readers))

    def test_chadali_cut_preserves_intimacy_receipt_and_aftermath(self):
        sid = 'chadali.fortunes.honey'
        approach = by_contract(self.node(sid, 'look')['Choices'], [{'Next': 'chadali.fortunes.honey.explicit.1', 'Requires': [], 'Forbids': [], 'Set': ['chadali.fortunes.night'], 'Check': None, 'Abort': False, 'Crusade': None}])
        self.assertEqual(sid + '.explicit.1', approach['Next'])
        self.assertEqual(['chadali.fortunes.night'], approach['Set'])
        self.assertEqual('cut', by_contract(self.node(sid, sid + '.explicit.1')['Choices'], [{'Next': 'cut', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])
        self.assertIsNone(by_contract(self.node(sid, 'cut')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])

    def test_chadali_sibling_reservation_keeps_existing_exit(self):
        sid = 'chadali.sessions.what_chance_wishes'
        self.assertEqual(sid + '.explicit.1', by_contract(self.node(sid, 'stay')['Choices'], [{'Next': 'chadali.sessions.what_chance_wishes.explicit.1', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])
        self.assertIsNone(by_contract(self.node(sid, sid + '.explicit.1')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])

    def test_second_ask_retains_paid_settlement_and_acceptance(self):
        sid = D + 'after.second_ask'
        price = by_contract(self.node(sid, 'price')['Choices'], [{'Next': 'told', 'Requires': [], 'Forbids': [], 'Set': ['dorgelinda.trickster.cost.told_all'], 'Check': None, 'Abort': False, 'Crusade': {'Resource': 'Materials', 'Amount': -100}}])
        self.assertEqual('told', price['Next'])
        self.assertEqual([D + 'cost.told_all'], price['Set'])
        self.assertEqual({'Resource': 'Materials', 'Amount': -100}, price['Crusade'])
        self.assertEqual('accepted', by_contract(self.node(sid, 'told')['Choices'], [{'Next': 'accepted', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])['Next'])
        self.assertEqual(['dorgelinda.committed', D + 'cost.told_all'],
                         by_contract(self.node(sid, 'accepted')['Choices'], [{'Next': None, 'Requires': ['trickster.now'], 'Forbids': [], 'Set': ['dorgelinda.committed', 'dorgelinda.trickster.cost.told_all'], 'Check': None, 'Abort': False, 'Crusade': None}])['Set'])

    def test_ordinary_settlement_readers_are_mutually_exclusive(self):
        paras = self.node(D + 'epilogue.committed', 'page')['Paragraphs']
        settled = [p for p in paras if D + 'cost.told_all' in p.get('Requires', ())]
        unsettled = [p for p in paras if D + 'cost.told_all' in p.get('Forbids', ())]
        self.assertTrue(settled)
        self.assertTrue(unsettled)
        for history, want_settled in (((), False), ((D + 'cost.told_all',), True)):
            flags = self.flags(*history)
            self.assertEqual(want_settled, any(enabled(p, flags) for p in settled))
            self.assertEqual(not want_settled, any(enabled(p, flags) for p in unsettled))

    def test_lastcall_settlement_variants_cover_both_histories(self):
        paras = self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
        flags = self.flags('dorgelinda.committed', D + 'declined',
                           D + 'cost.carts_signed', D + 'cost.told_all')
        settled = [p for p in paras if D + 'cost.told_all' in p.get('Requires', ())]
        unsettled = [p for p in paras if D + 'cost.told_all' in p.get('Forbids', ())]
        self.assertTrue(any(enabled(p, flags) for p in settled), 'LC-HISTORY-01: settled Last Call variant missing')
        self.assertFalse(any(enabled(p, flags) for p in unsettled))
        flags = self.flags('dorgelinda.committed', D + 'cost.carts_signed')
        self.assertTrue(any(enabled(p, flags) for p in unsettled), 'unsettled Last Call variant missing')
        self.assertFalse(any(enabled(p, flags) for p in settled))

    def test_lastcall_called_disclosure_does_not_replay_a_completed_disclosure(self):
        paras = self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
        flags = self.flags('dorgelinda.lastcall.called', D + 'cost.told_all')
        self.assertFalse(enabled(by_contract(paras, [{'Requires': ['dorgelinda.lastcall.called'], 'Forbids': ['dorgelinda.trickster.cost.told_all', 'dorgelinda.lastcall.account_settled'], 'AnyGroups': []}]), flags),
                         'LC-HISTORY-01: called paragraph replays completed disclosure')
        variants = [p for p in paras if {'dorgelinda.lastcall.called', D + 'cost.told_all'}
                    <= set(p.get('Requires', ()))]
        self.assertTrue(any(enabled(p, flags) for p in variants))

    def test_current_quarrel_fact_tracks_repair_rather_than_historical_cold(self):
        for history, cold in (((L + 'quarrel_cold',), True),
                              ((L + 'quarrel_cold', L + 'quarrel_mended'), False)):
            with self.subTest(history=history):
                self.assertEqual(cold, L + 'cold_unmended' in self.flags(*history))

    def test_lastcall_hostile_audit_respects_current_seal_quarrel(self):
        paras = self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
        hostile = [p for p in paras if D + 'cost.audit_hostile' in p.get('Requires', ())]
        self.assertTrue(hostile)
        histories = [((), True), ((L + 'quarrel_cold',), False),
                     ((L + 'quarrel_unmended',), False),
                     ((L + 'quarrel_cold', L + 'quarrel_mended'), True)]
        for history, want_supper in histories:
            with self.subTest(history=history):
                flags = self.flags('dorgelinda.committed', D + 'cost.audit_hostile', D + 'cost.twice_weekly', *history)
                # Existing supper paragraph index 2 retains its identity.
                self.assertEqual(want_supper, enabled(by_contract(paras, [{'Requires': ['dorgelinda.trickster.cost.audit_hostile', 'dorgelinda.trickster.cost.twice_weekly'], 'Forbids': ['dorgelinda.ledger.cold_unmended', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.lastcall.account_settled'], 'AnyGroups': []}]), flags),
                                 'LC-HISTORY-01: private supper contradicts current seal history')


if __name__ == '__main__':
    unittest.main()
