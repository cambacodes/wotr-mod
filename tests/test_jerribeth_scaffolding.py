"""Edge job 4: parked-save gates, appended fallbacks and native read-only hooks."""
import json
import unittest
from itertools import zip_longest
from tests.structure import without_prose
from itertools import product
from pathlib import Path
from unittest.mock import patch
import zipfile
from storylines import jerribeth_scaffolding as route
from tests.test_jerribeth_round2 import assemble
from tests.test_jerribeth_partner import allowed

def walk(event, flags, start=None):
    """Explore both native check outcomes, keeping each path's receipts."""
    nodes = {n["Id"]: n for n in event["Nodes"]}
    todo = [(start or event["Nodes"][0]["Id"], frozenset(flags), frozenset())]
    seen, ends = set(), []
    while todo:
        nid, held, path = todo.pop()
        if nid in path:
            raise AssertionError("Dialogue cycle: " + nid)
        if (nid, held) in seen:
            continue
        seen.add((nid, held))
        choices = [a for a in nodes[nid]["Choices"] if allowed(a, held)]
        if not choices:
            raise AssertionError("No answer: " + event["Id"] + "/" + nid)
        for choice in choices:
            state = held | frozenset(choice["Set"])
            check = choice.get("Check")
            targets = [check["Success"], check["Failure"]] if check else [choice.get("Next")]
            for target in targets:
                if target:
                    todo.append((target, state, path | {nid}))
                elif not choice.get("Abort"):
                    ends.append(state)
    return seen, ends

class ScaffoldingTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with patch.object(route, "integrate"):
            cls.before = assemble()
        cls.events = assemble()

    def gate(self, name, new, retired, parking_points):
        event = self.events[route.flag(name)]
        self.assertIn(route.flag(new), event["Requires"])
        self.assertNotIn(route.flag(retired), event["Requires"])
        for parking in parking_points:
            with self.subTest(parking=parking):
                # Other unchanged terms remain required; only the retired stretch
                # is absent. No new entitlement is supplied to a parked save.
                flags = set(event["Requires"]) - {route.flag(new)}
                flags.update(parking)
                self.assertTrue(allowed(event, flags))
                _, ends = walk(event, flags)
                self.assertTrue(ends)
        self.assertFalse(allowed(event, set(event["Requires"]) - {route.flag(new)}))

    def test_unsold_evening_gate_after_offered_signature_or_small_print(self):
        self.gate("unsold_evening", "counteroffer_sent", "sale_terms_set", [
            {route.flag("counteroffer_sent")},
            {route.flag("counteroffer_sent"), route.flag("sale_terms_set")},
        ])

    def test_guest_gate_after_unsold_evening_or_purchaser_answer(self):
        self.gate("counterfeit_guest", "unsold_evening_kept", "consequences_kept", [
            {route.flag("unsold_evening_kept")},
            {route.flag("unsold_evening_kept"), route.flag("consequences_kept")},
        ])

    def test_audience_gate_after_guest_hinge_or_clerk(self):
        self.gate("counterfeit_audience", "counter_invited", "counter_clerk_dealt", [
            {route.flag("counter_invited")},
            {route.flag("counter_invited"), route.flag("counter_mechanism_known")},
            {route.flag("counter_invited"), route.flag("counter_clerk_dealt")},
        ])

    def test_room_gate_after_spoil_after_or_settlement(self):
        self.gate("room_measure", "counter_spoils_settled", "settlement_visited", [
            {route.flag("counter_spoils_settled"), route.flag("counter_public_account")},
            {route.flag("counter_spoils_settled"), route.flag("counter_private_archive"), route.flag("counteroffer_kept")},
            {route.flag("counter_spoils_settled"), route.flag("counter_public_account"), route.flag("settlement_visited")},
        ])

    def test_farewell_gate_after_future_or_ordinary(self):
        self.gate("farewell", "future", "ordinary", [
            {route.flag("future")}, {route.flag("future"), route.flag("ordinary")},
        ])

    def test_farewell_review_gate_after_future_or_ordinary(self):
        self.gate("farewell_review", "future", "ordinary", [
            {route.flag("future")}, {route.flag("future"), route.flag("ordinary")},
        ])

    def test_fallbacks_cover_all_retired_history_combinations(self):
        for name, host, index, retired, routes in (('counterfeit_audience', 'challenge', 3, ('counter_clerk_witness', 'counter_clerk_rehearsal', 'counter_clerk_hidden'), ((),)), ('counterfeit_spoil', 'start', 2, ('counter_return_agreement', 'counter_hold_agreement'), (('counter_private_archive',), ('counter_public_account',))), ('room_measure', 'public_result', 3, ('inspection_visible', 'inspection_removed', 'inspection_refused'), ((),)), ('room_measure', 'private_result', 3, ('catalogue_play', 'catalogue_comedy', 'catalogue_declined'), ((),))):
            event = self.events[route.flag(name)]
            choices = route.node(event, host)['Choices']
            for branch in routes:
                for values in product((False, True), repeat=len(retired)):
                    flags = set(event['Requires']) | set(map(route.flag, branch))
                    flags.update((route.flag(f) for f, yes in zip(retired, values) if yes))
                    with self.subTest(scene=name, node=host, branch=branch, history=values):
                        self.assertTrue(any((allowed(a, flags) for a in choices)))
                        fallback_index = index + routes.index(branch)
                        fallback = next(a for a in choices if set(map(route.flag, retired)) <= set(a['Forbids']) and route.flag(branch[0]) in a['Requires']) if branch else next(a for a in choices if set(map(route.flag, retired)) <= set(a['Forbids']))
                        self.assertEqual(allowed(fallback, flags), not any(values))
                        self.assertTrue(walk(event, flags, host)[1])

    def test_saved_nodes_choices_prose_and_receipts_survive(self):
        for sid, old in self.before.items():
            current = self.events[sid]
            self.assertTrue(all(new is not None and was['Id'] == new['Id'] for was, new in zip_longest(old['Nodes'], current['Nodes']) if was is not None))
            for was, now in zip(old['Nodes'], current['Nodes']):
                kept = list(was.get('Paragraphs') or [])
                for previous in kept:
                    self.assertIn(without_prose(previous), [without_prose(p) for p in now.get('Paragraphs', [])])
                self.assertTrue(all(new is not None for old, new in zip_longest(was['Choices'], now['Choices']) if old is not None))
                self.assertTrue(all(new is not None for old, new in zip_longest(was['Choices'], now['Choices']) if old is not None))
                for old_choice, new_choice in zip(was['Choices'], now['Choices']):
                    self.assertTrue(set(old_choice['Set']) <= set(new_choice['Set']))
                self.assertTrue({a['Next'] for a in was['Choices'] if a.get('Next')} <= {n['Id'] for n in current['Nodes']})

    def test_retired_hosts_keep_every_surface_but_cannot_open(self):
        for name in route.RETIRED:
            event = self.events[route.flag(name)]
            self.assertIn('chapter_later', event['Forbids'])
            self.assertFalse(allowed(event, {*event['Requires'], 'chapter_later'}))
            self.assertEqual(without_prose(event['Nodes']), without_prose(self.before[route.flag(name)]['Nodes']))

    def test_visits_keep_remote_book_delivery_in_drezen(self):
        from storylines.scene_kinds import kind_of
        for name in route.VISITS:
            event = self.events[route.flag(name)]
            self.assertTrue(event["Remote"])
            self.assertEqual(kind_of(event), "visit")
            self.assertEqual(event["Areas"], [route.DREZEN])
            self.assertFalse(event.get("AnswerLists"))
            self.assertFalse(event.get("NativeReturnCue"))


    def test_binding_uses_native_observations_only(self):
        with patch.object(route, "integrate", wraps=route.integrate) as install:
            assemble()
        result = install.call_args.args[0]
        self.assertEqual(result["SeenCues"][route.flag("mark_seen")], [route.MARK_CUE])
        self.assertEqual(result["Etudes"]["arueshalae.in_party"], route.ARUESHALAE_PARTY)

    @unittest.skipUnless(Path('/wrath/blueprints.zip').exists(), 'native archive unavailable')
    def test_native_binding_evidence(self):
        with zipfile.ZipFile('/wrath/blueprints.zip') as archive:
            cue = json.loads(archive.read('World/Dialogs/c3/IvorySanctum/JerribethGreetings/Cue_0019.jbp'))
            etude = json.loads(archive.read('World/Etudes/Common/WrathOfTheRighteous/Companions/ArueshalaeCompanion/ArueshalaeInParty.jbp'))
        self.assertEqual(cue['AssetId'], route.MARK_CUE)
        self.assertEqual(etude['AssetId'], route.ARUESHALAE_PARTY)
        self.assertIn('CompanionInParty', json.dumps(etude))

    def test_companion_pages_require_current_party_presence(self):
        for name in route.VISITS:
            event = self.events[route.flag(name)]
            pages = {p['Id']: p for p in event['Nodes']}
            for page in event['Nodes']:
                for choice in page['Choices']:
                    target = choice.get('Next') or ''
                    if target.startswith('companion_'):
                        companion = target.removeprefix('companion_')
                        self.assertIn(companion + '.in_party', choice['Requires'])
                        self.assertIn(target, pages)

    def test_checks_costs_and_branch_receipts(self):
        checks = []
        for name in (*route.VISITS, 'farewell'):
            event = self.events[route.flag(name)]
            for page in event['Nodes']:
                for choice in page['Choices']:
                    if choice.get('Check'):
                        self.assertTrue(choice['Check']['CommanderOnly'])
                        checks.append((choice['Check']['Skill'], choice['Check']['DC']))
        for required in [('CheckDiplomacy', 24), ('SkillPerception', 20),
                         ('CheckDiplomacy', 22), ('SkillKnowledgeArcana', 32),
                         ('SkillPerception', 30), ('SkillKnowledgeWorld', 30),
                         ('SkillAthletics', 30), ('CheckDiplomacy', 32),
                         ('CheckDiplomacy', 30)]:
            self.assertIn(required, checks)
        event = self.events[route.flag('offered_signature')]
        _, ends = walk(event, set(event['Requires']))
        for held in ends:
            self.assertTrue({route.flag('counteroffer_sent'), route.flag('sale_terms_set'),
                             route.flag('consequences_kept')} <= held)
            self.assertTrue({route.flag('offer_performance'), route.flag('sale_corrected')} <= held
                            or {route.flag('offer_design'), route.flag('sale_corrected')} <= held
                            or {route.flag('offer_design'), route.flag('sale_withdrawn')} <= held)

    def test_every_live_terminal_emits_absorbed_receipts(self):
        for name, receipt, bridges in (
            ("offered_signature", "counteroffer_sent", ("sale_terms_set", "consequences_kept")),
            ("unsold_evening", "unsold_evening_kept", ("consequences_kept",)),
            ("counterfeit_guest", "counter_invited", ("consequences_kept", "counter_mechanism_known", "counter_clerk_dealt")),
            ("room_measure", "settlement_kept", ("settlement_visited", "counteroffer_kept")),
            ("farewell", "farewell_kept", ("ordinary",)),
        ):
            event = self.events[route.flag(name)]
            flags = set(event["Requires"]) | {route.flag("counter_public_account")}
            _, ends = walk(event, flags)
            for held in ends:
                if route.flag(receipt) in held:
                    self.assertTrue(set(map(route.flag, bridges)) <= held)
if __name__ == '__main__':
    unittest.main()
