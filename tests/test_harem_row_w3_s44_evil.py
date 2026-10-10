"""S44 optional staging: approval boundary, deeds, safety, clocks and reload."""
import copy
import unittest
from unittest.mock import patch

from storylines import household
from storylines.harem_rows import s44, w3_s44_evil as row
from tools import harem_schedule_lint, player_text_lint, rrt_verify, savecompat


class S44EvilTests(unittest.TestCase):
    def setUp(self):
        self.entries = list(household.ENTRIES)
        self.consumers = dict(household.CONSUMERS)
        household.ENTRIES[:] = []
        self.payload = {}
        s44.register(self.payload, [], {})
        self.base = copy.deepcopy(household.ENTRIES)
        with patch.object(row, "metadata_ready", return_value=True):
            row.register(self.payload, [], {})
        self.rows = copy.deepcopy(household.ENTRIES[4:])
        self.by = {s['Id'].removeprefix(row.P): s for s in self.rows}

    def tearDown(self):
        household.ENTRIES[:] = self.entries
        household.CONSUMERS.clear()
        household.CONSUMERS.update(self.consumers)

    def test_unreviewed_metadata_exports_no_extension_or_higher_stages(self):
        self.assertFalse(row.metadata_ready())
        household.ENTRIES[:] = []
        payload = {}
        s44.register(payload, [], {})
        before = copy.deepcopy(payload)
        row.register(payload, [], {})
        self.assertEqual(household.ENTRIES, self.base)
        self.assertEqual(payload, before)

    def test_approval_needs_both_branch_ceiling_and_allocation(self):
        import json
        approved = dict(rom=True, branch_ceilings={
            'arueshalae.redeemed': 'respect/respect', 'arueshalae.corrupted': 'lover/lover'},
            optional_arc=dict(id=row.ARC, chapter=5, steps=4))
        for missing in (None, 'rom', 'branch_ceilings', 'optional_arc'):
            candidate = copy.deepcopy(approved)
            if missing:
                candidate.pop(missing)
            with patch.object(row.Path, 'read_text', return_value=json.dumps({'rows': {'44': candidate}})):
                self.assertEqual(row.metadata_ready(), missing is None)

    def test_registration_preserves_base_identities_and_is_idempotent(self):
        with patch.object(row, 'metadata_ready', return_value=True):
            row.register(self.payload, [], {})
        self.assertEqual(len(household.ENTRIES), 8)
        self.assertEqual(household.ENTRIES[:4], self.base)
        self.assertEqual(savecompat.check({'Scenes': household.ENTRIES}, savecompat.inventory({'Scenes': self.base})), [])

    def test_metadata_alone_cannot_enable_an_over_budget_allocation(self):
        household.ENTRIES[:] = self.base
        payload = {}
        before = copy.deepcopy(payload)
        candidates = [dict(Id='budget.' + str(i), HouseholdCategory='pair',
            RestAllowance='household.pair', HouseholdWitness='budget.' + str(i),
            HouseholdArc='budget.arc', HouseholdArcStart=i == 0,
            Chapters=[5], MinChapter=5, MaxChapter=5) for i in range(15)]
        with patch.object(row, 'metadata_ready', return_value=True):
            with self.assertRaisesRegex(ValueError, 'optional step sum 19 exceeds 18'):
                row.register(payload, candidates, {})
        self.assertEqual(payload, before)
        self.assertEqual(household.ENTRIES, self.base)

    def model(self):
        payload = copy.deepcopy(self.payload)
        payload['Scenes'] = self.base + self.rows
        payload['RestAllowances'] = {'household.pair': 1}
        payload['Relationships'] = {r: dict(StartedFlag=r + '.started',
            CommittedFlag=r + '.committed', ClosedFlag=r + '.closed', UnavailableFlags=[])
            for r in (*s44.PAIR, 'household')}
        return rrt_verify.Model(payload)

    def state(self, step, hour):
        scene = self.by[step]
        state = rrt_verify.SimState(5, hour)
        state.flags.update(scene['Requires'])
        state.flags.add('arueshalae.evil_recruited')
        state.times[scene['HouseholdWitness']] = 0
        trigger = {'cover': 'shamira_released', 'counterstroke': 'cover.arueshalae_kept',
                   'choice': 'counterstroke.shamira_kept', 'morning': 'choice.both_yes'}[step]
        state.times[row.P + trigger] = 0
        return state

    def test_each_clock_and_reload_allowance(self):
        model = self.model()
        for step, hours in (('cover', 48), ('counterstroke', 48), ('choice', 48), ('morning', 8)):
            scene = model.by_id[row.P + step]
            self.assertEqual(scene['DelayHours'], hours)
            self.assertEqual(harem_schedule_lint.delayed_clock_errors(scene, {'Scenes': self.base + self.rows}), [])
            for hour, available in ((hours - 1, False), (hours, True)):
                self.assertEqual(rrt_verify.sim_available(model, scene, copy.deepcopy(self.state(step, hour))), available)
            spent = self.state(step, hours)
            spent.rest_spent['household.pair'] = 1
            self.assertFalse(rrt_verify.sim_available(model, scene, spent))

    def test_all_steps_require_current_bodies_page_branch_open_routes(self):
        model = self.model()
        for step in self.by:
            scene = model.by_id[row.P + step]
            self.assertEqual(scene['Participants'], list(s44.PAIR))
            self.assertNotIn('RouteOpen', scene)
            self.assertEqual(scene['ParticipantWomen'], list(s44.PAIR))
            self.assertEqual(scene['Chapters'], [5])
            state = self.state(step, 48)
            for gate in ('trickster', 'foresight.page_taken', 'arueshalae.corrupted',
                         'arueshalae.evil_recruited', 'shamira.present_now',
                         'arueshalae.present_now', 'shamira.trickster.embodied'):
                absent = copy.deepcopy(state)
                absent.flags.remove(gate)
                self.assertFalse(rrt_verify.sim_available(model, scene, absent), (step, gate))
            for loss in s44.FORBIDS:
                absent = copy.deepcopy(state)
                absent.flags.add(loss)
                absent.flags.add('arueshalae.trickster.returned')
                self.assertFalse(rrt_verify.sim_available(model, scene, absent), (step, loss))
            for a, b in (s44.PAIR, s44.PAIR[::-1]):
                opposed = copy.deepcopy(state)
                opposed.flags.add(a + '.harem.enmity.' + b)
                self.assertFalse(rrt_verify.sim_available(model, scene, opposed))
                opposed.flags.add(a + '.harem.reconciled.' + b)
                self.assertTrue(rrt_verify.sim_available(model, scene, opposed))

    def test_terminal_deeds_abort_and_ward_consumption(self):
        for scene in self.rows:
            for node in scene['Nodes']:
                self.assertTrue(any(not c['Requires'] and not c['Forbids']
                                    for c in node['Choices']), (scene['Id'], node['Id']))
                for choice in node['Choices']:
                    self.assertFalse(any('.harem.' in f for f in choice['Set']))
                    self.assertFalse(choice.get('Revive'))
                    if choice['Abort']:
                        self.assertEqual(choice['Set'], [])
                        self.assertFalse(choice.get('RemoveItem'))
        nodes = {n['Id']: n for n in self.by['choice']['Nodes']}
        nav, _, abort = nodes['start']['Choices']
        self.assertEqual(nav['Requires'], ['arueshalae.ward_held'])
        self.assertEqual(nav['Set'], [])
        self.assertFalse(nav.get('RemoveItem'))
        terminal = nodes['warded']['Choices'][0]
        self.assertEqual(terminal['RemoveItem'], row.SCROLL)
        self.assertEqual(terminal['Requires'], ['arueshalae.ward_held'])
        self.assertEqual(terminal['Set'], list(row.flags('choice.seen', 'choice.both_yes', 'choice.ward_spent', 'cost.commander_gallery')))
        self.assertEqual(terminal['Next'], s44.EXPLICIT_SLOT['Id'])
        self.assertEqual(nodes[s44.EXPLICIT_SLOT['Id']]['Text'], s44.EXPLICIT_SLOT['Text'])
        self.assertTrue(abort['Abort'])
        for node_id in ('start', 'warded'):
            selectable = [c for c in nodes[node_id]['Choices'] if not c['Requires']]
            self.assertTrue(any(c['Abort'] for c in selectable))
            self.assertFalse(any(c.get('RemoveItem') for c in selectable))

    def test_directional_friendships_and_mutual_choice_have_deed_gates(self):
        model = self.model()
        state = rrt_verify.SimState(5, 48)
        state.flags.update(['arueshalae.corrupted', *row.flags('shamira_released', 'arueshalae_ornament_returned')])
        state.flags.update(row.flags('cover.arueshalae_kept'))
        rrt_verify.sim_complete(model, state)
        self.assertIn('shamira.harem.attitude.arueshalae.friend', state.flags)
        self.assertNotIn('arueshalae.harem.attitude.shamira.friend', state.flags)
        self.assertFalse(rrt_verify.sim_available(model, model.by_id[row.P + 'choice'], state))
        state.flags.update(row.flags('counterstroke.shamira_kept', 'choice.both_yes'))
        rrt_verify.sim_complete(model, state)
        for a, b in (s44.PAIR, s44.PAIR[::-1]):
            self.assertIn(a + '.harem.attitude.' + b + '.lover', state.flags)
            self.assertNotIn(a + '.harem.attitude.' + b + '.friend', state.flags)
        state.flags.remove('arueshalae.corrupted')
        state.flags.add('arueshalae.redeemed')
        rrt_verify.sim_complete(model, state)
        for a, b in (s44.PAIR, s44.PAIR[::-1]):
            for stage in ('friend', 'lover'):
                self.assertNotIn(a + '.harem.attitude.' + b + '.' + stage, state.flags)

    def test_player_disclosures_stop_only_optional_continuation(self):
        model = self.model()
        for step in ('counterstroke', 'choice', 'morning'):
            state = self.state(step, 48)
            state.flags.add(row.P + 'lust.closed_by_player')
            self.assertFalse(rrt_verify.sim_available(model, model.by_id[row.P + step], state))
        for step, result in (('cover', 'public'), ('counterstroke', 'spoiled'), ('choice', 'ordinary')):
            node = next(n for n in self.by[step]['Nodes'] if n['Id'] == result)
            self.assertFalse(any(f.endswith('.closed') or '.enmity.' in f for f in node['Choices'][0]['Set']))

    def test_only_start_capped_and_four_step_budget(self):
        for step, scene in self.by.items():
            self.assertEqual(scene['HouseholdArcStart'], step == 'cover')
            self.assertEqual(scene['HouseholdArc'], row.ARC)
            self.assertEqual(scene['RestAllowance'], 'household.pair')
            self.assertEqual(any('.cap.' in f for f in scene['Forbids']), step == 'cover')
        self.assertEqual(harem_schedule_lint.scene_load_errors({'Scenes': self.base + self.rows},
                         {'load_caps': {'5': {'arcs': 4, 'optional': 16}}}), [])
        self.assertEqual(player_text_lint.check({'Scenes': self.rows})['review'], [])


if __name__ == '__main__':
    unittest.main()
