"""SAT parity, the old disclosure shape, and explicit proof deadline failures."""
import itertools
import random
import time
import unittest
from unittest.mock import patch

from tools.crossroute_checks.common import AND, OR, lit, Proof, satisfiable, verify, dependencies


def old_satisfiable(cs):
    """Frozen pre-fix solver, used only as a small-formula parity oracle."""
    while True:
        if any(not c for c in cs):
            return False
        units = {c[0] for c in cs if len(c) == 1}
        if any(-x in units for x in units):
            return False
        if not units:
            break
        cs = [tuple(x for x in c if -x not in units) for c in cs if not any(x in units for x in c)]
    if not cs:
        return True
    counts = {}
    for c in cs:
        for x in c:
            counts[x] = counts.get(x, 0) + 1
    pure = {x for x in counts if -x not in counts}
    if pure:
        return old_satisfiable([c for c in cs if not any(x in pure for x in c)])
    x = min(cs, key=len)[0]
    return old_satisfiable(cs + [(x,)]) or old_satisfiable(cs + [(-x,)])


def disclosure_model(groups):
    """Old subset dispatches with long negative prefixes and opaque Counts.

    Include the dispatch union in route_open, so proving unrelated household
    guards still encodes the whole disclosure dependency graph.
    """
    derived, forbids, counts = {}, {}, {}
    prefix, ready = [], []
    for group in range(groups):
        keys = ['undisclosed.%d.%d' % (group, i) for i in range(4)]
        for key in keys:
            derived[key] = [[key + '.current']]
            forbids[key] = [key + '.receipt']
        for bits in itertools.product((False, True), repeat=4):
            if not any(bits):
                continue
            key = 'disclosure_dispatch.%d.%s' % (group, ''.join(map(str, map(int, bits))))
            derived[key] = [[k for k, bit in zip(keys, bits) if bit]]
            forbids[key] = prefix + [k for k, bit in zip(keys, bits) if not bit]
            counts[key + '.ready'] = dict(Of=[key], Min=1)
            ready.append(key)
        prefix += keys
    derived['household.outcome.route_open'] = [['household.open', 'camellia', 'arueshalae.corrupted']] + [[k] for k in ready]
    return verify.Model(dict(Scenes=[], Relationships={}, Derived=derived, DerivedForbids=forbids, Counts=counts))


