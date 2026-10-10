"""Walk the audit's counterexamples using the assembled route predicates."""
import unittest
from pathlib import Path
import json

from tests.story_fixture import fresh_story
from storylines import soana_partner as P, soana_round2 as R, soana_round3 as Q



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class SoanaRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s['Id']: s for s in cls.story['Scenes']}

    def holds(self, key, flags, trail=()):
        if key == 'availability.observed':
            return True
        if key in trail:
            return False
        derived = self.story['Derived']
        if key not in derived:
            return key in flags
        if any(self.holds(x, flags, (*trail, key))
               for x in self.story.get('DerivedForbids', {}).get(key, ())):
            return False
        return any(all(self.holds(x, flags, (*trail, key)) for x in group)
                   for group in derived[key])

    def available(self, block, flags):
        return (all(self.holds(x, flags) for x in block.get('Requires', ()))
                and not any(self.holds(x, flags) for x in block.get('Forbids', ())))

    def walk(self, sid, flags, start='start'):
        event = self.scenes[sid]
        nodes = {n['Id']: n for n in event['Nodes']}
        def visit(key, state, trail):
            self.assertNotIn(key, trail)
            node = nodes[key]
            choices = [a for a in node['Choices'] if self.available(a, state)]
            self.assertTrue(choices, (sid, key, state))
            for a in choices:
                after = state | set(a['Set'])
                path = (*trail, key)
                if a['Next']:
                    yield from visit(a['Next'], after, path)
                else:
                    yield after, path
        return list(visit(start, set(flags), ()))

    def test_authentication_only_and_later_proposal_both_twins(self):
        for returned in ('', '.returned'):
            sid = 'soana.partner.reply' + returned
            outcomes = self.walk(sid, {P.PURSUED})
            self.assertTrue(any('family_friend' in path and Q.FRIEND in flags
                                and Q.DISCLOSED not in flags for flags, path in outcomes))
            for flags, path in outcomes:
                if 'share' in path:
                    self.assertIn('send_proposal', path)
                    self.assertIn(Q.DISCLOSED, flags)
            secret = self.walk(sid, {P.PURSUED, P.SECRET})
            self.assertTrue(all('share' not in path for _, path in secret))

    def test_proposal_at_home_does_not_claim_an_existing_bed(self):
        for returned in ('', '.returned'):
            sid = 'soana.partner.homecoming' + returned
            for flags, path in self.walk(sid, {P.PURSUED}):
                self.assertNotIn('share', path)
                if P.SHARE in flags:
                    self.assertIn('family_proposal', path)
                if Q.FRIEND in flags:
                    self.assertFalse(self.holds(Q.ARRANGEMENT, flags))
            for flags, path in self.walk(sid, {P.PURSUED, P.SHARE, Q.DISCLOSED}):
                self.assertIn('share', path)

    def test_burned_family_inquiry_never_invents_a_lover(self):
        for returned in ('', '.returned'):
            sid = 'soana.partner.returned_letter' + returned
            for flags, path in self.walk(sid, {P.BURIED}):
                self.assertIn('answer_family', path)
                self.assertNotIn('answer_share', path)
                self.assertIn(P.DISTANT, flags)
                self.assertIn(P.CONFIRMED, flags)
                self.assertIn(P.BROKEN, flags)

    def test_family_friendship_blocks_renewed_courtship(self):
        flags = {Q.FRIEND, P.CONFIRMED, P.TOGETHER}
        for after, path in self.walk('soana.name_between', flags, 'marriage'):
            self.assertNotIn('court', path)
            self.assertNotIn('round2_affair', path)
            self.assertNotIn('soana.courtship_chosen', after)
        self.assertFalse(self.holds(R.CURRENT, flags | {'soana.committed'}))
        for _, path in self.walk('soana.a_promise_still_spoken',
                                 flags | {'soana.courtship_chosen'}, 'history'):
            self.assertNotIn('court', path)

    def test_known_history_replaces_unknown_claims(self):
        cases = [('soana.name_between', 'court', 'The years cannot tell me'),
                 ('soana.when_the_road_returns', 'saved', 'no news of him'),
                 ('soana.the_days_she_counted', 'future', 'told me nothing')]
        for sid, key, obsolete in cases:
            event = self.scenes[sid]
            incoming = [a for node in event['Nodes'] for a in node['Choices']
                        if a['Next'] == key]
            self.assertTrue(incoming)
            self.assertTrue(all(Q.KNOWN in a['Forbids'] for a in incoming))
            known = next(n for n in event['Nodes'] if n['Id'] == key + '_r3_known')
            self.assertTrue(known['Choices'])
            self.assertTrue(any(a['Next'] == known['Id'] and Q.KNOWN in a['Requires']
                                for node in event['Nodes'] for a in node['Choices']))
        event = self.scenes['soana.the_days_she_counted']
        known = next(n for n in event['Nodes'] if n['Id'] == 'partner_share_commit_r3_answered')
        self.assertTrue(known['Choices'])
        self.assertTrue(any(a['Next'] == known['Id'] for node in event['Nodes'] for a in node['Choices']))

    def test_family_variants_play_their_answers_without_dead_ends(self):
        seen = set()
        cases = [
            ('soana.name_between', 'marriage', {'soana.courtship_chosen'}),
            ('soana.a_promise_still_spoken', 'delivered', {'soana.courtship_chosen', P.PURSUED}),
            ('soana.when_the_road_returns', 'welcome', {'soana.later_courting', 'soana.nursery_saved', 'soana.path_cleft'}),
            ('soana.the_days_she_counted', 'letter', {'soana.later_courting'}),
            ('soana.the_days_she_counted', 'guardian', {'soana.later_courting', 'soana.bear_dead'}),
        ]
        histories = [set(), {P.CONFIRMED, P.TOGETHER, P.SHARE, P.DECIDED},
                     {P.CONFIRMED, P.TOGETHER, P.SHARE, P.DECIDED, Q.HOME},
                     {P.CONFIRMED, P.SECRET, P.DECIDED, Q.HOME, P.QUIET_RETURN},
                     {P.CONFIRMED, P.SEPARATED, P.EXCLUSIVE, P.CHOSEN, P.DECIDED},
                     {Q.FAMILY, P.SECRET, P.DECIDED}]
        for sid, start, route in cases:
            for family in histories:
                for _, path in self.walk(sid, route | family | {'trickster'}, start):
                    seen.update((sid, key) for key in path)
        for sid in ('soana.name_between', 'soana.when_the_road_returns', 'soana.the_days_she_counted'):
            for node in self.scenes[sid]['Nodes']:
                if node['Id'].endswith(('_r3_known', '_r3_home', '_r3_separated')) and not node['Id'].startswith('quiet_'):
                    self.assertIn((sid, node['Id']), seen)

    def test_concealed_nights_keep_effects_and_leave_home_alone(self):
        names = ['soana.after_the_last_visitor', 'soana.before_the_far_road',
                 'soana.the_days_she_counted',
                 'soana.trickster.returned.terms', 'soana.trickster.returned.second_ask',
                 'soana.trickster.returned.rebind', 'soana.trickster.missed.bowl',
                 'soana.trickster.missed.second_ask']
        for sid in names:
            event = self.scenes[sid]
            start = by_contract(event['Nodes'], [{'Id': 'start'}])
            entry = next(a for a in start['Choices'] if a['Next'] == 'quiet_r3_start')
            self.assertTrue(all(P.QUIET_RETURN in a['Forbids'] for a in start['Choices']
                                if a is not entry and not a.get('Abort')))
            self.assertEqual(entry['Set'], [])
            self.assertIn(P.QUIET_RETURN, entry['Requires'])
            for node in event['Nodes']:
                if not node['Id'].startswith('quiet_r3_'):
                    continue
                original = next(n for n in event['Nodes'] if n['Id'] == node['Id'][9:])
                for a, b in zip(original['Choices'], node['Choices']):
                    self.assertEqual(a['Set'], b['Set'])
                    self.assertEqual(a.get('Crusade'), b.get('Crusade'))

    def test_reunion_and_negotiated_terms_are_mutually_exclusive(self):
        family = {P.TOGETHER, P.CONFIRMED, Q.FRIEND, Q.HOME}
        lovers = {P.TOGETHER, P.CONFIRMED, P.SHARE, Q.HOME}
        for event in self.scenes.values():
            if not event['Id'].startswith('soana.') or not event['Owner'].endswith('Epilogue'):
                continue
            for node in event['Nodes']:
                for block in node.get('Paragraphs', []):
                    if P.TOGETHER not in block['Requires']:
                        continue
                    if Q.ARRANGEMENT in block['Requires']:
                        self.assertFalse(self.available(block, family))
                    if Q.ARRANGEMENT in block['Forbids']:
                        self.assertFalse(self.available(block, lovers))

    def test_epilogue_briefs_use_past_narration(self):
        for path in Path('tools/route_packs/explicit_slots/soana').glob('*epilogue*.json'):
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['narration'], 'third-past')

    def test_pending_partner_answer_can_postpone_without_a_payoff(self):
        flags = {'trickster', 'soana.later_courting'}
        for sid, key in (('soana.after_the_last_visitor', 'private'),
                         ('soana.before_the_far_road', 'beloved'),
                         ('soana.before_the_far_road', 'courtship')):
            for after, _ in self.walk(sid, flags, key):
                self.assertEqual(after, flags)

    def test_first_secret_answer_keeps_invitation_and_price(self):
        flags = {'trickster', 'trickster.ever', P.RETURNED,
                 'soana.trickster.accounting_invited'}
        sid = 'soana.trickster.returned.terms'
        secret = self.walk(sid, flags, 'partner_secret_bind')
        accepted = [after for after, _ in secret if 'soana.committed' in after]
        self.assertTrue(accepted)
        self.assertTrue(all(P.SECRET in after and 'soana.trickster.cost.knot_bearer' in after
                            for after in accepted))
        for after, _ in self.walk(sid, flags, 'partner_share_bind'):
            self.assertNotIn('soana.committed', after)
        for after, _ in self.walk(sid, flags - {'soana.trickster.accounting_invited'},
                                  'partner_secret_bind'):
            self.assertNotIn('soana.committed', after)
        for after, _ in self.walk(sid, flags | {P.BROKEN}, 'partner_secret_bind'):
            self.assertNotIn('soana.committed', after)

    def test_second_proposal_waits_for_a_separate_relay_reply(self):
        for returned in ('', '.returned'):
            sid = 'soana.partner.reply' + returned
            outcomes = self.walk(sid, {P.PURSUED}, 'send_proposal')
            self.assertTrue(outcomes)
            for flags, path in outcomes:
                self.assertNotIn('share', path)
                self.assertIn(Q.PROPOSAL_SENT, flags)
                self.assertNotIn(P.CONFIRMED, flags)
            followup = self.scenes['soana.partner.proposal_reply' + returned]
            self.assertEqual(followup['DelayHours'], 168)
            self.assertIn(Q.PROPOSAL_SENT, followup['Requires'])
            self.assertNotIn(Q.PROPOSAL_SENT, self.story['Derived'])
            self.assertIn(Q.PROPOSAL_READ, followup['Forbids'])
            for flags, path in self.walk(followup['Id'], {Q.PROPOSAL_SENT, P.SHARE}):
                self.assertIn('share', path)
                self.assertIn(Q.PROPOSAL_READ, flags)
                self.assertIn(P.CONFIRMED, flags)

    def test_dead_guardian_selects_actual_husband_history(self):
        event = self.scenes['soana.the_days_she_counted']
        guardian = Q.page(event, 'guardian')
        for extra, target, wording in (
                (set(), 'dead', 'if he ever comes'),
                ({P.CONFIRMED}, 'dead_r3_known', 'alive in the south'),
                ({Q.HOME, P.CONFIRMED}, 'dead_r3_home', 'Corven is home'),
                ({Q.HOME, P.CONFIRMED, P.SEPARATED}, 'dead_r3_separated', 'ended our vows')):
            with self.subTest(target=target):
                choices = [a for a in guardian['Choices']
                           if a['Next'].startswith('dead') and self.available(a, extra | {'soana.bear_dead'})]
                self.assertEqual([a['Next'] for a in choices], [target])
                node = Q.page(event, target)
                self.assertTrue(node['Choices'])
                self.assertTrue(all(a['Next'] is None or a['Next'] in
                                    {n['Id'] for n in event['Nodes']} for a in node['Choices']))



    def test_speaker_repairs_add_no_strict_player_text_findings(self):
        from tools import player_text_lint, player_text_baseline
        route = {'Scenes': [s for s in self.story['Scenes'] if s['Id'].startswith('soana.')]}
        lint = player_text_lint.check(route)
        hard = player_text_baseline.new_findings(route, lint['review'],
                                               therapy_counts=lint['therapy_counts'])
        self.assertEqual(hard, [])


if __name__ == '__main__':
    unittest.main()
