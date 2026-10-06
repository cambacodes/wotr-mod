"""GLOBAL-TC and ER-H2 mirror tests use actual registered body contracts."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import rrt_verify as rules

ROOT = Path(__file__).resolve().parents[1]


class Transactions(unittest.TestCase):
    def test_paid_simulation_preserves_three_argument_availability_adapters(self):
        model, scene, choice = self.fixture('Materials', 150)
        state = rules.SimState(5, 100); state.crusade_resources = {'Materials': 150}
        available = rules.sim_available
        with patch.object(rules, 'sim_available', lambda model, scene, state: available(model, scene, state)):
            self.assertTrue(rules.sim_play(model, scene, state, {'committed': set(), 'closed': set()}))
        self.assertEqual(state.crusade_resources['Materials'], 0)

    def fixture(self, resource, price):
        choice = dict(Text='Pay', Set=['step.seen', 'cost.paid', 'first.concession', 'second.concession'],
                      Crusade=dict(Resource=resource, Amount=-price))
        scene = rules.norm_scene(dict(Id='test.singleton', Owner='Seelah', Relationship='household', MinChapter=5, MaxChapter=5,
                                      Forbids=['step.seen'], RestAllowance='household.protected', InteractionHub='household.table',
                                      Nodes=[dict(Id='start', Text='Test', Choices=[choice, dict(Text='Later', Abort=True)])]))
        model = rules.Model(dict(Relationships={'household': dict(StartedFlag='hh.started', ClosedFlag='hh.closed', CommittedFlag='hh.committed')},
                                 RestAllowances={'household.protected': 2}, Scenes=[scene]))
        return model, model.scenes[0], model.scenes[0]['Nodes'][0]['Choices'][0]

    def test_eight_terminal_payment_matrix_and_saved_replay(self):
        prices = [('Finances', 200), ('Finances', 300), ('Materials', 150), ('Materials', 200),
                  ('Materials', 100), ('Materials', 150), ('Materials', 150), ('Materials', 200)]
        for resource, price in prices:
            for funds in (None, 0, price - 1, price, price + 73):
                with self.subTest(resource=resource, price=price, funds=funds):
                    model, scene, choice = self.fixture(resource, price)
                    state = rules.SimState(5, 100)
                    state.crusade_resources = None if funds is None else {resource: funds}
                    state.flags.add('prior.witness'); state.times['prior.witness'] = 12
                    before = copy.deepcopy(state)
                    affordable = funds is not None and funds >= price
                    self.assertEqual(rules.sim_choice_available(choice, state), affordable)
                    def publish():
                        state.flags.update(choice['Set'] + [scene['Id']])
                        state.times.update({flag: state.hour for flag in choice['Set'] + [scene['Id']]})
                        state.rest_spent['household.protected'] = 1
                    self.assertEqual(rules.sim_paid_choice(model, scene, choice, state, publish), affordable)
                    self.assertEqual(state.times['prior.witness'], 12)
                    if affordable:
                        self.assertEqual(state.crusade_resources[resource], funds - price)
                        loaded = copy.deepcopy(state)
                        self.assertFalse(rules.sim_paid_choice(model, scene, choice, loaded, publish))
                        scene['Id'] = 'test.packet'
                        self.assertFalse(rules.sim_paid_choice(model, scene, choice, state, publish))
                        scene['Id'] = 'test.singleton'
                        def earlier_save_publish():
                            before.flags.update(choice['Set'] + [scene['Id']])
                            before.rest_spent['household.protected'] = 1
                        self.assertTrue(rules.sim_paid_choice(model, scene, choice, before, earlier_save_publish))
                    else:
                        self.assertEqual(state.__dict__, before.__dict__)

    def test_execution_rechecks_funds_kingdom_allowance_and_rolls_back_publication(self):
        model, scene, choice = self.fixture('Materials', 150)
        for rejected in ('changed_funds', 'lost_kingdom', 'spent_allowance', 'closed_scene', 'degraded_scene', 'publication_failure'):
            with self.subTest(rejected=rejected):
                state = rules.SimState(5, 100); state.crusade_resources = {'Materials': 150}
                self.assertTrue(rules.sim_choice_available(choice, state))
                if rejected == 'changed_funds': state.crusade_resources['Materials'] = 149
                elif rejected == 'lost_kingdom': state.crusade_resources = None
                elif rejected == 'spent_allowance': state.rest_spent['household.protected'] = 2
                elif rejected == 'closed_scene': state.flags.add('hh.closed')
                elif rejected == 'degraded_scene': state.flags.add('rrt.degraded.household')
                before = copy.deepcopy(state.__dict__)
                def publish():
                    state.flags.update(choice['Set']); state.times['cost.paid'] = state.hour
                    state.rest_spent['household.protected'] = 1
                    raise RuntimeError('publication interrupted')
                self.assertFalse(rules.sim_paid_choice(model, scene, choice, state, publish))
                self.assertEqual(state.__dict__, before)

    def test_legacy_paid_recovery_keeps_the_entry_witness_and_current_guards(self):
        scene = rules.norm_scene(dict(Id='legacy.paid', Owner='Narrator', Relationship='household', MinChapter=5, MaxChapter=5,
                                      InteractionHub='household.table', Forbids=['entry.seen'], Nodes=[
            dict(Id='start', Text='Test', Choices=[dict(Set=['entry.seen'], Next='recovery', Crusade=dict(Resource='Finances', Amount=-50))]),
            dict(Id='recovery', Text='Test', Choices=[dict(Set=['entry.seen', 'full.paid'], Crusade=dict(Resource='Finances', Amount=-150))])]))
        model = rules.Model(dict(Relationships={'household': dict(StartedFlag='hh.started', ClosedFlag='hh.closed', CommittedFlag='hh.committed')}, Scenes=[scene]))
        scene = model.scenes[0]; first = scene['Nodes'][0]['Choices'][0]; recovery = scene['Nodes'][1]['Choices'][0]
        state = rules.SimState(5, 100); state.crusade_resources = {'Finances': 200}
        self.assertTrue(rules.sim_paid_choice(model, scene, first, state, lambda: state.flags.update(first['Set'])))
        self.assertFalse(rules.sim_available(model, scene, state))
        self.assertFalse(rules.sim_paid_choice(model, scene, first, state, lambda: None))
        before = copy.deepcopy(state)
        def publish():
            state.flags.update(recovery['Set'] + [scene['Id']])
        self.assertTrue(rules.sim_paid_choice(model, scene, recovery, state, publish))
        self.assertEqual(state.crusade_resources['Finances'], 0)
        before.flags.add('hh.closed')
        self.assertFalse(rules.sim_paid_choice(model, scene, recovery, before, lambda: None))
        before.flags.remove('hh.closed'); recovery['Forbids'] = ['entry.seen']
        self.assertFalse(rules.sim_paid_choice(model, scene, recovery, before, lambda: None))


class PresenceAttachments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))

    def attachment(self, name):
        presence = self.story['Presences'][name]
        owner = rules.presence_relationship(name)
        return rules.norm_scene(dict(Id='household.test.attachment', Owner='Narrator', Relationship='household',
                                     InteractionHub=name, ContactUnit=presence['Unit'], Areas=[presence['Area']],
                                     MinChapter=5, MaxChapter=5, Chapters=[5], Participants=[owner],
                                     ParticipantWomen=['minagho'] if owner == 'minagho_chivarro' else [],
                                     Requires=['trickster' if flag == 'trickster.ever' else flag for flag in presence['Requires']],
                                     RequiresAnyGroups=copy.deepcopy(presence.get('RequiresAnyGroups', [])),
                                     Forbids=presence['Forbids'] + ['trickster.failed'],
                                     Nodes=[dict(Id='start', Text='Test', Choices=[dict(Text='Continue')])]))

    def test_registered_body_variants_and_negative_attachment_matrix(self):
        for name in ('nidalynn.presence', 'nidalynn.presence.chosen',
                     'minagho_chivarro.presence.minagho', 'minagho_chivarro.presence.minagho_spared'):
            with self.subTest(name=name):
                scene = self.attachment(name)
                self.assertTrue(rules.household_presence_attachment(self.story, scene))
                story = copy.deepcopy(self.story); story['Scenes'].append(scene)
                self.assertEqual(rules.validate(rules.Model(story)), [])
                mutations = [('ContactUnit', '0' * 31 + '1'), ('Areas', ['0' * 31 + '1']), ('Chapters', [6]),
                             ('Participants', []), ('Forbids', []), ('InteractionHub', 'nidalynn.presence.unknown')]
                mutations += [('Requires', [flag for flag in scene['Requires'] if flag != gate]) for gate in scene['Requires']]
                if scene['ParticipantWomen']: mutations.append(('ParticipantWomen', ['chivarro']))
                for field, value in mutations:
                    bad = copy.deepcopy(scene); bad[field] = value
                    self.assertFalse(rules.household_presence_attachment(self.story, bad), (name, field, value))
                    story = copy.deepcopy(self.story); story['Scenes'].append(bad)
                    self.assertIn('Invalid interaction hub: ' + scene['Id'], rules.validate(rules.Model(story)))

    def test_live_path_substitutes_only_the_weaker_history_requirement(self):
        scene = self.attachment('nidalynn.presence')
        scene['Requires'] = ['trickster.now' if flag == 'trickster' else flag for flag in scene['Requires']]
        self.assertTrue(rules.household_presence_attachment(self.story, scene))
        scene['Requires'].remove('nidalynn.trickster.hearth.grey_stone')
        self.assertFalse(rules.household_presence_attachment(self.story, scene))
