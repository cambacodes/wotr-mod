"""S01 branch walks against the current engine, including post-return losses."""
import unittest
from unittest.mock import patch

from storylines import household
from storylines.harem_rows import s01
from tests.story_fixture import fresh_story
from tools import rrt_verify as verify
from tools import player_text_lint



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class SnareRow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.consumers = dict(household.CONSUMERS)
        cls.story = fresh_story()
        s01.register(cls.story, cls.story['Scenes'], cls.story['Etudes'])
        cls.model = verify.Model(cls.story)

    @classmethod
    def tearDownClass(cls):
        household.CONSUMERS.clear()
        household.CONSUMERS.update(cls.consumers)

    def state(self):
        state = verify.SimState(5, 1000)
        state.flags.update(('trickster', 'household.table.kept', 'trickster.foresight.accepted',
                            'camellia.committed', 'camellia.trickster.terms_named',
                            'wenduag.committed', 'wenduag.trickster.proved', 'wenduag.trickster.gate_seen',
                            'wenduag.trickster.claim.given', 'wenduag.in_party', 'chapter_later'))
        state.available_contacts = {option['Units'][0]
                                    for contact in self.model.by_id[s01.p('settle')]['ParticipantContacts'].values()
                                    for option in contact['Options']}
        verify.sim_complete(self.model, state)
        return state

    def available(self, state, step='settle'):
        verify.sim_complete(self.model, state)
        return verify.sim_available(self.model, self.model.by_id[s01.p(step)], state)

    def terminal(self, state, step, node):
        choice = saved_answer(next(n for n in self.model.by_id[s01.p(step)]['Nodes'] if n['Id'] == node)['Choices'], 0)
        state.flags.update(choice['Set'])
        state.times.update({flag: state.hour for flag in choice['Set']})
        verify.sim_complete(self.model, state)
        return choice

    def test_deeds_alone_earn_bounded_respect(self):
        state = self.state()
        self.assertTrue(self.available(state))
        self.assertTrue(all(key not in state.flags for key in s01.LADDER))
        self.terminal(state, 'settle', 'reversed')
        self.assertFalse(self.available(state))
        self.assertFalse(self.available(state, 'retry'))
        for a, b in (s01.PAIR, s01.PAIR[::-1]):
            self.assertIn(a + '.harem.attitude.' + b + '.respect', state.flags)
            self.assertNotIn(a + '.harem.attitude.' + b + '.lover', state.flags)
        # A missing reciprocal deed cannot be replaced by page or commitment.
        state.flags.remove(s01.p('deed.wenduag_hunters_moved'))
        verify.sim_complete(self.model, state)
        self.assertNotIn('camellia.harem.attitude.wenduag.respect', state.flags)

    def test_failed_approach_has_one_timestamped_retry(self):
        state = self.state()
        self.terminal(state, 'settle', 'missed')
        state.hour += 47
        self.assertFalse(self.available(state, 'retry'))
        state.hour += 1
        self.assertTrue(self.available(state, 'retry'))
        self.terminal(state, 'retry', 'reversed')
        self.assertFalse(self.available(state, 'retry'))
        self.assertIn(s01.p('settle.done'), state.flags)

    def test_refusal_does_not_close_either_route_or_make_an_enemy(self):
        for retry in (False, True):
            state = self.state()
            if retry:
                self.terminal(state, 'settle', 'missed')
                state.hour += 48
            self.terminal(state, 'retry' if retry else 'settle', 'refused')
            self.assertFalse(self.available(state, 'retry'))
            for woman in s01.PAIR:
                self.assertNotIn(woman + '.closed', state.flags)
            self.assertNotIn('camellia.harem.attitude.wenduag.respect', state.flags)
            self.assertNotIn('camellia.harem.enmity.wenduag', state.flags)

    def test_abort_is_before_the_deed_and_spends_nothing(self):
        for step, later in (('settle', 3), ('retry', 2)):
            body = self.model.by_id[s01.p(step)]
            choice = saved_answer(body['Nodes'][0]['Choices'], later)
            self.assertTrue(choice['Abort'])
            self.assertEqual(choice['Set'], [])
            self.assertIsNone(choice['Next'])
            self.assertEqual(body['RestAllowance'], 'household.protected')
            self.assertEqual(body['HouseholdWitness'], s01.p(step + '.seen'))

    def test_page_path_chapter_enmity_and_saved_allowance_apply_to_both_entries(self):
        for step in ('settle', 'retry'):
            base = self.state()
            if step == 'retry':
                self.terminal(base, 'settle', 'missed')
                base.hour += 48
            self.assertTrue(self.available(base, step))
            for blocker in ('fool_king.gone', 'trickster.failed', 'camellia.closed', 'wenduag.closed',
                            'sacrifice', 'camellia.harem.enmity.wenduag', 'wenduag.harem.enmity.camellia'):
                with self.subTest(step=step, blocker=blocker):
                    base.flags.add(blocker)
                    self.assertFalse(self.available(base, step))
                    base.flags.remove(blocker)
            base.flags.remove('trickster.foresight.accepted')
            self.assertFalse(self.available(base, step))
            base.flags.add('trickster.foresight.accepted')
            base.flags.remove('trickster')
            self.assertFalse(self.available(base, step))
            base.flags.add('trickster')
            for chapter in (3, 4, 6):
                base.chapter = chapter
                self.assertFalse(self.available(base, step))
            base.chapter = 5
            base.rest_spent['household.protected'] = 2
            self.assertFalse(self.available(base, step))

    def test_returns_do_not_override_later_loss_or_closure(self):
        state = self.state()
        state.flags.remove('wenduag.in_party')
        state.flags.update(('camellia.killed', 'camellia.trickster.cost.knows_you_tried',
                            'camellia.trickster.native_death_observed', 'wenduag.dead_any', 'wenduag.trickster.returned'))
        self.assertTrue(self.available(state))
        for step in ('settle', 'retry'):
            if step == 'retry':
                self.terminal(state, 'settle', 'missed')
                state.hour += 48
            for blocker in ('camellia.returned_actor_lost', 'camellia.epoch_unavailable',
                            'wenduag.returned_actor_lost', 'wenduag.epoch_unavailable',
                            'wenduag.q3_sent_away', 'wenduag.q3_killed', 'wenduag.hello_sent_away',
                            'wenduag.hello_attacked', 'wenduag.trickster.echo.abyss.unavailable',
                            'camellia.closed', 'wenduag.closed'):
                with self.subTest(step=step, blocker=blocker):
                    state.flags.add(blocker)
                    self.assertFalse(self.available(state, step))
                    state.flags.remove(blocker)

    def test_registration_is_append_only_and_keeps_partner_terms(self):
        before = [s['Id'] for s in self.story['Scenes']]
        relationships = self.story['Relationships'].copy()
        s01.register(self.story, self.story['Scenes'], self.story['Etudes'])
        self.assertEqual([s['Id'] for s in self.story['Scenes']], before)
        self.assertEqual(self.story['Relationships'], relationships)
        for step in ('settle', 'retry'):
            body = self.model.by_id[s01.p(step)]
            for node in body['Nodes']:
                self.assertFalse(node.get('Paragraphs'))
                for choice in node['Choices']:
                    self.assertTrue(all(flag.startswith(s01.PREFIX) for flag in choice['Set']))

    def test_both_exchanges_pass_player_text_checks(self):
        row = {'Scenes': [s01._scene(False), s01._scene(True)]}
        self.assertEqual(player_text_lint.check(row)['review'], [])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        choice = self.model.by_id[s01.p('settle')]['Nodes'][0]['Choices'][3]
        with patch.dict(choice, Abort=False):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_abort_is_before_the_deed_and_spends_nothing()


if __name__ == '__main__':
    unittest.main()
