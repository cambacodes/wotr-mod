"""Round-three structure regressions, exercised after every integration pass."""
import unittest

from tests.story_fixture import fresh_story


class Fix14C(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def visible(self, surface, flags):
        return (all(k in flags for k in surface.get('Requires', []))
                and not any(k in flags for k in surface.get('Forbids', []))
                and (not surface.get('AnyGroups') or any(
                    all(k in flags for k in group) for group in surface['AnyGroups'])))

    def choices(self, node, flags):
        return [c for c in node['Choices'] if self.visible(c, flags)]

    def test_sparring_reference_does_not_need_the_goddess(self):
        sid = 'yaniel.trickster.beat.bout'
        fight = self.node(sid, 'fight')
        dirty = self.node(sid, 'dirty')
        for flags in (set(), {'iomedae.closed'}, {'iomedae.dead'}):
            self.assertIn(fight['Choices'][1], self.choices(fight, flags))
            self.assertIn(dirty['Choices'][0], self.choices(dirty, flags))
        self.assertEqual(fight['Choices'][1]['Next'], 'dirty')
        self.assertEqual(dirty['Choices'][0]['Next'], 'dirty2')
        # Removing a religious reference gate must retain the actual participant.
        scene = self.scenes[sid]
        self.assertIn('yaniel.present_now', scene['Requires'])
        self.assertIn('yaniel.killed.latched', scene['Forbids'])

    def test_beast_fed_cannot_skip_the_shown_act(self):
        sid = 'kaylessa.trickster.after.the_beast'
        receipt = 'kaylessa.trickster.beast_cruelty_shown'
        fed = self.node(sid, 'fed')
        self.assertEqual([c['Next'] for c in self.choices(fed, set())], ['fed_shown'])
        self.assertEqual([c['Next'] for c in self.choices(fed, {receipt})], ['fed_after'])
        shown = self.node(sid, 'fed_shown')['Choices'][0]
        self.assertEqual(shown['Next'], 'fed_after')
        self.assertIn(receipt, shown['Set'])
        # Both existing entry edges retain the moral cost and their save target.
        for nid in ('key', 'too_late'):
            choice = self.node(sid, nid)['Choices'][0]
            self.assertEqual(choice['Next'], 'fed')
            self.assertIn('kaylessa.trickster.cost.beast_fed', choice['Set'])
        self.assertFalse(self.scenes[sid].get('Remote', False))
        self.assertEqual(self.scenes[sid]['InteractionHub'], 'kaylessa.presence')

    def test_hunter_outcomes_must_visit_their_own_shown_node(self):
        sid = 'kaylessa.clearing.the_next_hunter'
        ask = self.node(sid, 'ask')
        self.assertEqual([c['Next'] for c in ask['Choices']], ['turned', 'hers'])
        for nid in ('turned', 'hers'):
            receipt = 'kaylessa.clearing.hunter_' + nid + '_shown'
            opposite = 'kaylessa.clearing.hunter_' + ('hers' if nid == 'turned' else 'turned') + '_shown'
            node = self.node(sid, nid)
            for flags in (set(), {opposite}):
                self.assertEqual([c['Next'] for c in self.choices(node, flags)], [nid + '_shown'])
            self.assertEqual(self.choices(node, {receipt}), [node['Choices'][0]])
            self.assertIsNone(node['Choices'][0]['Next'])
            self.assertIn(receipt, self.node(sid, nid + '_shown')['Choices'][0]['Set'])
        self.assertFalse(self.scenes[sid].get('Remote', False))

    def test_beast_history_still_selects_the_curse_paragraphs(self):
        # Independently chosen paragraph positions from the pinned authored COMMON.
        sid = 'kaylessa.trickster.epilogue.commit'
        paragraphs = self.node(sid, 'page')['Paragraphs']
        candidates = [p for p in paragraphs if {'kaylessa.trickster.cost.beast_fed',
            'kaylessa.trickster.cost.dark_fate_stalled'} <= set(p.get('Requires', []))]
        self.assertEqual(len(candidates), 1)
        paragraph = candidates[0]
        flags = set(paragraph['Requires'])
        self.assertTrue(self.visible(paragraph, flags))
        self.assertFalse(self.visible(paragraph, flags - {'kaylessa.trickster.cost.beast_fed'}))
        self.assertFalse(self.visible(paragraph, flags - {'kaylessa.trickster.cost.dark_fate_stalled'}))
