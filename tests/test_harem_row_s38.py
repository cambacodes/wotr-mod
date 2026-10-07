"""S38 deed paths, current woman scope, clocks and guarded reader destinations."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines import household_pair_delamere_minagho as pair
from tools import rrt_verify as V


class SanctuaryDispatch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = V.Model(cls.story)

    def state(self, **changes):
        st = V.SimState(5, 10000)
        st.flags.update(["trickster", "household.table.kept", "delamere.trickster.returned",
                         "delamere.committed", "trickster.ever", "delamere.trickster.second_hunt_offered",
                         "delamere.trickster.told_truth", "minachiv.complete", "minachiv.future_minagho",
                         pair.ARRIVED, "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                         pair.key("open.ready"), "chivarro.dead"])
        st.flags.update(changes.get("add", []))
        st.flags.difference_update(changes.get("remove", []))
        V.sim_complete(self.model, st)
        return st

    def test_woman_scope_and_current_presence(self):
        for extra, absent, expected in [([], [], True), (["minagho.dead"], [], False),
                                       (["minagho.dead", pair.RETURNED], [], True),
                                       (["minagho.dead", pair.RETURNED, "minachiv.closed"], [], False),
                                       (["minachiv.future_chivarro"], ["minachiv.future_minagho"], False),
                                       ([], [pair.ARRIVED], False), (["inhuman"], [], False),
                                       (["delamere.closed"], [], False),
                                       ([], ["trickster"], False),
                                       ([], ["trickster.foresight.accepted", "trickster.foresight.cost.promise"], False)]:
            with self.subTest(extra=extra, absent=absent):
                st = self.state(add=extra, remove=absent)
                body = self.model.by_id[pair.key("interception")]
                self.assertEqual(V.sim_available(self.model, body, st), expected)
        st = self.state(add=["minachiv.future_two"], remove=["minachiv.future_minagho"])
        self.assertIn("minagho.harem.eligible", st.flags)
        self.assertNotIn("minagho_chivarro.harem.eligible", st.flags)

    def test_exact_terminal_deeds_and_abort(self):
        for body in pair.SCENES:
            start = body["Nodes"][0]
            self.assertTrue(start["Choices"][-1]["Abort"])
            self.assertEqual(start["Choices"][-1]["Set"], [])
            for terminal in body["Nodes"][1:]:
                choices = terminal["Choices"]
                self.assertEqual(len(choices), 1)
                self.assertEqual(choices[0]["Set"], [pair.key(f) for f in pair.WRITES[terminal["Id"]]])
                self.assertFalse(choices[0]["Abort"])
            for node in body["Nodes"]:
                for choice in node["Choices"]:
                    self.assertNotIn("Check", choice)
                    self.assertFalse(any("hepzamirah" in f or "harem.attitude" in f or "reconciled" in f
                                         or "enmity" in f for f in choice["Set"]))

    def test_row_schema_and_witness_clocks(self):
        from tools.harem_schedule_lint import delayed_clock_errors
        self.assertEqual([e for e in V.validate(self.model) if pair.PREFIX in str(e)], [])
        for body in pair.SCENES:
            self.assertEqual(delayed_clock_errors(body, self.story), [])

    def test_recovery_requires_its_own_failure_and_never_reopens_resolution(self):
        body = self.model.by_id[pair.key("repair")]
        self.assertFalse(V.sim_available(self.model, body, self.state()))
        self.assertTrue(V.sim_available(self.model, body, self.state(add=[pair.key("interception.unsettled")])))
        for closed in ("resolved", "repair.seen", "permanent_refusal"):
            self.assertFalse(V.sim_available(self.model, body, self.state(
                add=[pair.key("interception.unsettled"), pair.key(closed)])))

    def test_save_roundtrip_keeps_every_deed_and_no_seat_dependency(self):
        import json
        clone = json.loads(json.dumps(self.story))
        for body in clone["Scenes"]:
            if body["Id"].startswith(pair.PREFIX):
                self.assertEqual(body["RestAllowance"], "household.protected")
                self.assertEqual(body["Kind"], "visit")
                self.assertTrue(body["ManualOnly"])
                self.assertNotIn("Participants", body)
                self.assertNotIn("chivarro.dead", body["Forbids"])
                self.assertIn("foresight.page_taken", body["Requires"])
                self.assertEqual(body["DelayHours"], 0 if body["Id"].endswith(".open") else 48)
        # Completing the other temple docket does not produce a single S38 deed.
        st = self.state(add=["household.pair.delamere_hepzamirah.resolved"])
        self.assertNotIn(pair.key("resolved"), st.flags)

    def test_lastcall_scope_and_commander_survival(self):
        host = self.model.by_id["trickster.lastcall.page.last_word"]
        blocks = next(n for n in host["Nodes"] if n["Id"] == "page")["Paragraphs"]
        blocks = [b for b in blocks if pair.key("resolved") in b["Requires"]]
        self.assertEqual(len(blocks), 2)
        def shown(block, flags):
            return set(block["Requires"]) <= flags and not set(block["Forbids"]) & flags
        for additions, count in [([], 1), (["sacrifice"], 0),
                                  (["sacrifice", "trickster.commander_back"], 1), (["minachiv.closed"], 0),
                                  (["minagho.dead"], 0), (["minagho.dead", pair.RETURNED], 1)]:
            st = self.state(add=[pair.key("resolved"), *additions])
            # The Commander-return producer belongs to Last Call, outside S38.
            # Test its public reader input after evaluating woman attendance.
            if "trickster.commander_back" in additions:
                st.flags.add("trickster.commander_back")
            with self.subTest(additions=additions):
                self.assertEqual(sum(shown(b, st.flags) for b in blocks), count)
        self.assertTrue(all("minagho_chivarro.harem.eligible" not in b["Requires"] for b in blocks))
        entries = self.story["Books"]["trickster.ledger"]["Entries"]
        ledger = next(e for e in entries if e["Id"] == pair.key("reader.ledger"))
        for cost in pair.COST_TEXT:
            self.assertTrue(any(pair.key(cost) in b["Requires"] for b in ledger["Lines"]))

    def test_append_preserves_every_old_scene_node_and_answer(self):
        from storylines import foresight
        before = fresh_story()
        before["Scenes"] = [s for s in before["Scenes"] if not s["Id"].startswith(pair.PREFIX)]
        for scene in before["Scenes"]:
            for node in scene["Nodes"]:
                node["Paragraphs"] = [p for p in node.get("Paragraphs", [])
                                      if not p.get("Label", "").startswith(pair.PREFIX)]
        entries = before["Books"]["trickster.ledger"]["Entries"]
        entries[:] = [e for e in entries if not e["Id"].startswith(pair.PREFIX)]
        after = copy.deepcopy(before)
        consumers = dict(foresight.CONSUMERS)
        try:
            pair.integrate(after)
        finally:
            foresight.CONSUMERS.clear()
            foresight.CONSUMERS.update(consumers)
        old_ids = [s["Id"] for s in before["Scenes"]]
        for flag, groups in before["Derived"].items():
            self.assertEqual(after["Derived"][flag], groups)
        self.assertEqual(old_ids, [s["Id"] for s in after["Scenes"][:len(old_ids)]])
        for old, new in zip(before["Scenes"], after["Scenes"]):
            self.assertEqual([n["Id"] for n in old["Nodes"]], [n["Id"] for n in new["Nodes"]])
            for a, b in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(a["Choices"], b["Choices"])


if __name__ == "__main__":
    unittest.main()
