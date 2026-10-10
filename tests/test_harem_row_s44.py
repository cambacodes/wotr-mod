"""S44 indexed outcome, presence, personality and retry contracts."""
import copy
import unittest

from storylines import household
from storylines.harem_rows import s44
from tools import player_text_lint, rrt_verify


class S44Tests(unittest.TestCase):
    def setUp(self):
        self.entries = list(household.ENTRIES)
        self.consumers = dict(household.CONSUMERS)
        household.ENTRIES[:] = []
        self.payload = {}
        s44.register(self.payload, [], {})
        self.rows = copy.deepcopy(household.ENTRIES)

    def tearDown(self):
        household.ENTRIES[:] = self.entries
        household.CONSUMERS.clear()
        household.CONSUMERS.update(self.consumers)

    def test_registration_is_idempotent_and_extension_is_not_activated(self):
        s44.register({}, [], {})
        self.assertEqual(len(household.ENTRIES), 4)
        self.assertEqual({s['Id'] for s in self.rows}, {
            s44.P + step + '.' + branch for step in ('settle', 'retry') for branch in ('good', 'evil')})

    def test_both_women_have_attributed_replies_in_every_wrapper(self):
        self.assertEqual(player_text_lint.check({'Scenes': self.rows})['review'], [])

    def test_current_physical_attendance_on_every_wrapper(self):
        for scene in self.rows:
            for flag in ('trickster', 'foresight.page_taken', 'household.table.kept',
                         *s44.REQUIRES, 'shamira.harem.eligible', 'arueshalae.harem.eligible'):
                self.assertIn(flag, scene['Requires'])
            self.assertEqual(scene['RouteOpen'], list(s44.PAIR))
            self.assertEqual(scene['ParticipantWomen'], list(s44.PAIR))
            self.assertEqual(scene['Chapters'], [5])
            self.assertEqual(scene['RestAllowance'], 'household.protected')
            self.assertTrue(set(s44.FORBIDS) <= set(scene['Forbids']))
            self.assertNotIn('arueshalae_dead', scene['ForbidOverrides'])
            self.assertNotIn('arueshalae.evil_dead', scene['ForbidOverrides'])
            for a, b in (s44.PAIR, s44.PAIR[::-1]):
                self.assertEqual(scene['ForbidOverrides'][a + '.harem.enmity.' + b],
                                 a + '.harem.reconciled.' + b)

    def test_personality_and_actual_recruited_body(self):
        for scene in self.rows:
            if scene['Id'].endswith('.good'):
                self.assertIn('arueshalae.redeemed', scene['Requires'])
                self.assertIn('arueshalae.corrupted', scene['Forbids'])
                self.assertEqual(scene['RequiresAnyGroups'], [[
                    'arueshalae.recruited_drezen', 'arueshalae.recruited_redoubt']])
            else:
                self.assertIn('arueshalae.corrupted', scene['Requires'])
                self.assertEqual(scene['RequiresAnyGroups'], [['arueshalae.evil_recruited']])

    def test_indexed_terminal_writes_and_abort_are_atomic(self):
        for scene in self.rows:
            retry = '.retry.' in scene['Id']
            nodes = {n['Id']: n for n in scene['Nodes']}
            start = nodes['start']['Choices']
            self.assertIn(contract_identities(start),
                    {4: (((None, 'held', 'fell', False, (), ()),
                          ('padded', None, None, False, (), ()),
                          ('declined', None, None, False, (), ()),
                          (None, None, None, True, (), ())),),
                     3: ((('kept', None, None, False, (), ()),
                          ('refused', None, None, False, (), ()),
                          (None, None, None, True, (), ())),)}[3 if retry else 4])
            for choice in start:
                self.assertEqual(choice['Set'], [])
            expected = ({'kept': ('retry.done',) + s44.SUCCESS + ('cost.commander_demonstration',),
                         'refused': ('retry.declined', 'claim.unsettled')} if retry else {
                'held': ('settle.done',) + s44.SUCCESS,
                'padded': ('settle.done',) + s44.SUCCESS + ('cost.commander_demonstration',),
                'fell': ('settle.failed', 'landing_stopped'),
                'declined': ('settle.declined', 'claim.unsettled')})
            for nid, suffixes in expected.items():
                choices = nodes[nid]['Choices']
                step = 'retry' if retry else 'settle'
                self.assertEqual(select_answer(choices, ((None, False, None, None, (), ()),), expected_position=0)['Set'], [s44.P + f for f in (step + '.seen',) + suffixes])
                self.assertTrue(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1)['Abort'])
                self.assertFalse(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1)['Set'])
                self.assertFalse(select_answer(choices, ((None, True, None, None, (), ()),), expected_position=1).get('NativeNext'))
            for node in scene['Nodes']:
                for choice in node['Choices']:
                    self.assertFalse(any('.harem.' in flag for flag in choice['Set']))
                    self.assertFalse(choice.get('RemoveItem'))
                    self.assertFalse(choice.get('Revive'))

    def test_retry_clock_uses_failure_not_derived_stage_and_no_cap(self):
        for scene in self.rows:
            self.assertFalse(any('household.cap.' in f for f in scene['Forbids']))
            if '.retry.' in scene['Id']:
                self.assertEqual(scene['DelayHours'], 48)
                self.assertIn(s44.P + 'settle.failed', scene['Requires'])
                self.assertNotIn(s44.P + 'settle.seen', scene['Forbids'])
            else:
                check = select_answer(scene['Nodes'][0]['Choices'], ((None, False, 'held', 'fell', (), ()),), expected_position=0)['Check']
                self.assertEqual(check, dict(Skill='SkillAthletics', DC=26, Success='held', Failure='fell'))

    def test_engine_respect_declarations_require_both_deed_and_cost(self):
        for key, flags in {
            'arueshalae.harem.attitude.shamira.respect': ['shamira_released', 'cost.shamira_public_release'],
            'shamira.harem.attitude.arueshalae.respect': ['arueshalae_ornament_returned', 'cost.arueshalae_trophy_yielded'],
        }.items():
            self.assertEqual(self.payload['Derived'][key], [[s44.P + f for f in flags]])
            self.assertEqual(self.payload['DerivedForbids'][key], [
                s44.P + 'suppressed.shamira', s44.P + 'suppressed.arueshalae'])
        for a, b in (s44.PAIR, s44.PAIR[::-1]):
            suppressed = s44.P + 'suppressed.' + a
            self.assertIn(a + '.harem.enmity.' + b, self.payload['PendingHooks'])
            self.assertIn(a + '.harem.reconciled.' + b, self.payload['PendingHooks'])
            self.assertEqual(self.payload['Derived'][suppressed], [[a + '.harem.enmity.' + b]])
            self.assertEqual(self.payload['DerivedForbids'][suppressed], [a + '.harem.reconciled.' + b])

    def model(self):
        payload = copy.deepcopy(self.payload)
        payload['Scenes'] = self.rows
        payload['RestAllowances'] = {'household.protected': 2}
        payload['Relationships'] = {r: dict(StartedFlag=r + '.started', CommittedFlag=r + '.committed',
                                           ClosedFlag=r + '.closed', UnavailableFlags=[])
                                    for r in (*s44.PAIR, 'household')}
        return rrt_verify.Model(payload)

    def state(self, scene, hour=0):
        state = rrt_verify.SimState(5, hour)
        state.flags.update(scene['Requires'])
        state.flags.update(group[0] for group in scene['RequiresAnyGroups'])
        return state

    def test_retry_47_48_hours_reload_and_allowance(self):
        model = self.model()
        for branch in ('good', 'evil'):
            initial = model.by_id[s44.P + 'settle.' + branch]
            retry = model.by_id[s44.P + 'retry.' + branch]
            state = self.state(initial)
            failure = select_answer(next(n for n in initial['Nodes'] if n['Id'] == 'fell')['Choices'], ((None, False, None, None, (), ()),), expected_position=0)
            state.flags.update(failure['Set'])
            state.times.update({flag: 0 for flag in failure['Set']})
            for hour, available in ((47, False), (48, True)):
                state.hour = hour
                self.assertEqual(rrt_verify.sim_available(model, retry, copy.deepcopy(state)), available)
            paused = copy.deepcopy(state)
            abort = select_answer(next(n for n in retry['Nodes'] if n['Id'] == 'kept')['Choices'], ((None, True, None, None, (), ()),), expected_position=1)
            self.assertTrue(abort['Abort'])
            self.assertEqual(abort['Set'], [])
            self.assertEqual(state.flags, paused.flags)
            success = select_answer(next(n for n in retry['Nodes'] if n['Id'] == 'kept')['Choices'], ((None, False, None, None, (), ()),), expected_position=0)
            state.flags.update(success['Set'])
            rrt_verify.sim_complete(model, state)
            self.assertIn(s44.P + 'settle.failed', state.flags)
            self.assertNotIn(s44.P + 'claim.unsettled', state.flags)
            for a, b in (s44.PAIR, s44.PAIR[::-1]):
                self.assertIn(a + '.harem.attitude.' + b + '.respect', state.flags)
                self.assertNotIn(a + '.harem.enmity.' + b, state.flags)
            spent = self.state(retry, 48)
            spent.times[s44.P + 'settle.failed'] = 0
            spent.rest_spent['household.protected'] = 2
            self.assertFalse(rrt_verify.sim_available(model, retry, spent))

    def test_unearned_page_current_loss_and_enmity_fail_closed(self):
        model = self.model()
        for scene in model.scenes:
            state = self.state(scene, 48)
            self.assertTrue(rrt_verify.sim_available(model, scene, state))
            for gate in ('foresight.page_taken', 'shamira.present_now', 'arueshalae.present_now',
                         'shamira.trickster.embodied'):
                missing = copy.deepcopy(state)
                missing.flags.remove(gate)
                self.assertFalse(rrt_verify.sim_available(model, scene, missing))
            for loss in ('arueshalae_dead', 'arueshalae.evil_dead', 'arueshalae.kicked_out',
                         'shamira.epoch_unavailable', 'shamira.trickster.cost.kept_captive'):
                absent = copy.deepcopy(state)
                absent.flags.update([loss, 'arueshalae.trickster.returned', 'shamira.trickster.returned'])
                self.assertFalse(rrt_verify.sim_available(model, scene, absent))
            for a, b in (s44.PAIR, s44.PAIR[::-1]):
                opposed = copy.deepcopy(state)
                opposed.flags.add(a + '.harem.enmity.' + b)
                self.assertFalse(rrt_verify.sim_available(model, scene, opposed))
                opposed.flags.add(a + '.harem.reconciled.' + b)
                self.assertTrue(rrt_verify.sim_available(model, scene, opposed))




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)


if __name__ == '__main__':
    unittest.main()
