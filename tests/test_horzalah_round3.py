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
                refusal = self.node(collar, source)['Choices'][0]
                self.assertIn(route.DECLINED, refusal['Set'])
                self.assertIn(route.H + 'refused.' + receipt, refusal['Set'])
                choices = self.node(move, 'start')['Choices']
                self.assertEqual([c['Next'] for c in choices if shown(c, set(refusal['Set']))], [target])
                text = self.node(move, target)['Text']
                self.assertIn('reached like a buyer' if source == 'buyer' else 'asked whose brand', text)
                if source == 'brand':
                    self.assertNotIn('reached', text)
                self.assertEqual(self.node(move, target)['Choices'][0]['Next'], 'move')

    def test_remote_letter_does_not_invent_a_departure(self):
        letter = self.node('letter.first', 'read')['Text']
        self.assertNotIn('left for your war', letter)
        self.assertNotIn('pitching the tents', letter)
        self.assertNotIn('Come back to Drezen', letter)
        self.assertIn('refused three offers for your head', letter)

    def test_wager_loss_is_her_preferred_outcome(self):
        text = ' '.join(p['Text'] for p in self.node('epilogue.together', 'page')['Paragraphs'])
        self.assertIn('If the Commander returned, she would lose every coin', text)
        self.assertNotIn('demons would owe her money', text)

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
        heroic = [p['Text'] for p in page['Paragraphs']
                  if 'lastcall.recovered_corked' in p.get('Requires', [])]
        self.assertTrue(any('flask stayed corked' in t for t in heroic))
        self.assertFalse(any('flask was opened' in t for t in heroic))


if __name__ == '__main__':
    unittest.main()
