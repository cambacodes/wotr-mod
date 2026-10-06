"""Partner stances, append-only save surfaces, and current-fate receipts."""
import copy
import json
from pathlib import Path
import unittest

from storylines import minagho_chivarro_stance as stance
from storylines import minagho_chivarro_continuation as ordinary
from storylines import minagho_chivarro_trickster as trickster
from tools import rrt_verify
from tools.canon_partner_lint import _dialogue_replacements


class MinaghoChivarroStanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests.story_fixture import fresh_story
        cls.story = fresh_story()
        cls.model = rrt_verify.Model(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}
        cls.dialogue_replacements = _dialogue_replacements(cls.story)

    def state(self, *flags):
        state = rrt_verify.SimState(5, 5000)
        state.flags.update(('chapter_later', 'trickster', 'trickster.ever', *flags))
        rrt_verify.sim_complete(self.model, state)
        return state

    def test_original_scene_nodes_choices_and_effects_stay_in_position(self):
        for original in ordinary.SCENES + trickster.SCENES:
            with self.subTest(scene=original['Id']):
                revised = self.scenes[original['Id']]
                self.assertEqual([n['Id'] for n in original['Nodes']], [n['Id'] for n in revised['Nodes'][:len(original['Nodes'])]])
                for before, after in zip(original['Nodes'], revised['Nodes']):
                    self.assertGreaterEqual(len(after['Choices']), len(before['Choices']))
                    for old, new in zip(before['Choices'], after['Choices']):
                        if (original['Id'] == stance.P + 'after.the_price_of_her_name_letter'
                                and before['Id'] == 'start' and old is before['Choices'][0]):
                            paying = next(n for n in revised['Nodes'] if n['Id'] == 'verdict_paid')
                            self.assertEqual(old['Set'], paying['Choices'][0]['Set'])
                            self.assertEqual(new['Set'], [])
                        elif (old['Next'] is None and '.explicit.' in (new['Next'] or '')
                              and new['Set'] != old['Set']):
                            by_id = {n['Id']: n for n in revised['Nodes']}
                            paying = by_id[new['Next']]
                            target = paying['Choices'][0]['Next']
                            if target and target.endswith('.after'):
                                paying = by_id[target]
                            self.assertEqual(old['Set'], paying['Choices'][0]['Set'])
                            self.assertEqual(new['Set'], [])
                        else:
                            self.assertTrue(set(old['Set']).issubset(new['Set']))

    def test_commitment_producers_record_exactly_one_initial_stance(self):
        produced = set()
        for page in self.scenes.values():
            if page.get('Relationship') != stance.REL:
                continue
            for node in page['Nodes']:
                for answer in node['Choices']:
                    states = set(answer['Set']) & {stance.SHARE, stance.EXCLUSIVE, stance.SECRET}
                    self.assertLessEqual(len(states), 1)
                    if stance.COMPLETE in answer['Set'] and any(f.startswith('minachiv.future_') and f not in
                            {'minachiv.future_open', 'minachiv.future_friends', 'minachiv.future_service'} for f in answer['Set']):
                        self.assertTrue(states, (page['Id'], node['Id']))
                    produced.update(states)
        self.assertEqual(produced, {stance.SHARE, stance.EXCLUSIVE, stance.SECRET})

    def test_current_fates_distinguish_death_departure_and_earned_return(self):
        cases = [
            (('minagho.dead',), 'minagho', 'dead'),
            (('minagho.dead', stance.RET_M, stance.MIN_IN), 'minagho', 'present'),
            ((stance.DECL_M,), 'minagho', 'distant'),
            ((), 'minagho', 'unknown'),
            (('chivarro.dead',), 'chivarro', 'unknown'),
            (('chivarro.dead', 'chivarro.exile_objective_done'), 'chivarro', 'dead'),
            (('chivarro.dead', 'chivarro.exile_objective_done', stance.P + 'chivarro_deposit'), 'chivarro', 'cellar'),
            (('chivarro.dead', 'chivarro.exile_objective_done', stance.RET_C, stance.CH_IN), 'chivarro', 'present'),
            (('chivarro.dead', 'chivarro.exile_objective_done', stance.RET_C, stance.CH_IN, stance.SENT_BACK), 'chivarro', 'distant'),
        ]
        for flags, woman, expected in cases:
            with self.subTest(flags=flags):
                state = self.state(*flags)
                names = ('dead', 'present', 'distant', 'unknown') + (('cellar',) if woman == 'chivarro' else ())
                visible = [name for name in names if stance.STATE + woman + '.' + name in state.flags]
                self.assertEqual(visible, [expected])
                self.assertEqual(stance.STATE + woman + ".alive" in state.flags, expected in {"present", "distant", "cellar"})

    def test_every_ending_page_and_own_lastcall_has_state_and_stance_receipts(self):
        for page in self.scenes.values():
            if page['Id'] in self.dialogue_replacements:
                continue
            if not (page.get('Relationship') == stance.REL and page['Owner'].endswith('Epilogue')
                    or page['Id'] == 'minachiv.lastcall.page') or page['Owner'] == 'AeonEpilogue':
                continue
            for node in page['Nodes']:
                if '.explicit.' in node['Id']:
                    # The heated cut returns to the saved ending node, whose
                    # current-state and stance receipts are checked below.
                    continue
                with self.subTest(scene=page['Id'], node=node['Id']):
                    reads = {f for p in node.get('Paragraphs', []) for f in p['Requires']}
                    self.assertTrue({stance.SHARE, stance.EXCLUSIVE, stance.SECRET}.issubset(reads))
                    for woman in ('minagho', 'chivarro'):
                        self.assertTrue({stance.STATE + woman + '.' + x for x in ('dead', 'present', 'distant', 'unknown')}.issubset(reads))

    def test_lost_welcome_does_not_play_the_lastcall_romance(self):
        page = self.scenes["minachiv.lastcall.page"]
        self.assertIn(stance.COOLED, page["Forbids"])
        self.assertNotIn(stance.COOLED, page.get("ForbidOverrides", {}))

    def test_late_decisions_record_stance_without_earlier_commitment(self):
        page = self.scenes[stance.P + 'epilogue.commit']
        self.assertTrue({'late_exclusive_minagho', 'late_exclusive_chivarro', 'late_secret_minagho', 'late_secret_chivarro'}.issubset({n['Id'] for n in page['Nodes']}))
        pair = next(n for n in page['Nodes'] if n['Id'] == 'pair')
        self.assertEqual(pair['Choices'][0]['Set'], [stance.SHARE])
        self.assertEqual([a['Set'][0] for a in pair['Choices'][3:7]],
                         [stance.EXCLUSIVE, stance.SECRET, stance.EXCLUSIVE, stance.SECRET])
        self.assertTrue(all(stance.COMPLETE not in a['Set'] and
                           all(f.startswith(stance.S) or f == stance.CLOSED for f in a['Set'])
                           for n in page['Nodes'] for a in n['Choices']))

    def test_secret_service_keeps_the_original_contract(self):
        page = self.scenes['minachiv.before_the_last_road']
        nodes = [n for n in page['Nodes'] if '_secret_chivarro' in n['Id']]
        service = [a for n in nodes for a in n['Choices'] if stance.SECRET in a['Set']
                   and 'minachiv.future_chivarro_service' in a['Set']]
        self.assertEqual(len(service), 1)
        self.assertNotIn('minachiv.future_chivarro', service[0]['Set'])
        coda = self.scenes[stance.P + 'epilogue.partner_refused']['Nodes'][0]
        self.assertTrue(any({stance.COOLED, 'minachiv.future_chivarro_service'} <= set(p['Requires'])
                            for p in coda['Paragraphs']))

    def test_generated_saved_exits_keep_their_indices(self):
        original = {s['Id']: s for s in ordinary.SCENES + trickster.SCENES}
        for (sid, nid), (_, exits) in stance._SAVED_GUARDS.items():
            count = len(next(n for n in original[sid]['Nodes'] if n['Id'] == nid)['Choices'])
            node = next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)
            for offset, flags in enumerate(exits):
                answer = node['Choices'][count + offset]
                self.assertTrue(answer['Abort'])
                self.assertEqual(tuple(answer['Forbids']), flags)
                self.assertEqual(answer['Set'], [])

    def test_unknown_partner_remains_possible_without_free_discovery(self):
        unknown = self.state(stance.SECRET, stance.TARGET_M, stance.MIN_IN, 'chivarro.dead')
        self.assertIn(stance.STATE + 'chivarro.unknown', unknown.flags)
        self.assertIn(stance.STATE + 'chivarro.possibly_alive', unknown.flags)
        self.assertNotIn(stance.S + 'discovery_due', unknown.flags)
        self.assertNotIn(stance.S + 'letter_due', unknown.flags)
        dead = self.state('chivarro.dead', 'chivarro.exile_objective_done')
        self.assertNotIn(stance.STATE + 'chivarro.possibly_alive', dead.flags)

    def test_discovery_needs_both_current_participants(self):
        distant = self.state(stance.SECRET, stance.TARGET_M, stance.MIN_IN, stance.SENT_BACK)
        together = self.state(stance.SECRET, stance.TARGET_M, stance.MIN_IN, stance.CH_IN)
        exposed = self.state(stance.SECRET, stance.EXPOSED, stance.MIN_IN, stance.CH_IN)
        due = stance.S + 'discovery_due'
        self.assertNotIn(due, distant.flags)
        self.assertIn(stance.S + 'letter_due', distant.flags)
        self.assertIn(due, together.flags)
        self.assertNotIn(stance.S + 'letter_due', together.flags)
        self.assertNotIn(due, exposed.flags)

    def test_inline_secret_nights_dispatch_before_shared_morning(self):
        witnessed = 0
        for page in self.scenes.values():
            nodes = {n['Id']: n for n in page['Nodes']}
            if 'stance_morning_route' not in nodes:
                continue
            nights = [n for n in page['Nodes'] if n['Id'].startswith('stance_') and '_night_' in n['Id']]
            self.assertTrue(nights)
            for night in nights:
                target = night['Choices'][0]['Next']
                if '.explicit.' in (target or ''):
                    slot = nodes[target]
                    self.assertEqual(slot['Choices'][0]['Set'], [])
                    target = slot['Choices'][0]['Next']
                self.assertEqual(target, 'stance_morning_route')
            branches = {a['Next']: a for a in nodes['stance_morning_route']['Choices']}
            self.assertIn(stance.S + 'discovery_due', branches['stance_discovery']['Requires'])
            self.assertIn(stance.S + 'letter_due', branches['stance_discovery_letter']['Requires'])
            self.assertIn(stance.P + 'cost.morning_after', branches['stance_discovery']['Set'])
            self.assertIn(stance.P + 'cost.morning_after', branches['stance_discovery_letter']['Set'])
            self.assertEqual(set(branches['morning']['Forbids']), {stance.S + 'discovery_due', stance.S + 'letter_due'})
            witnessed += 1
        self.assertGreater(witnessed, 0)

    def test_solo_insert_keeps_its_original_participant_contract(self):
        from types import SimpleNamespace
        from tools.crossroute_checks.late_commitment import outcome_woman
        page = self.scenes[stance.P + 'epilogue.commit']
        nodes = {node['Id']: node for node in page['Nodes']}
        for ordinal, woman in ((1, None), (2, 'chivarro')):
            node = nodes[page['Id'] + '.explicit.' + str(ordinal)]
            self.assertEqual(outcome_woman(SimpleNamespace(
                route=stance.REL, scene=page, node=node)), woman)

    def test_own_lastcall_entry_does_not_accumulate_paragraphs_on_reexport(self):
        from storylines import lastcall_partners
        part = next(x for x in lastcall_partners.PARTNERS if x['rel'] == stance.REL)
        saved = copy.deepcopy(part['paragraphs'])
        try:
            stance.integrate({'Scenes': []})
            first = copy.deepcopy(part['paragraphs'])
            stance.integrate({'Scenes': []})
            self.assertEqual(first, part['paragraphs'])
        finally:
            part['paragraphs'] = saved


if __name__ == '__main__':
    unittest.main()
