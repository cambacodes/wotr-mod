"""S48 graphs against the actual integration export; no shared registrations."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s48
from tools import rrt_verify as rules
from tools.harem_schedule_lint import delayed_clock_errors
from tools.savecompat import check as savecompat

ROOT = Path(__file__).resolve().parents[1]


def registered():
    payload = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
    if not any(body["Id"] == s48.P + "notice" for body in payload["Scenes"]):
        s48.register(payload, payload["Scenes"], payload["Etudes"])
    return payload


class S48Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = registered()
        cls.rows = [rules.norm_scene(s) for s in cls.payload["Scenes"] if s["Id"].startswith(s48.P)]
        cls.by = {s["Id"]: s for s in cls.rows}

    def test_savecompat_and_body_attachment(self):
        self.assertEqual(savecompat(self.payload), [])
        self.assertEqual(len(self.rows), 15)
        self.assertEqual(len(self.by), len(self.rows))
        for body in self.rows:
            self.assertEqual(body["Relationship"], "household")
            self.assertEqual(body["Chapters"], [5])
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["ParticipantWomen"], ["minagho"])
            if body["InteractionHub"] != "household.table":
                self.assertTrue(rules.household_presence_attachment(self.payload, body), body["Id"])
                self.assertNotIn("foresight.page_taken", body["Requires"])
                self.assertNotIn(s48.P + "minagho_eligible", body["Requires"])

    def test_clocks_abort_witnesses_and_no_attitude_writes(self):
        for body in self.rows:
            self.assertEqual(delayed_clock_errors(body, self.payload), [])
            root = body["Nodes"][0]
            self.assertTrue(root["Choices"][-1]["Abort"])
            for node in body["Nodes"]:
                self.assertTrue(node["Choices"], (body["Id"], node["Id"]))
                # Funds can hide a paid option; every page still has an
                # unconditional answer in all histories (including zero funds).
                self.assertTrue(any(not answer["Requires"] and not answer["Forbids"]
                                    and not answer.get("Crusade") for answer in node["Choices"]))
                self.assertFalse(node.get("Paragraphs"))
                for choice in node["Choices"]:
                    if choice["Abort"]:
                        self.assertFalse(choice["Next"])
                        self.assertFalse(choice["Set"])
                        self.assertFalse(choice.get("Crusade"))
                    for key in choice["Set"]:
                        self.assertNotIn(key, self.payload["Derived"])
                        self.assertFalse(any(word in key for word in (".enmity.", ".reconciled.", ".stance.")))
                    if choice.get("Check"):
                        self.assertEqual(choice["Check"]["DC"], 22)
                        self.assertTrue(choice["Check"]["CommanderOnly"])
                        self.assertFalse(choice["Set"])

    def test_terminal_matrix_and_wrapper_equivalence(self):
        for step in ("reply", "retry"):
            base = self.by[s48.P + step]
            for suffix in (".minagho", ".table"):
                self.assertEqual(base["Nodes"], self.by[s48.P + step + suffix]["Nodes"])
            roots = base["Nodes"][0]["Choices"]
            paid = roots[1 if step == "reply" else 0]
            self.assertEqual(paid["Set"], list(s48.success(step, True)))
            self.assertEqual(paid["Crusade"], dict(Resource="Finances", Amount=-200 if step == "reply" else -300))
            for node in base["Nodes"]:
                if node["Id"] in ("failed", "refused"):
                    for choice in node["Choices"]:
                        self.assertNotIn(s48.P + "settled", choice["Set"])
                        self.assertNotIn(s48.P + "herrax_order_withdrawn", choice["Set"])
            if step == "retry":
                self.assertIn([s48.P + "reply.failed", s48.P + "reply.refused"], base["RequiresAnyGroups"])
                self.assertIn(s48.P + "retry.seen", base["Forbids"])

    def test_target_is_current_qualified_and_history_cannot_settle(self):
        self.assertEqual(self.payload["Derived"][s48.P + "target_current"],
                         [["participant.chivarro.available", "chivarro.present_now"]])
        self.assertIn(s48.MC + "chivarro_sent_back", self.payload["DerivedForbids"][s48.P + "target_current"])
        for body in self.rows:
            self.assertNotIn("minagho_chivarro.harem.eligible", body["Requires"])
            self.assertNotIn("chivarro.dead", body["Forbids"])
            if ".historical" in body["Id"]:
                self.assertIn(s48.P + "target_current", body["Forbids"])
                choices = body["Nodes"][0]["Choices"]
                self.assertEqual(choices[0]["Set"], list(s48.flags("notice.seen", "notice.historical", "target_unprotected")))
                self.assertEqual(len(choices), 2)

    def test_page_table_enmity_and_respect_ceiling(self):
        for body in self.rows:
            if body["InteractionHub"] == "household.table":
                self.assertIn("foresight.page_taken", body["Requires"])
                self.assertIn("household.table.kept", body["Requires"])
                for edge, override in s48.EDGES.items():
                    self.assertIn(edge, body["Forbids"])
                    self.assertEqual(body["ForbidOverrides"][edge], override)
            else:
                self.assertFalse(set(s48.EDGES).intersection(body["Forbids"]))
        self.assertFalse(any("explicit" in body["Id"] for body in self.rows))
        for key in ("herrax.harem.attitude.w.minagho.respect", "minagho_chivarro.harem.attitude.minagho.herrax.respect"):
            self.assertIn(s48.P + "settled", self.payload["Derived"][key][0])

    def live_state(self, body):
        model = rules.Model(dict(self.payload, Scenes=self.rows))
        state = rules.SimState(5, 100)
        state.flags.update(body["Requires"])
        state.flags.add("trickster.ever")
        state.flags.update(group[0] for group in body["RequiresAnyGroups"])
        state.flags.add("herrax.harem.eligible")
        state.flags.update(model.composites["minagho_chivarro.harem.eligible"][0])
        seat = self.payload["SeatWomen"]["minagho"]
        state.flags.update(seat["Requires"])
        return model, state

    def test_live_page_closure_enmity_and_shared_step_clock(self):
        body = self.by[s48.P + "reply.table"]
        model, state = self.live_state(body)
        state.times[s48.P + "notice.sent"] = 53
        self.assertFalse(rules.sim_available(model, body, state))
        state.hour = 101
        self.assertTrue(rules.sim_available(model, body, state))
        for gate in ("foresight.page_taken", "trickster", "minagho.present_now", s48.P + "herrax_channel", s48.P + "target_current"):
            absent = copy.deepcopy(state)
            absent.flags.remove(gate)
            self.assertFalse(rules.sim_available(model, body, absent), gate)
        for closed in ("herrax.closed", "minachiv.closed", "minagho.epoch_unavailable"):
            absent = copy.deepcopy(state)
            absent.flags.add(closed)
            self.assertFalse(rules.sim_available(model, body, absent), closed)
        for edge, reconciled in s48.EDGES.items():
            hostile = copy.deepcopy(state)
            hostile.flags.add(edge)
            self.assertFalse(rules.sim_available(model, body, hostile))
            hostile.flags.add(reconciled)
            self.assertTrue(rules.sim_available(model, body, hostile))
        done = copy.deepcopy(state)
        done.flags.add(s48.P + "reply.seen")
        for suffix in ("", ".minagho", ".table"):
            self.assertFalse(rules.sim_available(model, self.by[s48.P + "reply" + suffix], done))

    def test_history_survives_absent_correspondent_and_private_runtime_blocker(self):
        body = self.by[s48.P + "notice.historical"]
        model, state = self.live_state(body)
        state.flags.add("herrax.closed")
        self.assertTrue(rules.sim_available(model, body, state))
        state.flags.add(s48.P + "target_current")
        self.assertFalse(rules.sim_available(model, body, state))
        # Document the existing shared bug instead of falsely certifying the
        # sheet's no-romance private channel: ParticipantsAvailable requires it.
        private = self.by[s48.P + "notice"]
        model, state = self.live_state(private)
        self.assertTrue(rules.sim_available(model, private, state))
        state.flags.remove("herrax.harem.eligible")
        self.assertFalse(rules.sim_available(model, private, state))

    def test_later_losses_withhold_current_target_even_after_earlier_return(self):
        model = rules.Model(dict(self.payload, Scenes=self.rows))
        for loss in ("chivarro.epoch_unavailable", s48.MC + "chivarro_walked", "chivarro.returned_actor_lost",
                     s48.MC + "chivarro_sent_back", s48.MC + "chivarro_declined", "minachiv.closed"):
            state = rules.SimState(5, 100)
            # Actual earned reunion/return, but a newer native loss wins.
            state.flags.update({"availability.observed", "trickster", s48.MC + "returned_chivarro",
                                s48.MC + "chivarro_in", "chivarro.dead", loss})
            rules.sim_complete(model, state)
            self.assertNotIn(s48.P + "target_current", state.flags, loss)

    def test_actual_paid_answers_recheck_and_share_completion(self):
        # Isolate the engine transaction from the separately escalated private
        # Participants eligibility defect; these are the actual row answers.
        for step, index, price in (("reply", 1, 200), ("retry", 0, 300)):
            body = copy.deepcopy(self.by[s48.P + step + ".table"])
            body.update(Participants=[], ParticipantWomen=[], Requires=[], RequiresAnyGroups=[],
                        Forbids=[s48.P + step + ".seen"])
            model = rules.Model(dict(Scenes=[body], Relationships={"household": self.payload["Relationships"]["household"]},
                                     RestAllowances=self.payload["RestAllowances"]))
            answer = body["Nodes"][0]["Choices"][index]
            for balance in (None, 0, price - 1, price, price + 19):
                state = rules.SimState(5, 100)
                state.crusade_resources = None if balance is None else {"Finances": balance}
                before = copy.deepcopy(state.__dict__)
                def publish():
                    state.flags.update(answer["Set"] + [body["Id"]])
                    state.rest_spent["household.protected"] = 1
                expected = balance is not None and balance >= price
                self.assertEqual(rules.sim_paid_choice(model, body, answer, state, publish), expected)
                if expected:
                    self.assertEqual(state.crusade_resources["Finances"], balance - price)
                    self.assertEqual(state.rest_spent["household.protected"], 1)
                    loaded = copy.deepcopy(state)
                    body["Id"] = s48.P + step
                    self.assertFalse(rules.sim_paid_choice(model, body, answer, loaded, publish))
                else:
                    self.assertEqual(state.__dict__, before)


if __name__ == "__main__":
    unittest.main()
