"""Assembled commitment gating, including friendship and promise siblings."""
import unittest
from tests.story_fixture import fresh_story

class ArsinoeExclusivityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scene = next((s for s in cls.story['Scenes'] if s['Id'] == 'arsinoe_what_she_asks'))
        cls.nodes = {n['Id']: n for n in cls.scene['Nodes']}

    def menu(self, flags):
        flags = set(flags)
        groups = self.story['Derived']['arsinoe.other_romance_committed']
        if any((set(g) <= flags for g in groups)):
            flags.add('arsinoe.other_romance_committed')
        return [c['Next'] for c in self.nodes['lasting']['Choices'] if set(c['Requires']) <= flags and (not set(c['Forbids']) & flags)]

    def test_every_registered_romance_commitment_keeps_only_shared_choice(self):
        for name, rel in self.story['Relationships'].items():
            if name in {'arsinoe', 'ember', 'aivu'}:
                continue
            with self.subTest(relationship=name):
                self.assertEqual(['shared_terms'], self.menu({rel['CommittedFlag']}))

    def test_interest_friendship_and_own_commitment_leave_sole_choice_open(self):
        for flags in (set(), {'seelah.started'}, {'arsinoe.committed'}, {'ember.trusted_friend'}, {'aivu.trusted'}, {'ember.trusted_friend', 'aivu.trusted', 'arsinoe.committed'}):
            with self.subTest(flags=flags):
                self.assertEqual(['shared_terms', 'sole_terms'], self.menu(flags))

    def test_choice_position_target_and_both_promise_receipts_survive(self):
        ordered_answer_1_prior_0, ordered_answer_1, *ordered_answer_1_rest = self.nodes['lasting']['Choices']
        self.assertEqual('sole_terms', ordered_answer_1['Next'])
        for node_id in ('sole_kiss', 'sole_hold'):
            ordered_answer_2, *ordered_answer_2_rest = self.nodes[node_id]['Choices']
            flags = ordered_answer_2['Set']
            self.assertIn('arsinoe.sole_intention', flags)
            self.assertIn('arsinoe.committed', flags)
            self.assertNotIn('arsinoe.shared_terms', flags)
        for node_id in ('promise_kiss', 'promise_hold'):
            ordered_answer_3, *ordered_answer_3_rest = self.nodes[node_id]['Choices']
            flags = ordered_answer_3['Set']
            self.assertIn('arsinoe.shared_terms', flags)
            self.assertNotIn('arsinoe.sole_intention', flags)
