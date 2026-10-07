"""S49's actual emitted gates, terminal deeds and full-debit recovery."""
import copy
import json
from pathlib import Path
import unittest

from storylines import household
from storylines.harem_rows import s49
from tools import harem_schedule_lint, rrt_verify as rules


class RowS49(unittest.TestCase):
    def setUp(self):
        self.payload = dict(Scenes=[], Derived={}, Relationships={
            w: dict(StartedFlag=w + ".started", CommittedFlag=w + ".committed", ClosedFlag=w + ".closed",
                    UnavailableFlags=[w + ".dead", w + ".epoch_unavailable"], UnavailableOverrides={}) for w in s49.PAIR})
        self.payload["Relationships"]["household"] = household.relationship()
        self.payload["RestAllowances"] = {"household.protected": 2}
        s49.register(self.payload, self.payload["Scenes"], {})
        self.model = rules.Model(self.payload)
        self.by = {s["Id"].rsplit(".", 1)[-1]: s for s in self.model.scenes}

    def state(self, step="notice", age=48):
        scene = self.by[step]
        state = rules.SimState(5, 100)
        state.flags.update(scene["Requires"])
        state.flags.update(["wenduag.in_party", "wenduag.committed", "vellexia.committed"])
        if step == "retry":
            state.flags.add(s49.P + "handover.failed")
        state.times.update({flag: 100 - age for flag in state.flags})
        return state

    def test_gate_clock_and_current_bodies_at_every_step(self):
        for step, scene in self.by.items():
            state = self.state(step)
            self.assertTrue(rules.sim_available(self.model, scene, state), step)
            for missing in ("trickster.now", household.PAGE_TAKEN, "wenduag.present_now",
                            "vellexia.present_now", "vellexia.trickster.in_person"):
                bad = copy.deepcopy(state)
                bad.flags.remove(missing)
                self.assertFalse(rules.sim_available(self.model, scene, bad), (step, missing))
            for blocker in ("wenduag.closed", "vellexia.closed", "vellexia.trickster.visited",
                            "vellexia.trickster.kept_as_mirror", "sacrifice",
                            "wenduag.dead", "vellexia.dead", "wenduag.epoch_unavailable",
                            "vellexia.epoch_unavailable"):
                bad = copy.deepcopy(state)
                bad.flags.add(blocker)
                self.assertFalse(rules.sim_available(self.model, scene, bad), (step, blocker))
            for a, b in (s49.PAIR, tuple(reversed(s49.PAIR))):
                bad = copy.deepcopy(state)
                bad.flags.add(household.enmity(a, b))
                self.assertFalse(rules.sim_available(self.model, scene, bad))
                bad.flags.add(a + ".harem.reconciled." + b)
                self.assertTrue(rules.sim_available(self.model, scene, bad))
            if step != "notice":
                self.assertFalse(rules.sim_available(self.model, scene, self.state(step, 47)))
                self.assertEqual(harem_schedule_lint.delayed_clock_errors(scene, self.payload), [])

    def test_no_history_fabrication_and_no_new_partner_terms(self):
        notice = self.by["notice"]
        history = next(n for n in notice["Nodes"] if n["Id"] == "history")
        for known in (False, True):
            state = self.state()
            if known:
                state.flags.add("wenduag.vellexia_conflict")
            live = [c for c in history["Choices"] if rules.sim_choice_available(c, state)]
            self.assertEqual([c["Next"] for c in live], ["recall" if known else "unknown"])
        all_sets = [f for s in self.by.values() for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]]
        self.assertTrue(all(f.startswith((s49.P, s49.FRICTION)) for f in all_sets))
        self.assertFalse(any("lover" in k or "friend" in k for k in self.payload["Derived"]))
        self.assertFalse(any("partner" in f or "reconciled" in f for f in all_sets))

    def test_full_debit_retry_refusal_and_abort_never_publish_success(self):
        for step, price, node in (("handover", 150, "watch_paid"), ("retry", 200, "paid")):
            scene = self.by[step]
            choice = next(n for n in scene["Nodes"] if n["Id"] == node)["Choices"][0]
            for money in (None, 0, price - 1, price, price + 1):
                state = self.state(step)
                state.crusade_resources = None if money is None else {"Materials": money}
                before = copy.deepcopy(state.__dict__)
                def publish():
                    state.flags.update(choice["Set"])
                    state.flags.add(scene["Id"])
                    state.times.update({f: state.hour for f in choice["Set"]})
                    state.rest_spent[scene["RestAllowance"]] = 1
                self.assertEqual(rules.sim_paid_choice(self.model, scene, choice, state, publish), money is not None and money >= price)
                if money is None or money < price:
                    self.assertEqual(before, state.__dict__)
                else:
                    self.assertEqual(state.crusade_resources["Materials"], money - price)
                    self.assertIn(s49.P + "settled", state.flags)
                    self.assertFalse(rules.sim_available(self.model, scene, state))
        for scene in self.by.values():
            for node in scene["Nodes"]:
                for choice in node["Choices"]:
                    if choice["Abort"]:
                        self.assertEqual(choice["Set"], [])
        failed = next(n for n in self.by["handover"]["Nodes"] if n["Id"] == "lost")["Choices"][0]
        self.assertNotIn(s49.P + "settled", failed["Set"])
        self.assertEqual(self.by["handover"]["Nodes"][0]["Choices"][0]["Check"]["DC"], 22)

    def test_retry_uses_both_real_failure_clocks_and_stops_after_settlement(self):
        scene = self.by["retry"]
        for witness in ("handover.failed", "handover.refused"):
            state = self.state("retry")
            state.flags.discard(s49.P + "handover.failed")
            state.flags.add(s49.P + witness)
            state.times[s49.P + witness] = 53
            self.assertFalse(rules.sim_available(self.model, scene, state))
            state.times[s49.P + witness] = 52
            self.assertTrue(rules.sim_available(self.model, scene, state))
            state.flags.add(s49.P + "settled")
            self.assertFalse(rules.sim_available(self.model, scene, state))

    def test_scoped_return_cannot_override_a_new_loss_or_closure(self):
        self.payload["Relationships"]["wenduag"]["UnavailableOverrides"] = {
            "wenduag.dead": "wenduag.trickster.echo.abyss.returned_available"}
        model = rules.Model(self.payload)
        scene = next(s for s in model.scenes if s["Id"] == s49.P + "handover")
        state = self.state("handover")
        state.flags.remove("wenduag.in_party")
        state.flags.update(["wenduag.dead", "wenduag.trickster.echo.abyss.returned_available"])
        self.assertTrue(rules.sim_available(model, scene, state))
        for lost in ("wenduag.epoch_unavailable", "wenduag.closed"):
            bad = copy.deepcopy(state)
            bad.flags.add(lost)
            self.assertFalse(rules.sim_available(model, scene, bad))

    def test_respect_has_both_cost_and_other_womans_deed(self):
        for woman, other, deed, cost in (
            ("wenduag", "vellexia", "vellexia_watch_kept", "cost.vellexia_amusement_yielded"),
            ("vellexia", "wenduag", "wenduag_quarry_yielded", "cost.wenduag_kill_yielded")):
            groups = self.payload["Derived"][woman + ".harem.attitude." + other + ".respect"]
            self.assertEqual(groups, [list(s49.flags("settled", deed, cost))])

    def test_registration_is_append_only_and_does_not_pollute_global_entries(self):
        before = copy.deepcopy(self.payload)
        entries = copy.deepcopy(household.ENTRIES)
        consumers = dict(household.CONSUMERS)
        s49.register(self.payload, self.payload["Scenes"], {})
        self.assertEqual(self.payload, before)
        self.assertEqual(household.ENTRIES, entries)
        self.assertEqual(household.CONSUMERS, consumers)
        self.assertEqual([s["Id"] for s in self.payload["Scenes"]], [s49.P + x for x in ("notice", "handover", "retry")])
        self.assertTrue(all(s["Chapters"] == [5] and s["Participants"] == list(s49.PAIR)
                            and s["RestAllowance"] == "household.protected" for s in self.by.values()))

    def test_unreviewed_extension_cannot_publish_above_ceiling_or_intimacy(self):
        # W3-S49 is conditional on reviewed metadata AND a whole-arc body
        # window. Baseline registration must not manufacture either contract.
        root = Path(__file__).resolve().parents[1]
        schedule = json.loads((root / "tools/harem-schedule.json").read_text(encoding="utf-8"))
        row = schedule["rows"]["49"]
        self.assertFalse(row["rom"])
        self.assertEqual(row["ceiling"], "respect/respect")
        optional = {s49.P + step for step in ("bond", "observance", "desire", "morning")}
        self.assertFalse(optional.intersection(s["Id"] for s in self.payload["Scenes"]))
        self.assertFalse(any(k.endswith((".friend", ".lover")) for k in self.payload["Derived"]))
        for scene in self.payload["Scenes"]:
            for node in scene["Nodes"]:
                self.assertNotIn("explicit", node["Id"])
                for choice in node["Choices"]:
                    self.assertFalse(set(choice["Set"]).intersection(s49.flags(
                        "bond.both_deeds", "observance.kept", "desire.both_wanted", "morning.done")))

    def test_historical_body_and_settlement_do_not_extend_vellexias_stay(self):
        for step in self.by:
            state = self.state(step)
            state.flags.update(s49.flags("wenduag_quarry_yielded", "vellexia_watch_kept",
                                         "cost.wenduag_kill_yielded", "cost.vellexia_amusement_yielded"))
            state.flags.add("vellexia.trickster.returned")
            self.assertTrue(rules.sim_available(self.model, self.by[step], state), step)
            state.flags.add("vellexia.trickster.visited")
            self.assertIn("vellexia.trickster.in_person", state.flags)
            self.assertFalse(rules.sim_available(self.model, self.by[step], state), step)

    def test_reserved_brief_is_woman_pair_editorial_material_only(self):
        root = Path(__file__).resolve().parents[1]
        slot = s49.P + "desire.explicit.1"
        path = root / "tools/route_packs/harem/explicit_slots/blocked/wenduag_vellexia" / (slot + ".json")
        brief = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(brief["slot_id"], slot)
        self.assertEqual(brief["commander"], "absent")
        self.assertEqual(set(brief["speakers"].values()), {"Wenduag", "Vellexia"})
        self.assertIn("NON-GRAPHIC EDITORIAL INTERVAL", brief["scene"])
        self.assertFalse(any(slot == n["Id"] for s in self.payload["Scenes"] for n in s["Nodes"]))


if __name__ == "__main__":
    unittest.main()
