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
            self.assertEqual(victory['Choices'][0]['Next'], 'beaten')
            defeat = self.node('unmet.knife', check['Failure'])
            terminal = defeat['Choices'][0]
            self.assertIsNone(terminal['Next'])
            self.assertEqual(set(terminal['Set']), {route.GUARD, route.CLOSED})
            flags = {'trickster.ever', 'trickster', 'iz.done', 'coronation.seen',
                     route.REFUSED, *terminal['Set']}
            for suffix in ('unmet.knife', 'late.at_night', 'guild.kept'):
                self.assertFalse(shown(self.scenes[route.H + suffix], flags))
            self.assertNotIn(route.PRIMED, flags)
            self.assertNotIn(route.EAR, flags)

    def test_price_disclosed_before_injury_with_existing_settlement_preserved(self):
        take = self.node('late.at_night', 'take')
        self.assertEqual(take['Choices'][0]['Next'], 'cut')
        self.assertIn('100 Favors', take['Choices'][0]['Text'])
        self.assertTrue(take['Choices'][1]['Abort'])
        paid = self.node('late.at_night', 'no_priest')['Choices'][0]
        self.assertEqual(paid['Crusade'], {'Resource': 'Favors', 'Amount': -100})
        self.assertIn('100 Favors', paid['Text'])
        self.assertIn('lords', take['Text'])
        self.assertIn('hundred', take['Text'])
        self.assertEqual(set(self.node('late.at_night', 'cut')['EnterSet']),
                         {route.EAR, route.LATE})
        for chapter_six in (False, True):
            flags = {route.EAR, route.LATE}
            if chapter_six:
                flags.add('chapter.six')
            resume = [a for a in self.node('late.at_night', 'start')['Choices'] if shown(a, flags)]
            self.assertEqual([a['Next'] for a in resume], ['no_priest'])
            endings = [a for a in self.node('late.at_night', 'no_priest')['Choices'] if shown(a, flags)]
            self.assertEqual(len(endings), 1)
            self.assertEqual(endings[0]['Crusade'], paid['Crusade'])
            self.assertIn(route.PRIMED, endings[0]['Set'])
            self.assertEqual(endings[0]['Next'], 'eng8.guild.arrival' if chapter_six else None)

    def test_family_killing_is_history_even_after_sister_return(self):
        text = self.node('beat.spit', 'hers')['Text']
        self.assertIn('killed my sister in Colyphyr', text)
        self.assertIn('I enjoyed hearing about it', text)
        self.assertNotIn('not killed', text)
        self.assertNotIn('gently', text)
        self.assertIn('smears it across his mouth', text)
        self.assertNotIn(route.HEPZ_BACK, self.node('beat.spit', 'hers').get('Forbids', []))

    def test_earned_guild_slide_claim_is_limited_to_her_chair(self):
        scene = self.scenes['horzalah.native.eng7_f6c.guild']
        text = ' '.join(n['Text'] for n in scene['Nodes'])
        self.assertIn('helped her keep her chair', text)
        self.assertNotIn("escaped her father's claim", text)
        self.assertIn('trickster.now', scene['Requires'])
        self.assertIn(route.PRIMED, scene['Requires'])
        self.assertIn(route.RETURNED, scene['Requires'])


if __name__ == '__main__':
    unittest.main()
