"""Round-2 Aranka graph continuity and saved payoff receipts."""
from copy import deepcopy
from pathlib import Path
import unittest
from storylines import aranka_continuation as island, aranka_trickster as route
ROOT = Path(__file__).resolve().parents[1]
SCENES = {s['Id']: s for s in [*route.SCENES, *island.SCENES]}

def nodes(scene):
    return {n['Id']: n for n in scene['Nodes']}

class ArankaRound2Tests(unittest.TestCase):

    def test_every_slot_is_unique_and_state_free(self):
        briefs = list((ROOT / 'tools/route_packs/explicit_slots/aranka').glob('*.json'))
        for brief in briefs:
            slot_id = brief.stem
            scene = SCENES[slot_id.rsplit('.explicit.', 1)[0]]
            slots = [n for n in scene['Nodes'] if n['Id'] == slot_id]
            slots += [p for n in scene['Nodes'] for p in n.get('Paragraphs', []) if p.get('Id') == slot_id]
            with self.subTest(slot=slot_id):
                dispatch_1, = slots
                for choice in slots[0].get('Choices', []):
                    self.assertEqual(choice['Set'], [])
                    self.assertFalse(choice['Abort'])

    def test_all_roof_siblings_return_to_the_saved_morning_receipt(self):
        roofs = [s for s in route.SCENES if s['Id'].startswith(('aranka.trickster.verse.encore', 'aranka.trickster.verse.third_verse'))]
        self.assertEqual({s['Id'] for s in roofs}, {'aranka.trickster.verse.' + family + suffix for family in ('encore', 'third_verse') for suffix in ('', '_late', '_yard', '_yard_late')})
        for scene in roofs:
            graph = nodes(scene)
            slot_id = scene['Id'] + '.explicit.1'
            ordered_answer_2, *ordered_answer_2_rest = graph['threshold']['Choices']
            self.assertEqual(ordered_answer_2['Next'], slot_id)
            ordered_answer_3, *ordered_answer_3_rest = graph[slot_id]['Choices']
            self.assertEqual(ordered_answer_3['Next'], 'morning')
            ordered_answer_4, *ordered_answer_4_rest = graph['morning']['Choices']
            self.assertEqual(ordered_answer_4['Set'], [route.NIGHT])
            ordered_answer_5, *ordered_answer_5_rest = graph['morning']['Choices']
            self.assertIsNone(ordered_answer_5['Next'])
            ordered_answer_6, *ordered_answer_6_rest = graph['song_counter']['Choices']
            self.assertEqual(ordered_answer_6['Set'], [route.NIGHT])
            self.assertEqual(scene['DelayHours'], 24 if scene['Id'].endswith('_late') else 72)

    def test_commitment_and_closure_choices_keep_their_indices_and_effects(self):
        for scene in route.SCENES:
            if scene['Id'].startswith('aranka.trickster.verse.encore'):
                choice = nodes(scene)['choice']['Choices']
                self.assertEqual([(c['Next'], c['Set']) for c in choice], [('stay', [route.KEPT]), ('not_yet', []), ('stage', [route.CLOSED, route.NEROSYAN])])
            elif scene['Id'].startswith('aranka.trickster.verse.third_verse'):
                choice = nodes(scene)['start']['Choices']
                self.assertEqual([(c['Next'], c['Set']) for c in choice], [('sung', [route.KEPT, route.SANG_ALONE]), ('refused', [route.CLOSED])])

    def test_all_letter_receipts_follow_bodily_arrival(self):
        deliveries = [s for s in route.SCENES if s['Id'] in ('aranka.trickster.verse.her_letter', 'aranka.trickster.verse.her_letter_late', 'aranka.trickster.verse.any_tavern', 'aranka.trickster.failure.second_verse', 'aranka.trickster.failure.second_verse_late', 'aranka.trickster.failure.mocking_verse_any')]
        self.assertEqual({s['Id'] for s in deliveries}, {'aranka.trickster.verse.her_letter', 'aranka.trickster.verse.her_letter_late', 'aranka.trickster.verse.any_tavern', 'aranka.trickster.failure.second_verse', 'aranka.trickster.failure.second_verse_late', 'aranka.trickster.failure.mocking_verse_any'})
        for scene in deliveries:
            if not scene.get('Remote'):
                self.assertTrue(scene.get('InteractionHub'), scene['Id'])
                continue
            for node in scene['Nodes']:
                if any((route.ANSWERED in c['Set'] for c in node['Choices'])):
                    for answer in node['Choices']:
                        if route.ANSWERED in answer['Set']:
                            self.assertIn('aranka.extension_started', answer['Set'])
                            if scene['Id'].startswith('aranka.trickster.failure.'):
                                self.assertIn(route.RETURNED, answer['Set'])
                    self.assertNotIn(route.MORAL_REPAIRED, [f for c in node['Choices'] for f in c['Set']])

    def test_each_duet_pays_apology_before_the_same_billing_receipts(self):
        for scene in route.SCENES:
            if not scene['Id'].startswith('aranka.trickster.verse.duet'):
                continue
            graph = nodes(scene)
            for opening in ('vandal', 'denied', 'mocking', 'posters'):
                self.assertEqual(['duet', 'duet_rival'], [c['Next'] for c in graph[opening]['Choices']])
            ordered_answer_7, *ordered_answer_7_rest = graph['signed']['Choices']
            self.assertEqual(ordered_answer_7['Set'], [route.DUET, route.CREDITED])
            ordered_answer_8, *ordered_answer_8_rest = graph['billing']['Choices']
            self.assertEqual(ordered_answer_8['Set'], [route.DUET, route.VAIN])

    def test_island_night_keeps_legacy_exit_and_deferral_bypasses_hollow_slot(self):
        graph = nodes(SCENES['aranka.no_encore_needed'])
        ordered_answer_9, *ordered_answer_9_rest = graph['desire']['Choices']
        self.assertEqual(ordered_answer_9['Next'], 'night_initiation')
        ordered_answer_10, *ordered_answer_10_rest = graph['night']['Choices']
        self.assertEqual(ordered_answer_10['Set'], ['aranka.extension_night', 'aranka.extension_kept'])
        for name, flag in (('kiss', 'extension_kiss'), ('quiet', 'extension_quiet')):
            ordered_answer_11, *ordered_answer_11_rest = graph[name]['Choices']
            self.assertEqual(ordered_answer_11['Set'], ['aranka.' + flag, route.KEPT])
        graph = nodes(SCENES['aranka.the_story_that_follows'])
        ordered_answer_12, *ordered_answer_12_rest = graph['private']['Choices']
        self.assertEqual(ordered_answer_12['Next'], 'aranka.the_story_that_follows.explicit.1')
        ordered_answer_13_prior_0, ordered_answer_13, *ordered_answer_13_rest = graph['private']['Choices']
        self.assertIsNone(ordered_answer_13['Next'])
        ordered_answer_14, *ordered_answer_14_rest = graph['hollow_morning']['Choices']
        self.assertEqual(ordered_answer_14['Set'], ['aranka.story_conversation_done'])

    def test_native_reunion_locations_are_mutually_exclusive_and_exit_unchanged(self):
        page = SCENES['aranka.trickster.epilogue.commit']['Nodes'][0]
        self.assertEqual(page['Id'], 'end')
        self.assertEqual([{k: v for k, v in c.items() if k != 'Text'} for c in page['Choices']], [dict(Next=None, Set=[], Requires=[], Forbids=[], Abort=False)])
        parts = page['Paragraphs']
        stay = next((p for p in parts if p.get('Requires') == [route.COMMANDER_STAYS]))
        leave = next((p for p in parts if p.get('Requires') == [route.COMMANDER_LEAVES]))
        self.assertEqual(stay['Requires'], [route.COMMANDER_STAYS])
        self.assertEqual(stay['Forbids'], [route.COMMANDER_LEAVES])
        self.assertEqual(leave['Requires'], [route.COMMANDER_LEAVES])
        self.assertIn('sacrifice', SCENES['aranka.trickster.epilogue.commit']['Forbids'])

    def test_thall_contact_is_native_living_and_does_not_create_a_partner(self):
        contact = SCENES['aranka.thall.answer']
        self.assertEqual(contact['ContactUnit'], '8fb65bd79574771429526eaef26762a9')
        self.assertEqual(contact['AdditionalContactUnits'], [island.ACTOR])
        self.assertEqual(contact['Areas'], [island.AREA])
        self.assertIn(route.THALL_DEAD, contact['Forbids'])
        graph = nodes(contact)
        self.assertEqual(graph['answer']['SpeakerUnit'], contact['ContactUnit'])
        ordered_answer_15, *ordered_answer_15_rest = graph['answer']['Choices']
        self.assertEqual(ordered_answer_15['Set'], [route.THALL_ANSWERED])
        self.assertNotIn('aranka.extension_kept', contact['Requires'])
        self.assertFalse(any(('partner_stance' in f for node in contact['Nodes'] for c in node['Choices'] for f in c['Set'])))

    def test_correspondence_requires_dispatch_and_does_not_gate_romance(self):
        reply = SCENES['aranka.thall.reply']
        self.assertIn(route.THALL_REQUESTED, reply['Requires'])
        self.assertIn(route.THALL_SAFE, reply['Requires'])
        self.assertIn(route.THALL_DEAD, reply['Forbids'])
        self.assertEqual(reply['DelayHours'], 24)
        for sid in ('aranka.thall.answer', 'aranka.thall.question', 'aranka.thall.question_yard', 'aranka.thall.reply'):
            self.assertIn('aranka.present_now', SCENES[sid]['Requires'])
        ordered_answer_16, *ordered_answer_16_rest = nodes(reply)['start']['Choices']
        self.assertEqual(ordered_answer_16['Set'], [route.THALL_ANSWERED])
        for scene in SCENES.values():
            if scene['Id'].startswith(('aranka.trickster.verse.encore', 'aranka.trickster.verse.third_verse')):
                self.assertNotIn(route.THALL_REQUESTED, scene['Requires'])
                self.assertNotIn(route.THALL_ANSWERED, scene['Requires'])

    def test_thall_conclusions_follow_contact_death_and_terminal_ownership(self):
        for ending in ('commit', 'verse', 'declined', 'unanswered', 'nerosyan'):
            parts = route.thall_ending('aranka.trickster.epilogue.' + ending)
            alive, unknown, dead = parts
            self.assertIn(route.THALL_ANSWERED, alive['Requires'])
            self.assertIn(route.THALL_DEAD, alive['Forbids'])
            self.assertIn(route.THALL_REQUESTED, unknown['Requires'])
            self.assertIn(route.THALL_ANSWERED, unknown['Forbids'])
            self.assertIn(route.THALL_DEAD, dead['Requires'])
            self.assertEqual('aranka.thall.coda_delivered' in alive['Forbids'], ending in ('commit', 'verse'))
        self.assertIn(route.LATE_COMMITTED, route.thall_ending('aranka.trickster.epilogue.verse')[0]['Forbids'])

    def test_merged_adapter_preserves_saved_nodes_without_forcing_thall_discussion(self):
        from storylines import endings_job3
        events = {sid: deepcopy(event) for sid, event in SCENES.items()}
        events['aranka.lastcall.page'] = dict(Id='aranka.lastcall.page', Nodes=[dict(Id='page', Paragraphs=[])])
        events['aranka.lastcall.call'] = dict(Id='aranka.lastcall.call', Nodes=[dict(Id='call', Text='The song')])
        payload = dict(Derived={})
        endings_job3.aranka(payload, events)
        for sid, event in events.items():
            targets = ('signed', 'billing') if sid.startswith('aranka.trickster.verse.duet') else ('desire',) if sid == 'aranka.no_encore_needed' else ()
            for target in targets:
                graph = nodes(event)
                old = nodes(SCENES[sid])[target]['Choices']
                choices = graph[target]['Choices']
                self.assertIn('thall_' + target, graph)
                self.assertIn('thall_dead_' + target, graph)
                for choice in choices[len(old):len(old) + 2]:
                    self.assertIn('trickster.ever', choice['Requires'])
                    self.assertIn('trickster.ever', choice['Forbids'])
                restored = [c for c in choices if c.get('Next') in {a.get('Next') for a in old} and 'trickster.ever' in c.get('Requires', ()) and ('trickster.ever' not in c.get('Forbids', ()))]
                self.assertEqual([(c['Next'], c['Set']) for c in restored], [(c['Next'], c['Set']) for c in old])
                self.assertTrue(all(('trickster.ever' in c['Requires'] for c in restored)))
if __name__ == '__main__':
    unittest.main()
