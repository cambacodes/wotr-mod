"""Situation receipts and negative histories, independent of prose wording."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from storylines import soana_round2 as R, soana_partner as P
from storylines import soana_opening as O, soana_continuation as C
from storylines import soana_later_progression as L, soana_late_campaign as V


class SoanaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s['Id']: s for s in cls.story['Scenes']}

    def holds(self, key, flags, trail=()):
        if key == 'availability.observed':
            return True
        if key in flags:
            return True
        if key in trail:
            return False
        derived = self.story['Derived']
        if key not in derived:
            return False
        if any(self.holds(k, flags, (*trail, key))
               for k in self.story.get('DerivedForbids', {}).get(key, [])):
            return False
        return any(all(self.holds(k, flags, (*trail, key)) for k in group)
                   for group in derived[key])

    def test_return_is_current_and_not_a_renewed_welcome(self):
        ordinary = {'soana.committed', P.TOGETHER, P.CONFIRMED, 'trickster', R.R}
        self.assertTrue(self.holds(R.EFFECTIVE, ordinary))
        self.assertFalse(self.holds(R.CURRENT, ordinary))
        ordinary.add('soana.trickster.accounting_invited')
        self.assertTrue(self.holds(R.CURRENT, ordinary))
        for state in ('legend', 'dragon', 'swarm', 'trickster.failed'):
            self.assertFalse(self.holds(R.EFFECTIVE, ordinary | {state}))
            self.assertFalse(self.holds(R.CURRENT, ordinary | {state}))
        for state in R.FORBIDDEN:
            self.assertFalse(self.holds(R.CURRENT, ordinary | {state}))

    def test_luck_and_work_are_not_a_romantic_yes(self):
        ready = {'trickster', 'trickster.ever', 'soana.trickster.luck_kept',
                 'soana.trickster.luck_tested', P.TOGETHER, P.CONFIRMED}
        self.assertFalse(self.holds(R.CURRENT, ready))
        self.assertTrue(self.holds(R.CURRENT, ready | {R.LATE_YES}))
        self.assertFalse(self.holds(R.CURRENT, ready | {R.LATE_YES, 'soana.trickster.friends'}))
        living = {'trickster', 'soana.progression_kept', 'soana.later_courting', P.TOGETHER, P.CONFIRMED}
        self.assertTrue(self.holds(R.READY, living))
        self.assertFalse(self.holds(R.CURRENT, living))
        self.assertTrue(self.holds(R.CURRENT, living | {R.LATE_YES}))
        self.assertFalse(self.holds(R.READY, living | {'soana.later_friends'}))
        self.assertIn('soana.round2.no_current_love',
                      self.story['DerivedForbids']['soana.harem.eligible'])
        self.assertIn('soana.round2.no_current_love',
                      self.by['soana.lastcall.page']['Forbids'])

    def test_all_thirteen_slots_keep_a_cut_and_rejoin(self):
        briefs = Path('tools/route_packs/explicit_slots/soana')
        self.assertEqual(len(list(briefs.glob('*.json'))), 13)
        nodes = {n['Id']: (s, n) for s in self.story['Scenes'] for n in s['Nodes']}
        for brief in briefs.glob('*.json'):
            data = json.loads(brief.read_text(encoding='utf-8'))
            s, node = nodes[brief.stem]
            self.assertTrue(node['Text'].startswith('{n}'))
            self.assertEqual(node['Choices'][0]['Set'], [])
            self.assertIn(node['Choices'][0]['Next'], {n['Id'] for n in s['Nodes']})
            self.assertEqual(data['commander_variants'], ['a man', 'a woman'])

    def test_letters_do_not_create_an_arrival(self):
        for sid in ('soana.partner.dispatch', 'soana.partner.reply', 'soana.partner.reply.returned'):
            for node in self.by[sid]['Nodes']:
                for answer in node['Choices']:
                    self.assertNotIn('soana.round2.arrived', answer['Set'])
        arrival = self.by['soana.partner.homecoming']
        self.assertIn('soana.round2.correspondence_only', arrival['Forbids'])
        self.assertIn(P.PURSUED, arrival['Requires'])
        self.assertEqual(arrival['DelayHours'], 168)

    def test_full_living_chain_is_at_most_twenty_one_days(self):
        # Includes the opening, continuing courtship, working and Ch5 chain up
        # to commitment. Correspondence starts early and overlaps these waits.
        chain = O.SCENES + C.SCENES + L.SCENES
        late = V.SCENES[:next(i for i,s in enumerate(V.SCENES)
                            if s['Id'] == 'soana.the_days_she_counted') + 1]
        # Optional Act IV reaction has no place in the mandatory Ch5 chain.
        late = [s for s in late if s['Id'] != 'soana.past_the_firelight']
        self.assertLessEqual(sum(s['DelayHours'] for s in chain + late), 504)

    def test_saved_late_exits_do_not_accept_the_invitation(self):
        for kind in ('commit', 'luck_late'):
            event = self.by['soana.trickster.epilogue.' + kind]
            first = event['Nodes'][0]['Choices'][0]
            self.assertEqual(first.get('Id'), 'continue')
            self.assertNotIn(R.LATE_YES, first['Set'])
            self.assertTrue(any(R.LATE_YES in a['Set']
                                for n in event['Nodes'] for a in n['Choices']))


if __name__ == '__main__':
    unittest.main()
