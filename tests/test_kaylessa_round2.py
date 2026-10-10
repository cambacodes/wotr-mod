"""Kaylessa history, presence and custody regressions from the round-two audit."""
import unittest
from tests.story_fixture import fresh_story
from tools import rrt_verify as rv

class KaylessaRoundTwoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    @staticmethod
    def selectable(choice, flags):
        return (all(f in flags for f in choice.get('Requires', []))
                and not any(f in flags for f in choice.get('Forbids', [])))

    def available_answers(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices'] if self.selectable(c, flags)]

    def test_paid_arrival_boundary_both_roads_and_missing_receipt(self):
        presence = self.story['Presences']['kaylessa.presence']
        primed = 'kaylessa.trickster.primed'
        for road in ('kaylessa.trickster.dead.borrow', 'kaylessa.trickster.dead.borrow_sending'):
            state = rv.SimState(5, 100)
            state.flags.update(presence['Requires'] + [road, primed])
            state.times[primed] = 100
            for elapsed in (0, 11, 12, 1000):
                state.hour = 100 + elapsed
                self.assertEqual(rv.presence_wanted(presence, state, presence['Area']), elapsed >= 12)
            state.times.pop(primed)
            self.assertFalse(rv.presence_wanted(presence, state, presence['Area']))
            state.flags.add('kaylessa.closed')
            self.assertFalse(rv.presence_wanted(presence, state, presence['Area']))

    def test_native_automatic_completion_never_accuses_a_sale(self):
        sid = 'kaylessa.wasps.last_words'
        resolved = 'native.history.kaylessa.message_resolved'
        flags = {resolved, 'kaylessa.message_auto_completed'}
        automatic = self.available_answers(sid, 'nocame', flags)
        self.assertEqual([c['Next'] for c in automatic], ['sold'])
        self.assertEqual([c['Set'] for c in automatic], [[]])
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'sold', flags)], ['auto'])
        sale = self.available_answers(sid, 'nocame', {resolved})
        self.assertEqual([c['Next'] for c in sale], ['sold'])
        self.assertEqual([c['Set'] for c in sale], [['kaylessa.wasps.letter_sold_told']])
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'nocame', set())], ['unsent', 'unsent'])

    def test_gift_removes_message_keep_preserves_it(self):
        gift, keep = self.node('kaylessa.wasps.last_words', 'still')['Choices']
        item = self.story['InventoryItems']['kaylessa.note_held']
        self.assertEqual(gift['RemoveItem'], item)
        self.assertIn(item, self.story['RemovableItems'])
        self.assertIn('kaylessa.note_held', gift['Requires'])
        self.assertNotIn('RemoveItem', keep)

    def test_three_rules_histories_always_have_a_response(self):
        sid = 'kaylessa.clearing.after_the_war'
        for flags, expected in ((set(), ['rules']), ({'kaylessa.trickster.rule_of_your_own'}, ['rules']), ({'kaylessa.trickster.rule_four'}, ['rules', 'four'])):
            self.assertEqual([c['Next'] for c in self.available_answers(sid, 'you', flags)], expected)

    def test_anemoras_words_and_death_both_reportable(self):
        sid = 'kaylessa.wasps.anemora'
        dead = {'iz.anemora_dead'}
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'told_her', dead)], ['dead'])
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'told_her', set())], ['after'])

    def test_exposure_sources_differ_without_false_ravine_memory(self):
        sid = 'kaylessa.clearing.the_next_hunter'
        sources = {'kaylessa.trickster.cost.council_knows': 'start', 'kaylessa.wasps.letter_sent': 'letter_source', 'kaylessa.wasps.claimed_as_scout': 'scout_source', 'kaylessa.wasps.let_them_look': 'market_source'}
        for flag, target in sources.items():
            flags = {'kaylessa.trickster.alive.swap_clean', flag}
            self.assertEqual([c['Next'] for c in self.available_answers(sid, 'open', flags)], [target])

    def test_tomb_custody_and_delayed_morning(self):
        sid = 'kaylessa.wasps.her_tomb'
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'scratch', {'kaylessa.trickster.knife_held'})], ['scratch_held'])
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'scratch', set())], ['scratch_own'])

    def test_available_witnesses_and_courier_receipt(self):
        self.assertIn('participant.woljif.available', self.scenes['kaylessa.wasps.woljif']['Requires'])
        sid = 'kaylessa.wasps.watching_hands'
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'anevia_route', set())], ['gate_absent'])
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'anevia_route', {'crossroute.anevia.available'})], ['gate'])
        sid = 'kaylessa.clearing.avennara'
        self.assertEqual([c['Next'] for c in self.available_answers(sid, 'receipt', {'kaylessa.wasps.remembered_the_courier', 'kaylessa.wasps.courier_in_first_letter'})], ['courier'])

    def test_reserved_slots_keep_old_exit_and_curse(self):
        sid = 'kaylessa.clearing.where_i_was_meant_to_die'
        ordered_answer_2, *_ = self.node(sid, 'cut')['Choices']
        self.assertEqual(ordered_answer_2['Next'], 'explicit.1')
        slot = self.node(sid, 'explicit.1')
        ordered_answer_3, *_ = slot['Choices']
        self.assertEqual(ordered_answer_3['Set'], [])
        ordered_answer_4, *_ = slot['Choices']
        self.assertFalse(ordered_answer_4['Abort'])
        late = self.node('kaylessa.trickster.epilogue.commit', 'page')
        self.assertTrue(any((p.get('Id') == 'kaylessa.trickster.epilogue.commit.explicit.1' for p in late['Paragraphs'])))
        ordered_answer_5, *_ = late['Choices']
        self.assertEqual(ordered_answer_5['Set'], [])

    def test_complete_endings_keep_custody_and_withdraw_exposed_cover(self):
        page = self.node('kaylessa.trickster.epilogue.no_lamb', 'page')
        held, returned = ('kaylessa.trickster.knife_held', 'kaylessa.trickster.knife_handed_back')
        for custody, other in ((held, returned), (returned, held)):
            flags = {'kaylessa.trickster.alive.swap_clean', custody, 'kaylessa.wasps.letter_sent'}
            owned = next((p for p in page['Paragraphs'] if p['Requires'] == [custody]))
            unowned = next((p for p in page['Paragraphs'] if p['Requires'] == [other]))
            self.assertTrue(self.selectable(owned, flags))
            self.assertFalse(self.selectable(unowned, flags))
            secret_cover = [p for p in page['Paragraphs'] if 'kaylessa.trickster.alive.swap_clean' in p['Requires']]
            self.assertTrue(secret_cover)
            self.assertFalse(any((self.selectable(p, flags) for p in secret_cover)))
            exposure = next((p for p in page['Paragraphs'] if p['Requires'] == ['kaylessa.wasps.letter_sent']))
            self.assertTrue(self.selectable(exposure, flags))
if __name__ == '__main__':
    unittest.main()
