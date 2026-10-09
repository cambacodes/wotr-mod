"""Route-local regression coverage for the round-2 situations and receipts."""
import json
import os
from pathlib import Path
import unittest

from storylines import hepzamirah_trickster as core, hepzamirah_flesh as flesh


SCENES = {s['Id']: s for s in core.SCENES + flesh.SCENES}


def node(suffix, nid):
    return next(n for n in SCENES[core.P + suffix]['Nodes'] if n['Id'] == nid)


def has_key(block, key):
    return key in block.get('Requires', []) or any(key in g for g in block.get('AnyGroups', []))


class HepzamirahRound2Tests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get('RRT_TEST_STORY'), 'requires the freshly generated export')
    def test_export_keeps_history_answers_and_optional_guest_fallbacks(self):
        from tests.story_fixture import fresh_story
        by = {s['Id']: s for s in fresh_story()['Scenes']}
        for suffix in ['ghost.body', 'body.hounds', 'body.terms', 'bond.eve', 'flesh.sister',
                       'bond.vorlesh', 'flesh.the_nexus', 'bond.the_weapon', 'bond.the_call']:
            s = by[core.P + suffix]
            for flag in s['Requires'] + s['Forbids']:
                self.assertNotIn(flag, ['areelu.closed', 'horzalah.closed', 'iomedae.closed',
                                       'crossroute.areelu.unavailable', 'crossroute.horzalah.unavailable',
                                       'crossroute.iomedae.unavailable', 'crossroute.ember.unavailable'])
        eve = next(n for n in by[flesh.EVE]['Nodes'] if n['Id'] == 'soul')
        self.assertTrue(all('areelu.closed' not in c['Forbids'] for c in eve['Choices']))
        opening = next(n for n in by[core.P + 'body.terms']['Nodes'] if n['Id'] == 'open')
        self.assertGreaterEqual(len(opening['Choices']), 9)
        self.assertEqual([c['Next'] for c in opening['Choices'][:9]],
                         ['ember', 'killed', 'forged', 'confined', 'price', 'killed', 'forged', 'confined', 'price'])

    def test_old_commitment_and_slot_continuations(self):
        self.assertEqual(node('body.terms', 'sealed')['Choices'][0]['Set'], [core.COMMITTED])
        for suffix, nid, receipt in [('body.terms', 'threshold', []),
                                      ('bond.crooked', 'down', [core.P + 'second_night'])]:
            answer = node(suffix, nid)['Choices'][0]
            slot = core.P + suffix + '.explicit.1'
            self.assertEqual(answer['Set'], receipt)
            self.assertEqual(answer['Next'], slot)
            brief = json.loads((Path('tools/route_packs/explicit_slots/hepzamirah') / (slot + '.json')).read_text(encoding='utf-8'))
            self.assertEqual(node(suffix, slot)['Text'], brief['default_text'])
            self.assertEqual(node(suffix, slot)['Choices'][0]['Set'], [])

    def test_altar_is_physical_and_has_a_real_refusal(self):
        s = SCENES[core.P + 'ghost.deed_by_fire']
        self.assertNotIn('Remote', s)
        self.assertEqual(s['Areas'], [core.DREZEN])
        self.assertEqual(s['DelayHours'], 72)
        self.assertEqual(node('ghost.deed_by_fire', 'deed')['Choices'][0]['Crusade']['Amount'], -200)
        self.assertNotIn(core.PRIMED, node('ghost.deed_by_fire', 'deed')['Choices'][0]['Set'])
        self.assertEqual(node('ghost.deed_by_fire', 'answer_from_cell')['Choices'][1]['Set'], [core.CLOSED])
        self.assertIn(core.PRIMED, node('ghost.deed_by_fire', 'crossing')['Choices'][0]['Set'])
        remote = [s for s in core.SCENES if (s.get('Remote') or s.get('Owner') == 'Memory') and s['MinChapter'] == 5]
        self.assertEqual([s["Id"] for s in remote], [core.P + "ghost.body"])

    def test_old_ending_exits_are_inert(self):
        for suffix in ['epilogue.leavable', 'epilogue.leavable_on_record', 'epilogue.commit', 'epilogue.refused']:
            exit = node(suffix, 'page')['Choices'][0]
            self.assertEqual(exit['Set'], [])
            self.assertIsNone(exit['Next'])
            self.assertFalse(exit['Abort'])

    def test_weapon_and_letter_provenance(self):
        for sid in [flesh.BLOODLINE, flesh.FLOWERS, flesh.CORNER]:
            self.assertIn(core.PICK, SCENES[sid]['Requires'])
        room = node('bond.her_room', 'room')['Choices']
        letter = next(c for c in room if c['Next'] == 'room_letter')
        self.assertEqual(letter['Requires'], [core.P + 'princess_letter_kept'])
        self.assertIn(core.P + 'princess_letter_kept', node('flesh.princess', 'silence')['Choices'][0]['Set'])
        self.assertIn(core.P + 'princess_letter_burned', node('flesh.princess', 'burn_say')['Choices'][0]['Set'])

    def test_ember_has_separate_memories_and_no_devastated_cameo(self):
        self.assertNotEqual(core.R2_SEEN_CUES[core.P + 'heard_ember_pity'],
                            core.R2_SEEN_CUES[core.P + 'heard_ember_apple'])
        for sid in [flesh.FLOWERS, flesh.EMBER_ASKS, core.P + 'react.ember']:
            self.assertIn('ember.native_devastated', SCENES[sid]['Forbids'])
        requires = node('body.terms', 'open')['Choices'][0]['Requires']
        self.assertIn(core.P + 'ember_messenger', requires)
        # The narrator still reaches terms without the optional messenger.
        self.assertTrue(any(c['Next'] != 'ember' and not c['Requires']
                            for c in node('body.terms', 'open')['Choices']))

    def test_sister_cameo_requires_actual_return_and_current_presence(self):
        c = node('body.hounds', 'sister_at_gate')['Choices'][0]
        self.assertEqual(c['Requires'], [core.P + 'sister_here'])
        self.assertEqual(core.DERIVED[core.P + 'sister_here'][0][:2],
                         ['horzalah.trickster.returned', 'horzalah.present_now'])
        self.assertNotIn('horzalah.trickster.returned', SCENES[core.P + 'body.hounds']['Requires'])
        self.assertEqual(node('body.hounds', 'sister_at_gate')['Choices'][1]['Forbids'], [core.P + 'sister_here'])

    def test_hunt_records_departure_before_elapsed_outcomes(self):
        for nid, suffix, hours in [('shadow', 'bond.hunt_shadow', 72), ('caught', 'bond.hunt_caught', 24)]:
            self.assertNotIn('comes in', node('bond.the_hunt', nid)['Text'])
            outcome = SCENES[core.P + suffix]
            self.assertIn(flesh.HUNT, outcome['Requires'])
            self.assertEqual(outcome['DelayHours'], hours)
            self.assertNotEqual(outcome.get('ContactUnit'), core.BODY_UNIT)
            self.assertEqual(outcome['AnswerLists'], ['6dccfd39947ef4242a8afbe36b21a46c'])
            self.assertNotIn('Remote', outcome)
            self.assertNotEqual(outcome['Owner'], 'Memory')
        self.assertEqual(SCENES[flesh.EYE]['DelayHours'], 120)
        self.assertEqual(core.PRESENCES[core.PRESENCE]['ContactWindows'][0]['MinAgeHours'], 120)

    def test_military_results_have_separate_decision_clocks(self):
        drill = SCENES[core.P + 'flesh.drill_result']
        scouts = SCENES[core.P + 'bond.scouts_result']
        self.assertEqual(drill['DelayHours'], 168)
        self.assertIn(flesh.DRILL, drill['Requires'])
        self.assertIn(core.P + 'drilled_troops', drill['Requires'])
        self.assertEqual(scouts['DelayHours'], 24)
        self.assertIn(flesh.COUNCIL, scouts['Requires'])
        self.assertIn(core.P + 'council_heard', scouts['Requires'])
        self.assertIn('unfit to march', node('flesh.drill_result', 'harsh')['Text'])

    def test_debts_read_only_their_earned_branch_and_respect_mortality(self):
        live = node('epilogue.leavable', 'page')['Paragraphs']
        dead = node('epilogue.leavable_on_record', 'page')['Paragraphs']
        for flag in [core.FAVOUR_OWED, core.CALL_FORBIDDEN, core.P + 'vorlesh_first']:
            self.assertTrue(any(has_key(p, flag) for p in live), flag)
        for suffix in ['epilogue.commit', 'epilogue.refused']:
            self.assertTrue(any(has_key(p, core.FAVOUR_OWED)
                                for p in node(suffix, 'page')['Paragraphs']), suffix)
        self.assertIn('favor for sparing', dead[0]['Text'])
        self.assertIn('died with the Commander', dead[0]['Text'])
        self.assertIn('sacrifice', SCENES[core.P + 'epilogue.leavable_on_record']['Requires'])
        self.assertIn('trickster.commander_back', SCENES[core.P + 'epilogue.leavable_on_record']['Forbids'])

    def test_political_cover_never_claims_external_recognition(self):
        for suffix, nid in [('flesh.chaplains', 'embassy'), ('bond.nerosyan', 'embassy_reply'),
                             ('bond.treaty', 'back')]:
            text = node(suffix, nid)['Text'].lower()
            self.assertNotIn('one lich', text)
            self.assertNotIn('canon law', text)
            self.assertNotIn('cannot touch', text)
        self.assertEqual(node('bond.nerosyan', 'embassy_reply')['Choices'][0]['Crusade']['Amount'], -300)


if __name__ == '__main__':
    unittest.main()
