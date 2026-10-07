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
        personal = next(held for held, _ in walk('dream.questions', late)
                        if io.PERSONAL in held)
        for banner in [io.BANNER_HELD, io.ORDER_BANNER]:
            committed = next(held for held, _ in walk('threshold.banner', personal | {banner})
                             if io.COMMITTED in held)
            outcomes = walk('epilogue.bridge', committed)
            self.assertTrue(outcomes)
            nodes = {n['Id']: n for n in SCENES[io.E + 'epilogue.bridge']['Nodes']}
            for held, path in outcomes:
                self.assertIn('her', path)
                self.assertNotIn('gorge', path)
                text = ' '.join(rendered(nodes[n], held) for n in path)
                self.assertNotIn('the banner showed you', text)
                self.assertNotIn('dream at the gorge', text)
                self.assertIn('recognize her from Threshold', text)
            her = nodes['her']
            self.assertIn('the banner showed you', rendered(her, {io.BRIDGE_SEEN}))
            self.assertIn('dream at the gorge', rendered(her, {io.MORTAL_SEEN}))
            self.assertNotIn('dream at the gorge', rendered(her, {io.BRIDGE_SEEN, io.MORTAL_SEEN}))

    def test_banner_only_return_does_not_invent_flask_preparation(self):
        node = SCENES[io.E + 'epilogue.after']['Nodes'][0]
        flask = next(p for p in node['Paragraphs'] if 'Pharasma kept the death' in p['Text'])
        required = {io.BURIED_ALIVE, io.H2, 'trickster.lastcall.primed.bottle'}
        self.assertTrue(matches(flask, required))
        for missing in required:
            self.assertFalse(matches(flask, required - {missing}))

    def test_consumed_banners_have_one_in_person_rescue_recollection(self):
        coda = next(s for s in fresh_story()['Scenes'] if s['Id'] == 'iomedae.lastcall.page')
        node = coda['Nodes'][0]
        memory = next(p for p in node['Paragraphs'] if 'In plain steel, Iomedae recalls' in p['Text'])
        self.assertFalse(memory.get('AnyGroups'))
        receipt = set(memory['Requires'])
        for banner in [io.BANNER_HELD, io.ORDER_BANNER]:
            held = receipt | {banner, io.H2}
            account = rendered(node, held)
            self.assertNotIn('Through the banner', account)
            self.assertEqual(1, account.count('Iomedae recalls the six names'))
        for missing in memory['Requires']:
            self.assertFalse(matches(memory, receipt - {missing}))
        live = next(p for p in node['Paragraphs'] if 'Through the banner' in p['Text']
                    and 'sacrifice' not in p.get('Requires', []))
        self.assertTrue(matches(live, set(live['Requires']) | {io.BANNER_HELD}))

    def test_pair_supplier_changes_only_iomedaes_resolved_reader(self):
        from storylines import household_pair_iomedae_nocticula as pair
        for woman in pair.PAIR:
            paragraphs = pair.living_paragraphs(woman)
            expected = 2 * (len(pair.OUTCOMES) + len(pair.COSTS))
            self.assertEqual(expected + (woman == 'iomedae'), len(paragraphs))
            for paragraph in paragraphs[:expected]:
                has_new_guard = io.BURIED_ALIVE in paragraph['Forbids']
                self.assertEqual(woman == 'iomedae' and 'Through the banner' in paragraph['Text'],
                                 has_new_guard)
            if woman == 'iomedae':
                self.assertIn('In plain steel', paragraphs[-1]['Text'])
                self.assertIn(pair.P + 'resolved', paragraphs[-1]['Requires'])
                self.assertIn(pair.reader_key(woman), paragraphs[-1]['Requires'])

    def test_both_bottling_histories_keep_commander_as_bottler(self):
        from storylines import lastcall
        for sid in ['trickster.lastcall.bottle.king', 'trickster.lastcall.bottle.alone']:
            scene = next(s for s in lastcall.SCENES if s['Id'] == sid)
            text = ' '.join(n['Text'] for n in scene['Nodes'])
            self.assertIn('You press', text)
        node = next(s for s in fresh_story()['Scenes'] if s['Id'] == 'iomedae.lastcall.page')['Nodes'][0]
        account = rendered(node, {io.BURIED_ALIVE, io.H2, 'crossroute.areelu.available'})
        self.assertIn('the Commander had drained from the Wound she created', account)
        self.assertNotIn('what she had put into it', account)
        self.assertIn('not witnessed the crossing inside the seam', account)


if __name__ == '__main__':
    unittest.main()
