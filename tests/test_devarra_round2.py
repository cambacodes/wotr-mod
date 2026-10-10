"""Devarra campaign witness and negative history forks; no fabricated romance."""
from copy import deepcopy
import itertools
import json
from pathlib import Path
import unittest
from storylines import devarra_tower as tower, devarra_trickster as spine
from storylines import devarra_round2 as r2

def visible(record, flags):
    return all((key in flags for key in record.get('Requires', []))) and (not any((key in flags for key in record.get('Forbids', [])))) and all((any((key in flags for key in group)) for group in record.get('RequiresAnyGroups', [])))

class DevarraRoundTwoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': deepcopy(spine.SCENES + tower.SCENES)}
        tower.integrate(payload)
        cls.scenes = {s['Id']: s for s in payload['Scenes']}

    def node(self, scene, node):
        return next((n for n in self.scenes[scene]['Nodes'] if n['Id'] == node))

    def choices(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices'] if visible(c, flags)]

    def take(self, scene, node, flags, index=0):
        options = self.choices(scene, node, flags)
        if not options:
            raise AssertionError('Invalid replay traversal')
        for ordinal, answer in enumerate(options):
            if ordinal == index:
                choice = answer
                break
        else:
            raise AssertionError('Replay answer is absent')
        flags.update(choice.get('Set', []))
        return choice.get('Next')

    def test_campaign_witness_uses_played_choices_and_native_observations(self):
        flags = {'trickster', 'trickster.ever', tower.CH3}
        pact = r2.P + 'flight.pact'
        for node, next_node in [('cover', 'tariff'), ('tariff', 'fable'), ('fable', 'named'), ('named', 'terms')]:
            self.assertEqual(self.take(pact, node, flags), next_node)
        self.take(pact, 'terms', flags)
        self.assertIn(spine.PACT, flags)
        self.assertNotIn(spine.COMMITTED, flags)
        flags.update((spine.ESCAPE_SEEN, 'devarra.golems_met.latched'))
        flags.add(spine.FLOWN)
        self.take(r2.P + 'flight.leash', 'report', flags)
        self.assertNotIn(spine.LEASH, flags)
        flags.update(('devarra.golems_deactivated', spine.LEASH))
        self.take(r2.P + 'flight.clutch_left', 'left', flags)
        visit = r2.P + 'flight.eggs'
        self.assertEqual(self.scenes[visit]['Kind'], 'visit')
        self.assertEqual(self.scenes[visit]['DelayHours'], 48)
        node = 'road'
        while node != 'clutch':
            node = self.take(visit, node, flags)
        self.take(visit, 'clutch', flags)
        self.assertIn(spine.RETURNED, flags)
        self.assertNotIn(spine.COMMITTED, flags)
        tithe = r2.P + 'after.tithe'
        node = self.scenes[tithe]['Nodes'][0]['Id']
        for _ in range(20):
            node = self.take(tithe, node, flags)
            if node is None:
                break
        self.assertIn(spine.TESTED, flags)
        self.assertNotIn(spine.COMMITTED, flags)
        climb = r2.T + 'first_climb'
        node = 'start' if any((n['Id'] == 'start' for n in self.scenes[climb]['Nodes'])) else self.scenes[climb]['Nodes'][0]['Id']
        for _ in range(15):
            node = self.take(climb, node, flags)
            if node is None:
                break
        self.assertIn(tower.CLIMBED, flags)
        lair = r2.P + 'after.lair'
        node = 'climb'
        while node != 'terms':
            node = self.take(lair, node, flags)
        accepted = next((c for c in self.choices(lair, node, flags) if spine.COMMITTED in c['Set']))
        flags.update(accepted['Set'])
        self.assertIn(spine.COMMITTED, flags)
        self.assertIn(spine.BITTEN, flags)
        first = r2.T + 'first_bite'
        node = 'start'
        visited = []
        while node is not None:
            visited.append(node)
            node = self.take(first, node, flags)
        self.assertIn(r2.T + 'first_bite.explicit.1', visited)
        self.assertIn('morning', visited)
        self.assertIn(tower.BITTEN_ONCE, flags)
        scene = r2.T + 'the_garrison_book'
        node = 'start'
        while node is not None:
            node = self.take(scene, node, flags)
        scene = r2.T + 'on_the_roof'
        node = 'start'
        while node is not None:
            node = self.take(scene, node, flags)
        self.assertIn(tower.ROOF, flags)
        self.assertIn(tower.CLIMBED_CH3, flags)
        flags.discard(tower.CH3)
        flags.add(tower.VOYAGE_SEEN)
        scene = r2.T + 'wrong_sky'
        node = self.scenes[scene]['Nodes'][0]['Id']
        while node is not None:
            node = self.take(scene, node, flags)
        self.assertIn(tower.SKY_FEAR, flags)
        scene = r2.T + 'after_the_abyss'
        self.assertIn(tower.CLIMBED_CH3, self.scenes[scene]['Requires'])
        self.take(scene, 'climb', flags, 2)
        self.take(scene, 'sky_fear', flags)
        self.take(scene, 'end', flags)
        self.take(scene, 'what', flags)
        self.assertIn(tower.ABYSS_BACK, flags)
        scene = r2.T + 'before_the_end'
        self.assertFalse(visible(self.scenes[scene], flags))
        flags.add('coronation.seen')
        self.assertTrue(visible(self.scenes[scene], flags))
        node = 'start'
        while node is not None:
            node = self.take(scene, node, flags)
        self.assertIn(tower.LAST_NIGHT, flags)

    def test_all_accumulated_egg_fates_have_one_dispatch_and_answer(self):
        scene = r2.P + 'flight.eggs'
        for bits in itertools.product((False, True), repeat=4):
            flags = {key for key, bit in zip((*r2.TERMINAL, 'eggs.project'), bits) if bit}
            flags.add(spine.LEASH)
            options = self.choices(scene, 'which_eggs', flags)
            dispatch_1, = options
            self.assertTrue(self.choices(scene, 'clutch', flags), flags)
            if 'eggs.destroyed' in flags and (not flags & {'eggs.omelet', 'eggs.druids'}):
                answer_in_order_1, *answer_in_order_1_following = options
                self.assertEqual(answer_in_order_1['Next'], 'said_destroyed')
                self.assertFalse(any((c['Next'] == 'warm' for c in self.choices(scene, 'clutch', flags))))

    def test_native_destruction_causes_match_both_accounts(self):
        for ordinal, cause in enumerate(r2.CAUSES, 1):
            flags = {'eggs.project', 'eggs.destroyed', cause, spine.FLOWN}
            for scene, source, prefix in ((r2.P + 'flight.eggs', 'which_eggs', 'said_destroyed.'), (r2.T + 'smallest_egg', 'climb_free', 'destroyed.')):
                options = self.choices(scene, source, flags)
                self.assertEqual([prefix + str(ordinal)], [c['Next'] for c in options])
                self.assertTrue(all((cause in c['Requires'] for c in options)))
            self.assertTrue(self.choices(r2.P + 'flight.eggs', 'clutch', flags))

    def test_project_without_deactivation_gets_no_password_credit(self):
        scene = r2.P + 'flight.eggs'
        flags = {'eggs.project', spine.FLOWN}
        self.assertEqual(self.take(scene, 'which_eggs', flags), 'said_project_combat')
        self.assertNotIn(spine.LEASH, flags)
        flags.add(spine.LEASH)
        self.assertEqual(self.take(scene, 'which_eggs', flags), 'said_project')

    def test_missing_life_is_billed_before_keeper_discovery_and_after_later_taking(self):
        for fate in ('eggs.omelet', 'eggs.druids', 'eggs.project', 'eggs.destroyed', spine.CLUTCH_LEFT, spine.COLLECTED):
            flags = {r2.EGG_OWED, fate, spine.LEASH}
            self.take(r2.P + 'flight.eggs', 'count', flags)
            self.assertIn(r2.EGG_BILL, flags)
            self.assertNotIn(tower.TWELFTH_TOLD, flags)
        short = r2.T + 'one_short'
        self.assertIn(r2.EGG_OWED, self.scenes[short]['Requires'])
        for index in range(3):
            flags = {spine.FLOWN, r2.EGG_OWED}
            self.take(short, 'climb_free', flags, index)
            self.assertIn(r2.EGG_BILL, flags)

    def test_keeper_hatch_and_departure_dispatch_are_exclusive(self):
        scene = r2.T + 'smallest_egg'
        for flight, hatched, north in itertools.product((False, True), repeat=3):
            flags = {key for key, bit in zip((spine.FLOWN, r2.HATCHED, r2.NORTH), (flight, hatched, north)) if bit}
            expected = 'climb_north' if north else ('climb_free' if flight else 'climb') + ('' if hatched else '_unhatched')
            self.assertEqual([expected], [c['Next'] for c in self.choices(scene, 'start', flags)])

    def test_greybor_current_state_and_flight_recollection(self):
        scene = r2.T + 'the_dwarf'
        for state in (set(), {'greybor.dead'}, {'greybor.kicked_out'}, {'greybor.dead', 'greybor.kicked_out'}):
            flags = state | {spine.FLOWN}
            choices = self.choices(scene, 'climb', flags)
            self.assertTrue(choices)
            self.assertFalse(any((c['Next'] == 'me' for c in choices)))
            if state:
                self.assertFalse(any((c['Next'] == 'protect' for c in choices)))
            for id in ('protect', 'me', 'me_free', 'rate'):
                exits = self.choices(scene, id, flags)
                dispatch_2, = exits
                answer_in_order_2, *answer_in_order_2_following = exits
                target = answer_in_order_2['Next']
                self.assertEqual(target, 'end_dead' if 'greybor.dead' in flags else 'end_gone' if 'greybor.kicked_out' in flags else 'end')

    def test_second_ask_interest_is_collected_before_first_tariff(self):
        flags = {spine.FLOWN, spine.LEFT_HUNGRY}
        self.take(r2.T + 'back_up_the_mountain', 'her', flags)
        self.assertIn(r2.INTEREST, flags)
        scene = r2.T + 'first_bite'
        self.assertEqual(self.take(scene, 'ridge', flags), 'interest_story')
        self.take(scene, 'interest_story', flags)
        self.assertIn(r2.INTEREST_PAID, flags)
        self.assertEqual(self.take(scene, 'interest_collected', flags), 'inside_free')

    def test_wagers_have_distinct_roof_returns_and_legacy_fallback(self):
        for reported in (False, True):
            flags = set()
            scene = r2.T + 'the_garrison_book'
            node = self.take(scene, 'tell_her', flags, 0 if reported else 1)
            self.take(scene, node, flags)
            self.assertIn(r2.REPORTED if reported else r2.UNREPORTED, flags)
            roof = self.take(r2.T + 'on_the_roof', 'roof', flags)
            self.assertEqual(roof, 'her_closed' if reported else 'her_unreported')
        self.assertEqual(self.take(r2.T + 'on_the_roof', 'roof', set()), 'her')

    def test_farewell_and_epilogue_current_fates(self):
        farewell = self.scenes[r2.T + 'before_the_end']
        self.assertIn('coronation.seen', farewell['Requires'])
        self.assertEqual(farewell['DelayHours'], 0)
        page = self.node(r2.P + 'epilogue.woken', 'page')
        vault = next((p for p in page['Paragraphs'] if p.get('Requires') == [tower.VAULT_OPENED]))
        self.assertTrue({'eggs.omelet', 'eggs.destroyed', 'eggs.druids'} <= set(vault['Forbids']))
        keeper = [p for p in page['Paragraphs'] if r2.EGG_BILL in p.get('Requires', ()) and 'devarra.lastcall.called' not in p.get('Requires', ()) + p.get('Forbids', ())]
        for flags, expected in (({r2.EGG_BILL, r2.NORTH}, [r2.EGG_BILL, r2.NORTH]), ({r2.EGG_BILL}, [r2.EGG_BILL]), ({r2.EGG_BILL, r2.HATCHED}, [r2.EGG_BILL, r2.HATCHED])):
            self.assertEqual([expected], [p['Requires'] for p in keeper if visible(p, flags)])
        slot = self.node(r2.T + 'first_bite', r2.T + 'first_bite.explicit.1')
        self.assertEqual(['morning'], [c['Next'] for c in slot['Choices']])
        self.assertEqual([[]], [c['Set'] for c in slot['Choices']])
if __name__ == '__main__':
    unittest.main()
