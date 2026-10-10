"""S27: exact claim producers, two methods, bounded retry and current attendance."""
import copy
import unittest

from tests.story_fixture import fresh_story, row_registration_fixture
from storylines.harem_rows import s27 as row
from tools import rrt_verify as rules
from tools.harem_schedule_lint import delayed_clock_errors

P = row.P


class S27Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.model.scenes if s['Id'].startswith(P)}

    def state(self):
        state = rules.SimState(5, 1000)
        state.flags.update(['trickster', 'trickster.foresight.accepted', 'household.table.kept',
            'soana.committed', 'soana.progression_kept', 'soana.late_thorn_tested',
            'soana.late_future_chosen', 'soana.partner_stance.secret',
            'camellia.committed', 'camellia.trickster.terms_named',
            'soana.trickster.returned', 'soana.trickster.accounting_invited', 'chapter_later'])
        rules.sim_complete(self.model, state)
        return state

    def answer(self, scene, node, index, state, result=None):
        page = next(n for n in scene['Nodes'] if n['Id'] == node)
        choice = page['Choices'][index]
        self.assertTrue(rules.sim_choice_available(choice, state), (node, index))
        state.flags.update(choice['Set'])
        for flag in choice['Set']:
            state.times[flag] = state.hour
        rules.sim_complete(self.model, state)
        return choice.get('Check', {}).get(result) if result else choice['Next']

    def test_each_method_produces_claim_before_withdrawal_and_unmasking_earns_nothing(self):
        settle = self.scenes[P + 'settle']
        for unmasked in (False, True):
            for method in ('check', 'witness'):
                for result in (('Success', 'Failure') if method == 'check' else (None,)):
                    with self.subTest(unmasked=unmasked, method=method, result=result):
                        state = self.state()
                        if unmasked:
                            state.flags.add('camellia.mireya_unmasked')
                        self.assertNotIn(P + 'respect', state.flags)
                        key = self.answer(settle, 'start', 0 if method == 'check' else 1, state)
                        self.assertFalse(set(row.CLAIM) & state.flags)
                        key = self.answer(settle, key, 0, state)
                        self.assertTrue(set(row.CLAIM) <= state.flags)
                        key = self.answer(settle, key, int(unmasked) if method == 'check' else 0, state, result)
                        self.answer(settle, key, 0, state)
                        kept = result != 'Failure'
                        self.assertEqual(P + 'respect' in state.flags, kept)
                        self.assertEqual(set(row.DEED) <= state.flags, kept)
                        self.assertIn(P + 'settle.' + ('kept' if kept else 'failed'), state.flags)

    def test_refusal_and_abort_do_not_assert_claim_or_spend_a_second_attempt(self):
        settle = self.scenes[P + 'settle']
        state = self.state()
        key = self.answer(settle, 'start', 2, state)
        self.answer(settle, key, 0, state)
        self.assertFalse(set(row.CLAIM) & state.flags)
        self.assertFalse(rules.sim_available(self.model, self.scenes[P + 'retry'], state))
        later = settle['Nodes'][0]['Choices'][3]
        self.assertTrue(later['Abort'])
        self.assertEqual(later['Set'], [])
        self.assertIsNone(later['Next'])

    def test_retry_uses_failed_timestamp_and_retains_same_scope(self):
        retry = self.scenes[P + 'retry']
        self.assertEqual(delayed_clock_errors(retry, self.story), [])
        for index, outcome in ((0, 'kept'), (1, 'failed'), (2, 'declined')):
            state = self.state()
            state.flags.update([P + 'settle.seen', P + 'settle.failed', *row.CLAIM])
            state.times[P + 'settle.failed'] = 1000
            rules.sim_complete(self.model, state)
            state.hour = 1047
            self.assertFalse(rules.sim_available(self.model, retry, state))
            state.hour = 1048
            self.assertTrue(rules.sim_available(self.model, retry, state))
            key = self.answer(retry, 'start', index, state)
            self.answer(retry, key, 0, state)
            self.assertIn(P + 'retry.' + outcome, state.flags)
            self.assertFalse(rules.sim_available(self.model, retry, state))

    def test_paid_page_current_routes_and_later_losses_guard_both_steps(self):
        for step in ('settle', 'retry'):
            scene = self.scenes[P + step]
            base = self.state()
            if step == 'retry':
                base.flags.update([P + 'settle.failed', *row.CLAIM])
                base.times[P + 'settle.failed'] = 900
                rules.sim_complete(self.model, base)
            self.assertTrue(rules.sim_available(self.model, scene, base))
            for flag in ('trickster', 'trickster.foresight.accepted', 'household.table.kept'):
                state = copy.deepcopy(base)
                state.flags.remove(flag)
                rules.sim_complete(self.model, state)
                self.assertFalse(rules.sim_available(self.model, scene, state), flag)
            for flag in ('soana.closed', 'camellia.closed', 'soana.dead', 'soana.killed_by_camellia',
                         'soana.forest_dead', 'camellia.dead', 'camellia.kicked_out',
                         'soana.epoch_unavailable', 'camellia.epoch_unavailable',
                         'soana.returned_actor_lost', 'camellia.returned_actor_lost', *row.ENMITY):
                state = copy.deepcopy(base)
                state.flags.add(flag)
                if flag in ("soana.dead", "soana.killed_by_camellia", "soana.forest_dead"):
                    state.flags.discard("soana.trickster.returned")
                rules.sim_complete(self.model, state)
                self.assertFalse(rules.sim_available(self.model, scene, state), flag)
            returned = copy.deepcopy(base)
            returned.flags.update(['soana.dead', 'soana.trickster.returned',
                                   'soana.trickster.accounting_invited'])
            rules.sim_complete(self.model, returned)
            self.assertIn('soana.round2.returned_now', returned.flags)
            self.assertTrue(rules.sim_available(self.model, scene, returned))
            returned.flags.add('soana.epoch_unavailable')
            rules.sim_complete(self.model, returned)
            self.assertFalse(rules.sim_available(self.model, scene, returned))

    def test_both_bodies_are_required_at_wintersun_and_no_canon_or_state_writers(self):
        for scene in self.scenes.values():
            self.assertEqual(scene['Areas'], [row.AREA])
            self.assertEqual(scene['ContactUnit'], row.SOANA)
            self.assertEqual(scene['AdditionalContactUnits'], [row.CAMELLIA])
            self.assertEqual(scene['Participants'], ['soana', 'camellia'])
            self.assertFalse(scene.get('ManualOnly'))
            self.assertTrue(scene['Entry'])
            self.assertEqual(scene['Chapters'], [5])
            self.assertEqual(scene['InteractionHub'], 'soana.presence')
            self.assertEqual(scene['RestAllowance'], 'household.protected')
            for node in scene['Nodes']:
                self.assertEqual(node.get('Paragraphs', []), [])
                for choice in node['Choices']:
                    final_failure = P + 'retry.failed' in choice['Set']
                    controller_flags = {'soana.harem.enmity.camellia', 'soana.harem.stance.tolerated'}
                    actual_controller = set(choice['Set']) & controller_flags
                    self.assertEqual(actual_controller,
                                     controller_flags if final_failure and
                                     'soana.harem.enmity_any' in choice['Forbids'] else set())
                    incident = set(choice['Set']) - controller_flags
                    self.assertTrue(all(flag.startswith(P) for flag in incident))
                    self.assertFalse(any(term in flag for term in ('.attitude.', '.enmity.', '.stance.', '.lover')
                                         for flag in incident))
        self.assertEqual(self.story['Derived'][P + 'respect'], [list(row.DEED)])

    def test_registration_is_repeatable_without_mutating_base_scene_list(self):
        from story import scenes
        before = copy.deepcopy(scenes)
        first, second = row_registration_fixture(row), row_registration_fixture(row)
        for payload in (first, second):
            row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(scenes, before)
        self.assertEqual(first, second)
        for payload in (first, second):
            self.assertEqual(sum(s['Id'].startswith(P) for s in payload['Scenes']), 2)
