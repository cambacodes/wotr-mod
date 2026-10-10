"""struct3-a: delayed native history and independent earned intimacy."""
import copy
import json
from pathlib import Path
import unittest

from storylines import aranka_trickster as aranka
from storylines import herrax_trickster as herrax
from storylines import crossroute_presence
from tests.test_crossroute_lint import relationship
from tests.test_jerribeth_partner import allowed, walk
from tests.story_fixture import fresh_story
from tools import rrt_verify as rules
from tools.claude_work_queue_lint import check as queue_check
from tools.prose_pending_lint import check as pending_check



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class DelayedHistoryTests(unittest.TestCase):
    def test_confrontation_partitions_native_history_without_losing_primer(self):
        for late in ('', '_late'):
            for venue in ('', '_yard'):
                sid = 'aranka.trickster.verse.her_letter' + late + venue
                scene = next(s for s in aranka.SCENES if s['Id'] == sid)
                nodes = {n['Id']: n for n in scene['Nodes']}
                for known in (False, True):
                    for crowned, gone, coronation, expected in (
                            (True, False, False, 'known' if known else 'unknown'),
                            (False, False, False, 'struct3_a.' + ('known' if known else 'unknown') + '.uncrowned'),
                            (False, True, False, 'struct3_a.' + ('known' if known else 'unknown') + '.departed'),
                            (True, True, False, 'struct3_a.' + ('known' if known else 'unknown') + '.departed'),
                            (False, False, True, 'struct3_a.' + ('known' if known else 'unknown') + '.crown_refused')):
                        with self.subTest(scene=sid, known=known, crowned=crowned, gone=gone):
                            flags = {aranka.PRIMED, 'trickster.now'}
                            if known:
                                flags.add(aranka.GAVE_SONG)
                            if coronation:
                                flags.add('coronation.seen')
                            if crowned:
                                flags.add(aranka.CROWNED)
                            if gone:
                                flags.add(aranka.KING_GONE)
                            choices = [c for c in nodes['start']['Choices'] if allowed(c, flags)]
                            self.assertEqual([expected], [c['Next'] for c in choices])
                            self.assertEqual(nodes['known' if known else 'unknown']['Choices'], nodes[expected]['Choices'])
                            self.assertNotIn(aranka.CROWNED, scene['Requires'])
                            self.assertNotIn(aranka.KING_GONE, scene['Forbids'])


class ClosingTests(unittest.TestCase):
    def closing(self, restored=False, mutation=False):
        sid = herrax.H + 'madam.reachable' + ('_restored' if restored else '')
        scene = copy.deepcopy(next(s for s in herrax.SCENES if s['Id'] == sid))
        if mutation:
            next(n for n in scene['Nodes'] if n['Id'] == 'cut')['Text'] += ' Chivarro stands beside the cushions.'
        story = dict(Relationships={'herrax': relationship('herrax'), 'chivarro': relationship('chivarro')},
                     Scenes=[scene], Derived={})
        crossroute_presence.integrate(story)
        return by_contract(story['Scenes'], [{'Id': 'herrax.trickster.madam.reachable'}, {'Id': 'herrax.trickster.madam.reachable_restored'}])

    def test_private_closing_finishes_with_foreign_actor_present_or_absent(self):
        for restored in (False, True):
            scene = self.closing(restored)
            nodes = {n['Id']: n for n in scene['Nodes']}
            for absent in (False, True):
                flags = {'trickster.ever'}
                flags.add('crossroute.chivarro.unavailable' if absent else 'crossroute.chivarro.available')
                with self.subTest(restored=restored, absent=absent):
                    offer = by_contract(nodes['offer']['Choices'], [{'Next': 'desire', 'Requires': [], 'Forbids': [], 'Set': ['herrax.committed'], 'Abort': False}])
                    accepted = flags | set(offer['Set'])
                    self.assertIn(herrax.COMMITTED, accepted)
                    self.assertNotIn(herrax.MORNING, accepted)
                    self.assertEqual(['cut', 'cut'],
                                     [c['Next'] for c in nodes['threshold2']['Choices'] if allowed(c, accepted)])
                    _, ends = walk(scene, accepted, start='desire')
                    self.assertTrue(ends)
                    self.assertTrue(all(herrax.MORNING in state for state in ends))
                    self.assertNotIn(herrax.MORNING, flags | set(by_contract(nodes['offer']['Choices'], [{'Next': 'no', 'Requires': [], 'Forbids': [], 'Set': ['herrax.closed'], 'Abort': False}])['Set']))

    def test_actual_foreign_participation_still_requires_presence(self):
        for restored in (False, True):
            scene = self.closing(restored, mutation=True)
            nodes = {n['Id']: n for n in scene['Nodes']}
            self.assertFalse(any(allowed(c, {'trickster.ever', 'crossroute.chivarro.unavailable'})
                                 for c in nodes['threshold2']['Choices']))


class AssembledTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)

    def test_delayed_consumers_remain_available_after_refusal_or_departure(self):
        for chapter, late in ((3, ''), (5, '_late')):
            for yard in (False, True):
                for history in ((), (aranka.KING_GONE,), (aranka.CROWNED, aranka.KING_GONE)):
                    state = rules.SimState(chapter, 100)
                    state.flags.update(('trickster.ever', 'trickster', 'chapter_later', aranka.PRIMED, 'coronation.seen'))
                    state.flags.update(history)
                    state.times[aranka.PRIMED] = 0
                    if yard:
                        state.flags.add(aranka.FYE_GONE)
                    rules.sim_complete(self.model, state)
                    sid = 'aranka.trickster.verse.her_letter' + late + ('_yard' if yard else '')
                    self.assertTrue(rules.sim_available(self.model, self.model.by_id[sid], state), (sid, history))
                    start = by_contract(self.model.by_id[sid]['Nodes'], [{'Id': 'start'}])
                    expected = 'struct3_a.unknown.departed' if aranka.KING_GONE in history else 'struct3_a.unknown.crown_refused'
                    self.assertEqual([expected], [c['Next'] for c in start['Choices'] if allowed(c, state.flags)])

    def test_exported_closing_has_no_foreign_presence_dead_end(self):
        for restored in (False, True):
            sid = herrax.H + 'madam.reachable' + ('_restored' if restored else '')
            scene = self.model.by_id[sid]
            for absent in (False, True):
                flags = {'trickster.ever', herrax.COMMITTED}
                flags.add('crossroute.chivarro.unavailable' if absent else 'crossroute.chivarro.available')
                _, ends = walk(scene, flags, start='desire')
                self.assertTrue(ends)
                self.assertTrue(all(herrax.MORNING in state for state in ends))

    def test_pending_surfaces_are_registered_if_unresolved(self):
        root = Path(__file__).resolve().parents[1]
        pending = json.loads((root / 'tools/route_packs/plans/prose-pending.json').read_text(encoding='utf-8'))
        queue = json.loads((root / 'tools/route_packs/plans/claude-work-queue.json').read_text(encoding='utf-8'))
        self.assertEqual([], pending_check(self.story, pending, integration=True))
        self.assertEqual([], queue_check(queue))


if __name__ == '__main__':
    unittest.main()
