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
                flags.update((flag for flag, played in ((folios.KISSED_EARLY, kissed), (folios.BITTEN, bitten)) if played))
                expected = 'receipt_kiss' if kissed else 'receipt_bite' if bitten else 'receipt_scribe'
                self.assertEqual(self.dispatch(scene, 'decides', flags), expected)
                self.assertEqual(self.dispatch(scene, expected, flags), 'variable')
                for loss in (route.UNREMEMBERED, route.RECREATED):
                    self.assertEqual(self.dispatch(scene, 'decides', flags | {loss}), 'receipt_scribe')
            for ident in ('receipt_kiss', 'receipt_bite', 'receipt_scribe'):
                self.assertFalse(any((route.COMMITTED in c['Set'] for c in self.node(scene, ident)['Choices'])))
            _, _, ordered_answer_1, *_ = self.node(scene, 'variable')['Choices']
            refusal = ordered_answer_1
            self.assertTrue({route.REFUSED, route.CLOSED} <= set(refusal['Set']))
            _, _, _, ordered_answer_2, *_ = self.node(scene, 'variable')['Choices']
            self.assertEqual(ordered_answer_2['Next'], 'postponed')

    def test_control_then_postponement_does_not_report_a_bite(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = self.scene(folios.TEETH + suffix)
            _, ordered_answer_3, *_ = self.node(scene, 'kiss')['Choices']
            control = ordered_answer_3
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
            ordered_answer_4, *_ = self.node(scene, 'watch')['Choices']
            legacy_exit = ordered_answer_4
            ordered_answer_5, *_ = slot['Choices']
            slot_exit = ordered_answer_5
            for key in ('Set', 'Next', 'Abort', 'Requires'):
                self.assertEqual(legacy_exit.get(key), slot_exit.get(key))
            self.assertNotIn(route.COMMITTED, slot_exit['Set'])
            self.assertFalse(slot.get('Paragraphs'))

    def test_late_first_night_is_only_in_supplement_with_legacy_exit(self):
        late = self.scene(route.P + 'epilogue.commit')
        native = next((s for s in route.NATIVE_ENDING_SCENES if s['Id'] == route.P + 'epilogue.native_commit'))
        slot = self.node(late, late['Id'] + '.explicit.1')
        _, ordered_answer_6, *_ = late['Nodes'][0]['Choices']
        self.assertEqual(ordered_answer_6['Next'], slot['Id'])
        ordered_answer_7, *_ = slot['Choices']
        self.assertEqual(ordered_answer_7['Next'], 'morning_after')
        self.assertIn(route.TEST, route.DERIVED[route.LATE_COMMITTED][0])
        for scene in (late, native):
            self.assertEqual([n['Id'] for n in scene['Nodes']],
                             ['page', late['Id'] + '.explicit.1', 'morning_after']
                             if scene is late else ['page'])
            ordered_answer_8, *_ = scene['Nodes'][0]['Choices']
            self.assertIsNone(ordered_answer_8['Next'])
            ordered_answer_9, *_ = scene['Nodes'][0]['Choices']
            self.assertEqual(ordered_answer_9['Set'], [])
            self.assertIn('sacrifice', scene['Forbids'])
            self.assertEqual(scene['ForbidOverrides']['sacrifice'], 'trickster.commander_back')
if __name__ == '__main__':
    unittest.main()