class SolverTests(unittest.TestCase):
    def test_dependency_walk_matches_old_paths_including_cycles(self):
        def old(model, expr, seen=()):
            if expr[0] != 'lit':
                return set().union(*(old(model, x, seen) for x in expr[1:]))
            key = expr[1]
            result = {key}
            if key not in seen:
                for source in verify.composite_inputs(model, key):
                    result.update(old(model, lit(source), (*seen, key)))
            return result

        rng = random.Random(910)
        for _ in range(80):
            keys = ['key%d' % i for i in range(6)]
            derived = {key: [[rng.choice(keys) for _ in range(rng.randrange(3))]
                             for _ in range(rng.randrange(3))] for key in keys}
            model = verify.Model(dict(Scenes=[], Relationships={}, Derived=derived,
                                      DerivedForbids={k: [rng.choice(keys)] for k in keys},
                                      Counts={'count': dict(Of=rng.sample(keys, rng.randrange(4)), Min=1)},
                                      Latches={'latch': [rng.choice(keys)]}))
            expression = AND(lit(rng.choice(keys)), OR(lit('count', False), lit('latch')))
            for seen in ((), ('key1', 'key4')):
                self.assertEqual(dependencies(model, expression, seen), old(model, expression, seen))

    def test_random_small_cnfs_match_old_solver_and_truth_table(self):
        rng = random.Random(83017)
        cases = [[], [()], [(1,), (-1,)], [(1, 1), (-1,)], [(1, -1)]]
        for _ in range(800):
            variables = rng.randint(1, 6)
            cases.append([tuple(rng.choice((-1, 1)) * rng.randint(1, variables)
                                for _ in range(rng.randint(1, 5)))
                          for _ in range(rng.randint(0, 18))])
        for cs in cases:
            keys = sorted({abs(x) for c in cs for x in c})
            truth = any(all(any(values[abs(x)] == (x > 0) for x in c) for c in cs)
                        for bits in itertools.product((False, True), repeat=len(keys))
                        for values in [dict(zip(keys, bits))])
            with self.subTest(clauses=cs):
                self.assertEqual(old_satisfiable(cs), truth)
                self.assertEqual(satisfiable(cs), truth)

    def test_deep_unit_chain_and_conflicting_last_assignment(self):
        chain = [(1,)] + [(-i, i + 1) for i in range(1, 1500)]
        self.assertTrue(satisfiable(chain))
        self.assertFalse(satisfiable(chain + [(-1500,)]))

    def test_dorgelinda_shaped_household_proof(self):
        model = disclosure_model(10)
        proof = Proof(model)
        target = lit('household.outcome.route_open')
        context = AND(lit('household.open'), lit('camellia'), lit('arueshalae.corrupted'),
                      lit('harem.attitudes'), lit('ward_spent', False))
        start = time.monotonic()
        self.assertTrue(proof.implies(context, target))
        # An unearned open guard has a counterexample: the solver must still
        # report False, even with all the expensive dispatch arms present.
        self.assertFalse(proof.implies(lit('camellia'), target))
        self.assertLess(time.monotonic() - start, 5)

    def test_small_disclosure_shape_preserves_old_proof_results(self):
        model = disclosure_model(2)
        target = lit('household.outcome.route_open')
        contexts = (lit('camellia'), AND(lit('household.open'), lit('camellia'), lit('arueshalae.corrupted')),
                    AND(lit('undisclosed.0.0'), lit('undisclosed.0.1', False),
                        lit('undisclosed.0.2', False), lit('undisclosed.0.3', False)))
        for context in contexts:
            expected = Proof(model).implies(context, target)
            with patch('tools.crossroute_checks.common.satisfiable',
                       side_effect=lambda cs, check_deadline: old_satisfiable(cs)):
                self.assertEqual(Proof(model).implies(context, target), expected)

    def test_deadline_names_context_and_target_and_does_not_cache(self):
        proof = Proof(verify.Model(dict(Scenes=[], Relationships={})))
        context, target = lit('household.pair.camellia_arueshalae'), lit('household.outcome.route_open')
        with patch('tools.crossroute_checks.common.time.monotonic', side_effect=[0, 31]):
            with self.assertRaisesRegex(TimeoutError, '30 s.*context=.*camellia_arueshalae.*target=.*route_open'):
                proof.implies(context, target)
        self.assertEqual(proof.cache, {})
        self.assertFalse(proof.implies(context, target))
        with patch('tools.crossroute_checks.common.time.monotonic', side_effect=[0, 31]):
            with self.assertRaises(TimeoutError):
                proof.implies(context, target)  # the guard also covers cache hits

    def test_held_guard_does_not_expand_unrelated_definitions(self):
        proof = Proof(disclosure_model(10))
        context = AND(lit('camellia'), lit('arueshalae.corrupted'), lit('household.outcome.route_open'))
        with patch('tools.crossroute_checks.common.satisfiable', side_effect=AssertionError('unnecessary SAT query')):
            self.assertTrue(proof.implies(context, lit('camellia')))
            self.assertTrue(proof.implies(context, AND(lit('camellia'), lit('arueshalae.corrupted'))))
            self.assertTrue(proof.implies(context, OR(lit('camellia'), lit('other'))))
        self.assertFalse(proof.implies(context, lit('other')))

    def test_deadline_is_checked_during_sat_search(self):
        proof = Proof(verify.Model(dict(Scenes=[], Relationships={})))
        def slow_search(clauses, check_deadline):
            with patch('tools.crossroute_checks.common.time.monotonic', return_value=31):
                check_deadline()
        with patch('tools.crossroute_checks.common.time.monotonic', return_value=0), \
                patch('tools.crossroute_checks.common.satisfiable', side_effect=slow_search):
            with self.assertRaises(TimeoutError):
                proof.implies(lit('context'), lit('target'))
        self.assertEqual(proof.cache, {})




