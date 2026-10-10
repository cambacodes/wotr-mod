"""Counterexample histories for endings plan job 3 (causes 4 and 5)."""
import unittest
from unittest.mock import patch

from tests.story_fixture import fresh_story
from storylines import jerribeth_partner as J, soana_partner as S
from tools.savecompat import EXIT_MECHANICS, check



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EndingsJob3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def holds(self, key, flags, active=()):
        if key in active:
            return False
        if any(self.holds(f, flags, (*active, key)) for f in self.story.get('DerivedForbids', {}).get(key, [])):
            return False
        if key in self.story['Derived']:
            return any(all(self.holds(f, flags, (*active, key)) for f in group)
                       for group in self.story['Derived'][key])
        return key in flags

    def enabled(self, record, flags):
        return (all(self.holds(f, flags) for f in record.get('Requires', []))
                and not any(self.holds(f, flags) for f in record.get('Forbids', []))
                and all(any(self.holds(f, flags) for f in group)
                        for group in record.get('AnyGroups', [])))

    def page(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def test_readiness_does_not_grant_separate_partner_coda(self):
        for route in ('gesmerha', 'devarra', 'eliandra', 'jerribeth', 'chadali', 'hepzamirah'):
            with self.subTest(route=route):
                self.assertEqual(self.story['Derived'][route + '.payoff.partner'], [[route + '.payoff.ordinary']])
                self.assertFalse(self.holds(route + '.payoff.partner', {'trickster.ever', route + '.trickster.late_committed'}))
                self.assertNotIn(route + '.trickster.late_committed',
                                 [flag for group in self.scenes[route + '.lastcall.page']['RequiresAnyGroups'] for flag in group])

    def test_paid_commission_needs_no_romance(self):
        for suffix in ('commit', 'commit_mourned'):
            scene = self.scenes['gesmerha.trickster.epilogue.' + suffix]
            self.assertNotIn('gesmerha.payoff.partner', scene['Requires'])
            self.assertIn('gesmerha.trickster.returned', scene['Requires'])
        flags = {'trickster.ever', 'gesmerha.trickster.returned', 'gesmerha.presence.failure_observed'}
        self.assertFalse(self.holds('gesmerha.payoff.partner', flags))

    def test_late_acceptance_refusal_and_friendship_have_local_codas(self):
        for route, branches in (
            ('devarra', ('late_accepted', 'late_refused')),
            ('hepzamirah', ('late_accepted', 'late_refused', 'late_friend')),
            ('eliandra', ('late_accepted', 'late_refused', 'late_friend')),
        ):
            suffix = 'unasked' if route == 'eliandra' else 'commit'
            sid = route + '.trickster.epilogue.' + suffix
            for branch in branches:
                with self.subTest(route=route, branch=branch):
                    page = self.page(sid, branch)
                    codas = [p for p in page.get('Paragraphs', []) if 'lastcall.active' in p['Requires']]
                    coda, = codas
                    self.assertFalse(self.enabled(coda, set()))
                    for history in (
                        {'trickster.lastcall.taken', 'ending.trickster'},
                        {'trickster.lastcall.taken', 'ending.wound_closed', 'sacrifice', 'trickster.lastcall.pillar.bottle'},
                    ):
                        self.assertTrue(self.enabled(coda, history))
                    self.assertTrue(all(not a['Set'] for a in page['Choices']))

    def test_eliandra_friendship_and_owed_letter_partition_unasked(self):
        scene = self.scenes['eliandra.trickster.epilogue.unasked']
        self.assertIn('eliandra.trickster.friendship_current', scene['Forbids'])
        self.assertIn('eliandra.trickster.letter_kept', scene['Forbids'])
        self.assertTrue(self.holds('eliandra.trickster.friendship_current',
                                  {'trickster.ever', 'eliandra.trickster.friendship_chosen'}))
        self.assertTrue(self.holds('eliandra.trickster.friendship_current',
                                  {'trickster.ever', 'eliandra.trickster.friendship_chosen', 'eliandra.trickster.letter_kept'}))
        self.assertFalse(self.holds('eliandra.trickster.friendship_current',
                                   {'trickster.ever', 'eliandra.trickster.friendship_chosen', 'eliandra.committed'}))
        self.assertTrue(any('eliandra.trickster.friendship_chosen' in a['Set']
                            for s in self.story['Scenes'] if s['Id'].startswith('eliandra.')
                            for n in s['Nodes'] for a in n['Choices']))

    def test_nocticula_and_chadali_selected_branches_keep_distinct_accounts(self):
        for route, nodes in (('nocticula', ('after_paid', 'after_refused', 'refused_page', 'inn')),
                             ('chadali', ('stay', 'half', 'friend', 'coin', 'penny'))):
            for nid in nodes:
                with self.subTest(route=route, node=nid):
                    page = self.page(route + '.trickster.epilogue.commit', nid)
                    self.assertTrue(any('lastcall.active' in p['Requires'] for p in page.get('Paragraphs', [])))
                    self.assertTrue(all(not a['Set'] for a in page['Choices']))

    def test_soana_loss_distinguishes_arrival_from_correspondence(self):
        receipt = 'soana.partner.homecoming_kept'
        for sid in S.LOSS_ENDINGS:
            paragraphs = self.scenes[sid]['Nodes'][0]['Paragraphs']
            arrivals = [p for p in paragraphs if receipt in p['Requires']]
            correspondence = [p for p in paragraphs if receipt in p['Forbids'] and S.TOGETHER in p['Requires']]
            self.assertTrue(arrivals)
            self.assertTrue(correspondence)
            for at_home in (False, True):
                flags = {S.TOGETHER, S.SHARE} | ({receipt} if at_home else set())
                selected, = [p for p in arrivals + correspondence if self.enabled(p, flags)]
                self.assertEqual(receipt in selected['Requires'], at_home)
                self.assertEqual(receipt in selected['Forbids'], not at_home)

    def test_soana_secret_stance_does_not_send_letters_or_stage_a_house_visit(self):
        sid = 'soana.trickster.epilogue.commit'
        morning = self.page(sid, 'round2_morning')
        night = next(n for n in self.scenes[sid]['Nodes'] if '.explicit.' in n['Id'])
        for node in (morning, night):
            readers = [p for p in node['Paragraphs'] if S.QUIET_RETURN in p['Requires']]
            self.assertTrue(readers)
            self.assertTrue(all(not self.enabled(p, set()) for p in readers))
            self.assertTrue(all(self.enabled(p, {S.QUIET_RETURN}) for p in readers))
        self.assertEqual([c['Next'] for c in night['Choices']], ['round2_morning'])

    def test_jerribeth_apart_has_no_ongoing_exclusive_lover(self):
        scene = self.scenes['jerribeth.ending_apart']
        self.assertIn('jerribeth.closed', scene['Requires'])
        forfeits = [p for p in scene['Nodes'][0]['Paragraphs'] if 'jerribeth.trickster.cost.forfeit' in p['Requires']]
        self.assertTrue(any('jerribeth.closed' in p['Requires'] for p in forfeits))
        self.assertTrue(any('jerribeth.closed' in p['Forbids'] for p in forfeits))
        self.assertTrue(all(not c['Set'] for n in scene['Nodes'] for c in n['Choices']))

    def test_jerribeth_selected_graph_keeps_fates_and_requires_signature_for_collection(self):
        scene = self.scenes['jerribeth.trickster.epilogue.commit']
        graph = {n['Id']: n for n in scene['Nodes']}
        for fate in (set(), {J.DEAD}, {J.CHIEF}, {J.PLANT}, {J.PLANT, J.RETURNED}):
            for stance in (set(), {J.READY, J.SHARE}, {J.READY, J.SECRET},
                           {J.READY, J.EXCLUSIVE, J.CHOSEN},
                           {J.READY, J.SECRET, J.EXPOSED, 'jerribeth.partner_exposure.plant'}):
                flags = {'chapter_later', 'trickster.ever', 'trickster.now',
                         'trickster.lastcall.taken', 'ending.trickster',
                         'jerribeth.shared_work', 'jerribeth.commission', *fate, *stance}
                pending = [('offer', False)]
                seen, terminals = set(), 0
                while pending:
                    key, signed = pending.pop()
                    if (key, signed) in seen:
                        continue
                    seen.add((key, signed))
                    self.assertFalse(key.startswith('late_local_'), key)
                    page = graph[key]
                    answers = [a for a in page['Choices'] if self.enabled(a, flags)]
                    self.assertTrue(answers, (fate, stance, key))
                    if key == 'collected':
                        self.assertTrue(signed, (fate, stance, key))
                    if key.startswith('job3_local_exit_'):
                        self.assertTrue(any('lastcall.active' in p['Requires'] for p in page['Paragraphs']))
                        self.assertTrue(all(not a['Next'] for a in page['Choices']))
                    signed = signed or key.startswith(('job3_local_signed_', 'job3_local_signed_mind_'))
                    for answer in answers:
                        self.assertEqual(answer['Set'], [], key)
                        if answer.get('Next'):
                            pending.append((answer['Next'], signed))
                        else:
                            terminals += 1
                self.assertGreater(terminals, 0, (fate, stance))

    def test_wenduag_exclusive_promise_precedes_vellexia_exception(self):
        for suffix in ('court.vellexia', 'court.vellexia.native_visit'):
            event = self.scenes['wenduag.trickster.' + suffix]
            what = next(n for n in event['Nodes'] if n['Id'] == 'what')
            self.assertIn('wenduag.partner_stance.exclusive', saved_answer(what['Choices'], 1)['Forbids'])
            exception = next(n for n in event['Nodes'] if n['Id'] == 'exclusive_exception')
            self.assertEqual([a['Next'] for a in exception['Choices']], ['hunt', 'leave'])
            self.assertIn('wenduag.partner.vellexia_exception', saved_answer(exception['Choices'], 0)['Set'])

    def test_thall_callback_is_contextual_and_delivered_once(self):
        from storylines import aranka_trickster as A
        ending = self.page('aranka.trickster.epilogue.commit', 'end')
        coda = self.page('aranka.lastcall.page', 'page')
        conclusion = next(p for p in ending['Paragraphs'] if A.THALL_ANSWERED in p['Requires'] and A.THALL_DEAD in p['Forbids'])
        callback = next(p for p in coda['Paragraphs'] if A.THALL_ANSWERED in p['Requires'] and A.THALL_DEAD in p['Forbids'])
        self.assertIn(A.THALL_ANSWERED, conclusion['Requires'])
        self.assertIn(A.THALL_DEAD, conclusion['Forbids'])
        self.assertIn(A.THALL_ANSWERED, callback['Requires'])
        self.assertIn(A.THALL_DEAD, callback['Forbids'])
        self.assertFalse(self.enabled(conclusion, set()))
        self.assertTrue(self.enabled(conclusion, {A.THALL_ANSWERED}))
        history = {A.THALL_ANSWERED, 'trickster.lastcall.taken', 'ending.trickster',
                   'trickster.ever', 'availability.observed', 'aranka.extension_kept',
                   'aranka.after_song_kept', 'aranka.extension_night'}
        self.assertFalse(self.enabled(conclusion, history))
        self.assertTrue(self.enabled(callback, history))
        self.assertTrue(any(A.THALL_ANSWERED in a['Set'] for s in self.story['Scenes']
                            for n in s['Nodes'] for a in n['Choices']))
        call = self.page('aranka.lastcall.call', 'call')

    def test_thall_verified_death_replaces_correspondence(self):
        from storylines import aranka_trickster as A
        ending = self.page('aranka.trickster.epilogue.commit', 'end')
        memory = next(p for p in ending['Paragraphs'] if A.THALL_DEAD in p['Requires'])
        conclusion = next(p for p in ending['Paragraphs'] if A.THALL_ANSWERED in p['Requires'] and A.THALL_DEAD in p['Forbids'])
        flags = {A.THALL_DEAD, A.THALL_ANSWERED}
        self.assertTrue(self.enabled(memory, flags))
        self.assertFalse(self.enabled(conclusion, flags))
        for sid in ('aranka.thall.answer', 'aranka.thall.reply'):
            self.assertIn(A.THALL_DEAD, self.scenes[sid]['Forbids'])

    def test_legacy_exit_identities_and_mechanics(self):
        self.assertEqual(check(self.story), [])
        for route in ('devarra', 'hepzamirah'):
            exit_answer = saved_answer(self.page(route + '.trickster.epilogue.commit', 'page')['Choices'], 0)
            self.assertEqual(exit_answer['Id'], 'continue')
            self.assertTrue(all(not exit_answer.get(k) for k in EXIT_MECHANICS))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        with patch.dict(self.story['Derived'], {'gesmerha.payoff.partner': [['gesmerha.trickster.late_committed']]}):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_readiness_does_not_grant_separate_partner_coda()


if __name__ == '__main__':
    unittest.main()
