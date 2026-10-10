"""Round-four earned encounter and pre-injury spending on the assembled export."""
import unittest
from tests.story_fixture import fresh_story
from tests.test_horzalah_round2 import shown
from storylines import horzalah_trickster as route

class HorzalahRound4Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def node(self, suffix, nid):
        return next(n for n in self.scenes[route.H + suffix]['Nodes'] if n['Id'] == nid)

    def test_both_attack_answers_require_the_commanders_tactical_success(self):
        for answer in self.node('unmet.knife', 'demise')['Choices']:
            check = answer['Check']
            self.assertTrue(check['CommanderOnly'])
            self.assertIn(check['Skill'], ('SkillMobility', 'SkillAthletics'))
            self.assertIsNone(answer['Next'])
            victory = self.node('unmet.knife', check['Success'])
            ordered_answer_1, *_ = victory['Choices']
            self.assertEqual(ordered_answer_1['Next'], 'beaten')
            defeat = self.node('unmet.knife', check['Failure'])
            ordered_answer_2, *_ = defeat['Choices']
            terminal = ordered_answer_2
            self.assertIsNone(terminal['Next'])
            self.assertEqual(set(terminal['Set']), {route.GUARD, route.CLOSED, route.STARTED})
            flags = {'trickster.ever', 'trickster', 'iz.done', 'coronation.seen', route.REFUSED, *terminal['Set']}
            for suffix in ('unmet.knife', 'late.at_night', 'guild.kept'):
                self.assertFalse(shown(self.scenes[route.H + suffix], flags))
            self.assertNotIn(route.PRIMED, flags)
            self.assertNotIn(route.EAR, flags)

    def test_price_disclosed_before_injury_with_existing_settlement_preserved(self):
        take = self.node('late.at_night', 'take')
        ordered_answer_3, *_ = take['Choices']
        self.assertEqual(ordered_answer_3['Next'], 'cut')
        _, ordered_answer_4, *_ = take['Choices']
        self.assertTrue(ordered_answer_4['Abort'])
        ordered_answer_5, *_ = self.node('late.at_night', 'no_priest')['Choices']
        paid = ordered_answer_5
        self.assertEqual(paid['Crusade'], {'Resource': 'Favors', 'Amount': -100})
        self.assertEqual(set(self.node('late.at_night', 'cut')['EnterSet']), {route.EAR, route.LATE})
        for chapter_six in (False, True):
            flags = {route.EAR, route.LATE}
            if chapter_six:
                flags.add('chapter.six')
            resume = [a for a in self.node('late.at_night', 'start')['Choices'] if shown(a, flags)]
            self.assertEqual([a['Next'] for a in resume], ['no_priest'])
            endings = [a for a in self.node('late.at_night', 'no_priest')['Choices'] if shown(a, flags)]
            self.assertEqual([a['Crusade'] for a in endings], [paid['Crusade']])
            ordered_answer_6, *_ = endings
            self.assertEqual(ordered_answer_6['Crusade'], paid['Crusade'])
            ordered_answer_7, *_ = endings
            self.assertIn(route.PRIMED, ordered_answer_7['Set'])
            ordered_answer_8, *_ = endings
            self.assertEqual(ordered_answer_8['Next'], 'eng8.guild.arrival' if chapter_six else None)

    def test_family_killing_is_history_even_after_sister_return(self):
        self.assertNotIn(route.HEPZ_BACK, self.node('beat.spit', 'hers').get('Forbids', []))

    def test_earned_guild_slide_claim_is_limited_to_her_chair(self):
        scene = self.scenes['horzalah.native.eng7_f6c.guild']
        self.assertIn('trickster.now', scene['Requires'])
        self.assertIn(route.PRIMED, scene['Requires'])
        self.assertIn(route.RETURNED, scene['Requires'])
if __name__ == '__main__':
    unittest.main()
