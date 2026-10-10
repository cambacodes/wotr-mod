"""fix19: earned narrated attendance and strict production registration."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines import household, contract_j01
from storylines.harem_rows import ensemble_ch5
from tools import hub_attachment_lint, rrt_verify as rules


class NarratedEnsembleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.scene = cls.model.by_id[ensemble_ch5.SCENE_ID]

    def state(self, remove=(), add=()):
        state = rules.SimState(5, 1000)
        state.area = household.DREZEN
        # No observed actors: this delivery is a narrated visit.
        state.available_contacts = set()
        state.flags.update({
            'trickster', 'trickster.foresight.accepted',
            'trickster.foresight.cost.promise', household.KEPT,
            'nenio.committed', 'nenio.trickster.test_running',
            'nenio.trickster.first_night', 'nenio.in_party',
            'wenduag.in_party', 'wenduag.romance_finished.latched',
            'delamere.committed', 'delamere.trickster.second_hunt_offered',
            'delamere.trickster.caught', 'delamere.trickster.returned',
        })
        state.flags.difference_update(remove)
        state.flags.update(add)
        rules.sim_complete(self.model, state)
        return state

    def test_earned_visit_is_table_only_and_keeps_saved_action_order(self):
        state = self.state()
        self.assertTrue(rules.sim_available(self.model, self.scene, state))
        self.assertTrue(rules.is_table_scene(self.scene))
        self.assertEqual([n['Id'] for n in self.scene['Nodes']], ['start', 'shafts', 'feathers'])
        choices = self.scene['Nodes'][0]['Choices']
        self.assertEqual([c['Next'] for c in choices], ['shafts', 'feathers', None])
        self.assertTrue(choices[2]['Abort'])
        state.area = 'unrelated-area'
        self.assertFalse(rules.sim_available(self.model, self.scene, state))

    def test_return_is_required_and_old_return_never_defeats_later_loss(self):
        self.assertFalse(rules.sim_available(self.model, self.scene,
            self.state(remove=('delamere.trickster.returned',))))
        for woman in ensemble_ch5.WOMEN:
            for loss in ('.closed', '.epoch_unavailable', '.returned_actor_lost'):
                with self.subTest(woman=woman, loss=loss):
                    self.assertFalse(rules.sim_available(self.model, self.scene,
                        self.state(add=(woman + loss,))))
        for missing in ('nenio.in_party', 'wenduag.in_party', household.KEPT,
                        'trickster.foresight.accepted'):
            self.assertFalse(rules.sim_available(self.model, self.scene,
                self.state(remove=(missing,))), missing)

    def test_selected_presentation_mutations_fail_public_registration_check(self):
        self.assertEqual([], hub_attachment_lint.lint(self.story))
        for field, value in (
            ('Remote', False), ('Kind', 'letter'), ('TableHosted', False),
            ('Areas', []), ('ManualOnly', True),
            ('ParticipantContacts', {'delamere': {'Kind': 'body', 'Options': []}}),
        ):
            with self.subTest(field=field):
                story = copy.deepcopy(self.story)
                scene = next(s for s in story['Scenes'] if s['Id'] == ensemble_ch5.SCENE_ID)
                scene[field] = value
                self.assertTrue(hub_attachment_lint.gameplay_entry_lint(story))

    def test_contact_pass_preserves_native_actor_siblings_and_narrated_visit(self):
        story = copy.deepcopy(self.story)
        before = {s['Id']: copy.deepcopy(s.get('ParticipantContacts', {}))
                  for s in story['Scenes'] if s.get('InteractionHub') == household.TABLE_HUB}
        contract_j01.install(story)
        after = {s['Id']: s.get('ParticipantContacts', {})
                 for s in story['Scenes'] if s.get('InteractionHub') == household.TABLE_HUB}
        self.assertEqual(before, after)
        self.assertFalse(after[ensemble_ch5.SCENE_ID])
        self.assertTrue(any(c.get('Kind') == 'body' for contacts in after.values()
                            for c in contacts.values()))


if __name__ == '__main__':
    unittest.main()
