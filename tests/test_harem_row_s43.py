"""S43's deed/attendance contract on the assembled integration payload."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s43
from tools import rrt_verify as verify, savecompat, harem_schedule_lint

ROOT = Path(__file__).resolve().parents[1]
P = s43.P


class RowS43(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
        s43.register(cls.story, cls.story["Scenes"], cls.story["Etudes"])
        cls.model = verify.Model(cls.story)
        cls.rows = {s["Id"]: s for s in cls.story["Scenes"] if s["Id"].startswith(P) and s.get("InteractionHub")}

    def state(self, seat="pair", step="settle", hour=1000):
        state = verify.SimState(5, hour)
        state.flags.update(["availability.observed", "trickster", "trickster.now", "foresight.page_taken",
                            "trickster.foresight.accepted", "trickster.foresight.cost.promise", "household.table.kept",
                            "kaylessa.committed", "kaylessa.trickster.returned", "kaylessa.trickster.clock_named",
                            "kaylessa.trickster.knife_shown", "kaylessa.trickster.knife_held",
                            "kaylessa.trickster.presence_on", "anevia.committed", "anevia.future_chosen", "anevia.developed",
                            "anevia.trickster.gate_seen", "anevia.trickster.terms_kept"])
        if seat == "pair":
            state.flags.update(["committed", "tirabade.trickster.third_chair"])
        if step == "retry":
            state.flags.update([P + "settle.seen", P + "settle.failed"])
            state.times[P + "settle.failed"] = 1000
        verify.sim_complete(self.model, state)
        return state

    def available(self, state, step="settle", seat="pair"):
        verify.sim_complete(self.model, state)
        return verify.sim_available(self.model, verify.norm_scene(self.rows[P + step + "." + seat]), state)

    def answer(self, seat, step, node, index=0):
        body = self.rows[P + step + "." + seat]
        return next(n for n in body["Nodes"] if n["Id"] == node)["Choices"][index]

    def test_pair_qualifies_only_anevia_and_solo_survives_group_closure(self):
        state = self.state()
        self.assertTrue(self.available(state))
        self.assertFalse(self.available(state, seat="solo"))
        for flag in ("irabeth_dead", "irabeth_gone", "irabeth.epoch_unavailable", "irabeth.closed"):
            with self.subTest(flag=flag):
                changed = copy.deepcopy(state)
                changed.flags.add(flag)
                self.assertTrue(self.available(changed))
        state.flags.add("closed")
        self.assertFalse(self.available(state))
        self.assertTrue(self.available(state, seat="solo"))
        for body in self.rows.values():
            self.assertNotIn("tirabade.harem.eligible", body["Requires"])
            self.assertNotIn("irabeth.present_now", body["Requires"])

    def test_current_losses_closures_page_and_path_block_both_steps(self):
        for seat in ("pair", "solo"):
            for step in ("settle", "retry"):
                for flag in ("anevia.closed", "anevia_dead", "anevia.epoch_unavailable", "kaylessa.closed",
                             "kaylessa.trickster.left_free", "kaylessa.epoch_unavailable", "inhuman"):
                    with self.subTest(seat=seat, step=step, flag=flag):
                        state = self.state(seat, step, 1048)
                        state.flags.update([flag, "anevia.trickster.returned"])
                        self.assertFalse(self.available(state, step, seat))
                for flag in ("trickster", "trickster.foresight.accepted"):
                    state = self.state(seat, step, 1048)
                    state.flags.discard(flag)
                    state.flags.discard("foresight.page_taken")
                    self.assertFalse(self.available(state, step, seat))
        state = self.state()
        state.flags.add("anevia_gone")
        self.assertFalse(self.available(state))
        state.flags.add("anevia.trickster.returned")
        self.assertTrue(self.available(state))
        state.flags.add("anevia.epoch_unavailable")  # observer's later-loss result
        self.assertFalse(self.available(state))

    def test_retry_clock_pending_failure_and_shared_seen_survive_reload(self):
        for seat in ("pair", "solo"):
            state = self.state(seat, "retry", 1047)
            self.assertFalse(self.available(state, "retry", seat))
            state.hour = 1048
            self.assertTrue(self.available(state, "retry", seat))
            failure = self.answer(seat, "settle", "spotted")
            self.assertNotIn(s43.UNRESOLVED_INPUT, failure["Set"])
            self.assertFalse(any("attitude" in f or "enmity" in f or "stance" in f for f in failure["Set"]))
            self.assertTrue(self.answer(seat, "retry", "closed", 1)["Abort"])
            self.assertEqual(self.answer(seat, "retry", "closed", 1)["Set"], [])
            state.flags.update(self.answer(seat, "retry", "closed")["Set"])
            verify.sim_complete(self.model, state)
            self.assertIn(P + "settle.failed", state.flags)
            self.assertIn("kaylessa.harem.attitude.w.anevia.respect", state.flags)
            edge = "tirabade.harem.attitude.anevia.kaylessa.respect" if seat == "pair" else "anevia.harem.attitude.kaylessa.respect"
            self.assertIn(edge, state.flags)
            # A JSON flags/timestamps round trip models persisted witnesses, then a seat change.
            saved = json.loads(json.dumps(dict(flags=list(state.flags), times=state.times)))
            loaded = self.state("solo", "retry", 1100)
            loaded.flags = set(saved["flags"])
            loaded.times = saved["times"]
            loaded.flags.add("closed")
            self.assertFalse(self.available(loaded, "settle", "solo"))
            self.assertFalse(self.available(loaded, "retry", "solo"))

    def test_checks_abort_refusals_and_success_exact_witnesses(self):
        for seat in ("pair", "solo"):
            start = self.answer(seat, "settle", "start")
            self.assertEqual(start["Set"], [])
            self.assertEqual(start["Check"], dict(Skill="SkillStealth", DC=27, Success="broken", Failure="spotted"))
            for step, node in (("settle", "broken"), ("settle", "contact"), ("retry", "closed")):
                writes = set(self.answer(seat, step, node)["Set"])
                expected = {P + step + ".seen", P + step + ".done", *(P + f for f in s43.SUCCESS), P + "used_" + seat + "_seat"}
                if node in ("contact", "closed"):
                    expected.update([P + "cost.commander_courier", P + "contact_spent"])
                if node == "closed":
                    expected.add(P + "cost.anevia_lookout_burned")
                self.assertEqual(writes, expected)
                self.assertTrue(self.answer(seat, step, node, 1)["Abort"])
            for step, node in (("settle", "declined"), ("retry", "refused")):
                self.assertEqual(set(self.answer(seat, step, node)["Set"]), {P + step + ".seen", P + step + ".declined", s43.UNRESOLVED_INPUT})

    def test_every_branch_keeps_a_selectable_answer_without_early_spending(self):
        for seat in ("pair", "solo"):
            for step in ("settle", "retry"):
                state = self.state(seat, step, 1048)
                body = self.rows[P + step + "." + seat]
                by_node = {node["Id"]: node for node in body["Nodes"]}
                pending = ["start"]
                reached = set()
                while pending:
                    nid = pending.pop()
                    if nid in reached:
                        continue
                    reached.add(nid)
                    answers = [a for a in by_node[nid]["Choices"] if verify.sim_choice_available(a, state)]
                    self.assertTrue(answers, body["Id"] + "/" + nid)
                    for answer in answers:
                        targets = ([answer["Next"]] if answer.get("Next") else
                                   [answer["Check"]["Success"], answer["Check"]["Failure"]] if answer.get("Check") else [])
                        if targets or answer["Abort"]:
                            self.assertEqual(answer["Set"], [])
                        pending.extend(targets)
                self.assertEqual(reached, set(by_node))

    def test_history_is_not_invented_and_unrelated_enmity_is_retained(self):
        for seat in ("pair", "solo"):
            state = self.state(seat)
            state.flags.add("anevia.harem.enmity.nurah")
            for history in ((), ("kaylessa.anevia_caught",), ("kaylessa.unmasked",),
                            ("kaylessa.anevia_caught", "kaylessa.unmasked")):
                changed = copy.deepcopy(state)
                changed.flags.update(history)
                self.assertTrue(self.available(changed, seat=seat))
                changed.flags.update(self.answer(seat, "settle", "broken")["Set"])
                verify.sim_complete(self.model, changed)
                self.assertIn("anevia.harem.enmity.nurah", changed.flags)
            text = " ".join(n["Text"] for n in self.rows[P + "settle." + seat]["Nodes"])
            self.assertNotIn("amulet", text)
            self.assertNotIn("mask", text)

    def test_distinct_edges_no_irabeth_objection_and_respect_requires_deeds(self):
        state = self.state()
        state.flags.add("tirabade.harem.enmity.irabeth.kaylessa")
        self.assertTrue(self.available(state))
        state.flags.add("tirabade.harem.enmity.anevia.kaylessa")
        self.assertFalse(self.available(state))
        state.flags.add("tirabade.harem.reconciled.anevia.kaylessa")
        self.assertTrue(self.available(state))
        for flag, groups in s43.STAGE_PRODUCERS.items():
            for missing in groups[0]:
                probe = verify.SimState(5, 1000)
                probe.flags.update(set(groups[0]) - {missing})
                verify.sim_complete(self.model, probe)
                self.assertNotIn(flag, probe.flags)

    def test_budget_savecompat_reader_shape_and_idempotent_registration(self):
        self.assertEqual(savecompat.check(self.story), [])
        for body in self.rows.values():
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["Chapters"], [5])
            self.assertNotIn("HouseholdArcStart", body)
            self.assertFalse(any(n.get("Paragraphs") for n in body["Nodes"]))
            self.assertEqual(harem_schedule_lint.delayed_clock_errors(body, self.story), [])
        for body in [*self.rows.values(), next(s for s in self.story["Scenes"] if s["Id"] == "kaylessa.clearing.grey_light")]:
            node_ids = {node["Id"] for node in body["Nodes"]}
            for node in body["Nodes"]:
                for answer in node["Choices"]:
                    if answer.get("Next"):
                        self.assertIn(answer["Next"], node_ids)
        before = copy.deepcopy(self.story)
        s43.register(self.story, self.story["Scenes"], self.story["Etudes"])
        self.assertEqual(before, self.story)


if __name__ == "__main__":
    unittest.main()
