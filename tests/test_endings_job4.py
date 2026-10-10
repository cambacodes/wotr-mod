"""Rendered chronology and original counterexamples for endings job 4."""
import unittest
from unittest.mock import patch

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
            opening = self.node(sid, 'page')
            self.assertEqual([c['Next'] for c in opening['Choices']], [None, 'late_accepted', 'late_refused', 'late_friend'])
            self.assertFalse(any('lastcall.active' in p['Requires'] for p in opening['Paragraphs']))
            for branch in ('late_accepted', 'late_refused', 'late_friend'):
                page = self.node(sid, branch)
                self.assertTrue(any('lastcall.active' in p['Requires'] for p in page['Paragraphs']))
                slots = {p['Id'] for p in page['Paragraphs'] if p.get('Id', '').find('.explicit.') >= 0}
                self.assertEqual(bool(slots), branch == 'late_accepted')
                self.assertEqual([c['Next'] for c in page['Choices']], ['page_exit'])
                self.assertTrue(all(not c['Set'] for c in page['Choices']))

    def test_camellia_immediate_curtain_is_not_three_nights_in_coffin(self):
        page = self.node('camellia.lastcall.page', 'page')
        for suffix in ('bargain_late', 'late'):
            receipt = 'camellia.trickster.cost.' + suffix
            readers = [p for p in page['Paragraphs'] if receipt in p['Requires']]
            self.assertTrue(readers, receipt)
            for p in readers:
                self.assertNotIn('camellia.trickster.cost.' + ('late' if suffix == 'bargain_late' else 'bargain_late'), p['Requires'])

    def test_lastcall_recollections_do_not_invent_bodies_or_reverse_choices(self):
        for route, suffix in (('areelu', 'cost.wound_ceded'), ('hepzamirah', 'cost.healed_against_terms'),
                              ('arueshalae', 'cost.chaplain'), ('targona', 'cost.unforgiven')):
            receipt = route + '.trickster.' + suffix
            readers = [p for p in self.node(route + '.lastcall.page', 'page')['Paragraphs'] if receipt in p['Requires']]
            self.assertTrue(readers, receipt)
            self.assertTrue(all(not p.get('Set') for p in readers))
            self.assertTrue(all(route + '.present_now' not in p['Requires'] for p in readers))

    def test_repeated_pair_summaries_only_follow_selected_terminal(self):
        event = self.scenes['minagho_chivarro.trickster.epilogue.commit']
        share = 'minagho_chivarro.partner_stance.share'
        state = V.SimState(6, 20000)
        state.flags = {'trickster.ever', share}
        V.sim_complete(self.model, state)
        def visible(block):
            return (set(block.get('Requires', [])) <= state.flags
                    and not set(block.get('Forbids', [])) & state.flags
                    and all(set(group) & state.flags for group in block.get('AnyGroups', [])))
        terminals = {node['Id'] for node in event['Nodes']
                     if all(not c.get('Next') and not c.get('Check') for c in node['Choices'])}
        self.assertIn('went', terminals)
        for page in event['Nodes']:
            summaries = [block for block in page.get('Paragraphs', [])
                         if share in block.get('Requires', []) and visible(block)]
            with self.subTest(node=page['Id']):
                if page['Id'] not in terminals:
                    self.assertFalse(summaries)
                elif page['Id'] == 'went':
                    self.assertTrue(summaries)
                    for block in summaries:
                        self.assertFalse(set(block.get('Requires', [])) <= set())
                        self.assertTrue(set(block.get('Requires', [])) <= {share})

    def test_jerribeth_selected_paths_print_each_partner_summary_once(self):
        from storylines import jerribeth_partner as J
        event = self.scenes['jerribeth.trickster.epilogue.commit']
        graph = self.model.nodes[event['Id']]
        summaries = {(tuple(block['Requires']), tuple(block['Forbids']), tuple(tuple(g) for g in block['AnyGroups'])) for block in J.partner_paragraphs()}
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
                here = [(tuple(b['Requires']), tuple(b['Forbids']), tuple(tuple(g) for g in b['AnyGroups'])) for b in page.get('Paragraphs', [])
                        if (tuple(b['Requires']), tuple(b['Forbids']), tuple(tuple(g) for g in b['AnyGroups'])) in summaries and visible(b)
                        and (b['Requires'] or all(not c.get('Next') for c in page['Choices']))]
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

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        page = self.node('eliandra.trickster.epilogue.late', 'page')
        with patch.dict(page, Choices=list(reversed(page['Choices']))):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_eliandra_decision_precedes_night_lifetime_and_coda()


if __name__ == '__main__':
    unittest.main()
