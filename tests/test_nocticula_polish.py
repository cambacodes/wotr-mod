"""Entrance receipts must follow the actual lodge operation, including failed UMD."""
from itertools import product
import unittest

from storylines import nocticula_continuation as route
from storylines import nocticula_acquired_harbor as acquired
from storylines.nocticula_trickster_acquisition import allowed


class LodgeReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in route.SCENES}

    def pick(self, scene, node, index, state, success=True):
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        answer = nodes[node]["Choices"][index]
        self.assertTrue(allowed(answer, state))
        state.update(answer["Set"])
        check = answer.get("Check")
        return check["Success" if success else "Failure"] if check else answer["Next"]

    def preparation(self, method):
        state = {"trickster"}
        scene = self.scenes["noct.empty_chair"]
        index = {"silent": 1, "failed": 1, "guest": 0, "announcement": 2}[method]
        node = self.pick(scene, "entrance", index, state, success=method != "failed")
        if node:
            self.pick(scene, node, 0, state)
        operation = self.scenes["noct.uninvited_guest"]
        options = [(i, c) for i, c in enumerate(operation["Nodes"][0]["Choices"])
                   if c["Next"] != "withdraw_undertaking" and allowed(c, state)]
        self.assertEqual(len(options), 1)
        node = self.pick(operation, "start", options[0][0], state)
        self.assertEqual(self.pick(operation, node, 0, state), "gallery")
        node = self.pick(operation, "gallery", 0, state)
        self.assertEqual(node, "bell")
        node = self.pick(operation, node, 1, state)
        node = self.pick(operation, node, 0, state)
        self.pick(operation, node, 0, state)
        return state

    def test_32_played_entrance_debt_house_credit_histories(self):
        report = self.scenes["noct.no_applause"]
        nodes = {n["Id"]: n for n in report["Nodes"]}
        for method, debt, house, credit in product(
                ("silent", "guest", "failed", "announcement"),
                ("denied", "purchased"), ("closed_house", "kept_house"), ("named", "private")):
            with self.subTest(method=method, debt=debt, house=house, credit=credit):
                state = self.preparation(method)
                receipts = {"noct.lodge_debt_" + debt, "noct.lodge_" + house, "noct.work_" + credit}
                self.pick(self.scenes["noct.last_buyer"], "named" if credit == "named" else "unnamed", 0, state)
                judgment = self.scenes["noct.bell_without_master"]
                node = self.pick(judgment, "judgment", int(house == "kept_house"), state)
                node = self.pick(judgment, node, 0, state)
                self.pick(judgment, node, int(debt == "purchased"), state)
                self.assertTrue(receipts <= state)
                node = self.pick(report, "start", int(house == "kept_house"), state)
                node = self.pick(report, node, 0, state)
                node = self.pick(report, node, int(debt == "purchased"), state)
                options = [(i, c) for i, c in enumerate(nodes[node]["Choices"]) if allowed(c, state)]
                self.assertEqual(len(options), 1)
                expected = {"silent": "agent", "announcement": "agent_announcement"}.get(method, "wound")
                self.assertEqual(options[0][1]["Next"], expected)
                self.assertEqual(options[0][1]["Set"], [])
                node = self.pick(report, node, options[0][0], state)
                self.assertEqual(node, expected)
                self.assertNotIn(node, {"agent", "agent_announcement", "wound"} - {expected})
                self.assertEqual(self.pick(report, node, 0, state), "wager")
                node = self.pick(report, "wager", 0 if debt == "purchased" else 2, state)
                self.assertEqual(node, "run.caught" if debt == "purchased" else "run.free")
                self.assertEqual(self.pick(report, node, 0, state), "credit")
                self.assertIn("noct.wager_won", state)
                self.assertEqual(self.pick(report, "credit", 2, state), "answer")
                self.pick(report, "answer", 0, state)
                self.assertIn("noct.lodge_consequences_finished", state)
                self.assertTrue(receipts <= state)

    def test_no_receipt_no_report_and_closures_stand(self):
        report = self.scenes["noct.no_applause"]
        for node in report["Nodes"]:
            if node["Id"] in ("debt_refused", "debt_bought"):
                self.assertFalse(any(allowed(c, {"noct.lodge_unmarked"}) for c in node["Choices"]))
        ready = set(report["Requires"])
        self.assertTrue(allowed(report, ready))
        self.assertFalse(allowed(report, ready - {"noct.lodge_judgment_finished"}))
        for blocker in ("noct.closed", "noct.dead", "noct.parent_rejected"):
            self.assertFalse(allowed(report, ready | {blocker}))
        state = self.preparation("announcement")
        self.pick(report, "start", 2, state)
        self.pick(report, "withdraw_undertaking", 0, state)
        self.assertTrue({"noct.closed", "noct.undertaking_withdrawn"} <= state)
        self.assertNotIn("noct.lodge_consequences_finished", state)

    def test_retired_copies_keep_frozen_reports_and_terminal_receipts(self):
        baseline = {s["Id"]: s for s in acquired.BASELINE["Scenes"]}
        for history in ("new", "refused", "prior"):
            clone = next(s for s in acquired.SCENES if s["Id"] == "noct.no_applause.acquired." + history)
            donor = baseline[clone["Id"]]
            self.assertEqual([n["Id"] for n in clone["Nodes"]], [n["Id"] for n in donor["Nodes"]])
            for original, copied in zip(donor["Nodes"], clone["Nodes"]):
                if original["Id"] in ("agent", "agent_announcement", "wound", "debt_refused", "debt_bought"):
                    self.assertEqual(copied, original)
            answer = next(n for n in clone["Nodes"] if n["Id"] == "answer")["Choices"][0]
            self.assertEqual(answer["Set"], ["noct.lodge_consequences_finished", "noct.no_applause"])


if __name__ == "__main__":
    unittest.main()
