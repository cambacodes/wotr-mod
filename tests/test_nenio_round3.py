"""Generated historical receipts and physical continuity for the r3 audit."""
import json
from pathlib import Path
import unittest

from storylines import nenio_trickster as route


class NenioRound3Tests(unittest.TestCase):
    def test_all_night_slots_continue_from_the_existing_position(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = next(s for s in route.SCENES if s['Id'] == route.P + 'night' + suffix)
            nodes = {n['Id']: n for n in scene['Nodes']}
            slot = nodes[scene['Id'] + '.explicit.1']
            self.assertEqual(nodes['lose']['Choices'][0]['Next'], 'watch')
            self.assertNotIn('pulls you down', slot['Text'])
            self.assertNotIn('reaches for it', slot['Text'])

    def test_late_slot_has_a_real_destination_and_past_narration_brief(self):
        scene = next(s for s in route.SCENES if s['Id'] == route.P + 'epilogue.commit')
        nodes = {n['Id']: n for n in scene['Nodes']}
        page = nodes['page']
        slot_id = scene['Id'] + '.explicit.1'
        self.assertEqual(page['Choices'][0]['Id'], 'continue')
        for key in ('Next', 'Set', 'Requires', 'Forbids', 'Abort'):
            self.assertFalse(page['Choices'][0].get(key))
        self.assertEqual(page['Choices'][1]['Next'], slot_id)
        self.assertEqual(nodes[slot_id]['Choices'][0]['Next'], 'morning_after')
        self.assertIn('sat on the bed', nodes[slot_id]['Text'])
        self.assertIn('In the morning', nodes['morning_after']['Text'])
        brief = json.loads(Path('tools/route_packs/explicit_slots/nenio', slot_id + '.json').read_text(encoding='utf-8'))
        self.assertEqual(brief['narration'], 'third-past')
        self.assertEqual(brief['default_text'], nodes[slot_id]['Text'])


if __name__ == '__main__':
    unittest.main()
