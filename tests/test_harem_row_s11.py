"""S11 branch, attendance, clocks, ward transaction and save identity contract."""
import copy
import unittest

from storylines.harem_rows import s11
from tools import rrt_verify


class S11Tests(unittest.TestCase):
    def setUp(self):
        self.payload = {"Scenes": [], "Etudes": {}}
        s11.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.by = {s["Id"]: s for s in self.payload["Scenes"]}

    def test_registration_is_idempotent_and_preserves_existing_scenes(self):
        old = copy.deepcopy(self.payload)
        s11.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.assertEqual(self.payload, old)
        sentinel = {"Id": "old", "Nodes": [{"Id": "old", "Choices": [0, 1]}]}
        scenes = [sentinel]
        s11.register({}, scenes, {})
        self.assertIs(scenes[0], sentinel)

    def test_every_step_has_current_attendance_page_and_epoch_guards(self):
        for body in self.by.values():
            self.assertEqual(body["Participants"], ["camellia", "arueshalae"])
            self.assertEqual(body["Chapters"], [5])
            for key in ("trickster", "foresight.page_taken", "household.stance_eligible",
                        "camellia.present_now", "arueshalae.present_now", s11.p("body.camellia")):
                self.assertIn(key, body["Requires"])
            for key in ("camellia.epoch_unavailable", "arueshalae.epoch_unavailable",
                        "arueshalae_dead", "arueshalae.evil_dead", "sacrifice"):
                self.assertIn(key, body["Forbids"])
            self.assertEqual(body["ForbidOverrides"]["sacrifice"], "trickster.commander_back")
            self.assertNotIn("arueshalae_dead", body["ForbidOverrides"])
            for a, b in (s11.PAIR, s11.PAIR[::-1]):
                self.assertEqual(body["ForbidOverrides"][a + ".harem.enmity." + b],
                                 a + ".harem.reconciled." + b)

    def test_personalities_share_primary_lock_and_good_never_promotes(self):
        for branch in ("good", "evil"):
            body = self.by[s11.p("settle." + branch)]
            self.assertIn(s11.p("settle.seen"), body["Forbids"])
            self.assertIn(s11.p("ready." + branch), body["Requires"])
        self.assertIn("arueshalae.corrupted", self.by[s11.p("settle.good")]["Forbids"])
        for direction in (s11.PAIR, s11.PAIR[::-1]):
            for stage in ("friend", "lover"):
                groups = self.payload["Derived"]["%s.harem.attitude.%s.%s" % (*direction, stage)]
                self.assertTrue(all("arueshalae.corrupted" in g and s11.p("settle.evil_done") in g for g in groups))

    def test_delays_read_real_terminal_witnesses_and_charge_four_optional_steps(self):
        for step, delay, witness in (("retry.good", 48, "settle.failed"),
                                     ("retry.evil", 48, "settle.failed"),
                                     ("desire", 48, "company.kept"),
                                     ("choice", 48, "desire.named"),
                                     ("morning", 8, "choice.both_yes")):
            body = self.by[s11.p(step)]
            self.assertEqual(body["DelayHours"], delay)
            self.assertIn(s11.p(witness), body["Requires"])
        optional = [s for s in self.by.values() if s["HouseholdCategory"] == "pair"]
        self.assertEqual(len(optional), 4)
        self.assertEqual([s["Id"] for s in optional if s["HouseholdArcStart"]], [s11.p("company")])
        for body in optional:
            self.assertEqual(body["RestAllowance"], "household.pair")

    def test_scroll_only_spent_after_both_answers_and_slot_is_state_free(self):
        nodes = {n["Id"]: n for n in self.by[s11.p("choice")]["Nodes"]}
        self.assertEqual(nodes["camellia_yes"]["Choices"][0]["Next"], "arueshalae_yes")
        self.assertEqual(nodes["arueshalae_yes"]["Choices"][0]["Next"], "ward_application")
        ward = nodes["ward_application"]["Choices"][0]
        self.assertEqual(ward["RemoveItem"], s11.SCROLL)
        self.assertIn(s11.p("ward.applied_camellia"), ward["Set"])
        self.assertIn("arueshalae.ward_held", ward["Requires"])
        self.assertEqual(sum("RemoveItem" in c for n in nodes.values() for c in n["Choices"]), 1)
        self.assertEqual(nodes[s11.SLOT]["Choices"][0]["Set"], [])
        self.assertEqual(nodes[s11.SLOT]["Choices"][0]["Next"], "kept_warded")
        self.assertNotIn(s11.p("choice.both_yes"), nodes["declined"]["Choices"][0]["Set"])
        for node in nodes.values():
            self.assertTrue(any(not c["Requires"] and not c["Forbids"] for c in node["Choices"]), node["Id"])

    def test_aborts_are_pre_action_and_write_nothing(self):
        for body in self.by.values():
            for node in body["Nodes"]:
                for choice in node["Choices"]:
                    if choice["Abort"]:
                        self.assertEqual(node["Id"], "start")
                        self.assertEqual(choice["Set"], [])
                    self.assertFalse(any(".harem." in flag for flag in choice["Set"]))

    def test_simulation_no_page_no_body_later_loss_and_enmity_block_entry(self):
        story = copy.deepcopy(self.payload)
        story["Relationships"] = {rel: {"ClosedFlag": rel + ".closed", "StartedFlag": rel + ".started",
                                        "CommittedFlag": rel + ".committed", "UnavailableFlags": []}
                                  for rel in ("household", *s11.PAIR)}
        story["RestAllowances"] = {"household.protected": 2, "household.pair": 1}
        model = rrt_verify.Model(story)
        body = model.by_id[s11.p("settle.evil")]
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(body["Requires"])
        state.flags.update(["arueshalae.corrupted", "arueshalae.evil_recruited"])
        rrt_verify.sim_complete(model, state)
        self.assertTrue(rrt_verify.sim_available(model, body, state))
        for key in ("foresight.page_taken", "camellia.present_now", "arueshalae.evil_recruited"):
            changed = copy.deepcopy(state)
            changed.flags.remove(key)
            rrt_verify.sim_complete(model, changed)
            self.assertFalse(rrt_verify.sim_available(model, body, changed), key)
        for key in ("arueshalae.evil_dead", "camellia.epoch_unavailable", "camellia.closed"):
            changed = copy.deepcopy(state)
            changed.flags.update([key, "camellia.trickster.coffin_life", "arueshalae.trickster.returned"])
            rrt_verify.sim_complete(model, changed)
            self.assertFalse(rrt_verify.sim_available(model, body, changed), key)
        state.flags.add("camellia.harem.enmity.arueshalae")
        self.assertFalse(rrt_verify.sim_available(model, body, state))
        state.flags.add("arueshalae.harem.reconciled.camellia")
        self.assertFalse(rrt_verify.sim_available(model, body, state))
        state.flags.add("camellia.harem.reconciled.arueshalae")
        self.assertTrue(rrt_verify.sim_available(model, body, state))

    def test_simulation_good_history_and_performed_warmth_do_not_earn_fallen_friendship(self):
        model = rrt_verify.Model(self.payload)
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(s11.p(x) for x in s11.BASE_DEEDS)
        state.flags.update([s11.p("settle.good_done"), "arueshalae.corrupted",
                            "camellia.harem.performs.arueshalae"])
        rrt_verify.sim_complete(model, state)
        self.assertTrue(all(key in state.flags for key in s11.RESPECT))
        self.assertFalse(any(key in state.flags for key in s11.FRIENDS))
        state.flags.update(s11.p(x) for x in s11.COMPANY[1:])
        rrt_verify.sim_complete(model, state)
        self.assertFalse(any(key in state.flags for key in s11.FRIENDS))
        state.flags.add(s11.p("settle.evil_done"))
        rrt_verify.sim_complete(model, state)
        self.assertTrue(all(key in state.flags for key in s11.FRIENDS))
        state.flags.remove("arueshalae.corrupted")
        state.flags.add("arueshalae.redeemed")
        rrt_verify.sim_complete(model, state)
        self.assertFalse(any(key in state.flags for key in s11.FRIENDS))


if __name__ == "__main__":
    unittest.main()
