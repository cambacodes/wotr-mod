"""Counterexample histories for the struct2-08 route consumers."""
import unittest
from tests.story_fixture import fresh_story


def visible(record, flags):
    return set(record.get('Requires', ())) <= flags and not set(record.get('Forbids', ())) & flags



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

class StructureHistories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def test_claimed_submission_and_played_refusal_are_distinct(self):
        common = {'trickster.ever', 'devarra.trickster.returned',
                  'devarra.trickster.ending_claimed', 'devarra.present_now'}
        judged = self.scenes['devarra.trickster.epilogue.claimed']
        unjudged = self.scenes['devarra.trickster.epilogue.claimed_unjudged']
        self.assertFalse(visible(judged, common))
        self.assertTrue(visible(unjudged, common))
        refused = common | {'devarra.trickster.judgment_refused'}
        self.assertTrue(visible(judged, refused))
        self.assertFalse(visible(unjudged, refused))

    def test_return_then_loss_cannot_select_present_alternatives(self):
        for woman, targets in [('irabeth', {'passes'}),
                               ('galfrey', {'queen_back', 'queen_back_priestess', 'queen_back_by_you'})]:
            for suffix in ('', '_awning'):
                sid = 'terendelev.trickster.watch.' + woman + suffix
                start = self.node(sid, 'start')
                flags = {woman + '.trickster.returned', woman + '.returned_actor_lost',
                         woman + ('.dead' if woman == 'galfrey' else '_dead')}
                if woman == 'irabeth':
                    flags.add('crossroute.irabeth.available')
                for choice in start['Choices']:
                    if choice.get('Next') in targets:
                        self.assertFalse(visible(choice, flags), (sid, choice['Next']))
                self.assertTrue(any(visible(c, flags) for c in start['Choices'] if c.get('Next') == 'absent_now'))
                flags.add(woman + '.present_now')
                self.assertTrue(any(visible(c, flags) for c in start['Choices'] if c.get('Next') in targets))

    def test_minagho_nights_not_completion_select_bed_confession(self):
        key = 'yaniel.trickster.minagho_played_intimacy'
        groups = self.story['Derived'][key]
        choices = self.node('yaniel.trickster.ch5.minagho', 'ask')['Choices']
        account = 'yaniel.trickster.minagho_debt_protection'
        cases = [({'minagho_chivarro.trickster.night.minagho'}, True),
                 ({'minagho_chivarro.trickster.night.pair'}, True),
                 ({'minachiv.complete', 'minachiv.future_friends'}, False),
                 ({'minachiv.complete', 'minachiv.future_chivarro', 'minagho_chivarro.trickster.night.chivarro'}, False),
                 ({'minachiv.complete', 'minachiv.future_service'}, False)]
        for history, bed in cases:
            actual = any(set(g) <= history for g in groups)
            self.assertEqual(bed, actual, history)
            flags = history | {account} | ({key} if actual else set())
            self.assertEqual(bed, visible(by_contract(choices, [{'Next': 'truth', 'Requires': ['yaniel.trickster.minagho_played_intimacy', 'yaniel.trickster.minagho_debt_protection'], 'Forbids': [], 'Set': [], 'Abort': False}]), flags), history)
            self.assertEqual(not bed, visible(by_contract(choices, [{'Next': 'truth_close', 'Requires': ['yaniel.trickster.minagho_debt_protection'], 'Forbids': ['yaniel.trickster.minagho_played_intimacy'], 'Set': [], 'Abort': False}]), flags), history)
            self.assertTrue(visible(by_contract(choices, [{'Next': 'truth_arrangement', 'Requires': [], 'Forbids': ['yaniel.trickster.minagho_debt_protection'], 'Set': [], 'Abort': False}]), history))
        self.assertNotIn(['minachiv.room_intimacy'], groups)  # Chivarro's night.

    def test_registered_pending_matches_full_export(self):
        import json
        from pathlib import Path
        from tools import prose_pending_lint
        path = Path(__file__).resolve().parents[1] / 'tools/route_packs/plans/prose-pending.json'
        pending = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual([], prose_pending_lint.check(self.story, pending, integration=True))

    def test_hoard_check_has_distinct_played_consequences(self):
        sid = 'devarra.tower.the_hoard'
        choices = self.node(sid, 'her')['Choices']
        self.assertEqual(['honest', 'steal', 'ask', 'ask_free'], [c['Next'] for c in choices[:4]])
        check = by_contract(choices, [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': {'Skill': 'SkillAthletics', 'DC': 25, 'Success': 'climb_checked', 'Failure': 'climb_noticed'}, 'Abort': False}])['Check']
        self.assertEqual('SkillAthletics', check['Skill'])
        won = by_contract(self.node(sid, check['Success'])['Choices'], [{'Next': 'honest', 'Requires': [], 'Forbids': [], 'Set': ['devarra.tower.hoard_climb_sure'], 'Abort': False}])
        lost = by_contract(self.node(sid, check['Failure'])['Choices'], [{'Next': 'honest', 'Requires': [], 'Forbids': [], 'Set': ['devarra.tower.hoard_climb_noticed'], 'Abort': False}])
        self.assertNotEqual(won['Set'], lost['Set'])
        self.assertEqual('honest', won['Next'])
        self.assertEqual('honest', lost['Next'])
