"""S16 branch walks, exact receipts, attendance and append-only registration."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from storylines.harem_rows import s16
from tools import rrt_verify
from story_fixture import fresh_story


class S16Tests(unittest.TestCase):
    def setUp(self):
        self.payload = {"Scenes": []}
        s16.register(self.payload, [], {})
        self.rows = self.payload["Scenes"]

    def test_registration_is_isolated_and_repeatable(self):
        original = [dict(Id="existing", Nodes=[dict(Id="old", Choices=[dict(Next="kept")])])]
        base = copy.deepcopy(original)
        payload = dict(Scenes=list(base))
        s16.register(payload, base, {})
        s16.register(payload, base, {})
        self.assertEqual(base, original)
        self.assertEqual(len(payload["Scenes"]), 9)

    def test_all_choice_paths_publish_only_the_exhaustive_sheet_receipts(self):
        for row in self.rows:
            step = "retry" if row["Id"].startswith(s16.P + "retry") else "settle"
            nodes = {n["Id"]: n for n in row["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertEqual(len(root), 4)
            self.assertTrue(root[3]["Abort"])
            self.assertFalse(root[3]["Set"])
            self.assertIsNone(root[3]["Next"])
            for choice in root[:3]:
                self.assertFalse(choice["Set"])
                destinations = ([choice["Check"]["Success"], choice["Check"]["Failure"]]
                                if "Check" in choice else [choice["Next"]])
                for destination in destinations:
                    result = nodes[destination]["Choices"]
                    self.assertEqual(len(result), 1)
                    self.assertIsNone(result[0]["Next"])
                    self.assertFalse(result[0]["Abort"])
                    outcome = ("kept" if destination in ("returned", "carried") else
                               "failed" if destination in ("failed", "misquoted") else "declined")
                    self.assertEqual(result[0]["Set"], list(s16.receipts(step, outcome)))
            if step == "settle":
                self.assertEqual(root[0]["Check"], dict(Skill="CheckDiplomacy", DC=22,
                                                       Success="carried", Failure="misquoted", CommanderOnly=True))

    def test_channel_variants_share_clocks_and_never_create_bodies(self):
        for row in self.rows:
            retry = row["Id"].startswith(s16.P + "retry")
            self.assertEqual(row["DelayHours"], 48 if retry else 0)
            self.assertEqual(row["RestAllowance"], "household.protected")
            self.assertEqual(row["Chapters"], [5])
            self.assertTrue(row["Remote"] and row["ManualOnly"])
            self.assertNotIn("InteractionHub", row)
            self.assertIn(row["ContactUnit"], (s16.QUEEN, s16.KITRANE))
            self.assertIn("galfrey.present_now", row["Requires"])
            if retry:
                self.assertIn(s16.P + "settle.failed", row["Requires"])
                self.assertIn(s16.P + "settle.kept", row["Forbids"])
            if row["Id"].endswith(".post"):
                self.assertIn("konomi.reachable_by_letter", row["Requires"])
                self.assertNotIn(s16.KONOMI, row["AdditionalContactUnits"])
                self.assertNotIn("konomi.present_now", row["Requires"])
            else:
                self.assertIn(s16.KONOMI, row["AdditionalContactUnits"])
                self.assertIn("konomi.present_now", row["Requires"])
                self.assertIn("konomi.private_departed", row["Forbids"])
                self.assertNotIn("konomi.dead.unreturned", row["Forbids"])
                self.assertNotIn("ForbidOverrides", row)
            if ".kitrane" in row["Id"]:
                self.assertIn("galfrey.trickster.returned", row["Requires"])
                self.assertEqual(row["ContactUnit"], s16.KITRANE)
            else:
                self.assertIn("galfrey.final", row["Requires"])
                self.assertIn("galfrey.trickster.returned", row["Forbids"])
                self.assertEqual(row["ContactUnit"], s16.QUEEN)

    def test_current_gate_negative_histories_and_retry_time(self):
        # Small Rules mirror isolates this row's gates from unrelated route paths.
        payload = copy.deepcopy(self.payload)
        payload.update(Relationships={r: dict(StartedFlag=r + ".started", ClosedFlag=r + ".closed", CommittedFlag=r + ".committed", UnavailableFlags=[])
                                      for r in ("household", "galfrey", "konomi")},
                       RestAllowances={"household.protected": 2})
        model = rrt_verify.Model(payload)
        row = model.by_id[s16.P + "retry"]
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(row["Requires"] + ["galfrey.harem.eligible", "konomi.harem.eligible", "konomi.present"])
        state.times[s16.P + "settle.failed"] = 952
        self.assertTrue(rrt_verify.sim_available(model, row, state))
        state.times[s16.P + "settle.failed"] = 953
        self.assertFalse(rrt_verify.sim_available(model, row, state))
        state.times[s16.P + "settle.failed"] = 952
        for key in ("trickster", "foresight.page_taken", "galfrey.present_now", "konomi.present_now"):
            state.flags.remove(key)
            self.assertFalse(rrt_verify.sim_available(model, row, state), key)
            state.flags.add(key)
        for key in ("galfrey.closed", "konomi.closed", "galfrey.epoch_unavailable",
                    "konomi.epoch_unavailable", "galfrey.killed_by_commander",
                    "konomi.retained_dead", "engine.l12.commander_unreturned", s16.P + "retry.seen"):
            state.flags.add(key)
            self.assertFalse(rrt_verify.sim_available(model, row, state), key)
            state.flags.remove(key)
        state.chapter = 6
        self.assertFalse(rrt_verify.sim_available(model, row, state))

    def test_assembled_earned_history_and_later_loss(self):
        model = rrt_verify.Model(fresh_story())
        row = model.by_id[s16.P + "settle"]
        state = rrt_verify.SimState(5, 1000)
        state.flags.update([
            "trickster", "trickster.foresight.accepted", "household.table.kept",
            "galfrey.romance_finished", "galfrey.final", "konomi.committed", "konomi.power",
            "konomi.present", "availability.observed",
        ])
        rrt_verify.sim_complete(model, state)
        self.assertTrue(rrt_verify.sim_available(model, row, state))
        for key in ("galfrey.epoch_unavailable", "konomi.returned_actor_lost", "konomi.closed"):
            lost = copy.deepcopy(state)
            lost.flags.add(key)
            lost.flags.update(["galfrey.trickster.returned", "konomi.trickster.returned"])
            rrt_verify.sim_complete(model, lost)
            self.assertFalse(rrt_verify.sim_available(model, row, lost))
        # Existing route-open eligibility veto is deliberately preserved: a
        # historical private-post arrangement does not become bodily attendance.
        departed = copy.deepcopy(state)
        departed.flags.discard("konomi.present")
        departed.flags.update(["konomi.private_departed", "konomi.private_evening_kept",
                               "konomi.private_address", "konomi.private_letters", "konomi.epoch_unavailable"])
        rrt_verify.sim_complete(model, departed)
        self.assertIn("konomi.reachable_by_letter", departed.flags)
        self.assertNotIn("konomi.harem.eligible", departed.flags)
        self.assertFalse(rrt_verify.sim_available(model, model.by_id[s16.P + "settle.post"], departed))



if __name__ == "__main__":
    unittest.main()
