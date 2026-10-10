"""Partner terms: state, save destinations, and current-fate partitions."""
import copy
import json
from pathlib import Path
from itertools import product
import unittest
from itertools import zip_longest
from storylines import jerribeth, jerribeth_partner as route, jerribeth_trickster
from story_format import c, n
from tests.structure import without_prose

def allowed(record, flags):
    return (set(record.get("Requires", ())) <= flags
            and not set(record.get("Forbids", ())) & flags)

def walk(scene, flags, start=None):
    nodes = {n["Id"]: n for n in scene["Nodes"]}
    pending = [(start or scene["Nodes"][0]["Id"], frozenset(flags), frozenset())]
    visited, ends = set(), []
    while pending:
        node_id, held, path = pending.pop()
        if node_id in path:
            raise AssertionError("Dialogue cycle: " + node_id)
        if (node_id, held) in visited:
            continue
        visited.add((node_id, held))
        choices = [ch for ch in nodes[node_id]["Choices"] if allowed(ch, held)]
        if not choices:
            raise AssertionError("No answer: " + node_id)
        for choice in choices:
            state = held | frozenset(choice["Set"])
            if choice["Next"]:
                pending.append((choice["Next"], state, path | {node_id}))
            elif not choice.get("Abort"):
                ends.append(state)
    return visited, ends

