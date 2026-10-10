"""Route-local regression contracts for the round-two situations."""
import json
from pathlib import Path
import unittest
from storylines import areelu_afterlogue as after
from storylines import areelu_trickster as route
from tools.slot_brief_lint import first_beat

class AreeluRoundTwoTests(unittest.TestCase):

    def setUp(self):
        self.scenes = {s['Id']: s for s in route.SCENES}

    def test_wager_is_not_acceptance(self):
        self.assertEqual(route.COMMITTED_ANY, [route.COMMITTED])
        self.assertEqual(after.COMMITS, [[route.COMMITTED]])
        for s in self.scenes.values():
            if '.report.' in s['Id'] and (not s['Id'].endswith('afterword')):
                self.assertIn(route.COMMITTED, s['Requires'], s['Id'])
        self.assertIn(route.DRAWN, self.scenes['areelu.trickster.wager.raised']['Forbids'])

    def test_fate_accounts_require_their_actual_device(self):
        bottle = self.scenes['areelu.trickster.finale.lien_bottled']
        self.assertIn('lastcall.h2', bottle['Requires'])
        self.assertIn('iomedae.trickster.rescued', bottle['Forbids'])
        bridge = self.scenes['areelu.trickster.finale.not_burned']
        self.assertIn(['iomedae.appointment_kept', 'iomedae.trickster.rescued'], bridge['RequiresAnyGroups'])
        self.assertIn('lastcall.h1', self.scenes['areelu.trickster.report.wound']['Forbids'])
        for worlds in [after.REWRITTEN, after.SPARED, after.RETURN_WORLDS]:
            for world in worlds:
                self.assertIn('trickster.now', world)

    def test_slots_are_append_only_choices_with_coherent_defaults(self):
        briefs = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/areelu-vorlesh'
        self.assertEqual(len(list(briefs.glob('*.json'))), 8)
        for file in briefs.glob('*.json'):
            brief = json.loads(file.read_text(encoding='utf-8'))
            slot = brief['slot_id']
            scene = self.scenes[slot.rsplit('.explicit.', 1)[0]]
            nodes = {n['Id']: n for n in scene['Nodes']}
            ordered_answer_1, *ordered_answer_1_rest = nodes[slot]['Choices']
            following = nodes[ordered_answer_1['Next']]
            ordered_answer_2, *ordered_answer_2_rest = nodes[slot]['Choices']
            self.assertIn(ordered_answer_2['Next'], nodes)
            ordered_answer_3, *ordered_answer_3_rest = nodes[slot]['Choices']
            self.assertFalse(ordered_answer_3['Set'])
            self.assertTrue(any((c['Next'] == slot for n in nodes.values() for c in n['Choices'])))

    def test_company_never_resolves_or_extracts_the_child(self):
        company = self.scenes['areelu.trickster.finale.company']
        self.assertIn(route.BURNED, company['Forbids'])
        self.assertIn(route.ASCENDED, company['Forbids'])
        for node in company['Nodes']:
            for answer in node['Choices']:
                self.assertFalse(answer['Set'])
        for name in ['answer', 'unexamined', 'intent']:
            node = next((n for n in company['Nodes'] if n['Id'] == name))
            self.assertTrue(any((c['Next'] == 'stopped' for c in node['Choices'])))

    def test_native_observation_reader_schemas(self):
        payload = {'Scenes': []}
        route.integrate(payload)
        self.assertEqual(payload['StartedDialogs'][route.P + 'cell_visited'], '246a775cece781740be00eed028086cf')
        self.assertEqual(payload['SeenCues'][route.P + 'promise_heard'], ['52830ee630aa6ee4dbe8e187367454d5'])

    def test_native_afterlogue_preserves_judgment_and_separation(self):
        replacements = []
        for edit in after.NATIVE_EPILOGUE_EDITS.values():
            self.assertEqual(edit['Parent'], after.PARENT)
            self.assertEqual(edit['Dialog'], after.DIALOG)
            self.assertFalse(edit['KeepNativeImage'])
            replacements.extend((v['Replacement'] for v in [edit, *edit['Variants']]))
        self.assertEqual(len(replacements), len(set(replacements)), 'The runtime requires each replacement scene to be used once')
if __name__ == '__main__':
    unittest.main()
