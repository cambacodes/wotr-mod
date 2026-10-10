"""Played-history regressions for the route's audited local residue."""
from copy import deepcopy
import unittest
from storylines import devarra_trickster as spine, devarra_tower as tower
from tests.test_devarra_round2 import visible
from storylines.endings_job3 import offer
from storylines.devarra_round3 import accepted_ending

class DevarraRoundFourTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        payload = {'Scenes': deepcopy(spine.SCENES + tower.SCENES)}
        tower.integrate(payload)
        cls.scenes = {s['Id']: s for s in payload['Scenes']}
        event = cls.scenes['devarra.trickster.epilogue.commit']
        offer(event, 'opening', ('accept', 'accepted'), ('refuse', 'refused'))
        accepted_ending(event)

    def node(self, scene, node):
        return next((n for n in self.scenes[scene]['Nodes'] if n['Id'] == node))

    def test_late_collection_uses_played_first_bite(self):
        page = self.node('devarra.trickster.epilogue.commit', 'page')
        for first in (False, True):
            flags = {'devarra.trickster.late_accepted'} | ({'devarra.tower.first_bite'} if first else set())
            selected = [p for p in page['Paragraphs'] if visible(p, flags)]
            self.assertEqual([['devarra.tower.first_bite']] if first else [[]], [p['Requires'] for p in selected])
            self.assertEqual([[]] if first else [['devarra.tower.first_bite']], [p['Forbids'] for p in selected])
            choices = [c for c in page['Choices'] if visible(c, flags)]
            self.assertEqual([(None, []), ('late_accepted', [])], [(c['Next'], c['Set']) for c in choices])

    def test_last_call_does_not_negotiate_a_price(self):
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        withheld = 'devarra.trickster.cost.egg_withheld'
        called_flag = 'devarra.lastcall.called'
        accounts = [p for p in page['Paragraphs'] if withheld in p.get('Requires', ()) and (called_flag in p.get('Requires', ()) or called_flag in p.get('Forbids', ()))]
        for called in (False, True):
            flags = {withheld} | ({called_flag} if called else set())
            self.assertEqual([[withheld, called_flag]] if called else [[withheld]], [p['Requires'] for p in accounts if visible(p, flags)])
            self.assertTrue(all((not c.get('Crusade') and (not c.get('Set')) for c in page['Choices'])))

    def test_intimacy_both_histories_leave_the_brush_fire(self):
        for flown in (False, True):
            flags = {'devarra.trickster.flown'} if flown else set()
            choices = self.node('devarra.tower.first_bite', 'ridge')['Choices']
            entry = next((c['Next'] for c in choices if visible(c, flags)))
            self.assertEqual(entry, 'inside_free' if flown else 'inside')
            bite = self.node('devarra.tower.first_bite', 'bite_free' if flown else 'bite')
            self.assertEqual(bite['Id'], 'bite_free' if flown else 'bite')
            ordered_answer_1, *ordered_answer_1_rest = bite['Choices']
            self.assertEqual(ordered_answer_1['Next'], 'devarra.tower.first_bite.explicit.1')

    def test_deliberate_destruction_has_separate_confrontations(self):
        for cause, target in [('manually_smashed', 'marked.responsible.1'), ('commanded_destruction', 'marked.responsible.2')]:
            flags = {'eggs.destroyed', 'native.history.eggs.' + cause}
            choices = self.node('devarra.trickster.flight.eggs', 'clutch')['Choices']
            selected = [c for c in choices if visible(c, flags) and c['Next'].startswith('marked.responsible.')]
            self.assertEqual([target], [c['Next'] for c in selected])
            self.assertTrue(all((spine.MARKED in c['Set'] for c in selected)))

    def test_military_offers_do_not_supply_a_battle_receipt(self):
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        accounts = [p for p in page['Paragraphs'] if 'devarra.tower.one_battle_sold' in p.get('Requires', ())]
        self.assertTrue(accounts)
        for mode in ('battle_offered', 'battle_price_accepted'):
            flags = {'devarra.tower.' + mode, 'devarra.tower.one_battle_sold'}
            self.assertEqual(mode == 'battle_price_accepted', any((visible(p, flags) for p in accounts)))
            self.assertTrue(all((not c.get('Set') and (not c.get('Crusade')) for c in page['Choices'])))

    def test_hunt_participation_precedes_the_outcome(self):
        *answer_in_order_1_preceding, answer_in_order_1 = self.node('devarra.tower.the_hunt', 'wait')['Choices']
        action = answer_in_order_1
        self.assertEqual(action['Check']['Skill'], 'SkillStealth')
        for result in ('Success', 'Failure'):
            target = self.node('devarra.tower.the_hunt', action['Check'][result])
            self.assertTrue(target['Choices'])
        shared = self.node('devarra.tower.the_hunt', 'shared_kill')
        self.assertEqual([c['Next'] for c in shared['Choices']], ['bite', 'gesture'])
        ordered_answer_2, *ordered_answer_2_rest = self.node('devarra.tower.the_hunt', 'rescued')['Choices']
        self.assertEqual(ordered_answer_2['Next'], 'finish_spotted')

    def test_reprisal_intervention_leaves_a_distinct_history(self):
        *answer_in_order_2_preceding, answer_in_order_2 = self.node('devarra.tower.the_clutch', 'nest')['Choices']
        action = answer_in_order_2
        self.assertEqual(action['Next'], 'intervene_nest')
        self.assertEqual(action['Set'], ['devarra.tower.nest_intervened'])
        judgment = self.node('devarra.tower.the_clutch', 'intervention_judged')
        self.assertEqual(judgment['Id'], 'intervention_judged')
        ordered_answer_3, *ordered_answer_3_rest = judgment['Choices']
        self.assertEqual(ordered_answer_3['Next'], 'end')
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        accounts = [p for p in page['Paragraphs'] if 'devarra.tower.nest_intervened' in p.get('Requires', ())]
        self.assertEqual([True], [visible(p, set(action['Set'])) for p in accounts])
