import copy
from tests.story_fixture import fresh_story
import unittest
from expansion import make_expansion
from tools import hub_attachment_lint as lint


class HubAttachments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()

    def test_reviewed_attachments(self):
        self.assertEqual(lint.lint(self.story), [])

    def test_missing_duplicate_unreviewed_and_unearned_attachments_fail(self):
        for mutation in ('missing', 'duplicate', 'unknown', 'gate', 'native'):
            with self.subTest(mutation=mutation):
                story = copy.deepcopy(self.story)
                p = story['Presences'][lint.HUBS[0]]
                if mutation == 'missing': p['ReactionScenes'].pop()
                if mutation == 'duplicate': p['ReactionScenes'].append(lint.REACTIONS[0])
                if mutation == 'unknown': p['ReactionScenes'][0] = 'unknown'
                if mutation == 'gate': p['Requires'].remove('nenio.trickster.visitor')
                if mutation == 'native':
                    next(s for s in story['Scenes'] if s['Id'] == lint.REACTIONS[0])['AnswerLists'] = []
                self.assertTrue(lint.lint(story))

    # eng7-f3
    def test_ch6_window_is_only_the_earned_shadow_reaction(self):
        presence = self.story['Presences'][lint.CH6_HUB]
        self.assertEqual(presence['ReactionScenes'], [lint.REACTIONS[0]])
        self.assertEqual((presence['MinChapter'], presence['MaxChapter']), (6, 6))
        for key in lint.HUBS:
            self.assertEqual(self.story['Presences'][key]['MaxChapter'], 5)
        for mutation in ('return', 'shadow', 'secret', 'area', 'window', 'dissolved', 'completed', 'extra', 'anchor'):
            with self.subTest(mutation=mutation):
                story = copy.deepcopy(self.story)
                p = story['Presences'][lint.CH6_HUB]
                if mutation == 'return': p['Requires'].remove('nenio.trickster.returned')
                if mutation == 'shadow': p['Requires'].remove('noct.defeated_not_dead')
                if mutation == 'secret': p['Requires'].remove('nocticula.trickster.cost.shade_secret')
                if mutation == 'area': p['Area'] = story['Presences'][lint.HUBS[0]]['Area']
                if mutation == 'window': p['MinChapter'] = 5
                if mutation == 'dissolved': p['Forbids'].remove('nenio.dissolved')
                if mutation == 'completed': p['Forbids'].remove(lint.REACTIONS[0])
                if mutation == 'extra': p['ReactionScenes'].append(lint.REACTIONS[1])
                if mutation == 'anchor': p['At']['NearUnit'] = p['Unit']
                self.assertTrue(lint.lint(story))
    # end eng7-f3
