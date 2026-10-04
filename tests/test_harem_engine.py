"""Shared household registrations, attendance mirrors, caps and delayed witness validation."""
import copy
import json
from pathlib import Path
import unittest

from story_format import c, n
from storylines import household, harem_caps
from tools import rrt_verify, harem_schedule_lint

ROOT = Path(__file__).resolve().parents[1]


class HouseholdEngine(unittest.TestCase):
    def test_registration_preserves_enmity_overrides_participants_and_allowance(self):
        previous = list(household.ENTRIES)
        consumers = dict(household.CONSUMERS)
        try:
            body = household.table_entry('test.pair', 'Test', '[Test]', [n('start', 'Seelah', 'Test.', c())],
                                         ('seelah', 'wenduag'), 'test.trigger')
            self.assertEqual(body['Participants'], ['seelah', 'wenduag'])
            self.assertEqual(body['Pair'], body['Participants'])
            self.assertEqual(body['RestAllowance'], 'household.pair')
            self.assertIn(household.PAGE_TAKEN, body['Requires'])
            for a, b in (('seelah', 'wenduag'), ('wenduag', 'seelah')):
                self.assertEqual(body['ForbidOverrides'][household.enmity(a, b)], a + '.harem.reconciled.' + b)
            self.assertEqual(household.CONSUMERS[body['Id']], household.PAGE_TAKEN)
        finally:
            household.ENTRIES[:] = previous
            household.CONSUMERS.clear()
            household.CONSUMERS.update(consumers)

    def test_arc_cap_affects_only_starts_and_protected_discoveries_stay_uncapped(self):
        scenes = []
        for i in range(5):
            scenes.append(dict(Id='arc.%d.start' % i, MinChapter=5, MaxChapter=5, Chapters=[5],
                               HouseholdCategory='pair', HouseholdArcStart=True, HouseholdWitness='arc.%d.seen' % i, Forbids=[]))
            scenes.append(dict(Id='arc.%d.next' % i, MinChapter=5, MaxChapter=5, Chapters=[5],
                               HouseholdCategory='pair', HouseholdWitness='arc.%d.next.seen' % i, Forbids=[]))
        scenes.append(dict(Id='protected.discovery', MinChapter=5, MaxChapter=5, Chapters=[5],
                           HouseholdCategory='protected', HouseholdWitness='discovery.seen', Forbids=[]))
        payload = dict(Scenes=scenes)
        harem_caps.apply(payload)
        cap = payload['Counts']['household.cap.ch5.arcs']
        self.assertEqual(cap['Min'], 4)
        self.assertEqual(len(cap['Of']), 5)
        self.assertTrue(all(s['Forbids'] for s in scenes if s.get('HouseholdArcStart')))
        self.assertTrue(all(not s['Forbids'] for s in scenes if not s.get('HouseholdArcStart')))

    def test_delayed_anygroups_must_supply_a_clock_on_every_alternative(self):
        scene = dict(Id='delayed', DelayHours=48, Requires=['derived.stage'],
                     RequiresAnyGroups=[['witness.a', 'derived.alternative']])
        story = dict(Derived={'derived.stage': [['native']], 'derived.alternative': [['native']]},
                     Etudes={'native': 'a' * 32}, Scenes=[{'Id': 'producer', 'Nodes': [{'Choices': [{'Set': ['witness.a']}]}]}])
        self.assertTrue(harem_schedule_lint.delayed_clock_errors(scene, story))
        scene['RequiresAnyGroups'] = [['witness.a', 'witness.b']]
        story['Scenes'][0]['Nodes'][0]['Choices'][0]['Set'].append('witness.b')
        self.assertEqual(harem_schedule_lint.delayed_clock_errors(scene, story), [])

    def test_pending_page_is_false_and_stub_opens_only_current_trickster_stance(self):
        story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))
        model = rrt_verify.Model(story)
        state = rrt_verify.SimState(3, 1000)
        state.flags.update(['trickster', 'seelah.committed'])
        rrt_verify.sim_complete(model, state)
        offer = model.by_id['household.table.offered']
        self.assertFalse(rrt_verify.sim_available(model, offer, state))
        state.flags.add(household.PAGE_TAKEN)
        rrt_verify.sim_complete(model, state)
        self.assertTrue(rrt_verify.sim_available(model, offer, state))
        state.flags.remove('trickster')
        rrt_verify.sim_complete(model, state)
        self.assertNotIn(household.STANCE_ELIGIBLE, state.flags)

    def test_caps_are_evaluated_in_their_chapter_and_seat_attendance_matches_rules(self):
        story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))
        story['Counts']['household.cap.ch5.arcs'] = dict(Of=['seelah.committed'], Min=1, Chapters=[5])
        model = rrt_verify.Model(story)
        for chapter in (3, 5):
            state = rrt_verify.SimState(chapter, 1000)
            state.flags.add('seelah.committed')
            rrt_verify.sim_complete(model, state)
            self.assertEqual('household.cap.ch5.arcs' in state.flags, chapter == 5)
        solo = rrt_verify.norm_scene(dict(Id='test.solo', Relationship='household', MinChapter=5, MaxChapter=5,
                                          Participants=['minagho_chivarro'], ParticipantWomen=['minagho']))
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(['minachiv.complete', 'chivarro.dead'])
        rrt_verify.sim_complete(model, state)
        self.assertTrue(rrt_verify.sim_available(model, solo, state))
        solo['ParticipantWomen'] = ['chivarro']
        self.assertFalse(rrt_verify.sim_available(model, solo, state))
        state.flags.add('minagho_chivarro.trickster.returned_chivarro')
        self.assertTrue(rrt_verify.sim_available(model, solo, state))
        state.flags.add(story['Relationships']['minagho_chivarro']['ClosedFlag'])
        self.assertFalse(rrt_verify.sim_available(model, solo, state))

    def test_row28_reads_the_verified_cue_in_the_correct_direction(self):
        story = json.loads((ROOT / 'development/Story.json').read_text(encoding='utf-8-sig'))
        key = 'jerribeth.harem.vellexia_defection_seen'
        self.assertEqual(story['SeenCues'][key], ['e0ee422a413a5f94ea90bede3096ee56'])
        schedule = json.loads((ROOT / 'tools/harem-schedule.json').read_text())
        row = next(row for row in schedule['schedule'] if row['ref'] == 'S28')
        self.assertIn(key, row['reads'])
        model = rrt_verify.Model(story)
        scene = rrt_verify.norm_scene(dict(Id='test.defection', Relationship='household', MinChapter=5, MaxChapter=5, Requires=[key]))
        state = rrt_verify.SimState(5, 1000)
        self.assertFalse(rrt_verify.sim_available(model, scene, state))
        state.flags.add(key)
        self.assertTrue(rrt_verify.sim_available(model, scene, state))
