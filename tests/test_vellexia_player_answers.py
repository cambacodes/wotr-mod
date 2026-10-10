"""VEL-A4-003 exchanges survive prose transforms and retain saved exits."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from storylines import vellexia_campaign, vellexia_cloud, vellexia_opening, vellexia_trickster

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'unfinished_likeness': {'start': 1, 'terms': 3},
    'second_painter': {'start': 2, 'ask': 3},
    'two_observers': {'question': 2},
    'unadvertised_hour': {'intent': 2},
    'a_question_kept': {'result': 2},
    'the_price_of_tomorrow': {'offer': 2},
    'the_cover_before_the_battle': {'start': 2, 'lovers': 1},
}


class VellexiaPlayerAnswersTests(unittest.TestCase):
    def setUp(self):
        self.before = {'Scenes': copy.deepcopy(
            vellexia_opening.SCENES + vellexia_campaign.SCENES + vellexia_trickster.SCENES)}
        self.after = copy.deepcopy(self.before)
        with patch.object(vellexia_cloud, '_player_answer_exchanges'):
            vellexia_cloud.integrate(self.before)
        vellexia_cloud.integrate(self.after)
        self.old = {s['Id']: s for s in self.before['Scenes']}
        self.new = {s['Id']: s for s in self.after['Scenes']}

    def test_saved_nodes_and_choices_are_retained_without_changes(self):
        def mechanics(value):
            if isinstance(value, dict):
                return {k: mechanics(v) for k, v in value.items() if k not in {'Text', 'Entry', 'Description'}}
            if isinstance(value, list):
                return [mechanics(v) for v in value]
            return value
        for sid, scene in self.old.items():
            nodes = {n['Id']: n for n in self.new[sid]['Nodes']}
            for old in scene['Nodes']:
                new = nodes[old['Id']]
                old_choices = mechanics(old.get('Choices', []))
                current = iter(mechanics(new.get('Choices', [])))
                self.assertEqual(old_choices, [next(current, None) for _ in old_choices])
                for field in old.keys() - {'Text', 'Choices'}:
                    self.assertEqual(mechanics(old[field]), mechanics(new[field]))
                suffix = sid.removeprefix('vellexia.')
                if old['Id'] not in EXPECTED.get(suffix, {}):
                    self.assertEqual(mechanics(old), mechanics(new))

    def test_appended_exchanges_end_at_the_original_exits(self):
        def mechanics(answers):
            return [{k: v for k, v in a.items() if k != 'Text'} for a in answers]
        for suffix, hosts in EXPECTED.items():
            sid = 'vellexia.' + suffix
            nodes = {n['Id']: n for n in self.new[sid]['Nodes']}
            old_nodes = {n['Id']: n for n in self.old[sid]['Nodes']}
            for host, count in hosts.items():
                with self.subTest(scene=sid, node=host):
                    current = nodes[host]
                    for index in range(1, count + 1):
                        target = f'{host}_commander_reply_{index}'
                        answer, = (a for a in current['Choices'] if a['Next'] == target)
                        self.assertFalse(answer['Set'] or answer['Requires'] or answer['Forbids'] or answer['Abort'])
                        current = nodes[target]
                        self.assertEqual(target, current['Id'])
                    self.assertEqual(mechanics(old_nodes[host]['Choices']), mechanics(current['Choices']))

    def test_restored_exchanges_leave_no_placeholder_or_queue_entry(self):
        pending = json.loads((ROOT / 'tools/route_packs/plans/prose-pending.json').read_text(encoding='utf-8'))
        queue = json.loads((ROOT / 'tools/route_packs/plans/claude-work-queue.json').read_text(encoding='utf-8'))
        self.assertFalse([p for p in pending['pending'] if p['scene'].startswith('vellexia.')])
        self.assertFalse([r for r in queue if r.get('finding') == 'VEL-A4-003'])
        from tools.prose_pending_lint import check
        scoped_pending = dict(pending, pending=[p for p in pending['pending'] if p['scene'].startswith('vellexia.')])
        self.assertEqual([], check(self.after, scoped_pending, integration=True))

    def test_stale_prose_binding_fails_instead_of_dropping_speech(self):
        payload = copy.deepcopy(self.before)
        scene = next(s for s in payload['Scenes'] if s['Id'] == 'vellexia.unfinished_likeness')
        node = next(n for n in scene['Nodes'] if n['Id'] == 'start')
        node['Text'] = node['Text'].replace('"Have you looked?"', '')
        with self.assertRaisesRegex(ValueError, 'missing embedded answer'):
            vellexia_cloud._player_answer_exchanges({s['Id']: s for s in payload['Scenes']})


if __name__ == '__main__':
    unittest.main()
