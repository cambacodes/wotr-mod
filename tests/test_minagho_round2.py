"""Earned situation receipts and transparent heated-cut slots."""
from tests.story_fixture import fresh_story

import json
from pathlib import Path
import unittest
from storylines import minagho_round2 as route
from tools import rrt_verify
ROOT = Path(__file__).resolve().parents[1]

class MinaghoRound2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.pages = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = rrt_verify.Model(cls.story)

    def state(self, *flags):
        state = rrt_verify.SimState(5, 5000)
        state.flags.update(("chapter_later", "trickster", "trickster.ever", *flags))
        rrt_verify.sim_complete(self.model, state)
        return state

    def test_killer_cannot_buy_affection_with_scar_or_transfer(self):
        base = ("chivarro.dead", "chivarro.exile_objective_done", route.P + "minagho_in",
                route.P + "cost.palm_scar", route.P + "cost.scar_burned")
        self.assertNotIn(route.RECEIPT, self.state(*base).flags)
        self.assertIn(route.RECEIPT, self.state(*base, route.RINGS).flags)
        self.assertIn(route.RECEIPT, self.state(*base, route.P + "chivarro_deposit").flags)
        for page in self.pages.values():
            if page["Id"].startswith(route.P + "alone.minagho"):
                for node in page["Nodes"]:
                    for answer in node["Choices"]:
                        if "minachiv.complete" in answer["Set"]:
                            self.assertIn(route.RECEIPT, answer["Requires"], (page["Id"], node["Id"]))

    def test_rings_receipt_is_produced_only_after_her_burial(self):
        expected = {route.P + part for part in ('alone.minagho', 'alone.minagho_spared', 'alone.minagho_letter', 'alone.minagho_when_it_scars')}
        self.assertEqual({s['Id'] for s in self.story['Scenes'] for n in s['Nodes'] for a in n['Choices'] if route.RINGS in a['Set']}, expected)
        for sid in expected:
            page = self.pages[sid]
            nodes = {n['Id']: n for n in page['Nodes']}
            self.assertTrue(any(route.RINGS in a['Set'] for a in nodes['rings_burial']['Choices']))
            self.assertFalse(any(route.RINGS in a['Set'] for n in page['Nodes'] if n['Id'] != 'rings_burial' for a in n['Choices']))
            offer = next(a for a in page['Nodes'][0]['Choices'] if a['Next'] == 'rings_demand')
            self.assertIn('chivarro.dead_confirmed', offer['Requires'])
            self.assertIn(route.P + 'chivarro_deposit', offer['Forbids'])
            pay, leave = nodes['rings_purchase']['Choices']
            self.assertNotIn(route.RINGS, pay['Set'])
            self.assertTrue(leave['Abort'])

    def test_departure_gets_both_answers_only_after_rejection(self):
        page = self.pages[route.P + 'reunion.wardrobe']
        nodes = {n['Id']: n for n in page['Nodes']}
        for nid in ('which', 'which_debt'):
            answer = next((a for a in nodes[nid]['Choices'] if route.P + 'chivarro_sent_back' in a['Set']))
            self.assertIn(route.P + 'chivarro_sent_back', answer['Set'])
            self.assertEqual(answer['Next'], 'departure_answer')

    def test_all_46_briefs_have_reachable_slots_and_no_new_effect(self):
        paths = sorted((ROOT / 'tools/route_packs/explicit_slots/minagho').glob('*.json'))
        self.assertFalse(list((ROOT / 'tools/route_packs/explicit_slots/chivarro').glob('*.json')))
        self.assertEqual({json.loads(p.read_text(encoding='utf-8'))['slot_id'] for p in paths}, {
            'minachiv.a_room_she_likes.explicit.1',
            'minachiv.after_the_last_lamp.explicit.1',
            'minachiv.before_the_last_road.explicit.1',
            'minachiv.before_the_last_road.explicit.2',
            'minachiv.before_the_last_road.explicit.3',
            'minachiv.before_the_last_road.explicit.4',
            'minachiv.before_the_last_road.explicit.5',
            'minachiv.before_the_last_road.explicit.6',
            'minachiv.before_the_last_road.explicit.7',
            'minachiv.the_unhired_evening.explicit.1',
            'minachiv.the_unhired_evening.explicit.2',
            'minachiv.the_unhired_evening.explicit.3',
            'minagho_chivarro.trickster.after.before_the_last_road.explicit.1',
            'minagho_chivarro.trickster.after.before_the_last_road.explicit.2',
            'minagho_chivarro.trickster.after.before_the_last_road.explicit.3',
            'minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1',
            'minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2',
            'minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3',
            'minagho_chivarro.trickster.after.when_it_scars.explicit.1',
            'minagho_chivarro.trickster.after.when_it_scars.explicit.2',
            'minagho_chivarro.trickster.after.when_it_scars.explicit.3',
            'minagho_chivarro.trickster.alone.chivarro.explicit.1',
            'minagho_chivarro.trickster.alone.chivarro.explicit.2',
            'minagho_chivarro.trickster.alone.chivarro.explicit.3',
            'minagho_chivarro.trickster.alone.chivarro.explicit.4',
            'minagho_chivarro.trickster.alone.chivarro_letter.explicit.1',
            'minagho_chivarro.trickster.alone.chivarro_letter.explicit.2',
            'minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1',
            'minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2',
            'minagho_chivarro.trickster.alone.minagho.explicit.1',
            'minagho_chivarro.trickster.alone.minagho.explicit.2',
            'minagho_chivarro.trickster.alone.minagho_letter.explicit.1',
            'minagho_chivarro.trickster.alone.minagho_letter.explicit.2',
            'minagho_chivarro.trickster.alone.minagho_letter.explicit.3',
            'minagho_chivarro.trickster.alone.minagho_letter.explicit.4',
            'minagho_chivarro.trickster.alone.minagho_letter.explicit.5',
            'minagho_chivarro.trickster.alone.minagho_spared.explicit.1',
            'minagho_chivarro.trickster.alone.minagho_spared.explicit.2',
            'minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1',
            'minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2',
            'minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.3',
            'minagho_chivarro.trickster.epilogue.commit.explicit.1',
            'minagho_chivarro.trickster.epilogue.commit.explicit.2',
            'minagho_chivarro.trickster.epilogue.commit.explicit.3',
            'minagho_chivarro.trickster.epilogue.commit.explicit.4',
            'minagho_chivarro.trickster.epilogue.commit.explicit.5',
        })
        for path in paths:
            brief = json.loads(path.read_text(encoding='utf-8'))
            page = self.pages[brief['source']['scene']]
            nodes = {n['Id']: n for n in page['Nodes']}
            slot = nodes[brief['slot_id']]
            self.assertTrue(any((a['Next'] == slot['Id'] for n in page['Nodes'] for a in n['Choices'])))
            self.assertTrue(all((not a['Set'] and (not a.get('Crusade')) for a in slot['Choices'])))

    def test_years_rent_refusal_refunds_and_letter_nights_pay_once(self):
        page = self.pages[route.P + 'alone.chivarro_when_it_scars']
        nodes = {n['Id']: n for n in page['Nodes']}
        ordered_answer_3, *_ = nodes['start']['Choices']
        debit = ordered_answer_3['Crusade']['Amount']
        _, ordered_answer_4, *_ = nodes['chv']['Choices']
        refund = ordered_answer_4['Crusade']['Amount']
        self.assertEqual(debit + refund, 0)
        page = self.pages[route.P + 'alone.chivarro_letter']
        for node in page['Nodes']:
            for answer in node['Choices']:
                if route.P + 'night.chivarro' in answer['Set']:
                    self.assertEqual(answer['Crusade'], dict(Resource='Finances', Amount=-100))

    def test_later_commitment_cannot_overwrite_trickster_arrangement(self):
        self.assertIn(route.P + "committed", self.pages["minachiv.before_the_last_road"]["Forbids"])
if __name__ == '__main__':
    unittest.main()
