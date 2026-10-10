"""Native outcome partitioning and current participant guards for ix-b."""
import itertools
import unittest

from storylines.trickster_interactions_ix_b import SCENES, REPLACEMENT


def matches(scene, flags):
    return (set(scene['Requires']) <= flags
            and not set(scene['Forbids']) & flags
            and all(set(group) & flags for group in scene.get('RequiresAnyGroups', [])))



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


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

class InteractionTests(unittest.TestCase):
    def test_dialogue_has_no_ambiguous_speaker_or_tooling_residue(self):
        from tools.player_text_lint import check
        self.assertEqual([], check({'Scenes': SCENES})['review'])

    def test_wintersun_outcomes_have_exactly_one_account(self):
        scenes = [s for s in SCENES if s['Relationship'] == 'gesmerha']
        for truth, ruling, dead in itertools.product((False, True), repeat=3):
            flags = {'trickster', 'gesmerha.present_now', 'soana.present_now',
                     'gesmerha.wintersun_resolved', 'soana.after_quest',
                     'gesmerha.truth' if truth else 'gesmerha.illusions'}
            if ruling:
                flags.add('gesmerha.marhevok_rules')
            if dead:
                flags.add('soana.guardian_dead')
            expected = 'gesmerha.react.soana.%s.%s.%s' % (
                'truth' if truth else 'illusions', 'marhevok' if ruling else 'chief', 'lost' if dead else 'orso')
            self.assertEqual([expected], [s['Id'] for s in scenes if matches(s, flags)])
            self.assertFalse(any(matches(s, flags | {"gesmerha.trickster.clan_destroyed"}) for s in scenes))
            for woman in ('soana', 'gesmerha'):
                self.assertFalse(any(matches(s, flags - {woman + '.present_now'}) for s in scenes))

    def test_replacement_has_no_old_memory_and_no_overlap(self):
        scenes = [s for s in SCENES if s['Relationship'] == 'nenio']
        base = {'trickster', 'nenio.present_now', 'arueshalae.present_now', 'arueshalae.evil_recruited', 'nenio.in_party'}
        for recreated, unremembered in itertools.product((False, True), repeat=2):
            flags = base | {key for key, enabled in zip(REPLACEMENT, (recreated, unremembered)) if enabled}
            self.assertFalse(any(matches(s, flags - {'nenio.in_party'}) for s in scenes))
            available = [s for s in scenes if matches(s, flags)]
            self.assertIsNotNone(only(available))
            expected = 'replacement' if recreated or unremembered else 'scholar'
            self.assertEqual(['nenio.react.fallen_arueshalae.' + expected], [s['Id'] for s in available])

    def test_encounters_grant_no_progression_and_require_both_women(self):
        for scene in SCENES:
            self.assertTrue(scene['Reaction'])
            self.assertEqual(scene['Owner'].lower(), scene['Relationship'])
            expected = {'gesmerha': {'gesmerha.present_now', 'soana.present_now'},
                        'nenio': {'nenio.present_now', 'arueshalae.present_now'},
                        'aranka': {'aranka.present_now', 'arueshalae.present_now'}}[scene['Relationship']]
            self.assertEqual(expected, {k for k in scene['Requires'] if k.endswith('.present_now')})
            self.assertIn('trickster', scene['Requires'])
            self.assertTrue(scene['AnswerLists'])
            for target in scene['AnswerLists']:
                self.assertRegex(target, r'^[0-9a-f]{32}$')
            self.assertIsNotNone(only(scene['Nodes']))
            self.assertFalse(by_contract(scene['Nodes'], [{'Id': 'start'}]).get('Paragraphs'))
            self.assertTrue(by_contract(scene['Nodes'], [{'Id': 'start'}])['Choices'])
            self.assertTrue(all(not c['Set'] and not c['Requires'] and not c['Forbids']
                                for c in by_contract(scene['Nodes'], [{'Id': 'start'}])['Choices']))


    def test_song_states_do_not_overlap(self):
        scenes = [s for s in SCENES if s['Relationship'] == 'aranka']
        for yard, fallen in itertools.product((False, True), repeat=2):
            flags = {'trickster', 'aranka.present_now', 'arueshalae.present_now',
                     'aranka.trickster.in_drezen',
                     'arueshalae.evil_recruited' if fallen else 'arueshalae.changed'}
            if yard:
                flags.add('aranka.presence.failed')
            expected = 'aranka.react.arueshalae.' + ('fallen' if fallen else 'dreamer') + ('.yard' if yard else '')
            self.assertEqual([expected], [s['Id'] for s in scenes if matches(s, flags)])
            self.assertFalse(any(matches(s, flags - {'aranka.present_now'}) for s in scenes))
            self.assertFalse(any(matches(s, flags - {'arueshalae.present_now'}) for s in scenes))
