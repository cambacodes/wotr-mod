"""Rubric round two: played preparation, inline history and earned memories."""
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as verify
from storylines import arsinoe_trickster as ars, eritrice_trickster as eri
from storylines import devarra_trickster as dev
from storylines.eritrice_rubric2 import OPENING


DEVARRA_CASES = (
    ('before_the_end', 'climb', 'rubric2_purchased_battle',
     ('devarra.tower.one_battle_sold', 'devarra.tower.battle_price_accepted'), ()),
    ('before_the_end', 'climb', 'rubric2_voluntary_battle',
     ('devarra.tower.battle_offered',), ('devarra.tower.battle_price_accepted',)),
    ('the_dwarf', 'protect', 'rubric2_protection_warning', ('devarra.tower.warned',), ()),
    ('the_hoard', 'honest_her', 'rubric2_clutch_debt_honest_her', ('devarra.trickster.debt_claimed',), ()),
    ('the_hoard', 'steal_her', 'rubric2_clutch_debt_steal_her', ('devarra.trickster.debt_claimed',), ()),
    ('the_hoard', 'ask_her', 'rubric2_clutch_debt_ask_her', ('devarra.trickster.debt_claimed',), ()),
)


class StructuralRoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        cls.model = verify.Model(cls.payload)

    def state(self, flags, chapter=5):
        state = verify.SimState(chapter, 10000)
        state.flags.update(flags)
        state.crusade_resources = {'Favors': 1000, 'Finances': 10000}
        verify.sim_complete(self.model, state)
        return state

    def available(self, sid, state):
        verify.sim_complete(self.model, state)
        return verify.sim_available(self.model, self.model.by_id[sid], state)

    def node(self, sid, nid):
        return next(n for n in self.model.by_id[sid]['Nodes'] if n['Id'] == nid)

    def play(self, sid, state, picks=None):
        self.assertTrue(self.available(sid, state), (sid, state.flags))
        node = self.model.by_id[sid]['Nodes'][0]
        trace = []
        for _ in range(40):
            trace.append(node['Id'])
            verify.sim_record_flags(node.get('EnterSet', []), [], state)
            verify.sim_complete(self.model, state)
            choices = [c for c in node['Choices'] if verify.sim_choice_available(c, state)]
            self.assertTrue(choices, (sid, node['Id']))
            desired = (picks or {}).get(node['Id'])
            if desired == '@refuse':
                answer = next(c for c in choices if c['Abort'])
            elif desired == '@grudge':
                answer = next(c for c in choices if eri.ON_AGENDA in c['Set'])
            else:
                answer = next((c for c in choices if (c['Next'] or c.get('PostPayment')) == desired), None) if desired else choices[0]
            self.assertIsNotNone(answer, (sid, node['Id'], desired))
            cost = answer.get('Crusade')
            def publish():
                verify.sim_record_flags(answer['Set'], [], state)
                if answer['Next'] is None and not answer['Abort']:
                    verify.sim_record_flags([sid], [], state)
            if cost and cost['Amount'] < 0:
                self.assertTrue(verify.sim_paid_choice(self.model, self.model.by_id[sid], answer, state, publish))
            else:
                publish()
            if answer['Abort']:
                return trace
            following = answer['Next'] or answer.get('PostPayment')
            if following is None:
                verify.sim_record_flags([sid], [], state)
                verify.sim_complete(self.model, state)
                return trace
            node = self.node(sid, following)
        self.fail('cycle in ' + sid)

    def test_reconciled_debate_is_playable_for_all_fought_preparation_histories(self):
        for fought in ('council.fought', 'council.fought_nocta_allied'):
            for primed in (False, True):
                for apology in (False, True):
                    with self.subTest(fought=fought, primed=primed, apology=apology):
                        flags = {'trickster', 'trickster.ever', fought, eri.LATCHED}
                        if primed:
                            flags.add(eri.PRIMED)
                        state = self.state(flags)
                        ruling = 'ruling' if fought == 'council.fought' else 'ruling_betrayal'
                        # Both actual reconciliation roads, starting at the
                        # available fought-history letter rather than a node jump.
                        state.flags.add(eri.THREAT if ruling == 'ruling' else 'trickster.ever')
                        scene = self.model.by_id[eri.P + 'fought.tabled']
                        start = scene['Nodes'][0]
                        target = next(c['Next'] for c in start['Choices']
                                      if verify.sim_choice_available(c, state) and c['Next'] not in ('struck',))
                        # Authored never-primed and primed branches choose their
                        # appropriate ruling through the whole scene.
                        picks = {start['Id']: target, target: ruling}
                        if apology:
                            # Price choice is terminal; select by position in
                            # this one node, while preserving its original price.
                            self.assertEqual(self.node(scene['Id'], ruling)['Choices'][0]['Crusade'],
                                             {'Resource': 'Favors', 'Amount': -200})
                        else:
                            # Both terminal answers have Next=None. Select the
                            # standing-grudge answer by its authored outcome.
                            picks[ruling] = '@grudge'
                        self.play(scene['Id'], state, picks)
                        self.play(eri.VISIT, state, {'open': 'apology' if apology else 'grudge'})
                        self.assertIn(eri.RETURNED, state.flags)
                        self.assertNotIn(eri.MINUTES_READ, state.flags)
                        self.assertTrue(self.available(OPENING, state))
                        grudge = [p for p in self.node(OPENING, 'open')['Paragraphs']
                                  if eri.ON_AGENDA in p['Requires']]
                        self.assertTrue(grudge)
                        self.assertEqual(not apology, any(set(p['Requires']) <= state.flags
                                                        and not set(p['Forbids']) & state.flags for p in grudge))
                        self.assertFalse(self.available('eritrice.minutes.point_one.drezen', state))
                        refusal = self.state(state.flags)
                        self.play(OPENING, refusal, {'open': '@refuse'})
                        self.assertNotIn(eri.MINUTES_READ, refusal.flags)
                        self.assertNotIn(eri.COMMITTED, refusal.flags)
                        self.play(OPENING, state, {'open': 'exchange'})
                        self.assertIn(eri.STARTED, state.flags)
                        self.assertIn(eri.MINUTES_READ, state.flags)
                        self.assertNotIn(eri.COMMITTED, state.flags)
                        state.hour += 1000
                        self.assertTrue(self.available('eritrice.minutes.point_one.drezen', state))
                        self.assertIn(eri.LATE_COMMITTED, state.flags)
                        epilogue = self.state(state.flags, chapter=6)
                        self.assertTrue(self.available(eri.P + 'epilogue.commit', epilogue))

    def test_return_opening_keeps_path_closure_and_latest_loss_guards(self):
        base = {'trickster', 'trickster.ever', eri.RETURNED, eri.VISIT, eri.ON_AGENDA}
        self.assertTrue(self.available(OPENING, self.state(base)))
        for loss in ('trickster.failed', eri.CLOSED, eri.DECLINED, 'eritrice.returned_actor_lost'):
            self.assertFalse(self.available(OPENING, self.state(base | {loss})), loss)

    def test_inline_readers_deliver_only_their_actual_histories(self):
        for suffix, host, reader, requires, forbids in DEVARRA_CASES:
            sid = 'devarra.tower.' + suffix
            for present in (False, True):
                state = self.state({'trickster', 'trickster.ever', dev.RETURNED} | (set(requires) if present else set()))
                answers = [c for c in self.node(sid, host)['Choices'] if verify.sim_choice_available(c, state)]
                self.assertEqual(reader in [c['Next'] for c in answers], present, reader)
                if present:
                    self.assertEqual([c['Next'] for c in answers], [reader])
                    self.assertTrue(self.node(sid, reader)['Choices'])
            for forbidden in forbids:
                state = self.state(set(requires) | {forbidden, 'trickster.ever'})
                self.assertNotIn(reader, [c['Next'] for c in self.node(sid, host)['Choices']
                                         if verify.sim_choice_available(c, state)])
            scene = self.model.by_id[sid]
            base = set(scene['Requires']) | set(requires) | {'trickster', 'trickster.ever', dev.RETURNED}
            for flown in (False, True):
                state = self.state(base | ({dev.PACT, dev.ESCAPED} if flown else set()))
                picks = {'climb': 'protect'} if suffix == 'the_dwarf' else {}
                if suffix == 'the_hoard':
                    approach = host.removesuffix('_her')
                    picks['her'] = 'ask_free' if flown and approach == 'ask' else approach
                trace = self.play(sid, state, picks)
                self.assertIn(reader, trace, (sid, flown))
            for loss in ('devarra.returned_actor_lost', dev.CLOSED):
                self.assertFalse(self.available(sid, self.state(base | {loss})), (sid, loss))

    def test_arsinoe_cauldron_only_entry_reaches_history_specific_late_nights(self):
        state = self.state({'trickster', 'trickster.ever', 'arsinoe.capital', 'council.cauldron_given'})
        self.play(ars.LEASE, state, {'start': 'terms', 'terms': 'rent'})
        state.hour += 1000
        self.play(ars.COLLECTION, state, {'pledge': 'word', 'stay': 'personal_offer'})
        self.assertIn(ars.STAYS, state.flags)
        self.assertNotIn('arsinoe.roof_shared', state.flags)
        self.play('arsinoe.trickster.late.ask', state, {'ask': 'yes'})
        for roof in (False, True):
            for returning in (False, True):
                flags = state.flags | ({'arsinoe.roof_shared'} if roof else set()) | ({'arsinoe.trickster.collection_night_shared'} if returning else set())
                late = self.state(flags, chapter=6)
                late.flags.add('ending.trickster')
                target = ('late_return' if returning else 'night') if roof else ('rubric2_cauldron_return' if returning else 'rubric2_cauldron_night')
                trace = self.play('arsinoe.trickster.late.commit', late, {'offer': target})
                self.assertIn(target, trace)
                self.assertIn('arsinoe.trickster.late.commit.explicit.1', trace)
                self.assertIn('morning', trace)
                self.assertEqual(roof, any(x in trace for x in ('night', 'late_return')))
                if not roof:
                    answer = next(c for c in self.node('arsinoe.trickster.late.commit', 'offer')['Choices']
                                  if c['Next'] == target)
                    self.assertIn(ars.LATE_COMMITTED, answer['Requires'])


if __name__ == '__main__':
    unittest.main()
