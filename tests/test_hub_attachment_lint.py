import copy
import unittest
from expansion import make_expansion
from tools import hub_attachment_lint as lint


class HubAttachments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = make_expansion()

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
