"""struct2-02: saved histories select the same earned dialogue branches."""
# struct2-02: saved histories must select the same earned dialogue branches.
import unittest

from tests.story_fixture import fresh_story
from tests.test_jerribeth_partner import allowed
from tools import rrt_verify as rules
from tools.claude_work_queue_lint import check as queue_check
from tools.prose_pending_lint import check as pending_check
from tools.voice_authority import read_json


class Struct2SaveHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}
        cls.model = rules.Model(cls.story)
        cls.scenes = cls.model.by_id

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_first_window_contact_has_one_owed_reply_without_island_recollection(self):
        from storylines import melazmera_trickster as route
        for suffix in ('ch4.hunt', 'ch4.hunt_found', 'ch5.hunt_window'):
            for voyage in (route.ATE, route.HARPOONED, route.CREVICE):
                flags = {'trickster.ever', route.SALTED, voyage}
                with self.subTest(meeting=suffix, voyage=voyage):
                    page = self.node(route.M + suffix, 'owed')
                    visible = [p for p in page['Paragraphs'] if allowed(p, flags)]
                    self.assertEqual(1, len(visible))
                    self.assertTrue(visible[0]['Text'].startswith('[PROSE PENDING: MEL-02'))
                    name = self.node(route.M + suffix, 'name')
                    debt = next(c for c in name['Choices'] if c['Next'] == 'owed')
                    flags.update(debt['Set'])
                    answer = next(c for c in page['Choices'] if not c['Abort'])
                    flags.update(answer['Set'])
                    if voyage == route.ATE:
                        count = self.node(route.M + 'commit.stone', 'count')
                        visible = [p for p in count['Paragraphs'] if allowed(p, flags)]
                        self.assertEqual(1, len(visible))
                        self.assertTrue(visible[0]['Text'].startswith('[PROSE PENDING: MEL-02'))

    def test_breakup_keeps_confession_only_for_actual_payment(self):
        event = 'jerribeth.commission'
        ask = self.node(event, 'ask')['Choices']
        confessed = next(c for c in ask if 'jerribeth.yard_confessed' in c['Set'])
        prisoner = next(c for c in ask if 'jerribeth.yard_prisoner_given' in c['Set'])
        histories = {
            'confession-payment': set(confessed['Set']),
            'prisoner-payment': set(prisoner['Set']),
            'successful-check': set(self.node(event, 'yard_talk_ok')['Choices'][0]['Set']),
            'pre-commission-breakup': {'jerribeth.closed'},
        }
        page = self.node('jerribeth.ending_apart', 'start')
        self.assertNotIn('a crusader\'s', page['Text'])
        paras = [p for p in page['Paragraphs'] if 'jerribeth.yard_confessed' in p['Requires']]
        self.assertEqual(1, len(paras))
        for label, flags in histories.items():
            with self.subTest(history=label):
                self.assertEqual(label == 'confession-payment', allowed(paras[0], flags))
        for sid, nid in (('jerribeth.farewell', 'start'), ('jerribeth.room_measure', 'shelves')):
            callbacks = [p for p in self.node(sid, nid).get('Paragraphs', [])
                         if 'jerribeth.yard_confessed' in p.get('Requires', [])]
            self.assertTrue(callbacks, (sid, nid))

    def test_aranka_first_meeting_is_playable_before_answer_and_once_across_venues(self):
        from storylines import aranka_trickster as route
        for chapter, suffix in ((3, ''), (5, '_late')):
            for yard in (False, True):
                state = rules.SimState(chapter, 100)
                state.flags.update(('trickster.ever', 'trickster', 'chapter_later', route.PRIMED))
                state.times[route.PRIMED] = 0
                if yard:
                    state.flags.add(route.FYE_GONE)
                rules.sim_complete(self.model, state)
                sid = 'aranka.trickster.verse.her_letter' + suffix
                primary, fallback = self.scenes[sid], self.scenes[sid + '_yard']
                selected, other = (fallback, primary) if yard else (primary, fallback)
                hub = self.story['Presences'][selected['InteractionHub']]
                self.assertTrue(rules.presence_wanted(hub, state, route.DREZEN))
                self.assertFalse(rules.presence_wanted(hub, state, 'elsewhere'))
                self.assertTrue(rules.sim_available(self.model, selected, state))
                self.assertFalse(rules.sim_available(self.model, other, state))
                self.assertFalse(selected.get('Remote'))
                self.assertNotIn('Kind', selected)
                state.flags.add(selected['Id'])
                self.assertFalse(rules.sim_available(self.model, primary, state))
                self.assertFalse(rules.sim_available(self.model, fallback, state))
                state.flags.add(route.CLOSED)
                self.assertFalse(rules.presence_wanted(hub, state, route.DREZEN))

    def test_cooled_dorgelinda_keeps_history_but_excludes_current_partner_readers(self):
        for extra in (('dorgelinda.ledger.quarrel_unmended',),
                      ('dorgelinda.ledger.quarrel_cold',),
                      ('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended')):
            state = rules.SimState(5, 100)
            state.flags.update(('trickster.ever', 'chapter_later', 'dorgelinda.committed',
                                'dorgelinda.trickster.methods_heard'))
            state.flags.update(extra)
            rules.sim_complete(self.model, state)
            self.assertIn('dorgelinda.committed', state.flags)
            expected = 'dorgelinda.ledger.quarrel_mended' in extra
            for reader in ('dorgelinda.harem.eligible', 'dorgelinda.outcome.accepted',
                           'dorgelinda.trickster.late_committed'):
                self.assertEqual(expected, reader in state.flags, (extra, reader))

    def test_placeholders_have_exact_registration_and_claude_owner(self):
        self.assertEqual([], queue_check(read_json('tools/route_packs/plans/claude-work-queue.json')))
        errors = pending_check(self.story, read_json('tools/route_packs/plans/prose-pending.json'), integration=True)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
