"""Current exported hosting and book custody across saved placement histories."""
import unittest

from tests.story_fixture import fresh_story



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

class BoundDraftTests(unittest.TestCase):
    def test_default_excludes_the_retained_draft_ending_account(self):
        from storylines import nenio_trickster as route
        retained = [p for p in route.KEPT_PARAS if p['Requires'] == [route.MANUSCRIPT]]
        self.assertIsNotNone(only(retained))
        self.assertIn(route.DEBT_DEFAULTED, by_contract(retained, [{'Requires': ['nenio.trickster.cost.manuscript_surrendered'], 'Forbids': ['nenio.trickster.debt.defaulted'], 'AnyGroups': []}])['Forbids'])


class Structure03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def dispatch(self, scene, node_id, flags):
        node = next(n for n in scene['Nodes'] if n['Id'] == node_id)
        choices = [a for a in node['Choices']
                   if set(a['Requires']) <= flags and not set(a['Forbids']) & flags]
        self.assertIsNotNone(only(choices))
        return by_contract(choices, [{'Next': 'default_after', 'Requires': [], 'Forbids': ['nenio.folio.volume_one.entrusted', 'nenio.folio.volume_one.entrusted', 'nenio.folio.volume_one.entrusted'], 'Set': [], 'Abort': False}, {'Next': 'default_after_commander', 'Requires': ['nenio.folio.volume_one.entrusted'], 'Forbids': [], 'Set': [], 'Abort': False}, {'Next': 'give', 'Requires': [], 'Forbids': ['nenio.trickster.debt.defaulted'], 'Set': [], 'Abort': False}, {'Next': 'give_new', 'Requires': ['nenio.trickster.debt.defaulted'], 'Forbids': [], 'Set': [], 'Abort': False}])['Next']

    def test_book_custody_across_both_orders_and_all_placement_twins(self):
        custody = 'nenio.folio.volume_one.entrusted'
        groups = self.story['Derived'][custody]
        # Independently enumerate the saved scene receipts: a completed gift
        # in ANY placement must redirect a later default in EVERY placement.
        gifts = ['nenio.folio.volume_one' + s for s in ('', '_visitor', '_arcade')]
        for suffix in ('', '_visitor', '_arcade'):
            debt = self.scenes['nenio.trickster.debt.collected' + suffix]
            self.assertEqual(self.dispatch(debt, 'default', set()), 'default_after')
            for gift in gifts:
                flags = {gift}
                if any(set(g) <= flags for g in groups):
                    flags.add(custody)
                self.assertEqual(self.dispatch(debt, 'default', flags), 'default_after_commander')
            nodes = {n['Id']: n for n in debt['Nodes']}
            self.assertEqual(by_contract(nodes['default']['Choices'], [{'Next': 'default_after', 'Requires': [], 'Forbids': ['nenio.folio.volume_one.entrusted', 'nenio.folio.volume_one.entrusted', 'nenio.folio.volume_one.entrusted'], 'Set': [], 'Abort': False}])['Next'], 'default_after')
            for nid in ('default_after', 'default_after_commander'):
                self.assertEqual(by_contract(nodes[nid]['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['nenio.trickster.debt.defaulted'], 'Abort': False}])['Set'], ['nenio.trickster.debt.defaulted'])
            gift_scene = self.scenes['nenio.folio.volume_one' + suffix]
            self.assertEqual(self.dispatch(gift_scene, 'open', set()), 'give')
            self.assertEqual(self.dispatch(gift_scene, 'open', {'nenio.trickster.debt.defaulted'}), 'give_new')

    def test_wintersun_host_family_and_followup_delivery(self):
        for sid in ('threshold', 'one_account', 'watch_line', 'the_thing_in_the_sack',
                    'the_inherited_debt', 'a_voice_in_the_dark', 'the_unwelcome_path',
                    'when_the_road_returns', 'a_track_with_two_ends', 'where_the_steps_end'):
            scene = self.scenes['soana.' + sid]
            self.assertEqual(scene['Areas'], ['0a5654e7dc18f074d9356009d55eb51b'])
            self.assertFalse(scene.get('Remote'))
            self.assertNotIn('Kind', scene)
            self.assertEqual(scene['ContactUnit'], '64805abb52739e44280a758f850b300c')
            self.assertIn('soana.present_now', scene['Requires'])

    def test_second_watch_has_a_physical_nexus_entry(self):
        scene = self.scenes['soana.past_the_firelight']
        self.assertFalse(scene.get('Remote'))
        self.assertNotIn('Kind', scene)
        self.assertEqual(scene['Areas'], ['7847c3e3537104f4694167af0b9fcd0e'])
        self.assertEqual(scene['AnswerLists'], ['88cfebc7c46549aba284036a26e9eade'])
        self.assertEqual(scene['ContactUnit'], 'da4c28dd01413694f82b08b728a8c6e5')
        self.assertEqual('start', scene['Nodes'][0]['Id'])
        self.assertEqual(scene['Chapters'], [4])
        self.assertNotIn('soana.present_now', scene['Requires'])


if __name__ == '__main__':
    unittest.main()
