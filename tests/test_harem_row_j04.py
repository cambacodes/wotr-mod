"""J04 assembled contracts, shared craft provenance and exception class sweep."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s11, s12, s14, s22
from tests.harem_row_walk import walk
from tests.story_fixture import fresh_story
from tools import rrt_verify as rules, savecompat, voice_lock_lint

ROOT = Path(__file__).resolve().parents[1]


class ContractJ04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)

    def test_assembled_lesson_and_exception_rows_preserve_save_and_voice_identity(self):
        self.assertEqual(savecompat.check(self.story), [])
        locks = json.loads((ROOT / "tools/route_packs/voice_locks.json").read_text(encoding="utf-8"))
        self.assertEqual(voice_lock_lint.check(self.story, locks["locked"]), ({}, []))
        for step in s12.STEPS:
            self.assertIn(step["id"], self.model.by_id)
        for sid in s22.RESERVED_IDS:
            self.assertNotIn(sid, self.model.by_id)
        self.assertEqual(s22.STATUS, "not activated")
        self.assertNotIn(s12.EVIDENCE["guid"], self.story.get("SeenCues", {}).values())

    def test_all_five_exception_classes_keep_primary_retry_costs_and_no_extra_tool(self):
        contracts = json.loads((ROOT / "tools/route_packs/plans/j04-contracts.json").read_text(encoding="utf-8"))
        self.assertEqual([r["row"] for r in contracts["deed_only_exceptions"]],
                         ["S01", "S03b", "S09", "S11", "S14"])
        for prefix in ("household.pair.camellia_wenduag.", "household.pair.seelah_arueshalae.fallen.",
                       "household.pair.wenduag_arueshalae.", s11.PREFIX, s14.P):
            bodies = [s for s in self.story["Scenes"] if s["Id"].startswith(prefix)
                      and s["HouseholdCategory"] == "protected"]
            self.assertEqual(len(bodies), 2 if prefix.endswith(("camellia_wenduag.", "fallen.")) else 4)
            for body in bodies:
                self.assertEqual(body["RestAllowance"], "household.protected")
                retry = ".retry" in body["Id"]
                self.assertEqual(body["DelayHours"], 48 if retry else 0)
                self.assertIn(prefix + ("settle.failed" if retry else "settle.seen"),
                              body["Requires"] if retry else body["Forbids"])
                self.assertEqual(set(body["ParticipantContacts"]), set(body["Pair"]))
                for node in body["Nodes"]:
                    self.assertFalse(node.get("Paragraphs"))
                    for choice in node["Choices"]:
                        self.assertFalse(any(choice.get(k) for k in ("Check", "Crusade", "RemoveItem", "Revive")))
                        if choice["Abort"]:
                            self.assertEqual(node["Id"], "start")
                            self.assertEqual(choice["Set"], [])

    def test_s11_protected_success_requires_real_inspection_in_every_wrapper(self):
        for retry in (False, True):
            for branch in ("good", "evil"):
                sid = s11.p(("retry." if retry else "settle.") + branch)
                body = self.model.by_id[sid]
                nodes = {n["Id"]: n for n in body["Nodes"]}
                self.assertEqual(nodes["owned"]["Choices"][0]["Set"], [])
                self.assertEqual(nodes["owned"]["Choices"][0]["Next"], "inspection_camellia")
                self.assertEqual(nodes["inspection_camellia"]["Choices"][0]["Next"], "inspection_arueshalae")
                state = rules.SimState(5, 1000)
                outcomes = walk(self, self.model, body, state)
                done = [o for o in outcomes if s11.p("settle.done") in o.flags]
                self.assertEqual(len(done), 1)
                self.assertIn(s11.p("deed.workbench_inspected"), done[0].flags)
                self.assertEqual(done[0].rest_spent["household.protected"], 1)
                for outcome in outcomes:
                    rules.sim_complete(self.model, outcome)
                    if s11.p("deed.workbench_inspected") in outcome.flags:
                        self.assertIn(s12.SHARED_CRAFT_WITNESS, outcome.flags)
                    else:
                        self.assertNotIn(s12.SHARED_CRAFT_WITNESS, outcome.flags)
                    self.assertNotIn(s12.P("settle.done"), outcome.flags)

    def test_s11_company_reuses_witness_with_saved_choice_and_no_second_preparation(self):
        body = self.model.by_id[s11.p("company")]
        for source in (s12.DEED_COSTS, (s11.p("deed.workbench_inspected"),)):
            state = rules.SimState(5, 1000)
            state.flags.update(source)
            rules.sim_complete(self.model, state)
            self.assertIn(s12.SHARED_CRAFT_WITNESS, state.flags)
            choices = body["Nodes"][0]["Choices"]
            self.assertFalse(rules.sim_choice_available(choices[0], state))
            self.assertTrue(rules.sim_choice_available(choices[3], state))
            self.assertEqual(choices[0]["Next"], "workbench")
            self.assertEqual(choices[3]["Next"], "witnessed_company")
            outcomes = walk(self, self.model, body, state)
            done = [o for o in outcomes if s11.p("company.kept") in o.flags]
            self.assertEqual(len(done), 1)
            self.assertEqual(done[0].rest_spent["household.pair"], 1)
            self.assertNotIn(s12.P("settle.done"), done[0].flags)
        state = rules.SimState(5, 1000)
        state.flags.add(s12.P("deed.camellia_correction"))
        rules.sim_complete(self.model, state)
        self.assertNotIn(s12.SHARED_CRAFT_WITNESS, state.flags)

    def test_s14_asymmetry_needs_exact_deeds_and_matching_enmity_overrides(self):
        for missing in s14.DEEDS:
            state = rules.SimState(5, 1000)
            state.flags.update(set(s14.DEEDS) - {missing})
            rules.sim_complete(self.model, state)
            self.assertNotIn("galfrey.harem.attitude.arueshalae.respect", state.flags)
            self.assertNotIn("arueshalae.harem.attitude.galfrey.friend", state.flags)
        # Minimal views isolate the approved deed logic from route eligibility.
        isolated = {"Derived": copy.deepcopy(s14.STAGES), "DerivedForbids": {}, "Scenes": []}
        model = rules.Model(isolated)
        state = rules.SimState(5, 1000)
        state.flags.update(s14.DEEDS)
        rules.sim_complete(model, state)
        self.assertIn("galfrey.harem.attitude.arueshalae.respect", state.flags)
        self.assertIn("arueshalae.harem.attitude.galfrey.friend", state.flags)
        self.assertFalse(any(f.endswith(".lover") for f in state.flags))

    def test_every_new_pending_text_has_an_exact_manifest_address(self):
        pending = json.loads((ROOT / "tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        rows = [r for r in pending if r.get("ruling") in (3, 21)]
        self.assertGreaterEqual(len(rows), 15)
        addresses = {(row["scene"], row["node"], row.get("choice")) for row in rows}
        for row in rows:
            body = self.model.by_id[row["scene"]]
            node = next(n for n in body["Nodes"] if n["Id"] == row["node"])
            text = node["Choices"][row["choice"]]["Text"] if "choice" in row else node["Text"]
            self.assertTrue(text, row)  # Voice-owner completion may replace the placeholder.
        for body in self.story["Scenes"]:
            if not body["Id"].startswith((s11.PREFIX, s12.PREFIX)):
                continue
            for node in body["Nodes"]:
                for index, text in [(None, node["Text"])] + [
                        (i, choice["Text"]) for i, choice in enumerate(node["Choices"])]:
                    if text.startswith("[PROSE PENDING:"):
                        self.assertIn((body["Id"], node["Id"], index), addresses)


if __name__ == "__main__":
    unittest.main()
