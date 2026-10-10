"""Replay Delamere's audited callbacks from the assembled, folded story."""
from tests.story_fixture import fresh_story
from tests.structure import visible_slots
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from expansion import make_expansion
from tools.rrt_verify import Model, SimState, sim_available, sim_complete
P = 'delamere.trickster.'

def matches(item, flags):
    return all((flag in flags for flag in item.get('Requires', []))) and (not any((flag in flags for flag in item.get('Forbids', [])))) and all((any((flag in flags for flag in group)) for group in item.get('AnyGroups', [])))

def play(scene, flags, *, choices=None, mobility='Success', checks=None):
    """Follow actual answer indices and check targets; default to the first open answer."""
    flags = set(flags) | {'trickster', 'chapter_later'}
    nodes = {node['Id']: node for node in scene['Nodes']}
    node_id = scene['Nodes'][0]['Id']
    seen = set()
    visited = set()
    while node_id:
        if node_id in seen:
            raise AssertionError('Replay loop: ' + node_id)
        seen.add(node_id)
        state = SimState(5, 5000)
        state.flags.update(flags)
        sim_complete(play.model, state)
        flags = state.flags
        node = nodes[node_id]
        visited.add(node_id)
        open_answers = [(i, c) for i, c in enumerate(node['Choices']) if matches(c, flags)]
        index = (choices or {}).get(node_id, open_answers[0][0] if open_answers else -1)
        answer = next((c for i, c in open_answers if i == index), None)
        if answer is None:
            raise AssertionError('No open answer: ' + node_id)
        flags.update(answer['Set'])
        check = answer.get('Check')
        if check:
            outcome = (checks or {}).get(check['Skill'], mobility if check['Skill'] == 'SkillMobility' else 'Success')
            node_id = check[outcome]
        else:
            node_id = answer['Next']
    return (flags, visited)

class DelamerePolishTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = cls.model.by_id
        play.model = cls.model

    def derive(self, flags):
        state = SimState(5, 5000)
        state.flags.update(set(flags) | {'chapter_later'})
        sim_complete(self.model, state)
        return state.flags

    def test_open_route_derives_late_commitment_and_household(self):
        for truth in ('told_truth', 'told_both', 'confessed'):
            with self.subTest(truth=truth):
                flags = self.derive({'trickster.ever', P + 'second_hunt_offered', P + truth})
                self.assertTrue({P + 'late_committed', 'delamere.harem.eligible', 'delamere.harem.voice.a_village_not_a_city'} <= flags)
        flags = self.derive({'delamere.committed'})
        self.assertNotIn('delamere.harem.eligible', flags)
        flags = self.derive({'delamere.committed', P + 'second_hunt_offered', P + 'caught'})
        self.assertIn('delamere.harem.eligible', flags)
        self.assertIn('delamere.harem.voice.a_village_not_a_city', flags)

    def test_second_hunt_closure_withholds_commitment_and_household(self):
        for hunt in ('woods.second_hunt', 'woods.second_hunt_page', 'woods.second_hunt_late'):
            for truth in ('told_truth', 'told_both', 'confessed'):
                with self.subTest(hunt=hunt, truth=truth):
                    flags, _ = play(self.scenes[P + hunt], {'trickster.ever', P + 'second_hunt_offered', P + truth}, choices={'choice': 2})
                    self.assertIn('delamere.closed', flags)
                    flags = self.derive(flags)
                    self.assertNotIn(P + 'late_committed', flags)
                    self.assertNotIn('delamere.harem.eligible', flags)
                    self.assertNotIn('delamere.harem.voice.a_village_not_a_city', flags)

    def test_every_closure_withholds_both_household_sources(self):
        for scene in self.scenes.values():
            if scene.get('Relationship') != 'delamere':
                continue
            for node in scene['Nodes']:
                for index, choice in enumerate(node['Choices']):
                    if 'delamere.closed' not in choice['Set']:
                        continue
                    with self.subTest(scene=scene['Id'], node=node['Id'], choice=index):
                        flags = self.derive({'trickster.ever', 'delamere.committed', P + 'second_hunt_offered', P + 'told_truth', *choice['Set']})
                        self.assertNotIn(P + 'late_committed', flags)
                        self.assertNotIn('delamere.harem.eligible', flags)
                        self.assertNotIn('delamere.harem.voice.a_village_not_a_city', flags)

    def test_mobility_outcomes_through_first_frost(self):
        waking = self.scenes[P + 'crypt.stag']
        for outcome in ('Success', 'Failure'):
            with self.subTest(outcome=outcome):
                flags, _ = play(waking, {'delamere.tomb_opened'}, mobility=outcome)
                flags.update({P + 'second_hunt_offered', P + 'told_truth'})
                flags, _ = play(self.scenes[P + 'woods.second_hunt'], flags)
                self.assertIn('delamere.committed', flags)
                flags, visited = play(self.scenes[P + 'woken.day_owed'], flags)
                self.assertIn(P + 'first_frost', flags)
                self.assertIn('roofs', visited)
                if outcome == 'Success':
                    self.assertIn('caught_again', visited)
                    self.assertNotIn('caught_again_short', visited)
                else:
                    self.assertIn('caught_again_short', visited)
                    self.assertNotIn('caught_again', visited)
                    self.assertNotIn('caught_again', visited)

    def test_first_meat_in_both_folds_and_standalone(self):
        for count in ('woken.count', 'woken.count_late'):
            for allocation in (0, 1):
                with self.subTest(count=count, allocation=allocation):
                    home = 'home_late' if count.endswith('_late') else 'home'
                    flags, folded = play(self.scenes[P + count], set(), choices={'first_meat.law': allocation, 'first_meat.' + home: allocation + 1})
                    self.assertIn(P + 'first_meat', flags)
                    _, standalone = play(self.scenes[P + 'woken.first_meat'], {P + 'counted_after_the_abyss'} if count.endswith('_late') else set(), choices={'law': allocation, home: allocation + 1})
                    for visited, prefix in ((folded, 'first_meat.'), (standalone, '')):
                        self.assertIn(prefix + home, visited)
                        self.assertNotIn(prefix + ('home' if home == 'home_late' else 'home_late'), visited)
                        expected = prefix + ('home_gate' if allocation == 0 else 'home_table')
                        wrong = prefix + ('home_table' if allocation == 0 else 'home_gate')
                        if count.endswith('_late'):
                            expected += '_late'
                            wrong += '_late'
                        self.assertIn(expected, visited)
                        self.assertNotIn(wrong, visited)

    def test_home_allocation_choices_in_every_copy(self):
        for scene_id in ('woken.first_meat', 'woken.count', 'woken.count_late'):
            nodes = {n['Id']: n for n in self.scenes[P + scene_id]['Nodes']}
            prefix = '' if scene_id == 'woken.first_meat' else 'first_meat.'
            for suffix in ('', '_late'):
                home = nodes[prefix + 'home' + suffix]
                self.assertEqual([None, prefix + 'home_gate' + suffix, prefix + 'home_table' + suffix], [a['Next'] for a in home['Choices']])
                for flags, target in ((set(), None), ({P + 'meat.gate'}, prefix + 'home_gate' + suffix), ({P + 'meat.table'}, prefix + 'home_table' + suffix)):
                    available = [a for a in home['Choices'] if matches(a, flags)]
                    self.assertEqual([target], [a['Next'] for a in available])
                    self.assertTrue(all((not a['Abort'] for a in available)))
                    if target:
                        self.assertTrue(all((a['Next'] is None for a in nodes[target]['Choices'])))

    def test_brace_after_waking_and_commitment_with_or_without_kyado(self):
        for dead in (False, True):
            with self.subTest(dead=dead):
                flags = self.derive({'trickster', 'trickster.ever', 'delamere.tomb_visited', 'delamere.tomb_book_locked_opened', *({'kyado.dead'} if dead else set())})
                waking = self.scenes[P + ('crypt.stag_alone' if dead else 'crypt.stag')]
                state = SimState(3, 5000)
                state.flags.update(flags)
                self.assertTrue(sim_available(self.model, waking, state))
                before = set(flags)
                flags, _ = play(waking, flags)
                state.times.update({flag: state.hour for flag in flags - before})
                for scene in ('woken.count', 'woken.feasting_table', 'woken.red_blood', 'woods.second_hunt_page' if dead else 'woods.second_hunt'):
                    flags = self.derive(flags)
                    state.flags = flags.copy()
                    state.hour += 200
                    self.assertTrue(sim_available(self.model, self.scenes[P + scene], state), scene)
                    before = set(flags)
                    flags, _ = play(self.scenes[P + scene], flags)
                    state.times.update({flag: state.hour for flag in flags - before})
                self.assertIn('delamere.committed', flags)
                hide = self.scenes[P + 'woken.hide']
                state.flags = self.derive(flags)
                state.hour += 200
                self.assertTrue(sim_available(self.model, hide, state))
                _, visited = play(hide, flags, choices={'what': 2 if dead else 0})
                self.assertIn('made_alone' if dead else 'made', visited)
                self.assertEqual('made' in visited, not dead)
                if dead:
                    self.assertIn('made_alone', visited)
                    what = next((n for n in hide['Nodes'] if n['Id'] == 'what'))
                    ordered_answer_1, *ordered_answer_1_rest = what['Choices']
                    self.assertFalse(matches(ordered_answer_1, flags))
                    *answer_in_order_1_preceding, answer_in_order_1 = what['Choices']
                    self.assertEqual(answer_in_order_1['Next'], 'made_alone')

    def test_failed_poacher_bluff_returns_to_both_judgments(self):
        scene = self.scenes[P + 'woken.poachers']
        for judgment, outcome in ((0, 'provost'), (1, 'her_law')):
            with self.subTest(judgment=judgment):
                flags, visited = play(scene, {P + 'village.given'}, choices={'law': 2, 'law_again': judgment}, checks={'CheckBluff': 'Failure'})
                self.assertIn('bluff_fail', visited)
                self.assertIn('law_again', visited)
                self.assertNotIn('bluffed', visited)
                self.assertIn(P + 'poachers.' + outcome, flags)
                self.assertNotIn(P + 'poachers.tricked', flags)

    def test_immediate_refusal_from_every_waking(self):
        for waking in ('crypt.stag', 'crypt.stag_alone', 'crypt.stag_late', 'drezen.stag'):
            for mobility in ('Success', 'Failure'):
                with self.subTest(waking=waking, mobility=mobility):
                    scene = self.scenes[P + waking]
                    flags, _ = play(scene, {'delamere.tomb_opened'}, choices={'lady': 2}, mobility=mobility)
                    self.assertIn('delamere.closed', flags)
                    self.assertNotIn(P + 'returned', flags)
                    self.assertEqual(P + 'woke_in_drezen' in flags, waking == 'drezen.stag')
                    for ending in ('never', 'never_sacrifice'):
                        node = self.scenes[P + 'epilogue.' + ending]['Nodes'][0]
                        slots = visible_slots(node, flags)
                        self.assertEqual(node['Id'] + '/paragraph/1' in slots, waking == 'drezen.stag')
                        self.assertEqual(node['Id'] + '/paragraph/0' in slots, waking != 'drezen.stag')
                    for node in scene['Nodes']:
                        if node['Id'] in ('lift', 'fumble'):
                            self.assertTrue(all((P + 'woke_in_drezen' not in c['Set'] for c in node['Choices'])))
if __name__ == '__main__':
    unittest.main()
