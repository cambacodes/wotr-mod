"""Konomi's authored clocks, accounts, choices and slot continuations."""
import json
import os
import unittest
from functools import reduce
from pathlib import Path
from tools import rrt_verify as verify
from tools import savecompat

class KonomiRound2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        exported = os.environ.get("RRT_KONOMI_TEST_STORY")
        if exported:
            cls.story = json.loads(Path(exported).read_text(encoding="utf-8"))
        else:
            from expansion import make_expansion
            cls.story = make_expansion()
        cls.model = verify.Model(cls.story)
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}

    def node(self, sid, nid):
        return next(n for n in self.by["konomi." + sid]["Nodes"] if n["Id"] == nid)

    def available_at(self, sid, choice, hour, dispatched=100, reload=False):
        page = self.model.by_id["konomi." + sid]
        state = verify.SimState(5, hour)
        state.flags.update(page["Requires"])
        state.times.update({f: 0 for f in page["Requires"]})
        for flag in choice["Set"]:
            state.flags.add(flag)
            state.times[flag] = dispatched
        if reload:
            saved = json.loads(json.dumps({"chapter": state.chapter, "hour": state.hour,
                "flags": sorted(state.flags), "times": state.times}))
            state = verify.SimState(saved["chapter"], saved["hour"])
            state.flags.update(saved["flags"])
            state.times.update(saved["times"])
        return verify.sim_available(self.model, page, state)

    def test_road_wait_starts_at_payment_and_survives_reload(self):
        *_, ordered_answer_1 = self.node('trickster.dismissed.late', 'driver')['Choices']
        choice = ordered_answer_1
        self.assertNotIn('konomi.trickster.back_from_the_road', choice['Set'])
        self.assertIn('konomi.trickster.road_sent', choice['Set'])
        for age, expected in ((0, False), (47, False), (48, True)):
            for reload in (False, True):
                self.assertEqual(expected, self.available_at('trickster.dismissed.arrival', choice, 100 + age, reload=reload))

    def test_report_wait_and_letter_fallback_are_separate(self):
        *_, ordered_answer_2 = self.node('trickster.never_arrived.accredited', 'nerosyan')['Choices']
        choice = ordered_answer_2
        self.assertNotIn('konomi.trickster.arrived', choice['Set'])
        self.assertIn('konomi.trickster.report_sent', choice['Set'])
        for age, expected in ((0, False), (95, False), (96, True)):
            for reload in (False, True):
                self.assertEqual(expected, self.available_at('trickster.never_arrived.arrival', choice, 100 + age, reload=reload))
        fallback = self.by['konomi.trickster.never_arrived.audience_letter']
        self.assertEqual(96, fallback['DelayHours'])
        self.assertIn('konomi.trickster.never_arrived.audience', fallback['Forbids'])
        self.assertIn('konomi.trickster.returned', fallback['Forbids'])

    def test_same_account_with_or_without_early_credit(self):
        ordered_answer_3, *_ = self.node('trickster.never_arrived.rooms', 'start')['Choices']
        full = -ordered_answer_3['Crusade']['Amount']
        _, ordered_answer_4, *_ = self.node('trickster.never_arrived.audience', 'start')['Choices']
        early = -ordered_answer_4['Crusade']['Amount']
        _, _, _, ordered_answer_5, *_ = self.node('trickster.never_arrived.rooms', 'start')['Choices']
        remaining = -ordered_answer_5['Crusade']['Amount']
        ordered_answer_6, *_ = self.node('trickster.never_arrived.rooms', 'haggle')['Choices']
        negotiated = -ordered_answer_6['Crusade']['Amount']
        ordered_answer_7, *_ = self.node('trickster.never_arrived.rooms', 'haggle_rest')['Choices']
        negotiated_credit = -ordered_answer_7['Crusade']['Amount']
        self.assertEqual((250, 225), (full, negotiated))
        self.assertEqual(full, early + remaining)
        self.assertEqual(negotiated, early + negotiated_credit)

    def test_first_supper_earns_only_an_invitation(self):
        close = self.node('trickster.never_arrived.rooms', 'stay')['Choices']
        active = [x for x in close if 'trickster.ever' not in x['Forbids']]
        self.assertTrue(active)
        for answer in active:
            self.assertNotIn('konomi.trickster.rooms_kept', answer['Set'])
            self.assertNotIn('konomi.lovers', answer['Set'])
            self.assertNotEqual('accept', answer['Next'])
        second = self.by['konomi.trickster.never_arrived.second_supper']
        self.assertEqual(48, second['DelayHours'])
        answers = second['Nodes'][0]['Choices']
        self.assertEqual(['accept', 'business', None], [a['Next'] for a in answers])
        *_, ordered_answer_8 = answers
        self.assertTrue(ordered_answer_8['Abort'])
        ordered_answer_9, *_ = answers
        self.assertIn('konomi.trickster.rooms_kept', ordered_answer_9['Set'])


    def test_whole_chains_fit_their_phase_budgets(self):
        names = ['capital_letter', 'return_offer', 'private_reunion', 'lease_offer', 'chosen_evening', 'private_future_choice']
        self.assertEqual(408, reduce(lambda total, hours: total + hours, (self.by['konomi.' + sid]['DelayHours'] for sid in names), 0))
        names = ['trickster.dismissed.late', 'trickster.dismissed.arrival', 'trickster.dismissed.terms', 'trickster.dismissed.private']
        self.assertEqual(168, reduce(lambda total, hours: total + hours, (self.by['konomi.' + sid]['DelayHours'] for sid in names), 0))
        self.assertEqual(72, self.by['konomi.trickster.dismissed.a_season']['DelayHours'])

    def test_slot_defaults_and_destinations_have_matching_briefs(self):
        root = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/konomi'
        slots = []
        for s in self.story['Scenes']:
            if s.get('Relationship') != 'konomi':
                continue
            ids = {n['Id'] for n in s['Nodes']}
            for n in s['Nodes']:
                if '.explicit.' not in n['Id']:
                    continue
                slots.append(n['Id'])
                ordered_answer_10, *_ = n['Choices']
                self.assertIn(ordered_answer_10['Next'], ids)
                brief = json.loads((root / (n['Id'] + '.json')).read_text(encoding='utf-8'))
                self.assertEqual([variant.split() for variant in brief['commander_variants']],
                                 [['a', 'man'], ['a', 'woman']])
                self.assertEqual(brief['speakers']['K'], 'Konomi')
        self.assertEqual(set(slots), {'konomi.trickster.never_arrived.second_supper.explicit.1', 'konomi.the_evening_she_kept.explicit.1', 'konomi.chosen_evening.explicit.1', 'konomi.evening.explicit.1', 'konomi.trickster.dismissed.private.explicit.1', 'konomi.trickster.dismissed.a_season.explicit.1', 'konomi.trickster.never_arrived.rooms.explicit.1', 'konomi.private_last_visit.explicit.1'})

    def test_postwar_legacy_continue_keeps_identity_and_mechanics(self):
        page = self.by['konomi.trickster.epilogue.refused']
        start = self.node('trickster.epilogue.refused', 'start')
        ordered_answer_11, *_ = start['Choices']
        old = ordered_answer_11
        self.assertEqual('continue', old['Id'])
        self.assertFalse(any((old.get(k) for k in savecompat.EXIT_MECHANICS)))
        self.assertIn('konomi.closed', page['Forbids'])
        for node in page['Nodes']:
            self.assertTrue(all((not ch['Set'] for ch in node['Choices'])))
if __name__ == '__main__':
    unittest.main()
