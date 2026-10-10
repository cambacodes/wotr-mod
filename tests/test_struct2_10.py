"""Pinned structure counterexamples, through the fully assembled scene inventory."""
import copy
import unittest

from tests.story_fixture import fresh_story



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

class Structure210Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def holds(self, key, flags, trail=()):
        if key in trail:
            return False
        groups = self.story.get('Derived', {}).get(key)
        if groups is None:
            return key in flags
        trail = (*trail, key)
        if any(self.holds(k, flags, trail) for k in self.story.get('DerivedForbids', {}).get(key, [])):
            return False
        return any(all(self.holds(k, flags, trail) for k in group) for group in groups)

    def enabled(self, block, flags):
        return (all(self.holds(k, flags) for k in block.get('Requires', []))
                and all(any(self.holds(k, flags) for k in group)
                        for group in block.get('RequiresAnyGroups', []) + block.get('AnyGroups', []))
                and not any(self.holds(k, flags)
                            and not self.holds(block.get('ForbidOverrides', {}).get(k, ''), flags)
                            for k in block.get('Forbids', [])))

    def nodes(self, sid):
        return {n['Id']: n for n in self.scenes[sid]['Nodes']}

    def test_deliberate_drowning_reaches_loss_at_chapter_six(self):
        flags = {'trickster.ever', 'shamira.killed', 'availability.observed'}
        choice = by_contract(self.nodes('shamira.trickster.killed.drowning')['choose']['Choices'], [{'Next': 'gone', 'Requires': [], 'Forbids': [], 'Set': ['shamira.trickster.declined', 'shamira.closed'], 'Abort': False}])
        self.assertEqual(choice['Next'], 'gone')
        flags.update(choice['Set'])
        self.assertIn('shamira.closed', flags)
        self.assertNotIn('shamira.trickster.returned', flags)
        flags.add('chapter_later')
        page = self.scenes['shamira.trickster.epilogue.drowned']
        self.assertEqual(page['MinChapter'], 6)
        self.assertTrue(self.enabled(page, flags))
        self.assertFalse(self.holds('shamira.present_now', flags))
        self.assertFalse(self.enabled(page, flags | {'shamira.trickster.returned'}))
        self.assertFalse(self.enabled(page, flags | {'sacrifice'}))
        self.assertTrue(self.enabled(page, flags | {'sacrifice', 'ending.trickster'}))
        mutant = copy.deepcopy(page)
        mutant['Requires'].append('shamira.present_now')
        self.assertFalse(self.enabled(mutant, flags))

    def test_kept_and_equal_court_survive_each_nocticula_fate(self):
        flags = {'trickster.ever', 'trickster', 'chapter_later', 'availability.observed',
                 'shamira.killed', 'shamira.trickster.returned', 'shamira.trickster.embodied',
                 'shamira.committed', 'shamira.partner_stance.share',
                 'shamira.trickster.visited', 'shamira.trickster.lost_on_purpose',
                 'shamira.trickster.arch'}
        page = self.scenes['shamira.trickster.epilogue.kept']
        for fate in (set(), {'noct.dead'}, {'noct.dead', 'noct.defeated_not_dead'},
                     {'noct.dead', 'nocticula.trickster.returned'}):
            with self.subTest(fate=fate):
                state = flags | fate
                self.assertTrue(self.enabled(page, state), page['Forbids'])
                for suffix in ('', '_awning'):
                    nodes = self.nodes('shamira.trickster.harem' + suffix)
                    for nid in ('bell_silence', 'partner_public_court'):
                        choice = by_contract(nodes[nid]['Choices'], [{'Next': 'equal', 'Requires': [], 'Forbids': [], 'Set': ['shamira.trickster.court.equal'], 'Abort': False}])
                        self.assertEqual(choice['Next'], 'equal')
                        self.assertTrue(self.enabled(choice, state), choice)
                self.assertFalse(self.enabled(page, state | {'shamira.returned_actor_lost'}))
        mutant = copy.deepcopy(page)
        mutant['Forbids'].append('crossroute.nocticula.unavailable')
        self.assertFalse(self.enabled(mutant, flags | {'noct.dead'}))

    def test_chaplain_refusal_does_not_earn_prayer(self):
        nodes = self.nodes('nidalynn.trickster.kiln.the_chaplain')
        for branch, expected in (('after_prayer', 'nidalynn.trickster.chaplain_prayed'),
                                 ('leave', 'nidalynn.trickster.chaplain_sent_away')):
            flags = set(by_contract(nodes[branch]['Choices'], [{'Next': 'end', 'Requires': [], 'Forbids': [], 'Set': ['nidalynn.trickster.chaplain_prayed'], 'Abort': False}, {'Next': 'end', 'Requires': [], 'Forbids': [], 'Set': ['nidalynn.trickster.chaplain_sent_away'], 'Abort': False}])['Set'])
            flags.update(by_contract(nodes['end']['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])['Set'])
            self.assertEqual(flags, {expected})

    def test_kiln_is_already_local_with_paid_delay_and_tending_choice(self):
        scene = self.scenes['nidalynn.trickster.kiln.fire']
        self.assertFalse(scene.get('Remote'))
        self.assertNotIn('Kind', scene)
        self.assertEqual(scene['InteractionHub'], 'nidalynn.presence')
        self.assertEqual(scene['Areas'], ['2570015799edf594daf2f076f2f975d8'])
        self.assertEqual(scene['DelayHours'], 24)
        self.assertIn('nidalynn.trickster.kiln_agreed', scene['Requires'])
        self.assertIn('nidalynn.trickster.kiln', scene['Forbids'])
        nodes = self.nodes(scene['Id'])
        self.assertEqual(by_contract(nodes['remember']['Choices'], [{'Next': 'feed', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])['Next'], 'feed')
        self.assertIn('nidalynn.trickster.kiln', by_contract(nodes['knocking']['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['nidalynn.trickster.kiln'], 'Abort': False}])['Set'])
