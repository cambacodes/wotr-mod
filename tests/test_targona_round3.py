"""Round-three arrival memories follow the paid acquisition branch."""
import unittest
from itertools import product

from tests.story_fixture import fresh_story
from tools.crossroute_checks.common import Proof, fields, lit, verify


class TargonaRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}
        cls.proof = Proof(verify.Model(cls.story))

    def test_arrival_recalls_each_cost_in_each_correspondence_order(self):
        scene = self.scenes['targona.trickster.free.furlough']
        nodes = {n['Id']: n for n in scene['Nodes']}
        charge = 'targona.trickster.cost.charges_spent'
        for ordinary in ('greet', 'greet_treated', 'greet_wayhouse'):
            unspent = ordinary + '_unspent'
            for target, spent in ((ordinary, True), (unspent, False)):
                answers = [c for c in nodes['start']['Choices'] if c['Next'] == target]
                self.assertEqual(1, len(answers))
                self.assertTrue(self.proof.implies(fields(answers[0]), lit(charge, spent)))
                self.assertEqual('why', nodes[target]['Choices'][0]['Next'])
                self.assertEqual([], nodes[target]['Choices'][0]['Set'])
            self.assertIn('supplied' if ordinary != 'greet' else 'buying supplies',
                          nodes[ordinary]['Text'])
            self.assertIn('worked his last healing wand through the night', nodes[unspent]['Text'])
            self.assertNotIn('still had light', nodes[unspent]['Text'])
            self.assertTrue(nodes[unspent]['Text'].startswith('"Commander.'))
            self.assertNotIn('get supplies', nodes[unspent]['Choices'][0]['Text'])
        self.assertIn('my physician', nodes['greet_treated_unspent']['Text'])
        self.assertIn('letter found me at the wayhouse', nodes['greet_wayhouse_unspent']['Text'])

    def test_lariel_condition_is_prepared_before_either_postponement(self):
        ward = self.scenes['targona.trickster.after.ward']
        start = next(n for n in ward['Nodes'] if n['Id'] == 'start')
        self.assertIn('not another healing wand', start['Text'])
        self.assertIn('beg him for a life', start['Text'])
        quiet = self.scenes['targona.trickster.after.quiet_ward']
        asking = next(n for n in quiet['Nodes'] if n['Id'] == 'start')
        self.assertIn("at the sergeant's cot", asking['Text'])
        self.assertIn('targona.trickster.cost.light_sealed', asking['Choices'][0]['Set'])

    def test_arrival_keeps_one_selectable_greeting_in_every_history(self):
        scene = self.scenes['targona.trickster.free.furlough']
        answers = next(n for n in scene['Nodes'] if n['Id'] == 'start')['Choices']
        flags = ('targona.trickster.told_in_lab', 'targona.trickster.cost.her_sleep',
                 'targona.ran_treatment_completed', 'targona.trickster.cost.charges_spent',
                 'targona.correspondence_opened')
        for values in product((False, True), repeat=len(flags)):
            history = {flag for flag, value in zip(flags, values) if value}
            selected = [c for c in answers if set(c['Requires']) <= history
                        and not set(c['Forbids']) & history]
            with self.subTest(history=sorted(history)):
                self.assertEqual(1, len(selected))


if __name__ == '__main__':
    unittest.main()
