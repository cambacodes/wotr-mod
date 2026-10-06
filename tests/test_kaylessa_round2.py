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

    def choices(self, scene, node, flags):
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
        scene = 'kaylessa.wasps.last_words'
        resolved = 'native.kaylessa.message_resolved'
        # Use the actual integration reader instead of depending on its prefix.
        resolved = next(f for f in self.node(scene, 'nocame')['Choices'][0]['Requires']
                        if f.endswith('kaylessa.message_resolved'))
        flags = {resolved, 'kaylessa.message_auto_completed'}
        choices = self.choices(scene, 'nocame', flags)
        self.assertEqual(len(choices), 1)
        self.assertIn('officials closed', choices[0]['Text'])
        self.assertNotIn('kaylessa.wasps.letter_sold_told', choices[0]['Set'])
        self.assertEqual([c['Next'] for c in self.choices(scene, 'sold', flags)], ['auto'])
        sale = self.choices(scene, 'nocame', {resolved})
        self.assertEqual(len(sale), 1)
        self.assertIn('paid me', sale[0]['Text'])
        self.assertEqual(len(self.choices(scene, 'nocame', set())), 2)

    def test_gift_removes_message_keep_preserves_it(self):
        gift, keep = self.node('kaylessa.wasps.last_words', 'still')['Choices']
        item = self.story['InventoryItems']['kaylessa.note_held']
        self.assertEqual(gift['RemoveItem'], item)
        self.assertIn(item, self.story['RemovableItems'])
        self.assertIn('kaylessa.note_held', gift['Requires'])
        self.assertNotIn('RemoveItem', keep)

    def test_three_rules_histories_always_have_a_response(self):
        sid = 'kaylessa.clearing.after_the_war'
        for flags, expected in ((set(), 1), ({'kaylessa.trickster.rule_of_your_own'}, 1),
                                ({'kaylessa.trickster.rule_four'}, 2)):
            self.assertEqual(len(self.choices(sid, 'you', flags)), expected)

    def test_anemoras_words_and_death_both_reportable(self):
        sid = 'kaylessa.wasps.anemora'
        dead = {'iz.anemora_dead'}
        self.assertEqual([c['Next'] for c in self.choices(sid, 'told_her', dead)], ['dead'])
        self.assertEqual([c['Next'] for c in self.choices(sid, 'told_her', set())], ['after'])

    def test_exposure_sources_differ_without_false_ravine_memory(self):
        sid = 'kaylessa.clearing.the_next_hunter'
        sources = {'kaylessa.trickster.cost.council_knows': 'start',
                   'kaylessa.wasps.letter_sent': 'letter_source',
                   'kaylessa.wasps.claimed_as_scout': 'scout_source',
                   'kaylessa.wasps.let_them_look': 'market_source'}
        for flag, target in sources.items():
            flags = {'kaylessa.trickster.alive.swap_clean', flag}
            self.assertEqual([c['Next'] for c in self.choices(sid, 'open', flags)], [target])
        self.assertNotIn('ravine', self.node(sid, 'ask')['Text'])

    def test_tomb_custody_and_delayed_morning(self):
        sid = 'kaylessa.wasps.her_tomb'
        self.assertEqual([c['Next'] for c in self.choices(sid, 'scratch', {'kaylessa.trickster.knife_held'})], ['scratch_held'])
        self.assertEqual([c['Next'] for c in self.choices(sid, 'scratch', set())], ['scratch_own'])
        self.assertIn('returns it hilt-first', self.node(sid, 'scratch_held')['Text'])
        self.assertIn('remember the morning', self.node('kaylessa.clearing.grey_light', 'open')['Text'])

    def test_available_witnesses_and_courier_receipt(self):
        self.assertIn('participant.woljif.available', self.scenes['kaylessa.wasps.woljif']['Requires'])
        sid = 'kaylessa.wasps.watching_hands'
        self.assertEqual([c['Next'] for c in self.choices(sid, 'anevia_route', set())], ['gate_absent'])
        self.assertEqual([c['Next'] for c in self.choices(sid, 'anevia_route', {'crossroute.anevia.available'})], ['gate'])
        sid = 'kaylessa.clearing.avennara'
        self.assertEqual([c['Next'] for c in self.choices(sid, 'receipt', {'kaylessa.wasps.remembered_the_courier'})], ['courier'])

    def test_reserved_slots_keep_old_exit_and_curse(self):
        sid = 'kaylessa.clearing.where_i_was_meant_to_die'
        self.assertEqual(self.node(sid, 'cut')['Choices'][0]['Next'], 'explicit.1')
        slot = self.node(sid, 'explicit.1')
        self.assertEqual(slot['Choices'][0]['Set'], [])
        self.assertFalse(slot['Choices'][0]['Abort'])
        late = self.node('kaylessa.trickster.epilogue.commit', 'page')
        self.assertTrue(any(p.get('Id') == 'kaylessa.trickster.epilogue.commit.explicit.1'
                            for p in late['Paragraphs']))
        self.assertEqual(late['Choices'][0]['Set'], [])

    def test_complete_endings_keep_custody_and_withdraw_exposed_cover(self):
        node = self.node('kaylessa.trickster.epilogue.no_lamb', 'page')
        base = {'kaylessa.trickster.alive.swap_clean'}
        for custody in ('kaylessa.trickster.knife_held', 'kaylessa.trickster.knife_handed_back'):
            flags = base | {custody, 'kaylessa.wasps.letter_sent'}
            text = node['Text'] + '\n' + '\n'.join(
                p['Text'] for p in node['Paragraphs'] if self.selectable(p, flags)
                and all(any(f in flags for f in g) for g in p.get('AnyGroups', [])))
            self.assertNotIn('preferred not to know', text)
            self.assertIn('living witness', text)
            if custody.endswith('knife_held'):
                self.assertIn('hung by the door', text)
                self.assertNotIn('sheathed in her left boot', text)
            else:
                self.assertIn('sheathed in her left boot', text)
                self.assertNotIn('hung by the door', text)


if __name__ == '__main__':
    unittest.main()
