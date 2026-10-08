"""Rendered history coverage for both runaway meeting hosts (R4 D03-D09)."""
import itertools
import unittest

from storylines import nurah_trickster as route


class NurahRunawayHistoryTests(unittest.TestCase):
    def walks(self, scene, history):
        nodes = {node['Id']: node for node in scene['Nodes']}
        pending = [('start', frozenset(history), ())]
        endings = []
        while pending:
            nid, flags, pages = pending.pop()
            node = nodes[nid]
            pages += (node['Text'],)
            choices = [c for c in node['Choices']
                       if set(c['Requires']) <= flags and not set(c['Forbids']) & flags]
            self.assertTrue(choices, (scene['Id'], nid, sorted(flags)))
            for choice in choices:
                next_flags = flags | frozenset(choice['Set'])
                if choice['Next']:
                    pending.append((choice['Next'], next_flags, pages))
                else:
                    endings.append((next_flags, '\n'.join(pages)))
        return endings

    def test_pardon_release_witness_does_not_earn_a_dedication(self):
        scenes = {s['Id']: s for s in route.SCENES}
        history = {'trickster', 'trickster.ever', 'trickster.now', 'nurah.prison'}
        for sid, nid, index in (
            ('nurah.trickster.prison.pardon', 'read', 0),
            ('nurah.trickster.prison.night_out', 'start', 2),
            ('nurah.trickster.prison.proofs', 'start', 1),
        ):
            node = next(n for n in scenes[sid]['Nodes'] if n['Id'] == nid)
            history.update(node['Choices'][index]['Set'])
        # Native Answer_0056 frees her and starts NuraRanOffAfterDrezen.
        history.discard('nurah.prison')
        history.add(route.RAN_OFF)
        self.assertNotIn(route.GHOST, history)
        self.assertTrue({route.LEDGER, route.ACCEPTED, route.PROOFS} <= history)
        for suffix in ('', '_night'):
            scene = scenes['nurah.trickster.ran_off.terms' + suffix]
            witness = history | ({'nurah.presence.failed'} if suffix else set())
            self.assertTrue(set(scene['Requires']) <= witness)
            self.assertFalse(set(scene['Forbids']) & witness)
            outcomes = self.walks(scene, witness)
            self.assertTrue(any(route.COMPLETE in f for f, _ in outcomes))
            for _, prose in outcomes:
                self.assertNotIn('dedication', prose)
                self.assertNotIn('You forged me', prose)
                self.assertIn('My corrections go in the book', prose)

    def test_both_hosts_all_proof_forgery_and_native_appearance_histories(self):
        for suffix, ghost, signed, evil, appearance in itertools.product(
                ('', '_night'), (False, True), (False, True), (False, True),
                (None, route.PULURA_WINK, route.PULURA_BETRAYAL)):
            scene = next(s for s in route.SCENES
                         if s['Id'] == 'nurah.trickster.ran_off.terms' + suffix)
            history = {route.RAN_OFF, route.ACCEPTED, route.PROOFS, route.LEDGER,
                       'trickster', 'trickster.ever', 'trickster.now'}
            history.update(k for k, active in ((route.GHOST, ghost),
                           (route.SIGNED, signed), (route.EVIL, evil)) if active)
            if appearance:
                history.add(appearance)
            outcomes = self.walks(scene, history)
            self.assertTrue(any(route.COMPLETE in f for f, _ in outcomes))
            self.assertTrue(any(route.BOOK in f and route.COMPLETE not in f
                                for f, _ in outcomes))
            self.assertTrue(any(route.CLOSED in f for f, _ in outcomes))
            for flags, prose in outcomes:
                if not ghost:
                    self.assertNotIn('dedication', prose)
                    self.assertNotIn('You forged me', prose)
                else:
                    self.assertIn('your forged dedication', prose)
                if appearance == route.PULURA_WINK:
                    self.assertIn('scratches out the word "Master"', prose)
                    self.assertNotIn('the people we gutted', prose)
                elif appearance == route.PULURA_BETRAYAL:
                    self.assertIn('the people we gutted', prose)
                    self.assertNotIn('scratches out the word "Master"', prose)
                    if route.COMPLETE in flags:
                        self.assertIn('seen my hands bloody', prose)
                else:
                    self.assertNotIn('Mutasafen', prose)
                    self.assertNotIn('Pulura', prose)

    def test_native_appearance_keys_bind_seen_cues_without_touching_native_state(self):
        payload = {'Relationships': {'nurah': {'Guidance': ''}}, 'Scenes': []}
        route.integrate(payload)
        self.assertEqual(payload['SeenCues'][route.PULURA_BETRAYAL],
                         ['76f9bab08efef874eb2837acd7ed31e8'])
        self.assertEqual(payload['SeenCues'][route.PULURA_WINK],
                         ['e5c3183a2c6252f4ebe3551db6dfd9ed'])
        self.assertNotIn('StartableEtudes', payload)

    def test_recollection_variants_introduce_no_hard_player_text_findings(self):
        from tools import player_text_baseline, player_text_lint
        story = {'Scenes': route.SCENES}
        result = player_text_lint.check(story)
        self.assertEqual(player_text_baseline.new_findings(
            story, result['review'], therapy_counts=result['therapy_counts']), [])


if __name__ == '__main__':
    unittest.main()
