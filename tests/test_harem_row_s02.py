"""Execute both approved personal-deed orders and negative S02 histories."""
import copy
import unittest

from story import make_story
from storylines import household as hh, household_pair_seelah_wenduag as sw, harem_s02
from tools import rrt_verify as v, harem_schedule_lint as schedule

P = sw.P


class S02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = make_story()
        cls.scenes = copy.deepcopy([s for s in hh.ENTRIES + hh.INVITATIONS if s['Id'].startswith(sw.PREFIX)])
        cls.story = dict(Scenes=cls.scenes, Derived=source['Derived'], DerivedForbids=source['DerivedForbids'],
                        RestAllowances=hh.REST_ALLOWANCES, PendingHooks=source['PendingHooks'],
                        Relationships={w: dict(ClosedFlag=w+'.closed', UnavailableFlags=[w+'.dead']) for w in sw.PAIR},
                        DerivedOpenRoutes={w+'.harem.eligible': [w] for w in sw.PAIR})
        cls.story['Relationships']['household'] = dict(ClosedFlag='household.closed', UnavailableFlags=[])
        for rel, spec in cls.story['Relationships'].items():
            spec.update(StartedFlag=rel+'.started', CommittedFlag=rel+'.committed')
        cls.story['Derived'].update({w+'.harem.eligible': [[w+'.committed']] for w in sw.PAIR})
        for scene in cls.scenes:
            scene.setdefault('Chapters', [5])
        cls.model = v.Model(cls.story)
        cls.scenes = cls.model.scenes

    def state(self):
        st = v.SimState(5, 1000)
        st.flags.update(['trickster', hh.PAGE_TAKEN, hh.STANCE_ELIGIBLE, hh.KEPT,
                         'seelah.committed', 'wenduag.committed', 'seelah.present_now', 'wenduag.present_now'])
        v.sim_complete(self.model, st)
        return st

    def scene(self, name):
        return next(s for s in self.scenes if s['Id'] == P(name))

    def enact(self, st, name, index=0, roll='Success'):
        scene = self.scene(name)
        self.assertTrue(v.sim_available(self.model, scene, st), name)
        node = scene['Nodes'][0]
        answer = node['Choices'][index]
        while True:
            if answer['Abort']:
                return
            target = answer.get('Next') or (answer.get('Check') or {}).get(roll)
            if target:
                node = next(n for n in scene['Nodes'] if n['Id'] == target)
                self.assertTrue(node['Choices'], target)
                answer = node['Choices'][0]
            else:
                for flag in answer['Set'] + [scene['Id']]:
                    st.flags.add(flag)
                    st.times[flag] = st.hour
                if scene.get('RestAllowance'):
                    st.rest_spent[scene['RestAllowance']] = st.rest_spent.get(scene['RestAllowance'], 0) + 1
                v.sim_complete(self.model, st)
                return

    def rest(self, st, hours=48):
        st.hour += hours
        st.rest_spent.clear()

    def prepare(self, st, restraint_first):
        self.enact(st, 'invite')
        self.enact(st, 'spar')
        self.rest(st)
        self.enact(st, 'watch')
        self.rest(st)
        self.enact(st, 'restraint' if restraint_first else 'stood')
        self.rest(st)
        self.enact(st, 'stood.after_restraint' if restraint_first else 'restraint.after_stood')
        self.rest(st)

    def test_both_orders_reach_one_mutual_night_and_morning(self):
        for first in (True, False):
            with self.subTest(restraint_first=first):
                st = self.state()
                self.prepare(st, first)
                self.enact(st, 'debt_repayment')
                self.assertFalse(v.sim_available(self.model, self.scene('choice'), st))
                self.rest(st)
                self.enact(st, 'choice')
                self.assertTrue(st.has(P('choice.both_yes')))
                self.assertTrue(st.has(sw.att('seelah', 'wenduag', 'lover')))
                self.assertFalse(st.has(sw.att('seelah', 'wenduag', 'friend')))
                self.rest(st, 8)
                self.enact(st, 'morning')
                self.assertFalse(v.sim_available(self.model, self.scene('choice'), st))

    def test_execution_rescue_failure_and_betrayal_never_buy_desire(self):
        for branch in ('execution', 'failure', 'betrayal'):
            st = self.state()
            self.enact(st, 'invite')
            self.enact(st, 'spar')
            self.rest(st)
            self.enact(st, 'watch')
            self.rest(st)
            if branch == 'execution':
                self.enact(st, 'restraint', 1)
            elif branch == 'failure':
                self.enact(st, 'stood', roll='Failure')
                self.assertFalse(st.has(sw.DEBT['owed']))
            else:
                self.enact(st, 'restraint')
                self.rest(st)
                self.enact(st, 'stood.after_restraint')
                self.rest(st)
                self.enact(st, 'debt_repayment', 2)
                self.assertFalse(st.has(sw.DEBT['paid']))
            self.rest(st)
            self.assertFalse(v.sim_available(self.model, self.scene('choice'), st), branch)
            self.assertFalse(st.has(P('choice.both_yes')))

    def test_rematch_failure_is_exhausted_and_abort_has_no_cost(self):
        st = self.state()
        self.enact(st, 'invite')
        before = copy.deepcopy(st.__dict__)
        self.enact(st, 'spar', 2)
        self.assertEqual(st.__dict__, before)
        self.enact(st, 'spar', roll='Failure')
        self.assertFalse(v.sim_available(self.model, self.scene('rematch'), st))
        self.rest(st)
        self.enact(st, 'rematch', roll='Failure')
        self.rest(st)
        self.assertFalse(v.sim_available(self.model, self.scene('watch'), st))
        self.assertFalse(v.sim_available(self.model, self.scene('rematch'), st))

    def test_attendance_page_and_enmity_rechecked(self):
        st = self.state()
        self.enact(st, 'invite')
        for flag in ('seelah.present_now', 'wenduag.present_now', hh.PAGE_TAKEN, 'trickster'):
            missing = copy.deepcopy(st)
            missing.flags.remove(flag)
            self.assertFalse(v.sim_available(self.model, self.scene('spar'), missing), flag)
        for flag in ('seelah.closed', 'wenduag.closed', 'seelah.dead', 'wenduag.dead', hh.KING_GONE):
            missing = copy.deepcopy(st)
            missing.flags.add(flag)
            v.sim_complete(self.model, missing)
            self.assertFalse(v.sim_available(self.model, self.scene('spar'), missing), flag)
        edge = hh.enmity('seelah', 'wenduag')
        st.flags.add(edge)
        v.sim_complete(self.model, st)
        self.assertFalse(v.sim_available(self.model, self.scene('spar'), st))
        st.flags.add('seelah.harem.reconciled.wenduag')
        v.sim_complete(self.model, st)
        self.assertTrue(v.sim_available(self.model, self.scene('spar'), st))

    def test_clocks_caps_and_witness_ownership(self):
        for scene in self.scenes:
            self.assertEqual(schedule.delayed_clock_errors(scene, self.story), [])
            self.assertEqual(scene.get('Participants'), list(sw.PAIR))
            for node in scene['Nodes']:
                self.assertFalse(node.get('Paragraphs'))
                for choice in node['Choices']:
                    self.assertTrue(all(flag.startswith(sw.PREFIX) for flag in choice['Set']))
        self.assertEqual(sum(s.get('HouseholdArcStart', False) for s in self.scenes), 1)
        self.assertEqual(sum(s.get('HouseholdCategory') == 'pair' for s in self.scenes), 8)

    def test_claim_recall_keeps_an_answer_in_every_knowledge_history(self):
        import itertools
        node = next(n for n in self.scene('watch')['Nodes'] if n['Id'] == 'result_0')
        flags = sw.EXTERNAL_READS['brask']
        for bits in itertools.product((False, True), repeat=3):
            held = {flag for flag, yes in zip(flags, bits) if yes}
            available = [c for c in node['Choices'] if set(c['Requires']) <= held
                         and not set(c['Forbids']) & held]
            self.assertEqual(len(available), 1, held)

    def test_every_exchange_identifies_its_speakers(self):
        from tools import player_text_lint
        self.assertEqual(player_text_lint.check(self.story)['review'], [])

    def test_exported_native_and_authored_eligibility_keep_both_orders(self):
        from tests.story_fixture import fresh_story
        exported = fresh_story()
        for native in (True, False):
            for first in (True, False):
                # Replace only the local test's mocked Wenduag eligibility with
                # the owning export's earned predicate and native history latch.
                specification = copy.deepcopy(self.story)
                specification['Derived']['wenduag.harem.eligible'] = copy.deepcopy(exported['Derived']['wenduag.harem.eligible'])
                specification['Derived']['wenduag.payoff.ordinary'] = copy.deepcopy(exported['Derived']['wenduag.payoff.ordinary'])
                model = v.Model(specification)
                st = self.state()
                st.flags.difference_update(['wenduag.committed', 'wenduag.harem.eligible'])
                if native:
                    st.flags.add('wenduag.romance_finished.latched')
                    self.assertEqual(exported['Latches']['wenduag.romance_finished.latched'], ['wenduag.romance_finished'])
                else:
                    st.flags.update(exported['Derived']['wenduag.payoff.ordinary'][0])
                v.sim_complete(model, st)
                self.assertIn('wenduag.harem.eligible', st.flags)
                previous = self.model
                self.model = model
                try:
                    self.prepare(st, first)
                    self.enact(st, 'debt_repayment', 1)
                    self.rest(st)
                    self.enact(st, 'choice')
                    self.rest(st, 8)
                    self.enact(st, 'morning')
                    self.assertFalse(v.sim_available(model, self.scene('choice'), st))
                finally:
                    self.model = previous


if __name__ == '__main__':
    unittest.main()
