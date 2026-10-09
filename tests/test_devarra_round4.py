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
        return next(n for n in self.scenes[scene]['Nodes'] if n['Id'] == node)

    def test_late_collection_uses_played_first_bite(self):
        page = self.node('devarra.trickster.epilogue.commit', 'page')
        for first in (False, True):
            flags = {'devarra.trickster.late_accepted'}
            if first:
                flags.add('devarra.tower.first_bite')
            text = page['Text'] + ''.join(p['Text'] for p in page['Paragraphs'] if visible(p, flags))
            self.assertEqual('first small bite' in text, not first)
            self.assertEqual('another small annual bite' in text, first)
            choices = [c for c in page['Choices'] if visible(c, flags)]
            self.assertEqual([c['Next'] for c in choices if c['Text'] == 'Continue'], ['late_accepted'])
            self.assertEqual(choices[0]['Text'], 'End the account.')
            self.assertIsNone(choices[0]['Next'])
            self.assertEqual(choices[0]['Set'], [])

    def test_last_call_does_not_negotiate_a_price(self):
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        for called in (False, True):
            flags = {'devarra.trickster.cost.egg_withheld'}
            if called:
                flags.add('devarra.lastcall.called')
            paragraphs = [p['Text'] for p in page['Paragraphs'] if visible(p, flags)]
            self.assertEqual(sum('never named what she would take' in p for p in paragraphs), 1)
            self.assertNotIn('a month in every year', ''.join(paragraphs))

    def test_intimacy_both_histories_leave_the_brush_fire(self):
        for flown in (False, True):
            flags = {'devarra.trickster.flown'} if flown else set()
            choices = self.node('devarra.tower.first_bite', 'ridge')['Choices']
            entry = next(c['Next'] for c in choices if visible(c, flags))
            self.assertIn('unlit side', self.node('devarra.tower.first_bite', entry)['Text'])
            bite = self.node('devarra.tower.first_bite', 'bite_free' if flown else 'bite')
            self.assertIn('cool stone', bite['Text'])
            self.assertIn('bind it', bite['Text'])
            self.assertEqual(bite['Choices'][0]['Next'], 'devarra.tower.first_bite.explicit.1')

    def test_deliberate_destruction_has_separate_confrontations(self):
        for cause, words in [('manually_smashed', 'Your hand broke them'),
                             ('commanded_destruction', 'You ordered their deaths')]:
            flags = {'eggs.destroyed', 'native.history.eggs.' + cause}
            choices = self.node('devarra.trickster.flight.eggs', 'clutch')['Choices']
            confession = next(c for c in choices if visible(c, flags) and c['Next'].startswith('marked.responsible.'))
            self.assertIn(words, self.node('devarra.trickster.flight.eggs', confession['Next'])['Text'])

    def test_military_offers_do_not_supply_a_battle_receipt(self):
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        for mode in ('battle_offered', 'battle_price_accepted'):
            flags = {'devarra.tower.' + mode, 'devarra.tower.one_battle_sold'}
            text = ''.join(p['Text'] for p in page['Paragraphs'] if visible(p, flags))
            self.assertNotIn('broke a demon host', text)
            self.assertTrue('unfulfilled' in text or 'No such account' in text)

    def test_hunt_participation_precedes_the_outcome(self):
        action = self.node('devarra.tower.the_hunt', 'wait')['Choices'][-1]
        self.assertEqual(action['Check']['Skill'], 'SkillStealth')
        for result in ('Success', 'Failure'):
            target = self.node('devarra.tower.the_hunt', action['Check'][result])
            self.assertTrue(target['Choices'])
        shared = self.node('devarra.tower.the_hunt', 'shared_kill')
        self.assertEqual([c['Next'] for c in shared['Choices']], ['bite', 'gesture'])
        self.assertEqual(self.node('devarra.tower.the_hunt', 'rescued')['Choices'][0]['Next'],
                         'finish_spotted')

    def test_reprisal_intervention_leaves_a_distinct_history(self):
        action = self.node('devarra.tower.the_clutch', 'nest')['Choices'][-1]
        self.assertEqual(action['Next'], 'intervene_nest')
        self.assertEqual(action['Set'], ['devarra.tower.nest_intervened'])
        judgment = self.node('devarra.tower.the_clutch', 'intervention_judged')
        self.assertIn('Now you move', judgment['Text'])
        self.assertEqual(judgment['Choices'][0]['Next'], 'end')
        page = self.node('devarra.trickster.epilogue.woken', 'page')
        rendered = ''.join(p['Text'] for p in page['Paragraphs'] if visible(p, set(action['Set'])))
        self.assertIn('Two vrocks escaped', rendered)
