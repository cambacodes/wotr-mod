"""Arueshalae's alternative courtships and the existing no-hands promise."""
import copy
import json
from pathlib import Path
import unittest
from tools import savecompat
from storylines import arueshalae_trickster, arueshalae_treatment, arueshalae_rounds, arueshalae_chapel, arueshalae_hours, arueshalae_notes
from storylines import arueshalae_round2 as polish

class RoundTwoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.before = {'Scenes': copy.deepcopy([s for m in (arueshalae_trickster, arueshalae_treatment, arueshalae_rounds, arueshalae_chapel, arueshalae_hours, arueshalae_notes) for s in m.SCENES])}
        cls.story = copy.deepcopy(cls.before)
        polish.integrate(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next((n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid))

    def held(self, flags, key):
        if key in self.story.get('Derived', {}):
            return not any((self.held(flags, f) for f in self.story.get('DerivedForbids', {}).get(key, []))) and any((all((self.held(flags, f) for f in g)) for g in self.story['Derived'][key]))
        return key in flags

    def visible(self, choice, flags):
        return all((self.held(flags, f) for f in choice['Requires'])) and (not any((self.held(flags, f) for f in choice['Forbids'])))

    def test_original_save_identities_and_exit_effects_survive(self):
        self.assertEqual([], savecompat.check(self.story, savecompat.inventory(self.before)))
        for old in self.before['Scenes']:
            if 'epilogue' not in old['Id']:
                continue
            for old_node in old['Nodes']:
                new = self.node(old['Id'], old_node['Id'])
                keys = ('Set', 'Abort', 'Revive', 'RemoveItem', 'NativeNext', 'StartEtude')
                self.assertEqual([[a.get(k) for k in keys] for a in old_node['Choices']], [[a.get(k) for k in keys] for a in new['Choices']])

    def test_fast_blocks_all_four_contacts_and_keeps_noncontact_choices(self):
        t = polish.T
        for hour in (24, 167, 168):
            for suffix, nid, ordinary_target in [('old_name', 'offer', 'didnt'), ('the_dance', 'start', 'dance_sleeve'), ('abyss_dose', 'start', 'sit'), ('the_scar', 'mark', 'keep')]:
                choices = self.node(t + suffix, nid)['Choices']
                touch, = [c for c in choices if c.get('RemoveItem') == '89e10c3f21fa50c4b8719e004c7628d3']
                ordinary = next((c for c in choices if c['Next'] == ordinary_target))
                flags = {t + 'fast', t + 'touched', 'arueshalae.ward_held'}
                self.assertFalse(self.visible(touch, flags))
                self.assertTrue(self.visible(ordinary, flags))
                flags.add(t + 'prescription')
                self.assertTrue(self.visible(touch, flags))
        proposal = self.scenes[t + 'prescription']
        self.assertEqual(168, proposal['DelayHours'])
        self.assertIn(t + 'relapse_two', proposal['Requires'])

    def test_fast_walk_rejects_intervening_hands_then_earns_proposal(self):
        t = polish.T
        flags = {'trickster.ever', t + 'intake', t + 'touched', 'arueshalae.ward_held'}
        times = {'trickster.ever': -1000, t + 'intake': -900, t + 'touched': -800}
        ordered_answer_1, *ordered_answer_1_rest = self.node(t + 'relapse_two', 'ask')['Choices']
        fast = ordered_answer_1
        for flag in fast['Set']:
            flags.add(flag)
            times[flag] = 0
        before = set(flags)
        for hour, suffix, nid, index in ((24, 'old_name', 'offer', 2), (48, 'the_dance', 'start', 1), (96, 'abyss_dose', 'start', 2), (167, 'the_scar', 'mark', 1)):
            choice, = [c for c in self.node(t + suffix, nid)['Choices'] if c.get('RemoveItem') == '89e10c3f21fa50c4b8719e004c7628d3']
            self.assertFalse(self.visible(choice, flags), (hour, suffix))
            self.assertEqual(before, flags)
        proposal = self.scenes[t + 'prescription']
        latest = max((times.get(k, -1000) for k in proposal['Requires']))
        self.assertLess(167 - latest, proposal['DelayHours'])
        self.assertEqual(168, 168 - latest)
        self.assertTrue(all((self.held(flags, k) for k in proposal['Requires'])))
        self.assertFalse(any((self.held(flags, k) for k in proposal['Forbids'])))
        for nid in ('start', 'fast', 'risk'):
            self.assertTrue(any((self.visible(a, flags) for a in self.node(t + 'prescription', nid)['Choices'])))
        ordered_answer_2, *ordered_answer_2_rest = self.node(t + 'prescription', 'ask')['Choices']
        acceptance = ordered_answer_2
        flags.update(acceptance['Set'])
        flags.add(t + 'prescription')
        self.assertIn('arueshalae.committed', flags)
        self.assertFalse(self.held(flags, polish.FAST_ACTIVE))

    def test_untreated_morning_has_selectable_answer_in_both_states(self):
        sid = polish.T + 'morning'
        for changed, nid in ((False, 'count'), (True, 'count_e')):
            flags = {polish.CHANGED} if changed else set()
            start = self.node(sid, 'start')
            available = [a for a in start['Choices'] if self.visible(a, flags)]
            self.assertEqual(['ordinary'], [a['Next'] for a in available])
            self.assertEqual([nid], [a['Next'] for a in self.node(sid, 'ordinary')['Choices'] if self.visible(a, flags)])
            answers = [a for a in self.node(sid, nid)['Choices'] if self.visible(a, flags)]
            dispatch_3, = answers
            answer_in_order_1, *answer_in_order_1_following = answers
            self.assertEqual([polish.T + 'morning'], answer_in_order_1['Set'])

    def displayed(self, scene):
        yield scene.get('Title', '')
        yield scene.get('Entry', '')
        for nd in scene['Nodes']:
            yield nd['Text']
            for par in nd.get('Paragraphs', []):
                yield par['Text']
            for answer in nd['Choices']:
                yield answer['Text']

    def test_morning_first_dream_variants_preserve_answer_positions(self):
        sid = polish.T + 'morning'
        fact = 'native.history.arueshalae.first_dream'
        for changed in (False, True):
            for seen in (False, True):
                flags = {polish.INTAKE} | ({polish.CHANGED} if changed else set()) | ({fact} if seen else set())
                first, = [a for a in self.node(sid, 'start')['Choices'] if self.visible(a, flags)]
                dispatch, = [a for a in self.node(sid, first['Next'])['Choices'] if self.visible(a, flags)]
                count_id = ('count_e' if changed else 'count') + ('.first_dream_seen' if seen and (not changed) else '')
                self.assertEqual(count_id, dispatch['Next'])
                expected = [('recovering_e' if changed else 'recovering') + ('.first_dream_seen' if seen else ''), 'doctor_e' if changed else 'doctor' + ('.first_dream_seen' if seen else '')]
                saved = self.node(sid, 'count_e' if changed else 'count')['Choices']
                recovering, doctor, *other_answers = saved
                self.assertEqual(['recovering_e', 'doctor_e'] if changed else ['recovering', 'doctor'],
                                 [recovering['Next'], doctor['Next']])
                choices = self.node(sid, count_id)['Choices']
                targets = [a['Next'] for a in choices if self.visible(a, flags) and a['Next'].startswith(('recovering', 'doctor'))]
                self.assertEqual(set(expected), set(targets))
                self.assertEqual(len(targets), len(set(targets)))
                self.assertTrue(set(expected) <= {n['Id'] for n in self.scenes[sid]['Nodes']})

    def test_old_acquaintance_callback_histories_are_disjoint(self):
        sid = polish.T + 'old_acquaintance'
        for confessed in (False, True):
            for touched in (False, True):
                flags = {polish.T + 'touched'} | ({polish.T + 'relapse'} if confessed else set()) | ({polish.T + 'cure_works'} if touched else set())
                for incoming, retained, earned in (('sister', 'offer', confessed), ('claws', 'after_claws', confessed and touched)):
                    answer, = [a for a in self.node(sid, incoming)['Choices'] if self.visible(a, flags)]
                    expected = ('offer' if confessed else 'offer.unheard') if incoming == 'sister' else (
                        'after_claws' if confessed and touched else 'after_claws.confession_only' if confessed else
                        'after_claws.touch_only' if touched else 'after_claws.no_callbacks')
                    self.assertEqual(expected, answer['Next'])
                    self.assertEqual(earned, answer['Next'] == retained)
                    self.assertIn(answer['Next'], {n['Id'] for n in self.scenes[sid]['Nodes']})

    def test_epilogue_recollections_require_prescription_answer(self):
        t, p = (polish.T, polish.P)
        answers = self.node(t + 'prescription', 'ask')['Choices']
        for index, result in enumerate(('both', 'saint', 'not_yet', 'neither')):
            answer = next((a for a in answers if a['Next'] == result))
            self.assertIn(t + 'prescription.' + result, answer['Set'])
        commit = next((a for a in self.node(p + 'epilogue.commit', 'page')['Paragraphs'] if t + 'prescription.both' in a.get('Requires', ())))
        self.assertIn(t + 'prescription.both', commit['Requires'])
        declined = self.node(p + 'epilogue.declined', 'page')['Paragraphs'][-2:]
        for paragraph, result in zip(declined, ('saint', 'not_yet')):
            flags = {t + 'relapse_two', p + 'cost.saint_only'} if result == 'saint' else {t + 'relapse_two'}
            self.assertFalse(self.visible(paragraph, flags))
            flags.add(t + 'prescription.' + result)
            self.assertTrue(self.visible(paragraph, flags))

    def test_chapter_four_edge_beat_costs_something(self):
        t = polish.T
        beat = self.scenes[t + 'old_acquaintance']
        self.assertEqual((4, 4, [4]), (beat['MinChapter'], beat['MaxChapter'], beat['Chapters']))
        self.assertEqual([arueshalae_treatment.MIDDLE_CITY], beat['Areas'])
        self.assertIn(t + 'intake', beat['Requires'])
        answers = self.node(t + 'old_acquaintance', 'offer')['Choices']
        costs = [arueshalae_treatment.ACQ_VOICE, arueshalae_treatment.ACQ_CLAWS, arueshalae_treatment.ACQ_LEASH]
        self.assertEqual([[arueshalae_treatment.ACQ, cost] for cost in costs], [a['Set'] for a in answers])
        self.assertFalse(any((a['Abort'] for a in answers)))
        answer_in_order_2_before_0, answer_in_order_2_before_1, answer_in_order_2, *answer_in_order_2_following = answers
        self.assertEqual('PlayerIsTrickster', answer_in_order_2['Mythic'])
        start = self.node(t + 'old_name', 'start')['Choices']
        answer_in_order_3, *answer_in_order_3_following = start
        self.assertIn(arueshalae_treatment.ACQ, answer_in_order_3['Forbids'])
        self.assertEqual([[c] for c in costs], [a['Requires'] for a in start[1:]])
        for answer in start[1:]:
            self.assertEqual(['didnt', 'hand'], [c['Next'] for c in self.node(t + 'old_name', answer['Next'])['Choices']])

    def test_changed_chaplain_question_and_refusal_are_not_hunger(self):
        sid = polish.P + 'terms'
        choices = self.node(sid, 'chaplain')['Choices']
        self.assertEqual(['question_changed'], [a['Next'] for a in choices if self.visible(a, {polish.CHANGED})])
        changed = self.node(sid, 'question_changed')
        self.assertEqual('saint_e', next((a for a in changed['Choices'] if a['Next'] == 'saint_e'))['Next'])

    def test_slots_are_alternatives_and_default_cuts_reach_original_aftermath(self):
        briefs = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/arueshalae'
        expected = {'arueshalae.treatment.night.explicit.1': 'morning_after_paid', 'arueshalae.treatment.night.explicit.2': 'morning_after', 'arueshalae.trickster.fallen.roof.explicit.1': 'after', 'arueshalae.trickster.evil.window.explicit.1': 'after', 'arueshalae.trickster.evil.window_yard.explicit.1': 'after'}
        self.assertEqual(set(expected), {p.stem for p in briefs.glob('*.json')})
        for key, dest in expected.items():
            sid = key.rsplit('.explicit.', 1)[0]
            nd = self.node(sid, key)
            ordered_answer_4, *ordered_answer_4_rest = nd['Choices']
            self.assertEqual(dest, ordered_answer_4['Next'])
            ordered_answer_5, *ordered_answer_5_rest = nd['Choices']
            self.assertEqual([], ordered_answer_5['Set'])
            brief = json.loads((briefs / (key + '.json')).read_text(encoding='utf-8'))
        undress = self.node(polish.T + 'night', 'undress')
        for flags in (set(), {polish.CHANGED}):
            answer, = [a for a in undress['Choices'] if self.visible(a, flags)]
            self.assertIn(answer['Next'], expected)

    def test_history_callbacks_require_all_producers(self):
        t = polish.T
        ordered_answer_6_prior_0, ordered_answer_6, *ordered_answer_6_rest = self.node(t + 'the_eve', 'fear')['Choices']
        list_answer = ordered_answer_6
        for missing in ('rx_want', 'mealtimes', 'kitchen', 'relapse'):
            flags = {t + x for x in ('rx_want', 'mealtimes', 'kitchen', 'relapse') if x != missing}
            self.assertFalse(self.visible(list_answer, flags))
        self.assertIn(t + 'intake', self.scenes[t + 'react.sosiel_morning']['Requires'])
        self.assertIn(t + 'night.warded', self.scenes[t + 'react.sosiel_morning']['Requires'])

    def test_contact_locations_and_cat_earliest_history(self):
        for sid in (polish.T + 'the_cat', polish.T + 'the_novice', polish.T + 'rainy_day', polish.P + 'chaplain.prayer'):
            self.assertEqual([polish.DREZEN], self.scenes[sid]['Areas'])
        cat = self.scenes[polish.T + 'the_cat']
        self.assertEqual(24, cat['DelayHours'])
if __name__ == '__main__':
    unittest.main()
