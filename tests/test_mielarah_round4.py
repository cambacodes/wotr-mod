"""Crew-policy histories through both physical placements (r4 D12-D19)."""
import unittest
from storylines import mielarah_deck as deck, mielarah_trickster as route
from tests.test_mielarah_round2 import answers, nodes

class MielarahRound4Tests(unittest.TestCase):

    def test_stowaway_remembers_only_the_policy_actually_chosen(self):
        scenes = {s['Id']: s for s in deck.SCENES}
        for suffix in ('', '.arcade'):
            correction = nodes(scenes[route.D + 'correction' + suffix])
            stowaway = nodes(scenes[route.D + 'stowaway' + suffix])
            for amulets in (False, True):
                histories = [(None, {route.AMULETS} if amulets else set())]
                decision = correction['amulets' if amulets else 'box_first']
                for choice in decision['Choices']:
                    flags = {route.AMULETS} if amulets else set()
                    flags.update(choice['Set'])
                    histories.append((choice['Next'], flags))
                for policy, flags in histories:
                    with self.subTest(placement=suffix, amulets=amulets, policy=policy):
                        offered = answers(stowaway['threat'], flags)
                        expected_targets = ['vouch', 'scare', 'bet'] if policy not in ('freed', 'laughing') else ['vouch', 'bet', 'scare_' + policy]
                        self.assertEqual([a['Next'] for a in offered], expected_targets)
                        scare = [a for a in offered if a.get('Requires', []) == [] and a.get('Forbids', []) == ['mielarah.deck.crew_freed', 'mielarah.deck.crew_laughing'] and (a.get('AnyGroups', []) == []) or (a.get('Requires', []) == ['mielarah.deck.crew_freed'] and a.get('Forbids', []) == [] and (a.get('AnyGroups', []) == [])) or (a.get('Requires', []) == ['mielarah.deck.crew_laughing'] and a.get('Forbids', []) == [] and (a.get('AnyGroups', []) == []))]
                        scare_answer, = scare
                        self.assertIn(scare_answer['Next'], {'scare', 'scare_freed', 'scare_laughing'})
                        target = scare[0]['Next']
                        expected = {'freed': 'scare_freed', 'laughing': 'scare_laughing'}.get(policy, 'scare')
                        self.assertEqual(expected, target)
                        exit_choice = answers(stowaway[target], flags)
                        terminal, = exit_choice
                        self.assertIsNone(terminal['Next'])
                        self.assertIn(deck.STOWAWAY, exit_choice[0]['Set'])
                        self.assertIsNone(exit_choice[0]['Next'])

    def test_city_protection_preserves_all_market_outcomes(self):
        for scene in deck.SCENES:
            if scene['Id'].removesuffix('.arcade') != route.D + 'market':
                continue
            ns = nodes(scene)
            for choice in ns['crowd']['Choices']:
                flags = set(choice['Set'])
                current = ns[choice['Next']]
                while True:
                    offered = answers(current, flags)
                    only_answer, = offered
                    self.assertTrue(only_answer['Next'] is None or only_answer['Next'] in ns)
                    flags.update(offered[0]['Set'])
                    target = offered[0]['Next']
                    if target is None:
                        break
                    current = ns[target]
                self.assertIn(deck.MARKET, flags)
                self.assertNotIn(route.CLOSED, flags)
if __name__ == '__main__':
    unittest.main()