class PartnerTermsTests(unittest.TestCase):

    def setUp(self):
        self.future = copy.deepcopy(next(s for s in jerribeth.SCENES if s["Id"] == "jerribeth.future"))
        self.before = copy.deepcopy(self.future)
        route.install_terms(self.future, {"future_entry"})

    def test_integrator_does_not_mutate_partner_discovery_templates(self):
        # Full assembly installs discovery into the legacy tenant-room template.
        # Reusing that object otherwise accumulates answers on every build.
        import expansion
        before = copy.deepcopy(jerribeth_trickster.IN_PERSON)
        expansion.make_expansion()
        self.assertEqual(without_prose(jerribeth_trickster.IN_PERSON), without_prose(before))

    def test_registry_uses_verified_readers_and_precommit_receipt(self):
        registry = json.loads(Path('tools/canon_partners.json').read_text(encoding='utf-8'))
        partner = next(e for e in registry['roster'] if e['relationship'] == 'jerribeth')['partners'][0]
        self.assertEqual(partner['acknowledgement_receipts'], [route.READY])
        bindings = {binding for fate in partner['native_fates']
                    for evidence in fate['evidence'] for binding in evidence.get('export_bindings', ())}
        self.assertTrue({'Etudes.' + key for key in route.ETUDES} <= bindings)
        states = {fate['state']: fate['when'] for fate in partner['native_fates']}
        self.assertEqual(states['dead'], [[route.DEAD]])
        self.assertIn('!' + route.DEAD, states['alive_chief_separated_by_judgment'][0])

    def test_every_current_fate_and_tenant_has_one_status_branch(self):
        for dead, chief, plant, returned in product((False, True), repeat=4):
            flags = {key for key, yes in zip((*route.FATES, route.RETURNED), (dead, chief, plant, returned)) if yes}
            choices = [fate for fate, guard in route.fate_guards().items() if allowed({'Requires': guard.get('requires', ()), 'Forbids': guard.get('forbids', ())}, flags)]
            selected_fate, = choices
            self.assertIn(selected_fate, route.fate_guards())
            if dead:
                self.assertEqual(choices, ['dead'])
            elif returned and plant and (not chief):
                self.assertEqual(choices, ['distant'])

    def test_all_commits_have_terms_and_single_stance_exclusive_is_refused(self):
        for fate in ((), (route.PLANT,), (route.DEAD,), (route.CHIEF,), (route.PLANT, route.RETURNED)):
            for branch in ("jerribeth.settlement_kept", "jerribeth.short_future_requested"):
                visited, ends = walk(self.future, {branch, *fate})
                self.assertTrue(ends)
                self.assertTrue(any("jerribeth.committed" in held for held in ends))
                for held in ends:
                    stances = held & {route.SHARE, route.EXCLUSIVE, route.SECRET}
                    if "jerribeth.committed" in held:
                        self.assertIn(route.READY, held)
                        self.assertEqual(len(stances), 1)
                    if route.EXCLUSIVE in held:
                        self.assertIn(route.REFUSED, held)
                        self.assertIn("jerribeth.closed", held)
                        self.assertNotIn("jerribeth.committed", held)
                self.assertTrue(any(node == "partner_name" for node, held in visited))

    def test_old_nodes_indices_destinations_and_effects_survive(self):
        nodes = {n['Id']: n for n in self.future['Nodes']}
        self.assertTrue(all((new is not None and old['Id'] == new['Id'] for old, new in zip_longest(self.before['Nodes'], self.future['Nodes']) if old is not None)))
        for node in self.before['Nodes']:
            self.assertTrue(all(new is not None for old, new in zip_longest(node['Choices'], nodes[node['Id']]['Choices']) if old is not None))
            for choice, after in zip(node['Choices'], nodes[node['Id']]['Choices']):
                self.assertEqual(after['Next'], choice['Next'])
                self.assertEqual(after['Set'], choice['Set'])

    def test_mid_scene_save_can_get_terms_without_dead_end(self):
        for node_id in ("promise", "short_future"):
            _, ends = walk(self.future, {"jerribeth.short_future_requested"}, node_id)
            self.assertTrue(any("jerribeth.committed" in held and route.READY in held for held in ends))

    def test_secret_is_exposed_only_to_known_partner_and_can_close(self):
        fixture = {"Id": "jerribeth.test_visit", "Nodes": [n("arrival_terms", "Jerribeth", "", c(next="threshold")),
                   n("threshold", "Jerribeth", "", c())]}
        route.install_discovery(fixture, {"arrival_terms"})
        for fate in ((), (route.PLANT,), (route.DEAD,), (route.CHIEF,), (route.PLANT, route.RETURNED)):
            _, ends = walk(fixture, {route.SECRET, *fate})
            survives = [held for held in ends if "jerribeth.closed" not in held]
            self.assertTrue(survives)
            exposed = route.PLANT in fate and route.RETURNED not in fate or route.CHIEF in fate
            self.assertTrue(all((route.EXPOSED in held) == exposed for held in survives))
            self.assertTrue(any("jerribeth.closed" in held for held in ends))

    def test_every_fate_has_one_epilogue_status_without_stance(self):
        guards = [
            ([route.DEAD], []),
            ([route.CHIEF], [route.DEAD]),
            ([route.PLANT], [route.DEAD, route.CHIEF, route.RETURNED, route.CHOSEN]),
            ([route.PLANT, route.RETURNED], [route.DEAD, route.CHIEF]),
            ([], list(route.FATES)),
        ]
        paragraphs = [p for p in route.partner_paragraphs()
                      if (p.get('Requires', []), p.get('Forbids', [])) in guards]
        for flags in (set(), {route.PLANT}, {route.DEAD}, {route.CHIEF}, {route.PLANT, route.RETURNED}, {route.PLANT, route.DEAD}):
            status, = [p for p in paragraphs if allowed(p, flags)]
            self.assertTrue(status.get('Requires') or status.get('Forbids'))

    def test_existing_visit_keeps_answers_for_all_stances_and_current_fates(self):
        fixture = {'Id': 'jerribeth.test_visit', 'Nodes': [n('arrival_terms', 'Jerribeth', '', c(next='threshold')), n('threshold', 'Jerribeth', '', c())]}
        route.install_discovery(fixture, {'arrival_terms'})
        route.install_shared_witness(fixture, {'arrival_terms'})
        for fate in ((), (route.PLANT,), (route.DEAD,), (route.CHIEF,), (route.PLANT, route.DEAD), (route.PLANT, route.RETURNED)):
            for stance in ((), (route.SHARE,), (route.SECRET,)):
                entry, = [a for a in fixture['Nodes'][0]['Choices'] if allowed(a, {*fate, *stance})]
                self.assertIn(entry['Next'], {n['Id'] for n in fixture['Nodes']})
                visited, ends = walk(fixture, {*fate, *stance})
                self.assertTrue(ends)
                shows = any((node == 'partner_witness_arrival_terms' for node, held in visited))
                self.assertEqual(shows, route.SHARE in stance and route.PLANT in fate and (route.DEAD not in fate) and (route.RETURNED not in fate))

    def test_secret_exposure_receipt_keeps_reaction_after_native_death(self):
        fixture = {"Id": "jerribeth.test_visit", "Nodes": [n("arrival_terms", "Jerribeth", "", c())]}
        route.install_discovery(fixture, {"arrival_terms"})
        _, ends = walk(fixture, {route.SECRET, route.PLANT})
        survivor = next(held for held in ends if "jerribeth.closed" not in held)
        self.assertIn("jerribeth.partner_exposure.plant", survivor)
        after_death = set(survivor) | {route.DEAD}
        exposed = [paragraph for paragraph in route.partner_paragraphs()
                   if route.EXPOSED in paragraph.get("Requires", ()) and allowed(paragraph, after_death)]
        exposed_receipt, = exposed
        self.assertIn(route.EXPOSED, exposed_receipt['Requires'])
if __name__ == '__main__':
    unittest.main()
