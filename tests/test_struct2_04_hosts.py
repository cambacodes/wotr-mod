"""Gameplay entry and journal witnesses over the final assembled export."""
import unittest

from tests.story_fixture import fresh_story


class GameplayHostsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s['Id']: s for s in cls.story['Scenes']}

    def physical(self, sid):
        body = self.by[sid]
        self.assertFalse(body.get('Remote', False), sid)
        self.assertFalse(body.get('ManualOnly', False), sid)
        self.assertNotIn('Kind', body, sid)
        self.assertTrue(body.get('ContactUnit'), sid)
        self.assertTrue(body.get('Areas'), sid)
        self.assertTrue(body.get('InteractionHub') or body.get('AnswerLists'), sid)
        return body

    def test_cave_both_histories_and_retry_keep_physical_doors(self):
        for step in ('settle', 'retry'):
            sid = 'household.pair.soana_camellia.' + step
            returned = self.physical(sid)
            native = self.physical(sid + '.native')
            self.assertEqual(returned['InteractionHub'], 'soana.presence')
            presence = self.story['Presences']['soana.presence']
            self.assertTrue(set(presence['Requires']) <= set(returned['Requires']))
            self.assertTrue(set(presence['Forbids']) <= set(returned['Forbids']))
            self.assertEqual(native['AnswerLists'], ['2b1776f3e398685479ff6b16290b4cc2'])
            self.assertIn('soana.trickster.returned', returned['Requires'])
            self.assertIn('soana.trickster.returned', native['Forbids'])
            for body in (returned, native):
                self.assertEqual(body['Areas'], ['0a5654e7dc18f074d9356009d55eb51b'])
                self.assertEqual(body['AdditionalContactUnits'], ['397b090721c41044ea3220445300e1b8'])
                self.assertIn('camellia.present_now', body['Requires'])
                self.assertIn('soana.closed', body['Forbids'])
                self.assertIn(sid + '.seen', body['Forbids'])
            self.assertEqual([n['Id'] for n in returned['Nodes']], [n['Id'] for n in native['Nodes']])
            if step == 'settle':
                check = next(n for n in returned['Nodes'] if n['Id'] == 'answer.check')['Choices'][0]['Check']
                self.assertEqual((check['Skill'], check['DC'], check['Success'], check['Failure']),
                                 ('SkillLoreReligion', 20, 'withdrawn', 'botched'))
            else:
                self.assertEqual(returned['DelayHours'], 48)
                self.assertIn('household.pair.soana_camellia.settle.failed', returned['Requires'])

    def test_survivors_use_infirmary_and_both_current_bodies(self):
        body = self.physical('targona.trickster.react.ix_a.yaniel')
        self.assertEqual(body['InteractionHub'], 'targona.presence')
        presence = self.story['Presences']['targona.presence']
        self.assertTrue(set(presence['Requires']) <= set(body['Requires']))
        self.assertTrue(set(presence['Forbids']) <= set(body['Forbids']))
        self.assertFalse(body['Reaction'])
        self.assertIn('targona.trickster.in_drezen', body['Requires'])
        self.assertIn('yaniel.trickster.returned', body['Requires'])
        self.assertIn('yaniel.present_now', body['Requires'])
        self.assertIn('yaniel.trickster.left_free', body['Forbids'])
        self.assertEqual(body['AdditionalContactUnits'], ['d914111e83e44194db99ab91d8c04632'])

    def test_redeemed_dispatch_and_retry_use_companion_door(self):
        for step in ('settle', 'retry'):
            body = self.physical('household.pair.arueshalae_minagho.' + step + '.good')
            self.assertEqual(body['AnswerLists'], ['03ebad9587cbea0438d901a0f8df44f1'])
            self.assertEqual(body['AdditionalContactUnits'], ['565ccab37e2475742b043ec912a750fa'])
            self.assertIn('arueshalae.redeemed', body['Requires'])
            self.assertIn('arueshalae.corrupted', body['Forbids'])
            self.assertIn('minagho.present_now', body['Requires'])
            self.assertIn('minachiv.closed', body['Forbids'])
            if step == 'settle':
                check = body['Nodes'][0]['Choices'][0]['Check']
                self.assertEqual((check['Skill'], check['DC'], check['Success'], check['Failure']),
                                 ('SkillPerception', 20, 'draw', 'botched'))
            else:
                self.assertEqual(body['DelayHours'], 48)

    def test_docket_journal_opens_on_appointment_and_settles_on_completed_work(self):
        entry = next(e for e in self.story['Relationships']['irabeth']['JournalEntries']
                     if e['Id'] == 'irabeth.seized_wagon.docket')
        self.assertEqual(entry['OpenWhen'], [['irabeth.wagon_heard']])
        self.assertEqual(entry['SettledWhen'], [['irabeth.account_resolved']])
        followup = self.physical('irabeth.the_sealed_account')
        self.assertEqual(entry['Description'], '[Agree to return for the docket.]')
        self.assertIn('irabeth.wagon_heard', followup['Requires'])
        self.assertEqual(followup['DelayHours'], 48)
        for branch in ('sealed', 'open'):
            node = next(n for n in followup['Nodes'] if n['Id'] == branch)
            self.assertNotIn('irabeth.account_resolved', node['Choices'][0]['Set'])
        end = next(n for n in followup['Nodes'] if n['Id'] == 'private')
        self.assertIn('irabeth.account_resolved', end['Choices'][0]['Set'])

    def test_chadali_bundled_witnesses_in_both_eritrice_states(self):
        cases = {
            'wagers.the_recipe': {'start': [2]},
            'wagers.born_lucky': {'start': [1]},
            'wagers.a_lucky_charm': {'start': [0, 2]},
            'wagers.knucklebones': {'start': [0, 1], 'honest': [0], 'open_cheat': [0]},
            'fortunes.a_great_big_fair': {'souls': [0]},
            'fortunes.burnt_edges': {'open': [0, 1], 'secret': [0], 'start': [0],
                                     'eat': [0, 1], 'more': [0], 'bed': [0]},
            'sessions.what_you_said': {'question': [1]},
            'hours.our_new_friend': {'start': [0, 1], 'fast': [0], 'why': [0, 1], 'votes': [0]},
            'hours.the_seat_beside_her': {'start': [1]},
        }
        foreign = {'eritrice.present_now', 'crossroute.eritrice.available',
                   'crossroute.eritrice.unavailable', 'eritrice.closed'}
        blocks = []
        for beat, nodes in cases.items():
            body = self.by['chadali.' + beat]
            for nid, indices in nodes.items():
                node = next(n for n in body['Nodes'] if n['Id'] == nid)
                blocks.extend(node['Choices'][i] for i in indices)
        blocks.extend(self.by['chadali.' + beat] for beat in
                      ('fortunes.burnt_edges', 'hours.our_new_friend'))
        for block in blocks:
            required, forbidden = set(block.get('Requires', [])), set(block.get('Forbids', []))
            self.assertFalse(foreign & (required | forbidden))
            # Hold the earned predicates and vary only Eritrice's current state.
            for state in ({'eritrice.present_now', 'crossroute.eritrice.available'},
                          {'eritrice.closed', 'crossroute.eritrice.unavailable'}):
                flags = required | state
                self.assertTrue(required <= flags and not forbidden & flags)
        breakfast = self.by['chadali.fortunes.burnt_edges']
        opening = next(n for n in breakfast['Nodes'] if n['Id'] == 'open')
        self.assertIn('chadali.wagers.guessed_the_spice', opening['Choices'][0]['Requires'])
        participant = self.by['chadali.trickster.react.eritrice_coin']
        self.assertIn('crossroute.eritrice.unavailable', participant['Forbids'])
        self.assertIn('eritrice.lost_at_council', participant['Forbids'])
