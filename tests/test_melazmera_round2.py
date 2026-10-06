"""Route-local regressions for the round-two historical branches and receipts."""
import copy
import itertools
import unittest

from storylines import melazmera_trickster as route
from storylines import melazmera_hoard as visits


class MelazmeraRoundTwoTests(unittest.TestCase):
    def setUp(self):
        self.scenes = {s['Id']: copy.deepcopy(s) for s in route.SCENES + visits.SCENES}

    def node(self, scene, node):
        return next(n for n in self.scenes[route.M + scene]['Nodes'] if n['Id'] == node)

    def available(self, spec, flags):
        def has(key):
            if key.startswith('!'):
                return not has(key[1:])
            if key in route.DERIVED:
                if key == route.HERD_PENDING and route.HERD_SETTLED in flags:
                    return False
                return any(all(has(k) for k in group) for group in route.DERIVED[key])
            return key in flags
        return (all(has(k) for k in spec.get('Requires', []))
                and all(not has(k) or (k in spec.get('ForbidOverrides', {})
                                      and has(spec['ForbidOverrides'][k]))
                        for k in spec.get('Forbids', [])))

    def choices(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices']
                if self.available(c, flags)]

    def test_each_positive_voyage_selects_one_history_in_every_meeting(self):
        histories = [({route.ATE}, 'crew_ate'), ({route.HARPOONED}, 'crew_harpoon'),
                     ({route.CREVICE}, 'crew_missed'), ({route.SCREAM}, 'crew_scream'),
                     ({route.CAPTURED}, 'crew_captured'), (set(), 'crew_unknown')]
        for scene, (flags, expected) in itertools.product(
                ['ch4.hunt', 'ch4.hunt_found', 'ch5.hunt_window'], histories):
            with self.subTest(scene=scene, flags=flags):
                self.assertEqual([expected], [c['Next'] for c in self.choices(scene, 'crew', flags)])
                claims = self.node(scene, 'name')['Choices']
                self.assertEqual(route.CREVICE in flags,
                                 self.available(claims[2], flags))

    def test_independent_disguises_have_four_unambiguous_visual_paths(self):
        for real, bait in itertools.product([False, True], repeat=2):
            flags = {k for k, present in [(route.LIFTED, real), (route.LIFTED_B, bait)] if present}
            flags.add(route.PLAN)
            node = 'start'
            visited = []
            while node != 'ring':
                visited.append(node)
                answers = self.choices('ch4.salt', node, flags)
                self.assertEqual(1, len(answers), (real, bait, node))
                node = answers[0]['Next']
            self.assertIn('salt_real' if real else 'salt_rocks', visited)
            self.assertIn('salt_bare_bait' if bait else 'salt_shiny_bait', visited)

    def test_cattle_debt_survives_failed_payment_then_settles_once(self):
        flags = {'trickster.ever', route.MESSAGE}
        debt = self.node('ch5.hunger', 'forbid_after')
        flags.update(debt['EnterSet'])
        scene = self.scenes[route.M + 'ch5.hunger']
        self.assertTrue(self.available(scene, flags))
        self.assertEqual(['forbid_after'], [c['Next'] for c in self.choices('ch5.hunger', 'start', flags)])
        for favors, answer in itertools.product([0, 49, 50], debt['Choices']):
            history = flags.copy()
            cost = -answer['Crusade']['Amount']
            if favors >= cost:
                history.update(answer['Set'])
                self.assertEqual(0, favors - cost)
                self.assertFalse(self.available(scene, history))
            else:
                self.assertIn(route.FED_HERD, history)
                self.assertNotIn(route.HERD_SETTLED, history)
                self.assertTrue(self.available(scene, history))

    def test_inquiry_records_only_the_players_actual_answer(self):
        choices = self.choices('beat.inquisitor', 'after_mine', set())
        self.assertEqual(['inquiry_lie', 'inquiry_admit', 'inquiry_refuse'], [c['Next'] for c in choices])
        for c in choices:
            receipt = self.node('beat.inquisitor', c['Next'])['Choices'][0]['Set']
            self.assertIn(route.M + 'beat.inquisitor_reported', receipt)
            self.assertEqual(c['Next'] == 'inquiry_lie', route.M + 'beat.inquisitor_lied' in receipt)

    def test_old_paid_herd_save_is_not_charged_again(self):
        flags = {'trickster.ever', route.MESSAGE, route.FED, route.FED_HERD}
        self.assertFalse(self.available(self.scenes[route.M + 'ch5.hunger'], flags))
        paragraphs = self.node('epilogue.together', 'page')['Paragraphs']
        self.assertTrue(any('never found out where they had gone' in p['Text']
                            and self.available(p, flags) for p in paragraphs))

    def test_queen_withholding_is_not_truth_or_survival(self):
        history = {route.M + 'queen_refused_crown', route.M + 'queen_withheld'}
        self.assertEqual(['withheld'], [c['Next'] for c in self.choices('beat.queen', 'start', history)])
        history.add('melazmera.fq_attacked')
        history.add(route.QUEEN_TURNED)
        self.assertEqual(['fought'], [c['Next'] for c in self.choices('beat.queen', 'start', history)])
        old = self.node('beat.queen', 'start')['Choices'][:7]
        self.assertEqual(['turned', 'fought', 'withdrew', 'crowned', 'denied', 'promised', 'plain'],
                         [c['Next'] for c in old])

    def test_bargains_check_current_power_before_the_offer(self):
        for suffix, receipt in [('commit.stone', route.FED), ('hunt.shared', route.DECLINED)]:
            scene = self.scenes[route.M + suffix]
            history = {'trickster.ever', receipt}
            self.assertFalse(self.available(scene, history))
            history.add('trickster.now')
            self.assertTrue(self.available(scene, history))

    def test_one_effectless_slot_connects_both_old_answers_to_morning(self):
        slot = route.M + 'visit.heap.explicit.1'
        self.assertEqual([slot, slot], [c['Next'] for c in self.node('visit.heap', 'cut')['Choices']])
        continuation = self.node('visit.heap', slot)['Choices'][0]
        self.assertEqual('morning', continuation['Next'])
        self.assertEqual([], continuation['Set'])
        self.assertEqual([], continuation['Requires'])
        self.assertIn('YOU HAVE YOUR BELT', self.node('visit.heap', 'home')['Text'])

    def test_closed_refused_and_departed_do_not_receive_romantic_mourning(self):
        scene = self.scenes[route.M + 'epilogue.mourned']
        flags = {'trickster.ever', route.RETURNED, 'sacrifice'}
        self.assertTrue(self.available(scene, flags))
        for revoker in [route.CLOSED, route.LEFT_FREE, route.DECLINED, route.DEAD, 'trickster.commander_back']:
            self.assertFalse(self.available(scene, flags | {revoker}), revoker)
        self.assertTrue(self.available(scene, flags | {route.DECLINED, route.COMMITTED}))


if __name__ == '__main__':
    unittest.main()
