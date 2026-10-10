"""Harem insertion briefs retain the reviewed participant scope."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch


class HaremExplicitScope(unittest.TestCase):
    def test_woman_pairs_have_no_absent_commander_participant(self):
        root = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/harem'
        briefs = sorted(root.rglob('*.json'))
        self.assertTrue(briefs)
        women = {'camellia', 'arueshalae', 'fallen_arueshalae', 'wenduag',
                 'shamira', 'jerribeth', 'vellexia', 'seelah', 'nocticula'}
        for path in briefs:
            brief = json.loads(path.read_text(encoding='utf-8'))
            participants = brief.get('participants', list(brief.get('speakers', {}).values()))
            participants = [name.lower().replace(' ', '_') for name in participants if name != 'Narrator']
            with self.subTest(slot=path.name):
                self.assertEqual(len(participants), 2)
                self.assertFalse(set(participants) - women)
                self.assertIn(brief.get('commander', 'absent'), ('absent',))
                self.assertFalse(brief.get('commander_variants'))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        read_text = Path.read_text
        def altered(path, *args, **kwargs):
            raw = read_text(path, *args, **kwargs)
            if 'explicit_slots/harem/' in path.as_posix():
                brief = json.loads(raw)
                brief['participants'] = ['Commander', 'Seelah']
                return json.dumps(brief)
            return raw
        with patch.object(Path, 'read_text', altered):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_woman_pairs_have_no_absent_commander_participant()
