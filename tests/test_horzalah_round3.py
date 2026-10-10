"""Round-three histories checked against the final assembled story."""
import itertools
import unittest

from tests.story_fixture import fresh_story
from tests.test_horzalah_round2 import shown
from storylines import horzalah_trickster as route


class HorzalahRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, suffix, nid):
        return next(n for n in self.scenes[route.H + suffix]['Nodes'] if n['Id'] == nid)

    def test_post_inventory_helper_repairs_every_folded_report_edge(self):
        # The final export currently still needs the out-of-scope expansion.py
        # hook. Verify the route-owned helper on that actual exported graph,
        # rather than presenting its intermediate result as shipped output.
        import copy
        from storylines.horzalah_guild import polish_sister_consumers
        payload = copy.deepcopy(self.story)
        polish_sister_consumers(payload)
        scenes = {s['Id']: s for s in payload['Scenes']}
        current = 'participant.hepzamirah.available'
        departure = route.H + 'sister_departed'
        for suffix in ('unmet.knife', 'late.at_night'):
            for source in ('hall', 'came', 'late', 'box'):
                choices = next(n for n in scenes[route.H + suffix]['Nodes']
                               if n['Id'] == 'eng8.guild.' + source)['Choices']
                for returned, available, departed in itertools.product((False, True), repeat=3):
                    # Current participant availability already entails return.
                    if available and not returned:
                        continue
                    flags = {key for key, value in ((route.HEPZ_BACK, returned),
                             (current, available), (departure, departed)) if value}
                    selected = [c['Next'] for c in choices if shown(c, flags)]
                    target = ('sister' if available else 'sister_departed' if returned and departed
                              else 'sister_unavailable' if returned else 'pivot')
                    self.assertEqual(selected, ['eng8.guild.' + target], (suffix, source, flags))
                    for came, late, box in itertools.product((False, True), repeat=3):
                        paid = flags | {key for key, value in ((route.CAME, came),
                                       (route.LATE, late), (route.BOX_KEPT, box)) if value}
                        expected = ('came' if source == 'hall' and came
                                    else 'late' if source in ('hall', 'came') and late
                                    else 'box' if source != 'box' and box else target)
                        self.assertEqual([c['Next'] for c in choices if shown(c, paid)],
                                         ['eng8.guild.' + expected], (suffix, source, paid))
                    if target != 'pivot':
                        reaction = next(n for n in scenes[route.H + suffix]['Nodes']
                                        if n['Id'] == 'eng8.guild.' + target)
                        self.assertEqual([c['Next'] for c in reaction['Choices'] if shown(c, flags)],
                                         ['eng8.guild.pivot'])
                        # Final exported reaction exits must remain usable
                        # even before the missing coordinator hook is added.
                        exported = self.node(suffix, 'eng8.guild.' + target)
                        self.assertEqual([c['Next'] for c in exported['Choices'] if shown(c, flags)],
                                         ['eng8.guild.pivot'])

    def test_refusal_recollection_in_both_commitment_locations(self):
        for collar, move in (('commit.collar', 'commit.her_move'),
                             ('commit.collar_night', 'commit.her_move_night')):
            for source, receipt, target in (('buyer', 'reached', 'decided'),
                                             ('brand', 'brand', 'decided_brand')):
                refusal = select_answer(self.node(collar, source)['Choices'], ((None, False, None, None, (), ()),), expected_position=0)
                self.assertIn(route.DECLINED, refusal['Set'])
                self.assertIn(route.H + 'refused.' + receipt, refusal['Set'])
                choices = self.node(move, 'start')['Choices']
                self.assertEqual([c['Next'] for c in choices if shown(c, set(refusal['Set']))], [target])
                self.assertEqual(select_answer(self.node(move, target)['Choices'], (('move', False, None, None, (), ()),), expected_position=0)['Next'], 'move')

    def test_remote_letter_does_not_invent_a_departure(self):
        letter = self.scenes[route.H + 'letter.first']
        self.assertTrue(letter.get('Remote'))
        self.assertEqual({c['Next'] for c in self.node('letter.first', 'read')['Choices']}, {'board'})
        self.assertFalse(any(route.LEFT_FREE in c['Set'] for n in letter['Nodes'] for c in n['Choices']))


    def test_native_leadership_survives_free_departure(self):
        for suffix in ('guild', 'trio'):
            scene = self.scenes['horzalah.native.eng7_f6c.' + suffix]
            self.assertNotIn('horzalah.present_now', scene.get('Requires', []))
            flags = {'trickster.now', route.PRIMED, route.RETURNED,
                     route.LEFT_FREE, route.H + 'guild_survives'}
            self.assertTrue(shown(scene, flags))
        forbidden = self.story['DerivedForbids'][route.H + 'guild_survives']
        self.assertIn('horzalah.dead', forbidden)
        self.assertIn('horzalah.returned_actor_lost', forbidden)

    def test_lastcall_completion_and_corked_recovery_preserved(self):
        # endings1 deliberately retains callable's old ear-only contract.
        # account_due is the added completion predicate required by the call.
        call = self.scenes['horzalah.lastcall.call']
        self.assertIn('horzalah.lastcall.account_due', call['Requires'])
        groups = self.story['Derived']['horzalah.lastcall.account_due']
        self.assertTrue(groups)
        for group in groups:
            self.assertIn(route.EAR, group)
            self.assertIn(route.PRIMED, group)
            self.assertIn(route.RETURNED, group)
        call_flags = {route.EAR}
        self.assertFalse(any(set(group) <= call_flags for group in groups))
        page = next(n for n in self.scenes['horzalah.lastcall.page']['Nodes'] if n['Id'] == 'page')
        heroic = [p for p in page['Paragraphs']
                  if 'lastcall.recovered_corked' in p.get('Requires', [])]
        self.assertTrue(heroic)
        self.assertTrue(all('lastcall.recovered_corked' in p['Requires'] for p in heroic))
        self.assertTrue(all('lastcall.recovered_opened' not in p['Requires'] for p in heroic))




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

if __name__ == '__main__':
    unittest.main()
