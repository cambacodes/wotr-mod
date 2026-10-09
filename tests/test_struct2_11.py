"""Current-export witnesses for struct2-11's presence and hosting repairs."""
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as verify


class Structure11Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.by[sid]['Nodes'] if n['Id'] == nid)

    def test_all_return_greetings_and_legend_without_iomedae(self):
        model = verify.Model(self.story)
        for suffix in ('', '_scarred', '_stall', '_scarred_stall'):
            sid = 'galfrey.trickster.return.kitrane' + suffix
            state = verify.SimState(5, 1000)
            state.flags.update({'trickster', 'chapter_later', 'iomedae.epoch_unavailable',
                                'galfrey.trickster.eulogy.legend'})
            verify.sim_complete(model, state)
            self.assertNotIn('iomedae.present_now', state.flags)
            for choice in self.node(sid, 'name')['Choices'][:3]:
                self.assertTrue(verify.sim_choice_available(choice, state), sid)
            legend = self.node(sid, 'heard')['Choices'][1]
            self.assertEqual('e_legend', legend['Next'])
            self.assertTrue(verify.sim_choice_available(legend, state), sid)

    def test_later_actor_loss_cannot_deliver_pie_or_cross_square(self):
        model = verify.Model(self.story)
        for woman, beat, live, absent in (
            ('seelah', 'seelah', {'seelah', 'seelah_drezen'}, {'stranger', 'stranger_absent'}),
            ('irabeth', 'irabeth', {'alive', 'drezen', 'drezen_knows', 'died_back'},
             {'struct2_irabeth_absent'}),
        ):
            for suffix in ('', '_stall'):
                sid = 'galfrey.trickster.kitrane.' + beat + suffix
                for loss in ('returned_actor_lost', 'epoch_unavailable'):
                    for remembered in (False, True):
                        state = verify.SimState(5, 1000)
                        state.flags.update({'trickster', 'chapter_later', woman + '.trickster.returned',
                                            woman + '.' + loss})
                        if remembered:
                            state.flags.add('galfrey.seelah_at_bed')
                        verify.sim_complete(model, state)
                        self.assertNotIn(woman + '.present_now', state.flags)
                        choices = self.node(sid, 'start')['Choices']
                        with self.subTest(scene=sid, loss=loss, remembered=remembered):
                            self.assertFalse(any(verify.sim_choice_available(c, state)
                                                 for c in choices if c['Next'] in live))
                            self.assertTrue(any(verify.sim_choice_available(c, state)
                                                for c in choices if c['Next'] in absent))

    def test_elixir_recollections_do_not_require_iomedaes_body(self):
        for suffix in ('', '_stall'):
            choice = self.node('galfrey.trickster.kitrane.elixir' + suffix, 'grow')['Choices'][1]
            self.assertNotIn('iomedae.present_now', choice['Requires'])

    def test_local_hosts_retire_remote_delivery_and_kind(self):
        for sid in ('galfrey.trickster.ch3.standing_orders', 'iomedae.trickster.disputation',
                    'iomedae.trickster.react.ix_a.targona', 'iomedae.trickster.react.ix_a.yaniel',
                    'noct.acq.the_paid_address'):
            scene = self.by[sid]
            self.assertFalse(scene.get('Remote'))
            self.assertNotIn('Kind', scene)
            self.assertEqual(['2570015799edf594daf2f076f2f975d8'], scene['Areas'])
            self.assertTrue(scene['Entry'])
            if '.react.ix_a.' in sid:
                self.assertFalse(scene.get('Reaction'))
                woman = sid.rsplit('.', 1)[1]
                self.assertIn(woman + '.present_now', scene['Requires'])

    def test_sidequest_objectives_require_the_played_leads_and_outcomes(self):
        journal = {e['Id']: e for e in self.story['Relationships']['tirabade']['JournalEntries']}
        for sid, outcome in (
            ('three_stolen_roads', 'three_stolen_roads.settled'),
            ('three_borrowed_names', 'three_borrowed_names.heard'),
            ('three_back_of_seal', 'three_back_of_seal.kept'),
            ('three_beth_account', 'three_beth_account.kept'),
            ('three_counterclaim', 'three_counterclaim.kept'),
        ):
            entry = journal['struct2.' + sid]
            self.assertEqual([[outcome]], entry['SettledWhen'])
            self.assertTrue(any(outcome in c['Set'] for n in self.by[sid]['Nodes']
                                for c in n['Choices']))
            self.assertFalse(self.by[sid].get('Remote'))
            self.assertNotIn('Kind', self.by[sid])
        settlement = journal['struct2.three_counterclaim']
        self.assertEqual([['three_back_of_seal.kept', 'three_beth_account.kept', 'kept_terms']],
                         settlement['OpenWhen'])
        noct = next(e for e in self.story['Relationships']['nocticula.acquisition']['JournalEntries']
                    if e['Id'] == 'struct2.paid_address')
        self.assertEqual([['noct.acq.borrowed_signature_done']], noct['OpenWhen'])
        self.assertEqual([['noct.acq.the_paid_address_done']], noct['SettledWhen'])
        scene = self.by['noct.acq.the_paid_address']
        check = self.node(scene['Id'], 'start')['Choices'][0]['Check']
        self.assertEqual(('SkillKnowledgeWorld', 35, 'read', 'mistake'),
                         (check['Skill'], check['DC'], check['Success'], check['Failure']))
        self.assertIn('nocticula.reachable_by_letter', scene['Requires'])
        self.assertNotIn('nocticula.present_now', scene['Requires'])

    def test_every_survivor_can_read_lifetime_without_reunion(self):
        from storylines import iomedae_trickster as io
        sid = io.E + 'epilogue.after'
        page = self.node(sid, 'page')
        self.assertEqual('continue', page['Choices'][0]['Id'])
        self.assertIsNone(page['Choices'][0]['Next'])
        read = page['Choices'][2]
        self.assertEqual('struct2_lifetime_summary', read['Next'])
        self.assertEqual([], read['Requires'])
        self.assertEqual([], read['Forbids'])
        summary = self.node(sid, read['Next'])
        morning = self.node(sid, 'vigil_morning')
        # Both routes must retain the same consequences and conditional histories.
        self.assertEqual(morning['Paragraphs'], summary['Paragraphs'])
        self.assertGreaterEqual(len(summary['Paragraphs']), 25)
        for flags in ({io.COMMITTED}, {io.COMMITTED, 'lastcall.dead_on_record'},
                      {io.COMMITTED, io.KEPT}):
            state = verify.SimState(6, 1000)
            state.flags.update(flags)
            self.assertTrue(verify.sim_choice_available(read, state))
            reunion = page['Choices'][1]
            self.assertEqual(io.KEPT in flags, verify.sim_choice_available(reunion, state))


if __name__ == '__main__':
    unittest.main()
