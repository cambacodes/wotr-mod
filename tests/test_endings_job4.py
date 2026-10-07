"""Rendered chronology and original counterexamples for endings job 4."""
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as V
from tools.savecompat import check


class EndingsJob4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = V.Model(cls.story)
        cls.scenes = cls.model.by_id

    def shown(self, page, flags):
        state = V.SimState(6, 20000)
        state.flags = set(flags)
        V.sim_complete(self.model, state)
        return '\n'.join([page['Text'], *[block['Text'] for block in page.get('Paragraphs', [])
            if all(f in state.flags for f in block.get('Requires', []))
            and not any(f in state.flags for f in block.get('Forbids', []))
            and all(any(f in state.flags for f in group) for group in block.get('AnyGroups', []))]])

    def node(self, sid, nid):
        return self.model.nodes[sid][nid]

    def test_eliandra_decision_precedes_night_lifetime_and_coda(self):
        for suffix in ('late', 'unasked'):
            sid = 'eliandra.trickster.epilogue.' + suffix
            flags = {'trickster.ever', 'eliandra.trickster.drezen.sea',
                     'eliandra.trickster.cost.tried_to_cheat', 'eliandra.trickster.lied_about_hand',
                     'trickster.lastcall.taken', 'ending.trickster'}
            opening = self.shown(self.node(sid, 'page'), flags)
            self.assertNotIn('second summer', opening)
            self.assertNotIn('Commander said either', opening)
            self.assertLess(opening.index('lie'), opening.index('Drezen, or the road?'))
            for branch in ('late_accepted', 'late_refused', 'late_friend'):
                text = self.shown(self.node(sid, branch), flags)
                self.assertIn('second summer', text)
                if branch == 'late_accepted':
                    self.assertLess(text.index('In the morning' if suffix == 'late' else 'at dawn'), text.index('second summer'))
                else:
                    self.assertNotIn('asleep against the Commander', text)
                blocks = self.node(sid, branch)['Paragraphs']
                self.assertIn('lastcall.active', blocks[-1]['Requires'])

    def test_camellia_immediate_curtain_is_not_three_nights_in_coffin(self):
        page = self.node('camellia.lastcall.page', 'page')
        late = self.shown(page, {'trickster.ever', 'camellia.trickster.cost.bargain_late'})
        third = self.shown(page, {'trickster.ever', 'camellia.trickster.cost.late'})
        self.assertIn('before she died', late)
        self.assertNotIn('three days alone', late)
        self.assertIn('three days alone', third)
        self.assertNotIn('before she died', third)

    def test_lastcall_recollections_do_not_invent_bodies_or_reverse_choices(self):
        cases = [('areelu', 'cost.wound_ceded', 'Commander ceded the wound', 'I ceded the Wound'),
                 ('hepzamirah', 'cost.healed_against_terms', 'smooth, healed patch', 'healed scar'),
                 ('arueshalae', 'cost.chaplain', 'chosen the company', 'given her the chance'),
                 ('targona', 'cost.unforgiven', 'at her ward', 'at her bier')]
        for route, receipt, expected, wrong in cases:
            text = self.shown(self.node(route + '.lastcall.page', 'page'),
                              {'trickster.ever', route + '.trickster.' + receipt})
            self.assertIn(expected, text)
            self.assertNotIn(wrong, text)
        self.assertNotIn('wrist that has none', self.node('areelu.lastcall.call', 'call')['Text'])
        self.assertNotIn('every morning', self.node('eliandra.lastcall.call', 'daily')['Text'])

    def test_repeated_pair_summaries_only_follow_selected_terminal(self):
        event = self.scenes['minagho_chivarro.trickster.epilogue.commit']
        flags = {'trickster.ever', 'minagho_chivarro.partner_stance.share'}
        for page in event['Nodes']:
            if any(answer.get('Next') for answer in page['Choices']):
                self.assertNotIn('had accepted the offered terms', self.shown(page, flags))
        self.assertIn('had accepted the offered terms', self.shown(self.node(event['Id'], 'went'), flags))
        for number in (1, 2, 3, 5):
            text = self.node(event['Id'], event['Id'] + '.explicit.' + str(number))['Text']
            self.assertLessEqual(text.count('opens her gown'), 1)
            self.assertLessEqual(text.count('gown falls'), 1)
            self.assertLessEqual(text.count('opens the door'), 1)
            self.assertNotIn('drops the sword belt', text)

    def test_jerribeth_selected_paths_print_each_partner_summary_once(self):
        from storylines import jerribeth_partner as J
        event = self.scenes['jerribeth.trickster.epilogue.commit']
        graph = self.model.nodes[event['Id']]
        summaries = {block['Text'] for block in J.partner_paragraphs()}
        for fate in (set(), {J.DEAD}, {J.CHIEF}, {J.PLANT}, {J.PLANT, J.RETURNED}):
            state = V.SimState(6, 20000)
            state.flags = {'chapter_later', 'trickster.ever', 'trickster.now',
                           'trickster.lastcall.taken', 'ending.trickster',
                           'jerribeth.shared_work', 'jerribeth.commission', *fate}
            V.sim_complete(self.model, state)
            def visible(record):
                return (all(f in state.flags for f in record.get('Requires', []))
                        and not any(f in state.flags for f in record.get('Forbids', []))
                        and all(any(f in state.flags for f in g) for g in record.get('AnyGroups', [])))
            pending, seen = [('offer', frozenset())], set()
            while pending:
                nid, printed = pending.pop()
                if (nid, printed) in seen:
                    continue
                seen.add((nid, printed))
                page = graph[nid]
                here = [b['Text'] for b in page.get('Paragraphs', [])
                        if b['Text'] in summaries and visible(b)]
                self.assertEqual(len(here), len(set(here)), (fate, nid))
                self.assertFalse(printed.intersection(here), (fate, nid))
                printed = printed.union(here)
                answers = [a for a in page['Choices'] if visible(a)]
                self.assertTrue(answers, (fate, nid))
                for answer in answers:
                    if answer.get('Next'):
                        pending.append((answer['Next'], printed))

    def test_codas_follow_all_route_variants_in_real_insertion_order(self):
        replacements = {v['Replacement'] for s in self.story['NativeEpilogueEdits'].values()
                        for v in (s, *s.get('Variants', [])) if v.get('Replacement')}
        pending = [e for e in self.story['Scenes'] if e['Owner'].endswith('Epilogue')
                   and e['Id'] not in replacements]
        placed, order, anchored = set(), [], set()
        while pending:
            event = next(e for e in pending if not (e.get('EpilogueAfter') or '').startswith('scene:')
                         or e['EpilogueAfter'][6:] in placed)
            pending.remove(event)
            placed.add(event['Id'])
            if event.get('EpilogueSequence') is not None or event['Owner'] == 'AeonEpilogue':
                continue
            target = (event.get('EpilogueAfter') or '')[6:]
            if target in order:
                at = order.index(target) + 1
                while at < len(order) and order[at] in anchored:
                    at += 1
                order.insert(at, event['Id'])
                anchored.add(event['Id'])
            else:
                order.append(event['Id'])
        self.assertEqual(order[-1], 'trickster.lastcall.page.last_word')
        from storylines.lastcall_partners import PARTNERS
        for part in PARTNERS:
            coda = part['key'] + '.lastcall.page'
            for sid in order:
                if self.scenes[sid].get('Relationship') == part['rel']:
                    self.assertLess(order.index(sid), order.index(coda), (sid, coda))

    def test_saved_ids_and_exits_survive(self):
        self.assertEqual(check(self.story), [])


if __name__ == '__main__':
    unittest.main()
