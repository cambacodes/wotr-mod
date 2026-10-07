"""Harem insertion briefs retain the reviewed participant scope."""
import json
from pathlib import Path
import unittest


class HaremExplicitScope(unittest.TestCase):
    def test_woman_pairs_have_no_absent_commander_participant(self):
        root = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/harem'
        briefs = sorted(root.rglob('*.json'))
        self.assertTrue(briefs)
        women = {'Camellia', 'Arueshalae', 'fallen Arueshalae', 'Wenduag',
                 'Shamira', 'Jerribeth', 'Vellexia', 'Seelah', 'Nocticula'}
        for path in briefs:
            brief = json.loads(path.read_text(encoding='utf-8'))
            participants = brief.get('participants', list(brief.get('speakers', {}).values()))
            participants = [name for name in participants if name != 'Narrator']
            with self.subTest(slot=path.name):
                self.assertEqual(len(participants), 2)
                self.assertTrue(set(participants) <= women)
                self.assertIn(brief.get('commander', 'absent'), ('absent',))
                self.assertFalse(brief.get('commander_variants'))
