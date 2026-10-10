"""J04 assembled contracts, shared craft provenance and exception class sweep."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from storylines.harem_rows import s11, s12, s14, s22
from tests.harem_row_walk import walk
from tests.story_fixture import fresh_story
from tools import rrt_verify as rules, savecompat

ROOT = Path(__file__).resolve().parents[1]



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class ContractJ04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)

    def test_assembled_lesson_and_exception_rows_preserve_save_and_voice_identity(self):
        self.assertEqual(savecompat.check(self.story), [])
        for step in s12.STEPS:
            self.assertIn(step["id"], self.model.by_id)
        for sid in s22.RESERVED_IDS:
            self.assertNotIn(sid, self.model.by_id)
        self.assertFalse(any(s["Id"] in s22.RESERVED_IDS for s in self.story["Scenes"]))
        self.assertNotIn(s12.EVIDENCE["guid"], self.story.get("SeenCues", {}).values())

    def test_all_five_exception_classes_keep_primary_retry_costs_and_no_extra_tool(self):
        contracts = json.loads((ROOT / "tools/route_packs/plans/j04-contracts.json").read_text(encoding="utf-8"))
        self.assertEqual([r["row"] for r in contracts["deed_only_exceptions"]],
                         ["S01", "S03b", "S09", "S11", "S14"])
        for prefix in ("household.pair.camellia_wenduag.", "household.pair.seelah_arueshalae.fallen.",
                       "household.pair.wenduag_arueshalae.", s11.PREFIX, s14.P):
            bodies = [s for s in self.story["Scenes"] if s["Id"].startswith(prefix)
                      and s["HouseholdCategory"] == "protected"]
            self.assertEqual({s["Id"].removeprefix(prefix) for s in bodies},
                             {"settle", "retry"} if prefix.endswith(("camellia_wenduag.", "fallen."))
                             else {"settle.good", "settle.evil", "retry.good", "retry.evil"} if prefix == s11.PREFIX
                             else {"settle", "retry", "settle.table", "retry.table"})
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
                self.assertEqual(saved_answer(nodes["owned"]["Choices"], 0)["Set"], [])
                self.assertEqual(saved_answer(nodes["owned"]["Choices"], 0)["Next"], "inspection_camellia")
                self.assertEqual(saved_answer(nodes["inspection_camellia"]["Choices"], 0)["Next"], "inspection_arueshalae")
                state = rules.SimState(5, 1000)
                outcomes = walk(self, self.model, body, state)
                done = [o for o in outcomes if s11.p("settle.done") in o.flags]
                finished, = done
                self.assertIn(s11.p("deed.workbench_inspected"), finished.flags)
                self.assertEqual(finished.rest_spent["household.protected"], 1)
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
            self.assertFalse(rules.sim_choice_available(saved_answer(choices, 0), state))
            self.assertTrue(rules.sim_choice_available(saved_answer(choices, 3), state))
            self.assertEqual(saved_answer(choices, 0)["Next"], "workbench")
            self.assertEqual(saved_answer(choices, 3)["Next"], "witnessed_company")
            outcomes = walk(self, self.model, body, state)
            done = [o for o in outcomes if s11.p("company.kept") in o.flags]
            finished, = done
            self.assertEqual(finished.rest_spent["household.pair"], 1)
            self.assertNotIn(s12.P("settle.done"), finished.flags)
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
        pending = json.loads((ROOT / "tools/route_packs/plans/claude-work-queue.json").read_text(encoding="utf-8"))
        rows = [row for row in pending if row.get("ruling") in (3, 21)]
        addresses = set()
        for row in rows:
            address = row["scene"], row["node"], row.get("choice")
            self.assertNotIn(address, addresses)
            addresses.add(address)
            body = self.model.by_id[row["scene"]]
            node = next(n for n in body["Nodes"] if n["Id"] == row["node"])
            if "choice" in row:
                choice = saved_answer(node["Choices"], row["choice"])
                self.assertIn(choice.get("Next"), {None, *(n["Id"] for n in body["Nodes"])})

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.model.by_id[s11.p('settle.good')]
        choice = next(n for n in scene['Nodes'] if n['Id'] == 'owned')['Choices'][0]
        with patch.dict(choice, Next='inspection_arueshalae'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_s11_protected_success_requires_real_inspection_in_every_wrapper()


if __name__ == "__main__":
    unittest.main()
