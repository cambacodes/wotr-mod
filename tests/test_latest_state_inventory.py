"""E-Q8-01 strict-inventory mutations, independent of the ordered C# histories."""
from tests.story_fixture import fresh_story
import copy
import unittest
import expansion
from tools import return_provenance_lint as lint

class LatestStateInventoryTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.data = lint.latest_contracts()

    def test_shipped_inventory(self):
        self.assertEqual([], lint.check_latest_state(self.story))

    def test_each_native_loss_override_and_ending_guard_is_enforced(self):
        n = self.data['nenio']
        for loss in n['overrides']:
            with self.subTest(loss=loss):
                story = copy.deepcopy(self.story)
                story['Relationships']['nenio']['UnavailableOverrides'][loss] = 'nenio.trickster.returned'
                self.assertTrue(lint.check_latest_state(story))
        for sid in n['consumers']:
            if 'epilogue' not in sid:
                continue
            for guard in (n['runtime_loss'], 'nenio.dead'):
                with self.subTest(scene=sid, guard=guard):
                    story = copy.deepcopy(self.story)
                    scene = next(s for s in story['Scenes'] if s['Id'] == sid)
                    scene['Forbids'].remove(guard)
                    self.assertTrue(lint.check_latest_state(story))

    def test_presence_stale_return_and_guest_route_guard_are_enforced(self):
        story = copy.deepcopy(self.story)
        key = 'nenio.presence.route_open.blocked.nenio.dead'
        story['DerivedForbids'][key] = ['nenio.trickster.returned']
        self.assertTrue(lint.check_latest_state(story))
        story = copy.deepcopy(self.story)
        guest = next(e for b in story['Books'].values() for e in b['Entries'] if e['Id'] == 'guest.nenio')
        guest['Requires'] = ['nenio.committed']
        self.assertTrue(lint.check_latest_state(story))

    def test_paid_restore_and_one_shot_retirement_are_enforced(self):
        n = self.data['nenio']
        for mutation in ('action', 'retirement'):
            story = copy.deepcopy(self.story)
            scene = next(s for s in story['Scenes'] if s['Id'] == n['producer'])
            if mutation == 'action':
                node = next(x for x in scene['Nodes'] if x['Id'] == n['producer_node'])
                node['Choices'][n['producer_choice']]['Revive'] = None
            else:
                scene['Forbids'].remove('nenio.trickster.returned')
            self.assertTrue(lint.check_latest_state(story))

    def test_every_living_closure_and_romance_reader_is_enforced(self):
        w = self.data['wenduag']
        for key in w['romance_readers']:
            story = copy.deepcopy(self.story)
            story['DerivedForbids'][key].remove('wenduag.closed')
            self.assertTrue(lint.check_latest_state(story))
        for sid in (w['refusal'], w['departure']):
            story = copy.deepcopy(self.story)
            next(s for s in story['Scenes'] if s['Id'] == sid)['Requires'].remove('wenduag.life.available')
            self.assertTrue(lint.check_latest_state(story))
        story = copy.deepcopy(self.story)
        story['Derived'][w['life_return']] = [['wenduag.trickster.returned']]
        self.assertTrue(lint.check_latest_state(story))

    def test_departure_cannot_silently_lose_receipt_or_grant_return(self):
        p = self.data['wenduag']['departure_producer']
        for mutation in ('receipt', 'return'):
            story = copy.deepcopy(self.story)
            scene = next((s for s in story['Scenes'] if s['Id'] == p['scene']))
            node = next((x for x in scene['Nodes'] if x['Id'] == p['node']))
            choice = next((a for a in node['Choices'] if p['receipt'] in a['Set']))
            if mutation == 'receipt':
                choice['Set'].remove(p['receipt'])
            else:
                choice['Set'].append('wenduag.trickster.returned')
            self.assertTrue(lint.check_latest_state(story))

    def test_departure_lint_exception_requires_exact_closure_coproduction(self):
        p = self.data['wenduag']['departure_producer']
        scene = next((s for s in self.story['Scenes'] if s['Id'] == p['scene']))
        node = next((x for x in scene['Nodes'] if x['Id'] == p['node']))
        choice = copy.deepcopy(next((a for a in node['Choices'] if p['receipt'] in a['Set'])))
        args = ('wenduag', p['scene'], p['node'], p['choice'], choice, p['receipt'])
        self.assertTrue(lint.registered_closing_departure(*args))
        self.assertFalse(lint.registered_closing_departure('wenduag', p['scene'], 'other', p['choice'], choice, p['receipt']))
        self.assertFalse(lint.registered_closing_departure('wenduag', p['scene'], p['node'], p['choice'] + 1, choice, p['receipt']))
        choice['Set'].remove('wenduag.closed')
        self.assertFalse(lint.registered_closing_departure(*args))
if __name__ == '__main__':
    unittest.main()
