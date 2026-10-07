"""Arueshalae's alternative courtships and the existing no-hands promise."""
import copy
import json
from pathlib import Path
import unittest

from tools import savecompat
from storylines import (arueshalae_trickster, arueshalae_treatment, arueshalae_rounds,
                        arueshalae_chapel, arueshalae_hours, arueshalae_notes)
from storylines import arueshalae_round2 as polish


class RoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = {'Scenes': copy.deepcopy([s for m in (
            arueshalae_trickster, arueshalae_treatment, arueshalae_rounds,
            arueshalae_chapel, arueshalae_hours, arueshalae_notes) for s in m.SCENES])}
        cls.story = copy.deepcopy(cls.before)
        polish.integrate(cls.story)
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def held(self, flags, key):
        if key in self.story.get('Derived', {}):
            return (not any(self.held(flags, f) for f in self.story.get('DerivedForbids', {}).get(key, []))
                    and any(all(self.held(flags, f) for f in g) for g in self.story['Derived'][key]))
        return key in flags

    def visible(self, choice, flags):
        return (all(self.held(flags, f) for f in choice['Requires'])
                and not any(self.held(flags, f) for f in choice['Forbids']))

    def test_original_save_identities_and_exit_effects_survive(self):
        self.assertEqual([], savecompat.check(self.story, savecompat.inventory(self.before)))
        for old in self.before['Scenes']:
            if 'epilogue' not in old['Id']:
                continue
            for old_node in old['Nodes']:
                new = self.node(old['Id'], old_node['Id'])
                for i, answer in enumerate(old_node['Choices']):
                    for key in ('Set', 'Abort', 'Revive', 'RemoveItem', 'NativeNext', 'StartEtude'):
                        self.assertEqual(answer.get(key), new['Choices'][i].get(key), (old['Id'], key))

    def test_fast_blocks_all_four_contacts_and_keeps_noncontact_choices(self):
        t = polish.T
        witnesses = [('old_name', 'offer', 2, 0), ('the_dance', 'start', 1, 2),
                     ('abyss_dose', 'start', 2, 1), ('the_scar', 'mark', 1, 0)]
        for hour in (24, 167, 168):
            # Hour 168 permits the existing proposal, not retrospective hands.
            for suffix, nid, touch, ordinary in witnesses:
                with self.subTest(hour=hour, scene=suffix):
                    choices = self.node(t + suffix, nid)['Choices']
                    flags = {t + 'fast', t + 'touched', 'arueshalae.ward_held'}
                    self.assertFalse(self.visible(choices[touch], flags))
                    self.assertTrue(self.visible(choices[ordinary], flags))
                    flags.add(t + 'prescription')
                    self.assertTrue(self.visible(choices[touch], flags))
        proposal = self.scenes[t + 'prescription']
        self.assertEqual(168, proposal['DelayHours'])
        self.assertIn(t + 'relapse_two', proposal['Requires'])

    def test_fast_walk_rejects_intervening_hands_then_earns_proposal(self):
        t = polish.T
        flags = {'trickster.ever', t + 'intake', t + 'touched', 'arueshalae.ward_held'}
        times = {'trickster.ever': -1000, t + 'intake': -900, t + 'touched': -800}
        # Select the real fast answer, rather than injecting its receipt.
        fast = self.node(t + 'relapse_two', 'ask')['Choices'][0]
        for flag in fast['Set']:
            flags.add(flag)
            times[flag] = 0
        before = set(flags)
        for hour, suffix, nid, index in ((24, 'old_name', 'offer', 2),
                                         (48, 'the_dance', 'start', 1),
                                         (96, 'abyss_dose', 'start', 2),
                                         (167, 'the_scar', 'mark', 1)):
            choice = self.node(t + suffix, nid)['Choices'][index]
            self.assertFalse(self.visible(choice, flags), (hour, suffix))
            self.assertEqual(before, flags)  # rejected touch spends/sets nothing
        proposal = self.scenes[t + 'prescription']
        latest = max(times.get(k, -1000) for k in proposal['Requires'])
        self.assertLess(167 - latest, proposal['DelayHours'])
        self.assertEqual(168, 168 - latest)
        self.assertTrue(all(self.held(flags, k) for k in proposal['Requires']))
        self.assertFalse(any(self.held(flags, k) for k in proposal['Forbids']))
        for nid in ('start', 'fast', 'risk'):
            self.assertTrue(any(self.visible(a, flags) for a in self.node(t + 'prescription', nid)['Choices']))
        acceptance = self.node(t + 'prescription', 'ask')['Choices'][0]
        flags.update(acceptance['Set'])
        flags.add(t + 'prescription')  # normal non-abort scene completion
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
            self.assertEqual(1, len(answers))
            self.assertEqual([polish.T + 'morning'], answers[0]['Set'])
            self.assertNotIn('doctor', self.node(sid, 'start')['Text'].lower())
            self.assertNotIn('daybook', self.node(sid, 'start')['Text'].lower())

    def test_redeemed_titles_and_journal_drop_the_clinic_frame(self):
        suffixes = ('intake', 'mealtimes', 'relapse', 'touched', 'relapse_two',
                    'prescription', 'morning', 'discharged', 'the_cat',
                    'the_wound', 'the_dance', 'after_the_war', 'abyss_dose',
                    'bad_day', 'first_quarrel')
        clinic = r'(?i)\b(treatment|intake|case notes|relapse|procedure|contraindications|patient|discharged|field observations|doctor|recommended exercise|prognosis|dose|symptoms|second opinion|medical condition)\b'
        for suffix in suffixes:
            with self.subTest(scene=suffix):
                self.assertNotRegex(self.scenes[polish.T + suffix]['Title'], clinic)
        journal = arueshalae_trickster.RELATIONSHIP
        self.assertEqual('Any caress', journal['Title'])
        for field in ('Title', 'Description', 'Objective', 'Guidance'):
            with self.subTest(journal=field):
                self.assertNotRegex(journal[field], clinic)
        self.assertIn('Scroll of Death Ward', journal['Description'])

    def test_changed_chaplain_question_and_refusal_are_not_hunger(self):
        sid = polish.P + 'terms'
        choices = self.node(sid, 'chaplain')['Choices']
        self.assertEqual(['question_changed'], [a['Next'] for a in choices if self.visible(a, {polish.CHANGED})])
        changed = self.node(sid, 'question_changed')
        self.assertIn('The hunger is gone', changed['Text'])
        self.assertEqual('saint_e', next(a for a in changed['Choices'] if a['Next'] == 'saint_e')['Next'])
        self.assertIn('No.', self.node(sid, 'saint_e')['Text'])

    def test_slots_are_alternatives_and_default_cuts_reach_original_aftermath(self):
        briefs = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/arueshalae'
        expected = {'arueshalae.treatment.night.explicit.1': 'morning_after_paid',
                    'arueshalae.treatment.night.explicit.2': 'morning_after',
                    'arueshalae.trickster.fallen.roof.explicit.1': 'after',
                    'arueshalae.trickster.evil.window.explicit.1': 'after',
                    'arueshalae.trickster.evil.window_yard.explicit.1': 'after'}
        self.assertEqual(set(expected), {p.stem for p in briefs.glob('*.json')})
        for key, dest in expected.items():
            sid = key.rsplit('.explicit.', 1)[0]
            nd = self.node(sid, key)
            self.assertTrue(nd['Text'])
            self.assertEqual(dest, nd['Choices'][0]['Next'])
            self.assertEqual([], nd['Choices'][0]['Set'])
            brief = json.loads((briefs / (key + '.json')).read_text(encoding='utf-8'))
            self.assertEqual(['a man', 'a woman'], brief['commander_variants'])
        undress = self.node(polish.T + 'night', 'undress')
        for flags in (set(), {polish.CHANGED}):
            self.assertEqual(1, sum(self.visible(a, flags) for a in undress['Choices']))

    def test_history_callbacks_require_all_producers(self):
        t = polish.T
        list_answer = self.node(t + 'the_eve', 'fear')['Choices'][1]
        for missing in ('rx_want', 'mealtimes', 'kitchen', 'relapse'):
            flags = {t + x for x in ('rx_want', 'mealtimes', 'kitchen', 'relapse') if x != missing}
            self.assertFalse(self.visible(list_answer, flags))
        self.assertIn(t + 'intake', self.scenes[t + 'react.sosiel_morning']['Requires'])
        self.assertIn(t + 'night.warded', self.scenes[t + 'react.sosiel_morning']['Requires'])
        self.assertNotIn('seventh out loud', self.node(t + 'prescription', 'no_fast')['Text'])
        self.assertNotIn('night this week', self.node(t + 'prescription', 'her_call')['Text'])

    def test_contact_locations_and_cat_earliest_history(self):
        for sid in (polish.T + 'the_cat', polish.T + 'the_novice', polish.T + 'rainy_day', polish.P + 'chaplain.prayer'):
            self.assertEqual([polish.DREZEN], self.scenes[sid]['Areas'])
        cat = self.scenes[polish.T + 'the_cat']
        self.assertEqual(24, cat['DelayHours'])
        for nd in cat['Nodes']:
            self.assertNotIn('weeks', nd['Text'])
            self.assertNotIn('bled', nd['Text'])
            self.assertNotIn('scratch', nd['Text'])
        self.assertNotIn('home a week', self.node(polish.T + 'abyss_dose', 'start')['Text'])


if __name__ == '__main__':
    unittest.main()
