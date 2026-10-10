"""Generated historical receipts and physical continuity for the r3 audit."""
import json
from pathlib import Path
import unittest
from storylines import nenio_trickster as route

class NenioRound3Tests(unittest.TestCase):

    def test_all_night_slots_continue_from_the_existing_position(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = next((s for s in route.SCENES if s['Id'] == route.P + 'night' + suffix))
            nodes = {n['Id']: n for n in scene['Nodes']}
            slot = nodes[scene['Id'] + '.explicit.1']
            ordered_answer_1, *_ = nodes['lose']['Choices']
            self.assertEqual(ordered_answer_1['Next'], 'watch')

    def test_late_slot_has_a_real_destination_and_past_narration_brief(self):
        scene = next((s for s in route.SCENES if s['Id'] == route.P + 'epilogue.commit'))
        nodes = {n['Id']: n for n in scene['Nodes']}
        page = nodes['page']
        slot_id = scene['Id'] + '.explicit.1'
        ordered_answer_2, *_ = page['Choices']
        self.assertEqual(ordered_answer_2['Id'], 'continue')
        for key in ('Next', 'Set', 'Requires', 'Forbids', 'Abort'):
            ordered_answer_3, *_ = page['Choices']
            self.assertFalse(ordered_answer_3.get(key))
        _, ordered_answer_4, *_ = page['Choices']
        self.assertEqual(ordered_answer_4['Next'], slot_id)
        ordered_answer_5, *_ = nodes[slot_id]['Choices']
        self.assertEqual(ordered_answer_5['Next'], 'morning_after')
        brief = json.loads(Path('tools/route_packs/explicit_slots/nenio', slot_id + '.json').read_text(encoding='utf-8'))
        self.assertEqual(brief['narration'], 'third-past')
if __name__ == '__main__':
    unittest.main()
