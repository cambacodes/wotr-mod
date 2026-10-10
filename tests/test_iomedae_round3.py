"""History regressions for the round-three Iomedae findings."""
import json
from pathlib import Path
import unittest
from tests.test_iomedae_round2 import SCENES, matches, walk
from storylines import iomedae_trickster as io

class IomedaeRound3Tests(unittest.TestCase):

    def test_first_white_dream_after_late_opening(self):
        for choice in SCENES[io.E + 'dream.questions']['Nodes'][0]['Choices']:
            self.assertNotIn('RequiresAnyGroups', choice)
        late = {io.STARTED, io.KEY_LATCH, io.CALLED, io.SPOKEN,
                io.SUMMIT_ASKED, io.E + 'iz.night'}
        paths = [path for _, path in walk('dream.questions', late)]
        self.assertTrue(paths)
        self.assertTrue(all('first_white' in path and 'returning_white' not in path
                            for path in paths))
        for history in [(io.E + 'dream.summit',), (io.HERALD_DREAM,),
                        (io.E + 'dream.summit', io.HERALD_DREAM)]:
            paths = [path for _, path in walk('dream.questions', late | set(history))]
            self.assertTrue(all('returning_white' in path and 'first_white' not in path
                                for path in paths))

    def test_dreams_recount_history_without_a_live_guest(self):
        from tests.story_fixture import fresh_story
        generated = {s['Id']: s for s in fresh_story()['Scenes']}
        for name in ['dream.summit', 'dream.eve']:
            scene = generated[io.E + name]
            self.assertNotIn('crossroute.nocticula.unavailable', scene['Forbids'])
        initial = {'trickster.ever', io.STARTED, io.KEY_LATCH, io.BANNER_HELD,
                   'iomedae.reachable_by_letter', 'noct.closed', 'noct.dead'}
        self.assertTrue(matches(generated[io.E + 'dream.eve'], initial))

    def test_banner_witnesses_do_not_earn_or_block_the_return(self):
        for guests, wanted in [(set(), set()),
                               ({'crossroute.nocticula.available'}, {'nocticula_objection'}),
                               ({'crossroute.areelu.available'}, {'areelu_objection'}),
                               ({'crossroute.nocticula.available', 'crossroute.areelu.available'},
                                {'nocticula_objection', 'areelu_objection'})]:
            with self.subTest(guests=guests):
                outcomes = walk('threshold.banner', {io.BANNER_HELD, 'noct.closed', *guests})
                carried = [(held, path) for held, path in outcomes if io.CARRIED in held]
                self.assertTrue(carried)
                self.assertTrue(all(wanted <= set(path) for _, path in carried))
                self.assertTrue(all(not ({'nocticula_objection', 'areelu_objection'} - wanted)
                                    & set(path) for _, path in carried))
                self.assertTrue(any(io.RESCUE_ONLY in held for held, _ in carried))
                self.assertFalse(any(io.COMMITTED in held for held, _ in carried))
                romantic = walk('threshold.banner', {io.BANNER_HELD, io.PERSONAL, *guests})
                self.assertTrue(any(io.COMMITTED in held for held, _ in romantic))

    def test_flask_account_reads_current_contents(self):
        node = SCENES[io.E + 'epilogue.after']['Nodes'][0]
        predicates = [
            (['lastcall.h1', 'lastcall.bottled_held', io.CARRIED], [io.BURIED_ALIVE]),
            (['lastcall.bottled_held'], [io.BURIED_ALIVE, io.CARRIED]),
            ([io.BURIED_ALIVE, io.H2, 'trickster.lastcall.primed.bottle'], []),
        ]
        histories = [
            {'lastcall.active', 'lastcall.h1', io.CARRIED, 'lastcall.bottled_held'},
            {'lastcall.active', io.H2, 'lastcall.dead_on_record', 'lastcall.bottled_held'},
            {'lastcall.active', io.H2, io.BURIED_ALIVE, io.CARRIED, 'trickster.lastcall.primed.bottle'},
        ]
        for requirements, exclusions in predicates:
            block = next(p for p in node['Paragraphs'] if p['Requires'] == requirements and p['Forbids'] == exclusions)
            self.assertTrue(matches(block, set(requirements)))
            for missing in requirements:
                self.assertFalse(matches(block, set(requirements) - {missing}))
            for forbidden in exclusions:
                self.assertFalse(matches(block, set(requirements) | {forbidden}))
        for flags, wanted in zip(histories, predicates):
            selected = {(tuple(p['Requires']), tuple(p['Forbids'])) for p in node['Paragraphs'] if matches(p, flags)}
            self.assertIn((tuple(wanted[0]), tuple(wanted[1])), selected)
            for other in predicates:
                if other != wanted:
                    self.assertNotIn((tuple(other[0]), tuple(other[1])), selected)

    def test_epilogue_briefs_use_third_past_and_preserve_exits(self):
        folder = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/iomedae'
        expected = {'iomedae.trickster.epilogue.after.explicit.1': 'third-past', 'iomedae.trickster.epilogue.platform.explicit.1': 'second-present'}
        for path in folder.glob('*.json'):
            self.assertEqual(expected[path.stem], json.loads(path.read_text(encoding='utf-8'))['narration'])
        page = SCENES[io.E + 'epilogue.after']['Nodes'][0]
        ordered_answer_1, *_ = page['Choices']
        legacy = ordered_answer_1
        self.assertEqual('continue', legacy['Id'])
        self.assertFalse(legacy['Next'])
        self.assertFalse(legacy['Set'])
        slot = next((n for n in SCENES[io.E + 'epilogue.after']['Nodes'] if n['Id'] == io.E + 'epilogue.after.explicit.1'))
        ordered_answer_2, *_ = slot['Choices']
        self.assertEqual('vigil_morning', ordered_answer_2['Next'])

    def test_generated_coda_keeps_banner_and_crossing_separate(self):
        from tests.story_fixture import fresh_story
        node = next((s for s in fresh_story()['Scenes'] if s['Id'] == 'iomedae.lastcall.page'))['Nodes'][0]
        self.assertEqual([c['Set'] for c in node['Choices']], [[]])
        self.assertEqual([c['Next'] for c in node['Choices']], [None])
        crossing = next((p for p in node['Paragraphs'] if p['Requires'] == [io.BURIED_ALIVE, io.H2]))
        self.assertTrue(matches(crossing, {io.H2, io.BURIED_ALIVE, io.CARRIED}))
        self.assertNotIn('crossroute.areelu.available', crossing['Requires'])
        witness = next((p for p in node['Paragraphs'] if p['Requires'] == [io.BURIED_ALIVE, io.H2, 'crossroute.areelu.available']))
        self.assertFalse(matches(witness, {io.H2, io.BURIED_ALIVE, io.CARRIED}))
        self.assertTrue(matches(witness, {io.H2, io.BURIED_ALIVE, io.CARRIED, 'crossroute.areelu.available'}))
        no_banner = next((p for p in node['Paragraphs'] if p['Forbids'] == [io.CARRIED]))
        self.assertTrue(matches(no_banner, {io.H2, 'lastcall.bottled_held'}))
        self.assertFalse(matches(no_banner, {io.H2, io.CARRIED, 'lastcall.bottled_held'}))

    def test_generated_banner_and_shared_heroic_partition(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        scenes = {s['Id']: s for s in story['Scenes']}
        plant = scenes[io.E + 'threshold.banner']['Nodes'][0]
        for choice in plant['Choices'][:2]:
            self.assertNotIn('crossroute.nocticula.unavailable', choice['Forbids'])
        heroic = scenes['trickster.lastcall.page.heroic']['Nodes'][0]
        for gate in ('lastcall.public_return', 'lastcall.bottled_held', 'lastcall.bridge_return'):
            self.assertTrue(any((gate in p['Requires'] for p in heroic['Paragraphs'])))
        for gate in ('lastcall.public_return', 'lastcall.bottled_held'):
            self.assertIn(io.BURIED_ALIVE, story['DerivedForbids'][gate])
        self.assertEqual([['lastcall.active', io.BURIED_ALIVE]], story['Derived']['lastcall.bridge_return'])
if __name__ == '__main__':
    unittest.main()
