"""Round 2: replay native reports, lifetime branches, and all chosen hunt deliveries."""
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story
from tests.test_DelamerePolish import P, matches, play
from tools.rrt_verify import Model

class DelamereRound2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = cls.model.by_id
        play.model = cls.model

    def test_reports_require_native_outcome_or_witness(self):
        self.assertEqual('d2b8c3609b202124fb39a364e20ae76b', self.story['UnlockableFlags'][P + 'zanedra.native_killed'])
        self.assertEqual(['cb268637168a0d3478bec0d97f10215c'], self.story['SeenCues'][P + 'zanedra.west_heard'])
        node = next((n for n in self.scenes[P + 'woken.feasting_table']['Nodes'] if n['Id'] == 'finish'))
        for flags, expected in ((set(), ['told_lost']), ({P + 'zanedra.west_heard'}, ['told_fled', 'told_lost']), ({P + 'zanedra.native_killed'}, ['told_dead', 'told_lost']), ({P + 'zanedra.native_killed', P + 'zanedra.west_heard'}, ['told_dead', 'told_lost'])):
            self.assertEqual(expected, [c['Next'] for c in node['Choices'] if matches(c, flags | {'chapter_later'})])

    def test_waking_snapshot_precedes_all_refusals(self):
        for suffix in ('crypt.stag', 'crypt.stag_alone', 'crypt.stag_late', 'drezen.stag'):
            for dead in (False, True):
                flags, _ = play(self.scenes[P + suffix], {'delamere.tomb_opened'} | ({'kyado.dead'} if dead else set()), choices={'lady': 2})
                self.assertIn(P + 'kyado.' + ('dead_at_wake' if dead else 'alive_at_wake'), flags)
                self.assertNotIn(P + 'kyado.' + ('alive_at_wake' if dead else 'dead_at_wake'), flags)
                self.assertIn('delamere.closed', flags)
                self.assertNotIn(P + 'returned', flags)

    def test_dead_at_wake_dead_later_and_legacy_acquaintance(self):
        table = self.scenes[P + 'woken.feasting_table']
        for flags, target in (({P + 'kyado.dead_at_wake'}, 'kyado_cairn'), ({P + 'kyado.alive_at_wake', P + 'woke_with_kyado'}, 'kyado_later'), ({P + 'woke_with_kyado'}, 'kyado_later'), ({P + 'kyado.dead_at_wake', P + 'woke_in_drezen'}, 'kyado_unknown'), (set(), 'kyado_unknown')):
            got, seen = play(table, flags | {'kyado.dead'})
            self.assertIn(target, seen)
            self.assertIn(P + 'kyado.mourned', got)
            if target != 'kyado_cairn':
                self.assertNotIn('kyado_cairn', seen)

    def test_all_hunts_reopen_chapel_oath_and_preserve_no_roads(self):
        for suffix in ('woods.second_hunt', 'woods.second_hunt_page', 'woods.second_hunt_late'):
            hunt = self.scenes[P + suffix]
            seed = {P + 'second_hunt_offered', P + 'lied_erastil', P + 'old_deadeye'}
            got, seen = play(hunt, seed)
            self.assertIn('chapel_oath', seen)
            self.assertIn(P + 'confessed', got)
            self.assertIn('delamere.committed', got)
            self.assertIn(P + suffix + '.explicit.1', seen)
            got, seen = play(hunt, seed, choices={'chapel_oath': 1})
            self.assertIn('delamere.closed', got)
            self.assertNotIn(P + suffix + '.explicit.1', seen)
            for index in (1, 2):
                got, seen = play(hunt, {P + 'second_hunt_offered', P + 'told_truth'}, choices={'choice': index})
                self.assertNotIn(P + suffix + '.explicit.1', seen)
                self.assertNotIn('delamere.committed', got)

    def test_four_boundary_mornings_and_optional_demon_test(self):
        for suffix in ('woods.second_hunt', 'woods.second_hunt_page', 'woods.second_hunt_late'):
            for outcome in ('given', 'forced', 'refused', 'clans'):
                got, seen = play(self.scenes[P + suffix], {P + 'told_truth', P + 'village.' + outcome})
                self.assertIn('boundary_' + outcome, seen)
                self.assertIn('boundary_answer', seen)
                self.assertIn('delamere.committed', got)
                self.assertNotIn(P + 'demon_hunted', got)
        for result in ('Success', 'Failure'):
            got, seen = play(self.scenes[P + 'woken.demon'], set(), checks={'SkillStealth': result})
            self.assertIn('where', seen)
            self.assertIn('after_clean' if result == 'Success' else 'after_hurt', seen)
            self.assertIn(P + 'demon_hunted', got)
            self.assertNotIn('delamere.committed', got)

    def test_briefs_match_slots_and_legacy_ending_exit_stays_terminal(self):
        root = Path(__file__).resolve().parents[1]
        for path in (root / 'tools/route_packs/explicit_slots/delamere').glob('*.json'):
            brief = json.loads(path.read_text(encoding='utf-8'))
            sid = brief.get('host_scene', path.stem.rsplit('.explicit.', 1)[0])
            nid = brief.get('host_node', path.stem)
            scene = self.scenes[sid]
            slots = [n for n in scene['Nodes'] if n['Id'] == nid]
            slots += [p for n in scene['Nodes'] for p in n.get('Paragraphs', []) if p.get('Id') == nid]
            slot, = slots
            self.assertEqual(slot['Id'], nid)
            if slot.get('Choices'):
                self.assertTrue(all(not c.get('Abort') for c in slot['Choices']))
        late = self.scenes[P + 'epilogue.late']['Nodes'][0]
        ordered_answer_2, *ordered_answer_2_rest = late['Choices']
        self.assertIsNone(ordered_answer_2['Next'])
        ordered_answer_3, *ordered_answer_3_rest = late['Choices']
        self.assertEqual([], ordered_answer_3['Set'])
        self.assertIn('delamere.committed', self.scenes[P + 'epilogue.late']['Forbids'])
        for suffix in ('caught', 'late', 'unfinished', 'apart', 'never', 'healed'):
            self.assertIn('sacrifice', self.scenes[P + 'epilogue.' + suffix]['Forbids'])

    def test_memorial_stays_with_the_dead_and_hide_names_stay_local(self):
        memorial = self.scenes[P + 'woken.names']
        node = next((n for n in memorial['Nodes'] if n['Id'] == 'names'))
        self.assertEqual(['how_many', 'look'], [c['Next'] for c in node['Choices']])
        for branch in (0, 1):
            flags, seen = play(memorial, set(), choices={'names': branch})
            self.assertIn('how_many', seen)
            self.assertIn(P + 'names_cut', flags)
        hide = self.scenes[P + 'woken.hide']
        paid = next((n for n in hide['Nodes'] if n['Id'] == 'names_paid'))
        for suffix in ('crypt.stag', 'crypt.stag_alone', 'crypt.stag_late', 'drezen.stag'):
            flags, seen = play(self.scenes[P + suffix], {'delamere.tomb_opened'})
            self.assertIn('moonset', seen)
if __name__ == '__main__':
    unittest.main()
