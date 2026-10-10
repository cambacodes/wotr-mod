"""Letter delivery classifications and mutations through departure_lint.check."""
import copy
import unittest
from tools import departure_lint
from tests.story_fixture import fresh_story
ARRIVALS = ('konomi.trickster.dismissed.arrival', 'konomi.trickster.never_arrived.arrival')
PAGES = (('nocticula', 'noct.acq.epilogue.correspondence'), ('melazmera', 'melazmera.trickster.epilogue.left_free'))
RULE = 'letter surface must be remote or an epilogue page'

def delivery_fixture(scene, surface):
    """A complete, independently specified one-woman availability contract."""
    scene = copy.deepcopy(scene)
    woman = 'canary'
    scene['Relationship'] = woman
    scene['Requires'] = [woman + '.reachable_by_letter']
    contract = {'relationship': woman, 'losses': [], 'overrides': {}, 'returns': [], 'surfaces': [dict(scene=scene['Id'], letter=True, **surface)], 'absence_variants': [], 'presences': [], 'guests': []}
    story = {'Scenes': [scene], 'Relationships': {woman: {'EpochUnavailableFlags': [woman + '.epoch_unavailable']}}, 'DepartureEpochs': {woman: {'Losses': [], 'Overrides': {}, 'Returns': [], 'NativeClearReturns': {}}}, 'Derived': {woman + '.present_now': [['availability.observed']], woman + '.reachable_by_letter': [[woman + '.present_now']]}, 'DerivedForbids': {woman + '.present_now': [woman + '.epoch_unavailable']}}
    return (story, {'women': {woman: contract}})

class CanaryLettersTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.scenes = {scene['Id']: scene for scene in fresh_story()['Scenes']}

    def test_arrival_reports_require_current_body_gate(self):
        surfaces = {s['scene']: s for s in departure_lint.contracts()['women']['konomi']['surfaces']}
        for sid in ARRIVALS:
            with self.subTest(scene=sid):
                self.assertFalse(surfaces[sid]['letter'])
                self.assertFalse(self.scenes[sid].get('Remote'))
                self.assertIn('konomi.present_now', self.scenes[sid]['Requires'])
                story, data = delivery_fixture(self.scenes[sid], {})
                self.assertEqual([f'canary/{sid}: {RULE}'], departure_lint.check(story, data))

    def test_mixed_correspondence_page_requires_nocticula_body(self):
        sid = 'noct.acq.epilogue.correspondence'
        surface = next((s for s in departure_lint.contracts()['women']['nocticula']['surfaces'] if s['scene'] == sid))
        self.assertFalse(surface['letter'])
        self.assertIn('nocticula.present_now', self.scenes[sid]['Requires'])
        self.assertNotIn('nocticula.reachable_by_letter', self.scenes[sid]['Requires'])

    def test_remote_letter_and_both_epilogue_owner_forms(self):
        cases = [self.scenes[sid] for _, sid in PAGES]
        remote = copy.deepcopy(self.scenes[ARRIVALS[0]])
        remote['Remote'] = True
        cases.append(remote)
        for scene in cases:
            with self.subTest(scene=scene['Id'], owner=scene['Owner']):
                story, data = delivery_fixture(scene, {})
                self.assertEqual([], departure_lint.check(story, data))
                story['Scenes'][0]['Remote'] = False
                story['Scenes'][0]['Owner'] = 'Konomi'
                self.assertEqual([f"canary/{scene['Id']}: {RULE}"], departure_lint.check(story, data))

    def test_melazmera_historical_payment_paragraph_keeps_letter_gate(self):
        sid = 'melazmera.trickster.epilogue.left_free'
        surface = next((s for s in departure_lint.contracts()['women']['melazmera']['surfaces'] if s['scene'] == sid))
        self.assertTrue(surface['letter'])
        self.assertEqual(('page', 2), (surface['node'], surface['paragraph']))
        paragraph = next((p for n in self.scenes[sid]['Nodes'] for p in n.get('Paragraphs', ()) if 'melazmera.reachable_by_letter' in p.get('Requires', ())))
        self.assertIn('melazmera.reachable_by_letter', paragraph['Requires'])

    def test_nested_letter_surfaces_cannot_bypass_delivery_rule(self):
        for field, blocks in (('paragraph', 'Paragraphs'), ('choice', 'Choices')):
            with self.subTest(surface=field):
                scene = copy.deepcopy(self.scenes[ARRIVALS[0]])
                scene['Remote'] = True
                node = scene['Nodes'][0]
                node[blocks] = [{'Requires': ['canary.reachable_by_letter']}]
                story, data = delivery_fixture(scene, {'node': node['Id'], field: 0})
                self.assertEqual([], departure_lint.check(story, data))
                story['Scenes'][0]['Remote'] = False
                self.assertEqual([f"canary/{scene['Id']}: {RULE}"], departure_lint.check(story, data))

    def test_ember_report_is_not_a_remote_chadali_scene(self):
        scene = self.scenes['chadali.trickster.react.ember_penny']
        self.assertEqual('Ember', scene['Owner'])
        self.assertEqual('Ember', scene['Nodes'][0]['Speaker'])
        story, data = delivery_fixture(scene, {})
        self.assertEqual([f"canary/{scene['Id']}: {RULE}"], departure_lint.check(story, data))
        story['Scenes'][0]['Remote'] = True
        self.assertEqual([], departure_lint.check(story, data))
if __name__ == '__main__':
    unittest.main()
