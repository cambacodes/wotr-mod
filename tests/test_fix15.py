"""Coordinator history regressions over the fully integrated story."""
import unittest
from unittest.mock import patch
from tests.story_fixture import fresh_story


def visible(block, flags):
    overrides = block.get('ForbidOverrides', {})
    return (set(block.get('Requires', ())) <= flags
            and not any(k in flags and overrides.get(k) not in flags for k in block.get('Forbids', ()))
            and all(set(g) & flags for g in block.get('AnyGroups', block.get('RequiresAnyGroups', ()))))



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class Fix15Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_yaniel_arrival_and_resurrection_are_distinct_in_all_deliveries(self):
        for sid in ('wenduag.trickster.early.yaniel', 'wenduag.trickster.court.yaniel',
                    'wenduag.trickster.court.yaniel.native_visit'):
            start = self.node(sid, 'start')
            def targets(flags):
                return [c['Next'] for c in start['Choices'] if visible(c, flags)]
            self.assertEqual(targets({'yaniel.trickster.returned'}), ['arrived_yaniel'], sid)
            self.assertEqual(targets({'yaniel.trickster.returned', 'yaniel.killed.latched'}), ['returned_yaniel'], sid)
            self.assertEqual(targets({'yaniel.killed.latched'}), ['killed'], sid)
            self.assertEqual(targets(set()), [], sid)
            self.assertIn('yaniel.trickster.returned', self.scenes[sid]['RequiresAnyGroups'][0])
            self.assertEqual(saved_answer(self.node(sid, 'arrived_yaniel')['Choices'], 0)['Next'], 'arrived_answer')
            self.assertIn('wenduag.trickster.yaniel.watched', saved_answer(self.node(sid, 'arrived_answer')['Choices'], 0)['Set'])

    def test_areelu_death_page_reads_history_and_never_living_entitlement(self):
        sid = 'areelu.trickster.finale.unnamed'
        s = self.scenes[sid]
        flags = {'trickster.ever', 'areelu.trickster.wager_struck', 'areelu.died_at_finale', 'areelu.committed'}
        for fate in ('areelu.dead_fight', 'areelu.incinerated', 'areelu.sacrifice_wound', 'areelu.sacrifice_before'):
            self.assertTrue(visible(s, flags | {fate}), fate)
        for loss in ('areelu.trickster.survives', 'areelu.trickster.stake_only',
                     'areelu.closed', 'areelu.trickster.commander_burned'):
            self.assertFalse(visible(s, flags | {loss}), loss)
        self.assertIn('areelu.trickster.declined', s['Forbids'])
        self.assertFalse(visible(s, (flags - {'areelu.committed'}) | {'areelu.trickster.declined'}))
        self.assertTrue(visible(s, flags | {'areelu.trickster.declined'}))  # existing accepted repair
        self.assertTrue(visible(s, flags | {'areelu.sacrifice_trickster'}))
        for k in ('areelu.outcome.route_open', 'areelu.payoff.partner', 'areelu.present_now'):
            self.assertNotIn(k, s['Requires'])
        for sibling in ('areelu.trickster.finale.stake_only', 'areelu.trickster.finale.report_stands'):
            self.assertIn(sibling, self.scenes)

    def test_hepzamirah_references_are_independent_but_participants_stay_guarded(self):
        for sid, nid, idx in (('hepzamirah.trickster.body.hounds', 'joke', 2),
                              ('hepzamirah.trickster.bond.the_call', 'if', 0),
                              ('hepzamirah.trickster.body.terms', 'price', 2)):
            choice = saved_answer(self.node(sid, nid)['Choices'], idx)
            flags = set(choice['Requires'])
            self.assertTrue(visible(choice, flags | {'areelu.closed', 'areelu.epoch_unavailable',
                                                     'horzalah.closed', 'horzalah.epoch_unavailable'}))
            self.assertFalse(any(k.startswith(('areelu.', 'horzalah.', 'crossroute.areelu.', 'crossroute.horzalah.'))
                                 for k in choice['Requires']))
        eve = self.scenes['hepzamirah.trickster.bond.eve']
        self.assertIn('hepzamirah.present_now', eve['Requires'])
        self.assertNotIn('areelu.present_now', eve['Requires'])
        sister = saved_answer(self.node('hepzamirah.trickster.body.hounds', 'sister_at_gate')['Choices'], 0)
        self.assertIn('hepzamirah.trickster.sister_here', sister['Requires'])
        self.assertIn('horzalah.present_now', self.story['Derived']['hepzamirah.trickster.sister_here'][0])

    def test_areelu_mask_references_survive_yaniel_absence(self):
        for sid in ('areelu.trickster.rivalry.lens', 'areelu.trickster.lens.watched'):
            node = self.node(sid, 'accounts')
            for index in (0, 5):
                choice = saved_answer(node['Choices'], index)
                flags = set(choice['Requires']) | {'yaniel.closed', 'yaniel.killed.latched', 'yaniel.trickster.left_free'}
                self.assertTrue(visible(choice, flags), (sid, index))
                self.assertNotIn('yaniel.present_now', choice['Requires'])
            self.assertIn('areelu.early.mask_counted', saved_answer(node['Choices'], 5)['Requires'])
        choice = saved_answer(self.node('areelu.trickster.wager.raised', 'start')['Choices'], 6)
        self.assertIn('household.pair.yaniel_areelu.cost.areelu_specific_guise', choice['Requires'])
        self.assertTrue(visible(choice, set(choice['Requires']) | {'yaniel.closed', 'yaniel.killed.latched'}))

    def test_arsinoe_physical_availability_does_not_consume_romance_closure(self):
        for key in ('crossroute.arsinoe.available', 'crossroute.arsinoe.correspondent'):
            if key not in self.story['Derived']:
                continue
            self.assertNotIn('arsinoe.closed', self.story.get('DerivedForbids', {}).get(key, []))
            self.assertNotIn('arsinoe', self.story.get('DerivedOpenRoutes', {}).get(key, []))
            self.assertTrue(all('arsinoe.present_now' in g or 'arsinoe.reachable_by_letter' in g
                                for g in self.story['Derived'][key]))
        presence = self.story['DerivedForbids']['arsinoe.present_now']
        self.assertIn('arsinoe.epoch_unavailable', presence)

    def test_nurah_parent_and_completed_prison_visits_reach_both_pair_steps(self):
        for step in ('audit', 'retry'):
            s = self.scenes['household.pair.arsinoe_nurah.' + step]
            base = set(s['Requires'])
            self.assertTrue(visible(s, base | {'nurah.meeting_arrived'}))
            self.assertTrue(visible(s, base | {'nurah.complete', 'nurah.prison', 'nurah.trickster.released'}))
            self.assertFalse(visible(s, base))
            self.assertFalse(visible(s, base | {'nurah.complete', 'nurah.prison'}))
            self.assertFalse(visible(s, (base | {'nurah.complete', 'nurah.prison', 'nurah.trickster.released'}) - {'nurah.present_now'}))

    def test_vellexia_visited_is_not_absence_at_the_shared_table(self):
        rows = [s for s in self.scenes.values() if s['Id'].startswith((
            'household.pair.arueshalae_vellexia.', 'household.pair.camellia_vellexia.',
            'household.pair.wenduag_vellexia.'))]
        self.assertTrue(rows)
        for s in rows:
            self.assertNotIn('vellexia.trickster.visited', s['Forbids'], s['Id'])
            self.assertIn('vellexia.present_now', s['Requires'], s['Id'])
            self.assertIn('vellexia.trickster.in_person', s['Requires'], s['Id'])
            self.assertIn('vellexia.trickster.kept_as_mirror', s['Forbids'], s['Id'])

    def test_shared_call_history_dispatch_retains_old_resolution_answers(self):
        for rel, cases in (
            ('galfrey', [ (set(), 'fix15_deathbed'),
                          ({'galfrey.trickster.cost.alone'}, 'fix15_alone'),
                          ({'galfrey.trickster.cost.alone', 'galfrey.trickster.cost.found_late'}, 'fix15_found_late')]),
            ('terendelev', [(set(), 'fix15_blood_thread'),
                            ({'terendelev.trickster.dressing'}, 'fix15_dressing_only'),
                            ({'terendelev.trickster.dressing', 'terendelev.lastcall.oath_recorded'}, 'fix15_oath_dressing')])):
            sid = rel + '.lastcall.call'
            node = self.node(sid, 'call')
            receipt = rel + '.lastcall.history_shown'
            for flags, target in cases:
                choices = [c for c in node['Choices'] if visible(c, flags)]
                self.assertEqual([c['Next'] for c in choices], [target], (rel, flags))
                return_choice = saved_answer(self.node(sid, target)['Choices'], 0)
                self.assertEqual(return_choice['Next'], 'call')
                self.assertIn(receipt, return_choice['Set'])
                choices = [c for c in node['Choices'] if visible(c, flags | {receipt})]
                self.assertTrue(choices)
                self.assertTrue(all(c['Next'] is None for c in choices))
                self.assertTrue(all(rel + '.lastcall.resolved' in c['Set'] for c in choices))

    def test_delamere_and_terendelev_recovery_paragraphs_read_their_histories(self):
        bridge = 'iomedae.trickster.buried_alive'
        d = self.node('delamere.lastcall.page', 'page')['Paragraphs']
        called, = [p for p in d if p['Requires'] == ['delamere.lastcall.called']]
        recovered, = [p for p in d if p['Requires'] == ['delamere.lastcall.called', bridge]]
        self.assertTrue(visible(called, {'delamere.lastcall.called'}))
        self.assertFalse(visible(called, {'delamere.lastcall.called', bridge}))
        self.assertTrue(visible(recovered, {'delamere.lastcall.called', bridge, 'crossroute.delamere.available'}))
        self.assertFalse(visible(recovered, {'delamere.lastcall.called', 'crossroute.delamere.available'}))
        t = self.node('terendelev.lastcall.page', 'page')['Paragraphs']
        dressed, = [p for p in t if p['Requires'] == ['lastcall.recovered_corked', 'terendelev.trickster.dressing', 'crossroute.terendelev.available']]
        undressed, = [p for p in t if p['Requires'] == ['lastcall.h2', bridge, 'crossroute.terendelev.available']]
        self.assertFalse(visible(dressed, {'lastcall.recovered_corked'}))
        self.assertTrue(visible(dressed, {'lastcall.recovered_corked', 'terendelev.trickster.dressing', 'crossroute.terendelev.available'}))
        self.assertTrue(visible(undressed, {'lastcall.h2', bridge, 'crossroute.terendelev.available'}))
        self.assertFalse(visible(undressed, {'lastcall.h2', bridge, 'terendelev.trickster.dressing', 'crossroute.terendelev.available'}))

    def test_dorgelinda_audit_reads_schedule_and_current_settlement(self):
        p, = [p for p in self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
              if p['Requires'] == ['dorgelinda.trickster.cost.audit_hostile', 'dorgelinda.trickster.cost.twice_weekly']]
        hostile = {'dorgelinda.trickster.cost.audit_hostile'}
        scheduled = hostile | {'dorgelinda.trickster.cost.twice_weekly'}
        self.assertFalse(visible(p, hostile))
        self.assertTrue(visible(p, scheduled))
        self.assertFalse(visible(p, scheduled | {'dorgelinda.lastcall.account_settled'}))
        self.assertEqual(self.story['Derived']['dorgelinda.lastcall.account_settled'],
                         [['dorgelinda.trickster.cost.told_all'], ['dorgelinda.lastcall.called']])

    def test_nidalynn_historical_closures_do_not_require_present_body(self):
        for ending in ('apart', 'wolves', 'lie', 'given', 'claimed'):
            sid = 'nidalynn.trickster.epilogue.' + ending
            self.assertNotIn('nidalynn.present_now', self.scenes[sid]['Requires'], sid)
        for ending in ('apart', 'unreturned', 'wolves'):
            parts = [p for p in self.node('nidalynn.trickster.epilogue.' + ending, 'page')['Paragraphs']
                     if p['Requires'] in (['nidalynn.trickster.kiln', 'nidalynn.trickster.hatched'], ['nidalynn.trickster.kiln'], [])
                     and ('nidalynn.trickster.kiln' in p['Requires'] or 'nidalynn.trickster.kiln' in p['Forbids'])]
            for flags, expected in ((set(), 2), ({'nidalynn.trickster.kiln'}, 1),
                                    ({'nidalynn.trickster.kiln', 'nidalynn.trickster.hatched'}, 0)):
                self.assertEqual([p['Requires'] for p in parts if visible(p, flags)],
                                 [[]] if expected == 2 else [['nidalynn.trickster.kiln']] if expected == 1
                                 else [['nidalynn.trickster.kiln', 'nidalynn.trickster.hatched']])

    def test_unavailable_eritrice_debt_cannot_hold_the_last_joke(self):
        key = 'eritrice.lastcall.callable'
        self.assertEqual(self.story['DerivedOpenRoutes'][key], ['eritrice'])
        self.assertIn('eritrice.epoch_unavailable', self.story['Relationships']['eritrice']['EpochUnavailableFlags'])
        for s in self.scenes.values():
            if s['Id'].startswith('trickster.lastcall.last_joke'):
                self.assertIn(key, s['Forbids'])

    def test_carrier_murder_is_shown_before_retry_completion(self):
        sid = 'household.pair.kaylessa_camellia.retry'
        prefix = 'household.pair.kaylessa_camellia.'
        sealed = self.node(sid, 'sealed')
        shown = prefix + 'carrier_cruelty_shown'
        self.assertFalse(visible(saved_answer(sealed['Choices'], 0), set()))
        self.assertTrue(visible(saved_answer(sealed['Choices'], 0), {shown}))
        self.assertIsNone(saved_answer(sealed['Choices'], 0)['Next'])
        self.assertIn(prefix + 'retry.done', saved_answer(sealed['Choices'], 0)['Set'])
        self.assertTrue(saved_answer(sealed['Choices'], 1)['Abort'])
        self.assertEqual(saved_answer(sealed['Choices'], 2)['Next'], 'carrier_shown')
        self.assertFalse(visible(saved_answer(sealed['Choices'], 2), {shown}))
        witness = saved_answer(self.node(sid, 'carrier_shown')['Choices'], 0)
        self.assertEqual(witness['Next'], 'sealed')
        self.assertTrue({shown, prefix + 'carrier_burned', prefix + 'cost.commander_evening'} <= set(witness['Set']))
        self.assertIn('kaylessa.present_now', self.scenes[sid]['Requires'])
        self.assertIn('camellia.present_now', self.scenes[sid]['Requires'])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        choice = next(c for c in self.node('wenduag.trickster.early.yaniel', 'start')['Choices'] if c['Next'] == 'arrived_yaniel')
        with patch.dict(choice, Next='returned_yaniel'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_yaniel_arrival_and_resurrection_are_distinct_in_all_deliveries()
