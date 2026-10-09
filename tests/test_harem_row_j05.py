"""J05 physical witnesses, negative histories and frozen host identities."""
import copy
import itertools
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from storylines.harem_rows import s18x, s26, z_j05_restitution as j05
from tools import rrt_verify, savecompat, voice_lock_lint

ROOT = Path(__file__).resolve().parents[1]


class MaterialRestitutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        # Isolate the three source hosts from the assembled export while
        # retaining the real presence/epoch adapters and locked route prose.
        own = {s18x.P + "account", s18x.P + "account_table", s26.P + "account"}
        cls.story["Scenes"] = [body for body in cls.story["Scenes"] if body["Id"] not in own]
        entries = cls.story["Books"]["trickster.ledger"]["Entries"]
        entries[:] = [entry for entry in entries if entry["Id"] not in
                      (s26.P + "account", s26.P + "material_relief")]
        s18x.register(cls.story, cls.story["Scenes"], {})
        s26.register(cls.story, cls.story["Scenes"], {})
        cls.before = copy.deepcopy(cls.story)
        j05.register(cls.story, cls.story["Scenes"], {})
        cls.by = {body["Id"]: body for body in cls.story["Scenes"]}
        cls.g = cls.by[s26.P + "account"]

    def state(self, *flags):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(flags)
        return state

    def node(self, key, body=None):
        return next(node for node in (body or self.g)["Nodes"] if node["Id"] == key)

    def take(self, state, node, index=0):
        choice = self.node(node)["Choices"][index]
        self.assertTrue(rrt_verify.sim_choice_available(choice, state), (node, index))
        state.flags.update(choice["Set"])
        return choice.get("Next")

    def traverse_cache(self):
        state = self.state(s26.REPLY)
        self.take(state, "start", 4)
        self.take(state, "j05_recipients")
        self.take(state, "j05_cache_offer")
        self.assertNotIn(s26.REMEDY, state.flags)
        self.take(state, "j05_cache_route")
        self.assertIn(s26.P + "cache_retrieved", state.flags)
        self.assertNotIn(s26.REMEDY, state.flags)
        self.take(state, "j05_cache_return")
        self.assertIn(s26.REMEDY, state.flags)
        self.assertNotIn(s26.P + "material_relief_verified", state.flags)
        self.take(state, "j05_cache_delivered")
        self.take(state, "remedy_reserved", 1)
        self.take(state, "j05_relief_inspected")
        return state

    def test_only_surrender_retrieval_delivery_and_inspection_finish_relief(self):
        state = self.traverse_cache()
        self.assertTrue(set(j05.G_PROOF + j05.G_DELIVERED) <= state.flags)
        self.assertNotIn(s26.P + "unsettled", state.flags)
        self.assertFalse(any("harem.attitude" in flag or "harem.reconciled" in flag
                             for flag in state.flags))

    def test_approval_native_knowledge_page_or_truce_is_not_delivery(self):
        for unrelated in ("foresight.page_taken", "gesmerha.wintersun_resolved",
                          "gesmerha.truth", "gesmerha.illusions", "jerribeth.trickster.returned",
                          "household.packet.k3.seen"):
            state = self.state(unrelated)
            self.assertFalse(rrt_verify.sim_choice_available(self.node("start")["Choices"][0], state))
            self.assertFalse(rrt_verify.sim_choice_available(
                self.node("j05_relief_inspected")["Choices"][0], state))

    def test_any_missing_physical_witness_keeps_verification_unavailable(self):
        choice = self.node("j05_relief_inspected")["Choices"][0]
        for absent in j05.G_PROOF:
            state = self.state(*(flag for flag in j05.G_PROOF if flag != absent))
            self.assertFalse(rrt_verify.sim_choice_available(choice, state), absent)
        state = self.state(s26.REMEDY)
        self.assertFalse(rrt_verify.sim_choice_available(self.node("remedy_reserved")["Choices"][1], state))
        self.assertTrue(any(rrt_verify.sim_choice_available(c, state)
                            for c in self.node("remedy_reserved")["Choices"]))

    def test_absent_tenant_cannot_surrender_a_cache(self):
        for flags in ((), (s26.RETURNED,), (s26.TENANT,), (s26.HOST,)):
            state = self.state(*flags)
            self.assertFalse(rrt_verify.sim_choice_available(self.node("start")["Choices"][4], state))
            self.assertFalse(rrt_verify.sim_choice_available(self.node("j05_cache_offer")["Choices"][0], state))
        state = self.state(s26.REPLY)
        state.flags.remove(s26.REPLY)  # loss after the directions menu opened
        self.assertFalse(rrt_verify.sim_choice_available(self.node("j05_cache_offer")["Choices"][0], state))

    def test_destroyed_clan_never_receives_supplies_or_reappears(self):
        for key, index in (("start", 4), ("j05_recipients", 0), ("j05_cache_offer", 0),
                           ("j05_cache_route", 0), ("j05_cache_return", 0),
                           ("remedy_reserved", 1), ("j05_relief_inspected", 0)):
            state = self.state(s26.REPLY, s26.CLAN_DESTROYED, *j05.G_PROOF)
            self.assertFalse(rrt_verify.sim_choice_available(self.node(key)["Choices"][index], state), key)

    def test_failed_retrieval_keeps_account_owed_and_has_no_retry(self):
        state = self.state(s26.REPLY)
        self.take(state, "j05_cache_offer")
        self.take(state, "j05_cache_route", 1)
        self.take(state, "unresolved")
        self.assertIn(s26.P + "unsettled", state.flags)
        self.assertNotIn(s26.REMEDY, state.flags)
        self.assertFalse(any(rrt_verify.sim_choice_available(self.node("start")["Choices"][i], state)
                             for i in (4, 5, 6)))

    def test_refused_carrying_does_not_deliver_or_cure_the_injury(self):
        state = self.state(s26.REPLY)
        self.take(state, "j05_cache_offer", 1)
        self.take(state, "unresolved")
        self.assertNotIn(s26.REMEDY, state.flags)
        self.assertNotIn(s26.P + "cache_retrieved", state.flags)
        writes = {flag for node in self.g["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
        self.assertFalse(any(flag.startswith(("gesmerha.", "jerribeth.")) for flag in writes))

    def test_reload_resumes_surrendered_or_retrieved_goods_without_duplicate_cost(self):
        state = self.state(s26.REPLY)
        self.take(state, "j05_cache_offer")
        state.flags = set(json.loads(json.dumps(sorted(state.flags))))
        self.assertTrue(rrt_verify.sim_choice_available(self.node("start")["Choices"][5], state))
        self.assertFalse(rrt_verify.sim_choice_available(self.node("start")["Choices"][4], state))
        self.take(state, "j05_cache_route")
        self.assertFalse(rrt_verify.sim_choice_available(self.node("start")["Choices"][5], state))
        self.assertTrue(rrt_verify.sim_choice_available(self.node("start")["Choices"][6], state))
        self.take(state, "j05_cache_return")
        self.assertFalse(rrt_verify.sim_choice_available(self.node("start")["Choices"][6], state))

    def test_later_changes_nothing_at_every_preaction_menu(self):
        for node in self.g["Nodes"]:
            for choice in node["Choices"]:
                if choice["Abort"]:
                    self.assertEqual(choice["Set"], [], node["Id"])
                    self.assertFalse(choice.get("Crusade"), node["Id"])

    def test_captivity_pending_hook_alone_cannot_buy_destruction(self):
        for sid in (s18x.P + "account", s18x.P + "account_table"):
            body = self.by[sid]
            entry = self.node("start", body)["Choices"][0]
            terminal = self.node("j05_instructions_destroyed", body)["Choices"][0]
            for absent in j05.H_PROOF:
                state = self.state(*(flag for flag in j05.H_PROOF if flag != absent))
                self.assertFalse(rrt_verify.sim_choice_available(entry, state), absent)
                self.assertFalse(rrt_verify.sim_choice_available(terminal, state), absent)
            self.assertEqual(entry["Next"], "remedy")
            self.assertTrue(rrt_verify.sim_choice_available(terminal, self.state(*j05.H_PROOF)))
            self.assertEqual(tuple(terminal["Set"]), j05.H_DELIVERED)
            self.assertFalse(any("truce" in flag or "reconciled" in flag for flag in terminal["Set"]))

    def test_blocked_surrender_has_no_live_producer(self):
        writes = {flag for body in self.story["Scenes"] for node in body["Nodes"]
                  for choice in node["Choices"] for flag in choice["Set"]}
        self.assertTrue(set(j05.H_PROOF).isdisjoint(writes))

    def test_existing_ids_order_destinations_text_and_locked_hosts_survive(self):
        self.assertEqual(savecompat.check(self.story, savecompat.inventory(self.before)), [])
        old = {body["Id"]: body for body in self.before["Scenes"]}
        self.assertEqual([body["Id"] for body in self.story["Scenes"]], list(old))
        for sid in (s18x.P + "account", s18x.P + "account_table", s26.P + "account"):
            body = self.by[sid]
            for index, node in enumerate(old[sid]["Nodes"]):
                now = body["Nodes"][index]
                self.assertEqual((now["Id"], now["Text"]), (node["Id"], node["Text"]))
                for i, choice in enumerate(node["Choices"]):
                    self.assertEqual(now["Choices"][i]["Next"], choice["Next"])
                    if (sid, node["Id"], i) == (s26.P + "account", "unresolved", 0):
                        self.assertIn("inspected", now["Choices"][i]["Text"])
                    else:
                        self.assertEqual(now["Choices"][i]["Text"], choice["Text"])
        locks = voice_lock_lint.validate_locks(json.loads(
            (ROOT / "tools/route_packs/voice_locks.json").read_text(encoding="utf-8")))

    def test_no_extra_completion_clock_currency_or_epilogue_paragraph(self):
        for sid in (s18x.P + "account", s18x.P + "account_table", s26.P + "account"):
            body = self.by[sid]
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["DelayHours"], 0)
            self.assertEqual(body["MaxChapter"], 5)
            for node in body["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                self.assertFalse(any(choice.get("Check") or choice.get("Crusade")
                                     or choice.get("Revive") for choice in node["Choices"]))

    def test_registration_is_idempotent_and_all_saved_nodes_have_safe_answers(self):
        again = copy.deepcopy(self.story)
        j05.register(again, again["Scenes"], {})
        self.assertEqual(again, self.story)
        for sid in (s18x.P + "account", s18x.P + "account_table", s26.P + "account"):
            body = self.by[sid]
            ids = {node["Id"] for node in body["Nodes"]}
            for node in body["Nodes"]:
                branches = ("gesmerha.truth", "gesmerha.illusions",
                            "gesmerha.marhevok_rules", s26.CLAN_DESTROYED)
                for history in itertools.product((False, True), repeat=len(branches)):
                    state = self.state(*(flag for flag, held in zip(branches, history) if held))
                    self.assertTrue(any(rrt_verify.sim_choice_available(choice, state)
                                        for choice in node["Choices"]), node["Id"])
                for choice in node["Choices"]:
                    self.assertTrue(choice["Next"] is None or choice["Next"] in ids)

    def test_ledger_cannot_claim_no_relief_after_verified_delivery(self):
        entries = {entry["Id"]: entry for entry in self.story["Books"]["trickster.ledger"]["Entries"]}
        self.assertIn(s26.P + "remedy.delivered", entries[s26.P + "account"]["Forbids"])
        self.assertEqual(entries[s26.P + "material_relief"]["Requires"], list(j05.G_DELIVERED))
        self.assertIn("No remedy was inspected", entries[s26.P + "account"]["Text"])
        self.assertNotIn("No remedy was delivered", entries[s26.P + "account"]["Text"])


if __name__ == "__main__":
    unittest.main()
