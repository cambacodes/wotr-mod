"""fix18 structure controls: omitted layers, current delivery, and history readers."""
import copy
import hashlib
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools import harem_schedule_lint, hub_attachment_lint, rrt_verify as rules


class BuildLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()

    def test_harem_less_build_omits_only_its_owned_registrations(self):
        partial = fresh_story(include_harem=False)
        ids = {s['Id'] for s in partial['Scenes']}
        self.assertNotIn('household.ensemble.ch5.arrows', ids)
        self.assertNotIn('household.docket.gesmerha_jerribeth.account', ids)
        self.assertEqual(hub_attachment_lint.lint(partial, omitted_layers=('harem',)), [])

    def test_full_build_missing_either_harem_registration_still_raises(self):
        for sid in ('household.ensemble.ch5.arrows',
                    'household.docket.gesmerha_jerribeth.account'):
            with self.subTest(scene=sid):
                story = copy.deepcopy(self.story)
                story['Scenes'] = [s for s in story['Scenes'] if s['Id'] != sid]
                with self.assertRaisesRegex(ValueError, sid + ': missing registered scene'):
                    hub_attachment_lint.integrate(story)

    def test_omitting_harem_does_not_waive_route_registration(self):
        story = copy.deepcopy(self.story)
        # A route-owned control must remain enforced when the harem layer is omitted.
        contract = hub_attachment_lint.gameplay_entry_diagnostics(story)
        control = next(row['scene'] for row in contract if not row['scene'].startswith('household.'))
        story['Scenes'] = [s for s in story['Scenes'] if s['Id'] != control]
        with self.assertRaisesRegex(ValueError, control + ': missing registered scene'):
            hub_attachment_lint.integrate(story, omitted_layers=('harem',))

    def test_j01_historical_reference_hashes_match_the_final_export(self):
        manifest = json.loads((Path(__file__).resolve().parents[1] /
            'tools/route_packs/plans/j01-reference-contexts.json').read_text(encoding='utf-8'))
        for sid in ('herrax.trickster.madam.reachable',
                    'herrax.trickster.madam.reachable_restored'):
            entries = [e for e in manifest['contexts']
                       if (e['scene'], e.get('node'), e['slot'], e['woman']) ==
                       (sid, 'cut', 'text', 'chivarro')]
            self.assertEqual(len(entries), 1)
            scene = next(s for s in self.story['Scenes'] if s['Id'] == sid)
            text = next(n for n in scene['Nodes'] if n['Id'] == 'cut')['Text']
            self.assertEqual(entries[0]['text_sha256'],
                             hashlib.sha256(text.encode('utf-8')).hexdigest())
            self.assertTrue(entries[0]['reason'])

    def test_nidalynn_unreturned_reads_earned_history_after_departure(self):
        model = rules.Model(self.story)
        scene = model.by_id['nidalynn.trickster.epilogue.unreturned']
        self.assertNotIn('nidalynn.present_now', scene['Requires'])
        state = rules.SimState(6, 1000)
        history = {'trickster.ever', 'sacrifice', 'nidalynn.committed',
                   'nidalynn.trickster.bread_kept', 'nidalynn.trickster.cost.salt_eaten',
                   'nidalynn.trickster.left_with_it', 'nidalynn.epoch_unavailable'}
        state.flags.update(history)
        rules.sim_complete(model, state)
        self.assertNotIn('nidalynn.present_now', state.flags)
        self.assertTrue(rules.sim_available(model, scene, state))
        state.flags.discard('nidalynn.trickster.cost.salt_eaten')
        rules.sim_complete(model, state)
        self.assertFalse(rules.sim_available(model, scene, state))


class OptionalBudgetTests(unittest.TestCase):
    def fixture(self):
        scenes = []
        for arc, steps, chapters, retired in (
                ('carried', 2, [3, 5], False), ('new.a', 3, [5], False),
                ('new.b', 3, [5], False), ('retired', 8, [3, 5], True)):
            for index in range(steps):
                scenes.append(dict(Id=f'{arc}.{index}', HouseholdCategory='pair',
                    HouseholdArc=arc, HouseholdArcStart=index == 0,
                    HouseholdWitness=f'{arc}.{index}.done', Chapters=chapters,
                    MinChapter=min(chapters), MaxChapter=max(chapters), DelayHours=0,
                    RestAllowance='household.pair', Requires=['retired'] if retired else [],
                    Forbids=['retired'] if retired else []))
        return {'Scenes': scenes}, {'load_caps': {'5': {'arcs': 2, 'optional': 5}}}

    def test_carried_arc_uses_a_slot_and_retired_arc_uses_no_budget(self):
        story, data = self.fixture()
        self.assertEqual([], harem_schedule_lint.scene_load_errors(story, data))
        data['load_caps']['5']['optional'] = 4
        self.assertTrue(any('optional step sum 5 exceeds 4' in e
                            for e in harem_schedule_lint.scene_load_errors(story, data)))

    def test_reactivating_retired_arc_exposes_its_remaining_steps(self):
        story, data = self.fixture()
        for scene in story['Scenes']:
            if scene['HouseholdArc'] == 'retired':
                scene['Forbids'] = []
        self.assertTrue(any('optional step sum 10 exceeds 5' in e
                            for e in harem_schedule_lint.scene_load_errors(story, data)))
