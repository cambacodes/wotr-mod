"""Round-three arrival memories follow the paid acquisition branch."""
import unittest
from itertools import product

from tests.story_fixture import fresh_story
from tools.crossroute_checks.common import Proof, fields, lit, verify



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

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
                self.assertIsNotNone(only(answers))
                self.assertTrue(self.proof.implies(fields(by_contract(answers, [{'Next': 'greet', 'Requires': ['targona.trickster.cost.charges_spent'], 'Forbids': ['targona.trickster.told_in_lab', 'targona.ran_treatment_completed'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': 'greet_unspent', 'Requires': [], 'Forbids': ['targona.trickster.told_in_lab', 'targona.ran_treatment_completed', 'targona.trickster.cost.charges_spent'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': 'greet_treated', 'Requires': ['targona.ran_treatment_completed', 'targona.trickster.cost.charges_spent'], 'Forbids': ['targona.correspondence_opened'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': 'greet_treated_unspent', 'Requires': ['targona.ran_treatment_completed'], 'Forbids': ['targona.correspondence_opened', 'targona.trickster.cost.charges_spent'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])), lit(charge, spent)))
                self.assertEqual('why', only(nodes[target]['Choices'])['Next'])
                self.assertEqual([], only(nodes[target]['Choices'])['Set'])

    def test_lariel_condition_is_prepared_before_either_postponement(self):
        ward = self.scenes['targona.trickster.after.ward']
        quiet = self.scenes['targona.trickster.after.quiet_ward']
        self.assertIn('targona.trickster.declined', ward['Forbids'])
        self.assertIn('targona.trickster.declined', quiet['Requires'])
        asking = next(n for n in quiet['Nodes'] if n['Id'] == 'start')
        accepted = next(c for c in asking['Choices'] if not c['Abort'] and 'targona.committed' in c['Set'])
        self.assertIn('targona.trickster.cost.light_sealed', accepted['Set'])

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
                self.assertIsNotNone(only(selected))


if __name__ == '__main__':
    unittest.main()
