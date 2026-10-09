"""Production-export witnesses for struct2-05's owned structure changes."""
import hashlib
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story

ROOT = Path(__file__).resolve().parents[1]


def available(block, flags):
    return (all(flag in flags for flag in block.get('Requires', []))
            and not any(flag in flags for flag in block.get('Forbids', [])))


class Structure05Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.by = {s['Id']: s for s in fresh_story()['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.by[sid]['Nodes'] if n['Id'] == nid)

    def test_drezen_visits_use_native_hub_and_retain_clocks(self):
        for suffix, hours in [('woken.glory', 48), ('woken.jester', 48),
                              ('woken.demon', 48), ('woken.count', 24),
                              ('woken.count_late', 24), ('woken.first_meat', 24)]:
            scene = self.by['delamere.trickster.' + suffix]
            with self.subTest(scene=scene['Id']):
                self.assertFalse(scene.get('Remote', False))
                self.assertNotIn('Kind', scene)
                self.assertEqual(scene['Areas'], ['2570015799edf594daf2f076f2f975d8'])
                self.assertEqual(scene['AnswerLists'], ['1a17d8053a3be7f47a7908eb6706f2fe',
                                                       '6dccfd39947ef4242a8afbe36b21a46c'])
                self.assertEqual(scene['DelayHours'], hours)
                self.assertIn('delamere.closed', scene['Forbids'])
                self.assertNotIn('household.table.kept', scene['Requires'])
                history = set(scene['Requires'])
                self.assertTrue(available(scene, history))
                self.assertFalse(available(scene, history | {'delamere.closed'}))

    def test_prisoner_twins_are_heard_only_at_the_command_camp(self):
        for sid, hours, legend in [('longcon.prisoner_loud', 48, 'longcon.legend_loud'),
                                   ('longcon.prisoner_quiet', 168, 'longcon.legend_quiet')]:
            scene = self.by[sid]
            self.assertFalse(scene.get('Remote', False))
            self.assertNotIn('Kind', scene)
            self.assertEqual(scene['Areas'], ['7a25c101fe6f7aa46b192db13373d03b'])
            self.assertEqual(scene['AnswerLists'], ['871af36f2ab2b1f40b5de77976c54276'])
            self.assertEqual(scene['Chapters'], [2])
            self.assertEqual(scene['DelayHours'], hours)
            self.assertIn(legend, scene['Requires'])
            self.assertIn('longcon.kc_appointed', scene['Requires'])
            self.assertIn('longcon.prisoner_seen', scene['Forbids'])
            self.assertEqual(self.node(sid, 'plural' if sid.endswith('loud') else 'quiet')['Choices'][0]['Next'],
                             'hanged')

    def test_seelah_letter_and_followups_are_local_companion_interactions(self):
        for sid, prerequisite in [('seelah.letter', 'seelah.abyss_together'),
                                  ('seelah.letter_after', 'seelah.letter_unsettled'),
                                  ('seelah.letter_work', 'seelah.letter_discussed')]:
            scene = self.by[sid]
            with self.subTest(scene=sid):
                self.assertFalse(scene.get('Remote', False))
                self.assertNotIn('Kind', scene)
                self.assertEqual(scene['AnswerLists'], ['417fa384f3250634bb71859fbc913453'])
                self.assertEqual(scene['Areas'], ['7847c3e3537104f4694167af0b9fcd0e'])
                self.assertEqual(scene['Chapters'], [4])
                self.assertEqual(scene['DelayHours'], 24)
                self.assertIn(prerequisite, scene['Requires'])
        self.assertEqual([a['Next'] for a in self.node('seelah.letter', 'start')['Choices']],
                         ['stall', None])

    def test_courier_uses_returned_body_hub_and_keeps_optional_sister(self):
        scene = self.by['hepzamirah.trickster.body.hounds']
        self.assertEqual(scene['Owner'], 'Hepzamirah')
        self.assertFalse(scene.get('Remote', False))
        self.assertNotIn('Kind', scene)
        self.assertEqual(scene['ContactUnit'], 'bd2a925967b5f5f489f6da0b03236d03')
        self.assertEqual(scene['InteractionHub'], 'hepzamirah.presence')
        self.assertEqual(scene['Areas'], ['2570015799edf594daf2f076f2f975d8'])
        self.assertIn('hepzamirah.trickster.returned', scene['Requires'])
        self.assertNotIn('horzalah.trickster.returned', scene['Requires'])
        self.assertEqual(scene['DelayHours'], 48)

    def test_attack_success_failure_and_legacy_trophies_are_disjoint(self):
        prefix = 'hepzamirah.trickster.'
        market = prefix + 'flesh.the_market'
        room = prefix + 'bond.her_room'
        attack = set(self.node(market, 'hep')['Choices'][0]['Set'])
        self.assertIn(prefix + 'market_struck', attack)
        repair = self.node(market, 'swing_say')['Choices'][1]['Check']
        self.assertEqual((repair['Success'], repair['Failure']), ('mended', 'strike'))
        histories = [
            (attack | set(self.node(market, 'mended')['Choices'][0]['Set']), 'room_paddle_mended'),
            (attack | set(self.node(market, 'strike')['Choices'][0]['Set']), 'room_paddle'),
            (attack | set(self.node(market, 'swing_say')['Choices'][0]['Set']), 'room_paddle'),
            (attack, 'room_paddle_unresolved'),
            (set(), None),
        ]
        incoming = [a for a in self.node(room, 'room')['Choices']
                    if (a.get('Next') or '').startswith('room_paddle')]
        for flags, target in histories:
            with self.subTest(flags=sorted(flags)):
                shown = [a['Next'] for a in incoming if available(a, flags)]
                self.assertEqual(shown, [] if target is None else [target])
        # Mixed old-save flags give the repaired account precedence.
        both = attack | {prefix + 'market_strike', prefix + 'market_mended'}
        self.assertEqual([a['Next'] for a in incoming if available(a, both)], ['room_paddle_mended'])
        self.assertEqual(self.node(room, 'room')['Choices'][0]['Next'], 'room_paddle')

    def test_new_prose_targets_are_exact_and_assigned_to_claude(self):
        sid = 'hepzamirah.trickster.bond.her_room'
        registry = json.loads((ROOT / 'tools/route_packs/plans/prose-pending.json').read_text(encoding='utf-8'))
        queue = json.loads((ROOT / 'tools/route_packs/plans/claude-work-queue.json').read_text(encoding='utf-8'))
        for nid in ['room_paddle_mended', 'room_paddle_unresolved']:
            text = self.node(sid, nid)['Text']
            self.assertTrue(text.startswith('[PROSE PENDING: '))
            self.assertIn(dict(scene=sid, node=nid, surface='node', index=None,
                               text_sha=hashlib.sha256(json.dumps(text, ensure_ascii=False, sort_keys=True,
                                                          separators=(',', ':')).encode('utf-8')).hexdigest()), registry['pending'])
            self.assertTrue(any(e['scene'] == sid and e.get('node') == nid and e['woman'] == 'hepzamirah'
                                for e in queue))


if __name__ == '__main__':
    unittest.main()
