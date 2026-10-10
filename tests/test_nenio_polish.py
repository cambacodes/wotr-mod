"""Reviewed Nenio callbacks: native observations, overlapping branches, saved targets."""
import itertools
import unittest
from storylines import nenio_folios as folios, nenio_trickster as route

class NenioPolishTests(unittest.TestCase):

    @staticmethod
    def scene(scene_id):
        return next(s for s in (*route.SCENES, *folios.SCENES) if s['Id'] == scene_id)

    @staticmethod
    def node(scene, node_id):
        return next(n for n in scene['Nodes'] if n['Id'] == node_id)

    @staticmethod
    def available(choice, flags):
        return set(choice.get('Requires', ())) <= flags and not set(choice.get('Forbids', ())) & flags

    def dispatch(self, scene, node_id, flags):
        choices = self.node(scene, node_id)['Choices']
        selected = [c for c in choices if self.available(c, flags)]
        selected_answer, = selected
        self.assertIn(selected_answer['Next'], {n['Id'] for n in scene['Nodes']} | {None})
        ordered_answer_1, *_ = selected
        return ordered_answer_1['Next']

    @staticmethod
    def observations(cues, flags=()):
        result = set(flags)
        for key, witnesses in route.NATIVE['SeenCues'].items():
            if set(witnesses) & set(cues):
                result.add(key)
        return result

    def memory_histories(self):
        dead = self.scene(route.P + 'dead.the_price_recreated')
        killed = self.scene(route.P + 'killed.recreated')
        ordered_answer_2, *_ = self.node(dead, 'terms')['Choices']
        paid_dead = set(ordered_answer_2['Set'])
        ordered_answer_3, *_ = self.node(killed, 'terms')['Choices']
        paid_killed = set(ordered_answer_3['Set'])
        return [set(), paid_dead, paid_killed, paid_dead | paid_killed]

    def test_optional_poetry_and_gossip_dispatch_all_twins(self):
        for suffix in ('', '_visitor', '_arcade'):
            rhyme = self.scene(folios.RHYMES + suffix)
            gossip = self.scene(folios.SLIPS + suffix)
            for memory in self.memory_histories():
                compatible = not {route.RECREATED, route.UNREMEMBERED} & memory
                for poetry in (False, True):
                    cues = ['3f9250674b4b8964583cd43c1dc2b7c4'] if poetry else []
                    flags = self.observations(cues, memory)
                    expected = 'poetry_again' if poetry and compatible else 'poetry_first'
                    self.assertEqual(self.dispatch(rhyme, 'open', flags), expected)
                for prepared, universal in itertools.product((False, True), repeat=2):
                    cues = []
                    if prepared:
                        cues.append('1c227b4093d74df489234b8e541a8b3e')
                    if universal:
                        cues.append('54ce8fab48409ca4eac54c02e95c6c71')
                    flags = self.observations(cues, memory)
                    expected = 'gossip_old' if compatible and universal else 'gossip_prepared' if compatible and prepared else 'gossip_new'
                    self.assertEqual(self.dispatch(gossip, 'open', flags), expected)

    def test_recruitment_safety_precedence_and_memory(self):
        for suffix in ('', '_visitor', '_arcade'):
            scene = self.scene(folios.INQUISITORS + suffix)
            for memory in self.memory_histories():
                compatible = not {route.RECREATED, route.UNREMEMBERED} & memory
                for safe, rejected in itertools.product((False, True), repeat=2):
                    cues = (['2cf370e2b4cdba2418ce7473ea858764'] if safe else [])
                    cues += ['8735d2087d3723b47b3692ea9dfa16df'] if rejected else []
                    flags = self.observations(cues, memory)
                    opening = self.dispatch(scene, 'open', flags)
                    self.assertEqual(opening, 'remembered_open' if compatible else 'records_open')
                    expected = 'remember' if compatible and safe else 'remember_sent' if compatible and rejected else 'remember_new'
                    self.assertEqual(self.dispatch(scene, 'run', flags), expected)

    def test_point_five_overlap_comes_from_native_cues(self):
        scene = self.scene(folios.POINT_FIVE)
        # Each native observation is optional. Tongue/credit also prove drawing.
        cues = ['9684eade0e1c5f043a3c780b1f644de5', 'caecc9b04ee4bb940a165251c7b6054c',
                'c1390044127cbbf428e7fb96cde940dc', 'b95a7017fd1cc6b40a23b9e7e9c54c88']
        for seen in itertools.product((False, True), repeat=4):
            observed = [cue for cue, yes in zip(cues, seen) if yes]
            for memory in self.memory_histories():
                flags = self.observations(observed, memory | {'trickster.ever'})
                drawing = route.FRIEND_SKETCH in flags
                tongue = route.FRIEND_TONGUE in flags
                refused = route.FRIEND_REFUSED in flags
                compatible = not {route.RECREATED, route.UNREMEMBERED} & flags
                self.assertEqual(self.dispatch(scene, 'open', flags), 'review_retained' if compatible else 'review_new')
                expected = ('result_refused_tongue' if refused and tongue else
                            'result_refused_drawing' if refused and drawing else
                            'result_refused' if refused else 'result_tongue' if tongue else
                            'result_drawing' if drawing else 'result_unknown') if compatible else 'result_unknown'
                self.assertEqual(self.dispatch(scene, 'five', flags), expected)
                self.assertEqual(self.dispatch(scene, 'end', flags), 'end_drawing' if compatible and drawing else 'end_new')
                if compatible and drawing:
                    self.assertEqual(self.dispatch(scene, 'sketch', flags), 'credit' if route.FRIEND_CREDIT in flags else 'drawing')

    def test_night_annotations_without_borrowed_memories(self):
        for suffix in ('', '_visitor', '_arcade'):
            night = self.scene(route.P + 'night' + suffix)
            for memory in self.memory_histories():
                for concluded, sketch, refused in itertools.product((False, True), repeat=3):
                    flags = memory | {'trickster.ever'}
                    flags |= {flag for flag, yes in [(route.FRIEND_DONE, concluded), (route.FRIEND_SKETCH, sketch), (route.FRIEND_REFUSED, refused)] if yes}
                    compatible = not {route.RECREATED, route.UNREMEMBERED} & flags
                    expected = ('friend_declined' if refused else 'friend_drawing' if sketch else 'friend_uncertain') if compatible and concluded else 'begin'
                    self.assertEqual(self.dispatch(night, 'friend_note', flags), expected)
            self.assertIn(route.KENABRES_PENDING, night['Forbids'])

    def test_replication_saved_targets_retained_and_new_departure_terminal(self):
        for suffix in ('', '_visitor', '_arcade'):
            original = self.scene(route.P + 'commit.replication' + suffix)
            self.assertTrue({'morning', 'yes', 'yes_kiss', 'refused'} <= {n['Id'] for n in original['Nodes']})
            ordered_answer_4, *_ = self.node(original, 'night')['Choices']
            departure = ordered_answer_4
            self.assertIsNone(departure['Next'])
            self.assertEqual(departure['Set'], [route.CONFESSED])
            result = self.scene(route.P + 'commit.replication_result' + suffix)
            self.assertEqual(result['DelayHours'], 24)
            for choice in self.node(result, 'morning')['Choices'][:2]:
                self.assertTrue({route.COMMITTED, route.FIRST_NIGHT, route.REPLICATED} <= set(choice['Set']))

    def test_riddle_telling_is_single_and_name_loss_requires_completed_filing(self):
        riddle = self.scene(route.P + 'taken.riddle')
        self.assertEqual(self.node(riddle, 'posed')['Id'], 'posed')
        self.assertTrue(self.node(riddle, 'posed')['Choices'])
        self.assertEqual(route.DERIVED[route.NAME_GONE], [[route.NAME_FILED]])
if __name__ == '__main__':
    unittest.main()