class S2ClosureProofTests(unittest.TestCase):
    def test_four_greetings_and_legends_are_selectable_with_iomedae_romance_closed(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        model = verify.Model(story)
        for suffix in ("", "_scarred", "_stall", "_scarred_stall"):
            scene = model.by_id["galfrey.trickster.return.kitrane" + suffix]
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            state = verify.SimState(5, 1000)
            state.flags.update({"trickster", "chapter_later", "iomedae.closed", "iomedae.epoch_unavailable",
                                "galfrey.trickster.eulogy.legend"})
            verify.sim_complete(model, state)
            self.assertIn("iomedae.closed", state.flags)
            self.assertNotIn("iomedae.present_now", state.flags)
            for index, choice in enumerate(nodes["name"]["Choices"][:3]):
                with self.subTest(scene=scene["Id"], node="name", index=index):
                    self.assertTrue(verify.sim_choice_available(choice, state))
            with self.subTest(scene=scene["Id"], node="heard", history="legend"):
                self.assertTrue(verify.sim_choice_available(nodes["heard"]["Choices"][1], state))

    def test_audited_reference_edges_do_not_depend_on_foreign_closed_flags(self):
        from tests.story_fixture import fresh_story
        from tools.crossroute_checks.common import fields
        story = fresh_story()
        model = verify.Model(story)
        cases = [("eritrice.trickster.fought.tabled", None, "noct.closed"),
                 ("nenio.folio.architect", None, "areelu.closed")]
        for suffix in ("", ".arcade"):
            for beat in ("correction", "captains", "other_voyage"):
                cases.append(("mielarah.deck." + beat + suffix, None, "noct.closed"))
        for suffix in ("", "_scarred", "_stall", "_scarred_stall"):
            cases.append(("galfrey.trickster.return.kitrane" + suffix, "name", "iomedae.closed"))
        for suffix in ("", "_visitor", "_arcade"):
            cases.append(("nenio.folio.edge" + suffix, "*", "areelu.closed"))
        for sid, nid, closed in cases:
            scene = model.by_id[sid]
            specs = ([scene] if nid is None else
                     [c for n in scene["Nodes"] for c in n["Choices"]] if nid == "*" else
                     next(n for n in scene["Nodes"] if n["Id"] == nid)["Choices"])
            for index, spec in enumerate(specs):
                with self.subTest(scene=sid, node=nid, index=index, closure=closed):
                    self.assertNotIn(closed, dependencies(model, fields(spec)))

    def test_four_greetings_are_selectable_with_iomedae_romance_closed(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        model = verify.Model(story)
        for suffix in ("", "_scarred", "_stall", "_scarred_stall"):
            scene = model.by_id["galfrey.trickster.return.kitrane" + suffix]
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            state = verify.SimState(5, 1000)
            state.flags.update({"trickster", "chapter_later", "iomedae.closed",
                                "galfrey.trickster.eulogy.legend"})
            verify.sim_complete(model, state)
            self.assertIn("iomedae.closed", state.flags)
            self.assertIn("iomedae.present_now", state.flags)
            for index, choice in enumerate(nodes["name"]["Choices"][:3]):
                with self.subTest(scene=scene["Id"], node="name", index=index):
                    self.assertTrue(verify.sim_choice_available(choice, state))


    def test_complete_both_mielarah_chains_after_nocticula_romance_closes(self):
        from tests.story_fixture import fresh_story
        model = verify.Model(fresh_story())
        romance_flags = {name: {r[field] for r in model.rels.values()}
                         for name, field in (("committed", "CommittedFlag"), ("closed", "ClosedFlag"))}
        for suffix in ("", ".arcade"):
            state = verify.SimState(5, 1000)
            state.area = "2570015799edf594daf2f076f2f975d8"
            state.available_contacts = {"9d9c523bc2b17434bb66df212b127187"}
            # Begin at her earned Chapter-5 flying lesson, before correction.
            state.flags.update({"trickster", "chapter_later", "noct.closed",
                                "mielarah.trickster.contact", "mielarah.deck.flown",
                                "mielarah.deck.docked", "mielarah.deck.reckoned",
                                "mielarah.trickster.landfall", "captain.kerz"})
            if suffix:
                state.flags.add("mielarah.presence.failed")
            verify.sim_complete(model, state)
            state.times = {flag: 0 for flag in state.flags}
            for beat in ("correction", "market", "wheel", "quarterdeck", "morning", "captains", "last_night"):
                scene = model.by_id["mielarah.deck." + beat + suffix]
                state.hour += 100
                verify.sim_complete(model, state)
                with self.subTest(scene=scene["Id"]):
                    self.assertTrue(verify.sim_available(model, scene, state))
                    self.assertTrue(verify.sim_play(model, scene, state, romance_flags))
            self.assertIn("mielarah.committed", state.flags)
            self.assertIn("mielarah.deck.captains", state.flags)
            self.assertIn("mielarah.deck.last_night", state.flags)
            self.assertIn("noct.closed", state.flags)
            self.assertNotIn("mielarah.closed", state.flags)

    def test_nenio_reads_the_badges_after_areelu_romance_closes(self):
        from tests.story_fixture import fresh_story
        model = verify.Model(fresh_story())
        for suffix in ("", "_visitor", "_arcade"):
            state = verify.SimState(5, 1000)
            state.flags.update({"trickster", "chapter_later", "areelu.closed", "nenio.trickster.scribe",
                                "nenio.folio.architect.the_dead"})
            verify.sim_complete(model, state)
            scene = model.by_id["nenio.folio.edge" + suffix]
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            for nid, index in (("open", 0), ("walk", 0), ("shields", 0), ("read", 0), ("sarkoris", 0), ("home", 0)):
                choice = nodes[nid]["Choices"][index]
                with self.subTest(scene=scene["Id"], node=nid, index=index):
                    self.assertTrue(verify.sim_choice_available(choice, state))
                state.flags.update(choice["Set"])
                verify.sim_complete(model, state)
            self.assertIn("nenio.folio.edge.shields", state.flags)
            self.assertIn("areelu.closed", state.flags)


if __name__ == '__main__':
    unittest.main()
