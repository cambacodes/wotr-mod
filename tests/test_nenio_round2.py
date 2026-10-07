"""Earned observations and append-only situation continuations for Nenio."""
import itertools
import unittest

from storylines import nenio_folios as folios, nenio_trickster as route
from tests.test_nenio_polish import NenioPolishTests


class NenioRound2Tests(unittest.TestCase):
    scene = staticmethod(NenioPolishTests.scene)
    node = staticmethod(NenioPolishTests.node)
    available = staticmethod(NenioPolishTests.available)
    dispatch = NenioPolishTests.dispatch

    def test_retention_uses_played_observation_with_kiss_precedence(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = self.scene(route.P + 'commit.result' + suffix)
            for kissed, bitten in itertools.product((False, True), repeat=2):
                flags = {'trickster.ever', route.SCRIBE}
                flags.update(flag for flag, played in ((folios.KISSED_EARLY, kissed),
                                                       (folios.BITTEN, bitten)) if played)
                expected = 'receipt_kiss' if kissed else 'receipt_bite' if bitten else 'receipt_scribe'
                self.assertEqual(self.dispatch(scene, 'decides', flags), expected)
                self.assertEqual(self.dispatch(scene, expected, flags), 'variable')
                for loss in (route.UNREMEMBERED, route.RECREATED):
                    self.assertEqual(self.dispatch(scene, 'decides', flags | {loss}), 'receipt_scribe')
            # A retained subject can still reject her invitation or pressure her
            # into postponing; observation is not an acceptance producer.
            for ident in ('receipt_kiss', 'receipt_bite', 'receipt_scribe'):
                self.assertFalse(any(route.COMMITTED in c['Set'] for c in self.node(scene, ident)['Choices']))
            refusal = self.node(scene, 'variable')['Choices'][2]
            self.assertTrue({route.REFUSED, route.CLOSED} <= set(refusal['Set']))
            self.assertEqual(self.node(scene, 'variable')['Choices'][3]['Next'], 'postponed')

    def test_control_then_postponement_does_not_report_a_bite(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = self.scene(folios.TEETH + suffix)
            control = self.node(scene, 'kiss')['Choices'][1]
            self.assertEqual(control['Next'], 'record')
            self.assertNotIn(folios.BITTEN, control['Set'])
            self.assertEqual(self.dispatch(scene, 'record', {'trickster.ever'}), 'record_control')
            self.assertEqual(self.dispatch(scene, 'record', {'trickster.ever', folios.BITTEN}), 'record_bite')

    def test_slot_walk_keeps_delivery_effects_and_no_commitment_producer(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = self.scene(route.P + 'night' + suffix)
            self.assertEqual(scene['Areas'], [route.DREZEN])
            slot_id = scene['Id'] + '.explicit.1'
            slot = self.node(scene, slot_id)
            self.assertEqual(self.dispatch(scene, 'watch', {'trickster.ever'}), slot_id)
            legacy_exit = self.node(scene, 'watch')['Choices'][0]
            slot_exit = slot['Choices'][0]
            for key in ('Set', 'Next', 'Abort', 'Requires'):
                self.assertEqual(legacy_exit[key], slot_exit[key])
            self.assertNotIn(route.COMMITTED, slot_exit['Set'])
            self.assertFalse(slot.get('Paragraphs'))
            self.assertTrue(slot['Text'].endswith('"Leave it. I want you here."'))

    def test_late_first_night_is_only_in_supplement_with_legacy_exit(self):
        late = self.scene(route.P + 'epilogue.commit')
        native = next(s for s in route.NATIVE_ENDING_SCENES if s['Id'] == route.P + 'epilogue.native_commit')
        self.assertIn('Eighteen months', native['Nodes'][0]['Text'])
        self.assertNotIn('In the morning', native['Nodes'][0]['Text'])
        self.assertNotIn('shirt', native['Nodes'][0]['Text'])
        self.assertIn('In the morning', self.node(late, 'morning_after')['Text'])
        slot = self.node(late, late['Id'] + '.explicit.1')
        self.assertEqual(late['Nodes'][0]['Choices'][1]['Next'], slot['Id'])
        self.assertEqual(slot['Choices'][0]['Next'], 'morning_after')
        self.assertIn(route.TEST, route.DERIVED[route.LATE_COMMITTED][0])
        for scene in (late, native):
            self.assertEqual(len(scene['Nodes']), 3 if scene is late else 1)
            self.assertIsNone(scene['Nodes'][0]['Choices'][0]['Next'])
            self.assertEqual(scene['Nodes'][0]['Choices'][0]['Set'], [])
            self.assertIn('sacrifice', scene['Forbids'])
            self.assertEqual(scene['ForbidOverrides']['sacrifice'], 'trickster.commander_back')


if __name__ == '__main__':
    unittest.main()
