"""Executable negative walks for the personal concession and both rescue receipts."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.fix16b_structure import reachable_nodes

from storylines import iomedae_banner as banner
from storylines import iomedae_trickster as io


SCENES = {s['Id']: s for s in [*io.SCENES, *banner.SCENES]}


def complete(flags):
    flags = set(flags)
    while True:
        extra = {key for key, groups in io.DERIVED.items()
                 if any(set(group) <= flags for group in groups)} - flags
        if not extra:
            return flags
        flags.update(extra)


def matches(block, flags):
    flags = complete(flags)
    overrides = block.get('ForbidOverrides', {})
    return (set(block.get('Requires', [])) <= flags
            and not any(f in flags and overrides.get(f) not in flags
                        for f in block.get('Forbids', []))
            and all(set(g) & flags for g in block.get('RequiresAnyGroups', [])))


def walk(sid, flags, scenes=None):
    scene = (SCENES if scenes is None else scenes)[io.E + sid]
    nodes = {n['Id']: n for n in scene['Nodes']}
    stack = [(scene['Nodes'][0]['Id'], complete(flags), ())]
    visited = set()
    outcomes = []
    while stack:
        nid, held, path = stack.pop()
        signature = nid, frozenset(held)
        if signature in visited:
            continue
        visited.add(signature)
        choices = [c for c in nodes[nid]['Choices'] if matches(c, held)]
        if not choices:
            raise AssertionError((sid, nid, 'Page has no selectable answers', sorted(held)))
        for choice in choices:
            gained = complete(held | set(choice['Set']))
            targets = [choice['Next']] if choice['Next'] else []
            if choice.get('Check'):
                targets = [choice['Check']['Success'], choice['Check']['Failure']]
            trail = (*path, nid)
            if targets:
                stack.extend((target, gained, trail) for target in targets)
            else:
                outcomes.append((gained, trail))
    return outcomes


class IomedaeRound2Tests(unittest.TestCase):
    def test_war_talk_and_argument_only_cannot_earn_personal_yes(self):
        for history in [(), (io.E + 'dream.summit', io.E + 'dream.herald'),
                        (io.ARGUMENT_ONLY,), (io.POSTPONED,)]:
            with self.subTest(history=history):
                flags = {'trickster', 'trickster.ever', io.STARTED, io.BANNER_HELD,
                         io.CALLED, io.BRIDGE_SEEN, io.IZ_DONE, *history}
                self.assertNotIn(io.COURTED, complete(flags))
                if not history or io.ARGUMENT_ONLY not in history:
                    out = walk('disputation', flags)
                    self.assertFalse(any(io.COMMITTED in held for held, _ in out))
                    self.assertTrue(any(io.POSTPONED in held for held, _ in out))
                out = walk('threshold.banner', flags)
                self.assertFalse(any(io.COMMITTED in held for held, _ in out))
                self.assertTrue(any(io.RESCUE_ONLY in held for held, _ in out))

    def test_personal_exchange_and_late_exchange_earn_their_own_answer(self):
        questions = walk('dream.questions', {io.STARTED, io.KEY_LATCH, io.CALLED})
        personal = [held for held, _ in questions if io.PERSONAL in held]
        professional = [held for held, path in questions if 'professional' in path]
        self.assertTrue(personal)
        self.assertTrue(professional)
        self.assertTrue(all(io.COURTED in held for held in personal))
        self.assertTrue(all(io.COURTED not in held for held in professional))
        self.assertTrue(all(io.COMMITTED not in held for held, _ in questions))
        late = walk('dream.eve', {io.POSTPONED, io.ARGUMENT_ONLY})
        self.assertTrue(any(io.COURTED in held and 'eve.answer' in path for held, path in late))
        self.assertTrue(any(io.COURTED not in held and 'eve.professional' in path for held, path in late))
        for receipt in [(io.PERSONAL,), (io.POSTPONED, io.EVE_PERSONAL)]:
            out = walk('threshold.banner', {io.BANNER_HELD, *receipt})
            self.assertTrue(any(io.COMMITTED in held for held, _ in out))

    def test_herald_outcomes_and_cruelty_are_distinct(self):
        for flag, wanted, absent in [(io.HERALD_HEAVEN, 'saved', 'exiled'),
                                     (io.HERALD_EXILED, 'exiled', 'saved'),
                                     (io.HERALD_FELL, 'fell', 'spite'),
                                     (io.HERALD_SPITE, 'spite', 'fell')]:
            out = walk('dream.herald', {flag, io.HERALD_SAVED} if flag in
                       (io.HERALD_HEAVEN, io.HERALD_EXILED) else {flag, io.HERALD_FELL})
            self.assertTrue(all(wanted in path and absent not in path for _, path in out))
        out = walk('dream.herald', {io.HERALD_SPITE, io.HERALD_FELL})
        self.assertTrue(any(io.CLOSED in held for held, _ in out))
        accounted = next(held for held, _ in out if io.HERALD_ACCOUNTED in held)
        self.assertNotIn(io.COMMITTED, accounted)
        scene = SCENES[io.E + 'dream.questions']
        initial = {'trickster.ever', io.STARTED, io.KEY_LATCH, io.CALLED, io.HERALD_SPITE}
        self.assertFalse(matches(scene, initial))
        self.assertTrue(matches(scene, initial | {io.HERALD_ACCOUNTED}))

    def test_private_memory_is_not_available_from_the_public_legend(self):
        out = walk('herald.legend', set())
        self.assertFalse(any('burned' in path or 'dreams' in path for _, path in out))
        self.assertTrue(any('how' in path for _, path in out))
        out = walk('herald.legend', {io.BRIDGE_SEEN})
        self.assertTrue(any('dreams' in path for _, path in out))

    def test_slots_have_one_first_night_and_history_specific_mornings(self):
        scenes = {scene['Id']: scene for scene in fresh_story()['Scenes']}
        slot = io.E + 'epilogue.platform.explicit.1'
        for flags, morning in [({io.KEPT, io.DEAD_TO_WORLD}, 'morning_kept'),
                               ({io.DEAD_TO_WORLD}, 'morning_dead'), (set(), 'morning_open')]:
            out = walk('epilogue.platform', flags, scenes)
            acts = [path for _, path in out if slot in path]
            self.assertTrue(acts)
            self.assertTrue(all(morning in path and path.count(slot) == 1 for path in acts))
            quiet = [path for _, path in out if 'night_quiet' in path]
            self.assertTrue(quiet)
            self.assertTrue(all(slot not in path and not any(n.startswith('morning_') for n in path)
                                for path in quiet))
        out = walk('epilogue.after', {io.KEPT}, scenes)
        self.assertTrue(any(io.E + 'epilogue.after.explicit.1' in path for _, path in out))
        self.assertFalse(any(io.E + 'epilogue.after.explicit.1' in path
                             for _, path in walk('epilogue.after', set(), scenes)))
        for scene in ['epilogue.platform', 'epilogue.after']:
            self.assertTrue(all(not c['Set'] for n in scenes[io.E + scene]['Nodes'] for c in n['Choices']))
        for sid, nid in ((io.E + 'epilogue.platform', slot),
                         (io.E + 'epilogue.after', io.E + 'epilogue.after.explicit.1')):
            self.assertIn(nid, reachable_nodes(scenes[sid]))

    def test_both_returns_collect_the_actual_banner_and_miracle_debts(self):
        for receipt, page in [(io.COMMITTED, 'after'), (io.RESCUE_ONLY, 'rescued')]:
            for cloth in [io.BANNER_HELD, io.ORDER_BANNER]:
                flags = complete({'trickster.ever', io.SACRIFICE, io.WOUND_CLOSED,
                                  io.CARRIED, receipt, cloth})
                flags.add(io.BACK)  # shared commander_back includes both earned bridge outcomes
                self.assertIn(io.BURIED_ALIVE, flags)
                self.assertIn(io.MIRACLE, flags)
                scene = SCENES[io.E + 'epilogue.' + page]
                self.assertTrue(matches(scene, flags))
                visible = [p['Text'] for n in scene['Nodes'] for p in n.get('Paragraphs', [])
                           if matches(p, flags)]
                account = ' '.join(visible)
                self.assertIn('ninth year', account)
                self.assertIn('debt is paid', account)
                self.assertIn('ford', account)
                self.assertIn('body could not wield', account)
                if page == 'rescued':
                    self.assertFalse(any('.explicit.' in n['Id'] for n in scene['Nodes']))
                    self.assertIn('fell into the seam' if cloth == io.BANNER_HELD else
                                  'palm never closed', account)
        unreturned = {'trickster.ever', io.SACRIFICE, io.STARTED, io.COMMITTED}
        for page in ['platform', 'after', 'lived']:
            self.assertFalse(matches(SCENES[io.E + 'epilogue.' + page], unreturned))


if __name__ == '__main__':
    unittest.main()
