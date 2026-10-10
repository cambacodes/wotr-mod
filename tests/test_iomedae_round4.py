"""Round-four history/custody regressions, without new route requirements."""
import unittest
from tests.test_iomedae_round2 import SCENES, matches, walk
from tests.story_fixture import fresh_story
from storylines import iomedae_trickster as io

def rendered(node, flags):
    return ' '.join([node['Text'], *(p['Text'] for p in node.get('Paragraphs', [])
                                    if matches(p, flags))])

class IomedaeRound4Tests(unittest.TestCase):

    def test_late_courtship_walk_has_no_unearned_banner_memory(self):
        late = {io.STARTED, io.KEY_LATCH, io.CALLED, io.SPOKEN, io.SUMMIT_ASKED}
        personal = next((held for held, _ in walk('dream.questions', late) if io.PERSONAL in held))
        for banner in (io.BANNER_HELD, io.ORDER_BANNER):
            committed = next((held for held, _ in walk('threshold.banner', personal | {banner}) if io.COMMITTED in held))
            outcomes = walk('epilogue.bridge', committed)
            self.assertTrue(outcomes)
            for held, path in outcomes:
                self.assertIn('her', path)
                self.assertNotIn('gorge', path)
        her = next((n for n in SCENES[io.E + 'epilogue.bridge']['Nodes'] if n['Id'] == 'her'))
        banner_memory = next((p for p in her['Paragraphs'] if p['Requires'] == [io.BRIDGE_SEEN]))
        mortal_memory = next((p for p in her['Paragraphs'] if p['Requires'] == [io.MORTAL_SEEN]))
        self.assertFalse(matches(banner_memory, late))
        self.assertFalse(matches(mortal_memory, late))
        self.assertTrue(matches(banner_memory, {io.BRIDGE_SEEN}))
        self.assertTrue(matches(mortal_memory, {io.MORTAL_SEEN}))
        self.assertFalse(matches(mortal_memory, {io.BRIDGE_SEEN, io.MORTAL_SEEN}))

    def test_banner_only_return_does_not_invent_flask_preparation(self):
        node = SCENES[io.E + 'epilogue.after']['Nodes'][0]
        required = [io.BURIED_ALIVE, io.H2, 'trickster.lastcall.primed.bottle']
        flask = next(p for p in node['Paragraphs'] if p['Requires'] == required)
        self.assertTrue(matches(flask, set(required)))
        for missing in required:
            self.assertFalse(matches(flask, set(required) - {missing}))

    def test_consumed_banners_have_one_in_person_rescue_recollection(self):
        from storylines import household_pair_iomedae_nocticula as pair
        node = next((s for s in fresh_story()['Scenes'] if s['Id'] == 'iomedae.lastcall.page'))['Nodes'][0]
        requirements = [pair.P + 'resolved', pair.reader_key('iomedae'), 'sacrifice', 'trickster.commander_back', io.BURIED_ALIVE]
        memory = next((p for p in node['Paragraphs'] if p['Requires'] == requirements))
        self.assertFalse(memory.get('AnyGroups'))
        receipt = set(requirements)
        for banner in (io.BANNER_HELD, io.ORDER_BANNER):
            held = receipt | {banner, io.H2}
            self.assertTrue(matches(memory, held))
            live = [p for p in node['Paragraphs'] if pair.P + 'resolved' in p['Requires'] and p.get('AnyGroups')]
            self.assertTrue(live)
            self.assertFalse(any((matches(p, held) for p in live)))
        for missing in requirements:
            self.assertFalse(matches(memory, receipt - {missing}))

    def test_pair_supplier_changes_only_iomedaes_resolved_reader(self):
        from storylines import household_pair_iomedae_nocticula as pair
        flags = [pair.P + name for name, _, _ in pair.OUTCOMES] + [pair.P + 'cost.' + name for name in pair.COSTS]
        for woman in pair.PAIR:
            supplied = pair.living_paragraphs(woman)
            for outcome in flags:
                blocks = [p for p in supplied if outcome in p['Requires']]
                self.assertTrue(blocks, (woman, outcome))
                for block in blocks:
                    self.assertIn(pair.reader_key(woman), block['Requires'])
                    if outcome == pair.P + 'resolved' and woman == 'iomedae' and block.get('AnyGroups'):
                        self.assertIn(io.BURIED_ALIVE, block['Forbids'])
            if woman == 'iomedae':
                self.assertTrue(any(pair.P + 'resolved' in p['Requires'] and io.BURIED_ALIVE in p['Requires'] and not p.get('AnyGroups') for p in supplied))

if __name__ == '__main__':
    unittest.main()
