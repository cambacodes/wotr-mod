"""S19 sheet contract: exact outcomes, branch precedence, current attendance."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines import household, foresight
from storylines.harem_rows import s19
from tools import harem_schedule_lint, rrt_verify, savecompat


class S19Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)

    def setUp(self):
        self.payload = copy.deepcopy(self.base)
        self.entries = list(household.ENTRIES)
        self.consumers = dict(household.CONSUMERS)
        self.foresight = dict(foresight.CONSUMERS)
        s19.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.rows = [s for s in self.payload["Scenes"] if s["Id"].startswith(s19.P)]

    def tearDown(self):
        household.ENTRIES[:] = self.entries
        household.CONSUMERS.clear()
        household.CONSUMERS.update(self.consumers)
        foresight.CONSUMERS.clear()
        foresight.CONSUMERS.update(self.foresight)

    def test_shared_ids_choices_and_terminal_sets(self):
        self.assertEqual(len(self.rows), 4)
        for row in self.rows:
            step, branch = row["Id"][len(s19.P):].split(".")
            nodes = {n["Id"]: n for n in row["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertEqual(len(root), 4)
            self.assertTrue(root[3]["Abort"])
            self.assertTrue(all(not c["Set"] for c in root))
            self.assertEqual(root[0].get("Check", {}).get("DC"), 20 if step == "settle" else None)
            for key, node in nodes.items():
                if key == "start":
                    continue
                self.assertEqual(len(node["Choices"]), 1)
                choice = node["Choices"][0]
                self.assertIsNone(choice["Next"])
                outcome = "kept" if key in ("draw", "carry") else "failed" if key in ("botched", "failed") else "declined"
                self.assertEqual(set(choice["Set"]), set(s19.terminal(step, outcome, branch)))
                self.assertTrue(all(flag.startswith(s19.P) for flag in choice["Set"]))
            self.assertFalse(any(n.get("Paragraphs") for n in nodes.values()))
        self.assertEqual(savecompat.check(self.payload), [])
        self.assertEqual(rrt_verify.validate(rrt_verify.Model(self.payload)), [])

    def test_paid_page_live_bodies_and_qualified_seat(self):
        for row in self.rows:
            self.assertEqual(row["Participants"], list(s19.PAIR))
            self.assertEqual(row["ParticipantWomen"], ["minagho"])
            self.assertNotIn("minagho_chivarro.harem.eligible", row["Requires"])
            self.assertIn("participant.minagho.available", row["Requires"])
            for flag in ("trickster", household.PAGE_TAKEN, household.KEPT, household.STANCE_ELIGIBLE,
                         "minagho.present_now", "arueshalae.present_now"):
                self.assertIn(flag, row["Requires"])
            for flag, override in s19.QUALIFIED.items():
                self.assertIn(flag, row["Forbids"])
                self.assertEqual(row["ForbidOverrides"][flag], override)
            for flag, override in row["ForbidOverrides"].items():
                self.assertIn(flag, self.payload["PendingHooks"])
                self.assertIn(override, self.payload["PendingHooks"])
            for flag in ("household.closed", "fool_king.gone", "trickster.failed", "engine.l12.commander_unreturned"):
                self.assertIn(flag, row["Forbids"])
            self.assertNotIn("chivarro.present_now", row["Requires"])
            self.assertFalse(any("chivarro.dead" == f for f in row["Requires"] + row["Forbids"]))

    def test_branch_precedence_clocks_and_caps(self):
        for row in self.rows:
            self.assertEqual(row["Chapters"], [5])
            self.assertEqual(row["RestAllowance"], "household.protected")
            self.assertEqual(row["HouseholdCategory"], "protected")
            self.assertFalse(any(".cap." in f for f in row["Forbids"]))
            if row["Id"].endswith(".good"):
                self.assertIn("arueshalae.redeemed", row["Requires"])
                self.assertIn("arueshalae.corrupted", row["Forbids"])
            else:
                self.assertIn("arueshalae.corrupted", row["Requires"])
            retry = ".retry." in row["Id"]
            self.assertEqual(row["DelayHours"], 48 if retry else 0)
            if retry:
                self.assertIn(s19.P + "settle.failed", row["Requires"])
                self.assertIn(s19.P + "settle.kept", row["Forbids"])
                self.assertIn(s19.P + "settle.declined", row["Forbids"])
            self.assertEqual(harem_schedule_lint.delayed_clock_errors(row, self.payload), [])

    def test_registration_is_repeatable_and_history_survives_departure(self):
        s19.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.assertEqual(len([s for s in self.payload["Scenes"] if s["Id"].startswith(s19.P)]), 4)
        ledger = self.payload["Books"]["trickster.ledger"]["Entries"]
        entries = [e for e in ledger if e["Id"] == "seating.s19"]
        self.assertEqual(len(entries), 1)
        self.assertFalse(any("present_now" in f for f in entries[0]["Requires"]))
        self.assertTrue(all(not any("present_now" in f for f in line["Requires"]) for line in entries[0]["Lines"]))

    def test_current_losses_enmity_and_retry_delay_in_rules_mirror(self):
        model = rrt_verify.Model(self.payload)
        good = model.by_id[s19.P + "settle.good"]
        fallen = model.by_id[s19.P + "settle.fallen"]
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(good["Requires"])
        # Qualified Participants still require an earned seat, not Chivarro's body.
        state.flags.update(["minachiv.complete", "minachiv.before_the_last_road", "minachiv.future_minagho",
                            "minagho_chivarro.payoff.ordinary"])
        for chivarro_state in (None, "chivarro.dead", "chivarro.epoch_unavailable", "chivarro.closed"):
            trial = copy.deepcopy(state)
            if chivarro_state:
                trial.flags.add(chivarro_state)
            self.assertTrue(rrt_verify.sim_available(model, good, trial), chivarro_state)
        for missing in ("foresight.page_taken", "trickster", "minagho.present_now", "arueshalae.present_now"):
            trial = copy.deepcopy(state)
            trial.flags.remove(missing)
            self.assertFalse(rrt_verify.sim_available(model, good, trial), missing)
        unknown = copy.deepcopy(state)
        unknown.flags.remove("arueshalae.redeemed")
        self.assertFalse(rrt_verify.sim_available(model, good, unknown))
        self.assertFalse(rrt_verify.sim_available(model, fallen, unknown))
        for loss in ("minachiv.closed", "arueshalae.closed", "minagho.dead", "minagho.epoch_unavailable", "arueshalae.kicked_out",
                     "minagho_chivarro.trickster.declined_minagho", "engine.l12.commander_unreturned"):
            trial = copy.deepcopy(state)
            trial.flags.add(loss)
            self.assertFalse(rrt_verify.sim_available(model, good, trial), loss)
        stale_return = copy.deepcopy(state)
        stale_return.flags.update(["minagho_chivarro.trickster.returned_minagho", "minagho.epoch_unavailable"])
        self.assertFalse(rrt_verify.sim_available(model, good, stale_return))
        state.flags.add("arueshalae.corrupted")
        self.assertFalse(rrt_verify.sim_available(model, good, state))
        self.assertTrue(rrt_verify.sim_available(model, fallen, state))
        for enmity, override in s19.QUALIFIED.items():
            trial = copy.deepcopy(state)
            trial.flags.add(enmity)
            self.assertFalse(rrt_verify.sim_available(model, fallen, trial))
            trial.flags.add(override)
            self.assertTrue(rrt_verify.sim_available(model, fallen, trial))
        retry = model.by_id[s19.P + "retry.fallen"]
        state.flags.add(s19.P + "settle.failed")
        state.times[s19.P + "settle.failed"] = 953
        self.assertFalse(rrt_verify.sim_available(model, retry, state))
        state.hour = 1001
        self.assertTrue(rrt_verify.sim_available(model, retry, state))
        state.rest_spent["household.protected"] = 2
        self.assertFalse(rrt_verify.sim_available(model, retry, state))


if __name__ == "__main__":
    unittest.main()
