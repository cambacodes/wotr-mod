"""Current-base structural acceptance; prose and live delivery remain owner work."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.test_anevia_partner_stance import holds
from tools.claude_work_queue_lint import check as queue_check
from tools.voice_authority import digest
from tools.prose_pending_lint import check as pending_check

ROOT = Path(__file__).resolve().parents[1]


class Struct207Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_return_then_loss_cannot_retain_bodily_wife_paragraphs(self):
        # At Threshold the observer reports a later loss, while the historical
        # paid return persists. A current body flag exists only before the loss.
        base = {'anevia.trickster.returned', 'irabeth.trickster.returned',
                'anevia.trickster.cost.knows_the_bargain',
                'anevia.trickster.late_committed'}
        live = base | {'irabeth.present_now', 'crossroute.irabeth.available'}
        for sid in ('anevia.ending_open', 'anevia.ending_kept', 'anevia.ending_promised',
                    'anevia.trickster.epilogue.nailed_wardrobe'):
            paragraphs = self.node(sid, 'end')['Paragraphs']
            bodily = [p for p in paragraphs if any(beat in p['Text'] for beat in
                       ('Beth stood watch', 'Irabeth came with her', 'Whenever Beth was in'))]
            self.assertGreaterEqual(len(bodily), 3)
            for loss in ('irabeth_dead', 'irabeth.returned_actor_lost', 'irabeth.epoch_redeparted'):
                lost = base | {loss, 'irabeth.epoch_unavailable'}
                for paragraph in bodily:
                    self.assertIn('irabeth.present_now', paragraph['Requires'])
                    self.assertFalse(holds(paragraph, lost), (sid, loss, paragraph))
            self.assertTrue(any(holds(p, live) for p in bodily))
            # Return-device memories remain historical, independent of Beth's body.
            tray = next(p for p in paragraphs if 'crate lid' in p['Text'])
            self.assertNotIn('irabeth.present_now', tray['Requires'])
        for sid in ('anevia.ending_open', 'anevia.ending_kept', 'anevia.ending_promised'):
            self.assertEqual('irabeth.present_now',
                             self.scenes[sid]['ForbidOverrides']['irabeth_dead'])

    def test_kept_door_without_konomi_preserves_earned_device_and_price(self):
        entry = self.node('anevia.trickster.gone.setup', 'start')['Choices'][1]
        self.assertTrue(holds(entry, {'closets.door_kept', 'socot.gone'}))
        self.assertEqual('door', entry['Next'])
        paid = self.node('anevia.trickster.gone.setup', 'door')['Choices'][0]
        self.assertIn('closets.door_kept', paid['Requires'])
        self.assertIn('trickster', paid['Requires'])
        self.assertTrue(any('stolen_door' in key for key in paid['Set']))
        self.assertNotIn('konomi.present_now', paid['Requires'])
        # Independent expected cost; do not derive it from the branch under test.
        self.assertEqual(-100, paid['Crusade']['Amount'])

    def test_saved_widow_kiss_predicate_and_retired_exit_siblings(self):
        for suffix, nid in (('commit', 'answer'), ('fetched_commit', 'answer'),
                            ('second_ask', 'price'), ('fetched_second_ask', 'price')):
            sid = 'anevia.trickster.gone.' + suffix
            page = self.node(sid, nid)
            if nid == 'answer':
                kiss = page['Choices'][0]
                self.assertEqual('yes', kiss['Next'])
                self.assertTrue(holds(kiss, {'irabeth_dead', 'trickster.now'}), sid)
                self.assertFalse(holds(kiss, {'irabeth_dead', 'irabeth.trickster.returned', 'trickster.now'}))
            exits = [a for a in page['Choices'] if a.get('Abort')]
            self.assertTrue(any(holds(a, set()) for a in exits))
            retired = [a for a in exits if set(a['Requires']) & set(a['Forbids'])]
            self.assertEqual(1, len(retired))
            self.assertEqual([], retired[0]['Set'])
            self.assertIsNone(retired[0]['Next'])

    def test_fetched_widow_has_a_legal_scene_entry(self):
        # This shared classifier dependency is outside route ownership. Keep
        # the acceptance failing until its owner extends the widow exemption
        # to the fetched sibling; choice satisfiability alone is insufficient.
        scene = self.scenes['anevia.trickster.gone.fetched_commit']
        self.assertNotIn('crossroute.irabeth.unavailable', scene['Forbids'])

    def test_fourth_uses_actual_survivor_completion_in_both_placements(self):
        for suffix in ('', '.arcade'):
            sid = 'mielarah.deck.fourth' + suffix
            seam = self.node(sid, 'seam')
            self.assertEqual(['owned', 'blamed'], [a['Next'] for a in seam['Choices'][:2]])
            for posted in (False, True):
                for owned in (False, True):
                    flags = {'mielarah.trickster.storm.survivor_drezen' if posted
                             else 'mielarah.trickster.storm.survivor'}
                    if owned:
                        flags.add('mielarah.trickster.storm.owned')
                    offered = [a for a in seam['Choices'] if holds(a, flags)]
                    self.assertEqual(1, len(offered), (suffix, posted, owned))
                    expected = ('owned' if owned else 'blamed') + ('_posted' if posted else '')
                    self.assertEqual(expected, offered[0]['Next'])
                    self.assertEqual('third_exp', self.node(sid, expected)['Choices'][0]['Next'])
            self.assertFalse(any(holds(a, set()) for a in seam['Choices']))

    def test_owned_placeholders_and_queue_are_registered(self):
        pending = json.loads((ROOT / 'tools/route_packs/plans/prose-pending.json').read_text(encoding='utf-8'))
        queue = json.loads((ROOT / 'tools/route_packs/plans/claude-work-queue.json').read_text(encoding='utf-8'))
        self.assertEqual([], queue_check(queue))
        errors = pending_check(self.story, pending, integration=True)
        self.assertEqual([], errors)
        for suffix in ('', '.arcade'):
            for nid in ('owned_posted', 'blamed_posted'):
                text = self.node('mielarah.deck.fourth' + suffix, nid)['Text']
                target = next(e for e in pending['pending'] if e['scene'] == 'mielarah.deck.fourth' + suffix
                              and e['node'] == nid)
                self.assertEqual(digest(text), target['text_sha'])

    def test_conversion_floor_is_local_and_e15c_legal(self):
        for sid in ('anevia.the_woman_with_the_basket', 'anevia.the_counting_room',
                    'gesmerha.the_box_with_two_names', 'gesmerha.the_things_still_here',
                    'mielarah.deck.wounded', 'mielarah.deck.correction', 'mielarah.deck.special_cargo'):
            siblings = [self.scenes[sid]]
            if sid + '.arcade' in self.scenes:
                siblings.append(self.scenes[sid + '.arcade'])
            for scene in siblings:
                self.assertFalse(scene.get('Remote'))
                self.assertNotIn('Kind', scene)
                self.assertTrue(scene['Areas'])
                self.assertTrue(scene['ContactUnit'])
                self.assertTrue(scene.get('AnswerLists') or scene.get('InteractionHub'))


if __name__ == '__main__':
    unittest.main()
