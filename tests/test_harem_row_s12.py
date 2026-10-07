"""Ruling 03: deeds, pending retry, directional refusal and current bodies."""
import copy
import unittest

from storylines import contract_j01
from storylines.harem_rows import s12, zz_contract_controller as controller
from tests.harem_row_walk import walk
from tools import rrt_verify as rules


class S12ContractTests(unittest.TestCase):
    def setUp(self):
        self.story = dict(Scenes=[], Etudes={}, Relationships={
            w: dict(StartedFlag=w + ".started", ClosedFlag=w + ".closed",
                    CommittedFlag=w + ".committed", UnavailableFlags=[])
            for w in ("household", *s12.PAIR)},
            Presences={w + ".presence": dict(Unit=str(i + 1) * 32)
                       for i, w in enumerate(s12.PAIR)},
            SeatWomen={}, DepartureEpochs={}, RestAllowances={"household.protected": 2})
        s12.register(self.story, self.story["Scenes"], {})
        controller._publish(self.story, self.story["Scenes"], [
            rule for rule in controller.policy()["failures"] if rule["ruling"] == 3])
        self.story["Derived"]["nenio.harem.enmity_any"] = [
            ["nenio.harem.enmity.camellia"], ["nenio.harem.enmity.seelah"]]
        contract_j01.install(self.story)
        self.model = rules.Model(self.story)
        self.rows = self.model.by_id

    def state(self):
        state = rules.SimState(5, 100)
        state.flags.update(s12.COMMON_REQUIRES)
        state.available_contacts = {"1" * 32, "2" * 32}
        state.area = self.rows[s12.P("settle")]["Areas"][0]
        return self.complete(state)

    def complete(self, state):
        rules.sim_complete(self.model, state)
        return state

    def outcomes(self, step, state):
        return [self.complete(st) for st in walk(self, self.model, self.rows[s12.P(step)], state)]

    def test_choice_indices_one_retry_and_no_new_check_fee_item_or_preparation(self):
        self.assertFalse(s12.BLOCKERS)
        for step, targets in (("settle", ["lesson", "spoiled", "refused", None]),
                              ("retry", ["lesson", "refused", None])):
            body = self.rows[s12.P(step)]
            choices = body["Nodes"][0]["Choices"]
            self.assertEqual([c["Next"] for c in choices[:len(targets)]], targets)
            self.assertEqual(choices[-1]["Next"], "bench_work")
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["HouseholdCategory"], "protected")
            self.assertEqual(body["Chapters"], [5])
            self.assertIn(s12.P(step + ".seen"), body["Forbids"])
            for node in body["Nodes"]:
                for choice in node["Choices"]:
                    self.assertFalse(any(choice.get(k) for k in ("Check", "RemoveItem", "Crusade", "Revive")))
                    self.assertNotIn("foresight.page_taken", choice["Set"])
        self.assertEqual(self.rows[s12.P("retry")]["DelayHours"], 48)
        self.assertIn(s12.P("settle.failed"), self.rows[s12.P("retry")]["Requires"])

    def test_both_approaches_finish_after_both_women_act_and_keep_asymmetry(self):
        nodes = {n["Id"]: n for n in self.rows[s12.P("settle")]["Nodes"]}
        for node in ("lesson", "bench_work", "manual_correction"):
            self.assertEqual(nodes[node]["Choices"][0]["Set"], [])
        done = [st for st in self.outcomes("settle", self.state()) if s12.P("settle.done") in st.flags]
        self.assertEqual(len(done), 2)
        for state in done:
            self.assertTrue(set(s12.DEED_COSTS) <= state.flags)
            self.assertIn(s12.SHARED_CRAFT_WITNESS, state.flags)
            self.assertIn("nenio.harem.attitude.camellia.respect", state.flags)
            self.assertNotIn("nenio.harem.attitude.camellia.rival", state.flags)
            self.assertIn("camellia.harem.attitude.nenio.rival", state.flags)
            self.assertNotIn("camellia.harem.attitude.nenio.respect", state.flags)
            self.assertEqual(state.rest_spent["household.protected"], 1)
            self.assertFalse(any(f.endswith((".friend", ".lover")) for f in state.flags))

    def test_accusation_then_48_hour_success_is_pending_without_enmity(self):
        failed = next(st for st in self.outcomes("settle", self.state()) if s12.P("settle.failed") in st.flags)
        self.assertNotIn("nenio.harem.enmity.camellia", failed.flags)
        self.assertNotIn("nenio.harem.stance.tolerated", failed.flags)
        self.assertNotIn(s12.P("unsettled"), failed.flags)
        retry = self.rows[s12.P("retry")]
        for hour, expected in ((147, False), (148, True)):
            failed.hour = hour
            self.assertEqual(rules.sim_available(self.model, retry, failed), expected)
        failed.times[s12.P("ready")] = 148
        self.assertTrue(rules.sim_available(self.model, retry, failed))
        done = next(st for st in self.outcomes("retry", failed) if s12.P("settle.done") in st.flags)
        self.assertIn(s12.P("settle.failed"), done.flags)
        self.assertIn("nenio.harem.attitude.camellia.respect", done.flags)
        self.assertFalse(any(".enmity." in f or ".reconciled." in f for f in done.flags))
        self.assertFalse(rules.sim_available(self.model, retry, done))
        self.assertEqual(done.rest_spent["household.protected"], 2)

    def test_direct_and_retry_refusal_publish_only_nenios_first_target(self):
        for retry in (False, True):
            state = self.state()
            if retry:
                state.flags.update((s12.P("settle.seen"), s12.P("settle.failed")))
                state.times[s12.P("settle.failed")] = 52
            refused = next(st for st in self.outcomes("retry" if retry else "settle", state)
                           if s12.P("unsettled") in st.flags)
            self.assertIn("nenio.harem.enmity.camellia", refused.flags)
            self.assertIn("nenio.harem.stance.tolerated", refused.flags)
            self.assertNotIn("camellia.harem.enmity.nenio", refused.flags)
            self.assertNotIn(s12.P("settle.done"), refused.flags)
            self.assertNotIn(s12.SHARED_CRAFT_WITNESS, refused.flags)
        state = self.state()
        state.flags.update(("nenio.harem.enmity.seelah", "nenio.harem.reconciled.seelah"))
        self.complete(state)
        refused = next(st for st in self.outcomes("settle", state) if s12.P("unsettled") in st.flags)
        self.assertNotIn("nenio.harem.enmity.camellia", refused.flags)
        self.assertIn("nenio.harem.enmity.seelah", refused.flags)

    def test_later_is_pre_action_with_no_receipt_or_allowance_spend(self):
        for step in ("settle", "retry"):
            state = self.state()
            state.flags.add(s12.P("settle.failed"))
            state.times[s12.P("settle.failed")] = 52
            aborted = [st for st in self.outcomes(step, state) if st.flags == state.flags]
            self.assertEqual(len(aborted), 1)
            self.assertEqual(aborted[0].rest_spent, {})

    def test_unpaid_off_path_absence_closure_and_latest_losses_block(self):
        for step in ("settle", "retry"):
            state = self.state()
            state.flags.add(s12.P("settle.failed"))
            state.times[s12.P("settle.failed")] = 52
            body = self.rows[s12.P(step)]
            self.assertTrue(rules.sim_available(self.model, body, state))
            for missing in s12.COMMON_REQUIRES:
                probe = copy.deepcopy(state)
                probe.flags.discard(missing)
                self.complete(probe)
                self.assertFalse(rules.sim_available(self.model, body, probe), missing)
            for loss in ("trickster.failed", "household.closed", "nenio.closed", "camellia.closed",
                         "nenio.life.unavailable", "nenio.epoch_unavailable", "camellia.returned_actor_lost",
                         "engine.l12.commander_unreturned", "sacrifice"):
                probe = copy.deepcopy(state)
                probe.flags.update((loss, "nenio.life.recreated", "camellia.trickster.coffin_life"))
                self.complete(probe)
                self.assertFalse(rules.sim_available(self.model, body, probe), loss)
            for unit in ("1" * 32, "2" * 32):
                probe = copy.deepcopy(state)
                probe.available_contacts.remove(unit)
                self.assertFalse(rules.sim_available(self.model, body, probe))
                for node in body["Nodes"]:
                    self.assertFalse(rules.sim_contact_available(self.model, body, probe), node["Id"])
            recreated = copy.deepcopy(state)
            recreated.flags.add("nenio.life.unremembered")
            self.assertTrue(rules.sim_available(self.model, body, recreated))

    def test_craft_needs_full_work_and_is_not_confession_or_affection(self):
        state = self.state()
        state.flags.update(s12.DEED_COSTS[:-1])
        self.complete(state)
        self.assertNotIn(s12.SHARED_CRAFT_WITNESS, state.flags)
        state.flags.add(s12.DEED_COSTS[-1])
        self.complete(state)
        self.assertIn(s12.SHARED_CRAFT_WITNESS, state.flags)
        self.assertNotIn("camellia.mireya_unmasked", state.flags)
        state.flags.add("nenio.harem.enmity.camellia")
        self.complete(state)
        self.assertNotIn("nenio.harem.attitude.camellia.respect", state.flags)
        state.flags.add("nenio.harem.reconciled.camellia")
        self.complete(state)
        self.assertIn("nenio.harem.attitude.camellia.respect", state.flags)


if __name__ == "__main__":
    unittest.main()
