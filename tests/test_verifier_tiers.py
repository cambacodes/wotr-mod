"""FAST must retain every failure raised by strict verification."""
import unittest
from unittest.mock import patch
from tools import rrt_verify as verify


class VerifierTierTests(unittest.TestCase):
    def test_gate_only_defers_advisory_search_and_keeps_strict_report_sections(self):
        # A broken choice target and a producerless guard must survive tiering.
        story = {'Relationships': {'her': {'StartedFlag': 'her.started', 'ClosedFlag': 'her.closed',
                                           'CommittedFlag': 'her.committed'}},
                 'Scenes': [{'Id': 'her.test', 'Relationship': 'her', 'Owner': 'Memory',
                             'Requires': ['unearned'], 'Nodes': [{'Id': 'start', 'Text': '"Wait."',
                                 'Choices': [{'Text': '[Leave.]', 'Next': 'missing'}]}]}]}
        drafts = {'fixture': {'scenes': [{'Id': 'draft', 'Nodes': [{'Id': 'start',
                    'Choices': [{'Next': 'missing'}]}]}]}}
        with patch.object(verify, 'Reach', side_effect=AssertionError('advisory walk ran')), \
                patch.object(verify.draft_contract_lint, 'inventory', return_value=drafts):
            fast, _ = verify.run(None, verify.GAME, use_zip=False, story_obj=story, gate_only=True, quiet=True)
        self.assertTrue(fast['validate_errors'])
        self.assertIn('unearned', fast['no_producer_required'])
        self.assertTrue(fast['drafts']['contracts'])
        # Archive/return-contract parity is measured on the real export too;
        # this synthetic fixture deliberately uses use_zip=False.
        for key in ('runtime', 'typeid', 'gate_lint', 'etude_lifecycle',
                    'earned_presence', 'text_structure', 'player_text', 'intimacy_contracts',
                    'memory_callbacks', 'transaction_exits', 'timeline_contracts',
                    'remote_allocation', 'obligation_flow', 'drafts'):
            self.assertIn(key, fast, key)
        self.assertIn('advisory_analysis_skipped', fast)


if __name__ == '__main__':
    unittest.main()
