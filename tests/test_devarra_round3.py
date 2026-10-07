"""Route-local history dispatch and legacy exit checks, without fabricated yes."""
from copy import deepcopy
import unittest

from storylines import devarra_trickster as spine, devarra_tower as tower
from storylines import devarra_round3 as r3
from test_devarra_round2 import visible


class DevarraRoundThreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': deepcopy(spine.SCENES + tower.SCENES)}
        tower.integrate(payload)
        cls.scenes = {s['Id']: s for s in payload['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_late_page_requires_actual_yes_and_keeps_inert_legacy_exit(self):
        page = self.scenes[r3.P + 'epilogue.commit']
        pending = {'trickster.ever', spine.TESTED, spine.RETURNED}
        self.assertFalse(visible(page, pending))
        self.assertTrue({r3.LATE_YES, spine.COMMITTED} <= set(page['Requires']))
        exit = page['Nodes'][0]['Choices'][0]
        self.assertEqual(exit['Set'], [])
        self.assertIsNone(exit['Next'])
        self.assertNotIn('Crusade', exit)

    def test_conqueror_cannot_skip_her_verdict(self):
        verdict = self.node(r3.P + 'after.lair', 'verdict')
        choices = [c for c in verdict['Choices'] if visible(c, {r3.CLAIMED})]
        self.assertEqual([c['Next'] for c in choices], ['claimed'])
        for name in ('after.late_proposal', 'epilogue.commit', 'epilogue.pending'):
            scene = self.scenes[r3.P + name]
            self.assertIn(r3.CLAIMED, scene['Forbids'])
            self.assertEqual(scene['ForbidOverrides'][r3.CLAIMED], r3.ANSWERED)
        for scene in self.scenes.values():
            if scene['Id'].startswith(r3.T):
                self.assertIn(r3.REFUSED, scene['Forbids'])
                self.assertEqual(scene['ForbidOverrides'][r3.REFUSED], r3.ANSWERED)

    def test_prior_entries_select_one_public_wager(self):
        choices = self.node(r3.T + 'the_garrison_book', 'start')['Choices']
        for flags, expected in ((set(), 'on_her'), ({tower.VAULT_OPENED}, 'on_her_vault'),
                                ({spine.COOK_GIVEN}, 'on_her_cook'),
                                ({tower.VAULT_OPENED, spine.COOK_GIVEN}, 'on_her_vault')):
            options = [c['Next'] for c in choices if visible(c, flags) and c['Next'].startswith('on_her')]
            self.assertEqual(options, [expected])

    def test_voluntary_battle_keeps_old_mechanics_without_buying_story(self):
        ask = self.node(r3.T + 'the_generals', 'ask')['Choices'][0]
        bargain = self.node(r3.T + 'the_generals', 'bargain')['Choices'][0]
        self.assertIn(tower.ONE_BATTLE, ask['Set'])
        self.assertIn(tower.ONE_BATTLE, bargain['Set'])
        self.assertIn(r3.VOLUNTARY, ask['Set'])
        self.assertNotIn(r3.PURCHASED, ask['Set'])
        paragraphs = self.node(r3.P + 'epilogue.woken', 'page')['Paragraphs']
        voluntary = '\n'.join(p['Text'] for p in paragraphs if visible(p, set(ask['Set'])))
        self.assertNotIn('every death in it', voluntary)
        purchased = '\n'.join(p['Text'] for p in paragraphs if visible(p, set(bargain['Set'])))
        self.assertIn('every death in it', purchased)


if __name__ == '__main__':
    unittest.main()
