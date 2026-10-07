"""S50 contract tests, including the shared no-romance attendance blocker."""
import copy
import json
from pathlib import Path
import sys
import unittest
from tests.story_fixture import fresh_story

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from storylines.harem_rows import s50
from storylines import contract_j01
from tools import rrt_verify as rules, savecompat
from tools.harem_schedule_lint import delayed_clock_errors


class S50Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story(include_harem=False)
        cls.before = savecompat.inventory(cls.story)
        s50.register(cls.story, cls.story["Scenes"], cls.story["Etudes"])
        contract_j01.install(cls.story)
        cls.model = rules.Model(cls.story)
        cls.rows = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(s50.P)}

    def row(self, step, body="widow"):
        return self.rows[s50.P + step + "." + body]

    def state(self, scene, hour=100):
        state = rules.SimState(5, hour)
        state.flags.update(scene["Requires"])
        state.flags.update((s50.N + "hatched", s50.N + "egg_owed", s50.RENOUNCED,
                            "trickster.ever", "nidalynn.harem.eligible"))
        if scene["RequiresAnyGroups"]:
            state.flags.add(scene["RequiresAnyGroups"][0][0])
        state.flags.add("nidalynn.present_now")
        state.available_contacts = {scene["ContactUnit"]}
        state.times.update({f: 0 for f in state.flags})
        return state

    def test_body_attachment_save_references_and_registration(self):
        self.assertEqual(len(self.rows), 6)
        self.assertEqual(rules.validate(self.model), [])
        self.assertEqual(savecompat.check(self.story, self.before), [])
        for scene in self.rows.values():
            self.assertTrue(rules.household_presence_attachment(self.story, scene))
            self.assertEqual(scene["Relationship"], "household")
            self.assertEqual(scene["Participants"], ["nidalynn"])
            self.assertFalse(scene["Remote"])
            self.assertEqual(scene["Chapters"], [5])
            self.assertEqual(delayed_clock_errors(scene, self.story), [])
            self.assertNotIn("foresight.page_taken", scene["Requires"])
        count = len(self.story["Scenes"])
        s50.register(self.story, self.story["Scenes"], self.story["Etudes"])
        self.assertEqual(len(self.story["Scenes"]), count)

    def test_ready_uses_actual_saved_child_and_never_a_derived_clock(self):
        self.assertEqual(self.story["Derived"][s50.P + "ready"],
                         [[s50.N + "hatched", s50.N + "egg_owed"]])
        for source in ("lamp_black", "vault", "straw"):
            scene = next(s for s in self.model.scenes if s["Id"] == s50.N + "eggs." + source)
            kept = [c for n in scene["Nodes"] for c in n["Choices"] if s50.N + "egg_owed" in c["Set"]]
            self.assertTrue(kept, source)
        for scene in self.rows.values():
            if scene["DelayHours"]:
                self.assertNotIn(s50.P + "ready", scene["Requires"])

    def test_stable_root_indices_and_abort_do_not_write(self):
        for step, count in (("notice", 3), ("custody", 4), ("repair", 3)):
            scene = self.row(step)
            choices = scene["Nodes"][0]["Choices"]
            self.assertEqual(len(choices), count)
            self.assertTrue(choices[-1]["Abort"])
            self.assertEqual(choices[-1]["Set"], [])
            self.assertIsNone(choices[-1]["Next"])
        check = self.row("custody")["Nodes"][0]["Choices"][0]
        self.assertEqual(check["Check"], dict(Skill="SkillAthletics", DC=18,
                                            Success="delivered", Failure="spilled", CommanderOnly=True))
        self.assertEqual(check["Set"], [])

    def test_cost_readers_are_epilogue_only_and_do_not_mend_fixed_hostility(self):
        for scene in self.rows.values():
            self.assertFalse(any(node.get("Paragraphs") for node in scene["Nodes"]))
        for sid in (s50.N + "epilogue.salt", s50.N + "epilogue.late",
                    "nidalynn.lastcall.page", "trickster.lastcall.page.last_word"):
            host = next(s for s in self.story["Scenes"] if s["Id"] == sid)
            paragraphs = [p for p in host["Nodes"][0]["Paragraphs"] if s50.P + "resolved" in p["Requires"]]
            self.assertEqual(len(paragraphs), 1, sid)
            self.assertIn(s50.P + "cost.nidalynn_guard_night", paragraphs[0]["Requires"])
            self.assertIn(s50.P + "cost.nidalynn_own_feed", paragraphs[0]["Requires"])
        ledger = next(e for e in self.story["Books"]["trickster.ledger"]["Entries"]
                      if e["Id"] == s50.P + "custody.record")
        self.assertEqual(ledger["Requires"], [s50.P + "notice.seen"])
        self.assertEqual(len(ledger["Lines"]), 3)

    def test_bill_debt_and_unnamed_histories_select_one_truthful_answer(self):
        node = next(n for n in self.row("notice")["Nodes"] if n["Id"] == "account")
        for flags, expected in (([], 2), ([s50.DEBT], 1), ([s50.BILL], 0), ([s50.BILL, s50.DEBT], 0)):
            state = rules.SimState(5, 0); state.flags.update(flags)
            self.assertEqual([i for i, c in enumerate(node["Choices"]) if rules.sim_choice_available(c, state)], [expected])

    def test_remedies_require_route_renunciation_and_do_not_change_diet_or_stance(self):
        for scene in self.rows.values():
            for node in scene["Nodes"]:
                for choice in node["Choices"]:
                    self.assertTrue(all(flag.startswith(s50.P) for flag in choice["Set"]))
                    self.assertFalse(any(word in flag for flag in choice["Set"]
                                         for word in ("attitude", "enmity", "reconciled", "lover", "fed_goats", "fed_demons", "fed_rats")))
        scene = self.row("custody"); state = self.state(scene)
        state.flags.remove(s50.RENOUNCED)
        self.assertEqual([rules.sim_choice_available(c, state) for c in scene["Nodes"][0]["Choices"]],
                         [False, False, True, True])
        failure = next(n for n in scene["Nodes"] if n["Id"] == "spilled")["Choices"][0]
        self.assertNotIn(s50.P + "resolved", failure["Set"])
        self.assertNotIn(s50.P + "feed_delivered", failure["Set"])

    def test_private_attendance_works_unromanced_with_table_closed(self):
        scene = self.row("notice"); state = self.state(scene)
        self.assertTrue(rules.sim_available(self.model, scene, state))
        state.flags.remove("nidalynn.harem.eligible")
        state.flags.add("household.closed")
        self.assertTrue(rules.sim_available(self.model, scene, state))
        self.assertNotIn("foresight.page_taken", state.flags)
        state.available_contacts.clear()
        self.assertFalse(rules.sim_available(self.model, scene, state))
        self.assertFalse(any("harem.eligible" in c["Set"] for s in self.rows.values()
                             for n in s["Nodes"] for c in n["Choices"]))

    def test_current_body_closure_epoch_delay_and_shared_step_witness(self):
        for body in s50.BODIES:
            scene = self.row("custody", body); state = self.state(scene)
            state.times[s50.P + "notice.opened"] = 53
            self.assertFalse(rules.sim_available(self.model, scene, state))
            state.hour = 101
            self.assertTrue(rules.sim_available(self.model, scene, state))
            for veto in ("nidalynn.closed", s50.N + "left_with_it", "nidalynn.epoch_unavailable",
                         "trickster.failed", s50.P + "custody.seen", s50.N + "lie_kept"):
                state.flags.add(veto)
                self.assertFalse(rules.sim_available(self.model, scene, state), veto)
                state.flags.remove(veto)
            if body == "widow":
                state.flags.add(s50.N + "form_chosen")
            else:
                state.flags.remove(s50.N + "form_chosen")
            self.assertFalse(rules.sim_available(self.model, scene, state))
        repair = self.row("repair", "chosen")
        for predecessor in ("custody.failed", "custody.refused"):
            state = self.state(repair); state.flags.difference_update(repair["RequiresAnyGroups"][0])
            state.flags.add(s50.P + predecessor); state.times[s50.P + predecessor] = 52
            self.assertTrue(rules.sim_available(self.model, repair, state))
            state.flags.add(s50.P + "repair.seen")
            self.assertFalse(rules.sim_available(self.model, repair, state))

    def test_shared_delay_clock_body_change_blocker(self):
        for step, predecessor in (("custody", "notice.opened"), ("repair", "custody.failed")):
            scene = self.row(step, "chosen"); state = self.state(scene)
            state.times[s50.P + predecessor] = 52
            self.assertTrue(rules.sim_available(self.model, scene, state))
            # The shared clock currently includes all Requires timestamps. A later
            # body choice incorrectly restarts a docket whose predecessor is 48h old.
            state.times[s50.N + "form_chosen"] = 99
            self.assertFalse(rules.sim_available(self.model, scene, state))

    def test_actual_paid_terminals_full_debit_replay_and_failure_matrix(self):
        for step, node_id, price in (("custody", "hire", 100), ("repair", "start", 150)):
            scene = self.row(step)
            choice = next(n for n in scene["Nodes"] if n["Id"] == node_id)["Choices"][0]
            for funds in (None, 0, price - 1, price, price + 73):
                state = self.state(scene)
                state.crusade_resources = None if funds is None else {"Materials": funds}
                before = copy.deepcopy(state.__dict__)
                def publish():
                    state.flags.update(choice["Set"] + [scene["Id"]])
                    state.times.update({f: state.hour for f in choice["Set"] + [scene["Id"]]})
                    state.rest_spent["household.protected"] = 1
                success = funds is not None and funds >= price
                self.assertEqual(rules.sim_paid_choice(self.model, scene, choice, state, publish), success)
                if success:
                    self.assertEqual(state.crusade_resources["Materials"], funds - price)
                    self.assertIn(s50.P + "feed_delivered", state.flags)
                    self.assertFalse(rules.sim_paid_choice(self.model, scene, choice, state, publish))
                    other = self.row(step, "chosen"); state.flags.add(s50.N + "form_chosen")
                    self.assertFalse(rules.sim_available(self.model, other, state))
                else:
                    self.assertEqual(state.__dict__, before)
            for veto in ("nidalynn.closed", "nidalynn.epoch_unavailable", "allowance", "kingdom", "balance"):
                state = self.state(scene); state.crusade_resources = {"Materials": price}
                if veto == "allowance": state.rest_spent["household.protected"] = 2
                elif veto == "kingdom": state.crusade_resources = None
                elif veto == "balance": state.crusade_resources["Materials"] -= 1
                else: state.flags.add(veto)
                before = copy.deepcopy(state.__dict__)
                self.assertFalse(rules.sim_paid_choice(self.model, scene, choice, state, lambda: state.flags.update(choice["Set"])))
                self.assertEqual(state.__dict__, before)


if __name__ == "__main__":
    unittest.main()
