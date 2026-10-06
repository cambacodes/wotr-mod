"""Devarra campaign witness and negative history forks; no fabricated romance."""
from copy import deepcopy
import itertools
import json
from pathlib import Path
import unittest

from storylines import devarra_tower as tower, devarra_trickster as spine
from storylines import devarra_round2 as r2


def visible(record, flags):
    return (all(key in flags for key in record.get('Requires', []))
            and not any(key in flags for key in record.get('Forbids', []))
            and all(any(key in flags for key in group)
                    for group in record.get('RequiresAnyGroups', [])))


class DevarraRoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': deepcopy(spine.SCENES + tower.SCENES)}
        tower.integrate(payload)
        cls.scenes = {s['Id']: s for s in payload['Scenes']}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def choices(self, scene, node, flags):
        return [c for c in self.node(scene, node)['Choices'] if visible(c, flags)]

    def take(self, scene, node, flags, index=0):
        options = self.choices(scene, node, flags)
        self.assertTrue(options, (scene, node, flags))
        choice = options[index]
        flags.update(choice.get('Set', []))
        return choice.get('Next')

    def test_campaign_witness_uses_played_choices_and_native_observations(self):
        flags = {'trickster', 'trickster.ever', tower.CH3}
        pact = r2.P + 'flight.pact'
        for node, next_node in [('cover', 'tariff'), ('tariff', 'fable'), ('fable', 'named'),
                                ('named', 'terms')]:
            self.assertEqual(self.take(pact, node, flags), next_node)
        self.take(pact, 'terms', flags)
        self.assertIn(spine.PACT, flags)
        self.assertNotIn(spine.COMMITTED, flags)
        # Real native escape then Deactivation; the errand amendment alone is not it.
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
        # Submission and climb are earned by their own answers, not a rescued dragon.
        tithe = r2.P + 'after.tithe'
        node = self.scenes[tithe]['Nodes'][0]['Id']
        for _ in range(20):
            node = self.take(tithe, node, flags)
            if node is None:
                break
        self.assertIn(spine.TESTED, flags)
        self.assertNotIn(spine.COMMITTED, flags)
        climb = r2.T + 'first_climb'
        node = 'start' if any(n['Id'] == 'start' for n in self.scenes[climb]['Nodes']) else self.scenes[climb]['Nodes'][0]['Id']
        # Default is the peaceful sitting answer, preserving her territory.
        for _ in range(15):
            node = self.take(climb, node, flags)
            if node is None:
                break
        self.assertIn(tower.CLIMBED, flags)
        lair = r2.P + 'after.lair'
        node = 'climb'
        while node != 'terms':
            node = self.take(lair, node, flags)
        # Select the offered arm, keeping refusal and postponement selectable.
        accepted = next(c for c in self.choices(lair, node, flags) if spine.COMMITTED in c['Set'])
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
        # The public wager and roof are real visits, then the actual Ch4 voyage.
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
        flags.add(tower.VOYAGE_SEEN)  # The native AirAdventures dialog actually began.
        scene = r2.T + 'wrong_sky'
        node = self.scenes[scene]['Nodes'][0]['Id']
        while node is not None:
            node = self.take(scene, node, flags)
        self.assertIn(tower.SKY_FEAR, flags)
        scene = r2.T + 'after_the_abyss'
        self.assertIn(tower.CLIMBED_CH3, self.scenes[scene]['Requires'])
        self.take(scene, 'climb', flags, 2)  # The kept voyage account, actually offered.
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
            self.assertEqual(len(options), 1, flags)
            self.assertTrue(self.choices(scene, 'clutch', flags), flags)
            if 'eggs.destroyed' in flags and not flags & {'eggs.omelet', 'eggs.druids'}:
                self.assertEqual(options[0]['Next'], 'said_destroyed')
                self.assertFalse(any(c['Next'] == 'warm' for c in self.choices(scene, 'clutch', flags)))

    def test_native_destruction_causes_match_both_accounts(self):
        for cause, phrase in zip(r2.CAUSES, ('smashed', 'order', 'wrong', 'watch')):
            flags = {'eggs.project', 'eggs.destroyed', cause, spine.FLOWN}
            for scene, source in ((r2.P + 'flight.eggs', 'which_eggs'), (r2.T + 'smallest_egg', 'climb_free')):
                options = self.choices(scene, source, flags)
                self.assertEqual(len(options), 1, (scene, cause))
                text = self.node(scene, options[0]['Next'])['Text'].lower()
                self.assertTrue(phrase in text or (phrase == 'watch' and 'waited to see' in text), text)
                self.assertNotIn('in your vault', text)
            self.assertTrue(self.choices(r2.P + 'flight.eggs', 'clutch', flags))

    def test_project_without_deactivation_gets_no_password_credit(self):
        scene = r2.P + 'flight.eggs'
        flags = {'eggs.project', spine.FLOWN}
        target = self.take(scene, 'which_eggs', flags)
        self.assertIn('broke the stone', self.node(scene, target)['Text'])
        self.assertNotIn('cut the leash', self.node(scene, target)['Text'])

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
            choices = self.choices(scene, 'start', flags)
            self.assertEqual(len(choices), 1, flags)
            text = self.node(scene, choices[0]['Next'])['Text']
            if north:
                self.assertIn('north', text)
                self.assertNotIn('kiln', text)
            elif not hatched:
                self.assertIn('inside its shell', text)

    def test_greybor_current_state_and_flight_recollection(self):
        scene = r2.T + 'the_dwarf'
        for state in (set(), {'greybor.dead'}, {'greybor.kicked_out'}, {'greybor.dead', 'greybor.kicked_out'}):
            flags = state | {spine.FLOWN}
            choices = self.choices(scene, 'climb', flags)
            self.assertTrue(choices)
            self.assertFalse(any(c['Next'] == 'me' for c in choices))
            if state:
                self.assertFalse(any(c['Next'] == 'protect' for c in choices))
            for id in ('protect', 'me', 'me_free', 'rate'):
                exits = self.choices(scene, id, flags)
                self.assertEqual(len(exits), 1)
                target = exits[0]['Next']
                self.assertEqual(target, 'end_dead' if 'greybor.dead' in flags else
                                 'end_gone' if 'greybor.kicked_out' in flags else 'end')

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
        for flags in ({tower.VAULT_OPENED, 'eggs.druids'}, {r2.EGG_BILL, r2.NORTH}, {r2.EGG_BILL}):
            text = '\n'.join(p['Text'] for p in page['Paragraphs'] if visible(p, flags))
            if 'eggs.druids' in flags:
                self.assertNotIn('Drezen vault hatched', text)
                self.assertIn('carried east', text)
            if r2.NORTH in flags:
                self.assertIn('where she grew', text)
                self.assertNotIn('by the east wall', text)
        # Supplied slot last lines agree byte-for-byte with their default insertion.
        for path in (Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/devarra').glob('*.json'):
            brief = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(brief['last_line'][3:], brief['default_text'].removeprefix('{n}').removesuffix('{/n}'))


if __name__ == '__main__':
    unittest.main()
