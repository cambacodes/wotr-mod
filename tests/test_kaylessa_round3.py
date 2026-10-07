"""Regression histories for the eleven round-three Kaylessa findings."""
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as rv


class KaylessaRoundThreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rv.Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_each_native_attack_blocks_every_road_even_with_legacy_return(self):
        bindings = {
            'kaylessa.attack_kenabres_masked': 'ac4468a7eded7fd43946f1a730791ff0',
            'kaylessa.attack_kenabres_drow': '53a2540656646e44e92e3d9b30b35179',
            'kaylessa.attack_camp': '0673b59a2f25dbf459a4dfe1dfa09c7a',
        }
        closure = 'kaylessa.early_player_killed'
        rel = self.story['Relationships']['kaylessa']
        self.assertIn(closure, rel['UnavailableFlags'])
        self.assertNotIn(closure, rel['UnavailableOverrides'])
        for attack, guid in bindings.items():
            self.assertEqual(self.story['SelectedAnswers'][attack], guid)
            for council in ('', 'shyka.gone', 'council.fought', 'council.fought_nocta_allied'):
                for legacy_return in (False, True):
                    with self.subTest(attack=attack, council=council, legacy=legacy_return):
                        state = rv.SimState(5, 1000)
                        state.flags.update({attack, council, 'kaylessa.dead', 'trickster', 'trickster.ever',
                                            'kaylessa.trickster.primed', 'kaylessa.committed',
                                            'kaylessa.trickster.knife_shown', 'kaylessa.wasps.in_the_dark',
                                            'kaylessa.trickster.told_borrowed'})
                        if legacy_return:
                            state.flags.add('kaylessa.trickster.returned')
                        state.times['kaylessa.trickster.primed'] = 0
                        rv.sim_complete(self.model, state)
                        self.assertIn(closure, state.flags)
                        self.assertFalse(rv.route_open(self.model, 'kaylessa', state.flags))
                        self.assertNotIn('kaylessa.harem.eligible', state.flags)
                        for sid in ('dead.borrow', 'dead.borrow_sending', 'dead.soldier', 'after.the_knife'):
                            self.assertFalse(rv.sim_available(self.model, self.model.by_id['kaylessa.trickster.' + sid], state))
                        self.assertFalse(rv.presence_wanted(self.story['Presences']['kaylessa.presence'], state,
                                                          self.story['Presences']['kaylessa.presence']['Area']))
                        for scene in self.model.scenes:
                            if scene['Id'].startswith('kaylessa.trickster.epilogue.'):
                                self.assertIn(closure, scene['Forbids'])

    def test_reveal_history_still_opens_both_bargains(self):
        state = rv.SimState(5, 1000)
        state.flags.update({'trickster', 'trickster.ever', 'kaylessa.dead', 'kaylessa.begged_death'})
        rv.sim_complete(self.model, state)
        self.assertNotIn('kaylessa.early_player_killed', state.flags)
        self.assertTrue(rv.sim_available(self.model, self.model.by_id['kaylessa.trickster.dead.borrow'], state))
        state.flags.add('council.fought')
        self.assertTrue(rv.sim_available(self.model, self.model.by_id['kaylessa.trickster.dead.borrow_sending'], state))

    def test_clean_cover_is_prepared_and_performed_for_both_hunters(self):
        sid = 'kaylessa.trickster.alive.amulet_swap'
        self.assertIn('kaylessa.trickster.alive.planned', self.scenes[sid]['Requires'])
        state = rv.SimState(5, 1000)
        state.flags.update(self.scenes[sid]['Requires'])
        state.flags.remove('kaylessa.trickster.alive.planned')
        self.assertFalse(rv.sim_available(self.model, self.model.by_id[sid], state))
        warning = 'kaylessa.trickster.alive.warning'
        for node in ('agreed', 'refused'):
            self.assertIn('patrol', self.node(warning, node)['Text'])
        for node in ('volley', 'volley_s'):
            text = self.node(sid, node)['Text']
            for step in ('kick the lantern', 'marked hollow', 'cloak', 'beneath the cloth', 'two fallen shapes', 'patrol'):
                self.assertIn(step, text)
        self.assertIn('Withdraw!', self.node(sid, 'after')['Text'])

    def test_reinforcement_loss_does_not_make_memorial_claims_false(self):
        # No current-army reader exists here: test the actual tomb/letter history with no live-unit flag.
        for sid, nid in (('kaylessa.wasps.last_words', 'tomb'), ('kaylessa.wasps.her_tomb', 'under')):
            state = rv.SimState(5, 1000)
            state.flags.update(self.scenes[sid]['Requires'])
            state.flags.update({'kaylessa.trickster.returned', 'kaylessa.trickster.primed',
                                'kaylessa.begged_death', 'kaylessa.tomb',
                                'kaylessa.trickster.cost.dark_fate_stalled'})
            state.times['kaylessa.trickster.primed'] = 0
            self.assertTrue(rv.sim_available(self.model, self.model.by_id[sid], state))
            nodes = self.scenes[sid]['Nodes']
            text = next(n['Text'] for n in nodes if n['Id'] == nid)
            for false_presence in ('in your barracks', 'in your army now', 'singing in the barracks'):
                self.assertNotIn(false_presence, text)
        self.assertIn('recorded', self.node('kaylessa.wasps.last_words', 'tomb')['Text'])
        self.assertIn('came west', self.node('kaylessa.wasps.her_tomb', 'under')['Text'])

    def test_introduction_discussion_records_request_only(self):
        sid = 'kaylessa.wasps.her_tomb'
        choice = self.node(sid, 'bring')['Choices'][0]
        self.assertIn('kaylessa.wasps.introduction_requested', choice['Set'])
        self.assertNotIn('kaylessa.wasps.marksmen_told', choice['Set'])
        self.assertIn('If their captain is alive', self.node(sid, 'bring')['Text'])
        self.assertFalse(any('kaylessa.wasps.marksmen_told' in c.get('Set', [])
                             for s in self.story['Scenes'] for n in s['Nodes'] for c in n['Choices']))

    def test_sending_memory_matches_camp_producer(self):
        text = self.node('kaylessa.wasps.the_other_you', 'shyka_sending')['Text']
        self.assertIn('dust-stained letters', text)
        self.assertIn('camp table', text)
        self.assertNotIn('empty hall', text)

    def test_both_remembered_morning_exits_return_to_awning(self):
        sid = 'kaylessa.clearing.grey_light'
        choices = self.node(sid, 'now')['Choices']
        self.assertEqual([c['Next'] for c in choices], ['ride', 'longer'])
        self.assertTrue(all('Remember' in c['Text'] for c in choices))
        self.assertIn('kaylessa.clearing.held_her', choices[1]['Set'])
        for nid in ('ride', 'longer'):
            node = self.node(sid, nid)
            self.assertIn('had', node['Text'])
            self.assertEqual(node['Choices'][0]['Text'], '[Return to the present, under the awning.]')
            self.assertFalse(node['Choices'][0]['Next'])

    def test_reserved_continuation_does_not_restart_cloak_motion(self):
        sid = 'kaylessa.clearing.where_i_was_meant_to_die'
        self.assertIn('dagger stays', self.node(sid, 'cut')['Text'])
        self.assertEqual(self.node(sid, 'cut')['Choices'][0]['Next'], 'explicit.1')
        self.assertNotIn('draws you onto', self.node(sid, 'explicit.1')['Text'])
        self.assertEqual(self.node(sid, 'explicit.1')['Choices'][0]['Set'], [])

    def test_reply_requires_thirty_day_round_trip(self):
        sid = 'kaylessa.clearing.avennara'
        scene = self.model.by_id[sid]
        state = rv.SimState(5, 0)
        state.flags.update(scene['Requires'])
        state.flags.update({'kaylessa.trickster.returned', 'kaylessa.trickster.primed'})
        state.flags.add('kaylessa.trickster.knife_held')
        state.times['kaylessa.trickster.knife_held'] = 0
        state.times['kaylessa.trickster.primed'] = 0
        state.times.update({f: 0 for f in scene['Requires']})
        for elapsed in (72, 240, 719, 720):
            state.hour = elapsed
            self.assertEqual(rv.sim_available(self.model, scene, state), elapsed >= 720)


if __name__ == '__main__':
    unittest.main()
